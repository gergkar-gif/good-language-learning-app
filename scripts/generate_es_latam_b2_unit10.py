#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Pair 10:
  - Core Unit 10: Conditionals II: Counterfactuals & Regrets (b2-10)
  - Regional Unit 10: Cuba: Island of Paradox, Revolution, Cinema & Music (b2-cuba)
"""

import json
from pathlib import Path
from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "content" / "es-latam"

def count_words(story_data):
    total = 0
    for p in story_data.get("paragraphs", []):
        total += len(p.get("text", "").split())
    return total

def run():
    # -------------------------------------------------------------------------
    # SKILL REGISTRY & GRAMMAR TITLES
    # -------------------------------------------------------------------------
    skill_reg_path = BASE / "indexes" / "skill-registry.json"
    with open(skill_reg_path, "r", encoding="utf-8") as f:
        skill_reg = json.load(f)

    new_skills = {
        "b2-unit10-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "counterfactuals, past regrets, historical decisions, and critical turning points"
        },
        "condicionales-tercer-tipo-contrafactico": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "third conditional structures with pluperfect subjunctive and compound conditional"
        },
        "pluscuamperfecto-subjuntivo-apodosis": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "pluperfect subjunctive in the apodosis / main clause in literary prose"
        },
        "lamento-reproche-condicional": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "expressions of past regret, reproach, and retrospective complaint"
        },
        "condicionales-pasadas-haber-participio": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "implicit past conditionals with compound infinitive and participle constructions"
        },
        "inversiones-condicionales-de-haber": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "rhetorical inversion and concessive conditionals with pluperfect subjunctive"
        },
        "b2-cuba-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "cuban cultural heritage, history, cinema, music, and contemporary society"
        },
        "cuba-arquitectura-habana-vinales": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "descriptive past aspect and historical architectural synthesis in havana and vinales"
        },
        "cuba-jose-marti-independencia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "political and literary argument in 19th-century cuban independence thought"
        },
        "cuba-revolucion-1959-alfabetizacion": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "counterfactual and causal discourse in the cuban revolution and literacy campaign"
        },
        "cuba-son-nueva-trova-cine": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "cultural analysis, musicology, and cinematographic criticism in cuba"
        },
        "cuba-periodo-especial-economia-diaspora": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "complex concessive and speculative structures regarding the special period and diaspora"
        }
    }

    for k, v in new_skills.items():
        if k not in skill_reg["skills"]:
            skill_reg["skills"][k] = v

    with open(skill_reg_path, "w", encoding="utf-8") as f:
        json.dump(skill_reg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated skill-registry.json")

    grammar_titles_path = BASE / "indexes" / "grammar-titles.json"
    with open(grammar_titles_path, "r", encoding="utf-8") as f:
        grammar_titles = json.load(f)

    new_titles = {
        "condicionales-tercer-tipo-contrafactico": "third conditionals and past counterfactual scenarios",
        "pluscuamperfecto-subjuntivo-apodosis": "pluperfect subjunctive in the main clause",
        "lamento-reproche-condicional": "past regrets and reproaches with conditional structures",
        "condicionales-pasadas-haber-participio": "implicit past conditionals with compound infinitive and participle",
        "inversiones-condicionales-de-haber": "rhetorical inversion and concessive conditions with pluperfect subjunctive",
        "cuba-arquitectura-habana-vinales": "architecture of havana and the viñales cultural landscape",
        "cuba-jose-marti-independencia": "the independence movement and thought of marti in cuba",
        "cuba-revolucion-1959-alfabetizacion": "the cuban revolution and the national literacy campaign",
        "cuba-son-nueva-trova-cine": "traditional son and revolutionary cinema in cuba",
        "cuba-periodo-especial-economia-diaspora": "the special period and contemporary society in cuba"
    }

    for k, v in new_titles.items():
        grammar_titles[k] = v

    with open(grammar_titles_path, "w", encoding="utf-8") as f:
        json.dump(grammar_titles, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated grammar-titles.json")

    # -------------------------------------------------------------------------
    # CORE UNIT 10 (b2-10): Conditionals II: Counterfactuals & Regrets
    # -------------------------------------------------------------------------

    # Lesson 1: b2-10-01 - Períodos condicionales irreales en el pasado
    l1 = "b2-10-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.10.01",
        "lesson": l1,
        "title": "Encrucijadas, desenlaces y decisiones históricas",
        "theme": "Vocabulario de puntos de inflexión y análisis contrafáctico",
        "words": [
            {"lemma": "la encrucijada", "translation": "crossroads, turning point", "pos": "noun"},
            {"lemma": "el desenlace", "translation": "outcome, denouement", "pos": "noun"},
            {"lemma": "irreversible", "translation": "irreversible", "pos": "adjective"},
            {"lemma": "el punto de inflexión", "translation": "inflection point, watershed moment", "pos": "noun"},
            {"lemma": "en retrospectiva", "translation": "in retrospect, with hindsight", "pos": "adverb"},
            {"lemma": "la coyuntura", "translation": "circumstance, juncture", "pos": "noun"},
            {"lemma": "desencadenar", "translation": "to trigger, to unleash", "pos": "verb"},
            {"lemma": "la secuela", "translation": "aftermath, consequence", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.10.01.condicional-tercer-tipo",
        "title": "Períodos condicionales irreales en el pasado (Tercer condicional)",
        "sections": [
            {
                "type": "text",
                "title": "Estructura del tercer condicional contrafáctico",
                "content": "El tercer condicional expresa hipótesis imposibles o no verificadas situadas íntegramente en el pasado. Se construye canónicamente mediante la fórmula: 'Si + pluscuamperfecto de subjuntivo (prótasis), condicional compuesto (apódosis)'. Por ejemplo: 'Si el gobierno hubiera escuchado las advertencias de los expertos, se habría evitado el colapso financiero'."
            },
            {
                "type": "table",
                "title": "Esquema temporal y modal del contrafáctico",
                "rows": [
                    ["Prótasis (condición no cumplida)", "'Si hubieras / hubieses llegado antes...'"],
                    ["Apódosis canónica (resultado irreal)", "'...habríamos alcanzado el tren'"],
                    ["Alternativa de apódosis (registro culto)", "'...hubiéramos alcanzado el tren'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el análisis histórico e interpersonal",
                "items": [
                    {"spanish": "Si los líderes de la oposición hubiesen firmado el acuerdo de paz en 1948, el país se habría ahorrado décadas de conflicto armado.", "english": "If the opposition leaders had signed the peace agreement in 1948, the country would have saved decades of armed conflict."},
                    {"spanish": "Si hubiéramos contado con financiamiento oportuno, el documental se habría estrenado el año pasado.", "english": "If we had had timely financing, the documentary would have premiered last year."},
                    {"spanish": "En retrospectiva, si no se hubiera producido aquella huelga general, los derechos laborales no se habrían consagrado tan pronto.", "english": "In retrospect, if that general strike had not occurred, labor rights would not have been enshrined so soon."}
                ]
            },
            {
                "type": "tip",
                "content": "Tanto la forma en '-ra' ('hubiera sabido') como en '-se' ('hubiese sabido') son perfectamente correctas en la prótasis. Sin embargo, en la apódosis nunca se debe utilizar condicional simple ('habría') si la consecuencia pertenece enteramente al pasado."
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
                    ["la encrucijada", "crossroads, turning point"],
                    ["el desenlace", "outcome, denouement"],
                    ["irreversible", "irreversible"],
                    ["la coyuntura", "circumstance, juncture"]
                ],
                "teaches": ["b2-unit10-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si la cancillería __ las alertas diplomáticas, no se habría desatado la crisis fronteriza. (haber atendido)",
                "answer": "hubiera atendido",
                "english": "If the foreign ministry had heeded the diplomatic alerts, the border crisis would not have broken out.",
                "teaches": ["condicionales-tercer-tipo-contrafactico"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la formulación canónica para una hipótesis contrafáctica irreal referida exclusivamente al pasado?",
                "options": [
                    "Si + pluscuamperfecto de subjuntivo en la condición y condicional compuesto en la consecuencia.",
                    "Si + condicional compuesto en la condición y pluscuamperfecto de indicativo en la consecuencia.",
                    "Si + pretérito indefinido en la condición y condicional simple en la consecuencia."
                ],
                "correct": 0,
                "teaches": ["condicionales-tercer-tipo-contrafactico"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Si", "hubiéramos", "previsto", "la", "crisis,", "habríamos", "tomado", "medidas", "inmediatas."],
                "solution": ["Si", "hubiéramos", "previsto", "la", "crisis,", "habríamos", "tomado", "medidas", "inmediatas."],
                "english": "If we had foreseen the crisis, we would have taken immediate measures.",
                "teaches": ["condicionales-tercer-tipo-contrafactico"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora", "text": "¿Cree usted que la guerra civil de 1891 pudo evitarse?"},
                    {"speaker": "Profesor", "text": "_____"},
                    {"speaker": "Historiadora", "text": "En efecto, la intransigencia mutua precipitó un desenlace irreparable."}
                ],
                "options": [
                    "Si el presidente Balmaceda hubiera pactado con el parlamento, el país se habría evitado un baño de sangre.",
                    "El puerto comercial de Valparaíso exportaba trigo hacia California en barcos veleros.",
                    "Los tratados internacionales se firman siempre en ceremonias solemnes de estado."
                ],
                "correct": 0,
                "teaches": ["condicionales-tercer-tipo-contrafactico"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si las partes hubiesen negociado de buena fe, el desenlace habría sido pacífico.",
                "english": "If the parties had negotiated in good faith, the outcome would have been peaceful.",
                "teaches": ["condicionales-tercer-tipo-contrafactico"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=10,
        title="Períodos condicionales irreales en el pasado",
        goal="Master third conditional counterfactual sentences (si + pluperfect subjunctive, compound conditional) to analyze past historical turning points.",
        grammar_desc="el tercer condicional contrafáctico: si + pluscuamperfecto de subjuntivo + condicional compuesto",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Formulate third conditional sentences referring to unfulfilled past events.",
            "Distinguish the role of the pluperfect subjunctive in protasis vs compound conditional in apodosis.",
            "Deploy historical analysis vocabulary (encrucijada, desenlace, punto de inflexión, coyuntura)."
        ]
    ))

    # Lesson 2: b2-10-02 - El pluscuamperfecto de subjuntivo en la apódosis
    l2 = "b2-10-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.10.02",
        "lesson": l2,
        "title": "Evaluación retrospectiva y rectificación institucional",
        "theme": "Vocabulario de revisión crítica, enmienda y desaciertos",
        "words": [
            {"lemma": "el desacierto", "translation": "mistake, blunder", "pos": "noun"},
            {"lemma": "soslayar", "translation": "to sidestep, to bypass", "pos": "verb"},
            {"lemma": "el menoscabo", "translation": "detriment, impairment", "pos": "noun"},
            {"lemma": "la rectificación", "translation": "rectification, correction", "pos": "noun"},
            {"lemma": "la imprevisión", "translation": "lack of foresight, negligence", "pos": "noun"},
            {"lemma": "prescindir", "translation": "to do without, to dispense with", "pos": "verb"},
            {"lemma": "reivindicar", "translation": "to vindicate, to claim rights", "pos": "verb"},
            {"lemma": "imprudente", "translation": "imprudent, rash", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.10.02.pluscuamperfecto-apodosis",
        "title": "El pluscuamperfecto de subjuntivo en la apódosis",
        "sections": [
            {
                "type": "text",
                "title": "Uso literario y formal de 'hubiera' en la consecuencia",
                "content": "En el español literario, periodístico y formal de América Latina, es sumamente frecuente sustituir el condicional compuesto ('habría sido') por el pluscuamperfecto de subjuntivo en la apódosis ('hubiera sido' o 'hubiese sido'): 'Si hubieras venido ayer, te hubieras enterado de la noticia'. Este uso es plenamente normativo y aporta fluidez estilística."
            },
            {
                "type": "table",
                "title": "Correspondencia de formas en la apódosis",
                "rows": [
                    ["Forma canónica", "'Si hubiéramos sabido el plan, habríamos intervenido'"],
                    ["Forma estilística con 'hubiera'", "'Si hubiéramos sabido el plan, hubiéramos intervenido'"],
                    ["Variante regional culta", "'Si hubiésemos sabido el plan, hubiésemos intervenido'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en editoriales y ensayo",
                "items": [
                    {"spanish": "De haber actuado con templanza, el ministro se hubiera ahorrado semejante humillación parlamentaria.", "english": "Had he acted with restraint, the minister would have spared himself such parliamentary humiliation."},
                    {"spanish": "Si no hubiera mediado la corte suprema, el proceso electoral hubiera terminado en desacato generalizado.", "english": "If the supreme court had not mediated, the electoral process would have ended in widespread defiance."},
                    {"spanish": "Cualquier observador imparcial hubiera llegado a la misma conclusión.", "english": "Any impartial observer would have reached the same conclusion."}
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que la sustitución inversa es estrictamente incorrecta: nunca se debe colocar el condicional en la prótasis introducida por 'si' (*'Si habríamos sabido...'* es un error gramatical grave)."
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
                    ["el desacierto", "mistake, blunder"],
                    ["soslayar", "to sidestep, to bypass"],
                    ["el menoscabo", "detriment, impairment"],
                    ["la rectificación", "rectification, correction"]
                ],
                "teaches": ["b2-unit10-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si el comité hubiera analizado los datos con rigor, no se __ cometido semejante desacierto. (haber - pluscuamperfecto de subjuntivo)",
                "answer": "hubiera",
                "english": "If the committee had analyzed the data rigorously, such a blunder would not have been made.",
                "teaches": ["pluscuamperfecto-subjuntivo-apodosis"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué es admisible decir 'Si me hubieras avisado, te hubiera acompañado' en español formal?",
                "options": [
                    "Porque el pluscuamperfecto de subjuntivo en '-ra' puede alternar con el condicional compuesto en la apódosis.",
                    "Porque la conjunción 'si' exige obligatoriamente subjuntivo en ambas cláusulas de la oración.",
                    "Porque en las oraciones subordinadas condicionales nunca se admite el modo indicativo."
                ],
                "correct": 0,
                "teaches": ["pluscuamperfecto-subjuntivo-apodosis"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Con", "más", "prudencia,", "el", "equipo", "se", "hubiera", "ahorrado", "este", "fracaso."],
                "solution": ["Con", "más", "prudencia,", "el", "equipo", "se", "hubiera", "ahorrado", "este", "fracaso."],
                "english": "With more prudence, the team would have spared themselves this failure.",
                "teaches": ["pluscuamperfecto-subjuntivo-apodosis"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Auditor", "text": "¿Qué impacto tuvo la falta de supervisión contable en la filial?"},
                    {"speaker": "Contralora", "text": "_____"},
                    {"speaker": "Auditor", "text": "Una lección costosa que exige protocolos de auditoría permanentes."}
                ],
                "options": [
                    "Si la gerencia hubiera revisado los balances semestrales, el fraude se hubiera detectado en su fase inicial.",
                    "Las oficinas centrales cuentan con estacionamiento subterráneo para los empleados.",
                    "Los contratos de arrendamiento comercial suelen firmarse por tres años renovables."
                ],
                "correct": 0,
                "teaches": ["pluscuamperfecto-subjuntivo-apodosis"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "De haber mediado mayor prudencia, no se hubiera producido este lamentable menoscabo.",
                "english": "Had greater prudence intervened, this regrettable impairment would not have occurred.",
                "teaches": ["pluscuamperfecto-subjuntivo-apodosis"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=10,
        title="El pluscuamperfecto de subjuntivo en la apódosis",
        goal="Employ the pluperfect subjunctive in the apodosis (hubiera hecho) as a stylistic alternative to the compound conditional in formal prose.",
        grammar_desc="alternancia estilística entre condicional compuesto y pluscuamperfecto de subjuntivo en la apódosis",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Recognize and produce 'hubiera + participle' in conditional main clauses.",
            "Differentiate between acceptable literary variation and grammatical errors.",
            "Deploy terminology of retrospective critique (desacierto, menoscabo, imprevisión, rectificación)."
        ]
    ))

    # Lesson 3: b2-10-03 - Fórmulas de lamento, queja y reproche en el pasado
    l3 = "b2-10-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.10.03",
        "lesson": l3,
        "title": "Remordimientos, reproches y quejas formales",
        "theme": "Vocabulario de lamento afectivo y responsabilidad retrospectiva",
        "words": [
            {"lemma": "el remordimiento", "translation": "remorse, regret", "pos": "noun"},
            {"lemma": "el reproche", "translation": "reproach, blame", "pos": "noun"},
            {"lemma": "la negligencia", "translation": "negligence", "pos": "noun"},
            {"lemma": "desaprovechar", "translation": "to waste, to squander", "pos": "verb"},
            {"lemma": "el saldo", "translation": "balance, end result", "pos": "noun"},
            {"lemma": "reclamar", "translation": "to claim, to demand", "pos": "verb"},
            {"lemma": "la amargura", "translation": "bitterness", "pos": "noun"},
            {"lemma": "el reproche", "translation": "reproach, reproachful remark", "pos": "noun"}
        ]
    })
    # Wait, replace duplicate "el reproche" with another word
    # Let's fix that word list:
    words_l3 = [
        {"lemma": "el remordimiento", "translation": "remorse, regret", "pos": "noun"},
        {"lemma": "el reproche", "translation": "reproach, blame", "pos": "noun"},
        {"lemma": "la negligencia", "translation": "negligence", "pos": "noun"},
        {"lemma": "desaprovechar", "translation": "to waste, to squander", "pos": "verb"},
        {"lemma": "el saldo", "translation": "balance, end result", "pos": "noun"},
        {"lemma": "reclamar", "translation": "to claim, to demand", "pos": "verb"},
        {"lemma": "la amargura", "translation": "bitterness", "pos": "noun"},
        {"lemma": "lamentar", "translation": "to regret, to lament", "pos": "verb"}
    ]
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.10.03",
        "lesson": l3,
        "title": "Remordimientos, reproches y quejas formales",
        "theme": "Vocabulario de lamento afectivo y responsabilidad retrospectiva",
        "words": words_l3
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.10.03.lamento-reproche",
        "title": "Fórmulas de lamento, queja y reproche en el pasado",
        "sections": [
            {
                "type": "text",
                "title": "Estructuras para expresar arrepentimiento y censura moral",
                "content": "Para formular reproches o lamentar conductas pasadas irrevocables, el español recurre a perífrasis modales compuestas y oraciones exclamativas independientes con subjuntivo: '¡Si al menos me hubieras consultado!', 'Deberías / Habrías debido advertirme a tiempo', 'Habría sido preferible que no firmaras ese documento'."
            },
            {
                "type": "table",
                "title": "Fórmulas canónicas de reproche y lamento",
                "rows": [
                    ["Exclamativa con 'si al menos'", "'¡Si al menos hubieras respondido mis llamadas!' (lamento/reproche)"],
                    ["Obligación moral no cumplida", "'Debiste haber / Deberías haber informado a la junta' (censura)"],
                    ["Preferencia irreal en el pasado", "'Habría sido mejor que aplazáramos la votación' (autocrítica)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el diálogo formal e interpersonal",
                "items": [
                    {"spanish": "¡Si tan solo hubiéramos invertido en tecnología preventiva antes del siniestro!", "english": "If only we had invested in preventive technology before the accident!"},
                    {"spanish": "Habría sido conveniente que presentaras la renuncia antes de que estallara el escándalo.", "english": "It would have been advisable for you to submit your resignation before the scandal erupted."},
                    {"spanish": "Los ciudadanos reclamaron que el ministerio debió haber coordinado las evacuaciones con mayor celeridad.", "english": "Citizens complained that the ministry should have coordinated evacuations with greater swiftness."}
                ]
            },
            {
                "type": "tip",
                "content": "'Deberías haber + participio' atenúa el reproche mediante la cortesía del condicional, mientras que 'debiste haber + participio' manifiesta una recriminación directa, categórica y sin matices atenuantes."
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
                    ["el remordimiento", "remorse, regret"],
                    ["la negligencia", "negligence"],
                    ["desaprovechar", "to waste, to squander"],
                    ["la amargura", "bitterness"]
                ],
                "teaches": ["b2-unit10-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "¡Si al menos nos __ la verdad a tiempo, habríamos protegido a los damnificados! (haber dicho)",
                "answer": "hubieras dicho",
                "english": "If at least you had told us the truth in time, we would have protected the victims!",
                "teaches": ["lamento-reproche-condicional"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz pragmático aporta 'Habrías debido avisar' frente a 'Debiste avisar'?",
                "options": [
                    "Atenúa cortésmente el reproche mediante el condicional compuesto.",
                    "Indica una obligación futura que aún no se ha cumplido.",
                    "Expresa una orden militar obligatoria sin derecho a réplica."
                ],
                "correct": 0,
                "teaches": ["lamento-reproche-condicional"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Habría", "sido", "preferible", "que", "hubiéramos", "esperado", "el", "informe", "final."],
                "solution": ["Habría", "sido", "preferible", "que", "hubiéramos", "esperado", "el", "informe", "final."],
                "english": "It would have been preferable for us to have waited for the final report.",
                "teaches": ["lamento-reproche-condicional"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diputado", "text": "El saldo presupuestario de la obra pública fue un verdadero desastre."},
                    {"speaker": "Ministra", "text": "_____"},
                    {"speaker": "Diputado", "text": "Reconocer ese error es el primer paso para corregir el rumbo institucional."}
                ],
                "options": [
                    "Reconozco que habríamos debido fiscalizar las licitaciones con mayor rigor desde el primer momento.",
                    "El cemento portland es el material más utilizado en la construcción de puentes carreteros.",
                    "La biblioteca del congreso nacional atesora colecciones de leyes coloniales."
                ],
                "correct": 0,
                "teaches": ["lamento-reproche-condicional"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "¡Si al menos hubiesen verificado los antecedentes, no lamentaríamos este engaño!",
                "english": "If at least they had verified the background, we would not be lamenting this deception!",
                "teaches": ["lamento-reproche-condicional"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=10,
        title="Fórmulas de lamento, queja y reproche en el pasado",
        goal="Formulate past regrets, moral reproaches, and retrospective critiques using modal periphrases and exclamatory clauses.",
        grammar_desc="estructuras de reproche y lamento: ¡si al menos hubieras...!, deberías haber + participio",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Formulate exclamatory conditional regrets with 'si tan solo' / 'si al menos'.",
            "Express calibrated reproaches with modal periphrases ('deberías haber...', 'habría sido preferible que...').",
            "Deploy emotional and ethical vocabulary of regret (remordimiento, negligencia, saldo, amargura)."
        ]
    ))

    # Lesson 4: b2-10-04 - Estructuras condicionales implícitas con participio y gerundio
    l4 = "b2-10-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.10.04",
        "lesson": l4,
        "title": "Condiciones tácitas y análisis de contingencias",
        "theme": "Vocabulario de atenuantes, agravantes y ponderación causal",
        "words": [
            {"lemma": "el atenuante", "translation": "mitigating factor, extenuating circumstance", "pos": "noun"},
            {"lemma": "el detonante", "translation": "trigger, spark", "pos": "noun"},
            {"lemma": "la omisión", "translation": "omission, failure to act", "pos": "noun"},
            {"lemma": "previsible", "translation": "foreseeable, predictable", "pos": "adjective"},
            {"lemma": "el agravante", "translation": "aggravating factor", "pos": "noun"},
            {"lemma": "dilucidar", "translation": "to elucidate, to clarify", "pos": "verb"},
            {"lemma": "ponderar", "translation": "to weigh, to consider carefully", "pos": "verb"},
            {"lemma": "la contingencia", "translation": "contingency, unforeseen event", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.10.04.condicionales-implicitas",
        "title": "Estructuras condicionales implícitas con participio y gerundio",
        "sections": [
            {
                "type": "text",
                "title": "Condiciones tácitas sin la conjunción 'si'",
                "content": "En la prosa analítica, jurídica e historiográfica, es común condensar períodos condicionales mediante construcciones no personales: 'De haber + participio', 'Habiendo + participio' o participios absolutos: 'De haber sabido las cláusulas ocultas, no habríamos firmado el tratado'."
            },
            {
                "type": "table",
                "title": "Mecanismos de condensación condicional en el pasado",
                "rows": [
                    ["'De haber + participio'", "'De haber previsto la tormenta, habríamos cancelado el zarpe' (= Si hubiéramos previsto)"],
                    ["'Habiendo + participio'", "'Habiendo contado con aval bancario, la empresa no hubiera quebrado' (= Si hubiera contado)"],
                    ["Participio absoluto", "'Aclarada la disputa a tiempo, se habrían evitado los tribunales' (= Si se hubiera aclarado)"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en informes técnicos y jurídicos",
                "items": [
                    {"spanish": "De haber mediado una supervisión adecuada, las omisiones contables se habrían detectado de inmediato.", "english": "Had adequate supervision intervened, the accounting omissions would have been detected immediately."},
                    {"spanish": "Habiendo ponderado todos los agravantes, el tribunal habría dictado una sentencia más severa.", "english": "Having weighed all aggravating factors, the court would have handed down a harsher sentence."},
                    {"spanish": "De no haberse divulgado las grabaciones secretas, el gabinete habría concluido su mandato sin sobresaltos.", "english": "Had the secret recordings not been disclosed, the cabinet would have finished its mandate without upheaval."}
                ]
            },
            {
                "type": "tip",
                "content": "La locución 'de haber + participio' exige identidad o correlación lógica estricta de sujeto con la apódosis, salvo cuando se emplea en fórmulas impersonales universales ('De haberse sabido la verdad...')."
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
                    ["el atenuante", "mitigating factor"],
                    ["el detonante", "trigger, spark"],
                    ["la omisión", "omission, failure to act"],
                    ["ponderar", "to weigh, to consider carefully"]
                ],
                "teaches": ["b2-unit10-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "De __ mediado una oportuna advertencia, el desastre aéreo se habría evitado por completo. (haber)",
                "answer": "haber",
                "english": "Had a timely warning intervened, the air disaster would have been completely avoided.",
                "teaches": ["condicionales-pasadas-haber-participio"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿A qué proposición condicional equivale exactamente la frase 'De haber conocido los términos...'?",
                "options": [
                    "A 'Si hubiera conocido los términos...'",
                    "A 'Dado que conocí los términos...'",
                    "A 'A pesar de que conozca los términos...'"
                ],
                "correct": 0,
                "teaches": ["condicionales-pasadas-haber-participio"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["De", "haber", "previsto", "la", "contingencia,", "no", "habríamos", "sufrido", "pérdidas."],
                "solution": ["De", "haber", "previsto", "la", "contingencia,", "no", "habríamos", "sufrido", "pérdidas."],
                "english": "Had we foreseen the contingency, we would not have suffered losses.",
                "teaches": ["condicionales-pasadas-haber-participio"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Fiscal", "text": "¿Pudo la junta directiva impedir la quiebra fraudulenta de la entidad bancaria?"},
                    {"speaker": "Perito judicial", "text": "_____"},
                    {"speaker": "Fiscal", "text": "Esa negligencia inexcusable compromete directamente su responsabilidad penal."}
                ],
                "options": [
                    "De haber actuado con la debida diligencia frente a los informes contables, el daño patrimonial habría sido mínimo.",
                    "El edificio principal del banco fue inaugurado por el gobernador en el año 1975.",
                    "Las tasas de interés de los créditos hipotecarios varían según la inflación anual."
                ],
                "correct": 0,
                "teaches": ["condicionales-pasadas-haber-participio"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "De haber ponderado los atenuantes, la corte no habría impuesto esa condena.",
                "english": "Had it weighed the mitigating factors, the court would not have imposed that sentence.",
                "teaches": ["condicionales-pasadas-haber-participio"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=10,
        title="Estructuras condicionales implícitas con participio y gerundio",
        goal="Construct implicit counterfactual conditions using 'de haber + participle' and absolute clauses in formal analytical registers.",
        grammar_desc="condicionales implícitas de pasado: de haber + participio, habiendo + participio",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Condense conditional periods using 'de haber + participle'.",
            "Interpret and produce absolute participle constructions with hypothetical past meaning.",
            "Deploy analytical prose terminology (atenuante, detonante, omisión, ponderar, contingencia)."
        ]
    ))

    # Lesson 5: b2-10-05 - Construcciones concesivo-condicionales e inversión retórica
    l5 = "b2-10-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.10.05",
        "lesson": l5,
        "title": "Rhetórica histórica, disyuntivas y fatalidad",
        "theme": "Vocabulario de determinismo histórico, sesgo y fatalidad",
        "words": [
            {"lemma": "la disyuntiva", "translation": "dilemma, fork in the road", "pos": "noun"},
            {"lemma": "el sesgo", "translation": "bias, slant", "pos": "noun"},
            {"lemma": "la postrimería", "translation": "later stage, waning period", "pos": "noun"},
            {"lemma": "ineludible", "translation": "inescapable, unavoidable", "pos": "adjective"},
            {"lemma": "desentrañar", "translation": "to unravel, to figure out", "pos": "verb"},
            {"lemma": "la fatalidad", "translation": "fatality, inexorable fate", "pos": "noun"},
            {"lemma": "el espejismo", "translation": "mirage, illusion", "pos": "noun"},
            {"lemma": "concluyente", "translation": "conclusive, decisive", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.10.05.inversiones-condicionales",
        "title": "Construcciones concesivo-condicionales e inversión retórica",
        "sections": [
            {
                "type": "text",
                "title": "Inversión retórica y combinación concesiva en el pasado",
                "content": "En la prosa ensayística y literaria, las condiciones contrafácticas adoptan giros de inversión sintáctica ('Hubiérase evitado semejante tragedia si...') y fórmulas concesivas hipotéticas ('Aun cuando hubiésemos intervenido, el desenlace habría sido idéntico'). Estos esquemas enfatizan la inevitabilidad o futilidad de una acción alternativa frente a fuerzas históricas mayores."
            },
            {
                "type": "table",
                "title": "Esquemas avanzados de retórica contrafáctica",
                "rows": [
                    ["Inversión literaria ('hubiérase')", "'Hubiérase evitado la guerra de haber existido voluntad civil'"],
                    ["Concesiva contrafáctica ('aun cuando')", "'Aun cuando hubieran ganado las elecciones, la crisis económica habría estallado'"],
                    ["Alternativa enfática ('así hubiera...')", "'No habría cambiado de parecer así hubieran insistido mil veces'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo filosófico e historiográfico",
                "items": [
                    {"spanish": "Aun cuando los diplomáticos hubiesen redactado un armisticio perfecto, las tensiones de fondo habrían dinamitado la paz.", "english": "Even if diplomats had drafted a perfect armistice, the underlying tensions would have detonated the peace."},
                    {"spanish": "Hubiérase pensado que la prosperidad salitrera traería estabilidad perpétua, pero resultó ser un mero espejismo.", "english": "One would have thought that nitrate prosperity would bring perpetual stability, but it turned out to be a mere mirage."},
                    {"spanish": "No habríamos claudicado en nuestros principios éticos así nos hubiesen ofrecido todas las riquezas del ministerio.", "english": "We would not have yielded in our ethical principles even if they had offered us all the riches of the ministry."}
                ]
            },
            {
                "type": "tip",
                "content": "La forma enclítica 'hubiérase + participio' es un cultismo propio de la lengua escrita más refinada. No debe abusarse de ella en la comunicación oral estándar, donde 'se habría pensado' o 'se hubiera pensado' resulta natural."
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
                    ["la disyuntiva", "dilemma, fork in the road"],
                    ["ineludible", "inescapable, unavoidable"],
                    ["desentrañar", "to unravel, to figure out"],
                    ["el espejismo", "mirage, illusion"]
                ],
                "teaches": ["b2-unit10-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Aun cuando __ intentado frenar la insurrección, las fuerzas armadas no habrían podido contener la cólera popular. (haber)",
                "answer": "hubieran",
                "english": "Even if they had tried to curb the insurrection, the armed forces would not have been able to contain popular anger.",
                "teaches": ["inversiones-condicionales-de-haber"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué valor discursivo transmite 'Aun cuando hubiésemos ganado, nada habría cambiado'?",
                "options": [
                    "Concesión contrafáctica que resalta la futilidad o ineficacia de la condición frente al desenlace.",
                    "Certeza absoluta sobre un acontecimiento que ocurrirá en el porvenir.",
                    "Duda existencial sobre hechos que están sucediendo en el presente."
                ],
                "correct": 0,
                "teaches": ["inversiones-condicionales-de-haber"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Aun", "cuando", "hubiéramos", "cedido,", "la", "ruptura", "habría", "sido", "inevitable."],
                "solution": ["Aun", "cuando", "hubiéramos", "cedido,", "la", "ruptura", "habría", "sido", "inevitable."],
                "english": "Even if we had yielded, the rupture would have been inevitable.",
                "teaches": ["inversiones-condicionales-de-haber"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Filósofo", "text": "¿Cree usted en el determinismo histórico ciego o en el libre albedrío de los pueblos?"},
                    {"speaker": "Sociólogo", "text": "_____"},
                    {"speaker": "Filósofo", "text": "Una distinción capital para no caer en el derrotismo cínico."}
                ],
                "options": [
                    "Aun cuando ciertas fuerzas estructurales condicionen la época, si los ciudadanos hubiesen carecido de voluntad moral, ningún avance social se habría consolidado.",
                    "Los tratados de sociología se organizan por capítulos temáticos e índices alfabéticos.",
                    "El debate parlamentario concluyó a las tres de la madrugada tras una votación unánime."
                ],
                "correct": 0,
                "teaches": ["inversiones-condicionales-de-haber"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aun cuando hubiésemos intervenido con presteza, el resultado habría sido idéntico.",
                "english": "Even if we had intervened promptly, the outcome would have been identical.",
                "teaches": ["inversiones-condicionales-de-haber"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=10,
        title="Construcciones concesivo-condicionales e inversión retórica",
        goal="Master advanced concessive-conditional schemes ('aun cuando hubiéramos...') and rhetorical inversion in historical and philosophical essays.",
        grammar_desc="concesivas hipotéticas de pasado e inversiones retóricas: aun cuando hubiera + participio",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Deploy past concessive conditionals ('aun cuando hubiera...') to argue inevitability.",
            "Analyze literary rhetorical inversions in historical counterfactual texts.",
            "Use sophisticated philosophical vocabulary (disyuntiva, sesgo, ineludible, espejismo)."
        ]
    ))

    # Consolidation: b2-10-consolidation
    l_con = "b2-10-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la encrucijada", "crossroads, turning point"],
                    ["el desenlace", "outcome, denouement"],
                    ["el desacierto", "mistake, blunder"],
                    ["el detonante", "trigger, spark"]
                ],
                "teaches": ["b2-unit10-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes construcciones ejemplifica una apódosis estilística culta con pluscuamperfecto de subjuntivo?",
                "options": [
                    "Si el gobierno hubiera escuchado al pueblo, se hubiera evitado el levantamiento.",
                    "Si el gobierno escucharía al pueblo, se evitaría el levantamiento social.",
                    "Si el gobierno haya escuchado al pueblo, se habrá evitado el levantamiento."
                ],
                "correct": 0,
                "teaches": ["pluscuamperfecto-subjuntivo-apodosis"]
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿A qué equivale semánticamente la locución 'De haber actuado con prudencia...'?",
                "options": [
                    "A una condición irreal en el pasado: 'Si hubiéramos actuado con prudencia...'",
                    "A una justificación causal consumada: 'Porque actuamos con prudencia...'",
                    "A una hipótesis de futuro contingente: 'Siempre que actuemos con prudencia...'"
                ],
                "correct": 0,
                "teaches": ["condicionales-pasadas-haber-participio"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "¡Si al menos __ consultado a los expertos, no habríamos incurrido en semejante negligencia! (haber)",
                "answer": "hubiéramos",
                "english": "If at least we had consulted the experts, we would not have incurred such negligence!",
                "teaches": ["lamento-reproche-condicional"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "El país enfrentaba una encrucijada política de consecuencias irreversibles. [The country faced a political crossroads of irreversible consequences.]",
                    "Si los líderes hubieran pactado con sensatez, la confrontación armada no se habría desencadenado. [If leaders had agreed sensibly, armed confrontation would not have been triggered.]",
                    "De haber mediado mayor prudencia internacional, el saldo humanitario hubiera sido menor. [Had greater international prudence intervened, the humanitarian toll would have been smaller.]",
                    "Aun cuando ambas facciones hubiesen firmado la tregua, las heridas tardaron décadas en cicatrizar. [Even if both factions had signed the truce, the wounds took decades to heal.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": [
                    "condicionales-tercer-tipo-contrafactico",
                    "pluscuamperfecto-subjuntivo-apodosis",
                    "condicionales-pasadas-haber-participio",
                    "inversiones-condicionales-de-haber"
                ]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítico", "text": "¿Cómo juzga la trayectoria vital del protagonista de Conversación en La Catedral?"},
                    {"speaker": "Profesor", "text": "_____"},
                    {"speaker": "Crítico", "text": "Una lúcida radiografía de la parálisis moral ante el autoritarismo."}
                ],
                "options": [
                    "Santiago Zavala personifica el tormento contrafáctico: si no hubiera roto con su familia ni hubiera abandonado sus ideales, su destino habría sido diametralmente opuesto.",
                    "Los diarios de la tarde se vendían en los quioscos de la plaza San Martín por veinte centavos.",
                    "El clima invernal de la capital peruana se caracteriza por una persistente garúa marina."
                ],
                "correct": 0,
                "teaches": ["condicionales-tercer-tipo-contrafactico"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "De haber sabido el precio de sus concesiones, jamás habrían claudicado.",
                "english": "Had they known the price of their concessions, they would never have yielded.",
                "teaches": ["condicionales-pasadas-haber-participio"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta una reflexión contrafáctica sobre una decisión histórica empleando la fórmula 'Si + pluscuamperfecto de subjuntivo, condicional compuesto' o 'De haber + participio'.",
                        "answer": "De haber sabido las consecuencias institucionales de aquel decreto, los legisladores habrían rechazado la propuesta por unanimidad."
                    }
                ],
                "teaches": ["condicionales-tercer-tipo-contrafactico"]
            }
        ]
    })

    # Classic Story for Unit 10: Mario Vargas Llosa - Conversación en La Catedral
    story_core_10 = {
        "id": "story.b2.10.vargasllosa",
        "title": "Mario Vargas Llosa: Conversación en La Catedral",
        "level": "B2",
        "lesson": 6,
        "type": "classic",
        "estimatedMinutes": 8,
        "characters": [
            "Santiago Zavala",
            "Ambrosio",
            "Don Fermín Zavala"
        ],
        "summary": "Adaptación pedagógica para nivel B2 de la célebre novela de Mario Vargas Llosa: el desencanto existencial, las encrucijadas éticas bajo la dictadura de Odría y la célebre interrogante sobre el destino peruano.",
        "author": "Mario Vargas Llosa (Perú, 1936–)",
        "work": "Conversación en La Catedral (1969)",
        "source": "Adaptado para estudiantes de nivel B2 a partir de la novela clásica de Mario Vargas Llosa",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Desde la puerta de 'La Crónica', Santiago Zavala contempla la avenida Tacna sin amor: automóviles, edificios desiguales y descoloridos, esqueletos de carteles luminosos flotando en el humo de la garúa limeña. Al contemplar ese gris plomizo que cubre la ciudad como una mortaja de humedad marina, una pregunta recurrente y punzante vuelve a morderle la conciencia como un reproche antiguo: ¿en qué momento se había jodido el Perú? Los lustrabotas voceaban los titulares de la tarde, los empleados públicos apuraban el paso con sus cartapacios raídos bajo el brazo, y Zavalita pensaba que si la república no hubiera caído bajo la bota autoritaria del general Odría en los años cincuenta, tal vez su generación no habría quedado desprovista de ideales y asfixiada en el desencanto más amargo."
            },
            {
                "type": "narration",
                "text": "Aquella misma tarde, el azar lo conduce hasta la perrera municipal para rescatar a su perro Batuque, atrapado en una redada callejera. En ese recinto desolado, entre aullidos desesperados y hedor a barro salobre, Santiago reconoce con estupor a un anciano chofer negro que arrastra una carretilla de madera: Ambrosio, el antiguo sirviente de confianza de su padre, don Fermín Zavala. Sintiendo el impacto visceral de un pasado que creía sepultado bajo toneladas de indiferencia, Santiago invita a Ambrosio a refugiarse en 'La Catedral', una cantina destartalada y miserable cercana al río Rímac, donde los parroquianos consumen cerveza tibia y aguardiente barato entre mesas de pino grasiento y zumbido constante de moscas."
            },
            {
                "type": "narration",
                "text": "Frente a dos botellas espumosas, comienza un diálogo torrencial de cuatro horas que teje de modo implacable las vidas de ambos hombres. En retrospectiva, Santiago comprende que su propia biografía constituye una cadena interminable de encrucijadas perdidas. Si no se hubiera rebelado contra la hipocresía burguesa de su hogar para ingresar a la rebelde Universidad de San Marcos, jamás habría conocido el fervor clandestino del grupo comunista Cahuide. Sin embargo, aquella rebeldía juvenil terminó truncada en un calabozo de la Seguridad Pública: si don Fermín no hubiera intervenido con sus poderosas influencias ministeriales para liberarlo, Santiago habría compartido el destierro con sus compañeros de militancia. Al descubrir que su padre lo había salvado sacrificando el honor de los otros, el joven rompió con su familia para siempre, condenándose a una vida gris como oscuro redactor de noticias locales."
            },
            {
                "type": "narration",
                "text": "Ambrosio escucha las preguntas ansiosas de Santiago con una mezcla de gratitud servil y pavor contenido. El chofer había sido testigo y ejecutor de los secretos más inconfesables del régimen dictatorial encabezado en las sombras por el siniestro Cayo Bermúdez, el implacable director de Gobierno que manejaba el espionaje, la delación y la tortura en las cloacas del poder. Si don Fermín Zavala no hubiera necesitado mantener sus negocios a flote mediante complicidades secretas con la tiranía, jamás se habría hundido en una ciénaga de corrupción moral que acabó por destruir a toda su familia. A través de las revelaciones entrecortadas de Ambrosio, Santiago desentraña que de haber exigido transparencia a tiempo, los crímenes que mancharon su estirpe no se habrían consumado en la más absoluta impunidad."
            },
            {
                "type": "narration",
                "text": "La atmósfera sofocante de 'La Catedral' adquiere el dramatismo de una catarsis trágica cuando surge la figura espectral de la Musa, una figura turbia del bajo mundo cuyo chantaje amenazaba con destapar las aberraciones íntimas de la oligarquía limeña. Ambrosio baja los ojos, aprieta los puños contra el vaso de cristal y sugiere con voz quebrada que cometió un acto atroz para proteger la dignidad de su patrón. Santiago siente que la cerveza se transforma en hiel en su garganta: si Ambrosio no le hubiera revelado aquella verdad abominable en aquel bar de mala muerte, él habría podido continuar refugiado en su apacible mediocridad cotidiana sin cargar con el peso intolerable de la culpa paterna."
            },
            {
                "type": "narration",
                "text": "La conversación concluye cuando las luces de la cantina comienzan a parpadear y los mozos recogen las sillas sobre las mesas vacías. Al despedirse en la niebla helada de la orilla del río, Santiago sabe que ninguna rectificación en el presente puede revocar las decisiones del pasado. De haber elegido la abogacía honorable que su padre deseaba para él, tal vez habría triunfado en los círculos aristocráticos; de haber mantenido su militancia clandestina con valentía irreductible, tal vez habría transformado la sociedad o muerto en una celda del penal del Frontón. Pero eligió el camino intermedio de la renuncia silenciosa, transformándose en un espectador escéptico de la tragedia nacional."
            },
            {
                "type": "narration",
                "text": "Caminando de regreso hacia su modesto departamento bajo la garúa incesante, Santiago comprende que la encrucijada del Perú no fue fruto de una fatalidad cósmica irresistible, sino la suma acumulada de cobardías individuales, silencios cómplices e ilusiones traicionadas. Si los hombres libres hubiesen alzado la voz con intransigente decencia cuando la dictadura comenzó a corromper los tribunales y las conciencias, la patria no habría extraviado su rumbo moral. La obra maestra de Vargas Llosa se consagra así como una implacable indagación contrafáctica sobre la responsabilidad ética frente a la corrupción del poder."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué interrogante fundamental atormenta a Santiago Zavala al inicio de su jornada en Lima?",
                        "options": [
                            "En qué momento preciso el Perú se desvió de su rumbo histórico y se hundió en la degradación moral.",
                            "Por qué el periódico 'La Crónica' decidió trasladar su sede editorial a la ciudad de Arequipa.",
                            "Cuándo se fundaron las primeras logias clandestinas de estudiantes en la Universidad de San Marcos.",
                            "Cómo organizar una campaña de recolección de fondos para modernizar la perrera municipal."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 expone la célebre pregunta que atormenta a Zavalita mientras contempla la avenida Tacna bajo la garúa: '¿en qué momento se había jodido el Perú?'."
                    },
                    {
                        "question": "¿Cuál fue el motivo de la ruptura definitiva entre Santiago y su padre, don Fermín Zavala?",
                        "options": [
                            "El descubrimiento de que su padre usó influencias con la dictadura para liberarlo de prisión sacrificando a sus camaradas.",
                            "La decisión de su padre de desheredarlo debido a su matrimonio con una artista de teatro extranjera.",
                            "La venta forzosa de la hacienda familiar para cancelar deudas adquiridas en el hipódromo de Lima.",
                            "La negativa de Santiago a matricularse en la escuela militar para iniciar una carrera en la infantería."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 narra que don Fermín utilizó sus conexiones ministeriales para liberar a Santiago de la cárcel, lo que provocó que el joven rompiera con su familia al no tolerar semejante complicidad."
                    },
                    {
                        "question": "¿A qué conclusión ética llega Santiago Zavala tras su prolongado diálogo con Ambrosio en 'La Catedral'?",
                        "options": [
                            "Que la descomposición moral del país obedeció a la cobardía individual y al silencio cómplice ante la tiranía, no a un destino ciego.",
                            "Que la única solución viable para la república radica en la reinstauración indefinida del gobierno militar.",
                            "Que las fortunas creadas bajo regímenes autoritarios deben ser expropiadas de inmediato por decreto legislativo.",
                            "Que la memoria histórica debe borrarse por completo para inaugurar una etapa de prosperidad comercial."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 7 destaca que la crisis peruana no provino del azar, sino de la renuncia ética, las complicidades y la falta de coraje moral de los ciudadanos frente al poder corrupto."
                    }
                ]
            }
        }
    }
    write_json(f"stories/classics/b2/b2-10.json", story_core_10)

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=10,
        title="Unit 10 Consolidation: Counterfactuals & Regrets",
        goal="Consolidate past counterfactual conditionals, pluperfect subjunctive in apodosis, modal reproaches, and implicit conditions through literary analysis.",
        grammar_desc="síntesis de períodos contrafácticos de pasado, reproches retrospectivos, condiciones implícitas con participio y concesivas hipotéticas",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Construct complex counterfactual sentences relating past decisions to alternative outcomes.",
            "Utilize the pluperfect subjunctive ('hubiera...') in literary apodoses.",
            "Condense conditions using 'de haber + participle' in formal analytical writing.",
            "Analyze literary turning points in Vargas Llosa's 'Conversación en La Catedral'."
        ],
        checklist_items=[
            "I can formulate third conditional sentences analyzing past unfulfilled events.",
            "I can alternate compound conditional with pluperfect subjunctive in formal apodoses.",
            "I can express past regrets and reproaches with '¡si al menos...!' and 'deberías haber...'.",
            "I can condense hypothetical conditions using 'de haber + participle'."
        ],
        story_ref=f"stories/classics/b2/b2-10.json"
    ))
    print("Completed Core Unit 10 generation!")

    # -------------------------------------------------------------------------
    # REGIONAL TRACK UNIT 10 (b2-cuba): Cuba: Island of Paradox, Revolution, Cinema & Music
    # -------------------------------------------------------------------------

    # Lesson 1: b2-cuba-01 - La arquitectura de La Habana y el paisaje de Viñales
    lc1 = "b2-cuba-01"
    write_json(f"vocabulary/b2/{lc1}-voc.json", {
        "id": "vocab.b2.cuba.01",
        "lesson": lc1,
        "title": "Arquitectura colonial habanera y topografía kárstica de Viñales",
        "theme": "Vocabulario de patrimonio urbano, aleros coloniales y geología caribeña",
        "words": [
            {"lemma": "el mogote", "translation": "karst limestone hill, mogote", "pos": "noun"},
            {"lemma": "el alero", "translation": "eaves, overhang", "pos": "noun"},
            {"lemma": "la vega", "translation": "tobacco meadow, fertile lowland", "pos": "noun"},
            {"lemma": "el vitral", "translation": "stained-glass window", "pos": "noun"},
            {"lemma": "la bóveda", "translation": "vault, dome", "pos": "noun"},
            {"lemma": "el portalón", "translation": "large entrance gate, grand portal", "pos": "noun"},
            {"lemma": "añejo", "translation": "aged, vintage", "pos": "adjective"},
            {"lemma": "la solana", "translation": "sunny terrace, sun balcony", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{lc1}-a-gr.json", {
        "id": "grammar.b2.cuba.01.arquitectura-vinales",
        "title": "La arquitectura de La Habana y el paisaje de Viñales",
        "sections": [
            {
                "type": "text",
                "title": "Descripción arquitectónica y recursos de registro culto",
                "content": "La caracterización del patrimonio urbano y paisajístico en nivel B2 integra estructuras descriptivas complejas: participios con valor adjetival estativo ('resguardado por robustos baluartes'), construcciones apositivas explicativas y oraciones subordinadas adjetivas explicativas introducidas por pronombres relativos compuestos ('cuyos vitrales polícromos tamizan la luz tropical')."
            },
            {
                "type": "table",
                "title": "Recursos estilísticos de la crónica arquitectónica",
                "rows": [
                    ["Participio de estado", "'Erigida en el siglo XVI, La Habana Vieja combina fortalezas y conventos barrocos'"],
                    ["Relativo compuesto 'cuyo'", "'Viñales, cuyos mogotes cársticos emergen verticalmente sobre las vegas de tabaco'"],
                    ["Adjetivación evocadora", "'Patios sombreados por arquerías dóricas y celosías de maderas nobles'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en guías patrimoniales de Cuba",
                "items": [
                    {"spanish": "El castillo de la Real Fuerza, concluido en 1577, resguarda el puerto de La Habana con murallas de piedra caliza coralina.", "english": "The Castillo de la Real Fuerza, completed in 1577, guards Havana's harbor with walls of coralline limestone."},
                    {"spanish": "En el valle de Viñales, las tradicionales casas de curado de tabaco conviven con formaciones geológicas del Jurásico.", "english": "In the Viñales Valley, traditional tobacco-curing barns coexist with Jurassic geological formations."},
                    {"spanish": "Los mediopuntos y vitrales abanicados de las casonas de El Vedado reflejan la riqueza ecléctica del modernismo caribeño.", "english": "The fanlight stained-glass transoms of El Vedado mansions reflect the eclectic wealth of Caribbean modernism."}
                ]
            },
            {
                "type": "tip",
                "content": "En la prosa descriptiva patrimonial, evita repetir verbos comodín como 'tener' o 'haber'; prefiere verbos de localización y rasgo como 'albergar', 'ostentar', 'erigirse', 'resguardar' o 'caracterizarse por'."
            }
        ]
    })

    write_json(f"exercises/b2/{lc1}-ex.json", {
        "lesson": lc1,
        "exercises": [
            {
                "id": f"{lc1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el mogote", "karst limestone hill"],
                    ["la vega", "tobacco meadow, fertile lowland"],
                    ["el vitral", "stained-glass window"],
                    ["el alero", "eaves, overhang"]
                ],
                "teaches": ["b2-cuba-vocab"]
            },
            {
                "id": f"{lc1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué singularidad paisajística distingue al valle de Viñales en la provincia de Pinar del Río?",
                "options": [
                    "Sus colosales mogotes kársticos de cimas redondeadas que emergen abruptamente entre fértiles vegas de tabaco.",
                    "Sus glaciares de alta montaña que alimentan lagunas de origen volcánico en la cordillera.",
                    "Sus extensos fiordos marítimos navegables que conectan el golfo de México con el mar Caribe."
                ],
                "correct": 0,
                "teaches": ["cuba-arquitectura-habana-vinales"]
            },
            {
                "id": f"{lc1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las casonas señoriales de La Habana Vieja __ por sus patios interiores con arquerías barrocas y aljibes de piedra. (caracterizarse - presente)",
                "answer": "se caracterizan",
                "english": "The stately mansions of Old Havana are characterized by their interior courtyards with baroque arches and stone cisterns.",
                "teaches": ["cuba-arquitectura-habana-vinales"]
            },
            {
                "id": f"{lc1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "mogotes", "de", "Viñales", "resguardan", "un", "paisaje", "cultural", "único."],
                "solution": ["Los", "mogotes", "de", "Viñales", "resguardan", "un", "paisaje", "cultural", "único."],
                "english": "The mogotes of Viñales safeguard a unique cultural landscape.",
                "teaches": ["cuba-arquitectura-habana-vinales"]
            },
            {
                "id": f"{lc1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Arquitecta", "text": "¿Cómo definiría el contraste entre La Habana Vieja y el barrio de El Vedado?"},
                    {"speaker": "Urbanista", "text": "_____"},
                    {"speaker": "Arquitecta", "text": "Esa superposición estilística convierte a la ciudad en un museo vivo al aire libre."}
                ],
                "options": [
                    "Mientras La Habana Vieja preserva una traza colonial compacta y barroca, El Vedado despliega avenidas arboladas con mansiones eclécticas y rascacielos Art Déco.",
                    "El servicio de ferris hacia la bahía de Cabañas funciona exclusivamente los fines de semana.",
                    "Los cultivos de caña de azúcar requieren abundante mano de obra durante la zafra de primavera."
                ],
                "correct": 0,
                "teaches": ["cuba-arquitectura-habana-vinales"]
            },
            {
                "id": f"{lc1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las arcadas coloniales y los vitrales polícromos resguardan los salones del sol caribeño.",
                "english": "Colonial arcades and polychrome stained-glass windows shield the rooms from the Caribbean sun.",
                "teaches": ["cuba-arquitectura-habana-vinales"]
            }
        ]
    })

    # Regional Story 1: b2-cuba-01.json
    story_cuba_01 = {
        "id": "b2-cuba-01",
        "title": "La Habana señorial y el santuario verde de Viñales",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica analítica de nivel B2 sobre el patrimonio arquitectónico de La Habana y el paisaje cultural de Viñales: historia urbana, ecología kárstica y tradición tabacalera.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Asentada en una bahía de bolsa providencial que la convirtió durante siglos en la 'Llave del Nuevo Mundo' y antemural de las Indias Occidentales, La Habana despliega ante el viajero una de las tramas urbanas más deslumbrantes y complejas de todo el continente americano. Fundada definitivamente en su emplazamiento actual en 1519 bajo la sombra tutelar de una ceiba sagrada, la capital cubana creció como escala forzosa de las flotas de galeones cargados con la plata del Potosí y del virreinato de Nueva España antes de emprender la peligrosa travesía transatlántica rumbo a Sevilla y Cádiz. Para resguardar semejante tesoro imperial frente a las incursiones devastadoras de corsarios y piratas ingleses y franceses, la corona española edificó un cinturón colosal de fortalezas militares que todavía hoy asombra por su solidez geométrica y su monumentalidad de piedra coralina, encabezado por el imponente castillo de los Tres Reyes del Morro y la fortaleza de San Carlos de la Cabaña."
            },
            {
                "type": "narration",
                "text": "Adentrarse en el corazón de La Habana Vieja, declarada Patrimonio de la Humanidad por la UNESCO en 1982, supone sumergirse en una sinfonía de estilos arquitectónicos donde el barroco mudéjar, el neoclasicismo republicano y el eclecticismo tropical conviven en una densidad urbana fascinante. Sus cuatro plazas históricas articulan la vida civil y religiosa: la plaza de Armas con el majestuoso palacio de los Capitanes Generales; la plaza de San Francisco de Asís frente a las brisas del puerto; la recoleta plaza Vieja, donde los aleros de teja criolla sombrean casonas aristocráticas; y la plaza de la Catedral, cuya fachada asimétrica de piedra fósil marina fue descrita memorablemente por el novelista Alejo Carpentier como 'música convertida en piedra'. En estas residencias señoriales, los amplios portales de arquería dórica protegían a los peatones del sol implacable, mientras que en los interiores los techos altos de cedro y los célebres 'mediopuntos' —vitrales policromados en forma de abanico— tamizaban la luz canicular en cascadas multicolores de azul, ámbar y rubí."
            },
            {
                "type": "narration",
                "text": "Con el cambio del siglo XIX al XX y el auge económico azucarero, la ciudad desbordó las antiguas murallas para expandirse hacia el oeste siguiendo el trazado señorial del Malecón, el célebre paseo marítimo de ocho kilómetros donde las olas del Atlántico rompen con furia salina contra el muro de hormigón. En barrios como El Vedado y Miramar florecieron residencias vanguardistas, mansiones art nouveau y rascacielos Art Déco tan emblemáticos como el Edificio Bacardí, cuyas torres escalonadas de terracota y bronce testimoniaban la prosperidad cosmopolita de la burguesía habanera en los años treinta. Aunque décadas de bloqueo económico, salinidad marina implacable y limitaciones materiales han deteriorado gravemente amplios sectores del tejido habitacional popular, los ambiciosos programas de restauración liderados durante décadas por el recordado historiador Eusebio Leal lograron rescatar cientos de palacios coloniales, convirtiendo la rehabilitación patrimonial en un modelo internacional de autogestión social y comunitaria."
            },
            {
                "type": "narration",
                "text": "Apenas a ciento sesenta kilómetros al occidente de la capital, en la provincia de Pinar del Río, el paisaje urbano cede su lugar a un prodigio geológico y humano absolutamente singular: el valle de Viñales. Enclavado en la cordillera de Guaniguanico, este valle intramontano cautiva por la presencia colosal de los 'mogotes', formaciones rocosas kársticas de caliza que emergen verticalmente del fondo llano con alturas que superan los trescientos metros. Estas elevaciones de laderas abruptas y cúpulas redondeadas, vestigios erosionados de antiguas mesetas del período Jurásico, albergan en sus laderas una flora fósil endémica extraordinariamente rara, entre la que descuella la 'palma corcho' (Microcycas calocoma), considerada un auténtico fósil viviente botánico que sobrevivió a los dinosaurios sin alterar su morfología primitiva."
            },
            {
                "type": "narration",
                "text": "Bajo la sombra tutelar de estos gigantes de piedra caliza se extiende un mosaico rural de tierras rojas de fertilidad excepcional donde se cultiva el tabaco más codiciado y perfecto del planeta. Los campesinos locales, conocidos cariñosamente como vegueros, han conservado durante siglos métodos agrícolas artesanales rigurosamente tradicionales: la tierra arcillosa continúa roturándose con yuntas de bueyes para evitar la compactación mecánica que arruinaría las delicadas raíces, mientras que las hojas de tabaco tapado y de sol se recolectan una a una con una paciencia orfebre antes de trasladarse a las 'casas de curado', tradicionales construcciones de madera cubiertas con techumbres cónicas de hojas secas de palma real donde el aroma balsámico de la hoja en fermentación satura el aire cálido."
            },
            {
                "type": "narration",
                "text": "El sistema cavernoso que horada las entrañas de estos mogotes añade otra dimensión de asombro científico e histórico. Grutas kilométricas como la Gran Caverna de Santo Tomás —la segunda red subterránea más extensa de América Latina con más de cuarenta y seis kilómetros de galerías exploradas— y la Cueva del Indio resguardaron tanto los ritos funerarios de las poblaciones originarias guanajatabeyes como los refugios secretos de los esclavos 'cimarrones' que escapaban de las plantaciones durante la época colonial. Estas cavidades, donde el río San Vicente discurre en la oscuridad perpetua entre estalagmitas milenarias, conservan pictografías rupestres que testimonian la remota presencia humana en este santuario insular."
            },
            {
                "type": "narration",
                "text": "La conjunción armoniosa entre la monumentalidad arquitectónica de La Habana y la serenidad campesina de Viñales define la dualidad primordial del alma cubana: una cultura nacida del encuentro cosmopolita entre Europa, África y América que supo alzar palacios barrocos frente a las tempestades oceánicas, al tiempo que aprendió a labrar con devoción franciscana la tierra fértil de sus valles jurásicos, forjando una identidad donde la elegancia formal de la piedra labrada y la nobleza del trabajo rural se funden en un patrimonio imperecedero."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué razón estratégica La Habana fue bautizada como la 'Llave del Nuevo Mundo' durante la época colonial?",
                        "options": [
                            "Porque servía como puerto de reunión y escala obligada de las flotas de galeones cargadas de plata antes de cruzar el Atlántico.",
                            "Porque fue la única ciudad antillana donde se acuñaban monedas de oro mediante autorización papal directa.",
                            "Porque albergaba el astillero militar exclusivo donde se construían todos los barcos mercantes de la corona francesa.",
                            "Porque disponía de un canal navegable artificial que conectaba el océano Atlántico con el Pacífico."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 precisa que La Habana era la escala forzosa de las flotas del tesoro de plata de Potosí y Nueva España antes de regresar a España."
                    },
                    {
                        "question": "¿Qué elemento arquitectónico tradicional de las casonas habaneras filtraba la luz solar mediante vitrales policromados?",
                        "options": [
                            "Los mediopuntos o vitrales abanicados instalados sobre puertas y ventanales.",
                            "Las troneras blindadas de las torres defensivas de piedra coralina.",
                            "Los pozos de agua subterránea ubicados en el centro de las plazas de armas.",
                            "Las tejas metálicas galvanizadas importadas desde los puertos de Inglaterra."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 describe los mediopuntos como vitrales policromados en forma de abanico que tamizaban la luz canicular en colores azul, ámbar y rubí."
                    },
                    {
                        "question": "¿Qué característica botánica y geológica singular define a los mogotes del valle de Viñales?",
                        "options": [
                            "Son elevaciones kársticas jurásicas de paredes verticales que albergan especies vegetales fósiles como la palma corcho.",
                            "Son cráteres volcánicos activos que expulsan azufre y ceniza sobre los sembradíos de caña de azúcar.",
                            "Son dunas de arena movediza arrastradas por los vientos alisios desde el golfo de México.",
                            "Son mesetas basálticas cubiertas por bosques de abetos alpinos y líquenes subárticos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 describe los mogotes como formaciones kársticas del Jurásico donde sobrevive la palma corcho, considerada un fósil viviente botánico."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc1}.json", story_cuba_01)

    write_json(f"lessons/b2/{lc1}.json", make_lesson(
        stem=lc1,
        unit_num=10,
        title="La arquitectura de La Habana y el paisaje de Viñales",
        goal="Analyze Havana's colonial architecture and Viñales' karst landscape using advanced descriptive vocabulary and relative clauses.",
        grammar_desc="recursos descriptivos cultos, oraciones adjetivas compuestas y léxico patrimonial cubano",
        grammar_ref=f"grammar/b2/{lc1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc1}-voc.json",
        ex_ref=f"exercises/b2/{lc1}-ex.json",
        ex_ids=[f"{lc1}.ex01", f"{lc1}.ex02", f"{lc1}.ex03", f"{lc1}.ex04", f"{lc1}.ex05", f"{lc1}.ex06"],
        goals=[
            "Examine the architectural evolution of Havana from colonial fortifications to Art Deco.",
            "Describe the karst topography and traditional tobacco agriculture of Viñales.",
            "Deploy heritage and geographical vocabulary (mogote, vega, alero, vitral, mediopunto)."
        ],
        story_ref=f"stories/world/b2/{lc1}.json"
    ))

    # Lesson 2: b2-cuba-02 - José Martí y la forja de la independencia patria
    lc2 = "b2-cuba-02"
    write_json(f"vocabulary/b2/{lc2}-voc.json", {
        "id": "vocab.b2.cuba.02",
        "lesson": lc2,
        "title": "El pensamiento martiano y la emancipación antillana",
        "theme": "Vocabulario de ideario político, prosa modernista y soberanía",
        "words": [
            {"lemma": "el ideario", "translation": "ideology, body of ideas", "pos": "noun"},
            {"lemma": "el apóstol", "translation": "apostle, dedicated champion", "pos": "noun"},
            {"lemma": "la emancipación", "translation": "emancipation, liberation", "pos": "noun"},
            {"lemma": "la contienda", "translation": "contest, battle, struggle", "pos": "noun"},
            {"lemma": "desterrado", "translation": "exiled, banished", "pos": "adjective"},
            {"lemma": "reivindicación", "translation": "vindication, rightful demand", "pos": "noun"},
            {"lemma": "antimperialista", "translation": "anti-imperialist", "pos": "adjective"},
            {"lemma": "la trinchera", "translation": "trench, bastion", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{lc2}-a-gr.json", {
        "id": "grammar.b2.cuba.02.jose-marti",
        "title": "José Martí y la forja de la independencia patria",
        "sections": [
            {
                "type": "text",
                "title": "El discurso político y la prosa ensayística martiana",
                "content": "La prosa de José Martí inauguró el Modernismo literario en Hispanoamérica al fundir belleza estética con agudeza política. En el nivel B2, el análisis de sus ensayos (como 'Nuestra América') requiere dominar construcciones metafóricas complejas, períodos hipotéticos en el pasado ('De no haber congregado a los veteranos, la guerra de 1895 no habría comenzado') y conectores de contraposición conceptual ('no... sino', 'lejos de... antes bien')."
            },
            {
                "type": "table",
                "title": "Recursos retóricos del ensayo martiano",
                "rows": [
                    ["Antítesis moral", "'Trincheras de ideas valen más que trincheras de piedra'"],
                    ["Condicional contrafáctico histórico", "'Si Martí no hubiera unificado a la emigración tabaquera, la causa patria habría fracasado'"],
                    ["Fórmula asertiva enfática", "'No hay proa que taje una nube de ideas'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ideario de la independencia",
                "items": [
                    {"spanish": "Martí sostuvo que si los pueblos latinoamericanos no se conocían a sí mismos, quedarían a merced de apetitos foráneos.", "english": "Martí maintained that if Latin American nations did not know themselves, they would remain at the mercy of foreign appetites."},
                    {"spanish": "En los talleres de Tampa y Cayo Hueso, los tabaqueros cubanos donaban un día de salario semanal para financiar la contienda.", "english": "In the cigar workshops of Tampa and Key West, Cuban rollers donated a day's weekly wage to finance the struggle."},
                    {"spanish": "De no haber caído heroicamente en Dos Ríos en mayo de 1895, el ideario martiano habría guiado directamente la asamblea constituyente.", "english": "Had he not fallen heroically at Dos Ríos in May 1895, Martí's body of ideas would have directly guided the constituent assembly."}
                ]
            },
            {
                "type": "tip",
                "content": "Al analizar figuras históricas consagradas, usa el pretérito indefinido para hechos puntuales ('murió en combate') y el imperfecto para posturas permanentes o idearios ('abogaba por una república inclusiva')."
            }
        ]
    })

    write_json(f"exercises/b2/{lc2}-ex.json", {
        "lesson": lc2,
        "exercises": [
            {
                "id": f"{lc2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el ideario", "ideology, body of ideas"],
                    ["la emancipación", "emancipation, liberation"],
                    ["la contienda", "contest, battle, struggle"],
                    ["la trinchera", "trench, bastion"]
                ],
                "teaches": ["b2-cuba-vocab"]
            },
            {
                "id": f"{lc2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál fue la tesis medular de José Martí en su célebre ensayo 'Nuestra América' (1891)?",
                "options": [
                    "Que los pueblos del continente debían gobernarse según su realidad propia y mestiza, no copiando modelos importados.",
                    "Que todas las colonias del Caribe debían integrarse formalmente en la monarquía constitucional española.",
                    "Que el progreso económico de las Antillas dependía exclusivamente del cultivo intensivo del tabaco de exportación."
                ],
                "correct": 0,
                "teaches": ["cuba-jose-marti-independencia"]
            },
            {
                "id": f"{lc2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si Martí no __ a los líderes militares de la Guerra de los Diez Años, la contienda de 1895 habría fracasado. (haber unido)",
                "answer": "hubiera unido",
                "english": "If Martí had not united the military leaders of the Ten Years' War, the struggle of 1895 would have failed.",
                "teaches": ["cuba-jose-marti-independencia"]
            },
            {
                "id": f"{lc2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Trincheras", "de", "ideas", "valen", "más", "que", "trincheras", "de", "piedra."],
                "solution": ["Trincheras", "de", "ideas", "valen", "más", "que", "trincheras", "de", "piedra."],
                "english": "Trenches of ideas are worth more than trenches of stone.",
                "teaches": ["cuba-jose-marti-independencia"]
            },
            {
                "id": f"{lc2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Cómo logró Martí financiar el Partido Revolucionario Cubano desde el exilio?"},
                    {"speaker": "Investigadora", "text": "_____"},
                    {"speaker": "Historiador", "text": "Una conmovedora alianza popular que unió a intelectuales y obreros de la emigración."}
                ],
                "options": [
                    "Recorrió los talleres tabaqueros de Tampa y Cayo Hueso, donde los obreros aportaban voluntariamente parte de su jornal diario.",
                    "Solicitó préstamos bancarios a las compañías navieras de vapor de Nueva York y Boston.",
                    "Organizó rifas benéficas de cuadros impresionistas en las galerías de arte de París."
                ],
                "correct": 0,
                "teaches": ["cuba-jose-marti-independencia"]
            },
            {
                "id": f"{lc2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "De no haber forjado la unidad patriótica, la independencia jamás se habría alcanzado.",
                "english": "Had he not forged patriotic unity, independence would never have been achieved.",
                "teaches": ["cuba-jose-marti-independencia"]
            }
        ]
    })

    # Regional Story 2: b2-cuba-02.json
    story_cuba_02 = {
        "id": "b2-cuba-02",
        "title": "José Martí y la forja de la independencia patria",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica biográfica e ideológica sobre José Martí: la unificación de la emigración revolucionaria, la fundación del Partido Revolucionario Cubano y el ideario ético de 'Nuestra América'.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Pocas figuras históricas encarnan con tanta pureza y dramatismo la conjunción entre la creación poética sublime y la acción revolucionaria intransigente como José Martí, proclamado por el pueblo cubano como el 'Apóstol' de su independencia nacional. Nacido en La Habana en 1853 en el seno de una familia española modesta, el joven Martí conoció muy temprano los rigores de la represión colonial: con apenas dieciséis años, tras redactar una carta donde acusaba de traidor a un condiscípulo que se había alistado como voluntario del ejército realista durante la Guerra de los Diez Años, fue condenado a seis años de trabajos forzados en las canteras de cal viva de San Lázaro. Las cadenas de hierro que laceraron sus tobillos de adolescente y el polvo abrasador que consumió sus pulmones no doblegaron su espíritu; por el contrario, grabaron en su alma un compromiso inextinguible con la libertad y la dignidad humana que orientaría cada página de su fecunda existencia."
            },
            {
                "type": "narration",
                "text": "Conmutada su pena por el destierro en España, Martí obtuvo títulos en Derecho, Filosofía y Letras en las universidades de Madrid y Zaragoza antes de emprender un periplo apasionado por México, Guatemala y Venezuela, periplo que le permitió palpar directamente los dolores, contradicciones y esperanzas de las jóvenes repúblicas hispanoamericanas. Al comprobar que muchos países liberados por Bolívar y San Martín habían caído en manos de tiranías caudillistas o élites oligárquicas que imitaban con servilismo modelos jurídicos franceses o estadounidenses, Martí comenzó a madurar su doctrina sobre la descolonización cultural y la soberanía continental. En enero de 1891 publicó en Nueva York y México su ensayo fundamental, 'Nuestra América', texto profético donde advirtió con deslumbrante clarividencia que 'el gobierno ha de nacer del país' y que 'trincheras de ideas valen más que trincheras de piedra'."
            },
            {
                "type": "narration",
                "text": "Instalado durante casi quince años en la ciudad de Nueva York como corresponsal de los periódicos más prestigiosos de Buenos Aires, Caracas y México, Martí admiró el dinamismo industrial y la energía cívica de los Estados Unidos, pero simultáneamente detectó con inquietud el surgimiento de apetitos imperialistas que amenazaban la soberanía de las Antillas. Consciente de que si Cuba caía bajo la órbita de Washington el equilibrio geopolítico del hemisferio se quebraría en perjuicio de los pueblos del sur, Martí se consagró a la titánica tarea de preparar la que denominó la 'guerra necesaria': una contienda bélica sin odio hacia el español honrado, rápida en su ejecución y generosa en sus fines, orientada a fundar una república democrática 'con todos y para el bien de todos'."
            },
            {
                "type": "narration",
                "text": "El genio político de Martí brilló de manera insuperable al lograr la reconciliación entre los veteranos legendarios de la primera guerra de independencia —figuras militares de la talla de Máximo Gómez y Antonio Maceo, el 'Titán de Bronce'— y las nuevas generaciones de jóvenes que no habían combatido en la manigua. En los talleres de tabaco de Tampa y Cayo Hueso en Florida, Martí encontró su base social más leal y abnegada: los torcedores cubanos emigrados, hombres y mujeres humildes que escuchaban sus discursos electrizantes entre el aroma a hoja curada y donaban puntualmente un día de salario por semana para comprar rifles, pertrechos y barcos. Con ellos fundó en 1892 el Partido Revolucionario Cubano, la primera organización política moderna concebida no para gobernar tras la victoria, sino como un instrumento unitario y democrático para conquistar la emancipación de Cuba y auxiliar a la de Puerto Rico."
            },
            {
                "type": "narration",
                "text": "Tras superar dolorosos reveses, como la incautación en el puerto floridano de Fernandina de tres barcos cargados de armamento que la conspiración había reunido con indecible sacrificio, Martí firmó junto al general Máximo Gómez el 'Manifiesto de Montecristi' en Santo Domingo y zarpó en una frágil goleta mercante para desembarcar en Playitas de Cajobabo, en el extremo oriental de Cuba, la noche borrascosa del 11 de abril de 1895. El poeta, que jamás había empuñado un arma en el campo de batalla, marchó a pie entre ciénagas y peñascos bajo el aguacero tropical con un revólver al cinto y una cartera repleta de notas manuscritas, sintiendo el orgullo indecible de respirar por fin el aire libre de su tierra amada."
            },
            {
                "type": "narration",
                "text": "Su destino fatal se selló apenas cinco semanas después, el mediodía del 19 de mayo de 1895 en los campos de Dos Ríos. Al estallar un tiroteo imprevisto con una columna de infantería realista, Gómez ordenó a Martí permanecer en la retaguardia para salvaguardar la vida del líder civil supremo; sin embargo, llevado por un impulso ético irresistible de congruencia heroica entre la palabra predicada y el sacrificio personal, el Apóstol espoleó su caballo blanco y cabalgó solo hacia las líneas enemigas, cayendo abatido por tres disparos de fusil Mauser entre la hierba alta y la sombra de los algarrobos."
            },
            {
                "type": "narration",
                "text": "La caída de José Martí privó a la revolución cubana de su mente más lúcida y humanista en vísperas de la victoria contra el colonialismo español y de la posterior intervención militar estadounidense de 1898. No obstante, su legado poético, sus 'Versos sencillos' y su intransigente ética antimperialista sobrevivieron a su muerte física, convirtiéndose en el faro inextinguible que ha nutrido la conciencia de cada generación de cubanos, recordándoles que la única soberanía auténtica descansa sobre el cultivo de la virtud, la justicia distributiva y la fraternidad de los humildes."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué experiencia juvenil marcó de manera indeleble la conciencia política de José Martí?",
                        "options": [
                            "Su condena a trabajos forzados en las canteras de San Lázaro a los dieciséis años por acusar de traición al régimen colonial.",
                            "Su servicio militar como oficial de artillería en las guerras carlistas en el norte de España.",
                            "Su trabajo como contable en las plantaciones azucareras de los hacendados franceses en Haití.",
                            "Su nombramiento como diplomático honorario de la corona británica en las Antillas Menores."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 detalla su condena a trabajos forzados a los dieciséis años con cadenas en las canteras de San Lázaro tras escribir una carta de protesta política."
                    },
                    {
                        "question": "¿En qué colectivo social de la emigración encontró Martí el respaldo fundamental para fundar el Partido Revolucionario Cubano?",
                        "options": [
                            "En los obreros tabaqueros de Tampa y Cayo Hueso que donaban parte de su jornal semanal.",
                            "En los banqueros y magnates navieros de Wall Street en la ciudad de Nueva York.",
                            "En las familias aristocráticas que poseían minas de plata en los Andes peruanos.",
                            "En las tripulaciones de barcos pesqueros procedentes de las islas Canarias."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 explica que los tabaqueros de Florida escuchaban a Martí y donaban un día de salario por semana para financiar la causa libertadora."
                    },
                    {
                        "question": "¿Cómo se produjo la muerte de José Martí en el combate de Dos Ríos el 19 de mayo de 1895?",
                        "options": [
                            "Avanzó a caballo hacia las líneas realistas contrariando la orden de Gómez de permanecer en retaguardia.",
                            "Fue capturado durante una reunión secreta en una choza campesina y fusilado sin juicio.",
                            "Pereció en un naufragio frente a las costas de Cajobabo antes de tocar tierra cubana.",
                            "Sucumbió a una fiebre tropical fulminante en el campamento rebelde de la serranía."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 relata que Martí, movido por un afán de coherencia heroica, cabalgó solo hacia el combate y fue alcanzado por disparos enemigos."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc2}.json", story_cuba_02)

    write_json(f"lessons/b2/{lc2}.json", make_lesson(
        stem=lc2,
        unit_num=10,
        title="José Martí y la forja de la independencia patria",
        goal="Examine the political thought and Modernist prose of José Martí, analyzing his anti-imperialist essays and the 1895 War of Independence.",
        grammar_desc="análisis de la prosa ensayística martiana, períodos hipotéticos contrafácticos y léxico de soberanía",
        grammar_ref=f"grammar/b2/{lc2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc2}-voc.json",
        ex_ref=f"exercises/b2/{lc2}-ex.json",
        ex_ids=[f"{lc2}.ex01", f"{lc2}.ex02", f"{lc2}.ex03", f"{lc2}.ex04", f"{lc2}.ex05", f"{lc2}.ex06"],
        goals=[
            "Analyze the thesis of 'Nuestra América' and Martí's anti-colonial ideology.",
            "Explain the role of the Florida cigar workers in funding the Cuban Revolutionary Party.",
            "Deploy political and literary vocabulary (ideario, emancipación, contienda, antimperialista)."
        ],
        story_ref=f"stories/world/b2/{lc2}.json"
    ))

    # Lesson 3: b2-cuba-03 - 1959: El triunfo revolucionario, la alfabetización y la Guerra Fría
    lc3 = "b2-cuba-03"
    write_json(f"vocabulary/b2/{lc3}-voc.json", {
        "id": "vocab.b2.cuba.03",
        "lesson": lc3,
        "title": "La Revolución de 1959, reformas sociales y tensiones geopolíticas",
        "theme": "Vocabulario de transformación agraria, alfabetización y Guerra Fría",
        "words": [
            {"lemma": "la zafra", "translation": "sugar cane harvest", "pos": "noun"},
            {"lemma": "el analfabetismo", "translation": "illiteracy", "pos": "noun"},
            {"lemma": "la nacionalización", "translation": "nationalization", "pos": "noun"},
            {"lemma": "el brigadista", "translation": "brigade volunteer, literacy worker", "pos": "noun"},
            {"lemma": "el embargo", "translation": "embargo, blockade", "pos": "noun"},
            {"lemma": "el cuartelazo", "translation": "military coup, garrison uprising", "pos": "noun"},
            {"lemma": "la soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "desmantelar", "translation": "to dismantle", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{lc3}-a-gr.json", {
        "id": "grammar.b2.cuba.03.revolucion-alfabetizacion",
        "title": "1959: El triunfo revolucionario, la alfabetización y la Guerra Fría",
        "sections": [
            {
                "type": "text",
                "title": "Causalidad y contrafácticos en el relato historiográfico",
                "content": "El análisis de procesos revolucionarios en nivel B2 articula relaciones de causa y consecuencia mediante conectores de causa formal ('habida cuenta de que', 'a raíz de', 'en virtud de') combinados con hipótesis contrafácticas sobre la Guerra Fría: 'Si Washington no hubiera decretado el embargo comercial total en 1962, la dependencia económica respecto a la Unión Soviética no habría alcanzado tal magnitud'."
            },
            {
                "type": "table",
                "title": "Conectores causales e hipotéticos de alto registro",
                "rows": [
                    ["Causa institucional ('en virtud de')", "'En virtud de la Ley de Reforma Agraria, los latifundios fueron expropiados'"],
                    ["Efecto acumulativo ('a raíz de')", "'A raíz de la crisis de los misiles, el planeta rozó una conflagración nuclear'"],
                    ["Contrafáctico de pasado", "'De no haberse movilizado cien mil brigadistas, no se habría erradicado el analfabetismo en un año'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate histórico contemporáneo",
                "items": [
                    {"spanish": "La campaña de alfabetización de 1961 movilizó a miles de jóvenes hacia los rincones más inaccesibles de la Sierra Maestra.", "english": "The 1961 literacy campaign mobilized thousands of young people to the most inaccessible corners of the Sierra Maestra."},
                    {"spanish": "De no haber resistido la invasión de Bahía de Cochinos en abril de 1961, el gobierno revolucionario habría sido derrocado.", "english": "Had it not resisted the Bay of Pigs invasion in April 1961, the revolutionary government would have been overthrown."},
                    {"spanish": "Las nacionalizaciones de refinerías y bancos extranjeros aceleraron la ruptura diplomática entre La Habana y Washington.", "english": "The nationalizations of refineries and foreign banks accelerated the diplomatic rupture between Havana and Washington."}
                ]
            },
            {
                "type": "tip",
                "content": "Para mantener la neutralidad analítica requerida en el nivel B2, emplea verbos de atribución y perspectiva ('los defensores argumentan que', 'los críticos señalan que', 'los documentos desclasificados revelan que')."
            }
        ]
    })

    write_json(f"exercises/b2/{lc3}-ex.json", {
        "lesson": lc3,
        "exercises": [
            {
                "id": f"{lc3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la zafra", "sugar cane harvest"],
                    ["el analfabetismo", "illiteracy"],
                    ["el brigadista", "literacy brigade volunteer"],
                    ["el embargo", "embargo, blockade"]
                ],
                "teaches": ["b2-cuba-vocab"]
            },
            {
                "id": f"{lc3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál fue el impacto social más emblemático de la Campaña Nacional de Alfabetización de 1961 en Cuba?",
                "options": [
                    "La movilización de más de cien mil jóvenes brigadistas que redujo el analfabetismo al 3.9% en menos de un año.",
                    "La creación de una red ferroviaria exclusiva para transportar profesores universitarios a las plantaciones.",
                    "La sustitución del idioma español por un dialecto técnico simplificado en las escuelas rurales."
                ],
                "correct": 0,
                "teaches": ["cuba-revolucion-1959-alfabetizacion"]
            },
            {
                "id": f"{lc3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si los brigadistas no __ las montañas de la Sierra Maestra, miles de campesinos habrían permanecido en el analfabetismo. (haber recorrido)",
                "answer": "hubieran recorrido",
                "english": "If the brigade members had not traversed the mountains of the Sierra Maestra, thousands of peasants would have remained illiterate.",
                "teaches": ["cuba-revolucion-1959-alfabetizacion"]
            },
            {
                "id": f"{lc3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "campaña", "de", "alfabetización", "transformó", "la", "educación", "en", "toda", "la", "isla."],
                "solution": ["La", "campaña", "de", "alfabetización", "transformó", "la", "educación", "en", "toda", "la", "isla."],
                "english": "The literacy campaign transformed education across the entire island.",
                "teaches": ["cuba-revolucion-1959-alfabetizacion"]
            },
            {
                "id": f"{lc3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Politólogo", "text": "¿Cómo influyó la crisis de los misiles de octubre de 1962 en la soberanía insular?"},
                    {"speaker": "Historiadora", "text": "_____"},
                    {"speaker": "Politólogo", "text": "Una tensión geopolítica extrema que marcó para siempre la historia del siglo XX."}
                ],
                "options": [
                    "Colocó a Cuba en el epicentro de la Guerra Fría cuando Washington y Moscú negociaron al borde de la guerra nuclear.",
                    "Provocó la congelación de los precios de las hortalizas frescas en los mercados de La Habana.",
                    "Incentivó la construcción de hoteles de lujo en las playas vírgenes de Varadero."
                ],
                "correct": 0,
                "teaches": ["cuba-revolucion-1959-alfabetizacion"]
            },
            {
                "id": f"{lc3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "De no haber mediado un pacto entre las superpotencias, la crisis habría desatado una guerra nuclear.",
                "english": "Had a pact between superpowers not intervened, the crisis would have triggered a nuclear war.",
                "teaches": ["cuba-revolucion-1959-alfabetizacion"]
            }
        ]
    })

    # Regional Story 3: b2-cuba-03.json
    story_cuba_03 = {
        "id": "b2-cuba-03",
        "title": "1959: El triunfo revolucionario, la alfabetización y la Guerra Fría",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica histórica de nivel B2 sobre el triunfo de la Revolución Cubana en 1959: el desmantelamiento de la dictadura de Batista, la Campaña Nacional de Alfabetización y la Crisis de los Misiles.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "La madrugada del 1 de enero de 1959 transformó de manera irreversible el destino de Cuba y la correlación de fuerzas políticas en todo el hemisferio occidental. Ante el colapso inminente de sus líneas militares y el avance implacable de las columnas guerrilleras comandadas por Ernesto 'Che' Guevara y Camilo Cienfuegos tras la batalla decisiva de Santa Clara, el dictador Fulgencio Batista abandonó secretamente la isla en un avión militar con destino a la República Dominicana, cargando consigo millones de dólares del tesoro nacional. En La Habana y Santiago de Cuba, multitudes jubilosas se volcaron a las calles para celebrar la caída de un régimen despótico que durante siete años había clausurado las libertades constitucionales, ensangrentado las ciudades con torturas policiales y convertido la economía nacional en un paraíso especulativo para casinos de la mafia estadounidense y corporaciones extranjeras."
            },
            {
                "type": "narration",
                "text": "La entrada triunfal de la 'Caravana de la Libertad' encabezada por Fidel Castro a La Habana el 8 de enero concitó el entusiasmo fervoroso de millones de ciudadanos que anhelaban la restauración de la democracia y la justicia social. Sin embargo, el rumbo del proceso se radicalizó con una celeridad vertiginosa: en mayo de 1959 se promulgó la Primera Ley de Reforma Agraria, que proscribió el latifundio, limitó la posesión de la tierra a cuatrocientas hectáreas y distribuyó títulos de propiedad a más de cien mil campesinos arrendatarios y aparceros que vivían en condiciones feudales. Cuando las compañías estadounidenses que controlaban el negocio azucarero, los servicios telefónicos y las refinerías de petróleo se opusieron a las compensaciones ofrecidas, el gobierno revolucionario procedió a su nacionalización masiva, precipitando la ruptura diplomática con Washington en enero de 1961."
            },
            {
                "type": "narration",
                "text": "En medio de este clima de confrontación geopolítica creciente, Cuba emprendió la que la UNESCO calificaría posteriormente como una de las gestas pedagógicas más extraordinarias del siglo XX: la Campaña Nacional de Alfabetización de 1961. En una isla donde casi un millón de personas —más del veintitrés por ciento de la población adulta, concentrada principalmente en las zonas rurales— no sabía leer ni escribir, el gobierno movilizó a más de doscientos cincuenta mil educadores voluntarios. Entre ellos destacaron cien mil adolescentes y jóvenes de secundaria, conocidos como los brigadistas 'Conrado Benítez', quienes empacaron en sus mochilas un farol chino de queroseno, la cartilla de lectura 'Venceremos' y un par de mudas de ropa para marchar a pie hacia los rincones más inaccesibles de la Sierra Maestra, la Ciénaga de Zapata y los llanos del Camagüey."
            },
            {
                "type": "narration",
                "text": "Durante meses inolvidables, aquellos jóvenes citadinos compartieron la choza de tierra apisonada de los campesinos, labraron los sembradíos durante el día y enseñaron las primeras letras a la luz temblorosa del farol por las noches, enseñando a firmar por primera vez a ancianos cuyas manos encallecidas jamás habían sujetado un lápiz. A pesar de los ataques de bandas armadas opositoras en las montañas que costaron la vida a varios maestros voluntarios, la campaña culminó el 22 de diciembre de 1961 en la plaza de la Revolución con un saldo apabullante: más de setecientas mil personas fueron alfabetizadas, reduciendo el índice de analfabetismo al 3.9 por ciento y declarando a Cuba como el primer territorio libre de analfabetismo en América Latina."
            },
            {
                "type": "narration",
                "text": "La radicalización del modelo cubano y su proclamación como revolución socialista en vísperas del desembarco mercenario de Bahía de Cochinos (Playa Girón) en abril de 1961 —donde las milicias populares derrotaron a una brigada invasora financiada por la CIA en apenas sesenta y seis horas— sellaron la alianza estratégica de La Habana con la Unión Soviética. El punto culminante de esta confrontación se produjo en octubre de 1962 durante la 'Crisis de los Misiles'. El descubrimiento por parte de aviones espías estadounidenses de rampas nucleares soviéticas instaladas en suelo cubano desató un bloqueo naval de Washington y colocó al planeta al borde de una catástrofe atómica mundial durante trece días de angustia cósmica."
            },
            {
                "type": "narration",
                "text": "El acuerdo final alcanzado directamente entre John F. Kennedy y Nikita Jrushchov a espaldas del liderazgo cubano —mediante el cual Moscú retiró los misiles a cambio del compromiso estadounidense de no invadir la isla y de retirar sus propios cohetes desplegados en Turquía— causó una profunda indignación en La Habana, revelando la vulnerabilidad de las pequeñas naciones atrapadas en las componendas de las superpotencias. A partir de entonces, Washington endureció el embargo comercial, financiero y marítimo que perdura hasta el presente, mientras Cuba reconstruía sus estructuras institucionales bajo la tutela técnica y el subsidio petrolero del bloque socialista europeo."
            },
            {
                "type": "narration",
                "text": "A sesenta y cinco años de aquellos acontecimientos sísmicos, el año 1959 sigue constituyendo la gran encrucijada de la historia contemporánea de Cuba. Si bien la revolución erradicó el analfabetismo, universalizó el acceso a la salud pública y forjó una soberanía internacional que desafió al mayor imperio del planeta, el régimen resultante instauró un monopolio político unipartidista y una centralización económica que limitarían severamente las libertades individuales y la prosperidad productiva, dejando abierta una compleja dialéctica entre conquistas sociales indiscutibles y contradicciones institucionales irresueltas."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué medida agraria fundamental adoptó el gobierno revolucionario cubano en mayo de 1959?",
                        "options": [
                            "La Primera Ley de Reforma Agraria que prohibió los latifundios y entregó títulos a más de cien mil campesinos.",
                            "La venta de las tierras cultivables a compañías transnacionales de granos y fertilizantes.",
                            "La importación obligatoria de azúcar refinada procedente de los puertos del mar Báltico.",
                            "El desalojo forzoso de los pequeños productores agrícolas para construir complejos hoteleros."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que la Primera Ley de Reforma Agraria proscribió el latifundio y repartió tierras a más de cien mil campesinos arrendatarios."
                    },
                    {
                        "question": "¿Cómo se estructuró la Campaña Nacional de Alfabetización de 1961 según el texto?",
                        "options": [
                            "Mediante la movilización de más de cien mil brigadistas jóvenes que convivieron con los campesinos en el campo.",
                            "A través de transmisiones televisivas diarias emitidas por satélites de telecomunicaciones soviéticos.",
                            "Mediante cursos por correspondencia administrados por funcionarios consulares desde México.",
                            "A través de la contratación de maestros de primaria jubilados de los países escandinavos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 describe cómo cien mil brigadistas jóvenes marcharon con faroles chinos y cartillas hacia las zonas rurales para alfabetizar en las chozas campesinas."
                    },
                    {
                        "question": "¿Qué provocó la profunda indignación del gobierno cubano al concluir la Crisis de los Misiles en octubre de 1962?",
                        "options": [
                            "Que el pacto de retirada de los misiles fue negociado directamente entre Kennedy y Jrushchov sin consultar a La Habana.",
                            "Que la Unión Soviética exigió el pago inmediato de toda la deuda azucarera en lingotes de oro.",
                            "Que las Naciones Unidas impusieron una administración militar permanente en el puerto de Santiago de Cuba.",
                            "Que los diplomáticos cubanos fueron expulsados de la asamblea general en la ciudad de Ginebra."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 señala que Kennedy y Jrushchov acordaron la retirada de los misiles a espaldas del liderazgo cubano, lo que generó malestar en la isla."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc3}.json", story_cuba_03)

    write_json(f"lessons/b2/{lc3}.json", make_lesson(
        stem=lc3,
        unit_num=10,
        title="1959: El triunfo revolucionario, la alfabetización y la Guerra Fría",
        goal="Analyze the 1959 Cuban Revolution, the National Literacy Campaign, and the Missile Crisis using causal and counterfactual structures.",
        grammar_desc="conectores de causa formal, oraciones contrafácticas de la Guerra Fría y léxico geopolítico",
        grammar_ref=f"grammar/b2/{lc3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc3}-voc.json",
        ex_ref=f"exercises/b2/{lc3}-ex.json",
        ex_ids=[f"{lc3}.ex01", f"{lc3}.ex02", f"{lc3}.ex03", f"{lc3}.ex04", f"{lc3}.ex05", f"{lc3}.ex06"],
        goals=[
            "Examine the agrarian and social reforms of the Cuban Revolution in 1959.",
            "Analyze the logistical organization and educational impact of the 1961 Literacy Campaign.",
            "Deploy Cold War historical and political vocabulary (zafra, analfabetismo, brigadista, embargo)."
        ],
        story_ref=f"stories/world/b2/{lc3}.json"
    ))

    # Lesson 4: b2-cuba-04 - El son, la trova y el auge del cine cubano
    lc4 = "b2-cuba-04"
    write_json(f"vocabulary/b2/{lc4}-voc.json", {
        "id": "vocab.b2.cuba.04",
        "lesson": lc4,
        "title": "Música patrimonial, Nueva Trova y cinematografía del ICAIC",
        "theme": "Vocabulario de musicología caribeña, son cubano y crítica de cine",
        "words": [
            {"lemma": "el tres", "translation": "Cuban tres (three-course guitar)", "pos": "noun"},
            {"lemma": "la síncopa", "translation": "syncopation", "pos": "noun"},
            {"lemma": "el trovador", "translation": "troubadour, singer-songwriter", "pos": "noun"},
            {"lemma": "el guantelete", "translation": "gauntlet, iron glove", "pos": "noun"},
            {"lemma": "la cadencia", "translation": "cadence, rhythmic flow", "pos": "noun"},
            {"lemma": "el celuloide", "translation": "celluloid, film", "pos": "noun"},
            {"lemma": "revitalizar", "translation": "to revitalize", "pos": "verb"},
            {"lemma": "el virtuosismo", "translation": "virtuosity", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{lc4}-a-gr.json", {
        "id": "grammar.b2.cuba.04.son-trova-cine",
        "title": "El son, la trova y el auge del cine cubano",
        "sections": [
            {
                "type": "text",
                "title": "Análisis estético y crítica cultural en registro formal",
                "content": "La crítica musical y cinematográfica en nivel B2 requiere estructurar juicios de valor complejos con oraciones subordinadas sustantivas y adjetivas: 'Resulta indiscutible que el son cubano transformó la música popular universal mediante la síncopa de la clave'; 'Películas emblemáticas como Memorias del subdesarrollo articulan una lúcida reflexión sobre las vacilaciones del intelectual burgués ante el cambio histórico'."
            },
            {
                "type": "table",
                "title": "Fórmulas de valoración estética y cinematográfica",
                "rows": [
                    ["Constatación de impacto", "'Es innegable que la Nueva Trova fundió la lírica poética con el compromiso social'"],
                    ["Juicio crítico con subjuntivo", "'Es sorprendente que un cine con recursos tan precarios lograra semejante maestría visual'"],
                    ["Aposición explicativa", "'Tomás Gutiérrez Alea, considerado el cineasta más lúcido del cine revolucionario'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en crítica cultural iberoamericana",
                "items": [
                    {"spanish": "El timbre metálico del tres cubano sostiene el entramado rítmico del son tradicional desde las montañas de Oriente.", "english": "The metallic timbre of the Cuban tres sustains the rhythmic framework of traditional son from the mountains of Oriente."},
                    {"spanish": "Silvio Rodríguez y Pablo Milanés crearon canciones que definieron la banda sonora sentimental de varias generaciones.", "english": "Silvio Rodríguez and Pablo Milanés created songs that defined the emotional soundtrack of several generations."},
                    {"spanish": "El Instituto Cubano del Arte e Industria Cinematográficos (ICAIC) promovió un cine descolonizador de renombre mundial.", "english": "The Cuban Institute of Cinematographic Art and Industry (ICAIC) promoted world-renowned decolonizing cinema."}
                ]
            },
            {
                "type": "tip",
                "content": "Al redactar sobre cine y música, combina términos técnicos precisos (síncopa, clave 3-2, plano secuencia, voz en off) con conectores argumentativos de matiz ('lejos de ser una mera recreación folclórica...')."
            }
        ]
    })

    write_json(f"exercises/b2/{lc4}-ex.json", {
        "lesson": lc4,
        "exercises": [
            {
                "id": f"{lc4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el tres", "Cuban three-course guitar"],
                    ["la síncopa", "syncopation"],
                    ["el trovador", "troubadour, singer-songwriter"],
                    ["la cadencia", "cadence, rhythmic flow"]
                ],
                "teaches": ["b2-cuba-vocab"]
            },
            {
                "id": f"{lc4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué obra cumbre del cine cubano dirigida por Tomás Gutiérrez Alea en 1968 retrata el desgarramiento de un intelectual burgués en La Habana?",
                "options": [
                    "Memorias del subdesarrollo, basada en la novela de Edmundo Desnoes.",
                    "Fresa y chocolate, nominada al premio Óscar de la Academia.",
                    "Lucía, dirigida por Humberto Solás en tres episodios históricos."
                ],
                "correct": 0,
                "teaches": ["cuba-son-nueva-trova-cine"]
            },
            {
                "id": f"{lc4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Es admirable que el movimiento de la Nueva Trova __ la poesía culta con las raíces populares de la canción campesina. (haber fusionado)",
                "answer": "haya fusionado",
                "english": "It is admirable that the Nueva Trova movement has fused educated poetry with the popular roots of peasant song.",
                "teaches": ["cuba-son-nueva-trova-cine"]
            },
            {
                "id": f"{lc4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "son", "cubano", "fundó", "las", "bases", "de", "la", "salsa", "internacional."],
                "solution": ["El", "son", "cubano", "fundó", "las", "bases", "de", "la", "salsa", "internacional."],
                "english": "Cuban son laid the foundations of international salsa.",
                "teaches": ["cuba-son-nueva-trova-cine"]
            },
            {
                "id": f"{lc4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Musicóloga", "text": "¿Por qué el disco Buena Vista Social Club causó tanto furor en el mundo en los años noventa?"},
                    {"speaker": "Crítico", "text": "_____"},
                    {"speaker": "Musicóloga", "text": "Una auténtica reivindicación de la elegancia y el duende del son oriental."}
                ],
                "options": [
                    "Porque rescató del olvido a leyendas octogenarias como Compay Segundo e Ibrahim Ferrer con grabaciones íntimas de enorme pureza acústica.",
                    "Porque introdujo guitarras eléctricas distorsionadas y sintetizadores digitales en el bolero tradicional.",
                    "Porque fue financiado íntegramente por los sellos discográficos de música tecno de Berlín."
                ],
                "correct": 0,
                "teaches": ["cuba-son-nueva-trova-cine"]
            },
            {
                "id": f"{lc4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El compás de la síncopa y el repique del bongó definen la cadencia del son.",
                "english": "The beat of the syncopation and the ring of the bongo define the cadence of son.",
                "teaches": ["cuba-son-nueva-trova-cine"]
            }
        ]
    })

    # Regional Story 4: b2-cuba-04.json
    story_cuba_04 = {
        "id": "b2-cuba-04",
        "title": "El son, la trova y el auge del cine cubano",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica cultural sobre los motores artísticos de Cuba: el nacimiento del son en Oriente, la poesía musical de la Nueva Trova y la cinematografía revolucionaria del ICAIC.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Si existe una manifestación artística en la que Cuba ha ejercido una influencia universal desproporcionada respecto a sus dimensiones geográficas, esa es indudablemente la música. Crisol sonoro donde se fundieron las complejas polirritmias africanas de los esclavos yorubas, congos y carabalíes con las décimas poéticas y las cadencias armónicas de los campesinos españoles procedentes de Andalucía y las islas Canarias, la isla engendró un abanico asombroso de géneros que revolucionarían la sensibilidad acústica del siglo XX: el danzón, el cha-cha-chá, el mambo, el bolero y, por encima de todos ellos como columna vertebral imperecedera, el son cubano."
            },
            {
                "type": "narration",
                "text": "Nacido a finales del siglo XIX en las serranías orientales de Santiago de Cuba, Guantánamo y Baracoa, el son constituyó una síntesis prodigiosa: sobre el patrón rítmico implacable marcado por la clave de madera —dos palos de caoba dura que dictan la métrica sagrada del compás tres-dos—, el 'tres' cubano despliega sus punteos sincopados metálicos mientras el bongó y las maracas rellenan el tejido tímbrico antes de que la voz del sonero entable un diálogo improvisado con el coro en el tradicional 'montuno'. Cuando los septetos de son desembarcaron en los salones de baile de La Habana en los años veinte, rompieron las barreras raciales y aristocráticas que marginaban a la música afrocubana, conquistando primero la radio y los sellos discográficos internacionales y fundando las bases rítmicas de lo que décadas más tarde la diáspora latina en Nueva York bautizaría universalmente como 'salsa'."
            },
            {
                "type": "narration",
                "text": "Tras el triunfo de la revolución de 1959, la efervescencia sociopolítica encontró su cauce lírico más depurado en el movimiento de la 'Nueva Trova'. Encabezado por compositores e intérpretes extraordinarios como Silvio Rodríguez, Pablo Milanés y Noel Nicola, este movimiento renovó radicalmente la vieja tradición de los trovadores errantes de cafetín. Despojando a la canción romántica de lugares comunes y cursilerías melosas, los nuevos trovadores armados únicamente con sus guitarras de cuerdas de nailon compusieron auténticas piezas maestras de la poesía hispanoamericana contemporánea. Canciones inmortales como 'Playa Girón', 'Ojalá', 'Yolanda' y 'Para vivir' fusionaron la metáfora vanguardista con el anhelo utópico de construcción de un 'hombre nuevo', convirtiéndose en la banda sonora sentimental de la juventud contestataria de toda América Latina y España durante las décadas de los setenta y ochenta."
            },
            {
                "type": "narration",
                "text": "En el terreno cinematográfico, el gobierno revolucionario fundó apenas tres meses después de llegar al poder el Instituto Cubano del Arte e Industria Cinematográficos (ICAIC), la primera institución cultural creada por el nuevo Estado. Concebido bajo el lema del 'cine imperfecto' teorizado por Julio García Espinosa —un cine despojado de artificios comerciales hollywoodenses que aspiraba a provocar la reflexión crítica del espectador antes que su mero entretenimiento pasivo—, el ICAIC produjo una edad de oro cinematográfica que situó a Cuba en la vanguardia del Nuevo Cine Latinoamericano."
            },
            {
                "type": "narration",
                "text": "La cumbre indiscutible de esta cinematografía llegó en 1968 con 'Memorias del subdesarrollo', dirigida por Tomás Gutiérrez Alea ('Titón') a partir de la novela homónima de Edmundo Desnoes. A través de la mirada escéptica y alienada de Sergio, un intelectual burgués que decide permanecer en La Habana tras la huida de su familia a Miami durante la Crisis de los Misiles, el filme utiliza el collage documental, la voz en off y la introspección sicológica para diseccionar las contradicciones morales de una clase social agonizante frente a la marea colectiva de una revolución arrolladora. Considerada unánimemente por la crítica internacional como una de las cien mejores películas de la historia del cine mundial, la obra demostró que el celuloide revolucionario era capaz de ejercer una autocrítica profunda y deslumbrante sin caer en la propaganda simplista."
            },
            {
                "type": "narration",
                "text": "Décadas después, a finales de los años noventa, cuando el país atravesaba las penurias extremas del Período Especial, la música tradicional cubana experimentó una resurrección planetaria apoteósica gracias al proyecto 'Buena Vista Social Club'. Grabado en apenas seis días en los míticos estudios Areito de La Habana por el guitarrista estadounidense Ry Cooder y el productor británico Nick Gold, el álbum rescató de la penumbra y el olvido a leyendas octogenarias de la época dorada: el nonagenario Compay Segundo con su armónico y su carisma incombustible, el pianista virtuoso Rubén González, el contrabajista Cachaito López y la voz aterciopelada y melancólica de Ibrahim Ferrer, quien lustraba zapatos en las calles habaneras antes de ser llevado al micrófono."
            },
            {
                "type": "narration",
                "text": "El documental homónimo dirigido por el cineasta alemán Wim Wenders culminó con un concierto apoteósico en el Carnegie Hall de Nueva York, donde aquellos ancianos humildes hicieron llorar y bailar a miles de espectadores mientras la bandera cubana ondeaba en el escenario más prestigioso de los Estados Unidos. Así, a través de la persistencia de sus tambores sagrados, la poesía deslumbrante de sus trovadores y la lucidez crítica de sus cineastas, Cuba ha demostrado al mundo que la cultura constituye su fortaleza más inexpugnable, un tesoro inmaterial que ninguna penuria económica ni bloqueo naval podrá jamás confinar al silencio."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué instrumento de tres órdenes de cuerdas dobles desempeña un papel melódico y rítmico central en el son cubano?",
                        "options": [
                            "El tres cubano.",
                            "El charango andino.",
                            "El cuatro venezolano.",
                            "El bandoneón porteño."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 subraya que sobre la métrica de la clave, el tres cubano despliega sus punteos sincopados metálicos en el son tradicional."
                    },
                    {
                        "question": "¿Cuál fue el aporte estético y poético más notable del movimiento de la Nueva Trova en Cuba?",
                        "options": [
                            "Renovar la lírica de la canción popular mediante metáforas vanguardistas y compromiso social.",
                            "Sustituir los instrumentos acústicos tradicionales por orquestaciones de música electrónica industrial.",
                            "Componer exclusivamente himnos militares de marcha para desfiles patrióticos obligatorios.",
                            "Traducir literalmente canciones folk estadounidenses para promover el acercamiento diplomático."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 describe cómo cantautores como Silvio Rodríguez y Pablo Milanés fundieron la poesía culta con el anhelo ético y la metáfora vanguardista."
                    },
                    {
                        "question": "¿Qué impacto internacional tuvo el disco y documental 'Buena Vista Social Club' a finales de los noventa?",
                        "options": [
                            "Rescató del olvido a leyendas septuagenarias del son tradicional y las consagró en escenarios globales como el Carnegie Hall.",
                            "Demostró la bancarrota definitiva de los estudios de grabación analógicos en el Caribe.",
                            "Provocó la prohibición total del bolero romántico en las emisoras de radio internacionales.",
                            "Generó una disputa legal que obligó a clausurar todas las salas de cine en la capital cubana."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los párrafos 6 y 7 relatan cómo el proyecto grabado por Ry Cooder devolvió la gloria internacional a maestros como Compay Segundo e Ibrahim Ferrer."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc4}.json", story_cuba_04)

    write_json(f"lessons/b2/{lc4}.json", make_lesson(
        stem=lc4,
        unit_num=10,
        title="El son, la trova y el auge del cine cubano",
        goal="Explore Cuban musicology (son, Buena Vista) and cinema (ICAIC, Memorias del subdesarrollo) using cultural criticism and aesthetic registers.",
        grammar_desc="fórmulas de valoración estética, léxico musicológico del Caribe y crítica cinematográfica",
        grammar_ref=f"grammar/b2/{lc4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc4}-voc.json",
        ex_ref=f"exercises/b2/{lc4}-ex.json",
        ex_ids=[f"{lc4}.ex01", f"{lc4}.ex02", f"{lc4}.ex03", f"{lc4}.ex04", f"{lc4}.ex05", f"{lc4}.ex06"],
        goals=[
            "Examine the Afro-Cuban origins and rhythmic structure of traditional son.",
            "Analyze the lyrical poetry of the Nueva Trova and the cinema of Gutiérrez Alea.",
            "Deploy musicological and cinematographic vocabulary (tres, síncopa, trovador, celuloide)."
        ],
        story_ref=f"stories/world/b2/{lc4}.json"
    ))

    # Lesson 5: b2-cuba-05 - Del Período Especial a la nueva economía y el éxodo contemporáneo
    lc5 = "b2-cuba-05"
    write_json(f"vocabulary/b2/{lc5}-voc.json", {
        "id": "vocab.b2.cuba.05",
        "lesson": lc5,
        "title": "El Período Especial, remesas y reformas socioeconómicas",
        "theme": "Vocabulario de resiliencia económica, dualidad monetaria y diáspora",
        "words": [
            {"lemma": "el cuentapropismo", "translation": "self-employment, small private enterprise", "pos": "noun"},
            {"lemma": "la remesa", "translation": "remittance", "pos": "noun"},
            {"lemma": "la libreta", "translation": "ration book (libreta de abastecimiento)", "pos": "noun"},
            {"lemma": "el apagón", "translation": "blackout, power outage", "pos": "noun"},
            {"lemma": "el jineterismo", "translation": "informal hustling, street touting", "pos": "noun"},
            {"lemma": "el éxodo", "translation": "exodus, mass emigration", "pos": "noun"},
            {"lemma": "la dualidad", "translation": "duality", "pos": "noun"},
            {"lemma": "paliar", "translation": "to alleviate, to mitigate", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{lc5}-a-gr.json", {
        "id": "grammar.b2.cuba.05.periodo-especial",
        "title": "Del Período Especial a la nueva economía y el éxodo contemporáneo",
        "sections": [
            {
                "type": "text",
                "title": "Concesión compleja y prospectiva económica",
                "content": "El análisis de la realidad socioeconómica contemporánea de Cuba en nivel B2 moviliza estructuras concesivas complejas ('a pesar de las tímidas aperturas al cuentapropismo', 'si bien las remesas alivian el consumo de las familias', 'por más que las reformas intenten captar divisas') combinadas con hipótesis sobre reformas de mercado."
            },
            {
                "type": "table",
                "title": "Estructuras de balance y contraste económico",
                "rows": [
                    ["Concesiva con indicativo ('si bien')", "'Si bien la dualidad monetaria protegió el salario estatal, distorsionó los precios relativos'"],
                    ["Concesiva intensiva ('por más que')", "'Por más que el gobierno promueva el turismo, la escasez de combustible paraliza la industria'"],
                    ["Prospectiva condicional", "'Si no se desmantelan las trabas burocráticas, la inversión foránea seguirá estancada'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo sociológico contemporáneo",
                "items": [
                    {"spanish": "El colapso de la Unión Soviética en 1991 privó a Cuba del 85% de su comercio exterior de la noche a la mañana.", "english": "The collapse of the Soviet Union in 1991 deprived Cuba of 85% of its foreign trade overnight."},
                    {"spanish": "Las familias cubanas subsistieron durante el Período Especial gracias a una ingeniosa capacidad de resistencia cotidiana.", "english": "Cuban families survived during the Special Period thanks to an ingenious capacity for everyday resilience."},
                    {"spanish": "El auge de los negocios privados o mipymes convive con una inflación que golpea con dureza a los jubilados estatales.", "english": "The rise of private businesses or MSMEs coexists with inflation that hits state retirees hard."}
                ]
            },
            {
                "type": "tip",
                "content": "Para describir fenómenos de migración y economía informal en registro culto, utiliza sustantivos abstractos y verbos precisos: 'éxodo migratorio', 'captación de divisas', 'brecha de desigualdad', 'paliar la carestía'."
            }
        ]
    })

    write_json(f"exercises/b2/{lc5}-ex.json", {
        "lesson": lc5,
        "exercises": [
            {
                "id": f"{lc5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el cuentapropismo", "self-employment, private business"],
                    ["la remesa", "remittance"],
                    ["la libreta", "ration book"],
                    ["el apagón", "blackout, power outage"]
                ],
                "teaches": ["b2-cuba-vocab"]
            },
            {
                "id": f"{lc5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué fenómeno socioeconómico traumático definió a Cuba durante el 'Período Especial en tiempo de paz' en los años noventa?",
                "options": [
                    "El desplome de la economía tras la caída de la Unión Soviética, marcado por apagones masivos y drástica escasez de alimentos.",
                    "La adopción del dólar como moneda única y la disolución inmediata de todas las empresas estatales.",
                    "La construcción acelerada de plantas de energía nuclear financiadas por bancos escandinavos."
                ],
                "correct": 0,
                "teaches": ["cuba-periodo-especial-economia-diaspora"]
            },
            {
                "id": f"{lc5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Por más que las familias __ remesas desde el exterior, la inflación erosiona el poder adquisitivo en la isla. (recibir - subjuntivo)",
                "answer": "reciban",
                "english": "However much families receive remittances from abroad, inflation erodes purchasing power on the island.",
                "teaches": ["cuba-periodo-especial-economia-diaspora"]
            },
            {
                "id": f"{lc5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "cuentapropismo", "abrió", "espacios", "para", "la", "iniciativa", "privada", "local."],
                "solution": ["El", "cuentapropismo", "abrió", "espacios", "para", "la", "iniciativa", "privada", "local."],
                "english": "Self-employment opened spaces for local private initiative.",
                "teaches": ["cuba-periodo-especial-economia-diaspora"]
            },
            {
                "id": f"{lc5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Economista", "text": "¿Cómo ha transformado la autorización de las mipymes la vida cotidiana en las ciudades cubanas?"},
                    {"speaker": "Socióloga", "text": "_____"},
                    {"speaker": "Economista", "text": "Una paradoja latente entre el dinamismo del mercado y la equidad social revolucionaria."}
                ],
                "options": [
                    "Ha multiplicado la oferta de alimentos y artículos importados, aunque ha agudizado la brecha económica frente a quienes dependen solo de un salario estatal.",
                    "Ha eliminado por completo el uso de teléfonos celulares en las áreas suburbanas de Matanzas.",
                    "Ha sustituido los barcos de carga por hidroaviones en el tráfico comercial con las Bahamas."
                ],
                "correct": 0,
                "teaches": ["cuba-periodo-especial-economia-diaspora"]
            },
            {
                "id": f"{lc5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las remesas familiares mitigan la carestía provocada por la inflación y los apagones.",
                "english": "Family remittances mitigate the shortages caused by inflation and blackouts.",
                "teaches": ["cuba-periodo-especial-economia-diaspora"]
            }
        ]
    })

    # Regional Story 5: b2-cuba-05.json
    story_cuba_05 = {
        "id": "b2-cuba-05",
        "title": "Del Período Especial a la nueva economía y el éxodo contemporáneo",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociológica de nivel B2 sobre la resiliencia cubana desde el Período Especial: el impacto de la caída soviética, la dualidad monetaria, el cuentapropismo y la crisis migratoria del siglo XXI.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "La desintegración formal de la Unión Soviética en diciembre de 1991 asestó a la sociedad cubana el golpe económico y existencial más devastador de su historia republicana. En cuestión de meses, la isla caribeña perdió de manera fulminante el ochenta y cinco por ciento de su comercio exterior, los créditos subsidiados y el suministro vital de trece millones de toneladas anuales de petróleo soviético que alimentaban sus centrales termoeléctricas, tractores y fábricas. El producto interno bruto se desplomó un treinta y cinco por ciento entre 1989 y 1993, inaugurando una etapa de penuria extrema bautizada oficialmente con el eufemismo castrense de 'Período Especial en tiempo de paz', un cataclismo material que obligó a once millones de ciudadanos a librar una titánica batalla diaria por la mera supervivencia física."
            },
            {
                "type": "narration",
                "text": "La vida cotidiana en las ciudades y campos cubanos durante los primeros años noventa se convirtió en una pesadilla de privaciones casi inimaginables en el mundo moderno. Los 'apagones' eléctricos de dieciséis horas diarias paralizaban los hogares en medio del calor asfixiante del verano antillano, el transporte público colapsó hasta el punto de que La Habana se inundó de medio millón de pesadas bicicletas chinas marca 'Forever' importadas de urgencia, y la tradicional 'libreta de abastecimiento' racionada vio reducirse sus raciones a cuotas simbólicas de arroz, frijoles y azúcar que apenas alcanzaban para diez días al mes. Ante la escasez casi total de combustible y fertilizantes químicos, la agricultura campesina debió reinventarse sobre la marcha mediante la tracción animal con bueyes y la creación pionera de 'organopónicos' y huertos urbanos comunitarios en solares abandonados, modelo agroecológico que la comunidad científica internacional elogiaría como un hito de sostenibilidad forzada."
            },
            {
                "type": "narration",
                "text": "Para evitar el colapso definitivo del Estado, el gobierno implementó a partir de 1993 una serie de reformas heterodoxas que alteraron profundamente el pacto social igualitario forjado en las décadas anteriores. Se despenalizó la tenencia de divisas extranjeras, se autorizó la inversión foránea en complejos hoteleros bajo empresas mixtas, se abrieron mercados agropecuarios de libre oferta y demanda, y se autorizó con cautela el 'cuentapropismo' o trabajo privado por cuenta propia en más de cien oficios artesanales y de servicios gastronómicos. La apertura al turismo internacional inyectó los dólares necesarios para mantener a flote los sistemas públicos universales de salud y educación; sin embargo, engendró una compleja 'dualidad económica y monetaria' donde quienes recibían propinas en hoteles o remesas familiares enviadas desde Miami y Madrid disfrutaban de un poder adquisitivo infinitamente superior al de médicos, ingenieros y maestros que cobraban modestos salarios en pesos cubanos sin acceso directo a las tiendas en divisas."
            },
            {
                "type": "narration",
                "text": "Esta profunda fractura socioeconómica y la desesperanza juvenil alimentaron sucesivas olas migratorias de dramatismo sobrecogedor. En el caluroso verano de 1994, tras las insólitas protestas callejeras conocidas como el 'Maleconazo', más de treinta y cinco mil cubanos se lanzaron al estrecho de la Florida en frágiles balsas caseras construidas con cámaras de camión, tablas de madera y lonas desgarradas en la célebre 'Crisis de los Balseros'. La tragedia marítima forzó a las administraciones de Bill Clinton y Fidel Castro a firmar nuevos acuerdos migratorios bilaterales para canalizar un éxodo legal mediante una cuota mínima de veinte mil visas anuales, estableciendo la controvertida política de 'pies secos, pies mojados'."
            },
            {
                "type": "narration",
                "text": "El breve deshielo diplomático iniciado en diciembre de 2014 por los presidentes Barack Obama y Raúl Castro —simbolizado por la reapertura de embajadas, la histórica visita presidencial estadounidense a La Habana en 2016 y la llegada de cruceros y vuelos comerciales directos— desató una ola de esperanza sin precedentes entre los emprendedores cubanos que abrieron restaurantes privados ('paladares') y alquilaron habitaciones a turistas de todo el planeta. Sin embargo, aquel florecimiento resultó efímero: el posterior endurecimiento implacable del embargo bajo la administración de Donald Trump con más de doscientas cuarenta nuevas sanciones, la inclusión de Cuba en la lista de Estados patrocinadores del terrorismo y el impacto devastador de la pandemia mundial de COVID-19 en 2020 volvieron a estrangular la maltrecha economía insular."
            },
            {
                "type": "narration",
                "text": "A partir de 2021, la implementación de una traumática reforma monetaria destinada a unificar las dos monedas desencadenó una inflación descontrolada que pulverizó los salarios y pensiones estatales. La crónica escasez de medicamentos esenciales, el desabastecimiento de alimentos y el deterioro del sistema electroenergético nacional provocaron las históricas manifestaciones populares del 11 de julio de 2021 (el '11J'), las más extendidas y masivas en seis décadas de revolución. La posterior respuesta gubernamental combinó el endurecimiento penal de las protestas con una tímida flexibilización económica que permitió por primera vez la creación formal de pequeñas y medianas empresas privadas (mipymes), abriendo un mercado comercial dual donde conviven estantes rebosantes de artículos importados a precios prohibitivos con largas filas de jubilados ante las bodegas estatales."
            },
            {
                "type": "narration",
                "text": "El resultado inmediato de esta combinación explosiva de asfixia material, desesperanza juvenil y cerrazón política ha sido el mayor éxodo migratorio en la historia de la nación: entre 2022 y 2024, más de medio millón de cubanos —casi el cinco por ciento de la población total, concentrada en sus estratos más jóvenes y calificados— abandonaron la isla por vía aérea o a través de extenuantes rutas terrestres centroamericanas hacia la frontera de los Estados Unidos. Así, la Cuba de hoy se debate en una encrucijada existencial inaplazable: preservar las conquistas de soberanía y justicia social que enorgullecieron a su pueblo durante generaciones, o reinventar con urgencia sus estructuras productivas y políticas para ofrecer un horizonte digno y próspero a una ciudadanía cuya paciencia y capacidad de resistencia parecen haber alcanzado su límite histórico."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál fue la causa directa del inicio del llamado 'Período Especial en tiempo de paz' a comienzos de los noventa?",
                        "options": [
                            "La desintegración de la Unión Soviética y la pérdida fulminante del 85% del comercio exterior de la isla.",
                            "La invasión de langostas marinas que arruinó por completo la zafra azucarera en la provincia de Camagüey.",
                            "La decisión del gobierno cubano de cancelar unilateralmente todas sus exportaciones hacia el mercado europeo.",
                            "Un terremoto submarino de gran magnitud que destruyó las terminales petroleras de la bahía de Cienfuegos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 señala que la caída de la URSS privó a Cuba del 85% de su comercio, créditos subsidiados y petróleo, detonando la crisis extrema."
                    },
                    {
                        "question": "¿Qué contradicción social provocó la despenalización del dólar y la apertura al turismo internacional en 1993?",
                        "options": [
                            "Una marcada dualidad económica donde quienes recibían propinas o remesas en divisas tenían mayor poder adquisitivo que los profesionales estatales.",
                            "La desaparición absoluta de los idiomas autóctonos en las provincias orientales del país.",
                            "El cierre definitivo de todas las escuelas primarias y secundarias en las zonas rurales de la isla.",
                            "La obligación de todos los ciudadanos de comprar vehículos automotores de importación japonesa."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 explica que la dualidad monetaria privilegió a quienes captaban dólares frente a médicos, profesores e ingenieros que cobraban en moneda nacional."
                    },
                    {
                        "question": "¿Qué magnitud demográfica alcanzó el éxodo migratorio cubano entre los años 2022 y 2024 según el texto?",
                        "options": [
                            "Más de medio millón de personas, casi el 5% de la población total de la isla, principalmente jóvenes.",
                            "Apenas dos mil técnicos petroleros que fueron contratados temporalmente en el golfo de México.",
                            "Cincuenta mil diplomáticos y deportistas de alto rendimiento que solicitaron asilo político en Europa.",
                            "Menos del uno por ciento de la población jubilada que se trasladó a residencias en el Caribe insular."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 7 precisa que entre 2022 y 2024 más de quinientos mil cubanos, casi el cinco por ciento de la población, emigraron en busca de porvenir."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc5}.json", story_cuba_05)

    write_json(f"lessons/b2/{lc5}.json", make_lesson(
        stem=lc5,
        unit_num=10,
        title="Del Período Especial a la nueva economía y el éxodo contemporáneo",
        goal="Analyze the Special Period, monetary duality, cuentapropismo, and contemporary migration using concessive and speculative structures.",
        grammar_desc="estructuras concesivas complejas, léxico de resiliencia socioeconómica y análisis de la diáspora",
        grammar_ref=f"grammar/b2/{lc5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc5}-voc.json",
        ex_ref=f"exercises/b2/{lc5}-ex.json",
        ex_ids=[f"{lc5}.ex01", f"{lc5}.ex02", f"{lc5}.ex03", f"{lc5}.ex04", f"{lc5}.ex05", f"{lc5}.ex06"],
        goals=[
            "Examine the impact of the Soviet collapse on daily life and agriculture in Cuba.",
            "Analyze the emergence of dollarization, cuentapropismo, and private mipymes.",
            "Deploy socioeconomic vocabulary (cuentapropismo, remesa, libreta, apagón, éxodo)."
        ],
        story_ref=f"stories/world/b2/{lc5}.json"
    ))

    # Consolidation: b2-cuba-consolidation
    lc_con = "b2-cuba-consolidation"
    write_json(f"exercises/b2/{lc_con}-ex.json", {
        "lesson": lc_con,
        "exercises": [
            {
                "id": f"{lc_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el mogote", "karst limestone hill"],
                    ["el ideario", "ideology, body of ideas"],
                    ["la síncopa", "syncopation"],
                    ["el cuentapropismo", "self-employment, private business"]
                ],
                "teaches": ["b2-cuba-vocab"]
            },
            {
                "id": f"{lc_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué relación histórica une a los tabaqueros de Tampa y Cayo Hueso con José Martí?",
                "options": [
                    "Aportaron su salario voluntario para fundar el Partido Revolucionario Cubano y financiar la guerra de 1895.",
                    "Firmaron un pacto secreto de no agresión con las autoridades navales de la capitanía general de La Habana.",
                    "Construyeron los primeros ferrocarriles azucareros que conectaban Pinar del Río con la capital."
                ],
                "correct": 0,
                "teaches": ["cuba-jose-marti-independencia"]
            },
            {
                "id": f"{lc_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la Campaña de Alfabetización de 1961 es considerada un modelo histórico en América Latina?",
                "options": [
                    "Porque movilizó a cien mil brigadistas jóvenes y redujo el analfabetismo al 3.9% en menos de doce meses.",
                    "Porque introdujo por primera vez ordenadores personales en las aulas de las zonas montañosas.",
                    "Porque sustituyó la enseñanza de la historia por manuales de ingeniería naval británica."
                ],
                "correct": 0,
                "teaches": ["cuba-revolucion-1959-alfabetizacion"]
            },
            {
                "id": f"{lc_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si los campesinos de Viñales no __ los métodos tradicionales, el tabaco cubano habría perdido su renombre mundial. (haber mantenido)",
                "answer": "hubieran mantenido",
                "english": "If the farmers of Viñales had not maintained traditional methods, Cuban tobacco would have lost its worldwide renown.",
                "teaches": ["cuba-arquitectura-habana-vinales"]
            },
            {
                "id": f"{lc_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "La Habana colonial resguarda fortalezas de piedra coralina y plazas de traza barroca. [Colonial Havana safeguards coralline limestone forts and baroque squares.]",
                    "Martí forjó la unidad patriótica desde el exilio entre obreros tabaqueros e intelectuales. [Martí forged patriotic unity from exile among cigar workers and intellectuals.]",
                    "El triunfo revolucionario de 1959 impulsó la reforma agraria y la gesta alfabetizadora. [The revolutionary triumph of 1959 propelled agrarian reform and the literacy campaign.]",
                    "La música y el cine han demostrado ser la fortaleza cultural más inexpugnable de la isla. [Music and cinema have proven to be the island's most impregnable cultural fortress.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": [
                    "cuba-arquitectura-habana-vinales",
                    "cuba-jose-marti-independencia",
                    "cuba-revolucion-1959-alfabetizacion",
                    "cuba-son-nueva-trova-cine"
                ]
            },
            {
                "id": f"{lc_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ensayista", "text": "¿Cómo resumiría usted la paradoja de la identidad cubana contemporánea?"},
                    {"speaker": "Sociólogo", "text": "_____"},
                    {"speaker": "Ensayista", "text": "Una tensión permanente entre la utopía colectiva, la dignidad patriótica y las urgencias materiales del individuo."}
                ],
                "options": [
                    "Es la fascinante contradicción de un pueblo que generó una cultura artística y musical de alcance planetario mientras resiste carestías materiales y encrucijadas políticas extremas.",
                    "Las exportaciones de níquel representan el principal rubro de intercambio con las naciones del golfo Pérsico.",
                    "El servicio meteorológico nacional emite avisos tempranos antes de la llegada de tormentas tropicales."
                ],
                "correct": 0,
                "teaches": ["cuba-periodo-especial-economia-diaspora"]
            },
            {
                "id": f"{lc_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La música y la literatura constituyen la soberanía espiritual más duradera de Cuba.",
                "english": "Music and literature constitute Cuba's most enduring spiritual sovereignty.",
                "teaches": ["cuba-son-nueva-trova-cine"]
            },
            {
                "id": f"{lc_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta una reflexión analítica sobre el papel de la cultura cubana frente a las crisis históricas empleando una estructura condicional o concesiva.",
                        "answer": "Aun cuando las dificultades económicas del Período Especial golpearon a la sociedad, la vitalidad del son y la literatura demostró la resiliencia moral del pueblo cubano."
                    }
                ],
                "teaches": ["cuba-periodo-especial-economia-diaspora"]
            }
        ]
    })

    # Regional Capstone Story: b2-cuba.json
    story_cuba_capstone = {
        "id": "b2-cuba",
        "title": "Consolidación: El enigma cubano",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica panorámica de nivel B2 sobre la paradoja histórica, cultural y política de Cuba: síntesis de su patrimonio arquitectónico, gestas emancipadoras, vanguardia artística y resiliencia contemporánea.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Comprender a Cuba exige desprenderse de esquemas binarios reductores y adentrarse en uno de los territorios culturales y geopolíticos más paradójicos, apasionantes y debatidos de la historia moderna. Suspendida en el centro del mar de las Antillas como una 'caimán verde' de más de mil doscientos kilómetros de longitud, esta isla mayor del Caribe ha ejercido sobre el imaginario universal una fascinación magnética que desborda con creces su extensión territorial y su peso demográfico. Desde las fortificaciones renacentistas de La Habana hasta los mogotes jurásicos de Viñales, desde los versos encendidos de José Martí hasta las síncopas irresistibles del son tradicional, Cuba representa un crisol de identidades donde la grandeza estética, la tragedia política y la tenacidad cotidiana se entrelazan de modo indisoluble."
            },
            {
                "type": "narration",
                "text": "El primer pilar de esta singularidad radica en su condición histórica de frontera oceánica y encrucijada imperial. Al erigirse durante tres centurias en el puerto de escala obligado para las flotas del Imperio español que conectaban los tesoros del virreinato de Nueva España y el Perú con las cortes europeas, La Habana forjó una vocación cosmopolita prematura. Su arquitectura barroca y neoclásica de piedra caliza fosilífera, atesorada en las plazas de Armas, de la Catedral y de San Francisco, coexiste con el eclecticismo deslumbrante de sus casonas de El Vedado y el Art Déco del Edificio Bacardí, testimoniando una prosperidad urbana que supo dialogar con las corrientes estéticas más avanzadas del orbe mientras resguardaba patios umbríos donde el agua de los aljibes apaciguaba el bochorno caribeño."
            },
            {
                "type": "narration",
                "text": "Paralelamente, la campiña cubana configuró un orden productivo y cultural de hondas resonancias antropológicas en torno al tabaco y la caña de azúcar, dualidad inmortalizada magistralmente por don Fernando Ortiz en su clásico 'Contrapunteo cubano del tabaco y el azúcar'. Mientras que el ingenio azucarero colonial dependió de la mano de obra esclavizada africana sometida a una disciplina brutal en barracones cerrados para alimentar el mercado especulativo internacional, la 'vega' de tabaco fomentó el minifundio familiar, el apego amoroso a la tierra roja de Pinar del Río y el trabajo artesanal meticuloso. En ese fértil mestizaje, los cantos sagrados de los cabildos yorubas y las décimas campesinas de origen hispánico se fecundaron mutuamente, alumbrando una religiosidad sincrética —la Regla de Ocha o santería— y una sensibilidad acústica donde la rumba, el son y el guaguancó rompieron todas las barreras sociales."
            },
            {
                "type": "narration",
                "text": "En el terreno político, la isla forjó su vocación de soberanía a través de un calvario heroico de tres décadas de guerras anticoloniales contra el imperio español (1868-1898). La figura gigantesca de José Martí iluminó ese combate al concebir una república cívica e integradora, sintetizada en su memorable fórmula 'con todos y para el bien de todos'. Su ensayo 'Nuestra América' anticipó con clarividencia las asechanzas del imperialismo emergente, fundando una tradición de dignidad intelectual y resistencia antimperialista que sobreviviría a su trágica muerte en el combate de Dos Ríos y a la posterior tutela militar impuesta por Washington mediante la Enmienda Platt tras la intervención estadounidense de 1898."
            },
            {
                "type": "narration",
                "text": "Esa búsqueda incesante de autodeterminación eclesiástica y justicia social eclosionó con furia telúrica en la Revolución de 1959 encabezada por Fidel Castro y el Movimiento 26 de Julio. El desmantelamiento fulminante de la dictadura de Batista, la erradicación del latifundio mediante la reforma agraria y la colosal Campaña Nacional de Alfabetización de 1961 —que transformó a miles de jóvenes citadinos en maestros rurales que redujeron el analfabetismo al 3.9 por ciento en un solo año— consagraron la revolución ante los ojos de los pueblos descolonizados del Tercer Mundo. Sin embargo, la posterior confrontación existencial con Washington durante la Guerra Fría, simbolizada por la derrota invasora en Playa Girón y el terror nuclear de la Crisis de los Misiles de 1962, condujo a una alineación acrítica con el bloque soviético y a la instauración de un monopolio estatal rígido que limitaría las libertades cívicas y pluralistas."
            },
            {
                "type": "narration",
                "text": "El derrumbe de la Unión Soviética en 1991 desató la dura prueba del Período Especial, obligando a los cubanos a desplegar una creatividad heroica para sobrevivir a apagones interminables, escasez de alimentos y el colapso del transporte. La paulatina apertura al turismo, la despenalización del dólar y las recientes licencias para empresas privadas (mipymes) aliviaron las arcas fiscales y abrieron espacios de dinamismo comercial; no obstante, profundizaron una desigualdad monetaria lacerante que contrasta con el idealismo igualitario de antaño. En este contexto de encarecimiento de la vida, envejecimiento demográfico y asfixiante cerco económico foráneo, el país ha presenciado en los últimos años el mayor éxodo migratorio de su historia, dispersando a cientos de miles de jóvenes por los cuatro rincones del planeta."
            },
            {
                "type": "narration",
                "text": "Con todo, el enigma cubano no reside en sus fracturas materiales, sino en la milagrosa permanencia de su espíritu vital. En medio de cualquier tormenta económica, La Habana sigue vibrando al compás de sus trovadores, la melodía de Compay Segundo y Silvio Rodríguez acompaña las esperanzas íntimas de las familias, y los cineastas y poetas continúan escudriñando con lucidez las encrucijadas de su tiempo. Cuba perdura así en la conciencia universal como un testimonio indeleble de que la dignidad soberana, el amor por la palabra poética y la alegría indomable de la música son fuerzas humanas invencibles, capaces de sobrevolar las penurias del presente para seguir alimentando el sueño inagotable de una patria libre, próspera y solidaria."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué célebre metáfora antropológica empleó don Fernando Ortiz para explicar la síntesis social y productiva de Cuba?",
                        "options": [
                            "El contrapunteo del tabaco (minifundio y apego artesanal) y el azúcar (latifundio y mano de obra esclava).",
                            "La comparación entre los arrecifes de coral y las fortalezas militares de piedra caliza.",
                            "La distinción entre los ritmos de guitarra campesina y los violines de la corte virreinal europea.",
                            "El contraste entre las minas de cobre de El Cobre y las salinas costeras del mar Caribe."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 analiza la teoría de Fernando Ortiz sobre el contrapunteo entre el tabaco campesino y el azúcar esclavista como forjadores de la identidad cubana."
                    },
                    {
                        "question": "¿Cuál fue el doble balance histórico de la Revolución de 1959 analizado en la consolidación?",
                        "options": [
                            "Logró avances universales en salud, soberanía y educación (alfabetización), pero consolidó un monopolio político unipartidista de economía centralizada.",
                            "Reincorporó a la isla a la monarquía española tras indemnizar a las corporaciones de servicios públicos.",
                            "Privatizó todos los hospitales y escuelas para financiar la construcción de puertos deportivos turísticos.",
                            "Sustituyó la producción agrícola tradicional por la industria pesada siderúrgica automotriz."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 destaca las indiscutibles conquistas sociales de la revolución frente al modelo político rígido y centralizado que limitó las libertades cívicas."
                    },
                    {
                        "question": "¿En qué reside la fuerza primordial de la identidad cubana según la reflexión final del texto?",
                        "options": [
                            "En la persistencia de su soberanía espiritual a través de la música, la palabra poética, el cine y la tenacidad cívica.",
                            "En la posesión de las reservas de petróleo y gas más extensas de la cuenca del golfo de México.",
                            "En la firma de tratados de libre comercio preferencial con las potencias navales asiáticas.",
                            "En la renuncia voluntaria a la historia nacional para asimilarse culturalmente a los países anglosajones."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 7 concluye que el enigma cubano descansa sobre la alegría indomable de su música, su dignidad soberana y la resiliencia ética de su cultura."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc_con}.json", story_cuba_capstone)
    # Also write the consolidated world story reference file: content/es-latam/stories/world/b2/b2-cuba.json
    write_json(f"stories/world/b2/b2-cuba.json", story_cuba_capstone)

    write_json(f"lessons/b2/{lc_con}.json", make_consolidation_lesson(
        stem=lc_con,
        unit_num=10,
        title="Unit 10 Consolidation: Cuba",
        goal="Consolidate Cuban historical, architectural, musical, and sociopolitical themes through advanced concessive, causal, and counterfactual discourse.",
        grammar_desc="síntesis discursiva sobre Cuba: arquitectura patrimonial, ideario martiano, transformaciones revolucionarias y musicología caribeña",
        ex_ref=f"exercises/b2/{lc_con}-ex.json",
        ex_ids=[f"{lc_con}.ex01", f"{lc_con}.ex02", f"{lc_con}.ex03", f"{lc_con}.ex04", f"{lc_con}.ex05", f"{lc_con}.ex06", f"{lc_con}.ex07", f"{lc_con}.ex08"],
        goals=[
            "Synthesize Havana's architectural legacy and Viñales' karst tobacco landscape.",
            "Evaluate José Martí's anti-imperialist thought and the 1959 revolutionary transformations.",
            "Analyze the global impact of Cuban son, Nueva Trova, and ICAIC cinema.",
            "Debate contemporary economic duality and migration dynamics with advanced connectors."
        ],
        checklist_items=[
            "I can analyze Cuban colonial architecture and Viñales' karst geology with formal vocabulary.",
            "I can interpret José Martí's 'Nuestra América' and the 1895 independence movement.",
            "I can discuss the social impact and Cold War context of the 1959 Cuban Revolution.",
            "I can evaluate Cuban music (son, trovadores) and cinema with precise critical terminology.",
            "I can analyze the Special Period, monetary reforms, and contemporary migration using concessive structures."
        ],
        story_ref=f"stories/world/b2/b2-cuba.json"
    ))
    print("Completed LatAm Unit 10 (Cuba) generation!")

    # -------------------------------------------------------------------------
    # CURRICULUM UNITS WIRING (content/es-latam/curriculum/units/b2.json)
    # -------------------------------------------------------------------------
    units_file = BASE / "curriculum" / "units" / "b2.json"
    with open(units_file, "r", encoding="utf-8") as f:
        units_data = json.load(f)

    # Check if already present
    existing_stems = set()
    for u in units_data:
        for s in u.get("stems", []):
            existing_stems.add(s)

    if "b2-10-01" not in existing_stems:
        units_data.append({
            "title": "Conditionals II: Counterfactuals & Regrets",
            "stems": [
                "b2-10-01",
                "b2-10-02",
                "b2-10-03",
                "b2-10-04",
                "b2-10-05",
                "b2-10-consolidation"
            ],
            "track": "core"
        })

    if "b2-cuba-01" not in existing_stems:
        units_data.append({
            "title": "Cuba: Island of Paradox, Revolution, Cinema & Music",
            "stems": [
                "b2-cuba-01",
                "b2-cuba-02",
                "b2-cuba-03",
                "b2-cuba-04",
                "b2-cuba-05",
                "b2-cuba-consolidation"
            ],
            "track": "latam"
        })

    with open(units_file, "w", encoding="utf-8") as f:
        json.dump(units_data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated curriculum/units/b2.json with Unit 10!")

    # -------------------------------------------------------------------------
    # VERIFY WORD COUNTS FOR ALL STORIES
    # -------------------------------------------------------------------------
    all_stories = [
        ("story_core_10", story_core_10),
        ("story_cuba_01", story_cuba_01),
        ("story_cuba_02", story_cuba_02),
        ("story_cuba_03", story_cuba_03),
        ("story_cuba_04", story_cuba_04),
        ("story_cuba_05", story_cuba_05),
        ("story_cuba_capstone", story_cuba_capstone),
    ]
    print("\n--- Story Word Count Audit ---")
    for name, s in all_stories:
        wc = count_words(s)
        status = "OK (650-825)" if 650 <= wc <= 825 else f"OUT OF RANGE: {wc}"
        print(f"{name:20s}: {wc:4d} words -> {status}")
        assert 650 <= wc <= 825, f"Word count {wc} out of range for {name}!"


if __name__ == "__main__":
    run()
