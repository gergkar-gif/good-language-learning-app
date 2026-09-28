#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Core Unit 3:
  - Title: "Hypothesizing & Probability" (Hipótesis y grados de probabilidad)
  - Stems: b2-03-01 through b2-03-consolidation
  - Classic Literature Story: Gabriel García Márquez - "Crónica de una muerte anunciada: Memoria, fatalidad y conjetura"
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_core_unit_3():
    # Vocab theme slug: b2-unit03-vocab
    # Grammar skills:
    #   - probabilidad-indicativo-subjuntivo
    #   - matrices-impersonales-probabilidad
    #   - futuro-conjetura-presente-pasado
    #   - condicional-conjetura-pasado

    # --------------------------------------------------------------------------
    # Lesson 1: b2-03-01 - Marcadores de probabilidad e indicativo/subjuntivo
    # --------------------------------------------------------------------------
    l1 = "b2-03-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.03.01",
        "lesson": l1,
        "title": "Incertidumbre, certeza y especulación",
        "theme": "Hipótesis, grados de probabilidad y conjetura",
        "words": [
            {"lemma": "la hipótesis", "translation": "hypothesis", "pos": "noun"},
            {"lemma": "la certeza", "translation": "certainty", "pos": "noun"},
            {"lemma": "la conjetura", "translation": "conjecture, guess", "pos": "noun"},
            {"lemma": "plausible", "translation": "plausible", "pos": "adjective"},
            {"lemma": "inverosímil", "translation": "improbable, unbelievable", "pos": "adjective"},
            {"lemma": "indagar", "translation": "to investigate, to probe", "pos": "verb"},
            {"lemma": "el indicio", "translation": "clue, sign, indication", "pos": "noun"},
            {"lemma": "corroborar", "translation": "to corroborate, to confirm", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.03.01.probabilidad-marcadores",
        "title": "Marcadores de probabilidad y selección de modo",
        "sections": [
            {
                "type": "text",
                "title": "La graduación epistémica",
                "content": "En el nivel B2, expresar probabilidad no se limita a usar 'tal vez'. El hablante competente modula el grado de compromiso con la verdad seleccionando entre indicativo (mayor certeza o hecho verosímil) y subjuntivo (duda, escepticismo o menor probabilidad)."
            },
            {
                "type": "table",
                "title": "Marcadores y régimen modal",
                "rows": [
                    ["A lo mejor / Igual / Lo mismo", "Rigen SIEMPRE indicativo en todas las variedades: 'A lo mejor viene mañana' (nunca subjuntivo)"],
                    ["Quizás / Tal vez / Acaso", "Antepuestos admiten indicativo (compromiso alto) o subjuntivo (compromiso bajo): 'Quizás llega hoy' vs 'Quizás llegue hoy'"],
                    ["Posposición de marcadores", "Si van pospuestos al verbo, exigen obligatoriamente indicativo: 'Vendrá mañana, tal vez', 'Lo sabe, quizás'"],
                    ["Por ahí / Capaz que (América Latina)", "'Capaz que' rige subjuntivo en el Cono Sur y Andes: 'Capaz que no venga'; 'Por ahí' rige indicativo: 'Por ahí se le olvidó'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos contrastivos",
                "items": [
                    {"spanish": "A lo mejor encontramos una solución antes del fin de semana.", "english": "Maybe we will find a solution before the weekend."},
                    {"spanish": "Quizás tengan razón los auditores en sus observaciones preliminares.", "english": "Perhaps the auditors are right in their preliminary observations."},
                    {"spanish": "El testigo cambió su versión; sospechaba algo, tal vez.", "english": "The witness changed his version; he suspected something, perhaps."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda la regla de oro: jamás uses subjuntivo con 'a lo mejor'. Decir 'A lo mejor tengamos' es un error agramatical grave en cualquier examen de certificación B2."
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
                    ["la conjetura", "conjecture, guess"],
                    ["plausible", "plausible"],
                    ["inverosímil", "improbable, unbelievable"],
                    ["corroborar", "to corroborate, to confirm"]
                ],
                "teaches": ["b2-unit03-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones es gramaticalmente correcta según las reglas modales del español culto?",
                "options": [
                    "A lo mejor el embajador llega a tiempo para la ceremonia de apertura.",
                    "A lo mejor el embajador llegue a tiempo para la ceremonia de apertura.",
                    "A lo mejor el embajador llegara a tiempo para la ceremonia de apertura."
                ],
                "correct": 0,
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Tal vez el comité consultivo __ conveniente revisar el protocolo de seguridad. (considerar - subjunctive)",
                "answer": "considere",
                "english": "Perhaps the advisory committee considers it convenient to review the safety protocol.",
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "lo", "mejor", "ya", "descubrieron", "el", "motivo."],
                "solution": ["A", "lo", "mejor", "ya", "descubrieron", "el", "motivo."],
                "english": "Maybe they already discovered the motive.",
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Fiscal", "text": "¿Qué tan verosímil considera la coartada presentada por el acusado?"},
                    {"speaker": "Perito", "text": "_____"},
                    {"speaker": "Fiscal", "text": "En ese caso, debemos recabar testimonios adicionales."}
                ],
                "options": [
                    "Quizás haya elementos ciertos, pero la cronología de los hechos resulta inverosímil.",
                    "El código penal fue promulgado hace más de cincuenta años en la república.",
                    "Ayer compramos varias carpetas de archivo en la papelería central."
                ],
                "correct": 0,
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "A lo mejor los peritos encuentran nuevos indicios que permitan esclarecer el enigma.",
                "english": "Maybe the forensics experts will find new clues that allow clearing up the enigma.",
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=3,
        title="Probability Markers & Mood Alternation",
        goal="Calibrate epistemic probability using markers that govern indicative (a lo mejor, igual) or alternate with subjunctive (quizás, tal vez).",
        grammar_desc="marcadores de probabilidad y selección entre indicativo y subjuntivo",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Distinguish markers that strictly mandate indicative from those allowing subjunctive.",
            "Modulate epistemic commitment to convey varying degrees of doubt and conviction.",
            "Use B2 vocabulary of hypothesis, verification, and investigative analysis."
        ],
        intro_body=[
            "Welcome to Unit 3: Hypothesizing & Probability. In upper-intermediate Spanish, expressing doubt and certainty is not an all-or-nothing affair; it is a nuanced scale of probability.",
            "In this unit, inspired by Gabriel García Márquez's investigative masterpiece 'Crónica de una muerte anunciada', you will master the epistemic markers of conjecture, impersonal probability matrices, the future and conditional of probability, and the delicate art of hedging in intellectual discourse."
        ],
        intro_title="Unit 3: Hypothesizing & Probability"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-03-02 - Matrices impersonales de probabilidad
    # --------------------------------------------------------------------------
    l2 = "b2-03-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.03.02",
        "lesson": l2,
        "title": "Matrices de evaluación y posibilidad",
        "theme": "Expresiones impersonales y grados de verosimilitud",
        "words": [
            {"lemma": "caber", "translation": "to fit, to be room for (cabe la posibilidad)", "pos": "verb"},
            {"lemma": "descartar", "translation": "to rule out, to dismiss", "pos": "verb"},
            {"lemma": "la probabilidad", "translation": "probability, likelihood", "pos": "noun"},
            {"lemma": "indudable", "translation": "undoubted, unmistakable", "pos": "adjective"},
            {"lemma": "la sospecha", "translation": "suspicion", "pos": "noun"},
            {"lemma": "la premisa", "translation": "premise", "pos": "noun"},
            {"lemma": "suponer", "translation": "to suppose, to assume", "pos": "verb"},
            {"lemma": "factible", "translation": "feasible, doable", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.03.02.matrices-impersonales",
        "title": "Matrices impersonales de probabilidad y certeza",
        "sections": [
            {
                "type": "text",
                "title": "Estructuras impersonales con 'ser' y sustantivos",
                "content": "Las oraciones subordinadas sustantivas que dependen de matrices impersonales seleccionan el modo según si la matriz afirma certeza objetiva o probabilidad/duda."
            },
            {
                "type": "table",
                "title": "Régimen modal según la matriz impersonal",
                "rows": [
                    ["Matrices de certeza -> INDICATIVO", "Es indudable que, es evidente que, está claro que, es seguro que: 'Es evidente que hubo irregularidades'"],
                    ["Matrices de probabilidad/posibilidad -> SUBJUNTIVO", "Es probable que, es posible que, cabe la posibilidad de que, hay pocas dudas de que: 'Es probable que presenten apelación'"],
                    ["Matrices de certeza NEGADAS -> SUBJUNTIVO", "No es seguro que, no está claro que, no es verdad que: 'No está claro que hayan actuado de buena fe'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate formal",
                "items": [
                    {"spanish": "Cabe la posibilidad de que el vuelo sufra demoras debido a la niebla.", "english": "There is a possibility that the flight may suffer delays due to fog."},
                    {"spanish": "Es probable que los cancilleres alcancen un consenso antes de la medianoche.", "english": "It is probable that the chancellors will reach a consensus before midnight."},
                    {"spanish": "No cabe duda de que el informe contiene revelaciones de enorme gravedad.", "english": "There is no doubt that the report contains revelations of immense gravity."}
                ]
            },
            {
                "type": "tip",
                "content": "Atención a 'No cabe duda de que': al ser una afirmación enfática de certeza, exige indicativo ('No cabe duda de que es culpable'), mientras que 'Cabe la posibilidad de que' exige subjuntivo ('Cabe la posibilidad de que sea inocente')."
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
                    ["descartar", "to rule out, to dismiss"],
                    ["factible", "feasible, doable"],
                    ["indudable", "undoubted, unmistakable"],
                    ["la premisa", "premise"]
                ],
                "teaches": ["b2-unit03-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo verbal exige la matriz 'Cabe la posibilidad de que'?",
                "options": [
                    "Subjuntivo, porque denota una hipótesis o posibilidad no confirmada.",
                    "Indicativo, porque afirma un hecho factual evidente.",
                    "Imperativo, porque imparte una instrucción judicial obligatoria."
                ],
                "correct": 0,
                "teaches": ["matrices-impersonales-probabilidad"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Es muy probable que la junta directiva __ la propuesta de fusión empresarial. (aprobar)",
                "answer": "apruebe",
                "english": "It is very probable that the board of directors will approve the business merger proposal.",
                "teaches": ["matrices-impersonales-probabilidad"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Cabe", "la", "posibilidad", "de", "que", "hayan", "escapado."],
                "solution": ["Cabe", "la", "posibilidad", "de", "que", "hayan", "escapado."],
                "english": "There is a possibility that they have escaped.",
                "teaches": ["matrices-impersonales-probabilidad"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Médica", "text": "¿Descarta usted que el paciente haya contraído el virus en el laboratorio?"},
                    {"speaker": "Epidemiólogo", "text": "_____"},
                    {"speaker": "Médica", "text": "En ese caso, debemos mantener el cerco sanitario estricto."}
                ],
                "options": [
                    "No descarto nada; es sumamente probable que el contagio se haya producido allí.",
                    "El hospital cuenta con trescientas camas de hospitalización general.",
                    "Las vacunas suelen distribuirse de forma gratuita en los centros de salud."
                ],
                "correct": 0,
                "teaches": ["matrices-impersonales-probabilidad"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Es poco probable que los acreedores acepten una reestructuración de la deuda sin garantías.",
                "english": "It is unlikely that the creditors will accept a debt restructuring without guarantees.",
                "teaches": ["matrices-impersonales-probabilidad"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=3,
        title="Impersonal Matrices of Probability",
        goal="Formulate high-level institutional and scholarly probability statements using impersonal matrices with indicative and subjunctive.",
        grammar_desc="matrices impersonales de probabilidad y certeza en la subordinación",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Govern mood correctly after impersonal matrices of likelihood (es probable que + subj).",
            "Contrast certainty matrices (es seguro que + ind) with negated certainty (no es seguro que + subj).",
            "Employ formal analytical vocabulary (descartar, plausible, indudable)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-03-03 - Futuro de conjetura en presente y pasado
    # --------------------------------------------------------------------------
    l3 = "b2-03-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.03.03",
        "lesson": l3,
        "title": "Conjetura temporal e inferencia",
        "theme": "Deducción lógica y cálculo de posibilidades",
        "words": [
            {"lemma": "averiguar", "translation": "to find out, to ascertain", "pos": "verb"},
            {"lemma": "deducir", "translation": "to deduce, to infer", "pos": "verb"},
            {"lemma": "la estimación", "translation": "estimate, estimation", "pos": "noun"},
            {"lemma": "el rastro", "translation": "trail, trace", "pos": "noun"},
            {"lemma": "aproximado", "translation": "approximate", "pos": "adjective"},
            {"lemma": "presunto", "translation": "alleged, presumed", "pos": "adjective"},
            {"lemma": "el cálculo", "translation": "calculation, estimate", "pos": "noun"},
            {"lemma": "desconocer", "translation": "to be unaware of, to not know", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.03.03.futuro-conjetura",
        "title": "El futuro simple y compuesto de conjetura",
        "sections": [
            {
                "type": "text",
                "title": "El valor modal del futuro",
                "content": "En español, las formas del futuro no solo indican posterioridad temporal, sino que cumplen una función modal epistémica primordial: expresar conjetura, suposición o probabilidad en el presente o en el pasado reciente."
            },
            {
                "type": "table",
                "title": "Valores epistémicos del futuro",
                "rows": [
                    ["Futuro simple -> Probabilidad en el PRESENTE", "'¿Qué hora es? —Serán las tres' (= Probablemente son las tres); '¿Quién llama? —Será el cartero' (= Supongo que es el cartero)"],
                    ["Futuro compuesto -> Probabilidad en el PASADO RECIENTE", "'Habrá salido ya' (= Probablemente ya ha salido / Supongo que ya salió); '¿Dónde habrá dejado las llaves?' (= ¿Dónde las habrá puesto?)"],
                    ["Preguntas retóricas de extrañeza", "'¿Será verdad lo que dicen?' (= Me pregunto si es verdad); '¿Dónde estará metido?' (= No tengo idea de dónde está)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el discurso deductivo",
                "items": [
                    {"spanish": "Tendrá unos cuarenta años, a juzgar por su aspecto físico.", "english": "He is probably around forty years old, judging by his physical appearance."},
                    {"spanish": "¿Dónde se habrán metido los documentos de la licitación?", "english": "Where could the bidding documents have gotten to?"},
                    {"spanish": "Habrá tenido algún contratiempo en el aeropuerto, pues no ha llegado aún.", "english": "She must have had some mishap at the airport, for she hasn't arrived yet."}
                ]
            },
            {
                "type": "tip",
                "content": "El futuro de probabilidad equivale semánticamente a construcciones perifrásticas con 'deber de + infinitivo' o 'probablemente + presente', pero resulta mucho más natural y conciso en español hablado y literario."
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
                    ["averiguar", "to find out, to ascertain"],
                    ["deducir", "to deduce, to infer"],
                    ["presunto", "alleged, presumed"],
                    ["el rastro", "trail, trace"]
                ],
                "teaches": ["b2-unit03-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué significado tiene 'Estará en su despacho' en respuesta a '¿Dónde está el decano?'?",
                "options": [
                    "Supongo o conjeturo que probablemente se encuentra en su despacho ahora.",
                    "Irá físicamente a su despacho dentro de dos horas.",
                    "Tiene la obligación legal de permanecer en su despacho."
                ],
                "correct": 0,
                "teaches": ["futuro-conjetura-presente-pasado"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No contesta el teléfono; se __ quedado dormido tras el largo viaje. (haber - future conjecture)",
                "answer": "habrá",
                "english": "He doesn't answer the phone; he must have fallen asleep after the long journey.",
                "teaches": ["futuro-conjetura-presente-pasado"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["¿Quién", "será", "a", "estas", "horas", "de", "la", "noche?"],
                "solution": ["¿Quién", "será", "a", "estas", "horas", "de", "la", "noche?"],
                "english": "Who could it be at these hours of the night?",
                "teaches": ["futuro-conjetura-presente-pasado"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Investigador", "text": "¿Por qué no se presentó el testigo clave a la audiencia de hoy?"},
                    {"speaker": "Ayudante", "text": "_____"},
                    {"speaker": "Investigador", "text": "Es lo más probable; enviaremos a alguien a verificar su domicilio."}
                ],
                "options": [
                    "Habrá recibido amenazas o tendrá temor a represalias de la banda.",
                    "El tribunal sesiona de lunes a viernes en el palacio de justicia.",
                    "El testigo declaró el año pasado ante un juez de instrucción."
                ],
                "correct": 0,
                "teaches": ["futuro-conjetura-presente-pasado"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Tendrá sus razones para guardar silencio, pero su actitud despierta muchas sospechas.",
                "english": "He must have his reasons for keeping silent, but his attitude arouses many suspicions.",
                "teaches": ["futuro-conjetura-presente-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=3,
        title="Future of Conjecture: Present & Past",
        goal="Express spontaneous deductions, present assumptions, and recent past conjectures using the simple and compound future.",
        grammar_desc="el futuro simple y compuesto de conjetura epistémica",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Use the simple future to speculate about current states (tendrá unos cuarenta años).",
            "Use the compound future for logical deductions about past events (se habrá quedado dormido).",
            "Deploy deductive vocabulary (averiguar, deducir, presunto, cálculo)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-03-04 - Condicional de probabilidad en marcos del pasado
    # --------------------------------------------------------------------------
    l4 = "b2-03-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.03.04",
        "lesson": l4,
        "title": "Conjetura retrospectiva y reconstrucción",
        "theme": "Suposiciones sobre el pasado y crónica judicial",
        "words": [
            {"lemma": "rondar", "translation": "to hover around, to prowl, to be around", "pos": "verb"},
            {"lemma": "el testigo", "translation": "witness", "pos": "noun"},
            {"lemma": "la incertidumbre", "translation": "uncertainty", "pos": "noun"},
            {"lemma": "reconstruir", "translation": "to reconstruct", "pos": "verb"},
            {"lemma": "aparente", "translation": "apparent", "pos": "adjective"},
            {"lemma": "constatar", "translation": "to verify, to confirm, to state", "pos": "verb"},
            {"lemma": "la cuartada", "translation": "alibi", "pos": "noun"},
            {"lemma": "el móvil", "translation": "motive (of a crime)", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.03.04.condicional-conjetura",
        "title": "El condicional de conjetura en el pasado",
        "sections": [
            {
                "type": "text",
                "title": "La conjetura en el pasado",
                "content": "Así como el futuro simple expresa conjetura sobre el presente ('tendrá hambre ahora'), el condicional simple expresa conjetura o probabilidad sobre un momento del pasado ('tendría hambre entonces' = probablemente tenía hambre). Es el tiempo estrella de la crónica periodística, la novela policial y la reconstrucción histórica."
            },
            {
                "type": "table",
                "title": "Paralelismo modal entre futuro y condicional",
                "rows": [
                    ["Presente -> Futuro simple", "'Serán las cinco' (= Supongo que son las cinco ahora)"],
                    ["Pasado -> Condicional simple", "'Serían las cinco cuando llegó' (= Supongo que eran las cinco cuando llegó)"],
                    ["Pasado anterior -> Condicional compuesto", "'Habría cumplido veinte años cuando se marchó' (= Probablemente ya había cumplido veinte años)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en crónicas y relatos",
                "items": [
                    {"spanish": "El sospechoso rondaría los treinta años y vestía una chaqueta oscura.", "english": "The suspect must have been around thirty years old and was wearing a dark jacket."},
                    {"spanish": "¿Quién llamaría a la puerta a esas horas de la madrugada?", "english": "Who could have been knocking at the door at those hours of the dawn?"},
                    {"spanish": "Habrían sido las tres cuando se escuchó el primer disparo en el callejón.", "english": "It must have been three o'clock when the first gunshot was heard in the alley."}
                ]
            },
            {
                "type": "tip",
                "content": "No confundas el condicional hipotético ('yo iría si tuviera tiempo') con el condicional de conjetura ('serían las dos cuando ocurrió'). En este último no hay ninguna condición expresa; funciona como un marcador de probabilidad retrospectiva."
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
                    ["rondar", "to hover around, to be around"],
                    ["la incertidumbre", "uncertainty"],
                    ["constatar", "to verify, to confirm"],
                    ["el móvil", "motive (of a crime)"]
                ],
                "teaches": ["b2-unit03-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué expresa el condicional en 'En aquel entonces el coronel tendría unos cincuenta años'?",
                "options": [
                    "Conjetura o cálculo aproximado sobre una situación en el pasado.",
                    "Una acción futura que dependía de una condición no cumplida.",
                    "Un deseo cortés formulado ante una autoridad militar."
                ],
                "correct": 0,
                "teaches": ["condicional-conjetura-pasado"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Cuando los vecinos salieron a la plaza, __ las cuatro de la madrugada. (ser - conditional of past conjecture)",
                "answer": "serían",
                "english": "When the neighbors came out into the square, it must have been four in the morning.",
                "teaches": ["condicional-conjetura-pasado"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["¿Quién", "sabría", "entonces", "la", "verdadera", "historia?"],
                "solution": ["¿Quién", "sabría", "entonces", "la", "verdadera", "historia?"],
                "english": "Who could have known the true story back then?",
                "teaches": ["condicional-conjetura-pasado"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Cronista", "text": "¿A qué hora exacta ocurrieron los trágicos sucesos?"},
                    {"speaker": "Vecino", "text": "_____"},
                    {"speaker": "Cronista", "text": "Esa franja horaria coincide con los testimonios del panadero."}
                ],
                "options": [
                    "Serían las seis y media cuando Santiago Nasar bajó hacia el muelle del puerto.",
                    "El puerto fluvial fue construido por ingenieros holandeses hace dos siglos.",
                    "Los lunes por la mañana siempre hay mercado de pescado fresco en la dársena."
                ],
                "correct": 0,
                "teaches": ["condicional-conjetura-pasado"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Nadie pudo precisar cuánto dinero llevaría la víctima en la cartera aquella fatídica noche.",
                "english": "No one could specify how much money the victim must have been carrying in his wallet that fateful night.",
                "teaches": ["condicional-conjetura-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=3,
        title="Conditional of Probability in the Past",
        goal="Reconstruct historical and forensic timelines by formulating retrospective conjectures with the simple and compound conditional.",
        grammar_desc="el condicional simple y compuesto de conjetura en marcos pretéritos",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Formulate speculative past estimates using the conditional (serían las tres).",
            "Integrate forensic and investigative vocabulary into narrative chronicles.",
            "Distinguish between hypothetical conditionality and past epistemic conjecture."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-03-05 - Adverbios epistémicos y matización asertiva
    # --------------------------------------------------------------------------
    l5 = "b2-03-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.03.05",
        "lesson": l5,
        "title": "Atenuación asertiva y argumentación",
        "theme": "Adverbios epistémicos y cautela en el juicio",
        "words": [
            {"lemma": "presumiblemente", "translation": "presumably", "pos": "adverb"},
            {"lemma": "aparentemente", "translation": "apparently", "pos": "adverb"},
            {"lemma": "sostener", "translation": "to claim, to maintain, to uphold", "pos": "verb"},
            {"lemma": "la deducción", "translation": "deduction", "pos": "noun"},
            {"lemma": "fehaciente", "translation": "reliable, irrefutable, authentic", "pos": "adjective"},
            {"lemma": "tajante", "translation": "blunt, sharp, categorical", "pos": "adjective"},
            {"lemma": "el matiz", "translation": "nuance, shade of meaning", "pos": "noun"},
            {"lemma": "disipar", "translation": "to dispel, to dissipate", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.03.05.adverbios-epistemicos",
        "title": "Adverbios epistémicos y atenuación de asertos",
        "sections": [
            {
                "type": "text",
                "title": "El arte de matizar las afirmaciones",
                "content": "En la argumentación académica, jurídica y periodística B2, afirmar algo de manera tajante sin pruebas contundentes resta credibilidad. Los adverbios epistémicos y las locuciones parentéticas permiten calibrar el grado de certeza sin comprometer la objetividad del análisis."
            },
            {
                "type": "table",
                "title": "Adverbios y locuciones epistémicas",
                "rows": [
                    ["Presumiblemente / Supuestamente", "Basado en indicios razonables pero sin confirmación definitiva: 'El acuerdo fue firmado presumiblemente a puerta cerrada'"],
                    ["Aparentemente / Según parece", "Basado en la evidencia visible o en testimonios externos: 'Aparentemente, no hubo daños estructurales'"],
                    ["Con toda probabilidad", "Certeza casi absoluta fundada en la lógica deductiva: 'Con toda probabilidad, el fallo se dará a conocer el viernes'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo formal",
                "items": [
                    {"spanish": "El informe pericial demuestra fehacientemente que el incendio fue intencional.", "english": "The forensic report irrefutably demonstrates that the fire was intentional."},
                    {"spanish": "Presumiblemente, los negociadores alcanzaron un principio de entendimiento antes del amanecer.", "english": "Presumably, the negotiators reached a preliminary understanding before dawn."},
                    {"spanish": "Según parece, las discrepancias presupuestarias son menos graves de lo previsto.", "english": "Apparently, the budgetary discrepancies are less serious than anticipated."}
                ]
            },
            {
                "type": "tip",
                "content": "La posición del adverbio epistémico en la frase altera el ritmo: al inicio de la oración ('Presumiblemente, el autor...') califica a toda la proposición; intercalado entre comas aporta un matiz reflexivo de cautela."
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
                    ["presumiblemente", "presumably"],
                    ["fehaciente", "reliable, irrefutable"],
                    ["tajante", "blunt, categorical"],
                    ["disipar", "to dispel, to dissipate"]
                ],
                "teaches": ["b2-unit03-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple 'presumiblemente' en 'El manuscrito fue redactado presumiblemente en el siglo dieciocho'?",
                "options": [
                    "Atenúa la afirmación indicando una deducción verosímil sin certeza absoluta.",
                    "Indica una condición indispensable para que el manuscrito exista.",
                    "Ordena cronológicamente los capítulos del texto."
                ],
                "correct": 0,
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las pruebas presentadas por la fiscalía demostraron de forma __ la culpabilidad del sospechoso. (fehaciente)",
                "answer": "fehaciente",
                "english": "The evidence presented by the prosecution irrefutably demonstrated the suspect's guilt.",
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Presumiblemente", "los", "fondos", "fueron", "desviados", "hacia", "el", "exterior."],
                "solution": ["Presumiblemente", "los", "fondos", "fueron", "desviados", "hacia", "el", "exterior."],
                "english": "Presumably the funds were diverted abroad.",
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Catedrático", "text": "¿Podemos sostener de forma tajante que la hipótesis fue corroborada?"},
                    {"speaker": "Doctorando", "text": "_____"},
                    {"speaker": "Catedrático", "text": "Una prudencia metodológica ejemplar para su tesis doctoral."}
                ],
                "options": [
                    "Conviene ser cautelosos; los datos apuntan en esa dirección, pero aún no contamos con pruebas fehacientes.",
                    "Ayer compramos una nueva pizarra para el aula magna de la facultad.",
                    "El semestre universitario concluirá a finales del mes de noviembre."
                ],
                "correct": 0,
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Para disipar las sospechas, el consejo directivo presentó un informe con pruebas fehacientes.",
                "english": "To dispel suspicions, the board of directors presented a report with irrefutable evidence.",
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=3,
        title="Epistemic Adverbs & Assertive Hedging",
        goal="Master the rhetoric of hedging and epistemic qualification in scholarly and journalistic debates using adverbs of probability.",
        grammar_desc="adverbios epistémicos y atenuación de asertos en la prosa analítica",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Hedge academic claims using adverbs of probability (presumiblemente, aparentemente).",
            "Avoid overly categorical claims in analytical essays through tactical qualification.",
            "Deploy high-register evidentiary vocabulary (fehaciente, tajante, disipar, conjetura)."
        ]
    ))

    # --------------------------------------------------------------------------
    # Story: stories/classics/b2/b2-03.json (Gabriel García Márquez: Crónica de una muerte anunciada)
    # --------------------------------------------------------------------------
    write_json("stories/classics/b2/b2-03.json", {
        "id": "story.b2.03.garciamarquez",
        "title": "Gabriel García Márquez: Memoria, fatalidad y conjetura",
        "level": "B2",
        "author": "Gabriel García Márquez (Colombia, 1927–2014)",
        "work": "Crónica de una muerte anunciada",
        "summary": "Una reflexión sobre la magistral novela de García Márquez donde la reconstrucción periodística, los testimonios contradictorios y el condicional de probabilidad exploran la fatalidad colectiva.",
        "vocabularyTopics": ["Novela latinoamericana", "Crónica policial", "Fatalidad y conjetura"],
        "grammar": ["condicional de conjetura en el pasado", "matrices impersonales de probabilidad"],
        "paragraphs": [
            {
                "text": "El día en que lo iban a matar, Santiago Nasar se levantó a las 5:30 de la mañana para esperar el buque en que llegaba el obispo. Había soñado que atravesaba un bosque de higuerones donde caía una llovizna tierna, pero al despertar se sintió por completo salpicado de cagada de pájaros. Nunca imaginó que aquel amanecer marcaría el término inexorable de su existencia.",
                "english": "On the day they were going to kill him, Santiago Nasar got up at 5:30 in the morning to wait for the boat the bishop was arriving on. He had dreamed that he was traversing a grove of fig trees where a gentle drizzle was falling, but on waking he felt completely spattered with bird droppings. He never imagined that that dawn would mark the inexorable end of his existence."
            },
            {
                "text": "Veintisiete años después, el narrador regresa al pueblo fluvial para reconstruir la memoria quebrada de aquel crimen que todos sabían que iba a ocurrir y que nadie evitó. Los testimonios recogidos en el sumario judicial están plagados de conjeturas: unos afirmaban que llovía a cántaros; otros sostenían que el sol radiaba sobre la dársena. Serían las seis y media cuando los gemelos Vicario afilaron los cuchillos de matar cerdos.",
                "english": "Twenty-seven years later, the narrator returns to the river town to reconstruct the fractured memory of that crime which everyone knew was going to occur and which no one prevented. The testimonies gathered in the judicial summary are riddled with conjectures: some claimed it was pouring rain; others maintained that the sun was radiating over the dock. It must have been six-thirty when the Vicario twins sharpened the pig-butchering knives."
            },
            {
                "text": "La genialidad de García Márquez radica en transformar una trama policíaca inversa en una meditación sobre la culpa compartida y la ambigüedad de la verdad. A través del condicional de probabilidad y las hipótesis no corroboradas, la novela demuestra que la memoria no es un registro exacto de los hechos, sino un laberinto de versiones donde la fatalidad se disfraza de casualidad.",
                "english": "García Márquez's genius lies in transforming an inverted detective plot into a meditation on shared guilt and the ambiguity of truth. Through the conditional of probability and uncorroborated hypotheses, the novel demonstrates that memory is not an exact record of events, but a labyrinth of versions where fatality disguises itself as coincidence."
            }
        ]
    })

    # --------------------------------------------------------------------------
    # Lesson 6: b2-03-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-03-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la conjetura", "conjecture, guess"],
                    ["descartar", "to rule out, to dismiss"],
                    ["presunto", "alleged, presumed"],
                    ["fehaciente", "irrefutable, reliable"]
                ],
                "teaches": ["b2-unit03-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según el análisis de 'Crónica de una muerte anunciada', ¿qué demuestra la multiplicidad de testimonios recogidos por el narrador?",
                "options": [
                    "Que la memoria es un laberinto de versiones contradictorias y conjeturas sobre un destino fatal.",
                    "Que todos los testigos mintieron deliberadamente ante el juez instructor.",
                    "Que el crimen se resolvió en menos de veinticuatro horas gracias a pruebas forenses definitivas."
                ],
                "correct": 0
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la frase 'Serían las seis cuando los hermanos salieron de la tienda', ¿qué expresa el verbo 'serían'?",
                "options": [
                    "Cálculo o suposición aproximada sobre la hora en el pasado.",
                    "Una orden indirecta transmitida en estilo indirecto.",
                    "Una condición imposible en el presente."
                ],
                "correct": 0,
                "teaches": ["condicional-conjetura-pasado"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Es muy probable que los peritos judiciales no __ todas las huellas de la escena del crimen. (encontrar)",
                "answer": "hayan encontrado",
                "english": "It is very probable that the forensic experts did not find all the footprints at the crime scene.",
                "teaches": ["matrices-impersonales-probabilidad"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "A lo mejor los vecinos pensaron que se trataba de una broma de carnaval. [Maybe the neighbors thought it was a carnival joke.]",
                    "Serían las seis de la mañana cuando Santiago Nasar salió de su casa vestido de blanco. [It must have been six in the morning when Santiago Nasar left his house dressed in white.]",
                    "Cabe la posibilidad de que nadie se atreviera a advertirle del peligro inminente. [There is a possibility that no one dared to warn him of the imminent danger.]",
                    "El informe forense concluyó que el ataque se produjo de manera fulminante. [The forensic report concluded that the attack took place in a lightning flash.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["probabilidad-indicativo-subjuntivo", "condicional-conjetura-pasado"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítico literario", "text": "¿Por qué García Márquez utiliza con tanta frecuencia el condicional en la novela?"},
                    {"speaker": "Investigadora", "text": "_____"},
                    {"speaker": "Crítico literario", "text": "Una técnica narrativa que refuerza la tragedia colectiva."}
                ],
                "options": [
                    "Porque le permite reconstruir los sucesos pasados como hipótesis de los testigos en lugar de certezas dogmáticas.",
                    "Porque el autor desconocía las reglas de conjugación del pretérito indefinido.",
                    "Porque la historia transcurre en un futuro distante de ciencia ficción."
                ],
                "correct": 0,
                "teaches": ["condicional-conjetura-pasado"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Presumiblemente, los motivos del crimen nunca quedaron esclarecidos de forma fehaciente.",
                "english": "Presumably, the motives of the crime were never irrefutably clarified.",
                "teaches": ["probabilidad-indicativo-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Escribe una conjetura sobre una situación pasada utilizando el condicional simple de probabilidad y el adverbio 'rondar'.",
                        "answer": "Cuando comenzó la asamblea, la temperatura en la sala rondaría los cuarenta grados."
                    }
                ],
                "teaches": ["condicional-conjetura-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=3,
        title="Unit 3 Consolidation",
        goal="Consolidate epistemic probability markers, impersonal matrices, future and conditional of conjecture, and academic hedging.",
        grammar_desc="síntesis de hipótesis, probabilidad y conjetura en español",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Consolidate indicative vs subjunctive selection with probability triggers.",
            "Formulate speculative hypotheses with future and conditional of conjecture.",
            "Apply assertive hedging and epistemic qualification to complex arguments.",
            "Analyze journalistic and literary excerpts from Gabriel García Márquez."
        ],
        checklist_items=[
            "I can use a lo mejor with indicative and quizás/tal vez with indicative or subjunctive.",
            "I can govern mood accurately after impersonal probability matrices (es probable que).",
            "I can formulate deductions about the present and past using the future and conditional of conjecture.",
            "I can qualify assertions and hedge claims in academic and professional prose."
        ],
        story_ref="stories/classics/b2/b2-03.json"
    ))
    print("Completed Core Unit 3 generation!")


if __name__ == "__main__":
    generate_core_unit_3()
