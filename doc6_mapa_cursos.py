"""DOC 6 — Mapa Oficial de Cursos"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def _tabela_escola(doc, nome_escola, cursos):
    h3(doc, nome_escola)
    tbl = doc.add_table(rows=1, cols=1)
    hdr = tbl.rows[0].cells
    hdr[0].text = ""
    r = hdr[0].paragraphs[0].add_run("Cursos")
    r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
    _shade_cell(hdr[0], "2E7D4F")
    for c in cursos:
        row = tbl.add_row().cells
        row[0].text = c
        for p in row[0].paragraphs:
            for run in p.runs:
                run.font.name = FONTE_CORPO; run.font.size = Pt(11)


def gerar():
    doc = novo_documento("Mapa Oficial de Cursos", "EBE-DOC-006")
    add_capa(doc,
        supratitulo="Documento Institucional N.º 6",
        titulo="Mapa Oficial de Cursos",
        subtitulo="Os Dez Institutos, Trinta e Quatro Escolas e a Trilha Formativa Epignósis",
        codigo="EBE-DOC-006", ano="2026")
    add_marco_filosofico(doc)

    h1(doc, "Sumário")
    lista(doc, [
        "1. Apresentação e Lógica do Mapa",
        "2. Os Quatro Níveis Formativos",
        "3. Nível 1 — Discípulo (Conhecer)",
        "4. Nível 2 — Crescimento (Ser)",
        "5. Nível 3 — Servir (Ministério)",
        "6. Nível 4 — Multiplicação (Reino)",
        "7. Estrutura Padrão (Apostila → Instituto)",
        "8. Volume Total Realista",
        "9. Diferencial Final Epignósis",
        "10. Resultado Final do Mapa",
    ])
    page_break(doc)

    h1(doc, "Apresentação e Lógica do Mapa", numero=1)
    paragrafo(doc,
        "O Mapa de Cursos da Escola Bíblica Epignósis apresenta o plano "
        "curricular completo da instituição, distribuído em quatro níveis "
        "formativos progressivos e dez institutos. Articula-se com a "
        "Arquitectura Oficial (EBE-DOC-005), a Duração Oficial (EBE-DOC-007) "
        "e o Sistema de Pré-Requisitos (EBE-DOC-008).")
    paragrafo(doc,
        "A lógica que sustenta o mapa é a do crescimento espiritual e "
        "ministerial integrado: o aluno avança do conhecimento dos "
        "fundamentos da fé até à multiplicação de ministérios.")
    citacao(doc, "Como meninos novamente nascidos, desejai afectuosamente o leite racional, não falsificado, para que por ele vades crescendo.", "1 Pedro 2.2")

    h1(doc, "Os Quatro Níveis Formativos", numero=2)
    tbl = doc.add_table(rows=1, cols=3)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Nível", "Verbo-chave", "Objectivo formativo"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    niveis = [
        ("1 — Discípulo",     "CONHECER",       "Fundamentos da fé cristã."),
        ("2 — Crescimento",   "SER",            "Maturidade espiritual e doutrinária."),
        ("3 — Servir",        "MINISTÉRIO",     "Capacitação ministerial prática."),
        ("4 — Multiplicação", "REINO",          "Formação de líderes e multiplicadores."),
    ]
    for n in niveis:
        row = tbl.add_row().cells
        for i, v in enumerate(n):
            row[i].text = v
            for p in row[i].paragraphs:
                for run in p.runs:
                    run.font.name = FONTE_CORPO; run.font.size = Pt(11)

    # === NÍVEL 1 ===
    h1(doc, "Nível 1 — Discípulo (Conhecer)", numero=3)
    paragrafo(doc, "Objectivo: estabelecer fundamentos sólidos da fé cristã.")

    h2(doc, "Instituto 1 — Formação Cristã")
    _tabela_escola(doc, "Escola de Fundamentos da Fé", [
        "Salvação e Novo Nascimento", "Arrependimento e Fé",
        "Baptismo e Ceia", "Identidade em Cristo",
    ])
    _tabela_escola(doc, "Escola de Vida Cristã", [
        "Santidade", "Oração Devocional", "Leitura Bíblica", "Vida de Obediência",
    ])
    _tabela_escola(doc, "Escola de Discipulado", [
        "Seguir a Cristo", "Vida de Discípulo", "Crescimento Espiritual",
    ])

    h2(doc, "Instituto 2 — Ciências Bíblicas (Base)")
    _tabela_escola(doc, "Escola de Panorama Bíblico", [
        "Panorama do Antigo Testamento", "Panorama do Novo Testamento",
    ])
    _tabela_escola(doc, "Escola de Introdução aos Livros Bíblicos", [
        "Pentateuco", "Evangelhos", "Epístolas",
    ])
    _tabela_escola(doc, "Escola de História Bíblica", [
        "História de Israel", "História da Igreja Primitiva",
    ])

    # === NÍVEL 2 ===
    h1(doc, "Nível 2 — Crescimento (Ser)", numero=4)
    paragrafo(doc, "Objectivo: aprofundar a maturidade espiritual e doutrinária.")

    h2(doc, "Instituto 3 — Ciências Teológicas")
    _tabela_escola(doc, "Escola ABC da Teologia", [
        "Doutrinas Básicas", "Natureza de Deus",
    ])
    _tabela_escola(doc, "Escola de Teologia Sistemática", [
        "Deus (Teontologia)", "Cristo (Cristologia)", "Espírito Santo (Pneumatologia)",
        "Salvação (Soteriologia)", "Igreja (Eclesiologia)", "Fim dos Tempos (Escatologia)",
    ])
    _tabela_escola(doc, "Escola de Hermenêutica Bíblica", [
        "Interpretação Bíblica", "Contexto Bíblico", "Erros de Interpretação",
    ])

    h2(doc, "Instituto 4 — Formação Espiritual")
    _tabela_escola(doc, "Escola de Oração", [
        "Vida de Oração", "Intercessão", "Oração Bíblica",
    ])
    _tabela_escola(doc, "Escola do Espírito Santo", [
        "Baptismo no Espírito Santo", "Dons Espirituais", "Fruto do Espírito",
    ])
    _tabela_escola(doc, "Escola de Santidade", [
        "Carácter Cristão", "Vida Santa", "Maturidade Espiritual",
    ])

    # === NÍVEL 3 ===
    h1(doc, "Nível 3 — Servir (Ministério)", numero=5)
    paragrafo(doc, "Objectivo: capacitar para o serviço ministerial prático.")

    h2(doc, "Instituto 5 — Ministerial")
    _tabela_escola(doc, "Escola de Liderança Cristã", [
        "Liderança Servidora", "Gestão Ministerial",
    ])
    _tabela_escola(doc, "Escola de Comunicação e Ensino", [
        "Homilética", "Pregação", "Ensino Bíblico",
    ])
    _tabela_escola(doc, "Escola de Administração Eclesiástica", [
        "Organização da Igreja", "Gestão de Ministérios",
    ])

    h2(doc, "Instituto 6 — Reino e Poder")
    _tabela_escola(doc, "Escola de Cura Divina", [
        "Cura no Ministério de Jesus", "Fé para Cura", "Prática de Cura",
    ])
    _tabela_escola(doc, "Escola de Libertação", [
        "Autoridade Espiritual", "Libertação Bíblica",
    ])
    _tabela_escola(doc, "Escola de Dons Espirituais", [
        "Profecia", "Discernimento", "Palavra de Conhecimento",
    ])

    h2(doc, "Instituto 7 — Cinco Ministérios")
    paragrafo(doc, "Cada uma das cinco escolas inclui: Curso de Fundamentos, Curso de Desenvolvimento e Curso de Prática Ministerial.")
    _tabela_escola(doc, "Escolas do Instituto dos Cinco Ministérios", [
        "Escola Apostólica", "Escola Profética", "Escola Evangelística",
        "Escola Pastoral", "Escola de Mestre",
    ])

    # === NÍVEL 4 ===
    h1(doc, "Nível 4 — Multiplicação (Reino)", numero=6)
    paragrafo(doc, "Objectivo: formar líderes, missionários e multiplicadores do Reino.")

    h2(doc, "Instituto 8 — Missões")
    _tabela_escola(doc, "Escola de Evangelismo", [
        "Evangelismo Pessoal", "Evangelismo Urbano",
    ])
    _tabela_escola(doc, "Escola de Missões", [
        "Missões Locais", "Missões Transculturais",
    ])

    h2(doc, "Instituto 9 — Liderança e Multiplicação")
    _tabela_escola(doc, "Escola de Formação de Líderes", [
        "Mentoria", "Desenvolvimento de Líderes",
    ])
    _tabela_escola(doc, "Escola de Plantação de Igrejas", [
        "Igrejas Locais", "Expansão Ministerial",
    ])

    h2(doc, "Instituto 10 — Pesquisa e Excelência")
    _tabela_escola(doc, "Escola de Produção Teológica", [
        "Escrita Cristã", "Produção de Apostilas",
    ])
    _tabela_escola(doc, "Escola de História e Avivamento", [
        "Avivamentos Bíblicos", "História da Igreja",
    ])
    _tabela_escola(doc, "Escola de Formação Avançada", [
        "Escatologia Avançada", "Apologética Avançada",
    ])

    # === ESTRUTURA ===
    h1(doc, "Estrutura Padrão (Apostila → Instituto)", numero=7)
    tbl = doc.add_table(rows=1, cols=3)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Unidade", "Composição", "Foco"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    for d in [
        ("Apostila", "10–15 páginas", "1 conceito central"),
        ("Módulo", "3–5 apostilas", "1 tema macro"),
        ("Curso", "3–6 módulos", "1 competência"),
        ("Escola", "2–4 cursos", "1 área de conhecimento"),
        ("Instituto", "3–5 escolas", "1 grande domínio teológico"),
    ]:
        row = tbl.add_row().cells
        for i, v in enumerate(d):
            row[i].text = v
            for p in row[i].paragraphs:
                for run in p.runs: run.font.name = FONTE_CORPO; run.font.size = Pt(11)

    h1(doc, "Volume Total Realista", numero=8)
    lista(doc, [
        "10 Institutos",
        "34 Escolas",
        "~120 a 160 Cursos iniciais",
        "~500 a 900 Módulos",
        "~2.000+ Apostilas possíveis",
    ])

    h1(doc, "Diferencial Final da Epignósis", numero=9)
    paragrafo(doc, "A Escola Bíblica Epignósis não é uma instituição linear, mas multidimensional. Articula simultaneamente:")
    lista(doc, [
        "Académica — estrutura curricular consistente.",
        "Espiritual — formação devocional integrada.",
        "Prática — capacitação ministerial real.",
        "Missionária — visão de multiplicação e Reino.",
    ])

    h1(doc, "Resultado Final do Mapa", numero=10)
    paragrafo(doc, "O aluno Epignósis conclui o seu percurso formativo com:")
    lista(doc, [
        "Conhecimento bíblico sólido.",
        "Formação teológica consistente.",
        "Vida espiritual madura.",
        "Capacitação ministerial prática.",
        "Mentalidade de Reino e multiplicação.",
    ])

    selo_final(doc)
    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-006_Mapa_de_Cursos.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
