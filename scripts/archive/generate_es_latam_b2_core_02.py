#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Core Unit 2:
  - Title: "Narrative Time & Aspect" (El relato en el pasado: matices aspectuales)
  - Stems: b2-02-01 through b2-02-consolidation
  - Classic Literature Story: Juan Rulfo - "Pedro Páramo y Luvina: El murmullo y el tiempo suspendido"
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_core_unit_2():
    # Vocab theme slug: b2-unit02-vocab
    # Grammar skills:
    #   - pret-indefinido-vs-imperfecto-narrativo
    #   - pluscuamperfecto-retrospectiva
    #   - verbos-cambio-significado-pasado
    #   - conectores-temporales-pasado

    # --------------------------------------------------------------------------
    # Lesson 1: b2-02-01 - Aspecto narrativo: Indefinido vs Imperfecto
    # --------------------------------------------------------------------------
    l1 = "b2-02-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.02.01",
        "lesson": l1,
        "title": "El tiempo del relato y la atmósfera",
        "theme": "Narrativa literaria y matices aspectuales",
        "words": [
            {"lemma": "el relato", "translation": "tale, account, story", "pos": "noun"},
            {"lemma": "la penumbra", "translation": "gloom, half-light", "pos": "noun"},
            {"lemma": "el murmullo", "translation": "murmur, whisper", "pos": "noun"},
            {"lemma": "estremecer", "translation": "to shudder, to shake", "pos": "verb"},
            {"lemma": "desvanecerse", "translation": "to fade away, to vanish", "pos": "verb"},
            {"lemma": "el vestigio", "translation": "vestige, trace", "pos": "noun"},
            {"lemma": "remoto", "translation": "remote, distant", "pos": "adjective"},
            {"lemma": "la quietud", "translation": "stillness, stillness of night", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.02.01.indefinido-imperfecto",
        "title": "Aspecto narrativo: Indefinido frente a Imperfecto",
        "sections": [
            {
                "type": "text",
                "title": "Primer plano frente a trasfondo",
                "content": "En la prosa narrativa de nivel B2, el pretérito indefinido (perfecto simple) y el pretérito imperfecto no solo distinguen acciones puntuales de habituales, sino que articulan la estructura informativa del relato: el indefinido impulsa los acontecimientos en primer plano (foreground), mientras que el imperfecto despliega el trasfondo escénico, sensorial y psicológico (background)."
            },
            {
                "type": "table",
                "title": "Funciones aspectuales en el relato literario",
                "rows": [
                    ["Indefinido (Perfectivo)", "Acciones delimitadas, sucesión cronológica, giros argumentales: 'El forastero cruzó el umbral y cerró la puerta'"],
                    ["Imperfecto (Imperfectivo)", "Circunstancias concomitantes, estados anímicos, descripciones sensoriales: 'La lluvia golpeaba los cristales y nadie decía una palabra'"],
                    ["Imperfecto de ruptura / narrativo", "Uso estilístico que focaliza el desarrollo de un evento clave como cuadro vivo: 'Apenas sonó el disparo, la multitud corría despavorida'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en prosa narrativa",
                "items": [
                    {"spanish": "Amanecía cuando el arriero divisó las primeras casas del pueblo.", "english": "It was dawning when the muleteer caught sight of the village's first houses."},
                    {"spanish": "El viento soplaba con furia; súbitamente se quebró la rama centenaria.", "english": "The wind was blowing furiously; suddenly the ancient branch snapped."},
                    {"spanish": "Mientras los demás dormían, él meditaba sobre su incierto destino.", "english": "While the others slept, he pondered his uncertain fate."}
                ]
            },
            {
                "type": "tip",
                "content": "Presta atención al efecto de perspectiva: el cambio del imperfecto al indefinido produce un golpe de efecto narrativo ('hacía frío, caía la tarde... y de pronto llegó la carta')."
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
                    ["la penumbra", "gloom, half-light"],
                    ["el vestigio", "vestige, trace"],
                    ["la quietud", "stillness, silence"],
                    ["desvanecerse", "to fade away, to vanish"]
                ],
                "teaches": ["b2-unit02-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el imperfecto en 'La niebla cubría el camino cuando sonaron las campanas'?",
                "options": [
                    "Establece el trasfondo escénico sobre el cual ocurre el evento puntual.",
                    "Indica una acción completada que interrumpe a otra.",
                    "Expresa una orden o mandato atenuado en el pasado."
                ],
                "correct": 0,
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El reloj de la sala marcaba las doce cuando alguien __ con violencia a la puerta. (llamar)",
                "answer": "llamó",
                "english": "The living room clock was striking twelve when someone knocked violently on the door.",
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "penumbra", "envolvía", "el", "valle", "cuando", "partieron."],
                "solution": ["La", "penumbra", "envolvía", "el", "valle", "cuando", "partieron."],
                "english": "The gloom enveloped the valley when they departed.",
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Narrador A", "text": "¿Cómo recuerdas la atmósfera de esa noche en Comala?"},
                    {"speaker": "Narrador B", "text": "_____"},
                    {"speaker": "Narrador A", "text": "Y en ese instante decisivo se produjo el encuentro."}
                ],
                "options": [
                    "Reinaba un silencio absoluto y las sombras se alargaban por los muros.",
                    "Ayer compramos dos pasajes para viajar en autobús.",
                    "Mañana terminará la reconstrucción del viejo campanario."
                ],
                "correct": 0,
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El viento soplaba sin descanso y los murmullos se apagaban en la distancia.",
                "english": "The wind blew ceaselessly and the murmurs died away in the distance.",
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=2,
        title="Narrative Time: Indefinido vs Imperfecto",
        goal="Master the contrast between preterite and imperfect to structure foreground events and atmospheric background in literary narration.",
        grammar_desc="contraste aspectual entre indefinido e imperfecto en la narración",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Distinguish foreground narrative action from background scene setting.",
            "Use B2 narrative vocabulary to establish mood, atmosphere, and sensory texture.",
            "Apply aspectual shifts to create narrative suspense and emotional pacing."
        ],
        intro_body=[
            "Welcome to Unit 2: Narrative Time & Aspect. At the B2 level, narrating in the past transcends merely listing past actions. It involves mastering aspectual perspective—the art of controlling how an audience perceives the duration, inception, background, and culmination of events.",
            "In this unit, inspired by the haunting, fractured narratives of Mexican master Juan Rulfo (Pedro Páramo, El llano en llamas), you will explore the subtle boundary between indefinido and imperfecto, delve into the temporal layers of the pluscuamperfecto, and uncover how certain verbs transform their core meaning when shifted across past tenses."
        ],
        intro_title="Unit 2: Narrative Time & Aspect"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-02-02 - La profundidad temporal: Pluscuamperfecto
    # --------------------------------------------------------------------------
    l2 = "b2-02-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.02.02",
        "lesson": l2,
        "title": "Retrospección y memoria",
        "theme": "Profundidad temporal y planos narrativos",
        "words": [
            {"lemma": "el trasfondo", "translation": "background, subtext", "pos": "noun"},
            {"lemma": "acontecer", "translation": "to happen, to take place", "pos": "verb"},
            {"lemma": "preceder", "translation": "to precede", "pos": "verb"},
            {"lemma": "la evocación", "translation": "evocation, reminiscence", "pos": "noun"},
            {"lemma": "retrospectivo", "translation": "retrospective", "pos": "adjective"},
            {"lemma": "la huella", "translation": "footprint, imprint, trace", "pos": "noun"},
            {"lemma": "desentrañar", "translation": "to unravel, to figure out", "pos": "verb"},
            {"lemma": "pretérito", "translation": "past, bygone", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.02.02.pluscuamperfecto",
        "title": "El pluscuamperfecto en la retrospección narrativa",
        "sections": [
            {
                "type": "text",
                "title": "El tiempo del pasado anterior al pasado",
                "content": "El pretérito pluscuamperfecto de indicativo (había + participio) sitúa una acción como consumada con anterioridad a otro punto de referencia en el pasado. En la literatura y el periodismo narrativo, es la herramienta fundamental para construir analepsis (flashbacks), revelar antecedentes ocultos y dotar a la historia de espesor cronológico."
            },
            {
                "type": "table",
                "title": "Usos y matices discursivos",
                "rows": [
                    ["Retrospección causal", "Explica la causa previa de una situación presente en el relato: 'Estaba exhausto porque había caminado toda la noche'"],
                    ["Acontecimiento preliminar", "Marca un hecho completado antes de un hito: 'Para cuando llegó la ayuda, el fuego ya se había extinguido'"],
                    ["Alineación temporal con 'ya' y 'apenas'", "Destaca inmediatez o culminación previa: 'Apenas se habían sentado cuando irrumpió la noticia'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos literarios",
                "items": [
                    {"spanish": "Muchos años antes, su abuelo le había advertido sobre los peligros del páramo.", "english": "Many years before, his grandfather had warned him about the dangers of the wasteland."},
                    {"spanish": "Todo lo que creía seguro se había desmoronado en cuestión de semanas.", "english": "Everything he believed secure had crumbled in a matter of weeks."},
                    {"spanish": "Cuando regresó a la casa natal, sus moradores ya habían partido para siempre.", "english": "When he returned to his childhood home, its dwellers had already departed forever."}
                ]
            },
            {
                "type": "tip",
                "content": "En textos narrativos elaborados, no es necesario mantener el pluscuamperfecto en cada verbo de un flashback largo: una vez establecido el marco con el pluscuamperfecto, la narración interna suele continuar en indefinido."
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
                    ["el trasfondo", "background, subtext"],
                    ["acontecer", "to happen, to take place"],
                    ["preceder", "to precede"],
                    ["desentrañar", "to unravel, to figure out"]
                ],
                "teaches": ["b2-unit02-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué se utiliza el pluscuamperfecto en 'Pedro comprendió que su hermano ya había tomado la decisión'?",
                "options": [
                    "Porque la decisión se tomó antes del momento en que Pedro lo comprendió.",
                    "Porque describe una acción habitual que se repetía con frecuencia.",
                    "Porque expresa una hipótesis probable en el momento presente."
                ],
                "correct": 0,
                "teaches": ["pluscuamperfecto-retrospectiva"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Cuando los rescatistas alcanzaron la cumbre, la tormenta ya __ por completo el sendero. (borrar)",
                "answer": "había borrado",
                "english": "When the rescuers reached the summit, the storm had already completely erased the trail.",
                "teaches": ["pluscuamperfecto-retrospectiva"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Él", "había", "previsto", "aquel", "desenlace", "muchos", "años", "atrás."],
                "solution": ["Él", "había", "previsto", "aquel", "desenlace", "muchos", "años", "atrás."],
                "english": "He had foreseen that outcome many years ago.",
                "teaches": ["pluscuamperfecto-retrospectiva"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Investigador", "text": "¿Cuándo descubrieron los documentos confidenciales?"},
                    {"speaker": "Archivista", "text": "_____"},
                    {"speaker": "Investigador", "text": "Eso explica por qué nadie los encontró durante la auditoría anterior."}
                ],
                "options": [
                    "Al revisar el sótano nos percatamos de que alguien los había ocultado allí.",
                    "Comenzaremos la clasificación formal el mes entrante.",
                    "Los archivistas siempre trabajan con guantes de algodón blanco."
                ],
                "correct": 0,
                "teaches": ["pluscuamperfecto-retrospectiva"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Nadie sospechaba que el anciano ya había dejado escritas todas sus memorias.",
                "english": "No one suspected that the old man had already left all his memoirs written.",
                "teaches": ["pluscuamperfecto-retrospectiva"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=2,
        title="Temporal Depth: The Pluperfect",
        goal="Construct multi-layered chronological narratives using the pluperfect indicative to integrate flashbacks, past causes, and retrospective revelations.",
        grammar_desc="el pretérito pluscuamperfecto en la retrospección narrativa",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Signal anteriority in past narration with the pluperfect indicative.",
            "Incorporate retrospective flashbacks (analepsis) into complex prose.",
            "Master B2 vocabulary of memory, prehistory, and causal antecedents."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-02-03 - Verbos con cambio de significado en el pasado
    # --------------------------------------------------------------------------
    l3 = "b2-02-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.02.03",
        "lesson": l3,
        "title": "Verbos modales y cognitivos en el pasado",
        "theme": "Significado aspectual de verbos de conocimiento y voluntad",
        "words": [
            {"lemma": "el dilema", "translation": "dilemma", "pos": "noun"},
            {"lemma": "la resolución", "translation": "resolution, decision", "pos": "noun"},
            {"lemma": "el desenlace", "translation": "outcome, ending", "pos": "noun"},
            {"lemma": "rehusar", "translation": "to refuse", "pos": "verb"},
            {"lemma": "la lucidez", "translation": "lucidity, clarity of mind", "pos": "noun"},
            {"lemma": "el empeño", "translation": "determination, endeavor", "pos": "noun"},
            {"lemma": "flaquear", "translation": "to falter, to weaken", "pos": "verb"},
            {"lemma": "concluyente", "translation": "conclusive", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.02.03.verbos-cambio-significado",
        "title": "Verbos con cambio de significado según el aspecto",
        "sections": [
            {
                "type": "text",
                "title": "Aspecto léxico y tiempo verbal",
                "content": "Ciertos verbos en español expresan un estado mental o volitivo continuo cuando se conjugan en pretérito imperfecto, pero denotan un acontecimiento puntual, el inicio de un estado o el resultado de un esfuerzo cuando se conjugan en pretérito indefinido."
            },
            {
                "type": "table",
                "title": "Pares contrastivos fundamentales",
                "rows": [
                    ["Conocer", "Imperfecto: 'Conocía la ciudad' (tenía conocimiento previo). Indefinido: 'Conoció al autor' (se encontró con él por primera vez)."],
                    ["Saber", "Imperfecto: 'Sabía la verdad' (poseía la información). Indefinido: 'Supo la verdad' (se enteró en ese instante preciso)."],
                    ["Querer", "Imperfecto: 'Quería marcharse' (tenía el deseo o intención). Indefinido: 'Quiso abrir la puerta' (hizo el intento deliberado)."],
                    ["No querer", "Imperfecto: 'No quería hablar' (no tenía ganas). Indefinido: 'No quiso firmar' (se negó rotundamente / rechazó hacerlo)."],
                    ["Poder", "Imperfecto: 'Podía escapar' (tenía la capacidad o permiso). Indefinido: 'Pudo escapar' (lo intentó y lo logró con éxito)."]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en contexto",
                "items": [
                    {"spanish": "Ayer supimos que el director había presentado su renuncia.", "english": "Yesterday we found out that the director had tendered his resignation."},
                    {"spanish": "El testigo no quiso declarar ante el magistrado.", "english": "The witness refused to testify before the magistrate."},
                    {"spanish": "A pesar de la tormenta, los montañistas pudieron alcanzar el refugio.", "english": "Despite the storm, the mountaineers managed to reach the shelter."}
                ]
            },
            {
                "type": "tip",
                "content": "En la traducción al inglés, estos contrastes a menudo requieren verbos totalmente distintos: 'sabía' (knew) vs 'supo' (found out); 'no quiso' (refused); 'pudo' (managed to / succeeded in)."
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
                    ["el desenlace", "outcome, ending"],
                    ["el dilema", "dilemma"],
                    ["rehusar", "to refuse"],
                    ["flaquear", "to falter, to weaken"]
                ],
                "teaches": ["b2-unit02-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz adquiere el verbo en 'La abogada no quiso firmar aquel documento fraudulento'?",
                "options": [
                    "Se negó explícitamente a firmarlo (rechazo enérgico y puntual).",
                    "Simplemente tenía la vaga intención de no firmarlo.",
                    "No tenía la capacidad física ni legal de estampar su firma."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-significado-pasado"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Tras largas horas de deliberación, el jurado por fin __ llegar a un veredicto unánime. (poder - managed to)",
                "answer": "pudo",
                "english": "After long hours of deliberation, the jury finally managed to reach a unanimous verdict.",
                "teaches": ["verbos-cambio-significado-pasado"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Fue", "en", "el", "aeropuerto", "donde", "conoció", "a", "su", "socio."],
                "solution": ["Fue", "en", "el", "aeropuerto", "donde", "conoció", "a", "su", "socio."],
                "english": "It was at the airport where he met his partner for the first time.",
                "teaches": ["verbos-cambio-significado-pasado"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Cuándo se enteraron del dictamen de la corte?"},
                    {"speaker": "Portavoz", "text": "_____"},
                    {"speaker": "Periodista", "text": "Comprendo, fue una noticia inesperada para todo el país."}
                ],
                "options": [
                    "Lo supimos esta misma mañana a través de un comunicado oficial.",
                    "Sabíamos perfectamente que el derecho procesal es muy complejo.",
                    "El tribunal suele reunirse los martes por la tarde."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-significado-pasado"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aunque la presión era insostenible, el diplomático no quiso ceder ni un milímetro.",
                "english": "Although the pressure was untenable, the diplomat refused to yield a single millimeter.",
                "teaches": ["verbos-cambio-significado-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=2,
        title="Aspectual Meaning Shifts in Past Verbs",
        goal="Master the aspect-driven semantic transformations of verbs like conocer, saber, querer, and poder between preterite and imperfect.",
        grammar_desc="cambio de significado de verbos de estado y voluntad en el pasado",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Distinguish between continuous mental states and punctual cognitive events.",
            "Accurately employ saber (knew vs found out) and conocer (knew vs met).",
            "Express refusal (no quiso) and successful achievement (pudo) with precision."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-02-04 - Conectores temporales y ritmo de la narración
    # --------------------------------------------------------------------------
    l4 = "b2-02-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.02.04",
        "lesson": l4,
        "title": "Conectores y transiciones temporales",
        "theme": "Sintaxis temporal y ritmo de la narración",
        "words": [
            {"lemma": "apenas", "translation": "barely, as soon as", "pos": "conjunction"},
            {"lemma": "súbitamente", "translation": "suddenly", "pos": "adverb"},
            {"lemma": "de improviso", "translation": "unexpectedly, out of the blue", "pos": "adverb"},
            {"lemma": "conforme", "translation": "as, in proportion as", "pos": "conjunction"},
            {"lemma": "el intervalo", "translation": "interval", "pos": "noun"},
            {"lemma": "el sobresalto", "translation": "startle, shock", "pos": "noun"},
            {"lemma": "paulatino", "translation": "gradual, step-by-step", "pos": "adjective"},
            {"lemma": "precipitar", "translation": "to trigger, to accelerate", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.02.04.conectores-temporales",
        "title": "Conectores temporales en el relato pasado",
        "sections": [
            {
                "type": "text",
                "title": "Articular la secuencia y el ritmo",
                "content": "Para estructurar un relato complejo, el nivel B2 exige ir más allá de 'entonces' y 'después'. Los conectores temporales avanzados permiten graduar la velocidad narrativa, marcar inmediatez vertiginosa o señalar progresiones simultáneas y paulatinas."
            },
            {
                "type": "table",
                "title": "Conectores narrativos en el pasado",
                "rows": [
                    ["Inmediatez estricta", "'Apenas / No bien + verbo': marcan que la segunda acción ocurre instantáneamente tras la primera ('Apenas asomó el sol, emprendieron la marcha')"],
                    ["Simultaneidad progresiva", "'A medida que / Conforme + verbo': expresan evolución paralela ('Conforme avanzaba la noche, el frío se volvía más intenso')"],
                    ["Posterioridad culminativa", "'Al cabo de / Al cabo de unos días': sitúan la culminación tras un lapso medido ('Al cabo de tres meses de búsqueda, hallaron el manuscrito')"],
                    ["Ruptura súbita", "'De improviso / Súbitamente': introducen giros inesperados que rompen la quietud del relato"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en prosa",
                "items": [
                    {"spanish": "No bien hubo terminado de hablar, un aplauso ensordecedor llenó el auditorio.", "english": "No sooner had he finished speaking than deafening applause filled the auditorium."},
                    {"spanish": "A medida que ascendían por la quebrada, el aire escaseaba.", "english": "As they ascended through the gorge, the air grew thinner."},
                    {"spanish": "Al cabo de varias horas de incertidumbre, se restablecieron las comunicaciones.", "english": "After several hours of uncertainty, communications were restored."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que en el pasado todos estos conectores rigen modo indicativo, a diferencia de los contextos de prospección o futuro ('en cuanto llegue', subjuntivo)."
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
                    ["súbitamente", "suddenly"],
                    ["el sobresalto", "startle, shock"],
                    ["paulatino", "gradual, step-by-step"],
                    ["precipitar", "to trigger, to accelerate"]
                ],
                "teaches": ["b2-unit02-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué conector denota inmediatez rigurosa en el pasado en '_____ escuchó los pasos, apagó la vela'?",
                "options": [
                    "Apenas",
                    "A medida que",
                    "Al cabo de"
                ],
                "correct": 0,
                "teaches": ["conectores-temporales-pasado"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Conforme __ las tropas hacia el norte, el aprovisionamiento se hacía más difícil. (avanzar)",
                "answer": "avanzaban",
                "english": "As the troops advanced toward the north, provisioning grew more difficult.",
                "teaches": ["conectores-temporales-pasado"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "bien", "sonó", "la", "alarma,", "desalojaron", "el", "edificio."],
                "solution": ["No", "bien", "sonó", "la", "alarma,", "desalojaron", "el", "edificio."],
                "english": "No sooner did the alarm sound than they evacuated the building.",
                "teaches": ["conectores-temporales-pasado"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Testigo A", "text": "¿En qué momento exacto se desató el pánico en la estación?"},
                    {"speaker": "Testigo B", "text": "_____"},
                    {"speaker": "Testigo A", "text": "Fue una reacción en cadena verdaderamente aterradora."}
                ],
                "options": [
                    "Apenas se escuchó el estruendo subterráneo, la gente corrió hacia las salidas.",
                    "El metro de la ciudad cuenta con doce líneas principales en funcionamiento.",
                    "Siempre compramos el billete mensual para viajar con descuento."
                ],
                "correct": 0,
                "teaches": ["conectores-temporales-pasado"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Al cabo de intensas negociaciones que duraron toda la noche, firmaron el acuerdo.",
                "english": "After intense negotiations that lasted all night, they signed the agreement.",
                "teaches": ["conectores-temporales-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=2,
        title="Temporal Connectors in Narrative",
        goal="Control narrative pacing, instantaneity, and progressive parallel actions using advanced temporal connectors in the past.",
        grammar_desc="conectores temporales y estructuración del ritmo narrativo",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Structure chronological sequences with barely and no sooner (apenas, no bien).",
            "Express progressive parallel developments with a medida que and conforme.",
            "Calibrate narrative timing and dramatic pauses in literary prose."
        ]
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-02-05 - Usos especiales del imperfecto
    # --------------------------------------------------------------------------
    l5 = "b2-02-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.02.05",
        "lesson": l5,
        "title": "Matices discursivos y cortesía",
        "theme": "Usos pragmáticos y estilísticos del pasado",
        "words": [
            {"lemma": "pretender", "translation": "to intend, to claim", "pos": "verb"},
            {"lemma": "titubear", "translation": "to hesitate, to waver", "pos": "verb"},
            {"lemma": "la deferencia", "translation": "deference, respect", "pos": "noun"},
            {"lemma": "el conato", "translation": "attempt, slight outbreak", "pos": "noun"},
            {"lemma": "inminente", "translation": "imminent", "pos": "adjective"},
            {"lemma": "rozar", "translation": "to graze, to border on", "pos": "verb"},
            {"lemma": "aplacar", "translation": "to soothe, to appease", "pos": "verb"},
            {"lemma": "la sutileza", "translation": "subtlety", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.02.05.imperfecto-discursivo",
        "title": "Usos estilísticos y pragmáticos del imperfecto",
        "sections": [
            {
                "type": "text",
                "title": "Más allá de la descripción",
                "content": "En el registro formal y literario B2, el imperfecto adquiere funciones pragmáticas muy refinadas: atenúa peticiones con delicadeza, describe acciones inminentes que casi ocurrieron y sustituye al condicional en el habla coloquial o enfática."
            },
            {
                "type": "table",
                "title": "Usos especiales del imperfecto",
                "rows": [
                    ["Imperfecto de cortesía", "Atenúa la aserción en el presente para no sonar impositivo: 'Quería consultarle sobre el proyecto' (en lugar de 'quiero')"],
                    ["Imperfecto de conato", "Acción inminente que estuvo a punto de consumarse pero se frustró: 'Por poco me caía por la escalera'"],
                    ["Imperfecto de apertura lúdica / ficcional", "Establece las reglas de una fantasía o hipótesis compartida: 'Yo era el pirata y tú me rescatabas'"],
                    ["Imperfecto de contracautela / plan previsto", "Verifica un acuerdo previo en el presente: '¿A qué hora salía el vuelo mañana?'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos pragmáticos",
                "items": [
                    {"spanish": "Buenas tardes, venía a pedirle una prórroga para la entrega del informe.", "english": "Good afternoon, I was coming to ask you for an extension on the report submission."},
                    {"spanish": "¡Cuidado! Casi volcaba el automóvil en la curva.", "english": "Careful! The car almost overturned on the curve."},
                    {"spanish": "¿No era que ustedes se mudaban la próxima semana?", "english": "Wasn't it the case that you were moving next week?"}
                ]
            },
            {
                "type": "tip",
                "content": "El imperfecto de cortesía ('venía a', 'quería', 'pensaba') es de uso universal en América Latina para interactuar con superioridad jerárquica o en oficinas públicas sin sonar tajante."
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
                    ["la deferencia", "deference, respect"],
                    ["el conato", "attempt, slight outbreak"],
                    ["titubear", "to hesitate, to waver"],
                    ["la sutileza", "subtlety"]
                ],
                "teaches": ["b2-unit02-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué valor pragmático tiene el imperfecto en 'Disculpe, señorita, venía a preguntar por las becas de posgrado'?",
                "options": [
                    "Atenuación cortés que suaviza una petición en el presente.",
                    "Descripción objetiva de una caminata completada en el pasado.",
                    "Acción habitual repetida diariamente durante varios años."
                ],
                "correct": 0,
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Buenas tardes, profesor; __ hablar con usted sobre la corrección del ensayo. (querer - polite imperfect)",
                "answer": "quería",
                "english": "Good afternoon, professor; I wanted to speak with you about the essay correction.",
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Por", "poco", "perdía", "el", "tren", "de", "las", "ocho."],
                "solution": ["Por", "poco", "perdía", "el", "tren", "de", "las", "ocho."],
                "english": "I almost missed the eight o'clock train.",
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Secretaria", "text": "Bienvenido al consulado. ¿En qué le puedo colaborar?"},
                    {"speaker": "Ciudadano", "text": "_____"},
                    {"speaker": "Secretaria", "text": "Con mucho gusto, tome asiento mientras reviso el expediente."}
                ],
                "options": [
                    "Venía a consultar los requisitos para la renovación del pasaporte.",
                    "El año pasado renové la cédula en mi ciudad natal.",
                    "Los pasaportes caducan invariablemente cada cinco o diez años."
                ],
                "correct": 0,
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Titubeó unos segundos porque no pretendía incomodar a los miembros del comité.",
                "english": "He hesitated a few seconds because he did not intend to inconvenience the committee members.",
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=2,
        title="Pragmatic Imperfect: Politeness & Nuance",
        goal="Employ the imperfect of politeness, imminent action, and planning to navigate high-register interpersonal exchanges in Latin America.",
        grammar_desc="usos pragmáticos, corteses y estilísticos del imperfecto",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Soften requests and inquiries with the imperfect of politeness (imperfecto de cortesía).",
            "Narrate close-call events that almost occurred with conative imperfect (por poco me caía).",
            "Master B2 vocabulary of deference, tact, and subtle intention."
        ]
    ))

    # --------------------------------------------------------------------------
    # Story: stories/classics/b2/b2-02.json (Juan Rulfo: Pedro Páramo / Luvina)
    # --------------------------------------------------------------------------
    write_json("stories/classics/b2/b2-02.json", {
        "id": "story.b2.02.rulfo",
        "title": "Juan Rulfo: Los murmullos de Comala y el tiempo suspendido",
        "level": "B2",
        "author": "Juan Rulfo (México, 1917–1986)",
        "work": "Pedro Páramo / El llano en llamas",
        "summary": "Una inmersión en la poética del tiempo de Juan Rulfo, donde el pasado no ha pasado, los muertos conversan desde las tumbas y el aspecto verbal articula una atmósfera de eternidad y desolación.",
        "vocabularyTopics": ["Narrativa mexicana", "Atmósfera y duelo", "El tiempo suspendido"],
        "grammar": ["contraste indefinido-imperfecto", "pluscuamperfecto retrospectivo"],
        "paragraphs": [
            {
                "text": "Fui a Comala porque me dijeron que acá vivía mi padre, un tal Pedro Páramo. Mi madre me lo había dicho en su lecho de muerte, y yo le prometí que vendría a verlo en cuanto ella muriera. Le apreté sus manos en señal de que lo haría, pues ella estaba por morir y yo en un plan de prometerlo todo.",
                "english": "I came to Comala because I was told my father lived here, a certain Pedro Páramo. My mother had told me so on her deathbed, and I promised her I would come see him as soon as she died. I squeezed her hands as a sign that I would, for she was about to die and I was in a frame of mind to promise anything."
            },
            {
                "text": "El calor era sofocante cuando descendí por la cuesta de Los Encuentros. Traía los ojos llenos de polvo y en la garganta se me había atorado una sed amarga. En el camino me topé con un arriero que conducía una hilera de burros. Le pregunté por Pedro Páramo y él se me quedó mirando fijamente antes de responder: 'Pedro Páramo murió hace muchos años'.",
                "english": "The heat was suffocating when I descended down the slope of Los Encuentros. My eyes were full of dust and in my throat a bitter thirst had lodged. On the road I came across a muleteer driving a line of donkeys. I asked him about Pedro Páramo and he stared at me intently before replying: 'Pedro Páramo died many years ago'."
            },
            {
                "text": "En Comala no había ruidos. Aquel pueblo parecía fundado sobre el eco de voces pretéritas. Las casas tenían las puertas desvencijadas y por las rendijas soplaba un aire tibio que olía a tierra quemada. Apenas oscureció, comprendí que los pasos que escuchaba no pertenecían a los vivos, sino a las ánimas que penaban por los callejones.",
                "english": "In Comala there were no sounds. That village seemed founded upon the echo of past voices. The houses had rickety doors and through the chinks blew a warm air that smelled of scorched earth. Barely had it grown dark when I understood that the footsteps I heard did not belong to the living, but to souls suffering penance through the alleys."
            },
            {
                "text": "Rulfo revolucionó la literatura hispanoamericana porque disolvió la frontera entre el presente del relato y el pasado remoto. En su universo, el pluscuamperfecto y el imperfecto conviven en una quietud intemporal donde los recuerdos pesan más que la carne, consagrando al autor jalisciense como una cumbre insoslayable del canon universal.",
                "english": "Rulfo revolutionized Spanish-American literature because he dissolved the boundary between the tale's present and the remote past. In his universe, the pluperfect and the imperfect coexist in a timeless stillness where memories weigh more than flesh, establishing the author from Jalisco as an inescapable peak of the universal canon."
            }
        ]
    })

    # --------------------------------------------------------------------------
    # Lesson 6: b2-02-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-02-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la penumbra", "gloom, half-light"],
                    ["el desenlace", "outcome, ending"],
                    ["súbitamente", "suddenly"],
                    ["el conato", "attempt, slight outbreak"]
                ],
                "teaches": ["b2-unit02-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según el texto sobre Comala, ¿qué descubre el narrador poco después de llegar al pueblo?",
                "options": [
                    "Que su padre, Pedro Páramo, ya había muerto hace muchos años y el pueblo está habitado por ánimas.",
                    "Que su madre todavía lo esperaba con vida en la casa parroquial.",
                    "Que el pueblo estaba prosperando gracias a la minería y el comercio fluvial."
                ],
                "correct": 0
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la frase 'Supimos la noticia cuando ya todos se habían marchado', ¿qué expresan respectivamente 'supimos' y 'habían marchado'?",
                "options": [
                    "'Supimos' marca enterarse en ese momento puntual; 'habían marchado' marca una acción previa completada.",
                    "'Supimos' describe una acción habitual; 'habían marchado' indica una acción que casi ocurrió.",
                    "Ambos verbos expresan acciones simultáneas en el presente de la narración."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-significado-pasado", "pluscuamperfecto-retrospectiva"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No bien __ el último acorde, la sala entera se puso de pie con entusiasmo. (sonar)",
                "answer": "sonó",
                "english": "No sooner did the final chord sound than the entire hall rose to its feet enthusiastically.",
                "teaches": ["conectores-temporales-pasado"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Amanecía cuando el forastero divisó las primeras casas del pueblo. [It was dawning when the stranger caught sight of the village's first houses.]",
                    "Apenas cruzó el umbral, advirtió que la casa había permanecido cerrada durante años. [Barely had he crossed the threshold when he noticed that the house had remained closed for years.]",
                    "El guía no quiso acompañarlo más allá del cementerio abandonado. [The guide refused to accompany him beyond the abandoned cemetery.]",
                    "Al cabo de varias horas de búsqueda infructuosa, decidió retirarse. [After several hours of fruitless search, he decided to withdraw.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo", "conectores-temporales-pasado"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Profesor", "text": "¿Por qué es tan impactante la prosa de Juan Rulfo en 'Pedro Páramo'?"},
                    {"speaker": "Estudiante", "text": "_____"},
                    {"speaker": "Profesor", "text": "Exacto: la ambigüedad temporal es la esencia de su estética."}
                ],
                "options": [
                    "Porque disolvió las fronteras temporales usando el imperfecto y el pluscuamperfecto para suspender el tiempo.",
                    "Porque describe con mucho detalle las leyes mercantiles del México virreinal.",
                    "Porque todos los capítulos están redactados exclusivamente en presente de indicativo."
                ],
                "correct": 0,
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "El viento soplaba entre las ruinas y nadie supo jamás qué destino tuvieron aquellos pobladores.",
                "english": "The wind blew among the ruins and no one ever found out what destiny those inhabitants met.",
                "teaches": ["verbos-cambio-significado-pasado"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Escribe una frase narrativa que contemple una acción en primer plano (indefinido) sobre un fondo sensorial (imperfecto), usando el conector 'apenas'.",
                        "answer": "Apenas oscureció, un frío intenso invadió las habitaciones desoladas de la hacienda."
                    }
                ],
                "teaches": ["pret-indefinido-vs-imperfecto-narrativo", "conectores-temporales-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=2,
        title="Unit 2 Consolidation",
        goal="Consolidate narrative aspect (indefinido vs imperfecto), the pluperfect in flashbacks, aspectual verb shifts, and advanced temporal connectors.",
        grammar_desc="síntesis de tiempo y aspecto narrativo en el relato",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Synthesize narrative pacing using the contrast of preterite and imperfect.",
            "Deploy the pluperfect to build multi-layered retrospective depths.",
            "Accurately master aspectual verb shifts and nuanced temporal conjunctions.",
            "Analyze literary excerpts from Juan Rulfo's Comala cycle."
        ],
        checklist_items=[
            "I can contrast the preterite and imperfect to structure foreground and background in stories.",
            "I can use the pluperfect indicative to integrate flashbacks and retrospective revelations.",
            "I can employ saber, conocer, querer, and poder with their exact aspectual meanings in the past.",
            "I can control the rhythm and suspense of narrative prose with temporal connectors."
        ],
        story_ref="stories/classics/b2/b2-02.json"
    ))
    print("Completed Core Unit 2 generation!")


if __name__ == "__main__":
    generate_core_unit_2()
