"""
APOSTILA PILOTO — Escola Bíblica Epignósis
Apostila 1 — O Contexto Imediato
Módulo 3 (Regras de Interpretação) · Curso: Introdução à Hermenêutica
Escola de Hermenêutica · Instituto de Ciências Teológicas

Esta apostila é uma referência de preenchimento, mostrando o padrão editorial
da EBE em conteúdo real, com fundamentação bíblica, doutrinária e didáctica.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Apostila — O Contexto Imediato", "EBE-APO-001")

    # ====== CAPA ======
    doc.add_paragraph()
    inserir_logo(doc, LOGO_PATH, largura_cm=5.5)

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Conhecer a Deus. Viver a Palavra. Manifestar o Reino.")
    r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    r.font.italic = True; r.font.color.rgb = COR_SECUNDARIA

    p = doc.add_paragraph(); _add_horizontal_line(p, color=HEX_SECUNDARIA, size=6)

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    r = p.add_run("INSTITUTO DE CIÊNCIAS TEOLÓGICAS")
    r.font.name = FONTE_TITULO; r.font.size = Pt(11); r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Escola de Hermenêutica  ·  Curso «Introdução à Hermenêutica»  ·  Módulo 3 — Regras de Interpretação")
    r.font.name = FONTE_CORPO; r.font.size = Pt(10); r.font.color.rgb = COR_CITACAO

    doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("APOSTILA N.º  01")
    r.font.name = FONTE_TITULO; r.font.size = Pt(13); r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("O Contexto Imediato")
    r.font.name = FONTE_TITULO; r.font.size = Pt(30); r.font.bold = True
    r.font.color.rgb = COR_PRIMARIA

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("A primeira regra de toda interpretação fiel")
    r.font.name = FONTE_TITULO; r.font.size = Pt(13)
    r.font.italic = True; r.font.color.rgb = COR_TEXTO

    doc.add_paragraph(); doc.add_paragraph()

    # quadro de identificação
    tbl = doc.add_table(rows=4, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    dados = [
        ("Autor / Docente", "Direcção Pedagógica · Escola Bíblica Epignósis"),
        ("Carga horária estimada", "2 horas de estudo"),
        ("Nível formativo", "Nível 2 — Crescimento (Ser)"),
        ("Edição / Ano", "1.ª edição — 2026"),
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

    doc.add_paragraph()
    p = doc.add_paragraph(); _add_horizontal_line(p, color=HEX_SECUNDARIA, size=4)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Material didáctico oficial · Código EBE-APO-001 · 2026")
    r.font.name = FONTE_CORPO; r.font.size = Pt(9); r.font.color.rgb = COR_CITACAO

    page_break(doc)

    # ====== MARCO FILOSÓFICO ======
    add_marco_filosofico(doc)

    # ====== FICHA TÉCNICA ======
    h1(doc, "Ficha Técnica")
    paragrafo(doc,
        "Este material didáctico é propriedade intelectual da Escola Bíblica "
        "Epignósis (EBE), produzido para uso exclusivo no âmbito dos seus "
        "programas de formação. A sua reprodução, no todo ou em parte, "
        "depende de autorização institucional escrita.")
    lista(doc, [
        "Título da apostila: O Contexto Imediato.",
        "Curso: Introdução à Hermenêutica.",
        "Módulo: 3 — Regras de Interpretação.",
        "Autor / Docente: Direcção Pedagógica da Escola Bíblica Epignósis.",
        "Revisão pedagógica: Coordenação Acadêmica.",
        "Revisão doutrinária: Conselho Doutrinário.",
        "Versão bíblica de referência: Almeida Revista e Corrigida (ARC).",
        "Edição: 1.ª — 2026.",
        "Código institucional: EBE-APO-001.",
    ])
    citacao(doc,
        "Toda a Escritura é divinamente inspirada e proveitosa para ensinar, "
        "para redarguir, para corrigir, para instruir em justiça; para que o "
        "homem de Deus seja perfeito e perfeitamente instruído para toda a boa obra.",
        "2 Timóteo 3.16-17")

    page_break(doc)

    # ====== SUMÁRIO ======
    h1(doc, "Sumário")
    lista(doc, [
        "Apresentação da apostila",
        "Objectivos de aprendizagem",
        "Versículo-chave",
        "Texto-base para leitura",
        "1. Introdução — Por que a interpretação precisa de contexto",
        "2. Desenvolvimento do conceito central",
        "   2.1 Fundamentos bíblicos",
        "   2.2 O que é o «contexto imediato»",
        "   2.3 As três camadas do contexto imediato",
        "   2.4 Dúvidas e equívocos comuns",
        "   2.5 Quadro de destaque — para reter",
        "3. Aplicação prática",
        "4. Síntese e conclusão",
        "Exercícios de revisão",
        "Estudo bíblico complementar — Filipenses 4.13 em contexto",
        "Para a próxima apostila",
        "Glossário",
        "Bibliografia recomendada",
        "Anotações pessoais",
    ])

    page_break(doc)

    # ====== APRESENTAÇÃO ======
    h1(doc, "Apresentação da Apostila")
    paragrafo(doc,
        "Esta apostila inaugura o Módulo 3 — Regras de Interpretação — do "
        "Curso «Introdução à Hermenêutica». Nas apostilas anteriores, o aluno "
        "compreendeu o que é Hermenêutica (Apostilas do Módulo 1) e a "
        "inspiração das Escrituras (Apostilas do Módulo 2). Agora, começamos "
        "a aprender, de forma prática, como interpretar fielmente o texto bíblico.")
    paragrafo(doc,
        "O primeiro princípio é também o mais negligenciado nas igrejas: "
        "“um texto fora do contexto torna-se pretexto”. Nesta apostila, vamos "
        "estudar o que é o contexto imediato — a camada mais próxima de "
        "qualquer versículo —, por que ele é decisivo para uma interpretação "
        "fiel, e como aplicá-lo na nossa leitura da Bíblia.")
    paragrafo(doc,
        "Ao final do estudo, o aluno terá em mãos uma ferramenta simples, "
        "bíblica e poderosa, capaz de evitar a maior parte dos erros de "
        "interpretação cometidos no púlpito, no grupo pequeno e na vida devocional.")

    # ====== OBJECTIVOS ======
    h1(doc, "Objectivos de Aprendizagem")
    paragrafo(doc, "Ao concluir o estudo desta apostila, o(a) aluno(a) será capaz de:")
    lista(doc, [
        "CONHECER — definir o que é “contexto imediato” e identificar as suas três camadas (versículos vizinhos, parágrafo e capítulo).",
        "CRER — interiorizar a convicção de que toda a interpretação fiel começa pelo respeito ao contexto em que o texto bíblico foi escrito.",
        "VIVER — aplicar o princípio do contexto imediato à sua leitura devocional diária da Bíblia, evitando conclusões precipitadas.",
        "SERVIR — corrigir, com mansidão e fundamento, usos descontextualizados de versículos bíblicos no ensino, na pregação e nas redes sociais.",
    ], ordenada=True)

    # ====== VERSÍCULO-CHAVE ======
    h1(doc, "Versículo-Chave")
    citacao(doc,
        "Procura apresentar-te a Deus aprovado, como obreiro que não tem de "
        "que se envergonhar, que maneja bem a palavra da verdade.",
        "2 Timóteo 2.15")

    # ====== TEXTO-BASE ======
    h1(doc, "Texto-Base para Leitura")
    paragrafo(doc,
        "Antes de iniciar o estudo, leia atentamente, em sua Bíblia "
        "(Almeida Revista e Corrigida), a seguinte passagem, observando "
        "tudo o que envolve o famoso versículo de Filipenses 4.13:")
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Filipenses 4.10-20")
    r.font.name = FONTE_TITULO; r.font.size = Pt(14); r.font.bold = True
    r.font.color.rgb = COR_SECUNDARIA

    page_break(doc)

    # ====== 1. INTRODUÇÃO ======
    h1(doc, "Introdução — Por que a Interpretação Precisa de Contexto", numero=1)
    paragrafo(doc,
        "Imagine alguém que, ao abrir uma carta familiar, lê apenas uma frase "
        "isolada do meio da página e tira dela conclusões definitivas. Esse "
        "leitor certamente entenderá mal o que foi escrito. A Bíblia, embora "
        "seja a Palavra de Deus, foi entregue como literatura — livros, "
        "cartas, profecias, poemas, narrativas históricas — escritos a "
        "destinatários concretos, em situações concretas. Por isso, todo "
        "versículo só é plenamente compreendido dentro do conjunto em que "
        "se encontra.")
    paragrafo(doc,
        "A história da Igreja é repleta de exemplos de doutrinas erradas que "
        "surgiram por leituras descontextualizadas. Hoje, com a facilidade "
        "de partilhar versículos isolados em imagens e redes sociais, este "
        "perigo aumentou. Para o aluno Epignósis, conhecer o contexto não é "
        "uma exigência académica fria — é um acto de reverência à Palavra "
        "de Deus e de amor à verdade.")
    citacao(doc,
        "Mas o homem natural não compreende as coisas do Espírito de Deus, "
        "porque lhe parecem loucura; e não pode entendê-las, porque elas se "
        "discernem espiritualmente.",
        "1 Coríntios 2.14")
    paragrafo(doc,
        "O Espírito Santo, que inspirou a Bíblia, é o mesmo que ilumina o "
        "intérprete. Por isso, hermenêutica não é apenas técnica: é "
        "responsabilidade espiritual diante de Deus.")

    # ====== 2. DESENVOLVIMENTO ======
    h1(doc, "Desenvolvimento do Conceito Central", numero=2)

    h2(doc, "Fundamentos bíblicos", numero="2.1")
    paragrafo(doc,
        "A própria Escritura ensina, pelo exemplo, a importância de "
        "interpretar respeitando o contexto. Observemos três passagens-chave:")

    h3(doc, "a) Jesus respondendo a Satanás (Mateus 4.1-11)")
    paragrafo(doc,
        "No deserto, o Diabo cita o Salmo 91.11-12 para induzir Jesus a "
        "atirar-se do pináculo do templo. O texto citado é verdadeiro — é a "
        "Palavra de Deus —, mas é usado fora de propósito. Jesus responde "
        "também com a Escritura (Deuteronómio 6.16), mostrando que a "
        "interpretação fiel exige confrontar texto com texto, no contexto.")
    citacao(doc,
        "Disse-lhe Jesus: Também está escrito: Não tentarás o Senhor teu Deus.",
        "Mateus 4.7")

    h3(doc, "b) Os bereanos examinando as Escrituras (Actos 17.10-11)")
    paragrafo(doc,
        "Ao receberem a pregação de Paulo, os bereanos não a recusaram nem "
        "a aceitaram cegamente: examinavam-na “cada dia” à luz das "
        "Escrituras. Lucas chama-os, por isso, de “mais nobres”. O método "
        "berenano pressupõe leitura cuidadosa, atenta ao que cada texto "
        "realmente diz no seu lugar.")
    citacao(doc,
        "Estes foram mais nobres do que os que estavam em Tessalónica, "
        "porque de bom grado receberam a palavra, examinando cada dia nas "
        "Escrituras se estas coisas eram assim.",
        "Actos 17.11")

    h3(doc, "c) Paulo exortando Timóteo (2 Timóteo 2.15)")
    paragrafo(doc,
        "O verbo grego traduzido por “manejar bem” (ὀρθοτομοῦντα — "
        "orthotomounta) significa literalmente “cortar em linha recta”. Era "
        "usado para descrever o trabalho do agricultor que abre um sulco "
        "direito ou do pedreiro que talha a pedra com precisão. Aplicado à "
        "Palavra, indica precisão hermenêutica: não distorcer, não acrescentar, "
        "não cortar fora do lugar.")

    h2(doc, "O que é o «contexto imediato»", numero="2.2")
    paragrafo(doc,
        "Chamamos de contexto imediato à porção do texto bíblico que está "
        "directamente em volta do versículo que estudamos. É a primeira "
        "fronteira de sentido, a mais próxima e, por isso, a mais decisiva.")
    paragrafo(doc,
        "Quando estudamos a Bíblia, lemos sempre, no mínimo, três camadas "
        "concêntricas de contexto. Nas próximas apostilas estudaremos o "
        "contexto histórico (Apostila 2), o contexto cultural (Apostila 3) "
        "e o contexto gramatical (Apostila 4). Aqui, ficamos com a base de "
        "tudo: o contexto imediato.")

    # Definição em destaque
    tbl = doc.add_table(rows=1, cols=1)
    cell = tbl.rows[0].cells[0]
    _shade_cell(cell, "E8F1EC")
    p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run("✦ Definição:  ")
    r.font.bold = True; r.font.color.rgb = COR_SECUNDARIA
    r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r2 = p.add_run(
        "Contexto imediato é o conjunto formado pelos versículos anteriores "
        "e posteriores, pelo parágrafo e pelo capítulo onde se encontra o "
        "texto que estudamos. Ele responde à pergunta: «de que o autor está "
        "a falar exactamente aqui?»")
    r2.font.name = FONTE_CORPO; r2.font.size = Pt(11); r2.font.italic = True

    page_break(doc)

    h2(doc, "As três camadas do contexto imediato", numero="2.3")
    paragrafo(doc, "Para aplicar correctamente esta primeira regra, é útil pensar em três camadas, da mais estreita à mais larga:")

    # Tabela de camadas
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Camada", "O que considerar", "Pergunta-guia"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    camadas = [
        ("1. Versículos vizinhos",
         "Os 2 a 5 versículos antes e depois.",
         "O que o autor diz logo antes e logo depois?"),
        ("2. Parágrafo",
         "A unidade de pensamento (geralmente marcada nas Bíblias de estudo).",
         "Qual o argumento ou narrativa em curso?"),
        ("3. Capítulo",
         "O bloco maior, com início e fim claros.",
         "Qual é o tema geral desta secção do livro?"),
    ]
    for c in camadas:
        row = tbl.add_row().cells
        for i, v in enumerate(c):
            row[i].text = v
            for p in row[i].paragraphs:
                for r in p.runs:
                    r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    paragrafo(doc,
        "Estas três camadas — vizinhos, parágrafo e capítulo — funcionam "
        "como círculos concêntricos. Quanto mais próximo o círculo, maior o "
        "peso interpretativo. Um versículo «depende» mais do seu parágrafo "
        "do que do capítulo inteiro, e mais do capítulo do que do livro todo.")

    h2(doc, "Dúvidas e equívocos comuns", numero="2.4")

    h3(doc, "Equívoco 1 — “Mas a Bíblia diz!”")
    paragrafo(doc,
        "Muitas vezes citamos um versículo isolado, como se a sua presença "
        "no texto sagrado bastasse para sustentar qualquer afirmação. O "
        "Diabo, em Mateus 4, também citou “a Bíblia”. A questão não é se o "
        "texto está na Escritura, mas se está sendo lido como Deus o "
        "entregou.")

    h3(doc, "Equívoco 2 — “Mas o versículo me toca!”")
    paragrafo(doc,
        "O Espírito Santo pode, sem dúvida, usar um versículo isolado para "
        "abençoar uma alma. Mas a aplicação devocional pessoal nunca pode "
        "ignorar o sentido original. Deus não contradiz o que Ele mesmo "
        "inspirou. Uma boa aplicação devocional respeita sempre o sentido "
        "original do texto.")

    h3(doc, "Equívoco 3 — “Toda interpretação é pessoal.”")
    paragrafo(doc,
        "Pedro afirma o contrário com firmeza:")
    citacao(doc,
        "Sabendo primeiramente isto: que nenhuma profecia da Escritura é de "
        "particular interpretação.",
        "2 Pedro 1.20")
    paragrafo(doc,
        "O texto tem um sentido original, dado por Deus ao autor humano. "
        "O nosso trabalho não é inventar sentidos novos, mas descobrir, com "
        "humildade e dependência do Espírito, o que Deus quis dizer.")

    # Quadro destaque
    h2(doc, "Quadro de Destaque — para reter", numero="2.5")
    tbl = doc.add_table(rows=1, cols=1)
    cell = tbl.rows[0].cells[0]
    _shade_cell(cell, "E8F1EC")
    p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run("✦ Para reter:  ")
    r.font.bold = True; r.font.color.rgb = COR_SECUNDARIA
    r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r2 = p.add_run(
        "Antes de aplicar qualquer versículo, leia ao menos o parágrafo "
        "inteiro em que ele se encontra. Pergunte: “De que o autor está "
        "realmente a falar aqui?” Esta única pergunta evita 80% dos erros "
        "de interpretação.")
    r2.font.name = FONTE_CORPO; r2.font.size = Pt(11); r2.font.italic = True

    page_break(doc)

    # ====== 3. APLICAÇÃO ======
    h1(doc, "Aplicação Prática", numero=3)
    paragrafo(doc,
        "A regra do contexto imediato deve transformar a forma como cada "
        "discípulo Epignósis lê a Bíblia, prega, ensina e partilha versículos "
        "na vida quotidiana. Vejamos cinco esferas de aplicação:")
    lista(doc, [
        "Na vida pessoal e devocional — adopte o hábito de ler sempre o "
        "parágrafo inteiro antes de meditar num versículo. Use uma Bíblia "
        "com divisões claras de parágrafo. Pergunte a Deus, em oração, a "
        "compreensão do contexto.",
        "Na família — quando ensinar uma passagem aos filhos ou ao "
        "cônjuge, mostre primeiro o «cenário» do texto, contando "
        "brevemente o que vem antes e depois. Eles aprenderão, pela prática, "
        "a ler bem.",
        "Na igreja local — ao preparar uma classe ou estudo bíblico, "
        "comece sempre por ler o capítulo inteiro de onde tirou o texto. "
        "Resista à tentação de saltar directamente para “pontos de aplicação”.",
        "No trabalho e na sociedade — ao partilhar versículos com colegas, "
        "amigos ou nas redes sociais, evite isolar frases impactantes que, "
        "lidas no contexto, dizem outra coisa. Um “meme bíblico” errado "
        "fere mais o testemunho do que ajuda.",
        "No exercício ministerial — todo pregador, mestre e líder Epignósis "
        "deve assumir o compromisso público de jamais pregar um versículo "
        "sem antes ter lido o seu contexto imediato.",
    ], ordenada=True)

    # ====== 4. SÍNTESE ======
    h1(doc, "Síntese e Conclusão", numero=4)
    paragrafo(doc,
        "Estudámos, nesta apostila, que o contexto imediato — formado pelos "
        "versículos vizinhos, pelo parágrafo e pelo capítulo — é a primeira "
        "e indispensável fronteira de sentido de qualquer texto bíblico. "
        "Aprendemos que respeitar o contexto não é meramente um exercício "
        "intelectual: é uma forma concreta de honrar a Deus, que entregou "
        "a Sua Palavra com sentido próprio.")
    paragrafo(doc,
        "Que esta primeira regra de interpretação seja, a partir de hoje, "
        "um hábito espiritual em sua vida: antes de aplicar, contextualize. "
        "Antes de ensinar, contextualize. Antes de partilhar, contextualize.")
    citacao(doc,
        "Procura apresentar-te a Deus aprovado, como obreiro que não tem de "
        "que se envergonhar, que maneja bem a palavra da verdade.",
        "2 Timóteo 2.15")

    page_break(doc)

    # ====== EXERCÍCIOS ======
    h1(doc, "Exercícios de Revisão")
    paragrafo(doc,
        "Responda às questões a seguir com base no conteúdo desta apostila "
        "e na sua leitura bíblica.")

    h3(doc, "I — Verifique a sua compreensão")
    lista(doc, [
        "Defina, com as suas próprias palavras, o que é “contexto imediato”.",
        "Quais são as três camadas do contexto imediato? Dê um exemplo de cada uma a partir da sua leitura.",
        "Por que razão Mateus 4 (a tentação de Jesus) é um exemplo bíblico da importância do contexto?",
        "Qual o significado literal do verbo grego “orthotomounta” em 2 Timóteo 2.15?",
        "Cite e explique brevemente o princípio expresso em 2 Pedro 1.20.",
    ], ordenada=True)

    h3(doc, "II — Reflexão pessoal")
    lista(doc, [
        "Lembra-se de algum versículo que você costumava aplicar de uma forma e que, ao ler em contexto, percebeu que dizia outra coisa? Qual?",
        "Que hábito concreto você adoptará a partir desta semana, para respeitar o contexto imediato na sua leitura diária?",
        "Que oração você fará a Deus para crescer como leitor fiel da Sua Palavra?",
    ], ordenada=True)

    h3(doc, "III — Ministério e serviço")
    lista(doc, [
        "Como você explicaria, em 3 minutos, a um irmão mais novo na fé, a importância de ler o contexto antes de aplicar um versículo?",
        "Que situação concreta em sua igreja (estudo, pregação, partilha) pode ser corrigida ou enriquecida com esta regra?",
    ], ordenada=True)

    # ====== ESTUDO BÍBLICO ======
    h1(doc, "Estudo Bíblico Complementar — Filipenses 4.13 em Contexto")
    paragrafo(doc,
        "“Posso todas as coisas naquele que me fortalece.” Este é, "
        "provavelmente, o versículo mais aplicado fora do seu contexto em "
        "toda a Bíblia. É citado em jogos de futebol, em provas escolares, "
        "em empreendimentos profissionais. Mas o que Paulo realmente quis "
        "dizer? Leia atentamente Filipenses 4.10-20 e responda:")
    lista(doc, [
        "Qual é a situação concreta vivida por Paulo no momento em que escreve? (vv. 10-11)",
        "Que “coisas” Paulo afirma ter aprendido? (vv. 11-12)",
        "À luz dos versículos 11 e 12, o que significa exactamente o “posso todas as coisas” do versículo 13?",
        "Esta passagem promete sucesso material? Justifique a partir do contexto.",
        "Como você passará a citar e a aplicar Filipenses 4.13 a partir de agora?",
    ], ordenada=True)

    # ====== PRÓXIMA APOSTILA ======
    h1(doc, "Para a Próxima Apostila")
    paragrafo(doc,
        "Na próxima apostila — Apostila 2 — estudaremos o Contexto "
        "Histórico: como o conhecimento da época em que o texto foi "
        "escrito ilumina o seu sentido. Para se preparar, leia previamente "
        "Actos 17.16-34 (o discurso de Paulo no Areópago) e reflicta sobre "
        "as seguintes perguntas:")
    lista(doc, [
        "O que mudaria na pregação de Paulo se ele não conhecesse a cultura ateniense?",
        "Que dados históricos da passagem ajudam a entender melhor a mensagem?",
    ])

    page_break(doc)

    # ====== GLOSSÁRIO ======
    h1(doc, "Glossário")
    paragrafo(doc, "Definições breves dos termos-chave utilizados nesta apostila.")
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Termo", "Definição"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]
        r = p.add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    termos = [
        ("Hermenêutica", "Ciência e arte da interpretação. Aplicada à Bíblia, é o conjunto de princípios que orientam o leitor a compreender fielmente o sentido das Escrituras."),
        ("Contexto",     "Conjunto de elementos (textuais, históricos, culturais, gramaticais) que envolvem um texto e ajudam a determinar o seu sentido."),
        ("Contexto imediato", "Camada mais próxima do contexto: versículos vizinhos, parágrafo e capítulo onde se encontra o texto estudado."),
        ("Exegese",      "Acto de extrair (do grego ex-egēsis, “tirar de dentro”) o sentido original do texto, em oposição à eisegese, que é introduzir sentidos estranhos ao texto."),
        ("Orthotomounta (ὀρθοτομοῦντα)", "Particípio grego em 2 Timóteo 2.15, traduzido por “maneja bem”. Significa literalmente “cortar em linha recta”, indicando precisão hermenêutica."),
        ("Epígnosis (ἐπίγνωσις)", "Conhecimento pleno, profundo e experimental de Deus — meta de todo o ensino da Escola Bíblica Epignósis."),
    ]
    for termo, defin in termos:
        row = tbl.add_row().cells
        row[0].text = termo; row[1].text = defin
        for c in row:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = FONTE_CORPO; r.font.size = Pt(10)
        for p in row[0].paragraphs:
            for r in p.runs:
                r.font.bold = True; r.font.color.rgb = COR_PRIMARIA

    # ====== BIBLIOGRAFIA ======
    h1(doc, "Bibliografia Recomendada")
    lista(doc, [
        "Bíblia Sagrada. Tradução de João Ferreira de Almeida, Revista e Corrigida.",
        "FEE, Gordon D.; STUART, Douglas. Entendes o que lês? Um guia para entender a Bíblia com auxílio da exegese e da hermenêutica. São Paulo: Vida Nova.",
        "VIRKLER, Henry A. Hermenêutica avançada: princípios e processos de interpretação bíblica. São Paulo: Vida.",
        "BERKHOF, Louis. Princípios de interpretação bíblica. São Paulo: Cultura Cristã.",
        "LOPES, Augustus Nicodemus. A Bíblia e seus intérpretes. São Paulo: Cultura Cristã.",
    ])

    # ====== ANOTAÇÕES ======
    h1(doc, "Anotações Pessoais")
    for _ in range(12):
        p = doc.add_paragraph(); _add_horizontal_line(p, color="C8C8C8", size=4)

    selo_final(doc)

    out = os.path.join(os.path.dirname(__file__), "EBE-APO-001_Apostila_Piloto_O_Contexto_Imediato.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
