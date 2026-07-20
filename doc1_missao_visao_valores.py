"""DOC 1 — Missão, Visão, Valores e Identidade Institucional"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Identidade Institucional", "EBE-DOC-001")

    add_capa(
        doc,
        supratitulo="Documento Institucional N.º 1",
        titulo="Identidade Institucional",
        subtitulo="Missão · Visão · Valores · Filosofia de Ensino",
        codigo="EBE-DOC-001",
        ano="2026",
    )
    add_marco_filosofico(doc)

    # === SUMÁRIO ===
    h1(doc, "Sumário")
    lista(doc, [
        "1. Apresentação e Identidade",
        "2. Significado do Nome: Epígnosis (ἐπίγνωσις)",
        "3. Lema Institucional",
        "4. Missão",
        "5. Visão",
        "6. Valores",
        "7. Propósito",
        "8. Filosofia de Ensino — As Quatro Dimensões",
        "9. Os Quatro Pilares da Formação",
        "10. Objectivos Gerais",
        "11. Perfil do Egresso",
        "12. Nosso Compromisso",
        "13. Fundamentação Bíblica",
    ], ordenada=False)

    page_break(doc)

    # === 1 ===
    h1(doc, "Apresentação e Identidade", numero=1)
    paragrafo(doc,
        "A Escola Bíblica Epignósis é uma instituição de formação cristã "
        "dedicada à educação bíblica, teológica, espiritual e ministerial, "
        "tendo como propósito conduzir homens e mulheres ao conhecimento "
        "pleno de Deus. Foi concebida para servir à Igreja de Cristo, "
        "promovendo uma formação equilibrada entre doutrina, espiritualidade, "
        "carácter e serviço cristão.")
    paragrafo(doc,
        "O seu compromisso fundamental é desenvolver discípulos maduros que "
        "conheçam profundamente as Escrituras, sejam guiados pelo Espírito "
        "Santo e vivam o Evangelho de forma prática, tornando-se instrumentos "
        "eficazes para a expansão do Reino de Deus na Igreja e na sociedade.")

    # === 2 ===
    h1(doc, "Significado do Nome — Epígnosis (ἐπίγνωσις)", numero=2)
    paragrafo(doc,
        "O nome “Epignósis” provém do substantivo grego ἐπίγνωσις (epígnōsis), "
        "frequentemente usado no Novo Testamento para designar não apenas um "
        "conhecimento intelectual (γνῶσις, gnōsis), mas um conhecimento "
        "profundo, pleno, experiencial e transformador de Deus.")
    paragrafo(doc,
        "Trata-se do conhecimento que penetra a mente, alcança o coração e "
        "molda a vida — aquele que o apóstolo Paulo persegue como meta suprema "
        "do discípulo (Filipenses 3.10) e que Pedro indica como caminho da "
        "graça multiplicada e da fuga das corrupções do mundo (2 Pedro 1.2-3).")
    citacao(doc,
        "Para o conhecimento (ἐπίγνωσιν) do mistério de Deus e Pai, e de "
        "Cristo, em quem estão escondidos todos os tesouros da sabedoria e "
        "da ciência.",
        "Colossenses 2.2-3")
    citacao(doc,
        "Graça e paz vos sejam multiplicadas no conhecimento "
        "(ἐπιγνώσει) de Deus e de Jesus, nosso Senhor.",
        "2 Pedro 1.2")

    # === 3 ===
    h1(doc, "Lema Institucional", numero=3)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("“Conhecer a Deus. Viver a Palavra. Manifestar o Reino.”")
    r.font.name = FONTE_TITULO
    r.font.size = Pt(16)
    r.font.italic = True
    r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA
    paragrafo(doc,
        "O lema sintetiza a tríplice vocação do aluno Epignósis: a busca de "
        "um conhecimento sólido e verdadeiro de Deus (mente), a apropriação "
        "existencial da Palavra (coração) e a manifestação prática do Reino "
        "na Igreja e no mundo (mãos).")

    # === 4 ===
    h1(doc, "Missão", numero=4)
    paragrafo(doc,
        "Conduzir cada aluno ao conhecimento pleno (epígnosis) de Deus por "
        "meio das Escrituras, da acção do Espírito Santo e da prática do "
        "Evangelho, formando discípulos maduros, líderes íntegros e ministros "
        "capacitados para servir ao Reino de Deus.")
    citacao(doc,
        "Ide, portanto, fazei discípulos de todas as nações, baptizando-os "
        "em nome do Pai, e do Filho, e do Espírito Santo; ensinando-os a "
        "guardar todas as coisas que eu vos tenho mandado.",
        "Mateus 28.19-20")

    # === 5 ===
    h1(doc, "Visão", numero=5)
    paragrafo(doc,
        "Ser uma referência na formação de discípulos, líderes e ministros "
        "comprometidos com a verdade das Escrituras, cheios do Espírito Santo, "
        "transformados à imagem de Cristo e preparados para impactar a Igreja "
        "e a sociedade por meio do Evangelho.")
    citacao(doc,
        "Até que todos cheguemos à unidade da fé, e ao conhecimento "
        "(ἐπίγνωσιν) do Filho de Deus, a homem perfeito, à medida da "
        "estatura completa de Cristo.",
        "Efésios 4.13")

    # === 6 ===
    h1(doc, "Valores", numero=6)
    paragrafo(doc,
        "Os valores institucionais constituem o solo ético, espiritual e "
        "doutrinário sobre o qual se edifica todo o ensino, a pesquisa, a "
        "convivência e o serviço da Escola Bíblica Epignósis:")

    valores = [
        ("Autoridade suprema das Sagradas Escrituras",
         "Reconhecemos a Bíblia como única regra infalível de fé e prática "
         "(2 Timóteo 3.16-17; 2 Pedro 1.20-21)."),
        ("Cristocentrismo",
         "Jesus Cristo é o centro de toda a revelação, do ensino e da formação "
         "(João 5.39; Colossenses 1.18)."),
        ("Dependência do Espírito Santo",
         "Reconhecemos que apenas o Espírito ilumina, convence, capacita e "
         "transforma (João 14.26; 16.13)."),
        ("Busca contínua do conhecimento pleno de Deus (epígnosis)",
         "Aspiramos ao conhecimento que produz comunhão e maturidade "
         "(Oseias 6.3; Filipenses 3.10)."),
        ("Santidade e transformação de vida",
         "A vida cristã é vocação à santificação prática (1 Pedro 1.15-16; "
         "Hebreus 12.14)."),
        ("Excelência no ensino e no aprendizado",
         "Servimos a Deus com qualidade, esforço e responsabilidade "
         "(Colossenses 3.23-24)."),
        ("Amor a Deus e ao próximo",
         "O duplo mandamento é o princípio reitor da convivência "
         "(Mateus 22.37-39)."),
        ("Integridade, humildade e carácter cristão",
         "A excelência académica caminha com a verdade interior "
         "(Salmo 51.6; Filipenses 2.3-5)."),
        ("Serviço ao Reino de Deus",
         "Toda formação visa servir, não dominar (Marcos 10.45)."),
        ("Unidade do Corpo de Cristo",
         "Promovemos o respeito, o diálogo e a comunhão entre os santos "
         "(Efésios 4.3-6; João 17.21)."),
        ("Compromisso com a sã doutrina",
         "Guardamos o depósito da fé que nos foi confiado (1 Timóteo 6.20; "
         "Tito 2.1)."),
        ("Discípulos que fazem discípulos",
         "Multiplicamos vidas que multiplicam vidas (2 Timóteo 2.2)."),
    ]
    for titulo_v, desc in valores:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.first_line_indent = Cm(-0.5)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run("•  ")
        r.font.bold = True; r.font.color.rgb = COR_SECUNDARIA
        r1 = p.add_run(f"{titulo_v}. ")
        r1.font.bold = True; r1.font.name = FONTE_TITULO; r1.font.size = Pt(12)
        r1.font.color.rgb = COR_PRIMARIA
        r2 = p.add_run(desc)
        r2.font.name = FONTE_CORPO; r2.font.size = Pt(12)

    # === 7 ===
    h1(doc, "Propósito", numero=7)
    paragrafo(doc,
        "Formar cristãos capazes de unir conhecimento bíblico sólido, vida "
        "espiritual profunda e prática ministerial eficaz, reflectindo o "
        "carácter de Cristo em todas as áreas da vida.")

    # === 8 ===
    h1(doc, "Filosofia de Ensino — As Quatro Dimensões", numero=8)
    paragrafo(doc,
        "A Escola Bíblica Epignósis acredita que o verdadeiro conhecimento "
        "de Deus não consiste apenas na aquisição de informações, mas na "
        "transformação integral da pessoa pelo poder da Palavra e do "
        "Espírito Santo (Romanos 12.2). Por isso, todo o ensino busca "
        "integrar quatro dimensões inseparáveis:")
    dims = [
        ("CONHECER", "Compreender correctamente as Escrituras", "Lucas 24.45; 2 Timóteo 2.15"),
        ("CRER",     "Desenvolver uma fé sólida e bíblica",     "Romanos 10.17; Hebreus 11.6"),
        ("VIVER",    "Aplicar a Palavra no quotidiano",         "Tiago 1.22; João 13.17"),
        ("SERVIR",   "Pôr os dons e talentos a serviço do Reino", "1 Pedro 4.10-11; Mateus 25.21"),
    ]
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Dimensão", "Descrição", "Fundamento Bíblico"]):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        r = p.add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    for nome, desc, ref in dims:
        row = tbl.add_row().cells
        row[0].text = nome
        row[1].text = desc
        row[2].text = ref
        for c in row:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = FONTE_CORPO
                    r.font.size = Pt(11)

    # === 9 ===
    h1(doc, "Os Quatro Pilares da Formação", numero=9)
    paragrafo(doc,
        "Toda a estrutura curricular da Escola é construída sobre quatro "
        "pilares interdependentes, que asseguram a integralidade da "
        "formação cristã:")
    pilares = [
        ("Conhecimento Bíblico",
         "Estudo profundo, sistemático e fiel das Escrituras "
         "(Salmo 119.105; Esdras 7.10)."),
        ("Formação Espiritual",
         "Intimidade com Deus, oração, santidade e vida no Espírito "
         "(João 15.4-5; Gálatas 5.16)."),
        ("Formação do Carácter",
         "Desenvolvimento das virtudes cristãs segundo o modelo de Cristo "
         "(Gálatas 5.22-23; 2 Pedro 1.5-7)."),
        ("Capacitação Ministerial",
         "Preparação prática para servir com excelência na Igreja e na missão "
         "(Efésios 4.11-12; 2 Timóteo 4.5)."),
    ]
    for t, d in pilares:
        h3(doc, t)
        paragrafo(doc, d)

    # === 10 ===
    h1(doc, "Objectivos Gerais", numero=10)
    paragrafo(doc, "Ao concluir a sua formação na Escola Bíblica Epignósis, espera-se que o aluno seja capaz de:")
    lista(doc, [
        "Conhecer profundamente a Bíblia, do Génesis ao Apocalipse.",
        "Interpretar correctamente as Escrituras à luz de princípios hermenêuticos sólidos.",
        "Desenvolver uma vida consistente de comunhão e oração com Deus.",
        "Demonstrar maturidade espiritual e equilíbrio emocional.",
        "Defender a fé cristã com mansidão e fundamentação bíblica (1 Pedro 3.15).",
        "Exercer os seus dons espirituais com equilíbrio e responsabilidade.",
        "Servir com excelência na Igreja local.",
        "Fazer discípulos e ensinar outros (2 Timóteo 2.2).",
        "Liderar com humildade, integridade e sabedoria.",
        "Manifestar o Reino de Deus por meio de uma vida e ministério transformados.",
    ], ordenada=True)

    # === 11 ===
    h1(doc, "Perfil do Egresso", numero=11)
    paragrafo(doc,
        "O egresso da Escola Bíblica Epignósis será reconhecido pela "
        "convergência de quatro qualidades essenciais — conhecimento, "
        "espiritualidade, carácter e ministério —, formando um discípulo "
        "íntegro e equilibrado.")

    h3(doc, "Quanto ao Conhecimento")
    lista(doc, [
        "Domínio das Sagradas Escrituras.",
        "Boa formação teológica geral.",
        "Capacidade de interpretar correctamente a Bíblia (hermenêutica).",
        "Conhecimento das principais doutrinas da fé cristã.",
    ])
    h3(doc, "Quanto à Espiritualidade")
    lista(doc, [
        "Vida devocional consistente.",
        "Dependência consciente do Espírito Santo.",
        "Vida de oração e intercessão.",
        "Busca activa de santidade.",
    ])
    h3(doc, "Quanto ao Carácter")
    lista(doc, [
        "Humildade.",
        "Integridade.",
        "Amor genuíno.",
        "Ética cristã.",
        "Fidelidade.",
    ])
    h3(doc, "Quanto ao Ministério")
    lista(doc, [
        "Capacidade para ensinar com fidelidade.",
        "Capacidade para discipular.",
        "Disposição para servir.",
        "Liderança bíblica e pastoral.",
        "Compromisso permanente com a missão da Igreja.",
    ])

    # === 12 ===
    h1(doc, "Nosso Compromisso", numero=12)
    paragrafo(doc, "A Escola Bíblica Epignósis compromete-se a oferecer uma formação que seja:")
    lista(doc, [
        "Bíblica em seu conteúdo.",
        "Cristocêntrica em sua mensagem.",
        "Guiada pelo Espírito Santo em sua prática.",
        "Teologicamente responsável.",
        "Espiritualmente saudável.",
        "Ministerialmente relevante.",
        "Prática para a vida diária.",
        "Transformadora em seus resultados.",
    ])

    # === 13 ===
    h1(doc, "Fundamentação Bíblica", numero=13)
    paragrafo(doc,
        "Os textos a seguir constituem o fundamento escriturístico da "
        "identidade e da vocação institucional da Escola Bíblica Epignósis:")
    citacao(doc, "Conheçamos, e prossigamos em conhecer ao Senhor; a sua saída, como a alva, é certa.", "Oseias 6.3")
    citacao(doc, "E não vos conformeis com este mundo, mas transformai-vos pela renovação do vosso entendimento.", "Romanos 12.2")
    citacao(doc, "Toda a Escritura é divinamente inspirada e proveitosa para ensinar, para redarguir, para corrigir, para instruir em justiça; para que o homem de Deus seja perfeito e perfeitamente instruído para toda a boa obra.", "2 Timóteo 3.16-17")
    citacao(doc, "Procura apresentar-te a Deus aprovado, como obreiro que não tem de que se envergonhar, que maneja bem a palavra da verdade.", "2 Timóteo 2.15")
    citacao(doc, "Para o conhecimento (ἐπίγνωσιν) do mistério de Deus e Pai, e de Cristo.", "Colossenses 2.2")

    selo_final(doc)

    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-001_Identidade_Institucional.docx")
    doc.save(out)
    print("OK:", out)


if __name__ == "__main__":
    gerar()
