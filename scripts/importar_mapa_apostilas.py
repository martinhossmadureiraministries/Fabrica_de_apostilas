#!/usr/bin/env python3
"""Extrai o mapa oficial de apostilas da EBE para JSONL estruturado.

Entrada esperada: EBE_Mapa_Completo_Apostilas-2.pdf
Saída: generated/manifests/mapa_apostilas.jsonl

Cada linha JSON representa uma apostila com a hierarquia:
Nível → Instituto → Escola → Curso → Módulo → Apostila.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Iterable

try:
    from pypdf import PdfReader
except Exception as exc:  # pragma: no cover
    raise SystemExit(
        "Dependência ausente: instale pypdf. Ex.: pip install -r requirements.txt"
    ) from exc

HEADER_PREFIXES = (
    "Escola Bíblica Epignósis · Mapa de Apostilas",
    "EBE-PLAN-APO",
    "Conhecer a Deus.",
    "DOCUMENTO DE PLANEAMENTO",
    "Mapa Completo de Apostilas",
    "Títulos e Temas",
    "Documento institucional",
    "Edição de trabalho",
    "Martinho S.",
)


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text or "sem-titulo"


def clean_line(line: str) -> str:
    line = re.sub(r"\s+", " ", line).strip()
    # OCR/PDF extraction por vezes cola a numeração à apostila: 100.Título
    line = re.sub(r"^(\d+)\.\s*", r"\1. ", line)
    return line


def iter_pdf_lines(pdf_path: Path) -> Iterable[str]:
    reader = PdfReader(str(pdf_path))
    for page in reader.pages:
        text = page.extract_text() or ""
        for raw in text.splitlines():
            line = clean_line(raw)
            if not line:
                continue
            if any(line.startswith(prefix) for prefix in HEADER_PREFIXES):
                continue
            # Número de página isolado ou ruído de capa/índice.
            if re.fullmatch(r"\d+", line):
                continue
            yield line


def parse_map(lines: Iterable[str]) -> list[dict]:
    nivel = instituto = escola = curso = modulo = None
    nivel_num = instituto_num = modulo_num = None
    curso_carga_horaria = None
    records: list[dict] = []
    started = False

    re_nivel = re.compile(r"^(?:NÍVEL|Nível)\s+(\d+)\s+—\s+(.+)$")
    re_instituto = re.compile(r"^Instituto\s+(\d+)\s+—\s+(.+)$")
    re_curso = re.compile(r"^Curso:\s*(.+?)\s*·\s*Carga horária:\s*(?:≈\s*)?([0-9]+)\s*h\s*$")
    re_modulo = re.compile(r"^Módulo\s+(\d+)\s+—\s+(.+)$")
    re_apostila = re.compile(r"^(\d+)\.\s*(.+)$")

    for line in lines:
        m = re_nivel.match(line)
        if m:
            nivel_num = int(m.group(1))
            nivel = f"Nível {nivel_num} — {m.group(2).strip()}"
            instituto = escola = curso = modulo = None
            started = True
            continue

        if not started:
            continue

        m = re_instituto.match(line)
        if m:
            instituto_num = int(m.group(1))
            instituto = m.group(2).strip()
            escola = curso = modulo = None
            continue

        # Só consideramos escolas dentro do corpo curricular, não no índice.
        if line.startswith("Escola ") and not line.startswith("Escola Bíblica"):
            escola = line.strip()
            curso = modulo = None
            continue

        m = re_curso.match(line)
        if m:
            curso = m.group(1).strip()
            curso_carga_horaria = int(m.group(2))
            modulo = None
            continue

        m = re_modulo.match(line)
        if m:
            modulo_num = int(m.group(1))
            modulo = m.group(2).strip()
            continue

        m = re_apostila.match(line)
        if m and all([nivel, instituto, escola, curso, modulo]):
            numero = int(m.group(1))
            titulo = m.group(2).strip()
            codigo = f"EBE-APO-{numero:04d}"
            records.append(
                {
                    "numero": numero,
                    "codigo": codigo,
                    "titulo": titulo,
                    "nivel_numero": nivel_num,
                    "nivel": nivel,
                    "instituto_numero": instituto_num,
                    "instituto": instituto,
                    "escola": escola,
                    "curso": curso,
                    "curso_carga_horaria": curso_carga_horaria,
                    "modulo_numero": modulo_num,
                    "modulo": modulo,
                    "slug": slugify(f"{codigo}-{titulo}"),
                    "path_partes": {
                        "nivel": slugify(nivel or ""),
                        "instituto": slugify(instituto or ""),
                        "escola": slugify(escola or ""),
                        "curso": slugify(curso or ""),
                        "modulo": slugify(f"modulo-{modulo_num}-{modulo}"),
                    },
                }
            )
            continue

    return records


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default="EBE_Mapa_Completo_Apostilas-2.pdf", help="PDF do mapa oficial")
    ap.add_argument("--saida", default="generated/manifests/mapa_apostilas.jsonl", help="JSONL de saída")
    ap.add_argument("--esperado", type=int, default=1029, help="Total esperado de apostilas")
    ap.add_argument("--allow-partial", action="store_true", help="Não falhar se a contagem divergir")
    args = ap.parse_args(argv)

    pdf = Path(args.pdf)
    if not pdf.exists():
        raise SystemExit(f"PDF não encontrado: {pdf}")

    records = parse_map(iter_pdf_lines(pdf))
    if len(records) != args.esperado and not args.allow_partial:
        raise SystemExit(
            f"Contagem inválida: extraídas {len(records)} apostilas; esperado {args.esperado}. "
            "Use --allow-partial apenas para diagnóstico."
        )

    out = Path(args.saida)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    resumo = {
        "apostilas": len(records),
        "niveis": len({r["nivel"] for r in records}),
        "institutos": len({r["instituto"] for r in records}),
        "escolas": len({r["escola"] for r in records}),
        "cursos": len({r["curso"] for r in records}),
        "modulos": len({(r["curso"], r["modulo_numero"], r["modulo"]) for r in records}),
        "saida": str(out),
    }
    print(json.dumps(resumo, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
