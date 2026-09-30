#!/usr/bin/env python3
"""
Generate Spain Citizenship (CCSE) B1 Units 10, 11, and 12 to the full B1 standard:
  - Unit 10: Símbolos del Estado: Bandera, Escudo e Himno (slug: simbolos, legacy: b1-ccse-simbolos)
  - Unit 11: El Castellano y las Lenguas Cooficiales (slug: lenguas, legacy: b1-ccse-lenguas)
  - Unit 12: Difusión Cultural: El Instituto Cervantes (slug: cervantes, legacy: b1-ccse-instituto-cervantes)
"""

from generate_es_b1_ccse_unit2_3 import emit_unit

UNIT_10 = {
    "slug": "simbolos",
    "legacy_prefix": "b1-ccse-simbolos",
    "unit_title": "Símbolos del Estado: Bandera, Escudo e Himno",
    "order": 10,
    "unit_summary": "Complete CCSE guide to the Official Symbols of Spain: the flag (Article 4.1, three horizontal stripes with the yellow middle stripe twice the width of each red stripe), the coat of arms (historical kingdoms, Pillars of Hercules, Plus Ultra motto), the National Anthem (Marcha Real, without lyrics), National Holidays (October 12 and December 6), and State honors.",
    "unit_paragraphs": [],
    "unit_questions": [],
    "lessons": [
        {
            "num": "01",
            "story_slug": "bandera",
            "title": "La bandera de España (artículo 4.1) y las enseñas de las comunidades autónomas",
            "goal": "Master Article 4 of the Constitution: the design and proportions of the Spanish flag (three horizontal stripes, red-yellow-red, with the yellow stripe twice the width of each red one) and its placement alongside autonomic flags.",
            "grammar_slug": "de-doble-anchura-que",
            "grammar_title": "Proporciones y descripciones oficiales: 'formada por' y 'de doble anchura que'",
            "grammar_summary": "Using 'estar formada por' and 'ser de doble anchura que cada una de las rojas' to describe the Spanish flag.",
            "grammar_text": "Article 4.1 of the Spanish Constitution defines the national flag with exact geometric precision: 'La bandera de España está formada por tres franjas horizontales, roja, amarilla y roja, siendo la amarilla de doble anchura que cada una de las rojas.' Article 4.2 adds that the Statutes may recognize flags and ensigns of the Autonomous Communities, which shall be used together with the flag of Spain ('se utilizarán junto a la bandera de España') on their public buildings and in their official acts.",
            "grammar_examples": [
                {"spanish": "La bandera de España está formada por tres franjas horizontales: roja, amarilla y roja.", "english": "The flag of Spain is formed by three horizontal stripes: red, yellow, and red."},
                {"spanish": "La franja amarilla central es de doble anchura que cada una de las franjas rojas.", "english": "The central yellow stripe is twice the width of each of the red stripes."},
                {"spanish": "Las banderas autonómicas se utilizan junto a la bandera de España en los edificios públicos.", "english": "Autonomic flags are used alongside the flag of Spain on public buildings."}
            ],
            "grammar_tip": "Watch out for the CCSE exam question on stripe widths: the yellow middle stripe is **twice as wide** ('el doble de ancha') as each of the two red stripes.",
            "story_title": "Tres franjas horizontales en la Plaza de Colón",
            "story_summary": "Under the monumental flag in Madrid's Plaza de Colón, a naval historian explains its 1785 origin under King Charles III and the exact proportions defined in Article 4 of the Constitution.",
            "story_location": "Madrid, Plaza de Colón",
            "story_paragraphs": [
                "En los jardines del Descubrimiento de la Plaza de Colón, en Madrid, ondea una de las banderas más grandes de España. Sus colores —rojo, amarillo gualda y rojo— tienen su origen en el concurso convocado en 1785 por el rey Carlos III para dotar a los buques de la Armada de una enseña que se distinguiera claramente a gran distancia en alta mar.",
                "El artículo 4.1 de la Constitución Española de 1978 recoge su diseño con precisión matemática: la bandera de España está formada por tres franjas horizontales, roja, amarilla y roja.",
                "Un detalle fundamental que todo ciudadano debe recordar para la prueba CCSE es la proporción de sus franjas: las tres no miden lo mismo, sino que la franja central amarilla es de doble anchura que cada una de las franjas rojas superior e inferior.",
                "A su vez, el artículo 4.2 establece que los Estatutos de Autonomía pueden reconocer banderas y enseñas propias de las comunidades autónomas.",
                "Por mandato constitucional, estas banderas autonómicas ondean siempre junto a la bandera de España (y, habitualmente, junto a la bandera de la Unión Europea y la del municipio) en el exterior de todos los edificios públicos y en los actos oficiales."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 4.1 de la Constitución, ¿cómo es la bandera de España?",
                    "options": ["Está formada por tres franjas horizontales (roja, amarilla y roja), siendo la amarilla de doble anchura que cada una de las rojas.", "Está formada por tres franjas verticales del mismo tamaño.", "Tiene dos franjas azules y una blanca central."],
                    "correctIndex": 0,
                    "explanation": "El artículo 4.1 define la bandera con tres franjas horizontales (roja, amarilla y roja) y precisa que la amarilla tiene el doble de anchura que cada una de las rojas."
                },
                {
                    "question": "¿Qué proporción tiene la franja amarilla central respecto a cada una de las franjas rojas de la bandera española?",
                    "options": ["Tiene el doble de anchura que cada una de las rojas.", "Tiene la mitad de anchura que las rojas.", "Tiene exactamente la misma anchura que las rojas."],
                    "correctIndex": 0,
                    "explanation": "La franja amarilla ocupa la mitad del alto total del paño, es decir, el doble que cada franja roja."
                },
                {
                    "question": "¿Dónde deben utilizarse las banderas propias de las comunidades autónomas según el artículo 4.2 de la Constitución?",
                    "options": ["Junto a la bandera de España en sus edificios públicos y en sus actos oficiales.", "En sustitución de la bandera española en las embajadas.", "Únicamente dentro de recintos deportivos privados."],
                    "correctIndex": 0,
                    "explanation": "El artículo 4.2 dispone que las banderas autonómicas se utilizarán junto a la bandera de España en sus edificios públicos y en sus actos oficiales."
                }
            ],
            "vocab": [
                {"lemma": "franja", "pos": "noun", "translation": "stripe / band", "ex_es": "La bandera de España consta de tres franjas horizontales.", "ex_en": "The flag of Spain consists of three horizontal stripes."},
                {"lemma": "doble anchura", "pos": "noun", "translation": "double width", "ex_es": "La franja amarilla central es de doble anchura que cada una de las rojas.", "ex_en": "The central yellow stripe is of double width compared to each of the red ones."},
                {"lemma": "horizontal", "pos": "adjective", "translation": "horizontal", "ex_es": "Las tres franjas de la bandera española tienen disposición horizontal.", "ex_en": "The three stripes of the Spanish flag have a horizontal layout."},
                {"lemma": "enseña", "pos": "noun", "translation": "ensign / standard / flag", "ex_es": "Los Estatutos pueden reconocer banderas y enseñas propias de las comunidades autónomas.", "ex_en": "Statutes may recognize flags and ensigns of the autonomous communities."},
                {"lemma": "rojigualda", "pos": "noun", "translation": "red-and-weld-yellow flag (traditional nickname of Spain's flag)", "ex_es": "La bandera española es conocida popularmente como la rojigualda por sus colores.", "ex_en": "The Spanish flag is popularly known as the rojigualda for its colors."},
                {"lemma": "ondear", "pos": "verb", "translation": "to wave / fly (a flag)", "ex_es": "La bandera nacional ondea en el exterior de todos los edificios públicos.", "ex_en": "The national flag flies outside all public buildings."},
                {"lemma": "acto oficial", "pos": "noun", "translation": "official ceremony / act", "ex_es": "En todo acto oficial la bandera autonómica se coloca junto a la de España.", "ex_en": "In every official act the autonomic flag is placed alongside that of Spain."},
                {"lemma": "edificio público", "pos": "noun", "translation": "public building", "ex_es": "Los ayuntamientos, ministerios y juzgados son edificios públicos.", "ex_en": "City halls, ministries, and courts are public buildings."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántas franjas tiene la bandera de España y de qué colores son?", "options": ["Tres franjas horizontales: roja, amarilla y roja", "Tres franjas verticales: roja, blanca y roja", "Dos franjas horizontales: roja y amarilla", "Cuatro franjas amarillas y rojas"], "answer": "Tres franjas horizontales: roja, amarilla y roja", "explanation": "Artículo 4.1 de la Constitución Española."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué anchura tiene la franja amarilla de la bandera de España respecto a cada una de las rojas?", "options": ["El doble de anchura que cada una de las rojas", "La misma anchura que las rojas", "La mitad de anchura que las rojas", "El triple de anchura"], "answer": "El doble de anchura que cada una de las rojas", "explanation": "La franja central amarilla es de doble anchura que cada una de las franjas rojas."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La bandera de España está formada por tres ___ horizontales: roja, amarilla y roja.", "answer": "franjas", "english": "The flag of Spain is formed by three horizontal stripes: red, yellow, and red.", "explanation": "'Franjas horizontales' means horizontal stripes."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "La franja amarilla central es de ___ anchura que cada una de las rojas.", "answer": "doble", "english": "The central yellow stripe is twice the width of each of the red ones.", "explanation": "'De doble anchura que'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the constitutional description of the Spanish flag:", "words": ["La", "bandera", "de", "España", "tiene", "tres", "franjas", "horizontales:", "roja,", "amarilla", "y", "roja."], "answer": "La bandera de España tiene tres franjas horizontales: roja, amarilla y roja.", "english": "The flag of Spain has three horizontal stripes: red, yellow, and red."},
                {"type": "dictation", "cat": "listening", "text": "La franja amarilla tiene el doble de anchura que cada una de las rojas.", "english": "The yellow stripe has twice the width of each of the red ones."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Cómo deben utilizarse las banderas de las comunidades autónomas según el artículo 4.2 de la Constitución?", "options": ["Junto a la bandera de España en los edificios públicos y actos oficiales", "Solo en fiestas privadas", "En lugar de la bandera de España", "Únicamente los domingos"], "answer": "Junto a la bandera de España en los edificios públicos y actos oficiales", "explanation": "Las banderas autonómicas se utilizan junto a la bandera de España en sus edificios públicos y actos oficiales."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Las banderas autonómicas ___ junto a la bandera de España en los ayuntamientos.", "answer": "ondean", "english": "Autonomic flags fly alongside the flag of Spain on city halls.", "explanation": "'Ondear' means to fly/wave."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about autonomic flags:", "words": ["Las", "banderas", "autonómicas", "se", "utilizan", "junto", "a", "la", "bandera", "de", "España."], "answer": "Las banderas autonómicas se utilizan junto a la bandera de España.", "english": "Autonomic flags are used alongside the flag of Spain."}
            ]
        },
        {
            "num": "02",
            "story_slug": "escudo",
            "title": "El Escudo de España: reinos históricos, las Columnas de Hércules y el lema «Plus Ultra»",
            "goal": "Identify every element on the official Coat of Arms of Spain (Law 33/1981): the four main quarters (Castile, León, Aragon, Navarre), the pomegranate of Granada at the base, the Bourbon fleur-de-lis, the Royal Crown, and the Pillars of Hercules with the motto 'Plus Ultra'.",
            "grammar_slug": "flanqueado-por-y-rematado-por",
            "grammar_title": "Descripción heráldica y espacial: 'en la parte inferior', 'flanqueado por' y 'rematado por'",
            "grammar_summary": "Using spatial and heraldic participial phrases ('flanqueado por dos columnas', 'rematado por la corona real').",
            "grammar_text": "To describe architectural or heraldic symbols like the Coat of Arms of Spain ('el Escudo de España', regulated by Law 33/1981), Spanish uses participial modifiers: 'integrado por cuatro cuarteles' (composed of four quarters: Castile, León, Aragon, and Navarre), 'en la punta / en la parte inferior' (at the bottom point: the pomegranate emblem of Granada), 'rematado por la corona real' (topped by the Royal Crown), and 'flanqueado por las Columnas de Hércules con el lema Plus Ultra' (flanked by the Pillars of Hercules bearing the Latin motto 'Plus Ultra', meaning 'Further Beyond').",
            "grammar_examples": [
                {"spanish": "El escudo de España está integrado por los emblemas de Castilla, León, Aragón, Navarra y Granada.", "english": "The coat of arms of Spain is composed of the emblems of Castile, León, Aragon, Navarre, and Granada."},
                {"spanish": "Está rematado por la corona real y flanqueado por las dos Columnas de Hércules.", "english": "It is topped by the royal crown and flanked by the two Pillars of Hercules."},
                {"spanish": "En la cinta que rodea las columnas figura escrito el lema latino «Plus Ultra».", "english": "On the scroll surrounding the columns appears the Latin motto 'Plus Ultra'."}
            ],
            "grammar_tip": "Memorize the 5 historical territories on the Coat of Arms (**Castilla, León, Aragón, Navarra, Granada**) and the motto on the Pillars of Hercules (**Plus Ultra**).",
            "story_title": "Cinco reinos y dos columnas hacia el océano",
            "story_summary": "Examining the yellow stripe of the Spanish flag and the cover of a Spanish passport, a heraldry curator explains the meaning of the castle, the lion, the four bars, the chains, the pomegranate, and the motto Plus Ultra.",
            "story_location": "Madrid, Museo Naval",
            "story_paragraphs": [
                "Sobre la franja amarilla de la bandera de España —y en la portada del pasaporte y del Documento Nacional de Identidad— figura el Escudo de España, regulado por la Ley 33/1981 como síntesis visual de la historia del país.",
                "El cuerpo central del escudo está dividido en cuatro cuarteles principales que representan a los antiguos reinos medievales: un castillo de oro sobre fondo rojo por el Reino de Castilla; un león rampante púrpura coronado por el Reino de León; cuatro barras rojas verticales sobre fondo dorado por la Corona de Aragón; y unas cadenas de oro sobre fondo rojo por el Reino de Navarra.",
                "En la parte inferior del escudo (llamada punta o entado) aparece una granada abierta con hojas verdes, símbolo del antiguo Reino de Granada. En el centro exacto, un óvalo azul con tres flores de lis doradas representa a la dinastía de los Borbones.",
                "El escudo aparece rematado en su parte superior por la Corona Real, símbolo de la monarquía parlamentaria española.",
                "A ambos lados lo flanquean las dos Columnas de Hércules —que simbolizan el estrecho de Gibraltar, puerta entre el Mediterráneo y el Atlántico— unidas por una cinta roja con el lema latino «Plus Ultra» («Más allá»), adoptado en el siglo XVI para recordar la proyección ultramarina de España hacia el Nuevo Mundo."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué cinco reinos históricos españoles están representados en los cuarteles y en la punta inferior del Escudo de España?",
                    "options": ["Castilla, León, Aragón, Navarra y Granada.", "Asturias, Galicia, Valencia, Murcia y Canarias.", "Toledo, Sevilla, Córdoba, Jaén y Cádiz."],
                    "correctIndex": 0,
                    "explanation": "El escudo integra el castillo de Castilla, el león de León, las barras de Aragón, las cadenas de Navarra y, en la punta inferior, la granada del Reino de Granada."
                },
                {
                    "question": "¿Qué lema en latín aparece inscrito en las Columnas de Hércules del Escudo de España?",
                    "options": ["«Plus Ultra» («Más allá»).", "«In varietate concordia».", "«E pluribus unum»."],
                    "correctIndex": 0,
                    "explanation": "En las Columnas de Hércules que flanquean el escudo figura el lema «Plus Ultra» («Más allá»)."
                },
                {
                    "question": "¿Qué elemento corona la parte superior del Escudo de España?",
                    "options": ["La Corona Real.", "Doce estrellas doradas.", "Un águila imperial."],
                    "correctIndex": 0,
                    "explanation": "El Escudo de España está timbrado o rematado en su parte superior por la Corona Real, símbolo de la monarquía parlamentaria."
                }
            ],
            "vocab": [
                {"lemma": "Escudo de España", "pos": "noun", "translation": "Coat of Arms of Spain", "ex_es": "El Escudo de España figura en la franja amarilla de la bandera y en el pasaporte.", "ex_en": "The Coat of Arms of Spain appears on the yellow stripe of the flag and on the passport."},
                {"lemma": "Plus Ultra", "pos": "noun", "translation": "Plus Ultra ('Further Beyond' - motto on Spain's Coat of Arms)", "ex_es": "El lema 'Plus Ultra' aparece escrito sobre las dos Columnas de Hércules.", "ex_en": "The motto 'Plus Ultra' appears written across the two Pillars of Hercules."},
                {"lemma": "Columnas de Hércules", "pos": "noun", "translation": "Pillars of Hercules", "ex_es": "Las dos Columnas de Hércules flanquean el escudo y simbolizan el estrecho de Gibraltar.", "ex_en": "The two Pillars of Hercules flank the coat of arms and symbolize the Strait of Gibraltar."},
                {"lemma": "granada", "pos": "noun", "translation": "pomegranate (emblem of the Kingdom of Granada)", "ex_es": "En la parte inferior del escudo se observa una granada que representa al Reino de Granada.", "ex_en": "At the bottom of the coat of arms a pomegranate representing the Kingdom of Granada can be seen."},
                {"lemma": "cuartel", "pos": "noun", "translation": "heraldic quarter (of a shield)", "ex_es": "Los cuatro cuarteles principales representan a Castilla, León, Aragón y Navarra.", "ex_en": "The four main quarters represent Castile, León, Aragon, and Navarre."},
                {"lemma": "Corona Real", "pos": "noun", "translation": "Royal Crown", "ex_es": "La Corona Real remata la parte superior del Escudo de España.", "ex_en": "The Royal Crown tops the upper part of the Coat of Arms of Spain."},
                {"lemma": "flor de lis", "pos": "noun", "translation": "fleur-de-lis (Bourbon dynasty emblem)", "ex_es": "En el centro del escudo hay un óvalo azul con tres flores de lis doradas.", "ex_en": "In the center of the coat of arms there is a blue oval with three golden fleurs-de-lis."},
                {"lemma": "emblema", "pos": "noun", "translation": "emblem", "ex_es": "Las cadenas de oro son el emblema histórico del Reino de Navarra.", "ex_en": "The golden chains are the historical emblem of the Kingdom of Navarre."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué lema figura escrito en las Columnas de Hércules del Escudo de España?", "options": ["Plus Ultra", "Unida en la diversidad", "Tanto monta", "Semper fidelis"], "answer": "Plus Ultra", "explanation": "«Plus Ultra» («Más allá») es el lema oficial inscrito en las Columnas de Hércules del Escudo de España."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué fruto aparece en la punta inferior del Escudo de España representando a su reino histórico?", "options": ["Una granada (por el Reino de Granada)", "Una naranja (por Valencia)", "Una aceituna (por Jaén)", "Una manzana (por Asturias)"], "answer": "Una granada (por el Reino de Granada)", "explanation": "En la punta inferior figura una granada abierta que simboliza el antiguo Reino de Granada."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En las Columnas de Hércules del escudo español aparece el lema latino «___ Ultra».", "answer": "Plus", "english": "On the Pillars of Hercules of the Spanish coat of arms appears the Latin motto 'Plus Ultra'.", "explanation": "'Plus Ultra' means 'Further Beyond'."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Escudo de España está rematado en su parte superior por la ___ Real.", "answer": "Corona", "english": "The Coat of Arms of Spain is topped in its upper part by the Royal Crown.", "explanation": "'La Corona Real'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the kingdoms on Spain's Coat of Arms:", "words": ["El", "escudo", "integra", "los", "emblemas", "de", "Castilla,", "León,", "Aragón,", "Navarra", "y", "Granada."], "answer": "El escudo integra los emblemas de Castilla, León, Aragón, Navarra y Granada.", "english": "The coat of arms integrates the emblems of Castile, León, Aragon, Navarre, and Granada."},
                {"type": "dictation", "cat": "listening", "text": "El lema Plus Ultra figura en las Columnas de Hércules del escudo.", "english": "The motto Plus Ultra appears on the Pillars of Hercules of the coat of arms."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué representan el castillo y el león en los dos cuarteles superiores del Escudo de España?", "options": ["A los antiguos reinos de Castilla y de León", "A las ciudades autónomas de Ceuta y Melilla", "A las islas Baleares y Canarias", "A Francia y Portugal"], "answer": "A los antiguos reinos de Castilla y de León", "explanation": "El castillo representa al Reino de Castilla y el león rampante al Reino de León."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Las cadenas de oro sobre fondo rojo del escudo representan a la Comunidad Foral de ___.", "answer": "Navarra", "english": "The golden chains on a red background of the coat of arms represent the Chartered Community of Navarre.", "explanation": "The chains are the emblem of Navarre."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the Pillars of Hercules:", "words": ["El", "Escudo", "de", "España", "está", "flanqueado", "por", "las", "dos", "Columnas", "de", "Hércules."], "answer": "El Escudo de España está flanqueado por las dos Columnas de Hércules.", "english": "The Coat of Arms of Spain is flanked by the two Pillars of Hercules."}
            ]
        },
        {
            "num": "03",
            "story_slug": "himno",
            "title": "El Himno Nacional de España: la «Marcha Real» o «Marcha Granadera»",
            "goal": "Know the essential facts about Spain's National Anthem for the CCSE exam: its names ('Marcha Real' or 'Marcha Granadera'), its 18th-century origin (1761/1770), and the key fact that it has NO official lyrics ('carece de letra oficial').",
            "grammar_slug": "carecer-de-letra-oficial",
            "grammar_title": "Ausencia de rasgo oficial: 'carecer de + sustantivo' y 'interpretarse sin'",
            "grammar_summary": "Using 'carecer de letra oficial' and 'ser conocido como' to describe the Spanish National Anthem.",
            "grammar_text": "One of the most famous facts about Spain's National Anthem ('el Himno Nacional de España') is expressed with 'carecer de + sustantivo' (to lack / have no) or 'no tener letra oficial': the Spanish anthem has NO official lyrics ('carece de letra oficial'). Known historically as the **Marcha Real** or **Marcha Granadera**, it is one of the oldest national anthems in Europe (documented in 1761 and declared Royal March of Honor by King Charles III in 1770) and is regulated today by Royal Decree 1560/1997.",
            "grammar_examples": [
                {"spanish": "El Himno Nacional de España es conocido tradicionalmente como la «Marcha Real» o «Marcha Granadera».", "english": "The National Anthem of Spain is traditionally known as the 'Marcha Real' or 'Marcha Granadera'."},
                {"spanish": "A diferencia de la mayoría de los himnos nacionales, la Marcha Real carece de letra oficial.", "english": "Unlike most national anthems, the Marcha Real has no official lyrics."},
                {"spanish": "Fue declarada Marcha de Honor por el rey Carlos III en el año 1770.", "english": "It was declared March of Honor by King Charles III in the year 1770."}
            ],
            "grammar_tip": "High-yield CCSE facts: 1) What is the name of Spain's national anthem? **La Marcha Real** (or **Marcha Granadera**). 2) Does it have official lyrics? **No, no tiene letra oficial**.",
            "story_title": "Un himno centenario sin palabras",
            "story_summary": "Before an international football match and a state reception in Madrid, a military band director explains why Spain's Marcha Real—dating back to 1761—is played purely as instrumental music without lyrics.",
            "story_location": "Madrid, Auditorio Nacional",
            "story_paragraphs": [
                "Quienes presencian por primera vez una recepción de Estado en Madrid o un partido internacional de las selecciones deportivas españolas suelen sorprenderse por un detalle singular: cuando suena el Himno Nacional de España, los jugadores y ciudadanos escuchan en respetuoso silencio sin cantar ninguna estrofa.",
                "La razón es que el Himno Nacional de España —regulado oficialmente por el Real Decreto 1560/1997— carece de letra oficial; es una composición exclusivamente instrumental.",
                "Su melodía es una de las más antiguas de Europa. Aparece recogida por primera vez en el año 1761 bajo el título de «Marcha Granadera» en el *Libro de la Ordenanza de los Toques de Pífanos yambores de la Infantería Española*, de Manuel de Espinosa de los Monteros.",
                "En el año 1770, el rey Carlos III la declaró «Marcha de Honor» para las solemnidades públicas a las que asistían los monarcas, motivo por el cual el pueblo empezó a llamarla popularmente la «Marcha Real».",
                "Así, al igual que el himno de la Unión Europea («Oda a la Alegría»), la «Marcha Real» o «Marcha Granadera» une a todos los ciudadanos españoles a través de la música sin palabras."
            ],
            "comp_questions": [
                {
                    "question": "¿Cómo se denomina tradicionalmente el Himno Nacional de España?",
                    "options": ["La «Marcha Real» o «Marcha Granadera».", "La «Oda a la Alegría».", "El «Canto de la Libertad»."],
                    "correctIndex": 0,
                    "explanation": "El Himno Nacional de España se conoce históricamente como «Marcha Real» o «Marcha Granadera»."
                },
                {
                    "question": "¿Cuál es una característica muy destacada del Himno Nacional de España en comparación con otros himnos del mundo?",
                    "options": ["Que no tiene letra oficial (es exclusivamente instrumental).", "Que se canta en latín y griego antiguo.", "Que cambia de melodía cada cuatro años."],
                    "correctIndex": 0,
                    "explanation": "El Himno Nacional de España carece de letra oficial."
                },
                {
                    "question": "¿En qué siglo tiene su origen la melodía de la «Marcha Granadera» o «Marcha Real»?",
                    "options": ["En el siglo XVIII (declarada Marcha de Honor por Carlos III en 1770).", "En el siglo XXI.", "En el siglo XII."],
                    "correctIndex": 0,
                    "explanation": "Data del siglo XVIII (documentada en 1761 y declarada Marcha de Honor por Carlos III en 1770)."
                }
            ],
            "vocab": [
                {"lemma": "Marcha Real", "pos": "noun", "translation": "Royal March (Spain's National Anthem)", "ex_es": "El Himno Nacional de España es la 'Marcha Real', también llamada 'Marcha Granadera'.", "ex_en": "The National Anthem of Spain is the 'Marcha Real', also called 'Marcha Granadera'."},
                {"lemma": "Marcha Granadera", "pos": "noun", "translation": "Grenadier March (original 1761 name of Spain's anthem)", "ex_es": "La 'Marcha Granadera' fue compuesta en el siglo XVIII como toque militar de honor.", "ex_en": "The 'Marcha Granadera' was composed in the 18th century as a military march of honor."},
                {"lemma": "letra oficial", "pos": "noun", "translation": "official lyrics", "ex_es": "El Himno Nacional de España carece de letra oficial.", "ex_en": "The National Anthem of Spain has no official lyrics."},
                {"lemma": "instrumental", "pos": "adjective", "translation": "instrumental", "ex_es": "La Marcha Real es una pieza musical puramente instrumental.", "ex_en": "The Marcha Real is a purely instrumental musical piece."},
                {"lemma": "himno nacional", "pos": "noun", "translation": "national anthem", "ex_es": "El himno nacional se interpreta en los actos solemnes de Estado y competiciones deportivas.", "ex_en": "The national anthem is played at solemn State ceremonies and sporting competitions."},
                {"lemma": "solemnidad", "pos": "noun", "translation": "solemnity / formal ceremony", "ex_es": "El himno aporta solemnidad a las recepciones oficiales del Jefe del Estado.", "ex_en": "The anthem brings solemnity to official receptions of the Head of State."},
                {"lemma": "partitura", "pos": "noun", "translation": "musical score", "ex_es": "El Real Decreto de 1997 fijó la partitura oficial del Himno Nacional.", "ex_en": "The 1997 Royal Decree established the official score of the National Anthem."},
                {"lemma": "estrofa", "pos": "noun", "translation": "stanza / verse", "ex_es": "Al no tener letra, en el himno español no se canta ninguna estrofa.", "ex_en": "Having no lyrics, no stanza is sung in the Spanish anthem."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo se llama el Himno Nacional de España?", "options": ["La Marcha Real (o Marcha Granadera)", "La Marsellesa", "La Oda a la Alegría", "El Himno de Riego"], "answer": "La Marcha Real (o Marcha Granadera)", "explanation": "El Himno Nacional de España es la «Marcha Real» o «Marcha Granadera»."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Tiene letra oficial el Himno Nacional de España?", "options": ["No, no tiene letra oficial", "Sí, escrita por Miguel de Cervantes", "Sí, el preámbulo de la Constitución", "Solo en las comunidades bilingües"], "answer": "No, no tiene letra oficial", "explanation": "El Himno Nacional de España es puramente instrumental y carece de letra oficial."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Himno Nacional de España se conoce como la «___ Real» o «Marcha Granadera».", "answer": "Marcha", "english": "The National Anthem of Spain is known as the 'Marcha Real' or 'Marcha Granadera'.", "explanation": "'La Marcha Real'."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "El Himno Nacional de España carece de ___ oficial; solo tiene música.", "answer": "letra", "english": "The National Anthem of Spain lacks official lyrics; it only has music.", "explanation": "'Carecer de letra oficial'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the Spanish National Anthem:", "words": ["El", "Himno", "Nacional", "de", "España", "no", "tiene", "letra", "oficial."], "answer": "El Himno Nacional de España no tiene letra oficial.", "english": "The National Anthem of Spain does not have official lyrics."},
                {"type": "dictation", "cat": "listening", "text": "El himno nacional de España es la Marcha Real y no tiene letra.", "english": "The national anthem of Spain is the Marcha Real and it has no lyrics."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué rey declaró la «Marcha Granadera» como Marcha de Honor en el siglo XVIII (1770) y creó también el diseño de la bandera rojigualda (1785)?", "options": ["Carlos III", "Felipe II", "Alfonso X el Sabio", "Fernando el Católico"], "answer": "Carlos III", "explanation": "Bajo el reinado de Carlos III (siglo XVIII) se adoptaron tanto la Marcha Real (1770) como la bandera rojigualda (1785)."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Marcha Real es una composición musical exclusivamente ___.", "answer": "instrumental", "english": "The Marcha Real is an exclusively instrumental musical composition.", "explanation": "'Instrumental' means played with instruments only."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the names of Spain's anthem:", "words": ["El", "himno", "español", "se", "llama", "Marcha", "Real", "o", "Marcha", "Granadera."], "answer": "El himno español se llama Marcha Real o Marcha Granadera.", "english": "The Spanish anthem is called Marcha Real or Marcha Granadera."}
            ]
        },
        {
            "num": "04",
            "story_slug": "fiestanacional",
            "title": "La Fiesta Nacional de España (12 de octubre) y el Día de la Constitución (6 de diciembre)",
            "goal": "Distinguish Spain's two principal civic national holidays tested on the CCSE exam: October 12 (Fiesta Nacional de España, Law 18/1987) and December 6 (Día de la Constitución).",
            "grammar_slug": "celebrarse-el-dia",
            "grammar_title": "Calendario cívico y efemérides: 'celebrarse el + fecha' y 'con motivo de'",
            "grammar_summary": "Using 'celebrarse el 12 de octubre' and 'con motivo de' for national civic holidays.",
            "grammar_text": "Law 18/1987 establishes **October 12** ('el 12 de octubre') as the **Fiesta Nacional de España** (National Day of Spain), commemorating the historical projection of Spain beyond Europe initiated in 1492 and its linguistic and cultural bond with the Ibero-American community of nations. Alongside October 12, Spain celebrates **December 6** ('el 6 de diciembre') as the **Día de la Constitución**, marking the 1978 referendum in which citizens approved the Constitution.",
            "grammar_examples": [
                {"spanish": "La Fiesta Nacional de España se celebra cada año el 12 de octubre.", "english": "The National Day of Spain is celebrated every year on October 12."},
                {"spanish": "El 6 de diciembre es festivo en toda España con motivo del Día de la Constitución.", "english": "December 6 is a holiday throughout Spain on the occasion of Constitution Day."},
                {"spanish": "El puente de diciembre une el Día de la Constitución (6 de diciembre) con el 8 de diciembre.", "english": "The December long weekend links Constitution Day (December 6) with December 8."}
            ],
            "grammar_tip": "Never confuse these three key dates on the CCSE exam: **12 de octubre** = Fiesta Nacional de España; **6 de diciembre** = Día de la Constitución; **9 de mayo** = Día de Europa.",
            "story_title": "Octubre y diciembre en el calendario cívico",
            "story_summary": "A family in Madrid watches the October 12 National Day parade and visits the Open Doors Day at the Congress of Deputies on December 6, Constitution Day.",
            "story_location": "Madrid",
            "story_paragraphs": [
                "En el calendario laboral y cívico de todos los españoles destacan dos fechas institucionales de ámbito nacional: el 12 de octubre y el 6 de diciembre.",
                "El 12 de octubre se celebra la Fiesta Nacional de España, establecida por la Ley 18/1987. Esta fecha conmemora la efeméride histórica de 1492, momento en que se inició el contacto entre Europa y América y comenzó la proyección lingüística y cultural de España más allá del continente europeo.",
                "Cada 12 de octubre tiene lugar en Madrid un acto solemne presidido por los Reyes de España, con un homenaje a la bandera nacional y el tradicional desfile de las Fuerzas Armadas y de los Cuerpos de Seguridad del Estado, además de celebrarse el Día de la Hispanidad en numerosos países hispanohablantes.",
                "Semanas más tarde, el 6 de diciembre, toda España celebra el Día de la Constitución, en recuerdo del referéndum del 6 de diciembre de 1978 en el que el pueblo español ratificó mayoritariamente la vigente Carta Magna.",
                "Con motivo del 6 de diciembre, el Congreso de los Diputados, el Senado y otros edificios constitucionales organizan jornadas de puertas abiertas para que los ciudadanos puedan recorrer libremente los salones donde se debaten y aprueban las leyes."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué fecha se celebra la Fiesta Nacional de España?",
                    "options": ["El 12 de octubre.", "El 6 de diciembre.", "El 2 de mayo."],
                    "correctIndex": 0,
                    "explanation": "La Ley 18/1987 establece el 12 de octubre como el día de la Fiesta Nacional de España."
                },
                {
                    "question": "¿Qué se conmemora en toda España el día 6 de diciembre?",
                    "options": ["El Día de la Constitución (aniversario del referéndum de 1978).", "El ingreso de España en la Unión Europea.", "El Día de las Fuerzas Armadas."],
                    "correctIndex": 0,
                    "explanation": "El 6 de diciembre se celebra el Día de la Constitución en recuerdo del referéndum del 6 de diciembre de 1978."
                },
                {
                    "question": "¿Quién preside cada 12 de octubre en Madrid el acto institucional y el desfile de la Fiesta Nacional de España?",
                    "options": ["El Rey de España (junto a la Familia Real y el Gobierno).", "El Presidente de la Comisión Europea.", "El Defensor del Pueblo."],
                    "correctIndex": 0,
                    "explanation": "El Rey, como Jefe del Estado y mando supremo de las Fuerzas Armadas, preside el acto central de la Fiesta Nacional el 12 de octubre."
                }
            ],
            "vocab": [
                {"lemma": "Fiesta Nacional de España", "pos": "noun", "translation": "National Day of Spain (October 12)", "ex_es": "La Fiesta Nacional de España se celebra el 12 de octubre en todo el país.", "ex_en": "The National Day of Spain is celebrated on October 12 throughout the country."},
                {"lemma": "Día de la Constitución", "pos": "noun", "translation": "Constitution Day (December 6)", "ex_es": "El 6 de diciembre es fiesta nacional por el Día de la Constitución.", "ex_en": "December 6 is a national holiday for Constitution Day."},
                {"lemma": "efeméride", "pos": "noun", "translation": "historical anniversary / milestone date", "ex_es": "El 12 de octubre recuerda una efeméride clave en la historia de España y América.", "ex_en": "October 12 commemorates a key historical anniversary in the history of Spain and the Americas."},
                {"lemma": "desfile", "pos": "noun", "translation": "parade", "ex_es": "El 12 de octubre se celebra en Madrid el tradicional desfile de las Fuerzas Armadas.", "ex_en": "On October 12 the traditional parade of the Armed Forces is held in Madrid."},
                {"lemma": "jornada de puertas abiertas", "pos": "noun", "translation": "open house / open doors day", "ex_es": "El Congreso organiza una jornada de puertas abiertas cada 6 de diciembre.", "ex_en": "Congress organizes an open doors day every December 6."},
                {"lemma": "festivo", "pos": "adjective", "translation": "public holiday / non-working day", "ex_es": "Tanto el 12 de octubre como el 6 de diciembre son días festivos nacionales.", "ex_en": "Both October 12 and December 6 are national public holidays."},
                {"lemma": "homenaje", "pos": "noun", "translation": "tribute / homage", "ex_es": "Durante el acto institucional se rinde homenaje a la bandera de España.", "ex_en": "During the institutional ceremony tribute is paid to the flag of Spain."},
                {"lemma": "proyección", "pos": "noun", "translation": "projection / outreach", "ex_es": "La Ley 18/1987 destaca la proyección lingüística y cultural de España.", "ex_en": "Law 18/1987 highlights the linguistic and cultural projection of Spain."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué día se celebra la Fiesta Nacional de España?", "options": ["El 12 de octubre", "El 6 de diciembre", "El 15 de agosto", "El 24 de junio"], "answer": "El 12 de octubre", "explanation": "El 12 de octubre es la Fiesta Nacional de España según la Ley 18/1987."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué día se celebra el Día de la Constitución en España?", "options": ["El 6 de diciembre", "El 12 de octubre", "El 9 de mayo", "El 1 de mayo"], "answer": "El 6 de diciembre", "explanation": "El 6 de diciembre conmemora el referéndum constitucional de 1978."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El 12 de ___ se celebra en toda España el día de la Fiesta Nacional.", "answer": "octubre", "english": "On October 12 the National Day is celebrated throughout Spain.", "explanation": "'12 de octubre' = Fiesta Nacional de España."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El 6 de ___ es festivo nacional porque se celebra el Día de la Constitución.", "answer": "diciembre", "english": "December 6 is a national holiday because Constitution Day is celebrated.", "explanation": "'6 de diciembre' = Día de la Constitución."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Spain's National Day:", "words": ["La", "Fiesta", "Nacional", "de", "España", "se", "celebra", "el", "doce", "de", "octubre."], "answer": "La Fiesta Nacional de España se celebra el doce de octubre.", "english": "The National Day of Spain is celebrated on October 12."},
                {"type": "dictation", "cat": "listening", "text": "El seis de diciembre celebramos el Día de la Constitución Española.", "english": "On December 6 we celebrate Spanish Constitution Day."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Por qué se eligió el 6 de diciembre como Día de la Constitución?", "options": ["Porque ese día de 1978 los ciudadanos españoles aprobaron la Constitución en referéndum", "Porque ese día España ingresó en la Unión Europea", "Porque ese día se adoptó el euro", "Porque es el inicio del invierno"], "answer": "Porque ese día de 1978 los ciudadanos españoles aprobaron la Constitución en referéndum", "explanation": "El 6 de diciembre de 1978 se celebró el referéndum de ratificación de la Constitución."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Cada 12 de octubre los Reyes presiden el tradicional ___ militar en Madrid.", "answer": "desfile", "english": "Every October 12 the King and Queen preside over the traditional military parade in Madrid.", "explanation": "'Desfile' means parade."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the open house at Congress:", "words": ["El", "Congreso", "celebra", "jornadas", "de", "puertas", "abiertas", "el", "seis", "de", "diciembre."], "answer": "El Congreso celebra jornadas de puertas abiertas el seis de diciembre.", "english": "Congress holds open doors days on December 6."}
            ]
        },
        {
            "num": "05",
            "story_slug": "premios",
            "title": "Distinciones y grandes reconocimientos: los Premios Princesa de Asturias y el Premio Cervantes",
            "goal": "Know Spain's most prestigious institutional awards tested on the CCSE exam: the Premios Princesa de Asturias (delivered every October at the Teatro Campoamor in Oviedo) and the Premio Cervantes (delivered every April 23 at the University of Alcalá de Henares).",
            "grammar_slug": "otorgarse-anualmente-a",
            "grammar_title": "Reconocimientos institucionales: 'otorgarse anualmente a' y 'hacer entrega de'",
            "grammar_summary": "Using 'otorgarse anualmente a' and 'hacer entrega de los galardones en' to describe official awards.",
            "grammar_text": "To describe institutional honors and prizes, Spanish uses 'otorgarse / concederse anualmente a' (to be awarded annually to) and 'hacer entrega de los galardones en + lugar' (to present the awards at...). Two major prizes appear frequently on the CCSE exam: the **Premios Princesa de Asturias**, presented every autumn in **Oviedo** (Asturias) across eight international categories (Arts, Literature, Social Sciences, Communication and Humanities, Technical and Scientific Research, International Cooperation, Concord, and Sports), and the **Premio de Literatura en Lengua Castellana Miguel de Cervantes** (the **Premio Cervantes**), the highest literary honor in Spanish, presented by the King every **April 23** at the **University of Alcalá de Henares**.",
            "grammar_examples": [
                {"spanish": "Los Premios Princesa de Asturias se entregan anualmente en el Teatro Campoamor de Oviedo.", "english": "The Princess of Asturias Awards are presented annually at the Campoamor Theater in Oviedo."},
                {"spanish": "El Premio Cervantes se otorga cada año a la trayectoria de un gran escritor en lengua española.", "english": "The Cervantes Prize is awarded every year to the career of a great writer in the Spanish language."},
                {"spanish": "El Rey hace entrega del Premio Cervantes el 23 de abril en la Universidad de Alcalá de Henares.", "english": "The King presents the Cervantes Prize on April 23 at the University of Alcalá de Henares."}
            ],
            "grammar_tip": "Memorize the cities for these two iconic CCSE questions: **Premios Princesa de Asturias** = **Oviedo** (Teatro Campoamor); **Premio Cervantes** = **Alcalá de Henares** (April 23, Día del Libro).",
            "story_title": "De Oviedo a Alcalá de Henares: la excelencia premiada",
            "story_summary": "From the sound of bagpipes at Oviedo's Teatro Campoamor in October to the Renaissance courtyard of the University of Alcalá de Henares on April 23, Spain celebrates universal science, concord, and Hispanic literature.",
            "story_location": "Oviedo y Alcalá de Henares",
            "story_paragraphs": [
                "Además de sus símbolos constitucionales y condecoraciones de Estado —como la Real Orden de Carlos III o la Orden de Isabel la Católica—, España proyecta sus valores culturales y científicos al mundo a través de dos grandes premios de prestigio internacional.",
                "Cada mes de octubre, la ciudad de Oviedo, capital del Principado de Asturias, acoge en el histórico Teatro Campoamor la ceremonia de entrega de los Premios Princesa de Asturias.",
                "Estos galardones internacionales se conceden anualmente en ocho categorías: Artes, Letras, Ciencias Sociales, Comunicación y Humanidades, Investigación Científica y Técnica, Cooperación Internacional, Concordia y Deportes, reconociendo a personas e instituciones de todo el mundo.",
                "En el ámbito de las letras hispánicas, el máximo reconocimiento mundial es el Premio de Literatura en Lengua Castellana Miguel de Cervantes, concedido por el Ministerio de Cultura a propuesta de las Academias de la Lengua Española.",
                "Cada 23 de abril —Día Internacional del Libro y aniversario del fallecimiento de Miguel de Cervantes en 1616—, los Reyes de España entregan el Premio Cervantes en el Paraninfo de la Universidad de Alcalá de Henares, ciudad natal del autor del *Quijote*."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué ciudad española se entregan cada año los Premios Princesa de Asturias?",
                    "options": ["En Oviedo (en el Teatro Campoamor).", "En Sevilla.", "En Valladolid."],
                    "correctIndex": 0,
                    "explanation": "Los Premios Princesa de Asturias se entregan anualmente en el Teatro Campoamor de Oviedo, capital del Principado de Asturias."
                },
                {
                    "question": "¿Cuál es el galardón más importante que se concede en España a los escritores en lengua castellana, entregado cada 23 de abril en la Universidad de Alcalá de Henares?",
                    "options": ["El Premio Miguel de Cervantes (Premio Cervantes).", "El Premio Goya.", "La Medalla al Mérito Deportivo."],
                    "correctIndex": 0,
                    "explanation": "El Premio Cervantes es el máximo reconocimiento a la labor creadora de escritores españoles e hispanoamericanos en lengua castellana."
                },
                {
                    "question": "¿Qué se celebra cada 23 de abril coincidiendo con la entrega del Premio Cervantes?",
                    "options": ["El Día Internacional del Libro.", "El Día de la Constitución.", "El Día de Europa."],
                    "correctIndex": 0,
                    "explanation": "El 23 de abril se celebra el Día Internacional del Libro en conmemoración de la muerte de Miguel de Cervantes y William Shakespeare en 1616."
                }
            ],
            "vocab": [
                {"lemma": "Premios Princesa de Asturias", "pos": "noun", "translation": "Princess of Asturias Awards", "ex_es": "Los Premios Princesa de Asturias se entregan en el Teatro Campoamor de Oviedo.", "ex_en": "The Princess of Asturias Awards are presented at the Campoamor Theater in Oviedo."},
                {"lemma": "Premio Cervantes", "pos": "noun", "translation": "Cervantes Prize (highest Spanish-language literary award)", "ex_es": "El Premio Cervantes reconoce la obra completa de grandes autores en lengua española.", "ex_en": "The Cervantes Prize recognizes the complete work of great authors in the Spanish language."},
                {"lemma": "Oviedo", "pos": "noun", "translation": "Oviedo (capital of Asturias)", "ex_es": "Oviedo es la sede de la Fundación y de los Premios Princesa de Asturias.", "ex_en": "Oviedo is the seat of the Princess of Asturias Foundation and Awards."},
                {"lemma": "Alcalá de Henares", "pos": "noun", "translation": "Alcalá de Henares (birthplace of Cervantes)", "ex_es": "El Premio Cervantes se entrega en el Paraninfo de la Universidad de Alcalá de Henares.", "ex_en": "The Cervantes Prize is presented in the Great Hall of the University of Alcalá de Henares."},
                {"lemma": "galardón", "pos": "noun", "translation": "award / prize", "ex_es": "Este galardón premia la cooperación internacional, las artes, las ciencias y la concordia.", "ex_en": "This award honors international cooperation, the arts, sciences, and concord."},
                {"lemma": "Día del Libro", "pos": "noun", "translation": "World Book Day (April 23)", "ex_es": "El 23 de abril se celebra en toda España el Día del Libro.", "ex_en": "On April 23 Book Day is celebrated throughout Spain."},
                {"lemma": "concordia", "pos": "noun", "translation": "concord / harmony and peace", "ex_es": "El Premio Princesa de Asturias de la Concordia distingue la defensa de los derechos humanos y la paz.", "ex_en": "The Princess of Asturias Award for Concord distinguishes the defense of human rights and peace."},
                {"lemma": "trayectoria", "pos": "noun", "translation": "career / life's work", "ex_es": "El Premio Cervantes distingue toda la trayectoria literaria de un escritor.", "ex_en": "The Cervantes Prize honors the entire literary career of a writer."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué ciudad de España se entregan anualmente los Premios Princesa de Asturias?", "options": ["En Oviedo", "En Málaga", "En Zaragoza", "En Santander"], "answer": "En Oviedo", "explanation": "Los Premios Princesa de Asturias se entregan en el Teatro Campoamor de Oviedo (Asturias)."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué premio es el máximo reconocimiento oficial a la literatura en lengua española y se entrega el 23 de abril en Alcalá de Henares?", "options": ["El Premio Cervantes", "El Premio Goya", "El Premio Planeta", "La Medalla de Oro de las Bellas Artes"], "answer": "El Premio Cervantes", "explanation": "El Premio de Literatura en Lengua Castellana Miguel de Cervantes se entrega cada 23 de abril en la Universidad de Alcalá de Henares."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los Premios Princesa de Asturias se entregan cada otoño en el Teatro Campoamor de ___.", "answer": "Oviedo", "english": "The Princess of Asturias Awards are presented every autumn at the Campoamor Theater in Oviedo.", "explanation": "Oviedo is the capital of Asturias."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El 23 de abril se celebra el Día del ___ y se entrega el Premio Cervantes.", "answer": "Libro", "english": "On April 23 Book Day is celebrated and the Cervantes Prize is presented.", "explanation": "'Día del Libro' (April 23)."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the Princess of Asturias Awards:", "words": ["Los", "Premios", "Princesa", "de", "Asturias", "se", "entregan", "anualmente", "en", "Oviedo."], "answer": "Los Premios Princesa de Asturias se entregan anualmente en Oviedo.", "english": "The Princess of Asturias Awards are presented annually in Oviedo."},
                {"type": "dictation", "cat": "listening", "text": "El Premio Cervantes es el máximo galardón de las letras en español.", "english": "The Cervantes Prize is the highest award for literature in Spanish."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Dónde nació Miguel de Cervantes y se entrega cada año el premio que lleva su nombre?", "options": ["En Alcalá de Henares (Madrid)", "En Burgos", "En Alicante", "En Vigo"], "answer": "En Alcalá de Henares (Madrid)", "explanation": "Miguel de Cervantes nació en Alcalá de Henares en 1547 y allí se entrega el Premio Cervantes."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Premio ___ reconoce la trayectoria de escritores españoles e hispanoamericanos.", "answer": "Cervantes", "english": "The Cervantes Prize recognizes the career of Spanish and Hispanic American writers.", "explanation": "'El Premio Cervantes'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the Cervantes Prize ceremony:", "words": ["El", "Rey", "entrega", "el", "Premio", "Cervantes", "en", "Alcalá", "de", "Henares."], "answer": "El Rey entrega el Premio Cervantes en Alcalá de Henares.", "english": "The King presents the Cervantes Prize in Alcalá de Henares."}
            ]
        }
    ],
    "consolidation_exercises": [
        {"type": "multiple-choice", "cat": "grammar", "prompt": "Según el artículo 4.1 de la Constitución, ¿cómo son las tres franjas de la bandera de España?", "options": ["Tres franjas horizontales (roja, amarilla y roja), siendo la amarilla de doble anchura que cada roja", "Tres franjas verticales iguales", "Dos franjas rojas y una blanca", "Tres franjas horizontales de igual anchura"], "answer": "Tres franjas horizontales (roja, amarilla y roja), siendo la amarilla de doble anchura que cada roja", "explanation": "Artículo 4.1 de la Constitución."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué lema aparece inscrito en las Columnas de Hércules del Escudo de España?", "options": ["Plus Ultra", "Unida en la diversidad", "Libertad e Igualdad", "In hoc signo vinces"], "answer": "Plus Ultra", "explanation": "«Plus Ultra» («Más allá») figura en el Escudo de España."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cómo se llama el Himno Nacional de España?", "options": ["La Marcha Real (o Marcha Granadera)", "El Himno de la Alegría", "El Canto de España", "La Marcha Triunfal"], "answer": "La Marcha Real (o Marcha Granadera)", "explanation": "El Himno Nacional es la «Marcha Real» o «Marcha Granadera»."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál de las siguientes afirmaciones sobre el Himno Nacional de España es verdadera?", "options": ["No tiene letra oficial (es exclusivamente instrumental)", "Tiene cuatro estrofas oficiales en castellano", "Se canta únicamente en latín", "Fue compuesto en el año 1978"], "answer": "No tiene letra oficial (es exclusivamente instrumental)", "explanation": "La Marcha Real carece de letra oficial."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué fechas se celebran respectivamente la Fiesta Nacional de España y el Día de la Constitución?", "options": ["El 12 de octubre y el 6 de diciembre", "El 6 de diciembre y el 9 de mayo", "El 23 de abril y el 1 de enero", "El 2 de mayo y el 15 de agosto"], "answer": "El 12 de octubre y el 6 de diciembre", "explanation": "Fiesta Nacional = 12 de octubre; Día de la Constitución = 6 de diciembre."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué ciudad se entregan anualmente los Premios Princesa de Asturias?", "options": ["En Oviedo", "En Barcelona", "En Sevilla", "En Valencia"], "answer": "En Oviedo", "explanation": "En el Teatro Campoamor de Oviedo."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "La franja central amarilla de la bandera de España es de ___ anchura que cada una de las rojas.", "answer": "doble", "english": "The central yellow stripe of the flag of Spain is twice the width of each of the red ones.", "explanation": "'Doble anchura'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "En la parte inferior del Escudo de España figura una ___ que representa al Reino de Granada.", "answer": "granada", "english": "At the bottom of the Coat of Arms of Spain appears a pomegranate representing the Kingdom of Granada.", "explanation": "'Una granada'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Himno Nacional de España es la «Marcha ___» y carece de letra oficial.", "answer": "Real", "english": "The National Anthem of Spain is the 'Marcha Real' and has no official lyrics.", "explanation": "'La Marcha Real'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El 12 de ___ se celebra la Fiesta Nacional de España.", "answer": "octubre", "english": "On October 12 the National Day of Spain is celebrated.", "explanation": "'12 de octubre'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El 6 de ___ se celebra el Día de la Constitución Española.", "answer": "diciembre", "english": "On December 6 Spanish Constitution Day is celebrated.", "explanation": "'6 de diciembre'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Premio ___ de literatura se entrega el 23 de abril en Alcalá de Henares.", "answer": "Cervantes", "english": "The Cervantes Prize for literature is presented on April 23 in Alcalá de Henares.", "explanation": "'Premio Cervantes'."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the Spanish flag:", "words": ["La", "bandera", "española", "está", "formada", "por", "tres", "franjas", "horizontales."], "answer": "La bandera española está formada por tres franjas horizontales.", "english": "The Spanish flag is formed by three horizontal stripes."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the motto on the Coat of Arms:", "words": ["El", "lema", "Plus", "Ultra", "aparece", "en", "el", "Escudo", "de", "España."], "answer": "El lema Plus Ultra aparece en el Escudo de España.", "english": "The motto Plus Ultra appears on the Coat of Arms of Spain."},
        {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Order the sentence about the Princess of Asturias Awards:", "words": ["Los", "Premios", "Princesa", "de", "Asturias", "se", "entregan", "en", "el", "Teatro", "Campoamor", "de", "Oviedo."], "answer": "Los Premios Princesa de Asturias se entregan en el Teatro Campoamor de Oviedo.", "english": "The Princess of Asturias Awards are presented at the Campoamor Theater in Oviedo."},
        {"type": "dictation", "cat": "listening", "text": "La bandera de España tiene tres franjas horizontales: roja, amarilla y roja.", "english": "The flag of Spain has three horizontal stripes: red, yellow, and red."},
        {"type": "dictation", "cat": "listening", "text": "La Fiesta Nacional de España se celebra el doce de octubre.", "english": "The National Day of Spain is celebrated on October 12."},
        {"type": "dictation", "cat": "listening", "text": "El Himno Nacional de España no tiene letra oficial.", "english": "The National Anthem of Spain has no official lyrics."}
    ]
}

UNIT_11 = {
    "slug": "lenguas",
    "legacy_prefix": "b1-ccse-lenguas",
    "unit_title": "El Castellano y las Lenguas Cooficiales",
    "order": 11,
    "unit_summary": "Complete CCSE guide to Languages in Spain (Article 3 of the Constitution): Castilian Spanish as the official language of the State (duty to know and right to use), the co-official languages in their respective Autonomous Communities (Catalan, Valencian, Galician, Basque/Euskera, and Aranese), the Real Academia Española (RAE) and ASALE, and linguistic diversity as cultural heritage.",
    "unit_paragraphs": [],
    "unit_questions": [],
    "lessons": [
        {
            "num": "01",
            "story_slug": "castellano",
            "title": "El artículo 3 de la Constitución: el castellano y el patrimonio plurilingüe",
            "goal": "Understand all three paragraphs of Article 3 of the Constitution: Castilian as the official language of the State (duty to know and right to use), co-official languages according to Statutes of Autonomy, and linguistic modalities as cultural heritage worthy of special respect and protection.",
            "grammar_slug": "especial-respeto-y-proteccion",
            "grammar_title": "Deber, derecho y protección constitucional: 'el deber de conocerla', 'el derecho a usarla' y 'ser objeto de'",
            "grammar_summary": "Mastering the three clauses of Article 3 ('el deber de conocerla y el derecho a usarla', 'ser objeto de especial respeto y protección').",
            "grammar_text": "Article 3 of the Preliminary Title is structured in three balanced clauses: 1) 'El castellano es la lengua española oficial del Estado. Todos los españoles tienen el deber de conocerla y el derecho a usarla.' 2) 'Las demás lenguas españolas serán también oficiales en las respectivas Comunidades Autónomas de acuerdo con sus Estatutos.' 3) 'La riqueza de las distintas modalidades lingüísticas de España es un patrimonio cultural que será objeto de especial respeto y protección.'",
            "grammar_examples": [
                {"spanish": "Todos los españoles tienen el deber de conocer el castellano y el derecho a usarlo.", "english": "All Spaniards have the duty to know Castilian Spanish and the right to use it."},
                {"spanish": "Las demás lenguas españolas son también oficiales en sus respectivas comunidades autónomas.", "english": "The other Spanish languages are also official in their respective autonomous communities."},
                {"spanish": "La riqueza de las distintas modalidades lingüísticas es un patrimonio cultural objeto de especial respeto y protección.", "english": "The richness of the different linguistic modalities is a cultural heritage subject to special respect and protection."}
            ],
            "grammar_tip": "Note the exact wording of Article 3.1: for Castilian Spanish, citizens have BOTH the **duty** to know it ('el deber de conocerla') AND the **right** to use it ('el derecho a usarla') throughout the entire State.",
            "story_title": "Una biblioteca con muchas voces",
            "story_summary": "At the National Library of Spain in Madrid, a philologist shows how Article 3 of the 1978 Constitution turned Spain's linguistic diversity into a protected cultural treasure alongside the common language, Castilian.",
            "story_location": "Madrid, Biblioteca Nacional de España",
            "story_paragraphs": [
                "En los fondos de la Biblioteca Nacional de España, en el paseo de Recoletos de Madrid, se conservan manuscritos medievales e impresos modernos escritos no solo en castellano, sino también en catalán, gallego, valenciano, euskera, aranés, bable asturiano o fabla aragonesa.",
                "El artículo 3 del Título Preliminar de la Constitución Española de 1978 regula esta realidad histórica en tres apartados complementarios.",
                "El artículo 3.1 establece que el castellano es la lengua española oficial del Estado, y que todos los españoles tienen el deber de conocerla y el derecho a usarla en cualquier punto del territorio nacional.",
                "El artículo 3.2 añade que las demás lenguas españolas serán también oficiales en las respectivas comunidades autónomas de acuerdo con sus Estatutos de Autonomía, compartiendo rango de cooficialidad con el castellano en sus territorios.",
                "Finalmente, el artículo 3.3 proclama que la riqueza de las distintas modalidades lingüísticas de España es un patrimonio cultural que será objeto de especial respeto y protección por parte de todos los poderes públicos."
            ],
            "comp_questions": [
                {
                    "question": "Según el artículo 3.1 de la Constitución Española, ¿cuál es la lengua oficial de todo el Estado español?",
                    "options": ["El castellano.", "El latín.", "El inglés junto al castellano."],
                    "correctIndex": 0,
                    "explanation": "El artículo 3.1 dispone que el castellano es la lengua española oficial del Estado."
                },
                {
                    "question": "¿Qué establece el artículo 3.1 respecto a los ciudadanos españoles y la lengua castellana?",
                    "options": ["Que todos los españoles tienen el deber de conocerla y el derecho a usarla.", "Que su aprendizaje es opcional según la provincia.", "Que solo se emplea en las relaciones diplomáticas."],
                    "correctIndex": 0,
                    "explanation": "Todos los españoles tienen el deber de conocer el castellano y el derecho a usarlo."
                },
                {
                    "question": "¿Cómo considera el artículo 3.3 de la Constitución la riqueza de las distintas modalidades lingüísticas de España?",
                    "options": ["Un patrimonio cultural que será objeto de especial respeto y protección.", "Una barrera administrativa que debe suprimirse.", "Un asunto privado ajeno a las leyes."],
                    "correctIndex": 0,
                    "explanation": "El artículo 3.3 declara que la riqueza de las distintas modalidades lingüísticas es un patrimonio cultural que será objeto de especial respeto y protección."
                }
            ],
            "vocab": [
                {"lemma": "castellano", "pos": "noun", "translation": "Castilian / Spanish language", "ex_es": "El castellano es la lengua española oficial de todo el Estado.", "ex_en": "Castilian is the official Spanish language of the entire State."},
                {"lemma": "cooficial", "pos": "adjective", "translation": "co-official", "ex_es": "Seis comunidades autónomas cuentan con una lengua cooficial junto al castellano.", "ex_en": "Six autonomous communities have a co-official language alongside Castilian."},
                {"lemma": "modalidad lingüística", "pos": "noun", "translation": "linguistic variety / modality", "ex_es": "Cada modalidad lingüística de España forma parte del patrimonio cultural.", "ex_en": "Every linguistic modality of Spain forms part of the cultural heritage."},
                {"lemma": "patrimonio cultural", "pos": "noun", "translation": "cultural heritage", "ex_es": "El plurilingüismo español es un patrimonio cultural protegido por la Constitución.", "ex_en": "Spanish multilingualism is a cultural heritage protected by the Constitution."},
                {"lemma": "bilingüe", "pos": "adjective", "translation": "bilingual", "ex_es": "En las comunidades bilingües la educación y la administración emplean ambas lenguas oficiales.", "ex_en": "In bilingual communities education and administration use both official languages."},
                {"lemma": "lengua materna", "pos": "noun", "translation": "mother tongue / native language", "ex_es": "El español es la segunda lengua del mundo por número de hablantes como lengua materna.", "ex_en": "Spanish is the second language in the world by number of native speakers."},
                {"lemma": "hablante", "pos": "noun", "translation": "speaker", "ex_es": "Más de quinientos millones de hablantes se comunican hoy en español.", "ex_en": "More than five hundred million speakers communicate in Spanish today."},
                {"lemma": "protección", "pos": "noun", "translation": "protection", "ex_es": "Las lenguas españolas gozan de especial respeto y protección institucional.", "ex_en": "The Spanish languages enjoy special institutional respect and protection."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "Según la Constitución Española, ¿cuál es la lengua oficial de todo el Estado?", "options": ["El castellano", "El catalán", "El euskera", "El gallego"], "answer": "El castellano", "explanation": "El artículo 3.1 establece que el castellano es la lengua española oficial del Estado."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué tienen todos los españoles respecto a la lengua castellana según el artículo 3.1?", "options": ["El deber de conocerla y el derecho a usarla", "Solo el derecho a usarla sin deber de conocerla", "La obligación de hablar únicamente castellano en casa", "El deber de traducirla al latín"], "answer": "El deber de conocerla y el derecho a usarla", "explanation": "Artículo 3.1: «Todos los españoles tienen el deber de conocerla y el derecho a usarla»."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La riqueza de las distintas modalidades lingüísticas de España es un ___ cultural.", "answer": "patrimonio", "english": "The richness of the different linguistic modalities of Spain is a cultural heritage.", "explanation": "'Patrimonio cultural' (Article 3.3)."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Las demás lenguas españolas son también ___ en sus respectivas comunidades autónomas.", "answer": "oficiales", "english": "The other Spanish languages are also official in their respective autonomous communities.", "explanation": "Artículo 3.2: 'serán también oficiales'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order Article 3.1 of the Spanish Constitution:", "words": ["El", "castellano", "es", "la", "lengua", "española", "oficial", "del", "Estado."], "answer": "El castellano es la lengua española oficial del Estado.", "english": "Castilian is the official Spanish language of the State."},
                {"type": "dictation", "cat": "listening", "text": "Todos los españoles tienen el deber de conocer el castellano y el derecho a usarlo.", "english": "All Spaniards have the duty to know Castilian and the right to use it."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué texto legal determina la cooficialidad de una lengua propia en una comunidad autónoma?", "options": ["Su respectivo Estatuto de Autonomía (de acuerdo con el artículo 3.2 de la Constitución)", "Un decreto municipal de cada alcaldía", "El reglamento de la Dirección General de Tráfico", "El Tratado de Schengen"], "answer": "Su respectivo Estatuto de Autonomía (de acuerdo con el artículo 3.2 de la Constitución)", "explanation": "El artículo 3.2 señala que serán también oficiales en las respectivas Comunidades Autónomas de acuerdo con sus Estatutos."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Las modalidades lingüísticas de España son objeto de especial respeto y ___.", "answer": "protección", "english": "The linguistic modalities of Spain are the object of special respect and protection.", "explanation": "'Especial respeto y protección'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about linguistic heritage:", "words": ["La", "diversidad", "lingüística", "de", "España", "es", "un", "patrimonio", "cultural", "protegido."], "answer": "La diversidad lingüística de España es un patrimonio cultural protegido.", "english": "The linguistic diversity of Spain is a protected cultural heritage."}
            ]
        },
        {
            "num": "02",
            "story_slug": "catalanvalenciano",
            "title": "El catalán, el valenciano y el aranés en el arco mediterráneo y el Pirineo",
            "goal": "Know the co-official languages of Catalonia (Catalan and Aranese/Occitan), the Valencian Community (Valencian), and the Balearic Islands (Catalan).",
            "grammar_slug": "junto-con-el-castellano",
            "grammar_title": "Cooficialidad territorial: 'ser cooficial junto con el castellano en'",
            "grammar_summary": "Using 'ser lengua propia y cooficial junto con el castellano en...' to map languages to Autonomous Communities.",
            "grammar_text": "To express where each Romance co-official language is spoken, Spanish administrative prose uses 'ser cooficial junto con el castellano en + Comunidad Autónoma'. In **Cataluña** and the **Islas Baleares**, **el catalán** is co-official with Castilian; in addition, in the Pyrenean valley of **Val d'Aran** (Catalonia), **el aranés** (a variety of Occitan) is also official across Catalonia since the 2006 Statute of Autonomy. In the **Comunidad Valenciana**, the co-official language according to its Statute of Autonomy is **el valenciano**.",
            "grammar_examples": [
                {"spanish": "El catalán es lengua cooficial junto con el castellano en Cataluña y en las Islas Baleares.", "english": "Catalan is a co-official language alongside Castilian in Catalonia and in the Balearic Islands."},
                {"spanish": "En la Comunidad Valenciana la lengua propia y cooficial con el castellano se denomina valenciano.", "english": "In the Valencian Community the own and co-official language with Castilian is called Valencian."},
                {"spanish": "En Cataluña también es oficial el aranés, hablado tradicionalmente en el Valle de Arán.", "english": "In Catalonia Aranese is also official, traditionally spoken in the Val d'Aran."}
            ],
            "grammar_tip": "Don't forget **el aranés** (Occitan of the Val d'Aran) — Catalonia actually has THREE official languages under its Statute: Castilian, Catalan, and Aranese!",
            "story_title": "Del Mediterráneo a las cumbres del Valle de Arán",
            "story_summary": "Traveling from Palma de Mallorca and Valencia to Barcelona and the Pyrenean valley of Aran, a journalist hears Catalan, Valencian, and Aranese in schools, signs, and daily life.",
            "story_location": "Barcelona, Valencia, Palma y Vielha",
            "story_paragraphs": [
                "A lo largo de la costa mediterránea española y en las islas del archipiélago balear, millones de ciudadanos viven en un entorno bilingüe donde las lenguas romances nacidas del latín conviven diariamente en la escuela, los medios de comunicación y la administración pública.",
                "En Cataluña y en las Islas Baleares, el catalán es lengua oficial junto con el castellano. Cuenta con una rica tradición literaria que se remonta a la Edad Media, con figuras como Ramon Llull o Ausiàs March, y con instituciones académicas como el Institut d'Estudis Catalans.",
                "Además, en el extremo noroccidental del Pirineo catalán se encuentra el Valle de Arán (Val d'Aran), donde se habla el aranés, una variedad de la lengua occitana que el Estatuto de Autonomía de Cataluña reconoce también como lengua oficial.",
                "Por su parte, en la Comunidad Valenciana (integrada por las provincias de Castellón, Valencia y Alicante), el Estatuto de Autonomía establece que la lengua propia es el valenciano, oficial en toda la comunidad junto con el castellano y regulado normativamente por la Acadèmia Valenciana de la Llengua.",
                "En todas estas comunidades, las señales de tráfico, los impresos administrativos, la rotulación pública y el sistema educativo garantizan que los ciudadanos puedan expresarse y ser atendidos indistintamente en cualquiera de las lenguas oficiales."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué dos comunidades autónomas es lengua cooficial el catalán junto con el castellano?",
                    "options": ["En Cataluña y en las Islas Baleares.", "En Galicia y en Asturias.", "En Extremadura y en Murcia."],
                    "correctIndex": 0,
                    "explanation": "El catalán es lengua cooficial junto con el castellano en Cataluña y en las Islas Baleares."
                },
                {
                    "question": "¿Cuál es la lengua cooficial junto con el castellano en la Comunidad Valenciana según su Estatuto de Autonomía?",
                    "options": ["El valenciano.", "El euskera.", "El gallego."],
                    "correctIndex": 0,
                    "explanation": "Según el Estatuto de Autonomía de la Comunidad Valenciana, la lengua propia y cooficial junto con el castellano es el valenciano."
                },
                {
                    "question": "¿Qué tercera lengua, variedad del occitano hablada en el Valle de Arán, es también oficial en Cataluña?",
                    "options": ["El aranés.", "El bable.", "El silbo gomero."],
                    "correctIndex": 0,
                    "explanation": "El aranés (lengua occitana del Valle de Arán) es también lengua oficial en Cataluña junto con el castellano y el catalán."
                }
            ],
            "vocab": [
                {"lemma": "catalán", "pos": "noun", "translation": "Catalan language", "ex_es": "El catalán es cooficial junto con el castellano en Cataluña y en las Islas Baleares.", "ex_en": "Catalan is co-official alongside Castilian in Catalonia and in the Balearic Islands."},
                {"lemma": "valenciano", "pos": "noun", "translation": "Valencian language", "ex_es": "El valenciano es la lengua propia y cooficial de la Comunidad Valenciana.", "ex_en": "Valencian is the own and co-official language of the Valencian Community."},
                {"lemma": "aranés", "pos": "noun", "translation": "Aranese (Occitan variety spoken in Val d'Aran)", "ex_es": "El aranés se habla en el Valle de Arán y es lengua oficial en Cataluña.", "ex_en": "Aranese is spoken in the Val d'Aran and is an official language in Catalonia."},
                {"lemma": "lengua romance", "pos": "noun", "translation": "Romance language (derived from Latin)", "ex_es": "El castellano, el catalán, el valenciano, el gallego y el aranés son lenguas romances.", "ex_en": "Castilian, Catalan, Valencian, Galician, and Aranese are Romance languages."},
                {"lemma": "Islas Baleares", "pos": "noun", "translation": "Balearic Islands", "ex_es": "En las Islas Baleares son oficiales tanto el castellano como el catalán.", "ex_en": "In the Balearic Islands both Castilian and Catalan are official."},
                {"lemma": "Valle de Arán", "pos": "noun", "translation": "Aran Valley (Pyrenees, Lleida)", "ex_es": "El Valle de Arán se sitúa en el Pirineo de la provincia de Lleida.", "ex_en": "The Val d'Aran is located in the Pyrenees of the province of Lleida."},
                {"lemma": "lengua propia", "pos": "noun", "translation": "own / historical regional language", "ex_es": "Los Estatutos de Autonomía definen la lengua histórica de cada territorio como lengua propia.", "ex_en": "The Statutes of Autonomy define the historical language of each territory as its own language."},
                {"lemma": "rotulación", "pos": "noun", "translation": "signage / public signs", "ex_es": "La rotulación de las calles y estaciones es bilingüe en las comunidades con lengua cooficial.", "ex_en": "Street and station signage is bilingual in communities with a co-official language."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué comunidades autónomas es lengua cooficial el catalán junto al castellano?", "options": ["En Cataluña y en las Islas Baleares", "En Galicia y Cantabria", "En Navarra y La Rioja", "En Andalucía y Murcia"], "answer": "En Cataluña y en las Islas Baleares", "explanation": "El catalán es cooficial en Cataluña y en las Islas Baleares."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué lengua es cooficial junto con el castellano en la Comunidad Valenciana?", "options": ["El valenciano", "El gallego", "El euskera", "El aranés"], "answer": "El valenciano", "explanation": "El Estatuto de Autonomía de la Comunidad Valenciana establece la cooficialidad del valenciano."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En el Valle de Arán (Cataluña) se habla el ___, que también tiene carácter oficial.", "answer": "aranés", "english": "In the Val d'Aran (Catalonia) Aranese is spoken, which also has official status.", "explanation": "'El aranés' is the Occitan variety official in Catalonia."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En las Islas ___ son lenguas oficiales el castellano y el catalán.", "answer": "Baleares", "english": "In the Balearic Islands both Castilian and Catalan are official languages.", "explanation": "'Las Islas Baleares'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Valencian:", "words": ["El", "valenciano", "es", "lengua", "cooficial", "en", "la", "Comunidad", "Valenciana."], "answer": "El valenciano es lengua cooficial en la Comunidad Valenciana.", "english": "Valencian is a co-official language in the Valencian Community."},
                {"type": "dictation", "cat": "listening", "text": "El catalán es lengua oficial en Cataluña y en las Islas Baleares.", "english": "Catalan is an official language in Catalonia and in the Balearic Islands."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Dónde se habla el aranés en España?", "options": ["En el Valle de Arán (en el Pirineo de Cataluña)", "En las Islas Canarias", "En la provincia de Cádiz", "En la ciudad autónoma de Melilla"], "answer": "En el Valle de Arán (en el Pirineo de Cataluña)", "explanation": "El aranés es la lengua propia del Valle de Arán (Lleida, Cataluña)."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El castellano, el catalán y el gallego proceden del latín: son lenguas ___.", "answer": "romances", "english": "Castilian, Catalan, and Galician come from Latin: they are Romance languages.", "explanation": "'Lenguas romances' derive from Latin."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the three official languages of Catalonia:", "words": ["En", "Cataluña", "son", "oficiales", "el", "castellano,", "el", "catalán", "y", "el", "aranés."], "answer": "En Cataluña son oficiales el castellano, el catalán y el aranés.", "english": "In Catalonia Castilian, Catalan, and Aranese are official."}
            ]
        },
        {
            "num": "03",
            "story_slug": "gallegoeuskera",
            "title": "El gallego y el euskera (vasco): del Atlántico al singular idioma prerromano",
            "goal": "Know where Galician (Galicia) and Basque/Euskera (Basque Country and the Basque-speaking zone of Navarre) are co-official, and why Euskera is unique as Europe's oldest living pre-Roman (non-Indo-European) language.",
            "grammar_slug": "a-diferencia-de-las-demas",
            "grammar_title": "Contraste lingüístico: 'a diferencia de las demás lenguas' y 'no proceder de'",
            "grammar_summary": "Using 'a diferencia de las demás lenguas de España, el euskera no procede del latín' to contrast language families.",
            "grammar_text": "While Castilian, Catalan, Valencian, Galician, and Aranese are all Romance languages derived from Latin ('lenguas romances que proceden del latín'), **el euskera** (or **vasco**) stands out with 'a diferencia de las demás lenguas de España, no procede del latín ni pertenece a la familia indoeuropea' (unlike the other languages of Spain, it does not come from Latin nor belong to the Indo-European family). **El gallego** is co-official in **Galicia** (4 provinces: A Coruña, Lugo, Ourense, Pontevedra), while **el euskera** is co-official in the **País Vasco** and in the Basque-speaking areas of **Navarra**.",
            "grammar_examples": [
                {"spanish": "El gallego es la lengua propia y cooficial junto con el castellano en Galicia.", "english": "Galician is the own and co-official language alongside Castilian in Galicia."},
                {"spanish": "A diferencia de las demás lenguas de España, el euskera no procede del latín.", "english": "Unlike the other languages of Spain, Basque (Euskera) does not come from Latin."},
                {"spanish": "El euskera es lengua cooficial en el País Vasco y en las zonas vascófonas de Navarra.", "english": "Basque is a co-official language in the Basque Country and in the Basque-speaking areas of Navarre."}
            ],
            "grammar_tip": "Key CCSE linguistic question: Which official language in Spain does NOT derive from Latin ('no es una lengua romance')? **El euskera (o vasco)**.",
            "story_title": "Los versos de Rosalía y el misterio milenario del euskera",
            "story_summary": "From Santiago de Compostela, where Galician shares roots with Portuguese, to San Sebastián and northern Navarre, where Euskera preserves Europe's oldest pre-Roman tongue.",
            "story_location": "Santiago de Compostela y San Sebastián",
            "story_paragraphs": [
                "En el noroeste atlántico de la península ibérica, el gallego es la lengua propia y cooficial junto con el castellano en las cuatro provincias de Galicia: A Coruña, Lugo, Ourense y Pontevedra.",
                "Nacido del latín vulgar del antiguo Reino de Galicia en estrecha hermandad histórica con el portugués, el gallego vivió una brillante época medieval con las cantigas líricas de Alfonso X el Sabio y un renacimiento literario en el siglo XIX —el *Rexurdimento*— liderado por la poeta Rosalía de Castro.",
                "Si viajamos hacia el este por la cornisa cantábrica hasta el País Vasco y el norte de la Comunidad Foral de Navarra, escucharemos una lengua completamente distinta a todas las demás de Europa: el euskera (también llamado vasco o vascuence).",
                "A diferencia del castellano, el catalán, el valenciano, el gallego o el aranés, el euskera no procede del latín ni pertenece siquiera a la familia de las lenguas indoeuropeas.",
                "Considerado la lengua viva más antigua de Europa occidental, de origen prerromano, el euskera es hoy lengua cooficial junto al castellano en toda la Comunidad Autónoma del País Vasco y en las zonas vascófonas de Navarra, contando con el impulso académico de Euskaltzaindia (la Real Academia de la Lengua Vasca)."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué comunidad autónoma es lengua cooficial el gallego junto con el castellano?",
                    "options": ["En Galicia.", "En Extremadura.", "En La Rioja."],
                    "correctIndex": 0,
                    "explanation": "El gallego es la lengua propia y cooficial junto con el castellano en la Comunidad Autónoma de Galicia."
                },
                {
                    "question": "¿En qué comunidades autónomas tiene estatus de lengua cooficial el euskera (o vasco)?",
                    "options": ["En el País Vasco y en las zonas vascófonas de la Comunidad Foral de Navarra.", "En Cataluña y en Aragón.", "En Asturias y en Cantabria."],
                    "correctIndex": 0,
                    "explanation": "El euskera es cooficial en el País Vasco y en las zonas vascófonas de Navarra."
                },
                {
                    "question": "¿Cuál de las lenguas oficiales de España es prerromana y NO procede del latín?",
                    "options": ["El euskera (vasco).", "El gallego.", "El catalán."],
                    "correctIndex": 0,
                    "explanation": "El euskera es la única lengua no romance (prerromana y no indoeuropea) de España."
                }
            ],
            "vocab": [
                {"lemma": "gallego", "pos": "noun", "translation": "Galician language", "ex_es": "El gallego es lengua cooficial junto con el castellano en toda Galicia.", "ex_en": "Galician is a co-official language alongside Castilian throughout Galicia."},
                {"lemma": "euskera", "pos": "noun", "translation": "Basque language (Euskera)", "ex_es": "El euskera es lengua cooficial en el País Vasco y en parte de Navarra.", "ex_en": "Euskera is a co-official language in the Basque Country and in part of Navarre."},
                {"lemma": "prerromano", "pos": "adjective", "translation": "pre-Roman", "ex_es": "El euskera es una lengua de origen prerromano que no procede del latín.", "ex_en": "Euskera is a language of pre-Roman origin that does not come from Latin."},
                {"lemma": "vascófono", "pos": "adjective", "translation": "Basque-speaking", "ex_es": "En la zona vascófona de Navarra el euskera comparte oficialidad con el castellano.", "ex_en": "In the Basque-speaking zone of Navarre Euskera shares official status with Castilian."},
                {"lemma": "latín", "pos": "noun", "translation": "Latin", "ex_es": "Todas las lenguas oficiales de España salvo el euskera evolucionaron a partir del latín.", "ex_en": "All official languages of Spain except Euskera evolved from Latin."},
                {"lemma": "Rosalía de Castro", "pos": "noun", "translation": "Rosalía de Castro (19th-century Galician poet)", "ex_es": "Rosalía de Castro es la gran figura literaria del renacimiento de la lengua gallega.", "ex_en": "Rosalía de Castro is the great literary figure of the revival of the Galician language."},
                {"lemma": "indoeuropeo", "pos": "adjective", "translation": "Indo-European", "ex_es": "El euskera es una lengua aislada que no pertenece al tronco indoeuropeo.", "ex_en": "Euskera is a language isolate that does not belong to the Indo-European family."},
                {"lemma": "convivencia", "pos": "noun", "translation": "coexistence", "ex_es": "La convivencia de lenguas enriquece la vida cultural de las comunidades autónomas.", "ex_en": "The coexistence of languages enriches the cultural life of the autonomous communities."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué comunidad autónoma es lengua cooficial el gallego?", "options": ["En Galicia", "En Cantabria", "En el País Vasco", "En Castilla y León"], "answer": "En Galicia", "explanation": "El gallego es la lengua propia y cooficial de Galicia."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál de las siguientes lenguas cooficiales de España NO procede del latín?", "options": ["El euskera (vasco)", "El gallego", "El catalán", "El valenciano"], "answer": "El euskera (vasco)", "explanation": "El euskera es una lengua prerromana y no indoeuropea; las demás son lenguas romances derivadas del latín."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ es lengua cooficial en el País Vasco y en la zona vascófona de Navarra.", "answer": "euskera", "english": "Basque (Euskera) is a co-official language in the Basque Country and in the Basque-speaking area of Navarre.", "explanation": "'El euskera' (o vasco)."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "A diferencia del castellano y del gallego, el euskera no procede del ___.", "answer": "latín", "english": "Unlike Castilian and Galician, Basque does not come from Latin.", "explanation": "Euskera does not derive from Latin ('latín')."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Galician:", "words": ["El", "gallego", "es", "lengua", "cooficial", "junto", "con", "el", "castellano", "en", "Galicia."], "answer": "El gallego es lengua cooficial junto con el castellano en Galicia.", "english": "Galician is a co-official language alongside Castilian in Galicia."},
                {"type": "dictation", "cat": "listening", "text": "El euskera se habla en el País Vasco y en el norte de Navarra.", "english": "Euskera is spoken in the Basque Country and in northern Navarre."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Cuántas comunidades autónomas españolas tienen reconocida en sus Estatutos una lengua cooficial junto al castellano?", "options": ["Seis comunidades autónomas (Cataluña, Comunidad Valenciana, Islas Baleares, Galicia, País Vasco y Navarra)", "Las diecisiete comunidades autónomas", "Únicamente dos comunidades", "Ninguna comunidad autónoma"], "answer": "Seis comunidades autónomas (Cataluña, Comunidad Valenciana, Islas Baleares, Galicia, País Vasco y Navarra)", "explanation": "Seis comunidades autónomas tienen lengua cooficial: Cataluña, Comunidad Valenciana, Islas Baleares, Galicia, País Vasco y Navarra."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En las cuatro provincias de ___ (A Coruña, Lugo, Ourense y Pontevedra) se habla el gallego.", "answer": "Galicia", "english": "In the four provinces of Galicia (A Coruña, Lugo, Ourense, and Pontevedra) Galician is spoken.", "explanation": "Galicia has four provinces."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the origin of Euskera:", "words": ["El", "euskera", "es", "la", "única", "lengua", "prerromana", "viva", "de", "España."], "answer": "El euskera es la única lengua prerromana viva de España.", "english": "Euskera is the only living pre-Roman language of Spain."}
            ]
        },
        {
            "num": "04",
            "story_slug": "rae",
            "title": "La Real Academia Española (RAE) y las Academias de la Lengua (ASALE)",
            "goal": "Understand the role of the Real Academia Española (founded in Madrid in 1713) and the Association of Academies of the Spanish Language (ASALE, 23 academies across the world) in maintaining the pan-Hispanic unity of the Spanish language.",
            "grammar_slug": "velar-por-que-no-se-quiebre",
            "grammar_title": "Finalidad normativa: 'velar por que + subjuntivo' y 'en colaboración con'",
            "grammar_summary": "Using 'velar por que los cambios no quiebren la unidad del idioma' and 'en colaboración con las academias hermanas'.",
            "grammar_text": "To express institutional stewardship over a goal, Spanish uses 'velar por que + subjuntivo' (to watch over / ensure that...). Founded in Madrid in **1713** under King Philip V, the **Real Academia Española (RAE)** works in collaboration with the 22 other Academies of the Spanish-speaking world within **ASALE** (Asociación de Academias de la Lengua Española) to ensure that the natural evolution of Spanish does not break its essential unity ('velar por que los cambios no quiebren la esencial unidad que mantiene en todo el ámbito hispánico').",
            "grammar_examples": [
                {"spanish": "La Real Academia Española fue fundada en Madrid en 1713 para velar por el buen uso del idioma.", "english": "The Royal Spanish Academy was founded in Madrid in 1713 to watch over the proper use of the language."},
                {"spanish": "La RAE elabora el Diccionario, la Ortografía y la Gramática en colaboración con las veintidós academias hispanoamericanas.", "english": "The RAE prepares the Dictionary, Orthography, and Grammar in collaboration with the twenty-two Hispanic American academies."},
                {"spanish": "Existen academias propias para las lenguas cooficiales, como el Institut d'Estudis Catalans, la Real Academia Galega y Euskaltzaindia.", "english": "There are specific academies for the co-official languages, such as the Institut d'Estudis Catalans, the Real Academia Galega, and Euskaltzaindia."}
            ],
            "grammar_tip": "Distinguish for the CCSE exam: **Real Academia Española (RAE)** = regulates the dictionary, grammar, and orthography of the Spanish language (alongside ASALE); **Instituto Cervantes** = public institution that promotes the teaching of Spanish and Hispanic culture abroad (and administers the DELE and CCSE exams!).",
            "story_title": "Veintitrés academias para quinientos millones de hablantes",
            "story_summary": "At the headquarters of the Real Academia Española in Madrid, lexicographers from Spain and Latin America collaborate on the pan-Hispanic Dictionary of the Spanish Language.",
            "story_location": "Madrid, Sede de la Real Academia Española",
            "story_paragraphs": [
                "En la calle Felipe IV de Madrid, muy cerca del Museo del Prado, se alza la sede de la Real Academia Española (RAE), institución cultural fundada en el año 1713 por iniciativa de Juan Manuel Fernández Pacheco, marqués de Villena, bajo el reinado de Felipe V.",
                "Aunque nació en el siglo XVIII con el célebre lema «Limpia, fija y da esplendor», hoy la misión principal de la RAE es velar por que los cambios que experimenta la lengua española al adaptarse a las necesidades de sus hablantes no quiebren la esencial unidad que mantiene en todo el mundo hispánico.",
                "Dado que cerca del noventa por ciento de los más de quinientos millones de hispanohablantes viven hoy en América, la RAE no fija las normas en solitario, sino de manera consensuada a través de la Asociación de Academias de la Lengua Española (ASALE), que agrupa a veintitrés academias de España, América, Filipinas y Guinea Ecuatorial.",
                "Fruto de esta política lingüística panhispánica son obras conjuntas como el *Diccionario de la lengua española* (DLE), la *Ortografía* y la *Nueva gramática de la lengua española*.",
                "Asimismo, en España existen instituciones académicas encargadas de velar por las lenguas cooficiales en sus respectivos territorios: el Institut d'Estudis Catalans y la Acadèmia Valenciana de la Llengua, la Real Academia Galega y Euskaltzaindia (Real Academia de la Lengua Vasca)."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la institución fundada en Madrid en 1713 que, junto con las academias de los demás países hispanohablantes, elabora el diccionario, la ortografía y la gramática de la lengua española?",
                    "options": ["La Real Academia Española (RAE).", "El Tribunal Supremo.", "El Banco de España."],
                    "correctIndex": 0,
                    "explanation": "La Real Academia Española (RAE), junto con la Asociación de Academias de la Lengua Española (ASALE), vela por la unidad y normativa del idioma español."
                },
                {
                    "question": "¿Aproximadamente cuántas personas hablan español hoy en el mundo?",
                    "options": ["Más de 500 millones de personas (cerca de 600 millones sumando hablantes nativos y de competencia limitada).", "Unos 48 millones únicamente.", "Menos de 100 millones."],
                    "correctIndex": 0,
                    "explanation": "El español cuenta con cerca de 500 millones de hablantes nativos y casi 600 millones de hablantes potenciales en todo el mundo."
                },
                {
                    "question": "¿Qué instituciones académicas velan por las normas de las lenguas cooficiales como el catalán, el gallego y el euskera?",
                    "options": ["El Institut d'Estudis Catalans (y la Acadèmia Valenciana de la Llengua), la Real Academia Galega y Euskaltzaindia.", "Las cámaras de comercio provinciales.", "Las federaciones deportivas."],
                    "correctIndex": 0,
                    "explanation": "Cada lengua cooficial cuenta con su propia institución académica normativa reconocida oficialmente."
                }
            ],
            "vocab": [
                {"lemma": "Real Academia Española", "pos": "noun", "translation": "Royal Spanish Academy (RAE)", "ex_es": "La Real Academia Española fue fundada en 1713 y tiene su sede en Madrid.", "ex_en": "The Royal Spanish Academy was founded in 1713 and is headquartered in Madrid."},
                {"lemma": "diccionario", "pos": "noun", "translation": "dictionary", "ex_es": "La RAE y las academias americanas publican el Diccionario de la lengua española.", "ex_en": "The RAE and the American academies publish the Dictionary of the Spanish Language."},
                {"lemma": "ortografía", "pos": "noun", "translation": "orthography / spelling rules", "ex_es": "La ortografía del español es compartida por los veintitrés países con academia de la lengua.", "ex_en": "The orthography of Spanish is shared by the twenty-three countries with a language academy."},
                {"lemma": "hispanohablante", "pos": "noun", "translation": "Spanish speaker", "ex_es": "En el mundo viven hoy más de quinientos millones de hispanohablantes.", "ex_en": "More than five hundred million Spanish speakers live in the world today."},
                {"lemma": "panhispánico", "pos": "adjective", "translation": "pan-Hispanic (shared across all Spanish-speaking countries)", "ex_es": "Las normas actuales del idioma tienen carácter panhispánico y consensuado.", "ex_en": "Current rules of the language have a pan-Hispanic and consensual character."},
                {"lemma": "Euskaltzaindia", "pos": "noun", "translation": "Royal Academy of the Basque Language", "ex_es": "Euskaltzaindia es la academia oficial encargada de la lengua vasca o euskera.", "ex_en": "Euskaltzaindia is the official academy in charge of the Basque language or Euskera."},
                {"lemma": "Real Academia Galega", "pos": "noun", "translation": "Royal Galician Academy", "ex_es": "La Real Academia Galega fija las normas ortográficas y léxicas del gallego.", "ex_en": "The Royal Galician Academy sets the orthographic and lexical rules of Galician."},
                {"lemma": "unidad del idioma", "pos": "noun", "translation": "unity of the language", "ex_es": "Las academias trabajan juntas para preservar la unidad del idioma español.", "ex_en": "The academies work together to preserve the unity of the Spanish language."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué institución española elabora el Diccionario, la Ortografía y la Gramática de la lengua española junto con las demás academias hispanohablantes?", "options": ["La Real Academia Española (RAE)", "La Biblioteca Nacional", "El Museo del Prado", "El Consejo de Estado"], "answer": "La Real Academia Española (RAE)", "explanation": "La Real Academia Española (RAE), fundada en 1713, elabora la normativa lingüística junto con la ASALE."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Con cuántas academias hermanas de América, Filipinas y Guinea Ecuatorial colabora la RAE en la Asociación de Academias de la Lengua Española (ASALE)?", "options": ["Con 22 academias (23 en total junto con la RAE)", "Con ninguna, actúa sola", "Con 5 academias europeas", "Con 100 academias municipales"], "answer": "Con 22 academias (23 en total junto con la RAE)", "explanation": "La ASALE integra a las 23 Academias de la Lengua Española del mundo."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Real ___ Española (RAE) tiene su sede en Madrid y fue fundada en 1713.", "answer": "Academia", "english": "The Royal Spanish Academy (RAE) has its headquarters in Madrid and was founded in 1713.", "explanation": "'Real Academia Española'."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En el mundo hay hoy más de quinientos millones de ___ que se comunican en español.", "answer": "hispanohablantes", "english": "In the world today there are more than five hundred million Spanish speakers who communicate in Spanish.", "explanation": "'Hispanohablantes' means Spanish speakers."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the RAE:", "words": ["La", "Real", "Academia", "Española", "vela", "por", "la", "unidad", "del", "idioma."], "answer": "La Real Academia Española vela por la unidad del idioma.", "english": "The Royal Spanish Academy watches over the unity of the language."},
                {"type": "dictation", "cat": "listening", "text": "La Real Academia Española publica el diccionario y la ortografía del español.", "english": "The Royal Spanish Academy publishes the dictionary and the orthography of Spanish."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Cómo se llama la academia oficial encargada del estudio y normativa de la lengua vasca (euskera)?", "options": ["Euskaltzaindia", "Real Academia Galega", "Institut d'Estudis Catalans", "Instituto Cervantes"], "answer": "Euskaltzaindia", "explanation": "Euskaltzaindia es la Real Academia de la Lengua Vasca."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La RAE publica el ___ de la lengua española en colaboración con las academias americanas.", "answer": "Diccionario", "english": "The RAE publishes the Dictionary of the Spanish Language in collaboration with the American academies.", "explanation": "'Diccionario de la lengua española'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about Spanish speakers worldwide:", "words": ["El", "español", "es", "hablado", "por", "más", "de", "quinientos", "millones", "de", "personas."], "answer": "El español es hablado por más de quinientos millones de personas.", "english": "Spanish is spoken by more than five hundred million people."}
            ]
        },
        {
            "num": "05",
            "story_slug": "modalidades",
            "title": "Otras modalidades lingüísticas y patrimonio inmaterial: asturiano, aragonés y el silbo gomero",
            "goal": "Appreciate Spain's broader linguistic and communicative heritage under Article 3.3: protected regional varieties such as Asturian (bable) and Aragonese (fabla), Spanish Sign Language (LSE) and Catalan Sign Language (LSC), and the Silbo Gomero (UNESCO Intangible Cultural Heritage in La Gomera, Canary Islands).",
            "grammar_slug": "gozar-de-proteccion-y-reconocimiento",
            "grammar_title": "Reconocimiento y patrimonio: 'gozar de protección' y 'ser declarado Patrimonio de la Humanidad'",
            "grammar_summary": "Using 'gozar de protección en su Estatuto' and 'ser declarado Patrimonio Cultural Inmaterial de la Humanidad'.",
            "grammar_text": "Beyond co-official languages, several Statutes of Autonomy and national laws grant legal protection and promotion ('gozan de protección y promoción') to specific linguistic modalities ('modalidades lingüísticas') and communicative systems. These include **el bable o asturiano** in the Principality of Asturias, **el aragonés** in Aragon, **el leonés** in Castile and León, the officially recognized **Lengua de Signos Española (LSE)** and **Lengua de Signos Catalana (LSC)** (Law 27/2007), and **el silbo gomero**, an ancient whistled language on the Canary Island of La Gomera declared Intangible Cultural Heritage of Humanity by UNESCO.",
            "grammar_examples": [
                {"spanish": "El bable o asturiano goza de protección y difusión en el Principado de Asturias.", "english": "Bable or Asturian enjoys protection and promotion in the Principality of Asturias."},
                {"spanish": "El silbo gomero fue declarado Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO.", "english": "The Silbo Gomero was declared Intangible Cultural Heritage of Humanity by UNESCO."},
                {"spanish": "La ley española reconoce oficialmente la Lengua de Signos Española y la Lengua de Signos Catalana.", "english": "Spanish law officially recognizes Spanish Sign Language and Catalan Sign Language."}
            ],
            "grammar_tip": "Remember **el silbo gomero** (from the island of **La Gomera**, in the Canary Islands): a whistled language capable of transmitting messages in Spanish across deep ravines ('barrancos'), recognized by UNESCO.",
            "story_title": "De los valles asturianos a los barrancos de La Gomera",
            "story_summary": "A cultural documentary explores Spain's protected linguistic modalities—Asturian bable, Aragonese fabla, Spanish Sign Language, and the remarkable whistled language of La Gomera.",
            "story_location": "Asturias, Aragón y La Gomera (Canarias)",
            "story_paragraphs": [
                "El artículo 3.3 de la Constitución Española protege no solo las lenguas cooficiales, sino toda la riqueza de las distintas modalidades lingüísticas de España como un patrimonio cultural común.",
                "En el Principado de Asturias, el Estatuto de Autonomía protege y promueve el uso del bable o asturiano (cuya institución consultiva es la Academia de la Llingua Asturiana), mientras que en Aragón se impulsa la conservación del aragonés (o fabla) en los valles pirenaicos.",
                "Asimismo, la riqueza expresiva del castellano se manifiesta en sus grandes variedades dialectales históricas, como el español meridional de Andalucía, Extremadura, Murcia y Canarias, estrechamente vinculado con el español de América.",
                "En la isla canaria de La Gomera se conserva además un tesoro único en el mundo: el silbo gomero, un lenguaje silbado que reproduce con silbidos los sonidos del idioma español para comunicarse a varios kilómetros de distancia a través de los profundos barrancos de la isla. En 2009 fue inscrito por la UNESCO como Patrimonio Cultural Inmaterial de la Humanidad y se enseña en todas las escuelas gomeras.",
                "Por último, España garantiza la plena inclusión comunicativa de las personas sordas o con discapacidad auditiva mediante la Ley 27/2007, que reconoce oficialmente la Lengua de Signos Española (LSE) y la Lengua de Signos Catalana (LSC)."
            ],
            "comp_questions": [
                {
                    "question": "¿Cómo se llama la modalidad lingüística propia del Principado de Asturias, protegida y promovida por su Estatuto de Autonomía?",
                    "options": ["El bable o asturiano.", "El aranés.", "El valenciano."],
                    "correctIndex": 0,
                    "explanation": "El Estatuto de Autonomía del Principado de Asturias protege el bable o asturiano y promueve su difusión y enseñanza voluntaria."
                },
                {
                    "question": "¿En qué isla de las Canarias se practica y enseña el «silbo gomero», lenguaje silbado declarado Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO?",
                    "options": ["En la isla de La Gomera.", "En la isla de Menorca.", "En la isla de Ibiza."],
                    "correctIndex": 0,
                    "explanation": "El silbo gomero es propio de la isla canaria de La Gomera."
                },
                {
                    "question": "¿Qué lenguas reconoce oficialmente la Ley 27/2007 para garantizar los derechos comunicativos de las personas sordas en España?",
                    "options": ["La Lengua de Signos Española (LSE) y la Lengua de Signos Catalana (LSC).", "Únicamente el alfabeto morse.", "El esperanto."],
                    "correctIndex": 0,
                    "explanation": "La Ley 27/2007 reconoce y regula la Lengua de Signos Española (LSE) y la Lengua de Signos Catalana (LSC)."
                }
            ],
            "vocab": [
                {"lemma": "bable", "pos": "noun", "translation": "Bable / Asturian language variety", "ex_es": "El bable o asturiano goza de protección en el Estatuto de Autonomía de Asturias.", "ex_en": "Bable or Asturian enjoys protection in the Statute of Autonomy of Asturias."},
                {"lemma": "silbo gomero", "pos": "noun", "translation": "Silbo Gomero (whistled language of La Gomera)", "ex_es": "El silbo gomero permite comunicarse a través de los barrancos de la isla de La Gomera.", "ex_en": "The Silbo Gomero allows communication across the ravines of the island of La Gomera."},
                {"lemma": "Lengua de Signos Española", "pos": "noun", "translation": "Spanish Sign Language (LSE)", "ex_es": "La Lengua de Signos Española está reconocida por ley para las personas sordas.", "ex_en": "Spanish Sign Language is recognized by law for deaf people."},
                {"lemma": "Patrimonio Inmaterial", "pos": "noun", "translation": "Intangible Cultural Heritage", "ex_es": "La UNESCO declaró el silbo gomero Patrimonio Cultural Inmaterial de la Humanidad.", "ex_en": "UNESCO declared the Silbo Gomero Intangible Cultural Heritage of Humanity."},
                {"lemma": "aragonés", "pos": "noun", "translation": "Aragonese language variety (fabla)", "ex_es": "El aragonés se conserva en varios valles del Pirineo de Huesca.", "ex_en": "Aragonese is preserved in several valleys of the Pyrenees of Huesca."},
                {"lemma": "barranco", "pos": "noun", "translation": "ravine / gorge", "ex_es": "Los pastores salvaban la distancia de cada barranco comunicándose mediante el silbo.", "ex_en": "Shepherds bridged the distance of each ravine by communicating through whistling."},
                {"lemma": "inclusión", "pos": "noun", "translation": "inclusion", "ex_es": "Los intérpretes de lengua de signos favorecen la plena inclusión en los actos públicos.", "ex_en": "Sign language interpreters foster full inclusion at public events."},
                {"lemma": "difusión", "pos": "noun", "translation": "dissemination / promotion", "ex_es": "Los poderes públicos apoyan la difusión de las distintas modalidades lingüísticas.", "ex_en": "Public authorities support the promotion of the different linguistic modalities."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué comunidad autónoma se habla y protege la modalidad lingüística conocida como bable o asturiano?", "options": ["En el Principado de Asturias", "En la Región de Murcia", "En las Islas Baleares", "En La Rioja"], "answer": "En el Principado de Asturias", "explanation": "El bable o asturiano es la modalidad lingüística propia del Principado de Asturias."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué es el «silbo gomero», declarado Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO?", "options": ["Un lenguaje silbado tradicional de la isla canaria de La Gomera", "Un instrumento musical de viento de Galicia", "Un baile regional de Aragón", "Un plato típico de Menorca"], "answer": "Un lenguaje silbado tradicional de la isla canaria de La Gomera", "explanation": "El silbo gomero es el lenguaje silbado de la isla de La Gomera (Canarias)."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En el Principado de Asturias se protege el ___ o asturiano.", "answer": "bable", "english": "In the Principality of Asturias Bable or Asturian is protected.", "explanation": "'El bable o asturiano'."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ gomero es un lenguaje silbado propio de la isla de La Gomera en Canarias.", "answer": "silbo", "english": "The Silbo Gomero is a whistled language native to the island of La Gomera in the Canary Islands.", "explanation": "'El silbo gomero'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Silbo Gomero:", "words": ["El", "silbo", "gomero", "es", "Patrimonio", "Cultural", "Inmaterial", "de", "la", "Humanidad."], "answer": "El silbo gomero es Patrimonio Cultural Inmaterial de la Humanidad.", "english": "The Silbo Gomero is Intangible Cultural Heritage of Humanity."},
                {"type": "dictation", "cat": "listening", "text": "La ley española reconoce oficialmente la Lengua de Signos Española.", "english": "Spanish law officially recognizes Spanish Sign Language."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿En qué archipiélago español se encuentra la isla de La Gomera, famosa por su lenguaje silbado?", "options": ["En las Islas Canarias", "En las Islas Baleares", "En las Islas Cíes", "En las Islas Columbretes"], "answer": "En las Islas Canarias", "explanation": "La Gomera es una de las islas del archipiélago de Canarias (provincia de Santa Cruz de Tenerife)."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La Ley 27/2007 reconoce oficialmente la Lengua de ___ Española (LSE).", "answer": "Signos", "english": "Law 27/2007 officially recognizes Spanish Sign Language (LSE).", "explanation": "'Lengua de Signos Española'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about Asturian:", "words": ["El", "bable", "o", "asturiano", "goza", "de", "protección", "en", "el", "Principado", "de", "Asturias."], "answer": "El bable o asturiano goza de protección en el Principado de Asturias.", "english": "Bable or Asturian enjoys protection in the Principality of Asturias."}
            ]
        }
    ],
    "consolidation_exercises": [
        {"type": "multiple-choice", "cat": "grammar", "prompt": "Según el artículo 3.1 de la Constitución, ¿cuál es la lengua española oficial del Estado?", "options": ["El castellano", "El catalán", "El euskera", "El gallego"], "answer": "El castellano", "explanation": "Artículo 3.1 de la Constitución."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué comunidades autónomas es cooficial el catalán?", "options": ["En Cataluña y en las Islas Baleares", "En Galicia y Asturias", "En Valencia y Murcia", "En Navarra y Aragón"], "answer": "En Cataluña y en las Islas Baleares", "explanation": "El catalán es cooficial en Cataluña y en las Islas Baleares; en la Comunidad Valenciana la lengua cooficial se denomina valenciano."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es la lengua cooficial de Galicia?", "options": ["El gallego", "El bable", "El aranés", "El euskera"], "answer": "El gallego", "explanation": "El gallego es cooficial junto al castellano en Galicia."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué comunidades autónomas tiene carácter cooficial el euskera (o vasco)?", "options": ["En el País Vasco y en las zonas vascófonas de Navarra", "En Cataluña y Aragón", "En Cantabria y La Rioja", "En Asturias y León"], "answer": "En el País Vasco y en las zonas vascófonas de Navarra", "explanation": "El euskera es cooficial en el País Vasco y en la zona vascófona de Navarra."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál de las lenguas oficiales de España es de origen prerromano y NO procede del latín?", "options": ["El euskera", "El gallego", "El catalán", "El aranés"], "answer": "El euskera", "explanation": "El euskera es la única lengua no indoeuropea y no derivada del latín en España."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué institución fundada en 1713 fija el Diccionario, la Ortografía y la Gramática de la lengua española junto con las academias hispanoamericanas?", "options": ["La Real Academia Española (RAE)", "El Tribunal Constitucional", "La Biblioteca Nacional", "El Consejo Superior de Deportes"], "answer": "La Real Academia Española (RAE)", "explanation": "La RAE trabaja junto con las 22 academias hermanas en la ASALE."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Todos los españoles tienen el ___ de conocer el castellano y el derecho a usarlo.", "answer": "deber", "english": "All Spaniards have the duty to know Castilian and the right to use it.", "explanation": "Artículo 3.1: 'el deber de conocerla y el derecho a usarla'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "En la Comunidad Valenciana la lengua propia y cooficial es el ___.", "answer": "valenciano", "english": "In the Valencian Community the own and co-official language is Valencian.", "explanation": "'El valenciano'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "En el Valle de Arán (Cataluña) es oficial el ___, una variedad de la lengua occitana.", "answer": "aranés", "english": "In the Val d'Aran (Catalonia) Aranese, a variety of the Occitan language, is official.", "explanation": "'El aranés'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "En el Principado de Asturias se protege la modalidad lingüística del ___ o asturiano.", "answer": "bable", "english": "In the Principality of Asturias the linguistic modality of Bable or Asturian is protected.", "explanation": "'El bable o asturiano'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El ___ gomero es un lenguaje silbado de la isla de La Gomera (Canarias).", "answer": "silbo", "english": "The Silbo Gomero is a whistled language of the island of La Gomera (Canary Islands).", "explanation": "'El silbo gomero'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "La riqueza de las modalidades lingüísticas de España es un ___ cultural protegido.", "answer": "patrimonio", "english": "The richness of the linguistic modalities of Spain is a protected cultural heritage.", "explanation": "'Patrimonio cultural' (Artículo 3.3)."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order Article 3.1 about the duty and right of citizens:", "words": ["Todos", "los", "españoles", "tienen", "el", "deber", "de", "conocerla", "y", "el", "derecho", "a", "usarla."], "answer": "Todos los españoles tienen el deber de conocerla y el derecho a usarla.", "english": "All Spaniards have the duty to know it and the right to use it."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Euskera:", "words": ["El", "euskera", "es", "una", "lengua", "prerromana", "que", "no", "procede", "del", "latín."], "answer": "El euskera es una lengua prerromana que no procede del latín.", "english": "Euskera is a pre-Roman language that does not come from Latin."},
        {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Order the sentence about the RAE:", "words": ["La", "Real", "Academia", "Española", "elabora", "el", "diccionario", "y", "la", "gramática", "del", "español."], "answer": "La Real Academia Española elabora el diccionario y la gramática del español.", "english": "The Royal Spanish Academy prepares the dictionary and the grammar of Spanish."},
        {"type": "dictation", "cat": "listening", "text": "El castellano es la lengua española oficial del Estado.", "english": "Castilian is the official Spanish language of the State."},
        {"type": "dictation", "cat": "listening", "text": "El gallego es cooficial en Galicia y el valenciano en la Comunidad Valenciana.", "english": "Galician is co-official in Galicia and Valencian in the Valencian Community."},
        {"type": "dictation", "cat": "listening", "text": "La riqueza de las modalidades lingüísticas de España es un patrimonio cultural.", "english": "The richness of the linguistic modalities of Spain is a cultural heritage."}
    ]
}

UNIT_12 = {
    "slug": "cervantes",
    "legacy_prefix": "b1-ccse-instituto-cervantes",
    "unit_title": "Difusión Cultural: El Instituto Cervantes",
    "order": 12,
    "unit_summary": "Complete CCSE guide to Cultural Promotion and the Instituto Cervantes: its creation in 1991 under the Ministry of Foreign Affairs, its two headquarters (Madrid and Alcalá de Henares), the DELE and SIELE Spanish language diplomas, the CCSE citizenship exam itself (25 questions, 60% / 15 correct to pass, 45 minutes), and colleague cultural institutions like the Institut Ramon Llull and Instituto Camões.",
    "unit_paragraphs": [],
    "unit_questions": [],
    "lessons": [
        {
            "num": "01",
            "story_slug": "misioncervantes",
            "title": "El Instituto Cervantes: creación (1991), sedes y misión internacional",
            "goal": "Know what the Instituto Cervantes is, when it was created (1991), which ministry it depends on (Ministry of Foreign Affairs, European Union and Cooperation), and its two headquarters (Madrid and Alcalá de Henares).",
            "grammar_slug": "creado-para-promover",
            "grammar_title": "Finalidad institucional: 'creado en + año para + infinitivo' y 'adscrito a'",
            "grammar_summary": "Using 'institución pública creada en 1991 para promover universalmente la enseñanza del español' and 'adscrito al Ministerio de Asuntos Exteriores'.",
            "grammar_text": "The **Instituto Cervantes** is a public institution created by Spain in **1991** ('creada por la Ley 7/1991') and attached to the **Ministry of Foreign Affairs, European Union and Cooperation** ('adscrita al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación'). Its mission is to universally promote the teaching, study, and use of the Spanish language and to contribute to the dissemination of Hispanic cultures abroad ('contribuir a la difusión de las culturas hispánicas en el exterior'). It has two official headquarters in Spain: its central executive headquarters in the **Edificio de las Cariátides on Calle de Alcalá in Madrid**, and its registered institutional seat at the **Colegio del Rey in Alcalá de Henares** (birthplace of Miguel de Cervantes).",
            "grammar_examples": [
                {"spanish": "El Instituto Cervantes fue creado en 1991 para promover la enseñanza y el uso del español en el mundo.", "english": "The Instituto Cervantes was created in 1991 to promote the teaching and use of Spanish in the world."},
                {"spanish": "Está adscrito al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación.", "english": "It is attached to the Ministry of Foreign Affairs, European Union and Cooperation."},
                {"spanish": "Cuenta con dos sedes en España: la sede central de Madrid y la sede institucional de Alcalá de Henares.", "english": "It has two headquarters in Spain: the central headquarters in Madrid and the institutional seat in Alcalá de Henares."}
            ],
            "grammar_tip": "High-frequency CCSE exam question: What is the mission of the Instituto Cervantes? **Promover universalmente la enseñanza, el estudio y el uso del español y difundir la cultura en español en el exterior**.",
            "story_title": "El Edificio de las Cariátides y la Caja de las Letras",
            "story_summary": "A visitor enters the historic Edificio de las Cariátides on Madrid's Calle de Alcalá—central headquarters of the Instituto Cervantes—and visits the famous Caja de las Letras vault where Hispanic writers leave their legacies.",
            "story_location": "Madrid y Alcalá de Henares",
            "story_paragraphs": [
                "En la confluencia de la calle de Alcalá con el paseo del Prado, en pleno centro de Madrid, se levanta el majestuoso Edificio de las Cariátides, sede central del Instituto Cervantes.",
                "Creado por ley en el año 1991 y adscrito al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación, el Instituto Cervantes es la institución pública encargada de promover universalmente la enseñanza, el estudio y el uso de la lengua española y de contribuir a la difusión de las culturas hispánicas en el exterior.",
                "La institución cuenta con dos sedes oficiales en España: la sede operativa de la calle de Alcalá en Madrid y la sede institucional del Colegio del Rey en Alcalá de Henares, ciudad natal de Miguel de Cervantes (1547-1616), autor de *Don Quijote de la Mancha*.",
                "En el sótano de la sede madrileña —que antiguamente fue la cámara acorazada de un banco— se encuentra hoy la célebre «Caja de las Letras», donde premios Cervantes, premios Nobel y grandes creadores de España e Hispanoamérica depositan legados simbólicos en cajas de seguridad para las generaciones futuras.",
                "Presente hoy en más de noventa ciudades de los cinco continentes, cada centro del Instituto Cervantes cuenta con aulas de enseñanza, programación cultural y una biblioteca que lleva el nombre de un gran escritor o escritora en lengua española."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la misión principal del Instituto Cervantes, creado en España en 1991?",
                    "options": ["Promover universalmente la enseñanza, el estudio y el uso del español y difundir las culturas hispánicas en el exterior.", "Recaudar los impuestos aduaneros en los puertos españoles.", "Redactar las leyes orgánicas en las Cortes Generales."],
                    "correctIndex": 0,
                    "explanation": "El Instituto Cervantes es la institución pública creada en 1991 para promover la enseñanza del español y difundir la cultura hispánica en el mundo."
                },
                {
                    "question": "¿De qué ministerio depende orgánicamente el Instituto Cervantes?",
                    "options": ["Del Ministerio de Asuntos Exteriores, Unión Europea y Cooperación.", "Del Ministerio de Sanidad.", "Del Ministerio de Transportes."],
                    "correctIndex": 0,
                    "explanation": "El Instituto Cervantes es un organismo público adscrito al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación."
                },
                {
                    "question": "¿En qué dos municipios de la Comunidad de Madrid se encuentran las sedes oficiales del Instituto Cervantes en España?",
                    "options": ["En Madrid (calle de Alcalá) y en Alcalá de Henares (Colegio del Rey).", "En Aranjuez y en El Escorial.", "En Toledo y en Segovia."],
                    "correctIndex": 0,
                    "explanation": "El Instituto Cervantes tiene su sede central en Madrid y su sede institucional en Alcalá de Henares, ciudad natal de Cervantes."
                }
            ],
            "vocab": [
                {"lemma": "Instituto Cervantes", "pos": "noun", "translation": "Instituto Cervantes (Spanish public institution for language and cultural promotion)", "ex_es": "El Instituto Cervantes promueve la enseñanza del español y la cultura hispánica en los cinco continentes.", "ex_en": "The Instituto Cervantes promotes the teaching of Spanish and Hispanic culture across all five continents."},
                {"lemma": "difusión cultural", "pos": "noun", "translation": "cultural promotion / dissemination", "ex_es": "Los centros del Instituto Cervantes realizan una intensa labor de difusión cultural en el exterior.", "ex_en": "Instituto Cervantes centers carry out intensive cultural promotion work abroad."},
                {"lemma": "Ministerio de Asuntos Exteriores", "pos": "noun", "translation": "Ministry of Foreign Affairs", "ex_es": "El Instituto Cervantes está adscrito al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación.", "ex_en": "The Instituto Cervantes is attached to the Ministry of Foreign Affairs, European Union and Cooperation."},
                {"lemma": "Caja de las Letras", "pos": "noun", "translation": "Vault of Letters (at the Instituto Cervantes headquarters in Madrid)", "ex_es": "En la Caja de las Letras los grandes escritores hispánicos guardan legados literarios.", "ex_en": "In the Vault of Letters great Hispanic writers store literary legacies."},
                {"lemma": "enseñanza del español", "pos": "noun", "translation": "teaching of Spanish", "ex_es": "Miles de alumnos asisten a cursos de enseñanza del español en la red del Instituto Cervantes.", "ex_en": "Thousands of students attend Spanish teaching courses in the Instituto Cervantes network."},
                {"lemma": "cultura hispánica", "pos": "noun", "translation": "Hispanic culture", "ex_es": "El Instituto Cervantes difunde la cultura hispánica de España y de toda América Latina.", "ex_en": "The Instituto Cervantes disseminates the Hispanic culture of Spain and all of Latin America."},
                {"lemma": "sede central", "pos": "noun", "translation": "central headquarters", "ex_es": "La sede central del Instituto Cervantes ocupa el Edificio de las Cariátides en Madrid.", "ex_en": "The central headquarters of the Instituto Cervantes occupies the Caryatids Building in Madrid."},
                {"lemma": "legado", "pos": "noun", "translation": "legacy", "ex_es": "Cada autor deposita un legado personal en una caja de seguridad con fecha de apertura.", "ex_en": "Each author deposits a personal legacy in a safe deposit box with an opening date."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué institución pública española creada en 1991 promueve la enseñanza del español y la difusión de la cultura hispánica en el extranjero?", "options": ["El Instituto Cervantes", "El Instituto Nacional de Estadística", "El Tribunal de Cuentas", "El Consejo General del Poder Judicial"], "answer": "El Instituto Cervantes", "explanation": "El Instituto Cervantes promueve universalmente la enseñanza del español y difunde las culturas hispánicas en el exterior."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿A qué ministerio está adscrito el Instituto Cervantes?", "options": ["Al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación", "Al Ministerio de Defensa", "Al Ministerio de Agricultura", "Al Ministerio de Sanidad"], "answer": "Al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación", "explanation": "El Instituto Cervantes depende del Ministerio de Asuntos Exteriores, Unión Europea y Cooperación."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Instituto ___ promueve el estudio del español en más de noventa ciudades del mundo.", "answer": "Cervantes", "english": "The Instituto Cervantes promotes the study of Spanish in more than ninety cities around the world.", "explanation": "'El Instituto Cervantes'."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Su misión es promover la enseñanza del español y la ___ de las culturas hispánicas en el exterior.", "answer": "difusión", "english": "Its mission is to promote the teaching of Spanish and the dissemination of Hispanic cultures abroad.", "explanation": "'Difusión de las culturas hispánicas'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the mission of the Instituto Cervantes:", "words": ["El", "Instituto", "Cervantes", "promueve", "la", "enseñanza", "del", "español", "en", "el", "mundo."], "answer": "El Instituto Cervantes promueve la enseñanza del español en el mundo.", "english": "The Instituto Cervantes promotes the teaching of Spanish in the world."},
                {"type": "dictation", "cat": "listening", "text": "El Instituto Cervantes difunde la lengua española y la cultura hispánica.", "english": "The Instituto Cervantes disseminates the Spanish language and Hispanic culture."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Dónde se encuentran las dos sedes oficiales del Instituto Cervantes en España?", "options": ["En Madrid y en Alcalá de Henares", "En Barcelona y en Girona", "En Sevilla y en Huelva", "En Bilbao y en Vitoria"], "answer": "En Madrid y en Alcalá de Henares", "explanation": "Tiene su sede central en Madrid (calle de Alcalá) y su sede institucional en Alcalá de Henares."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "En el sótano de la sede de Madrid se encuentra la famosa «___ de las Letras».", "answer": "Caja", "english": "In the basement of the Madrid headquarters is the famous 'Vault of Letters'.", "explanation": "'La Caja de las Letras'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the Ministry of Foreign Affairs:", "words": ["El", "Instituto", "Cervantes", "depende", "del", "Ministerio", "de", "Asuntos", "Exteriores."], "answer": "El Instituto Cervantes depende del Ministerio de Asuntos Exteriores.", "english": "The Instituto Cervantes depends on the Ministry of Foreign Affairs."}
            ]
        },
        {
            "num": "02",
            "story_slug": "delesiele",
            "title": "Los diplomas oficiales de español: el DELE (nivel mínimo A2 para nacionalidad) y el SIELE",
            "goal": "Understand the official Spanish language certifications managed by the Instituto Cervantes: the DELE diplomas (levels A1 to C2, indefinite validity, and minimum DELE A2 required for Spanish nationality by residence for non-Hispanic applicants) and the digital SIELE service.",
            "grammar_slug": "acreditar-un-nivel-minimo-de",
            "grammar_title": "Requisitos de acreditación oficial: 'acreditar un nivel mínimo de' y 'tener vigencia indefinida'",
            "grammar_summary": "Using 'acreditar el diploma DELE de nivel A2 o superior' and 'estar exento de' for citizenship language requirements.",
            "grammar_text": "To apply for Spanish nationality by residence ('solicitar la nacionalidad española por residencia'), applicants must prove sufficient integration into Spanish society. Alongside passing the CCSE test, applicants whose native language is not Spanish must accredit a minimum **A2 level** in the **DELE** exam ('acreditar el Diploma de Español como Lengua Extranjera DELE de nivel A2 o superior'), issued by the Instituto Cervantes on behalf of the Ministry of Education. Nationals of Ibero-American countries where Spanish is an official language are exempt from the DELE requirement ('están exentos del examen DELE'), though they DO take the CCSE test.",
            "grammar_examples": [
                {"spanish": "Para solicitar la nacionalidad por residencia se exige acreditar el diploma DELE de nivel A2 o superior.", "english": "To apply for nationality by residence, accrediting the DELE diploma at level A2 or higher is required."},
                {"spanish": "Los diplomas DELE son títulos oficiales con vigencia indefinida expedidos por el Instituto Cervantes.", "english": "DELE diplomas are official certificates with indefinite validity issued by the Instituto Cervantes."},
                {"spanish": "Los ciudadanos nacionales de países hispanohablantes están exentos de realizar el examen DELE.", "english": "Citizens who are nationals of Spanish-speaking countries are exempt from taking the DELE exam."}
            ],
            "grammar_tip": "Crucial CCSE rule: What is the minimum DELE CEFR level required for Spanish nationality by residence (for applicants from non-Spanish-speaking countries)? **DELE A2 o superior** (A2, B1, B2, C1, or C2). And nationals of Spanish-speaking countries only take the **CCSE**, not the DELE!",
            "story_title": "Del nivel A1 al C2: el pasaporte lingüístico del español",
            "story_summary": "An academic coordinator at an accredited Instituto Cervantes examination center explains the six CEFR levels of the DELE diploma, its indefinite validity, the A2 requirement for nationality, and the SIELE exam.",
            "story_location": "Madrid, Centro de Examen Acreditado",
            "story_paragraphs": [
                "El Instituto Cervantes administra las dos grandes certificaciones internacionales de dominio del idioma español: los Diplomas de Español como Lengua Extranjera (DELE) y el Servicio Internacional de Evaluación de la Lengua Española (SIELE).",
                "Los diplomas DELE son títulos oficiales que otorga el Instituto Cervantes en nombre del Ministerio de Educación, Formación Profesional y Deportes de España. Tienen reconocimiento internacional y una vigencia indefinida: una vez obtenidos, nunca caducan.",
                "Siguiendo el Marco Común Europeo de Referencia para las Lenguas (MCER), los exámenes DELE evalúan las cuatro destrezas lingüísticas —comprensión de lectura, comprensión auditiva, expresión e interacción escritas y expresión e interacción orales— en seis niveles: A1, A2, B1, B2, C1 y C2.",
                "Para el trámite de adquisición de la nacionalidad española por residencia, la legislación exige a los solicitantes cuya lengua materna no sea el español acreditar como mínimo el diploma DELE de nivel A2 o cualquier nivel superior (B1, B2, C1 o C2), salvo que cuenten con dispensa o titulación oficial española equivalente.",
                "En cambio, los solicitantes nacionales de países o territorios hispanohablantes en los que el español es lengua oficial están exentos del examen DELE, por lo que únicamente deben superar la prueba de conocimientos constitucionales y socioculturales (CCSE)."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es el nivel mínimo del diploma oficial DELE exigido para solicitar la nacionalidad española por residencia a los candidatos de países no hispanohablantes?",
                    "options": ["El nivel A2 o superior (B1, B2, C1 o C2).", "El nivel C2 exclusivamente.", "Ningún nivel de idioma."],
                    "correctIndex": 0,
                    "explanation": "La normativa de nacionalidad española por residencia exige acreditar como mínimo el diploma DELE de nivel A2 o superior."
                },
                {
                    "question": "¿Qué vigencia temporal tienen los Diplomas de Español como Lengua Extranjera (DELE) expedidos por el Instituto Cervantes?",
                    "options": ["Vigencia indefinida (no caducan).", "Vigencia de seis meses únicamente.", "Vigencia de un año."],
                    "correctIndex": 0,
                    "explanation": "Los diplomas oficiales DELE tienen vigencia indefinida y validez internacional permanente."
                },
                {
                    "question": "¿Están obligados los ciudadanos nacionales de países hispanohablantes (donde el español es lengua oficial) a realizar el examen DELE para solicitar la nacionalidad española por residencia?",
                    "options": ["No, están exentos del examen DELE (solo deben realizar la prueba CCSE).", "Sí, deben aprobar obligatoriamente el DELE C2.", "Sí, deben realizar dos exámenes DELE."],
                    "correctIndex": 0,
                    "explanation": "Los nacionales de países o territorios en que el español sea idioma oficial están exentos del requisito del examen DELE, aunque sí deben superar la prueba CCSE."
                }
            ],
            "vocab": [
                {"lemma": "DELE", "pos": "noun", "translation": "Diploma of Spanish as a Foreign Language (DELE)", "ex_es": "El diploma DELE es el título oficial que acredita el grado de competencia en español.", "ex_en": "The DELE diploma is the official certificate that accredits the degree of competence in Spanish."},
                {"lemma": "nivel A2", "pos": "noun", "translation": "A2 level (minimum CEFR level required for Spanish nationality)", "ex_es": "Para la nacionalidad española se exige al menos el diploma DELE de nivel A2.", "ex_en": "For Spanish nationality at least the DELE A2 level diploma is required."},
                {"lemma": "vigencia indefinida", "pos": "noun", "translation": "indefinite / lifetime validity", "ex_es": "Los diplomas DELE tienen vigencia indefinida y no necesitan renovarse.", "ex_en": "DELE diplomas have indefinite validity and do not need to be renewed."},
                {"lemma": "exento", "pos": "adjective", "translation": "exempt", "ex_es": "Los ciudadanos de países hispanohablantes están exentos de presentar el diploma DELE.", "ex_en": "Citizens of Spanish-speaking countries are exempt from submitting the DELE diploma."},
                {"lemma": "SIELE", "pos": "noun", "translation": "International Assessment Service for the Spanish Language (SIELE)", "ex_es": "El SIELE certifica por medios electrónicos el grado de dominio del español con carácter panhispánico.", "ex_en": "SIELE electronically certifies the degree of mastery of Spanish with a pan-Hispanic character."},
                {"lemma": "destreza", "pos": "noun", "translation": "language skill", "ex_es": "El examen evalúa cada destreza: leer, escuchar, escribir y hablar en español.", "ex_en": "The exam evaluates each skill: reading, listening, writing, and speaking in Spanish."},
                {"lemma": "dispensa", "pos": "noun", "translation": "official waiver / exemption", "ex_es": "El Ministerio de Justicia puede conceder dispensa parcial o total a personas con discapacidad o que no sepan leer ni escribir.", "ex_en": "The Ministry of Justice can grant a partial or total waiver to people with disabilities or who do not know how to read or write."},
                {"lemma": "nacionalidad por residencia", "pos": "noun", "translation": "nationality by residence", "ex_es": "La nacionalidad por residencia requiere acreditar buena conducta cívica e integración mediante el CCSE y el DELE.", "ex_en": "Nationality by residence requires proving good civic conduct and integration through the CCSE and DELE."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es el nivel mínimo del diploma DELE requerido para solicitar la nacionalidad española por residencia (para solicitantes de países no hispanohablantes)?", "options": ["Nivel A2 o superior", "Nivel C2 únicamente", "Nivel C1 mínimo", "No existe requisito de nivel"], "answer": "Nivel A2 o superior", "explanation": "Se exige el diploma DELE de nivel A2 o superior."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué institución expide los diplomas oficiales DELE en nombre del Ministerio de Educación de España?", "options": ["El Instituto Cervantes", "El Banco de España", "La Dirección General de Tráfico", "El Senado"], "answer": "El Instituto Cervantes", "explanation": "El Instituto Cervantes organiza las pruebas y expide los diplomas DELE en nombre del Ministerio de Educación."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Para la nacionalidad española se exige acreditar al menos el diploma ___ de nivel A2 o superior.", "answer": "DELE", "english": "For Spanish nationality it is required to accredit at least the DELE diploma at level A2 or higher.", "explanation": "DELE = Diploma de Español como Lengua Extranjera."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "Los ciudadanos nacionales de países hispanohablantes están ___ de realizar el examen DELE.", "answer": "exentos", "english": "Citizens who are nationals of Spanish-speaking countries are exempt from taking the DELE exam.", "explanation": "'Estar exento de' means to be exempt from."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the requirement for the DELE diploma:", "words": ["Para", "la", "nacionalidad", "se", "exige", "el", "diploma", "DELE", "de", "nivel", "A2", "o", "superior."], "answer": "Para la nacionalidad se exige el diploma DELE de nivel A2 o superior.", "english": "For nationality the DELE diploma at level A2 or higher is required."},
                {"type": "dictation", "cat": "listening", "text": "Los diplomas DELE tienen reconocimiento internacional y vigencia indefinida.", "english": "DELE diplomas have international recognition and indefinite validity."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Caduca el diploma oficial DELE una vez que el candidato ha resultado «Apto»?", "options": ["No, tiene vigencia indefinida", "Sí, caduca a los dos años", "Sí, caduca cada doce meses", "Caduca al cambiar de municipio"], "answer": "No, tiene vigencia indefinida", "explanation": "Los diplomas DELE tienen vigencia indefinida."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los diplomas DELE tienen vigencia ___: una vez aprobados, no caducan nunca.", "answer": "indefinida", "english": "DELE diplomas have indefinite validity: once passed, they never expire.", "explanation": "'Vigencia indefinida'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about Spanish-speaking applicants:", "words": ["Los", "ciudadanos", "de", "países", "hispanohablantes", "solo", "deben", "realizar", "la", "prueba", "CCSE."], "answer": "Los ciudadanos de países hispanohablantes solo deben realizar la prueba CCSE.", "english": "Citizens of Spanish-speaking countries only have to take the CCSE test."}
            ]
        },
        {
            "num": "03",
            "story_slug": "pruebaccse",
            "title": "La prueba CCSE de nacionalidad: estructura (25 preguntas, 60% y 15 aciertos), tareas y duración",
            "goal": "Master every official detail of the CCSE exam itself (often tested directly on Task 1/5 of the CCSE!): 25 questions total (15 on Government, Legislation and Citizen Participation [60%]; 10 on Spanish Culture, History and Society [40%]), 45 minutes maximum duration, 15 correct answers (60%) required to receive 'Apto', 4-year validity of the certificate, and second-chance registration included.",
            "grammar_slug": "para-obtener-la-calificacion-de-apto",
            "grammar_title": "Criterios de evaluación: 'constar de + cifra', 'superar el porcentaje del' y 'obtener la calificación de Apto'",
            "grammar_summary": "Using 'constar de 25 preguntas', 'contestar correctamente al menos a 15 de las 25 preguntas (60%)' and 'tener una validez de cuatro años'.",
            "grammar_text": "The Instituto Cervantes frequently includes questions on the CCSE exam about the rules of the **CCSE test** (Prueba de Conocimientos Constitucionales y Socioculturales de España) itself! Memorize these exact numbers: the test consists of **25 questions** ('consta de 25 preguntas cerradas' — multiple choice with 3 options and true/false), divided into **60% (15 questions)** on Government, Legislation and Citizen Participation (Tasks 1–3) and **40% (10 questions)** on Spanish Culture, History and Society (Tasks 4–5). Its maximum duration is **45 minutes**. To pass ('obtener la calificación de Apto'), you must answer at least **15 out of 25 questions correctly (60%)**. Each registration fee includes **two opportunities** ('dos convocatorias'), and the CCSE certificate is valid for **4 years**.",
            "grammar_examples": [
                {"spanish": "La prueba CCSE consta de 25 preguntas y tiene una duración máxima de 45 minutos.", "english": "The CCSE test consists of 25 questions and has a maximum duration of 45 minutes."},
                {"spanish": "Para obtener la calificación de «Apto» es necesario responder correctamente al menos a 15 de las 25 preguntas (el 60%).", "english": "To obtain the grade of 'Pass' ('Apto') it is necessary to answer at least 15 of the 25 questions correctly (60%)."},
                {"spanish": "El certificado de haber superado la prueba CCSE tiene una validez de cuatro años desde la fecha de aprobación.", "english": "The certificate of having passed the CCSE test has a validity of four years from the date of approval."}
            ],
            "grammar_tip": "Memorize every single number here — they are real CCSE official exam questions: **25 questions** total (**15** Government/Law = 60%, **10** Culture/History/Society = 40%); **15 correct answers (60%)** to pass ('Apto'); **45 minutes** duration; **2 attempts** per registration; **4 years** certificate validity!",
            "story_title": "Veinticinco preguntas y cuarenta y cinco minutos",
            "story_summary": "On the last Thursday of the month, candidates sit the official CCSE exam at an Instituto Cervantes center, reviewing the 25-question structure, the 15-point pass mark, and the 4-year validity of the Apto certificate.",
            "story_location": "Madrid, Aula de Examen CCSE",
            "story_paragraphs": [
                "El último jueves de cada mes (salvo en agosto y diciembre), miles de candidatos acuden a los centros de examen acreditados por el Instituto Cervantes en España y en todo el mundo para realizar la prueba CCSE (Conocimientos Constitucionales y Socioculturales de España).",
                "La estructura oficial de la prueba es muy precisa y suele ser objeto de pregunta en el propio examen: el cuadernillo consta de un total de 25 preguntas de respuesta cerrada (preguntas de selección múltiple con tres opciones y preguntas de verdadero o falso), que los candidatos deben responder en un tiempo máximo de 45 minutos.",
                "El contenido se divide en dos grandes bloques: el 60% de la prueba (15 preguntas, repartidas en las Tareas 1, 2 y 3) evalúa conocimientos sobre el Gobierno, la legislación y la participación ciudadana en España; el 40% restante (10 preguntas, en las Tareas 4 y 5) evalúa conocimientos sobre la organización territorial, la geografía, la cultura, la historia y la sociedad españolas.",
                "Cada respuesta correcta suma un punto y las respuestas incorrectas o en blanco no restan puntuación. Para superar la prueba y obtener la calificación de «Apto», es necesario contestar correctamente al menos a 15 de las 25 preguntas (es decir, el 60% del total).",
                "Además, la inscripción en la prueba CCSE da derecho a presentarse hasta un máximo de dos veces (una segunda oportunidad sin pagar de nuevo la tasa si el candidato resulta «No apto» o no se presenta en la primera), y el certificado electrónico de «Apto» tiene una validez oficial de cuatro años."
            ],
            "comp_questions": [
                {
                    "question": "¿De cuántas preguntas consta en total la prueba oficial CCSE y cuántas es necesario responder correctamente como mínimo para obtener la calificación de «Apto»?",
                    "options": ["Consta de 25 preguntas y es necesario acertar al menos 15 preguntas (el 60%).", "Consta de 100 preguntas y hay que acertar 90.", "Consta de 10 preguntas abiertas de redacción."],
                    "correctIndex": 0,
                    "explanation": "La prueba CCSE tiene 25 preguntas (15 de Gobierno/leyes y 10 de cultura/historia/sociedad) y se aprueba («Apto») con un mínimo de 15 respuestas correctas (60%)."
                },
                {
                    "question": "¿Cuál es la duración máxima establecida para realizar el examen CCSE?",
                    "options": ["45 minutos.", "3 horas.", "15 minutos."],
                    "correctIndex": 0,
                    "explanation": "El tiempo máximo para contestar las 25 preguntas de la prueba CCSE es de 45 minutos."
                },
                {
                    "question": "¿Qué validez temporal tiene el certificado oficial de haber resultado «Apto» en la prueba CCSE?",
                    "options": ["Cuatro años desde la fecha de aprobación del acta de calificación.", "Seis meses.", "Un mes."],
                    "correctIndex": 0,
                    "explanation": "El certificado de la prueba CCSE tiene una validez de 4 años (a diferencia del diploma DELE, cuya vigencia es indefinida)."
                }
            ],
            "vocab": [
                {"lemma": "prueba CCSE", "pos": "noun", "translation": "CCSE test (Constitutional and Sociocultural Knowledge of Spain)", "ex_es": "La prueba CCSE consta de veinticinco preguntas y dura cuarenta y cinco minutos.", "ex_en": "The CCSE test consists of twenty-five questions and lasts forty-five minutes."},
                {"lemma": "Apto", "pos": "adjective", "translation": "Pass / Qualified (official grade on CCSE and DELE)", "ex_es": "Para obtener la calificación de 'Apto' en el CCSE hay que acertar al menos quince preguntas.", "ex_en": "To obtain the grade of 'Pass' on the CCSE you must get at least fifteen questions right."},
                {"lemma": "cuarenta y cinco minutos", "pos": "noun", "translation": "forty-five minutes (maximum duration of CCSE exam)", "ex_es": "Los candidatos disponen de cuarenta y cinco minutos para completar la hoja de respuestas.", "ex_en": "Candidates have forty-five minutes to complete the answer sheet."},
                {"lemma": "quince aciertos", "pos": "noun", "translation": "fifteen correct answers (60% pass threshold)", "ex_es": "El mínimo para superar la prueba CCSE es lograr quince aciertos sobre veinticinco.", "ex_en": "The minimum to pass the CCSE test is achieving fifteen correct answers out of twenty-five."},
                {"lemma": "validez de cuatro años", "pos": "noun", "translation": "four-year validity (of the CCSE certificate)", "ex_es": "El certificado de la prueba CCSE tiene una validez de cuatro años.", "ex_en": "The CCSE test certificate has a validity of four years."},
                {"lemma": "segunda oportunidad", "pos": "noun", "translation": "second chance / retake included in registration", "ex_es": "La inscripción en el examen CCSE incluye una segunda oportunidad sin coste adicional.", "ex_en": "Registration for the CCSE exam includes a second opportunity at no additional cost."},
                {"lemma": "hoja de respuestas", "pos": "noun", "translation": "answer sheet", "ex_es": "Todas las contestaciones deben marcarse con claridad en la hoja de respuestas.", "ex_en": "All answers must be clearly marked on the answer sheet."},
                {"lemma": "manual CCSE", "pos": "noun", "translation": "CCSE study manual", "ex_es": "El Instituto Cervantes publica gratuitamente cada año el manual CCSE para preparar la prueba.", "ex_en": "The Instituto Cervantes publishes the CCSE manual free of charge every year to prepare for the test."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántas preguntas tiene la prueba CCSE y cuántas hay que acertar como mínimo para ser «Apto»?", "options": ["25 preguntas en total y un mínimo de 15 aciertos (60%)", "50 preguntas y 40 aciertos", "10 preguntas y 8 aciertos", "100 preguntas y 50 aciertos"], "answer": "25 preguntas en total y un mínimo de 15 aciertos (60%)", "explanation": "La prueba CCSE consta de 25 preguntas y requiere al menos 15 respuestas correctas (60%) para obtener «Apto»."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿De cuánto tiempo disponen los candidatos para realizar la prueba CCSE?", "options": ["45 minutos", "120 minutos", "15 minutos", "90 minutos"], "answer": "45 minutos", "explanation": "La duración máxima de la prueba CCSE es de 45 minutos."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Para obtener la calificación de «___» en la prueba CCSE es necesario acertar al menos 15 de las 25 preguntas.", "answer": "Apto", "english": "To obtain the grade of 'Pass' ('Apto') on the CCSE test it is necessary to get at least 15 of the 25 questions right.", "explanation": "'Apto' is the official passing grade."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "El certificado de haber superado la prueba CCSE tiene una validez de ___ años.", "answer": "cuatro", "english": "The certificate of having passed the CCSE test has a validity of four years.", "explanation": "The CCSE certificate is valid for 4 years ('cuatro años')."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the CCSE exam structure:", "words": ["La", "prueba", "CCSE", "consta", "de", "veinticinco", "preguntas", "y", "dura", "cuarenta", "y", "cinco", "minutos."], "answer": "La prueba CCSE consta de veinticinco preguntas y dura cuarenta y cinco minutos.", "english": "The CCSE test consists of twenty-five questions and lasts forty-five minutes."},
                {"type": "dictation", "cat": "listening", "text": "Para aprobar el examen se necesitan al menos quince respuestas correctas.", "english": "To pass the exam at least fifteen correct answers are needed."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué porcentaje de la prueba CCSE corresponde a Gobierno, legislación y participación ciudadana (15 preguntas) y qué porcentaje a cultura, historia y sociedad (10 preguntas)?", "options": ["60% Gobierno y legislación; 40% cultura, historia y sociedad", "50% cada parte", "80% cultura y 20% leyes", "100% geografía"], "answer": "60% Gobierno y legislación; 40% cultura, historia y sociedad", "explanation": "El 60% (15 preguntas) corresponde a Gobierno, legislación y participación ciudadana, y el 40% (10 preguntas) a cultura, historia y sociedad."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "La tasa de inscripción en el examen CCSE da derecho a presentarse hasta ___ veces.", "answer": "dos", "english": "The registration fee for the CCSE exam entitles the candidate to sit the test up to two times.", "explanation": "Each registration includes up to 2 attempts ('dos convocatorias')."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the CCSE pass threshold:", "words": ["Es", "necesario", "acertar", "quince", "de", "las", "veinticinco", "preguntas", "para", "ser", "Apto."], "answer": "Es necesario acertar quince de las veinticinco preguntas para ser Apto.", "english": "It is necessary to get fifteen of the twenty-five questions right to pass."}
            ]
        },
        {
            "num": "04",
            "story_slug": "institutoslenguas",
            "title": "Institutos de proyección de las lenguas cooficiales y red cultural europea",
            "goal": "Recognize the sister institutions that promote Spain's co-official languages internationally (Institut Ramon Llull for Catalan language and culture, Etxepare Euskal Institutua for Basque language and culture) and European counterparts (Goethe-Institut, Alliance Française, British Council, Società Dante Alighieri, Instituto Camões).",
            "grammar_slug": "al-igual-que-homologo",
            "grammar_title": "Comparación institucional: 'al igual que' y 'ser el organismo homólogo de'",
            "grammar_summary": "Using 'al igual que el Instituto Cervantes' and 'ser el organismo encargado de proyectar en el exterior'.",
            "grammar_text": "To compare cultural institutes across languages and countries, Spanish uses 'al igual que' (just like) and 'ser la institución homóloga encargada de...' (to be the counterpart institution in charge of...). Within Spain, the **Institut Ramon Llull** promotes the Catalan language and culture internationally, and the **Etxepare Euskal Institutua** (Instituto Vasco Etxepare) promotes the Basque language (Euskera) and Basque creation abroad. Together with the **Instituto Cervantes** (Awarded the Prince of Asturias Award for Communication and Humanities in 2005 alongside the Alliance Française, Società Dante Alighieri, British Council, Goethe-Institut, and Instituto Camões), they represent Spain's cultural diplomacy.",
            "grammar_examples": [
                {"spanish": "Al igual que el Instituto Cervantes difunde el español, el Institut Ramon Llull proyecta la lengua y cultura catalanas en el exterior.", "english": "Just as the Instituto Cervantes disseminates Spanish, the Institut Ramon Llull projects Catalan language and culture abroad."},
                {"spanish": "El Instituto Vasco Etxepare promueve internacionalmente el euskera y la creación vasca.", "english": "The Etxepare Basque Institute promotes Euskera and Basque creation internationally."},
                {"spanish": "El Instituto Cervantes recibió en 2005 el Premio Príncipe de Asturias junto a los grandes institutos culturales europeos.", "english": "The Instituto Cervantes received the Prince of Asturias Award in 2005 alongside the major European cultural institutes."}
            ],
            "grammar_tip": "Remember for CCSE cultural questions: **Institut Ramon Llull** = proyección exterior de la lengua y cultura catalanas; **Instituto Vasco Etxepare** = proyección exterior del euskera y la cultura vasca; **Instituto Cervantes** = proyección universal del español y las culturas hispánicas.",
            "story_title": "Diplomacia cultural y lenguas en diálogo",
            "story_summary": "At a European Day of Languages festival in Madrid, representatives from the Instituto Cervantes, the Institut Ramon Llull, the Etxepare Basque Institute, and the Council of Galicia's language network celebrate multilingual cultural projection.",
            "story_location": "Madrid, Círculo de Bellas Artes",
            "story_paragraphs": [
                "Cada 26 de septiembre, con motivo del Día Europeo de las Lenguas, el Instituto Cervantes organiza en Madrid jornadas conjuntas con las instituciones que proyectan en el exterior las demás lenguas oficiales de España y con los institutos culturales de otros países europeos.",
                "Junto a la labor mundial del Instituto Cervantes, las comunidades autónomas con lengua propia cuentan con organismos específicos para difundir su lengua y su creación literaria y artística en las universidades y festivales internacionales.",
                "Así, el Institut Ramon Llull es el consorcio público encargado de la proyección exterior de la lengua y la cultura catalanas, organizando enseñanzas universitarias y exámenes oficiales de catalán fuera de su ámbito lingüístico.",
                "Del mismo modo, el Etxepare Euskal Institutua (Instituto Vasco Etxepare) tiene como misión difundir el euskera y la cultura vasca en todo el mundo, mientras que la Xunta de Galicia impulsa la red de lectorados de lengua, literatura y cultura gallegas y los certificados oficiales Celga.",
                "En el ámbito europeo, el Instituto Cervantes recibió en el año 2005 el Premio Príncipe de Asturias de Comunicación y Humanidades conjuntamente con sus cinco instituciones homólogas europeas: el Goethe-Institut (Alemania), la Alliance Française (Francia), el British Council (Reino Unido), la Società Dante Alighieri (Italia) y el Instituto Camões (Portugal)."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué institución pública promueve en el exterior la enseñanza y difusión de la lengua y la cultura catalanas?",
                    "options": ["El Institut Ramon Llull.", "El Instituto de Crédito Oficial.", "El Instituto Geográfico Nacional."],
                    "correctIndex": 0,
                    "explanation": "El Institut Ramon Llull es la institución encargada de la proyección exterior de la lengua y la cultura catalanas."
                },
                {
                    "question": "¿Cuál es la misión del Instituto Vasco Etxepare (Etxepare Euskal Institutua)?",
                    "options": ["Promover y difundir internacionalmente el euskera y la cultura vasca.", "Regular el tráfico marítimo en el mar Cantábrico.", "Gestionar los parques nacionales de Canarias."],
                    "correctIndex": 0,
                    "explanation": "El Instituto Vasco Etxepare promueve el euskera y la creación cultural vasca en el ámbito internacional."
                },
                {
                    "question": "¿Qué importante galardón español recibió el Instituto Cervantes en 2005 junto con los otros cinco grandes institutos culturales europeos (Goethe, Alliance Française, British Council, Dante Alighieri y Camões)?",
                    "options": ["El Premio Príncipe de Asturias de Comunicación y Humanidades.", "El Premio Goya a la mejor película.", "La Copa del Rey."],
                    "correctIndex": 0,
                    "explanation": "En 2005 los seis grandes institutos culturales europeos recibieron conjuntamente el Premio Príncipe de Asturias de Comunicación y Humanidades."
                }
            ],
            "vocab": [
                {"lemma": "Institut Ramon Llull", "pos": "noun", "translation": "Institut Ramon Llull (institution promoting Catalan language and culture abroad)", "ex_es": "El Institut Ramon Llull impulsa la enseñanza y traducción de la literatura catalana en el exterior.", "ex_en": "The Institut Ramon Llull promotes the teaching and translation of Catalan literature abroad."},
                {"lemma": "Instituto Vasco Etxepare", "pos": "noun", "translation": "Etxepare Basque Institute (promoting Basque language and culture abroad)", "ex_es": "El Instituto Vasco Etxepare difunde la lengua vasca en universidades internacionales.", "ex_en": "The Etxepare Basque Institute promotes the Basque language in international universities."},
                {"lemma": "proyección exterior", "pos": "noun", "translation": "international projection / outreach abroad", "ex_es": "La proyección exterior de las lenguas españolas fortalece el diálogo cultural.", "ex_en": "The international projection of the Spanish languages strengthens cultural dialogue."},
                {"lemma": "homólogo", "pos": "adjective", "translation": "counterpart / equivalent", "ex_es": "El Instituto Cervantes colabora estrechamente con sus institutos homólogos europeos.", "ex_en": "The Instituto Cervantes collaborates closely with its European counterpart institutes."},
                {"lemma": "lectorado", "pos": "noun", "translation": "university language lectureship", "ex_es": "Numerosas universidades extranjeras cuentan con un lectorado de español, catalán, gallego o euskera.", "ex_en": "Numerous foreign universities have a lectureship in Spanish, Catalan, Galician, or Euskera."},
                {"lemma": "diplomacia cultural", "pos": "noun", "translation": "cultural diplomacy", "ex_es": "El Instituto Cervantes es el pilar principal de la diplomacia cultural española.", "ex_en": "The Instituto Cervantes is the main pillar of Spanish cultural diplomacy."},
                {"lemma": "traducción", "pos": "noun", "translation": "translation", "ex_es": "Los institutos culturales apoyan la traducción de obras literarias a otros idiomas.", "ex_en": "Cultural institutes support the translation of literary works into other languages."},
                {"lemma": "cooperación cultural", "pos": "noun", "translation": "cultural cooperation", "ex_es": "España mantiene programas permanentes de cooperación cultural con Iberoamérica y Europa.", "ex_en": "Spain maintains permanent cultural cooperation programs with Ibero-America and Europe."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué institución tiene como misión la proyección exterior de la lengua y la cultura catalanas?", "options": ["El Institut Ramon Llull", "El Instituto Nacional de la Seguridad Social", "El Instituto Astrofísico de Canarias", "El Instituto de Salud Carlos III"], "answer": "El Institut Ramon Llull", "explanation": "El Institut Ramon Llull promueve internacionalmente la lengua y la cultura catalanas."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué institución promueve internacionalmente el euskera y la cultura vasca fuera del País Vasco?", "options": ["El Instituto Vasco Etxepare (Etxepare Euskal Institutua)", "El SEPRONA", "El Tribunal de Cuentas", "La Junta Electoral Central"], "answer": "El Instituto Vasco Etxepare (Etxepare Euskal Institutua)", "explanation": "El Instituto Vasco Etxepare difunde la lengua vasca y la creación vasca en el mundo."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Institut Ramon ___ promueve en el exterior la lengua y la cultura catalanas.", "answer": "Llull", "english": "The Institut Ramon Llull promotes Catalan language and culture abroad.", "explanation": "'Institut Ramon Llull'."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Instituto Vasco ___ difunde el euskera y la cultura vasca en el ámbito internacional.", "answer": "Etxepare", "english": "The Etxepare Basque Institute disseminates Euskera and Basque culture internationally.", "explanation": "'Instituto Vasco Etxepare'."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about cultural diplomacy:", "words": ["El", "Instituto", "Cervantes", "colabora", "con", "los", "institutos", "de", "las", "lenguas", "cooficiales."], "answer": "El Instituto Cervantes colabora con los institutos de las lenguas cooficiales.", "english": "The Instituto Cervantes collaborates with the institutes of the co-official languages."},
                {"type": "dictation", "cat": "listening", "text": "El Institut Ramon Llull difunde la lengua y la cultura catalanas en el exterior.", "english": "The Institut Ramon Llull disseminates Catalan language and culture abroad."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Con qué otras instituciones compartió el Instituto Cervantes el Premio Príncipe de Asturias de Comunicación y Humanidades en 2005?", "options": ["Con los principales institutos culturales europeos (Goethe-Institut, Alliance Française, British Council, Dante Alighieri e Instituto Camões)", "Con los clubes de fútbol de primera división", "Con los bancos centrales europeos", "Con las aerolíneas internacionales"], "answer": "Con los principales institutos culturales europeos (Goethe-Institut, Alliance Française, British Council, Dante Alighieri e Instituto Camões)", "explanation": "El premio distinguió conjuntamente a los seis grandes institutos europeos de difusión lingüística y cultural."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Instituto Cervantes es el principal instrumento de la ___ cultural española en el mundo.", "answer": "diplomacia", "english": "The Instituto Cervantes is the main instrument of Spanish cultural diplomacy in the world.", "explanation": "'Diplomacia cultural'."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the Etxepare Institute:", "words": ["El", "Instituto", "Etxepare", "promueve", "el", "euskera", "en", "universidades", "de", "todo", "el", "mundo."], "answer": "El Instituto Etxepare promueve el euskera en universidades de todo el mundo.", "english": "The Etxepare Institute promotes Euskera at universities all over the world."}
            ]
        },
        {
            "num": "05",
            "story_slug": "bibliotecavirtual",
            "title": "El español en la era digital: el Centro Virtual Cervantes, el Anuario y los Congresos Internacionales",
            "goal": "Know the digital and global cultural initiatives led by the Instituto Cervantes and the RAE: the Centro Virtual Cervantes (CVC, created in 1997), the yearbook 'El español en el mundo', the International Congresses of the Spanish Language (CILE), and the Biblioteca Virtual Miguel de Cervantes.",
            "grammar_slug": "poner-a-disposicion-de",
            "grammar_title": "Acceso público y difusión digital: 'poner a disposición de' y 'celebrarse periódicamente'",
            "grammar_summary": "Using 'poner gratuitamente a disposición de los usuarios' and 'publicar anualmente el informe'.",
            "grammar_text": "To describe digital public resources and periodic cultural summits, Spanish uses 'poner a disposición de + destinatario' (to make available to) and 'celebrarse cada tres años / periódicamente'. Since 1997, the Instituto Cervantes has operated the **Centro Virtual Cervantes (CVC)**, which makes teaching resources, literature, and the **CCSE portal** freely available to students and teachers worldwide. Every year, the Instituto Cervantes also publishes the official yearbook ***El español en el mundo*** (demographic and cultural report on the Spanish language) and co-organizes with the RAE and ASALE the **Congresos Internacionales de la Lengua Española (CILE)**.",
            "grammar_examples": [
                {"spanish": "El Centro Virtual Cervantes pone recursos educativos y culturales a disposición de estudiantes y profesores.", "english": "The Centro Virtual Cervantes makes educational and cultural resources available to students and teachers."},
                {"spanish": "El Instituto Cervantes publica anualmente el informe demográfico «El español en el mundo».", "english": "The Instituto Cervantes annually publishes the demographic report 'Spanish in the World'."},
                {"spanish": "Los Congresos Internacionales de la Lengua Española reúnen a escritores, académicos y expertos de todo el ámbito hispánico.", "english": "The International Congresses of the Spanish Language bring together writers, academics, and experts from across the Hispanic world."}
            ],
            "grammar_tip": "Remember: the official portal where candidates register for the **CCSE** and **DELE** exams and download the free annual preparation manual is managed by the **Instituto Cervantes** (`examenes.cervantes.es`).",
            "story_title": "Una comunidad global conectada en español",
            "story_summary": "From preparing the CCSE exam online through the Instituto Cervantes portal to consulting the annual report 'El español en el mundo' and the International Congresses of the Spanish Language.",
            "story_location": "Madrid y Cádiz",
            "story_paragraphs": [
                "Más allá de sus centros presenciales repartidos por los cinco continentes, el Instituto Cervantes impulsa desde 1997 el Centro Virtual Cervantes (CVC), uno de los portales culturales y educativos en español más visitados de internet.",
                "A través de sus plataformas digitales (`examenes.cervantes.es`), el Instituto Cervantes pone gratuitamente a disposición de todos los candidatos a la nacionalidad española el manual oficial de preparación de la prueba CCSE, las guías de examen y el acceso a sus certificaciones.",
                "Cada año, el Instituto Cervantes publica también su prestigioso Anuario, titulado *El español en el mundo*, que ofrece los datos actualizados sobre la demografía del idioma: el español es hoy la segunda lengua materna del mundo por número de hablantes (tras el chino mandarín) y una de las lenguas más estudiadas como idioma extranjero.",
                "Asimismo, el Instituto Cervantes y la Real Academia Española (junto con la ASALE) organizan periódicamente los Congresos Internacionales de la Lengua Española (CILE), grandes encuentros celebrados en ciudades de América y de España —como Valladolid o Cádiz— donde escritores, científicos, periodistas y profesores debaten el presente y el futuro del idioma común.",
                "De este modo, la lengua de Cervantes funciona hoy como un puente vivo de cultura, ciencia y ciudadanía que une a España con más de veinte naciones hermanas y con millones de estudiantes en todo el planeta."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la posición del idioma español en el mundo por número de hablantes nativos (lengua materna), según los informes anuales del Instituto Cervantes?",
                    "options": ["Es la segunda lengua materna del mundo por número de hablantes nativos.", "Es la décima lengua del mundo.", "Solo se habla en el continente europeo."],
                    "correctIndex": 0,
                    "explanation": "Según el anuario *El español en el mundo* del Instituto Cervantes, el español es la segunda lengua materna del mundo por número de hablantes nativos."
                },
                {
                    "question": "¿Qué organismo pone gratuitamente a disposición de los candidatos el manual anual de preparación y gestiona la inscripción en la prueba CCSE?",
                    "options": ["El Instituto Cervantes (en su portal de exámenes).", "La Agencia Estatal de Meteorología.", "El Museo Nacional del Prado."],
                    "correctIndex": 0,
                    "explanation": "El Instituto Cervantes publica gratuitamente el manual oficial de preparación y gestiona íntegramente las convocatorias de la prueba CCSE."
                },
                {
                    "question": "¿Qué grandes encuentros internacionales organizan conjuntamente el Instituto Cervantes, la RAE y las Academias de la Lengua Española en ciudades de España e Hispanoamérica?",
                    "options": ["Los Congresos Internacionales de la Lengua Española (CILE).", "Los Juegos Mediterráneos.", "La Feria Internacional deuestras."],
                    "correctIndex": 0,
                    "explanation": "Los Congresos Internacionales de la Lengua Española (CILE) son organizados por el Instituto Cervantes, la RAE y la ASALE."
                }
            ],
            "vocab": [
                {"lemma": "Centro Virtual Cervantes", "pos": "noun", "translation": "Cervantes Virtual Center (CVC)", "ex_es": "El Centro Virtual Cervantes ofrece materiales didácticos y culturales en internet desde 1997.", "ex_en": "The Cervantes Virtual Center has offered educational and cultural materials on the internet since 1997."},
                {"lemma": "Anuario", "pos": "noun", "translation": "Yearbook ('El español en el mundo')", "ex_es": "El Anuario del Instituto Cervantes analiza cada año el crecimiento del español en el mundo.", "ex_en": "The Instituto Cervantes Yearbook analyzes the growth of Spanish in the world every year."},
                {"lemma": "Congreso Internacional de la Lengua Española", "pos": "noun", "translation": "International Congress of the Spanish Language (CILE)", "ex_es": "Cádiz acogió el IX Congreso Internacional de la Lengua Española.", "ex_en": "Cádiz hosted the 9th International Congress of the Spanish Language."},
                {"lemma": "segunda lengua materna", "pos": "noun", "translation": "second mother tongue in the world", "ex_es": "El español es la segunda lengua materna del mundo por número de hablantes.", "ex_en": "Spanish is the second mother tongue in the world by number of speakers."},
                {"lemma": "portal de exámenes", "pos": "noun", "translation": "exam portal (examenes.cervantes.es)", "ex_es": "La inscripción en las pruebas CCSE y DELE se realiza en el portal de exámenes del Instituto Cervantes.", "ex_en": "Registration for the CCSE and DELE tests is done on the Instituto Cervantes exam portal."},
                {"lemma": "demografía", "pos": "noun", "translation": "demographics", "ex_es": "La demografía de la lengua española supera ya los quinientos millones de hablantes.", "ex_en": "The demographics of the Spanish language now exceed five hundred million speakers."},
                {"lemma": "lengua extranjera", "pos": "noun", "translation": "foreign language", "ex_es": "Más de veinte millones de alumnos estudian hoy español como lengua extranjera.", "ex_en": "More than twenty million students study Spanish as a foreign language today."},
                {"lemma": "comunidad hispánica", "pos": "noun", "translation": "Hispanic community", "ex_es": "La comunidad hispánica comparte un rico patrimonio literario, histórico y lingüístico.", "ex_en": "The Hispanic community shares a rich literary, historical, and linguistic heritage."}
            ],
            "exercises": [
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué organismo publica gratuitamente el manual oficial para preparar la prueba CCSE y organiza las convocatorias mensuales?", "options": ["El Instituto Cervantes", "El Tribunal Supremo", "El Banco Central Europeo", "La Real Academia de Bellas Artes"], "answer": "El Instituto Cervantes", "explanation": "El Instituto Cervantes elabora el manual y administra las pruebas CCSE y DELE."},
                {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Qué lugar ocupa el español en el mundo por número de hablantes nativos (como lengua materna)?", "options": ["Es la segunda lengua materna del mundo", "Es la décima lengua del mundo", "Es la vigésima lengua del mundo", "Solo se habla en España"], "answer": "Es la segunda lengua materna del mundo", "explanation": "El español es la segunda lengua del mundo por número de hablantes nativos."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Instituto Cervantes publica cada año el informe «El español en el ___».", "answer": "mundo", "english": "The Instituto Cervantes publishes every year the report 'Spanish in the World'.", "explanation": "'El español en el mundo' is the annual report of the Instituto Cervantes."},
                {"type": "fill-blank", "cat": "grammar", "prompt": "El Centro ___ Cervantes pone recursos educativos y culturales a disposición de los usuarios en internet.", "answer": "Virtual", "english": "The Cervantes Virtual Center makes educational and cultural resources available to users on the internet.", "explanation": "'Centro Virtual Cervantes' (CVC)."},
                {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about Spanish as a native language:", "words": ["El", "español", "es", "la", "segunda", "lengua", "materna", "del", "mundo."], "answer": "El español es la segunda lengua materna del mundo.", "english": "Spanish is the second mother tongue in the world."},
                {"type": "dictation", "cat": "listening", "text": "El Instituto Cervantes organiza la prueba de conocimientos constitucionales y socioculturales.", "english": "The Instituto Cervantes organizes the constitutional and sociocultural knowledge test."},
                {"type": "multiple-choice", "cat": "reading", "prompt": "¿Qué instituciones organizan conjuntamente los Congresos Internacionales de la Lengua Española (CILE)?", "options": ["El Instituto Cervantes, la Real Academia Española y la Asociación de Academias de la Lengua Española", "El Congreso de los Diputados y el Senado", "Las diputaciones provinciales", "Los colegios profesionales de abogados"], "answer": "El Instituto Cervantes, la Real Academia Española y la Asociación de Academias de la Lengua Española", "explanation": "Los CILE son coorganizados por el Instituto Cervantes, la RAE y la ASALE."},
                {"type": "fill-blank", "cat": "vocabulary", "prompt": "Más de veinte millones de alumnos estudian español como lengua ___ en el mundo.", "answer": "extranjera", "english": "More than twenty million students study Spanish as a foreign language in the world.", "explanation": "'Español como lengua extranjera' (ELE)."},
                {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Build the sentence about the CCSE registration portal:", "words": ["El", "Instituto", "Cervantes", "publica", "gratuitamente", "el", "manual", "de", "la", "prueba", "CCSE."], "answer": "El Instituto Cervantes publica gratuitamente el manual de la prueba CCSE.", "english": "The Instituto Cervantes publishes the manual for the CCSE test free of charge."}
            ]
        }
    ],
    "consolidation_exercises": [
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿En qué año fue creado el Instituto Cervantes para promover la enseñanza del español y difundir la cultura hispánica?", "options": ["En 1991", "En 1713", "En 1978", "En 2015"], "answer": "En 1991", "explanation": "El Instituto Cervantes fue creado por ley en 1991 (mientras que la RAE se fundó en 1713)."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿A qué ministerio está adscrito el Instituto Cervantes?", "options": ["Al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación", "Al Ministerio del Interior", "Al Ministerio de Sanidad", "Al Ministerio de Hacienda"], "answer": "Al Ministerio de Asuntos Exteriores, Unión Europea y Cooperación", "explanation": "Depende del Ministerio de Asuntos Exteriores."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Dónde se encuentran las dos sedes del Instituto Cervantes en España?", "options": ["En Madrid y en Alcalá de Henares", "En Sevilla y en Granada", "En Barcelona y en Tarragona", "En Valencia y en Alicante"], "answer": "En Madrid y en Alcalá de Henares", "explanation": "En Madrid (calle de Alcalá) y en Alcalá de Henares (Colegio del Rey)."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es el nivel mínimo del diploma oficial DELE exigido para solicitar la nacionalidad española por residencia (a candidatos de países no hispanohablantes)?", "options": ["Nivel A2 o superior", "Nivel C1 mínimo", "Nivel C2", "No se exige diploma"], "answer": "Nivel A2 o superior", "explanation": "Se exige el diploma DELE de nivel A2 o superior."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuántas preguntas tiene la prueba CCSE y cuántas respuestas correctas se necesitan como mínimo para obtener «Apto»?", "options": ["25 preguntas y al menos 15 respuestas correctas (60%)", "50 preguntas y 30 correctas", "20 preguntas y 10 correctas", "30 preguntas y 25 correctas"], "answer": "25 preguntas y al menos 15 respuestas correctas (60%)", "explanation": "La prueba CCSE consta de 25 preguntas y se aprueba con al menos 15 aciertos (60%)."},
        {"type": "multiple-choice", "cat": "grammar", "prompt": "¿Cuál es la duración máxima de la prueba CCSE y qué validez tiene su certificado de «Apto»?", "options": ["Duración máxima de 45 minutos y validez del certificado de 4 años", "Duración de 2 horas y validez de 6 meses", "Duración de 15 minutos y validez de 1 año", "Duración de 90 minutos y validez de 10 años"], "answer": "Duración máxima de 45 minutos y validez del certificado de 4 años", "explanation": "El examen dura como máximo 45 minutos y el certificado CCSE tiene validez de 4 años."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Instituto ___ organiza las pruebas oficiales DELE y CCSE.", "answer": "Cervantes", "english": "The Instituto Cervantes organizes the official DELE and CCSE tests.", "explanation": "'El Instituto Cervantes'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los ciudadanos nacionales de países hispanohablantes están ___ de realizar el examen DELE.", "answer": "exentos", "english": "Citizens who are nationals of Spanish-speaking countries are exempt from taking the DELE exam.", "explanation": "'Exentos del examen DELE'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Los diplomas oficiales DELE tienen vigencia ___: no caducan nunca.", "answer": "indefinida", "english": "Official DELE diplomas have indefinite validity: they never expire.", "explanation": "'Vigencia indefinida'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "Para aprobar la prueba CCSE y ser «___» hay que acertar al menos 15 de las 25 preguntas.", "answer": "Apto", "english": "To pass the CCSE test and be 'Pass' ('Apto') you must get at least 15 of the 25 questions right.", "explanation": "'Apto'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Institut Ramon ___ promueve en el exterior la lengua y la cultura catalanas.", "answer": "Llull", "english": "The Institut Ramon Llull promotes Catalan language and culture abroad.", "explanation": "'Institut Ramon Llull'."},
        {"type": "fill-blank", "cat": "vocabulary", "prompt": "El Instituto Vasco ___ promueve internacionalmente el euskera y la cultura vasca.", "answer": "Etxepare", "english": "The Etxepare Basque Institute promotes Euskera and Basque culture internationally.", "explanation": "'Instituto Vasco Etxepare'."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the Instituto Cervantes:", "words": ["El", "Instituto", "Cervantes", "promueve", "la", "enseñanza", "del", "español", "y", "la", "cultura", "hispánica."], "answer": "El Instituto Cervantes promueve la enseñanza del español y la cultura hispánica.", "english": "The Instituto Cervantes promotes the teaching of Spanish and Hispanic culture."},
        {"type": "sentence-builder", "cat": "grammar", "prompt": "Order the sentence about the CCSE test:", "words": ["La", "prueba", "CCSE", "tiene", "veinticinco", "preguntas", "y", "dura", "cuarenta", "y", "cinco", "minutos."], "answer": "La prueba CCSE tiene veinticinco preguntas y dura cuarenta y cinco minutos.", "english": "The CCSE test has twenty-five questions and lasts forty-five minutes."},
        {"type": "sentence-builder", "cat": "vocabulary", "prompt": "Order the sentence about the CCSE certificate validity:", "words": ["El", "certificado", "de", "la", "prueba", "CCSE", "tiene", "una", "validez", "de", "cuatro", "años."], "answer": "El certificado de la prueba CCSE tiene una validez de cuatro años.", "english": "The CCSE test certificate has a validity of four years."},
        {"type": "dictation", "cat": "listening", "text": "El Instituto Cervantes tiene sedes en Madrid y en Alcalá de Henares.", "english": "The Instituto Cervantes has headquarters in Madrid and in Alcalá de Henares."},
        {"type": "dictation", "cat": "listening", "text": "Para solicitar la nacionalidad se exige el diploma DELE de nivel A2 o superior.", "english": "To apply for nationality the DELE diploma at level A2 or higher is required."},
        {"type": "dictation", "cat": "listening", "text": "Para superar la prueba CCSE hay que acertar quince de las veinticinco preguntas.", "english": "To pass the CCSE test you must get fifteen of the twenty-five questions right."}
    ]
}


def main():
    emit_unit(UNIT_10)
    emit_unit(UNIT_11)
    emit_unit(UNIT_12)


if __name__ == "__main__":
    main()
