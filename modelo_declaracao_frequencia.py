"""
MODELO OFICIAL DE DECLARAÇÃO DE FREQUÊNCIA — Escola Bíblica Epignósis
Documento mais simples que o histórico, emitido para alunos em curso.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Declaração de Frequência", "EBE-FRM-DEC")

    # CAPA-CABEÇALHO
    doc.add_paragraph()
    inserir_logo(doc, LOGO_PATH, largura_cm=5.5)

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("ESCOLA BÍBLICA EPIGNÓSIS")
    r.font.name = FONTE_TITULO; r.font.size = Pt(14); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("ἐπίγνωσις · Conhecer a Deus. Viver a Palavra. Manifestar o Reino.")
    r.font.name = FONTE_TITULO; r.font.size = Pt(9)
    r.font.italic = True; r.font.color.rgb = COR_SECUNDARIA

    p = doc.add_paragraph(); _add_horizontal_line(p, color=HEX_SECUNDARIA, size=6)

    # Quadro de protocolo (canto superior, direita)
    tbl_pro = doc.add_table(rows=1, cols=2)
    tbl_pro.alignment = WD_TABLE_ALIGNMENT.RIGHT
    tbl_pro.rows[0].cells[0].width = Cm(4)
    tbl_pro.rows[0].cells[1].width = Cm(5)
    c0 = tbl_pro.rows[0].cells[0]
    c1 = tbl_pro.rows[0].cells[1]
    c0.text = "N.º do documento:"
    c1.text = "EBE-DEC-«[ano]»-«[n.º]»"
    _shade_cell(c0, "E8F1EC")
    for p in c0.paragraphs:
        for r in p.runs:
            r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(9)
            r.font.color.rgb = COR_PRIMARIA
    for p in c1.paragraphs:
        for r in p.runs:
            r.font.name = FONTE_CORPO; r.font.size = Pt(9)

    # Título
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    r = p.add_run("DECLARAÇÃO DE FREQUÊNCIA")
    r.font.name = FONTE_TITULO; r.font.size = Pt(22); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    doc.add_paragraph()

    # CORPO
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.8
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run(
        "A Secretaria Acadêmica da Escola Bíblica Epignósis, no uso "
        "das suas atribuições e em conformidade com o Regimento "
        "Acadêmico (EBE-DOC-004), declara, para os devidos fins, que "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)

    r = p.add_run("«[NOME COMPLETO DO(A) ALUNO(A)]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", portador(a) do documento de identificação n.º "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[N.º do BI / Passaporte]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", matriculado(a) sob o n.º "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[N.º de matrícula]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", encontra-se regularmente inscrito(a) e frequentando o curso "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[Nome do curso / programa]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", da Escola de "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[Nome da Escola]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(", integrante do Instituto de ")
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[Nome do Instituto]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", correspondente ao nível formativo "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[Discípulo / Crescimento / Servir / Multiplicação]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", com carga horária total de "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[…]» horas")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", em regime "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[presencial / híbrido / on-line]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        ", iniciado em "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[__/__/____]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    r = p.add_run(
        " e com previsão de conclusão em "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[__/__/____]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA
    r = p.add_run(".")
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)

    # Frequência
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.line_spacing = 1.8
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run(
        "Mais se declara que, até à presente data, o(a) referido(a) aluno(a) "
        "apresenta frequência de "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[…] %»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA
    r = p.add_run(
        " às actividades acadêmicas, mantendo conduta compatível com os "
        "valores institucionais e em situação acadêmica "
    )
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[regular / em dia / sem pendências]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA
    r = p.add_run(".")
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)

    # Finalidade
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.line_spacing = 1.8
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("A presente declaração é emitida a pedido do(a) interessado(a) para a finalidade de ")
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[indicar finalidade — comprovação eclesial, ministerial, profissional, etc.]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA
    r = p.add_run(", não substituindo o Histórico Escolar oficial nem o Diploma de Conclusão, os quais serão emitidos no momento próprio, após o cumprimento integral dos requisitos académicos.")
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)

    # Versículo
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(14)
    r = p.add_run("“Tudo posso naquele que me fortalece.”  —  Filipenses 4.13 (ARC)")
    r.font.name = FONTE_TITULO; r.font.size = Pt(11); r.font.italic = True
    r.font.color.rgb = COR_SECUNDARIA

    # Fecho
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run("Por ser verdade, firma-se a presente declaração, em ")
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)
    r = p.add_run("«[Local]», aos «[__]» dias do mês de «[mês]» do ano de «[ano]»")
    r.font.name = FONTE_TITULO; r.font.size = Pt(12); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA
    r = p.add_run(".")
    r.font.name = FONTE_CORPO; r.font.size = Pt(12)

    # ASSINATURAS
    for _ in range(3):
        doc.add_paragraph()

    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c in tbl.rows[0].cells:
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("__________________________________")
        r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    rot = [
        ("«[Nome do(a) Secretário(a) Acadêmico(a)]»", "Secretaria Acadêmica"),
        ("«[Nome do(a) Coordenador(a) Acadêmico(a)]»", "Coordenação Acadêmica"),
    ]
    for i, (n, l) in enumerate(rot):
        c = tbl.rows[1].cells[i]
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(n)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10); r.font.bold = True
        r.font.color.rgb = COR_PRIMARIA
        p2 = c.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r2 = p2.add_run(l)
        r2.font.name = FONTE_CORPO; r2.font.size = Pt(9)
        r2.font.italic = True; r2.font.color.rgb = COR_SECUNDARIA

    # CARIMBO
    doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ CARIMBO INSTITUCIONAL ]")
    r.font.name = FONTE_TITULO; r.font.size = Pt(10); r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA

    doc.add_paragraph()
    p = doc.add_paragraph(); _add_horizontal_line(p, color=HEX_SECUNDARIA, size=4)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Documento de validade institucional. Cópia verificável junto à Secretaria Acadêmica mediante apresentação do n.º acima indicado.")
    r.font.name = FONTE_CORPO; r.font.size = Pt(8); r.font.italic = True
    r.font.color.rgb = COR_CITACAO

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Conhecer a Deus.  Viver a Palavra.  Manifestar o Reino.  ·  Soli Deo Gloria.")
    r.font.name = FONTE_TITULO; r.font.size = Pt(9); r.font.italic = True
    r.font.color.rgb = COR_PRIMARIA

    out = os.path.join(os.path.dirname(__file__), "EBE-FRM-003_Declaracao_de_Frequencia.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
