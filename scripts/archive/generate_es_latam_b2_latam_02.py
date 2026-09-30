#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Latin America Regional Studies Unit 2:
  - Title: "Mexico II: The North, the Border & Industrial Modernity" (México II: El Norte, la frontera y la modernidad industrial)
  - Stems: b2-mexiconorte-01 through b2-mexiconorte-consolidation
  - Cultural Focus: The Mexican Septentrión, Rarámuri runners, Monterrey's industrial engine, borderlands & nearshoring.
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_latam_unit_2():
    # Vocab theme slug: b2-mexiconorte-vocab
    # Grammar skills:
    #   - perifrasis-ir-gerundio
    #   - focalizacion-discursiva-nortena
    #   - condicional-de-infinitivo
    #   - relativos-preposicionales-complejos

    # --------------------------------------------------------------------------
    # Lesson 1: b2-mexiconorte-01 - El desierto y la geografía del Septentrión
    # --------------------------------------------------------------------------
    l1 = "b2-mexiconorte-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.mexiconorte.01",
        "lesson": l1,
        "title": "Geografía del Septentrión y desierto",
        "theme": "Ecosistemas áridos, cañones y resistencia física",
        "words": [
            {"lemma": "el septentrión", "translation": "the north, northern region", "pos": "noun"},
            {"lemma": "la aridez", "translation": "aridness, barrenness", "pos": "noun"},
            {"lemma": "la serranía", "translation": "mountain range, mountainous highlands", "pos": "noun"},
            {"lemma": "el barranco", "translation": "ravine, precipice", "pos": "noun"},
            {"lemma": "la resistencia", "translation": "endurance, resistance", "pos": "noun"},
            {"lemma": "el cañón", "translation": "canyon, gorge", "pos": "noun"},
            {"lemma": "inhóspito", "translation": "inhospitable", "pos": "adjective"},
            {"lemma": "la estepa", "translation": "steppe, scrubland", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.mexiconorte.01.perifrasis-ir-gerundio",
        "title": "La perífrasis aspectual ir + gerundio",
        "sections": [
            {
                "type": "text",
                "title": "Gradualidad y acumulación progresiva",
                "content": "La perífrasis 'ir + gerundio' expresa una acción que se desarrolla de manera paulatina, paso a paso o por etapas acumulativas. En el análisis geográfico e histórico, es idónea para describir transformaciones territoriales, migraciones lentas o procesos que ganan intensidad con el transcurso del tiempo: 'El desierto fue avanzando sobre las planicies'."
            },
            {
                "type": "table",
                "title": "Diferencias aspectuales con otras perífrasis continuativas",
                "rows": [
                    ["Estar + gerundio", "Acción en curso puntual en un momento dado: 'Está cambiando el clima hoy'"],
                    ["Seguir / Continuar + gerundio", "Persistencia o mantenimiento de un estado previo: 'Sigue lloviendo poco en Sonora'"],
                    ["Ir + gerundio", "Proceso acumulativo, gradual y orientado hacia una meta: 'Los pueblos originarios fueron adaptándose a la aridez extrema'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en contexto regional",
                "items": [
                    {"spanish": "A lo largo de los siglos, los rarámuri fueron desarrollando una resistencia física legendaria.", "english": "Throughout the centuries, the Rarámuri gradually developed a legendary physical endurance."},
                    {"spanish": "Conforme ascendemos a la sierra, la vegetación va cambiando hacia densos bosques de pino.", "english": "As we ascend into the highlands, the vegetation gradually changes into dense pine forests."},
                    {"spanish": "Las temperaturas van descendiendo drásticamente al caer la noche en el desierto de Chihuahua.", "english": "Temperatures gradually drop drastically as night falls in the Chihuahuan desert."}
                ]
            },
            {
                "type": "tip",
                "content": "No confundas 'ir + gerundio' con el desplazamiento físico literal: en 'el proyecto va marchando bien', 'ir' funciona puramente como auxiliar aspectual de desarrollo progresivo."
            }
        ]
    })

    write_json(f"stories/world/b2/{l1}.json", {
        "id": f"story.b2.{l1}",
        "title": "El Septentrión mexicano y los corredores del viento",
        "level": "B2",
        "author": "Crónicas del México Norteño",
        "summary": "Una travesía por el inmenso norte mexicano, las Barrancas del Cobre y la resistencia milenaria del pueblo rarámuri frente a la aridez de la Sierra Madre Occidental.",
        "vocabularyTopics": ["Geografía del norte", "Pueblos indígenas", "Resistencia física"],
        "grammar": ["perífrasis ir + gerundio", "descripción geográfica B2"],
        "paragraphs": [
            {
                "text": "El norte de México, conocido históricamente como el Septentrión, abarca más del cincuenta por ciento del territorio nacional. Lejos de ser un páramo uniforme, este espacio inmenso se compone de cuencas desérticas, sierras escarpadas y llanuras donde la luz adquiere una nitidez deslumbrante. El desierto de Sonora y las dunas de Samalayuca en Chihuahua configuran ecosistemas donde la vida ha tenido que aprender a resistir.",
                "english": "Northern Mexico, historically known as the Septentrión, encompasses more than fifty percent of the national territory. Far from being a uniform wasteland, this immense expanse is composed of desert basins, rugged mountain ranges, and plains where the light takes on a dazzling clarity. The Sonoran Desert and the dunes of Samalayuca in Chihuahua configure ecosystems where life has had to learn to endure."
            },
            {
                "text": "En el corazón de Chihuahua se despliegan las Barrancas del Cobre, un sistema de cañones cuatro veces más extenso y más profundo que el Gran Cañón del Colorado. En este relieve quebrado habitan los rarámuri, 'los de los pies ligeros', quienes a lo largo de las generaciones fueron perfeccionando la carrera de resistencia como práctica ritual, cotidiana y comunitaria, recorriendo cientos de kilómetros entre desfiladeros con sandalias de cuero.",
                "english": "In the heart of Chihuahua unfold the Copper Canyon, a canyon system four times larger and deeper than the Grand Canyon of the Colorado. In this fractured terrain live the Rarámuri, 'those of the light feet', who across generations gradually perfected endurance running as a ritual, daily, and community practice, traversing hundreds of kilometers through gorges in leather sandals."
            },
            {
                "text": "La relación de los pueblos norteños con su geografía forjó un temple particular: la inmensidad del horizonte y el aislamiento frente a la capital colonial moldearon una identidad de autonomía, pragmatismo y resiliencia que sigue distinguiendo a los habitantes del Septentrión frente al centro del país.",
                "english": "The relationship of northern peoples with their geography forged a distinctive mettle: the immensity of the horizon and isolation from the colonial capital shaped an identity of autonomy, pragmatism, and resilience that continues to distinguish the inhabitants of the Septentrión from the center of the country."
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
                    ["el septentrión", "the north, northern region"],
                    ["la aridez", "aridness, barrenness"],
                    ["el barranco", "ravine, precipice"],
                    ["inhóspito", "inhospitable"]
                ],
                "teaches": ["b2-mexiconorte-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz aspectual aporta la perífrasis en 'Las comunidades fueron adaptándose gradualmente al clima desértico'?",
                "options": [
                    "Indica un proceso progresivo, acumulativo y continuo a lo largo del tiempo.",
                    "Señala una acción puntual que interrumpió bruscamente a otra.",
                    "Expresa una hipótesis incierta en el presente."
                ],
                "correct": 0,
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Con el paso de las horas, el cañón __ cubriendo de sombras impenetrables. (ir - imperfect)",
                "answer": "se iba",
                "english": "With the passage of the hours, the canyon was gradually becoming covered with impenetrable shadows.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "rarámuri", "fueron", "dominando", "las", "grandes", "distancias."],
                "solution": ["Los", "rarámuri", "fueron", "dominando", "las", "grandes", "distancias."],
                "english": "The Rarámuri gradually mastered the vast distances.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Viajero", "text": "¿Cómo lograron los habitantes del norte sobrevivir en un entorno tan hostil?"},
                    {"speaker": "Guía", "text": "_____"},
                    {"speaker": "Viajero", "text": "Esa adaptación milenaria es digna de admiración."}
                ],
                "options": [
                    "A lo largo de los siglos fueron aprendiendo a aprovechar cada gota de agua subterránea.",
                    "La capital colonial contaba con excelentes teatros barrocos.",
                    "El café se cultiva preferentemente en valles húmedos del sur tropical."
                ],
                "correct": 0,
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La sequía fue transformando los antiguos pastizales en planicies pedregosas e inhóspitas.",
                "english": "The drought gradually transformed the ancient grasslands into stony and inhospitable plains.",
                "teaches": ["perifrasis-ir-gerundio"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=2,
        title="El desierto y la geografía del Septentrión",
        goal="Describe northern Mexican desert landscapes and Rarámuri endurance culture using the progressive aspectual periphrasis 'ir + gerundio'.",
        grammar_desc="la perífrasis aspectual ir + gerundio en la descripción de procesos",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Analyze the physical geography of the Chihuahuan and Sonoran deserts and the Copper Canyon.",
            "Describe the endurance athletic culture of the Rarámuri people.",
            "Use the aspectual periphrasis 'ir + gerundio' to convey gradual environmental and social changes."
        ],
        story_ref=f"stories/world/b2/{l1}.json",
        intro_body=[
            "Welcome to Unit 2 of Latin American Regional Studies: Mexico II: The North, the Border & Industrial Modernity. Spanning over half the Mexican republic, the Septentrión is a territory of immense horizons, dramatic canyons, and rugged individualism.",
            "In this lesson, we explore the arid landscapes of Chihuahua and Sonora, the ancient canyons of the Sierra Tarahumara, and the extraordinary physical endurance of the Rarámuri runners, while mastering the progressive periphrasis 'ir + gerundio'."
        ],
        intro_title="Unit 2: The North, the Border & Industrial Modernity"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-mexiconorte-02 - La cultura vaquera y la forja del norteño
    # --------------------------------------------------------------------------
    l2 = "b2-mexiconorte-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.mexiconorte.02",
        "lesson": l2,
        "title": "Cultura ganadera y carácter norteño",
        "theme": "Tradición vaquera, agostaderos y gastronomía del norte",
        "words": [
            {"lemma": "el vaquero", "translation": "cowboy, cattle herder", "pos": "noun"},
            {"lemma": "el agostadero", "translation": "summer grazing pasture, range", "pos": "noun"},
            {"lemma": "la faena", "translation": "chore, ranch task, labor", "pos": "noun"},
            {"lemma": "la reciedumbre", "translation": "toughness, sturdiness, strength", "pos": "noun"},
            {"lemma": "el ganado", "translation": "livestock, cattle", "pos": "noun"},
            {"lemma": "fronterizo", "translation": "border, frontier (adj)", "pos": "adjective"},
            {"lemma": "el corral", "translation": "corral, pen", "pos": "noun"},
            {"lemma": "el temple", "translation": "mettle, temper, fortitude", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.mexiconorte.02.focalizacion-discursiva",
        "title": "Focalización discursiva y partículas norteñas",
        "sections": [
            {
                "type": "text",
                "title": "Marcadores y modulación del discurso en el norte",
                "content": "El habla del norte de México se caracteriza por una entonación enérgica y el uso de marcadores discursivos de focalización e intensidad. En el nivel B2, comprender estas partículas permite identificar el registro regional sin incurrir en estereotipos."
            },
            {
                "type": "table",
                "title": "Partículas y giros discursivos característicos",
                "rows": [
                    ["Nomás (nada más)", "Restricción y focalización de inmediatez: 'Nomás te pido que seas puntual', 'Llegó y nomás saludó'"],
                    ["Bien + adjetivo / adverbio", "Intensificador de grado alto equivalente a 'muy' o 'sumamente': 'La jornada estuvo bien pesada', 'Eran bien trabajadores'"],
                    ["Focalización de cierre con 'pues'", "Refuerza la conclusión o aserción contundente: 'Así son las cosas por acá, pues'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el registro oral norteño",
                "items": [
                    {"spanish": "El trabajo en el rancho empezaba bien temprano, antes de que despuntara el sol.", "english": "Work on the ranch used to start very early, before the sun peeked out."},
                    {"spanish": "Nomás terminaron de arrear el ganado, se reunieron alrededor de la fogata.", "english": "As soon as they finished herding the cattle, they gathered around the campfire."},
                    {"spanish": "Frente a la adversidad del clima, hay que tener mucho temple, pues.", "english": "Faced with the adversity of the weather, one has to have great fortitude, after all."}
                ]
            },
            {
                "type": "tip",
                "content": "En la escritura formal y ensayística B2, estas partículas se reconocen en textos testimoniales, reportajes periodísticos y obras literarias de autores norteños como Elmer Mendoza o David Toscana."
            }
        ]
    })

    write_json(f"stories/world/b2/{l2}.json", {
        "id": f"story.b2.{l2}",
        "title": "La forja del norteño: Ganado, carne asada y frontera",
        "level": "B2",
        "author": "Crónicas de Coahuila y Sonora",
        "summary": "Una mirada a la cultura ranchera del norte de México, el origen novohispano del vaquero americano y el ritual comunitario de la carne asada.",
        "vocabularyTopics": ["Cultura vaquera", "Sociología del norte", "Gastronomía comunitaria"],
        "grammar": ["focalización discursiva", "adverbios intensificadores regionales"],
        "paragraphs": [
            {
                "text": "Mucho antes de que el cine de Hollywood popularizara la figura del cowboy en el suroeste estadounidense, la cultura vaquera ya se había gestado en las llanuras novohispanas de Sonora, Coahuila y Chihuahua. Las técnicas de arreo, la silla de montar con fuste, el lazo de cuero y la vestimenta de faena fueron desarrolladas por criollos, mestizos e indígenas en los extensos agostaderos norteños.",
                "english": "Long before Hollywood cinema popularized the figure of the cowboy in the American Southwest, vaquero culture had already developed in the viceregal plains of Sonora, Coahuila, and Chihuahua. Herding techniques, the horn-saddle, the leather lasso, and work attire were developed by criollos, mestizos, and indigenous people in the vast northern grazing ranges."
            },
            {
                "text": "La distancia respecto a la capital virreinal y la constante defensa frente a incursiones nómadas crearon una sociedad con escasa reverencia por las jerarquías aristocráticas. En el norte prevaleció una ética del esfuerzo individual, la palabra empeñada y el compañerismo de campamento. La reciedumbre de carácter se convirtió en el valor fundacional de la comunidad.",
                "english": "The distance from the viceregal capital and constant defense against nomadic raids created a society with little reverence for aristocratic hierarchies. In the north, an ethic of individual effort, pledged word, and camp fellowship prevailed. Toughness of character became the foundational value of the community."
            },
            {
                "text": "Hoy en día, esa herencia convive con la modernidad urbana a través del ritual de la carne asada. Reunirse frente a la parrilla de carbón en Sonora o Nuevo León no es simplemente comer; es un acto de cohesión social donde se reafirman los lazos familiares, se discute de negocios y se celebra el orgullo de pertenecer al norte.",
                "english": "Today, that heritage coexists with urban modernity through the ritual of the carne asada. Gathering around the charcoal grill in Sonora or Nuevo León is not simply eating; it is an act of social cohesion where family bonds are reaffirmed, business is discussed, and pride in belonging to the north is celebrated."
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
                    ["el agostadero", "summer grazing range"],
                    ["la faena", "ranch task, chore"],
                    ["la reciedumbre", "toughness, sturdiness"],
                    ["el temple", "mettle, fortitude"]
                ],
                "teaches": ["b2-mexiconorte-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el adverbio 'bien' en 'Los vaqueros salían bien temprano hacia las llanuras'?",
                "options": [
                    "Funciona como intensificador de grado equivalente a 'muy' o 'sumamente'.",
                    "Indica una evaluación moral positiva de la acción de madrugar.",
                    "Señala que la acción se realizó de manera correcta y conforme a la ley."
                ],
                "correct": 0,
                "teaches": ["focalizacion-discursiva-nortena"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Para arrear el ganado bajo el sol abrasador se necesita __ temple. (mucho / intense mettle)",
                "answer": "mucho",
                "english": "To herd cattle under the scorching sun one needs great fortitude.",
                "teaches": ["focalizacion-discursiva-nortena"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "cultura", "vaquera", "surgió", "en", "estos", "agostaderos."],
                "solution": ["La", "cultura", "vaquera", "surgió", "en", "estos", "agostaderos."],
                "english": "Vaquero culture arose in these grazing ranges.",
                "teaches": ["focalizacion-discursiva-nortena"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Qué elemento distingue la sociabilidad familiar en el norte mexicano?"},
                    {"speaker": "Historiador", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Es un auténtico espacio de encuentro intergeneracional."}
                ],
                "options": [
                    "El ritual de la carne asada, donde la comunidad reafirma sus lazos de forma horizontal.",
                    "El cultivo intensivo de caña de azúcar en las marismas costeras.",
                    "Las procesiones de carnavales barrocos heredados del siglo diecisiete."
                ],
                "correct": 0,
                "teaches": ["focalizacion-discursiva-nortena"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La reciedumbre de los vaqueros novohispanos dio origen a las tradiciones ganaderas continentales.",
                "english": "The toughness of viceregal cowboys gave rise to continental cattle ranching traditions.",
                "teaches": ["focalizacion-discursiva-nortena"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=2,
        title="La cultura vaquera y la forja del norteño",
        goal="Examine the historical roots of vaquero cattle culture and northern Mexican social identity while analyzing emphatic discourse markers.",
        grammar_desc="focalización discursiva e intensificadores en el habla regional",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Trace the origins of American cowboy heritage to viceregal northern Mexican vaqueros.",
            "Understand the cultural and social significance of the carne asada ritual.",
            "Recognize and analyze regional discourse markers and intensifiers in northern Mexican speech."
        ],
        story_ref=f"stories/world/b2/{l2}.json"
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-mexiconorte-03 - Monterrey y el poder industrial mexicano
    # --------------------------------------------------------------------------
    l3 = "b2-mexiconorte-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.mexiconorte.03",
        "lesson": l3,
        "title": "Industrialización e innovación urbana",
        "theme": "Siderurgia, corporaciones y crisis hídrica",
        "words": [
            {"lemma": "la acería", "translation": "steel mill, steelworks", "pos": "noun"},
            {"lemma": "el empuje", "translation": "drive, momentum, energy", "pos": "noun"},
            {"lemma": "la fundición", "translation": "foundry, smelting plant", "pos": "noun"},
            {"lemma": "la urbe", "translation": "large city, metropolis", "pos": "noun"},
            {"lemma": "la escasez", "translation": "scarcity, shortage", "pos": "noun"},
            {"lemma": "la siderurgia", "translation": "iron and steel industry", "pos": "noun"},
            {"lemma": "prosperar", "translation": "to prosper, to thrive", "pos": "verb"},
            {"lemma": "el consorcio", "translation": "consortium, corporate group", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.mexiconorte.03.condicional-de-infinitivo",
        "title": "Estructuras condicionales con de + infinitivo",
        "sections": [
            {
                "type": "text",
                "title": "Condición sintética y contrafáctica",
                "content": "En el registro formal y periodístico de nivel B2, la construcción preposicional 'de + infinitivo simple' o 'de + infinitivo compuesto' sustituye elegantemente a las oraciones condicionales introducidas por 'si': 'De haber contado con agua suficiente, la producción habría aumentado' (equivalente a 'Si hubiera contado...')."
            },
            {
                "type": "table",
                "title": "Equivalencias condicionales",
                "rows": [
                    ["De + infinitivo simple", "Condición hipotética presente o futura: 'De continuar la sequía, habrá restricciones severas' (= Si continúa...)"],
                    ["De + infinitivo compuesto", "Condición contrafáctica en el pasado: 'De haberse postergado las obras, la ciudad habría colapsado' (= Si se hubieran postergado...)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el análisis económico",
                "items": [
                    {"spanish": "De no haberse fundado la Fundidora en 1900, Monterrey no sería el epicentro industrial que es hoy.", "english": "Had Fundidora not been founded in 1900, Monterrey would not be the industrial epicenter it is today."},
                    {"spanish": "De persistir la escasez hídrica, los consorcios deberán relocalizar sus plantas de tratamiento.", "english": "Should water scarcity persist, corporate groups will have to relocate their treatment plants."},
                    {"spanish": "De haber sabido las implicaciones logísticas, habrían diversificado sus proveedores.", "english": "Had they known the logistical implications, they would have diversified their suppliers."}
                ]
            },
            {
                "type": "tip",
                "content": "Esta fórmula es muy apreciada en la redacción de informes ejecutivos, editoriales y ensayos históricos por su concisión y elevado registro estilístico."
            }
        ]
    })

    write_json(f"stories/world/b2/{l3}.json", {
        "id": f"story.b2.{l3}",
        "title": "El titán del acero: Monterrey bajo el Cerro de la Silla",
        "level": "B2",
        "author": "Estudios Industriales de Nuevo León",
        "summary": "El ascenso de Monterrey como la capital industrial de México, la mística del trabajo regiomontana y la encrucijada del estrés hídrico contemporáneo.",
        "vocabularyTopics": ["Desarrollo industrial", "Historia de Monterrey", "Sostenibilidad hídrica"],
        "grammar": ["condicional con de + infinitivo", "léxico económico y técnico"],
        "paragraphs": [
            {
                "text": "Bajo la silueta inconfundible del Cerro de la Silla se extiende la zona metropolitana de Monterrey, la urbe que transformó el destino económico del norte mexicano. Fundada en un valle semidesértico sin yacimientos de oro ni tierras agrícolas fértiles, la ciudad apostó desde finales del siglo diecinueve por el ingenio manufacturero y la industria pesada.",
                "english": "Under the unmistakable silhouette of the Cerro de la Silla stretches the metropolitan area of Monterrey, the metropolis that transformed the economic destiny of northern Mexico. Founded in a semi-desert valley without gold deposits or fertile agricultural lands, the city banked from the late nineteenth century on manufacturing ingenuity and heavy industry."
            },
            {
                "text": "En 1900 nació la Compañía Fundidora de Fierro y Acero de Monterrey, la primera acería moderna de América Latina. A su alrededor floreció un ecosistema empresarial que dio origen a gigantes globales en el vidrio, el cemento y las bebidas, complementado con instituciones de excelencia académica como el Tecnológico de Monterrey.",
                "english": "In 1900 the Monterrey Iron and Steel Foundry Company was born, the first modern steelworks in Latin America. Around it flourished an entrepreneurial ecosystem that gave rise to global giants in glass, cement, and beverages, complemented by institutions of academic excellence such as the Tecnológico de Monterrey."
            },
            {
                "text": "Sin embargo, el vertiginoso empuje industrial enfrenta hoy su mayor desafío: la grave escasez de agua provocada por sequías prolongadas y el crecimiento demográfico. De no implementar políticas integrales de recirculación y captación, el modelo de desarrollo regiomontano comprometerá su propia viabilidad ecológica.",
                "english": "However, the dizzying industrial momentum faces its greatest challenge today: the severe water scarcity caused by prolonged droughts and demographic growth. Should comprehensive policies of recirculation and catchment not be implemented, the Monterrey development model will compromise its own ecological viability."
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
                    ["la acería", "steelworks, steel mill"],
                    ["el empuje", "drive, momentum, energy"],
                    ["la escasez", "scarcity, shortage"],
                    ["el consorcio", "consortium, corporate group"]
                ],
                "teaches": ["b2-mexiconorte-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué significado equivale a 'De no haber invertido en infraestructura hídrica, la ciudad habría colapsado'?",
                "options": [
                    "Si no hubiera invertido en infraestructura hídrica, la ciudad habría colapsado.",
                    "Aunque no invirtió en infraestructura, la ciudad colapsó irremediablemente.",
                    "Para invertir en agua, era indispensable que la ciudad colapsara primero."
                ],
                "correct": 0,
                "teaches": ["condicional-de-infinitivo"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "De __ persistido las altas temperaturas, el sistema eléctrico habría sufrido apagones masivos. (haber)",
                "answer": "haber",
                "english": "Had the high temperatures persisted, the electrical grid would have suffered massive blackouts.",
                "teaches": ["condicional-de-infinitivo"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["De", "haber", "previsto", "la", "crisis,", "habrían", "actuado."],
                "solution": ["De", "haber", "previsto", "la", "crisis,", "habrían", "actuado."],
                "english": "Had they foreseen the crisis, they would have acted.",
                "teaches": ["condicional-de-infinitivo"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Economista", "text": "¿Por qué Monterrey logró consolidarse como polo fabril sin tener recursos minerales en su suelo?"},
                    {"speaker": "Analista", "text": "_____"},
                    {"speaker": "Economista", "text": "Fue una visión estratégica que cambió el mapa de la república."}
                ],
                "options": [
                    "De haber dependido solo de la agricultura, jamás habría atraído las cuantiosas inversiones que forjaron la fundición.",
                    "La ciudad contaba con enormes minas de plata descubiertas por los conquistadores españoles.",
                    "El puerto marítimo de la ciudad permitía exportar trigo a Europa durante todo el año."
                ],
                "correct": 0,
                "teaches": ["condicional-de-infinitivo"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "De no resolverse el déficit hídrico, las acerías deberán reducir drásticamente su producción.",
                "english": "Should the water deficit not be resolved, the steel mills will have to drastically reduce their production.",
                "teaches": ["condicional-de-infinitivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=2,
        title="Monterrey y el poder industrial mexicano",
        goal="Analyze the industrial emergence and ecological challenges of Monterrey using hypothetical conditionals with 'de + infinitivo'.",
        grammar_desc="estructuras condicionales sintéticas con de + infinitivo",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Trace the industrial trajectory of Monterrey from the 1900 Fundidora to global conglomerates.",
            "Debate contemporary industrial challenges, nearshoring, and severe water scarcity.",
            "Formulate concise hypothetical and counterfactual arguments with 'de + infinitivo'."
        ],
        story_ref=f"stories/world/b2/{l3}.json"
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-mexiconorte-04 - La frontera y la cultura fronteriza
    # --------------------------------------------------------------------------
    l4 = "b2-mexiconorte-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.mexiconorte.04",
        "lesson": l4,
        "title": "Espacio fronterizo y dinámicas binacionales",
        "theme": "Cultura de frontera, garitas, corridos y bilingüismo",
        "words": [
            {"lemma": "el cruce", "translation": "crossing, border crossing", "pos": "noun"},
            {"lemma": "la garita", "translation": "checkpoint, border control booth", "pos": "noun"},
            {"lemma": "el corrido", "translation": "corrido (traditional narrative ballad)", "pos": "noun"},
            {"lemma": "el flujo", "translation": "flow, stream", "pos": "noun"},
            {"lemma": "la binacionalidad", "translation": "binationality", "pos": "noun"},
            {"lemma": "el tránsito", "translation": "transit, passage, traffic", "pos": "noun"},
            {"lemma": "cotidiano", "translation": "daily, everyday", "pos": "adjective"},
            {"lemma": "el muro", "translation": "wall, barrier", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.mexiconorte.04.relativos-preposicionales",
        "title": "Oraciones de relativo con preposición + artículo",
        "sections": [
            {
                "type": "text",
                "title": "Precisión sintáctica en cláusulas relativas",
                "content": "En la descripción sociológica y periodística de nivel B2, las cláusulas de relativo complejas combinan preposiciones (mediante, a través de, frente a, con respecto a) con los relativos articulados 'el cual / la cual / los cuales / las cuales' o 'el que / la que'. Estas estructuras evitan la ambigüedad sobre el antecedente y dotan al texto de gran elegancia analítica."
            },
            {
                "type": "table",
                "title": "Estructuras relativas preposicionales",
                "rows": [
                    ["A través de + el/la cual", "Movimiento o intermediación: 'La garita a través de la cual circulan miles de vehículos diariamente'"],
                    ["En torno a + el/la que", "Temática o eje articulador: 'La problemática en torno a la cual gira el debate migratorio'"],
                    ["Frente a + el/la cual", "Oposición o contraste espacial/conceptual: 'El muro frente al cual se reúnen familias separadas'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el contexto fronterizo",
                "items": [
                    {"spanish": "Tijuana y San Diego conforman una conurbación binacional en la cual conviven dos realidades jurídicas.", "english": "Tijuana and San Diego form a binational conurbation in which two legal realities coexist."},
                    {"spanish": "Los acuerdos comerciales mediante los cuales se reguló el cruce agilizaron el transporte.", "english": "The trade agreements through which the crossing was regulated sped up transportation."},
                    {"spanish": "El corrido es un género musical mediante el cual los pueblos fronterizos han narrado sus epopeyas.", "english": "The corrido is a musical genre through which border communities have narrated their epics."}
                ]
            },
            {
                "type": "tip",
                "content": "Usa 'el cual / la cual' preferentemente en oraciones explicativas (entre comas) o cuando el antecedente esté alejado del pronombre, garantizando que el género y número señalen al referente exacto."
            }
        ]
    })

    write_json(f"stories/world/b2/{l4}.json", {
        "id": f"story.b2.{l4}",
        "title": "Vidas entre dos mundos: La frontera Tijuana-San Diego y Ciudad Juárez",
        "level": "B2",
        "author": "Estudios Fronterizos del Colegio de la Frontera Norte",
        "summary": "Una inmersión en la frontera más transitada del planeta, la hibridez cultural del spanglish, los corridos y la vida cotidiana transfronteriza.",
        "vocabularyTopics": ["Frontera norte", "Identidad binacional", "Cultura del corrido"],
        "grammar": ["relativos preposicionales complejos", "léxico de sociología fronteriza"],
        "paragraphs": [
            {
                "text": "La frontera entre México y Estados Unidos se extiende a lo largo de más de tres mil cien kilómetros, pero su corazón palpitante reside en las urbes gemelas como Tijuana-San Diego y Ciudad Juárez-El Paso. La garita de San Ysidro en Tijuana es el cruce terrestre más transitado del planeta, con decenas de millones de cruces anuales de personas que viven en México y trabajan o estudian al norte de la línea.",
                "english": "The border between Mexico and the United States stretches over more than three thousand one hundred kilometers, but its beating heart resides in twin cities like Tijuana-San Diego and Ciudad Juárez-El Paso. The San Ysidro port of entry in Tijuana is the busiest land crossing on the planet, with tens of millions of annual crossings of people who live in Mexico and work or study north of the line."
            },
            {
                "text": "Lejos de ser únicamente una barrera de concreto y acero, la frontera es un espacio generador de cultura híbrida. En este laboratorio lingüístico y artístico florece la literatura del norte, la experimentación culinaria 'Baja Med' y la música de corridos mediante la cual se documentan las vicisitudes del migrante, el desarraigo y la persistencia de la dignidad comunitaria.",
                "english": "Far from being solely a barrier of concrete and steel, the border is a space generating hybrid culture. In this linguistic and artistic laboratory flourishes northern literature, 'Baja Med' culinary experimentation, and corrido music through which the tribulations of the migrant, uprooting, and the persistence of community dignity are documented."
            },
            {
                "text": "La binacionalidad cotidiana desafía los discursos simplistas: miles de familias tienen raíces a ambos lados del cerco, articulando una identidad transfronteriza donde el inglés y el español se entrelazan de manera orgánica y donde el sentido de pertenencia trasciende los límites territoriales del Estado-nación.",
                "english": "Everyday binationality challenges simplistic discourses: thousands of families have roots on both sides of the fence, articulating a transborder identity where English and Spanish intertwine organically and where the sense of belonging transcends the territorial boundaries of the nation-state."
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
                    ["la garita", "checkpoint, border control booth"],
                    ["el cruce", "border crossing"],
                    ["la binacionalidad", "binationality"],
                    ["cotidiano", "daily, everyday"]
                ],
                "teaches": ["b2-mexiconorte-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué relativo preposicional completa correctamente 'La garita internacional a través de _____ circulan mercancías fue modernizada'?",
                "options": [
                    "la cual",
                    "el que",
                    "quienes"
                ],
                "correct": 0,
                "teaches": ["relativos-preposicionales-complejos"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las leyes migratorias conforme a __ se regulan los visados laborales requieren reformas urgentes. (las cuales)",
                "answer": "las cuales",
                "english": "The immigration laws in accordance with which work visas are regulated require urgent reforms.",
                "teaches": ["relativos-preposicionales-complejos"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Es", "el", "espacio", "en", "el", "cual", "florece", "la", "cultura."],
                "solution": ["Es", "el", "espacio", "en", "el", "cual", "florece", "la", "cultura."],
                "english": "It is the space in which culture flourishes.",
                "teaches": ["relativos-preposicionales-complejos"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Antropóloga", "text": "¿Cómo definiría la dinámica cotidiana de quienes viven en Tijuana y laboran en San Diego?"},
                    {"speaker": "Investigador", "text": "_____"},
                    {"speaker": "Antropóloga", "text": "En efecto, la frontera es tanto una separación física como un puente continuo."}
                ],
                "options": [
                    "Es una existencia transfronteriza mediante la cual desafían las nociones tradicionales de soberanía y pertenencia.",
                    "La mayoría de las personas prefiere mudarse definitivamente al hemisferio sur.",
                    "Los trámites aduanales se realizan sin ningún tipo de pasaporte ni documento oficial."
                ],
                "correct": 0,
                "teaches": ["relativos-preposicionales-complejos"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El corrido fronterizo es una manifestación lírica mediante la cual se inmortalizan los relatos populares.",
                "english": "The border corrido is a lyrical manifestation through which popular tales are immortalized.",
                "teaches": ["relativos-preposicionales-complejos"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=2,
        title="La frontera y la cultura fronteriza",
        goal="Explore the binational social dynamics, cultural hybridity, and musical traditions of the US-Mexico border using complex prepositional relative clauses.",
        grammar_desc="oraciones de relativo con preposición y artículo determinado",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Examine daily life across the busiest land crossing in the world (Tijuana-San Diego).",
            "Analyze hybrid linguistic forms, border literature, and corrido balladry.",
            "Construct nuanced prepositional relative clauses with 'el cual' and 'el que'."
        ],
        story_ref=f"stories/world/b2/{l4}.json"
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-mexiconorte-05 - El T-MEC, las maquiladoras y el nuevo panorama
    # --------------------------------------------------------------------------
    l5 = "b2-mexiconorte-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.mexiconorte.05",
        "lesson": l5,
        "title": "Comercio internacional y manufactura",
        "theme": "Tratado T-MEC, nearshoring, maquilas y cadenas de suministro",
        "words": [
            {"lemma": "la maquiladora", "translation": "export assembly plant, maquiladora", "pos": "noun"},
            {"lemma": "el ensamblaje", "translation": "assembly", "pos": "noun"},
            {"lemma": "la logística", "translation": "logistics", "pos": "noun"},
            {"lemma": "el arancel", "translation": "tariff, customs duty", "pos": "noun"},
            {"lemma": "la relocalización", "translation": "nearshoring, relocation of manufacturing", "pos": "noun"},
            {"lemma": "el suministro", "translation": "supply, procurement", "pos": "noun"},
            {"lemma": "manufacturero", "translation": "manufacturing (adj)", "pos": "adjective"},
            {"lemma": "el tratado", "translation": "treaty, trade pact", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.mexiconorte.05.pasiva-refleja-economia",
        "title": "La pasiva refleja en el discurso económico",
        "sections": [
            {
                "type": "text",
                "title": "Impersonalidad y procesos productivos",
                "content": "En la prosa periodística y económica B2, la pasiva refleja ('se' + verbo en tercera persona concordando con el sujeto paciente) es la estructura predilecta para describir operaciones mercantiles, ensamblaje industrial y tratados internacionales, focalizando el proceso sin necesidad de nombrar al agente humano."
            },
            {
                "type": "table",
                "title": "Concordancia rigurosa en pasiva refleja",
                "rows": [
                    ["Sujeto paciente singular", "'Se firmó el nuevo tratado comercial' (verbo singular)"],
                    ["Sujeto paciente plural", "'Se ensamblan componentes aeroespaciales en Querétaro y Sonora' (verbo plural)"],
                    ["Diferencia con 'se' impersonal", "La pasiva refleja concuerda con cosas ('se exportan vehículos'); la impersonal lleva objeto de persona con preposición 'a' y verbo en singular ('se capacitó a los operarios')"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el sector manufacturero",
                "items": [
                    {"spanish": "En las plantas fronterizas se fabrican dispositivos médicos de alta tecnología.", "english": "In border plants high-tech medical devices are manufactured."},
                    {"spanish": "Con el fenómeno del nearshoring se han atraído miles de millones de dólares en inversión.", "english": "With the nearshoring phenomenon billions of dollars in investment have been attracted."},
                    {"spanish": "En el tratado se estipulan cláusulas estrictas sobre derechos laborales y medio ambiente.", "english": "In the treaty strict clauses on labor rights and environment are stipulated."}
                ]
            },
            {
                "type": "tip",
                "content": "Evita el error frecuente de mantener el verbo en singular cuando el sustantivo posterior es plural: di 'se exportan automóviles', nunca 'se exporta automóviles'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l5}.json", {
        "id": f"story.b2.{l5}",
        "title": "El taller de América del Norte: Del TLCAN al fenómeno del nearshoring",
        "level": "B2",
        "author": "Análisis Económico de El Colegio de México",
        "summary": "La transformación del norte mexicano en uno de los centros de manufactura más avanzados del mundo bajo el T-MEC y el rediseño global de las cadenas de suministro.",
        "vocabularyTopics": ["Comercio global", "Nearshoring en México", "Industria automotriz"],
        "grammar": ["pasiva refleja en economía", "concordancia de sujetos pacientes plurales"],
        "paragraphs": [
            {
                "text": "La entrada en vigor del Tratado de Libre Comercio de América del Norte en 1994 transformó radicalmente la geografía económica de México. El norte del país, gracias a su contigüidad geográfica con Estados Unidos y a una red de parques industriales en constante expansión, se consolidó como una de las plataformas de manufactura y exportación más competitivas del planeta.",
                "english": "The entry into force of the North American Free Trade Agreement in 1994 radically transformed Mexico's economic geography. The north of the country, thanks to its geographical contiguity with the United States and a constantly expanding network of industrial parks, established itself as one of the most competitive manufacturing and export platforms on the planet."
            },
            {
                "text": "Las maquiladoras tradicionales de mano de obra intensiva dieron paso a instalaciones de alta tecnología. Hoy en día, en ciudades como Saltillo, Ciudad Juárez, Hermosillo y Reynosa se ensamblan vehículos eléctricos, procesadores informáticos y piezas aeroespaciales que abastecen las cadenas de valor integradas de América del Norte.",
                "english": "Traditional labor-intensive maquiladoras gave way to high-tech facilities. Today, in cities such as Saltillo, Ciudad Juárez, Hermosillo, and Reynosa, electric vehicles, computer processors, and aerospace parts that supply the integrated North American value chains are assembled."
            },
            {
                "text": "Con el fenómeno de la relocalización industrial o 'nearshoring', motivado por las tensiones geopolíticas globales, México vive una oportunidad histórica. Sin embargo, para consolidar este salto cualitativo se requiere modernizar la red eléctrica, garantizar fuentes de energía renovable y fortalecer la formación técnica de la fuerza laboral.",
                "english": "With the phenomenon of industrial relocation or 'nearshoring', prompted by global geopolitical tensions, Mexico is experiencing a historic opportunity. However, to consolidate this qualitative leap, modernizing the electrical grid, guaranteeing renewable energy sources, and strengthening the technical training of the workforce are required."
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
                    ["la maquiladora", "export assembly plant"],
                    ["el arancel", "customs duty, tariff"],
                    ["la relocalización", "nearshoring, manufacturing relocation"],
                    ["el suministro", "supply, procurement"]
                ],
                "teaches": ["b2-mexiconorte-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones presenta una pasiva refleja con concordancia gramatical correcta?",
                "options": [
                    "En las maquiladoras se fabrican microprocesadores para la industria automotriz.",
                    "En las maquiladoras se fabrica microprocesadores para la industria automotriz.",
                    "En las maquiladoras se fueron fabricando a los microprocesadores."
                ],
                "correct": 0,
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En el marco del nuevo tratado __ estrictas normas sobre el contenido regional de autopartes. (acordar - passive se)",
                "answer": "se acordaron",
                "english": "Within the framework of the new treaty strict rules on regional autopart content were agreed upon.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "ensamblan", "motores", "eléctricos", "en", "esta", "planta."],
                "solution": ["Se", "ensamblan", "motores", "eléctricos", "en", "esta", "planta."],
                "english": "Electric motors are assembled in this plant.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Empresaria", "text": "¿Por qué tantas multinacionales están relocalizando sus plantas en el norte de México?"},
                    {"speaker": "Consultor", "text": "_____"},
                    {"speaker": "Empresaria", "text": "La proximidad con el mercado consumidor estadounidense es insustituible."}
                ],
                "options": [
                    "Porque se reducen los tiempos logísticos y se aprovechan las ventajas arancelarias del T-MEC.",
                    "Porque en el desierto llueve abundantemente durante los doce meses del año.",
                    "Porque las empresas prefieren pagar los aranceles más elevados de la región."
                ],
                "correct": 0,
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Con el tratado comercial se multiplicaron las inversiones industriales en todo el corredor fronterizo.",
                "english": "With the trade treaty industrial investments multiplied across the entire border corridor.",
                "teaches": ["perifrasis-ir-gerundio"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=2,
        title="El T-MEC, las maquiladoras y el nuevo panorama económico",
        goal="Discuss international trade, nearshoring, and supply chain logistics in Northern Mexico using passive and impersonal constructions.",
        grammar_desc="la pasiva refleja en el discurso económico y manufacturero",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Understand the economic impact of NAFTA/USMCA (T-MEC) on northern Mexican industrial corridors.",
            "Debate the opportunities and infrastructure bottlenecks of the nearshoring phenomenon.",
            "Produce formal economic reports using passive with 'se' with proper plural agreement."
        ],
        story_ref=f"stories/world/b2/{l5}.json"
    ))

    # --------------------------------------------------------------------------
    # Consolidated Unit Story: stories/world/b2/b2-mexiconorte.json
    # --------------------------------------------------------------------------
    write_json("stories/world/b2/b2-mexiconorte.json", {
        "id": "story.b2.mexiconorte",
        "title": "Horizontes del Septentrión: Desierto, industria y frontera",
        "level": "B2",
        "author": "Antología de Estudios Regionales de México",
        "summary": "Una síntesis integral del norte mexicano: la inmensidad desértica, la resistencia de los rarámuri, la tradición vaquera, la potencia fabril de Monterrey y la encrucijada transfronteriza del T-MEC.",
        "vocabularyTopics": ["Septentrión mexicano", "Industria y nearshoring", "Cultura fronteriza"],
        "grammar": ["perífrasis aspectual ir + gerundio", "condicional de infinitivo", "relativos preposicionales"],
        "paragraphs": [
            {
                "text": "El norte de México encarna una dimensión geográfica y cultural que desafía las visiones centralistas del país. Desde las cumbres nevadas de la Sierra Tarahumara hasta los llanos calcinantes de Sonora y Coahuila, este territorio forjó en sus habitantes una cultura de esfuerzo perseverante, pragmatismo y autonomía comunitaria.",
                "english": "Northern Mexico embodies a geographical and cultural dimension that challenges centralist visions of the country. From the snow-capped summits of the Sierra Tarahumara to the scorching plains of Sonora and Coahuila, this territory forged in its inhabitants a culture of persevering effort, pragmatism, and community autonomy."
            },
            {
                "text": "La herencia del vaquero novohispano sentó las bases de la ganadería continental, mientras que en el siglo veinte la ciudad de Monterrey demostró que la determinación humana puede erigir una metrópoli industrial de vanguardia sobre un suelo árido y desafiante.",
                "english": "The heritage of the viceregal vaquero laid the foundations for continental cattle ranching, while in the twentieth century the city of Monterrey demonstrated that human determination can erect a cutting-edge industrial metropolis on arid and challenging soil."
            },
            {
                "text": "En las ciudades fronterizas como Tijuana y Ciudad Juárez, el dinamismo binacional y las cadenas globales de valor del T-MEC conviven con una identidad híbrida donde el español dialoga cotidianamente con el inglés, consolidando al norte como el puente indiscutible entre América Latina y el resto del mundo.",
                "english": "In border cities like Tijuana and Ciudad Juárez, binational dynamism and global USMCA value chains coexist with a hybrid identity where Spanish dialogues daily with English, establishing the north as the indisputable bridge between Latin America and the rest of the world."
            }
        ]
    })

    # --------------------------------------------------------------------------
    # Lesson 6: b2-mexiconorte-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-mexiconorte-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el septentrión", "northern region"],
                    ["el agostadero", "summer grazing range"],
                    ["la acería", "steelworks"],
                    ["la maquiladora", "export assembly plant"]
                ],
                "teaches": ["b2-mexiconorte-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según la síntesis sobre el Septentrión mexicano, ¿qué rasgo caracterizó históricamente a las sociedades del norte?",
                "options": [
                    "Una cultura forjada en la autonomía, el pragmatismo y la resiliencia frente a la aridez y el aislamiento.",
                    "Una dependencia absoluta de la agricultura de regadío colonial del valle central.",
                    "Un aislamiento completo que impidió cualquier tipo de comercio con el exterior."
                ],
                "correct": 0
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la frase 'De no haberse firmado el acuerdo, las inversiones se habrían detenido', ¿qué estructura gramatical se emplea?",
                "options": [
                    "Una condición contrafáctica con 'de + infinitivo compuesto' equivalente a 'Si no se hubiera firmado'.",
                    "Una oración temporal de inmediatez equivalente a 'En cuanto se firmó'.",
                    "Una oración de relativo sin antecedente expreso."
                ],
                "correct": 0,
                "teaches": ["condicional-de-infinitivo"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Conforme pasaban los meses, las fábricas __ adaptando a los nuevos protocolos del T-MEC. (ir - imperfect)",
                "answer": "se iban",
                "english": "As the months passed, the factories were gradually adapting to the new USMCA protocols.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Los rarámuri fueron perfeccionando la carrera pedestre como práctica ritual en los cañones. [The Rarámuri gradually perfected foot running as a ritual practice in the canyons.]",
                    "La cultura vaquera sentó las bases de la economía ganadera en los agostaderos del norte. [Vaquero culture laid the foundations of the cattle economy in northern pastures.]",
                    "Monterrey se transformó en un polo siderúrgico gracias a la fundación de su primera acería en 1900. [Monterrey transformed into a steel hub thanks to the founding of its first mill in 1900.]",
                    "El tratado comercial agilizó los flujos mercantiles en todas las garitas fronterizas. [The trade treaty sped up merchandise flows across all border checkpoints.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["perifrasis-ir-gerundio", "relativos-preposicionales-complejos"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diplomático", "text": "¿Cómo resumiría la importancia geopolítica del norte mexicano hoy?"},
                    {"speaker": "Especialista", "text": "_____"},
                    {"speaker": "Diplomático", "text": "Por ello el T-MEC es una pieza angular de la estabilidad continental."}
                ],
                "options": [
                    "Es un corredor estratégico mediante el cual se integran las cadenas industriales más sofisticadas del mundo.",
                    "Es una región dedicada casi en su totalidad al turismo de cruceros marítimos tropicales.",
                    "Carece de infraestructura de transporte terrestre con el vecino del norte."
                ],
                "correct": 0,
                "teaches": ["relativos-preposicionales-complejos"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "De no haberse diversificado la economía norteña, el impacto de las crisis globales habría sido devastador.",
                "english": "Had the northern economy not been diversified, the impact of global crises would have been devastating.",
                "teaches": ["condicional-de-infinitivo"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Escribe un breve balance sobre la importancia manufacturera del norte mexicano, usando la perífrasis 'ir + gerundio' y el término 'maquiladora'.",
                        "answer": "A lo largo de las décadas, la industria maquiladora fue modernizando sus plantas hasta ensamblar tecnología aeroespacial y automotriz de vanguardia."
                    }
                ],
                "teaches": ["perifrasis-ir-gerundio"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=2,
        title="Unit 2 Consolidation",
        goal="Consolidate knowledge of northern Mexican geography, vaquero heritage, Monterrey's industrial prowess, borderlands culture, and USMCA nearshoring.",
        grammar_desc="síntesis de estudios regionales sobre el México norteño",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Consolidate geographic, historical, and economic insights on the Mexican Septentrión.",
            "Review 40 key vocabulary terms spanning desert ecology, cattle culture, steel manufacturing, and border logistics.",
            "Apply 'ir + gerundio', conditional 'de + infinitivo', and complex relative clauses in regional analysis.",
            "Synthesize the contemporary binational role of northern Mexico."
        ],
        checklist_items=[
            "I can describe the desert landscapes of Sonora and Chihuahua and Rarámuri athletic heritage.",
            "I can discuss the historical origin of vaquero culture and northern social values.",
            "I can evaluate the industrial development of Monterrey and its water sustainability challenges.",
            "I can analyze border identity, corrido music, and the economic dynamics of nearshoring."
        ],
        story_ref="stories/world/b2/b2-mexiconorte.json"
    ))
    print("Completed LatAm Unit 2 generation!")


if __name__ == "__main__":
    generate_latam_unit_2()
