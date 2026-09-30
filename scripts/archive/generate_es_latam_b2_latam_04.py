#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Latin America Regional Studies Unit 4:
  - Title: "Guatemala: Mayan Heritage, Highland Communities & Modern Transitions"
    (Guatemala: Herencia maya, comunidades del altiplano y transiciones modernas)
  - Stems: b2-guatemala-01 through b2-guatemala-consolidation
  - Cultural Focus: Tikal & Petén biosphere, Popol Vuh & K'iche' cosmogony,
    Antigua seismic baroque, Rigoberta Menchú & historical memory (CEH),
    highland coffee, Lake Atitlán & the 48 Cantones of Totonicapán.
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_latam_unit_4():
    # Vocab theme slug: b2-guatemala-vocab
    # Grammar skills:
    #   - pasiva-analitica-geografia
    #   - temporales-antes-despues-que
    #   - concesivas-historicas-si-bien
    #   - estilo-indirecto-testimonios

    # --------------------------------------------------------------------------
    # Lesson 1: b2-guatemala-01 - Tikal y el Petén: La gran civilización clásica
    # --------------------------------------------------------------------------
    l1 = "b2-guatemala-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.guatemala.01",
        "lesson": l1,
        "title": "Arqueología y selva petenera",
        "theme": "Urbanismo maya clásico, estelas y biosfera del Petén",
        "words": [
            {"lemma": "el yacimiento", "translation": "archaeological site", "pos": "noun"},
            {"lemma": "el basamento", "translation": "plinth, pyramid base", "pos": "noun"},
            {"lemma": "la acrópolis", "translation": "acropolis", "pos": "noun"},
            {"lemma": "el dintel", "translation": "lintel (carved wooden or stone)", "pos": "noun"},
            {"lemma": "erigir", "translation": "to erect, to raise", "pos": "verb"},
            {"lemma": "el estucado", "translation": "stucco work", "pos": "noun"},
            {"lemma": "la calzada", "translation": "causeway, ceremonial avenue", "pos": "noun"},
            {"lemma": "la biosfera", "translation": "biosphere", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.guatemala.01.pasiva-analitica",
        "title": "Pasiva analítica con 'ser' y complemento agente en textos históricos",
        "sections": [
            {
                "type": "text",
                "title": "Estructura y función en la prosa formal histórica y geográfica",
                "content": "La voz pasiva analítica ('ser' + participio concertado en género y número + 'por' + complemento agente) es un recurso estilístico clave del registro formal B2. A diferencia del habla coloquial (que prefiere la pasiva refleja con 'se'), en los textos de historia, antropología y geografía la pasiva analítica permite focalizar el objeto monumental o el hecho histórico mientras se identifica con precisión el agente causal: 'El Templo del Gran Jaguar fue erigido por el soberano Jasaw Chan K'awiil I'."
            },
            {
                "type": "table",
                "title": "Tiempos verbales frecuentes de la pasiva analítica",
                "rows": [
                    ["Pretérito indefinido", "'La ciudad de Tikal fue redescubierta por expedicionarios en 1848.'"],
                    ["Pretérito imperfecto", "'Las calzadas eran transitadas por peregrinos y comerciantes de toda Mesoamérica.'"],
                    ["Pretérito pluscuamperfecto", "'El sitio ya había sido abandonado por sus habitantes antes del siglo X.'"],
                    ["Presente histórico", "'La Reserva de la Biosfera Maya es gestionada por comunidades forestales locales.'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la arqueología de Guatemala",
                "items": [
                    {"spanish": "Los monumentales dinteles de madera de zapote fueron tallados por artesanos mayas.", "english": "The monumental sapodilla wood lintels were carved by Mayan craftsmen."},
                    {"spanish": "La majestuosa Acrópolis Norte fue modificada a lo largo de varios siglos por sucesivas dinastías.", "english": "The majestic North Acropolis was modified over several centuries by successive dynasties."},
                    {"spanish": "Las extensas áreas de selva son resguardadas por concesiones comunitarias sostenibles.", "english": "The extensive areas of jungle are safeguarded by sustainable community concessions."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que el participio pasivo debe concordar siempre en género y número con el sujeto paciente: 'Las estelas fueron esculpidas', 'Los templos fueron construidos'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l1}.json", {
        "id": f"story.b2.{l1}",
        "title": "Ecos del Petén: El renacimiento del Gran Jaguar",
        "level": "B2",
        "author": "Arqueología y Selva Maya",
        "summary": "Una travesía por el Parque Nacional Tikal, el poderío de la dinastía K'awiil y el rescate de la selva petenera a través de concesiones forestales comunitarias.",
        "vocabularyTopics": ["Arqueología maya", "Urbanismo prehispánico", "Conservación del Petén"],
        "grammar": ["pasiva analítica con ser", "concordancia del participio"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el corazón del departamento de Petén, emergiendo por encima del dosel arbóreo de la selva tropical, las crestas del Templo I y el Templo II de Tikal vigilan la inmensidad verde. Durante el período clásico mesoamericano, esta urbe dominó amplias rutas comerciales y alianzas geopolíticas que se extendían desde el Altiplano mexicano hasta el golfo de Honduras."
            },
            {
                "type": "narration",
                "text": "Los complejos arquitectónicos de Tikal fueron erigidos por arquitectos e ingenieros mayas que transformaron el terreno kárstico en un sofisticado sistema de acrópolis, plazas ceremoniales y embalses hidráulicos capaces de recolectar millones de litros de agua pluvial durante los meses de sequía."
            },
            {
                "type": "narration",
                "text": "Hoy en día, las ruinas no están solas en medio del silencio; la Reserva de la Biosfera Maya es resguardada activamente por comunidades campesinas e indígenas que combinan la conservación ecológica con el manejo forestal sostenible, demostrando que el legado de Tikal sigue vivo en la custodia colectiva del bosque."
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
                    ["el yacimiento", "archaeological site"],
                    ["el basamento", "pyramid base, plinth"],
                    ["el dintel", "carved lintel"],
                    ["la calzada", "causeway, ceremonial avenue"]
                ],
                "teaches": ["b2-guatemala-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la función del complemento introducido por 'por' en 'Las estelas fueron esculpidas por artesanos de la corte real'?",
                "options": [
                    "Complemento agente: identifica quién realizó la acción en la estructura pasiva.",
                    "Complemento circunstancial de causa que explica por qué se tallaron las estelas.",
                    "Complemento indirecto que designa a los destinatarios de los monumentos."
                ],
                "correct": 0,
                "teaches": ["pasiva-analitica-geografia"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las pirámides gemelas de Tikal __ erigidas por el gobernante Jasaw Chan K'awiil. (ser - pretérito indefinido)",
                "answer": "fueron",
                "english": "The twin pyramids of Tikal were erected by ruler Jasaw Chan K'awiil.",
                "teaches": ["pasiva-analitica-geografia"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "templos", "fueron", "restaurados", "por", "arqueólogos", "guatemaltecos."],
                "solution": ["Los", "templos", "fueron", "restaurados", "por", "arqueólogos", "guatemaltecos."],
                "english": "The temples were restored by Guatemalan archaeologists.",
                "teaches": ["pasiva-analitica-geografia"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora", "text": "¿Cómo se estructuró la expansión política de Tikal durante el período clásico tardío?"},
                    {"speaker": "Arqueólogo", "text": "_____"},
                    {"speaker": "Historiadora", "text": "Eso explica la monumentalidad de las calzadas y complejos ceremoniales."}
                ],
                "options": [
                    "Las rutas de comercio fueron consolidadas por gobernantes dinásticos mediante alianzas militares estratégicas.",
                    "El hotel del parque nacional cuenta con restaurante y transporte turístico.",
                    "El café guatemalteco se cultiva en laderas volcánicas por encima de los mil metros."
                ],
                "correct": 0,
                "teaches": ["pasiva-analitica-geografia"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La biosfera petenera es protegida por comunidades organizadas que gestionan los recursos forestales.",
                "english": "The Petén biosphere is protected by organized communities that manage forest resources.",
                "teaches": ["pasiva-analitica-geografia"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=4,
        title="Tikal y el Petén: La gran civilización clásica",
        goal="Analyze classical Mayan urbanism, architecture, and rainforest conservation in El Petén using analytical passive voice.",
        grammar_desc="la voz pasiva analítica con 'ser' y complemento agente en el discurso histórico",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Describe the architectural layout, water management, and monumental art of Tikal.",
            "Examine modern community forest management in the Maya Biosphere Reserve.",
            "Construct analytical passive sentences with gender and number participle agreement."
        ],
        story_ref=f"stories/world/b2/{l1}.json",
        intro_body=[
            "Welcome to Unit 4 of Latin American Regional Studies: Guatemala: Mayan Heritage, Highland Communities & Modern Transitions. Guatemala stands as the cultural core of the ancient Maya world and the heartland of Central America.",
            "In this lesson, we explore the monumental ruins of Tikal, the vast biodiversity of El Petén, and the historical use of the analytical passive voice ('ser' + participle + 'por') in archaeological and historical accounts."
        ],
        intro_title="Unit 4: Guatemala: Mayan Heritage, Highland Communities & Modern Transitions"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-guatemala-02 - El Popol Vuh y el Altiplano: La creación y el maíz
    # --------------------------------------------------------------------------
    l2 = "b2-guatemala-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.guatemala.02",
        "lesson": l2,
        "title": "Cosmovisión maya y el Popol Vuh",
        "theme": "Mitología k'iche', narrativa cosmogónica y el ciclo sagrado del maíz",
        "words": [
            {"lemma": "el relato fundacional", "translation": "foundational narrative", "pos": "noun"},
            {"lemma": "el maíz", "translation": "corn, maize", "pos": "noun"},
            {"lemma": "la deidad", "translation": "deity", "pos": "noun"},
            {"lemma": "el linaje", "translation": "lineage, ancestry", "pos": "noun"},
            {"lemma": "el inframundo", "translation": "underworld (Xibalbá)", "pos": "noun"},
            {"lemma": "esculpir", "translation": "to sculpt, to carve", "pos": "verb"},
            {"lemma": "la gestación", "translation": "gestation, genesis", "pos": "noun"},
            {"lemma": "el barro", "translation": "clay, mud", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.guatemala.02.temporales-antes-despues",
        "title": "Subordinadas temporales con antes de que y después de que",
        "sections": [
            {
                "type": "text",
                "title": "Reglas de modo en oraciones de anterioridad y posterioridad",
                "content": "En la narración mitológica e histórica de nivel B2, las conjunciones temporales exigen una rigurosa selección modal. La locución 'antes de que' rige obligatoriamente subjuntivo en todos los tiempos y contextos (incluso en el pasado), porque la acción temporalizada se concibe como no realizada en el punto de referencia temporal: 'Los dioses hicieron tres intentos antes de que lograran crear a los hombres de maíz'. Por el contrario, 'después de que' rige indicativo si la acción ya se consumó en el pasado, o subjuntivo si se proyecta hacia el futuro."
            },
            {
                "type": "table",
                "title": "Contraste modal con nexos temporales",
                "rows": [
                    ["antes de que + SUBJUNTIVO (siempre)", "'Antes de que amaneciera, los Procreadores se reunieron en consejo.'"],
                    ["después de que + INDICATIVO (hecho consumado)", "'Después de que derrotaron a los señores de Xibalbá, los gemelos ascendieron al cielo.'"],
                    ["después de que + SUBJUNTIVO (acción futura o hipotética)", "'Celebraremos la cosecha después de que las lluvias cesen.'"],
                    ["en cuanto / tan pronto como + INDICATIVO o SUBJUNTIVO", "Indicativo para rutinas/pasado; subjuntivo para futuro: 'En cuanto brota el maíz...'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el Popol Vuh",
                "items": [
                    {"spanish": "Antes de que existiera la luz del sol, los señores del cielo deliberaban en la oscuridad.", "english": "Before the light of the sun existed, the lords of heaven deliberated in the darkness."},
                    {"spanish": "Los creadores moldearon figuras de barro antes de que comprendieran la necesidad de la carne de maíz.", "english": "The creators molded clay figures before they understood the necessity of flesh made of corn."},
                    {"spanish": "Después de que Hunahpú e Ixbalanqué triunfaron sobre la muerte, se transformaron en el sol y la luna.", "english": "After Hunahpú and Ixbalanqué triumphed over death, they transformed into the sun and the moon."}
                ]
            },
            {
                "type": "tip",
                "content": "¡Regla de oro!: 'Antes de que' nunca va seguido de indicativo en español culto. Siempre usa presente o imperfecto de subjuntivo según la concordancia temporal."
            }
        ]
    })

    write_json(f"stories/world/b2/{l2}.json", {
        "id": f"story.b2.{l2}",
        "title": "El libro del consejo: Cosmovisión y origen en el Popol Vuh",
        "level": "B2",
        "author": "Literatura Maya K'iche'",
        "summary": "Una aproximación al Popol Vuh, la cosmogonía k'iche' en las tierras altas de Chichicastenango y la creación de los seres humanos a partir de la masa de maíz.",
        "vocabularyTopics": ["Literatura maya", "Mitología mesoamericana", "El ciclo del maíz"],
        "grammar": ["oraciones temporales con antes de que", "subjuntivo en el pasado"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Redactado en lengua k'iche' con caracteres latinos a mediados del siglo dieciséis en Santa Cruz del Quiché, el Popol Vuh —o Libro del Consejo— es una de las obras cumbres del pensamiento universal. En sus páginas iniciales, el texto describe el silencio primordial: antes de que existiera la tierra, los animales o los árboles, solo había inmovilidad y aguas en calma bajo el cielo."
            },
            {
                "type": "narration",
                "text": "Los dioses creadores, Tepeu y Gucumatz, intentaron formar seres que los alabaran y reconocieran su linaje. Primero modelaron criaturas de barro que se deshacían con la lluvia; luego tallaron muñecos de madera que hablaban pero carecían de memoria y gratitud. Ambos ensayos fracasaron antes de que los Procreadores descubrieran el ingrediente sagrado."
            },
            {
                "type": "narration",
                "text": "Fue gracias a los animales que trajeron mazorcas amarillas y blancas desde Paxil y Cayalá que la diosa Ixmukané molió el grano para moldear la carne y los huesos de los primeros cuatro humanos verdaderos. Desde entonces, para los pueblos mayas del altiplano guatemalteco, el maíz no es un simple cultivo agrícola, sino la sustancia viva de su identidad."
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
                    ["el relato fundacional", "foundational narrative"],
                    ["la deidad", "deity"],
                    ["el inframundo", "underworld (Xibalbá)"],
                    ["el linaje", "lineage, ancestry"]
                ],
                "teaches": ["b2-guatemala-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo exige obligatoriamente la locución 'antes de que' en cualquier contexto temporal?",
                "options": [
                    "Subjuntivo, porque la acción temporalizada se concibe como prospectiva o pendiente respecto a la matriz.",
                    "Indicativo, siempre que la acción haya ocurrido comprobadamente en el pasado.",
                    "Condicional simple, para señalar una hipótesis futura."
                ],
                "correct": 0,
                "teaches": ["temporales-antes-despues-que"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los dioses deliberaron largamente antes de que __ a los seres humanos de maíz. (crear - imperfect subjunctive)",
                "answer": "crearan",
                "english": "The gods deliberated at length before they created the human beings of corn.",
                "teaches": ["temporales-antes-despues-que"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Antes", "de", "que", "amaneciera,", "los", "sabios", "iniciaron", "la", "ceremonia."],
                "solution": ["Antes", "de", "que", "amaneciera,", "los", "sabios", "iniciaron", "la", "ceremonia."],
                "english": "Before it dawned, the wise elders began the ceremony.",
                "teaches": ["temporales-antes-despues-que"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Estudiante", "text": "¿Por qué el Popol Vuh concede tanta importancia al maíz como sustancia de los humanos?"},
                    {"speaker": "Profesor de literatura", "text": "_____"},
                    {"speaker": "Estudiante", "text": "Comprendo, simboliza la alianza recíproca entre la naturaleza y la vida."}
                ],
                "options": [
                    "Porque después de que fracasaron con el barro y la madera, el maíz otorgó sabiduría y reverencia a los primeros humanos.",
                    "Porque las calzadas de Tikal eran de piedra caliza blanca pulida.",
                    "Porque el quetzal es el ave nacional que aparece en la bandera guatemalteca."
                ],
                "correct": 0,
                "teaches": ["temporales-antes-despues-que"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Antes de que los sacerdotes recitaran los versos sagrados, la comunidad guardó un respetuoso silencio.",
                "english": "Before the priests recited the sacred verses, the community kept a respectful silence.",
                "teaches": ["temporales-antes-despues-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=4,
        title="El Popol Vuh y el Altiplano: La creación y el maíz",
        goal="Examine Mayan cosmogony, the sacred significance of maize, and K'iche' literary traditions using temporal clauses with 'antes de que' and 'después de que'.",
        grammar_desc="el modo subjuntivo e indicativo en oraciones temporales de anterioridad y posterioridad",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Interpret the cosmogonic narratives of the Popol Vuh and K'iche' mythological structure.",
            "Understand the cultural and spiritual centrality of corn in Mayan highland life.",
            "Apply the strict subjunctive rule after 'antes de que' in past and future narratives."
        ],
        story_ref=f"stories/world/b2/{l2}.json",
        intro_body=[
            "In this second lesson of Unit 4, we climb into the misty highlands of Guatemala to study the greatest literary treasure of the Americas: the Popol Vuh.",
            "Through the creation myth of the humans of corn and the adventures of the Hero Twins in Xibalbá, we analyze the rigorous modal mechanics of temporal connectors ('antes de que' vs 'después de que')."
        ],
        intro_title="The Popol Vuh & Highland Cosmogony"
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-guatemala-03 - Antigua y el barroco sísmico: Resiliencia colonial
    # --------------------------------------------------------------------------
    l3 = "b2-guatemala-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.guatemala.03",
        "lesson": l3,
        "title": "Arquitectura y sismicidad colonial",
        "theme": "Santiago de los Caballeros, barroco sísmico y los terremotos de Santa Marta",
        "words": [
            {"lemma": "el sismo", "translation": "earthquake, seismic tremor", "pos": "noun"},
            {"lemma": "el contrafuerte", "translation": "buttress", "pos": "noun"},
            {"lemma": "la fachada", "translation": "facade", "pos": "noun"},
            {"lemma": "derruir", "translation": "to demolish, to raze, to collapse", "pos": "verb"},
            {"lemma": "el campanario", "translation": "bell tower", "pos": "noun"},
            {"lemma": "la ruina", "translation": "ruin, relic", "pos": "noun"},
            {"lemma": "la orden monástica", "translation": "monastic order", "pos": "noun"},
            {"lemma": "la arcada", "translation": "arcade, series of arches", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.guatemala.03.concesivas-si-bien",
        "title": "Concesivas formales en el discurso histórico: si bien, a pesar de que y pese a que",
        "sections": [
            {
                "type": "text",
                "title": "Contraste y ponderación en registros académicos",
                "content": "Para matizar afirmaciones históricas y arquitectónicas en nivel B2, los nexos concesivos formales 'si bien', 'a pesar de que' y 'pese a que' permiten reconocer un obstáculo, hecho o premisa real sin que este invalide la conclusión principal. El conector 'si bien' rige habitualmente modo indicativo en prosa analítica cuando introduce un hecho probado o admitido: 'Si bien los terremotos de 1773 destruyeron gran parte de los templos, Antigua Guatemala conserva una belleza arquitectónica incomparable'."
            },
            {
                "type": "table",
                "title": "Nexos concesivos de registro culto",
                "rows": [
                    ["si bien + INDICATIVO", "Admite un hecho verídico con matiz formal: 'Si bien la capital fue trasladada, la urbe colonial jamás perdió su vitalidad'"],
                    ["a pesar de que / pese a que + INDICATIVO", "Realidad fáctica comprobada: 'A pesar de que las murallas colapsaron, los contrafuertes resistieron'"],
                    ["a pesar de que / pese a que + SUBJUNTIVO", "Hipótesis o indiferencia epistémica: 'Pese a que ocurran nuevos sismos, la estructura barroca es sólida'"],
                    ["por más que / por mucho que", "Intensidad máxima del obstáculo: 'Por más que intentaron reconstruirla en el mismo valle, se ordenó el traslado'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la arquitectura de Antigua",
                "items": [
                    {"spanish": "Si bien la ciudad fue abandonada como sede del gobierno virreinal, numerosos conventos continuaron habitados.", "english": "Although the city was abandoned as seat of viceregal government, numerous convents continued to be inhabited."},
                    {"spanish": "Pese a que los temblores derruyeron los campanarios, los gruesos muros de mampostería permanecieron erguidos.", "english": "Even though tremors demolished the bell towers, the thick masonry walls remained upright."},
                    {"spanish": "A pesar de que el agua subterránea desgasta las bases, las arcadas coloniales se mantienen en pie.", "english": "Despite the fact that underground water wears away the foundations, the colonial arcades remain standing."}
                ]
            },
            {
                "type": "tip",
                "content": "'Si bien' se utiliza exclusivamente al inicio de oración o de proposición subordinada con indicativo; nunca rige subjuntivo en español formal."
            }
        ]
    })

    write_json(f"stories/world/b2/{l3}.json", {
        "id": f"story.b2.{l3}",
        "title": "Piedra y ceniza: El barroco sísmico de Antigua Guatemala",
        "level": "B2",
        "author": "Historia y Arquitectura Colonial",
        "summary": "La historia de Santiago de los Caballeros de Guatemala, el surgimiento del barroco sísmico ante las sacudidas telúricas y la mudanza forzada tras los terremotos de Santa Marta en 1773.",
        "vocabularyTopics": ["Urbanismo colonial", "Barroco hispanoamericano", "Riesgo volcánico y sísmico"],
        "grammar": ["concesivas con si bien y a pesar de que", "léxico arquitectónico especializado"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Custodiada por los volcanes de Agua, Fuego y Acatenango en el valle de Panchoy, la ciudad de Santiago de los Caballeros —actualmente Antigua Guatemala— fungió durante más de dos siglos como la floreciente capital de la Capitanía General de Guatemala, un vasto territorio que abarcaba desde Chiapas hasta Costa Rica."
            },
            {
                "type": "narration",
                "text": "Los alarifes y constructores coloniales debieron enfrentarse a la implacable actividad telúrica del cinturón de fuego. Como respuesta creativa, desarrollaron el célebre 'barroco sísmico': templos con muros de hasta tres metros de espesor, torres campanario rechonchas y monumentales contrafuertes laterales diseñados para disipar la energía de los terremotos."
            },
            {
                "type": "narration",
                "text": "Si bien los catastróficos sismos de Santa Marta en 1773 llevaron a la corona a ordenar el traslado definitivo de la capital a la actual Nueva Guatemala de la Asunción, Antigua se negó a morir. Sus conventos en ruinas, silenciosos claustros y calles empedradas ofrecen hoy uno de los testimonios más sobrecogedores de la resiliencia humana frente a las fuerzas de la naturaleza."
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
                    ["el sismo", "earthquake, seismic tremor"],
                    ["el contrafuerte", "buttress"],
                    ["derruir", "to demolish, to raze"],
                    ["la arcada", "arcade, series of arches"]
                ],
                "teaches": ["b2-guatemala-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo verbal sigue habitualmente a la locución concesiva 'si bien' en la prosa analítica?",
                "options": [
                    "Modo indicativo, porque introduce un hecho verificado o concedido como premisa real.",
                    "Modo subjuntivo, porque siempre denota duda y rechazo epistémico.",
                    "Modo imperativo, porque transmite una instrucción técnica."
                ],
                "correct": 0,
                "teaches": ["concesivas-historicas-si-bien"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si bien los terremotos de Santa Marta __ gran parte de la urbe, los claustros monásticos conservaron su encanto. (destruir - pretérito indefinido)",
                "answer": "destruyeron",
                "english": "Although the Santa Marta earthquakes destroyed a large part of the city, the monastic cloisters preserved their charm.",
                "teaches": ["concesivas-historicas-si-bien"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "pesar", "de", "que", "hubo", "sismos,", "los", "muros", "resistieron."],
                "solution": ["A", "pesar", "de", "que", "hubo", "sismos,", "los", "muros", "resistieron."],
                "english": "Despite the fact that there were earthquakes, the walls resisted.",
                "teaches": ["concesivas-historicas-si-bien"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Turista", "text": "¿Por qué las iglesias de Antigua Guatemala tienen torres tan bajas y muros tan anchos?"},
                    {"speaker": "Guía local", "text": "_____"},
                    {"speaker": "Turista", "text": "Es una arquitectura verdaderamente nacida de la necesidad de sobrevivir."}
                ],
                "options": [
                    "Si bien el barroco europeo buscaba gran elevación, aquí los arquitectos adaptaron las formas para resistir constantes terremotos.",
                    "El lago de Atitlán se encuentra a unos setenta kilómetros hacia el occidente.",
                    "En los telares tradicionales de Totonicapán se emplean hilos teñidos naturalmente."
                ],
                "correct": 0,
                "teaches": ["concesivas-historicas-si-bien"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Pese a que la corona ordenó desalojar la ciudad, muchas familias se quedaron entre las ruinas barrocas.",
                "english": "Even though the crown ordered the evacuation of the city, many families remained among the baroque ruins.",
                "teaches": ["concesivas-historicas-si-bien"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=4,
        title="Antigua y el barroco sísmico: Resiliencia colonial",
        goal="Analyze colonial Latin American architecture, urbanism, and seismic adaptation in Antigua Guatemala using formal concessive clauses.",
        grammar_desc="nexos concesivos formales ('si bien', 'a pesar de que', 'pese a que') en el análisis histórico",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Understand the architectural concepts of seismic baroque and masonry engineering in Santiago de Guatemala.",
            "Analyze the historical consequences of the 1773 Santa Marta earthquakes and the capital's relocation.",
            "Deploy formal concessive clauses ('si bien' + indicative) to balance competing historical facts."
        ],
        story_ref=f"stories/world/b2/{l3}.json",
        intro_body=[
            "In this third lesson, we walk through the cobblestone streets and evocative ruins of Antigua Guatemala.",
            "We examine how indigenous and Spanish builders developed 'seismic baroque' architecture to survive frequent tremors, while mastering sophisticated concessive structures ('si bien', 'a pesar de que', 'pese a que')."
        ],
        intro_title="Antigua & Seismic Baroque Resilience"
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-guatemala-04 - Conflicto armado y memoria: La voz testimonial
    # --------------------------------------------------------------------------
    l4 = "b2-guatemala-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.guatemala.04",
        "lesson": l4,
        "title": "Memoria histórica y derechos humanos",
        "theme": "Conflicto armado interno, Rigoberta Menchú y la Comisión para el Esclarecimiento Histórico",
        "words": [
            {"lemma": "el testimonio", "translation": "testimony, witness account", "pos": "noun"},
            {"lemma": "el esclarecimiento", "translation": "clarification, shedding of light", "pos": "noun"},
            {"lemma": "el resarcimiento", "translation": "reparation, redress", "pos": "noun"},
            {"lemma": "la impunidad", "translation": "impunity", "pos": "noun"},
            {"lemma": "reivindicar", "translation": "to claim, to demand rights", "pos": "verb"},
            {"lemma": "la pacificación", "translation": "pacification, peace process", "pos": "noun"},
            {"lemma": "la concordia", "translation": "harmony, concord", "pos": "noun"},
            {"lemma": "el genocidio", "translation": "genocide", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.guatemala.04.estilo-indirecto",
        "title": "Estilo indirecto y correlación de tiempos en testimonios y memoria",
        "sections": [
            {
                "type": "text",
                "title": "Transformación de citas directas en discurso testimonial reportado",
                "content": "El relato testimonial y la documentación de derechos humanos en nivel B2 requieren un dominio riguroso de la correlación de tiempos en estilo indirecto. Cuando el verbo de habla o reporte está en pasado ('declaró', 'afirmó', 'denunció'), las oraciones subordinadas adaptan sus tiempos verbales: el presente pasa a pretérito imperfecto, el pretérito o presente perfecto pasan a pretérito pluscuamperfecto, y el futuro simple pasa a condicional simple."
            },
            {
                "type": "table",
                "title": "Tabla de correlación temporal en estilo indirecto (matriz en pasado)",
                "rows": [
                    ["Discurso directo: Presente", "Estilo indirecto: Pretérito imperfecto: 'Ella dijo: Vivo con miedo' -> 'Ella dijo que vivía con miedo'"],
                    ["Discurso directo: Pretérito / Perfecto", "Estilo indirecto: Pretérito pluscuamperfecto: 'El testigo afirmó: Escuché disparos' -> 'El testigo afirmó que había escuchado disparos'"],
                    ["Discurso directo: Futuro", "Estilo indirecto: Condicional simple: 'Prometieron: Esclareceremos los hechos' -> 'Prometieron que esclarecerían los hechos'"],
                    ["Discurso directo: Imperativo / Subjuntivo", "Estilo indirecto: Pretérito imperfecto de subjuntivo: 'Exigió: ¡Abran los archivos!' -> 'Exigió que abrieran los archivos'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el informe de memoria histórica 'Guatemala: Memoria del Silencio'",
                "items": [
                    {"spanish": "Los testigos manifestaron que habían abandonado sus aldeas durante los operativos militares.", "english": "The witnesses declared that they had abandoned their villages during the military operations."},
                    {"spanish": "La activista denunció que las autoridades judiciales no investigaban los crímenes cometidos.", "english": "The activist denounced that judicial authorities were not investigating the crimes committed."},
                    {"spanish": "El informe concluyó que el Estado reconocería la dignidad de las comunidades afectadas.", "english": "The report concluded that the State would recognize the dignity of the affected communities."}
                ]
            },
            {
                "type": "tip",
                "content": "No olvides cambiar también los pronombres personales, posesivos y demostrativos: 'este lugar' -> 'aquel lugar', 'hoy' -> 'aquel día', 'aquí' -> 'allí'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l4}.json", {
        "id": f"story.b2.{l4}",
        "title": "Memoria del silencio: Testimonio y dignidad en Guatemala",
        "level": "B2",
        "author": "Memoria Histórica y Derechos Humanos",
        "summary": "Una reflexión sobre las tres décadas y media del conflicto armado guatemalteco, la voz de Rigoberta Menchú y las conclusiones de la Comisión para el Esclarecimiento Histórico.",
        "vocabularyTopics": ["Conflicto armado interno", "Testimonio y memoria", "Acuerdos de paz de 1996"],
        "grammar": ["estilo indirecto con matriz en pasado", "correlación de tiempos verbales"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Entre 1960 y 1996, Guatemala atravesó un doloroso conflicto armado interno que dejó más de doscientas mil personas muertas o desaparecidas, afectando de manera desproporcionada y sistemática a las comunidades mayas del altiplano occidental, particularmente en las regiones de Quiché, Huehuetenango y las Verapaces."
            },
            {
                "type": "narration",
                "text": "En 1983, la publicación del testimonio 'Me llamo Rigoberta Menchú y así me nació la conciencia' rompió el cerco del aislamiento internacional. Menchú narró con dolor y lucidez la persecución sufrida por su familia campesina, demostrando que su voz individual encarnaba el clamor colectivo de millones de indígenas despojados de sus derechos elementales, labor que le valió el Premio Nobel de la Paz en 1992."
            },
            {
                "type": "narration",
                "text": "Tras la firma de los Acuerdos de Paz en 1996, la Comisión para el Esclarecimiento Histórico (CEH) presentó su emblemático informe 'Guatemala: Memoria del Silencio'. Los comisionados declararon que el esclarecimiento de la verdad era el único cimiento posible para evitar la repetición y reconstruir el tejido de concordia democrática en una sociedad plural."
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
                    ["el testimonio", "testimony, witness account"],
                    ["el esclarecimiento", "clarification, shedding of light"],
                    ["el resarcimiento", "reparation, redress"],
                    ["la impunidad", "impunity"]
                ],
                "teaches": ["b2-guatemala-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se transforma al estilo indirecto la declaración 'El testigo dijo: No vi a los atacantes' si la matriz está en pasado?",
                "options": [
                    "El testigo dijo que no había visto a los atacantes.",
                    "El testigo dijo que no ve a los atacantes.",
                    "El testigo dijo que no verá a los atacantes."
                ],
                "correct": 0,
                "teaches": ["estilo-indirecto-testimonios"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La lideresa comunitaria afirmó que las víctimas __ justicia y resarcimiento moral. (exigir - pretérito imperfecto)",
                "answer": "exigían",
                "english": "The community leader stated that the victims were demanding justice and moral redress.",
                "teaches": ["estilo-indirecto-testimonios"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "comisionados", "afirmaron", "que", "habían", "escuchado", "miles", "de", "testimonios."],
                "solution": ["Los", "comisionados", "afirmaron", "que", "habían", "escuchado", "miles", "de", "testimonios."],
                "english": "The commissioners stated that they had heard thousands of testimonies.",
                "teaches": ["estilo-indirecto-testimonios"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Qué concluyó el informe de la comisión de la verdad en su comparecencia pública?"},
                    {"speaker": "Abogada de derechos humanos", "text": "_____"},
                    {"speaker": "Periodista", "text": "Es un documento fundamental para cerrar las heridas históricas del país."}
                ],
                "options": [
                    "Manifestaron que el Estado debía reparar integralmente a las comunidades afectadas por el conflicto.",
                    "Las semillas de cacao se utilizaban como moneda en el período clásico.",
                    "El volcán de Fuego permanece en actividad eruptiva intermitente."
                ],
                "correct": 0,
                "teaches": ["estilo-indirecto-testimonios"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Rigoberta Menchú afirmó que la memoria de los pueblos originarios no podía ser silenciada por el miedo.",
                "english": "Rigoberta Menchú stated that the memory of indigenous peoples could not be silenced by fear.",
                "teaches": ["estilo-indirecto-testimonios"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=4,
        title="Conflicto armado y memoria: La voz testimonial",
        goal="Analyze human rights documentation, historical memory, and testimonial literature in Guatemala using reported speech transformations.",
        grammar_desc="el estilo indirecto y la correlación de tiempos verbales en el relato testimonial",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Understand the impact of Guatemala's internal armed conflict (1960–1996) and the 1996 Peace Accords.",
            "Examine Rigoberta Menchú's testimony and the findings of the Historical Clarification Commission (CEH).",
            "Master tense shifting in indirect discourse with past-tense reporting verbs."
        ],
        story_ref=f"stories/world/b2/{l4}.json",
        intro_body=[
            "Lesson 4 addresses one of the most critical chapters of modern Central American history: Guatemala's internal armed conflict and the heroic struggle for historical memory.",
            "We examine the testimonial genre pioneered by Rigoberta Menchú and the landmark 'Memoria del Silencio' report, focusing on reported speech transformations and tense correlation in documentary analysis."
        ],
        intro_title="Armed Conflict, Testimony & Historical Memory"
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-guatemala-05 - Café, Atitlán y los 48 Cantones: Tradición y gobierno comunal
    # --------------------------------------------------------------------------
    l5 = "b2-guatemala-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.guatemala.05",
        "lesson": l5,
        "title": "Economía agraria y gobierno comunal",
        "theme": "Caficultura de altura, Lago Atitlán y las autoridades indígenas de Totonicapán",
        "words": [
            {"lemma": "el grano de oro", "translation": "golden bean (coffee)", "pos": "noun"},
            {"lemma": "el minifundio", "translation": "smallholding, small family farm", "pos": "noun"},
            {"lemma": "la comunalidad", "translation": "communality, collective governance", "pos": "noun"},
            {"lemma": "el cantón", "translation": "canton, community subdivision", "pos": "noun"},
            {"lemma": "la cuenca endorreica", "translation": "endorheic basin, closed drainage basin", "pos": "noun"},
            {"lemma": "el tejido de cintura", "translation": "backstrap weaving", "pos": "noun"},
            {"lemma": "la vara edilicia", "translation": "staff of civic/indigenous authority", "pos": "noun"},
            {"lemma": "la soberanía alimentaria", "translation": "food sovereignty", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.guatemala.05.integracion-discurso-comunal",
        "title": "Integración discursiva: Estructuras pasivas, causales y concesivas en la crónica social",
        "sections": [
            {
                "type": "text",
                "title": "Síntesis de recursos gramaticales para la crónica regional",
                "content": "La crónica sociopolítica y etnográfica de nivel B2 combina la voz pasiva (para registrar acuerdos y resoluciones institucionales), los nexos temporales (para ordenar procesos asamblearios) y las estructuras concesivas (para contraponer presiones externas con resistencia comunitaria). Esta integración permite redactar análisis matizados sobre la gobernanza indígena en los 48 Cantones de Totonicapán y las cooperativas cafetaleras de Atitlán."
            },
            {
                "type": "examples",
                "title": "Modelos sintácticos integrados",
                "items": [
                    {"spanish": "Las decisiones de la asamblea son acatadas por todos los cantones antes de que comiencen las negociaciones con el gobierno central.", "english": "The assembly's decisions are complied with by all cantons before negotiations with the central government begin."},
                    {"spanish": "Si bien el precio internacional del café fluctúa drásticamente, las cooperativas de Atitlán protegen a los pequeños agricultores.", "english": "Although the international price of coffee fluctuates drastically, Atitlán cooperatives protect small farmers."},
                    {"spanish": "Los dirigentes manifestaron que no cederían la custodia de los bosques comunales comunales bajo ninguna circunstancia.", "english": "The leaders stated that they would not yield custody of communal forests under any circumstances."}
                ]
            },
            {
                "type": "tip",
                "content": "Presta atención a los conectores de causa y consecuencia en la argumentación comunal: 'dado que', 'puesto que', 'de ahí que + subjuntivo'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l5}.json", {
        "id": f"story.b2.{l5}",
        "title": "El bastón de mando: Los 48 Cantones y las aguas sagradas de Atitlán",
        "level": "B2",
        "author": "Gobernanza Indígena y Ecosistemas del Altiplano",
        "summary": "Una mirada a la organización política de los 48 Cantones de Totonicapán, el cultivo del café de altura en las laderas volcánicas y la cosmovisión maya alrededor del lago Atitlán.",
        "vocabularyTopics": ["Gobernanza comunal", "Caficultura de altura", "Lago Atitlán"],
        "grammar": ["pasiva analítica", "estilo indirecto", "concesivas de contraste"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Rodeado por los conos perfectos de los volcanes Atitlán, Tolimán y San Pedro, el lago Atitlán constituye una cuenca endorreica de impresionante belleza y honda sacralidad. A sus orillas conviven pueblos tz'utujiles y kaqchikeles cuyos telares de cintura y huipiles tradicionales plasman narrativas identitarias ininterrumpidas desde hace más de un milenio."
            },
            {
                "type": "narration",
                "text": "En las faldas de estos volcanes maduran algunos de los mejores cafés de sombra del mundo. Organizados en cooperativas de comercio justo, los pequeños productores demuestran que la agricultura sostenible y la defensa del bosque de niebla son viables frente a la especulación de los monocultivos de exportación."
            },
            {
                "type": "narration",
                "text": "Más al norte, en Totonicapán, la histórica institución de los 48 Cantones encarna el modelo más sólido de democracia comunitaria de la región. Sus autoridades son electas no por partidos políticos, sino por servicio ad honorem a la colectividad; portan la vara edilicia como símbolo ético y resguardan comunalmente el bosque de pinabete y las fuentes de agua que abastecen a todo el altiplano."
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
                    ["el grano de oro", "golden bean (coffee)"],
                    ["el minifundio", "small family farm"],
                    ["la comunalidad", "collective governance"],
                    ["la vara edilicia", "staff of indigenous authority"]
                ],
                "teaches": ["b2-guatemala-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura refleja con mayor precisión el registro formal de la gobernanza comunal?",
                "options": [
                    "Las fuentes de agua comunales son resguardadas por los guardabosques de los 48 Cantones.",
                    "Los bosques se van a cuidar por los vecinos de la comarca.",
                    "Habían muchos bosques que la gente los cuidaba todos los días."
                ],
                "correct": 0,
                "teaches": ["pasiva-analitica-geografia"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las autoridades comunales convocaron a una asamblea antes de que el congreso __ la ley de aguas. (aprobar - imperfect subjunctive)",
                "answer": "aprobara",
                "english": "Community authorities convened an assembly before Congress passed the water law.",
                "teaches": ["temporales-antes-despues-que"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "caficultores", "afirmaron", "que", "exportarían", "granos", "de", "comercio", "justo."],
                "solution": ["Los", "caficultores", "afirmaron", "que", "exportarían", "granos", "de", "comercio", "justo."],
                "english": "The coffee growers stated that they would export fair-trade beans.",
                "teaches": ["estilo-indirecto-testimonios"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Cómo logran los 48 Cantones mantener una cohesión social tan vigorosa frente al poder central?"},
                    {"speaker": "Investigador maya", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Es un ejemplo extraordinario de democracia directa y soberanía comunitaria."}
                ],
                "options": [
                    "Porque las decisiones se toman por consenso asambleario y las autoridades ejercen su cargo como un servicio honorífico a la comunidad.",
                    "Porque en Tikal se utilizaba la calzada ceremonial durante las fiestas solares.",
                    "Porque las iglesias coloniales tenían gruesos contrafuertes para amortiguar los sismos."
                ],
                "correct": 0,
                "teaches": ["concesivas-historicas-si-bien"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si bien el mercado mundial de materias primas es incierto, las cooperativas de Atitlán garantizan un pago digno.",
                "english": "Although the global commodities market is uncertain, Atitlán cooperatives guarantee fair pay.",
                "teaches": ["concesivas-historicas-si-bien"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=4,
        title="Café, Atitlán y los 48 Cantones: Tradición y gobierno comunal",
        goal="Analyze highland agroecology, fair-trade coffee cooperatives, and indigenous self-governance in Totonicapán using integrated grammatical structures.",
        grammar_desc="integración discursiva de pasivas, subordinadas temporales y concesivas formales",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Examine fair-trade coffee farming and lake basin ecology around Lake Atitlán.",
            "Understand the ancestral political architecture and legitimacy of the 48 Cantones of Totonicapán.",
            "Combine passive voice, temporal subjunctive, and formal concessives in complex sociological prose."
        ],
        story_ref=f"stories/world/b2/{l5}.json",
        intro_body=[
            "Our final topic lesson in Unit 4 focuses on contemporary indigenous society, volcanic agriculture, and community governance in the highlands.",
            "We examine the volcanic coffee of Lake Atitlán and the centuries-old democratic autonomy of the 48 Cantones of Totonicapán, synthesizing the grammatical structures mastered throughout the unit."
        ],
        intro_title="Coffee, Lake Atitlán & Communal Governance"
    ))

    # --------------------------------------------------------------------------
    # Lesson 6: b2-guatemala-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-guatemala-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el basamento", "pyramid base, plinth"],
                    ["el relato fundacional", "foundational narrative"],
                    ["el contrafuerte", "buttress"],
                    ["el resarcimiento", "moral/material redress"]
                ],
                "teaches": ["b2-guatemala-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones utiliza correctamente la voz pasiva analítica con complemento agente?",
                "options": [
                    "Los textos sagrados fueron traducidos por investigadores lingüísticos a mediados del siglo pasado.",
                    "Los textos sagrados se tradujeron para que la gente los lea con cuidado.",
                    "Se tradujeron los libros sagrados por los lingüistas que llegaron de la capital."
                ],
                "correct": 0,
                "teaches": ["pasiva-analitica-geografia"]
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué es incorrecto decir '*Antes de que llegaron los comisionados' en español culto?",
                "options": [
                    "Porque la locución 'antes de que' exige invariablemente el modo subjuntivo (llegaran o hubieran llegado).",
                    "Porque 'antes de que' solo puede utilizarse con tiempos futuros.",
                    "Porque el verbo 'llegar' es intransitivo y no admite subordinación temporal."
                ],
                "correct": 0,
                "teaches": ["temporales-antes-despues-que"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si bien los informes internacionales __ la crisis agraria, las cooperativas de café han mantenido su producción. (constatar - pretérito indefinido)",
                "answer": "constataron",
                "english": "Although international reports noted the agrarian crisis, coffee cooperatives have maintained their production.",
                "teaches": ["concesivas-historicas-si-bien"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Tikal fue erigida por constructores mayas en medio de la densa selva del Petén. [Tikal was erected by Mayan builders in the midst of the dense Petén jungle.]",
                    "Los dioses del Popol Vuh deliberaron antes de que crearan a la humanidad a partir del maíz. [The gods of the Popol Vuh deliberated before they created humanity from corn.]",
                    "Si bien los terremotos dañaron Antigua, los templos barrocos conservaron su majestuosidad. [Although earthquakes damaged Antigua, the baroque temples preserved their majesty.]",
                    "Los dirigentes declararon que defenderían la autonomía de sus cantones comunitarios. [The leaders stated that they would defend the autonomy of their community cantons.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["pasiva-analitica-geografia", "temporales-antes-despues-que", "concesivas-historicas-si-bien", "estilo-indirecto-testimonios"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diplomática", "text": "¿Cómo resumiría la trayectoria histórica de Guatemala desde el mundo clásico maya hasta el presente?"},
                    {"speaker": "Historiador", "text": "_____"},
                    {"speaker": "Diplomática", "text": "Una lección imperecedera de dignidad comunitaria y riqueza cultural."}
                ],
                "options": [
                    "Es una historia marcada por monumentales creaciones civilizatorias y dolorosas rupturas, donde los pueblos originarios preservaron su memoria y cosmovisión.",
                    "Los boletos para visitar el parque arqueológico de Tikal se adquieren en los bancos autorizados.",
                    "El clima del valle central es templado durante casi todos los meses del año."
                ],
                "correct": 0,
                "teaches": ["concesivas-historicas-si-bien"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las asambleas comunitarias ratificaron que resguardarían los bosques comunales antes de que se autorizaran nuevas concesiones.",
                "english": "Community assemblies ratified that they would safeguard communal forests before new concessions were authorized.",
                "teaches": ["estilo-indirecto-testimonios"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta un breve análisis histórico empleando la pasiva analítica con 'por' y la locución temporal 'antes de que' con subjuntivo.",
                        "answer": "La monumental acrópolis fue restaurada por arqueólogos locales antes de que comenzara la temporada de lluvias."
                    }
                ],
                "teaches": ["pasiva-analitica-geografia", "temporales-antes-despues-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=4,
        title="Unit 4 Consolidation: Guatemala",
        goal="Consolidate analytical passive voice, temporal subjunctive clauses, formal concessives, and reported speech through Guatemalan history and culture.",
        grammar_desc="síntesis de voz pasiva, temporales, concesivas y estilo indirecto",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Formulate analytical passive statements with agentive 'por' in archaeological descriptions.",
            "Apply the obligatory subjunctive rule with 'antes de que' across narrative tenses.",
            "Deploy formal concessive markers ('si bien', 'a pesar de que') in historical essays.",
            "Report testimonies and historical claims accurately using sequence of tenses."
        ],
        checklist_items=[
            "I can describe historical monuments and events using the analytical passive voice with 'ser'.",
            "I can use 'antes de que' with the subjunctive in past, present, and hypothetical sentences.",
            "I can introduce balanced concessions using 'si bien' with the indicative.",
            "I can convert direct testimonies and official statements into indirect reported speech."
        ],
        story_ref=f"stories/world/b2/{l5}.json"
    ))
    print("Completed LatAm Unit 4 (Guatemala) generation!")


if __name__ == "__main__":
    generate_latam_unit_4()
