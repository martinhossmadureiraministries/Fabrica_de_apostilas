"""
MODELO OFICIAL DE APOSTILA — Escola Bíblica Epignósis
Modelo .docx editável e totalmente preenchível.
A apostila é a unidade mínima de estudo (10–15 páginas, 1 conceito central, 1–3 horas).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Modelo de Apostila", "EBE-MOD-APOSTILA")

    # ====== CAPA DA APOSTILA ======
    doc.add_paragraph()
    inserir_logo(doc, LOGO_PATH, largura_cm=6.0)

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Conhecer a Deus. Viver a Palavra. Manifestar o Reino.")
    r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    r.font.italic = True; r.font.color.rgb = COR_SECUNDARIA

    p = doc.add_paragraph(); _add_horizontal_line(p, color=HEX_SECUNDARIA, size=6)

    for _ in range(2): doc.add_paragraph()

    # Trilha hierárquica (Instituto > Escola > Curso > Módulo > Apostila)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("INSTITUTO «[Nome do Instituto]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(11); r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Escola de «[Nome da Escola]»  ·  Curso «[Nome do Curso]»  ·  Módulo «[N.º — Nome do Módulo]»")
    r.font.name = FONTE_CORPO; r.font.size = Pt(10); r.font.color.rgb = COR_CITACAO

    for _ in range(2): doc.add_paragraph()

    # Numeração da apostila
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("APOSTILA N.º  [00]")
    r.font.name = FONTE_TITULO; r.font.size = Pt(13); r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA

    # Título principal da apostila
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ TÍTULO DA APOSTILA ]")
    r.font.name = FONTE_TITULO; r.font.size = Pt(28); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ subtítulo opcional ]")
    r.font.name = FONTE_TITULO; r.font.size = Pt(13)
    r.font.italic = True; r.font.color.rgb = COR_TEXTO

    for _ in range(3): doc.add_paragraph()

    # Quadro de identificação
    tbl = doc.add_table(rows=4, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    dados = [
        ("Autor / Docente", "«[Nome completo]»"),
        ("Carga horária estimada", "«[1–3 horas de estudo]»"),
        ("Nível formativo", "«[Discípulo / Crescimento / Servir / Multiplicação]»"),
        ("Edição / Ano", "«[N.º — Ano]»"),
    ]
    for i, (k, v) in enumerate(dados):
        row = tbl.rows[i].cells
        row[0].text = k; row[1].text = v
        _shade_cell(row[0], "E8F1EC")
        for p in row[0].paragraphs:
            for r in p.runs:
                r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(10)
                r.font.color.rgb = COR_PRIMARIA
        for p in row[1].paragraphs:
            for r in p.runs:
                r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    for _ in range(2): doc.add_paragraph()
    p = doc.add_paragraph(); _add_horizontal_line(p, color=HEX_SECUNDARIA, size=4)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Material didáctico oficial · Escola Bíblica Epignósis · 2026")
    r.font.name = FONTE_CORPO; r.font.size = Pt(9); r.font.color.rgb = COR_CITACAO

    page_break(doc)

    # ====== MARCO FILOSÓFICO ======
    add_marco_filosofico(doc)

    # ====== FICHA TÉCNICA / DIREITOS ======
    h1(doc, "Ficha Técnica")
    paragrafo(doc,
        "Este material didáctico é propriedade intelectual da Escola Bíblica "
        "Epignósis (EBE), produzido para uso exclusivo no âmbito dos seus "
        "programas de formação. A sua reprodução, no todo ou em parte, "
        "depende de autorização institucional escrita.")
    lista(doc, [
        "Título da apostila: «[Título]»",
        "Autor / Docente: «[Nome]»",
        "Revisão pedagógica: «[Nome]»",
        "Revisão doutrinária (Conselho Doutrinário): «[Nome]»",
        "Diagramação: «[Nome]»",
        "Versão bíblica de referência: Almeida Revista e Corrigida (ARC).",
        "Edição: «[N.º]» — Ano «[YYYY]».",
        "Código institucional: EBE-APO-«[XXX]».",
    ])
    citacao(doc,
        "Toda a Escritura é divinamente inspirada e proveitosa para ensinar, "
        "para redarguir, para corrigir, para instruir em justiça; para que o "
        "homem de Deus seja perfeito e perfeitamente instruído para toda a boa obra.",
        "2 Timóteo 3.16-17")

    page_break(doc)

    # ====== SUMÁRIO DA APOSTILA ======
    h1(doc, "Sumário")
    lista(doc, [
        "Apresentação da apostila",
        "Objectivos de aprendizagem",
        "Versículo-chave",
        "Texto-base para leitura",
        "1. Introdução",
        "2. Desenvolvimento do conceito central",
        "3. Aplicação prática",
        "4. Síntese e conclusão",
        "Exercícios de revisão",
        "Estudo bíblico complementar",
        "Para a próxima apostila",
        "Glossário",
        "Bibliografia recomendada",
        "Anotações pessoais",
    ], ordenada=False)

    page_break(doc)

    # ====== APRESENTAÇÃO ======
    h1(doc, "Apresentação da Apostila")
    paragrafo(doc,
        "«[Apresente, em 2 a 4 parágrafos, o conceito central desta apostila, "
        "a sua relevância para a vida cristã e o seu lugar dentro do módulo "
        "e do curso. Destaque por que vale a pena estudar este tema agora, "
        "neste momento da formação do aluno.]»")

    # ====== OBJECTIVOS ======
    h1(doc, "Objectivos de Aprendizagem")
    paragrafo(doc, "Ao concluir o estudo desta apostila, o aluno será capaz de:")
    lista(doc, [
        "«[Conhecer — verbo no infinitivo: identificar, descrever, distinguir…]»",
        "«[Crer — interiorizar uma convicção bíblica específica…]»",
        "«[Viver — aplicar a verdade aprendida em uma situação concreta…]»",
        "«[Servir — exercer um dom ou uma prática ministerial decorrente…]»",
    ], ordenada=True)

    # ====== VERSÍCULO-CHAVE ======
    h1(doc, "Versículo-Chave")
    citacao(doc,
        "«[Texto bíblico que sintetiza o ensinamento central desta apostila.]»",
        "«[Referência, ARC]»")

    # ====== TEXTO-BASE ======
    h1(doc, "Texto-Base para Leitura")
    paragrafo(doc,
        "Antes de iniciar o estudo, o aluno é convidado a ler atentamente "
        "a seguinte passagem em sua Bíblia (Almeida Revista e Corrigida):")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("«[Livro Cap.versículo-versículo]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(14); r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA

    page_break(doc)

    # ====== 1. INTRODUÇÃO ======
    h1(doc, "Introdução", numero=1)
    paragrafo(doc,
        "«[Apresente o tema, contextualize-o histórica, teológica e "
        "pastoralmente. Que problema, pergunta ou necessidade espiritual "
        "esta apostila busca responder?]»")
    paragrafo(doc,
        "«[Faça a ponte com o conhecimento anterior do aluno, recordando "
        "brevemente o que foi estudado nas apostilas precedentes do módulo.]»")

    # ====== 2. DESENVOLVIMENTO ======
    h1(doc, "Desenvolvimento do Conceito Central", numero=2)

    h2(doc, "Fundamentos bíblicos", numero="2.1")
    paragrafo(doc,
        "«[Apresente as bases bíblicas do tema, citando ao menos 3 a 5 textos "
        "fundamentais. Cada texto deve ser comentado brevemente.]»")
    citacao(doc, "«[Texto bíblico citado.]»", "«[Referência, ARC]»")
    citacao(doc, "«[Texto bíblico citado.]»", "«[Referência, ARC]»")

    h2(doc, "Desenvolvimento doutrinário", numero="2.2")
    paragrafo(doc,
        "«[Desenvolva o conteúdo doutrinário em parágrafos articulados. Use "
        "linguagem clara, didáctica, evitando jargão excessivo. Defina "
        "termos-chave logo na primeira ocorrência.]»")

    h3(doc, "Definição")
    paragrafo(doc, "«[Definição precisa do conceito central da apostila.]»")

    h3(doc, "Aspectos principais")
    lista(doc, [
        "«[Aspecto 1 — breve explicação.]»",
        "«[Aspecto 2 — breve explicação.]»",
        "«[Aspecto 3 — breve explicação.]»",
    ], ordenada=True)

    h2(doc, "Possíveis dúvidas e equívocos comuns", numero="2.3")
    paragrafo(doc,
        "«[Apresente 2 ou 3 dúvidas frequentes ou interpretações erradas "
        "sobre o tema, e responda-as com base nas Escrituras.]»")

    # Quadro destaque
    h2(doc, "Quadro de Destaque", numero="2.4")
    tbl = doc.add_table(rows=1, cols=1)
    cell = tbl.rows[0].cells[0]
    cell.text = ""
    _shade_cell(cell, "E8F1EC")
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run("✦ Para reter:  ")
    r.font.bold = True; r.font.color.rgb = COR_SECUNDARIA
    r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r2 = p.add_run("«[Síntese em uma ou duas frases — o aluno deve sair com isto na memória.]»")
    r2.font.name = FONTE_CORPO; r2.font.size = Pt(11); r2.font.italic = True

    page_break(doc)

    # ====== 3. APLICAÇÃO ======
    h1(doc, "Aplicação Prática", numero=3)
    paragrafo(doc,
        "«[Como o conteúdo estudado se aplica à vida diária, à família, "
        "à igreja local e ao testemunho público do aluno? Apresente 3 a 5 "
        "aplicações concretas.]»")
    lista(doc, [
        "«[Aplicação 1 — Na vida pessoal e devocional.]»",
        "«[Aplicação 2 — Na família.]»",
        "«[Aplicação 3 — Na igreja local.]»",
        "«[Aplicação 4 — No trabalho / sociedade.]»",
        "«[Aplicação 5 — No exercício ministerial.]»",
    ], ordenada=True)

    # ====== 4. SÍNTESE ======
    h1(doc, "Síntese e Conclusão", numero=4)
    paragrafo(doc,
        "«[Recapitule, em um único parágrafo, o que foi estudado. Termine "
        "com um apelo pastoral, levando o aluno a uma decisão, a uma "
        "oração ou a uma prática concreta.]»")
    citacao(doc, "«[Versículo de encerramento — pode repetir o versículo-chave.]»", "«[Referência, ARC]»")

    page_break(doc)

    # ====== EXERCÍCIOS ======
    h1(doc, "Exercícios de Revisão")
    paragrafo(doc, "Responda às questões a seguir com base no conteúdo desta apostila e na sua leitura bíblica.")

    h3(doc, "I — Verifique a sua compreensão")
    lista(doc, [
        "Defina, com suas próprias palavras, o conceito central desta apostila.",
        "Cite ao menos três textos bíblicos que sustentam o tema estudado.",
        "Identifique uma dúvida comum e responda a ela biblicamente.",
    ], ordenada=True)

    h3(doc, "II — Reflexão pessoal")
    lista(doc, [
        "Como este ensino se aplica à sua vida nesta semana?",
        "Existe alguma área em que você precisa de mudar à luz do que aprendeu?",
        "Que oração você fará a Deus em resposta a este estudo?",
    ], ordenada=True)

    h3(doc, "III — Ministério e serviço")
    lista(doc, [
        "Como você ensinaria este tema a um irmão mais novo na fé?",
        "Que situação concreta na sua igreja local pode ser iluminada por este ensino?",
    ], ordenada=True)

    # ====== ESTUDO BÍBLICO ======
    h1(doc, "Estudo Bíblico Complementar")
    paragrafo(doc,
        "Leia atentamente «[Livro Cap.versículos]» e responda:")
    lista(doc, [
        "Qual é o contexto histórico e literário desta passagem?",
        "Quais são as palavras-chave do texto?",
        "Que verdade central o autor sagrado quer transmitir?",
        "Como esta passagem se relaciona com o tema da apostila?",
        "Que aplicação prática você extrai deste texto?",
    ], ordenada=True)

    # ====== PRÓXIMA APOSTILA ======
    h1(doc, "Para a Próxima Apostila")
    paragrafo(doc,
        "Na próxima apostila estudaremos «[Tema da próxima apostila]». "
        "Para se preparar, leia previamente «[passagem bíblica]» e reflicta "
        "sobre as perguntas a seguir:")
    lista(doc, [
        "«[Pergunta orientadora 1]»",
        "«[Pergunta orientadora 2]»",
    ])

    page_break(doc)

    # ====== GLOSSÁRIO ======
    h1(doc, "Glossário")
    paragrafo(doc, "Definições breves dos termos-chave utilizados nesta apostila.")
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Termo", "Definição"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], HEX_PRIMARIA)
    for i in range(5):
        row = tbl.add_row().cells
        row[0].text = "«[Termo]»"; row[1].text = "«[Definição clara e breve.]»"
        for c in row:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = FONTE_CORPO; r.font.size = Pt(11)

    # ====== BIBLIOGRAFIA ======
    h1(doc, "Bibliografia Recomendada")
    lista(doc, [
        "Bíblia Sagrada. Tradução de João Ferreira de Almeida, Revista e Corrigida.",
        "«[Sobrenome, Nome. Título da obra. Cidade: Editora, ano.]»",
        "«[Sobrenome, Nome. Título da obra. Cidade: Editora, ano.]»",
        "«[Sobrenome, Nome. Título da obra. Cidade: Editora, ano.]»",
    ])

    # ====== ANOTAÇÕES ======
    h1(doc, "Anotações Pessoais")
    for _ in range(15):
        p = doc.add_paragraph()
        _add_horizontal_line(p, color="C8C8C8", size=4)

    selo_final(doc)

    out = os.path.join(os.path.dirname(__file__), "EBE-MODELO_APOSTILA_em_branco.docx")
    doc.save(out)
    print("OK:", out)


if __name__ == "__main__":
    gerar()
