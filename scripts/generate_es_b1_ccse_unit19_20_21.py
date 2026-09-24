#!/usr/bin/env python3
"""Generate Spain Citizenship (CCSE) Units 19, 20, and 21 for es-es B1 track."""

from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict

UNITS_19_20_21 = [
    # =========================================================================
    # UNIT 19: Comunidades del Mediterráneo e Islas Baleares (unit_num=55, b1-mediterraneo)
    # =========================================================================
    {
        "slug": "mediterraneo",
        "unit_num": 55,
        "title": "Comunidades del Mediterráneo e Islas Baleares",
        "description": "Provincias, capitales, instituciones y patrimonio de Aragón, Cataluña, la Comunitat Valenciana, la Región de Murcia y las Islas Baleares.",
        "Badge": "Arco Mediterráneo",
        "lessons": [
            {
                "num": "01",
                "Title": "Aragón: Huesca, Zaragoza, Teruel y el Valle del Ebro",
                "title": "Aragón: Huesca, Zaragoza, Teruel y el Valle del Ebro",
                "grammar_slug": "extenderse-de-norte-a-sur-a-lo-largo-de",
                "story_slug": "aragon",
                "story_title": "Del pico Aneto al Pilar de Zaragoza y las torres mudéjares de Teruel",
                "objectives": [
                    "Memorizar las tres provincias de Aragón (Huesca, Zaragoza y Teruel) y su capital autonómica (Zaragoza).",
                    "Identificar la Basílica del Pilar, el Palacio de la Aljafería (sede de las Cortes de Aragón), la arquitectura mudéjar y el Parque Nacional de Ordesa y Monte Perdido.",
                    "Practicar las construcciones «extenderse de norte a sur» y «estar atravesado por el río Ebro»."
                ],
                "vocab": [
                    {"lemma": "Aragón", "pos": "noun", "translation": "Aragon"},
                    {"lemma": "Huesca, Zaragoza y Teruel", "pos": "noun", "translation": "the three provinces of Aragon"},
                    {"lemma": "Zaragoza", "pos": "noun", "translation": "Zaragoza (capital of Aragon)"},
                    {"lemma": "la Basílica del Pilar", "pos": "noun", "translation": "Basilica of Our Lady of the Pillar (Zaragoza)"},
                    {"lemma": "el Palacio de la Aljafería", "pos": "noun", "translation": "Aljafería Palace (Islamic palace and seat of the Cortes of Aragon)"},
                    {"lemma": "el arte mudéjar aragonés", "pos": "noun", "translation": "Aragonese Mudéjar architecture (UNESCO)"},
                    {"lemma": "la jota aragonesa", "pos": "noun", "translation": "Aragonese jota (traditional music and dance)"},
                    {"lemma": "el Justicia de Aragón", "pos": "noun", "translation": "Justicia de Aragón (historic Aragonese Ombudsman)"}
                ],
                "grammar_title": "Geografía del noreste interior: las tres provincias de Aragón",
                "grammar_text": "En el examen CCSE es esencial recordar de norte a sur las **tres provincias de Aragón**: **Huesca** (en los Pirineos, donde se alzan el pico Aneto y el Parque Nacional de Ordesa y Monte Perdido), **Zaragoza** (en el valle central del río Ebro, capital autonómica) y **Teruel** (en el Sistema Ibérico al sur).",
                "grammar_examples": [
                    {"es": "La comunidad autónoma de Aragón está formada por tres provincias: Huesca, Zaragoza y Teruel.", "en": "The autonomous community of Aragon is formed by three provinces: Huesca, Zaragoza, and Teruel."},
                    {"es": "Zaragoza, bañada por el río Ebro, es la capital de Aragón y celebra las Fiestas del Pilar el 12 de octubre.", "en": "Zaragoza, on the banks of the Ebro River, is the capital of Aragon and celebrates the Pillar Festival on October 12."}
                ],
                "grammar_tip": "Recuerda para el CCSE: Huesca, Zaragoza y Teruel son las 3 provincias de Aragón; su capital es Zaragoza y su baile tradicional es la jota aragonesa.",
                "paragraphs": [
                    "Desde las cumbres más altas de los Pirineos en la frontera con Francia hasta las serranías del Sistema Ibérico en el sur, la comunidad autónoma de Aragón se extiende como un gran puente histórico entre la Meseta Central, el valle del Ebro y el Mediterráneo. Su territorio está dividido de norte a sur en tres extensas provincias: Huesca, Zaragoza y Teruel.",
                    "En el norte, la provincia de Huesca alberga las montañas más elevadas de los Pirineos, encabezadas por el pico Aneto (3.404 metros), y los cañones glaciares del Parque Nacional de Ordesa y Monte Perdido, declarado Patrimonio de la Humanidad por la UNESCO.",
                    "En el centro, atravesada por el caudaloso río Ebro, se levanta Zaragoza, capital de la provincia homónima y capital de toda la comunidad autónoma de Aragón. En sus orillas brillan dos monumentos inconfundibles: la Basílica de Nuestra Señora del Pilar —en torno a la cual se celebran cada 12 de octubre las multitudinarias Fiestas del Pilar— y el Palacio de la Aljafería, una joya del arte hispanomusulmán del siglo XI que hoy es la sede del parlamento autonómico (las Cortes de Aragón).",
                    "En el sur, la provincia de Teruel (junto con Zaragoza y Calatayud) conserva un estilo arquitectónico único declarado Patrimonio de la Humanidad: el arte mudéjar aragonés, fruto de la convivencia medieval de alarifes musulmanes y cristianos que levantaron esbeltas torres de ladrillo y cerámica vidriada.",
                    "Aragón es también la tierra natal de genios universales como el pintor Francisco de Goya (nacido en Fuendetodos, Zaragoza), el premio Nobel de Medicina Santiago Ramón y Cajal y el cineasta Luis Buñuel (nacido en Calanda, Teruel), y su folclore vibra al ritmo potente de la jota aragonesa."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las tres provincias que integran la comunidad autónoma de Aragón?",
                        "options": [
                            "Huesca, Zaragoza y Teruel",
                            "Lleida, Girona y Tarragona",
                            "Castellón, Valencia y Alicante",
                            "Álava, Bizkaia y Gipuzkoa"
                        ],
                        "correctIndex": 0,
                        "explanation": "Aragón está formada de norte a sur por las tres provincias de Huesca, Zaragoza y Teruel."
                    },
                    {
                        "question": "¿Cuál es la capital de la comunidad autónoma de Aragón, situada a orillas del río Ebro?",
                        "options": [
                            "Zaragoza",
                            "Huesca",
                            "Teruel",
                            "Logroño"
                        ],
                        "correctIndex": 0,
                        "explanation": "Zaragoza es la capital de Aragón."
                    },
                    {
                        "question": "¿Qué estilo arquitectónico de ladrillo y cerámica vidriada, muy característico de Teruel y Zaragoza, es Patrimonio de la Humanidad por la UNESCO?",
                        "options": [
                            "El arte mudéjar aragonés",
                            "El arte faraónico",
                            "El gótico báltico",
                            "El barroco colonial"
                        ],
                        "correctIndex": 0,
                        "explanation": "La arquitectura mudéjar de Aragón está declarada Patrimonio de la Humanidad por la UNESCO."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué palacio histórico de origen islámico en Zaragoza alberga hoy la sede de las Cortes de Aragón?",
                        "options": [
                            "El Palacio de la Aljafería",
                            "El Palacio de la Magdalena",
                            "El Palacio de Carlos V",
                            "El Palacio de la Generalitat"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Palacio de la Aljafería en Zaragoza es la sede de las Cortes de Aragón."
                    },
                    {
                        "prompt": "¿Cuál es el canto y baile tradicional más representativo del folclore de Aragón?",
                        "options": [
                            "La jota aragonesa",
                            "La sardana",
                            "La muñeira",
                            "El aurresku"
                        ],
                        "correctIndex": 0,
                        "explanation": "La jota aragonesa es la manifestación musical y dancística más famosa de Aragón."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Las tres provincias de Aragón son Huesca, ___ y Teruel.",
                        "answer": "Zaragoza",
                        "options": ["Zaragoza", "Cuenca", "Soria", "Lleida"],
                        "explanation": "Huesca, Zaragoza y Teruel componen Aragón.",
                        "english": "The three provinces of Aragon are Huesca, Zaragoza, and Teruel."
                    },
                    {
                        "sentence": "La Basílica de Nuestra Señora del ___ se levanta a orillas del río Ebro en Zaragoza.",
                        "answer": "Pilar",
                        "options": ["Pilar", "Naranco", "Teide", "Monfragüe"],
                        "explanation": "La Basílica del Pilar es el gran símbolo monumental de Zaragoza.",
                        "english": "The Basilica of Our Lady of the Pillar stands on the banks of the Ebro River in Zaragoza."
                    }
                ],
                "ex_dict": {
                    "audioText": "La comunidad autónoma de Aragón está formada por Huesca, Zaragoza y Teruel, y su capital es Zaragoza.",
                    "english": "The autonomous community of Aragon is formed by Huesca, Zaragoza, and Teruel, and its capital is Zaragoza."
                },
                "ex_sb": {
                    "words": ["Zaragoza", "es", "la", "capital", "de", "Aragón", "y", "está", "bañada", "por", "el", "Ebro."],
                    "english": "Zaragoza is the capital of Aragon and is bathed by the Ebro."
                }
            },
            {
                "num": "02",
                "Title": "Cataluña: Las Cuatro Provincias, Barcelona y Gaudí",
                "title": "Cataluña: Las Cuatro Provincias, Barcelona y Gaudí",
                "grammar_slug": "contar-con-cuatro-provincias-y-tres-lenguas",
                "story_slug": "cataluna",
                "story_title": "De las piedras romanas de Tarraco a la Sagrada Familia y el Día de Sant Jordi",
                "objectives": [
                    "Memorizar las cuatro provincias de Cataluña (Barcelona, Girona, Lleida y Tarragona) y su capital (Barcelona).",
                    "Identificar la Generalitat de Catalunya, las lenguas oficiales (castellano, catalán y aranés), las obras de Antoni Gaudí (Sagrada Familia, Parc Güell, La Pedrera) y tradiciones como Sant Jordi y los castells.",
                    "Practicar las construcciones «dividirse en cuatro provincias» y «celebrar la tradición del libro y la rosa»."
                ],
                "vocab": [
                    {"lemma": "Cataluña (Catalunya)", "pos": "noun", "translation": "Catalonia"},
                    {"lemma": "Barcelona, Girona, Lleida y Tarragona", "pos": "noun", "translation": "the four provinces of Catalonia"},
                    {"lemma": "la Generalitat de Catalunya", "pos": "noun", "translation": "Autonomous Government and institutions of Catalonia"},
                    {"lemma": "la Sagrada Familia / el Parc Güell", "pos": "noun", "translation": "Sagrada Familia / Park Güell (works by Antoni Gaudí in Barcelona)"},
                    {"lemma": "el modernismo catalán", "pos": "noun", "translation": "Catalan Modernisme (Art Nouveau architecture)"},
                    {"lemma": "los castells (castellers)", "pos": "noun", "translation": "human towers (UNESCO Intangible Heritage)"},
                    {"lemma": "la sardana", "pos": "noun", "translation": "sardana (traditional Catalan circle dance)"},
                    {"lemma": "Sant Jordi (23 de abril)", "pos": "noun", "translation": "Saint George's Day (Day of the Book and the Rose)"}
                ],
                "grammar_title": "Geografía y cultura de Cataluña: cuatro provincias y la institución de la Generalitat",
                "grammar_text": "En el examen CCSE se pregunta tanto por las **cuatro provincias de Cataluña** (**Barcelona, Girona, Lleida y Tarragona**) como por el nombre de su institución de autogobierno (**la Generalitat de Catalunya**, integrada por el Parlament y el Govern) y por el arquitecto modernista **Antoni Gaudí**, autor de la **Sagrada Familia** y el **Parc Güell** en Barcelona.",
                "grammar_examples": [
                    {"es": "Cataluña está formada por cuatro provincias: Barcelona, Girona, Lleida y Tarragona, y su capital es Barcelona.", "en": "Catalonia is formed by four provinces: Barcelona, Girona, Lleida, and Tarragona, and its capital is Barcelona."},
                    {"es": "La Sagrada Familia y el Parc Güell de Barcelona fueron diseñados por el arquitecto Antoni Gaudí.", "en": "The Sagrada Familia and Park Güell in Barcelona were designed by the architect Antoni Gaudí."}
                ],
                "grammar_tip": "Tres claves de Cataluña para el CCSE: 1) 4 provincias: Barcelona, Girona, Lleida (la única sin costa) y Tarragona. 2) Arquitecto de la Sagrada Familia: Antoni Gaudí. 3) Baile tradicional: la sardana.",
                "paragraphs": [
                    "Situada en el extremo noreste de la península ibérica, entre la frontera de los Pirineos con Francia y Andorra y las aguas del mar Mediterráneo, se encuentra Cataluña (Catalunya). Su institución de autogobierno recibe el nombre histórico de Generalitat de Catalunya y en su territorio son oficiales el castellano, el catalán y el aranés (hablado en el pirenaico Valle de Arán).",
                    "Cataluña se divide en cuatro provincias: tres de ellas bañadas por el mar Mediterráneo —Girona (con la Costa Brava y el Museo Dalí en Figueres), Barcelona y Tarragona (donde desemboca el río Ebro y se conserva el impresionante conjunto arqueológico romano de Tarraco)—, y una provincia interior y pirenaica, Lleida, donde se alza el Parque Nacional de Aigüestortes i Estany de Sant Maurici y las iglesias románicas del Valle de Boí.",
                    "Su capital, Barcelona, es una de las grandes metrópolis culturales, económicas y portuarias del Mediterráneo y fue sede de los inolvidables Juegos Olímpicos de 1992. El paisaje urbano de Barcelona está marcado por el modernismo catalán de finales del siglo XIX y principios del XX, liderado por el genial arquitecto Antoni Gaudí, autor de la Basílica de la Sagrada Familia, el Parc Güell, la Casa Batlló y la Casa Milà (La Pedrera), junto al Palau de la Música Catalana de Lluís Domènech i Montaner.",
                    "Entre las tradiciones culturales catalanas más queridas destacan el baile colectivo en círculo de la sardana y las impresionantes torres humanas llamadas «castells» (levantadas por las cuadrillas de «castellers» al son de las grallas), declaradas Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO.",
                    "Además de su fiesta oficial del 11 de septiembre (la Diada), cada 23 de abril Cataluña vive una de las jornadas más hermosas de la cultura europea: el Día de Sant Jordi, coincidiendo con el Día Internacional del Libro, en el que las calles se llenan de puestos de libros y los ciudadanos se regalan mutuamente un libro y una rosa."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las cuatro provincias que forman la comunidad autónoma de Cataluña?",
                        "options": [
                            "Barcelona, Girona, Lleida y Tarragona",
                            "Castellón, Valencia, Alicante y Murcia",
                            "Huesca, Zaragoza, Teruel y Soria",
                            "A Coruña, Lugo, Ourense y Pontevedra"
                        ],
                        "correctIndex": 0,
                        "explanation": "Cataluña está integrada por las cuatro provincias de Barcelona, Girona, Lleida y Tarragona."
                    },
                    {
                        "question": "¿Quién fue el arquitecto modernista autor de la Sagrada Familia, el Parc Güell y La Pedrera en Barcelona?",
                        "options": [
                            "Antoni Gaudí",
                            "Santiago Calatrava",
                            "Rafael Moneo",
                            "Juan de Herrera"
                        ],
                        "correctIndex": 0,
                        "explanation": "Antoni Gaudí (1852–1926) es el máximo exponente del modernismo catalán y autor de la Sagrada Familia."
                    },
                    {
                        "question": "¿Cuál es la danza tradicional de Cataluña que se baila en círculo dándose las manos?",
                        "options": [
                            "La sardana",
                            "La jota",
                            "La sevillana",
                            "El chotis"
                        ],
                        "correctIndex": 0,
                        "explanation": "La sardana es el baile tradicional en círculo propio de Cataluña."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál de las cuatro provincias de Cataluña es la única que no tiene costa en el mar Mediterráneo?",
                        "options": [
                            "Lleida",
                            "Girona",
                            "Tarragona",
                            "Barcelona"
                        ],
                        "correctIndex": 0,
                        "explanation": "Lleida es la única provincia interior de Cataluña."
                    },
                    {
                        "prompt": "¿En qué año acogió la ciudad de Barcelona los Juegos Olímpicos de verano?",
                        "options": [
                            "En 1992",
                            "En 1978",
                            "En 2004",
                            "En 1982"
                        ],
                        "correctIndex": 0,
                        "explanation": "Barcelona organizó los Juegos Olímpicos de 1992."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Las cuatro provincias de Cataluña son Barcelona, Girona, ___ y Tarragona.",
                        "answer": "Lleida",
                        "options": ["Lleida", "Huesca", "Castellón", "Teruel"],
                        "explanation": "Barcelona, Girona, Lleida y Tarragona componen Cataluña.",
                        "english": "The four provinces of Catalonia are Barcelona, Girona, Lleida, and Tarragona."
                    },
                    {
                        "sentence": "La Basílica de la Sagrada Familia de Barcelona es la obra maestra del arquitecto Antoni ___.",
                        "answer": "Gaudí",
                        "options": ["Gaudí", "Velázquez", "Goya", "Sorolla"],
                        "explanation": "Antoni Gaudí proyectó la Sagrada Familia de Barcelona.",
                        "english": "The Basilica of the Sagrada Familia in Barcelona is the masterpiece of the architect Antoni Gaudí."
                    }
                ],
                "ex_dict": {
                    "audioText": "Cataluña está formada por las provincias de Barcelona, Girona, Lleida y Tarragona.",
                    "english": "Catalonia is formed by the provinces of Barcelona, Girona, Lleida, and Tarragona."
                },
                "ex_sb": {
                    "words": ["La", "Sagrada", "Familia", "de", "Barcelona", "fue", "diseñada", "por", "Antoni", "Gaudí."],
                    "english": "The Sagrada Familia in Barcelona was designed by Antoni Gaudí."
                }
            },
            {
                "num": "03",
                "Title": "La Comunitat Valenciana: Castellón, Valencia, Alicante y Fallas",
                "title": "La Comunitat Valenciana: Castellón, Valencia, Alicante y Fallas",
                "grammar_slug": "de-norte-a-sur-castellon-valencia-alicante",
                "story_slug": "valencia",
                "story_title": "Fuego de Fallas en marzo, la Lonja de la Seda y el sol del Mediterráneo",
                "objectives": [
                    "Memorizar de norte a sur las tres provincias de la Comunitat Valenciana (Castellón, Valencia y Alicante) y su capital (Valencia).",
                    "Conocer las Fallas de Valencia (del 15 al 19 de marzo), las Hogueras de San Juan en Alicante, la Ciudad de las Artes y las Ciencias, la Lonja de la Seda y la paella.",
                    "Practicar las construcciones «celebrarse en el mes de marzo» y «estar bañada por el río Turia»."
                ],
                "vocab": [
                    {"lemma": "la Comunitat Valenciana (Comunidad Valenciana)", "pos": "noun", "translation": "Valencian Community"},
                    {"lemma": "Castellón, Valencia y Alicante", "pos": "noun", "translation": "the three provinces of the Valencian Community"},
                    {"lemma": "las Fallas de Valencia", "pos": "noun", "translation": "Fallas festival of Valencia (March 15–19, UNESCO)"},
                    {"lemma": "la cremà", "pos": "noun", "translation": "the burning of the fallas monuments on the night of March 19"},
                    {"lemma": "la Ciudad de las Artes y las Ciencias", "pos": "noun", "translation": "City of Arts and Sciences (Valencia)"},
                    {"lemma": "la Lonja de la Seda", "pos": "noun", "translation": "Silk Exchange (Gothic building in Valencia, UNESCO)"},
                    {"lemma": "el Tribunal de las Aguas de Valencia", "pos": "noun", "translation": "Water Tribunal of Valencia (oldest justice institution in Europe)"},
                    {"lemma": "la paella valenciana / la horchata", "pos": "noun", "translation": "Valencian paella / tiger nut milk (horchata)"}
                ],
                "grammar_title": "Geografía y fiestas levantinas: las tres provincias valencianas",
                "grammar_text": "La **Comunitat Valenciana** se extiende a lo largo de la costa oriental mediterránea dividida de norte a sur en **tres provincias**: **Castellón** (Castelló), **Valencia** (València, capital de la comunidad) y **Alicante** (Alacant). Sus dos lenguas oficiales son el castellano y el **valenciano**.",
                "grammar_examples": [
                    {"es": "La Comunidad Valenciana está formada de norte a sur por las provincias de Castellón, Valencia y Alicante.", "en": "The Valencian Community is formed from north to south by the provinces of Castellón, Valencia, and Alicante."},
                    {"es": "Las Fallas de Valencia se celebran cada mes de marzo y culminan la noche del 19 de marzo con la cremà.", "en": "The Fallas of Valencia are celebrated every March and culminate on the night of March 19 with the cremà."}
                ],
                "grammar_tip": "Dos preguntas muy frecuentes en el CCSE: 1) Las 3 provincias de la Comunidad Valenciana son Castellón, Valencia y Alicante. 2) Las Fallas se celebran en Valencia en el mes de marzo (del 15 al 19 de marzo, San José).",
                "paragraphs": [
                    "Al sur de Cataluña y al este de Aragón y Castilla-La Mancha se abre al mar Mediterráneo la Comunitat Valenciana (Comunidad Valenciana), tierra de luz inmortalizada en los lienzos del pintor valenciano Joaquín Sorolla. Su institución de autogobierno es la Generalitat Valenciana y sus ciudadanos cuentan con dos lenguas oficiales: el castellano y el valenciano.",
                    "Para el examen CCSE es fundamental recordar de norte a sur sus tres provincias costeras: Castellón (con la Costa del Azahar y castillos como el de Peñíscola), Valencia (en el centro, donde desembocan los ríos Turia y Júcar y se extiende el parque natural de la Albufera) y Alicante (al sur, famosa por la Costa Blanca, el Palmeral de Elche y el Misteri d'Elx).",
                    "La ciudad de Valencia, tercera más poblada de España, combina siglos de historia con la arquitectura del siglo XXI: en su casco histórico brillan la gótica Lonja de la Seda (Patrimonio de la Humanidad) y la puerta de la Catedral donde cada jueves a las doce del mediodía se reúne en valenciano el milenario Tribunal de las Aguas para resolver de forma oral los conflictos de riego de la huerta; mientras que en el antiguo cauce ajardinado del río Turia se levanta la futurista Ciudad de las Artes y las Ciencias, diseñada por Santiago Calatrava y Félix Candela.",
                    "Cada primavera, del 15 al 19 de marzo (festividad de San José), Valencia vive su fiesta más universal, declarada Patrimonio Cultural Inmaterial de la Humanidad: las Fallas. Cientos de monumentos artísticos y satíricos («ninots») llenan las plazas entre pasacalles, ofrendas florales y el estruendo diario de las «mascletàs», hasta arder en las llamas purificadoras de «la cremà» la noche del 19 de marzo. En junio, Alicante celebra una fiesta hermana del fuego: las Hogueras de San Juan.",
                    "Por último, Valencia ha regalado a la gastronomía mundial el plato más internacional de la cocina española: la paella, nacida en las tierras de arrozales de la Albufera de Valencia, acompañada de los cítricos de su huerta, el turrón alicantino de Jijona y Alicante, y la refrescante horchata de chufa."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son, de norte a sur, las tres provincias que integran la Comunidad Valenciana?",
                        "options": [
                            "Castellón, Valencia y Alicante",
                            "Barcelona, Girona y Tarragona",
                            "Huesca, Zaragoza y Teruel",
                            "Almería, Granada y Málaga"
                        ],
                        "correctIndex": 0,
                        "explanation": "De norte a sur, la Comunidad Valenciana está integrada por las provincias de Castellón, Valencia y Alicante."
                    },
                    {
                        "question": "¿En qué ciudad y en qué mes se celebran las famosas fiestas de las Fallas, declaradas Patrimonio de la Humanidad?",
                        "options": [
                            "En Valencia, en el mes de marzo (del 15 al 19 de marzo)",
                            "En Pamplona, en el mes de julio",
                            "En Sevilla, en el mes de abril",
                            "En Santander, en el mes de agosto"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Fallas se celebran en Valencia del 15 al 19 de marzo y terminan con «la cremà» la noche de San José."
                    },
                    {
                        "question": "¿Qué complejo arquitectónico y cultural vanguardista se levanta en el antiguo cauce del río Turia en la ciudad de Valencia?",
                        "options": [
                            "La Ciudad de las Artes y las Ciencias",
                            "El Museo Guggenheim",
                            "La Alhambra",
                            "El Teatro Romano de Mérida"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Ciudad de las Artes y las Ciencias es el gran emblema contemporáneo de la ciudad de Valencia."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál es el plato de arroz más famoso de la gastronomía de la Comunidad Valenciana e icono internacional de la cocina española?",
                        "options": [
                            "La paella",
                            "La fabada",
                            "El pulpo á feira",
                            "El marmitako"
                        ],
                        "correctIndex": 0,
                        "explanation": "La paella es el plato tradicional nacido en la huerta y la Albufera de Valencia."
                    },
                    {
                        "prompt": "¿Qué edificio gótico mercantil del siglo XV situado en el centro de Valencia es Patrimonio de la Humanidad por la UNESCO?",
                        "options": [
                            "La Lonja de la Seda",
                            "La Torre de Hércules",
                            "El Acueducto de Segovia",
                            "La Giralda"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Lonja de la Seda de Valencia es una obra maestra del gótico civil mediterráneo declarada Patrimonio de la Humanidad."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Las tres provincias de la Comunidad Valenciana son Castellón, ___ y Alicante.",
                        "answer": "Valencia",
                        "options": ["Valencia", "Murcia", "Albacete", "Tarragona"],
                        "explanation": "Castellón, Valencia y Alicante forman la Comunidad Valenciana.",
                        "english": "The three provinces of the Valencian Community are Castellón, Valencia, and Alicante."
                    },
                    {
                        "sentence": "Las fiestas de las ___ se celebran en Valencia cada mes de marzo y terminan el día 19 con la cremà.",
                        "answer": "Fallas",
                        "options": ["Fallas", "Cruces", "Médulas", "Rías"],
                        "explanation": "Las Fallas de Valencia culminan la noche del 19 de marzo.",
                        "english": "The Fallas festival is celebrated in Valencia every March and ends on the 19th with the cremà."
                    }
                ],
                "ex_dict": {
                    "audioText": "La Comunidad Valenciana está formada por Castellón, Valencia y Alicante, y celebra las Fallas en marzo.",
                    "english": "The Valencian Community is formed by Castellón, Valencia, and Alicante, and celebrates the Fallas in March."
                },
                "ex_sb": {
                    "words": ["La", "Ciudad", "de", "las", "Artes", "y", "las", "Ciencias", "está", "en", "Valencia."],
                    "english": "The City of Arts and Sciences is in Valencia."
                }
            },
            {
                "num": "04",
                "Title": "La Región de Murcia: Huerta de Europa y Cartagena",
                "title": "La Región de Murcia: Huerta de Europa y Cartagena",
                "grammar_slug": "conocida-como-la-huerta-de-europa",
                "story_slug": "murcia",
                "story_title": "El río Segura, el Teatro Romano de Cartagena y las aguas del Mar Menor",
                "objectives": [
                    "Identificar la Región de Murcia como comunidad autónoma uniprovincial con capital en Murcia y sede de su Asamblea Regional en Cartagena.",
                    "Conocer el río Segura, la laguna costera del Mar Menor, el Teatro Romano de Cartagena y la tradición agrícola («la Huerta de Europa»).",
                    "Practicar las expresiones «comunidad uniprovincial del sureste» y «tener la sede de la Asamblea Regional en Cartagena»."
                ],
                "vocab": [
                    {"lemma": "la Región de Murcia", "pos": "noun", "translation": "Region of Murcia"},
                    {"lemma": "Murcia", "pos": "noun", "translation": "Murcia (capital of the Region of Murcia)"},
                    {"lemma": "Cartagena", "pos": "noun", "translation": "Cartagena (historic port and seat of the Regional Assembly)"},
                    {"lemma": "el Mar Menor", "pos": "noun", "translation": "Mar Menor (coastal saltwater lagoon in Murcia)"},
                    {"lemma": "la Huerta de Europa", "pos": "noun", "translation": "the Orchard/Garden of Europe"},
                    {"lemma": "el río Segura", "pos": "noun", "translation": "Segura River"},
                    {"lemma": "el Teatro Romano de Cartagena", "pos": "noun", "translation": "Roman Theater of Cartagena"},
                    {"lemma": "el Consejo de Hombres Buenos", "pos": "noun", "translation": "Council of Good Men (traditional irrigation court of Murcia, UNESCO)"}
                ],
                "grammar_title": "Reparto institucional en una comunidad uniprovincial: Murcia y Cartagena",
                "grammar_text": "La **Región de Murcia** es una comunidad autónoma **uniprovincial** situada en el sureste de la península ibérica. Su capital y sede del Gobierno autonómico es la ciudad de **Murcia** (atravesada por el río Segura), mientras que su parlamento autonómico —la **Asamblea Regional de Murcia**— tiene su sede en la ciudad portuaria de **Cartagena**.",
                "grammar_examples": [
                    {"es": "La Región de Murcia es una comunidad autónoma uniprovincial cuya capital es la ciudad de Murcia.", "en": "The Region of Murcia is a single-province autonomous community whose capital is the city of Murcia."},
                    {"es": "En la costa de la Región de Murcia se encuentra el Mar Menor, la mayor laguna salada de España.", "en": "On the coast of the Region of Murcia lies the Mar Menor, the largest saltwater lagoon in Spain."}
                ],
                "grammar_tip": "Recuerda para el CCSE: la Región de Murcia es una de las 7 comunidades autónomas uniprovinciales de España, su capital es Murcia y está bañada por el mar Mediterráneo y el río Segura.",
                "paragraphs": [
                    "En el sureste de la península ibérica, entre Andalucía, Castilla-La Mancha, la Comunidad Valenciana y el mar Mediterráneo, se sitúa la Región de Murcia. Es una de las siete comunidades autónomas uniprovinciales de España y disfruta de más de tres mil horas de sol al año.",
                    "A pesar de contar con un clima mediterráneo seco, el aprovechamiento milenario de las aguas del río Segura y de sus acequias —cuyo reparto de riego dirime desde la Edad Media el Consejo de Hombres Buenos de la Huerta de Murcia, declarado Patrimonio Inmaterial de la Humanidad junto al Tribunal de las Aguas de Valencia— ha convertido al campo murciano en la llamada «Huerta de Europa», líder en exportación de frutas, hortalizas y flores.",
                    "La capital de la comunidad autónoma y sede del Consejo de Gobierno es la ciudad de Murcia, presidida por la magnífica fachada barroca de su Catedral de Santa María y el Real Casino. En primavera, tras su célebre Semana Santa con las tallas del escultor Francisco Salzillo, la ciudad celebra las Fiestas de Primavera y el festivo Bando de la Huerta.",
                    "En el litoral mediterráneo —conocido como la Costa Cálida— brilla la milenaria ciudad de Cartagena, fundada por el cartaginés Asdrúbal como Qart Hadasht y conquistada por el romano Escipión como Carthago Nova. En Cartagena tiene su sede el parlamento autonómico (la Asamblea Regional de Murcia), una de las principales bases de la Armada Española y el impresionante Teatro Romano de Cartagena, descubierto a finales del siglo XX.",
                    "Otro símbolo geográfico inconfundible de la Región de Murcia es el Mar Menor, una gran albufera o laguna litoral de agua salada separada del mar Mediterráneo por un estrecho cordón de arena de 22 kilómetros llamado La Manga del Mar Menor. En el interior destacan además la ciudad monumental de Lorca y el santuario de Caravaca de la Cruz."
                ],
                "questions": [
                    {
                        "question": "¿Por cuántas provincias está formada la comunidad autónoma de la Región de Murcia y cuál es su capital?",
                        "options": [
                            "Por una sola provincia (es uniprovincial) y su capital es la ciudad de Murcia",
                            "Por tres provincias y su capital es Albacete",
                            "Por cuatro provincias y su capital es Almería",
                            "Por dos provincias insulares"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Región de Murcia es una comunidad autónoma uniprovincial cuya capital es la ciudad de Murcia."
                    },
                    {
                        "question": "¿En qué ciudad portuaria e histórica de la Región de Murcia tiene su sede la Asamblea Regional (el parlamento autonómico) y el famoso Teatro Romano?",
                        "options": [
                            "En Cartagena",
                            "En Santander",
                            "En Vigo",
                            "En Gijón"
                        ],
                        "correctIndex": 0,
                        "explanation": "Cartagena alberga la sede de la Asamblea Regional de Murcia y el Teatro Romano."
                    },
                    {
                        "question": "¿Cómo se llama la gran laguna costera de agua salada situada en el litoral de la Región de Murcia, separada del Mediterráneo por La Manga?",
                        "options": [
                            "El Mar Menor",
                            "El Lago de Sanabria",
                            "Los Lagos de Covadonga",
                            "El Estanque del Retiro"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Mar Menor, en la costa de la Región de Murcia, es la mayor laguna litoral salada de España."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué río principal atraviesa la ciudad de Murcia y riega su tradicional huerta antes de desembocar en el Mediterráneo?",
                        "options": [
                            "El río Segura",
                            "El río Miño",
                            "El río Duero",
                            "El río Bidasoa"
                        ],
                        "correctIndex": 0,
                        "explanation": "El río Segura atraviesa la Región de Murcia y la ciudad de Murcia."
                    },
                    {
                        "prompt": "¿Con qué sobrenombre es conocida internacionalmente la Región de Murcia por su extraordinaria producción y exportación de frutas y hortalizas?",
                        "options": [
                            "La Huerta de Europa",
                            "La Cornisa Cantábrica",
                            "La Submeseta Norte",
                            "La Suiza Española"
                        ],
                        "correctIndex": 0,
                        "explanation": "Por su riqueza hortofrutícola, la Región de Murcia es conocida como la Huerta de Europa."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La Región de ___ es una comunidad autónoma uniprovincial situada en el sureste de España.",
                        "answer": "Murcia",
                        "options": ["Murcia", "Galicia", "Aragón", "Cataluña"],
                        "explanation": "La Región de Murcia es uniprovincial.",
                        "english": "The Region of Murcia is a single-province autonomous community located in southeastern Spain."
                    },
                    {
                        "sentence": "La Asamblea Regional de Murcia tiene su sede en la histórica ciudad portuaria de ___.",
                        "answer": "Cartagena",
                        "options": ["Cartagena", "Lugo", "Ourense", "Huesca"],
                        "explanation": "Cartagena es la sede del parlamento autonómico (Asamblea Regional) de la Región de Murcia.",
                        "english": "The Regional Assembly of Murcia has its seat in the historic port city of Cartagena."
                    }
                ],
                "ex_dict": {
                    "audioText": "La Región de Murcia es una comunidad autónoma uniprovincial bañada por el mar Mediterráneo.",
                    "english": "The Region of Murcia is a single-province autonomous community bathed by the Mediterranean Sea."
                },
                "ex_sb": {
                    "words": ["El", "río", "Segura", "atraviesa", "la", "ciudad", "de", "Murcia", "y", "su", "huerta."],
                    "english": "The Segura River flows through the city of Murcia and its orchard."
                }
            },
            {
                "num": "05",
                "Title": "Las Islas Baleares: Mallorca, Menorca, Ibiza y Formentera",
                "title": "Las Islas Baleares: Mallorca, Menorca, Ibiza y Formentera",
                "grammar_slug": "archipielago-formado-por-mallorca-menorca-ibiza",
                "story_slug": "baleares",
                "story_title": "La Seu frente al mar de Palma, las calas de Menorca y los muros blancos de Ibiza",
                "objectives": [
                    "Recordar las islas principales del archipiélago de las Islas Baleares (Mallorca, Menorca, Ibiza, Formentera y Cabrera) y su capital (Palma, en la isla de Mallorca).",
                    "Identificar su condición de comunidad autónoma uniprovincial en el mar Mediterráneo, sus Consells Insulars (Consejos Insulares) y su bilingüismo (castellano y catalán).",
                    "Practicar las construcciones «constituir una sola provincia insular» y «tener su capital en Palma»."
                ],
                "vocab": [
                    {"lemma": "las Islas Baleares (Illes Balears)", "pos": "noun", "translation": "Balearic Islands"},
                    {"lemma": "Mallorca, Menorca, Ibiza y Formentera", "pos": "noun", "translation": "the four main inhabited islands of the Balearics"},
                    {"lemma": "Palma (Palma de Mallorca)", "pos": "noun", "translation": "Palma (capital of the Balearic Islands)"},
                    {"lemma": "el Consejo Insular (Consell Insular)", "pos": "noun", "translation": "Island Council (governing body of each Balearic island)"},
                    {"lemma": "la Serra de Tramuntana", "pos": "noun", "translation": "Serra de Tramuntana mountain range in Mallorca (UNESCO)"},
                    {"lemma": "la Catedral de Mallorca (La Seu)", "pos": "noun", "translation": "Cathedral of Santa María of Palma (La Seu)"},
                    {"lemma": "la ensaimada / la sobrasada", "pos": "noun", "translation": "ensaimada pastry / sobrasada cured sausage"},
                    {"lemma": "el Archipiélago de Cabrera", "pos": "noun", "translation": "Cabrera Archipelago (National Park in the Balearics)"}
                ],
                "grammar_title": "Geografía insular mediterránea: las Islas Baleares y sus Consejos Insulares",
                "grammar_text": "A diferencia de las Islas Canarias (que tienen dos provincias y Cabildos Insulares), la comunidad autónoma de las **Islas Baleares (Illes Balears)** constituye **una sola provincia** en el mar Mediterráneo, cuya capital es **Palma** (situada en la isla de **Mallorca**), y cada isla cuenta con su propio órgano de gobierno llamado **Consejo Insular (*Consell Insular*)**.",
                "grammar_examples": [
                    {"es": "Las Islas Baleares forman una comunidad autónoma uniprovincial en el mar Mediterráneo y su capital es Palma.", "en": "The Balearic Islands form a single-province autonomous community in the Mediterranean Sea and their capital is Palma."},
                    {"es": "Las principales islas del archipiélago balear son Mallorca, Menorca, Ibiza, Formentera y Cabrera.", "en": "The main islands of the Balearic archipelago are Mallorca, Menorca, Ibiza, Formentera, and Cabrera."}
                ],
                "grammar_tip": "¡Contraste clásico del examen CCSE! En las Islas Baleares el gobierno de cada isla se llama **Consejo Insular (*Consell Insular*)** y hay **1 sola provincia**; en las Islas Canarias se llama **Cabildo Insular** y hay **2 provincias**.",
                "paragraphs": [
                    "Frente a la costa oriental de la península ibérica, en aguas del mar Mediterráneo, emerge el archipiélago de las Islas Baleares (Illes Balears en catalán, lengua cooficial de la comunidad junto al castellano). Desde el punto de vista administrativo, las Islas Baleares constituyen una de las siete comunidades autónomas uniprovinciales de España, y el gobierno y administración propios de cada isla están encomendados a los Consejos Insulares (Consells Insulars).",
                    "El archipiélago se divide tradicionalmente en dos grupos de islas: las Gimnesias al norte —integradas por Mallorca, Menorca y el pequeño archipiélago deshabitado de Cabrera, protegido como Parque Nacional Marítimo-Terrestre— y las Pitiusas («islas de pinos») al suroeste, formadas por Ibiza (Eivissa) y Formentera.",
                    "Mallorca es la isla de mayor extensión y población del archipiélago. En su bahía meridional se asienta Palma (conocida tradicionalmente como Palma de Mallorca), capital de toda la comunidad autónoma, presidida por la espectacular Catedral gótica de Santa María (llamada «La Seu») y el redondo Castillo de Bellver. En el norte de la isla se levanta la Serra de Tramuntana, paisaje cultural declarado Patrimonio de la Humanidad por la UNESCO.",
                    "Al noreste, la isla de Menorca (con ciudades históricas como Mahón y Ciutadella) fue declarada Reserva de la Biosfera en su totalidad y alberga los monumentos prehistóricos de la cultura talayótica (taulas, navetas y talayots), reconocidos como Patrimonio de la Humanidad en 2023. Al suroeste, Ibiza cuenta también con la declaración de Patrimonio Mundial por su biodiversidad marina (las praderas de posidonia oceánica que dan transparencia turquesa a sus aguas y a las de Formentera) y por la ciudad amurallada renacentista de Dalt Vila.",
                    "La gastronomía balear es célebre en toda España por dos productos con indicación geográfica protegida: la dulce y espiral ensaimada de Mallorca y la sobrasada, además del queso con denominación de origen Mahón-Menorca y la caldereta de langosta."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las cuatro islas habitadas principales del archipiélago de las Islas Baleares y cuál es su capital autonómica?",
                        "options": [
                            "Mallorca, Menorca, Ibiza y Formentera, y su capital es Palma (en Mallorca)",
                            "Tenerife, Gran Canaria, Lanzarote y Fuerteventura, y su capital es Santa Cruz",
                            "Cíes, Ons, Sálvora y Arousa, y su capital es Vigo",
                            "Córcega, Cerdeña, Sicilia y Malta"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las principales islas baleares son Mallorca, Menorca, Ibiza y Formentera (más Cabrera), y la capital es Palma."
                    },
                    {
                        "question": "¿Cómo se llaman los órganos de gobierno y administración propios de cada una de las Islas Baleares?",
                        "options": [
                            "Consejos Insulares (Consells Insulars)",
                            "Diputaciones Forales",
                            "Veguerías Pirenaicas",
                            "Mancomunidades del Norte"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 141.4 CE y el Estatuto de Autonomía balear establecen los Consejos Insulares (Consells Insulars) como gobierno insular en Baleares."
                    },
                    {
                        "question": "¿En qué mar se encuentra situado el archipiélago de las Islas Baleares?",
                        "options": [
                            "En el mar Mediterráneo",
                            "En el mar Cantábrico",
                            "En el océano Pacífico",
                            "En el mar del Norte"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Islas Baleares están situadas en el mar Mediterráneo occidental."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál es el dulce tradicional en forma de espiral más famoso de la repostería de Mallorca y de las Islas Baleares?",
                        "options": [
                            "La ensaimada",
                            "El sobao pasiego",
                            "La tarta de Santiago",
                            "El gofio"
                        ],
                        "correctIndex": 0,
                        "explanation": "La ensaimada de Mallorca y la sobrasada son los productos gastronómicos más conocidos de las Islas Baleares."
                    },
                    {
                        "prompt": "¿Cuántas provincias forman la comunidad autónoma de las Islas Baleares?",
                        "options": [
                            "Una sola provincia (es una comunidad autónoma uniprovincial)",
                            "Dos provincias",
                            "Cuatro provincias",
                            "Cinco provincias"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Islas Baleares forman una única provincia, a diferencia de Canarias que tiene dos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La capital de la comunidad autónoma de las Islas Baleares es la ciudad de ___, situada en la isla de Mallorca.",
                        "answer": "Palma",
                        "options": ["Palma", "Mahón", "Ibiza", "Arrecife"],
                        "explanation": "Palma es la capital de las Islas Baleares.",
                        "english": "The capital of the autonomous community of the Balearic Islands is the city of Palma, located on the island of Mallorca."
                    },
                    {
                        "sentence": "En las Islas Baleares, el órgano de gobierno de cada isla recibe el nombre de ___ Insular.",
                        "answer": "Consejo",
                        "options": ["Consejo", "Cabildo", "Senado", "Tribunal"],
                        "explanation": "En Baleares existen los Consejos Insulares (Consells Insulars), mientras que en Canarias se llaman Cabildos Insulares.",
                        "english": "In the Balearic Islands, the governing body of each island is called the Island Council."
                    }
                ],
                "ex_dict": {
                    "audioText": "Las Islas Baleares están en el mar Mediterráneo y su capital es Palma, en la isla de Mallorca.",
                    "english": "The Balearic Islands are in the Mediterranean Sea and their capital is Palma, on the island of Mallorca."
                },
                "ex_sb": {
                    "words": ["Mallorca,", "Menorca,", "Ibiza", "y", "Formentera", "forman", "parte", "de", "las", "Islas", "Baleares."],
                    "english": "Mallorca, Menorca, Ibiza, and Formentera are part of the Balearic Islands."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 20: Comunidades del Centro, Sur y Canarias (unit_num=56, b1-centrosur)
    # =========================================================================
    {
        "slug": "centrosur",
        "unit_num": 56,
        "title": "Comunidades del Centro, Sur y Canarias",
        "description": "Madrid, las 9 provincias de Castilla y León, Castilla-La Mancha, Extremadura, las 8 provincias de Andalucía y las 2 provincias de Canarias.",
        "Badge": "Centro, Sur y Canarias",
        "lessons": [
            {
                "num": "01",
                "Title": "La Comunidad de Madrid: Capital del Estado y Patrimonio",
                "title": "La Comunidad de Madrid: Capital del Estado y Patrimonio",
                "grammar_slug": "la-capital-del-estado-es-la-villa-de-madrid",
                "story_slug": "madrid",
                "story_title": "El kilómetro cero en la Puerta del Sol, el Paseo del Prado y la sierra de Guadarrama",
                "objectives": [
                    "Recordar el artículo 5 de la Constitución Española: «La capital del Estado es la villa de Madrid».",
                    "Identificar la Comunidad de Madrid como comunidad uniprovincial y sus lugares Patrimonio de la Humanidad: Alcalá de Henares, San Lorenzo de El Escorial, Aranjuez y el Paisaje de la Luz (Paseo del Prado y el Retiro).",
                    "Practicar la fórmula «la capital del Estado es la villa de Madrid»."
                ],
                "vocab": [
                    {"lemma": "la villa de Madrid", "pos": "noun", "translation": "the town/city of Madrid (constitutional title)"},
                    {"lemma": "la Puerta del Sol (el Kilómetro Cero)", "pos": "noun", "translation": "Puerta del Sol (Kilometer Zero of Spain's radial roads)"},
                    {"lemma": "el Paseo del Prado y el Buen Retiro", "pos": "noun", "translation": "Paseo del Prado and Buen Retiro ('Landscape of Light', UNESCO)"},
                    {"lemma": "el Museo del Prado / el Museo Reina Sofía", "pos": "noun", "translation": "Prado Museum / Reina Sofía Museum"},
                    {"lemma": "San Lorenzo de El Escorial", "pos": "noun", "translation": "Monastery of San Lorenzo de El Escorial (UNESCO)"},
                    {"lemma": "Alcalá de Henares", "pos": "noun", "translation": "Alcalá de Henares (birthplace of Cervantes and historic University, UNESCO)"},
                    {"lemma": "el Paisaje Cultural de Aranjuez", "pos": "noun", "translation": "Cultural Landscape of Aranjuez (UNESCO)"},
                    {"lemma": "San Isidro Labrador (15 de mayo)", "pos": "noun", "translation": "Saint Isidore the Laborer (patron saint of Madrid, May 15)"}
                ],
                "grammar_title": "El artículo 5 de la Constitución: «La capital del Estado es la villa de Madrid»",
                "grammar_text": "El **artículo 5 de la Constitución Española** consta de una sola frase que se pregunta literalmente en el examen CCSE: **«La capital del Estado es la villa de Madrid»**. Además, la **Comunidad de Madrid** es una de las siete comunidades autónomas **uniprovinciales** de España.",
                "grammar_examples": [
                    {"es": "Según el artículo 5 de la Constitución Española, la capital del Estado es la villa de Madrid.", "en": "According to Article 5 of the Spanish Constitution, the capital of the State is the city of Madrid."},
                    {"es": "En el Paseo del Prado de Madrid se concentran los museos del Prado, Thyssen-Bornemisza y Reina Sofía.", "en": "On the Paseo del Prado in Madrid are concentrated the Prado, Thyssen-Bornemisza, and Reina Sofía museums."}
                ],
                "grammar_tip": "Recuerda para el CCSE: la Comunidad de Madrid es uniprovincial, su fiesta autonómica es el 2 de mayo y la fiesta del patrón de la ciudad de Madrid (San Isidro) es el 15 de mayo.",
                "paragraphs": [
                    "En el centro geográfico de la península ibérica, al pie de la vertiente sur de la sierra de Guadarrama, se sitúa la Comunidad de Madrid. Es una de las siete comunidades autónomas uniprovinciales de España y la tercera más poblada del país, conerca de siete millones de habitantes.",
                    "Su capital, Madrid, ostenta desde 1561 la capitalidad de España, consagrada hoy en el artículo 5 de la Constitución Española con una frase solemne: «La capital del Estado es la villa de Madrid». En la Puerta del Sol —donde se encuentra la Real Casa de Correos, sede de la Presidencia de la Comunidad de Madrid, y cuyo reloj marca las doce campanadas de Nochevieja— una placa en el suelo señala el «Kilómetro Cero» de las seis grandes carreteras radiales del Estado.",
                    "Como capital de España, Madrid acoge las sedes de las altas instituciones del Estado: el Palacio de la Zarzuela y el Palacio Real (Jefatura del Estado), el Palacio de las Cortes en la Carrera de San Jerónimo (Congreso de los Diputados) y la Plaza de la Marina Española (Senado), el Palacio de la Moncloa (Presidencia del Gobierno), el Tribunal Supremo y el Tribunal Constitucional.",
                    "El corazón cultural de la ciudad es el «Paisaje de la Luz» (el Paseo del Prado y el Parque del Buen Retiro, declarado Patrimonio de la Humanidad por la UNESCO en 2021), donde en apenas un kilómetro se reúnen tres de las pinacotecas más importantes del mundo: el Museo Nacional del Prado (con obras maestras de Velázquez, Goya y El Bosco), el Museo Nacional Centro de Arte Reina Sofía (donde se exhibe el *Guernica* de Pablo Picasso) y el Museo Nacional Thyssen-Bornemisza.",
                    "Además, dentro de la Comunidad de Madrid existen otros tres conjuntos declarados Patrimonio de la Humanidad: el Monasterio y Real Sitio de San Lorenzo de El Escorial (del siglo XVI), el Paisaje Cultural del Real Sitio de Aranjuez a orillas del Tajo, y la Universidad y recinto histórico de Alcalá de Henares, ciudad natal de Miguel de Cervantes."
                ],
                "questions": [
                    {
                        "question": "Según el artículo 5 de la Constitución Española, ¿cuál es la capital del Estado?",
                        "options": [
                            "La villa de Madrid",
                            "La ciudad de Toledo",
                            "La ciudad de Valladolid",
                            "La ciudad de Sevilla"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 5 CE establece textualmente: «La capital del Estado es la villa de Madrid»."
                    },
                    {
                        "question": "¿En qué museo de Madrid se encuentra expuesto el famoso cuadro «Guernica» de Pablo Picasso?",
                        "options": [
                            "En el Museo Nacional Centro de Arte Reina Sofía",
                            "En el Museo Arqueológico Nacional",
                            "En el Museo Naval",
                            "En el Museo Sorolla"
                        ],
                        "correctIndex": 0,
                        "explanation": "El «Guernica» de Pablo Picasso se exhibe en el Museo Reina Sofía de Madrid."
                    },
                    {
                        "question": "¿Qué tres localidades de la Comunidad de Madrid cuentan con conjuntos históricos declarados Patrimonio de la Humanidad por la UNESCO, además del Paseo del Prado y el Retiro?",
                        "options": [
                            "Alcalá de Henares, San Lorenzo de El Escorial y Aranjuez",
                            "Getafe, Leganés y Alcorcón",
                            "Móstoles, Fuenlabrada y Parla",
                            "Torrejón, Coslada y Alcobendas"
                        ],
                        "correctIndex": 0,
                        "explanation": "Alcalá de Henares, San Lorenzo de El Escorial y Aranjuez son Patrimonio de la Humanidad en la Comunidad de Madrid."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Por cuántas provincias está formada la Comunidad de Madrid?",
                        "options": [
                            "Por una sola provincia (es una comunidad autónoma uniprovincial)",
                            "Por cinco provincias",
                            "Por nueve provincias",
                            "Por dos provincias"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Comunidad de Madrid es una comunidad autónoma uniprovincial."
                    },
                    {
                        "prompt": "¿Qué plaza del centro de Madrid alberga el «Kilómetro Cero» de las carreteras radiales españolas y el famoso reloj de las campanadas de fin de año?",
                        "options": [
                            "La Puerta del Sol",
                            "La Plaza de Oriente",
                            "La Plaza de Castilla",
                            "La Glorieta de Atocha"
                        ],
                        "correctIndex": 0,
                        "explanation": "En la Puerta del Sol se sitúan la placa del Kilómetro Cero y el reloj de la Real Casa de Correos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Según el artículo 5 de la Constitución, la capital del Estado es la ___ de Madrid.",
                        "answer": "villa",
                        "options": ["villa", "isla", "ría", "veguería"],
                        "explanation": "«La capital del Estado es la villa de Madrid» (Art. 5 CE).",
                        "english": "According to Article 5 of the Constitution, the capital of the State is the city (villa) of Madrid."
                    },
                    {
                        "sentence": "La ciudad de Alcalá de ___, en la Comunidad de Madrid, es la cuna de Miguel de Cervantes.",
                        "answer": "Henares",
                        "options": ["Henares", "Tormes", "Guadiana", "Barrameda"],
                        "explanation": "Miguel de Cervantes nació en Alcalá de Henares (Madrid) en 1547.",
                        "english": "The city of Alcalá de Henares, in the Community of Madrid, is the birthplace of Miguel de Cervantes."
                    }
                ],
                "ex_dict": {
                    "audioText": "Según el artículo cinco de la Constitución, la capital del Estado es la villa de Madrid.",
                    "english": "According to Article five of the Constitution, the capital of the State is the city of Madrid."
                },
                "ex_sb": {
                    "words": ["El", "Museo", "del", "Prado", "y", "el", "Parque", "del", "Retiro", "están", "en", "Madrid."],
                    "english": "The Prado Museum and the Retiro Park are in Madrid."
                }
            },
            {
                "num": "02",
                "Title": "Castilla y León: Las Nueve Provincias de la Submeseta Norte",
                "title": "Castilla y León: Las Nueve Provincias de la Submeseta Norte",
                "grammar_slug": "la-comunidad-mas-extensa-integrada-por-nueve-provincias",
                "story_slug": "castillayleon",
                "story_title": "Nueve provincias bañadas por el Duero: de la Universidad de Salamanca al Acueducto de Segovia",
                "objectives": [
                    "Memorizar que Castilla y León es la comunidad autónoma más extensa de España y tiene 9 provincias: Ávila, Burgos, León, Palencia, Salamanca, Segovia, Soria, Valladolid y Zamora.",
                    "Identificar que las instituciones autonómicas (Junta y Cortes de Castilla y León) tienen su sede en Valladolid, y conocer monumentos clave como el Acueducto de Segovia, la Muralla de Ávila, la Catedral de Burgos y la Universidad de Salamanca.",
                    "Practicar las construcciones «ser la comunidad autónoma con mayor número de provincias»."
                ],
                "vocab": [
                    {"lemma": "Castilla y León", "pos": "noun", "translation": "Castile and León (largest autonomous community in Spain, 9 provinces)"},
                    {"lemma": "Valladolid", "pos": "noun", "translation": "Valladolid (seat of the regional government and Cortes of Castile and León)"},
                    {"lemma": "el Acueducto de Segovia", "pos": "noun", "translation": "Roman Aqueduct of Segovia (UNESCO)"},
                    {"lemma": "la Universidad de Salamanca", "pos": "noun", "translation": "University of Salamanca (founded in 1218, oldest in Spain)"},
                    {"lemma": "la Catedral de Burgos / Atapuerca", "pos": "noun", "translation": "Cathedral of Burgos / Atapuerca archaeological site (UNESCO)"},
                    {"lemma": "la Muralla de Ávila", "pos": "noun", "translation": "Medieval Walls of Ávila (UNESCO)"},
                    {"lemma": "Las Médulas (León)", "pos": "noun", "translation": "Las Médulas (Roman gold mines in León, UNESCO)"},
                    {"lemma": "la cuenca del río Duero", "pos": "noun", "translation": "Douro River basin"}
                ],
                "grammar_title": "Superlativos territoriales: las nueve provincias de Castilla y León",
                "grammar_text": "**Castilla y León** ostenta dos récords geográficos que suelen preguntarse en el examen CCSE: es la **comunidad autónoma más extensa de España** (con más de 94.000 km²) y la que tiene **mayor número de provincias: nueve** (**Ávila, Burgos, León, Palencia, Salamanca, Segovia, Soria, Valladolid y Zamora**). La sede de la Junta y de las Cortes de Castilla y León está en **Valladolid**.",
                "grammar_examples": [
                    {"es": "Castilla y León es la comunidad autónoma más extensa de España y está integrada por nueve provincias.", "en": "Castile and León is the largest autonomous community in Spain and is made up of nine provinces."},
                    {"es": "La Universidad de Salamanca, fundada en 1218, es la universidad en activo más antigua de España.", "en": "The University of Salamanca, founded in 1218, is the oldest active university in Spain."}
                ],
                "grammar_tip": "¡Pregunta estrella de la Tarea 3 del CCSE! ¿Cuántas provincias tiene Castilla y León? **Nueve (9)**: Ávila, Burgos, León, Palencia, Salamanca, Segovia, Soria, Valladolid y Zamora.",
                "paragraphs": [
                    "Ocupando toda la inmensa llanura de la Submeseta Norte y rodeada por la Cordillera Cantábrica, el Sistema Ibérico y el Sistema Central, se extiende Castilla y León. Con más de 94.000 kilómetros cuadrados (una superficie mayor que la de países enteros como Portugal, Austria o Bélgica), es la comunidad autónoma más extensa de España y una de las mayores regiones de la Unión Europea.",
                    "Para el examen CCSE es imprescindible saber que Castilla y León es la comunidad autónoma con mayor número de provincias: cuenta con nueve provincias —Ávila, Burgos, León, Palencia, Salamanca, Segovia, Soria, Valladolid y Zamora—, todas ellas vertebradas por la cuenca del río Duero. Aunque su Estatuto de Autonomía no declara formalmente una capital, la ley fija en la ciudad de Valladolid la sede de las instituciones básicas de autogobierno: la Junta de Castilla y León y las Cortes de Castilla y León.",
                    "Ninguna otra región del mundo concentra tantos bienes declarados Patrimonio de la Humanidad por la UNESCO. En Segovia se levanta su colosal Acueducto romano del siglo II, construido con sillares de granito unidos sin argamasa, junto a su Alcázar. En Ávila se conserva intacta su imponente Muralla medieval del siglo XI con ochenta y siete torreones, en la ciudad natal de Santa Teresa de Jesús.",
                    "En Salamanca brillan su Plaza Mayor barroca y la Universidad de Salamanca, fundada en 1218 por el rey Alfonso IX de León, que es la universidad en activo más antigua de España y de todo el mundo hispánico. En Burgos se alzan su prodigiosa Catedral gótica y los yacimientos prehistóricos de la Sierra de Atapuerca, clave para estudiar la evolución humana en Europa.",
                    "Por su parte, la provincia de León atesora la Catedral de León (con sus célebres vidrieras góticas), el paisaje rojizo de las antiguas minas de oro romanas de Las Médulas y la vertiente leonesa de los Picos de Europa, mientras que el Camino de Santiago Francés recorre de este a oeste las tierras de Burgos, Palencia y León."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la comunidad autónoma más extensa de España y cuántas provincias la integran?",
                        "options": [
                            "Castilla y León, integrada por 9 provincias (Ávila, Burgos, León, Palencia, Salamanca, Segovia, Soria, Valladolid y Zamora)",
                            "Andalucía, integrada por 12 provincias",
                            "Cataluña, integrada por 3 provincias",
                            "Galicia, integrada por 6 provincias"
                        ],
                        "correctIndex": 0,
                        "explanation": "Castilla y León es la comunidad más extensa de España y cuenta con 9 provincias."
                    },
                    {
                        "question": "¿En qué ciudad de Castilla y León se encuentra el famoso Acueducto romano de piedra construido sin argamasa?",
                        "options": [
                            "En Segovia",
                            "En Soria",
                            "En Palencia",
                            "En Valladolid"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Acueducto de Segovia es una de las obras de ingeniería romana mejor conservadas del mundo."
                    },
                    {
                        "question": "¿En qué ciudad de Castilla y León se encuentra la universidad en activo más antigua de España, fundada en 1218?",
                        "options": [
                            "En Salamanca (Universidad de Salamanca)",
                            "En Ávila",
                            "En Zamora",
                            "En Teruel"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Universidad de Salamanca (1218) es la más antigua de las universidades españolas existentes."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué ciudad tienen su sede la Junta de Castilla y León y las Cortes de Castilla y León?",
                        "options": [
                            "En Valladolid",
                            "En Santander",
                            "En Logroño",
                            "En Toledo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Valladolid es la sede de las instituciones de autogobierno de Castilla y León (y sede de la Semana Internacional de Cine, SEMINCI)."
                    },
                    {
                        "prompt": "¿En qué provincia de Castilla y León se encuentran los famosos yacimientos prehistóricos de Atapuerca y una célebre Catedral gótica?",
                        "options": [
                            "En Burgos",
                            "En Zamora",
                            "En Soria",
                            "En Ávila"
                        ],
                        "correctIndex": 0,
                        "explanation": "Tanto la Catedral de Burgos como los yacimientos de la Sierra de Atapuerca están en la provincia de Burgos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Castilla y León es la comunidad autónoma más extensa de España y está formada por ___ provincias.",
                        "answer": "nueve",
                        "options": ["nueve", "cuatro", "ocho", "cinco"],
                        "explanation": "Castilla y León tiene 9 provincias.",
                        "english": "Castile and León is the largest autonomous community in Spain and is formed by nine provinces."
                    },
                    {
                        "sentence": "El famoso Acueducto romano se encuentra en la ciudad castellana de ___.",
                        "answer": "Segovia",
                        "options": ["Segovia", "Salamanca", "Soria", "Palencia"],
                        "explanation": "El Acueducto de Segovia es el símbolo monumental de la ciudad.",
                        "english": "The famous Roman Aqueduct is located in the Castilian city of Segovia."
                    }
                ],
                "ex_dict": {
                    "audioText": "Castilla y León está formada por nueve provincias y la sede de sus instituciones está en Valladolid.",
                    "english": "Castile and León is formed by nine provinces and the seat of its institutions is in Valladolid."
                },
                "ex_sb": {
                    "words": ["La", "Universidad", "de", "Salamanca", "es", "la", "más", "antigua", "de", "España."],
                    "english": "The University of Salamanca is the oldest in Spain."
                }
            },
            {
                "num": "03",
                "Title": "Castilla-La Mancha y Extremadura: Toledo, Cuenca y Mérida",
                "title": "Castilla-La Mancha y Extremadura: Toledo, Cuenca y Mérida",
                "grammar_slug": "cinco-provincias-manchegas-y-dos-extremenas",
                "story_slug": "castillalamanchayextremadura",
                "story_title": "Molinos del Quijote en La Mancha y el Teatro Romano de Mérida",
                "objectives": [
                    "Memorizar las 5 provincias de Castilla-La Mancha (Albacete, Ciudad Real, Cuenca, Guadalajara y Toledo; capital Toledo) y las 2 provincias de Extremadura (Cáceres y Badajoz; capital Mérida).",
                    "Identificar a Toledo como «la Ciudad de las Tres Culturas», las Casas Colgadas de Cuenca, los molinos del Quijote y el Teatro Romano de Mérida.",
                    "Practicar el contraste entre las cinco provincias de Castilla-La Mancha y las dos provincias de Extremadura."
                ],
                "vocab": [
                    {"lemma": "Castilla-La Mancha", "pos": "noun", "translation": "Castile-La Mancha (5 provinces: Albacete, Ciudad Real, Cuenca, Guadalajara, Toledo)"},
                    {"lemma": "Toledo", "pos": "noun", "translation": "Toledo (capital of Castile-La Mancha, 'City of the Three Cultures')"},
                    {"lemma": "las Casas Colgadas de Cuenca", "pos": "noun", "translation": "Hanging Houses of Cuenca (UNESCO)"},
                    {"lemma": "Extremadura", "pos": "noun", "translation": "Extremadura (2 provinces: Cáceres and Badajoz)"},
                    {"lemma": "Cáceres y Badajoz", "pos": "noun", "translation": "the two provinces of Extremadura"},
                    {"lemma": "Mérida", "pos": "noun", "translation": "Mérida (capital of Extremadura, located in the province of Badajoz)"},
                    {"lemma": "el Teatro Romano de Mérida", "pos": "noun", "translation": "Roman Theater of Mérida (UNESCO)"},
                    {"lemma": "la dehesa / el jamón ibérico", "pos": "noun", "translation": "dehesa oak pastureland / Iberian cured ham"}
                ],
                "grammar_title": "Submeseta Sur: las 5 provincias de Castilla-La Mancha y las 2 de Extremadura",
                "grammar_text": "La Submeseta Sur está ocupada por dos grandes comunidades autónomas: **Castilla-La Mancha**, integrada por **cinco provincias** (**Albacete, Ciudad Real, Cuenca, Guadalajara y Toledo**, con capital en **Toledo**), y **Extremadura**, integrada por **dos provincias** (**Cáceres y Badajoz**, las dos provincias más extensas de España, con capital autonómica en **Mérida**).",
                "grammar_examples": [
                    {"es": "Castilla-La Mancha está formada por cinco provincias: Albacete, Ciudad Real, Cuenca, Guadalajara y Toledo.", "en": "Castile-La Mancha is formed by five provinces: Albacete, Ciudad Real, Cuenca, Guadalajara, and Toledo."},
                    {"es": "Extremadura se compone de las provincias de Cáceres y Badajoz, y su capital autonómica es Mérida.", "en": "Extremadura is composed of the provinces of Cáceres and Badajoz, and its regional capital is Mérida."}
                ],
                "grammar_tip": "¡Cuidado en el CCSE! La capital de Extremadura NO es Cáceres ni Badajoz, sino **Mérida** (situada en la provincia de Badajoz). Y la capital de Castilla-La Mancha es **Toledo**.",
                "paragraphs": [
                    "Al sur de Madrid y del Sistema Central se extienden por la Submeseta Sur dos comunidades autónomas hermanadas por los ríos Tajo y Guadiana y por una historia milenaria: Castilla-La Mancha y Extremadura.",
                    "Castilla-La Mancha está integrada por cinco provincias: Albacete, Ciudad Real, Cuenca, Guadalajara y Toledo. Su capital autonómica es la histórica ciudad de Toledo, abrazada por un meandro del río Tajo y conocida universalmente como «la Ciudad de las Tres Culturas» porque durante siglos convivieron en sus calles cristianos, judíos y musulmanes (dejando joyas como su Catedral gótica, las sinagogas del Tránsito y Santa María la Blanca, la mezquita del Cristo de la Luz y los cuadros de El Greco).",
                    "Las llanuras de La Mancha son el escenario inmortal donde Miguel de Cervantes situó las aventuras de don Quijote y Sancho Panza entre molinos de viento (como los de Campo de Criptana y Consuegra), viñedos, azafrán y el célebre queso manchego. Además de Toledo, en Castilla-La Mancha son Patrimonio de la Humanidad la ciudad amurallada de Cuenca —famosa por sus Casas Colgadas sobre la hoz del río Huécar— y las minas históricas de mercurio de Almadén (Ciudad Real), junto a los parques nacionales de las Tablas de Daimiel y Cabañeros.",
                    "Al oeste de Castilla-La Mancha, junto a la frontera con Portugal, se sitúa Extremadura, formada por dos provincias que son, precisamente, las dos provincias de mayor superficie de toda España: Badajoz (al sur, regada por el Guadiana) y Cáceres (al norte, regada por el Tajo y el Parque Nacional de Monfragüe, con el Valle del Jerte famoso por sus cerezos en flor).",
                    "La capital de la comunidad autónoma de Extremadura es la ciudad de Mérida (situada en la provincia de Badajoz), antigua Augusta Emerita, que conserva el conjunto romano más completo de España —presidido por el Teatro y el Anfiteatro Romanos, sede cada verano del Festival Internacional de Teatro Clásico de Mérida—. Junto a Mérida, Extremadura cuenta con otros dos bienes Patrimonio de la Humanidad: la ciudad monumental de Cáceres y el Real Monasterio de Santa María de Guadalupe, además de sus dehesas de encinas y alcornoques donde se cría el cerdo ibérico de bellota."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las cinco provincias de Castilla-La Mancha y cuál es su capital autonómica?",
                        "options": [
                            "Albacete, Ciudad Real, Cuenca, Guadalajara y Toledo, y su capital es Toledo",
                            "Cáceres y Badajoz, y su capital es Mérida",
                            "Ávila, Segovia, Soria, Burgos y León",
                            "Jaén, Córdoba, Sevilla, Huelva y Cádiz"
                        ],
                        "correctIndex": 0,
                        "explanation": "Castilla-La Mancha tiene cinco provincias (Albacete, Ciudad Real, Cuenca, Guadalajara y Toledo) y su capital es Toledo."
                    },
                    {
                        "question": "¿Cuáles son las dos provincias que forman la comunidad autónoma de Extremadura y cuál es su capital?",
                        "options": [
                            "Las provincias son Cáceres y Badajoz, y la capital autonómica es Mérida",
                            "Las provincias son Toledo y Cuenca, y la capital es Albacete",
                            "Las provincias son Huelva y Sevilla, y la capital es Córdoba",
                            "Las provincias son Salamanca y Zamora, y la capital es León"
                        ],
                        "correctIndex": 0,
                        "explanation": "Extremadura está integrada por las provincias de Cáceres y Badajoz, y su capital es Mérida."
                    },
                    {
                        "question": "¿En qué ciudad española se encuentran las famosas «Casas Colgadas», declaradas Patrimonio de la Humanidad?",
                        "options": [
                            "En Cuenca (Castilla-La Mancha)",
                            "En Guadalajara",
                            "En Badajoz",
                            "En Ciudad Real"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Casas Colgadas son el símbolo arquitectónico de la ciudad de Cuenca."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Con qué sobrenombre histórico se conoce a la ciudad de Toledo por la convivencia medieval de cristianos, judíos y musulmanes?",
                        "options": [
                            "La Ciudad de las Tres Culturas",
                            "La Huerta de Europa",
                            "La Costa del Sol",
                            "La Perla del Cantábrico"
                        ],
                        "correctIndex": 0,
                        "explanation": "Toledo es conocida como la Ciudad de las Tres Culturas."
                    },
                    {
                        "prompt": "¿En qué ciudad extremeña se celebra cada verano el famoso Festival Internacional de Teatro Clásico en su Teatro Romano?",
                        "options": [
                            "En Mérida",
                            "En Plasencia",
                            "En Almendralejo",
                            "En Talavera"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Teatro Romano de Mérida acoge desde 1933 el Festival Internacional de Teatro Clásico."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La capital de la comunidad autónoma de Castilla-La Mancha es la histórica ciudad de ___.",
                        "answer": "Toledo",
                        "options": ["Toledo", "Albacete", "Cuenca", "Mérida"],
                        "explanation": "Toledo es la capital de Castilla-La Mancha.",
                        "english": "The capital of the autonomous community of Castile-La Mancha is the historic city of Toledo."
                    },
                    {
                        "sentence": "La comunidad autónoma de Extremadura está formada por las provincias de Cáceres y ___, y su capital es Mérida.",
                        "answer": "Badajoz",
                        "options": ["Badajoz", "Huelva", "Salamanca", "Toledo"],
                        "explanation": "Cáceres y Badajoz son las dos provincias de Extremadura.",
                        "english": "The autonomous community of Extremadura is formed by the provinces of Cáceres and Badajoz, and its capital is Mérida."
                    }
                ],
                "ex_dict": {
                    "audioText": "Toledo es la capital de Castilla-La Mancha y Mérida es la capital de Extremadura.",
                    "english": "Toledo is the capital of Castile-La Mancha and Mérida is the capital of Extremadura."
                },
                "ex_sb": {
                    "words": ["Extremadura", "está", "formada", "por", "las", "provincias", "de", "Cáceres", "y", "Badajoz."],
                    "english": "Extremadura is formed by the provinces of Cáceres and Badajoz."
                }
            },
            {
                "num": "04",
                "Title": "Andalucía: Las Ocho Provincias, Sevilla, Córdoba y Granada",
                "title": "Andalucía: Las Ocho Provincias, Sevilla, Córdoba y Granada",
                "grammar_slug": "la-comunidad-mas-poblada-con-ocho-provincias",
                "story_slug": "andalucia",
                "story_title": "De la Mezquita de Córdoba y la Alhambra de Granada a la Giralda de Sevilla",
                "objectives": [
                    "Memorizar que Andalucía es la comunidad autónoma más poblada de España y está formada por 8 provincias: Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga y Sevilla.",
                    "Identificar su capital autonómica (Sevilla, sede de la Junta de Andalucía) y sus monumentos universales: la Alhambra de Granada, la Mezquita de Córdoba y la Giralda y el Alcázar de Sevilla.",
                    "Practicar las construcciones «ser la comunidad autónoma más poblada de España» y «estar integrada por ocho provincias»."
                ],
                "vocab": [
                    {"lemma": "Andalucía", "pos": "noun", "translation": "Andalusia (most populous autonomous community in Spain, 8 provinces)"},
                    {"lemma": "Sevilla", "pos": "noun", "translation": "Seville (capital of Andalusia)"},
                    {"lemma": "Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga y Sevilla", "pos": "noun", "translation": "the eight provinces of Andalusia"},
                    {"lemma": "la Alhambra y el Generalife (Granada)", "pos": "noun", "translation": "Alhambra and Generalife palaces in Granada (UNESCO)"},
                    {"lemma": "la Mezquita-Catedral de Córdoba", "pos": "noun", "translation": "Mosque-Cathedral of Córdoba (UNESCO)"},
                    {"lemma": "la Giralda y el Real Alcázar de Sevilla", "pos": "noun", "translation": "Giralda tower and Royal Alcázar of Seville (UNESCO)"},
                    {"lemma": "el flamenco", "pos": "noun", "translation": "flamenco (Andalusian music and dance, UNESCO)"},
                    {"lemma": "la Junta de Andalucía", "pos": "noun", "translation": "Regional Government of Andalusia"}
                ],
                "grammar_title": "Demografía y geografía del sur: las ocho provincias de Andalucía",
                "grammar_text": "**Andalucía** es la **comunidad autónoma más poblada de España** (con más de 8,6 millones de habitantes) y la segunda más extensa después de Castilla y León. Está integrada por **ocho provincias**: **Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga y Sevilla**, y su capital autonómica es **Sevilla**.",
                "grammar_examples": [
                    {"es": "Andalucía es la comunidad autónoma más poblada de España y cuenta con ocho provincias.", "en": "Andalusia is the most populous autonomous community in Spain and has eight provinces."},
                    {"es": "La Alhambra se encuentra en la ciudad de Granada y la Mezquita-Catedral en la ciudad de Córdoba.", "en": "The Alhambra is located in the city of Granada and the Mosque-Cathedral in the city of Córdoba."}
                ],
                "grammar_tip": "¡Tres preguntas clásicas del CCSE sobre Andalucía! 1) Es la comunidad autónoma MÁS POBLADA de España. 2) Tiene 8 provincias. 3) Alhambra = Granada; Mezquita = Córdoba; Giralda y Torre del Oro = Sevilla.",
                "paragraphs": [
                    "Ocupando todo el sur de la península ibérica entre Sierra Morena, el océano Atlántico y el mar Mediterráneo, y separada de África únicamente por el estrecho de Gibraltar, se extiende Andalucía. Con más de 8,6 millones de habitantes, es la comunidad autónoma más poblada de España y la segunda de mayor superficie territorial.",
                    "Andalucía está formada por ocho provincias que todo aspirante a la nacionalidad debe recordar: cinco tienen costa marítima —Huelva y Cádiz en el océano Atlántico (con la Costa de la Luz), Cádiz en el estrecho, y Málaga (la Costa del Sol, ciudad natal de Pablo Picasso), Granada y Almería en el mar Mediterráneo— y tres son interiores, recorridas por el río Guadalquivir: Jaén (primera productora mundial de aceite de oliva, con las ciudades renacentistas de Úbeda y Baeza), Córdoba y Sevilla.",
                    "La capital de la comunidad autónoma y sede de la Junta de Andalucía y de su Parlamento es la ciudad de Sevilla, que en 1992 acogió la Exposición Universal (Expo 92). En el corazón de Sevilla se alzan tres monumentos declarados conjuntamente Patrimonio de la Humanidad: la Catedral con su famoso campanario almohade (la Giralda), el Real Alcázar y el Archivo de Indias, además de la Torre del Oro a orillas del Guadalquivir y la Plaza de España.",
                    "Otras dos capitales andaluzas custodian joyas universales que aparecen constantemente en el examen CCSE: en Córdoba se levanta la imponente Mezquita-Catedral (símbolo del Califato de Córdoba en el siglo X, famosa por su bosque de columnas y arcos bicolores y por su Fiesta de los Patios en mayo); y en Granada, frente a las cumbres de Sierra Nevada, se alza el conjunto palaciego nazarí de la Alhambra, el Generalife y el barrio del Albaicín.",
                    "Andalucía es cuna del arte del flamenco (declarado Patrimonio Cultural Inmaterial de la Humanidad), del gazpacho y el salmorejo, del pescaíto frito y los vinos de Jerez, y celebra fiestas de fama mundial como la Feria de Abril y la Semana Santa de Sevilla, el Carnaval de Cádiz, la Romería de El Rocío en Huelva y el Día de Andalucía cada 28 de febrero."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la comunidad autónoma con mayor población de España y cuántas provincias tiene?",
                        "options": [
                            "Andalucía, con 8 provincias (Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga y Sevilla)",
                            "Castilla y León, con 9 provincias",
                            "La Comunidad de Madrid, con 4 provincias",
                            "Galicia, con 4 provincias"
                        ],
                        "correctIndex": 0,
                        "explanation": "Andalucía es la comunidad autónoma más poblada de España y está dividida en 8 provincias."
                    },
                    {
                        "question": "¿En qué ciudades andaluzas se encuentran, respectivamente, la Alhambra, la Mezquita y la Giralda?",
                        "options": [
                            "La Alhambra en Granada, la Mezquita en Córdoba y la Giralda en Sevilla",
                            "La Alhambra en Cádiz, la Mezquita en Málaga y la Giralda en Jaén",
                            "Las tres están en la ciudad de Almería",
                            "La Alhambra en Sevilla, la Mezquita en Granada y la Giralda en Córdoba"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Alhambra está en Granada, la Mezquita-Catedral en Córdoba y la Giralda en Sevilla."
                    },
                    {
                        "question": "¿Cuál es la capital de la comunidad autónoma de Andalucía y sede de la Junta de Andalucía?",
                        "options": [
                            "Sevilla",
                            "Málaga",
                            "Granada",
                            "Córdoba"
                        ],
                        "correctIndex": 0,
                        "explanation": "Sevilla es la capital de Andalucía y sede de sus instituciones autonómicas."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué provincia andaluza se encuentran las ciudades renacentistas de Úbeda y Baeza (Patrimonio de la Humanidad) y la mayor producción mundial de aceite de oliva?",
                        "options": [
                            "En Jaén",
                            "En Huelva",
                            "En Cádiz",
                            "En Almería"
                        ],
                        "correctIndex": 0,
                        "explanation": "Jaén es la capital mundial del aceite de oliva y alberga Úbeda y Baeza."
                    },
                    {
                        "prompt": "¿En qué ciudad andaluza de la Costa del Sol nació el pintor universal Pablo Picasso y se encuentra hoy el Museo Picasso Málaga?",
                        "options": [
                            "En Málaga",
                            "En Córdoba",
                            "En Huelva",
                            "En Jaén"
                        ],
                        "correctIndex": 0,
                        "explanation": "Pablo Ruiz Picasso nació en Málaga en 1881."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El palacio nazarí de la Alhambra y los jardines del Generalife se encuentran en la ciudad de ___.",
                        "answer": "Granada",
                        "options": ["Granada", "Córdoba", "Sevilla", "Cádiz"],
                        "explanation": "La Alhambra y el Generalife son el gran tesoro monumental de Granada.",
                        "english": "The Nasrid palace of the Alhambra and the Generalife gardens are located in the city of Granada."
                    },
                    {
                        "sentence": "Andalucía es la comunidad autónoma más poblada de España y su capital es ___.",
                        "answer": "Sevilla",
                        "options": ["Sevilla", "Málaga", "Huelva", "Almería"],
                        "explanation": "Sevilla es la capital de Andalucía.",
                        "english": "Andalusia is the most populous autonomous community in Spain and its capital is Seville."
                    }
                ],
                "ex_dict": {
                    "audioText": "Andalucía tiene ocho provincias y su capital es la ciudad de Sevilla.",
                    "english": "Andalusia has eight provinces and its capital is the city of Seville."
                },
                "ex_sb": {
                    "words": ["La", "Alhambra", "está", "en", "Granada", "y", "la", "Mezquita", "está", "en", "Córdoba."],
                    "english": "The Alhambra is in Granada and the Mosque is in Córdoba."
                }
            },
            {
                "num": "05",
                "Title": "Las Islas Canarias: Dos Provincias y Capitalidad Compartida",
                "title": "Las Islas Canarias: Dos Provincias y Capitalidad Compartida",
                "grammar_slug": "capitalidad-compartida-y-cabildos-insulares",
                "story_slug": "canarias",
                "story_title": "Ocho islas en el Atlántico: Cabildos Insulares, el Teide y el Carnaval",
                "objectives": [
                    "Memorizar que la comunidad autónoma de Canarias está dividida en 2 provincias (Santa Cruz de Tenerife y Las Palmas) y tiene capitalidad compartida entre Santa Cruz de Tenerife y Las Palmas de Gran Canaria.",
                    "Recordar las islas de cada provincia: Santa Cruz de Tenerife (Tenerife, La Palma, La Gomera y El Hierro) y Las Palmas (Gran Canaria, Fuerteventura, Lanzarote y La Graciosa), así como el gobierno insular de los Cabildos Insulares.",
                    "Practicar las construcciones «compartir la capitalidad autonómica» y «estar gobernada cada isla por un Cabildo Insular»."
                ],
                "vocab": [
                    {"lemma": "las Islas Canarias", "pos": "noun", "translation": "Canary Islands"},
                    {"lemma": "Santa Cruz de Tenerife y Las Palmas", "pos": "noun", "translation": "the two provinces of the Canary Islands"},
                    {"lemma": "Tenerife, La Palma, La Gomera y El Hierro", "pos": "noun", "translation": "the western islands (province of Santa Cruz de Tenerife)"},
                    {"lemma": "Gran Canaria, Fuerteventura, Lanzarote y La Graciosa", "pos": "noun", "translation": "the eastern islands (province of Las Palmas)"},
                    {"lemma": "el Cabildo Insular", "pos": "noun", "translation": "Island Council (governing body of each Canary Island)"},
                    {"lemma": "la capitalidad compartida", "pos": "noun", "translation": "shared regional capital status"},
                    {"lemma": "el silbo gomero", "pos": "noun", "translation": "Silbo Gomero (whistled language of La Gomera, UNESCO)"},
                    {"lemma": "las papas arrugadas con mojo / el gofio", "pos": "noun", "translation": "wrinkled potatoes with mojo sauce / toasted grain flour (gofio)"}
                ],
                "grammar_title": "La singularidad institucional de Canarias: dos provincias, capitalidad compartida y Cabildos",
                "grammar_text": "La comunidad autónoma de **Canarias** es la única de España con **capitalidad compartida**: según su Estatuto de Autonomía, la capitalidad la comparten las ciudades de **Santa Cruz de Tenerife** y **Las Palmas de Gran Canaria**. El archipiélago se divide en **dos provincias** y cada isla se gobierna a través de su **Cabildo Insular**.",
                "grammar_examples": [
                    {"es": "La comunidad autónoma de Canarias tiene dos provincias: Santa Cruz de Tenerife y Las Palmas.", "en": "The autonomous community of the Canary Islands has two provinces: Santa Cruz de Tenerife and Las Palmas."},
                    {"es": "En las Islas Canarias, el órgano de gobierno y administración propio de cada isla es el Cabildo Insular.", "en": "In the Canary Islands, the governing and administrative body of each island is the Cabildo Insular."}
                ],
                "grammar_tip": "¡Pregunta fija del CCSE! En **Canarias** hay **2 provincias** (Santa Cruz de Tenerife y Las Palmas) y cada isla tiene un **Cabildo Insular**.",
                "paragraphs": [
                    "En el océano Atlántico, frente a la costa noroccidental de África y con condición de región ultraperiférica de la Unión Europea, se levanta el archipiélago de origen volcánico de las Islas Canarias. Disfruta de un clima subtropical único en España y de cuatro parques nacionales: el Teide (en Tenerife), Timanfaya (en Lanzarote), Garajonay (en La Gomera) y la Caldera de Taburiente (en La Palma).",
                    "A diferencia de las Islas Baleares (que forman una sola provincia), la comunidad autónoma de Canarias está dividida en dos provincias: la provincia occidental de Santa Cruz de Tenerife —integrada por las islas de Tenerife, La Palma, La Gomera y El Hierro— y la provincia oriental de Las Palmas —integrada por las islas de Gran Canaria, Fuerteventura, Lanzarote y la octava isla habitada, La Graciosa—.",
                    "Además, Canarias presenta una característica institucional única en España: la capitalidad de la comunidad autónoma es compartida entre las dos capitales provinciales, Santa Cruz de Tenerife y Las Palmas de Gran Canaria, donde alterna la sede de la Presidencia del Gobierno de Canarias (mientras que el Parlamento de Canarias tiene su sede en Santa Cruz de Tenerife).",
                    "Conforme al artículo 141.4 de la Constitución Española, en los archipiélagos las islas tendrán su administración propia en forma de Cabildos o Consejos. En Canarias, el órgano de gobierno, administración y representación de cada isla recibe el nombre histórico de Cabildo Insular.",
                    "La cultura canaria posee tesoros declarados Patrimonio de la Humanidad por la UNESCO como la ciudad colonial de San Cristóbal de La Laguna (en Tenerife), el Risco Caído y las Montañas Sagradas de Gran Canaria y el sorprendente «silbo gomero» (lenguaje silbado prehispánico de la isla de La Gomera). En febrero brillan sus famosísimos Carnavales de Santa Cruz de Tenerife y de Las Palmas de Gran Canaria, y en su mesa destacan el plátano de Canarias, el gofio y las papas arrugadas con mojo picón."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las dos provincias en que se divide la comunidad autónoma de las Islas Canarias?",
                        "options": [
                            "Santa Cruz de Tenerife y Las Palmas",
                            "Mallorca y Menorca",
                            "Cádiz y Huelva",
                            "Ceuta y Melilla"
                        ],
                        "correctIndex": 0,
                        "explanation": "El archipiélago canario está dividido en las dos provincias de Santa Cruz de Tenerife y Las Palmas."
                    },
                    {
                        "question": "¿Cómo se llaman los órganos de gobierno y administración propios de cada una de las islas del archipiélago canario?",
                        "options": [
                            "Cabildos Insulares",
                            "Diputaciones Forales",
                            "Sindicaturas de Cuentas",
                            "Concejos Abiertos"
                        ],
                        "correctIndex": 0,
                        "explanation": "En las Islas Canarias, la administración propia de cada isla corresponde a los Cabildos Insulares."
                    },
                    {
                        "question": "¿Qué dos ciudades comparten la capitalidad de la comunidad autónoma de Canarias?",
                        "options": [
                            "Santa Cruz de Tenerife y Las Palmas de Gran Canaria",
                            "Arrecife y Puerto del Rosario",
                            "La Laguna y Maspalomas",
                            "Palma e Ibiza"
                        ],
                        "correctIndex": 0,
                        "explanation": "Santa Cruz de Tenerife y Las Palmas de Gran Canaria comparten la capitalidad autonómica de Canarias."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿A qué provincia canaria pertenecen las islas de Gran Canaria, Fuerteventura, Lanzarote y La Graciosa?",
                        "options": [
                            "A la provincia de Las Palmas",
                            "A la provincia de Santa Cruz de Tenerife",
                            "A la provincia de Baleares",
                            "A la provincia de Cádiz"
                        ],
                        "correctIndex": 0,
                        "explanation": "Gran Canaria, Fuerteventura, Lanzarote y La Graciosa forman la provincia oriental de Las Palmas."
                    },
                    {
                        "prompt": "¿En qué isla canaria se conserva el lenguaje silbado conocido como «el silbo gomero», declarado Patrimonio Cultural Inmaterial de la Humanidad?",
                        "options": [
                            "En La Gomera",
                            "En Lanzarote",
                            "En Fuerteventura",
                            "En Mallorca"
                        ],
                        "correctIndex": 0,
                        "explanation": "El silbo gomero es el lenguaje silbado tradicional de la isla de La Gomera."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En las Islas Canarias, el órgano de gobierno propio de cada isla se denomina ___ Insular.",
                        "answer": "Cabildo",
                        "options": ["Cabildo", "Consejo", "Fuero", "Cantón"],
                        "explanation": "Los Cabildos Insulares gobiernan cada isla de Canarias.",
                        "english": "In the Canary Islands, the governing body of each island is called the Island Cabildo."
                    },
                    {
                        "sentence": "La capitalidad de Canarias es compartida entre Santa Cruz de Tenerife y Las ___ de Gran Canaria.",
                        "answer": "Palmas",
                        "options": ["Palmas", "Médulas", "Tablas", "Lagunas"],
                        "explanation": "Santa Cruz de Tenerife y Las Palmas de Gran Canaria comparten la capitalidad de Canarias.",
                        "english": "The capital status of the Canary Islands is shared between Santa Cruz de Tenerife and Las Palmas de Gran Canaria."
                    }
                ],
                "ex_dict": {
                    "audioText": "Las Islas Canarias tienen dos provincias y cada isla está gobernada por un Cabildo Insular.",
                    "english": "The Canary Islands have two provinces and each island is governed by an Island Cabildo."
                },
                "ex_sb": {
                    "words": ["Santa", "Cruz", "de", "Tenerife", "y", "Las", "Palmas", "comparten", "la", "capitalidad", "de", "Canarias."],
                    "english": "Santa Cruz de Tenerife and Las Palmas share the capital status of the Canary Islands."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 21: Ceuta, Melilla y Municipios de España (unit_num=57, b1-ciudadesautonomas)
    # =========================================================================
    {
        "slug": "ciudadesautonomas",
        "unit_num": 57,
        "title": "Ceuta, Melilla y Municipios de España",
        "description": "Las ciudades autónomas de Ceuta y Melilla, los 8.132 municipios y ayuntamientos, las 50 provincias y la demografía española (INE y Padrón).",
        "Badge": "Ceuta, Melilla y Municipios",
        "lessons": [
            {
                "num": "01",
                "Title": "La Ciudad Autónoma de Ceuta: En el Estrecho de Gibraltar",
                "title": "La Ciudad Autónoma de Ceuta: En el Estrecho de Gibraltar",
                "grammar_slug": "ciudad-autonoma-situada-en-el-norte-de-africa",
                "story_slug": "ceuta",
                "story_title": "Donde se abrazan dos mares y cuatro culturas: las Murallas Reales de Ceuta",
                "objectives": [
                    "Situar geográficamente la Ciudad Autónoma de Ceuta en el norte de África, en la orilla sur del estrecho de Gibraltar, frente a las costas de Cádiz.",
                    "Conocer su Estatuto de Autonomía de 1995, sus instituciones de autogobierno (Asamblea de Ceuta y Presidente-Alcalde) y su representación en las Cortes Generales.",
                    "Practicar las construcciones «contar con Estatuto de Autonomía desde 1995» y «estar situada en la orilla del estrecho de Gibraltar»."
                ],
                "vocab": [
                    {"lemma": "la Ciudad Autónoma de Ceuta", "pos": "noun", "translation": "Autonomous City of Ceuta"},
                    {"lemma": "el Estatuto de Autonomía de 1995", "pos": "noun", "translation": "1995 Statute of Autonomy (Organic Law 1/1995)"},
                    {"lemma": "la Asamblea de Ceuta", "pos": "noun", "translation": "Assembly of Ceuta (25 members)"},
                    {"lemma": "el Presidente-Alcalde", "pos": "noun", "translation": "President-Mayor (head of the autonomous city)"},
                    {"lemma": "las Murallas Reales de Ceuta", "pos": "noun", "translation": "Royal Walls of Ceuta (fortified moat and walls)"},
                    {"lemma": "el Monte Hacho", "pos": "noun", "translation": "Mount Hacho (promontory in Ceuta)"},
                    {"lemma": "la convivencia de cuatro culturas", "pos": "noun", "translation": "coexistence of four cultures (Christian, Muslim, Jewish, and Hindu)"},
                    {"lemma": "el puerto franco", "pos": "noun", "translation": "free port / special tax territory"}
                ],
                "grammar_title": "Estatus constitucional especial: «las dos ciudades autónomas de España»",
                "grammar_text": "Al amparo de la Disposición Transitoria Quinta de la Constitución Española, en marzo de **1995** las Cortes Generales aprobaron los Estatutos de Autonomía de **Ceuta** y **Melilla**. Ambas tienen condición de **Ciudades Autónomas** (17 comunidades autónomas + 2 ciudades autónomas): cuentan con su propia **Asamblea** de 25 miembros y un **Presidente** que es a la vez **Alcalde**, pero no tienen potestad para dictar leyes con rango formal de ley sino reglamentos.",
                "grammar_examples": [
                    {"es": "Ceuta es una de las dos ciudades autónomas de España y está situada en el norte de África, junto al estrecho de Gibraltar.", "en": "Ceuta is one of the two autonomous cities of Spain and is located in North Africa, next to the Strait of Gibraltar."},
                    {"es": "Tanto Ceuta como Melilla cuentan con su propio Estatuto de Autonomía aprobado por ley orgánica en 1995.", "en": "Both Ceuta and Melilla have their own Statute of Autonomy approved by organic law in 1995."}
                ],
                "grammar_tip": "Recuerda siempre la fórmula territorial completa para el CCSE: España está organizada en **17 comunidades autónomas y 2 ciudades autónomas (Ceuta y Melilla)**.",
                "paragraphs": [
                    "Cuando estudiamos la organización territorial de España para el examen CCSE, hay una cifra que debemos tener siempre presente: el Estado español se compone de 17 comunidades autónomas y 2 ciudades autónomas. Esas dos ciudades autónomas, situadas en el norte del continente africano, son Ceuta y Melilla.",
                    "La Ciudad Autónoma de Ceuta se asienta sobre un istmo y la península de la Almina, en la orilla norteafricana del estrecho de Gibraltar, donde se encuentran las aguas del océano Atlántico y del mar Mediterráneo, a menos de una hora en barco del puerto gaditano de Algeciras y con frontera terrestre con Marruecos.",
                    "Vinculada a la península ibérica desde 1415 e integrada en la Corona de España bajo Felipe II (y ratificada por el Tratado de Lisboa de 1668), Ceuta accedió al autogobierno mediante la Ley Orgánica 1/1995, que aprobó su Estatuto de Autonomía. Sus instituciones de autogobierno son la Asamblea de Ceuta (compuesta por 25 miembros elegidos por sufragio universal cada cuatro años), el Consejo de Gobierno y el Presidente de la Ciudad Autónoma, que ostenta simultáneamente la condición de Alcalde.",
                    "En su patrimonio monumental brillan las imponentes Murallas Reales de Ceuta y el Foso Real de San Felipe —único foso navegable de agua marina de su género en Europa—, el Parque Marítimo del Mediterráneo diseñado por el artista canario César Manrique y el mirador del Monte Hacho.",
                    "Ceuta es además un modelo de convivencia multicultural donde comparten vecindad y fiestas cuatro comunidades históricas: la cristiana, la musulmana, la hebrea (sefardí) y la hindú. En las Cortes Generales de Madrid, los ciudadanos de Ceuta están representados por un diputado en el Congreso y dos senadores en el Senado."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las dos ciudades autónomas de España situadas en el norte del continente africano?",
                        "options": [
                            "Ceuta y Melilla",
                            "Tenerife y Las Palmas",
                            "Cádiz y Algeciras",
                            "Ibiza y Formentera"
                        ],
                        "correctIndex": 0,
                        "explanation": "Ceuta y Melilla son las dos ciudades autónomas de España, situadas en el norte de África."
                    },
                    {
                        "question": "¿En qué año se aprobaron mediante ley orgánica los Estatutos de Autonomía de Ceuta y de Melilla?",
                        "options": [
                            "En 1995",
                            "En 1812",
                            "En 2018",
                            "En 1960"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Leyes Orgánicas 1/1995 y 2/1995 aprobaron los Estatutos de Autonomía de Ceuta y Melilla."
                    },
                    {
                        "question": "¿Cuántos diputados y cuántos senadores elige cada una de las ciudades autónomas (Ceuta y Melilla) en las elecciones generales a las Cortes Generales?",
                        "options": [
                            "1 diputado en el Congreso y 2 senadores en el Senado cada una",
                            "10 diputados y 10 senadores cada una",
                            "Ninguno",
                            "5 diputados y 4 senadores cada una"
                        ],
                        "correctIndex": 0,
                        "explanation": "Según los artículos 68.2 y 69.4 de la Constitución Española, Ceuta y Melilla eligen cada una 1 diputado y 2 senadores."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué estrecho marítimo baña la Ciudad Autónoma de Ceuta y la separa de la costa de la provincia de Cádiz?",
                        "options": [
                            "El estrecho de Gibraltar",
                            "El canal de Menorca",
                            "El golfo de Vizcaya",
                            "El cabo de Gata"
                        ],
                        "correctIndex": 0,
                        "explanation": "Ceuta se sitúa en la orilla sur del estrecho de Gibraltar."
                    },
                    {
                        "prompt": "¿Cómo se llama el órgano representativo de autogobierno de la Ciudad Autónoma de Ceuta, formado por 25 miembros?",
                        "options": [
                            "La Asamblea de Ceuta",
                            "El Cabildo de Ceuta",
                            "La Diputación Foral",
                            "El Consejo Insular"
                        ],
                        "correctIndex": 0,
                        "explanation": "El órgano representativo de la ciudad autónoma es la Asamblea de Ceuta."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "España está organizada territorialmente en 17 comunidades autónomas y dos ___ autónomas: Ceuta y Melilla.",
                        "answer": "ciudades",
                        "options": ["ciudades", "regiones", "islas", "comarcas"],
                        "explanation": "Ceuta y Melilla son las dos ciudades autónomas de España.",
                        "english": "Spain is territorially organized into 17 autonomous communities and two autonomous cities: Ceuta and Melilla."
                    },
                    {
                        "sentence": "La Ciudad Autónoma de ___ está situada en la orilla norteafricana del estrecho de Gibraltar.",
                        "answer": "Ceuta",
                        "options": ["Ceuta", "Palma", "Mérida", "Oviedo"],
                        "explanation": "Ceuta se sitúa junto al estrecho de Gibraltar, en el norte de África.",
                        "english": "The Autonomous City of Ceuta is located on the North African shore of the Strait of Gibraltar."
                    }
                ],
                "ex_dict": {
                    "audioText": "Ceuta y Melilla son las dos ciudades autónomas de España situadas en el norte de África.",
                    "english": "Ceuta and Melilla are the two autonomous cities of Spain located in North Africa."
                },
                "ex_sb": {
                    "words": ["Ceuta", "elige", "un", "diputado", "en", "el", "Congreso", "y", "dos", "senadores."],
                    "english": "Ceuta elects one deputy in the Congress and two senators."
                }
            },
            {
                "num": "02",
                "Title": "La Ciudad Autónoma de Melilla: Melilla la Vieja y el Modernismo",
                "title": "La Ciudad Autónoma de Melilla: Melilla la Vieja y el Modernismo",
                "grammar_slug": "la-segunda-ciudad-con-mas-edificios-modernistas",
                "story_slug": "melilla",
                "story_title": "El Peñón de Melilla la Vieja y el «Triángulo de Oro» modernista",
                "objectives": [
                    "Situar la Ciudad Autónoma de Melilla en la costa oriental norteafricana (península de Tres Forcas), bañada por el mar Mediterráneo.",
                    "Conocer su vinculación a la Corona desde 1497, la ciudadela fortificada de Melilla la Vieja y su extraordinario patrimonio de arquitectura modernista (el segundo mayor de España tras Barcelona).",
                    "Practicar las construcciones «estar bañada por el mar Mediterráneo» y «ocupar el segundo lugar en arquitectura modernista»."
                ],
                "vocab": [
                    {"lemma": "la Ciudad Autónoma de Melilla", "pos": "noun", "translation": "Autonomous City of Melilla"},
                    {"lemma": "Melilla la Vieja", "pos": "noun", "translation": "Melilla la Vieja (16th-century fortified citadel on a rocky promontory)"},
                    {"lemma": "la arquitectura modernista de Melilla", "pos": "noun", "translation": "Modernist architecture of Melilla (second largest in Spain after Barcelona)"},
                    {"lemma": "Enrique Nieto", "pos": "noun", "translation": "Enrique Nieto (architect disciple of Gaudí who designed Modernist Melilla)"},
                    {"lemma": "la Asamblea de Melilla", "pos": "noun", "translation": "Assembly of Melilla"},
                    {"lemma": "el Palacio de la Asamblea", "pos": "noun", "translation": "Assembly Palace (Art Deco seat of Melilla's government)"},
                    {"lemma": "el mar de Alborán (Mediterráneo)", "pos": "noun", "translation": "Alboran Sea (western Mediterranean)"},
                    {"lemma": "la interculturalidad", "pos": "noun", "translation": "intercultural coexistence"}
                ],
                "grammar_title": "Patrimonio e instituciones: la Ciudad Autónoma de Melilla",
                "grammar_text": "La **Ciudad Autónoma de Melilla**, situada en la costa mediterránea del norte de África (a unas millas al sur de Málaga, Granada y Almería), forma parte de España desde **1497** (durante el reinado de los Reyes Católicos) y sorprende por ser **la segunda ciudad de España con más edificios modernistas y *art déco*** después de Barcelona.",
                "grammar_examples": [
                    {"es": "Melilla es una ciudad autónoma española bañada por el mar Mediterráneo en el norte de África.", "en": "Melilla is a Spanish autonomous city washed by the Mediterranean Sea in North Africa."},
                    {"es": "Después de Barcelona, Melilla es la ciudad española que conserva mayor número de edificios modernistas.", "en": "After Barcelona, Melilla is the Spanish city that preserves the largest number of Modernist buildings."}
                ],
                "grammar_tip": "Dato muy útil para el CCSE: Ceuta y Melilla tienen exactamente la misma estructura institucional: una Asamblea de 25 miembros, un Presidente-Alcalde, 1 diputado en el Congreso y 2 senadores en el Senado.",
                "paragraphs": [
                    "A unos doscientos cincuenta kilómetros al este de Ceuta, en la base oriental de la península de Tres Forcas y bañada por las aguas del mar de Alborán (mar Mediterráneo), se alza la Ciudad Autónoma de Melilla. Conectada diariamente por barco y avión con los puertos y aeropuertos andaluces de Málaga, Almería y Motril (además de Madrid y Barcelona), Melilla cuenta con cerca de 86.000 habitantes.",
                    "Su historia dentro de la Corona española comenzó en septiembre de 1497, apenas cinco años después de la toma de Granada, cuando la expedición de Pedro de Estopiñán incorporó el enclave para los Reyes Católicos. Sobre un imponente peñón rocoso que se adentra en el Mediterráneo se levantan los cuatro recintos amurallados de «Melilla la Vieja», una monumental ciudadela fortificada de los siglos XVI al XVIII con aljibes, baluartes y las Cuevas del Conventico.",
                    "Pero quien pasea por el ensanche del centro de Melilla descubre una sorpresa arquitectónica fascinante: el «Triángulo de Oro» del modernismo melillense. Con más de quinientos edificios catalogados, Melilla es la segunda ciudad de España con mayor representación de arquitectura modernista y art déco, solo por detrás de Barcelona, gracias a la obra del arquitecto barcelonés Enrique Nieto (discípulo de Antoni Gaudí), quien diseñó también el Palacio de la Asamblea.",
                    "Al igual que Ceuta, Melilla aprobó su Estatuto de Autonomía en marzo de 1995 (Ley Orgánica 2/1995). Su gobierno y administración corresponden a la Asamblea de Melilla (integrada por 25 miembros elegidos cada cuatro años), al Consejo de Gobierno y a su Presidente, que ejerce a la vez las atribuciones de Alcalde.",
                    "En Melilla conviven estrechamente comunidades cristianas, musulmanas (de lengua materna tamazight o amazigh junto al castellano), sefardíes e hindúes, reflejando su vocación de puente cultural entre Europa y el norte de África."
                ],
                "questions": [
                    {
                        "question": "¿En qué mar se encuentra bañada la costa de la Ciudad Autónoma de Melilla?",
                        "options": [
                            "En el mar Mediterráneo (mar de Alborán)",
                            "En el mar Cantábrico",
                            "En el mar Báltico",
                            "En el océano Índico"
                        ],
                        "correctIndex": 0,
                        "explanation": "Melilla está bañada por las aguas del mar Mediterráneo en el norte de África."
                    },
                    {
                        "question": "¿Por qué destaca especialmente el patrimonio arquitectónico urbano del centro de Melilla del siglo XX?",
                        "options": [
                            "Por ser la segunda ciudad de España con mayor número de edificios modernistas y art déco, después de Barcelona",
                            "Por tener rascacielos de cien plantas",
                            "Por carecer de murallas históricas",
                            "Por estar construida íntegramente de madera"
                        ],
                        "correctIndex": 0,
                        "explanation": "Gracias al arquitecto Enrique Nieto (discípulo de Gaudí), Melilla es la segunda ciudad modernista de España tras Barcelona."
                    },
                    {
                        "question": "¿Qué cargo ostenta simultáneamente el Presidente de la Ciudad Autónoma de Melilla (al igual que el de Ceuta)?",
                        "options": [
                            "El cargo de Alcalde de la ciudad",
                            "El cargo de Defensor del Pueblo estatal",
                            "El cargo de Presidente del Senado",
                            "El cargo de Gobernador del Banco de España"
                        ],
                        "correctIndex": 0,
                        "explanation": "En Ceuta y Melilla, el Presidente de la Ciudad Autónoma es elegido por la Asamblea entre sus miembros y ostenta también la condición de Alcalde."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cómo se llama la histórica ciudadela amurallada de los siglos XVI al XVIII situada sobre un peñón frente al mar en Melilla?",
                        "options": [
                            "Melilla la Vieja",
                            "La Aljafería",
                            "Dalt Vila",
                            "La Alhambra"
                        ],
                        "correctIndex": 0,
                        "explanation": "Melilla la Vieja es el recinto fortificado histórico de la ciudad."
                    },
                    {
                        "prompt": "¿Con qué país tiene frontera terrestre la Ciudad Autónoma de Melilla (al igual que Ceuta)?",
                        "options": [
                            "Con Marruecos",
                            "Con Portugal",
                            "Con Andorra",
                            "Con Francia"
                        ],
                        "correctIndex": 0,
                        "explanation": "Tanto Ceuta como Melilla limitan por tierra con el Reino de Marruecos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La Ciudad Autónoma de ___ está situada en el norte de África y es famosa por su recinto de Melilla la Vieja y su arquitectura modernista.",
                        "answer": "Melilla",
                        "options": ["Melilla", "Segovia", "Cuenca", "Vitoria"],
                        "explanation": "Melilla destaca por Melilla la Vieja y su conjunto modernista.",
                        "english": "The Autonomous City of Melilla is located in North Africa and is famous for its citadel of Melilla la Vieja and its Modernist architecture."
                    },
                    {
                        "sentence": "Tanto Ceuta como Melilla tienen frontera terrestre con ___.",
                        "answer": "Marruecos",
                        "options": ["Marruecos", "Portugal", "Andorra", "Italia"],
                        "explanation": "Ceuta y Melilla tienen frontera terrestre con Marruecos.",
                        "english": "Both Ceuta and Melilla share a land border with Morocco."
                    }
                ],
                "ex_dict": {
                    "audioText": "Melilla es una ciudad autónoma española situada en la costa mediterránea del norte de África.",
                    "english": "Melilla is a Spanish autonomous city located on the Mediterranean coast of North Africa."
                },
                "ex_sb": {
                    "words": ["El", "Presidente", "de", "Melilla", "ejerce", "también", "las", "funciones", "de", "Alcalde."],
                    "english": "The President of Melilla also exercises the functions of Mayor."
                }
            },
            {
                "num": "03",
                "Title": "Los Más de 8.100 Municipios de España y el Ayuntamiento",
                "title": "Los Más de 8.100 Municipios de España y el Ayuntamiento",
                "grammar_slug": "corresponder-el-gobierno-y-administracion-al-ayuntamiento",
                "story_slug": "municipios",
                "story_title": "La administración más cercana: Alcalde, Concejales y los servicios de cada día",
                "objectives": [
                    "Comprender el artículo 140 CE: autonomía de los municipios y gobierno de los Ayuntamientos (integrados por el Alcalde y los Concejales).",
                    "Conocer que España cuenta con más de 8.100 municipios (8.132) y saber cómo se eligen los concejales (por los vecinos cada 4 años) y el alcalde (por los concejales o por los vecinos en Concejo Abierto).",
                    "Practicar las construcciones «estar integrado por los Alcaldes y los Concejales» y «prestar servicios públicos municipales»."
                ],
                "vocab": [
                    {"lemma": "el municipio", "pos": "noun", "translation": "municipality (basic local territorial entity)"},
                    {"lemma": "el Ayuntamiento", "pos": "noun", "translation": "City Council / Town Hall"},
                    {"lemma": "el Alcalde / la Alcaldesa", "pos": "noun", "translation": "Mayor"},
                    {"lemma": "el Concejal / la Concejala", "pos": "noun", "translation": "City Councillor"},
                    {"lemma": "el Pleno Municipal", "pos": "noun", "translation": "Municipal Plenary Session (all councillors and the mayor)"},
                    {"lemma": "el Concejo Abierto", "pos": "noun", "translation": "Open Council (direct assembly democracy in very small villages)"},
                    {"lemma": "la ordenanza municipal", "pos": "noun", "translation": "municipal ordinance / bylaw"},
                    {"lemma": "los servicios municipales obligatorios", "pos": "noun", "translation": "mandatory municipal public services"}
                ],
                "grammar_title": "El artículo 140 CE: «Su gobierno y administración corresponde a sus respectivos Ayuntamientos»",
                "grammar_text": "El **artículo 140 de la Constitución Española** regula el municipio, entidad básica del Estado: **«La Constitución garantiza la autonomía de los municipios. Estos disfrutarán de personalidad jurídica plena. Su gobierno y administración corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales»**.",
                "grammar_examples": [
                    {"es": "El gobierno y la administración de los municipios corresponden a los Ayuntamientos, integrados por el Alcalde y los Concejales.", "en": "The government and administration of municipalities correspond to the City Councils, made up of the Mayor and the Councillors."},
                    {"es": "Los Concejales son elegidos por los vecinos del municipio mediante sufragio universal cada cuatro años.", "en": "Councillors are elected by the residents of the municipality by universal suffrage every four years."}
                ],
                "grammar_tip": "Pregunta frecuente del CCSE: ¿Quién integra el Ayuntamiento? El **Alcalde** y los **Concejales**. Los vecinos eligen a los concejales en las elecciones municipales, y los concejales eligen al Alcalde.",
                "paragraphs": [
                    "Según el artículo 137 de la Constitución Española, el Estado se organiza territorialmente en municipios, en provincias y en las Comunidades Autónomas que se constituyan. El primer escalón —el más próximo al domicilio de cada ciudadano— es el municipio. En España existen actualmente 8.132 municipios, desde grandes metrópolis como Madrid y Barcelona hasta pequeños pueblos de montaña de menos de cien habitantes.",
                    "El artículo 140 de la Constitución garantiza la autonomía de los municipios y establece que su gobierno y administración corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales. ¿Cómo se eligen? Cada cuatro años (el cuarto domingo de mayo), los vecinos mayores de 18 años —incluidos los ciudadanos de la Unión Europea y de países con acuerdo de reciprocidad residentes en el municipio— acuden a las urnas en las elecciones municipales para elegir a los Concejales.",
                    "Una vez constituido el Pleno del Ayuntamiento, son los propios Concejales quienes votan y eligen entre ellos al Alcalde o Alcaldesa. Existe una hermosa excepción histórica regulada por la propia Constitución: en los municipios muy pequeños (generalmente de menos de 100 habitantes) funciona el régimen de «Concejo Abierto», donde el gobierno corresponde a un Alcalde elegido directamente por los vecinos y a una Asamblea Vecinal de la que forman parte todos los electores del pueblo.",
                    "¿De qué se ocupa el Ayuntamiento en nuestra vida diaria? La Ley Reguladora de las Bases del Régimen Local establece que todos los municipios españoles, sin importar su tamaño, deben prestar servicios esenciales como el alumbrado público, la recogida de residuos, la limpieza viaria, el abastecimiento domiciliario de agua potable, el alcantarillado y la pavimentación de las vías públicas.",
                    "Además, conforme aumenta su población (a partir de 5.000, 20.000 o 50.000 habitantes), los ayuntamientos tienen obligación de ofrecer parque público, biblioteca pública, instalaciones deportivas, servicios sociales, protección civil, transporte colectivo urbano de viajeros y protección del medio ambiente urbano."
                ],
                "questions": [
                    {
                        "question": "Según el artículo 140 de la Constitución Española, ¿qué órgano gobierna y administra cada municipio y quiénes lo integran?",
                        "options": [
                            "El Ayuntamiento, integrado por el Alcalde y los Concejales",
                            "El Senado, integrado por los senadores provinciales",
                            "El Consejo de Estado, integrado por exministros",
                            "La Audiencia Provincial, integrada por magistrados"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 140 CE establece que el gobierno y administración de los municipios corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales."
                    },
                    {
                        "question": "¿Cómo se elige de forma general al Alcalde o Alcaldesa de un municipio en España?",
                        "options": [
                            "Los vecinos eligen a los Concejales en las elecciones municipales y los Concejales eligen al Alcalde (salvo en Concejo Abierto)",
                            "Lo nombra directamente el Ministro de Hacienda por sorteo",
                            "El cargo se hereda de padres a hijos",
                            "Lo designa el Tribunal Constitucional cada diez años"
                        ],
                        "correctIndex": 0,
                        "explanation": "Conforme al artículo 140 CE, los concejales son elegidos por los vecinos y los alcaldes son elegidos por los concejales o por los vecinos (en Concejo Abierto)."
                    },
                    {
                        "question": "¿Cuál de los siguientes servicios públicos es competencia propia de los Ayuntamientos en los municipios españoles?",
                        "options": [
                            "El alumbrado público, la recogida de basuras, el abastecimiento de agua potable y la limpieza de calles",
                            "La defensa militar de las fronteras y el mando de la Armada",
                            "La expedición de títulos de piloto de aviación comercial",
                            "La firma de tratados internacionales con otros Estados"
                        ],
                        "correctIndex": 0,
                        "explanation": "El alumbrado público, el agua potable, la limpieza viaria y la recogida de residuos son servicios municipales obligatorios."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cada cuántos años se celebran en España las elecciones municipales para renovar los Ayuntamientos?",
                        "options": [
                            "Cada 4 años",
                            "Cada 8 años",
                            "Cada 2 años",
                            "Cada 10 años"
                        ],
                        "correctIndex": 0,
                        "explanation": "El mandato de los alcaldes y concejales dura cuatro años."
                    },
                    {
                        "prompt": "¿Cómo se llama el régimen especial de democracia directa que funciona en los pueblos muy pequeños de España, donde todos los vecinos forman la Asamblea Vecinal?",
                        "options": [
                            "Concejo Abierto",
                            "Estado de Sitio",
                            "Cuestión de Confianza",
                            "Recurso de Amparo"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 140 de la Constitución prevé el régimen de Concejo Abierto para los pequeños municipios."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El gobierno y la administración de los municipios corresponden a los ___, integrados por los Alcaldes y los Concejales.",
                        "answer": "Ayuntamientos",
                        "options": ["Ayuntamientos", "Ministerios", "Consulados", "Juzgados"],
                        "explanation": "Los Ayuntamientos son los órganos de gobierno municipal (Art. 140 CE).",
                        "english": "The government and administration of municipalities correspond to the City Councils, made up of Mayors and Councillors."
                    },
                    {
                        "sentence": "Los ___ son elegidos por los vecinos del municipio mediante sufragio universal, libre, igual, directo y secreto.",
                        "answer": "Concejales",
                        "options": ["Concejales", "Jueces", "Embajadores", "Notarios"],
                        "explanation": "En las elecciones municipales los vecinos eligen a los Concejales.",
                        "english": "Councillors are elected by the residents of the municipality through universal, free, equal, direct, and secret suffrage."
                    }
                ],
                "ex_dict": {
                    "audioText": "El gobierno y la administración de los municipios corresponden a los Ayuntamientos, integrados por el Alcalde y los Concejales.",
                    "english": "The government and administration of municipalities correspond to the City Councils, made up of the Mayor and the Councillors."
                },
                "ex_sb": {
                    "words": ["Los", "vecinos", "eligen", "a", "los", "concejales", "en", "las", "elecciones", "municipales."],
                    "english": "Residents elect the councillors in the municipal elections."
                }
            },
            {
                "num": "04",
                "Title": "Las Cincuenta Provincias y las Diputaciones Provinciales",
                "title": "Las Cincuenta Provincias y las Diputaciones Provinciales",
                "grammar_slug": "agrupacion-de-municipios-en-cincuenta-provincias",
                "story_slug": "provincias",
                "story_title": "De Javier de Burgos en 1833 a las cincuenta provincias actuales y las Diputaciones",
                "objectives": [
                    "Recordar que España está dividida en 50 provincias y comprender el artículo 141 CE (la provincia como agrupación de municipios).",
                    "Identificar las Diputaciones Provinciales como órganos de gobierno y administración de las provincias (y recordar que en las 7 comunidades uniprovinciales no existe Diputación separada).",
                    "Practicar las construcciones «estar determinada por la agrupación de municipios» y «requerir ley orgánica aprobada por las Cortes Generales»."
                ],
                "vocab": [
                    {"lemma": "la provincia", "pos": "noun", "translation": "province (50 provinces in Spain)"},
                    {"lemma": "la agrupación de municipios", "pos": "noun", "translation": "grouping of municipalities"},
                    {"lemma": "la Diputación Provincial", "pos": "noun", "translation": "Provincial Council (governing body of a province)"},
                    {"lemma": "la Diputación Foral", "pos": "noun", "translation": "Foral Council (in the 3 Basque provinces)"},
                    {"lemma": "la circunscripción electoral", "pos": "noun", "translation": "electoral constituency / district"},
                    {"lemma": "el Subdelegado del Gobierno", "pos": "noun", "translation": "Government Sub-delegate (in each province)"},
                    {"lemma": "los códigos postales (del 01 al 52)", "pos": "noun", "translation": "Spanish postal codes (first two digits identify the province)"},
                    {"lemma": "la cooperación con los pequeños municipios", "pos": "noun", "translation": "cooperation with small municipalities"}
                ],
                "grammar_title": "El artículo 141 CE: la provincia y la Diputación Provincial",
                "grammar_text": "El **artículo 141 de la Constitución Española** define la provincia como una entidad local con personalidad jurídica propia, **«determinada por la agrupación de municipios»**, y establece que **cualquier alteración de los límites provinciales habrá de ser aprobada por las Cortes Generales mediante ley orgánica**. Su gobierno y administración corresponden a las **Diputaciones** u otras Corporaciones de carácter representativo.",
                "grammar_examples": [
                    {"es": "España se divide en cincuenta provincias y el gobierno de cada provincia pluriprovincial corresponde a la Diputación Provincial.", "en": "Spain is divided into fifty provinces and the government of each multi-province province corresponds to the Provincial Council."},
                    {"es": "Cualquier alteración de los límites provinciales debe ser aprobada por las Cortes Generales mediante ley orgánica.", "en": "Any alteration of provincial boundaries must be approved by the Cortes Generales by organic law."}
                ],
                "grammar_tip": "Dato curioso y muy útil para el CCSE: en España hay **50 provincias** (más las 2 ciudades autónomas de Ceuta y Melilla, por eso los códigos postales españoles van del `01` de Álava al `50` de Zaragoza, más `51` para Ceuta y `52` para Melilla).",
                "paragraphs": [
                    "Entre el municipio y la Comunidad Autónoma se sitúa el segundo nivel territorial de España: la provincia. El mapa provincial español actual —integrado por 50 provincias— tiene una notable estabilidad histórica, pues procede en su práctica totalidad de la división territorial diseñada en 1833 por Javier de Burgos (con la única adición posterior de la división de Canarias en dos provincias en 1927).",
                    "El artículo 141 de la Constitución Española define la provincia como una entidad local con personalidad jurídica propia, determinada por la agrupación de municipios, y también como división territorial para el cumplimiento de las actividades del Estado (por ejemplo, la provincia es la circunscripción electoral para elegir a los diputados y senadores en las elecciones generales). Si algún día se quisieran modificar los límites de una provincia, sería necesaria una ley orgánica aprobada por las Cortes Generales.",
                    "¿Quién gobierna y administra cada provincia? En las comunidades autónomas formadas por varias provincias, esa tarea corresponde a la Diputación Provincial (compuesta por diputados provinciales elegidos entre los concejales de los ayuntamientos de esa provincia), cuya misión principal es asegurar la prestación integral de los servicios municipales en los pueblos pequeños de menos de 20.000 habitantes.",
                    "Ahora bien, existen tres regímenes provinciales especiales que siempre conviene recordar para el examen CCSE: en primer lugar, en las siete comunidades autónomas uniprovinciales (Asturias, Cantabria, La Rioja, Navarra, Madrid, Murcia e Islas Baleares) las competencias de la Diputación Provincial quedan integradas en el propio Gobierno de la Comunidad Autónoma, para no duplicar administraciones.",
                    "En segundo lugar, en los tres territorios históricos del País Vasco (Álava, Bizkaia y Gipuzkoa) existen las Diputaciones Forales y las Juntas Generales, con amplias competencias fiscales propias. Y en tercer lugar, en los archipiélagos el gobierno insular recae en los Cabildos Insulares (en Canarias) y en los Consejos Insulares (en las Islas Baleares). Además, cada código postal español de cinco cifras comienza siempre con los dos dígitos de su provincia (del 01 al 50, más el 51 de Ceuta y el 52 de Melilla)."
                ],
                "questions": [
                    {
                        "question": "¿Cuántas provincias existen en total en España?",
                        "options": [
                            "50 provincias (además de las 2 ciudades autónomas de Ceuta y Melilla)",
                            "17 provincias",
                            "36 provincias",
                            "65 provincias"
                        ],
                        "correctIndex": 0,
                        "explanation": "España está dividida en 50 provincias repartidas entre las 17 comunidades autónomas."
                    },
                    {
                        "question": "¿Qué institución se encarga del gobierno y la administración autónoma de una provincia en las comunidades pluriprovinciales?",
                        "options": [
                            "La Diputación Provincial",
                            "El Tribunal de Cuentas",
                            "El Consejo General del Poder Judicial",
                            "El Ministerio de Asuntos Exteriores"
                        ],
                        "correctIndex": 0,
                        "explanation": "Según el artículo 141.2 CE, el gobierno y la administración de las provincias están encomendados a las Diputaciones Provinciales."
                    },
                    {
                        "question": "Según el artículo 141.1 de la Constitución Española, ¿qué se necesita para poder modificar los límites de una provincia en España?",
                        "options": [
                            "Una ley orgánica aprobada por las Cortes Generales",
                            "Un simple bando del alcalde de un pueblo",
                            "Un acuerdo privado entre dos empresas",
                            "Una orden verbal de un concejal"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 141.1 CE dispone que cualquier alteración de los límites provinciales habrá de ser aprobada por las Cortes Generales mediante ley orgánica."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué indican las dos primeras cifras de los códigos postales de cinco dígitos en España (del 01 al 52)?",
                        "options": [
                            "La provincia (del 01 al 50) o la ciudad autónoma (51 Ceuta, 52 Melilla) a la que pertenece la localidad",
                            "La altitud sobre el nivel del mar",
                            "La temperatura media anual",
                            "El número de hospitales del municipio"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los dos primeros dígitos del código postal español corresponden a cada una de las 50 provincias más Ceuta (51) y Melilla (52)."
                    },
                    {
                        "prompt": "¿Qué ocurre con la Diputación Provincial en las siete comunidades autónomas uniprovinciales como Madrid, Asturias, Cantabria, La Rioja, Navarra o Murcia?",
                        "options": [
                            "No existe Diputación Provincial separada; sus funciones las asume directamente la Comunidad Autónoma",
                            "Tienen diez Diputaciones Provinciales cada una",
                            "Las gobierna el Ayuntamiento de otra comunidad",
                            "Dependían del Banco de España"
                        ],
                        "correctIndex": 0,
                        "explanation": "En las comunidades autónomas uniprovinciales, las competencias de la Diputación Provincial se integran en los órganos de la propia Comunidad Autónoma."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El territorio de España está dividido en ___ provincias.",
                        "answer": "cincuenta",
                        "options": ["cincuenta", "diecisiete", "veinte", "ochenta"],
                        "explanation": "En España existen 50 provincias.",
                        "english": "The territory of Spain is divided into fifty provinces."
                    },
                    {
                        "sentence": "El gobierno y la administración de las provincias están encomendados a las ___ Provinciales.",
                        "answer": "Diputaciones",
                        "options": ["Diputaciones", "Embajadas", "Universidades", "Aduanas"],
                        "explanation": "Las Diputaciones Provinciales gobiernan y administran las provincias (Art. 141.2 CE).",
                        "english": "The government and administration of the provinces are entrusted to the Provincial Councils (Diputaciones)."
                    }
                ],
                "ex_dict": {
                    "audioText": "España se divide en cincuenta provincias y su gobierno corresponde a las Diputaciones Provinciales.",
                    "english": "Spain is divided into fifty provinces and their government corresponds to the Provincial Councils."
                },
                "ex_sb": {
                    "words": ["La", "provincia", "es", "una", "entidad", "local", "determinada", "por", "la", "agrupación", "de", "municipios."],
                    "english": "The province is a local entity determined by the grouping of municipalities."
                }
            },
            {
                "num": "05",
                "Title": "Demografía, Padrón Municipal e Instituto Nacional de Estadística",
                "title": "Demografía, Padrón Municipal e Instituto Nacional de Estadística",
                "grammar_slug": "superar-los-cuarenta-y-ocho-millones-de-habitantes",
                "story_slug": "demografia",
                "story_title": "Más de 48 millones de habitantes: cómo cuenta y dónde vive la sociedad española",
                "objectives": [
                    "Recordar la población aproximada de España (más de 48 millones de habitantes) y su elevada esperanza de vida (más de 83 años, una de las más altas del mundo).",
                    "Identificar el Instituto Nacional de Estadística (INE) como organismo encargado de los censos demográficos y económicos y de coordinar el Padrón Municipal.",
                    "Practicar las construcciones «superar los cuarenta y ocho millones de habitantes» y «concentrarse en las costas, islas y Madrid»."
                ],
                "vocab": [
                    {"lemma": "el Instituto Nacional de Estadística (INE)", "pos": "noun", "translation": "National Statistics Institute"},
                    {"lemma": "el Censo de Población y Viviendas", "pos": "noun", "translation": "Population and Housing Census"},
                    {"lemma": "el Padrón Municipal de Habitantes", "pos": "noun", "translation": "Municipal Register of Inhabitants"},
                    {"lemma": "la esperanza de vida", "pos": "noun", "translation": "life expectancy (over 83 years in Spain)"},
                    {"lemma": "la densidad de población", "pos": "noun", "translation": "population density"},
                    {"lemma": "el envejecimiento demográfico", "pos": "noun", "translation": "demographic aging"},
                    {"lemma": "el reto demográfico (la España vaciada)", "pos": "noun", "translation": "demographic challenge (rural depopulation in inland Spain)"},
                    {"lemma": "el saldo migratorio", "pos": "noun", "translation": "net migration balance"}
                ],
                "grammar_title": "Datos demográficos y estadísticos: «superar los 48 millones» y el papel del INE",
                "grammar_text": "Para describir la población de España en el examen CCSE se emplean verbos cuantitativos como **«superar»**, **«alcanzar»** y **«concentrarse en»**: *La población de España **supera los 48 millones de habitantes** según los datos oficiales del **Instituto Nacional de Estadística (INE)***.",
                "grammar_examples": [
                    {"es": "Según el Instituto Nacional de Estadística (INE), España supera los cuarenta y ocho millones de habitantes.", "en": "According to the National Statistics Institute (INE), Spain exceeds forty-eight million inhabitants."},
                    {"es": "España es uno de los países con mayor esperanza de vida del mundo, superando los ochenta y tres años de media.", "en": "Spain is one of the countries with the highest life expectancy in the world, exceeding an average of eighty-three years."}
                ],
                "grammar_tip": "Recuerda para el CCSE: la población de España ronda los **48-49 millones de habitantes**, el organismo que elabora las estadísticas y censos oficiales es el **INE (Instituto Nacional de Estadística)**, y las 4 comunidades más pobladas son **Andalucía, Cataluña, Comunidad de Madrid y Comunidad Valenciana**.",
                "paragraphs": [
                    "¿Cuántas personas viven hoy en España y cómo sabemos exactamente cuántos somos? El organismo autónomo del Estado encargado de elaborar los censos de población, coordinar los padrones municipales, calcular el Índice de Precios de Consumo (IPC) o la Encuesta de Población Activa (EPA) y proporcionar los datos oficiales del censo electoral es el Instituto Nacional de Estadística, conocido por sus siglas INE.",
                    "Según los datos oficiales del INE, la población de España supera actualmente los 48 millones de habitantes (cerca de 49 millones en los registros más recientes), tras haber crecido en casi nueve millones de personas desde el comienzo del siglo XXI gracias fundamentalmente a la llegada e integración de nuevos residentes procedentes de Iberoamérica, la Unión Europea, el norte de África y otras regiones del mundo.",
                    "¿Cómo se reparte esa población sobre el mapa español? La distribución es muy desigual: la población se concentra de forma muy intensa en el área metropolitana de Madrid, en el litoral del mar Mediterráneo y del Atlántico sur, en los valles del Ebro y del Guadalquivir y en los dos archipiélagos (Baleares y Canarias). De hecho, cuatro comunidades autónomas —Andalucía, Cataluña, la Comunidad de Madrid y la Comunidad Valenciana— reúnen por sí solas cerca del 60 % de todos los habitantes de España.",
                    "Por el contrario, extensas provincias del interior de la Meseta y del Sistema Ibérico —como Soria, Teruel, Cuenca, Zamora o Ávila— presentan densidades de población muy bajas (inferiores en algunos casos a los 10 o 12 habitantes por kilómetro cuadrado), fenómeno conocido como el «reto demográfico» o «la España vaciada».",
                    "Por último, una de las señas de identidad más admiradas de la sociedad española —gracias a la calidad de su Sistema Nacional de Salud, su dieta mediterránea y su estilo de vida social y familiar— es su extraordinaria longevidad: con una esperanza de vida al nacer superior a los 83 años (y más de 86 años en el caso de las mujeres), España es uno de los tres países más longevos del planeta."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la población aproximada actual de España según los datos oficiales?",
                        "options": [
                            "Alrededor de 48-49 millones de habitantes",
                            "Alrededor de 15 millones de habitantes",
                            "Más de 120 millones de habitantes",
                            "Menos de 8 millones de habitantes"
                        ],
                        "correctIndex": 0,
                        "explanation": "España cuenta actualmente con una población que supera los 48 millones de habitantes."
                    },
                    {
                        "question": "¿Qué organismo público elabora en España el Censo de Población, el Índice de Precios de Consumo (IPC) y las estadísticas demográficas oficiales?",
                        "options": [
                            "El Instituto Nacional de Estadística (INE)",
                            "El Instituto de Cinematografía (ICAA)",
                            "El Instituto Cervantes",
                            "El Consejo Superior de Investigaciones Científicas (CSIC)"
                        ],
                        "correctIndex": 0,
                        "explanation": "El INE (Instituto Nacional de Estadística) es el organismo estatal encargado de las estadísticas y censos oficiales."
                    },
                    {
                        "question": "¿Cuáles son las cuatro comunidades autónomas más pobladas de España?",
                        "options": [
                            "Andalucía, Cataluña, la Comunidad de Madrid y la Comunidad Valenciana",
                            "La Rioja, Cantabria, Navarra y Asturias",
                            "Extremadura, Aragón, Baleares y Murcia",
                            "Galicia, País Vasco, Canarias y Castilla y León"
                        ],
                        "correctIndex": 0,
                        "explanation": "Por orden de población, las cuatro comunidades más pobladas son Andalucía (~8,6 M), Cataluña (~8 M), Madrid (~7 M) y la Comunidad Valenciana (~5,3 M)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cómo es la esperanza de vida de la población española en comparación con el resto del mundo?",
                        "options": [
                            "Es una de las más altas del mundo, superando los 83 años de media",
                            "Es la más baja de Europa occidental (55 años)",
                            "Es exactamente de 60 años",
                            "No se mide desde 1978"
                        ],
                        "correctIndex": 0,
                        "explanation": "Con más de 83 años de media, España tiene una de las esperanzas de vida más altas de la Unión Europea y del mundo."
                    },
                    {
                        "prompt": "¿En qué zonas de España se registra la menor densidad de población, fenómeno conocido como el «reto demográfico»?",
                        "options": [
                            "En provincias del interior peninsular como Soria, Teruel, Cuenca o Zamora",
                            "En el centro de Madrid y Barcelona",
                            "En la costa de Málaga y Alicante",
                            "En las islas de Tenerife y Mallorca"
                        ],
                        "correctIndex": 0,
                        "explanation": "El interior peninsular (especialmente provincias como Soria, Teruel o Cuenca) presenta la menor densidad demográfica de España."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El Instituto Nacional de ___ (INE) es el organismo público que elabora los censos de población en España.",
                        "answer": "Estadística",
                        "options": ["Estadística", "Seguridad", "Tráfico", "Arquitectura"],
                        "explanation": "INE son las siglas del Instituto Nacional de Estadística.",
                        "english": "The National Statistics Institute (INE) is the public body that prepares population censuses in Spain."
                    },
                    {
                        "sentence": "La población total de España supera los cuarenta y ___ millones de habitantes.",
                        "answer": "ocho",
                        "options": ["ocho", "dos", "veinte", "noventa"],
                        "explanation": "La población española supera los 48 millones de habitantes.",
                        "english": "The total population of Spain exceeds forty-eight million inhabitants."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Instituto Nacional de Estadística elabora los censos oficiales de población en España.",
                    "english": "The National Statistics Institute prepares the official population censuses in Spain."
                },
                "ex_sb": {
                    "words": ["España", "es", "uno", "de", "los", "países", "con", "mayor", "esperanza", "de", "vida", "del", "mundo."],
                    "english": "Spain is one of the countries with the highest life expectancy in the world."
                }
            }
        ]
    }
]


def main():
    for u in UNITS_19_20_21:
        emit_unit_from_dict(u)


if __name__ == "__main__":
    main()
