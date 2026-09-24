#!/usr/bin/env python3
"""Generate Spain Citizenship (CCSE) Units 22, 23, and 24 for es-es B1 track."""

from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict

UNITS_22_23_24 = [
    # =========================================================================
    # UNIT 22: Historia: De Hispania al Siglo de Oro (unit_num=58, b1-historiaantigua)
    # =========================================================================
    {
        "slug": "historiaantigua",
        "unit_num": 58,
        "title": "Historia: De Hispania al Siglo de Oro",
        "description": "Prehistoria e Hispania romana, Edad Media (Al-Ándalus y reinos cristianos), 1492 y los Reyes Católicos, los Austrias (Carlos I y Felipe II) y los Borbones del siglo XVIII.",
        "Badge": "Historia Antigua y Moderna",
        "lessons": [
            {
                "num": "01",
                "Title": "De Altamira y los Íberos a la Hispania Romana",
                "title": "De Altamira y los Íberos a la Hispania Romana",
                "grammar_slug": "remontarse-a-dar-origen-al-latin",
                "story_slug": "prehistoriayroma",
                "story_title": "De la Dama de Elche a las calzadas, el latín y los emperadores de Hispania",
                "objectives": [
                    "Identificar las raíces prehistóricas (Atapuerca, Altamira) y prerromanas (íberos, celtas y la escultura de la Dama de Elche).",
                    "Comprender el legado de la romanización de Hispania: el latín (origen del castellano, catalán y gallego), el Derecho romano, emperadores nacidos en Hispania (Trajano, Adriano y Teodosio), el filósofo Séneca y obras como el Acueducto de Segovia y el Teatro de Mérida.",
                    "Practicar las construcciones históricas «remontarse a», «dejar como legado» y «tener su origen en el latín»."
                ],
                "vocab": [
                    {"lemma": "la Dama de Elche", "pos": "noun", "translation": "Lady of Elche (masterpiece of Iberian sculpture, 5th–4th century BC)"},
                    {"lemma": "los pueblos íberos y celtas", "pos": "noun", "translation": "Iberian and Celtic peoples"},
                    {"lemma": "la romanización de Hispania", "pos": "noun", "translation": "Romanization of Hispania"},
                    {"lemma": "el latín", "pos": "noun", "translation": "Latin (origin of Spanish, Catalan, and Galician)"},
                    {"lemma": "el Derecho romano", "pos": "noun", "translation": "Roman Law"},
                    {"lemma": "Trajano y Adriano", "pos": "noun", "translation": "Trajan and Hadrian (Roman emperors born in Italica, near Seville)"},
                    {"lemma": "Lucio Anneo Séneca", "pos": "noun", "translation": "Seneca (Stoic philosopher born in Corduba / Córdoba)"},
                    {"lemma": "la calzada romana", "pos": "noun", "translation": "Roman road (such as the Vía de la Plata)"}
                ],
                "grammar_title": "Narración histórica: «remontarse a» y «tener su origen en»",
                "grammar_text": "Para situar el origen de una lengua, una institución o un monumento en el pasado lejano, el español histórico emplea los verbos **«remontarse a»** y **«tener su origen en»**: *Las lenguas romances de España —el castellano, el catalán y el gallego— **tienen su origen en** el latín hablado en la Hispania romana*.",
                "grammar_examples": [
                    {"es": "La escultura íbera de la Dama de Elche se remonta al siglo IV antes de Cristo y se conserva en Madrid.", "en": "The Iberian sculpture of the Lady of Elche dates back to the 4th century BC and is preserved in Madrid."},
                    {"es": "El castellano, el catalán y el gallego tienen su origen en el latín traído por Roma a Hispania.", "en": "Spanish, Catalan, and Galician have their origin in the Latin brought by Rome to Hispania."}
                ],
                "grammar_tip": "Recuerda para el CCSE: la **Dama de Elche** pertenece al arte **íbero** (se exhibe en el Museo Arqueológico Nacional de Madrid), y el castellano, el catalán y el gallego proceden del **latín** (mientras que el euskera es prerromano).",
                "paragraphs": [
                    "La historia humana en la península ibérica se remonta a más de un millón de años en los yacimientos de la Sierra de Atapuerca (Burgos) y alcanza su primera cumbre artística hace 14.000 años en los bisontes policromados de la Cueva de Altamira (Cantabria). En el primer milenio antes de Cristo, mientras fenicios, griegos y cartagineses fundaban puertos comerciales como Gadir (Cádiz, considerada la ciudad más antigua de Occidente), la península estaba habitada por los pueblos celtas (en el norte y el oeste) y los pueblos íberos (en el sur y el este mediterráneo).",
                    "La obra maestra más famosa del arte íbero —y una pregunta clásica del examen CCSE— es la Dama de Elche, un enigmático busto de piedra tallado entre los siglos V y IV a. C., descubierto en 1897 en Elche (Alicante) y conservado hoy en el Museo Arqueológico Nacional de Madrid, junto a la Dama de Baza.",
                    "A partir del año 218 a. C., en el marco de las Guerras Púnicas contra Cartago, comenzó la conquista y romanización de la península, a la que los romanos llamaron Hispania. Durante más de seis siglos, Hispania se integró profundamente en el Imperio romano, adoptando sus ciudades, sus calzadas, el Derecho romano y, sobre todo, su lengua: el latín vulgar, del que nacieron todas las lenguas oficiales de España actuales (el castellano, el catalán/valenciano y el gallego), con la única excepción del euskera.",
                    "Hispania no fue una provincia periférica, sino una cuna de dirigentes y pensadores de Roma: en Itálica (cerca de Sevilla) nacieron los grandes emperadores Trajano y Adriano (a los que se sumó más tarde Teodosio), y en Córdoba nació el gran filósofo estoico Lucio Anneo Séneca.",
                    "El paisaje español sigue salpicado hoy de monumentos romanos colosales declarados Patrimonio de la Humanidad: el Acueducto de Segovia, el Teatro y Anfiteatro de Mérida, la Muralla de Lugo, la Torre de Hércules en A Coruña, el conjunto arqueológico de Tarraco (Tarragona) y el Puente de Alcántara (Cáceres)."
                ],
                "questions": [
                    {
                        "question": "¿A qué cultura prerromana pertenece la famosa escultura de piedra conocida como «la Dama de Elche»?",
                        "options": [
                            "Al arte íbero (cultura íbera)",
                            "Al arte gótico medieval",
                            "Al renacimiento italiano",
                            "A la cultura vikinga"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Dama de Elche (siglos V-IV a. C.) es la escultura más representativa del arte íbero."
                    },
                    {
                        "question": "¿De qué lengua antigua proceden el castellano, el catalán y el gallego como herencia de la romanización de Hispania?",
                        "options": [
                            "Del latín",
                            "Del griego clásico",
                            "Del germánico oriental",
                            "Del sánscrito"
                        ],
                        "correctIndex": 0,
                        "explanation": "El castellano, el catalán/valenciano y el gallego son lenguas romances que proceden del latín hablado en Hispania."
                    },
                    {
                        "question": "¿Qué dos célebres emperadores romanos del siglo II d. C. nacieron en la ciudad hispana de Itálica (en la actual provincia de Sevilla)?",
                        "options": [
                            "Trajano y Adriano",
                            "Rómulo y Remo",
                            "Alejandro Magno y Pericles",
                            "Carlomagno y Otón"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los emperadores Trajano y Adriano nacieron en Itálica (Santiponce, Sevilla)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué museo de Madrid se conserva y exhibe actualmente la escultura íbera de la Dama de Elche?",
                        "options": [
                            "En el Museo Arqueológico Nacional (MAN)",
                            "En el Museo Reina Sofía",
                            "En el Museo Naval",
                            "En el Museo del Ferrocarril"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Dama de Elche se exhibe en el Museo Arqueológico Nacional de Madrid."
                    },
                    {
                        "prompt": "¿Cuál de los siguientes monumentos españoles fue construido durante la época de la Hispania romana?",
                        "options": [
                            "El Acueducto de Segovia y el Teatro Romano de Mérida",
                            "La Sagrada Familia de Barcelona",
                            "El Museo Guggenheim de Bilbao",
                            "El Monasterio de El Escorial"
                        ],
                        "correctIndex": 0,
                        "explanation": "Tanto el Acueducto de Segovia como el Teatro de Mérida son grandes obras de la Hispania romana."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La famosa escultura prerromana conocida como la Dama de ___ pertenece al arte íbero.",
                        "answer": "Elche",
                        "options": ["Elche", "Mérida", "Lugo", "Segovia"],
                        "explanation": "La Dama de Elche fue hallada en Elche (Alicante) en 1897.",
                        "english": "The famous pre-Roman sculpture known as the Lady of Elche belongs to Iberian art."
                    },
                    {
                        "sentence": "El castellano, el catalán y el gallego son lenguas romances que tienen su origen en el ___.",
                        "answer": "latín",
                        "options": ["latín", "euskera", "celta", "fenicio"],
                        "explanation": "Las lenguas romances de España derivan del latín traído por Roma.",
                        "english": "Spanish, Catalan, and Galician are Romance languages that have their origin in Latin."
                    }
                ],
                "ex_dict": {
                    "audioText": "La Dama de Elche pertenece al arte íbero y el castellano tiene su origen en el latín.",
                    "english": "The Lady of Elche belongs to Iberian art and Spanish has its origin in Latin."
                },
                "ex_sb": {
                    "words": ["El", "Acueducto", "de", "Segovia", "es", "una", "gran", "obra", "de", "la", "Hispania", "romana."],
                    "english": "The Aqueduct of Segovia is a great work of Roman Hispania."
                }
            },
            {
                "num": "02",
                "Title": "Visigodos, Al-Ándalus y los Reinos Cristianos Medievales",
                "title": "Visigodos, Al-Ándalus y los Reinos Cristianos Medievales",
                "grammar_slug": "convivir-durante-ocho-siglos-en-la-peninsula",
                "story_slug": "edadmedia",
                "story_title": "Del Reino Visigodo de Toledo al Califato de Córdoba y las Cortes de León de 1188",
                "objectives": [
                    "Conocer el Reino Visigodo con capital en Toledo y el periodo de Al-Ándalus (711–1492), desde el Califato de Córdoba en el siglo X hasta el Reino Nazarí de Granada.",
                    "Identificar la formación de los reinos cristianos (Asturias, León, Castilla, Navarra, Corona de Aragón), las Cortes de León de 1188 (primer parlamento europeo según la UNESCO) y la Escuela de Traductores de Toledo bajo Alfonso X el Sabio.",
                    "Practicar las expresiones históricas «establecer su capital en» y «alcanzar su máximo esplendor bajo el Califato de Córdoba»."
                ],
                "vocab": [
                    {"lemma": "el Reino Visigodo de Toledo", "pos": "noun", "translation": "Visigothic Kingdom of Toledo (5th–8th centuries)"},
                    {"lemma": "Al-Ándalus", "pos": "noun", "translation": "Al-Andalus (Muslim-ruled territory of the Iberian Peninsula, 711–1492)"},
                    {"lemma": "el Califato de Córdoba", "pos": "noun", "translation": "Caliphate of Córdoba (10th century cultural and political peak)"},
                    {"lemma": "el Reino Nazarí de Granada", "pos": "noun", "translation": "Nasrid Kingdom of Granada (last kingdom of Al-Andalus, until 1492)"},
                    {"lemma": "los Reinos Cristianos (Castilla, León, Navarra, Corona de Aragón)", "pos": "noun", "translation": "the Medieval Christian Kingdoms"},
                    {"lemma": "las Cortes de León de 1188", "pos": "noun", "translation": "1188 Cortes of León (cradle of European parliamentarism, UNESCO)"},
                    {"lemma": "la Escuela de Traductores de Toledo", "pos": "noun", "translation": "Toledo School of Translators (promoted by King Alfonso X the Wise)"},
                    {"lemma": "Alfonso X el Sabio", "pos": "noun", "translation": "Alfonso X the Wise (13th-century King of Castile and León)"}
                ],
                "grammar_title": "Cronología medieval: del año 711 a las Cortes de 1188",
                "grammar_text": "Para narrar los ocho siglos de la Edad Media peninsular se utilizan marcadores cronológicos como **«tras la caída del Imperio romano»**, **«a partir del año 711»** y **«bajo el reinado de»**: *En el siglo X, Al-Ándalus **alcanzó su máximo esplendor** con el **Califato de Córdoba***.",
                "grammar_examples": [
                    {"es": "Tras la caída del Imperio romano, los visigodos establecieron la capital de su reino en Toledo.", "en": "After the fall of the Roman Empire, the Visigoths established the capital of their kingdom in Toledo."},
                    {"es": "A partir del año 711 se desarrolló en la península la civilización de Al-Ándalus, cuya cumbre fue el Califato de Córdoba.", "en": "Starting in the year 711, the civilization of Al-Andalus developed on the peninsula, whose peak was the Caliphate of Córdoba."}
                ],
                "grammar_tip": "Recuerda para el CCSE: los **visigodos** fijaron su capital en **Toledo**; en el año **711** comenzó la etapa de **Al-Ándalus** (que dejó la Mezquita de Córdoba y la Alhambra de Granada); y **Alfonso X el Sabio** impulsó la **Escuela de Traductores de Toledo**.",
                "paragraphs": [
                    "Tras la caída del Imperio romano de Occidente en el siglo V, el pueblo germánico de los visigodos unificó políticamente la península ibérica, estableció la capital de su reino en la ciudad de Toledo y promulgó un código de leyes común para hispanorromanos y visigodos: el *Liber Iudiciorum* (Fuero Juzgo), mientras brillaban intelectuales como San Isidoro de Sevilla.",
                    "En el año 711, tropas musulmanas procedentes del norte de África cruzaron el estrecho de Gibraltar y derrotaron al último rey visigodo, don Rodrigo. Comenzaba así la historia de Al-Ándalus, que durante casi ocho siglos (hasta 1492) transformó la agricultura (introduciendo el regadío, la naranja, el arroz y el azafrán), las ciencias, la medicina, la filosofía (con figuras universales como el cordobés Averroes y el filósofo judío Maimónides) y la arquitectura hispánica.",
                    "El momento de mayor esplendor político y cultural de Al-Ándalus fue el Califato de Córdoba en el siglo X (proclamado por Abderramán III en 929), cuando Córdoba era la ciudad más poblada y culta de Europa occidental y se amplió su prodigiosa Mezquita. Tras la fragmentación en los reinos de taifas y las etapas almorávide y almohade (que levantaron la Giralda de Sevilla), el último territorio andalusí fue el Reino Nazarí de Granada (siglos XIII al XV), constructor del palacio de la Alhambra.",
                    "Simultáneamente, en las montañas del norte nacieron y se expandieron hacia el sur los reinos cristianos: el Reino de Asturias (que pasó a ser Reino de León), el Reino de Castilla, el Reino de Navarra y la Corona de Aragón (integrada por el Reino de Aragón, los Condados Catalanes, y más tarde los reinos de Valencia y Mallorca). En el año 1188, el rey Alfonso IX convocó las Cortes de León con participación por primera vez de representantes de las ciudades, consideradas por la UNESCO la cuna del parlamentarismo europeo.",
                    "Lejos de ser únicamente una frontera militar, la Edad Media hispánica dio frutos culturales admirables, como el Camino de Santiago (que conectó España con toda Europa) y la Escuela de Traductores de Toledo, impulsada en el siglo XIII por el rey Alfonso X el Sabio, donde sabios cristianos, judíos y musulmanes tradujeron al castellano y al latín el saber científico y filosófico árabe y griego."
                ],
                "questions": [
                    {
                        "question": "¿Qué pueblo estableció la capital de su reino en la ciudad de Toledo tras la caída del Imperio romano y antes del año 711?",
                        "options": [
                            "Los visigodos",
                            "Los fenicios",
                            "Los normandos",
                            "Los incas"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Reino Visigodo de Toledo gobernó la península entre los siglos VI y principios del VIII (hasta el año 711)."
                    },
                    {
                        "question": "¿En qué año comenzó la presencia musulmana en la península ibérica (Al-Ándalus) y cuál fue su etapa de máximo esplendor en el siglo X?",
                        "options": [
                            "Comenzó en el año 711 y alcanzó su máximo esplendor con el Califato de Córdoba",
                            "Comenzó en 1812 y tuvo su capital en Santander",
                            "Comenzó en 1978 y su capital fue Valladolid",
                            "Comenzó en 1561 en El Escorial"
                        ],
                        "correctIndex": 0,
                        "explanation": "Al-Ándalus se inició en el año 711 y vivió su apogeo en el siglo X con el Califato de Córdoba."
                    },
                    {
                        "question": "¿Qué rey castellano del siglo XIII impulsó el uso escrito del castellano y la célebre Escuela de Traductores de Toledo?",
                        "options": [
                            "Alfonso X el Sabio",
                            "Carlos III",
                            "Felipe V",
                            "Fernando VII"
                        ],
                        "correctIndex": 0,
                        "explanation": "Alfonso X el Sabio (1221–1284) impulsó la Escuela de Traductores de Toledo y las «Siete Partidas»."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál fue el último reino musulmán de Al-Ándalus en la península ibérica, que perduró hasta enero de 1492 y construyó la Alhambra?",
                        "options": [
                            "El Reino Nazarí de Granada",
                            "El Reino de Asturias",
                            "El Condado de Barcelona",
                            "El Señorío de Vizcaya"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Reino Nazarí de Granada fue el último reino de Al-Ándalus hasta su entrega a los Reyes Católicos en 1492."
                    },
                    {
                        "prompt": "¿En qué ciudad española se celebraron en el año 1188 las primeras Cortes con representantes de las ciudades, reconocidas por la UNESCO como el testimonio documental más antiguo del sistema parlamentario europeo?",
                        "options": [
                            "En León (Cortes de León de 1188)",
                            "En Cádiz",
                            "En Málaga",
                            "En Alicante"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los «Decreta» de las Cortes de León de 1188 están inscritos en el Registro de la Memoria del Mundo de la UNESCO."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En el siglo X, Al-Ándalus alcanzó su máximo esplendor político y cultural durante el Califato de ___.",
                        "answer": "Córdoba",
                        "options": ["Córdoba", "Oviedo", "Burgos", "Lugo"],
                        "explanation": "El Califato de Córdoba (siglo X) fue la cumbre política y cultural de Al-Ándalus.",
                        "english": "In the 10th century, Al-Andalus reached its political and cultural peak during the Caliphate of Córdoba."
                    },
                    {
                        "sentence": "El rey Alfonso X el ___ impulsó en el siglo XIII la Escuela de Traductores de Toledo.",
                        "answer": "Sabio",
                        "options": ["Sabio", "Católico", "Hechizado", "Prudente"],
                        "explanation": "Alfonso X el Sabio convirtió Toledo en un faro cultural europeo.",
                        "english": "King Alfonso X the Wise promoted the Toledo School of Translators in the 13th century."
                    }
                ],
                "ex_dict": {
                    "audioText": "Los visigodos establecieron su capital en Toledo y en el siglo diez brilló el Califato de Córdoba.",
                    "english": "The Visigoths established their capital in Toledo and in the tenth century the Caliphate of Córdoba shone."
                },
                "ex_sb": {
                    "words": ["Alfonso", "X", "el", "Sabio", "impulsó", "la", "Escuela", "de", "Traductores", "de", "Toledo."],
                    "english": "Alfonso X the Wise promoted the Toledo School of Translators."
                }
            },
            {
                "num": "03",
                "Title": "El Año 1492: Los Reyes Católicos y el Encuentro con América",
                "title": "El Año 1492: Los Reyes Católicos y el Encuentro con América",
                "grammar_slug": "unir-las-coronas-bajo-el-reinado-de",
                "story_slug": "reyescatolicos",
                "story_title": "1492: Isabel y Fernando, la Gramática de Nebrija y las tres carabelas de Colón",
                "objectives": [
                    "Identificar a los Reyes Católicos (Isabel I de Castilla y Fernando II de Aragón) y la unión dinástica de las dos grandes Coronas.",
                    "Recordar los tres grandes acontecimientos de 1492: la toma de Granada, la primera Gramática de la lengua castellana de Antonio de Nebrija y la llegada de Cristóbal Colón a América el 12 de octubre de 1492.",
                    "Practicar las construcciones «culminar con la toma de Granada» y «llegar al continente americano el doce de octubre»."
                ],
                "vocab": [
                    {"lemma": "los Reyes Católicos (Isabel I de Castilla y Fernando II de Aragón)", "pos": "noun", "translation": "the Catholic Monarchs"},
                    {"lemma": "la unión dinástica", "pos": "noun", "translation": "dynastic union (of Castile and Aragon)"},
                    {"lemma": "la toma de Granada (2 de enero de 1492)", "pos": "noun", "translation": "capture/surrender of Granada"},
                    {"lemma": "Cristóbal Colón", "pos": "noun", "translation": "Christopher Columbus"},
                    {"lemma": "el Descubrimiento / Encuentro con América (12 de octubre de 1492)", "pos": "noun", "translation": "Arrival in America (October 12, 1492)"},
                    {"lemma": "las tres carabelas (la Pinta, la Niña y la Santa María)", "pos": "noun", "translation": "the three ships of Columbus's first voyage"},
                    {"lemma": "Antonio de Nebrija", "pos": "noun", "translation": "Antonio de Nebrija (author of the first Grammar of the Spanish language, 1492)"},
                    {"lemma": "los judíos sefardíes", "pos": "noun", "translation": "Sephardic Jews (descendants of Spanish Jews expelled in 1492)"}
                ],
                "grammar_title": "El año clave de la historia moderna: los hechos de 1492",
                "grammar_text": "En la Tarea 4 del examen CCSE, el año **1492** bajo el reinado de los **Reyes Católicos (Isabel de Castilla y Fernando de Aragón)** reúne tres acontecimientos decisivos: el final del Reino Nazarí de **Granada**, la llegada de la expedición de **Cristóbal Colón a América el 12 de octubre de 1492** y la publicación de la primera ***Gramática de la lengua castellana*** de **Antonio de Nebrija**.",
                "grammar_examples": [
                    {"es": "El matrimonio de Isabel I de Castilla y Fernando II de Aragón unió dinásticamente las dos grandes Coronas.", "en": "The marriage of Isabella I of Castile and Ferdinand II of Aragon dynastically united the two great Crowns."},
                    {"es": "El 12 de octubre de 1492, la expedición de Cristóbal Colón llegó a América tras partir de Palos de la Frontera.", "en": "On October 12, 1492, Christopher Columbus's expedition arrived in America after departing from Palos de la Frontera."}
                ],
                "grammar_tip": "¡Pregunta fija del CCSE! ¿Quiénes eran los Reyes Católicos? **Isabel I de Castilla y Fernando II de Aragón**. ¿Qué ocurrió el **12 de octubre de 1492**? La llegada de Cristóbal Colón a América (fecha que da origen a la Fiesta Nacional de España).",
                "paragraphs": [
                    "En octubre de 1469 se celebró en Valladolid un matrimonio que cambiaría para siempre la historia de España y del mundo: el enlace entre la princesa Isabel de Castilla y el príncipe Fernando de Aragón, conocidos en la historia como los Reyes Católicos. Su reinado conjunto significó la unión dinástica de las dos grandes coronas peninsulares —la Corona de Castilla y la Corona de Aragón—, a las que se sumaría en 1512 la incorporación del Reino de Navarra, sentando las bases de la Monarquía Hispánica moderna.",
                    "El año más decisivo de su reinado fue 1492, fecha en la que coincidieron varios acontecimientos de alcance universal. El 2 de enero de 1492, el último sultán nazarí, Boabdil, entregó las llaves de la Alhambra de Granada a los Reyes Católicos, poniendo fin a casi ocho siglos de presencia política musulmana en la península. Ese mismo año, la Corona decretó también la expulsión de los judíos españoles que no se convirtieran al cristianismo, dando origen a la diáspora de los judíos sefardíes (a cuyos descendientes la legislación española actual reconoce una vinculación especial con España).",
                    "En agosto de 1492 salió de la imprenta en Salamanca una obra pionera en toda Europa: la *Gramática de la lengua castellana*, escrita por el humanista andaluz Antonio de Nebrija. Fue la primera gramática impresa de una lengua vulgar moderna (romance) en la historia europea.",
                    "Mientras tanto, el 3 de agosto de 1492 habían zarpado del puerto onubense de Palos de la Frontera (Huelva) tres naves —las carabelas *la Pinta* y *la Niña* y la nao *Santa María*— al mando del navegante Cristóbal Colón y de los hermanos Pinzón, financiadas por la Corona de Castilla con el propósito de abrir una ruta marítima hacia las Indias navegando hacia el oeste por el océano Atlántico.",
                    "El 12 de octubre de 1492, la expedición avistó tierra en la isla de Guanahaní (en el mar Caribe). Aquel encuentro entre dos mundos dio inicio a más de tres siglos de historia compartida y mestizaje cultural y lingüístico con América, motivo por el cual el 12 de octubre se celebra hoy la Fiesta Nacional de España."
                ],
                "questions": [
                    {
                        "question": "¿Quiénes fueron los monarcas conocidos en la historia de España como «los Reyes Católicos»?",
                        "options": [
                            "Isabel I de Castilla y Fernando II de Aragón",
                            "Carlos I y Felipe II",
                            "Alfonso X el Sabio y Jaime I",
                            "Carlos III y Carlos IV"
                        ],
                        "correctIndex": 0,
                        "explanation": "Isabel I de Castilla y Fernando II de Aragón son los Reyes Católicos."
                    },
                    {
                        "question": "¿Qué dos grandes acontecimientos históricos tuvieron lugar en el año 1492 durante el reinado de los Reyes Católicos?",
                        "options": [
                            "La toma de Granada y la llegada de Cristóbal Colón a América (el 12 de octubre de 1492)",
                            "La Constitución de Cádiz y la Guerra de la Independencia",
                            "El ingreso de España en la Unión Europea y los Juegos Olímpicos",
                            "La proclamación de la Segunda República y la Guerra Civil"
                        ],
                        "correctIndex": 0,
                        "explanation": "En 1492 se produjeron la toma de Granada, la llegada de Colón a América y la publicación de la Gramática de Nebrija."
                    },
                    {
                        "question": "¿Quién escribió y publicó en 1492 la primera «Gramática de la lengua castellana», primera gramática de una lengua moderna en Europa?",
                        "options": [
                            "Antonio de Nebrija",
                            "Miguel de Unamuno",
                            "Gustavo Adolfo Bécquer",
                            "Benito Pérez Galdós"
                        ],
                        "correctIndex": 0,
                        "explanation": "El humanista Antonio de Nebrija publicó en 1492 la primera Gramática de la lengua castellana."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿De qué puerto de la provincia de Huelva partió el 3 de agosto de 1492 la expedición de Cristóbal Colón con la Pinta, la Niña y la Santa María?",
                        "options": [
                            "De Palos de la Frontera (Huelva)",
                            "De Santander",
                            "De Tarragona",
                            "De Gijón"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las tres naves de Colón partieron del puerto de Palos de la Frontera (Huelva)."
                    },
                    {
                        "prompt": "¿En qué fecha exacta llegó la expedición de Cristóbal Colón a América, fecha que hoy conmemora la Fiesta Nacional de España?",
                        "options": [
                            "El 12 de octubre de 1492",
                            "El 6 de diciembre de 1492",
                            "El 2 de mayo de 1492",
                            "El 23 de abril de 1492"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 12 de octubre de 1492 llegó Cristóbal Colón a América."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Los Reyes Católicos fueron la reina ___ I de Castilla y el rey Fernando II de Aragón.",
                        "answer": "Isabel",
                        "options": ["Isabel", "Juana", "Sofía", "Leonor"],
                        "explanation": "Isabel I de Castilla y Fernando II de Aragón fueron los Reyes Católicos.",
                        "english": "The Catholic Monarchs were Queen Isabella I of Castile and King Ferdinand II of Aragon."
                    },
                    {
                        "sentence": "El 12 de octubre de 1492, la expedición de Cristóbal ___ llegó al continente americano.",
                        "answer": "Colón",
                        "options": ["Colón", "Elcano", "Nebrija", "Goya"],
                        "explanation": "Cristóbal Colón llegó a América el 12 de octubre de 1492.",
                        "english": "On October 12, 1492, the expedition of Christopher Columbus arrived on the American continent."
                    }
                ],
                "ex_dict": {
                    "audioText": "En mil cuatrocientos noventa y dos los Reyes Católicos tomaron Granada y Cristóbal Colón llegó a América.",
                    "english": "In fourteen ninety-two the Catholic Monarchs captured Granada and Christopher Columbus arrived in America."
                },
                "ex_sb": {
                    "words": ["Isabel", "de", "Castilla", "y", "Fernando", "de", "Aragón", "fueron", "los", "Reyes", "Católicos."],
                    "english": "Isabella of Castile and Ferdinand of Aragon were the Catholic Monarchs."
                }
            },
            {
                "num": "04",
                "Title": "Los Austrias (Carlos I y Felipe II) y la Primera Vuelta al Mundo",
                "title": "Los Austrias (Carlos I y Felipe II) y la Primera Vuelta al Mundo",
                "grammar_slug": "fijar-la-capital-en-madrid-y-dar-la-vuelta-al-mundo",
                "story_slug": "austrias",
                "story_title": "El imperio donde no se ponía el sol: Magallanes, Elcano y la corte de Madrid",
                "objectives": [
                    "Identificar la dinastía de la Casa de Austria (Habsburgo) en los siglos XVI y XVII, encabezada por Carlos I de España (y V de Alemania) y su hijo Felipe II.",
                    "Recordar dos hitos fundamentales: la primera vuelta al mundo de Fernando de Magallanes y Juan Sebastián Elcano (1519–1522) y el establecimiento de la capital en Madrid por Felipe II en 1561.",
                    "Practicar las construcciones «completar la primera vuelta al mundo» y «trasladar la Corte a la villa de Madrid»."
                ],
                "vocab": [
                    {"lemma": "la Casa de Austria (los Habsburgo)", "pos": "noun", "translation": "House of Austria / Habsburgs (16th and 17th centuries)"},
                    {"lemma": "Carlos I de España y V de Alemania", "pos": "noun", "translation": "Charles I of Spain and V of the Holy Roman Empire"},
                    {"lemma": "Felipe II", "pos": "noun", "translation": "Philip II (established Madrid as capital in 1561)"},
                    {"lemma": "Fernando de Magallanes y Juan Sebastián Elcano", "pos": "noun", "translation": "Ferdinand Magellan and Juan Sebastián Elcano"},
                    {"lemma": "la primera vuelta al mundo (1519–1522)", "pos": "noun", "translation": "first circumnavigation of the globe"},
                    {"lemma": "el Siglo de Oro español", "pos": "noun", "translation": "Spanish Golden Age (literary and artistic peak)"},
                    {"lemma": "la Escuela de Salamanca (Francisco de Vitoria)", "pos": "noun", "translation": "School of Salamanca (founders of modern international law)"},
                    {"lemma": "la Paz de Westfalia (1648)", "pos": "noun", "translation": "Peace of Westphalia"}
                ],
                "grammar_title": "Los siglos XVI y XVII: la Casa de Austria, Elcano y la capitalidad de Madrid",
                "grammar_text": "Durante los siglos XVI y XVII reinó en España la **Casa de Austria (dinastía de los Habsburgo)**. Bajo **Carlos I** se completó la **primera vuelta al mundo (1519–1522)** iniciada por **Fernando de Magallanes** y culminada por el marino vasco **Juan Sebastián Elcano** a bordo de la nao *Victoria*; y bajo **Felipe II** se fijó en **1561** la Corte y capital en **Madrid**.",
                "grammar_examples": [
                    {"es": "Entre 1519 y 1522, la expedición de Magallanes y Juan Sebastián Elcano completó la primera vuelta al mundo.", "en": "Between 1519 and 1522, the expedition of Magellan and Juan Sebastián Elcano completed the first circumnavigation of the globe."},
                    {"es": "En el año 1561, el rey Felipe II trasladó la Corte a la villa de Madrid y ordenó construir El Escorial.", "en": "In the year 1561, King Philip II moved the Court to the town of Madrid and ordered the construction of El Escorial."}
                ],
                "grammar_tip": "Dos preguntas muy frecuentes en el CCSE: 1) ¿Quiénes protagonizaron la primera vuelta al mundo? **Magallanes y Juan Sebastián Elcano**. 2) ¿Qué rey fijó la capital en Madrid en 1561? **Felipe II**.",
                "paragraphs": [
                    "En el siglo XVI llegó al trono español una nueva dinastía europea, la Casa de Austria (o de los Habsburgo), en la persona de Carlos I de España (nieto de los Reyes Católicos), que en 1519 fue elegido también emperador del Sacro Imperio Romano Germánico como Carlos V. Bajo su reinado y el de su hijo Felipe II, la Monarquía Hispánica abarcó territorios en Europa, América, Asia (las Islas Filipinas) y África, hasta el punto de acuñarse la célebre frase: «En mis dominios no se pone el sol».",
                    "Durante el reinado de Carlos I tuvo lugar una de las mayores hazañas navales y científicas de todos los tiempos: la primera vuelta al mundo (1519–1522). Una expedición española de cinco naves partió de Sevilla y Sanlúcar de Barrameda al mando del portugués Fernando de Magallanes; tras cruzar el estrecho que lleva su nombre, atravesar el océano Pacífico y morir Magallanes en Filipinas, el marino vasco Juan Sebastián Elcano (natural de Getaria, Gipuzkoa) tomó el mando de la única nave superviviente —la nao *Victoria*— y regresó a España en septiembre de 1522, demostrando empíricamente que la Tierra es esférica y que todos los océanos están conectados.",
                    "Al mismo tiempo, en las aulas de la Universidad de Salamanca, pensadores como fray Francisco de Vitoria y fray Bartolomé de las Casas debatían sobre la dignidad y los derechos de los pueblos indígenas de América, fundando con la Escuela de Salamanca las bases del Derecho Internacional moderno y de los derechos humanos.",
                    "En 1556 abdicó Carlos I (retirándose al Monasterio de Yuste, en Cáceres) y le sucedió su hijo Felipe II (1556–1598), quien en 1580 logró también la unión dinástica con el Reino de Portugal y su imperio durante sesenta años. A Felipe II se deben dos decisiones que siguen marcando la España actual: en el año 1561 estableció de forma permanente la Corte y capital de la Monarquía en el centro geográfico de la península, la villa de Madrid, y mandó levantar en la sierra madrileña el colosal Monasterio de San Lorenzo de El Escorial.",
                    "Los siglos XVI y XVII (bajo los llamados «Austrias mayores», Carlos I y Felipe II, y los «Austrias menores», Felipe III, Felipe IV y Carlos II) coincidieron con el mayor esplendor cultural de nuestra historia: el Siglo de Oro de las letras y las artes, con genios como Cervantes, Lope de Vega, Calderón de la Barca, Quevedo, Góngora, El Greco, Zurbarán, Murillo y Diego Velázquez."
                ],
                "questions": [
                    {
                        "question": "¿Qué dos navegantes protagonizaron entre 1519 y 1522 la expedición española que logró dar por primera vez la vuelta completa al mundo?",
                        "options": [
                            "Fernando de Magallanes y Juan Sebastián Elcano",
                            "Marco Polo y Vasco da Gama",
                            "James Cook y Roald Amundsen",
                            "Américo Vespucio y Francis Drake"
                        ],
                        "correctIndex": 0,
                        "explanation": "Fernando de Magallanes inició la expedición en 1519 y el español Juan Sebastián Elcano la culminó en 1522 al mando de la nao Victoria."
                    },
                    {
                        "question": "¿Qué rey de la Casa de Austria trasladó la Corte a la villa de Madrid en el año 1561, convirtiéndola en la capital de España, y mandó construir el Monasterio de El Escorial?",
                        "options": [
                            "Felipe II",
                            "Fernando VII",
                            "Amadeo de Saboya",
                            "Alfonso XII"
                        ],
                        "correctIndex": 0,
                        "explanation": "Felipe II fijó la capital en Madrid en 1561 y ordenó edificar el Real Monasterio de San Lorenzo de El Escorial."
                    },
                    {
                        "question": "¿Con qué nombre se conoce el periodo de extraordinario florecimiento artístico y literario de España durante los siglos XVI y XVII (con autores como Cervantes, Lope de Vega y Velázquez)?",
                        "options": [
                            "El Siglo de Oro",
                            "La Belle Époque",
                            "La Revolución Industrial",
                            "La Movida"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Siglo de Oro abarca el esplendor cultural español del Renacimiento y el Barroco (siglos XVI y XVII)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cómo se llamaba la dinastía que reinó en España durante los siglos XVI y XVII, a la que pertenecieron Carlos I y Felipe II?",
                        "options": [
                            "La Casa de Austria (dinastía de los Habsburgo)",
                            "La Casa de Tudor",
                            "La Casa de Saboya",
                            "La dinastía Merovingia"
                        ],
                        "correctIndex": 0,
                        "explanation": "Carlos I, Felipe II, Felipe III, Felipe IV y Carlos II pertenecieron a la Casa de Austria (Habsburgo)."
                    },
                    {
                        "prompt": "¿En qué monasterio extremeño de la provincia de Cáceres se retiró el emperador Carlos I (Carlos V) tras abdicar en 1556?",
                        "options": [
                            "En el Monasterio de Yuste",
                            "En el Monasterio de Poblet",
                            "En el Monasterio de Roncesvalles",
                            "En el Monasterio de Santo Toribio"
                        ],
                        "correctIndex": 0,
                        "explanation": "Carlos V pasó sus últimos años en el Monasterio de Yuste (Cáceres)."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El marino vasco Juan Sebastián ___ completó en 1522 la primera vuelta al mundo a bordo de la nao Victoria.",
                        "answer": "Elcano",
                        "options": ["Elcano", "Colón", "Vitoria", "Pizarro"],
                        "explanation": "Juan Sebastián Elcano culminó la primera circunnavegación del globo en 1522.",
                        "english": "The Basque sailor Juan Sebastián Elcano completed the first circumnavigation of the world in 1522 aboard the ship Victoria."
                    },
                    {
                        "sentence": "En el año 1561, el rey ___ II estableció la Corte y capital en la villa de Madrid.",
                        "answer": "Felipe",
                        "options": ["Felipe", "Carlos", "Alfonso", "Sancho"],
                        "explanation": "Felipe II fijó la capitalidad en Madrid en 1561.",
                        "english": "In the year 1561, King Philip II established the Court and capital in the town of Madrid."
                    }
                ],
                "ex_dict": {
                    "audioText": "Juan Sebastián Elcano completó la primera vuelta al mundo y Felipe Segundo fijó la capital en Madrid.",
                    "english": "Juan Sebastián Elcano completed the first circumnavigation of the world and Philip the Second set the capital in Madrid."
                },
                "ex_sb": {
                    "words": ["Magallanes", "y", "Juan", "Sebastián", "Elcano", "protagonizaron", "la", "primera", "vuelta", "al", "mundo."],
                    "english": "Magallanes and Juan Sebastián Elcano carried out the first circumnavigation of the world."
                }
            },
            {
                "num": "05",
                "Title": "El Siglo XVIII: La Llegada de los Borbones y la Ilustración",
                "title": "El Siglo XVIII: La Llegada de los Borbones y la Ilustración",
                "grammar_slug": "instaurar-la-dinastia-de-los-borbones-e-impulsar-la-ilustracion",
                "story_slug": "borbones",
                "story_title": "De Felipe V y las Reales Academias al Madrid ilustrado de Carlos III",
                "objectives": [
                    "Comprender el cambio dinástico de 1700: la Guerra de Sucesión Española y la llegada de la Casa de Borbón (la dinastía reinante hoy en España) con Felipe V.",
                    "Conocer las reformas del siglo XVIII (la Ilustración): la creación de las Reales Academias (RAE en 1713 y Real Academia de la Historia) y el reinado modernizador de Carlos III («el mejor alcalde de Madrid»).",
                    "Practicar las construcciones «llegar al trono español en el siglo XVIII» e «impulsar las reformas de la Ilustración»."
                ],
                "vocab": [
                    {"lemma": "la Casa de Borbón", "pos": "noun", "translation": "House of Bourbon (ruling royal dynasty of Spain since 1700)"},
                    {"lemma": "la Guerra de Sucesión Española (1701–1714)", "pos": "noun", "translation": "War of the Spanish Succession"},
                    {"lemma": "el Tratado de Utrecht (1713)", "pos": "noun", "translation": "Treaty of Utrecht"},
                    {"lemma": "Felipe V", "pos": "noun", "translation": "Philip V (first Bourbon king of Spain, reigned 1700–1746)"},
                    {"lemma": "la Ilustración (el Siglo de las Luces)", "pos": "noun", "translation": "the Enlightenment (18th century)"},
                    {"lemma": "Carlos III", "pos": "noun", "translation": "Charles III (enlightened 18th-century monarch, 'the best mayor of Madrid')"},
                    {"lemma": "las Reales Academias (RAE, 1713)", "pos": "noun", "translation": "Royal Academies (such as the Royal Spanish Academy)"},
                    {"lemma": "Gaspar Melchor de Jovellanos", "pos": "noun", "translation": "Jovellanos (leading thinker and reformer of the Spanish Enlightenment)"}
                ],
                "grammar_title": "El siglo XVIII español: la Casa de Borbón y las reformas ilustradas",
                "grammar_text": "En el año **1700**, al morir sin descendencia el último rey de la Casa de Austria (Carlos II), llegó al trono español la **Casa de Borbón** —la misma dinastía a la que pertenece el rey actual **Felipe VI**— con el rey **Felipe V**. Durante el **siglo XVIII (el Siglo de las Luces o de la Ilustración)** destacó especialmente el rey **Carlos III**.",
                "grammar_examples": [
                    {"es": "En 1700 llegó al trono de España la dinastía de la Casa de Borbón con el rey Felipe V.", "en": "In 1700 the dynasty of the House of Bourbon came to the throne of Spain with King Philip V."},
                    {"es": "El rey Carlos III impulsó las reformas de la Ilustración y embelleció Madrid con el Paseo del Prado y la Puerta de Alcalá.", "en": "King Charles III promoted the reforms of the Enlightenment and beautified Madrid with the Paseo del Prado and the Puerta de Alcalá."}
                ],
                "grammar_tip": "Pregunta clave para el CCSE: ¿A qué dinastía o casa real pertenecen los reyes de España desde 1700 (incluido el rey actual Felipe VI)? A la **Casa de Borbón**.",
                "paragraphs": [
                    "En noviembre del año 1700 murió en Madrid sin dejar hijos Carlos II, el último monarca español de la Casa de Austria. En su testamento designó como sucesor a Felipe de Anjou, nieto del rey Luis XIV de Francia, quien subió al trono como Felipe V. Aquella decisión desencadenó un gran conflicto europeo e interior: la Guerra de Sucesión Española (1701–1714), que concluyó con los Tratados de Utrecht (1713) y Rastatt, por los cuales las potencias europeas reconocieron a Felipe V como rey de España a cambio de la cesión de las posesiones europeas de Flandes e Italia, así como de Gibraltar y temporalmente Menorca al Reino Unido.",
                    "Con Felipe V (1700–1746) se instauró en España la Casa de Borbón, la dinastía reinante hoy en nuestro país en la persona de Su Majestad el Rey Felipe VI. Los Borbones del siglo XVIII reformaron y centralizaron la administración del Estado (mediante los Decretos de Nueva Planta), construyeron el actual Palacio Real de Madrid y el Palacio de La Granja de San Ildefonso (Segovia) y fundaron grandes instituciones culturales que perduran hoy, como la Biblioteca Nacional (1712), la Real Academia Española (RAE, 1713) y la Real Academia de la Historia (1738).",
                    "La segunda mitad del siglo XVIII estuvo iluminada por las ideas de la Ilustración (el «Siglo de las Luces»), un movimiento intelectual y reformista europeo que confiaba en la educación, la ciencia, la agricultura y las obras públicas para mejorar el bienestar de la nación, representado en España por ministros e intelectuales como el asturiano Gaspar Melchor de Jovellanos, el conde de Floridablanca o el conde de Campomanes.",
                    "El monarca más admirado del siglo XVIII español fue Carlos III (1759–1788), hijo de Felipe V. Durante sus casi treinta años de reinado, Carlos III impulsó el libre comercio con América, promovió las Sociedades Económicas de Amigos del País, modernizó los puertos y caminos y realizó la primera expedición científica de vacunación mundial (la Real Expedición Filantrópica de la Vacuna de Francisco Javier Balmis pocos años después).",
                    "Carlos III transformó tan profundamente la capital de España —dotándola de alumbrado público, empedrado, alcantarillado, el Real Jardín Botánico, la Puerta de Alcalá, las fuentes de Cibeles y Neptuno y el edificio de Juan de Villanueva que hoy alberga el Museo del Prado— que los madrileños lo recuerdan con el cariñoso título de «el mejor alcalde de Madrid». En 1785, además, Carlos III eligió los colores rojo y amarillo para la bandera naval que hoy es la bandera de España."
                ],
                "questions": [
                    {
                        "question": "¿Qué dinastía real llegó al trono de España en el año 1700 con Felipe V y es la misma casa real a la que pertenece el rey actual Felipe VI?",
                        "options": [
                            "La Casa de Borbón",
                            "La Casa de Lancaster",
                            "La dinastía Romanov",
                            "La Casa de Orange"
                        ],
                        "correctIndex": 0,
                        "explanation": "Desde el año 1700 (con Felipe V), la dinastía reinante en España es la Casa de Borbón."
                    },
                    {
                        "question": "¿Qué rey ilustrado del siglo XVIII modernizó España y embelleció Madrid con monumentos como la Puerta de Alcalá y el actual Museo del Prado, siendo recordado como «el mejor alcalde de Madrid»?",
                        "options": [
                            "Carlos III",
                            "Felipe II",
                            "Alfonso X",
                            "Recaredo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Carlos III (1759–1788) es el gran monarca de la Ilustración española y es conocido como «el mejor alcalde de Madrid»."
                    },
                    {
                        "question": "¿En qué siglo se desarrolló en España y en Europa el movimiento cultural y reformista conocido como «la Ilustración» o «el Siglo de las Luces», durante el cual se fundó la Real Academia Española?",
                        "options": [
                            "En el siglo XVIII",
                            "En el siglo XII",
                            "En el siglo XV",
                            "En el siglo XX"
                        ],
                        "correctIndex": 0,
                        "explanation": "El siglo XVIII es el Siglo de las Luces o de la Ilustración."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué tratado internacional firmado en 1713 puso fin en gran medida a la Guerra de Sucesión Española y supuso la cesión de Gibraltar al Reino Unido?",
                        "options": [
                            "El Tratado de Utrecht",
                            "El Tratado de Maastricht",
                            "El Tratado de Tordesillas",
                            "El Pacto de la Moncloa"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Tratado de Utrecht (1713) reconoció a Felipe V como rey de España y cedió Gibraltar a Gran Bretaña."
                    },
                    {
                        "prompt": "¿Qué institución lingüística fundamental fue fundada en Madrid en 1713 bajo el reinado de Felipe V?",
                        "options": [
                            "La Real Academia Española (RAE)",
                            "El Tribunal Constitucional",
                            "La Agencia Espacial Española",
                            "El Defensor del Pueblo"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Real Academia Española (RAE) se fundó en 1713 durante el reinado de Felipe V."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Desde el año 1700, con el rey Felipe V, reina en España la dinastía de la Casa de ___.",
                        "answer": "Borbón",
                        "options": ["Borbón", "Austria", "Trastámara", "Tudor"],
                        "explanation": "La Casa de Borbón reina en España desde 1700.",
                        "english": "Since the year 1700, with King Philip V, the dynasty of the House of Bourbon has reigned in Spain."
                    },
                    {
                        "sentence": "El rey ___ III impulsó en el siglo XVIII las reformas de la Ilustración y la construcción de la Puerta de Alcalá.",
                        "answer": "Carlos",
                        "options": ["Carlos", "Ramiro", "Ordoño", "Boabdil"],
                        "explanation": "Carlos III fue el gran rey ilustrado del siglo XVIII.",
                        "english": "King Charles III promoted the reforms of the Enlightenment and the construction of the Puerta de Alcalá in the 18th century."
                    }
                ],
                "ex_dict": {
                    "audioText": "En el siglo dieciocho llegó al trono español la Casa de Borbón y brilló el reinado ilustrado de Carlos Tercero.",
                    "english": "In the eighteenth century the House of Bourbon came to the Spanish throne and the enlightened reign of Charles the Third shone."
                },
                "ex_sb": {
                    "words": ["La", "Casa", "de", "Borbón", "reina", "en", "España", "desde", "el", "siglo", "dieciocho."],
                    "english": "The House of Bourbon has reigned in Spain since the eighteenth century."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 23: Historia Contemporánea y Transición a la Democracia (unit_num=59, b1-historiacontemporanea)
    # =========================================================================
    {
        "slug": "historiacontemporanea",
        "unit_num": 59,
        "title": "Historia Contemporánea y Transición a la Democracia",
        "description": "La Constitución de Cádiz de 1812 («La Pepa»), la Segunda República y el voto femenino (1931), la Guerra Civil y la dictadura, la Transición (1975–1978) y la España democrática.",
        "Badge": "Historia Contemporánea",
        "lessons": [
            {
                "num": "01",
                "Title": "La Guerra de la Independencia y la Constitución de Cádiz de 1812",
                "title": "La Guerra de la Independencia y la Constitución de Cádiz de 1812",
                "grammar_slug": "promulgar-la-primera-constitucion-liberal-conocida-como-la-pepa",
                "story_slug": "cadiz1812",
                "story_title": "¡Viva la Pepa!: el 19 de marzo de 1812 en el Oratorio de San Felipe Neri",
                "objectives": [
                    "Conocer la Guerra de la Independencia (1808–1814) frente a la invasión napoleónica de José Bonaparte.",
                    "Recordar la promulgación el 19 de marzo de 1812 en Cádiz de la primera Constitución liberal de la historia de España, conocida popularmente como «La Pepa».",
                    "Practicar las construcciones «ser promulgada en Cádiz en mil ochocientos doce» y «ser conocida popularmente como La Pepa»."
                ],
                "vocab": [
                    {"lemma": "la Guerra de la Independencia (1808–1814)", "pos": "noun", "translation": "Spanish War of Independence (Peninsular War)"},
                    {"lemma": "el levantamiento del 2 de mayo de 1808", "pos": "noun", "translation": "May 2, 1808 uprising in Madrid"},
                    {"lemma": "las Cortes de Cádiz", "pos": "noun", "translation": "Cortes of Cádiz (constituent assembly)"},
                    {"lemma": "la Constitución de 1812 («La Pepa»)", "pos": "noun", "translation": "Constitution of 1812 ('La Pepa', Spain's first liberal constitution)"},
                    {"lemma": "la soberanía nacional", "pos": "noun", "translation": "national sovereignty"},
                    {"lemma": "la división de poderes", "pos": "noun", "translation": "separation of powers"},
                    {"lemma": "la libertad de imprenta", "pos": "noun", "translation": "freedom of the press"},
                    {"lemma": "el día de San José (19 de marzo)", "pos": "noun", "translation": "Saint Joseph's Day (March 19, why the 1812 Constitution is called 'La Pepa')"}
                ],
                "grammar_title": "El nacimiento del constitucionalismo español: «La Pepa» (1812)",
                "grammar_text": "La primera Constitución propiamente española de nuestra historia fue aprobada por las **Cortes de Cádiz** el **19 de marzo de 1812**, en plena Guerra de la Independencia contra las tropas de Napoleón. Por haberse promulgado el **día de San José**, el pueblo la bautizó cariñosamente como **«La Pepa»**.",
                "grammar_examples": [
                    {"es": "La primera Constitución liberal de España se aprobó en Cádiz el 19 de marzo de 1812 y se conoce como «La Pepa».", "en": "The first liberal Constitution of Spain was approved in Cádiz on March 19, 1812, and is known as 'La Pepa'."},
                    {"es": "El pintor Francisco de Goya retrató el levantamiento popular del 2 de mayo de 1808 en Madrid.", "en": "The painter Francisco de Goya portrayed the popular uprising of May 2, 1808, in Madrid."}
                ],
                "grammar_tip": "¡Pregunta fija del CCSE! ¿En qué ciudad y año se aprobó la primera Constitución española, llamada **«La Pepa»**? En **Cádiz**, el **19 de marzo de 1812**.",
                "paragraphs": [
                    "La Edad Contemporánea de España se abrió en la primavera de 1808 con una sacudida dramática. El emperador francés Napoleón Bonaparte, con el pretexto de atravesar la península hacia Portugal, ocupó militarmente las principales plazas españolas, obligó a abdicar en Bayona a Carlos IV y a su hijo Fernando VII, e impuso en el trono a su propio hermano, José Bonaparte.",
                    "El 2 de mayo de 1808, el pueblo de Madrid se alzó en armas contra las tropas napoleónicas en una jornada heroica y trágica que el pintor aragonés Francisco de Goya inmortalizaría para siempre en dos lienzos universales conservados hoy en el Museo del Prado: *El 2 de mayo de 1808 en Madrid* (o *La carga de los mamelucos*) y *El 3 de mayo en Madrid* (o *Los fusilamientos en la montaña del Príncipe Pío*). Comenzaba así la Guerra de la Independencia (1808–1814).",
                    "Mientras el país luchaba por su libertad, en la única ciudad peninsular que resistió el asedio francés gracias a sus murallas y al mar —la ciudad andaluza de Cádiz— se reunieron en septiembre de 1810 diputados procedentes de toda España y de los territorios españoles de América y Filipinas: las históricas Cortes de Cádiz.",
                    "En el Oratorio de San Felipe Neri de Cádiz, aquellos diputados redactaron y promulgaron el 19 de marzo de 1812 la primera Constitución liberal de la historia de España. Como el 19 de marzo es la festividad de San José (y a los llamados José se les dice familiarmente «Pepe» o «Pepa» en español), los ciudadanos celebraron su nacimiento al grito de «¡Viva la Pepa!».",
                    "La Constitución de Cádiz de 1812 fue un faro de libertad que inspiró a los liberales de toda Europa e Iberoamérica: proclamó por primera vez que la soberanía reside esencialmente en la Nación (y no en la voluntad absoluta del rey), estableció la división de poderes (legislativo en las Cortes con el Rey, ejecutivo y judicial), abolió la Inquisición y reconoció los derechos individuales y la libertad de imprenta."
                ],
                "questions": [
                    {
                        "question": "¿En qué ciudad y en qué año se promulgó la primera Constitución liberal de la historia de España, conocida popularmente como «La Pepa»?",
                        "options": [
                            "En Cádiz, el 19 de marzo de 1812",
                            "En Burgos, en 1512",
                            "En Barcelona, en 1931",
                            "En Oviedo, en 1713"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Constitución de Cádiz fue promulgada el 19 de marzo de 1812 y recibió el sobrenombre de «La Pepa» por aprobarse el día de San José."
                    },
                    {
                        "question": "¿Contra la invasión de qué ejército extranjero luchó el pueblo español durante la Guerra de la Independencia (1808–1814), que comenzó con el levantamiento del 2 de mayo de 1808?",
                        "options": [
                            "Contra el ejército francés de Napoleón Bonaparte",
                            "Contra el Imperio otomano",
                            "Contra el Imperio ruso",
                            "Contra el Imperio austrohúngaro"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Guerra de la Independencia enfrentó al pueblo español (con apoyo aliado británico y portugués) contra la ocupación napoleónica francesa."
                    },
                    {
                        "question": "¿Qué gran pintor español retrató los sucesos del 2 y del 3 de mayo de 1808 en Madrid y la serie de grabados «Los desastres de la guerra»?",
                        "options": [
                            "Francisco de Goya",
                            "Salvador Dalí",
                            "Joan Miró",
                            "Bartolomé Esteban Murillo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Francisco de Goya (1746–1828) fue el gran cronista visual de la Guerra de la Independencia."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Por qué se conoce popularmente como «La Pepa» a la Constitución de Cádiz de 1812?",
                        "options": [
                            "Porque fue promulgada el 19 de marzo, día de San José",
                            "Porque la redactó una reina llamada Josefa",
                            "Porque se firmó en un barco de ese nombre",
                            "Porque tenía solo doce artículos"
                        ],
                        "correctIndex": 0,
                        "explanation": "Al promulgarse el 19 de marzo (festividad de San José), recibió el apelativo popular de «La Pepa»."
                    },
                    {
                        "prompt": "¿Qué principio revolucionario proclamó la Constitución de Cádiz de 1812 frente al absolutismo?",
                        "options": [
                            "La soberanía nacional, la división de poderes y la libertad de imprenta",
                            "El poder absoluto e ilimitado del monarca",
                            "La prohibición de las imprentas y periódicos",
                            "La supresión de las Cortes parlamentarias"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Constitución de 1812 proclamó la soberanía nacional y la división de poderes."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La primera Constitución española se aprobó en ___ el 19 de marzo de 1812.",
                        "answer": "Cádiz",
                        "options": ["Cádiz", "Vigo", "Huesca", "Lugo"],
                        "explanation": "Las Cortes de Cádiz promulgaron la Constitución de 1812.",
                        "english": "The first Spanish Constitution was approved in Cádiz on March 19, 1812."
                    },
                    {
                        "sentence": "La Constitución de 1812 es conocida popularmente con el nombre de «La ___».",
                        "answer": "Pepa",
                        "options": ["Pepa", "Gloriosa", "Novena", "Magna"],
                        "explanation": "«La Pepa» es el nombre popular de la Constitución de Cádiz de 1812.",
                        "english": "The Constitution of 1812 is popularly known by the name 'La Pepa'."
                    }
                ],
                "ex_dict": {
                    "audioText": "La primera Constitución española se promulgó en Cádiz en mil ochocientos doce y se conoce como La Pepa.",
                    "english": "The first Spanish Constitution was promulgated in Cádiz in eighteen twelve and is known as La Pepa."
                },
                "ex_sb": {
                    "words": ["La", "Constitución", "de", "Cádiz", "de", "mil", "ochocientos", "doce", "proclamó", "la", "soberanía", "nacional."],
                    "english": "The Cádiz Constitution of eighteen twelve proclaimed national sovereignty."
                }
            },
            {
                "num": "02",
                "Title": "Del Siglo XIX a la Segunda República y el Voto Femenino",
                "title": "Del Siglo XIX a la Segunda República y el Voto Femenino",
                "grammar_slug": "reconocer-por-primera-vez-el-sufragio-femenino",
                "story_slug": "sigloxixyxx",
                "story_title": "1898, Clara Campoamor en la tribuna de 1931 y la herida de la Guerra Civil",
                "objectives": [
                    "Comocer la crisis de 1898 (pérdida de las últimas colonias de Cuba, Puerto Rico y Filipinas) y el nacimiento de la Generación del 98.",
                    "Recordar la proclamación de la Segunda República en 1931 y la conquista histórica del sufragio femenino impulsada por Clara Campoamor (aprobado en la Constitución de 1931 y ejercido por primera vez en las elecciones generales de 1933), así como las fechas de la Guerra Civil Española (1936–1939).",
                    "Practicar las construcciones «aprobarse el derecho al voto de las mujeres» y «estallar la Guerra Civil en mil novecientos treinta y seis»."
                ],
                "vocab": [
                    {"lemma": "el Desastre del 98 (1898)", "pos": "noun", "translation": "Crisis of 1898 (loss of Cuba, Puerto Rico, and the Philippines)"},
                    {"lemma": "la Segunda República Española (1931–1936)", "pos": "noun", "translation": "Second Spanish Republic"},
                    {"lemma": "el sufragio femenino (voto de la mujer)", "pos": "noun", "translation": "women's suffrage (approved in 1931, first voted in 1933)"},
                    {"lemma": "Clara Campoamor", "pos": "noun", "translation": "Clara Campoamor (lawyer and deputy who championed women's right to vote in 1931)"},
                    {"lemma": "la Guerra Civil Española (1936–1939)", "pos": "noun", "translation": "Spanish Civil War"},
                    {"lemma": "el bombardeo de Guernica (1937)", "pos": "noun", "translation": "bombing of Guernica"},
                    {"lemma": "la Restauración borbónica", "pos": "noun", "translation": "Bourbon Restoration (1874–1931)"},
                    {"lemma": "la Generación del 98", "pos": "noun", "translation": "Generation of '98 (literary and intellectual movement)"}
                ],
                "grammar_title": "Hitos del primer tercio del siglo XX: el voto femenino (1931/1933) y la Guerra Civil (1936–1939)",
                "grammar_text": "En el examen CCSE se preguntan tres fechas fundamentales de este periodo: **1898** (fin del imperio colonial de ultramar en Cuba, Puerto Rico y Filipinas), **1931 / 1933** (aprobación constitucional del **voto femenino** en 1931 gracias a **Clara Campoamor**, durante la **Segunda República**, y primer ejercicio en las urnas en **1933**), y **1936–1939** (la **Guerra Civil Española**).",
                "grammar_examples": [
                    {"es": "Gracias al discurso de la diputada Clara Campoamor, la Constitución de 1931 reconoció el derecho al voto de las mujeres.", "en": "Thanks to the speech by Deputy Clara Campoamor, the 1931 Constitution recognized women's right to vote."},
                    {"es": "Las mujeres españolas votaron por primera vez en unas elecciones generales en noviembre de 1933.", "en": "Spanish women voted for the first time in a general election in November 1933."}
                ],
                "grammar_tip": "¡Preguntas favoritas del CCSE! 1) ¿Quién fue la gran defensora del voto femenino en las Cortes de 1931? **Clara Campoamor**. 2) ¿En qué años tuvo lugar la Guerra Civil Española? Entre **1936 y 1939**.",
                "paragraphs": [
                    "A lo largo del siglo XIX, España vivió la lucha entre absolutistas y liberales, la independencia de las nuevas repúblicas hispanoamericanas, el inicio de la industrialización y el ferrocarril (con la primera línea peninsular Barcelona-Mataró en 1848) y el periodo constitucional de la Restauración iniciado en 1874 con Alfonso XII. Al terminar el siglo, en el año 1898, tras la guerra hispano-estadounidense y el Tratado de París, España perdió sus tres últimas posesiones de ultramar: Cuba, Puerto Rico y Filipinas. Aquella conmoción moral dio nacimiento a un extraordinario grupo de escritores y pensadores preocupados por la regeneración de España: la Generación del 98.",
                    "El 14 de abril de 1931, tras unas elecciones municipales en las que triunfaron las candidaturas republicanas en las grandes ciudades y la marcha del rey Alfonso XIII, se proclamó la Segunda República Española (1931–1936). La Constitución republicana de diciembre de 1931 impulsó grandes reformas educativas (creando miles de escuelas públicas y las Misiones Pedagógicas), el matrimonio civil y el divorcio, y los primeros estatutos de autonomía.",
                    "Pero el hito democrático más luminoso de 1931 se vivió el 1 de octubre en el hemiciclo del Congreso de los Diputados: la abogada y diputada madrileña Clara Campoamor defendió con brillantez y valentía el sufragio universal sin exclusión de sexo frente a quienes temían que aún no había llegado el momento. Gracias a su empeño, el artículo 36 de la Constitución de 1931 reconoció el voto femenino en igualdad con los hombres, y en noviembre de 1933 las mujeres españolas ejercieron por primera vez su derecho al voto en unas elecciones generales, antes incluso que en países como Francia o Italia.",
                    "Lamentablemente, la creciente polarización política y social de los años treinta —en una Europa sacudida por el ascenso de los totalitarismos— desembocó el 17 y 18 de julio de 1936 en una sublevación militar que dividió el país en dos zonas y dio comienzo a la Guerra Civil Española (1936–1939).",
                    "Durante casi tres años (desde julio de 1936 hasta el 1 de abril de 1939), la Guerra Civil causó cientos de miles de víctimas, la muerte de figuras como el poeta Federico García Lorca, la destrucción de ciudades como Guernica (cuyo bombardeo en abril de 1937 inspiró el célebre lienzo antibélico de Pablo Picasso para el Pabellón de la República en París) y el exilio de medio millón de españoles."
                ],
                "questions": [
                    {
                        "question": "¿Qué abogada y diputada defendió en las Cortes Constituyentes de 1931 el reconocimiento del derecho al voto de las mujeres en España?",
                        "options": [
                            "Clara Campoamor",
                            "Emilia Pardo Bazán",
                            "Rosalía de Castro",
                            "Margarita Salas"
                        ],
                        "correctIndex": 0,
                        "explanation": "Clara Campoamor (1888–1972) logró que las Cortes de 1931 aprobaran el sufragio femenino en España."
                    },
                    {
                        "question": "¿En qué años tuvo lugar la Guerra Civil Española?",
                        "options": [
                            "Entre 1936 y 1939",
                            "Entre 1914 y 1918",
                            "Entre 1808 y 1814",
                            "Entre 1975 y 1978"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Guerra Civil Española comenzó en julio de 1936 y terminó el 1 de abril de 1939."
                    },
                    {
                        "question": "¿Qué tres últimos territorios de ultramar dejó de administrar España en el año 1898, hecho que dio nombre a la «Generación del 98»?",
                        "options": [
                            "Cuba, Puerto Rico y Filipinas",
                            "Mallorca, Menorca e Ibiza",
                            "Tenerife, Gran Canaria y Lanzarote",
                            "Flandes, Nápoles y Sicilia"
                        ],
                        "correctIndex": 0,
                        "explanation": "En 1898 España perdió sus últimas colonias de ultramar: Cuba, Puerto Rico y Filipinas."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué año votaron por primera vez las mujeres españolas en unas elecciones generales tras el reconocimiento constitucional de 1931?",
                        "options": [
                            "En 1933",
                            "En 1812",
                            "En 1995",
                            "En 2004"
                        ],
                        "correctIndex": 0,
                        "explanation": "Reconocido el derecho en la Constitución de 1931, las mujeres votaron en elecciones generales en noviembre de 1933."
                    },
                    {
                        "prompt": "¿Qué régimen político existía en España cuando se aprobó por primera vez el sufragio femenino en 1931?",
                        "options": [
                            "La Segunda República",
                            "El Califato de Córdoba",
                            "El Imperio de Carlos V",
                            "La Regencia de Espartero"
                        ],
                        "correctIndex": 0,
                        "explanation": "El sufragio femenino fue aprobado por las Cortes de la Segunda República en 1931."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La diputada Clara ___ fue la gran impulsora del reconocimiento del voto femenino en 1931.",
                        "answer": "Campoamor",
                        "options": ["Campoamor", "Laforet", "Matute", "Chacel"],
                        "explanation": "Clara Campoamor defendió el voto femenino en las Cortes de 1931.",
                        "english": "Deputy Clara Campoamor was the great promoter of the recognition of women's suffrage in 1931."
                    },
                    {
                        "sentence": "La Guerra ___ Española tuvo lugar entre los años 1936 y 1939.",
                        "answer": "Civil",
                        "options": ["Civil", "Púnica", "Colonial", "Sucesoria"],
                        "explanation": "La Guerra Civil Española se desarrolló de 1936 a 1939.",
                        "english": "The Spanish Civil War took place between the years 1936 and 1939."
                    }
                ],
                "ex_dict": {
                    "audioText": "Clara Campoamor defendió el voto de las mujeres en mil novecientos treinta y uno durante la Segunda República.",
                    "english": "Clara Campoamor defended women's right to vote in nineteen thirty-one during the Second Republic."
                },
                "ex_sb": {
                    "words": ["La", "Guerra", "Civil", "Española", "tuvo", "lugar", "entre", "mil", "novecientos", "treinta", "y", "seis", "y", "mil", "novecientos", "treinta", "y", "nueve."],
                    "english": "The Spanish Civil War took place between nineteen thirty-six and nineteen thirty-nine."
                }
            },
            {
                "num": "03",
                "Title": "La Dictadura de Francisco Franco (1939–1975)",
                "title": "La Dictadura de Francisco Franco (1939–1975)",
                "grammar_slug": "prolongarse-desde-el-final-de-la-guerra-hasta-mil-novecientos-setenta-y-cinco",
                "story_slug": "dictadura",
                "story_title": "Casi cuarenta años sin libertades políticas: de la posguerra de 1939 a noviembre de 1975",
                "objectives": [
                    "Situar cronológicamente la dictadura del general Francisco Franco entre el final de la Guerra Civil (1 de abril de 1939) y su muerte (20 de noviembre de 1975).",
                    "Comprender las características políticas del régimen (ausencia de Constitución democrática, prohibición de partidos políticos, sindicatos libres y estatutos de autonomía, y censura) y los cambios económicos y sociales de los años cincuenta y sesenta.",
                    "Practicar las construcciones temporales «prolongarse durante casi cuarenta años» y «finalizar en noviembre de mil novecientos setenta y cinco»."
                ],
                "vocab": [
                    {"lemma": "la dictadura de Francisco Franco (1939–1975)", "pos": "noun", "translation": "dictatorship of Francisco Franco"},
                    {"lemma": "la posguerra y la autarquía", "pos": "noun", "translation": "post-war period and economic autarky (1940s)"},
                    {"lemma": "las cartillas de racionamiento", "pos": "noun", "translation": "ration books"},
                    {"lemma": "la supresión de libertades políticas", "pos": "noun", "translation": "suppression of political freedoms"},
                    {"lemma": "el exilio republicano", "pos": "noun", "translation": "Republican exile (to Mexico, France, Argentina, etc.)"},
                    {"lemma": "el Plan de Estabilización (1959)", "pos": "noun", "translation": "1959 Stabilization Plan (economic opening)"},
                    {"lemma": "el éxodo rural y la emigración exterior", "pos": "noun", "translation": "rural-to-urban migration and emigration to Western Europe"},
                    {"lemma": "el 20 de noviembre de 1975", "pos": "noun", "translation": "November 20, 1975 (death of Franco and end of the dictatorship)"}
                ],
                "grammar_title": "Cronología del siglo XX: el periodo 1939–1975",
                "grammar_text": "Al concluir la Guerra Civil el **1 de abril de 1939**, se instauró en España la **dictadura del general Francisco Franco**, un régimen autoritario que concentró todos los poderes del Estado y se prolongó durante treinta y seis años hasta su fallecimiento el **20 de noviembre de 1975**, fecha en que se abrió paso a la **Transición a la democracia**.",
                "grammar_examples": [
                    {"es": "La dictadura de Francisco Franco comenzó al terminar la Guerra Civil en 1939 y finalizó con su muerte en 1975.", "en": "The dictatorship of Francisco Franco began at the end of the Civil War in 1939 and ended with his death in 1975."},
                    {"es": "Durante la dictadura estuvieron prohibidos los partidos políticos, los sindicatos libres y los estatutos de autonomía.", "en": "During the dictatorship political parties, free trade unions, and statutes of autonomy were banned."}
                ],
                "grammar_tip": "Recuerda las fechas exactas para el CCSE: Guerra Civil = **1936–1939**. Dictadura de Franco = **1939–1975**. Transición y Constitución = **1975–1978**.",
                "paragraphs": [
                    "El 1 de abril de 1939, al terminar la Guerra Civil, se estableció en España la dictadura militar y personal del general Francisco Franco, quien asumió como «Caudillo» la Jefatura del Estado, la Presidencia del Gobierno y el mando supremo de los ejércitos. Durante casi cuatro décadas (1939–1975), España careció de Constitución democrática y de elecciones libres.",
                    "El nuevo régimen suprimió el sufragio universal, ilegalizó todos los partidos políticos (estableciendo un partido único, FET y de las JONS) y los sindicatos de clase (sustituidos por el Sindicato Vertical obligatorio), derogó los estatutos de autonomía, restringió el uso público de las lenguas cooficiales distintas del castellano e impuso la censura previa sobre libros, prensa, cine y teatro.",
                    "Los años cuarenta —la dura posguerra— estuvieron marcados por la represión política, el exilio de grandes intelectuales, artistas y científicos en países como México, Argentina, Francia o Estados Unidos (entre ellos Antonio Machado, Juan Ramón Jiménez, Rafael Alberti, Luis Buñuel, Pau Casals o Severo Ochoa), el aislamiento internacional (España no ingresó en la ONU hasta 1955) y la escasez económica de la autarquía y las cartillas de racionamiento.",
                    "A partir del Plan de Estabilización de 1959, la economía española se abrió al exterior y vivió durante la década de los sesenta una rápida industrialización y urbanización. Millones de familias del campo emigraron hacia las zonas industriales de Madrid, Cataluña y el País Vasco o hacia países europeos como Alemania, Francia y Suiza, mientras llegaban a las costas españolas millones de turistas europeos y crecía una nueva clase media urbana y universitaria que reclamaba libertades democráticas.",
                    "El 20 de noviembre de 1975 falleció en Madrid Francisco Franco. Tan solo dos días después, el 22 de noviembre de 1975, fue proclamado ante las Cortes el rey Juan Carlos I, quien desde su primer mensaje expresó su voluntad de ser «el Rey de todos los españoles» e impulsar el camino hacia una democracia plena e integrada en Europa."
                ],
                "questions": [
                    {
                        "question": "¿Entre qué años se prolongó en España la dictadura del general Francisco Franco?",
                        "options": [
                            "Desde el final de la Guerra Civil en 1939 hasta su muerte en noviembre de 1975",
                            "Desde 1812 hasta 1898",
                            "Desde 1978 hasta 1986",
                            "Desde 1900 hasta 1931"
                        ],
                        "correctIndex": 0,
                        "explanation": "La dictadura de Francisco Franco comenzó en 1939 al finalizar la Guerra Civil y terminó con su muerte el 20 de noviembre de 1975."
                    },
                    {
                        "question": "¿En qué año falleció Francisco Franco y comenzó en España el proceso histórico conocido como «la Transición a la democracia»?",
                        "options": [
                            "En 1975",
                            "En 1939",
                            "En 1992",
                            "En 1955"
                        ],
                        "correctIndex": 0,
                        "explanation": "Francisco Franco murió el 20 de noviembre de 1975, dando paso al inicio de la Transición democrática."
                    },
                    {
                        "question": "¿Qué situación tenían los partidos políticos y los sindicatos libres en España durante la etapa de 1939 a 1975?",
                        "options": [
                            "Estaban prohibidos y no se celebraban elecciones democráticas libres",
                            "Se celebraban elecciones generales multipartidistas cada dos años",
                            "Existían diecisiete parlamentos autonómicos en funcionamiento",
                            "Funcionaba el Tribunal Constitucional de 1978"
                        ],
                        "correctIndex": 0,
                        "explanation": "Durante la dictadura (1939–1975) estuvieron prohibidos los partidos políticos, los sindicatos libres y los estatutos de autonomía."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué organización internacional ingresó España en diciembre de 1955 tras años de aislamiento diplomático de posguerra?",
                        "options": [
                            "En la Organización de las Naciones Unidas (ONU)",
                            "En la zona euro",
                            "En el espacio Schengen",
                            "En el Mercosur"
                        ],
                        "correctIndex": 0,
                        "explanation": "España ingresó en la Organización de las Naciones Unidas (ONU) en diciembre de 1955."
                    },
                    {
                        "prompt": "¿Quién fue proclamado Rey de España el 22 de noviembre de 1975 tras el fallecimiento de Francisco Franco, impulsando la Transición a la democracia?",
                        "options": [
                            "El rey Juan Carlos I",
                            "El rey Carlos III",
                            "El rey Alfonso XII",
                            "El rey Felipe II"
                        ],
                        "correctIndex": 0,
                        "explanation": "Juan Carlos I fue proclamado Rey el 22 de noviembre de 1975 y reinó hasta su abdicación en junio de 2014."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La dictadura de Francisco Franco comenzó en 1939 y terminó con su fallecimiento en noviembre de ___.",
                        "answer": "1975",
                        "options": ["1975", "1931", "1898", "2002"],
                        "explanation": "En noviembre de 1975 terminó la dictadura y comenzó la Transición a la democracia.",
                        "english": "The dictatorship of Francisco Franco began in 1939 and ended with his death in November 1975."
                    },
                    {
                        "sentence": "El 22 de noviembre de 1975 fue proclamado Rey de España ___ Carlos I.",
                        "answer": "Juan",
                        "options": ["Juan", "Felipe", "Fernando", "Amadeo"],
                        "explanation": "Juan Carlos I fue el monarca de la Transición democrática.",
                        "english": "On November 22, 1975, Juan Carlos I was proclaimed King of Spain."
                    }
                ],
                "ex_dict": {
                    "audioText": "La dictadura de Francisco Franco terminó en mil novecientos setenta y cinco y dio paso a la Transición.",
                    "english": "The dictatorship of Francisco Franco ended in nineteen seventy-five and gave way to the Transition."
                },
                "ex_sb": {
                    "words": ["En", "noviembre", "de", "mil", "novecientos", "setenta", "y", "cinco", "comenzó", "la", "Transición", "democrática."],
                    "english": "In November nineteen seventy-five the democratic Transition began."
                }
            },
            {
                "num": "04",
                "Title": "La Transición Democrática (1975–1978) y Adolfo Suárez",
                "title": "La Transición Democrática (1975–1978) y Adolfo Suárez",
                "grammar_slug": "pasar-de-la-dictadura-a-la-democracia-mediante-el-consenso",
                "story_slug": "transicion",
                "story_title": "De la ley a la ley: Adolfo Suárez, el 15 de junio de 1977 y el espíritu del consenso",
                "objectives": [
                    "Comprender el proceso de la Transición Española (1975–1978): el paso pacífico y pactado de la dictadura a una democracia constitucional plena.",
                    "Recordar al primer presidente del Gobierno de la democracia (Adolfo Suárez, al frente de UCD), las primeras elecciones democráticas del 15 de junio de 1977, los Pactos de la Moncloa (1977) y el referéndum constitucional del 6 de diciembre de 1978.",
                    "Practicar las construcciones «celebrarse las primeras elecciones democráticas en mil novecientos setenta y siete» y «ser elegido primer presidente del Gobierno de la democracia»."
                ],
                "vocab": [
                    {"lemma": "la Transición Española (1975–1978)", "pos": "noun", "translation": "Spanish Transition to democracy"},
                    {"lemma": "Adolfo Suárez", "pos": "noun", "translation": "Adolfo Suárez (first Prime Minister of democratic Spain, 1976–1981)"},
                    {"lemma": "la Unión de Centro Democrático (UCD)", "pos": "noun", "translation": "Union of the Democratic Centre (party led by Adolfo Suárez)"},
                    {"lemma": "la Ley para la Reforma Política (1976)", "pos": "noun", "translation": "Political Reform Act"},
                    {"lemma": "las primeras elecciones democráticas (15 de junio de 1977)", "pos": "noun", "translation": "first democratic general elections since 1936"},
                    {"lemma": "los Pactos de la Moncloa (octubre de 1977)", "pos": "noun", "translation": "Moncloa Pacts (economic and political consensus agreements)"},
                    {"lemma": "el espíritu de consenso y reconciliación", "pos": "noun", "translation": "spirit of consensus and national reconciliation"},
                    {"lemma": "los siete Padres de la Constitución", "pos": "noun", "translation": "the seven Founding Fathers of the 1978 Constitution"}
                ],
                "grammar_title": "El vocabulario de la reconciliación: la Transición (1975–1978)",
                "grammar_text": "Se conoce como **la Transición** al proceso histórico pacífico mediante el cual España pasó de la dictadura de Franco a un Estado social y democrático de Derecho entre **1975 y 1978**, impulsado por el rey **Juan Carlos I** y el presidente del Gobierno **Adolfo Suárez** (primer presidente elegido en las **primeras elecciones democráticas del 15 de junio de 1977**).",
                "grammar_examples": [
                    {"es": "Adolfo Suárez fue el primer presidente del Gobierno de la etapa democrática actual tras ganar las elecciones de junio de 1977.", "en": "Adolfo Suárez was the first Prime Minister of the current democratic era after winning the elections of June 1977."},
                    {"es": "En octubre de 1977 todos los partidos parlamentarios firmaron los Pactos de la Moncloa para superar la crisis económica.", "en": "In October 1977 all parliamentary parties signed the Moncloa Pacts to overcome the economic crisis."}
                ],
                "grammar_tip": "¡Dos preguntas fijas del CCSE! 1) ¿Quién fue el primer presidente del Gobierno de la democracia española tras la Constitución/Transición? **Adolfo Suárez**. 2) ¿En qué año se celebraron las primeras elecciones generales democráticas tras el franquismo? En **1977** (15 de junio de 1977).",
                "paragraphs": [
                    "Entre noviembre de 1975 y diciembre de 1978, la sociedad española protagonizó uno de los capítulos más admirados de la historia política contemporánea: la Transición a la democracia. Frente a quienes temían un nuevo enfrentamiento civil, los españoles demostraron una madurez cívica ejemplar y lograron desmontar pacíficamente las estructuras de la dictadura para construir un régimen de libertades, reconciliación nacional y consenso.",
                    "El gran arquitecto político de aquel cambio fue Adolfo Suárez (1932–2014), un joven político abulense nombrado presidente del Gobierno por el rey Juan Carlos I en julio de 1976, con el apoyo jurídico de Torcuato Fernández-Miranda. Bajo la máxima de ir «de la ley a la ley a través de la ley», Suárez impulsó la Ley para la Reforma Política, que fue aprobada por abrumadora mayoría de los ciudadanos en el referéndum de diciembre de 1976.",
                    "En los primeros meses de 1977 el Gobierno de Adolfo Suárez legalizó todos los partidos políticos —incluido el Partido Comunista de España en la Semana Santa de 1977— y los sindicatos libres (como UGT y Comisiones Obreras), decretó la amnistía y convocó las primeras elecciones generales democráticas en cuarenta y un años.",
                    "El 15 de junio de 1977, millones de españoles acudieron emocionados a las urnas en libertad. Aquellas primeras elecciones fueron ganadas por la Unión de Centro Democrático (UCD), la coalición liderada por Adolfo Suárez, quien se convirtió así en el primer presidente del Gobierno elegido democráticamente en la España contemporánea (seguido en escaños por el PSOE de Felipe González). En octubre de ese mismo año 1977, todos los partidos con representación parlamentaria firmaron los históricos Pactos de la Moncloa para estabilizar la economía, frenar la inflación y consolidar las libertades.",
                    "Finalmente, aquellas Cortes elegidas en 1977 actuaron como Cortes Constituyentes: una ponencia de siete diputados de distintas ideologías —los siete «Padres de la Constitución»— redactó el texto constitucional, que fue aprobado por las Cortes el 31 de octubre, ratificado por el pueblo español en el referéndum del 6 de diciembre de 1978 y sancionado el 27 de diciembre de 1978."
                ],
                "questions": [
                    {
                        "question": "¿Quién fue el primer presidente del Gobierno de la democracia española durante la Transición, líder de la Unión de Centro Democrático (UCD) y ganador de las elecciones generales de 1977 y 1979?",
                        "options": [
                            "Adolfo Suárez",
                            "Manuel Azaña",
                            "Antonio Cánovas del Castillo",
                            "Práxedes Mateo Sagasta"
                        ],
                        "correctIndex": 0,
                        "explanation": "Adolfo Suárez presidió el Gobierno entre 1976 y 1981 y ganó las primeras elecciones democráticas de junio de 1977."
                    },
                    {
                        "question": "¿En qué fecha se celebraron en España las primeras elecciones generales democráticas tras casi cuarenta años de dictadura?",
                        "options": [
                            "El 15 de junio de 1977",
                            "El 12 de octubre de 1992",
                            "El 1 de enero de 1986",
                            "El 14 de abril de 1931"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 15 de junio de 1977 se celebraron las primeras elecciones generales libres desde 1936."
                    },
                    {
                        "question": "¿Con qué nombre se conocen los acuerdos económicos, sociales y políticos firmados en octubre de 1977 por todos los partidos parlamentarios con el Gobierno de Adolfo Suárez para estabilizar el país?",
                        "options": [
                            "Los Pactos de la Moncloa",
                            "El Tratado de Tordesillas",
                            "El Convenio de Vergara",
                            "La Paz de los Pirineos"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Pactos de la Moncloa (octubre de 1977) son el símbolo del acuerdo económico y político de la Transición."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Con qué nombre se conoce el proceso histórico mediante el cual España pasó pacíficamente de la dictadura de Franco a la democracia constitucional a partir de 1975?",
                        "options": [
                            "La Transición (o Transición democrática)",
                            "La Reconquista",
                            "La Restauración",
                            "La Ilustración"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Transición Española es el paso pacífico de la dictadura al régimen constitucional de 1978."
                    },
                    {
                        "prompt": "¿Qué aeropuerto internacional lleva hoy el nombre de Adolfo Suárez en homenaje al primer presidente del Gobierno de la democracia española?",
                        "options": [
                            "El Aeropuerto de Madrid-Barajas (Aeropuerto Adolfo Suárez Madrid-Barajas)",
                            "El Aeropuerto de Palma de Mallorca",
                            "El Aeropuerto de Bilbao",
                            "El Aeropuerto de Tenerife Norte"
                        ],
                        "correctIndex": 0,
                        "explanation": "Desde 2014, el principal aeropuerto de España se denomina oficialmente Aeropuerto Adolfo Suárez Madrid-Barajas."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Adolfo ___ fue el primer presidente del Gobierno de la democracia española tras ganar las elecciones de junio de 1977.",
                        "answer": "Suárez",
                        "options": ["Suárez", "Nebrija", "Jovellanos", "Sorolla"],
                        "explanation": "Adolfo Suárez lideró el Gobierno de la Transición y ganó las elecciones de 1977 y 1979.",
                        "english": "Adolfo Suárez was the first Prime Minister of Spanish democracy after winning the June 1977 elections."
                    },
                    {
                        "sentence": "En octubre de 1977, las fuerzas políticas firmaron los Pactos de la ___ para hacer frente a la crisis económica.",
                        "answer": "Moncloa",
                        "options": ["Moncloa", "Zarzuela", "Aljafería", "Magdalena"],
                        "explanation": "Los Pactos de la Moncloa fueron firmados en octubre de 1977 en el Palacio de la Moncloa.",
                        "english": "In October 1977, political forces signed the Moncloa Pacts to address the economic crisis."
                    }
                ],
                "ex_dict": {
                    "audioText": "Adolfo Suárez fue el primer presidente del Gobierno de la democracia tras las elecciones de mil novecientos setenta y siete.",
                    "english": "Adolfo Suárez was the first Prime Minister of the democracy after the elections of nineteen seventy-seven."
                },
                "ex_sb": {
                    "words": ["La", "Transición", "permitió", "pasar", "pacíficamente", "de", "la", "dictadura", "a", "la", "democracia."],
                    "english": "The Transition made it possible to pass peacefully from dictatorship to democracy."
                }
            },
            {
                "num": "05",
                "Title": "La Democracia Consolidada: De 1981 y 1992 hasta la Actualidad",
                "title": "La Democracia Consolidada: De 1981 y 1992 hasta la Actualidad",
                "grammar_slug": "consolidar-el-estado-de-las-autonomias-y-la-integracion-europea",
                "story_slug": "democraciaconsolidada",
                "story_title": "El fracaso del 23-F, la integración en la OTAN y la UE, y el gran año de 1992",
                "objectives": [
                    "Conocer la superación del intento de golpe de Estado del 23 de febrero de 1981 (23-F) y el ingreso de España en la OTAN (1982) y en las Comunidades Europeas / UE (1 de enero de 1986).",
                    "Recordar los grandes hitos de 1992 (Juegos Olímpicos de Barcelona, Exposición Universal de Sevilla e inauguración del primer tren AVE Madrid-Sevilla), la lista de los presidentes del Gobierno de la democracia y la proclamación de Felipe VI en 2014.",
                    "Practicar las construcciones «consolidarse la democracia» y «celebrarse en mil novecientos noventa y dos»."
                ],
                "vocab": [
                    {"lemma": "el 23-F (23 de febrero de 1981)", "pos": "noun", "translation": "February 23, 1981 failed coup d'état attempt"},
                    {"lemma": "el ingreso en la OTAN (1982)", "pos": "noun", "translation": "Spain's entry into NATO (1982)"},
                    {"lemma": "los Juegos Olímpicos de Barcelona (1992)", "pos": "noun", "translation": "1992 Barcelona Olympic Games"},
                    {"lemma": "la Exposición Universal de Sevilla (Expo 92)", "pos": "noun", "translation": "1992 Universal Exposition of Seville"},
                    {"lemma": "el tren de Alta Velocidad Española (AVE)", "pos": "noun", "translation": "Spanish High-Speed Rail (first line Madrid–Seville opened in 1992)"},
                    {"lemma": "los presidentes del Gobierno de la democracia", "pos": "noun", "translation": "Prime Ministers of democratic Spain (Suárez, Calvo-Sotelo, González, Aznar, Zapatero, Rajoy, Sánchez)"},
                    {"lemma": "la proclamación de Felipe VI (19 de junio de 2014)", "pos": "noun", "translation": "proclamation of King Felipe VI"},
                    {"lemma": "el fin del terrorismo de ETA (2011)", "pos": "noun", "translation": "definitive end of ETA terrorism"}
                ],
                "grammar_title": "Los presidentes y grandes hitos de la España democrática (1978–actualidad)",
                "grammar_text": "Desde la aprobación de la Constitución de 1978, siete políticos han ocupado la **Presidencia del Gobierno de España**: **Adolfo Suárez** (UCD), **Leopoldo Calvo-Sotelo** (UCD), **Felipe González** (PSOE), **José María Aznar** (PP), **José Luis Rodríguez Zapatero** (PSOE), **Mariano Rajoy** (PP) y **Pedro Sánchez** (PSOE).",
                "grammar_examples": [
                    {"es": "En el año 1992 España celebró los Juegos Olímpicos de Barcelona y la Exposición Universal de Sevilla.", "en": "In the year 1992 Spain celebrated the Olympic Games in Barcelona and the Universal Exposition in Seville."},
                    {"es": "Ese mismo año 1992 se inauguró entre Madrid y Sevilla la primera línea del tren de alta velocidad (AVE).", "en": "That same year 1992, the first high-speed train (AVE) line was inaugurated between Madrid and Seville."}
                ],
                "grammar_tip": "¡Memoriza para el CCSE el año mágico **1992**! En **1992** coincidieron tres grandes eventos en España: 1) **Juegos Olímpicos de Barcelona**, 2) **Exposición Universal de Sevilla (Expo 92)** y 3) **primera línea del AVE (Madrid-Sevilla)**.",
                "paragraphs": [
                    "La joven democracia española nacida en 1978 superó su prueba de fuego más difícil la tarde del 23 de febrero de 1981 (el «23-F»). Durante la votación de investidura de Leopoldo Calvo-Sotelo como presidente del Gobierno tras la dimisión de Adolfo Suárez, un grupo de guardias civiles al mando del teniente coronel Tejero irrumpió por la fuerza en el hemiciclo del Congreso de los Diputados intentando dar un golpe de Estado militar. Aquella noche, el firme mensaje televisado del rey Juan Carlos I en defensa de la Constitución y el respaldo masivo de toda la ciudadanía hicieron fracasar el golpe y consolidaron definitivamente la democracia.",
                    "Bajo la breve presidencia de Leopoldo Calvo-Sotelo (1981–1982), España ingresó en mayo de 1982 en la Organización del Tratado del Atlántico Norte (OTAN, permanencia ratificada por los ciudadanos en el referéndum de 1986). En octubre de 1982, el Partido Socialista Obrero Español (PSOE), liderado por Felipe González, obtuvo una histórica mayoría absoluta, iniciando una etapa de catorce años de gobierno (1982–1996) en la que se universalizaron la sanidad, la educación y las pensiones, se culminó el mapa de los 17 Estatutos de Autonomía (1983) y España firmó e ingresó en las Comunidades Europeas (hoy Unión Europea) el 1 de enero de 1986.",
                    "El año 1992 mostró al mundo entero el rostro de una España moderna, abierta y creativa. Aquel verano se celebraron los Juegos Olímpicos de Barcelona 92 y la Exposición Universal de Sevilla (Expo 92), mientras Madrid ejercía como Capital Europea de la Cultura y se inauguraba entre Madrid y Sevilla la primera línea del tren de Alta Velocidad Española (AVE); hoy España posee la red de alta velocidad ferroviaria más extensa de toda Europa.",
                    "La alternancia democrática pacífica continuó con los gobiernos del Partido Popular presididos por José María Aznar (1996–2004, etapa en la que España adoptó el euro, puesto en circulación en 2002, y profesionalizó las Fuerzas Armadas), los gobiernos socialistas de José Luis Rodríguez Zapatero (2004–2011, que impulsaron las leyes contra la violencia de género, el matrimonio igualitario y la dependencia, y bajo los cuales la banda terrorista ETA anunció en octubre de 2011 el cese definitivo de su violencia tras décadas de dolor), los gobiernos populares de Mariano Rajoy (2011–2018) y, desde junio de 2018, los gobiernos presididos por Pedro Sánchez.",
                    "En junio de 2014, tras la abdicación del rey Juan Carlos I, las Cortes Generales proclamaron Rey de España a su hijo Felipe VI, casado con la reina Letizia y padre de la princesa de Asturias, Leonor de Borbón, y de la infanta Sofía."
                ],
                "questions": [
                    {
                        "question": "¿Qué tres grandes acontecimientos internacionales y de infraestructuras se celebraron o inauguraron en España en el año 1992?",
                        "options": [
                            "Los Juegos Olímpicos de Barcelona, la Exposición Universal de Sevilla (Expo 92) y la primera línea del AVE (Madrid-Sevilla)",
                            "La Constitución de Cádiz, el Museo del Prado y el Canal de Castilla",
                            "El ingreso en la ONU, el Plan de Estabilización y el voto femenino",
                            "La entrada en circulación del euro, el tratado de Schengen y la reforma del artículo 49"
                        ],
                        "correctIndex": 0,
                        "explanation": "En 1992 coincidieron los Juegos Olímpicos de Barcelona, la Expo 92 de Sevilla y la primera línea del tren AVE entre Madrid y Sevilla."
                    },
                    {
                        "question": "¿En qué año ingresó España en la OTAN (Organización del Tratado del Atlántico Norte) y en qué año ingresó en la Comunidad Económica Europea (hoy Unión Europea)?",
                        "options": [
                            "En la OTAN en 1982 y en las Comunidades Europeas (UE) en 1986",
                            "En ambas organizaciones en 1945",
                            "En la OTAN en 1931 y en la UE en 1939",
                            "En la OTAN en 2014 y en la UE en 2020"
                        ],
                        "correctIndex": 0,
                        "explanation": "España ingresó en la OTAN en mayo de 1982 (ratificado en referéndum en 1986) y en las Comunidades Europeas el 1 de enero de 1986."
                    },
                    {
                        "question": "¿Cuál de las siguientes listas recoge exclusivamente a presidentes del Gobierno de la España democrática desde la Constitución de 1978?",
                        "options": [
                            "Adolfo Suárez, Leopoldo Calvo-Sotelo, Felipe González, José María Aznar, José Luis Rodríguez Zapatero, Mariano Rajoy y Pedro Sánchez",
                            "Miguel Primo de Rivera, Francisco Franco, Luis Carrero Blanco y Carlos Arias Navarro",
                            "Conde-Duque de Olivares, Duque de Lerma, Floridablanca y Godoy",
                            "Cánovas del Castillo, Sagasta, Maura y Canalejas"
                        ],
                        "correctIndex": 0,
                        "explanation": "Suárez, Calvo-Sotelo, González, Aznar, Zapatero, Rajoy y Sánchez son los siete presidentes del Gobierno de la democracia actual."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Entre qué dos ciudades españolas se inauguró en abril de 1992 la primera línea de tren de Alta Velocidad Española (AVE)?",
                        "options": [
                            "Entre Madrid y Sevilla",
                            "Entre Bilbao y Vigo",
                            "Entre Palma e Ibiza",
                            "Entre Santander y Oviedo"
                        ],
                        "correctIndex": 0,
                        "explanation": "El primer tren AVE unió Madrid y Sevilla en abril de 1992 con motivo de la Expo 92."
                    },
                    {
                        "prompt": "¿Qué ocurrió el 23 de febrero de 1981 (23-F) en el Congreso de los Diputados?",
                        "options": [
                            "Un intento de golpe de Estado militar que fracasó gracias a la defensa de la Constitución y de la democracia",
                            "La aprobación del matrimonio igualitario",
                            "La firma de los Pactos de la Moncloa",
                            "La inauguración del Museo Guggenheim"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 23-F de 1981 fue un intento fallido de golpe de Estado en el Congreso de los Diputados."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En el año 1992 se celebraron los Juegos Olímpicos de ___ y la Exposición Universal de Sevilla.",
                        "answer": "Barcelona",
                        "options": ["Barcelona", "Valencia", "Málaga", "Zaragoza"],
                        "explanation": "Barcelona acogió los Juegos Olímpicos de verano de 1992.",
                        "english": "In the year 1992 the Olympic Games of Barcelona and the Universal Exposition of Seville were held."
                    },
                    {
                        "sentence": "La primera línea del tren de alta velocidad (___) se inauguró en 1992 entre Madrid y Sevilla.",
                        "answer": "AVE",
                        "options": ["AVE", "BOE", "DNI", "INE"],
                        "explanation": "AVE son las siglas de Alta Velocidad Española.",
                        "english": "The first high-speed train (AVE) line was inaugurated in 1992 between Madrid and Seville."
                    }
                ],
                "ex_dict": {
                    "audioText": "En mil novecientos noventa y dos se celebraron los Juegos Olímpicos de Barcelona y la Exposición Universal de Sevilla.",
                    "english": "In nineteen ninety-two the Olympic Games in Barcelona and the Universal Exposition in Seville were held."
                },
                "ex_sb": {
                    "words": ["España", "tiene", "la", "red", "de", "alta", "velocidad", "ferroviaria", "más", "extensa", "de", "Europa."],
                    "english": "Spain has the most extensive high-speed rail network in Europe."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 24: Literatura Española: De Cervantes a la Generación del 27 (unit_num=60, b1-literatura)
    # =========================================================================
    {
        "slug": "literatura",
        "unit_num": 60,
        "title": "Literatura Española: De Cervantes a la Generación del 27",
        "description": "El Cantar de mio Cid y La Celestina, Miguel de Cervantes y el Quijote, el Siglo de Oro, las Generaciones del 98 y del 27 (Lorca y Machado) y los cinco Premios Nobel de Literatura españoles.",
        "Badge": "Literatura Española",
        "lessons": [
            {
                "num": "01",
                "Title": "Orígenes Literarios: El Cantar de mio Cid, La Celestina y el Lazarillo",
                "title": "Orígenes Literarios: El Cantar de mio Cid, La Celestina y el Lazarillo",
                "grammar_slug": "ser-considerado-la-primera-gran-obra-literaria",
                "story_slug": "edadmediayrenacimiento",
                "story_title": "De las hazañas del Cid Campeador al ingenio del pequeño Lázaro de Tormes",
                "objectives": [
                    "Identificar el «Cantar de mio Cid» como el gran poema épico medieval anónimo de la literatura española, protagonizado por Rodrigo Díaz de Vivar.",
                    "Conocer «La Celestina» de Fernando de Rojas (1499), «El Lazarillo de Tormes» (1554, origen de la novela picaresca) y la poesía del Renacimiento (Garcilaso de la Vega, Santa Teresa de Jesús y San Juan de la Cruz).",
                    "Practicar las construcciones «estar protagonizado por» y «inaugurar el género de la novela picaresca»."
                ],
                "vocab": [
                    {"lemma": "el Cantar de mio Cid", "pos": "noun", "translation": "The Lay of the Cid (oldest preserved Spanish epic poem, c. 1200)"},
                    {"lemma": "Rodrigo Díaz de Vivar (el Cid Campeador)", "pos": "noun", "translation": "Rodrigo Díaz de Vivar (11th-century Castilian knight and hero of the epic)"},
                    {"lemma": "el cantar de gesta", "pos": "noun", "translation": "medieval epic poem (chanson de geste)"},
                    {"lemma": "La Celestina (Fernando de Rojas)", "pos": "noun", "translation": "La Celestina (Tragicomedy of Calisto and Melibea, 1499)"},
                    {"lemma": "El Lazarillo de Tormes (1554)", "pos": "noun", "translation": "The Life of Lazarillo de Tormes (anonymous picaresque novel)"},
                    {"lemma": "la novela picaresca", "pos": "noun", "translation": "picaresque novel"},
                    {"lemma": "Santa Teresa de Jesús y San Juan de la Cruz", "pos": "noun", "translation": "Saint Teresa of Ávila and Saint John of the Cross (Renaissance mystic writers)"},
                    {"lemma": "Jorge Manrique", "pos": "noun", "translation": "Jorge Manrique (15th-century poet, author of 'Coplas por la muerte de su padre')"}
                ],
                "grammar_title": "Obras fundacionales: atribución de autoría y género literario",
                "grammar_text": "En la Tarea 4 del CCSE es muy común relacionar las obras clásicas con su género o protagonista: el ***Cantar de mio Cid*** es un **cantar de gesta anónimo** sobre **Rodrigo Díaz de Vivar**; ***La Celestina*** (de **Fernando de Rojas**) narra los amores de **Calisto y Melibea**; y ***El Lazarillo de Tormes*** es la obra anónima que creó la **novela picaresca**.",
                "grammar_examples": [
                    {"es": "El «Cantar de mio Cid» es el cantar de gesta más importante de la literatura medieval española.", "en": "The 'Lay of the Cid' is the most important epic poem of medieval Spanish literature."},
                    {"es": "«El Lazarillo de Tormes», publicado de forma anónima en 1554, inauguró el género de la novela picaresca.", "en": "'Lazarillo de Tormes', published anonymously in 1554, inaugurated the genre of the picaresque novel."}
                ],
                "grammar_tip": "¡Tres relaciones clave para el CCSE! 1) *Cantar de mio Cid* = poema épico medieval sobre Rodrigo Díaz de Vivar. 2) *La Celestina* = Fernando de Rojas (Calisto y Melibea). 3) *El Lazarillo de Tormes* = novela picaresca anónima.",
                "paragraphs": [
                    "La literatura en lengua castellana cuenta con más de ocho siglos de obras maestras ininterrumpidas. Su primer gran monumento conservado es el *Cantar de mio Cid*, un cantar de gesta anónimo compuesto hacia finales del siglo XII o el año 1200 (conservado en un manuscrito copiado por Per Abbat que se custodia en la Biblioteca Nacional de España). El poema narra con extraordinario realismo y humanidad el destierro, las batallas en tierras de Valencia y la recuperación del honor del caballero castellano Rodrigo Díaz de Vivar, conocido como el Cid Campeador.",
                    "A lo largo de la Edad Media florecieron también los *Milagros de Nuestra Señora* de Gonzalo de Berceo (primer poeta de nombre conocido en castellano), *El conde Lucanor* de don Juan Manuel, el *Libro de buen amor* del Arcipreste de Hita y, ya en el siglo XV, las inmortales *Coplas por la muerte de su padre* de Jorge Manrique («Nuestras vidas son los ríos / que van a dar en la mar, / que es el morir»).",
                    "En el año 1499, en la frontera misma entre la Edad Media y el Renacimiento, el jurista toledano Fernando de Rojas publicó *La Celestina* (originalmente titulada *Comedia o Tragicomedia de Calisto y Melibea*), donde una vieja alcahueta astuta e inolvidable interviene en la pasión amorosa de dos jóvenes, creando uno de los retratos psicológicos más modernos de las letras europeas.",
                    "Mediado el siglo XVI, mientras la poesía española se renovaba con el endecasílabo italiano de Garcilaso de la Vega y alcanzaba las cumbres más altas de la espiritualidad mística con Santa Teresa de Jesús (nacida en Ávila) y San Juan de la Cruz, apareció en 1554 un pequeño libro anónimo que revolucionó para siempre el arte de narrar: *La vida de Lazarillo de Tormes y de sus fortunas y adversidades*.",
                    "En *El Lazarillo de Tormes*, un niño humilde nacido a orillas del río Tormes en Salamanca cuenta en primera persona cómo debe servir a varios amos —empezando por un ciego astuto y un clérigo avaro— usando su ingenio para sobrevivir al hambre. Con *El Lazarillo* nació la novela picaresca, semilla directa de la novela moderna que culminaría medio siglo después con Miguel de Cervantes."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es el poema épico o cantar de gesta más antiguo y famoso de la literatura española medieval, que narra las hazañas de Rodrigo Díaz de Vivar?",
                        "options": [
                            "El Cantar de mio Cid",
                            "La Odisea",
                            "El Romancero gitano",
                            "Campos de Castilla"
                        ],
                        "correctIndex": 0,
                        "explanation": "El «Cantar de mio Cid» es el gran cantar de gesta de la Edad Media española sobre Rodrigo Díaz de Vivar."
                    },
                    {
                        "question": "¿Qué obra anónima publicada en 1554 cuenta las peripecias de un muchacho salmantino al servicio de un ciego e inauguró el género de la novela picaresca?",
                        "options": [
                            "El Lazarillo de Tormes",
                            "Platero y yo",
                            "La Regenta",
                            "Fuenteovejuna"
                        ],
                        "correctIndex": 0,
                        "explanation": "«El Lazarillo de Tormes» (1554) es la obra fundacional de la novela picaresca española."
                    },
                    {
                        "question": "¿Quién escribió en 1499 «La Celestina» (Tragicomedia de Calisto y Melibea)?",
                        "options": [
                            "Fernando de Rojas",
                            "Federico García Lorca",
                            "Camilo José Cela",
                            "Pío Baroja"
                        ],
                        "correctIndex": 0,
                        "explanation": "Fernando de Rojas es el autor de «La Celestina»."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cómo se llamaba en la vida real el caballero castellano del siglo XI conocido como «el Cid Campeador»?",
                        "options": [
                            "Rodrigo Díaz de Vivar",
                            "Alonso Quijano",
                            "Gonzalo de Berceo",
                            "Jorge Manrique"
                        ],
                        "correctIndex": 0,
                        "explanation": "Rodrigo Díaz de Vivar (nacido en Vivar, Burgos) fue el Cid Campeador."
                    },
                    {
                        "prompt": "¿Qué dos grandes escritores del siglo XVI son los máximos representantes de la literatura mística española del Renacimiento?",
                        "options": [
                            "Santa Teresa de Jesús y San Juan de la Cruz",
                            "Benito Pérez Galdós y Clarín",
                            "Azorín y Valle-Inclán",
                            "Rafael Alberti y Luis Cernuda"
                        ],
                        "correctIndex": 0,
                        "explanation": "Santa Teresa de Jesús y San Juan de la Cruz representan la cumbre de la mística española."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El «Cantar de mio ___» es el poema épico medieval que narra la vida de Rodrigo Díaz de Vivar.",
                        "answer": "Cid",
                        "options": ["Cid", "Tormes", "Duero", "Lazarillo"],
                        "explanation": "El «Cantar de mio Cid» es el cantar de gesta más famoso de la literatura española.",
                        "english": "The 'Lay of the Cid' is the medieval epic poem that narrates the life of Rodrigo Díaz de Vivar."
                    },
                    {
                        "sentence": "«El ___ de Tormes» es una novela anónima del siglo XVI que dio origen a la novela picaresca.",
                        "answer": "Lazarillo",
                        "options": ["Lazarillo", "Caballero", "Alcalde", "Buscón"],
                        "explanation": "«El Lazarillo de Tormes» se publicó en 1554.",
                        "english": "'Lazarillo de Tormes' is an anonymous 16th-century novel that gave rise to the picaresque novel."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Cantar de mio Cid es un poema épico medieval y El Lazarillo de Tormes es una novela picaresca.",
                    "english": "The Lay of the Cid is a medieval epic poem and Lazarillo de Tormes is a picaresque novel."
                },
                "ex_sb": {
                    "words": ["Fernando", "de", "Rojas", "escribió", "La", "Celestina", "a", "finales", "del", "siglo", "quince."],
                    "english": "Fernando de Rojas wrote La Celestina at the end of the fifteenth century."
                }
            },
            {
                "num": "02",
                "Title": "Miguel de Cervantes, el Quijote y el Teatro del Siglo de Oro",
                "title": "Miguel de Cervantes, el Quijote y el Teatro del Siglo de Oro",
                "grammar_slug": "publicarse-en-dos-partes-y-crear-la-novela-moderna",
                "story_slug": "cervantesysiglodeoro",
                "story_title": "En un lugar de la Mancha: Cervantes, don Quijote y los corrales de comedias",
                "objectives": [
                    "Dominar todos los datos clave sobre Miguel de Cervantes Saavedra (nacido en Alcalá de Henares en 1547, fallecido en Madrid en abril de 1616) y su obra «El ingenioso hidalgo don Quijote de la Mancha» (publicada en 1605 y 1615).",
                    "Identificar a los personajes principales del Quijote (Alonso Quijano / don Quijote, Sancho Panza, Dulcinea del Toboso y el caballo Rocinante) y a los grandes autores del Siglo de Oro: Lope de Vega («Fuenteovejuna»), Calderón de la Barca («La vida es sueño»), Quevedo y Góngora.",
                    "Practicar las construcciones «ser considerada la primera novela moderna» y «protagonizar junto a su escudero Sancho Panza»."
                ],
                "vocab": [
                    {"lemma": "Miguel de Cervantes Saavedra (1547–1616)", "pos": "noun", "translation": "Miguel de Cervantes (author of Don Quixote, born in Alcalá de Henares)"},
                    {"lemma": "El ingenioso hidalgo don Quijote de la Mancha (1605 y 1615)", "pos": "noun", "translation": "Don Quixote (considered the first modern novel in world literature)"},
                    {"lemma": "Alonso Quijano y Sancho Panza", "pos": "noun", "translation": "Alonso Quijano (Don Quixote) and his squire Sancho Panza"},
                    {"lemma": "Dulcinea del Toboso / Rocinante", "pos": "noun", "translation": "Dulcinea del Toboso (lady idealized by Don Quixote) / Rocinante (his horse)"},
                    {"lemma": "Lope de Vega («Fuenteovejuna», «El perro del hortelano»)", "pos": "noun", "translation": "Lope de Vega (great Golden Age playwright, 'Fénix de los Ingenios')"},
                    {"lemma": "Pedro Calderón de la Barca («La vida es sueño»)", "pos": "noun", "translation": "Pedro Calderón de la Barca (Baroque playwright, author of 'Life Is a Dream')"},
                    {"lemma": "Francisco de Quevedo y Luis de Góngora", "pos": "noun", "translation": "Quevedo and Góngora (great poets of the Spanish Baroque)"},
                    {"lemma": "el Día Internacional del Libro (23 de abril)", "pos": "noun", "translation": "World Book Day (commemorating the death of Cervantes and Shakespeare in April 1616)"}
                ],
                "grammar_title": "El centro del canon hispánico: Cervantes, el Quijote y el teatro barroco",
                "grammar_text": "La obra cumbre de la lengua española es ***El ingenioso hidalgo don Quijote de la Mancha***, escrita por **Miguel de Cervantes** (nacido en **Alcalá de Henares**) y publicada en dos partes (**1605 y 1615**). Junto a Cervantes brillan en el teatro del Siglo de Oro **Lope de Vega** (autor de ***Fuenteovejuna***) y **Pedro Calderón de la Barca** (autor de ***La vida es sueño*** y ***El alcalde de Zalamea***).",
                "grammar_examples": [
                    {"es": "Miguel de Cervantes nació en Alcalá de Henares y publicó la primera parte del Quijote en el año 1605.", "en": "Miguel de Cervantes was born in Alcalá de Henares and published the first part of Don Quixote in the year 1605."},
                    {"es": "En «La vida es sueño», obra teatral de Calderón de la Barca, el príncipe Segismundo reflexiona sobre la libertad.", "en": "In 'Life Is a Dream', a play by Calderón de la Barca, Prince Segismundo reflects on freedom."}
                ],
                "grammar_tip": "¡Preguntas imprescindibles del CCSE! 1) ¿Dónde nació Miguel de Cervantes? En **Alcalá de Henares (Madrid)**. 2) ¿Quiénes son los protagonistas del *Quijote*? **Don Quijote (Alonso Quijano) y su escudero Sancho Panza**. 3) ¿Por qué se celebra el **Día del Libro el 23 de abril**? En conmemoración del fallecimiento de Miguel de Cervantes (y de Shakespeare y el Inca Garcilaso) en abril de 1616.",
                "paragraphs": [
                    "«En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor...». Con estas palabras inmortales se abre *El ingenioso hidalgo don Quijote de la Mancha*, obra maestra de Miguel de Cervantes Saavedra y libro más traducido y editado de la historia universal después de la Biblia.",
                    "Miguel de Cervantes nació en Alcalá de Henares (Comunidad de Madrid) en 1547. Su vida fue tan novelesca como su literatura: luchó como soldado en la batalla naval de Lepanto (1571), donde perdió el movimiento de la mano izquierda (de ahí su sobrenombre de «el Manco de Lepanto»), sufrió cinco años de cautiverio en Argel y recorrió Andalucía como recaudador de provisiones antes de publicar en 1605 la primera parte del *Quijote* y en 1615 la segunda parte, además de las *Novelas ejemplares* y el *Persiles*. Falleció en Madrid en abril de 1616; por esa fecha (23 de abril de 1616, coincidiendo con la muerte de William Shakespeare y del Inca Garcilaso de la Vega) se celebra cada 23 de abril el Día Internacional del Libro y se entrega el Premio Cervantes en la Universidad de Alcalá de Henares.",
                    "En el *Quijote*, el hidalgo manchego Alonso Quijano enloquece de tanto leer libros de caballerías y sale a recorrer los caminos de La Mancha, Aragón y Barcelona sobre su caballo *Rocinante* para defender a los débiles, acompañado por su leal y sensato vecino, el escudero Sancho Panza (montado en su rucio), y dedicando todas sus aventuras a una dama imaginaria: Dulcinea del Toboso. Del diálogo constante entre el idealismo de don Quijote y el sentido práctico de Sancho nació para siempre la novela moderna.",
                    "Aquel mismo Siglo de Oro (siglos XVI y XVII) vio florecer en los «corrales de comedias» uno de los teatros más vibrantes de la historia universal. Su gran creador fue Lope de Vega (1562–1635), llamado el «Fénix de los Ingenios», autor de centenares de comedias en verso como *Fuenteovejuna*, *El caballero de Olmedo*, *La dama boba* y *El perro del hortelano*.",
                    "Junto a Lope brillaron Tirso de Molina (creador del mito universal de don Juan en *El burlador de Sevilla*) y el gran dramaturgo filosófico del Barroco, Pedro Calderón de la Barca (1600–1681), autor de *El alcalde de Zalamea* y de *La vida es sueño* («¿Qué es la vida? Un frenesí. ¿Qué es la vida? Una ilusión, una sombra, una ficción...»), mientras que en la poesía lírica rivalizaban dos titanes inigualables: el cordobés Luis de Góngora y el madrileño Francisco de Quevedo."
                ],
                "questions": [
                    {
                        "question": "¿Quién es el autor de «El ingenioso hidalgo don Quijote de la Mancha» y en qué ciudad de la Comunidad de Madrid nació?",
                        "options": [
                            "Miguel de Cervantes, nacido en Alcalá de Henares",
                            "Lope de Vega, nacido en Sevilla",
                            "Calderón de la Barca, nacido en Valencia",
                            "Francisco de Quevedo, nacido en Bilbao"
                        ],
                        "correctIndex": 0,
                        "explanation": "Miguel de Cervantes Saavedra (1547–1616) nació en Alcalá de Henares y es el autor de «Don Quijote de la Mancha»."
                    },
                    {
                        "question": "¿Cómo se llama el fiel escudero que acompaña a don Quijote en sus aventuras y cómo se llama la dama a la que don Quijote dedica sus hazañas?",
                        "options": [
                            "El escudero es Sancho Panza y la dama es Dulcinea del Toboso",
                            "El escudero es Calisto y la dama es Melibea",
                            "El escudero es Segismundo y la dama es Laurencia",
                            "El escudero es Lázaro y la dama es Celestina"
                        ],
                        "correctIndex": 0,
                        "explanation": "Sancho Panza es el escudero de don Quijote y Dulcinea del Toboso es su dama idealizada."
                    },
                    {
                        "question": "¿Qué dramaturgo del Siglo de Oro español escribió la famosa obra teatral filosófica «La vida es sueño»?",
                        "options": [
                            "Pedro Calderón de la Barca",
                            "Miguel de Unamuno",
                            "Jacinto Benavente",
                            "Leopoldo Alas «Clarín»"
                        ],
                        "correctIndex": 0,
                        "explanation": "Pedro Calderón de la Barca (1600–1681) es el autor de «La vida es sueño» y «El alcalde de Zalamea»."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Por qué se celebra cada año el Día Internacional del Libro el 23 de abril?",
                        "options": [
                            "En conmemoración del fallecimiento de Miguel de Cervantes (y de Shakespeare) en abril de 1616",
                            "Porque ese día se inauguró la primera línea del AVE",
                            "Porque ese día se aprobó la Constitución de 1978",
                            "Porque ese día terminan las Fallas de Valencia"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 23 de abril conmemora la muerte en abril de 1616 de Miguel de Cervantes, William Shakespeare y el Inca Garcilaso de la Vega."
                    },
                    {
                        "prompt": "¿Qué autor teatral del Siglo de Oro escribió «Fuenteovejuna» y «El perro del hortelano»?",
                        "options": [
                            "Lope de Vega",
                            "Antonio Machado",
                            "Gustavo Adolfo Bécquer",
                            "Camilo José Cela"
                        ],
                        "correctIndex": 0,
                        "explanation": "Félix Lope de Vega y Carpio escribió «Fuenteovejuna» y «El perro del hortelano»."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Miguel de ___ es el autor de «Don Quijote de la Mancha», la obra cumbre de la literatura en español.",
                        "answer": "Cervantes",
                        "options": ["Cervantes", "Quevedo", "Góngora", "Bécquer"],
                        "explanation": "Miguel de Cervantes publicó el Quijote en dos partes (1605 y 1615).",
                        "english": "Miguel de Cervantes is the author of 'Don Quixote of La Mancha', the masterpiece of literature in Spanish."
                    },
                    {
                        "sentence": "En sus aventuras por La Mancha, don Quijote va siempre acompañado de su fiel escudero ___ Panza.",
                        "answer": "Sancho",
                        "options": ["Sancho", "Rodrigo", "Lázaro", "Calisto"],
                        "explanation": "Sancho Panza es el inseparable escudero de don Quijote.",
                        "english": "In his adventures through La Mancha, Don Quixote is always accompanied by his faithful squire Sancho Panza."
                    }
                ],
                "ex_dict": {
                    "audioText": "Miguel de Cervantes nació en Alcalá de Henares y escribió El ingenioso hidalgo don Quijote de la Mancha.",
                    "english": "Miguel de Cervantes was born in Alcalá de Henares and wrote The Ingenious Gentleman Don Quixote of La Mancha."
                },
                "ex_sb": {
                    "words": ["Cada", "veintitrés", "de", "abril", "se", "celebra", "el", "Día", "Internacional", "del", "Libro."],
                    "english": "Every twenty-third of April, World Book Day is celebrated."
                }
            },
            {
                "num": "03",
                "Title": "Romanticismo y Realismo: Bécquer, Rosalía, Galdós y Clarín",
                "title": "Romanticismo y Realismo: Bécquer, Rosalía, Galdós y Clarín",
                "grammar_slug": "retratar-la-sociedad-espanola-del-siglo-diecinueve",
                "story_slug": "sigloxix",
                "story_title": "De las «Rimas» de Bécquer y Rosalía de Castro a las novelas de Galdós y «La Regenta»",
                "objectives": [
                    "Conocer a los grandes poetas del Romanticismo y Posromanticismo español del siglo XIX: José de Espronceda, José Zorrilla («Don Juan Tenorio»), Gustavo Adolfo Bécquer («Rimas y Leyendas») y la gallega Rosalía de Castro («Cantares gallegos»).",
                    "Identificar a los maestros de la novela realista y naturalista de la segunda mitad del siglo XIX: Benito Pérez Galdós («Fortunata y Jacinta» y los «Episodios Nacionales»), Leopoldo Alas «Clarín» («La Regenta») y Emilia Pardo Bazán («Los pazos de Ulloa»).",
                    "Practicar las construcciones «ser el máximo exponente del realismo» y «retratar la sociedad del siglo XIX»."
                ],
                "vocab": [
                    {"lemma": "Gustavo Adolfo Bécquer («Rimas y Leyendas»)", "pos": "noun", "translation": "Gustavo Adolfo Bécquer (19th-century Romantic poet from Seville)"},
                    {"lemma": "Rosalía de Castro («Cantares gallegos», «Follas novas»)", "pos": "noun", "translation": "Rosalía de Castro (great 19th-century Galician and Spanish poet)"},
                    {"lemma": "Benito Pérez Galdós («Fortunata y Jacinta», «Episodios Nacionales»)", "pos": "noun", "translation": "Benito Pérez Galdós (greatest 19th-century Spanish realist novelist)"},
                    {"lemma": "Leopoldo Alas «Clarín» («La Regenta»)", "pos": "noun", "translation": "Leopoldo Alas 'Clarín' (author of the masterpiece novel 'La Regenta')"},
                    {"lemma": "Emilia Pardo Bazán («Los pazos de Ulloa»)", "pos": "noun", "translation": "Emilia Pardo Bazán (pioneer novelist and feminist intellectual from A Coruña)"},
                    {"lemma": "José Zorrilla («Don Juan Tenorio»)", "pos": "noun", "translation": "José Zorrilla (Romantic playwright, author of 'Don Juan Tenorio')"},
                    {"lemma": "Mariano José de Larra («Vuelva usted mañana»)", "pos": "noun", "translation": "Mariano José de Larra (pioneer of Romantic journalism)"},
                    {"lemma": "la novela realista", "pos": "noun", "translation": "realist novel"}
                ],
                "grammar_title": "El siglo XIX literario: la lírica de Bécquer y Rosalía y la gran novela de Galdós y Clarín",
                "grammar_text": "En la literatura española del **siglo XIX** destacan dos grandes movimientos: el **Romanticismo** —con los poetas **Gustavo Adolfo Bécquer** (autor de las ***Rimas y Leyendas***) y **Rosalía de Castro**, además de **José Zorrilla** (*Don Juan Tenorio*)— y el **Realismo** —con los grandes novelistas **Benito Pérez Galdós** (*Fortunata y Jacinta* y *Episodios Nacionales*), **Leopoldo Alas «Clarín»** (*La Regenta*) y **Emilia Pardo Bazán** (*Los pazos de Ulloa*)—.",
                "grammar_examples": [
                    {"es": "Gustavo Adolfo Bécquer es el autor de las famosas «Rimas y Leyendas» del siglo XIX.", "en": "Gustavo Adolfo Bécquer is the author of the famous 19th-century 'Rhymes and Legends'."},
                    {"es": "Benito Pérez Galdós, nacido en Las Palmas de Gran Canaria, escribió «Fortunata y Jacinta» y los «Episodios Nacionales».", "en": "Benito Pérez Galdós, born in Las Palmas de Gran Canaria, wrote 'Fortunata and Jacinta' and the 'National Episodes'."}
                ],
                "grammar_tip": "Relaciones clave del siglo XIX para el CCSE: Bécquer = *Rimas y Leyendas*; Rosalía de Castro = *Cantares gallegos* (renacimiento literario de Galicia); Pérez Galdós = *Episodios Nacionales* y *Fortunata y Jacinta*; Clarín = *La Regenta*.",
                "paragraphs": [
                    "Durante la primera mitad del siglo XIX, el Romanticismo trajo a las letras españolas la pasión por la libertad individual, el misterio y el sentimiento íntimo. En el periodismo brillaron los artículos satíricos de Mariano José de Larra (como *Vuelva usted mañana*); en la poesía exaltada destacó José de Espronceda (*La canción del pirata*); y en los teatros triunfó *Don Juan Tenorio* (1844), de José Zorrilla.",
                    "Sin embargo, la verdadera voz poética moderna nació hacia la década de 1860 con dos figuras inolvidables del posromanticismo. El primero fue el sevillano Gustavo Adolfo Bécquer (1836–1870), cuyas breves y musicales *Rimas* («¿Qué es poesía?, dices mientras clavas / en mi pupila tu pupila azul...» o «Volverán las oscuras golondrinas») y sus misteriosas *Leyendas* abrieron el camino a toda la poesía española del siglo XX.",
                    "La segunda gran voz fue la escritora gallega Rosalía de Castro (1837–1885), nacida en Santiago de Compostela. Con libros fundamentales en lengua gallega como *Cantares gallegos* (1863, cuya fecha de publicación, el 17 de mayo, conmemora hoy el Día das Letras Galegas) y *Follas novas*, y en castellano como *En las orillas del Sar*, Rosalía lideró el *Rexurdimento* cultural de Galicia y dio voz al dolor de los emigrantes y de las mujeres.",
                    "En el último tercio del siglo XIX, la literatura española vivió una segunda edad de oro gracias a la novela realista y naturalista. Su figura central fue Benito Pérez Galdós (1843–1920), nacido en Las Palmas de Gran Canaria y afincado en Madrid, considerado el mayor novelista español después de Cervantes: Galdós retrató todas las capas sociales de Madrid en obras maestras como *Fortunata y Jacinta*, *Doña Perfecta* y *Misericordia*, y narró toda la historia del siglo XIX español en las cuarenta y seis novelas de sus *Episodios Nacionales*.",
                    "Junto a Galdós brillaron con luz propia Leopoldo Alas «Clarín» (1852–1901), catedrático de la Universidad de Oviedo y autor de *La Regenta* (ambientada en la ciudad imaginaria de Vetusta, trasunto de Oviedo, una de las grandes novelas europeas del siglo XIX), y la coruñesa Emilia Pardo Bazán (1851–1921), autora de *Los pazos de Ulloa*, primera mujer catedrática universitaria y pionera en la defensa de los derechos educativos de las mujeres en España."
                ],
                "questions": [
                    {
                        "question": "¿Quién es el gran novelista canario del realismo español del siglo XIX, autor de «Fortunata y Jacinta» y de los cuarenta y seis «Episodios Nacionales»?",
                        "options": [
                            "Benito Pérez Galdós",
                            "Luis de Góngora",
                            "Tirso de Molina",
                            "Vicente Aleixandre"
                        ],
                        "correctIndex": 0,
                        "explanation": "Benito Pérez Galdós (1843–1920), nacido en Las Palmas de Gran Canaria, es el autor de «Fortunata y Jacinta» y los «Episodios Nacionales»."
                    },
                    {
                        "question": "¿Qué poeta sevillano del siglo XIX escribió el famoso libro de poemas y relatos «Rimas y Leyendas»?",
                        "options": [
                            "Gustavo Adolfo Bécquer",
                            "Jorge Manrique",
                            "Garcilaso de la Vega",
                            "Camilo José Cela"
                        ],
                        "correctIndex": 0,
                        "explanation": "Gustavo Adolfo Bécquer es el autor de las célebres «Rimas y Leyendas»."
                    },
                    {
                        "question": "¿Qué escritora nacida en Santiago de Compostela es la gran figura literaria de Galicia en el siglo XIX, autora de «Cantares gallegos», «Follas novas» y «En las orillas del Sar»?",
                        "options": [
                            "Rosalía de Castro",
                            "Clara Campoamor",
                            "María Zambrano",
                            "Santa Teresa de Jesús"
                        ],
                        "correctIndex": 0,
                        "explanation": "Rosalía de Castro (1837–1885) es el símbolo de la literatura gallega y una de las grandes poetas del siglo XIX español."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Quién escribió la gran novela realista del siglo XIX «La Regenta», ambientada en la ciudad de Vetusta (Oviedo)?",
                        "options": [
                            "Leopoldo Alas «Clarín»",
                            "Fernando de Rojas",
                            "Miguel Hernández",
                            "Pío Baroja"
                        ],
                        "correctIndex": 0,
                        "explanation": "Leopoldo Alas «Clarín» publicó «La Regenta» entre 1884 y 1885."
                    },
                    {
                        "prompt": "¿Qué escritora gallega nacida en A Coruña escribió la novela «Los pazos de Ulloa» y fue una pionera en la defensa de la educación de la mujer?",
                        "options": [
                            "Emilia Pardo Bazán",
                            "Almudena Grandes",
                            "Carmen Laforet",
                            "Rosa Chacel"
                        ],
                        "correctIndex": 0,
                        "explanation": "Emilia Pardo Bazán (1851–1921) escribió «Los pazos de Ulloa» y fue la primera mujer catedrática en la Universidad Central."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Benito Pérez ___ es el autor de «Fortunata y Jacinta» y de los «Episodios Nacionales».",
                        "answer": "Galdós",
                        "options": ["Galdós", "Bécquer", "Zorrilla", "Larra"],
                        "explanation": "Benito Pérez Galdós es el máximo representante de la novela realista española del siglo XIX.",
                        "english": "Benito Pérez Galdós is the author of 'Fortunata and Jacinta' and of the 'National Episodes'."
                    },
                    {
                        "sentence": "El poeta sevillano Gustavo Adolfo ___ escribió las famosas «Rimas y Leyendas».",
                        "answer": "Bécquer",
                        "options": ["Bécquer", "Clarín", "Machado", "Lorca"],
                        "explanation": "Gustavo Adolfo Bécquer es el autor de las «Rimas y Leyendas».",
                        "english": "The Sevillian poet Gustavo Adolfo Bécquer wrote the famous 'Rhymes and Legends'."
                    }
                ],
                "ex_dict": {
                    "audioText": "Benito Pérez Galdós escribió Fortunata y Jacinta y Leopoldo Alas Clarín escribió La Regenta.",
                    "english": "Benito Pérez Galdós wrote Fortunata and Jacinta and Leopoldo Alas Clarín wrote La Regenta."
                },
                "ex_sb": {
                    "words": ["Rosalía", "de", "Castro", "es", "la", "gran", "poeta", "de", "Galicia", "del", "siglo", "diecinueve."],
                    "english": "Rosalía de Castro is the great poet of Galicia of the nineteenth century."
                }
            },
            {
                "num": "04",
                "Title": "La Edad de Plata: Generación del 98 y Generación del 27",
                "title": "La Edad de Plata: Generación del 98 y Generación del 27",
                "grammar_slug": "pertenecer-a-la-generacion-del-noventa-y-ocho-y-del-veintisiete",
                "story_slug": "generacion98y27",
                "story_title": "Caminante, no hay camino: de Antonio Machado y Unamuno a Federico García Lorca",
                "objectives": [
                    "Distinguir a los grandes autores de la Generación del 98: Miguel de Unamuno («Niebla»), Pío Baroja («El árbol de la ciencia»), Ramón María del Valle-Inclán («Luces de bohemia»), Azorín y el poeta Antonio Machado («Campos de Castilla»).",
                    "Identificar a los miembros de la Generación del 27 encabezada por Federico García Lorca («Romancero gitano», «Bodas de sangre», «La casa de Bernarda Alba»), junto a Rafael Alberti, Pedro Salinas, Luis Cernuda, Vicente Aleixandre, Miguel Hernández y las pensadoras y artistas «Las Sinsombrero» (María Zambrano, Maruja Mallo).",
                    "Practicar las expresiones «pertenecer a la Generación del 98 / del 27»."
                ],
                "vocab": [
                    {"lemma": "Antonio Machado («Campos de Castilla»)", "pos": "noun", "translation": "Antonio Machado (great poet of the Generation of '98, 'Caminante, no hay camino')"},
                    {"lemma": "Miguel de Unamuno («Niebla») y Pío Baroja («El árbol de la ciencia»)", "pos": "noun", "translation": "Unamuno and Baroja (leading Basque novelists and thinkers of the Generation of '98)"},
                    {"lemma": "Ramón María del Valle-Inclán («Luces de bohemia», el esperpento)", "pos": "noun", "translation": "Valle-Inclán (Galician playwright and novelist, creator of 'esperpento')"},
                    {"lemma": "la Generación del 27", "pos": "noun", "translation": "Generation of '27 (group of poets gathered in 1927 for the tricentenary of Góngora)"},
                    {"lemma": "Federico García Lorca (1898–1936)", "pos": "noun", "translation": "Federico García Lorca (poet and playwright from Granada, 'Romancero gitano', 'La casa de Bernarda Alba')"},
                    {"lemma": "Rafael Alberti / Luis Cernuda / Pedro Salinas", "pos": "noun", "translation": "Alberti, Cernuda, and Salinas (poets of the Generation of '27)"},
                    {"lemma": "María Zambrano y Las Sinsombrero", "pos": "noun", "translation": "María Zambrano (philosopher, first woman to win the Cervantes Prize) and the women of '27"},
                    {"lemma": "la Residencia de Estudiantes de Madrid", "pos": "noun", "translation": "Student Residence of Madrid (cultural hub where Lorca, Dalí, and Buñuel met)"}
                ],
                "grammar_title": "Las dos grandes generaciones del siglo XX: el 98 y el 27",
                "grammar_text": "El primer tercio del siglo XX se conoce como **«la Edad de Plata de la cultura española»** y se articula en torno a dos grupos literarios muy preguntados en el CCSE: la **Generación del 98** (**Unamuno, Baroja, Valle-Inclán, Azorín y Antonio Machado**) y la **Generación del 27** (**Federico García Lorca, Rafael Alberti, Vicente Aleixandre, Pedro Salinas, Luis Cernuda, Jorge Guillén, Dámaso Alonso y Gerardo Diego**, junto a **Las Sinsombrero**).",
                "grammar_examples": [
                    {"es": "Antonio Machado, autor de «Campos de Castilla», y Miguel de Unamuno pertenecen a la Generación del 98.", "en": "Antonio Machado, author of 'Fields of Castile', and Miguel de Unamuno belong to the Generation of '98."},
                    {"es": "El poeta y dramaturgo granadino Federico García Lorca es la figura más universal de la Generación del 27.", "en": "The Granadan poet and playwright Federico García Lorca is the most universal figure of the Generation of '27."}
                ],
                "grammar_tip": "¡No confundas las dos generaciones en el CCSE! **Generación del 98** = Antonio Machado, Miguel de Unamuno, Pío Baroja, Valle-Inclán, Azorín. **Generación del 27** = Federico García Lorca (*La casa de Bernarda Alba*, *Bodas de sangre*, *Romancero gitano*), Rafael Alberti, Vicente Aleixandre.",
                "paragraphs": [
                    "Entre 1898 y 1936, España vivió un florecimiento intelectual, científico y literario tan intenso que los historiadores lo denominan «la Edad de Plata de la cultura española», solo comparable al Siglo de Oro. Su primera gran promoción fue la Generación del 98, nacida de la reflexión sobre la identidad y los problemas de España tras la pérdida de las últimas colonias ultramarinas en 1898.",
                    "A la Generación del 98 pertenecieron gigantes del pensamiento y de la novela como el bilbaíno Miguel de Unamuno (rector de la Universidad de Salamanca y autor de *Niebla* y *San Manuel Bueno, mártir*), el donostiarra Pío Baroja (*El árbol de la ciencia*), el alicantino Azorín y el gallego Ramón María del Valle-Inclán (creador de la estética deformante del «esperpento» en su obra teatral *Luces de bohemia*). Su gran voz poética fue el sevillano Antonio Machado (1875–1939), autor de *Soledades* y de *Campos de Castilla* (donde escribió los célebres versos: «Caminante, son tus huellas / el camino y nada más; / caminante, no hay camino, / se hace camino al andar»).",
                    "Tres décadas más tarde, en diciembre de 1927, un grupo de jóvenes poetas se reunió en el Ateneo de Sevilla para conmemorar el tercer centenario de la muerte del poeta barroco Luis de Góngora. Nacía así la Generación del 27, que supo unir la vanguardia europea más audaz con la canción popular tradicional española. En la legendaria Residencia de Estudiantes de Madrid coincidieron como amigos inseparables tres jóvenes que cambiarían el arte del siglo XX: el poeta Federico García Lorca, el pintor Salvador Dalí y el cineasta Luis Buñuel.",
                    "El granadino Federico García Lorca (1898–1936) se convirtió en el poeta y dramaturgo español más leído y representado del siglo XX. En poesía deslumbró con el *Romancero gitano* y *Poeta en Nueva York*, y en teatro creó una trilogía trágica protagonizada por mujeres que luchan por su libertad frente a las normas opresivas: *Bodas de sangre*, *Yerma* y *La casa de Bernarda Alba*.",
                    "Junto a Lorca integraron la Generación del 27 poetas extraordinarios como el gaditano Rafael Alberti (*Marinero en tierra*), Vicente Aleixandre, Pedro Salinas, Jorge Guillén, Luis Cernuda, Gerardo Diego, Dámaso Alonso y su «epígono» alicantino Miguel Hernández (*Viento del pueblo*, *Nanas de la cebolla*), además de las brillantes escritoras, filósofas y artistas conocidas como «Las Sinsombrero» —entre ellas la filósofa malagueña María Zambrano (primera mujer galardonada con el Premio Cervantes en 1988), Rosa Chacel, Ernestina de Champourcin y la pintora Maruja Mallo—."
                ],
                "questions": [
                    {
                        "question": "¿Qué poeta y dramaturgo granadino de la Generación del 27 escribió el «Romancero gitano» y obras teatrales como «Bodas de sangre», «Yerma» y «La casa de Bernarda Alba»?",
                        "options": [
                            "Federico García Lorca",
                            "Benito Pérez Galdós",
                            "Fernando de Rojas",
                            "José Echegaray"
                        ],
                        "correctIndex": 0,
                        "explanation": "Federico García Lorca (1898–1936) es el gran poeta y dramaturgo de la Generación del 27."
                    },
                    {
                        "question": "¿A qué generación literaria pertenecen Miguel de Unamuno, Pío Baroja, Ramón María del Valle-Inclán, Azorín y el poeta Antonio Machado?",
                        "options": [
                            "A la Generación del 98",
                            "Al Romanticismo del siglo XVIII",
                            "A la Escuela de Traductores de Toledo",
                            "Al Mester de Clerecía"
                        ],
                        "correctIndex": 0,
                        "explanation": "Unamuno, Baroja, Valle-Inclán, Azorín y Antonio Machado forman el núcleo de la Generación del 98."
                    },
                    {
                        "question": "¿Quién es el autor del libro de poemas «Campos de Castilla» y de los famosos versos «Caminante, no hay camino, se hace camino al andar»?",
                        "options": [
                            "Antonio Machado",
                            "Lope de Vega",
                            "Camilo José Cela",
                            "Leopoldo Alas «Clarín»"
                        ],
                        "correctIndex": 0,
                        "explanation": "Antonio Machado (1875–1939) publicó «Campos de Castilla» en 1912."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué tres grandes creadores españoles del siglo XX —un poeta, un pintor y un director de cine— entablaron amistad en la Residencia de Estudiantes de Madrid en los años veinte?",
                        "options": [
                            "Federico García Lorca, Salvador Dalí y Luis Buñuel",
                            "Miguel de Cervantes, Diego Velázquez y Calderón de la Barca",
                            "Francisco de Goya, Gustavo Adolfo Bécquer y José Zorrilla",
                            "Pío Baroja, Joaquín Sorolla y Santiago Calatrava"
                        ],
                        "correctIndex": 0,
                        "explanation": "Lorca, Dalí y Buñuel convivieron y colaboraron en la Residencia de Estudiantes de Madrid."
                    },
                    {
                        "prompt": "¿Qué filósofa malagueña vinculada a la Generación del 27 y a «Las Sinsombrero» se convirtió en 1988 en la primera mujer galardonada con el Premio Miguel de Cervantes?",
                        "options": [
                            "María Zambrano",
                            "Concepción Arenal",
                            "Margarita Xirgu",
                            "Sara Montiel"
                        ],
                        "correctIndex": 0,
                        "explanation": "La filósofa y ensayista María Zambrano (1904–1991) recibió el Premio Príncipe de Asturias en 1981 y el Premio Cervantes en 1988."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Federico García ___ es el autor de «La casa de Bernarda Alba» y figura clave de la Generación del 27.",
                        "answer": "Lorca",
                        "options": ["Lorca", "Machado", "Unamuno", "Baroja"],
                        "explanation": "Federico García Lorca escribió «La casa de Bernarda Alba», «Bodas de sangre» y «Yerma».",
                        "english": "Federico García Lorca is the author of 'The House of Bernarda Alba' and a key figure of the Generation of '27."
                    },
                    {
                        "sentence": "El poeta Antonio ___ escribió el libro «Campos de Castilla» y pertenece a la Generación del 98.",
                        "answer": "Machado",
                        "options": ["Machado", "Alberti", "Cernuda", "Salinas"],
                        "explanation": "Antonio Machado es el gran poeta de la Generación del 98.",
                        "english": "The poet Antonio Machado wrote the book 'Fields of Castile' and belongs to the Generation of '98."
                    }
                ],
                "ex_dict": {
                    "audioText": "Antonio Machado pertenece a la Generación del noventa y ocho y Federico García Lorca a la del veintisiete.",
                    "english": "Antonio Machado belongs to the Generation of ninety-eight and Federico García Lorca to that of twenty-seven."
                },
                "ex_sb": {
                    "words": ["Federico", "García", "Lorca", "escribió", "La", "casa", "de", "Bernarda", "Alba", "y", "Bodas", "de", "sangre."],
                    "english": "Federico García Lorca wrote The House of Bernarda Alba and Blood Wedding."
                }
            },
            {
                "num": "05",
                "Title": "Los Premios Nobel de Literatura Españoles y el Premio Cervantes",
                "title": "Los Premios Nobel de Literatura Españoles y el Premio Cervantes",
                "grammar_slug": "ser-galardonado-con-el-premio-nobel-de-literatura",
                "story_slug": "premiosnobel",
                "story_title": "De «Platero y yo» y «La colmena» a la entrega del Premio Cervantes en Alcalá",
                "objectives": [
                    "Memorizar a los cinco escritores nacidos en España galardonados con el Premio Nobel de Literatura: José Echegaray (1904), Jacinto Benavente (1922), Juan Ramón Jiménez (1956, autor de «Platero y yo»), Vicente Aleixandre (1977) y Camilo José Cela (1989, autor de «La colmena» y «La familia de Pascual Duarte»), además del hispano-peruano Mario Vargas Llosa (2010).",
                    "Conocer el Premio Miguel de Cervantes (el galardón más importante de las letras en lengua española, entregado cada 23 de abril en la Universidad de Alcalá de Henares) y el Premio Planeta.",
                    "Practicar la construcción pasiva «ser galardonado con el Premio Nobel de Literatura»."
                ],
                "vocab": [
                    {"lemma": "el Premio Nobel de Literatura", "pos": "noun", "translation": "Nobel Prize in Literature"},
                    {"lemma": "Juan Ramón Jiménez (Nobel 1956, «Platero y yo»)", "pos": "noun", "translation": "Juan Ramón Jiménez (Andalusian poet from Moguer, 1956 Nobel laureate)"},
                    {"lemma": "Vicente Aleixandre (Nobel 1977)", "pos": "noun", "translation": "Vicente Aleixandre (Generation of '27 poet, 1977 Nobel laureate)"},
                    {"lemma": "Camilo José Cela (Nobel 1989, «La colmena», «La familia de Pascual Duarte»)", "pos": "noun", "translation": "Camilo José Cela (Galician novelist, 1989 Nobel laureate)"},
                    {"lemma": "José Echegaray (1904) y Jacinto Benavente (1922)", "pos": "noun", "translation": "Echegaray and Benavente (the first two Spanish Nobel laureates in Literature)"},
                    {"lemma": "Mario Vargas Llosa (Nobel 2010)", "pos": "noun", "translation": "Mario Vargas Llosa (Peruvian-Spanish writer, 2010 Nobel laureate)"},
                    {"lemma": "el Premio Miguel de Cervantes", "pos": "noun", "translation": "Miguel de Cervantes Prize (highest award for Spanish-language literature)"},
                    {"lemma": "Miguel Delibes («Los santos inocentes») y Carmen Laforet («Nada»)", "pos": "noun", "translation": "Miguel Delibes and Carmen Laforet (great 20th-century Spanish novelists)"}
                ],
                "grammar_title": "Reconocimientos literarios: los Nobel españoles y el Premio Cervantes",
                "grammar_text": "En el examen CCSE se pregunta con mucha frecuencia por los **Premios Nobel de Literatura españoles** y sus obras más conocidas: **José Echegaray** (1904), **Jacinto Benavente** (1922, *Los intereses creados*), **Juan Ramón Jiménez** (1956, ***Platero y yo***), **Vicente Aleixandre** (1977) y **Camilo José Cela** (1989, ***La familia de Pascual Duarte*** y ***La colmena***), además de **Mario Vargas Llosa** (2010, con doble nacionalidad peruana y española).",
                "grammar_examples": [
                    {"es": "El poeta andaluz Juan Ramón Jiménez, autor de «Platero y yo», fue galardonado con el Premio Nobel de Literatura en 1956.", "en": "The Andalusian poet Juan Ramón Jiménez, author of 'Platero and I', was awarded the Nobel Prize in Literature in 1956."},
                    {"es": "El novelista gallego Camilo José Cela recibió el Premio Nobel de Literatura en 1989 por obras como «La colmena».", "en": "The Galician novelist Camilo José Cela received the Nobel Prize in Literature in 1989 for works such as 'The Hive'."}
                ],
                "grammar_tip": "¡Tres preguntas favoritas del CCSE sobre literatura del siglo XX! 1) ¿Quién escribió *Platero y yo* y ganó el Nobel en 1956? **Juan Ramón Jiménez**. 2) ¿Quién escribió *La colmena* y *La familia de Pascual Duarte* y ganó el Nobel en 1989? **Camilo José Cela**. 3) ¿Cuál es el premio institucional más importante de la literatura en lengua española? El **Premio Miguel de Cervantes**.",
                "paragraphs": [
                    "La grandeza de la literatura española del siglo XX ha sido reconocida en seis ocasiones por la Academia Sueca con el Premio Nobel de Literatura (cinco escritores nacidos en España y el escritor hispano-peruano Mario Vargas Llosa). Los dos primeros galardonados fueron dos grandes dramaturgos: el madrileño José Echegaray en 1904 (primer español en recibir un Premio Nobel) y Jacinto Benavente en 1922, autor de la comedia *Los intereses creados*.",
                    "En el año 1956 el Premio Nobel de Literatura recayó en el gran poeta onubense Juan Ramón Jiménez (1881–1958), nacido en Moguer (Huelva). Maestro de los poetas de la Generación del 27, Juan Ramón Jiménez es el autor de uno de los libros más leídos y queridos en todas las escuelas del mundo hispánico: *Platero y yo* («Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos...»), la entrañable elegía andaluza sobre la amistad del poeta con un pequeño burro plateado.",
                    "Veintiún años más tarde, en diciembre de 1977 —coincidiendo con el renacer de las libertades en la Transición—, el Nobel premió al poeta sevillano Vicente Aleixandre (1898–1984), miembro de la Generación del 27 y autor de *La destrucción o el amor* y *Sombra del paraíso*, en nombre de toda aquella generación irrepetible.",
                    "En 1989 recibió el Premio Nobel de Literatura el novelista gallego Camilo José Cela (1916–2002), nacido en Iria Flavia (Padrón, A Coruña), quien renovó la novela española de posguerra con *La familia de Pascual Duarte* (1942), retrató el Madrid de los años cuarenta con más de trescientos personajes en su obra maestra *La colmena* (1951) y narró su recorrido por las tierras alcarreñas en *Viaje a la Alcarria*. En 2010 se sumó a esta lista el novelista hispano-peruano Mario Vargas Llosa (nacionalizado español en 1993 y miembro de la RAE). Nota importante para el examen CCSE: España cuenta además con dos Premios Nobel de Medicina y Fisiología: Santiago Ramón y Cajal (1906) y Severo Ochoa (1959).",
                    "Por último, desde 1976 el Ministerio de Cultura de España concede anualmente el Premio de Literatura en Lengua Castellana «Miguel de Cervantes» (el Premio Cervantes), considerado el galardón más importante de las letras hispánicas, que entrega el Rey cada 23 de abril en el Paraninfo de la Universidad de Alcalá de Henares a grandes autores de España e Hispanoamérica (junto a otros grandes premios literarios como el Premio Nacional de las Letras Españolas, el Premio Princesa de Asturias de las Letras o el popular Premio Planeta de novela). Entre los grandes narradores españoles contemporáneos brillan también Carmen Laforet (*Nada*), Ana María Matute, Miguel Delibes (*Los santos inocentes*, *Cinco horas con Mario*), Gonzalo Torrente Ballester, Eduardo Mendoza, Antonio Muñoz Molina, Javier Marías, Arturo Pérez-Reverte, Rosa Montero o Almudena Grandes."
                ],
                "questions": [
                    {
                        "question": "¿Qué poeta andaluz nacido en Moguer (Huelva) escribió la famosa obra «Platero y yo» y recibió el Premio Nobel de Literatura en 1956?",
                        "options": [
                            "Juan Ramón Jiménez",
                            "Gustavo Adolfo Bécquer",
                            "Luis de Góngora",
                            "Jorge Manrique"
                        ],
                        "correctIndex": 0,
                        "explanation": "Juan Ramón Jiménez (1881–1958) escribió «Platero y yo» y ganó el Premio Nobel de Literatura en 1956."
                    },
                    {
                        "question": "¿Qué escritor gallego ganó el Premio Nobel de Literatura en 1989 y es autor de las novelas «La colmena», «La familia de Pascual Duarte» y «Viaje a la Alcarria»?",
                        "options": [
                            "Camilo José Cela",
                            "Ramón María del Valle-Inclán",
                            "Benito Pérez Galdós",
                            "Fernando de Rojas"
                        ],
                        "correctIndex": 0,
                        "explanation": "Camilo José Cela recibió el Premio Nobel de Literatura en 1989."
                    },
                    {
                        "question": "¿Cuál es el premio institucional más importante que se concede anualmente en España al conjunto de la obra de un escritor en lengua castellana, entregado cada 23 de abril en la Universidad de Alcalá de Henares?",
                        "options": [
                            "El Premio Miguel de Cervantes (Premio Cervantes)",
                            "El Premio Goya",
                            "La Concha de Oro",
                            "El Premio Pritzker"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Premio Miguel de Cervantes es el máximo reconocimiento a la labor creadora de escritores españoles e hispanoamericanos."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál de los siguientes escritores españoles fue galardonado con el Premio Nobel de Literatura en 1977 como miembro de la Generación del 27?",
                        "options": [
                            "Vicente Aleixandre",
                            "Lope de Vega",
                            "Miguel de Cervantes",
                            "Mariano José de Larra"
                        ],
                        "correctIndex": 0,
                        "explanation": "El poeta Vicente Aleixandre ganó el Premio Nobel de Literatura en 1977."
                    },
                    {
                        "prompt": "¿Además de los cinco Premios Nobel de Literatura nacidos en España, qué dos científicos españoles ganaron el Premio Nobel de Fisiología o Medicina en 1906 y 1959?",
                        "options": [
                            "Santiago Ramón y Cajal (1906) y Severo Ochoa (1959)",
                            "Isaac Peral y Juan de la Cierva",
                            "Leonardo Torres Quevedo y Emilio Herrera",
                            "Miguel Servet y Francisco Javier Balmis"
                        ],
                        "correctIndex": 0,
                        "explanation": "Santiago Ramón y Cajal (1906) y Severo Ochoa (1959) son los dos Premios Nobel españoles en ciencias (Medicina y Fisiología)."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El poeta Juan Ramón ___, autor de «Platero y yo», ganó el Premio Nobel de Literatura en 1956.",
                        "answer": "Jiménez",
                        "options": ["Jiménez", "Machado", "Alberti", "Delibes"],
                        "explanation": "Juan Ramón Jiménez es el autor de «Platero y yo» y Nobel de Literatura en 1956.",
                        "english": "The poet Juan Ramón Jiménez, author of 'Platero and I', won the Nobel Prize in Literature in 1956."
                    },
                    {
                        "sentence": "El novelista gallego Camilo José ___ ganó el Premio Nobel de Literatura en 1989 y escribió «La colmena».",
                        "answer": "Cela",
                        "options": ["Cela", "Baroja", "Clarín", "Rojas"],
                        "explanation": "Camilo José Cela obtuvo el Premio Nobel de Literatura en 1989.",
                        "english": "The Galician novelist Camilo José Cela won the Nobel Prize in Literature in 1989 and wrote 'The Hive'."
                    }
                ],
                "ex_dict": {
                    "audioText": "Juan Ramón Jiménez escribió Platero y yo y Camilo José Cela escribió La colmena.",
                    "english": "Juan Ramón Jiménez wrote Platero and I and Camilo José Cela wrote The Hive."
                },
                "ex_sb": {
                    "words": ["El", "Premio", "Cervantes", "se", "entrega", "cada", "año", "en", "la", "Universidad", "de", "Alcalá", "de", "Henares."],
                    "english": "The Cervantes Prize is awarded every year at the University of Alcalá de Henares."
                }
            }
        ]
    }
]


def main():
    for u in UNITS_22_23_24:
        emit_unit_from_dict(u)


if __name__ == "__main__":
    main()
