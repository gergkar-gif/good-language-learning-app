"""
Generate Latin American Spanish (es-latam) B2 Unit 15:
- Core Unit 15: b2-15 (The Imperfect Subjunctive: Forms & Nuances)
  Classic Literature: Rómulo Gallegos - Doña Bárbara
- Regional Unit 15: b2-venezuelapetroleo (Venezuela I: The Oil Century, Modernism & Caracas)
  Lessons:
    1. La cordillera de la Costa, El Ávila y el valle de Caracas
    2. El pozo Zumaque I, el Barroso II y el nacimiento del petroestado
    3. Carlos Raúl Villanueva y la Ciudad Universitaria de Caracas: Utopía moderna
    4. El cinetismo y las vanguardias plásticas: Cruz-Diez y Soto
    5. La bonanza petrolera y las ilusiones del 'Dakar' suramericano
    6. Consolidación: La modernidad petrolera
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def write_json(rel_path: str, data: dict):
    path = ROOT / "content" / "es-latam" / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {path.relative_to(ROOT)}")

def count_words(story: dict) -> int:
    return sum(len(p["text"].split()) for p in story.get("paragraphs", []))

def run():
    # ----------------------------------------------------
    # 1. Skill Registry & Grammar Titles Updates
    # ----------------------------------------------------
    reg_path = ROOT / "content" / "es-latam" / "indexes" / "skill-registry.json"
    with open(reg_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    skills_to_add = {
        "b2-15-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "core upper-intermediate imperfect subjunctive and discourse vocabulary"
        },
        "subjuntivo-imperfecto-ra-se": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "imperfect subjunctive morphological forms in ra and se"
        },
        "subjuntivo-imperfecto-registro": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "stylistic register contrast between ra and se forms"
        },
        "subjuntivo-imperfecto-cortesia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "polite courtesy requests with imperfect subjunctive forms"
        },
        "subjuntivo-imperfecto-hipotesis": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "retrospective hypotheses with imperfect subjunctive"
        },
        "subjuntivo-imperfecto-estilistico-ra": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "stylistic indicative use of ra form in formal prose"
        },
        "b2-venezuelapetroleo-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "venezuelan oil urbanism architecture and kinetic art vocabulary"
        },
        "venezuela-geografia-valle-avila": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "caracas valley geography coastal range and avila mountain"
        },
        "venezuela-petroleo-zumaque-petroestado": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "lake maracaibo oil discovery and the rentier petrostate"
        },
        "venezuela-arquitectura-villanueva-ucv": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "modernist architecture and villanueva synthesis in caracas"
        },
        "venezuela-arte-cinetico-cruzdiez-soto": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "kinetic art vanguardism and musical education in venezuela"
        },
        "venezuela-bonanza-petrolera-sociedad": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "oil boom consumerism and socioeconomic shifts in venezuela"
        }
    }

    for k, v in skills_to_add.items():
        registry["skills"][k] = v

    with open(reg_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated skill-registry.json for Unit 15")

    titles_path = ROOT / "content" / "es-latam" / "indexes" / "grammar-titles.json"
    with open(titles_path, "r", encoding="utf-8") as f:
        titles = json.load(f)

    titles_to_add = {
        "subjuntivo-imperfecto-ra-se": "imperfect subjunctive morphological forms in ra and se",
        "subjuntivo-imperfecto-registro": "stylistic register contrast between ra and se forms",
        "subjuntivo-imperfecto-cortesia": "polite courtesy requests with imperfect subjunctive forms",
        "subjuntivo-imperfecto-hipotesis": "retrospective hypotheses with imperfect subjunctive",
        "subjuntivo-imperfecto-estilistico-ra": "stylistic indicative use of ra form in formal prose",
        "venezuela-geografia-valle-avila": "caracas valley geography coastal range and avila mountain",
        "venezuela-petroleo-zumaque-petroestado": "lake maracaibo oil discovery and the rentier petrostate",
        "venezuela-arquitectura-villanueva-ucv": "modernist architecture and villanueva synthesis in caracas",
        "venezuela-arte-cinetico-cruzdiez-soto": "kinetic art vanguardism and musical education in venezuela",
        "venezuela-bonanza-petrolera-sociedad": "oil boom consumerism and socioeconomic shifts in venezuela"
    }

    for k, v in titles_to_add.items():
        titles[k] = v

    with open(titles_path, "w", encoding="utf-8") as f:
        json.dump(titles, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated grammar-titles.json for Unit 15")

    # ====================================================
    # 2. CORE UNIT 15 (b2-15)
    # ====================================================
    c_unit = "b2-15"

    # --- Lesson 1: b2-15-01 ---
    l1 = f"{c_unit}-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.15.01",
        "lesson": l1,
        "title": "Morfología verbal y desinencias del subjuntivo",
        "theme": "Léxico de lingüística histórica, desinencias verbales y paradigmas",
        "words": [
            {
                        "lemma": "desinencia",
                        "translation": "verb ending, inflectional suffix",
                        "pos": "noun"
            },
            {
                        "lemma": "etimológico",
                        "translation": "etymological",
                        "pos": "adjective"
            },
            {
                        "lemma": "pluscuamperfecto",
                        "translation": "pluperfect",
                        "pos": "noun"
            },
            {
                        "lemma": "alternancia",
                        "translation": "alternation, variation",
                        "pos": "noun"
            },
            {
                        "lemma": "paradigma",
                        "translation": "inflectional model, paradigm",
                        "pos": "noun"
            },
            {
                        "lemma": "homogéneo",
                        "translation": "homogeneous",
                        "pos": "adjective"
            }
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.15.01.subjuntivo-imperfecto-ra-se",
        "title": "Las dos desinencias del imperfecto de subjuntivo: -ra y -se",
        "sections": [
            {
                "type": "text",
                "content": "El español dispone de dos paradigmas morfológicos plenamente válidos para conjugar el imperfecto de subjuntivo: las formas terminadas en **-ra** (*cantara, comiera, viviera*) y las terminadas en **-se** (*cantase, comiese, viviese*). Ambas desinencias proceden históricamente de tiempos latinos distintos: la forma en *-ra* deriva del pluscuamperfecto de indicativo latino (*amaveram*), mientras que la forma en *-se* proviene del pluscuamperfecto de subjuntivo latino (*amavissem*). En la inmensa mayoría de los contextos subordinados actuales, ambas formas son gramaticalmente intercambiables y equivalentes en significado."
            },
            {
                "type": "table",
                "title": "Conjugación comparativa de -ra y -se",
                "rows": [
                    ["yo cantara / cantase", "I sang / were to sing"],
                    ["tú cantaras / cantases", "you sang / were to sing"],
                    ["él/ella hablara / hablase", "he/she spoke / were to speak"],
                    ["nosotros comiéramos / comiésemos", "we ate / were to eat"],
                    ["ustedes vivieran / viviesen", "you all lived / were to live"],
                    ["ellos durmieran / durmiesen", "they slept / were to sleep"]
                ]
            },
            {
                "type": "tip",
                "content": "Ambas formas parten siempre de la tercera persona plural del pretérito indefinido: de *hablaron* se elimina *-ron* para obtener la raíz *habla-*, a la que se añaden las desinencias *-ra/-ras/-ra/-ramos/-ran* o *-se/-ses/-se/-semos/-sen*. Recuerda que la primera persona del plural siempre lleva tilde en la vocal temática: *cantáramos*, *tuviésemos*."
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
                    ["desinencia", "inflectional verb ending"],
                    ["etimológico", "etymological"],
                    ["alternancia", "alternation"],
                    ["paradigma", "inflectional model"]
                ],
                "teaches": ["b2-15-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El profesor dudaba de que los estudiantes __ el texto a tiempo. (terminar)",
                "answer": "terminaran",
                "english": "The professor doubted that the students would finish the text on time.",
                "teaches": ["subjuntivo-imperfecto-ra-se"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es el origen etimológico de la desinencia verbal en -ra?",
                "options": [
                    "Proviene del pluscuamperfecto de indicativo del latín.",
                    "Deriva del futuro imperfecto del griego clásico.",
                    "Surgió como una invención dialectal del siglo XVIII.",
                    "Procede exclusivamente del imperativo plural visigodo."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-ra-se"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "era", "probable", "que", "ellos", "viniesen", "a", "la", "reunión."],
                "solution": ["No", "era", "probable", "que", "ellos", "viniesen", "a", "la", "reunión."],
                "english": "It was not likely that they would come to the meeting.",
                "teaches": ["subjuntivo-imperfecto-ra-se"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Valentina", "text": "¿Esperabas que el embajador hablara hoy sobre el acuerdo comercial?"},
                    {"speaker": "Mateo", "text": "_____"}
                ],
                "options": [
                    "Sí, todos deseábamos que hablase con total franqueza sobre los aranceles.",
                    "No, el embajador siempre habla en presente de indicativo.",
                    "Creo que el acuerdo se firma mañana sin ninguna duda.",
                    "Ayer compramos los boletos de avión para Caracas."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-ra-se"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aunque tuviéramos discrepancias metodológicas, acordamos redactar el dictamen de común acuerdo.",
                "english": "Even if we had methodological discrepancies, we agreed to draft the ruling by mutual agreement.",
                "teaches": ["subjuntivo-imperfecto-ra-se"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", {
        "id": "lesson.b2.15.01",
        "title": "Las dos formas del imperfecto de subjuntivo: -ra y -se",
        "level": "B2",
        "goal": "Master the morphological distinction, historical origins, and equivalence between the -ra and -se forms of the imperfect subjunctive.",
        "grammar": "morfología comparada del imperfecto de subjuntivo en -ra y -se",
        "sections": [
            {"type": "goal", "items": [
                "Conjugate regular and irregular verbs in both -ra and -se imperfect subjunctive.",
                "Understand the historical derivation from Latin pluperfect tenses.",
                "Apply correct accentuation in the first-person plural forms."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l1}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l1}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{l1}-ex.json", "exerciseRefs": [f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{l1}-ex.json", "exerciseRefs": [f"{l1}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{l1}-ex.json", "exerciseRefs": [f"{l1}.ex06"]}
        ]
    })

    # --- Lesson 2: b2-15-02 ---
    l2 = f"{c_unit}-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.15.02",
        "lesson": l2,
        "title": "Registros estilísticos y sociolingüística",
        "theme": "Léxico de registros comunicativos, formalidad y uso protocolar",
        "words": [
            {
                        "lemma": "coloquial",
                        "translation": "colloquial, everyday",
                        "pos": "adjective"
            },
            {
                        "lemma": "arcaizante",
                        "translation": "archaizing, archaic in tone",
                        "pos": "adjective"
            },
            {
                        "lemma": "protocolar",
                        "translation": "protocolary, formal",
                        "pos": "adjective"
            },
            {
                        "lemma": "predominio",
                        "translation": "predominance, prevalence",
                        "pos": "noun"
            },
            {
                        "lemma": "forense",
                        "translation": "forensic, judicial legal",
                        "pos": "adjective"
            },
            {
                        "lemma": "frecuencia",
                        "translation": "frequency",
                        "pos": "noun"
            }
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.15.02.subjuntivo-imperfecto-registro",
        "title": "Contraste de registro estilístico entre -ra y -se",
        "sections": [
            {
                "type": "text",
                "content": "Aunque ambas variantes son intercambiables en gramática descriptiva, su distribución estilística y geográfica presenta notorias divergencias en el mundo hispanohablante. En toda América Latina, la variante en **-ra** ostenta un predominio casi hegemónico (más del 95% de las ocurrencias tanto en el habla oral coloquial como en la prensa escrita y la literatura). Por el contrario, la forma en **-se** ha quedado relegada a registros sumamente formales, textos jurídicos, actas notariales, prosa académica o discursos solemnes."
            },
            {
                "type": "table",
                "title": "Distribución sociolingüística y de registro",
                "rows": [
                    ["quisiera un café (oral)", "I would like a coffee (natural, widespread)"],
                    ["quisiese expresar mi gratitud (protocolar)", "I would wish to express my gratitude (solemn)"],
                    ["si tuviera tiempo iría (LatAm estándar)", "if I had time I would go (predominant in LatAm)"],
                    ["en caso de que compareciese (jurídico)", "in case he/she were to appear (legal statute)"],
                    ["como si no supiera nada (común)", "as if he didn't know anything (spontaneous standard)"],
                    ["a menos que sobreviniese un fallo (académico)", "unless a ruling were to supervene (formal analysis)"]
                ]
            },
            {
                "type": "tip",
                "content": "Para desenvolverte con naturalidad en el español de América Latina, utiliza sistemáticamente las formas en *-ra* en tus conversaciones y redacciones cotidianas. Reserva *-se* para cuando desees dotar a tu texto de una solemnidad especial, un matiz arcaizante deliberado o un tono forense muy estricto."
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
                    ["coloquial", "everyday / informal"],
                    ["arcaizante", "archaizing in tone"],
                    ["protocolar", "formal protocol"],
                    ["predominio", "prevalence / predominance"]
                ],
                "teaches": ["b2-15-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En el español americano habitual, resulta mucho más natural decir: 'Ojalá __ tiempo libre mañana'. (tener)",
                "answer": "tuviera",
                "english": "In standard American Spanish, it is much more natural to say: 'I wish I had free time tomorrow'.",
                "teaches": ["subjuntivo-imperfecto-registro"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿En qué tipo de textos suele encontrarse con mayor frecuencia la variante en -se en América Latina?",
                "options": [
                    "En documentos jurídicos notariales, textos académicos formales y discursos solemnes.",
                    "En conversaciones informales entre jóvenes universitarios.",
                    "En mensajes de texto rápidos y redes sociales cotidianas.",
                    "Únicamente en manuales técnicos de cocina tradicional."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-registro"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "variante", "en", "-ra", "predomina", "en", "el", "español", "hispanoamericano."],
                "solution": ["La", "variante", "en", "-ra", "predomina", "en", "el", "español", "hispanoamericano."],
                "english": "The variant in -ra predominates in Spanish American Spanish.",
                "teaches": ["subjuntivo-imperfecto-registro"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Abogado Pérez", "text": "He redactado la cláusula estipulando que en caso de que surgiese algún diferendo se recurra al arbitraje."},
                    {"speaker": "Colega", "text": "_____"}
                ],
                "options": [
                    "Es impecable; ese uso de la desinencia en -se confiere al contrato un rigor jurídico intachable.",
                    "No me gusta el café con azúcar por las mañanas.",
                    "Ayer fuimos al cine a ver una película de acción.",
                    "Las desinencias en -ra son incorrectas según la ley."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-registro"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aunque ambas formas sean correctas, la prensa latinoamericana prefiere de manera uniforme la terminación en -ra.",
                "english": "Even though both forms are correct, Latin American press uniformly prefers the termination in -ra.",
                "teaches": ["subjuntivo-imperfecto-registro"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", {
        "id": "lesson.b2.15.02",
        "title": "Contraste de registro estilístico entre -ra y -se",
        "level": "B2",
        "goal": "Analyze sociolinguistic frequency and stylistic distribution: overwhelming preference for -ra in Latin America versus judicial/protocolar uses of -se.",
        "grammar": "distribución de registro y frecuencia dialectal de -ra y -se en el mundo hispánico",
        "sections": [
            {"type": "goal", "items": [
                "Distinguish natural Latin American spoken standard (-ra) from high-formal written register (-se).",
                "Identify -se in judicial statutes, academic prose, and solemn declarations.",
                "Choose the appropriate form based on communicative context and genre."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l2}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l2}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{l2}-ex.json", "exerciseRefs": [f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{l2}-ex.json", "exerciseRefs": [f"{l2}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{l2}-ex.json", "exerciseRefs": [f"{l2}.ex06"]}
        ]
    })

    # --- Lesson 3: b2-15-03 ---
    l3 = f"{c_unit}-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.15.03",
        "lesson": l3,
        "title": "Cortesía pragmática y diplomacia",
        "theme": "Léxico de atenuación, deferencia y fórmulas de cortesía",
        "words": [
            {
                        "lemma": "cortesía",
                        "translation": "courtesy, politeness",
                        "pos": "noun"
            },
            {
                        "lemma": "atenuación",
                        "translation": "mitigation, softening of tone",
                        "pos": "noun"
            },
            {
                        "lemma": "imperativo",
                        "translation": "imperative, command",
                        "pos": "noun"
            },
            {
                        "lemma": "petición",
                        "translation": "request, petition",
                        "pos": "noun"
            },
            {
                        "lemma": "diplomático",
                        "translation": "diplomatic, tactful",
                        "pos": "adjective"
            },
            {
                        "lemma": "deferencia",
                        "translation": "deference, respectful regard",
                        "pos": "noun"
            }
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.15.03.subjuntivo-imperfecto-cortesia",
        "title": "Fórmulas de cortesía y atenuación con imperfecto de subjuntivo",
        "sections": [
            {
                "type": "text",
                "content": "Uno de los usos independientes más distinguidos del imperfecto de subjuntivo en español es la expresión de **cortesía pragmática y atenuación**. Tres verbos modales específicos —**querer**, **deber** y **poder**— se emplean en imperfecto de subjuntivo (*quisiera*, *debiera*, *pudiera*) en oraciones principales para suavizar peticiones, consejos o sugerencias, sustituyendo ventajosamente al condicional simple (*querría, debería, podría*)."
            },
            {
                "type": "table",
                "title": "Formulaciones atenuadas de cortesía",
                "rows": [
                    ["Quisiera consultar una duda.", "I would like to ask a question."],
                    ["¿Pudiera usted indicarme la oficina?", "Could you show me the office?"],
                    ["Debiéramos considerar otra opción.", "We ought to consider another option."],
                    ["Quisiéramos agradecer su amable atención.", "We would like to thank your kind attention."],
                    ["¿Pudieras prestarme ese informe?", "Could you lend me that report?"],
                    ["No debieras precipitar tu dictamen.", "You ought not to rush your ruling."]
                ]
            },
            {
                "type": "tip",
                "content": "Ten presente una asimetría modal fundamental: en este uso atenuado de cortesía en cláusulas independientes, **únicamente se admite la forma en -ra** (*quisiera, debiera, pudiera*). Las formas en *-se* (*quisiese, debiese, pudiese*) resultan agramaticales o arcaicas en función de petición directa independiente (*'Quisiera un favor'*, nunca *'Quisiese un favor'*)."
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
                    ["cortesía", "politeness"],
                    ["atenuación", "mitigation / softening"],
                    ["petición", "formal request"],
                    ["deferencia", "respectful deference"]
                ],
                "teaches": ["b2-15-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Disculpe, señor Ministro, ¿__ usted concedernos diez minutos de su audiencia? (poder)",
                "answer": "pudiera",
                "english": "Excuse me, Mr. Minister, could you grant us ten minutes of your audience?",
                "teaches": ["subjuntivo-imperfecto-cortesia"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué es incorrecto decir 'Quisiese un vaso de agua' para pedir algo con cortesía?",
                "options": [
                    "Porque en las oraciones independientes de cortesía modal solo es gramatical la desinencia en -ra.",
                    "Porque el verbo querer no admite subjuntivo bajo ninguna circunstancia.",
                    "Porque en español solo se puede pedir agua usando el imperativo.",
                    "Porque la forma debiese sustituye obligatoriamente a quisiese."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-cortesia"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Quisiéramos", "proponer", "una", "solución", "equitativa", "para", "ambas", "partes."],
                "solution": ["Quisiéramos", "proponer", "una", "solución", "equitativa", "para", "ambas", "partes."],
                "english": "We would like to propose an equitable solution for both parties.",
                "teaches": ["subjuntivo-imperfecto-cortesia"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Asistente", "text": "Buenos días, ¿en qué puedo colaborar con usted hoy?"},
                    {"speaker": "Investigador", "text": "_____"}
                ],
                "options": [
                    "Quisiera revisar los archivos históricos del siglo diecinueve correspondientes a la cancillería.",
                    "Quiero que me des todos los papeles ahora mismo sin dilación.",
                    "Ayer almorcé una sopa caliente en el comedor central.",
                    "Los archivos están cerrados durante todo el fin de semana."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-cortesia"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Debiéramos examinar con cautela las cláusulas contractuales antes de estampar la firma definitiva.",
                "english": "We ought to cautiously examine the contractual clauses before placing our definitive signature.",
                "teaches": ["subjuntivo-imperfecto-cortesia"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", {
        "id": "lesson.b2.15.03",
        "title": "Fórmulas de cortesía y atenuación con imperfecto de subjuntivo",
        "level": "B2",
        "goal": "Deploy modal imperfect subjunctive forms (quisiera, debiera, pudiera) in independent clauses to soften requests and express polite deference.",
        "grammar": "subjuntivo atenuador de cortesía con verbos modales en cláusulas independientes",
        "sections": [
            {"type": "goal", "items": [
                "Formulate diplomatic requests and inquiries using 'quisiera' and 'pudiera'.",
                "Offer mitigated advice or institutional suggestions with 'debiera'.",
                "Recognize the ungrammaticality of *-se* in direct independent courtesy formulas."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l3}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l3}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{l3}-ex.json", "exerciseRefs": [f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{l3}-ex.json", "exerciseRefs": [f"{l3}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{l3}-ex.json", "exerciseRefs": [f"{l3}.ex06"]}
        ]
    })

    # --- Lesson 4: b2-15-04 ---
    l4 = f"{c_unit}-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.15.04",
        "lesson": l4,
        "title": "Hipótesis irreales y conjeturas",
        "theme": "Léxico de análisis contrafáctico, simulación y verosimilitud",
        "words": [
            {
                        "lemma": "contrafáctico",
                        "translation": "counterfactual",
                        "pos": "adjective"
            },
            {
                        "lemma": "simulación",
                        "translation": "simulation, pretense",
                        "pos": "noun"
            },
            {
                        "lemma": "verosimilitud",
                        "translation": "verisimilitude, plausibility",
                        "pos": "noun"
            },
            {
                        "lemma": "conjetura",
                        "translation": "conjecture, reasoned guess",
                        "pos": "noun"
            },
            {
                        "lemma": "desiderativo",
                        "translation": "desiderative, expressing a wish",
                        "pos": "adjective"
            },
            {
                        "lemma": "anáfora",
                        "translation": "anaphora",
                        "pos": "noun"
            }
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.15.04.subjuntivo-imperfecto-hipotesis",
        "title": "Hipótesis irreales y deseos presentes con 'como si' y 'ojalá'",
        "sections": [
            {
                "type": "text",
                "content": "El imperfecto de subjuntivo es la forma obligada para expresar situaciones hipotéticas contrarias a la realidad presente o de difícil cumplimiento. Se manifiesta principalmente en dos estructuras modales cruciales de nivel B2:\n1. **Locución comparativa irreal 'como si'**: introduce siempre subjuntivo (*como si supiera, como si fuese*), denotando una equiparación ficticia que el hablante sabe que no se corresponde con los hechos.\n2. **Partícula desiderativa 'ojalá'**: seguida de imperfecto de subjuntivo (*¡ojalá tuviera!, ¡ojalá lloviese!*), formula un deseo sentido en el presente pero percibido como irrealizable o de bajísima probabilidad actual."
            },
            {
                "type": "table",
                "title": "Estructuras hipotéticas de irrealidad presente",
                "rows": [
                    ["Habla como si fuera el dueño del consorcio.", "He speaks as if he were the owner of the consortium."],
                    ["Camina como si no le doliese la pierna.", "She walks as if her leg didn't hurt."],
                    ["¡Ojalá tuviéramos mayores recursos fiscales!", "I wish we had greater fiscal resources!"],
                    ["Actúan como si conocieran el desenlace.", "They act as if they knew the outcome."],
                    ["¡Ojalá viviera más cerca de la universidad!", "I wish he lived closer to the university!"],
                    ["Me mira como si yo fuese un forastero.", "She looks at me as if I were a stranger."]
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que después de 'como si' **nunca** se utiliza el presente de subjuntivo ni el indicativo: decir *'habla como si tenga dinero'* o *'habla como si tiene dinero'* constituye un error grave en la norma culta. La correlación modal exige siempre imperfecto (para simultaneidad) o pluscuamperfecto (para anterioridad)."
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
                    ["contrafáctico", "counterfactual"],
                    ["simulación", "pretense / simulation"],
                    ["conjetura", "reasoned guess"],
                    ["desiderativo", "expressing a wish"]
                ],
                "teaches": ["b2-15-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El testigo declaró ante el juez con evasivas, como si no __ nada de lo ocurrido. (saber)",
                "answer": "supiera",
                "english": "The witness testified before the judge evasively, as if he knew nothing of what had happened.",
                "teaches": ["subjuntivo-imperfecto-hipotesis"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué tiempo verbal exige rigurosamente la locución comparativa 'como si' para indicar simultaneidad irreal?",
                "options": [
                    "El imperfecto de subjuntivo (en -ra o -se).",
                    "El presente de indicativo.",
                    "El futuro simple de indicativo.",
                    "El presente de subjuntivo obligatoriamente."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-hipotesis"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["¡Ojalá", "tuviéramos", "la", "certeza", "absoluta", "sobre", "el", "resultado!"],
                "solution": ["¡Ojalá", "tuviéramos", "la", "certeza", "absoluta", "sobre", "el", "resultado!"],
                "english": "I wish we had absolute certainty about the outcome!",
                "teaches": ["subjuntivo-imperfecto-hipotesis"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Mariana", "text": "¿Notaste cómo reaccionó Julián al enterarse de la auditoría externa?"},
                    {"speaker": "Camilo", "text": "_____"}
                ],
                "options": [
                    "Sí, se encogió de hombros y sonrió como si la medida no tuviese ninguna consecuencia para su equipo.",
                    "No conozco al nuevo director de la empresa auditora.",
                    "La auditoría comenzará el próximo lunes a primera hora.",
                    "Julián tiene un automóvil de color rojo oscuro."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-hipotesis"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "¡Ojalá encontráramos una vía diplomática que evitara mayores tensiones fronterizas entre ambas naciones!",
                "english": "I wish we found a diplomatic path that avoided further border tensions between both nations!",
                "teaches": ["subjuntivo-imperfecto-hipotesis"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", {
        "id": "lesson.b2.15.04",
        "title": "Hipótesis irreales y deseos presentes con 'como si' y 'ojalá'",
        "level": "B2",
        "goal": "Formulate counterfactual present hypotheses and low-probability wishes using 'como si' and 'ojalá' with imperfect subjunctive.",
        "grammar": "oraciones comparativas irreales (como si) y desiderativas presentes (ojalá)",
        "sections": [
            {"type": "goal", "items": [
                "Construct unreal comparisons with 'como si' + imperfect subjunctive.",
                "Express present unfulfilled wishes using 'ojalá' + imperfect subjunctive.",
                "Avoid indicative or present subjunctive errors following counterfactual triggers."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l4}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l4}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{l4}-ex.json", "exerciseRefs": [f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{l4}-ex.json", "exerciseRefs": [f"{l4}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{l4}-ex.json", "exerciseRefs": [f"{l4}.ex06"]}
        ]
    })

    # --- Lesson 5: b2-15-05 ---
    l5 = f"{c_unit}-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.15.05",
        "lesson": l5,
        "title": "Recursos estilísticos y prosa periodística",
        "theme": "Léxico de crítica estilística, cronística y redacción formal",
        "words": [
            {
                        "lemma": "estilístico",
                        "translation": "stylistic",
                        "pos": "adjective"
            },
            {
                        "lemma": "pretérito",
                        "translation": "past tense, preterite",
                        "pos": "noun"
            },
            {
                        "lemma": "periodístico",
                        "translation": "journalistic",
                        "pos": "adjective"
            },
            {
                        "lemma": "antedicho",
                        "translation": "aforementioned, said",
                        "pos": "adjective"
            },
            {
                        "lemma": "vestigio",
                        "translation": "vestige, historical trace",
                        "pos": "noun"
            },
            {
                        "lemma": "remanente",
                        "translation": "remnant, surviving trace",
                        "pos": "adjective"
            }
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.15.05.subjuntivo-imperfecto-estilistico-ra",
        "title": "El uso estilístico de -ra con valor de indicativo en la prosa formal",
        "sections": [
            {
                "type": "text",
                "content": "En la prosa periodística, ensayística y literaria formal del ámbito hispánico, es sumamente frecuente encontrar la forma en **-ra** empleada con valor de tiempo pretérito de indicativo (equivalente a *había sido*, *fue* o *había llegado*). Este fenómeno gramatical no es una incorrección caprichosa, sino un vestigio etimológico directo del latín clásico, donde la desinencia *-ra* correspondía originalmente al pluscuamperfecto de indicativo (*había amado*).\n\nAunque los manuales de estilo desaconsejan su proliferación indiscriminada en textos técnicos, su reconocimiento y apreciación estilística resultan indispensables para alcanzar la competencia lectora de nivel B2 en literatura y crónica política."
            },
            {
                "type": "table",
                "title": "Equivalencias del valor indicativo de -ra",
                "rows": [
                    ["el que fuera presidente del senado", "the one who was / had been president of the senate"],
                    ["la ley que aprobara el Congreso en 1999", "the law that Congress approved / had approved in 1999"],
                    ["el edificio donde naciera el ilustre poeta", "the building where the illustrious poet was born"],
                    ["el acuerdo al que llegaran los cancilleres", "the agreement that the chancellors had reached"],
                    ["la huelga que paralizara el transporte", "the strike that paralyzed / had paralyzed transit"],
                    ["según afirmara el portavoz gubernamental", "as the government spokesperson stated"]
                ]
            },
            {
                "type": "tip",
                "content": "Fíjate bien en la restricción morfológica: este valor de indicativo **solo lo posee la forma en -ra** (*fuera, naciera, aprobara*). Jamás se puede emplear la desinencia en *-se* con valor de indicativo (*'el que fuese presidente'* con valor afirmativo fáctico sería un error garrafal)."
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
                    ["estilístico", "stylistic"],
                    ["periodístico", "journalistic"],
                    ["antedicho", "aforementioned"],
                    ["vestigio", "historical trace / vestige"]
                ],
                "teaches": ["b2-15-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la crónica necrológica se recordó la figura del novelista que __ el Premio Nobel de Literatura. (obtener)",
                "answer": "obtuviera",
                "english": "In the obituary column, the figure of the novelist who had obtained the Nobel Prize for Literature was recalled.",
                "teaches": ["subjuntivo-imperfecto-estilistico-ra"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿A qué tiempo verbal equivale la frase periodística 'el acuerdo que rubricaran los mandatarios'?",
                "options": [
                    "A 'que habían rubricado' o 'que rubricaron' en modo indicativo.",
                    "A una orden imperativa futura e irrevocable.",
                    "A un deseo irrealizable e incierto en presente.",
                    "A una condición hipotética sin cumplir."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-estilistico-ra"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "ministro", "que", "asumiera", "el", "cargo", "renunció", "ayer."],
                "solution": ["El", "ministro", "que", "asumiera", "el", "cargo", "renunció", "ayer."],
                "english": "The minister who had assumed office resigned yesterday.",
                "teaches": ["subjuntivo-imperfecto-estilistico-ra"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Editor", "text": "¿Por qué el articulista escribió 'la reforma que promoviera el presidente' en lugar de 'promovió'?"},
                    {"speaker": "Corrector", "text": "_____"}
                ],
                "options": [
                    "Es un recurso estilístico formal muy extendido en el periodismo que evoca el antiguo valor etimológico de pluscuamperfecto de indicativo.",
                    "Se trata de un descuido tipográfico que debe corregirse de inmediato.",
                    "El presidente no quiso firmar la reforma porque no le gustaba.",
                    "En los artículos de opinión está prohibido conjugar los verbos en pasado."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-estilistico-ra"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La delegación visitó el palacio colonial donde residiera el primer gobernador republicano.",
                "english": "The delegation visited the colonial palace where the first republican governor had resided.",
                "teaches": ["subjuntivo-imperfecto-estilistico-ra"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", {
        "id": "lesson.b2.15.05",
        "title": "El uso estilístico de -ra con valor de indicativo en la prosa formal",
        "level": "B2",
        "goal": "Recognize and interpret the stylistic use of the -ra form with past indicative value in journalistic, historiographical, and literary prose.",
        "grammar": "uso estilístico etimológico de -ra con valor de pretérito o pluscuamperfecto de indicativo",
        "sections": [
            {"type": "goal", "items": [
                "Identify the etymological indicative value of -ra ('el que fuera presidente').",
                "Differentiate indicative -ra from true subjunctive modal subordinations.",
                "Understand why this stylistic feature is strictly restricted to the -ra variant."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l5}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l5}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{l5}-ex.json", "exerciseRefs": [f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{l5}-ex.json", "exerciseRefs": [f"{l5}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{l5}-ex.json", "exerciseRefs": [f"{l5}.ex06"]}
        ]
    })

    # --- Lesson 6: b2-15-consolidation ---
    l6_con = f"{c_unit}-consolidation"
    write_json(f"exercises/b2/{l6_con}-ex.json", {
        "lesson": l6_con,
        "exercises": [
            {
                "id": f"{l6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["desinencia", "verb inflectional ending"],
                    ["cortesía", "polite mitigation"],
                    ["contrafáctico", "counterfactual scenario"],
                    ["vestigio", "historical trace / remnant"]
                ],
                "teaches": ["b2-15-vocab"]
            },
            {
                "id": f"{l6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si el hacendado __ la ley con firmeza, la violencia en el llano habría cesado mucho antes. (aplicar)",
                "answer": "aplicara",
                "english": "If the rancher had applied the law with firmness, violence in the plains would have ceased much earlier.",
                "teaches": ["subjuntivo-imperfecto-ra-se"]
            },
            {
                "id": f"{l6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones formula una petición atenuada de cortesía de manera correcta?",
                "options": [
                    "Quisiera solicitar formalmente una prórroga para la entrega del informe.",
                    "Quisiese solicitar formalmente una prórroga para la entrega del informe.",
                    "Quiero que me des una prórroga inmediatamente.",
                    "Querría yo que tú quisieras darme una prórroga."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-cortesia"]
            },
            {
                "id": f"{l6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El protagonista cabalgaba por la sabana como si no __ ningún peligro en las ciénagas. (temer)",
                "answer": "temiera",
                "english": "The protagonist rode through the savanna as if he feared no danger in the marshes.",
                "teaches": ["subjuntivo-imperfecto-hipotesis"]
            },
            {
                "id": f"{l6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo distingue el uso de -ra con valor de indicativo en la prosa periodística?",
                "options": [
                    "Que equivale a un pretérito o pluscuamperfecto de indicativo y solo es posible con la desinencia en -ra.",
                    "Que expresa una orden imperativa que debe cumplirse en el futuro.",
                    "Que es una regla moderna inventada en los medios digitales de comunicación.",
                    "Que se puede reemplazar indistintamente por la desinencia en -se sin alterar la norma culta."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-estilistico-ra"]
            },
            {
                "id": f"{l6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Debiéramos", "fomentar", "el", "diálogo", "civilizado", "en", "todo", "el", "territorio."],
                "solution": ["Debiéramos", "fomentar", "el", "diálogo", "civilizado", "en", "todo", "el", "territorio."],
                "english": "We ought to foster civilized dialogue throughout the territory.",
                "teaches": ["subjuntivo-imperfecto-cortesia"]
            },
            {
                "id": f"{l6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "En la novela cumbre de Gallegos, Santos Luzardo luchó para que la civilización triunfara sobre la barbarie.",
                "english": "In Gallegos's masterwork novel, Santos Luzardo fought so that civilization would triumph over barbarism.",
                "teaches": ["subjuntivo-imperfecto-ra-se"]
            },
            {
                "id": f"{l6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la distribución sociolingüística predominante del imperfecto de subjuntivo en América Latina?",
                "options": [
                    "La desinencia en -ra abarca más del noventa y cinco por ciento de las ocurrencias habituales.",
                    "La desinencia en -se es la única empleada en el lenguaje de la calle.",
                    "Ambas desinencias se usan exactamente en una proporción del cincuenta por ciento.",
                    "Ninguna de las dos formas se utiliza en el habla hispanoamericana."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-imperfecto-registro"]
            }
        ]
    })

    # Classic Story for Core Unit 15: Rómulo Gallegos - Doña Bárbara (~700 words, strictly 650-825 words)
    story_core_15 = {
        "id": "b2-15",
        "title": "Doña Bárbara: El duelo entre la ley y el llano indómito",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de nivel B2 de la célebre novela de Rómulo Gallegos: el retorno del joven abogado Santos Luzardo a las llanuras venezolanas del Arauca para rescatar la hacienda familiar Altamira, su confrontación moral con la despótica terrateniente Doña Bárbara y la redención de la joven Marisela como símbolo del triunfo de la educación sobre la barbarie.",
        "characters": [
            "Santos Luzardo",
            "Doña Bárbara",
            "Marisela",
            "Lorenzo Barquero"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Bajo el sol de fuego que calcinaba las inmensidades del río Arauca, una boga solitaria hendía las aguas terrosas empujada por los pechos sudorosos de recios llaneros. En la popa de la embarcación viajaba un joven de porte erguido y mirada reflexiva: Santos Luzardo. Tras culminar con honores sus estudios de Derecho en la Universidad Central de Caracas, Santos regresaba a las sabanas de Apure resuelto a vender la hacienda Altamira, el predio ganadero heredado de sus ancestros donde las sangrientas disputas familiares habían diezmado a su estirpe. Su plan inicial consistía en liquidar aquellas tierras bravías y marcharse para siempre a Europa; sin embargo, al contemplar la majestad de la llanura y palpar la desolación de su pueblo, una íntima convicción patriótica sacudió su conciencia: no podía abandonar su tierra natal a la tiranía del despojo."
            },
            {
                "type": "narration",
                "text": "Altamira agonizaba bajo la sombra de 'El Miedo', la hacienda colindante dominada por una mujer despótica: Doña Bárbara. Conocida como la 'devoradora de hombres' y acusada de dominar la voluntad ajena mediante bebedizos de brujería y la complicidad de jueces venales, la cacica expandía sus dominios corriendo las cercas durante las noches y sobornando a las autoridades distritales. Su corazón, endurecido tras un atroz ultraje padecido en su juventud a manos de piratas fluviales, repudiaba cualquier signo de compasión: Bárbara gobernaba el llano como si las leyes jamás hubieran sido promulgadas y la violencia fuera el único orden concebible."
            },
            {
                "type": "narration",
                "text": "Al instalarse en el viejo caserón de Altamira, Santos Luzardo descubrió el más penoso vestigio de aquella tragedia territorial: su primo Lorenzo Barquero, otrora joven de brillante inteligencia y orador de tribuna, consumía sus días embrutecido por el aguardiente en un mísero bohío palustre. Barquero había sido seducido y arruinado años atrás por Doña Bárbara, quien tras despojarlo de su hacienda La Barquereña lo arrojó al cieno del olvido, dejándole como única compañía a Marisela, la hija nacida de aquel amor funesto. Santos halló a la muchacha descalza, vestida con andrajos sucios y viviendo en un estado de completo abandono montaraz, hablando un lenguaje rudimentario como si perteneciese a la bravía manigua animal."
            },
            {
                "type": "narration",
                "text": "Conmovido por la inocencia desamparada de la joven, Santos decidió asumir el rescate ético de su estirpe. La trasladó a la casona señorial de Altamira y, con infinita paciencia pedagógica, comenzó a educarla. Le enseñó a asear su cuerpo, a peinar sus cabellos dorados, a modular la voz con delicadeza civilizada y a descubrir la dignidad interior que yacía sepultada bajo el barro del monte. A medida que Marisela despertaba a la luz del raciocinio y el lenguaje culto, una transformación deslumbrante operó en ella: la criatura montaraz dio paso a una mujer de sublime belleza espiritual y moral que miraba a Santos con una mezcla enternecedora de veneración y naciente enamoramiento."
            },
            {
                "type": "narration",
                "text": "El choque inevitable entre Santos Luzardo y Doña Bárbara trascendió el litigio de linderos ganaderos para convertirse en un duelo fundacional entre civilización y barbarie. Cuando la temida terrateniente acudió a Altamira esperando encontrar al típico hacendado prepotente o acobardado al que pudiera doblegar con argucias hechiceras o amenazas de peones armados, quedó desconcertada ante la serenidad inquebrantable del abogado caraqueño. Santos le habló con la autoridad moral del Código Civil, desnudando la ilegitimidad de sus títulos posesorios y exigiéndole el deslinde judicial de los predios. Por primera vez en su vida despótica, Doña Bárbara sintió que su poder se resquebrajaba frente a un hombre incorruptible al que no lograba infundir terror ni concupiscencia."
            },
            {
                "type": "narration",
                "text": "Al descubrir que Santos tutelaba a su propia hija Marisela y que entre ambos florecía un afecto puro, el odio de Doña Bárbara se tornó en un tormento insoportable. Armada de una carabina, cabalgó hasta las cercanías de la casa dispuesta a liquidar a su rival; sin embargo, al espiar por la ventana y contemplar la sonrisa angelical de Marisela junto a Santos, una insólita piedad materna detuvo su dedo sobre el gatillo. Aquella revelación desgarró su rencor: comprendió que su tiempo de opresión y sangre había fenecido ante la claridad de una nueva aurora civilizatoria."
            },
            {
                "type": "narration",
                "text": "A la mañana siguiente, las riberas del Arauca despertaron con una noticia asombrosa: Doña Bárbara había desmantelado sus aposentos, cedido formalmente todas sus tierras a su hija legítima Marisela y desaparecido para siempre en los meandros misteriosos del Orinoco, perdiéndose en el horizonte fluvial como una sombra que el viento dispersa. Altamira y El Miedo quedaron unificadas en un solo territorio de trabajo digno y legalidad republicana. En el abrazo final de Santos y Marisela frente a la sabana verdeante, Rómulo Gallegos legó a Venezuela y al continente su más perdurable lección moral: que la barbarie no se vence con violencia recíproca, sino con la fuerza invencible de la justicia, la educación comunitaria y el imperio luminoso de la ley."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál era la intención inicial de Santos Luzardo al emprender el viaje de regreso a la hacienda Altamira?",
                        "options": [
                            "Vender las tierras ganaderas heredadas de su familia y trasladarse a vivir definitivamente a Europa.",
                            "Convertirse en lugarteniente armado de la cacica Doña Bárbara.",
                            "Fundar una compañía petrolera en las riberas del río Arauca.",
                            "Establecer un monasterio religioso en medio de la sabana."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 expone que Santos planeaba inicialmente vender Altamira y marcharse a Europa, pero el amor a su tierra y la injusticia reinante le hicieron cambiar de parecer."
                    },
                    {
                        "question": "¿De qué manera interviene Santos Luzardo en la vida de la joven Marisela?",
                        "options": [
                            "La rescata del abandono selvático en el bohío de su padre alcohólico y la educa pacientemente en el raciocinio, el aseo y el lenguaje digno.",
                            "La expulsa del territorio acusándola de complicidad con los crímenes de su madre.",
                            "La envía prisionera a la capital para que sea juzgada por las autoridades judiciales.",
                            "La obliga a trabajar como peona en las faenas ganaderas más duras de la hacienda."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 detalla cómo Santos traslada a Marisela a la casona y con dedicación pedagógica despierta su dignidad interior y su educación."
                    },
                    {
                        "question": "¿Qué suceso determina la desaparición definitiva de Doña Bárbara de las llanuras del Arauca?",
                        "options": [
                            "Al ver la inocencia y felicidad de su hija Marisela junto a Santos, desiste de su venganza, cede sus tierras legalmente y desaparece en el río.",
                            "Es derrotada y apresada tras una sangrienta batalla campal entre peones armados.",
                            "Es nombrada gobernadora del estado por un decreto presidencial en Caracas.",
                            "Sufre un naufragio accidental en el río Arauca durante una crecida invernal."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los párrafos 6 y 7 narran que un despertar de piedad materna detiene a Doña Bárbara, quien cede sus posesiones a Marisela y se aleja para siempre en el río."
                    }
                ]
            }
        }
    }

    write_json(f"stories/classics/b2/{c_unit}.json", story_core_15)

    write_json(f"lessons/b2/{l6_con}.json", {
        "id": "lesson.b2.15.consolidation",
        "title": "Consolidación: El imperfecto de subjuntivo y Doña Bárbara",
        "level": "B2",
        "goal": "Synthesize all aspects of the imperfect subjunctive through classical literary analysis of Rómulo Gallegos's Doña Bárbara.",
        "grammar": "síntesis del imperfecto de subjuntivo: alternancia -ra/-se, cortesía, contrafácticos y valor periodístico",
        "sections": [
            {"type": "goal", "items": [
                "Contrast -ra and -se across narrative, legal, and colloquial registers.",
                "Deploy polite modal formulas ('quisiera', 'pudiera') in formal dialogue.",
                "Analyze literary conflict (civilization vs. barbarism) using nuanced subjunctive structures."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{l6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Conjuga con soltura ambas desinencias (-ra y -se) del imperfecto de subjuntivo.",
                "Aplica las fórmulas atenuadas de cortesía con los verbos modales querer, deber y poder.",
                "Formula hipótesis contrafácticas con 'como si' y deseos presentes con 'ojalá'.",
                "Identifica el valor de indicativo de la desinencia en -ra en textos periodísticos y formales."
            ]}
        ]
    })
    print("Completed Core Unit 15 generation!")

    # ====================================================
    # 3. REGIONAL UNIT 15 (b2-venezuelapetroleo)
    # ====================================================
    r_unit = "b2-venezuelapetroleo"

    # --- Lesson 1: b2-venezuelapetroleo-01 ---
    r1 = f"{r_unit}-01"
    write_json(f"vocabulary/b2/{r1}-voc.json", {
        "id": "vocab.b2.venezuelapetroleo.01",
        "lesson": r1,
        "title": "Geografía de Caracas y el Ávila",
        "theme": "Léxico de orografía costera, valles intramontanos y cordilleras",
        "words": [
            {
                        "lemma": "litoral",
                        "translation": "coastal, littoral",
                        "pos": "adjective"
            },
            {
                        "lemma": "cordillera",
                        "translation": "mountain range",
                        "pos": "noun"
            },
            {
                        "lemma": "valle",
                        "translation": "valley",
                        "pos": "noun"
            },
            {
                        "lemma": "serranía",
                        "translation": "mountain ridge, highlands",
                        "pos": "noun"
            },
            {
                        "lemma": "orografía",
                        "translation": "terrain relief, orography",
                        "pos": "noun"
            },
            {
                        "lemma": "abrupto",
                        "translation": "abrupt, steep",
                        "pos": "adjective"
            }
        ]
    })

    write_json(f"grammar/b2/{r1}-a-gr.json", {
        "id": "grammar.b2.venezuelapetroleo.01.venezuela-geografia-valle-avila",
        "title": "La cordillera de la Costa, El Ávila y la geografía del valle de Caracas",
        "sections": [
            {
                "type": "text",
                "content": "La capital venezolana, Santiago de León de Caracas, se encuentra enclavada en un estrecho valle tectónico de la cordillera de la Costa a casi mil metros sobre el nivel del mar. La fisonomía urbana y el clima templado de la metrópoli están determinados por la presencia colosal del cerro El Ávila (bautizado por los pueblos indígenas caribes como **Waraira Repano**, 'la ola que vino de lejos'), una imponente muralla vegetal que supera los dos mil setecientos metros de altitud y separa físicamente al valle urbano de las cálidas aguas del mar Caribe."
            },
            {
                "type": "table",
                "title": "Toponimia y términos geográficos centrales",
                "rows": [
                    ["el Waraira Repano", "the sacred mountain separating Caracas from the sea"],
                    ["la cordillera de la Costa", "the rugged coastal mountain range"],
                    ["el valle de los Caracas", "the high tectonic valley of the capital"],
                    ["el clima de eterna primavera", "the pleasant tropical highland mountain climate"],
                    ["el litoral guaireño", "the Caribbean port coastline beneath the ridge"],
                    ["la quebrada de Catuche", "the urban streams descending from the heights"]
                ]
            },
            {
                "type": "tip",
                "content": "Para los caraqueños, El Ávila no es únicamente una formación geológica, sino un punto cardinal identitario insustituible: orienta la mirada urbana hacia el norte y actúa como un pulmón vegetal protegido bajo la categoría de Parque Nacional desde 1958."
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
                    ["litoral", "coastal shore"],
                    ["cordillera", "mountain range"],
                    ["valle", "valley"],
                    ["orografía", "terrain relief"]
                ],
                "teaches": ["b2-venezuelapetroleo-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El cerro El Ávila separa de manera majestuosa el valle de Caracas del __ Caribe. (litoral)",
                "answer": "litoral",
                "english": "Mount El Ávila majestically separates the Caracas valley from the Caribbean coast.",
                "teaches": ["venezuela-geografia-valle-avila"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es el nombre originario que los indígenas caribes daban al cerro El Ávila?",
                "options": [
                    "Waraira Repano, que significa la gran ola que vino de lejos.",
                    "Pico Bolívar en homenaje al libertador republicano.",
                    "Serranía de los Andes centrales.",
                    "Cerro de la Plata colonial."
                ],
                "correct": 0,
                "teaches": ["venezuela-geografia-valle-avila"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Ávila", "actúa", "como", "un", "pulmón", "vegetal", "para", "Caracas."],
                "solution": ["El", "Ávila", "actúa", "como", "un", "pulmón", "vegetal", "para", "Caracas."],
                "english": "El Ávila acts as a green lung for Caracas.",
                "teaches": ["venezuela-geografia-valle-avila"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Turista", "text": "¿Por qué el clima de Caracas resulta tan templado estando tan cerca del Caribe tropical?"},
                    {"speaker": "Guía", "text": "_____"}
                ],
                "options": [
                    "Se debe a que el valle se ubica a casi mil metros de altitud y la brisa del Ávila refresca la atmósfera.",
                    "Porque en Venezuela nieva durante todos los meses del año.",
                    "Debido a que el océano se secó por completo en el siglo pasado.",
                    "Porque las fábricas de hielo enfrían toda la ciudad."
                ],
                "correct": 0,
                "teaches": ["venezuela-geografia-valle-avila"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Desde el mirador de la montaña, la ciudad se despliega a lo largo de un valle estrecho y luminoso.",
                "english": "From the mountain lookout, the city unfolds along a narrow and luminous valley.",
                "teaches": ["venezuela-geografia-valle-avila"]
            }
        ]
    })

    # --- Lesson 2: b2-venezuelapetroleo-02 ---
    r2 = f"{r_unit}-02"
    write_json(f"vocabulary/b2/{r2}-voc.json", {
        "id": "vocab.b2.venezuelapetroleo.02",
        "lesson": r2,
        "title": "El pozo petrolero y el petroestado",
        "theme": "Léxico de hidrocarburos, yacimientos y rentismo minero",
        "words": [
            {
                        "lemma": "yacimiento",
                        "translation": "mineral or oil deposit",
                        "pos": "noun"
            },
            {
                        "lemma": "rentismo",
                        "translation": "reliance on resource rents",
                        "pos": "noun"
            },
            {
                        "lemma": "concesión",
                        "translation": "operating concession, license",
                        "pos": "noun"
            },
            {
                        "lemma": "hidrocarburo",
                        "translation": "hydrocarbon, petroleum",
                        "pos": "noun"
            },
            {
                        "lemma": "fiscal",
                        "translation": "fiscal, public tax-related",
                        "pos": "adjective"
            },
            {
                        "lemma": "reventón",
                        "translation": "oil blowout, sudden gush",
                        "pos": "noun"
            }
        ]
    })

    write_json(f"grammar/b2/{r2}-a-gr.json", {
        "id": "grammar.b2.venezuelapetroleo.02.venezuela-petroleo-zumaque-petroestado",
        "title": "El pozo Zumaque I, el Barroso II y la génesis del petroestado venezolano",
        "sections": [
            {
                "type": "text",
                "content": "A comienzos del siglo XX, Venezuela era una república predominantemente agraria cuya modesta economía dependía de la exportación de café y cacao fino de aroma. Esta realidad cambió de forma telúrica el 31 de julio de 1914 con el inicio de la explotación del pozo **Zumaque I** en el campo Mene Grande, en las riberas orientales del lago de Maracaibo. El proceso se consolidó definitivamente en diciembre de 1922 con el legendario reventón del pozo **Los Barrosos II**, que arrojó más de cien mil barriles diarios de crudo durante nueve días consecutivos, revelando al planeta la presencia de uno de los mayores depósitos de hidrocarburos del globo."
            },
            {
                "type": "table",
                "title": "Conceptos clave del rentismo petrolero",
                "rows": [
                    ["el petroestado", "the state apparatus financed primarily by oil royalties"],
                    ["la renta petrolera", "the sovereign capture of extraordinary resource revenue"],
                    ["el pozo Zumaque I", "the historic first commercial well drilled in 1914"],
                    ["el reventón del Barroso II", "the massive 1922 oil blowout that attracted global syndicates"],
                    ["el éxodo rural", "the mass migration of agricultural peasants to oil camps"],
                    ["sembrar el petróleo", "Arturo Uslar Pietri's call to reinvest oil rents in agriculture"]
                ]
            },
            {
                "type": "tip",
                "content": "El intelectual Arturo Uslar Pietri formuló en 1936 su famosa consigna editorial: *'Sembrar el petróleo'*. Advertía que si la nación no invertía la fabulosa renta de los hidrocarburos en educación, tecnificación agrícola e industrialización, el petróleo se convertiría en un espejismo transitorio que ahogaría la capacidad productiva nacional."
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
                    ["yacimiento", "oil deposit"],
                    ["rentismo", "reliance on resource rents"],
                    ["concesión", "operating concession"],
                    ["reventón", "oil gush / blowout"]
                ],
                "teaches": ["b2-venezuelapetroleo-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El reventón del pozo Barroso II en 1922 convirtió a Venezuela en un actor determinante en el mercado global de __. (hidrocarburo)",
                "answer": "hidrocarburos",
                "english": "The blowout of the Barroso II well in 1922 turned Venezuela into a decisive actor in the global hydrocarbons market.",
                "teaches": ["venezuela-petroleo-zumaque-petroestado"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué advertía el intelectual Arturo Uslar Pietri con la célebre frase 'sembrar el petróleo'?",
                "options": [
                    "Que la renta petrolera debía reinvertirse en educación, industria y agricultura para evitar la ruina de una economía monoproductora.",
                    "Que los barriles de petróleo debían enterrarse literalmente en los campos de cultivo.",
                    "Que el Estado debía renunciar a extraer crudo para proteger el café tradicional.",
                    "Que las compañías petroleras extranjeras debían gobernar el país."
                ],
                "correct": 0,
                "teaches": ["venezuela-petroleo-zumaque-petroestado"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "renta", "petrolera", "transformó", "las", "finanzas", "públicas", "de", "Venezuela."],
                "solution": ["La", "renta", "petrolera", "transformó", "las", "finanzas", "públicas", "de", "Venezuela."],
                "english": "Oil rent transformed Venezuela's public finances.",
                "teaches": ["venezuela-petroleo-zumaque-petroestado"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Cómo afectó el descubrimiento petrolero al campo venezolano tradicional?"},
                    {"speaker": "Investigadora", "text": "_____"}
                ],
                "options": [
                    "Provocó un éxodo masivo del campesinado hacia los campos petroleros y las ciudades, reduciendo drásticamente la producción de café y cacao.",
                    "Hizo que todos los venezolanos se dedicaran exclusivamente a pescar en el mar Caribe.",
                    "Aumentó la producción de cacao hasta triplicar el comercio con Europa.",
                    "No generó ningún impacto en la vida rural venezolana."
                ],
                "correct": 0,
                "teaches": ["venezuela-petroleo-zumaque-petroestado"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "En pocas décadas, el petroestado centralizó los recursos fiscales y redefinió el pacto social.",
                "english": "In a few decades, the petrostate centralized fiscal resources and redefined the social pact.",
                "teaches": ["venezuela-petroleo-zumaque-petroestado"]
            }
        ]
    })

    # --- Lesson 3: b2-venezuelapetroleo-03 ---
    r3 = f"{r_unit}-03"
    write_json(f"vocabulary/b2/{r3}-voc.json", {
        "id": "vocab.b2.venezuelapetroleo.03",
        "lesson": r3,
        "title": "Arquitectura moderna y síntesis de las artes",
        "theme": "Léxico de vanguardias constructivas, acústica y hormigón armado",
        "words": [
            {
                        "lemma": "vanguardia",
                        "translation": "avant-garde, forefront",
                        "pos": "noun"
            },
            {
                        "lemma": "acústica",
                        "translation": "acoustics, sound properties",
                        "pos": "noun"
            },
            {
                        "lemma": "hormigón",
                        "translation": "concrete, reinforced concrete",
                        "pos": "noun"
            },
            {
                        "lemma": "sincretismo",
                        "translation": "syncretism, integration",
                        "pos": "noun"
            },
            {
                        "lemma": "mural",
                        "translation": "mural, wall painting",
                        "pos": "noun"
            },
            {
                        "lemma": "brutalismo",
                        "translation": "brutalist architecture",
                        "pos": "noun"
            }
        ]
    })

    write_json(f"grammar/b2/{r3}-a-gr.json", {
        "id": "grammar.b2.venezuelapetroleo.03.venezuela-arquitectura-villanueva-ucv",
        "title": "Carlos Raúl Villanueva y la Ciudad Universitaria de Caracas",
        "sections": [
            {
                "type": "text",
                "content": "Construida entre 1940 y 1960 bajo el liderazgo del eminente arquitecto venezolano **Carlos Raúl Villanueva**, la Ciudad Universitaria de Caracas (campus central de la Universidad Central de Venezuela, UCV) constituye una de las cumbres más acabadas de la arquitectura moderna mundial, declarada en el año 2000 como Patrimonio Cultural de la Humanidad por la UNESCO.\n\nEl proyecto materializó el concepto de **'Síntesis de las Artes Mayores'**, integrando de manera orgánica los volúmenes de hormigón armado, las celosías tropicales que filtran la luz solar y la ventilación cruzada con más de cien obras de maestros de las vanguardias internacionales como Alexander Calder, Fernand Léger, Victor Vasarely, Jean Arp y los insignes creadores plásticos venezolanos Francisco Narváez y Mateo Manaure."
            },
            {
                "type": "table",
                "title": "Elementos emblemáticos del campus de la UCV",
                "rows": [
                    ["el Aula Magna", "Villanueva's grand hall renowned for its acoustic perfection"],
                    ["las Nubes Flotantes", "Alexander Calder's flying acoustic saucers inside the hall"],
                    ["el reloj de la plaza del Rectorado", "the iconic three-legged concrete modernist clock tower"],
                    ["el mural de Fernand Léger", "the celebrated colorful mosaic mural framing the open plaza"],
                    ["las celosías y corredores cubiertos", "tropical brise-soleil corridors creating shade and breeze"],
                    ["la Biblioteca Central", "the towering intellectual centerpiece facing the Plaza Cubierta"]
                ]
            },
            {
                "type": "tip",
                "content": "Las *Nubes Flotantes* de Alexander Calder en el techo del Aula Magna son un ejemplo célebre a nivel planetario donde la escultura cinética y la ingeniería acústica se fusionan: los paneles no solo embellecen el espacio, sino que eliminan cualquier reverberación defectuosa, logrando una acústica perfecta."
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
                    ["vanguardia", "avant-garde"],
                    ["acústica", "sound properties / acoustics"],
                    ["hormigón", "reinforced concrete"],
                    ["brutalismo", "brutalist architecture"]
                ],
                "teaches": ["b2-venezuelapetroleo-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Carlos Raúl Villanueva concibió la Ciudad Universitaria como una síntesis armónica de la arquitectura con las artes __. (plástico)",
                "answer": "plásticas",
                "english": "Carlos Raúl Villanueva conceived the University City as a harmonic synthesis of architecture with the plastic arts.",
                "teaches": ["venezuela-arquitectura-villanueva-ucv"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función dual cumplen las 'Nubes Flotantes' de Alexander Calder en el Aula Magna?",
                "options": [
                    "Operan simultáneamente como esculturas artísticas de vanguardia y como paneles de calibración acústica perfecta.",
                    "Sirven únicamente como pararrayos en caso de tormentas tropicales.",
                    "Eran pantallas de televisión instaladas para transmitir conferencias magistrales.",
                    "Son depósitos de agua para el sistema de incendios del auditorio."
                ],
                "correct": 0,
                "teaches": ["venezuela-arquitectura-villanueva-ucv"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "UNESCO", "declaró", "la", "Ciudad", "Universitaria", "Patrimonio", "de", "la", "Humanidad."],
                "solution": ["La", "UNESCO", "declaró", "la", "Ciudad", "Universitaria", "Patrimonio", "de", "la", "Humanidad."],
                "english": "UNESCO declared the University City World Heritage.",
                "teaches": ["venezuela-arquitectura-villanueva-ucv"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Estudiante", "text": "¿Por qué los pasillos de la UCV son abiertos y poseen tantas celosías de hormigón?"},
                    {"speaker": "Profesora", "text": "_____"}
                ],
                "options": [
                    "Villanueva diseñó celosías y corredores cubiertos para permitir la ventilación natural y la sombra constante frente al calor caraqueño.",
                    "Faltaba presupuesto para construir ventanas y paredes normales.",
                    "Para que los estudiantes pudieran saltar por los pasillos sin utilizar escaleras.",
                    "Porque las normas coloniales exigían que no hubiera puertas."
                ],
                "correct": 0,
                "teaches": ["venezuela-arquitectura-villanueva-ucv"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La integración de murales y esculturas en los patios universitarios democratizó el acceso cotidiano al arte.",
                "english": "The integration of murals and sculptures in university courtyards democratized daily access to art.",
                "teaches": ["venezuela-arquitectura-villanueva-ucv"]
            }
        ]
    })

    # --- Lesson 4: b2-venezuelapetroleo-04 ---
    r4 = f"{r_unit}-04"
    write_json(f"vocabulary/b2/{r4}-voc.json", {
        "id": "vocab.b2.venezuelapetroleo.04",
        "lesson": r4,
        "title": "Arte cinético y educación musical",
        "theme": "Léxico de cinetismo plástico, percepción cromática y orquestas",
        "words": [
            {
                        "lemma": "cinetismo",
                        "translation": "kinetic art",
                        "pos": "noun"
            },
            {
                        "lemma": "cromático",
                        "translation": "chromatic, color-related",
                        "pos": "adjective"
            },
            {
                        "lemma": "percepción",
                        "translation": "perception",
                        "pos": "noun"
            },
            {
                        "lemma": "penetrable",
                        "translation": "walk-in interactive sculpture",
                        "pos": "noun"
            },
            {
                        "lemma": "orquestal",
                        "translation": "orchestral",
                        "pos": "adjective"
            },
            {
                        "lemma": "inducción",
                        "translation": "optical induction, stimulating effect",
                        "pos": "noun"
            }
        ]
    })

    write_json(f"grammar/b2/{r4}-a-gr.json", {
        "id": "grammar.b2.venezuelapetroleo.04.venezuela-arte-cinetico-cruzdiez-soto",
        "title": "El cinetismo de Cruz-Diez y Soto y la revolución orquestal venezolana",
        "sections": [
            {
                "type": "text",
                "content": "A mediados del siglo XX, Venezuela se posicionó en la vanguardia plástica mundial a través del arte cinético y óptico, impulsado por dos figuras monumentales: **Jesús Rafael Soto** y **Carlos Cruz-Diez**. Soto revolucionó la relación entre el espectador y la obra mediante sus célebres *Penetrables*, bosques de varillas colgantes de nailon o aluminio que el público atraviesa físicamente, disolviendo los límites entre espacio y materia. Por su parte, Cruz-Diez investigó el color no como un pigmento estático sobre el lienzo, sino como una realidad efímera y autónoma en constante mutación a través de sus *Fisicromías* y sus cruces peatonales cromáticos instalados en el aeropuerto de Maiquetía y las principales avenidas caraqueñas.\n\nEn paralelo a este auge visual, en 1975 el maestro **José Antonio Abreu** fundó el Sistema Nacional de Orquestas y Coros Juveniles e Infantiles de Venezuela ('El Sistema'), un modelo pedagógico y social pionero a nivel global que transformó la práctica musical colectiva en una formidable herramienta de rescate social, inclusión comunitaria y excelencia interpretativa."
            },
            {
                "type": "table",
                "title": "Hitos artísticos y musicales venezolanos",
                "rows": [
                    ["los Penetrables de Soto", "interactive sculptures where the viewer physically walks inside color"],
                    ["las Fisicromías de Cruz-Diez", "kinetic works exploring color as a living optical phenomenon"],
                    ["el piso del Aeropuerto de Maiquetía", "Cruz-Diez's world-famous chromatic floor mosaic symbol of journeys"],
                    ["El Sistema (Fundación Musical)", "pioneering youth orchestral program founded by maestro Abreu"],
                    ["Gustavo Dudamel", "world-renowned conductor formed inside El Sistema's classrooms"],
                    ["la Esfera Caracas", "Soto's giant orange kinetic sphere floating beside the highway"]
                ]
            },
            {
                "type": "tip",
                "content": "Para millones de venezolanos en todo el mundo, la *Cromointerferencia de color aditivo* de Cruz-Diez en el suelo del aeropuerto internacional Simón Bolívar de Maiquetía se convirtió en el icono sentimental más poderoso de la despedida y el reencuentro de la diáspora contemporánea."
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
                    ["cinetismo", "kinetic art"],
                    ["cromatico", "color-related"],
                    ["penetrable", "walk-in sculpture"],
                    ["orquestal", "orchestral"]
                ],
                "teaches": ["b2-venezuelapetroleo-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Jesús Rafael Soto invitaba a los espectadores a atravesar físicamente sus famosos __ de varillas colgantes. (penetrable)",
                "answer": "penetrables",
                "english": "Jesús Rafael Soto invited viewers to physically walk through his famous penetrables of hanging rods.",
                "teaches": ["venezuela-arte-cinetico-cruzdiez-soto"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál fue el objetivo fundacional de 'El Sistema' creado por José Antonio Abreu en 1975?",
                "options": [
                    "Utilizar la educación orquestal colectiva como un instrumento de rescate social, disciplina y superación de la pobreza.",
                    "Cobrar entradas carísimas para conciertos exclusivos de música europea.",
                    "Prohibir que los niños de sectores populares tocaran instrumentos clásicos.",
                    "Exportar instrumentos de cuerda hacia los Estados Unidos."
                ],
                "correct": 0,
                "teaches": ["venezuela-arte-cinetico-cruzdiez-soto"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Cruz-Diez", "investigó", "el", "color", "como", "un", "acontecimiento", "espacial."],
                "solution": ["Cruz-Diez", "investigó", "el", "color", "como", "un", "acontecimiento", "espacial."],
                "english": "Cruz-Diez investigated color as a spatial event.",
                "teaches": ["venezuela-arte-cinetico-cruzdiez-soto"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Curador", "text": "¿Por qué el suelo del aeropuerto de Maiquetía tiene un significado tan entrañable para los venezolanos?"},
                    {"speaker": "Historiadora", "text": "_____"}
                ],
                "options": [
                    "Porque la obra cinética de Cruz-Diez fue el último tapiz de color que pisaron millones de compatriotas al emigrar del país.",
                    "Porque allí se descubrió el primer yacimiento de oro del siglo veinte.",
                    "Debido a que es la pista de aterrizaje más larga de América del Sur.",
                    "Porque allí ensayaba la orquesta sinfónica todos los domingos por la tarde."
                ],
                "correct": 0,
                "teaches": ["venezuela-arte-cinetico-cruzdiez-soto"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La música sinfónica se convirtió en una herramienta de dignidad comunitaria en los barrios de Venezuela.",
                "english": "Symphonic music became a tool of community dignity in the neighborhoods of Venezuela.",
                "teaches": ["venezuela-arte-cinetico-cruzdiez-soto"]
            }
        ]
    })

    # --- Lesson 5: b2-venezuelapetroleo-05 ---
    r5 = f"{r_unit}-05"
    write_json(f"vocabulary/b2/{r5}-voc.json", {
        "id": "vocab.b2.venezuelapetroleo.05",
        "lesson": r5,
        "title": "Bonanza petrolera y sociología urbana",
        "theme": "Léxico de economía política, petrodólares y consumo cosmopolita",
        "words": [
            {
                        "lemma": "bonanza",
                        "translation": "economic prosperity boom",
                        "pos": "noun"
            },
            {
                        "lemma": "espejismo",
                        "translation": "mirage, illusion",
                        "pos": "noun"
            },
            {
                        "lemma": "petrodólar",
                        "translation": "petrodollar",
                        "pos": "noun"
            },
            {
                        "lemma": "consumismo",
                        "translation": "frenzied consumerism",
                        "pos": "noun"
            },
            {
                        "lemma": "paradoja",
                        "translation": "paradox",
                        "pos": "noun"
            },
            {
                        "lemma": "sobrevalorado",
                        "translation": "overvalued",
                        "pos": "adjective"
            }
        ]
    })

    write_json(f"grammar/b2/{r5}-a-gr.json", {
        "id": "grammar.b2.venezuelapetroleo.05.venezuela-bonanza-petrolera-sociedad",
        "title": "La bonanza petrolera de los años setenta y las ilusiones de la 'Venezuela Saudita'",
        "sections": [
            {
                "type": "text",
                "content": "Durante la década de 1970, impulsada por la crisis energética mundial de 1973 y el embargo petrolero de la OPEP, Venezuela experimentó una avalancha de ingresos fiscales sin precedentes en la historia latinoamericana. El país fue bautizado en los medios internacionales como la **'Venezuela Saudita'**: el bolívar gozaba de una fortaleza cambiaria extraordinaria, los centros comerciales de Caracas rebosaban de bienes de lujo importados y viajar de compras a Miami ('¡Dame dos!') se convirtió en una costumbre generalizada entre las clases medias y altas.\n\nSin embargo, aquella opulencia encerraba graves distorsiones estructurales descritas en la economía política como la 'enfermedad holandesa': una moneda sobrevalorada que arruinó la agricultura y la manufactura local, un gasto público deficitario financiado con endeudamiento externo y una creciente dependencia del precio internacional del barril, que al desplomarse en la década siguiente dio paso al 'Viernes Negro' de 1983 y a severas crisis inflacionarias."
            },
            {
                "type": "table",
                "title": "Términos sociológicos y venezolanos de la época",
                "rows": [
                    ["la Venezuela Saudita", "the 1970s petrodollar boom characterized by opulent consumerism"],
                    ["el '¡Dame dos!'", "popular catchphrase mocking the frenzy for cheap imported luxury goods"],
                    ["la enfermedad holandesa", "economic distortion where resource exports crush domestic industry"],
                    ["el Viernes Negro (1983)", "the historic currency devaluation ending decades of exchange stability"],
                    ["pana / chamo / chévere", "emblematic Venezuelan slang: buddy / kid / cool or excellent"],
                    ["la nacionalización del petróleo", "the 1976 legal creation of the state-owned oil enterprise PDVSA"]
                ]
            },
            {
                "type": "tip",
                "content": "En el habla cotidiana venezolana, palabras como *pana* (amigo íntimo), *chamo* (muchacho o joven) y *chévere* (excelente, agradable) se consolidaron durante estas décadas cosmopolitas, extendiéndose posteriormente por toda la cuenca del Caribe y los países receptores de la migración venezolana."
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
                    ["bonanza", "economic prosperity boom"],
                    ["espejismo", "mirage / illusion"],
                    ["petrodólar", "petroleum revenue dollar"],
                    ["consumismo", "frenzied consumerism"]
                ],
                "teaches": ["b2-venezuelapetroleo-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La enorme entrada de petrodólares en los años setenta desató un periodo de opulencia conocido como la Venezuela __. (saudita)",
                "answer": "Saudita",
                "english": "The huge influx of petrodollars in the seventies unleashed a period of opulence known as Saudi Venezuela.",
                "teaches": ["venezuela-bonanza-petrolera-sociedad"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué fenómeno económico se conoció como 'la enfermedad holandesa' en Venezuela?",
                "options": [
                    "La sobrevaloración de la moneda petrolera que abarató las importaciones y desmanteló la agricultura y manufactura locales.",
                    "Una epidemia biológica transmitida por el ganado vacuno en los Llanos.",
                    "La prohibición de comerciar con los países de los Países Bajos y las Antillas.",
                    "La obligación de pagar todos los salarios en monedas de plata."
                ],
                "correct": 0,
                "teaches": ["venezuela-bonanza-petrolera-sociedad"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Viernes", "Negro", "de", "1983", "puso", "fin", "a", "la", "estabilidad."],
                "solution": ["El", "Viernes", "Negro", "de", "1983", "puso", "fin", "a", "la", "estabilidad."],
                "english": "Black Friday of 1983 put an end to stability.",
                "teaches": ["venezuela-bonanza-petrolera-sociedad"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Qué lecciones dejó el espejismo de la bonanza petrolera de los años setenta?"},
                    {"speaker": "Economista", "text": "_____"}
                ],
                "options": [
                    "Demostró que el consumo de bienes importados no sustituye al desarrollo productivo y que la dependencia del crudo genera extrema vulnerabilidad.",
                    "Que un país puede vivir indefinidamente sin producir alimentos ni energía.",
                    "Que los precios del petróleo en el mercado internacional nunca vuelven a caer.",
                    "Que las monedas latinoamericanas no sufren devaluaciones fiscales."
                ],
                "correct": 0,
                "teaches": ["venezuela-bonanza-petrolera-sociedad"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La volatilidad de los precios del crudo evidenció los riesgos del modelo monoproductor rentista.",
                "english": "The volatility of crude prices showed the risks of the rentier single-product model.",
                "teaches": ["venezuela-bonanza-petrolera-sociedad"]
            }
        ]
    })

    # --- Lesson 6: b2-venezuelapetroleo-consolidation ---
    rc_con = f"{r_unit}-consolidation"
    write_json(f"exercises/b2/{rc_con}-ex.json", {
        "lesson": rc_con,
        "exercises": [
            {
                "id": f"{rc_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["cordillera", "mountain range"],
                    ["yacimiento", "petroleum deposit"],
                    ["cinetismo", "kinetic art"],
                    ["bonanza", "prosperity boom"]
                ],
                "teaches": ["b2-venezuelapetroleo-vocab"]
            },
            {
                "id": f"{rc_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Ávila o Waraira Repano protege el valle de Caracas frente a los vientos marinos del __. (litoral)",
                "answer": "litoral",
                "english": "El Ávila or Waraira Repano protects the Caracas valley against marine winds from the coast.",
                "teaches": ["venezuela-geografia-valle-avila"]
            },
            {
                "id": f"{rc_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué hito arquitectónico fue declarado Patrimonio de la Humanidad por la UNESCO en el año 2000 en Caracas?",
                "options": [
                    "La Ciudad Universitaria de Caracas, diseñada por Carlos Raúl Villanueva.",
                    "Las murallas coloniales del puerto de La Guaira.",
                    "El teleférico del cerro El Ávila.",
                    "El centro comercial más moderno de América Latina."
                ],
                "correct": 0,
                "teaches": ["venezuela-arquitectura-villanueva-ucv"]
            },
            {
                "id": f"{rc_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El artista Carlos Cruz-Diez investigó el color como una realidad espacial autónoma en sus famosas __. (fisicromía)",
                "answer": "fisicromías",
                "english": "Artist Carlos Cruz-Diez investigated color as an autonomous spatial reality in his famous physichromies.",
                "teaches": ["venezuela-arte-cinetico-cruzdiez-soto"]
            },
            {
                "id": f"{rc_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál fue el impacto social de El Sistema de orquestas fundado por José Antonio Abreu?",
                "options": [
                    "Democratizó la educación musical y sirvió de modelo internacional de inclusión para jóvenes de todos los estratos.",
                    "Restringió el aprendizaje de instrumentos a familias adineradas de la capital.",
                    "Sustituyó las escuelas primarias por teatros de ópera en todo el territorio.",
                    "Desapareció a los pocos meses de su fundación por falta de alumnos."
                ],
                "correct": 0,
                "teaches": ["venezuela-arte-cinetico-cruzdiez-soto"]
            },
            {
                "id": f"{rc_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "economía", "del", "petroestado", "centralizó", "la", "renta", "en", "Caracas."],
                "solution": ["La", "economía", "del", "petroestado", "centralizó", "la", "renta", "en", "Caracas."],
                "english": "The economy of the petrostate centralized rent in Caracas.",
                "teaches": ["venezuela-petroleo-zumaque-petroestado"]
            },
            {
                "id": f"{rc_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Caracas vivió el siglo veinte entre el esplendor de las artes modernas y los dilemas del rentismo.",
                "english": "Caracas lived the twentieth century between the splendor of modern arts and the dilemmas of rentierism.",
                "teaches": ["venezuela-bonanza-petrolera-sociedad"]
            },
            {
                "id": f"{rc_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué acontecimiento histórico en 1922 confirmó la inmensa riqueza petrolera del subsuelo venezolano?",
                "options": [
                    "El reventón del pozo Los Barrosos II en el lago de Maracaibo que arrojó cien mil barriles diarios.",
                    "La inauguración del primer ferrocarril eléctrico andino.",
                    "La llegada de los primeros barcos pesqueros a Margarita.",
                    "El terremoto que destruyó la antigua catedral colonial."
                ],
                "correct": 0,
                "teaches": ["venezuela-petroleo-zumaque-petroestado"]
            }
        ]
    })

    # ----------------------------------------------------
    # Regional Stories (5 lesson stories + 1 capstone = 6)
    # Strictly between 650 and 825 words (~700 words target)
    # ----------------------------------------------------

    story_ven1_01 = {
        "id": "b2-venezuelapetroleo-01",
        "title": "Caracas y el Ávila: El valle verde bajo la montaña tutelar",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica geográfica y urbana de nivel B2 sobre Santiago de León de Caracas: su emplazamiento en el valle tectónico de la cordillera de la Costa, la imponente presencia del Waraira Repano (El Ávila) como barrera climática ante el mar Caribe, la arquitectura moderna entre autopistas y la memoria de las quebradas que nutrieron la capital.",
        "characters": [
            "Arquitecto Mendoza",
            "Carolina",
            "Guardaparques González"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Enclavada en un sinuoso valle intramontano a novecientos metros sobre el nivel del mar, la ciudad de Caracas se revela ante los ojos del viajero como un prodigio de contrastes topográficos donde la jungla de concreto y el verde salvaje de los trópicos conviven en un apretado abrazo. La metrópoli debe su existencia y su microclima de eterna primavera a una gigantesca columna vertebral de roca precámbrica: la cordillera de la Costa, un plegamiento orográfico abrupto que recorre el norte de Venezuela y que en su flanco capitalino se yergue con una soberanía colosal personificada en el cerro El Ávila. Esta mole pétrea, que los originarios indígenas caribes veneraban bajo el nombre sagrado de Waraira Repano —'la gran ola que vino de lejos'—, se alza verticalmente hasta rozar los dos mil ochocientos metros de altitud en el Pico Naiguatá, actuando como un escudo protector inexpugnable frente a los ciclones tropicales y las tempestades marinas del Caribe."
            },
            {
                "type": "narration",
                "text": "Para cualquier habitante de Caracas, el Waraira Repano no constituye una mera formación geológica de interés paisajístico, sino un punto cardinal de la conciencia existencial: mirar hacia el cerro es orientar el norte del alma, comprobar si la calima cubre el valle o si los penachos de niebla blanca descienden como algodón hilado sobre los techos de la ciudad. El arquitecto Mendoza, contemplando el perfil escarpado de la cordillera desde la terraza de un edificio brutalista en Los Caobos junto a Carolina, una joven urbanista caraqueña, reflexiona sobre esta singularidad: 'En la mayoría de las capitales mundiales el horizonte se expande en llanuras infinitas; en Caracas, en cambio, la montaña es nuestra pared maestra, una presencia viva e imponente que nos recuerda a diario que la naturaleza tropical es indómita frente al afán urbanizador de los seres humanos'."
            },
            {
                "type": "narration",
                "text": "Durante la época colonial, cuando el conquistador Diego de Losada fundó Santiago de León de Caracas en 1567, el valle era un paraíso de huertos agrícolas regado por cuatro cursos de agua fundamentales: el río Guaire y las quebradas Catuche, Caroata y Anauco. En aquellas riberas fértiles crecían haciendas de caña dulce y plantaciones del célebre cacao 'Chuao' y 'Carenero', codiciado en las cortes virreinales europeas por su suavidad aromática inigualable. El guardaparques González, quien custodia las nacientes de agua en los senderos de Sabas Nieves, recuerda que de esas mismas laderas empinadas bajaban los arrieros con recuas de mulas cargadas de café hacia el puerto de La Guaira, desafiando el histórico 'Camino de los Españoles', un sendero empedrado que trepaba las cumbres nubladas antes de desplomarse hacia el calor ardiente del mar."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el siglo veinte transformó radicalmente aquella apacible comarca bucólica. La irrupción masiva de la renta petrolera inyectó en el estrecho valle una ambición modernista desmesurada. En pocas décadas, las antiguas haciendas de café dieron paso a formidables autopistas de varios canales como la Francisco Fajardo y la Cota Mil, rascacielos vanguardistas de vidrio espejado y audaces complejos residenciales levantados sobre las colinas colindantes. Caracas se convirtió en una de las urbes más vertiginosas y cosmopolitas del continente, donde los automóviles último modelo transitaban al pie de una montaña que fue declarada Parque Nacional en 1958 para impedir que la codicia inmobiliaria talara sus bosques nubosos de helechos gigantes y orquídeas endémicas."
            },
            {
                "type": "narration",
                "text": "Esa misma orografía compleja generó una profunda fractura sociourbana. Mientras el fondo plano del valle albergaba el trazado ordenado de las clases medias y altas, cientos de miles de familias campesinas atraídas por el espejismo del oro negro se asentaron en las faldas empinadas de los cerros occidentales y orientales, levantando con ladrillo rojo y planchas de zinc los inmensos barrios populares de Petare, Catia y San Agustín. Estas barriadas autoconstruidas desafían la gravedad sobre las pendientes inestables, tejiendo una red solidaria de escalinatas infinitas donde el sonido cadencioso de la salsa brava, el pregón callejero y el olor a café recién colado confirman la inquebrantable vitalidad del pueblo caraqueño frente a cualquier rigor socioeconómico."
            },
            {
                "type": "narration",
                "text": "Al caer el atardecer, cuando las luces de la urbe comienzan a encenderse como un mar de luciérnagas y el Ávila se tiñe de tonos violetas y cobrizos bajo el crepúsculo ecuatorial, Caracas revela su magia inextinguible. Desde las alturas del teleférico que corona la cima de la montaña hasta el bullicio nocturno de las plazas públicas, el valle late con una energía intensa y solidaria. Sus habitantes saben que a pesar de las crisis políticas y las transformaciones urbanas, la montaña siempre permanecerá allí: vigilante, verde y eterna, recordándoles que en el corazón de este valle caribeño la belleza y la resistencia humana florecen con la misma tenacidad que las orquídeas en la roca virgen."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué nombre ancestral daban los indígenas caribes al cerro El Ávila y qué significado tiene?",
                        "options": [
                            "Waraira Repano, que significa la gran ola que vino de lejos.",
                            "Pico Naiguatá en conmemoración de un gran cacique.",
                            "Mene Grande por las emanaciones de alquitrán en sus laderas.",
                            "Serranía de San Agustín en honor a los primeros frailes."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 precisa que los pueblos indígenas caribes llamaban a la montaña Waraira Repano, que significa 'la gran ola que vino de lejos'."
                    },
                    {
                        "question": "¿Qué productos agrícolas se cultivaban en las haciendas del valle de Caracas antes de la llegada de la era petrolera?",
                        "options": [
                            "Cacao fino de aroma como el Chuao y Carenero, además de caña de azúcar y café.",
                            "Trigo sarraceno y cebada de clima polar.",
                            "Únicamente uvas para la producción de vino de exportación.",
                            "Algodón transgénico y soja intensiva."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 detalla que en las haciendas coloniales del valle se cosechaba cacao fino de gran renombre como Chuao y Carenero, caña y café."
                    },
                    {
                        "question": "¿En qué año fue declarado Parque Nacional el cerro El Ávila para protegerlo de la expansión urbana?",
                        "options": [
                            "En 1958, para resguardar sus bosques nubosos de helechos y orquídeas de la voracidad inmobiliaria.",
                            "En 1567 con la llegada de Diego de Losada.",
                            "En 1983 tras la devaluación del Viernes Negro.",
                            "En el año 2000 mediante un decreto de la UNESCO."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 menciona que el cerro fue protegido legalmente bajo la figura de Parque Nacional en el año 1958."
                    }
                ]
            }
        }
    }

    story_ven1_02 = {
        "id": "b2-venezuelapetroleo-02",
        "title": "El oro negro: De los manantiales de asfalto al estallido del petroestado",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica histórica y económica de nivel B2 sobre la transformación petrolera de Venezuela: los 'mene' de alquitrán conocidos por los pueblos originarios añú y wayúu en el lago de Maracaibo, el pozo Zumaque I de 1914, el colosal reventón del Barroso II en 1922 y el surgimiento del Estado rentista que reconfiguró la sociedad venezolana.",
        "characters": [
            "Don Cipriano Valera",
            "Ingeniero Briceño",
            "María Chiquinquirá"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Siglos antes de que los consorcios financieros de Londres y Nueva York soñaran con el dominio de los combustibles fósiles, las aguas serenas de la cuenca del lago de Maracaibo ya conocían el misterio del hidrocarburo. Los pueblos originarios añú y wayúu recogían con canoas de madera el asfalto natural que brotaba espontáneamente de las hendiduras de la tierra y del fondo lacustre, al cual denominaban 'mene'. Con este betún espeso e impermeable calafateaban los maderos de sus embarcaciones de pesca, curaban heridas cutáneas e iluminaban sus chozas ceremoniales mediante antorchas de fuego inextinguible. Para aquellos navegantes ancestrales, el petróleo no era una mercancía cotizada en bolsas de valores bursátiles, sino un elemento sagrado de la naturaleza que la tierra regalaba para sellar la madera contra el agua salobre."
            },
            {
                "type": "narration",
                "text": "La transición hacia la era industrial global comenzó de forma oficial el 31 de julio de 1914 en las colinas de Mene Grande, cuando la empresa Caribbean Petroleum Company logró extraer con éxito crudo comercial del pozo Zumaque I (MG-1). Sin embargo, fue en las calurosas navidades de diciembre de 1922 cuando el destino histórico de Venezuela dio un vuelco irreversible con el legendario reventón del pozo Los Barrosos II (R-4) en el campo La Rosa, en Cabimas. Una columna ensordecedora de gas y petróleo negro pulverizado se elevó a más de cuarenta metros de altura, arrojando a la atmósfera más de cien mil barriles diarios durante nueve días continuos. El rugido del pozo retumbó en las redacciones de prensa de todo el mundo occidental: Venezuela no era un modesto exportador agrícola, sino un emporio energético de proporciones colosales."
            },
            {
                "type": "narration",
                "text": "A partir de aquel instante telúrico, las grandes corporaciones extranjeras —la Royal Dutch Shell, la Creole Petroleum filial de Standard Oil y la Gulf Oil— se abalanzaron sobre el país en busca de concesiones de explotación. Don Cipriano Valera, anciano testigo de aquellos años de mutación febril en las orillas del lago, relata cómo miles de campesinos abandonaron sus conucos de yuca y sus sembradíos andinos de café para trabajar como peones en las torres de perforación: 'El olor a cacao maduro fue devorado por el hedor a gas y gasóleo. La gente creía que el dinero brotaba de las cañerías del pozo sin necesidad de sudar la tierra con el arado; todos queríamos ser asalariados del taladro'."
            },
            {
                "type": "narration",
                "text": "El dictador Juan Vicente Gómez, quien gobernó el país con mano de hierro durante casi tres décadas, administró la entrega de las concesiones a través de un círculo íntimo de compadres y allegados, enriqueciendo a la élite cortesana mientras las arcas públicas comenzaban a percibir fabulosas sumas por concepto de regalías e impuestos aduaneros. El ingeniero Briceño, especialista en historia de los hidrocarburos, explica que aquel modelo alumbró un fenómeno político y sociológico sin equivalentes en la región: el nacimiento del 'petroestado'. A diferencia de los Estados republicanos tradicionales que dependían de los tributos de sus ciudadanos para sostener el presupuesto nacional, el Estado venezolano se convirtió en el propietario supremo de la renta del subsuelo, transformándose en el gran benefactor y distribuidor de la riqueza colectiva."
            },
            {
                "type": "narration",
                "text": "Frente a los peligros evidentes de este esquema parasitario, intelectuales visionarios alzaron su voz de alarma. En julio de 1936, en un memorable editorial del diario caraqueño *Ahora*, el escritor y jurista Arturo Uslar Pietri acuñó la consigna que marcaría el debate nacional durante todo el siglo: 'Sembrar el petróleo'. Uslar Pietri advertía con clarividencia que los hidrocarburos eran un recurso mineral no renovable y que la única salvación económica de Venezuela residía en reinvertir cada bolívar de la renta extractiva en tecnificar el campo abandonado, construir presas hidroeléctricas, erigir escuelas rurales y forjar un tejido industrial sólido que sobreviviera al inevitable agotamiento de los yacimientos."
            },
            {
                "type": "narration",
                "text": "A pesar de las advertencias intelectuales, el rentismo permeó profundamente la mentalidad colectiva. El país multiplicó su red hospitalaria, pavimentó autopistas que cruzaban montañas y fundó centros universitarios de primer nivel, pero descuidó su soberanía alimentaria, acostumbrándose a importar desde alimentos básicos hasta automóviles de lujo con petrodólares baratos. María Chiquinquirá, profesora emérita en Maracaibo, concluye mientras contempla las viejas torres de balancines en el lago: 'El pozo Zumaque I nos regaló una modernidad deslumbrante y acelerada, pero también nos inoculó la ilusión peligrosa de la riqueza sin esfuerzo. Recordar nuestra historia petrolera es el primer paso para comprender que el verdadero porvenir de una nación no duerme bajo el lodo de los pozos, sino en el talento, la ciencia y el trabajo laborioso de sus gentes'."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué uso daban los indígenas añú y wayúu al asfalto natural ('mene') antes de la llegada de las compañías petroleras?",
                        "options": [
                            "Calafateaban la madera de sus canoas de pesca, curaban afecciones de la piel e iluminaban chozas ceremoniales.",
                            "Lo refinaban en laboratorios químicos para producir combustible de aviación.",
                            "Lo vendían como moneda de cambio con los navegantes holandeses de Curazao.",
                            "Lo utilizaban para teñir tejidos de algodón en telares mecánicos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 explica que los pueblos originarios usaban el 'mene' natural para impermeabilizar barcas, sanar heridas y hacer antorchas."
                    },
                    {
                        "question": "¿Qué acontecimiento histórico convirtió a Venezuela en un foco mundial de la industria petrolera en diciembre de 1922?",
                        "options": [
                            "El colosal reventón del pozo Los Barrosos II en Cabimas, que arrojó más de cien mil barriles diarios durante nueve días.",
                            "La firma de la Constitución democrática de Caracas.",
                            "El descubrimiento de las minas de bauxita en el estado Bolívar.",
                            "La expropiación total de los taladros por parte de pescadores locales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 relata el histórico reventón del pozo Los Barrosos II en diciembre de 1922, que atrajo el interés de los grandes consorcios energéticos mundiales."
                    },
                    {
                        "question": "¿En qué consistía la advertencia de Arturo Uslar Pietri resumida en la frase 'Sembrar el petróleo'?",
                        "options": [
                            "En reinvertir urgentemente la renta petrolera en educación, infraestructura e industrialización agrícola para evitar ser una economía dependiente del crudo.",
                            "En enterrar los barriles de petróleo para esperar que aumentara el precio mundial.",
                            "En entregar todos los pozos a consorcios exclusivamente privados extranjeros.",
                            "En sustituir a los campesinos por ingenieros químicos en las plantaciones."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 detalla la célebre tesis de Uslar Pietri de 1936: sembrar el petróleo implicaba transformar el recurso agotable en capacidad productiva, educativa e industrial sostenible."
                    }
                ]
            }
        }
    }

    story_ven1_03 = {
        "id": "b2-venezuelapetroleo-03",
        "title": "La Ciudad Universitaria de Caracas: Utopía moderna y síntesis de las artes",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica arquitectónica y estética de nivel B2 sobre el campus central de la Universidad Central de Venezuela (UCV): el genio visionario de Carlos Raúl Villanueva, la integración de la escultura y el muralismo de vanguardia con el concreto tropical, la acústica prodigiosa del Aula Magna con las Nubes de Calder y su consagración por la UNESCO como Patrimonio de la Humanidad.",
        "characters": [
            "Maestro Carlos Raúl Villanueva",
            "Marta",
            "Profesor Arismendi"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Bajo la luz dorada y limpia del trópico caraqueño, los corredores cubiertos de la Ciudad Universitaria de Caracas se extienden como una partitura musical trazada en hormigón armado, vegetación exuberante y viento fresco. Diseñado y construido entre las décadas de 1940 y 1960 bajo la dirección magistral del arquitecto Carlos Raúl Villanueva, el campus principal de la Universidad Central de Venezuela (UCV) representa uno de los momentos estelares de la arquitectura moderna del siglo veinte en todo el planeta. En sus doscientas hectáreas de superficie, Villanueva no se limitó a proyectar facultades universitarias convencionales con aulas cerradas; concibió una auténtica 'utopía espacial' donde la ciencia pedagógica, la luz tropical y las más audaces expresiones del arte contemporáneo se fundieron en un organismo armónico e indisoluble."
            },
            {
                "type": "narration",
                "text": "El núcleo filosófico de este prodigio arquitectónico fue bautizado por su propio creador como la **'Síntesis de las Artes Mayores'**. Villanueva estaba convencido de que la obra de arte no debía permanecer confinada en museos elitistas ni en colecciones privadas de acceso restringido, sino que debía dialogar diariamente con los estudiantes, profesores y transeúntes comunes. Para materializar esta visión democrática y universal, convocó a los principales maestros de la vanguardia abstracta internacional: Alexander Calder, Fernand Léger, Victor Vasarely, Jean Arp y Henri Laurens, articulándolos con glorias fundamentales del arte venezolano como Francisco Narváez, Mateo Manaure, Armando Barrios y Pascual Navarro. Más de un centenar de esculturas monumentales, murales de mosaico veneciano y vidrieras polícromas fueron concebidos no como simples adornos agregados a las paredes, sino como elementos estructurales de la propia experiencia arquitectónica."
            },
            {
                "type": "narration",
                "text": "El corazón palpitante de este conjunto monumental es, sin duda alguna, el Aula Magna. Al franquear sus puertas solemnes, el visitante experimenta una sensación sobrecogedora: flotando en el techo abovedado de la gran sala de conciertos se despliegan las veintidós 'Nubes' de Alexander Calder, discos y elipses gigantescas de madera multilaminada pintadas en tonos puros de negro, amarillo, rojo y azul cobalto. Aquellas esculturas suspendidas en el aire no solo encarnan una obra maestra de arte cinético flotante, sino que resuelven de forma prodigiosa la acústica del recinto: calculadas en colaboración con los ingenieros de la firma estadounidense Bolt, Beranek and Newman, las nubes absorben y redirigen las ondas sonoras con tal precisión milimétrica que el auditorio está catalogado entre los cinco recintos de mejor acústica sinfónica del mundo entero."
            },
            {
                "type": "narration",
                "text": "Asimismo, la arquitectura de Villanueva ofreció una respuesta brillante a los desafíos del clima tropical. Frente a los modelos de rascacielos acristalados anglosajones que demandaban costosísimos sistemas de aire acondicionado artificial, el maestro venezolano ideó las célebres 'celosías' de hormigón perforado y los pasillos techados al aire libre. Estas pantallas porosas filtran la inclemente radiación solar creando una penumbra fresca y relajante, al tiempo que permiten que las corrientes de aire procedentes del cerro El Ávila circulen libremente por los corredores, patios interiores y jardines sombreados por centenarios chaguaramos, ceibas y jabillos."
            },
            {
                "type": "narration",
                "text": "Marta, una joven estudiante de artes visuales que dibuja en su libreta el emblemático reloj tridimensional de la Plaza del Rectorado junto al veterano profesor Arismendi, contempla con admiración las figuras policromadas del mural de Fernand Léger. 'Caminar por este campus para asistir a una clase de matemáticas o filosofía significa convivir cotidianamente con la belleza más elevada de la humanidad', comenta Marta conmovida. El profesor Arismendi asiente mientras recuerda los debates políticos y estudiantiles que resonaron en esa misma plaza: 'Villanueva nos demostró que una universidad libre y plural requería un espacio físico que respirara libertad, dignidad y audacia intelectual'."
            },
            {
                "type": "narration",
                "text": "En el año 2000, la UNESCO inscribió a la Ciudad Universitaria de Caracas en la lista del Patrimonio Cultural de la Humanidad, consagrándola formalmente como una obra maestra del genio creador humano y el más puro ejemplo de la arquitectura moderna tropical en América Latina. A pesar de los desafíos presupuestarios y el desgaste del tiempo contemporáneo, la UCV continúa erguida en el corazón de Caracas como un faro de resistencia civil y sabiduría estética, demostrando que cuando el arte y la arquitectura se ponen al servicio de la educación popular, el hormigón armado es capaz de transformarse en poesía inmortal para todas las generaciones."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué concepto estético fundamental guio a Carlos Raúl Villanueva en el diseño de la Ciudad Universitaria de Caracas?",
                        "options": [
                            "La Síntesis de las Artes Mayores, integrando pintura, escultura y arquitectura en la vida cotidiana universitaria.",
                            "El retorno al barroco colonial andaluz de arcos de medio punto.",
                            "La imitación estricta de las fábricas textiles industriales de Mánchester.",
                            "La prohibición de colocar obras de arte plásticas en los espacios públicos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que el concepto central fue la Síntesis de las Artes Mayores, integrando las vanguardias plásticas internacionales y nacionales con el espacio arquitectónico."
                    },
                    {
                        "question": "¿Qué función dual y prodigiosa cumplen las 'Nubes' de Alexander Calder instaladas en el techo del Aula Magna?",
                        "options": [
                            "Son esculturas flotantes de vanguardia y paneles de calibración acústica que sitúan al auditorio entre los mejores del planeta.",
                            "Eran compuertas secretas de escape en caso de incendio fortuito.",
                            "Servían de soporte para colgar reflectores de televisión comercial.",
                            "Eran depósitos herméticos de agua de lluvia recolectada."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 describe que las Nubes de Calder operan como esculturas cinéticas aéreas y como difusores acústicos calculados científicamente para una resonancia perfecta."
                    },
                    {
                        "question": "¿De qué manera Villanueva resolvió las altas temperaturas tropicales de Caracas en el diseño de los edificios de la UCV?",
                        "options": [
                            "Mediante celosías de hormigón perforado y pasillos cubiertos que generan sombra y favorecen la ventilación cruzada natural.",
                            "Instalando enormes aparatos mecánicos de refrigeración en todas las áreas abiertas.",
                            "Pintando todos los techos con pintura negra para atraer el calor.",
                            "Construyendo todas las aulas en túneles subterráneos sin luz solar."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 detalla el uso de celosías perforadas y corredores techados abiertos que filtran el sol y aprovechan la brisa del Ávila para refrescar naturalmente."
                    }
                ]
            }
        }
    }

    story_ven1_04 = {
        "id": "b2-venezuelapetroleo-04",
        "title": "El movimiento y el color: El cinetismo venezolano y la siembra musical",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica estética y cultural de nivel B2 sobre las grandes vanguardias venezolanas de la segunda mitad del siglo XX: las exploraciones ópticas y lumínicas de Carlos Cruz-Diez, los Penetrables espaciales de Jesús Rafael Soto, la consagración del arte público y la epopeya pedagógica de El Sistema fundado por el maestro José Antonio Abreu.",
        "characters": [
            "Carlos Cruz-Diez",
            "Jesús Rafael Soto",
            "Maestro Abreu",
            "Gabriela"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A partir de la década de 1950, la escena cultural venezolana experimentó una explosión de creatividad de vanguardia que deslumbró a las capitales artísticas del mundo. En un país que se modernizaba a pasos agigantados gracias a los recursos del petróleo, una generación brillante de artistas visuales decidió romper definitivamente con el realismo pictórico figurativo y el paisajismo tradicional para sumergirse en una aventura revolucionaria: capturar el movimiento puro, la luz y la inestabilidad de la percepción humana. A la cabeza de aquella corriente vanguardista descollaron dos figuras colosales del arte contemporáneo universal: el caraqueño Carlos Cruz-Diez y el guayanés Jesús Rafael Soto, auténticos profetas de la revolución del arte cinético y óptico."
            },
            {
                "type": "narration",
                "text": "Para Carlos Cruz-Diez, el color no era una pasta densa untada de forma estática sobre una tela inerte, ni una simple propiedad adherida a los objetos cotidianos; era un acontecimiento físico autónomo que se producía en el espacio aéreo entre la obra y los ojos del espectador. A través de sus célebres *Fisicromías*, *Inducciones cromáticas* y *Cromosaturaciones*, Cruz-Diez diseñó estructuras ópticas mediante finísimas láminas de color superpuestas que mutaban de tono y brillo a medida que el transeúnte caminaba frente a ellas. El artista liberó al color de la forma geométrica fija, transformándolo en una experiencia viva y efímera: el espectador dejaba de ser un receptor pasivo para convertirse en el coproductor indispensable del fenómeno artístico."
            },
            {
                "type": "narration",
                "text": "Simultáneamente, Jesús Rafael Soto exploraba los misterios del espacio cósmico y la vibración óptica. Nacido en Ciudad Bolívar a orillas del majestuoso río Orinoco, Soto trascendió los límites del cuadro tradicional inventando sus legendarios *Penetrables*. Estas obras monumentales consistían en densos bosques de varillas flexibles de nylon o finos tubos de aluminio suspendidos verticalmente desde una estructura superior, formando un cubo inmenso de color transparente en medio del espacio público o la sala de exposición. Al adentrarse físicamente en el interior del Penetrable, el público sentía cómo los límites de su propio cuerpo se desvanecían entre la lluvia de filamentos oscilantes, experimentando la materia como una vibración de energía pura en constante movimiento."
            },
            {
                "type": "narration",
                "text": "Ambos creadores compartían un imperativo ético democratizador: el arte debía abandonar la reclusión silenciosa de las galerías privadas para ocupar plazas, autopistas, estaciones de transporte subterráneo y terminales aéreas. En Caracas, la colosal *Esfera Caracas* de Soto —una esfera naranja brillante compuesta por varillas suspendidas al costado de la autopista Francisco Fajardo— se convirtió en el faro visual predilecto de millones de conductores cotidianos. Y en el Aeropuerto Internacional de Maiquetía, la *Cromointerferencia de color aditivo* de Cruz-Diez cubrió miles de metros cuadrados de piso, convirtiéndose en el símbolo sentimental más profundo de los viajes, las despedidas y los anhelos de retorno de todo el pueblo venezolano."
            },
            {
                "type": "narration",
                "text": "En ese mismo contexto de efervescencia modernista, en 1975 floreció otra de las mayores hazañas culturales del continente: la fundación del Sistema Nacional de Orquestas y Coros Juveniles e Infantiles de Venezuela ('El Sistema'), ideado por el maestro y economista José Antonio Abreu. Con apenas once muchachos ensayando en un garaje de Caracas, Abreu formuló una tesis tan revolucionaria como humanista: la orquesta sinfónica no debía ser un privilegio para familias acomodadas, sino un aula de dignidad, disciplina colectiva y salvación social para niños y jóvenes de los sectores más vulnerables de la sociedad. A través de la práctica musical compartida, cientos de miles de niños de barriadas humildes cambiaron las armas y el desamparo por violines, chelos y clarinetes, asombrando al mundo en escenarios de Salzburgo, Londres y Viena bajo la batuta de directores geniales formados en sus filas, como Gustavo Dudamel."
            },
            {
                "type": "narration",
                "text": "Gabriela, una joven violonchelista de diecisiete años que ensaya la Quinta Sinfonía de Chaikovski en el Centro de Acción Social por la Música mientras contempla una serigrafía cinética en el vestíbulo, sintetiza con orgullo este legado: 'Soto y Cruz-Diez nos enseñaron que el arte se construye en movimiento con la mirada de quien camina; el maestro Abreu nos enseñó que una orquesta es una comunidad donde nadie vale más que el conjunto armónico de todos. Ambos mundos confirman que Venezuela es tierra de luz, sonido y esperanza indestructible ante cualquier tempestad'."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué manera concebía Carlos Cruz-Diez el fenómeno del color en sus obras de arte cinético?",
                        "options": [
                            "Como un acontecimiento autónomo y cambiante que ocurre en el espacio en interacción con el movimiento del espectador.",
                            "Como un pigmento estático que debe copiar exactamente la naturaleza muerta.",
                            "Como una propiedad reservada exclusivamente para pinturas religiosas medievales.",
                            "Como una fórmula matemática sin ninguna relación con la visión humana."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que para Cruz-Diez el color es un acontecimiento efímero y autónomo que muta con la mirada y el desplazamiento del espectador."
                    },
                    {
                        "question": "¿En qué consistían los célebres 'Penetrables' ideados por el artista venezolano Jesús Rafael Soto?",
                        "options": [
                            "En densos bosques de varillas flexibles suspendidas en el espacio que el público atraviesa físicamente sintiendo la disolución de la materia.",
                            "En túneles de hormigón armado completamente oscuros y cerrados.",
                            "En cuadros figurativos protegidos por gruesos cristales blindados.",
                            "En pirámides de piedra talladas con inscripciones antiguas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 describe los Penetrables como estructuras transitables de varillas de nylon suspendidas donde el espectador entra corporalmente en la obra."
                    },
                    {
                        "question": "¿Cuál era la premisa social y pedagógica central del maestro José Antonio Abreu al crear El Sistema de orquestas?",
                        "options": [
                            "Convertir la práctica orquestal colectiva en una herramienta de inclusión social, rescate humano y dignidad para niños de sectores vulnerables.",
                            "Seleccionar únicamente a niños de familias millonarias para viajar al extranjero.",
                            "Eliminar la enseñanza de la música clásica y sustituirla por marchas militares.",
                            "Cobrar costosas matrículas para financiar teatros privados en la capital."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 detalla la visión de Abreu: la música sinfónica colectiva como modelo de rescate social, disciplina comunitaria y excelencia accesible a todos los estratos."
                    }
                ]
            }
        }
    }

    story_ven1_05 = {
        "id": "b2-venezuelapetroleo-05",
        "title": "La Venezuela Saudita: La embriaguez del petrodólar y las fisuras del rentismo",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociopolítica y económica de nivel B2 sobre los años del petrodólar desbordado en Venezuela: el embargo petrolero de 1973, la bonanza consumista de la 'Venezuela Saudita', el espejismo del '¡Dame dos!' en Miami, la distorsión estructural de la enfermedad holandesa y el despertar abrupto del 'Viernes Negro' de 1983.",
        "characters": [
            "Don Bernardo Morillo",
            "Doctora Albarrán",
            "Héctor"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia el último tercio del siglo veinte, el destino de Venezuela pareció colmarse de una abundancia material casi legendaria. A raíz de la guerra árabe-israelí de Yom Kipur en 1973 y el consiguiente embargo decretado por los países miembros de la OPEP —organización que la propia diplomacia venezolana había cofundado con orgullo en 1960 de la mano de Juan Pablo Pérez Alfonzo—, los precios internacionales del crudo se cuadruplicaron en cuestión de meses. Las arcas fiscales de la república se vieron súbitamente anegadas por un torrente colosal de petrodólares que multiplicó por cuatro el presupuesto del Estado de la noche a la mañana. La prensa internacional, fascinada ante el despliegue de riqueza de aquella nación caribeña, no tardó en acuñar una denominación que resumía el espíritu triunfalista de la época: la **'Venezuela Saudita'**."
            },
            {
                "type": "narration",
                "text": "Durante aquellos años de embriaguez financiera, bajo el primer mandato presidencial de Carlos Andrés Pérez y la histórica nacionalización de la industria petrolera que dio origen a la estatal PDVSA en 1976, Caracas se consagró como la capital del hedonismo y el cosmopolitismo suramericano. El bolívar disfrutaba de una solidez cambiaria inquebrantable frente al dólar estadounidense (tasado a una paridad casi inamovible de 4,30 bolívares por dólar), lo que otorgó a las clases medias y altas un poder adquisitivo extraordinario. Se levantaron los centros comerciales más lujosos de la región, los restaurantes de alta gastronomía francesa e italiana abarrotaban sus mesas todas las noches y la sociedad se habituó a consumir con desenfado whisky escocés de dieciocho años y los automóviles importados de mayor cilindrada del mercado automotor."
            },
            {
                "type": "narration",
                "text": "Aquel delirio consumista tuvo su manifestación sociológica más pintoresca en los vuelos diarios que despegaban repletos desde Maiquetía hacia el sur de la Florida. En los centros comerciales y tiendas departamentales de Miami, los turistas venezolanos se hicieron célebres por su compulsión de compra desenfrenada, sintetizada en una frase inmortal que retrató la arrogancia de la bonanza: '¡Está barato, dame dos!'. Familias enteras llenaban maletas gigantescas con ropa de marca, televisores a color y electrodomésticos de última generación, aprovechando una tasa de cambio sobrevalorada que hacía que comprar en el exterior resultara insólitamente más económico que adquirir cualquier producto manufacturado en territorio nacional."
            },
            {
                "type": "narration",
                "text": "Don Bernardo Morillo, veterano comerciante que regentó una ferretería en el centro de Caracas durante aquellos años dorados, dialoga con su nieto Héctor sobre el espejismo que envolvía a la sociedad: 'Creíamos que la fiesta del petrodólar duraría mil años; que éramos un pueblo bendecido por la providencia al que le correspondía gastar sin pensar en el ahorro. Quien hablaba de prudencia fiscal o de cultivar la tierra era tildado de retrógrado o pesimista. Nadie quería sembrar tomates ni producir acero cuando era infinitamente más rápido importar todo en barcos mercantes pagados con la factura petrolera'."
            },
            {
                "type": "narration",
                "text": "Detrás de aquella fachada resplandeciente de abundancia se incubaba, no obstante, una severa patología macroeconómica conocida por los especialistas como la **'enfermedad holandesa'**. La doctora Albarrán, destacada economista e investigadora universitaria, explica que el aluvión indiscriminado de divisas petroleras sobrevaluó artificialmente la moneda nacional, aniquilando la competitividad de las fábricas locales y empujando a la quiebra definitiva a miles de agricultores en el campo. El Estado, embriagado por ingresos que parecían inagotables, no solo gastó hasta el último centavo de la renta corriente, sino que contrató billonarios préstamos con la banca internacional privada, disparando la deuda externa a niveles insostenibles bajo el supuesto ilusorio de que el barril de petróleo jamás detendría su escalada de precios."
            },
            {
                "type": "narration",
                "text": "El despertar de la borrachera fue brutal e inevitable. A comienzos de la década de 1980, una sobreoferta mundial de crudo derrumbó las cotizaciones internacionales del hidrocarburo, dejando al Estado venezolano en la incapacidad absoluta de cumplir los pagos de su exorbitante deuda externa. El 18 de febrero de 1983 —bautizado en la memoria colectiva como el **'Viernes Negro'**—, el gobierno se vio forzado a suspender la libre convertibilidad del bolívar y decretar una traumática devaluación monetaria. Aquel día se desmoronó el mito de la prosperidad perpetua garantizada por el subsuelo. La Venezuela Saudita quedó atrás como un sueño lejano y doloroso, legando al país una profunda lección histórica que todavía resuena en el debate contemporáneo: ninguna riqueza que brote de las entrañas de la tierra puede sustituir a la disciplina del trabajo productivo, la diversificación económica y el pacto ético de una sociedad verdaderamente creadora."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué factor geopolítico internacional desató la gigantesca bonanza petrolera de la 'Venezuela Saudita' en 1973?",
                        "options": [
                            "La guerra de Yom Kipur y el embargo petrolero de la OPEP que cuadruplicaron los precios del crudo en el mercado global.",
                            "La invención del motor de agua que sustituyó a los hidrocarburos.",
                            "Un tratado de libre comercio exclusivo firmado con la Unión Soviética.",
                            "El descubrimiento de yacimientos gigantescos de carbón en los Andes."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 detalla que el conflicto en Oriente Medio y el embargo de la OPEP multiplicaron los precios internacionales del crudo, inundando de petrodólares a Venezuela."
                    },
                    {
                        "question": "¿En qué consistía la patología económica denominada 'enfermedad holandesa' que aquejó a Venezuela durante la bonanza?",
                        "options": [
                            "En la sobrevaloración de la moneda nacional por el auge exportador del crudo, lo que abarató las importaciones y destruyó el agro y la industria local.",
                            "En una epidemia de fiebre amarilla importada por comerciantes de los Países Bajos.",
                            "En el cierre forzoso de todos los puertos marítimos y aeropuertos comerciales.",
                            "En la negativa de los países europeos a comprar petróleo latinoamericano."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 define la enfermedad holandesa: la abundancia de divisas petroleras apreció la moneda, haciendo baratas las importaciones y quebrando la producción nacional."
                    },
                    {
                        "question": "¿Qué suceso histórico ocurrido el 18 de febrero de 1983 marcó el fin traumático de la era del '4,30'?",
                        "options": [
                            "El 'Viernes Negro', cuando el gobierno suspendió la convertibilidad del bolívar y decretó una severa devaluación monetaria.",
                            "La nacionalización de las empresas automotrices en Caracas.",
                            "La promulgación de una ley que prohibía viajar al exterior a los ciudadanos.",
                            "La inundación total de los campos petroleros del lago de Maracaibo."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 describe el 'Viernes Negro' de 1983, fecha en que la caída de los ingresos del crudo obligó a poner fin a la estabilidad cambiaria y devaluar el bolívar."
                    }
                ]
            }
        }
    }

    # Consolidated Story for Regional Unit 15 (~700 words, strictly 650-825 words)
    story_ven1_capstone = {
        "id": "b2-venezuelapetroleo-consolidation",
        "title": "La modernidad petrolera: Luces y sombras de la utopía venezolana",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Gran crónica de consolidación de nivel B2 sobre el siglo petrolero y la modernidad en Venezuela: la imponente silueta del Waraira Repano sobre el valle de Caracas, el impacto fundacional de los pozos Zumaque I y Barroso II, la vanguardia arquitectónica de Villanueva en la UCV, la magia óptica de Soto y Cruz-Diez, el rescate social de El Sistema de orquestas y las lecciones históricas de la bonanza del petrodólar.",
        "characters": [
            "Profesora Valentina Cisneros",
            "Andrés"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Comprender la trayectoria de Venezuela a lo largo del siglo veinte exige adentrarse en la historia más fascinante y paradójica de modernización acelerada que conoció América Latina. En un abrir y cerrar de ojos histórico, una república pastoril y despoblada, cuya frágil economía dependía de las cosechas de café y los caprichos del paludismo en las tierras bajas, se vio catapultada al epicentro de las finanzas y la energía mundial gracias al descubrimiento de los mayores yacimientos de hidrocarburos del hemisferio. Aquel torrente de oro negro que brotó en 1914 en el pozo Zumaque I y estalló con el colosal reventón de Los Barrosos II en 1922 no solo alteró los balances presupuestarios del Estado, sino que reconfiguró de raíz la psicología social, el paisaje urbano y las aspiraciones estéticas de una nación entera."
            },
            {
                "type": "narration",
                "text": "El epicentro de esa prodigiosa mutación civilizatoria fue el estrecho valle de Santiago de León de Caracas. Custodiada por la silueta colosal del cerro El Ávila —el ancestral Waraira Repano de los indígenas caribes que separa a la metrópoli del mar Caribe con su muralla esmeralda—, la capital se transformó en un laboratorio arquitectónico de vanguardia universal. Las viejas casonas coloniales con patios de geranios dieron paso a vertiginosas autopistas de concreto, rascacielos vanguardistas y audaces soluciones de infraestructura que desafiaban la gravedad de las pendientes tropicales. Caracas encarnó la convicción colectiva de que el porvenir había desembarcado para siempre en sus calles luminosas."
            },
            {
                "type": "narration",
                "text": "La manifestación suprema de aquel espíritu visionario fue la Ciudad Universitaria de Caracas, concebida por el genio arquitectónico de Carlos Raúl Villanueva y consagrada con justicia como Patrimonio de la Humanidad. En sus aulas y corredores abiertos, protegidos del sol ardiente por celosías de hormigón que dejaban circular la brisa pura de la montaña, Villanueva materializó la utopía de la Síntesis de las Artes Mayores. El Aula Magna, con las legendarias Nubes Flotantes de Alexander Calder suspendidas en el cielo raso, demostró al planeta que la ingeniería acústica más rigurosa podía dialogar en perfecta hermandad con la escultura cinética, convirtiendo el espacio del saber en una experiencia estética accesible a todos los ciudadanos."
            },
            {
                "type": "narration",
                "text": "Esa misma vocación de vanguardia universal impulsó las indagaciones ópticas de Jesús Rafael Soto y Carlos Cruz-Diez. Al liberar al color de la superficie plana del lienzo y crear los interactivos Penetrables y las mutantes Fisicromías, los artistas venezolanos colocaron al ser humano en el centro del fenómeno plástico: el movimiento y la percepción se convirtieron en el lenguaje de una sociedad dinámica. Y cuando en 1975 el maestro José Antonio Abreu fundó El Sistema Nacional de Orquestas Juveniles, demostró que la música sinfónica no era un entretenimiento ornamental, sino una trinchera inigualable de salvación comunitaria que arrebató a millones de niños humildes de las garras de la exclusión para consagrarlos en maestros de la armonía colectiva."
            },
            {
                "type": "narration",
                "text": "Sin embargo, aquel deslumbrante edificio de modernidad cargaba con una peligrosa debilidad estructural: el rentismo petrolero. El espejismo de la 'Venezuela Saudita' en los años setenta, con su fiebre consumista de bienes importados y su desdén por la producción agraria nacional, olvidó la lúcida profecía de Arturo Uslar Pietri de 'sembrar el petróleo'. La sobrevaloración cambiaria y el endeudamiento público desembocaron en el colapso del 'Viernes Negro' de 1983, recordándole dolorosamente a la sociedad que ningún recurso del subsuelo puede sustituir la perseverancia del trabajo diversificado, la justicia distributiva y la fortaleza institucional."
            },
            {
                "type": "narration",
                "text": "La profesora Valentina Cisneros, guiando a su alumno Andrés por los pasillos cubiertos de la UCV mientras el sol poniente enciende las celosías de hormigón, resume este siglo de búsquedas y contrastes: 'Venezuela vivió en el siglo veinte la tentación de creer que la riqueza era un milagro que manaba de los pozos; pero también nos legó a Villanueva, a Soto, a Cruz-Diez y a millones de jóvenes orquestistas que supieron transformar la materia en luz y belleza trascendente'. En esa síntesis fecunda entre el aprendizaje de los errores económicos y la gloria de sus conquistas culturales late la verdadera fuerza de Venezuela, un país cuya mayor riqueza jamás descansó bajo el lodo de sus pozos, sino en el corazón noble, solidario y luminoso de su pueblo ante la historia."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cómo describe el texto la transformación económica de Venezuela entre principios y mediados del siglo veinte?",
                        "options": [
                            "Como una acelerada mutación que pasó de una economía rural basada en el café a un petroestado moderno e industrializado.",
                            "Como una caída drástica en la producción minera que obligó al retorno de la agricultura primitiva.",
                            "Como un proceso lento y sin consecuencias apreciables en la vida urbana de la capital.",
                            "Como una transición exclusiva hacia el turismo ecológico de playa."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 explica que el descubrimiento del petróleo convirtió rápidamente a una república pastoril en un emporio energético global."
                    },
                    {
                        "question": "¿Qué obra arquitectónica ejemplifica de manera suprema la integración del arte de vanguardia con el espacio universitario en Caracas?",
                        "options": [
                            "La Ciudad Universitaria de Caracas diseñada por Carlos Raúl Villanueva, con el Aula Magna y las Nubes de Calder.",
                            "El puerto marítimo colonial de La Guaira construido en piedra caliza.",
                            "Las antiguas casas de hacienda cafetalera del siglo dieciocho.",
                            "Los centros comerciales construidos durante la bonanza del petrodólar."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 resalta la Ciudad Universitaria de Villanueva y el Aula Magna como la cima de la síntesis entre arte y arquitectura moderna."
                    },
                    {
                        "question": "¿Cuál es la lección histórica fundamental que dejó el colapso de la 'Venezuela Saudita' y el 'Viernes Negro' de 1983?",
                        "options": [
                            "Que la riqueza minera de una nación es insostenible si no se reinvierte en diversificación económica, trabajo productivo e instituciones sólidas.",
                            "Que un país debe evitar a toda costa la construcción de universidades y orquestas sinfónicas.",
                            "Que las crisis financieras internacionales nunca afectan a los países exportadores de crudo.",
                            "Que las monedas latinoamericanas deben mantenerse fijas mediante subsidios permanentes."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 subraya que la dependencia exclusiva de la renta petrolera sin diversificación ni trabajo productivo condujo inevitablemente a la crisis."
                    }
                ]
            }
        }
    }

    # Write all regional stories
    write_json(f"stories/world/b2/{r1}.json", story_ven1_01)
    write_json(f"stories/world/b2/{r2}.json", story_ven1_02)
    write_json(f"stories/world/b2/{r3}.json", story_ven1_03)
    write_json(f"stories/world/b2/{r4}.json", story_ven1_04)
    write_json(f"stories/world/b2/{r5}.json", story_ven1_05)
    write_json(f"stories/world/b2/{rc_con}.json", story_ven1_capstone)
    write_json(f"stories/world/b2/{r_unit}.json", story_ven1_capstone)

    # Lessons for Regional Unit 15
    write_json(f"lessons/b2/{r1}.json", {
        "id": "lesson.b2.venezuelapetroleo.01",
        "title": "La cordillera de la Costa y el valle de Caracas",
        "level": "B2",
        "goal": "Examine the physical geography of Caracas, the tectonic coastal range, and the tutelary presence of El Ávila (Waraira Repano).",
        "grammar": "geografía orográfica, toponimia indígena y fisonomía urbana caraqueña",
        "sections": [
            {"type": "goal", "items": [
                "Analyze the ecological and cultural significance of the Waraira Repano / El Ávila mountain.",
                "Explore the urban transformation from colonial agricultural valley to mountain megalopolis.",
                "Deploy geographic, orographic, and urban vocabulary (cordillera, valle, litoral, vertiente)."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r1}.json"},
            {"type": "grammar", "ref": f"grammar/b2/{r1}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{r1}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{r1}-ex.json", "exerciseRefs": [f"{r1}.ex01", f"{r1}.ex02", f"{r1}.ex03", f"{r1}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{r1}-ex.json", "exerciseRefs": [f"{r1}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{r1}-ex.json", "exerciseRefs": [f"{r1}.ex06"]}
        ]
    })

    write_json(f"lessons/b2/{r2}.json", {
        "id": "lesson.b2.venezuelapetroleo.02",
        "title": "El pozo Zumaque I y el nacimiento del petroestado",
        "level": "B2",
        "goal": "Investigate the historic oil strikes of Zumaque I (1914) and Los Barrosos II (1922) and the emergence of the rentier state in Venezuela.",
        "grammar": "historiografía económica de los hidrocarburos y teoría del petroestado",
        "sections": [
            {"type": "goal", "items": [
                "Trace the transition from agro-exporting nation (coffee and cacao) to global oil power.",
                "Analyze Arturo Uslar Pietri's historical mandate to 'sembrar el petróleo'.",
                "Deploy petroleum and political economy vocabulary (yacimiento, concesión, rentismo, hidrocarburo)."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r2}.json"},
            {"type": "grammar", "ref": f"grammar/b2/{r2}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{r2}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{r2}-ex.json", "exerciseRefs": [f"{r2}.ex01", f"{r2}.ex02", f"{r2}.ex03", f"{r2}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{r2}-ex.json", "exerciseRefs": [f"{r2}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{r2}-ex.json", "exerciseRefs": [f"{r2}.ex06"]}
        ]
    })

    write_json(f"lessons/b2/{r3}.json", {
        "id": "lesson.b2.venezuelapetroleo.03",
        "title": "Carlos Raúl Villanueva y la Ciudad Universitaria: Utopía moderna",
        "level": "B2",
        "goal": "Explore Carlos Raúl Villanueva's modernist masterpiece (UCV) and the concept of the Synthesis of Major Arts.",
        "grammar": "análisis arquitectónico, acústica de vanguardia y patrimonio moderno de la UNESCO",
        "sections": [
            {"type": "goal", "items": [
                "Examine the architectural integration of tropical brise-soleil, open corridors, and fine arts.",
                "Analyze the acoustic and visual triumph of Alexander Calder's Floating Clouds in the Aula Magna.",
                "Deploy architectural and aesthetic vocabulary (hormigón, celosía, acústica, vanguardia)."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r3}.json"},
            {"type": "grammar", "ref": f"grammar/b2/{r3}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{r3}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{r3}-ex.json", "exerciseRefs": [f"{r3}.ex01", f"{r3}.ex02", f"{r3}.ex03", f"{r3}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{r3}-ex.json", "exerciseRefs": [f"{r3}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{r3}-ex.json", "exerciseRefs": [f"{r3}.ex06"]}
        ]
    })

    write_json(f"lessons/b2/{r4}.json", {
        "id": "lesson.b2.venezuelapetroleo.04",
        "title": "El cinetismo y las vanguardias plásticas: Cruz-Diez y Soto",
        "level": "B2",
        "goal": "Analyze the Venezuelan kinetic art movement of Carlos Cruz-Diez and Jesús Rafael Soto, alongside José Antonio Abreu's El Sistema.",
        "grammar": "teoría estética del arte cinético, percepción óptica y pedagogía musical orquestal",
        "sections": [
            {"type": "goal", "items": [
                "Explore Cruz-Diez's chromatic events and Soto's walk-in interactive Penetrables.",
                "Trace the social mission and global impact of El Sistema Nacional de Orquestas.",
                "Deploy artistic and musicological vocabulary (cinetismo, cromático, penetrable, orquestal)."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r4}.json"},
            {"type": "grammar", "ref": f"grammar/b2/{r4}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{r4}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{r4}-ex.json", "exerciseRefs": [f"{r4}.ex01", f"{r4}.ex02", f"{r4}.ex03", f"{r4}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{r4}-ex.json", "exerciseRefs": [f"{r4}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{r4}-ex.json", "exerciseRefs": [f"{r4}.ex06"]}
        ]
    })

    write_json(f"lessons/b2/{r5}.json", {
        "id": "lesson.b2.venezuelapetroleo.05",
        "title": "La bonanza petrolera y las ilusiones del 'Dakar' suramericano",
        "level": "B2",
        "goal": "Examine the 1970s petrodollar boom ('Venezuela Saudita'), consumerism, the Dutch disease, and the 1983 Black Friday collapse.",
        "grammar": "economía del auge de recursos, sociología del consumo y modismos venezolanos",
        "sections": [
            {"type": "goal", "items": [
                "Analyze the macroeconomic distortions of the Dutch disease and currency overvaluation.",
                "Examine the cultural legacy of 1970s consumerism and the '¡Dame dos!' phenomenon.",
                "Incorporate authentic Venezuelan colloquialisms (pana, chamo, chévere, petrodólar)."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r5}.json"},
            {"type": "grammar", "ref": f"grammar/b2/{r5}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{r5}-voc.json"},
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{r5}-ex.json", "exerciseRefs": [f"{r5}.ex01", f"{r5}.ex02", f"{r5}.ex03", f"{r5}.ex04"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{r5}-ex.json", "exerciseRefs": [f"{r5}.ex05"]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{r5}-ex.json", "exerciseRefs": [f"{r5}.ex06"]}
        ]
    })

    write_json(f"lessons/b2/{rc_con}.json", {
        "id": "lesson.b2.venezuelapetroleo.consolidation",
        "title": "Consolidación: La modernidad petrolera venezolana",
        "level": "B2",
        "goal": "Consolidate regional studies on Venezuela's oil century: modernist architecture, kinetic art, youth orchestras, and rentier political economy.",
        "grammar": "síntesis de estudios regionales venezolanos: petroestado, arquitectura moderna y cinetismo",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize the historical transformation from agro-exporting society to modern petrostate.",
                "Analyze the interplay of avant-garde visual arts, architecture, and public space in Caracas.",
                "Reflect on the socioeconomic lessons of the resource boom and the ongoing dignity of Venezuelan culture."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{rc_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{rc_con}-ex.json", "exerciseRefs": [f"{rc_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Identifico los factores geográficos determinantes del valle de Caracas y el cerro El Ávila.",
                "Comprendo la evolución histórica del petroestado desde Zumaque I hasta la OPEP.",
                "Reconozco el valor universal de la Ciudad Universitaria de Villanueva y las Nubes de Calder.",
                "Valoro las aportaciones mundiales del cinetismo de Soto y Cruz-Diez y de El Sistema orquestal."
            ]}
        ]
    })
    print("Completed LatAm Unit 15 (Venezuela Petróleo) generation!")

    # ----------------------------------------------------
    # 4. Curriculum Registration (curriculum/units/b2.json)
    # ----------------------------------------------------
    b2_units_path = ROOT / "content" / "es-latam" / "curriculum" / "units" / "b2.json"
    with open(b2_units_path, "r", encoding="utf-8") as f:
        b2_units = json.load(f)

    unit_stems_core = [f"{c_unit}-0{i}" for i in range(1, 6)] + [f"{c_unit}-consolidation"]
    unit_stems_reg = [f"{r_unit}-0{i}" for i in range(1, 6)] + [f"{r_unit}-consolidation"]

    existing_core = next((u for u in b2_units if u.get("stems") == unit_stems_core), None)
    if not existing_core:
        b2_units.append({
            "title": "The Imperfect Subjunctive: Forms & Nuances",
            "stems": unit_stems_core,
            "track": "core"
        })

    existing_reg = next((u for u in b2_units if u.get("stems") == unit_stems_reg), None)
    if not existing_reg:
        b2_units.append({
            "title": "Venezuela I: The Oil Century, Modernism & Caracas",
            "stems": unit_stems_reg,
            "track": "regional"
        })

    with open(b2_units_path, "w", encoding="utf-8") as f:
        json.dump(b2_units, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated curriculum/units/b2.json with Unit 15!")

    # ----------------------------------------------------
    # 5. Programmatic Word Count Audit
    # ----------------------------------------------------
    stories = {
        "story_core_15": story_core_15,
        "story_ven1_01": story_ven1_01,
        "story_ven1_02": story_ven1_02,
        "story_ven1_03": story_ven1_03,
        "story_ven1_04": story_ven1_04,
        "story_ven1_05": story_ven1_05,
        "story_ven1_capstone": story_ven1_capstone
    }

    print("\n--- Story Word Count Audit ---")
    all_ok = True
    for name, s in stories.items():
        wc = count_words(s)
        status = "OK (650-825)" if 650 <= wc <= 825 else "OUT OF RANGE"
        print(f"{name:<20}: {wc:4d} words -> {status}")
        if not (650 <= wc <= 825):
            all_ok = False

    if not all_ok:
        raise ValueError("Some stories failed the word count requirement (650-825 words)!")

if __name__ == "__main__":
    run()
