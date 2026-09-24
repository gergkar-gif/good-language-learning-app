#!/usr/bin/env python3
"""Generate Spain Citizenship (CCSE) Units 13, 14, and 15 for es-es B1 track."""

from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict

UNITS_13_14_15 = [
    # =========================================================================
    # UNIT 13: Derechos y Libertades Fundamentales (unit_num=49, b1-derechos)
    # =========================================================================
    {
        "slug": "derechos",
        "unit_num": 49,
        "title": "Derechos y Libertades Fundamentales",
        "description": "Vida, libertad personal, inviolabilidad del domicilio, libertad de expresión, reunión, huelga y derechos sociales.",
        "Badge": "Derechos Fundamentales",
        "lessons": [
            {
                "num": "01",
                "Title": "La Dignidad Humana, la Vida y la Libertad Personal",
                "title": "La Dignidad Humana, la Vida y la Libertad Personal",
                "grammar_slug": "quedar-abolido-plazo-maximo",
                "story_slug": "vidalibertad",
                "story_title": "Setenta y dos horas y una línea roja constitucional",
                "objectives": [
                    "Comprender los artículos 10, 12, 15 y 17 de la Constitución Española sobre dignidad, mayoría de edad, vida y libertad.",
                    "Recordar la abolición de la pena de muerte y el límite máximo de 72 horas para la detención preventiva.",
                    "Dominar las construcciones «quedar abolido/a» y «en el plazo máximo de»."
                ],
                "vocab": [
                    {"lemma": "la dignidad humana", "pos": "noun", "translation": "human dignity"},
                    {"lemma": "la mayoría de edad", "pos": "noun", "translation": "legal age / age of majority (18)"},
                    {"lemma": "la pena de muerte", "pos": "noun", "translation": "death penalty"},
                    {"lemma": "la integridad física", "pos": "noun", "translation": "physical integrity"},
                    {"lemma": "la detención preventiva", "pos": "noun", "translation": "preventive detention"},
                    {"lemma": "la puesta en libertad", "pos": "noun", "translation": "release from custody"},
                    {"lemma": "la autoridad judicial", "pos": "noun", "translation": "judicial authority"},
                    {"lemma": "el hábeas corpus", "pos": "noun", "translation": "habeas corpus"}
                ],
                "grammar_title": "Expresar garantías legales: «quedar abolido/a» y «en el plazo máximo de»",
                "grammar_text": "Para enunciar prohibiciones absolutas y límites temporales que protegen a los ciudadanos frente a los abusos de poder, el lenguaje constitucional utiliza **«quedar + participio»** (*queda abolida la pena de muerte*) y la locución temporal **«en el plazo máximo de»** (*en el plazo máximo de setenta y dos horas*).",
                "grammar_examples": [
                    {"es": "En España queda abolida la pena de muerte por mandato del artículo 15 de la Constitución.", "en": "In Spain the death penalty is abolished by mandate of Article 15 of the Constitution."},
                    {"es": "En el plazo máximo de setenta y dos horas, el detenido debe ser puesto en libertad o entregado al juez.", "en": "Within a maximum period of seventy-two hours, the detainee must be released or handed over to the judge."}
                ],
                "grammar_tip": "Recuerda para el examen CCSE: la mayoría de edad en España se alcanza a los 18 años (Art. 12 CE) y la detención preventiva policial nunca puede superar las 72 horas (Art. 17 CE).",
                "paragraphs": [
                    "El Título I de la Constitución Española se abre con el artículo 10, considerado la piedra angular de todo el edificio de los derechos: la dignidad de la persona, los derechos inviolables que le son inherentes y el libre desarrollo de la personalidad son el fundamento del orden político y de la paz social. Además, la Constitución establece que todas las normas relativas a los derechos fundamentales deben interpretarse de conformidad con la Declaración Universal de Derechos Humanos.",
                    "Muy cerca de ese pórtico, el artículo 12 fija un dato que todo aspirante a la nacionalidad debe recordar con exactitud: los españoles son mayores de edad a los dieciocho años. Al cumplir los dieciocho años, el ciudadano adquiere la plena capacidad de obrar en la vida civil y política, incluido el derecho de sufragio activo y pasivo.",
                    "El artículo 15 proclama que todos tienen derecho a la vida y a la integridad física y moral, sin que, en ningún caso, puedan ser sometidos a tortura ni a penas o tratos inhumanos o degradantes. A continuación, el texto constitucional añade una frase histórica: queda abolida la pena de muerte. En 1995, las Cortes Generales suprimieron la pena capital incluso del Código Penal Militar para tiempos de guerra, convirtiendo la abolición en total y absoluta.",
                    "Por su parte, el artículo 17 protege la libertad y la seguridad personales. Nadie puede ser privado de su libertad sino en los casos y en la forma previstos en la ley. Si la policía practica una detención preventiva, esta no puede durar más del tiempo estrictamente necesario para esclarecer los hechos y, en todo caso, en el plazo máximo de setenta y dos horas el detenido deberá ser puesto en libertad o a disposición de la autoridad judicial.",
                    "Además, toda persona detenida debe ser informada de forma inmediata, y de modo que le sea comprensible, de sus derechos y de las razones de su detención, no pudiendo ser obligada a declarar. Se garantiza la asistencia de abogado en las diligencias policiales y judiciales, así como el procedimiento de «hábeas corpus» para poner inmediatamente a disposición del juez a cualquier persona detenida ilegalmente."
                ],
                "questions": [
                    {
                        "question": "¿A qué edad se alcanza la mayoría de edad en España según el artículo 12 de la Constitución?",
                        "options": ["A los 18 años", "A los 16 años", "A los 21 años", "A los 20 años"],
                        "correctIndex": 0,
                        "explanation": "El artículo 12 de la Constitución Española establece que los españoles son mayores de edad a los 18 años."
                    },
                    {
                        "question": "¿Cuál es la duración máxima de la detención preventiva policial antes de que el detenido pase a disposición judicial o quede en libertad?",
                        "options": ["72 horas", "24 horas", "48 horas", "96 horas"],
                        "correctIndex": 0,
                        "explanation": "El artículo 17.2 de la Constitución fija un plazo máximo improrrogable de 72 horas para la detención preventiva."
                    },
                    {
                        "question": "¿Qué establece el artículo 15 de la Constitución respecto a la pena de muerte y la tortura?",
                        "options": [
                            "Prohíbe la tortura en todo caso y declara abolida la pena de muerte",
                            "Mantiene la pena de muerte para delitos económicos graves",
                            "Permite tratos degradantes con autorización policial",
                            "Delega la pena capital en los ayuntamientos"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 15 garantiza la vida y la integridad física y moral, prohíbe la tortura sin excepciones y abole la pena de muerte."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿A qué edad adquieren los españoles la mayoría de edad constitucional?",
                        "options": ["A los 18 años", "A los 16 años", "A los 21 años", "A los 25 años"],
                        "correctIndex": 0,
                        "explanation": "El artículo 12 CE fija la mayoría de edad a los 18 años."
                    },
                    {
                        "prompt": "¿Cuál es el plazo máximo de una detención preventiva antes de pasar ante el juez o quedar libre?",
                        "options": ["72 horas", "12 horas", "36 horas", "120 horas"],
                        "correctIndex": 0,
                        "explanation": "Según el artículo 17 CE, el plazo máximo es de 72 horas."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En España queda ___ la pena de muerte y están prohibidos los tratos inhumanos o degradantes.",
                        "answer": "abolida",
                        "options": ["abolida", "vigente", "aprobada", "obligatoria"],
                        "explanation": "El artículo 15 CE declara que queda abolida la pena de muerte.",
                        "english": "In Spain the death penalty is abolished and inhuman or degrading treatment is prohibited."
                    },
                    {
                        "sentence": "En el ___ máximo de setenta y dos horas, el detenido deberá pasar a disposición de la autoridad judicial.",
                        "answer": "plazo",
                        "options": ["plazo", "voto", "escaño", "himno"],
                        "explanation": "«En el plazo máximo de 72 horas» es la fórmula del artículo 17 CE.",
                        "english": "Within a maximum period of seventy-two hours, the detainee must be brought before the judicial authority."
                    }
                ],
                "ex_dict": {
                    "audioText": "En España la mayoría de edad se alcanza a los dieciocho años y queda abolida la pena de muerte.",
                    "english": "In Spain legal majority is reached at eighteen years of age and the death penalty is abolished."
                },
                "ex_sb": {
                    "words": ["La", "detención", "preventiva", "no", "puede", "durar", "más", "de", "setenta", "y", "dos", "horas."],
                    "english": "Preventive detention cannot last more than seventy-two hours."
                }
            },
            {
                "num": "02",
                "Title": "Honor, Intimidad, Domicilio y Protección de Datos",
                "title": "Honor, Intimidad, Domicilio y Protección de Datos",
                "grammar_slug": "salvo-flagrante-delito-consentimiento",
                "story_slug": "intimidad",
                "story_title": "Tras la puerta de casa: el domicilio inviolable y la huella digital",
                "objectives": [
                    "Conocer las garantías del artículo 18 CE: derecho al honor, a la intimidad personal y familiar, y a la propia imagen.",
                    "Identificar los tres únicos supuestos para entrar en un domicilio y el secreto de las comunicaciones.",
                    "Utilizar la estructura «salvo en caso de flagrante delito o resolución judicial»."
                ],
                "vocab": [
                    {"lemma": "el derecho al honor", "pos": "noun", "translation": "right to honor"},
                    {"lemma": "la intimidad personal", "pos": "noun", "translation": "personal privacy"},
                    {"lemma": "la propia imagen", "pos": "noun", "translation": "own image"},
                    {"lemma": "la inviolabilidad del domicilio", "pos": "noun", "translation": "inviolability of the home"},
                    {"lemma": "el flagrante delito", "pos": "noun", "translation": "flagrant crime (caught in the act)"},
                    {"lemma": "el secreto de las comunicaciones", "pos": "noun", "translation": "secrecy of communications"},
                    {"lemma": "la protección de datos", "pos": "noun", "translation": "data protection"},
                    {"lemma": "la resolución judicial", "pos": "noun", "translation": "court order / judicial warrant"}
                ],
                "grammar_title": "Excepciones legales estrictas: «salvo consentimiento del titular, resolución judicial o flagrante delito»",
                "grammar_text": "Para expresar que un derecho es inviolable salvo en contadas excepciones tasadas por la Constitución, se emplean las preposiciones **«salvo»** o **«sin»** seguidas de sustantivos jurídicos: *el domicilio es inviolable; ninguna entrada o registro podrá hacerse en él sin consentimiento del titular o resolución judicial, salvo en caso de flagrante delito*.",
                "grammar_examples": [
                    {"es": "Nadie puede entrar en tu vivienda sin tu consentimiento o una orden del juez, salvo en caso de flagrante delito.", "en": "No one may enter your home without your consent or a judge's warrant, except in the case of a flagrant crime."},
                    {"es": "Se garantiza el secreto de las comunicaciones postales, telegráficas y telefónicas, salvo resolución judicial.", "en": "The secrecy of postal, telegraphic, and telephone communications is guaranteed, unless there is a court order."}
                ],
                "grammar_tip": "En el examen CCSE se pregunta con frecuencia qué se necesita para que la policía entre en un domicilio particular: consentimiento del titular, orden judicial o delito flagrante.",
                "paragraphs": [
                    "El artículo 18 de la Constitución Española protege la esfera más íntima de cada ciudadano. En su primer apartado garantiza tres derechos estrechamente unidos: el derecho al honor, a la intimidad personal y familiar, y a la propia imagen. Gracias a ellos, nadie puede difundir informaciones difamatorias ni utilizar la fotografía o la vida privada de una persona sin su autorización.",
                    "El segundo apartado consagra un principio clásico del constitucionalismo liberal: el domicilio es inviolable. Ninguna entrada o registro puede hacerse en una vivienda particular sin el consentimiento de su titular o sin una resolución judicial motivada, salvo en el caso de que se esté cometiendo un flagrante delito en su interior.",
                    "Del mismo modo, el tercer apartado garantiza el secreto de las comunicaciones y, en especial, de las postales, telegráficas y telefónicas, así como de los mensajes electrónicos actuales. Ni siquiera las fuerzas policiales pueden interceptar una llamada telefónica o leer la correspondencia privada de un ciudadano sin contar previamente con la autorización expresa de un juez.",
                    "Con una extraordinaria visión de futuro en 1978, el cuarto apartado del artículo 18 ordenó que la ley limitara el uso de la informática para garantizar el honor y la intimidad personal y familiar de los ciudadanos. De ese mandato nació el derecho fundamental a la protección de datos personales, supervisado en España por la Agencia Española de Protección de Datos (AEPD).",
                    "Finalmente, el artículo 19 completa esta esfera de libertad personal garantizando a los españoles el derecho a elegir libremente su residencia y a circular por todo el territorio nacional, así como a entrar y salir libremente de España en los términos que la ley establezca, un derecho que nunca puede ser limitado por motivos políticos o ideológicos."
                ],
                "questions": [
                    {
                        "question": "Según el artículo 18 de la Constitución, ¿en qué casos se puede entrar o registrar un domicilio particular?",
                        "options": [
                            "Solo con consentimiento del titular, resolución judicial o en caso de flagrante delito",
                            "En cualquier momento si lo decide un concejal municipal",
                            "Cuando lo solicita la comunidad de vecinos por mayoría simple",
                            "Con una simple orden verbal de cualquier funcionario administrativo"
                        ],
                        "correctIndex": 0,
                        "explanation": "El domicilio es inviolable y solo admite entrada con consentimiento del titular, orden judicial o flagrante delito."
                    },
                    {
                        "question": "¿Qué se requiere para poder intervenir legalmente las comunicaciones telefónicas o postales de una persona?",
                        "options": [
                            "Una resolución judicial",
                            "El permiso del alcalde de la localidad",
                            "Un informe de una empresa privada",
                            "Una solicitud de cualquier periódico"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 18.3 CE garantiza el secreto de las comunicaciones salvo resolución judicial."
                    },
                    {
                        "question": "¿Qué organismo público vela en España por el cumplimiento de la legislación sobre privacidad e informática?",
                        "options": [
                            "La Agencia Española de Protección de Datos (AEPD)",
                            "La Real Academia Española",
                            "El Banco de España",
                            "La Dirección General de Tráfico"
                        ],
                        "correctIndex": 0,
                        "explanation": "La AEPD supervisa el derecho fundamental a la protección de datos personales derivado del artículo 18.4 CE."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué declara el artículo 18.2 de la Constitución sobre el domicilio?",
                        "options": [
                            "Que el domicilio es inviolable",
                            "Que el domicilio puede ser registrado sin permiso ni orden judicial",
                            "Que cada ciudadano solo puede vivir en su municipio natal",
                            "Que las cartas privadas son de acceso público"
                        ],
                        "correctIndex": 0,
                        "explanation": "El domicilio es inviolable salvo consentimiento, resolución judicial o flagrante delito."
                    },
                    {
                        "prompt": "¿Pueden limitarse por motivos políticos o ideológicos el derecho a entrar y salir libremente de España?",
                        "options": [
                            "No, el artículo 19 prohíbe expresamente limitarlo por motivos políticos o ideológicos",
                            "Sí, cuando cambia el Gobierno",
                            "Sí, en cada elección municipal",
                            "Solo en las ciudades costeras"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 19 CE garantiza la libertad de residencia y circulación y prohíbe limitarla por motivos políticos o ideológicos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El domicilio es ___ y nadie puede entrar en él sin consentimiento del titular o resolución judicial.",
                        "answer": "inviolable",
                        "options": ["inviolable", "público", "temporal", "confiscatorio"],
                        "explanation": "«El domicilio es inviolable» es la fórmula exacta del artículo 18.2 CE.",
                        "english": "The home is inviolable and no one may enter it without the owner's consent or a court order."
                    },
                    {
                        "sentence": "Se garantiza el ___ de las comunicaciones postales, telegráficas y telefónicas, salvo resolución judicial.",
                        "answer": "secreto",
                        "options": ["secreto", "impuesto", "censo", "escudo"],
                        "explanation": "El artículo 18.3 CE protege el secreto de las comunicaciones.",
                        "english": "The secrecy of postal, telegraphic, and telephone communications is guaranteed, unless there is a court order."
                    }
                ],
                "ex_dict": {
                    "audioText": "El domicilio es inviolable y se garantiza el secreto de las comunicaciones salvo resolución judicial.",
                    "english": "The home is inviolable and the secrecy of communications is guaranteed unless there is a court order."
                },
                "ex_sb": {
                    "words": ["Se", "garantiza", "el", "derecho", "al", "honor,", "a", "la", "intimidad", "y", "a", "la", "propia", "imagen."],
                    "english": "The right to honor, privacy, and one's own image is guaranteed."
                }
            },
            {
                "num": "03",
                "Title": "Libertad Ideológica, Religiosa y de Expresión",
                "title": "Libertad Ideológica, Religiosa y de Expresión",
                "grammar_slug": "ninguna-confesion-tendrad-caracter-estatal",
                "story_slug": "expresion",
                "story_title": "Sin religión de Estado ni censura previa: la palabra libre",
                "objectives": [
                    "Comprender el carácter aconfesional del Estado español y la libertad religiosa (Art. 16 CE).",
                    "Identificar las libertades de expresión, información y cátedra, así como la prohibición de la censura previa (Art. 20 CE).",
                    "Manejar las fórmulas «ninguna confesión tendrá carácter estatal» y «mediante ningún tipo de censura previa»."
                ],
                "vocab": [
                    {"lemma": "la libertad ideológica", "pos": "noun", "translation": "ideological freedom"},
                    {"lemma": "la libertad religiosa y de culto", "pos": "noun", "translation": "religious freedom and freedom of worship"},
                    {"lemma": "el Estado aconfesional", "pos": "noun", "translation": "non-confessional State"},
                    {"lemma": "la confesión religiosa", "pos": "noun", "translation": "religious denomination"},
                    {"lemma": "la libertad de expresión", "pos": "noun", "translation": "freedom of expression"},
                    {"lemma": "la libertad de cátedra", "pos": "noun", "translation": "academic freedom"},
                    {"lemma": "la censura previa", "pos": "noun", "translation": "prior censorship"},
                    {"lemma": "el secreto profesional", "pos": "noun", "translation": "professional secrecy (of journalists)"}
                ],
                "grammar_title": "Neutralidad y pluralismo: «ninguna confesión tendrá carácter estatal»",
                "grammar_text": "El artículo 16 de la Constitución define a España como un **Estado aconfesional** mediante una oración negativa de valor universal: **«Ninguna confesión tendrá carácter estatal»**, complementada con la prohibición de obligar a nadie a declarar sobre sus creencias: *«Nadie podrá ser obligado a declarar sobre su ideología, religión o creencias»*.",
                "grammar_examples": [
                    {"es": "En España ninguna confesión tendrá carácter estatal, aunque los poderes públicos cooperan con las confesiones.", "en": "In Spain no religious denomination shall have the character of a state religion, although public authorities cooperate with denominations."},
                    {"es": "El ejercicio de la libertad de expresión no puede restringirse mediante ningún tipo de censura previa.", "en": "The exercise of freedom of expression cannot be restricted by any kind of prior censorship."}
                ],
                "grammar_tip": "Pregunta clave del CCSE: España es un Estado aconfesional (ninguna confesión tiene carácter estatal), y está prohibida cualquier forma de censura previa.",
                "paragraphs": [
                    "Durante siglos, la historia política de España estuvo marcada por la confesionalidad del Estado. La Constitución de 1978 cerró aquella etapa en su artículo 16 al garantizar la libertad ideológica, religiosa y de culto de los individuos y las comunidades, sin más limitación en sus manifestaciones que la necesaria para el mantenimiento del orden público protegido por la ley.",
                    "Ese mismo artículo 16 contiene dos reglas esenciales que definen el modelo español. En primer lugar, nadie podrá ser obligado a declarar sobre su ideología, religión o creencias. En segundo lugar, ninguna confesión tendrá carácter estatal. España es, por tanto, un Estado aconfesional: los poderes públicos tienen en cuenta las creencias religiosas de la sociedad española y mantienen relaciones de cooperación con la Iglesia Católica y las demás confesiones (evangélica, judía y musulmana, entre otras).",
                    "En el terreno de la comunicación pública, el artículo 20 reconoce y protege el derecho a expresar y difundir libremente los pensamientos, ideas y opiniones mediante la palabra, el escrito o cualquier otro medio de reproducción, así como la producción literaria, artística, científica y técnica, la libertad de cátedra y el derecho a comunicar o recibir libremente información veraz.",
                    "Para blindar el pluralismo democrático frente a los recuerdos de la dictadura, la Constitución proclama con rotundidad que el ejercicio de estos derechos no puede restringirse mediante ningún tipo de censura previa. Además, el secuestro de publicaciones o grabaciones solo podrá acordarse en virtud de una resolución judicial.",
                    "Por último, la ley regula la cláusula de conciencia y el secreto profesional de los periodistas en el ejercicio de estas libertades, recordando que su límite reside en el respeto a los demás derechos fundamentales, especialmente el derecho al honor, a la intimidad, a la propia imagen y a la protección de la juventud y de la infancia."
                ],
                "questions": [
                    {
                        "question": "Según el artículo 16 de la Constitución Española, ¿cuál es la relación del Estado con la religión?",
                        "options": [
                            "España es un Estado aconfesional: ninguna confesión tendrá carácter estatal",
                            "El catolicismo es la única religión permitida por la ley",
                            "Está prohibido practicar cualquier religión en territorio español",
                            "Todos los ciudadanos están obligados a declarar su religión en el DNI"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 16.3 CE establece que ninguna confesión tendrá carácter estatal, garantizando la libertad religiosa y de culto."
                    },
                    {
                        "question": "¿Puede obligarse a un ciudadano en España a declarar sobre su ideología, religión o creencias?",
                        "options": [
                            "No, nadie podrá ser obligado a declarar sobre su ideología, religión o creencias",
                            "Sí, al matricularse en la universidad",
                            "Sí, en el censo electoral municipal",
                            "Sí, al renovar el pasaporte"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 16.2 CE prohíbe expresamente obligar a nadie a declarar sobre su ideología, religión o creencias."
                    },
                    {
                        "question": "¿Permite el artículo 20 de la Constitución la censura previa de libros o periódicos?",
                        "options": [
                            "No, prohíbe restringir la libertad de expresión mediante ningún tipo de censura previa",
                            "Sí, el Gobierno puede censurar periódicos antes de su impresión",
                            "Sí, los alcaldes revisan los libros antes de su venta",
                            "Solo se permite para novelas y obras de teatro"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 20.2 CE prohíbe cualquier tipo de censura previa."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cómo se define España en materia religiosa según el artículo 16 de la Constitución?",
                        "options": [
                            "Como un Estado aconfesional donde ninguna confesión tiene carácter estatal",
                            "Como un Estado confesional obligatorio",
                            "Como un Estado donde está prohibido el culto",
                            "Como una teocracia parlamentaria"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 16.3 CE señala que ninguna confesión tendrá carácter estatal."
                    },
                    {
                        "prompt": "¿Quién es el único que puede acordar el secuestro de una publicación cuando vulnera gravemente la ley?",
                        "options": [
                            "Un juez mediante resolución judicial",
                            "El director de una comisaría",
                            "Un ministro del Gobierno",
                            "El presidente de una diputación"
                        ],
                        "correctIndex": 0,
                        "explanation": "Según el artículo 20.5 CE, el secuestro de publicaciones solo puede acordarse en virtud de resolución judicial."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Según el artículo 16 de la Constitución, ninguna ___ tendrá carácter estatal en España.",
                        "answer": "confesión",
                        "options": ["confesión", "provincia", "sentencia", "elección"],
                        "explanation": "«Ninguna confesión tendrá carácter estatal» (Art. 16.3 CE).",
                        "english": "According to Article 16 of the Constitution, no religious denomination shall have the character of a state religion in Spain."
                    },
                    {
                        "sentence": "La libertad de expresión no puede restringirse mediante ningún tipo de ___ previa.",
                        "answer": "censura",
                        "options": ["censura", "lectura", "reforma", "consulta"],
                        "explanation": "El artículo 20.2 CE prohíbe la censura previa.",
                        "english": "Freedom of expression cannot be restricted by any kind of prior censorship."
                    }
                ],
                "ex_dict": {
                    "audioText": "Nadie podrá ser obligado a declarar sobre su ideología, religión o creencias.",
                    "english": "No one may be compelled to make statements regarding their ideology, religion, or beliefs."
                },
                "ex_sb": {
                    "words": ["En", "España", "ninguna", "confesión", "religiosa", "tendrá", "carácter", "estatal."],
                    "english": "In Spain no religious denomination shall have the character of a state religion."
                }
            },
            {
                "num": "04",
                "Title": "Reunión, Asociación, Sindicación y Huelga",
                "title": "Reunión, Asociación, Sindicación y Huelga",
                "grammar_slug": "sin-autorizacion-previa-comunicacion",
                "story_slug": "reunion",
                "story_title": "La plaza pública y el taller: reunirse, asociarse y hacer huelga",
                "objectives": [
                    "Distinguir entre el derecho de reunión pacífica sin autorización previa y la comunicación previa para manifestaciones en vías públicas (Art. 21 CE).",
                    "Conocer el derecho de asociación (Art. 22 CE) y los derechos de libertad sindical y de huelga con mantenimiento de servicios esenciales (Art. 28 CE).",
                    "Practicar las construcciones «no necesitará autorización previa» y «asegurar el mantenimiento de los servicios esenciales»."
                ],
                "vocab": [
                    {"lemma": "la reunión pacífica y sin armas", "pos": "noun", "translation": "peaceful and unarmed assembly"},
                    {"lemma": "la autorización previa", "pos": "noun", "translation": "prior authorization"},
                    {"lemma": "la comunicación previa", "pos": "noun", "translation": "prior notification"},
                    {"lemma": "la manifestación", "pos": "noun", "translation": "public demonstration"},
                    {"lemma": "el derecho de asociación", "pos": "noun", "translation": "right of association"},
                    {"lemma": "la libertad sindical", "pos": "noun", "translation": "trade union freedom"},
                    {"lemma": "el derecho a la huelga", "pos": "noun", "translation": "right to strike"},
                    {"lemma": "los servicios esenciales", "pos": "noun", "translation": "essential services (minimum services)"}
                ],
                "grammar_title": "Matices jurídicos: «no necesitar autorización previa» frente a «dar comunicación previa»",
                "grammar_text": "En español constitucional es crucial distinguir entre pedir permiso (**autorización previa**, que no se exige para reunirse) e informar a la autoridad (**comunicación previa**, necesaria cuando la manifestación ocupa calles o plazas): *El ejercicio del derecho de reunión pacífica y sin armas no necesitará autorización previa*.",
                "grammar_examples": [
                    {"es": "El ejercicio del derecho de reunión pacífica y sin armas no necesitará autorización previa.", "en": "The exercise of the right to peaceful and unarmed assembly shall not require prior authorization."},
                    {"es": "La ley que regule el derecho a la huelga establecerá las garantías para asegurar el mantenimiento de los servicios esenciales.", "en": "The law regulating the right to strike shall establish guarantees to ensure the maintenance of essential services."}
                ],
                "grammar_tip": "¡Atención al matiz CCSE! Reunirse pacíficamente no necesita autorización previa; para manifestarse en la vía pública solo se exige dar comunicación previa a la autoridad.",
                "paragraphs": [
                    "Una democracia viva no se ejerce únicamente cada cuatro años frente a una urna; también se vive en las calles, en las asociaciones vecinales y en los centros de trabajo. Por eso el artículo 21 de la Constitución reconoce el derecho de reunión pacífica y sin armas, estableciendo que el ejercicio de este derecho no necesitará autorización previa.",
                    "Ahora bien, cuando se trata de reuniones en lugares de tránsito público y manifestaciones que recorren calles o plazas, los organizadores deben dar comunicación previa a la autoridad gubernativa. Esta solo podrá prohibirlas cuando existan razones fundadas de alteración del orden público, con peligro para personas o bienes.",
                    "Junto al derecho de reunión, el artículo 22 reconoce el derecho de asociación. Los ciudadanos pueden crear libremente asociaciones culturales, deportivas, vecinales o benéficas, que solo deben inscribirse en un registro a los solos efectos de publicidad. La Constitución declara ilegales las asociaciones que persigan fines o utilicen medios tipificados como delito, y prohíbe expresamente las asociaciones secretas y las de carácter paramilitar.",
                    "En el ámbito laboral, el artículo 28 consagra dos derechos fundamentales de los trabajadores. El primero es la libertad sindical: todos tienen derecho a sindicarse libremente para defender sus intereses económicos y sociales, y nadie podrá ser obligado a afiliarse a un sindicato.",
                    "El segundo es el derecho a la huelga de los trabajadores para la defensa de sus intereses. La Constitución añade una garantía indispensable para el conjunto de la ciudadanía: la ley que regule el ejercicio de este derecho establecerá las garantías precisas para asegurar el mantenimiento de los servicios esenciales de la comunidad, conocidos habitualmente como «servicios mínimos» en hospitales, transporte o emergencias."
                ],
                "questions": [
                    {
                        "question": "Según el artículo 21 de la Constitución, ¿se necesita autorización previa para ejercer el derecho de reunión pacífica y sin armas?",
                        "options": [
                            "No, no necesita autorización previa (solo comunicación previa si es en lugares de tránsito público)",
                            "Sí, siempre hace falta un permiso firmado por el Tribunal Supremo",
                            "Está prohibido reunirse más de diez personas en España",
                            "Solo pueden reunirse los funcionarios públicos"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 21.1 CE establece que el derecho de reunión pacífica y sin armas no necesitará autorización previa."
                    },
                    {
                        "question": "¿Qué tipo de asociaciones están expresamente prohibidas por el artículo 22 de la Constitución?",
                        "options": [
                            "Las asociaciones secretas y las de carácter paramilitar",
                            "Las asociaciones deportivas y juveniles",
                            "Las asociaciones de vecinos y consumidores",
                            "Los clubes de lectura y coros musicales"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 22.5 CE prohíbe las asociaciones secretas y las de carácter paramilitar."
                    },
                    {
                        "question": "¿Qué debe garantizarse siempre durante el ejercicio del derecho a la huelga según el artículo 28.2 CE?",
                        "options": [
                            "El mantenimiento de los servicios esenciales de la comunidad",
                            "El cierre total de todos los hospitales y servicios de urgencias",
                            "La afiliación obligatoria de todos los trabajadores a un sindicato único",
                            "La suspensión de todas las pensiones públicas"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 28.2 CE exige asegurar el mantenimiento de los servicios esenciales de la comunidad."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Se puede obligar a un trabajador en España a afiliarse a un sindicato?",
                        "options": [
                            "No, el artículo 28 establece que nadie podrá ser obligado a afiliarse a un sindicato",
                            "Sí, es obligatorio desde el primer contrato laboral",
                            "Sí, para todos los mayores de 25 años",
                            "Depende de la provincia donde resida"
                        ],
                        "correctIndex": 0,
                        "explanation": "La libertad sindical incluye tanto el derecho a afiliarse como el derecho a no ser obligado a afiliarse."
                    },
                    {
                        "prompt": "¿Cuándo debe darse comunicación previa a la autoridad para ejercer el derecho de reunión?",
                        "options": [
                            "En los casos de reuniones en lugares de tránsito público y manifestaciones",
                            "Cuando una familia cena en su domicilio privado",
                            "Cuando tres amigos toman café en una cafetería",
                            "En ningún caso"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 21.2 CE exige comunicación previa únicamente para reuniones en lugares de tránsito público y manifestaciones."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El ejercicio del derecho de reunión pacífica y sin armas no necesitará ___ previa.",
                        "answer": "autorización",
                        "options": ["autorización", "educación", "jubilación", "monarquía"],
                        "explanation": "El artículo 21.1 CE dispone que no necesitará autorización previa.",
                        "english": "The exercise of the right to peaceful and unarmed assembly shall not require prior authorization."
                    },
                    {
                        "sentence": "Durante una huelga se debe asegurar el mantenimiento de los servicios ___ de la comunidad.",
                        "answer": "esenciales",
                        "options": ["esenciales", "secretos", "privados", "paramilitares"],
                        "explanation": "El artículo 28.2 CE protege el mantenimiento de los servicios esenciales de la comunidad.",
                        "english": "During a strike, the maintenance of essential community services must be ensured."
                    }
                ],
                "ex_dict": {
                    "audioText": "El ejercicio del derecho de reunión pacífica y sin armas no necesitará autorización previa.",
                    "english": "The exercise of the right to peaceful and unarmed assembly shall not require prior authorization."
                },
                "ex_sb": {
                    "words": ["Se", "reconoce", "el", "derecho", "a", "la", "huelga", "de", "los", "trabajadores", "para", "defender", "sus", "intereses."],
                    "english": "The right of workers to strike in order to defend their interests is recognized."
                }
            },
            {
                "num": "05",
                "Title": "Educación, Salud, Vivienda y Pensiones",
                "title": "Educación, Salud, Vivienda y Pensiones",
                "grammar_slug": "obligatoria-y-gratuita-vivienda-digna",
                "story_slug": "sociales",
                "story_title": "Del pupitre escolar a la jubilación: los pilares del Estado del bienestar",
                "objectives": [
                    "Dominar el artículo 27 CE: derecho a la educación y enseñanza básica obligatoria y gratuita (de los 6 a los 16 años).",
                    "Conocer los derechos sociales a la protección de la salud (Art. 43 CE), vivienda digna (Art. 47 CE) y pensiones actualizadas (Art. 50 CE).",
                    "Practicar las expresiones «la enseñanza básica es obligatoria y gratuita» y «disfrutar de una vivienda digna y adecuada»."
                ],
                "vocab": [
                    {"lemma": "la enseñanza básica", "pos": "noun", "translation": "basic education (ages 6–16)"},
                    {"lemma": "obligatorio/a y gratuito/a", "pos": "adjective", "translation": "compulsory and free of charge"},
                    {"lemma": "la autonomía universitaria", "pos": "noun", "translation": "university autonomy"},
                    {"lemma": "la protección de la salud", "pos": "noun", "translation": "health protection"},
                    {"lemma": "la Seguridad Social", "pos": "noun", "translation": "Social Security"},
                    {"lemma": "la vivienda digna y adecuada", "pos": "noun", "translation": "decent and adequate housing"},
                    {"lemma": "la tercera edad", "pos": "noun", "translation": "senior citizens / elderly"},
                    {"lemma": "la pensión actualizada", "pos": "noun", "translation": "updated pension"}
                ],
                "grammar_title": "Derechos educativos y sociales: «obligatoria y gratuita»",
                "grammar_text": "El artículo 27.4 de la Constitución contiene una de las frases más preguntadas en el examen CCSE: **«La enseñanza básica es obligatoria y gratuita»**. En España, esta etapa abarca diez años de escolarización, desde los **6 hasta los 16 años** (Educación Primaria y Educación Secundaria Obligatoria, ESO).",
                "grammar_examples": [
                    {"es": "Según la Constitución Española, la enseñanza básica es obligatoria y gratuita para todos.", "en": "According to the Spanish Constitution, basic education is compulsory and free for everyone."},
                    {"es": "Todos los españoles tienen derecho a disfrutar de una vivienda digna y adecuada.", "en": "All Spaniards have the right to enjoy decent and adequate housing."}
                ],
                "grammar_tip": "Dato imprescindible para el examen CCSE: la enseñanza básica (Primaria y ESO, de 6 a 16 años) es obligatoria y gratuita en España.",
                "paragraphs": [
                    "Un Estado social y democrático de Derecho no se limita a garantizar libertades civiles; también asegura condiciones materiales de vida digna desde la infancia hasta la vejez. En la esfera educativa, el artículo 27 de la Constitución proclama que todos tienen el derecho a la educación y reconoce la libertad de enseñanza, añadiendo una regla fundamental: la enseñanza básica es obligatoria y gratuita.",
                    "En el sistema educativo español actual, esa enseñanza básica comprende diez cursos escolares, entre los 6 y los 16 años de edad, divididos en la Educación Primaria (de 6 a 12 años) y la Educación Secundaria Obligatoria o ESO (de 12 a 16 años). El mismo artículo 27 garantiza el derecho de los padres a que sus hijos reciban la formación religiosa y moral que esté de acuerdo con sus propias convicciones y reconoce la autonomía de las universidades.",
                    "Más adelante, en el Capítulo III del Título I («De los principios rectores de la política social y económica»), el artículo 41 encomienda a los poderes públicos mantener un régimen público de Seguridad Social para todos los ciudadanos, que garantice la asistencia y prestaciones sociales suficientes ante situaciones de necesidad, especialmente en caso de desempleo.",
                    "A su lado, el artículo 43 reconoce el derecho a la protección de la salud, articulado a través del Sistema Nacional de Salud con cobertura universal, y fomenta la educación sanitaria, la educación física y el deporte. Por su parte, el artículo 47 establece que todos los españoles tienen derecho a disfrutar de una vivienda digna y adecuada, ordenando a los poderes públicos regular la utilización del suelo de acuerdo con el interés general para impedir la especulación.",
                    "Finalmente, el artículo 50 dedica una protección especial a los ciudadanos durante la tercera edad: los poderes públicos garantizarán, mediante pensiones adecuadas y periódicamente actualizadas, la suficiencia económica de los mayores, promoviendo asimismo su bienestar mediante un sistema de servicios sociales que atenderán sus problemas específicos de salud, vivienda, cultura y ocio."
                ],
                "questions": [
                    {
                        "question": "¿Cómo es la enseñanza básica en España según el artículo 27.4 de la Constitución?",
                        "options": [
                            "Obligatoria y gratuita (y comprende de los 6 a los 16 años)",
                            "Voluntaria y de pago en todos los centros públicos",
                            "Obligatoria únicamente hasta los 10 años",
                            "Exclusiva para mayores de 18 años"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 27.4 CE establece que la enseñanza básica es obligatoria y gratuita, abarcando Primaria y ESO (6–16 años)."
                    },
                    {
                        "question": "¿Qué derecho reconoce el artículo 47 de la Constitución Española a todos los españoles?",
                        "options": [
                            "El derecho a disfrutar de una vivienda digna y adecuada",
                            "El derecho a no pagar impuestos nunca",
                            "El derecho a poseer dos palacios históricos",
                            "El derecho a elegir directamente a los jueces"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 47 CE reconoce el derecho a disfrutar de una vivienda digna y adecuada."
                    },
                    {
                        "question": "¿Qué garantiza el artículo 50 de la Constitución a los ciudadanos durante la tercera edad?",
                        "options": [
                            "La suficiencia económica mediante pensiones adecuadas y periódicamente actualizadas",
                            "La exención del DNI",
                            "El voto doble en las elecciones generales",
                            "Un escaño vitalicio en el Senado"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 50 CE garantiza pensiones adecuadas y periódicamente actualizadas para los mayores."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Entre qué edades es obligatoria la escolarización básica en España?",
                        "options": [
                            "De los 6 a los 16 años (Educación Primaria y ESO)",
                            "De los 3 a los 12 años",
                            "De los 10 a los 20 años",
                            "De los 8 a los 14 años"
                        ],
                        "correctIndex": 0,
                        "explanation": "La enseñanza básica obligatoria y gratuita abarca de los 6 a los 16 años."
                    },
                    {
                        "prompt": "¿Qué institución pública garantiza prestaciones ante situaciones de necesidad y desempleo según el artículo 41 CE?",
                        "options": [
                            "La Seguridad Social",
                            "La Real Academia de la Historia",
                            "El Tribunal de Cuentas",
                            "El Museo del Prado"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 41 CE ordena mantener un régimen público de Seguridad Social para todos los ciudadanos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En España, la enseñanza básica es ___ y gratuita desde los seis hasta los dieciséis años.",
                        "answer": "obligatoria",
                        "options": ["obligatoria", "optativa", "secreta", "privada"],
                        "explanation": "«La enseñanza básica es obligatoria y gratuita» (Art. 27.4 CE).",
                        "english": "In Spain, basic education is compulsory and free from six to sixteen years of age."
                    },
                    {
                        "sentence": "Todos los españoles tienen derecho a disfrutar de una ___ digna y adecuada.",
                        "answer": "vivienda",
                        "options": ["vivienda", "aduana", "moción", "regencia"],
                        "explanation": "El artículo 47 CE consagra el derecho a una vivienda digna y adecuada.",
                        "english": "All Spaniards have the right to enjoy decent and adequate housing."
                    }
                ],
                "ex_dict": {
                    "audioText": "La enseñanza básica es obligatoria y gratuita para todos en España.",
                    "english": "Basic education is compulsory and free for everyone in Spain."
                },
                "ex_sb": {
                    "words": ["Todos", "los", "españoles", "tienen", "derecho", "a", "disfrutar", "de", "una", "vivienda", "digna."],
                    "english": "All Spaniards have the right to enjoy decent housing."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 14: Igualdad, Familia y No Discriminación (unit_num=50, b1-igualdad)
    # =========================================================================
    {
        "slug": "igualdad",
        "unit_num": 50,
        "title": "Igualdad, Familia y No Discriminación",
        "description": "Igualdad ante la ley (Art. 14 CE), teléfono 016 contra la violencia de género, matrimonio igualitario, reforma del artículo 49 CE y nacionalidad por residencia.",
        "Badge": "Igualdad y Familia",
        "lessons": [
            {
                "num": "01",
                "Title": "Igualdad ante la Ley y Prohibición de Discriminación",
                "title": "Igualdad ante la Ley y Prohibición de Discriminación",
                "grammar_slug": "sin-que-pueda-prevalecer-por-razon-de",
                "story_slug": "anteley",
                "story_title": "El artículo 14: de la igualdad escrita en el papel a la igualdad real",
                "objectives": [
                    "Dominar el contenido del artículo 14 de la Constitución sobre igualdad ante la ley y no discriminación.",
                    "Comprender el mandato del artículo 9.2 CE de promover la igualdad real y efectiva y remover los obstáculos.",
                    "Practicar las construcciones «sin que pueda prevalecer discriminación alguna por razón de...»."
                ],
                "vocab": [
                    {"lemma": "la igualdad ante la ley", "pos": "noun", "translation": "equality before the law"},
                    {"lemma": "por razón de", "pos": "preposition", "translation": "on the grounds of / by reason of"},
                    {"lemma": "la discriminación", "pos": "noun", "translation": "discrimination"},
                    {"lemma": "prevalecer", "pos": "verb", "translation": "to prevail"},
                    {"lemma": "real y efectivo/a", "pos": "adjective", "translation": "real and effective"},
                    {"lemma": "remover los obstáculos", "pos": "verb", "translation": "to remove obstacles"},
                    {"lemma": "la condición o circunstancia personal", "pos": "noun", "translation": "personal condition or circumstance"},
                    {"lemma": "la igualdad de oportunidades", "pos": "noun", "translation": "equal opportunities"}
                ],
                "grammar_title": "Cláusulas antidiscriminatorias: «sin que pueda prevalecer discriminación alguna por razón de...»",
                "grammar_text": "El artículo 14 de la Constitución abre el Capítulo II del Título I con una fórmula solemne: **«Los españoles son iguales ante la ley, sin que pueda prevalecer discriminación alguna por razón de nacimiento, raza, sexo, religión, opinión o cualquier otra condición o circunstancia personal o social»**.",
                "grammar_examples": [
                    {"es": "Los españoles son iguales ante la ley, sin que pueda prevalecer discriminación alguna por razón de sexo o raza.", "en": "Spaniards are equal before the law, without any discrimination prevailing on grounds of sex or race."},
                    {"es": "Corresponde a los poderes públicos promover las condiciones para que la igualdad sea real y efectiva.", "en": "It is the duty of public authorities to promote conditions so that equality is real and effective."}
                ],
                "grammar_tip": "Recuerda que en la Constitución Española la igualdad formal está en el artículo 14 y el mandato de igualdad material (real y efectiva) en el artículo 9.2.",
                "paragraphs": [
                    "El Capítulo Segundo del Título I de la Constitución Española no comienza numerando un derecho más, sino situando en su pórtico el artículo 14. Su texto es breve pero decisivo: «Los españoles son iguales ante la ley, sin que pueda prevalecer discriminación alguna por razón de nacimiento, raza, sexo, religión, opinión o cualquier otra condición o circunstancia personal o social».",
                    "Esta proclamación recoge la igualdad formal: la ley debe ser la misma para todos los ciudadanos, sin privilegios de cuna ni exclusiones arbitrarias, y los tribunales deben aplicarla de manera imparcial. Si una norma o una actuación administrativa discrimina a una persona por cualquiera de esas causas, el ciudadano puede acudir incluso en recurso de amparo ante el Tribunal Constitucional.",
                    "Sin embargo, los redactores de 1978 sabían que proclamar la igualdad en el Boletín Oficial del Estado no basta cuando en la vida cotidiana persisten desigualdades económicas, sociales o históricas. Por eso introdujeron también el artículo 9.2, auténtico motor del Estado social.",
                    "El artículo 9.2 ordena a los poderes públicos promover las condiciones para que la libertad y la igualdad del individuo y de los grupos en que se integra sean reales y efectivas, remover los obstáculos que impidan o dificulten su plenitud y facilitar la participación de todos los ciudadanos en la vida política, económica, cultural y social.",
                    "De la unión entre el artículo 14 y el artículo 9.2 nacen todas las políticas españolas de igualdad de oportunidades: las becas de estudio para familias con menos recursos, los planes de igualdad en las empresas, la protección de los colectivos vulnerables y la lucha contra cualquier forma de racismo, xenofobia, homofobia o discriminación por edad."
                ],
                "questions": [
                    {
                        "question": "¿Qué artículo de la Constitución Española proclama que los españoles son iguales ante la ley sin discriminación por nacimiento, raza, sexo, religión u opinión?",
                        "options": ["El artículo 14", "El artículo 1", "El artículo 56", "El artículo 155"],
                        "correctIndex": 0,
                        "explanation": "El artículo 14 de la Constitución consagra la igualdad ante la ley y la prohibición de toda discriminación."
                    },
                    {
                        "question": "¿Qué ordena el artículo 9.2 de la Constitución a los poderes públicos respecto a la libertad y la igualdad?",
                        "options": [
                            "Promover las condiciones para que sean reales y efectivas y remover los obstáculos que las dificulten",
                            "Dejar que cada provincia decida si aplica o no la igualdad",
                            "Reservar los derechos civiles únicamente a los propietarios de tierras",
                            "Suprimir las becas públicas de educación"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 9.2 CE establece el mandato de igualdad material (real y efectiva)."
                    },
                    {
                        "question": "¿Ante qué órgano puede presentarse un recurso de amparo si se vulnera el principio de igualdad del artículo 14 CE?",
                        "options": [
                            "Ante el Tribunal Constitucional",
                            "Ante el Consejo de Estado",
                            "Ante la Cámara de Comercio",
                            "Ante la Real Academia Española"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 14 está protegido por el recurso de amparo ante el Tribunal Constitucional (Art. 53.2 CE)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "Según el artículo 14 CE, ¿puede prevalecer discriminación alguna por razón de nacimiento, raza, sexo, religión u opinión?",
                        "options": [
                            "No, todos los españoles son iguales ante la ley sin discriminación alguna",
                            "Sí, en el acceso al empleo público",
                            "Sí, según el nivel de renta",
                            "Solo en los municipios pequeños"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 14 CE prohíbe cualquier discriminación por razón de nacimiento, raza, sexo, religión, opinión o circunstancia personal o social."
                    },
                    {
                        "prompt": "¿Cuál es la finalidad de los planes públicos de igualdad y becas inspirados en el artículo 9.2 CE?",
                        "options": [
                            "Lograr que la libertad y la igualdad sean reales y efectivas removiendo obstáculos",
                            "Limitar el acceso a la universidad",
                            "Establecer impuestos confiscatorios",
                            "Restaurar los privilegios estamentales"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 9.2 CE manda remover los obstáculos que impidan la igualdad real y efectiva."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Los españoles son ___ ante la ley, sin que pueda prevalecer discriminación alguna por razón de sexo o raza.",
                        "answer": "iguales",
                        "options": ["iguales", "ajenos", "distintos", "vitalicios"],
                        "explanation": "«Los españoles son iguales ante la ley» (Art. 14 CE).",
                        "english": "Spaniards are equal before the law, without any discrimination prevailing on grounds of sex or race."
                    },
                    {
                        "sentence": "Corresponde a los poderes públicos remover los ___ que impidan que la igualdad sea real y efectiva.",
                        "answer": "obstáculos",
                        "options": ["obstáculos", "estatutos", "escaños", "tributos"],
                        "explanation": "El artículo 9.2 CE ordena remover los obstáculos para alcanzar la igualdad real y efectiva.",
                        "english": "It is up to the public authorities to remove the obstacles that prevent equality from being real and effective."
                    }
                ],
                "ex_dict": {
                    "audioText": "Los españoles son iguales ante la ley, sin discriminación por razón de nacimiento, raza, sexo o religión.",
                    "english": "Spaniards are equal before the law, without discrimination on grounds of birth, race, sex, or religion."
                },
                "ex_sb": {
                    "words": ["Corresponde", "a", "los", "poderes", "públicos", "promover", "que", "la", "igualdad", "sea", "real", "y", "efectiva."],
                    "english": "It is the responsibility of public authorities to promote that equality be real and effective."
                }
            },
            {
                "num": "02",
                "Title": "Igualdad de Género y Teléfono 016 contra la Violencia",
                "title": "Igualdad de Género y Teléfono 016 contra la Violencia",
                "grammar_slug": "no-dejar-rastro-en-la-factura",
                "story_slug": "genero",
                "story_title": "El número 016 y las dieciséis semanas: una transformación social",
                "objectives": [
                    "Conocer las leyes españolas de igualdad efectiva entre mujeres y hombres y contra la violencia de género.",
                    "Recordar el número de teléfono 016 (gratuito, confidencial, 24 horas y que no deja rastro en la factura telefónica).",
                    "Dominar la expresión «no dejar rastro en la factura» y los permisos iguales por nacimiento y cuidado de menor."
                ],
                "vocab": [
                    {"lemma": "la violencia de género", "pos": "noun", "translation": "gender-based violence"},
                    {"lemma": "el teléfono 016", "pos": "noun", "translation": "016 helpline against gender violence"},
                    {"lemma": "no dejar rastro", "pos": "verb", "translation": "to leave no trace"},
                    {"lemma": "la factura telefónica", "pos": "noun", "translation": "phone bill"},
                    {"lemma": "la brecha salarial", "pos": "noun", "translation": "gender pay gap"},
                    {"lemma": "la corresponsabilidad", "pos": "noun", "translation": "co-responsibility (in family care)"},
                    {"lemma": "el permiso de nacimiento", "pos": "noun", "translation": "parental leave (16 weeks)"},
                    {"lemma": "la conciliación laboral y familiar", "pos": "noun", "translation": "work-life balance"}
                ],
                "grammar_title": "Garantías de protección: «gratuito, confidencial y que no deja rastro en la factura»",
                "grammar_text": "Para describir el funcionamiento del servicio público **016** de atención a las víctimas de violencia contra las mujeres, se emplea la locución verbal **«no dejar rastro en la factura»** (*la llamada al 016 es gratuita y no deja rastro en la factura telefónica*), aunque sí conviene borrarla del registro de llamadas del propio teléfono móvil.",
                "grammar_examples": [
                    {"es": "El teléfono 016 atiende a las víctimas de violencia de género las veinticuatro horas y no deja rastro en la factura.", "en": "The 016 phone line assists victims of gender violence twenty-four hours a day and leaves no trace on the phone bill."},
                    {"es": "En España ambos progenitores disfrutan de un permiso igual e intransferible por nacimiento y cuidado del menor.", "en": "In Spain both parents enjoy an equal and non-transferable leave for birth and childcare."}
                ],
                "grammar_tip": "Pregunta fija del examen CCSE: el número de información y asesoramiento jurídico contra la violencia de género es el 016 (gratuito y no deja rastro en la factura).",
                "paragraphs": [
                    "En las últimas décadas, España se ha situado en la vanguardia europea de las políticas de igualdad entre mujeres y hombres. En diciembre de 2004, el Congreso de los Diputados aprobó por unanimidad la Ley Orgánica 1/2004 de Medidas de Protección Integral contra la Violencia de Género, una norma pionera que creó juzgados especializados en violencia sobre la mujer y articuló medidas de asistencia jurídica, psicológica y económica para las víctimas.",
                    "Dentro de esa red de protección destaca un número de tres cifras que todo ciudadano debe conocer: el 016. El teléfono 016 ofrece información y asesoramiento jurídico en materia de violencia contra las mujeres las 24 horas del día, los 365 días del año, en decenas de idiomas y con accesibilidad para personas con discapacidad auditiva o del habla.",
                    "Una característica fundamental del 016 es que la llamada es totalmente gratuita, confidencial y no deja rastro en la factura telefónica, para proteger la seguridad de la mujer en caso de que el agresor revise los recibos domésticos (aunque se recomienda borrarla del historial de llamadas del propio dispositivo móvil). En situaciones de peligro inmediato, también se puede llamar al 112 o utilizar la aplicación móvil AlertCops.",
                    "Tres años después de aquella ley, las Cortes aprobaron la Ley Orgánica 3/2007 para la igualdad efectiva de mujeres y hombres, gestionada con el apoyo del Instituto de las Mujeres (adscrito al Ministerio de Igualdad). Esta legislación impulsa la presencia equilibrada de mujeres y hombres en los órganos de decisión, combate la brecha salarial y protege a las trabajadoras frente al acoso laboral y la discriminación por embarazo o maternidad.",
                    "Además, desde 2021 España equiparó por completo los permisos de maternidad y paternidad bajo un único permiso por nacimiento y cuidado de menor de 16 semanas, retribuido al cien por cien e intransferible para cada progenitor, fomentando la corresponsabilidad en el cuidado de los hijos y la conciliación de la vida familiar y laboral."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es el número de teléfono gratuito y confidencial de información y asesoramiento contra la violencia de género en España, que no deja rastro en la factura?",
                        "options": ["016", "060", "091", "1004"],
                        "correctIndex": 0,
                        "explanation": "El teléfono 016 atiende a las víctimas de violencia de género las 24 horas, es gratuito y no deja rastro en la factura telefónica."
                    },
                    {
                        "question": "¿Qué organismo público adscrito al Ministerio de Igualdad promueve la igualdad real entre mujeres y hombres en España?",
                        "options": [
                            "El Instituto de las Mujeres",
                            "El Instituto Geográfico Nacional",
                            "El Instituto Cervantes",
                            "El Instituto de Crédito Oficial"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Instituto de las Mujeres es el organismo estatal encargado de promover la igualdad entre mujeres y hombres."
                    },
                    {
                        "question": "¿Cómo son en España los permisos por nacimiento y cuidado de menor para ambos progenitores?",
                        "options": [
                            "Iguales e intransferibles para ambos progenitores (16 semanas retribuidas al 100 %)",
                            "Exclusivos para la madre y prohibidos para el padre",
                            "Sin sueldo durante todo el primer año",
                            "Solo de dos días naturales"
                        ],
                        "correctIndex": 0,
                        "explanation": "España equiparó los permisos por nacimiento y cuidado del menor a 16 semanas iguales e intransferibles para cada progenitor."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué característica especial tiene la llamada al teléfono 016 para proteger a la víctima?",
                        "options": [
                            "Es gratuita y no deja rastro en la factura telefónica",
                            "Cuesta diez euros por minuto",
                            "Envía una carta certificada al domicilio al día siguiente",
                            "Solo funciona los lunes por la mañana"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 016 es gratuito, funciona las 24 horas y no aparece reflejado en la factura telefónica."
                    },
                    {
                        "prompt": "¿Qué ley española fue aprobada por unanimidad en 2004 para proteger a las mujeres frente al maltrato?",
                        "options": [
                            "La Ley Orgánica de Medidas de Protección Integral contra la Violencia de Género",
                            "La Ley de Aguas y Costas",
                            "La Ley de Propiedad Horizontal",
                            "El Reglamento General de Circulación"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Ley Orgánica 1/2004 estableció la protección integral contra la violencia de género en España."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El teléfono ___ ofrece información y asesoramiento jurídico a las víctimas de violencia de género.",
                        "answer": "016",
                        "options": ["016", "060", "080", "092"],
                        "explanation": "El 016 es el teléfono de atención a víctimas de violencia de género.",
                        "english": "The 016 phone line offers information and legal advice to victims of gender violence."
                    },
                    {
                        "sentence": "Las llamadas al servicio 016 son gratuitas y no dejan ___ en la factura telefónica.",
                        "answer": "rastro",
                        "options": ["rastro", "impuesto", "escaño", "estatuto"],
                        "explanation": "«No dejar rastro en la factura» protege la confidencialidad de la llamada.",
                        "english": "Calls to the 016 service are free and leave no trace on the phone bill."
                    }
                ],
                "ex_dict": {
                    "audioText": "El teléfono cero dieciséis atiende a las víctimas de violencia de género y no deja rastro en la factura.",
                    "english": "The zero-one-six telephone line assists victims of gender violence and leaves no trace on the bill."
                },
                "ex_sb": {
                    "words": ["El", "Instituto", "de", "las", "Mujeres", "promueve", "la", "igualdad", "entre", "mujeres", "y", "hombres."],
                    "english": "The Institute of Women promotes equality between women and men."
                }
            },
            {
                "num": "03",
                "Title": "Matrimonio, Modelos de Familia y Filiación",
                "title": "Matrimonio, Modelos de Familia y Filiación",
                "grammar_slug": "con-independencia-de-su-filiacion",
                "story_slug": "matrimonio",
                "story_title": "Plena igualdad jurídica: del matrimonio igualitario de 2005 a la protección de los hijos",
                "objectives": [
                    "Comprender los artículos 32 y 39 CE sobre el matrimonio con plena igualdad jurídica y la protección de la familia.",
                    "Recordar la legalización del matrimonio entre personas del mismo sexo en España en 2005 y la igualdad absoluta de los hijos con independencia de su filiación.",
                    "Utilizar la expresión «con independencia de su filiación o del estado civil de sus padres»."
                ],
                "vocab": [
                    {"lemma": "la plena igualdad jurídica", "pos": "noun", "translation": "full legal equality"},
                    {"lemma": "el matrimonio igualitario", "pos": "noun", "translation": "same-sex / equal marriage"},
                    {"lemma": "la pareja de hecho", "pos": "noun", "translation": "registered civil partnership"},
                    {"lemma": "la filiación", "pos": "noun", "translation": "parentage / filiation"},
                    {"lemma": "el estado civil", "pos": "noun", "translation": "marital status"},
                    {"lemma": "la familia monoparental", "pos": "noun", "translation": "single-parent family"},
                    {"lemma": "la familia numerosa", "pos": "noun", "translation": "large family (3+ children)"},
                    {"lemma": "prestar asistencia", "pos": "verb", "translation": "to provide assistance / support"}
                ],
                "grammar_title": "Igualdad familiar: «con plena igualdad jurídica» y «con independencia de su filiación»",
                "grammar_text": "El artículo 32 de la Constitución reconoce el derecho a contraer matrimonio **«con plena igualdad jurídica»**, mientras que el artículo 39 declara que todos los hijos son iguales ante la ley **«con independencia de su filiación»** y que los padres deben prestar asistencia de todo orden a los hijos **«habidos dentro o fuera del matrimonio»**.",
                "grammar_examples": [
                    {"es": "En España todas las personas tienen derecho a contraer matrimonio con plena igualdad jurídica.", "en": "In Spain all persons have the right to marry with full legal equality."},
                    {"es": "Los hijos son iguales ante la ley con independencia de su filiación y del estado civil de sus madres o padres.", "en": "Children are equal before the law regardless of their parentage and the marital status of their mothers or fathers."}
                ],
                "grammar_tip": "Recuerda para el CCSE: España legalizó el matrimonio entre personas del mismo sexo en 2005, y todos los hijos tienen exactamente los mismos derechos nazcan dentro o fuera del matrimonio.",
                "paragraphs": [
                    "El derecho de familia español experimentó una profunda modernización tras la entrada en vigor de la Constitución de 1978. El artículo 32 reconoce que el hombre y la mujer tienen derecho a contraer matrimonio con plena igualdad jurídica, dejando atrás viejas leyes en las que la esposa necesitaba la autorización marital para abrir una cuenta bancaria, trabajar o vender un bien.",
                    "Además, la ley regula las formas de matrimonio (civil o en las formas religiosas legalmente previstas, todas con plenos efectos civiles tras su inscripción en el Registro Civil), la edad y capacidad para contraerlo (18 años, o mayores de 16 años legalmente emancipados), los derechos y deberes de los cónyuges y las causas de separación y disolución mediante el divorcio, regulado en España desde 1981.",
                    "En julio de 2005, las Cortes Generales aprobaron la Ley 13/2005, por la que se modificó el Código Civil para reconocer el matrimonio entre personas del mismo sexo con idénticos derechos y deberes —incluida la adopción conjunta— que los matrimonios heterosexuales. Con aquella ley, España se convirtió en el tercer país del mundo en legalizar el matrimonio igualitario.",
                    "Por su parte, el artículo 39 de la Constitución ordena a los poderes públicos asegurar la protección social, económica y jurídica de la familia en toda su diversidad actual: matrimonios, parejas de hecho inscritas en registros autonómicos, familias monoparentales y familias numerosas (generalmente a partir de tres hijos, o dos si uno tiene discapacidad).",
                    "Ese mismo artículo 39 establece un principio ético y jurídico innegociable: los hijos son iguales ante la ley con independencia de su filiación. Los padres deben prestar asistencia de todo orden a los hijos habidos dentro o fuera del matrimonio, durante su minoría de edad y en los demás casos en que legalmente proceda."
                ],
                "questions": [
                    {
                        "question": "¿En qué año aprobó España la ley que reconoce el matrimonio entre personas del mismo sexo con plenos derechos?",
                        "options": ["En 2005", "En 1978", "En 2019", "En 1992"],
                        "correctIndex": 0,
                        "explanation": "La Ley 13/2005 convirtió a España en uno de los primeros países del mundo en legalizar el matrimonio igualitario."
                    },
                    {
                        "question": "Según el artículo 39 de la Constitución Española, ¿tienen los mismos derechos los hijos nacidos dentro y fuera del matrimonio?",
                        "options": [
                            "Sí, todos los hijos son iguales ante la ley con independencia de su filiación",
                            "No, solo tienen derechos de herencia los nacidos dentro del matrimonio",
                            "Depende de la comunidad autónoma donde nazcan",
                            "Solo si los padres están casados por la Iglesia"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 39 CE garantiza la igualdad absoluta de los hijos ante la ley y el deber de los padres de asistir a los hijos habidos dentro o fuera del matrimonio."
                    },
                    {
                        "question": "¿Qué categoría legal recibe en España de forma general una familia integrada por uno o dos ascendientes y tres o más hijos?",
                        "options": [
                            "Familia numerosa",
                            "Mancomunidad provincial",
                            "Colegio profesional",
                            "Corporación municipal"
                        ],
                        "correctIndex": 0,
                        "explanation": "En España, las familias con tres o más hijos (o dos en supuestos especiales como discapacidad) reciben el título de familia numerosa."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cómo es la posición jurídica de los dos cónyuges dentro del matrimonio en España?",
                        "options": [
                            "Tienen plena igualdad jurídica en derechos y deberes",
                            "Uno de los cónyuges tiene autoridad legal sobre el otro",
                            "No pueden divorciarse bajo ningún concepto",
                            "Necesitan permiso municipal para abrir cuentas bancarias"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 32 CE garantiza el derecho a contraer matrimonio con plena igualdad jurídica."
                    },
                    {
                        "prompt": "¿Cuál es la obligación constitucional de los padres respecto a los hijos menores de edad?",
                        "options": [
                            "Prestar asistencia de todo orden a los hijos habidos dentro o fuera del matrimonio",
                            "Prestar asistencia únicamente a los hijos mayores de 25 años",
                            "Elegir obligatoriamente su profesión futura",
                            "Inscribirlos en un partido político"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 39.3 CE impone el deber de prestar asistencia de todo orden a los hijos habidos dentro o fuera del matrimonio."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En España el matrimonio se contrae con plena ___ jurídica entre ambos cónyuges.",
                        "answer": "igualdad",
                        "options": ["igualdad", "jerarquía", "inmunidad", "censura"],
                        "explanation": "El artículo 32 CE establece la plena igualdad jurídica en el matrimonio.",
                        "english": "In Spain marriage is entered into with full legal equality between both spouses."
                    },
                    {
                        "sentence": "Los padres deben prestar ___ de todo orden a los hijos habidos dentro o fuera del matrimonio.",
                        "answer": "asistencia",
                        "options": ["asistencia", "abstención", "sanción", "regencia"],
                        "explanation": "«Prestar asistencia de todo orden a los hijos» es la obligación del artículo 39.3 CE.",
                        "english": "Parents must provide assistance of every kind to children born inside or outside marriage."
                    }
                ],
                "ex_dict": {
                    "audioText": "Todos los hijos son iguales ante la ley con independencia de que nazcan dentro o fuera del matrimonio.",
                    "english": "All children are equal before the law regardless of whether they are born inside or outside marriage."
                },
                "ex_sb": {
                    "words": ["España", "reconoce", "el", "matrimonio", "entre", "personas", "del", "mismo", "sexo", "con", "plena", "igualdad."],
                    "english": "Spain recognizes marriage between persons of the same sex with full equality."
                }
            },
            {
                "num": "04",
                "Title": "Inclusión, Accesibilidad y Personas con Discapacidad",
                "title": "Inclusión, Accesibilidad y Personas con Discapacidad",
                "grammar_slug": "reforma-constitucional-personas-con-discapacidad",
                "story_slug": "discapacidad",
                "story_title": "Enero de 2024 y el cupón de la ONCE: dignidad en el artículo 49",
                "objectives": [
                    "Conocer la histórica reforma constitucional del artículo 49 CE en 2024 que consagró la expresión «personas con discapacidad».",
                    "Identificar el papel social de la ONCE (Organización Nacional de Ciegos Españoles) y del CERMI.",
                    "Dominar el vocabulario de accesibilidad universal, autonomía personal e inclusión laboral."
                ],
                "vocab": [
                    {"lemma": "la persona con discapacidad", "pos": "noun", "translation": "person with a disability"},
                    {"lemma": "la accesibilidad universal", "pos": "noun", "translation": "universal accessibility"},
                    {"lemma": "la autonomía personal", "pos": "noun", "translation": "personal autonomy"},
                    {"lemma": "la inclusión social", "pos": "noun", "translation": "social inclusion"},
                    {"lemma": "la ONCE", "pos": "noun", "translation": "National Organization of Spanish Blind People"},
                    {"lemma": "la reserva de plazas", "pos": "noun", "translation": "job quota / reserved positions"},
                    {"lemma": "el entorno universalmente accesible", "pos": "noun", "translation": "universally accessible environment"},
                    {"lemma": "la dependencia", "pos": "noun", "translation": "dependency / long-term care need"}
                ],
                "grammar_title": "Lenguaje de derechos y dignidad: la reforma del artículo 49 CE (2024)",
                "grammar_text": "En enero de 2024, las Cortes Generales aprobaron la **tercera reforma de la Constitución Española** para renovar íntegramente el **artículo 49**: se eliminó un término arcaico de 1978 y se sustituyó por **«personas con discapacidad»**, reconociendo su derecho a ejercer los derechos en **«condiciones de libertad e igualdad reales y efectivas»** y en **«entornos universalmente accesibles»**.",
                "grammar_examples": [
                    {"es": "El artículo 49 reformado en 2024 garantiza la plena autonomía personal y la inclusión social de las personas con discapacidad.", "en": "Article 49, amended in 2024, guarantees the full personal autonomy and social inclusion of persons with disabilities."},
                    {"es": "La ONCE realiza una extraordinaria labor de inclusión laboral y educativa en toda España.", "en": "ONCE carries out extraordinary work in labor and educational inclusion throughout Spain."}
                ],
                "grammar_tip": "Recuerda para el CCSE: el artículo 49 CE fue reformado en 2024 para consagrar los derechos de las «personas con discapacidad», y la ONCE es la Organización Nacional de Ciegos Españoles.",
                "paragraphs": [
                    "En enero de 2024 se vivió en el hemiciclo del Congreso de los Diputados una jornada histórica y profundamente emotiva. Desde la tribuna de invitados, representantes de las organizaciones de la discapacidad aplaudieron la aprobación de la tercera reforma de la Constitución Española de 1978: la nueva redacción íntegra del artículo 49.",
                    "El texto original de 1978 empleaba un vocabulario asistencialista propio de otra época. La reforma de 2024 lo sustituyó por la expresión «personas con discapacidad» y situó en el centro los derechos humanos: las personas con discapacidad ejercen los derechos previstos en el Título I en condiciones de libertad e igualdad reales y efectivas, y los poderes públicos impulsarán las políticas que garanticen su plena autonomía personal y su inclusión social en entornos universalmente accesibles.",
                    "Además, el nuevo artículo 49 introdujo una mención expresa para atender las necesidades específicas de las mujeres y los menores con discapacidad, reconociendo la doble barrera a la que a menudo se enfrentan en la vida cotidiana y laboral.",
                    "En la sociedad española, una institución ocupa un lugar único en el corazón de los ciudadanos desde su fundación en 1938: la ONCE (Organización Nacional de Ciegos Españoles). Gracias a la venta de su célebre cupón diario y de sus juegos responsables, la ONCE y la Fundación ONCE financian educación inclusiva, perros guía, tecnología adaptada y decenas de miles de empleos para personas con ceguera u otras discapacidades.",
                    "Junto a la ONCE y al CERMI (Comité Español de Representantes de Personas con Discapacidad), la legislación española establece cuotas de reserva de empleo (al menos el 2 % de la plantilla en empresas de 50 o más trabajadores y al menos el 7 % de las plazas en las ofertas de empleo público del Estado) y el Sistema para la Autonomía y Atención a la Dependencia."
                ],
                "questions": [
                    {
                        "question": "¿Qué artículo de la Constitución Española fue reformado en enero de 2024 para actualizar su lenguaje y reforzar los derechos de las personas con discapacidad?",
                        "options": ["El artículo 49", "El artículo 2", "El artículo 116", "El artículo 168"],
                        "correctIndex": 0,
                        "explanation": "En enero de 2024 se reformó el artículo 49 de la Constitución para consagrar los derechos de las «personas con discapacidad»."
                    },
                    {
                        "question": "¿Qué significan las siglas de la histórica organización social española ONCE?",
                        "options": [
                            "Organización Nacional de Ciegos Españoles",
                            "Oficina Nacional de Comercio Exterior",
                            "Organismo de Navegación de las Costas Españolas",
                            "Orden Nacional de Consejeros Electorales"
                        ],
                        "correctIndex": 0,
                        "explanation": "La ONCE es la Organización Nacional de Ciegos Españoles, referente mundial en inclusión social y laboral."
                    },
                    {
                        "question": "¿Qué garantizan las políticas públicas del artículo 49 CE a las personas con discapacidad?",
                        "options": [
                            "Su plena autonomía personal e inclusión social en entornos universalmente accesibles",
                            "La prohibición de acceder a las universidades públicas",
                            "La pérdida del derecho de sufragio",
                            "El aislamiento respecto al mercado laboral"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 49 CE garantiza la plena autonomía personal y la inclusión social en entornos universalmente accesibles."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál es la labor principal de la ONCE y de la Fundación ONCE en España?",
                        "options": [
                            "La inclusión social, educativa y laboral de las personas ciegas y con otras discapacidades",
                            "La recaudación de los impuestos aduaneros",
                            "El control del tráfico aéreo civil",
                            "La gestión de los embalses hidrográficos"
                        ],
                        "correctIndex": 0,
                        "explanation": "La ONCE y la Fundación ONCE dedican sus recursos a la inclusión de personas ciegas y con discapacidad."
                    },
                    {
                        "prompt": "¿A qué dos grupos presta atención específica el artículo 49 CE tras su reforma de 2024?",
                        "options": [
                            "A las mujeres y a los menores con discapacidad",
                            "Solo a los deportistas profesionales",
                            "Exclusivamente a los diplomáticos extranjeros",
                            "A los senadores vitalicios"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 49.2 CE ordena atender particularmente las necesidades específicas de las mujeres y los menores con discapacidad."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La reforma constitucional de 2024 actualizó el artículo 49 para garantizar los derechos de las personas con ___.",
                        "answer": "discapacidad",
                        "options": ["discapacidad", "aforamiento", "inmunidad", "regencia"],
                        "explanation": "El artículo 49 CE consagra los derechos de las personas con discapacidad.",
                        "english": "The 2024 constitutional reform updated Article 49 to guarantee the rights of persons with disabilities."
                    },
                    {
                        "sentence": "La ___ es la Organización Nacional de Ciegos Españoles y promueve la inclusión social y laboral.",
                        "answer": "ONCE",
                        "options": ["ONCE", "AEAT", "DGT", "RAE"],
                        "explanation": "ONCE son las siglas de la Organización Nacional de Ciegos Españoles.",
                        "english": "ONCE is the National Organization of Spanish Blind People and promotes social and labor inclusion."
                    }
                ],
                "ex_dict": {
                    "audioText": "El artículo cuarenta y nueve garantiza la plena autonomía personal y la inclusión social de las personas con discapacidad.",
                    "english": "Article forty-nine guarantees the full personal autonomy and social inclusion of persons with disabilities."
                },
                "ex_sb": {
                    "words": ["La", "ONCE", "es", "la", "Organización", "Nacional", "de", "Ciegos", "Españoles."],
                    "english": "ONCE is the National Organization of Spanish Blind People."
                }
            },
            {
                "num": "05",
                "Title": "Extranjería, Asilo y Adquisición de la Nacionalidad",
                "title": "Extranjería, Asilo y Adquisición de la Nacionalidad",
                "grammar_slug": "plazo-de-residencia-legal-y-continuada",
                "story_slug": "extranjeria",
                "story_title": "Diez, cinco, dos o un año: los caminos legales hacia la nacionalidad española",
                "objectives": [
                    "Comprender los artículos 11 y 13 CE sobre nacionalidad española y derechos de los extranjeros.",
                    "Dominar los plazos exactos de residencia legal para adquirir la nacionalidad española: 10 años (general), 5 años (refugiados), 2 años (iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o sefardíes) y 1 año (nacidos en España o casados con español/a).",
                    "Practicar la expresión «residencia legal, continuada e inmediatamente anterior a la petición»."
                ],
                "vocab": [
                    {"lemma": "la nacionalidad por residencia", "pos": "noun", "translation": "nationality by residence"},
                    {"lemma": "la residencia legal y continuada", "pos": "noun", "translation": "legal and continuous residence"},
                    {"lemma": "el derecho de asilo", "pos": "noun", "translation": "right of asylum"},
                    {"lemma": "la condición de refugiado", "pos": "noun", "translation": "refugee status"},
                    {"lemma": "la doble nacionalidad", "pos": "noun", "translation": "dual nationality"},
                    {"lemma": "el origen sefardí", "pos": "noun", "translation": "Sephardic origin"},
                    {"lemma": "la buena conducta cívica", "pos": "noun", "translation": "good civic conduct"},
                    {"lemma": "el grado de integración", "pos": "noun", "translation": "degree of integration"}
                ],
                "grammar_title": "Plazos legales de nacionalidad: «diez, cinco, dos o un año de residencia»",
                "grammar_text": "Según el artículo 22 del Código Civil español, para adquirir la **nacionalidad por residencia** esta debe ser **legal, continuada e inmediatamente anterior a la petición**, con cuatro plazos que suelen preguntarse en el CCSE: **10 años** (plazo general), **5 años** (refugiados), **2 años** (países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o sefardíes) y **1 año** (nacidos en España o casados durante un año con español/a).",
                "grammar_examples": [
                    {"es": "El plazo general para solicitar la nacionalidad española por residencia es de diez años legales y continuados.", "en": "The general period to apply for Spanish nationality by residence is ten legal and continuous years."},
                    {"es": "Para los nacionales de países iberoamericanos o de Portugal bastan dos años de residencia legal.", "en": "For nationals of Ibero-American countries or Portugal, two years of legal residence are sufficient."}
                ],
                "grammar_tip": "Memoriza los 4 plazos del Código Civil para la nacionalidad por residencia: 10 años (general), 5 años (refugiados), 2 años (Iberoamérica, Andorra, Filipinas, Guinea Ecuatorial, Portugal, sefardíes) y 1 año (nacido en España o cónyuge de español/a).",
                "paragraphs": [
                    "El artículo 11 de la Constitución Española establece que la nacionalidad española se adquiere, se conserva y se pierde de acuerdo con lo establecido por la ley, y añade una garantía inviolable: ningún español de origen podrá ser privado de su nacionalidad. Además, el Estado puede concertar tratados de doble nacionalidad con los países iberoamericanos o con aquellos que hayan tenido o tengan una particular vinculación con España.",
                    "A su vez, el artículo 13 dispone que los extranjeros gozarán en España de las libertades públicas que garantiza el Título I en los términos que establezcan los tratados y la ley, y regula el derecho de asilo para los ciudadanos de otros países y los apátridas perseguidos en su lugar de origen.",
                    "¿Cómo se obtiene la nacionalidad española por residencia según el Código Civil? El solicitante debe acreditar una residencia en España que sea legal, continuada e inmediatamente anterior a la petición, además de buena conducta cívica (carecer de antecedentes penales) y suficiente grado de integración en la sociedad española (acreditado mediante la prueba CCSE y, si su lengua materna no es el español, el diploma DELE A2 o superior).",
                    "El plazo general de residencia legal exigido en España es de diez años. Sin embargo, la ley reduce ese tiempo en función de las circunstancias personales o históricas del solicitante: serán suficientes cinco años para las personas que hayan obtenido la condición de refugiado.",
                    "El plazo se reduce a dos años cuando se trate de nacionales de origen de países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial o Portugal, o de sefardíes (descendientes de los judíos españoles). Finalmente, basta un solo año de residencia legal para quien haya nacido en territorio español y para quien al tiempo de la solicitud lleve un año casado con un español o española y no esté separado legalmente o de hecho."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es el plazo general de residencia legal y continuada exigido en España para solicitar la nacionalidad por residencia?",
                        "options": ["10 años", "20 años", "3 años", "15 años"],
                        "correctIndex": 0,
                        "explanation": "El artículo 22 del Código Civil fija en 10 años el plazo general de residencia legal y continuada."
                    },
                    {
                        "question": "¿Cuántos años de residencia legal necesitan los nacionales de origen de países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o los sefardíes?",
                        "options": ["2 años", "10 años", "8 años", "6 meses"],
                        "correctIndex": 0,
                        "explanation": "Para iberoamericanos, andorranos, filipinos, ecuatoguineanos, portugueses y sefardíes bastan 2 años de residencia legal."
                    },
                    {
                        "question": "¿Qué plazo de residencia legal se exige a una persona que lleva un año casada con un ciudadano español (sin estar separada) o que ha nacido en territorio español?",
                        "options": ["1 año", "5 años", "10 años", "4 años"],
                        "correctIndex": 0,
                        "explanation": "Basta 1 año de residencia legal para los nacidos en España o casados durante un año con español/a."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuántos años de residencia legal se exigen en España a las personas que han obtenido la condición de refugiado?",
                        "options": ["5 años", "10 años", "15 años", "25 años"],
                        "correctIndex": 0,
                        "explanation": "Para quienes hayan obtenido la condición de refugiado son suficientes 5 años de residencia legal."
                    },
                    {
                        "prompt": "Según el artículo 11.2 de la Constitución, ¿puede un español de origen ser privado de su nacionalidad?",
                        "options": [
                            "No, ningún español de origen podrá ser privado de su nacionalidad",
                            "Sí, por decisión de un alcalde",
                            "Sí, si viaja al extranjero durante un mes",
                            "Sí, al cumplir los 65 años"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 11.2 CE establece que ningún español de origen podrá ser privado de su nacionalidad."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El plazo general para adquirir la nacionalidad española por residencia es de ___ años legales y continuados.",
                        "answer": "diez",
                        "options": ["diez", "dos", "cinco", "veinte"],
                        "explanation": "El plazo general de residencia legal en el Código Civil es de diez años.",
                        "english": "The general period to acquire Spanish nationality by residence is ten legal and continuous years."
                    },
                    {
                        "sentence": "Para los ciudadanos de origen de países iberoamericanos o de Portugal bastan ___ años de residencia legal.",
                        "answer": "dos",
                        "options": ["dos", "diez", "doce", "quince"],
                        "explanation": "Los nacionales de países iberoamericanos, Portugal, Andorra, Filipinas, Guinea Ecuatorial o sefardíes solo necesitan dos años.",
                        "english": "For citizens of origin from Ibero-American countries or Portugal, two years of legal residence are sufficient."
                    }
                ],
                "ex_dict": {
                    "audioText": "Para los nacionales de países iberoamericanos bastan dos años de residencia legal y continuada en España.",
                    "english": "For nationals of Ibero-American countries, two years of legal and continuous residence in Spain are sufficient."
                },
                "ex_sb": {
                    "words": ["Ningún", "español", "de", "origen", "podrá", "ser", "privado", "de", "su", "nacionalidad."],
                    "english": "No Spaniard by origin may be deprived of their nationality."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 15: Deberes Ciudadanos y Sistema Tributario (unit_num=51, b1-deberes)
    # =========================================================================
    {
        "slug": "deberes",
        "unit_num": 51,
        "title": "Deberes Ciudadanos y Sistema Tributario",
        "description": "Deberes constitucionales, Agencia Tributaria (AEAT), impuestos directos (IRPF) e indirectos (IVA), Seguridad Social, DGT y DNI obligatorio desde los 14 años.",
        "Badge": "Deberes e Impuestos",
        "lessons": [
            {
                "num": "01",
                "Title": "Los Deberes Constitucionales de los Ciudadanos",
                "title": "Los Deberes Constitucionales de los Ciudadanos",
                "grammar_slug": "el-derecho-y-el-deber-de",
                "story_slug": "constitucionales",
                "story_title": "Cuando los derechos van acompañados de deberes: defensa, trabajo y emergencias",
                "objectives": [
                    "Identificar los deberes constitucionales de los artículos 30 y 35 CE: defensa de España, colaboración en caso de catástrofe y deber de trabajar.",
                    "Conocer la obligatoriedad del Documento Nacional de Identidad (DNI) a partir de los 14 años.",
                    "Practicar la construcción simétrica «tienen el derecho y el deber de + infinitivo»."
                ],
                "vocab": [
                    {"lemma": "el derecho y el deber", "pos": "noun", "translation": "the right and the duty"},
                    {"lemma": "defender a España", "pos": "verb", "translation": "to defend Spain"},
                    {"lemma": "la objeción de conciencia", "pos": "noun", "translation": "conscientious objection"},
                    {"lemma": "el grave riesgo o catástrofe", "pos": "noun", "translation": "grave risk or catastrophe"},
                    {"lemma": "la calamidad pública", "pos": "noun", "translation": "public calamity"},
                    {"lemma": "el DNI (Documento Nacional de Identidad)", "pos": "noun", "translation": "National Identity Document"},
                    {"lemma": "el TIE (Tarjeta de Identidad de Extranjero)", "pos": "noun", "translation": "Foreigner Identity Card"},
                    {"lemma": "el empadronamiento", "pos": "noun", "translation": "municipal registration (padrón)"}
                ],
                "grammar_title": "Fórmulas de corresponsabilidad: «tienen el derecho y el deber de + infinitivo»",
                "grammar_text": "La Constitución Española une en dos artículos clave la facultad y la obligación ciudadana mediante la coordinación **«el derecho y el deber de»**: *«Los españoles tienen el derecho y el deber de defender a España»* (Art. 30.1 CE) y *«Todos los españoles tienen el deber de trabajar y el derecho al trabajo»* (Art. 35.1 CE).",
                "grammar_examples": [
                    {"es": "Según el artículo 30 de la Constitución, los españoles tienen el derecho y el deber de defender a España.", "en": "According to Article 30 of the Constitution, Spaniards have the right and the duty to defend Spain."},
                    {"es": "En España el Documento Nacional de Identidad (DNI) es obligatorio a partir de los catorce años.", "en": "In Spain the National Identity Document (DNI) is mandatory from fourteen years of age."}
                ],
                "grammar_tip": "Dato muy preguntado en el CCSE: el DNI es obligatorio en España a partir de los 14 años (aunque puede obtenerse desde el nacimiento).",
                "paragraphs": [
                    "La Segunda Sección del Capítulo II del Título I de la Constitución Española lleva por título «De los derechos y deberes de los ciudadanos». La ciudadanía democrática no es únicamente una lista de prestaciones que se reclaman al Estado, sino un pacto de convivencia en el que cada persona asume responsabilidades hacia la comunidad.",
                    "El artículo 30.1 establece que los españoles tienen el derecho y el deber de defender a España. Aunque el servicio militar obligatorio (popularmente llamado «la mili») quedó suspendido en España en el año 2001 para dar paso a unas Fuerzas Armadas totalmente profesionales, el artículo 30 sigue reconociendo la objeción de conciencia y prevé que mediante ley podrán regularse los deberes de los ciudadanos en los casos de grave riesgo, catástrofe o calamidad pública.",
                    "Por su parte, el artículo 35.1 une de nuevo ambas dimensiones en el ámbito económico: todos los españoles tienen el deber de trabajar y el derecho al trabajo, a la libre elección de profesión u oficio, a la promoción a través del trabajo y a una remuneración suficiente para satisfacer sus necesidades y las de su familia, sin que en ningún caso pueda hacerse discriminación por razón de sexo.",
                    "En la vida administrativa cotidiana existen además deberes documentales que todo residente debe conocer para el examen CCSE. El primero es el Documento Nacional de Identidad (DNI), expedido por el Cuerpo Nacional de Policía: en España, el DNI es obligatorio para todos los ciudadanos españoles a partir de los 14 años de edad (si bien los menores de 14 años pueden obtenerlo de forma voluntaria, por ejemplo para viajar).",
                    "El segundo deber cívico es la inscripción en el Padrón Municipal del ayuntamiento donde se reside habitualmente (el empadronamiento), trámite gratuito e indispensable para acreditar el domicilio, acceder al centro de salud correspondiente, escolarizar a los hijos y figurar en el censo electoral."
                ],
                "questions": [
                    {
                        "question": "¿A partir de qué edad es obligatorio poseer el Documento Nacional de Identidad (DNI) para los ciudadanos españoles?",
                        "options": [
                            "A partir de los 14 años",
                            "A partir de los 18 años",
                            "A partir de los 21 años",
                            "Solo al jubilarse"
                        ],
                        "correctIndex": 0,
                        "explanation": "En España el DNI es obligatorio a partir de los 14 años de edad."
                    },
                    {
                        "question": "Según el artículo 30 de la Constitución, ¿en qué situaciones extraordinarias puede la ley regular los deberes de colaboración de los ciudadanos?",
                        "options": [
                            "En los casos de grave riesgo, catástrofe o calamidad pública",
                            "En las inauguraciones de exposiciones artísticas",
                            "Durante los campeonatos deportivos de verano",
                            "Cuando se estrena una película española"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 30.4 CE prevé que mediante ley se regulen los deberes ciudadanos en casos de grave riesgo, catástrofe o calamidad pública."
                    },
                    {
                        "question": "¿Qué registro municipal acredita la residencia habitual de cualquier vecino en un municipio español?",
                        "options": [
                            "El Padrón Municipal (empadronamiento)",
                            "El Registro Mercantil Central",
                            "El Catastro Vitivinícola",
                            "El Boletín de Propiedad Industrial"
                        ],
                        "correctIndex": 0,
                        "explanation": "Toda persona que viva en España está obligada a inscribirse en el Padrón del municipio en el que resida habitualmente."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Existe actualmente el servicio militar obligatorio en España?",
                        "options": [
                            "No, quedó suspendido en 2001 y las Fuerzas Armadas son profesionales",
                            "Sí, dura tres años para todos los mayores de 18 años",
                            "Sí, es obligatorio durante seis meses cada verano",
                            "Solo es obligatorio en las ciudades costeras"
                        ],
                        "correctIndex": 0,
                        "explanation": "El servicio militar obligatorio quedó suspendido en España en 2001."
                    },
                    {
                        "prompt": "¿Qué cuerpo de seguridad expide el DNI y el pasaporte en España?",
                        "options": [
                            "El Cuerpo Nacional de Policía (Policía Nacional)",
                            "La Policía Local",
                            "Los Bomberos Municipales",
                            "Protección Civil"
                        ],
                        "correctIndex": 0,
                        "explanation": "La expedición del DNI y del pasaporte es competencia exclusiva de la Policía Nacional."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En España, el Documento Nacional de Identidad (DNI) es obligatorio a partir de los ___ años.",
                        "answer": "catorce",
                        "options": ["catorce", "dieciocho", "veintiún", "diez"],
                        "explanation": "El DNI es obligatorio desde los 14 años.",
                        "english": "In Spain, the National Identity Document (DNI) is mandatory from fourteen years of age."
                    },
                    {
                        "sentence": "Los españoles tienen el derecho y el ___ de defender a España según el artículo 30 de la Constitución.",
                        "answer": "deber",
                        "options": ["deber", "tributo", "escaño", "indulto"],
                        "explanation": "«Tienen el derecho y el deber de defender a España» (Art. 30.1 CE).",
                        "english": "Spaniards have the right and the duty to defend Spain according to Article 30 of the Constitution."
                    }
                ],
                "ex_dict": {
                    "audioText": "En España el Documento Nacional de Identidad es obligatorio a partir de los catorce años.",
                    "english": "In Spain the National Identity Document is mandatory from fourteen years of age."
                },
                "ex_sb": {
                    "words": ["Todos", "los", "españoles", "tienen", "el", "deber", "de", "trabajar", "y", "el", "derecho", "al", "trabajo."],
                    "english": "All Spaniards have the duty to work and the right to work."
                }
            },
            {
                "num": "02",
                "Title": "El Sistema Tributario y la Agencia Tributaria",
                "title": "El Sistema Tributario y la Agencia Tributaria",
                "grammar_slug": "de-acuerdo-con-su-capacidad-economica",
                "story_slug": "tributos",
                "story_title": "Hacienda somos todos: capacidad económica, progresividad y servicios públicos",
                "objectives": [
                    "Comprender el artículo 31 CE: contribuir al sostenimiento de los gastos públicos según la capacidad económica.",
                    "Identificar los principios del sistema tributario (igualdad, progresividad y no confiscatoriedad) y el papel de la Agencia Tributaria (AEAT).",
                    "Practicar las expresiones «de acuerdo con su capacidad económica» y «inspirado en los principios de igualdad y progresividad»."
                ],
                "vocab": [
                    {"lemma": "el sostenimiento de los gastos públicos", "pos": "noun", "translation": "financing / maintenance of public expenditure"},
                    {"lemma": "la capacidad económica", "pos": "noun", "translation": "economic capacity"},
                    {"lemma": "el sistema tributario", "pos": "noun", "translation": "tax system"},
                    {"lemma": "la progresividad", "pos": "noun", "translation": "progressivity (paying a higher rate as income rises)"},
                    {"lemma": "el alcance confiscatorio", "pos": "noun", "translation": "confiscatory scope"},
                    {"lemma": "la Agencia Tributaria (AEAT)", "pos": "noun", "translation": "Spanish Tax Agency"},
                    {"lemma": "el contribuyente", "pos": "noun", "translation": "taxpayer"},
                    {"lemma": "la recaudación fiscal", "pos": "noun", "translation": "tax collection / revenue"}
                ],
                "grammar_title": "Principios fiscales: «de acuerdo con su capacidad económica» y «alcance confiscatorio»",
                "grammar_text": "El artículo 31.1 de la Constitución resume la justicia fiscal en una sola frase: **«Todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica mediante un sistema tributario justo inspirado en los principios de igualdad y progresividad que, en ningún caso, tendrá alcance confiscatorio»**.",
                "grammar_examples": [
                    {"es": "Todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica.", "en": "Everyone shall contribute to the financing of public expenditure in accordance with their economic capacity."},
                    {"es": "El sistema tributario español está inspirado en los principios de igualdad y progresividad.", "en": "The Spanish tax system is inspired by the principles of equality and progressivity."}
                ],
                "grammar_tip": "Recuerda para el CCSE: los impuestos sirven para financiar los servicios públicos (sanidad, educación, pensiones, infraestructuras) y la Agencia Tributaria (AEAT) es el organismo que los recauda.",
                "paragraphs": [
                    "¿De dónde salen los recursos para que un hospital público realice un trasplante gratuito, para que los colegios e institutos públicos funcionen en cada barrio o para que los trenes de alta velocidad conecten las ciudades españolas? La respuesta se encuentra en el artículo 31 de la Constitución Española, dedicado al deber de contribuir a los gastos públicos.",
                    "Su primer apartado establece que todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica, mediante un sistema tributario justo inspirado en los principios de igualdad y progresividad que, en ningún caso, tendrá alcance confiscatorio.",
                    "¿Qué significa el principio de progresividad? Significa que no todo el mundo paga exactamente la misma cuota fija, sino que quienes tienen mayor renta o mayor patrimonio aportan un porcentaje mayor que quienes disponen de menos recursos. Al mismo tiempo, la prohibición de alcance confiscatorio garantiza que los impuestos nunca puedan privar al ciudadano de una parte sustancial de su propiedad o de su sustento.",
                    "El segundo apartado del artículo 31 añade la otra cara de la moneda: el gasto público realizará una asignación equitativa de los recursos públicos, y su programación y ejecución responderán a los criterios de eficiencia y economía. Pagar impuestos y gestionar honradamente cada euro público son, por tanto, dos deberes inseparables.",
                    "En España, el organismo público adscrito al Ministerio de Hacienda encargado de la aplicación efectiva del sistema tributario estatal y aduanero es la Agencia Estatal de Administración Tributaria, conocida por todos los ciudadanos como la Agencia Tributaria o por sus siglas AEAT (excepto en el País Vasco y Navarra, que cuentan con sus propias Haciendas Forales)."
                ],
                "questions": [
                    {
                        "question": "Según el artículo 31 de la Constitución Española, ¿en qué principios debe inspirarse el sistema tributario?",
                        "options": [
                            "En los principios de igualdad y progresividad, de acuerdo con la capacidad económica y sin alcance confiscatorio",
                            "En que las personas con menos ingresos paguen el doble de impuestos",
                            "En la confiscación total de los ahorros familiares",
                            "En la voluntariedad absoluta del pago de impuestos"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 31.1 CE establece que todos contribuirán según su capacidad económica mediante un sistema justo inspirado en la igualdad y la progresividad, sin alcance confiscatorio."
                    },
                    {
                        "question": "¿Qué organismo del Estado se encarga de gestionar y recaudar los impuestos estatales en España?",
                        "options": [
                            "La Agencia Tributaria (AEAT)",
                            "La Dirección General de Tráfico (DGT)",
                            "El Instituto Nacional de las Artes Escénicas",
                            "El Consejo Superior de Deportes"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Agencia Estatal de Administración Tributaria (AEAT), adscrita al Ministerio de Hacienda, gestiona los tributos estatales."
                    },
                    {
                        "question": "¿Para qué sirven principalmente los impuestos que pagan los ciudadanos y las empresas en España?",
                        "options": [
                            "Para financiar los gastos y servicios públicos como la sanidad, la educación, las infraestructuras y la seguridad",
                            "Únicamente para pagar campañas publicitarias privadas",
                            "Para financiar clubes deportivos extranjeros",
                            "No tienen ningún destino público"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los impuestos financian los servicios públicos esenciales del Estado del bienestar."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿A qué ministerio pertenece la Agencia Tributaria (AEAT)?",
                        "options": [
                            "Al Ministerio de Hacienda",
                            "Al Ministerio de Cultura",
                            "Al Ministerio de Sanidad",
                            "Al Ministerio de Agricultura"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Agencia Tributaria está adscrita al Ministerio de Hacienda."
                    },
                    {
                        "prompt": "¿Qué significa que un impuesto es progresivo?",
                        "options": [
                            "Que pagan un porcentaje mayor quienes tienen mayor capacidad económica",
                            "Que solo lo pagan los jubilados",
                            "Que desaparece cada mes de agosto",
                            "Que se paga únicamente en monedas metálicas"
                        ],
                        "correctIndex": 0,
                        "explanation": "La progresividad fiscal implica que el tipo impositivo aumenta conforme crece la capacidad económica del contribuyente."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su ___ económica.",
                        "answer": "capacidad",
                        "options": ["capacidad", "provincia", "inmunidad", "lengua"],
                        "explanation": "«De acuerdo con su capacidad económica» es la expresión del artículo 31.1 CE.",
                        "english": "Everyone shall contribute to the maintenance of public expenditure in accordance with their economic capacity."
                    },
                    {
                        "sentence": "El sistema tributario español está inspirado en los principios de igualdad y ___.",
                        "answer": "progresividad",
                        "options": ["progresividad", "censura", "vitalidad", "regencia"],
                        "explanation": "Igualdad y progresividad son los dos principios del artículo 31.1 CE.",
                        "english": "The Spanish tax system is inspired by the principles of equality and progressivity."
                    }
                ],
                "ex_dict": {
                    "audioText": "Todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica.",
                    "english": "Everyone shall contribute to the financing of public expenditure in accordance with their economic capacity."
                },
                "ex_sb": {
                    "words": ["La", "Agencia", "Tributaria", "se", "encarga", "de", "recaudar", "los", "impuestos", "del", "Estado."],
                    "english": "The Tax Agency is responsible for collecting State taxes."
                }
            },
            {
                "num": "03",
                "Title": "Impuestos Directos e Indirectos: IRPF, IVA y Sociedades",
                "title": "Impuestos Directos e Indirectos: IRPF, IVA y Sociedades",
                "grammar_slug": "gravar-la-renta-frente-al-consumo",
                "story_slug": "impuestos",
                "story_title": "IRPF, IVA e IBI: el mapa práctico de los impuestos en la vida diaria",
                "objectives": [
                    "Distinguir con precisión entre impuestos directos (IRPF, Impuesto sobre Sociedades) e impuestos indirectos (IVA, Impuestos Especiales).",
                    "Conocer qué grava el IRPF (la renta de las personas físicas), el IVA (el consumo de bienes y servicios) y el IBI (bienes inmuebles municipales).",
                    "Practicar el verbo «gravar» y la clasificación fiscal."
                ],
                "vocab": [
                    {"lemma": "el impuesto directo", "pos": "noun", "translation": "direct tax"},
                    {"lemma": "el impuesto indirecto", "pos": "noun", "translation": "indirect tax"},
                    {"lemma": "el IRPF (Impuesto sobre la Renta de las Personas Físicas)", "pos": "noun", "translation": "Personal Income Tax"},
                    {"lemma": "el IVA (Impuesto sobre el Valor Añadido)", "pos": "noun", "translation": "Value Added Tax (VAT)"},
                    {"lemma": "el Impuesto sobre Sociedades", "pos": "noun", "translation": "Corporate Income Tax"},
                    {"lemma": "el IBI (Impuesto sobre Bienes Inmuebles)", "pos": "noun", "translation": "Property Tax (municipal)"},
                    {"lemma": "gravar", "pos": "verb", "translation": "to tax / to levy a tax on"},
                    {"lemma": "la declaración de la Renta", "pos": "noun", "translation": "annual income tax return"}
                ],
                "grammar_title": "Léxico fiscal: «gravar la obtención de renta» frente a «gravar el consumo»",
                "grammar_text": "En español jurídico y económico, el verbo **«gravar»** (con *v*) significa imponer una carga fiscal sobre una actividad o bien: *El **IRPF** es un impuesto directo que **grava** la renta de los ciudadanos; el **IVA** es un impuesto indirecto que **grava** el consumo de bienes y servicios*.",
                "grammar_examples": [
                    {"es": "El IRPF es un impuesto directo que grava los ingresos anuales de los trabajadores y profesionales.", "en": "Personal Income Tax (IRPF) is a direct tax that taxes the annual income of workers and professionals."},
                    {"es": "El IVA es un impuesto indirecto que pagamos al comprar un producto o contratar un servicio.", "en": "VAT (IVA) is an indirect tax that we pay when buying a product or hiring a service."}
                ],
                "grammar_tip": "Diferencia esencial para el examen CCSE: el IRPF y el Impuesto sobre Sociedades son impuestos DIRECTOS; el IVA es un impuesto INDIRECTO sobre el consumo.",
                "paragraphs": [
                    "En el examen CCSE aparecen con mucha frecuencia preguntas que piden distinguir entre dos grandes familias de tributos: los impuestos directos y los impuestos indirectos. La diferencia es muy sencilla si nos fijamos en qué grava cada uno.",
                    "Los impuestos directos recaen directamente sobre la renta o el patrimonio de una persona o empresa concreta, teniendo en cuenta su situación económica. El más importante para los ciudadanos es el IRPF (Impuesto sobre la Renta de las Personas Físicas): un tributo personal y progresivo que grava los ingresos obtenidos durante el año (salarios, pensiones, rendimientos de actividades autónomas o del ahorro). Cada primavera, millones de residentes presentan ante la Agencia Tributaria su «declaración de la Renta».",
                    "Junto al IRPF, el otro gran impuesto directo estatal es el Impuesto sobre Sociedades (IS), que grava los beneficios obtenidos por las empresas y personas jurídicas. También existen impuestos directos sobre la riqueza o las herencias, como el Impuesto sobre el Patrimonio o el Impuesto sobre Sucesiones y Donaciones (cedidos en gran medida a las comunidades autónomas).",
                    "Por el contrario, los impuestos indirectos no gravan lo que una persona gana, sino cómo lo gasta: recaen sobre el consumo de bienes y servicios, y se aplican por igual a cualquier comprador en el momento de pagar en una tienda o restaurante. El rey de los impuestos indirectos es el IVA (Impuesto sobre el Valor Añadido). En España existen tres tipos de IVA: el general (21 %), el reducido (10 %, aplicable por ejemplo al transporte de viajeros o la hostelería) y el superreducido (4 %, para productos de primera necesidad como el pan, la leche, los huevos, la fruta, los libros o los medicamentos).",
                    "Finalmente, en el ámbito de los ayuntamientos destacan impuestos locales como el IBI (Impuesto sobre Bienes Inmuebles, que pagan anualmente los propietarios de viviendas o locales) y el Impuesto sobre Vehículos de Tracción Mecánica (el conocido «numerito» o impuesto de circulación del automóvil)."
                ],
                "questions": [
                    {
                        "question": "¿Qué significa la sigla IRPF y qué tipo de impuesto es?",
                        "options": [
                            "Impuesto sobre la Renta de las Personas Físicas, y es un impuesto directo",
                            "Impuesto Regional de Productos Farmacéuticos, y es un impuesto indirecto",
                            "Índice de Recaudación de Puertos y Ferrocarriles, y es una tasa municipal",
                            "Impuesto de Registro de Propiedades Forestales"
                        ],
                        "correctIndex": 0,
                        "explanation": "El IRPF es el Impuesto sobre la Renta de las Personas Físicas y es el principal impuesto directo en España."
                    },
                    {
                        "question": "¿Cuál es el impuesto indirecto que grava el consumo cuando compramos bienes o contratamos servicios en España?",
                        "options": [
                            "El IVA (Impuesto sobre el Valor Añadido)",
                            "El IRPF",
                            "El Impuesto sobre Sociedades",
                            "El Impuesto sobre Sucesiones"
                        ],
                        "correctIndex": 0,
                        "explanation": "El IVA (Impuesto sobre el Valor Añadido) es el impuesto indirecto que recae sobre el consumo."
                    },
                    {
                        "question": "¿Qué impuesto pagan las empresas sobre los beneficios obtenidos en su actividad económica?",
                        "options": [
                            "El Impuesto sobre Sociedades",
                            "El Impuesto sobre Vehículos de Tracción Mecánica",
                            "La tasa de expedición del pasaporte",
                            "El canon de bibliotecas públicas"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Impuesto sobre Sociedades es un impuesto directo que grava los beneficios de las empresas."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál de los siguientes tributos es un impuesto INDIRECTO en España?",
                        "options": [
                            "El IVA (Impuesto sobre el Valor Añadido)",
                            "El IRPF (Impuesto sobre la Renta de las Personas Físicas)",
                            "El Impuesto sobre Sociedades",
                            "El Impuesto sobre el Patrimonio"
                        ],
                        "correctIndex": 0,
                        "explanation": "El IVA es un impuesto indirecto porque grava el consumo de bienes y servicios."
                    },
                    {
                        "prompt": "¿Qué impuesto municipal pagan cada año a su ayuntamiento los propietarios de un piso o una casa?",
                        "options": [
                            "El IBI (Impuesto sobre Bienes Inmuebles)",
                            "El arancel aduanero exterior",
                            "El impuesto especial de hidrocarburos",
                            "El sello postal internacional"
                        ],
                        "correctIndex": 0,
                        "explanation": "El IBI es el tributo local que grava la propiedad de bienes inmuebles."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El ___ es un impuesto directo que grava los ingresos anuales de las personas físicas en España.",
                        "answer": "IRPF",
                        "options": ["IRPF", "IVA", "IBI", "BOE"],
                        "explanation": "El IRPF (Impuesto sobre la Renta de las Personas Físicas) grava los ingresos personales.",
                        "english": "Personal Income Tax (IRPF) is a direct tax that taxes the annual income of natural persons in Spain."
                    },
                    {
                        "sentence": "El ___ es el impuesto indirecto sobre el valor añadido que se paga al consumir productos y servicios.",
                        "answer": "IVA",
                        "options": ["IVA", "IRPF", "DNI", "SMI"],
                        "explanation": "El IVA grava el consumo de bienes y servicios.",
                        "english": "VAT (IVA) is the indirect value-added tax paid when consuming products and services."
                    }
                ],
                "ex_dict": {
                    "audioText": "El IRPF es un impuesto directo sobre la renta y el IVA es un impuesto indirecto sobre el consumo.",
                    "english": "IRPF is a direct tax on income and IVA is an indirect tax on consumption."
                },
                "ex_sb": {
                    "words": ["El", "IVA", "es", "un", "impuesto", "indirecto", "que", "grava", "el", "consumo", "de", "bienes."],
                    "english": "VAT is an indirect tax that taxes the consumption of goods."
                }
            },
            {
                "num": "04",
                "Title": "Seguridad Social, Empleo y Estatuto de los Trabajadores",
                "title": "Seguridad Social, Empleo y Estatuto de los Trabajadores",
                "grammar_slug": "cotizar-a-la-seguridad-social-jornada-maxima",
                "story_slug": "seguridadsocial",
                "story_title": "Nómina, cotizaciones y treinta días de vacaciones: las reglas del trabajo en España",
                "objectives": [
                    "Conocer el sistema de cotizaciones a la Seguridad Social, el Informe de Vida Laboral y el papel del SEPE.",
                    "Recordar los datos clave del Estatuto de los Trabajadores: jornada máxima ordinaria de 40 horas semanales, mínimo de 30 días naturales de vacaciones pagadas al año y el Salario Mínimo Interprofesional (SMI).",
                    "Practicar las construcciones «cotizar a la Seguridad Social» y «en ningún caso inferior a treinta días naturales»."
                ],
                "vocab": [
                    {"lemma": "cotizar a la Seguridad Social", "pos": "verb", "translation": "to contribute to Social Security"},
                    {"lemma": "la vida laboral", "pos": "noun", "translation": "official employment history report"},
                    {"lemma": "el Estatuto de los Trabajadores", "pos": "noun", "translation": "Workers' Statute"},
                    {"lemma": "el Salario Mínimo Interprofesional (SMI)", "pos": "noun", "translation": "Minimum Interprofessional Wage"},
                    {"lemma": "el convenio colectivo", "pos": "noun", "translation": "collective bargaining agreement"},
                    {"lemma": "la prestación por desempleo (el paro)", "pos": "noun", "translation": "unemployment benefit"},
                    {"lemma": "el trabajador autónomo", "pos": "noun", "translation": "self-employed worker"},
                    {"lemma": "el SEPE (Servicio Público de Empleo Estatal)", "pos": "noun", "translation": "State Public Employment Service"}
                ],
                "grammar_title": "Derechos laborales básicos: «treinta días naturales» y «cuarenta horas semanales»",
                "grammar_text": "El **Estatuto de los Trabajadores** establece mínimos legales que ningún contrato puede empeorar: la jornada ordinaria máxima es de **40 horas semanales** de trabajo efectivo de promedio en cómputo anual, y el periodo de vacaciones anuales retribuidas no será **«en ningún caso inferior a treinta días naturales»**.",
                "grammar_examples": [
                    {"es": "En España las vacaciones anuales pagadas no pueden ser en ningún caso inferiores a treinta días naturales.", "en": "In Spain annual paid vacations may in no case be less than thirty calendar days."},
                    {"es": "Tanto las empresas como los trabajadores cotizan mensualmente a la Seguridad Social.", "en": "Both companies and workers contribute monthly to Social Security."}
                ],
                "grammar_tip": "Memoriza para el CCSE: la edad mínima para trabajar en España es de 16 años (con autorización de los padres o tutores), y las vacaciones anuales mínimas son de 30 días naturales.",
                "paragraphs": [
                    "Cuando una persona empieza a trabajar en España —ya sea como asalariada por cuenta ajena en una empresa o por cuenta propia como trabajador autónomo—, debe ser dada de alta y cotizar a la Seguridad Social. Esas aportaciones mensuales de empresas y trabajadores financian las pensiones de jubilación, las bajas por enfermedad o accidente (incapacidad temporal), los permisos por nacimiento de hijo y la asistencia sanitaria.",
                    "Cualquier ciudadano puede solicitar en pocos segundos, por internet o por teléfono, un documento oficial muy útil: el Informe de Vida Laboral, expedido por la Tesorería General de la Seguridad Social (TGSS), donde constan todas las empresas y los días exactos en que ha estado dado de alta. Si un trabajador pierde su empleo de forma involuntaria y ha cotizado al menos 360 días en los últimos seis años, tiene derecho a cobrar la prestación contributiva por desempleo (conocida popularmente como «el paro»), gestionada por el SEPE (Servicio Público de Empleo Estatal).",
                    "La norma fundamental que regula los derechos y deberes en el empleo es el Estatuto de los Trabajadores. En primer lugar, fija la edad mínima legal de admisión al trabajo en los 16 años (coincidiendo con el final de la enseñanza básica obligatoria); los menores de 18 años necesitan autorización de sus padres o tutores y no pueden realizar trabajos nocturnos ni horas extraordinarias.",
                    "En segundo lugar, el Estatuto establece que la duración máxima de la jornada ordinaria de trabajo es de 40 horas semanales de promedio en cómputo anual (aunque muchos convenios colectivos pactan jornadas inferiores), y que todo trabajador tiene derecho a un periodo de vacaciones anuales retribuidas no sustituible por compensación económica y que en ningún caso será inferior a 30 días naturales por año trabajado.",
                    "Por último, el Gobierno fija anualmente, previa consulta con los sindicatos y las asociaciones empresariales más representativas, el Salario Mínimo Interprofesional (SMI), que garantiza la cuantía retributiva mínima que debe percibir cualquier trabajador en España por la jornada legal de trabajo."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la edad mínima legal para poder trabajar en España según el Estatuto de los Trabajadores?",
                        "options": ["16 años", "12 años", "14 años", "21 años"],
                        "correctIndex": 0,
                        "explanation": "La edad mínima para trabajar en España es de 16 años, una vez finalizada la enseñanza básica obligatoria."
                    },
                    {
                        "question": "¿Cuál es la duración mínima legal de las vacaciones anuales pagadas en España?",
                        "options": [
                            "30 días naturales por año trabajado",
                            "7 días al año",
                            "10 días cada dos años",
                            "No existen vacaciones pagadas por ley"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Estatuto de los Trabajadores garantiza un mínimo de 30 días naturales (o 22 días laborables) de vacaciones anuales retribuidas."
                    },
                    {
                        "question": "¿Qué documento oficial de la Seguridad Social recoge de forma cronológica todos los periodos en que una persona ha trabajado y cotizado?",
                        "options": [
                            "El Informe de Vida Laboral",
                            "El Libro de Familia",
                            "El Padrón Municipal",
                            "El Certificado de Empadronamiento"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Informe de Vida Laboral acredita todos los periodos de alta y cotización en la Seguridad Social."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Quién fija cada año en España el Salario Mínimo Interprofesional (SMI)?",
                        "options": [
                            "El Gobierno, previa consulta con los sindicatos y las organizaciones empresariales",
                            "El Tribunal Constitucional",
                            "Cada ayuntamiento por separado",
                            "El Defensor del Pueblo"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 27 del Estatuto de los Trabajadores atribuye al Gobierno la fijación anual del SMI."
                    },
                    {
                        "prompt": "¿Qué organismo público gestiona las prestaciones por desempleo («el paro») en España?",
                        "options": [
                            "El SEPE (Servicio Público de Empleo Estatal)",
                            "La Dirección General de Tráfico (DGT)",
                            "El Instituto Geográfico Nacional",
                            "AENA"
                        ],
                        "correctIndex": 0,
                        "explanation": "El SEPE gestiona las prestaciones por desempleo en todo el Estado."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En España, la edad mínima legal para trabajar es de ___ años.",
                        "answer": "dieciséis",
                        "options": ["dieciséis", "doce", "catorce", "veintiún"],
                        "explanation": "El Estatuto de los Trabajadores fija en 16 años la edad mínima para trabajar.",
                        "english": "In Spain, the minimum legal age to work is sixteen years."
                    },
                    {
                        "sentence": "Las vacaciones anuales retribuidas nunca pueden ser inferiores a ___ días naturales.",
                        "answer": "treinta",
                        "options": ["treinta", "diez", "cinco", "quince"],
                        "explanation": "El periodo mínimo de vacaciones anuales es de 30 días naturales.",
                        "english": "Annual paid vacations can never be less than thirty calendar days."
                    }
                ],
                "ex_dict": {
                    "audioText": "En España la edad mínima para trabajar es de dieciséis años y las vacaciones son de treinta días naturales.",
                    "english": "In Spain the minimum age to work is sixteen years and vacations are thirty calendar days."
                },
                "ex_sb": {
                    "words": ["El", "Gobierno", "fija", "cada", "año", "el", "Salario", "Mínimo", "Interprofesional", "en", "España."],
                    "english": "The Government sets the Minimum Interprofessional Wage in Spain every year."
                }
            },
            {
                "num": "05",
                "Title": "Seguridad Vial, Medio Ambiente y Convivencia Cívica",
                "title": "Seguridad Vial, Medio Ambiente y Convivencia Cívica",
                "grammar_slug": "velocidad-maxima-permiso-por-puntos",
                "story_slug": "civismo",
                "story_title": "A 120 km/h por la autovía y cuatro colores para reciclar: el civismo cotidiano",
                "objectives": [
                    "Conocer las normas de la Dirección General de Tráfico (DGT): límite general de 120 km/h en autopistas y autovías, permiso por puntos y uso obligatorio de cinturón y casco.",
                    "Identificar el deber de conservar el medio ambiente (Art. 45 CE) y los colores de los contenedores de reciclaje (amarillo, azul, verde y marrón).",
                    "Practicar las expresiones de normativa cívica y vial."
                ],
                "vocab": [
                    {"lemma": "la Dirección General de Tráfico (DGT)", "pos": "noun", "translation": "Directorate-General for Traffic"},
                    {"lemma": "el permiso de conducir por puntos", "pos": "noun", "translation": "points-based driving licence"},
                    {"lemma": "la autopista / la autovía", "pos": "noun", "translation": "toll highway / dual carriageway"},
                    {"lemma": "la Inspección Técnica de Vehículos (ITV)", "pos": "noun", "translation": "mandatory vehicle inspection (MOT)"},
                    {"lemma": "el seguro obligatorio", "pos": "noun", "translation": "compulsory motor insurance"},
                    {"lemma": "el medio ambiente", "pos": "noun", "translation": "the environment"},
                    {"lemma": "el contenedor de reciclaje", "pos": "noun", "translation": "recycling bin"},
                    {"lemma": "la tasa de alcoholemia", "pos": "noun", "translation": "blood alcohol limit"}
                ],
                "grammar_title": "Límites y obligaciones cívicas: «estar obligado a» y «velocidad máxima permitida»",
                "grammar_text": "Para expresar normas de circulación y convivencia ciudadana, se emplean construcciones impersonales y pasivas reflejas: *La velocidad máxima permitida para turismos y motocicletas en autopistas y autovías es de **120 kilómetros por hora***; *Todo vehículo está obligado a contar con seguro en vigor y superar la **ITV***.",
                "grammar_examples": [
                    {"es": "En las autopistas y autovías españolas la velocidad máxima permitida para turismos es de 120 km/h.", "en": "On Spanish motorways and dual carriageways the maximum permitted speed for passenger cars is 120 km/h."},
                    {"es": "En el contenedor azul se depositan el papel y el cartón, y en el amarillo los envases de plástico y latas.", "en": "Paper and cardboard are placed in the blue bin, and plastic packaging and cans in the yellow one."}
                ],
                "grammar_tip": "Preguntas clásicas de la Tarea 5 del CCSE: límite de 120 km/h en autopistas y autovías, permiso por puntos de la DGT, y colores del reciclaje (azul = papel/cartón, amarillo = envases/latas, verde = vidrio).",
                "paragraphs": [
                    "La convivencia cívica en España se refleja cada día tanto en las carreteras como en el cuidado de los espacios públicos y del entorno natural. En materia de circulación, el organismo autónomo adscrito al Ministerio del Interior responsable de la seguridad vial y de expedir los permisos de conducir (a partir de los 18 años para automóviles) es la Dirección General de Tráfico (DGT).",
                    "Desde 2006, España cuenta con el permiso de conducir por puntos: los conductores comienzan de forma general con 12 puntos (8 para los conductores noveles durante sus dos primeros años) y pueden llegar hasta un máximo de 15 puntos si no cometen infracciones; por el contrario, conductas peligrosas como superar las tasas máximas de alcoholemia, usar el teléfono móvil al volante o no llevar el cinturón de seguridad o el casco restan puntos y conllevan sanciones.",
                    "Para el examen CCSE conviene recordar tres datos viales básicos: la velocidad máxima genérica para turismos y motocicletas en autopistas y autovías es de 120 km/h (90 km/h en carreteras convencionales y 30 o 50 km/h en vías urbanas según el número de carriles); todo vehículo matriculado debe tener contratado un seguro obligatorio de responsabilidad civil; y debe superar periódicamente la ITV (Inspección Técnica de Vehículos).",
                    "Por otro lado, el artículo 45 de la Constitución reconoce que todos tienen el derecho a disfrutar de un medio ambiente adecuado para el desarrollo de la persona, así como el deber de conservarlo. En todos los municipios españoles, ese deber se traduce en la recogida selectiva de residuos mediante contenedores de colores.",
                    "¿Qué se deposita en cada contenedor? En el contenedor amarillo van los envases ligeros (botellas y envases de plástico, latas metálicas y briks); en el contenedor azul, el papel y el cartón; en el iglú verde, los envases de vidrio (botellas, tarros y frascos); en el contenedor marrón, la materia orgánica; y los aparatos electrónicos, pilas o aceites usados deben llevarse a los «puntos limpios» municipales."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la velocidad máxima genérica permitida para turismos y motocicletas en las autopistas y autovías de España?",
                        "options": ["120 km/h", "150 km/h", "80 km/h", "100 km/h"],
                        "correctIndex": 0,
                        "explanation": "En España, el límite máximo general en autopistas y autovías para turismos y motocicletas es de 120 km/h."
                    },
                    {
                        "question": "¿Qué organismo del Ministerio del Interior gestiona la seguridad vial y expide el permiso de conducir en España?",
                        "options": [
                            "La Dirección General de Tráfico (DGT)",
                            "La Agencia Tributaria (AEAT)",
                            "El Instituto Nacional de Estadística (INE)",
                            "La Tesorería General de la Seguridad Social"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Dirección General de Tráfico (DGT) es el organismo encargado de la política vial y de los permisos de conducción."
                    },
                    {
                        "question": "En los municipios españoles, ¿qué residuos deben depositarse en el contenedor azul y en el contenedor amarillo?",
                        "options": [
                            "En el azul, papel y cartón; en el amarillo, envases de plástico, latas y briks",
                            "En el azul, vidrio; en el amarillo, muebles antiguos",
                            "En el azul, baterías de coche; en el amarillo, papel de periódico",
                            "Todos los residuos van juntos sin separar"
                        ],
                        "correctIndex": 0,
                        "explanation": "El contenedor azul es para papel y cartón; el amarillo, para envases de plástico, latas y briks; y el verde, para vidrio."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué inspección periódica obligatoria deben superar los automóviles en España para comprobar su buen estado técnico y de seguridad?",
                        "options": [
                            "La ITV (Inspección Técnica de Vehículos)",
                            "La prueba CCSE",
                            "El censo electoral",
                            "La declaración del IRPF"
                        ],
                        "correctIndex": 0,
                        "explanation": "La ITV (Inspección Técnica de Vehículos) verifica periódicamente que el vehículo cumple las normas de seguridad y emisiones."
                    },
                    {
                        "prompt": "¿A qué edad se puede obtener en España el permiso general de conducir automóviles (permiso B)?",
                        "options": [
                            "A los 18 años",
                            "A los 14 años",
                            "A los 15 años",
                            "A los 23 años"
                        ],
                        "correctIndex": 0,
                        "explanation": "En España la edad mínima para obtener el permiso B de conducción de turismos es de 18 años."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "En las autopistas y autovías españolas, la velocidad máxima para turismos es de ___ kilómetros por hora.",
                        "answer": "120",
                        "options": ["120", "160", "80", "50"],
                        "explanation": "El límite general en autopistas y autovías es de 120 km/h.",
                        "english": "On Spanish motorways and dual carriageways, the maximum speed for passenger cars is 120 kilometers per hour."
                    },
                    {
                        "sentence": "El artículo 45 de la Constitución establece el derecho a disfrutar de un medio ___ adecuado y el deber de conservarlo.",
                        "answer": "ambiente",
                        "options": ["ambiente", "escaño", "senado", "arancel"],
                        "explanation": "El artículo 45 CE protege el medio ambiente.",
                        "english": "Article 45 of the Constitution establishes the right to enjoy an adequate environment and the duty to preserve it."
                    }
                ],
                "ex_dict": {
                    "audioText": "La velocidad máxima permitida para turismos en autopistas y autovías es de ciento veinte kilómetros por hora.",
                    "english": "The maximum speed permitted for passenger cars on motorways and dual carriageways is one hundred and twenty kilometers per hour."
                },
                "ex_sb": {
                    "words": ["La", "Dirección", "General", "de", "Tráfico", "expide", "el", "permiso", "de", "conducir", "en", "España."],
                    "english": "The Directorate-General for Traffic issues the driving licence in Spain."
                }
            }
        ]
    }
]


def main():
    for u in UNITS_13_14_15:
        emit_unit_from_dict(u)


if __name__ == "__main__":
    main()
