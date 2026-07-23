#!/usr/bin/env python3
"""Gera apostilas EBE em lote com Gemini + Groq, preservando identidade visual.

Fluxo recomendado:
1) scripts/importar_mapa_apostilas.py cria o manifesto JSONL com 1.029 itens.
2) Este script filtra por nível/instituto/escola/curso/módulo e gera lotes pequenos.
3) Gemini pode redigir a apostila; Groq pode planear/revisar; modo offline permite teste.

As apostilas geradas são artefactos de build e ficam em generated/ por padrão.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import textwrap
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import requests
import yaml

# Permite importar _estilos.py a partir da raiz quando este script é executado de scripts/.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _estilos import (  # noqa: E402
    Cm,
    COR_PRIMARIA,
    COR_SECUNDARIA,
    FONTE_CORPO,
    FONTE_TITULO,
    HEX_SECUNDARIA,
    Pt,
    WD_ALIGN_PARAGRAPH,
    WD_TABLE_ALIGNMENT,
    _add_horizontal_line,
    _shade_cell,
    add_marco_filosofico,
    citacao,
    h1,
    h2,
    h3,
    inserir_logo,
    lista,
    novo_documento,
    page_break,
    paragrafo,
    selo_final,
)


@dataclass
class AIConfig:
    gemini_api_key: str | None
    groq_api_key: str | None
    gemini_model: str = "gemini-1.5-flash"
    groq_model: str = "llama-3.1-8b-instant"
    temp_plan: float = 0.45
    temp_write: float = 0.72
    temp_review: float = 0.2


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text or "sem-titulo"


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", text.lower()).strip()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def read_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def extract_json(text: str) -> Any:
    """Extrai JSON mesmo quando o modelo responde com fences markdown."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start_obj = text.find("{")
        start_arr = text.find("[")
        starts = [x for x in (start_obj, start_arr) if x >= 0]
        if not starts:
            raise
        start = min(starts)
        end = max(text.rfind("}"), text.rfind("]"))
        if end <= start:
            raise
        return json.loads(text[start : end + 1])


def json_hash(data: Any) -> str:
    payload = json.dumps(data, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


class AIClient:
    def __init__(self, cfg: AIConfig, timeout: int = 120, retries: int = 2):
        self.cfg = cfg
        self.timeout = timeout
        self.retries = retries

    def gemini(self, prompt: str, temperature: float) -> str:
        if not self.cfg.gemini_api_key:
            raise RuntimeError("GEMINI_API_KEY não configurada nos secrets/ambiente.")
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{self.cfg.gemini_model}:generateContent?key={self.cfg.gemini_api_key}"
        )
        body = {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": temperature, "responseMimeType": "application/json"},
        }
        return self._post_json(url, body, headers={}, provider="gemini")

    def groq(self, prompt: str, temperature: float) -> str:
        if not self.cfg.groq_api_key:
            raise RuntimeError("GROQ_API_KEY não configurada nos secrets/ambiente.")
        url = "https://api.groq.com/openai/v1/chat/completions"
        body = {
            "model": self.cfg.groq_model,
            "temperature": temperature,
            "response_format": {"type": "json_object"},
            "messages": [
                {
                    "role": "system",
                    "content": "Responda sempre em JSON válido, sem markdown, em Português europeu/Angola.",
                },
                {"role": "user", "content": prompt},
            ],
        }
        headers = {"Authorization": f"Bearer {self.cfg.groq_api_key}"}
        return self._post_json(url, body, headers=headers, provider="groq")

    def _post_json(self, url: str, body: dict[str, Any], headers: dict[str, str], provider: str) -> str:
        headers = {"Content-Type": "application/json", **headers}
        last_exc: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                resp = requests.post(url, json=body, headers=headers, timeout=self.timeout)
                if resp.status_code in {429, 500, 502, 503, 504} and attempt < self.retries:
                    time.sleep(8 * (attempt + 1))
                    continue
                resp.raise_for_status()
                data = resp.json()
                if provider == "gemini":
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                return data["choices"][0]["message"]["content"]
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
                if attempt < self.retries:
                    time.sleep(5 * (attempt + 1))
                    continue
        raise RuntimeError(f"Falha ao chamar {provider}: {last_exc}")


SCHEMA_HINT = """
JSON obrigatório:
{
  "subtitulo": "string curta",
  "ideia_unica": "string",
  "palavras_chave": ["..."],
  "apresentacao": ["2-4 parágrafos"],
  "objectivos": {"conhecer":"...", "crer":"...", "viver":"...", "servir":"..."},
  "versiculo_chave": {"texto":"texto bíblico curto ou paráfrase fiel", "referencia":"Livro 1.1"},
  "texto_base": "Referência bíblica principal",
  "introducao": ["2-4 parágrafos"],
  "desenvolvimento": [
    {"titulo":"Fundamento bíblico", "paragrafos":["..."], "citacoes":[{"texto":"...", "referencia":"..."}]},
    {"titulo":"Desenvolvimento doutrinário", "paragrafos":["..."], "citacoes":[]},
    {"titulo":"Dúvidas e equívocos comuns", "paragrafos":["..."], "citacoes":[]},
    {"titulo":"Quadro de destaque", "paragrafos":["síntese memorável"], "citacoes":[]}
  ],
  "aplicacoes": ["vida pessoal", "família", "igreja local", "trabalho/sociedade", "ministério"],
  "sintese": "parágrafo conclusivo pastoral",
  "exercicios": {
    "compreensao": ["5 perguntas"],
    "reflexao": ["3 perguntas"],
    "ministerio": ["3 tarefas práticas"]
  },
  "estudo_biblico_complementar": {"passagem":"...", "orientacoes":["..."]},
  "glossario": [{"termo":"...", "definicao":"..."}],
  "bibliografia": ["Bíblia Sagrada, ARC", "..."]
}
"""


def context_prompt(item: dict[str, Any]) -> str:
    return f"""
Hierarquia curricular:
- Código: {item['codigo']}
- Título da apostila: {item['titulo']}
- Nível: {item['nivel']}
- Instituto: {item['instituto']}
- Escola: {item['escola']}
- Curso: {item['curso']} ({item.get('curso_carga_horaria', '')} h)
- Módulo {item['modulo_numero']}: {item['modulo']}

Identidade obrigatória:
- Escola Bíblica Epignósis (EBE)
- Lema: Conhecer a Deus. Viver a Palavra. Manifestar o Reino.
- Língua: Português europeu/Angola (pt-PT)
- Versão bíblica de referência: Almeida Revista e Corrigida (ARC)
- Tom: académico formal, bíblico, pastoral, didáctico, confessional cristão evangélico.
- Eixos pedagógicos: Conhecer, Crer, Viver, Servir.
""".strip()


def prompt_outline(item: dict[str, Any]) -> str:
    return f"""
Crie um PLANO ÚNICO para uma apostila da Escola Bíblica Epignósis.
{context_prompt(item)}

O plano deve impedir conteúdo genérico e repetido. Defina um ângulo exclusivo para esta apostila, termos-chave,
textos bíblicos adequados e uma progressão pedagógica coerente com o curso e o módulo.

Responda apenas JSON:
{{
  "ideia_unica": "...",
  "limites_do_tema": ["o que entra", "o que não entra"],
  "palavras_chave": ["..."],
  "textos_biblicos": ["..."],
  "seccoes": ["..."],
  "riscos_de_repeticao": ["..."],
  "criterios_de_qualidade": ["..."]
}}
""".strip()


def prompt_write(item: dict[str, Any], outline: dict[str, Any] | None) -> str:
    return f"""
Redija o conteúdo integral de uma apostila oficial da Escola Bíblica Epignósis.
{context_prompt(item)}

Plano/ângulo aprovado:
{json.dumps(outline or {}, ensure_ascii=False, indent=2)}

Regras:
1. O conteúdo deve condizer claramente com o título, curso e módulo.
2. Não use blocos genéricos que serviriam para qualquer apostila.
3. Não repita parágrafos; varie exemplos, aplicações e perguntas.
4. Preserve linguagem pt-PT/Angola: acção, objectivo, baptismo, ministério, etc.
5. Use citações bíblicas curtas e referências; não invente referências.
6. Inclua os eixos Conhecer, Crer, Viver e Servir nos objectivos.
7. A apostila deve ter densidade suficiente para 10-15 páginas quando diagramada.
8. Responda apenas JSON válido no formato abaixo.

{SCHEMA_HINT}
""".strip()


def prompt_review(item: dict[str, Any], content: dict[str, Any]) -> str:
    sample = json.dumps(content, ensure_ascii=False)[:12000]
    return f"""
Revise a apostila abaixo como revisor pedagógico e doutrinário da EBE.
{context_prompt(item)}

Conteúdo JSON parcial/integral:
{sample}

Avalie coerência título-conteúdo, adequação bíblica, estrutura institucional, repetição e prontidão para gerar DOCX.
Responda apenas JSON:
{{
  "aprovado": true,
  "pontuacao": 0.0,
  "problemas": ["..."],
  "melhorias_obrigatorias": ["..."],
  "termos_esperados_presentes": ["..."],
  "parecer": "..."
}}
""".strip()


def offline_content(item: dict[str, Any]) -> dict[str, Any]:
    """Conteúdo determinístico para teste sem API; útil para validar workflow e DOCX."""
    titulo = item["titulo"]
    curso = item["curso"]
    modulo = item["modulo"]
    escola = item["escola"]
    instituto = item["instituto"]
    base = (
        f"Esta apostila estuda {titulo} dentro do módulo {modulo}, no curso {curso}. "
        f"O objectivo é conduzir o aluno a compreender o tema com fidelidade bíblica, "
        f"discernimento espiritual e aplicação prática na igreja local."
    )
    return {
        "subtitulo": f"Uma abordagem bíblica e formativa em {curso}",
        "ideia_unica": f"Aplicar {titulo} ao percurso formativo de {modulo}, evitando tratamento genérico.",
        "palavras_chave": [w for w in re.findall(r"[A-Za-zÀ-ÿ]{4,}", titulo)[:8]] + [curso, modulo],
        "apresentacao": [
            base,
            f"Na arquitectura da EBE, esta unidade pertence a {instituto}, {escola}, e prepara o estudante para crescer nos eixos Conhecer, Crer, Viver e Servir.",
            "O tratamento do tema é introdutório, mas pastoralmente exigente: o aluno deve terminar com convicções bíblicas, linguagem clara e práticas concretas.",
        ],
        "objectivos": {
            "conhecer": f"Identificar os fundamentos bíblicos de {titulo}.",
            "crer": f"Assumir uma convicção cristã madura acerca de {titulo}.",
            "viver": f"Aplicar {titulo} à vida devocional, familiar e comunitária.",
            "servir": f"Usar o aprendizado de {titulo} para edificar a igreja local.",
        },
        "versiculo_chave": {
            "texto": "Procura apresentar-te a Deus aprovado, como obreiro que não tem de que se envergonhar.",
            "referencia": "2 Timóteo 2.15",
        },
        "texto_base": "2 Timóteo 2.15; Efésios 4.11-16",
        "introducao": [
            f"O tema {titulo} não deve ser estudado de modo isolado. Ele pertence ao módulo {modulo} e responde a necessidades reais de formação cristã.",
            "A EBE entende que o conhecimento verdadeiro transforma mente, coração e vida. Por isso, cada conceito é tratado com base bíblica, reflexão doutrinária e aplicação ministerial.",
            f"Ao longo desta apostila, o estudante será convidado a relacionar {titulo} com a sua caminhada de fé, a sua igreja local e o serviço ao Reino de Deus.",
        ],
        "desenvolvimento": [
            {
                "titulo": "Fundamentos bíblicos",
                "paragrafos": [
                    f"A Escritura é o ponto de partida para compreender {titulo}. Nenhuma prática cristã deve ser sustentada apenas por tradição, experiência ou preferência pessoal.",
                    "O estudante deve perguntar: que textos bíblicos iluminam este assunto? Que princípios permanentes emergem desses textos? Como a igreja deve responder hoje?",
                    f"No contexto de {curso}, esta abordagem protege o aluno de conclusões apressadas e fortalece uma espiritualidade submetida à Palavra.",
                ],
                "citacoes": [
                    {"texto": "Toda a Escritura é divinamente inspirada e proveitosa para ensinar.", "referencia": "2 Timóteo 3.16"}
                ],
            },
            {
                "titulo": "Desenvolvimento doutrinário",
                "paragrafos": [
                    f"Doutrinariamente, {titulo} deve ser definido com precisão. Uma definição clara evita confusão, superficialidade e usos indevidos do conceito.",
                    "A boa doutrina não é mera informação; ela orienta adoração, carácter, decisões e missão. Por isso, o aluno deve ligar verdade aprendida e vida obediente.",
                    f"Dentro do módulo {modulo}, este tema contribui para a maturidade progressiva do estudante e prepara conteúdos posteriores do percurso.",
                ],
                "citacoes": [],
            },
            {
                "titulo": "Dúvidas e equívocos comuns",
                "paragrafos": [
                    f"Um equívoco comum é tratar {titulo} como assunto secundário, sem relação com a formação integral do discípulo. Na verdade, o tema toca convicções e práticas.",
                    "Outro risco é confundir aplicação contextual com relativização bíblica. A aplicação pode mudar de forma, mas deve preservar o princípio revelado nas Escrituras.",
                    "A EBE recomenda que o aluno discuta dúvidas com o docente, compare textos bíblicos e evite conclusões baseadas em frases isoladas.",
                ],
                "citacoes": [],
            },
            {
                "titulo": "Quadro de destaque",
                "paragrafos": [
                    f"Para reter: {titulo} deve conduzir o aluno a conhecer melhor a Deus, viver a Palavra com fidelidade e servir com maturidade no Reino."
                ],
                "citacoes": [],
            },
        ],
        "aplicacoes": [
            f"Na vida devocional, ore pedindo discernimento para viver {titulo} com sinceridade.",
            "Na família, transforme o aprendizado em conversas, reconciliação e exemplo cristão.",
            "Na igreja local, procure edificar outros com humildade e fidelidade bíblica.",
            "No trabalho e na sociedade, manifeste carácter cristão coerente com a verdade estudada.",
            f"No ministério, use {titulo} para servir pessoas, não para exibir conhecimento.",
        ],
        "sintese": f"Estudar {titulo} é responder ao chamado de unir conhecimento bíblico, fé obediente, vida transformada e serviço frutífero. O aluno deve guardar o princípio central, praticá-lo e partilhá-lo com responsabilidade.",
        "exercicios": {
            "compreensao": [
                f"Como definiria {titulo} em uma frase clara?",
                "Quais textos bíblicos fundamentam melhor o tema?",
                f"Qual é a ligação entre {titulo} e o módulo {modulo}?",
                "Que erro comum deve ser evitado?",
                "Como os eixos Conhecer, Crer, Viver e Servir aparecem nesta apostila?",
            ],
            "reflexao": [
                f"Que convicção pessoal precisa ser corrigida ou fortalecida sobre {titulo}?",
                "Onde este ensino confronta hábitos actuais da sua vida?",
                "Como este tema pode ser ensinado a um novo convertido?",
            ],
            "ministerio": [
                "Prepare uma breve partilha de cinco minutos sobre o conceito central.",
                "Converse com um líder ou mentor sobre uma aplicação prática desta lição.",
                "Escreva uma oração de compromisso relacionada ao tema.",
            ],
        },
        "estudo_biblico_complementar": {
            "passagem": "Efésios 4.11-16",
            "orientacoes": [
                "Observe o propósito da edificação do Corpo de Cristo.",
                "Identifique sinais de maturidade apresentados no texto.",
                f"Relacione a passagem com {titulo}.",
            ],
        },
        "glossario": [
            {"termo": "Epignósis", "definicao": "Conhecimento pleno, relacional e transformador de Deus."},
            {"termo": "Aplicação", "definicao": "Passagem da verdade compreendida para a obediência concreta."},
            {"termo": "Discernimento", "definicao": "Capacidade de julgar ideias e práticas à luz das Escrituras."},
        ],
        "bibliografia": [
            "Bíblia Sagrada, Almeida Revista e Corrigida (ARC).",
            "Documentos Institucionais Oficiais da Escola Bíblica Epignósis.",
            "Manual do Aluno da Escola Bíblica Epignósis.",
        ],
    }


def generate_content(item: dict[str, Any], client: AIClient, mode: str) -> tuple[dict[str, Any], dict[str, Any]]:
    meta: dict[str, Any] = {"mode": mode, "outline_provider": None, "writer_provider": None, "review_provider": None}
    if mode == "offline":
        content = offline_content(item)
        meta["review"] = {"aprovado": True, "pontuacao": 0.75, "parecer": "Modo offline para teste técnico."}
        return content, meta

    outline = None
    if mode in {"gemini_groq", "groq"}:
        outline = extract_json(client.groq(prompt_outline(item), client.cfg.temp_plan))
        meta["outline_provider"] = "groq"
    elif mode == "gemini":
        outline = extract_json(client.gemini(prompt_outline(item), client.cfg.temp_plan))
        meta["outline_provider"] = "gemini"

    if mode in {"gemini_groq", "gemini"}:
        content = extract_json(client.gemini(prompt_write(item, outline), client.cfg.temp_write))
        meta["writer_provider"] = "gemini"
    elif mode == "groq":
        content = extract_json(client.groq(prompt_write(item, outline), client.cfg.temp_write))
        meta["writer_provider"] = "groq"
    else:
        raise ValueError(f"Modo inválido: {mode}")

    try:
        if mode in {"gemini_groq", "groq"}:
            review = extract_json(client.groq(prompt_review(item, content), client.cfg.temp_review))
            meta["review_provider"] = "groq"
        else:
            review = extract_json(client.gemini(prompt_review(item, content), client.cfg.temp_review))
            meta["review_provider"] = "gemini"
        meta["review"] = review
    except Exception as exc:  # noqa: BLE001
        meta["review_error"] = str(exc)
        meta["review"] = {"aprovado": None, "pontuacao": None, "problemas": [str(exc)]}
    return content, meta


def flatten_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(flatten_text(v) for v in value)
    if isinstance(value, dict):
        return "\n".join(flatten_text(v) for v in value.values())
    return ""


def ngrams(text: str, n: int = 5) -> set[str]:
    words = re.findall(r"[a-zà-ÿ0-9]+", norm(text))
    return {" ".join(words[i : i + n]) for i in range(max(0, len(words) - n + 1))}


def validate_local(item: dict[str, Any], content: dict[str, Any], previous: list[set[str]], min_chars: int, max_sim: float) -> dict[str, Any]:
    text = flatten_text(content)
    issues: list[str] = []
    if len(text) < min_chars:
        issues.append(f"Conteúdo curto: {len(text)} caracteres; mínimo {min_chars}.")

    required = ["apresentacao", "objectivos", "introducao", "desenvolvimento", "exercicios", "glossario", "bibliografia"]
    for key in required:
        if key not in content:
            issues.append(f"Campo obrigatório ausente: {key}.")

    title_terms = [t for t in re.findall(r"[a-zà-ÿ]{4,}", norm(item["titulo"])) if t not in {"para", "como", "deus"}]
    matched = [t for t in title_terms if t in norm(text)]
    if title_terms and len(matched) / max(1, len(title_terms)) < 0.5:
        issues.append("Poucos termos do título aparecem no conteúdo.")

    paragraphs = [p.strip() for p in re.split(r"\n+", text) if len(p.strip()) > 80]
    duplicates = len(paragraphs) - len(set(paragraphs))
    if duplicates > 1:
        issues.append(f"Parágrafos repetidos detectados: {duplicates}.")

    gram = ngrams(text)
    max_found = 0.0
    for other in previous:
        if not gram or not other:
            continue
        sim = len(gram & other) / len(gram | other)
        max_found = max(max_found, sim)
    if max_found > max_sim:
        issues.append(f"Similaridade alta com apostila anterior do lote: {max_found:.2f} > {max_sim:.2f}.")

    return {
        "aprovado_local": not issues,
        "problemas_local": issues,
        "caracteres": len(text),
        "termos_titulo": title_terms,
        "termos_titulo_encontrados": matched,
        "similaridade_maxima_lote": round(max_found, 4),
        "fingerprint": json_hash(content),
        "ngrams": gram,
    }


def add_table_key_values(doc, rows: list[tuple[str, str]]) -> None:
    tbl = doc.add_table(rows=len(rows), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (k, v) in enumerate(rows):
        c0, c1 = tbl.rows[i].cells
        c0.text = k
        c1.text = v
        _shade_cell(c0, "E8F1EC")
        for p in c0.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.name = FONTE_TITULO
                r.font.size = Pt(10)
                r.font.color.rgb = COR_PRIMARIA
        for p in c1.paragraphs:
            for r in p.runs:
                r.font.name = FONTE_CORPO
                r.font.size = Pt(10)


def render_docx(item: dict[str, Any], content: dict[str, Any], out_path: Path, author: str = "Escola Bíblica Epignósis") -> None:
    codigo = item["codigo"]
    titulo = item["titulo"]
    doc = novo_documento(titulo, codigo)

    doc.add_paragraph()
    logo = ROOT / "logo_ebe.png"
    if logo.exists():
        inserir_logo(doc, str(logo), largura_cm=6.0)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Conhecer a Deus. Viver a Palavra. Manifestar o Reino.")
    r.font.name = FONTE_TITULO
    r.font.size = Pt(10)
    r.font.italic = True
    r.font.color.rgb = COR_SECUNDARIA
    p = doc.add_paragraph()
    _add_horizontal_line(p, color=HEX_SECUNDARIA, size=6)

    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(item["instituto"].upper())
    r.font.name = FONTE_TITULO
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"{item['escola']} · Curso {item['curso']} · Módulo {item['modulo_numero']} — {item['modulo']}")
    r.font.name = FONTE_CORPO
    r.font.size = Pt(10)

    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"APOSTILA N.º {item['numero']:04d}")
    r.font.name = FONTE_TITULO
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(titulo)
    r.font.name = FONTE_TITULO
    r.font.size = Pt(28)
    r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA
    if content.get("subtitulo"):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(str(content["subtitulo"]))
        r.font.name = FONTE_TITULO
        r.font.size = Pt(13)
        r.font.italic = True

    for _ in range(2):
        doc.add_paragraph()
    add_table_key_values(
        doc,
        [
            ("Autor / Docente", author),
            ("Carga horária estimada", "1–3 horas de estudo"),
            ("Nível formativo", item["nivel"]),
            ("Código institucional", codigo),
            ("Edição / Ano", "1.ª edição — 2026"),
        ],
    )
    doc.add_paragraph()
    p = doc.add_paragraph()
    _add_horizontal_line(p, color=HEX_SECUNDARIA, size=4)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Material didáctico oficial · Escola Bíblica Epignósis · 2026")
    r.font.name = FONTE_CORPO
    r.font.size = Pt(9)
    page_break(doc)

    add_marco_filosofico(doc)

    h1(doc, "Ficha Técnica")
    paragrafo(
        doc,
        "Este material didáctico é propriedade intelectual da Escola Bíblica Epignósis (EBE), produzido "
        "para uso no âmbito dos seus programas de formação. A sua reprodução depende de autorização institucional escrita.",
    )
    lista(
        doc,
        [
            f"Título da apostila: {titulo}",
            f"Código institucional: {codigo}",
            f"Instituto: {item['instituto']}",
            f"Escola: {item['escola']}",
            f"Curso: {item['curso']}",
            f"Módulo: {item['modulo_numero']} — {item['modulo']}",
            "Versão bíblica de referência: Almeida Revista e Corrigida (ARC).",
        ],
    )
    citacao(
        doc,
        "Toda a Escritura é divinamente inspirada e proveitosa para ensinar, para redarguir, para corrigir, para instruir em justiça.",
        "2 Timóteo 3.16",
    )
    page_break(doc)

    h1(doc, "Sumário")
    lista(
        doc,
        [
            "Apresentação da apostila",
            "Objectivos de aprendizagem",
            "Versículo-chave e texto-base",
            "1. Introdução",
            "2. Desenvolvimento do conceito central",
            "3. Aplicação prática",
            "4. Síntese e conclusão",
            "Exercícios de revisão",
            "Estudo bíblico complementar",
            "Glossário",
            "Bibliografia recomendada",
        ],
    )
    page_break(doc)

    h1(doc, "Apresentação da Apostila")
    for ptxt in content.get("apresentacao", []):
        paragrafo(doc, str(ptxt))

    h1(doc, "Objectivos de Aprendizagem")
    paragrafo(doc, "Ao concluir o estudo desta apostila, o aluno será capaz de:")
    obj = content.get("objectivos", {}) or {}
    lista(
        doc,
        [
            f"Conhecer — {obj.get('conhecer', '')}",
            f"Crer — {obj.get('crer', '')}",
            f"Viver — {obj.get('viver', '')}",
            f"Servir — {obj.get('servir', '')}",
        ],
        ordenada=True,
    )

    h1(doc, "Versículo-Chave")
    vc = content.get("versiculo_chave", {}) or {}
    citacao(doc, str(vc.get("texto", "")), str(vc.get("referencia", "")))
    h1(doc, "Texto-Base para Leitura")
    paragrafo(doc, str(content.get("texto_base", "")), bold=True, justify=False)
    page_break(doc)

    h1(doc, "Introdução", numero=1)
    for ptxt in content.get("introducao", []):
        paragrafo(doc, str(ptxt))

    h1(doc, "Desenvolvimento do Conceito Central", numero=2)
    for idx, sec in enumerate(content.get("desenvolvimento", []), start=1):
        h2(doc, str(sec.get("titulo", f"Secção {idx}")), numero=f"2.{idx}")
        for ptxt in sec.get("paragrafos", []):
            paragrafo(doc, str(ptxt))
        for c in sec.get("citacoes", []) or []:
            citacao(doc, str(c.get("texto", "")), str(c.get("referencia", "")))

    page_break(doc)
    h1(doc, "Aplicação Prática", numero=3)
    lista(doc, [str(x) for x in content.get("aplicacoes", [])], ordenada=True)

    h1(doc, "Síntese e Conclusão", numero=4)
    paragrafo(doc, str(content.get("sintese", "")))

    page_break(doc)
    h1(doc, "Exercícios de Revisão")
    ex = content.get("exercicios", {}) or {}
    h3(doc, "I — Verifique a sua compreensão")
    lista(doc, [str(x) for x in ex.get("compreensao", [])], ordenada=True)
    h3(doc, "II — Reflita diante de Deus")
    lista(doc, [str(x) for x in ex.get("reflexao", [])], ordenada=True)
    h3(doc, "III — Aplique no ministério")
    lista(doc, [str(x) for x in ex.get("ministerio", [])], ordenada=True)

    h1(doc, "Estudo Bíblico Complementar")
    eb = content.get("estudo_biblico_complementar", {}) or {}
    paragrafo(doc, f"Passagem: {eb.get('passagem', '')}", bold=True, justify=False)
    lista(doc, [str(x) for x in eb.get("orientacoes", [])])

    h1(doc, "Glossário")
    gloss = content.get("glossario", []) or []
    if gloss:
        tbl = doc.add_table(rows=1, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.rows[0].cells[0].text = "Termo"
        tbl.rows[0].cells[1].text = "Definição"
        for cell in tbl.rows[0].cells:
            _shade_cell(cell, "E8F1EC")
        for item_gloss in gloss:
            row = tbl.add_row().cells
            row[0].text = str(item_gloss.get("termo", ""))
            row[1].text = str(item_gloss.get("definicao", ""))

    h1(doc, "Bibliografia Recomendada")
    lista(doc, [str(x) for x in content.get("bibliografia", [])])
    selo_final(doc)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)


def match_filter(value: str, expected: str | None) -> bool:
    if not expected:
        return True
    return norm(expected) in norm(value)


def output_path(base: Path, item: dict[str, Any]) -> Path:
    parts = item["path_partes"]
    filename = f"{item['codigo']}_{slugify(item['titulo'])}.docx"
    return base / parts["nivel"] / parts["instituto"] / parts["escola"] / parts["curso"] / parts["modulo"] / filename


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config/gerador_apostilas.yml")
    ap.add_argument("--manifest", default="generated/manifests/mapa_apostilas.jsonl")
    ap.add_argument("--saida", default=None)
    ap.add_argument("--inicio", type=int, default=1, help="Número inicial da apostila, ex.: 1")
    ap.add_argument("--limite", type=int, default=3, help="Quantidade máxima a gerar no lote")
    ap.add_argument("--nivel", default=None)
    ap.add_argument("--instituto", default=None)
    ap.add_argument("--escola", default=None)
    ap.add_argument("--curso", default=None)
    ap.add_argument("--modulo", default=None)
    ap.add_argument("--provider-mode", choices=["gemini_groq", "gemini", "groq", "offline"], default="offline")
    ap.add_argument("--dry-run", action="store_true", help="Só mostra o plano do lote; não chama IA nem gera DOCX")
    ap.add_argument("--offline-if-missing", action="store_true", help="Usa modo offline se secrets de IA ausentes")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--retries", type=int, default=2)
    args = ap.parse_args(argv)

    cfg_raw = read_config(ROOT / args.config)
    ai_raw = cfg_raw.get("ia", {})
    quality_raw = cfg_raw.get("qualidade", {})
    out_base = Path(args.saida or cfg_raw.get("saida", {}).get("pasta_base", "generated/apostilas"))
    if not out_base.is_absolute():
        out_base = ROOT / out_base

    manifest = Path(args.manifest)
    if not manifest.is_absolute():
        manifest = ROOT / manifest
    records = load_jsonl(manifest)

    selected = [
        r
        for r in records
        if r["numero"] >= args.inicio
        and match_filter(r["nivel"], args.nivel)
        and match_filter(r["instituto"], args.instituto)
        and match_filter(r["escola"], args.escola)
        and match_filter(r["curso"], args.curso)
        and match_filter(r["modulo"], args.modulo)
    ][: args.limite]

    print(json.dumps({"selecionadas": len(selected), "limite": args.limite, "modo": args.provider_mode}, ensure_ascii=False))
    for r in selected:
        print(f"- {r['codigo']} | {r['instituto']} > {r['escola']} > {r['curso']} > M{r['modulo_numero']} | {r['titulo']}")

    if args.dry_run:
        return 0

    mode = args.provider_mode
    gemini_key = os.getenv(ai_raw.get("gemini_api_key_env", "GEMINI_API_KEY"))
    groq_key = os.getenv(ai_raw.get("groq_api_key_env", "GROQ_API_KEY"))
    if mode == "gemini_groq" and (not gemini_key or not groq_key) and args.offline_if_missing:
        print("Secrets de IA ausentes; alternando para modo offline por --offline-if-missing.")
        mode = "offline"
    elif mode == "gemini" and not gemini_key and args.offline_if_missing:
        print("GEMINI_API_KEY ausente; alternando para modo offline por --offline-if-missing.")
        mode = "offline"
    elif mode == "groq" and not groq_key and args.offline_if_missing:
        print("GROQ_API_KEY ausente; alternando para modo offline por --offline-if-missing.")
        mode = "offline"

    if mode == "gemini_groq" and (not gemini_key or not groq_key):
        raise SystemExit("Modo gemini_groq exige GEMINI_API_KEY e GROQ_API_KEY nos secrets do GitHub Actions.")
    if mode == "gemini" and not gemini_key:
        raise SystemExit("Modo gemini exige GEMINI_API_KEY nos secrets do GitHub Actions.")
    if mode == "groq" and not groq_key:
        raise SystemExit("Modo groq exige GROQ_API_KEY nos secrets do GitHub Actions.")

    ai_cfg = AIConfig(
        gemini_api_key=gemini_key,
        groq_api_key=groq_key,
        gemini_model=os.getenv("GEMINI_MODEL") or ai_raw.get("gemini_model", "gemini-1.5-flash"),
        groq_model=os.getenv("GROQ_MODEL") or ai_raw.get("groq_model", "llama-3.1-8b-instant"),
        temp_plan=float(ai_raw.get("temperatura_planeamento", 0.45)),
        temp_write=float(ai_raw.get("temperatura_redaccao", 0.72)),
        temp_review=float(ai_raw.get("temperatura_revisao", 0.2)),
    )
    client = AIClient(ai_cfg, timeout=args.timeout, retries=args.retries)

    min_chars = int(quality_raw.get("minimo_caracteres", 6500)) if mode != "offline" else 2500
    max_sim = float(quality_raw.get("similaridade_maxima_jaccard", 0.32))
    index_path = ROOT / cfg_raw.get("saida", {}).get("indice_qualidade", "generated/indices/qualidade.jsonl")
    index_path.parent.mkdir(parents=True, exist_ok=True)
    cache_dir = ROOT / "generated" / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    previous_ngrams: list[set[str]] = []
    generated: list[str] = []

    for item in selected:
        print(f"\nGerando {item['codigo']} — {item['titulo']}")
        cache_file = cache_dir / f"{item['codigo']}.json"
        if cache_file.exists():
            bundle = json.loads(cache_file.read_text(encoding="utf-8"))
            content = bundle["content"]
            meta = bundle.get("meta", {"cache": True})
            print("  usando cache JSON")
        else:
            content, meta = generate_content(item, client, mode)
            cache_file.write_text(json.dumps({"item": item, "content": content, "meta": meta}, ensure_ascii=False, indent=2), encoding="utf-8")

        local = validate_local(item, content, previous_ngrams, min_chars=min_chars, max_sim=max_sim)
        previous_ngrams.append(local.pop("ngrams"))
        out = output_path(out_base, item)
        render_docx(item, content, out)
        generated.append(str(out.relative_to(ROOT)))

        quality_record = {
            "codigo": item["codigo"],
            "titulo": item["titulo"],
            "arquivo": str(out.relative_to(ROOT)),
            "modo": mode,
            "meta": meta,
            "qualidade_local": local,
            "gerado_em": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        with index_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(quality_record, ensure_ascii=False) + "\n")
        print(f"  DOCX: {out.relative_to(ROOT)}")
        if not local["aprovado_local"]:
            print("  aviso qualidade:", "; ".join(local["problemas_local"]))

    summary_path = ROOT / "generated" / "ultima_execucao.json"
    summary_path.write_text(
        json.dumps({"geradas": generated, "quantidade": len(generated), "modo": mode}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({"geradas": len(generated), "resumo": str(summary_path.relative_to(ROOT))}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
