#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Core Unit 5:
  - Title: "Doubt, Denial & Epistemic Stance" (Duda, negación y posicionamiento epistémico)
  - Stems: b2-05-01 through b2-05-consolidation
  - Classic Literature Story: Octavio Paz - "El laberinto de la soledad: Las máscaras de la identidad mexicana"
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_core_unit_5():
    # Vocab theme slug: b2-unit05-vocab
    # Grammar skills:
    #   - creencia-negada-subjuntivo
    #   - duda-negacion-lexica
    #   - refutacion-no-es-que-sino
    #   - matizacion-epistemica-subjuntivo

    # --------------------------------------------------------------------------
    # Lesson 1: b2-05-01 - Negación de opiniones y creencias
    # --------------------------------------------------------------------------
    l1 = "b2-05-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.05.01",
        "lesson": l1,
        "title": "Pensamiento crítico y juicio intelectual",
        "theme": "Verbos de opinión, creencia y matrices cognitivas",
        "words": [
            {"lemma": "el postulado", "translation": "postulate, premise", "pos": "noun"},
            {"lemma": "concebir", "translation": "to conceive, to imagine", "pos": "verb"},
            {"lemma": "inverosímil", "translation": "unlikely, implausible", "pos": "adjective"},
            {"lemma": "la aseveración", "translation": "assertion, claim", "pos": "noun"},
            {"lemma": "disentir", "translation": "to dissent, to disagree", "pos": "verb"},
            {"lemma": "la certeza", "translation": "certainty", "pos": "noun"},
            {"lemma": "falaz", "translation": "fallacious, misleading", "pos": "adjective"},
            {"lemma": "vislumbrar", "translation": "to glimpse, to envision", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.05.01.creencia-negada",
        "title": "Subjuntivo tras matrices de opinión y creencia en forma negativa",
        "sections": [
            {
                "type": "text",
                "title": "Contraste afirmativo vs negativo en verbos de entendimiento",
                "content": "Los verbos de opinión, percepción mental y comunicación (creer, pensar, opinar, considerar, estimar, parecer) rigen indicativo cuando la cláusula principal es afirmativa, porque aseveran la realidad de la subordinada: 'Creo que la hipótesis es válida'. Sin embargo, al formularse en forma negativa, el hablante rechaza la aserción o suspende el compromiso con su veracidad, rigiendo obligatoriamente subjuntivo: 'No creo que la hipótesis sea válida'."
            },
            {
                "type": "table",
                "title": "Selección modal según la polaridad de la matriz",
                "rows": [
                    ["Matriz afirmativa -> INDICATIVO", "'Pienso que los datos confirman la teoría' / 'Consideramos que es un avance'"],
                    ["Matriz negativa -> SUBJUNTIVO", "'No pienso que los datos confirmen la teoría' / 'No consideramos que sea suficiente'"],
                    ["Interrogación negativa retórica -> INDICATIVO o SUBJUNTIVO", "'¿No crees que tiene / tenga razón?' (según si se presupone afirmación o duda)"],
                    ["Negación de mandato -> SUBJUNTIVO", "'No creas que sea tan sencillo' (exhortación a no albergar una falsa creencia)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo académico",
                "items": [
                    {"spanish": "No consideramos que las conclusiones del estudio reflejen fielmente la realidad socioeconómica.", "english": "We do not consider that the study's conclusions faithfully reflect socioeconomic reality."},
                    {"spanish": "Los analistas no opinan que la reforma tributaria resuelva el déficit a corto plazo.", "english": "Analysts do not believe that the tax reform will resolve the deficit in the short term."},
                    {"spanish": "No me parece que la evidencia presentada baste para refutar el postulado inicial.", "english": "It does not seem to me that the evidence presented is sufficient to refute the initial premise."}
                ]
            },
            {
                "type": "tip",
                "content": "Cuidado con 'no dudar que': como la negación de una duda equivale a una certeza afirmativa, rige indicativo: 'No dudo que tienes razón'."
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
                    ["el postulado", "postulate, premise"],
                    ["la aseveración", "assertion, claim"],
                    ["inverosímil", "unlikely, implausible"],
                    ["falaz", "fallacious, misleading"]
                ],
                "teaches": ["b2-unit05-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué se utiliza el subjuntivo en 'No creemos que esa teoría explique la complejidad del fenómeno'?",
                "options": [
                    "Porque la negación de la matriz de creencia ('no creemos') suspende la aserción de la proposición subordinada.",
                    "Porque 'explicar' es un verbo intransitivo que rechaza el indicativo.",
                    "Porque la oración expresa un mandato indirecto a los científicos."
                ],
                "correct": 0,
                "teaches": ["creencia-negada-subjuntivo"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La historiadora no opina que el cambio político __ de un día para otro. (ocurrir)",
                "answer": "ocurra",
                "english": "The historian does not believe that the political change happens overnight.",
                "teaches": ["creencia-negada-subjuntivo"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "consideramos", "que", "esa", "postura", "sea", "sostenible."],
                "solution": ["No", "consideramos", "que", "esa", "postura", "sea", "sostenible."],
                "english": "We do not consider that that position is tenable.",
                "teaches": ["creencia-negada-subjuntivo"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Profesor", "text": "¿Crees que la hipótesis del autor sobre el colapso social está suficientemente fundamentada?"},
                    {"speaker": "Estudiante de maestría", "text": "_____"},
                    {"speaker": "Profesor", "text": "Coincido plenamente; sus premisas se apoyan en una muestra demasiado reducida."}
                ],
                "options": [
                    "No me parece que los datos estadísticos respalden una afirmación tan categórica.",
                    "El informe preliminar tiene ochenta páginas y varios apéndices gráficos.",
                    "La biblioteca cierra sus puertas a las ocho de la noche los fines de semana."
                ],
                "correct": 0,
                "teaches": ["creencia-negada-subjuntivo"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "No pienso que la solución al diferendo dependa únicamente de voluntades individuales.",
                "english": "I do not think that the solution to the dispute depends solely on individual wills.",
                "teaches": ["creencia-negada-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=5,
        title="Negación de opiniones y creencias",
        goal="Express critical intellectual judgment and counter-arguments using the subjunctive after negated verbs of opinion and belief.",
        grammar_desc="el modo subjuntivo tras matrices de pensamiento, creencia y percepción en forma negativa",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Distinguish modal selection between affirmative (indicative) and negative (subjunctive) belief matrices.",
            "Deploy academic debate vocabulary (postulado, aseveración, disentir, falaz).",
            "Formulate nuanced philosophical and sociological counter-arguments."
        ],
        intro_body=[
            "Welcome to Unit 5 of Spanish B2 Core: Doubt, Denial & Epistemic Stance. At the B2 level, critical engagement requires learning how to distance oneself from propositions, dispute arguments, and calibrate certainty.",
            "In this first lesson, we explore the contrast between affirmative assertion and negated belief matrices ('creer', 'pensar', 'opinar', 'considerar'), mastering the subjunctive mechanics of intellectual critique."
        ],
        intro_title="Unit 5: Doubt, Denial & Epistemic Stance"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-05-02 - Verbos léxicos de duda, negación e incertidumbre
    # --------------------------------------------------------------------------
    l2 = "b2-05-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.05.02",
        "lesson": l2,
        "title": "Incertidumbre, refutación y escepticismo",
        "theme": "Verbos léxicos de duda, impugnación y desmentido",
        "words": [
            {"lemma": "dudar", "translation": "to doubt", "pos": "verb"},
            {"lemma": "desmentir", "translation": "to deny, to refute", "pos": "verb"},
            {"lemma": "cuestionar", "translation": "to question, to challenge", "pos": "verb"},
            {"lemma": "la incertidumbre", "translation": "uncertainty", "pos": "noun"},
            {"lemma": "sospechoso", "translation": "suspicious", "pos": "adjective"},
            {"lemma": "la impugnación", "translation": "challenge, contestation", "pos": "noun"},
            {"lemma": "el escepticismo", "translation": "skepticism", "pos": "noun"},
            {"lemma": "poner en tela de juicio", "translation": "to call into question", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.05.02.duda-negacion-lexica",
        "title": "Subjuntivo con verbos léxicos de duda, negación e impugnación",
        "sections": [
            {
                "type": "text",
                "title": "Verbos que codifican duda o falsedad de modo inherente",
                "content": "A diferencia de los verbos de creencia (que necesitan la partícula 'no' para inducir subjuntivo), los verbos que contienen duda o negación en su significado léxico intrínseco (dudar, negar, cuestionar, poner en duda, impugnar) rigen siempre subjuntivo en la proposición subordinada: 'Dudo que hayan actuado de buena fe', 'El portavoz negó que existieran irregularidades contables'."
            },
            {
                "type": "table",
                "title": "Duda afirmativa vs duda negada",
                "rows": [
                    ["dudar que + SUBJUNTIVO", "'Dudo que el tratado resuelva las tensiones limítrofes' (incertidumbre manifiesta)"],
                    ["negar que + SUBJUNTIVO", "'La cancillería niega que se hayan violado los protocolos internacionales'"],
                    ["no dudar que + INDICATIVO", "'No dudo que el equipo tiene capacidad técnica' (certeza indudable)"],
                    ["no negar que + INDICATIVO o SUBJUNTIVO", "'No niego que es difícil' (admisión de un hecho) frente a 'No niego que sea posible' (concesión cautelosa)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate sociopolítico",
                "items": [
                    {"spanish": "La comisión anticorrupción cuestiona que los contratos se adjudicaran con transparencia.", "english": "The anti-corruption commission questions whether the contracts were awarded transparently."},
                    {"spanish": "El presidente desmintió que su gabinete hubiera participado en las negociaciones secretas.", "english": "The president denied that his cabinet had participated in the secret negotiations."},
                    {"spanish": "Muchos juristas ponen en tela de juicio que la enmienda respete los principios constitucionales.", "english": "Many jurists call into question whether the amendment respects constitutional principles."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda la alternancia temporal: si la matriz está en presente ('dudo'), la subordinada va en presente de subjuntivo ('venga') o pretérito perfecto de subjuntivo ('haya venido'); si está en pasado ('dudaba'), rige imperfecto ('viniera') o pluscuamperfecto ('hubiera venido')."
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
                    ["desmentir", "to deny, to refute"],
                    ["cuestionar", "to question, to challenge"],
                    ["la incertidumbre", "uncertainty"],
                    ["el escepticismo", "skepticism"]
                ],
                "teaches": ["b2-unit05-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo exige la subordinada en 'El director niega que la empresa _____ en prácticas desleales'?",
                "options": [
                    "Subjuntivo (haya incurrido), porque 'negar' es un verbo léxico de falsedad que induce subjuntivo.",
                    "Indicativo (ha incurrido), porque el director es la máxima autoridad corporativa.",
                    "Condicional (habría incurrido), porque es un rumor periodístico."
                ],
                "correct": 0,
                "teaches": ["duda-negacion-lexica"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los peritos dudan que el incendio __ accidental. (ser)",
                "answer": "sea",
                "english": "The experts doubt that the fire is accidental.",
                "teaches": ["duda-negacion-lexica"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Dudamos", "que", "hayan", "actuado", "con", "total", "transparencia."],
                "solution": ["Dudamos", "que", "hayan", "actuado", "con", "total", "transparencia."],
                "english": "We doubt that they have acted with total transparency.",
                "teaches": ["duda-negacion-lexica"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Qué declaró el ministro respecto a las acusaciones de malversación?"},
                    {"speaker": "Portavoz de prensa", "text": "_____"},
                    {"speaker": "Periodista", "text": "Sin embargo, el tribunal de cuentas abrirá una auditoría formal."}
                ],
                "options": [
                    "Negó rotundamente que se hubieran desviado fondos públicos asignados al programa de salud.",
                    "Los edificios coloniales del centro histórico tienen fachadas de cantera gris.",
                    "El precio del transporte público aumentó a principios del mes pasado."
                ],
                "correct": 0,
                "teaches": ["duda-negacion-lexica"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Ponemos en duda que los nuevos gravámenes arancelarios fomenten la competitividad nacional.",
                "english": "We call into question whether the new tariff duties encourage national competitiveness.",
                "teaches": ["duda-negacion-lexica"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=5,
        title="Verbos léxicos de duda, negación e incertidumbre",
        goal="Deploy lexical verbs of doubt, denial, and contestation (dudar, negar, cuestionar) with required subjunctive complements.",
        grammar_desc="el régimen de subjuntivo con verbos inherentemente negativos o dubitativos",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Identify verbs that inherently code epistemic doubt and negation.",
            "Contrast 'dudar que' (subjunctive) with 'no dudar que' (indicative).",
            "Articulate rigorous scholarly skepticism in institutional discourse."
        ],
        intro_body=[
            "In this second lesson, we explore verbs whose very meaning embodies doubt, contestation, or denial: 'dudar', 'negar', 'cuestionar', and 'desmentir'.",
            "We analyze why these verbs inherently induce the subjunctive, and practice the crucial pragmatic contrast between affirmative doubt and negated doubt ('no dudar que' + indicativo)."
        ],
        intro_title="Lexical Verbs of Doubt & Negation"
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-05-03 - Refutación discursiva: No es que... sino que...
    # --------------------------------------------------------------------------
    l3 = "b2-05-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.05.03",
        "lesson": l3,
        "title": "Argumentación y rectificación",
        "theme": "Estructuras contrastivas de refutación y aclaración conceptual",
        "words": [
            {"lemma": "rectificar", "translation": "to rectify, to correct", "pos": "verb"},
            {"lemma": "la salvedad", "translation": "caveat, exception", "pos": "noun"},
            {"lemma": "el matiz", "translation": "nuance, shade of meaning", "pos": "noun"},
            {"lemma": "tergiversar", "translation": "to distort, to misrepresent", "pos": "verb"},
            {"lemma": "la objeción", "translation": "objection", "pos": "noun"},
            {"lemma": "esclarecer", "translation": "to clarify, to shed light on", "pos": "verb"},
            {"lemma": "inadmisible", "translation": "inadmissible, unacceptable", "pos": "adjective"},
            {"lemma": "rebatir", "translation": "to refute, to rebut", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.05.03.refutacion-no-es-que-sino",
        "title": "Estructuras de refutación discursiva con 'no es que' + subjuntivo",
        "sections": [
            {
                "type": "text",
                "title": "Mecanismo retórico de aclaración y rectificación",
                "content": "La fórmula 'no es que + subjuntivo, sino (que) + indicativo' es una de las construcciones argumentativas más elegantes del español formal. Se utiliza para desestimar una falsa interpretación o premisa errónea en la primera parte (marcada con subjuntivo porque se niega su pertinencia o adecuación explicativa) y sustituirla inmediatamente por la verdadera causa o explicación (marcada con indicativo porque se asevera como un hecho real): 'No es que rechacemos la propuesta, sino que carecemos de presupuesto'."
            },
            {
                "type": "table",
                "title": "Esquema sintáctico de la rectificación",
                "rows": [
                    ["Segmento refutado (SUBJUNTIVO)", "'No es que queramos imponer restricciones...' (rechaza el motivo aparente)"],
                    ["Segmento correctivo (INDICATIVO)", "'...sino que debemos velar por la seguridad' (afirma el motivo real)"],
                    ["Variante de pasado", "'No era que ignorara la ley, sino que decidió actuar por necesidad'"],
                    ["Con adjetivos evaluativos", "'No es que sea imposible, sino que exige una inversión considerable'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el discurso formal",
                "items": [
                    {"spanish": "No es que desconfiemos de sus capacidades, sino que el protocolo exige una certificación oficial.", "english": "It is not that we distrust your capabilities, but rather that the protocol requires an official certification."},
                    {"spanish": "No es que la ciudadanía sea apática, sino que las instituciones tradicionales han perdido credibilidad.", "english": "It is not that the citizenry is apathetic, but rather that traditional institutions have lost credibility."},
                    {"spanish": "No era que faltaran recursos naturales, sino que la distribución de la tierra era profundamente desigual.", "english": "It was not that natural resources were lacking, but rather that land distribution was profoundly unequal."}
                ]
            },
            {
                "type": "tip",
                "content": "¡Recuerda!: En el segundo término, 'sino que' introduce una oración con verbo conjugado ('sino que tenemos...'), mientras que 'sino' a secas introduce un sintagma nominal o adjetival ('no era blanco, sino gris')."
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
                    ["rectificar", "to rectify, to correct"],
                    ["la salvedad", "caveat, exception"],
                    ["tergiversar", "to distort, to misrepresent"],
                    ["rebatir", "to refute, to rebut"]
                ],
                "teaches": ["b2-unit05-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la estructura 'No es que no queramos cooperar, sino que nos faltan garantías jurídicas' combina subjuntivo e indicativo?",
                "options": [
                    "Porque la primera cláusula descarta una falsa motivación (en subjuntivo) y la segunda asevera la causa real (en indicativo).",
                    "Porque 'querer' siempre rige subjuntivo y 'faltar' siempre rige indicativo.",
                    "Porque se trata de una oración condicional mixta de pasado y presente."
                ],
                "correct": 0,
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No es que la propuesta __ deficiente, sino que los plazos de ejecución son demasiado ajustados. (ser)",
                "answer": "sea",
                "english": "It is not that the proposal is deficient, but rather that implementation deadlines are too tight.",
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "es", "que", "ignoremos", "el", "problema,", "sino", "que", "faltan", "fondos."],
                "solution": ["No", "es", "que", "ignoremos", "el", "problema,", "sino", "que", "faltan", "fondos."],
                "english": "It is not that we ignore the problem, but rather that funds are lacking.",
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Auditor", "text": "¿Por qué el comité directivo rechazó el plan de digitalización presentado por el departamento técnico?"},
                    {"speaker": "Vocal del comité", "text": "_____"},
                    {"speaker": "Auditor", "text": "Entiendo, entonces reformularán los términos del cronograma."}
                ],
                "options": [
                    "No es que consideremos innecesaria la modernización, sino que la propuesta financiera compromete la liquidez a corto plazo.",
                    "Las instalaciones del archivo central fueron remodeladas durante el verano pasado.",
                    "Los servidores informáticos consumen abundante energía durante las noches."
                ],
                "correct": 0,
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "No es que nos opongamos a la reforma tributaria, sino que demandamos mayor equidad distributiva.",
                "english": "It is not that we oppose the tax reform, but rather that we demand greater distributive equity.",
                "teaches": ["refutacion-no-es-que-sino"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=5,
        title="Refutación discursiva: No es que... sino que...",
        goal="Master discursive rectification and nuanced refutation using the paired formula 'no es que' + subjunctive followed by 'sino que' + indicative.",
        grammar_desc="la correlación modal en construcciones rectificativas de negación y contraafirmación",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Deconstruct erroneous assumptions using 'no es que' + subjunctive.",
            "Assert true motivations with 'sino que' + indicative.",
            "Apply high-register vocabulary of clarification (matiz, salvedad, rebatir, rectificar)."
        ],
        intro_body=[
            "One of the most powerful rhetorical devices in sophisticated argument is the clarification formula: 'no es que... sino que...'.",
            "In this lesson, we study how to dismiss misunderstandings in the subjunctive while establishing empirical reality in the indicative, sharpening our persuasive edge."
        ],
        intro_title="Discursive Refutation & Rectification"
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-05-04 - Moduladores epistémicos de posibilidad y probabilidad
    # --------------------------------------------------------------------------
    l4 = "b2-05-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.05.04",
        "lesson": l4,
        "title": "Conjetura y ponderación de hipótesis",
        "theme": "Adverbios de duda, matrices de probabilidad y grados de certeza",
        "words": [
            {"lemma": "acaso", "translation": "perhaps, maybe", "pos": "adverb"},
            {"lemma": "la plausibilidad", "translation": "plausibility", "pos": "noun"},
            {"lemma": "conjeturar", "translation": "to conjecture, to surmise", "pos": "verb"},
            {"lemma": "presunto", "translation": "presumed, alleged", "pos": "adjective"},
            {"lemma": "la verosimilitud", "translation": "verisimilitude, credibility", "pos": "noun"},
            {"lemma": "factible", "translation": "feasible, workable", "pos": "adjective"},
            {"lemma": "la probabilidad", "translation": "probability, likelihood", "pos": "noun"},
            {"lemma": "el indicio", "translation": "indication, clue, hint", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.05.04.matizacion-epistemica",
        "title": "Moduladores epistémicos de probabilidad: puede que, es probable que, quizá y tal vez",
        "sections": [
            {
                "type": "text",
                "title": "Gradación de la certeza y alternancia modal",
                "content": "En el registro formal B2, modular el grado de adhesión a una afirmación evita juicios dogmáticos. Las expresiones impersonales 'puede que', 'es probable que' y 'es posible que' rigen siempre subjuntivo: 'Puede que las negociaciones concluyan la próxima semana'. Por otra parte, los adverbios de duda ('quizá / quizás', 'tal vez', 'acaso') admiten alternancia: si anteceden al verbo, seleccionan subjuntivo para denotar mayor incertidumbre, o indicativo para sugerir mayor probabilidad factual. Si van pospuestos al verbo, exigen obligatoriamente indicativo: 'Vendrá mañana, tal vez'."
            },
            {
                "type": "table",
                "title": "Matices y reglas modales con moduladores de probabilidad",
                "rows": [
                    ["puede que / es probable que / es posible que + SUBJUNTIVO (invariable)", "'Es probable que el parlamento apruebe la moción'"],
                    ["quizás / tal vez + SUBJUNTIVO (mayor incertidumbre o hipótesis)", "'Quizás logren un acuerdo de paz duradero'"],
                    ["quizás / tal vez + INDICATIVO (mayor inclinación a la verdad del hecho)", "'Tal vez tienen razones de peso para postergar el viaje'"],
                    ["a lo mejor / igual / lo mismo + INDICATIVO (registro coloquial / general)", "'A lo mejor llega tarde' (nunca lleva subjuntivo)"],
                    ["adverbio pospuesto al verbo -> INDICATIVO obligatorio", "'Llegarán a tiempo, tal vez' (nunca '*Lleguen a tiempo, tal vez')"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el análisis geopolítico y social",
                "items": [
                    {"spanish": "Puede que el incremento en las tasas de interés desacelere el crecimiento de las inversiones.", "english": "It may be that the rise in interest rates slows down investment growth."},
                    {"spanish": "Es factible que las dos delegaciones alcancen un entendimiento en materia migratoria.", "english": "It is feasible that the two delegations reach an understanding on migration matters."},
                    {"spanish": "Tal vez existan indicios suficientes para reabrir la investigación penal.", "english": "Perhaps there are sufficient indications to reopen the criminal investigation."}
                ]
            },
            {
                "type": "tip",
                "content": "'A lo mejor' es un falso amigo sintáctico: a pesar de expresar probabilidad como 'quizás', en español rige SIEMPRE modo indicativo."
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
                    ["la plausibilidad", "plausibility"],
                    ["conjeturar", "to conjecture, to surmise"],
                    ["la verosimilitud", "verisimilitude, credibility"],
                    ["factible", "feasible, workable"]
                ],
                "teaches": ["b2-unit05-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo exige de forma obligatoria la expresión impersonal 'puede que'?",
                "options": [
                    "Modo subjuntivo, porque denota posibilidad e indeterminación sobre la factualidad del evento.",
                    "Modo indicativo, siempre que el hecho esté ocurriendo en el presente.",
                    "Modo infinitivo, porque carece de concordancia de persona."
                ],
                "correct": 0,
                "teaches": ["matizacion-epistemica-subjuntivo"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Es muy probable que los delegados __ el memorando de entendimiento mañana. (firmar)",
                "answer": "firmen",
                "english": "It is very likely that the delegates will sign the memorandum of understanding tomorrow.",
                "teaches": ["matizacion-epistemica-subjuntivo"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Puede", "que", "hayan", "encontrado", "nuevos", "indicios", "del", "caso."],
                "solution": ["Puede", "que", "hayan", "encontrado", "nuevos", "indicios", "del", "caso."],
                "english": "It may be that they have found new clues about the case.",
                "teaches": ["matizacion-epistemica-subjuntivo"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diplomático", "text": "¿Cree que la cumbre multilateral concluya con un tratado vinculante sobre emisiones?"},
                    {"speaker": "Analista ambiental", "text": "_____"},
                    {"speaker": "Diplomático", "text": "En efecto, los intereses económicos de las potencias son divergentes."}
                ],
                "options": [
                    "Puede que firmen una declaración de intenciones, pero es poco probable que adopten metas legalmente obligatorias.",
                    "El palacio de convenciones fue renovado por el ministerio de obras públicas.",
                    "Las credenciales de acceso se entregan en el mostrador del vestíbulo."
                ],
                "correct": 0,
                "teaches": ["matizacion-epistemica-subjuntivo"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Quizás convenga postergar la votación definitiva hasta que se disipen todas las dudas jurídicas.",
                "english": "Perhaps it is advisable to postpone the final vote until all legal doubts are dispelled.",
                "teaches": ["matizacion-epistemica-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=5,
        title="Moduladores epistémicos de posibilidad y probabilidad",
        goal="Calibrate degrees of certainty, conjecture, and likelihood using epistemic markers like 'puede que', 'es probable que', and 'quizás'.",
        grammar_desc="moduladores de probabilidad y alternancia modal con adverbios de duda",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Master invariable subjunctive triggers of possibility ('puede que', 'es probable que').",
            "Understand modal nuance between indicative and subjunctive after 'tal vez' and 'quizás'.",
            "Express cautious scholarly and diplomatic hypotheses."
        ],
        intro_body=[
            "Intellectual maturity requires knowing how to frame hypotheses without claiming unearned certainty.",
            "In this lesson, we study epistemic modifiers: from categorical subjunctive triggers ('puede que', 'es probable que') to versatile modal adverbs ('quizás', 'tal vez')."
        ],
        intro_title="Epistemic Modulators of Probability"
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-05-05 - Escepticismo diplomático, debate intelectual y dialéctica
    # --------------------------------------------------------------------------
    l5 = "b2-05-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.05.05",
        "lesson": l5,
        "title": "Dialéctica, controversia y escepticismo",
        "theme": "Debate intelectual, contraste de hipótesis y diplomacia",
        "words": [
            {"lemma": "la discrepancia", "translation": "discrepancy, divergence", "pos": "noun"},
            {"lemma": "controvertido", "translation": "controversial, disputed", "pos": "adjective"},
            {"lemma": "zanjar", "translation": "to settle, to resolve", "pos": "verb"},
            {"lemma": "el diferendo", "translation": "dispute, disagreement", "pos": "noun"},
            {"lemma": "sesgado", "translation": "biased, slanted", "pos": "adjective"},
            {"lemma": "la reticencia", "translation": "reluctance, reticence", "pos": "noun"},
            {"lemma": "esgrimir", "translation": "to wield (an argument), to put forward", "pos": "verb"},
            {"lemma": "categórico", "translation": "categorical, definitive", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.05.05.escepticismo-dialectico",
        "title": "Integración discursiva: Escepticismo, rectificación y atenuación en el debate intelectual",
        "sections": [
            {
                "type": "text",
                "title": "Síntesis de posicionamiento epistémico",
                "content": "El debate intelectual y la diplomacia de nivel B2 exigen articular objeciones sin agresividad. Esto se logra combinando matrices de opinión negada ('no estimamos que...'), aclaraciones rectificativas ('no es que desconozcamos X, sino que advertimos Y') y moduladores de probabilidad ('puede que existan alternativas'). Esta constelación modal permite desarmar argumentos falaces manteniendo el rigor académico y la cortesía discursiva."
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo argumentativo",
                "items": [
                    {"spanish": "No consideramos que el informe sea concluyente, y dudamos que los datos hayan sido recopilados sin sesgos.", "english": "We do not consider that the report is conclusive, and we doubt that data was collected without bias."},
                    {"spanish": "No es que pretendamos zanjar la controversia unilateralmente, sino que esgrimimos salvaguardas legítimas.", "english": "It is not that we seek to settle the controversy unilaterally, but rather that we wield legitimate safeguards."},
                    {"spanish": "Puede que ambas partes muestren reticencia a ceder, pero es factible que alcancen un consenso pragmático.", "english": "Both parties may show reluctance to yield, but it is feasible that they reach a pragmatic consensus."}
                ]
            },
            {
                "type": "tip",
                "content": "Para atenuar una crítica contundente, utiliza el condicional en la matriz: 'No me atrevería a decir que sea un error total, pero...' o 'Sería dudoso que tal premisa se sostuviera'."
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
                    ["la discrepancia", "discrepancy, divergence"],
                    ["zanjar", "to settle, to resolve"],
                    ["sesgado", "biased, slanted"],
                    ["esgrimir", "to put forward, to wield an argument"]
                ],
                "teaches": ["b2-unit05-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué opción integra con mayor precisión la duda y la rectificación formal?",
                "options": [
                    "Dudamos que el plan sea viable; no es que rechacemos la idea, sino que carecemos de recursos técnicos.",
                    "Dudamos que el plan es viable; no es que rechazamos la idea, sino que carezcamos de recursos.",
                    "No dudamos que el plan sea viable; no es que rechazamos la idea, sino que carecemos de recursos."
                ],
                "correct": 0,
                "teaches": ["duda-negacion-lexica"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La delegación no considera que el mediador internacional __ parcializado en sus apreciaciones. (estar)",
                "answer": "esté",
                "english": "The delegation does not consider that the international mediator is biased in his appraisals.",
                "teaches": ["creencia-negada-subjuntivo"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "es", "que", "desestimemos", "su", "tesis,", "sino", "que", "exige", "matices."],
                "solution": ["No", "es", "que", "desestimemos", "su", "tesis,", "sino", "que", "exige", "matices."],
                "english": "It is not that we dismiss your thesis, but rather that it demands nuances.",
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Moderadora", "text": "¿Cómo responde la comisión evaluadora ante las objeciones presentadas por los investigadores discrepantes?"},
                    {"speaker": "Presidente de la mesa", "text": "_____"},
                    {"speaker": "Moderadora", "text": "Una aclaración muy oportuna para continuar el diálogo constructivo."}
                ],
                "options": [
                    "No es que pretendamos silenciar las discrepancias metodológicas, sino que debemos ceñirnos a los estándares verificables del protocolo.",
                    "La sala de conferencias dispone de proyectores digitales y traducción simultánea.",
                    "Los ponentes recibieron un certificado de asistencia al término de las jornadas académicas."
                ],
                "correct": 0,
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Puede que existan interpretaciones divergentes, pero nadie niega que los resultados ameritan un debate profundo.",
                "english": "There may be divergent interpretations, but nobody denies that the results merit a profound debate.",
                "teaches": ["matizacion-epistemica-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=5,
        title="Escepticismo diplomático, debate intelectual y dialéctica",
        goal="Synthesize epistemic stance, negation of belief, lexical doubt, and discursive refutation in high-register intellectual debates.",
        grammar_desc="integración de posicionamiento epistémico, duda razonada y rectificación retórica",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Formulate courteous intellectual objections without dogmatic assertion.",
            "Combine 'no es que' + subjunctive with 'sino que' + indicative in academic debates.",
            "Deploy lexical diplomacy verbs (zanjar, disentir, esgrimir, sesgado)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Story: stories/classics/b2/b2-05.json (Octavio Paz: El laberinto de la soledad)
    # --------------------------------------------------------------------------
    write_json("stories/classics/b2/b2-05.json", {
        "id": "story.b2.05.paz",
        "title": "Octavio Paz: Las máscaras de la soledad y la dialéctica del ser",
        "level": "B2",
        "author": "Octavio Paz (México, 1914–1998, Premio Nobel 1990)",
        "work": "El laberinto de la soledad",
        "summary": "Una meditación sobre la obra cumbre del ensayo latinoamericano: las máscaras defensivas del mexicano, la hermeticidad psicológica frente a la otredad y la fiesta como catarsis de comunión colectiva.",
        "vocabularyTopics": ["Ensayo filosófico", "Identidad y ontología", "Dialéctica de la máscara"],
        "grammar": ["subjuntivo tras opinión negada", "refutación discursiva no es que sino que", "verbos de duda y cuestionamiento"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En 'El laberinto de la soledad' (1950), Octavio Paz emprende una de las indagaciones ontológicas más hondas de la literatura en lengua española. El poeta y ensayista mexicano no pretende que su texto sea un tratado sociológico cuantitativo, sino una reflexión fenomenológica sobre los pliegues íntimos de la psicología nacional y la herida histórica del mestizaje."
            },
            {
                "type": "narration",
                "text": "Paz describe al mexicano como un ser hermético que se encierra en sí mismo para proteger su vulnerabilidad. De ahí surge la máscara: la cortesía ceremonial, el disimulo y el pudor ante la mirada extraña. No es que el individuo carezca de pasiones o de una afectividad ardiente, sino que teme que abrirse a los demás implique una claudicación o una entrega destructiva frente al mundo exterior."
            },
            {
                "type": "narration",
                "text": "Esta cerrazón cotidiana encuentra su única transgresión en la fiesta y en la rebelión. Durante el festejo, los límites estallan: el mexicano se desgarra la máscara, canta, maldice y comulga temporalmente con la totalidad. Sin embargo, pasada la embriaguez sagrada, el regreso a la soledad es inevitable. Paz concluye que la soledad no es una condena privativa de México, sino la condición existencial más profunda del ser humano que busca reconciliarse con la historia y con el otro."
            }
        ]
    })

    # --------------------------------------------------------------------------
    # Lesson 6: b2-05-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-05-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el postulado", "postulate, premise"],
                    ["desmentir", "to refute, to deny"],
                    ["la salvedad", "caveat, exception"],
                    ["la verosimilitud", "verisimilitude, credibility"]
                ],
                "teaches": ["b2-unit05-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿En cuál de las siguientes frases se selecciona el modo indicativo en lugar del subjuntivo?",
                "options": [
                    "No dudo que los resultados tienen una base empírica incuestionable.",
                    "No creo que los resultados tengan una base empírica incuestionable.",
                    "Dudo que los resultados tengan una base empírica incuestionable."
                ],
                "correct": 0,
                "teaches": ["duda-negacion-lexica"]
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la función sintáctica y pragmática de la fórmula 'no es que... sino que...'?",
                "options": [
                    "Rectificar una premisa errónea en subjuntivo y aseverar la explicación verdadera en indicativo.",
                    "Expresar una hipótesis irreal sobre el pasado con pluscuamperfecto.",
                    "Introducir una orden atenuada con pronombres enclíticos."
                ],
                "correct": 0,
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Puede que el tribunal __ conveniente escuchar a nuevos testigos antes del veredicto. (considerar)",
                "answer": "considere",
                "english": "It may be that the court considers it advisable to hear new witnesses before the verdict.",
                "teaches": ["matizacion-epistemica-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "No consideramos que la tesis del autor refleje con exactitud la complejidad histórica. [We do not consider that the author's thesis accurately reflects historical complexity.]",
                    "Los expertos dudan que la política monetaria resuelva la inflación sin causar recesión. [Experts doubt that monetary policy resolves inflation without causing recession.]",
                    "No es que los ciudadanos rechacen las normas, sino que exigen instituciones probas. [It is not that citizens reject rules, but rather that they demand honest institutions.]",
                    "Es factible que la cumbre multilateral concluya con un compromiso vinculante. [It is feasible that the multilateral summit concludes with a binding commitment.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["creencia-negada-subjuntivo", "duda-negacion-lexica", "refutacion-no-es-que-sino", "matizacion-epistemica-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítico literario", "text": "¿Por qué afirma Octavio Paz que la máscara del mexicano no es un signo de falsedad moral?"},
                    {"speaker": "Ensayista", "text": "_____"},
                    {"speaker": "Crítico literario", "text": "Exacto: la máscara es una defensa frente a la herida de la historia."}
                ],
                "options": [
                    "Porque no es que el mexicano carezca de sinceridad, sino que utiliza el pudor y la reserva como escudo para preservar su intimidad.",
                    "Porque en las pirámides prehispánicas se colocaban mascarones de jade en las tumbas.",
                    "Porque las fiestas populares se financian mediante cooperaciones vecinales voluntarias."
                ],
                "correct": 0,
                "teaches": ["refutacion-no-es-que-sino"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "No pensamos que la controversia deba zanjarse sin escuchar a todas las voces implicadas.",
                "english": "We do not think that the controversy should be settled without listening to all implicated voices.",
                "teaches": ["creencia-negada-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Escribe una refutación académica utilizando la fórmula 'No es que [subjuntivo], sino que [indicativo]'.",
                        "answer": "No es que desestimemos los hallazgos empíricos, sino que consideramos necesaria una mayor fundamentación estadística."
                    }
                ],
                "teaches": ["refutacion-no-es-que-sino"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=5,
        title="Unit 5 Consolidation",
        goal="Consolidate epistemic positioning, negation of belief matrices, lexical doubt, rectificative refutation, and probability modulators.",
        grammar_desc="síntesis de estructuras de duda, negación, refutación retórica y matización epistémica",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Deploy the subjunctive after negated opinion and perception verbs.",
            "Distinguish affirmative doubt (subjunctive) from negated doubt (indicative).",
            "Construct elegant discursive refutations with 'no es que... sino que...'.",
            "Analyze philosophical essays from Octavio Paz's 'El laberinto de la soledad'."
        ],
        checklist_items=[
            "I can govern the subjunctive after negated belief verbs (no creo, no opino que).",
            "I can use lexical doubt verbs (dudar, negar, cuestionar) with proper modal selection.",
            "I can construct nuanced refutations using 'no es que' + subjunctive and 'sino que' + indicative.",
            "I can calibrate degrees of possibility using 'puede que', 'es probable que', and 'quizás'."
        ],
        story_ref="stories/classics/b2/b2-05.json"
    ))
    print("Completed Core Unit 5 generation!")


if __name__ == "__main__":
    generate_core_unit_5()
