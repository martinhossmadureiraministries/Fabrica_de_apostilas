"""DOC 8 — Sistema de Pré-Requisitos"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Sistema de Pré-Requisitos", "EBE-DOC-008")
    add_capa(doc,
        supratitulo="Documento Institucional N.º 8",
        titulo="Sistema de\nPré-Requisitos",
        subtitulo="Princípios de Progressão Acadêmica e Espiritual",
        codigo="EBE-DOC-008", ano="2026")
    add_marco_filosofico(doc)

    h1(doc, "Sumário")
    lista(doc, [
        "1. Princípio Fundamental",
        "2. Estrutura de Dependência (4 tipos)",
        "3. Nível 1 — Discípulo (acesso livre controlado)",
        "4. Nível 2 — Crescimento",
        "5. Nível 3 — Servir (Ministério)",
        "6. Nível 4 — Multiplicação",
        "7. Pré-requisitos por Instituto",
        "8. Sistema de Trilhas Obrigatórias",
        "9. Regras Gerais do Sistema",
        "10. Resultado do Sistema",
    ])
    page_break(doc)

    h1(doc, "Princípio Fundamental", numero=1)
    paragrafo(doc,
        "Nenhum curso da Escola Bíblica Epignósis é isolado. Todo o "
        "aprendizado é progressivo, cumulativo e formativo. Trata-se de "
        "uma convicção pedagógica e espiritual: o aluno precisa de base "
        "antes de avançar; o conhecimento é construído em camadas; e a "
        "maturidade espiritual deve acompanhar a maturidade acadêmica.")
    citacao(doc,
        "Pelo tempo já devíeis ser mestres, e tendes outra vez necessidade "
        "de que se vos torne a ensinar quais sejam os primeiros rudimentos "
        "das palavras de Deus.",
        "Hebreus 5.12")
    citacao(doc, "Como meninos novamente nascidos, desejai afectuosamente o leite racional, não falsificado, para que por ele vades crescendo.", "1 Pedro 2.2")

    h1(doc, "Estrutura de Dependência — 4 Tipos de Pré-Requisitos", numero=2)
    tbl = doc.add_table(rows=1, cols=3)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Tipo", "Define", "Exemplo"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    rows = [
        ("1. Pré-requisito de Nível",     "Nível espiritual mínimo exigido.",
         "Teologia Sistemática → Nível Crescimento obrigatório."),
        ("2. Pré-requisito de Instituto", "Domínio prévio de área anterior.",
         "Ministério → exige Formação Espiritual básica."),
        ("3. Pré-requisito de Escola",    "Base específica dentro do mesmo campo.",
         "Homilética → exige Hermenêutica básica."),
        ("4. Pré-requisito de Curso",     "Dependência directa de outro curso.",
         "Pregação → exige Homilética."),
    ]
    for r in rows:
        row = tbl.add_row().cells
        for i, v in enumerate(r):
            row[i].text = v
            for p in row[i].paragraphs:
                for run in p.runs:
                    run.font.name = FONTE_CORPO; run.font.size = Pt(11)

    # === NÍVEL 1 ===
    h1(doc, "Nível 1 — Discípulo (Acesso Livre Controlado)", numero=3)
    paragrafo(doc,
        "Regra geral: todos os alunos podem iniciar a sua formação neste "
        "nível, sem pré-requisito formal. Exceções poderão ser definidas "
        "para programas avançados específicos.")
    h3(doc, "Cursos Fundamentais (Base Obrigatória)")
    paragrafo(doc, "Estes cursos constituem a porta de entrada da Epignósis e são pré-requisito universal para os demais:")
    lista(doc, [
        "Salvação e Novo Nascimento",
        "Arrependimento e Fé",
        "Identidade em Cristo",
        "Santidade",
        "Vida de Oração",
    ], ordenada=True)

    # === NÍVEL 2 ===
    h1(doc, "Nível 2 — Crescimento (Depende do Nível 1 Completo)", numero=4)
    paragrafo(doc, "Regra geral: para entrar no Nível 2, o aluno deve concluir o Nível 1 (ou comprovar equivalente validado pela Coordenação Acadêmica).")

    h3(doc, "Exemplos de Pré-Requisitos")
    lista(doc, [
        "Teologia Sistemática → Nível Discípulo completo + Fundamentos da Fé.",
        "Hermenêutica → Panorama Bíblico + Leitura Bíblica Básica.",
        "Escola do Espírito Santo → Vida de Oração + Identidade em Cristo.",
    ])

    # === NÍVEL 3 ===
    h1(doc, "Nível 3 — Servir / Ministério (Depende do Nível 2)", numero=5)
    paragrafo(doc, "Regra geral: conclusão do Nível Crescimento.")
    h3(doc, "Exemplos de Pré-Requisitos")
    lista(doc, [
        "Homilética → Hermenêutica + Leitura Bíblica Avançada.",
        "Pregação → Homilética obrigatória.",
        "Cura Divina → Espírito Santo + Dons Espirituais.",
        "Libertação → Autoridade Espiritual + Teologia Básica.",
        "Liderança Cristã → Vida de Discípulo + Santidade.",
    ])

    # === NÍVEL 4 ===
    h1(doc, "Nível 4 — Multiplicação (Depende do Nível 3)", numero=6)
    paragrafo(doc, "Regra geral: conclusão do Nível Ministério.")
    h3(doc, "Exemplos de Pré-Requisitos")
    lista(doc, [
        "Missões → Evangelismo + Vida Cristã madura.",
        "Plantação de Igrejas → Liderança Cristã + Administração Eclesiástica.",
        "Mentoria → Liderança Cristã + Discipulado Avançado.",
    ])

    # === INSTITUTOS ===
    h1(doc, "Pré-Requisitos por Instituto (Visão Macro)", numero=7)
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Instituto", "Pré-requisito de entrada"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    rows = [
        ("Ciências Teológicas", "Nível Crescimento."),
        ("Ministerial",         "Nível Crescimento + parte de Teologia."),
        ("Reino e Poder",       "Nível Crescimento completo + Espírito Santo concluído."),
        ("Cinco Ministérios",   "Nível Ministério completo + Liderança Cristã + Dons Espirituais."),
        ("Missões",             "Evangelismo + Vida Cristã madura."),
        ("Liderança e Multiplicação", "Nível Ministério completo."),
        ("Pesquisa Bíblica",    "Nível Ministério completo + Hermenêutica avançada."),
    ]
    for r in rows:
        row = tbl.add_row().cells
        for i, v in enumerate(r):
            row[i].text = v
            for p in row[i].paragraphs:
                for run in p.runs:
                    run.font.name = FONTE_CORPO; run.font.size = Pt(11)

    # === TRILHAS ===
    h1(doc, "Sistema de Trilhas Obrigatórias", numero=8)
    h3(doc, "Trilha Base (obrigatória para todos)")
    lista(doc, ["Salvação", "Fé", "Identidade em Cristo", "Vida de Oração"])
    paragrafo(doc, "→ Libera todos os cursos iniciais.")

    h3(doc, "Trilha Teológica")
    lista(doc, ["Panorama Bíblico", "Teologia Sistemática", "Hermenêutica"])

    h3(doc, "Trilha Ministerial")
    lista(doc, ["Liderança", "Homilética", "Dons Espirituais"])

    h3(doc, "Trilha Avançada")
    lista(doc, ["Missões", "Plantação de Igrejas", "Pesquisa Bíblica"])

    # === REGRAS ===
    h1(doc, "Regras Gerais do Sistema", numero=9)
    lista(doc, [
        "Regra da Progressão — nenhum aluno pode “saltar” níveis.",
        "Regra da Base Espiritual — nenhum ministério substitui a vida espiritual.",
        "Regra da Coerência — todo curso pressupõe a base bíblica anterior.",
        "Regra da Multiplicação — nenhum conhecimento é terminal; "
        "todo conhecimento gera ensino (2 Timóteo 2.2).",
    ], ordenada=True)

    h1(doc, "Resultado do Sistema", numero=10)
    paragrafo(doc, "Com a aplicação deste sistema, a Escola Bíblica Epignósis assegura:")
    lista(doc, [
        "Progressão clara e mensurável.",
        "Caminho espiritual estruturado.",
        "Eliminação da superficialidade doutrinária.",
        "Formação de líderes reais, e não apenas titulados.",
        "Maturidade cristã gradual e duradoura.",
    ])
    citacao(doc, "Mas crescei na graça e conhecimento de nosso Senhor e Salvador, Jesus Cristo.", "2 Pedro 3.18")

    selo_final(doc)
    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-008_Sistema_de_Pre_Requisitos.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
