#!/usr/bin/env python3
"""
Generate Spain Citizenship (CCSE) B1 Units 7, 8, and 9 to the full B1 standard:
  - Unit 7: Elecciones y Participación Ciudadana (slug: participacion, legacy: b1-ccse-participacion)
  - Unit 8: Fuerzas Armadas y Cuerpos de Seguridad (slug: seguridad, legacy: b1-ccse-fuerzas-seguridad)
  - Unit 9: España en la Unión Europea (slug: unioneuropea, legacy: b1-ccse-union-europea)
"""

from generate_es_b1_ccse_unit2_3 import emit_unit

UNIT_7 = {
    "slug": "participacion",
    "legacy_prefix": "b1-ccse-participacion",
    "unit_title": "Elecciones y Participación Ciudadana",
    "order": 7,
    "unit_summary": "Complete CCSE guide to Elections and Citizen Participation in Spain: universal suffrage at 18, types of elections (general, autonomic, municipal, European), the D'Hondt proportional system, political parties and trade unions, and the Popular Legislative Initiative (500,000 signatures).",
    "unit_paragraphs": [],
    "unit_questions": [],
    "lessons": [
        {
            "num": "01",
            "story_slug": "sufragio",
            "title": "El derecho de sufragio: libre, igual, directo y secreto",
            "goal": "Understand the constitutional rules of voting in Spain (Article 23 and Article 68): universal suffrage from age 18, voluntary voting, and the difference between active and passive suffrage.",
            "grammar_slug": "tener-derecho-a-participar",
            "grammar_title": "Expresar derechos políticos: 'tener derecho a + infinitivo' y 'por medio de'",
            "grammar_summary": "Using 'tener derecho a + infinitivo' and 'por medio de representantes' to express democratic participation.",
            "grammar_text": "Article 23 of the Spanish Constitution recognizes the fundamental right of citizens to participate in public affairs ('tener derecho a participar en los asuntos públicos'), either directly or through freely elected representatives ('directamente o por medio de representantes'). In Spanish electoral law, 'sufragio activo' is the right to vote, whereas 'sufragio pasivo' is the right to stand as a candidate and be elected.",
            "grammar_examples": [
                {"spanish": "Los ciudadanos tienen derecho a participar en los asuntos públicos por medio de representantes.", "english": "Citizens have the right to participate in public affairs through representatives."},
                {"spanish": "El sufragio es universal, libre, igual, directo y secreto en toda España.", "english": "Suffrage is universal, free, equal, direct, and secret throughout Spain."},
                {"spanish": "En España nadie puede ser obligado a declarar el sentido de su voto.", "english": "In Spain nobody can be forced to declare how they voted."}
            ],
            "grammar_tip": "For the CCSE exam, remember: voting in Spain is a constitutional right ('un derecho'), NOT a legal obligation ('no es obligatorio'), and the voting age is 18.",
            "story_title": "El primer domingo de urna",
            "story_summary": "On election Sunday in a Madrid public school, eighteen-year-old Alejandro casts his first ballot while learning how polling stations are formed by ordinary citizens chosen by public lottery.",
            "story_location": "Madrid, Colegio Público",
            "story_paragraphs": [
                "A las nueve en punto de un domingo electoral, las puertas del colegio público del barrio se abren para recibir a los votantes. Alejandro acaba de cumplir dieciocho años y acude por primera vez con su Documento Nacional de Identidad en la mano.",
                "En España, el artículo 23 de la Constitución garantiza que todos los ciudadanos mayores de edad tienen derecho a participar en los asuntos públicos mediante sufragio universal, libre, igual, directo y secreto.",
                "Detrás de las urnas transparentes se sientan el presidente y los dos vocales de la mesa electoral. No son políticos ni funcionarios profesionales, sino vecinos elegidos por sorteo público entre los electores menores de setenta años que saben leer y escribir.",
                "Alejandro entra en la cabina para garantizar el secreto de su voto, introduce la papeleta blanca para el Congreso en su sobre y la papeleta sepia para el Senado en el suyo. A diferencia de otros países, en España votar es un derecho libre y nunca una obligación sancionable.",
                "Cuando el presidente de la mesa pronuncia las palabras tradicionales —«Vota»— y el sobre cae en la urna, Alejandro comprende que cada ciudadano ejerce tanto el sufragio activo al elegir como el sufragio pasivo cuando decide presentarse como candidato."
            ],
            "comp_questions": [
                {
                    "question": "¿A partir de qué edad tienen derecho a votar los ciudadanos españoles en las elecciones?",
                    "options": ["A partir de los 18 años.", "A partir de los 16 años.", "A partir de los 21 años."],
                    "correctIndex": 0,
                    "explanation": "En España la mayoría de edad y el derecho de sufragio universal comienzan a los 18 años."
                },
                {
                    "question": "¿Cómo se eligen el presidente y los vocales que forman una mesa electoral en España?",
                    "options": ["Por sorteo público entre los ciudadanos censados en esa sección.", "Por nombramiento directo de los partidos políticos.", "Por oposición entre jueces y secretarios judiciales."],
                    "correctIndex": 0,
                    "explanation": "Los miembros de las mesas electorales (un presidente y dos vocales) se designan mediante sorteo público realizado por cada ayuntamiento."
                },
                {
                    "question": "¿Qué características tiene el voto según la Constitución Española?",
                    "options": ["Es universal, libre, igual, directo y secreto.", "Es obligatorio, censitario y público.", "Es indirecto a través de compromisarios provinciales."],
                    "correctIndex": 0,
                    "explanation": "La Constitución establece que el sufragio es universal, libre, igual, directo y secreto."
                }
            ],
            "vocab": [
                {"lemma": "sufragio", "pos": "noun", "translation": "suffrage / right to vote", "ex_es": "El sufragio universal permite votar a todos los ciudadanos mayores de dieciocho años.", "ex_en": "Universal suffrage allows all citizens over eighteen to vote."},
                {"lemma": "urna", "pos": "noun", "translation": "ballot box", "ex_es": "Los electores depositan su sobre cerrado dentro de la urna transparente.", "ex_en": "Voters deposit their sealed envelope inside the transparent ballot box."},
                {"lemma": "papeleta", "pos": "noun", "translation": "ballot paper", "ex_es": "La papeleta blanca corresponde a la elección de los diputados del Congreso.", "ex_en": "The white ballot paper corresponds to the election of Congress deputies."},
                {"lemma": "mesa electoral", "pos": "noun", "translation": "polling station board", "ex_es": "La mesa electoral está formada por un presidente y dos vocales elegidos por sorteo.", "ex_en": "The polling station board is formed by a president and two members chosen by lottery."},
                {"lemma": "censo electoral", "pos": "noun", "translation": "electoral roll / voter register", "ex_es": "Para poder votar es imprescindible estar inscrito en el censo electoral vigente.", "ex_en": "To be able to vote it is essential to be registered on the current electoral roll."},
                {"lemma": "sorteo", "pos": "noun", "translation": "public draw / lottery", "ex_es": "Los ayuntamientos realizan un sorteo público para designar a los miembros de las mesas.", "ex_en": "City councils hold a public draw to appoint the members of the polling tables."},
                {"lemma": "vocal", "pos": "noun", "translation": "polling board member", "ex_es": "Cada mesa cuenta con un presidente y dos vocales titulares con sus suplentes.", "ex_en": "Each table has a president and two regular members with their alternates."},
                {"lemma": "secreto", "pos": "adjective", "translation": "secret", "ex_es": "Las cabinas garantizan que el voto sea siempre libre y secreto.", "ex_en": "The booths guarantee that the vote is always free and secret."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es la edad mínima para ejercer el derecho al voto en España?", "options": ["18 años", "16 años", "21 años", "25 años"], "answer": "18 años", "explanation": "La mayoría de edad constitucional y electoral en España se alcanza a los 18 años."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo es el voto en las elecciones españolas?", "options": ["Libre, igual, directo y secreto (y no obligatorio)", "Obligatorio bajo multa económica", "Público y a mano alzada", "Exclusivo para propietarios"], "answer": "Libre, igual, directo y secreto (y no obligatorio)", "explanation": "En España votar es un derecho constitucional libre, igual, directo y secreto, nunca una obligación sancionable."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los ciudadanos depositan su voto dentro de la ___ en el colegio electoral.", "answer": "urna", "english": "Citizens deposit their vote inside the ballot box at the polling station.", "explanation": "'Urna' is the ballot box."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Todos los españoles tienen ___ a participar en los asuntos públicos.", "answer": "derecho", "english": "All Spaniards have the right to participate in public affairs.", "explanation": "Article 23: 'tienen derecho a participar'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the constitutional characteristics of Spanish suffrage:", "words": ["El", "sufragio", "es", "universal,", "libre,", "igual,", "directo", "y", "secreto."], "answer": "El sufragio es universal, libre, igual, directo y secreto.", "english": "Suffrage is universal, free, equal, direct, and secret."},
                {"type": "dictation", "cat": "listening", "text": "En España pueden votar todos los ciudadanos mayores de dieciocho años.", "english": "In Spain all citizens over eighteen years of age can vote."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Cómo se selecciona a los ciudadanos que integran una mesa electoral?", "options": ["Por sorteo público entre los electores censados", "Por designación del Gobierno", "Por inscripción voluntaria en los partidos", "Entre los policías municipales"], "answer": "Por sorteo público entre los electores censados", "explanation": "El presidente y los dos vocales se eligen por sorteo público en cada municipio."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Para poder votar es obligatorio figurar inscrito en el ___ electoral.", "answer": "censo", "english": "To be able to vote it is mandatory to be registered on the electoral roll.", "explanation": "'Censo electoral' is the official register of voters."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about polling tables:", "words": ["La", "mesa", "electoral", "está", "compuesta", "por", "un", "presidente", "y", "dos", "vocales."], "answer": "La mesa electoral está compuesta por un presidente y dos vocales.", "english": "The polling station board is composed of a president and two members."}
            ]
        },
        {
            "num": "02",
            "story_slug": "convocatorias",
            "title": "Las cuatro citas con las urnas: generales, autonómicas, municipales y europeas",
            "goal": "Distinguish Spain's four types of elections, who can vote in municipal and European elections (including EU and reciprocal-treaty residents), and the 4-year mandate.",
            "grammar_slug": "cada-cuatro-anos-reciprocidad",
            "grammar_title": "Periodicidad y condición jurídica: 'cada cuatro años' y 'atendiendo a criterios de reciprocidad'",
            "grammar_summary": "Expressing electoral cycles ('cada cuatro años') and legal conditions ('atendiendo a criterios de reciprocidad').",
            "grammar_text": "All representative mandates in Spain—general, autonomic, and municipal—last four years ('cada cuatro años'), whereas European Parliament elections take place every five years across all EU member states. Under Article 13.2 of the Constitution (reformed in 1992), foreign residents in Spain may exercise active and passive suffrage in municipal elections under criteria of reciprocity ('atendiendo a criterios de reciprocidad'), a right enjoyed automatically by all European Union citizens.",
            "grammar_examples": [
                {"spanish": "Las elecciones generales y municipales se celebran en España cada cuatro años.", "english": "General and municipal elections are held in Spain every four years."},
                {"spanish": "Los ciudadanos de la Unión Europea residentes en España pueden votar en las elecciones municipales y europeas.", "english": "European Union citizens residing in Spain can vote in municipal and European elections."},
                {"spanish": "Atendiendo a criterios de reciprocidad, ciertos extranjeros residentes pueden votar en los comicios locales.", "english": "Based on criteria of reciprocity, certain foreign residents can vote in local elections."}
            ],
            "grammar_tip": "Key CCSE distinction: Only Spanish citizens vote in General and Autonomic elections, whereas EU citizens (and citizens of countries with reciprocity treaties) registered on the 'padrón' can vote in Municipal elections.",
            "story_title": "Cuatro urnas, cuatro ámbitos",
            "story_summary": "At a municipal voter information office in Valencia, an electoral officer explains to a Spanish citizen, an Italian resident, and a Colombian resident which elections each of them can participate in.",
            "story_location": "Valencia, Oficina del Censo Electoral",
            "story_paragraphs": [
                "En la Oficina del Censo Electoral de Valencia coinciden tres vecinos del mismo edificio: Clara, ciudadana española; Matteo, diseñador italiano residente en España desde hace cinco años; y Valentina, arquitecta colombiana con permiso de residencia y empadronada en la ciudad.",
                "La funcionaria les explica que en España existen cuatro grandes tipos de elecciones: las elecciones generales (para elegir a los diputados y senadores de las Cortes Generales), las elecciones autonómicas (para los parlamentos de las comunidades autónomas), las elecciones municipales (para los concejales de los ayuntamientos) y las elecciones al Parlamento Europeo.",
                "Clara, como ciudadana española, tiene derecho a votar en las cuatro convocatorias. Tanto las elecciones generales como las autonómicas y las municipales se convocan cada cuatro años, mientras que las europeas se celebran cada cinco.",
                "Matteo, por ser ciudadano de la Unión Europea empadronado en Valencia, puede votar y presentarse como candidato en las elecciones municipales españolas, así como elegir a los eurodiputados en las elecciones al Parlamento Europeo, pero no vota en las generales ni en las autonómicas.",
                "Valentina descubre que, gracias al tratado bilateral de reciprocidad firmado entre España y Colombia conforme al artículo 13.2 de la Constitución, ella también tiene derecho a votar en las elecciones municipales de su ayuntamiento tras haberse inscrito previamente en el censo electoral de extranjeros residentes."
            ],
            "comp_questions": [
                {
                    "question": "¿Con qué frecuencia se celebran de forma ordinaria las elecciones generales, autonómicas y municipales en España?",
                    "options": ["Cada cuatro años.", "Cada cinco años.", "Cada seis años."],
                    "correctIndex": 0,
                    "explanation": "El mandato de las Cortes Generales, los parlamentos autonómicos y los ayuntamientos en España es de cuatro años."
                },
                {
                    "question": "¿En qué elecciones españolas tienen derecho a votar los ciudadanos de la Unión Europea residentes y empadronados en España?",
                    "options": ["En las elecciones municipales y en las elecciones al Parlamento Europeo.", "En las elecciones generales y autonómicas únicamente.", "En ningún proceso electoral celebrado en España."],
                    "correctIndex": 0,
                    "explanation": "Los ciudadanos de la UE residentes en España pueden votar (y ser candidatos) en las elecciones municipales y en las elecciones al Parlamento Europeo."
                },
                {
                    "question": "¿Qué requisito constitucional permite a ciudadanos extracomunitarios residentes votar en las elecciones municipales?",
                    "options": ["La existencia de un tratado o acuerdo de reciprocidad con su país de origen.", "Tener un contrato indefinido en una empresa pública.", "Llevar más de veinte años residiendo en Madrid."],
                    "correctIndex": 0,
                    "explanation": "El artículo 13.2 de la Constitución permite el sufragio en elecciones municipales atendiendo a criterios de reciprocidad por tratado o ley."
                }
            ],
            "vocab": [
                {"lemma": "elecciones generales", "pos": "noun", "translation": "general elections", "ex_es": "En las elecciones generales se elige a los miembros del Congreso y del Senado.", "ex_en": "In general elections the members of Congress and the Senate are elected."},
                {"lemma": "elecciones municipales", "pos": "noun", "translation": "municipal / local elections", "ex_es": "En las elecciones municipales los vecinos eligen a los concejales de su ayuntamiento.", "ex_en": "In municipal elections residents elect the councilors of their city hall."},
                {"lemma": "reciprocidad", "pos": "noun", "translation": "reciprocity", "ex_es": "Los tratados de reciprocidad permiten votar en los comicios locales a ciertos residentes extranjeros.", "ex_en": "Reciprocity treaties allow certain foreign residents to vote in local elections."},
                {"lemma": "comicios", "pos": "noun", "translation": "elections / polls", "ex_es": "Los comicios autonómicos renuevan los parlamentos de las diecisiete comunidades.", "ex_en": "Autonomic elections renew the parliaments of the seventeen communities."},
                {"lemma": "eurodiputado", "pos": "noun", "translation": "Member of the European Parliament (MEP)", "ex_es": "Los ciudadanos eligen cada cinco años a sus eurodiputados en el Parlamento Europeo.", "ex_en": "Citizens elect their MEPs in the European Parliament every five years."},
                {"lemma": "mandato", "pos": "noun", "translation": "term of office / mandate", "ex_es": "El mandato de los diputados, senadores y concejales dura cuatro años.", "ex_en": "The term of office of deputies, senators, and councilors lasts four years."},
                {"lemma": "empadronado", "pos": "adjective", "translation": "registered in the municipal census", "ex_es": "Los ciudadanos europeos empadronados pueden votar en su municipio español.", "ex_en": "European citizens registered on the municipal roll can vote in their Spanish municipality."},
                {"lemma": "convocatoria", "pos": "noun", "translation": "call / election notice", "ex_es": "El Real Decreto de convocatoria fija la fecha exacta de la votación.", "ex_en": "The Royal Decree of convocation sets the exact date of the vote."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cada cuántos años se celebran las elecciones generales en España?", "options": ["Cada 4 años", "Cada 5 años", "Cada 3 años", "Cada 6 años"], "answer": "Cada 4 años", "explanation": "Las elecciones generales, autonómicas y municipales se celebran cada 4 años."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué elecciones pueden votar los ciudadanos de la Unión Europea residentes en España?", "options": ["En las elecciones municipales y al Parlamento Europeo", "En las elecciones generales al Congreso", "En las elecciones autonómicas", "En todas las elecciones sin excepción"], "answer": "En las elecciones municipales y al Parlamento Europeo", "explanation": "Los residentes comunitarios tienen derecho de sufragio activo y pasivo en las elecciones municipales y europeas."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En las elecciones ___ se elige a los concejales de los ayuntamientos.", "answer": "municipales", "english": "In municipal elections the councilors of city halls are elected.", "explanation": "'Elecciones municipales' elect local councilors."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Atendiendo a criterios de ___, algunos residentes extranjeros pueden votar en las elecciones locales.", "answer": "reciprocidad", "english": "Based on criteria of reciprocity, some foreign residents can vote in local elections.", "explanation": "Article 13.2 establishes 'criterios de reciprocidad'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about general elections:", "words": ["Las", "elecciones", "generales", "se", "celebran", "cada", "cuatro", "años."], "answer": "Las elecciones generales se celebran cada cuatro años.", "english": "General elections are held every four years."},
                {"type": "dictation", "cat": "listening", "text": "En las elecciones generales se elige a los diputados y a los senadores.", "english": "In general elections deputies and senators are elected."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Quiénes son elegidos directamente por los ciudadanos en las elecciones generales?", "options": ["Los diputados y senadores de las Cortes Generales", "El Presidente del Gobierno y los ministros", "Los magistrados del Tribunal Constitucional", "Los alcaldes y concejales"], "answer": "Los diputados y senadores de las Cortes Generales", "explanation": "En las generales los ciudadanos eligen a los diputados y senadores; luego el Congreso inviste al Presidente del Gobierno."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ de los diputados y concejales españoles tiene una duración de cuatro años.", "answer": "mandato", "english": "The term of office of Spanish deputies and councilors has a duration of four years.", "explanation": "'Mandato' means term of office."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about EU citizens in Spain:", "words": ["Los", "ciudadanos", "europeos", "residentes", "pueden", "votar", "en", "las", "elecciones", "municipales."], "answer": "Los ciudadanos europeos residentes pueden votar en las elecciones municipales.", "english": "Resident European citizens can vote in municipal elections."}
            ]
        },
        {
            "num": "03",
            "story_slug": "dhondt",
            "title": "El sistema proporcional, la circunscripción provincial y la Junta Electoral",
            "goal": "Understand how votes translate into seats in Spain: the province as electoral district ('circunscripción electoral'), proportional representation (D'Hondt method), and the Junta Electoral Central.",
            "grammar_slug": "en-proporcion-a",
            "grammar_title": "Expresar proporcionalidad y reparto: 'en proporción a' y 'con arreglo a'",
            "grammar_summary": "Using 'en proporción a' and 'con arreglo a' to describe seat allocation and legal formulas.",
            "grammar_text": "Article 68.2 of the Constitution specifies that the electoral district ('la circunscripción electoral') for the Congress and Senate is the province ('la provincia'), while Ceuta and Melilla elect one deputy and two senators each. Seats in the Congress are allocated in proportion to the votes obtained ('en proporción a los votos obtenidos') using the D'Hondt formula ('con arreglo a la ley D'Hondt') and closed, blocked lists ('listas cerradas y bloqueadas').",
            "grammar_examples": [
                {"spanish": "Los escaños del Congreso se reparten en proporción a los votos obtenidos en cada provincia.", "english": "Seats in Congress are distributed in proportion to the votes obtained in each province."},
                {"spanish": "La elección se verifica en cada circunscripción atendiendo a criterios de representación proporcional.", "english": "The election is carried out in each constituency following criteria of proportional representation."},
                {"spanish": "La Junta Electoral Central vela por la transparencia del escrutinio con arreglo a la ley.", "english": "The Central Electoral Board watches over the transparency of the count in accordance with the law."}
            ],
            "grammar_tip": "Remember for the CCSE exam: for general elections, the electoral constituency ('la circunscripción electoral') is the PROVINCE (except in European elections, where the constituency is the entire national territory).",
            "story_title": "La noche del escrutinio",
            "story_summary": "At eight in the evening when polling stations close, a math teacher and her daughter follow the public vote count and see how the provincial constituencies and the Junta Electoral Central guarantee a transparent result.",
            "story_location": "Zaragoza",
            "story_paragraphs": [
                "A las ocho de la tarde se cierran los colegios electorales y comienza el escrutinio, un recuento de votos que en España es un acto totalmente público al que cualquier ciudadano puede asistir en silencio.",
                "Carmen, profesora de matemáticas en Zaragoza, le explica a su hija cómo se transforman millones de papeletas en los 350 escaños del Congreso de los Diputados. Según el artículo 68 de la Constitución, la circunscripción electoral básica es la provincia.",
                "Cada una de las cincuenta provincias españolas tiene asignado un mínimo inicial de dos diputados, Ceuta y Melilla eligen un diputado cada una, y los demás escaños se distribuyen en proporción a la población de cada provincia.",
                "Para el Congreso se utilizan listas cerradas y bloqueadas: el elector elige la papeleta completa de un partido sin alterar el orden de los candidatos, y los escaños se reparten mediante la fórmula proporcional de la ley D'Hondt entre las candidaturas que superan el tres por ciento de los votos válidos.",
                "Todo el proceso está supervisado por la Administración Electoral, encabezada por la Junta Electoral Central —un órgano permanente integrado por magistrados del Tribunal Supremo y catedráticos de Derecho y Ciencias Políticas— que garantiza la limpieza y objetividad de cada elección."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la circunscripción electoral para las elecciones al Congreso de los Diputados y al Senado en España?",
                    "options": ["La provincia (además de las ciudades autónomas de Ceuta y Melilla).", "El barrio o distrito postal.", "La comarca histórica únicamente."],
                    "correctIndex": 0,
                    "explanation": "El artículo 68.2 de la Constitución establece que la circunscripción electoral es la provincia."
                },
                {
                    "question": "¿Qué órgano permanente garantiza la transparencia, objetividad e igualdad de los procesos electorales en España?",
                    "options": ["La Junta Electoral Central.", "El Consejo de Estado.", "El Tribunal de Cuentas."],
                    "correctIndex": 0,
                    "explanation": "La Junta Electoral Central (junto con las juntas provinciales y de zona) integra la Administración Electoral que supervisa las elecciones."
                },
                {
                    "question": "¿Cuántos diputados eligen las ciudades autónomas de Ceuta y Melilla en el Congreso?",
                    "options": ["Un diputado cada una.", "Cinco diputados cada una.", "Ningún diputado."],
                    "correctIndex": 0,
                    "explanation": "Ceuta y Melilla están representadas en el Congreso de los Diputados por un diputado cada una (y dos senadores cada una en el Senado)."
                }
            ],
            "vocab": [
                {"lemma": "circunscripción", "pos": "noun", "translation": "electoral district / constituency", "ex_es": "En las elecciones generales, la circunscripción electoral es la provincia.", "ex_en": "In general elections, the electoral constituency is the province."},
                {"lemma": "escrutinio", "pos": "noun", "translation": "vote count / scrutiny", "ex_es": "El escrutinio en las mesas electorales es público y comienza a las ocho de la tarde.", "ex_en": "The vote count at polling tables is public and begins at eight in the evening."},
                {"lemma": "proporcional", "pos": "adjective", "translation": "proportional", "ex_es": "El Congreso se elige siguiendo criterios de representación proporcional.", "ex_en": "Congress is elected following criteria of proportional representation."},
                {"lemma": "Junta Electoral Central", "pos": "noun", "translation": "Central Electoral Board", "ex_es": "La Junta Electoral Central vela por la legalidad y transparencia de las elecciones.", "ex_en": "The Central Electoral Board watches over the legality and transparency of elections."},
                {"lemma": "candidatura", "pos": "noun", "translation": "candidacy / party list", "ex_es": "Cada partido político presenta una candidatura en forma de lista cerrada.", "ex_en": "Each political party presents a candidacy in the form of a closed list."},
                {"lemma": "recuento", "pos": "noun", "translation": "count / tally", "ex_es": "Al finalizar el recuento, el presidente de la mesa anuncia en voz alta los resultados.", "ex_en": "At the end of the count, the table president announces the results aloud."},
                {"lemma": "lista cerrada", "pos": "noun", "translation": "closed party list", "ex_es": "Para el Congreso se vota mediante lista cerrada, mientras que en el Senado la lista es abierta.", "ex_en": "For Congress voting uses a closed list, whereas in the Senate the list is open."},
                {"lemma": "acta", "pos": "noun", "translation": "official record / tally sheet", "ex_es": "Los miembros de la mesa firman el acta de escrutinio con el resultado final.", "ex_en": "The members of the polling table sign the tally sheet with the final result."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es la circunscripción electoral en las elecciones generales españolas?", "options": ["La provincia", "El municipio", "El barrio", "La Unión Europea"], "answer": "La provincia", "explanation": "Según el artículo 68.2 de la Constitución, la circunscripción electoral es la provincia."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué institución supervisa la transparencia y legalidad de los procesos electorales en España?", "options": ["La Junta Electoral Central", "El Banco de España", "La Real Academia Española", "El Ministerio de Defensa"], "answer": "La Junta Electoral Central", "explanation": "La Administración Electoral, encabezada por la Junta Electoral Central, garantiza la transparencia y objetividad electoral."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En las elecciones generales, la ___ electoral básica es la provincia.", "answer": "circunscripción", "english": "In general elections, the basic electoral constituency is the province.", "explanation": "'Circunscripción electoral' means electoral constituency."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Los escaños del Congreso se reparten en ___ a los votos obtenidos.", "answer": "proporción", "english": "Seats in Congress are distributed in proportion to the votes obtained.", "explanation": "'En proporción a' expresses proportional allocation."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the electoral constituency:", "words": ["La", "circunscripción", "electoral", "para", "el", "Congreso", "es", "la", "provincia."], "answer": "La circunscripción electoral para el Congreso es la provincia.", "english": "The electoral constituency for Congress is the province."},
                {"type": "dictation", "cat": "listening", "text": "La Junta Electoral Central garantiza la transparencia de las elecciones.", "english": "The Central Electoral Board guarantees the transparency of the elections."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Cuántos diputados eligen Ceuta y Melilla para el Congreso de los Diputados?", "options": ["Un diputado cada una (dos en total)", "Diez diputados cada una", "Tres diputados cada una", "Ninguno"], "answer": "Un diputado cada una (dos en total)", "explanation": "Las poblaciones de Ceuta y Melilla están representadas cada una de ellas por un diputado en el Congreso."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ de los votos en los colegios electorales es un acto público.", "answer": "escrutinio", "english": "The counting of votes at polling stations is a public act.", "explanation": "'Escrutinio' is the official vote count."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about Ceuta and Melilla in Congress:", "words": ["Ceuta", "y", "Melilla", "eligen", "un", "diputado", "cada", "una."], "answer": "Ceuta y Melilla eligen un diputado cada una.", "english": "Ceuta and Melilla elect one deputy each."}
            ]
        },
        {
            "num": "04",
            "story_slug": "partidos",
            "title": "Partidos políticos, sindicatos y asociaciones empresariales",
            "goal": "Understand Articles 6 and 7 of the Preliminary Title: the constitutional role of political parties as expressions of political pluralism, and of trade unions and business associations.",
            "grammar_slug": "contribuir-a-la-defensa",
            "grammar_title": "Verbos de función social: 'expresar el pluralismo', 'concurrir a' y 'contribuir a'",
            "grammar_summary": "Using 'concurrir a' and 'contribuir a' to describe the constitutional mission of parties and unions.",
            "grammar_text": "Articles 6 and 7 of the Preliminary Title define the intermediate pillars of Spanish democracy. Political parties express political pluralism, concur in forming and manifesting the popular will ('concurren a la formación y manifestación de la voluntad popular'), and are fundamental instruments for political participation. Trade unions ('los sindicatos de trabajadores') and business associations ('las asociaciones empresariales') contribute to the defense and promotion of their economic and social interests ('contribuyen a la defensa y promoción de los intereses económicos y sociales'). Both must have a democratic internal structure and functioning.",
            "grammar_examples": [
                {"spanish": "Los partidos políticos expresan el pluralismo político y son instrumento fundamental para la participación.", "english": "Political parties express political pluralism and are a fundamental instrument for participation."},
                {"spanish": "Los sindicatos y las asociaciones empresariales contribuyen a la defensa de los intereses económicos y sociales.", "english": "Trade unions and business associations contribute to the defense of economic and social interests."},
                {"spanish": "Su estructura interna y su funcionamiento deberán ser siempre democráticos.", "english": "Their internal structure and functioning must always be democratic."}
            ],
            "grammar_tip": "Both Article 6 (political parties) and Article 7 (trade unions and employers' associations) end with the exact same constitutional requirement: 'Su estructura interna y funcionamiento deberán ser democráticos.'",
            "story_title": "El diálogo social y político",
            "story_summary": "During a civic forum in Bilbao, representatives from political parties, trade unions, and business organizations explain how Articles 6 and 7 of the Constitution require internal democracy in their organizations.",
            "story_location": "Bilbao",
            "story_paragraphs": [
                "El Título Preliminar de la Constitución Española dedica dos artículos clave —el 6 y el 7— a las organizaciones que canalizan la vida política y socioeconómica de España: los partidos políticos, los sindicatos de trabajadores y las asociaciones empresariales.",
                "En un foro cívico celebrado en Bilbao, una profesora de Derecho Constitucional recuerda que durante la dictadura franquista tanto los partidos políticos como los sindicatos libres estuvieron prohibidos, por lo que los constituyentes de 1978 quisieron blindar su papel en el propio Título Preliminar.",
                "Según el artículo 6, los partidos políticos expresan el pluralismo político, concurren a la formación y manifestación de la voluntad popular y son instrumento fundamental para la participación política. Su creación es libre dentro del respeto a la Constitución y a la ley.",
                "A su vez, el artículo 7 establece que los sindicatos de trabajadores (como UGT o CCOO, entre otros) y las asociaciones empresariales (como la CEOE) contribuyen a la defensa y promoción de los intereses económicos y sociales que les son propios mediante la negociación colectiva y el diálogo social.",
                "Para ambos tipos de organizaciones, la Constitución impone una regla innegociable: tanto la estructura interna como el funcionamiento de los partidos políticos, los sindicatos y las organizaciones empresariales deberán ser siempre democráticos."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 6 de la Constitución, ¿cuál es la función de los partidos políticos en España?",
                    "options": ["Expresar el pluralismo político, manifestar la voluntad popular y ser instrumento fundamental para la participación política.", "Sustituir a los jueces en la aplicación de las leyes.", "Recaudar directamente los impuestos municipales."],
                    "correctIndex": 0,
                    "explanation": "El artículo 6 define a los partidos políticos como expresión del pluralismo político e instrumento fundamental para la participación política."
                },
                {
                    "question": "¿Qué requisito exige la Constitución a la estructura interna y al funcionamiento de los partidos políticos y los sindicatos?",
                    "options": ["Que sean democráticos y respeten la Constitución y la ley.", "Que dependan jerárquicamente del Ministerio del Interior.", "Que tengan sede únicamente en la capital del Estado."],
                    "correctIndex": 0,
                    "explanation": "Tanto el artículo 6 como el artículo 7 exigen que su creación y ejercicio sean libres dentro del respeto a la Constitución y a la ley, y que su estructura interna y funcionamiento sean democráticos."
                },
                {
                    "question": "¿Qué organizaciones defienden y promueven los intereses económicos y sociales de los trabajadores y de los empresarios según el artículo 7?",
                    "options": ["Los sindicatos de trabajadores y las asociaciones empresariales.", "Las Reales Academias y los colegios electorales.", "Las diputaciones provinciales."],
                    "correctIndex": 0,
                    "explanation": "El artículo 7 reconoce a los sindicatos de trabajadores y a las asociaciones empresariales."
                }
            ],
            "vocab": [
                {"lemma": "partido político", "pos": "noun", "translation": "political party", "ex_es": "Los partidos políticos expresan el pluralismo político en las instituciones.", "ex_en": "Political parties express political pluralism in institutions."},
                {"lemma": "sindicato", "pos": "noun", "translation": "trade union / labor union", "ex_es": "Todo ciudadano tiene derecho a afiliarse libremente a un sindicato de trabajadores.", "ex_en": "Every citizen has the right to freely join a labor union."},
                {"lemma": "asociación empresarial", "pos": "noun", "translation": "business / employers' association", "ex_es": "Las asociaciones empresariales participan en el diálogo social junto a los sindicatos.", "ex_en": "Business associations participate in social dialogue alongside trade unions."},
                {"lemma": "afiliación", "pos": "noun", "translation": "membership / affiliation", "ex_es": "La afiliación a un partido o a un sindicato es completamente libre y voluntaria.", "ex_en": "Membership in a party or union is completely free and voluntary."},
                {"lemma": "negociación colectiva", "pos": "noun", "translation": "collective bargaining", "ex_es": "La Constitución garantiza el derecho a la negociación colectiva laboral entre representantes de trabajadores y empresarios.", "ex_en": "The Constitution guarantees the right to labor collective bargaining between representatives of workers and employers."},
                {"lemma": "huelga", "pos": "noun", "translation": "strike", "ex_es": "Se reconoce el derecho a la huelga de los trabajadores para la defensa de sus intereses.", "ex_en": "The right of workers to strike in defense of their interests is recognized."},
                {"lemma": "voluntad popular", "pos": "noun", "translation": "popular will", "ex_es": "Los partidos concurren a la formación y manifestación de la voluntad popular.", "ex_en": "Parties concur in forming and manifesting the popular will."},
                {"lemma": "diálogo social", "pos": "noun", "translation": "social dialogue", "ex_es": "El diálogo social busca acuerdos sobre empleo, salarios y pensiones.", "ex_en": "Social dialogue seeks agreements on employment, wages, and pensions."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "Según la Constitución, ¿qué organizaciones expresan el pluralismo político y son instrumento fundamental para la participación política?", "options": ["Los partidos políticos", "Las sociedades anónimas", "Los juzgados de guardia", "Las juntas electorales"], "answer": "Los partidos políticos", "explanation": "El artículo 6 de la Constitución atribuye esta función a los partidos políticos."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo deben ser la estructura interna y el funcionamiento de los partidos políticos y sindicatos en España?", "options": ["Democráticos", "Secretos y vitalicios", "Subordinados al Ejército", "Designados por el Gobierno"], "answer": "Democráticos", "explanation": "Los artículos 6 y 7 establecen que su estructura interna y funcionamiento deberán ser democráticos."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los ___ de trabajadores y las asociaciones empresariales defienden sus intereses económicos y sociales.", "answer": "sindicatos", "english": "Trade unions and business associations defend their economic and social interests.", "explanation": "'Sindicatos de trabajadores' are labor unions."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Los partidos políticos concurren a la formación y manifestación de la ___ popular.", "answer": "voluntad", "english": "Political parties concur in the formation and manifestation of the popular will.", "explanation": "'Voluntad popular' means popular will."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the constitutional rule from Articles 6 and 7:", "words": ["Su", "estructura", "interna", "y", "su", "funcionamiento", "deberán", "ser", "democráticos."], "answer": "Su estructura interna y su funcionamiento deberán ser democráticos.", "english": "Their internal structure and their functioning must be democratic."},
                {"type": "dictation", "cat": "listening", "text": "La afiliación a un sindicato o partido político es libre y voluntaria.", "english": "Affiliation with a trade union or political party is free and voluntary."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Es obligatorio en España estar afiliado a un sindicato para poder trabajar?", "options": ["No, nadie puede ser obligado a afiliarse a un sindicato", "Sí, en todas las empresas de más de diez empleados", "Sí, para los funcionarios públicos", "Solo en el sector industrial"], "answer": "No, nadie puede ser obligado a afiliarse a un sindicato", "explanation": "El artículo 28.1 de la Constitución establece que la libertad sindical comprende el derecho a fundar sindicatos y a afiliarse al de su elección, y que nadie podrá ser obligado a afiliarse."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los trabajadores tienen reconocido en la Constitución el derecho a la ___ para defender sus intereses.", "answer": "huelga", "english": "Workers have the right to strike recognized in the Constitution to defend their interests.", "explanation": "'Huelga' means strike (Article 28.2)."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about trade unions:", "words": ["Los", "sindicatos", "contribuyen", "a", "la", "defensa", "de", "los", "intereses", "de", "los", "trabajadores."], "answer": "Los sindicatos contribuyen a la defensa de los intereses de los trabajadores.", "english": "Trade unions contribute to the defense of workers' interests."}
            ]
        },
        {
            "num": "05",
            "story_slug": "iniciativa",
            "title": "Democracia directa: la Iniciativa Legislativa Popular y el referéndum",
            "goal": "Learn the mechanisms of direct citizen participation in Spain: the 500,000 accredited signatures required for a Popular Legislative Initiative (Article 87.3), the right of petition, and consultative referendums (Article 92).",
            "grammar_slug": "no-menos-de-firmas",
            "grammar_title": "Cuantificación mínima legal: 'no menos de + cifra' y 'quedar excluido de'",
            "grammar_summary": "Using 'no menos de 500.000 firmas acreditadas' and 'quedar excluido de' for constitutional requirements and exclusions.",
            "grammar_text": "To specify legal minimums and exceptions, Spanish constitutional prose uses 'no menos de + cifra' (no fewer than) and 'no procederá / queda excluido en materias de...' (it shall not apply / is excluded in matters of...). Under Article 87.3, citizens can present a Popular Legislative Initiative ('Iniciativa Legislativa Popular' or ILP) to Parliament with no fewer than 500,000 accredited signatures ('no menos de 500.000 firmas acreditadas'), although organic laws, tax laws, international affairs, and the prerogative of pardons are excluded.",
            "grammar_examples": [
                {"spanish": "Para presentar una Iniciativa Legislativa Popular se exigen no menos de 500.000 firmas acreditadas.", "english": "To submit a Popular Legislative Initiative, no fewer than 500,000 accredited signatures are required."},
                {"spanish": "Quedan excluidas de la iniciativa popular las materias propias de ley orgánica y las tributarias.", "english": "Matters proper to organic law and tax matters are excluded from the popular initiative."},
                {"spanish": "Las decisiones políticas de especial trascendencia podrán someterse a referéndum consultivo.", "english": "Political decisions of special importance may be submitted to a consultative referendum."}
            ],
            "grammar_tip": "Memorize the number 500,000 ('quinientas mil firmas acreditadas') — it is one of the most frequently tested CCSE numbers for citizen legislative initiatives!",
            "story_title": "Quinientas mil firmas para cambiar una ley",
            "story_summary": "A civic association collects 500,000 certified signatures across Spanish plazas to bring a Popular Legislative Initiative before the Congress of Deputies.",
            "story_location": "Madrid, Plaza de las Cortes",
            "story_paragraphs": [
                "¿Pueden los ciudadanos proponer directamente una ley a las Cortes Generales sin ser diputados ni senadores? La Constitución Española responde afirmativamente en su artículo 87.3 a través de la figura de la Iniciativa Legislativa Popular (ILP).",
                "Durante nueve meses, una plataforma ciudadana recorre plazas y universidades de toda España con pliegos oficiales sellados por la Junta Electoral Central. Su objetivo es reunir el mínimo constitucional exigido: no menos de 500.000 firmas acreditadas de ciudadanos mayores de edad inscritos en el censo electoral.",
                "La Constitución establece, sin embargo, límites precisos: no procede la iniciativa popular en materias propias de ley orgánica (como los derechos fundamentales o el Código Penal), ni en asuntos de naturaleza tributaria (impuestos), de carácter internacional o relativos a la prerrogativa de gracia (indultos).",
                "Además de la Iniciativa Legislativa Popular, el artículo 92 prevé que las decisiones políticas de especial trascendencia puedan ser sometidas a referéndum consultivo de todos los ciudadanos, convocado por el Rey a propuesta del Presidente del Gobierno y previamente autorizado por el Congreso de los Diputados.",
                "Asimismo, el artículo 29 reconoce a todos los ciudadanos el derecho de petición individual y colectiva, por escrito, ante cualquier institución o autoridad pública, completando los cauces de participación directa en la democracia española."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuántas firmas acreditadas como mínimo exige la Constitución para que los ciudadanos puedan presentar una Iniciativa Legislativa Popular?",
                    "options": ["No menos de 500.000 firmas acreditadas.", "No menos de 50.000 firmas.", "Un millón y medio de firmas."],
                    "correctIndex": 0,
                    "explanation": "El artículo 87.3 de la Constitución exige al menos 500.000 firmas acreditadas para presentar una proposición de ley mediante Iniciativa Legislativa Popular."
                },
                {
                    "question": "¿En cuál de las siguientes materias NO se puede presentar una Iniciativa Legislativa Popular?",
                    "options": ["En materias propias de ley orgánica, tributarias o de carácter internacional.", "En materias de protección medioambiental.", "En materias de fomento de la lectura y la cultura."],
                    "correctIndex": 0,
                    "explanation": "El artículo 87.3 excluye de la ILP las materias propias de ley orgánica, las tributarias, las de carácter internacional y la prerrogativa de gracia."
                },
                {
                    "question": "¿Quién convoca formalmente un referéndum consultivo en España, a propuesta del Presidente del Gobierno y con autorización previa del Congreso?",
                    "options": ["El Rey.", "El Defensor del Pueblo.", "El Fiscal General del Estado."],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 92.2 de la Constitución, el referéndum será convocado por el Rey, mediante propuesta del Presidente del Gobierno, previamente autorizada por el Congreso de los Diputados."
                }
            ],
            "vocab": [
                {"lemma": "Iniciativa Legislativa Popular", "pos": "noun", "translation": "Popular Legislative Initiative (ILP)", "ex_es": "La Iniciativa Legislativa Popular requiere al menos quinientas mil firmas acreditadas.", "ex_en": "A Popular Legislative Initiative requires at least five hundred thousand accredited signatures."},
                {"lemma": "firma acreditada", "pos": "noun", "translation": "accredited / certified signature", "ex_es": "Cada firma acreditada debe corresponder a un elector inscrito en el censo.", "ex_en": "Each accredited signature must correspond to a voter registered on the electoral roll."},
                {"lemma": "referéndum consultivo", "pos": "noun", "translation": "consultative referendum", "ex_es": "Las decisiones políticas de especial trascendencia pueden someterse a referéndum consultivo.", "ex_en": "Political decisions of special importance can be submitted to a consultative referendum."},
                {"lemma": "derecho de petición", "pos": "noun", "translation": "right of petition", "ex_es": "Todos los españoles tienen el derecho de petición individual y colectiva por escrito.", "ex_en": "All Spaniards have the right of individual and collective written petition."},
                {"lemma": "materia tributaria", "pos": "noun", "translation": "tax matter", "ex_es": "La materia tributaria está excluida de la Iniciativa Legislativa Popular.", "ex_en": "Tax matters are excluded from the Popular Legislative Initiative."},
                {"lemma": "indulto", "pos": "noun", "translation": "pardon", "ex_es": "La prerrogativa de gracia o indulto tampoco admite iniciativa popular.", "ex_en": "The prerogative of mercy or pardon also does not admit popular initiative."},
                {"lemma": "pliego", "pos": "noun", "translation": "official signature sheet", "ex_es": "Los promotores recogen las firmas de los ciudadanos en pliegos sellados.", "ex_en": "Promoters collect citizens' signatures on sealed sheets."},
                {"lemma": "trascendencia", "pos": "noun", "translation": "importance / far-reaching significance", "ex_es": "El referéndum se reserva para decisiones políticas de especial trascendencia.", "ex_en": "The referendum is reserved for political decisions of special significance."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántas firmas acreditadas se necesitan en España para presentar una Iniciativa Legislativa Popular (ILP)?", "options": ["Al menos 500.000 firmas", "Al menos 10.000 firmas", "Al menos 100.000 firmas", "Dos millones de firmas"], "answer": "Al menos 500.000 firmas", "explanation": "El artículo 87.3 de la Constitución exige no menos de 500.000 firmas acreditadas."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo debe ejercerse siempre el derecho de petición ante los poderes públicos según el artículo 29?", "options": ["Por escrito", "Únicamente por teléfono", "Por medio de un juez", "En sesión secreta"], "answer": "Por escrito", "explanation": "El artículo 29.1 reconoce el derecho de petición individual y colectiva, siempre por escrito."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Para presentar una Iniciativa Legislativa Popular se exigen no menos de 500.000 ___ acreditadas.", "answer": "firmas", "english": "To submit a Popular Legislative Initiative, no fewer than 500,000 accredited signatures are required.", "explanation": "'Firmas acreditadas' means accredited signatures."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Las decisiones políticas de especial trascendencia pueden someterse a ___ consultivo.", "answer": "referéndum", "english": "Political decisions of special significance can be submitted to a consultative referendum.", "explanation": "'Referéndum consultivo' (Article 92)."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the requirement for a Popular Legislative Initiative:", "words": ["La", "iniciativa", "popular", "exige", "no", "menos", "de", "quinientas", "mil", "firmas."], "answer": "La iniciativa popular exige no menos de quinientas mil firmas.", "english": "The popular initiative requires no fewer than five hundred thousand signatures."},
                {"type": "dictation", "cat": "listening", "text": "Se necesitan quinientas mil firmas para presentar una iniciativa legislativa popular.", "english": "Five hundred thousand signatures are needed to submit a popular legislative initiative."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué cámara debe autorizar previamente la convocatoria de un referéndum consultivo propuesto por el Presidente del Gobierno?", "options": ["El Congreso de los Diputados", "El Senado exclusivamente", "El Tribunal de Cuentas", "La Diputación Provincial"], "answer": "El Congreso de los Diputados", "explanation": "El artículo 92.2 exige que la propuesta del Presidente del Gobierno sea previamente autorizada por el Congreso de los Diputados."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Todos los españoles tienen el derecho de ___ individual y colectiva por escrito.", "answer": "petición", "english": "All Spaniards have the right of individual and collective petition in writing.", "explanation": "'Derecho de petición' (Article 29)."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about excluded subjects in an ILP:", "words": ["Las", "materias", "tributarias", "quedan", "excluidas", "de", "la", "iniciativa", "legislativa", "popular."], "answer": "Las materias tributarias quedan excluidas de la iniciativa legislativa popular.", "english": "Tax matters are excluded from the popular legislative initiative."}
            ]
        }
    ],
    "consolidation_exercises": [
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿A qué edad se adquiere el derecho al voto en España?", "options": ["A los 18 años", "A los 16 años", "A los 21 años", "A los 25 años"], "answer": "A los 18 años", "explanation": "Todos los españoles mayores de 18 años tienen derecho de sufragio."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Es obligatorio votar en las elecciones en España?", "options": ["No, votar es un derecho libre y no una obligación", "Sí, bajo sanción de multa", "Sí, salvo para mayores de 65 años", "Solo en las elecciones generales"], "answer": "No, votar es un derecho libre y no una obligación", "explanation": "El voto es libre y voluntario."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cada cuántos años se celebran las elecciones generales y municipales en España?", "options": ["Cada 4 años", "Cada 5 años", "Cada 6 años", "Cada 2 años"], "answer": "Cada 4 años", "explanation": "El mandato representativo en España dura 4 años."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es la circunscripción electoral en las elecciones al Congreso y al Senado?", "options": ["La provincia (más Ceuta y Melilla)", "El municipio", "El barrio", "La comarca"], "answer": "La provincia (más Ceuta y Melilla)", "explanation": "Artículo 68.2 de la Constitución."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué elecciones españolas pueden votar los ciudadanos de la Unión Europea residentes en España?", "options": ["En las elecciones municipales y al Parlamento Europeo", "En las elecciones generales", "En las elecciones autonómicas", "En ninguna"], "answer": "En las elecciones municipales y al Parlamento Europeo", "explanation": "Derecho de sufragio municipal y europeo para ciudadanos de la UE."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántas firmas acreditadas se requieren para presentar una Iniciativa Legislativa Popular?", "options": ["Al menos 500.000 firmas", "Al menos 50.000 firmas", "Al menos 100.000 firmas", "Un millón de firmas"], "answer": "Al menos 500.000 firmas", "explanation": "Artículo 87.3 de la Constitución."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El sufragio en España es universal, libre, igual, directo y ___.", "answer": "secreto", "english": "Suffrage in Spain is universal, free, equal, direct, and secret.", "explanation": "Characteristics of the vote."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los miembros de la mesa electoral (presidente y vocales) se eligen por ___ público.", "answer": "sorteo", "english": "The members of the polling table (president and members) are chosen by public lottery.", "explanation": "'Sorteo público'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Para votar es necesario estar inscrito en el ___ electoral.", "answer": "censo", "english": "To vote it is necessary to be registered on the electoral roll.", "explanation": "'Censo electoral'."},
        {"type": "fill-blank", "cat": "grammar", "prompt": "Los partidos políticos expresan el ___ político y concurren a formar la voluntad popular.", "answer": "pluralismo", "english": "Political parties express political pluralism and concur in forming the popular will.", "explanation": "Artículo 6 de la Constitución."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "La ___ Electoral Central garantiza la transparencia y objetividad de las elecciones.", "answer": "Junta", "english": "The Central Electoral Board guarantees the transparency and objectivity of the elections.", "explanation": "'Junta Electoral Central'."},
        {"type": "fill-blank", "cat": "grammar", "prompt": "Los ___ de trabajadores defienden y promueven los intereses laborales y sociales.", "answer": "sindicatos", "english": "Labor unions defend and promote labor and social interests.", "explanation": "Artículo 7 de la Constitución."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about voting age:", "words": ["En", "España", "pueden", "votar", "los", "ciudadanos", "mayores", "de", "dieciocho", "años."], "answer": "En España pueden votar los ciudadanos mayores de dieciocho años.", "english": "In Spain citizens over eighteen years of age can vote."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about internal democracy:", "words": ["La", "estructura", "interna", "de", "los", "partidos", "políticos", "debe", "ser", "democrática."], "answer": "La estructura interna de los partidos políticos debe ser democrática.", "english": "The internal structure of political parties must be democratic."},
        {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Order the sentence about the Popular Legislative Initiative:", "words": ["La", "Iniciativa", "Legislativa", "Popular", "requiere", "quinientas", "mil", "firmas", "acreditadas."], "answer": "La Iniciativa Legislativa Popular requiere quinientas mil firmas acreditadas.", "english": "The Popular Legislative Initiative requires five hundred thousand accredited signatures."},
        {"type": "dictation", "cat": "listening", "text": "El sufragio es universal, libre, igual, directo y secreto.", "english": "Suffrage is universal, free, equal, direct, and secret."},
        {"type": "dictation", "cat": "listening", "text": "Las elecciones generales y municipales se celebran cada cuatro años.", "english": "General and municipal elections are held every four years."},
        {"type": "dictation", "cat": "listening", "text": "Los partidos políticos son instrumento fundamental para la participación política.", "english": "Political parties are a fundamental instrument for political participation."}
    ]
}

UNIT_8 = {
    "slug": "seguridad",
    "legacy_prefix": "b1-ccse-fuerzas-seguridad",
    "unit_title": "Fuerzas Armadas y Cuerpos de Seguridad",
    "order": 8,
    "unit_summary": "Complete CCSE guide to Spain's Armed Forces and Law Enforcement: Article 8 constitutional mission of the Ejércitos (Tierra, Armada, Aire y Espacio), the King as supreme commander and the Government's direction of defense, Police (Policía Nacional and Guardia Civil), autonomic police forces (Mossos, Ertzaintza, Policía Foral), local police, and the 112 emergency number.",
    "unit_paragraphs": [],
    "unit_questions": [],
    "lessons": [
        {
            "num": "01",
            "story_slug": "fuerzasarmadas",
            "title": "Las Fuerzas Armadas: misión constitucional y ramas de los Ejércitos",
            "goal": "Understand Article 8 of the Constitution: the three branches of the Spanish Armed Forces (Ejército de Tierra, Armada, Ejército del Aire y del Espacio) and their mission to guarantee sovereignty, territorial integrity, and the constitutional order.",
            "grammar_slug": "tener-como-mision-garantizar",
            "grammar_title": "Misión institucional: 'tener como misión + infinitivo'",
            "grammar_summary": "Using 'tener como misión garantizar/defender' to state the constitutional mandate of the Armed Forces.",
            "grammar_text": "Article 8 of the Preliminary Title defines the composition and mission of the Spanish Armed Forces ('Las Fuerzas Armadas') using the structure 'constituidas por... tienen como misión + infinitivo'. They consist of the Army ('el Ejército de Tierra'), the Navy ('la Armada'), and the Air and Space Force ('el Ejército del Aire y del Espacio'). Their constitutional mission is threefold: to guarantee the sovereignty and independence of Spain, to defend its territorial integrity, and to protect the constitutional order.",
            "grammar_examples": [
                {"spanish": "Las Fuerzas Armadas tienen como misión garantizar la soberanía e independencia de España.", "english": "The Armed Forces have the mission of guaranteeing the sovereignty and independence of Spain."},
                {"spanish": "Están constituidas por el Ejército de Tierra, la Armada y el Ejército del Aire y del Espacio.", "english": "They are constituted by the Army, the Navy, and the Air and Space Force."},
                {"spanish": "El Rey ostenta el mando supremo, pero el Gobierno dirige la Administración militar y la defensa.", "english": "The King holds supreme command, but the Government directs the military administration and defense."}
            ],
            "grammar_tip": "Remember the division of roles for CCSE: the King holds the supreme command ('ostenta el mando supremo') of the Armed Forces (Art. 62), while the Government directs defense policy and military administration (Art. 97) through the Ministry of Defense.",
            "story_title": "Tierra, mar, aire y emergencias",
            "story_summary": "During Armed Forces Day, an officer of the Military Emergency Unit (UME) explains Article 8 of the Constitution, the three military branches, and Spain's humanitarian and peacekeeping missions.",
            "story_location": "Madrid, Paseo de la Castellana",
            "story_paragraphs": [
                "Según el artículo 8 del Título Preliminar de la Constitución Española, las Fuerzas Armadas están constituidas por el Ejército de Tierra, la Armada y el Ejército del Aire y del Espacio.",
                "Su misión constitucional consiste en garantizar la soberanía e independencia de España, defender su integridad territorial y proteger el ordenamiento constitucional frente a cualquier amenaza.",
                "Aunque el Rey ostenta el mando supremo de las Fuerzas Armadas como Jefe del Estado, la dirección efectiva de la política de defensa y de la Administración militar corresponde al Gobierno de la Nación, a través del Ministerio de Defensa.",
                "Desde el año 2001 el servicio militar obligatorio quedó suprimido en España, por lo que las Fuerzas Armadas están integradas íntegramente por militares profesionales, hombres y mujeres en plena igualdad de condiciones.",
                "Además de la defensa nacional y de las misiones internacionales de paz bajo bandera de la ONU, la OTAN y la Unión Europea, los militares españoles cuentan con la Unidad Militar de Emergencias (UME), que interviene dentro de España ante graves catástrofes naturales como incendios forestales, inundaciones o nevadas."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 8 de la Constitución, ¿qué tres ramas integran las Fuerzas Armadas españolas?",
                    "options": ["El Ejército de Tierra, la Armada y el Ejército del Aire y del Espacio.", "La Policía Nacional, la Guardia Civil y la Policía Local.", "El Congreso, el Senado y el Gobierno."],
                    "correctIndex": 0,
                    "explanation": "El artículo 8 establece que las Fuerzas Armadas están constituidas por el Ejército de Tierra, la Armada y el Ejército del Aire y del Espacio."
                },
                {
                    "question": "¿Cuál es la misión constitucional de las Fuerzas Armadas según el artículo 8?",
                    "options": ["Garantizar la soberanía e independencia de España, defender su integridad territorial y el ordenamiento constitucional.", "Aprobar las leyes orgánicas y los Presupuestos Generales.", "Juzgar los delitos civiles y mercantiles."],
                    "correctIndex": 0,
                    "explanation": "El artículo 8.1 les encomienda garantizar la soberanía e independencia de España y defender su integridad territorial y el ordenamiento constitucional."
                },
                {
                    "question": "¿Quién dirige la política de defensa y la Administración militar en España conforme al artículo 97?",
                    "options": ["El Gobierno de la Nación (a través del Ministerio de Defensa).", "El Tribunal Constitucional.", "Los alcaldes de cada municipio."],
                    "correctIndex": 0,
                    "explanation": "El Rey ostenta el mando supremo simbólico, pero el Gobierno dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado."
                }
            ],
            "vocab": [
                {"lemma": "Fuerzas Armadas", "pos": "noun", "translation": "Armed Forces", "ex_es": "Las Fuerzas Armadas defienden la soberanía y la integridad territorial de España.", "ex_en": "The Armed Forces defend the sovereignty and territorial integrity of Spain."},
                {"lemma": "Ejército de Tierra", "pos": "noun", "translation": "Army (Land Force)", "ex_es": "El Ejército de Tierra es el componente terrestre de las Fuerzas Armadas.", "ex_en": "The Army is the land component of the Armed Forces."},
                {"lemma": "Armada", "pos": "noun", "translation": "Navy", "ex_es": "La Armada española protege los espacios marítimos y las costas nacionales.", "ex_en": "The Spanish Navy protects the maritime spaces and national coasts."},
                {"lemma": "integridad territorial", "pos": "noun", "translation": "territorial integrity", "ex_es": "Defender la integridad territorial de España es una misión constitucional.", "ex_en": "Defending the territorial integrity of Spain is a constitutional mission."},
                {"lemma": "misión de paz", "pos": "noun", "translation": "peacekeeping mission", "ex_es": "España participa activamente en misiones internacionales de paz de la ONU y la UE.", "ex_en": "Spain actively participates in UN and EU international peacekeeping missions."},
                {"lemma": "Unidad Militar de Emergencias", "pos": "noun", "translation": "Military Emergency Unit (UME)", "ex_es": "La Unidad Militar de Emergencias auxilia a la población en incendios e inundaciones.", "ex_en": "The Military Emergency Unit assists the population in fires and floods."},
                {"lemma": "profesional", "pos": "adjective", "translation": "professional", "ex_es": "En España el ejército es totalmente profesional y el servicio militar no es obligatorio.", "ex_en": "In Spain the military is completely professional and military service is not compulsory."},
                {"lemma": "defensa", "pos": "noun", "translation": "defense", "ex_es": "El Ministerio de Defensa coordina la administración militar del Estado.", "ex_en": "The Ministry of Defense coordinates the state's military administration."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuáles son las tres ramas que componen las Fuerzas Armadas españolas?", "options": ["Ejército de Tierra, Armada y Ejército del Aire y del Espacio", "Policía Nacional, Guardia Civil y Policía Local", "Tierra, Guardia Real y Aduanas", "Armada, Cruz Roja y Protección Civil"], "answer": "Ejército de Tierra, Armada y Ejército del Aire y del Espacio", "explanation": "Artículo 8.1 de la Constitución Española."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Es obligatorio actualmente el servicio militar en España?", "options": ["No, las Fuerzas Armadas son totalmente profesionales desde 2001", "Sí, durante doce meses para los varones", "Sí, para todos los mayores de 18 años", "Solo en las comunidades costeras"], "answer": "No, las Fuerzas Armadas son totalmente profesionales desde 2001", "explanation": "El servicio militar obligatorio fue suspendido definitivamente en 2001."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Las Fuerzas Armadas están integradas por el Ejército de Tierra, la ___ y el Ejército del Aire y del Espacio.", "answer": "Armada", "english": "The Armed Forces are made up of the Army, the Navy, and the Air and Space Force.", "explanation": "'La Armada' is the Spanish Navy."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Las Fuerzas Armadas tienen como misión defender la ___ territorial y el ordenamiento constitucional.", "answer": "integridad", "english": "The Armed Forces have the mission of defending territorial integrity and the constitutional order.", "explanation": "'Integridad territorial' (Article 8.1)."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the constitutional mission of the Armed Forces:", "words": ["Las", "Fuerzas", "Armadas", "garantizan", "la", "soberanía", "e", "independencia", "de", "España."], "answer": "Las Fuerzas Armadas garantizan la soberanía e independencia de España.", "english": "The Armed Forces guarantee the sovereignty and independence of Spain."},
                {"type": "dictation", "cat": "listening", "text": "El Gobierno dirige la administración militar y la defensa del Estado.", "english": "The Government directs the military administration and the defense of the State."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué unidad de las Fuerzas Armadas interviene dentro de España para socorrer a la población en incendios forestales, inundaciones o grandes nevadas?", "options": ["La Unidad Militar de Emergencias (UME)", "La Junta Electoral Central", "El Tribunal de Cuentas", "La Inspección de Hacienda"], "answer": "La Unidad Militar de Emergencias (UME)", "explanation": "La UME actúa en situaciones de grave riesgo, catástrofe o calamidad pública."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Rey ostenta el mando supremo de las Fuerzas Armadas, pero el ___ dirige la política de defensa.", "answer": "Gobierno", "english": "The King holds supreme command of the Armed Forces, but the Government directs defense policy.", "explanation": "Article 97 assigns defense direction to the Government."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the Ministry of Defense:", "words": ["El", "Ministerio", "de", "Defensa", "coordina", "las", "Fuerzas", "Armadas", "españolas."], "answer": "El Ministerio de Defensa coordina las Fuerzas Armadas españolas.", "english": "The Ministry of Defense coordinates the Spanish Armed Forces."}
            ]
        },
        {
            "num": "02",
            "story_slug": "policianacional",
            "title": "Las Fuerzas y Cuerpos de Seguridad del Estado: la Policía Nacional",
            "goal": "Learn Article 104 of the Constitution and the role of the Cuerpo Nacional de Policía: a civilian state force under the Ministry of the Interior responsible for urban security and issuing the DNI and passport.",
            "grammar_slug": "bajo-la-dependencia-del",
            "grammar_title": "Adscripción orgánica: 'bajo la dependencia de' y 'corresponder la expedición de'",
            "grammar_summary": "Using 'bajo la dependencia del Gobierno' and 'expedir documentos' to describe police competencies.",
            "grammar_text": "Article 104 of the Constitution states that the Security Forces and Corps, under the authority of the Government ('bajo la dependencia del Gobierno'), have the mission of protecting the free exercise of rights and freedoms and guaranteeing citizen security ('garantizar la seguridad ciudadana'). The Cuerpo Nacional de Policía (Policía Nacional) is an armed institute of a civilian nature ('de naturaleza civil') dependent on the Ministry of the Interior, acting mainly in provincial capitals and urban areas and holding exclusive competence throughout Spain for issuing the DNI, passport, and foreigner documentation (TIE/NIE).",
            "grammar_examples": [
                {"spanish": "Las Fuerzas y Cuerpos de Seguridad, bajo la dependencia del Gobierno, garantizan la seguridad ciudadana.", "english": "The Security Forces and Corps, under the authority of the Government, guarantee citizen security."},
                {"spanish": "La Policía Nacional es un instituto armado de naturaleza civil dependiente del Ministerio del Interior.", "english": "The National Police is an armed institute of a civilian nature dependent on the Ministry of the Interior."},
                {"spanish": "A la Policía Nacional le corresponde en exclusiva la expedición del DNI y del pasaporte.", "english": "The National Police has exclusive responsibility for issuing the DNI and the passport."}
            ],
            "grammar_tip": "High-frequency CCSE exam question: Which body issues the DNI, passport, and NIE/TIE in Spain? Always the **Policía Nacional** (under the Ministry of the Interior).",
            "story_title": "En la comisaría de la Policía Nacional",
            "story_summary": "At a National Police station in Seville, a citizen renews her DNI and passport while an inspector explains the civilian nature and urban responsibilities of the Cuerpo Nacional de Policía.",
            "story_location": "Sevilla, Comisaría de la Policía Nacional",
            "story_paragraphs": [
                "El artículo 104 de la Constitución establece que las Fuerzas y Cuerpos de Seguridad, bajo la dependencia del Gobierno, tienen como misión proteger el libre ejercicio de los derechos y libertades y garantizar la seguridad ciudadana.",
                "A nivel estatal, existen dos grandes cuerpos dependientes del Ministerio del Interior: el Cuerpo Nacional de Policía (conocido como Policía Nacional) y la Guardia Civil.",
                "La Policía Nacional es un instituto armado de naturaleza civil que ejerce sus funciones de seguridad ciudadana e investigación criminal principalmente en las capitales de provincia y en los grandes núcleos urbanos de España.",
                "Además de perseguir el delito y controlar la entrada y salida de españoles y extranjeros en las fronteras y aeropuertos, la Policía Nacional tiene una competencia administrativa exclusiva en todo el territorio nacional: la expedición del Documento Nacional de Identidad (DNI), del pasaporte español y de las tarjetas de identidad de extranjero (TIE).",
                "En cualquier comisaría de la Policía Nacional, los ciudadanos pueden tanto presentar denuncias y solicitar protección como tramitar sus documentos oficiales de identidad con cita previa."
            ],
            "comp_questions": [
                {
                    "question": "¿De qué ministerio dependen las Fuerzas y Cuerpos de Seguridad del Estado (Policía Nacional y Guardia Civil)?",
                    "options": ["Del Ministerio del Interior.", "Del Ministerio de Hacienda.", "Del Ministerio de Educación."],
                    "correctIndex": 0,
                    "explanation": "Tanto la Policía Nacional como la Guardia Civil dependen del Ministerio del Interior en el ejercicio de sus funciones de seguridad ciudadana."
                },
                {
                    "question": "¿Qué cuerpo policial tiene la competencia exclusiva para expedir el DNI y el pasaporte en toda España?",
                    "options": ["La Policía Nacional (Cuerpo Nacional de Policía).", "La Policía Local de cada ayuntamiento.", "La Guardia Civil."],
                    "correctIndex": 0,
                    "explanation": "La expedición del DNI, del pasaporte y de la documentación de extranjería corresponde en exclusiva a la Policía Nacional."
                },
                {
                    "question": "¿Qué carácter tiene la Policía Nacional y dónde desarrolla principalmente sus funciones de seguridad?",
                    "options": ["Es un instituto armado de naturaleza civil que actúa principalmente en capitales de provincia y núcleos urbanos.", "Es un cuerpo militar que actúa solo en alta mar.", "Es una policía municipal dependiente del alcalde."],
                    "correctIndex": 0,
                    "explanation": "La Policía Nacional tiene naturaleza civil y actúa principalmente en las capitales de provincia y grandes ciudades."
                }
            ],
            "vocab": [
                {"lemma": "Policía Nacional", "pos": "noun", "translation": "National Police", "ex_es": "La Policía Nacional actúa en los núcleos urbanos y expide el DNI y el pasaporte.", "ex_en": "The National Police operates in urban areas and issues the DNI and passport."},
                {"lemma": "seguridad ciudadana", "pos": "noun", "translation": "citizen / public security", "ex_es": "Las fuerzas policiales tienen la misión de garantizar la seguridad ciudadana.", "ex_en": "Police forces have the mission of guaranteeing public security."},
                {"lemma": "comisaría", "pos": "noun", "translation": "police station", "ex_es": "El ciudadano acudió a la comisaría para renovar su pasaporte y presentar una denuncia.", "ex_en": "The citizen went to the police station to renew his passport and file a report."},
                {"lemma": "expedición", "pos": "noun", "translation": "issuance (of official documents)", "ex_es": "La expedición del DNI corresponde en exclusiva al Cuerpo Nacional de Policía.", "ex_en": "The issuance of the DNI belongs exclusively to the National Police Corps."},
                {"lemma": "naturaleza civil", "pos": "noun", "translation": "civilian nature", "ex_es": "A diferencia de la Guardia Civil, la Policía Nacional tiene naturaleza civil.", "ex_en": "Unlike the Civil Guard, the National Police has a civilian nature."},
                {"lemma": "pasaporte", "pos": "noun", "translation": "passport", "ex_es": "El pasaporte español permite viajar fuera de la Unión Europea.", "ex_en": "The Spanish passport allows travel outside the European Union."},
                {"lemma": "extranjería", "pos": "noun", "translation": "immigration / foreigner affairs", "ex_es": "Las oficinas de extranjería y la Policía Nacional tramitan las tarjetas de residencia.", "ex_en": "Immigration offices and the National Police process residence cards."},
                {"lemma": "denuncia", "pos": "noun", "translation": "police report / formal complaint", "ex_es": "Ante cualquier robo o delito, se puede presentar una denuncia en la comisaría.", "ex_en": "In case of any theft or crime, a report can be filed at the police station."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué cuerpo de seguridad expide el DNI y el pasaporte en España?", "options": ["La Policía Nacional", "La Guardia Civil", "La Policía Local", "El Ejército de Tierra"], "answer": "La Policía Nacional", "explanation": "La expedición del DNI y del pasaporte es competencia exclusiva de la Policía Nacional."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "Según el artículo 104 de la Constitución, ¿cuál es la misión de las Fuerzas y Cuerpos de Seguridad?", "options": ["Proteger el libre ejercicio de los derechos y libertades y garantizar la seguridad ciudadana", "Dictar sentencias penales", "Aprobar las leyes orgánicas", "Elegir al Defensor del Pueblo"], "answer": "Proteger el libre ejercicio de los derechos y libertades y garantizar la seguridad ciudadana", "explanation": "Artículo 104.1 de la Constitución Española."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Policía Nacional es un instituto armado de naturaleza ___ que actúa en las ciudades.", "answer": "civil", "english": "The National Police is an armed institute of a civilian nature that operates in cities.", "explanation": "'Naturaleza civil' distinguishes the National Police from the military-status Guardia Civil."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Las Fuerzas de Seguridad del Estado actúan bajo la dependencia del Ministerio del ___.", "answer": "Interior", "english": "State Security Forces operate under the authority of the Ministry of the Interior.", "explanation": "'Ministerio del Interior' directs public security."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about DNI issuance:", "words": ["La", "Policía", "Nacional", "expide", "el", "DNI", "y", "el", "pasaporte", "en", "toda", "España."], "answer": "La Policía Nacional expide el DNI y el pasaporte en toda España.", "english": "The National Police issues the DNI and the passport throughout Spain."},
                {"type": "dictation", "cat": "listening", "text": "Las Fuerzas de Seguridad garantizan la seguridad ciudadana y protegen los derechos.", "english": "The Security Forces guarantee citizen security and protect rights."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Dónde desarrolla principalmente sus funciones de seguridad ciudadana la Policía Nacional?", "options": ["En las capitales de provincia y grandes núcleos urbanos", "Únicamente en las carreteras comarcales y montes", "Exclusivamente en el mar territorial", "Solo dentro del Congreso de los Diputados"], "answer": "En las capitales de provincia y grandes núcleos urbanos", "explanation": "La Policía Nacional actúa en capitales de provincia y núcleos urbanos, mientras la Guardia Civil lo hace en el medio rural y vías interurbanas."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Para renovar el DNI o presentar una denuncia acudimos a una ___ de la Policía Nacional.", "answer": "comisaría", "english": "To renew the DNI or file a complaint we go to a National Police station.", "explanation": "'Comisaría' is a police station."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about Article 104:", "words": ["La", "policía", "protege", "el", "libre", "ejercicio", "de", "los", "derechos", "y", "libertades."], "answer": "La policía protege el libre ejercicio de los derechos y libertades.", "english": "The police protect the free exercise of rights and freedoms."}
            ]
        },
        {
            "num": "03",
            "story_slug": "guardiacivil",
            "title": "La Guardia Civil: naturaleza militar, medio rural, tráfico y SEPRONA",
            "goal": "Understand the distinctive nature and competencies of the Guardia Civil: an armed institute of military nature operating in rural Spain, interurban roads, ports/airports customs custody, and environmental protection (SEPRONA).",
            "grammar_slug": "tanto-en-como-en",
            "grammar_title": "Doble dependencia institucional: 'depender de... en cuanto a... y de... en lo relativo a'",
            "grammar_summary": "Describing dual institutional dependence ('del Ministerio del Interior en seguridad y del Ministerio de Defensa en misiones militares').",
            "grammar_text": "The Guardia Civil (founded in 1844) is an armed institute of a military nature ('un instituto armado de naturaleza militar'). Because of this status, it has a dual dependence: it depends on the Ministry of the Interior regarding citizen security and police services ('en cuanto a servicios de seguridad ciudadana'), and on the Ministry of Defense regarding promotions and military missions ('en lo relativo a ascensos y misiones de carácter militar').",
            "grammar_examples": [
                {"spanish": "La Guardia Civil es un instituto armado de naturaleza militar que forma parte de las Fuerzas de Seguridad del Estado.", "english": "The Civil Guard is an armed institute of a military nature that forms part of the State Security Forces."},
                {"spanish": "Vela por la seguridad tanto en el medio rural como en las carreteras interurbanas del Estado.", "english": "It watches over security both in rural areas and on the State's interurban highways."},
                {"spanish": "A través del SEPRONA, protege la naturaleza, los bosques y el medio ambiente.", "english": "Through SEPRONA, it protects nature, forests, and the environment."}
            ],
            "grammar_tip": "Remember the key contrasts for CCSE: Policía Nacional = civilian nature, cities, DNI/passport; Guardia Civil = military nature, rural areas, interurban highway traffic, coasts/borders, arms licenses, and environmental protection (SEPRONA).",
            "story_title": "De las carreteras al cuidado de los montes",
            "story_summary": "In a mountain municipality in Asturias, two Guardia Civil officers from the traffic unit and SEPRONA explain their rural, highway, customs, and environmental duties.",
            "story_location": "Asturias, Cuartel de la Guardia Civil",
            "story_paragraphs": [
                "Fundada en 1844, la Guardia Civil es el otro gran cuerpo que integra las Fuerzas y Cuerpos de Seguridad del Estado. A diferencia de la Policía Nacional, es un instituto armado de naturaleza militar.",
                "Por su estatuto especial, la Guardia Civil depende del Ministerio del Interior en todo lo relativo a la seguridad ciudadana, el orden público y las retribuciones, y depende del Ministerio de Defensa en cuanto a ascensos y misiones de carácter militar.",
                "Su ámbito territorial abarca los municipios rurales de toda España y el mar territorial. Además, la Agrupación de Tráfico de la Guardia Civil es la encargada de vigilar la circulación y auxiliar a los conductores en las carreteras y autopistas interurbanas del Estado.",
                "Entre sus competencias exclusivas en todo el territorio nacional figuran el control de armas y explosivos, el resguardo fiscal del Estado (la vigilancia aduanera contra el contrabando en puertos, aeropuertos y costas) y la custodia de vías de comunicación.",
                "Asimismo, la Guardia Civil cuenta con una unidad pionera en Europa, el SEPRONA (Servicio de Protección de la Naturaleza), dedicada a perseguir los delitos ecológicos, proteger la fauna y los parques nacionales e investigar los incendios forestales."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la naturaleza institucional de la Guardia Civil en España?",
                    "options": ["Es un instituto armado de naturaleza militar.", "Es una asociación privada de vigilancia vecinal.", "Es un cuerpo municipal dependiente de los alcaldes."],
                    "correctIndex": 0,
                    "explanation": "La Guardia Civil es un instituto armado de naturaleza militar que forma parte de las Fuerzas y Cuerpos de Seguridad del Estado."
                },
                {
                    "question": "¿Dónde ejerce principalmente la Guardia Civil sus funciones de seguridad ciudadana y vigilancia del tráfico?",
                    "options": ["En el medio rural y en las carreteras y vías interurbanas del Estado.", "Exclusivamente dentro de las calles peatonales del centro de Madrid.", "Únicamente en el extranjero."],
                    "correctIndex": 0,
                    "explanation": "La Guardia Civil garantiza la seguridad en el medio rural y vigila el tráfico en las vías interurbanas."
                },
                {
                    "question": "¿Qué servicio especializado de la Guardia Civil se encarga de la protección del medio ambiente y la persecución de delitos ecológicos?",
                    "options": ["El SEPRONA (Servicio de Protección de la Naturaleza).", "La Junta Electoral Provincial.", "El Instituto Cervantes."],
                    "correctIndex": 0,
                    "explanation": "El SEPRONA es la unidad de la Guardia Civil encargada de velar por la conservación de la naturaleza y el medio ambiente."
                }
            ],
            "vocab": [
                {"lemma": "Guardia Civil", "pos": "noun", "translation": "Civil Guard", "ex_es": "La Guardia Civil vigila la seguridad en el medio rural y en las carreteras interurbanas.", "ex_en": "The Civil Guard monitors security in rural areas and on interurban highways."},
                {"lemma": "naturaleza militar", "pos": "noun", "translation": "military nature", "ex_es": "La Guardia Civil es un instituto armado de naturaleza militar.", "ex_en": "The Civil Guard is an armed institute of a military nature."},
                {"lemma": "medio rural", "pos": "noun", "translation": "rural areas / countryside", "ex_es": "Los cuarteles de la Guardia Civil garantizan la seguridad en el medio rural.", "ex_en": "Civil Guard barracks guarantee security in rural areas."},
                {"lemma": "vía interurbana", "pos": "noun", "translation": "interurban highway / road between towns", "ex_es": "La Agrupación de Tráfico controla la seguridad vial en cada vía interurbana.", "ex_en": "The Traffic Division monitors road safety on every interurban highway."},
                {"lemma": "SEPRONA", "pos": "noun", "translation": "Nature Protection Service (of the Guardia Civil)", "ex_es": "El SEPRONA investiga los incendios forestales y protege las especies amenazadas.", "ex_en": "SEPRONA investigates forest fires and protects endangered species."},
                {"lemma": "resguardo fiscal", "pos": "noun", "translation": "customs / fiscal border guard", "ex_es": "La Guardia Civil ejerce el resguardo fiscal del Estado en puertos y aeropuertos.", "ex_en": "The Civil Guard exercises the State's fiscal customs guard in ports and airports."},
                {"lemma": "armas y explosivos", "pos": "noun", "translation": "weapons and explosives", "ex_es": "El control de licencias de armas y explosivos corresponde a la Guardia Civil.", "ex_en": "Control of weapons and explosives licenses belongs to the Civil Guard."},
                {"lemma": "cuartel", "pos": "noun", "translation": "barracks / Guardia Civil station", "ex_es": "Los vecinos del pueblo acudieron al cuartel de la Guardia Civil para pedir ayuda en la nevada.", "ex_en": "The town residents went to the Civil Guard station to ask for help during the snowfall."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué cuerpo policial vigila el tráfico en las carreteras interurbanas y garantiza la seguridad en el medio rural de la mayor parte de España?", "options": ["La Guardia Civil", "La Policía Local", "El Cuerpo de Bomberos", "El Tribunal Supremo"], "answer": "La Guardia Civil", "explanation": "La Guardia Civil actúa en el medio rural y en el control del tráfico de las vías interurbanas."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿De qué dos ministerios depende la Guardia Civil según sus funciones?", "options": ["Del Ministerio del Interior y del Ministerio de Defensa", "Del Ministerio de Justicia y del Ministerio de Cultura", "Del Ministerio de Sanidad y del Ministerio de Trabajo", "Únicamente del Ayuntamiento"], "answer": "Del Ministerio del Interior y del Ministerio de Defensa", "explanation": "Depende del Ministerio del Interior en seguridad ciudadana y del Ministerio de Defensa en ascensos y misiones militares."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Guardia Civil es un instituto armado de naturaleza ___.", "answer": "militar", "english": "The Civil Guard is an armed institute of a military nature.", "explanation": "'Naturaleza militar' defines the status of the Guardia Civil."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ es el servicio de la Guardia Civil encargado de proteger la naturaleza y el medio ambiente.", "answer": "SEPRONA", "english": "SEPRONA is the service of the Civil Guard in charge of protecting nature and the environment.", "explanation": "SEPRONA stands for Servicio de Protección de la Naturaleza."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the Guardia Civil's rural role:", "words": ["La", "Guardia", "Civil", "garantiza", "la", "seguridad", "en", "el", "medio", "rural."], "answer": "La Guardia Civil garantiza la seguridad en el medio rural.", "english": "The Civil Guard guarantees security in rural areas."},
                {"type": "dictation", "cat": "listening", "text": "La Guardia Civil vigila el tráfico en las carreteras interurbanas.", "english": "The Civil Guard monitors traffic on interurban highways."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué cuerpo tiene la competencia exclusiva en España sobre el control de licencias de armas y explosivos y el resguardo fiscal en aduanas?", "options": ["La Guardia Civil", "La Policía Local", "Protección Civil", "La Cruz Roja"], "answer": "La Guardia Civil", "explanation": "El control de armas y explosivos y el resguardo fiscal del Estado corresponden a la Guardia Civil."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En puertos y aeropuertos, la Guardia Civil ejerce el resguardo ___ del Estado contra el contrabando.", "answer": "fiscal", "english": "In ports and airports, the Civil Guard exercises the State's fiscal guard against smuggling.", "explanation": "'Resguardo fiscal del Estado'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about environmental protection:", "words": ["El", "SEPRONA", "protege", "los", "bosques", "y", "persigue", "los", "delitos", "ecológicos."], "answer": "El SEPRONA protege los bosques y persigue los delitos ecológicos.", "english": "SEPRONA protects forests and prosecutes environmental crimes."}
            ]
        },
        {
            "num": "04",
            "story_slug": "policiasautonomicas",
            "title": "Policías autonómicas y policías locales: Mossos d'Esquadra, Ertzaintza y Policía Foral",
            "goal": "Identify Spain's autonomic police forces (Mossos d'Esquadra in Catalonia, Ertzaintza in the Basque Country, Policía Foral in Navarre, Policía Canaria) and the role of municipal Policía Local.",
            "grammar_slug": "en-el-ambito-de",
            "grammar_title": "Delimitación territorial de competencias: 'en el ámbito de' y 'dentro de su municipio'",
            "grammar_summary": "Using 'en el ámbito de su comunidad' and 'dentro del término municipal' to delimit territorial jurisdiction.",
            "grammar_text": "Under Article 149.1.29 of the Constitution, Autonomous Communities may create their own police forces in accordance with their Statutes of Autonomy ('en la forma que se establezca en los respectivos Estatutos'). Consequently, distinct police forces operate within their territorial sphere ('en el ámbito de su comunidad autónoma'): the **Mossos d'Esquadra** in Catalonia, the **Ertzaintza** in the Basque Country, the **Policía Foral** in Navarre, and the **Cuerpo General de la Policía Canaria** in the Canary Islands. Meanwhile, every city council directs its **Policía Local** (or Guardia Urbana / Policía Municipal) within its municipality.",
            "grammar_examples": [
                {"spanish": "Los Mossos d'Esquadra ejercen las funciones de policía integral en el ámbito de Cataluña.", "english": "The Mossos d'Esquadra exercise full police functions within the territory of Catalonia."},
                {"spanish": "La Ertzaintza es la policía autonómica del País Vasco y la Policía Foral actúa en Navarra.", "english": "The Ertzaintza is the autonomic police of the Basque Country and the Foral Police operates in Navarre."},
                {"spanish": "La Policía Local regula el tráfico urbano y vela por el cumplimiento de las ordenanzas dentro de su municipio.", "english": "The Local Police regulates urban traffic and watches over compliance with bylaws within its municipality."}
            ],
            "grammar_tip": "CCSE favorite matching question: Mossos d'Esquadra = Cataluña; Ertzaintza = País Vasco; Policía Foral = Navarra; Policía Local/Municipal = Ayuntamientos.",
            "story_title": "Coordinación policial en cada territorio",
            "story_summary": "At a road safety congress in Pamplona, officers from the Policía Foral of Navarre, the Ertzaintza of the Basque Country, the Mossos d'Esquadra of Catalonia, and a municipal Policía Local share how they coordinate with state forces.",
            "story_location": "Pamplona",
            "story_paragraphs": [
                "El modelo policial español refleja la estructura descentralizada del Estado de las Autonomías. Junto a la Policía Nacional y la Guardia Civil, el artículo 149.1.29 de la Constitución permite la creación de policías por las comunidades autónomas en el marco de sus respectivos Estatutos.",
                "En un congreso sobre seguridad vial celebrado en Pamplona coinciden agentes de las distintas policías autonómicas de España: los Mossos d'Esquadra, que constituyen la policía autonómica de Cataluña; la Ertzaintza, policía autonómica del País Vasco; la Policía Foral (Foruzaingoa), propia de la Comunidad Foral de Navarra; y el Cuerpo General de la Policía Canaria.",
                "En Cataluña, el País Vasco y Navarra, estas policías autonómicas asumen la seguridad ciudadana ordinaria y el control del tráfico en las carreteras de su comunidad, trabajando en estrecha coordinación con las Fuerzas y Cuerpos de Seguridad del Estado a través de las Juntas de Seguridad.",
                "Por su parte, los ayuntamientos de toda España cuentan con sus propios cuerpos de Policía Local (también denominados Policía Municipal o Guardia Urbana en ciudades como Barcelona).",
                "La Policía Local depende directamente de cada alcalde y se encarga de ordenar y regular el tráfico dentro del casco urbano, vigilar los espacios públicos municipales, proteger las corporaciones locales y hacer cumplir las ordenanzas del ayuntamiento."
            ],
            "comp_questions": [
                {
                    "question": "¿Cómo se denomina la policía autonómica de Cataluña?",
                    "options": ["Mossos d'Esquadra.", "Ertzaintza.", "Policía Foral."],
                    "correctIndex": 0,
                    "explanation": "Los Mossos d'Esquadra son el cuerpo de policía autonómica de la Generalitat de Cataluña."
                },
                {
                    "question": "¿En qué comunidad autónoma ejerce sus funciones la Ertzaintza?",
                    "options": ["En el País Vasco.", "En Galicia.", "En Andalucía."],
                    "correctIndex": 0,
                    "explanation": "La Ertzaintza es la policía autonómica de la Comunidad Autónoma del País Vasco."
                },
                {
                    "question": "¿De qué autoridad depende directamente la Policía Local (o Policía Municipal) y cuál es una de sus funciones principales?",
                    "options": ["Depende del ayuntamiento (alcalde) y regula el tráfico dentro del casco urbano y el cumplimiento de las ordenanzas municipales.", "Depende del Senado y expide los pasaportes diplomáticos.", "Depende de la OTAN y vigila las fronteras internacionales."],
                    "correctIndex": 0,
                    "explanation": "La Policía Local depende de cada ayuntamiento y regula el tráfico urbano y el cumplimiento de las ordenanzas municipales."
                }
            ],
            "vocab": [
                {"lemma": "Mossos d'Esquadra", "pos": "noun", "translation": "Catalan autonomic police", "ex_es": "Los Mossos d'Esquadra son la policía autonómica de Cataluña.", "ex_en": "The Mossos d'Esquadra are the autonomic police of Catalonia."},
                {"lemma": "Ertzaintza", "pos": "noun", "translation": "Basque autonomic police", "ex_es": "La Ertzaintza vela por la seguridad ciudadana y el tráfico en el País Vasco.", "ex_en": "The Ertzaintza watches over citizen security and traffic in the Basque Country."},
                {"lemma": "Policía Foral", "pos": "noun", "translation": "Navarrese autonomic police", "ex_es": "La Policía Foral es el cuerpo policial propio de la Comunidad Foral de Navarra.", "ex_en": "The Foral Police is the police force of the Chartered Community of Navarre."},
                {"lemma": "Policía Local", "pos": "noun", "translation": "Local / Municipal Police", "ex_es": "La Policía Local regula el tráfico en las calles del municipio.", "ex_en": "The Local Police regulates traffic on the streets of the municipality."},
                {"lemma": "casco urbano", "pos": "noun", "translation": "urban center / town streets", "ex_es": "Dentro del casco urbano, la regulación del tráfico corresponde a la Policía Local.", "ex_en": "Within the town center, traffic regulation belongs to the Local Police."},
                {"lemma": "ordenanza municipal", "pos": "noun", "translation": "municipal bylaw / ordinance", "ex_es": "Los agentes locales vigilan el cumplimiento de cada ordenanza municipal sobre convivencia y ruido.", "ex_en": "Local officers monitor compliance with every municipal ordinance on coexistence and noise."},
                {"lemma": "Guardia Urbana", "pos": "noun", "translation": "Urban Guard (local police in cities like Barcelona)", "ex_es": "En Barcelona y otras ciudades catalanas, la Policía Local recibe el nombre tradicional de Guardia Urbana.", "ex_en": "In Barcelona and other Catalan cities, the Local Police receives the traditional name of Urban Guard."},
                {"lemma": "Junta de Seguridad", "pos": "noun", "translation": "Security Coordination Board", "ex_es": "La Junta de Seguridad coordina la actuación entre las policías del Estado y las autonómicas.", "ex_en": "The Security Board coordinates action between State and autonomic police forces."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo se llama la policía autonómica del País Vasco?", "options": ["Ertzaintza", "Mossos d'Esquadra", "Policía Foral", "Guardia Urbana"], "answer": "Ertzaintza", "explanation": "La Ertzaintza es la policía autonómica del País Vasco; los Mossos d'Esquadra son de Cataluña y la Policía Foral de Navarra."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo se llama la policía autonómica de Cataluña?", "options": ["Mossos d'Esquadra", "Ertzaintza", "Policía Foral", "SEPRONA"], "answer": "Mossos d'Esquadra", "explanation": "Los Mossos d'Esquadra son la policía autonómica de Cataluña."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En la Comunidad Foral de Navarra actúa su propia policía autonómica, denominada Policía ___.", "answer": "Foral", "english": "In the Chartered Community of Navarre its own autonomic police force operates, called the Foral Police.", "explanation": "'Policía Foral' is the autonomic police of Navarre."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "La Policía ___ depende del ayuntamiento y regula el tráfico dentro del casco urbano.", "answer": "Local", "english": "The Local Police depends on the city council and regulates traffic within the urban area.", "explanation": "'Policía Local' (or Municipal) depends on the Ayuntamiento."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Local Police duties:", "words": ["La", "Policía", "Local", "regula", "el", "tráfico", "dentro", "de", "su", "municipio."], "answer": "La Policía Local regula el tráfico dentro de su municipio.", "english": "The Local Police regulates traffic within its municipality."},
                {"type": "dictation", "cat": "listening", "text": "Los Mossos d'Esquadra y la Ertzaintza son policías autonómicas.", "english": "The Mossos d'Esquadra and the Ertzaintza are autonomic police forces."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué cuerpo policial se encarga de vigilar el cumplimiento de las ordenanzas municipales y regular el tráfico en las calles de un pueblo o ciudad?", "options": ["La Policía Local (dependiente del Ayuntamiento)", "La Armada Española", "El Tribunal Constitucional", "El Cuerpo Diplomático"], "answer": "La Policía Local (dependiente del Ayuntamiento)", "explanation": "La Policía Local depende de cada Ayuntamiento y regula el tráfico urbano y el cumplimiento de las ordenanzas."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Policía Local vela por el cumplimiento de las ___ municipales aprobadas por el Ayuntamiento.", "answer": "ordenanzas", "english": "The Local Police watches over compliance with the municipal ordinances approved by the City Council.", "explanation": "'Ordenanzas municipales' are local bylaws."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the Basque and Navarrese police:", "words": ["La", "Ertzaintza", "actúa", "en", "el", "País", "Vasco", "y", "la", "Policía", "Foral", "en", "Navarra."], "answer": "La Ertzaintza actúa en el País Vasco y la Policía Foral en Navarra.", "english": "The Ertzaintza operates in the Basque Country and the Foral Police in Navarre."}
            ]
        },
        {
            "num": "05",
            "story_slug": "emergencias112",
            "title": "Protección Civil, seguridad vial (DGT) y los teléfonos de emergencia (112 y 016)",
            "goal": "Memorize the essential emergency and public safety numbers tested on the CCSE exam: 112 (European single emergency number, free 24/7), 091 (Policía Nacional), 062 (Guardia Civil), 016 (Gender Violence helpline), and the Dirección General de Tráfico (DGT).",
            "grammar_slug": "en-caso-de-emergencia",
            "grammar_title": "Instrucciones de emergencia: 'en caso de + sustantivo' y 'sin coste alguno'",
            "grammar_summary": "Using 'en caso de emergencia' and 'sin coste alguno' for public safety procedures.",
            "grammar_text": "Public safety instructions in Spain rely on conditional prepositional phrases like 'en caso de accidente, incendio o urgencia sanitaria' (in the event of an accident, fire, or medical emergency) and 'de forma gratuita / sin coste alguno' (free of charge). Across Spain and the entire European Union, the single emergency telephone number is **112**, operating 24 hours a day, free of charge, in multiple languages. In addition, **016** provides confidential information and legal advice to victims of gender violence without leaving a trace on the phone bill ('sin dejar rastro en la factura telefónica').",
            "grammar_examples": [
                {"spanish": "En caso de emergencia sanitaria, incendio o accidente, se debe llamar inmediatamente al 112.", "english": "In case of a medical emergency, fire, or accident, one must immediately call 112."},
                {"spanish": "El teléfono 112 funciona las veinticuatro horas del día sin coste alguno en toda la Unión Europea.", "english": "The 112 telephone number operates twenty-four hours a day at no cost throughout the European Union."},
                {"spanish": "El teléfono 016 atiende a las víctimas de violencia de género y no deja rastro en la factura.", "english": "The 016 phone line assists victims of gender violence and leaves no trace on the bill."}
            ],
            "grammar_tip": "Essential CCSE phone numbers to know cold: **112** = general emergencies (police, fire, ambulance across the EU); **016** = gender violence assistance (leaves no trace on bill); **091** = Policía Nacional; **062** = Guardia Civil; **DGT** = Dirección General de Tráfico.",
            "story_title": "Una llamada que salva vidas: el 112",
            "story_summary": "Inside the 112 emergency coordination center in Madrid, operators dispatch ambulances, firefighters, police, and Civil Protection while explaining the DGT and the 016 helpline.",
            "story_location": "Madrid, Centro de Emergencias 112",
            "story_paragraphs": [
                "En una gran sala iluminada por pantallas de mapas digitales, los operadores del Centro de Emergencias 112 responden llamadas las veinticuatro horas del día, los 365 días del año.",
                "El 112 es el número único de emergencias tanto en toda España como en el conjunto de la Unión Europea. Es totalmente gratuito, puede marcarse incluso desde teléfonos móviles sin saldo o bloqueados y coordina en un solo aviso a las ambulancias sanitarias, los bomberos, Protección Civil y todos los cuerpos policiales.",
                "Además del 112 como teléfono general de urgencias, existen líneas directas específicas: el 091 para la Policía Nacional, el 062 para la Guardia Civil y el 016 para la información y asesoramiento jurídico en materia de violencia de género, una línea gratuita y confidencial que no deja rastro en la factura telefónica.",
                "En el ámbito de la circulación por carretera, la Dirección General de Tráfico (DGT), dependiente del Ministerio del Interior, es el organismo encargado de expedir los permisos de conducir, gestionar el permiso por puntos y promover la educación y seguridad vial en toda España.",
                "Cuando se produce una gran emergencia climática o natural, los servicios de Protección Civil y el 112 trabajan mano a mano con los ciudadanos, recordando que conocer estos números esenciales es un deber cívico que salva miles de vidas cada año."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es el número telefónico único y gratuito para cualquier emergencia (sanitaria, incendio o policial) en toda España y en la Unión Europea?",
                    "options": ["El 112.", "El 999.", "El 010."],
                    "correctIndex": 0,
                    "explanation": "El 112 es el número único europeo de emergencias, gratuito y operativo las 24 horas del día."
                },
                {
                    "question": "¿Qué número telefónico gratuito ofrece atención e información a las víctimas de violencia de género sin dejar rastro en la factura?",
                    "options": ["El 016.", "El 062.", "El 118."],
                    "correctIndex": 0,
                    "explanation": "El 016 es el servicio telefónico de información y asesoramiento jurídico en materia de violencia de género."
                },
                {
                    "question": "¿Qué organismo público dependiente del Ministerio del Interior expide los permisos de conducir y gestiona la seguridad vial en España?",
                    "options": ["La Dirección General de Tráfico (DGT).", "El Instituto Nacional de Estadística (INE).", "La Agencia Tributaria (AEAT)."],
                    "correctIndex": 0,
                    "explanation": "La Dirección General de Tráfico (DGT) gestiona la política vial y la expedición de los permisos de conducir."
                }
            ],
            "vocab": [
                {"lemma": "112", "pos": "noun", "translation": "112 (European single emergency number)", "ex_es": "En caso de accidente o urgencia médica, hay que llamar gratuitamente al 112.", "ex_en": "In case of an accident or medical emergency, you should call 112 free of charge."},
                {"lemma": "016", "pos": "noun", "translation": "016 (gender violence helpline)", "ex_es": "El teléfono 016 atiende a las víctimas de violencia de género sin dejar rastro en la factura.", "ex_en": "The 016 number assists victims of gender violence without leaving a trace on the phone bill."},
                {"lemma": "Dirección General de Tráfico", "pos": "noun", "translation": "Directorate-General for Traffic (DGT)", "ex_es": "La Dirección General de Tráfico (DGT) expide el permiso de conducir por puntos.", "ex_en": "The Directorate-General for Traffic (DGT) issues the points-based driving license."},
                {"lemma": "Protección Civil", "pos": "noun", "translation": "Civil Protection", "ex_es": "Protección Civil previene riesgos y coordina la ayuda a la población ante catástrofes.", "ex_en": "Civil Protection prevents risks and coordinates aid to the population in disasters."},
                {"lemma": "permiso de conducir", "pos": "noun", "translation": "driver's license", "ex_es": "Para obtener el permiso de conducir en España hay que superar un examen teórico y otro práctico en la DGT.", "ex_en": "To obtain a driver's license in Spain you must pass a theory test and a practical test at the DGT."},
                {"lemma": "bomberos", "pos": "noun", "translation": "firefighters", "ex_es": "El centro 112 moviliza de inmediato a los bomberos y a las ambulancias.", "ex_en": "The 112 center immediately mobilizes firefighters and ambulances."},
                {"lemma": "gratuito", "pos": "adjective", "translation": "free of charge", "ex_es": "El servicio de emergencias 112 es totalmente gratuito y funciona las veinticuatro horas.", "ex_en": "The 112 emergency service is completely free of charge and operates twenty-four hours a day."},
                {"lemma": "violencia de género", "pos": "noun", "translation": "gender-based violence", "ex_es": "España cuenta con juzgados específicos y con el teléfono 016 contra la violencia de género.", "ex_en": "Spain has specific courts and the 016 helpline against gender-based violence."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es el teléfono gratuito de emergencias válido en toda España y en toda la Unión Europea?", "options": ["112", "911", "010", "080"], "answer": "112", "explanation": "El 112 es el número único europeo de emergencias, gratuito y disponible las 24 horas."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿A qué número gratuito se debe llamar en España para recibir información y atención ante casos de violencia de género?", "options": ["016", "091", "062", "1004"], "answer": "016", "explanation": "El 016 es el teléfono de atención a víctimas de violencia de género y no deja rastro en la factura."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En caso de urgencia sanitaria, incendio o accidente, debemos llamar al número ___.", "answer": "112", "english": "In case of a medical emergency, fire, or accident, we should call the number 112.", "explanation": "'112' is the single emergency number."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Dirección General de ___ (DGT) es el organismo que expide los permisos de conducir.", "answer": "Tráfico", "english": "The Directorate-General for Traffic (DGT) is the body that issues driving licenses.", "explanation": "DGT = Dirección General de Tráfico."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the 112 emergency number:", "words": ["El", "teléfono", "112", "es", "gratuito", "y", "funciona", "en", "toda", "la", "Unión", "Europea."], "answer": "El teléfono 112 es gratuito y funciona en toda la Unión Europea.", "english": "The 112 telephone number is free and works throughout the European Union."},
                {"type": "dictation", "cat": "listening", "text": "El teléfono ciento doce atiende cualquier emergencia las veinticuatro horas.", "english": "The one-one-two telephone number handles any emergency twenty-four hours a day."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué organismo público gestiona la seguridad vial y el permiso de conducir por puntos en España?", "options": ["La Dirección General de Tráfico (DGT)", "El Instituto Cervantes", "El Tribunal de Cuentas", "La Junta Electoral Central"], "answer": "La Dirección General de Tráfico (DGT)", "explanation": "La DGT, dependiente del Ministerio del Interior, gestiona el tráfico y los permisos de conducir."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El teléfono ___ ofrece asesoramiento sobre violencia de género y no deja rastro en la factura.", "answer": "016", "english": "The 016 phone line offers advice on gender violence and leaves no trace on the bill.", "explanation": "'016' is the gender violence helpline."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the DGT:", "words": ["La", "Dirección", "General", "de", "Tráfico", "expide", "los", "permisos", "de", "conducir."], "answer": "La Dirección General de Tráfico expide los permisos de conducir.", "english": "The Directorate-General for Traffic issues driving licenses."}
            ]
        }
    ],
    "consolidation_exercises": [
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué tres ramas componen las Fuerzas Armadas españolas según el artículo 8 de la Constitución?", "options": ["Ejército de Tierra, Armada y Ejército del Aire y del Espacio", "Policía Nacional, Guardia Civil y Policía Local", "Congreso, Senado y Gobierno", "Tierra, Marina Mercante y Aduanas"], "answer": "Ejército de Tierra, Armada y Ejército del Aire y del Espacio", "explanation": "Artículo 8.1 de la Constitución."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Quién dirige la política de defensa y la Administración militar en España?", "options": ["El Gobierno", "El Tribunal Supremo", "El Defensor del Pueblo", "Los ayuntamientos"], "answer": "El Gobierno", "explanation": "Artículo 97 de la Constitución."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué cuerpo policial tiene competencia exclusiva para expedir el DNI y el pasaporte en España?", "options": ["La Policía Nacional", "La Guardia Civil", "La Policía Local", "Los Mossos d'Esquadra"], "answer": "La Policía Nacional", "explanation": "El Cuerpo Nacional de Policía expide el DNI, el pasaporte y la TIE."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es la naturaleza de la Guardia Civil y dónde actúa principalmente?", "options": ["Instituto armado de naturaleza militar; actúa en el medio rural y vías interurbanas", "Cuerpo civil municipal; actúa solo en parques urbanos", "Asociación voluntaria; actúa solo en el extranjero", "Órgano judicial; dicta sentencias penales"], "answer": "Instituto armado de naturaleza militar; actúa en el medio rural y vías interurbanas", "explanation": "La Guardia Civil tiene naturaleza militar y vigila el medio rural y el tráfico interurbano."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo se llaman las policías autonómicas de Cataluña, el País Vasco y Navarra?", "options": ["Mossos d'Esquadra, Ertzaintza y Policía Foral", "Guardia Civil, SEPRONA y UME", "Policía Municipal, Guardia Real y Aduanas", "DGT, Protección Civil y Cruz Roja"], "answer": "Mossos d'Esquadra, Ertzaintza y Policía Foral", "explanation": "Mossos (Cataluña), Ertzaintza (País Vasco) y Policía Foral (Navarra)."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es el teléfono único y gratuito de emergencias en toda España y la Unión Europea?", "options": ["112", "016", "911", "010"], "answer": "112", "explanation": "El 112 es el número único europeo de emergencias."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Las Fuerzas Armadas garantizan la ___ e independencia de España.", "answer": "soberanía", "english": "The Armed Forces guarantee the sovereignty and independence of Spain.", "explanation": "Artículo 8.1 de la Constitución."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Policía Nacional y la Guardia Civil dependen del Ministerio del ___.", "answer": "Interior", "english": "The National Police and the Civil Guard depend on the Ministry of the Interior.", "explanation": "'Ministerio del Interior'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ es el servicio de la Guardia Civil dedicado a la protección de la naturaleza.", "answer": "SEPRONA", "english": "SEPRONA is the Civil Guard service dedicated to nature protection.", "explanation": "Servicio de Protección de la Naturaleza."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los ___ d'Esquadra son la policía autonómica de Cataluña.", "answer": "Mossos", "english": "The Mossos d'Esquadra are the autonomic police of Catalonia.", "explanation": "'Mossos d'Esquadra'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El teléfono ___ atiende a las víctimas de violencia de género sin dejar rastro en la factura.", "answer": "016", "english": "The 016 phone line assists victims of gender violence without leaving a trace on the bill.", "explanation": "'016'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Dirección General de ___ (DGT) expide los permisos de conducir en España.", "answer": "Tráfico", "english": "The Directorate-General for Traffic (DGT) issues driver's licenses in Spain.", "explanation": "'Dirección General de Tráfico'."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the Armed Forces:", "words": ["Las", "Fuerzas", "Armadas", "defienden", "la", "integridad", "territorial", "de", "España."], "answer": "Las Fuerzas Armadas defienden la integridad territorial de España.", "english": "The Armed Forces defend the territorial integrity of Spain."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about DNI issuance:", "words": ["La", "Policía", "Nacional", "es", "encargada", "de", "expedir", "el", "DNI", "y", "el", "pasaporte."], "answer": "La Policía Nacional es encargada de expedir el DNI y el pasaporte.", "english": "The National Police is in charge of issuing the DNI and the passport."},
        {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Order the sentence about emergency number 112:", "words": ["En", "caso", "de", "emergencia", "debemos", "llamar", "al", "teléfono", "gratuito", "112."], "answer": "En caso de emergencia debemos llamar al teléfono gratuito 112.", "english": "In case of emergency we should call the free phone number 112."},
        {"type": "dictation", "cat": "listening", "text": "La Policía Nacional expide el documento nacional de identidad y el pasaporte.", "english": "The National Police issues the national identity document and the passport."},
        {"type": "dictation", "cat": "listening", "text": "La Ertzaintza es la policía autonómica del País Vasco.", "english": "The Ertzaintza is the autonomic police of the Basque Country."},
        {"type": "dictation", "cat": "listening", "text": "El ciento doce es el teléfono único de emergencias en toda Europa.", "english": "One-one-two is the single emergency phone number throughout Europe."}
    ]
}

UNIT_9 = {
    "slug": "unioneuropea",
    "legacy_prefix": "b1-ccse-union-europea",
    "unit_title": "España en la Unión Europea",
    "order": 9,
    "unit_summary": "Complete CCSE guide to Spain in the European Union: the 1985 Madrid Treaty of Accession and entry on January 1, 1986; the Euro (in circulation since January 1, 2002) and the Schengen Area; EU institutions (European Parliament, Commission, Council, CJEU, ECB); Europe Day (May 9) and EU symbols; and the rights of European citizenship and Erasmus+.",
    "unit_paragraphs": [],
    "unit_questions": [],
    "lessons": [
        {
            "num": "01",
            "story_slug": "adhesion1986",
            "title": "La adhesión de España a las Comunidades Europeas (1985-1986)",
            "goal": "Know the historical dates and milestones of Spain's integration into the European Union: the signing of the Treaty of Accession in the Royal Palace of Madrid on June 12, 1985, and official entry on January 1, 1986.",
            "grammar_slug": "desde-su-ingreso-en",
            "grammar_title": "Hitos históricos y cronología: 'firmar el tratado el + fecha' y 'desde su ingreso en + año'",
            "grammar_summary": "Expressing historical dates and treaty milestones ('el 12 de junio de 1985', 'desde su ingreso el 1 de enero de 1986').",
            "grammar_text": "Historical and institutional milestones in Spanish use 'el + día + de + mes + de + año' for exact dates and 'en + año / desde su ingreso en + año' for years. On June 12, 1985 ('el 12 de junio de 1985'), Spain signed the Treaty of Accession ('el Tratado de Adhesión') in the Salón de Columnas of the Royal Palace of Madrid, and on January 1, 1986 ('el 1 de enero de 1986'), Spain and Portugal became full members of the European Communities (today the 27-member European Union).",
            "grammar_examples": [
                {"spanish": "España firmó el Tratado de Adhesión en el Palacio Real de Madrid el 12 de junio de 1985.", "english": "Spain signed the Treaty of Accession at the Royal Palace of Madrid on June 12, 1985."},
                {"spanish": "España es Estado miembro de pleno derecho de la Unión Europea desde el 1 de enero de 1986.", "english": "Spain has been a full Member State of the European Union since January 1, 1986."},
                {"spanish": "Desde su ingreso en 1986, España ha presidido el Consejo de la Unión Europea en cinco ocasiones.", "english": "Since its entry in 1986, Spain has held the presidency of the Council of the European Union five times."}
            ],
            "grammar_tip": "Memorize the year **1986** (January 1, 1986) as the year Spain joined the European Union (together with Portugal), and **27** as the current number of EU member states.",
            "story_title": "El Salón de Columnas y el 1 de enero de 1986",
            "story_summary": "A historian recalls the solemn signing of the Treaty of Accession in the Royal Palace of Madrid on June 12, 1985, and Spain's entry into the European Communities on January 1, 1986.",
            "story_location": "Madrid, Salón de Columnas del Palacio Real",
            "story_paragraphs": [
                "Tras recuperar la democracia con la Constitución de 1978, uno de los grandes objetivos históricos de la sociedad española fue reincorporarse plenamente al proyecto común europeo.",
                "El 12 de junio de 1985, en una solemne ceremonia celebrada en el Salón de Columnas del Palacio Real de Madrid, el presidente del Gobierno, Felipe González, firmó el Tratado de Adhesión de España a las entonces llamadas Comunidades Europeas.",
                "Pocos meses después, el 1 de enero de 1986, España —junto con Portugal— se convirtió oficialmente en Estado miembro de pleno derecho, pasando la comunidad europea de diez a doce países.",
                "Con el Tratado de Maastricht, firmado en 1992, las Comunidades Europeas adoptaron la denominación actual de Unión Europea y crearon el estatuto de la ciudadanía europea para todos los nacionales de sus Estados miembros.",
                "En la actualidad, la Unión Europea está integrada por veintisiete Estados miembros democráticos, y España ha ejercido la presidencia rotatoria del Consejo de la Unión Europea en cinco ocasiones: 1989, 1995, 2002, 2010 y 2023."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué fecha ingresó oficialmente España como miembro de pleno derecho en las Comunidades Europeas (actual Unión Europea)?",
                    "options": ["El 1 de enero de 1986.", "El 6 de diciembre de 1978.", "El 1 de enero de 2002."],
                    "correctIndex": 0,
                    "explanation": "España firmó el Tratado de Adhesión el 12 de junio de 1985 e ingresó oficialmente el 1 de enero de 1986 junto con Portugal."
                },
                {
                    "question": "¿Con qué otro país ibérico ingresó España simultáneamente en las Comunidades Europeas en 1986?",
                    "options": ["Con Portugal.", "Con Suiza.", "Con Noruega."],
                    "correctIndex": 0,
                    "explanation": "España y Portugal ingresaron juntos el 1 de enero de 1986."
                },
                {
                    "question": "¿Cuántos Estados miembros integran actualmente la Unión Europea?",
                    "options": ["27 Estados miembros.", "15 Estados miembros.", "50 Estados miembros."],
                    "correctIndex": 0,
                    "explanation": "Actualmente la Unión Europea está compuesta por 27 Estados miembros."
                }
            ],
            "vocab": [
                {"lemma": "Tratado de Adhesión", "pos": "noun", "translation": "Treaty of Accession", "ex_es": "España firmó el Tratado de Adhesión en el Palacio Real de Madrid en 1985.", "ex_en": "Spain signed the Treaty of Accession at the Royal Palace of Madrid in 1985."},
                {"lemma": "Estado miembro", "pos": "noun", "translation": "Member State", "ex_es": "España es Estado miembro de la Unión Europea desde el 1 de enero de 1986.", "ex_en": "Spain has been a Member State of the European Union since January 1, 1986."},
                {"lemma": "Unión Europea", "pos": "noun", "translation": "European Union (EU)", "ex_es": "La Unión Europea está formada actualmente por veintisiete países democráticos.", "ex_en": "The European Union is currently made up of twenty-seven democratic countries."},
                {"lemma": "Tratado de Maastricht", "pos": "noun", "translation": "Treaty of Maastricht (1992)", "ex_es": "El Tratado de Maastricht de 1992 instituyó la ciudadanía europea y preparó la moneda única.", "ex_en": "The 1992 Treaty of Maastricht established European citizenship and prepared the single currency."},
                {"lemma": "pleno derecho", "pos": "noun", "translation": "full right / full membership", "ex_es": "En 1986 España se integró como socio europeo de pleno derecho.", "ex_en": "In 1986 Spain joined as a full European partner."},
                {"lemma": "presidencia rotatoria", "pos": "noun", "translation": "rotating presidency", "ex_es": "Cada seis meses un país asume la presidencia rotatoria del Consejo de la Unión Europea.", "ex_en": "Every six months a country assumes the rotating presidency of the Council of the European Union."},
                {"lemma": "integración", "pos": "noun", "translation": "integration", "ex_es": "La integración europea impulsó la modernización de las infraestructuras españolas.", "ex_en": "European integration boosted the modernization of Spanish infrastructure."},
                {"lemma": "ciudadanía europea", "pos": "noun", "translation": "European citizenship", "ex_es": "Toda persona que ostente la nacionalidad de un Estado miembro tiene la ciudadanía europea.", "ex_en": "Every person who holds the nationality of a Member State has European citizenship."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué año ingresó España en la Comunidad Económica Europea (actual Unión Europea)?", "options": ["En 1986", "En 1978", "En 1992", "En 2002"], "answer": "En 1986", "explanation": "España ingresó oficialmente el 1 de enero de 1986 (tras firmar el Tratado de Adhesión el 12 de junio de 1985)."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántos países forman parte actualmente de la Unión Europea?", "options": ["27 países", "12 países", "19 países", "35 países"], "answer": "27 países", "explanation": "La Unión Europea cuenta actualmente con 27 Estados miembros."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "España firmó el Tratado de ___ en el Palacio Real de Madrid en junio de 1985.", "answer": "Adhesión", "english": "Spain signed the Treaty of Accession at the Royal Palace of Madrid in June 1985.", "explanation": "'Tratado de Adhesión' is the Treaty of Accession."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "España es ___ miembro de la Unión Europea desde el 1 de enero de 1986.", "answer": "Estado", "english": "Spain has been a Member State of the European Union since January 1, 1986.", "explanation": "'Estado miembro' means Member State."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the historical sentence about Spain's entry into the EU:", "words": ["España", "ingresó", "en", "la", "Unión", "Europea", "el", "uno", "de", "enero", "de", "1986."], "answer": "España ingresó en la Unión Europea el uno de enero de 1986.", "english": "Spain joined the European Union on January 1, 1986."},
                {"type": "dictation", "cat": "listening", "text": "España forma parte de la Unión Europea desde el año mil novecientos ochenta y seis.", "english": "Spain has been part of the European Union since the year nineteen eighty-six."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué tratado europeo firmado en 1992 dio nombre a la Unión Europea y creó la ciudadanía europea?", "options": ["El Tratado de Maastricht", "El Tratado de Versalles", "El Tratado de Tordesillas", "El Pacto de Toledo"], "answer": "El Tratado de Maastricht", "explanation": "El Tratado de la Unión Europea (Tratado de Maastricht, 1992) creó la ciudadanía de la Unión y sentó las bases del euro."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Toda persona con nacionalidad española posee también la ___ europea.", "answer": "ciudadanía", "english": "Every person with Spanish nationality also holds European citizenship.", "explanation": "'Ciudadanía europea'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the 27 EU countries:", "words": ["La", "Unión", "Europea", "está", "compuesta", "actualmente", "por", "veintisiete", "Estados", "miembros."], "answer": "La Unión Europea está compuesta actualmente por veintisiete Estados miembros.", "english": "The European Union is currently composed of twenty-seven Member States."}
            ]
        },
        {
            "num": "02",
            "story_slug": "euroschengen",
            "title": "La moneda única (el euro) y la libre circulación en el espacio Schengen",
            "goal": "Know when the euro replaced the peseta in physical circulation (January 1, 2002), the role of the European Central Bank, and free movement across the Schengen Area.",
            "grammar_slug": "sustituir-a-entrar-en-circulacion",
            "grammar_title": "Cambio monetario y circulación: 'entrar en circulación' y 'sustituir a'",
            "grammar_summary": "Using 'entrar en circulación el 1 de enero de 2002' and 'sustituir a la peseta' to describe monetary transition.",
            "grammar_text": "To describe currency transitions and border rules, Spanish uses 'entrar en circulación' (to enter physical circulation) and 'sustituir a' (to replace, always taking the preposition 'a' before the replaced noun). While the euro was born as an accounting currency in 1999, euro banknotes and coins entered physical circulation in Spain on January 1, 2002 ('entraron en circulación el 1 de enero de 2002'), replacing the historic Spanish currency, the peseta ('sustituyendo a la peseta', which had been Spain's official currency since 1868).",
            "grammar_examples": [
                {"spanish": "Los billetes y monedas de euro entraron en circulación en España el 1 de enero de 2002.", "english": "Euro banknotes and coins entered circulation in Spain on January 1, 2002."},
                {"spanish": "El euro sustituyó a la peseta como moneda oficial de España.", "english": "The euro replaced the peseta as the official currency of Spain."},
                {"spanish": "El acuerdo de Schengen permite viajar entre los países firmantes sin controles en las fronteras interiores.", "english": "The Schengen Agreement allows travel between signatory countries without checks at internal borders."}
            ],
            "grammar_tip": "Don't confuse the two CCSE years: **1986** = Spain joins the EU; **2002** (January 1, 2002) = euro coins and banknotes enter circulation in Spain, replacing the **peseta**.",
            "story_title": "De la peseta al euro y las fronteras abiertas",
            "story_summary": "A Madrid shopkeeper shows his grandchildren a collection of old silver and aluminum pesetas and remembers New Year's Day 2002 when the euro entered everyday life.",
            "story_location": "Madrid",
            "story_paragraphs": [
                "En una caja metálica de su comercio en Madrid, don Emilio conserva billetes antiguos con la efigie de escritores españoles y monedas doradas llamadas «rubias». Son pesetas, la moneda oficial de España desde 1868 hasta la llegada del euro.",
                "Aunque el euro nació como moneda financiera y contable el 1 de enero de 1999, los billetes y monedas de euro entraron físicamente en circulación en España el 1 de enero de 2002, sustituyendo definitivamente a la peseta a un tipo de cambio fijo de 166,386 pesetas por cada euro.",
                "España forma parte desde su origen de la llamada eurozona (o zona del euro), cuya política monetaria y estabilidad de precios dirige el Banco Central Europeo (BCE), con sede en la ciudad alemana de Fráncfort.",
                "Junto a la moneda única, otro pilar cotidiano de la integración europea es el espacio Schengen, al que España se adhirió en 1991. Dentro del espacio Schengen se han suprimido los controles en las fronteras interiores, de modo que los ciudadanos pueden cruzar libremente de España a Francia, Portugal o Alemania utilizando simplemente su DNI en vigor.",
                "La combinación del mercado único, la moneda común y el espacio Schengen facilita a millones de españoles y europeos viajar, comerciar, trabajar o jubilarse en cualquier rincón del continente sin aduanas ni cambios de divisa."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál era la moneda oficial de España antes de la entrada en circulación del euro en el año 2002?",
                    "options": ["La peseta.", "El escudo.", "El marco."],
                    "correctIndex": 0,
                    "explanation": "La peseta fue la moneda oficial de España desde 1868 hasta su sustitución por el euro en 2002."
                },
                {
                    "question": "¿En qué fecha entraron físicamente en circulación los billetes y monedas de euro en España?",
                    "options": ["El 1 de enero de 2002.", "El 1 de enero de 1986.", "El 12 de octubre de 1992."],
                    "correctIndex": 0,
                    "explanation": "Los billetes y monedas de euro comenzaron a circular físicamente en España el 1 de enero de 2002."
                },
                {
                    "question": "¿Qué documento necesita un ciudadano español para viajar a otro país de la Unión Europea o del espacio Schengen?",
                    "options": ["El Documento Nacional de Identidad (DNI) o el pasaporte en vigor.", "Un visado consular obligatorio expedido por el Senado.", "El libro de familia sellado por el alcalde."],
                    "correctIndex": 0,
                    "explanation": "Los ciudadanos españoles pueden viajar por toda la Unión Europea y el espacio Schengen con su DNI en vigor (o su pasaporte)."
                }
            ],
            "vocab": [
                {"lemma": "euro", "pos": "noun", "translation": "euro", "ex_es": "El euro entró en circulación física en España el 1 de enero de 2002.", "ex_en": "The euro entered physical circulation in Spain on January 1, 2002."},
                {"lemma": "peseta", "pos": "noun", "translation": "peseta (former Spanish currency)", "ex_es": "El euro sustituyó a la peseta como moneda oficial de España en 2002.", "ex_en": "The euro replaced the peseta as Spain's official currency in 2002."},
                {"lemma": "espacio Schengen", "pos": "noun", "translation": "Schengen Area", "ex_es": "El espacio Schengen permite viajar entre los países europeos sin controles fronterizos interiores.", "ex_en": "The Schengen Area allows travel between European countries without internal border checks."},
                {"lemma": "eurozona", "pos": "noun", "translation": "eurozone", "ex_es": "La eurozona agrupa a los Estados miembros de la UE que han adoptado el euro como moneda.", "ex_en": "The eurozone groups the EU Member States that have adopted the euro as their currency."},
                {"lemma": "Banco Central Europeo", "pos": "noun", "translation": "European Central Bank (ECB)", "ex_es": "El Banco Central Europeo gestiona el euro y mantiene la estabilidad de los precios.", "ex_en": "The European Central Bank manages the euro and maintains price stability."},
                {"lemma": "libre circulación", "pos": "noun", "translation": "free movement", "ex_es": "La Unión Europea garantiza la libre circulación de personas, mercancías, servicios y capitales.", "ex_en": "The European Union guarantees the free movement of persons, goods, services, and capital."},
                {"lemma": "frontera interior", "pos": "noun", "translation": "internal border", "ex_es": "Entre España y Portugal o Francia no existen controles permanentes en la frontera interior.", "ex_en": "Between Spain and Portugal or France there are no permanent checks at the internal border."},
                {"lemma": "moneda única", "pos": "noun", "translation": "single currency", "ex_es": "La moneda única facilita el comercio y el turismo entre los países europeos.", "ex_en": "The single currency facilitates trade and tourism among European countries."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué año entraron en circulación los billetes y monedas de euro en España?", "options": ["En 2002", "En 1986", "En 1978", "En 2010"], "answer": "En 2002", "explanation": "Los billetes y monedas de euro entraron en circulación el 1 de enero de 2002."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué moneda oficial utilizaba España antes del euro?", "options": ["La peseta", "La lira", "El franco", "El escudo"], "answer": "La peseta", "explanation": "La peseta fue la moneda española sustituida por el euro en 2002."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El 1 de enero de 2002 el euro sustituyó a la ___ en España.", "answer": "peseta", "english": "On January 1, 2002, the euro replaced the peseta in Spain.", "explanation": "'La peseta' was Spain's previous currency."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El acuerdo de ___ suprime los controles en las fronteras interiores entre los países europeos firmantes.", "answer": "Schengen", "english": "The Schengen agreement abolishes controls at internal borders between signatory European countries.", "explanation": "'Espacio Schengen' enables border-free travel."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the introduction of the euro:", "words": ["El", "euro", "sustituyó", "a", "la", "peseta", "en", "el", "año", "2002."], "answer": "El euro sustituyó a la peseta en el año 2002.", "english": "The euro replaced the peseta in the year 2002."},
                {"type": "dictation", "cat": "listening", "text": "El euro es la moneda oficial de España desde el año dos mil dos.", "english": "The euro has been the official currency of Spain since the year two thousand and two."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Con qué documento oficial puede viajar un ciudadano español por los países de la Unión Europea?", "options": ["Con su DNI en vigor (o pasaporte)", "Únicamente con visado de trabajo", "Con el certificado de empadronamiento", "Con la tarjeta sanitaria exclusivamente"], "answer": "Con su DNI en vigor (o pasaporte)", "explanation": "Dentro de la Unión Europea y del espacio Schengen, los españoles pueden viajar con su DNI en vigor."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Banco ___ Europeo (BCE) dirige la política monetaria de la zona del euro.", "answer": "Central", "english": "The European Central Bank (ECB) directs the monetary policy of the euro area.", "explanation": "'Banco Central Europeo'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about free movement in the EU:", "words": ["La", "Unión", "Europea", "garantiza", "la", "libre", "circulación", "de", "personas", "y", "mercancías."], "answer": "La Unión Europea garantiza la libre circulación de personas y mercancías.", "english": "The European Union guarantees the free movement of people and goods."}
            ]
        },
        {
            "num": "03",
            "story_slug": "institucionesue",
            "title": "Las instituciones de la Unión Europea: Parlamento, Comisión y Consejo",
            "goal": "Distinguish the main institutions of the European Union and their seats: the European Parliament (elected directly by citizens every 5 years), the European Commission (executive), the Council of the EU, the European Council, and the Court of Justice.",
            "grammar_slug": "encargado-de-velar-por",
            "grammar_title": "Atribución institucional europea: 'encargado de + infinitivo' y 'con sede en'",
            "grammar_summary": "Using 'órgano encargado de + infinitivo' and 'con sede en Bruselas/Estrasburgo' to describe EU institutions.",
            "grammar_text": "To describe European institutions, Spanish uses 'órgano encargado de + infinitivo' (body in charge of...) and 'con sede en + ciudad' (headquartered in...). Note the difference between the **Parlamento Europeo** (elected directly by EU citizens every 5 years, with seats in Strasbourg and Brussels), the **Comisión Europea** (the executive body in Brussels that proposes EU laws and watches over the treaties), the **Consejo Europeo** (summits of Heads of State or Government), and the **Consejo de la Unión Europea** (where ministers from the 27 member states vote on laws alongside the Parliament).",
            "grammar_examples": [
                {"spanish": "El Parlamento Europeo es la única institución de la Unión elegida directamente por los ciudadanos cada cinco años.", "english": "The European Parliament is the only institution of the Union elected directly by citizens every five years."},
                {"spanish": "La Comisión Europea, con sede en Bruselas, es el órgano ejecutivo encargado de proponer las leyes comunitarias.", "english": "The European Commission, headquartered in Brussels, is the executive body in charge of proposing EU laws."},
                {"spanish": "El Tribunal de Justicia de la Unión Europea tiene su sede en Luxemburgo.", "english": "The Court of Justice of the European Union has its seat in Luxembourg."}
            ],
            "grammar_tip": "Be careful not to confuse the two Councils: **Consejo Europeo** = Heads of State or Government (e.g. Spain's Prime Minister); **Consejo de la Unión Europea** = sectorial Ministers of the 27 countries.",
            "story_title": "Bruselas, Estrasburgo y Luxemburgo",
            "story_summary": "A Spanish trainee at the European Parliament in Brussels guides visitors through how laws are proposed by the European Commission and approved by the Parliament and the Council of the EU.",
            "story_location": "Bruselas y Estrasburgo",
            "story_paragraphs": [
                "La arquitectura institucional de la Unión Europea combina la representación directa de los ciudadanos, el interés común europeo y la voz de los gobiernos nacionales de los veintisiete Estados miembros.",
                "El Parlamento Europeo —con sedes en Estrasburgo y Bruselas— es la única institución europea elegida por sufragio universal directo cada cinco años. Sus eurodiputados aprueban las leyes europeas y el presupuesto común conjuntamente con el Consejo de la Unión Europea.",
                "La Comisión Europea, con sede en Bruselas e integrada por un comisario de cada Estado miembro, actúa como poder ejecutivo de la Unión: tiene la iniciativa legislativa para proponer nuevas directivas y reglamentos, ejecuta las políticas comunes y vigila el cumplimiento de los tratados.",
                "Por su parte, el Consejo Europeo reúne a los jefes de Estado o de Gobierno de los veintisiete países (en el caso de España, acude el Presidente del Gobierno) para fijar las grandes prioridades políticas de la Unión, mientras que el Consejo de la Unión Europea reúne a los ministros de cada ramo para legislar.",
                "El sistema se completa con el Tribunal de Justicia de la Unión Europea (con sede en Luxemburgo), que garantiza que el Derecho europeo se interprete y aplique por igual en todos los países, y el Banco Central Europeo (en Fráncfort)."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la única institución de la Unión Europea cuyos miembros son elegidos directamente en las urnas por los ciudadanos cada cinco años?",
                    "options": ["El Parlamento Europeo.", "La Comisión Europea.", "El Banco Central Europeo."],
                    "correctIndex": 0,
                    "explanation": "Los ciudadanos de la UE eligen directamente a los eurodiputados del Parlamento Europeo cada cinco años."
                },
                {
                    "question": "¿Qué institución actúa como órgano ejecutivo de la Unión Europea, propone nuevas leyes comunitarias y vela por el cumplimiento de los tratados?",
                    "options": ["La Comisión Europea (con sede en Bruselas).", "El Tribunal Constitucional español.", "El Consejo de Europa."],
                    "correctIndex": 0,
                    "explanation": "La Comisión Europea es el órgano ejecutivo de la UE con iniciativa legislativa y sede principal en Bruselas."
                },
                {
                    "question": "¿Quién representa a España en las cumbres del Consejo Europeo de jefes de Estado o de Gobierno?",
                    "options": ["El Presidente del Gobierno.", "El Fiscal General del Estado.", "El Presidente del Tribunal Supremo."],
                    "correctIndex": 0,
                    "explanation": "En las reuniones del Consejo Europeo, España está representada por el Presidente del Gobierno."
                }
            ],
            "vocab": [
                {"lemma": "Parlamento Europeo", "pos": "noun", "translation": "European Parliament", "ex_es": "El Parlamento Europeo se elige por sufragio universal cada cinco años.", "ex_en": "The European Parliament is elected by universal suffrage every five years."},
                {"lemma": "Comisión Europea", "pos": "noun", "translation": "European Commission", "ex_es": "La Comisión Europea es el órgano ejecutivo de la Unión y propone las normas europeas.", "ex_en": "The European Commission is the executive body of the Union and proposes European rules."},
                {"lemma": "Consejo Europeo", "pos": "noun", "translation": "European Council", "ex_es": "El Consejo Europeo reúne a los jefes de Estado o de Gobierno de los veintisiete países.", "ex_en": "The European Council brings together the Heads of State or Government of the twenty-seven countries."},
                {"lemma": "Consejo de la Unión Europea", "pos": "noun", "translation": "Council of the European Union", "ex_es": "En el Consejo de la Unión Europea se reúnen los ministros de los Estados miembros para aprobar leyes.", "ex_en": "In the Council of the European Union the ministers of the Member States meet to approve laws."},
                {"lemma": "comisario europeo", "pos": "noun", "translation": "European Commissioner", "ex_es": "Cada uno de los veintisiete Estados miembros cuenta con un comisario europeo en la Comisión.", "ex_en": "Each of the twenty-seven Member States has one European Commissioner in the Commission."},
                {"lemma": "directiva", "pos": "noun", "translation": "EU directive", "ex_es": "Cada directiva europea aprobada debe incorporarse a las leyes nacionales de los Estados miembros.", "ex_en": "Every approved European directive must be incorporated into the national laws of the Member States."},
                {"lemma": "Bruselas", "pos": "noun", "translation": "Brussels", "ex_es": "La Comisión Europea y el Consejo Europeo tienen su sede principal en Bruselas.", "ex_en": "The European Commission and the European Council have their main seat in Brussels."},
                {"lemma": "Estrasburgo", "pos": "noun", "translation": "Strasbourg", "ex_es": "La sede oficial de los plenos del Parlamento Europeo se encuentra en Estrasburgo.", "ex_en": "The official seat of the plenary sessions of the European Parliament is in Strasbourg."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cada cuántos años eligen los ciudadanos a los diputados del Parlamento Europeo?", "options": ["Cada 5 años", "Cada 4 años", "Cada 2 años", "Cada 10 años"], "answer": "Cada 5 años", "explanation": "Las elecciones al Parlamento Europeo se celebran cada 5 años en todos los Estados miembros."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es el órgano ejecutivo de la Unión Europea encargado de proponer nuevas leyes y velar por el cumplimiento de los tratados?", "options": ["La Comisión Europea", "El Parlamento Europeo", "El Tribunal de Cuentas", "La OTAN"], "answer": "La Comisión Europea", "explanation": "La Comisión Europea es el poder ejecutivo de la UE y tiene la iniciativa legislativa."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ Europeo es la única institución de la UE elegida directamente por los ciudadanos.", "answer": "Parlamento", "english": "The European Parliament is the only EU institution elected directly by citizens.", "explanation": "'El Parlamento Europeo'."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La ___ Europea tiene su sede principal en Bruselas y está formada por 27 comisarios.", "answer": "Comisión", "english": "The European Commission has its main seat in Brussels and is made up of 27 commissioners.", "explanation": "'La Comisión Europea'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about European elections:", "words": ["Las", "elecciones", "al", "Parlamento", "Europeo", "se", "celebran", "cada", "cinco", "años."], "answer": "Las elecciones al Parlamento Europeo se celebran cada cinco años.", "english": "Elections to the European Parliament are held every five years."},
                {"type": "dictation", "cat": "listening", "text": "La Comisión Europea es el órgano ejecutivo de la Unión Europea.", "english": "The European Commission is the executive body of the European Union."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Quién representa a España en las reuniones del Consejo Europeo?", "options": ["El Presidente del Gobierno", "El Defensor del Pueblo", "El Alcalde de Madrid", "El Fiscal General"], "answer": "El Presidente del Gobierno", "explanation": "El Consejo Europeo reúne a los jefes de Estado o de Gobierno; por España asiste el Presidente del Gobierno."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En el ___ Europeo se reúnen los jefes de Estado o de Gobierno de los veintisiete países.", "answer": "Consejo", "english": "In the European Council the Heads of State or Government of the twenty-seven countries meet.", "explanation": "'El Consejo Europeo'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the European Parliament and Council:", "words": ["El", "Parlamento", "Europeo", "aprueba", "las", "leyes", "junto", "con", "el", "Consejo."], "answer": "El Parlamento Europeo aprueba las leyes junto con el Consejo.", "english": "The European Parliament approves laws together with the Council."}
            ]
        },
        {
            "num": "04",
            "story_slug": "simbolosue",
            "title": "Los símbolos de la Unión Europea y el Día de Europa (9 de mayo)",
            "goal": "Know the symbols of the European Union: the blue flag with 12 golden stars, the anthem ('Oda a la Alegría' from Beethoven's Ninth Symphony), the motto ('Unida en la diversidad'), and Europe Day on May 9 (Schuman Declaration).",
            "grammar_slug": "en-conmemoracion-de",
            "grammar_title": "Conmemoraciones y simbolismo: 'en conmemoración de' y 'representar la unidad'",
            "grammar_summary": "Using 'en conmemoración de' and 'simbolizar la armonía y solidaridad' for civic dates and symbols.",
            "grammar_text": "To explain historical commemorations and civic emblems, Spanish uses 'en conmemoración de' (in commemoration of) and verbs like 'simbolizar / representar' (to symbolize / represent). On May 9 ('el 9 de mayo') Europe celebrates **el Día de Europa** in commemoration of the 1950 Schuman Declaration ('en conmemoración de la Declaración Schuman de 1950'), which initiated European integration. Notice that the **12 golden stars** on the blue European flag do NOT depend on the number of member states (currently 27), but symbolize perfection, completeness, and unity.",
            "grammar_examples": [
                {"spanish": "El 9 de mayo se celebra el Día de Europa en conmemoración de la Declaración Schuman de 1950.", "english": "On May 9 Europe Day is celebrated in commemoration of the 1950 Schuman Declaration."},
                {"spanish": "La bandera europea tiene doce estrellas doradas en círculo sobre fondo azul que simbolizan la unidad.", "english": "The European flag has twelve golden stars in a circle on a blue background symbolizing unity."},
                {"spanish": "El himno europeo es la 'Oda a la Alegría' de la Novena Sinfonía de Beethoven.", "english": "The European anthem is the 'Ode to Joy' from Beethoven's Ninth Symphony."}
            ],
            "grammar_tip": "Classic CCSE trap: How many stars are on the European Union flag? Always **12** golden stars in a circle on a blue background (never 27!). And Europe Day is **9 de mayo**.",
            "story_title": "Doce estrellas doradas el 9 de mayo",
            "story_summary": "On May 9—Europe Day—a youth orchestra in Granada performs Beethoven's Ode to Joy beneath the Spanish and European flags while explaining the meaning of the 12 stars and the EU motto.",
            "story_location": "Granada",
            "story_paragraphs": [
                "Cada 9 de mayo, los edificios públicos de España y del resto de los veintisiete Estados miembros celebran el Día de Europa en conmemoración de la histórica Declaración pronunciada por el ministro francés Robert Schuman el 9 de mayo de 1950, considerada el acto de nacimiento de la actual Unión Europea.",
                "Junto a la bandera rojigualda española ondea en todos los ayuntamientos, ministerios y colegios la bandera de la Unión Europea: un círculo de doce estrellas doradas sobre un fondo azul.",
                "Un error frecuente es pensar que cada estrella representa a un país miembro. En realidad, el número de estrellas es fijo —siempre doce— porque el doce es el símbolo tradicional de la perfección, la plenitud y la unidad, y el círculo representa la solidaridad y la armonía entre los pueblos de Europa.",
                "En la plaza del Ayuntamiento de Granada, una joven orquesta interpreta el himno europeo: la melodía de la «Oda a la Alegría», compuesta por Ludwig van Beethoven en 1823 para el movimiento final de su Novena Sinfonía. Al igual que el himno español, el himno oficial europeo se interpreta sin letra en los actos institucionales para emplear el lenguaje universal de la música.",
                "Bajo las banderas se lee el lema oficial de la Unión Europea, «Unida en la diversidad», que resume cómo quinientos millones de europeos cooperan por la paz y la prosperidad manteniendo vivas sus distintas culturas, tradiciones y veinticuatro lenguas oficiales."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué día del año se celebra el Día de Europa en España y en toda la Unión Europea?",
                    "options": ["El 9 de mayo.", "El 6 de diciembre.", "El 12 de octubre."],
                    "correctIndex": 0,
                    "explanation": "El Día de Europa se celebra cada 9 de mayo en recuerdo de la Declaración Schuman del 9 de mayo de 1950."
                },
                {
                    "question": "¿Cómo es la bandera oficial de la Unión Europea?",
                    "options": ["Un círculo de doce estrellas doradas sobre fondo azul.", "Veintisiete estrellas blancas sobre fondo verde.", "Tres franjas horizontales roja, blanca y azul."],
                    "correctIndex": 0,
                    "explanation": "La bandera europea está formada por un círculo de 12 estrellas doradas sobre fondo azul."
                },
                {
                    "question": "¿Cuál es el lema oficial de la Unión Europea?",
                    "options": ["«Unida en la diversidad».", "«Plus Ultra».", "«Libertad, igualdad, fraternidad»."],
                    "correctIndex": 0,
                    "explanation": "El lema de la Unión Europea es «Unida en la diversidad»."
                }
            ],
            "vocab": [
                {"lemma": "Día de Europa", "pos": "noun", "translation": "Europe Day (May 9)", "ex_es": "El Día de Europa se celebra el 9 de mayo en todos los Estados miembros.", "ex_en": "Europe Day is celebrated on May 9 in all Member States."},
                {"lemma": "doce estrellas", "pos": "noun", "translation": "twelve stars (on the EU flag)", "ex_es": "La bandera europea muestra doce estrellas doradas dispuestas en círculo sobre fondo azul.", "ex_en": "The European flag shows twelve golden stars arranged in a circle on a blue background."},
                {"lemma": "Oda a la Alegría", "pos": "noun", "translation": "Ode to Joy (European anthem)", "ex_es": "El himno de la Unión Europea es la 'Oda a la Alegría' de Beethoven.", "ex_en": "The anthem of the European Union is Beethoven's 'Ode to Joy'."},
                {"lemma": "Unida en la diversidad", "pos": "noun", "translation": "United in diversity (EU motto)", "ex_es": "El lema 'Unida en la diversidad' destaca la riqueza cultural y lingüística europea.", "ex_en": "The motto 'United in diversity' highlights European cultural and linguistic richness."},
                {"lemma": "Declaración Schuman", "pos": "noun", "translation": "Schuman Declaration (May 9, 1950)", "ex_es": "La Declaración Schuman de 1950 puso la primera piedra de la integración europea.", "ex_en": "The 1950 Schuman Declaration laid the cornerstone of European integration."},
                {"lemma": "armonía", "pos": "noun", "translation": "harmony", "ex_es": "El círculo de estrellas simboliza la unidad, la solidaridad y la armonía entre los pueblos.", "ex_en": "The circle of stars symbolizes unity, solidarity, and harmony among peoples."},
                {"lemma": "lema", "pos": "noun", "translation": "motto", "ex_es": "Cada institución cuenta con símbolos propios como su bandera, su himno y su lema.", "ex_en": "Each institution has its own symbols such as its flag, its anthem, and its motto."},
                {"lemma": "fondo azul", "pos": "noun", "translation": "blue background", "ex_es": "Las doce estrellas amarillas destacan sobre el fondo azul de la bandera europea.", "ex_en": "The twelve yellow stars stand out against the blue background of the European flag."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuándo se celebra el Día de Europa?", "options": ["El 9 de mayo", "El 6 de diciembre", "El 12 de octubre", "El 23 de abril"], "answer": "El 9 de mayo", "explanation": "El 9 de mayo se celebra el Día de Europa en conmemoración de la Declaración Schuman de 1950."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántas estrellas doradas tiene la bandera de la Unión Europea?", "options": ["12 estrellas", "27 estrellas", "17 estrellas", "15 estrellas"], "answer": "12 estrellas", "explanation": "La bandera europea tiene un número fijo de 12 estrellas doradas en círculo sobre fondo azul."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La bandera de la Unión Europea tiene doce estrellas doradas sobre fondo ___.", "answer": "azul", "english": "The flag of the European Union has twelve golden stars on a blue background.", "explanation": "'Sobre fondo azul'."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El lema oficial de la Unión Europea es «Unida en la ___».", "answer": "diversidad", "english": "The official motto of the European Union is 'United in diversity'.", "explanation": "'Unida en la diversidad'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Europe Day:", "words": ["El", "Día", "de", "Europa", "se", "celebra", "el", "nueve", "de", "mayo."], "answer": "El Día de Europa se celebra el nueve de mayo.", "english": "Europe Day is celebrated on May 9."},
                {"type": "dictation", "cat": "listening", "text": "La bandera de la Unión Europea tiene doce estrellas doradas sobre fondo azul.", "english": "The flag of the European Union has twelve golden stars on a blue background."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿De qué compositor es la melodía de la «Oda a la Alegría», himno oficial de la Unión Europea?", "options": ["De Ludwig van Beethoven", "De Wolfgang Amadeus Mozart", "De Manuel de Falla", "De Giuseppe Verdi"], "answer": "De Ludwig van Beethoven", "explanation": "El himno europeo procede del último movimiento de la Novena Sinfonía de Beethoven."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El himno de la Unión Europea es la «Oda a la ___» de Beethoven.", "answer": "Alegría", "english": "The anthem of the European Union is Beethoven's 'Ode to Joy'.", "explanation": "'Oda a la Alegría'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the EU motto:", "words": ["El", "lema", "de", "la", "Unión", "Europea", "es", "Unida", "en", "la", "diversidad."], "answer": "El lema de la Unión Europea es Unida en la diversidad.", "english": "The motto of the European Union is United in diversity."}
            ]
        },
        {
            "num": "05",
            "story_slug": "ciudadaniaeuropea",
            "title": "Derechos de la ciudadanía europea: tarjeta sanitaria europea, protección consular y Erasmus+",
            "goal": "Understand the practical benefits of Spanish and EU citizenship: right to live, study, and work in any of the 27 EU countries, the European Health Insurance Card (Tarjeta Sanitaria Europea), diplomatic protection by any EU embassy abroad, and the Erasmus+ program.",
            "grammar_slug": "en-las-mismas-condiciones-que",
            "grammar_title": "Igualdad de trato comunitario: 'en las mismas condiciones que los nacionales'",
            "grammar_summary": "Using 'en las mismas condiciones que los nacionales de dicho Estado' to express EU non-discrimination rights.",
            "grammar_text": "European Union treaties guarantee equal treatment across all 27 Member States using the comparative legal structure 'en las mismas condiciones que los nacionales de dicho Estado' (under the same conditions as nationals of that State). This applies to working without a work permit, voting in municipal and European elections where you reside, receiving urgent healthcare with the **Tarjeta Sanitaria Europea (TSE)**, and receiving consular protection from the embassy of any EU country in a third country where Spain has no diplomatic representation.",
            "grammar_examples": [
                {"spanish": "Los españoles pueden trabajar en cualquier país de la Unión en las mismas condiciones que sus nacionales.", "english": "Spaniards can work in any country of the Union under the same conditions as its nationals."},
                {"spanish": "La Tarjeta Sanitaria Europea permite recibir asistencia médica pública durante estancias temporales en Europa.", "english": "The European Health Insurance Card allows receiving public medical care during temporary stays in Europe."},
                {"spanish": "En un tercer país sin embajada española, cualquier ciudadano puede acudir a la embajada de otro Estado miembro.", "english": "In a third country without a Spanish embassy, any citizen can go to the embassy of another Member State."}
            ],
            "grammar_tip": "Key practical items on the CCSE exam: **Tarjeta Sanitaria Europea (TSE)** for medical care when traveling in the EU, and **Erasmus+** as the EU program for educational, university, and youth mobility.",
            "story_title": "Ciudadanos sin fronteras: de Erasmus a la Tarjeta Sanitaria",
            "story_summary": "Spain is the leading destination and sender of students in the European Erasmus+ program; two university students in Salamanca prepare their semester abroad with their European Health Insurance Card.",
            "story_location": "Salamanca, Universidad de Salamanca",
            "story_paragraphs": [
                "Adquirir la nacionalidad española otorga automáticamente la ciudadanía de la Unión Europea, un estatuto jurídico que suma derechos prácticos fundamentales sin sustituir a la nacionalidad española.",
                "El primero de estos derechos es la libertad de circular, residir, estudiar y trabajar en cualquiera de los veintisiete Estados miembros de la Unión sin necesidad de visado ni permiso de trabajo, en las mismas condiciones que los ciudadanos de ese país.",
                "En la Universidad de Salamanca, Lucía y Mateo preparan su beca del programa Erasmus+, el programa de la Unión Europea para la educación, la formación, la juventud y el deporte. España es desde hace más de dos décadas el país europeo que más estudiantes Erasmus recibe y uno de los que más jóvenes envía al resto del continente.",
                "Antes de viajar a Bolonia y a Múnich, ambos solicitan gratuitamente en la Seguridad Social la Tarjeta Sanitaria Europea (TSE), el documento personal que acredita el derecho a recibir las prestaciones sanitarias públicas necesarias durante una estancia temporal en cualquiera de los países de la Unión Europea, el Espacio Económico Europeo y Suiza.",
                "Además, si un ciudadano español viaja fuera de Europa a un país donde España no tenga embajada ni consulado propio, tiene derecho a recibir protección diplomática y consular en la embajada de cualquier otro Estado miembro de la Unión Europea exactamente igual que si fuera nacional de ese país."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué documento gratuito permite a los ciudadanos residentes en España recibir asistencia médica pública durante un viaje temporal por países de la Unión Europea?",
                    "options": ["La Tarjeta Sanitaria Europea (TSE).", "El certificado de antecedentes penales.", "El abono de transporte joven."],
                    "correctIndex": 0,
                    "explanation": "La Tarjeta Sanitaria Europea (TSE) acredita el derecho a recibir prestaciones sanitarias públicas durante estancias temporales en el espacio europeo."
                },
                {
                    "question": "¿Cómo se denomina el programa de la Unión Europea que fomenta la movilidad de estudiantes universitarios, profesores y jóvenes entre países europeos?",
                    "options": ["Erasmus+.", "SEPRONA.", "IMSERSO."],
                    "correctIndex": 0,
                    "explanation": "Erasmus+ es el programa de la Unión Europea para apoyar la educación, la formación, la juventud y el deporte en Europa."
                },
                {
                    "question": "¿A dónde puede acudir un ciudadano español si necesita ayuda consular urgente en un país extracomunitario donde no existe embajada de España?",
                    "options": ["A la embajada o consulado de cualquier otro Estado miembro de la Unión Europea.", "Únicamente a una oficina bancaria privada.", "A ninguna embajada hasta regresar a Madrid."],
                    "correctIndex": 0,
                    "explanation": "La ciudadanía europea garantiza el derecho a acogerse a la protección diplomática y consular de cualquier Estado miembro de la UE cuando el propio país no tenga representación."
                }
            ],
            "vocab": [
                {"lemma": "Tarjeta Sanitaria Europea", "pos": "noun", "translation": "European Health Insurance Card (EHIC / TSE)", "ex_es": "La Tarjeta Sanitaria Europea cubre la atención médica pública durante viajes temporales por Europa.", "ex_en": "The European Health Insurance Card covers public medical care during temporary trips across Europe."},
                {"lemma": "Erasmus+", "pos": "noun", "translation": "Erasmus+ (EU education and youth mobility program)", "ex_es": "España es el país líder en recepción de estudiantes universitarios del programa Erasmus+.", "ex_en": "Spain is the leading country in receiving university students from the Erasmus+ program."},
                {"lemma": "protección consular", "pos": "noun", "translation": "consular protection", "ex_es": "Todo ciudadano europeo tiene derecho a la protección consular de cualquier embajada de la UE en terceros países.", "ex_en": "Every European citizen has the right to consular protection from any EU embassy in third countries."},
                {"lemma": "estancia temporal", "pos": "noun", "translation": "temporary stay", "ex_es": "Durante una estancia temporal por estudios o turismo, la TSE garantiza la asistencia sanitaria.", "ex_en": "During a temporary stay for studies or tourism, the EHIC guarantees healthcare assistance."},
                {"lemma": "movilidad", "pos": "noun", "translation": "mobility", "ex_es": "La movilidad estudiantil y laboral fortalece los lazos entre los países europeos.", "ex_en": "Student and labor mobility strengthens ties between European countries."},
                {"lemma": "permiso de trabajo", "pos": "noun", "translation": "work permit", "ex_es": "Los ciudadanos españoles no necesitan permiso de trabajo para emplearse en otro país de la UE.", "ex_en": "Spanish citizens do not need a work permit to be employed in another EU country."},
                {"lemma": "beca", "pos": "noun", "translation": "scholarship / grant", "ex_es": "Miles de jóvenes españoles estudian cada curso en universidades europeas con una beca Erasmus+.", "ex_en": "Thousands of young Spaniards study each academic year at European universities with an Erasmus+ grant."},
                {"lemma": "consulado", "pos": "noun", "translation": "consulate", "ex_es": "El consulado asiste a los ciudadanos que pierden su pasaporte o sufren una emergencia en el exterior.", "ex_en": "The consulate assists citizens who lose their passport or suffer an emergency abroad."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué documento permite recibir asistencia médica pública durante un viaje o estancia temporal en otro país de la Unión Europea?", "options": ["La Tarjeta Sanitaria Europea (TSE)", "El carné de biblioteca municipal", "El recibo del impuesto de circulación", "La papeleta electoral"], "answer": "La Tarjeta Sanitaria Europea (TSE)", "explanation": "La Tarjeta Sanitaria Europea acredita el derecho a recibir asistencia sanitaria pública durante estancias temporales en la UE."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es el programa de la Unión Europea destinado a la movilidad de estudiantes, profesores y jóvenes?", "options": ["Erasmus+", "Cervantes Digital", "Plan Renove", "Pacto de Toledo"], "answer": "Erasmus+", "explanation": "Erasmus+ es el programa de la UE para la educación, la formación, la juventud y el deporte."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Tarjeta ___ Europea permite recibir atención médica pública en los países de la Unión.", "answer": "Sanitaria", "english": "The European Health Insurance Card allows receiving public medical care in the countries of the Union.", "explanation": "'Tarjeta Sanitaria Europea' (TSE)."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El programa europeo de intercambio universitario y educativo más conocido se llama ___.", "answer": "Erasmus+", "english": "The best-known European university and educational exchange program is called Erasmus+.", "explanation": "'Erasmus+'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about working in the European Union:", "words": ["Los", "ciudadanos", "españoles", "pueden", "trabajar", "libremente", "en", "cualquier", "país", "de", "la", "Unión", "Europea."], "answer": "Los ciudadanos españoles pueden trabajar libremente en cualquier país de la Unión Europea.", "english": "Spanish citizens can work freely in any country of the European Union."},
                {"type": "dictation", "cat": "listening", "text": "La Tarjeta Sanitaria Europea permite recibir asistencia médica en Europa.", "english": "The European Health Insurance Card allows receiving medical assistance in Europe."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Necesita un ciudadano español un visado o permiso de trabajo para trabajar en Francia o Alemania?", "options": ["No, tiene derecho a la libre circulación y residencia en toda la Unión Europea", "Sí, debe solicitar un visado cada tres meses", "Solo si es menor de veinticinco años", "Sí, autorizado por el Senado"], "answer": "No, tiene derecho a la libre circulación y residencia en toda la Unión Europea", "explanation": "La ciudadanía europea garantiza el derecho a residir y trabajar libremente en cualquiera de los 27 Estados miembros."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En un país sin embajada española, un ciudadano español tiene derecho a la protección ___ de cualquier otro Estado de la UE.", "answer": "consular", "english": "In a country without a Spanish embassy, a Spanish citizen has the right to consular protection from any other EU State.", "explanation": "'Protección consular'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the Erasmus+ program:", "words": ["España", "es", "el", "país", "europeo", "que", "más", "estudiantes", "Erasmus+", "recibe."], "answer": "España es el país europeo que más estudiantes Erasmus+ recibe.", "english": "Spain is the European country that receives the most Erasmus+ students."}
            ]
        }
    ],
    "consolidation_exercises": [
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué año ingresó España en las Comunidades Europeas (actual Unión Europea)?", "options": ["En 1986", "En 1978", "En 2002", "En 1995"], "answer": "En 1986", "explanation": "España ingresó el 1 de enero de 1986."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Dónde se firmó el Tratado de Adhesión de España a las Comunidades Europeas el 12 de junio de 1985?", "options": ["En el Palacio Real de Madrid", "En la Alhambra de Granada", "En el Acueducto de Segovia", "En la Torre del Oro de Sevilla"], "answer": "En el Palacio Real de Madrid", "explanation": "Se firmó en el Salón de Columnas del Palacio Real de Madrid."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué año entraron en circulación física los billetes y monedas de euro en España?", "options": ["En 2002", "En 1986", "En 1992", "En 2010"], "answer": "En 2002", "explanation": "El 1 de enero de 2002 el euro sustituyó físicamente a la peseta."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál era la moneda oficial de España antes del euro?", "options": ["La peseta", "El escudo", "El franco", "La corona"], "answer": "La peseta", "explanation": "La peseta fue la moneda española desde 1868 hasta 2002."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué día se celebra el Día de Europa?", "options": ["El 9 de mayo", "El 6 de diciembre", "El 12 de octubre", "El 1 de enero"], "answer": "El 9 de mayo", "explanation": "El 9 de mayo conmemora la Declaración Schuman de 1950."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántas estrellas tiene la bandera de la Unión Europea?", "options": ["12 estrellas doradas sobre fondo azul", "27 estrellas blancas", "17 estrellas amarillas", "15 estrellas plateadas"], "answer": "12 estrellas doradas sobre fondo azul", "explanation": "Tiene 12 estrellas doradas dispuestas en círculo sobre fondo azul."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Actualmente la Unión Europea está formada por ___ Estados miembros.", "answer": "veintisiete", "english": "Currently the European Union is made up of twenty-seven Member States.", "explanation": "27 Estados miembros."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El acuerdo de ___ permite viajar por Europa sin controles en las fronteras interiores.", "answer": "Schengen", "english": "The Schengen agreement allows travel across Europe without internal border controls.", "explanation": "'Espacio Schengen'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ Europeo es elegido directamente por los ciudadanos cada cinco años.", "answer": "Parlamento", "english": "The European Parliament is elected directly by citizens every five years.", "explanation": "'Parlamento Europeo'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "La ___ Europea es el órgano ejecutivo de la Unión y tiene su sede en Bruselas.", "answer": "Comisión", "english": "The European Commission is the executive body of the Union and is headquartered in Brussels.", "explanation": "'Comisión Europea'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El himno europeo es la «Oda a la ___» de la Novena Sinfonía de Beethoven.", "answer": "Alegría", "english": "The European anthem is the 'Ode to Joy' from Beethoven's Ninth Symphony.", "explanation": "'Oda a la Alegría'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Tarjeta ___ Europea cubre la asistencia médica pública en viajes temporales por la UE.", "answer": "Sanitaria", "english": "The European Health Insurance Card covers public healthcare on temporary trips across the EU.", "explanation": "'Tarjeta Sanitaria Europea'."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Spain joining the EU:", "words": ["España", "y", "Portugal", "ingresaron", "en", "la", "Comunidad", "Europea", "en", "1986."], "answer": "España y Portugal ingresaron en la Comunidad Europea en 1986.", "english": "Spain and Portugal joined the European Community in 1986."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the euro:", "words": ["Los", "billetes", "y", "monedas", "de", "euro", "entraron", "en", "circulación", "en", "2002."], "answer": "Los billetes y monedas de euro entraron en circulación en 2002.", "english": "Euro banknotes and coins entered circulation in 2002."},
        {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Order the sentence about the European flag:", "words": ["La", "bandera", "europea", "tiene", "doce", "estrellas", "doradas", "sobre", "fondo", "azul."], "answer": "La bandera europea tiene doce estrellas doradas sobre fondo azul.", "english": "The European flag has twelve golden stars on a blue background."},
        {"type": "dictation", "cat": "listening", "text": "El nueve de mayo se celebra el Día de Europa en toda la Unión.", "english": "On May 9 Europe Day is celebrated throughout the Union."},
        {"type": "dictation", "cat": "listening", "text": "El euro sustituyó a la peseta el uno de enero de dos mil dos.", "english": "The euro replaced the peseta on January 1, 2002."},
        {"type": "dictation", "cat": "listening", "text": "El lema de la Unión Europea es Unida en la diversidad.", "english": "The motto of the European Union is United in diversity."}
    ]
}


def main():
    emit_unit(UNIT_7)
    emit_unit(UNIT_8)
    emit_unit(UNIT_9)


if __name__ == "__main__":
    main()
