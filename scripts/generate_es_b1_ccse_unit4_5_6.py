#!/usr/bin/env python3
"""Generate Spain CCSE Units 4, 5 & 6 (content/es-es, B1, track: cultura).

Unit 4: El Gobierno y la Administración del Estado (b1-gobierno)
Unit 5: El Poder Judicial y el Tribunal Constitucional (b1-judicial)
Unit 6: Las Instituciones Autonómicas y Locales (b1-autonomias)
"""

from pathlib import Path
from generate_es_b1_ccse_unit2_3 import emit_unit


def build_unit_4():
    lessons = [
        {
            "num": "01",
            "story_suffix": "composicion",
            "title": "Composición del Gobierno y la Presidencia",
            "theme": "El Gobierno y la Administración",
            "goal": "Conocer la composición del Gobierno (Presidente, Vicepresidentes y Ministros), sus funciones según el artículo 97 y su sede en la Moncloa.",
            "grammar_short": "dirigir y ejercer",
            "grammar_slug": "dirigir-y-ejercer",
            "grammar_title": "Colocaciones del poder ejecutivo: «dirigir la política» y «ejercer la potestad»",
            "location": "Madrid, Palacio de la Moncloa",
            "words": [
                {"lemma": "el poder ejecutivo", "translation": "executive power / branch", "pos": "expression"},
                {"lemma": "el Palacio de la Moncloa", "translation": "Moncloa Palace (official seat of the PM)", "pos": "expression"},
                {"lemma": "la potestad reglamentaria", "translation": "regulatory power", "pos": "expression"},
                {"lemma": "el vicepresidente", "translation": "deputy prime minister / vice-president", "pos": "noun"},
                {"lemma": "la política interior", "translation": "domestic policy", "pos": "expression"},
                {"lemma": "la política exterior", "translation": "foreign policy", "pos": "expression"},
                {"lemma": "la Administración civil", "translation": "civil administration", "pos": "expression"},
                {"lemma": "coordinar", "translation": "to coordinate", "pos": "verb"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 97 de la Constitución sintetiza el papel del Gobierno mediante dos verbos clave: *dirigir* (aplicado a la política interior y exterior, la Administración civil y militar y la defensa) y *ejercer* (aplicado a la función ejecutiva y la potestad reglamentaria)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Gobierno dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado.", "english": "The Government directs domestic and foreign policy, civil and military administration, and the defense of the State."},
                        {"spanish": "El Gobierno ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes.", "english": "The Government exercises the executive function and regulatory power in accordance with the Constitution and the laws."},
                        {"spanish": "El Presidente del Gobierno dirige la acción del Gobierno y coordina las funciones de los demás miembros.", "english": "The Prime Minister directs the action of the Government and coordinates the functions of the other members."},
                        {"spanish": "La sede de la Presidencia del Gobierno se encuentra en el complejo del Palacio de la Moncloa, en Madrid.", "english": "The seat of the Presidency of the Government is located in the Moncloa Palace complex in Madrid."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "No confundas la *potestad legislativa* (que ejercen las Cortes Generales al hacer leyes) con la *potestad reglamentaria* (que ejerce el Gobierno al dictar reglamentos y reales decretos)."
                }
            ],
            "story_summary": "Title IV (Articles 97 and 98) defines the Government as the executive branch composed of the Prime Minister (Presidente), Deputy Prime Ministers (Vicepresidentes), and Ministers, headquartered at the Moncloa Palace in Madrid.",
            "story_paragraphs": [
                "El Título IV de la Constitución Española, bajo la rúbrica «Del Gobierno y de la Administración», regula el poder ejecutivo del Estado.",
                "Su artículo 97 resume las atribuciones esenciales del Ejecutivo: el Gobierno dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado, y ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes.",
                "Según el artículo 98.1, el Gobierno se compone del Presidente, de los Vicepresidentes, en su caso, de los Ministros y de los demás miembros que establezca la ley (Siendo siempre obligatorios el Presidente y los Ministros, y opcionales los Vicepresidentes).",
                "El Presidente del Gobierno dirige la acción del Ejecutivo y coordina las funciones de sus ministros, sin perjuicio de la competencia y responsabilidad directa de estos en su gestión.",
                "La residencia oficial y sede de trabajo de la Presidencia del Gobierno, donde también se celebran las reuniones semanales del gabinete, es el Palacio de la Moncloa, situado en el noroeste de Madrid."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la residencia oficial del Presidente del Gobierno y sede de la Presidencia?",
                    "options": ["El Palacio de la Moncloa", "El Palacio de la Zarzuela", "El Palacio de las Cortes", "El Palacio de Santa Cruz"],
                    "correctIndex": 0,
                    "explanation": "El Palacio de la Moncloa en Madrid es la residencia oficial del Presidente del Gobierno y sede del Consejo de Ministros."
                },
                {
                    "question": "Según el artículo 98 de la Constitución, ¿quiénes componen el Gobierno?",
                    "options": [
                        "El Presidente, los Vicepresidentes en su caso, los Ministros y los demás miembros que establezca la ley",
                        "El Rey, los senadores y los alcaldes",
                        "Los 350 diputados y los 12 magistrados constitucionales",
                        "Los delegados provinciales y los jueces"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 98.1 establece que el Gobierno se compone del Presidente, de los Vicepresidentes en su caso y de los Ministros."
                },
                {
                    "question": "¿Qué funciones atribuye el artículo 97 al Gobierno de España?",
                    "options": [
                        "Dirigir la política interior y exterior, la Administración civil y militar y la defensa, y ejercer la función ejecutiva y la potestad reglamentaria",
                        "Dictar sentencias firmes en los tribunales penales",
                        "Reformar en solitario la Constitución Española",
                        "Elegir a los concejales de los ayuntamientos"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 97 encomienda al Gobierno la dirección política y administrativa y el ejercicio de la función ejecutiva y reglamentaria."
                }
            ],
            "goals": [
                "Describe the composition of the Government under Article 98: President, Vice-Presidents (when applicable), and Ministers.",
                "Identify the Moncloa Palace as the official seat of the Presidency of the Government.",
                "State the Government's constitutional functions under Article 97 (domestic/foreign policy, executive and regulatory power).",
                "Use 'dirigir' and 'ejercer' with their proper institutional collocations."
            ],
            "mc1": {
                "q": "¿Dónde se encuentra la residencia oficial del Presidente del Gobierno de España?",
                "opts": ["En el Palacio de la Moncloa.", "En el Palacio de la Zarzuela.", "En el Palacio del Senado."]
            },
            "mc2": {
                "q": "¿Qué órgano del Estado dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado?",
                "opts": ["El Gobierno.", "El Tribunal Constitucional.", "El Defensor del Pueblo."]
            },
            "fb": {
                "sentence": "El Gobierno ___ la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución. (ejercer)",
                "answer": "ejerce",
                "english": "The Government exercises the executive function and regulatory power in accordance with the Constitution."
            },
            "mc3": {
                "q": "¿Quién coordina las funciones de los demás miembros del Gobierno según el artículo 98.2?",
                "opts": ["El Presidente del Gobierno.", "El Presidente del Tribunal Supremo.", "El Alcalde de Madrid."]
            },
            "sb": {
                "words": ["El", "Gobierno", "dirige", "la", "política", "interior", "y", "exterior", "de", "España."],
                "english": "The Government directs the domestic and foreign policy of Spain."
            },
            "dlg": {
                "s1": "Clara", "s2": "Rubén",
                "q": "¿Es obligatorio que en todos los gobiernos exista al menos un Vicepresidente?",
                "opts": [
                    "No, la Constitución dice «los Vicepresidentes, en su caso», por lo que su existencia es potestativa del Presidente.",
                    "Sí, la Constitución exige exactamente cinco vicepresidentes siempre.",
                    "No, porque en España nunca ha existido el cargo de vicepresidente."
                ]
            },
            "listen": {
                "sentence": "El Gobierno se compone del Presidente, de los Vicepresidentes en su caso y de los Ministros, y celebra sus reuniones en el Palacio de la Moncloa.",
                "opts": [
                    "The Government is composed of the Prime Minister, Deputy Prime Ministers if applicable, and Ministers, and holds its meetings at the Moncloa Palace.",
                    "The Government is composed of the 350 deputies and meets at the Zarzuela Palace.",
                    "Regulatory power belongs exclusively to the municipal councils."
                ]
            }
        },
        {
            "num": "02",
            "story_suffix": "consejoministros",
            "title": "El Consejo de Ministros y los Reales Decretos",
            "theme": "El Gobierno y la Administración",
            "goal": "Entender el funcionamiento del Consejo de Ministros y diferenciar los reales decretos-leyes y los reales decretos legislativos.",
            "grammar_short": "en el plazo de + tiempo",
            "grammar_slug": "en-el-plazo-de",
            "grammar_title": "Límites temporales en normas de urgencia: «en el plazo de»",
            "location": "Madrid, Palacio de la Moncloa",
            "words": [
                {"lemma": "el Consejo de Ministros", "translation": "Council of Ministers (Cabinet)", "pos": "expression"},
                {"lemma": "el real decreto-ley", "translation": "royal decree-law (emergency executive norm)", "pos": "expression"},
                {"lemma": "el real decreto legislativo", "translation": "royal legislative decree (delegated by Cortes)", "pos": "expression"},
                {"lemma": "el reglamento", "translation": "regulation, statutory instrument", "pos": "noun"},
                {"lemma": "convalidar", "translation": "to validate, confirm (a decree-law in Congress)", "pos": "verb"},
                {"lemma": "derogar", "translation": "to repeal, revoke", "pos": "verb"},
                {"lemma": "la urgente necesidad", "translation": "urgent need", "pos": "expression"},
                {"lemma": "el órgano colegiado", "translation": "collegiate body", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "En derecho administrativo y constitucional, la locución *en el plazo de + expresión temporal* (*en el plazo de treinta días*) fija el tiempo máximo improrrogable dentro del cual un órgano debe convalidar, sancionar o recurrir una norma."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "Los reales decretos-leyes deben ser sometidos a debate y votación en el Congreso en el plazo de los treinta días siguientes a su promulgación.", "english": "Royal decree-laws must be submitted for debate and vote in Congress within thirty days following their promulgation."},
                        {"spanish": "El Congreso habrá de pronunciarse expresamente dentro de dicho plazo sobre su convalidación o derogación.", "english": "Congress must expressly rule within that period on their validation or repeal."},
                        {"spanish": "En caso de extraordinaria y urgente necesidad, el Gobierno puede dictar disposiciones legislativas provisionales.", "english": "In the event of extraordinary and urgent need, the Government may issue provisional legislative provisions."},
                        {"spanish": "El Consejo de Ministros se reúne habitualmente cada martes en el Palacio de la Moncloa.", "english": "The Council of Ministers usually meets every Tuesday at the Moncloa Palace."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda que un *real decreto-ley* (Art. 86) responde a una *extraordinaria y urgente necesidad* y lo convalida el Congreso en 30 días, mientras que un *real decreto legislativo* (Art. 82) nace de una delegación previa de las Cortes."
                }
            ],
            "story_summary": "How the Council of Ministers acts as a collegiate body, and when the Government can issue norms with the rank of law: Royal Legislative Decrees (by delegation of the Cortes, Article 82) and emergency Royal Decree-Laws (validated by Congress within 30 days, Article 86).",
            "story_paragraphs": [
                "El Gobierno actúa como un órgano colegiado a través del Consejo de Ministros, que reúne al Presidente, a los Vicepresidentes y a los titulares de los distintos ministerios (como Asuntos Exteriores, Justicia, Defensa, Hacienda, Interior, Educación o Sanidad).",
                "En el ejercicio ordinario de su potestad reglamentaria, el Consejo de Ministros aprueba reales decretos y reglamentos que desarrollan y aplican las leyes aprobadas por el Parlamento, situándose siempre por debajo de la ley en la jerarquía normativa.",
                "Sin embargo, los artículos 82 y 86 de la Constitución permiten al Gobierno dictar normas con rango de ley en dos supuestos muy concretos y sometidos al control parlamentario.",
                "El primero es el «real decreto legislativo» (artículo 82), mediante el cual las Cortes Generales delegan en el Gobierno la potestad de refundir varios textos legales en uno solo o desarrollar una ley de bases.",
                "El segundo es el «real decreto-ley» (artículo 86): en caso de extraordinaria y urgente necesidad, el Gobierno puede dictar disposiciones legislativas provisionales que no pueden afectar a los derechos fundamentales ni al régimen electoral, y que deben ser convalidadas o derogadas por el Congreso de los Diputados en el plazo de treinta días."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué supuesto permite el artículo 86 de la Constitución que el Gobierno dicte un Real Decreto-ley?",
                    "options": [
                        "En caso de extraordinaria y urgente necesidad",
                        "Para reformar los derechos fundamentales del Título I",
                        "Para cambiar la ley electoral general sin el Congreso",
                        "Para suprimir los Estatutos de Autonomía"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 86.1 autoriza al Gobierno a dictar reales decretos-leyes únicamente en caso de extraordinaria y urgente necesidad."
                },
                {
                    "question": "¿Qué cámara debe convalidar o derogar un Real Decreto-ley en el plazo de treinta días desde su promulgación?",
                    "options": ["El Congreso de los Diputados", "El Senado en exclusiva", "El Tribunal de Cuentas", "La Asamblea de Madrid"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 86.2, los decretos-leyes deben ser sometidos inmediatamente al Congreso de los Diputados en el plazo de treinta días."
                },
                {
                    "question": "¿Cómo se llama el órgano colegiado que reúne semanalmente al Presidente del Gobierno y a todos los ministros?",
                    "options": ["El Consejo de Ministros", "El Consejo de Estado", "La Mesa del Congreso", "La Junta Electoral"],
                    "correctIndex": 0,
                    "explanation": "El Consejo de Ministros es el órgano colegiado plenario del Gobierno de la Nación."
                }
            ],
            "goals": [
                "Identify the Council of Ministers as the collegiate body of the Government.",
                "Distinguish regulations ('reales decretos') from norms with the force of law ('reales decretos legislativos' and 'reales decretos-leyes').",
                "State that a Royal Decree-Law requires extraordinary and urgent need and must be validated by Congress within 30 days.",
                "Use 'en el plazo de' to express statutory deadlines."
            ],
            "mc1": {
                "q": "¿Cómo se denomina la norma provisional con rango de ley que puede dictar el Gobierno en caso de extraordinaria y urgente necesidad?",
                "opts": ["Real Decreto-ley.", "Ley Orgánica.", "Estatuto de Autonomía."]
            },
            "mc2": {
                "q": "¿En qué plazo máximo debe pronunciarse el Congreso de los Diputados sobre la convalidación o derogación de un Real Decreto-ley?",
                "opts": ["En el plazo de treinta días siguientes a su promulgación.", "En el plazo de cuatro años.", "En el plazo de un año natural."]
            },
            "fb": {
                "sentence": "El Real Decreto-ley debe ser convalidado por el Congreso en el ___ de treinta días. (plazo)",
                "answer": "plazo",
                "english": "The Royal Decree-Law must be validated by Congress within the period of thirty days."
            },
            "mc3": {
                "q": "¿Dónde se reúne habitualmente cada semana el Consejo de Ministros?",
                "opts": ["En el Palacio de la Moncloa.", "En el Palacio de la Zarzuela.", "En la sede del Defensor del Pueblo."]
            },
            "sb": {
                "words": ["El", "Consejo", "de", "Ministros", "aprueba", "los", "proyectos", "de", "ley."],
                "english": "The Council of Ministers approves government bills."
            },
            "dlg": {
                "s1": "Gema", "s2": "Iván",
                "q": "¿Puede el Gobierno utilizar un Real Decreto-ley de urgencia para modificar el régimen electoral general?",
                "opts": [
                    "No, el artículo 86 prohíbe que los decretos-leyes afecten a los derechos fundamentales, a las comunidades autónomas o al régimen electoral general.",
                    "Sí, el Gobierno puede cambiar la ley electoral por decreto-ley sin límite alguno.",
                    "Sí, siempre que lo firme un alcalde."
                ]
            },
            "listen": {
                "sentence": "En caso de extraordinaria y urgente necesidad, el Gobierno puede dictar reales decretos-leyes que deben ser convalidados por el Congreso en treinta días.",
                "opts": [
                    "In cases of extraordinary and urgent need, the Government may issue royal decree-laws that must be validated by Congress within thirty days.",
                    "Royal decree-laws can abolish fundamental constitutional rights permanently.",
                    "The Council of Ministers only meets once every four years."
                ]
            }
        },
        {
            "num": "03",
            "story_suffix": "administracion",
            "title": "La Administración Pública y el acceso a la función pública",
            "theme": "El Gobierno y la Administración",
            "goal": "Conocer los principios del artículo 103 (objetividad, eficacia, descentralización) y el acceso al empleo público por mérito y capacidad (oposiciones).",
            "grammar_short": "de acuerdo con / conforme a",
            "grammar_slug": "de-acuerdo-con",
            "grammar_title": "Locuciones de conformidad legal: «de acuerdo con» y «conforme a»",
            "location": "España",
            "words": [
                {"lemma": "la Administración Pública", "translation": "Public Administration", "pos": "expression"},
                {"lemma": "el interés general", "translation": "general / public interest", "pos": "expression"},
                {"lemma": "la eficacia", "translation": "effectiveness, efficiency", "pos": "noun"},
                {"lemma": "la jerarquía", "translation": "hierarchy", "pos": "noun"},
                {"lemma": "la función pública", "translation": "civil service", "pos": "expression"},
                {"lemma": "el funcionario", "translation": "civil servant, public official", "pos": "noun"},
                {"lemma": "las oposiciones", "translation": "competitive civil service examinations", "pos": "noun"},
                {"lemma": "el mérito y la capacidad", "translation": "merit and ability", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 103 de la Constitución introduce los principios de actuación administrativa mediante las locuciones *de acuerdo con* (in accordance with) y *con sometimiento pleno a la ley y al Derecho* (with full submission to the law and the legal order)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "La Administración Pública sirve con objetividad los intereses generales y actúa de acuerdo con los principios de eficacia y descentralización.", "english": "The Public Administration objectively serves the general interest and acts in accordance with the principles of effectiveness and decentralization."},
                        {"spanish": "El acceso a la función pública se regula de acuerdo con los principios constitucionales de mérito y capacidad.", "english": "Access to the civil service is regulated in accordance with the constitutional principles of merit and ability."},
                        {"spanish": "Todas las administraciones públicas actúan con sometimiento pleno a la ley y al Derecho.", "english": "All public administrations act with full submission to the law and the legal order."},
                        {"spanish": "Los funcionarios públicos son seleccionados conforme a convocatorias públicas e imparciales llamadas oposiciones.", "english": "Civil servants are selected in accordance with public, impartial examinations called 'oposiciones'."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "En el examen CCSE es muy importante el término *oposiciones*: las pruebas públicas mediante las cuales los ciudadanos acceden al empleo como funcionarios de acuerdo con los principios de igualdad, mérito y capacidad."
                }
            ],
            "story_summary": "Article 103 requires the Public Administration to serve the general interest objectively under the principles of effectiveness, hierarchy, decentralization, deconcentration, and coordination, selecting civil servants ('funcionarios') through public competitive exams ('oposiciones') based on merit and ability.",
            "story_paragraphs": [
                "Mientras que el Gobierno cambia cuando las urnas dan la mayoría parlamentaria a otro partido, la Administración Pública permanece estable para garantizar el funcionamiento diario de los servicios públicos a todos los ciudadanos.",
                "El artículo 103.1 de la Constitución ofrece una definición fundamental: «La Administración Pública sirve con objetividad los intereses generales y actúa de acuerdo con los principios de eficacia, jerarquía, descentralización, desconcentración y coordinación, con sometimiento pleno a la ley y al Derecho».",
                "¿Cómo se garantiza la imparcialidad y la profesionalidad de quienes trabajan al servicio del Estado, de las comunidades autónomas o de los ayuntamientos?",
                "El artículo 103.3 establece que la ley regulará el estatuto de los funcionarios públicos y el acceso a la función pública de acuerdo con los principios constitucionales de mérito y capacidad.",
                "En la práctica española, este mandato constitucional se materializa a través del sistema de «oposiciones»: exámenes públicos, abiertos y competitivos en los que cualquier ciudadano que cumpla los requisitos de titulación puede demostrar sus conocimientos en igualdad de condiciones para obtener una plaza en la Administración."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 103.1, ¿con qué criterio sirve la Administración Pública los intereses generales?",
                    "options": ["Con objetividad y sometimiento pleno a la ley y al Derecho", "Según los intereses privados de cada partido", "Sin sujeción a los tribunales de justicia", "Exclusivamente en beneficio de la capital"],
                    "correctIndex": 0,
                    "explanation": "El artículo 103.1 dispone que la Administración Pública sirve con objetividad los intereses generales."
                },
                {
                    "question": "¿De acuerdo con qué principios constitucionales se realiza el acceso a la función pública en España?",
                    "options": ["De acuerdo con los principios de igualdad, mérito y capacidad", "Por herencia familiar directa", "Por sorteo anual en cada municipio", "Por antigüedad en el padrón"],
                    "correctIndex": 0,
                    "explanation": "El artículo 103.3 consagra el acceso a la función pública de acuerdo con los principios de mérito y capacidad."
                },
                {
                    "question": "¿Cómo se denominan en España los exámenes públicos competitivos para acceder a una plaza de funcionario público?",
                    "options": ["Oposiciones", "Mociones", "Interpelaciones", "Refrendos"],
                    "correctIndex": 0,
                    "explanation": "Las pruebas selectivas públicas para ingresar como funcionario se denominan oposiciones."
                }
            ],
            "goals": [
                "State that the Public Administration objectively serves the general interest with full submission to the law (Article 103.1).",
                "List the five organizational principles of Article 103: effectiveness, hierarchy, decentralization, deconcentration, and coordination.",
                "Explain that access to the civil service ('función pública') is governed by merit and ability through 'oposiciones'.",
                "Use 'de acuerdo con' to reference constitutional standards."
            ],
            "mc1": {
                "q": "¿Bajo qué principios constitucionales se regula el acceso de los ciudadanos a la función pública (empleo como funcionario)?",
                "opts": ["Igualdad, mérito y capacidad.", "Herencia y designación discrecional.", "Sorteo provincial."]
            },
            "mc2": {
                "q": "¿Cómo se llaman las pruebas selectivas públicas que se convocan en España para acceder a una plaza de funcionario?",
                "opts": ["Oposiciones.", "Plebiscitos.", "Enmiendas."]
            },
            "fb": {
                "sentence": "La Administración Pública actúa de ___ con los principios de eficacia, jerarquía y descentralización. (acuerdo)",
                "answer": "acuerdo",
                "english": "The Public Administration acts in accordance with the principles of effectiveness, hierarchy, and decentralization."
            },
            "mc3": {
                "q": "Según el artículo 103.1 de la Constitución, ¿qué sirve con objetividad la Administración Pública?",
                "opts": ["Los intereses generales.", "Los intereses de un solo grupo parlamentario.", "Las empresas extranjeras exclusivamente."]
            },
            "sb": {
                "words": ["La", "Administración", "Pública", "sirve", "con", "objetividad", "los", "intereses", "generales."],
                "english": "The Public Administration objectively serves the general interest."
            },
            "dlg": {
                "s1": "Sonia", "s2": "Víctor",
                "q": "¿En qué portales oficiales pueden consultar los ciudadanos las convocatorias de oposiciones y realizar trámites con la Administración?",
                "opts": [
                    "En el Boletín Oficial del Estado (BOE) y en el Punto de Acceso General electrónico (administracion.gob.es).",
                    "Únicamente acudiendo en persona al Tribunal Constitucional.",
                    "Las convocatorias de empleo público no se publican en ningún boletín."
                ]
            },
            "listen": {
                "sentence": "El acceso a la función pública se realiza mediante oposiciones de acuerdo con los principios constitucionales de mérito y capacidad.",
                "opts": [
                    "Access to the civil service takes place through competitive exams in accordance with the constitutional principles of merit and ability.",
                    "Civil servants are dismissed every time a new mayor is elected.",
                    "Public Administration is exempt from obeying the law."
                ]
            }
        },
        {
            "num": "04",
            "story_suffix": "delegados",
            "title": "Delegados del Gobierno, subdelegados y el Consejo de Estado",
            "theme": "El Gobierno y la Administración",
            "goal": "Identificar la figura del Delegado del Gobierno en las comunidades autónomas (artículo 154) y el Consejo de Estado (artículo 107).",
            "grammar_short": "cuyo / cuya en definiciones",
            "grammar_slug": "cuya-funcion-es",
            "grammar_title": "Relativos posesivos en definiciones institucionales: «cuyo / cuya»",
            "location": "España",
            "words": [
                {"lemma": "el Delegado del Gobierno", "translation": "Government Delegate (in an Autonomous Community)", "pos": "expression"},
                {"lemma": "el subdelegado del Gobierno", "translation": "Government Sub-delegate (in a province)", "pos": "expression"},
                {"lemma": "el Consejo de Estado", "translation": "Council of State (supreme advisory body)", "pos": "expression"},
                {"lemma": "el órgano consultivo", "translation": "advisory / consultative body", "pos": "expression"},
                {"lemma": "el dictamen", "translation": "legal opinion, advisory report", "pos": "noun"},
                {"lemma": "la Administración periférica", "translation": "peripheral state administration", "pos": "expression"},
                {"lemma": "el servicio público", "translation": "public service", "pos": "expression"},
                {"lemma": "cooperar", "translation": "to cooperate", "pos": "verb"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El pronombre relativo posesivo *cuyo, cuya, cuyos, cuyas* (whose) es característico del estilo formal y jurídico para definir la misión o el ámbito de un órgano (*una institución cuya función es...*). Concuerda siempre en género y número con el sustantivo que va detrás, no con el antecedente."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Delegado del Gobierno es un alto cargo cuya misión es dirigir la Administración del Estado en la comunidad autónoma.", "english": "The Government Delegate is a senior official whose mission is to direct the State Administration in the autonomous community."},
                        {"spanish": "El Consejo de Estado es el supremo órgano consultivo cuyos dictámenes orientan la legalidad de la acción del Gobierno.", "english": "The Council of State is the supreme advisory body whose opinions guide the legality of the Government's action."},
                        {"spanish": "En cada provincia existe un subdelegado del Gobierno, cuyas funciones dependen del Delegado del Gobierno.", "english": "In each province there is a Government Sub-delegate, whose functions depend on the Government Delegate."},
                        {"spanish": "La Administración General del Estado cuenta con servicios periféricos cuya finalidad es acercar la gestión al ciudadano.", "english": "The General State Administration has peripheral services whose purpose is to bring management closer to the citizen."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Fíjate siempre en la palabra que sigue a *cuyo*: *cuya misión* (femenino singular), *cuyos dictámenes* (masculino plural)."
                }
            ],
            "story_summary": "How the General State Administration operates across the territory through Government Delegates in each Autonomous Community (Article 154) and Sub-delegates in the provinces, and how the Council of State acts as the Government's supreme advisory body (Article 107).",
            "story_paragraphs": [
                "La Administración General del Estado no actúa únicamente desde los ministerios situados en Madrid, sino que está presente en todo el territorio nacional a través de la llamada Administración periférica.",
                "El artículo 154 de la Constitución crea una figura clave: «Un Delegado nombrado por el Gobierno dirigirá la Administración del Estado en el territorio de la Comunidad Autónoma y la coordinará, cuando proceda, con la administración propia de la Comunidad».",
                "Por tanto, en cada una de las diecisiete comunidades autónomas (y en Ceuta y Melilla) existe un Delegado del Gobierno nombrado por Real Decreto del Consejo de Ministros a propuesta del Presidente del Gobierno, mientras que en cada provincia de las comunidades pluriprovinciales actúa bajo su dependencia un Subdelegado del Gobierno.",
                "De este modo, los servicios estatales en el territorio —como la expedición del DNI y del pasaporte, las oficinas de extranjería o el mando de las Fuerzas y Cuerpos de Seguridad del Estado— se gestionan de forma cercana y coordinada con las autoridades autonómicas.",
                "Por otro lado, cuando el Gobierno necesita un dictamen jurídico de máxima autoridad antes de aprobar un reglamento o un proyecto de ley, acude al Consejo de Estado, definido en el artículo 107 de la Constitución como «el supremo órgano consultivo del Gobierno»."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 154 de la Constitución, ¿quién dirige la Administración del Estado en el territorio de una comunidad autónoma y la coordina con la administración autonómica?",
                    "options": [
                        "El Delegado del Gobierno nombrado por el Gobierno",
                        "El Presidente del Tribunal Superior de Justicia",
                        "El Alcalde de la capital autonómica",
                        "El Defensor del Pueblo"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 154 dispone que un Delegado nombrado por el Gobierno dirigirá la Administración del Estado en la Comunidad Autónoma y la coordinará con la administración propia de esta."
                },
                {
                    "question": "¿Cuál es el supremo órgano consultivo del Gobierno según el artículo 107 de la Constitución?",
                    "options": ["El Consejo de Estado", "El Tribunal de Cuentas", "El Consejo General del Poder Judicial", "El Senado"],
                    "correctIndex": 0,
                    "explanation": "El artículo 107 establece textualmente: «El Consejo de Estado es el supremo órgano consultivo del Gobierno»."
                },
                {
                    "question": "¿Quién representa a la Administración General del Estado en cada una de las provincias de una comunidad pluriprovincial?",
                    "options": ["El Subdelegado del Gobierno (bajo la dirección del Delegado del Gobierno)", "El Juez Decano", "El Notario Mayor", "El Presidente del Senado"],
                    "correctIndex": 0,
                    "explanation": "En cada provincia existe un Subdelegado del Gobierno dependiente del Delegado del Gobierno en la comunidad autónoma."
                }
            ],
            "goals": [
                "Explain the role of the Government Delegate ('Delegado del Gobierno') in each Autonomous Community under Article 154.",
                "Identify the Government Sub-delegate ('Subdelegado del Gobierno') at the provincial level.",
                "Define the Council of State ('Consejo de Estado') as the supreme advisory body of the Government (Article 107).",
                "Use 'cuyo / cuya / cuyos / cuyas' accurately in institutional definitions."
            ],
            "mc1": {
                "q": "Según el artículo 107 de la Constitución, ¿cuál es el supremo órgano consultivo del Gobierno?",
                "opts": ["El Consejo de Estado.", "El Tribunal de Cuentas.", "El Congreso de los Diputados."]
            },
            "mc2": {
                "q": "¿Qué autoridad nombrada por el Gobierno dirige la Administración del Estado en el territorio de cada comunidad autónoma?",
                "opts": ["El Delegado del Gobierno.", "El Fiscal Superior.", "El Alcalde pedáneo."]
            },
            "fb": {
                "sentence": "El Consejo de Estado es el supremo órgano consultivo ___ misión es asesorar jurídicamente al Gobierno. (cuyo, femenino singular)",
                "answer": "cuya",
                "english": "The Council of State is the supreme advisory body whose mission is to advise the Government on legal matters."
            },
            "mc3": {
                "q": "¿Con qué administración debe coordinarse el Delegado del Gobierno según el artículo 154 de la Constitución?",
                "opts": [
                    "Con la administración propia de la comunidad autónoma.",
                    "Exclusivamente con los tribunales internacionales.",
                    "Con los parlamentos de otros países europeos."
                ]
            },
            "sb": {
                "words": ["El", "Consejo", "de", "Estado", "es", "el", "supremo", "órgano", "consultivo", "del", "Gobierno."],
                "english": "The Council of State is the supreme advisory body of the Government."
            },
            "dlg": {
                "s1": "Berta", "s2": "Luis",
                "q": "¿Es lo mismo el Presidente de una Comunidad Autónoma que el Delegado del Gobierno en esa Comunidad?",
                "opts": [
                    "No: el Presidente autonómico dirige el gobierno de la Comunidad Autónoma, mientras que el Delegado del Gobierno representa y dirige la Administración del Estado en ese territorio.",
                    "Sí, son exactamente el mismo cargo con dos nombres distintos.",
                    "El Delegado del Gobierno preside el Parlamento autonómico."
                ]
            },
            "listen": {
                "sentence": "Un Delegado nombrado por el Gobierno dirige la Administración del Estado en el territorio de la comunidad autónoma.",
                "opts": [
                    "A Delegate appointed by the Government directs the State Administration in the territory of the autonomous community.",
                    "The Council of State is the supreme auditing body of the Cortes Generales.",
                    "Each municipality appoints its own ambassador."
                ]
            }
        },
        {
            "num": "05",
            "story_suffix": "responsabilidad",
            "title": "Responsabilidad solidaria y el Gobierno en funciones",
            "theme": "El Gobierno y la Administración",
            "goal": "Comprender la responsabilidad solidaria del Gobierno ante el Congreso (artículo 108) y los supuestos de cese y Gobierno en funciones (artículo 101).",
            "grammar_short": "hasta que + subjuntivo",
            "grammar_slug": "hasta-que-subjuntivo",
            "grammar_title": "Límite temporal futuro: «hasta que + presente de subjuntivo»",
            "location": "Madrid",
            "words": [
                {"lemma": "responder solidariamente", "translation": "to be jointly and collectively accountable", "pos": "expression"},
                {"lemma": "el cese", "translation": "cessation of office, dismissal", "pos": "noun"},
                {"lemma": "la dimisión", "translation": "resignation", "pos": "noun"},
                {"lemma": "el Gobierno en funciones", "translation": "caretaker / acting Government", "pos": "expression"},
                {"lemma": "la toma de posesión", "translation": "swearing-in, taking of office", "pos": "expression"},
                {"lemma": "el despacho ordinario", "translation": "ordinary day-to-day administration", "pos": "expression"},
                {"lemma": "el estado de alarma", "translation": "state of alarm", "pos": "expression"},
                {"lemma": "la gestión política", "translation": "political management", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "Cuando una norma establece hasta qué momento futuro se prolonga una situación provisional —como el Gobierno en funciones—, el conector temporal *hasta que* va seguido de presente de subjuntivo (*hasta que tome posesión el nuevo Gobierno*)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Gobierno cesante continúa en funciones hasta que tome posesión el nuevo Gobierno.", "english": "The outgoing Government continues in a caretaker capacity until the new Government takes office."},
                        {"spanish": "El Ejecutivo en funciones limita su gestión al despacho ordinario de los asuntos públicos hasta que el Congreso invista a un nuevo Presidente.", "english": "The caretaker Executive limits its management to the ordinary dispatch of public affairs until Congress invests a new President."},
                        {"spanish": "El Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados.", "english": "The Government is collectively accountable in its political management before the Congress of Deputies."},
                        {"spanish": "El estado de alarma es declarado por el Gobierno por un plazo máximo de quince días y no puede prorrogarse sin autorización del Congreso.", "english": "A state of alarm is declared by the Government for a maximum period of fifteen days and cannot be extended without the authorization of Congress."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda: *hasta que + indicativo* describe hechos pasados o habituales; *hasta que + subjuntivo* señala una condición o evento futuro que pondrá fin a la situación provisional."
                }
            ],
            "story_summary": "Article 108 establishes that the Government is collectively accountable to the Congress of Deputies, while Article 101 regulates when a Government ceases (elections, loss of confidence, resignation or death of the PM) and remains as an acting caretaker government ('Gobierno en funciones') until the new Cabinet takes office.",
            "story_paragraphs": [
                "En la monarquía parlamentaria española, la supervivencia política del Gobierno depende en todo momento de la confianza de la Cámara Baja.",
                "Así lo proclama de forma rotunda el artículo 108 de la Constitución: «El Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados». Que la responsabilidad sea «solidaria» significa que las decisiones del Consejo de Ministros comprometen políticamente a todo el gabinete en su conjunto.",
                "¿Cuándo cesa el Gobierno según el artículo 101.1? Existen cuatro causas constitucionales tasadas: tras la celebración de elecciones generales, en los casos de pérdida de la confianza parlamentaria previstos en la Constitución (si pierde una cuestión de confianza o triunfa una moción de censura), o por dimisión o fallecimiento de su Presidente.",
                "Para evitar que el país quede sin dirección administrativa ni un solo día, el artículo 101.2 dispone que el Gobierno cesante continuará «en funciones» hasta la toma de posesión del nuevo Gobierno.",
                "Durante el período en que está en funciones, el Gobierno debe limitarse al despacho ordinario de los asuntos públicos y facilitar el traspaso de poderes, sin poder presentar proyectos de ley ni aprobar el proyecto de Presupuestos Generales del Estado."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 108 de la Constitución, ¿ante qué institución responde solidariamente el Gobierno en su gestión política?",
                    "options": ["Ante el Congreso de los Diputados", "Ante el Tribunal Supremo", "Ante el Consejo de Estado", "Ante las Diputaciones Provinciales"],
                    "correctIndex": 0,
                    "explanation": "El artículo 108 dispone que el Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados."
                },
                {
                    "question": "¿Qué ocurre con el Gobierno tras la celebración de unas elecciones generales según el artículo 101?",
                    "options": [
                        "Cesa y continúa en funciones hasta la toma de posesión del nuevo Gobierno",
                        "Deja abandonados los ministerios el mismo día de la votación",
                        "Pasa a estar dirigido por los jueces del Tribunal Constitucional",
                        "Prorroga su mandato automáticamente otros cuatro años sin investidura"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 101 establece que el Gobierno cesa tras las elecciones generales, pero continúa en funciones hasta la toma de posesión del nuevo Gobierno."
                },
                {
                    "question": "¿Cuál de las siguientes causas provoca el cese de todo el Gobierno?",
                    "options": [
                        "La dimisión o el fallecimiento del Presidente del Gobierno, la pérdida de la confianza parlamentaria o la celebración de elecciones generales",
                        "El relevo de un concejal municipal",
                        "La jubilación de un embajador",
                        "Un dictamen consultivo del Consejo de Estado"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 101.1 enumera como causas de cese las elecciones generales, la pérdida de confianza parlamentaria y la dimisión o fallecimiento del Presidente."
                }
            ],
            "goals": [
                "State that the Government is collectively ('solidariamente') accountable for its political management before the Congress of Deputies (Article 108).",
                "List the causes of cessation of the Government under Article 101.1 (general elections, loss of parliamentary confidence, resignation or death of the PM).",
                "Explain the role and limits of a caretaker government ('Gobierno en funciones') until the new Government takes office.",
                "Use 'hasta que + subjunctive' to indicate the future endpoint of a provisional status."
            ],
            "mc1": {
                "q": "¿Ante qué cámara responde solidariamente el Gobierno en su gestión política según el artículo 108?",
                "opts": ["Ante el Congreso de los Diputados.", "Ante el Tribunal de Cuentas.", "Ante la Asamblea municipal."]
            },
            "mc2": {
                "q": "¿En qué situación queda el Gobierno desde el día de las elecciones generales hasta que toma posesión el nuevo Ejecutivo?",
                "opts": ["Continúa como Gobierno en funciones.", "Se disuelve sin que nadie gestione los ministerios.", "Se integra en el Poder Judicial."]
            },
            "fb": {
                "sentence": "El Gobierno cesante continuará en funciones hasta que ___ posesión el nuevo Gobierno. (tomar, presente de subjuntivo)",
                "answer": "tome",
                "english": "The outgoing Government shall continue in office until the new Government takes office."
            },
            "mc3": {
                "q": "¿Qué órgano declara mediante decreto el estado de alarma por un plazo máximo inicial de quince días según el artículo 116?",
                "opts": [
                    "El Gobierno (dando cuenta al Congreso de los Diputados, sin cuya autorización no puede prorrogarse).",
                    "Los alcaldes de cada municipio sin dar cuenta al Congreso.",
                    "El Defensor del Pueblo."
                ]
            },
            "sb": {
                "words": ["El", "Gobierno", "responde", "solidariamente", "ante", "el", "Congreso", "de", "los", "Diputados."],
                "english": "The Government is collectively accountable before the Congress of Deputies."
            },
            "dlg": {
                "s1": "Alicia", "s2": "Fernando",
                "q": "¿Puede un Gobierno que está en funciones aprobar el proyecto de Ley de Presupuestos Generales del Estado?",
                "opts": [
                    "No, el Gobierno en funciones se limita al despacho ordinario y no puede presentar el proyecto de Presupuestos ni proyectos de ley.",
                    "Sí, tiene exactamente las mismas facultades legislativas que un Gobierno con plenas funciones.",
                    "Sí, puede incluso reformar la Constitución por decreto."
                ]
            },
            "listen": {
                "sentence": "El Gobierno cesa tras la celebración de elecciones generales, pero continúa en funciones hasta la toma de posesión del nuevo Gobierno.",
                "opts": [
                    "The Government ceases after general elections are held, but continues in a caretaker capacity until the new Government takes office.",
                    "The Government is accountable only to the Constitutional Court.",
                    "The resignation of the Prime Minister does not affect the rest of the Government."
                ]
            }
        }
    ]

    comb = {
        "title": "El Gobierno y la Administración del Estado",
        "summary": "Complete CCSE overview of Title IV of the Constitution: composition of the Government (PM, Vice-Presidents, Ministers) at the Moncloa Palace, the Council of Ministers and emergency Decree-Laws, Article 103 and civil service access ('oposiciones'), Government Delegates and the Council of State, and collective accountability before Congress.",
        "paragraphs": [
            "El Gobierno (Título IV de la Constitución) dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado, y ejerce la función ejecutiva y la potestad reglamentaria; se compone del Presidente, de los Vicepresidentes en su caso y de los Ministros, con sede en el Palacio de la Moncloa.",
            "Reunido en el Consejo de Ministros, el Ejecutivo aprueba reglamentos y proyectos de ley, y puede dictar normas con rango de ley por delegación parlamentaria (reales decretos legislativos) o por extraordinaria y urgente necesidad (reales decretos-leyes, convalidados por el Congreso en 30 días).",
            "La Administración Pública sirve con objetividad los intereses generales bajo los principios de eficacia, jerarquía, descentralización, desconcentración y coordinación, seleccionando a los funcionarios mediante oposiciones basadas en el mérito y la capacidad.",
            "En cada comunidad autónoma un Delegado del Gobierno dirige la Administración del Estado y la coordina con la autonómica (con subdelegados en las provincias), mientras que el Consejo de Estado actúa como supremo órgano consultivo del Gobierno.",
            "El Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados y, tras cesar por elecciones, pérdida de confianza o dimisión del Presidente, continúa en funciones hasta la toma de posesión del nuevo Gobierno."
        ],
        "comp_questions": [
            {
                "question": "¿Cuál es la sede de la Presidencia del Gobierno y quiénes componen el Ejecutivo?",
                "options": [
                    "La sede es el Palacio de la Moncloa y lo componen el Presidente, los Vicepresidentes en su caso y los Ministros",
                    "La sede es el Palacio de la Zarzuela y lo componen los senadores",
                    "La sede es el Congreso y lo componen 350 jueces",
                    "La sede es el Consejo de Estado y lo componen los alcaldes"
                ],
                "correctIndex": 0,
                "explanation": "El Gobierno tiene su sede presidencial en el Palacio de la Moncloa y está integrado por el Presidente, Vicepresidentes (en su caso) y Ministros."
            },
            {
                "question": "¿Cómo se accede al empleo como funcionario público en la Administración española?",
                "options": [
                    "Mediante pruebas públicas selectivas (oposiciones) basadas en los principios de igualdad, mérito y capacidad",
                    "Por nombramiento directo sin examen",
                    "Por sorteo entre los residentes de Madrid",
                    "Solo por recomendación parlamentaria"
                ],
                "correctIndex": 0,
                "explanation": "El artículo 103.3 garantiza el acceso a la función pública de acuerdo con los principios de mérito y capacidad."
            },
            {
                "question": "¿Cuál es el supremo órgano consultivo del Gobierno y quién dirige la Administración del Estado en cada comunidad autónoma?",
                "options": [
                    "El Consejo de Estado es el supremo órgano consultivo, y el Delegado del Gobierno dirige la Administración estatal en la comunidad autónoma",
                    "El Defensor del Pueblo es el órgano consultivo y el alcalde dirige la comunidad",
                    "El Tribunal de Cuentas es el órgano consultivo",
                    "El Senado dirige la Administración periférica"
                ],
                "correctIndex": 0,
                "explanation": "El artículo 107 regula el Consejo de Estado y el artículo 154 la figura del Delegado del Gobierno."
            }
        ]
    }

    cons_stem = "b1-gobierno-consolidation"
    consolidation = {
        "title": "Repaso y Simulacro: El Gobierno y la Administración",
        "goal": "Consolidar la composición y funciones del Gobierno, los decretos-leyes, el artículo 103, los Delegados del Gobierno y el Consejo de Estado para el examen CCSE.",
        "grammar": "Consolidación de estructuras ejecutivas y administrativas",
        "goals": [
            "Consolidate CCSE exam facts on the Government's composition, the Moncloa Palace, and Article 97.",
            "Review Royal Decree-Laws (30-day validation in Congress) and civil service examinations ('oposiciones').",
            "Verify mastery of Government Delegates (Article 154), the Council of State (Article 107), and caretaker governments ('en funciones').",
            "Practice 'dirigir / ejercer', 'en el plazo de', 'de acuerdo con', 'cuyo / cuya', and 'hasta que + subjunctive'."
        ],
        "exercises": [
            {
                "id": f"{cons_stem}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el Palacio de la Moncloa", "Moncloa Palace (seat of the Prime Minister)"],
                    ["la potestad reglamentaria", "regulatory power"],
                    ["el real decreto-ley", "emergency royal decree-law"],
                    ["las oposiciones", "competitive civil service exams"],
                    ["el mérito y la capacidad", "merit and ability"],
                    ["el Delegado del Gobierno", "Government Delegate in an Autonomous Community"],
                    ["el Consejo de Estado", "Council of State (supreme advisory body)"],
                    ["el Gobierno en funciones", "caretaker / acting Government"]
                ],
                "teaches": ["dirigir-y-ejercer"]
            },
            {
                "id": f"{cons_stem}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración resume con exactitud el artículo 97 de la Constitución?",
                "options": [
                    "El Gobierno dirige la política interior y exterior y ejerce la función ejecutiva y la potestad reglamentaria.",
                    "El Gobierno ejerce la potestad judicial y dirige el Tribunal Constitucional.",
                    "El Gobierno sanciona las leyes en el Palacio de la Zarzuela."
                ],
                "correct": 0,
                "teaches": ["dirigir-y-ejercer"]
            },
            {
                "id": f"{cons_stem}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué locución expresa el límite de treinta días para que el Congreso convalide un Real Decreto-ley?",
                "options": [
                    "Debe ser sometido a debate y votación en el Congreso en el plazo de treinta días.",
                    "Debe ser sometido al Congreso sin el plazo por treinta días.",
                    "Debe ser sometido al Congreso hacia el plazo con treinta días."
                ],
                "correct": 0,
                "teaches": ["en-el-plazo-de"]
            },
            {
                "id": f"{cons_stem}.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración utiliza correctamente el relativo posesivo «cuyo / cuya»?",
                "options": [
                    "El Consejo de Estado es el supremo órgano consultivo cuya función es emitir dictámenes jurídicos.",
                    "El Consejo de Estado es el supremo órgano consultivo que su función es emitir dictámenes.",
                    "El Consejo de Estado es el supremo órgano consultivo cuyo función es emitir dictámenes."
                ],
                "correct": 0,
                "teaches": ["cuya-funcion-es"]
            },
            {
                "id": f"{cons_stem}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué forma verbal exige «hasta que» cuando se refiere a la futura toma de posesión del nuevo Gobierno?",
                "options": [
                    "El Gobierno cesante continuará en funciones hasta que tome posesión el nuevo Gobierno.",
                    "El Gobierno cesante continuará en funciones hasta que tomó posesión el nuevo Gobierno.",
                    "El Gobierno cesante continuará en funciones hasta que tomando posesión el nuevo Gobierno."
                ],
                "correct": 0,
                "teaches": ["hasta-que-subjuntivo"]
            },
            {
                "id": f"{cons_stem}.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El acceso a la función pública se regula de ___ con los principios de mérito y capacidad. (acuerdo)",
                "answer": "acuerdo",
                "teaches": ["de-acuerdo-con"],
                "english": "Access to the civil service is regulated in accordance with the principles of merit and ability."
            },
            {
                "id": f"{cons_stem}.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En cada comunidad autónoma existe un Delegado del Gobierno ___ misión es dirigir la Administración del Estado. (cuyo, femenino singular)",
                "answer": "cuya",
                "teaches": ["cuya-funcion-es"],
                "english": "In each autonomous community there is a Government Delegate whose mission is to direct the State Administration."
            },
            {
                "id": f"{cons_stem}.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Ejecutivo en funciones continuará en su puesto hasta que ___ posesión el nuevo gabinete. (tomar, presente de subjuntivo)",
                "answer": "tome",
                "teaches": ["hasta-que-subjuntivo"],
                "english": "The caretaker Executive will remain in office until the new cabinet takes office."
            },
            {
                "id": f"{cons_stem}.ex09",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "Administración", "Pública", "sirve", "con", "objetividad", "los", "intereses", "generales."],
                "solution": ["La", "Administración", "Pública", "sirve", "con", "objetividad", "los", "intereses", "generales."],
                "english": "The Public Administration objectively serves the general interest.",
                "teaches": ["de-acuerdo-con"]
            },
            {
                "id": f"{cons_stem}.ex10",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Se celebran elecciones generales y el Gobierno saliente cesa en su mandato. [General elections are held and the outgoing Government ceases its term.]",
                    "Mientras se tramita la nueva investidura, el Gobierno permanece en funciones para el despacho ordinario. [While the new investiture is processed, the Government remains in a caretaker capacity for ordinary business.]",
                    "Finalmente, el nuevo Presidente es investido por el Congreso y el nuevo Gobierno toma posesión. [Finally, the new President is invested by Congress and the new Government takes office.]"
                ],
                "solution": [0, 1, 2],
                "teaches": ["hasta-que-subjuntivo"]
            },
            {
                "id": f"{cons_stem}.ex11",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Qué órgano asesora jurídicamente al Gobierno como supremo órgano consultivo?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "El Consejo de Estado, regulado en el artículo 107 de la Constitución.",
                    "El Tribunal de Cuentas.",
                    "La Junta Electoral Provincial."
                ],
                "correct": 0,
                "teaches": ["cuya-funcion-es"]
            },
            {
                "id": f"{cons_stem}.ex12",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "El Gobierno dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado.",
                "options": [
                    "The Government directs domestic and foreign policy, civil and military administration, and the defense of the State.",
                    "The Government is composed of judges elected by the provinces.",
                    "The seat of the Government is the Royal Palace of Madrid."
                ],
                "correct": 0,
                "teaches": ["dirigir-y-ejercer"]
            },
            {
                "id": f"{cons_stem}.ex13",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "El Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados.",
                "options": [
                    "The Government is collectively accountable in its political management before the Congress of Deputies.",
                    "Each minister is accountable only to the Mayor of Madrid.",
                    "The Senate can dismiss a caretaker government without elections."
                ],
                "correct": 0,
                "teaches": ["hasta-que-subjuntivo"]
            },
            {
                "id": f"{cons_stem}.ex14",
                "type": "dictation",
                "category": "listening",
                "sentence": "El Consejo de Estado es el supremo órgano consultivo del Gobierno.",
                "teaches": ["cuya-funcion-es"],
                "english": "The Council of State is the supreme advisory body of the Government."
            },
            {
                "id": f"{cons_stem}.ex15",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Indica quiénes componen el Gobierno de España y cuál es la sede de la Presidencia. [State who composes the Government of Spain and what the seat of the Presidency is.]",
                        "answer": "El Gobierno se compone del Presidente, de los Vicepresidentes en su caso y de los Ministros, y la sede de la Presidencia es el Palacio de la Moncloa."
                    }
                ],
                "teaches": ["dirigir-y-ejercer"]
            },
            {
                "id": f"{cons_stem}.ex16",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica cómo sirve la Administración Pública a los ciudadanos y cómo se selecciona a los funcionarios. [Explain how the Public Administration serves citizens and how civil servants are selected.]",
                        "answer": "La Administración Pública sirve con objetividad los intereses generales y selecciona a los funcionarios mediante oposiciones basadas en los principios de mérito y capacidad."
                    }
                ],
                "teaches": ["de-acuerdo-con"]
            },
            {
                "id": f"{cons_stem}.ex17",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Resume la función del Delegado del Gobierno en cada comunidad autónoma. [Summarise the role of the Government Delegate in each autonomous community.]",
                        "answer": "El Delegado del Gobierno dirige la Administración del Estado en el territorio de la comunidad autónoma y la coordina con la administración propia de la comunidad."
                    }
                ],
                "teaches": ["cuya-funcion-es"]
            },
            {
                "id": f"{cons_stem}.ex18",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Cuándo entra en funciones el Gobierno y hasta cuándo permanece así?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "Tras su cese (por ejemplo, tras las elecciones generales), y continúa en funciones hasta la toma de posesión del nuevo Gobierno.",
                    "Solo durante los meses de verano de cada año.",
                    "Durante toda la legislatura de cuatro años."
                ],
                "correct": 0,
                "teaches": ["hasta-que-subjuntivo"]
            }
        ]
    }

    emit_unit("gobierno", "b1-ccse-gobierno", "El Gobierno", 4, lessons, comb, consolidation)


def build_unit_5():
    lessons = [
        {
            "num": "01",
            "story_suffix": "independencia",
            "title": "Principios del Poder Judicial: independencia e imperio de la ley",
            "theme": "El Poder Judicial",
            "goal": "Comprender el artículo 117 de la Constitución: origen popular de la justicia, independencia judicial y justicia gratuita.",
            "grammar_short": "sometido únicamente a",
            "grammar_slug": "sometido-unicamente-a",
            "grammar_title": "Exclusividad y sumisión a la ley: «sometido únicamente a»",
            "location": "España",
            "words": [
                {"lemma": "el Poder Judicial", "translation": "Judicial Power / Judiciary", "pos": "expression"},
                {"lemma": "el juez", "translation": "judge", "pos": "noun"},
                {"lemma": "el magistrado", "translation": "magistrate, senior judge", "pos": "noun"},
                {"lemma": "el imperio de la ley", "translation": "rule / supremacy of law", "pos": "expression"},
                {"lemma": "inamovible", "translation": "irremovable (guaranteed tenure)", "pos": "adjective"},
                {"lemma": "juzgar", "translation": "to judge, adjudicate", "pos": "verb"},
                {"lemma": "la justicia gratuita", "translation": "free legal aid", "pos": "expression"},
                {"lemma": "la sentencia", "translation": "court judgment, ruling", "pos": "noun"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 117.1 de la Constitución define la independencia de los jueces mediante una serie de adjetivos y un participio clave: *independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley* (subject solely to the rule of law)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "La justicia emana del pueblo y se administra en nombre del Rey por jueces y magistrados sometidos únicamente al imperio de la ley.", "english": "Justice emanates from the people and is administered in the name of the King by judges and magistrates subject solely to the rule of law."},
                        {"spanish": "El ejercicio de la potestad jurisdiccional, juzgando y haciendo ejecutar lo juzgado, corresponde exclusivamente a los juzgados y tribunales.", "english": "The exercise of jurisdictional power, judging and enforcing judgments, belongs exclusively to the courts and tribunals."},
                        {"spanish": "La justicia será gratuita cuando así lo disponga la ley y para quienes acrediten insuficiencia de recursos para litigar.", "english": "Justice shall be free when so provided by law and for those who prove insufficient means to litigate."},
                        {"spanish": "Los jueces y magistrados no podrán ser separados ni trasladados sino por alguna de las causas previstas en la ley.", "english": "Judges and magistrates may not be dismissed or transferred except for one of the causes provided for by law."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Los adverbios en *-mente* como *únicamente* y *exclusivamente* son esenciales en las respuestas del examen CCSE sobre el Poder Judicial."
                }
            ],
            "story_summary": "Title VI (Articles 117-127) regulates the Judiciary: justice emanates from the people and is administered in the name of the King by independent, irremovable judges subject solely to the rule of law, with free legal aid guaranteed for citizens lacking resources.",
            "story_paragraphs": [
                "El tercer pilar de la separación de poderes en un Estado democrático de Derecho es el Poder Judicial, regulado en el Título VI de la Constitución Española (artículos 117 a 127).",
                "El artículo 117.1 contiene una declaración fundamental que conecta directamente con la soberanía popular: «La justicia emana del pueblo y se administra en nombre del Rey por Jueces y Magistrados integrantes del poder judicial, independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley».",
                "¿Qué significa que los jueces sean «inamovibles»? Significa que ningún gobierno puede destituirlos, suspenderlos ni trasladarlos por motivos políticos, garantizando así que sus resoluciones dependan exclusivamente de lo que dictan las leyes.",
                "A los juzgados y tribunales les corresponde en exclusiva la potestad jurisdiccional en todo tipo de procesos, que se resume en la célebre fórmula constitucional: «juzgando y haciendo ejecutar lo juzgado».",
                "Además, para que nadie quede indefenso por motivos económicos, el artículo 119 de la Constitución garantiza que la justicia será gratuita en todo caso respecto de quienes acrediten insuficiencia de recursos para litigar (a través del turno de oficio)."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 117.1 de la Constitución, ¿de quién emana la justicia y en nombre de quién se administra?",
                    "options": [
                        "Emana del pueblo y se administra en nombre del Rey por jueces y magistrados",
                        "Emana del Gobierno y se administra en nombre del Senado",
                        "Emana de los ayuntamientos y se administra en nombre de los alcaldes",
                        "Emana del Consejo de Estado"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 117.1 establece que la justicia emana del pueblo y se administra en nombre del Rey por jueces y magistrados."
                },
                {
                    "question": "¿A qué están sometidos únicamente los jueces y magistrados en el ejercicio de su función?",
                    "options": ["Únicamente al imperio de la ley", "A las órdenes diarias de los ministros", "A las instrucciones de los partidos políticos", "A las decisiones de los concejales"],
                    "correctIndex": 0,
                    "explanation": "Los jueces son independientes y están sometidos únicamente al imperio de la ley."
                },
                {
                    "question": "¿Qué garantiza el artículo 119 de la Constitución a las personas que acrediten insuficiencia de recursos económicos para litigar?",
                    "options": ["La justicia gratuita (asistencia jurídica gratuita)", "La exención de cumplir las leyes", "Un escaño en el Parlamento", "El indulto automático"],
                    "correctIndex": 0,
                    "explanation": "El artículo 119 garantiza la gratuidad de la justicia a quienes acrediten insuficiencia de recursos para litigar."
                }
            ],
            "goals": [
                "State that justice emanates from the people and is administered in the name of the King by judges and magistrates (Article 117.1).",
                "Explain why judges are independent, irremovable, and subject solely to the rule of law ('imperio de la ley').",
                "Identify the constitutional right to free legal aid ('justicia gratuita') for those with insufficient means (Article 119).",
                "Use 'sometido únicamente a' and 'exclusivamente' in legal definitions."
            ],
            "mc1": {
                "q": "Según la Constitución Española, ¿a quién corresponde en exclusiva el ejercicio del Poder Judicial (juzgar y hacer ejecutar lo juzgado)?",
                "opts": ["A los jueces y magistrados que integran los juzgados y tribunales.", "Al Ministerio del Interior.", "A las comisiones del Senado."]
            },
            "mc2": {
                "q": "¿De quién emana la justicia en España según el artículo 117.1 de la Constitución?",
                "opts": ["Del pueblo.", "Del Consejo de Ministros.", "De la Policía Nacional."]
            },
            "fb": {
                "sentence": "Los jueces y magistrados son independientes y están ___ únicamente al imperio de la ley. (sometido, masculino plural)",
                "answer": "sometidos",
                "english": "Judges and magistrates are independent and are subject solely to the rule of law."
            },
            "mc3": {
                "q": "¿En qué caso es gratuita la administración de justicia en España según el artículo 119?",
                "opts": [
                    "Cuando así lo disponga la ley y, en todo caso, respecto de quienes acrediten insuficiencia de recursos para litigar.",
                    "Solamente para los miembros del Gobierno.",
                    "En ningún caso; siempre es obligatorio pagar al juez."
                ]
            },
            "sb": {
                "words": ["La", "justicia", "emana", "del", "pueblo", "y", "se", "administra", "en", "nombre", "del", "Rey."],
                "english": "Justice emanates from the people and is administered in the name of the King."
            },
            "dlg": {
                "s1": "Rocío", "s2": "Andrés",
                "q": "¿Puede un ministro ordenar a un juez qué sentencia debe dictar en un juicio?",
                "opts": [
                    "No, los jueces gozan de total independencia judicial y están sometidos únicamente al imperio de la ley.",
                    "Sí, el Ministro de Justicia redacta las sentencias de los juzgados.",
                    "Sí, siempre que lo autorice el Alcalde."
                ]
            },
            "listen": {
                "sentence": "La justicia emana del pueblo y se administra en nombre del Rey por jueces y magistrados independientes.",
                "opts": [
                    "Justice emanates from the people and is administered in the name of the King by independent judges and magistrates.",
                    "Judges are appointed and dismissed at will by the Council of Ministers.",
                    "Free legal aid is forbidden by the Spanish Constitution."
                ]
            }
        },
        {
            "num": "02",
            "story_suffix": "cgpj",
            "title": "El Consejo General del Poder Judicial y el Tribunal Supremo",
            "theme": "El Poder Judicial",
            "goal": "Diferenciar el Consejo General del Poder Judicial (órgano de gobierno de los jueces) y el Tribunal Supremo (órgano jurisdiccional superior).",
            "grammar_short": "salvo lo dispuesto en",
            "grammar_slug": "salvo-lo-dispuesto-en",
            "grammar_title": "Excepciones jurídicas: «salvo lo dispuesto en» y «con jurisdicción en»",
            "location": "Madrid, plaza de la Villa de París",
            "words": [
                {"lemma": "el Consejo General del Poder Judicial", "translation": "General Council of the Judiciary (CGPJ)", "pos": "expression"},
                {"lemma": "el Tribunal Supremo", "translation": "Supreme Court", "pos": "expression"},
                {"lemma": "el órgano jurisdiccional", "translation": "jurisdictional body / court", "pos": "expression"},
                {"lemma": "el órgano de gobierno", "translation": "governing body", "pos": "expression"},
                {"lemma": "el vocal", "translation": "council member (of the CGPJ)", "pos": "noun"},
                {"lemma": "la jurisdicción", "translation": "jurisdiction", "pos": "noun"},
                {"lemma": "la garantía constitucional", "translation": "constitutional guarantee", "pos": "expression"},
                {"lemma": "el ascenso", "translation": "promotion (in the judicial career)", "pos": "noun"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 123.1 de la Constitución define al Tribunal Supremo como el órgano jurisdiccional superior en todos los órdenes, introduciendo una excepción precisa con la fórmula *salvo lo dispuesto en materia de garantías constitucionales* (que corresponde al Tribunal Constitucional)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Tribunal Supremo, con jurisdicción en toda España, es el órgano jurisdiccional superior en todos los órdenes, salvo lo dispuesto en materia de garantías constitucionales.", "english": "The Supreme Court, with jurisdiction throughout Spain, is the highest judicial body in all areas of law, except as provided in matters of constitutional guarantees."},
                        {"spanish": "El Consejo General del Poder Judicial es el órgano de gobierno del Poder Judicial.", "english": "The General Council of the Judiciary is the governing body of the Judiciary."},
                        {"spanish": "El CGPJ está integrado por el Presidente del Tribunal Supremo, que lo preside, y por veinte vocales nombrados por cinco años.", "english": "The CGPJ is composed of the President of the Supreme Court, who presides over it, and twenty members appointed for five years."},
                        {"spanish": "El CGPJ no dicta sentencias, sino que gestiona los nombramientos, ascensos, inspección y régimen disciplinario de los jueces.", "english": "The CGPJ does not issue court judgments; rather, it manages the appointments, promotions, inspection, and disciplinary regime of judges."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Para el examen CCSE, distingue con claridad: el *Tribunal Supremo* es el tribunal superior que juzga y dicta sentencias en toda España; el *Consejo General del Poder Judicial (CGPJ)* es el órgano que gobierna a los jueces (nombramientos, ascensos, disciplina) para proteger su independencia frente al Gobierno."
                }
            ],
            "story_summary": "Articles 122 and 123 distinguish the General Council of the Judiciary (CGPJ) — the 20-member governing body of judges that safeguards their independence — from the Supreme Court (Tribunal Supremo), the highest court in Spain across all legal orders.",
            "story_paragraphs": [
                "Si los jueces deben ser independientes del Gobierno, ¿quién decide entonces sus destinos, sus ascensos y su régimen disciplinario sin interferencias políticas?",
                "Para cumplir esa función, el artículo 122.2 de la Constitución crea el Consejo General del Poder Judicial (CGPJ), que es el órgano de gobierno de los jueces y magistrados.",
                "El CGPJ está integrado por el Presidente del Tribunal Supremo —que preside también el Consejo— y por veinte miembros (llamados vocales) nombrados por el Rey por un período de cinco años: doce entre jueces y magistrados de todas las categorías judiciales y ocho entre abogados y otros juristas de reconocida competencia con más de quince años de ejercicio, elegidos por mayoría de tres quintos del Congreso y del Senado.",
                "Por su parte, el órgano que ocupa la cúspide de los tribunales que dictan sentencias es el Tribunal Supremo, regulado en el artículo 123 con sede en Madrid y jurisdicción en toda España.",
                "El Tribunal Supremo es el órgano jurisdiccional superior en todos los órdenes (civil, penal, contencioso-administrativo, social y militar), salvo lo dispuesto en materia de garantías constitucionales, ámbito reservado al Tribunal Constitucional."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es el órgano de gobierno de los jueces y magistrados en España según el artículo 122 de la Constitución?",
                    "options": [
                        "El Consejo General del Poder Judicial (CGPJ)",
                        "El Ministerio del Interior",
                        "El Consejo de Estado",
                        "El Tribunal de Cuentas"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 122.2 establece que el Consejo General del Poder Judicial es el órgano de gobierno del mismo."
                },
                {
                    "question": "¿Cuál es el órgano jurisdiccional superior en todos los órdenes, con jurisdicción en toda España, salvo en materia de garantías constitucionales?",
                    "options": ["El Tribunal Supremo", "La Audiencia Provincial", "El Juzgado de Paz", "El Defensor del Pueblo"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 123.1, el Tribunal Supremo es el órgano jurisdiccional superior en todos los órdenes."
                },
                {
                    "question": "¿Quién preside tanto el Tribunal Supremo como el Consejo General del Poder Judicial?",
                    "options": [
                        "El Presidente del Tribunal Supremo (nombrado por el Rey a propuesta del CGPJ)",
                        "El Alcalde de Madrid",
                        "El Presidente del Senado",
                        "El Ministro de Hacienda"
                    ],
                    "correctIndex": 0,
                    "explanation": "El Presidente del Tribunal Supremo preside asimismo el Consejo General del Poder Judicial."
                }
            ],
            "goals": [
                "Identify the 'Consejo General del Poder Judicial' (CGPJ) as the governing body of judges (Article 122).",
                "Identify the 'Tribunal Supremo' as the highest court in all legal orders across Spain (Article 123).",
                "State that the President of the Supreme Court also presides over the CGPJ (composed of 20 members appointed for 5 years).",
                "Use 'salvo lo dispuesto en' to express constitutional exceptions."
            ],
            "mc1": {
                "q": "¿Qué institución es el órgano de gobierno del Poder Judicial encargado de los nombramientos, ascensos e inspección de los jueces?",
                "opts": ["El Consejo General del Poder Judicial (CGPJ).", "El Consejo de Estado.", "El Senado."]
            },
            "mc2": {
                "q": "Según el artículo 123 de la Constitución, ¿cuál es el órgano jurisdiccional superior en todos los órdenes en España?",
                "opts": ["El Tribunal Supremo.", "El Tribunal de Cuentas.", "El Juzgado de Primera Instancia."]
            },
            "fb": {
                "sentence": "El Tribunal Supremo es el órgano jurisdiccional superior en todos los órdenes, ___ lo dispuesto en materia de garantías constitucionales. (salvo)",
                "answer": "salvo",
                "english": "The Supreme Court is the highest judicial body in all orders, except as provided in matters of constitutional guarantees."
            },
            "mc3": {
                "q": "¿Por cuántos vocales (además de su Presidente) está integrado el Consejo General del Poder Judicial y cuánto dura su mandato?",
                "opts": [
                    "Por veinte vocales nombrados por un período de cinco años.",
                    "Por trescientos cincuenta vocales por cuatro años.",
                    "Por cinco vocales vitalicios."
                ]
            },
            "sb": {
                "words": ["El", "Consejo", "General", "del", "Poder", "Judicial", "es", "el", "órgano", "de", "gobierno", "de", "los", "jueces."],
                "english": "The General Council of the Judiciary is the governing body of the judges."
            },
            "dlg": {
                "s1": "César", "s2": "Marina",
                "q": "¿Dicta sentencias judiciales el Consejo General del Poder Judicial (CGPJ)?",
                "opts": [
                    "No, el CGPJ es un órgano de gobierno administrativo de los jueces; quienes dictan sentencias son los juzgados y tribunales como el Tribunal Supremo.",
                    "Sí, el CGPJ juzga todos los delitos de tráfico.",
                    "Sí, es la única cámara que aprueba las leyes orgánicas."
                ]
            },
            "listen": {
                "sentence": "El Tribunal Supremo tiene jurisdicción en toda España y su Presidente preside también el Consejo General del Poder Judicial.",
                "opts": [
                    "The Supreme Court has jurisdiction throughout Spain and its President also presides over the General Council of the Judiciary.",
                    "The CGPJ is part of the Ministry of the Interior.",
                    "Each municipality has its own Supreme Court."
                ]
            }
        },
        {
            "num": "03",
            "story_suffix": "fiscalia",
            "title": "El Ministerio Fiscal y la participación ciudadana en la justicia",
            "theme": "El Poder Judicial",
            "goal": "Conocer la misión del Ministerio Fiscal (artículo 124), el Fiscal General del Estado y la participación ciudadana mediante el Jurado (artículo 125).",
            "grammar_short": "tener por misión + infinitivo",
            "grammar_slug": "tener-por-mision-infinitivo",
            "grammar_title": "Definir la misión institucional: «tener por misión + infinitivo»",
            "location": "Madrid",
            "words": [
                {"lemma": "el Ministerio Fiscal", "translation": "Public Prosecutor's Office", "pos": "expression"},
                {"lemma": "el Fiscal General del Estado", "translation": "State Attorney General / Chief Public Prosecutor", "pos": "expression"},
                {"lemma": "la legalidad", "translation": "legality", "pos": "noun"},
                {"lemma": "el interés público", "translation": "public interest", "pos": "expression"},
                {"lemma": "el jurado", "translation": "jury (citizen jury)", "pos": "noun"},
                {"lemma": "la acción popular", "translation": "popular prosecution / citizen legal action", "pos": "expression"},
                {"lemma": "la imparcialidad", "translation": "impartiality", "pos": "noun"},
                {"lemma": "promover", "translation": "to promote, initiate (legal action)", "pos": "verb"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 124 de la Constitución utiliza la estructura *tener por misión + infinitivo* (*el Ministerio Fiscal tiene por misión promover la acción de la justicia*) para enunciar el propósito constitucional de un órgano del Estado."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Ministerio Fiscal tiene por misión promover la acción de la justicia en defensa de la legalidad y del interés público.", "english": "The Public Prosecutor's Office has the mission of promoting the action of justice in defense of legality and the public interest."},
                        {"spanish": "El Ministerio Fiscal ejerce sus funciones conforme a los principios de unidad de actuación, dependencia jerárquica, legalidad e imparcialidad.", "english": "The Public Prosecutor's Office exercises its functions in accordance with the principles of unity of action, hierarchical dependence, legality, and impartiality."},
                        {"spanish": "El Fiscal General del Estado es nombrado por el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial.", "english": "The State Attorney General is appointed by the King, at the proposal of the Government, after hearing the General Council of the Judiciary."},
                        {"spanish": "Los ciudadanos pueden participar en la Administración de Justicia mediante la institución del Jurado.", "english": "Citizens may participate in the Administration of Justice through the institution of the Jury."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Observa el participio absoluto jurídico *oído el Consejo General del Poder Judicial* (after hearing / consulting the CGPJ), muy habitual en los nombramientos constitucionales."
                }
            ],
            "story_summary": "Articles 124 and 125 regulate the Public Prosecutor's Office (Ministerio Fiscal), headed by the State Attorney General to defend legality and citizens' rights, and direct citizen participation in justice through the Jury (Tribunal del Jurado) and popular action.",
            "story_paragraphs": [
                "En los procesos judiciales, junto a los jueces que dictan sentencia y a los abogados que defienden a las partes, interviene una institución pública esencial regulada en el artículo 124 de la Constitución: el Ministerio Fiscal (o Fiscalía).",
                "El Ministerio Fiscal tiene por misión promover la acción de la justicia en defensa de la legalidad, de los derechos de los ciudadanos y del interés público tutelado por la ley, así como velar por la independencia de los tribunales y proteger especialmente a los menores y a las víctimas.",
                "La Fiscalía ejerce sus funciones por medio de órganos propios conforme a los principios de unidad de actuación y dependencia jerárquica y con sujeción, en todo caso, a los de legalidad e imparcialidad.",
                "A la cabeza de esta institución se sitúa el Fiscal General del Estado, que es nombrado por el Rey, a propuesta del Gobierno, oído previamente el Consejo General del Poder Judicial.",
                "Finalmente, el artículo 125 de la Constitución abre la puerta a la participación directa de los ciudadanos en la Administración de Justicia a través de tres vías: el ejercicio de la acción popular, la participación en el Tribunal del Jurado (integrado por nueve ciudadanos elegidos por sorteo y presidido por un magistrado en determinados procesos penales) y los tribunales consuetudinarios y tradicionales (como el histórico Tribunal de las Aguas de Valencia o el Consejo de Hombres Buenos de Murcia)."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 124 de la Constitución, ¿qué institución tiene por misión promover la acción de la justicia en defensa de la legalidad, de los derechos de los ciudadanos y del interés público?",
                    "options": ["El Ministerio Fiscal", "El Tribunal de Cuentas", "La Junta Electoral", "El Banco de España"],
                    "correctIndex": 0,
                    "explanation": "El artículo 124.1 define esta misión como propia del Ministerio Fiscal."
                },
                {
                    "question": "¿Cómo se nombra al Fiscal General del Estado según el artículo 124.4?",
                    "options": [
                        "Lo nombra el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial",
                        "Lo eligen los alcaldes cada dos años",
                        "Lo nombra el Defensor del Pueblo sin intervención del Gobierno",
                        "Accede al cargo por herencia"
                    ],
                    "correctIndex": 0,
                    "explanation": "El Fiscal General del Estado es nombrado por el Rey, a propuesta del Gobierno, oído el CGPJ."
                },
                {
                    "question": "¿A través de qué institución prevista en el artículo 125 pueden participar directamente los ciudadanos en determinados juicios penales?",
                    "options": ["Mediante la institución del Jurado (Tribunal del Jurado)", "Mediante el Consejo de Ministros", "Mediante el Senado", "Mediante el Consejo de Estado"],
                    "correctIndex": 0,
                    "explanation": "El artículo 125 reconoce la participación de los ciudadanos en la Administración de Justicia mediante la institución del Jurado."
                }
            ],
            "goals": [
                "State the constitutional mission of the Public Prosecutor's Office ('Ministerio Fiscal') under Article 124.",
                "Explain how the State Attorney General ('Fiscal General del Estado') is appointed (by the King, at the proposal of the Government, after hearing the CGPJ).",
                "Identify how citizens participate in the administration of justice: popular action, the Jury ('Jurado'), and traditional customary courts (Article 125).",
                "Use 'tener por misión + infinitivo' to define institutional purposes."
            ],
            "mc1": {
                "q": "¿Qué institución tiene por misión promover la acción de la justicia en defensa de la legalidad, de los derechos de los ciudadanos y del interés público?",
                "opts": ["El Ministerio Fiscal.", "El Consejo de Estado.", "El Tribunal de Cuentas."]
            },
            "mc2": {
                "q": "¿Cómo participan los ciudadanos en la Administración de Justicia según el artículo 125 de la Constitución?",
                "opts": [
                    "Mediante el ejercicio de la acción popular, la institución del Jurado y los tribunales consuetudinarios.",
                    "Dictando reales decretos-leyes en los ayuntamientos.",
                    "Nombrando directamente a los magistrados del Tribunal Supremo."
                ]
            },
            "fb": {
                "sentence": "El Ministerio Fiscal tiene por ___ promover la acción de la justicia en defensa de la legalidad. (misión)",
                "answer": "misión",
                "english": "The Public Prosecutor's Office has the mission of promoting the action of justice in defense of legality."
            },
            "mc3": {
                "q": "¿Quién nombra al Fiscal General del Estado a propuesta del Gobierno, oído el Consejo General del Poder Judicial?",
                "opts": ["El Rey.", "El Presidente del Senado.", "El Defensor del Pueblo."]
            },
            "sb": {
                "words": ["Los", "ciudadanos", "pueden", "participar", "en", "la", "justicia", "mediante", "el", "Jurado."],
                "english": "Citizens can participate in justice through the Jury."
            },
            "dlg": {
                "s1": "Irene", "s2": "Carlos",
                "q": "¿Existen en España tribunales consuetudinarios y tradicionales reconocidos por la Constitución?",
                "opts": [
                    "Sí, el artículo 125 los reconoce expresamente, como el Tribunal de las Aguas de la Vega de Valencia o el Consejo de Hombres Buenos de Murcia.",
                    "No, están prohibidos desde 1978.",
                    "Solo existen para juzgar delitos militares."
                ]
            },
            "listen": {
                "sentence": "El Fiscal General del Estado es nombrado por el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial.",
                "opts": [
                    "The State Attorney General is appointed by the King, at the proposal of the Government, after hearing the General Council of the Judiciary.",
                    "The State Attorney General is elected directly by municipal councils.",
                    "Citizens are barred from serving on juries in Spain."
                ]
            }
        },
        {
            "num": "04",
            "story_suffix": "constitucional",
            "title": "El Tribunal Constitucional: intérprete supremo de la Constitución",
            "theme": "El Poder Judicial",
            "goal": "Conocer la composición de los 12 magistrados del Tribunal Constitucional (Título IX), su mandato de 9 años y su independencia.",
            "grammar_short": "nombrados a propuesta de",
            "grammar_slug": "a-propuesta-de",
            "grammar_title": "Distribución de nombramientos: «cuatro a propuesta del Congreso...»",
            "location": "Madrid, calle Domenico Scarlatti",
            "words": [
                {"lemma": "el Tribunal Constitucional", "translation": "Constitutional Court", "pos": "expression"},
                {"lemma": "el intérprete supremo", "translation": "supreme interpreter", "pos": "expression"},
                {"lemma": "el jurista", "translation": "jurist, legal scholar", "pos": "noun"},
                {"lemma": "la reconocida competencia", "translation": "recognized competence / standing", "pos": "expression"},
                {"lemma": "el período", "translation": "period, term of office", "pos": "noun"},
                {"lemma": "renovarse", "translation": "to be renewed", "pos": "verb"},
                {"lemma": "incompatible", "translation": "incompatible", "pos": "adjective"},
                {"lemma": "la mayoría de tres quintos", "translation": "three-fifths majority", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 159.1 de la Constitución detalla la composición de los doce miembros del Tribunal Constitucional repartiendo su origen entre los tres poderes del Estado mediante la preposición *a propuesta de*: cuatro a propuesta del Congreso, cuatro del Senado, dos del Gobierno y dos del CGPJ."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Tribunal Constitucional se compone de doce miembros nombrados por el Rey por un período de nueve años.", "english": "The Constitutional Court is composed of twelve members appointed by the King for a period of nine years."},
                        {"spanish": "De los doce magistrados, cuatro son nombrados a propuesta del Congreso por mayoría de tres quintos de sus miembros y cuatro a propuesta del Senado.", "english": "Of the twelve magistrates, four are appointed at the proposal of Congress by a three-fifths majority of its members and four at the proposal of the Senate."},
                        {"spanish": "Asimismo, dos magistrados son nombrados a propuesta del Gobierno y dos a propuesta del Consejo General del Poder Judicial.", "english": "Likewise, two magistrates are appointed at the proposal of the Government and two at the proposal of the General Council of the Judiciary."},
                        {"spanish": "Los miembros del Tribunal Constitucional se renuevan por terceras partes cada tres años.", "english": "The members of the Constitutional Court are renewed by thirds every three years."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Memoriza la cifra clave para el examen CCSE: **12 magistrados** en el Tribunal Constitucional (4 Congreso + 4 Senado + 2 Gobierno + 2 CGPJ), nombrados por **9 años**."
                }
            ],
            "story_summary": "Title IX (Articles 159-165) regulates the Constitutional Court (Tribunal Constitucional) as the supreme interpreter of the Constitution, independent of the ordinary Judiciary and composed of 12 magistrates appointed by the King for 9-year terms.",
            "story_paragraphs": [
                "¿Qué órgano vigila que ninguna ley aprobada por el Parlamento o por las comunidades autónomas vulnere la Constitución Española? Esa misión corresponde al Tribunal Constitucional, regulado en un título propio: el Título IX de la Constitución (artículos 159 a 165).",
                "El Tribunal Constitucional es el intérprete supremo de la Constitución; es un órgano constitucional independiente de los demás y no forma parte del Poder Judicial ordinario (cuya cúspide es el Tribunal Supremo).",
                "Según el artículo 159.1, el Tribunal Constitucional se compone exactamente de doce miembros nombrados por el Rey: cuatro a propuesta del Congreso de los Diputados por mayoría de tres quintos de sus miembros; cuatro a propuesta del Senado, con idéntica mayoría; dos a propuesta del Gobierno, y dos a propuesta del Consejo General del Poder Judicial.",
                "Para ser nombrado magistrado constitucional es necesario ser ciudadano español y ser magistrado, fiscal, profesor de universidad, funcionario público o abogado, todos ellos juristas de reconocida competencia con más de quince años de ejercicio profesional.",
                "Los doce magistrados son designados por un período de nueve años, se renuevan por terceras partes cada tres años y eligen entre sus propios miembros, en votación secreta, al Presidente del Tribunal Constitucional por un período de tres años."
            ],
            "comp_questions": [
                {
                    "question": "¿De cuántos miembros se compone el Tribunal Constitucional según el artículo 159.1 de la Constitución?",
                    "options": ["De 12 miembros", "De 20 miembros", "De 350 miembros", "De 5 miembros"],
                    "correctIndex": 0,
                    "explanation": "El Tribunal Constitucional se compone de 12 miembros nombrados por el Rey (4 Congreso, 4 Senado, 2 Gobierno y 2 CGPJ)."
                },
                {
                    "question": "¿Por cuántos años son designados los magistrados del Tribunal Constitucional?",
                    "options": ["Por un período de 9 años (renovándose por terceras partes cada 3 años)", "Por un período de 4 años", "Con carácter vitalicio", "Por un período de 2 años"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 159.3, los miembros del Tribunal Constitucional son designados por un período de nueve años."
                },
                {
                    "question": "¿Cuál es la función principal del Tribunal Constitucional?",
                    "options": [
                        "Ser el intérprete supremo de la Constitución y garantizar que las leyes y actos públicos respeten el texto constitucional",
                        "Elaborar los Presupuestos Generales del Estado",
                        "Dirigir la política exterior y las embajadas",
                        "Gestionar el padrón de los municipios"
                    ],
                    "correctIndex": 0,
                    "explanation": "El Tribunal Constitucional es el intérprete supremo de la Constitución y vela por la constitucionalidad de las leyes y los derechos fundamentales."
                }
            ],
            "goals": [
                "Define the Constitutional Court ('Tribunal Constitucional') under Title IX as the supreme interpreter of the Constitution.",
                "State its exact composition: 12 members appointed by the King (4 proposed by Congress, 4 by the Senate, 2 by the Government, 2 by the CGPJ).",
                "Identify the 9-year term of office of constitutional magistrates (renewed by thirds every 3 years).",
                "Use 'a propuesta de' to detail institutional appointments."
            ],
            "mc1": {
                "q": "¿Cuántos magistrados integran el Tribunal Constitucional de España?",
                "opts": ["Doce miembros.", "Veinte miembros.", "Cincuenta miembros."]
            },
            "mc2": {
                "q": "¿Cómo se reparte la propuesta de los doce miembros del Tribunal Constitucional antes de su nombramiento por el Rey?",
                "opts": [
                    "Cuatro a propuesta del Congreso, cuatro del Senado, dos del Gobierno y dos del Consejo General del Poder Judicial.",
                    "Seis a propuesta de los alcaldes y seis a propuesta del Defensor del Pueblo.",
                    "Los doce son elegidos únicamente por el Senado."
                ]
            },
            "fb": {
                "sentence": "Los doce magistrados del Tribunal Constitucional son nombrados por el Rey, cuatro de ellos a ___ del Congreso de los Diputados. (propuesta)",
                "answer": "propuesta",
                "english": "The twelve magistrates of the Constitutional Court are appointed by the King, four of them at the proposal of the Congress of Deputies."
            },
            "mc3": {
                "q": "¿Cuál es la duración del mandato de los magistrados del Tribunal Constitucional?",
                "opts": ["Nueve años.", "Cuatro años.", "Cinco años."]
            },
            "sb": {
                "words": ["El", "Tribunal", "Constitucional", "se", "compone", "de", "doce", "miembros", "nombrados", "por", "el", "Rey."],
                "english": "The Constitutional Court is composed of twelve members appointed by the King."
            },
            "dlg": {
                "s1": "Elena", "s2": "Roberto",
                "q": "¿Forma parte el Tribunal Constitucional del Poder Judicial ordinario que encabeza el Tribunal Supremo?",
                "opts": [
                    "No, el Tribunal Constitucional se regula en el Título IX como un órgano constitucional independiente y es el intérprete supremo de la Constitución.",
                    "Sí, es una sala más dentro del Tribunal Supremo.",
                    "Sí, depende jerárquicamente del Ministerio del Interior."
                ]
            },
            "listen": {
                "sentence": "El Tribunal Constitucional es el intérprete supremo de la Constitución y se compone de doce miembros nombrados por un período de nueve años.",
                "opts": [
                    "The Constitutional Court is the supreme interpreter of the Constitution and is composed of twelve members appointed for a period of nine years.",
                    "The Constitutional Court has twenty members appointed for five years.",
                    "Constitutional magistrates do not need to be legal professionals."
                ]
            }
        },
        {
            "num": "05",
            "story_suffix": "amparo",
            "title": "El recurso de inconstitucionalidad y el recurso de amparo",
            "theme": "El Poder Judicial",
            "goal": "Diferenciar los tres grandes procesos ante el Tribunal Constitucional: el recurso de inconstitucionalidad, el recurso de amparo y los conflictos de competencia.",
            "grammar_short": "ante + instancia judicial",
            "grammar_slug": "ante-preposicion-juridica",
            "grammar_title": "Preposición procesal «ante»: presentar un recurso ante un tribunal",
            "location": "Madrid",
            "words": [
                {"lemma": "el recurso de amparo", "translation": "constitutional appeal for protection of fundamental rights", "pos": "expression"},
                {"lemma": "el recurso de inconstitucionalidad", "translation": "appeal of unconstitutionality (against a law)", "pos": "expression"},
                {"lemma": "el conflicto de competencia", "translation": "conflict of jurisdiction (between State and regions)", "pos": "expression"},
                {"lemma": "vulnerar", "translation": "to infringe, violate (a right)", "pos": "verb"},
                {"lemma": "interponer", "translation": "to lodge, file (an appeal)", "pos": "verb"},
                {"lemma": "la objeción de conciencia", "translation": "conscientious objection", "pos": "expression"},
                {"lemma": "la fuerza de ley", "translation": "force of law", "pos": "expression"},
                {"lemma": "el valor de cosa juzgada", "translation": "res judicata value (final, non-appealable ruling)", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "En el lenguaje procesal español, la preposición *ante* (before / with) indica el tribunal o autoridad al que se acude para reclamar tutela jurídica (*interponer un recurso de amparo ante el Tribunal Constitucional*, *comparecer ante el juez*)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "Cualquier ciudadano puede interponer un recurso de amparo ante el Tribunal Constitucional cuando se vulneren sus derechos fundamentales.", "english": "Any citizen may file an appeal for constitutional protection before the Constitutional Court when their fundamental rights are violated."},
                        {"spanish": "El Presidente del Gobierno, el Defensor del Pueblo, 50 diputados o 50 senadores están legitimados para interponer el recurso de inconstitucionalidad ante el Tribunal Constitucional.", "english": "The Prime Minister, the Ombudsman, 50 deputies, or 50 senators have standing to file an appeal of unconstitutionality before the Constitutional Court."},
                        {"spanish": "El Estado y las comunidades autónomas plantean sus conflictos de competencia ante el Tribunal Constitucional.", "english": "The State and the autonomous communities bring their conflicts of jurisdiction before the Constitutional Court."},
                        {"spanish": "Contra las sentencias del Tribunal Constitucional no cabe recurso alguno en el orden interno.", "english": "No appeal lies against the judgments of the Constitutional Court in the domestic legal order."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Distingue los dos grandes recursos para el examen CCSE: el *recurso de inconstitucionalidad* se dirige contra **leyes** (lo presentan el Presidente, el Defensor del Pueblo, 50 diputados, 50 senadores o los gobiernos/parlamentos autonómicos); el *recurso de amparo* protege los **derechos fundamentales** de las personas (lo puede presentar cualquier ciudadano afectado, el Defensor del Pueblo o el Ministerio Fiscal)."
                }
            ],
            "story_summary": "Articles 161 and 162 define the three key powers of the Constitutional Court: appeals of unconstitutionality against laws, constitutional 'amparo' appeals protecting fundamental rights (Articles 14 to 29 and 30.2), and conflicts of jurisdiction between the State and Autonomous Communities.",
            "story_paragraphs": [
                "El artículo 161 de la Constitución Española atribuye al Tribunal Constitucional jurisdicción en todo el territorio español y le encomienda tres grandes funciones que son materia esencial del examen CCSE.",
                "En primer lugar, el Tribunal conoce del «recurso de inconstitucionalidad» contra leyes y disposiciones normativas con fuerza de ley. Según el artículo 162.1, están legitimados para interponerlo el Presidente del Gobierno, el Defensor del Pueblo, cincuenta Diputados, cincuenta Senadores, los órganos colegiados ejecutivos de las comunidades autónomas y, en su caso, las asambleas de las mismas.",
                "En segundo lugar, conoce del «recurso de amparo» por violación de los derechos y libertades fundamentales reconocidos en el artículo 14 (igualdad ante la ley), en la Sección primera del Capítulo segundo del Título I (artículos 15 a 29) y en el artículo 30.2 (objeción de conciencia).",
                "A diferencia del recurso contra leyes, el recurso de amparo puede ser interpuesto directamente por toda persona natural o jurídica que invoque un interés legítimo (una vez agotada la vía judicial previa), así como por el Defensor del Pueblo y por el Ministerio Fiscal.",
                "En tercer lugar, el Tribunal Constitucional resuelve los «conflictos de competencia» entre el Estado y las comunidades autónomas o de los de estas entre sí, asegurando que cada administración ejerza sus competencias dentro de los límites de la Constitución y de los Estatutos de Autonomía."
            ],
            "comp_questions": [
                {
                    "question": "¿Cómo se llama el recurso que cualquier ciudadano puede presentar ante el Tribunal Constitucional cuando considera vulnerados sus derechos fundamentales (artículos 14 a 29)?",
                    "options": ["Recurso de amparo", "Moción de censura", "Cuestión de confianza", "Iniciativa legislativa popular"],
                    "correctIndex": 0,
                    "explanation": "El recurso de amparo ante el Tribunal Constitucional tutela los derechos y libertades fundamentales de los artículos 14 a 29 y 30.2."
                },
                {
                    "question": "¿Quiénes están legitimados según el artículo 162.1 para interponer un recurso de inconstitucionalidad contra una ley?",
                    "options": [
                        "El Presidente del Gobierno, el Defensor del Pueblo, 50 diputados, 50 senadores y los gobiernos o parlamentos de las comunidades autónomas",
                        "Un solo concejal municipal",
                        "Cualquier turista extranjero sin agotar la vía judicial",
                        "Las cámaras de comercio provinciales"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 162.1 reserva la legitimación del recurso de inconstitucionalidad al Presidente del Gobierno, Defensor del Pueblo, 50 diputados, 50 senadores y órganos ejecutivos o legislativos autonómicos."
                },
                {
                    "question": "¿Qué órgano resuelve los conflictos de competencia entre el Estado y las comunidades autónomas?",
                    "options": ["El Tribunal Constitucional", "El Tribunal de Cuentas", "El Ayuntamiento de Madrid", "El Consejo de Estado"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 161.1.c, el Tribunal Constitucional es competente para resolver los conflictos de competencia entre el Estado y las comunidades autónomas."
                }
            ],
            "goals": [
                "Distinguish an appeal of unconstitutionality ('recurso de inconstitucionalidad' against laws) from an appeal for protection ('recurso de amparo' for fundamental rights).",
                "List who has standing to file an appeal of unconstitutionality: the Prime Minister, Ombudsman, 50 deputies, 50 senators, and regional governments/parliaments (Article 162).",
                "Identify the Constitutional Court as the body that resolves conflicts of jurisdiction between the State and Autonomous Communities.",
                "Use the procedural preposition 'ante' accurately."
            ],
            "mc1": {
                "q": "¿Qué recurso protege ante el Tribunal Constitucional a los ciudadanos frente a la vulneración de los derechos fundamentales de los artículos 14 a 29 de la Constitución?",
                "opts": ["El recurso de amparo.", "El recurso de alzada municipal.", "La cuestión de confianza."]
            },
            "mc2": {
                "q": "¿Cuántos diputados o cuántos senadores como mínimo se necesitan para interponer un recurso de inconstitucionalidad contra una ley?",
                "opts": ["Cincuenta diputados o cincuenta senadores.", "Cinco diputados o cinco senadores.", "Trescientos diputados."]
            },
            "fb": {
                "sentence": "Cualquier ciudadano afectado puede interponer un recurso de amparo ___ el Tribunal Constitucional. (ante)",
                "answer": "ante",
                "english": "Any affected citizen may file an appeal for constitutional protection before the Constitutional Court."
            },
            "mc3": {
                "q": "¿Puede el Defensor del Pueblo interponer tanto el recurso de inconstitucionalidad como el recurso de amparo?",
                "opts": [
                    "Sí, el artículo 162 de la Constitución le otorga legitimación para interponer ambos recursos.",
                    "No, el Defensor del Pueblo no puede acudir nunca al Tribunal Constitucional.",
                    "Solo puede presentar quejas ante los alcaldes."
                ]
            },
            "sb": {
                "words": ["El", "Tribunal", "Constitucional", "resuelve", "los", "conflictos", "de", "competencia."],
                "english": "The Constitutional Court resolves conflicts of jurisdiction."
            },
            "dlg": {
                "s1": "Patricia", "s2": "Gonzalo",
                "q": "Si una comunidad autónoma aprueba una ley que invade una competencia exclusiva del Estado, ¿a qué institución acude el Gobierno?",
                "opts": [
                    "Acude ante el Tribunal Constitucional mediante un recurso de inconstitucionalidad o un conflicto de competencia.",
                    "Acude al Tribunal de Cuentas para anular la ley.",
                    "Acude al Defensor del Pueblo para que dicte sentencia."
                ]
            },
            "listen": {
                "sentence": "El recurso de amparo protege a los ciudadanos ante el Tribunal Constitucional cuando se vulneran sus derechos y libertades fundamentales.",
                "opts": [
                    "The 'amparo' appeal protects citizens before the Constitutional Court when their fundamental rights and liberties are violated.",
                    "Only fifty senators can file an 'amparo' appeal.",
                    "Conflicts of jurisdiction between regions are decided by the Mayor of Madrid."
                ]
            }
        }
    ]

    comb = {
        "title": "El Poder Judicial y el Tribunal Constitucional",
        "summary": "Complete CCSE guide to Title VI and Title IX of the Spanish Constitution: judicial independence and free legal aid (Articles 117 & 119), the 20-member CGPJ vs. the Supreme Court (Articles 122 & 123), the Public Prosecutor's Office and the Jury (Articles 124 & 125), and the 12-member Constitutional Court with its appeals of unconstitutionality and 'amparo'.",
        "paragraphs": [
            "Según el artículo 117 de la Constitución, la justicia emana del pueblo y se administra en nombre del Rey por jueces y magistrados independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley, garantizándose la justicia gratuita a quienes acrediten insuficiencia de recursos.",
            "El Consejo General del Poder Judicial (CGPJ), presidido por el Presidente del Tribunal Supremo e integrado por 20 vocales nombrados por cinco años, es el órgano de gobierno de los jueces, mientras que el Tribunal Supremo es el órgano jurisdiccional superior en todos los órdenes.",
            "El Ministerio Fiscal, encabezado por el Fiscal General del Estado, promueve la acción de la justicia en defensa de la legalidad y del interés público, y los ciudadanos participan en la justicia mediante la acción popular, el Tribunal del Jurado y los tribunales consuetudinarios.",
            "En el Título IX se regula el Tribunal Constitucional, intérprete supremo de la Constitución e independiente del Poder Judicial ordinario, compuesto por 12 magistrados nombrados por el Rey por nueve años (4 a propuesta del Congreso, 4 del Senado, 2 del Gobierno y 2 del CGPJ).",
            "Ante el Tribunal Constitucional se interponen el recurso de inconstitucionalidad contra leyes (por el Presidente del Gobierno, el Defensor del Pueblo, 50 diputados, 50 senadores o los gobiernos/parlamentos autonómicos), el recurso de amparo para tutelar derechos fundamentales y los conflictos de competencia."
        ],
        "comp_questions": [
            {
                "question": "¿Cuál es la diferencia entre el Consejo General del Poder Judicial (CGPJ), el Tribunal Supremo y el Tribunal Constitucional?",
                "options": [
                    "El CGPJ gobierna a los jueces (20 vocales), el Tribunal Supremo es el tribunal superior ordinario, y el Tribunal Constitucional (12 magistrados) es el intérprete supremo de la Constitución",
                    "Los tres son el mismo tribunal con distinta sede",
                    "El CGPJ dicta leyes y el Tribunal Supremo aprueba los Presupuestos",
                    "El Tribunal Constitucional depende de los alcaldes"
                ],
                "correctIndex": 0,
                "explanation": "Cada uno cumple un papel distinto: gobierno judicial (CGPJ), cúspide jurisdiccional ordinaria (Tribunal Supremo) y jurisdicción constitucional (Tribunal Constitucional)."
            },
            {
                "question": "¿Cuántos miembros componen el Tribunal Constitucional y cuánto dura su mandato?",
                "options": ["12 miembros nombrados por 9 años", "20 miembros nombrados por 5 años", "350 miembros nombrados por 4 años", "15 miembros vitalicios"],
                "correctIndex": 0,
                "explanation": "El Tribunal Constitucional consta de 12 miembros nombrados por 9 años (mientras que el CGPJ tiene 20 vocales por 5 años)."
            },
            {
                "question": "¿Qué recurso protege ante el Tribunal Constitucional los derechos fundamentales de cualquier ciudadano (artículos 14 a 29)?",
                "options": ["El recurso de amparo", "El recurso de inconstitucionalidad", "La moción de censura", "El real decreto legislativo"],
                "correctIndex": 0,
                "explanation": "El recurso de amparo es la garantía jurisdiccional ante el Tribunal Constitucional para proteger los derechos fundamentales."
            }
        ]
    }

    cons_stem = "b1-judicial-consolidation"
    consolidation = {
        "title": "Repaso y Simulacro: Poder Judicial y Tribunal Constitucional",
        "goal": "Consolidar el artículo 117, el CGPJ, el Tribunal Supremo, el Ministerio Fiscal, el Jurado y el Tribunal Constitucional para el examen CCSE.",
        "grammar": "Consolidación de estructuras judiciales y procesales",
        "goals": [
            "Consolidate CCSE exam facts on judicial independence, free legal aid, and the rule of law ('imperio de la ley').",
            "Distinguish the 20-member CGPJ (5-year term) from the Supreme Court and the 12-member Constitutional Court (9-year term).",
            "Verify mastery of the Public Prosecutor's Office ('Ministerio Fiscal'), the Jury, appeals of unconstitutionality, and 'amparo' appeals.",
            "Practice 'sometido únicamente a', 'salvo lo dispuesto en', 'tener por misión', 'a propuesta de', and 'ante'."
        ],
        "exercises": [
            {
                "id": f"{cons_stem}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el imperio de la ley", "rule / supremacy of law"],
                    ["la justicia gratuita", "free legal aid"],
                    ["el Consejo General del Poder Judicial", "General Council of the Judiciary (20 members)"],
                    ["el Tribunal Supremo", "Supreme Court"],
                    ["el Ministerio Fiscal", "Public Prosecutor's Office"],
                    ["el jurado", "citizen jury"],
                    ["el Tribunal Constitucional", "Constitutional Court (12 magistrates)"],
                    ["el recurso de amparo", "constitutional appeal for fundamental rights"]
                ],
                "teaches": ["sometido-unicamente-a"]
            },
            {
                "id": f"{cons_stem}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración expresa correctamente la sujeción de los jueces según el artículo 117.1?",
                "options": [
                    "Los jueces son independientes y están sometidos únicamente al imperio de la ley.",
                    "Los jueces están sometidos únicamente a las órdenes del Gobierno.",
                    "Los jueces son sometidos hacia el imperio de la ley."
                ],
                "correct": 0,
                "teaches": ["sometido-unicamente-a"]
            },
            {
                "id": f"{cons_stem}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué fórmula constitucional introduce la excepción relativa al Tribunal Constitucional en el artículo 123?",
                "options": [
                    "El Tribunal Supremo es el órgano jurisdiccional superior en todos los órdenes, salvo lo dispuesto en materia de garantías constitucionales.",
                    "El Tribunal Supremo es el órgano superior, mediante lo dispuesto en garantías constitucionales.",
                    "El Tribunal Supremo es el órgano superior, para que lo dispuesto en garantías constitucionales."
                ],
                "correct": 0,
                "teaches": ["salvo-lo-dispuesto-en"]
            },
            {
                "id": f"{cons_stem}.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura define el propósito constitucional del Ministerio Fiscal?",
                "options": [
                    "El Ministerio Fiscal tiene por misión promover la acción de la justicia en defensa de la legalidad.",
                    "El Ministerio Fiscal tiene de misión promoviendo la acción de la justicia.",
                    "El Ministerio Fiscal carece por misión promover la justicia."
                ],
                "correct": 0,
                "teaches": ["tener-por-mision-infinitivo"]
            },
            {
                "id": f"{cons_stem}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué preposición se utiliza para indicar el tribunal al que se dirige un recurso de amparo?",
                "options": [
                    "El ciudadano interpuso un recurso de amparo ante el Tribunal Constitucional.",
                    "El ciudadano interpuso un recurso de amparo bajo el Tribunal Constitucional.",
                    "El ciudadano interpuso un recurso de amparo según el Tribunal Constitucional."
                ],
                "correct": 0,
                "teaches": ["ante-preposicion-juridica"]
            },
            {
                "id": f"{cons_stem}.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La justicia emana del pueblo y se administra en nombre del Rey por jueces ___ únicamente al imperio de la ley. (sometido, masculino plural)",
                "answer": "sometidos",
                "teaches": ["sometido-unicamente-a"],
                "english": "Justice emanates from the people and is administered in the name of the King by judges subject solely to the rule of law."
            },
            {
                "id": f"{cons_stem}.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Ministerio Fiscal tiene por ___ promover la acción de la justicia en defensa de los derechos de los ciudadanos. (misión)",
                "answer": "misión",
                "teaches": ["tener-por-mision-infinitivo"],
                "english": "The Public Prosecutor's Office has the mission of promoting the action of justice in defense of citizens' rights."
            },
            {
                "id": f"{cons_stem}.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Defensor del Pueblo está legitimado para interponer recursos de amparo ___ el Tribunal Constitucional. (ante)",
                "answer": "ante",
                "teaches": ["ante-preposicion-juridica"],
                "english": "The Ombudsman has standing to file 'amparo' appeals before the Constitutional Court."
            },
            {
                "id": f"{cons_stem}.ex09",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Tribunal", "Supremo", "es", "el", "órgano", "jurisdiccional", "superior", "en", "todos", "los", "órdenes."],
                "solution": ["El", "Tribunal", "Supremo", "es", "el", "órgano", "jurisdiccional", "superior", "en", "todos", "los", "órdenes."],
                "english": "The Supreme Court is the highest judicial body in all areas of law.",
                "teaches": ["salvo-lo-dispuesto-en"]
            },
            {
                "id": f"{cons_stem}.ex10",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Un ciudadano considera que un acto ha vulnerado uno de sus derechos fundamentales reconocidos en los artículos 14 a 29. [A citizen considers that an act has violated one of their fundamental rights recognized in Articles 14 to 29.]",
                    "Primero acude a los tribunales ordinarios para agotar la vía judicial previa. [First they go to the ordinary courts to exhaust prior judicial remedies.]",
                    "Si la vulneración persiste, interpone finalmente un recurso de amparo ante el Tribunal Constitucional. [If the violation persists, they finally file an appeal for constitutional protection before the Constitutional Court.]"
                ],
                "solution": [0, 1, 2],
                "teaches": ["ante-preposicion-juridica"]
            },
            {
                "id": f"{cons_stem}.ex11",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Cuántos miembros tienen el Consejo General del Poder Judicial y el Tribunal Constitucional?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "El CGPJ está integrado por su Presidente y 20 vocales (por 5 años), mientras que el Tribunal Constitucional se compone de 12 magistrados (por 9 años).",
                    "Ambos tienen exactamente 50 miembros elegidos cada dos años.",
                    "El CGPJ tiene 12 miembros y el Tribunal Constitucional tiene 350."
                ],
                "correct": 0,
                "teaches": ["a-propuesta-de"]
            },
            {
                "id": f"{cons_stem}.ex12",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "La justicia será gratuita cuando así lo disponga la ley y, en todo caso, respecto de quienes acrediten insuficiencia de recursos para litigar.",
                "options": [
                    "Justice shall be free when so provided by law and, in all cases, for those who prove insufficient means to litigate.",
                    "Free legal aid does not exist in the Spanish judicial system.",
                    "Only members of Parliament have access to the courts."
                ],
                "correct": 0,
                "teaches": ["sometido-unicamente-a"]
            },
            {
                "id": f"{cons_stem}.ex13",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "El Tribunal Constitucional conoce del recurso de inconstitucionalidad contra leyes, del recurso de amparo y de los conflictos de competencia.",
                "options": [
                    "The Constitutional Court hears appeals of unconstitutionality against laws, 'amparo' appeals, and conflicts of jurisdiction.",
                    "The Constitutional Court is presided over by the Mayor of Madrid.",
                    "The Court of Auditors decides on fundamental rights appeals."
                ],
                "correct": 0,
                "teaches": ["ante-preposicion-juridica"]
            },
            {
                "id": f"{cons_stem}.ex14",
                "type": "dictation",
                "category": "listening",
                "sentence": "La justicia emana del pueblo y se administra en nombre del Rey.",
                "teaches": ["sometido-unicamente-a"],
                "english": "Justice emanates from the people and is administered in the name of the King."
            },
            {
                "id": f"{cons_stem}.ex15",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica la diferencia entre el Consejo General del Poder Judicial y el Tribunal Supremo. [Explain the difference between the General Council of the Judiciary and the Supreme Court.]",
                        "answer": "El Consejo General del Poder Judicial es el órgano de gobierno de los jueces, mientras que el Tribunal Supremo es el órgano jurisdiccional superior en todos los órdenes."
                    }
                ],
                "teaches": ["salvo-lo-dispuesto-en"]
            },
            {
                "id": f"{cons_stem}.ex16",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Indica cuántos magistrados componen el Tribunal Constitucional y qué órganos los proponen. [State how many magistrates compose the Constitutional Court and which bodies propose them.]",
                        "answer": "El Tribunal Constitucional se compone de doce miembros nombrados por el Rey: cuatro a propuesta del Congreso, cuatro del Senado, dos del Gobierno y dos del Consejo General del Poder Judicial."
                    }
                ],
                "teaches": ["a-propuesta-de"]
            },
            {
                "id": f"{cons_stem}.ex17",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Resume para qué sirve el recurso de amparo ante el Tribunal Constitucional. [Summarise what the 'amparo' appeal before the Constitutional Court is for.]",
                        "answer": "El recurso de amparo sirve para proteger a los ciudadanos ante el Tribunal Constitucional frente a la vulneración de sus derechos y libertades fundamentales reconocidos en los artículos 14 a 29 y 30.2 de la Constitución."
                    }
                ],
                "teaches": ["ante-preposicion-juridica"]
            },
            {
                "id": f"{cons_stem}.ex18",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Cómo pueden participar los ciudadanos en la Administración de Justicia según el artículo 125?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "Mediante el ejercicio de la acción popular, la institución del Jurado y los tribunales consuetudinarios y tradicionales.",
                    "No pueden participar de ninguna manera.",
                    "Eligiendo por votación popular a los fiscales cada año."
                ],
                "correct": 0,
                "teaches": ["tener-por-mision-infinitivo"]
            }
        ]
    }

    emit_unit("judicial", "b1-ccse-judicial", "El Poder Judicial", 5, lessons, comb, consolidation)


def build_unit_6():
    lessons = [
        {
            "num": "01",
            "story_suffix": "instituciones",
            "title": "Las instituciones de las comunidades autónomas",
            "theme": "Instituciones Autonómicas y Locales",
            "goal": "Conocer los tres órganos institucionales de toda comunidad autónoma según el artículo 152: Asamblea Legislativa, Consejo de Gobierno y Presidente.",
            "grammar_short": "elegido entre sus miembros",
            "grammar_slug": "elegido-entre-sus-miembros",
            "grammar_title": "Participios de origen parlamentario: «elegido por la Asamblea entre sus miembros»",
            "location": "España, 17 Comunidades Autónomas",
            "words": [
                {"lemma": "el Parlamento autonómico", "translation": "regional parliament / legislative assembly", "pos": "expression"},
                {"lemma": "el Consejo de Gobierno", "translation": "Regional Governing Council (regional cabinet)", "pos": "expression"},
                {"lemma": "el Presidente autonómico", "translation": "President of the Autonomous Community", "pos": "expression"},
                {"lemma": "el Tribunal Superior de Justicia", "translation": "High Court of Justice (in an Autonomous Community)", "pos": "expression"},
                {"lemma": "el consejero", "translation": "regional minister (member of a Consejo de Gobierno)", "pos": "noun"},
                {"lemma": "autogobernarse", "translation": "to govern oneself, exercise self-government", "pos": "verb"},
                {"lemma": "la representación proporcional", "translation": "proportional representation", "pos": "expression"},
                {"lemma": "políticamente responsable", "translation": "politically accountable", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 152.1 de la Constitución describe cómo se forma el gobierno de una comunidad autónoma encadenando participios pasivos con dos preposiciones precisas: *elegido POR la Asamblea ENTRE sus miembros y nombrado POR el Rey*."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Presidente de la comunidad autónoma es elegido por la Asamblea Legislativa entre sus miembros y nombrado por el Rey.", "english": "The President of the autonomous community is elected by the Legislative Assembly from among its members and appointed by the King."},
                        {"spanish": "El Consejo de Gobierno está integrado por el Presidente y los consejeros encargados de áreas como sanidad o educación.", "english": "The Governing Council is composed of the President and the regional ministers in charge of areas such as healthcare or education."},
                        {"spanish": "El Presidente y los miembros del Consejo de Gobierno serán políticamente responsables ante la Asamblea.", "english": "The President and the members of the Governing Council shall be politically accountable before the Assembly."},
                        {"spanish": "Un Tribunal Superior de Justicia culmina la organización judicial en el ámbito territorial de la comunidad autónoma.", "english": "A High Court of Justice culminates the judicial organization within the territorial scope of the autonomous community."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Fíjate en la diferencia de vocabulario: en el Gobierno de España los titulares de cada departamento se llaman *ministros*; en el Consejo de Gobierno de una comunidad autónoma se llaman *consejeros*."
                }
            ],
            "story_summary": "Article 152 sets out the institutional architecture of each Autonomous Community: a Legislative Assembly elected every 4 years by universal suffrage, a Governing Council (with regional 'consejeros'), a President elected by the Assembly and appointed by the King, and a High Court of Justice.",
            "story_paragraphs": [
                "¿Cómo se gobierna por dentro cada una de las diecisiete comunidades autónomas de España? El artículo 152.1 de la Constitución establece un modelo parlamentario semejante al del Estado central, articulado en torno a tres instituciones autonómicas propias.",
                "La primera institución es la Asamblea Legislativa (o Parlamento autonómico), elegida cada cuatro años por sufragio universal con arreglo a un sistema de representación proporcional que asegura la representación de las diversas zonas del territorio.",
                "La segunda institución es el Consejo de Gobierno, que ejerce las funciones ejecutivas y administrativas de la comunidad autónoma y está formado por el Presidente y los «consejeros» (equivalentes autonómicos de los ministros, al frente de las consejerías de Sanidad, Educación, Cultura o Hacienda).",
                "La tercera institución es el Presidente de la Comunidad Autónoma, que es elegido por la Asamblea Legislativa de entre sus miembros y nombrado formalmente por el Rey; al Presidente le corresponde la dirección del Consejo de Gobierno, la suprema representación de la respectiva comunidad y la representación ordinaria del Estado en aquella.",
                "Además, sin perjuicio de la jurisdicción que corresponde al Tribunal Supremo en toda España, en cada comunidad autónoma existe un Tribunal Superior de Justicia (TSJ) que culmina la organización judicial en su ámbito territorial."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuáles son las tres instituciones de autogobierno de una comunidad autónoma según el artículo 152 de la Constitución?",
                    "options": [
                        "La Asamblea Legislativa (Parlamento autonómico), el Consejo de Gobierno y el Presidente",
                        "El Senado, el Consejo de Estado y el Alcalde",
                        "La Diputación, el Juzgado de Paz y el Subdelegado",
                        "El Congreso, el Defensor del Pueblo y el Embajador"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 152.1 dispone que la organización institucional autonómica se basa en una Asamblea Legislativa, un Consejo de Gobierno y un Presidente."
                },
                {
                    "question": "¿Quién elige al Presidente de una comunidad autónoma y quién lo nombra formalmente?",
                    "options": [
                        "Lo elige la Asamblea Legislativa autonómica entre sus miembros y lo nombra el Rey",
                        "Lo elige el Senado y lo nombra el Alcalde",
                        "Lo elige directamente el Tribunal Constitucional",
                        "Lo nombra el Delegado del Gobierno sin votación"
                    ],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 152.1, el Presidente es elegido por la Asamblea entre sus miembros y nombrado por el Rey."
                },
                {
                    "question": "¿Cómo se denominan los miembros del Consejo de Gobierno autonómico que dirigen departamentos como Sanidad o Educación?",
                    "options": ["Consejeros", "Concejales", "Senadores", "Embajadores"],
                    "correctIndex": 0,
                    "explanation": "Los miembros del gobierno autonómico se denominan consejeros (mientras que en los ayuntamientos son concejales y en el Gobierno central son ministros)."
                }
            ],
            "goals": [
                "Name the three self-governing institutions of every Autonomous Community under Article 152: Legislative Assembly, Governing Council, and President.",
                "Explain that the Regional President is elected by the Assembly from among its members and appointed by the King.",
                "Distinguish 'consejeros' (regional cabinet members) from 'ministros' (state cabinet) and 'concejales' (municipal councilors).",
                "Use 'elegido por... entre sus miembros' accurately."
            ],
            "mc1": {
                "q": "¿Quién elige al Presidente de una comunidad autónoma según el artículo 152 de la Constitución?",
                "opts": [
                    "La Asamblea Legislativa (Parlamento) de la comunidad autónoma, de entre sus miembros.",
                    "El Senado en votación secreta.",
                    "El Consejo General del Poder Judicial."
                ]
            },
            "mc2": {
                "q": "¿Cómo se llaman los miembros del Consejo de Gobierno de una comunidad autónoma?",
                "opts": ["Consejeros (junto con el Presidente).", "Concejales.", "Magistrados."]
            },
            "fb": {
                "sentence": "El Presidente de la comunidad autónoma es elegido por la Asamblea ___ sus miembros y nombrado por el Rey. (entre)",
                "answer": "entre",
                "english": "The President of the autonomous community is elected by the Assembly from among its members and appointed by the King."
            },
            "mc3": {
                "q": "¿Qué órgano judicial culmina la organización judicial en el ámbito territorial de cada comunidad autónoma?",
                "opts": ["El Tribunal Superior de Justicia (TSJ).", "El Tribunal de Cuentas.", "El Juzgado de Paz."]
            },
            "sb": {
                "words": ["El", "Consejo", "de", "Gobierno", "ejerce", "las", "funciones", "ejecutivas", "autonómicas."],
                "english": "The Governing Council exercises regional executive functions."
            },
            "dlg": {
                "s1": "Lucía", "s2": "Óscar",
                "q": "¿Ante quién responden políticamente el Presidente y los consejeros de una comunidad autónoma?",
                "opts": [
                    "Responden políticamente ante la Asamblea Legislativa (Parlamento) de su comunidad autónoma.",
                    "Responden únicamente ante los alcaldes de los pueblos vecinos.",
                    "No responden ante ningún parlamento."
                ]
            },
            "listen": {
                "sentence": "La organización institucional autonómica se basa en una Asamblea Legislativa, un Consejo de Gobierno y un Presidente elegido por la Asamblea.",
                "opts": [
                    "Regional institutional organization is based on a Legislative Assembly, a Governing Council, and a President elected by the Assembly.",
                    "Autonomous communities do not have parliaments or executive councils.",
                    "Regional ministers in Spain are called ambassadors."
                ]
            }
        },
        {
            "num": "02",
            "story_suffix": "denominaciones",
            "title": "Denominaciones históricas: Generalitat, Xunta, Junta y Lehendakari",
            "theme": "Instituciones Autonómicas y Locales",
            "goal": "Identificar los nombres históricos de las instituciones autonómicas en el examen CCSE: Generalitat, Xunta, Junta, Gobierno Vasco y Diputación Foral.",
            "grammar_short": "denominarse y conocerse como",
            "grammar_slug": "denominarse-y-conocerse-como",
            "grammar_title": "Introducir nombres propios institucionales: «denominarse», «recibir el nombre de» y «conocerse como»",
            "location": "Cataluña, Comunidad Valenciana, Galicia, País Vasco, Andalucía y Navarra",
            "words": [
                {"lemma": "la Generalitat", "translation": "Generalitat (institutional system of Catalonia and Valencia)", "pos": "noun"},
                {"lemma": "la Xunta de Galicia", "translation": "Xunta de Galicia (regional government of Galicia)", "pos": "expression"},
                {"lemma": "el Lehendakari", "translation": "Lehendakari (President of the Basque Government)", "pos": "noun"},
                {"lemma": "la Junta", "translation": "Junta (regional government in Andalusia, Castile and León, Extremadura, Castile-La Mancha)", "pos": "noun"},
                {"lemma": "la Diputación Foral", "translation": "Foral Deputation (in Navarre and Basque historical territories)", "pos": "expression"},
                {"lemma": "el Parlamento", "translation": "Parliament", "pos": "noun"},
                {"lemma": "la denominación", "translation": "official name, denomination", "pos": "noun"},
                {"lemma": "histórico", "translation": "historic, historical", "pos": "adjective"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 147.2 de la Constitución dispone que los Estatutos de Autonomía deben contener la *denominación de la Comunidad que mejor corresponda a su identidad histórica* y la de sus instituciones propias. Para expresarlo se emplean *denominarse*, *recibir el nombre de* y *conocerse como*."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "En Cataluña y en la Comunitat Valenciana, el conjunto de sus instituciones de autogobierno recibe el nombre histórico de Generalitat.", "english": "In Catalonia and in the Valencian Community, the set of self-governing institutions bears the historical name of Generalitat."},
                        {"spanish": "En Galicia, el órgano ejecutivo autonómico se denomina Xunta de Galicia.", "english": "In Galicia, the regional executive body is called Xunta de Galicia."},
                        {"spanish": "En el País Vasco, el Presidente del Gobierno Vasco (Eusko Jaurlaritza) es conocido como Lehendakari.", "english": "In the Basque Country, the President of the Basque Government (Eusko Jaurlaritza) is known as the Lehendakari."},
                        {"spanish": "En Andalucía, Castilla y León, Castilla-La Mancha y Extremadura, el gobierno autonómico se denomina Junta.", "english": "In Andalusia, Castile and León, Castile-La Mancha, and Extremadura, the regional government is called Junta."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Conocer qué comunidades usan *Generalitat* (Cataluña y Comunidad Valenciana), *Xunta* (Galicia), *Lehendakari* (País Vasco) y *Junta* (Andalucía, Extremadura, Castilla y León, Castilla-La Mancha) es una pregunta muy habitual en el manual oficial CCSE."
                }
            ],
            "story_summary": "Under Article 147.2, Statutes of Autonomy preserve the historical names of regional institutions tested on the CCSE exam: Generalitat (Catalonia and Valencian Community), Xunta de Galicia, Eusko Jaurlaritza / Lehendakari (Basque Country), Junta (Andalusia, Extremadura, Castile and León, Castile-La Mancha), and Diputación Foral (Navarre).",
            "story_paragraphs": [
                "Aunque todas las comunidades autónomas cuentan con una Asamblea Legislativa, un Consejo de Gobierno y un Presidente, el artículo 147.2 de la Constitución permite que cada Estatuto de Autonomía adopte las denominaciones que mejor correspondan a su tradición e identidad histórica.",
                "Así, en Cataluña y en la Comunitat Valenciana, el sistema institucional en que se organiza su autogobierno (Presidente, Gobierno o Consell y Parlamento o Les Corts) recibe el nombre histórico de origen medieval de «Generalitat» (Generalitat de Catalunya y Generalitat Valenciana).",
                "En el noroeste peninsular, el gobierno autonómico de Galicia se denomina oficialmente «Xunta de Galicia», mientras que en el País Vasco (Euskadi) el ejecutivo recibe el nombre de «Gobierno Vasco» o «Eusko Jaurlaritza», y su presidente ostenta la denominación tradicional de «Lehendakari».",
                "Por su parte, en la Comunidad Foral de Navarra el ejecutivo autonómico se denomina «Gobierno de Navarra o Diputación Foral», y en los tres territorios históricos vascos (Álava, Bizkaia y Gipuzkoa) existen también Diputaciones Forales y Juntas Generales.",
                "Finalmente, en cuatro comunidades autónomas —Andalucía, Castilla y León, Castilla-La Mancha y Extremadura— el gobierno regional recibe el nombre de «Junta» (como la Junta de Andalucía o la Junta de Extremadura), mientras que otras emplean «Gobierno» (como el Gobierno de Canarias, de Cantabria, de Aragón o de las Illes Balears) o «Consejo de Gobierno» (como en el Principado de Asturias, la Región de Murcia o la Comunidad de Madrid)."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué dos comunidades autónomas recibe el nombre histórico de «Generalitat» el conjunto de sus instituciones de autogobierno?",
                    "options": [
                        "En Cataluña y en la Comunitat Valenciana",
                        "En Galicia y en Asturias",
                        "En Andalucía y en Extremadura",
                        "En Madrid y en La Rioja"
                    ],
                    "correctIndex": 0,
                    "explanation": "Tanto en Cataluña (Generalitat de Catalunya) como en la Comunitat Valenciana (Generalitat Valenciana) sus instituciones de autogobierno se denominan Generalitat."
                },
                {
                    "question": "¿A qué comunidad autónoma corresponde el gobierno denominado «Xunta» y a cuál el presidente llamado «Lehendakari»?",
                    "options": [
                        "La Xunta corresponde a Galicia y el Lehendakari al País Vasco",
                        "La Xunta corresponde a Aragón y el Lehendakari a Canarias",
                        "Ambos corresponden a la Comunidad de Madrid",
                        "La Xunta corresponde a Murcia y el Lehendakari a Cantabria"
                    ],
                    "correctIndex": 0,
                    "explanation": "La Xunta de Galicia es el gobierno gallego y el Lehendakari preside el Gobierno Vasco (Eusko Jaurlaritza)."
                },
                {
                    "question": "¿Cómo se denomina el gobierno autonómico en Andalucía, Castilla y León, Castilla-La Mancha y Extremadura?",
                    "options": ["Junta (por ejemplo, Junta de Andalucía)", "Cabildo", "Generalitat", "Consell Insular"],
                    "correctIndex": 0,
                    "explanation": "En Andalucía, Castilla y León, Castilla-La Mancha y Extremadura el ejecutivo autonómico se denomina Junta."
                }
            ],
            "goals": [
                "Identify 'Generalitat' as the institutional name in Catalonia and the Valencian Community.",
                "Identify 'Xunta de Galicia' in Galicia and 'Eusko Jaurlaritza / Lehendakari' in the Basque Country.",
                "Recognize 'Junta' as the regional government name in Andalusia, Castile and León, Castile-La Mancha, and Extremadura, and 'Diputación Foral' in Navarre and the Basque territories.",
                "Use 'denominarse' and 'recibir el nombre de' in institutional descriptions."
            ],
            "mc1": {
                "q": "¿Cómo se denomina el órgano de gobierno autonómico de Galicia?",
                "opts": ["Xunta de Galicia.", "Generalitat de Galicia.", "Cabildo de Galicia."]
            },
            "mc2": {
                "q": "¿En qué comunidad autónoma recibe el Presidente del Gobierno autonómico el nombre de Lehendakari?",
                "opts": ["En el País Vasco.", "En el Principado de Asturias.", "En la Región de Murcia."]
            },
            "fb": {
                "sentence": "En Cataluña y en la Comunitat Valenciana, el sistema institucional de autogobierno ___ el nombre de Generalitat. (recibir)",
                "answer": "recibe",
                "english": "In Catalonia and in the Valencian Community, the self-governing institutional system bears the name of Generalitat."
            },
            "mc3": {
                "q": "¿Cuál de las siguientes comunidades autónomas denomina «Junta» a su institución de gobierno?",
                "opts": ["Andalucía (Junta de Andalucía).", "Cataluña.", "Illes Balears."]
            },
            "sb": {
                "words": ["En", "Galicia,", "el", "gobierno", "autonómico", "se", "denomina", "Xunta", "de", "Galicia."],
                "english": "In Galicia, the regional government is called Xunta de Galicia."
            },
            "dlg": {
                "s1": "Nerea", "s2": "Iker",
                "q": "¿En qué documento legal se fijan el nombre oficial de cada comunidad autónoma, su capital y la denominación de sus instituciones?",
                "opts": [
                    "En su respectivo Estatuto de Autonomía, de acuerdo con el artículo 147.2 de la Constitución.",
                    "En un bando municipal del alcalde.",
                    "En el reglamento interno del Tribunal de Cuentas."
                ]
            },
            "listen": {
                "sentence": "Las instituciones de autogobierno se denominan Generalitat en Cataluña y la Comunitat Valenciana, Xunta en Galicia y Junta en Andalucía.",
                "opts": [
                    "Self-governing institutions are called Generalitat in Catalonia and the Valencian Community, Xunta in Galicia, and Junta in Andalusia.",
                    "All autonomous communities are forbidden from using historical institutional names.",
                    "The President of Andalusia is called the Lehendakari."
                ]
            }
        },
        {
            "num": "03",
            "story_suffix": "competencias",
            "title": "Reparto de competencias y financiación autonómica",
            "theme": "Instituciones Autonómicas y Locales",
            "goal": "Diferenciar las competencias exclusivas del Estado (artículo 149) de las competencias autonómicas (artículo 148) y conocer el régimen común y foral de financiación.",
            "grammar_short": "mientras que de contraste",
            "grammar_slug": "mientras-que-contraste",
            "grammar_title": "Contraste de atribuciones territoriales: «mientras que»",
            "location": "España",
            "words": [
                {"lemma": "la competencia exclusiva", "translation": "exclusive competence / jurisdiction", "pos": "expression"},
                {"lemma": "la sanidad", "translation": "public healthcare", "pos": "noun"},
                {"lemma": "la educación", "translation": "education", "pos": "noun"},
                {"lemma": "la asistencia social", "translation": "social welfare / social services", "pos": "expression"},
                {"lemma": "las relaciones internacionales", "translation": "international relations", "pos": "expression"},
                {"lemma": "el régimen foral", "translation": "foral tax / financial regime (Basque Country and Navarre)", "pos": "expression"},
                {"lemma": "el Concierto Económico", "translation": "Economic Agreement (Basque fiscal system)", "pos": "expression"},
                {"lemma": "el Fondo de Compensación Interterritorial", "translation": "Interterritorial Compensation Fund", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "Para comparar qué competencias pertenecen en exclusiva al Estado central (artículo 149) y cuáles han asumido las comunidades autónomas en sus Estatutos (artículo 148), el conector adversativo-comparativo *mientras que* (whereas / while) ofrece la máxima claridad expositiva."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Estado tiene competencia exclusiva sobre defensa y relaciones internacionales, mientras que las comunidades autónomas gestionan la sanidad y la educación.", "english": "The State has exclusive competence over defense and international relations, whereas the autonomous communities manage healthcare and education."},
                        {"spanish": "Quince comunidades autónomas se financian mediante el régimen común, mientras que el País Vasco y Navarra cuentan con un régimen foral propio.", "english": "Fifteen autonomous communities are financed through the common regime, while the Basque Country and Navarre have their own foral regime."},
                        {"spanish": "La nacionalidad y la extranjería corresponden en exclusiva al Estado, mientras que la asistencia social y el urbanismo corresponden a las comunidades autónomas.", "english": "Nationality and immigration belong exclusively to the State, whereas social welfare and urban planning belong to the autonomous communities."},
                        {"spanish": "El Fondo de Compensación Interterritorial corrige desequilibrios económicos, mientras que el principio de solidaridad garantiza la igualdad de derechos.", "english": "The Interterritorial Compensation Fund corrects economic imbalances, while the principle of solidarity guarantees equal rights."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Mientras que* va siempre seguido de indicativo y va precedido de una coma para marcar el contraste entre dos sujetos distintos (*el Estado..., mientras que las comunidades...*)."
                }
            ],
            "story_summary": "Articles 148 and 149 divide competencies between the State (defense, foreign affairs, nationality, immigration, foreign trade) and the Autonomous Communities (healthcare, education, social services, urban planning), while Articles 156-158 and the First Additional Provision regulate the common financing regime and the Basque/Navarrese foral economic regimes.",
            "story_paragraphs": [
                "¿Qué asuntos decide el Estado para toda España y qué servicios gestionan directamente las comunidades autónomas? Ese reparto de responsabilidades se regula en los artículos 148 y 149 de la Constitución y en cada Estatuto de Autonomía.",
                "El artículo 149.1 reserva al Estado la «competencia exclusiva» sobre las materias que vertebran la soberanía y la igualdad de todos los españoles: la nacionalidad, inmigración, emigración y extranjería; las relaciones internacionales; la defensa y las Fuerzas Armadas; la Administración de Justicia; la legislación laboral, mercantil y penal, y el comercio exterior.",
                "Por su parte, a través de sus Estatutos de Autonomía, las diecisiete comunidades autónomas han asumido la gestión directa de los grandes servicios del Estado del bienestar que más influyen en la vida cotidiana: la sanidad pública (hospitales y centros de salud), la educación (colegios, institutos y universidades), la asistencia social, el urbanismo, la vivienda, el transporte intrarregional y el fomento de la cultura y del turismo.",
                "Para financiar estos servicios, la Constitución contempla dos modelos económicos: el «régimen común» (aplicado en quince comunidades autónomas e instrumentado mediante impuestos cedidos, transferencias del Estado y el Fondo de Compensación Interterritorial del artículo 158 para hacer efectivo el principio de solidaridad).",
                "Junto al régimen común, la Disposición Adicional Primera de la Constitución ampara y respeta los derechos históricos de los territorios forales, en virtud de los cuales el País Vasco (mediante el Concierto Económico) y la Comunidad Foral de Navarra (mediante el Convenio Económico) recaudan sus propios impuestos y abonan un cupo o aportación anual al Estado por las competencias no transferidas."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál de las siguientes materias es competencia exclusiva del Estado según el artículo 149.1 de la Constitución?",
                    "options": [
                        "Defensa y Fuerzas Armadas, relaciones internacionales, nacionalidad y extranjería",
                        "La limpieza viaria de los municipios",
                        "El alumbrado público de las calles",
                        "La artesanía local exclusivamente"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 149.1 reserva al Estado en exclusiva la defensa, relaciones internacionales, nacionalidad, inmigración y extranjería."
                },
                {
                    "question": "¿Qué dos grandes servicios públicos cotidianos están transferidos y son gestionados directamente por todas las comunidades autónomas?",
                    "options": ["La sanidad y la educación", "El Ejército y las embajadas", "La emisión de moneda y las aduanas", "La concesión de la nacionalidad española"],
                    "correctIndex": 0,
                    "explanation": "Todas las comunidades autónomas gestionan en su territorio las competencias de sanidad pública y educación."
                },
                {
                    "question": "¿Qué dos comunidades autónomas cuentan con un régimen foral propio de financiación (Concierto y Convenio Económico)?",
                    "options": ["El País Vasco y la Comunidad Foral de Navarra", "Madrid y Cataluña", "Andalucía y Galicia", "Canarias y Baleares"],
                    "correctIndex": 0,
                    "explanation": "El País Vasco (Concierto Económico) y Navarra (Convenio Económico) tienen régimen fiscal y financiero foral amparado por la Constitución."
                }
            ],
            "goals": [
                "Distinguish exclusive State powers under Article 149 (defense, foreign policy, nationality, immigration) from Autonomous Community powers (healthcare, education, social welfare).",
                "Explain the Interterritorial Compensation Fund (Article 158) as the financial instrument of territorial solidarity.",
                "Identify the Basque Country and Navarre as the two Autonomous Communities with a foral financial regime ('Concierto Económico' and 'Convenio Económico').",
                "Use 'mientras que' to contrast State and regional powers."
            ],
            "mc1": {
                "q": "¿A qué administración le corresponde en España la gestión directa de los hospitales públicos (sanidad) y de los colegios e institutos (educación) en cada territorio?",
                "opts": ["A las comunidades autónomas.", "Al Tribunal Constitucional.", "A las embajadas extranjeras."]
            },
            "mc2": {
                "q": "Según el artículo 149 de la Constitución, ¿quién tiene competencia exclusiva en materia de nacionalidad, inmigración, emigración, extranjería y derecho de asilo?",
                "opts": ["El Estado.", "Los ayuntamientos.", "Las diputaciones provinciales."]
            },
            "fb": {
                "sentence": "El Estado tiene competencia exclusiva en relaciones internacionales, ___ que las comunidades autónomas gestionan la sanidad y la educación. (mientras)",
                "answer": "mientras",
                "english": "The State has exclusive competence in international relations, whereas the autonomous communities manage healthcare and education."
            },
            "mc3": {
                "q": "¿Qué dos comunidades autónomas disponen de un régimen foral de financiación (Concierto Económico y Convenio Económico)?",
                "opts": [
                    "El País Vasco y la Comunidad Foral de Navarra.",
                    "Castilla-La Mancha y Extremadura.",
                    "La Región de Murcia y La Rioja."
                ]
            },
            "sb": {
                "words": ["La", "defensa", "y", "las", "relaciones", "internacionales", "son", "competencias", "exclusivas", "del", "Estado."],
                "english": "Defense and international relations are exclusive powers of the State."
            },
            "dlg": {
                "s1": "Cristina", "s2": "Manuel",
                "q": "¿Para qué existe el Fondo de Compensación Interterritorial previsto en el artículo 158 de la Constitución?",
                "opts": [
                    "Para corregir desequilibrios económicos interterritoriales y hacer efectivo el principio constitucional de solidaridad.",
                    "Para financiar únicamente las campañas electorales de los partidos.",
                    "Para pagar las multas de tráfico municipales."
                ]
            },
            "listen": {
                "sentence": "El Estado tiene competencia exclusiva sobre defensa, nacionalidad y relaciones internacionales, mientras que las comunidades autónomas gestionan la sanidad y la educación.",
                "opts": [
                    "The State has exclusive competence over defense, nationality, and international relations, whereas the autonomous communities manage healthcare and education.",
                    "Each municipality grants Spanish citizenship independently.",
                    "Autonomous communities command the Armed Forces."
                ]
            }
        },
        {
            "num": "04",
            "story_suffix": "municipios",
            "title": "El municipio: el Ayuntamiento, el alcalde y los concejales",
            "theme": "Instituciones Autonómicas y Locales",
            "goal": "Comprender el artículo 140 de la Constitución: la autonomía municipal, el Ayuntamiento (alcalde y concejales), las elecciones locales y el padrón municipal.",
            "grammar_short": "integrado por + cargos",
            "grammar_slug": "integrado-por",
            "grammar_title": "Composición de corporaciones locales: «integrado por»",
            "location": "Los más de 8.100 municipios de España",
            "words": [
                {"lemma": "el Ayuntamiento", "translation": "City / Town Council (City Hall)", "pos": "noun"},
                {"lemma": "el alcalde", "translation": "mayor", "pos": "noun"},
                {"lemma": "el concejal", "translation": "city councilor", "pos": "noun"},
                {"lemma": "el vecino", "translation": "resident, local citizen (registered in a municipality)", "pos": "noun"},
                {"lemma": "el padrón municipal", "translation": "municipal register of inhabitants", "pos": "expression"},
                {"lemma": "empadronarse", "translation": "to register as a resident at the Town Hall", "pos": "verb"},
                {"lemma": "la ordenanza municipal", "translation": "municipal ordinance / bylaw", "pos": "expression"},
                {"lemma": "el pleno municipal", "translation": "full municipal council session", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "El artículo 140 de la Constitución describe el gobierno municipal con una estructura clara: *Su gobierno y administración corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales*."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El gobierno y la administración de los municipios corresponde a sus respectivos Ayuntamientos, integrados por los alcaldes y los concejales.", "english": "The government and administration of municipalities belongs to their respective Town Councils, composed of the mayors and councilors."},
                        {"spanish": "Los concejales son elegidos por los vecinos del municipio mediante sufragio universal, igual, libre, directo y secreto cada cuatro años.", "english": "Councilors are elected by the residents of the municipality by universal, equal, free, direct, and secret suffrage every four years."},
                        {"spanish": "Los alcaldes son elegidos por los concejales en el pleno constitutivo o por los vecinos en el régimen de concejo abierto.", "english": "Mayors are elected by the councilors in the constitutive plenary session or by the residents under the open council system."},
                        {"spanish": "Toda persona que viva en España está obligada a inscribirse en el padrón del municipio en el que resida habitualmente.", "english": "Every person living in Spain is required to register in the municipal roll of the municipality where they habitually reside."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda el orden de elección del artículo 140: los **vecinos** eligen en las urnas a los **concejales**, y después los **concejales** eligen al **alcalde** (o alcaldesa)."
                }
            ],
            "story_summary": "Article 140 guarantees the autonomy of Spain's more than 8,100 municipalities, governed by Town Councils (Ayuntamientos) composed of the Mayor (alcalde) and Councilors (concejales), elected every 4 years and responsible for the municipal register ('padrón') and local services.",
            "story_paragraphs": [
                "La administración más cercana a la vida diaria de los ciudadanos es el municipio: en España existen más de 8.130 municipios repartidos por toda la geografía nacional.",
                "El artículo 140 de la Constitución garantiza la autonomía de los municipios y dispone que su gobierno y administración corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales.",
                "¿Cómo se eligen los miembros del Ayuntamiento? Cada cuatro años (el cuarto domingo de mayo) se celebran las elecciones municipales, en las que tienen derecho de sufragio tanto los ciudadanos españoles como los ciudadanos de la Unión Europea residentes y los extranjeros de países con tratado de reciprocidad. Los vecinos eligen mediante sufragio universal a los concejales, y son los concejales quienes, en la sesión constitutiva del pleno municipal, eligen de entre ellos al Alcalde o Alcaldesa (salvo en pequeños pueblos con régimen de «concejo abierto», donde los vecinos lo eligen directamente).",
                "El Ayuntamiento presta servicios esenciales que dependen del tamaño de la población: alumbrado público, recogida de residuos, limpieza viaria, abastecimiento de agua potable, alcantarillado, parques y jardines, policía local, transporte urbano y centros culturales y deportivos.",
                "Además, corresponde al Ayuntamiento gestionar el «padrón municipal de habitantes»: el registro administrativo donde constan todos los vecinos de un municipio, cuya inscripción (el empadronamiento) acredita la residencia en España y permite acceder a la tarjeta sanitaria, la escolarización de los hijos y los servicios sociales."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 140 de la Constitución, ¿a qué órgano corresponde el gobierno y la administración de los municipios y quiénes lo integran?",
                    "options": [
                        "Corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales",
                        "Corresponde a las Diputaciones Forales, integradas por senadores",
                        "Corresponde al Consejo de Estado, integrado por ministros",
                        "Corresponde al Tribunal Superior de Justicia"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 140 establece que el gobierno y administración de los municipios corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales."
                },
                {
                    "question": "¿Cómo se elige con carácter general al Alcalde o Alcaldesa de un municipio en España?",
                    "options": [
                        "Los vecinos eligen a los concejales en las elecciones municipales, y los concejales eligen al Alcalde",
                        "Lo nombra directamente el Rey por nueve años",
                        "Lo designa el Delegado del Gobierno sin elecciones",
                        "Accede al cargo mediante oposiciones"
                    ],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 140, los concejales son elegidos por los vecinos mediante sufragio universal y los alcaldes son elegidos por los concejales (o por los vecinos en concejo abierto)."
                },
                {
                    "question": "¿Cómo se llama el registro administrativo del Ayuntamiento donde deben inscribirse todas las personas que residen habitualmente en un municipio?",
                    "options": ["El padrón municipal de habitantes", "El Boletín Oficial del Estado", "El Registro Mercantil", "El Censo del Senado"],
                    "correctIndex": 0,
                    "explanation": "El padrón municipal es el registro administrativo gestionado por cada Ayuntamiento donde constan los vecinos del municipio."
                }
            ],
            "goals": [
                "State that the government and administration of municipalities belongs to their Town Councils ('Ayuntamientos'), integrated by Mayors ('alcaldes') and Councilors ('concejales') (Article 140).",
                "Explain how councilors are elected by residents ('vecinos') every 4 years and how mayors are elected by councilors.",
                "Identify the municipal register ('padrón municipal') and basic local services managed by Town Councils.",
                "Use 'integrado por' to describe the composition of collegiate municipal bodies."
            ],
            "mc1": {
                "q": "¿Qué institución gobierna y administra cada municipio en España?",
                "opts": ["El Ayuntamiento (integrado por el alcalde y los concejales).", "La Subdelegación del Gobierno.", "El Parlamento autonómico."]
            },
            "mc2": {
                "q": "Según el artículo 140 de la Constitución, ¿quiénes eligen a los concejales y quiénes eligen al alcalde?",
                "opts": [
                    "Los vecinos eligen a los concejales por sufragio universal, y los concejales (o los vecinos en concejo abierto) eligen al alcalde.",
                    "El Presidente de la comunidad autónoma nombra tanto al alcalde como a los concejales.",
                    "El Tribunal Supremo elige a los alcaldes cada nueve años."
                ]
            },
            "fb": {
                "sentence": "Los Ayuntamientos están ___ por los alcaldes y los concejales elegidos democráticamente. (integrado, masculino plural)",
                "answer": "integrados",
                "english": "Town Councils are composed of democratically elected mayors and councilors."
            },
            "mc3": {
                "q": "¿Ante qué administración debe realizarse el trámite de empadronamiento al fijar la residencia habitual en una localidad de España?",
                "opts": ["En el Ayuntamiento del municipio correspondiente.", "En el Tribunal Constitucional.", "En el Congreso de los Diputados."]
            },
            "sb": {
                "words": ["El", "gobierno", "municipal", "corresponde", "al", "Ayuntamiento,", "integrado", "por", "el", "alcalde", "y", "los", "concejales."],
                "english": "Municipal government belongs to the Town Council, composed of the mayor and the councilors."
            },
            "dlg": {
                "s1": "Marta", "s2": "Javier",
                "q": "¿Pueden votar en las elecciones municipales en España los ciudadanos de otros países de la Unión Europea residentes en el municipio?",
                "opts": [
                    "Sí, desde la reforma constitucional de 1992 gozan de sufragio activo y pasivo en las elecciones municipales.",
                    "No, en las elecciones municipales no puede votar ningún residente europeo.",
                    "Solo pueden votar si son senadores."
                ]
            },
            "listen": {
                "sentence": "El gobierno y administración de los municipios corresponde a sus respectivos Ayuntamientos, integrados por los alcaldes y los concejales.",
                "opts": [
                    "The government and administration of municipalities belongs to their respective Town Councils, composed of the mayors and councilors.",
                    "Mayors are appointed by the Council of State for nine years.",
                    "The municipal register is managed by the Constitutional Court."
                ]
            }
        },
        {
            "num": "05",
            "story_suffix": "provincias",
            "title": "La provincia, las Diputaciones, los Cabildos y Ceuta y Melilla",
            "theme": "Instituciones Autonómicas y Locales",
            "goal": "Conocer las 50 provincias españolas, las Diputaciones Provinciales (artículo 141), los Cabildos Insulares en Canarias, los Consejos Insulares en Baleares y las Ciudades Autónomas.",
            "grammar_short": "contar con + institución",
            "grammar_slug": "carecer-de-o-contar-con",
            "grammar_title": "Dotación institucional: «contar con» en geografía política",
            "location": "50 provincias, Canarias, Illes Balears, Ceuta y Melilla",
            "words": [
                {"lemma": "la Diputación Provincial", "translation": "Provincial Council / Deputation", "pos": "expression"},
                {"lemma": "uniprovincial", "translation": "single-province (Autonomous Community)", "pos": "adjective"},
                {"lemma": "pluriprovincial", "translation": "multi-province (Autonomous Community)", "pos": "adjective"},
                {"lemma": "el Cabildo Insular", "translation": "Island Council (in the Canary Islands)", "pos": "expression"},
                {"lemma": "el Consejo Insular", "translation": "Island Council (in the Balearic Islands)", "pos": "expression"},
                {"lemma": "la ciudad autónoma", "translation": "autonomous city (Ceuta and Melilla)", "pos": "expression"},
                {"lemma": "el archipiélago", "translation": "archipelago", "pos": "noun"},
                {"lemma": "contar con", "translation": "to have, possess (an institution)", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "Para indicar qué órgano de gobierno propio posee cada isla, provincia o ciudad autónoma, el español institucional emplea con gran frecuencia el verbo preposicional *contar con* (*en los archipiélagos, cada isla cuenta con su propia administración*)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "En Canarias, cada una de las siete islas cuenta con su propio órgano de gobierno llamado Cabildo Insular.", "english": "In the Canary Islands, each of the seven islands has its own governing body called a Cabildo Insular."},
                        {"spanish": "En las Illes Balears, cada isla cuenta con un Consejo Insular (Consell Insular).", "english": "In the Balearic Islands, each island has an Island Council (Consell Insular)."},
                        {"spanish": "España cuenta con cincuenta provincias, cuyas administraciones propias en las comunidades pluriprovinciales son las Diputaciones Provinciales.", "english": "Spain has fifty provinces, whose governing bodies in multi-province communities are the Provincial Councils."},
                        {"spanish": "Ceuta y Melilla cuentan con sendos Estatutos de Ciudad Autónoma aprobados por ley orgánica en 1995.", "english": "Ceuta and Melilla each have Autonomous City Statutes approved by organic law in 1995."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Esta distinción es un clásico del examen CCSE: en **Canarias** los gobiernos insulares se llaman **Cabildos Insulares**; en **Baleares** se llaman **Consejos Insulares** (*Consells Insulars*)."
                }
            ],
            "story_summary": "Article 141 defines the 50 provinces of Spain governed by Provincial Councils ('Diputaciones Provinciales' in multi-province communities), while single-province communities integrate provincial duties, Canary islands are governed by 'Cabildos Insulares', Balearic islands by 'Consejos Insulares', and Ceuta and Melilla as Autonomous Cities.",
            "story_paragraphs": [
                "Entre el municipio y la comunidad autónoma se sitúa el segundo nivel de la administración local española: la provincia. En total, España está dividida en 50 provincias.",
                "El artículo 141.1 de la Constitución define la provincia como una entidad local con personalidad jurídica propia, determinada por la agrupación de municipios, y añade que cualquier alteración de los límites provinciales habrá de ser aprobada por las Cortes Generales mediante ley orgánica.",
                "El gobierno y la administración autónoma de las provincias están encomendados a las «Diputaciones Provinciales» (cuyos diputados provinciales se eligen de forma indirecta entre los concejales de los ayuntamientos de la provincia), cuya función principal es asistir y cooperar con los municipios de menor población para garantizar que todos los vecinos reciban servicios públicos de calidad.",
                "En las siete comunidades autónomas «uniprovinciales» (Asturias, Cantabria, La Rioja, Navarra, Madrid, Región de Murcia e Illes Balears), no existe Diputación Provincial separada porque sus competencias las asume directamente el gobierno de la comunidad autónoma.",
                "Por último, el artículo 141.4 establece que en los archipiélagos las islas tendrán además su administración propia en forma de «Cabildos Insulares» en Canarias y «Consejos Insulares» (*Consells Insulars*) en las Illes Balears; mientras que en el norte de África las dos ciudades autónomas de Ceuta y Melilla cuentan cada una con su Asamblea y su Presidente-Alcalde."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuántas provincias existen en total en España y qué institución gobierna cada provincia en las comunidades pluriprovinciales?",
                    "options": [
                        "Existen 50 provincias y las gobiernan las Diputaciones Provinciales",
                        "Existen 17 provincias y las gobierna el Senado",
                        "Existen 100 provincias sin administración propia",
                        "Existen 25 provincias gobernadas por embajadores"
                    ],
                    "correctIndex": 0,
                    "explanation": "España se divide en 50 provincias, cuyo gobierno y administración corresponde a las Diputaciones Provinciales."
                },
                {
                    "question": "¿Cómo se denominan los órganos de gobierno insular de cada isla en Canarias y cómo se denominan en las Illes Balears?",
                    "options": [
                        "En Canarias se llaman Cabildos Insulares y en las Illes Balears se llaman Consejos Insulares (Consells Insulars)",
                        "En Canarias se llaman Consejos y en Baleares se llaman Cabildos",
                        "En ambos archipiélagos se llaman Diputaciones Forales",
                        "En ambos se llaman Xuntas Insulares"
                    ],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 141.4 y los respectivos Estatutos, en Canarias son Cabildos Insulares y en Baleares son Consejos Insulares."
                },
                {
                    "question": "¿Cuáles son las dos ciudades autónomas de España situadas en el norte de África?",
                    "options": ["Ceuta y Melilla", "Tenerife y Gran Canaria", "Ibiza y Menorca", "Cádiz y Málaga"],
                    "correctIndex": 0,
                    "explanation": "Ceuta y Melilla son las dos ciudades autónomas de España, con Estatutos aprobados en 1995."
                }
            ],
            "goals": [
                "State that Spain is divided into 50 provinces governed by Provincial Councils ('Diputaciones Provinciales') under Article 141.",
                "Identify the 7 single-province Autonomous Communities where regional institutions assume provincial powers.",
                "Distinguish 'Cabildos Insulares' (Canary Islands) from 'Consejos Insulares' (Balearic Islands) and identify Ceuta and Melilla as Autonomous Cities.",
                "Use 'contar con' to describe territorial and island governance."
            ],
            "mc1": {
                "q": "¿Cómo se llaman los órganos de gobierno propios de cada una de las islas en la comunidad autónoma de Canarias?",
                "opts": ["Cabildos Insulares.", "Consejos Insulares.", "Diputaciones Forales."]
            },
            "mc2": {
                "q": "¿Cómo se llaman los órganos de gobierno propios de cada isla (Mallorca, Menorca, Ibiza y Formentera) en las Illes Balears?",
                "opts": ["Consejos Insulares (Consells Insulars).", "Cabildos Insulares.", "Juntas Generales."]
            },
            "fb": {
                "sentence": "En Canarias, cada isla ___ con su propia administración en forma de Cabildo Insular. (contar)",
                "answer": "cuenta",
                "english": "In the Canary Islands, each island has its own administration in the form of an Island Council."
            },
            "mc3": {
                "q": "¿A qué institución están encomendados el gobierno y la administración autónoma de las provincias según el artículo 141.2 de la Constitución?",
                "opts": ["A las Diputaciones Provinciales (u otras corporaciones de carácter representativo).", "Al Tribunal de Cuentas.", "Al Consejo de Estado."]
            },
            "sb": {
                "words": ["España", "cuenta", "con", "cincuenta", "provincias,", "diecisiete", "comunidades", "y", "dos", "ciudades", "autónomas."],
                "english": "Spain has fifty provinces, seventeen communities, and two autonomous cities."
            },
            "dlg": {
                "s1": "Clara", "s2": "Hugo",
                "q": "¿Por qué comunidades como Madrid, Asturias, Cantabria, La Rioja o Murcia no tienen una Diputación Provincial separada?",
                "opts": [
                    "Porque son comunidades autónomas uniprovinciales y sus competencias provinciales quedan integradas en el gobierno de la comunidad autónoma.",
                    "Porque no son provincias españolas.",
                    "Porque dependen de la Diputación de otra región."
                ]
            },
            "listen": {
                "sentence": "En los archipiélagos, las islas cuentan con su administración propia en forma de Cabildos Insulares en Canarias y Consejos Insulares en Baleares.",
                "opts": [
                    "In the archipelagos, the islands have their own administration in the form of Island Cabildos in the Canaries and Island Councils in the Balearics.",
                    "Spain has thirty provinces and four autonomous cities.",
                    "Canary islands are governed by Consejos Insulares."
                ]
            }
        }
    ]

    comb = {
        "title": "Las Instituciones Autonómicas y Locales",
        "summary": "Comprehensive CCSE guide to Spain's regional and local institutions: the Legislative Assembly, Governing Council, and President of each Autonomous Community (Article 152), historical institutional names (Generalitat, Xunta, Junta, Lehendakari), competency sharing and common/foral financing, Town Councils (Ayuntamientos, mayors, councilors, and 'padrón'), the 50 provinces (Diputaciones), Cabildos, Consejos Insulares, and Ceuta and Melilla.",
        "paragraphs": [
            "Según el artículo 152 de la Constitución, la organización institucional de cada comunidad autónoma se basa en una Asamblea Legislativa (Parlamento) elegida cada cuatro años, un Consejo de Gobierno (formado por el Presidente y los consejeros) y un Presidente elegido por la Asamblea entre sus miembros y nombrado por el Rey, además de un Tribunal Superior de Justicia.",
            "De acuerdo con su identidad histórica, las instituciones autonómicas reciben nombres propios como Generalitat (en Cataluña y la Comunitat Valenciana), Xunta de Galicia (en Galicia), Gobierno Vasco presidido por el Lehendakari (en el País Vasco), Diputación Foral (en Navarra) y Junta (en Andalucía, Castilla y León, Castilla-La Mancha y Extremadura).",
            "El Estado conserva competencias exclusivas sobre defensa, relaciones internacionales, nacionalidad y extranjería (artículo 149), mientras que las comunidades autónomas gestionan la sanidad, la educación y los servicios sociales, financiándose 15 de ellas por el régimen común y el País Vasco y Navarra por el régimen foral (Concierto y Convenio Económico).",
            "En el ámbito local, el artículo 140 garantiza la autonomía de los más de 8.100 municipios, gobernados por sus Ayuntamientos (integrados por el alcalde y los concejales elegidos por los vecinos cada cuatro años) y encargados del padrón municipal y los servicios urbanos.",
            "Finalmente, las 50 provincias cuentan con Diputaciones Provinciales en las comunidades pluriprovinciales, las islas cuentan con Cabildos Insulares en Canarias y Consejos Insulares en las Illes Balears, y Ceuta y Melilla se rigen por sus Estatutos de Ciudad Autónoma."
        ],
        "comp_questions": [
            {
                "question": "¿Cuáles son las tres instituciones de autogobierno de una comunidad autónoma y cómo se llaman los titulares de los departamentos de su gobierno?",
                "options": [
                    "Asamblea Legislativa, Consejo de Gobierno y Presidente; los titulares de los departamentos se llaman consejeros",
                    "Ayuntamiento, Diputación y Cabildo; sus miembros se llaman concejales",
                    "Senado, Consejo de Estado y Defensor; sus miembros se llaman ministros",
                    "Tribunal Supremo, Fiscalía y Jurado"
                ],
                "correctIndex": 0,
                "explanation": "Toda comunidad autónoma tiene Asamblea Legislativa, Consejo de Gobierno (integrado por el Presidente y los consejeros) y Presidente."
            },
            {
                "question": "¿Qué diferencia hay entre el gobierno de un municipio, el de una provincia y el de las islas en Canarias y Baleares?",
                "options": [
                    "El municipio lo gobierna el Ayuntamiento (alcalde y concejales), la provincia la Diputación Provincial, las islas de Canarias los Cabildos Insulares y las de Baleares los Consejos Insulares",
                    "Todos los municipios y las islas están gobernados por el Consejo de Estado",
                    "En Canarias existen Consejos Insulares y en Baleares existen Cabildos Insulares",
                    "Los alcaldes gobiernan las provincias sin concejales"
                ],
                "correctIndex": 0,
                "explanation": "Cada entidad local tiene su órgano propio: Ayuntamiento (municipio), Diputación (provincia), Cabildo Insular (Canarias) y Consejo Insular (Baleares)."
            },
            {
                "question": "¿En qué comunidades autónomas se denominan sus instituciones «Generalitat», «Xunta» y «Lehendakari»?",
                "options": [
                    "Generalitat en Cataluña y Comunitat Valenciana, Xunta en Galicia y Lehendakari en el País Vasco",
                    "Generalitat en Galicia, Xunta en Andalucía y Lehendakari en Madrid",
                    "Generalitat en Navarra y Xunta en Canarias",
                    "Lehendakari en Extremadura y Xunta en Baleares"
                ],
                "correctIndex": 0,
                "explanation": "Generalitat corresponde a Cataluña y Comunitat Valenciana; Xunta a Galicia; Lehendakari al Presidente del Gobierno Vasco."
            }
        ]
    }

    cons_stem = "b1-autonomias-consolidation"
    consolidation = {
        "title": "Repaso y Simulacro: Instituciones Autonómicas y Locales",
        "goal": "Consolidar las instituciones autonómicas, sus denominaciones históricas, el reparto de competencias, los Ayuntamientos, las Diputaciones y los Cabildos y Consejos Insulares.",
        "grammar": "Consolidación de estructuras territoriales y locales",
        "goals": [
            "Consolidate CCSE exam facts on the Legislative Assembly, Governing Council ('consejeros'), and Regional President (Article 152).",
            "Review historical institutional names: Generalitat, Xunta de Galicia, Lehendakari, Junta, and Diputación Foral.",
            "Verify mastery of State vs. regional powers, common vs. foral financing, Town Councils ('Ayuntamientos', 'alcalde', 'concejales', 'padrón'), and provincial/island councils ('Diputaciones', 'Cabildos Insulares', 'Consejos Insulares').",
            "Practice 'elegido entre sus miembros', 'denominarse', 'mientras que', 'integrado por', and 'contar con'."
        ],
        "exercises": [
            {
                "id": f"{cons_stem}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el Consejo de Gobierno", "Regional Governing Council (cabinet of 'consejeros')"],
                    ["la Generalitat", "Generalitat (Catalonia and Valencian Community)"],
                    ["la Xunta de Galicia", "regional government of Galicia"],
                    ["el Lehendakari", "President of the Basque Government"],
                    ["el Ayuntamiento", "Town Council (mayor and councilors)"],
                    ["el padrón municipal", "municipal register of inhabitants"],
                    ["el Cabildo Insular", "Island Council in the Canary Islands"],
                    ["el Consejo Insular", "Island Council in the Balearic Islands"]
                ],
                "teaches": ["denominarse-y-conocerse-como"]
            },
            {
                "id": f"{cons_stem}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración describe correctamente la elección del Presidente de una comunidad autónoma?",
                "options": [
                    "El Presidente es elegido por la Asamblea Legislativa entre sus miembros y nombrado por el Rey.",
                    "El Presidente es elegido entre el Rey por la Asamblea Legislativa.",
                    "El Presidente es elegido para los alcaldes sin la Asamblea."
                ],
                "correct": 0,
                "teaches": ["elegido-entre-sus-miembros"]
            },
            {
                "id": f"{cons_stem}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué conector permite contrastar las competencias exclusivas del Estado con las competencias autonómicas?",
                "options": [
                    "El Estado gestiona la defensa y las relaciones internacionales, mientras que las comunidades autónomas gestionan la sanidad y la educación.",
                    "El Estado gestiona la defensa, a menos que las comunidades gestionan la sanidad.",
                    "El Estado gestiona la defensa, para que las comunidades gestionan la educación."
                ],
                "correct": 0,
                "teaches": ["mientras-que-contraste"]
            },
            {
                "id": f"{cons_stem}.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración describe con exactitud la composición del Ayuntamiento según el artículo 140?",
                "options": [
                    "El gobierno municipal corresponde al Ayuntamiento, integrado por el alcalde y los concejales.",
                    "El gobierno municipal corresponde al Ayuntamiento, integrando de los consejeros.",
                    "El gobierno municipal corresponde al Ayuntamiento, compuesto hacia los senadores."
                ],
                "correct": 0,
                "teaches": ["integrado-por"]
            },
            {
                "id": f"{cons_stem}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué verbo preposicional expresa qué administración insular posee cada isla en Canarias y Baleares?",
                "options": [
                    "Cada isla de Canarias cuenta con un Cabildo Insular y cada isla de Baleares cuenta con un Consejo Insular.",
                    "Cada isla de Canarias carece con un Cabildo Insular.",
                    "Cada isla de Canarias consiste a un Cabildo Insular."
                ],
                "correct": 0,
                "teaches": ["carecer-de-o-contar-con"]
            },
            {
                "id": f"{cons_stem}.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En Galicia, el órgano ejecutivo de la comunidad autónoma se ___ Xunta de Galicia. (denominar)",
                "answer": "denomina",
                "teaches": ["denominarse-y-conocerse-como"],
                "english": "In Galicia, the executive body of the autonomous community is called Xunta de Galicia."
            },
            {
                "id": f"{cons_stem}.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los Ayuntamientos están ___ por los alcaldes y los concejales. (integrado, masculino plural)",
                "answer": "integrados",
                "teaches": ["integrado-por"],
                "english": "Town Councils are composed of mayors and councilors."
            },
            {
                "id": f"{cons_stem}.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En las Illes Balears, cada isla ___ con su propio Consejo Insular. (contar)",
                "answer": "cuenta",
                "teaches": ["carecer-de-o-contar-con"],
                "english": "In the Balearic Islands, each island has its own Island Council."
            },
            {
                "id": f"{cons_stem}.ex09",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "concejales", "son", "elegidos", "por", "los", "vecinos", "del", "municipio."],
                "solution": ["Los", "concejales", "son", "elegidos", "por", "los", "vecinos", "del", "municipio."],
                "english": "The councilors are elected by the residents of the municipality.",
                "teaches": ["integrado-por"]
            },
            {
                "id": f"{cons_stem}.ex10",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Los vecinos del municipio votan en las elecciones municipales cada cuatro años para elegir a los concejales. [The residents of the municipality vote in municipal elections every four years to elect the councilors.]",
                    "Una vez constituido el pleno del Ayuntamiento, los concejales eligen de entre ellos al alcalde o alcaldesa. [Once the plenary of the Town Council is constituted, the councilors elect the mayor from among themselves.]",
                    "A partir de ese momento, el Ayuntamiento dirige la administración municipal y los servicios locales. [From that moment on, the Town Council directs the municipal administration and local services.]"
                ],
                "solution": [0, 1, 2],
                "teaches": ["integrado-por"]
            },
            {
                "id": f"{cons_stem}.ex11",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Qué diferencia hay entre los Cabildos Insulares y los Consejos Insulares?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "Los Cabildos Insulares son los órganos de gobierno de cada isla en Canarias, mientras que los Consejos Insulares (Consells Insulars) son los de cada isla en las Illes Balears.",
                    "Los Cabildos Insulares están en Galicia y los Consejos Insulares están en Madrid.",
                    "No hay diferencia: ambos son tribunales de justicia."
                ],
                "correct": 0,
                "teaches": ["carecer-de-o-contar-con"]
            },
            {
                "id": f"{cons_stem}.ex12",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "El Presidente de la comunidad autónoma es elegido por la Asamblea entre sus miembros y nombrado por el Rey.",
                "options": [
                    "The President of the autonomous community is elected by the Assembly from among its members and appointed by the King.",
                    "The President of the autonomous community is appointed by the Mayor of Madrid.",
                    "Autonomous communities do not have legislative assemblies."
                ],
                "correct": 0,
                "teaches": ["elegido-entre-sus-miembros"]
            },
            {
                "id": f"{cons_stem}.ex13",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "Toda persona que viva en España debe inscribirse en el padrón del Ayuntamiento del municipio en el que resida habitualmente.",
                "options": [
                    "Every person living in Spain must register in the municipal roll of the Town Council where they habitually reside.",
                    "Registration in the municipal roll is only for members of the Senate.",
                    "Provincial Councils manage foreign embassies."
                ],
                "correct": 0,
                "teaches": ["integrado-por"]
            },
            {
                "id": f"{cons_stem}.ex14",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los Ayuntamientos están integrados por los alcaldes y los concejales.",
                "teaches": ["integrado-por"],
                "english": "Town Councils are composed of the mayors and the councilors."
            },
            {
                "id": f"{cons_stem}.ex15",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica cuáles son las tres instituciones de autogobierno de una comunidad autónoma según el artículo 152. [Explain what the three self-governing institutions of an autonomous community are under Article 152.]",
                        "answer": "Las tres instituciones de una comunidad autónoma son la Asamblea Legislativa (Parlamento), el Consejo de Gobierno (formado por el Presidente y los consejeros) y el Presidente."
                    }
                ],
                "teaches": ["elegido-entre-sus-miembros"]
            },
            {
                "id": f"{cons_stem}.ex16",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Indica dónde reciben las instituciones autonómicas el nombre de Generalitat, dónde el de Xunta y dónde el de Lehendakari. [State where regional institutions are called Generalitat, where Xunta, and where Lehendakari.]",
                        "answer": "Se denominan Generalitat en Cataluña y en la Comunitat Valenciana, Xunta de Galicia en Galicia y Lehendakari al Presidente del Gobierno Vasco en el País Vasco."
                    }
                ],
                "teaches": ["denominarse-y-conocerse-como"]
            },
            {
                "id": f"{cons_stem}.ex17",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Resume cómo se gobiernan los municipios, las provincias y las islas de Canarias y Baleares. [Summarise how municipalities, provinces, and the islands of the Canaries and Balearics are governed.]",
                        "answer": "Los municipios se gobiernan por los Ayuntamientos (alcaldes y concejales), las provincias por las Diputaciones Provinciales, las islas de Canarias por los Cabildos Insulares y las islas de Baleares por los Consejos Insulares."
                    }
                ],
                "teaches": ["carecer-de-o-contar-con"]
            },
            {
                "id": f"{cons_stem}.ex18",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Qué comunidades autónomas recaudan sus propios impuestos mediante el régimen foral de Concierto o Convenio Económico?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "El País Vasco (mediante el Concierto Económico) y la Comunidad Foral de Navarra (mediante el Convenio Económico).",
                    "Todas las comunidades autónomas uniprovinciales.",
                    "Únicamente las ciudades autónomas de Ceuta y Melilla."
                ],
                "correct": 0,
                "teaches": ["mientras-que-contraste"]
            }
        ]
    }

    emit_unit("autonomias", "b1-ccse-autonomias-inst", "Las Instituciones Autonómicas", 6, lessons, comb, consolidation)


if __name__ == "__main__":
    build_unit_4()
    build_unit_5()
    build_unit_6()
