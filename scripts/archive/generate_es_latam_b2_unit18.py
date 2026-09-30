#!/usr/bin/env python3
"""
Generate complete curriculum content for Latin American Spanish (es-latam)
B2 Unit Pair 18:
- Core Unit 18: b2-18 (Rhetorical Reporting Verbs / Verbos de comunicación y atribución retórica)
- Regional Unit 18: b2-peruandino (Peru I: Cusco, Tawantinsuyu & Andean Worldview)

Adheres strictly to all schemas:
- Vocabulary schema: id, lesson, title, words [{lemma, translation, pos}]
- Grammar schema: 2-column tables (rows: [[es, en], ...]), no headers
- Exercise schema: matching, fill-blank, multiple-choice, sentence-builder, dialogue-complete, dictation
- Lesson schema: id, level, title, goal, grammar, sections
- Story schema: id, title, level, lesson, type, estimatedMinutes, summary, characters,
  paragraphs: [{"type": "narration", "text": p}],
  narration: {"pedagogical": {"comprehensionQuestions": [...]}}
- Word counts: strictly 650 - 825 words (~700 words) audited programmatically
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LATAM_DIR = ROOT / "content" / "es-latam"

def write_json(rel_path, data):
    p = LATAM_DIR / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {p.relative_to(ROOT)}")

def count_words(text):
    return len(text.split())

def main():
    # -------------------------------------------------------------------------
    # 1. Skill Registry & Grammar Titles Updates
    # -------------------------------------------------------------------------
    reg_path = LATAM_DIR / "indexes" / "skill-registry.json"
    reg = json.loads(reg_path.read_text(encoding="utf-8")) if reg_path.is_file() else {"skills": {}}
    
    new_skills = {
        # Core Unit 18 skills
        "b2-18-vocab": {
            "kind": "vocabulary",
            "level": "b2",
            "name": "Rhetorical Reporting Verbs Vocabulary"
        },
        "verbos-comunicacion-aseverativos": {
            "kind": "grammar",
            "level": "b2",
            "name": "Assertive Reporting Verbs in Formal Discourse"
        },
        "verbos-comunicacion-disputa-refutacion": {
            "kind": "grammar",
            "level": "b2",
            "name": "Dispute & Refutation Verbs in Debate"
        },
        "verbos-comunicacion-advertencia-recordatorio": {
            "kind": "grammar",
            "level": "b2",
            "name": "Warning & Reminder Verbs in Attributions"
        },
        "verbos-comunicacion-reproche-critica": {
            "kind": "grammar",
            "level": "b2",
            "name": "Reproach & Critique Verbs in Analysis"
        },
        "verbos-comunicacion-subjetividad-conjetura": {
            "kind": "grammar",
            "level": "b2",
            "name": "Conjecture & Subjective Stance Reporting Verbs"
        },
        # Regional Unit 18 (Peru I - Andean) skills
        "b2-peruandino-vocab": {
            "kind": "vocabulary",
            "level": "b2",
            "name": "Andean Peruvian Culture & Geography Vocabulary"
        },
        "peru-cordillera-blanca-glaciares": {
            "kind": "grammar",
            "level": "b2",
            "name": "Glacial Geography & High-Altitude Hydrology"
        },
        "peru-civilizaciones-preincas-caral": {
            "kind": "grammar",
            "level": "b2",
            "name": "Pre-Inca Civilizations & Ancient Architecture"
        },
        "peru-tawantinsuyu-qhapaq-nan": {
            "kind": "grammar",
            "level": "b2",
            "name": "Imperial Administration & Road Networks"
        },
        "peru-cusco-escuela-cusquena-sincretismo": {
            "kind": "grammar",
            "level": "b2",
            "name": "Colonial Art & Cultural Syncretism"
        },
        "peru-quechua-vitalidad-linguistica": {
            "kind": "grammar",
            "level": "b2",
            "name": "Linguistic Vitality & Contemporary Quechua Literature"
        }
    }
    
    reg["skills"].update(new_skills)
    reg_path.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated skill-registry.json for Unit 18")

    # Grammar titles for Grammar Driller (starts lowercase, <= 11 words, plain CEFR English, no unauthorized caps)
    titles_path = LATAM_DIR / "indexes" / "grammar-titles.json"
    titles = json.loads(titles_path.read_text(encoding="utf-8")) if titles_path.is_file() else {}
    
    new_titles = {
        "verbos-comunicacion-aseverativos": "reporting statements with assertive communication verbs",
        "verbos-comunicacion-disputa-refutacion": "reporting arguments with dispute and refutation verbs",
        "verbos-comunicacion-advertencia-recordatorio": "reporting warnings and reminders with specialized communication verbs",
        "verbos-comunicacion-reproche-critica": "reporting critical feedback and reproaches with communicative verbs",
        "verbos-comunicacion-subjetividad-conjetura": "reporting conjectures and subjective claims in formal discourse",
        "peru-cordillera-blanca-glaciares": "glacial geography and high-altitude hydrology in mountain ranges",
        "peru-civilizaciones-preincas-caral": "pre-Inca civilizations and ancient architecture in coastal valleys",
        "peru-tawantinsuyu-qhapaq-nan": "imperial administration and road networks in ancient societies",
        "peru-cusco-escuela-cusquena-sincretismo": "colonial religious art and cultural syncretism in painting",
        "peru-quechua-vitalidad-linguistica": "linguistic vitality and contemporary literature in indigenous languages"
    }
    titles.update(new_titles)
    titles_path.write_text(json.dumps(titles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json for Unit 18")

    # -------------------------------------------------------------------------
    # 2. CORE UNIT 18: b2-18 (Rhetorical Reporting Verbs)
    # -------------------------------------------------------------------------
    c_unit = "b2-18"

    # --- Lesson 1: b2-18-01 ---
    l1 = f"{c_unit}-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.18.01",
        "lesson": l1,
        "title": "Verbos declarativos y aseverativos formales",
        "theme": "Léxico de aseveración categórica, argumentación formal y rigor discursivo",
        "words": [
            {"lemma": "aseverar", "translation": "to assert firmly, to state as factual", "pos": "verb"},
            {"lemma": "sostener", "translation": "to maintain, to argue a position", "pos": "verb"},
            {"lemma": "puntualizar", "translation": "to point out, to specify in detail", "pos": "verb"},
            {"lemma": "recalcar", "translation": "to emphasize, to stress repeatedly", "pos": "verb"},
            {"lemma": "constatar", "translation": "to verify, to establish as fact", "pos": "verb"},
            {"lemma": "manifestar", "translation": "to express, to state publicly", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.18.01.verbos-comunicacion-aseverativos",
        "title": "Verbos declarativos y aseverativos: precisión en la atribución formal",
        "sections": [
            {
                "type": "text",
                "content": "En el registro formal, periodístico y académico de nivel B2, el uso excesivo del verbo comodín *decir* empobrece la prosa y desdibuja la intención pragmática del emisor. El español culto dispone de una rica batería de **verbos aseverativos y declarativos** que especifican el grado de certeza, la solemnidad o la contundencia con que se formula una afirmación.\n\nVerbos como **aseverar**, **sostener**, **recalcar** o **puntualizar** rigen normalmente proposiciones subordinadas sustantivas en modo indicativo cuando el hablante valida la existencia del hecho informado (*El ministro aseveró que el déficit había disminuido*)."
            },
            {
                "type": "table",
                "title": "Matices de verbos aseverativos formales",
                "rows": [
                    ["aseverar", "to state categorically as absolute truth without room for doubt"],
                    ["sostener", "to defend an argument or thesis tenaciously against opposition"],
                    ["recalcar", "to put heavy emphasis on a crucial detail of the message"],
                    ["puntualizar", "to specify fine distinctions or correct minor inaccuracies"],
                    ["constatar", "to verify objectively that an event has actually transpired"],
                    ["manifestar", "to declare an official position openly in public communiques"]
                ]
            },
            {
                "type": "tip",
                "content": "Observa el régimen preposicional: *sostener que* (sin preposición), *hacer hincapié en que*, *puntualizar que*. Evita el queísmo incorrecto: no digas *'aseveró de que'*, sino *'aseveró que'*."
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
                    ["aseverar", "to affirm as factual truth"],
                    ["sostener", "to maintain a defended thesis"],
                    ["recalcar", "to stress with special emphasis"],
                    ["puntualizar", "to clarify specific nuances"]
                ],
                "teaches": ["b2-18-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En su informe pericial, la ingeniera __ que los cimientos del puente presentaban fallas graves. (aseverar)",
                "answer": "aseveró",
                "english": "In her expert report, the engineer asserted that the bridge foundations showed serious flaws.",
                "teaches": ["verbos-comunicacion-aseverativos"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz pragmático aporta el verbo 'recalcar' frente al neutro 'decir'?",
                "options": [
                    "Indica que el emisor puso especial énfasis y subrayó deliberadamente ese punto concreto.",
                    "Señala que el hablante tenía dudas sobre la veracidad del mensaje transmitido.",
                    "Indica que el mensaje fue pronunciado en voz muy baja y confidencial.",
                    "Expresa que la afirmación fue desmentida minutos después por los testigos."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-aseverativos"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "canciller", "recalcó", "que", "el", "tratado", "garantizaba", "la", "paz."],
                "solution": ["El", "canciller", "recalcó", "que", "el", "tratado", "garantizaba", "la", "paz."],
                "english": "The chancellor stressed that the treaty guaranteed peace.",
                "teaches": ["verbos-comunicacion-aseverativos"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Cómo resumiría la declaración del director del banco central ante la comisión parlamentaria?"},
                    {"speaker": "Analista", "text": "_____"}
                ],
                "options": [
                    "Sostuvo que las reservas monetarias eran sólidas, pero puntualizó que la inflación global exigía prudencia fiscal.",
                    "El edificio del banco central tiene diez pisos y una fachada de mármol gris.",
                    "Los banqueros almorzaron en un restaurante tradicional del centro histórico.",
                    "El precio del café bajó en los mercados internacionales durante el verano."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-aseverativos"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La investigadora constató que los datos climáticos confirmaban el retroceso acelerado de los glaciares andinos.",
                "english": "The researcher verified that the climate data confirmed the accelerated retreat of Andean glaciers.",
                "teaches": ["verbos-comunicacion-aseverativos"]
            }
        ]
    })

    # --- Lesson 2: b2-18-02 ---
    l2 = f"{c_unit}-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.18.02",
        "lesson": l2,
        "title": "Verbos de disputa, refutación y desmentido",
        "theme": "Léxico de controversia judicial, debate parlamentario y réplica dialéctica",
        "words": [
            {"lemma": "desmentir", "translation": "to deny formally, to debunk rumors", "pos": "verb"},
            {"lemma": "refutar", "translation": "to refute, to disprove with evidence", "pos": "verb"},
            {"lemma": "impugnar", "translation": "to contest, to challenge legally", "pos": "verb"},
            {"lemma": "rebatir", "translation": "to rebut, to counter an argument", "pos": "verb"},
            {"lemma": "objetar", "translation": "to object, to raise an exception", "pos": "verb"},
            {"lemma": "contradecir", "translation": "to contradict, to oppose a claim", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.18.02.verbos-comunicacion-disputa-refutacion",
        "title": "Verbos de disputa, refutación y réplica dialéctica",
        "sections": [
            {
                "type": "text",
                "content": "En el debate dialéctico, la controversia judicial y la prensa de investigación, los **verbos de disputa y refutación** permiten estructurar la réplica a las afirmaciones de un adversario. Estos verbos denotan una actitud de oposición activa, rechazo frontal o desarticulación racional de una tesis previa.\n\nEs fundamental distinguir entre **desmentir** (declarar categóricamente que una noticia o rumor es falso), **refutar** o **rebatir** (demostrar con pruebas o razonamientos sólidos la falsedad o invalidez de una tesis) e **impugnar** (cuestionar la validez legal o formal de un acto, elección o documento)."
            },
            {
                "type": "table",
                "title": "Verbos de controversia y sus regímenes sintácticos",
                "rows": [
                    ["desmentir un rumor", "El portavoz desmintió que hubiera habido negociaciones secretas."],
                    ["refutar una hipótesis", "La científica refutó con datos la hipótesis del consorcio minero."],
                    ["rebatir un argumento", "El abogado rebatió punto por punto los alegatos de la fiscalía."],
                    ["impugnar un fallo", "Los campesinos impugnaron la resolución judicial ante el tribunal."],
                    ["objetar una propuesta", "La delegada objetó que el presupuesto ignoraba la educación rural."],
                    ["contradecir un testimonio", "Las grabaciones contradijeron la versión inicial del sospechoso."]
                ]
            },
            {
                "type": "tip",
                "content": "Cuando *desmentir* introduce una cláusula con *que*, puede exigir **modo subjuntivo** si se enfatiza el rechazo de la veracidad del hecho: *Desmintió que hubiera participado en el soborno* (subjuntivo = no ocurrió según el hablante)."
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
                    ["desmentir", "to deny rumors formally"],
                    ["refutar", "to disprove with empirical evidence"],
                    ["impugnar", "to challenge legal validity"],
                    ["rebatir", "to counter opposed arguments"]
                ],
                "teaches": ["b2-18-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El ministerio desmintió categóricamente que se __ privatizar el sistema público de salud. (ir)",
                "answer": "fuera a",
                "english": "The ministry categorically denied that it was going to privatize the public health system.",
                "teaches": ["verbos-comunicacion-disputa-refutacion"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la diferencia conceptual entre 'desmentir' y 'refutar'?",
                "options": [
                    "Desmentir declara que algo es falso; refutar demuestra su falsedad mediante argumentos y pruebas.",
                    "Desmentir se usa únicamente en tribunales y refutar en conversaciones familiares.",
                    "Ambos verbos son completamente idénticos y pueden intercambiarse sin cambio alguno.",
                    "Refutar significa apoyar entusiastamente una propuesta comercial."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-disputa-refutacion"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "comuneros", "impugnaron", "el", "desalojo", "ante", "la", "corte", "superior."],
                "solution": ["Los", "comuneros", "impugnaron", "el", "desalojo", "ante", "la", "corte", "superior."],
                "english": "The community members contested the eviction before the superior court.",
                "teaches": ["verbos-comunicacion-disputa-refutacion"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Fiscal", "text": "¿Cómo reaccionó la defensa ante las pruebas documentales presentadas en el juicio?"},
                    {"speaker": "Secretaria judicial", "text": "_____"}
                ],
                "options": [
                    "El abogado defensor intentó rebatir los peritajes alegando que la cadena de custodia había sido vulnerada.",
                    "El tribunal comenzó la audiencia a las nueve en punto de la mañana.",
                    "El código penal consta de varios cientos de artículos redactados en latín.",
                    "La sala de audiencias cuenta con micrófonos digitales para grabar la voz."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-disputa-refutacion"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La asamblea comunitaria rebatió los argumentos de la corporación minera demostrando el impacto en las fuentes hídricas.",
                "english": "The community assembly rebutted the mining corporation's arguments by proving the impact on water sources.",
                "teaches": ["verbos-comunicacion-disputa-refutacion"]
            }
        ]
    })

    # --- Lesson 3: b2-18-03 ---
    l3 = f"{c_unit}-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.18.03",
        "lesson": l3,
        "title": "Verbos de advertencia, prevención y recordatorio",
        "theme": "Léxico de previsión de riesgos, cautela institucional y recomendaciones",
        "words": [
            {"lemma": "advertir", "translation": "to warn, to caution of danger", "pos": "verb"},
            {"lemma": "prevenir", "translation": "to forewarn, to take preventive measures", "pos": "verb"},
            {"lemma": "alertar", "translation": "to alert, to raise a flag", "pos": "verb"},
            {"lemma": "recordar", "translation": "to remind of an existing obligation", "pos": "verb"},
            {"lemma": "conminar", "translation": "to summon formally under threat of penalty", "pos": "verb"},
            {"lemma": "apercibir", "translation": "to give official admonition/notice", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.18.03.verbos-comunicacion-advertencia-recordatorio",
        "title": "Verbos de advertencia, prevención y recordatorio",
        "sections": [
            {
                "type": "text",
                "content": "Cuando un emisor anticipa un peligro futuro, previene sobre un riesgo inminente o recuerda una obligación legal pendiente, el español culto emplea verbos especializados de advertencia como **advertir**, **alertar**, **prevenir** y **conminar**.\n\nEl verbo **advertir** presenta una interesante bivalencia sintáctica y semántica:\n1. Con **indicativo** significa percibir o comunicar un hecho objetivo (*Nos advirtió que el camino estaba bloqueado*).\n2. Con **subjuntivo** funciona como orden o advertencia imperativa (*Nos advirtió que no cruzáramos el río crecido*)."
            },
            {
                "type": "table",
                "title": "Verbos de advertencia y sus regímenes",
                "rows": [
                    ["advertir (de) que + ind.", "Los meteorólogos advirtieron que la tormenta llegaría esa noche."],
                    ["advertir que + subj.", "El guía nos advirtió que tuviéramos prudencia en el precipicio."],
                    ["alertar sobre / de que", "La comunidad alertó sobre la presencia de taladores ilegales."],
                    ["recordar que + ind.", "El juez recordó que el plazo de apelación vencía el viernes."],
                    ["conminar a que + subj.", "El prefecto conminó a la empresa a que suspendiera las obras."],
                    ["prevenir contra / de", "Los ancianos previnieron a los jóvenes de no perder la memoria ancestral."]
                ]
            },
            {
                "type": "tip",
                "content": "Con el verbo *advertir* con sentido de advertencia de riesgo, tanto *advertir que* como *advertir de que* son construcciones admitidas por la Real Academia Española (*advirtió de que era peligroso* = *advirtió que era peligroso*)."
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
                    ["advertir", "to caution of impending risk"],
                    ["alertar", "to sound the alarm on hazards"],
                    ["recordar", "to bring to mind an obligation"],
                    ["conminar", "to demand compliance under penalty"]
                ],
                "teaches": ["b2-18-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El guardaparque nos advirtió que no nos __ del sendero señalizado en la montaña. (desviar)",
                "answer": "desviáramos",
                "english": "The park ranger warned us not to stray from the marked trail on the mountain.",
                "teaches": ["verbos-comunicacion-advertencia-recordatorio"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué diferencia de significado existe entre 'Advirtió que salían temprano' y 'Advirtió que salieran temprano'?",
                "options": [
                    "La primera informa sobre un hecho (indicativo); la segunda formula una advertencia o mandato imperativo (subjuntivo).",
                    "La primera expresa una duda existencial y la segunda una certeza matemática.",
                    "La primera se refiere al pasado y la segunda obligatoriamente al siglo diecinueve.",
                    "Ninguna; ambas oraciones son exactamente intercambiables en todos los contextos."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-advertencia-recordatorio"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "geólogos", "alertaron", "de", "que", "el", "volcán", "podía", "entrar", "en", "erupción."],
                "solution": ["Los", "geólogos", "alertaron", "de", "que", "el", "volcán", "podía", "entrar", "en", "erupción."],
                "english": "The geologists warned that the volcano could erupt.",
                "teaches": ["verbos-comunicacion-advertencia-recordatorio"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Alcaldesa", "text": "¿Qué medida cautelar adoptó el comité de emergencia tras el informe sobre la crecida del río?"},
                    {"speaker": "Director de Protección Civil", "text": "_____"}
                ],
                "options": [
                    "Conminamos a las poblaciones de las riberas bajas a que evacuaran preventivamente hacia zonas altas.",
                    "Los ríos andinos nacen en los deshielos de las cumbres nevadas.",
                    "Compramos nuevos escritorios de madera para la oficina de turismo municipal.",
                    "El agua potable contiene sales minerales disueltas en cantidades moderadas."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-advertencia-recordatorio"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El tribunal recordó a las partes litigantes que el desacato a la resolución acarrearía severas sanciones penales.",
                "english": "The court reminded the litigating parties that contempt of the ruling would entail severe criminal penalties.",
                "teaches": ["verbos-comunicacion-advertencia-recordatorio"]
            }
        ]
    })

    # --- Lesson 4: b2-18-04 ---
    l4 = f"{c_unit}-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.18.04",
        "lesson": l4,
        "title": "Verbos de reproche, censura y crítica discursiva",
        "theme": "Léxico de denuncia social, crítica política y reprobación ética",
        "words": [
            {"lemma": "reprochar", "translation": "to reproach, to blame for an error", "pos": "verb"},
            {"lemma": "censurar", "translation": "to censure, to condemn publicly", "pos": "verb"},
            {"lemma": "recriminar", "translation": "to recriminate, to counter-blame", "pos": "verb"},
            {"lemma": "cuestionar", "translation": "to question, to dispute integrity", "pos": "verb"},
            {"lemma": "denunciar", "translation": "to denounce, to expose wrongdoing", "pos": "verb"},
            {"lemma": "increpar", "translation": "to scold sharply, to call out angrily", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.18.04.verbos-comunicacion-reproche-critica",
        "title": "Verbos de reproche, censura y evaluación crítica",
        "sections": [
            {
                "type": "text",
                "content": "En el análisis crítico, los debates parlamentarios y la literatura de denuncia social (como las novelas indigenistas de Ciro Alegría), los **verbos de reproche y censura** permiten reportar acusaciones morales, señalamientos éticos o desaprobaciones explícitas de conductas pasadas.\n\nVerbos como **reprochar**, **recriminar** y **censurar** construyen cláusulas subordinadas sustantivas donde el emisor juzga retrospectivamente una falta, negligencia o injusticia cometida por su contraparte (*Le reprochó que no hubiera defendido a la comunidad*)."
            },
            {
                "type": "table",
                "title": "Estructuras de reproche y crítica",
                "rows": [
                    ["reprochar (a alguien) que + subj.", "Los comuneros le reprocharon al alcalde que hubiera pactado con el patrón."],
                    ["recriminar (a alguien) por + inf.", "El juez le recriminó por haber falsificado los títulos de propiedad."],
                    ["censurar la conducta de", "La prensa independiente censuró la pasividad del gobierno ante la violencia."],
                    ["cuestionar la legitimidad de", "Los líderes andinos cuestionaron que el tribunal fallara a espaldas del pueblo."],
                    ["denunciar que + ind.", "Los campesinos denunciaron que los guardias habían incendiado las cosechas."],
                    ["increpar a viva voz", "El dirigente increpó al terrateniente exigiéndole respeto para los ancianos."]
                ]
            },
            {
                "type": "tip",
                "content": "Observa que *reprochar que* rige habitualmente **subjuntivo** porque el emisor no se limita a comunicar un hecho, sino que proyecta sobre él una valoración afectiva de censura moral: *Me reprochó que llegara tarde*."
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
                    ["reprochar", "to blame someone for moral failure"],
                    ["censurar", "to condemn unethical behavior"],
                    ["cuestionar", "to doubt legitimacy or truth"],
                    ["increpar", "to confront and scold angrily"]
                ],
                "teaches": ["b2-18-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La comunidad le reprochó al gobernador que no __ cumplido sus promesas de campaña electoral. (haber)",
                "answer": "hubiera",
                "english": "The community reproached the governor for not having fulfilled his campaign promises.",
                "teaches": ["verbos-comunicacion-reproche-critica"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el verbo 'reprochar que' exige obligatoriamente modo subjuntivo en la proposición subordinada?",
                "options": [
                    "Porque expresa un juicio de valor afectivo y una censura moral sobre una conducta previa.",
                    "Porque describe una acción que ocurrirá con certeza en el siglo próximo.",
                    "Porque es un verbo de percepción física como ver u oír.",
                    "Porque se utiliza exclusivamente en oraciones interrogativas directas."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-reproche-critica"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "diputados", "censuraron", "la", "omisión", "de", "las", "autoridades", "locales."],
                "solution": ["Los", "diputados", "censuraron", "la", "omisión", "de", "las", "autoridades", "locales."],
                "english": "The deputies censured the omission of the local authorities.",
                "teaches": ["verbos-comunicacion-reproche-critica"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Líder comunal", "text": "¿Qué le recriminó Rosendo Maqui al hacendado durante el violento deslinde de tierras?"},
                    {"speaker": "Testigo", "text": "_____"}
                ],
                "options": [
                    "Le reprochó con amargura que hubiera comprado testimonios falsos para despojar a los comuneros de sus parcelas ancestrales.",
                    "Le ofreció un café caliente para abrigarse de la brisa serrana.",
                    "El ganado pacía pacíficamente en los prados comunales del valle.",
                    "Los caballos de la hacienda eran de raza andaluza importada."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-reproche-critica"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La prensa independiente cuestionó severamente que los contratos mineros se hubieran firmado en audiencias a puerta cerrada.",
                "english": "The independent press severely questioned that the mining contracts had been signed in closed-door hearings.",
                "teaches": ["verbos-comunicacion-reproche-critica"]
            }
        ]
    })

    # --- Lesson 5: b2-18-05 ---
    l5 = f"{c_unit}-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.18.05",
        "lesson": l5,
        "title": "Verbos de conjetura, sospecha y distanciamiento epistémico",
        "theme": "Léxico de cautela periodística, hipótesis forenses y no-compromiso asertivo",
        "words": [
            {"lemma": "conjeturar", "translation": "to conjecture, to surmise", "pos": "verb"},
            {"lemma": "sospechar", "translation": "to suspect, to infer with doubt", "pos": "verb"},
            {"lemma": "insinuar", "translation": "to insinuate, to hint subtly", "pos": "verb"},
            {"lemma": "presumir", "translation": "to presume, to take for granted tentatively", "pos": "verb"},
            {"lemma": "especular", "translation": "to speculate without full certainty", "pos": "verb"},
            {"lemma": "alegar", "translation": "to claim/allege without endorsement", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.18.05.verbos-comunicacion-subjetividad-conjetura",
        "title": "Verbos de conjetura, sospecha y distanciamiento epistémico",
        "sections": [
            {
                "type": "text",
                "content": "En el periodismo de rigor y el análisis ensayístico de nivel B2, a menudo es imperativo reportar declaraciones ajenas **sin asumir la responsabilidad de su veracidad**. Los verbos de distanciamiento epistémico permiten al redactor señalar que una información no ha sido comprobada de forma independiente, o que constituye una mera hipótesis de su interlocutor.\n\nVerbos como **alegar** (*alegó que había actuado en defensa propia*), **insinuar** (*insinuó que existían presiones políticas*), **conjeturar** o **especular** permiten modular con máxima sutileza la distancia crítica entre el relator y el mensaje reportado."
            },
            {
                "type": "table",
                "title": "Verbos de distanciamiento epistémico",
                "rows": [
                    ["alegar que", "He alleged that the contract had already been rescinded (unverified claim)."],
                    ["insinuar que", "The columnist hinted that private interests guided the legislative vote."],
                    ["conjeturar que", "Analysts conjectured that the border dispute would be resolved diplomatically."],
                    ["presumir que", "Investigators presumed that the documents were stored in the vault."],
                    ["especular con que", "The markets speculated that the interest rates would rise next quarter."],
                    ["dar a entender que", "The spokesperson implied that significant policy changes were underway."]
                ]
            },
            {
                "type": "tip",
                "content": "El verbo *alegar* es el recurso estrella del periodismo legal anglo e hispanoamericano: al escribir *'El acusado alegó que...'*, el periodista informa de lo que dijo la defensa sin respaldar su certeza factual, protegiéndose contra demandas de difamación."
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
                    ["conjeturar", "to infer from circumstantial evidence"],
                    ["insinuar", "to hint obliquely without naming"],
                    ["alegar", "to claim without official proof"],
                    ["especular", "to theorize without firm basis"]
                ],
                "teaches": ["b2-18-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La defensa __ que el imputado se hallaba en otra provincia el día del despojo territorial. (alegar)",
                "answer": "alegó",
                "english": "The defense claimed that the accused was in another province the day of the land seizure.",
                "teaches": ["verbos-comunicacion-subjetividad-conjetura"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué un periodista profesional elige 'alegar que' en lugar de 'afirmar que' en una crónica judicial?",
                "options": [
                    "Para distanciarse de la afirmación y dejar en claro que se trata de un argumento no verificado de parte.",
                    "Porque la palabra afirmar está prohibida en los manuales de redacción de los diarios.",
                    "Para indicar que el juicio ya concluyó con una sentencia condenatoria firme.",
                    "Porque alegar significa que el tribunal aprobó la declaración de manera unánime."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-subjetividad-conjetura"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "editorialistas", "insinuaron", "que", "hubo", "presiones", "políticas", "ocultas."],
                "solution": ["Los", "editorialistas", "insinuaron", "que", "hubo", "presiones", "políticas", "ocultas."],
                "english": "The editorialists hinted that there were hidden political pressures.",
                "teaches": ["verbos-comunicacion-subjetividad-conjetura"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Corresponsal", "text": "¿Qué postura adoptó la empresa acusada de contaminar el río comunal?"},
                    {"speaker": "Abogada ambiental", "text": "_____"}
                ],
                "options": [
                    "Alegó que sus efluentes cumplían los estándares técnicos, insinuando que la turbidez del agua se debía a deslaves naturales.",
                    "Los ríos de la sierra bajan caudalosos desde los glaciares en la primavera.",
                    "La empresa se fundó hace cincuenta años en la ciudad capital.",
                    "El agua mineral con gas se vende en botellas de vidrio reciclado."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-subjetividad-conjetura"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los analistas conjeturaron que las partes alcanzarían un acuerdo preliminar antes de la próxima asamblea general.",
                "english": "The analysts conjectured that the parties would reach a preliminary agreement before the next general assembly.",
                "teaches": ["verbos-comunicacion-subjetividad-conjetura"]
            }
        ]
    })

    # --- Lesson 6: b2-18-consolidation ---
    l6_con = f"{c_unit}-consolidation"
    write_json(f"exercises/b2/{l6_con}-ex.json", {
        "lesson": l6_con,
        "exercises": [
            {
                "id": f"{l6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["aseverar", "to state as factual truth"],
                    ["rebatir", "to counter opposing arguments"],
                    ["reprochar", "to blame for ethical failure"],
                    ["alegar", "to claim without endorsement"]
                ],
                "teaches": ["b2-18-vocab"]
            },
            {
                "id": f"{l6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la novela de Ciro Alegría, el alcalde Rosendo Maqui __ que la tierra pertenecía a la comunidad desde tiempos inmemoriales. (sostener)",
                "answer": "sostuvo",
                "english": "In Ciro Alegría's novel, Mayor Rosendo Maqui maintained that the land belonged to the community since times immemorial.",
                "teaches": ["verbos-comunicacion-aseverativos"]
            },
            {
                "id": f"{l6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el verbo 'desmentir' en una rueda de prensa oficial?",
                "options": [
                    "Negar rotundamente la veracidad de una información o rumor considerado falso.",
                    "Confirmar que un tratado entrará en vigor de inmediato.",
                    "Pedir disculpas públicas por un error administrativo.",
                    "Felicitar a los organizadores de un certamen cultural."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-disputa-refutacion"]
            },
            {
                "id": f"{l6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los ancianos advirtieron a la asamblea comunal que no se __ en promesas de abogados corruptos. (confiar)",
                "answer": "confiara",
                "english": "The elders warned the community assembly not to trust corrupt lawyers' promises.",
                "teaches": ["verbos-comunicacion-advertencia-recordatorio"]
            },
            {
                "id": f"{l6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué efecto retórico logra un autor al usar 'reprochó que' seguido de subjuntivo en una crónica?",
                "options": [
                    "Enfatiza la condena moral y la decepción ética ante una omisión o falta cometida.",
                    "Expresa un deseo futuro de que la economía prospere sin inflación.",
                    "Describe un paisaje natural de forma neutra y puramente geométrica.",
                    "Introduce una fórmula de cortesía epistolar obligatoria en cartas comerciales."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-reproche-critica"]
            },
            {
                "id": f"{l6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "hacendado", "alegó", "que", "poseía", "los", "títulos", "legítimos", "de", "compra."],
                "solution": ["El", "hacendado", "alegó", "que", "poseía", "los", "títulos", "legítimos", "de", "compra."],
                "english": "The landowner claimed that he possessed the legitimate purchase titles.",
                "teaches": ["verbos-comunicacion-subjetividad-conjetura"]
            },
            {
                "id": f"{l6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "El tribunal desestimó la demanda comunitaria tras rebatir los alegatos sobre la posesión inmemorial de las tierras.",
                "english": "The court dismissed the community lawsuit after rebutting the claims regarding immemorial land possession.",
                "teaches": ["verbos-comunicacion-disputa-refutacion"]
            },
            {
                "id": f"{l6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué tema central inmortalizó Ciro Alegría en su obra maestra El mundo es ancho y ajeno?",
                "options": [
                    "La lucha titánica de la comunidad indígena de Rumi por defender sus tierras comunales frente al latifundismo voraz.",
                    "La construcción del primer ferrocarril eléctrico en las costas del mar Pacífico.",
                    "Las aventuras cómicas de un hidalgo en los caminos de la Mancha en el siglo diecisiete.",
                    "Un tratado de astronomía maya sobre los eclipses solares en Yucatán."
                ],
                "correct": 0,
                "teaches": ["verbos-comunicacion-aseverativos"]
            }
        ]
    })

    # Classic Story for Core Unit 18: Ciro Alegría - El mundo es ancho y ajeno (~700 words, strictly 650-825 words)
    story_core_18 = {
        "id": "b2-18",
        "title": "El mundo es ancho y ajeno: La resistencia inmortal de la comunidad de Rumi",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de nivel B2 de la obra maestra del indigenismo peruano de Ciro Alegría: la vida armónica de la comunidad andina de Rumi bajo el liderazgo de su sabio alcalde Rosendo Maqui, el despojo legal orquestado por el codicioso hacendado Álvaro Amenábar, la muerte de Rosendo en prisión y el regreso de Benito Castro para organizar la defensa final de la tierra comunal.",
        "characters": [
            "Rosendo Maqui",
            "Don Álvaro Amenábar",
            "Benito Castro",
            "Bismark Ruiz",
            "Marguina"
        ],
        "narration": {
            "paragraphs": [
                "En las laderas fértiles de los Andes septentrionales del Perú, abrazada por el rumor transparente de las quebradas y el verdor de los trigales, florecía la comunidad indígena de Rumi. Para sus centenares de comuneros, la tierra no era una mercancía que pudiera comprarse o venderse en las ferias coloniales, sino una madre generosa que sus abuelos habían cultivado en hermandad solidaria desde tiempos inmemoriales. Al frente de aquel pueblo laborioso se hallaba el viejo alcalde Rosendo Maqui, un hombre sabio de cabellos plateados, rostro surcado de arrugas venerables y ojos penetrantes que conocía el secreto de las hierbas curativas y conversaba con el espíritu del cerro Rumi.",
                "El sosiego ancestral de la comunidad se quebró cuando el codicioso hacendado don Álvaro Amenábar de Umay puso sus ojos ambiciosos sobre los valles de Rumi. Amenábar no se conformaba con sus inmensas posesiones ganaderas; requería apoderarse de las tierras fértiles de los comuneros y forzar a sus hombres a trabajar como peones semiesclavos en sus peligrosos lavaderos de oro en las selvas calientes del río Marañón. Amparado en su poder económico y en sus relaciones de compadrazgo político, el hacendado interpuso una fraudulenta demanda de linderos contra Rumi ante el tribunal provincial.",
                "Rosendo Maqui convocó a la asamblea comunal y viajó a la ciudad para contratar al abogado Bismark Ruiz. En el juzgado, el viejo alcalde aseveró con dignidad que la comunidad poseía títulos virreinales sellados por el propio rey de España que acreditaban la propiedad colectiva desde hacía más de tres siglos. Sin embargo, el aparato judicial estaba completamente corrompido: Amenábar sobornó al juez, compró testimonios falsos de testigos perjuros que afirmaban bajo juramento que Rumi pertenecía a la hacienda Umay, e intimidó a los escribanos locales. Pese a que los comuneros rebatieron las calumnias con documentos irrefutables, el tribunal dictó un fallo infame despojando a Rumi de todas sus tierras agrícolas.",
                "Los comuneros fueron forzados a abandonar sus huertos, sus molinos de trigo y sus casas de adobe. Con lágrimas en los ojos pero con la cabeza erguida, Rosendo Maqui guio a su pueblo hacia las alturas pedregosas y gélidas de Yanañahui, una meseta estéril donde el viento helado calaba los huesos. Allí levantaron nuevas chozas precarias, desafiando a la intemperie y sembrando papas amargas en la roca viva. Pero la saña del hacendado no tenía límites: para desarticular la moral de los campesinos, acusó a Rosendo de liderar un motín sedicioso y lo encarceló en una celda húmeda de la capital provincial, donde el noble anciano murió tras ser salvajemente golpeado por los carceleros.",
                "La comunidad parecía condenada a extinguirse entre la dispersión forzada y el desaliento. Desesperados por el hambre, muchos comuneros emigraron a la costa para cortar caña de azúcar en haciendas palúdicas, o marcharon a las minas de carbón donde la tisis pulverizaba los pulmones de los jóvenes. Sin embargo, la esperanza renació con el regreso inesperado de Benito Castro, un comunero adoptado por Rosendo que había recorrido el mundo como soldado y tipógrafo, aprendiendo a leer las leyes y a descifrar los mecanismos de dominación de la sociedad criolla.",
                "Elegido como nuevo alcalde por la asamblea comunitaria, Benito proclamó que la huida hacia tierras más altas ya no era una opción viable porque 'el mundo es ancho, pero ajeno para los pobres que no tienen armas ni justicia'. El joven líder enseñó a los comuneros a organizarse militarmente, a colocar centinelas en los desfiladeros y a defender las parcelas que les quedaban frente al avance de los mayordomos y de la policía montada enviada por el prefecto departamental.",
                "La batalla final estalló en los riscos de Yanañahui cuando las tropas gubernamentales atacaron con fusiles Máuser automáticos. Aunque los comuneros resistieron con heroísmo usando hondas, piedras rodantes y viejas escopetas de caza, la superioridad militar de los atacantes se impuso en una masacre desgarradora. Benito Castro cayó mortalmente herido en las rocas mientras contemplaba a su pueblo resistir hasta el último aliento. En esta cumbre de la novela indigenista latinoamericana, Ciro Alegría no solo retrató la tragedia del despojo feudal, sino la dignidad indomable de la comunidad andina, cuyo amor sagrado por la tierra sobrevive a todas las violencias de la historia."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué el hacendado don Álvaro Amenábar interpuso una demanda fraudulenta contra la comunidad de Rumi?",
                        "options": [
                            "Para arrebatarles sus tierras agrícolas y obligar a los comuneros a trabajar como mano de obra en sus minas.",
                            "Para construir una universidad pedagógica en beneficio de los niños indígenas de la sierra.",
                            "Porque la comunidad de Rumi había invadido los pastizales ganaderos de la hacienda Umay.",
                            "Para proteger los bosques andinos de la tala ilegal de madera comercial."
                        ],
                        "correctIndex": 0,
                        "explanation": "Amenábar ambicionaba las ricas tierras de Rumi y necesitaba mano de obra barata forzada para sus lavaderos de oro en el río Marañón."
                    },
                    {
                        "question": "¿Qué destino sufrió el sabio alcalde Rosendo Maqui tras el despojo de las tierras comunales?",
                        "options": [
                            "Fue encarcelado injustamente bajo falsas acusaciones de sedición y murió a causa de los golpes recibidos en prisión.",
                            "Se convirtió en hacendado próspero y compró parcelas agrícolas en la costa norte.",
                            "Emigró a Europa para estudiar jurisprudencia en la Universidad de París.",
                            "Fue nombrado juez de primera instancia por el prefecto del departamento."
                        ],
                        "correctIndex": 0,
                        "explanation": "Rosendo fue apresado con calumnias tras el traslado a Yanañahui y falleció en su celda debido a los maltratos de los carceleros."
                    },
                    {
                        "question": "¿Qué lección fundamental transmitió Benito Castro a la comunidad tras regresar de sus viajes?",
                        "options": [
                            "Que el mundo era ancho pero ajeno para los desposeídos, y que debían defender la tierra con organización y firmeza.",
                            "Que los campesinos debían abandonar la agricultura para dedicarse al comercio de telas importadas.",
                            "Que el hacendado tenía el derecho divino de administrar todas las montañas del Perú.",
                            "Que la solución residía en aceptar pacíficamente la servidumbre feudal de la hacienda."
                        ],
                        "correctIndex": 0,
                        "explanation": "Benito sintetizó el título de la novela advirtiendo que el mundo era ancho pero ajeno para los campesinos sin tierras, liderando la resistencia armada."
                    }
                ]
            }
        }
    }

    # -------------------------------------------------------------------------
    # 3. REGIONAL UNIT 18: b2-peruandino (Peru I: Cusco, Tawantinsuyu & Andean Worldview)
    # -------------------------------------------------------------------------
    r_unit = "b2-peruandino"

    # --- Lesson 1: b2-peruandino-01 ---
    r1 = f"{r_unit}-01"
    write_json(f"vocabulary/b2/{r1}-voc.json", {
        "id": "vocab.b2.peruandino.01",
        "lesson": r1,
        "title": "La cordillera Blanca y los glaciares andinos",
        "theme": "Léxico de glaciología tropical, geomorfología de alta montaña y riesgo hídrico",
        "words": [
            {"lemma": "glaciar", "translation": "glacier, tropical ice mass", "pos": "noun"},
            {"lemma": "laguna", "translation": "glacial lake, high tarn", "pos": "noun"},
            {"lemma": "aluvión", "translation": "flash flood / debris flow from glacial breach", "pos": "noun"},
            {"lemma": "quebrada", "translation": "mountain gorge, ravine", "pos": "noun"},
            {"lemma": "morrena", "translation": "glacial moraine, rock deposit", "pos": "noun"},
            {"lemma": "retroceso", "translation": "retreat of ice sheet / shrinkage", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r1}-a-gr.json", {
        "id": "grammar.b2.peruandino.01.peru-cordillera-blanca-glaciares",
        "title": "La cordillera Blanca y el sistema hidrográfico de las alturas peruanas",
        "sections": [
            {
                "type": "text",
                "content": "Ubicada en el departamento de Áncash, en los Andes centrales del Perú, la **cordillera Blanca** es la cadena montañosa tropical cubierta de nieve más alta y extensa del planeta. A lo largo de casi doscientos kilómetros se alinean más de setecientos glaciares individuales coronados por decenas de picos que superan los seis mil metros de altitud, entre los que descuella el imponente **Huascarán** (6.768 m s. n. m.), la cumbre más alta del Perú y de toda la zona tórrida mundial.\n\nEste laberinto de picos piramidales y quebradas profundas cumple un papel hidrológico irremplazable: durante la temporada seca de la sierra (de mayo a septiembre), el deshielo gradual de los glaciares aporta más del cuarenta por ciento del caudal del **río Santa**, cuyas aguas riegan los valles agrícolas del Callejón de Huaylas y abastecen las centrales hidroeléctricas y los valles agroexportadores de la árida costa desértica del Pacífico."
            },
            {
                "type": "table",
                "title": "Geografía física y lagunas de la cordillera Blanca",
                "rows": [
                    ["el Huascarán", "highest tropical peak on Earth at 6,768 meters in the Ancash region"],
                    ["el Alpamayo", "voted the world's most beautiful mountain for its perfect ice pyramid"],
                    ["el río Santa", "main hydrological artery flowing through the Callejón de Huaylas"],
                    ["la laguna Llanganuco", "turquoise glacial lakes Chinancocha and Orconcocha below Huascarán"],
                    ["el aluvión de Yungay", "tragic 1970 earthquake avalanche burying the town of Yungay"],
                    ["el Parque Nacional Huascarán", "UNESCO Biosphere Reserve and World Natural Heritage Site"]
                ]
            },
            {
                "type": "tip",
                "content": "Debido a la crisis climática global, la cordillera Blanca ha perdido más del cincuenta por ciento de su masa glaciar en las últimas cuatro décadas. Esta desglaciación acelerada genera lagunas glaciares inestables que exigen constantes obras de ingeniería para prevenir aluviones catastróficos."
            }
        ]
    })

    write_json(f"exercises/b2/{r1}-ex.json", {
        "lesson": r1,
        "exercises": [
            {
                "id": f"{r1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["glaciar", "tropical ice mass"],
                    ["aluvión", "debris avalanche flood"],
                    ["quebrada", "deep mountain ravine"],
                    ["morrena", "glacial sediment deposit"]
                ],
                "teaches": ["b2-peruandino-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Huascarán es la cumbre más alta del Perú y de toda la zona __ del planeta. (tropical)",
                "answer": "tropical",
                "english": "Huascarán is the highest peak in Peru and in the entire tropical zone of the planet.",
                "teaches": ["peru-cordillera-blanca-glaciares"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función hidrológica primordial cumple el deshielo glaciar de la cordillera Blanca en los meses de sequía?",
                "options": [
                    "Alimenta el caudal del río Santa, abasteciendo de agua potable, electricidad y riego a la costa y la sierra.",
                    "Provoca el congelamiento instantáneo de los puertos pesqueros del norte peruano.",
                    "Suministra agua salada a los arrozales de la selva baja amazónica.",
                    "Impide que los vientos alisios crucen la cordillera hacia el océano Atlántico."
                ],
                "correct": 0,
                "teaches": ["peru-cordillera-blanca-glaciares"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "glaciares", "tropicales", "regulan", "el", "caudal", "del", "río", "Santa."],
                "solution": ["Los", "glaciares", "tropicales", "regulan", "el", "caudal", "del", "río", "Santa."],
                "english": "Tropical glaciers regulate the flow of the Santa river.",
                "teaches": ["peru-cordillera-blanca-glaciares"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Glacióloga", "text": "¿Por qué los científicos vigilan de forma permanente las lagunas de alta montaña en Áncash?"},
                    {"speaker": "Ingeniero ambiental", "text": "_____"}
                ],
                "options": [
                    "Para prevenir roturas de morrenas y aluviones devastadores causados por desprendimientos de hielo en las lagunas glaciares.",
                    "Para contar cuántas truchas nadan en las aguas superficiales durante el verano.",
                    "Porque las lagunas contienen petróleo liviano que puede ser extraído con bombas.",
                    "Para medir la profundidad de las aguas y autorizar carreras de lanchas a motor."
                ],
                "correct": 0,
                "teaches": ["peru-cordillera-blanca-glaciares"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El Parque Nacional Huascarán protege ecosistemas de montaña excepcionales declarados Patrimonio Natural de la Humanidad.",
                "english": "Huascarán National Park protects exceptional mountain ecosystems declared a World Natural Heritage Site.",
                "teaches": ["peru-cordillera-blanca-glaciares"]
            }
        ]
    })

    # --- Lesson 2: b2-peruandino-02 ---
    r2 = f"{r_unit}-02"
    write_json(f"vocabulary/b2/{r2}-voc.json", {
        "id": "vocab.b2.peruandino.02",
        "lesson": r2,
        "title": "Civilizaciones preincas: Caral, Chavín y Moche",
        "theme": "Léxico de arqueología andina, arquitectura monumental y metalurgia precolombina",
        "words": [
            {"lemma": "civilización", "translation": "civilization, complex urban society", "pos": "noun"},
            {"lemma": "piramidal", "translation": "pyramidal, stepped platform structure", "pos": "adjective"},
            {"lemma": "oráculo", "translation": "oracle, sacred divination shrine", "pos": "noun"},
            {"lemma": "metalurgia", "translation": "metallurgy, gold/silver craftsmanship", "pos": "noun"},
            {"lemma": "iconografía", "translation": "iconography, visual religious motifs", "pos": "noun"},
            {"lemma": "monolito", "translation": "monolith, carved single-stone pillar", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r2}-a-gr.json", {
        "id": "grammar.b2.peruandino.02.peru-civilizaciones-preincas-caral",
        "title": "Milenios antes de los incas: Caral, Chavín y la complejidad andina",
        "sections": [
            {
                "type": "text",
                "content": "Aunque el imperio incaico cautiva la imaginación universal, su apogeo representó únicamente el último siglo de un desarrollo civilizatorio andino que se remonta a más de cinco mil años de antigüedad. En el valle de Supe, al norte de Lima, floreció **Caral** (3000 a. C.), reconocida por la UNESCO como **la civilización más antigua de todo el continente americano**, contemporánea de las pirámides de Egipto y de las ciudades sumerias de Mesopotamia.\n\nSiglos más tarde, en la sierra de Áncash, el centro ceremonial de **Chavín de Huántar** (1200 a 800 a. C.) actuó como un poderoso oráculo panandino. Sus galerías subterráneas laberínticas, el enigmático **Lanzón Monolítico** esculpido en granito y sus cabezas clavas felínicas difundieron una cosmovisión religiosa unificada. En la costa norte, la cultura **Moche** (100 a 700 d. C.) asombró por sus impresionantes pirámides de adobe (Huaca del Sol y de la Luna), su refinada metalurgia en oro y cobre dorado demostrada en la fastuosa tumba del **Señor de Sipán**, y su cerámica escultórica realista única en América."
            },
            {
                "type": "table",
                "title": "Hitos preincaicos del Antiguo Perú",
                "rows": [
                    ["la Ciudad Sagrada de Caral", "oldest American civilization (3000 BCE) with monumental stepped plazas"],
                    ["el Lanzón Monolítico de Chavín", "4.5-meter carved granite deity in subterranean labyrinthine galleries"],
                    ["las cabezas clavas", "tenon stone heads depicting priests transforming into sacred jaguars"],
                    ["el Señor de Sipán", "unlooted royal Moche tomb revealing elite gold, turquoise, and feather regalia"],
                    ["los huacos retratos moche", "finely modelled realistic ceramics capturing psychological human states"],
                    ["la Dama de Cao", "tattooed Moche female ruler demonstrating prominent women's authority in governance"]
                ]
            },
            {
                "type": "tip",
                "content": "Caral demostró que la civilización urbana en América surgió de manera completamente autóctona e independiente, sin influencia de culturas de otros continentes y fundamentada en el comercio pacífico entre pescadores de la costa y agricultores de algodón del valle."
            }
        ]
    })

    write_json(f"exercises/b2/{r2}-ex.json", {
        "lesson": r2,
        "exercises": [
            {
                "id": f"{r2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["civilización", "complex urban society"],
                    ["piramidal", "stepped platform shape"],
                    ["oráculo", "sacred divination shrine"],
                    ["monolito", "carved stone pillar"]
                ],
                "teaches": ["b2-peruandino-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Caral es reconocida por la UNESCO como la civilización más __ de todo el continente americano. (antigua)",
                "answer": "antigua",
                "english": "Caral is recognized by UNESCO as the oldest civilization on the entire American continent.",
                "teaches": ["peru-civilizaciones-preincas-caral"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué revelaron las excavaciones de la tumba del Señor de Sipán en la costa norte peruana?",
                "options": [
                    "El extraordinario dominio metalúrgico y la opulencia ceremonial de la élite de la cultura Moche.",
                    "Que los incas habían conquistado el valle de Supe dos milenios antes de Cristo.",
                    "Que las culturas precolombinas carecían de jerarquías políticas estructuradas.",
                    "La presencia de carabelas europeas en las costas peruanas durante el siglo primero."
                ],
                "correct": 0,
                "teaches": ["peru-civilizaciones-preincas-caral"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Chavín", "de", "Huántar", "fue", "un", "oráculo", "panandino", "de", "gran", "influencia."],
                "solution": ["Chavín", "de", "Huántar", "fue", "un", "oráculo", "panandino", "de", "gran", "influencia."],
                "english": "Chavín de Huántar was a pan-Andean oracle of great influence.",
                "teaches": ["peru-civilizaciones-preincas-caral"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Arqueóloga", "text": "¿Por qué el descubrimiento de la Dama de Cao modificó las teorías históricas sobre la cultura Moche?"},
                    {"speaker": "Historiador", "text": "_____"}
                ],
                "options": [
                    "Porque demostró que las mujeres de la élite moche ejercían un poder político y religioso prominente como sacerdotisas y gobernantes.",
                    "Porque sus armas eran de acero inoxidable importado del mar Mediterráneo.",
                    "Porque la tumba no contenía ninguna joya ni ornamento ceremonial.",
                    "Porque fue la primera gobernante en redactar leyes en papel papiro."
                ],
                "correct": 0,
                "teaches": ["peru-civilizaciones-preincas-caral"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "En las galerías subterráneas de Chavín, el Lanzón Monolítico concentra la energía sagrada de divinidades felínicas y marinas.",
                "english": "In the underground galleries of Chavín, the Monolithic Lanzón concentrates the sacred energy of feline and marine deities.",
                "teaches": ["peru-civilizaciones-preincas-caral"]
            }
        ]
    })

    # --- Lesson 3: b2-peruandino-03 ---
    r3 = f"{r_unit}-03"
    write_json(f"vocabulary/b2/{r3}-voc.json", {
        "id": "vocab.b2.peruandino.03",
        "lesson": r3,
        "title": "Tawantinsuyu y la red vial del Qhapaq Ñan",
        "theme": "Léxico de administración incaica, arquitectura sismorresistente y red vial",
        "words": [
            {"lemma": "chasqui", "translation": "relay postal runner in the Inca empire", "pos": "noun"},
            {"lemma": "quipu", "translation": "knotted-string mnemonic accounting recording device", "pos": "noun"},
            {"lemma": "almohadillado", "translation": "cushioned-edge stone masonry joint", "pos": "adjective"},
            {"lemma": "sismorresistente", "translation": "earthquake-resistant engineering", "pos": "adjective"},
            {"lemma": "redistribución", "translation": "state economic redistribution", "pos": "noun"},
            {"lemma": "reciprocidad", "translation": "ayni: reciprocal communal exchange", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r3}-a-gr.json", {
        "id": "grammar.b2.peruandino.03.peru-tawantinsuyu-qhapaq-nan",
        "title": "Tawantinsuyu: Administración imperial y la red vial del Qhapaq Ñan",
        "sections": [
            {
                "type": "text",
                "content": "En menos de un siglo de vertiginosa expansión, los incas forjaron el **Tawantinsuyu** (el imperio de las cuatro regiones unidas: Chinchaysuyu, Antisuyu, Cuntisuyu y Collasuyu), el Estado más extenso de la América precolombina, que abarcaba desde el sur de Colombia hasta el centro de Chile y el noroeste de Argentina, con su capital en la sagrada ciudad de **Cusco** ('el ombligo del mundo').\n\nLa columna vertebral que hizo posible gobernar un territorio de más de dos millones de kilómetros cuadrados a través de cordilleras abruptas, desiertos costeros y selvas fue el **Qhapaq Ñan** (Gran Camino Inca), una prodigiosa red vial empedrada de más de treinta mil kilómetros declarada Patrimonio Mundial por la UNESCO. A través de este sistema circulaban los **chasquis** (ágiles mensajeros de relevo que transmitían órdenes orales a velocidades asombrosas) y se gestionaban los depósitos estatales (*qollqas*) mediante el **quipu**, sofisticado sistema de cordeles de algodón y nudos que registraba censos poblacionales, cosechas agrícolas y tributos laborales con estricta precisión matemática."
            },
            {
                "type": "table",
                "title": "Pilares de la ingeniería y administración del Tawantinsuyu",
                "rows": [
                    ["el Qhapaq Ñan", "30,000-km paved stone highway crossing six modern South American nations"],
                    ["los chasquis", "relay runners covering up to 240 kilometers per day along mountain passes"],
                    ["el quipu", "binary-like decimal knotted string device encoding demographic and fiscal data"],
                    ["la mita", "rotational state labor obligation building roads, terraces, and fortresses"],
                    ["la arquitectura sismorresistente", "perfectly interlocked stone blocks without mortar withstanding mega-quakes"],
                    ["Machu Picchu", "royal estate and sacred astronomical sanctuary perched above the Urubamba canyon"]
                ]
            },
            {
                "type": "tip",
                "content": "La mampostería imperial incaica en piedra almohadillada ensamblaba gigantescos bloques poligonales con tal perfección milimétrica que no es posible introducir la hoja de un cuchillo entre sus junturas. Durante los terremotos, las piedras bailan absorbiendo la energía sísmica y vuelven a encajar en su posición original."
            }
        ]
    })

    write_json(f"exercises/b2/{r3}-ex.json", {
        "lesson": r3,
        "exercises": [
            {
                "id": f"{r3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["chasqui", "imperial relay messenger runner"],
                    ["quipu", "knotted-cord accounting system"],
                    ["almohadillado", "beveled stone-masonry finish"],
                    ["sismorresistente", "engineered to endure earthquakes"]
                ],
                "teaches": ["b2-peruandino-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La red vial del Qhapaq Ñan abarcaba más de treinta mil kilómetros declarados Patrimonio __ por la UNESCO. (Mundial)",
                "answer": "Mundial",
                "english": "The Qhapaq Ñan road network spanned over thirty thousand kilometers declared World Heritage by UNESCO.",
                "teaches": ["peru-tawantinsuyu-qhapaq-nan"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo funcionaba el sistema de comunicación imperial de los chasquis en el Qhapaq Ñan?",
                "options": [
                    "Mediante corredores de relevo apostados en postas que transmitían mensajes orales a gran velocidad.",
                    "Mediante palomas mensajeras entrenadas en las costas del océano Pacífico.",
                    "A través de barcos de vapor que navegaban por los canales de riego.",
                    "Utilizando caballos veloces importados de las llanuras del norte."
                ],
                "correct": 0,
                "teaches": ["peru-tawantinsuyu-qhapaq-nan"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "muros", "incas", "ensamblan", "piedras", "con", "precisión", "milimétrica", "asombrosa."],
                "solution": ["Los", "muros", "incas", "ensamblan", "piedras", "con", "precisión", "milimétrica", "asombrosa."],
                "english": "Inca walls assemble stones with astonishing millimeter precision.",
                "teaches": ["peru-tawantinsuyu-qhapaq-nan"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ingeniero civil", "text": "¿Por qué los muros incas de Cusco sobrevivieron a los terremotos que destruyeron iglesias coloniales?"},
                    {"speaker": "Arqueólogo", "text": "_____"}
                ],
                "options": [
                    "Porque su arquitectura sismorresistente de piedras trapezoidales machihembradas absorbe las ondas telúricas sin fracturarse.",
                    "Porque fueron reforzados con vigas de acero moderno en el siglo veinte.",
                    "Porque los incas construían sus fortalezas exclusivamente sobre suelos de arena marina.",
                    "Porque los templos incaicos carecían de techumbres de madera."
                ],
                "correct": 0,
                "teaches": ["peru-tawantinsuyu-qhapaq-nan"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El quipu registraba censos de población y depósitos agrícolas mediante un riguroso sistema decimal de nudos y cuerdas.",
                "english": "The quipu recorded population censuses and agricultural storehouses through a rigorous decimal system of knots and cords.",
                "teaches": ["peru-tawantinsuyu-qhapaq-nan"]
            }
        ]
    })

    # --- Lesson 4: b2-peruandino-04 ---
    r4 = f"{r_unit}-04"
    write_json(f"vocabulary/b2/{r4}-voc.json", {
        "id": "vocab.b2.peruandino.04",
        "lesson": r4,
        "title": "Cusco colonial y la Escuela Cusqueña de pintura",
        "theme": "Léxico de sincretismo religioso, pintura barroca andina y arquitectura virreinal",
        "words": [
            {"lemma": "sincretismo", "translation": "syncretism, cultural and religious fusion", "pos": "noun"},
            {"lemma": "palimpsesto", "translation": "palimpsest, architectural layered strata", "pos": "noun"},
            {"lemma": "brocateado", "translation": "brocateado: fine gold-leaf gilding on canvas", "pos": "noun"},
            {"lemma": "virreinato", "translation": "viceroyalty, colonial territory", "pos": "noun"},
            {"lemma": "arcángel", "translation": "archangel depicted with harquebus (arcabucero)", "pos": "noun"},
            {"lemma": "hibridación", "translation": "hybridization, cultural crossover", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r4}-a-gr.json", {
        "id": "grammar.b2.peruandino.04.peru-cusco-escuela-cusquena-sincretismo",
        "title": "Cusco colonial: La Escuela Cusqueña y el sincretismo andino",
        "sections": [
            {
                "type": "text",
                "content": "Pocas ciudades del mundo exhiben una superposición histórica tan elocuente como el **Cusco**. Tras la conquista española en 1533, los templos y conventos católicos fueron levantados directamente sobre los cimientos ciclópeos de los palacios incas, creando un fascinante **palimpsesto urbano** cuyo ejemplo más sobrecogedor es el convento de Santo Domingo erigido sobre los muros curvos de piedra oscura del **Qorikancha** (el Templo del Sol).\n\nEn este escenario de choque y resistencia germinó en los siglos XVII y XVIII la **Escuela Cusqueña de pintura**, la manifestación pictórica más original del barroco virreinal hispanoamericano. Liderada por maestros indígenas y mestizos como **Diego Quispe Tito**, esta escuela se emancipó de los modelos europeos incorporando elementos de la cosmovisión andina: paisajes poblados por flora y fauna local, vírgenes triangulares que evocan la figura de la sagrada **Pachamama** (la Madre Tierra identificada con el cerro nevado), y los célebres **Ángeles Arcabuceros**, seres celestiales vestidos con fastuosos trajes aristocráticos que empuñan armas de fuego coloniales en lugar de espadas."
            },
            {
                "type": "table",
                "title": "Iconos del sincretismo y la Escuela Cusqueña",
                "rows": [
                    ["el Qorikancha y Santo Domingo", "magnificent architectural palimpsest merging Inca stone base and Spanish Baroque"],
                    ["la Virgen del Cerro", "syncretic representation of the Virgin Mary embodying the sacred mountain Pachamama"],
                    ["los Ángeles Arcabuceros", "unique iconographic genre portraying winged celestial beings with muskets and brocade"],
                    ["el brocateado en pan de oro", "delicate raised gold gilding adorning robes, crowns, and floral borders on canvas"],
                    ["Diego Quispe Tito", "indigenous master painter and leader of the independent Cusqueño workshop guild"],
                    ["la Última Cena de la Catedral", "iconic painting depicting Christ and apostles dining on roasted guinea pig (cuy) and chicha"]
                ]
            },
            {
                "type": "tip",
                "content": "En la monumental *Última Cena* que cuelga en la Catedral de Cusco, pintada por el maestro quechua Marcos Zapata en 1753, la bandeja central de la mesa de Jesús no contiene cordero pascual, sino un *cuy* (conejillo de indias) asado, y los apóstoles brindan con copas de chicha de jora andina."
            }
        ]
    })

    write_json(f"exercises/b2/{r4}-ex.json", {
        "lesson": r4,
        "exercises": [
            {
                "id": f"{r4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["sincretismo", "religious and cultural fusion"],
                    ["palimpsesto", "architectural layered history"],
                    ["brocateado", "gold-leaf ornamentation on canvas"],
                    ["virreinato", "Spanish colonial administrative realm"]
                ],
                "teaches": ["b2-peruandino-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la Escuela Cusqueña, las representaciones triangulares de la Virgen evocaban a la sagrada __ andina. (Pachamama)",
                "answer": "Pachamama",
                "english": "In the Cusqueña School, triangular depictions of the Virgin evoked the sacred Andean Pachamama.",
                "teaches": ["peru-cusco-escuela-cusquena-sincretismo"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué elemento iconográfico singular caracteriza a la pintura de la 'Última Cena' en la Catedral de Cusco?",
                "options": [
                    "Jesús y sus discípulos tienen en el centro de la mesa un cuy asado servido con chicha de jora.",
                    "La escena transcurre en la cubierta de un galeón español en alta mar.",
                    "Los apóstoles visten armaduras romanas de hierro forjado.",
                    "Todos los personajes aparecen con alas de ángeles doradas."
                ],
                "correct": 0,
                "teaches": ["peru-cusco-escuela-cusquena-sincretismo"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "Ángeles", "Arcabuceros", "fusionan", "símbolos", "celestiales", "y", "armas", "coloniales."],
                "solution": ["Los", "Ángeles", "Arcabuceros", "fusionan", "símbolos", "celestiales", "y", "armas", "coloniales."],
                "english": "The Harquebusier Angels fuse celestial symbols and colonial weapons.",
                "teaches": ["peru-cusco-escuela-cusquena-sincretismo"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora del arte", "text": "¿Por qué los pintores indígenas de la Escuela Cusqueña decidieron separarse del gremio español en 1688?"},
                    {"speaker": "Guía cusqueño", "text": "_____"}
                ],
                "options": [
                    "Para liberarse del control estético peninsular y crear libremente obras con identidad andina, fauna local y brocateado en oro.",
                    "Porque el rey de España prohibió la venta de lienzos en toda América del Sur.",
                    "Para dedicarse exclusivamente a la construcción de carreteras empedradas.",
                    "Porque no disponían de pinceles ni pigmentos vegetales en la sierra."
                ],
                "correct": 0,
                "teaches": ["peru-cusco-escuela-cusquena-sincretismo"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El templo de Santo Domingo descansa sobre los muros de granito del Qorikancha en un testimonio visible del mestizaje arquitectónico.",
                "english": "The church of Santo Domingo rests upon the granite walls of Qorikancha in a visible testimony of architectural mestizaje.",
                "teaches": ["peru-cusco-escuela-cusquena-sincretismo"]
            }
        ]
    })

    # --- Lesson 5: b2-peruandino-05 ---
    r5 = f"{r_unit}-05"
    write_json(f"vocabulary/b2/{r5}-voc.json", {
        "id": "vocab.b2.peruandino.05",
        "lesson": r5,
        "title": "El quechua hoy: vitalidad lingüística y literatura andina",
        "theme": "Léxico de sociolingüística andina, revitalización digital y literatura quechua",
        "words": [
            {"lemma": "aglutinante", "translation": "agglutinative language morphology", "pos": "adjective"},
            {"lemma": "oralidad", "translation": "orality, spoken ancestral tradition", "pos": "noun"},
            {"lemma": "dignificación", "translation": "dignification, reclaiming prestige", "pos": "noun"},
            {"lemma": "cosmovisión", "translation": "worldview, cultural philosophy", "pos": "noun"},
            {"lemma": "sufijo", "translation": "suffix in agglutinative word building", "pos": "noun"},
            {"lemma": "políglota", "translation": "polyglot, speaking multiple languages", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r5}-a-gr.json", {
        "id": "grammar.b2.peruandino.05.peru-quechua-vitalidad-linguistica",
        "title": "El quechua hoy: Vitalidad lingüística y literatura andina contemporánea",
        "sections": [
            {
                "type": "text",
                "content": "Con cerca de cuatro millones de hablantes en el Perú y más de ocho millones en toda la cordillera de los Andes (desde el sur de Colombia hasta el norte de Argentina), el **quechua** o **Runa Simi** ('el habla de los seres humanos') es la lengua originaria más extendida demográficamente de las Américas. Lejos de ser un vestigio arcaico, es un idioma aglutinante de prodigiosa precisión expresiva y riqueza conceptual, capaz de modular con un solo sufijo afectivo o evidencial el grado exacto de empatía, certidumbre o experiencia directa de quien habla.\n\nEl gran novelista y antropólogo andahuaylino **José María Arguedas** (1911-1969) dedicó su vida a tender puentes entre el mundo quechua y la lengua castellana en obras cumbres como *Los ríos profundos* y *Todas las sangres*, demostrando que la sensibilidad andina encierra un torrente poético inagotable. En el siglo XXI, el quechua vive un vibrante renacimiento: desde programas informativos diarios en la televisión pública nacional (*Ñuqanchik*) y doblajes de obras maestras cinematográficas, hasta la efervescencia del rap y la música urbana en quechua liderada por artistas como Renata Flores."
            },
            {
                "type": "table",
                "title": "Conceptos y sufijos de la lengua quechua (Runa Simi)",
                "rows": [
                    ["Runa Simi", "the people's speech: native name for the Quechua linguistic family"],
                    ["la morfología aglutinante", "words built by attaching precise suffixes conveying emotion, evidence, and aspect"],
                    ["el sufijo -cha", "diminutive of tender endearment: Urpi (dove) -> Urpicha (beloved little dove)"],
                    ["el sufijo evidencial -mi / -m", "grammatical marker denoting that the speaker witnessed the event firsthand"],
                    ["José María Arguedas", "bilingual writer integrating Quechua poetic syntax into contemporary Spanish prose"],
                    ["el quechua en la era digital", "viral Quechua pop, TikTok revitalization, and news broadcasts reaching millions"]
                ]
            },
            {
                "type": "tip",
                "content": "En la gramática quechua existe una distinción crucial entre dos tipos de 'nosotros': el *inclusivo* (*ñuqanchik* = tú y yo juntos, todos nosotros) y el *exclusivo* (*ñuqayku* = nosotros, pero sin ti). Esta precisión fomenta un sentido de comunidad y delicadeza interpersonal único."
            }
        ]
    })

    write_json(f"exercises/b2/{r5}-ex.json", {
        "lesson": r5,
        "exercises": [
            {
                "id": f"{r5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["aglutinante", "suffixes attached to word roots"],
                    ["oralidad", "spoken knowledge transmission"],
                    ["dignificación", "elevating social status and respect"],
                    ["cosmovisión", "holistic cultural worldview"]
                ],
                "teaches": ["b2-peruandino-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El escritor José María Arguedas plasmó la riqueza poética del mundo andino en su célebre novela Los ríos __. (profundos)",
                "answer": "profundos",
                "english": "The writer José María Arguedas captured the poetic richness of the Andean world in his famous novel Deep Rivers.",
                "teaches": ["peru-quechua-vitalidad-linguistica"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo lingüístico notable distingue a la primera persona plural (nosotros) en la lengua quechua?",
                "options": [
                    "Distingue entre un nosotros inclusivo (que incluye al oyente) y un nosotros exclusivo (que lo excluye).",
                    "No existe pronombre para la primera persona del plural en la lengua quechua.",
                    "Se utiliza exclusivamente en ceremonias religiosas durante la luna llena.",
                    "Es idéntico al pronombre de segunda persona del singular."
                ],
                "correct": 0,
                "teaches": ["peru-quechua-vitalidad-linguistica"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "quechua", "es", "la", "lengua", "originaria", "más", "hablada", "de", "América."],
                "solution": ["El", "quechua", "es", "la", "lengua", "originaria", "más", "hablada", "de", "América."],
                "english": "Quechua is the most widely spoken indigenous language of the Americas.",
                "teaches": ["peru-quechua-vitalidad-linguistica"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Lingüista", "text": "¿Cómo se manifiesta la vitalidad contemporánea del quechua entre las nuevas generaciones urbanas?"},
                    {"speaker": "Profesora", "text": "_____"}
                ],
                "options": [
                    "A través de géneros musicales juveniles como el rap y el pop en quechua, junto a contenidos virales en plataformas digitales y noticieros televisivos.",
                    "El quechua ha dejado de hablarse por completo en todos los pueblos de la sierra.",
                    "Los diccionarios de quechua se imprimieron únicamente en el siglo dieciocho.",
                    "Los hablantes de quechua solo se comunican mediante señales de humo en las montañas."
                ],
                "correct": 0,
                "teaches": ["peru-quechua-vitalidad-linguistica"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La sufijación aglutinante del quechua permite modular matices de empatía y testimonio con una finura poética extraordinaria.",
                "english": "The agglutinative suffixation of Quechua allows for modulating nuances of empathy and testimony with extraordinary poetic finesse.",
                "teaches": ["peru-quechua-vitalidad-linguistica"]
            }
        ]
    })

    # --- Lesson 6: b2-peruandino-consolidation ---
    r6_con = f"{r_unit}-consolidation"
    write_json(f"exercises/b2/{r6_con}-ex.json", {
        "lesson": r6_con,
        "exercises": [
            {
                "id": f"{r6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["glaciar", "tropical high-altitude ice"],
                    ["oráculo", "sacred pilgrimage sanctuary"],
                    ["chasqui", "Inca imperial relay runner"],
                    ["sincretismo", "cultural and artistic fusion"]
                ],
                "teaches": ["b2-peruandino-vocab"]
            },
            {
                "id": f"{r6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El nevado Huascarán se eleva en la cordillera __ a más de seis mil setecientos metros de altitud. (Blanca)",
                "answer": "Blanca",
                "english": "The snowy peak Huascarán rises in the Cordillera Blanca to over six thousand seven hundred meters of altitude.",
                "teaches": ["peru-cordillera-blanca-glaciares"]
            },
            {
                "id": f"{r6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué civilización preincaica floreció en el valle de Supe hace cinco mil años de forma contemporánea a las pirámides egipcias?",
                "options": [
                    "La Ciudad Sagrada de Caral.",
                    "La civilización de los aztecas en Mesoamérica.",
                    "El imperio Wari en Ayacucho.",
                    "La cultura Chachapoyas en la selva alta."
                ],
                "correct": 0,
                "teaches": ["peru-civilizaciones-preincas-caral"]
            },
            {
                "id": f"{r6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La gran red vial empedrada de más de treinta mil kilómetros construida por los incas se llama Qhapaq __. (Ñan)",
                "answer": "Ñan",
                "english": "The great paved stone road network of over thirty thousand kilometers built by the Incas is called Qhapaq Ñan.",
                "teaches": ["peru-tawantinsuyu-qhapaq-nan"]
            },
            {
                "id": f"{r6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué representa el convento colonial de Santo Domingo edificado sobre el templo incaico del Qorikancha en Cusco?",
                "options": [
                    "Un palimpsesto arquitectónico que evidencia físicamente la superposición colonial y el sincretismo andino.",
                    "Un castillo militar construido por caballeros templarios medievales.",
                    "Una fábrica textil moderna construida durante la Revolución Industrial.",
                    "Un monumento conmemorativo de la aviación comercial del siglo veinte."
                ],
                "correct": 0,
                "teaches": ["peru-cusco-escuela-cusquena-sincretismo"]
            },
            {
                "id": f"{r6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Cusco", "fue", "el", "ombligo", "sagrado", "del", "imperio", "del", "Tawantinsuyu."],
                "solution": ["Cusco", "fue", "el", "ombligo", "sagrado", "del", "imperio", "del", "Tawantinsuyu."],
                "english": "Cusco was the sacred navel of the empire of Tawantinsuyu.",
                "teaches": ["peru-tawantinsuyu-qhapaq-nan"]
            },
            {
                "id": f"{r6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La lengua quechua mantiene viva la memoria ancestral y la poesía de los Andes a través de millones de hablantes.",
                "english": "The Quechua language keeps alive the ancestral memory and poetry of the Andes through millions of speakers.",
                "teaches": ["peru-quechua-vitalidad-linguistica"]
            },
            {
                "id": f"{r6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la trascendencia literaria de José María Arguedas en las letras latinoamericanas?",
                "options": [
                    "Fusionó magistralmente la cosmovisión y el ritmo poético quechua con la narrativa en lengua castellana.",
                    "Escribió novelas policiales ambientadas exclusivamente en las calles de Londres.",
                    "Fue el creador de la primera enciclopedia botánica sobre los cactus mexicanos.",
                    "Compuso óperas en italiano para los teatros del Río de la Plata."
                ],
                "correct": 0,
                "teaches": ["peru-quechua-vitalidad-linguistica"]
            }
        ]
    })

    # -------------------------------------------------------------------------
    # 4. REGIONAL STORIES: Peru I - Andean (6 stories, strictly 650-825 words)
    # -------------------------------------------------------------------------
    # Story 1: Cordillera Blanca y Huascarán
    story_peru_01 = {
        "id": "b2-peruandino-01",
        "title": "Las cumbres de la cordillera Blanca: Guardianes de hielo y agua",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica de alta montaña en el Callejón de Huaylas: la majestuosidad de la cordillera Blanca en Áncash, el coloso nevado del Huascarán, la belleza piramidal del Alpamayo, la memoria del aluvión de Yungay de 1970 y los retos contemporáneos del cambio climático frente al retroceso de los glaciares tropicales.",
        "characters": [
            "Don Teófilo Huerta",
            "Doctora Marleny Yauri",
            "Guardaparque Celso Obregón",
            "Joven montañista Raúl"
        ],
        "narration": {
            "paragraphs": [
                "Bajo el cielo cobalto y diáfano de la sierra de Áncash, el Callejón de Huaylas se abre como un escenario titánico donde la naturaleza exhibe su esplendor más sobrecogedor. A la izquierda del valle discurre la adusta cordillera Negra, desprovista de nieves perpetuas pero rica en minerales; a la derecha, recortándose con blancura cegadora contra el azul del firmamento, se yergue la cordillera Blanca, la cadena montañosa tropical cubierta de hielo más alta y extensa del planeta Tierra. En esta muralla de casi doscientos kilómetros de longitud se suceden decenas de picos piramidales que superan los seis mil metros de altitud, coronados por el coloso Huascarán, cuyos 6.768 metros lo consagran como el techo indiscutible del Perú.",
                "Para los ancianos quechuas que habitan los caseríos de las quebradas, estas cumbres no son simples masas inertes de granito y nieve comprimida: son los Apus tutelares, divinidades protectoras que vigilan el destino de los pueblos y gobiernan las lluvias que riegan las chacras de papas, habas y maíz. Don Teófilo Huerta, arriero veterano que ha guiado expediciones alpinas durante medio siglo por los glaciares del nevado Alpamayo —considerada por montañistas de los cinco continentes como la montaña más hermosa del mundo por la simetría perfecta de su pirámide de hielo—, contempla el horizonte con una mezcla de devoción y desasosiego mientras ajusta los arreos de sus mulas.",
                "Don Teófilo recuerda con nitidez sobrecogedora la tarde fatídica del 31 de mayo de 1970. Aquel domingo soleado, un terremoto de magnitud 7.9 sacudió la costa y la sierra de Áncash, desprendiendo una gigantesca cornisa de hielo y roca de la cumbre norte del Huascarán. La masa colosal, estimada en más de cincuenta millones de metros cúbicos, descendió a más de trescientos kilómetros por hora por la quebrada de Ranrahirca, pulverizándose en un aluvión letal de lodo y peñascos gigantescos que en menos de tres minutos sepultó por completo la próspera ciudad colonial de Yungay, segando la vida de más de veinte mil personas. Hoy, el camposanto de Yungay, presidido por un Cristo blanco monumental con los brazos abiertos sobre las copas de las cuatro palmeras que sobrevivieron a la catástrofe, es un santuario mudo que recuerda la fragilidad humana ante las fuerzas geológicas.",
                "En la actualidad, la cordillera Blanca enfrenta una amenaza más silenciosa pero igualmente inexorable: el calentamiento global de la atmósfera. Científicos peruanos e internacionales que monitorean el Parque Nacional Huascarán han constatado que la cordillera ha perdido más de la mitad de su superficie glaciar en las últimas cuatro décadas. Los hielos eternos retroceden visiblemente año tras año, dejando al descubierto morrenas pardas de roca desnuda y dando origen a centenares de nuevas lagunas glaciares de color turquesa, como las hermosas pero inestables lagunas de Llanganuco y Palcacocha.",
                "Estas lagunas de alta montaña son motivo de constante vigilancia técnica por parte de los ingenieros de la Autoridad Nacional del Agua. Contenidas por diques naturales de morrena que pueden colapsar ante una avalancha repentina de bloques de hielo, las lagunas exigen complejas obras de desagüe mediante tuberías de sifonaje y túneles artificiales para rebajar sus niveles y prevenir aluviones que amenacen a ciudades populosas como Huaraz y Caraz.",
                "Al mismo tiempo, la agonía de los glaciares plantea un dilema de seguridad hídrica continental. Durante los meses secos del invierno andino, el deshielo de las cumbres nevadas aporta más del cuarenta por ciento del caudal del río Santa, la arteria hídrica vital que no solo abastece a las poblaciones serranas y genera energía hidroeléctrica en el Cañón del Pato, sino que también viaja hacia el desierto costero para alimentar gigantescos proyectos de irrigación como Chavimochic y Chinecas, donde florecen campos de espárragos y arándanos para la exportación mundial.",
                "La cordillera Blanca enseña al mundo que la supervivencia de los valles y las urbes depende de la preservación de los santuarios de hielo de las alturas. En las miradas de los montañistas que ascienden los colosos nevados y de los comuneros que rinden tributo al Huascarán late un compromiso urgente: honrar a los glaciares antes de que su despedida definitiva transforme para siempre la geografía sagrada de los Andes peruanos."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singularidad geográfica distingue a la cordillera Blanca en el departamento de Áncash a escala global?",
                        "options": [
                            "Es la cadena montañosa tropical cubierta de nieve más alta y extensa del planeta Tierra.",
                            "Es la única cordillera volcánica activa situada en el hemisferio norte.",
                            "Es un macizo de mesetas desérticas que carece por completo de glaciares y ríos.",
                            "Es la cordillera más baja de América del Sur, con elevaciones inferiores a mil metros."
                        ],
                        "correctIndex": 0,
                        "explanation": "La cordillera Blanca alberga la mayor concentración de glaciares tropicales del mundo, coronada por el nevado Huascarán."
                    },
                    {
                        "question": "¿Qué tragedia histórica provocada por un terremoto sepultó la ciudad de Yungay en mayo de 1970?",
                        "options": [
                            "El desprendimiento de una gigantesca masa de hielo y roca del Huascarán que generó un aluvión devastador.",
                            "Una erupción volcánica de lava ardiente que destruyó las iglesias coloniales del valle.",
                            "Un tsunami oceánico que remontó las quebradas de la cordillera hasta la sierra.",
                            "El desbordamiento artificial de una represa hidroeléctrica en construcción."
                        ],
                        "correctIndex": 0,
                        "explanation": "El sismo de 1970 desprendió un colosal bloque de hielo del Huascarán que formó un aluvión a más de 300 km/h que sepultó Yungay."
                    },
                    {
                        "question": "¿Por qué el retroceso de los glaciares de la cordillera Blanca afecta directamente a la costa árida del Perú?",
                        "options": [
                            "Porque el deshielo aporta el caudal del río Santa, que riega proyectos agrícolas y abastece de energía a la costa.",
                            "Porque los glaciares evitan que los barcos pesqueros encallen en las bahías marinas.",
                            "Porque el hielo derretido se evapora y forma nubes que enfrían las aguas de la corriente de Humboldt.",
                            "Porque la costa depende de la exportación de bloques de hielo natural hacia los mercados vecinos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El río Santa capta el agua del deshielo de la cordillera Blanca, alimentando centrales hidroeléctricas e irrigando los valles costeros."
                    }
                ]
            }
        }
    }

    # Story 2: Caral y Chavín
    story_peru_02 = {
        "id": "b2-peruandino-02",
        "title": "Caral y Chavín: El amanecer de las civilizaciones sagradas",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Un viaje arqueológico a los albores de la civilización andina: la Ciudad Sagrada de Caral en el valle de Supe con cinco mil años de antigüedad pacífica, el monumental centro ceremonial de Chavín de Huántar con su enigmático Lanzón Monolítico en las galerías subterráneas y el esplendor orfebre del Señor de Sipán en la costa norte.",
        "characters": [
            "Doctora Ruth Shady",
            "Doctor Walter Alva",
            "Arqueólogo Mario Córdova",
            "Sacerdote de Chavín"
        ],
        "narration": {
            "paragraphs": [
                "En el paisaje desértico del valle de Supe, a unos ciento ochenta kilómetros al norte de Lima, el viento caliente levanta remolinos de polvo sobre terrazas de piedra que durante milenios permanecieron cubiertas por el olvido. Fue en este valle árido donde las investigaciones pioneras iniciadas en 1994 por la arqueóloga peruana Ruth Shady deslumbraron a la comunidad científica internacional: las dataciones de radiocarbono revelaron que las imponentes pirámides truncas, plazas circulares hundidas y conjuntos residenciales de la Ciudad Sagrada de Caral se construyeron hacia el año 3000 antes de Cristo. Caral demostró que la civilización urbana en el continente americano no nació en los valles mesoamericanos, sino en la costa central del Perú, contemporánea de las pirámides de Giza en Egipto y de los zigurats de Mesopotamia.",
                "Lo más fascinante de Caral es que se forjó sin el uso de armas de guerra ni fortificaciones defensivas. Los arqueólogos no hallaron murallas, armas militares ni esqueletos con señales de violencia violenta; en su lugar, desenterraron delicadas flautas traversas talladas en huesos de pelícano y cóndor, cornetas de caracol marino y ofrendas de algodón y peces secos. Caral fue una civilización pacífica sustentada en el intercambio complementario entre agricultores que cultivaban algodón de colores naturales en el valle y pescadores de la caleta de Áspero que extraían anchovetas y moluscos en el océano Pacífico, tejiendo una red comercial que irradiaba bienes e ideas religiosas hacia la selva y la sierra.",
                "Dos milenios más tarde, en el cruce estratégico de dos ríos serranos en Áncash, surgió otro de los hitos fundacionales del mundo andino: el complejo ceremonial de Chavín de Huántar (1200 a 400 a. C.). Ubicado en una garganta montañosa que conecta la costa con la cuenca amazónica, Chavín operó como un prestigioso oráculo panandino donde peregrinaban gobernantes y sacerdotes de regiones lejanas para consultar a los dioses sobre las estaciones agrícolas, las sequías y los movimientos de los astros.",
                "El corazón espiritual de Chavín reside en sus misteriosas galerías subterráneas laberínticas, diseñadas con un avanzado conocimiento acústico e hidráulico. Los arquitectos canalizaron las aguas de los ríos mediante túneles subterráneos que, combinados con el sonido de los caracoles sagrados de concha marina llamados *pututos*, producían en las entrañas oscuras del templo un bramido ensordecedor que imitaba el rugido del jaguar. En la intersección de dos galerías de granito se eleva el Lanzón Monolítico, una escultura colosal de cuatro metros y medio de altura que representa a una deidad antropomorfa con colmillos de felino, garras de ave rapaz y serpientes en lugar de cabellos.",
                "Chavín sentó las bases de una iconografía unificada y de una teocracia que transformó la geografía andina. En las paredes exteriores del templo, las enigmáticas 'cabezas clavas' esculpidas en piedra plasmaban la metamorfosis chamánica de los sacerdotes, quienes ingerían el cactus sagrado de San Pedro para acceder a estados visionarios y comunicarse con las fuerzas creadoras del cosmos.",
                "Hacia los primeros siglos de nuestra era, en los valles costeños de Lambayeque y La Libertad, la cultura Moche llevó la complejidad artística y la organización política a un pináculo deslumbrante. En 1987, el arqueólogo Walter Alva descubrió en Huaca Rajada la tumba intacta del Señor de Sipán, el hallazgo funerario más fastuoso de las Américas. El soberano moche descansaba en su sarcófago de madera rodeado de ornamentos de oro y turquesa, pectorales de conchas *spondylus*, cetros de mando y guardianes armados, evidenciando un virtuosismo metalúrgico que dominaba aleaciones sofisticadas de oro, plata y cobre mucho antes de la llegada de los conquistadores europeos.",
                "Desde las plazas pacíficas de Caral hasta los laberintos sagrados de Chavín y el esplendor real de Sipán, el territorio peruano revela que el ingenio humano floreció en los Andes con originalidad absoluta. Estas culturas milenarias demostraron que la comunión con el mar, la veneración de las montañas y la sabiduría astronómica crearon una civilización inmortal que sentaría los cimientos para el surgimiento del imperio incaico."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué revelaron las investigaciones arqueológicas dirigidas por Ruth Shady en la Ciudad Sagrada de Caral?",
                        "options": [
                            "Que es la civilización más antigua de América (3000 a. C.), coetánea de las primeras ciudades de Egipto y Mesopotamia.",
                            "Que fue un campamento militar romano establecido en las costas del océano Pacífico.",
                            "Que los incas la construyeron durante su expansión hacia el norte en el siglo quince.",
                            "Que fue una colonia fundada por navegantes vikingos que buscaban oro en la sierra."
                        ],
                        "correctIndex": 0,
                        "explanation": "Caral data del 3000 a. C. y es reconocida como la cuna más antigua de la civilización en el continente americano."
                    },
                    {
                        "question": "¿Cómo utilizaban los sacerdotes de Chavín de Huántar los túneles subterráneos de su templo ceremonial?",
                        "options": [
                            "Canalizaban agua y sonidos de caracoles marinos para generar un rugido acústico que sobrecogía a los peregrinos.",
                            "Guardaban pólvora traída de otros continentes para defenderse de invasiones extranjeras.",
                            "Los utilizaban como establos subterráneos para criar rebaños de ganado vacuno.",
                            "Eran almacenes secretos donde guardaban monedas de oro impresas por el Estado."
                        ],
                        "correctIndex": 0,
                        "explanation": "Chavín empleaba conductos hidráulicos y acústicos subterráneos para producir efectos sonoros que emulaban el rugido del jaguar ante el oráculo."
                    },
                    {
                        "question": "¿Por qué el descubrimiento de la tumba del Señor de Sipán en 1987 tuvo repercusión arqueológica mundial?",
                        "options": [
                            "Porque fue la primera tumba real de un monarca precolombino encontrada completamente intacta sin saquear en América.",
                            "Porque contenía manuscritos en latín que describían la ruta hacia la ciudad de El Dorado.",
                            "Porque demostró que los pueblos andinos no sabían trabajar los metales preciosos.",
                            "Porque se halló en la cima nevada del volcán Huascarán a gran altitud."
                        ],
                        "correctIndex": 0,
                        "explanation": "La tumba intacta del Señor de Sipán reveló la fastuosa orfebrería y la sofisticada estructura de poder de la élite moche sin alteraciones."
                    }
                ]
            }
        }
    }

    # Story 3: Tawantinsuyu y Qhapaq Ñan
    story_peru_03 = {
        "id": "b2-peruandino-03",
        "title": "Qhapaq Ñan: Las arterias del imperio de las cuatro regiones",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una inmersión histórica en el corazón del Tawantinsuyu: la colosal red vial del Qhapaq Ñan de más de treinta mil kilómetros, la velocidad legendaria de los corredores chasquis, el registro contable decimal de los quipus, la arquitectura sismorresistente del Cusco y la armonía astronómica de Machu Picchu sobre el cañón del Urubamba.",
        "characters": [
            "Inca Pachacútec",
            "Chasqui Huamán",
            "Quipucamayoc Apocunti",
            "Amauta Tupac"
        ],
        "narration": {
            "paragraphs": [
                "En el siglo XV, bajo la visión transformadora del Inca Pachacútec ('el que transforma la tierra y el tiempo'), una confederación tribal asentada en el fértil valle del río Huatanay protagonizó una de las expansiones geopolíticas, arquitectónicas y culturales más asombrosas y vertiginosas de toda la historia universal. En el curso de unas pocas décadas, la modesta aldea de Cusco dejó de ser una pequeña urbe serrana para erigirse en la capital sagrada del Tawantinsuyu: el monumental imperio de las cuatro regiones unidas que llegó a abarcar más de dos millones de kilómetros cuadrados y congregó a más de diez millones de habitantes pertenecientes a cientos de naciones y etnias diversas a lo largo de la imponente cordillera de los Andes.",
                "Gobernar un territorio tan colosal y abrupto, surcado por desiertos hiperáridos en el litoral costero, cumbres gélidas coronadas de nieve perpetua y quebradas selváticas vertiginosas, demandaba una hazaña de ingeniería civil sin parangón en el mundo preindustrial: el Qhapaq Ñan, o la Gran Red Vial Incaica. Con más de treinta mil kilómetros de calzadas perfectamente empedradas, graderías labradas a golpe de cincel en la roca viva, canales laterales de drenaje pluvial y audaces puentes colgantes trenzados con fibras vegetales de q'oya y paja brava que salvaban abismos insondables sobre ríos rugientes, este sistema articulaba cada rincón del imperio. A intervalos regulares de una jornada de marcha se levantaban los tambos, confortables albergues estatales de aprovisionamiento donde las comitivas oficiales, los ejércitos en desplazamiento y los viajeros encontraban cobijo, raciones de comida seca, mantas abrigadas y descanso reparador.",
                "A través de estas interminables arterias de piedra corrían día y noche los chasquis, jóvenes atletas especialmente adiestrados desde la adolescencia que conformaban el sistema de comunicaciones y correo de postas más rápido y eficiente del planeta en su época. Apostados estratégicamente en pequeñas chozas de relevo denominadas chaskiwasi, espaciadas cada dos o tres kilómetros a lo largo de las rutas, los corredores se transferían órdenes gubernamentales, mensajes verbales cifrados o encomiendas urgentes corriendo a máxima velocidad. Gracias a este relevo ininterrumpido de postas, una orden del emperador recorría más de dos mil kilómetros en cuestión de días, y se cuenta con certeza histórica que el soberano inca degustaba con frecuencia en su palacio cusqueño pescado marino fresco transportado desde las costas del Pacífico en menos de cuarenta y ocho horas.",
                "La administración de esta inmensa maquinaria imperial reposaba sobre dos pilares conceptuales y éticos fundamentales: la reciprocidad comunal (ayni y minka) y la redistribución estatal. En el Tawantinsuyu no se empleaba el dinero ni existían mercados especulativos privados; la cohesión económica se articulaba a través de la mita, un tributo rotativo y obligatorio de mano de obra donde los varones adultos aportaban temporadas de trabajo agrícola, vial o constructivo a favor del Estado. A cambio de esta energía laboral organizada, el soberano garantizaba la absoluta seguridad alimentaria de las familias en años de sequía o heladas, abriendo las monumentales qollqas o depósitos públicos provinciales repletos de maíz desgranado, chuño desecado y charqui curado al sol.",
                "Para llevar un control estadístico escrupuloso de los censos poblacionales, la producción textil, las reservas armamentísticas y los tributos de cada provincia, los incas inventaron y perfeccionaron el quipu. Custodiado e interpretado por los sabios contadores oficiales o quipucamayoc, este instrumento de registro nemotécnico consistía en un cordel grueso principal del que colgaban docenas de hilos secundarios teñidos en tintes vegetales multicolores. Mediante un sistema posicional decimal de nudos simples, dobles y compuestos, los quipus no solo plasmaban minuciosos cómputos aritméticos, sino que según revelan recientes hallazgos arqueológicos codificaban crónicas dinásticas, cantares épicos y genealogías reales.",
                "La maestría incaica halló su cumbre más sublime en la arquitectura lítica sismorresistente. En templos sacros como el Qorikancha y ciclópeas ciudadelas como Sacsayhuamán y Ollantaytambo, los talladores andinos labraron bloques poligonales de basalto, andesita y diorita que encajaban entre sí con precisión milimétrica, sin emplear mortero ni argamasa. Esta asombrosa técnica de junta seca dotaba a los muros de elasticidad dinámica: cuando un violento terremoto sacudía la sierra, los pesados sillares oscilaban y danzaban en sus lechos de piedra disipando la energía telúrica, para acomodarse milagrosamente de nuevo en su lugar al cesar las sacudidas.",
                "En la cima de una cresta escarpada sobre el majestuoso cañón del río Urubamba resplandece la joya suprema del Tawantinsuyu: Machu Picchu. Concebida como una hacienda imperial y santuario de observación astronómica, sus templos solares, plazas ceremoniales y la enigmática roca del Intihuatana demuestran una perfecta comunión entre la edificación humana y la agreste naturaleza andina. El Tawantinsuyu demostró para siempre que el desarrollo civilizatorio alcanza su máxima dignidad cuando sabe tender puentes que hermanan a los pueblos respetando el equilibrio sagrado del universo."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál era la función primordial del Qhapaq Ñan en la gobernanza del imperio del Tawantinsuyu?",
                        "options": [
                            "Conectar militar, económica y administrativamente a las cuatro regiones del imperio a lo largo de treinta mil kilómetros.",
                            "Servir exclusivamente como circuito para carreras atléticas de exhibición.",
                            "Evitar que las aguas de los ríos de la sierra llegaran al océano Pacífico.",
                            "Facilitar la exportación masiva de caballos importados de otros continentes."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Qhapaq Ñan era la columna vertebral que unía militar, administrativa y económicamente los dos millones de km² del imperio."
                    },
                    {
                        "question": "¿En qué consistía el principio andino de la 'mita' en el sistema económico incaico?",
                        "options": [
                            "En un tributo de trabajo comunitario rotativo para obras públicas a cambio de redistribución estatal de bienes.",
                            "En el pago obligatorio de impuestos exclusivamente en monedas de oro y plata.",
                            "En la compraventa libre de tierras comunitarias en subastas comerciales públicas.",
                            "En el comercio marítimo desregulado con corporaciones comerciales privadas."
                        ],
                        "correctIndex": 0,
                        "explanation": "La mita era un sistema rotativo de trabajo comunal que construía infraestructura pública a cambio de seguridad y alimentos del Estado."
                    },
                    {
                        "question": "¿Por qué los muros incas de piedra poligonales son célebres por su ingeniería sismorresistente?",
                        "options": [
                            "Porque ensamblan bloques tallados sin argamasa que vibran y absorben la energía sísmica sin derrumbarse.",
                            "Porque estaban construidos con cemento importado resistente a las heladas.",
                            "Porque las piedras estaban reforzadas con vigas de hierro forjado en sus cimientos.",
                            "Porque se edificaron únicamente en zonas llanas donde jamás se producen temblores."
                        ],
                        "correctIndex": 0,
                        "explanation": "El ensamble sin mortero de piedras almohadilladas disipa el impacto de los sismos, haciendo que los bloques vuelvan a encajar tras la vibración."
                    }
                ]
            }
        }
    }

    # Story 4: Cusco y la Escuela Cusqueña
    story_peru_04 = {
        "id": "b2-peruandino-04",
        "title": "Cusco: El pincel mestizo y el sincretismo de la piedra",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica cultural y estética en el ombligo del mundo: la superposición arquitectónica de iglesias barrocas sobre templos incas en Cusco, la emancipación artística de los maestros quechuas en la Escuela Cusqueña de pintura, los lienzos dorados de Diego Quispe Tito y la presencia oculta de la Pachamama en los retablos virreinales.",
        "characters": [
            "Diego Quispe Tito",
            "Maestro Marcos Zapata",
            "Hermana Asunción",
            "Restaurador Fernando Puma"
        ],
        "narration": {
            "paragraphs": [
                "Caminar por las calles empedradas de la ciudad imperial de Cusco es experimentar un diálogo ininterrumpido entre dos mundos que chocaron con violencia y terminaron fundiéndose en un sincretismo cultural verdaderamente asombroso. En ninguna otra parte del continente americano es más evidente este palimpsesto físico que en la plazoleta de Santo Domingo. Allí, los frailes dominicos levantaron su imponente convento barroco de arcadas renacentistas directamente sobre los muros curvados de andesita negra pulida del Qorikancha, el sagrado Templo del Sol incaico cuyas paredes alguna vez resplandecieron revestidas con planchas macizas de oro laminado. Cuando los catastróficos terremotos de 1650 y 1950 sacudieron la comarca derrumbando las torres de yeso y ladrillo coloniales, los ciclópeos cimientos incas permanecieron absolutamente intactos, proclamando la inmortalidad de la piedra andina.",
                "Tras el devastador sismo de 1650, el célebre obispo Manuel de Mollinedo y Angulo impulsó una reconstrucción monumental sin precedentes que convirtió a Cusco en la capital artística y espiritual de todo el virreinato peruano. Se requería vestir de belleza sacra a docenas de iglesias, capillas y catedrales recién reedificadas, pero los escasos pintores peninsulares llegados de la metrópoli no daban abasto para cubrir los pedidos. Fue entonces cuando los prolíficos talleres locales de artistas indígenas y mestizos comenzaron a pintar febrilmente día y noche, asimilando con deslumbrante rapidez las técnicas del claroscuro tenebrista y la perspectiva renacentista transmitidas en los grabados flamencos e italianos traídos en los galeones de España.",
                "Pronto, el genio y la sensibilidad autóctona desbordaron los estrechos moldes académicos y las rígidas imposiciones doctrinales de los maestros europeos. En 1688 se produjo un hito de rebeldía gremial histórico: los pintores quechuas, liderados por el insigne maestro Diego Quispe Tito, rompieron formalmente con el gremio corporativo español dominado por artistas blancos y fundaron su propia cofradía de arte independiente. Había nacido la Escuela Cusqueña de pintura, un movimiento estético deslumbrante y profundamente original que durante más de un siglo llenó de lienzos luminosos los templos católicos a lo largo de toda la cordillera de los Andes, desde el actual Ecuador hasta los confines del Alto Perú.",
                "Los lienzos de la Escuela Cusqueña se distinguen a primera vista por su encanto lírico, la deliberada ausencia de sombras tenebristas y, sobre todo, por el fastuoso *brocateado*: una técnica minuciosa mediante la cual las túnicas, mantos y coronas de los santos se decoran en relieve con filigranas de pan de oro auténtico aplicado con barnices especiales de goma vegetal. Pero detrás de esa aparente sumisión devota a la liturgia católica latía una resistencia sutil y profundamente poética: los maestros andinos introdujeron de manera subrepticia elementos cardinales de su propia cosmovisión telúrica y su geografía sagrada en los relatos bíblicos.",
                "En las representaciones de la Virgen María, los mantos sagrados adoptaron una forma marcadamente triangular y acampanada, ricamente ornamentados con flores silvestres y ríos serpenteantes. Para la mirada cómplice del feligrés indígena, aquella figura triangular no era únicamente la madre de Jesús según el dogma cristiano, sino la personificación viva de la Pachamama, la Madre Tierra sagrada encarnada en la silueta protectora de los cerros tutelares (*Apus*). Asimismo, los paisajes bíblicos y desérticos de Judea fueron enteramente sustituidos por los fértiles valles andinos del Vilcanota, poblados por papagayos tropicales, vizcachas saltarinas y frondosas arboledas de queñuales nativos.",
                "El cenit de esta originalidad iconográfica cristalizó en los célebres Ángeles Arcabuceros. Inspirados lejanamente en las láminas de tratados militares de la corte de los Austrias pero imbuidos de la milenaria veneración andina por los espíritus celestes del rayo y el trueno (*Illapa*), los maestros cusqueños retrataron seres alados andróginos con rostros serenos, vestidos con fastuosos atuendos cortesanos de terciopelo y brocado, suntuosos sombreros adornados con plumas de avestruz andino (*suri*) y empuñando pesados arcabuces de chispa de los que brotaba fuego celestial purificador.",
                "En la majestuosa Catedral del Cusco, el maestro Marcos Zapata plasmó en 1753 la cima de este mestizaje cultural en su célebre lienzo de la *Última Cena*. En el centro exacto de la mesa redonda, ante un Jesucristo solemne y los doce apóstoles, el plato principal servido no es el cordero pascual de la tradición judía europea, sino un cuy asado crujiente con las patas levantadas en una bandeja de plata reluciente, acompañado de rocotos rojos y cuencos rebosantes de chicha de jora fermentada. Cusco demostró al mundo que el arte plástico constituye el territorio supremo donde las culturas supuestamente subyugadas transforman los símbolos del vencedor para resguardar la antorcha inmortal de su propia memoria histórica."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito histórico acontecido en 1688 consolidó la autonomía estética de la Escuela Cusqueña de pintura?",
                        "options": [
                            "La separación de los pintores indígenas liderados por Diego Quispe Tito del gremio corporativo español.",
                            "La llegada de barcos mercantes que trajeron tubos de pintura al óleo sintética.",
                            "La prohibición imperial del uso de pan de oro en todos los retablos virreinales.",
                            "La destrucción intencional de todas las iglesias coloniales del centro de la ciudad."
                        ],
                        "correctIndex": 0,
                        "explanation": "En 1688 los pintores quechuas rompieron con el gremio peninsular y fundaron su cofradía propia, consagrando la Escuela Cusqueña."
                    },
                    {
                        "question": "¿Qué significado sincrético escondía la silueta triangular acampanada de las Vírgenes cusqueñas para el pueblo andino?",
                        "options": [
                            "Evocaba a la Pachamama y a los cerros sagrados andinos (Apus) bajo el manto protector cristiano.",
                            "Simbolizaba la forma de las carabelas con las que los conquistadores cruzaron el océano Atlántico.",
                            "Representaba el diseño de las pirámides egipcias de la antigüedad clásica.",
                            "Era un homenaje a la geometría militar de las murallas de las fortalezas europeas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El manto triangular identificaba a la Virgen con los montes sagrados y la Pachamama (Madre Tierra)."
                    },
                    {
                        "question": "¿Qué banquete tradicional andino retrató Marcos Zapata en el lienzo de la Última Cena de la Catedral de Cusco?",
                        "options": [
                            "Un cuy asado servido en una fuente de plata acompañado de chicha de maíz.",
                            "Una paella de mariscos importados de las costas del mar Mediterráneo.",
                            "Un banquete de carne de venado con ensalada de frutas tropicales.",
                            "Pan ácimo sin levadura servido exclusivamente con vino tinto de Europa."
                        ],
                        "correctIndex": 0,
                        "explanation": "Zapata pintó un cuy asado tradicional en el centro de la mesa de Jesús, junto a ajíes y copas de chicha andina."
                    }
                ]
            }
        }
    }

    # Story 5: Quechua hoy
    story_peru_05 = {
        "id": "b2-peruandino-05",
        "title": "Runa Simi: El canto vivo del quechua en el siglo XXI",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sociolingüística y cultural sobre el renacimiento contemporáneo del quechua en el Perú: la memoria literaria de José María Arguedas, la sabiduría afectiva de sus sufijos aglutinantes, la dignificación en los medios públicos y el fenómeno juvenil del rap y pop quechua en las plataformas digitales del siglo XXI.",
        "characters": [
            "Renata Flores",
            "Profesor Demetrio Tupacyupanqui",
            "Periodista Clodomiro Landeo",
            "Abuela Mama Asunta"
        ],
        "narration": {
            "paragraphs": [
                "En el patio soleado de una escuela rural en las alturas de Ayacucho, una muchacha de dieciocho años ajusta sus auriculares frente al micrófono de su teléfono móvil. Viste un bordado tradicional de flores andinas multicolores sobre una chaqueta de cuero moderno, y cuando el ritmo sincopado del trap comienza a golpear la pista electrónica, su voz estalla con fuerza eléctrica cantando en Runa Simi, el idioma de la gente. Se trata de Renata Flores, icono del 'quechua pop' urbano que ha acumulado millones de visualizaciones globales interpretando música contemporánea en la lengua de los incas. Para Renata y miles de jóvenes de su generación en Huamanga, Cusco y las barriadas de Lima, el quechua ya no es el símbolo del repliegue campesino o de la discriminación colonial, sino una insignia de orgullo identitario, empoderamiento juvenil y vanguardia estética internacional.",
                "Con casi cuatro millones de hablantes en el territorio peruano y más de ocho millones a lo largo de seis países suramericanos, el quechua es la familia lingüística originaria más extendida demográficamente del continente americano. A pesar de haber sobrevivido a siglos de prohibición punitiva tras la rebelión de Túpac Amaru II en 1780 y a décadas de marginación republicana que pretendió imponer a sangre y fuego el monolingüismo en castellano, la lengua andina mantuvo su latido intacto en el calor protector de los hogares comunales, en los cantos colectivos de la siembra y en la inagotable tradición oral de las abuelas quechuahablantes.",
                "Estructuralmente, el quechua es una lengua aglutinante de una precisión conceptual y una delicadeza poética incomparables. Mediante la adición sucesiva y ordenada de sufijos a una raíz verbal o nominal, un hablante puede expresar matices afectivos, modales y epistemológicos sumamente sutiles que en las lenguas indoeuropeas requerirían largas oraciones subordinadas. Por ejemplo, el sufijo afectivo *-cha* transforma la palabra *urpi* (paloma) en *urpicha*, que significa 'mi adorada y tierna palomita'; mientras que el riguroso sistema de sufijos evidenciales indica con estricta honestidad testimonial si lo que se afirma fue presenciado directamente con los propios ojos (*-mi*), si fue escuchado por boca de terceros (*-si*), o si constituye una conjetura o deducción lógica (*-chá*).",
                "El intelectual que comprendió con mayor profundidad la conmovedora hondura humana y poética del quechua fue el ilustre escritor y antropólogo andahuaylino José María Arguedas (1911-1969). Habiéndose criado desde la más tierna infancia en la intimidad de las cocinas campesinas indígenas donde aprendió a sentir, pensar y amar en quechua antes de dominar el castellano, Arguedas consagró su fecunda obra literaria a tender puentes de comprensión mutua entre los dos grandes ríos culturales del Perú. En novelas maestras como *Los ríos profundos* y *Todas las sangres*, Arguedas protagonizó una verdadera revolución estilística: transfundió la sintaxis musical, el lirismo cósmico y la cosmovisión telúrica del quechua a la prosa castellana, demostrando que la cultura andina no pertenecía a un pasado arqueológico extinto, sino a un presente vivo, combativo y palpitante.",
                "En las últimas décadas, el reconocimiento institucional del quechua ha dado pasos históricos largamente postergados. En 2016, el Instituto Nacional de Radio y Televisión del Perú marcó un hito fundacional con el lanzamiento de *Ñuqanchik* ('Nosotros'), el primer noticiero diario de televisión abierta transmitido íntegramente en lengua quechua, sintonizado cada madrugada por millones de ciudadanos desde las cumbres de los Andes hasta los conos populosos de la capital. Asimismo, la educación intercultural bilingüe se afianza en miles de aulas andinas, y traductores quechuas debidamente acreditados asisten hoy en audiencias judiciales, centros de salud pública y trámites registrales del Estado, garantizando por fin el pleno ejercicio de los derechos civiles para las poblaciones originarias.",
                "El quechua ha conquistado también los estrados académicos universitarios y las ciencias humanas. En 2019, la estudiante cusqueña Roxana Quispe Collantes defendió con máximos honores la primera tesis doctoral escrita y sustentada completamente en lengua quechua en los cuatrocientos sesenta y ocho años de historia ininterrumpida de la Universidad Nacional Mayor de San Marcos en Lima, analizando rigurosamente la obra poética andina de Andrés Alencastre Gutiérrez ante un jurado atónito y conmovido.",
                "El presente del quechua confirma que las lenguas originarias no mueren cuando sus comunidades se apropian con audacia y solvencia de las tecnologías y plataformas del mundo digital contemporáneo. En los versos contestatarios de los jóvenes raperos andinos, en los diccionarios digitales interactivos, en las aplicaciones de mensajería para teléfonos inteligentes y en las asambleas comunales resuena la verdad profunda del Runa Simi: una lengua milenaria que abraza el futuro con la certeza inquebrantable de que mientras haya seres humanos que canten a la Pachamama con respeto, ternura y fraternidad, la voz de los Andes jamás se extinguirá ante los ojos del mundo."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué función cumplen los sufijos evidenciales (-mi, -si, -chá) en la estructura gramatical de la lengua quechua?",
                        "options": [
                            "Indican con precisión si el hablante presenció el hecho, si lo oyó de otros o si es una hipótesis.",
                            "Señalan exclusivamente el tiempo futuro de los verbos irregulares.",
                            "Transforman los nombres comunes en títulos de nobleza aristocrática.",
                            "Obligan a los hablantes a pronunciar las palabras en voz baja y con secreto."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los evidenciales quechuas codifican la fuente del conocimiento: experiencia directa (-mi), información referida (-si) o conjetura (-chá)."
                    },
                    {
                        "question": "¿Cuál fue el aporte literario fundamental de José María Arguedas a las letras peruanas e hispanoamericanas?",
                        "options": [
                            "Transfundir la sintaxis, el lirismo y la cosmovisión del quechua a la prosa narrativa en lengua castellana.",
                            "Escribir tratados de economía bancaria sobre la moneda del virreinato.",
                            "Traducir las comedias clásicas del teatro griego antiguo al idioma francés.",
                            "Rechazar el uso del quechua en favor de la literatura moderna en inglés."
                        ],
                        "correctIndex": 0,
                        "explanation": "Arguedas revolucionó la literatura hispanoamericana impregnando la prosa castellana con la música y el pensamiento del quechua."
                    },
                    {
                        "question": "¿Qué acontecimiento histórico pionero protagonizó Roxana Quispe Collantes en la Universidad de San Marcos en 2019?",
                        "options": [
                            "Sustentó con honores la primera tesis doctoral redactada íntegramente en quechua en la historia de la universidad.",
                            "Fue nombrada decana vitalicia de la Facultad de Medicina Humana.",
                            "Descubrió un nuevo yacimiento arqueológico bajo las aulas del campus universitario.",
                            "Fundó la primera estación de radio comercial transmitida desde un helicóptero."
                        ],
                        "correctIndex": 0,
                        "explanation": "Quispe Collantes defendió en 2019 la primera tesis doctoral en quechua en los casi 500 años de la Universidad de San Marcos."
                    }
                ]
            }
        }
    }

    # Story 6: Capstone regional story: El ombligo del mundo
    story_peru_capstone = {
        "id": "b2-peruandino-consolidation",
        "title": "El ombligo del mundo: La herencia inagotable de los Andes peruanos",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis panorámica de los Estudios Regionales sobre el Perú andino: la geomorfología de la cordillera Blanca y el río Santa, las civilizaciones milenarias de Caral y Chavín, la administración y la ingeniería del Tawantinsuyu a lo largo del Qhapaq Ñan, el sincretismo virreinal cusqueño y la vitalidad contemporánea del quechua.",
        "characters": [
            "Pachacútec",
            "José María Arguedas",
            "Micaela Bastidas",
            "Amauta Quispe"
        ],
        "narration": {
            "paragraphs": [
                "En el corazón geográfico y espiritual del continente suramericano, el territorio andino del Perú se alza como uno de los centros civilizatorios originarios de la historia de la humanidad. Desde las costas áridas bañadas por el mar Pacífico hasta las cumbres coronadas de hielo perpetuo que desafían al firmamento y los templados valles interandinos donde maduran centenares de variedades nativas de papa, quinua y maíz, los Andes peruanos representan un laboratorio milenario irrepetible. En este escarpado escenario vertical de múltiples pisos ecológicos, la creatividad y la tenacidad humanas demostraron que el aislamiento orográfico y la severidad del clima no constituyen barreras insuperables, sino poderosos acicates para forjar civilizaciones de prodigiosa sabiduría ecológica y sólida armonía comunitaria.",
                "En las alturas septentrionales del departamento de Áncash, la imponente cordillera Blanca despliega sus más de setecientos glaciares tropicales custodiados por la silueta colosal del nevado Huascarán. Este invalorable reservorio natural de agua dulce congelada no solo alimenta los mitos ancestrales de los Apus tutelares que velan por el destino de las comunidades campesinas, sino que constituye el corazón hidrológico insustituible de la sierra y la costa: a través del caudaloso río Santa, sus aguas de deshielo irrigan florecientes valles agroindustriales en pleno desierto y abastecen de energía hidroeléctrica a las ciudades modernas, recordando a la sociedad contemporánea la urgencia ineludible de custodiar los glaciares frente a los embates devastadores del calentamiento global.",
                "Milenios antes de que los primeros imperios organizados conquistaran las quebradas cordilleranas, en el valle costero de Supe germinó la Ciudad Sagrada de Caral hace cinco mil años. Reconocida unánimemente como la cuna civilizatoria más antigua de todo el continente americano, contemporánea de las pirámides del Egipto faraónico, Caral articuló un temprano modelo de vida urbana pacífica sustentado en la observación astronómica, la música sagrada, la domesticación del algodón y el intercambio complementario y fraterno entre pescadores del litoral y agricultores del valle. Este humanismo fundacional andino floreció siglos más tarde en el santuario de Chavín de Huántar, cuyo oráculo subterráneo, sus galerías laberínticas y su enigmático Lanzón Monolítico irradiaron una profunda unificación religiosa a través del culto al felino sagrado.",
                "Sobre estos cimientos civilizatorios milenarios, los gobernantes incas erigieron en el siglo XV el colosal Tawantinsuyu, articulando en menos de una centuria un imperio sin parangón que abarcó dos millones de kilómetros cuadrados a lo largo de seis repúblicas suramericanas modernas. Mediante el Qhapaq Ñan, una colosal red vial empedrada de más de treinta mil kilómetros recorrida con increíble presteza por los esforzados chasquis, y apoyándose en el registro aritmético de los quipus que fiscalizaban censos poblacionales y provisiones provinciales, el Tawantinsuyu demostró que el trabajo rotativo solidario de la mita y los valores éticos de la reciprocidad comunitaria podían garantizar bienestar y abundancia para millones de personas sin necesidad de instaurar monedas mercantiles ni mercados especulativos.",
                "En la capital imperial de Cusco, la piedra incaica resistió victoriosa el embate destructivo de las guerras de conquista y la violencia ciega de los terremotos. Edificadas directamente sobre los cimientos sagrados del Templo del Sol o Qorikancha, las iglesias católicas y los conventos virreinales fueron colonizados estéticamente desde adentro por los maestros indígenas y mestizos de la Escuela Cusqueña. Bajo el pincel luminoso y el brocateado de oro de artífices insignes como Diego Quispe Tito y Marcos Zapata, los ángeles empuñaron arcabuces andinos celestiales, la Virgen María adoptó la silueta cónica protectora de la Pachamama y Jesucristo cenó cuy asado en el altar mayor de la Catedral, demostrando que el arte pictórico funcionó como un escudo inexpugnable para preservar intacta la identidad andina.",
                "Esa misma memoria ancestral palpita hoy con renovado vigor en la lengua quechua o Runa Simi, hablada por millones de ciudadanos plenamente orgullosos de su estirpe en todo el país. Como lo proclamara con pasión el gran José María Arguedas en sus conmovedores cantos, el quechua no es un vestigio fósil del pasado, sino una lengua contemporánea rebosante de ternura en sus sufijos aglutinantes, que hoy informa con solvencia profesional en los noticieros televisivos del Estado, se defiende en tesis doctorales universitarias y conquista a las juventudes globales en los compases electrónicos del pop y el rap andino.",
                "Al contemplar con detenimiento la vasta trayectoria inmemorial del Perú andino, el visitante comprende cabalmente por qué el Cusco fue bautizado con reverencia como 'el ombligo del mundo'. En esta encrucijada donde el pasado pétreo dialoga de igual a igual con las tecnologías del porvenir digital, los Andes peruanos continúan enseñando a la humanidad entera que la dignidad innegociable de los pueblos, la devoción por la Madre Tierra y la solidaridad colectiva son los pilares inconmovibles sobre los que se edifica una civilización verdaderamente libre, sabia y duradera."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué tres elementos fundamentales articularon la integración territorial del Tawantinsuyu en los Andes?",
                        "options": [
                            "La red vial del Qhapaq Ñan, el sistema de mensajería de los chasquis y la contabilidad en quipus.",
                            "El uso generalizado de monedas de plata, la navegación en carabelas y el ferrocarril a vapor.",
                            "La construcción de murallas chinas continuas a lo largo de las fronteras imperiales.",
                            "El comercio bancario regulado por bolsas de valores financieras privadas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Tawantinsuyu unificó su inmenso territorio mediante el Qhapaq Ñan, los veloces chasquis y los quipus administrativos."
                    },
                    {
                        "question": "¿De qué manera el arte de la Escuela Cusqueña sirvió como vehículo de preservación cultural para los pueblos andinos?",
                        "options": [
                            "Incorporó símbolos de la cosmovisión originaria como la Pachamama, fauna local y platos tradicionales en los relatos bíblicos.",
                            "Copió estrictamente los manuales de pintura flamenca sin alterar ningún detalle original.",
                            "Obligó a los sacerdotes católicos a pintar exclusivamente paisajes desérticos sin figuras humanas.",
                            "Sustituyó todos los templos religiosos por galerías comerciales de venta de cerámicas."
                        ],
                        "correctIndex": 0,
                        "explanation": "La Escuela Cusqueña integró elementos andinos (Pachamama en la Virgen, fauna local, cuy) dentro de la imaginería religiosa virreinal."
                    },
                    {
                        "question": "¿Cuál es la vigencia sociolingüística del quechua en el Perú contemporáneo del siglo XXI?",
                        "options": [
                            "Es hablado por millones de personas y protagoniza un renacimiento cultural en la música juvenil, la televisión y la academia.",
                            "Ha desaparecido por completo de las ciudades y solo subsiste en grabaciones fonográficas antiguas.",
                            "Ha sido reemplazado oficialmente por el latín en todas las instituciones del Estado.",
                            "Se utiliza exclusivamente en ceremonias turísticas sin presencia en los hogares familiares."
                        ],
                        "correctIndex": 0,
                        "explanation": "El quechua es hablado por millones de ciudadanos y vive un auge en música urbana, medios públicos y tesis universitarias."
                    }
                ]
            }
        }
    }

    # Helper to convert story dictionary into valid schema structure
    def to_schema_story(s):
        paras = s["narration"]["paragraphs"]
        questions = s["narration"]["pedagogical"]["comprehensionQuestions"]
        return {
            "id": s["id"],
            "title": s["title"],
            "level": s["level"],
            "lesson": s["lesson"],
            "type": s["type"],
            "estimatedMinutes": s.get("estimatedMinutes", 8),
            "summary": s["summary"],
            "characters": s["characters"],
            "paragraphs": [{"type": "narration", "text": p} for p in paras],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": questions
                }
            }
        }

    # Write stories
    # Core classic story:
    write_json(f"stories/classics/b2/{c_unit}.json", to_schema_story(story_core_18))
    # Regional lesson stories:
    write_json(f"stories/world/b2/{r1}.json", to_schema_story(story_peru_01))
    write_json(f"stories/world/b2/{r2}.json", to_schema_story(story_peru_02))
    write_json(f"stories/world/b2/{r3}.json", to_schema_story(story_peru_03))
    write_json(f"stories/world/b2/{r4}.json", to_schema_story(story_peru_04))
    write_json(f"stories/world/b2/{r5}.json", to_schema_story(story_peru_05))
    write_json(f"stories/world/b2/{r6_con}.json", to_schema_story(story_peru_capstone))
    write_json(f"stories/world/b2/{r_unit}.json", to_schema_story(story_peru_capstone))

    # -------------------------------------------------------------------------
    # 5. LESSON FILES (6 Core + 6 Regional)
    # -------------------------------------------------------------------------
    core_lessons_info = [
        ("b2-18-01", "lesson.b2.18.01", "Verbos declarativos y aseverativos formales",
         "Deploy assertive and declarative reporting verbs (aseverar, sostener, recalcar) to specify conviction and formal attribution.",
         "verbos declarativos y aseverativos formales en el registro periodístico y académico",
         ["Select precise assertive verbs (aseverar, sostener) instead of overusing 'decir'.", "Emphasize critical distinctions using 'recalcar' and 'puntualizar'.", "Avoid incorrect 'dequeísmo' in formal assertive clauses."]),
        ("b2-18-02", "lesson.b2.18.02", "Verbos de disputa, refutación y réplica dialéctica",
         "Master verbs of dispute, refutation, and legal challenge (desmentir, refutar, impugnar, rebatir) in debate.",
         "verbos de controversia dialéctica, refutación argumentativa y desmentido institucional",
         ["Distinguish between declaring falsehood (desmentir) and proving invalidity (refutar, rebatir).", "Challenge the legal validity of acts and rulings using 'impugnar'.", "Apply correct subjunctive mood following 'desmentir que' when truth value is rejected."]),
        ("b2-18-03", "lesson.b2.18.03", "Verbos de advertencia, prevención y recordatorio",
         "Deploy communication verbs of warning, risk anticipation, and legal reminders (advertir, alertar, conminar).",
         "verbos de advertencia, precaución institucional y recordatorio legal",
         ["Master the indicative/subjunctive alternation with 'advertir que'.", "Deploy 'alertar sobre/de que' to anticipate public risks.", "Formulate formal institutional injunctions using 'conminar a que + subjuntivo'."]),
        ("b2-18-04", "lesson.b2.18.04", "Verbos de reproche, censura y evaluación crítica",
         "Express retrospective moral censure, critique, and ethical reproach using specialized reporting verbs (reprochar, censurar).",
         "verbos de reproche ético, censura institucional y cuestionamiento crítico",
         ["Report moral accusations and omissions using 'reprochar (a alguien) que + subjuntivo'.", "Formulate institutional censure using 'censurar' and 'recriminar'.", "Critique procedural and ethical legitimacy using 'cuestionar que + subjuntivo'."]),
        ("b2-18-05", "lesson.b2.18.05", "Verbos de conjetura, sospecha y distanciamiento epistémico",
         "Employ journalistic distancing verbs (alegar, conjeturar, insinuar) to report claims without committing to their truth value.",
         "verbos de distanciamiento epistémico, cautela informativa y conjetura en la prensa",
         ["Deploy 'alegar que' to report unverified legal claims neutrally.", "Indicate subtle oblique hints using 'insinuar que'.", "Frame analytical hypotheses and speculative scenarios using 'conjeturar' and 'especular'."])
    ]

    for s, lid, tit, gol, gmr, items in core_lessons_info:
        write_json(f"lessons/b2/{s}.json", {
            "id": lid, "title": tit, "level": "B2", "goal": gol, "grammar": gmr,
            "sections": [
                {"type": "goal", "items": items},
                {"type": "recycle", "count": 3},
                {"type": "grammar", "ref": f"grammar/b2/{s}-a-gr.json"},
                {"type": "vocabulary", "ref": f"vocabulary/b2/{s}-voc.json"},
                {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex01", f"{s}.ex02", f"{s}.ex03", f"{s}.ex04"]},
                {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex05"]},
                {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex06"]}
            ]
        })

    # Core Consolidation Lesson
    write_json(f"lessons/b2/{l6_con}.json", {
        "id": "lesson.b2.18.consolidation",
        "title": "Consolidación B2: Verbos retóricos y El mundo es ancho y ajeno",
        "level": "B2",
        "goal": "Synthesize rhetorical reporting verbs of assertion, refutation, warning, and critique through Ciro Alegría's indigenist masterpiece El mundo es ancho y ajeno.",
        "grammar": "síntesis de verbos de comunicación retórica y adaptación de El mundo es ancho y ajeno",
        "sections": [
            {"type": "goal", "items": [
                "Select nuanced communication verbs to convey precise rhetorical stance in formal discourse.",
                "Employ epistemic distancing (alegar, conjeturar) to maintain objective neutrality.",
                "Analyze the tragic struggle of the Andean indigenous community against feudal dispossession."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{l6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Utilizo verbos aseverativos (aseverar, sostener, recalcar) con propiedad y rigor.",
                "Distingo entre desmentir una falsedad y refutar una tesis con argumentos.",
                "Manejo la alternancia de modo con verbos de advertencia (advertir que + ind./subj.).",
                "Aplico verbos de distanciamiento epistémico (alegar, insinuar) en crónicas formales."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-peruandino-01", "lesson.b2.peruandino.01", "La cordillera Blanca y los glaciares andinos",
         "Explore the high-altitude geography of the Cordillera Blanca, the Huascarán peak, and tropical glacial hydrology.",
         "geomorfología de la cordillera Blanca, glaciología tropical e hidrología del río Santa",
         ["Analyze the physical geography of Huascarán, Alpamayo, and the Callejón de Huaylas.", "Examine the vital dry-season role of glacial runoff for coastal and highland irrigation.", "Deploy glacial, mountainous, and avalanche risk vocabulary (glaciar, aluvión, quebrada, morrena)."]),
        ("b2-peruandino-02", "lesson.b2.peruandino.02", "Civilizaciones preincas: Caral, Chavín y Moche",
         "Investigate the millenary pre-Inca cultures: Caral's 5,000-year-old sacred city, Chavín's oracle, and the Lord of Sipán's gold regalia.",
         "arqueología preincaica: Caral (3000 a. C.), oráculo de Chavín y orfebrería moche",
         ["Analyze Caral as the oldest independent American civilization.", "Explore the acoustic architecture and feline deities of Chavín de Huántar.", "Deploy archaeological, monumental, and metallurgical vocabulary (civilización, piramidal, oráculo, monolito)."]),
        ("b2-peruandino-03", "lesson.b2.peruandino.03", "Tawantinsuyu y la red vial del Qhapaq Ñan",
         "Examine Inca imperial statecraft, the 30,000-km Qhapaq Ñan road network, chasqui messengers, quipu records, and seismic masonry.",
         "organización del Tawantinsuyu, ingeniería del Qhapaq Ñan y arquitectura sismorresistente",
         ["Trace the imperial administration across four regions and the Qhapaq Ñan highway.", "Analyze the economic principles of reciprocity (ayni), rotational labor (mita), and quipu records.", "Deploy Inca statecraft and engineering vocabulary (chasqui, quipu, almohadillado, sismorresistente)."]),
        ("b2-peruandino-04", "lesson.b2.peruandino.04", "Cusco colonial y la Escuela Cusqueña de pintura",
         "Explore the architectural palimpsest of Cusco, the indigenous painters' guild of Diego Quispe Tito, and religious syncretism.",
         "barroco virreinal andino, Escuela Cusqueña de pintura y sincretismo de la Pachamama",
         ["Analyze the architectural palimpsest of Santo Domingo built over the Qorikancha.", "Explore the unique Andean motifs in Cusqueño paintings (Harquebusier Angels, Pachamama virgins).", "Deploy art history, Baroque painting, and syncretism vocabulary (sincretismo, palimpsesto, brocateado, arcángel)."]),
        ("b2-peruandino-05", "lesson.b2.peruandino.05", "El quechua hoy: vitalidad lingüística y literatura andina",
         "Analyze the contemporary vitality of the Quechua language (Runa Simi), Arguedas's bilingual legacy, and youth Quechua urban music.",
         "sociolingüística andina, morfología aglutinante del quechua y revitalización contemporánea",
         ["Explore the agglutinative precision and evidential suffixation of Runa Simi.", "Analyze José María Arguedas's translation of Quechua poetic syntax into Spanish.", "Deploy sociolinguistic, indigenous dignity, and bilingualism vocabulary (aglutinante, oralidad, dignificación, cosmovisión)."])
    ]

    for s, lid, tit, gol, gmr, items in reg_lessons_info:
        write_json(f"lessons/b2/{s}.json", {
            "id": lid, "title": tit, "level": "B2", "goal": gol, "grammar": gmr,
            "sections": [
                {"type": "goal", "items": items},
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": f"stories/world/b2/{s}.json"},
                {"type": "grammar", "ref": f"grammar/b2/{s}-a-gr.json"},
                {"type": "vocabulary", "ref": f"vocabulary/b2/{s}-voc.json"},
                {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex01", f"{s}.ex02", f"{s}.ex03", f"{s}.ex04"]},
                {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex05"]},
                {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex06"]}
            ]
        })

    # Regional Consolidation Lesson
    write_json(f"lessons/b2/{r6_con}.json", {
        "id": "lesson.b2.peruandino.consolidation",
        "title": "Consolidación Regional: El ombligo del mundo y los Andes peruanos",
        "level": "B2",
        "goal": "Consolidate regional studies on Andean Peru: Cordillera Blanca glaciation, pre-Inca foundations, Tawantinsuyu statecraft, Cusqueño syncretism, and Quechua vitality.",
        "grammar": "síntesis de estudios regionales del Perú andino: Tawantinsuyu, Qhapaq Ñan y Escuela Cusqueña",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize high-altitude glacial hydrology and mountain ecosystem management.",
                "Appreciate the millennia-old architectural and administrative legacy from Caral to the Incas.",
                "Reflect on cultural syncretism in Cusqueño art and the borderless vitality of Quechua."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r6_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{r6_con}-ex.json", "exerciseRefs": [f"{r6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la importancia hidrológica y los riesgos climáticos de la cordillera Blanca.",
                "Reconozco la antigüedad de Caral y la influencia ceremonial de Chavín de Huántar.",
                "Explico la ingeniería del Qhapaq Ñan y el funcionamiento administrativo del Tawantinsuyu.",
                "Valoro el sincretismo de la Escuela Cusqueña y la vitalidad contemporánea del quechua."
            ]}
        ]
    })

    print("Completed LatAm Unit 18 (Peru Andino) generation!")

    # -------------------------------------------------------------------------
    # 6. UPDATE CURRICULUM UNITS (b2.json)
    # -------------------------------------------------------------------------
    b2_units_path = LATAM_DIR / "curriculum" / "units" / "b2.json"
    b2_units = json.loads(b2_units_path.read_text(encoding="utf-8"))
    
    # Check if Unit 18 entries already exist
    has_core_18 = any(u.get("title") == "Rhetorical Reporting Verbs" for u in b2_units)
    has_reg_18 = any(u.get("title") == "Peru I: Cusco, Tawantinsuyu & Andean Worldview" for u in b2_units)
    
    if not has_core_18:
        b2_units.append({
            "title": "Rhetorical Reporting Verbs",
            "stems": [
                f"{c_unit}-01",
                f"{c_unit}-02",
                f"{c_unit}-03",
                f"{c_unit}-04",
                f"{c_unit}-05",
                f"{c_unit}-consolidation"
            ],
            "track": "core"
        })
    if not has_reg_18:
        b2_units.append({
            "title": "Peru I: Cusco, Tawantinsuyu & Andean Worldview",
            "stems": [
                f"{r_unit}-01",
                f"{r_unit}-02",
                f"{r_unit}-03",
                f"{r_unit}-04",
                f"{r_unit}-05",
                f"{r_unit}-consolidation"
            ],
            "track": "regional"
        })
    
    b2_units_path.write_text(json.dumps(b2_units, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated curriculum/units/b2.json with Unit 18!")

    # -------------------------------------------------------------------------
    # 7. Word Count Audit for Stories
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_18", story_core_18),
        ("story_peru_01", story_peru_01),
        ("story_peru_02", story_peru_02),
        ("story_peru_03", story_peru_03),
        ("story_peru_04", story_peru_04),
        ("story_peru_05", story_peru_05),
        ("story_peru_capstone", story_peru_capstone)
    ]
    print("\n--- Story Word Count Audit ---")
    for name, s in stories_to_audit:
        full_text = " ".join(s["narration"]["paragraphs"])
        wc = count_words(full_text)
        status = "OK (650-825)" if 650 <= wc <= 825 else f"FAILED ({wc} words, must be 650-825)"
        print(f"{name:22}: {wc:4} words -> {status}")
        assert 650 <= wc <= 825, f"Story {name} has {wc} words, out of bounds!"

if __name__ == "__main__":
    main()
