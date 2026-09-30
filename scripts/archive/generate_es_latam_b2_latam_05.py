#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Latin America Regional Studies Unit 5:
  - Title: "El Salvador & Honduras: Copán, Memory, Migration & Resilience"
    (El Salvador y Honduras: Copán, memoria, migración y resiliencia)
  - Stems: b2-salvadorhonduras-01 through b2-salvadorhonduras-consolidation
  - Cultural Focus: Copán & the Gulf of Fonseca trinational ecosystem,
    banana enclaves, Garifuna heritage & Berta Cáceres environmental defense,
    Monseñor Romero, liberation theology & Salvadoran peace accords,
    Northern Triangle migration & remittances, contemporary security debates.
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_latam_unit_5():
    # Vocab theme slug: b2-salvadorhonduras-vocab
    # Grammar skills:
    #   - relativos-posesivos-cuyo
    #   - verbos-atribucion-denuncia
    #   - conectores-contraste-discursivo
    #   - conectores-causales-complejos

    # --------------------------------------------------------------------------
    # Lesson 1: b2-salvadorhonduras-01 - Copán y el Golfo de Fonseca: Arqueología y cuencas compartidas
    # --------------------------------------------------------------------------
    l1 = "b2-salvadorhonduras-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.salvadorhonduras.01",
        "lesson": l1,
        "title": "Arqueología maya y ecología costera",
        "theme": "Escultura en Copán, escalinata jeroglífica y el Golfo de Fonseca",
        "words": [
            {"lemma": "la estela", "translation": "stela, carved stone slab", "pos": "noun"},
            {"lemma": "la escalinata jeroglífica", "translation": "hieroglyphic stairway", "pos": "noun"},
            {"lemma": "el bajorrelieve", "translation": "low relief, bas-relief", "pos": "noun"},
            {"lemma": "el manglar", "translation": "mangrove swamp", "pos": "noun"},
            {"lemma": "el estuario", "translation": "estuary", "pos": "noun"},
            {"lemma": "la cuenca compartida", "translation": "shared watershed", "pos": "noun"},
            {"lemma": "trinacional", "translation": "trinational", "pos": "adjective"},
            {"lemma": "el glifo", "translation": "glyph", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.salvadorhonduras.01.relativos-posesivos-cuyo",
        "title": "El pronombre relativo posesivo cuyo en la descripción formal",
        "sections": [
            {
                "type": "text",
                "title": "Concordancia y función del relativo 'cuyo/a/os/as'",
                "content": "El pronombre relativo posesivo 'cuyo' (y sus variantes 'cuya', 'cuyos', 'cuyas') es exclusivo de los registros formales y escritos en nivel B2. Establece un nexo de posesión o pertenencia entre su antecedente y el sustantivo que lo sigue inmediatamente, concordando SIEMPRE en género y número con la cosa poseída (el sustantivo que le sigue), jamás con el poseedor antecedente: 'Copán es una urbe clásica cuyas estelas destacan por su tridimensionalidad' ('cuyas' concuerda en femenino plural con 'estelas', no con 'Copán')."
            },
            {
                "type": "table",
                "title": "Reglas de concordancia de 'cuyo'",
                "rows": [
                    ["Masculino singular", "'Un gobernante maya cuyo legado perdura en la piedra'"],
                    ["Femenino singular", "'Una cuenca trinacional cuya biodiversidad marina es excepcional'"],
                    ["Masculino plural", "'Monumentos ceremoniales cuyos relieves asombran a los arqueólogos'"],
                    ["Femenino plural", "'Comunidades pesqueras cuyas tradiciones se remontan a siglos'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la historia regional",
                "items": [
                    {"spanish": "El templo de Copán, cuya escalinata jeroglífica contiene el texto maya más extenso del mundo, es Patrimonio de la Humanidad.", "english": "The temple of Copán, whose hieroglyphic stairway contains the most extensive Mayan text in the world, is a World Heritage site."},
                    {"spanish": "El Golfo de Fonseca es un estuario trinacional cuyos recursos pesqueros son compartidos por El Salvador, Honduras y Nicaragua.", "english": "The Gulf of Fonseca is a trinational estuary whose fishing resources are shared by El Salvador, Honduras, and Nicaragua."},
                    {"spanish": "Los monarcas dinásticos, cuyas tumbas reales fueron descubiertas intactas, gobernaron el valle durante cuatro siglos.", "english": "The dynastic monarchs, whose royal tombs were discovered intact, ruled the valley for four centuries."}
                ]
            },
            {
                "type": "tip",
                "content": "¡Error común a evitar!: Nunca combines 'cuyo' con artículo definido ('*el cuyo*', '*la cuya*') ni uses 'que su' en prosa formal ('*un rey que su tumba...*'). Emplea únicamente 'cuyo'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l1}.json", {
        "id": f"story.b2.{l1}",
        "title": "La piedra parlante: Copán y el espejo del Golfo de Fonseca",
        "level": "B2",
        "author": "Arqueología y Geopolítica Centroamericana",
        "summary": "Un viaje por el valle de Copán en el occidente de Honduras, la maestría escultórica de sus estelas mayas y el ecosistema compartido del Golfo de Fonseca.",
        "vocabularyTopics": ["Arqueología de Copán", "Escultura maya clásica", "Ecosistemas del Golfo de Fonseca"],
        "grammar": ["relativo posesivo cuyo", "concordancia de género y número"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el extremo occidental de Honduras, casi en el linde fronterizo con Guatemala, floreció la ciudad de Copán, a menudo llamada la Atenas del mundo maya. A diferencia de las figuras planas de otras metrópolis de las tierras bajas, los escultores copanecos labraron estelas de toba volcánica en altorrelieve casi tridimensional, inmortalizando los rostros y tocados ceremoniales de la dinastía iniciada por K'inich Yax K'uk' Mo'."
            },
            {
                "type": "narration",
                "text": "La joya suprema del sitio es la majestuosa Escalinata Jeroglífica, cuyos sesenta y tres peldaños conservan más de dos mil glifos tallados en piedra, constituyendo el documento epigráfico continuo más extenso de la América precolombina. Cada escalón narra las victorias militares, alianzas dinásticas y ceremonias astronómicas de los reyes que gobernaron el valle de Copán."
            },
            {
                "type": "narration",
                "text": "Hacia el sur, donde convergen las costas de Honduras, El Salvador y Nicaragua, se abre el imponente Golfo de Fonseca. Este estuario de manglares y aguas calmas, cuyas ensenadas albergan a miles de aves migratorias y pescadores artesanales, simboliza la necesidad ineludible de una integración ecológica y diplomática trinacional para salvaguardar el futuro común de la región."
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
                    ["la estela", "stela, carved stone slab"],
                    ["el bajorrelieve", "low relief, bas-relief"],
                    ["el manglar", "mangrove swamp"],
                    ["la escalinata jeroglífica", "hieroglyphic stairway"]
                ],
                "teaches": ["b2-salvadorhonduras-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Con qué elemento concuerda en género y número el relativo 'cuyo'?",
                "options": [
                    "Con el sustantivo que le sigue inmediatamente (la cosa poseída).",
                    "Con el antecedente anterior (el poseedor).",
                    "Permanece siempre invariable en masculino singular."
                ],
                "correct": 0,
                "teaches": ["relativos-posesivos-cuyo"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Copán es una urbe arqueológica __ estelas son admiradas por su relieve tridimensional. (cuyo - feminine plural)",
                "answer": "cuyas",
                "english": "Copán is an archaeological city whose stelae are admired for their three-dimensional relief.",
                "teaches": ["relativos-posesivos-cuyo"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Visitamos", "el", "golfo", "cuyos", "manglares", "protegen", "la", "costa."],
                "solution": ["Visitamos", "el", "golfo", "cuyos", "manglares", "protegen", "la", "costa."],
                "english": "We visited the gulf whose mangroves protect the coast.",
                "teaches": ["relativos-posesivos-cuyo"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Epigrafista", "text": "¿Por qué es tan singular la Escalinata Jeroglífica de Copán?"},
                    {"speaker": "Arqueóloga", "text": "_____"},
                    {"speaker": "Epigrafista", "text": "Es una enciclopedia histórica grabada para la eternidad."}
                ],
                "options": [
                    "Porque es un monumento único cuyos peldaños contienen el texto dinástico maya más largo conservado en Mesoamérica.",
                    "Porque los trenes bananeros transportaban fruta hacia Puerto Cortés.",
                    "Porque la moneda nacional de Honduras es el lempira."
                ],
                "correct": 0,
                "teaches": ["relativos-posesivos-cuyo"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El golfo de Fonseca es un espacio trinacional cuyas costas exigen una gestión ambiental compartida.",
                "english": "The Gulf of Fonseca is a trinational space whose coasts demand shared environmental management.",
                "teaches": ["relativos-posesivos-cuyo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=5,
        title="Copán y el Golfo de Fonseca: Arqueología y cuencas compartidas",
        goal="Examine Copán's Mayan sculpture, epigraphy, and the shared trinational waters of the Gulf of Fonseca using the relative possessive pronoun 'cuyo'.",
        grammar_desc="el pronombre relativo posesivo cuyo/a/os/as en descripciones formales",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Analyze the artistic and epigraphic uniqueness of Copán's Hieroglyphic Stairway and stelae.",
            "Understand the geopolitical and ecological significance of the trinational Gulf of Fonseca.",
            "Master possessive relative agreement with 'cuyo' based on the following possessed noun."
        ],
        story_ref=f"stories/world/b2/{l1}.json",
        intro_body=[
            "Welcome to Unit 5 of Latin American Regional Studies: El Salvador & Honduras: Copán, Memory, Migration & Resilience.",
            "In this opening lesson, we explore the extraordinary sculpture and hieroglyphs of ancient Copán in Honduras and the shared Pacific estuary of the Gulf of Fonseca, mastering the relative possessive 'cuyo'."
        ],
        intro_title="Unit 5: El Salvador & Honduras: Copán, Memory, Migration & Resilience"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-salvadorhonduras-02 - Enclaves bananeros, cultura garífuna y Berta Cáceres
    # --------------------------------------------------------------------------
    l2 = "b2-salvadorhonduras-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.salvadorhonduras.02",
        "lesson": l2,
        "title": "Extractivismo y defensa del territorio",
        "theme": "Enclaves bananeros, costa garífuna y resistencia lenca",
        "words": [
            {"lemma": "el enclave", "translation": "enclave (economic concession)", "pos": "noun"},
            {"lemma": "el monocultivo", "translation": "monoculture", "pos": "noun"},
            {"lemma": "la concesión", "translation": "concession, franchise", "pos": "noun"},
            {"lemma": "la lideresa", "translation": "female leader, activist", "pos": "noun"},
            {"lemma": "el despojo", "translation": "dispossession, dispossession of land", "pos": "noun"},
            {"lemma": "el resguardo territorial", "translation": "territorial protection/title", "pos": "noun"},
            {"lemma": "la hidroeléctrica", "translation": "hydroelectric dam/plant", "pos": "noun"},
            {"lemma": "ancestral", "translation": "ancestral", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.salvadorhonduras.02.verbos-atribucion-denuncia",
        "title": "Verbos de atribución y reporte en la denuncia social y ambiental",
        "sections": [
            {
                "type": "text",
                "title": "Precisión léxica en la documentación de derechos colectivos",
                "content": "En el periodismo de investigación, la sociología crítica y los informes de derechos humanos de nivel B2, el uso genérico de 'decir' resulta insuficiente. Se emplean verbos de atribución de mayor fuerza pragmática y compromiso testimonial: 'denunciar que', 'reclamar que', 'advertir de que', 'constatar que', 'puntualizar que'. Estos verbos seleccionan indicativo cuando constatan un hecho o aseveran una infracción consumada ('Denunciaron que las corporaciones habían contaminado el río'), o subjuntivo cuando expresan demandas, reclamos o advertencias preventivas ('Reclaman que se respeten los convenios territoriales')."
            },
            {
                "type": "table",
                "title": "Clasificación de verbos de denuncia y reporte",
                "rows": [
                    ["Denuncia de hechos fácticos -> INDICATIVO", "'Constatar que / Denunciar que': 'La fiscalía constató que se talaron hectáreas protegidas'"],
                    ["Exigencia de restitución o amparo -> SUBJUNTIVO", "'Exigir que / Reclamar que': 'Las comunidades lencas reclaman que el gobierno cancele la presa'"],
                    ["Advertencia de riesgo futuro -> INDICATIVO o SUBJUNTIVO", "'Advertir de que ocurrirá un desastre' (certeza) vs 'Advertir de que no se cometan abusos' (mandato preventivo)"],
                    ["Puntualización analítica -> INDICATIVO", "'Puntualizar que / Señalar que': 'La defensora puntualizó que la consulta previa era obligatoria'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la lucha ecoterritorial de Honduras",
                "items": [
                    {"spanish": "Berta Cáceres denunció en foros internacionales que el proyecto hidroeléctrico violaba los derechos del pueblo lenca.", "english": "Berta Cáceres denounced in international forums that the hydroelectric project violated the rights of the Lenca people."},
                    {"spanish": "Las organizaciones garífunas reclaman que el Estado reconozca sus títulos de propiedad ancestral sobre la costa caribeña.", "english": "Garifuna organizations demand that the State recognize their ancestral property titles over the Caribbean coast."},
                    {"spanish": "Los ambientalistas advirtieron de que la deforestación aceleraría la sedimentación de las cuencas fluviales.", "english": "Environmentalists warned that deforestation would accelerate river basin sedimentation."}
                ]
            },
            {
                "type": "tip",
                "content": "Atención al régimen preposicional: 'advertir de que' lleva preposición 'de' cuando significa prevenir de un peligro ('Advirtió de que era peligroso'); omitirla incurre en queísmo en la norma culta."
            }
        ]
    })

    write_json(f"stories/world/b2/{l2}.json", {
        "id": f"story.b2.{l2}",
        "title": "Los espíritus del río Gualcarque: Berta Cáceres y la dignidad lenca",
        "level": "B2",
        "author": "Movimientos Ecosociales e Historia de Honduras",
        "summary": "La memoria histórica de las repúblicas bananeras en la costa norte hondureña, la presencia viva del pueblo afroindígena garífuna y el martirio de la ecologista Berta Cáceres en defensa de los ríos sagrados.",
        "vocabularyTopics": ["Enclaves fruteros", "Pueblo garífuna", "Ecologismo y derechos indígenas"],
        "grammar": ["verbos de atribución y denuncia", "advertir de que"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A principios del siglo veinte, las corporaciones fruteras transnacionales transformaron la costa norte de Honduras en un arquetípico enclave bananero. Mediante generosas concesiones fiscales y control ferroviario, la United Fruit Company y la Standard Fruit Company moldearon la política interna del país, dando origen al infame término 'república bananera', mientras miles de trabajadores lencas, mestizos y garífunas soportaban condiciones de explotación extrema en las plantaciones."
            },
            {
                "type": "narration",
                "text": "En ese mismo litoral caribeño pervive la cultura garífuna, una comunidad afroindígena declarada Obra Maestra del Patrimonio Oral e Intangible de la Humanidad por su música de tambores, su lengua y su modelo comunal de subsistencia marina. Hoy en día, sus líderes denuncian que megaproyectos turísticos y plantaciones de palma africana amenazan con despojarlos de sus territorios ancestrales."
            },
            {
                "type": "narration",
                "text": "En el interior montañoso de Intibucá, la lideresa lenca Berta Cáceres encarnó la lucha más valiente en defensa de los bienes comunes. Al frente del COPINH, Cáceres movilizó a su pueblo para frenar la represa hidroeléctrica de Agua Zarca en el río sagrado Gualcarque. A pesar de haber recibido el prestigioso Premio Goldman en 2015, fue asesinada en 2016 por sicarios vinculados a intereses empresariales, convirtiéndose en un símbolo imperecedero de dignidad ecofeminista planetaria."
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
                    ["el enclave", "enclave (economic concession)"],
                    ["el monocultivo", "monoculture"],
                    ["la lideresa", "female leader, activist"],
                    ["el despojo", "dispossession of land"]
                ],
                "teaches": ["b2-salvadorhonduras-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué régimen verbal rige el verbo 'reclamar que' cuando introduce una demanda o exigencia colectiva?",
                "options": [
                    "Modo subjuntivo, porque manifiesta voluntad, aspiración e influencia sobre la conducta institucional.",
                    "Modo indicativo, porque constata un dato financiero del pasado.",
                    "Modo gerundio, porque describe una acción en progreso continuo."
                ],
                "correct": 0,
                "teaches": ["verbos-atribucion-denuncia"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las comunidades lencas reclaman que el Estado __ la consulta previa e informada. (garantizar)",
                "answer": "garantice",
                "english": "Lenca communities demand that the State guarantee prior and informed consultation.",
                "teaches": ["verbos-atribucion-denuncia"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Berta", "Cáceres", "advirtió", "de", "que", "el", "río", "estaba", "amenazado."],
                "solution": ["Berta", "Cáceres", "advirtió", "de", "que", "el", "río", "estaba", "amenazado."],
                "english": "Berta Cáceres warned that the river was threatened.",
                "teaches": ["verbos-atribucion-denuncia"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Relator especial", "text": "¿Cuáles son las principales demandas de las organizaciones garífunas en la corte interamericana?"},
                    {"speaker": "Abogada ambiental", "text": "_____"},
                    {"speaker": "Relator especial", "text": "El cumplimiento de esas sentencias es imperativo para evitar nuevos desplazamientos."}
                ],
                "options": [
                    "Denuncian que las concesiones turísticas violan sus títulos ancestrales y reclaman que se restituyan sus tierras comunales.",
                    "El café de Copán Ruinas se procesa en húmedo durante el invierno.",
                    "Los vuelos chárter llegan al aeropuerto de Roatán los sábados por la tarde."
                ],
                "correct": 0,
                "teaches": ["verbos-atribucion-denuncia"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La activista denunció que los megaproyectos extractivos provocaban el despojo sistemático de los ríos comunitarios.",
                "english": "The activist denounced that extractive megaprojects caused the systematic dispossession of community rivers.",
                "teaches": ["verbos-atribucion-denuncia"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=5,
        title="Enclaves bananeros, cultura garífuna y Berta Cáceres",
        goal="Analyze economic enclaves, Garifuna coastal sovereignty, and the environmental defense of Berta Cáceres using reporting verbs of denunciation.",
        grammar_desc="verbos de atribución, reporte y demanda en la denuncia social y de derechos humanos",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Understand the historical legacy of fruit company enclaves in Northern Honduras.",
            "Explore Garifuna intangible cultural heritage and ancestral coastal land defense.",
            "Deploy powerful attribution verbs (denunciar, advertir de que, reclamar que) in socio-environmental critique."
        ],
        story_ref=f"stories/world/b2/{l2}.json",
        intro_body=[
            "In Lesson 2, we explore Honduras's northern coast and interior mountains: from the banana enclaves of the twentieth century to the vibrant cultural world of the Afro-indigenous Garifuna.",
            "We examine the martyrdom of Goldman Prize winner Berta Cáceres and master advanced reporting verbs of denunciation and advocacy ('denunciar que', 'reclamar que', 'advertir de que')."
        ],
        intro_title="Banana Enclaves, Garifuna Culture & Environmental Resistance"
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-salvadorhonduras-03 - Monseñor Romero, teología de la liberación y paz
    # --------------------------------------------------------------------------
    l3 = "b2-salvadorhonduras-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.salvadorhonduras.03",
        "lesson": l3,
        "title": "Doctrina social, martirio y pacificación",
        "theme": "Monseñor Óscar Arnulfo Romero, guerra civil salvadoreña y Acuerdos de Chapultepec",
        "words": [
            {"lemma": "la homilía", "translation": "homily, sermon", "pos": "noun"},
            {"lemma": "el mártir", "translation": "martyr", "pos": "noun"},
            {"lemma": "la pastoral", "translation": "pastoral work/ministry", "pos": "noun"},
            {"lemma": "el cese al fuego", "translation": "ceasefire", "pos": "noun"},
            {"lemma": "la reconciliación", "translation": "reconciliation", "pos": "noun"},
            {"lemma": "la represión", "translation": "repression, crackdown", "pos": "noun"},
            {"lemma": "la impunidad", "translation": "impunity", "pos": "noun"},
            {"lemma": "la tregua", "translation": "truce", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.salvadorhonduras.03.conectores-contraste-discursivo",
        "title": "Conectores discursivos de contraste y oposición: no obstante, en cambio y por el contrario",
        "sections": [
            {
                "type": "text",
                "title": "Articulación de polaridades en el discurso histórico",
                "content": "Para estructurar un análisis histórico equilibrado en nivel B2, los conectores discursivos parentéticos de contraargumentación y oposición permiten contraponer realidades antagónicas. 'En cambio' y 'por el contrario' señalan una antítesis radical entre dos términos, mientras que 'no obstante' y 'sin embargo' introducen una objeción restrictiva sin anular la proposición previa. Todos ellos se aíslan habitualmente entre comas o tras punto y coma: 'La oligarquía militar apostó por la intensificación represiva; Monseñor Romero, por el contrario, abrazó la defensa incondicional de los oprimidos'."
            },
            {
                "type": "table",
                "title": "Matices y posición de los conectores de contraste",
                "rows": [
                    ["Por el contrario / Por contra", "Oposición total y excluyente: 'El gobierno negó el diálogo; por el contrario, desató una ofensiva'"],
                    ["En cambio", "Contraste distributivo entre dos sujetos o situaciones: 'Las ciudades contaban con servicios; en cambio, el campo vivía en la indigencia'"],
                    ["No obstante / Sin embargo", "Concesión restrictiva (a pesar de lo anterior): 'El arzobispo sabía que su vida corría peligro; no obstante, no claudicó'"],
                    ["Mientras que / En tanto que", "Nexos subordinantes continuos: 'Un sector exigía la guerra, mientras que la iglesia mediaba por la paz'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la historia de El Salvador",
                "items": [
                    {"spanish": "El régimen intentó acallar la voz de la Iglesia; no obstante, las homilías dominicales de Monseñor Romero eran transmitidas clandestinamente por radio a todo el territorio.", "english": "The regime tried to silence the voice of the Church; nevertheless, Archbishop Romero's Sunday homilies were clandestinely broadcast by radio to the entire territory."},
                    {"spanish": "La violencia armada desangró al país durante doce años; en cambio, la firma de los Acuerdos de Chapultepec en 1992 sentó las bases institucionales para la transición democrática.", "english": "Armed violence bled the country for twelve years; on the other hand, the signing of the Chapultepec Accords in 1992 laid the institutional foundations for democratic transition."},
                    {"spanish": "Muchos creían que la pacificación era imposible; por el contrario, la mediación de las Naciones Unidas facilitó el cese al fuego definitivo.", "english": "Many believed that pacification was impossible; on the contrary, United Nations mediation facilitated the definitive ceasefire."}
                ]
            },
            {
                "type": "tip",
                "content": "Puntuación rigurosa: 'no obstante', 'por el contrario' y 'en cambio' van precedidos de punto y coma o punto y seguidos inmediatamente de coma cuando conectan dos oraciones independientes."
            }
        ]
    })

    write_json(f"stories/world/b2/{l3}.json", {
        "id": f"story.b2.{l3}",
        "title": "La voz de los sin voz: Monseñor Romero y la esperanza salvadoreña",
        "level": "B2",
        "author": "Historia y Memoria Salvadoreña",
        "summary": "La trayectoria de San Óscar Arnulfo Romero, su opción profética por los campesinos descalzos frente a la represión estatal, y el camino hacia los Acuerdos de Paz de 1992.",
        "vocabularyTopics": ["Guerra civil salvadoreña", "Teología de la liberación", "Paz de Chapultepec"],
        "grammar": ["conectores de contraste discursivo", "no obstante, por el contrario, en cambio"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Nombrado arzobispo de San Salvador en 1977 como un clérigo considerado conservador y moderado, Monseñor Óscar Arnulfo Romero experimentó una profunda conversión pastoral tras el asesinato de su entrañable amigo, el sacerdote jesuita Rutilio Grande, acribillado por escuadrones de la muerte tras organizar comunidades campesinas en Aguilares."
            },
            {
                "type": "narration",
                "text": "A partir de ese instante, Romero transformó la catedral metropolitana y la emisora diocesana YSAX en el único refugio para los perseguidos. Cada domingo, millones de salvadoreños sintonizaban sus homilías, donde el arzobispo leía con rigor forense los nombres de los desaparecidos y exigía el fin de las torturas. El poder militar esperaba su sumisión; por el contrario, Romero proclamó valientemente: 'Les suplico, les ruego, les ordeno en nombre de Dios: ¡cese la represión!'."
            },
            {
                "type": "narration",
                "text": "El 24 de marzo de 1980, un francotirador le disparó al corazón mientras celebraba la eucaristía en la capilla del hospital de la Divina Providencia. Su martirio desató una sangrienta guerra civil de doce años que costó más de setenta y cinco mil vidas; no obstante, el anhelo de reconciliación sembrado por Romero culminó en 1992 con los Acuerdos de Paz de Chapultepec, consolidando su canonización universal como San Óscar Romero, la voz inmortal de los sin voz."
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
                    ["la homilía", "homily, sermon"],
                    ["el mártir", "martyr"],
                    ["el cese al fuego", "ceasefire"],
                    ["la reconciliación", "reconciliation"]
                ],
                "teaches": ["b2-salvadorhonduras-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la función semántica del conector 'por el contrario' en el discurso formal?",
                "options": [
                    "Introducir una afirmación radicalmente opuesta que sustituye o contradice lo previamente negado.",
                    "Indicar una causa temporal consecutiva equivalente a 'por lo tanto'.",
                    "Añadir información complementaria sin modificar el sentido previo."
                ],
                "correct": 0,
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Monseñor Romero sabía que lo amenazaban de muerte; __ obstante, continuó denunciando los abusos en sus homilías. (conector concesivo restrictivo)",
                "answer": "no",
                "english": "Archbishop Romero knew he was threatened with death; nevertheless, he continued denouncing abuses in his homilies.",
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "régimen", "buscaba", "el", "silencio;", "Romero,", "por", "el", "contrario,", "habló."],
                "solution": ["El", "régimen", "buscaba", "el", "silencio;", "Romero,", "por", "el", "contrario,", "habló."],
                "english": "The regime sought silence; Romero, on the contrary, spoke.",
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Cómo influyó el mensaje de Monseñor Romero en el desenlace del conflicto civil salvadoreño?"},
                    {"speaker": "Politóloga", "text": "_____"},
                    {"speaker": "Historiador", "text": "Su legado ético fue el pilar moral que hizo posible el pacto de paz."}
                ],
                "options": [
                    "Muchos temían que su asesinato aniquilara la esperanza; no obstante, su martirio fortaleció la conciencia democrática hasta alcanzar los Acuerdos de Chapultepec.",
                    "El puerto de La Unión en el golfo de Fonseca dispone de grúas para contenedores.",
                    "La pupusa tradicional salvadoreña se elabora con masa de maíz o de arroz."
                ],
                "correct": 0,
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La represión pretendía imponer el miedo; por el contrario, las homilías unieron al pueblo en la exigencia de justicia.",
                "english": "Repression intended to impose fear; on the contrary, the homilies united the people in the demand for justice.",
                "teaches": ["conectores-contraste-discursivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=5,
        title="Monseñor Romero, teología de la liberación y paz",
        goal="Examine Archbishop Óscar Romero's prophetic pastoral ministry, the Salvadoran civil war, and the 1992 Chapultepec Peace Accords using contrastive discourse markers.",
        grammar_desc="conectores discursivos de oposición y contraste (no obstante, por el contrario, en cambio)",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Trace the historical evolution of liberation theology and Romero's defense of human rights in El Salvador.",
            "Analyze the causes and negotiation trajectory leading to the 1992 Chapultepec Peace Accords.",
            "Master parenthetical discourse connectors of opposition ('en cambio', 'por el contrario', 'no obstante')."
        ],
        story_ref=f"stories/world/b2/{l3}.json",
        intro_body=[
            "In this third lesson, we turn to El Salvador and the towering figure of Saint Óscar Romero, 'the voice of the voiceless'.",
            "We examine the social roots of the Salvadoran civil war, the path to peace at Chapultepec, and the use of sophisticated contrastive discourse markers in historical argumentation."
        ],
        intro_title="Óscar Romero, Liberation Theology & the Path to Peace"
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-salvadorhonduras-04 - El Triángulo Norte: Migración, remesas y desarraigo
    # --------------------------------------------------------------------------
    l4 = "b2-salvadorhonduras-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.salvadorhonduras.04",
        "lesson": l4,
        "title": "Dinámicas migratorias y economía familiar",
        "theme": "Remesas, éxodo centroamericano y familias transnacionales",
        "words": [
            {"lemma": "la remesa", "translation": "remittance", "pos": "noun"},
            {"lemma": "el desarraigo", "translation": "rootlessness, uprooting", "pos": "noun"},
            {"lemma": "el éxodo", "translation": "exodus", "pos": "noun"},
            {"lemma": "el sustento", "translation": "livelihood, sustenance", "pos": "noun"},
            {"lemma": "la reunificación familiar", "translation": "family reunification", "pos": "noun"},
            {"lemma": "el corredor migratorio", "translation": "migration corridor", "pos": "noun"},
            {"lemma": "la precariedad", "translation": "precariousness, fragility", "pos": "noun"},
            {"lemma": "la repatriación", "translation": "repatriation, deportation return", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.salvadorhonduras.04.conectores-causales-complejos",
        "title": "Construcciones causales complejas: debido a que, en vista de que y a causa de",
        "sections": [
            {
                "type": "text",
                "title": "Causalidad sociológica y rigor analítico",
                "content": "En los estudios demográficos y ensayos económicos de nivel B2, el conector básico 'porque' se sustituye por fórmulas causales de mayor precisión formal. Las locuciones preposicionales seguidas de sustantivo ('a causa de', 'debido a', 'por motivo de') identifican causas directas. Por su parte, las conjunciones subordinadas 'debido a que', 'en vista de que', 'dado que' y 'toda vez que' introducen cláusulas oracionales completas en modo indicativo cuando la causa se plantea como un hecho factual comprobado: 'En vista de que el empleo formal es escaso, las familias dependen vitalmente de las remesas'."
            },
            {
                "type": "table",
                "title": "Estructuras causales formales",
                "rows": [
                    ["debido a / a causa de + SUSTANTIVO", "'A causa de la sequía recurrente en el Corredor Seco...'"],
                    ["debido a que + INDICATIVO", "'Muchos jóvenes emigran debido a que las oportunidades locales son limitadas'"],
                    ["en vista de que + INDICATIVO", "'En vista de que las remesas representan el 25% del PIB, sostienen el consumo interno'"],
                    ["toda vez que + INDICATIVO (registro jurídico/formal)", "'El estado debe intervenir toda vez que los derechos de la infancia están desprotegidos'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el fenómeno migratorio regional",
                "items": [
                    {"spanish": "Debido a que el cambio climático arruinó las cosechas de subsistencia, miles de campesinos se unieron a las caravanas.", "english": "Because climate change ruined subsistence harvests, thousands of small farmers joined the caravans."},
                    {"spanish": "En vista de que las transferencias financieras sostienen la canasta básica, la economía salvadoreña es fuertemente transnacional.", "english": "Given that financial transfers sustain the basic food basket, the Salvadoran economy is heavily transnational."},
                    {"spanish": "A causa del desarraigo prolongado, muchos niños crecen bajo el cuidado de sus abuelos en comunidades rurales.", "english": "On account of prolonged separation, many children grow up under their grandparents' care in rural communities."}
                ]
            },
            {
                "type": "tip",
                "content": "Evita la incorrección '*debido a que + infinitivo*' o la fórmula vulgar '*a cuenta de que*'. Utiliza 'debido a que + verbo conjugado' o 'debido a + sintagma nominal'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l4}.json", {
        "id": f"story.b2.{l4}",
        "title": "El hilo invisible: Remesas, ausencia y lazos transnacionales",
        "level": "B2",
        "author": "Sociología de la Migración Centroamericana",
        "summary": "Una mirada a la realidad humana del Triángulo Norte: el viaje por la ruta migratoria, el peso macroeconómico de las remesas familiares y el costo afectivo del desarraigo.",
        "vocabularyTopics": ["Migración centroamericana", "Economía de remesas", "Familias transnacionales"],
        "grammar": ["causales complejas con debido a que y en vista de que", "léxico de sociología migratoria"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A lo largo de las últimas cuatro décadas, Honduras y El Salvador han conformado uno de los corredores migratorios más transitados del hemisferio occidental. Impulsados por la falta de empleo formal, la extorsión de pandillas y los efectos del cambio climático sobre el Corredor Seco centroamericano, cientos de miles de hombres y mujeres emprendieron el peligroso periplo rumbo al norte."
            },
            {
                "type": "narration",
                "text": "En vista de que las remesas familiares superan en conjunto la cuarta parte del Producto Interno Bruto de ambos países, estas divisas constituyen la verdadera red de seguridad social para millones de hogares. Con ese dinero enviado dólar a dólar desde Los Ángeles, Houston o Washington D.C., las familias rurales costean la alimentación diaria, sufragan estudios universitarios y levantan viviendas de cemento en aldeas remotas."
            },
            {
                "type": "narration",
                "text": "No obstante, detrás de los indicadores macroeconómicos se oculta el costo humano del desarraigo. Generaciones enteras de niños han crecido al amparo de abuelas abnegadas, manteniendo el afecto materno y paterno a través de videollamadas nocturnas por teléfono celular, demostrando que la identidad salvadoreña y hondureña es hoy una patria extendida y transnacional sin fronteras fijas."
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
                    ["la remesa", "remittance"],
                    ["el desarraigo", "rootlessness, uprooting"],
                    ["el sustento", "livelihood, sustenance"],
                    ["la precariedad", "fragility, precariousness"]
                ],
                "teaches": ["b2-salvadorhonduras-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo verbal introduce la locución causal 'en vista de que' cuando presenta un hecho comprobado?",
                "options": [
                    "Modo indicativo, porque introduce la causa real y verificada de una situación.",
                    "Modo subjuntivo, porque todas las subordinadas causales rechazan el indicativo.",
                    "Modo imperativo, porque exhorta a tomar una decisión política."
                ],
                "correct": 0,
                "teaches": ["conectores-causales-complejos"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Debido a que las sequías __ las milpas, los agricultores se vieron forzados a emigrar. (arruinar - pretérito indefinido)",
                "answer": "arruinaron",
                "english": "Because droughts ruined the cornfields, the farmers were forced to emigrate.",
                "teaches": ["conectores-causales-complejos"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["En", "vista", "de", "que", "faltaba", "empleo,", "buscaron", "nuevas", "oportunidades."],
                "solution": ["En", "vista", "de", "que", "faltaba", "empleo,", "buscaron", "nuevas", "oportunidades."],
                "english": "In view of the fact that jobs were lacking, they sought new opportunities.",
                "teaches": ["conectores-causales-complejos"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Economista", "text": "¿Qué papel cumplen las remesas familiares en la estabilidad económica centroamericana?"},
                    {"speaker": "Socióloga", "text": "_____"},
                    {"speaker": "Economista", "text": "Es un motor indispensable, pero evidencia la fragilidad productiva interna."}
                ],
                "options": [
                    "En vista de que representan un porcentaje decisivo del PIB, amortiguan la pobreza extrema y sostienen el consumo familiar.",
                    "Las playas salvadoreñas atraen a surfistas profesionales durante la temporada estival.",
                    "El lempira hondureño lleva el nombre de un célebre cacique de la resistencia indígena."
                ],
                "correct": 0,
                "teaches": ["conectores-causales-complejos"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "A causa del desarraigo forzado, millones de familias mantienen el vínculo afectivo a la distancia.",
                "english": "On account of forced uprooting, millions of families maintain affective bonds across distance.",
                "teaches": ["conectores-causales-complejos"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=5,
        title="El Triángulo Norte: Migración, remesas y desarraigo",
        goal="Analyze demographic corridors, remittances, and transnational families in El Salvador and Honduras using complex causal constructions.",
        grammar_desc="construcciones causales complejas ('debido a que', 'en vista de que', 'a causa de') en el análisis sociológico",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Examine the root economic and climate drivers of Northern Triangle migration.",
            "Assess the macroeconomic weight and emotional costs of family remittances.",
            "Deploy sophisticated causal conjunctions ('debido a que', 'en vista de que') in analytical writing."
        ],
        story_ref=f"stories/world/b2/{l4}.json",
        intro_body=[
            "Lesson 4 tackles one of the central sociological realities shaping Central America today: the migratory phenomenon across the Northern Triangle.",
            "We analyze remittances, transnational family bonds, and the socio-economic causes of uprooting, focusing on complex causal syntax ('debido a que', 'en vista de que', 'a causa de')."
        ],
        intro_title="The Northern Triangle: Migration, Remittances & Uprooting"
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-salvadorhonduras-05 - Seguridad, democracia y juventud: Debates contemporáneos
    # --------------------------------------------------------------------------
    l5 = "b2-salvadorhonduras-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.salvadorhonduras.05",
        "lesson": l5,
        "title": "Sociedad contemporánea y espacio público",
        "theme": "Seguridad ciudadana, estado de derecho y resistencia comunitaria",
        "words": [
            {"lemma": "el tejido social", "translation": "social fabric", "pos": "noun"},
            {"lemma": "la gobernabilidad", "translation": "governability, state capacity", "pos": "noun"},
            {"lemma": "la pacificación barrial", "translation": "neighborhood pacification", "pos": "noun"},
            {"lemma": "la cohesión comunitaria", "translation": "community cohesion", "pos": "noun"},
            {"lemma": "el estigma", "translation": "stigma", "pos": "noun"},
            {"lemma": "la reinserción", "translation": "reintegration, rehabilitation", "pos": "noun"},
            {"lemma": "la institucionalidad", "translation": "institutional framework/integrity", "pos": "noun"},
            {"lemma": "el espacio público", "translation": "public space", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.salvadorhonduras.05.integracion-analisis-politico",
        "title": "Integración discursiva: Relativos posesivos, contraste discursivo y argumentación causal",
        "sections": [
            {
                "type": "text",
                "title": "Síntesis sintáctica para el ensayo político y sociológico",
                "content": "El debate contemporáneo sobre seguridad, libertades civiles y regeneración social en Centroamérica requiere articular perspectivas múltiples. La combinación de oraciones de relativo posesivo ('cuyo'), conectores de contraste ponderado ('no obstante', 'por el contrario', 'en cambio') y nexos causales ('debido a que', 'en vista de que') permite construir ensayos académicos de alta complejidad conceptual y madurez estilística."
            },
            {
                "type": "examples",
                "title": "Modelos sintácticos integrados",
                "items": [
                    {"spanish": "El Salvador implementó políticas de mano dura cuyas repercusiones suscitan intensos debates sobre los derechos humanos.", "english": "El Salvador implemented heavy-handed policies whose repercussions spark intense debates on human rights."},
                    {"spanish": "Muchos ciudadanos respaldan la reducción de la criminalidad; no obstante, organismos internacionales advierten del debilitamiento institucional.", "english": "Many citizens back crime reduction; nevertheless, international organizations warn of institutional weakening."},
                    {"spanish": "En vista de que la violencia azotó a las comunidades durante décadas, la recuperación del espacio público es celebrada por los jóvenes.", "english": "Given that violence battered communities for decades, the reclaiming of public space is celebrated by youth."}
                ]
            },
            {
                "type": "tip",
                "content": "Para estructurar un párrafo de opinión equilibrado, formula la tesis con 'si bien / en vista de que', matiza el contrapunto con 'no obstante / en cambio' y remata con una cláusula relativa con 'cuyo'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l5}.json", {
        "id": f"story.b2.{l5}",
        "title": "Colores sobre el asfalto: Juventud, arte urbano y reconstrucción comunitaria",
        "level": "B2",
        "author": "Cultura Urbana y Juventud Centroamericana",
        "summary": "Los dilemas de seguridad y libertades ciudadanas en el El Salvador y Honduras actuales, y cómo colectivos juveniles de San Salvador y Tegucigalpa recuperan barrios enteros a través del muralismo, el rap y la autogestión.",
        "vocabularyTopics": ["Políticas de seguridad", "Muralismo y cultura urbana", "Tejido comunitario"],
        "grammar": ["relativo cuyo", "conectores de contraste", "causales complejas"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En los últimos años, El Salvador y Honduras han ocupado el centro de la atención internacional por sus modelos contrapuestos de gestión de la seguridad ciudadana. En El Salvador, la implementación del régimen de excepción y el encarcelamiento masivo lograron desplomar drásticamente los homicidios, permitiendo que comunidades históricamente sitiadas volvieran a caminar de noche; no obstante, analistas constitucionales y defensores de libertades civiles advierten sobre el riesgo de socavar el debido proceso y la división de poderes."
            },
            {
                "type": "narration",
                "text": "Frente a los enfoques meramente punitivos, en barrios populares de San Salvador como Soyapango y en colonias de Tegucigalpa como El Carrizal, colectivos de jóvenes artistas demuestran que la auténtica pacificación pasa por sanar el tejido social. Mediante talleres de hip-hop, escuelas de patinaje y huertos urbanos, estas iniciativas arrebatan a la juventud del estigma de la marginación."
            },
            {
                "type": "narration",
                "text": "Las fachadas antes marcadas con símbolos delictivos lucen hoy monumentales murales de colores vivos, cuyas pinturas homenajean a mujeres tejedoras, volcanes y niños sonrientes. En vista de que la paz verdadera no puede depender indefinidamente de soldados en las esquinas, las comunidades centroamericanas apuestan por la educación, el arte y la solidaridad como los únicos cimientos sostenibles de su porvenir."
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
                    ["el tejido social", "social fabric"],
                    ["la gobernabilidad", "governability"],
                    ["el estigma", "stigma"],
                    ["la cohesión comunitaria", "community cohesion"]
                ],
                "teaches": ["b2-salvadorhonduras-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué conector de contraste se adapta mejor para introducir un contrapunto formal tras punto y coma?",
                "options": [
                    "no obstante,",
                    "porque,",
                    "así que,"
                ],
                "correct": 0,
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los colectivos de jóvenes pintaron murales __ colores devuelven la vida a los callejones del barrio. (cuyo - masculine plural)",
                "answer": "cuyos",
                "english": "Youth collectives painted murals whose colors bring life back to neighborhood alleys.",
                "teaches": ["relativos-posesivos-cuyo"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["En", "vista", "de", "que", "hubo", "paz,", "los", "vecinos", "salieron."],
                "solution": ["En", "vista", "de", "que", "hubo", "paz,", "los", "vecinos", "salieron."],
                "english": "In view of the fact that there was peace, the neighbors came out.",
                "teaches": ["conectores-causales-complejos"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Cómo se equilibra el éxito en seguridad pública con el fortalecimiento del estado de derecho?"},
                    {"speaker": "Jurista centroamericana", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Sin duda, la sostenibilidad democrática requiere justicia independiente y prevención integral."}
                ],
                "options": [
                    "La reducción de la violencia es innegable; no obstante, una paz duradera exige instituciones transparentes cuyas actuaciones respeten las garantías constitucionales.",
                    "El cultivo del añil o índigo fue la principal exportación salvadoreña en el siglo dieciocho.",
                    "Las pupusas de frijol con queso se sirven con encurtido de repollo fermentado."
                ],
                "correct": 0,
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Debido a que el arte urbano fomenta la cohesión comunitaria, los jóvenes han transformado el espacio público.",
                "english": "Because urban art fosters community cohesion, youth have transformed public space.",
                "teaches": ["conectores-causales-complejos"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=5,
        title="Seguridad, democracia y juventud: Debates contemporáneos",
        goal="Analyze contemporary Central American debates on public security, constitutional governance, and youth urban resilience using integrated syntactic structures.",
        grammar_desc="integración discursiva de pronombres relativos posesivos, contraste y subordinación causal",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Examine contemporary public security policies and constitutional debates in El Salvador and Honduras.",
            "Explore urban youth culture, muralism, and community resilience in San Salvador and Tegucigalpa.",
            "Synthesize possessive relatives ('cuyo'), contrast connectors ('no obstante'), and complex causals in sociopolitical prose."
        ],
        story_ref=f"stories/world/b2/{l5}.json",
        intro_body=[
            "Our final topic lesson in Unit 5 explores the urgent contemporary debates shaping El Salvador and Honduras: public security, rule of law, and youth civic culture.",
            "Through muralism and community arts reclaiming urban neighborhoods, we synthesize all grammatical structures practiced across the unit."
        ],
        intro_title="Security, Democracy & Youth Resilience"
    ))

    # --------------------------------------------------------------------------
    # Lesson 6: b2-salvadorhonduras-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-salvadorhonduras-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la estela", "stela, carved stone slab"],
                    ["la lideresa", "female activist leader"],
                    ["el cese al fuego", "ceasefire"],
                    ["el desarraigo", "rootlessness, uprooting"]
                ],
                "teaches": ["b2-salvadorhonduras-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones utiliza con corrección gramatical el pronombre relativo 'cuyo'?",
                "options": [
                    "Visitamos el valle de Copán, cuyas ruinas mayas son Patrimonio de la Humanidad.",
                    "Visitamos el valle de Copán, el cuyo patrimonio es reconocido por la UNESCO.",
                    "Visitamos el valle de Copán, que sus ruinas son famosas en todo el mundo."
                ],
                "correct": 0,
                "teaches": ["relativos-posesivos-cuyo"]
            },
            {
                "id": f"{lcon if False else l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la puntuación canónica del conector discursivo 'no obstante' cuando enlaza dos oraciones independientes?",
                "options": [
                    "Precedido de punto y coma o punto, y seguido de coma (; no obstante,).",
                    "Entre signos de exclamación (!no obstante!).",
                    "Sin ninguna puntuación antes ni después."
                ],
                "correct": 0,
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En vista de que las remesas __ un tercio del ingreso familiar, la economía depende de la diáspora. (representar)",
                "answer": "representan",
                "english": "Given that remittances represent a third of family income, the economy depends on the diaspora.",
                "teaches": ["conectores-causales-complejos"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Copán es una urbe maya cuyas estelas destacan por su maestría escultórica. [Copán is a Mayan city whose stelae stand out for their sculptural mastery.]",
                    "Berta Cáceres advirtió de que la represa amenazaba el río sagrado del pueblo lenca. [Berta Cáceres warned that the dam threatened the sacred river of the Lenca people.]",
                    "El régimen militar buscó el silencio; Romero, por el contrario, proclamó la verdad. [The military regime sought silence; Romero, on the contrary, proclaimed the truth.]",
                    "Debido a que las condiciones eran difíciles, miles de familias emigraron al norte. [Because conditions were difficult, thousands of families emigrated north.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["relativos-posesivos-cuyo", "verbos-atribucion-denuncia", "conectores-contraste-discursivo", "conectores-causales-complejos"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora", "text": "¿Qué lección fundamental nos dejan las luchas históricas de El Salvador y Honduras?"},
                    {"speaker": "Sociólogo", "text": "_____"},
                    {"speaker": "Historiadora", "text": "Una muestra de entereza moral frente a la adversidad."}
                ],
                "options": [
                    "Que a pesar de las heridas de la violencia y el desarraigo, sus pueblos han sabido tejer redes comunitarias de resistencia, dignidad y esperanza.",
                    "El ferri entre La Unión y Potosí conecta las costas del golfo de Fonseca.",
                    "El lago de Yojoa es el único lago natural de origen volcánico en Honduras."
                ],
                "correct": 0,
                "teaches": ["conectores-contraste-discursivo"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las comunidades garífunas reclaman que se respeten sus títulos ancestrales sobre el litoral caribeño.",
                "english": "Garifuna communities demand that their ancestral titles over the Caribbean coast be respected.",
                "teaches": ["verbos-atribucion-denuncia"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta un enunciado formal combinando el relativo posesivo 'cuyo/a' y el conector causal 'debido a que'.",
                        "answer": "La comunidad lenca, cuya identidad está ligada al río sagrado, resiste debido a que defiende su territorio ancestral."
                    }
                ],
                "teaches": ["relativos-posesivos-cuyo", "conectores-causales-complejos"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=5,
        title="Unit 5 Consolidation: El Salvador & Honduras",
        goal="Consolidate possessive relative 'cuyo', reporting verbs of denunciation, contrastive connectors, and complex causals through the history and culture of El Salvador and Honduras.",
        grammar_desc="síntesis de relativos posesivos, verbos de reporte, conectores de contraste y causales complejas",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Deploy possessive relative 'cuyo' with proper noun agreement in archaeological descriptions.",
            "Use reporting verbs of denunciation (denunciar, advertir de que, reclamar que).",
            "Articulate historical counterpoints with 'no obstante', 'por el contrario', and 'en cambio'.",
            "Explain demographic and economic phenomena using complex causal conjunctions."
        ],
        checklist_items=[
            "I can use 'cuyo/a/os/as' matching the gender and number of the possessed noun.",
            "I can report social demands and environmental claims using verbs of denunciation.",
            "I can structure formal historical contrast using 'no obstante', 'por el contrario', and 'en cambio'.",
            "I can express complex causality using 'debido a que', 'en vista de que', and 'a causa de'."
        ],
        story_ref=f"stories/world/b2/{l5}.json"
    ))
    print("Completed LatAm Unit 5 (El Salvador & Honduras) generation!")


if __name__ == "__main__":
    generate_latam_unit_5()
