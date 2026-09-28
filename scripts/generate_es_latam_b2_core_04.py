#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Core Unit 4:
  - Title: "Influence, Will & Value Judgments" (Voluntad, influencia y juicios de valor)
  - Stems: b2-04-01 through b2-04-consolidation
  - Classic Literature Story: Carlos Fuentes - "La muerte de Artemio Cruz: Voluntad, poder y juicio póstumo"
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_core_unit_4():
    # Vocab theme slug: b2-unit04-vocab
    # Grammar skills:
    #   - subjuntivo-influencia-mandato
    #   - juicios-valor-subjuntivo
    #   - reaccion-afectiva-subjuntivo
    #   - infinitivo-vs-subjuntivo-correferencia

    # --------------------------------------------------------------------------
    # Lesson 1: b2-04-01 - Verbos de influencia, mandato y exigencia
    # --------------------------------------------------------------------------
    l1 = "b2-04-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.04.01",
        "lesson": l1,
        "title": "Voluntad, imposición y demandas cívicas",
        "theme": "Verbos de influencia, coerción y petición formal",
        "words": [
            {"lemma": "exigir", "translation": "to demand, to require", "pos": "verb"},
            {"lemma": "el requerimiento", "translation": "requirement, formal demand", "pos": "noun"},
            {"lemma": "instar", "translation": "to urge, to press", "pos": "verb"},
            {"lemma": "la prerrogativa", "translation": "prerogative, privilege", "pos": "noun"},
            {"lemma": "acatar", "translation": "to comply with, to abide by", "pos": "verb"},
            {"lemma": "imperativo", "translation": "imperative, urgent", "pos": "adjective"},
            {"lemma": "el desacato", "translation": "contempt, non-compliance", "pos": "noun"},
            {"lemma": "estipular", "translation": "to stipulate", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.04.01.subjuntivo-influencia",
        "title": "El subjuntivo en oraciones sustantivas de influencia",
        "sections": [
            {
                "type": "text",
                "title": "Verbos de voluntad y mandato",
                "content": "Los verbos que implican influir sobre la conducta de otra persona (mandar, prohibir, exigir, instar, solicitar, pedir, impedir) exigen de modo categórico el verbo subordinado en modo subjuntivo cuando hay cambio de sujeto: 'El comité exige que los delegados presenten credenciales'."
            },
            {
                "type": "table",
                "title": "Matices de influencia en registro formal",
                "rows": [
                    ["Mandato estricto", "'Exigir / Ordenar que + subjuntivo': 'La ley exige que se respeten los plazos procesales'"],
                    ["Exhortación formal", "'Instar a que / Exhortar a que + subjuntivo': 'La cancillería insta a que las partes reanuden el diálogo'"],
                    ["Oposición e impedimento", "'Impedir / Prohibir que + subjuntivo': 'El bloqueo impidió que llegaran los suministros médicos'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el discurso institucional",
                "items": [
                    {"spanish": "El presidente del tribunal ordenó que se desalojara la sala de audiencias.", "english": "The court president ordered that the courtroom be cleared."},
                    {"spanish": "La comisión internacional insta a que los gobiernos garanticen la libertad de prensa.", "english": "The international commission urges governments to guarantee freedom of the press."},
                    {"spanish": "Las normas sanitarias impiden que los pasajeros aborden sin la documentación requerida.", "english": "Health regulations prevent passengers from boarding without the required documentation."}
                ]
            },
            {
                "type": "tip",
                "content": "Con verbos como 'prohibir', 'permitir' o 'aconsejar', cuando el destinatario aparece como pronombre indirecto, el español culto permite alternar entre subjuntivo e infinitivo: 'Les aconsejó que guardaran calma' o 'Les aconsejó guardar calma'."
            }
        ]
    })

    write_json(f"exercises/b2/{l1}-ex.json", {
        "lesson": l1,
        "exercises": [
            {
                "id": f"{l1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["instar", "to urge, to press"],
                    ["acatar", "to comply with, to abide by"],
                    ["el desacato", "contempt, non-compliance"],
                    ["la prerrogativa", "prerogative, privilege"]
                ],
                "teaches": ["b2-unit04-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo verbal rige obligatoriamente el verbo principal en 'El consejo directivo exige que los gerentes _____ el plan de reestructuración'?",
                "options": [
                    "Subjuntivo (acaten), porque denota mandato e influencia sobre la conducta ajena.",
                    "Indicativo (acatan), porque afirma un hecho factual comprobado.",
                    "Condicional (acatarían), porque plantea una hipótesis lejana."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La defensora del pueblo instó a que las autoridades __ de inmediato a los detenidos. (liberar - imperfect subjunctive)",
                "answer": "liberaran",
                "english": "The ombudsperson urged the authorities to immediately release the detainees.",
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Exigen", "que", "se", "respete", "el", "orden", "constitucional."],
                "solution": ["Exigen", "que", "se", "respete", "el", "orden", "constitucional."],
                "english": "They demand that the constitutional order be respected.",
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Mediador", "text": "¿Cuál es la postura irrenunciable del sindicato en esta huelga?"},
                    {"speaker": "Portavoz obrero", "text": "_____"},
                    {"speaker": "Mediador", "text": "Trasladaremos esa petición a la mesa de negociaciones patronal."}
                ],
                "options": [
                    "Exigimos que la empresa restablezca de inmediato los salarios y garantice la seguridad laboral.",
                    "La fábrica fue construida a mediados del siglo pasado junto a la línea férrea.",
                    "El café con leche cuesta dos dólares en la cafetería de la planta."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El juez ordenó que las partes acataran la sentencia sin dilaciones indebidas.",
                "english": "The judge ordered the parties to comply with the sentence without undue delay.",
                "teaches": ["subjuntivo-influencia-mandato"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=4,
        title="Influence, Commands & Institutional Demands",
        goal="Master the subjunctive in noun clauses governed by verbs of influence, command, prohibition, and civic demand.",
        grammar_desc="el subjuntivo en proposiciones subordinadas de influencia y mandato",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Construct formal institutional demands with exigir, ordenar, and instar a que.",
            "Govern past and present subjunctive sequences after verbs of influence.",
            "Deploy civic and legal vocabulary (acatar, prerrogativa, desacato, imperativo)."
        ],
        intro_body=[
            "Welcome to Unit 4: Influence, Will & Value Judgments. At B2, advanced communication requires navigating power relations, institutional authority, and moral critique with precision.",
            "In this unit, inspired by Carlos Fuentes' monumental post-revolutionary novel 'La muerte de Artemio Cruz', you will master the syntax of will and command, impersonal value judgments, affective stance, and the boundary between subjunctive and infinitive coreference."
        ],
        intro_title="Unit 4: Influence, Will & Value Judgments"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-04-02 - Juicios de valor y matrices impersonales
    # --------------------------------------------------------------------------
    l2 = "b2-04-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.04.02",
        "lesson": l2,
        "title": "Evaluación ética y juicios de valor",
        "theme": "Matrices axiológicas y valoración institucional",
        "words": [
            {"lemma": "convenir", "translation": "to be advisable, to suit", "pos": "verb"},
            {"lemma": "indispensable", "translation": "indispensable, essential", "pos": "adjective"},
            {"lemma": "inadmisible", "translation": "unacceptable, inadmissible", "pos": "adjective"},
            {"lemma": "el juicio", "translation": "judgment, trial, sanity", "pos": "noun"},
            {"lemma": "legítimo", "translation": "legitimate, lawful", "pos": "adjective"},
            {"lemma": "censurable", "translation": "blameworthy, censurable", "pos": "adjective"},
            {"lemma": "pertinente", "translation": "pertinent, relevant", "pos": "adjective"},
            {"lemma": "la gravedad", "translation": "seriousness, gravity", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.04.02.juicios-valor-subjuntivo",
        "title": "Juicios de valor y matrices impersonales evaluativas",
        "sections": [
            {
                "type": "text",
                "title": "Valoración moral y conveniencia",
                "content": "Las oraciones impersonales con el verbo 'ser' y un adjetivo o sustantivo de valoración (es indispensable, es insólito, es inadmisible, es una vergüenza, conviene que) seleccionan obligatoriamente modo subjuntivo en la proposición subordinada porque no informan de un hecho objetivo, sino que emiten un juicio sobre él."
            },
            {
                "type": "table",
                "title": "Matrices axiológicas comunes",
                "rows": [
                    ["Necesidad y conveniencia", "'Es imprescindible que', 'Es indispensable que', 'Conviene que': 'Es indispensable que se investigue a fondo'"],
                    ["Juicio ético o desaprobación", "'Es inadmisible que', 'Es censurable que', 'Es una lástima que': 'Es inadmisible que se desvíen fondos públicos'"],
                    ["Extrañeza y sorpresa", "'Es insólito que', 'Es inaudito que', 'Resulta curioso que': 'Es insólito que nadie advirtiera el fraude'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo crítico",
                "items": [
                    {"spanish": "Es inadmisible que persista la opacidad en las contrataciones estatales.", "english": "It is inadmissible that lack of transparency persists in state contracting."},
                    {"spanish": "Conviene que el cuerpo diplomático actúe con prudencia antes de emitir comunicados.", "english": "It is advisable that the diplomatic corps act with prudence before issuing statements."},
                    {"spanish": "Resulta insólito que los legisladores ignoren la jurisprudencia de la corte suprema.", "english": "It is unheard of that legislators ignore the supreme court's case law."}
                ]
            },
            {
                "type": "tip",
                "content": "Contrasta: 'Es seguro que viene' (certeza -> indicativo) frente a 'Es natural que venga' (juicio de valor -> subjuntivo)."
            }
        ]
    })

    write_json(f"exercises/b2/{l2}-ex.json", {
        "lesson": l2,
        "exercises": [
            {
                "id": f"{l2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["inadmisible", "unacceptable, inadmissible"],
                    ["pertinente", "pertinent, relevant"],
                    ["censurable", "blameworthy, censurable"],
                    ["convenir", "to be advisable, to suit"]
                ],
                "teaches": ["b2-unit04-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo exige la matriz 'Es inadmisible que'?",
                "options": [
                    "Subjuntivo, porque formula una valoración ética subjetiva.",
                    "Indicativo, porque describe una regla matemática comprobada.",
                    "Futuro simple, porque pospone el juicio para el próximo año."
                ],
                "correct": 0,
                "teaches": ["juicios-valor-subjuntivo"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Es indispensable que la comisión __ un informe detallado sobre el impacto ecológico. (presentar)",
                "answer": "presente",
                "english": "It is indispensable that the commission submit a detailed report on the ecological impact.",
                "teaches": ["juicios-valor-subjuntivo"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Es", "insólito", "que", "nadie", "haya", "denunciado", "el", "fraude."],
                "solution": ["Es", "insólito", "que", "nadie", "haya", "denunciado", "el", "fraude."],
                "english": "It is unheard of that no one reported the fraud.",
                "teaches": ["juicios-valor-subjuntivo"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Editorialista", "text": "¿Qué opinión le merece la negativa de los funcionarios a declarar?"},
                    {"speaker": "Jurista", "text": "_____"},
                    {"speaker": "Editorialista", "text": "Coincido plenamente; socava la confianza en las instituciones."}
                ],
                "options": [
                    "Es sumamente censurable que servidores públicos eludan la rendición de cuentas ante la ciudadanía.",
                    "El palacio de gobierno tiene una fachada renacentista con seis balcones de hierro forjado.",
                    "Los funcionarios públicos cobran sus salarios el último día hábil de cada mes."
                ],
                "correct": 0,
                "teaches": ["juicios-valor-subjuntivo"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Conviene que todos los actores políticos antepongan el bienestar colectivo a sus intereses partidistas.",
                "english": "It is advisable that all political actors prioritize the collective well-being over their partisan interests.",
                "teaches": ["juicios-valor-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=4,
        title="Value Judgments & Impersonal Matrices",
        goal="Formulate sophisticated moral evaluations, policy judgments, and institutional critiques using impersonal matrices with the subjunctive.",
        grammar_desc="el subjuntivo en oraciones impersonales axiológicas y juicios de valor",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Govern the subjunctive after evaluative matrices (es inadmisible que, conviene que).",
            "Articulate civic and editorial critiques with ethical nuance.",
            "Deploy evaluation vocabulary (censurable, pertinente, indispensable, gravedad)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-04-03 - Reacción afectiva y subjetividad
    # --------------------------------------------------------------------------
    l3 = "b2-04-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.04.03",
        "lesson": l3,
        "title": "Subjetividad y postura afectiva",
        "theme": "Verbos de afección, indignación y complacencia",
        "words": [
            {"lemma": "indignar", "translation": "to outrage, to anger", "pos": "verb"},
            {"lemma": "lamentar", "translation": "to regret, to lament", "pos": "verb"},
            {"lemma": "alarmar", "translation": "to alarm", "pos": "verb"},
            {"lemma": "la indignación", "translation": "outrage, indignation", "pos": "noun"},
            {"lemma": "el regocijo", "translation": "joy, rejoicing", "pos": "noun"},
            {"lemma": "reconfortar", "translation": "to comfort, to hearten", "pos": "verb"},
            {"lemma": "el pesar", "translation": "sorrow, grief", "pos": "noun"},
            {"lemma": "desconcertar", "translation": "to baffle, to disconcert", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.04.03.reaccion-afectiva-subjuntivo",
        "title": "Subjuntivo en proposiciones de reacción afectiva",
        "sections": [
            {
                "type": "text",
                "title": "Verbos de emoción psicológica y postura subjetiva",
                "content": "Los verbos y construcciones que expresan la reacción anímica del emisor ante un hecho ajeno (me alegra que, me indigna que, lamento que, nos alarma que, me reconforta que) seleccionan invariable y obligatoriamente el modo subjuntivo, incluso cuando el hecho aludido es completamente real y verificado en la realidad: 'Me alegra que hayas venido' (el interlocutor vino, pero la cláusula verbaliza la emoción, no el hecho)."
            },
            {
                "type": "table",
                "title": "Estructuras de afección anímica",
                "rows": [
                    ["Pronombre indirecto + verbo + que + SUBJ", "'Me indigna que los monopolios fijen los precios a su antojo'"],
                    ["Verbo transitivo sujeto + que + SUBJ", "'Lamento profundamente que hayamos llegado a esta encrucijada'"],
                    ["Sustantivos de sentimiento + de que + SUBJ", "'Tengo la esperanza de que la diplomacia prospere', 'Siento el pesar de que partan'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate público",
                "items": [
                    {"spanish": "A la ciudadanía le indigna que los casos de corrupción queden impunes.", "english": "Citizens are outraged that corruption cases go unpunished."},
                    {"spanish": "Nos reconforta que las comunidades hayan encontrado formas de resistencia comunal.", "english": "It heartens us that communities have found forms of communal resistance."},
                    {"spanish": "La comunidad científica lamenta que se reduzcan los fondos para la investigación.", "english": "The scientific community laments that funding for research is being cut."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda: el subjuntivo no solo expresa irrealidad o duda; en contextos afectivos expresa la postura valorativa del hablante frente a un hecho conocido ('factividad emotiva')."
            }
        ]
    })

    write_json(f"exercises/b2/{l3}-ex.json", {
        "lesson": l3,
        "exercises": [
            {
                "id": f"{l3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["indignar", "to outrage, to anger"],
                    ["reconfortar", "to comfort, to hearten"],
                    ["el pesar", "sorrow, grief"],
                    ["desconcertar", "to baffle, to disconcert"]
                ],
                "teaches": ["b2-unit04-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué se utiliza el subjuntivo en 'A los vecinos les alarma que aumente la criminalidad'?",
                "options": [
                    "Porque la oración expresa la reacción afectiva o emocional ante el fenómeno.",
                    "Porque los vecinos no están seguros de si la criminalidad existe.",
                    "Porque describe una orden que los vecinos impartieron a la policía."
                ],
                "correct": 0,
                "teaches": ["reaccion-afectiva-subjuntivo"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Nos reconforta que la juventud __ con tanta energía en la defensa de los derechos humanos. (participar)",
                "answer": "participe",
                "english": "It heartens us that youth participate with such energy in the defense of human rights.",
                "teaches": ["reaccion-afectiva-subjuntivo"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Me", "indigna", "que", "hayan", "ocultado", "la", "verdad."],
                "solution": ["Me", "indigna", "que", "hayan", "ocultado", "la", "verdad."],
                "english": "It outrages me that they hid the truth.",
                "teaches": ["reaccion-afectiva-subjuntivo"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Activista", "text": "¿Cómo ha reaccionado la sociedad civil ante el nuevo recorte presupuestario?"},
                    {"speaker": "Abogada", "text": "_____"},
                    {"speaker": "Activista", "text": "Por esa razón han convocado a una marcha multitudinaria."}
                ],
                "options": [
                    "A todo el gremio docente le indigna que se desmantelen las escuelas públicas de las zonas rurales.",
                    "El año fiscal comienza el primero de enero en todo el territorio de la república.",
                    "Los edificios escolares se pintan habitualmente durante las vacaciones de verano."
                ],
                "correct": 0,
                "teaches": ["reaccion-afectiva-subjuntivo"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La comunidad entera lamentó profundamente que el histórico teatro fuera demolido.",
                "english": "The entire community deeply lamented that the historic theater was demolished.",
                "teaches": ["reaccion-afectiva-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=4,
        title="Emotional Reactions & Affective Stance",
        goal="Express personal, civic, and moral reactions using affective matrix verbs that govern the subjunctive.",
        grammar_desc="el subjuntivo en construcciones de afección psicológica y emotiva",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Govern the subjunctive after emotional affect matrices (me indigna que, lamento que).",
            "Express empathy, grief, and moral outrage in formal debate.",
            "Master affective vocabulary (reconfortar, desconcertar, regocijo, pesar)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-04-04 - Infinitivo frente a subjuntivo por correferencia
    # --------------------------------------------------------------------------
    l4 = "b2-04-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.04.04",
        "lesson": l4,
        "title": "Correferencia, agencia y propósito",
        "theme": "Sintaxis de infinitivo frente a subordinación plena",
        "words": [
            {"lemma": "la pretensión", "translation": "aspiration, claim, intention", "pos": "noun"},
            {"lemma": "anhelar", "translation": "to yearn for, to crave", "pos": "verb"},
            {"lemma": "la aspiración", "translation": "aspiration, ambition", "pos": "noun"},
            {"lemma": "eludir", "translation": "to avoid, to elude", "pos": "verb"},
            {"lemma": "procurar", "translation": "to try to, to ensure", "pos": "verb"},
            {"lemma": "la renuncia", "translation": "resignation, waiver", "pos": "noun"},
            {"lemma": "desistir", "translation": "to desist, to give up", "pos": "verb"},
            {"lemma": "el propósito", "translation": "purpose, resolution", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.04.04.infinitivo-vs-subjuntivo",
        "title": "Infinitivo frente a subjuntivo: Correferencia del sujeto",
        "sections": [
            {
                "type": "text",
                "title": "La regla de identidad de sujetos",
                "content": "Con verbos de voluntad, deseo, juicio y emoción, la norma culta del español exige el INFINITIVO cuando el sujeto del verbo principal coincide con el sujeto del verbo subordinado (correferencia). El SUBJUNTIVO solo se emplea cuando los sujetos son distintos (disjunción referencial)."
            },
            {
                "type": "table",
                "title": "Contraste de correferencia",
                "rows": [
                    ["Mismo sujeto -> INFINITIVO", "'El testigo pretende declarar ante el juez' (él pretende + él declara; NUNCA 'pretende que él declare')"],
                    ["Sujetos distintos -> SUBJUNTIVO", "'El abogado pretende que el testigo declare' (el abogado pretende + el testigo declara)"],
                    ["Con matrices impersonales genéricas", "'Conviene analizar los datos' (sentido general, sin sujeto específico) vs 'Conviene que el perito analice los datos' (sujeto explícito)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos normativos",
                "items": [
                    {"spanish": "Anhelamos alcanzar la paz en toda la región fronteriza.", "english": "We yearn to achieve peace across the entire border region."},
                    {"spanish": "Anhelamos que las futuras generaciones vivan sin violencia.", "english": "We yearn for future generations to live without violence."},
                    {"spanish": "Procuró eludir las preguntas comprometedoras de los periodistas.", "english": "He tried to avoid the compromising questions of the journalists."}
                ]
            },
            {
                "type": "tip",
                "content": "Evita el calco del inglés con 'que yo': en español no se dice 'Espero que yo apruebe', sino 'Espero aprobar'."
            }
        ]
    })

    write_json(f"exercises/b2/{l4}-ex.json", {
        "lesson": l4,
        "exercises": [
            {
                "id": f"{l4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["anhelar", "to yearn for, to crave"],
                    ["eludir", "to avoid, to elude"],
                    ["desistir", "to desist, to give up"],
                    ["la aspiración", "aspiration, ambition"]
                ],
                "teaches": ["b2-unit04-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes frases es correcta según la regla de correferencia de sujetos?",
                "options": [
                    "El candidato pretende asumir el cargo de forma transparente.",
                    "El candidato pretende que él asuma el cargo de forma transparente.",
                    "El candidato pretende que asumiría el cargo de forma transparente."
                ],
                "correct": 0,
                "teaches": ["infinitivo-vs-subjuntivo-correferencia"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los diplomáticos procuraron __ el conflicto armado mediante el diálogo directo. (evitar - same subject)",
                "answer": "evitar",
                "english": "The diplomats tried to avoid armed conflict through direct dialogue.",
                "teaches": ["infinitivo-vs-subjuntivo-correferencia"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Anhelan", "que", "la", "justicia", "prevalezca", "en", "el", "país."],
                "solution": ["Anhelan", "que", "la", "justicia", "prevalezca", "en", "el", "país."],
                "english": "They yearn for justice to prevail in the country.",
                "teaches": ["infinitivo-vs-subjuntivo-correferencia"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministra", "text": "¿Cuál es la pretensión última de su delegación en la cumbre?"},
                    {"speaker": "Embajador", "text": "_____"},
                    {"speaker": "Ministra", "text": "Es una aspiración compartida por toda la comunidad internacional."}
                ],
                "options": [
                    "Pretendemos consolidar un tratado vinculante que proteja la biodiversidad marina.",
                    "La sala de conferencias tiene capacidad para ochocientos representantes acreditados.",
                    "Los vuelos diplomáticos salieron ayer por la tarde desde Ginebra."
                ],
                "correct": 0,
                "teaches": ["infinitivo-vs-subjuntivo-correferencia"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Desistió de presentar la apelación porque comprendió la inutilidad de su empeño.",
                "english": "He gave up on presenting the appeal because he understood the futility of his endeavor.",
                "teaches": ["infinitivo-vs-subjuntivo-correferencia"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=4,
        title="Infinitive vs Subjunctive with Coreference",
        goal="Select accurately between the infinitive and subjunctive based on subject coreference and reference disjunction.",
        grammar_desc="el régimen de infinitivo frente al subjuntivo por correferencia del sujeto",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Apply the rule of subject coreference to avoid ungrammatical subjunctive calques.",
            "Contrast personal and impersonal uses with evaluative and volitive matrix verbs.",
            "Deploy vocabulary of desire, striving, and desistance (anhelar, eludir, desistir)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-04-05 - Recomendación diplomática y atenuación
    # --------------------------------------------------------------------------
    l5 = "b2-04-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.04.05",
        "lesson": l5,
        "title": "Diplomacia y formulación de recomendaciones",
        "theme": "Léxico de mediación, consenso y sugerencias formales",
        "words": [
            {"lemma": "sugerir", "translation": "to suggest", "pos": "verb"},
            {"lemma": "el dictamen", "translation": "formal opinion, ruling", "pos": "noun"},
            {"lemma": "el consenso", "translation": "consensus", "pos": "noun"},
            {"lemma": "aconsejable", "translation": "advisable", "pos": "adjective"},
            {"lemma": "la cautela", "translation": "caution, prudence", "pos": "noun"},
            {"lemma": "dirimir", "translation": "to settle, to resolve (a dispute)", "pos": "verb"},
            {"lemma": "la mediación", "translation": "mediation", "pos": "noun"},
            {"lemma": "la concordia", "translation": "harmony, concord", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.04.05.recomendacion-diplomatica",
        "title": "Fórmulas de recomendación institucional y diplomática",
        "sections": [
            {
                "type": "text",
                "title": "Atenuar el mandato en el plano internacional",
                "content": "En la redacción de dictámenes, resoluciones de organismos multilaterales y despachos diplomáticos B2, las órdenes no se formulan de manera imperativa directa. Se emplean estructuras de recomendación atenuada con pasiva refleja ('se sugiere que', 'se insta a que', 'se recomienda que') gobernando siempre modo subjuntivo."
            },
            {
                "type": "table",
                "title": "Fórmulas diplomáticas de recomendación",
                "rows": [
                    ["Se recomienda que + SUBJ", "'Se recomienda que las comisiones técnicas elaboren una hoja de ruta'"],
                    ["Se sugiere que + SUBJ", "'Se sugiere que el informe sea revisado por expertos independientes'"],
                    ["Sería aconsejable que + SUBJ IMPERF", "'Sería aconsejable que las delegaciones aplazaran la votación hasta alcanzar consenso'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el derecho internacional",
                "items": [
                    {"spanish": "El panel de expertos sugiere que se establezca una moratoria sobre la explotación minera.", "english": "The expert panel suggests that a moratorium on mining exploitation be established."},
                    {"spanish": "Sería conveniente que los signatarios ratificaran el protocolo antes de fin de año.", "english": "It would be advisable that signatories ratify the protocol before the end of the year."},
                    {"spanish": "Se insta a las partes involucradas a que diriman sus diferencias pacíficamente.", "english": "The involved parties are urged to settle their differences peacefully."}
                ]
            },
            {
                "type": "tip",
                "content": "Observa la concordancia de tiempos: con condicional en la matriz ('sería aconsejable que...'), la norma exige pretérito imperfecto de subjuntivo ('ratificaran', 'establecieran')."
            }
        ]
    })

    write_json(f"exercises/b2/{l5}-ex.json", {
        "lesson": l5,
        "exercises": [
            {
                "id": f"{l5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el dictamen", "formal ruling, legal opinion"],
                    ["dirimir", "to settle, to resolve (dispute)"],
                    ["la cautela", "caution, prudence"],
                    ["la concordia", "harmony, concord"]
                ],
                "teaches": ["b2-unit04-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué tiempo verbal exige 'Sería conveniente que' en una recomendación diplomática formal?",
                "options": [
                    "Pretérito imperfecto de subjuntivo (dialogaran), por correlación temporal con el condicional.",
                    "Presente de indicativo (dialogan), porque describe una reunión en curso.",
                    "Futuro simple (dialogarán), porque la reunión se celebrará el mes entrante."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Se sugiere que los delegados __ el texto final antes de someterlo a votación. (revisar)",
                "answer": "revisen",
                "english": "It is suggested that the delegates review the final text before submitting it to a vote.",
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "recomienda", "que", "actúen", "con", "la", "máxima", "cautela."],
                "solution": ["Se", "recomienda", "que", "actúen", "con", "la", "máxima", "cautela."],
                "english": "It is recommended that they act with utmost caution.",
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Embajadora", "text": "¿Cuál es la recomendación del mediador ante el estancamiento de las negociaciones de paz?"},
                    {"speaker": "Consejero", "text": "_____"},
                    {"speaker": "Embajadora", "text": "Es la única vía sensata para evitar una ruptura definitiva."}
                ],
                "options": [
                    "Sugiere que las delegaciones declaren una tregua temporal y establezcan mesas técnicas de trabajo.",
                    "El edificio de las Naciones Unidas en Nueva York fue inaugurado en octubre de 1952.",
                    "Los pasaportes diplomáticos se expiden con tapas de color negro o granate."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Sería aconsejable que ambas naciones dirimieran su diferendo limítrofe ante la corte de La Haya.",
                "english": "It would be advisable that both nations settle their border dispute before the court in The Hague.",
                "teaches": ["subjuntivo-influencia-mandato"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=4,
        title="Diplomatic Recommendations & Tactical Politeness",
        goal="Formulate high-register institutional recommendations and multilateral diplomatic proposals using attenuated subjunctive structures.",
        grammar_desc="estructuras atenuadas de recomendación diplomática e institucional",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Employ impersonal passive formulas (se sugiere que, se insta a que) in official communication.",
            "Maintain sequence of tenses between conditional matrices and imperfect subjunctive.",
            "Deploy diplomatic negotiation terminology (dirimir, dictamen, cautela, consenso)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Story: stories/classics/b2/b2-04.json (Carlos Fuentes: La muerte de Artemio Cruz)
    # --------------------------------------------------------------------------
    write_json("stories/classics/b2/b2-04.json", {
        "id": "story.b2.04.fuentes",
        "title": "Carlos Fuentes: Voluntad, poder y la agonía de Artemio Cruz",
        "level": "B2",
        "author": "Carlos Fuentes (México, 1928–2012)",
        "work": "La muerte de Artemio Cruz",
        "summary": "Una reflexión sobre la obra cumbre de Carlos Fuentes, donde la voluntad implacable de poder, las decisiones morales y la agonía en tres personas gramaticales desentrañan el destino del México contemporáneo.",
        "vocabularyTopics": ["Novela del Boom latinoamericano", "Poder y política", "Juicio ético póstumo"],
        "grammar": ["subjuntivo con verbos de voluntad", "matrices de juicio de valor"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Postrado en su lecho de agonía en la Ciudad de México, Artemio Cruz contempla los fragmentos dispersos de su existencia. Antiguo soldado de la Revolución mexicana transformado en magnate despiadado de los negocios y la prensa, su vida entera ha sido un ejercicio feroz de voluntad: imponer su ley sobre los demás, exigir que sus subordinados acataran cada designio y neutralizar cualquier atisbo de debilidad moral."
            },
            {
                "type": "narration",
                "text": "Fuentes estructura la novela mediante una audaz polifonía en tres personas gramaticales: el 'yo' presente y decrépito que sufre el deterioro corporal; el 'tú' profético en futuro que conjetura el destino de la memoria; y el 'él' omnisciente que narra en pasado los doce días cruciales en que Artemio tomó las decisiones que definieron su fortuna, desde los campos de batalla de Puebla hasta los lujosos despachos corporativos."
            },
            {
                "type": "narration",
                "text": "A través de esta arquitectura formal, la obra formula un severo juicio ético sobre la Revolución traicionada. Es insólito cómo la insurgencia popular que exigía tierra y libertad devino en una nueva oligarquía financiera. Al examinar el alma de Artemio Cruz, Fuentes exige que el lector se enfrente a los dilemas morales del poder y a la amarga lucidez de quien comprende que el éxito material conllevó la renuncia definitiva a su propia dignidad."
            }
        ]
    })

    # --------------------------------------------------------------------------
    # Lesson 6: b2-04-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-04-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["acatar", "to comply with, to abide by"],
                    ["inadmisible", "unacceptable"],
                    ["reconfortar", "to comfort, to hearten"],
                    ["eludir", "to avoid, to elude"]
                ],
                "teaches": ["b2-unit04-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según el texto sobre 'La muerte de Artemio Cruz', ¿qué técnica narrativa innovadora utiliza Carlos Fuentes para explorar la psicología del protagonista?",
                "options": [
                    "Una polifonía en tres personas gramaticales (yo, tú, él) que intercalan el presente de la agonía, el futuro profético y el pasado biográfico.",
                    "Un monólogo en verso alejandrino rimado de estilo barroco virreinal.",
                    "Una recopilación de cartas ficticias dirigidas a autoridades del imperio español."
                ],
                "correct": 0
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la frase 'Conviene que el parlamento apruebe la reforma tributaria sin demoras', ¿qué tipo de estructura gramatical se presenta?",
                "options": [
                    "Una matriz impersonal de juicio de conveniencia que rige modo subjuntivo en la subordinada.",
                    "Una oración condicional irreal que exige imperfecto de subjuntivo.",
                    "Una afirmación factual objetiva que debería redactarse en modo indicativo."
                ],
                "correct": 0,
                "teaches": ["juicios-valor-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A los ciudadanos les indigna que los gobernantes __ los reclamos de la comunidad. (desoír)",
                "answer": "desoigan",
                "english": "It outrages citizens that rulers turn a deaf ear to community grievances.",
                "teaches": ["reaccion-afectiva-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "La asamblea ciudadana exige que se transparenten las cuentas públicas. [The citizen assembly demands that public accounts be made transparent.]",
                    "Es inadmisible que las autoridades ignoren los dictámenes vinculantes de la corte. [It is inadmissible that authorities ignore the binding rulings of the court.]",
                    "A los defensores de derechos humanos les indigna que persista la impunidad. [It outrages human rights defenders that impunity persists.]",
                    "Se recomienda que ambas partes firmen un acuerdo de concordia cívica. [It is recommended that both parties sign a civic concord agreement.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["subjuntivo-influencia-mandato", "juicios-valor-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diputado", "text": "¿Cuál es la recomendación del comité de ética parlamentario?"},
                    {"speaker": "Presidente del comité", "text": "_____"},
                    {"speaker": "Diputado", "text": "Acataremos el dictamen en la sesión plenaria de mañana."}
                ],
                "options": [
                    "Se recomienda que el legislador involucrado sea suspendido de sus funciones hasta esclarecer los hechos.",
                    "El congreso nacional fue construido por ingenieros franceses en el siglo diecinueve.",
                    "Los diarios de debates se publican en papel membretado oficial."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-influencia-mandato"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Es indispensable que la fiscalía investigue a fondo para que no prevalezca la impunidad.",
                "english": "It is essential that the prosecution investigate thoroughly so that impunity does not prevail.",
                "teaches": ["juicios-valor-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Escribe una demanda institucional formal utilizando el verbo 'exigir que' con subjuntivo y el término 'acatar'.",
                        "answer": "La sociedad civil exige que las corporaciones acaten las normativas medioambientales vigentes."
                    }
                ],
                "teaches": ["subjuntivo-influencia-mandato"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=4,
        title="Unit 4 Consolidation",
        goal="Consolidate the subjunctive in noun clauses of influence, impersonal value judgments, affective stance, and coreference rules.",
        grammar_desc="síntesis de estructuras de voluntad, influencia y juicios axiológicos",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Formulate binding civic demands and multilateral recommendations.",
            "Govern the subjunctive after evaluative and emotional matrix verbs.",
            "Apply the coreference rule between infinitive and subjunctive accurately.",
            "Analyze literary excerpts from Carlos Fuentes' 'La muerte de Artemio Cruz'."
        ],
        checklist_items=[
            "I can use the subjunctive with verbs of influence, command, and urging (exigir, instar).",
            "I can formulate ethical critiques using impersonal matrices (es inadmisible que).",
            "I can express emotional outrage, empathy, and comfort using affective verbs.",
            "I can correctly select between the infinitive and subjunctive based on subject coreference."
        ],
        story_ref="stories/classics/b2/b2-04.json"
    ))
    print("Completed Core Unit 4 generation!")


if __name__ == "__main__":
    generate_core_unit_4()
