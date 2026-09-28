#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Latin America Regional Studies Unit 6:
  - Title: "Nicaragua: Land of Lakes, Volcanoes & Poetry"
    (Nicaragua: Tierra de lagos, volcanes y poesía)
  - Stems: b2-nicaragua-01 through b2-nicaragua-consolidation
  - Cultural Focus: Lake Cocibolca (Ometepe & freshwater sharks),
    Rubén Darío & Modernism (the poetic revolution of Spanish),
    Augusto C. Sandino & national sovereignty,
    1979 Sandinista Revolution & National Literacy Crusade (Solentiname & Ernesto Cardenal),
    Contemporary civil resistance, stripped nationality & the intellectual diaspora.
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_latam_unit_6():
    # Vocab theme slug: b2-nicaragua-vocab
    # Grammar skills:
    #   - consecutivas-de-tal-manera
    #   - recursos-retoricos-poesia
    #   - condicional-contrafactico-pasado
    #   - concesivas-politicas-aun-cuando

    # --------------------------------------------------------------------------
    # Lesson 1: b2-nicaragua-01 - El Gran Lago Cocibolca, Ometepe y los volcanes
    # --------------------------------------------------------------------------
    l1 = "b2-nicaragua-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.nicaragua.01",
        "lesson": l1,
        "title": "Geografía lacustre y vulcanología",
        "theme": "El Lago Cocibolca, isla de Ometepe y vulcanismo activo",
        "words": [
            {"lemma": "la cuenca lacustre", "translation": "lake basin", "pos": "noun"},
            {"lemma": "el oleaje", "translation": "surge, waves, swell", "pos": "noun"},
            {"lemma": "el volcán gemelo", "translation": "twin volcano", "pos": "noun"},
            {"lemma": "el itsmo", "translation": "isthmus", "pos": "noun"},
            {"lemma": "el archipiélago", "translation": "archipelago", "pos": "noun"},
            {"lemma": "la toba volcánica", "translation": "volcanic tuff", "pos": "noun"},
            {"lemma": "el cráter", "translation": "crater", "pos": "noun"},
            {"lemma": "el tiburón de agua dulce", "translation": "freshwater bull shark", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.nicaragua.01.consecutivas-de-tal-manera",
        "title": "Oraciones consecutivas de intensidad y modo: de tal manera que y de modo que",
        "sections": [
            {
                "type": "text",
                "title": "Consecuencia factual frente a consecuencia intencional o hipotética",
                "content": "Las locuciones consecutivas 'de tal manera que', 'de modo que' y 'de forma que' expresan la consecuencia o derivación natural de una acción previa. En el nivel B2, la selección modal es fundamental: rigen INDICATIVO cuando expresan una consecuencia real y efectiva consumada en los hechos ('El viento sopló con furia, de tal manera que las olas inundaron la costa lacustre'); por el contrario, rigen SUBJUNTIVO cuando la consecuencia se proyecta como una finalidad intencional buscada por el sujeto o como una hipótesis futura ('Debemos regular el transporte lacustre de tal manera que no se contamine el acuífero de Ometepe')."
            },
            {
                "type": "table",
                "title": "Selección modal en consecutivas formales",
                "rows": [
                    ["de tal manera que + INDICATIVO", "Efecto real consumado: 'El volcán arrojó cenizas de tal manera que oscureció todo el valle'"],
                    ["de tal manera que + SUBJUNTIVO", "Efecto intencional o meta deseada: 'Diseñaron el dique de tal manera que resista el oleaje lacustre'"],
                    ["tanto / tan... que + INDICATIVO", "Consecutiva de intensidad cuantitativa: 'El lago es tan inmenso que parece un mar interior'"],
                    ["de ahí que + SUBJUNTIVO (siempre)", "Consecuencia explicativa formal: 'El lago alberga tiburones toro; de ahí que sea un ecosistema único'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la geografía nicaragüense",
                "items": [
                    {"spanish": "El lago Cocibolca posee una extensión tan vasta que los cronistas coloniales lo bautizaron como 'la Mar Dulce'.", "english": "Lake Cocibolca possesses such a vast expanse that colonial chroniclers christened it 'the Sweet Sea'."},
                    {"spanish": "Los volcanes Concepción y Maderas emergieron de tal manera que formaron la singular isla de Ometepe en medio del lago.", "english": "The Concepción and Maderas volcanoes emerged in such a way that they formed the unique island of Ometepe in the middle of the lake."},
                    {"spanish": "Es indispensable ordenar las rutas turísticas de modo que no se perturben los santuarios de petroglifos indígenas.", "english": "It is essential to organize tourist routes so that indigenous petroglyph sanctuaries are not disturbed."}
                ]
            },
            {
                "type": "tip",
                "content": "No confundas 'de modo que' ilativo (que equivale a 'por consiguiente' y lleva indicativo) con 'de modo que' final (que equivale a 'para que' y lleva subjuntivo)."
            }
        ]
    })

    write_json(f"stories/world/b2/{l1}.json", {
        "id": f"story.b2.{l1}",
        "title": "La Mar Dulce: Ometepe y los misterios del Cocibolca",
        "level": "B2",
        "author": "Geografía Lacustre y Naturaleza de Nicaragua",
        "summary": "Una travesía por el inmenso Lago Cocibolca, la silueta volcánica perfecta de Ometepe, los tiburones toro de agua dulce y la ciudad colonial de Granada.",
        "vocabularyTopics": ["Geografía del Cocibolca", "Vulcanología de Ometepe", "Ecosistemas lacustres únicos"],
        "grammar": ["consecutivas con de tal manera que", "indicativo vs subjuntivo en consecutivas"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Con más de ocho mil kilómetros cuadrados de superficie, el Gran Lago de Nicaragua —conocido ancestralmente como Cocibolca— es el mayor cuerpo de agua dulce de América Central. Su inmensidad es tan sobrecogedora que genera tempestades y marejadas comparables a las de un océano abierto, razón por la cual los navegantes españoles del siglo dieciséis lo llamaron con asombro 'la Mar Dulce'."
            },
            {
                "type": "narration",
                "text": "En su centro se alza Ometepe, una prodigiosa isla con figura de ocho esculpida por dos colosos volcánicos: el Concepción, un cono activo de simetría imponente, y el Maderas, cubierto por una densa selva nubosa que cobija una laguna de aguas frías en su cráter extinto. Sus laderas volcánicas conservan cientos de petroglifos precolombinos tallados en basalto que atestiguan el culto sagrado de los pueblos nahuas y chorotegas al agua y al fuego."
            },
            {
                "type": "narration",
                "text": "El Cocibolca ostenta además una singularidad biológica fascinante: a través del río San Juan, los tiburones toro del mar Caribe remontaron la corriente a lo largo de los milenios adaptando su fisiología al agua dulce, de tal manera que convirtieron a este lago en uno de los laboratorios evolutivos más asombrosos del planeta."
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
                    ["la cuenca lacustre", "lake basin"],
                    ["el oleaje", "waves, swell"],
                    ["el archipiélago", "archipelago"],
                    ["el tiburón de agua dulce", "freshwater bull shark"]
                ],
                "teaches": ["b2-nicaragua-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo rige la locución 'de tal manera que' cuando expresa una meta o finalidad intencional?",
                "options": [
                    "Modo subjuntivo, porque la consecuencia se proyecta como un objetivo deseado o prospectivo.",
                    "Modo indicativo, porque describe un fenómeno meteorológico comprobado.",
                    "Modo infinitivo, porque carece de agente explícito."
                ],
                "correct": 0,
                "teaches": ["consecutivas-de-tal-manera"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El viento sopló con fuerza en el lago, de tal manera que los pescadores __ buscar refugio en la bahía. (tener - pretérito indefinido)",
                "answer": "tuvieron",
                "english": "The wind blew strongly on the lake, in such a way that the fishermen had to seek shelter in the bay.",
                "teaches": ["consecutivas-de-tal-manera"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "lago", "es", "tan", "vasto", "que", "parece", "un", "mar."],
                "solution": ["El", "lago", "es", "tan", "vasto", "que", "parece", "un", "mar."],
                "english": "The lake is so vast that it seems like a sea.",
                "teaches": ["consecutivas-de-tal-manera"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Bióloga marina", "text": "¿Cómo lograron los tiburones toro habitar el lago de Nicaragua?"},
                    {"speaker": "Guía científico", "text": "_____"},
                    {"speaker": "Bióloga marina", "text": "Un fenómeno de adaptación osmótica extraordinario en el reino animal."}
                ],
                "options": [
                    "Remontaron los rápidos del río San Juan y adaptaron sus órganos de tal manera que toleran perfectamente el agua dulce.",
                    "La ciudad de Granada fue fundada a orillas del lago en 1524.",
                    "Los transbordadores conectan San Jorge con Moyogalpa dos veces al día."
                ],
                "correct": 0,
                "teaches": ["consecutivas-de-tal-manera"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La erupción formó el itsmo de tal manera que unió las dos cumbres volcánicas en una sola isla.",
                "english": "The eruption formed the isthmus in such a way that it joined the two volcanic peaks into a single island.",
                "teaches": ["consecutivas-de-tal-manera"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=6,
        title="El Gran Lago Cocibolca, Ometepe y los volcanes",
        goal="Describe Lake Nicaragua's inland sea ecology, Ometepe volcanic geography, and evolutionary phenomena using consecutive clauses of intensity and manner.",
        grammar_desc="oraciones consecutivas de intensidad y modo con 'de tal manera que', 'de modo que' y 'tanto que'",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Examine Lake Cocibolca's vast freshwater geography and the unique adaptation of bull sharks.",
            "Understand the volcanic formation and indigenous petroglyph heritage of Ometepe island.",
            "Distinguish between factual consecutive indicative and purposive consecutive subjunctive."
        ],
        story_ref=f"stories/world/b2/{l1}.json",
        intro_body=[
            "Welcome to Unit 6 of Latin American Regional Studies: Nicaragua: Land of Lakes, Volcanoes & Poetry. Nicaragua's geography is defined by colossal freshwater bodies and active volcanic alignments.",
            "In this opening lesson, we set sail across Lake Cocibolca (the 'Sweet Sea') and explore the twin volcanoes of Ometepe, mastering consecutive structures of manner and intensity ('de tal manera que')."
        ],
        intro_title="Unit 6: Nicaragua: Land of Lakes, Volcanoes & Poetry"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-nicaragua-02 - Rubén Darío y el Modernismo: La revolución del verso
    # --------------------------------------------------------------------------
    l2 = "b2-nicaragua-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.nicaragua.02",
        "lesson": l2,
        "title": "Poesía y estética modernista",
        "theme": "Rubén Darío, 'Azul...', métrica francesa y la renovación del castellano",
        "words": [
            {"lemma": "el modernismo", "translation": "Modernism (literary movement)", "pos": "noun"},
            {"lemma": "el verso alejandrino", "translation": "Alexandrine verse (14-syllable line)", "pos": "noun"},
            {"lemma": "la sinestesia", "translation": "synesthesia", "pos": "noun"},
            {"lemma": "el cisne", "translation": "swan (emblem of Modernist beauty)", "pos": "noun"},
            {"lemma": "la cadencia", "translation": "cadence, rhythm", "pos": "noun"},
            {"lemma": "el refinamiento", "translation": "refinement, sophistication", "pos": "noun"},
            {"lemma": "la estrofa", "translation": "stanza", "pos": "noun"},
            {"lemma": "la rima consonante", "translation": "consonant rhyme", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.nicaragua.02.recursos-retoricos-poesia",
        "title": "Recursos retóricos y léxico poético en el análisis literario",
        "sections": [
            {
                "type": "text",
                "title": "Figuras estilísticas y metalenguaje poético en nivel B2",
                "content": "El análisis estilístico de la poesía hispanoamericana exige un dominio riguroso de las figuras retóricas y del vocabulario de la preceptiva literaria. El Modernismo dariano renovó la lengua mediante la sinestesia (cruce sensorial: 'sonoro marfil', 'música dorada'), la aliteración eufónica, la recuperación del verso alejandrino de catorce sílabas con cesura central y el empleo de adjetivos cromáticos exóticos. Al comentar poesía en nivel B2, se utilizan verbos como 'evocar', 'sugerir', 'simbolizar', 'plasmar' y 'rimar'."
            },
            {
                "type": "table",
                "title": "Figuras retóricas del Modernismo",
                "rows": [
                    ["Sinestesia", "Fusión de percepciones de sentidos distintos: 'agria penumbra', 'cálido suspiro azul'"],
                    ["Metáfora estética", "Transposición analógica refinada: 'el cisne de níveo plumaje como signo interrogativo'"],
                    ["Verso alejandrino", "Métrica de 14 sílabas dividida en dos hemistiquios de 7 sílabas por una pausa o cesura"],
                    ["Aliteración", "Reiteración fónica musical: 'el ala aleve del leve abanico'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en los versos de Rubén Darío",
                "items": [
                    {"spanish": "Darío evoca la melancolía del otoño mediante sutiles sinestesias que combinan color y perfume.", "english": "Darío evokes autumn melancholy through subtle synesthesias combining color and scent."},
                    {"spanish": "El ritmo musical de los alejandrinos en 'Cantos de vida y esperanza' revolucionó la métrica tradicional en lengua española.", "english": "The musical rhythm of Alexandrines in 'Cantos de vida y esperanza' revolutionized traditional metrics in the Spanish language."},
                    {"spanish": "El cisne simboliza la búsqueda de la belleza pura frente al utilitarismo de la sociedad industrial.", "english": "The swan symbolizes the search for pure beauty in the face of industrial society's utilitarianism."}
                ]
            },
            {
                "type": "tip",
                "content": "Para redactar un comentario literario formal, evita frases coloquiales como 'el poema habla de'. Prefiere fórmulas como 'la estrofa plasma', 'el poeta articula', 'el texto transparenta'."
            }
        ]
    })

    write_json(f"stories/world/b2/{l2}.json", {
        "id": f"story.b2.{l2}",
        "title": "El príncipe de las letras: Rubén Darío y el renacer del idioma",
        "level": "B2",
        "author": "Literatura Hispanoamericana y Poética",
        "summary": "La vida de Félix Rubén García Sarmiento (Rubén Darío), la publicación de 'Azul...' en Valparaíso en 1888 y cómo un joven nicaragüense refundó la música y la métrica de toda la literatura en lengua española.",
        "vocabularyTopics": ["Modernismo literario", "Métrica y figuras retóricas", "Legado de Rubén Darío"],
        "grammar": ["léxico de análisis poético", "sinestesia y metáfora modernista"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Nacido en la humilde aldea de Metapa en 1867, Rubén Darío estaba predestinado a encabezar la transformación estética más trascendental de las letras hispanas. En 1888, con apenas veintiún años y residiendo en Chile, publicó 'Azul...', una colección de cuentos líricos y poemas en prosa cuya deslumbrante plasticidad verbal y musicalidad inauguraron formalmente el Modernismo."
            },
            {
                "type": "narration",
                "text": "Darío liberó al idioma castellano de la rigidez académica y el provincialismo en que había caído tras el Siglo de Oro. Asimilando la lección de los parnasianos y simbolistas franceses como Verlaine y Mallarmé, rescató el viejo verso alejandrino de los cantares de gesta medievales y le infundió una cadencia flexible, repleta de sinestesias y refinamientos sonoros donde el cisne se erigió en el blasón de la belleza inmortal."
            },
            {
                "type": "narration",
                "text": "Con 'Prosas profanas' y más tarde con la madurez reflexiva de 'Cantos de vida y esperanza' (1905), el bardo nicaragüense no solo conquistó a los lectores de América Latina, sino que cruzó el Atlántico para discipular a los propios maestros peninsulares como Antonio Machado y Juan Ramón Jiménez. Por primera vez en la historia de la literatura, una corriente estética nacida en tierras americanas reeducaba poéticamente a su metrópoli original."
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
                    ["el modernismo", "Modernism (literary movement)"],
                    ["el verso alejandrino", "14-syllable verse line"],
                    ["la sinestesia", "synesthesia (sensory fusion)"],
                    ["el cisne", "swan (symbol of pure beauty)"]
                ],
                "teaches": ["b2-nicaragua-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué figura retórica se manifiesta en la célebre expresión modernista 'dulce silencio azul'?",
                "options": [
                    "Sinestesia: combina percepciones del gusto (dulce), del oído (silencio) y de la vista (azul).",
                    "Hipérbole: exagera desmesuradamente la extensión del paisaje.",
                    "Antítesis: contrapone dos ideas lógicamente incompatibles."
                ],
                "correct": 0,
                "teaches": ["recursos-retoricos-poesia"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El poema de Darío __ la angustia existencial mediante metáforas crepusculares. (evocar)",
                "answer": "evoca",
                "english": "Darío's poem evokes existential anguish through crepuscular metaphors.",
                "teaches": ["recursos-retoricos-poesia"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Darío", "revolucionó", "la", "métrica", "con", "el", "ritmo", "alejandrino."],
                "solution": ["Darío", "revolucionó", "la", "métrica", "con", "el", "ritmo", "alejandrino."],
                "english": "Darío revolutionized metrics with the Alexandrine rhythm.",
                "teaches": ["recursos-retoricos-poesia"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Profesora de literatura", "text": "¿Por qué se considera a Rubén Darío el refundador de la poesía en lengua española?"},
                    {"speaker": "Investigador literario", "text": "_____"},
                    {"speaker": "Profesora de literatura", "text": "Efectivamente, invirtió el flujo cultural entre España y América."}
                ],
                "options": [
                    "Porque introdujo una revolución métrica y sonora sin precedentes que revitalizó el idioma a ambos lados del Atlántico.",
                    "Porque nació en Metapa y fue diplomático en París y Madrid.",
                    "Porque los volcanes de Nicaragua son visitados por montañistas extranjeros."
                ],
                "correct": 0,
                "teaches": ["recursos-retoricos-poesia"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El refinamiento estético de las estrofas modernistas transformó la cadencia lírica castellana.",
                "english": "The aesthetic refinement of Modernist stanzas transformed Castilian lyrical cadence.",
                "teaches": ["recursos-retoricos-poesia"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=6,
        title="Rubén Darío y el Modernismo: La revolución del verso",
        goal="Analyze Rubén Darío's Modernist literary revolution, metric renovations (Alexandrines), and synesthetic aesthetics using poetic literary analysis vocabulary.",
        grammar_desc="recursos retóricos, figuras estilísticas y metalenguaje de la crítica literaria",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Trace the historical impact of Darío's 'Azul...' and the transatlantic Modernist movement.",
            "Identify key poetic devices: synesthesia, musical cadence, and the 14-syllable Alexandrine.",
            "Write formal literary critiques using analytical verbs (evocar, plasmar, simbolizar)."
        ],
        story_ref=f"stories/world/b2/{l2}.json",
        intro_body=[
            "Nicaragua is celebrated as the undisputed 'land of poets', and at its apex stands Rubén Darío: the diplomat and genius who reshaped modern Spanish.",
            "In this second lesson, we study the aesthetics of Modernism, learning the rhetorical metalanguage (synesthesia, Alexandrines, stanzas) required for literary critique at the B2 level."
        ],
        intro_title="Rubén Darío & Modernism's Poetic Revolution"
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-nicaragua-03 - Augusto C. Sandino: Soberanía y dignidad nacional
    # --------------------------------------------------------------------------
    l3 = "b2-nicaragua-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.nicaragua.03",
        "lesson": l3,
        "title": "Soberanía nacional y guerrilla libertaria",
        "theme": "Augusto C. Sandino, ocupación estadounidense y el Ejército Defensor de la Soberanía Nacional",
        "words": [
            {"lemma": "la soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "el intervencionismo", "translation": "interventionism", "pos": "noun"},
            {"lemma": "la emboscada", "translation": "ambush", "pos": "noun"},
            {"lemma": "la proclama", "translation": "proclamation, manifesto", "pos": "noun"},
            {"lemma": "la gesta libertaria", "translation": "heroic liberation feat", "pos": "noun"},
            {"lemma": "insumiso", "translation": "unsubmissive, rebellious", "pos": "adjective"},
            {"lemma": "el destacamento", "translation": "detachment (military)", "pos": "noun"},
            {"lemma": "el armisticio", "translation": "armistice, truce", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.nicaragua.03.condicional-contrafactico",
        "title": "Períodos hipotéticos contrafácticos en el pasado con pluscuamperfecto de subjuntivo",
        "sections": [
            {
                "type": "text",
                "title": "Hipótesis irreales sobre el pasado en el análisis historiográfico",
                "content": "El análisis histórico contrafáctico en nivel B2 evalúa lo que habría ocurrido si las circunstancias del pasado hubieran sido diferentes. La prótasis condicional se formula en pretérito pluscuamperfecto de subjuntivo ('si + hubiera / hubiese + participio'), y la apódosis consecuente se formula en condicional compuesto ('habría + participio') o, alternativamente en español culto, en otro pluscuamperfecto de subjuntivo: 'Si Sandino no hubiera resistido en las montañas de Las Segovias, la ocupación militar extranjera se habría prolongado indefinidamente'."
            },
            {
                "type": "table",
                "title": "Estructura del período contrafáctico de pasado",
                "rows": [
                    ["Prótasis: Si + Pluscuamperfecto de subjuntivo", "'Si los campesinos no hubieran apoyado a la guerrilla...'"],
                    ["Apódosis: Condicional compuesto", "'...el ejército defensor no habría podido resistir seis años de asedio.'"],
                    ["Apódosis: Pluscuamperfecto de subjuntivo (variante literaria)", "'...el ejército defensor no hubiera podido resistir.'"],
                    ["Contrafáctico mixto (pasado con consecuencia en presente)", "'Si Sandino hubiera capitulado en 1927, hoy no existiría este legado de soberanía'."]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la gesta sandinista",
                "items": [
                    {"spanish": "Si los marines estadounidenses hubieran conocido el terreno selvático de El Chipote, no habrían caído en tantas emboscadas.", "english": "If the US Marines had known the jungle terrain of El Chipote, they would not have fallen into so many ambushes."},
                    {"spanish": "Si Sandino no hubiese firmado la paz de buena fe en 1934, la Guardia Nacional no habría podido asesinarlo a traición.", "english": "If Sandino had not signed the peace in good faith in 1934, the National Guard would not have been able to assassinate him through treason."},
                    {"spanish": "Si la doctrina de soberanía no hubiera calado tan hondo, las futuras generaciones no habrían retomado su bandera.", "english": "If the doctrine of sovereignty had not penetrated so deeply, future generations would not have taken up his flag."}
                ]
            },
            {
                "type": "tip",
                "content": "¡Regla estricta!: Nunca utilices condicional simple ni condicional compuesto en la cláusula que empieza con 'si' ('*Si habría sabido*' es un error grave en la norma culta panhispánica; usa 'Si hubiera sabido')."
            }
        ]
    })

    write_json(f"stories/world/b2/{l3}.json", {
        "id": f"story.b2.{l3}",
        "title": "El general de hombres libres: Sandino en las brumas de Las Segovias",
        "level": "B2",
        "author": "Historia y Soberanía Nicaragüense",
        "summary": "La epopeya de Augusto C. Sandino, el rechazo al pacto del Espino Negro en 1927, la guerra de guerrillas en las montañas del norte contra los marines estadounidenses y el ideal cooperativo de Wiwilí.",
        "vocabularyTopics": ["Gesta sandinista", "Resistencia antimperialista", "Soberanía nacional"],
        "grammar": ["condicionales contrafácticos de pasado", "si + pluscuamperfecto de subjuntivo"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En mayo de 1927, tras la firma del pacto del Espino Negro entre los caudillos liberales y conservadores bajo la tutela de Washington, un joven líder de origen humilde se negó a entregar las armas. Augusto C. Sandino proclamó que la soberanía de una nación no se negocia y se internó en las intrincadas serranías de Las Segovias junto a veintinueve obreros y campesinos, fundando el legendario Ejército Defensor de la Soberanía Nacional de Nicaragua."
            },
            {
                "type": "narration",
                "text": "Durante seis años de asedio continuo, las tropas de intervención norteamericana emplearon por primera vez en la historia de la aviación militar el bombardeo aéreo en picada contra posiciones guerrilleras. Si los combatientes sandinistas no hubieran contado con el respaldo solidario de la población campesina y el dominio magistral de la selva, jamás habrían logrado doblegar al ejército expedicionario más poderoso de la época, forzando la retirada total de los marines en 1933."
            },
            {
                "type": "narration",
                "text": "Tras concertar un armisticio honorable con el gobierno democrático, Sandino fundó cooperativas agrícolas a orillas del río Coco para demostrar que la libertad política requería emancipación económica. Sin embargo, en febrero de 1934, fue asesinado por orden del jefe de la recién creada Guardia Nacional, Anastasio Somoza García, inaugurando una dinastía dictatorial de cuatro décadas pero legando al continente un ejemplo inmortal de dignidad patriótica."
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
                    ["la soberanía", "sovereignty"],
                    ["el intervencionismo", "interventionism"],
                    ["la emboscada", "ambush"],
                    ["insumiso", "unsubmissive, rebellious"]
                ],
                "teaches": ["b2-nicaragua-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la estructura gramatical canónica de una hipótesis irreal sobre el pasado en español formal?",
                "options": [
                    "Si + pretérito pluscuamperfecto de subjuntivo, condicional compuesto.",
                    "Si + condicional compuesto, pluscuamperfecto de subjuntivo.",
                    "Si + pretérito imperfecto de indicativo, presente de subjuntivo."
                ],
                "correct": 0,
                "teaches": ["condicional-contrafactico-pasado"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si Sandino __ las armas en 1927, la soberanía nacional no habría tenido un defensor tan decidido. (entregar - pluscuamperfecto de subjuntivo)",
                "answer": "hubiera entregado",
                "english": "If Sandino had surrendered his weapons in 1927, national sovereignty would not have had such a resolute defender.",
                "teaches": ["condicional-contrafactico-pasado"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Si", "hubieran", "conocido", "la", "selva,", "no", "habrían", "caído."],
                "solution": ["Si", "hubieran", "conocido", "la", "selva,", "no", "habrían", "caído."],
                "english": "If they had known the jungle, they would not have fallen.",
                "teaches": ["condicional-contrafactico-pasado"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador militar", "text": "¿Cómo logró una pequeña guerrilla campesina forzar el retiro de las tropas expedicionarias norteamericanas?"},
                    {"speaker": "Catedrática", "text": "_____"},
                    {"speaker": "Historiador militar", "text": "Fue bautizado por Gabriela Mistral como el 'pequeño ejército loco'."}
                ],
                "options": [
                    "Si Sandino no hubiera organizado redes campesinas de inteligencia en Las Segovias, sus destacamentos habrían sido neutralizados rápidamente.",
                    "La ciudad de León conserva la catedral colonial más grande de Centroamérica.",
                    "El gallo pinto nicaragüense se prepara con arroz, frijoles rojos y cebolla frita."
                ],
                "correct": 0,
                "teaches": ["condicional-contrafactico-pasado"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si los campesinos no hubiesen respaldado la causa libertaria, la resistencia no habría perdurado.",
                "english": "If the peasants had not backed the liberation cause, the resistance would not have endured.",
                "teaches": ["condicional-contrafactico-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=6,
        title="Augusto C. Sandino: Soberanía y dignidad nacional",
        goal="Examine Augusto C. Sandino's defense of national sovereignty and guerrilla strategy against foreign military occupation using past counterfactual conditionals.",
        grammar_desc="períodos condicionales contrafácticos en el pasado ('si + pluscuamperfecto de subjuntivo, condicional compuesto')",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Understand the military and geopolitical significance of Sandino's defense of Nicaraguan sovereignty (1927–1933).",
            "Assess the socioeconomic vision of the Segovias agricultural cooperatives.",
            "Master counterfactual reasoning in historical writing with past subjunctive and compound conditional."
        ],
        story_ref=f"stories/world/b2/{l3}.json",
        intro_body=[
            "Lesson 3 centers on Augusto C. Sandino, the 'General of Free Men', whose anti-imperialist campaign in the Segovian mountains captured global imagination.",
            "We analyze the historical strategy of sovereignty and examine how to formulate counterfactual hypotheses in the past ('si hubiera X, habría ocurrido Y')."
        ],
        intro_title="Sandino & National Sovereignty"
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-nicaragua-04 - La Revolución de 1979, la alfabetización y Solentiname
    # --------------------------------------------------------------------------
    l4 = "b2-nicaragua-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.nicaragua.04",
        "lesson": l4,
        "title": "Revolución, educación popular y arte primitivista",
        "theme": "Triunfo sandinista de 1979, Cruzada Nacional de Alfabetización y Ernesto Cardenal",
        "words": [
            {"lemma": "la alfabetización", "translation": "literacy teaching/crusade", "pos": "noun"},
            {"lemma": "el brigadista", "translation": "literacy brigade volunteer", "pos": "noun"},
            {"lemma": "la cartilla", "translation": "primer, elementary reading book", "pos": "noun"},
            {"lemma": "el arte primitivista", "translation": "primitivist/naif painting", "pos": "noun"},
            {"lemma": "la insurrección", "translation": "insurrection, uprising", "pos": "noun"},
            {"lemma": "el campesinado", "translation": "peasantry", "pos": "noun"},
            {"lemma": "la epopeya", "translation": "epic, saga", "pos": "noun"},
            {"lemma": "la utopía", "translation": "utopia", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.nicaragua.04.concesivas-politicas-aun-cuando",
        "title": "Concesivas de registro formal: aun cuando, si bien y a sabiendas de que",
        "sections": [
            {
                "type": "text",
                "title": "Ponderación de obstáculos en la crónica revolucionaria y sociológica",
                "content": "Para relatar epopeyas colectivas y dilemas sociopolíticos en nivel B2, los nexos concesivos de registro formal aportan riqueza matizada. La locución 'aun cuando' equivale a 'aunque' en un registro más elevado; rige indicativo cuando se refiere a un obstáculo real constatado ('Aun cuando enfrentaban una escasez material severa, los brigadistas no se desalentaron') o subjuntivo si la circunstancia se concibe como hipótesis o indiferencia ('Aun cuando arrecien las dificultades, la campaña continuará'). Por su parte, 'a sabiendas de que' denota conciencia plena de un hecho adverso y rige siempre indicativo: 'Partieron hacia la selva a sabiendas de que el paludismo era endémico'."
            },
            {
                "type": "table",
                "title": "Conectores concesivos avanzados",
                "rows": [
                    ["aun cuando + INDICATIVO", "Obstáculo verificado: 'Aun cuando el analfabetismo rondaba el 50%, la cruzada triunfó'"],
                    ["aun cuando + SUBJUNTIVO", "Hipótesis o condición extrema: 'Aun cuando intenten silenciar el arte, la belleza perdura'"],
                    ["a sabiendas de que + INDICATIVO", "Conciencia deliberada de un riesgo real: 'Asumieron la tarea a sabiendas de que sería titánica'"],
                    ["siquiera (con negación)", "Matiz de concesión mínima: 'No descansaron ni siquiera cuando cayó la noche'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la Cruzada de Alfabetización y Solentiname",
                "items": [
                    {"spanish": "Aun cuando los caminos rurales eran intransitables por el fango, sesenta mil jóvenes brigadistas llegaron a cada rincón del país.", "english": "Even though rural roads were impassable from mud, sixty thousand young brigade members reached every corner of the country."},
                    {"spanish": "Los campesinos de Solentiname pintaban sus lienzos primitivistas a sabiendas de que la guardia somocista vigilaba sus reuniones.", "english": "Solentiname peasants painted their primitivist canvases fully knowing that the Somoza guard was surveilling their meetings."},
                    {"spanish": "Si bien la guerra de agresión posterior truncó muchas metas sociales, la erradicación del analfabetismo fue reconocida por la UNESCO.", "english": "Although the subsequent war of aggression thwarted many social goals, the eradication of illiteracy was recognized by UNESCO."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que 'a sabiendas de que' nunca lleva subjuntivo en español formal, porque el hablante presupone que la verdad del hecho es enteramente conocida por el sujeto."
            }
        ]
    })

    write_json(f"stories/world/b2/{l4}.json", {
        "id": f"story.b2.{l4}",
        "title": "Lápiz y fusil: La epopeya de la alfabetización y las islas de Solentiname",
        "level": "B2",
        "author": "Educación Popular y Arte Comunitario",
        "summary": "El derrocamiento de la dinastía somocista en julio de 1979, la gesta educativa de la Cruzada Nacional de Alfabetización de 1980 y la comunidad poética y pictórica fundada por Ernesto Cardenal en el archipiélago de Solentiname.",
        "vocabularyTopics": ["Revolución popular sandinista", "Cruzada de Alfabetización", "Comunidad de Solentiname"],
        "grammar": ["concesivas avanzadas con aun cuando", "a sabiendas de que con indicativo"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "El 19 de julio de 1979, una insurrección popular generalizada puso fin a más de cuatro décadas de tiranía de la familia Somoza en Nicaragua. Conscientes de que ninguna transformación social es duradera sin la emancipación cultural, las nuevas autoridades lanzaron en marzo de 1980 la Cruzada Nacional de Alfabetización 'Héroes y Mártires por la Liberación de Nicaragua', una de las epopeyas educativas más luminosas de la historia contemporánea."
            },
            {
                "type": "narration",
                "text": "Más de noventa mil voluntarios —en su inmensa mayoría muchachos y muchachas de secundaria y universidad llamados brigadistas— se trasladaron a las montañas, compartieron el rancho, la milpa y la hamaca con las familias campesinas y enseñaron a leer y escribir a más de cuatrocientas mil personas. Aun cuando el país enfrentaba una bancarrota económica total, en apenas cinco meses el analfabetismo se redujo del cincuenta al doce por ciento, hazaña galardonada con la medalla Nadezhda Krúpskaya de la UNESCO."
            },
            {
                "type": "narration",
                "text": "Simultáneamente, en el archipiélago de Solentiname, en el extremo sur del lago Cocibolca, el poeta y sacerdote trapense Ernesto Cardenal había sembrado las semillas de una revolución espiritual y estética. Pescadores y agricultores que jamás habían tocado un pincel comenzaron a plasmar aves tropicales, volcanes y aguas turquesas en lienzos de un luminoso arte primitivista, demostrando que la poesía y la belleza son derechos inalienables del pueblo llano."
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
                    ["la alfabetización", "literacy teaching/crusade"],
                    ["el brigadista", "literacy brigade volunteer"],
                    ["la cartilla", "primer, reading booklet"],
                    ["el arte primitivista", "primitivist/naif painting"]
                ],
                "teaches": ["b2-nicaragua-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo exige de manera obligatoria la locución concesiva 'a sabiendas de que'?",
                "options": [
                    "Modo indicativo, porque presupone la certeza consciente y deliberada de un hecho real.",
                    "Modo subjuntivo, porque denota un deseo altruista no consumado.",
                    "Modo imperativo, porque transmite una orden a los brigadistas."
                ],
                "correct": 0,
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Aun cuando los caminos __ inundados por el invierno tropical, los brigadistas llegaron a las aldeas. (estar - pretérito imperfecto de indicativo)",
                "answer": "estaban",
                "english": "Even though roads were flooded by the tropical winter, the brigade members reached the villages.",
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Viajaron", "a", "sabiendas", "de", "que", "las", "condiciones", "eran", "duras."],
                "solution": ["Viajaron", "a", "sabiendas", "de", "que", "las", "condiciones", "eran", "duras."],
                "english": "They traveled knowing that conditions were harsh.",
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador de la educación", "text": "¿Por qué causó tanto impacto mundial la Cruzada de Alfabetización de 1980 en Nicaragua?"},
                    {"speaker": "Pedagoga", "text": "_____"},
                    {"speaker": "Historiador de la educación", "text": "Un modelo de solidaridad juvenil e integración social sin precedentes."}
                ],
                "options": [
                    "Aun cuando los recursos eran escasos, movilizó a toda una generación urbana para convivir con los campesinos y erradicar el analfabetismo.",
                    "El café de Matagalpa y Jinotega se exporta principalmente a mercados europeos.",
                    "Las iglesias coloniales de León albergan imágenes religiosas talladas en madera."
                ],
                "correct": 0,
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aun cuando las dificultades materiales eran inmensas, la cartilla de lectura llevó la luz del saber al campo.",
                "english": "Even though material difficulties were immense, the reading primer brought the light of knowledge to the countryside.",
                "teaches": ["concesivas-politicas-aun-cuando"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=6,
        title="La Revolución de 1979, la alfabetización y Solentiname",
        goal="Analyze the 1979 Sandinista triumph, the 1980 National Literacy Crusade, and Ernesto Cardenal's Solentiname peasant art using advanced concessive structures.",
        grammar_desc="nexos concesivos formales ('aun cuando', 'a sabiendas de que') en la narración social e histórica",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Examine the mobilization and UNESCO recognition of the 1980 Nicaraguan Literacy Crusade.",
            "Understand Ernesto Cardenal's liberation theology community and primitivist painting in Solentiname.",
            "Deploy formal concessive markers ('aun cuando', 'a sabiendas de que') accurately in sociological prose."
        ],
        story_ref=f"stories/world/b2/{l4}.json",
        intro_body=[
            "Lesson 4 explores one of the most remarkable social mobilizations in Latin American history: the 1980 Literacy Crusade and the artistic utopian community of Solentiname.",
            "We examine how poetry, education, and social emancipation converged, while mastering high-register concessive syntax ('aun cuando', 'a sabiendas de que')."
        ],
        intro_title="The 1979 Revolution, Literacy & Solentiname"
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-nicaragua-05 - Resistencia cívica, destierro y la voz de la diáspora
    # --------------------------------------------------------------------------
    l5 = "b2-nicaragua-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.nicaragua.05",
        "lesson": l5,
        "title": "Autoritarismo, resistencia y la patria en el exilio",
        "theme": "Protestas de abril de 2018, privación de nacionalidad y literatura en el destierro",
        "words": [
            {"lemma": "el destierro", "translation": "banishment, exile", "pos": "noun"},
            {"lemma": "la privación de nacionalidad", "translation": "stripping of citizenship", "pos": "noun"},
            {"lemma": "la patria portátil", "translation": "portable homeland (culture in exile)", "pos": "noun"},
            {"lemma": "la disidencia", "translation": "dissent, political opposition", "pos": "noun"},
            {"lemma": "la censura", "translation": "censorship", "pos": "noun"},
            {"lemma": "la diáspora", "translation": "diaspora", "pos": "noun"},
            {"lemma": "la resiliencia ciudadana", "translation": "civic resilience", "pos": "noun"},
            {"lemma": "despojar", "translation": "to strip, to dispossess", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.nicaragua.05.integracion-cronica-politica",
        "title": "Integración discursiva: Consecutivas, contrafácticos y concesivas en la crónica del exilio",
        "sections": [
            {
                "type": "text",
                "title": "Síntesis gramatical para el ensayo sobre derechos humanos y literatura",
                "content": "La crónica contemporánea sobre el autoritarismo, la privación de nacionalidad y la diáspora intelectual en Nicaragua exige una articulación sintáctica madura. La integración de cláusulas consecutivas ('de tal manera que'), hipótesis contrafácticas sobre el pasado ('si la comunidad cívica no hubiera salido a las calles...') y nexos concesivos de registro formal ('aun cuando los despojaron de sus pasaportes...') permite relatar con profundidad moral y solvencia académica la defensa de la libertad."
            },
            {
                "type": "examples",
                "title": "Modelos sintácticos en el ensayo contemporáneo",
                "items": [
                    {"spanish": "El régimen clausuró universidades y medios de prensa de tal manera que asfixió el debate público independiente.", "english": "The regime closed universities and press outlets in such a way that it choked independent public debate."},
                    {"spanish": "Si los escritores no hubieran asumido la palabra como trinchera moral, la memoria de las víctimas habría sido silenciada por el decreto estatal.", "english": "If writers had not embraced the word as a moral trench, the memory of victims would have been silenced by state decree."},
                    {"spanish": "Aun cuando los despojaron de su nacionalidad formal, autores como Sergio Ramírez y Gioconda Belli llevan a Nicaragua en el alma de su literatura.", "english": "Even though they were stripped of their formal nationality, authors like Sergio Ramírez and Gioconda Belli carry Nicaragua in the soul of their literature."}
                ]
            },
            {
                "type": "tip",
                "content": "Para estructurar un ensayo de clausura de unidad, plantea la paradoja histórica con una concesiva ('Aun cuando X'), desarrolla el impacto con una consecutiva ('de modo que Y') y reflexiona sobre la memoria con un contrafáctico ('Si no hubiese sido por Z...')."
            }
        ]
    })

    write_json(f"stories/world/b2/{l5}.json", {
        "id": f"story.b2.{l5}",
        "title": "La patria en la palabra: Escritores nicaragüenses en el destierro",
        "level": "B2",
        "author": "Literatura y Derechos Humanos en Nicaragua",
        "summary": "Las protestas cívicas de abril de 2018, la deriva autoritaria del gobierno nicaragüense, la insólita medida de despojar de su nacionalidad a más de trescientos escritores, líderes y periodistas en 2023, y la defensa de la patria portátil a través de la literatura de Gioconda Belli y Sergio Ramírez.",
        "vocabularyTopics": ["Crisis política de 2018", "Destierro y apátridas forzados", "Literatura de la diáspora"],
        "grammar": ["consecutivas formales", "contrafácticos de pasado", "concesivas con aun cuando"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En abril de 2018, lo que comenzó como una protesta pacífica de estudiantes y ancianos contra reformas unilaterales a la seguridad social desencadenó una movilización cívica masiva en toda Nicaragua. La respuesta armada estatal dejó cientos de manifestantes asesinados, miles de heridos y el encarcelamiento sistemático de líderes opositores, clausurando las libertades democráticas de tal manera que sumió al país en la crisis institucional más grave de su historia reciente."
            },
            {
                "type": "narration",
                "text": "A comienzos de 2023, en una medida sin precedentes en el derecho internacional contemporáneo, el régimen desterró y despojó arbitrariamente de su nacionalidad a más de trescientas personalidades de la sociedad civil, incluidos obispos católicos, activistas de derechos humanos y gigantes de las letras hispanas como el Premio Cervantes Sergio Ramírez y la laureada poeta Gioconda Belli, declarándolos traidores a la patria y confiscando sus bienes y bibliotecas."
            },
            {
                "type": "narration",
                "text": "Aun cuando los gobernantes pretendieron borrarlos de su propio suelo, los escritores respondieron con la serena dignidad de la inteligencia. Desde el exilio en Madrid, San José o Ciudad de México, proclamaron que la verdadera nacionalidad no radica en un pasaporte expedido por un déspota, sino en la lengua de Rubén Darío, en el recuerdo de sus lagos y volcanes y en la patria portátil de sus poemas y novelas, los cuales ninguna tiranía podrá jamás arrebatarles ni confiscar."
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
                    ["el destierro", "banishment, exile"],
                    ["la privación de nacionalidad", "stripping of citizenship"],
                    ["la patria portátil", "portable homeland in exile"],
                    ["la resiliencia ciudadana", "civic resilience"]
                ],
                "teaches": ["b2-nicaragua-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué recurso sintáctico resume con mayor elegancia la resistencia intelectual frente al despojo de nacionalidad?",
                "options": [
                    "Aun cuando les arrebataron la nacionalidad formal, los escritores mantienen viva la memoria de su país en la literatura.",
                    "Porque les quitaron el pasaporte entonces ellos ahora viven en otro país lejano.",
                    "Se fueron los escritores para que el gobierno no los mirara más en la calle."
                ],
                "correct": 0,
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El régimen clausuró los medios independientes de tal manera que __ la libertad de prensa. (asfixiar - pretérito indefinido)",
                "answer": "asfixió",
                "english": "The regime closed independent media in such a way that it choked press freedom.",
                "teaches": ["consecutivas-de-tal-manera"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Si", "no", "hubieran", "escrito,", "la", "memoria", "se", "habría", "perdido."],
                "solution": ["Si", "no", "hubieran", "escrito,", "la", "memoria", "se", "habría", "perdido."],
                "english": "If they had not written, the memory would have been lost.",
                "teaches": ["condicional-contrafactico-pasado"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista internacional", "text": "¿Cómo conciben los intelectuales desterrados su vínculo con Nicaragua tras el retiro forzado de su nacionalidad?"},
                    {"speaker": "Ensayista nicaragüense", "text": "_____"},
                    {"speaker": "Periodista internacional", "text": "La palabra poética como patria inalienable frente al autoritarismo."}
                ],
                "options": [
                    "Aun cuando un decreto arbitrario nos declare apátridas, la identidad nicaragüense es una patria portátil tejida con versos, memoria y dignidad que nadie puede confiscar.",
                    "El café de exportación se clasifica según el tamaño del grano y la altitud del cafetal.",
                    "Los transbordadores lacustres parten puntualmente al despuntar el alba."
                ],
                "correct": 0,
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si la diáspora no hubiese alzado la voz en foros internacionales, el atropello a las libertades habría pasado inadvertido.",
                "english": "If the diaspora had not raised its voice in international forums, the outrage against freedoms would have gone unnoticed.",
                "teaches": ["condicional-contrafactico-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=6,
        title="Resistencia cívica, destierro y la voz de la diáspora",
        goal="Analyze contemporary Nicaraguan civic resistance, exile, and the intellectual diaspora using integrated consecutive, counterfactual, and concessive syntax.",
        grammar_desc="integración discursiva de consecutivas, períodos contrafácticos de pasado y concesivas de registro formal",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Examine the 2018 civic uprising and contemporary authoritarian repression in Nicaragua.",
            "Assess the legal and human impact of stripping nationality from writers and civic leaders.",
            "Combine consecutive clauses, past counterfactual conditionals, and formal concessions in political essays."
        ],
        story_ref=f"stories/world/b2/{l5}.json",
        intro_body=[
            "Our final topic lesson in Unit 6 addresses contemporary Nicaragua: the 2018 civic mobilization, authoritarian closure, and the defense of freedom by writers in exile like Sergio Ramírez and Gioconda Belli.",
            "We examine the concept of the 'portable homeland' in the diaspora, integrating consecutive, counterfactual, and concessive grammatical structures."
        ],
        intro_title="Civic Resistance, Exile & the Diaspora's Voice"
    ))

    # --------------------------------------------------------------------------
    # Lesson 6: b2-nicaragua-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-nicaragua-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la cuenca lacustre", "lake basin"],
                    ["el verso alejandrino", "14-syllable verse line"],
                    ["la soberanía", "national sovereignty"],
                    ["el destierro", "banishment, exile"]
                ],
                "teaches": ["b2-nicaragua-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿En cuál de las siguientes oraciones la locución 'de tal manera que' rige modo subjuntivo?",
                "options": [
                    "Debemos redactar las leyes de tal manera que protejan efectivamente la libertad de expresión.",
                    "El volcán arrojó tanta lava de tal manera que sepultó la antigua ermita colonial.",
                    "El oleaje del lago aumentó de tal manera que los barcos suspendieron sus travesías."
                ],
                "correct": 0,
                "teaches": ["consecutivas-de-tal-manera"]
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué es incorrecto decir '*Si Sandino sabría de la traición, no habría ido a la reunión'?",
                "options": [
                    "Porque la cláusula introducida por 'si' en una hipótesis irreal sobre el pasado exige pretérito pluscuamperfecto de subjuntivo (hubiera sabido), nunca condicional.",
                    "Porque el verbo 'saber' es defectivo en tiempos compuestos.",
                    "Porque 'Sandino' es un nombre propio y exige artículo definido."
                ],
                "correct": 0,
                "teaches": ["condicional-contrafactico-pasado"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Aun cuando los despojaron de sus pasaportes, su literatura __ viva en el corazón de Nicaragua. (permanecer)",
                "answer": "permanece",
                "english": "Even though they were stripped of their passports, their literature remains alive in the heart of Nicaragua.",
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "El lago Cocibolca es tan inmenso que alberga olas similares a las del mar abierto. [Lake Cocibolca is so immense that it harbors waves similar to those of the open sea.]",
                    "Darío renovó la métrica española mediante el verso alejandrino y sutiles sinestesias. [Darío renovated Spanish metrics through the Alexandrine verse and subtle synesthesias.]",
                    "Si Sandino no hubiera resistido, la intervención extranjera se habría prolongado. [If Sandino had not resisted, the foreign intervention would have been prolonged.]",
                    "Aun cuando enfrentan el destierro, los poetas defienden su patria portátil en la diáspora. [Even though they face exile, the poets defend their portable homeland in the diaspora.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["consecutivas-de-tal-manera", "recursos-retoricos-poesia", "condicional-contrafactico-pasado", "concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diplomático", "text": "¿Cómo sintetizaría el destino de Nicaragua desde Darío y Sandino hasta la resistencia contemporánea?"},
                    {"speaker": "Escritora en el exilio", "text": "_____"},
                    {"speaker": "Diplomático", "text": "Una vocación indomable de poesía, libertad y soberanía que trasciende cualquier frontera."}
                ],
                "options": [
                    "Es la historia de una nación apasionada donde la belleza de la palabra poética y el reclamo de justicia popular siempre han vencido a la tiranía.",
                    "Las lanchas de motor viajan entre Granada y la isla de Ometepe todas las mañanas.",
                    "El parque nacional volcán Masaya cuenta con miradores seguros para los turistas."
                ],
                "correct": 0,
                "teaches": ["concesivas-politicas-aun-cuando"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si los brigadistas no hubieran recorrido las montañas, no se habría erradicado el analfabetismo.",
                "english": "If the brigade members had not traversed the mountains, illiteracy would not have been eradicated.",
                "teaches": ["condicional-contrafactico-pasado"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta una reflexión histórica empleando un período condicional contrafáctico de pasado ('Si + pluscuamperfecto de subjuntivo, condicional compuesto').",
                        "answer": "Si la sociedad civil no hubiera alzado su voz con valentía, el autoritarismo se habría consolidado sin resistencia moral."
                    }
                ],
                "teaches": ["condicional-contrafactico-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=6,
        title="Unit 6 Consolidation: Nicaragua",
        goal="Consolidate consecutive clauses of manner, poetic analysis vocabulary, past counterfactual conditionals, and formal concessions through Nicaraguan history and literature.",
        grammar_desc="síntesis de consecutivas, retórica poética, períodos contrafácticos de pasado y concesivas formales",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Construct consecutive clauses ('de tal manera que') differentiating indicative from subjunctive.",
            "Deploy literary analysis vocabulary (verso alejandrino, sinestesia, cadencia, metáfora).",
            "Master counterfactual historical reasoning with past subjunctive and compound conditional.",
            "Use formal concessive markers ('aun cuando', 'a sabiendas de que') in political essays."
        ],
        checklist_items=[
            "I can formulate consecutive sentences of manner and intensity with indicative and subjunctive.",
            "I can analyze poetry using Modernist aesthetic terminology (sinestesia, alejandrino).",
            "I can express past counterfactual hypotheses with 'si' + pluperfect subjunctive.",
            "I can deploy high-register concessions ('aun cuando', 'a sabiendas de que') in historical essays."
        ],
        story_ref=f"stories/world/b2/{l5}.json"
    ))
    print("Completed LatAm Unit 6 (Nicaragua) generation!")


if __name__ == "__main__":
    generate_latam_unit_6()
