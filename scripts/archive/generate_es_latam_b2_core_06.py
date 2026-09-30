#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Core Unit 6:
  - Title: "Emotional Reactions & Affective Stance" (Reacciones emocionales y posicionamiento afectivo)
  - Stems: b2-06-01 through b2-06-consolidation
  - Classic Literature Story: Eduardo Galeano - "Las venas abiertas de América Latina: Indignación moral y la memoria saqueada"
"""

from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson


def generate_core_unit_6():
    # Vocab theme slug: b2-unit06-vocab
    # Grammar skills:
    #   - afeccion-psicologica-subjuntivo
    #   - empatia-pesar-subjuntivo
    #   - exclamativas-evaluativas-subjuntivo
    #   - el-hecho-de-que-subjuntivo

    # --------------------------------------------------------------------------
    # Lesson 1: b2-06-01 - Verbos de afección psicológica con experimentador dativo
    # --------------------------------------------------------------------------
    l1 = "b2-06-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.06.01",
        "lesson": l1,
        "title": "Afección psicológica e inquietud",
        "theme": "Verbos de afección psíquica y estados anímicos",
        "words": [
            {"lemma": "inquietar", "translation": "to worry, to disquiet", "pos": "verb"},
            {"lemma": "la consternación", "translation": "consternation, dismay", "pos": "noun"},
            {"lemma": "desconcertar", "translation": "to disconcert, to bewilder", "pos": "verb"},
            {"lemma": "el desasosiego", "translation": "unease, restlessness", "pos": "noun"},
            {"lemma": "asombrar", "translation": "to astonish, to amaze", "pos": "verb"},
            {"lemma": "el estupor", "translation": "stupor, astonishment", "pos": "noun"},
            {"lemma": "indignar", "translation": "to outrage, to anger", "pos": "verb"},
            {"lemma": "desolador", "translation": "devastating, bleak", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.06.01.afeccion-psicologica",
        "title": "Subjuntivo con verbos de afección psicológica tipo gustar",
        "sections": [
            {
                "type": "text",
                "title": "Estructura sintáctica con experimentador dativo",
                "content": "Los verbos de afección psicológica o reacción emotiva (inquietar, preocupar, molestar, indignar, asombrar, desconcertar, entristecer) funcionan sintácticamente con un pronombre de objeto indirecto (el experimentador o experimentador afectivo: 'me', 'te', 'le', 'nos', 'les') y una proposición sustantiva sujeto introducida por 'que'. En el nivel B2, esta proposición subordinada exige obligatoriamente modo subjuntivo, ya que el hablante no afirma el hecho de manera neutra, sino que lo filtra a través de su impacto anímico: 'A los ciudadanos les indigna que los gobernantes ignoren sus reclamos'."
            },
            {
                "type": "table",
                "title": "Estructura de la reacción afectiva",
                "rows": [
                    ["Pronombre dativo + Verbo de afección + que + SUBJUNTIVO", "'Me inquieta que persista la polarización política'"],
                    ["Con intensificación", "'A la comunidad internacional le desconcierta que no se respeten los tratados'"],
                    ["Contraste con indicativo (causales)", "Compárese con 'Me enojé porque llegaron tarde' (causal factual) frente a 'Me enoja que lleguen tarde' (sustantiva sujeto evaluativa)"],
                    ["Con infinitivo (sin cambio de experimentador)", "'Me asombra descubrir la verdad' (mismo sujeto/experimentador)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo social",
                "items": [
                    {"spanish": "Nos preocupa profundamente que la desigualdad económica continúe ensanchándose en la región.", "english": "It deeply concerns us that economic inequality continues widening in the region."},
                    {"spanish": "A los historiadores les asombra que la memoria colectiva haya resistido a décadas de censura.", "english": "It astounds historians that collective memory has resisted decades of censorship."},
                    {"spanish": "Les indigna que las corporaciones evadan sus responsabilidades medioambientales sin consecuencias.", "english": "It outrages them that corporations evade their environmental responsibilities without consequences."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que el verbo de afección concuerda en singular (tercera persona) cuando el sujeto es una oración subordinada: 'Me indigna que hagan X' (nunca '*Me indignan que hagan X*')."
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
                    ["inquietar", "to worry, to disquiet"],
                    ["la consternación", "consternation, dismay"],
                    ["el desasosiego", "unease, restlessness"],
                    ["desolador", "devastating, bleak"]
                ],
                "teaches": ["b2-unit06-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el verbo subordinado va en subjuntivo en 'A las comunidades les preocupa que el río se contamine'?",
                "options": [
                    "Porque la proposición subordinada es el sujeto de un verbo de afección psicológica que evalúa emocionalmente el evento.",
                    "Porque el río no existe en la realidad empírica.",
                    "Porque 'preocupar' es un verbo de habla que exige estilo indirecto."
                ],
                "correct": 0,
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A los defensores de derechos humanos les desconcierta que la fiscalía __ los expedientes. (archivar)",
                "answer": "archive",
                "english": "It bewilders human rights defenders that the prosecution archives the files.",
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Nos", "indigna", "que", "se", "tolere", "la", "impunidad", "sistemática."],
                "solution": ["Nos", "indigna", "que", "se", "tolere", "la", "impunidad", "sistemática."],
                "english": "It outrages us that systematic impunity is tolerated.",
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Cuál es la reacción general de la ciudadanía ante los recientes recortes en el presupuesto educativo?"},
                    {"speaker": "Líder estudiantil", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Es una reacción enteramente comprensible ante la merma de oportunidades."}
                ],
                "options": [
                    "A las familias les inquieta profundamente que las universidades públicas pierdan recursos esenciales para la investigación.",
                    "El campus universitario fue diseñado a mediados del siglo pasado por arquitectos modernistas.",
                    "Los exámenes de admisión se celebran anualmente en el mes de noviembre."
                ],
                "correct": 0,
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Nos asombra que las autoridades no hayan tomado medidas preventivas frente a la emergencia climática.",
                "english": "It astounds us that authorities have not taken preventive measures in the face of the climate emergency.",
                "teaches": ["afeccion-psicologica-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=6,
        title="Verbos de afección psicológica con experimentador dativo",
        goal="Express psychological concern, bewilderment, and outrage using gustar-type affective verbs with dative experiencers and subjunctive complements.",
        grammar_desc="el régimen de subjuntivo en oraciones sustantivas sujeto con verbos de afección psicológica",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Structure affective sentences with dative pronouns (me, te, le, nos, les) and third-person singular verbs.",
            "Trigger subjunctive complements expressing emotional reaction (inquietar, indignar, desconcertar).",
            "Deploy sophisticated psychological vocabulary (desasosiego, consternación, estupor)."
        ],
        intro_body=[
            "Welcome to Unit 6 of Spanish B2 Core: Emotional Reactions & Affective Stance. Mastering adult, high-level Spanish requires moving beyond simple statements of fact to articulate emotional impact, ethical indignation, and empathetic solidarity.",
            "In this first lesson, we explore psychological affective verbs like 'inquietar', 'preocupar', and 'indignar', examining their dative syntactic architecture and subjunctive governance."
        ],
        intro_title="Unit 6: Emotional Reactions & Affective Stance"
    ))

    # --------------------------------------------------------------------------
    # Lesson 2: b2-06-02 - Empatía, pesar, solidaridad y disculpa
    # --------------------------------------------------------------------------
    l2 = "b2-06-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.06.02",
        "lesson": l2,
        "title": "Empatía, compasión y solidaridad",
        "theme": "Expresiones de aflicción, duelo, solidaridad y disculpa",
        "words": [
            {"lemma": "lamentar", "translation": "to regret, to lament", "pos": "verb"},
            {"lemma": "la solidaridad", "translation": "solidarity", "pos": "noun"},
            {"lemma": "conmoverse", "translation": "to be moved/touched", "pos": "verb"},
            {"lemma": "el pésame", "translation": "condolences", "pos": "noun"},
            {"lemma": "solidarizarse", "translation": "to stand in solidarity", "pos": "verb"},
            {"lemma": "la aflicción", "translation": "affliction, grief", "pos": "noun"},
            {"lemma": "deplorar", "translation": "to deplore, to lament deeply", "pos": "verb"},
            {"lemma": "el desagravio", "translation": "redress, apology, vindication", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.06.02.empatia-pesar-subjuntivo",
        "title": "Subjuntivo con verbos de sentimiento, empatía y pesar",
        "sections": [
            {
                "type": "text",
                "title": "Verbos de afección directa y expresión de condolencias",
                "content": "A diferencia de los verbos con dativo, los verbos de sentimiento donde el sujeto gramatical es quien experimenta la emoción (lamentar, sentir, deplorar, alegrarse de, dolerse de) también rigen obligatoriamente subjuntivo cuando su complemento oracional tiene un sujeto diferente: 'Lamentamos que la catástrofe haya causado tantas pérdidas'. Si no hay cambio de sujeto, se utiliza infinitivo: 'Lamentamos no poder asistir'."
            },
            {
                "type": "table",
                "title": "Verbos y locuciones de pesar y solidaridad",
                "rows": [
                    ["lamentar / sentir que + SUBJUNTIVO", "'Sentimos que hayan tenido que atravesar una situación tan dolorosa'"],
                    ["deplorar que + SUBJUNTIVO", "'La comunidad internacional deplora que se violen los derechos fundamentales'"],
                    ["alegrarse de que + SUBJUNTIVO", "'Nos alegramos de que las familias se hayan reencontrado sanas y salvas'"],
                    ["solidarizarse con que + SUBJUNTIVO", "'Nos solidarizamos con que los trabajadores reclamen un salario digno'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el registro diplomático y humanitario",
                "items": [
                    {"spanish": "El comité humanitario lamenta que los convoyes de alimentos no hayan podido acceder a la zona de conflicto.", "english": "The humanitarian committee regrets that food convoys have not been able to access the conflict zone."},
                    {"spanish": "Deploramos que la violencia empañe los esfuerzos de pacificación comunitaria.", "english": "We deplore that violence tarnishes community pacification efforts."},
                    {"spanish": "Nos conmueve que tantas personas anónimas hayan donado víveres para los damnificados.", "english": "It moves us that so many anonymous individuals have donated provisions for the victims."}
                ]
            },
            {
                "type": "tip",
                "content": "No confundas 'sentir que' en sentido de 'lamentar' (que rige subjuntivo: 'Siento que estés enfermo') con 'sentir que' como percepción física o mental (que rige indicativo: 'Siento que el ambiente está tenso')."
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
                    ["lamentar", "to regret, to lament"],
                    ["deplorar", "to deplore, to lament deeply"],
                    ["la aflicción", "affliction, grief"],
                    ["el desagravio", "redress, apology, vindication"]
                ],
                "teaches": ["b2-unit06-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿En cuál de las siguientes oraciones 'sentir que' rige modo subjuntivo?",
                "options": [
                    "Siento mucho que hayas tenido que pasar por esa amarga experiencia.",
                    "Siento que alguien me está observando desde la ventana.",
                    "Sentí que el temblor sacudía levemente el suelo."
                ],
                "correct": 0,
                "teaches": ["empatia-pesar-subjuntivo"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Deploramos profundamente que las partes en conflicto no __ el cese al fuego humanitario. (respetar)",
                "answer": "respeten",
                "english": "We deeply deplore that the parties in conflict do not respect the humanitarian ceasefire.",
                "teaches": ["empatia-pesar-subjuntivo"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Lamentamos", "que", "las", "familias", "hayan", "sufrido", "tanto", "dolor."],
                "solution": ["Lamentamos", "que", "las", "familias", "hayan", "sufrido", "tanto", "dolor."],
                "english": "We regret that the families have suffered so much pain.",
                "teaches": ["empatia-pesar-subjuntivo"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Portavoz de la Cruz Roja", "text": "¿Cuál es la postura oficial del organismo tras el colapso del puente fronterizo?"},
                    {"speaker": "Delegada regional", "text": "_____"},
                    {"speaker": "Portavoz de la Cruz Roja", "text": "Iniciaremos de inmediato el puente aéreo para suministrar medicinas."}
                ],
                "options": [
                    "Lamentamos profundamente que las comunidades ribereñas hayan quedado incomunicadas y exigimos un corredor seguro.",
                    "El puente fue construido en hormigón armado durante la administración anterior.",
                    "Las lanchas de motor consumen combustible diésel para su desplazamiento."
                ],
                "correct": 0,
                "teaches": ["empatia-pesar-subjuntivo"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Nos alegra que los acuerdos de reconciliación hayan devuelto la tranquilidad a los pobladores.",
                "english": "We are glad that the reconciliation agreements have returned peace of mind to the townspeople.",
                "teaches": ["empatia-pesar-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=6,
        title="Empatía, pesar, solidaridad y disculpa",
        goal="Express diplomatic empathy, humanitarian grief, and ethical solidarity using verbs of feeling with subjunctive complements (lamentar, deplorar, dolerse de).",
        grammar_desc="el modo subjuntivo con verbos de sentimiento, empatía y aflicción",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Distinguish between emotive 'sentir que' (+ subj) and cognitive/perceptive 'sentir que' (+ ind).",
            "Express formal condolences and humanitarian solidarity in diplomatic letters.",
            "Deploy compassionate and consoling lexical items (desagravio, aflicción, conmocionado)."
        ],
        intro_body=[
            "Expressing empathy, ethical grief, and solidarity is an indispensable component of mature social interaction and diplomatic discourse.",
            "In this lesson, we study verbs of regret and emotion ('lamentar', 'deplorar', 'alegrarse de'), analyzing modal selection and subject coreference."
        ],
        intro_title="Empathy, Grief & Humanitarian Solidarity"
    ))

    # --------------------------------------------------------------------------
    # Lesson 3: b2-06-03 - Exclamaciones evaluativas y matrices afectivas
    # --------------------------------------------------------------------------
    l3 = "b2-06-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.06.03",
        "lesson": l3,
        "title": "Valoración exclamativa y vehemencia",
        "theme": "Estructuras exclamativas, desahogo emotivo y juicio axiológico",
        "words": [
            {"lemma": "inaudito", "translation": "unheard of, unprecedented", "pos": "adjective"},
            {"lemma": "la indignación", "translation": "indignation, outrage", "pos": "noun"},
            {"lemma": "vergonzoso", "translation": "shameful, disgraceful", "pos": "adjective"},
            {"lemma": "la paradoja", "translation": "paradox", "pos": "noun"},
            {"lemma": "clamoroso", "translation": "clamorous, resounding", "pos": "adjective"},
            {"lemma": "desgarrador", "translation": "heartbreaking, harrowing", "pos": "adjective"},
            {"lemma": "el oprobio", "translation": "opprobrium, disgrace", "pos": "noun"},
            {"lemma": "inaudible", "translation": "inaudible", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.06.03.exclamativas-evaluativas",
        "title": "Estructuras exclamativas y matrices afectivas con subjuntivo",
        "sections": [
            {
                "type": "text",
                "title": "Construcciones ponderativas y exclamativas con 'que'",
                "content": "Las expresiones de valoración afectiva enfática adoptan a menudo la forma exclamativa en el discurso apasionado o editorial: '¡Qué lástima que + subjuntivo!', '¡Es una vergüenza que + subjuntivo!', '¡Qué tristeza que + subjuntivo!'. Al tratarse de juicios de valor afectivo sobre una situación presupuesta, el verbo subordinado se formula obligatoriamente en subjuntivo. Por el contrario, la fórmula de alivio '¡Menos mal que...!' rige indicativo, porque asevera con gratitud la consumación real y positiva de un hecho: '¡Menos mal que no llovió!'."
            },
            {
                "type": "table",
                "title": "Contraste en exclamativas evaluativas",
                "rows": [
                    ["¡Qué pena / lástima que + SUBJUNTIVO!", "'¡Qué lástima que hayan cancelado el concierto de gala!'"],
                    ["¡Es una vergüenza / un escándalo que + SUBJUNTIVO!", "'¡Es una vergüenza que los fondos públicos se despilfarren de ese modo!'"],
                    ["¡Qué bueno / maravilloso que + SUBJUNTIVO!", "'¡Qué bueno que la verdad haya salido a la luz!'"],
                    ["¡Menos mal que + INDICATIVO! (alivio/gratitud)", "'¡Menos mal que el médico llegó a tiempo y controló la crisis!'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo de opinión",
                "items": [
                    {"spanish": "¡Qué desgarrador que tantas familias continúen buscando a sus seres queridos sin respuesta estatal!", "english": "How heartbreaking that so many families continue searching for their loved ones without a state response!"},
                    {"spanish": "¡Es inaudito que una nación con semejante fertilidad agrícola sufra desnutrición infantil!", "english": "It is unheard of that a nation with such agricultural fertility suffers infant malnutrition!"},
                    {"spanish": "¡Menos mal que la sociedad civil se organizó con rapidez para brindar socorro a los afectados!", "english": "Thank goodness civil society organized quickly to provide relief to those affected!"}
                ]
            },
            {
                "type": "tip",
                "content": "Acuérdate de la excepción notable: 'Menos mal que' siempre va con indicativo en español culto ('Menos mal que estás aquí', nunca '*Menos mal que estés aquí*')."
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
                    ["inaudito", "unheard of, unprecedented"],
                    ["desgarrador", "heartbreaking, harrowing"],
                    ["el oprobio", "opprobrium, disgrace"],
                    ["vergonzoso", "shameful, disgraceful"]
                ],
                "teaches": ["b2-unit06-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes expresiones exclamativas exige MODO INDICATIVO en lugar de subjuntivo?",
                "options": [
                    "¡Menos mal que...!",
                    "¡Qué lástima que...!",
                    "¡Es una vergüenza que...!"
                ],
                "correct": 0,
                "teaches": ["exclamativas-evaluativas-subjuntivo"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "¡Qué indignante que los responsables __ impunes ante la justicia! (quedar)",
                "answer": "queden",
                "english": "How outrageous that the culprits remain unpunished before justice!",
                "teaches": ["exclamativas-evaluativas-subjuntivo"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["¡Qué", "tristeza", "que", "hayan", "destruido", "ese", "patrimonio", "histórico!"],
                "solution": ["¡Qué", "tristeza", "que", "hayan", "destruido", "ese", "patrimonio", "histórico!"],
                "english": "What a sadness that they have destroyed that historical heritage!",
                "teaches": ["exclamativas-evaluativas-subjuntivo"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ciudadana indignada", "text": "¿Viste cómo concluyó la audiencia preliminar del caso de corrupción?"},
                    {"speaker": "Abogado", "text": "_____"},
                    {"speaker": "Ciudadana indignada", "text": "Es un auténtico insulto a la decencia cívica."}
                ],
                "options": [
                    "¡Es un verdadero oprobio que los jueces desestimen pruebas tan contundentes sin justificación alguna!",
                    "La audiencia comenzó a las nueve y media de la mañana en la sala tres.",
                    "El código penal fue reformado por última vez hace cinco años."
                ],
                "correct": 0,
                "teaches": ["exclamativas-evaluativas-subjuntivo"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "¡Menos mal que los vecinos rescataron a tiempo los documentos históricos de la inundación!",
                "english": "Thank goodness the neighbors rescued the historical documents from the flood in time!",
                "teaches": ["exclamativas-evaluativas-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=6,
        title="Exclamaciones evaluativas y matrices afectivas",
        goal="Express strong evaluative indignation, grief, and relief using affective exclamatory patterns with subjunctive and indicative contrasts.",
        grammar_desc="construcciones exclamativas afectivas ('¡Qué lástima que!', '¡Es una vergüenza que!') y la excepción de '¡Menos mal que!'",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Master exclamatory evaluation frames with obligatory subjunctive complements.",
            "Identify the indicative relief exception in '¡Menos mal que...!'.",
            "Incorporate vehement rhetorical vocabulary (inaudito, oprobio, desgarrador, clamoroso)."
        ],
        intro_body=[
            "When discourse demands passion, moral evaluation, or dramatic relief, exclamatory syntax provides the necessary rhetorical punch.",
            "In this lesson, we study evaluative exclamation frames like '¡Qué lástima que...!' and '¡Es un oprobio que...!', mastering the modal contrast with '¡Menos mal que...!'."
        ],
        intro_title="Evaluative Exclamations & Affective Stance"
    ))

    # --------------------------------------------------------------------------
    # Lesson 4: b2-06-04 - La construcción 'El hecho de que...'
    # --------------------------------------------------------------------------
    l4 = "b2-06-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.06.04",
        "lesson": l4,
        "title": "Nominalización y tematización discursiva",
        "theme": "Evaluación de hechos conocidos y estructuras tematizadoras",
        "words": [
            {"lemma": "el precedente", "translation": "precedent", "pos": "noun"},
            {"lemma": "minimizar", "translation": "to downplay, to minimize", "pos": "verb"},
            {"lemma": "legitimar", "translation": "to legitimize", "pos": "verb"},
            {"lemma": "el síntoma", "translation": "symptom, sign", "pos": "noun"},
            {"lemma": "agravar", "translation": "to aggravate, to worsen", "pos": "verb"},
            {"lemma": "la gravedad", "translation": "gravity, seriousness", "pos": "noun"},
            {"lemma": "el agravio", "translation": "offense, grievance", "pos": "noun"},
            {"lemma": "conllevar", "translation": "to entail, to imply", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.06.04.el-hecho-de-que",
        "title": "Subjuntivo e indicativo con 'el hecho de que'",
        "sections": [
            {
                "type": "text",
                "title": "Tematización de hechos reales y selección modal",
                "content": "La fórmula 'el hecho de que' es el recurso formal por excelencia para tematizar un hecho conocido (colocarlo como sujeto o punto de partida de la oración) y someterlo a comentario, evaluación axiológica o juicio causal: 'El hecho de que las partes dialoguen es una señal esperanzadora'. En el español formal contemporáneo, 'el hecho de que' rige predominantemente SUBJUNTIVO cuando la proposición introduce un hecho que se da por consabido, no para informarlo de nuevo, sino para evaluarlo: 'El hecho de que el acusado se negara a declarar no prueba su culpabilidad'."
            },
            {
                "type": "table",
                "title": "Selección modal con 'el hecho de que'",
                "rows": [
                    ["el hecho de que + SUBJUNTIVO (norma culta general)", "Tematización evaluativa de un hecho admitido: 'El hecho de que hayan ganado no justifica la soberbia'"],
                    ["el hecho de que + INDICATIVO (énfasis factual enfático)", "Invocación apodíctica de un dato incuestionable: 'El hecho de que todos somos iguales ante la ley...'"],
                    ["Negación de la relevancia", "'El hecho de que no responda no significa que esté de acuerdo' (subjuntivo obligatorio)"],
                    ["Función como sujeto preverbal", "'El hecho de que persista la pobreza nos interpela a todos'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo crítico",
                "items": [
                    {"spanish": "El hecho de que el país cuente con abundantes recursos hídricos no garantiza el acceso equitativo al agua potable.", "english": "The fact that the country has abundant water resources does not guarantee equitable access to drinking water."},
                    {"spanish": "El hecho de que hayan firmado la paz no borra el dolor de las víctimas ni agota la necesidad de justicia.", "english": "The fact that they have signed peace does not erase the pain of the victims nor exhaust the need for justice."},
                    {"spanish": "Que se minimice la crisis no mitiga su extrema gravedad económica.", "english": "That the crisis is minimized does not mitigate its extreme economic gravity."}
                ]
            },
            {
                "type": "tip",
                "content": "En la prosa académica B2, anteponer 'El hecho de que + subjuntivo' al inicio del párrafo permite resumir elegantemente el argumento anterior antes de refutarlo o complementarlo."
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
                    ["el precedente", "precedent"],
                    ["minimizar", "to downplay, to minimize"],
                    ["legitimar", "to legitimize"],
                    ["conllevar", "to entail, to imply"]
                ],
                "teaches": ["b2-unit06-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la locución tematizadora 'el hecho de que' rige habitualmente modo subjuntivo en español formal?",
                "options": [
                    "Porque tematiza una información ya conocida para convertirla en objeto de evaluación, sin carácter asertivo primario.",
                    "Porque expresa un deseo imposible en el futuro.",
                    "Porque es un marcador temporal que equivale a 'antes de que'."
                ],
                "correct": 0,
                "teaches": ["el-hecho-de-que-subjuntivo"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El hecho de que la economía __ no significa que los salarios hayan recuperado su poder adquisitivo. (crecer)",
                "answer": "crezca",
                "english": "The fact that the economy grows does not mean that wages have recovered their purchasing power.",
                "teaches": ["el-hecho-de-que-subjuntivo"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "hecho", "de", "que", "hayan", "firmado", "no", "garantiza", "la", "paz."],
                "solution": ["El", "hecho", "de", "que", "hayan", "firmado", "no", "garantiza", "la", "paz."],
                "english": "The fact that they have signed does not guarantee peace.",
                "teaches": ["el-hecho-de-que-subjuntivo"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿No considera usted que el aumento de exportaciones convalida la política del ministerio?"},
                    {"speaker": "Economista crítica", "text": "_____"},
                    {"speaker": "Periodista", "text": "Es una advertencia muy pertinente sobre la concentración de la riqueza."}
                ],
                "options": [
                    "El hecho de que las exportaciones aumenten no significa en absoluto que los beneficios se distribuyan equitativamente entre los trabajadores.",
                    "Los puertos marítimos cuentan con silos de almacenamiento de grano.",
                    "La tasa de cambio oficial se publica diariamente en el portal del banco central."
                ],
                "correct": 0,
                "teaches": ["el-hecho-de-que-subjuntivo"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El hecho de que no haya habido denuncias previas no minimiza la gravedad de lo sucedido.",
                "english": "The fact that there have been no previous complaints does not downplay the gravity of what happened.",
                "teaches": ["el-hecho-de-que-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=6,
        title="La construcción 'El hecho de que...'",
        goal="Master discursive topic-framing and evaluation of known facts using the nominalized structure 'el hecho de que' with the subjunctive.",
        grammar_desc="el modo subjuntivo con la locución tematizadora 'el hecho de que' en la prosa ensayística",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Thematize pre-existing premises in academic essays using 'el hecho de que' + subjunctive.",
            "Formulate counter-arguments denying logical consequence ('el hecho de que X no implica Y').",
            "Incorporate analytical essay vocabulary (conllevar, minimizar, legitimar, precedente)."
        ],
        intro_body=[
            "Advanced essay writing frequently requires summarizing a known reality to scrutinize its implications.",
            "In this lesson, we study the nominalized topic-setting construction 'el hecho de que', examining why the subjunctive is standard in formal evaluation."
        ],
        intro_title="Discursive Thematization: 'El hecho de que...'"
    ))

    # --------------------------------------------------------------------------
    # Lesson 5: b2-06-05 - Indignación moral, diplomacia humanitaria y retórica afectiva
    # --------------------------------------------------------------------------
    l5 = "b2-06-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.06.05",
        "lesson": l5,
        "title": "Ética pública y diplomacia humanitaria",
        "theme": "Denuncia de abusos, mediación humanitaria e indignación cívica",
        "words": [
            {"lemma": "intolerable", "translation": "intolerable, unbearable", "pos": "adjective"},
            {"lemma": "la vejación", "translation": "harassment, mistreatment, vexation", "pos": "noun"},
            {"lemma": "conculcar", "translation": "to infringe, to violate (rights)", "pos": "verb"},
            {"lemma": "el desamparo", "translation": "helplessness, abandonment", "pos": "noun"},
            {"lemma": "la indignidad", "translation": "indignity, unworthiness", "pos": "noun"},
            {"lemma": "repudiar", "translation": "to repudiate, to condemn", "pos": "verb"},
            {"lemma": "flagrante", "translation": "flagrant, blatant", "pos": "adjective"},
            {"lemma": "el atropello", "translation": "abuse of power, outrage", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.06.05.integracion-retorica-afectiva",
        "title": "Integración discursiva: Reacción afectiva, vehemencia ética y evaluación en el manifiesto social",
        "sections": [
            {
                "type": "text",
                "title": "Síntesis de posicionamiento ético y afectivo",
                "content": "La redacción de manifiestos cívicos, editoriales periodísticos y declaraciones de derechos humanos de nivel B2 moviliza toda la gama de estructuras afectivas: verbos de afección psíquica para expresar desasosiego ('nos indigna que'), fórmulas de pesar para manifestar duelo ('deploramos que'), exclamaciones valorativas para conmover a la audiencia ('¡es un atropello que!') y nominalizaciones tematizadoras ('el hecho de que persista el oprobio'). Esta síntesis otorga a la prosa un poderoso vigor moral sin perder el rigor sintáctico."
            },
            {
                "type": "examples",
                "title": "Modelos sintácticos en el manifiesto cívico",
                "items": [
                    {"spanish": "A la ciudadanía consciente le duele que se conculquen las libertades públicas más elementales.", "english": "It pains the conscious citizenry that the most elementary civil liberties are infringed."},
                    {"spanish": "¡Qué paradoja desgarradora que quienes defienden el territorio sean criminalizados!", "english": "What a heartbreaking paradox that those who defend the territory are criminalized!"},
                    {"spanish": "El hecho de que las autoridades guarden silencio no neutraliza el clamor popular de desagravio.", "english": "The fact that authorities keep silent does not neutralize the popular clamor for redress."}
                ]
            },
            {
                "type": "tip",
                "content": "Para dotar de sobriedad a la indignación vehemente, intercala oraciones nominales con adjetivos cultos: 'Flagrante atropello a la soberanía popular', 'Inadmisible vejación contra la dignidad humana'."
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
                    ["la vejación", "mistreatment, harassment"],
                    ["conculcar", "to infringe, to violate rights"],
                    ["el desamparo", "helplessness, abandonment"],
                    ["el atropello", "abuse of power, outrage"]
                ],
                "teaches": ["b2-unit06-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué combinación modal refleja mayor corrección en un comunicado de derechos humanos?",
                "options": [
                    "Nos indigna que se conculquen los derechos fundamentales; el hecho de que ocurra en democracia agrava la situación.",
                    "Nos indigna que se conculcan los derechos fundamentales; el hecho de que ocurre en democracia agrava la situación.",
                    "Nos indignamos de que se conculquen los derechos; el hecho de que ocurriría es un problema."
                ],
                "correct": 0,
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Deploramos que las fuerzas estatales __ la autonomía de las comunidades campesinas. (vulnerar)",
                "answer": "vulneren",
                "english": "We deplore that state forces violate the autonomy of peasant communities.",
                "teaches": ["empatia-pesar-subjuntivo"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "hecho", "de", "que", "callen", "no", "borra", "el", "atropello."],
                "solution": ["El", "hecho", "de", "que", "callen", "no", "borra", "el", "atropello."],
                "english": "The fact that they stay silent does not erase the abuse of power.",
                "teaches": ["el-hecho-de-que-subjuntivo"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista internacional", "text": "¿Cómo califica el informe anual de derechos humanos la respuesta estatal ante la protesta social?"},
                    {"speaker": "Relatora especial", "text": "_____"},
                    {"speaker": "Periodista internacional", "text": "Un llamado urgente a la comunidad jurídica internacional."}
                ],
                "options": [
                    "Nos consterna que se criminalice la disidencia pacífica y repudiamos que se conculquen las garantías constitucionales más elementales.",
                    "El informe se distribuye en formato PDF de acceso abierto en internet.",
                    "La sede central del tribunal de arbitraje se encuentra en La Haya."
                ],
                "correct": 0,
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "¡Es un flagrante atropello que las víctimas del despojo no hayan recibido ninguna reparación moral!",
                "english": "It is a flagrant outrage that the victims of dispossession have not received any moral reparation!",
                "teaches": ["exclamativas-evaluativas-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=6,
        title="Indignación moral, diplomacia humanitaria y retórica afectiva",
        goal="Synthesize psychological affect, ethical grief, evaluative exclamations, and topic-thematization in civic manifestos and human rights advocacy.",
        grammar_desc="integración de posicionamiento ético, retórica de indignación y valoración axiológica",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Combine affective verbs and evaluative exclamations in powerful advocacy prose.",
            "Deploy human rights legal terminology (conculcar, vejación, atropello, flagrante).",
            "Maintain grammatical coherence across multi-clause ethical critiques."
        ]
    ))

    # --------------------------------------------------------------------------
    # Story: stories/classics/b2/b2-06.json (Eduardo Galeano: Las venas abiertas de América Latina)
    # --------------------------------------------------------------------------
    write_json("stories/classics/b2/b2-06.json", {
        "id": "story.b2.06.galeano",
        "title": "Eduardo Galeano: Indignación moral y las venas abiertas de la memoria",
        "level": "B2",
        "author": "Eduardo Galeano (Uruguay, 1940–2015)",
        "work": "Las venas abiertas de América Latina",
        "summary": "Una reflexión sobre la obra emblemática de Eduardo Galeano, su prosa ardiente contra el saqueo colonial e imperial de la región, y la dignidad de los pueblos que transforman el dolor en resistencia viva.",
        "vocabularyTopics": ["Crónica política e histórica", "Indignación moral y colonialismo", "Memoria de los pueblos saqueados"],
        "grammar": ["verbos de afección psicológica", "exclamativas evaluativas", "el hecho de que con subjuntivo"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Publicada en 1971 en vísperas de las dictaduras militares del Cono Sur, 'Las venas abiertas de América Latina' de Eduardo Galeano no es un árido inventario de estadísticas macroeconómicas; es una crónica apasionada escrita desde la entraña de la indignación moral. Con una prosa poética y mordaz que funde el rigor histórico con el latido del ensayo lírico, Galeano reconstruye cinco siglos de saqueo sistemático en el continente."
            },
            {
                "type": "narration",
                "text": "Al lector le estremece comprobar cómo la riqueza natural de una comarca se transformó invariablemente en la causa directa de su miseria: la plata fulgurante del Cerro Rico de Potosí que desangró a millones de mitayos indígenas; el azúcar amargo del Caribe y del nordeste brasileño cultivado sobre las espaldas de esclavos africanos; y el oro negro de las petroleras transnacionales en Venezuela y la Amazonía. ¡Qué trágica paradoja que el suelo más fértil y pródigo del planeta haya albergado históricamente a las poblaciones más desamparadas!"
            },
            {
                "type": "narration",
                "text": "No obstante, Galeano rehúsa entregarse a la resignación impotente. El hecho de que la historia latinoamericana haya sido una carrera de despojos no significa que su destino esté fatalmente sellado por la derrota. En cada página, el escritor uruguayo reivindica la memoria insumisa de los vencidos, recordándonos que recordar el dolor del pasado es el primer paso indispensable para recuperar la soberanía sobre nuestro propio futuro."
            }
        ]
    })

    # --------------------------------------------------------------------------
    # Lesson 6: b2-06-consolidation
    # --------------------------------------------------------------------------
    l_con = "b2-06-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["inquietar", "to worry, to disquiet"],
                    ["deplorar", "to deplore, to lament deeply"],
                    ["inaudito", "unheard of, unprecedented"],
                    ["conculcar", "to violate, to infringe rights"]
                ],
                "teaches": ["b2-unit06-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿En cuál de las siguientes opciones se utiliza incorrectamente el modo verbal?",
                "options": [
                    "¡Menos mal que llegues a tiempo para la reunión!",
                    "Nos indigna que se toleren semejantes abusos institucionales.",
                    "El hecho de que hayan ganado no significa que tengan la razón."
                ],
                "correct": 0,
                "teaches": ["exclamativas-evaluativas-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se comporta la concordancia del verbo de afección psíquica cuando el sujeto sintáctico es una proposición introducida por 'que'?",
                "options": [
                    "Se conjuga en tercera persona singular (nos preocupa que...), sin importar el número de personas afectadas.",
                    "Debe concordar en plural si el pronombre de objeto indirecto es 'nos' o 'les'.",
                    "Adopta forma impersonal con el pronombre 'se' obligatoriamente."
                ],
                "correct": 0,
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A los ciudadanos les asombra que el gobierno __ los informes técnicos sobre el impacto ambiental. (desoír)",
                "answer": "desoiga",
                "english": "It astounds citizens that the government ignores technical reports on environmental impact.",
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "A la sociedad civil le indigna que persista la opacidad en las instituciones públicas. [Civil society is outraged that opacity persists in public institutions.]",
                    "Lamentamos profundamente que el desastre natural haya dejado a tantas familias sin hogar. [We deeply regret that the natural disaster left so many families homeless.]",
                    "¡Es un flagrante atropello que se vulnere la libertad de expresión de los periodistas! [It is a flagrant outrage that journalists' freedom of expression is violated!]",
                    "El hecho de que el país sea pródigo en recursos no garantiza una distribución equitativa. [The fact that the country is bountiful in resources does not guarantee equitable distribution.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": ["afeccion-psicologica-subjuntivo", "empatia-pesar-subjuntivo", "exclamativas-evaluativas-subjuntivo", "el-hecho-de-que-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Por qué la obra de Eduardo Galeano sigue despertando tanta conmoción ética más de medio siglo después?"},
                    {"speaker": "Ensayista", "text": "_____"},
                    {"speaker": "Historiador", "text": "Una prosa que transforma la herida de la historia en esperanza insumisa."}
                ],
                "options": [
                    "Porque al lector le conmueve que Galeano haya rescatado la memoria viva de los despojados con una vehemencia moral inquebrantable.",
                    "Porque las minas de plata de Potosí se encuentran a más de cuatro mil metros sobre el nivel del mar.",
                    "Porque las ediciones de bolsillo del libro suelen encuadernarse en tapa blanda."
                ],
                "correct": 0,
                "teaches": ["afeccion-psicologica-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Deploramos que las advertencias de los científicos hayan sido minimizadas durante tanto tiempo.",
                "english": "We deplore that scientists' warnings have been downplayed for so long.",
                "teaches": ["empatia-pesar-subjuntivo"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Escribe una frase de indignación cívica combinando un verbo de afección psicológica y la construcción 'el hecho de que' con subjuntivo.",
                        "answer": "Nos indigna que las autoridades toleren la impunidad; el hecho de que no investiguen los atropellos agrava la crisis."
                    }
                ],
                "teaches": ["afeccion-psicologica-subjuntivo", "el-hecho-de-que-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=6,
        title="Unit 6 Consolidation",
        goal="Consolidate affective stance, psychological concern, diplomatic empathy, evaluative exclamations, and topic-thematization with 'el hecho de que'.",
        grammar_desc="síntesis de afección psicológica, empatía, exclamativas afectivas y la construcción 'el hecho de que'",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Govern subjunctive complements after dative affective verbs (inquietar, preocupar, indignar).",
            "Express humanitarian condolences with verbs of feeling (lamentar, deplorar, dolerse).",
            "Construct evaluative exclamations ('¡Qué lástima que!') and contrast with '¡Menos mal que!'.",
            "Thematize pre-existing facts with 'el hecho de que' + subjunctive in essays.",
            "Analyze literary excerpts from Eduardo Galeano's 'Las venas abiertas de América Latina'."
        ],
        checklist_items=[
            "I can use psychological affect verbs with dative pronouns and subjunctive subject clauses.",
            "I can express grief and diplomatic empathy using 'lamentar que' and 'deplorar que'.",
            "I can formulate evaluative exclamations and apply the indicative exception of 'menos mal que'.",
            "I can use 'el hecho de que' with the subjunctive to thematize and critique known realities."
        ],
        story_ref="stories/classics/b2/b2-06.json"
    ))
    print("Completed Core Unit 6 generation!")


if __name__ == "__main__":
    generate_core_unit_6()
