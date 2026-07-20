"""DOC 3 — Projecto Pedagógico Oficial (PPO)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _estilos import *
from _estilos import _shade_cell, _add_horizontal_line


def gerar():
    doc = novo_documento("Projecto Pedagógico Oficial", "EBE-DOC-003")
    add_capa(doc,
        supratitulo="Documento Institucional N.º 3",
        titulo="Projecto Pedagógico\nOficial (PPO)",
        subtitulo="Fundamentos Acadêmicos, Pedagógicos e Ministeriais",
        codigo="EBE-DOC-003", ano="2026")
    add_marco_filosofico(doc)

    h1(doc, "Sumário")
    lista(doc, [
        "1. Apresentação",
        "2. Natureza da Escola",
        "3. Finalidade",
        "4. Objectivos Gerais",
        "5. Perfil do Egresso",
        "6. Modelo Pedagógico — Os Quatro Eixos",
        "7. Estrutura Acadêmica",
        "8. Metodologia de Ensino",
        "9. Materiais Didácticos",
        "10. Sistema de Avaliação",
        "11. Corpo Docente",
        "12. Organização Curricular Progressiva",
        "13. Certificação",
        "14. Compromisso com a Excelência",
        "15. Compromisso com o Reino de Deus",
        "Declaração Institucional Final",
    ])
    page_break(doc)

    h1(doc, "Apresentação", numero=1)
    paragrafo(doc,
        "O presente Projecto Pedagógico Oficial (PPO) estabelece os "
        "fundamentos acadêmicos, pedagógicos e ministeriais que orientam a "
        "actuação da Escola Bíblica Epignósis. Trata-se do documento "
        "estruturante da actividade educativa da instituição, articulando-se "
        "com a Declaração de Fé, a Missão, a Visão, os Valores e o Regimento "
        "Académico.")
    paragrafo(doc,
        "A Escola Bíblica Epignósis nasce com o propósito de oferecer uma "
        "formação bíblica, teológica, espiritual e ministerial de excelência, "
        "conduzindo os seus alunos ao conhecimento pleno de Deus (ἐπίγνωσις) "
        "por meio das Escrituras, da acção do Espírito Santo e da prática do "
        "Evangelho.")
    paragrafo(doc,
        "Toda a organização curricular, metodologia, produção de materiais "
        "didácticos e formação docente está fundamentada na Palavra de Deus, "
        "tendo Jesus Cristo como centro e o Espírito Santo como Aquele que "
        "ilumina e transforma o coração do estudante.")
    citacao(doc, "Estatuiu Esdras no seu coração estudar a lei do Senhor, e cumpri-la, e ensinar em Israel os seus estatutos e os seus juízos.", "Esdras 7.10")

    h1(doc, "Natureza da Escola", numero=2)
    paragrafo(doc,
        "A Escola Bíblica Epignósis é uma instituição de formação cristã "
        "dedicada ao ensino das Escrituras, à capacitação ministerial e ao "
        "desenvolvimento integral do discípulo de Cristo. A sua proposta "
        "pedagógica une cinco dimensões formativas indissociáveis:")
    lista(doc, [
        "Formação Bíblica — domínio sistemático e progressivo das Escrituras.",
        "Formação Teológica — compreensão estruturada das doutrinas da fé.",
        "Formação Espiritual — vida no Espírito, oração e santidade.",
        "Formação Ministerial — capacitação prática para o serviço cristão.",
        "Formação do Carácter — virtudes e maturidade segundo Cristo.",
    ], ordenada=True)
    paragrafo(doc,
        "O objectivo da Escola não é apenas transmitir conhecimento, mas "
        "formar discípulos maduros, líderes íntegros e ministros preparados "
        "para servir ao Reino de Deus.")

    h1(doc, "Finalidade", numero=3)
    paragrafo(doc, "A Escola Bíblica Epignósis existe para:")
    lista(doc, [
        "Ensinar fielmente as Sagradas Escrituras.",
        "Formar discípulos comprometidos com Cristo.",
        "Desenvolver maturidade espiritual no povo de Deus.",
        "Capacitar líderes e obreiros para o serviço cristão.",
        "Preparar ministros para todas as áreas de serviço na Igreja.",
        "Fortalecer a Igreja por meio do ensino consistente e doutrinariamente fiel.",
        "Promover uma vida de santidade, comunhão e serviço.",
        "Multiplicar discípulos que ensinam outros (2 Timóteo 2.2).",
    ], ordenada=True)

    h1(doc, "Objectivos Gerais", numero=4)
    paragrafo(doc, "Ao concluir sua formação, espera-se que o aluno:")
    lista(doc, [
        "Conheça profundamente a Bíblia, em seu conjunto e em suas partes.",
        "Interprete correctamente as Escrituras à luz de princípios hermenêuticos sólidos.",
        "Desenvolva uma vida de oração e comunhão consistente com Deus.",
        "Demonstre maturidade espiritual e equilíbrio emocional.",
        "Exerça os seus dons com discernimento e responsabilidade.",
        "Sirva com excelência na igreja local.",
        "Faça discípulos e ensine outros com fidelidade.",
        "Pregue o Evangelho com clareza, fundamentação e ousadia.",
        "Reflicta o carácter de Cristo em todas as esferas da vida.",
    ], ordenada=True)

    h1(doc, "Perfil do Egresso", numero=5)
    paragrafo(doc,
        "O egresso da Escola Bíblica Epignósis será reconhecido pela "
        "convergência de quatro grandes dimensões de formação:")

    h3(doc, "Conhecimento")
    lista(doc, [
        "Domínio das Sagradas Escrituras.",
        "Sólida formação teológica.",
        "Capacidade de interpretar correctamente a Bíblia.",
        "Conhecimento das principais doutrinas cristãs.",
    ])
    h3(doc, "Espiritualidade")
    lista(doc, [
        "Vida devocional consistente.",
        "Dependência consciente do Espírito Santo.",
        "Vida de oração e intercessão.",
        "Busca permanente de santidade.",
    ])
    h3(doc, "Carácter")
    lista(doc, [
        "Humildade.", "Integridade.", "Amor genuíno.", "Ética cristã.", "Fidelidade.",
    ])
    h3(doc, "Ministério")
    lista(doc, [
        "Capacidade para ensinar.",
        "Capacidade para discipular.",
        "Disposição para servir.",
        "Liderança bíblica.",
        "Compromisso com a missão da Igreja.",
    ])

    h1(doc, "Modelo Pedagógico — Os Quatro Eixos", numero=6)
    paragrafo(doc,
        "Toda formação na Escola Bíblica Epignósis seguirá quatro eixos "
        "integrados, que estruturam o desenho de cada apostila, módulo, "
        "curso, escola e instituto:")
    eixos = [
        ("CONHECER", "Compreender correctamente as Escrituras e as doutrinas da fé."),
        ("CRER",     "Firmar convicções bíblicas sólidas e duradouras."),
        ("VIVER",    "Aplicar a Palavra na vida diária — família, trabalho, igreja, sociedade."),
        ("SERVIR",   "Pôr os dons a serviço do Reino com excelência e amor."),
    ]
    tbl = doc.add_table(rows=1, cols=2)
    hdr = tbl.rows[0].cells
    for i, t in enumerate(["Eixo", "Descrição"]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(t)
        r.font.bold = True; r.font.name = FONTE_TITULO; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        _shade_cell(hdr[i], "1B3A5C")
    for nome, d in eixos:
        row = tbl.add_row().cells
        row[0].text = nome; row[1].text = d
        for c in row:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = FONTE_CORPO; r.font.size = Pt(11)

    h1(doc, "Estrutura Acadêmica", numero=7)
    paragrafo(doc,
        "A Escola Bíblica Epignósis está organizada numa arquitectura "
        "hierárquica de sete níveis, da macroestrutura institucional até à "
        "unidade mínima de estudo (apostila). Esta arquitectura é "
        "detalhadamente apresentada no Documento N.º 5 — Arquitectura Oficial.")
    lista(doc, [
        "Nível 1 — Escola Bíblica Epignósis (instituição).",
        "Nível 2 — Institutos (grandes áreas do conhecimento cristão).",
        "Nível 3 — Escolas (especializações dentro de cada Instituto).",
        "Nível 4 — Programas de Formação (públicos e níveis distintos).",
        "Nível 5 — Cursos (unidades temáticas com competência específica).",
        "Nível 6 — Módulos (subdivisões temáticas de cada curso).",
        "Nível 7 — Apostilas (unidades mínimas de estudo).",
    ], ordenada=True)
    paragrafo(doc, "A formação integral é articulada em quatro grandes níveis espirituais e formativos:")
    lista(doc, [
        "Nível Discípulo (Conhecer) — fundamentos da fé cristã.",
        "Nível Crescimento (Ser) — maturidade espiritual e doutrinária.",
        "Nível Servir (Ministério) — capacitação ministerial prática.",
        "Nível Multiplicação (Reino) — formação de líderes e multiplicadores.",
    ], ordenada=True)

    h1(doc, "Metodologia de Ensino", numero=8)
    paragrafo(doc, "Toda aula buscará integrar, conforme o conteúdo:")
    lista(doc, [
        "Exposição bíblica clara e fundamentada.",
        "Reflexão teológica articulada.",
        "Aplicação prática à vida do aluno.",
        "Exercícios e tarefas de fixação.",
        "Momentos de oração e adoração.",
        "Estudos de caso ministeriais.",
        "Perguntas para revisão e auto-avaliação.",
        "Incentivo permanente à leitura da Bíblia.",
        "Diálogo respeitoso e construtivo.",
    ])
    paragrafo(doc,
        "O aluno será constantemente estimulado a colocar em prática aquilo "
        "que aprender, segundo o princípio de Tiago 1.22: “Sede cumpridores "
        "da palavra, e não somente ouvintes, enganando-vos com falsos "
        "discursos”.")

    h1(doc, "Materiais Didácticos", numero=9)
    paragrafo(doc,
        "A Escola utilizará materiais produzidos especialmente para o seu "
        "currículo, dentro de um padrão editorial e identidade visual "
        "próprios, incluindo, entre outros:")
    lista(doc, [
        "Apostilas (unidade mínima de estudo, 10–15 páginas, um conceito central).",
        "Livros e manuais.", "Revistas e periódicos institucionais.",
        "Guias de estudo.", "Mapas mentais e esquemas conceituais.",
        "Quadros comparativos e infográficos.",
        "Exercícios, questionários e avaliações.",
        "Planos de leitura bíblica orientada.",
    ])
    paragrafo(doc,
        "Cada apostila trará na sua abertura o Marco Filosófico da Escola, "
        "garantindo unidade de identidade e propósito em todo material "
        "produzido.")

    h1(doc, "Sistema de Avaliação", numero=10)
    paragrafo(doc,
        "A avaliação na Escola Bíblica Epignósis não se reduz à verificação "
        "da memorização de conteúdos. Visa, antes, acompanhar a compreensão, "
        "a capacidade de aplicação e o crescimento integral do aluno. "
        "Adopta, portanto, carácter formativo e contínuo, podendo recorrer "
        "aos seguintes instrumentos:")
    lista(doc, [
        "Provas escritas.", "Questionários.", "Trabalhos académicos.",
        "Pesquisas bíblicas e teológicas.", "Apresentações orais.",
        "Estudos bíblicos preparados pelo aluno.",
        "Projectos ministeriais práticos.", "Participação activa nas aulas.",
        "Auto-avaliação reflexiva.",
    ])
    paragrafo(doc,
        "Os critérios específicos de aprovação serão definidos pela "
        "Coordenação Acadêmica para cada curso, observados os princípios do "
        "Regimento Académico.")

    h1(doc, "Corpo Docente", numero=11)
    paragrafo(doc, "Os professores da Escola Bíblica Epignósis deverão demonstrar:")
    lista(doc, [
        "Fidelidade às Sagradas Escrituras.",
        "Adesão integral à Declaração de Fé Institucional.",
        "Maturidade cristã reconhecida.",
        "Carácter íntegro e testemunho público compatível.",
        "Capacidade pedagógica e didática.",
        "Espírito de serviço e humildade.",
        "Compromisso com a formação integral dos alunos.",
        "Disposição para o estudo e a actualização permanentes.",
    ])
    citacao(doc, "E o que de mim, entre muitas testemunhas, ouviste, confia-o a homens fiéis, que sejam idóneos para também ensinarem os outros.", "2 Timóteo 2.2")

    h1(doc, "Organização Curricular Progressiva", numero=12)
    paragrafo(doc,
        "O currículo da Escola Bíblica Epignósis é progressivo, cumulativo "
        "e integrado. Nenhum curso existe isoladamente: todos formam uma "
        "única jornada de crescimento espiritual e ministerial. Cada etapa "
        "prepara o aluno para a seguinte, e o conhecimento é edificado em "
        "camadas, conforme detalhado no Documento N.º 8 — Sistema de "
        "Pré-Requisitos.")
    paragrafo(doc,
        "Aplicam-se quatro princípios fundamentais à progressão curricular:")
    lista(doc, [
        "Princípio da Base — não há ministério sem fundamentos da fé.",
        "Princípio da Progressão — nenhum aluno pode “saltar” níveis.",
        "Princípio da Coerência — todo curso pressupõe os anteriores.",
        "Princípio da Multiplicação — todo conhecimento gera ensino.",
    ], ordenada=True)

    h1(doc, "Certificação", numero=13)
    paragrafo(doc, "A Escola Bíblica Epignósis poderá conceder:")
    lista(doc, [
        "Certificados de Conclusão de Apostila.",
        "Certificados de Conclusão de Módulo.",
        "Certificados de Conclusão de Curso.",
        "Certificados de Conclusão de Escola.",
        "Certificados de Conclusão de Programa de Formação.",
        "Diplomas Institucionais para trilhas completas (Discípulo, Crescimento, Servir, Multiplicação).",
        "Diploma de Formação Completa Epignósis (2.200–2.400 horas).",
    ], ordenada=True)
    paragrafo(doc,
        "A certificação acadêmica reconhece o progresso do aluno, mas não "
        "substitui os critérios de vocação, chamado e reconhecimento "
        "ministerial pela igreja local.")

    h1(doc, "Compromisso com a Excelência", numero=14)
    paragrafo(doc,
        "A Escola Bíblica Epignósis compromete-se a manter elevado padrão "
        "de qualidade em seu ensino, materiais didácticos, formação docente "
        "e acompanhamento dos alunos, buscando glorificar a Deus por meio "
        "da excelência em todas as suas actividades (Colossenses 3.23-24).")

    h1(doc, "Compromisso com o Reino de Deus", numero=15)
    paragrafo(doc,
        "Toda formação oferecida pela Escola Bíblica Epignósis existe para "
        "glorificar a Deus, fortalecer Sua Igreja e preparar discípulos que "
        "anunciem o Evangelho, sirvam com humildade e manifestem o Reino de "
        "Cristo em todas as áreas da vida.")
    citacao(doc, "Mas, buscai primeiro o reino de Deus, e a sua justiça, e todas estas coisas vos serão acrescentadas.", "Mateus 6.33")

    h1(doc, "Declaração Institucional Final")
    paragrafo(doc,
        "A Escola Bíblica Epignósis entende que o verdadeiro sucesso de sua "
        "missão não será medido apenas pela quantidade de cursos oferecidos "
        "ou de certificados emitidos, mas pela formação de homens e mulheres "
        "que conheçam profundamente a Deus, vivam fielmente Sua Palavra e "
        "manifestem o Reino de Cristo por meio de uma vida transformada.")

    selo_final(doc)
    out = os.path.join(os.path.dirname(__file__), "EBE-DOC-003_Projecto_Pedagogico_Oficial.docx")
    doc.save(out); print("OK:", out)


if __name__ == "__main__":
    gerar()
