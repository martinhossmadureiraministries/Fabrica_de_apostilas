"""
MANUAL DO ALUNO — Escola Bíblica Epignósis
Versão condensada e prática do Regimento, com dicas espirituais e
orientações concretas para a vida acadêmica do(a) aluno(a).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def _quadro_destaque(doc, titulo, corpo, cor_fundo="E8F1EC"):
    tbl = doc.add_table(rows=1, cols=1)
    cell = tbl.rows[0].cells[0]
    _shade_cell(cell, cor_fundo)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"✦ {titulo}")
    r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r.font.color.rgb = COR_PRIMARIA
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    r2 = p2.add_run(corpo)
    r2.font.name = FONTE_CORPO; r2.font.size = Pt(11)


def _dica(doc, texto):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("💡  ")
    r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r.font.color.rgb = COR_SECUNDARIA; r.font.bold = True
    r2 = p.add_run(texto)
    r2.font.name = FONTE_CORPO; r2.font.size = Pt(11)


def gerar():
    doc = novo_documento("Manual do Aluno", "EBE-MAN-ALU")

    add_capa(doc,
        supratitulo="Documento de Acolhimento N.º 1",
        titulo="Manual do Aluno",
        subtitulo="Guia prático para a sua jornada formativa na Escola Bíblica Epignósis",
        codigo="EBE-MAN-ALU", ano="2026")
    add_marco_filosofico(doc)

    # ====== CARTA DE BOAS-VINDAS ======
    h1(doc, "Carta de Boas-Vindas")
    paragrafo(doc, "Querido(a) aluno(a),")
    paragrafo(doc,
        "Seja muito bem-vindo(a) à Escola Bíblica Epignósis. Receba, em "
        "primeiro lugar, o nosso abraço fraterno em nome do nosso Senhor "
        "Jesus Cristo. O facto de ter chegado até aqui já é, em si mesmo, "
        "fruto da graça de Deus. Acreditamos que cada matrícula é uma "
        "resposta concreta a um chamado divino — talvez um chamado claro, "
        "talvez ainda um sussurro. Em qualquer caso, Deus o(a) trouxe.")
    paragrafo(doc,
        "Este manual foi preparado para ajudá-lo(a) a percorrer com sabedoria, "
        "alegria e disciplina o caminho da formação Epignósis. Aqui encontrará "
        "as orientações essenciais sobre a Escola, os seus direitos e deveres, "
        "as suas responsabilidades espirituais e académicas, e dicas práticas "
        "para tirar o máximo proveito de cada apostila, módulo e curso.")
    paragrafo(doc,
        "Mais do que um regulamento, este Manual é um convite. Convite a "
        "estudar com seriedade, a viver com integridade, a servir com amor "
        "e a manifestar o Reino de Deus em cada esfera da sua vida.")
    citacao(doc,
        "E não vos conformeis com este mundo, mas transformai-vos pela "
        "renovação do vosso entendimento, para que experimenteis qual seja "
        "a boa, agradável e perfeita vontade de Deus.",
        "Romanos 12.2")
    paragrafo(doc,
        "Que esta jornada seja, antes de tudo, um encontro renovado e "
        "profundo com Deus. Estamos a orar por si.")
    paragrafo(doc, "Em Cristo,", italic=True)
    paragrafo(doc, "Direcção e Corpo Docente da Escola Bíblica Epignósis.", italic=True)

    # ====== SUMÁRIO ======
    h1(doc, "Sumário")
    lista(doc, [
        "1.  Quem somos — A identidade da Escola Bíblica Epignósis",
        "2.  O que é o conhecimento Epignósis",
        "3.  A sua jornada formativa — 4 níveis, 10 institutos",
        "4.  Como funciona a arquitectura (Apostila → Diploma)",
        "5.  Os seus direitos como aluno",
        "6.  Os seus deveres como aluno",
        "7.  Conduta cristã esperada",
        "8.  Como estudar bem — método Epignósis em 7 passos",
        "9.  Como ler bem uma apostila",
        "10. Vida devocional do(a) estudante",
        "11. Frequência, avaliações e certificação",
        "12. Pré-requisitos e progressão",
        "13. Ética acadêmica e plágio",
        "14. Disciplina e restauração",
        "15. Acompanhamento pastoral e mentoria",
        "16. Modalidades de estudo (presencial · híbrido · on-line)",
        "17. Convivência saudável e unidade",
        "18. Documentos institucionais que regem a sua matrícula",
        "19. Glossário Epignósis",
        "20. Compromisso final do(a) aluno(a)",
    ])
    page_break(doc)

    # ====== 1. IDENTIDADE ======
    h1(doc, "Quem Somos — A Identidade da Escola Bíblica Epignósis", numero=1)
    paragrafo(doc,
        "A Escola Bíblica Epignósis é uma instituição de formação cristã "
        "dedicada à educação bíblica, teológica, espiritual e ministerial. "
        "Existimos para servir à Igreja de Cristo, formando discípulos "
        "maduros, líderes íntegros e ministros capacitados.")
    h3(doc, "Nosso lema")
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Conhecer a Deus.  Viver a Palavra.  Manifestar o Reino.")
    r.font.name = FONTE_TITULO; r.font.size = Pt(14); r.font.italic = True
    r.font.bold = True; r.font.color.rgb = COR_PRIMARIA

    h3(doc, "Nossa missão")
    paragrafo(doc,
        "Conduzir cada aluno ao conhecimento pleno (epígnosis) de Deus por "
        "meio das Escrituras, da acção do Espírito Santo e da prática do "
        "Evangelho.")

    h3(doc, "Nossa visão")
    paragrafo(doc,
        "Ser uma referência na formação de discípulos, líderes e ministros "
        "comprometidos com a verdade das Escrituras, cheios do Espírito Santo, "
        "transformados à imagem de Cristo e preparados para impactar a "
        "Igreja e a sociedade pelo Evangelho.")

    # ====== 2. EPÍGNOSIS ======
    h1(doc, "O Que É o Conhecimento Epignósis", numero=2)
    paragrafo(doc,
        "O nome da nossa Escola vem do substantivo grego ἐπίγνωσις "
        "(epígnōsis), que aparece muitas vezes no Novo Testamento. "
        "Diferente do simples conhecimento intelectual (γνῶσις, gnōsis), "
        "epígnosis indica um conhecimento profundo, pleno, experiencial e "
        "transformador de Deus.")
    paragrafo(doc, "Por isso, na nossa Escola, conhecimento NÃO é:")
    lista(doc, [
        "Apenas acumular informações bíblicas.",
        "Aprovar em provas e esquecer no dia seguinte.",
        "Adquirir argumentos para vencer discussões.",
        "Sentir-se superior a outros cristãos.",
    ])
    paragrafo(doc, "Conhecimento na Epignósis É:")
    lista(doc, [
        "Compreender as Escrituras com a mente.",
        "Crer profundamente com o coração.",
        "Viver com integridade no quotidiano.",
        "Servir com humildade no Reino de Deus.",
    ])
    citacao(doc,
        "Graça e paz vos sejam multiplicadas no conhecimento (ἐπιγνώσει) de "
        "Deus, e de Jesus, nosso Senhor.",
        "2 Pedro 1.2")

    # ====== 3. JORNADA ======
    h1(doc, "A Sua Jornada Formativa — 4 Níveis, 10 Institutos", numero=3)
    paragrafo(doc, "A Escola Bíblica Epignósis está organizada em quatro grandes níveis formativos progressivos:")
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Nível", "Verbo-chave", "Objectivo"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    niveis = [
        ("1 — Discípulo",     "CONHECER",   "Fundamentos da fé cristã (≈ 380 h)."),
        ("2 — Crescimento",   "SER",        "Maturidade espiritual e doutrinária (≈ 385 h)."),
        ("3 — Servir",        "MINISTÉRIO", "Capacitação ministerial prática (≈ 830 h)."),
        ("4 — Multiplicação", "REINO",      "Formação de líderes e multiplicadores (≈ 700 h)."),
    ]
    for n in niveis:
        row = tbl.add_row().cells
        for i, v in enumerate(n):
            row[i].text = v
            for p in row[i].paragraphs:
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    paragrafo(doc, "Esses níveis articulam-se em dez institutos:")
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

    _quadro_destaque(doc,
        "Para saber mais",
        "Consulte o Mapa Oficial de Cursos (EBE-DOC-006) para ver todas as "
        "Escolas e cursos disponíveis em cada Instituto, e a Duração Oficial "
        "(EBE-DOC-007) para a carga horária de cada um.")

    # ====== 4. ARQUITETURA ======
    h1(doc, "Como Funciona a Arquitectura (Apostila → Diploma)", numero=4)
    paragrafo(doc, "A formação Epignósis está organizada em sete níveis hierárquicos. Conhecer essa estrutura ajuda-o(a) a saber sempre onde está e para onde caminha:")
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Unidade", "Composição", "Carga horária"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    for r_data in [
        ("Apostila",   "10–15 páginas",  "1–3 horas"),
        ("Módulo",     "3–5 apostilas",  "4–10 horas"),
        ("Curso",      "3–6 módulos",    "20–60 horas"),
        ("Escola",     "2–4 cursos",     "60–180 horas"),
        ("Programa",   "Conjunto de cursos", "Variável"),
        ("Instituto",  "3–5 escolas",    "200–600 horas"),
        ("Formação completa Epignósis", "10 institutos", "2.200–2.400 horas"),
    ]:
        row = tbl.add_row().cells
        for i, v in enumerate(r_data):
            row[i].text = v
            for p in row[i].paragraphs:
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    paragrafo(doc,
        "A cada etapa concluída, você recebe um Certificado oficial. Ao "
        "concluir todos os níveis, recebe o Diploma de Formação Completa "
        "Epignósis.")

    page_break(doc)

    # ====== 5. DIREITOS ======
    h1(doc, "Os Seus Direitos Como Aluno(a)", numero=5)
    paragrafo(doc, "Conforme o Regimento Acadêmico (EBE-DOC-004, Art. 9.º), você tem direito a:")
    lista(doc, [
        "Receber ensino fundamentado nas Escrituras e de qualidade.",
        "Utilizar todos os materiais didácticos disponibilizados pela Escola.",
        "Ser tratado(a) com respeito, dignidade e imparcialidade.",
        "Participar activamente das actividades acadêmicas e devocionais.",
        "Solicitar esclarecimentos sobre as suas avaliações.",
        "Ser acompanhado(a) pastoral e pedagogicamente.",
        "Receber certificação adequada ao concluir cada etapa.",
        "Ter preservada a confidencialidade das suas informações pessoais.",
    ], ordenada=True)

    # ====== 6. DEVERES ======
    h1(doc, "Os Seus Deveres Como Aluno(a)", numero=6)
    paragrafo(doc, "Conforme o Regimento Acadêmico (Art. 10.º), você compromete-se a:")
    lista(doc, [
        "Respeitar e honrar os princípios e a identidade doutrinária da Escola.",
        "Manter postura cristã dentro e fora do ambiente acadêmico.",
        "Cumprir, dentro dos prazos, as actividades propostas.",
        "Preservar o património material e intelectual da instituição.",
        "Respeitar professores, colegas e colaboradores.",
        "Zelar pela unidade, pelo amor fraterno e pela boa convivência.",
        "Comunicar à Coordenação eventuais impedimentos ou dificuldades.",
        "Submeter-se à disciplina acadêmica e espiritual da Escola.",
    ], ordenada=True)
    citacao(doc, "Tudo quanto fizerdes, fazei-o de todo o coração, como ao Senhor, e não aos homens.", "Colossenses 3.23")

    # ====== 7. CONDUTA ======
    h1(doc, "Conduta Cristã Esperada", numero=7)
    paragrafo(doc,
        "A Escola Bíblica Epignósis espera de cada aluno(a) uma vida "
        "coerente com o Evangelho. Isso é mais do que “bons modos”: é "
        "santidade prática.")

    h3(doc, "Atitudes encorajadas")
    lista(doc, [
        "Amor fraterno (João 13.34-35).",
        "Respeito mútuo (Romanos 12.10).",
        "Honestidade em todas as palavras e acções.",
        "Humildade no aprender e no servir.",
        "Espírito de cooperação e unidade.",
        "Domínio próprio e mansidão (Gálatas 5.22-23).",
    ])
    h3(doc, "Atitudes não toleradas")
    lista(doc, [
        "Desrespeito a professores, colegas ou colaboradores.",
        "Divisão, fofoca, calúnia, maledicência.",
        "Discriminação de qualquer natureza.",
        "Desonestidade acadêmica (plágio, cola, fraude).",
        "Imoralidade pública.",
        "Comportamento ofensivo ou agressivo em redes sociais que envolva membros da Escola.",
    ])

    # ====== 8. MÉTODO ======
    h1(doc, "Como Estudar Bem — Método Epignósis em 7 Passos", numero=8)
    paragrafo(doc, "Sugerimos a seguinte rotina para cada nova apostila:")
    lista(doc, [
        "ORE — peça ao Espírito Santo iluminação antes de abrir o material (Salmo 119.18).",
        "LEIA o texto-base na Bíblia (ARC), com atenção, sem pressa.",
        "ESTUDE a apostila do início ao fim, sem saltar secções.",
        "ANOTE — sublinhe, escreva nas margens, marque palavras novas.",
        "MEMORIZE o versículo-chave durante a semana.",
        "APLIQUE — pergunte: “Como isto muda a minha vida hoje?”",
        "ENSINE alguém — partilhe o aprendido com um irmão (2 Tm 2.2).",
    ], ordenada=True)

    _quadro_destaque(doc,
        "Regra de ouro",
        "O que você não consegue explicar com clareza a outra pessoa, você "
        "ainda não compreendeu de verdade. Ensinar é a prova final de que "
        "aprendeu.")

    # ====== 9. COMO LER APOSTILA ======
    h1(doc, "Como Ler Bem Uma Apostila", numero=9)
    paragrafo(doc, "Cada apostila Epignósis segue uma estrutura padronizada. Aproveite-a:")
    lista(doc, [
        "Comece sempre pela Apresentação — entenderá o lugar daquele tema no curso.",
        "Memorize o Versículo-Chave logo no início da semana.",
        "Leia o Texto-Base na sua Bíblia ANTES de avançar.",
        "Marque palavras do Glossário à medida que aparecem.",
        "No quadro “Para reter”, sublinhe e revisite ao longo da semana.",
        "Não pule os Exercícios — eles consolidam a aprendizagem.",
        "Faça as Anotações Pessoais; elas serão preciosas no futuro.",
    ])

    _dica(doc, "Tenha um caderno dedicado exclusivamente aos estudos Epignósis.")
    _dica(doc, "Reserve um horário fixo na semana para os seus estudos — a disciplina abençoa mais que a inspiração.")
    _dica(doc, "Estude com a Bíblia aberta, sempre. A apostila é instrumento; a Bíblia é a fonte.")

    page_break(doc)

    # ====== 10. DEVOCIONAL ======
    h1(doc, "Vida Devocional do(a) Estudante", numero=10)
    paragrafo(doc,
        "O aluno Epignósis estuda como quem ora, e ora como quem estuda. "
        "Não há epígnosis sem comunhão com Deus. Por isso, recomendamos "
        "fortemente um ritmo devocional diário simples e consistente:")

    h3(doc, "Ritmo diário sugerido (mínimo 30 minutos)")
    lista(doc, [
        "5 min — Oração inicial: peça a Deus que abra os seus olhos (Sl 119.18).",
        "15 min — Leitura bíblica (siga um plano; comece pelos Evangelhos).",
        "5 min — Meditação no versículo do dia.",
        "5 min — Oração de gratidão, intercessão e súplica.",
    ], ordenada=True)

    h3(doc, "Ritmo semanal sugerido")
    lista(doc, [
        "1 dia para revisão da apostila da semana.",
        "1 dia para memorização do versículo-chave.",
        "1 dia para partilhar o aprendido com alguém.",
        "1 dia de jejum (parcial ou alimentar), conforme orientação espiritual.",
        "Frequência fiel ao culto da igreja local — a Escola não substitui a Igreja.",
    ])

    citacao(doc, "Estatuiu Esdras no seu coração estudar a lei do Senhor, e cumpri-la, e ensinar em Israel os seus estatutos e os seus juízos.", "Esdras 7.10")
    _quadro_destaque(doc,
        "Estudo, prática e ensino",
        "Esdras revela o caminho do verdadeiro mestre da Palavra: primeiro "
        "ESTUDAR, depois CUMPRIR (viver) e só então ENSINAR. Esta é a ordem "
        "Epignósis. Ensinar sem viver é hipocrisia. Viver sem estudar é "
        "superficialidade.")

    # ====== 11. FREQUÊNCIA E AVALIAÇÃO ======
    h1(doc, "Frequência, Avaliações e Certificação", numero=11)

    h3(doc, "Frequência")
    paragrafo(doc, "Para receber certificação, é necessário cumprir a frequência mínima definida pela Coordenação Acadêmica:")
    lista(doc, [
        "Cursos presenciais e híbridos: presença mínima de 75 % das aulas.",
        "Cursos on-line: cumprimento de 75 % das actividades propostas, dentro dos prazos.",
        "Faltas justificadas devem ser comunicadas à Secretaria com antecedência.",
    ])

    h3(doc, "Avaliações")
    paragrafo(doc, "A avaliação Epignósis é integral, nas 4 dimensões:")
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Dimensão", "Peso"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    for nome, peso in [
        ("Conhecer (provas, trabalhos, estudo bíblico)", "40 %"),
        ("Crer (adesão à Declaração de Fé, defesa da fé)", "20 %"),
        ("Viver (conduta, vida devocional, coerência)", "20 %"),
        ("Servir (participação, prática ministerial, frutos)", "20 %"),
    ]:
        row = tbl.add_row().cells
        row[0].text = nome; row[1].text = peso
        for c in row:
            for p in c.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    paragrafo(doc, "Escala institucional de notas:")
    lista(doc, [
        "9,0 – 10,0 → Excelente (com louvor).",
        "7,5 – 8,9  → Muito bom.",
        "6,0 – 7,4  → Satisfatório.",
        "5,0 – 5,9  → Suficiente.",
        "0,0 – 4,9  → Insuficiente (reprovado).",
    ])
    paragrafo(doc, "A média mínima institucional para aprovação é 6,0.", italic=True)

    h3(doc, "Certificação")
    paragrafo(doc, "A Escola emite certificados em todas as etapas: apostila, módulo, curso, escola, instituto, programa e Diploma de Formação Completa. Consulte os modelos no documento de Modelos de Certificados.")

    # ====== 12. PRÉ-REQUISITOS ======
    h1(doc, "Pré-Requisitos e Progressão", numero=12)
    paragrafo(doc,
        "Na Epignósis, ninguém pode “saltar etapas”. O nosso ensino é "
        "progressivo: um curso prepara para o próximo; uma etapa prepara "
        "para a outra. Esta é uma convicção espiritual, não apenas "
        "pedagógica.")
    paragrafo(doc, "Cinco cursos da base são pré-requisito universal para qualquer outro curso da Escola:")
    lista(doc, [
        "Salvação e Novo Nascimento",
        "Arrependimento e Fé",
        "Identidade em Cristo",
        "Santidade",
        "Vida de Oração",
    ], ordenada=True)
    _quadro_destaque(doc,
        "Princípio do crescimento",
        "“Pelo tempo já devíeis ser mestres, e tendes outra vez necessidade "
        "de que se vos torne a ensinar quais sejam os primeiros rudimentos "
        "das palavras de Deus.” (Hebreus 5.12). Não tenha pressa: o que se "
        "constrói depressa cai depressa.")

    paragrafo(doc, "Para detalhes completos, consulte o documento EBE-DOC-008 — Sistema de Pré-Requisitos.")

    # ====== 13. ÉTICA ======
    h1(doc, "Ética Acadêmica e Plágio", numero=13)
    paragrafo(doc,
        "Excelência acadêmica e integridade cristã caminham juntas. "
        "Esperamos que cada aluno(a) produza os seus trabalhos com "
        "honestidade, cite correctamente as suas fontes e evite qualquer "
        "forma de plágio.")
    h3(doc, "O que é plágio?")
    paragrafo(doc,
        "Plágio é apropriar-se de ideias, textos ou produções de outra "
        "pessoa sem atribuir o devido crédito. Equivale, biblicamente, a "
        "uma forma de roubo (Êxodo 20.15) e de mentira (Provérbios 12.22).")
    h3(doc, "Como evitar")
    lista(doc, [
        "Cite sempre as fontes que utilizar (autor, obra, ano, página).",
        "Use aspas para qualquer texto copiado literalmente.",
        "Reescreva com suas palavras o que aprender em outros autores.",
        "Quando usar a Internet, identifique o site e a data de acesso.",
    ])
    paragrafo(doc, "O plágio é considerado falta grave e poderá implicar reprovação, advertência ou outras medidas disciplinares.")

    # ====== 14. DISCIPLINA ======
    h1(doc, "Disciplina e Restauração", numero=14)
    paragrafo(doc,
        "Toda medida disciplinar na Epignósis tem propósito restaurador, "
        "nunca punitivo. Buscamos a correcção, a reconciliação e o "
        "crescimento do aluno.")
    paragrafo(doc, "Conforme a gravidade, podem ser aplicadas:")
    lista(doc, [
        "Advertência verbal — em conversa pessoal e pastoral.",
        "Advertência escrita — registada no histórico interno.",
        "Suspensão temporária — afastamento provisório das actividades.",
        "Desligamento institucional — em casos de gravidade extrema.",
    ], ordenada=True)
    paragrafo(doc, "Toda medida será sempre precedida de diálogo, contraditório e oração (Gálatas 6.1).")

    page_break(doc)

    # ====== 15. ACOMPANHAMENTO ======
    h1(doc, "Acompanhamento Pastoral e Mentoria", numero=15)
    paragrafo(doc,
        "Você não está sozinho(a) na sua formação. A Escola Bíblica "
        "Epignósis possui uma Coordenação Espiritual e Pastoral, e cada "
        "aluno(a) pode contar com:")
    lista(doc, [
        "Atendimento pastoral por agendamento, em situações de luto, crise, dúvida espiritual ou ministerial.",
        "Mentoria, conforme disponibilidade — um irmão(ã) mais maduro(a) que acompanha o seu desenvolvimento.",
        "Cuidado pastoral nos momentos disciplinares.",
        "Orientação vocacional sobre dons e chamados ministeriais.",
    ])
    _dica(doc, "Não tenha vergonha de pedir ajuda. Esconder a dificuldade só atrasa o crescimento.")

    # ====== 16. MODALIDADES ======
    h1(doc, "Modalidades de Estudo (Presencial · Híbrido · On-line)", numero=16)

    h3(doc, "Modalidade presencial")
    lista(doc, [
        "Presença física obrigatória nas aulas, conforme calendário.",
        "Participação directa nos cultos e momentos devocionais da Escola.",
        "Frequência mínima: 75 % das aulas presenciais.",
    ])
    h3(doc, "Modalidade híbrida")
    lista(doc, [
        "Combinação de aulas presenciais e on-line.",
        "Frequência aferida pela soma de presenças e cumprimento das tarefas on-line.",
        "Encontros presenciais obrigatórios em datas-chave.",
    ])
    h3(doc, "Modalidade on-line")
    lista(doc, [
        "Acesso aos materiais pela plataforma oficial da Escola.",
        "Acompanhamento das aulas gravadas ou ao vivo, conforme o curso.",
        "Cumprimento das actividades dentro dos prazos (frequência aferida pela actividade).",
        "Recomenda-se forte vínculo com igreja local presencial.",
    ])
    _quadro_destaque(doc,
        "A Escola não substitui a Igreja",
        "Independente da modalidade, esperamos que cada aluno(a) seja membro "
        "activo de uma igreja local. A formação Epignósis serve à Igreja, e "
        "nunca compete com ela.")

    # ====== 17. CONVIVÊNCIA ======
    h1(doc, "Convivência Saudável e Unidade", numero=17)
    paragrafo(doc,
        "A Epignósis recebe alunos de denominações diferentes, idades "
        "diferentes, formações diferentes, dons diferentes. Esta diversidade "
        "é riqueza, mas exige amor.")
    lista(doc, [
        "Respeite tradições denominacionais distintas em pontos secundários.",
        "Mantenha a unidade no essencial da fé (Declaração de Fé EBE-DOC-002).",
        "Evite discussões inflamadas sobre temas controversos não-essenciais.",
        "Acolha o aluno novo como você gostaria de ter sido acolhido(a).",
        "Trate professores com honra (1 Timóteo 5.17).",
    ])
    citacao(doc, "Em essência, unidade; em dúvidas, liberdade; em tudo, amor.", "Máxima cristã clássica")
    citacao(doc, "Eis quão bom e quão suave é que os irmãos vivam em união!", "Salmo 133.1")

    # ====== 18. DOCUMENTOS ======
    h1(doc, "Documentos Institucionais Que Regem a Sua Matrícula", numero=18)
    paragrafo(doc, "Como aluno(a), você está sujeito(a) aos seguintes documentos oficiais — todos podem ser consultados na Secretaria Acadêmica:")
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Código", "Documento"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    for cod, nome in [
        ("EBE-DOC-001", "Identidade Institucional"),
        ("EBE-DOC-002", "Declaração de Fé Institucional"),
        ("EBE-DOC-003", "Projecto Pedagógico Oficial"),
        ("EBE-DOC-004", "Regimento Acadêmico"),
        ("EBE-DOC-005", "Arquitectura Oficial"),
        ("EBE-DOC-006", "Mapa Oficial de Cursos"),
        ("EBE-DOC-007", "Duração Oficial dos Cursos"),
        ("EBE-DOC-008", "Sistema de Pré-Requisitos"),
    ]:
        row = tbl.add_row().cells
        row[0].text = cod; row[1].text = nome
        for c in row:
            for p in c.paragraphs:
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    # ====== 19. GLOSSÁRIO ======
    h1(doc, "Glossário Epignósis", numero=19)
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Termo", "Significado"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    glossario = [
        ("Apostila",  "Unidade mínima de estudo (10–15 pp., 1 conceito central, 1–3 h)."),
        ("Módulo",    "Conjunto de 3–5 apostilas, com um tema macro."),
        ("Curso",     "Conjunto de 3–6 módulos, com uma competência."),
        ("Escola",    "Conjunto de 2–4 cursos, com uma área de conhecimento."),
        ("Instituto", "Conjunto de 3–5 escolas, com um grande domínio teológico."),
        ("Trilha",    "Sequência recomendada de cursos para um propósito específico (teológica, ministerial, etc.)."),
        ("Mentor",    "Aluno(a) ou docente mais maduro que acompanha pessoalmente o desenvolvimento de outro(a)."),
        ("Epígnosis", "Conhecimento pleno, profundo e experimental de Deus."),
        ("Hermenêutica", "Princípios de interpretação fiel das Escrituras."),
        ("Discípulo", "Aprendiz comprometido com Cristo — aluno básico da Epignósis."),
    ]
    for t, d in glossario:
        row = tbl.add_row().cells
        row[0].text = t; row[1].text = d
        for c in row:
            for p in c.paragraphs:
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)
        for p in row[0].paragraphs:
            for r in p.runs: r.font.bold = True; r.font.color.rgb = COR_PRIMARIA

    # ====== 20. COMPROMISSO ======
    h1(doc, "Compromisso Final do(a) Aluno(a)", numero=20)
    paragrafo(doc,
        "Ao tomar conhecimento deste Manual, você é convidado(a) a renovar, "
        "diante de Deus, o seu compromisso com a sua formação. Sugerimos "
        "que faça esta oração:")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.5); p.paragraph_format.right_indent = Cm(1.0)
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(
        "“Senhor Deus, eu Te agradeço por me chamares ao conhecimento "
        "(ἐπίγνωσις) do Teu nome. Concede-me um coração ensinável, uma "
        "mente atenta, uma vida coerente e mãos prontas para servir. Que "
        "esta jornada na Escola Bíblica Epignósis seja um tempo de "
        "transformação profunda. Em nome de Jesus, amém.”")
    r.font.name = FONTE_TITULO; r.font.size = Pt(13)
    r.font.italic = True; r.font.color.rgb = COR_PRIMARIA

    citacao(doc, "Mas crescei na graça e conhecimento de nosso Senhor e Salvador, Jesus Cristo. A ele seja dada a glória, assim agora, como no dia da eternidade. Amém.", "2 Pedro 3.18")

    doc.add_paragraph()
    paragrafo(doc, "Termo de ciência:", bold=True)
    paragrafo(doc, "Declaro que recebi e li o presente Manual do Aluno e comprometo-me a cumpri-lo em comunhão com Deus e com a Escola Bíblica Epignósis.")

    doc.add_paragraph()
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c in tbl.rows[0].cells:
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("__________________________________")
        r.font.name = FONTE_CORPO; r.font.size = Pt(10)
    rot = [
        ("«[Nome do(a) aluno(a)]»", "Assinatura do(a) aluno(a)"),
        ("«[Local], «[__]» de «[mês]» de «[ano]»", "Data"),
    ]
    for i, (n, l) in enumerate(rot):
        c = tbl.rows[1].cells[i]
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(n); r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(10)
        r.font.color.rgb = COR_PRIMARIA
        p2 = c.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r2 = p2.add_run(l)
        r2.font.name = FONTE_CORPO; r2.font.size = Pt(9); r2.font.italic = True
        r2.font.color.rgb = COR_SECUNDARIA

    selo_final(doc)

    out = os.path.join(os.path.dirname(__file__), "EBE-MAN-ALU_Manual_do_Aluno.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
