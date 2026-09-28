#!/usr/bin/env python3
"""
Generate complete curriculum content for Latin American Spanish (es-latam)
B2 Unit Pair 17:
- Core Unit 17: b2-17 (Reported Speech in Past Frames / El discurso referido en el pasado)
- Regional Unit 17: b2-ecuador (Ecuador: Plurinationalism, The Equatorial Andes & The Galápagos)

Adheres strictly to all schemas:
- Vocabulary schema: id, lesson, title, words [{lemma, translation, pos}]
- Grammar schema: 2-column tables (rows: [[es, en], ...]), no headers
- Exercise schema: matching, fill-blank, multiple-choice, sentence-builder, dialogue-complete, dictation
- Lesson schema: id, level, title, sections
- Story schema: id, title, level, lesson, type, estimatedMinutes, summary, characters, narration
  with comprehensionQuestions inside narration.pedagogical.comprehensionQuestions
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
        # Core Unit 17 skills
        "b2-17-vocab": {
            "kind": "vocabulary",
            "level": "b2",
            "name": "Reported Speech & Discourse Vocabulary"
        },
        "discurso-indirecto-tiempos-pasados": {
            "kind": "grammar",
            "level": "b2",
            "name": "Backshifting Statements in Past Reported Speech"
        },
        "discurso-indirecto-interrogativas": {
            "kind": "grammar",
            "level": "b2",
            "name": "Reporting Questions in Past Frames"
        },
        "discurso-indirecto-peticiones-subjuntivo": {
            "kind": "grammar",
            "level": "b2",
            "name": "Reporting Commands & Petitions with Subjunctive"
        },
        "discurso-indirecto-deicticos": {
            "kind": "grammar",
            "level": "b2",
            "name": "Deictic Shifts in Indirect Discourse"
        },
        "discurso-indirecto-libre": {
            "kind": "grammar",
            "level": "b2",
            "name": "Free Indirect Discourse in Prose"
        },
        # Regional Unit 17 (Ecuador) skills
        "b2-ecuador-vocab": {
            "kind": "vocabulary",
            "level": "b2",
            "name": "Ecuadorian Geography, Politics & Ecology Vocabulary"
        },
        "ecuador-volcanes-callejon-interandino": {
            "kind": "grammar",
            "level": "b2",
            "name": "Inter-Andean Corridor & Volcanoes Geography"
        },
        "ecuador-galapagos-evolucion-darwin": {
            "kind": "grammar",
            "level": "b2",
            "name": "Galapagos Biodiversity & Evolutionary Science"
        },
        "ecuador-conaie-movimiento-indigena": {
            "kind": "grammar",
            "level": "b2",
            "name": "Indigenous Mobilization & the CONAIE Movement"
        },
        "ecuador-constitucion-derechos-naturaleza": {
            "kind": "grammar",
            "level": "b2",
            "name": "Rights of Nature & Sumak Kawsay Jurisprudence"
        },
        "ecuador-yasuni-petroleo-amazonia": {
            "kind": "grammar",
            "level": "b2",
            "name": "Yasuní Oil Exploitation & Popular Referendum"
        }
    }
    
    reg["skills"].update(new_skills)
    reg_path.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated skill-registry.json for Unit 17")

    # Grammar titles for Grammar Driller (starts lowercase, <= 11 words, plain CEFR English)
    titles_path = LATAM_DIR / "indexes" / "grammar-titles.json"
    titles = json.loads(titles_path.read_text(encoding="utf-8")) if titles_path.is_file() else {}
    
    new_titles = {
        "discurso-indirecto-tiempos-pasados": "backshifting statements in past reported speech frames",
        "discurso-indirecto-interrogativas": "reporting questions and interrogative clauses in the past",
        "discurso-indirecto-peticiones-subjuntivo": "reporting commands and requests with the subjunctive",
        "discurso-indirecto-deicticos": "shifting temporal and spatial deictic markers in narratives",
        "discurso-indirecto-libre": "free indirect discourse in narrative prose",
        "ecuador-volcanes-callejon-interandino": "volcanic geography of the equatorial valley corridor",
        "ecuador-galapagos-evolucion-darwin": "wildlife and evolutionary biology in oceanic island sanctuaries",
        "ecuador-conaie-movimiento-indigena": "indigenous political mobilization and grassroots confederations",
        "ecuador-constitucion-derechos-naturaleza": "constitutional rights of nature and biocentric jurisprudence",
        "ecuador-yasuni-petroleo-amazonia": "oil extraction in the rainforest and environmental referendums"
    }
    titles.update(new_titles)
    titles_path.write_text(json.dumps(titles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json for Unit 17")

    # -------------------------------------------------------------------------
    # 2. CORE UNIT 17: b2-17 (Reported Speech in Past Frames)
    # -------------------------------------------------------------------------
    c_unit = "b2-17"

    # --- Lesson 1: b2-17-01 ---
    l1 = f"{c_unit}-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.17.01",
        "lesson": l1,
        "title": "Verbos introductorios y traslación de asertos",
        "theme": "Léxico de comunicación indirecta, testimonio y aserción",
        "words": [
            {"lemma": "afirmar", "translation": "to assert, to affirm", "pos": "verb"},
            {"lemma": "declarar", "translation": "to declare, to state formally", "pos": "verb"},
            {"lemma": "comunicado", "translation": "official communique, statement", "pos": "noun"},
            {"lemma": "testimonio", "translation": "testimony, witness account", "pos": "noun"},
            {"lemma": "correlación", "translation": "tense correlation, concordance", "pos": "noun"},
            {"lemma": "anterioridad", "translation": "anteriority, prior occurrence", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.17.01.discurso-indirecto-tiempos-pasados",
        "title": "El estilo indirecto con verbo principal en pasado: traslación temporal de asertos",
        "sections": [
            {
                "type": "text",
                "content": "Cuando reproducimos las palabras de otra persona y el verbo introductorio se halla en un tiempo pretérito (*dijo, afirmó, explicó, comunicó*), los tiempos verbales del mensaje original experimentan una **traslación temporal obligatoria hacia el pasado** (correlación de tiempos o *consecutio temporum*).\n\nEsta regla formal garantiza la coherencia temporal de la narración, desplazando la perspectiva enunciativa desde el presente del emisor original hasta el marco pretérito del relator."
            },
            {
                "type": "table",
                "title": "Tabla de correspondencias temporales de asertos",
                "rows": [
                    ["Presente ('Trabajo aquí') -> Imperfecto", "Dijo que trabajaba allí."],
                    ["Indefinido ('Llegué ayer') -> Pluscuamperfecto", "Afirmó que había llegado el día anterior."],
                    ["Pretérito Perfecto ('He leído el informe') -> Pluscuamperfecto", "Comentó que había leído el informe."],
                    ["Futuro Simple ('Firmaremos hoy') -> Condicional Simple", "Aseguró que firmarían ese día."],
                    ["Futuro Compuesto ('Habré terminado') -> Condicional Compuesto", "Sostuvo que habría terminado."],
                    ["Imperfecto ('Vivía en Quito') -> Imperfecto (invariable)", "Aclaró que vivía en Quito."]
                ]
            },
            {
                "type": "tip",
                "content": "El pretérito imperfecto y el pluscuamperfecto permanecen inalterables en la traslación indirecta porque ya representan el pasado duradero o anterior: *'Yo ya había salido' -> Declaró que ya había salido*."
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
                    ["afirmar", "to state firmly"],
                    ["comunicado", "official statement"],
                    ["testimonio", "firsthand witness account"],
                    ["correlación", "tense agreement in grammar"]
                ],
                "teaches": ["b2-17-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El portavoz declaró a la prensa que el ministro __ el decreto esa misma tarde. (firmar)",
                "answer": "firmaría",
                "english": "The spokesperson declared to the press that the minister would sign the decree that very afternoon.",
                "teaches": ["discurso-indirecto-tiempos-pasados"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se traslada al estilo indirecto en pasado la afirmación: 'Compré las acciones en la bolsa'?",
                "options": [
                    "Explicó que había comprado las acciones en la bolsa.",
                    "Explicó que comprará las acciones en la bolsa.",
                    "Explicó que compra las acciones en la bolsa.",
                    "Explicó que compraría las acciones en la bolsa."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-tiempos-pasados"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "geólogo", "afirmó", "que", "el", "volcán", "había", "entrado", "en", "actividad."],
                "solution": ["El", "geólogo", "afirmó", "que", "el", "volcán", "había", "entrado", "en", "actividad."],
                "english": "The geologist stated that the volcano had entered into activity.",
                "teaches": ["discurso-indirecto-tiempos-pasados"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Reportera", "text": "¿Qué dijo el presidente ejecutivo tras salir de la cumbre energética?"},
                    {"speaker": "Asistente", "text": "_____"}
                ],
                "options": [
                    "Aseguró que la empresa aumentaría la producción de energía eólica en los próximos tres años.",
                    "Asegura que vendrá mañana por la tarde a la oficina.",
                    "El café colombiano tiene un aroma sumamente agradable.",
                    "Los contratos se firman con pluma de tinta negra."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-tiempos-pasados"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La delegada señaló que habían alcanzado un consenso preliminar antes de suspender la sesión.",
                "english": "The delegate pointed out that they had reached a preliminary consensus before suspending the session.",
                "teaches": ["discurso-indirecto-tiempos-pasados"]
            }
        ]
    })

    # --- Lesson 2: b2-17-02 ---
    l2 = f"{c_unit}-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.17.02",
        "lesson": l2,
        "title": "Preguntas indirectas e indagación en pasado",
        "theme": "Léxico de interrogación, indagación judicial y diplomática",
        "words": [
            {"lemma": "indagar", "translation": "to investigate, to inquire into", "pos": "verb"},
            {"lemma": "inquirir", "translation": "to inquire, to ask formally", "pos": "verb"},
            {"lemma": "cuestionario", "translation": "questionnaire, survey", "pos": "noun"},
            {"lemma": "deliberación", "translation": "deliberation, debate", "pos": "noun"},
            {"lemma": "averiguación", "translation": "fact-finding investigation", "pos": "noun"},
            {"lemma": "esclarecer", "translation": "to clarify, to shed light on", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.17.02.discurso-indirecto-interrogativas",
        "title": "Preguntas indirectas y traslación interrogativa en pasado",
        "sections": [
            {
                "type": "text",
                "content": "Al reportar interrogaciones con verbos introductorios en pasado (*preguntó, quiso saber, indagó, averiguó*), distinguimos dos estructuras fundamentales:\n\n1. **Interrogativas totales (sí/no):** Se introducen con la conjunción **si** (sin tilde), aplicando la misma traslación temporal que en los asertos (*'¿Vendrás mañana?' -> Me preguntó si vendría al día siguiente*).\n\n2. **Interrogativas parciales:** Mantienen el pronombre o adverbio interrogativo con su tilde diacrítica (*qué, cuándo, dónde, cómo, por qué, quién*), sin signos de interrogación y con traslación temporal de tiempos verbales."
            },
            {
                "type": "table",
                "title": "Traslación de preguntas directas a estilo indirecto",
                "rows": [
                    ["'¿Llegó el informe?' -> si + pluscuamperfecto", "Me preguntó si había llegado el informe."],
                    ["'¿Cuándo saldrán?' -> cuándo + condicional", "Quiso saber cuándo saldrían."],
                    ["'¿Dónde vives?' -> dónde + imperfecto", "Indagó dónde vivía yo en ese momento."],
                    ["'¿Por qué renunciaste?' -> por qué + pluscuamperfecto", "Averiguó por qué había renunciado."],
                    ["'¿Quién es el responsable?' -> quién + imperfecto", "Inquirió quién era el responsable."],
                    ["'¿Podemos pasar?' -> si + imperfecto", "Preguntaron si podían pasar."]
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que en las preguntas indirectas **nunca** se colocan signos de interrogación (¿ ?). Los interrogativos (*qué, quién, cuál, cuándo, dónde, cómo*) conservan siempre su tilde ortográfica para distinguirlos de los pronombres relativos."
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
                    ["indagar", "to look deeply into"],
                    ["inquirir", "to ask in formal inquiry"],
                    ["deliberación", "formal thoughtful debate"],
                    ["esclarecer", "to bring truth to light"]
                ],
                "teaches": ["b2-17-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El inspector nos preguntó __ habíamos visto a los sospechosos merodeando por el edificio. (si)",
                "answer": "si",
                "english": "The inspector asked us whether we had seen the suspects loitering around the building.",
                "teaches": ["discurso-indirecto-interrogativas"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la transformación correcta al estilo indirecto de la pregunta: '¿Dónde pusiste los planos?'?",
                "options": [
                    "Me preguntó dónde había puesto los planos.",
                    "Me preguntó si dónde puse los planos.",
                    "Me preguntó dónde pongo los planos.",
                    "Me preguntó que dónde pondré los planos."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-interrogativas"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "jueza", "quiso", "saber", "por", "qué", "no", "habían", "comparecido."],
                "solution": ["La", "jueza", "quiso", "saber", "por", "qué", "no", "habían", "comparecido."],
                "english": "The judge wanted to know why they had not appeared.",
                "teaches": ["discurso-indirecto-interrogativas"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Abogado", "text": "¿Qué le preguntó el fiscal al testigo durante el interrogatorio?"},
                    {"speaker": "Procuradora", "text": "_____"}
                ],
                "options": [
                    "Le preguntó cuándo había tenido conocimiento de las irregularidades contables de la empresa.",
                    "El tribunal se encuentra en la avenida principal de la ciudad.",
                    "El café del tribunal está cerrado durante las vacaciones de verano.",
                    "Los testigos visten ropa formal ante el jurado popular."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-interrogativas"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El periodista indagó cuántos recursos públicos se habían destinado a la construcción del hospital.",
                "english": "The journalist inquired how many public resources had been allocated to building the hospital.",
                "teaches": ["discurso-indirecto-interrogativas"]
            }
        ]
    })

    # --- Lesson 3: b2-17-03 ---
    l3 = f"{c_unit}-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.17.03",
        "lesson": l3,
        "title": "Mandatos, peticiones y prohibiciones en estilo indirecto",
        "theme": "Léxico de directrices, órdenes institucionales y requerimientos",
        "words": [
            {"lemma": "exigir", "translation": "to demand, to require strictly", "pos": "verb"},
            {"lemma": "suplicar", "translation": "to plead, to beg", "pos": "verb"},
            {"lemma": "prohibición", "translation": "prohibition, ban", "pos": "noun"},
            {"lemma": "mandato", "translation": "mandate, official command", "pos": "noun"},
            {"lemma": "requerimiento", "translation": "formal injunction, summons", "pos": "noun"},
            {"lemma": "instar", "translation": "to urge, to press strongly", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.17.03.discurso-indirecto-peticiones-subjuntivo",
        "title": "Órdenes, ruegos y peticiones referidas: del imperativo al imperfecto de subjuntivo",
        "sections": [
            {
                "type": "text",
                "content": "Cuando se reporta una orden directa, petición, consejo o prohibición formulada originalmente en modo imperativo o en presente de subjuntivo (*'¡Firme aquí!', 'Por favor, no salgan'*) y el verbo introductorio está en pasado (*ordenó, pidió, sugirió, prohibió, rogó*), la cláusula subordinada pasa obligatoriamente al **pretérito imperfecto de subjuntivo** (*-ra* o *-se*).\n\nEste mecanismo de traslación refleja la influencia sobre la conducta de un interlocutor proyectada en el pasado."
            },
            {
                "type": "table",
                "title": "Correspondencias de mandatos y peticiones",
                "rows": [
                    ["'¡Entreguen los pasaportes!' -> que + imperfecto subj.", "Nos ordenó que entregáramos los pasaportes."],
                    ["'No revele el secreto' -> que + imperfecto subj.", "Le suplicó que no revelara el secreto."],
                    ["'Vengan temprano' -> que + imperfecto subj.", "Les pidió que vinieran temprano."],
                    ["'Ten cuidado con el camino' -> que + imperfecto subj.", "Me aconsejó que tuviera cuidado."],
                    ["'No estacionen frente a la puerta' -> prohibió que", "Prohibió que estacionaran frente a la puerta."],
                    ["'Revisen los cálculos' -> instó a que", "Instó a que revisaran los cálculos minuciosamente."]
                ]
            },
            {
                "type": "tip",
                "content": "Verbos como *decir* cambian de significado según el modo de la subordinada:\n- Con indicativo transmite información: *Dijo que venía* (afirmación).\n- Con subjuntivo transmite una orden o mandato: *Dijo que viniera* (imperativo indirecto: *'¡Ven!'*)."
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
                    ["exigir", "to demand categorically"],
                    ["suplicar", "to plead earnestly"],
                    ["prohibición", "statutory ban"],
                    ["instar", "to urge prompt action"]
                ],
                "teaches": ["b2-17-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El oficial nos ordenó que no __ la zona acordonada bajo ninguna circunstancia. (cruzar)",
                "answer": "cruzáramos",
                "english": "The officer ordered us not to cross the cordoned-off area under any circumstance.",
                "teaches": ["discurso-indirecto-peticiones-subjuntivo"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se reporta en pasado la instrucción médica: 'Tome este medicamento cada ocho horas'?",
                "options": [
                    "El doctor me indicó que tomara ese medicamento cada ocho horas.",
                    "El doctor me indicó que tomo ese medicamento cada ocho horas.",
                    "El doctor me indicó que tomaré ese medicamento cada ocho horas.",
                    "El doctor me indicó que había tomado ese medicamento cada ocho horas."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-peticiones-subjuntivo"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Nos", "suplicaron", "que", "guardáramos", "absoluto", "silencio", "durante", "el", "rescate."],
                "solution": ["Nos", "suplicaron", "que", "guardáramos", "absoluto", "silencio", "durante", "el", "rescate."],
                "english": "They begged us to keep absolute silence during the rescue.",
                "teaches": ["discurso-indirecto-peticiones-subjuntivo"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diplomático", "text": "¿Qué resolvió el Consejo de Seguridad con respecto a las hostilidades en la frontera?"},
                    {"speaker": "Canciller", "text": "_____"}
                ],
                "options": [
                    "Emitió una resolución vinculante instando a que ambas partes cesaran el fuego de inmediato.",
                    "La sala de conferencias tiene capacidad para doscientas personas.",
                    "Los diplomáticos almuerzan en el restaurante del tercer piso.",
                    "El tratado de paz se firmó sobre papel pergamino en el siglo pasado."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-peticiones-subjuntivo"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La directora nos exigió que entregáramos las conclusiones periciales antes de que concluyera la semana.",
                "english": "The director demanded that we submit the expert findings before the week ended.",
                "teaches": ["discurso-indirecto-peticiones-subjuntivo"]
            }
        ]
    })

    # --- Lesson 4: b2-17-04 ---
    l4 = f"{c_unit}-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.17.04",
        "lesson": l4,
        "title": "Traslación de deícticos temporales y espaciales",
        "theme": "Léxico de coordenadas temporales, espaciales y contextuales",
        "words": [
            {"lemma": "deíctico", "translation": "deictic, context-dependent pointer", "pos": "adjective"},
            {"lemma": "coordenada", "translation": "coordinate, spatial/temporal frame", "pos": "noun"},
            {"lemma": "advenimiento", "translation": "arrival, advent of an event", "pos": "noun"},
            {"lemma": "proximidad", "translation": "proximity, closeness", "pos": "noun"},
            {"lemma": "distanciamiento", "translation": "distancing, temporal displacement", "pos": "noun"},
            {"lemma": "enunciación", "translation": "enunciation, act of speaking", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.17.04.discurso-indirecto-deicticos",
        "title": "Traslación de deícticos temporales, espaciales y demostrativos en el relato",
        "sections": [
            {
                "type": "text",
                "content": "Además de los verbos, el estilo indirecto en pasado exige adaptar todos los **elementos deícticos** (adverbios de tiempo y lugar, demostrativos y posesivos) cuyo significado dependía originalmente del momento y lugar de la enunciación primaria.\n\nCuando el relator habla desde un tiempo y espacio distintos al del hablante original, estos marcadores se desplazan sistemáticamente desde la proximidad hacia la lejanía."
            },
            {
                "type": "table",
                "title": "Tabla de equivalencias deícticas en pasado",
                "rows": [
                    ["hoy / esta tarde", "aquel día / ese día / esa tarde"],
                    ["ayer / anoche", "el día anterior / la víspera / la noche anterior"],
                    ["mañana / el año que viene", "al día siguiente / el año siguiente"],
                    ["aquí / acá", "allí / allá / en ese lugar"],
                    ["este / esta / esto", "aquel / aquella / aquello / ese / esa"],
                    ["hace tres días / ahora", "hacía tres días / entonces / en aquel momento"]
                ]
            },
            {
                "type": "tip",
                "content": "La adaptación no es automática si el marco temporal sigue vigente: si alguien dijo esta mañana *'Vendré hoy'* y tú lo cuentas esa misma tarde, dirás: *'Dijo que vendría hoy'*, conservando el deíctico porque el día aún no ha concluido."
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
                    ["deíctico", "context-pointing word"],
                    ["coordenada", "spatial or temporal anchor"],
                    ["distanciamiento", "perspective displacement"],
                    ["enunciación", "act of uttering speech"]
                ],
                "teaches": ["b2-17-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El ministro anunció que la comitiva partiría al día __ hacia la conferencia internacional. (siguiente)",
                "answer": "siguiente",
                "english": "The minister announced that the delegation would depart the following day for the international conference.",
                "teaches": ["discurso-indirecto-deicticos"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se adapta en estilo indirecto pasado la frase: 'Estaremos aquí mañana por la tarde'?",
                "options": [
                    "Aseguraron que estarían allí al día siguiente por la tarde.",
                    "Aseguraron que están aquí mañana por la tarde.",
                    "Aseguraron que hubieran estado aquí ayer tarde.",
                    "Aseguraron que estarán allí hoy por la tarde."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-deicticos"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Nos", "explicó", "que", "aquel", "documento", "había", "sido", "redactado", "entonces."],
                "solution": ["Nos", "explicó", "que", "aquel", "documento", "había", "sido", "redactado", "entonces."],
                "english": "He explained to us that that document had been drafted back then.",
                "teaches": ["discurso-indirecto-deicticos"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Corresponsal", "text": "¿Cómo reportó el enviado especial el mensaje que los líderes grabaron hace tres días diciendo 'Firmaremos el pacto aquí mañana'?"},
                    {"speaker": "Editora", "text": "_____"}
                ],
                "options": [
                    "Informó que los mandatarios habían asegurado que firmarían el pacto allí al día siguiente.",
                    "Informó que los mandatarios firmarán el pacto aquí mañana sin falta.",
                    "El canal de televisión emite programas de entretenimiento los fines de semana.",
                    "Los periódicos se imprimen en prensas rotativas de alta velocidad."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-deicticos"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La testigo declaró que había visto al sospechoso en aquel mismo portal la noche anterior al incidente.",
                "english": "The witness declared that she had seen the suspect in that very doorway the night before the incident.",
                "teaches": ["discurso-indirecto-deicticos"]
            }
        ]
    })

    # --- Lesson 5: b2-17-05 ---
    l5 = f"{c_unit}-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.17.05",
        "lesson": l5,
        "title": "Discurso indirecto libre y polifonía narrativa",
        "theme": "Léxico de técnica literaria, focalización y conciencia narrativa",
        "words": [
            {"lemma": "polifonía", "translation": "polyphony, coexistence of voices", "pos": "noun"},
            {"lemma": "monólogo", "translation": "monologue, interior reflection", "pos": "noun"},
            {"lemma": "focalización", "translation": "narrative focalization, viewpoint", "pos": "noun"},
            {"lemma": "conciencia", "translation": "consciousness, internal mind", "pos": "noun"},
            {"lemma": "fluctuar", "translation": "to fluctuate, to oscillate", "pos": "verb"},
            {"lemma": "verosimilitud", "translation": "verisimilitude, realism", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.17.05.discurso-indirecto-libre",
        "title": "El discurso indirecto libre en la prosa narrativa hispanoamericana",
        "sections": [
            {
                "type": "text",
                "content": "El **discurso indirecto libre** es un refinado recurso estilístico característico de la gran narrativa hispanoamericana moderna (desde Juan Rulfo y Gabriel García Márquez hasta Jorge Icaza). En él, los pensamientos, dudas y emociones de un personaje se funden directamente con la voz del narrador **sin verbo introductorio** (*dijo, pensó*) y **sin conjunción subordinante** (*que*).\n\nSintácticamente conserva la tercera persona y los tiempos del pasado del narrador (imperfecto, pluscuamperfecto, condicional), pero adopta el tono afectivo, las exclamaciones, las dudas y los deícticos subjetivos del personaje."
            },
            {
                "type": "table",
                "title": "Comparativa de estilos narrativos",
                "rows": [
                    ["Estilo Directo", "Andrés pensó: '¿Adónde iremos ahora? No tengo tierras.'"],
                    ["Estilo Indirecto Canónico", "Andrés pensó que adónde irían entonces, pues no tenía tierras."],
                    ["Discurso Indirecto Libre", "¿Adónde irían ahora? Ya no le quedaban tierras ni maíz."],
                    ["Efecto Estético", "Fundición íntima entre la voz del narrador y la angustia del protagonista."],
                    ["Tiempos Verbales", "Uso predominante del imperfecto y condicional con valor subjetivo."],
                    ["Marcadores Emotivos", "Exclamaciones e interrogaciones sin comillas ni guiones de diálogo."]
                ]
            },
            {
                "type": "tip",
                "content": "Para reconocer el discurso indirecto libre en un texto literario B2, busca oraciones interrogativas o exclamativas en tercera persona del pasado que expresen la perplejidad íntima de un personaje sin que aparezca la fórmula explícita *'él se preguntaba'*. Es la marca suprema de la introspección narrativa moderna."
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
                    ["polifonía", "multiple narrative voices"],
                    ["focalización", "character perspective lens"],
                    ["conciencia", "internal stream of thought"],
                    ["verosimilitud", "artistic realism"]
                ],
                "teaches": ["b2-17-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la novela indigenista, el campesino miraba la colina desierta: ¿adónde __ sus hijos tras el desalojo forzoso? (ir)",
                "answer": "irían",
                "english": "In the indigenist novel, the peasant looked at the deserted hill: where would his children go after the forced eviction?",
                "teaches": ["discurso-indirecto-libre"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo sintáctico define de manera concluyente al discurso indirecto libre?",
                "options": [
                    "La ausencia de verbo de comunicación introductorio (decir, pensar) y de nexo subordinante (que).",
                    "El uso obligatorio de comillas dobles y guiones largos de conversación.",
                    "La presencia constante de verbos en tiempo futuro de indicativo.",
                    "La narración obligatoria en segunda persona del singular."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-libre"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["¿Qué", "haría", "él", "ahora", "sin", "su", "familia", "ni", "su", "choza?"],
                "solution": ["¿Qué", "haría", "él", "ahora", "sin", "su", "familia", "ni", "su", "choza?"],
                "english": "What would he do now without his family or his hut?",
                "teaches": ["discurso-indirecto-libre"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítica literaria", "text": "¿Por qué Jorge Icaza recurre al discurso indirecto libre en pasajes cruciales de Huasipungo?"},
                    {"speaker": "Profesor", "text": "_____"}
                ],
                "options": [
                    "Para sumergir al lector directamente en la angustia existencial del comunero sin la distancia fría de un relator externo.",
                    "Porque en los años treinta la gramática española no permitía el uso de comillas.",
                    "Para abaratar los costos de imprenta suprimiendo los signos de puntuación.",
                    "Porque los personajes de la novela hablaban exclusivamente en idiomas europeos."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-libre"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "¿Cómo resistir el embate de los fusiles si el hambre consumía sus últimas fuerzas desde hacía semanas?",
                "english": "How could they resist the onslaught of rifles if hunger had been draining their last strength for weeks?",
                "teaches": ["discurso-indirecto-libre"]
            }
        ]
    })

    # --- Lesson 6: b2-17-consolidation ---
    l6_con = f"{c_unit}-consolidation"
    write_json(f"exercises/b2/{l6_con}-ex.json", {
        "lesson": l6_con,
        "exercises": [
            {
                "id": f"{l6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["traslación", "systematic tense shift"],
                    ["indagación", "profound questioning"],
                    ["mandato", "binding directive"],
                    ["deíctico", "contextual pointer"]
                ],
                "teaches": ["b2-17-vocab"]
            },
            {
                "id": f"{l6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El hacendado ordenó tajantemente que todos los huasipungueros se __ de sus parcelas ancestrales. (retirar)",
                "answer": "retiraran",
                "english": "The landowner strictly ordered all the huasipungueros to withdraw from their ancestral parcels.",
                "teaches": ["discurso-indirecto-peticiones-subjuntivo"]
            },
            {
                "id": f"{l6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se reporta en pasado la pregunta directa: '¿Cuándo terminará la construcción de la carretera'?",
                "options": [
                    "Preguntaron cuándo terminaría la construcción de la carretera.",
                    "Preguntaron si cuándo termina la construcción de la carretera.",
                    "Preguntaron cuándo terminó la construcción de la carretera.",
                    "Preguntaron que cuándo terminará la construcción de la carretera."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-interrogativas"]
            },
            {
                "id": f"{l6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El cronista aseguró que la asamblea comunitaria se había celebrado el día __ en la plaza mayor. (anterior)",
                "answer": "anterior",
                "english": "The chronicler stated that the community assembly had been held the previous day in the main plaza.",
                "teaches": ["discurso-indirecto-deicticos"]
            },
            {
                "id": f"{l6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué distingue al estilo indirecto libre frente al estilo indirecto convencional?",
                "options": [
                    "Fusiona la voz del relator con la conciencia del personaje eliminando el verbo introductorio y el nexo que.",
                    "Exige siempre el uso de comillas inglesas al inicio y final de cada párrafo.",
                    "Obliga al narrador a traducir todos los términos al latín eclesiástico.",
                    "Se utiliza exclusivamente en cartas comerciales y contratos jurídicos."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-libre"]
            },
            {
                "id": f"{l6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "comuneros", "clamaban", "que", "aquella", "tierra", "pertenecía", "a", "sus", "hijos."],
                "solution": ["Los", "comuneros", "clamaban", "que", "aquella", "tierra", "pertenecía", "a", "sus", "hijos."],
                "english": "The villagers cried out that that land belonged to their children.",
                "teaches": ["discurso-indirecto-tiempos-pasados"]
            },
            {
                "id": f"{l6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "El prefecto exigió que los líderes comunitarios presentaran los títulos de propiedad ante el juzgado cantonal.",
                "english": "The prefect demanded that community leaders present the property titles before the cantonal court.",
                "teaches": ["discurso-indirecto-peticiones-subjuntivo"]
            },
            {
                "id": f"{l6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué trascendencia histórica ostenta la novela Huasipungo de Jorge Icaza en la literatura latinoamericana?",
                "options": [
                    "Consagró el realismo social indigenista denunciando la explotación feudal del campesinado andino.",
                    "Fue una comedia satírica sobre la moda aristocrática en las cortes de Europa.",
                    "Constituyó el primer manual de agronomía para el cultivo de trigo en tierras templadas.",
                    "Narró expediciones espaciales en una clave de ciencia ficción vanguardista."
                ],
                "correct": 0,
                "teaches": ["discurso-indirecto-libre"]
            }
        ]
    })

    # Classic Story for Core Unit 17: Jorge Icaza - Huasipungo (~700 words, strictly 650-825 words)
    story_core_17 = {
        "id": "b2-17",
        "title": "Huasipungo: El grito de la tierra y la resistencia comunitaria",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de nivel B2 de la cumbre indigenista de Jorge Icaza: la vida de Andrés Chiliquinga en los páramos de Cangahua, el despojo de los huasipungos por el hacendado don Alfonso Pereira y una compañía maderera extranjera, la muerte de su compañera Cunshi y el levantamiento campesino final defendiendo sus parcelas ancestrales bajo el lema inextinguible de la resistencia andina.",
        "characters": [
            "Andrés Chiliquinga",
            "Cunshi",
            "Don Alfonso Pereira",
            "Míster Chapy",
            "El Cura Pedro"
        ],
        "narration": {
            "paragraphs": [
                "En las faldas escarpadas de la cordillera ecuatoriana, donde el viento helado del páramo azota los pajonales sin tregua, se extendían los huasipungos de la hacienda Cuchitambo. Para Andrés Chiliquinga y su compañera Cunshi, el huasipungo no era una simple concesión graciosa de la hacienda: era un pedazo minúsculo de tierra pedregosa que sus antepasados habían regado con sudor inmemorial. Allí levantaban su choza de barro y paja, sembraban unas cuantas hileras de papas y maíz, y a cambio de aquel rincón de supervivencia entregaban semanas enteras de faena gratuita abriendo zanjas, deshierbando laderas y apacentando el ganado del patrón. Desde el alba hasta el anochecer, las campanas de la hacienda marcaban el ritmo implacable de una servidumbre hereditaria que encadenaba a las familias a la tierra ajena, sin recibir jamás salario monetario ni derechos legales.",
                "El frágil equilibrio de aquella servidumbre feudal se fracturó cuando don Alfonso Pereira, acosado por pesadas deudas bancarias en la capital, pactó un lucrativo acuerdo con míster Chapy, el representante de una poderosa corporación maderera y petrolera extranjera. Los empresarios requerían construir de urgencia una amplia carretera carreteable que comunicara las serranías con los yacimientos de la selva virgen. Para abrir paso a los camiones y aserraderos mecánicos, era indispensable drenar las ciénagas pantanosas y desalojar sin miramientos las humildes chozas que estorbaban el trazado de la obra.",
                "El hacendado y el párroco local convocaron a los comuneros para ordenarles que entregaran todo su esfuerzo en las faenas camineras. Aseguraban que la carretera traería el progreso cristiano a toda la comarca y que Dios castigaría severamente a quienes eludieran el trabajo comunal. Andrés y sus compañeros obedecieron cabizbajos, pero las jornadas resultaron mortales. Hundidos hasta la cintura en el lodo podrido de los pantanos, bajo lluvias torrenciales que no cesaban jamás, decenas de indígenas enfermaron de fiebres malignas o quedaron sepultados por los repentinos desprendimientos de tierra de las quebradas.",
                "Cuando la carretera estuvo casi terminada a costa de innumerables vidas humanas, llegó la orden definitiva que nadie quería creer: el hacendado anunció que los huasipungos debían ser desmantelados y que las familias debían retirarse hacia las cumbres estériles del páramo alto, donde ni el ganado lograba alimentarse. Andrés Chiliquinga sintió que el suelo se abría bajo sus pies. ¿Adónde irían ahora con los niños famélicos? Las laderas más altas estaban azotadas por heladas implacables que congelaban las raíces antes de brotar. Poco después, una peste implacable se propagó por las chozas y Cunshi enfermó gravemente de gangrena estomacal tras comer carne podrida de una res desechada por la hacienda.",
                "La agonía de Cunshi sumió a Andrés en la desesperación más desgarradora. Para pagar el entierro en el camposanto católico y evitar que el alma de su compañera vagara en las sombras, el cura le exigió una suma exorbitante de dinero que Andrés no poseía. Desesperado, el comunero robó una vaca de la manada patronal para venderla en el pueblo vecino, pero fue capturado por los mayordomos y azotado con saña ejemplarizante en el patio central de la hacienda hasta perder el conocimiento. Atado al poste de castigo, Andrés soportó los latigazos en silencio mientras el patrón advertía a los demás comuneros que ese sería el destino implacable de cualquiera que osara desafiar la autoridad señorial.",
                "Apenas recobró el aliento y enterró a Cunshi en la soledad de la ladera, Andrés comprendió que la resignación ya no tenía sentido alguno. Cuando los peones de la compañía y los soldados arribaron armados para incendiar los techos de paja y expulsar a los campesinos con bayonetas caladas, Andrés levantó su machete oxidado y convocó a toda la comunidad con el bramido sordo del churo ancestral. Hombres, ancianos y mujeres con sus hijos en brazos se parapetaron en la choza comunal más alta, negándose a claudicar ante el avance de las tropas armadas.",
                "El estampido de los fusiles no tardó en rasgar el aire gélido de la sierra andina. Aunque el fuego devoraba las vigas de madera y las balas atravesaban el adobe sin piedad, el clamor de los rebeldes se elevó como una sola voz poderosa por encima de las montañas: «¡Ñucanchik huasipungo! ¡La tierra es nuestra!». En esa resistencia trágica e indomeñable, Jorge Icaza plasmó para siempre el dolor visceral de los pueblos originarios y la dignidad inquebrantable de una cultura que jamás aceptó el despojo como destino inevitable."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué don Alfonso Pereira decidió desalojar los huasipungos de los comuneros indígenas?",
                        "options": [
                            "Para abrir paso a una carretera exigida por una corporación maderera y petrolera extranjera.",
                            "Para construir un balneario turístico de aguas termales en la montaña.",
                            "Porque los huasipungueros se negaban a cultivar maíz para el mercado local.",
                            "Para vender las tierras a una orden religiosa procedente de la capital."
                        ],
                        "correctIndex": 0,
                        "explanation": "El hacendado pactó con inversionistas extranjeros la construcción de una carretera hacia la selva maderera, lo que requería desalojar y destruir las chozas campesinas."
                    },
                    {
                        "question": "¿Qué situación desesperada empujó a Andrés Chiliquinga a robar una res de la hacienda?",
                        "options": [
                            "La necesidad apremiante de pagar los derechos eclesiásticos para sepultar a su compañera Cunshi.",
                            "El deseo de fundar su propia carnicería en el mercado del pueblo cantonal.",
                            "Una apuesta económica que había perdido con los mayordomos del establo.",
                            "La orden secreta que le habían dado los delegados de la compañía extranjera."
                        ],
                        "correctIndex": 0,
                        "explanation": "El cura le exigió una elevada suma de dinero para permitir el entierro de Cunshi en el camposanto, lo que llevó a Andrés a cometer el robo para conseguir los fondos."
                    },
                    {
                        "question": "¿Cuál fue la respuesta final de la comunidad campesina ante la llegada de las tropas armadas para desalojarlos?",
                        "options": [
                            "Se atrincheraron en las chozas altas y resistieron al grito ancestral de '¡Ñucanchik huasipungo!'.",
                            "Abandonaron pacíficamente la sierra para trasladarse a trabajar en los puertos marítimos.",
                            "Aceptaron una compensación económica y firmaron un acuerdo voluntario de traslado.",
                            "Se dispersaron en secreto por la noche sin presentar ninguna oposición organizada."
                        ],
                        "correctIndex": 0,
                        "explanation": "Liderados por Andrés tras el llamado del churo, los comuneros se atrincheraron en la choza alta y defendieron sus tierras ancestrales frente a las tropas."
                    }
                ]
            }
        }
    }

    # -------------------------------------------------------------------------
    # 3. REGIONAL UNIT 17: b2-ecuador (Ecuador: Plurinationalism & The Galápagos)
    # -------------------------------------------------------------------------
    r_unit = "b2-ecuador"

    # --- Lesson 1: b2-ecuador-01 ---
    r1 = f"{r_unit}-01"
    write_json(f"vocabulary/b2/{r1}-voc.json", {
        "id": "vocab.b2.ecuador.01",
        "lesson": r1,
        "title": "La avenida de los volcanes y el callejón interandino",
        "theme": "Léxico de geomorfología volcánica, valles andinos y ciudades patrimoniales",
        "words": [
            {"lemma": "nevado", "translation": "snow-capped peak", "pos": "noun"},
            {"lemma": "callejón", "translation": "inter-Andean valley corridor", "pos": "noun"},
            {"lemma": "glaciar", "translation": "glacier, high-altitude ice mass", "pos": "noun"},
            {"lemma": "patrimonial", "translation": "heritage, historical monument", "pos": "adjective"},
            {"lemma": "estratovolcán", "translation": "stratovolcano", "pos": "noun"},
            {"lemma": "barroco", "translation": "Baroque colonial architecture", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r1}-a-gr.json", {
        "id": "grammar.b2.ecuador.01.ecuador-volcanes-callejon-interandino",
        "title": "La avenida de los volcanes y el callejón interandino del Ecuador",
        "sections": [
            {
                "type": "text",
                "content": "Flanqueado por dos cadenas montañosas paralelas de la cordillera de los Andes —la cordillera Occidental y la cordillera Real u Oriental—, el **callejón interandino** ecuatoriano constituye una depresión geográfica única en el continente. Bautizada en 1802 por el sabio naturalista prusiano Alexander von Humboldt como la *'Avenida de los Volcanes'*, esta franja de más de cuatrocientos kilómetros alberga más de ochenta volcanes, veintisiete de los cuales continúan activos o potencialmente activos.\n\nEn este sobrecogedor escenario sobresalen colosos como el **Chimborazo** (cuyo pico nevado de 6.263 metros sobre el nivel del mar es el punto más cercano al sol y más alejado del centro de la Tierra debido al abultamiento ecuatorial del planeta) y el majestuoso **Cotopaxi** (uno de los estratovolcanes activos más altos y perfectamente cónicos del globo). Entre estos gigantes se asientan valles fértiles de clima templado perpetuo donde florecieron ciudades declaradas Patrimonio Cultural de la Humanidad por la UNESCO: **Quito**, la primera capital del mundo en recibir dicho título en 1978 por su centro histórico colonial barroco intacto, y **Cuenca**, joya arquitectónica atravesada por cuatro ríos cristalinos."
            },
            {
                "type": "table",
                "title": "Hitos orográficos y patrimoniales del callejón interandino",
                "rows": [
                    ["el Chimborazo", "highest point from Earth's center at 6,263 meters above sea level"],
                    ["el Cotopaxi", "active stratovolcano with a perfect snow-covered crater cone"],
                    ["el Tungurahua", "active volcanic peak known as the 'Throat of Fire' in Baños"],
                    ["el centro histórico de Quito", "largest and best-preserved colonial Baroque ensemble in the Americas"],
                    ["Cuenca (Santa Ana de los Cuatro Ríos)", "UNESCO gem famed for colonial cobblestones and Panama hats"],
                    ["el páramo andino", "sponge-like alpine moorland supplying fresh water to the valleys"]
                ]
            },
            {
                "type": "tip",
                "content": "Debido a la fuerza centrífuga de la rotación terrestre en la latitud cero grados, la cumbre del volcán Chimborazo supera la cima del monte Everest por más de dos mil metros si la altura se mide tomando como referencia el centro geodésico de la Tierra, convirtiéndolo en el auténtico 'techo del planeta'."
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
                    ["nevado", "snow-covered summit"],
                    ["callejón", "corridor between ranges"],
                    ["glaciar", "permanent ice mass"],
                    ["estratovolcán", "layered conical volcano"]
                ],
                "teaches": ["b2-ecuador-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El sabio Alexander von Humboldt bautizó al corredor volcánico de la sierra como la __ de los volcanes. (avenida)",
                "answer": "avenida",
                "english": "The scholar Alexander von Humboldt named the volcanic corridor of the highlands the avenue of volcanoes.",
                "teaches": ["ecuador-volcanes-callejon-interandino"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el volcán Chimborazo es considerado el punto más cercano al sol en el planeta Tierra?",
                "options": [
                    "Debido al abultamiento ecuatorial terrestre, que eleva su cumbre más lejos del centro del planeta que el monte Everest.",
                    "Porque es la montaña con mayor altitud absoluta sobre el nivel medio del mar.",
                    "Porque la atmósfera es más delgada en la línea equinoccial que en los polos.",
                    "Debido a que su cráter permanece en constante erupción solar."
                ],
                "correct": 0,
                "teaches": ["ecuador-volcanes-callejon-interandino"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Quito", "fue", "declarada", "Patrimonio", "de", "la", "Humanidad", "en", "1978."],
                "solution": ["Quito", "fue", "declarada", "Patrimonio", "de", "la", "Humanidad", "en", "1978."],
                "english": "Quito was declared a World Heritage Site in 1978.",
                "teaches": ["ecuador-volcanes-callejon-interandino"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Geógrafa", "text": "¿Qué función hidrológica cumplen los páramos que rodean a los volcanes ecuatorianos?"},
                    {"speaker": "Guardaparque", "text": "_____"}
                ],
                "options": [
                    "Actúan como gigantescas esponjas vegetales que absorben la humedad de las nieblas y regulan el caudal de agua potable para las ciudades.",
                    "Impiden que los aviones aterricen en las pistas de los aeropuertos internacionales.",
                    "Generan corrientes de aire cálido que derriten los glaciares en invierno.",
                    "Son yacimientos de sal marina explotados por cooperativas mineras."
                ],
                "correct": 0,
                "teaches": ["ecuador-volcanes-callejon-interandino"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Desde las torres barrocas del centro de Quito se divisa la silueta imponente del volcán Pichincha en el horizonte.",
                "english": "From the Baroque towers of downtown Quito, the imposing silhouette of the Pichincha volcano is visible on the horizon.",
                "teaches": ["ecuador-volcanes-callejon-interandino"]
            }
        ]
    })

    # --- Lesson 2: b2-ecuador-02 ---
    r2 = f"{r_unit}-02"
    write_json(f"vocabulary/b2/{r2}-voc.json", {
        "id": "vocab.b2.ecuador.02",
        "lesson": r2,
        "title": "Las islas Galápagos y la evolución biológica",
        "theme": "Léxico de biología evolutiva, biogeografía insular y conservación oceánica",
        "words": [
            {"lemma": "endemismo", "translation": "endemism, native ecological uniqueness", "pos": "noun"},
            {"lemma": "especiación", "translation": "speciation, evolutionary emergence", "pos": "noun"},
            {"lemma": "arrecife", "translation": "marine reef, coral formation", "pos": "noun"},
            {"lemma": "corriente", "translation": "oceanic current", "pos": "noun"},
            {"lemma": "insular", "translation": "insular, pertaining to islands", "pos": "adjective"},
            {"lemma": "santuario", "translation": "wildlife sanctuary, reserve", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r2}-a-gr.json", {
        "id": "grammar.b2.ecuador.02.ecuador-galapagos-evolucion-darwin",
        "title": "El archipiélago de Galápagos: Laboratorio vivo de la evolución",
        "sections": [
            {
                "type": "text",
                "content": "Situadas a casi mil kilómetros al oeste de la costa continental ecuatoriana, las **Islas Galápagos** (oficialmente llamadas Archipiélago de Colón) constituyen uno de los ecosistemas oceánicos más singulares del planeta. Emergidas como producto de una intensa actividad volcánica submarina sobre un punto caliente geológico (*hotspot*), las islas jamás estuvieron conectadas con el continente, lo que obligó a las pocas especies pioneras que llegaron flotando en balsas de vegetación o arrastradas por las corrientes a adaptarse a condiciones extremas de aislamiento.\n\nLa confluencia única de tres corrientes marinas mayores —la fría **corriente de Humboldt**, la cálida de Panamá y la profunda **corriente de Cromwell** cargada de nutrientes— genera una prodigiosa abundancia marina que sostiene a animales insólitos: las únicas **iguanas marinas** del mundo que bucean para alimentarse de algas submarinas, **tortugas gigantes terrestres** (*Chelonoidis*) que pueden vivir casi dos siglos, y pingüinos que habitan en la línea equinoccial. La observación meticulosa de los pinzones y cormoranes de Galápagos en 1835 brindó al joven naturalista británico **Charles Darwin** las piezas clave para formular su revolucionaria teoría de la evolución por selección natural en *El origen de las especies*."
            },
            {
                "type": "table",
                "title": "Fauna emblemática y corrientes de Galápagos",
                "rows": [
                    ["la iguana marina", "the only sea-diving lizard on Earth feeding on marine algae"],
                    ["la tortuga gigante", "endemic giant tortoises showing distinct shell shapes by island"],
                    ["los pinzones de Darwin", "thirteen species showing adaptive beak morphology by food source"],
                    ["el cormorán no volador", "marine diving bird that lost flight capability due to lack of land predators"],
                    ["el tiburón martillo", "schooling in thousands around Darwin and Wolf marine sanctuaries"],
                    ["la Reserva Marina de Galápagos", "one of Earth's largest and most protected oceanic reserves"]
                ]
            },
            {
                "type": "tip",
                "content": "En 2022, Ecuador creó la histórica reserva marina *Hermandad*, añadiendo 60.000 kilómetros cuadrados de protección estricta para conectar el corredor biológico migratorio que une Galápagos con la Isla del Coco en Costa Rica y Malpelo en Colombia."
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
                    ["endemismo", "species restricted to a region"],
                    ["especiación", "evolution of distinct species"],
                    ["arrecife", "underwater coral structure"],
                    ["santuario", "strictly protected haven"]
                ],
                "teaches": ["b2-ecuador-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las islas Galápagos sirvieron de laboratorio natural a Charles Darwin para formular la teoría de la __ natural. (selección)",
                "answer": "selección",
                "english": "The Galápagos Islands served as a natural laboratory for Charles Darwin to formulate the theory of natural selection.",
                "teaches": ["ecuador-galapagos-evolucion-darwin"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué las iguanas marinas de Galápagos son una especie biológicamente extraordinaria?",
                "options": [
                    "Porque son los únicos lagartos del planeta que bucean en el mar para alimentarse de algas submarinas.",
                    "Porque pueden volar de una isla a otra durante la época de apareamiento.",
                    "Porque cambian de color como los camaleones para ocultarse en la arena blanca.",
                    "Porque hibernan bajo el hielo polar durante seis meses al año."
                ],
                "correct": 0,
                "teaches": ["ecuador-galapagos-evolucion-darwin"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "corriente", "de", "Cromwell", "aporta", "nutrientes", "vitales", "al", "archipiélago."],
                "solution": ["La", "corriente", "de", "Cromwell", "aporta", "nutrientes", "vitales", "al", "archipiélago."],
                "english": "The Cromwell current brings vital nutrients to the archipelago.",
                "teaches": ["ecuador-galapagos-evolucion-darwin"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Biólogo marino", "text": "¿Qué motivó a Charles Darwin a advertir que las especies no eran inmutables al visitar las islas?"},
                    {"speaker": "Historiadora", "text": "_____"}
                ],
                "options": [
                    "Observó que la morfología de los picos de los pinzones y los caparazones de las tortugas variaban sistemáticamente según la isla y su dieta.",
                    "Descubrió fósiles de dinosaurios carnívoros en las cumbres de los volcanes submarinos.",
                    "Encontró mapas antiguos dibujados por piratas españoles en las playas desiertas.",
                    "Habló con los pescadores locales que criaban especies de laboratorio."
                ],
                "correct": 0,
                "teaches": ["ecuador-galapagos-evolucion-darwin"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La Reserva Marina de Galápagos protege un santuario oceánico vital para la migración de tiburones martillo y ballenas.",
                "english": "The Galápagos Marine Reserve protects a vital oceanic sanctuary for the migration of hammerhead sharks and whales.",
                "teaches": ["ecuador-galapagos-evolucion-darwin"]
            }
        ]
    })

    # --- Lesson 3: b2-ecuador-03 ---
    r3 = f"{r_unit}-03"
    write_json(f"vocabulary/b2/{r3}-voc.json", {
        "id": "vocab.b2.ecuador.03",
        "lesson": r3,
        "title": "La CONAIE y el movimiento indígena ecuatoriano",
        "theme": "Léxico de movilización social, plurinacionalidad y autonomía originaria",
        "words": [
            {"lemma": "levantamiento", "translation": "popular uprising, collective strike", "pos": "noun"},
            {"lemma": "plurinacional", "translation": "plurinational, multi-nation state", "pos": "adjective"},
            {"lemma": "nacionalidad", "translation": "indigenous nationality, distinct people", "pos": "noun"},
            {"lemma": "comunero", "translation": "member of an indigenous community", "pos": "noun"},
            {"lemma": "reivindicar", "translation": "to demand, to reclaim ancestral rights", "pos": "verb"},
            {"lemma": "consenso", "translation": "consensus, collective decision", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r3}-a-gr.json", {
        "id": "grammar.b2.ecuador.03.ecuador-conaie-movimiento-indigena",
        "title": "La CONAIE y la fuerza histórica del movimiento indígena",
        "sections": [
            {
                "type": "text",
                "content": "Fundada en 1986, la **Confederación de Nacionalidades Indígenas del Ecuador (CONAIE)** se ha consolidado como una de las organizaciones sociales y políticas más influyentes, articuladas y respetadas de toda América Latina. Agrupando a las catorce nacionalidades y dieciocho pueblos originarios del país (desde los pueblos Kichwa de la Sierra y de la Amazonía hasta los Shuar, Achuar, Waorani y Chachi de las tierras bajas), la CONAIE trascendió la vieja lucha puramente agraria para situar en el centro del debate nacional la exigencia de un **Estado Plurinacional e Intercultural**.\n\nEl punto de inflexión histórico ocurrió en junio de 1990 con el recordado **Primer Gran Levantamiento Indígena del Inti Raymi**: cientos de miles de campesinos bloquearon pacíficamente las carreteras del país y marcharon hacia Quito exigiendo títulos de propiedad colectiva de la tierra, reconocimiento de la educación intercultural bilingüe y solución a conflictos de linderos. Con su brazo político electoral, el movimiento **Pachakutik**, el movimiento indígena alteró para siempre la correlación de fuerzas de la política republicana ecuatoriana."
            },
            {
                "type": "table",
                "title": "Pilares de la organización indígena en Ecuador",
                "rows": [
                    ["la CONAIE", "Confederation of Indigenous Nationalities of Ecuador uniting Sierra, Coast, and Amazon"],
                    ["el levantamiento de 1990", "historic nationwide general mobilization transforming indigenous political visibility"],
                    ["Pachakutik", "plurinational political party representing indigenous and social movements in parliament"],
                    ["la plurinacionalidad", "constitutional principle recognizing multiple distinct indigenous nations within one republic"],
                    ["la justicia comunitaria", "ancestral customary legal system recognized with constitutional parity"],
                    ["la educación bilingüe", "intercultural bilingual school curriculum taught in Kichwa, Shuar, and Spanish"]
                ]
            },
            {
                "type": "tip",
                "content": "El término quechua *Pachakutik* simboliza el renacimiento cíclico del tiempo y del espacio: la idea de que la historia no avanza en línea recta, sino que atraviesa momentos de profunda transformación cósmica donde los saberes de abajo vuelven a guiar a la sociedad."
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
                    ["levantamiento", "widespread popular mobilization"],
                    ["plurinacional", "multi-nation civic model"],
                    ["nacionalidad", "distinct indigenous ethnolinguistic group"],
                    ["reivindicar", "to assert legitimate rights"]
                ],
                "teaches": ["b2-ecuador-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En junio de 1990, el levantamiento de la CONAIE paralizó las carreteras exigiendo la titulación de tierras __. (comunitarias)",
                "answer": "comunitarias",
                "english": "In June 1990, the CONAIE uprising paralyzed highways demanding collective community land titles.",
                "teaches": ["ecuador-conaie-movimiento-indigena"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál fue el logro conceptual más trascendente que impulsó la CONAIE en la política ecuatoriana?",
                "options": [
                    "Redefinir la república como un Estado Plurinacional que reconoce formalmente a las diversas nacionalidades ancestrales.",
                    "Exigir la clausura de todas las universidades públicas de las ciudades serranas.",
                    "Prohibir que los ciudadanos aprendan lenguas extranjeras en los colegios.",
                    "Fomentar la importación masiva de semillas transgénicas de maíz."
                ],
                "correct": 0,
                "teaches": ["ecuador-conaie-movimiento-indigena"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "CONAIE", "agrupa", "a", "catorce", "nacionalidades", "originarias", "del", "Ecuador."],
                "solution": ["La", "CONAIE", "agrupa", "a", "catorce", "nacionalidades", "originarias", "del", "Ecuador."],
                "english": "CONAIE groups fourteen native nationalities of Ecuador.",
                "teaches": ["ecuador-conaie-movimiento-indigena"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Por qué el movimiento Pachakutik representó una novedad radical en los comicios de Ecuador?"},
                    {"speaker": "Politóloga", "text": "_____"}
                ],
                "options": [
                    "Porque permitió que los pueblos originarios accedieran a escaños legislativos con una agenda propia sin depender de los partidos tradicionales.",
                    "Porque sus candidatos prometieron privatizar todos los bosques amazónicos de la nación.",
                    "Porque el partido prohibía que las mujeres participaran en los debates electorales.",
                    "Porque fue fundado por inversionistas extranjeros procedentes de Europa del norte."
                ],
                "correct": 0,
                "teaches": ["ecuador-conaie-movimiento-indigena"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las comunidades andinas toman decisiones mediante asambleas abiertas fundamentadas en la deliberación y el consenso.",
                "english": "Andean communities make decisions through open assemblies grounded in deliberation and consensus.",
                "teaches": ["ecuador-conaie-movimiento-indigena"]
            }
        ]
    })

    # --- Lesson 4: b2-ecuador-04 ---
    r4 = f"{r_unit}-04"
    write_json(f"vocabulary/b2/{r4}-voc.json", {
        "id": "vocab.b2.ecuador.04",
        "lesson": r4,
        "title": "La Constitución de Montecristi y la Pachamama",
        "theme": "Léxico de jurisprudencia ecológica, derechos de la naturaleza y buen vivir",
        "words": [
            {"lemma": "constituyente", "translation": "constitutional assembly delegate", "pos": "noun"},
            {"lemma": "biocéntrico", "translation": "biocentric, life-centered", "pos": "adjective"},
            {"lemma": "jurisprudencia", "translation": "jurisprudence, legal case law", "pos": "noun"},
            {"lemma": "regeneración", "translation": "ecological regeneration", "pos": "noun"},
            {"lemma": "tutela", "translation": "legal guardianship, protection", "pos": "noun"},
            {"lemma": "armonía", "translation": "harmony, ecological balance", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r4}-a-gr.json", {
        "id": "grammar.b2.ecuador.04.ecuador-constitucion-derechos-naturaleza",
        "title": "La Constitución de Montecristi: Pachamama y los Derechos de la Naturaleza",
        "sections": [
            {
                "type": "text",
                "content": "Aprobada por abrumadora votación popular en referéndum en 2008 tras intensas deliberaciones en la ciudad de Montecristi, la **Constitución de la República del Ecuador** protagonizó una revolución jurídica de escala planetaria: se convirtió en la **primera constitución en la historia de la humanidad en reconocer a la Naturaleza o Pachamama como sujeto de derechos plenos** (Artículos 71 al 74).\n\nEste giro copernicano reemplazó la clásica visión antropocéntrica (que consideraba a la naturaleza como mera propiedad o recurso inerte al servicio exclusivo de la economía) por un paradigma **biocéntrico** inspirado en la filosofía milenaria del **Sumak Kawsay** (el 'Buen Vivir' en lengua kichwa). Bajo este principio, la naturaleza tiene el derecho inalienable a que se respete integralmente su existencia, el mantenimiento y la regeneración de sus ciclos vitales, estructura y funciones ecológicas, facultando a cualquier ciudadano para exigir judicialmente su tutela y restauración integral frente a daños ambientales."
            },
            {
                "type": "table",
                "title": "Conceptos clave de la jurisprudencia de Montecristi",
                "rows": [
                    ["los Derechos de la Naturaleza", "legal personality of ecosystems: right to existence, restoration, and vital cycles"],
                    ["el Sumak Kawsay / Buen Vivir", "indigenous ethics of living in balanced harmony with communities and the biosphere"],
                    ["la justicia biocéntrica", "legal theory placing life and ecological integrity above capital accumulation"],
                    ["la acción de protección ambiental", "right of any citizen to litigate in court on behalf of rivers and forests"],
                    ["el principio precautorio", "duty of the state to halt activities where serious ecological harm is plausible"],
                    ["la Corte Constitucional", "highest tribunal setting precedents protecting rivers like the Vilcabamba and Los Cedros"]
                ]
            },
            {
                "type": "tip",
                "content": "En la histórica sentencia de 2021 sobre el Bosque Protector Los Cedros, la Corte Constitucional de Ecuador anuló concesiones mineras basándose en los Derechos de la Naturaleza, sentando un precedente global citado por juristas ambientales de los cinco continentes."
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
                    ["biocéntrico", "life-centered legal paradigm"],
                    ["jurisprudencia", "court precedents and legal theory"],
                    ["regeneración", "vital ecological renewal"],
                    ["tutela", "judicial protection mechanism"]
                ],
                "teaches": ["b2-ecuador-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La Constitución de 2008 consagró el principio del Sumak Kawsay, que en español se traduce como el Buen __. (Vivir)",
                "answer": "Vivir",
                "english": "The 2008 Constitution enshrined the principle of Sumak Kawsay, which in Spanish translates as Buen Vivir (Good Living).",
                "teaches": ["ecuador-constitucion-derechos-naturaleza"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué innovación jurídica histórica introdujo la Constitución de Montecristi en el derecho internacional?",
                "options": [
                    "Reconocer a la Naturaleza o Pachamama como sujeto de derechos con personería jurídica exigible ante los tribunales.",
                    "Eliminar los tribunales de justicia y sustituirlos por consejos militares provinciales.",
                    "Declarar que los ríos y bosques pertenecen exclusivamente a consorcios privados extranjeros.",
                    "Establecer que los recursos naturales no pueden ser investigados por universidades científicas."
                ],
                "correct": 0,
                "teaches": ["ecuador-constitucion-derechos-naturaleza"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Cualquier", "ciudadano", "puede", "exigir", "la", "restauración", "integral", "del", "ecosistema."],
                "solution": ["Cualquier", "ciudadano", "puede", "exigir", "la", "restauración", "integral", "del", "ecosistema."],
                "english": "Any citizen can demand the comprehensive restoration of the ecosystem.",
                "teaches": ["ecuador-constitucion-derechos-naturaleza"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Abogada ambientalista", "text": "¿Qué falló la Corte Constitucional en el caso del Bosque Protector Los Cedros?"},
                    {"speaker": "Magistrado", "text": "_____"}
                ],
                "options": [
                    "Determinó que la minería vulneraba los Derechos de la Naturaleza consagrados en la Constitución y canceló las concesiones extractivas.",
                    "Ordenó talar el bosque para construir un parqueadero de maquinaria pesada.",
                    "Declaró que la Constitución de Montecristi no tenía validez fuera de la capital.",
                    "Recomendó sustituir los árboles nativos por eucaliptos comerciales."
                ],
                "correct": 0,
                "teaches": ["ecuador-constitucion-derechos-naturaleza"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El paradigma biocéntrico postula que los ríos y bosques poseen valor intrínseco independiente de su utilidad comercial.",
                "english": "The biocentric paradigm posits that rivers and forests possess intrinsic value independent of their commercial utility.",
                "teaches": ["ecuador-constitucion-derechos-naturaleza"]
            }
        ]
    })

    # --- Lesson 5: b2-ecuador-05 ---
    r5 = f"{r_unit}-05"
    write_json(f"vocabulary/b2/{r5}-voc.json", {
        "id": "vocab.b2.ecuador.05",
        "lesson": r5,
        "title": "El petróleo amazónico, Yasuní-ITT y la consulta popular",
        "theme": "Léxico de conservación amazónica, pueblos en aislamiento y soberanía energética",
        "words": [
            {"lemma": "intangible", "translation": "intangible, strictly inviolable reserve", "pos": "adjective"},
            {"lemma": "aislamiento", "translation": "voluntary isolation of uncontacted tribes", "pos": "noun"},
            {"lemma": "biodiversidad", "translation": "biodiversity, ecological richness", "pos": "noun"},
            {"lemma": "extractivismo", "translation": "extractivism, resource depletion economy", "pos": "noun"},
            {"lemma": "referéndum", "translation": "referendum, binding ballot vote", "pos": "noun"},
            {"lemma": "yacimiento", "translation": "oil or mineral deposit/reserve", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r5}-a-gr.json", {
        "id": "grammar.b2.ecuador.05.ecuador-yasuni-petroleo-amazonia",
        "title": "El petróleo amazónico, Yasuní-ITT y la consulta popular histórica",
        "sections": [
            {
                "type": "text",
                "content": "En el corazón de la cuenca amazónica ecuatoriana, el **Parque Nacional Yasuní** (declarado Reserva de la Biosfera por la UNESCO en 1989) alberga la mayor densidad biológica documentada de la Tierra: una sola hectárea de su selva contiene más especies de árboles que todo el subcontinente norteamericano junto. Además, en esta floresta milenaria habitan los últimos clanes indígenas en **aislamiento voluntario** del Ecuador: los **Tagaeri** y los **Taromenane**, pueblos no contactados emparentados con la nacionalidad Waorani que han decidido rechazar cualquier contacto con la civilización industrial.\n\nSin embargo, bajo el subsuelo del sector oriental del parque, conocido como el bloque **ITT (Ishpingo-Tambococha-Tiputini)**, yacen cientos de millones de barriles de crudo pesado. Tras años de intensos debates entre la dependencia macroeconómica del petroestado y la preservación ecológica, en agosto de 2023 el pueblo ecuatoriano protagonizó un hito ambiental sin parangón en el mundo: en una histórica **consulta popular nacional vinculante**, casi el sesenta por ciento de los votantes aprobó dejar el petróleo del bloque Yasuní-ITT indefinidamente bajo tierra, sentando un precedente universal en la lucha contra la crisis climática."
            },
            {
                "type": "table",
                "title": "Hitos del dilema de Yasuní-ITT",
                "rows": [
                    ["el Parque Nacional Yasuní", "global biodiversity hotspot holding over 650 tree species per hectare"],
                    ["los Tagaeri y Taromenane", "indigenous nomadic clans living in voluntary isolation in the Amazon"],
                    ["la iniciativa Yasuní-ITT", "2007 proposal seeking global co-funding to keep 850M barrels underground"],
                    ["el colectivo Yasunidos", "youth and civil society campaign gathering signatures for a decade"],
                    ["la consulta popular de 2023", "first nationwide democratic referendum deciding to halt ongoing oil extraction"],
                    ["el desmontaje de infraestructura", "court-ordered plan to decommission oil wells and reforest Amazonian corridors"]
                ]
            },
            {
                "type": "tip",
                "content": "La consulta popular de Yasuní marcó la primera vez en la historia global que la ciudadanía de un país petrolero acudió a las urnas para votar democráticamente a favor de detener la explotación de hidrocarburos con el fin de proteger la selva y a los pueblos no contactados."
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
                    ["intangible", "inviolable conservation zone"],
                    ["aislamiento", "deliberate voluntary separation"],
                    ["extractivismo", "resource-dependent economic model"],
                    ["yacimiento", "underground petroleum reserve"]
                ],
                "teaches": ["b2-ecuador-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la consulta de agosto de 2023, la ciudadanía votó mayoritariamente por dejar el crudo bajo __ en el Yasuní. (tierra)",
                "answer": "tierra",
                "english": "In the August 2023 referendum, citizens voted by majority to leave the crude underground in Yasuní.",
                "teaches": ["ecuador-yasuni-petroleo-amazonia"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Quiénes son los pueblos Tagaeri y Taromenane que habitan en el Parque Nacional Yasuní?",
                "options": [
                    "Clanes indígenas que viven en aislamiento voluntario rechazando el contacto con la sociedad industrial.",
                    "Familias de colonos agrícolas procedentes de las provincias costeras de Guayaquil.",
                    "Ingenieros petroleros encargados del mantenimiento de los pozos de bombeo.",
                    "Comerciantes fluviales que exportan madera fina a los países vecinos."
                ],
                "correct": 0,
                "teaches": ["ecuador-yasuni-petroleo-amazonia"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Yasuní", "alberga", "la", "mayor", "densidad", "biológica", "documentada", "del", "planeta."],
                "solution": ["Yasuní", "alberga", "la", "mayor", "densidad", "biológica", "documentada", "del", "planeta."],
                "english": "Yasuní harbors the highest documented biological density on the planet.",
                "teaches": ["ecuador-yasuni-petroleo-amazonia"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ambientalista", "text": "¿Por qué el resultado del referéndum de Yasuní en 2023 fue calificado como un precedente mundial?"},
                    {"speaker": "Científica", "text": "_____"}
                ],
                "options": [
                    "Porque fue la primera vez en la historia que una nación votó en las urnas para suspender la extracción de petróleo y salvar la biodiversidad.",
                    "Porque el petróleo de Yasuní no tenía ningún valor comercial en los mercados internacionales.",
                    "Porque la votación se realizó exclusivamente a través de mensajes de telefonía móvil.",
                    "Porque la Corte Internacional de La Haya impuso el resultado de manera obligatoria."
                ],
                "correct": 0,
                "teaches": ["ecuador-yasuni-petroleo-amazonia"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La protección de los pueblos no contactados exige salvaguardar sus territorios ancestrales de cualquier incursión extractiva.",
                "english": "Protecting uncontacted peoples requires safeguarding their ancestral territories from any extractive incursion.",
                "teaches": ["ecuador-yasuni-petroleo-amazonia"]
            }
        ]
    })

    # --- Lesson 6: b2-ecuador-consolidation ---
    r6_con = f"{r_unit}-consolidation"
    write_json(f"exercises/b2/{r6_con}-ex.json", {
        "lesson": r6_con,
        "exercises": [
            {
                "id": f"{r6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["callejón", "inter-Andean corridor"],
                    ["endemismo", "unique native species"],
                    ["plurinacional", "multi-nation civic model"],
                    ["intangible", "inviolable conservation territory"]
                ],
                "teaches": ["b2-ecuador-vocab"]
            },
            {
                "id": f"{r6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Chimborazo es el punto más alejado del centro de la Tierra debido al abultamiento __ del planeta. (ecuatorial)",
                "answer": "ecuatorial",
                "english": "Chimborazo is the farthest point from the center of the Earth due to the planet's equatorial bulge.",
                "teaches": ["ecuador-volcanes-callejon-interandino"]
            },
            {
                "id": f"{r6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué corrientes oceánicas confluyen en el archipiélago de Galápagos generando su insólita riqueza biológica?",
                "options": [
                    "La corriente fría de Humboldt, la corriente cálida de Panamá y la corriente submarina de Cromwell.",
                    "La corriente del Golfo, la corriente de Benguela y la corriente del Labrador.",
                    "La corriente de California y la corriente de las Malvinas.",
                    "La corriente monzónica de Madagascar y el canal de Mozambique."
                ],
                "correct": 0,
                "teaches": ["ecuador-galapagos-evolucion-darwin"]
            },
            {
                "id": f"{r6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La Constitución de Montecristi reconoció formalmente a la __ como sujeto titular de derechos constitucionales. (Pachamama)",
                "answer": "Pachamama",
                "english": "The Constitution of Montecristi formally recognized the Pachamama as a subject holding constitutional rights.",
                "teaches": ["ecuador-constitucion-derechos-naturaleza"]
            },
            {
                "id": f"{r6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué demostró la consulta popular vinculante sobre el bloque petrolero Yasuní-ITT celebrada en 2023?",
                "options": [
                    "Que una sociedad puede decidir democráticamente priorizar la conservación de la selva virgen sobre las rentas petroleras.",
                    "Que los parques nacionales deben ser explotados por corporaciones transnacionales sin restricciones.",
                    "Que los pueblos indígenas están a favor de la construcción de refinerías en sus comunidades.",
                    "Que la Constitución de 2008 prohibía votar sobre temas ambientales."
                ],
                "correct": 0,
                "teaches": ["ecuador-yasuni-petroleo-amazonia"]
            },
            {
                "id": f"{r6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Ecuador", "reúne", "cuatro", "mundos", "diversos", "en", "un", "solo", "territorio."],
                "solution": ["Ecuador", "reúne", "cuatro", "mundos", "diversos", "en", "un", "solo", "territorio."],
                "english": "Ecuador brings together four diverse worlds in a single territory.",
                "teaches": ["ecuador-volcanes-callejon-interandino"]
            },
            {
                "id": f"{r6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La plurinacionalidad y el Sumak Kawsay definen la búsqueda ecuatoriana de una convivencia armónica entre pueblos y naturaleza.",
                "english": "Plurinationality and Sumak Kawsay define Ecuador's quest for harmonious coexistence between peoples and nature.",
                "teaches": ["ecuador-constitucion-derechos-naturaleza"]
            },
            {
                "id": f"{r6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la trascendencia de la educación intercultural bilingüe impulsada por la CONAIE?",
                "options": [
                    "Garantizar la preservación y vitalidad académica de las lenguas originarias como el Kichwa y el Shuar en el sistema escolar.",
                    "Obligar a todos los estudiantes a cursar sus carreras universitarias en idiomas asiáticos.",
                    "Suprimir las asignaturas de ciencias naturales y matemáticas en las escuelas rurales.",
                    "Limitar la enseñanza escolar exclusivamente a la formación religiosa conventual."
                ],
                "correct": 0,
                "teaches": ["ecuador-conaie-movimiento-indigena"]
            }
        ]
    })

    # -------------------------------------------------------------------------
    # 4. REGIONAL STORIES: Ecuador (6 stories, strictly 650-825 words each)
    # -------------------------------------------------------------------------
    # Story 1: Volcanes del callejón interandino
    story_ecuador_01 = {
        "id": "b2-ecuador-01",
        "title": "La avenida de los volcanes: Donde la tierra toca el cielo",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica de viaje y exploración científica a lo largo del callejón interandino ecuatoriano: el legado de Alexander von Humboldt en las faldas del Chimborazo, el cono perfecto y activo del Cotopaxi, la arquitectura barroca de Quito y Cuenca, y el papel vital de los páramos andinos como fuentes de agua dulce para las poblaciones de las alturas.",
        "characters": [
            "Alexander von Humboldt",
            "Carlos Montúfar",
            "Elena Carvajal",
            "Mateo Quispe"
        ],
        "narration": {
            "paragraphs": [
                "En el amanecer límpido de los Andes ecuatorianos, cuando la niebla se disipa de los valles y deja al descubierto una muralla infinita de crestas nevadas, es fácil comprender la admiración que sintió el naturalista prusiano Alexander von Humboldt al recorrer esta geografía en 1802. Acompañado por el botánico francés Aimé Bonpland y el joven criollo quiteño Carlos Montúfar, Humboldt quedó maravillado ante la procesión ininterrumpida de conos volcánicos que escoltan el callejón interandino a lo largo de más de cuatrocientos kilómetros. Con justa fascinación poética y rigor científico, el sabio bautizó a esta majestuosa depresión orográfica como la 'Avenida de los Volcanes'.",
                "En el corazón de esta cordillera se alza el imponente Chimborazo, coloso extinto cuyos glaciares eternos alcanzan los 6.263 metros sobre el nivel del mar. Para los pueblos Puruhá que habitan sus faldas desde tiempos inmemoriales, la montaña es el Taita Chimborazo, un padre protector sagrado. La ciencia moderna confirmó una singularidad cósmica que Humboldt ya sospechaba: debido a la rotación de la Tierra y al consiguiente ensanchamiento ecuatorial del planeta en la latitud cero, la cumbre del Chimborazo es el punto más alejado del núcleo terrestre y, por ende, el lugar más cercano al sol sobre la superficie de nuestro globo.",
                "Humboldt intentó escalar el Chimborazo provisto únicamente de pesados barómetros de mercurio, botas ordinarias de cuero y abrigos de lana. Aunque el frío polar, el mal de montaña y las grietas insalvables forzaron al sabio a detenerse a unos cientos de metros del cráter, sus mediciones minuciosas sobre la altitud, la presión atmosférica y los pisos de vegetación sentaron las bases universales de la biogeografía moderna. En sus cuadernos de campo, Humboldt ilustró cómo las plantas se escalonan en franjas precisas a medida que se asciende desde las selvas húmedas de la costa hasta el gélido páramo. Al descender de la montaña, Humboldt plasmó en su célebre grabado del Cuadro de la naturaleza una síntesis gráfica donde cada especie vegetal, animal y mineral se integraba en una red de interdependencias ecológicas armoniosas que anticipó el pensamiento ambiental contemporáneo.",
                "Más al norte, el volcán Cotopaxi vigila el horizonte con su cono simétrico perfecto cubierto por un manto deslumbrante de hielo perenne. A diferencia del sosegado Chimborazo, el Cotopaxi es uno de los estratovolcanes activos más altos y vigilados del mundo. Sus erupciones históricas han esculpido la topografía del valle de Latacunga con gigantescos lahares y flujos piroclásticos, recordando a los pobladores andinos que la fertilidad asombrosa de sus suelos agrícolas es hija directa de la lava y la ceniza mineral expulsadas por las entrañas de la tierra.",
                "Abrazadas por estos volcanes milenarios florecieron las dos joyas urbanas del patrimonio continental ecuatoriano. Quito, edificada a 2.850 metros de altitud en las faldas del volcán Pichincha, deslumbró al mundo en 1978 al ser declarada el primer Patrimonio Cultural de la Humanidad por la UNESCO. Su centro histórico colonial, el más extenso y mejor conservado de América, alberga conventos deslumbrantes como San Francisco y La Compañía de Jesús, cuyos retablos barrocos tallados en madera y cubiertos de pan de oro fusionan la imaginería católica con soles y querubines mestizos de rasgos indígenas.",
                "Hacia el sur del corredor interandino, la ciudad de Cuenca seduce con su sosiego republicano, sus techos de teja rojiza y sus cuatro ríos cantarines. En sus calles adoquinadas pervive el arte centenario de las tejedoras de los célebres sombreros de paja toquilla —conocidos erróneamente en el mercado global como 'Panama hats'—, una técnica textil ancestral que transforma fibras vegetales de la costa en finísimas piezas de colección que requieren meses de paciencia. Al recorrer los talleres artesanales de Cuenca, el visitante percibe la maestría con que las artesanas seleccionan cada hebra de fibra flexible, entrelazándola con movimientos rítmicos heredados de madres a hijas durante generaciones.",
                "Sin embargo, el alma invisible que hace posible la vida en todo el callejón interandino reside en el páramo. Estos ecosistemas de alta montaña, cubiertos de pajonales dorados y almohadillas vegetales de musgo, operan como inmensas esponjas naturales capaces de absorber la humedad que traen los vientos alisios de la Amazonía para filtrarla lentamente hacia los ríos y embalses. Cuidar la Avenida de los Volcanes es, en última instancia, salvaguardar el santuario hídrico del cual beben millones de ciudadanos en la mitad del mundo."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Quién acuñó en 1802 la célebre expresión 'Avenida de los Volcanes' para describir el callejón interandino?",
                        "options": [
                            "El sabio y naturalista prusiano Alexander von Humboldt durante sus exploraciones científicas.",
                            "El conquistador español Sebastián de Belalcázar al fundar la ciudad de Quito.",
                            "El novelista indigenista Jorge Icaza en su famosa obra Huasipungo.",
                            "El científico británico Charles Darwin durante su travesía en el HMS Beagle."
                        ],
                        "correctIndex": 0,
                        "explanation": "Alexander von Humboldt acuñó este nombre en 1802 al quedar fascinado por la hilera continua de colosos volcánicos que flanquean la sierra ecuatoriana."
                    },
                    {
                        "question": "¿Por qué el volcán Chimborazo es considerado el punto más cercano al sol sobre la Tierra?",
                        "options": [
                            "Debido al ensanchamiento ecuatorial del planeta en latitud cero, que aleja su cima del centro de la Tierra más que el Everest.",
                            "Porque se encuentra en una meseta donde la temperatura atmosférica es superior a los cincuenta grados.",
                            "Porque es la montaña con mayor altitud oficial medida desde el nivel del mar.",
                            "Debido a que sus erupciones proyectan lava a decenas de kilómetros hacia la estratosfera."
                        ],
                        "correctIndex": 0,
                        "explanation": "Por el abultamiento del globo terrestre en la zona ecuatorial, la cima del Chimborazo se proyecta más lejos del centro de la Tierra que cualquier otra montaña del planeta."
                    },
                    {
                        "question": "¿Qué función ecológica primordial desempeñan los páramos andinos en el callejón interandino?",
                        "options": [
                            "Absorben la humedad atmosférica como esponjas naturales y regulan el suministro de agua dulce para valles y ciudades.",
                            "Producen maderas duras utilizadas exclusivamente para la construcción de barcos mercantes.",
                            "Evitan que los volcanes entren en erupción mediante corrientes de vapor geotérmico.",
                            "Son zonas desérticas destinadas al almacenamiento de minerales pesados."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los páramos actúan como reguladores e inmensas esponjas hidrológicas que captan agua de nieblas y lluvias para alimentar cuencas y acueductos."
                    }
                ]
            }
        }
    }

    # Story 2: Galápagos y la evolución
    story_ecuador_02 = {
        "id": "b2-ecuador-02",
        "title": "Galápagos: Las islas encantadas donde el tiempo esculpe la vida",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía biológica e histórica por el archipiélago de Galápagos: su origen volcánico sobre un punto caliente oceánico, las adaptaciones insólitas de las iguanas marinas y tortugas gigantes, la estancia crucial de Charles Darwin en 1835 y los retos contemporáneos de conservación en la Reserva Marina de Galápagos y el corredor biológico Hermandad.",
        "characters": [
            "Charles Darwin",
            "Capitán Robert FitzRoy",
            "Doctora Silvia Vega",
            "Guardaparque Marcelo Ramos"
        ],
        "narration": {
            "paragraphs": [
                "Emergiendo de las aguas profundas del océano Pacífico a casi mil kilómetros de las costas del Ecuador, el archipiélago de Galápagos parece pertenecer a otro planeta. Sus paisajes de lava negra solidificada, conos de ceniza roja y playas de arena olivina fueron moldeados por la furia de erupciones volcánicas submarinas que continúan activas en las islas occidentales de Fernandina e Isabela. En los primeros siglos coloniales, los navegantes españoles llamaron a este archipiélago las 'Islas Encantadas' porque las corrientes marítimas traicioneras y las espesas neblinas garúas daban la misteriosa ilusión de que las islas flotaban y cambiaban de posición a capricho en medio de la inmensidad marina.",
                "En septiembre de 1835, el bergantín de investigación británico HMS Beagle fondeó frente a la isla San Cristóbal. A bordo viajaba un joven naturalista de veintiséis años llamado Charles Darwin, cuya curiosidad infatigable cambiaría para siempre la comprensión humana de la naturaleza. Al desembarcar en aquel territorio pedregoso y desolado, Darwin sintió que retrocedía en el tiempo hacia los albores de la creación. Lo que más desconcertó al científico no fue la aridez del terreno, sino la extraordinaria docilidad de los animales, que carecían por completo de miedo instintivo hacia los seres humanos debido a la ausencia milenaria de grandes depredadores terrestres.",
                "En las rocas basálticas azotadas por el oleaje, Darwin observó perplejo a las iguanas marinas. A diferencia de todos los demás lagartos del planeta, que habitan en árboles o madrigueras terrestres, estos reptiles de aspecto prehistórico habían desarrollado garras afiladas para anclarse a las rocas submarinas contra la corriente, colas aplanadas para nadar con agilidad y glándulas especiales en el hocico para estornudar el exceso de sal marina que ingieren mientras pastan algas en las profundidades del océano.",
                "El segundo misterio biológico se manifestó en las tortugas gigantes que dan nombre al archipiélago. El vicegobernador local mencionó a Darwin una observación asombrosa: un baquiano experto podía adivinar con total exactitud de qué isla procedía una tortuga con solo examinar la forma de su caparazón. En las islas húmedas con vegetación abundante en el suelo, las tortugas poseían caparazones abovedados en forma de cúpula; en cambio, en las islas secas donde el alimento escaseaba y las ramas de cactus crecían altas, las tortugas exhibían caparazones en forma de silla de montar, con una pronunciada escotadura frontal que les permitía estirar el cuello hacia arriba para alimentarse.",
                "La intuición de Darwin maduró al estudiar a los sinsontes y a los pequeños pinzones recolectados en las diversas islas. Cada población insular presentaba una forma y tamaño de pico perfectamente adaptados a su dieta particular: unos tenían picos gruesos y robustos para triturar semillas duras, otros picos finos y curvados para extraer néctar de flores, y otros empleaban espinas de cactus como herramientas para desenterrar larvas de corteza. Si todas aquellas especies procedían de un antepasado común llegado del continente, ¿cómo explicar tanta diversidad? La respuesta germinaría años más tarde en su obra cumbre: la selección natural esculpía gradualmente a los seres vivos a través de adaptaciones acumuladas a lo largo de las eras geológicas.",
                "Hoy en día, el valor biológico de Galápagos trasciende sus orillas terrestres. En las aguas transparentes de la Reserva Marina de Galápagos convergen la fría corriente de Humboldt, la cálida de Panamá y la surgencia de Cromwell, creando uno de los hábitats marinos más fértiles y biodiversos del planeta. En los santuarios de las islas norteñas de Darwin y Wolf se congregan miles de tiburones martillo en cardúmenes hipnóticos, junto a ballenas jorobadas, mantarrayas gigantes y tortugas marinas verdes.",
                "La creación en 2022 de la reserva marina 'Hermandad' sumó sesenta mil kilómetros cuadrados adicionales de protección estricta, blindando el corredor biológico que conecta Galápagos con las aguas de Costa Rica y Colombia. En este laboratorio vivo de la evolución, científicos, guardaparques y pescadores locales aúnan esfuerzos para demostrar al mundo que la supervivencia de la vida silvestre depende de la capacidad humana para respetar el ritmo milenario con que la naturaleza teje sus prodigios."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singular adaptación biológica poseen las iguanas marinas de Galápagos frente a otros lagartos?",
                        "options": [
                            "Bucean en el océano para alimentarse de algas y expulsan el exceso de sal por glándulas nasales.",
                            "Tienen alas membranosas que les permiten volar entre las islas cercanas.",
                            "Ponen huevos en nidos construidos en las copas de los árboles tropicales.",
                            "Mudan de piel cada semana para almacenar agua dulce en el desierto."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las iguanas marinas son los únicos lagartos marinos del planeta: bucean para alimentarse de algas y poseen glándulas para expulsar la sal marina concentrada."
                    },
                    {
                        "question": "¿Qué indicio clave sobre las tortugas gigantes ayudó a Darwin a comprender la evolución adaptativa?",
                        "options": [
                            "Que la forma de su caparazón variaba según la vegetación y el clima de cada isla particular.",
                            "Que todas las tortugas del archipiélago compartían exactamente el mismo ADN sin variación.",
                            "Que las tortugas migraban a nado miles de kilómetros hacia la costa del continente.",
                            "Que se alimentaban exclusivamente de peces capturados en la orilla del mar."
                        ],
                        "correctIndex": 0,
                        "explanation": "La variación morfológica de los caparazones (abovedados en islas húmedas frente a silla de montar en islas secas) demostraba la adaptación insular al medio."
                    },
                    {
                        "question": "¿Qué objetivo persigue la creación de la reserva marina 'Hermandad' en 2022?",
                        "options": [
                            "Proteger el corredor biológico migratorio que conecta Galápagos con las reservas de Costa Rica y Colombia.",
                            "Fomentar la pesca de arrastre industrial en alta mar sin restricciones ambientales.",
                            "Construir plataformas de exploración petrolera submarina fuera de la costa.",
                            "Facilitar el tráfico comercial de buques de carga de gran calado entre los continentes."
                        ],
                        "correctIndex": 0,
                        "explanation": "La reserva Hermandad blindó sesenta mil kilómetros cuadrados para proteger las rutas migratorias marinas compartidas con la Isla del Coco y Malpelo."
                    }
                ]
            }
        }
    }

    # Story 3: CONAIE y levantamiento indigena
    story_ecuador_03 = {
        "id": "b2-ecuador-03",
        "title": "El despertar del cóndor: El levantamiento histórico de las nacionalidades indígenas",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica épica sobre la transformación política del Ecuador moderno: la fundación de la CONAIE en 1986, el histórico levantamiento nacional del Inti Raymi en 1990 que bloqueó carreteras y marchó sobre Quito, la conquista de la educación intercultural bilingüe y la consagración constitucional del Estado Plurinacional.",
        "characters": [
            "Luis Macas",
            "Blanca Chancoso",
            "Alberto Conejo",
            "Mariana Yumbay"
        ],
        "narration": {
            "paragraphs": [
                "Durante casi cinco siglos de historia colonial y republicana, los pueblos originarios del Ecuador fueron tratados por las élites dominantes como sombras invisibles confinadas a la servidumbre de las haciendas andinas o a la lejanía impenetrable de las selvas amazónicas. Se asumía con soberbia paternalista que el campesino indígena carecía de voz política y que su único porvenir consistía en una asimilación cultural silenciosa que borrara su idioma, sus saberes agrícolas y su memoria comunitaria. Sin embargo, en las entrañas de las comunidades de base, al calor de las asambleas comunales y del trabajo solidario de la minga, se gestaba una fuerza colectiva que cambiaría el destino de la república para siempre. En las comunidades andinas, la minga no constituía únicamente una faena de trabajo colectivo gratuito para limpiar acequias o techar casas; era una verdadera escuela de deliberación horizontal donde cada voz tenía peso y donde las decisiones colectivas se forjaban por consenso pacífico.",
                "En 1986, tras años de confluencia paciente entre las federaciones campesinas de la Sierra (Ecuarunari) y los pueblos indígenas de la cuenca amazónica (Confeniae), nació la Confederación de Nacionalidades Indígenas del Ecuador (CONAIE). La gran innovación de esta organización fue superar las reivindicaciones meramente gremiales o salariales para plantear un desafío civilizatorio integral: los pueblos indígenas no eran simples sectores pobres o campesinos desposeídos; eran nacionalidades ancestrales preexistentes al Estado criollo, con derecho a su territorio, su idioma, sus sistemas de justicia y su libre determinación.",
                "El terremoto sociopolítico estalló el 28 de mayo de 1990, en vísperas de las tradicionales celebraciones andinas del solsticio del Inti Raymi. En una acción coordinada con asombrosa disciplina comunitaria, cientos de miles de comuneros salieron pacíficamente a las carreteras de diez provincias de la Sierra y el Oriente, bloqueando el transporte interprovincial con barricadas de troncos, piedras y zanjas. Al mismo tiempo, miles de hombres y mujeres de poncho rojo y sombrero oscuro ocuparon de forma pacífica la histórica iglesia de Santo Domingo en el centro de Quito, transformando el templo colonial en cuartel general del diálogo y la resistencia.",
                "La sociedad urbana de la capital contempló estupefacta un espectáculo inédito: una inmensa marea humana disciplinada, liderada por dirigentes lúcidos y elocuentes como Luis Macas y Blanca Chancoso, que dialogaban de igual a igual con los ministros de Estado, portando un pliego de dieciséis demandas fundamentales. Los indígenas no exigían privilegios; reclamaban la legalización de tierras comunales usurpadas por terratenientes, la condonación de deudas agrícolas ruinosas, presupuesto para el agua de riego, el fin del hostigamiento a las comunidades y la creación de una Dirección Nacional de Educación Intercultural Bilingüe gestionada por las propias nacionalidades. Desde las tarimas improvisadas, los oradores hablaban con pausada firmeza, demostrando que la dignidad de un pueblo no se mide por sus bienes materiales, sino por la coherencia ética de sus convicciones y la memoria viva de sus antepasados.",
                "El gobierno nacional se vio obligado a sentarse a negociar en mesas públicas de concertación. Aquel histórico 'Levantamiento de 1990' demostró al país y al continente que el movimiento indígena era el actor político más organizado, coherente y moralmente legítimo del Ecuador. Las radios comunitarias transmitían los debates en kichwa y shuar, mientras en las plazas los comuneros repartían comida de sus cosechas a los vecinos pobres de las barriadas urbanas, tejiendo lazos de empatía y desarmando los prejuicios racistas heredados de la época colonial.",
                "El impacto del movimiento se proyectó de inmediato en el ámbito institucional. En 1995, la CONAIE impulsó la creación del Movimiento de Unidad Plurinacional Pachakutik, su brazo electoral autónomo, que en los comicios subsiguientes conquistó decenas de alcaldías, prefecturas y escaños parlamentarios. Los líderes indígenas dejaron de ser espectadores en los pasillos del Congreso para convertirse en legisladores que redactaban leyes, fiscalizaban a los gobernantes y defendían los derechos colectivos.",
                "La consagración definitiva de esta lucha de generaciones llegó con la Asamblea Constituyente de Montecristi en 2008, cuando la Constitución definió formalmente al Ecuador como un 'Estado constitucional de derechos y justicia, social, democrático, soberano, independiente, unitario, intercultural, plurinacional y laico'. Aquel despertar del cóndor en 1990 enseñó a toda América Latina que una democracia auténtica no consiste en la imposición de una mayoría uniforme, sino en la convivencia digna de pueblos diversos unidos por la justicia y el respeto mutuo."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué innovación política fundamental introdujo la CONAIE desde su fundación en 1986?",
                        "options": [
                            "Plantear que los indígenas son nacionalidades ancestrales con derechos colectivos y modelo de Estado Plurinacional.",
                            "Exigir que todas las haciendas agrícolas del país fueran entregadas a corporaciones extranjeras.",
                            "Limitar la lucha social a la petición de aumentos de sueldo para peones asalariados.",
                            "Promover la disolución de las comunidades tradicionales para fomentar la vida urbana individual."
                        ],
                        "correctIndex": 0,
                        "explanation": "La CONAIE transformó la lucha campesina en una demanda civilizatoria de nacionalidades indígenas con derecho a la plurinacionalidad y autonomía."
                    },
                    {
                        "question": "¿Cuál fue el detonante y escenario visible del histórico Levantamiento de mayo de 1990?",
                        "options": [
                            "El bloqueo pacífico coordinado de carreteras y la ocupación pacífica de la iglesia de Santo Domingo en Quito.",
                            "Un combate armado contra las fuerzas de seguridad en la frontera marítima con Perú.",
                            "La firma de un tratado de libre comercio con los países de América del Norte.",
                            "La clausura voluntaria de todas las escuelas rurales de la provincia del Guayas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El levantamiento paralizó las carreteras de la sierra y ocupó pacíficamente Santo Domingo en Quito para exigir diálogo público y tierras comunitarias."
                    },
                    {
                        "question": "¿Qué definición del Estado ecuatoriano se consagró en la Constitución de 2008 gracias a estas movilizaciones?",
                        "options": [
                            "La definición del Ecuador como un Estado constitucional, intercultural y plurinacional.",
                            "La declaración de un régimen absolutista centrado en el poder militar.",
                            "El establecimiento de una confederación de provincias autónomas sin gobierno central.",
                            "La prohibición de partidos políticos fundados por movimientos sociales."
                        ],
                        "correctIndex": 0,
                        "explanation": "La Constitución de Montecristi consagró en su primer artículo que el Ecuador es un Estado intercultural y plurinacional."
                    }
                ]
            }
        }
    }

    # Story 4: Montecristi y los Derechos de la Naturaleza
    story_ecuador_04 = {
        "id": "b2-ecuador-04",
        "title": "El pacto de Montecristi: Cuando los ríos y montañas ganaron voz",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La crónica de un hito en la historia del derecho universal: las deliberaciones de la Asamblea Constituyente de Montecristi en 2008, la incorporación de la filosofía kichwa del Sumak Kawsay, la consagración de la Pachamama como sujeto de derechos inalienables y los fallos pioneros de la Corte Constitucional en defensa de los bosques y ríos.",
        "characters": [
            "Alberto Acosta",
            "Mónica Chuji",
            "Doctor Ramiro Ávila",
            "Leonor Santi"
        ],
        "narration": {
            "paragraphs": [
                "En la soleada meseta de Montecristi, cuna del legendario líder liberal Eloy Alfaro, un viento de renovación soplaba sobre las colinas manabitas a mediados de 2008. En la sede de la Asamblea Constituyente, erigida especialmente para refundar las bases institucionales del país tras una década de inestabilidad política y crisis bancarias, ciento treinta asambleístas debatían el texto de una nueva carta magna. Sin embargo, en aquellas salas climatizadas no solo se discutían la separación de poderes o los presupuestos estatales ordinarios; se estaba gestando la transformación jurídica más audaz y vanguardista de la historia del constitucionalismo moderno.",
                "Impulsados por líderes indígenas, filósofos andinos y juristas ecologistas encabezados por Alberto Acosta y Mónica Chuji, los asambleístas colocaron sobre la mesa una premisa que al principio descolocó a los abogados formados en la dogmática clásica: la necesidad de reconocer a la Naturaleza o Pachamama como sujeto de derechos con personería jurídica propia. Durante siglos, la tradición legal occidental había considerado al medio ambiente como un objeto inerte, una propiedad privada o un recurso económico explotable que solo merecía protección en la medida en que afectaba la salud o el patrimonio de los seres humanos. Los juristas indígenas recordaron a la asamblea que la civilización moderna enfrentaba un colapso ecológico precisamente por haber cosificado a la naturaleza, convirtiendo ríos caudalosos y selvas milenarias en meros vertederos de desechos industriales o almacenes de materias primas intercambiables.",
                "Frente a esa visión antropocéntrica y utilitaria, la Constitución de Montecristi propuso una ruptura epistemológica radical sustentada en el Sumak Kawsay, el 'Buen Vivir' de la cosmovisión kichwa. Para los pueblos andinos y amazónicos, los humanos no son dueños ni administradores omnipotentes de la creación, sino una hebra más en el tejido vivo de la biosfera. El Buen Vivir no persigue el consumo material infinito ni la acumulación ilimitada de riquezas, sino una convivencia armónica y equitativa entre las comunidades humanas y la madre tierra que las sustenta.",
                "Tras intensos debates parlamentarios que captaron la atención de constitucionalistas de todo el planeta, el 20 de octubre de 2008 el pueblo ecuatoriano ratificó en las urnas la nueva Constitución con casi el sesenta y cuatro por ciento de los votos. En su revolucionario Capítulo Séptimo, el Artículo 71 estableció de manera categórica: «La naturaleza o Pacha Mama, donde se reproduce y realiza la vida, tiene derecho a que se respete integralmente su existencia y el mantenimiento y regeneración de sus ciclos vitales, estructura, funciones y procesos evolutivos».",
                "Por primera vez en la jurisprudencia universal, un río, un bosque tropical o una especie en peligro de extinción dejaban de ser cosas para convertirse en titulares de derechos inalienables. Además, el Artículo 72 consagró el derecho autónomo de la naturaleza a la restauración integral frente a impactos ambientales graves, independientemente de las indemnizaciones económicas debidas a las personas afectadas. Crucialmente, la Constitución facultó a cualquier ciudadano, comunidad o colectivo a interponer acciones judiciales de protección en nombre de los ecosistemas vulnerados.",
                "Los escépticos vaticinaron que aquellos artículos quedarían como mera poesía jurídica inaplicable en la práctica. No obstante, los tribunales ecuatorianos pronto comenzaron a aplicar el mandato constitucional. El primer precedente trascendental ocurrió en 2011 con el caso del río Vilcabamba en la provincia de Loja, donde una corte cantonal ordenó paralizar el ensanchamiento de una carretera municipal y restaurar el cauce fluvial dañado invocando directamente los derechos del río. Los jueces comprendieron que el daño infligido a la cuenca hidrográfica no podía repararse mediante multas pecuniarias ordinarias, sino que requería una reforestación activa de las riberas y la restauración biológica de los sedimentos arrastrados por las retroexcavadoras.",
                "Una década después, en diciembre de 2021, la Corte Constitucional de Ecuador emitió un fallo de alcance global en el caso del Bosque Protector Los Cedros: los magistrados determinaron que la minería a gran escala vulneraba los derechos intrínsecos de los anfibios, aves y bosques de neblina protegidos, anulando las concesiones otorgadas por el Estado. Aquella sentencia histórica consolidó la doctrina de que los ecosistemas frágiles gozan de protección constitucional prioritaria frente a proyectos económicos destructivos. El pacto de Montecristi demostró que el derecho puede ser una herramienta viva de sabiduría ecológica, recordándole a la humanidad entera que no puede haber futuro posible para los seres humanos sobre una tierra despojada de su dignidad natural."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué cambio paradigmático introdujo el Artículo 71 de la Constitución de Montecristi de 2008?",
                        "options": [
                            "Reconoció a la Naturaleza o Pachamama como sujeto pleno de derechos inalienables con personería jurídica.",
                            "Declaró que todos los recursos naturales debían ser exportados sin procesamiento industrial previo.",
                            "Estableció que solo las empresas mineras extranjeras tenían derecho a administrar los ríos.",
                            "Eliminó el derecho de los ciudadanos a presentar demandas por contaminación ambiental."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Artículo 71 convirtió por primera vez en el mundo a la Naturaleza en titular de derechos constitucionales plenos a su existencia y regeneración."
                    },
                    {
                        "question": "¿Qué concepto ético indígena sirvió de fundamento filosófico para los Derechos de la Naturaleza en Montecristi?",
                        "options": [
                            "El Sumak Kawsay o Buen Vivir, que postula la armonía comunitaria con la biosfera frente a la acumulación infinita.",
                            "La doctrina mercantilista del libre comercio colonial sin intervención judicial.",
                            "El feudalismo agrario heredado de las encomiendas españolas del siglo dieciséis.",
                            "El individualismo contractualista de las bolsas de valores financieras internacionales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El concepto kichwa de Sumak Kawsay inspiró el modelo biocéntrico de equilibrio armónico entre seres humanos y ecosistemas."
                    },
                    {
                        "question": "¿Qué resolvió la Corte Constitucional de Ecuador en 2021 en el histórico caso del Bosque Los Cedros?",
                        "options": [
                            "Anuló las concesiones mineras al constatar que vulneraban los Derechos de la Naturaleza en el bosque de neblina.",
                            "Ordenó desmantelar el bosque para facilitar el paso de oleoductos comerciales.",
                            "Determinó que los bosques protegidos no tenían derecho a ser defendidos en tribunales.",
                            "Permitió la caza deportiva de especies de anfibios en peligro de extinción."
                        ],
                        "correctIndex": 0,
                        "explanation": "La Corte aplicó los Derechos de la Naturaleza para frenar la actividad minera y proteger la biodiversidad amenazada en Los Cedros."
                    }
                ]
            }
        }
    }

    # Story 5: Yasuní-ITT y el petróleo amazónico
    story_ecuador_05 = {
        "id": "b2-ecuador-05",
        "title": "Yasuní: El latido verde de la selva frente al crudo",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La epopeya social y ecológica del Parque Nacional Yasuní: su prodigiosa biodiversidad amazónica, la protección de los pueblos no contactados Tagaeri y Taromenane, el dilema extractivista del bloque petrolero ITT, la perseverancia de una década del colectivo juvenil Yasunidos y la histórica consulta popular de 2023.",
        "characters": [
            "Alicia Cahuiya",
            "Pedro Bermeo",
            "Doctora Kelly Swing",
            "Tepare Enqueri"
        ],
        "narration": {
            "paragraphs": [
                "Visto desde la ventanilla de una avioneta ligera que sobrevuela la cuenca baja de los ríos Napo y Tiputini, el Parque Nacional Yasuní se despliega como un océano verde e infinito que se pierde en la bruma del horizonte amazónico. Declarada Reserva de la Biosfera por la UNESCO en 1989, esta floresta de casi un millón de hectáreas representa el epicentro biológico más exuberante del planeta Tierra. Los científicos de la Estación de Biodiversidad Tiputini han contabilizado en una sola hectárea de su bosque más de seiscientas cincuenta especies de árboles nativos —una cifra superior a la totalidad de especies arbóreas de Estados Unidos y Canadá combinados—, junto a cientos de anfibios de colores iridiscentes, jaguares y bandadas de guacamayos escarlata.",
                "En la espesura de este edén húmedo laten también los últimos testimonios de la vida nómada originaria del continente. Los Tagaeri y los Taromenane, clanes emparentados con la nacionalidad Waorani, viven en aislamiento voluntario en la denominada Zona Intangible del parque. Guiados por los ritmos de las estaciones fluviales, cazando con largas cerbatanas de chonta y lanzas de madera dura, estos pueblos han elegido rechazar tajantemente cualquier contacto con la civilización petrolera, dependiendo absolutamente de la selva intacta para su supervivencia física y espiritual.",
                "Sin embargo, la inmensa riqueza sobre el dosel selvático contrastaba con otra riqueza oculta en las profundidades geológicas del subsuelo. En el extremo oriental del parque se descubrió el yacimiento petrolero Ishpingo-Tambococha-Tiputini (ITT), que contenía reservas estimadas en más de ochocientos millones de barriles de crudo pesado. Para un país como Ecuador, cuya economía fiscal dependía estrechamente de los ingresos por exportación de hidrocarburos para financiar escuelas, hospitales y carreteras, la tentación de perforar el corazón del Yasuní representaba un dilema ético desgarrador.",
                "En 2007, el gobierno ecuatoriano lanzó ante la Asamblea General de la ONU una propuesta pionera y visionaria: la Iniciativa Yasuní-ITT. El país se comprometía solemnemente a dejar el crudo del bloque indefinidamente bajo tierra para evitar la emisión de cuatrocientos millones de toneladas de dióxido de carbono y proteger a los pueblos en aislamiento, a cambio de que la comunidad internacional compensara al Estado con la mitad de los ingresos que habría obtenido por la venta del petróleo. Lamentablemente, la falta de aportes financieros suficientes por parte de las potencias industriales provocó el colapso de la iniciativa en 2013, y las maquinarias pesadas comenzaron a ingresar al parque para abrir plataformas y pozos extractivos.",
                "Fue entonces cuando surgió una resistencia ciudadana sin precedentes. Jóvenes estudiantes, líderes indígenas y activistas ecologistas conformaron el colectivo Yasunidos y se lanzaron a las calles de todo el país armados únicamente con carpetas de firmas y megáfonos. Su objetivo era activar el mecanismo constitucional de la consulta popular para que fuera el pueblo ecuatoriano en las urnas quien decidiera el destino de la selva. Durante diez largos años, enfrentando trabas burocráticas, descalificaciones de firmas y dilaciones judiciales, el colectivo perseveró hasta que la Corte Constitucional validó finalmente la consulta popular.",
                "El 20 de agosto de 2023, junto a las elecciones presidenciales generales, los ecuatorianos se pronunciaron sobre una pregunta concisa y trascendental: «¿Está usted de acuerdo en que el gobierno ecuatoriano mantenga el crudo del ITT, conocido como bloque 43, indefinidamente en el subsuelo?». Los pronósticos de las consultoras económicas auguraban que el temor a la pérdida de ingresos fiscales inclinaría la balanza a favor del petróleo. Pero el resultado sorprendió al planeta: casi el sesenta por ciento de los votantes marcó con convicción la casilla del «Sí».",
                "Aquella jornada electoral histórica convirtió al Ecuador en el primer país del mundo que votó democráticamente en las urnas a favor de desmantelar pozos petroleros existentes para salvar la selva y la vida de los pueblos en aislamiento voluntario. En las comunidades waorani a orillas del río Yasuní, las familias celebraron el fallo cantando en su idioma milenario. La victoria de Yasuní demostró que frente al cinismo de la crisis climática global, la soberanía democrática de los pueblos puede desafiar la inercia del extractivismo para elegir la vida como el bien supremo de nuestro tiempo."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singularidad biológica documentada distingue al Parque Nacional Yasuní a escala mundial?",
                        "options": [
                            "Posee la mayor densidad biológica del planeta, con más de 650 especies de árboles en una sola hectárea.",
                            "Es el desierto de arena más árido de América del Sur sin presencia de fauna nativa.",
                            "Alberga las mayores plantaciones comerciales de trigo y cebada del trópico.",
                            "Es una isla marina aislada donde solo habitan pingüinos emperador."
                        ],
                        "correctIndex": 0,
                        "explanation": "Yasuní es reconocido por la ciencia como el punto con mayor concentración de biodiversidad del planeta por hectárea."
                    },
                    {
                        "question": "¿En qué consistía la propuesta original de la Iniciativa Yasuní-ITT planteada en 2007?",
                        "options": [
                            "Dejar el crudo bajo tierra a cambio de que la comunidad internacional compensara la mitad de los fondos fiscales previstos.",
                            "Exportar todo el crudo a los países vecinos a cambio de maquinaria industrial pesada.",
                            "Permitir la tala selectiva de árboles madereros para financiar la construcción de hidroeléctricas.",
                            "Trasladar forzosamente a los clanes indígenas Tagaeri y Taromenane hacia la costa."
                        ],
                        "correctIndex": 0,
                        "explanation": "La iniciativa pionera proponía no extraer los 850 millones de barriles si la comunidad global aportaba compensaciones ecológicas."
                    },
                    {
                        "question": "¿Cuál fue el veredicto democrático de la consulta popular nacional celebrada el 20 de agosto de 2023?",
                        "options": [
                            "Casi el 60% votó a favor de mantener el petróleo del bloque ITT indefinidamente en el subsuelo.",
                            "Se aprobó por unanimidad duplicar la perforación de pozos en toda la Reserva de la Biosfera.",
                            "Los votantes decidieron privatizar el parque y entregarlo a una corporación internacional.",
                            "Se declaró nula la votación por falta de participación ciudadana en las urnas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El pueblo ecuatoriano aprobó por amplia mayoría (59%) mantener el crudo bajo tierra y desmantelar la explotación en el bloque ITT."
                    }
                ]
            }
        }
    }

    # Story 6: Capstone regional story: Ecuador cuatro mundos
    story_ecuador_capstone = {
        "id": "b2-ecuador-consolidation",
        "title": "Ecuador: La síntesis viva de los cuatro mundos",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis integral de los Estudios Regionales sobre el Ecuador contemporáneo: la convivencia en un territorio compacto de la Costa marina, la Sierra volcánica, la Amazonía megadiversa y las Islas Galápagos; la solidez organizativa del movimiento indígena plurinacional, el vanguardismo de los Derechos de la Naturaleza y el liderazgo ético en la conservación planetaria.",
        "characters": [
            "Manuela Sáenz",
            "Eugenio Espejo",
            "Rosa Elena Lema",
            "Gabriel Cárdenas"
        ],
        "narration": {
            "paragraphs": [
                "En el mapa del continente suramericano, la silueta del Ecuador ocupa una extensión territorial aparentemente modesta encajada entre las gigantescas masas geográficas de Colombia, Perú y la inmensidad del océano Pacífico. Sin embargo, detrás de esa escala compacta se esconde una prodigiosa condensación de vida, historia y diversidad cultural que no encuentra paralelo en ningún otro rincón del planeta. Con justicia geográfica indiscutible, el país es celebrado en el mundo como 'el país de los cuatro mundos': la Costa del litoral marítimo y los manglares fértiles, la Sierra de los volcanes y los páramos sagrados, la Amazonía de los ríos caudalosos y la selva profunda, y el archipiélago insular de Galápagos.",
                "En pocas horas de viaje terrestre, un viajero puede desayunar en los puertos tropicales de Guayaquil rodeado de plantaciones de cacao fino de aroma y camarón, ascender al mediodía entre las cumbres nevadas del Chimborazo y los conventos barrocos de Quito a casi tres mil metros de altitud, y descender al caer la tarde hacia las cascadas rumorosas de Puyo y las selvas vírgenes del río Pastaza. Esta cercanía vertiginosa de ecosistemas extremos ha forjado un carácter nacional profundamente polifónico, donde la riqueza reside en la articulación de contrastes que dialogan permanentemente entre sí.",
                "En la Sierra andina, el latido identitario está marcado por la resistencia milenaria de los pueblos Kichwa. A través de la CONAIE y de la práctica cotidiana de la minga comunitaria, el movimiento indígena demostró al continente que la dignidad no se suplica, sino que se construye con organización colectiva y claridad ideológica. Al conquistar el reconocimiento del Estado Plurinacional en la Constitución de Montecristi de 2008, Ecuador rompió con la ficción del Estado criollo monocultural para abrazar con orgullo sus catorce nacionalidades y dieciocho pueblos ancestrales, garantizando que el Kichwa y el Shuar convivan como idiomas de relación intercultural junto al castellano.",
                "Esa misma sabiduría ancestral fecundó la mayor aportación ecuatoriana a la jurisprudencia universal: la consagración de la Pachamama o Naturaleza como sujeto de derechos inalienables. Al fundar su ordenamiento legal en el principio del Sumak Kawsay —la búsqueda del Buen Vivir en equilibrio armónico con la comunidad y el entorno natural—, el país demostró que el derecho no puede limitarse a legitimar la mercantilización de los recursos ecológicos. Los fallos judiciales que protegieron al río Vilcabamba o frenaron la minería en el Bosque Protector Los Cedros son hoy referencias doctrinales estudiadas en las facultades de derecho de los cinco continentes.",
                "Hacia el oriente amazónico, el Parque Nacional Yasuní se consagró como el bastión supremo de la ética planetaria contemporánea. En sus bosques, donde una sola hectárea reúne más diversidad botánica que continentes enteros, habitan los pueblos Tagaeri y Taromenane en aislamiento voluntario, custodiando un modo de vida que desconoce la codicia del petróleo y la voracidad industrial. La histórica consulta popular de 2023, en la que casi el sesenta por ciento de la ciudadanía nacional votó para dejar el crudo del bloque ITT indefinidamente en el subsuelo, fijó un hito democrático universal de coraje ecológico.",
                "En las aguas oceánicas del archipiélago de Galápagos, la ciencia y la conservación continúan rindiendo homenaje a la teoría evolutiva que Charles Darwin comenzó a vislumbrar entre pinzones e iguanas buceadoras en 1835. Con la creación de la reserva marina Hermandad en 2022, el Ecuador extendió sus brazos marítimos hacia las islas de Costa Rica y Colombia, blindando el gran corredor biológico por donde nadan libres miles de tiburones martillo, tortugas marinas y ballenas jorobadas.",
                "Al contemplar la trayectoria contemporánea del Ecuador, se descubre una nación que supo transformar su fragilidad geográfica en una lección moral de esperanza para la humanidad entera. En la mitad del mundo, donde la latitud cero anula las sombras en el mediodía equinoccial, el pueblo ecuatoriano sigue enseñando que es posible imaginar un porvenir donde la justicia social, el respeto plurinacional entre las culturas y la veneración sagrada por la madre tierra sean los cimientos inquebrantables de una vida digna y plena."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuáles son las cuatro regiones geográficas que fundamentan la denominación de Ecuador como 'el país de los cuatro mundos'?",
                        "options": [
                            "La Costa litoral, la Sierra andina, el Oriente amazónico y las Islas Galápagos.",
                            "La Pampa cerealera, la Patagonia helada, el Altiplano y la Puna.",
                            "El Chaco boreal, el Pantanal pantanoso, el Cerrado y la Mata Atlántica.",
                            "La Península ibérica, las Islas Baleares, las Canarias y Ceuta."
                        ],
                        "correctIndex": 0,
                        "explanation": "Ecuador reúne cuatro mundos claramente diferenciados: la Costa, la Sierra andina, la Amazonía y el archipiélago de Galápagos."
                    },
                    {
                        "question": "¿Qué principio filosófico andino orienta la concepción ecuatoriana del Buen Vivir consagrado en la Constitución?",
                        "options": [
                            "El Sumak Kawsay, que promueve la vida armónica entre los seres humanos y la naturaleza frente a la acumulación material.",
                            "La doctrina de la industrialización sustitutiva de importaciones a gran escala.",
                            "El positivismo jurídico que subordina el medio ambiente al desarrollo industrial.",
                            "La economía de libre mercado desregulada basada en la privatización de tierras comunitarias."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Sumak Kawsay (Buen Vivir) es la filosofía que busca la convivencia equitativa y la armonía entre comunidades y la biosfera."
                    },
                    {
                        "question": "¿Cuál es el significado global del referéndum de 2023 sobre el crudo de Yasuní-ITT en la política climática contemporánea?",
                        "options": [
                            "Demostró que una sociedad puede decidir democráticamente suspender la extracción petrolera para salvar la biodiversidad y pueblos aislados.",
                            "Obligó al país a construir refinerías petroleras en las playas de Galápagos.",
                            "Canceló todos los tratados ambientales suscritos con las Naciones Unidas.",
                            "Permitió la venta de reservas naturales a consorcios privados internacionales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El referéndum sentó un precedente global histórico de una nación que votó democráticamente dejar el petróleo bajo tierra para proteger la selva."
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
    write_json(f"stories/classics/b2/{c_unit}.json", to_schema_story(story_core_17))
    # Regional lesson stories:
    write_json(f"stories/world/b2/{r1}.json", to_schema_story(story_ecuador_01))
    write_json(f"stories/world/b2/{r2}.json", to_schema_story(story_ecuador_02))
    write_json(f"stories/world/b2/{r3}.json", to_schema_story(story_ecuador_03))
    write_json(f"stories/world/b2/{r4}.json", to_schema_story(story_ecuador_04))
    write_json(f"stories/world/b2/{r5}.json", to_schema_story(story_ecuador_05))
    write_json(f"stories/world/b2/{r6_con}.json", to_schema_story(story_ecuador_capstone))
    write_json(f"stories/world/b2/{r_unit}.json", to_schema_story(story_ecuador_capstone))

    # -------------------------------------------------------------------------
    # 5. LESSON FILES (6 Core + 6 Regional)
    # -------------------------------------------------------------------------
    core_lessons_info = [
        ("b2-17-01", "lesson.b2.17.01", "El estilo indirecto con verbo principal en pasado: traslación de asertos",
         "Master the backshifting of statements from direct to indirect discourse with past reporting verbs.",
         "el estilo indirecto con verbo principal en pasado: traslación temporal de asertos",
         ["Apply systematic tense backshifting to statements in past reporting frames.", "Recognize invariable tenses like the imperfect and pluperfect in reported speech.", "Distinguish between direct speech assertion and indirect reported perspective."]),
        ("b2-17-02", "lesson.b2.17.02", "Preguntas indirectas y traslación interrogativa en pasado",
         "Report yes/no questions and information questions in past frames using 'si' and interrogative pronouns.",
         "interrogativas indirectas totales y parciales con verbos introductorios en pasado",
         ["Transform direct yes/no questions into indirect clauses using 'si'.", "Report wh-questions preserving diacritic accent marks on interrogative pronouns.", "Synthesize judicial, diplomatic, and investigative inquiries in formal past frames."]),
        ("b2-17-03", "lesson.b2.17.03", "Órdenes, ruegos y peticiones referidas: del imperativo al subjuntivo",
         "Report direct commands, requests, and prohibitions by shifting imperatives to the imperfect subjunctive.",
         "estilo indirecto de mandatos y peticiones con verbo en pasado y pretérito imperfecto de subjuntivo",
         ["Transform imperative commands into subordinate clauses with the imperfect subjunctive.", "Differentiate between reporting information (indicative) and reporting commands (subjunctive).", "Formulate formal institutional directives and legal injunctions in reported speech."]),
        ("b2-17-04", "lesson.b2.17.04", "Traslación de deícticos temporales, espaciales y demostrativos",
         "Systematically shift temporal, spatial, and demonstrative deictic markers in past reported speech frames.",
         "traslación deíctica temporal y espacial en el discurso referido",
         ["Shift temporal deictics from proximity to distance (hoy -> ese día, ayer -> el día anterior).", "Shift spatial adverbs (aquí -> allí) and demonstratives (este -> aquel).", "Determine whether deictic adaptation is required based on the persistence of the temporal frame."]),
        ("b2-17-05", "lesson.b2.17.05", "El discurso indirecto libre en la prosa narrativa hispanoamericana",
         "Analyze and deploy free indirect discourse in literary narratives, blending narrator voice and character consciousness.",
         "el discurso indirecto libre en la prosa narrativa hispanoamericana",
         ["Identify the absence of reporting verbs and subordinating conjunctions in free indirect style.", "Analyze the emotional and existential focalization achieved in Latin American social realism.", "Recognize subjective past interrogatives and exclamations in third-person narrative prose."])
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
        "id": "lesson.b2.17.consolidation",
        "title": "Consolidación B2: El discurso referido y Huasipungo",
        "level": "B2",
        "goal": "Synthesize reported speech backshifting, indirect questions, requests, and free indirect discourse through Jorge Icaza's indigenist classic Huasipungo.",
        "grammar": "síntesis del discurso referido en el pasado y adaptación literaria de Huasipungo",
        "sections": [
            {"type": "goal", "items": [
                "Master temporal backshifting of statements, questions, and commands in past narrative frames.",
                "Shift temporal and spatial deictic markers accurately according to narrative perspective.",
                "Analyze social and indigenous struggles in the Ecuadorian Andes through literary indigenism."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{l6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Domino la traslación temporal de asertos en estilo indirecto con verbo principal en pasado.",
                "Formulo interrogativas indirectas totales y parciales con tildes diacríticas correctas.",
                "Transformo mandatos e imperativos en cláusulas con pretérito imperfecto de subjuntivo.",
                "Reconozco el discurso indirecto libre en la prosa narrativa andina y latinoamericana."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-ecuador-01", "lesson.b2.ecuador.01", "La avenida de los volcanes y el callejón interandino",
         "Explore the volcanic geography of the Ecuadorian Andes, Humboldt's exploration of Chimborazo, and colonial Quito and Cuenca.",
         "geomorfología volcánica del callejón interandino, pisos ecológicos y ciudades patrimoniales",
         ["Trace the volcanic corridor between the Western and Eastern cordilleras.", "Analyze the physical geography of Chimborazo, Cotopaxi, and the water-sponge role of the paramos.", "Deploy volcanic, geomorphological, and heritage vocabulary (nevado, callejón, glaciar, estratovolcán)."]),
        ("b2-ecuador-02", "lesson.b2.ecuador.02", "El archipiélago de Galápagos: Laboratorio de la evolución",
         "Investigate the unique evolutionary adaptations of Galapagos wildlife, Charles Darwin's historic visit, and oceanic marine reserves.",
         "biogeografía insular, especiación por selección natural y reservas marinas oceánicas",
         ["Examine the unique adaptations of marine iguanas, giant tortoises, and Darwin's finches.", "Analyze the convergence of oceanic currents (Humboldt, Panama, Cromwell).", "Deploy evolutionary biology and marine conservation vocabulary (endemismo, especiación, arrecife, santuario)."]),
        ("b2-ecuador-03", "lesson.b2.ecuador.03", "La CONAIE y la fuerza histórica del movimiento indígena",
         "Examine the political rise of the indigenous movement in Ecuador, the 1990 nationwide uprising, and the Pachakutik movement.",
         "sociología del movimiento indígena, Estado Plurinacional y democracia intercultural",
         ["Analyze the historic 1990 Inti Raymi indigenous uprising and its transformative national impact.", "Examine the foundation and parliamentary role of the Pachakutik political movement.", "Deploy indigenous politics and plurinational vocabulary (levantamiento, plurinacional, nacionalidad, comunero)."]),
        ("b2-ecuador-04", "lesson.b2.ecuador.04", "La Constitución de Montecristi: Pachamama y Derechos de la Naturaleza",
         "Explore the groundbreaking 2008 Montecristi Constitution recognizing Nature as a legal subject under the Sumak Kawsay principle.",
         "derechos de la naturaleza, constitucionalismo biocéntrico y filosofía del Sumak Kawsay",
         ["Analyze the historic constitutional recognition of Pachamama as a rights-bearing subject.", "Examine the biocentric legal doctrine and landmark court rulings (Vilcabamba, Los Cedros).", "Deploy constitutional jurisprudence and ecological ethics vocabulary (biocéntrico, jurisprudencia, regeneración, tutela)."]),
        ("b2-ecuador-05", "lesson.b2.ecuador.05", "El petróleo amazónico, Yasuní-ITT y la consulta popular",
         "Examine the biodiversity of Yasuni National Park, uncontacted peoples (Tagaeri/Taromenane), and the landmark 2023 popular referendum.",
         "ecología política amazónica, pueblos en aislamiento voluntario y democracia ambiental directa",
         ["Analyze Yasuni's extraordinary global biodiversity and the threats of oil exploitation.", "Reflect on the constitutional protection of clans in voluntary isolation (Tagaeri and Taromenane).", "Deploy Amazonian conservation, extractivism, and referendum vocabulary (intangible, aislamiento, biodiversidad, yacimiento)."])
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
        "id": "lesson.b2.ecuador.consolidation",
        "title": "Consolidación Regional: Ecuador, la síntesis de los cuatro mundos",
        "level": "B2",
        "goal": "Consolidate regional studies on Ecuador's four worlds, Andean volcanoes, Galapagos evolution, indigenous plurinationalism, and biocentric jurisprudence.",
        "grammar": "síntesis de estudios regionales ecuatorianos: volcanes, Galápagos, CONAIE y Derechos de la Naturaleza",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize the ecological diversity across Costa, Sierra, Amazonia, and Galapagos.",
                "Analyze the historical leadership of the indigenous movement and the constitutional vanguard of Sumak Kawsay.",
                "Appreciate Ecuador's pioneering democratic precedent in leaving crude underground in Yasuni."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r6_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{r6_con}-ex.json", "exerciseRefs": [f"{r6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Reconozco la geomorfología de la Avenida de los Volcanes y el valor hídrico de los páramos.",
                "Comprendo la importancia de Galápagos en la formulación de la teoría de la evolución.",
                "Valoro las conquistas sociales y políticas de la CONAIE y el modelo de Estado Plurinacional.",
                "Explico el concepto de los Derechos de la Naturaleza consagrado en la Constitución de Montecristi."
            ]}
        ]
    })

    print("Completed LatAm Unit 17 (Ecuador) generation!")

    # -------------------------------------------------------------------------
    # 6. UPDATE CURRICULUM UNITS (b2.json)
    # -------------------------------------------------------------------------
    b2_units_path = LATAM_DIR / "curriculum" / "units" / "b2.json"
    b2_units = json.loads(b2_units_path.read_text(encoding="utf-8"))
    
    # Check if Unit 17 entries already exist
    has_core_17 = any(u.get("title") == "Reported Speech in Past Frames" for u in b2_units)
    has_reg_17 = any(u.get("title") == "Ecuador: Plurinationalism, The Equatorial Andes & The Galápagos" for u in b2_units)
    
    if not has_core_17:
        b2_units.append({
            "title": "Reported Speech in Past Frames",
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
    if not has_reg_17:
        b2_units.append({
            "title": "Ecuador: Plurinationalism, The Equatorial Andes & The Galápagos",
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
    print("Updated curriculum/units/b2.json with Unit 17!")

    # -------------------------------------------------------------------------
    # 7. Word Count Audit for Stories
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_17", story_core_17),
        ("story_ecuador_01", story_ecuador_01),
        ("story_ecuador_02", story_ecuador_02),
        ("story_ecuador_03", story_ecuador_03),
        ("story_ecuador_04", story_ecuador_04),
        ("story_ecuador_05", story_ecuador_05),
        ("story_ecuador_capstone", story_ecuador_capstone)
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
