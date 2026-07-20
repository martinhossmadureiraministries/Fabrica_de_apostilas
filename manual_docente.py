"""
MANUAL DO DOCENTE — Escola Bíblica Epignósis
Guia formativo, pedagógico e pastoral para o(a) professor(a) Epignósis.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def _quadro(doc, titulo, corpo, cor_fundo="E8F1EC"):
    tbl = doc.add_table(rows=1, cols=1)
    cell = tbl.rows[0].cells[0]
    _shade_cell(cell, cor_fundo)
    p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"✦ {titulo}")
    r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r.font.color.rgb = COR_PRIMARIA
    p2 = cell.add_paragraph(); p2.paragraph_format.space_after = Pt(0)
    r2 = p2.add_run(corpo); r2.font.name = FONTE_CORPO; r2.font.size = Pt(11)


def _pratica(doc, texto):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("✓  ")
    r.font.name = FONTE_TITULO; r.font.size = Pt(11)
    r.font.bold = True; r.font.color.rgb = COR_SECUNDARIA
    r2 = p.add_run(texto); r2.font.name = FONTE_CORPO; r2.font.size = Pt(11)


def _evitar(doc, texto):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("✗  ")
    r.font.name = FONTE_TITULO; r.font.size = Pt(11); r.font.bold = True
    r.font.color.rgb = RGBColor(0xB0, 0x30, 0x30)
    r2 = p.add_run(texto); r2.font.name = FONTE_CORPO; r2.font.size = Pt(11)


def gerar():
    doc = novo_documento("Manual do Docente", "EBE-MAN-DOC")

    add_capa(doc,
        supratitulo="Documento de Formação Docente N.º 1",
        titulo="Manual do Docente",
        subtitulo="Guia formativo, pedagógico e pastoral do(a) professor(a) Epignósis",
        codigo="EBE-MAN-DOC", ano="2026")
    add_marco_filosofico(doc)

    # ====== CARTA AO DOCENTE ======
    h1(doc, "Carta ao(à) Docente Epignósis")
    paragrafo(doc, "Estimado(a) docente,")
    paragrafo(doc,
        "É com profunda alegria que a Escola Bíblica Epignósis o(a) recebe "
        "como parte do seu corpo docente. Ensinar a Palavra de Deus é, "
        "antes de mais nada, um ministério: uma honra que vem do Senhor "
        "e uma responsabilidade que se exerce diante d’Ele.")
    paragrafo(doc,
        "Este Manual é, ao mesmo tempo, um instrumento prático e um pacto "
        "espiritual. Procura ajudá-lo(a) a ensinar com excelência acadêmica "
        "e fidelidade doutrinária, mas também a cuidar do seu próprio "
        "coração, da sua vida espiritual e do seu rebanho de alunos.")
    citacao(doc,
        "Meus irmãos, muitos de vós não sejam mestres, sabendo que "
        "receberemos maior juízo.",
        "Tiago 3.1")
    paragrafo(doc,
        "Esta advertência sóbria de Tiago não nos deve paralisar, mas "
        "manter-nos atentos: ensinar a Palavra exige preparo, oração, "
        "humildade e santidade. Que o Senhor nos guarde a todos.")
    paragrafo(doc, "Em comunhão,", italic=True)
    paragrafo(doc, "Direcção e Coordenação Pedagógica da Escola Bíblica Epignósis.", italic=True)

    # ====== SUMÁRIO ======
    h1(doc, "Sumário")
    lista(doc, [
        "1.  O ensino como ministério",
        "2.  Perfil do(a) docente Epignósis",
        "3.  Compromissos fundamentais",
        "4.  Subscrição da Declaração de Fé",
        "5.  Os Quatro Eixos pedagógicos da EBE",
        "6.  Preparação da aula — o método dos 7 passos",
        "7.  As 5 fases da aula Epignósis (cronograma)",
        "8.  Boas práticas pedagógicas",
        "9.  O que evitar em sala de aula",
        "10. Hermenêutica responsável — guardando a fidelidade ao texto",
        "11. Critérios de avaliação detalhados (Conhecer · Crer · Viver · Servir)",
        "12. Como dar feedback que edifica",
        "13. Conduzir momentos de oração e devoção em aula",
        "14. Cuidado pastoral com os alunos",
        "15. Disciplina restauradora",
        "16. Vida espiritual do(a) docente",
        "17. Plágio, originalidade e ética acadêmica do docente",
        "18. Modalidades de ensino (presencial · híbrido · on-line)",
        "19. Relação com a Coordenação e o Conselho Doutrinário",
        "20. Produção de materiais e revisão",
        "21. Documentos institucionais que regem o magistério",
        "22. Compromisso final do(a) docente",
    ])
    page_break(doc)

    # ====== 1. ENSINO COMO MINISTÉRIO ======
    h1(doc, "O Ensino Como Ministério", numero=1)
    paragrafo(doc,
        "Na Escola Bíblica Epignósis, ensinar não é apenas uma actividade "
        "profissional ou intelectual: é ministério. O dom de mestre é um "
        "dos cinco dons ministeriais entregues por Cristo à Sua Igreja "
        "(Efésios 4.11). É o Senhor quem chama, capacita e envia.")
    citacao(doc, "E ele mesmo deu uns para apóstolos, e outros para profetas, e outros para evangelistas, e outros para pastores e doutores.", "Efésios 4.11")
    paragrafo(doc, "Por isso, o(a) docente Epignósis entende-se a si mesmo(a) não como mero transmissor de conteúdo, mas como:")
    lista(doc, [
        "Servo(a) da Palavra (Lucas 1.2).",
        "Instrumento do Espírito Santo (1 Coríntios 2.13).",
        "Pastor(a) intelectual dos seus alunos (Hebreus 13.17).",
        "Modelo de vida cristã (1 Timóteo 4.12; Tito 2.7).",
    ])

    # ====== 2. PERFIL DOCENTE ======
    h1(doc, "Perfil do(a) Docente Epignósis", numero=2)
    paragrafo(doc, "O Regimento Acadêmico (Art. 11.º) estabelece os requisitos para o exercício do magistério na EBE:")
    lista(doc, [
        "Vocação clara, reconhecida pela Igreja local.",
        "Preparo bíblico-teológico compatível com a matéria que ensinará.",
        "Testemunho cristão público inquestionável.",
        "Maturidade espiritual e emocional.",
        "Adesão integral à Declaração de Fé Institucional.",
        "Capacidade pedagógica e didática.",
        "Espírito de serviço e humildade.",
        "Disposição para o estudo permanente e a actualização.",
    ], ordenada=True)
    _quadro(doc,
        "Convicção institucional",
        "Não basta saber muito — é preciso saber ensinar. E não basta "
        "saber ensinar — é preciso ser pessoa de oração. O(a) docente "
        "Epignósis integra conhecimento, didáctica e espiritualidade.")

    # ====== 3. COMPROMISSOS ======
    h1(doc, "Compromissos Fundamentais", numero=3)
    paragrafo(doc, "Ao aceitar uma cátedra na Escola Bíblica Epignósis, o(a) docente assume os seguintes compromissos:")
    lista(doc, [
        "Ensinar em estrita conformidade com as Escrituras e com a Declaração de Fé.",
        "Subscrever formalmente a Declaração de Fé Institucional (EBE-DOC-002).",
        "Preparar cuidadosa e oracionalmente cada aula.",
        "Manter postura ética, espiritual e cristã exemplar.",
        "Tratar com confidencialidade as informações dos alunos.",
        "Submeter os seus materiais à revisão pedagógica e doutrinária da Escola.",
        "Frequentar formações continuadas oferecidas pela Coordenação.",
        "Encaminhar à Coordenação Pastoral os casos que ultrapassem o âmbito acadêmico.",
        "Honrar a unidade institucional, evitando ensinos divergentes da Declaração de Fé.",
    ], ordenada=True)

    # ====== 4. SUBSCRIÇÃO DECLARAÇÃO ======
    h1(doc, "Subscrição da Declaração de Fé", numero=4)
    paragrafo(doc,
        "Antes de iniciar o magistério, o(a) docente Epignósis deve "
        "assinar formalmente o Termo de Adesão à Declaração de Fé "
        "Institucional (EBE-DOC-002), que contém os 16 artigos doutrinários "
        "que regem o ensino da Escola.")
    paragrafo(doc, "Em caso de evolução ou alteração de convicção pessoal sobre algum desses artigos, o(a) docente deve:")
    lista(doc, [
        "Comunicar prontamente à Coordenação Acadêmica e ao Conselho Doutrinário.",
        "Abster-se de ensinar aquela posição divergente em sala.",
        "Aguardar diálogo institucional para discernir o caminho a seguir.",
        "Em caso de divergência irreconciliável, considerar, com paz, o desligamento do quadro docente.",
    ], ordenada=True)
    _quadro(doc,
        "Princípio da integridade",
        "Não é desonra rever convicções. É desonra continuar ensinando "
        "publicamente o que já não se crê. A Epignósis valoriza a honestidade "
        "doutrinária acima da conveniência institucional.")

    page_break(doc)

    # ====== 5. EIXOS PEDAGÓGICOS ======
    h1(doc, "Os Quatro Eixos Pedagógicos da EBE", numero=5)
    paragrafo(doc,
        "Todo conteúdo ensinado na Epignósis articula quatro eixos "
        "indissociáveis. Cada plano de aula e cada apostila devem "
        "explicitar como tocam cada um dos eixos:")
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Eixo", "O que o eixo busca", "Como o docente o trabalha"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    eixos = [
        ("CONHECER", "Compreensão correcta das Escrituras e da doutrina.",
         "Exposição clara, definições precisas, contextualização bíblica."),
        ("CRER",     "Convicções bíblicas sólidas e duradouras.",
         "Articulação doutrinária; defesa da fé com mansidão (1 Pe 3.15)."),
        ("VIVER",    "Aplicação da Palavra à vida diária.",
         "Estudos de caso, aplicações concretas, testemunho do próprio docente."),
        ("SERVIR",   "Dons e talentos colocados a serviço do Reino.",
         "Tarefas práticas, ligação com a igreja local, projectos ministeriais."),
    ]
    for nome, o_que, como in eixos:
        row = tbl.add_row().cells
        row[0].text = nome; row[1].text = o_que; row[2].text = como
        for c in row:
            for p in c.paragraphs:
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    _quadro(doc,
        "Cuidado pedagógico",
        "Evite aulas centradas apenas em um eixo. Aulas só de “Conhecer” "
        "produzem cristãos arrogantes. Só de “Crer” geram dogmáticos. Só "
        "de “Viver” formam moralistas. Só de “Servir” criam activistas. "
        "A Epignósis quer formar discípulos integrais.")

    # ====== 6. PREPARAÇÃO DA AULA ======
    h1(doc, "Preparação da Aula — Método dos 7 Passos", numero=6)
    paragrafo(doc, "Para cada aula, recomenda-se o seguinte processo de preparação:")
    lista(doc, [
        "ORE — peça ao Espírito Santo discernimento e poder (João 14.26).",
        "LEIA o texto-base e o contexto bíblico imediato com calma.",
        "ESTUDE a apostila e o material de referência indicado pelo curso.",
        "PESQUISE pelo menos duas fontes complementares confiáveis.",
        "PLANEIE a aula em formulário oficial (EBE-FRM-002), distribuindo o tempo nas 5 fases.",
        "ANTECIPE perguntas, dúvidas e equívocos comuns dos alunos.",
        "REVISE com oração: “Senhor, o que falta? O que sobra? O que devo cortar?”",
    ], ordenada=True)
    _quadro(doc,
        "Regra de Spurgeon",
        "“Uma aula sem oração é uma aula sem unção.” Nenhum brilhantismo "
        "intelectual substitui o tempo gasto a sós com Deus na preparação.")

    # ====== 7. FASES DA AULA ======
    h1(doc, "As 5 Fases da Aula Epignósis", numero=7)
    paragrafo(doc, "Cada aula deve, sempre que possível, percorrer cinco fases:")
    tbl = doc.add_table(rows=1, cols=4)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Fase", "Tempo sugerido", "Objectivo", "Recursos"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    fases = [
        ("1. Acolhimento e Oração",     "5–10 min",
         "Criar ambiente de comunhão; recapitular a aula anterior.",
         "Bíblia, lista de presença."),
        ("2. Apresentação do Tema",     "10–15 min",
         "Introduzir o conceito central; apresentar versículo-chave.",
         "Apostila, slides, quadro."),
        ("3. Desenvolvimento Doutrinário", "25–40 min",
         "Exposição articulada, definições, fundamentos bíblicos, esclarecimento de dúvidas.",
         "Apostila, Bíblia (ARC), recursos visuais."),
        ("4. Aplicação e Diálogo",      "15–20 min",
         "Discussão, exemplos práticos, partilha de testemunhos, oração de aplicação.",
         "Perguntas norteadoras, exercícios."),
        ("5. Síntese e Envio",          "5–10 min",
         "Recapitulação; oração final; tarefas; indicação da próxima aula.",
         "Folheto de tarefas, apostila."),
    ]
    for fase in fases:
        row = tbl.add_row().cells
        for i, v in enumerate(fase):
            row[i].text = v
            for p in row[i].paragraphs:
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    page_break(doc)

    # ====== 8. BOAS PRÁTICAS ======
    h1(doc, "Boas Práticas Pedagógicas", numero=8)
    _pratica(doc, "Comece e termine sempre em oração.")
    _pratica(doc, "Mantenha a Bíblia aberta na frente, fisicamente visível.")
    _pratica(doc, "Pronuncie claramente os nomes dos livros, lugares e personagens bíblicos.")
    _pratica(doc, "Use ilustrações simples, ligadas ao quotidiano dos alunos.")
    _pratica(doc, "Repita os pontos centrais ao longo da aula (a repetição é mãe da aprendizagem).")
    _pratica(doc, "Faça perguntas frequentes para envolver toda a turma.")
    _pratica(doc, "Trate cada aluno pelo nome.")
    _pratica(doc, "Reconheça publicamente as boas contribuições dos alunos.")
    _pratica(doc, "Quando não souber uma resposta, diga-o com humildade: “Vou estudar e respondemos na próxima aula.”")
    _pratica(doc, "Encerre cada aula com um “pedido de fixação” claro (um versículo, uma frase, uma prática).")
    _pratica(doc, "Cumpra rigorosamente o horário — começar e terminar a tempo é testemunho.")
    _pratica(doc, "Confie no Espírito Santo, não no seu próprio brilhantismo.")

    # ====== 9. O QUE EVITAR ======
    h1(doc, "O Que Evitar em Sala de Aula", numero=9)
    _evitar(doc, "Improvisar — chegar sem plano de aula.")
    _evitar(doc, "Pregar polémicas denominacionais não-essenciais.")
    _evitar(doc, "Ridicularizar perguntas, dúvidas ou tradições dos alunos.")
    _evitar(doc, "Citar versículos fora de contexto para reforçar ideias preferidas.")
    _evitar(doc, "Falar mal de outros docentes, igrejas ou ministérios.")
    _evitar(doc, "Tornar a aula um monólogo — comunicação só funciona em diálogo.")
    _evitar(doc, "Usar a sala para “desabafos” pessoais ou conflitos familiares.")
    _evitar(doc, "Permitir-se proximidade emocional ou física inadequada com alunos do sexo oposto.")
    _evitar(doc, "Atrasar-se ou prolongar a aula sem necessidade.")
    _evitar(doc, "Fazer da turma um “fã-clube” do docente: o ensino aponta para Cristo, não para si.")
    citacao(doc, "Porque não nos pregamos a nós mesmos, mas a Cristo Jesus, o Senhor; e nós mesmos somos vossos servos por amor de Jesus.", "2 Coríntios 4.5")

    # ====== 10. HERMENÊUTICA RESPONSÁVEL ======
    h1(doc, "Hermenêutica Responsável — Guardando a Fidelidade ao Texto", numero=10)
    paragrafo(doc,
        "O(a) docente Epignósis é, por vocação, um intérprete fiel da Palavra. "
        "Algumas convicções hermenêuticas devem orientar todo o seu ensino:")
    lista(doc, [
        "Toda interpretação respeita o contexto imediato, histórico, cultural e gramatical do texto.",
        "Texto sem contexto torna-se pretexto.",
        "A Escritura interpreta a Escritura (analogia da fé).",
        "Versículos isolados não fundam doutrinas — temas bíblicos sim.",
        "Há um sentido original do texto, dado pelo autor humano sob inspiração divina; aplicações posteriores não podem contradizê-lo.",
        "Mistérios revelados pertencem a Deus (Dt 29.29); o(a) mestre fiel não especula onde a Bíblia se cala.",
    ])
    citacao(doc, "Procura apresentar-te a Deus aprovado, como obreiro que não tem de que se envergonhar, que maneja bem a palavra da verdade.", "2 Timóteo 2.15")

    # ====== 11. AVALIAÇÃO DETALHADA ======
    h1(doc, "Critérios de Avaliação Detalhados", numero=11)
    paragrafo(doc,
        "A avaliação Epignósis é integral nas 4 dimensões. Os pesos "
        "institucionais são fixos; os instrumentos podem variar conforme "
        "o conteúdo e a modalidade. Cada nota é dada na escala 0–10.")

    h3(doc, "Distribuição institucional dos pesos")
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Dimensão", "Peso"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    for nome, peso in [("Conhecer", "40 %"), ("Crer", "20 %"), ("Viver", "20 %"), ("Servir", "20 %")]:
        row = tbl.add_row().cells
        row[0].text = nome; row[1].text = peso
        for c in row:
            for p in c.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    h3(doc, "Dimensão Conhecer — o que avaliar")
    lista(doc, [
        "Compreensão dos conceitos centrais.",
        "Capacidade de articular o conteúdo com suas próprias palavras.",
        "Domínio das referências bíblicas citadas.",
        "Capacidade de interpretar correctamente passagens estudadas.",
        "Conhecimento da terminologia técnica do curso.",
    ])
    h3(doc, "Dimensão Crer — o que avaliar")
    lista(doc, [
        "Articulação bíblica das próprias convicções.",
        "Coerência com a Declaração de Fé Institucional.",
        "Capacidade de defender a fé com mansidão.",
        "Discernimento espiritual e doutrinário.",
    ])
    h3(doc, "Dimensão Viver — o que avaliar")
    lista(doc, [
        "Vida devocional consistente (testemunho do próprio aluno).",
        "Conduta cristã em sala e fora dela.",
        "Pontualidade, assiduidade, responsabilidade.",
        "Relação respeitosa com colegas e docentes.",
        "Coerência entre o que estuda e o que pratica (Tg 1.22).",
    ])
    h3(doc, "Dimensão Servir — o que avaliar")
    lista(doc, [
        "Participação activa nas actividades práticas.",
        "Disposição para trabalho em equipa.",
        "Iniciativa em projectos ministeriais ou missionários.",
        "Exercício equilibrado de dons.",
        "Frutos observáveis na igreja local.",
    ])
    paragrafo(doc,
        "Use o formulário oficial EBE-FRM-004 (Ficha de Avaliação) para "
        "registar formalmente o aproveitamento de cada aluno(a). Para cada "
        "instrumento aplicado, atribua peso (%) e nota; a média final será "
        "calculada pela ponderação.")
    paragrafo(doc, "Média mínima institucional para aprovação: 6,0 (seis vírgula zero).", italic=True)

    page_break(doc)

    # ====== 12. FEEDBACK ======
    h1(doc, "Como Dar Feedback Que Edifica", numero=12)
    paragrafo(doc,
        "Avaliar não é apenas medir: é também formar. Todo feedback "
        "Epignósis deve ser honesto, oportuno, específico e edificante.")
    h3(doc, "Princípios bíblicos do feedback")
    lista(doc, [
        "Verdade em amor (Efésios 4.15).",
        "Mansidão na correcção (Gálatas 6.1).",
        "Edificação como propósito (Efésios 4.29).",
        "Discrição com matérias delicadas (Mateus 18.15).",
    ])
    h3(doc, "Método sugerido — “Afirmar · Apontar · Apoiar”")
    lista(doc, [
        "AFIRMAR — comece por reconhecer um ponto forte real (não fingido).",
        "APONTAR — descreva o ponto a melhorar com clareza e exemplos concretos.",
        "APOIAR — termine com encorajamento e indicação prática de como avançar.",
    ], ordenada=True)
    _quadro(doc,
        "Cuidado pastoral",
        "Lembre-se: alunos não são apenas “mentes a treinar”. São filhos "
        "amados de Deus. O modo como você corrige pode aproximá-los ou "
        "afastá-los da formação. Corrija como Cristo o corrigiria.")

    # ====== 13. DEVOÇÃO NA AULA ======
    h1(doc, "Conduzir Momentos de Oração e Devoção em Aula", numero=13)
    _pratica(doc, "Abra cada aula com oração breve, focada (não dispersiva).")
    _pratica(doc, "Inclua intercessão por necessidades reais dos alunos sempre que possível.")
    _pratica(doc, "Termine cada aula com um “envio” espiritual claro (uma promessa, uma exortação, uma bênção).")
    _pratica(doc, "Reserve um momento de adoração silenciosa quando o conteúdo tocar profundamente a turma.")
    _pratica(doc, "Esteja pronto(a) para pausar a matéria se houver clamor genuíno por oração ou ministração.")
    _evitar(doc, "Oração mecânica, repetitiva, sem alma.")
    _evitar(doc, "Sensacionalismo emocional ou “fabricação” de manifestações espirituais.")
    _evitar(doc, "Confundir o lugar do docente com o lugar do pastor da igreja local.")

    # ====== 14. CUIDADO PASTORAL ======
    h1(doc, "Cuidado Pastoral Com os Alunos", numero=14)
    paragrafo(doc,
        "O(a) docente Epignósis é também pastor(a) intelectual da sua "
        "turma. Aprenda a “ler” os seus alunos:")
    lista(doc, [
        "Quem está ausente? Faltou — ou está em crise?",
        "Quem mudou de comportamento de uma aula para outra?",
        "Quem tem feito perguntas insistentes sobre o mesmo tema (pode haver luta interna)?",
        "Quem está visivelmente cansado ou desanimado?",
    ])
    paragrafo(doc, "Em todos esses casos, procure conversar discretamente após a aula, com escuta empática. Quando exceder o que cabe ao docente, encaminhe à Coordenação Pastoral.")
    _quadro(doc,
        "Limite saudável",
        "O(a) docente não substitui o pastor da igreja local nem o psicólogo. "
        "Saiba escutar, orar e encaminhar. Querer “resolver tudo” pode "
        "prejudicar o aluno e esgotar o docente.")

    # ====== 15. DISCIPLINA ======
    h1(doc, "Disciplina Restauradora", numero=15)
    paragrafo(doc, "Quando for necessário aplicar correcção a algum aluno:")
    lista(doc, [
        "Converse primeiro em privado (Mateus 18.15).",
        "Registe por escrito apenas se o diálogo privado não resolver.",
        "Envolva a Coordenação Acadêmica antes de qualquer medida formal.",
        "Mantenha sempre o objectivo restaurador, não punitivo.",
        "Garanta ao aluno direito de contraditório.",
        "Após a correcção, ore com o aluno se ele(a) permitir.",
    ], ordenada=True)
    citacao(doc, "Irmãos, se algum homem chegar a ser surpreendido nalguma ofensa, vós, que sois espirituais, encaminhai o tal com espírito de mansidão.", "Gálatas 6.1")

    page_break(doc)

    # ====== 16. VIDA ESPIRITUAL DO DOCENTE ======
    h1(doc, "Vida Espiritual do(a) Docente", numero=16)
    paragrafo(doc,
        "Você não pode dar o que não tem. Um(a) docente sem comunhão "
        "diária com Deus secará, mais cedo ou mais tarde, por dentro — "
        "mesmo sendo brilhante por fora.")
    h3(doc, "Ritmos espirituais recomendados")
    lista(doc, [
        "Oração diária pessoal — antes de qualquer estudo.",
        "Leitura bíblica diária em plano sistemático (não apenas para preparar aula).",
        "Participação activa em uma igreja local — submisso(a) à liderança pastoral.",
        "Dia de sabbath (descanso integral) por semana.",
        "Retiro espiritual periódico (mínimo uma vez por ano).",
        "Mentoria espiritual — todo mestre precisa também de mestre.",
        "Acompanhamento pastoral em situações de luto, desânimo, conflito.",
    ])
    citacao(doc, "Tem cuidado de ti mesmo e da doutrina. Persevera nestes deveres; porque, fazendo isto, te salvarás, tanto a ti mesmo como aos que te ouvem.", "1 Timóteo 4.16")

    # ====== 17. ÉTICA DO DOCENTE ======
    h1(doc, "Plágio, Originalidade e Ética Acadêmica do Docente", numero=17)
    paragrafo(doc,
        "O(a) docente Epignósis é, antes do aluno, um exemplo de "
        "honestidade intelectual:")
    lista(doc, [
        "Cite sempre as suas fontes em apostilas, slides e materiais.",
        "Reconheça publicamente quando uma ideia veio de outro autor.",
        "Não use materiais de terceiros sem autorização ou crédito.",
        "Resista à tentação de copiar pregações inteiras da internet — escreva as suas próprias.",
        "Mantenha a integridade nas avaliações: corrija com critério, não por simpatia.",
    ])
    citacao(doc, "Não faltai ninguém com o que lhe é devido… nada devais a ninguém, senão o amor com que vos ameis uns aos outros.", "Romanos 13.7-8")

    # ====== 18. MODALIDADES ======
    h1(doc, "Modalidades de Ensino", numero=18)

    h3(doc, "Aula presencial")
    _pratica(doc, "Esteja na sala 10 minutos antes do início.")
    _pratica(doc, "Verifique os recursos (projector, quadro, materiais) antecipadamente.")
    _pratica(doc, "Faça contacto visual com toda a turma.")
    _pratica(doc, "Movimente-se moderadamente; evite ficar “preso” a um único ponto.")

    h3(doc, "Aula híbrida")
    _pratica(doc, "Garanta que os alunos on-line vejam e ouçam bem.")
    _pratica(doc, "Dirija perguntas alternadamente a presenciais e remotos.")
    _pratica(doc, "Use ferramentas digitais (formulários, quizzes) para envolver os dois grupos.")

    h3(doc, "Aula on-line")
    _pratica(doc, "Teste câmara, microfone e ligação antes da aula.")
    _pratica(doc, "Reduza distrações no fundo do enquadramento.")
    _pratica(doc, "Faça pausas a cada 20–25 min para evitar saturação digital.")
    _pratica(doc, "Use legendas, slides e materiais escritos em paralelo.")
    _pratica(doc, "Mantenha contacto pastoral por mensagem privada com alunos que se ausentam.")

    # ====== 19. COORDENAÇÃO ======
    h1(doc, "Relação com a Coordenação e o Conselho Doutrinário", numero=19)
    paragrafo(doc, "O(a) docente Epignósis trabalha sempre em comunhão institucional:")
    lista(doc, [
        "Coordenação Acadêmica — apoio pedagógico, calendário, turmas, avaliações.",
        "Coordenação Pedagógica — metodologia, materiais, formação contínua.",
        "Coordenação Espiritual e Pastoral — cuidado pastoral dos alunos.",
        "Conselho Doutrinário — guarda da sã doutrina e revisão de conteúdos.",
        "Secretaria Acadêmica — registos, frequência, certificações.",
    ])
    paragrafo(doc, "Submeta o seu Plano de Aula (EBE-FRM-002) à Coordenação Pedagógica antes de cada novo curso. Submeta apostilas e materiais autorais ao Conselho Doutrinário.")

    # ====== 20. PRODUÇÃO ======
    h1(doc, "Produção de Materiais e Revisão", numero=20)
    paragrafo(doc, "Ao produzir apostilas, slides, exercícios ou livros para a Epignósis:")
    lista(doc, [
        "Siga o Modelo Oficial de Apostila (EBE-MODELO_APOSTILA).",
        "Inclua sempre o Marco Filosófico Institucional na abertura.",
        "Use a Almeida Revista e Corrigida (ARC) como versão de referência.",
        "Cite fontes em formato consistente (autor, título, editora, ano, página).",
        "Envie em formato editável à Coordenação Pedagógica para revisão.",
        "Aguarde a aprovação do Conselho Doutrinário antes da publicação.",
        "Aceite com humildade as sugestões de revisão.",
    ], ordenada=True)
    _quadro(doc,
        "Princípio editorial",
        "O nome de cada docente aparecerá nos materiais que produzir, mas o "
        "selo institucional Epignósis exige unidade de identidade visual, "
        "padronização editorial e revisão doutrinária — não há excepções.")

    # ====== 21. DOCUMENTOS ======
    h1(doc, "Documentos Institucionais Que Regem o Magistério", numero=21)
    paragrafo(doc, "O(a) docente Epignósis deve conhecer e operar segundo:")
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Código", "Documento"]):
        hdr[i].text = ""
        _shade_cell(hdr[i], HEX_PRIMARIA)
        p = hdr[i].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        r.font.name = FONTE_TITULO; r.font.size = Pt(10)
    docs = [
        ("EBE-DOC-001", "Identidade Institucional"),
        ("EBE-DOC-002", "Declaração de Fé Institucional (subscrição obrigatória)"),
        ("EBE-DOC-003", "Projecto Pedagógico Oficial"),
        ("EBE-DOC-004", "Regimento Acadêmico"),
        ("EBE-DOC-005", "Arquitectura Oficial"),
        ("EBE-DOC-006", "Mapa Oficial de Cursos"),
        ("EBE-DOC-007", "Duração Oficial dos Cursos"),
        ("EBE-DOC-008", "Sistema de Pré-Requisitos"),
        ("EBE-FRM-002", "Plano de Aula"),
        ("EBE-FRM-004", "Ficha de Avaliação"),
        ("EBE-MODELO_APOSTILA", "Modelo Oficial de Apostila"),
        ("EBE-MAN-ALU", "Manual do Aluno"),
    ]
    for cod, n in docs:
        row = tbl.add_row().cells
        row[0].text = cod; row[1].text = n
        for c in row:
            for p in c.paragraphs:
                for r in p.runs: r.font.name = FONTE_CORPO; r.font.size = Pt(10)

    # ====== 22. COMPROMISSO ======
    h1(doc, "Compromisso Final do(a) Docente", numero=22)
    paragrafo(doc, "Sugerimos que o(a) docente faça, na sua posse ao quadro Epignósis, a seguinte oração-compromisso:")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.5); p.paragraph_format.right_indent = Cm(1.0)
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(
        "“Senhor Deus, eu Te agradeço pelo privilégio de ensinar a Tua "
        "Palavra. Conheço a sobriedade desta vocação (Tiago 3.1) e quero "
        "exercê-la em fidelidade. Guarda os meus lábios da mentira, o meu "
        "coração da soberba e a minha vida da hipocrisia. Que cada aluno "
        "que cruzar o meu caminho encontre, em mim, não um homem nem uma "
        "mulher de palavras, mas alguém que vive o que ensina. Em nome "
        "de Jesus, amém.”")
    r.font.name = FONTE_TITULO; r.font.size = Pt(13)
    r.font.italic = True; r.font.color.rgb = COR_PRIMARIA

    citacao(doc,
        "E o que de mim, entre muitas testemunhas, ouviste, confia-o a "
        "homens fiéis, que sejam idóneos para também ensinarem os outros.",
        "2 Timóteo 2.2")

    doc.add_paragraph()
    paragrafo(doc, "Termo de ciência e adesão:", bold=True)
    paragrafo(doc,
        "Declaro que recebi e li o presente Manual do Docente, que conheço "
        "e adiro à Declaração de Fé Institucional (EBE-DOC-002), e que me "
        "comprometo, perante Deus e perante a Escola Bíblica Epignósis, a "
        "exercer o magistério em fidelidade, integridade e amor.")

    doc.add_paragraph()
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c in tbl.rows[0].cells:
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("__________________________________")
        r.font.name = FONTE_CORPO; r.font.size = Pt(10)
    rot = [
        ("«[Nome do(a) docente]»", "Assinatura do(a) docente"),
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

    doc.add_paragraph()
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c in tbl.rows[0].cells:
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("__________________________________")
        r.font.name = FONTE_CORPO; r.font.size = Pt(10)
    rot2 = [
        ("«[Coordenação Acadêmica]»", "Aprovação institucional"),
        ("«[Conselho Doutrinário]»",  "Verificação doutrinária"),
    ]
    for i, (n, l) in enumerate(rot2):
        c = tbl.rows[1].cells[i]
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(n); r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(10)
        r.font.color.rgb = COR_PRIMARIA
        p2 = c.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r2 = p2.add_run(l)
        r2.font.name = FONTE_CORPO; r2.font.size = Pt(9); r2.font.italic = True
        r2.font.color.rgb = COR_SECUNDARIA

    selo_final(doc)

    out = os.path.join(os.path.dirname(__file__), "EBE-MAN-DOC_Manual_do_Docente.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
