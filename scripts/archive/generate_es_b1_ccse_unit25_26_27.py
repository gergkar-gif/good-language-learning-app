#!/usr/bin/env python3
"""Generate Spain Citizenship (CCSE) Units 25, 26, and 27 for es-es B1 track."""

from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict

UNITS_25_26_27 = [
    # =========================================================================
    # UNIT 25: Pintura y Escultura: Velázquez, Goya, Picasso y Dalí (unit_num=61, b1-arte)
    # =========================================================================
    {
        "slug": "arte",
        "unit_num": 61,
        "title": "Pintura y Escultura: Velázquez, Goya, Picasso y Dalí",
        "description": "El Greco, Diego Velázquez («Las Meninas»), Francisco de Goya, Joaquín Sorolla, Pablo Picasso («Guernica»), Salvador Dalí, Joan Miró, Eduardo Chillida y los grandes museos de España.",
        "Badge": "Arte y Museos",
        "lessons": [
            {
                "num": "01",
                "Title": "El Greco y Diego Velázquez: De Toledo a «Las Meninas»",
                "title": "El Greco y Diego Velázquez: De Toledo a «Las Meninas»",
                "grammar_slug": "ser-pintado-por-y-conservarse-en-el-museo-del-prado",
                "story_slug": "elgrecoyvelazquez",
                "story_title": "El caballero de la mano en el pecho y el misterio de «Las Meninas»",
                "objectives": [
                    "Identificar a El Greco (Doménikos Theotokópoulos, afincado en Toledo, autor de «El entierro del conde de Orgaz» y «El caballero de la mano en el pecho»).",
                    "Dominar la figura de Diego Velázquez (nacido en Sevilla, pintor de cámara de Felipe IV, autor de «Las Meninas», «La rendición de Breda» y «Las hilanderas», conservados en el Museo del Prado).",
                    "Practicar las construcciones «ser obra de» y «conservarse en el Museo Nacional del Prado»."
                ],
                "vocab": [
                    {"lemma": "El Greco (Doménikos Theotokópoulos)", "pos": "noun", "translation": "El Greco (Renaissance/Mannerist painter settled in Toledo)"},
                    {"lemma": "El entierro del conde de Orgaz / El caballero de la mano en el pecho", "pos": "noun", "translation": "The Burial of the Count of Orgaz / The Nobleman with his Hand on his Chest"},
                    {"lemma": "Diego Velázquez (1599–1660)", "pos": "noun", "translation": "Diego Velázquez (Sevillian Baroque painter, master of light and perspective)"},
                    {"lemma": "Las Meninas (La familia de Felipe IV)", "pos": "noun", "translation": "Las Meninas (masterpiece by Diego Velázquez in the Prado Museum)"},
                    {"lemma": "La rendición de Breda («Las lanzas») / Las hilanderas", "pos": "noun", "translation": "The Surrender of Breda / The Spinners (works by Velázquez)"},
                    {"lemma": "Bartolomé Esteban Murillo y Francisco de Zurbarán", "pos": "noun", "translation": "Murillo and Zurbarán (great painters of the Spanish Baroque)"},
                    {"lemma": "el pintor de cámara", "pos": "noun", "translation": "court painter to the King"},
                    {"lemma": "el Museo Nacional del Prado", "pos": "noun", "translation": "Prado National Museum (Madrid)"}
                ],
                "grammar_title": "Atribución artística y ubicación museística: «ser obra de» y «exponerse en»",
                "grammar_text": "En la Tarea 4 del examen CCSE se pide con mucha frecuencia relacionar un cuadro universal con su pintor y con el museo donde se expone: ***Las Meninas*** es la obra cumbre de **Diego Velázquez** y **se conserva en el Museo Nacional del Prado** en Madrid.",
                "grammar_examples": [
                    {"es": "El cuadro «Las Meninas» fue pintado por el sevillano Diego Velázquez en 1656 y se expone en el Museo del Prado.", "en": "The painting 'Las Meninas' was painted by the Sevillian Diego Velázquez in 1656 and is exhibited in the Prado Museum."},
                    {"es": "«El entierro del conde de Orgaz», obra maestra de El Greco, se encuentra en la iglesia de Santo Tomé de Toledo.", "en": "'The Burial of the Count of Orgaz', El Greco's masterpiece, is located in the Church of Santo Tomé in Toledo."}
                ],
                "grammar_tip": "¡Pregunta estrella del CCSE! ¿Quién pintó ***Las Meninas*** y en qué museo se encuentra? Lo pintó **Diego Velázquez** y se encuentra en el **Museo Nacional del Prado (Madrid)**.",
                "paragraphs": [
                    "La pintura española de los siglos XVI y XVII regaló a la historia del arte universal algunos de sus nombres más luminosos. El primero de ellos llegó desde la isla griega de Creta, pasó por Venecia y Roma y se instaló en 1577 en la ciudad imperial de Toledo, donde vivió hasta su muerte: Doménikos Theotokópoulos, conocido universalmente como El Greco (1541–1614).",
                    "Con sus figuras estilizadas y alargadas y sus colores vibrantes, El Greco inmortalizó el espíritu místico del Siglo de Oro en lienzos inolvidables como *El caballero de la mano en el pecho* (conservado en el Museo del Prado) y su obra cumbre, *El entierro del conde de Orgaz*, que sigue admirándose hoy en la iglesia de Santo Tomé de Toledo.",
                    "Un año antes de terminar el siglo XVI, en 1599, nació en Sevilla el pintor más grande del Barroco español y uno de los mayores genios de todos los tiempos: Diego Rodríguez de Silva y Velázquez (1599–1660). Llamado a Madrid como pintor de cámara del rey Felipe IV, Velázquez revolucionó la pintura al lograr pintar la atmósfera y el aire mismo que rodea a los personajes.",
                    "Todas las grandes obras maestras de Diego Velázquez —como *La rendición de Breda* (o *Las lanzas*), *La fragua de Vulcano*, *El triunfo de Baco* (*Los borrachos*) y *Las hilanderas*— culminan en el lienzo que pintó en 1656 y que hoy constituye el corazón del Museo Nacional del Prado en Madrid: *Las Meninas* (o *La familia de Felipe IV*). En él, la pequeña infanta Margarita aparece rodeada de sus damas de honor («meninas») mientras el propio Velázquez nos mira pincel en mano desde el interior del cuadro y los reyes se reflejan en el espejo del fondo.",
                    "En aquel mismo siglo XVII brillaron en la escuela barroca española otros grandes maestros como José de Ribera, Francisco de Zurbarán (célebre por sus bodegones y sus monjes blancos) y el sevillano Bartolomé Esteban Murillo, famoso por sus Inmaculadas y sus tiernas escenas de niños humildes en las calles de Sevilla."
                ],
                "questions": [
                    {
                        "question": "¿Qué gran pintor del Siglo de Oro español, nacido en Sevilla en 1599, es el autor del famoso cuadro «Las Meninas»?",
                        "options": [
                            "Diego Velázquez",
                            "Pablo Picasso",
                            "Salvador Dalí",
                            "Joan Miró"
                        ],
                        "correctIndex": 0,
                        "explanation": "Diego Velázquez (1599–1660) pintó «Las Meninas», conservado hoy en el Museo Nacional del Prado."
                    },
                    {
                        "question": "¿En qué museo de España se encuentra expuesto el cuadro «Las Meninas» de Diego Velázquez?",
                        "options": [
                            "En el Museo Nacional del Prado, en Madrid",
                            "En el Museo Guggenheim, en Bilbao",
                            "En el Teatro-Museo Dalí, en Figueres",
                            "En el IVAM, en Valencia"
                        ],
                        "correctIndex": 0,
                        "explanation": "«Las Meninas» es la obra más emblemática del Museo Nacional del Prado en Madrid."
                    },
                    {
                        "question": "¿En qué ciudad española se estableció y pintó sus grandes obras maestras (como «El entierro del conde de Orgaz») el pintor renacentista conocido como El Greco?",
                        "options": [
                            "En Toledo",
                            "En Santander",
                            "En Vigo",
                            "En Pamplona"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Greco vivió y pintó en Toledo desde 1577 hasta su fallecimiento en 1614."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Quién pintó «El caballero de la mano en el pecho» y «El entierro del conde de Orgaz»?",
                        "options": [
                            "El Greco",
                            "Francisco de Goya",
                            "Joaquín Sorolla",
                            "Antoni Tàpies"
                        ],
                        "correctIndex": 0,
                        "explanation": "Ambas obras maestras pertenecen a El Greco."
                    },
                    {
                        "prompt": "¿De qué rey de la Casa de Austria fue pintor de cámara Diego Velázquez?",
                        "options": [
                            "De Felipe IV",
                            "De Fernando VII",
                            "De Carlos III",
                            "De Alfonso XIII"
                        ],
                        "correctIndex": 0,
                        "explanation": "Diego Velázquez fue pintor de cámara del rey Felipe IV durante casi cuarenta años."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El cuadro «Las ___» fue pintado por Diego Velázquez y se conserva en el Museo del Prado.",
                        "answer": "Meninas",
                        "options": ["Meninas", "Fallas", "Médulas", "Glosas"],
                        "explanation": "«Las Meninas» (1656) es la obra maestra de Diego Velázquez.",
                        "english": "The painting 'Las Meninas' was painted by Diego Velázquez and is preserved in the Prado Museum."
                    },
                    {
                        "sentence": "El pintor conocido como El ___ realizó en Toledo «El entierro del conde de Orgaz».",
                        "answer": "Greco",
                        "options": ["Greco", "Cid", "Sabio", "Manco"],
                        "explanation": "El Greco desarrolló su gran obra pictórica en la ciudad de Toledo.",
                        "english": "The painter known as El Greco painted 'The Burial of the Count of Orgaz' in Toledo."
                    }
                ],
                "ex_dict": {
                    "audioText": "El cuadro Las Meninas fue pintado por Diego Velázquez y se expone en el Museo del Prado en Madrid.",
                    "english": "The painting Las Meninas was painted by Diego Velázquez and is exhibited in the Prado Museum in Madrid."
                },
                "ex_sb": {
                    "words": ["Diego", "Velázquez", "pintó", "Las", "Meninas", "y", "La", "rendición", "de", "Breda."],
                    "english": "Diego Velázquez painted Las Meninas and The Surrender of Breda."
                }
            },
            {
                "num": "02",
                "Title": "Francisco de Goya y Joaquín Sorolla: La Luz y la Historia",
                "title": "Francisco de Goya y Joaquín Sorolla: La Luz y la Historia",
                "grammar_slug": "ser-considerado-el-padre-del-arte-moderno",
                "story_slug": "goyaysorolla",
                "story_title": "De los «Caprichos» y el 3 de mayo de Goya a las playas luminosas de Sorolla",
                "objectives": [
                    "Conocer la figura de Francisco de Goya (nacido en Fuendetodos, Zaragoza, en 1746; autor de «La maja vestida», «La maja desnuda», «La familia de Carlos IV», «El 3 de mayo en Madrid» y las «Pinturas negras»).",
                    "Identificar a Joaquín Sorolla (nacido en Valencia en 1863, el «pintor de la luz» del Mediterráneo, con casa-museo en Madrid).",
                    "Practicar las construcciones «anticipar la pintura moderna» y «captar la luz del mar Mediterráneo»."
                ],
                "vocab": [
                    {"lemma": "Francisco de Goya y Lucientes (1746–1828)", "pos": "noun", "translation": "Francisco de Goya (Aragonese painter and printmaker, father of modern art)"},
                    {"lemma": "El 3 de mayo de 1808 en Madrid (Los fusilamientos)", "pos": "noun", "translation": "The Third of May 1808 in Madrid (masterpiece by Goya in the Prado Museum)"},
                    {"lemma": "La maja desnuda y La maja vestida", "pos": "noun", "translation": "The Nude Maja and The Clothed Maja (paintings by Goya)"},
                    {"lemma": "las Pinturas negras / Los caprichos", "pos": "noun", "translation": "the Black Paintings / Los Caprichos engravings (by Goya)"},
                    {"lemma": "Joaquín Sorolla (1863–1923)", "pos": "noun", "translation": "Joaquín Sorolla (Valencian painter of Mediterranean light)"},
                    {"lemma": "Paseo a orillas del mar / Niños en la playa", "pos": "noun", "translation": "Stroll on the Beach / Children on the Beach (paintings by Sorolla)"},
                    {"lemma": "el luminismo valenciano", "pos": "noun", "translation": "Valencian luminism"},
                    {"lemma": "los premios del cine español (Premios Goya)", "pos": "noun", "translation": "Spanish Film Academy Awards (named in honor of Francisco de Goya)"}
                ],
                "grammar_title": "Dos genios entre dos siglos: Francisco de Goya y Joaquín Sorolla",
                "grammar_text": "**Francisco de Goya** (nacido en **Fuendetodos, Zaragoza**, en 1746) es el eslabón entre el arte clásico y las vanguardias del siglo XX. Sus lienzos más famosos —***La familia de Carlos IV***, ***La maja vestida***, ***La maja desnuda***, ***El 2 y el 3 de mayo de 1808 en Madrid*** y las ***Pinturas negras***— se exhiben en el **Museo Nacional del Prado**. Por su parte, el valenciano **Joaquín Sorolla** es el gran maestro de la luz mediterránea.",
                "grammar_examples": [
                    {"es": "El pintor aragonés Francisco de Goya pintó «La familia de Carlos IV» y «El 3 de mayo en Madrid».", "en": "The Aragonese painter Francisco de Goya painted 'The Family of Charles IV' and 'The Third of May in Madrid'."},
                    {"es": "El pintor valenciano Joaquín Sorolla es conocido en todo el mundo por captar la luz de las playas del Mediterráneo.", "en": "The Valencian painter Joaquín Sorolla is known worldwide for capturing the light of the Mediterranean beaches."}
                ],
                "grammar_tip": "Recuerda para el CCSE: **Francisco de Goya** nació en **Aragón (Fuendetodos, Zaragoza)** y dio nombre a los **Premios Goya** del cine español; **Joaquín Sorolla** nació en **Valencia**.",
                "paragraphs": [
                    "A caballo entre los siglos XVIII y XIX se alza la figura gigantesca del pintor aragonés Francisco de Goya y Lucientes (1746–1828), nacido en el pequeño pueblo zaragozano de Fuendetodos y considerado por la historia del arte como el verdadero padre de la pintura moderna.",
                    "Goya comenzó pintando alegres cartones llenos de color para la Real Fábrica de Tapices de Madrid (como *El quitasol* o *La pradera de San Isidro*) y llegó a ser primer pintor de cámara del rey Carlos IV, a quien retrató junto a toda su corte con asombrosa sinceridad psicológica en *La familia de Carlos IV*, además de pintar *La maja desnuda* y *La maja vestida*.",
                    "Sin embargo, la sordera que sufrió en 1792 y el horror de la Guerra de la Independencia (1808–1814) transformaron radicalmente su arte. Con sus series de grabados al aguafuerte (*Los caprichos*, *Los desastres de la guerra*, *Los disparates*), sus dos lienzos monumentales sobre el levantamiento madrileño (*El 2 de mayo* y *El 3 de mayo de 1808 en Madrid*) y las sobrecogedoras *Pinturas negras* que pintó directamente sobre los muros de su casa («la Quinta del Sordo», como *Saturno devorando a su hijo* o *El perro semihundido*), Goya anticipó el expresionismo y el surrealismo del siglo XX. Todas estas obras se conservan hoy en el Museo del Prado, y en su honor los premios anuales de la Academia de Cine de España llevan el nombre de Premios Goya.",
                    "Medio siglo después de la muerte de Goya, en 1863, nació en Valencia el pintor que llenaría los lienzos españoles de sol, mar y alegría de vivir: Joaquín Sorolla (1863–1923), máximo representante del luminismo o impresionismo mediterráneo español.",
                    "Con pinceladas rápidas y blancos deslumbrantes, Sorolla pintó a los pescadores, los barcos de vela latina, las mujeres con vestidos blancos al viento (*Paseo a orillas del mar*) y los niños bañándose en las aguas del Mediterráneo (*Chicos en la playa*), además de los grandes murales sobre las regiones de España que realizó para la Hispanic Society de Nueva York. Su antigua vivienda y taller en el barrio de Chamberí de Madrid es hoy el entrañable Museo Sorolla."
                ],
                "questions": [
                    {
                        "question": "¿En qué provincia y comunidad autónoma nació el pintor Francisco de Goya, autor de «La maja vestida» y «El 3 de mayo en Madrid»?",
                        "options": [
                            "En Fuendetodos (provincia de Zaragoza, Aragón)",
                            "En Figueres (Girona, Cataluña)",
                            "En Málaga (Andalucía)",
                            "En Santiago de Compostela (Galicia)"
                        ],
                        "correctIndex": 0,
                        "explanation": "Francisco de Goya nació en Fuendetodos, en la provincia de Zaragoza (Aragón), en 1746."
                    },
                    {
                        "question": "¿Qué pintor español nacido en Valencia en 1863 es célebre internacionalmente como «el pintor de la luz» por sus cuadros de playas y escenas del mar Mediterráneo?",
                        "options": [
                            "Joaquín Sorolla",
                            "Francisco de Zurbarán",
                            "El Greco",
                            "Eduardo Chillida"
                        ],
                        "correctIndex": 0,
                        "explanation": "El valenciano Joaquín Sorolla (1863–1923) es el gran maestro de la luz mediterránea."
                    },
                    {
                        "question": "¿En qué museo se conservan «La familia de Carlos IV», «El 3 de mayo en Madrid» y las «Pinturas negras» de Francisco de Goya?",
                        "options": [
                            "En el Museo Nacional del Prado (Madrid)",
                            "En el Museo Guggenheim (Bilbao)",
                            "En el Museo Picasso (Málaga)",
                            "En el Museo Nacional de Arte Romano (Mérida)"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Museo Nacional del Prado alberga la colección más importante del mundo de obras de Francisco de Goya."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En honor de qué gran pintor español reciben su nombre los premios anuales de la Academia de las Artes y las Ciencias Cinematográficas de España?",
                        "options": [
                            "De Francisco de Goya (los Premios Goya)",
                            "De Diego Velázquez",
                            "De Bartolomé Esteban Murillo",
                            "De Joan Miró"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los premios anuales del cine español se llaman Premios Goya en homenaje a Francisco de Goya."
                    },
                    {
                        "prompt": "¿Cuál de las siguientes obras pertenece a Francisco de Goya?",
                        "options": [
                            "«La maja vestida», «La maja desnuda» y «Los caprichos»",
                            "«Las Meninas» y «La rendición de Breda»",
                            "«La persistencia de la memoria»",
                            "«El entierro del conde de Orgaz»"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las dos Majas y la serie de grabados de Los caprichos son obras célebres de Francisco de Goya."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El pintor aragonés Francisco de ___ es el autor de «El 3 de mayo en Madrid» y de las «Pinturas negras».",
                        "answer": "Goya",
                        "options": ["Goya", "Sorolla", "Velázquez", "Dalí"],
                        "explanation": "Francisco de Goya pintó los fusilamientos del 3 de mayo y las Pinturas negras.",
                        "english": "The Aragonese painter Francisco de Goya is the author of 'The Third of May in Madrid' and the 'Black Paintings'."
                    },
                    {
                        "sentence": "El pintor valenciano Joaquín ___ es mundialmente famoso por sus luminosos cuadros de playas mediterráneas.",
                        "answer": "Sorolla",
                        "options": ["Sorolla", "Murillo", "Zurbarán", "Chillida"],
                        "explanation": "Joaquín Sorolla es el gran pintor valenciano de la luz del Mediterráneo.",
                        "english": "The Valencian painter Joaquín Sorolla is world-famous for his luminous paintings of Mediterranean beaches."
                    }
                ],
                "ex_dict": {
                    "audioText": "Francisco de Goya nació en Zaragoza y Joaquín Sorolla nació en la ciudad de Valencia.",
                    "english": "Francisco de Goya was born in Zaragoza and Joaquín Sorolla was born in the city of Valencia."
                },
                "ex_sb": {
                    "words": ["Los", "cuadros", "más", "famosos", "de", "Goya", "se", "conservan", "en", "el", "Museo", "del", "Prado."],
                    "english": "The most famous paintings by Goya are preserved in the Prado Museum."
                }
            },
            {
                "num": "03",
                "Title": "Vanguardias del Siglo XX: Pablo Picasso, Salvador Dalí y Joan Miró",
                "title": "Vanguardias del Siglo XX: Pablo Picasso, Salvador Dalí y Joan Miró",
                "grammar_slug": "ser-el-creador-del-cubismo-y-maximo-exponente-del-surrealismo",
                "story_slug": "picassoydali",
                "story_title": "Del «Guernica» de Picasso a los relojes blandos de Dalí y las constelaciones de Miró",
                "objectives": [
                    "Dominar la figura de Pablo Picasso (nacido en Málaga en 1881, creador del cubismo con «Las señoritas de Avignon» y autor del «Guernica» en 1937, expuesto en el Museo Reina Sofía).",
                    "Identificar a los dos grandes maestros catalanes del surrealismo: Salvador Dalí (nacido en Figueres, Girona, autor de «La persistencia de la memoria») y Joan Miró (nacido en Barcelona).",
                    "Practicar las construcciones «ser el fundador del cubismo» y «ser el máximo representante del surrealismo»."
                ],
                "vocab": [
                    {"lemma": "Pablo Ruiz Picasso (1881–1973)", "pos": "noun", "translation": "Pablo Picasso (born in Málaga, creator of Cubism and painter of 'Guernica')"},
                    {"lemma": "el cubismo", "pos": "noun", "translation": "Cubism (avant-garde movement created by Picasso and Juan Gris)"},
                    {"lemma": "el Guernica (1937)", "pos": "noun", "translation": "Guernica (Picasso's anti-war masterpiece in the Reina Sofía Museum)"},
                    {"lemma": "Las señoritas de Avignon (1907)", "pos": "noun", "translation": "Les Demoiselles d'Avignon (foundational painting of Cubism by Picasso)"},
                    {"lemma": "Salvador Dalí (1904–1989)", "pos": "noun", "translation": "Salvador Dalí (Catalan Surrealist painter born in Figueres, Girona)"},
                    {"lemma": "el surrealismo", "pos": "noun", "translation": "Surrealism"},
                    {"lemma": "La persistencia de la memoria (los relojes blandos)", "pos": "noun", "translation": "The Persistence of Memory (iconic Surrealist painting by Salvador Dalí)"},
                    {"lemma": "Joan Miró (1893–1983)", "pos": "noun", "translation": "Joan Miró (Barcelona painter, sculptor, and ceramicist)"}
                ],
                "grammar_title": "Las vanguardias artísticas del siglo XX: cubismo y surrealismo",
                "grammar_text": "Tres pintores españoles transformaron para siempre el arte mundial del siglo XX: el malagueño **Pablo Picasso** (creador del **cubismo** junto al madrileño Juan Gris y autor del ***Guernica***, que se exhibe en el **Museo Reina Sofía** de Madrid) y los catalanes **Salvador Dalí** (nacido en Figueres, Girona, figura cumbre del **surrealismo**) y **Joan Miró** (nacido en Barcelona).",
                "grammar_examples": [
                    {"es": "Pablo Picasso nació en Málaga, creó el cubismo y pintó en 1937 el famoso mural «Guernica».", "en": "Pablo Picasso was born in Málaga, created Cubism, and painted the famous mural 'Guernica' in 1937."},
                    {"es": "Salvador Dalí, nacido en Figueres (Girona), es uno de los máximos representantes mundiales del surrealismo.", "en": "Salvador Dalí, born in Figueres (Girona), is one of the world's leading representatives of Surrealism."}
                ],
                "grammar_tip": "¡Tres preguntas clásicas del CCSE! 1) ¿Quién pintó el ***Guernica*** y dónde está? **Pablo Picasso**, y está en el **Museo Reina Sofía (Madrid)**. 2) ¿Dónde nació Picasso? En **Málaga**. 3) ¿A qué movimiento artístico pertenecen **Salvador Dalí** y **Joan Miró**? Al **surrealismo**.",
                "paragraphs": [
                    "Si el siglo XVII fue el siglo de Velázquez y el cambio al XIX fue el de Goya, el arte mundial del siglo XX no podría entenderse sin la aportación revolucionaria de tres creadores españoles: Pablo Picasso, Salvador Dalí y Joan Miró.",
                    "Pablo Ruiz Picasso (1881–1973) nació en la ciudad andaluza de Málaga y se formó en A Coruña, Barcelona y Madrid antes de instalarse en París. Tras sus etapas azul y rosa, en 1907 rompió todas las reglas de la perspectiva tradicional con el cuadro *Las señoritas de Avignon*, dando nacimiento al cubismo (movimiento en el que brilló también el pintor madrileño Juan Gris). En la primavera de 1937, por encargo del Gobierno de la Segunda República para la Exposición Internacional de París, Picasso pintó su obra más universal: el *Guernica*, un sobrecogedor grito en blanco, negro y gris contra el bombardeo de la villa vasca de Gernika y contra todas las guerras. Desde 1992, el *Guernica* es la pieza central del Museo Nacional Centro de Arte Reina Sofía en Madrid.",
                    "En otra gran corriente de vanguardia —el surrealismo, que exploraba el mundo de los sueños y del subconsciente— brilló con fama planetaria el pintor catalán Salvador Dalí (1904–1989), nacido en Figueres (Girona). Con una técnica de dibujo prodigiosa e imágenes oníricas inolvidables como los relojes blandos de *La persistencia de la memoria* (1931), *El gran masturbador* o *Muchacha en la ventana*, Dalí creó además en su ciudad natal el fascinante Teatro-Museo Dalí de Figueres.",
                    "Junto a Dalí destacó el barcelonés Joan Miró (1893–1983), pintor, escultor y ceramista que creó un lenguaje poético propio lleno de estrellas, pájaros, lunas y colores primarios (azul, rojo, amarillo y negro), presente hoy en la Fundació Joan Miró de Barcelona y en la Fundación Pilar i Joan Miró de Palma de Mallorca (además de ser el autor del famoso logotipo del sol de Turespaña).",
                    "En la segunda mitad del siglo XX y comienzos del XXI, la pintura y el arte contemporáneo español continuaron dando figuras de prestigio internacional como el catalán Antoni Tàpies (maestro del informalismo matérico), el manchego Antonio López (gran maestro del realismo contemporáneo) o el mallorquín Miquel Barceló (autor de la cúpula de la Sala de los Derechos Humanos de la ONU en Ginebra)."
                ],
                "questions": [
                    {
                        "question": "¿Quién pintó el famoso cuadro «Guernica» en 1937 y en qué museo de Madrid se exhibe actualmente?",
                        "options": [
                            "Lo pintó el malagueño Pablo Picasso y se exhibe en el Museo Nacional Centro de Arte Reina Sofía",
                            "Lo pintó Diego Velázquez y se exhibe en el Museo del Prado",
                            "Lo pintó Salvador Dalí y se exhibe en el Museo de Figueres",
                            "Lo pintó El Greco y se exhibe en Toledo"
                        ],
                        "correctIndex": 0,
                        "explanation": "El «Guernica» fue pintado por Pablo Picasso en 1937 y se encuentra expuesto en el Museo Reina Sofía de Madrid."
                    },
                    {
                        "question": "¿A qué movimiento artístico de vanguardia del siglo XX pertenece principalmente el pintor catalán Salvador Dalí, autor de «La persistencia de la memoria»?",
                        "options": [
                            "Al surrealismo",
                            "Al arte románico",
                            "Al neoclasicismo del siglo XVIII",
                            "Al gótico flamígero"
                        ],
                        "correctIndex": 0,
                        "explanation": "Salvador Dalí (1904–1989) es uno de los máximos exponentes mundiales del surrealismo."
                    },
                    {
                        "question": "¿En qué ciudad andaluza nació en 1881 el pintor Pablo Ruiz Picasso, creador del cubismo?",
                        "options": [
                            "En Málaga",
                            "En Córdoba",
                            "En Almería",
                            "En Jaén"
                        ],
                        "correctIndex": 0,
                        "explanation": "Pablo Picasso nació en Málaga el 25 de octubre de 1881."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué pintor, escultor y ceramista nacido en Barcelona es célebre por su universo surrealista de estrellas, pájaros y colores vivos, y tiene una gran fundación en la montaña de Montjuïc?",
                        "options": [
                            "Joan Miró",
                            "Francisco de Zurbarán",
                            "José de Ribera",
                            "Mariano Fortuny"
                        ],
                        "correctIndex": 0,
                        "explanation": "Joan Miró (1893–1983) es el gran artista barcelonés creador de ese universo simbólico."
                    },
                    {
                        "prompt": "¿En qué localidad catalana de la provincia de Girona nació Salvador Dalí y se encuentra hoy el famoso Teatro-Museo Dalí?",
                        "options": [
                            "En Figueres",
                            "En Reus",
                            "En Manresa",
                            "En Tortosa"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Teatro-Museo Dalí se encuentra en Figueres (Girona), ciudad natal de Salvador Dalí."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El famoso cuadro «___», pintado por Pablo Picasso en 1937, se exhibe en el Museo Reina Sofía de Madrid.",
                        "answer": "Guernica",
                        "options": ["Guernica", "Meninas", "Capricho", "Quitasol"],
                        "explanation": "El «Guernica» de Pablo Picasso se conserva en el Museo Reina Sofía.",
                        "english": "The famous painting 'Guernica', painted by Pablo Picasso in 1937, is exhibited at the Reina Sofía Museum in Madrid."
                    },
                    {
                        "sentence": "El pintor catalán Salvador ___ es mundialmente famoso por sus obras surrealistas como los relojes blandos.",
                        "answer": "Dalí",
                        "options": ["Dalí", "Goya", "Sorolla", "Murillo"],
                        "explanation": "Salvador Dalí pintó «La persistencia de la memoria» (los relojes blandos).",
                        "english": "The Catalan painter Salvador Dalí is world-famous for his Surrealist works such as the melting watches."
                    }
                ],
                "ex_dict": {
                    "audioText": "Pablo Picasso nació en Málaga y pintó el Guernica, que se expone en el Museo Reina Sofía.",
                    "english": "Pablo Picasso was born in Málaga and painted Guernica, which is exhibited at the Reina Sofía Museum."
                },
                "ex_sb": {
                    "words": ["Salvador", "Dalí", "y", "Joan", "Miró", "fueron", "dos", "grandes", "maestros", "del", "surrealismo."],
                    "english": "Salvador Dalí and Joan Miró were two great masters of Surrealism."
                }
            },
            {
                "num": "04",
                "Title": "Escultura y Arquitectura: Chillida, Gaudí, Moneo y Calatrava",
                "title": "Escultura y Arquitectura: Chillida, Gaudí, Moneo y Calatrava",
                "grammar_slug": "integrar-la-escultura-en-el-paisaje-natural-y-urbano",
                "story_slug": "esculturayarquitectura",
                "story_title": "El hierro del «Peine del Viento» frente al Cantábrico y los puentes del siglo XXI",
                "objectives": [
                    "Conocer a los grandes escultores españoles del siglo XX y XXI: Eduardo Chillida (autor de «El Peine del Viento» en San Sebastián), Jorge Oteiza, Pablo Gargallo, Julio González, Cristina Iglesias y Jaume Plensa.",
                    "Identificar a los grandes arquitectos españoles contemporáneos: Antoni Gaudí, Rafael Moneo (primer español ganador del Premio Pritzker en 1996), el estudio RCR Arquitectes (Premio Pritzker 2017) y Santiago Calatrava.",
                    "Practicar las construcciones «fundirse con el paisaje» y «ser galardonado con el Premio Pritzker de Arquitectura»."
                ],
                "vocab": [
                    {"lemma": "Eduardo Chillida (1924–2002)", "pos": "noun", "translation": "Eduardo Chillida (Basque sculptor, author of 'The Comb of the Wind')"},
                    {"lemma": "El Peine del Viento (San Sebastián)", "pos": "noun", "translation": "The Comb of the Wind (iconic steel sculptures by Chillida in Donostia-San Sebastián)"},
                    {"lemma": "Jaume Plensa y Cristina Iglesias", "pos": "noun", "translation": "Jaume Plensa and Cristina Iglesias (leading contemporary Spanish sculptors)"},
                    {"lemma": "Rafael Moneo (Premio Pritzker 1996)", "pos": "noun", "translation": "Rafael Moneo (Navarrese architect, designer of the Mérida Roman Art Museum and Prado extension)"},
                    {"lemma": "Santiago Calatrava", "pos": "noun", "translation": "Santiago Calatrava (Valencian architect and engineer, City of Arts and Sciences)"},
                    {"lemma": "el Premio Pritzker de Arquitectura", "pos": "noun", "translation": "Pritzker Architecture Prize"},
                    {"lemma": "el museo Chillida Leku (Hernani)", "pos": "noun", "translation": "Chillida Leku open-air sculpture museum"},
                    {"lemma": "Juan de Herrera (siglo XVI)", "pos": "noun", "translation": "Juan de Herrera (architect of the Monastery of El Escorial)"}
                ],
                "grammar_title": "Escultura y arquitectura española: de Chillida a Moneo y Calatrava",
                "grammar_text": "En escultura contemporánea destaca el donostiarra **Eduardo Chillida**, autor de ***El Peine del Viento*** en las rocas de la bahía de La Concha en **San Sebastián**. En arquitectura contemporánea brillan el navarro **Rafael Moneo** (Premio Pritzker), el valenciano **Santiago Calatrava** (autor de gran parte de la **Ciudad de las Artes y las Ciencias** de Valencia) y el estudio catalán **RCR Arquitectes** (Premio Pritzker).",
                "grammar_examples": [
                    {"es": "La escultura «El Peine del Viento», obra de Eduardo Chillida, se encuentra frente al mar en San Sebastián.", "en": "The sculpture 'The Comb of the Wind', by Eduardo Chillida, is located facing the sea in San Sebastián."},
                    {"es": "El arquitecto navarro Rafael Moneo fue el primer español en recibir el prestigioso Premio Pritzker de Arquitectura.", "en": "The Navarrese architect Rafael Moneo was the first Spaniard to receive the prestigious Pritzker Architecture Prize."}
                ],
                "grammar_tip": "Recuerda para el CCSE: **Eduardo Chillida** es el escultor vasco autor de ***El Peine del Viento*** (en Donostia-San Sebastián); **Santiago Calatrava** diseñó la **Ciudad de las Artes y las Ciencias** de Valencia.",
                "paragraphs": [
                    "No solo la pintura española ha dejado una huella imborrable en la cultura universal; también la escultura y la arquitectura españolas han sabido dialogar como pocas con la luz, el hierro, la piedra y el paisaje.",
                    "En el siglo XX, tras los pioneros de la escultura en hierro forjado como Julio González y Pablo Gargallo, surgió en el País Vasco una generación de escultores extraordinaria encabezada por Jorge Oteiza y, muy especialmente, por el donostiarra Eduardo Chillida (1924–2002). En el extremo occidental de la bahía de La Concha, en su ciudad natal de Donostia-San Sebastián, Chillida instaló en 1977 su obra más emblemática: *El Peine del Viento*, tres grandes piezas curvas de acero incrustadas en las rocas donde rompen las olas y sopla el viento del Cantábrico, junto al museo al aire libre Chillida Leku en Hernani.",
                    "Hoy, las plazas de medio mundo —desde Madrid, Barcelona o Bilbao hasta Chicago, Tokio o Londres— exhiben las esculturas monumentales de grandes creadores españoles actuales como la donostiarra Cristina Iglesias (autora de las puertas escultóricas de la ampliación del Museo del Prado) y el barcelonés Jaume Plensa (célebre por sus grandes rostros serenos en silencio, como la escultura *Julia* en la plaza de Colón de Madrid).",
                    "En el campo de la arquitectura, la tradición que comenzó en el siglo XVI con Juan de Herrera (autor del Monasterio de El Escorial), continuó en el XVIII con Juan de Villanueva (autor del edificio del Museo del Prado) y revolucionó el cambio al siglo XX con el modernismo de Antoni Gaudí e Ildefons Cerdà, vive hoy una época dorada.",
                    "En 1996, el arquitecto navarro Rafael Moneo (nacido en Tudela y autor del Museo Nacional de Arte Romano de Mérida, la estación de Atocha, el Kursaal de San Sebastián y la ampliación del Museo del Prado) se convirtió en el primer español galardonado con el Premio Pritzker —considerado el Nobel de la arquitectura—, distinción que en 2017 recibió también el estudio catalán RCR Arquitectes (de Olot, Girona), mientras que los puentes blancos y la Ciudad de las Artes y las Ciencias del valenciano Santiago Calatrava son iconos urbanos en los cinco continentes."
                ],
                "questions": [
                    {
                        "question": "¿Qué gran escultor vasco nacido en San Sebastián es el autor de la famosa obra en acero «El Peine del Viento», situada junto al mar Cantábrico?",
                        "options": [
                            "Eduardo Chillida",
                            "Joaquín Sorolla",
                            "Mariano Benlliure",
                            "Francisco Salzillo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Eduardo Chillida (1924–2002) creó «El Peine del Viento» en la costa de su ciudad natal, Donostia-San Sebastián."
                    },
                    {
                        "question": "¿Qué arquitecto e ingeniero valenciano diseñó la mayor parte del complejo de la Ciudad de las Artes y las Ciencias de Valencia y numerosos puentes internacionales?",
                        "options": [
                            "Santiago Calatrava",
                            "Juan de Herrera",
                            "Juan de Villanueva",
                            "Ventura Rodríguez"
                        ],
                        "correctIndex": 0,
                        "explanation": "El valenciano Santiago Calatrava es el autor principal de la Ciudad de las Artes y las Ciencias."
                    },
                    {
                        "question": "¿Qué arquitecto español nacido en Tudela (Navarra), autor del Museo Nacional de Arte Romano de Mérida y de la ampliación del Museo del Prado, fue el primer español en ganar el Premio Pritzker de Arquitectura?",
                        "options": [
                            "Rafael Moneo",
                            "Antoni Gaudí",
                            "Enrique Nieto",
                            "Lluís Domènech i Montaner"
                        ],
                        "correctIndex": 0,
                        "explanation": "Rafael Moneo ganó el Premio Pritzker de Arquitectura en 1996."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué ciudad vasca se encuentra la escultura «El Peine del Viento» de Eduardo Chillida?",
                        "options": [
                            "En Donostia-San Sebastián",
                            "En Vitoria-Gasteiz",
                            "En Santander",
                            "En Pamplona"
                        ],
                        "correctIndex": 0,
                        "explanation": "«El Peine del Viento» se alza al final de la playa de Ondarreta, en Donostia-San Sebastián."
                    },
                    {
                        "prompt": "¿Qué escultor barcelonés contemporáneo es mundialmente conocido por sus grandes cabezas humanas blancas en actitud de silencio, como la escultura «Julia» en Madrid?",
                        "options": [
                            "Jaume Plensa",
                            "Pablo Gargallo",
                            "Alonso Berruguete",
                            "Juan Martínez Montañés"
                        ],
                        "correctIndex": 0,
                        "explanation": "Jaume Plensa es uno de los escultores españoles contemporáneos de mayor proyección mundial."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La famosa escultura «El Peine del Viento» en San Sebastián es obra del escultor vasco Eduardo ___.",
                        "answer": "Chillida",
                        "options": ["Chillida", "Calatrava", "Moneo", "Gaudí"],
                        "explanation": "Eduardo Chillida realizó «El Peine del Viento» en Donostia-San Sebastián.",
                        "english": "The famous sculpture 'The Comb of the Wind' in San Sebastián is the work of the Basque sculptor Eduardo Chillida."
                    },
                    {
                        "sentence": "El arquitecto navarro Rafael ___ diseñó el Museo Nacional de Arte Romano de Mérida y ganó el Premio Pritzker.",
                        "answer": "Moneo",
                        "options": ["Moneo", "Herrera", "Villanueva", "Plensa"],
                        "explanation": "Rafael Moneo es Premio Pritzker de Arquitectura (1996) y Premio Príncipe de Asturias de las Artes (2012).",
                        "english": "The Navarrese architect Rafael Moneo designed the National Museum of Roman Art in Mérida and won the Pritzker Prize."
                    }
                ],
                "ex_dict": {
                    "audioText": "La escultura El Peine del Viento de Eduardo Chillida se encuentra en la costa de San Sebastián.",
                    "english": "The sculpture The Comb of the Wind by Eduardo Chillida is located on the coast of San Sebastián."
                },
                "ex_sb": {
                    "words": ["Santiago", "Calatrava", "diseñó", "la", "Ciudad", "de", "las", "Artes", "y", "las", "Ciencias", "de", "Valencia."],
                    "english": "Santiago Calatrava designed the City of Arts and Sciences in Valencia."
                }
            },
            {
                "num": "05",
                "Title": "Los Grandes Museos de España: Prado, Reina Sofía, Thyssen y Guggenheim",
                "title": "Los Grandes Museos de España: Prado, Reina Sofía, Thyssen y Guggenheim",
                "grammar_slug": "formar-el-triangulo-del-arte-en-el-paseo-del-prado",
                "story_slug": "grandesmuseos",
                "story_title": "Un paseo por las grandes pinacotecas: dónde vive cada obra maestra en España",
                "objectives": [
                    "Distinguir sin error para el CCSE los tres museos del «Triángulo del Arte» en el Paseo del Prado de Madrid: Museo Nacional del Prado (arte clásico hasta el siglo XIX: Velázquez, Goya, El Greco, El Bosco), Museo Nacional Centro de Arte Reina Sofía (arte del siglo XX y contemporáneo: «Guernica» de Picasso, Dalí, Miró) y Museo Nacional Thyssen-Bornemisza.",
                    "Recordar la ubicación de otros museos clave de España: Museo Guggenheim (Bilbao), Teatro-Museo Dalí (Figueres), MNAC y Museo Picasso (Barcelona), Museo Picasso (Málaga) y Museo Nacional de Arte Romano (Mérida).",
                    "Practicar las construcciones «albergar la colección de» y «conformar el Paseo del Arte»."
                ],
                "vocab": [
                    {"lemma": "el Paseo del Arte (Triángulo del Arte de Madrid)", "pos": "noun", "translation": "Art Walk / Golden Triangle of Art in Madrid (Prado, Reina Sofía, and Thyssen)"},
                    {"lemma": "el Museo Nacional del Prado (inaugurado en 1819)", "pos": "noun", "translation": "Prado National Museum"},
                    {"lemma": "el Museo Nacional Centro de Arte Reina Sofía (MNCARS)", "pos": "noun", "translation": "Reina Sofía National Art Center Museum"},
                    {"lemma": "el Museo Nacional Thyssen-Bornemisza", "pos": "noun", "translation": "Thyssen-Bornemisza National Museum"},
                    {"lemma": "el Museo Guggenheim Bilbao (1997)", "pos": "noun", "translation": "Guggenheim Museum Bilbao"},
                    {"lemma": "el Teatro-Museo Dalí (Figueres, Girona)", "pos": "noun", "translation": "Dalí Theatre-Museum in Figueres"},
                    {"lemma": "el Museo Nacional de Arte Romano (Mérida)", "pos": "noun", "translation": "National Museum of Roman Art in Mérida"},
                    {"lemma": "la pinacoteca", "pos": "noun", "translation": "art gallery / painting museum"}
                ],
                "grammar_title": "Guía rápida de museos para el examen CCSE: ¿qué hay en cada museo?",
                "grammar_text": "En el examen CCSE es esencial no confundir el **Museo del Prado** (pintura de los siglos XII al XIX: *Las Meninas* de **Velázquez**, *El 3 de mayo* y *Las majas* de **Goya**, *El jardín de las delicias* de **El Bosco**, **El Greco**, **Rubens** y **Tiziano**) con el **Museo Reina Sofía** (arte del siglo XX y actual: el ***Guernica*** de **Picasso**, obras de **Dalí** y **Miró**).",
                "grammar_examples": [
                    {"es": "El Museo del Prado, el Museo Reina Sofía y el Museo Thyssen-Bornemisza forman el llamado Triángulo del Arte de Madrid.", "en": "The Prado Museum, the Reina Sofía Museum, and the Thyssen-Bornemisza Museum form the so-called Golden Triangle of Art in Madrid."},
                    {"es": "Mientras que «Las Meninas» de Velázquez está en el Prado, el «Guernica» de Picasso está en el Reina Sofía.", "en": "While 'Las Meninas' by Velázquez is in the Prado, 'Guernica' by Picasso is in the Reina Sofía."}
                ],
                "grammar_tip": "¡Regla infalible para el CCSE! **Prado** = Velázquez, Goya, El Greco, El Bosco (hasta el siglo XIX). **Reina Sofía** = Picasso (*Guernica*), Dalí, Miró (siglo XX en adelante). **Bilbao** = Museo Guggenheim.",
                "paragraphs": [
                    "Para superar con éxito las preguntas de cultura del examen CCSE conviene tener muy claro el mapa de los grandes museos de España y saber qué época o qué obras maestras alberga cada uno. El epicentro museístico del país se encuentra en el Paseo del Prado de Madrid, donde tres grandes instituciones forman el célebre «Triángulo del Arte» (dentro del Paisaje de la Luz, Patrimonio de la Humanidad).",
                    "El primero es el Museo Nacional del Prado, inaugurado en noviembre de 1819 en el edificio neoclásico diseñado por Juan de Villanueva. Es una de las pinacotecas de arte antiguo y clásico más importantes del planeta (desde el Románico hasta finales del siglo XIX): en sus salas se admiran *Las Meninas* y *Las hilanderas* de Diego Velázquez, *La familia de Carlos IV*, *Las majas* y *El 3 de mayo* de Francisco de Goya, *El caballero de la mano en el pecho* de El Greco y *El jardín de las delicias* de El Bosco.",
                    "A pocos pasos, junto a la glorieta de Atocha y en el edificio del antiguo Hospital General del siglo XVIII ampliado por Jean Nouvel, se levanta el Museo Nacional Centro de Arte Reina Sofía (MNCARS). Su colección toma el relevo cronológico exactamente donde termina la del Prado (finales del siglo XIX, todo el siglo XX y el arte actual), y su sala más visitada custodia el *Guernica* (1937) de Pablo Picasso, acompañado por grandes obras de Salvador Dalí, Joan Miró, Juan Gris y Julio González.",
                    "El tercer vértice del triángulo madrileño es el Museo Nacional Thyssen-Bornemisza (en el Palacio de Villahermosa), cuya extraordinaria colección recorre siete siglos de pintura europea y norteamericana —desde el Renacimiento y el Impresionismo hasta el Pop Art—, completado muy cerca por el Museo Arqueológico Nacional (donde está la Dama de Elche) y la Galería de las Colecciones Reales junto al Palacio Real.",
                    "Fuera de Madrid, España cuenta con una red museística de primer orden mundial que aparece con frecuencia en el CCSE: en Bilbao (País Vasco), el Museo Guggenheim Bilbao diseñado por Frank Gehry; en Figueres (Girona, Cataluña), el Teatro-Museo Dalí; en Barcelona, el Museu Nacional d'Art de Catalunya (MNAC, famoso por su arte románico), el Museu Picasso y la Fundació Joan Miró; en Málaga, el Museo Picasso Málaga y el Centro Pompidou; en Valencia, el IVAM y el Museo de Bellas Artes; y en Mérida (Extremadura), el Museo Nacional de Arte Romano."
                ],
                "questions": [
                    {
                        "question": "¿Qué tres grandes museos forman el famoso «Triángulo del Arte» en el entorno del Paseo del Prado de Madrid?",
                        "options": [
                            "El Museo Nacional del Prado, el Museo Nacional Centro de Arte Reina Sofía y el Museo Nacional Thyssen-Bornemisza",
                            "El Museo Guggenheim, el Teatro-Museo Dalí y el IVAM",
                            "El Museo Naval, el Museo del Ferrocarril y el Museo de Ciencias Naturales",
                            "La Alhambra, la Mezquita de Córdoba y el Alcázar de Sevilla"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Prado, el Reina Sofía y el Thyssen-Bornemisza integran el Triángulo del Arte en el Paseo del Prado de Madrid."
                    },
                    {
                        "question": "¿Cuál es la diferencia principal entre las colecciones del Museo del Prado y las del Museo Reina Sofía en Madrid?",
                        "options": [
                            "El Prado alberga pintura clásica hasta el siglo XIX (como Velázquez y Goya) y el Reina Sofía arte del siglo XX y contemporáneo (como el «Guernica» de Picasso)",
                            "El Prado solo expone aviones antiguos y el Reina Sofía solo expone monedas romanas",
                            "El Prado está en Bilbao y el Reina Sofía está en Sevilla",
                            "No hay ninguna diferencia, son el mismo edificio"
                        ],
                        "correctIndex": 0,
                        "explanation": "El límite cronológico entre el Prado y el Reina Sofía se sitúa en torno al nacimiento de Pablo Picasso (1881): arte clásico hasta el XIX en el Prado, y siglo XX y contemporáneo en el Reina Sofía."
                    },
                    {
                        "question": "¿En qué ciudad de Extremadura se encuentra el Museo Nacional de Arte Romano, proyectado por el arquitecto Rafael Moneo?",
                        "options": [
                            "En Mérida (Badajoz)",
                            "En Cáceres",
                            "En Toledo",
                            "En Salamanca"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Museo Nacional de Arte Romano (MNAR) se encuentra en Mérida, junto al Teatro y Anfiteatro Romanos."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué museo de Madrid se puede contemplar el famoso tríptico «El jardín de las delicias» de El Bosco junto a las obras de Velázquez y Goya?",
                        "options": [
                            "En el Museo Nacional del Prado",
                            "En el Museo del Traje",
                            "En el Museo América",
                            "En el Museo Romántico"
                        ],
                        "correctIndex": 0,
                        "explanation": "«El jardín de las delicias» de El Bosco forma parte de las colecciones reales expuestas en el Museo del Prado."
                    },
                    {
                        "prompt": "¿Qué arquitecto canadiense-estadounidense diseñó el edificio revestido de placas de titanio del Museo Guggenheim de Bilbao, inaugurado en 1997?",
                        "options": [
                            "Frank Gehry",
                            "Antoni Gaudí",
                            "Juan de Villanueva",
                            "Ildefons Cerdà"
                        ],
                        "correctIndex": 0,
                        "explanation": "Frank Gehry proyectó el edificio del Museo Guggenheim Bilbao."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El Museo Nacional del ___, en Madrid, alberga las obras maestras de Diego Velázquez y Francisco de Goya.",
                        "answer": "Prado",
                        "options": ["Prado", "Tajo", "Teide", "Retiro"],
                        "explanation": "El Museo Nacional del Prado fue inaugurado en 1819 y custodia las obras de Velázquez y Goya.",
                        "english": "The Prado National Museum, in Madrid, houses the masterpieces of Diego Velázquez and Francisco de Goya."
                    },
                    {
                        "sentence": "El Museo Nacional Centro de Arte ___ Sofía alberga el arte español del siglo XX, incluido el «Guernica».",
                        "answer": "Reina",
                        "options": ["Reina", "Princesa", "Infanta", "Corona"],
                        "explanation": "El Museo Nacional Centro de Arte Reina Sofía custodia el «Guernica» de Picasso.",
                        "english": "The Reina Sofía National Art Center Museum houses 20th-century Spanish art, including 'Guernica'."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Museo del Prado, el Museo Reina Sofía y el Museo Thyssen forman el Triángulo del Arte de Madrid.",
                    "english": "The Prado Museum, the Reina Sofía Museum, and the Thyssen Museum form the Golden Triangle of Art in Madrid."
                },
                "ex_sb": {
                    "words": ["Las", "obras", "de", "Velázquez", "y", "Goya", "se", "exponen", "en", "el", "Museo", "del", "Prado."],
                    "english": "The works of Velázquez and Goya are exhibited in the Prado Museum."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 26: Música, Danza y Cine Español (unit_num=62, b1-musicacine)
    # =========================================================================
    {
        "slug": "musicacine",
        "unit_num": 62,
        "title": "Música, Danza y Cine Español",
        "description": "Falla, Albéniz, Rodrigo, la zarzuela, Caballé y Plácido Domingo, Paco de Lucía y el flamenco, Buñuel, Berlanga, Almodóvar, Amenábar, Bardem, Penélope Cruz y los Premios Goya.",
        "Badge": "Música, Danza y Cine",
        "lessons": [
            {
                "num": "01",
                "Title": "Música Clásica y Lírica: Falla, Rodrigo, la Zarzuela y las Grandes Voces",
                "title": "Música Clásica y Lírica: Falla, Rodrigo, la Zarzuela y las Grandes Voces",
                "grammar_slug": "componer-obras-sinfonicas-e-interpretar-en-los-principales-teatros",
                "story_slug": "musicaclasicayzarzuela",
                "story_title": "De las notas del «Concierto de Aranjuez» a las voces de Montserrat Caballé y Plácido Domingo",
                "objectives": [
                    "Identificar a los grandes compositores españoles de música clásica: Isaac Albéniz, Enrique Granados, Manuel de Falla («El amor brujo», «El sombrero de tres picos») y Joaquín Rodrigo («Concierto de Aranjuez»), además del violonchelista Pau Casals y el guitarrista Andrés Segovia.",
                    "Conocer el género lírico español de la zarzuela y a los grandes cantantes de ópera españoles (Plácido Domingo, José Carreras, Alfredo Kraus, Montserrat Caballé, Teresa Berganza y Victoria de los Ángeles).",
                    "Practicar las construcciones «ser el compositor de» y «destacar en el ámbito de la lírica internacional»."
                ],
                "vocab": [
                    {"lemma": "Manuel de Falla (1876–1946)", "pos": "noun", "translation": "Manuel de Falla (Andalusian classical composer, 'El amor brujo')"},
                    {"lemma": "Joaquín Rodrigo («Concierto de Aranjuez»)", "pos": "noun", "translation": "Joaquín Rodrigo (blind Valencian composer of the 'Concierto de Aranjuez')"},
                    {"lemma": "Isaac Albéniz («Suite Iberia») y Enrique Granados («Goyescas»)", "pos": "noun", "translation": "Albéniz and Granados (great Catalan pianist-composers)"},
                    {"lemma": "la zarzuela", "pos": "noun", "translation": "zarzuela (traditional Spanish lyric-dramatic operetta genre)"},
                    {"lemma": "Montserrat Caballé y Teresa Berganza", "pos": "noun", "translation": "Montserrat Caballé and Teresa Berganza (legendary Spanish opera singers)"},
                    {"lemma": "Plácido Domingo, José Carreras y Alfredo Kraus", "pos": "noun", "translation": "Plácido Domingo, José Carreras, and Alfredo Kraus (world-famous Spanish tenors)"},
                    {"lemma": "Pau Casals (violonchelo) y Andrés Segovia (guitarra clásica)", "pos": "noun", "translation": "Pau Casals and Andrés Segovia (master instrumentalists)"},
                    {"lemma": "el Teatro Real de Madrid / el Gran Teatre del Liceu de Barcelona", "pos": "noun", "translation": "Royal Theater of Madrid / Liceu Opera House of Barcelona"}
                ],
                "grammar_title": "Grandes nombres de la música española para el CCSE",
                "grammar_text": "En el examen CCSE se pregunta con frecuencia por dos compositores fundamentales del siglo XX: el gaditano **Manuel de Falla** (autor de ***El amor brujo*** y ***El sombrero de tres picos***) y el valenciano **Joaquín Rodrigo** (autor del famoso ***Concierto de Aranjuez*** para guitarra y orquesta), así como por el género musical escénico típicamente español: **la zarzuela**.",
                "grammar_examples": [
                    {"es": "El compositor gaditano Manuel de Falla es el autor de obras universales como «El amor brujo».", "en": "The Cádiz-born composer Manuel de Falla is the author of universal works such as 'Love, the Magician'."},
                    {"es": "El «Concierto de Aranjuez» para guitarra y orquesta fue compuesto por el maestro Joaquín Rodrigo.", "en": "The 'Concierto de Aranjuez' for guitar and orchestra was composed by maestro Joaquín Rodrigo."}
                ],
                "grammar_tip": "Relaciones musicales imprescindibles para el CCSE: **Manuel de Falla** = *El amor brujo*; **Joaquín Rodrigo** = *Concierto de Aranjuez*; **Pau Casals** = violonchelista; **Montserrat Caballé, Plácido Domingo y José Carreras** = cantantes de ópera.",
                "paragraphs": [
                    "La música española ocupa un lugar de honor en los auditorios de todo el planeta gracias a su capacidad para fundir las raíces populares de sus distintas regiones con el lenguaje sinfónico universal. A finales del siglo XIX y principios del XX, los pianistas y compositores catalanes Isaac Albéniz (autor de la *Suite Iberia*) y Enrique Granados (autor de *Goyescas*) llevaron los ritmos hispanos a las grandes salas de conciertos de París y Nueva York.",
                    "La cumbre de la música sinfónica española del siglo XX llegó con el compositor gaditano Manuel de Falla (1876–1946), autor de obras maestras como *Noches en los jardines de España*, la ópera *La vida breve* y los ballets *El amor brujo* (con su célebre «Danza ritual del fuego») y *El sombrero de tres picos*.",
                    "En 1939, el compositor valenciano Joaquín Rodrigo (1901–1999) —ciego desde los tres años de edad— escribió la obra española más interpretada en todo el mundo: el *Concierto de Aranjuez* para guitarra y orquesta, cuyo segundo movimiento (*Adagio*) evoca los jardines del Palacio Real de Aranjuez. Al prestigio universal de la guitarra clásica española contribuyó decisivamente el maestro jiennense Andrés Segovia, mientras que el catalán Pau Casals (1876–1973) revolucionó para siempre la interpretación del violonchelo y recibió la Medalla de la Paz de la ONU.",
                    "España cuenta además con un género lírico y teatral propio de enorme arraigo popular desde el siglo XVII hasta el XX: la zarzuela, que alterna escenas habladas con partes cantadas, coros y danzas (con títulos inmortales como *La verbena de la Paloma* de Tomás Bretón, *La revoltosa* de Ruperto Chapí o *Doña Francisquita* de Amadeo Vives), representada habitualmente en el Teatro de la Zarzuela de Madrid.",
                    "Por último, en los grandes templos mundiales de la ópera —encabezados en España por el Teatro Real de Madrid, el Gran Teatre del Liceu de Barcelona, el Palau de les Arts de Valencia y el Teatro de la Maestranza de Sevilla— han brillado voces españolas irrepetibles: las sopranos y mezzosopranos Montserrat Caballé (que protagonizó junto a Freddie Mercury el himno *Barcelona* para los Juegos Olímpicos de 1992), Victoria de los Ángeles y Teresa Berganza, y los tenores Alfredo Kraus, Plácido Domingo y José Carreras."
                ],
                "questions": [
                    {
                        "question": "¿Quién compuso el famoso «Concierto de Aranjuez» para guitarra y orquesta, una de las piezas musicales españolas más célebres en todo el mundo?",
                        "options": [
                            "Joaquín Rodrigo",
                            "Pedro Almodóvar",
                            "Eduardo Chillida",
                            "Camilo José Cela"
                        ],
                        "correctIndex": 0,
                        "explanation": "El compositor valenciano Joaquín Rodrigo (1901–1999) compuso el «Concierto de Aranjuez» en 1939."
                    },
                    {
                        "question": "¿Qué gran compositor español nacido en Cádiz es el autor de los ballets «El amor brujo» y «El sombrero de tres picos»?",
                        "options": [
                            "Manuel de Falla",
                            "Santiago Calatrava",
                            "Benito Pérez Galdós",
                            "Luis Buñuel"
                        ],
                        "correctIndex": 0,
                        "explanation": "Manuel de Falla (1876–1946) compuso «El amor brujo» y «El sombrero de tres picos»."
                    },
                    {
                        "question": "¿Qué profesión artística compartieron figuras españolas de fama mundial como Montserrat Caballé, Plácido Domingo, José Carreras, Alfredo Kraus y Teresa Berganza?",
                        "options": [
                            "Cantantes de ópera y lírica",
                            "Arquitectos modernistas",
                            "Directores de fotografía",
                            "Escultores abstractos"
                        ],
                        "correctIndex": 0,
                        "explanation": "Caballé, Berganza, Kraus, Domingo y Carreras son grandes figuras españolas del canto lírico y la ópera mundial."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cómo se llama el género musical escénico tradicionalmente español que combina partes cantadas y habladas, con obras como «La verbena de la Paloma»?",
                        "options": [
                            "La zarzuela",
                            "La sonata",
                            "El madrigal",
                            "La fuga"
                        ],
                        "correctIndex": 0,
                        "explanation": "La zarzuela es el género lírico-dramático español que alterna escenas habladas y cantadas."
                    },
                    {
                        "prompt": "¿Qué instrumento musical tocaba con maestría universal el músico catalán Pau Casals?",
                        "options": [
                            "El violonchelo",
                            "La gaita",
                            "La trompeta",
                            "El acordeón"
                        ],
                        "correctIndex": 0,
                        "explanation": "Pau Casals (1876–1973) fue uno de los mejores violonchelistas de todos los tiempos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El famoso «Concierto de ___» para guitarra y orquesta fue compuesto por Joaquín Rodrigo.",
                        "answer": "Aranjuez",
                        "options": ["Aranjuez", "Altamira", "Doñana", "Mérida"],
                        "explanation": "El «Concierto de Aranjuez» es la obra maestra de Joaquín Rodrigo.",
                        "english": "The famous 'Concierto de Aranjuez' for guitar and orchestra was composed by Joaquín Rodrigo."
                    },
                    {
                        "sentence": "El compositor gaditano Manuel de ___ es el autor de «El amor brujo».",
                        "answer": "Falla",
                        "options": ["Falla", "Goya", "Lorca", "Cela"],
                        "explanation": "Manuel de Falla compuso «El amor brujo».",
                        "english": "The Cádiz-born composer Manuel de Falla is the author of 'Love, the Magician'."
                    }
                ],
                "ex_dict": {
                    "audioText": "Manuel de Falla compuso El amor brujo y Joaquín Rodrigo compuso el Concierto de Aranjuez.",
                    "english": "Manuel de Falla composed Love, the Magician and Joaquín Rodrigo composed the Concierto de Aranjuez."
                },
                "ex_sb": {
                    "words": ["Montserrat", "Caballé", "y", "Plácido", "Domingo", "son", "grandes", "figuras", "de", "la", "ópera."],
                    "english": "Montserrat Caballé and Plácido Domingo are great figures of opera."
                }
            },
            {
                "num": "02",
                "Title": "El Flamenco, Paco de Lucía y las Danzas de España",
                "title": "El Flamenco, Paco de Lucía y las Danzas de España",
                "grammar_slug": "ser-declarado-patrimonio-cultural-inmaterial-de-la-humanidad",
                "story_slug": "flamencoydanza",
                "story_title": "Cante, toque y baile: de la guitarra de Paco de Lucía al mapa de las danzas españolas",
                "objectives": [
                    "Comprender el arte del flamenco (declarado Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO en 2010) en sus tres vertientes: el cante, el toque (guitarra) y el baile.",
                    "Recordar al guitarrista Paco de Lucía (Premio Príncipe de Asturias de las Artes), al cantaor Camarón de la Isla, a bailaores como Sara Baras y Antonio Gades, y relacionar cada danza tradicional con su región (sardana en Cataluña, muñeira en Galicia, jota en Aragón, aurresku en el País Vasco, chotis en Madrid, sevillanas en Andalucía).",
                    "Practicar la construcción «integrar el cante, el toque y el baile»."
                ],
                "vocab": [
                    {"lemma": "el flamenco (cante, toque y baile)", "pos": "noun", "translation": "flamenco (singing, guitar playing, and dance; UNESCO Intangible Heritage)"},
                    {"lemma": "Paco de Lucía (1947–2014)", "pos": "noun", "translation": "Paco de Lucía (legendary flamenco guitarist from Algeciras, Cádiz)"},
                    {"lemma": "Camarón de la Isla y Enrique Morente", "pos": "noun", "translation": "Camarón de la Isla and Enrique Morente (great flamenco singers / cantaores)"},
                    {"lemma": "Sara Baras, Carmen Amaya y Antonio Gades", "pos": "noun", "translation": "Sara Baras, Carmen Amaya, and Antonio Gades (world-famous flamenco dancers)"},
                    {"lemma": "la muñeira (Galicia) / la sardana (Cataluña)", "pos": "noun", "translation": "muñeira (Galician dance) / sardana (Catalan circle dance)"},
                    {"lemma": "la jota (Aragón) / el aurresku (País Vasco)", "pos": "noun", "translation": "jota (Aragonese dance) / aurresku (traditional Basque ceremonial dance)"},
                    {"lemma": "el chotis (Madrid) / las sevillanas (Andalucía)", "pos": "noun", "translation": "chotis (traditional dance of Madrid) / sevillanas"},
                    {"lemma": "el Ballet Nacional de España / Tamara Rojo", "pos": "noun", "translation": "National Ballet of Spain / Tamara Rojo (classical ballet dancer)"}
                ],
                "grammar_title": "El mapa musical y dancístico de España para el examen CCSE",
                "grammar_text": "En el examen CCSE se pregunta tanto por las grandes figuras del **flamenco** —como el guitarrista gaditano **Paco de Lucía**, el cantaor **Camarón de la Isla** o la bailaora **Sara Baras**— como por la danza tradicional de cada comunidad autónoma: **muñeira** (Galicia), **sardana** (Cataluña), **jota** (Aragón), **aurresku** (País Vasco), **chotis** (Madrid) e **isa** (Canarias).",
                "grammar_examples": [
                    {"es": "El guitarrista gaditano Paco de Lucía llevó la guitarra flamenca a los escenarios de todo el mundo.", "en": "The Cádiz-born guitarist Paco de Lucía brought the flamenco guitar to stages all over the world."},
                    {"es": "En el año 2010 la UNESCO declaró el flamenco Patrimonio Cultural Inmaterial de la Humanidad.", "en": "In the year 2010 UNESCO declared flamenco an Intangible Cultural Heritage of Humanity."}
                ],
                "grammar_tip": "¡Repaso rápido de bailes regionales para el CCSE! **Sardana** = Cataluña; **Muñeira** = Galicia; **Jota** = Aragón (y otras regiones); **Chotis** = Madrid; **Aurresku** = País Vasco; **Sevillanas / Flamenco** = Andalucía.",
                "paragraphs": [
                    "Nacido en Andalucía (con hondas raíces también en regiones vecinas como Extremadura y Murcia, donde se celebra el Festival Internacional del Cante de las Minas de La Unión) de la fusión secular de tradiciones andaluzas, gitanas, árabes, castellanas y sefardíes, el flamenco es una de las expresiones artísticas más intensas y admiradas del planeta. En noviembre de 2010, la UNESCO lo inscribió en la Lista Representativa del Patrimonio Cultural Inmaterial de la Humanidad.",
                    "El arte flamenco se apoya en tres pilares inseparables: el «cante» (la voz del cantaor o cantaora, que expresa desde el dolor profundo de la *seguiriya* o la *soleá* hasta la fiesta de las *bulerías* y *alegrías*), el «toque» (la guitarra española o flamenca) y el «baile» (caracterizado por el zapateado, el braceo y el compás).",
                    "En la historia contemporánea del flamenco brillan dos nombres que revolucionaron este arte en el último tercio del siglo XX: el cantaor gaditano Camarón de la Isla (nacido en San Fernando, Cádiz) y el genial guitarrista Paco de Lucía (1947–2014, nacido en Algeciras, Cádiz), autor de *Entre dos aguas* y galardonado con el Premio Príncipe de Asturias de las Artes, quien abrió el flamenco al diálogo con el jazz y la música clásica. Junto a ellos destacan cantaores como Enrique Morente, Carmen Linares, José Mercé o Miguel Poveda, y bailaores y coreógrafos como Carmen Amaya, Antonio Gades, Cristina Hoyos, Joaquín Cortés y la gaditana Sara Baras.",
                    "Además del flamenco y de la danza clásica y estilizada —representada por el Ballet Nacional de España, la Compañía Nacional de Danza y grandes bailarines internacionales como Tamara Rojo, Nacho Duato, Ángel Corella o Igor Yebra—, cada región de España conserva con orgullo sus propios bailes e instrumentos tradicionales.",
                    "Así, en Galicia resuena la gaita en el baile de la muñeira; en Cataluña se baila en corro la sardana al son de la cobla; en Aragón y buena parte del interior vibra la jota con castañuelas y rondallas; en el País Vasco se baila en momentos solemnes el aurresku de honor al toque del txistu; en las Islas Canarias se entona la isa acompañada del timple; y en las verbenas de San Isidro de Madrid los «chulapos» y «chulapas» bailan el tradicional chotis sobre el espacio de un ladrillo al son del organillo."
                ],
                "questions": [
                    {
                        "question": "¿Qué gran guitarrista español nacido en Algeciras (Cádiz), autor de «Entre dos aguas», revolucionó la guitarra flamenca y recibió el Premio Príncipe de Asturias de las Artes?",
                        "options": [
                            "Paco de Lucía",
                            "Pau Casals",
                            "Salvador Dalí",
                            "Rafael Moneo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Paco de Lucía (1947–2014) es el guitarrista flamenco más universal de la historia."
                    },
                    {
                        "question": "¿En qué profesión artística han destacado internacionalmente los españoles Sara Baras, Antonio Gades, Joaquín Cortés y Tamara Rojo?",
                        "options": [
                            "En la danza y el baile (flamenco y ballet)",
                            "En la arquitectura de puentes",
                            "En la novela realista del siglo XIX",
                            "En la investigación bioquímica"
                        ],
                        "correctIndex": 0,
                        "explanation": "Sara Baras, Antonio Gades y Joaquín Cortés son grandes figuras del baile flamenco y la danza española, y Tamara Rojo del ballet clásico."
                    },
                    {
                        "question": "¿Cuál es la danza tradicional propia de Galicia y cuál es el baile castizo típico de las fiestas de San Isidro en Madrid?",
                        "options": [
                            "En Galicia la muñeira y en Madrid el chotis",
                            "En Galicia la sardana y en Madrid el aurresku",
                            "En Galicia la isa canaria y en Madrid la muñeira",
                            "Ambos bailes son exclusivos de las Islas Baleares"
                        ],
                        "correctIndex": 0,
                        "explanation": "La muñeira (acompañada de la gaita) es el baile tradicional de Galicia, y el chotis es el baile típico de Madrid."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuáles son las tres disciplinas fundamentales que integran el arte del flamenco?",
                        "options": [
                            "El cante, el toque (guitarra) y el baile",
                            "La pintura, la escultura y el grabado",
                            "La novela, el ensayo y el periodismo",
                            "El remo, la vela y la natación"
                        ],
                        "correctIndex": 0,
                        "explanation": "El flamenco se compone de cante, toque y baile."
                    },
                    {
                        "prompt": "¿Cómo se llama la danza solemne de reverencia y honor tradicional del País Vasco, interpretada al son del txistu y el tamboril?",
                        "options": [
                            "El aurresku",
                            "El chotis",
                            "La sevillana",
                            "La muñeira"
                        ],
                        "correctIndex": 0,
                        "explanation": "El aurresku es la danza tradicional de homenaje y respeto del País Vasco."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El guitarrista gaditano ___ de Lucía es una de las mayores leyendas mundiales de la guitarra flamenca.",
                        "answer": "Paco",
                        "options": ["Paco", "Luis", "Pedro", "Juan"],
                        "explanation": "Paco de Lucía (Francisco Sánchez Gómez) llevó la guitarra flamenca a todos los continentes.",
                        "english": "The Cádiz-born guitarist Paco de Lucía is one of the greatest world legends of the flamenco guitar."
                    },
                    {
                        "sentence": "La ___ es el baile tradicional de Galicia, mientras que la sardana es propia de Cataluña.",
                        "answer": "muñeira",
                        "options": ["muñeira", "zarzuela", "fabada", "ensaimada"],
                        "explanation": "La muñeira es la danza tradicional gallega.",
                        "english": "The muñeira is the traditional dance of Galicia, while the sardana is typical of Catalonia."
                    }
                ],
                "ex_dict": {
                    "audioText": "El flamenco fue declarado Patrimonio Cultural Inmaterial de la Humanidad y Paco de Lucía fue su gran guitarrista.",
                    "english": "Flamenco was declared an Intangible Cultural Heritage of Humanity and Paco de Lucía was its great guitarist."
                },
                "ex_sb": {
                    "words": ["Sara", "Baras", "y", "Tamara", "Rojo", "son", "grandes", "figuras", "de", "la", "danza", "española."],
                    "english": "Sara Baras and Tamara Rojo are great figures of Spanish dance."
                }
            },
            {
                "num": "03",
                "Title": "Grandes Directores del Cine Español: De Buñuel y Berlanga a Almodóvar",
                "title": "Grandes Directores del Cine Español: De Buñuel y Berlanga a Almodóvar",
                "grammar_slug": "ganar-el-oscar-a-la-mejor-pelicula-internacional",
                "story_slug": "historiadelcine",
                "story_title": "De «Bienvenido, Míster Marshall» a los Óscar de Garci, Trueba, Almodóvar y Amenábar",
                "objectives": [
                    "Identificar a los maestros históricos del cine español: el aragonés Luis Buñuel («Viridiana», «El discreto encanto de la burguesía»), el valenciano Luis García Berlanga («Bienvenido, Míster Marshall», «El verdugo»), Juan Antonio Bardem y Carlos Saura.",
                    "Memorizar a los cuatro directores españoles que han ganado el premio Óscar a la mejor película internacional/extranjera: José Luis Garci («Volver a empezar», 1982), Fernando Trueba («Belle Époque», 1993), Pedro Almodóvar («Todo sobre mi madre», 1999, y mejor guion original por «Hable con ella») y Alejandro Amenábar («Mar adentro», 2004), además de directores actuales como J. A. Bayona, Isabel Coixet e Iciar Bollaín.",
                    "Practicar las construcciones «ser dirigida por» y «obtener el premio Óscar a la mejor película internacional»."
                ],
                "vocab": [
                    {"lemma": "Luis Buñuel (1900–1983)", "pos": "noun", "translation": "Luis Buñuel (Aragonese surrealist film director, 'Viridiana')"},
                    {"lemma": "Luis García Berlanga («Bienvenido, Míster Marshall», «El verdugo»)", "pos": "noun", "translation": "Luis García Berlanga (Valencian film director, master of social satire)"},
                    {"lemma": "José Luis Garci («Volver a empezar», primer Óscar español en 1982)", "pos": "noun", "translation": "José Luis Garci (director of Spain's first Academy Award-winning film)"},
                    {"lemma": "Pedro Almodóvar («Todo sobre mi madre», «Volver», «Mujeres al borde de un ataque de nervios»)", "pos": "noun", "translation": "Pedro Almodóvar (Manchego film director, winner of two Oscars)"},
                    {"lemma": "Alejandro Amenábar («Mar adentro», «Los otros», «Tesis»)", "pos": "noun", "translation": "Alejandro Amenábar (film director and composer, Oscar winner for 'The Sea Inside')"},
                    {"lemma": "Fernando Trueba («Belle Époque»)", "pos": "noun", "translation": "Fernando Trueba (Oscar-winning film director)"},
                    {"lemma": "Isabel Coixet, Iciar Bollaín y Carla Simón", "pos": "noun", "translation": "Coixet, Bollaín, and Simón (acclaimed Spanish women film directors)"},
                    {"lemma": "Juan Antonio Bayona («Lo imposible», «La sociedad de la nieve»)", "pos": "noun", "translation": "J. A. Bayona (contemporary film director from Barcelona)"}
                ],
                "grammar_title": "El cine español y sus cuatro premios Óscar a la mejor película internacional",
                "grammar_text": "En el examen CCSE es muy frecuente preguntar por los grandes **directores de cine españoles**. Cuatro películas españolas han ganado el **Óscar de Hollywood a la mejor película de habla no inglesa**: ***Volver a empezar*** de **José Luis Garci** (1982, el primero de nuestra historia), ***Belle Époque*** de **Fernando Trueba** (1993), ***Todo sobre mi madre*** de **Pedro Almodóvar** (1999) y ***Mar adentro*** de **Alejandro Amenábar** (2004), además del Óscar de **Luis Buñuel** por su película francesa *El discreto encanto de la burguesía* (1972).",
                "grammar_examples": [
                    {"es": "«Volver a empezar», dirigida por José Luis Garci, fue la primera película española que ganó el premio Óscar.", "en": "'Begin the Beguine', directed by José Luis Garci, was the first Spanish film to win the Academy Award."},
                    {"es": "El director manchego Pedro Almodóvar ganó el Óscar por «Todo sobre mi madre» y por el guion de «Hable con ella».", "en": "The Manchego director Pedro Almodóvar won the Oscar for 'All About My Mother' and for the screenplay of 'Talk to Her'."}
                ],
                "grammar_tip": "¡Memoriza estos nombres de cine para el CCSE! **Luis Buñuel** y **Luis García Berlanga** (maestros clásicos); **José Luis Garci** (primer Óscar español con *Volver a empezar*); **Pedro Almodóvar** (*Todo sobre mi madre*, *Volver*); **Alejandro Amenábar** (*Mar adentro*, *Los otros*).\"",
                "paragraphs": [
                    "El cine español tiene más de un siglo de historia apasionante. Su primer genio universal nació en Calanda (Teruel, Aragón) en el año 1900: Luis Buñuel (1900–1983). Amigo de Salvador Dalí y Federico García Lorca en la Residencia de Estudiantes de Madrid, Buñuel inauguró el cine surrealista con *Un perro andaluz* (1929), desarrolló una brillante etapa en México (*Los olvidados*), ganó la Palma de Oro del Festival de Cannes con la española *Viridiana* (1961) y obtuvo en 1972 el premio Óscar con *El discreto encanto de la burguesía*.",
                    "Dentro de España, durante los años cincuenta y sesenta, el director valenciano Luis García Berlanga (1921–2010) —a menudo en colaboración con el genial guionista riojano Rafael Azcona— creó un retrato tierno, coral e irónico de la sociedad española en obras maestras inmortales como *Bienvenido, Míster Marshall* (1953), *Plácido*, *El verdugo* y *La escopeta nacional*, junto a otros grandes directores como Juan Antonio Bardem, Carlos Saura o Mario Camus (*Los santos inocentes*).",
                    "Con la llegada de la democracia, el cine español conquistó el reconocimiento de la Academia de Hollywood. En marzo de 1983, la película *Volver a empezar* (1982), dirigida por José Luis Garci y rodada en Gijón (Asturias), hizo historia al ganar el primer premio Óscar a la mejor película en lengua extranjera para España. Diez años después, Fernando Trueba logró el segundo Óscar para nuestro cine con la luminosa comedia *Belle Époque* (1993).",
                    "El cineasta español de mayor proyección internacional en las últimas cuatro décadas es el manchego Pedro Almodóvar (nacido en Calzada de Calatrava, Ciudad Real, en 1949). Con un estilo inconfundible lleno de color, emoción y grandes personajes femeninos, Almodóvar ha dirigido clásicos como *Mujeres al borde de un ataque de nervios*, *Todo sobre mi madre* (Óscar a la mejor película extranjera en 1999), *Hable con ella* (Óscar al mejor guion original en 2002), *Volver* o *Dolor y gloria*. En 2004, Alejandro Amenábar (autor también de *Tesis*, *Abre los ojos* y *Los otros*) conquistó un nuevo Óscar a la mejor película internacional con *Mar adentro*, protagonizada por Javier Bardem.",
                    "Hoy el cine español brilla en los festivales de todo el mundo gracias a cineastas como Juan Antonio Bayona (*El orfanato*, *Lo imposible*, *La sociedad de la nieve*), Álex de la Iglesia, Alberto Rodríguez, Rodrigo Sorogoyen, y a una extraordinaria generación de mujeres directoras —pioneras como Pilar Miró y Josefina Molina, y autoras actuales como Isabel Coixet (*La vida secreta de las palabras*, *La librería*), Iciar Bollaín (*Te doy mis ojos*, *Maixabel*), Carla Simón (*Alcarràs*, Oso de Oro en el Festival de Berlín) o Alauda Ruiz de Azúa—."
                ],
                "questions": [
                    {
                        "question": "¿Cuál fue la primera película española en ganar el premio Óscar de Hollywood a la mejor película en lengua extranjera (en 1982/1983) y quién la dirigió?",
                        "options": [
                            "«Volver a empezar», dirigida por José Luis Garci",
                            "«Lo que el viento se llevó», dirigida por Victor Fleming",
                            "«La dolce vita», dirigida por Federico Fellini",
                            "«Ciudadano Kane», dirigida por Orson Welles"
                        ],
                        "correctIndex": 0,
                        "explanation": "«Volver a empezar» (1982), de José Luis Garci, ganó el primer Óscar a la mejor película de habla no inglesa para España."
                    },
                    {
                        "question": "¿Qué director de cine manchego ha ganado dos premios Óscar por «Todo sobre mi madre» y «Hable con ella», y es autor de películas como «Volver» y «Mujeres al borde de un ataque de nervios»?",
                        "options": [
                            "Pedro Almodóvar",
                            "Eduardo Chillida",
                            "Paco de Lucía",
                            "Camilo José Cela"
                        ],
                        "correctIndex": 0,
                        "explanation": "Pedro Almodóvar es el director español más premiado internacionalmente."
                    },
                    {
                        "question": "¿Qué director de cine español dirigió «Mar adentro» (ganadora del Óscar en 2004), «Tesis» y «Los otros»?",
                        "options": [
                            "Alejandro Amenábar",
                            "Luis García Berlanga",
                            "Segundo de Chomón",
                            "Fructuós Gelabert"
                        ],
                        "correctIndex": 0,
                        "explanation": "Alejandro Amenábar escribió, dirigió y compuso la música de «Mar adentro», «Tesis» y «Los otros»."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué director valenciano es el autor de comedias clásicas fundamentales del cine español como «Bienvenido, Míster Marshall» y «El verdugo»?",
                        "options": [
                            "Luis García Berlanga",
                            "Joaquín Sorolla",
                            "Vicente Blasco Ibáñez",
                            "Santiago Calatrava"
                        ],
                        "correctIndex": 0,
                        "explanation": "Luis García Berlanga (1921–2010) dirigió «Bienvenido, Míster Marshall», «Plácido» y «El verdugo»."
                    },
                    {
                        "prompt": "¿Cuál es la profesión de las españolas Isabel Coixet, Iciar Bollaín y Carla Simón?",
                        "options": [
                            "Directoras de cine",
                            "Magistradas del Tribunal Supremo",
                            "Jugadoras de baloncesto",
                            "Soprano de zarzuela"
                        ],
                        "correctIndex": 0,
                        "explanation": "Isabel Coixet, Iciar Bollaín y Carla Simón son destacadas directoras del cine español contemporáneo."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El cineasta manchego Pedro ___ dirigió «Todo sobre mi madre» y «Mujeres al borde de un ataque de nervios».",
                        "answer": "Almodóvar",
                        "options": ["Almodóvar", "Berlanga", "Garci", "Buñuel"],
                        "explanation": "Pedro Almodóvar ganó el Óscar por «Todo sobre mi madre» y «Hable con ella».",
                        "english": "The Manchego filmmaker Pedro Almodóvar directed 'All About My Mother' and 'Women on the Verge of a Nervous Breakdown'."
                    },
                    {
                        "sentence": "El director aragonés Luis ___ fue una figura clave del cine surrealista mundial con obras como «Viridiana».",
                        "answer": "Buñuel",
                        "options": ["Buñuel", "Sorolla", "Falla", "Rodrigo"],
                        "explanation": "Luis Buñuel (nacido en Calanda, Teruel) dirigió «Un perro andaluz» y «Viridiana».",
                        "english": "The Aragonese director Luis Buñuel was a key figure of world Surrealist cinema with works such as 'Viridiana'."
                    }
                ],
                "ex_dict": {
                    "audioText": "Pedro Almodóvar ganó el premio Óscar con la película Todo sobre mi madre.",
                    "english": "Pedro Almodóvar won the Oscar award with the film All About My Mother."
                },
                "ex_sb": {
                    "words": ["José", "Luis", "Garci", "ganó", "el", "primer", "premio", "Óscar", "para", "el", "cine", "español."],
                    "english": "José Luis Garci won the first Oscar award for Spanish cinema."
                }
            },
            {
                "num": "04",
                "Title": "Actores, Actrices y los Premios Goya de la Academia de Cine",
                "title": "Actores, Actrices y los Premios Goya de la Academia de Cine",
                "grammar_slug": "ser-premiado-con-el-goya-y-el-oscar-de-interpretacion",
                "story_slug": "actoresygoya",
                "story_title": "De Fernando Fernán Gómez y Carmen Maura a los Óscar de Javier Bardem y Penélope Cruz",
                "objectives": [
                    "Recordar que los premios anuales de la Academia de las Artes y las Ciencias Cinematográficas de España son los Premios Goya.",
                    "Identificar a los dos intérpretes españoles ganadores del premio Óscar de actuación: Javier Bardem (2007, por «No es país para viejos») y Penélope Cruz (2008, por «Vicky Cristina Barcelona»), así como a Antonio Banderas y a grandes leyendas como Fernando Rey, Francisco Rabal, Fernando Fernán Gómez, José Sacristán, Lola Herrera, Concha Velasco, Carmen Maura y Marisa Paredes.",
                    "Practicar las construcciones «recibir el Premio Goya» y «ser el primer actor / la primera actriz española en ganar el Óscar»."
                ],
                "vocab": [
                    {"lemma": "los Premios Goya", "pos": "noun", "translation": "Goya Awards (annual awards of the Spanish Film Academy)"},
                    {"lemma": "la Academia de las Artes y las Ciencias Cinematográficas de España", "pos": "noun", "translation": "Spanish Academy of Film Arts and Sciences"},
                    {"lemma": "Javier Bardem (Óscar 2007)", "pos": "noun", "translation": "Javier Bardem (first Spanish actor to win an acting Oscar)"},
                    {"lemma": "Penélope Cruz (Óscar 2008)", "pos": "noun", "translation": "Penélope Cruz (first Spanish actress to win an acting Oscar)"},
                    {"lemma": "Antonio Banderas", "pos": "noun", "translation": "Antonio Banderas (actor and director born in Málaga)"},
                    {"lemma": "Fernando Fernán Gómez, Fernando Rey y Francisco Rabal", "pos": "noun", "translation": "classic legends of Spanish acting"},
                    {"lemma": "Carmen Maura, Concha Velasco, Lola Herrera y Marisa Paredes", "pos": "noun", "translation": "iconic Spanish theater and film actresses"},
                    {"lemma": "José Sacristán y Luis Tosar", "pos": "noun", "translation": "acclaimed Spanish actors"}
                ],
                "grammar_title": "Reconocimientos del cine español: los Premios Goya y los Óscar de interpretación",
                "grammar_text": "En el examen CCSE aparece de forma recurrente esta pregunta: **¿Cómo se llaman los premios anuales del cine español?** Se llaman **Premios Goya** (y consisten en un busto de bronce del pintor Francisco de Goya). Además, dos intérpretes españoles han ganado el **Óscar de interpretación**: **Javier Bardem** y **Penélope Cruz**.",
                "grammar_examples": [
                    {"es": "Los Premios Goya son los galardones que concede cada año la Academia de Cine de España.", "en": "The Goya Awards are the prizes awarded each year by the Film Academy of Spain."},
                    {"es": "Javier Bardem y Penélope Cruz son los dos primeros actores españoles galardonados con el premio Óscar de interpretación.", "en": "Javier Bardem and Penélope Cruz are the first two Spanish actors awarded the Oscar for acting."}
                ],
                "grammar_tip": "¡Pregunta fija del CCSE! **Premios Goya** = cine español; **Premios Max** = teatro y artes escénicas; **Premio Cervantes** = literatura.",
                "paragraphs": [
                    "Cada invierno, millones de espectadores siguen por televisión la gran fiesta anual del cine español: la gala de entrega de los Premios Goya. Creados en 1987 por la Academia de las Artes y las Ciencias Cinematográficas de España, los Premios Goya reconocen a los mejores profesionales de cada especialidad cinematográfica (mejor película, dirección, interpretación, guion, música o efectos especiales) con un busto en bronce del pintor Francisco de Goya, diseñado originalmente por el escultor Mariano Benlliure.",
                    "La historia de la interpretación en España cuenta con una estirpe extraordinaria de actores y actrices de teatro y cine. Entre las grandes leyendas clásicas brillaron Sara Montiel (la primera estrella española en triunfar en el Hollywood de los años cincuenta), Fernando Rey (protagonista de las películas de Luis Buñuel y de *The French Connection*), Francisco Rabal, Alfredo Landa, José Luis López Vázquez y el polifacético actor, escritor, dramaturgo y académico de la RAE Fernando Fernán Gómez.",
                    "En el teatro y el cine de la democracia han dejado actuaciones inolvidables actrices como Concha Velasco, Lola Herrera, Núria Espert (Premio Princesa de Asturias de las Artes), Carmen Maura, Marisa Paredes, Victoria Abril, Verónica Forqué, Maribel Verdú o Emma Suárez, y actores como José Sacristán, Héctor Alterio, Juan Diego, Eduard Fernández, Javier Gutiérrez, Antonio de la Torre o el gallego Luis Tosar.",
                    "A partir de los años noventa, tres intérpretes españoles dieron el salto definitivo al estrellato mundial. El primero en abrir camino en Hollywood fue el malagueño Antonio Banderas (nominado al Óscar por *Dolor y gloria* y ganador del premio al mejor actor en el Festival de Cannes, además de impulsor del Teatro del Soho en su Málaga natal).",
                    "Pocos años después llegaron dos hitos históricos para la interpretación española: en la gala de 2008 (por el año 2007), Javier Bardem (nacido en Las Palmas de Gran Canaria en el seno de una histórica familia de cineastas) se convirtió en el primer actor español en ganar el premio Óscar de interpretación por *No es país para viejos*; y justo al año siguiente, en 2009 (por el año 2008), la madrileña Penélope Cruz (nacida en Alcobendas, Madrid, y ganadora también de la Copa Volpi en Venecia) se convirtió en la primera actriz española en ganar el premio Óscar por su papel en *Vicky Cristina Barcelona*."
                ],
                "questions": [
                    {
                        "question": "¿Cómo se llaman los premios anuales más importantes que concede la Academia de las Artes y las Ciencias Cinematográficas de España?",
                        "options": [
                            "Los Premios Goya",
                            "Los Premios Cervantes",
                            "Los Premios Planeta",
                            "Los Premios Pritzker"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Premios Goya son los galardones anuales del cine español."
                    },
                    {
                        "question": "¿Qué dos intérpretes españoles hicieron historia al convertirse en el primer actor y la primera actriz de España en ganar el premio Óscar de interpretación en Hollywood?",
                        "options": [
                            "Javier Bardem y Penélope Cruz",
                            "Rafael Nadal y Pau Gasol",
                            "Plácido Domingo y Montserrat Caballé",
                            "Paco de Lucía y Sara Baras"
                        ],
                        "correctIndex": 0,
                        "explanation": "Javier Bardem (2007/2008) y Penélope Cruz (2008/2009) son los dos intérpretes españoles ganadores del premio Óscar de actuación."
                    },
                    {
                        "question": "¿Cuál es la profesión de los españoles Antonio Banderas, José Sacristán, Luis Tosar, Carmen Maura y Maribel Verdú?",
                        "options": [
                            "Actores y actrices de cine y teatro",
                            "Pintores del Barroco",
                            "Presidentes de parlamentos autonómicos",
                            "Científicos del CSIC"
                        ],
                        "correctIndex": 0,
                        "explanation": "Todos ellos son reconocidos actores y actrices del cine y el teatro español."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué ciudad andaluza nació el actor y director internacional Antonio Banderas?",
                        "options": [
                            "En Málaga",
                            "En Burgos",
                            "En Lugo",
                            "En Huesca"
                        ],
                        "correctIndex": 0,
                        "explanation": "Antonio Banderas nació en Málaga en 1960."
                    },
                    {
                        "prompt": "¿A qué gran pintor español representa la estatuilla o busto que se entrega a los ganadores de los premios anuales del cine español?",
                        "options": [
                            "A Francisco de Goya",
                            "A El Greco",
                            "A Diego Velázquez",
                            "A Salvador Dalí"
                        ],
                        "correctIndex": 0,
                        "explanation": "El trofeo de los Premios Goya es un busto en bronce de Francisco de Goya."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Los Premios ___ son los galardones que otorga anualmente la Academia de Cine de España.",
                        "answer": "Goya",
                        "options": ["Goya", "Max", "Ondas", "Nadal"],
                        "explanation": "Los Premios Goya premian cada año las mejores obras del cine español.",
                        "english": "The Goya Awards are the prizes granted annually by the Film Academy of Spain."
                    },
                    {
                        "sentence": "Penélope ___ fue la primera actriz española en ganar el premio Óscar de interpretación.",
                        "answer": "Cruz",
                        "options": ["Cruz", "Maura", "Velasco", "Baras"],
                        "explanation": "Penélope Cruz ganó el premio Óscar en la edición de 2009.",
                        "english": "Penélope Cruz was the first Spanish actress to win the Oscar for acting."
                    }
                ],
                "ex_dict": {
                    "audioText": "Javier Bardem y Penélope Cruz son dos actores españoles que han ganado el premio Óscar.",
                    "english": "Javier Bardem and Penélope Cruz are two Spanish actors who have won the Oscar award."
                },
                "ex_sb": {
                    "words": ["La", "Academia", "de", "Cine", "entrega", "cada", "año", "los", "Premios", "Goya."],
                    "english": "The Film Academy presents the Goya Awards every year."
                }
            },
            {
                "num": "05",
                "Title": "Festivales de Cine, Teatro y Medios de Comunicación en España",
                "title": "Festivales de Cine, Teatro y Medios de Comunicación en España",
                "grammar_slug": "acoger-el-festival-internacional-de-cine-y-entregar-la-concha-de-oro",
                "story_slug": "escenayfestivales",
                "story_title": "De la Concha de Oro en San Sebastián al corral de comedias de Almagro y RTVE",
                "objectives": [
                    "Ubicar los grandes festivales de cine de España: San Sebastián (Concha de Oro), Málaga (Biznaga de Oro al cine en español), Valladolid (SEMINCI, Espiga de Oro) y Sitges (cine fantástico y de terror).",
                    "Identificar los grandes festivales de teatro (Mérida para el teatro grecolatino y Almagro en Ciudad Real para el teatro clásico del Siglo de Oro) y los Premios Max de las Artes Escénicas.",
                    "Conocer la radiotelevisión pública estatal (RTVE: La 1, La 2, Canal 24 Horas, RNE) y la agencia pública de noticias EFE."
                ],
                "vocab": [
                    {"lemma": "el Festival Internacional de Cine de San Sebastián (Concha de Oro)", "pos": "noun", "translation": "San Sebastián International Film Festival (Golden Shell award)"},
                    {"lemma": "el Festival de Málaga (Biznaga de Oro) y la SEMINCI de Valladolid (Espiga de Oro)", "pos": "noun", "translation": "Málaga Film Festival and Valladolid International Film Week"},
                    {"lemma": "el Festival de Cine Fantástico de Sitges (Barcelona)", "pos": "noun", "translation": "Sitges International Fantastic Film Festival"},
                    {"lemma": "el Festival Internacional de Teatro Clásico de Almagro (Ciudad Real)", "pos": "noun", "translation": "Almagro International Classical Theater Festival (Corral de Comedias)"},
                    {"lemma": "los Premios Max de las Artes Escénicas", "pos": "noun", "translation": "Max Awards for the Performing Arts (theater and dance)"},
                    {"lemma": "Radiotelevisión Española (RTVE: TVE y RNE)", "pos": "noun", "translation": "Spanish Public Broadcasting Corporation (public TV and radio)"},
                    {"lemma": "la Agencia EFE", "pos": "noun", "translation": "EFE News Agency (world's leading Spanish-language news agency)"},
                    {"lemma": "los Premios Ondas", "pos": "noun", "translation": "Ondas Awards (radio, television, and music awards)"}
                ],
                "grammar_title": "Festivales, premios escénicos y medios públicos en el examen CCSE",
                "grammar_text": "En las tareas 4 y 5 del CCSE se pregunta a menudo por la ciudad sede de cada festival y por los medios de comunicación públicos: **Donostia-San Sebastián** acoge el principal festival internacional de cine de España (**Concha de Oro**), **Sitges** el de cine fantástico, **Mérida** y **Almagro** los festivales de teatro clásico, **RTVE** es la corporación pública de radio y televisión, y **EFE** es la gran agencia internacional de noticias en español.",
                "grammar_examples": [
                    {"es": "El Festival Internacional de Cine de San Sebastián entrega como máximo galardón la Concha de Oro.", "en": "The San Sebastián International Film Festival awards the Golden Shell as its highest prize."},
                    {"es": "Radiotelevisión Española (RTVE) es la corporación pública estatal que agrupa a Televisión Española y Radio Nacional de España.", "en": "Spanish Radio and Television (RTVE) is the state public corporation that brings together Spanish Television and National Radio of Spain."}
                ],
                "grammar_tip": "¡Cuatro asociaciones directas para el CCSE! 1) **Concha de Oro** = Festival de Cine de San Sebastián. 2) **Premios Max** = Teatro y Danza. 3) **RTVE (La 1, La 2, RNE)** = radiotelevisión pública estatal. 4) **Agencia EFE** = agencia internacional de noticias en español.",
                "paragraphs": [
                    "A lo largo del año, numerosas ciudades españolas se visten de alfombra roja para celebrar festivales cinematográficos y teatrales de prestigio mundial. El más importante y de máxima categoría internacional («clase A») es el Festival Internacional de Cine de San Sebastián (Zinemaldia), fundado en 1953 en la capital guipuzcoana, cuyo premio principal a la mejor película es la Concha de Oro y cuyo premio honorífico a toda una carrera es el Premio Donostia.",
                    "Junto al festival donostiarra brillan otras tres citas cinematográficas muy preguntadas en el examen CCSE: en otoño, la Semana Internacional de Cine de Valladolid (SEMINCI, que entrega la Espiga de Oro al cine de autor) y el Festival Internacional de Cine Fantástico de Cataluña en la villa costera de Sitges (Barcelona), referente mundial del cine fantástico y de terror; y en primavera, el Festival de Málaga, consagrado al cine en español, que concede la Biznaga de Oro.",
                    "En el ámbito de las artes escénicas, cuyos galardones anuales en toda España son los Premios Max (en forma de manzana con antifaz), dos localidades históricas se convierten cada verano en capitales del teatro clásico: en Mérida (Badajoz), su Teatro Romano de dos mil años de antigüedad acoge el Festival Internacional de Teatro Clásico de Mérida; y en Almagro (Ciudad Real, Castilla-La Mancha), su Corral de Comedias del siglo XVII —el único conservado íntegro de aquella época— es el corazón del Festival Internacional de Teatro Clásico de Almagro, dedicado al teatro del Siglo de Oro.",
                    "¿Y cómo se informan y entretienen diariamente los ciudadanos en España? El sistema audiovisual español combina grandes grupos privados de televisión y radio (como Atresmedia y Mediaset, o cadenas radiofónicas como la SER, COPE u Onda Cero) con un servicio público estatal: la Corporación de Radio y Televisión Española (RTVE), integrada por Televisión Española (con canales como La 1, La 2, el canal informativo 24 Horas, Teledeporte y Clan) y Radio Nacional de España (RNE), además de las radiotelevisiones públicas de las comunidades autónomas agrupadas en la FORTA.",
                    "En la prensa escrita destacan cabeceras de información general como *El País*, *El Mundo*, *ABC*, *La Vanguardia* o *La Voz de Galicia* (junto a diarios deportivos como *Marca* o *As*), y en el corazón de la información mundial late la Agencia EFE, fundada en 1939, que es la primera agencia de noticias en lengua española del mundo y la cuarta mayor del planeta."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es el máximo galardón que se entrega a la mejor película en el Festival Internacional de Cine de San Sebastián?",
                        "options": [
                            "La Concha de Oro",
                            "El Oso de Plata",
                            "El León de Bronce",
                            "La Palma del Desierto"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Concha de Oro (inspirada en la bahía de La Concha de San Sebastián) es el máximo premio del Festival de Cine de San Sebastián."
                    },
                    {
                        "question": "¿Qué corporación pública estatal gestiona en España los canales de televisión «La 1», «La 2» y «Canal 24 Horas», así como «Radio Nacional de España (RNE)»?",
                        "options": [
                            "Radiotelevisión Española (RTVE)",
                            "La Agencia Tributaria (AEAT)",
                            "La Red de Parques Nacionales",
                            "Patrimonio Nacional"
                        ],
                        "correctIndex": 0,
                        "explanation": "RTVE (Corporación de Radio y Televisión Española) es el organismo público estatal de radiodifusión y televisión."
                    },
                    {
                        "question": "¿Cómo se llama la principal agencia internacional de noticias de España y la más importante del mundo en lengua española?",
                        "options": [
                            "La Agencia EFE",
                            "La Agencia AENA",
                            "La Agencia AEMET",
                            "La Agencia RENFE"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Agencia EFE es la agencia pública internacional de noticias de España y líder mundial de información en español."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué localidad manchega de la provincia de Ciudad Real se conserva un famoso Corral de Comedias del siglo XVII y se celebra cada verano el Festival Internacional de Teatro Clásico del Siglo de Oro?",
                        "options": [
                            "En Almagro",
                            "En Sitges",
                            "En Ribadesella",
                            "En Santoña"
                        ],
                        "correctIndex": 0,
                        "explanation": "Almagro (Ciudad Real) conserva su Corral de Comedias de 1628 y celebra el Festival Internacional de Teatro Clásico."
                    },
                    {
                        "prompt": "¿Cómo se llaman los premios anuales más importantes del teatro y la danza (artes escénicas) en España?",
                        "options": [
                            "Los Premios Max",
                            "Los Premios Goya",
                            "Los Premios Cervantes",
                            "Los Premios Planeta"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Premios Max de las Artes Escénicas reconocen anualmente al teatro y la danza en España."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El Festival Internacional de Cine de San Sebastián entrega como máximo premio la ___ de Oro.",
                        "answer": "Concha",
                        "options": ["Concha", "Espiga", "Biznaga", "Estrella"],
                        "explanation": "La Concha de Oro es el premio principal del Festival de San Sebastián.",
                        "english": "The San Sebastián International Film Festival awards the Golden Shell as its highest prize."
                    },
                    {
                        "sentence": "La Agencia ___ es la agencia internacional de noticias más importante del mundo en lengua española.",
                        "answer": "EFE",
                        "options": ["EFE", "BOE", "DGT", "ONU"],
                        "explanation": "La Agencia EFE es la gran agencia española de noticias.",
                        "english": "The EFE Agency is the most important international news agency in the world in the Spanish language."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Festival Internacional de Cine de San Sebastián entrega la Concha de Oro a la mejor película.",
                    "english": "The San Sebastián International Film Festival awards the Golden Shell to the best film."
                },
                "ex_sb": {
                    "words": ["Radiotelevisión", "Española", "es", "la", "corporación", "pública", "de", "radio", "y", "televisión."],
                    "english": "Spanish Radio and Television is the public radio and television corporation."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 27: Fiestas Nacionales, Autonómicas y Tradiciones (unit_num=63, b1-fiestas)
    # =========================================================================
    {
        "slug": "fiestas",
        "unit_num": 63,
        "title": "Fiestas Nacionales, Autonómicas y Tradiciones",
        "description": "Las doce uvas de Nochevieja y los Reyes Magos, Semana Santa, Feria de Abril, San Juan y la Tomatina, calendario laboral de festivos y los grandes campeones del deporte español.",
        "Badge": "Fiestas y Deporte",
        "lessons": [
            {
                "num": "01",
                "Title": "De la Navidad y las Doce Uvas a los Reyes Magos y el Carnaval",
                "title": "De la Navidad y las Doce Uvas a los Reyes Magos y el Carnaval",
                "grammar_slug": "tomar-las-doce-uvas-al-compas-de-las-campanadas",
                "story_slug": "fiestasdeinviernoycarnaval",
                "story_title": "Doce campanadas en la Puerta del Sol, la Cabalgata de Reyes y las coplas de febrero",
                "objectives": [
                    "Conocer las tradiciones navideñas españolas: el Sorteo de la Lotería de Navidad (22 de diciembre), la Nochebuena (24 de diciembre), las doce uvas de la suerte en Nochevieja (31 de diciembre a medianoche con el reloj de la Puerta del Sol) y la Cabalgata y Día de los Reyes Magos (5 y 6 de enero, con el roscón de Reyes).",
                    "Identificar los dos Carnavales más famosos de España en el mes de febrero (Santa Cruz de Tenerife y Cádiz).",
                    "Practicar las construcciones «tomar las doce uvas de la suerte» y «celebrar la llegada de los Reyes Magos»."
                ],
                "vocab": [
                    {"lemma": "las doce uvas de la suerte (Nochevieja, 31 de diciembre)", "pos": "noun", "translation": "the twelve lucky grapes eaten at midnight on New Year's Eve"},
                    {"lemma": "las campanadas de la Puerta del Sol", "pos": "noun", "translation": "the midnight chimes of the Puerta del Sol clock in Madrid"},
                    {"lemma": "los Reyes Magos (Melchor, Gaspar y Baltasar, 6 de enero)", "pos": "noun", "translation": "the Three Wise Men / Epiphany (January 6)"},
                    {"lemma": "la Cabalgata de Reyes (5 de enero) y el roscón de Reyes", "pos": "noun", "translation": "Three Kings Parade and Kings' ring cake"},
                    {"lemma": "el Sorteo Extraordinario de Navidad (22 de diciembre, «El Gordo»)", "pos": "noun", "translation": "Spanish Christmas Lottery"},
                    {"lemma": "el turrón, el mazapán y los polvorones", "pos": "noun", "translation": "traditional Spanish Christmas sweets"},
                    {"lemma": "el Carnaval de Santa Cruz de Tenerife", "pos": "noun", "translation": "Carnival of Santa Cruz de Tenerife (Reina del Carnaval)"},
                    {"lemma": "el Carnaval de Cádiz (las chirigotas y comparsas)", "pos": "noun", "translation": "Carnival of Cádiz (satirical musical groups in the Gran Teatro Falla)"}
                ],
                "grammar_title": "Tradiciones de invierno en el examen CCSE: Nochevieja, Reyes y Carnaval",
                "grammar_text": "En el examen CCSE se preguntan con mucha frecuencia las costumbres españolas de fin de año y febrero: la noche del **31 de diciembre (Nochevieja)** los españoles toman **doce uvas** al son de las doce campanadas de medianoche; la noche del **5 de enero** desfila la **Cabalgata de los Reyes Magos** y el **6 de enero** se comen el **roscón de Reyes** y se abren los regalos; y en **febrero** destacan los **Carnavales de Santa Cruz de Tenerife y de Cádiz**.",
                "grammar_examples": [
                    {"es": "En Nochevieja es tradición en toda España comer doce uvas al compás de las doce campanadas de medianoche.", "en": "On New Year's Eve it is a tradition throughout Spain to eat twelve grapes to the beat of the twelve midnight chimes."},
                    {"es": "Los Carnavales más famosos de España se celebran en febrero en Santa Cruz de Tenerife y en Cádiz.", "en": "The most famous Carnivals in Spain are celebrated in February in Santa Cruz de Tenerife and in Cádiz."}
                ],
                "grammar_tip": "¡Tres preguntas muy frecuentes del CCSE! 1) ¿Qué toman los españoles a medianoche del 31 de diciembre? **Doce uvas**. 2) ¿Cuál es el dulce típico del 6 de enero? El **roscón de Reyes** (y en toda la Navidad el **turrón**). 3) ¿En qué dos ciudades son especialmente famosos los Carnavales? En **Santa Cruz de Tenerife** y en **Cádiz**.",
                "paragraphs": [
                    "El ciclo festivo del invierno en España comienza extraoficialmente la mañana del 22 de diciembre, cuando las voces de los niños del Colegio de San Ildefonso cantan los premios del Sorteo Extraordinario de la Lotería de Navidad (popularmente llamado «El Gordo»). Dos días después, la noche del 24 de diciembre (Nochebuena), las familias se reúnen alrededor de la mesa y del tradicional belén (o nacimiento) para cenar y compartir dulces navideños con siglos de historia como el turrón (de almendra y miel, típico de Jijona y Alicante), el mazapán (de Toledo) y los polvorones y mantecados (de Estepa).",
                    "Tras el día de Navidad (25 de diciembre) y el Día de los Santos Inocentes (28 de diciembre, jornada en la que es costumbre gastar pequeñas bromas o «inocentadas»), llega la noche del 31 de diciembre: la Nochevieja. Unos segundos antes de las doce de la noche, todas las familias y plazas de España miran hacia el reloj de la Real Casa de Correos en la Puerta del Sol de Madrid.",
                    "Con cada una de las doce campanadas que marcan la entrada del Año Nuevo (1 de enero), los españoles comen una a una las «doce uvas de la suerte», una tradición nacida a principios del siglo XX para atraer la prosperidad en los doce meses del año que comienza.",
                    "Sin embargo, la noche más mágica del año para los niños españoles es la del 5 al 6 de enero: la llegada de los Reyes Magos de Oriente (Melchor, Gaspar y Baltasar). La tarde del 5 de enero, espectaculares Cabalgatas de Reyes recorren todas las ciudades y pueblos de España (siendo la de Alcoy, en Alicante, la más antigua documentada), y la mañana del 6 de enero —día festivo en toda España— las familias abren los regalos y desayunan el tradicional «roscón de Reyes» (un bollo en forma de anillo decorado con frutas escarchadas que esconde en su interior una figurita y un haba) con chocolate caliente.",
                    "Pocas semanas después, en el mes de febrero, estalla la alegría del Carnaval. Aunque se celebra en numerosos lugares (como Águilas en Murcia, Badajoz, Sitges o Verín y Xinzo de Limia en Galicia), dos ciudades ostentan la máxima fama internacional: Santa Cruz de Tenerife (famoso por sus desfiles de ritmo caribeño y la deslumbrante gala de elección de la Reina del Carnaval) y Cádiz, donde las «chirigotas», comparsas, coros y cuartetos cantan con ingenio y humor sus coplas satíricas en el Gran Teatro Falla y en las calles."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la tradición que cumplen millones de españoles a las doce de la noche del 31 de diciembre (Nochevieja) para dar la bienvenida al Año Nuevo?",
                        "options": [
                            "Comer doce uvas al compás de las doce campanadas del reloj (especialmente el de la Puerta del Sol)",
                            "Quemar monumentos de cartón piedra en las playas",
                            "Saltar siete olas en el mar Cantábrico",
                            "Lanzar tomates maduros desde los balcones"
                        ],
                        "correctIndex": 0,
                        "explanation": "Comer las doce uvas de la suerte con las doce campanadas de medianoche del 31 de diciembre es la tradición española de Nochevieja."
                    },
                    {
                        "question": "¿En qué dos ciudades españolas son mundialmente famosos los Carnavales que se celebran en el mes de febrero, declarados de Interés Turístico Internacional?",
                        "options": [
                            "En Santa Cruz de Tenerife y en Cádiz",
                            "En Valladolid y en Soria",
                            "En Burgos y en Teruel",
                            "En Huesca y en Palencia"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Carnavales de Santa Cruz de Tenerife y de Cádiz son los dos más famosos de España."
                    },
                    {
                        "question": "¿Qué dulce tradicional con forma de corona o anillo, que esconde sorpresas en su interior, se consume en toda España el 6 de enero para celebrar el Día de los Reyes Magos?",
                        "options": [
                            "El roscón de Reyes",
                            "La mona de Pascua",
                            "El hueso de santo",
                            "La torrija de Cuaresma"
                        ],
                        "correctIndex": 0,
                        "explanation": "El roscón de Reyes es el dulce típico del 6 de enero en toda España."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál es el dulce navideño español por excelencia elaborado principalmente con almendras y miel, muy típico de Jijona y Alicante?",
                        "options": [
                            "El turrón",
                            "El gazpacho",
                            "La paella",
                            "El churro"
                        ],
                        "correctIndex": 0,
                        "explanation": "El turrón (blando de Jijona o duro de Alicante) es el dulce tradicional de la Navidad en España."
                    },
                    {
                        "prompt": "¿Cómo se llaman las agrupaciones musicales populares que cantan coplas llenas de humor e ironía sobre la actualidad durante el Carnaval de Cádiz?",
                        "options": [
                            "Las chirigotas (junto a comparsas, coros y cuartetos)",
                            "Los castellers",
                            "Las rondallas del Pilar",
                            "Los tamborradas"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las chirigotas gaditanas son famosas en toda España por su ingenio humorístico."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En la medianoche del 31 de diciembre (Nochevieja), es tradición en España tomar las doce ___ de la suerte.",
                        "answer": "uvas",
                        "options": ["uvas", "naranjas", "aceitunas", "castañas"],
                        "explanation": "Las doce uvas se toman con las doce campanadas de Nochevieja.",
                        "english": "At midnight on December 31 (New Year's Eve), it is a tradition in Spain to eat the twelve lucky grapes."
                    },
                    {
                        "sentence": "La mañana del 6 de enero los niños abren los regalos de los ___ Magos y se desayuna el tradicional roscón.",
                        "answer": "Reyes",
                        "options": ["Reyes", "Santos", "Alcaldes", "Jueces"],
                        "explanation": "El 6 de enero se celebra la Epifanía o Día de los Reyes Magos.",
                        "english": "On the morning of January 6 children open the gifts from the Three Wise Men and eat the traditional roscón for breakfast."
                    }
                ],
                "ex_dict": {
                    "audioText": "En Nochevieja los españoles comen doce uvas con las campanadas del reloj de la Puerta del Sol.",
                    "english": "On New Year's Eve Spaniards eat twelve grapes with the chimes of the Puerta del Sol clock."
                },
                "ex_sb": {
                    "words": ["Los", "Carnavales", "de", "Santa", "Cruz", "de", "Tenerife", "y", "de", "Cádiz", "son", "muy", "famosos."],
                    "english": "The Carnivals of Santa Cruz de Tenerife and Cádiz are very famous."
                }
            },
            {
                "num": "02",
                "Title": "Primavera de Tradición: Semana Santa, Feria de Abril y Romerías",
                "title": "Primavera de Tradición: Semana Santa, Feria de Abril y Romerías",
                "grammar_slug": "desfilar-en-procesion-por-las-calles-durante-la-semana-santa",
                "story_slug": "primaverayfuego",
                "story_title": "Tambores de Semana Santa, casetas en la Feria de Abril y el Camino del Rocío",
                "objectives": [
                    "Conocer la celebración de la Semana Santa en toda España (procesiones de cofradías con pasos e imágenes escultóricas, desde el fervor de Sevilla y Málaga hasta la sobriedad de Valladolid y Zamora o las tamborradas de Calanda).",
                    "Identificar la Feria de Abril de Sevilla (dos semanas después de Semana Santa), la Fiesta de los Patios de Córdoba (mayo), la Romería del Rocío en Almonte (Huelva) y las fiestas de Moros y Cristianos en el levante (Alcoy).",
                    "Practicar las construcciones «salir en procesión» y «celebrarse dos semanas después de la Semana Santa»."
                ],
                "vocab": [
                    {"lemma": "la Semana Santa (las procesiones y cofradías)", "pos": "noun", "translation": "Holy Week (religious brotherhoods and processions)"},
                    {"lemma": "el paso (o trono) procesional", "pos": "noun", "translation": "processional float carrying wooden sculptures"},
                    {"lemma": "el nazareno (o penitente) y el costalero", "pos": "noun", "translation": "robed brotherhood member and float bearer"},
                    {"lemma": "la saeta", "pos": "noun", "translation": "saeta (emotional flamenco song sung from a balcony during a procession)"},
                    {"lemma": "la Feria de Abril de Sevilla", "pos": "noun", "translation": "April Fair of Seville (casetas, sevillanas, and farolillos)"},
                    {"lemma": "la Romería de El Rocío (Almonte, Huelva)", "pos": "noun", "translation": "Pilgrimage of El Rocío in Huelva (Pentecost)"},
                    {"lemma": "la Fiesta de los Patios de Córdoba (mayo)", "pos": "noun", "translation": "Courtyards Festival of Córdoba (UNESCO Intangible Heritage)"},
                    {"lemma": "las fiestas de Moros y Cristianos (Alcoy, Alicante)", "pos": "noun", "translation": "Moors and Christians festivals"}
                ],
                "grammar_title": "El calendario festivo de la primavera española",
                "grammar_text": "Durante la primavera tienen lugar algunas de las tradiciones más representativas de España: tras las **Fallas de Valencia** (en marzo), entre marzo y abril se celebra en todas las ciudades la **Semana Santa** (con **procesiones** organizadas por **cofradías** y dulces típicos como las **torrijas** y las **monas de Pascua**), seguida dos semanas después por la **Feria de Abril de Sevilla**.",
                "grammar_examples": [
                    {"es": "Durante la Semana Santa, las cofradías sacan en procesión por las calles tallas barrocas de gran valor artístico.", "en": "During Holy Week, brotherhoods carry Baroque wood carvings of great artistic value in procession through the streets."},
                    {"es": "Dos semanas después de la Semana Santa, la ciudad de Sevilla celebra su famosa Feria de Abril.", "en": "Two weeks after Holy Week, the city of Seville celebrates its famous April Fair."}
                ],
                "grammar_tip": "Recuerda para el CCSE: las **procesiones** con «pasos» y cofradías son propias de la **Semana Santa** (en ciudades como Sevilla, Málaga, Valladolid, Zamora o Cuenca); la **Feria de Abril** (con casetas y baile por sevillanas) se celebra en **Sevilla**.",
                "paragraphs": [
                    "Cuando llega la primavera (entre finales de marzo y el mes de abril, según el calendario lunar), toda España vive una de sus tradiciones culturales y artísticas más profundas: la Semana Santa. Desde el Domingo de Ramos hasta el Domingo de Resurrección, centenares de hermandades y cofradías —algunas fundadas hace más de quinientos años— salen en procesión por las calles llevando sobre los hombros de los «costaleros» o «portadores» los «pasos» o «tronos»: auténticos museos ambulantes con esculturas de madera policromada del Siglo de Oro (de imagineros como Gregorio Fernández, Juan de Juni, Martínez Montañés o Francisco Salzillo).",
                    "La Semana Santa ofrece dos estilos llenos de emoción y belleza: en el norte y en la Meseta (en ciudades como Valladolid, Zamora, León o Salamanca) predominan el silencio sobrecogedor y la sobriedad nocturna (mientras en Cuenca suena la Semana de Música Religiosa y en Calanda, Teruel, miles de tambores y bombos «rompen la hora» al mediodía del Viernes Santo); por el contrario, en Andalucía (especialmente en Sevilla y en Málaga) las procesiones se viven entre el aroma del azahar y el incienso, las bandas de cornetas y tambores y el canto desgarrado de una «saeta» flamenca desde un balcón. En las pastelerías de toda España son típicas de estos días las torrijas (rebanadas de pan con leche, huevo, miel y canela) y las monas de Pascua en el levante y Cataluña.",
                    "Apenas dos semanas después del Domingo de Resurrección, Sevilla cambia el recogimiento por el color deslumbrante de la Feria de Abril. Tras la noche del «alumbrao» (el encendido de miles de bombillas en la portada y los farolillos del recinto ferial), más de mil «casetas» se llenan de música de sevillanas, trajes de flamenca con lunares y volantes, paseos de caballos y enganches y alegría compartida.",
                    "En el mes de mayo, Andalucía celebra otras dos citas declaradas de interés universal: en Córdoba tiene lugar la Fiesta de los Patios (Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO), en la que los vecinos del casco histórico abren gratuitamente sus patios blancos repletos de geranios, claveles y jazmines; y en Pentecostés, cerca de un millón de peregrinos a pie, a caballo y en carretas atraviesan los caminos de las marismas de Doñana hasta la aldea de El Rocío (en el municipio de Almonte, Huelva) para celebrar la Romería del Rocío.",
                    "Entretanto, en numerosas poblaciones de la Comunidad Valenciana, Murcia y Andalucía oriental (con especial fama en Alcoy, Alicante, en torno al 23 de abril) se celebran los espectaculares desfiles históricos de las fiestas de Moros y Cristianos."
                ],
                "questions": [
                    {
                        "question": "¿En qué celebración tradicional española salen a las calles las cofradías y hermandades acompañando en procesión los «pasos» o «tronos» con esculturas religiosas?",
                        "options": [
                            "En la Semana Santa",
                            "En la Nochevieja",
                            "En la Tomatina",
                            "En el Día de la Constitución"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las procesiones de cofradías con pasos e imágenes escultóricas son la manifestación principal de la Semana Santa en España."
                    },
                    {
                        "question": "¿En qué ciudad andaluza se celebra cada primavera, dos semanas después de la Semana Santa, la famosa Feria de Abril con casetas, farolillos y baile por sevillanas?",
                        "options": [
                            "En Sevilla",
                            "En Lugo",
                            "En Santander",
                            "En Logroño"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Feria de Abril es la gran fiesta de primavera de la ciudad de Sevilla."
                    },
                    {
                        "question": "¿En qué provincia andaluza (municipio de Almonte, junto al Parque Nacional de Doñana) tiene lugar cada primavera la multitudinaria Romería de El Rocío?",
                        "options": [
                            "En Huelva",
                            "En Jaén",
                            "En Almería",
                            "En Soria"
                        ],
                        "correctIndex": 0,
                        "explanation": "La aldea de El Rocío pertenece al municipio de Almonte, en la provincia de Huelva."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué ciudad andaluza celebra cada mes de mayo la famosa «Fiesta de los Patios», en la que los vecinos decoran sus patios con cientos de macetas de flores y los abren al público?",
                        "options": [
                            "Córdoba",
                            "Oviedo",
                            "Pamplona",
                            "Bilbao"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Fiesta de los Patios de Córdoba (en mayo) es Patrimonio Cultural Inmaterial de la Humanidad."
                    },
                    {
                        "prompt": "¿Cuál es el dulce tradicional elaborado con pan, leche, huevo, canela y miel o azúcar que se consume en toda España durante la Semana Santa?",
                        "options": [
                            "Las torrijas",
                            "Las doce uvas",
                            "El roscón de Reyes",
                            "Los panellets"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las torrijas son el postre más típico de la Semana Santa española."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Durante la Semana ___, las cofradías recorren las calles de las ciudades españolas en procesión.",
                        "answer": "Santa",
                        "options": ["Santa", "Blanca", "Verde", "Vaciada"],
                        "explanation": "La Semana Santa se celebra en toda España con procesiones de gran valor artístico y tradicional.",
                        "english": "During Holy Week, brotherhoods walk through the streets of Spanish cities in procession."
                    },
                    {
                        "sentence": "Dos semanas después de la Semana Santa, la ciudad de Sevilla celebra su famosa Feria de ___.",
                        "answer": "Abril",
                        "options": ["Abril", "Enero", "Agosto", "Noviembre"],
                        "explanation": "La Feria de Abril se celebra en Sevilla en primavera.",
                        "english": "Two weeks after Holy Week, the city of Seville celebrates its famous April Fair."
                    }
                ],
                "ex_dict": {
                    "audioText": "Durante la Semana Santa las cofradías salen en procesión y después se celebra la Feria de Abril en Sevilla.",
                    "english": "During Holy Week the brotherhoods go out in procession and afterwards the April Fair is celebrated in Seville."
                },
                "ex_sb": {
                    "words": ["La", "Fiesta", "de", "los", "Patios", "se", "celebra", "en", "mayo", "en", "Córdoba."],
                    "english": "The Courtyards Festival is celebrated in May in Córdoba."
                }
            },
            {
                "num": "03",
                "Title": "Las Fiestas del Verano: San Juan, San Fermín y la Tomatina",
                "title": "Las Fiestas del Verano: San Juan, San Fermín y la Tomatina",
                "grammar_slug": "encender-hogueras-en-las-playas-la-noche-de-san-juan",
                "story_slug": "veranoysanfermin",
                "story_title": "Fuego en las playas el 23 de junio, pañuelos rojos en Pamplona y tomates en Buñol",
                "objectives": [
                    "Recordar las grandes fiestas del verano español: la noche de las Hogueras de San Juan (del 23 al 24 de junio, especialmente en Alicante, A Coruña y todas las costas), los Sanfermines de Pamplona (del 6 al 14 de julio), el Apóstol Santiago en Galicia (25 de julio), la Semana Grande de Bilbao y San Sebastián (agosto) y la Tomatina de Buñol en Valencia (último miércoles de agosto).",
                    "Conocer la tradición otoñal del Día de Todos los Santos (1 de noviembre, con los huesos de santo, buñuelos y castañas).",
                    "Practicar las construcciones «encender hogueras en la playa» y «celebrarse el último miércoles de agosto»."
                ],
                "vocab": [
                    {"lemma": "las Hogueras de San Juan (noche del 23 al 24 de junio)", "pos": "noun", "translation": "Bonfires of Saint John (Midsummer's Eve)"},
                    {"lemma": "las fiestas de San Fermín (Pamplona, 6–14 de julio)", "pos": "noun", "translation": "San Fermín festival in Pamplona (the chupinazo and encierros)"},
                    {"lemma": "el Día del Apóstol Santiago (25 de julio, Día de Galicia)", "pos": "noun", "translation": "Saint James's Day (July 25)"},
                    {"lemma": "el Descenso Internacional del Sella (Asturias, agosto)", "pos": "noun", "translation": "International Descent of the Sella River in canoes"},
                    {"lemma": "la Semana Grande (Aste Nagusia en Bilbao y San Sebastián)", "pos": "noun", "translation": "Big Week summer festival in August"},
                    {"lemma": "la Tomatina de Buñol (Valencia, último miércoles de agosto)", "pos": "noun", "translation": "La Tomatina tomato-throwing festival in Buñol"},
                    {"lemma": "las Fiestas del Pilar (Zaragoza, 12 de octubre)", "pos": "noun", "translation": "Pillar Festival in Zaragoza"},
                    {"lemma": "el Día de Todos los Santos (1 de noviembre: huesos de santo y panellets)", "pos": "noun", "translation": "All Saints' Day (November 1)"}
                ],
                "grammar_title": "El calendario estival: de la noche de San Juan a la Tomatina de Buñol",
                "grammar_text": "En el examen CCSE suelen preguntarse tres fiestas de verano muy concretas: la noche del **23 al 24 de junio** se encienden las **Hogueras de San Juan** en las playas de toda España (y son las fiestas mayores de **Alicante** y **A Coruña**); del **6 al 14 de julio** se celebran los **Sanfermines** en **Pamplona (Navarra)**; y el último miércoles de agosto se celebra **la Tomatina** en el pueblo valenciano de **Buñol**.",
                "grammar_examples": [
                    {"es": "La noche del 23 de junio se encienden hogueras en las playas para dar la bienvenida al verano en la fiesta de San Juan.", "en": "On the night of June 23 bonfires are lit on the beaches to welcome summer in the festival of Saint John."},
                    {"es": "El último miércoles de agosto se celebra en la localidad valenciana de Buñol la famosa fiesta de la Tomatina.", "en": "On the last Wednesday of August the famous Tomatina festival is held in the Valencian town of Buñol."}
                ],
                "grammar_tip": "Recuerda para el CCSE: **Hogueras de San Juan** = noche del 23 al 24 de junio (Alicante y costas); **San Fermín** = 7 de julio en **Pamplona**; **La Tomatina** = agosto en **Buñol (Valencia)**.",
                "paragraphs": [
                    "La llegada del solsticio de verano se celebra en toda España en la noche más corta y mágica del año: la noche de San Juan, del 23 al 24 de junio. En las playas del Mediterráneo, del Atlántico y del Cantábrico (con especial esplendor en ciudades como A Coruña o Málaga), miles de personas encienden hogueras en la arena a medianoche para quemar los malos recuerdos y saltar sobre las olas. En la ciudad de Alicante, las Hogueras de San Juan (*les Fogueres de Sant Joan*) constituyen sus fiestas mayores oficiales, con grandes monumentos artísticos que arden la noche del 24 de junio.",
                    "En julio, el protagonismo viaja al norte. Del 6 al 14 de julio, todo el mundo mira hacia Pamplona (capital de la Comunidad Foral de Navarra), donde los participantes vestidos de blanco con pañuelo y faja rojos celebran las fiestas de San Fermín desde el lanzamiento del cohete («el chupinazo») en la plaza del Ayuntamiento hasta el canto final del *Pobre de mí*. Y el 25 de julio, Santiago de Compostela celebra con espectaculares fuegos artificiales en la plaza del Obradoiro la festividad del Apóstol Santiago, patrón de España y Día Nacional de Galicia.",
                    "Agosto es el mes por excelencia de las fiestas patronales y verbenas en los más de ocho mil pueblos de España. En el norte destacan el Descenso Internacional del Sella en piragua (en Asturias), la fiesta de la Virgen Blanca en Vitoria y las Semanas Grandes (*Aste Nagusia*) de San Sebastián y de Bilbao (con su simpático símbolo *Marijaia*). En el Mediterráneo, Elche representa en su basílica el drama sacro-lírico medieval del *Misteri d'Elx* (Patrimonio de la Humanidad), y el último miércoles de agosto miles de jóvenes de todo el mundo se dan cita en la localidad valenciana de Buñol para participar en «la Tomatina», una divertida batalla pacífica en la que se lanzan toneladas de tomates maduros.",
                    "En septiembre y octubre toman el relevo las Fiestas de la Vendimia (como las de Jerez y Logroño), las fiestas de la Mercè en Barcelona (24 de septiembre) y las grandes Fiestas del Pilar de Zaragoza en torno al 12 de octubre, con su multitudinaria Ofrenda de Flores a la Virgen del Pilar.",
                    "Finalmente, el 1 de noviembre toda España celebra un día festivo de recuerdo familiar: el Día de Todos los Santos, en el que es tradición llevar flores a los cementerios, representar en los teatros *Don Juan Tenorio* de José Zorrilla y degustar dulces de otoño como los «huesos de santo» (de mazapán y yema), los buñuelos de viento, los «panellets» (en Cataluña, Baleares y Valencia) y las castañas asadas del «magosto» o la «castanyada»."
                ],
                "questions": [
                    {
                        "question": "¿En qué fecha se celebra en las playas de España (y como fiesta mayor oficial de la ciudad de Alicante) la fiesta de las Hogueras de San Juan?",
                        "options": [
                            "La noche del 23 al 24 de junio, coincidiendo con el inicio del verano",
                            "El 31 de diciembre en invierno",
                            "El 1 de noviembre en otoño",
                            "El 6 de enero"
                        ],
                        "correctIndex": 0,
                        "explanation": "La noche del 23 al 24 de junio se celebran las Hogueras de San Juan para dar la bienvenida al verano."
                    },
                    {
                        "question": "¿En qué localidad de la provincia de Valencia se celebra cada año, el último miércoles de agosto, la famosa fiesta de «la Tomatina»?",
                        "options": [
                            "En Buñol (Valencia)",
                            "En Astorga (León)",
                            "En Jaca (Huesca)",
                            "En Tarifa (Cádiz)"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Tomatina se celebra el último miércoles de agosto en el municipio valenciano de Buñol."
                    },
                    {
                        "question": "¿En qué ciudad se celebran en torno al 12 de octubre las famosas Fiestas del Pilar, con su tradicional Ofrenda de Flores?",
                        "options": [
                            "En Zaragoza (Aragón)",
                            "En Vigo (Galicia)",
                            "En Badajoz (Extremadura)",
                            "En Mahón (Baleares)"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Fiestas del Pilar son las fiestas mayores de la ciudad de Zaragoza."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué día festivo nacional se celebra en toda España el 1 de noviembre, en el que es costumbre visitar los cementerios y comer dulces como los «huesos de santo», buñuelos o «panellets»?",
                        "options": [
                            "El Día de Todos los Santos",
                            "El Día del Trabajo",
                            "El Día de la Constitución",
                            "El Día de San Fermín"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 1 de noviembre es el Día de Todos los Santos, festivo nacional en toda España."
                    },
                    {
                        "prompt": "¿Cómo se viste tradicionalmente la gente para participar en las fiestas de San Fermín en Pamplona del 6 al 14 de julio?",
                        "options": [
                            "Con camisa y pantalón blancos y un pañuelo y faja rojos",
                            "Con frac negro y sombrero de copa",
                            "Con traje de esquí alpino",
                            "Con túnica morada de terciopelo"
                        ],
                        "correctIndex": 0,
                        "explanation": "El atuendo tradicional de los Sanfermines de Pamplona es ropa blanca con el pañuelo («pañuelico») y la faja de color rojo."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La noche del 23 al 24 de junio se encienden hogueras en las playas españolas para celebrar la noche de San ___.",
                        "answer": "Juan",
                        "options": ["Juan", "Fermín", "José", "Isidro"],
                        "explanation": "La noche del 23 al 24 de junio es la Noche de San Juan.",
                        "english": "On the night of June 23 to 24, bonfires are lit on Spanish beaches to celebrate Saint John's Eve."
                    },
                    {
                        "sentence": "En la localidad valenciana de Buñol se celebra en agosto la famosa fiesta de la ___.",
                        "answer": "Tomatina",
                        "options": ["Tomatina", "Fabada", "Sardana", "Muñeira"],
                        "explanation": "La Tomatina de Buñol es una de las fiestas estivales españolas más conocidas en el extranjero.",
                        "english": "In the Valencian town of Buñol, the famous Tomatina festival is celebrated in August."
                    }
                ],
                "ex_dict": {
                    "audioText": "La noche de San Juan se celebra en junio con hogueras en las playas y la Tomatina se celebra en Buñol.",
                    "english": "Saint John's Eve is celebrated in June with bonfires on the beaches and the Tomatina is celebrated in Buñol."
                },
                "ex_sb": {
                    "words": ["El", "uno", "de", "noviembre", "se", "celebra", "el", "Día", "de", "Todos", "los", "Santos."],
                    "english": "On the first of November All Saints' Day is celebrated."
                }
            },
            {
                "num": "04",
                "Title": "El Calendario Laboral de Festivos Nacionales en España",
                "title": "El Calendario Laboral de Festivos Nacionales en España",
                "grammar_slug": "ser-dia-festivo-no-laborable-en-todo-el-territorio-nacional",
                "story_slug": "fiestasnacionalesylaborales",
                "story_title": "Catorce días festivos al año: cómo se reparten las fiestas nacionales, autonómicas y locales",
                "objectives": [
                    "Saber que el calendario laboral español establece un máximo de 14 días festivos retribuidos y no recuperables al año (de los cuales 2 son fiestas locales de cada municipio).",
                    "Memorizar las fechas de los principales festivos nacionales fijos: 1 de enero (Año Nuevo), 6 de enero (Epifanía/Reyes), Viernes Santo, 1 de mayo (Fiesta del Trabajo), 15 de agosto (Asunción), 12 de octubre (Fiesta Nacional de España), 1 de noviembre (Todos los Santos), 6 de diciembre (Día de la Constitución Española), 8 de diciembre (Inmaculada Concepción) y 25 de diciembre (Navidad).",
                    "Practicar las construcciones «ser festivo de ámbito nacional» y «fijar dos fiestas de carácter local»."
                ],
                "vocab": [
                    {"lemma": "el calendario laboral (14 días festivos al año)", "pos": "noun", "translation": "official working calendar (14 paid public holidays per year)"},
                    {"lemma": "el festivo nacional no sustituible", "pos": "noun", "translation": "non-replaceable national public holiday"},
                    {"lemma": "el 1 de mayo (Fiesta del Trabajo)", "pos": "noun", "translation": "May 1 (International Workers' Day / Labor Day)"},
                    {"lemma": "el 12 de octubre (Fiesta Nacional de España)", "pos": "noun", "translation": "October 12 (National Day of Spain)"},
                    {"lemma": "el 6 de diciembre (Día de la Constitución Española)", "pos": "noun", "translation": "December 6 (Spanish Constitution Day)"},
                    {"lemma": "el 8 de diciembre (La Inmaculada Concepción)", "pos": "noun", "translation": "December 8 (Feast of the Immaculate Conception)"},
                    {"lemma": "el «puente» festivo (el puente de diciembre)", "pos": "noun", "translation": "long weekend / bridge holiday (especially around December 6 and 8)"},
                    {"lemma": "las dos fiestas locales municipales", "pos": "noun", "translation": "the two local municipal holidays set by each town hall"}
                ],
                "grammar_title": "El Estatuto de los Trabajadores y los 14 días festivos anuales",
                "grammar_text": "Según el **artículo 37.2 del Estatuto de los Trabajadores**, las fiestas laborales en España tienen carácter retribuido y no recuperable y **no podrán exceder de catorce (14) al año**, de las cuales **dos (2) serán locales** (fijadas por el ayuntamiento de cada municipio). Entre las fiestas nacionales cívicas destacan el **1 de mayo**, el **12 de octubre** y el **6 de diciembre**.",
                "grammar_examples": [
                    {"es": "En España el calendario laboral comprende catorce días festivos al año, de los cuales dos son fiestas locales.", "en": "In Spain the working calendar comprises fourteen public holidays per year, of which two are local holidays."},
                    {"es": "El 6 de diciembre es día festivo en toda España porque se conmemora el referéndum de la Constitución de 1978.", "en": "December 6 is a public holiday throughout Spain because it commemorates the referendum on the 1978 Constitution."}
                ],
                "grammar_tip": "¡Repaso de fechas clave para el CCSE! **1 de mayo** = Fiesta del Trabajo; **12 de octubre** = Fiesta Nacional de España; **1 de noviembre** = Todos los Santos; **6 de diciembre** = Día de la Constitución; **25 de diciembre** = Navidad.",
                "paragraphs": [
                    "¿Cuántos días festivos oficiales tienen al año los trabajadores en España y quién los decide? De acuerdo con el artículo 37 del Estatuto de los Trabajadores, cada año existen en España 14 días festivos laborales, todos ellos retribuidos (pagados) y no recuperables.",
                    "Esos 14 días festivos se articulan en tres niveles que reflejan la organización territorial del Estado: en primer lugar, las fiestas de ámbito nacional (entre 8 y 9 días obligatorios en todo el país); en segundo lugar, las fiestas fijadas por cada Comunidad Autónoma (entre 3 y 4 días, incluido el Día de la Comunidad Autónoma, como el 28 de febrero en Andalucía, el 23 de abril en Aragón y Castilla y León, el 2 de mayo en Madrid, el 30 de mayo en Canarias, el 25 de julio en Galicia, el 11 de septiembre en Cataluña o el 9 de octubre en la Comunidad Valenciana); y en tercer lugar, 2 fiestas locales decididas por cada Ayuntamiento (como el 15 de mayo, San Isidro, en la ciudad de Madrid).",
                    "Dentro de los festivos nacionales que se celebran sin excepción en toda España destacan tres grandes conmemoraciones cívicas y laborales que suelen preguntarse en el examen CCSE: el 1 de mayo se celebra la Fiesta del Trabajo (Día Internacional de los Trabajadores); el 12 de octubre se celebra la Fiesta Nacional de España (con el tradicional desfile de las Fuerzas Armadas en Madrid presidido por el Rey); y el 6 de diciembre se celebra el Día de la Constitución Española, en aniversario del referéndum del 6 de diciembre de 1978.",
                    "A ellos se suman los festivos nacionales de origen tradicional o religioso: el 1 de enero (Año Nuevo), el 6 de enero (Epifanía del Señor o Día de los Reyes Magos), el Viernes Santo (en marzo o abril), el 15 de agosto (Asunción de la Virgen, en pleno corazón de las fiestas de verano), el 1 de noviembre (Todos los Santos), el 8 de diciembre (la Inmaculada Concepción) y el 25 de diciembre (Natividad del Señor o Navidad).",
                    "En el vocabulario cotidiano español existe además una palabra muy popular: «hacer puente». Cuando un día festivo cae en martes o en jueves —o cuando se unen en la misma semana el 6 de diciembre (Día de la Constitución) y el 8 de diciembre (la Inmaculada)—, muchos ciudadanos toman libre los días intermedios formando el famoso «puente de diciembre» o «puente de la Constitución»."
                ],
                "questions": [
                    {
                        "question": "¿Cuántos días festivos laborales retribuidos al año existen en España según el Estatuto de los Trabajadores, y cuántos de ellos son fiestas locales de cada municipio?",
                        "options": [
                            "14 días festivos al año en total, de los cuales 2 son fiestas locales de cada municipio",
                            "30 días festivos nacionales y 10 locales",
                            "Solo 3 días festivos al año en total",
                            "No existen días festivos oficiales en España"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Estatuto de los Trabajadores fija en 14 el número total de días festivos anuales, siendo 2 de ellos de carácter local."
                    },
                    {
                        "question": "¿Qué se celebra en toda España el día 1 de mayo, festivo nacional?",
                        "options": [
                            "La Fiesta del Trabajo (Día Internacional de los Trabajadores)",
                            "El Día de la Constitución Española",
                            "El Día de Todos los Santos",
                            "El Día de los Reyes Magos"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 1 de mayo es el Día Internacional de los Trabajadores o Fiesta del Trabajo."
                    },
                    {
                        "question": "¿Qué dos días festivos nacionales se celebran muy seguidos en la primera semana de diciembre, dando lugar al conocido «puente de diciembre»?",
                        "options": [
                            "El 6 de diciembre (Día de la Constitución Española) y el 8 de diciembre (La Inmaculada Concepción)",
                            "El 1 de mayo y el 15 de agosto",
                            "El 12 de octubre y el 1 de noviembre",
                            "El 23 de abril y el 24 de junio"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 6 de diciembre (Día de la Constitución) y el 8 de diciembre (Inmaculada Concepción) son ambos festivos nacionales."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué fecha se celebra la Fiesta Nacional de España en todo el país?",
                        "options": [
                            "El 12 de octubre",
                            "El 1 de mayo",
                            "El 6 de diciembre",
                            "El 15 de agosto"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Fiesta Nacional de España se celebra cada año el 12 de octubre."
                    },
                    {
                        "prompt": "¿Qué se conmemora en España cada 6 de diciembre?",
                        "options": [
                            "El Día de la Constitución Española de 1978",
                            "El ingreso de España en las Naciones Unidas",
                            "El inicio del curso escolar",
                            "El solsticio de verano"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 6 de diciembre conmemora la aprobación en referéndum de la Constitución Española de 1978."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En España existen catorce días festivos al año, de los cuales ___ son fiestas locales fijadas por cada ayuntamiento.",
                        "answer": "dos",
                        "options": ["dos", "diez", "doce", "ocho"],
                        "explanation": "De los 14 festivos anuales, 2 son fiestas locales de cada municipio.",
                        "english": "In Spain there are fourteen public holidays per year, of which two are local holidays set by each town hall."
                    },
                    {
                        "sentence": "El 1 de mayo es festivo en toda España porque se celebra la Fiesta del ___.",
                        "answer": "Trabajo",
                        "options": ["Trabajo", "Libro", "Cine", "Mar"],
                        "explanation": "El 1 de mayo es la Fiesta del Trabajo.",
                        "english": "May 1 is a public holiday throughout Spain because Labor Day is celebrated."
                    }
                ],
                "ex_dict": {
                    "audioText": "El seis de diciembre se celebra el Día de la Constitución y el doce de octubre la Fiesta Nacional.",
                    "english": "On December sixth Constitution Day is celebrated and on October twelfth the National Day."
                },
                "ex_sb": {
                    "words": ["El", "uno", "de", "mayo", "se", "celebra", "la", "Fiesta", "del", "Trabajo", "en", "España."],
                    "english": "On the first of May Labor Day is celebrated in Spain."
                }
            },
            {
                "num": "05",
                "Title": "El Deporte en España: Grandes Campeones y Competiciones",
                "title": "El Deporte en España: Grandes Campeones y Competiciones",
                "grammar_slug": "proclamarse-campeon-del-mundo-y-destacar-en-el-deporte",
                "story_slug": "deporteespanol",
                "story_title": "De la raqueta de Rafa Nadal y Carlos Alcaraz a los balones de oro del deporte español",
                "objectives": [
                    "Identificar la disciplina deportiva de los grandes campeones españoles preguntados en el CCSE: Rafael Nadal y Carlos Alcaraz (tenis), Pau y Marc Gasol (baloncesto), Fernando Alonso y Carlos Sainz (automovilismo / Fórmula 1 y rallies), Marc Márquez y Ángel Nieto (motociclismo), Miguel Induráin y Alberto Contador (ciclismo), Severiano Ballesteros y Jon Rahm (golf), Mireia Belmonte y Teresa Perales (natación), Carolina Marín (bádminton) y Alexia Putellas y Aitana Bonmatí (fútbol).",
                    "Recordar que las selecciones españolas masculina (2010) y femenina (2023) de fútbol y la selección de baloncesto (2006 y 2019) han sido campeonas del mundo, y conocer el Consejo Superior de Deportes (CSD) y el Comité Olímpico Español (COE).",
                    "Practicar las construcciones «destacar en la disciplina de» y «proclamarse campeón del mundo»."
                ],
                "vocab": [
                    {"lemma": "Rafael Nadal y Carlos Alcaraz (tenis)", "pos": "noun", "translation": "Rafael Nadal and Carlos Alcaraz (world-famous Spanish tennis champions)"},
                    {"lemma": "Pau Gasol y Marc Gasol (baloncesto)", "pos": "noun", "translation": "Pau and Marc Gasol (Spanish NBA and World Cup basketball champions)"},
                    {"lemma": "Fernando Alonso y Carlos Sainz (automovilismo / Fórmula 1)", "pos": "noun", "translation": "Fernando Alonso and Carlos Sainz (motorsport / Formula 1 and rally champions)"},
                    {"lemma": "Miguel Induráin (ciclismo, 5 Tours de Francia) y La Vuelta a España", "pos": "noun", "translation": "Miguel Induráin (cycling legend) and the Vuelta a España"},
                    {"lemma": "Mireia Belmonte (natación) y Teresa Perales (natación paralímpica)", "pos": "noun", "translation": "Mireia Belmonte and Teresa Perales (Olympic and Paralympic swimming champions)"},
                    {"lemma": "Carolina Marín (bádminton) y Severiano Ballesteros (golf)", "pos": "noun", "translation": "Carolina Marín (badminton champion) and Seve Ballesteros (golf legend)"},
                    {"lemma": "Alexia Putellas, Aitana Bonmatí y Andrés Iniesta (fútbol)", "pos": "noun", "translation": "Putellas, Bonmatí (Ballon d'Or winners), and Iniesta (Spanish football stars)"},
                    {"lemma": "el Consejo Superior de Deportes (CSD) y el Comité Olímpico Español (COE)", "pos": "noun", "translation": "Higher Sports Council and Spanish Olympic Committee"}
                ],
                "grammar_title": "El deporte en la Tarea 4 y 5 del CCSE: relacionar deportista y deporte",
                "grammar_text": "En el examen CCSE aparecen con mucha frecuencia preguntas que piden asociar el nombre de un deportista español con su deporte: **Rafael Nadal, Carlos Alcaraz, Arantxa Sánchez Vicario, Conchita Martínez y Garbiñe Muguruza** = **tenis**; **Pau y Marc Gasol** = **baloncesto**; **Fernando Alonso** = **Fórmula 1 (automovilismo)**; **Miguel Induráin** = **ciclismo**; **Mireia Belmonte y Teresa Perales** = **natación**; **Carolina Marín** = **bádminton**.",
                "grammar_examples": [
                    {"es": "El mallorquín Rafael Nadal y el murciano Carlos Alcaraz son dos grandes campeones del tenis mundial.", "en": "The Mallorcan Rafael Nadal and the Murcian Carlos Alcaraz are two great champions of world tennis."},
                    {"es": "Los hermanos catalanes Pau y Marc Gasol lideraron los mayores éxitos de la historia del baloncesto español.", "en": "The Catalan brothers Pau and Marc Gasol led the greatest successes in the history of Spanish basketball."}
                ],
                "grammar_tip": "¡Tabla rápida de campeones para el CCSE! **Tenis**: Rafa Nadal, Carlos Alcaraz, Garbiñe Muguruza. **Baloncesto**: Pau y Marc Gasol. **Fórmula 1**: Fernando Alonso. **Ciclismo**: Miguel Induráin. **Natación**: Mireia Belmonte y Teresa Perales (Premio Princesa de Asturias). **Bádminton**: Carolina Marín.",
                "paragraphs": [
                    "Desde el punto de vista de la participación ciudadana y de los éxitos internacionales, el deporte es uno de los grandes fenómenos sociales de la España contemporánea. El artículo 43.3 de la Constitución encomienda a los poderes públicos fomentar la educación física y el deporte, tarea que impulsa a nivel estatal el Consejo Superior de Deportes (CSD), junto al Comité Olímpico Español (COE) y el Comité Paralímpico Español (CPE). El punto de inflexión histórico del deporte español fueron los Juegos Olímpicos y Paralímpicos de Barcelona 1992, donde España conquistó 22 medallas olímpicas (13 de oro).",
                    "El deporte con mayor número de aficionados y licencias federativas en España es el fútbol (organizado profesionalmente en «LaLiga»). La selección española masculina proclamó a España campeona del mundo por primera vez en Sudáfrica 2010 (con el inolvidable gol de Andrés Iniesta en la final) y ha ganado cuatro Eurocopas (1964, 2008, 2012 y 2024), mientras que la selección española femenina se proclamó campeona del mundo en 2023 en Sídney, liderada por las ganadoras del Balón de Oro Alexia Putellas y Aitana Bonmatí. Además, clubes como el Real Madrid y el FC Barcelona se cuentan entre los más laureados del planeta.",
                    "El segundo gran deporte de equipo en España es el baloncesto (con la Liga ACB): impulsada por la llamada «Generación de Oro» de los hermanos catalanes Pau Gasol y Marc Gasol (ambos campeones de la NBA estadounidense y Premios Princesa de Asturias de los Deportes), Ricky Rubio, Juan Carlos Navarro o Rudy Fernández, España ha sido dos veces campeona del mundo de baloncesto (2006 y 2019) y cuatro veces campeona de Europa (además de los cuatro títulos europeos de la selección femenina liderada por Amaya Valdemoro y Alba Torrens).",
                    "En los deportes individuales, ningún nombre simboliza mejor los valores de esfuerzo, respeto y humildad que el tenista mallorquín Rafael Nadal (nacido en Manacor, Mallorca), ganador de 22 torneos de Grand Slam (incluidos 14 títulos de Roland Garros) y dos oros olímpicos, cuyo testigo en la cima del tenis mundial ha recogido el joven murciano Carlos Alcaraz, dentro de una tradición tenística en la que brillaron también Manolo Santana, Arantxa Sánchez Vicario, Conchita Martínez, Juan Carlos Ferrero y Garbiñe Muguruza.",
                    "El palmarés español se completa con leyendas del ciclismo como el navarro Miguel Induráin (ganador de cinco Tours de Francia consecutivos entre 1991 y 1995, además de celebrarse cada año en nuestras carreteras La Vuelta Ciclista a España); del motor, como el asturiano Fernando Alonso (bicampeón mundial de Fórmula 1), Carlos Sainz (en rallies) y Marc Márquez y Ángel Nieto (en motociclismo); del golf, con el cántabro Severiano Ballesteros y el vasco Jon Rahm; de la natación, con la campeona olímpica Mireia Belmonte y la nadadora paralímpica aragonesa Teresa Perales (ganadora de 28 medallas paralímpicas y Premio Princesa de Asturias); del bádminton, con la onubense Carolina Marín; y del piragüismo, con Saúl Craviotto y David Cal."
                ],
                "questions": [
                    {
                        "question": "¿En qué deportes han destacado mundialmente los campeones españoles Rafael Nadal, Pau Gasol y Fernando Alonso, respectivamente?",
                        "options": [
                            "Rafael Nadal en tenis, Pau Gasol en baloncesto y Fernando Alonso en automovilismo (Fórmula 1)",
                            "Rafael Nadal en ciclismo, Pau Gasol en natación y Fernando Alonso en golf",
                            "Los tres son jugadores de balonmano",
                            "Rafael Nadal en esquí, Pau Gasol en esgrima y Fernando Alonso en remo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Rafael Nadal (al igual que Carlos Alcaraz) es campeón de tenis; Pau Gasol, de baloncesto; y Fernando Alonso, bicampeón mundial de Fórmula 1."
                    },
                    {
                        "question": "¿Qué deportista navarro hizo historia en el ciclismo mundial al ganar cinco veces consecutivas el Tour de Francia entre 1991 y 1995?",
                        "options": [
                            "Miguel Induráin",
                            "Severiano Ballesteros",
                            "Andrés Iniesta",
                            "Marc Márquez"
                        ],
                        "correctIndex": 0,
                        "explanation": "El ciclista navarro Miguel Induráin ganó cinco Tours de Francia consecutivos y el Premio Príncipe de Asturias de los Deportes."
                    },
                    {
                        "question": "¿En qué deporte han conquistado el campeonato del mundo tanto la selección española masculina (en 2010) como la selección española femenina (en 2023), contando con ganadoras del Balón de Oro como Alexia Putellas y Aitana Bonmatí?",
                        "options": [
                            "En el fútbol",
                            "En el hockey sobre hielo",
                            "En el béisbol",
                            "En el rugby"
                        ],
                        "correctIndex": 0,
                        "explanation": "España es campeona del mundo de fútbol tanto en categoría masculina (2010) como femenina (2023)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué disciplina deportiva han ganado medallas olímpicas y paralímpicas las deportistas españolas Mireia Belmonte y Teresa Perales?",
                        "options": [
                            "En natación",
                            "En hípica",
                            "En tiro con arco",
                            "En halterofilia"
                        ],
                        "correctIndex": 0,
                        "explanation": "Mireia Belmonte es campeona olímpica de natación y la aragonesa Teresa Perales ha ganado 28 medallas en natación paralímpica."
                    },
                    {
                        "prompt": "¿Qué organismo público adscrito al Ministerio de Educación, Formación Profesional y Deportes coordina la política deportiva estatal en España?",
                        "options": [
                            "El Consejo Superior de Deportes (CSD)",
                            "El Consejo de Estado",
                            "El Instituto Geográfico Nacional",
                            "La Real Academia de Bellas Artes"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Consejo Superior de Deportes (CSD) es el órgano estatal encargado del deporte en España."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El deportista mallorquín Rafael ___ y el murciano Carlos Alcaraz son grandes campeones mundiales de tenis.",
                        "answer": "Nadal",
                        "options": ["Nadal", "Gasol", "Alonso", "Induráin"],
                        "explanation": "Rafael Nadal es uno de los mejores tenistas de la historia.",
                        "english": "The Mallorcan athlete Rafael Nadal and the Murcian Carlos Alcaraz are great world tennis champions."
                    },
                    {
                        "sentence": "Los hermanos Pau y Marc ___ son dos leyendas de la historia del baloncesto español.",
                        "answer": "Gasol",
                        "options": ["Gasol", "Márquez", "Sainz", "Rahm"],
                        "explanation": "Pau y Marc Gasol lideraron a la selección española de baloncesto campeona del mundo.",
                        "english": "Brothers Pau and Marc Gasol are two legends in the history of Spanish basketball."
                    }
                ],
                "ex_dict": {
                    "audioText": "Rafael Nadal destaca en el tenis, Pau Gasol en el baloncesto y Fernando Alonso en la Fórmula Uno.",
                    "english": "Rafael Nadal excels in tennis, Pau Gasol in basketball, and Fernando Alonso in Formula One."
                },
                "ex_sb": {
                    "words": ["La", "selección", "española", "femenina", "de", "fútbol", "ganó", "el", "Mundial", "en", "dos", "mil", "veintitrés."],
                    "english": "The Spanish women's national football team won the World Cup in twenty twenty-three."
                }
            }
        ]
    }
]


def main():
    for u in UNITS_25_26_27:
        emit_unit_from_dict(u)


if __name__ == "__main__":
    main()
