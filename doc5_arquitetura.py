"""DOC 5 — Arquitectura Oficial"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Arquitectura Institucional", "EBE-DOC-005")
    add_capa(doc,
        supratitulo="Documento Institucional N.º 5",
        titulo="Arquitectura Oficial",
        subtitulo="Estrutura Hierárquica de Sete Níveis",
        codigo="EBE-DOC-005", ano="2026")
    add_marco_filosofico(doc)

    h1(doc, "Sumário")
    lista(doc, [
        "1. Apresentação",
        "2. Princípios Estruturantes",
        "3. Visão Geral da Arquitectura (7 níveis)",
        "4. Nível 1 — Escola Bíblica Epignósis",
        "5. Nível 2 — Institutos",
        "6. Nível 3 — Escolas",
        "7. Nível 4 — Programas de Formação",
        "8. Nível 5 — Cursos",
        "9. Nível 6 — Módulos",
        "10. Nível 7 — Apostilas",
        "11. Quadro-Resumo Estrutural",
        "12. Marco Filosófico Institucional",
    ])
    page_break(doc)

    h1(doc, "Apresentação", numero=1)
    paragrafo(doc,
        "A Arquitectura Oficial da Escola Bíblica Epignósis descreve a forma "
        "como o conhecimento é organizado, distribuído e ensinado dentro da "
        "instituição. Trata-se de uma estrutura em sete níveis, do mais "
        "amplo (a Escola) ao mais específico (a apostila), assegurando "
        "unidade pedagógica, progressão curricular e clareza administrativa.")
    paragrafo(doc,
        "Esta arquitectura permite que a Escola cresça organicamente, "
        "agregando novos institutos, escolas, programas, cursos, módulos e "
        "apostilas sem perder a coerência interna nem a sua identidade "
        "doutrinária.")

    h1(doc, "Princípios Estruturantes", numero=2)
    lista(doc, [
        "Unidade — toda a estrutura serve a uma única missão.",
        "Hierarquia — cada nível agrupa e organiza os níveis inferiores.",
        "Progressão — o conhecimento é construído em camadas.",
        "Especialização — cada nível foca-se em uma competência específica.",
        "Modularidade — cada unidade pode ser estudada em si mesma e "
        "também integrar caminhos formativos maiores.",
        "Multiplicação — toda apostila, módulo, curso ou escola pode gerar novos.",
    ], ordenada=True)

    h1(doc, "Visão Geral da Arquitectura (7 Níveis)", numero=3)
    tbl = doc.add_table(rows=1, cols=3)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Nível", "Unidade", "Função"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    niveis = [
        ("1", "Escola Bíblica Epignósis", "Instituição-mãe; identidade, missão e governo."),
        ("2", "Institutos", "Grandes áreas do conhecimento cristão."),
        ("3", "Escolas", "Especializações dentro de cada Instituto."),
        ("4", "Programas de Formação", "Públicos e níveis (fundamental, avançado, etc.)."),
        ("5", "Cursos", "Unidades temáticas; uma competência."),
        ("6", "Módulos", "Subdivisões do curso; um tema macro."),
        ("7", "Apostilas", "Unidade mínima de estudo; um conceito."),
    ]
    for n, u, f in niveis:
        row = tbl.add_row().cells
        row[0].text = n; row[1].text = u; row[2].text = f
        for c in row:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = FONTE_CORPO; r.font.size = Pt(11)

    h1(doc, "Nível 1 — Escola Bíblica Epignósis", numero=4)
    paragrafo(doc,
        "É a instituição principal, à qual estão subordinadas todas as "
        "demais unidades. É a entidade jurídica, espiritual e académica que "
        "responde pela missão, pela identidade doutrinária e pela governança "
        "global da formação.")

    h1(doc, "Nível 2 — Institutos", numero=5)
    paragrafo(doc,
        "Cada Instituto representa uma grande área do conhecimento cristão. "
        "São departamentos macro que reúnem escolas especializadas afins. "
        "A Escola Bíblica Epignósis estrutura-se a partir de dez institutos "
        "fundadores, podendo ser ampliados conforme a maturidade institucional:")
    lista(doc, [
        "Instituto de Formação Cristã",
        "Instituto de Ciências Bíblicas",
        "Instituto de Ciências Teológicas",
        "Instituto de Formação Espiritual",
        "Instituto Ministerial",
        "Instituto do Reino e Poder",
        "Instituto dos Cinco Ministérios",
        "Instituto de Missões",
        "Instituto de Liderança e Multiplicação",
        "Instituto de Pesquisa Bíblica e Excelência",
    ], ordenada=True)

    h1(doc, "Nível 3 — Escolas", numero=6)
    paragrafo(doc,
        "Cada Instituto possui diversas Escolas especializadas, cada uma "
        "dedicada a uma área específica de conhecimento.")
    h3(doc, "Exemplo — Instituto de Ciências Teológicas")
    lista(doc, [
        "Escola de Teologia Sistemática",
        "Escola de Hermenêutica",
        "Escola de Homilética",
        "Escola de Exegese",
        "Escola de Apologética",
    ])

    h1(doc, "Nível 4 — Programas de Formação", numero=7)
    paragrafo(doc,
        "Cada Escola pode oferecer diferentes Programas de Formação, "
        "destinados a públicos e níveis distintos. Assim, a mesma Escola "
        "atende a alunos com necessidades diferentes sem duplicar "
        "conteúdos nem comprometer a profundidade.")
    h3(doc, "Exemplo — Escola de Hermenêutica")
    lista(doc, [
        "Programa Fundamental",
        "Programa Intermediário",
        "Programa Avançado",
        "Programa para Professores",
    ])

    h1(doc, "Nível 5 — Cursos", numero=8)
    paragrafo(doc,
        "Cada Programa é composto por diversos cursos. O curso é a unidade "
        "que entrega uma competência específica ao aluno.")
    h3(doc, "Exemplo — Programa Fundamental de Hermenêutica")
    lista(doc, [
        "Introdução à Hermenêutica",
        "Princípios de Interpretação Bíblica",
        "Géneros Literários da Bíblia",
        "Contexto Histórico e Cultural",
    ])

    h1(doc, "Nível 6 — Módulos", numero=9)
    paragrafo(doc,
        "Cada curso é dividido em módulos, que correspondem a temas macro "
        "dentro do curso.")
    h3(doc, "Exemplo — Curso: Introdução à Hermenêutica")
    lista(doc, [
        "Módulo 1 — O que é Hermenêutica.",
        "Módulo 2 — A inspiração das Escrituras.",
        "Módulo 3 — Regras de interpretação.",
        "Módulo 4 — Erros comuns de interpretação.",
    ])

    h1(doc, "Nível 7 — Apostilas", numero=10)
    paragrafo(doc,
        "Cada módulo possui uma ou mais apostilas. A apostila é a unidade "
        "mínima de estudo: contém em geral entre 10 e 15 páginas, "
        "concentrando-se num único conceito central. É o coração do método "
        "Epignósis: ensino curto, profundo, prático e aplicável.")
    h3(doc, "Exemplo — Módulo 3: Regras de Interpretação")
    lista(doc, [
        "Apostila 1 — O contexto imediato.",
        "Apostila 2 — O contexto histórico.",
        "Apostila 3 — O contexto cultural.",
        "Apostila 4 — O contexto gramatical.",
    ])

    h1(doc, "Quadro-Resumo Estrutural", numero=11)
    tbl = doc.add_table(rows=1, cols=3)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Unidade", "Composição", "Foco"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    rows = [
        ("Apostila", "10–15 páginas", "1 conceito central"),
        ("Módulo", "3–5 apostilas", "1 tema macro"),
        ("Curso", "3–6 módulos", "1 competência"),
        ("Escola", "2–4 cursos", "1 área de conhecimento"),
        ("Instituto", "3–5 escolas", "1 grande domínio teológico"),
        ("Programa", "Conjunto de cursos", "1 público / nível"),
        ("EBE", "10 Institutos", "Formação integral cristã"),
    ]
    for r in rows:
        row = tbl.add_row().cells
        for i, v in enumerate(r):
            row[i].text = v
            for p in row[i].paragraphs:
                for run in p.runs:
                    run.font.name = FONTE_CORPO; run.font.size = Pt(11)

    h1(doc, "Marco Filosófico Institucional", numero=12)
    paragrafo(doc,
        "Este Marco Filosófico, expresso pela Escola, sintetiza a sua visão "
        "de educação cristã e deve aparecer na abertura de toda apostila, "
        "manual, livro e certificado emitido pela instituição:")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.left_indent = Cm(1.5)
    p.paragraph_format.right_indent = Cm(1.5)
    r = p.add_run(
        "“Acreditamos que o verdadeiro conhecimento de Deus transforma "
        "a mente pela verdade das Escrituras, o coração pela acção do "
        "Espírito Santo e a vida pelo compromisso de viver e anunciar "
        "o Evangelho de Jesus Cristo.”")
    r.font.name = FONTE_TITULO; r.font.size = Pt(13)
    r.font.italic = True; r.font.color.rgb = COR_PRIMARIA

    selo_final(doc)
    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-005_Arquitectura_Oficial.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
