"""DOC 4 — Regimento Académico"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Regimento Académico", "EBE-DOC-004")
    add_capa(doc,
        supratitulo="Documento Institucional N.º 4",
        titulo="Regimento Académico",
        subtitulo="Normas de Organização e Funcionamento",
        codigo="EBE-DOC-004", ano="2026")
    add_marco_filosofico(doc)

    h1(doc, "Sumário")
    lista(doc, [
        "Capítulo I — Das Disposições Gerais",
        "Capítulo II — Da Organização Institucional",
        "Capítulo III — Dos Alunos",
        "Capítulo IV — Dos Professores",
        "Capítulo V — Da Metodologia",
        "Capítulo VI — Das Avaliações",
        "Capítulo VII — Da Frequência",
        "Capítulo VIII — Da Certificação",
        "Capítulo IX — Da Conduta Cristã",
        "Capítulo X — Da Ética Acadêmica",
        "Capítulo XI — Da Disciplina",
        "Capítulo XII — Da Revisão Curricular",
        "Capítulo XIII — Das Disposições Finais",
    ])
    page_break(doc)

    capitulo(doc, "I", "Das Disposições Gerais")
    artigo(doc, 1,
        "O presente Regimento Académico estabelece as normas de funcionamento "
        "da Escola Bíblica Epignósis, regulamentando a sua organização "
        "administrativa, pedagógica e académica, em conformidade com a sua "
        "Missão, Visão, Valores, Declaração de Fé e Projecto Pedagógico Oficial.")
    artigo(doc, 2,
        "A Escola Bíblica Epignósis tem como finalidade promover uma formação "
        "bíblica, teológica, espiritual e ministerial fundamentada nas "
        "Sagradas Escrituras e orientada pela acção do Espírito Santo.")
    artigo(doc, 3,
        "O Lema Institucional “Conhecer a Deus. Viver a Palavra. Manifestar "
        "o Reino.” inspira e orienta toda a actuação académica, pastoral e "
        "comunitária da instituição.")
    artigo(doc, 4,
        "Aplicam-se a este Regimento, como documentos correlatos e "
        "complementares: a Declaração de Fé (EBE-DOC-002), o Projecto "
        "Pedagógico Oficial (EBE-DOC-003), a Arquitectura Institucional "
        "(EBE-DOC-005), o Mapa de Cursos (EBE-DOC-006), a Duração Oficial "
        "(EBE-DOC-007) e o Sistema de Pré-Requisitos (EBE-DOC-008).")

    capitulo(doc, "II", "Da Organização Institucional")
    artigo(doc, 5,
        "A Escola Bíblica Epignósis será composta pelos seguintes órgãos e instâncias:",
        incisos=[
            "Diretoria Geral, responsável pela direção institucional e estratégica;",
            "Coordenação Acadêmica, responsável pela execução do currículo e dos cursos;",
            "Coordenação Pedagógica, responsável pelas metodologias, materiais e avaliação;",
            "Coordenação Espiritual e Pastoral, responsável pela vida devocional e cuidado pastoral;",
            "Conselho Doutrinário, responsável pela guarda da sã doutrina e revisão de conteúdos;",
            "Corpo Docente;",
            "Corpo Discente;",
            "Secretaria Acadêmica;",
            "Departamentos, Institutos e Escolas Temáticas, quando instituídos.",
        ])
    artigo(doc, 6,
        "A Diretoria Geral é a instância máxima de governo da Escola, sendo "
        "responsável pela aprovação dos planos institucionais, revisão dos "
        "documentos oficiais e nomeação dos coordenadores.")
    artigo(doc, 7,
        "O Conselho Doutrinário é composto por membros maduros na fé, "
        "indicados pela Diretoria, e tem como atribuição zelar pela "
        "fidelidade do ensino à Declaração de Fé Institucional.")

    capitulo(doc, "III", "Dos Alunos")
    artigo(doc, 8,
        "Considera-se aluno da Escola Bíblica Epignósis toda pessoa "
        "regularmente matriculada em qualquer programa de formação oferecido "
        "pela instituição, observados os pré-requisitos próprios de cada curso.")

    secao_titulada(doc, "Secção I — Dos Direitos do Aluno")
    artigo(doc, 9, "São direitos do aluno:",
        incisos=[
            "receber ensino fundamentado nas Escrituras e de qualidade;",
            "utilizar os materiais didácticos disponibilizados;",
            "ser tratado com respeito, dignidade e imparcialidade;",
            "participar activamente das actividades acadêmicas e devocionais;",
            "solicitar esclarecimentos sobre as suas avaliações;",
            "ser acompanhado pastoral e pedagogicamente em seu desenvolvimento;",
            "receber certificação adequada quando cumprir os requisitos estabelecidos;",
            "ter preservada a confidencialidade das suas informações pessoais.",
        ])

    secao_titulada(doc, "Secção II — Dos Deveres do Aluno")
    artigo(doc, 10, "São deveres do aluno:",
        incisos=[
            "respeitar e honrar os princípios e a identidade doutrinária da Escola;",
            "manter postura cristã dentro e fora do ambiente académico;",
            "cumprir, dentro dos prazos, as actividades propostas;",
            "preservar o património material e intelectual da instituição;",
            "respeitar professores, colegas e colaboradores;",
            "zelar pela unidade, pelo amor fraterno e pela boa convivência;",
            "comunicar à Coordenação eventuais impedimentos ou dificuldades;",
            "submeter-se à disciplina académica e espiritual da Escola.",
        ])

    capitulo(doc, "IV", "Dos Professores")
    artigo(doc, 11,
        "O exercício do magistério na Escola Bíblica Epignósis é considerado "
        "ministério, sendo conferido a homens e mulheres com vocação, "
        "preparo bíblico-teológico e testemunho cristão público compatível.")
    artigo(doc, 12, "São deveres do docente:",
        incisos=[
            "ensinar em estrita conformidade com as Escrituras e com a Declaração de Fé da Escola;",
            "subscrever formalmente a Declaração de Fé Institucional;",
            "preparar cuidadosa e oracionalmente as suas aulas e materiais;",
            "manter postura ética, espiritual e cristã exemplar;",
            "incentivar o crescimento espiritual e intelectual dos alunos;",
            "actualizar continuamente os seus conhecimentos;",
            "submeter os seus materiais à revisão pedagógica e doutrinária da Escola, quando solicitado;",
            "tratar com confidencialidade as informações dos alunos.",
        ])
    citacao(doc, "Meus irmãos, muitos de vós não sejam mestres, sabendo que receberemos maior juízo.", "Tiago 3.1")

    capitulo(doc, "V", "Da Metodologia")
    artigo(doc, 13, "O ensino na Escola Bíblica Epignósis combinará, conforme o conteúdo:",
        incisos=[
            "aulas expositivas;",
            "estudos bíblicos dirigidos;",
            "leitura orientada de textos e fontes;",
            "exercícios e questionários;",
            "actividades práticas e ministeriais;",
            "debates respeitosos e construtivos;",
            "momentos de oração, adoração e reflexão devocional;",
            "avaliações formativas e somativas.",
        ])
    artigo(doc, 14,
        "Toda aprendizagem deverá conduzir à transformação de vida, à "
        "maturidade espiritual e ao serviço cristão, em fidelidade ao "
        "modelo educativo descrito no Projecto Pedagógico Oficial.")

    capitulo(doc, "VI", "Das Avaliações")
    artigo(doc, 15, "A avaliação poderá ocorrer por meio de:",
        incisos=[
            "provas escritas;",
            "questionários;",
            "trabalhos académicos;",
            "apresentações orais;",
            "projectos ministeriais;",
            "estudos bíblicos preparados pelo aluno;",
            "actividades práticas;",
            "participação activa nas aulas;",
            "auto-avaliação reflexiva.",
        ])
    artigo(doc, 16,
        "O objectivo principal da avaliação é acompanhar o progresso do "
        "aluno, identificar dificuldades, incentivar o seu crescimento e "
        "verificar o cumprimento dos objectivos formativos do curso.",
        paragrafo_unico=
        "Os critérios objectivos de aprovação serão definidos pela Coordenação "
        "Acadêmica para cada curso, observada a média mínima institucional "
        "fixada em ato próprio.")

    capitulo(doc, "VII", "Da Frequência")
    artigo(doc, 17,
        "A frequência às aulas é considerada parte essencial da formação, "
        "expressando o compromisso do aluno com o seu próprio desenvolvimento.")
    artigo(doc, 18,
        "A Escola estabelecerá percentual mínimo de participação para "
        "certificação em cursos presenciais ou híbridos, fixado por acto "
        "da Coordenação Acadêmica.",
        paragrafo_unico=
        "Nos cursos on-line, a participação poderá ser aferida pelo "
        "acompanhamento sistemático das actividades propostas e pelo "
        "cumprimento dos prazos.")

    capitulo(doc, "VIII", "Da Certificação")
    artigo(doc, 19,
        "Receberá certificação o aluno que cumprir os critérios "
        "estabelecidos para cada curso, incluindo frequência, participação "
        "e aproveitamento acadêmico, conforme definido pela Coordenação "
        "Acadêmica.")
    artigo(doc, 20, "A Escola poderá conceder, conforme a etapa concluída:",
        incisos=[
            "Certificados de Conclusão de Apostila;",
            "Certificados de Conclusão de Módulo;",
            "Certificados de Conclusão de Curso;",
            "Certificados de Conclusão de Escola;",
            "Certificados de Conclusão de Programa de Formação;",
            "Diplomas Institucionais para trilhas completas (Discípulo, Crescimento, Servir, Multiplicação);",
            "Diploma de Formação Completa Epignósis.",
        ])
    artigo(doc, 21,
        "A certificação académica reconhece o progresso do aluno, mas não "
        "substitui a vocação, o chamado nem o reconhecimento ministerial "
        "concedido pela igreja local.")

    capitulo(doc, "IX", "Da Conduta Cristã")
    artigo(doc, 22,
        "A Escola Bíblica Epignósis espera de todos os seus membros uma "
        "conduta compatível com os princípios cristãos, em todas as "
        "esferas — académica, eclesial, familiar e pública.")
    artigo(doc, 23, "São incentivadas, entre outras, as seguintes atitudes:",
        incisos=[
            "amor fraterno;",
            "respeito mútuo;",
            "honestidade;",
            "humildade;",
            "espírito de serviço;",
            "responsabilidade;",
            "espírito de cooperação e unidade;",
            "domínio próprio;",
            "mansidão na palavra.",
        ])
    artigo(doc, 24,
        "Não serão toleradas atitudes que promovam desrespeito, divisão, "
        "discriminação, desonestidade, imoralidade pública ou qualquer "
        "comportamento incompatível com os valores da instituição.")
    citacao(doc, "Em tudo te dá por exemplo de boas obras; na doutrina mostra incorrupção, gravidade, sinceridade.", "Tito 2.7")

    capitulo(doc, "X", "Da Ética Acadêmica")
    artigo(doc, 25, "Constituem deveres éticos de docentes e discentes:",
        incisos=[
            "produzir trabalhos originais;",
            "citar correctamente as fontes utilizadas;",
            "evitar qualquer forma de plágio;",
            "realizar as avaliações com honestidade;",
            "preservar a integridade acadêmica e espiritual;",
            "abster-se de utilizar a instituição para fins pessoais incompatíveis com a sua missão.",
        ])
    artigo(doc, 26,
        "A Escola entende que excelência acadêmica e integridade cristã "
        "caminham juntas, e que a desonestidade intelectual é incompatível "
        "com o testemunho cristão.")

    capitulo(doc, "XI", "Da Disciplina")
    artigo(doc, 27,
        "Sempre que necessário, situações disciplinares serão tratadas com:",
        incisos=[
            "justiça;",
            "imparcialidade;",
            "espírito pastoral;",
            "oportunidade de diálogo e contraditório;",
            "objectivo restaurador;",
            "confidencialidade.",
        ])
    artigo(doc, 28,
        "Toda medida disciplinar buscará a correcção, a reconciliação e o "
        "crescimento do aluno, e não a sua humilhação.",
        paragrafo_unico=
        "Conforme a gravidade do caso, poderá haver: advertência verbal, "
        "advertência escrita, suspensão temporária ou desligamento "
        "institucional, sempre precedidos de contraditório e oração.")
    citacao(doc, "Irmãos, se algum homem chegar a ser surpreendido nalguma ofensa, vós, que sois espirituais, encaminhai o tal com espírito de mansidão.", "Gálatas 6.1")

    capitulo(doc, "XII", "Da Revisão Curricular")
    artigo(doc, 29,
        "O currículo da Escola poderá ser ampliado, actualizado ou "
        "reorganizado sempre que necessário, preservando a sua identidade "
        "doutrinária, missão institucional e compromisso com as Escrituras.")
    artigo(doc, 30,
        "A revisão curricular será proposta pela Coordenação Acadêmica, "
        "ouvido o Conselho Doutrinário, e aprovada pela Diretoria Geral.")

    capitulo(doc, "XIII", "Das Disposições Finais")
    artigo(doc, 31,
        "Os casos não previstos neste Regimento serão analisados pela "
        "Diretoria e pela Coordenação Acadêmica, sempre à luz das "
        "Escrituras, da Declaração de Fé, dos Princípios Pedagógicos e do "
        "Projecto Pedagógico Oficial da Escola Bíblica Epignósis.")
    artigo(doc, 32,
        "Este Regimento entra em vigor na data da sua aprovação institucional, "
        "permanecendo válido até a sua revisão oficial.",
        paragrafo_unico=
        "Toda alteração deste Regimento depende de aprovação formal da "
        "Diretoria Geral, registada em acta institucional.")

    h1(doc, "Compromisso Final")
    paragrafo(doc,
        "A Escola Bíblica Epignósis existe para servir à Igreja de Cristo por "
        "meio da formação de discípulos que conheçam profundamente a Deus, "
        "vivam fielmente Sua Palavra e manifestem o Reino em todas as áreas da vida.")

    selo_final(doc)
    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-004_Regimento_Academico.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
