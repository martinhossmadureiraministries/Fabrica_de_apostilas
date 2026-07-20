"""DOC 2 — Declaração de Fé Institucional"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Declaração de Fé", "EBE-DOC-002")

    add_capa(doc,
        supratitulo="Documento Institucional N.º 2",
        titulo="Declaração de Fé\nInstitucional",
        subtitulo="Os Fundamentos Doutrinários da Escola Bíblica Epignósis",
        codigo="EBE-DOC-002", ano="2026")
    add_marco_filosofico(doc)

    # Sumário
    h1(doc, "Sumário")
    lista(doc, [
        "Preâmbulo",
        "Art. 1.º — As Sagradas Escrituras",
        "Art. 2.º — O Deus Triúno",
        "Art. 3.º — Jesus Cristo",
        "Art. 4.º — O Espírito Santo",
        "Art. 5.º — A Criação",
        "Art. 6.º — O Ser Humano e o Pecado",
        "Art. 7.º — A Salvação",
        "Art. 8.º — O Baptismo nas Águas e a Ceia do Senhor",
        "Art. 9.º — O Baptismo no Espírito Santo",
        "Art. 10.º — A Igreja",
        "Art. 11.º — Os Ministérios e os Dons",
        "Art. 12.º — Santidade e Vida Cristã",
        "Art. 13.º — Evangelização e Missões",
        "Art. 14.º — Cura Divina e Acção Sobrenatural de Deus",
        "Art. 15.º — A Segunda Vinda de Cristo",
        "Art. 16.º — A Esperança Eterna",
        "Compromisso Doutrinário",
        "Lema Institucional",
    ])
    page_break(doc)

    # Preâmbulo
    h1(doc, "Preâmbulo")
    paragrafo(doc,
        "A Escola Bíblica Epignósis fundamenta todo o seu ensino na autoridade "
        "das Sagradas Escrituras e reconhece a Bíblia como a única regra "
        "infalível de fé e prática. Cremos que o verdadeiro conhecimento "
        "de Deus — em grego ἐπίγνωσις (epígnōsis) — é fruto da revelação divina, "
        "da iluminação do Espírito Santo e da obediência à Palavra, produzindo "
        "transformação de vida e conformidade ao carácter de Jesus Cristo.")
    paragrafo(doc,
        "Esta Declaração de Fé orienta o currículo, o ensino, a produção de "
        "materiais didácticos, a formação de professores e a vida académica "
        "da Escola Bíblica Epignósis. Todo docente, discente e colaborador "
        "compromete-se a respeitá-la, vivê-la e ensiná-la com fidelidade.")
    paragrafo(doc,
        "A presente Declaração possui natureza confessional e não exaustiva: "
        "afirma o essencial da fé cristã histórica, deixando espaço para o "
        "estudo aprofundado das demais doutrinas no âmbito do ensino regular.")
    citacao(doc,
        "Amados, procurando eu escrever-vos com toda a diligência acerca da "
        "salvação comum, tive por necessidade escrever-vos, e exortar-vos a "
        "batalhar pela fé que uma vez foi dada aos santos.",
        "Judas 3")

    capitulo(doc, "ÚNICO", "Dos Artigos de Fé")

    # === Art. 1
    h2(doc, "As Sagradas Escrituras", numero="1.º")
    paragrafo(doc,
        "Cremos que a Bíblia Sagrada, composta pelo Antigo e pelo Novo "
        "Testamentos (66 livros canónicos), é a Palavra de Deus inspirada "
        "pelo Espírito Santo, plenamente verdadeira, suficiente e autoritativa "
        "para ensinar, redarguir, corrigir, instruir e conduzir o cristão em "
        "toda a sua vida e ministério.")
    paragrafo(doc,
        "Reconhecemos a Bíblia como a única regra infalível de fé e prática, "
        "submetendo a ela todo o ensino, toda a tradição e toda a experiência.")
    citacao(doc, "Toda a Escritura é divinamente inspirada, e proveitosa para ensinar, para redarguir, para corrigir, para instruir em justiça.", "2 Timóteo 3.16")
    citacao(doc, "Nunca jamais a profecia foi produzida por vontade de homem algum, mas os homens santos de Deus falaram inspirados pelo Espírito Santo.", "2 Pedro 1.21")
    citacao(doc, "Lâmpada para os meus pés é tua palavra, e luz para o meu caminho.", "Salmo 119.105")

    # === Art. 2
    h2(doc, "O Deus Triúno", numero="2.º")
    paragrafo(doc,
        "Cremos em um único Deus eterno, soberano, omnisciente, omnipotente, "
        "omnipresente, santo, justo, amoroso e digno de toda a adoração, "
        "que existe eternamente em três Pessoas distintas e inseparáveis: o "
        "Pai, o Filho e o Espírito Santo, iguais em essência, glória e poder.")
    citacao(doc, "Ouve, Israel, o Senhor nosso Deus é o único Senhor.", "Deuteronómio 6.4")
    citacao(doc, "Ide, portanto, fazei discípulos de todas as nações, baptizando-os em nome do Pai, e do Filho, e do Espírito Santo.", "Mateus 28.19")
    citacao(doc, "A graça do Senhor Jesus Cristo, e o amor de Deus, e a comunhão do Espírito Santo seja com vós todos.", "2 Coríntios 13.13")

    # === Art. 3
    h2(doc, "Jesus Cristo", numero="3.º")
    paragrafo(doc,
        "Cremos que Jesus Cristo é o eterno Filho de Deus, verdadeiro Deus e "
        "verdadeiro homem, concebido pelo Espírito Santo, nascido da virgem "
        "Maria, sem pecado em sua natureza e em sua conduta. Viveu uma vida "
        "perfeita, morreu voluntariamente na cruz como substituto dos "
        "pecadores, ressuscitou corporalmente ao terceiro dia, ascendeu aos "
        "céus, está assentado à direita do Pai intercedendo pelos santos, "
        "e retornará em glória para consumar todas as coisas.")
    citacao(doc, "E o Verbo se fez carne, e habitou entre nós, e vimos a sua glória, como a glória do Unigénito do Pai, cheio de graça e de verdade.", "João 1.14")
    citacao(doc, "Cristo morreu pelos nossos pecados, segundo as Escrituras… ressuscitou ao terceiro dia, segundo as Escrituras.", "1 Coríntios 15.3-4")
    citacao(doc, "Para que ao nome de Jesus se dobre todo o joelho dos que estão nos céus, e na terra, e debaixo da terra.", "Filipenses 2.10")

    # === Art. 4
    h2(doc, "O Espírito Santo", numero="4.º")
    paragrafo(doc,
        "Cremos que o Espírito Santo é Deus, terceira Pessoa da Trindade, "
        "consubstancial e coeterno com o Pai e o Filho. Actuou na criação "
        "(Génesis 1.2), na inspiração das Escrituras (2 Pedro 1.21), e actua "
        "hoje na regeneração, santificação, consolação, direcção e capacitação "
        "do povo de Deus.")
    paragrafo(doc,
        "Cremos na actualidade dos dons espirituais concedidos para a edificação "
        "da Igreja e para o cumprimento da missão de Cristo, exercidos em "
        "amor, ordem e submissão às Escrituras.")
    citacao(doc, "Mas recebereis a virtude do Espírito Santo, que há-de vir sobre vós; e ser-me-eis testemunhas.", "Actos 1.8")
    citacao(doc, "A um pela mesma fé, por meio do mesmo Espírito… mas um só e o mesmo Espírito opera todas estas coisas, repartindo particularmente a cada um como quer.", "1 Coríntios 12.9, 11")

    # === Art. 5
    h2(doc, "A Criação", numero="5.º")
    paragrafo(doc,
        "Cremos que Deus criou todas as coisas — visíveis e invisíveis — por "
        "Sua Palavra, do nada (ex nihilo), revelando Sua sabedoria, poder e "
        "bondade. Toda a criação pertence ao Senhor e existe para Sua glória, "
        "estando o ser humano constituído mordomo responsável por ela.")
    citacao(doc, "No princípio criou Deus os céus e a terra.", "Génesis 1.1")
    citacao(doc, "Pois nele foram criadas todas as coisas que há nos céus e na terra, visíveis e invisíveis… tudo foi criado por ele e para ele.", "Colossenses 1.16")

    # === Art. 6
    h2(doc, "O Ser Humano e o Pecado", numero="6.º")
    paragrafo(doc,
        "Cremos que o ser humano — homem e mulher — foi criado por Deus à Sua "
        "imagem e semelhança, com dignidade, propósito e vocação. Pela "
        "desobediência voluntária dos nossos primeiros pais, o pecado entrou "
        "no mundo, alcançando toda a humanidade e separando-a de Deus. "
        "Todos nasceram em pecado, pecam por natureza e por prática, e estão "
        "destituídos da glória de Deus, necessitando da graça e da redenção "
        "oferecidas em Cristo.")
    citacao(doc, "E criou Deus o homem à sua imagem; à imagem de Deus o criou; macho e fêmea os criou.", "Génesis 1.27")
    citacao(doc, "Todos pecaram e destituídos estão da glória de Deus.", "Romanos 3.23")

    # === Art. 7
    h2(doc, "A Salvação", numero="7.º")
    paragrafo(doc,
        "Cremos que a salvação é oferecida exclusivamente pela graça de Deus, "
        "mediante a fé em Jesus Cristo, e não por obras humanas. O "
        "arrependimento, a fé, a regeneração, a justificação, a adopção e a "
        "santificação são obras da graça divina na vida daquele que crê. A "
        "nova vida em Cristo produz transformação visível, frutos do Espírito "
        "e perseverança no caminho do Senhor.")
    citacao(doc, "Porque pela graça sois salvos, por meio da fé; e isto não vem de vós; é dom de Deus. Não vem das obras, para que ninguém se glorie.", "Efésios 2.8-9")
    citacao(doc, "Se alguém está em Cristo, nova criatura é: as coisas velhas já passaram; eis que tudo se fez novo.", "2 Coríntios 5.17")

    # === Art. 8
    h2(doc, "O Baptismo nas Águas e a Ceia do Senhor", numero="8.º")
    paragrafo(doc,
        "Cremos que o baptismo nas águas e a Ceia do Senhor foram instituídos "
        "pelo próprio Jesus Cristo como ordenanças da Igreja:")
    lista(doc, [
        "O baptismo nas águas, por imersão, testemunha publicamente a fé do crente, "
        "simbolizando a sua morte para o pecado e a sua ressurreição para uma nova vida em Cristo (Romanos 6.3-4).",
        "A Ceia do Senhor proclama a morte do Senhor até que Ele venha, fortalecendo "
        "a comunhão dos santos e a memória da obra redentora de Cristo (1 Coríntios 11.23-26).",
    ])
    citacao(doc, "Arrependei-vos, e cada um de vós seja baptizado em nome de Jesus Cristo, para perdão dos pecados.", "Actos 2.38")

    # === Art. 9
    h2(doc, "O Baptismo no Espírito Santo", numero="9.º")
    paragrafo(doc,
        "Cremos na promessa do baptismo no Espírito Santo como experiência "
        "concedida por Deus para revestir o crente de poder para testemunhar "
        "e servir. Reconhecemos a actuação contínua do Espírito Santo na "
        "vida da Igreja e a manifestação dos dons espirituais segundo Sua "
        "soberana vontade, sempre em conformidade com a Palavra e para a "
        "edificação do Corpo de Cristo.")
    citacao(doc, "Mas recebereis a virtude do Espírito Santo, que há-de vir sobre vós; e ser-me-eis testemunhas.", "Actos 1.8")
    citacao(doc, "E todos foram cheios do Espírito Santo, e começaram a falar noutras línguas, conforme o Espírito Santo lhes concedia que falassem.", "Actos 2.4")

    # === Art. 10
    h2(doc, "A Igreja", numero="10.º")
    paragrafo(doc,
        "Cremos que a Igreja é o Corpo de Cristo, una, santa, universal e "
        "apostólica, composta por todos os que nasceram de novo, em todos "
        "os tempos e lugares. Manifesta-se localmente em comunidades de "
        "fé visíveis. A sua missão é adorar a Deus, proclamar o Evangelho, "
        "fazer discípulos, servir ao próximo, edificar os santos e "
        "manifestar o Reino de Deus até à volta de Cristo.")
    citacao(doc, "E sobre esta pedra edificarei a minha igreja, e as portas do inferno não prevalecerão contra ela.", "Mateus 16.18")
    citacao(doc, "Há um só corpo e um só Espírito, como também fostes chamados em uma só esperança da vossa vocação.", "Efésios 4.4")

    # === Art. 11
    h2(doc, "Os Ministérios e os Dons", numero="11.º")
    paragrafo(doc,
        "Cremos que Deus continua chamando e capacitando homens e mulheres "
        "para servirem conforme os dons e ministérios concedidos pelo "
        "Espírito Santo, visando à edificação da Igreja, ao amadurecimento "
        "dos discípulos e à expansão do Reino. Reconhecemos os ministérios "
        "edificadores indicados em Efésios 4.11 — apóstolos, profetas, "
        "evangelistas, pastores e mestres — como dons de Cristo para o "
        "aperfeiçoamento dos santos.")
    citacao(doc, "E ele mesmo deu uns para apóstolos, e outros para profetas, e outros para evangelistas, e outros para pastores e doutores, querendo o aperfeiçoamento dos santos.", "Efésios 4.11-12")

    # === Art. 12
    h2(doc, "Santidade e Vida Cristã", numero="12.º")
    paragrafo(doc,
        "Cremos que todos os discípulos de Cristo são chamados a viver em "
        "santidade, amor, integridade, humildade e obediência à Palavra de "
        "Deus, reflectindo o carácter de Cristo em todas as áreas da vida — "
        "família, trabalho, igreja, sociedade. A santidade não é opcional, "
        "mas vocação inseparável da salvação.")
    citacao(doc, "Sede santos, porque eu sou santo.", "1 Pedro 1.16")
    citacao(doc, "Segui a paz com todos, e a santificação, sem a qual ninguém verá o Senhor.", "Hebreus 12.14")

    # === Art. 13
    h2(doc, "Evangelização e Missões", numero="13.º")
    paragrafo(doc,
        "Cremos que anunciar o Evangelho de Jesus Cristo e fazer discípulos "
        "de todas as nações é responsabilidade permanente e irrenunciável da "
        "Igreja. Cada cristão é chamado a testemunhar do Senhor por meio de "
        "palavras, obras e uma vida transformada, contribuindo activamente "
        "para o cumprimento da Grande Comissão.")
    citacao(doc, "Ide por todo o mundo, pregai o evangelho a toda criatura.", "Marcos 16.15")
    citacao(doc, "E ser-me-eis testemunhas tanto em Jerusalém como em toda a Judéia e Samaria, e até aos confins da terra.", "Actos 1.8")

    # === Art. 14
    h2(doc, "Cura Divina e Acção Sobrenatural de Deus", numero="14.º")
    paragrafo(doc,
        "Cremos que Deus continua agindo com poder, respondendo às orações, "
        "realizando curas, milagres e intervenções sobrenaturais segundo Sua "
        "soberana vontade. Toda manifestação espiritual deve ser exercida em "
        "conformidade com as Escrituras, em ordem, em amor e para a glória de "
        "Deus, sem sensacionalismo nem manipulação.")
    citacao(doc, "Está alguém entre vós doente? Chame os anciãos da igreja, e orem sobre ele, ungindo-o com azeite em nome do Senhor.", "Tiago 5.14")
    citacao(doc, "Jesus Cristo é o mesmo ontem, e hoje, e eternamente.", "Hebreus 13.8")

    # === Art. 15
    h2(doc, "A Segunda Vinda de Cristo", numero="15.º")
    paragrafo(doc,
        "Cremos na volta pessoal, visível, corporal e gloriosa de Jesus Cristo, "
        "na ressurreição dos mortos, no juízo final, na consumação do Reino de "
        "Deus, na vida eterna dos salvos e na condenação eterna dos que rejeitam "
        "o Evangelho. Esta esperança alimenta a vigilância, a santificação e a "
        "missão da Igreja.")
    citacao(doc, "Este Jesus, que dentre vós foi recebido em cima no céu, há-de vir assim como para o céu o vistes ir.", "Actos 1.11")
    citacao(doc, "Eis que cedo venho, e o meu galardão está comigo, para dar a cada um segundo a sua obra.", "Apocalipse 22.12")

    # === Art. 16
    h2(doc, "A Esperança Eterna", numero="16.º")
    paragrafo(doc,
        "Cremos que Deus estabelecerá plenamente o Seu Reino — novos céus e "
        "nova terra, onde habita a justiça —, onde habitarão para sempre "
        "todos os que pertencem a Cristo. Essa esperança bem-aventurada "
        "fortalece a Igreja para viver em fidelidade, perseverança e expectativa "
        "da plena restauração de todas as coisas.")
    citacao(doc, "Eis o tabernáculo de Deus com os homens, pois com eles habitará, e eles serão o seu povo, e o mesmo Deus estará com eles, e será o seu Deus.", "Apocalipse 21.3")
    citacao(doc, "Mas, segundo a sua promessa, aguardamos novos céus e nova terra, em que habita a justiça.", "2 Pedro 3.13")

    # === Compromisso
    h1(doc, "Compromisso Doutrinário")
    paragrafo(doc,
        "A Escola Bíblica Epignósis compromete-se a ensinar as Sagradas "
        "Escrituras com fidelidade, tendo Jesus Cristo como centro de toda a "
        "revelação bíblica e reconhecendo a actuação presente do Espírito "
        "Santo na vida da Igreja. Todo conteúdo produzido pela escola "
        "buscará promover um conhecimento profundo de Deus que conduza à "
        "maturidade espiritual, ao desenvolvimento do carácter cristão e ao "
        "serviço fiel no Reino.")
    paragrafo(doc,
        "Todo docente, ao assumir uma cátedra na Escola Bíblica Epignósis, "
        "subscreve formalmente esta Declaração de Fé, assumindo o compromisso "
        "de ensiná-la com fidelidade e integridade. Toda revisão da presente "
        "Declaração depende de aprovação institucional, em conformidade com o "
        "Regimento Académico.")

    h1(doc, "Lema Institucional")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Conhecer a Deus. Viver a Palavra. Manifestar o Reino.")
    r.font.name = FONTE_TITULO; r.font.size = Pt(15); r.font.italic = True
    r.font.bold = True; r.font.color.rgb = COR_PRIMARIA

    selo_final(doc)

    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-002_Declaracao_de_Fe.docx")
    doc.save(out)
    print("OK:", out)


if __name__ == "__main__":
    gerar()
