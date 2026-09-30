#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Latin America Regional Studies Unit 3:
  - Title: "Mexico III: The South, Indigenous Pueblos & Biodiversity" (México III: El Sur, pueblos originarios y biodiversidad)
  - Stems: b2-mexicosur-01 through b2-mexicosur-consolidation
  - Cultural Focus: Oaxaca, Chiapas, Yucatán peninsula, cenotes, tequio communal governance, Zapatismo & biodiversity.
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_latam_unit_3():
    # Vocab theme slug: b2-mexicosur-vocab
    # Grammar skills:
    #   - relativas-subjuntivo-antecedente
    #   - concesivas-por-mas-que
    #   - impersonalidad-usos-costumbres
    #   - finalidad-a-fin-de-que

    # --------------------------------------------------------------------------
    # Lesson 1: b2-mexicosur-01 - Selvas, cenotes y cordilleras
    # --------------------------------------------------------------------------
    l1 = "b2-mexicosur-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.mexicosur.01",
        "lesson": l1,
        "title": "Geografía sagrada y biodiversidad del sur",
        "theme": "Topografía kárstica, selvas tropicales y cenotes",
        "words": [
            {"lemma": "el cenote", "translation": "cenote, natural sinkhole", "pos": "noun"},
            {"lemma": "el karst", "translation": "karst, limestone landscape", "pos": "noun"},
            {"lemma": "la selva", "translation": "jungle, tropical rainforest", "pos": "noun"},
            {"lemma": "el endemismo", "translation": "endemism, endemic species status", "pos": "noun"},
            {"lemma": "sagrado", "translation": "sacred, holy", "pos": "adjective"},
            {"lemma": "la neblina", "translation": "mist, fog", "pos": "noun"},
            {"lemma": "la cuenca", "translation": "river basin, watershed", "pos": "noun"},
            {"lemma": "el acuífero", "translation": "aquifer", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.mexicosur.01.relativas-subjuntivo",
        "title": "Subjuntivo en oraciones de relativo con antecedente inespecífico",
        "sections": [
            {
                "type": "text",
                "title": "Existencia presupuesta frente a entidad hipotética",
                "content": "En la descripción científica, geográfica y ecológica de nivel B2, las oraciones de relativo llevan verbo en modo subjuntivo cuando su antecedente es una entidad no identificada, hipotética o cuya existencia se ignora o niega: 'Buscamos una reserva biológica que proteja al jaguar' (no sabemos cuál o si existe una con esas características exactas)."
            },
            {
                "type": "table",
                "title": "Contraste indicativo vs subjuntivo en relativas",
                "rows": [
                    ["Antecedente conocido / específico -> INDICATIVO", "'Visitamos un cenote que tiene aguas cristalinas' (cenote concreto y conocido)"],
                    ["Antecedente inespecífico / deseado -> SUBJUNTIVO", "'Exploramos la selva en busca de un cenote que albergue especies ciegas endémicas' (entidad hipotética)"],
                    ["Antecedente negado -> SUBJUNTIVO", "'No hay ningún acuífero en la región que no sufra la presión del turismo masivo'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la ecología del sur",
                "items": [
                    {"spanish": "Los biólogos necesitan una metodología que permita monitorear la selva sin perturbar a la fauna.", "english": "Biologists need a methodology that permits monitoring the rainforest without disturbing the fauna."},
                    {"spanish": "En la península de Yucatán no existe ningún río superficial que desemboque en el mar.", "english": "In the Yucatan Peninsula there exists no surface river that empties into the sea."},
                    {"spanish": "Urge crear corredores biológicos que conecten los fragmentos aislados de selva.", "english": "It is urgent to create biological corridors that connect isolated fragments of rainforest."}
                ]
            },
            {
                "type": "tip",
                "content": "Fíjate en el artículo: los antecedentes precedidos de artículo indeterminado ('un, una') o indefinidos negativos ('ningún, nadie') suelen exigir subjuntivo cuando expresan perfiles de búsqueda o requisitos."
            }
        ]
    })

    write_json(f"stories/world/b2/{l1}.json", {
        "id": f"story.b2.{l1}",
        "title": "El manto kárstico de Yucatán y las selvas de Chiapas",
        "level": "B2",
        "author": "Ecología del Sureste Mexicano",
        "summary": "Un viaje por el ecosistema subterráneo de la península de Yucatán, los cenotes mayas como umbrales sagrados y la exuberancia de la Selva Lacandona.",
        "vocabularyTopics": ["Geografía del sureste", "Sistemas kársticos", "Cosmovisión del agua"],
        "grammar": ["relativas con subjuntivo", "léxico de biodiversidad tropical"],
        "paragraphs": [
            {
                "text": "El sureste de México alberga una de las concentraciones de biodiversidad más extraordinarias del continente americano. En la península de Yucatán, el suelo calcáreo impidió la formación de ríos superficiales, dando lugar en su lugar a una gigantesca red de ríos subterráneos y cenotes: dolinas kársticas donde la roca caliza se desplomó para revelar aguas de una pureza sobrenatural.",
                "english": "Southeastern Mexico harbors one of the most extraordinary concentrations of biodiversity on the American continent. In the Yucatan Peninsula, limestone soil prevented the formation of surface rivers, giving rise instead to a gigantic network of subterranean rivers and cenotes: karstic sinkholes where limestone rock collapsed to reveal waters of supernatural purity."
            },
            {
                "text": "Para la civilización maya, los cenotes no eran únicamente fuentes vitales de abastecimiento; representaban las puertas de acceso al Xibalbá, el inframundo sagrado. Sumergirse en sus profundidades equivalía a entrar en comunión con las deidades de la lluvia y la fertilidad.",
                "english": "For the Maya civilization, cenotes were not merely vital sources of water supply; they represented entry portals to Xibalbá, the sacred underworld. Immersing oneself in their depths was tantamount to communing with deities of rain and fertility."
            },
            {
                "text": "Hacia el occidente, la Selva Lacandona en Chiapas y los bosques de niebla de la Sierra de Juárez en Oaxaca completan este mosaico biológico. Sin embargo, este tesoro enfrenta graves amenazas derivadas de la deforestación y megaproyectos de transporte que no siempre respetan la fragilidad de los acuíferos.",
                "english": "Toward the west, the Lacandon Jungle in Chiapas and the cloud forests of the Sierra de Juárez in Oaxaca complete this biological mosaic. However, this treasure faces serious threats stemming from deforestation and transportation megaprojects that do not always respect the fragility of the aquifers."
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
                    ["el cenote", "natural sinkhole, cenote"],
                    ["el karst", "karst, limestone landscape"],
                    ["el endemismo", "endemism, endemic species status"],
                    ["el acuífero", "aquifer"]
                ],
                "teaches": ["b2-mexicosur-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué se usa el subjuntivo en 'Buscamos un biólogo que conozca los ecosistemas kársticos de Yucatán'?",
                "options": [
                    "Porque el antecedente es inespecífico: no se alude a una persona concreta, sino a un perfil hipotético.",
                    "Porque el biólogo ya trabaja en la universidad desde hace varios años.",
                    "Porque expresa una acción que ocurrió obligatoriamente en el pasado."
                ],
                "correct": 0,
                "teaches": ["relativas-subjuntivo-antecedente"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la península no hay ningún río superficial que __ agua hacia el golfo de México. (llevar - negative antecedent)",
                "answer": "lleve",
                "english": "In the peninsula there is no surface river that carries water toward the Gulf of Mexico.",
                "teaches": ["relativas-subjuntivo-antecedente"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Necesitamos", "un", "proyecto", "que", "proteja", "los", "cenotes", "sagrados."],
                "solution": ["Necesitamos", "un", "proyecto", "que", "proteja", "los", "cenotes", "sagrados."],
                "english": "We need a project that protects the sacred cenotes.",
                "teaches": ["relativas-subjuntivo-antecedente"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ambientalista", "text": "¿Qué condiciones debe reunir la nueva reserva natural de la biosfera?"},
                    {"speaker": "Guardaparques", "text": "_____"},
                    {"speaker": "Ambientalista", "text": "Eso asegurará la supervivencia del jaguar a largo plazo."}
                ],
                "options": [
                    "Debe ser un área extensa que garantice la conectividad entre los distintos corredores biológicos.",
                    "El parque cuenta con un museo colonial en el centro de la plaza mayor.",
                    "Ayer compramos varias botas de montaña para los nuevos guardaparques."
                ],
                "correct": 0,
                "teaches": ["relativas-subjuntivo-antecedente"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Urge diseñar un plan de desarrollo que no comprometa la pureza de los acuíferos subterráneos.",
                "english": "It is urgent to design a development plan that does not compromise the purity of underground aquifers.",
                "teaches": ["relativas-subjuntivo-antecedente"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=3,
        title="Selvas, cenotes y cordilleras: La geografía sagrada del sur",
        goal="Describe tropical rainforest ecosystems and karstic cenote aquifers using relative clauses with the subjunctive.",
        grammar_desc="el subjuntivo en oraciones de relativo con antecedente inespecífico o negado",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Examine the geological formation and sacred Mayan significance of cenotes in Yucatan.",
            "Analyze the ecological richness of the Lacandon jungle and Oaxaca cloud forests.",
            "Formulate relative clauses requiring the subjunctive with indefinite or negative antecedents."
        ],
        story_ref=f"stories/world/b2/{l1}.json",
        intro_body=[
            "Welcome to Unit 3 of Latin American Regional Studies: Mexico III: The South, Indigenous Pueblos & Biodiversity. The Mexican South encompasses the culturally dense and ecologically magnificent lands of Oaxaca, Chiapas, and the Yucatán peninsula.",
            "In this lesson, we delve into the sacred limestone hydrology of cenotes, the dense canopy of the Lacandon rainforest, and the critical struggle for environmental conservation, while mastering the subjunctive in relative clauses with indefinite antecedents."
        ],
        intro_title="Unit 3: The South, Indigenous Pueblos & Biodiversity"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-mexicosur-02 - Zapotecos, mixtecos y mayas: Civilizaciones vivas
    # --------------------------------------------------------------------------
    l2 = "b2-mexicosur-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.mexicosur.02",
        "lesson": l2,
        "title": "Pueblos originarios y lenguas vivas",
        "theme": "Cosmovisión indígena, telares y memoria ancestral",
        "words": [
            {"lemma": "el telar", "translation": "loom (especially backstrap loom)", "pos": "noun"},
            {"lemma": "el linaje", "translation": "lineage, ancestry", "pos": "noun"},
            {"lemma": "la cosmovisión", "translation": "worldview, cosmovision", "pos": "noun"},
            {"lemma": "ancestral", "translation": "ancestral", "pos": "adjective"},
            {"lemma": "la iconografía", "translation": "iconography", "pos": "noun"},
            {"lemma": "perdurar", "translation": "to endure, to outlast", "pos": "verb"},
            {"lemma": "el glifo", "translation": "glyph", "pos": "noun"},
            {"lemma": "la transmisión", "translation": "transmission, passing down", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.mexicosur.02.concesivas-por-mas-que",
        "title": "Oraciones concesivas intensivas con por más que",
        "sections": [
            {
                "type": "text",
                "title": "Concesión de grado extremo",
                "content": "Las estructuras concesivas 'por más que' o 'por mucho que' expresan que una acción o esfuerzo extremo no logra impedir o alterar el resultado principal. En el discurso B2, rigen subjuntivo cuando la circunstancia se plantea como hipótesis, esfuerzo indefinido o hecho general: 'Por más que pasen los siglos, la lengua maya perdurará'."
            },
            {
                "type": "table",
                "title": "Selección modal en concesivas intensivas",
                "rows": [
                    ["Por más que + SUBJUNTIVO", "Hipótesis, esfuerzo no verificado o principio categórico: 'Por más que intenten asimilarlos, conservarán sus tradiciones'"],
                    ["Por más que + INDICATIVO", "Constatación factual de un esfuerzo real ya consumado: 'Por más que estudió toda la noche, no aprobó el examen'"],
                    ["Por mucho que + sustantivo / verbo", "Cuantificación de grado extremo: 'Por mucho esfuerzo que pongan...', 'Por mucho que insistan...'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la historia de los pueblos originarios",
                "items": [
                    {"spanish": "Por más que los conquistadores destruyeron códices, la tradición oral preservó la memoria de los pueblos.", "english": "Even though the conquistadors destroyed codices, oral tradition preserved the memory of the peoples."},
                    {"spanish": "Por más presiones homogeneizadoras que existan, las tejedoras oaxaqueñas defienden sus diseños ancestrales.", "english": "No matter what homogenizing pressures exist, Oaxacan weavers defend their ancestral designs."},
                    {"spanish": "Por mucho que cambie el mundo contemporáneo, el vínculo con la tierra sigue siendo sagrado.", "english": "No matter how much the contemporary world changes, the bond with the land remains sacred."}
                ]
            },
            {
                "type": "tip",
                "content": "Utiliza 'por más que + subjuntivo' en debates argumentativos para conceder de antemano el máximo argumento del oponente ('Por más que se argumente X, lo cierto es que Y')."
            }
        ]
    })

    write_json(f"stories/world/b2/{l2}.json", {
        "id": f"story.b2.{l2}",
        "title": "La palabra tejida: Zapotecos, mixtecos y mayas contemporáneos",
        "level": "B2",
        "author": "Etnolingüística de Oaxaca y Chiapas",
        "summary": "Una exploración de las civilizaciones vivas del sur de México, la resistencia lingüística de zapotecos y mayas, y el telar de cintura como libro abierto de filosofía.",
        "vocabularyTopics": ["Pueblos originarios", "Arte textil", "Diversidad lingüística"],
        "grammar": ["concesivas con por más que", "vocabulario de patrimonio vivo"],
        "paragraphs": [
            {
                "text": "En los valles centrales de Oaxaca, en las sierras mixtecas y en las tierras bajas mayas de Yucatán y Chiapas, los pueblos originarios no son vestigios arqueológicos conservados en vitrinas; son sociedades vivas y dinámicas que hablan más de sesenta lenguas indígenas y transmiten cotidianamente saberes filosóficos milenarios.",
                "english": "In the central valleys of Oaxaca, in the Mixtec highlands, and in the Maya lowlands of Yucatan and Chiapas, indigenous peoples are not archaeological vestiges preserved in display cases; they are living, dynamic societies that speak more than sixty indigenous languages and daily transmit millenary philosophical knowledge."
            },
            {
                "text": "El telar de cintura es un ejemplo supremo de esta continuidad. En comunidades zapotecas como Teotitlán del Valle o mayas como San Juan Chamula, cada greca, color vegetal y rombo geométrico representa un relato genealógico o una cartografía del cosmos. Para las maestras tejedoras, tejer es escribir; los huipiles son bibliotecas corporales que ninguna censura colonial pudo erradicar.",
                "english": "The backstrap loom is a supreme example of this continuity. In Zapotec communities like Teotitlán del Valle or Maya ones like San Juan Chamula, each fret, vegetable dye, and geometric rhombus represents a genealogical narrative or a cartography of the cosmos. For master weavers, weaving is writing; huipiles are bodily libraries that no colonial censorship could eradicate."
            },
            {
                "text": "Por más que las políticas educativas del siglo veinte buscaron imponer un modelo castellanizador uniforme, las comunidades del sur resistieron mediante la transmisión intergeneracional en el hogar y en la milpa, demostrando que la verdadera riqueza de México radica en su irreductible pluralidad civilizatoria.",
                "english": "No matter how much twentieth-century educational policies sought to impose a uniform Hispanizing model, southern communities resisted through intergenerational transmission in the home and in the milpa, demonstrating that Mexico's true wealth lies in its irreducible civilizational plurality."
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
                    ["el telar", "loom (especially backstrap loom)"],
                    ["la cosmovisión", "worldview, cosmovision"],
                    ["la iconografía", "iconography"],
                    ["perdurar", "to endure, to outlast"]
                ],
                "teaches": ["b2-mexicosur-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo verbal debe emplearse en 'Por más que los críticos _____ la validez de los saberes tradicionales, la comunidad mantendrá sus prácticas'?",
                "options": [
                    "Subjuntivo (cuestionen), porque la objeción se plantea como hipótesis extrema.",
                    "Indicativo (cuestionaban), porque es un hecho verificado en el pasado.",
                    "Imperativo (cuestionen), porque expresa una orden de la asamblea."
                ],
                "correct": 0,
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Por más que se __ la lengua española en la escuela, los niños conservaron el zapoteco en el hogar. (imponer)",
                "answer": "impuso",
                "english": "Even though the Spanish language was imposed at school, the children preserved Zapotec at home.",
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Por", "más", "que", "insistan,", "no", "venderán", "sus", "tierras."],
                "solution": ["Por", "más", "que", "insistan,", "no", "venderán", "sus", "tierras."],
                "english": "No matter how much they insist, they will not sell their lands.",
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Lingüista", "text": "¿Cómo lograron las lenguas originarias sobrevivir a cinco siglos de marginación institucional?"},
                    {"speaker": "Sabia zapoteca", "text": "_____"},
                    {"speaker": "Lingüista", "text": "Esa lealtad lingüística comunitaria es un ejemplo para todo el mundo."}
                ],
                "options": [
                    "Por más que se nos prohibió hablarla en público, seguimos arrullando a nuestros hijos en nuestra lengua materna.",
                    "El café soluble se comercializa en todas las tiendas de autoservicio del país.",
                    "Los tratados de navegación marítima se firman en los puertos principales."
                ],
                "correct": 0,
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Por mucho que avance la modernización técnica, el telar de cintura preserva códigos ancestrales de identidad.",
                "english": "No matter how much technical modernization advances, the backstrap loom preserves ancestral codes of identity.",
                "teaches": ["concesivas-por-mas-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=3,
        title="Zapotecos, mixtecos y mayas: Civilizaciones vivas",
        goal="Analyze living indigenous cultures, textile iconography, and linguistic revitalization in southern Mexico using intensive concessive clauses with 'por más que'.",
        grammar_desc="oraciones concesivas intensivas con por más que y por mucho que",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Understand the vibrant contemporary presence of Zapotec, Mixtec, and Maya peoples.",
            "Analyze the backstrap loom as a repository of historical memory and cosmic iconography.",
            "Formulate nuanced counter-arguments with 'por más que' and 'por mucho que'."
        ],
        story_ref=f"stories/world/b2/{l2}.json"
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-mexicosur-03 - Comunidades, tequio y gobierno por usos y costumbres
    # --------------------------------------------------------------------------
    l3 = "b2-mexicosur-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.mexicosur.03",
        "lesson": l3,
        "title": "Comunalidad y gobierno indígena",
        "theme": "Tequio, asambleas comunitarias y sistema de cargos",
        "words": [
            {"lemma": "el tequio", "translation": "collective communal labor, tequio", "pos": "noun"},
            {"lemma": "la asamblea", "translation": "community assembly", "pos": "noun"},
            {"lemma": "la comunalidad", "translation": "communality, indigenous communal philosophy", "pos": "noun"},
            {"lemma": "el cargo", "translation": "community civic/religious post, duty", "pos": "noun"},
            {"lemma": "rotativo", "translation": "rotating, rotating term", "pos": "adjective"},
            {"lemma": "consensuar", "translation": "to reach consensus on, to agree collectively", "pos": "verb"},
            {"lemma": "la reciprocidad", "translation": "reciprocity", "pos": "noun"},
            {"lemma": "el faena", "translation": "communal task, labor day", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.mexicosur.03.impersonalidad-usos-costumbres",
        "title": "Impersonalidad y voz colectiva en el gobierno indígena",
        "sections": [
            {
                "type": "text",
                "title": "El 'se' institucional y la deliberación colectiva",
                "content": "Para describir sistemas políticos indígenas basados en la comunalidad, donde las decisiones no las toma un individuo aislado sino el colectivo reunido en asamblea, el español emplea estructuras impersonales y de pasiva refleja: 'Se practica el tequio', 'Se eligen las autoridades por aclamación', 'Se acuerdan los turnos de faena'."
            },
            {
                "type": "table",
                "title": "Construcciones colectivas e impersonales",
                "rows": [
                    ["Pasiva refleja con sustantivo colectivo", "'En la asamblea se toman las decisiones por consenso' (concordancia obligatoria en plural si el sujeto lo es)"],
                    ["Impersonal con 'se' de persona", "'Se respeta a los ancianos del pueblo' (verbo en singular + 'a' de objeto personal)"],
                    ["Tercera persona del plural sin sujeto", "'Eligen a los mayordomos sin recurrir a partidos políticos'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el derecho consuetudinario de Oaxaca",
                "items": [
                    {"spanish": "En más de cuatrocientos municipios de Oaxaca se gobierna mediante el régimen de sistemas normativos indígenas.", "english": "In more than four hundred municipalities of Oaxaca, governance is conducted through the regime of indigenous normative systems."},
                    {"spanish": "Mediante el tequio se construyen escuelas, se limpian caminos y se rehabilitan los sistemas de agua.", "english": "Through tequio schools are built, roads are cleared, and water systems are rehabilitated."},
                    {"spanish": "A las autoridades comunitarias no se les paga un sueldo; se sirve al pueblo como un deber de honor.", "english": "Community authorities are not paid a salary; one serves the people as a duty of honor."}
                ]
            },
            {
                "type": "tip",
                "content": "El concepto oaxaqueño de 'comunalidad' (articulado por teóricos mixes y zapotecos como Floriberto Díaz y Jaime Martínez Luna) sostiene que la tierra, el trabajo y la fiesta son inseparables del autogobierno asambleario."
            }
        ]
    })

    write_json(f"stories/world/b2/{l3}.json", {
        "id": f"story.b2.{l3}",
        "title": "El mandato de servir: Tequio, asambleas y comunalidad en Oaxaca",
        "level": "B2",
        "author": "Antropología Jurídica de Oaxaca",
        "summary": "El modelo de democracia participativa más antiguo de América: más de 400 municipios oaxaqueños gobernados por asamblea popular, el trabajo colectivo del tequio y el sistema de cargos sin partidos políticos.",
        "vocabularyTopics": ["Gobernanza indígena", "Sistemas normativos internos", "Solidaridad comunal"],
        "grammar": ["impersonalidad institucional", "estructuras con se en gobernanza"],
        "paragraphs": [
            {
                "text": "En el estado de Oaxaca conviven 570 municipios, de los cuales 417 eligen a sus autoridades mediante Sistemas Normativos Indígenas (anteriormente conocidos como 'usos y costumbres'), sin propaganda electoral ni intervención de partidos políticos. En este modelo, el órgano supremo de gobierno es la asamblea comunitaria, donde cada ciudadano participa con voz y voto.",
                "english": "In the state of Oaxaca 570 municipalities coexist, of which 417 elect their authorities through Indigenous Normative Systems (formerly known as 'customs and traditions'), without electoral propaganda or political party intervention. In this model, the supreme governing body is the community assembly, where every citizen participates with voice and vote."
            },
            {
                "text": "La columna vertebral de la vida comunitaria es el tequio: el trabajo colectivo y no remunerado que los miembros del pueblo aportan para el bien común. Gracias al tequio se pavimentan caminos vecinales, se construyen aulas escolares, se reforestan los bosques comunales y se apagan incendios forestales. No acudir a la faena sin causa justificada acarrea sanciones morales o multas fijadas por la propia asamblea.",
                "english": "The backbone of community life is tequio: collective, unremunerated labor that village members contribute for the common good. Thanks to tequio, rural roads are paved, schoolrooms are built, communal forests are reforested, and forest fires are extinguished. Failing to attend the work session without justified cause brings moral sanctions or fines set by the assembly itself."
            },
            {
                "text": "El sistema de cargos rotativos establece que el poder no es un privilegio para enriquecerse, sino una carga cívica de servicio. Para llegar a ser presidente municipal, una persona debe haber servido previamente como policía comunitario, mayordomo de las fiestas patronales y regidor, demostrando a lo largo de décadas su rectitud, capacidad de escucha y lealtad a la comunidad.",
                "english": "The rotating cargo system establishes that power is not a privilege for self-enrichment, but a civic burden of service. To become municipal president, a person must have previously served as community police officer, patron festival steward, and councilor, demonstrating over decades rectitude, capacity to listen, and loyalty to the community."
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
                    ["el tequio", "collective communal labor, tequio"],
                    ["la asamblea", "community assembly"],
                    ["consensuar", "to reach consensus on, to agree collectively"],
                    ["la reciprocidad", "reciprocity"]
                ],
                "teaches": ["b2-mexicosur-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones describe correctamente una práctica comunitaria mediante pasiva refleja plural?",
                "options": [
                    "En los pueblos de la sierra se coordinan faenas colectivas todos los fines de semana.",
                    "En los pueblos de la sierra se coordina faenas colectivas todos los fines de semana.",
                    "En los pueblos de la sierra se está coordinando a las faenas colectivas."
                ],
                "correct": 0,
                "teaches": ["impersonalidad-usos-costumbres"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la asamblea comunitaria no se __ sueldos a las autoridades municipales. (pagar - passive se plural)",
                "answer": "pagan",
                "english": "In the community assembly salaries are not paid to municipal authorities.",
                "teaches": ["impersonalidad-usos-costumbres"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Mediante", "el", "tequio", "se", "construyen", "los", "caminos", "rurales."],
                "solution": ["Mediante", "el", "tequio", "se", "construyen", "los", "caminos", "rurales."],
                "english": "Through tequio rural roads are built.",
                "teaches": ["impersonalidad-usos-costumbres"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Politólogo", "text": "¿Cómo se eligen las autoridades en los municipios regidos por usos y costumbres?"},
                    {"speaker": "Alcalde oaxaqueño", "text": "_____"},
                    {"speaker": "Politólogo", "text": "Es una auténtica democracia de base sin intermediarios partidistas."}
                ],
                "options": [
                    "Se debate abiertamente en asamblea general y se elige a los candidatos por consenso o aclamación popular.",
                    "Se contratan empresas encuestadoras privadas que realizan sondeos telefónicos.",
                    "El gobernador de la capital designa a los alcaldes por decreto ejecutivo vinculante."
                ],
                "correct": 0,
                "teaches": ["impersonalidad-usos-costumbres"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "En el régimen comunal se concibe el servicio público como un deber ético y no como un empleo lucrativo.",
                "english": "In the communal regime public service is conceived as an ethical duty and not as lucrative employment.",
                "teaches": ["impersonalidad-usos-costumbres"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=3,
        title="Comunidades, tequio y gobierno por usos y costumbres",
        goal="Analyze indigenous participatory democracy, the tequio labor system, and rotating community cargo governance using passive and impersonal structures.",
        grammar_desc="impersonalidad y pasiva refleja en el derecho consuetudinario y la comunalidad",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Examine the normative systems of participatory democracy in over 400 Oaxacan municipalities.",
            "Analyze tequio as a foundational practice of communal solidarity and infrastructure building.",
            "Master passive with 'se' and impersonal structures to describe collective deliberative governance."
        ],
        story_ref=f"stories/world/b2/{l3}.json"
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-mexicosur-04 - El levantamiento zapatista y el grito de dignidad
    # --------------------------------------------------------------------------
    l4 = "b2-mexicosur-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.mexicosur.04",
        "lesson": l4,
        "title": "Zapatismo, autonomía y derechos indígenas",
        "theme": "EZLN, Acuerdos de San Andrés y municipios autónomos",
        "words": [
            {"lemma": "el autogobierno", "translation": "self-government, self-rule", "pos": "noun"},
            {"lemma": "la dignidad", "translation": "dignity", "pos": "noun"},
            {"lemma": "el levantamiento", "translation": "uprising, insurrection", "pos": "noun"},
            {"lemma": "el caracol", "translation": "caracol (Zapatista autonomous regional center)", "pos": "noun"},
            {"lemma": "la proclama", "translation": "proclamation, manifesto", "pos": "noun"},
            {"lemma": "autónomo", "translation": "autonomous", "pos": "adjective"},
            {"lemma": "la insurgencia", "translation": "insurgency", "pos": "noun"},
            {"lemma": "el agravio", "translation": "grievance, offense, historical injustice", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.mexicosur.04.finalidad-a-fin-de-que",
        "title": "Oraciones finales avanzadas con a fin de que y con el objeto de que",
        "sections": [
            {
                "type": "text",
                "title": "Articulación de objetivos y propósitos institucionales",
                "content": "En los tratados de paz, proclamas políticas y textos legislativos de nivel B2, las oraciones subordinadas de finalidad van más allá del simple 'para que'. Locuciones como 'a fin de que', 'con el objeto de que' y 'con el propósito de que' seleccionan obligatoriamente modo subjuntivo y confieren al discurso un tono solemne y formal."
            },
            {
                "type": "table",
                "title": "Conectores de finalidad formal",
                "rows": [
                    ["A fin de que + SUBJUNTIVO", "Propósito institucional o jurídico: 'Se firmaron los Acuerdos de San Andrés a fin de que se garantizara la autonomía indígena'"],
                    ["Con el objeto de que + SUBJUNTIVO", "Meta estratégica deliberada: 'Se crearon los Caracoles con el objeto de que las comunidades administraran su salud y educación'"],
                    ["De modo que / De manera que + SUBJUNTIVO", "Finalidad intencional (a diferencia del valor consecutivo con indicativo): 'Organizaron la guardia de modo que nadie fuera sorprendido'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el movimiento zapatista",
                "items": [
                    {"spanish": "El EZLN promulgó la Primera Declaración de la Selva Lacandona a fin de que el mundo conociera los agravios de los pueblos mayas.", "english": "The EZLN promulgated the First Declaration of the Lacandon Jungle so that the world would know the grievances of the Maya peoples."},
                    {"spanish": "Las juntas de buen gobierno se coordinan con el objeto de que las decisiones se tomen de abajo hacia arriba.", "english": "The good-government councils coordinate with the aim that decisions be made from the bottom up."},
                    {"spanish": "Se organizaron brigadas médicas autónomas a fin de que la atención sanitaria llegara a los rincones más aislados de la selva.", "english": "Autonomous medical brigades were organized so that health care would reach the most isolated corners of the jungle."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que cuando el sujeto de la cláusula principal coincide con el de la subordinada, se prefiere la estructura preposicional con infinitivo: 'Lucharon a fin de defender sus tierras' (no 'a fin de que defendieran')."
            }
        ]
    })

    write_json(f"stories/world/b2/{l4}.json", {
        "id": f"story.b2.{l4}",
        "title": "¡Ya basta!: El levantamiento zapatista y la rebelión de la dignidad",
        "level": "B2",
        "author": "Historia Contemporánea de Chiapas",
        "summary": "El 1 de enero de 1994, el Ejército Zapatista de Liberación Nacional estremeció al mundo al rebelarse contra siglos de olvido indígena, inaugurando un nuevo paradigma de autonomía comunitaria.",
        "vocabularyTopics": ["Zapatismo", "Derechos indígenas", "Historia contemporánea de México"],
        "grammar": ["finalidad con a fin de que", "proclamas políticas B2"],
        "paragraphs": [
            {
                "text": "El 1 de enero de 1994, el mismo día en que México celebraba la entrada en vigor del Tratado de Libre Comercio con Estados Unidos y Canadá, un ejército de indígenas mayas con el rostro cubierto por pasamontañas tomó por las armas siete cabeceras municipales en el estado de Chiapas. Era el Ejército Zapatista de Liberación Nacional (EZLN), liderado políticamente por un portavoz enigmático conocido como el Subcomandante Marcos.",
                "english": "On January 1, 1994, the very day Mexico celebrated the entry into force of the Free Trade Agreement with the United States and Canada, an army of Maya indigenous people with faces covered by balaclavas took seven municipal seats in the state of Chiapas by arms. It was the Zapatista Army of National Liberation (EZLN), politically led by an enigmatic spokesman known as Subcomandante Marcos."
            },
            {
                "text": "Bajo la consigna ¡Ya basta!, el movimiento zapatista denunció cinco siglos de opresión, despojo de tierras y desnutrición infantil en una región rica en petróleo y energía hidroeléctrica pero sumida en la miseria extrema. Pronto, el conflicto armado dio paso a una gigantesca movilización civil y al diálogo en San Andrés Larráinzar, donde se redactaron acuerdos históricos sobre derechos y cultura indígena.",
                "english": "Under the slogan Enough!, the Zapatista movement denounced five centuries of oppression, land dispossession, and child malnutrition in a region rich in oil and hydroelectric power but mired in extreme misery. Soon, armed conflict gave way to a gigantic civil mobilization and dialogue in San Andrés Larráinzar, where historic accords on indigenous rights and culture were drafted."
            },
            {
                "text": "Ante el incumplimiento de los acuerdos por parte del Estado, los zapatistas decidieron construir la autonomía por la vía de los hechos. Fundaron los Caracoles y las Juntas de Buen Gobierno con el objeto de que los pueblos gestionaran sus propios sistemas de salud, educación y agroecología bajo el principio revolucionario de 'mandar obedeciendo', convirtiéndose en un referente insoslayable para los movimientos altermundistas de todo el planeta.",
                "english": "Faced with the state's breach of the accords, the Zapatistas decided to build autonomy de facto. They founded the Caracoles and Good Government Councils with the aim that the peoples manage their own health, education, and agroecology systems under the revolutionary principle of 'leading by obeying', becoming an inescapable benchmark for alter-globalization movements across the entire planet."
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
                    ["el autogobierno", "self-government, self-rule"],
                    ["el caracol", "Zapatista autonomous regional center"],
                    ["la proclama", "manifesto, proclamation"],
                    ["el agravio", "grievance, historical injustice"]
                ],
                "teaches": ["b2-mexicosur-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué conector formal de finalidad encabeza la oración 'Se convocó a un diálogo nacional _____ se reformara la constitución'?",
                "options": [
                    "a fin de que",
                    "puesto que",
                    "a menos que"
                ],
                "correct": 0,
                "teaches": ["finalidad-a-fin-de-que"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las comunidades fundaron escuelas autónomas con el objeto de que los jóvenes __ su lengua tzotzil. (aprender - imperfect subjunctive)",
                "answer": "aprendieran",
                "english": "The communities founded autonomous schools with the aim that young people would learn their Tzotzil language.",
                "teaches": ["finalidad-a-fin-de-que"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Lucharon", "a", "fin", "de", "que", "se", "reconociera", "su", "dignidad."],
                "solution": ["Lucharon", "a", "fin", "de", "que", "se", "reconociera", "su", "dignidad."],
                "english": "They fought so that their dignity would be recognized.",
                "teaches": ["finalidad-a-fin-de-que"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Cuál fue el objetivo central de los Acuerdos de San Andrés de 1996?"},
                    {"speaker": "Historiador", "text": "_____"},
                    {"speaker": "Periodista", "text": "Fue un hito jurídico que transformó el debate constitucional en México."}
                ],
                "options": [
                    "Establecer reformas constitucionales a fin de que se reconocieran plenamente los derechos colectivos y la autonomía de los pueblos originarios.",
                    "Fomentar la importación masiva de granos básicos desde el sudeste asiático.",
                    "Eliminar las lenguas mayas del currículo de las escuelas rurales bilingües."
                ],
                "correct": 0,
                "teaches": ["finalidad-a-fin-de-que"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las juntas de buen gobierno se crearon con el objeto de que el pueblo ejerciera el mandato de servir.",
                "english": "The good-government councils were created with the aim that the people would exercise the mandate to serve.",
                "teaches": ["finalidad-a-fin-de-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=3,
        title="El levantamiento zapatista y el grito de dignidad",
        goal="Analyze the 1994 Zapatista uprising, the San Andrés Accords, and de facto indigenous autonomy using formal finality clauses with 'a fin de que'.",
        grammar_desc="oraciones de finalidad con a fin de que y con el objeto de que",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Understand the historical roots and global impact of the 1994 EZLN insurrection in Chiapas.",
            "Analyze the concept of 'mandar obedeciendo' and autonomous governance in Zapatista Caracoles.",
            "Formulate institutional objectives and peace demands using advanced purpose clauses (a fin de que)."
        ],
        story_ref=f"stories/world/b2/{l4}.json"
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-mexicosur-05 - Megaproyectos, conservación ambiental y soberanía alimentaria
    # --------------------------------------------------------------------------
    l5 = "b2-mexicosur-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.mexicosur.05",
        "lesson": l5,
        "title": "Desarrollo territorial y soberanía agrícola",
        "theme": "Tren Maya, sistema milpa, maíz nativo y consulta previa",
        "words": [
            {"lemma": "la milpa", "translation": "milpa (traditional polyculture maize field)", "pos": "noun"},
            {"lemma": "el maíz criollo", "translation": "native/creole maize", "pos": "noun"},
            {"lemma": "la soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "la consulta", "translation": "prior community consultation", "pos": "noun"},
            {"lemma": "el trazado", "translation": "route, layout (of railway/road)", "pos": "noun"},
            {"lemma": "preservar", "translation": "to preserve", "pos": "verb"},
            {"lemma": "el ecoturismo", "translation": "ecotourism", "pos": "noun"},
            {"lemma": "el impacto", "translation": "impact, environmental impact", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.mexicosur.05.conectores-argumentativos",
        "title": "Conectores concesivos y adversativos en el debate ambiental",
        "sections": [
            {
                "type": "text",
                "title": "Articular la tensión entre desarrollo y conservación",
                "content": "El debate en torno a los megaproyectos en el sur de México exige equilibrar argumentos sobre crecimiento económico, conectividad territorial y preservación de la selva y el agua. Los conectores 'si bien', 'a pesar de que' y 'en contrapartida' permiten estructurar ensayos equilibrados de nivel B2."
            },
            {
                "type": "table",
                "title": "Conectores de contraste y contra-argumentación",
                "rows": [
                    ["Si bien + INDICATIVO", "Admite un hecho real antes de introducir el contra-argumento decisivo: 'Si bien el ferrocarril generará empleos, el impacto ambiental sobre los cenotes es alarmante'"],
                    ["A pesar de que + IND / SUBJ", "Indica obstáculo superado: con indicativo constata hechos reales; con subjuntivo formula reservas cautelosas"],
                    ["En contrapartida / Por el contrario", "Introduce una dimensión opuesta que equilibra la balanza argumentativa"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate territorial",
                "items": [
                    {"spanish": "Si bien el turismo genera divisas, las comunidades demandan que se respete el derecho a la consulta previa.", "english": "While tourism generates foreign exchange, communities demand that the right to prior consultation be respected."},
                    {"spanish": "A pesar de la deforestación circundante, las reservas ejidales han logrado conservar bosques maduros.", "english": "Despite surrounding deforestation, communal ejido reserves have managed to conserve mature forests."},
                    {"spanish": "El sistema de la milpa milenaria asegura la soberanía alimentaria frente a las crisis de los monocultivos.", "english": "The millenary milpa system secures food sovereignty in the face of monoculture crises."}
                ]
            },
            {
                "type": "tip",
                "content": "'Si bien' siempre rige indicativo y encabeza una concesión matizada en registro formal culto, funcionando de modo mucho más elegante que el reiterativo 'aunque'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l5}.json", {
        "id": f"story.b2.{l5}",
        "title": "La milpa milenaria y las vías del futuro: El sur en la encrucijada",
        "level": "B2",
        "author": "Centro de Investigaciones y Estudios Superiores en Antropología Social (CIESAS)",
        "summary": "El debate contemporáneo en el sureste mexicano entre los megaproyectos de transporte como el Tren Maya y la milenaria sabiduría agroecológica de la milpa maya.",
        "vocabularyTopics": ["Megaproyectos en México", "Soberanía alimentaria", "Agroecología tradicional"],
        "grammar": ["conectores concesivos si bien y a pesar de que", "léxico de consulta previa"],
        "paragraphs": [
            {
                "text": "El sur de México se halla hoy en una encrucijada decisiva entre dos visiones del territorio. Por un lado, el Estado ha impulsado megaproyectos de infraestructura monumental, destacando el Tren Maya, un ferrocarril de más de mil quinientos kilómetros concebido para interconectar los principales sitios arqueológicos, centros turísticos y urbes de la península de Yucatán y Chiapas.",
                "english": "Southern Mexico stands today at a decisive crossroads between two visions of territory. On one hand, the state has promoted monumental infrastructure megaprojects, prominently the Maya Train, a railway of more than one thousand five hundred kilometers conceived to interconnect major archaeological sites, tourist centers, and cities of the Yucatan Peninsula and Chiapas."
            },
            {
                "text": "Si bien sus defensores sostienen que la obra generará polos de desarrollo económico y empleo en una región históricamente desatendida, científicos, ambientalistas y organizaciones mayas han denunciado el impacto del trazado sobre cuevas sumergidas, la fragmentación de la selva y el riesgo de colapso de los acuíferos kársticos, exigiendo el cumplimiento estricto del Convenio 169 de la OIT sobre consulta previa, libre e informada.",
                "english": "While its defenders maintain that the project will generate economic development hubs and employment in a historically neglected region, scientists, environmentalists, and Maya organizations have denounced the route's impact on submerged caves, jungle fragmentation, and the risk of karst aquifer collapse, demanding strict adherence to ILO Convention 169 on free, prior, and informed consultation."
            },
            {
                "text": "Frente a los modelos de turismo masivo, las comunidades defienden la milpa tradicional: un policultivo prehispánico donde el maíz, el frijol, la calabaza y el chile crecen en simbiosis perfecta. Preservar las semillas criollas y la autonomía alimentaria representa no solo un acto de resistencia cultural, sino la alternativa ecológica más resiliente frente al cambio climático global.",
                "english": "Faced with mass tourism models, communities defend the traditional milpa: a pre-Hispanic polyculture where maize, beans, squash, and chili grow in perfect symbiosis. Preserving native seeds and food autonomy represents not only an act of cultural resistance, but the most resilient ecological alternative in the face of global climate change."
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
                    ["la milpa", "traditional polyculture maize field"],
                    ["el maíz criollo", "native/creole maize"],
                    ["el trazado", "railway/road route, layout"],
                    ["el ecoturismo", "ecotourism"]
                ],
                "teaches": ["b2-mexicosur-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el conector 'si bien' en 'Si bien el proyecto generará empleo, los ambientalistas advierten sobre los riesgos biológicos'?",
                "options": [
                    "Concede un hecho positivo antes de introducir la objeción principal con verbo en indicativo.",
                    "Plantea una condición estricta e hipotética que exige subjuntivo.",
                    "Expresa una consecuencia lógica derivada directamente de la premisa."
                ],
                "correct": 0,
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A pesar de que el tren ya comenzó a operar, los científicos __ monitoreando la calidad del agua en los cenotes. (continuar - present indicative)",
                "answer": "continúan",
                "english": "Even though the train already began operating, scientists continue monitoring water quality in the cenotes.",
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "milpa", "tradicional", "garantiza", "la", "soberanía", "alimentaria."],
                "solution": ["La", "milpa", "tradicional", "garantiza", "la", "soberanía", "alimentaria."],
                "english": "The traditional milpa guarantees food sovereignty.",
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Agrónomo", "text": "¿Por qué es tan valioso el sistema de la milpa frente a la agricultura industrial moderna?"},
                    {"speaker": "Comunera maya", "text": "_____"},
                    {"speaker": "Agrónomo", "text": "Es una lección milenaria de equilibrio y sostenibilidad ecológica."}
                ],
                "options": [
                    "Porque el maíz, el frijol y la calabaza se nutren mutuamente y protegen la fertilidad del suelo sin agroquímicos.",
                    "Porque requiere tractores importados de última generación para nivelar el terreno.",
                    "Porque las semillas transgénicas son las únicas que pueden resistir las lluvias tropicales."
                ],
                "correct": 0,
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las comunidades exigen que se respeten los resultados de las consultas previas antes de autorizar las obras.",
                "english": "Communities demand that the results of prior consultations be respected before authorizing the works.",
                "teaches": ["relativas-subjuntivo-antecedente"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=3,
        title="Megaproyectos, conservación ambiental y soberanía alimentaria",
        goal="Debate monumental infrastructure projects, indigenous prior consultation, and traditional milpa agroecology using concessive and relative structures.",
        grammar_desc="conectores concesivos formales y subordinación en el debate ecológico",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Evaluate the socio-environmental controversies surrounding the Maya Train in Yucatan.",
            "Understand the agroecological resilience of the traditional milpa and native creole maize.",
            "Deploy formal concessive connectors (si bien, a pesar de que) to construct balanced environmental essays."
        ],
        story_ref=f"stories/world/b2/{l5}.json"
    ))

    # --------------------------------------------------------------------------
    # Consolidated Unit Story: stories/world/b2/b2-mexicosur.json
    # --------------------------------------------------------------------------
    write_json("stories/world/b2/b2-mexicosur.json", {
        "id": "story.b2.mexicosur",
        "title": "La resistencia del sur profundo: Naturaleza sagrada, comunalidad y dignidad",
        "level": "B2",
        "author": "Antología del Pensamiento del Sur de México",
        "summary": "Una síntesis exhaustiva del México profundo: la geografía kárstica de los cenotes, la vitalidad de zapotecos y mayas, el autogobierno comunal del tequio, la insurgencia zapatista y la defensa de la milpa milenaria.",
        "vocabularyTopics": ["Sur de México", "Pueblos originarios y autonomía", "Biodiversidad y milpa"],
        "grammar": ["relativas con subjuntivo", "concesivas de grado extremo", "finalidad con a fin de que"],
        "paragraphs": [
            {
                "text": "El sur de México custodia la memoria civilizatoria más densa del país. Desde las selvas milenarias de Chiapas y las cuencas kársticas de la península de Yucatán hasta las cordilleras habitadas por mixtecos y zapotecos en Oaxaca, este territorio demuestra que el pasado mesoamericano no es una reliquia inerte, sino un principio activo de dignidad comunitaria.",
                "english": "Southern Mexico guards the country's densest civilizational memory. From the millenary jungles of Chiapas and karstic basins of the Yucatan Peninsula to mountain ranges inhabited by Mixtecs and Zapotecs in Oaxaca, this territory demonstrates that the Mesoamerican past is not an inert relic, but an active principle of community dignity."
            },
            {
                "text": "En cientos de municipios oaxaqueños, el tequio y el sistema de cargos articulan una democracia directa donde el poder se concibe como servicio desinteresado y la asamblea decide el destino colectivo. Esta vocación autonómica halló eco universal en 1994 con el levantamiento zapatista, que exigió al mundo reconocer los derechos inalienables de los pueblos indígenas bajo el lema de mandar obedeciendo.",
                "english": "In hundreds of Oaxacan municipalities, tequio and the cargo system articulate a direct democracy where power is conceived as selfless service and the assembly decides the collective destiny. This autonomic vocation found universal echo in 1994 with the Zapatista uprising, which demanded the world recognize the inalienable rights of indigenous peoples under the motto of leading by obeying."
            },
            {
                "text": "Hoy, frente a los embates de la homogeneización global y los megaproyectos que amenazan los acuíferos sagrados, las comunidades del sur profundo defienden la milpa milenaria y sus lenguas originarias a fin de que las futuras generaciones hereden una tierra viva donde quepan muchos mundos.",
                "english": "Today, faced with the onslaught of global homogenization and megaprojects that threaten sacred aquifers, the communities of the deep south defend the millenary milpa and their native languages so that future generations inherit a living land where many worlds fit."
            }
        ]
    })

    # --------------------------------------------------------------------------
    # Lesson 6: b2-mexicosur-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-mexicosur-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el cenote", "natural sinkhole, cenote"],
                    ["el telar", "backstrap loom"],
                    ["el tequio", "collective communal labor"],
                    ["la milpa", "traditional maize field"]
                ],
                "teaches": ["b2-mexicosur-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según el texto de consolidación del sur de México, ¿qué principio ético rige el sistema de cargos en las comunidades oaxaqueñas?",
                "options": [
                    "Que el poder político no es un privilegio lucrativo, sino una carga cívica de servicio desinteresado al pueblo.",
                    "Que solo los ciudadanos con mayor poder adquisitivo pueden gobernar la comunidad.",
                    "Que las autoridades se eligen exclusivamente a través de comités designados por el gobierno central."
                ],
                "correct": 0
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la frase 'Luchan a fin de que se respete la consulta previa', ¿por qué se utiliza el subjuntivo?",
                "options": [
                    "Porque la locución final 'a fin de que' rige obligatoriamente modo subjuntivo para expresar propósito.",
                    "Porque describe una acción rutinaria que ya ocurrió con certeza en el pasado.",
                    "Porque indica una condición contrafáctica imposible de cumplir."
                ],
                "correct": 0,
                "teaches": ["finalidad-a-fin-de-que"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Por más que __ las presiones del mercado turístico, las cooperativas no vendieron sus tierras ejidales. (aumentar)",
                "answer": "aumentaron",
                "english": "Even though tourist market pressures increased, the cooperatives did not sell their communal lands.",
                "teaches": ["concesivas-por-mas-que"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Los mayas concibieron los cenotes como umbrales sagrados hacia el inframundo de Xibalbá. [The Maya conceived cenotes as sacred thresholds to the underworld of Xibalbá.]",
                    "Las tejedoras zapotecas preservaron en sus huipiles una iconografía astronómica milenaria. [Zapotec weavers preserved an ancient astronomical iconography in their huipiles.]",
                    "En los municipios oaxaqueños se practica el tequio para realizar obras de beneficio común. [In Oaxacan municipalities tequio is practiced to carry out works of common benefit.]",
                    "El zapatismo fundó los Caracoles a fin de que las comunidades construyeran su autogobierno. [Zapatismo founded the Caracoles so that communities would build their self-government.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["relativas-subjuntivo-antecedente", "finalidad-a-fin-de-que"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Por qué el sur de México representa una alternativa ética frente a la crisis climática?"},
                    {"speaker": "Investigadora", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Es la demostración de que la soberanía alimentaria y la autonomía comunitaria van de la mano."}
                ],
                "options": [
                    "Porque la milpa tradicional y la comunalidad demuestran que es posible convivir en armonía con los ecosistemas sin destruirlos.",
                    "Porque el sur depende exclusivamente de la importación masiva de alimentos desde el exterior.",
                    "Porque en las selvas del sur no existe ninguna forma de organización social ni comunitaria."
                ],
                "correct": 0,
                "teaches": ["relativas-subjuntivo-antecedente"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las comunidades defienden sus semillas nativas a fin de que prevalezca la soberanía alimentaria en la región.",
                "english": "Communities defend their native seeds so that food sovereignty will prevail in the region.",
                "teaches": ["finalidad-a-fin-de-que"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Escribe una reflexión sobre la resistencia de los pueblos del sur de México, utilizando la locución 'a fin de que' y el término 'tequio'.",
                        "answer": "Los pueblos de Oaxaca preservan la práctica comunal del tequio a fin de que las obras públicas respondan a las verdaderas necesidades colectivas."
                    }
                ],
                "teaches": ["finalidad-a-fin-de-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=3,
        title="Unit 3 Consolidation",
        goal="Consolidate knowledge of southern Mexican geography, indigenous living civilisations, tequio communality, Zapatismo, and milpa agroecology.",
        grammar_desc="síntesis de estudios regionales sobre el México del sur profundo",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Consolidate geographic, anthropological, and political insights on southern Mexico.",
            "Review 40 key vocabulary terms spanning karst hydrology, textile arts, indigenous governance, and agroecology.",
            "Apply the subjunctive in relative clauses, concessives with 'por más que', and purpose clauses with 'a fin de que'.",
            "Synthesize the civilizational dignity of the deep Mexican south."
        ],
        checklist_items=[
            "I can describe cenote hydrology, the Lacandon jungle, and southern Mexican ecosystems.",
            "I can analyze living Zapotec, Mixtec, and Maya heritage and textile iconography.",
            "I can explain participatory democracy in Oaxaca, tequio labor, and rotating cargos.",
            "I can discuss the 1994 Zapatista insurrection, the San Andrés Accords, and milpa agroecology."
        ],
        story_ref="stories/world/b2/b2-mexicosur.json"
    ))
    print("Completed LatAm Unit 3 generation!")


if __name__ == "__main__":
    generate_latam_unit_3()
