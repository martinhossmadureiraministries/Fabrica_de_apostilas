"""DOC 7 — Duração Oficial dos Cursos"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def _tab_carga(doc, titulo, linhas, total_horas):
    h3(doc, titulo)
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Curso", "Carga horária"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "2E7D4F")
    for nome, h in linhas:
        row = tbl.add_row().cells
        row[0].text = nome; row[1].text = h
        for c in row:
            for p in c.paragraphs:
                for run in p.runs:
                    run.font.name = FONTE_CORPO; run.font.size = Pt(11)
    # Linha de total
    row = tbl.add_row().cells
    row[0].text = "Total da escola"; row[1].text = total_horas
    for c in row:
        _shade_cell(c, "E8F1EC")
        for p in c.paragraphs:
            for run in p.runs:
                run.font.bold = True; run.font.name = FONTE_TITULO; run.font.size = Pt(11)


def gerar():
    doc = novo_documento("Duração Oficial dos Cursos", "EBE-DOC-007")
    add_capa(doc,
        supratitulo="Documento Institucional N.º 7",
        titulo="Duração Oficial\ndos Cursos",
        subtitulo="Carga Horária Padronizada por Nível, Instituto e Escola",
        codigo="EBE-DOC-007", ano="2026")
    add_marco_filosofico(doc)

    h1(doc, "Sumário")
    lista(doc, [
        "1. Padrão Geral de Tempo",
        "2. Nível 1 — Discípulo (Conhecer)",
        "3. Nível 2 — Crescimento (Ser)",
        "4. Nível 3 — Servir (Ministério)",
        "5. Nível 4 — Multiplicação (Reino)",
        "6. Resumo Geral da Formação",
        "7. Interpretação Pedagógica",
    ])
    page_break(doc)

    h1(doc, "Padrão Geral de Tempo", numero=1)
    paragrafo(doc,
        "A Escola Bíblica Epignósis adopta as seguintes faixas-padrão de "
        "carga horária para cada unidade da sua arquitectura:")
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Unidade", "Carga horária"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    rows = [
        ("Apostila",            "1 a 3 horas de estudo"),
        ("Módulo",              "4 a 10 horas"),
        ("Curso",               "20 a 60 horas"),
        ("Escola",              "60 a 180 horas"),
        ("Instituto",           "200 a 600 horas"),
        ("Formação Completa",   "800 a 2.400 horas"),
    ]
    for r in rows:
        row = tbl.add_row().cells
        for i, v in enumerate(r):
            row[i].text = v
            for p in row[i].paragraphs:
                for run in p.runs:
                    run.font.name = FONTE_CORPO; run.font.size = Pt(11)

    # NÍVEL 1
    h1(doc, "Nível 1 — Discípulo (Conhecer) · Formação Básica", numero=2)

    h2(doc, "Instituto de Formação Cristã")
    _tab_carga(doc, "Escola de Fundamentos da Fé", [
        ("Salvação e Novo Nascimento", "25 h"),
        ("Arrependimento e Fé", "20 h"),
        ("Baptismo e Ceia", "15 h"),
        ("Identidade em Cristo", "25 h"),
    ], "85 h")
    _tab_carga(doc, "Escola de Vida Cristã", [
        ("Santidade", "25 h"),
        ("Oração Devocional", "20 h"),
        ("Leitura Bíblica", "15 h"),
        ("Vida de Obediência", "20 h"),
    ], "80 h")
    _tab_carga(doc, "Escola de Discipulado", [
        ("Seguir a Cristo", "20 h"),
        ("Vida de Discípulo", "25 h"),
        ("Crescimento Espiritual", "25 h"),
    ], "70 h")

    h2(doc, "Instituto de Ciências Bíblicas")
    _tab_carga(doc, "Escola de Panorama Bíblico", [
        ("Antigo Testamento", "40 h"),
        ("Novo Testamento", "30 h"),
    ], "70 h")
    _tab_carga(doc, "Escola de Introdução aos Livros Bíblicos", [
        ("Pentateuco", "25 h"),
        ("Evangelhos", "25 h"),
        ("Epístolas", "25 h"),
    ], "75 h")
    _tab_carga(doc, "Escola de História Bíblica", [
        ("História de Israel", "30 h"),
        ("Igreja Primitiva", "25 h"),
    ], "55 h")

    # NÍVEL 2
    h1(doc, "Nível 2 — Crescimento (Ser) · Formação Intermediária", numero=3)

    h2(doc, "Instituto de Ciências Teológicas")
    _tab_carga(doc, "Escola ABC da Teologia", [
        ("Doutrinas Básicas", "25 h"),
        ("Natureza de Deus", "25 h"),
    ], "50 h")
    _tab_carga(doc, "Escola de Teologia Sistemática", [
        ("Deus (Teontologia)", "30 h"),
        ("Cristo (Cristologia)", "30 h"),
        ("Espírito Santo (Pneumatologia)", "30 h"),
        ("Salvação (Soteriologia)", "30 h"),
        ("Igreja (Eclesiologia)", "30 h"),
        ("Escatologia", "30 h"),
    ], "180 h")
    _tab_carga(doc, "Escola de Hermenêutica", [
        ("Interpretação Bíblica", "30 h"),
        ("Contexto Bíblico", "25 h"),
        ("Erros de Interpretação", "25 h"),
    ], "80 h")

    h2(doc, "Instituto de Formação Espiritual")
    _tab_carga(doc, "Escola de Oração", [
        ("Vida de Oração", "25 h"),
        ("Intercessão", "30 h"),
        ("Oração Bíblica", "20 h"),
    ], "75 h")
    _tab_carga(doc, "Escola do Espírito Santo", [
        ("Baptismo no Espírito Santo", "25 h"),
        ("Dons Espirituais", "30 h"),
        ("Fruto do Espírito", "20 h"),
    ], "75 h")
    _tab_carga(doc, "Escola de Santidade", [
        ("Carácter Cristão", "25 h"),
        ("Vida Santa", "25 h"),
        ("Maturidade Espiritual", "30 h"),
    ], "80 h")

    # NÍVEL 3
    h1(doc, "Nível 3 — Servir (Ministério) · Formação Prática", numero=4)

    h2(doc, "Instituto Ministerial")
    _tab_carga(doc, "Escola de Liderança Cristã", [
        ("Liderança Servidora", "30 h"),
        ("Gestão Ministerial", "30 h"),
    ], "60 h")
    _tab_carga(doc, "Escola de Comunicação e Ensino", [
        ("Homilética", "35 h"),
        ("Pregação", "35 h"),
        ("Ensino Bíblico", "30 h"),
    ], "100 h")
    _tab_carga(doc, "Escola de Administração Eclesiástica", [
        ("Organização da Igreja", "30 h"),
        ("Gestão de Ministérios", "30 h"),
    ], "60 h")

    h2(doc, "Instituto Reino e Poder")
    _tab_carga(doc, "Escola de Cura Divina", [
        ("Ministério de Jesus", "30 h"),
        ("Fé para Cura", "30 h"),
        ("Prática de Cura", "40 h"),
    ], "100 h")
    _tab_carga(doc, "Escola de Libertação", [
        ("Autoridade Espiritual", "30 h"),
        ("Libertação Bíblica", "40 h"),
    ], "70 h")
    _tab_carga(doc, "Escola de Dons Espirituais", [
        ("Profecia", "30 h"),
        ("Discernimento", "25 h"),
        ("Palavra de Conhecimento", "25 h"),
    ], "80 h")

    h2(doc, "Instituto dos Cinco Ministérios")
    paragrafo(doc,
        "Cada escola (Apostólica, Profética, Evangelística, Pastoral e de "
        "Mestre) terá carga horária entre 120 e 150 horas, perfazendo um "
        "Instituto completo entre 600 e 750 horas.")

    # NÍVEL 4
    h1(doc, "Nível 4 — Multiplicação (Reino) · Formação Avançada", numero=5)

    h2(doc, "Instituto de Missões")
    _tab_carga(doc, "Escolas do Instituto", [
        ("Evangelismo", "60 h"),
        ("Missões Locais", "60 h"),
        ("Missões Transculturais", "80 h"),
    ], "200 h")

    h2(doc, "Instituto de Liderança e Multiplicação")
    _tab_carga(doc, "Escolas do Instituto", [
        ("Formação de Líderes", "80 h"),
        ("Mentoria", "60 h"),
        ("Plantação de Igrejas", "80 h"),
    ], "220 h")

    h2(doc, "Instituto de Pesquisa Bíblica")
    _tab_carga(doc, "Escolas do Instituto", [
        ("Escrita Cristã", "60 h"),
        ("Produção de Apostilas", "60 h"),
        ("História da Igreja", "80 h"),
        ("Escatologia Avançada", "80 h"),
    ], "280 h")

    # RESUMO
    h1(doc, "Resumo Geral da Formação", numero=6)
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Nível formativo", "Carga horária aproximada"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    for n, h in [
        ("Nível 1 — Discípulo (Conhecer)",       "≈ 380 horas"),
        ("Nível 2 — Crescimento (Ser)",          "≈ 385 horas"),
        ("Nível 3 — Servir (Ministério)",        "≈ 830 horas"),
        ("Nível 4 — Multiplicação (Reino)",      "≈ 700 horas"),
    ]:
        row = tbl.add_row().cells
        row[0].text = n; row[1].text = h
        for c in row:
            for p in c.paragraphs:
                for run in p.runs:
                    run.font.name = FONTE_CORPO; run.font.size = Pt(11)
    # total
    row = tbl.add_row().cells
    row[0].text = "FORMAÇÃO COMPLETA EPIGNÓSIS"; row[1].text = "2.200 a 2.400 horas"
    for c in row:
        _shade_cell(c, "2E7D4F")
        for p in c.paragraphs:
            for run in p.runs:
                run.font.bold = True; run.font.name = FONTE_TITULO; run.font.size = Pt(12)
                run.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)

    h1(doc, "Interpretação Pedagógica", numero=7)
    lista(doc, [
        "Formação básica — 3 a 6 meses (dependendo do ritmo).",
        "Formação completa — 2 a 4 anos.",
        "Formação ministerial avançada — equivalente, em horas, à preparação pastoral real.",
    ])
    paragrafo(doc,
        "A carga horária aqui apresentada deve ser entendida como referência "
        "média. A Coordenação Acadêmica poderá ajustar, dentro das faixas "
        "do padrão geral, conforme o público, a modalidade (presencial, "
        "híbrida ou on-line) e os objectivos específicos do programa.")

    selo_final(doc)
    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-007_Duracao_Oficial.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
