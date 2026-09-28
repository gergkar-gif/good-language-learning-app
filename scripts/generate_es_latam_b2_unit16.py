"""
Generate Latin American Spanish (es-latam) B2 Unit 16:
- Core Unit 16: b2-16 (The Pluperfect Subjunctive in Independence)
  Classic Literature: Teresa de la Parra - Ifigenia
- Regional Unit 16: b2-venezuelasabana (Venezuela II: The Llanos, Tepuis & Modern Diaspora)
  Lessons:
    1. Los Llanos del Orinoco: Joropo, ganado y poesía llanera
    2. La Gran Sabana, Canaima y el mundo de los tepuyes
    3. El colapso institucional y la hiperinflación contemporánea
    4. El éxodo venezolano: La mayor migración en la historia regional
    5. La diáspora y la reinvención de la identidad venezolana en el exterior
    6. Consolidación: Paisajes inmemoriales y diáspora viva
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
        "b2-16-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "core upper-intermediate pluperfect subjunctive and retrospective discourse vocabulary"
        },
        "subjuntivo-pluscuamperfecto-formas": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "pluperfect subjunctive compound forms with hubiera and hubiese"
        },
        "subjuntivo-pluscuamperfecto-ojala": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "retrospective past wishes and regrets with ojala"
        },
        "subjuntivo-pluscuamperfecto-de-haber": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "counterfactual past structures with de haber and participle"
        },
        "subjuntivo-pluscuamperfecto-alternativas": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "retrospective alternatives and counterfactual critique in discourse"
        },
        "subjuntivo-pluscuamperfecto-literario": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "stylistic register nuances of hubiese in literary prose"
        },
        "b2-venezuelasabana-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "venezuelan llanos tepuis macroeconomic crisis and diaspora vocabulary"
        },
        "venezuela-llanos-joropo-vaqueria": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "venezuelan llanos cattle culture and joropo musical heritage"
        },
        "venezuela-canaima-tepuyes-angel": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "gran sabana tepui plateaus angel falls and pemon worldview"
        },
        "venezuela-crisis-economica-inflacion": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "contemporary macroeconomic crisis hyperinflation and institutional collapse in venezuela"
        },
        "venezuela-migracion-exodo-continental": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "contemporary venezuelan migration corridors and regional humanitarian response"
        },
        "venezuela-diaspora-identidad-global": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "venezuelan diaspora culinary diplomacy and transcontinental cultural identity"
        }
    }

    for k, v in skills_to_add.items():
        registry["skills"][k] = v

    with open(reg_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated skill-registry.json for Unit 16")

    titles_path = ROOT / "content" / "es-latam" / "indexes" / "grammar-titles.json"
    with open(titles_path, "r", encoding="utf-8") as f:
        titles = json.load(f)

    titles_to_add = {
        "subjuntivo-pluscuamperfecto-formas": "pluperfect subjunctive compound forms with hubiera and hubiese",
        "subjuntivo-pluscuamperfecto-ojala": "retrospective past wishes and regrets with ojala",
        "subjuntivo-pluscuamperfecto-de-haber": "counterfactual past structures with de haber and participle",
        "subjuntivo-pluscuamperfecto-alternativas": "retrospective alternatives and counterfactual critique in discourse",
        "subjuntivo-pluscuamperfecto-literario": "stylistic register nuances of hubiese in literary prose",
        "venezuela-llanos-joropo-vaqueria": "venezuelan llanos cattle culture and joropo musical heritage",
        "venezuela-canaima-tepuyes-angel": "gran sabana tepui plateaus angel falls and pemon worldview",
        "venezuela-crisis-economica-inflacion": "contemporary macroeconomic crisis hyperinflation and institutional collapse in venezuela",
        "venezuela-migracion-exodo-continental": "contemporary venezuelan migration corridors and regional humanitarian response",
        "venezuela-diaspora-identidad-global": "venezuelan diaspora culinary diplomacy and transcontinental cultural identity"
    }

    for k, v in titles_to_add.items():
        titles[k] = v

    with open(titles_path, "w", encoding="utf-8") as f:
        json.dump(titles, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated grammar-titles.json for Unit 16")

    # ====================================================
    # 2. CORE UNIT 16 (b2-16)
    # ====================================================
    c_unit = "b2-16"

    # --- Lesson 1: b2-16-01 ---
    l1 = f"{c_unit}-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.16.01",
        "lesson": l1,
        "title": "Morfología del pluscuamperfecto de subjuntivo",
        "theme": "Léxico de tiempos compuestos, anterioridad y contrafacticidad",
        "words": [
            {"lemma": "auxiliar", "translation": "auxiliary verb, helping verb", "pos": "noun"},
            {"lemma": "participio", "translation": "participle", "pos": "noun"},
            {"lemma": "anterioridad", "translation": "anteriority, prior occurrence", "pos": "noun"},
            {"lemma": "compuesto", "translation": "compound, composite", "pos": "adjective"},
            {"lemma": "retrospectivo", "translation": "retrospective, looking back", "pos": "adjective"},
            {"lemma": "hipotético", "translation": "hypothetical", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.16.01.subjuntivo-pluscuamperfecto-formas",
        "title": "El pretérito pluscuamperfecto de subjuntivo: estructura y alternancia",
        "sections": [
            {
                "type": "text",
                "content": "El pretérito pluscuamperfecto de subjuntivo es un tiempo compuesto que expresa una acción pasada anterior a otro momento del pasado, o bien una acción contrafáctica que no llegó a consumarse en la realidad. Se construye mediante el imperfecto de subjuntivo del verbo auxiliar **haber** (*hubiera* o *hubiese*) seguido invariablemente del **participio pasivo** del verbo principal (*cantado, vivido, resuelto*).\n\nAl igual que en las formas simples, la alternancia entre *hubiera* y *hubiese* es gramaticalmente intercambiable en cláusulas subordinadas, predominando *hubiera* en más del noventa por ciento del uso oral y escrito en toda América Latina."
            },
            {
                "type": "table",
                "title": "Paradigma del pluscuamperfecto de subjuntivo",
                "rows": [
                    ["yo hubiera / hubiese dicho", "I had said / would have said"],
                    ["tú hubieras / hubieses sabido", "you had known / would have known"],
                    ["él hubiera / hubiese venido", "he had come / would have come"],
                    ["nosotros hubiéramos / hubiésemos ido", "we had gone / would have gone"],
                    ["ustedes hubieran / hubiesen actuado", "you all had acted / would have acted"],
                    ["ellos hubieran / hubiesen ganado", "they had won / would have won"]
                ]
            },
            {
                "type": "tip",
                "content": "El participio permanece siempre invariable en masculino singular (*hubiéramos llegado*, nunca *'hubiéramos llegados'*). En la primera persona plural (*nosotros*), el auxiliar siempre lleva tilde en la vocal temática: *hubiéramos*, *hubiésemos*."
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
                    ["auxiliar", "auxiliary verb"],
                    ["participio", "verb participle"],
                    ["anterioridad", "prior occurrence"],
                    ["retrospectivo", "looking back in time"]
                ],
                "teaches": ["b2-16-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Dudábamos de que el consorcio __ el contrato antes de la fecha límite. (firmar)",
                "answer": "hubiera firmado",
                "english": "We doubted that the consortium had signed the contract before the deadline.",
                "teaches": ["subjuntivo-pluscuamperfecto-formas"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se forma morfológicamente el pretérito pluscuamperfecto de subjuntivo?",
                "options": [
                    "Con el imperfecto de subjuntivo de haber (hubiera/hubiese) más el participio invariable.",
                    "Con el presente de subjuntivo de haber más el infinitivo del verbo.",
                    "Con el condicional simple de haber más el gerundio del verbo.",
                    "Con el pretérito indefinido de ser más el adjetivo correspondiente."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-formas"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "creíamos", "que", "ellos", "hubiesen", "tomado", "esa", "decisión."],
                "solution": ["No", "creíamos", "que", "ellos", "hubiesen", "tomado", "esa", "decisión."],
                "english": "We did not believe that they had made that decision.",
                "teaches": ["subjuntivo-pluscuamperfecto-formas"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Valeria", "text": "¿Esperabas que la junta directiva hubiera aprobado el presupuesto ayer?"},
                    {"speaker": "Esteban", "text": "_____"}
                ],
                "options": [
                    "Sí, todos confiábamos en que hubieran alcanzado un acuerdo unánime tras la deliberación.",
                    "Ayer almorcé una ensalada fresca en el comedor universitario.",
                    "El presupuesto se aprueba siempre en presente de indicativo.",
                    "No conozco las oficinas centrales de la empresa."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-formas"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Nos sorprendió que el diplomático hubiera presentado su dimisión sin previo aviso.",
                "english": "We were surprised that the diplomat had submitted his resignation without prior notice.",
                "teaches": ["subjuntivo-pluscuamperfecto-formas"]
            }
        ]
    })

    # --- Lesson 2: b2-16-02 ---
    l2 = f"{c_unit}-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.16.02",
        "lesson": l2,
        "title": "Lamentos y deseos retrospectivos con ojalá",
        "words": [
            {"lemma": "lamento", "translation": "lament, regret", "pos": "noun"},
            {"lemma": "nostalgia", "translation": "nostalgia, longing", "pos": "noun"},
            {"lemma": "irreversible", "translation": "irreversible", "pos": "adjective"},
            {"lemma": "desiderativo", "translation": "desiderative, wish-expressing", "pos": "adjective"},
            {"lemma": "anhelo", "translation": "yearning, deep longing", "pos": "noun"},
            {"lemma": "remordimiento", "translation": "remorse, qualm", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.16.02.subjuntivo-pluscuamperfecto-ojala",
        "title": "Deseos retrospectivos y lamentos pasados con '¡Ojalá!'",
        "sections": [
            {
                "type": "text",
                "content": "Cuando la partícula desiderativa **¡Ojalá!** va seguida del pretérito pluscuamperfecto de subjuntivo (*¡Ojalá hubiera sabido!, ¡Ojalá hubiese estado allí!*), expresa un deseo retrospectivo referido al pasado que ya no puede cumplirse. La estructura denota invariablemente un lamento, arrepentimiento o añoranza ante un hecho consumado e irreversible.\n\nEn este uso exclamativo independiente, ambas desinencias (*hubiera* y *hubiese*) son legítimas, manteniendo *hubiera* su primacía en la conversación espontánea y *hubiese* un matiz más melancólico y literario."
            },
            {
                "type": "table",
                "title": "Lamentos retrospectivos con ¡Ojalá!",
                "rows": [
                    ["¡Ojalá hubiéramos llegado a tiempo!", "If only we had arrived on time! (regret)"],
                    ["¡Ojalá me hubieras dicho la verdad!", "If only you had told me the truth!"],
                    ["¡Ojalá no hubiese ocurrido ese conflicto!", "If only that conflict hadn't occurred!"],
                    ["¡Ojalá hubieran aceptado la propuesta!", "If only they had accepted the proposal!"],
                    ["¡Ojalá yo hubiera tenido esa oportunidad!", "If only I had had that opportunity!"],
                    ["¡Ojalá hubieses presenciado el concierto!", "If only you had witnessed the concert!"]
                ]
            },
            {
                "type": "tip",
                "content": "Contrasta cuidadosamente los dos tiempos con '¡Ojalá!':\n- *¡Ojalá venga!* (presente) = deseo realizable en el futuro.\n- *¡Ojalá viniera!* (imperfecto) = deseo irrealizable o muy improbable en el presente.\n- *¡Ojalá hubiera venido!* (pluscuamperfecto) = lamento retrospectivo por algo que no ocurrió en el pasado."
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
                    ["lamento", "regret / lamentation"],
                    ["nostalgia", "longing for the past"],
                    ["irreversible", "cannot be undone"],
                    ["remordimiento", "remorseful feeling"]
                ],
                "teaches": ["b2-16-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "¡Ojalá __ la advertencia de los especialistas antes de emprender la inversión! (escuchar)",
                "answer": "hubiéramos escuchado",
                "english": "If only we had listened to the specialists' warning before undertaking the investment!",
                "teaches": ["subjuntivo-pluscuamperfecto-ojala"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz pragmático expresa la frase '¡Ojalá hubieras asistido a la ceremonia!'?",
                "options": [
                    "Un lamento o arrepentimiento retrospectivo sobre un hecho pasado que no ocurrió.",
                    "Una invitación cordial para un evento del próximo año.",
                    "Una orden imperativa de asistencia inmediata.",
                    "Una hipótesis de futuro probable."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-ojala"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["¡Ojalá", "hubiésemos", "tenido", "mayor", "prudencia", "en", "aquel", "momento!"],
                "solution": ["¡Ojalá", "hubiésemos", "tenido", "mayor", "prudencia", "en", "aquel", "momento!"],
                "english": "If only we had had greater prudence at that moment!",
                "teaches": ["subjuntivo-pluscuamperfecto-ojala"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Beatriz", "text": "Al final cancelaron el vuelo por el temporal de nieve en la cordillera."},
                    {"speaker": "Gonzalo", "text": "_____"}
                ],
                "options": [
                    "¡Qué lástima! ¡Ojalá hubiéramos salido en el vuelo de la mañana como sugeriste!",
                    "El clima siempre es cálido en el mes de agosto.",
                    "Me gusta mucho el café con leche por las mañanas.",
                    "Los aviones vuelan a diez mil metros de altitud."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-ojala"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "¡Ojalá el gobierno hubiera implementado las reformas económicas antes del estallido de la crisis!",
                "english": "If only the government had implemented the economic reforms before the crisis erupted!",
                "teaches": ["subjuntivo-pluscuamperfecto-ojala"]
            }
        ]
    })

    # --- Lesson 3: b2-16-03 ---
    l3 = f"{c_unit}-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.16.03",
        "lesson": l3,
        "title": "Condicionales contrafácticas con infinitivo compuesto",
        "words": [
            {"lemma": "condición", "translation": "condition, prerequisite", "pos": "noun"},
            {"lemma": "infinitivo", "translation": "infinitive", "pos": "noun"},
            {"lemma": "abreviado", "translation": "abbreviated, shortened", "pos": "adjective"},
            {"lemma": "consecuencia", "translation": "consequence, outcome", "pos": "noun"},
            {"lemma": "peritaje", "translation": "expert assessment, survey", "pos": "noun"},
            {"lemma": "desenlace", "translation": "denouement, outcome", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.16.03.subjuntivo-pluscuamperfecto-de-haber",
        "title": "Estructuras condicionales contrafácticas con 'de haber + participio'",
        "sections": [
            {
                "type": "text",
                "content": "En la prosa formal, académica y periodística culta de nivel B2, la subordinada condicional contrafáctica *'si hubiera / hubiese + participio'* se abrevia elegantemente mediante la estructura preposicional **'de haber + participio'**.\n\nEsta construcción de infinitivo compuesto equivale exactamente a una prótasis condicional irreal del pasado (*De haber sabido la verdad = Si hubiera sabido la verdad*), permitiendo una mayor agilidad sintáctica y evitando la repetición del nexo *si* en textos complejos."
            },
            {
                "type": "table",
                "title": "Equivalencias sintácticas contrafácticas",
                "rows": [
                    ["De haber tenido fondos, habríamos comprado el lote.", "Had we had funds, we would have bought the lot."],
                    ["De haberse aplicado la ley, nada de esto habría ocurrido.", "Had the law been applied, none of this would have happened."],
                    ["De haber llegado diez minutos antes, no perdías el tren.", "Had you arrived ten minutes earlier, you wouldn't have missed it."],
                    ["De haber consultado a los expertos, el error era evitable.", "Had the experts been consulted, the error was avoidable."],
                    ["De habernos avisado, habríamos asistido al debate.", "Had they warned us, we would have attended the debate."],
                    ["De haber mediado el diálogo, se habrían evitado sanciones.", "Had dialogue mediated, sanctions would have been avoided."]
                ]
            },
            {
                "type": "tip",
                "content": "Los pronombres clíticos (reflexivos o de objeto) se unen obligatoriamente al final del infinitivo auxiliar *haber*: *de habérselo dicho*, *de habernos enterado*, *de haberse promulgado*. Nunca los coloques intercalados ni antes de la preposición (*'de se haber enterado'* es incorrecto)."
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
                    ["condición", "prerequisite condition"],
                    ["infinitivo", "infinitive verb form"],
                    ["peritaje", "expert survey"],
                    ["desenlace", "final outcome"]
                ],
                "teaches": ["b2-16-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "De __ mediado una intervención judicial a tiempo, el fraude se habría prevenido. (haber)",
                "answer": "haber",
                "english": "Had a judicial intervention mediated in time, the fraud would have been prevented.",
                "teaches": ["subjuntivo-pluscuamperfecto-de-haber"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿A qué oración equivale exactamente la expresión 'De haber contado con más tiempo'?",
                "options": [
                    "A 'Si hubiéramos contado con más tiempo' en modo subjuntivo contrafáctico.",
                    "A 'Cuando tengamos más tiempo' en modo subjuntivo futuro.",
                    "A 'Porque tenemos mucho tiempo disponible' en indicativo causal.",
                    "A 'Para que todos tengan tiempo libre' en cláusula final."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-de-haber"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["De", "haber", "sabido", "el", "desenlace,", "no", "habríamos", "viajado."],
                "solution": ["De", "haber", "sabido", "el", "desenlace,", "no", "habríamos", "viajado."],
                "english": "Had we known the outcome, we wouldn't have traveled.",
                "teaches": ["subjuntivo-pluscuamperfecto-de-haber"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Abogada", "text": "¿Qué dictaminó la comisión pericial sobre el colapso del puente?"},
                    {"speaker": "Ingeniero", "text": "_____"}
                ],
                "options": [
                    "Concluyeron que de haberse realizado el mantenimiento preventivo anual, la falla estructural no se habría producido.",
                    "El puente mide trescientos metros de longitud sobre el río.",
                    "El mantenimiento de puentes se realiza en días soleados.",
                    "Ayer compramos los materiales de construcción en la ferretería."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-de-haber"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "De haberse respetado el calendario electoral, la tensión política se habría disipado pacíficamente.",
                "english": "Had the electoral calendar been respected, political tension would have dissipated peacefully.",
                "teaches": ["subjuntivo-pluscuamperfecto-de-haber"]
            }
        ]
    })

    # --- Lesson 4: b2-16-04 ---
    l4 = f"{c_unit}-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.16.04",
        "lesson": l4,
        "title": "Bifurcaciones históricas y juicios retrospectivos",
        "words": [
            {"lemma": "alternativa", "translation": "alternative, option", "pos": "noun"},
            {"lemma": "omisión", "translation": "omission, failure to act", "pos": "noun"},
            {"lemma": "bifurcación", "translation": "fork, branching point", "pos": "noun"},
            {"lemma": "reproche", "translation": "reproach, censure", "pos": "noun"},
            {"lemma": "conjeturar", "translation": "to conjecture, to speculate", "pos": "verb"},
            {"lemma": "ponderar", "translation": "to weigh, to balance", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.16.04.subjuntivo-pluscuamperfecto-alternativas",
        "title": "Juicios retrospectivos y alternativas históricas en el debate crítico",
        "sections": [
            {
                "type": "text",
                "content": "En el análisis histórico, el debate político y la crítica ensayística de nivel B2, el pluscuamperfecto de subjuntivo se utiliza frecuentemente en cláusulas independientes o en correlación con condicionales para evaluar **bifurcaciones históricas y cursos de acción alternativos no adoptados**.\n\nEstructuras fijas como *'más nos hubiera valido + inf'*, *'bien pudiera haber sido'*, *'habría convenido que + subjuntivo'* o *'habríamos debido + inf'* permiten formular juicios de valor ponderados sobre errores u omisiones pasadas, manteniendo una distancia analítica respetuosa y rigurosa."
            },
            {
                "type": "table",
                "title": "Fórmulas de evaluación histórica retrospectiva",
                "rows": [
                    ["Más nos hubiera valido postergar la firma.", "It would have been far better for us to postpone the signing."],
                    ["Habríamos debido priorizar la inversión social.", "We ought to have prioritized social investment."],
                    ["Bien pudiera haber cambiado el rumbo del país.", "It very well could have changed the country's direction."],
                    ["Habría convenido que se convocara a elecciones.", "It would have been advisable for elections to be called."],
                    ["Habríamos preferido evitar la confrontación bélica.", "We would have preferred to avoid military confrontation."],
                    ["Habría sido deseable que mediaran las potencias.", "It would have been desirable for powers to mediate."]
                ]
            },
            {
                "type": "tip",
                "content": "En español formal, la fórmula *'más le hubiera valido / más nos hubiera valido'* utiliza el pluscuamperfecto de subjuntivo como sustituto enfático del condicional compuesto (*'más le habría valido'*), otorgando al reproche o reflexión un tono de sabiduría moral clásica."
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
                    ["alternativa", "course of action option"],
                    ["omisión", "failure to take action"],
                    ["bifurcación", "historical turning point"],
                    ["reproche", "critical reproach"]
                ],
                "teaches": ["b2-16-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A la luz de los acontecimientos posteriores, más nos __ valido buscar un consenso con la oposición. (haber)",
                "answer": "hubiera",
                "english": "In light of subsequent events, it would have been far better for us to seek a consensus with the opposition.",
                "teaches": ["subjuntivo-pluscuamperfecto-alternativas"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función discursiva cumple la estructura 'Habríamos debido prever la crisis bancaria'?",
                "options": [
                    "Formular un juicio crítico retrospectivo sobre una responsabilidad u omisión en el pasado.",
                    "Predecir un evento financiero que ocurrirá en el próximo trimestre.",
                    "Prohibir que los bancos otorguen préstamos en moneda extranjera.",
                    "Describir una rutina bancaria cotidiana sin emitir opiniones."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-alternativas"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Más", "les", "hubiera", "valido", "acatar", "el", "fallo", "del", "tribunal."],
                "solution": ["Más", "les", "hubiera", "valido", "acatar", "el", "fallo", "del", "tribunal."],
                "english": "It would have been far better for them to comply with the court's ruling.",
                "teaches": ["subjuntivo-pluscuamperfecto-alternativas"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Analista", "text": "¿Cómo juzga la historiografía la decisión del presidente de no nacionalizar los ferrocarriles en 1930?"},
                    {"speaker": "Profesor", "text": "_____"}
                ],
                "options": [
                    "Los historiadores coinciden en que habría convenido acelerar la regulación estatal para evitar la fuga de capitales.",
                    "Los trenes circulan sobre rieles de acero laminado en caliente.",
                    "El café venezolano era muy apreciado en las capitales de Europa.",
                    "En 1930 no existían carreteras pavimentadas en América del Sur."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-alternativas"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Bien pudiera haberse evitado la fractura institucional mediante un pacto de gobernabilidad democrática.",
                "english": "The institutional fracture could very well have been avoided through a democratic governance pact.",
                "teaches": ["subjuntivo-pluscuamperfecto-alternativas"]
            }
        ]
    })

    # --- Lesson 5: b2-16-05 ---
    l5 = f"{c_unit}-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.16.05",
        "lesson": l5,
        "title": "Estilo literario y alternancia de desinencias",
        "words": [
            {"lemma": "matiz", "translation": "nuance, shade of meaning", "pos": "noun"},
            {"lemma": "cadencia", "translation": "cadence, rhythm", "pos": "noun"},
            {"lemma": "arcaísmo", "translation": "archaism", "pos": "noun"},
            {"lemma": "melodioso", "translation": "melodious, lyrical", "pos": "adjective"},
            {"lemma": "ponderado", "translation": "thoughtful, balanced", "pos": "adjective"},
            {"lemma": "prosodia", "translation": "prosody, rhythmic phrasing", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.16.05.subjuntivo-pluscuamperfecto-literario",
        "title": "Matices estilísticos de 'hubiese' en la prosa literaria y ensayística",
        "sections": [
            {
                "type": "text",
                "content": "Si bien en la lengua oral y el periodismo latinoamericano contemporáneo la forma auxiliar en **-ra** (*hubiera cantado*) es abrumadoramente dominante, en la prosa literaria de autor, el ensayo filosófico y la crónica de alta cultura la variante en **-se** (*hubiese cantado*) conserva un prestigio estilístico singular.\n\nLos grandes escritores hispanoamericanos recurren deliberadamente a *hubiese* por tres motivos retóricos fundamentales:\n1. **Eufonía y prosodia**: evitar la repetición cacofónica de sonidos en *-ra* en frases sucesivas (*'si hubiera querido que saliera'* -> *'si hubiese querido que saliera'*).\n2. **Tono introspectivo y memorialístico**: conferir a la voz narrativa una cadencia íntima, sosegada y poética.\n3. **Distancia ficcional**: enmarcar la acción en un tiempo clásico o legendario, diferenciándolo de la inmediatez del reportaje periodístico."
            },
            {
                "type": "table",
                "title": "Ejemplos de refinamiento estilístico literario",
                "rows": [
                    ["como si el tiempo se hubiese detenido", "as if time had stopped (lyrical cadence)"],
                    ["de haber sabido que ella hubiese partido", "had he known that she had departed (euphonic balance)"],
                    ["aunque nada hubiese cambiado en la estancia", "even though nothing had changed on the ranch"],
                    ["quienquiera que hubiese pisado ese umbral", "whoever had stepped across that threshold"],
                    ["sin que nadie hubiese advertido su presencia", "without anyone having noticed his presence"],
                    ["cual si una sombra hubiese cubierto el cielo", "as if a shadow had covered the sky (literary)"]
                ]
            },
            {
                "type": "tip",
                "content": "Al redactar tus propios textos literarios o ensayos académicos en español B2, busca la alternancia deliberada: utiliza *hubiese* cuando una cláusula cercana ya contenga una terminación en *-ra*, mejorando la cadencia rítmica de tu prosa."
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
                    ["matiz", "fine nuance"],
                    ["cadencia", "rhythmic cadence"],
                    ["arcaísmo", "archaic turn of phrase"],
                    ["prosodia", "rhythmic prosody"]
                ],
                "teaches": ["b2-16-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la novela de Teresa de la Parra, la protagonista sentía como si su juventud se __ marchitado entre convencionalismos. (haber)",
                "answer": "hubiese",
                "english": "In Teresa de la Parra's novel, the protagonist felt as if her youth had withered among conventionalisms.",
                "teaches": ["subjuntivo-pluscuamperfecto-literario"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué un escritor culto elige a menudo 'hubiese' en lugar de 'hubiera' en un pasaje narrativo?",
                "options": [
                    "Para evitar la cacofonía y dotar al relato de una cadencia prosódica lírica y sosegada.",
                    "Porque la forma hubiera está terminantemente prohibida en la literatura.",
                    "Porque hubiese se refiere exclusivamente a acontecimientos del siglo diecinueve.",
                    "Para indicar que el personaje principal es extranjero."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-literario"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Era", "como", "si", "la", "memoria", "se", "hubiese", "disuelto", "en", "la", "niebla."],
                "solution": ["Era", "como", "si", "la", "memoria", "se", "hubiese", "disuelto", "en", "la", "niebla."],
                "english": "It was as if memory had dissolved in the fog.",
                "teaches": ["subjuntivo-pluscuamperfecto-literario"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítica", "text": "¿Qué efecto estético logra Teresa de la Parra al emplear la forma 'hubiese' en las cartas de Ifigenia?"},
                    {"speaker": "Profesor", "text": "_____"}
                ],
                "options": [
                    "Modula la voz epistolar de María Eugenia con una intimidad melancólica y una elegancia irónica que cuestiona la hipocresía social.",
                    "Comete una serie de faltas ortográficas propias de la juventud inexperta.",
                    "Demuestra que no conocía las reglas de la gramática castellana contemporánea.",
                    "Obliga al lector a consultar un diccionario de términos jurídicos."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-literario"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aunque nadie se hubiese atrevido a desafiar la tradición familiar, su espíritu rebelde jamás claudicó.",
                "english": "Even though no one had dared to challenge family tradition, her rebellious spirit never surrendered.",
                "teaches": ["subjuntivo-pluscuamperfecto-literario"]
            }
        ]
    })

    # --- Lesson 6: b2-16-consolidation ---
    l6_con = f"{c_unit}-consolidation"
    write_json(f"exercises/b2/{l6_con}-ex.json", {
        "lesson": l6_con,
        "exercises": [
            {
                "id": f"{l6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["auxiliar", "auxiliary verb"],
                    ["lamento", "retrospective regret"],
                    ["peritaje", "expert survey"],
                    ["cadencia", "rhythmic phrasing"]
                ],
                "teaches": ["b2-16-vocab"]
            },
            {
                "id": f"{l6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "¡Ojalá la protagonista de la novela __ encontrado una sociedad más abierta a la emancipación de la mujer! (haber)",
                "answer": "hubiera",
                "english": "If only the novel's protagonist had found a society more open to women's emancipation!",
                "teaches": ["subjuntivo-pluscuamperfecto-ojala"]
            },
            {
                "id": f"{l6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura condicional culta abrevia 'si hubiera recibido la herencia paterna'?",
                "options": [
                    "De haber recibido la herencia paterna.",
                    "Por recibir la herencia paterna.",
                    "Habiendo de recibir la herencia paterna.",
                    "Con tal de que recibiera la herencia paterna."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-de-haber"]
            },
            {
                "id": f"{l6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A la sociedad caraqueña de entonces más le __ valido escuchar la voz lúcida de sus jóvenes escritoras. (haber)",
                "answer": "hubiera",
                "english": "It would have been far better for the Caracas society of that time to listen to the lucid voice of its young women writers.",
                "teaches": ["subjuntivo-pluscuamperfecto-alternativas"]
            },
            {
                "id": f"{l6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la función estilística de alternar hubiera y hubiese en la prosa narrativa?",
                "options": [
                    "Evitar repeticiones cacofónicas y matizar el ritmo melódico e introspectivo de las oraciones.",
                    "Indicar que el narrador no sabe cuál de las dos formas es correcta.",
                    "Señalar obligatoriamente un cambio de tiempo verbal entre presente y futuro.",
                    "Ninguna; ambas formas deben usarse de manera idéntica sin variación."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-literario"]
            },
            {
                "id": f"{l6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["De", "haber", "tenido", "autonomía", "financiera,", "María", "habría", "sido", "libre."],
                "solution": ["De", "haber", "tenido", "autonomía", "financiera,", "María", "habría", "sido", "libre."],
                "english": "Had she had financial autonomy, María would have been free.",
                "teaches": ["subjuntivo-pluscuamperfecto-de-haber"]
            },
            {
                "id": f"{l6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Ifigenia simbolizó el doloroso dilema entre la libertad individual y el sacrificio social.",
                "english": "Iphigenia symbolized the painful dilemma between individual freedom and social sacrifice.",
                "teaches": ["subjuntivo-pluscuamperfecto-formas"]
            },
            {
                "id": f"{l6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué representa la obra Ifigenia de Teresa de la Parra en las letras latinoamericanas?",
                "options": [
                    "Una de las cumbres fundacionales de la narrativa feminista y psicológica moderna de principios del siglo veinte.",
                    "Un tratado de botánica tropical sobre las flores del valle de Caracas.",
                    "Una crónica militar sobre las guerras de independencia de Bolívar.",
                    "Un manual pedagógico para la enseñanza de idiomas extranjeros."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-pluscuamperfecto-literario"]
            }
        ]
    })

    # Classic Story for Core Unit 16: Teresa de la Parra - Ifigenia (~700 words, strictly 650-825 words)
    story_core_16 = {
        "id": "b2-16",
        "title": "Ifigenia: El diario íntimo y el sacrificio de una señorita caraqueña",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de nivel B2 de la célebre novela de Teresa de la Parra: el regreso de la joven e ilustrada María Eugenia Alonso a la conservadora Caracas de los años veinte tras educarse en París, el despojo de su herencia paterna, la asfixia moral impuesta por su abuela y su tía, y su trágica capitulación matrimonial como una moderna Ifigenia sacrificada en el altar de las apariencias.",
        "characters": [
            "María Eugenia Alonso",
            "Abuelita",
            "Tía Clara",
            "Gabriel Quiroga",
            "César Leal"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al desembarcar en el muelle de La Guaira tras una prolongada y luminosa estancia juvenil en París, María Eugenia Alonso contempló el imponente cerro El Ávila con una mezcla de fascinación estética e íntimo desasosiego. Educada con plena libertad en las academias francesas, acostumbrada a debatir sobre literatura universal, a vestir con la elegancia sobria de los bulevares europeos y a cultivar un intelecto agudo e independiente, la joven de dieciocho años regresaba a su Venezuela natal obligada por el repentino fallecimiento de su padre. En su equipaje traía baúles atestados de novelas de Anatole France, vestidos ligeros de seda y un nutrido fajo de cuartillas en blanco donde proyectaba volcar las confidencias más íntimas de su espíritu: el diario epistolar que enviaría a su inseparable amiga Cristina Iturbe."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el choque con la realidad caraqueña fue brutal y despiadado. Al instalarse en la sombría casona señorial de su abuela materna, una anciana de devoción monacal y modales intransigentes, María Eugenia descubrió que la prometida fortuna familiar se había esfumado por completo, devorada por la codicia inescrupulosa de su tío Eduardo, quien fungía como administrador legal de los bienes. Despojada de cualquier dote o patrimonio propio, la muchacha quedó reducida a la condición humillante de pariente pobre y dependiente, sometida a la vigilancia asfixiante de su tía Clara, una solterona resignada que consideraba que la mayor virtud de una mujer decente residía en el silencio sumiso, el bordado de manteles de iglesia y la renuncia absoluta a cualquier brillo intelectual."
            },
            {
                "type": "narration",
                "text": "En aquella atmósfera conventual donde los espejos parecían vigilar el pudor y las celosías de madera filtraban las miradas de los vecinos curiosos, los hábitos cosmopolitas de María Eugenia desataron el escándalo social. Su costumbre de asomarse sola al balcón para contemplar el crepúsculo sobre la plaza, su afición por leer a solas en el patio umbroso y su negativa a arrodillarse durante horas interminables en rezos mecánicos fueron juzgados por su familia como pecados de orgullo y descaro. '¡Ojalá te hubieses quedado en un convento de clausura en Europa antes de traer estas ideas subversivas que deshonran a nuestro apellido!', sentenciaba la severa Abuelita con la voz trémula de quien defiende los últimos cimientos de un orden colonial sagrado."
            },
            {
                "type": "narration",
                "text": "En medio de aquella asfixia cotidiana, un destello fugaz de esperanza iluminó el corazón de la protagonista con la aparición de Gabriel Quiroga, un joven diplomático e intelectual de mirada apasionada con quien compartía lecturas afines y el anhelo de una existencia basada en la complicidad espiritual. Entre las páginas de su diario, María Eugenia confesaba con ternura conmovedora que junto a Gabriel sentía que su inteligencia no era un defecto vergonzoso, sino un don fecundo. No obstante, aquel amor estaba condenado de antemano por las férreas convenciones de clase: Gabriel carecía de fortuna material y la familia de María Eugenia no admitiría jamás un enlace nupcial que no garantizara la solvencia económica y la restauración del linaje familiar."
            },
            {
                "type": "narration",
                "text": "Fue entonces cuando entró en escena don César Leal, un próspero y autoritario hacendado y alto funcionario gubernamental que personificaba todo lo que María Eugenia repudiaba íntimamente: la prepotencia masculina, el conservadurismo cerril y la convicción machista de que la esposa era una propiedad subordinada que debía acatar sin murmuraciones los mandatos maritales. Presionada sin tregua por el chantaje emocional de su tía, los lamentos de su abuela agonizante y el terror insoportable a verse condenada a la miseria y a la soltería marginada, María Eugenia comprendió con lúcida amargura que su destino ya no le pertenecía."
            },
            {
                "type": "narration",
                "text": "En una memorable noche de insomnio frente a su diario, la joven trazó la analogía mitológica que otorgaría título a la obra cumbre de Teresa de la Parra: al igual que la doncella griega Ifigenia fue inmolada por su propio padre Agamenón en el altar de los dioses para que los vientos soplaran favorables hacia Troya, ella sería sacrificada por su familia en el altar de las conveniencias burguesas de Caracas. Ningún dios bajaría del cielo para rescatarla de los brazos de César Leal: su inteligencia, su sensibilidad estética y sus ansias de libertad debían ser sepultadas bajo el velo blanco de una boda sin amor."
            },
            {
                "type": "narration",
                "text": "Al cerrar su diario con la firma definitiva de María Eugenia Alonso, Teresa de la Parra no solo legó a la literatura hispanoamericana una de sus novelas más audaces, irónicas y psicológicamente refinadas, sino que erigió un monumento imperecedero de protesta cívica. Ifigenia desnudó ante el continente las cárceles invisibles que el patriarcado y la hipocresía social construían en torno a la mujer latinoamericana, recordando a las generaciones venideras que no habrá civilización verdadera mientras la dignidad, el talento y el destino libre de una mujer sigan siendo inmolados en nombre de las apariencias."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál era la situación económica en la que quedó María Eugenia Alonso al regresar a Caracas tras la muerte de su padre?",
                        "options": [
                            "Quedó despojada de su herencia y dote debido al mal manejo y codicia de su tío Eduardo, viviendo como pariente dependiente.",
                            "Heredó una de las mayores empresas petroleras del país y gran fortuna.",
                            "Recibió un castillo señorial en los valles del Tuy sin deudas.",
                            "Fue contratada como embajadora de Venezuela en la capital francesa."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que su fortuna se esfumó por la codicia de su tío Eduardo, dejándola sin dinero y dependiente de su abuela."
                    },
                    {
                        "question": "¿Por qué el amor entre María Eugenia y el joven Gabriel Quiroga resultó inviable dentro de su círculo familiar?",
                        "options": [
                            "Porque Gabriel carecía de fortuna material y la familia exigía un matrimonio ventajoso que restaurara la posición económica del apellido.",
                            "Porque Gabriel fue desterrado del país de forma inmediata.",
                            "Debido a que María Eugenia no compartía gustos intelectuales con él.",
                            "Porque la ley prohibía el matrimonio entre diplomáticos e intelectuales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 expone que la familia rechazaba a Gabriel por carecer de solvencia económica, exigiendo un enlace con alguien acaudalado."
                    },
                    {
                        "question": "¿Qué simboliza el mito clásico de Ifigenia en la decisión final que toma María Eugenia Alonso?",
                        "options": [
                            "El sacrificio voluntario y trágico de su libertad e intelecto en el altar del matrimonio por conveniencia y las apariencias burguesas.",
                            "Su decisión heroica de huir a la selva amazónica para vivir como exploradora.",
                            "La inauguración de una escuela náutica en el puerto de La Guaira.",
                            "Su coronación como reina de las fiestas de carnaval de Caracas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los párrafos 6 y 7 detallan que María Eugenia se compara con Ifigenia porque es sacrificada por las conveniencias familiares al casarse sin amor con César Leal."
                    }
                ]
            }
        }
    }

    # ====================================================
    # 3. REGIONAL UNIT 16 (b2-venezuelasabana)
    # ====================================================
    r_unit = "b2-venezuelasabana"

    # --- Lesson 1: b2-venezuelasabana-01 ---
    r1 = f"{r_unit}-01"
    write_json(f"vocabulary/b2/{r1}-voc.json", {
        "id": "vocab.b2.venezuelasabana.01",
        "lesson": r1,
        "title": "Los Llanos, faenas ganaderas y música de joropo",
        "theme": "Léxico de sabanas inundables, cultura pastoril y organología llanera",
        "words": [
            {"lemma": "sabana", "translation": "savanna, open grassland", "pos": "noun"},
            {"lemma": "vaquería", "translation": "cattle roundup, herding cattle", "pos": "noun"},
            {"lemma": "joropo", "translation": "joropo (traditional dance and musical genre)", "pos": "noun"},
            {"lemma": "estero", "translation": "wetland, seasonal marsh", "pos": "noun"},
            {"lemma": "coplero", "translation": "llanero verse improviser, singer", "pos": "noun"},
            {"lemma": "baquiano", "translation": "expert local wilderness guide", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r1}-a-gr.json", {
        "id": "grammar.b2.venezuelasabana.01.venezuela-llanos-joropo-vaqueria",
        "title": "Los Llanos del Orinoco: Joropo, ganado y poesía llanera",
        "sections": [
            {
                "type": "text",
                "content": "Desplegándose en una inmensa cuenca sedimentaria que abarca casi la tercera parte del territorio nacional, los Llanos del Orinoco (en los estados de Apure, Barinas, Portuguesa, Cojedes y Guárico) configuran el paisaje identitario más visceral de Venezuela. Esta planicie sin fin vive al ritmo de dos estaciones extremas: el 'invierno' (temporada de lluvias torrenciales que transforma millones de hectáreas en un mar de agua dulce poblado por garzas, chigüires y caimanes) y el 'verano' (rigurosa sequía que calcina los pastos y fuerza las grandes travesías de ganado).\n\nEn esta geografía épica se forjó la figura del llanero, jinete legendario célebre por su destreza en el lazo y por los **cantos de vaquería** —declarados por la UNESCO como Patrimonio Cultural Inmaterial de la Humanidad en 2017—, cantos a capela con los que el arriero sosiega a las reses durante las faenas de ordeño y pastoreo."
            },
            {
                "type": "table",
                "title": "Elementos de la identidad y organología llanera",
                "rows": [
                    ["los cantos de vaquería", "work songs sung to calm cattle during roundups and milking"],
                    ["el arpa llanera", "the diatonic nylon-strung harp leading the joropo ensemble"],
                    ["el cuatro venezolano", "the four-stringed small acoustic guitar providing harmonic pulse"],
                    ["las maracas de capacho", "dried seed shakers creating complex polyrhythmic patterns"],
                    ["el contrapunteo", "poetic improvisational duel between two llanero singers"],
                    ["el chigüire / capibara", "the world's largest rodent thriving in seasonal wetlands"]
                ]
            },
            {
                "type": "tip",
                "content": "El joropo llanero no es solo una danza; es una filosofía vital que combina la elegancia del zapateo criollo con la poesía oral improvisada del *contrapunteo*, donde dos copleros rivalizan durante horas en versos octosílabos rimados demostrando agudeza e ingenio sin pausa."
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
                    ["sabana", "open tropical grassland"],
                    ["vaquería", "cattle roundup chores"],
                    ["joropo", "traditional folk music and dance"],
                    ["baquiano", "expert regional pathfinder"]
                ],
                "teaches": ["b2-venezuelasabana-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los cantos de __ fueron declarados Patrimonio Cultural Inmaterial por la UNESCO en 2017. (vaquería)",
                "answer": "vaquería",
                "english": "Cattle herding songs were declared Intangible Cultural Heritage by UNESCO in 2017.",
                "teaches": ["venezuela-llanos-joropo-vaqueria"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué instrumentos componen tradicionalmente el ensamble musical del joropo llanero?",
                "options": [
                    "El arpa llanera, el cuatro venezolano y las maracas de capacho.",
                    "El acordeón, la caja vallenata y la guacharaca.",
                    "El piano de cola y el clarinete de madera.",
                    "La flauta traversa y el violonchelo europeo."
                ],
                "correct": 0,
                "teaches": ["venezuela-llanos-joropo-vaqueria"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "arpa", "llanera", "guía", "el", "zapateo", "del", "joropo."],
                "solution": ["El", "arpa", "llanera", "guía", "el", "zapateo", "del", "joropo."],
                "english": "The llanero harp guides the zapateo of the joropo.",
                "teaches": ["venezuela-llanos-joropo-vaqueria"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Viajero", "text": "¿Por qué el llanero canta mientras ordeña o arrea el ganado a través de los ríos?"},
                    {"speaker": "Baquiano", "text": "_____"}
                ],
                "options": [
                    "Los cantos de vaquería modulan tonos que tranquilizan a los animales y evitan estampidas durante las travesías.",
                    "Porque la ley prohíbe que el ganado camine en completo silencio.",
                    "Para ahuyentar a los barcos de turistas que navegan por el río.",
                    "Porque los copleros practican para concursos de ópera en Europa."
                ],
                "correct": 0,
                "teaches": ["venezuela-llanos-joropo-vaqueria"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "En los esteros de Apure, el chigüire y la corocora roja conviven en un equilibrio ecológico milenario.",
                "english": "In the wetlands of Apure, the capybara and the scarlet ibis coexist in a millenary ecological balance.",
                "teaches": ["venezuela-llanos-joropo-vaqueria"]
            }
        ]
    })

    # --- Lesson 2: b2-venezuelasabana-02 ---
    r2 = f"{r_unit}-02"
    write_json(f"vocabulary/b2/{r2}-voc.json", {
        "id": "vocab.b2.venezuelasabana.02",
        "lesson": r2,
        "title": "La Gran Sabana, los tepuyes y Canaima",
        "words": [
            {"lemma": "tepuy", "translation": "tepui, flat-topped table mountain", "pos": "noun"},
            {"lemma": "meseta", "translation": "plateau, tableland", "pos": "noun"},
            {"lemma": "catarata", "translation": "waterfall, cataract", "pos": "noun"},
            {"lemma": "precámbrico", "translation": "Precambrian", "pos": "adjective"},
            {"lemma": "endemismo", "translation": "endemism, native uniqueness", "pos": "noun"},
            {"lemma": "abismo", "translation": "abyss, chasm", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r2}-a-gr.json", {
        "id": "grammar.b2.venezuelasabana.02.venezuela-canaima-tepuyes-angel",
        "title": "La Gran Sabana, Canaima y el reino de los tepuyes",
        "sections": [
            {
                "type": "text",
                "content": "Al sureste del río Orinoco, en el Escudo Guayanés, se extiende la geología más antigua del planeta: el Parque Nacional Canaima y la Gran Sabana. En este territorio sagrado emergen de la densa selva húmeda los **tepuyes**, gigantescas mesetas tabulares de arenisca precámbrica con paredes verticales de cientos de metros de caída libre que se formaron hace más de mil setecientos millones de años.\n\nPara el pueblo indígena originario **Pemón**, los tepuyes son moradas de los espíritus ancestrales (*Mawari*). En el Auyán-tepui ('la montaña del diablo') se precipita el **Kerepakupai Vená** (conocido mundialmente como el Salto Ángel), la caída de agua ininterrumpida más alta del mundo con novecientos setenta y nueve metros de altitud, cuyo torrente se pulveriza en una bruma etérea antes de tocar el dosel selvático."
            },
            {
                "type": "table",
                "title": "Tepuyes e hitos geográficos de Canaima",
                "rows": [
                    ["el Roraima", "the famous triple-border tepui inspiring Conan Doyle's The Lost World"],
                    ["el Auyán-tepui", "the massive heart-shaped plateau cradling the world's tallest waterfall"],
                    ["el Kerepakupai Vená", "Angel Falls: 979 meters of free-falling water into the jungle"],
                    ["las plantas carnívoras", "endemic Drosera and Heliamphora adapted to nutrient-poor sandstone summits"],
                    ["el pueblo Pemón", "indigenous custodians of Canaima and the Gran Sabana"],
                    ["el Escudo Guayanés", "one of Earth's oldest geological cratons holding unique biodiversity"]
                ]
            },
            {
                "type": "tip",
                "content": "Debido a millones de años de aislamiento geográfico en las cimas de los tepuyes, estos ecosistemas operan como 'islas en el cielo': más de la tercera parte de las especies vegetales que habitan sus cumbres son endémicas y no existen en ningún otro rincón del planeta."
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
                    ["tepuy", "sandstone table mountain"],
                    ["catarata", "waterfall cataract"],
                    ["endemismo", "biological uniqueness to a locale"],
                    ["abismo", "vertical precipice abyss"]
                ],
                "teaches": ["b2-venezuelasabana-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Kerepakupai Vená o Salto Ángel cae desde el Auyán-tepui con una altura de casi mil metros sin tocar __. (pared)",
                "answer": "paredes",
                "english": "Kerepakupai Vená or Angel Falls drops from Auyán-tepui with a height of nearly a thousand meters without touching walls.",
                "teaches": ["venezuela-canaima-tepuyes-angel"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué las cumbres de los tepuyes albergan un porcentaje tan elevado de especies endémicas?",
                "options": [
                    "Debido a millones de años de aislamiento biológico en las alturas sobre mesetas precámbricas.",
                    "Porque fueron plantadas por exploradores botánicos británicos en el siglo veinte.",
                    "Debido al uso intensivo de fertilizantes químicos en las mesetas.",
                    "Porque la vegetación se renovó por completo tras una glaciación reciente."
                ],
                "correct": 0,
                "teaches": ["venezuela-canaima-tepuyes-angel"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "tepuyes", "constituyen", "la", "geología", "más", "antigua", "del", "planeta."],
                "solution": ["Los", "tepuyes", "constituyen", "la", "geología", "más", "antigua", "del", "planeta."],
                "english": "Tepuis constitute the oldest geology on the planet.",
                "teaches": ["venezuela-canaima-tepuyes-angel"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Bióloga", "text": "¿Cómo se adaptaron las plantas de las cimas de los tepuyes a la escasez de nutrientes?"},
                    {"speaker": "Guía Pemón", "text": "_____"}
                ],
                "options": [
                    "Desarrollaron mecanismos carnívoros como las heliamphoras, que capturan insectos para obtener nitrógeno mineral.",
                    "Absorben los nutrientes del petróleo que brota de las rocas areniscas.",
                    "Reciben abonos orgánicos traídos en helicópteros científicos todos los meses.",
                    "No necesitan nutrientes porque se alimentan exclusivamente de luz lunar."
                ],
                "correct": 0,
                "teaches": ["venezuela-canaima-tepuyes-angel"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Para el pueblo Pemón, el tepuy es un santuario sagrado donde reposan las fuerzas creadoras de la tierra.",
                "english": "For the Pemón people, the tepui is a sacred sanctuary where the earth's creative forces rest.",
                "teaches": ["venezuela-canaima-tepuyes-angel"]
            }
        ]
    })

    # --- Lesson 3: b2-venezuelasabana-03 ---
    r3 = f"{r_unit}-03"
    write_json(f"vocabulary/b2/{r3}-voc.json", {
        "id": "vocab.b2.venezuelasabana.03",
        "lesson": r3,
        "title": "La crisis macroeconómica e hiperinflación",
        "words": [
            {"lemma": "hiperinflación", "translation": "hyperinflation", "pos": "noun"},
            {"lemma": "colapso", "translation": "collapse, systemic breakdown", "pos": "noun"},
            {"lemma": "desabastecimiento", "translation": "shortage, scarcity of goods", "pos": "noun"},
            {"lemma": "precariedad", "translation": "precariousness, fragility", "pos": "noun"},
            {"lemma": "resiliencia", "translation": "resilience", "pos": "noun"},
            {"lemma": "dolarización", "translation": "dollarization", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r3}-a-gr.json", {
        "id": "grammar.b2.venezuelasabana.03.venezuela-crisis-economica-inflacion",
        "title": "La crisis macroeconómica, la hiperinflación y el colapso del modelo rentista",
        "sections": [
            {
                "type": "text",
                "content": "En la segunda década del siglo XXI, Venezuela se precipitó en la crisis económica, social e institucional más severa de su historia republicana moderna. La confluencia letal de un colapso en la producción petrolera nacional (que cayó de más de tres millones de barriles diarios a menos de setecientos mil por falta de mantenimiento e inversión técnica), un control de cambios distorsionador, la emisión descontrolada de dinero inorgánico y la polarización política desembocó entre 2017 y 2021 en una hiperinflación devastadora que pulverizó los salarios y el valor del bolívar.\n\nLa contracción de más del setenta y cinco por ciento del Producto Interno Bruto generó graves episodios de desabastecimiento de alimentos y medicinas, obligando a la sociedad a implementar estrategias de supervivencia basadas en la dolarización transaccional de facto, las remesas familiares y la solidaridad comunitaria."
            },
            {
                "type": "table",
                "title": "Conceptos de la crisis económica venezolana",
                "rows": [
                    ["la hiperinflación", "exponential price rises reaching thousands of percent annually"],
                    ["el colapso productivo", "75% drop in GDP between 2014 and 2020"],
                    ["la dolarización de facto", "spontaneous adoption of US dollars for everyday commercial transactions"],
                    ["las remesas familiares", "transfers sent home by millions of diaspora relatives abroad"],
                    ["el control de cambios", "protracted currency controls distorting imports and pricing"],
                    ["la emergencia humanitaria compleja", "UN designation describing systemic healthcare and nutritional strain"]
                ]
            },
            {
                "type": "tip",
                "content": "Para superar la hiperinflación, el país vivió un proceso espontáneo de dolarización informal: los precios en comercios y servicios comenzaron a fijarse en dólares estadounidenses, reduciendo la volatilidad aunque profundizando las brechas de desigualdad entre quienes reciben divisas del exterior y quienes dependen de salarios públicos locales."
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
                    ["hiperinflación", "extreme price increases"],
                    ["desabastecimiento", "shortage of goods"],
                    ["precariedad", "fragile living conditions"],
                    ["resiliencia", "capacity to endure and recover"]
                ],
                "teaches": ["b2-venezuelasabana-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Para protegerse frente a la pérdida de poder adquisitivo, el comercio adoptó una __ transaccional de facto. (dolarización)",
                "answer": "dolarización",
                "english": "To protect against the loss of purchasing power, commerce adopted a de facto transactional dollarization.",
                "teaches": ["venezuela-crisis-economica-inflacion"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuáles fueron los factores determinantes de la profunda hiperinflación vivida en Venezuela a partir de 2017?",
                "options": [
                    "El desplome de la producción petrolera, controles de cambio distorsionados y la emisión monetaria inorgánica.",
                    "Un terremoto que destruyó los puertos comerciales del mar Caribe.",
                    "El aumento de las exportaciones de café y cacao tradicional.",
                    "La adopción del euro como moneda nacional oficial."
                ],
                "correct": 0,
                "teaches": ["venezuela-crisis-economica-inflacion"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Las", "remesas", "familiares", "sostienen", "el", "consumo", "de", "millones", "de", "hogares."],
                "solution": ["Las", "remesas", "familiares", "sostienen", "el", "consumo", "de", "millones", "de", "hogares."],
                "english": "Family remittances support the consumption of millions of households.",
                "teaches": ["venezuela-crisis-economica-inflacion"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Cómo lograron las familias venezolanas sobrellevar los peores años de la crisis económica?"},
                    {"speaker": "Socióloga", "text": "_____"}
                ],
                "options": [
                    "Mediante redes de resiliencia comunitaria, el trabajo independiente y el apoyo vital de las remesas enviadas por la diáspora.",
                    "Renunciando a utilizar teléfonos móviles e internet en todo el territorio.",
                    "Comprando acciones en la bolsa de valores de Londres.",
                    "Mudándose todas las familias a vivir en los campos petroleros abandonados."
                ],
                "correct": 0,
                "teaches": ["venezuela-crisis-economica-inflacion"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La reconstrucción productiva demanda seguridad jurídica, diversificación económica y consensos institucionales.",
                "english": "Productive reconstruction demands legal certainty, economic diversification, and institutional consensus.",
                "teaches": ["venezuela-crisis-economica-inflacion"]
            }
        ]
    })

    # --- Lesson 4: b2-venezuelasabana-04 ---
    r4 = f"{r_unit}-04"
    write_json(f"vocabulary/b2/{r4}-voc.json", {
        "id": "vocab.b2.venezuelasabana.04",
        "lesson": r4,
        "title": "El éxodo venezolano y la migración continental",
        "words": [
            {"lemma": "éxodo", "translation": "exodus, mass migration", "pos": "noun"},
            {"lemma": "caminante", "translation": "walker, on-foot migrant", "pos": "noun"},
            {"lemma": "páramo", "translation": "paramo, cold alpine moor", "pos": "noun"},
            {"lemma": "regularización", "translation": "regularization, legal integration", "pos": "noun"},
            {"lemma": "acogida", "translation": "welcome, reception of refugees", "pos": "noun"},
            {"lemma": "travesía", "translation": "crossing, journey through hardship", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r4}-a-gr.json", {
        "id": "grammar.b2.venezuelasabana.04.venezuela-migracion-exodo-continental",
        "title": "El éxodo venezolano: La mayor migración en la historia de América Latina",
        "sections": [
            {
                "type": "text",
                "content": "Como consecuencia de la prolongada crisis socioeconómica y política, más de siete millones de venezolanos abandonaron su país en el transcurso de una década, configurando el mayor fenómeno de desplazamiento humano en la historia contemporánea del hemisferio occidental, superado a escala global únicamente por los conflictos de Siria y Ucrania.\n\nLa odisea migratoria tuvo su rostro más conmovedor en los 'caminantes', familias enteras que cruzaron a pie miles de kilómetros por las carreteras suramericanas, desafiando el frío mortal del páramo de Berlín en Colombia, las alturas de los Andes ecuatorianos y los desiertos del norte de Perú y Chile, o arriesgando la vida a través de la densa y peligrosa selva del Darién en la frontera entre Colombia y Panamá."
            },
            {
                "type": "table",
                "title": "Rutas y países de acogida de la migración",
                "rows": [
                    ["Colombia", "main host nation sheltering nearly three million Venezuelan migrants"],
                    ["el Estatuto Temporal (ETPV)", "pioneering Colombian 10-year regularization framework"],
                    ["los caminantes del páramo", "migrants walking across high freezing mountain passes toward the south"],
                    ["el Tapón del Darién", "perilous tropical jungle route toward Central and North America"],
                    ["Perú, Chile y Ecuador", "key Andean destinations integrating skilled and labor workforce"],
                    ["la hermandad continental", "civil society and international humanitarian response"]
                ]
            },
            {
                "type": "tip",
                "content": "Colombia implementó en 2021 el *Estatuto Temporal de Protección para Migrantes Venezolanos* (ETPV), un modelo elogiado internacionalmente por el ACNUR que otorgó estatus legal regular por diez años a casi dos millones de personas, permitiéndoles acceder al sistema de salud, educación formal y empleo digno."
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
                    ["éxodo", "mass human migration"],
                    ["caminante", "on-foot migrant"],
                    ["páramo", "freezing alpine moorland"],
                    ["acogida", "humanitarian reception"]
                ],
                "teaches": ["b2-venezuelasabana-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Colombia otorgó un Estatuto Temporal de Protección para facilitar la __ legal de casi dos millones de migrantes. (regularización)",
                "answer": "regularización",
                "english": "Colombia granted a Temporary Protection Statute to facilitate the legal regularization of nearly two million migrants.",
                "teaches": ["venezuela-migracion-exodo-continental"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la magnitud estimada del éxodo venezolano en la última década según organismos de la ONU?",
                "options": [
                    "Más de siete millones de personas en todo el mundo, la mayor migración en la historia regional.",
                    "Menos de cincuenta mil personas en provincias limítrofes.",
                    "Únicamente unas pocas familias adineradas en Europa.",
                    "No se cuenta con ningún registro sobre desplazamientos de población."
                ],
                "correct": 0,
                "teaches": ["venezuela-migracion-exodo-continental"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "caminantes", "desafiaron", "el", "frío", "extremo", "de", "los", "páramos."],
                "solution": ["Los", "caminantes", "desafiaron", "el", "frío", "extremo", "de", "los", "páramos."],
                "english": "The walkers defied the extreme cold of the alpine passes.",
                "teaches": ["venezuela-migracion-exodo-continental"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Cooperante", "text": "¿Por qué el Estatuto Temporal otorgado por Colombia fue considerado un hito humanitario?"},
                    {"speaker": "Delegada ACNUR", "text": "_____"}
                ],
                "options": [
                    "Porque garantizó diez años de regularidad migratoria, acceso formal a la salud, educación y permisos de trabajo legales.",
                    "Porque obligó a todos los migrantes a permanecer en campamentos cerrados en la frontera.",
                    "Porque exigió el pago de elevadas multas para ingresar al territorio nacional.",
                    "Porque canceló todos los vuelos comerciales entre ambos países."
                ],
                "correct": 0,
                "teaches": ["venezuela-migracion-exodo-continental"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La solidaridad entre los pueblos latinoamericanos fue fundamental para amortiguar el impacto del éxodo.",
                "english": "Solidarity among Latin American peoples was fundamental to cushioning the impact of the exodus.",
                "teaches": ["venezuela-migracion-exodo-continental"]
            }
        ]
    })

    # --- Lesson 5: b2-venezuelasabana-05 ---
    r5 = f"{r_unit}-05"
    write_json(f"vocabulary/b2/{r5}-voc.json", {
        "id": "vocab.b2.venezuelasabana.05",
        "lesson": r5,
        "title": "La diáspora y la identidad cultural transcontinental",
        "words": [
            {"lemma": "diáspora", "translation": "diaspora, scattered population", "pos": "noun"},
            {"lemma": "arepa", "translation": "arepa (traditional corn cake)", "pos": "noun"},
            {"lemma": "arraigo", "translation": "deep root, emotional attachment", "pos": "noun"},
            {"lemma": "transcultural", "translation": "transcultural", "pos": "adjective"},
            {"lemma": "fraternidad", "translation": "fraternity, brotherhood", "pos": "noun"},
            {"lemma": "añoranza", "translation": "yearning, homesickness", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{r5}-a-gr.json", {
        "id": "grammar.b2.venezuelasabana.05.venezuela-diaspora-identidad-global",
        "title": "La diáspora y la reinvención de la identidad venezolana en el exterior",
        "sections": [
            {
                "type": "text",
                "content": "Lejos de diluirse en el olvido, la identidad venezolana ha experimentado en los últimos años una asombrosa reinvención transcontinental a través de su diáspora. Desde Bogotá, Lima, Santiago de Chile y Buenos Aires hasta Madrid, Miami y Montreal, millones de profesionales, médicos, ingenieros, artistas y cocineros venezolanos se han integrado activamente en las sociedades de acogida, enriqueciendo su vida económica y cultural.\n\nEl icono universal de este reencuentro ha sido la **arepa** —torta circular de harina de maíz precocida asada a la plancha y rellena con queso blanco, caraotas negras, carne mechada ('la pelúa') o ensalada de pollo y aguacate ('reina pepiada')—, que se ha transformado en un fenómeno gastronómico global. Junto a la comida, la música del cuatro, la gaita zuliana navideña y las redes comunitarias confirman que Venezuela ya no es solo una delimitación geográfica, sino una patria viva que late en cada rincón del mundo donde un compatriota trabaja con dignidad y esperanza."
            },
            {
                "type": "table",
                "title": "Iconos culturales de la venezolanidad global",
                "rows": [
                    ["la reina pepiada", "iconic arepa filled with shredded chicken, avocado, and lime"],
                    ["el pabellón criollo", "national dish of shredded beef, black beans, white rice, and plantains"],
                    ["el cuatro y la gaita", "traditional four-string guitar and Zulia festive December rhythms"],
                    ["el tequeño", "cheese-stuffed fried pastry dough staple of celebrations everywhere"],
                    ["la resiliencia diaspórica", "integration through professional excellence and civic contribution"],
                    ["Venezuela transcontinental", "the living idea of identity persisting across borders and oceans"]
                ]
            },
            {
                "type": "tip",
                "content": "La arepa venezolana es una herencia milenaria de los pueblos cumanagoto y caribe: su nombre proviene del vocablo indígena *erepa*, que significaba 'maíz'. Hoy las areperas son embajadas vivas de sabor y fraternidad en las principales capitales de los cinco continentes."
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
                    ["diáspora", "population dispersed abroad"],
                    ["arepa", "grilled cornflour cake"],
                    ["arraigo", "deep emotional attachment"],
                    ["añoranza", "homesick longing"]
                ],
                "teaches": ["b2-venezuelasabana-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La arepa con pollo desmechado y aguacate se conoce popularmente como reina __. (pepiada)",
                "answer": "pepiada",
                "english": "The arepa with shredded chicken and avocado is popularly known as reina pepiada.",
                "teaches": ["venezuela-diaspora-identidad-global"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué ha demostrado la experiencia de la diáspora venezolana en las naciones de acogida?",
                "options": [
                    "Que la identidad se reinventa mediante el trabajo digno, la excelencia profesional y la diplomacia gastronómica y cultural.",
                    "Que los migrantes renuncian de inmediato a todas sus costumbres culinarias.",
                    "Que la cocina tradicional desaparece cuando una persona cruza una frontera.",
                    "Que la música del cuatro solo puede interpretarse en territorio nacional."
                ],
                "correct": 0,
                "teaches": ["venezuela-diaspora-identidad-global"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "arepa", "se", "convirtió", "en", "un", "icono", "gastronómico", "mundial."],
                "solution": ["La", "arepa", "se", "convirtió", "en", "un", "icono", "gastronómico", "mundial."],
                "english": "The arepa became a global gastronomic icon.",
                "teaches": ["venezuela-diaspora-identidad-global"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Cliente", "text": "He visto areperas en Madrid, Santiago y Buenos Aires. ¿A qué se debe su enorme popularidad?"},
                    {"speaker": "Cocinero", "text": "_____"}
                ],
                "options": [
                    "La arepa es versátil, deliciosa y lleva consigo el calor hogareño y la memoria viva de nuestra tierra a cualquier parte del mundo.",
                    "Es una comida obligatoria impuesta por los tratados comerciales internacionales.",
                    "Porque en las ciudades modernas no existe ningún otro tipo de restaurante.",
                    "Porque la masa de maíz se fabrica exclusivamente en laboratorios farmacéuticos."
                ],
                "correct": 0,
                "teaches": ["venezuela-diaspora-identidad-global"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La venezolanidad florece hoy en miles de comunidades solidarias que construyen puentes de fraternidad continental.",
                "english": "Venezuelan identity flourishes today in thousands of solidarity communities building bridges of continental fraternity.",
                "teaches": ["venezuela-diaspora-identidad-global"]
            }
        ]
    })

    # --- Lesson 6: b2-venezuelasabana-consolidation ---
    rc_con = f"{r_unit}-consolidation"
    write_json(f"exercises/b2/{rc_con}-ex.json", {
        "lesson": rc_con,
        "exercises": [
            {
                "id": f"{rc_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["sabana", "vast tropical plain"],
                    ["tepuy", "sandstone table mountain"],
                    ["éxodo", "mass migration movement"],
                    ["diáspora", "community living abroad"]
                ],
                "teaches": ["b2-venezuelasabana-vocab"]
            },
            {
                "id": f"{rc_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Salto Ángel se precipita desde el Auyán-__ en el corazón del Parque Nacional Canaima. (tepui)",
                "answer": "tepuy",
                "english": "Angel Falls plunges from Auyán-tepui in the heart of Canaima National Park.",
                "teaches": ["venezuela-canaima-tepuyes-angel"]
            },
            {
                "id": f"{rc_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué reconocimiento internacional otorgó la UNESCO a los cantos de vaquería llaneros en 2017?",
                "options": [
                    "Los declaró Patrimonio Cultural Inmaterial de la Humanidad por su valor poético y etnográfico.",
                    "Los catalogó como himno militar obligatorio para las fuerzas armadas.",
                    "Los prohibió por considerar que perturbaban la tranquilidad del ganado.",
                    "Los declaró monumento histórico de piedra caliza."
                ],
                "correct": 0,
                "teaches": ["venezuela-llanos-joropo-vaqueria"]
            },
            {
                "id": f"{rc_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Estatuto Temporal implementado por Colombia facilitó la __ de casi dos millones de migrantes. (regularización)",
                "answer": "regularización",
                "english": "The Temporary Statute implemented by Colombia facilitated the regularization of nearly two million migrants.",
                "teaches": ["venezuela-migracion-exodo-continental"]
            },
            {
                "id": f"{rc_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿De qué manera el plato tradicional de la arepa se convirtió en un símbolo de la diáspora?",
                "options": [
                    "Transformó la comida criolla en una embajada de encuentro, nostalgia y dignificación laboral en decenas de países.",
                    "Sirvió únicamente como alimento racionado en campos de refugiados.",
                    "Fue declarada moneda de curso legal en los bancos comerciales.",
                    "Sustituyó a la harina de trigo en todas las panaderías de Europa."
                ],
                "correct": 0,
                "teaches": ["venezuela-diaspora-identidad-global"]
            },
            {
                "id": f"{rc_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "Llanos", "y", "los", "tepuyes", "custodian", "la", "memoria", "ancestral."],
                "solution": ["Los", "Llanos", "y", "los", "tepuyes", "custodian", "la", "memoria", "ancestral."],
                "english": "The Llanos and the tepuis guard ancestral memory.",
                "teaches": ["venezuela-canaima-tepuyes-angel"]
            },
            {
                "id": f"{rc_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La historia contemporánea de Venezuela une la inmensidad de sus paisajes con el coraje de su pueblo.",
                "english": "The contemporary history of Venezuela unites the immensity of its landscapes with the courage of its people.",
                "teaches": ["venezuela-diaspora-identidad-global"]
            },
            {
                "id": f"{rc_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué lección fundamental se desprende del estudio de las dos unidades de Venezuela en B2?",
                "options": [
                    "Que más allá de las vicisitudes del petroestado y las crisis, Venezuela resplandece en su arte, su naturaleza grandiosa y la dignidad inquebrantable de su gente.",
                    "Que los países exportadores de materias primas nunca logran crear literatura o música propia.",
                    "Que las regiones geográficas de un país no guardan relación con la historia de sus habitantes.",
                    "Que la migración debilita irrevocablemente los lazos de identidad cultural de un pueblo."
                ],
                "correct": 0,
                "teaches": ["venezuela-diaspora-identidad-global"]
            }
        ]
    })

    # ----------------------------------------------------
    # Regional Stories (5 lesson stories + 1 capstone = 6)
    # Strictly between 650 and 825 words (~700 words target)
    # ----------------------------------------------------

    story_ven2_01 = {
        "id": "b2-venezuelasabana-01",
        "title": "Los Llanos del Orinoco: El canto del arriero y la sabana infinita",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica etnográfica y musical de nivel B2 sobre las llanuras venezolanas: el ciclo implacable del invierno fluvial y el verano ardiente en Apure y Barinas, la vida ruda del hato ganadero, la maestría del lazo, los cantos de vaquería declarados Patrimonio de la Humanidad por la UNESCO y la magia polirrítmica del joropo con arpa llanera.",
        "characters": [
            "Don Dámaso Hurtado",
            "Yajaira",
            "Maestro arpista Eloy"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Cuando el viajero contempla por primera vez las inmensidades de los Llanos del Orinoco en los estados venezolanos de Apure, Barinas o Guárico, una sensación de sobrecogimiento y pequeñez se apodera de sus sentidos. La llanura no tiene principio ni fin aparente: el horizonte se dilata en una línea recta y perfecta donde la tierra y el cielo se funden bajo el vuelo cadencioso de miles de garzas blancas, corocoras escarlatas y bandadas de patos reales. Esta gigantesca cuenca sedimentaria de pastizales y bosques de galería, que abarca casi un tercio de la superficie de Venezuela, vive sometida a un péndulo climático implacable dividido en dos estaciones extremas: el 'invierno', seis meses de lluvias copiosas que desbordan los ríos Apure, Arauca y Capanaparo convirtiendo la sabana en un inmenso océano de agua dulce, y el 'verano', rigurosa sequía que calcina los pastos bajo un sol implacable de cuarenta grados a la sombra."
            },
            {
                "type": "narration",
                "text": "En esta geografía anfibia y bravía se templó el carácter del llanero, un jinete de indomable resistencia física cuya existencia es inseparable del caballo criollo y de las faenas ganaderas en los tradicionales 'hatos'. Don Dámaso Hurtado, curtido arriero de setenta años de edad que ha cruzado a nado ríos infestados de caimanes y rayas de río arreando miles de novillos salvajes, ensilla su potro al amanecer junto a su nieta Yajaira. 'En el llano nadie manda si no sabe domar primero su propio miedo; la sabana exige respeto, paciencia infinita para esperar que las aguas bajen y un ojo certero para descifrar en la brisa el rastro de la fiera', reflexiona Don Dámaso mientras ajusta la cincha de cuero crudo."
            },
            {
                "type": "narration",
                "text": "El alma espiritual y estética de esta cultura ganadera late con una belleza conmovedora en los **cantos de vaquería**, proclamados en 2017 por la UNESCO como Patrimonio Cultural Inmaterial de la Humanidad. Se trata de melodías vocales entonadas a capela, lentas y quejumbrosas, improvisadas por los arrieros en versos octosílabos para apaciguar al ganado vacuno durante las extenuantes travesías o al momento del ordeño en los corrales. Cada vaca responde al canto personalizado de su nombre ('Mariposa', 'Nube blanca', 'Lucerito'), y al escuchar la modulación aguda y melódica del peón, el rebaño se sosiega, camina en orden sin descarriarse y permite que la leche fluya mansa hacia el cántaro de aluminio."
            },
            {
                "type": "narration",
                "text": "Al caer la tarde, cuando los animales descansan en las majadas y el olor a carne asada en vara sobre brasas de leña de espino perfuma la noche estrellada, el hato se transforma en un templo de celebración festiva. En el caney principal resuenan los primeros acordes vertiginosos del arpa llanera, magistralmente pulsada por el maestro Eloy. Sus dedos arrancan de las treinta y dos cuerdas de nailon cascadas de bordoneos graves y melodías centelleantes que imitan el galope del potro sobre el barrizal. A su lado, el cuatro venezolano marca el compás sincopado con rasgueos enérgicos y las maracas de semillas secas de capacho dibujan un bordado rítmico de virtuosa complejidad."
            },
            {
                "type": "narration",
                "text": "Es el reino del joropo, donde los bailadores demuestran su prestancia en el zapateo y el escobillao, desafiándose con giros elegantes sin rozar el suelo con las rodillas. En el clímax de la velada estalla el 'contrapunteo': dos copleros se sitúan frente a frente bajo la luz de las lámparas de carburo para batirse en un duelo de versos rimados e ingenio fulminante. Ninguno puede titubear ni repetir una rima consonante ya empleada; cada estrofa debe responder al argumento del adversario abordando temas que van desde el desamor y la política hasta la cosmogonía y la muerte, demostrando una prodigiosa agilidad poética heredada de los antiguos romances andaluces y recreada en la vastedad americana."
            },
            {
                "type": "narration",
                "text": "Los Llanos del Orinoco confirman así que la venezolanidad no es solo modernidad urbana o rentismo petrolero de autopista, sino una raíz telúrica profunda que respira en la sabiduría del jinete, en la comunión respetuosa con la fauna de los esteros y en el cántico sagrado que calma a la bestia bajo la lluvia torrencial. En la voz solitaria del arriero que canta a la luna en medio de la sabana infinita resplandece la verdad más pura de esta tierra: un pacto indisoluble entre el hombre y el horizonte libre que ningún vendaval histórico ha logrado quebrar jamás ante los ojos del mundo."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué distinción otorgó la UNESCO a los cantos de vaquería llaneros venezolanos en el año 2017?",
                        "options": [
                            "Los declaró Patrimonio Cultural Inmaterial de la Humanidad por su singularidad etnográfica y su función armonizadora con el ganado.",
                            "Los catalogó como himno oficial para ceremonias diplomáticas internacionales.",
                            "Los declaró reserva natural biológica de carácter forestal.",
                            "Los reconoció como el baile más rápido de las pistas comerciales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 explica que la UNESCO declaró los cantos de vaquería como Patrimonio Cultural Inmaterial de la Humanidad en 2017."
                    },
                    {
                        "question": "¿En qué consiste el duelo poético llanero conocido popularmente como 'contrapunteo'?",
                        "options": [
                            "En una competencia de versos rimados e improvisados donde dos copleros rivalizan en agudeza sobre el compás del joropo.",
                            "En una carrera de caballos salvajes a lo largo de los esteros secos.",
                            "En un concurso gastronómico para preparar el mejor asado de ternera.",
                            "En una batalla física cuerpo a cuerpo entre peones del hato."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 detalla el contrapunteo: un desafío de poesía oral improvisada en décimas u octosílabos donde dos cantadores miden su ingenio sin titubear."
                    },
                    {
                        "question": "¿Cuáles son las dos estaciones climáticas extremas que rigen la vida biológica y humana en los Llanos?",
                        "options": [
                            "El invierno de lluvias torrenciales que inunda la llanura y el verano de intensa sequía y calor sofocante.",
                            "La primavera templada y el otoño con nevadas en las colinas.",
                            "Una estación única y uniforme sin ninguna alteración térmica.",
                            "Temporadas de monzones asiáticos con granizo perpetuo."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 describe el ciclo del invierno con grandes inundaciones que crean mares de agua dulce y el verano de implacable sequía."
                    }
                ]
            }
        }
    }

    story_ven2_02 = {
        "id": "b2-venezuelasabana-02",
        "title": "Canaima y los tepuyes: Las islas del tiempo y la caída del ángel",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica geográfica y antropológica de nivel B2 sobre el Parque Nacional Canaima y la Gran Sabana: la geología precámbrica del Escudo Guayanés, las majestuosas mesetas tabulares o tepuyes (Roraima, Auyán-tepui), la cosmovisión sagrada del pueblo Pemón y el espectáculo sublime del Kerepakupai Vená (Salto Ángel), la catarata más alta de la Tierra.",
        "characters": [
            "Juvencio Pemón",
            "Doctora Arreaza",
            "Kerepakupai"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al cruzar la franja colosal del río Orinoco hacia el confín suroriental de Venezuela, el paisaje terrestre abandona cualquier escala humana convencional para adentrarse en la memoria geológica primordial del planeta Tierra. En el corazón del Parque Nacional Canaima, una reserva natural de más de treinta mil kilómetros cuadrados inscrita en 1994 como Patrimonio Natural de la Humanidad por la UNESCO, se yergue el Escudo Guayanés, uno de los cratones rocosos más antiguos y estables de la corteza continental. Emergiendo de la canopia selvática virgen como fortalezas ciclópeas esculpidas por el agua y el viento a lo largo de mil setecientos millones de años, los **tepuyes** desafían el firmamento con paredes verticales de arenisca rosada que se desploman en abismos de más de mil metros de caída libre."
            },
            {
                "type": "narration",
                "text": "Para el pueblo originario **Pemón**, habitantes ancestrales de la Gran Sabana divididos en las comunidades arekuna, kamarakoto y taurepán, los tepuyes no son meros accidentes orográficos de interés turístico, sino moradas sagradas de divinidades tutelares y espíritus primigenios conocidos como los *Mawari*. Ningún indígena tradicional osaba escalar sus cumbres escarpadas sin un propósito ceremonial reverente, temiendo perturbar el equilibrio cósmico de las aguas y los vientos. El sabedor y guía comunitario Juvencio Pemón, navegando en una curiara tradicional de madera por las aguas rojizas del río Carrao cargadas de taninos vegetales, explica a la doctora Arreaza, geóloga e investigadora: 'En nuestra lengua, 'tepuy' significa la casa de los dioses de piedra; ellos estaban aquí antes de que el primer árbol naciera y permanecerán vigilantes cuando el último ser humano haya partido'."
            },
            {
                "type": "narration",
                "text": "La cumbre más imponente y misteriosa de este conjunto es el Auyán-tepui, una colosal meseta con forma de corazón invertido que abarca una superficie de casi setecientos kilómetros cuadrados. De su garganta más profunda, el mítico Cañón del Diablo, se precipita al vacío el prodigio hidrológico supremo del planeta: el **Kerepakupai Vená** ('el salto del lugar más profundo'), bautizado en la cartografía occidental como el Salto Ángel en homenaje al aviador estadounidense Jimmy Angel, quien en 1937 aterrizó de emergencia sobre su cima fangosa. Con novecientos setenta y nueve metros de caída total y ochocientos siete metros de caída libre ininterrumpida, el torrente de agua se desprende con tal ímpetu que, antes de alcanzar las copas de los árboles en el fondo del cañón, se pulveriza en una nube etérea de millones de gotas irisadas que empapan la selva circundante en un rocío perpetuo."
            },
            {
                "type": "narration",
                "text": "Debido a su aislamiento físico absoluto durante decenas de millones de años, las cumbres de los tepuyes constituyen auténticas 'islas biológicas en el cielo'. Sobre sus mesetas de roca desnuda calcinadas por la radiación ultravioleta y lavadas por lluvias torrenciales diarias que barren cualquier capa de suelo orgánico fértil, la vida vegetal desarrolló adaptaciones evolutivas asombrosas que inspiraron la célebre novela *El mundo perdido* de Arthur Conan Doyle. Entre charcas de agua cristalina y laberintos de piedra esculpida crecen las *Heliamphora*, fascinantes plantas carnívoras con hojas tubulares que atrapan insectos para nutrirse de minerales, junto a orquídeas microscópicas, ranas negras que no saben nadar y cientos de especies botánicas endémicas que no existen en ningún otro punto del globo terráqueo."
            },
            {
                "type": "narration",
                "text": "Hacia el este, en la frontera triple donde convergen las soberanías de Venezuela, Brasil y la Guayana Esequiba, se levanta el majestuoso Roraima-tepui con su perfil de proa de navío petrificado a dos mil ochocientos metros sobre el nivel del mar. La doctora Arreaza, contemplando el mar de nubes blancas que envuelve la base del farallón al amanecer, reflexiona sobre la fragilidad de este paraíso: 'Canaima es el laboratorio viviente donde se preserva la infancia del planeta; protegerlo de la minería ilegal y del turismo depredador es una obligación moral insustituible ante toda la humanidad'."
            },
            {
                "type": "narration",
                "text": "Frente a las aguas rumorosas de la laguna de Canaima, donde las cascadas del Hacha, Golondrina y Ucaima braman en una sinfonía acuática perfecta, la Gran Sabana reafirma su condición de santuario intemporal. En el arcoíris permanente que corona la bruma del Kerepakupai Vená resplandece la mayor verdad de esta geografía mágica: que la belleza suprema de la naturaleza no necesita la justificación de la utilidad mercantil, sino que existe por sí misma como un cántico sagrado de pureza, misterio y eternidad que trasciende las fronteras del tiempo."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál es la altura total de la caída de agua del Kerepakupai Vená (Salto Ángel)?",
                        "options": [
                            "Novecientos setenta y nueve metros, con ochocientos siete metros de caída libre ininterrumpida.",
                            "Doscientos metros sobre un cauce escalonado de piedra.",
                            "Cincuenta metros en una garganta estrecha de montaña.",
                            "Cinco mil metros en medio de un glaciar andino."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 especifica que el Salto Ángel tiene una altura total de 979 metros, con una caída libre sin interrupciones de 807 metros."
                    },
                    {
                        "question": "¿Cómo se adaptaron las plantas carnívoras del género Heliamphora a las cimas rocosas de los tepuyes?",
                        "options": [
                            "Desarrollaron hojas tubulares para atrapar insectos y obtener los nutrientes minerales que la roca lavada no provee.",
                            "Desarrollaron raíces gigantescas que perforan kilómetros de profundidad en la tierra.",
                            "Perdieron la clorofila y se transformaron en hongos subterráneos.",
                            "Sobreviven alimentándose de la savia de los árboles madereros circundantes."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 explica que las Heliamphora crecen en charcas rocosas y capturan insectos para compensar la falta de suelo orgánico fértil."
                    },
                    {
                        "question": "¿Qué significado tienen los tepuyes dentro de la cosmovisión del pueblo originario Pemón?",
                        "options": [
                            "Son moradas sagradas de divinidades tutelares y espíritus ancestrales primigenios llamados Mawari.",
                            "Eran fortalezas militares construidas durante las guerras coloniales del siglo dieciséis.",
                            "Constituyen minas de sal marina para la conservación de alimentos.",
                            "Son cementerios modernos para las autoridades distritales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 expone que para los Pemón los tepuyes son sitios sagrados donde habitan los espíritus Mawari y las fuerzas tutelares de la naturaleza."
                    }
                ]
            }
        }
    }

    story_ven2_03 = {
        "id": "b2-venezuelasabana-03",
        "title": "La fractura del petroestado: Crónica de la hiperinflación y el tejido de la resiliencia",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociopolítica y económica de nivel B2 sobre la crisis contemporánea de Venezuela: el desplome de la producción petrolera, los controles de cambio disfuncionales, el torbellino hiperinflacionario de 2017 a 2021, la pérdida del poder adquisitivo salarial, la dolarización de facto y las redes comunitarias de resiliencia civil.",
        "characters": [
            "Profesora Carmen Elena",
            "Manuel",
            "Doctor Quintero"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Durante más de siete décadas de bonanza hidrocarburífera, la sociedad venezolana se acostumbró a concebir su destino bajo la premisa de una abundancia material casi garantizada por el Estado rentista. Sin embargo, a partir de 2014, una convergencia catastrófica de factores macroeconómicos y políticos desató el colapso productivo más fulminante que haya padecido un país en tiempos de paz en la historia moderna de América Latina. La caída abrupta de las cotizaciones mundiales del crudo coincidió trágicamente con el desmantelamiento técnico de la empresa estatal PDVSA: afectada por la falta de inversión preventiva, la desprofesionalización gerencial y severos escándalos de corrupción, la extracción petrolera nacional se desplomó de tres millones de barriles diarios a menos de setecientos mil, amputando de raíz el noventa y cinco por ciento de las divisas que alimentaban el presupuesto público nacional."
            },
            {
                "type": "narration",
                "text": "Para cubrir el gigantesco déficit fiscal resultante, las autoridades gubernamentales recurrieron a la emisión masiva de dinero inorgánico sin respaldo productivo, mientras mantenían un férreo y disfuncional control de cambio de divisas que distorsionaba por completo la fijación de precios en el mercado interno. El desenlace inevitable fue un torbellino hiperinflacionario devastador que entre 2017 y 2021 alcanzó tasas anuales superiores al cien mil por ciento según estimaciones de organismos internacionales. El papel moneda del bolívar perdió todo valor transaccional práctico: los billetes eran desechados en las aceras o utilizados por artesanos callejeros para tejer carteras y sombreros decorativos, mientras el salario mínimo mensual de los trabajadores públicos y pensionados se evaporaba hasta equivaler a escasos dos o tres dólares mensuales."
            },
            {
                "type": "narration",
                "text": "La profesora Carmen Elena, veterana docente de secundaria en la ciudad de Valencia, recuerda con lágrimas aquellos años de angustia colectiva marcados por el desabastecimiento crónico de alimentos básicos como harina de maíz, leche y medicamentos esenciales: 'Íbamos a los supermercados con fajos de billetes que pesaban más que la comida que lográbamos comprar tras hacer colas interminables de doce horas bajo el sol. En los hospitales públicos, los médicos tenían que pedir a los familiares de los enfermos que trajeran gasas, suero y bombillos eléctricos para poder realizar una intervención quirúrgica de urgencia'."
            },
            {
                "type": "narration",
                "text": "El doctor Quintero, médico internista en el Hospital Central, relata cómo la precariedad forzó a la comunidad científica y sanitaria a reinventar mecanismos de emergencia para salvar vidas infantiles frente a la reaparición de enfermedades tropicales como la malaria y la difteria, que habían sido erradicadas décadas atrás. Fue en medio de ese abismo donde la sociedad venezolana descubrió una reserva moral insospechada: la resiliencia ciudadana. Vecinos de sectores populares organizaron 'ollas comunitarias' para alimentar a los niños más desnutridos, iglesias y organizaciones no gubernamentales distribuyeron insumos médicos puerta a puerta y las familias apelaron al trueque de bienes básicos para sobrellevar la adversidad más amarga."
            },
            {
                "type": "narration",
                "text": "Hacia 2019, asfixiado por el colapso del sistema de pagos y las sanciones financieras internacionales, el gobierno flexibilizó de facto los controles económicos, permitiendo la libre circulación del dólar estadounidense en el comercio minorista. En cuestión de meses, Venezuela vivió una 'dolarización transaccional' espontánea: desde los quioscos de periódicos hasta los grandes almacenes fijaron sus precios en divisas, poniendo fin a la escasez de productos en los anaqueles pero consolidando una dolorosa brecha social entre quienes contaban con acceso a dólares —generalmente a través de remesas familiares enviadas desde el extranjero— y la gran masa de trabajadores que continuaba percibiendo salarios testimoniales en moneda local."
            },
            {
                "type": "narration",
                "text": "Manuel, un joven emprendedor de veinticinco años que repara equipos electrónicos en un pequeño local del este de Caracas junto a Carmen Elena, sintetiza las lecciones de esta traumática travesía: 'Nuestra generación aprendió por las malas que un Estado no puede regalar lo que no produce y que el rentismo fácil fue una trampa histórica. Hoy nos levantamos cada mañana con la certeza de que el futuro de Venezuela dependerá exclusivamente de nuestro esfuerzo productivo, de la educación real y de la reconstrucción democrática de nuestras instituciones'. En esa tenaz dignidad de quienes resistieron y continuaron trabajando contra toda adversidad late la esperanza inquebrantable de una nación que se niega a rendirse ante su propio dolor."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuáles fueron los factores determinantes que precipitaron el colapso económico venezolano a partir de 2014?",
                        "options": [
                            "La drástica caída de los precios mundiales del crudo combinada con el desplome productivo de PDVSA, el control de cambios y la emisión monetaria inorgánica.",
                            "Una invasión militar extranjera que destruyó las refinerías petroleras.",
                            "Un tratado comercial que obligaba a regalar todo el petróleo a los países vecinos.",
                            "El abandono masivo de las ciudades para dedicarse a la caza silvestre."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 detalla la confluencia de la caída de cotizaciones, la desinversión en PDVSA, los controles cambiarios y el déficit fiscal cubierto con dinero inorgánico."
                    },
                    {
                        "question": "¿Qué fenómeno comercial espontáneo surgió hacia 2019 para mitigar los efectos de la hiperinflación en el país?",
                        "options": [
                            "Una dolarización transaccional de facto donde comercios y servicios adoptaron el dólar para fijar precios y realizar pagos.",
                            "La sustitución de todo el comercio por el trueque exclusivo de lingotes de oro.",
                            "La prohibición total del uso de cualquier moneda física o electrónica.",
                            "La adopción obligatoria de la libra esterlina británica."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 describe cómo la sociedad adoptó de facto el dólar estadounidense para transacciones cotidianas, frenando la escasez en los anaqueles."
                    },
                    {
                        "question": "¿De qué manera respondieron las comunidades y la sociedad civil venezolana frente a la escasez en los momentos más duros?",
                        "options": [
                            "Organizando redes de resiliencia comunitaria como ollas populares solidarias, donaciones de insumos médicos y trueques de auxilio mutuo.",
                            "Destruyendo todos los hospitales y centros educativos de los barrios.",
                            "Negándose a colaborar entre vecinos bajo cualquier circunstancia.",
                            "Clausurando todas las iglesias y organizaciones benéficas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 resalta la resiliencia civil: ollas comunitarias para niños, apoyo médico de ONG y solidaridad comunitaria para proteger a los más vulnerables."
                    }
                ]
            }
        }
    }

    story_ven2_04 = {
        "id": "b2-venezuelasabana-04",
        "title": "Los caminos del éxodo: De los páramos andinos al corazón del continente",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica humanitaria de nivel B2 sobre la mayor crisis migratoria de la historia latinoamericana: la partida de más de siete millones de venezolanos, la dolorosa odisea de los 'caminantes' cruzando el páramo de Berlín en Colombia hacia el sur andino y la selva del Darién hacia el norte, la solidaridad de los pueblos receptores y el pionero Estatuto Temporal de Protección en Colombia.",
        "characters": [
            "Yorman Colmenares",
            "Mireya",
            "Socorrista Amador"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En las terminales de autobuses de San Cristóbal y sobre el puente internacional Simón Bolívar, que une a la ciudad venezolana de San Antonio del Táchira con la colombiana Cúcuta, el siglo veintiuno fue testigo de una de las mareas humanas más desgarradoras y masivas de la historia contemporánea. Empujados por el hambre, la falta de medicamentos esenciales y la asfixia económica, más de siete millones setecientos mil venezolanos abandonaron su tierra natal a lo largo de una década según registros oficiales del Alto Comisionado de las Naciones Unidas para los Refugiados (ACNUR). Aquella diáspora no constituyó una migración selectiva de élites profesionales como en épocas pretéritas, sino un verdadero éxodo popular que despojó a la nación de más del veinte por ciento de su población total, dispersándola por todos los rincones del hemisferio occidental."
            },
            {
                "type": "narration",
                "text": "El símbolo más estremecedor de este drama continental fue la figura de los 'caminantes'. Familias enteras compuestas por abuelos ancianos, madres con bebés en brazos y jóvenes recién graduados emprendieron travesías a pie de miles de kilómetros empujando maltrechos carritos de bebé y cargando mochilas descoloridas con los colores amarillo, azul y rojo de la bandera patria. Para llegar hacia el sur del continente —hacia Bogotá, Quito, Lima o Santiago de Chile—, los migrantes debían ascender a pie las alturas glaciales del páramo de Berlín, en la cordillera Oriental colombiana, a más de tres mil cuatrocientos metros sobre el nivel del mar. Con zapatos agujereados y abrigos improvisados con mantas donadas, desafiaron temperaturas bajo cero que provocaron hipotermias fulminantes en medio de la niebla densa de la montaña."
            },
            {
                "type": "narration",
                "text": "Yorman Colmenares, un joven mecánico de veintidós años procedente del estado Lara que recorrió a pie más de dos mil kilómetros hasta llegar a la capital peruana junto a su hermana Mireya, recuerda con estremecimiento aquellas jornadas: 'Caminar doce horas diarias por la orilla de una autopista esquivando camiones de carga te enseña lo que vale un sorbo de agua limpia. Hubo noches en el páramo donde sentíamos que los pies se congelaban; lo único que nos mantenía despiertos para no morir de frío era el compromiso sagrado de enviar dinero a nuestra madre enferma que quedó esperando en Barquisimeto'."
            },
            {
                "type": "narration",
                "text": "Frente a esta colosal emergencia humanitaria, la respuesta solidaria de los pueblos latinoamericanos alumbró lecciones conmovedoras de fraternidad cívica. El socorrista Amador, voluntario de la Cruz Roja en el albergue de Pamplona, relata cómo campesinos colombianos instalaban ollas humeantes de sopa caliente al borde de la carretera para alimentar gratuitamente a los caminantes exhaustos: 'Vimos el dolor más hondo en los ojos de esos muchachos, pero también una dignidad indestructible. Compartir con ellos una taza de café caliente y un par de calcetines secos era recordar que la frontera es una línea de papel y que el dolor del hermano nos interpela a todos por igual'."
            },
            {
                "type": "narration",
                "text": "En el terreno de las políticas públicas, Colombia adoptó en febrero de 2021 una decisión de vanguardia internacional: la creación del Estatuto Temporal de Protección para Migrantes Venezolanos (ETPV). Este marco normativo inédito en la región concedió un permiso de regularización migratoria por diez años a casi dos millones y medio de venezolanos, otorgándoles documentos de identidad oficiales, acceso pleno al sistema nacional de salud y educación pública y el derecho a trabajar formalmente con todas las garantías de ley, demostrando al mundo que la migración no debe gestionarse con muros ni deportaciones violentas, sino mediante la integración digna y el reconocimiento de derechos fundamentales."
            },
            {
                "type": "narration",
                "text": "Aunque otros miles de migrantes continuaron arriesgando sus vidas en rutas aún más peligrosas —como la temible selva tropical del Darién entre Colombia y Panamá en su anhelo de alcanzar la frontera de los Estados Unidos—, el éxodo venezolano ha transformado para siempre el mapa demográfico y social de América Latina. En las calles de Lima, en los hospitales de Bogotá, en los talleres de Santiago y en las escuelas de Quito, los migrantes venezolanos demuestran a diario que su mayor equipaje no fueron las privaciones padecidas, sino el coraje laborioso de un pueblo hermano que siembra futuro y dignidad en cada tierra que le abrió los brazos con generosidad fraterna."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál fue el paso geográfico montañoso que debían superar a pie los 'caminantes' en Colombia rumbo al sur del continente?",
                        "options": [
                            "El gélido páramo de Berlín en la cordillera Oriental colombiana, a más de tres mil cuatrocientos metros de altitud.",
                            "El cañón del Colorado en el desierto norteamericano.",
                            "La quebrada de Humahuaca en el norte argentino.",
                            "El paso de San Gotardo en los Alpes suizos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que los migrantes caminantes debían ascender a pie el páramo de Berlín en Colombia bajo temperaturas bajo cero y niebla densa."
                    },
                    {
                        "question": "¿Qué garantía fundamental otorgó el Estatuto Temporal de Protección (ETPV) implementado por Colombia en 2021?",
                        "options": [
                            "Diez años de regularización legal, acceso al sistema de salud, educación y permisos de trabajo formal para casi dos millones y medio de personas.",
                            "La obligación de permanecer en campos de detención temporal indefinidos.",
                            "La entrega automática de propiedades inmobiliarias en la capital.",
                            "Un pasaje aéreo de deportación forzosa hacia Centroamérica."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 detalla el ETPV colombiano: un hito de integración humanitaria que otorgó regularidad por 10 años, salud, educación y trabajo digno."
                    },
                    {
                        "question": "¿Qué cifra aproximada de personas abandonó Venezuela durante la crisis según los registros de la ONU?",
                        "options": [
                            "Más de siete millones setecientos mil venezolanos, representando más del veinte por ciento de la población del país.",
                            "Menos de cien mil personas en provincias limítrofes.",
                            "Un millón de personas exclusivamente con doble nacionalidad europea.",
                            "Cincuenta mil diplomáticos con salvoconductos oficiales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 cita las cifras oficiales del ACNUR: más de 7,7 millones de personas salieron de Venezuela durante la década de crisis."
                    }
                ]
            }
        }
    }

    story_ven2_05 = {
        "id": "b2-venezuelasabana-05",
        "title": "La arepa en el mapa: Gastronomía, resiliencia y la identidad sin fronteras",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociocultural de nivel B2 sobre la reinvención de la identidad venezolana en la diáspora: la expansión global de la arepa como embajada culinaria y afectiva, la fusión de tradiciones gastronómicas (el pabellón criollo, los tequeños, la gaita navideña), la integración laboral de millones de profesionales y el surgimiento de una Venezuela transcontinental unida por la solidaridad.",
        "characters": [
            "Cocinera Coromoto",
            "Sebastián",
            "Marta Elena"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En las calles cosmopolitas de Madrid, en las esquinas gastronómicas de Buenos Aires, a lo largo de las avenidas concurridas de Santiago de Chile o en los barrios bohemios de Montreal, un aroma inconfundible a maíz tostado sobre planchas de hierro caliente comenzó a conquistar los paladares del mundo entero. Al verse forzados a abandonar su tierra natal con el corazón desgarrado por la distancia, los venezolanos llevaron consigo en sus maletas el patrimonio intangible más entrañable e indestructible de su cultura cotidiana: la **arepa**. Aquella torta circular de harina de maíz precocida, crujiente por fuera y humeante por dentro, trascendió rápidamente su condición de alimento diario para convertirse en el símbolo supremo de la resiliencia, la dignidad laboral y la identidad de una nación que aprendió a renacer más allá de sus fronteras geopolíticas."
            },
            {
                "type": "narration",
                "text": "La genealogía de la arepa se remonta a miles de años antes de la llegada de los colonizadores europeos a las costas del Caribe. Los pueblos originarios cumanagoto, caribe y timoto-cuica cultivaban con reverencia sagrada el maíz tierno, desgranándolo sobre morteros de piedra pulida y amasándolo con agua de manantial para cocerlo sobre planchas de barro cocido llamadas 'budares'. El vocablo mismo proviene de la palabra indígena *erepa*, que designaba al pan sagrado de maíz. Tras la invención revolucionaria en la década de 1950 de la harina de maíz precocida por el ingeniero venezolano Luis Caballero Mejías y su posterior industrialización bajo la popular marca Harina P.A.N., la arepa se democratizó en todos los estratos sociales, consolidándose como el corazón palpitante del desayuno y la cena de cada hogar venezolano."
            },
            {
                "type": "narration",
                "text": "La cocinera Coromoto, una talentosa caraqueña de cincuenta y dos años que inauguró un exitoso restaurante de comida criolla en el céntrico barrio de Lavapiés en Madrid junto a su hijo Sebastián, atiende a una clientela diversa mientras voltea las arepas en el budare: 'La arepa es como el corazón del venezolano: noble, generosa y capaz de abrazar cualquier relleno con amor. Cuando un compatriota entra por esa puerta y muerde una 'reina pepiada' con su aguacate cremoso y su pollo desmechado, o una 'pelúa' con queso amarillo rallado, se le llenan los ojos de lágrimas porque no está comiendo solo harina; está saboreando los domingos en familia, la voz de su madre en la cocina y la patria que llevamos adentro'."
            },
            {
                "type": "narration",
                "text": "Junto a la arepa, la gastronomía venezolana expandió por el planeta los tequeños —dedos de masa de trigo crujiente rellenos de queso blanco fundido que coronan cualquier fiesta respetable—, el tradicional **pabellón criollo** —sinfonía mestiza de carne mechada, frijoles o caraotas negras, arroz blanco brillante y plátano maduro frito— y el asado negro bañado en melaza de caña de azúcar. En los meses decembrinos, la preparación colectiva de la hallaca —pastel festivo de masa de maíz teñida con onoto, relleno con un sofisticado guiso de tres carnes con alcaparras, uvas pasas y aceitunas, envuelto en hojas de plátano ahumadas— reúne a familias de la diáspora en apartamentos de todo el mundo al compás alegre de las gaitas zulianas del cuatro y la tambora."
            },
            {
                "type": "narration",
                "text": "Marta Elena, una médica pediatra egresada de la Universidad Central de Venezuela que revalidó sus títulos con honores en Chile y hoy coordina un centro de salud pública en Santiago, reflexiona sobre el significado sociológico de este renacimiento: 'Al principio nos veían solo como víctimas de una crisis trágica; hoy la sociedad chilena, peruana o española nos reconoce como médicos competentes, ingenieros rigurosos, docentes entregados y vecinos solidarios. La diáspora nos obligó a madurar, a superar cualquier arrogancia del antiguo petroestado y a valorar el trabajo honesto como la única fuente legítima de prosperidad'."
            },
            {
                "type": "narration",
                "text": "En ese diálogo fecundo entre las tierras de acogida y la memoria viva de la patria lejana, se ha forjado una **Venezuela transcontinental**: una nación sin límites territoriales que habita en las canciones de Simón Díaz tarareadas en el metro de París, en los niños que crecen hablando con acento mestizo en Bogotá o Lima y en la certeza invencible de que el desarraigo no destruyó la fraternidad de su pueblo. Cada arepa servida con orgullo en cualquier latitud del globo terráqueo confirma que Venezuela sigue en pie: hermosa, trabajadora y luminosa, tejiendo lazos indestructibles de hermandad con todos los pueblos del continente y del mundo."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué término indígena originario proviene la palabra 'arepa' según la investigación histórica?",
                        "options": [
                            "Del vocablo cumanagoto y caribe 'erepa', que designaba al pan sagrado de maíz.",
                            "Del nombre de una antigua hacienda colonial en los valles de Aragua.",
                            "De una raíz latina introducida por los sacerdotes misioneros capuchinos.",
                            "De una ordenanza militar dictada por Simón Bolívar durante la campaña libertadora."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que la palabra proviene del vocablo indígena cumanagoto 'erepa', con el cual los originarios llamaban al maíz y a su pan sagrado."
                    },
                    {
                        "question": "¿Cuáles son los ingredientes tradicionales que componen el relleno de la emblemática arepa 'reina pepiada'?",
                        "options": [
                            "Pollo desmechado aderezado con aguacate cremoso, mayonesa y limón.",
                            "Carne de cerdo ahumada con mostaza dulce y pepinillos agrios.",
                            "Pescado crudo marinado con cebolla morada y ají picante.",
                            "Queso de cabra madurado con mermelada de moras andinas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 describe la reina pepiada con su relleno de pollo desmechado, aguacate cremoso y mayonesa."
                    },
                    {
                        "question": "¿De qué manera la preparación de la hallaca en diciembre fortalece los vínculos de la diáspora venezolana en el exterior?",
                        "options": [
                            "Reúne a familias y comunidades enteras en un rito culinario colectivo que evoca la memoria hogareña al ritmo de gaitas zulianas.",
                            "Es un requisito consular obligatorio para renovar los pasaportes en las embajadas.",
                            "Sirve para recolectar fondos destinados a comprar empresas comerciales en Europa.",
                            "Es una competencia deportiva televisada en directo para todo el continente."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 detalla cómo la preparación familiar de las hallacas envueltas en hojas de plátano congrega a los venezolanos en el exterior en torno a su memoria festiva y musical."
                    }
                ]
            }
        }
    }

    # Consolidated Story for Regional Unit 16 (~700 words, strictly 650-825 words)
    story_ven2_capstone = {
        "id": "b2-venezuelasabana-consolidation",
        "title": "Paisajes inmemoriales y diáspora viva: La Venezuela transcontinental",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Gran crónica de consolidación de nivel B2 sobre la totalidad geográfica y humana de Venezuela: la inmensidad agreste de los Llanos y sus cantos de vaquería, la eternidad precámbrica de los tepuyes de Canaima, las lecciones éticas de la crisis socioeconómica, la dignidad heroica de los migrantes y la reconstrucción transcontinental de la venezolanidad a través del trabajo, el arte y la solidaridad.",
        "characters": [
            "Profesor Arreaza",
            "Liliana"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Recorrer con mirada profunda la totalidad de Venezuela supone contemplar una de las geografías más majestuosas, complejas y conmovedoras del continente americano. Durante el siglo veinte, el país se acostumbró a mirarse en el espejo deslumbrante de sus rascacielos caraqueños, en las autopistas colosales financiadas por el maná del petróleo y en el dinamismo vanguardista de sus universidades y museos de arte cinético. Sin embargo, cuando se desciende hacia el sur del territorio nacional y se cruza el cauce monumental del río Orinoco, se descubre que la verdadera columna vertebral de esta patria descansa sobre paisajes inmemoriales que anteceden por millones de años a la civilización humana y que forjaron el temple indoblegable de su pueblo ante la adversidad."
            },
            {
                "type": "narration",
                "text": "En las sabanas infinitas de Apure, Barinas y Guárico, los Llanos del Orinoco extienden su manto de pastizales y esteros donde el agua y el sol libran un combate eterno. Allí, el llanero a caballo demostró al mundo que la comunión con la naturaleza bravía no se construye mediante el exterminio de las especies, sino a través del respeto y la poesía oral. Los cantos de vaquería, proclamados por la UNESCO como Patrimonio Cultural Inmaterial, convirtieron la faena ruda del arreo ganadero en un cántico sagrado que sosiega al rebaño bajo la lluvia torrencial, mientras en los caneyes festivos el arpa llanera, el cuatro y las maracas encienden el zapateo del joropo y el duelo verbal del contrapunteo, demostrando la prodigiosa riqueza lírica de las gentes del campo."
            },
            {
                "type": "narration",
                "text": "Más al sur, en las profundidades del Escudo Guayanés, el Parque Nacional Canaima y la Gran Sabana custodian las rocas más arcaicas de la corteza planetaria. Sobre paredes verticales de arenisca rosada que desafían el cielo, los tepuyes se alzan como fortalezas del tiempo donde el pueblo originario Pemón venera a sus divinidades tutelares. Del colosal Auyán-tepui se desprende el Kerepakupai Vená —el Salto Ángel—, arrojando su cascada de casi mil metros de altitud en una nube de bruma irisada que nutre la selva tropical circundante. En las cumbres del Roraima, las plantas carnívoras y las especies vegetales endémicas recuerdan a la humanidad que en estas mesetas sagradas duerme la memoria de la creación de la Tierra, un tesoro biológico que demanda la protección ética de toda la comunidad internacional."
            },
            {
                "type": "narration",
                "text": "Esa misma entereza espiritual que desafía la inmensidad del llano y la altura de los tepuyes sostuvo a la sociedad venezolana durante los años más amargos de su historia republicana. Cuando el colapso del modelo rentista petrolero y el torbellino hiperinflacionario desarticularon las bases materiales de la vida cotidiana, las comunidades no se resignaron a la desesperanza. Con una resiliencia conmovedora, vecinos anónimos organizaron ollas solidarias, compartieron insumos médicos en hospitales en penumbra y tejieron redes de apoyo mutuo que amortiguaron los rigores de la escasez, demostrando que la mayor reserva de Venezuela jamás descansó en las arcas fiscales, sino en la nobleza compasiva de sus ciudadanos."
            },
            {
                "type": "narration",
                "text": "Y cuando la crisis forzó a más de siete millones de compatriotas a emprender el camino del éxodo por las carreteras del continente, la venezolanidad se transformó en una patria transcontinental. Los 'caminantes' que desafiaron el hielo del páramo de Berlín y las incertidumbres de fronteras desconocidas llevaron consigo el aroma del maíz asado en la arepa, la cadencia festiva de la gaita zuliana y una vocación irreductible por el trabajo honesto. En Bogotá, Lima, Santiago, Madrid y cientos de ciudades del mundo, los médicos, ingenieros, cocineros y artistas venezolanos retribuyen con generosidad la acogida brindada por los pueblos hermanos, convirtiendo el dolor de la partida en una sinfonía fecunda de integración latinoamericana."
            },
            {
                "type": "narration",
                "text": "El profesor Arreaza, contemplando junto a su alumna Liliana el horizonte donde el Orinoco se abraza con el Caroní en una frontera de aguas doradas y negras que no se mezclan de inmediato, sintetiza el horizonte de la nación: 'Venezuela ha padecido pruebas colosales, pero cada una de esas fracturas nos despojó del espejismo de la abundancia fácil para enseñarnos el valor de la dignidad, la democracia y el esfuerzo creador'. De los baluartes caraqueños a la bruma sagrada del Salto Ángel, del repique del arpa en el llano a las arepas que humean en cualquier confín del planeta, Venezuela late hoy como una patria sin fronteras, unida por la memoria, la fraternidad continental y la inextinguible esperanza de un porvenir de libertad y justicia plena."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis geográfica y cultural propone el texto respecto a las dos regiones emblemáticas del sur de Venezuela?",
                        "options": [
                            "Muestra que los Llanos con sus cantos ganaderos y Canaima con sus tepuyes milenarios constituyen la reserva telúrica, ecológica y espiritual más profunda de la nación.",
                            "Afirma que ambas regiones están completamente despobladas y carecen de interés cultural o biológico.",
                            "Sostiene que el sur venezolano debe dedicarse exclusivamente a la explotación de carbón a cielo abierto.",
                            "Indica que los Llanos y Canaima pertenecen a la soberanía de países europeos vecinos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los párrafos 1, 2 y 3 articulan la riqueza etnográfica y musical de los Llanos y la antigüedad precámbrica y biodiversidad sagrada de los tepuyes de Canaima."
                    },
                    {
                        "question": "¿De qué manera el texto caracteriza el surgimiento de la 'Venezuela transcontinental' a partir del éxodo migratorio?",
                        "options": [
                            "Como una nación viva que superó las fronteras geográficas, enriqueciendo a los países de acogida con su trabajo digno, su gastronomía y su solidaridad.",
                            "Como la desaparición definitiva e irreversible de la cultura venezolana en el extranjero.",
                            "Como un movimiento militar armado destinado a conquistar capitales vecinas.",
                            "Como un experimento gubernamental para despoblar las ciudades capitales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 define la Venezuela transcontinental: una identidad dispersa por el continente que aporta profesionalismo, cultura y hermandad en los países que la recibieron."
                    },
                    {
                        "question": "¿Cuál es la lección ética fundamental que deja la superación de la crisis del modelo rentista según las reflexiones del texto?",
                        "options": [
                            "Que la verdadera prosperidad de una nación no depende de la riqueza fácil del subsuelo, sino del trabajo productivo, la educación y la reconstrucción democrática e institucional.",
                            "Que los países latinoamericanos deben evitar la construcción de escuelas y museos artísticos.",
                            "Que la economía rentista de hidrocarburos es el único modelo viable para el desarrollo sostenible.",
                            "Que la solidaridad comunitaria es perjudicial para la convivencia ciudadana."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 subraya la lección histórica: liberarse del espejismo de la renta fácil para fundar el porvenir en el esfuerzo creador, la dignidad y la democracia."
                    }
                ]
            }
        }
    }

    # Write all regional stories
    write_json(f"stories/world/b2/{r1}.json", story_ven2_01)
    write_json(f"stories/world/b2/{r2}.json", story_ven2_02)
    write_json(f"stories/world/b2/{r3}.json", story_ven2_03)
    write_json(f"stories/world/b2/{r4}.json", story_ven2_04)
    write_json(f"stories/world/b2/{r5}.json", story_ven2_05)
    write_json(f"stories/world/b2/{rc_con}.json", story_ven2_capstone)
    write_json(f"stories/world/b2/{r_unit}.json", story_ven2_capstone)

    # Write Core Story
    write_json(f"stories/classics/b2/{c_unit}.json", story_core_16)

    # ----------------------------------------------------
    # Lessons Writing (Matching Schema Exactly)
    # ----------------------------------------------------
    # Core Lessons 1-5
    core_lessons_info = [
        ("b2-16-01", "lesson.b2.16.01", "Morfología del pluscuamperfecto de subjuntivo",
         "Master the morphological structure, auxiliary alternation (hubiera/hubiese), and anteriority value of the pluperfect subjunctive.",
         "morfología del pluscuamperfecto de subjuntivo: haber (hubiera/hubiese) + participio",
         ["Conjugate pluperfect subjunctive compound forms with regular and irregular participles.", "Analyze the anteriority relationship relative to past reference points.", "Recognize the predominant distribution of 'hubiera' across Latin America."]),
        ("b2-16-02", "lesson.b2.16.02", "Deseos retrospectivos y lamentos pasados con '¡Ojalá!'",
         "Deploy '¡Ojalá!' followed by pluperfect subjunctive to express retrospective past wishes, regrets, and unfulfilled nostalgic longings.",
         "oraciones desiderativas retrospectivas independientes con ¡Ojalá! y pluscuamperfecto de subjuntivo",
         ["Formulate retrospective regrets and nostalgic lamentations with '¡Ojalá hubiera/hubiese!'.", "Distinguish present wishes (imperfect) from unfulfilled past regrets (pluperfect).", "Evaluate emotional stances of remorse and wistfulness in authentic discourse."]),
        ("b2-16-03", "lesson.b2.16.03", "Estructuras condicionales contrafácticas con 'de haber + participio'",
         "Deploy abbreviated counterfactual conditional structures with 'de haber + participio' in formal, academic, and journalistic registers.",
         "estructuras condicionales contrafácticas implícitas con de haber + participio",
         ["Transform 'si hubiera + participio' into elegant 'de haber + participio' clauses.", "Place clitic pronouns correctly attached to the auxiliary infinitive (de habérselo dicho).", "Interpret counterfactual clauses in formal legal, investigative, and historical reports."]),
        ("b2-16-04", "lesson.b2.16.04", "Juicios retrospectivos y alternativas históricas en el debate crítico",
         "Formulate retrospective evaluations, historical alternatives, and counterfactual critique in intellectual essays and political discourse.",
         "fórmulas modales de evaluación retrospectiva: más hubiera valido, habríamos debido, bien pudiera haber sido",
         ["Formulate critical retrospective judgments using 'más nos hubiera valido + inf'.", "Deploy modal periphrases of past duty ('habríamos debido prever').", "Explore missed historical turning points and branching alternative scenarios."]),
        ("b2-16-05", "lesson.b2.16.05", "Matices estilísticos de 'hubiese' en la prosa literaria y ensayística",
         "Analyze the stylistic nuances, euphonic cadence, and literary prestige of the 'hubiese' variant in artistic and reflective prose.",
         "estilística narrativa y eufonía de la variante auxiliar en -se en la prosa culta",
         ["Analyze why authors employ 'hubiese' for introspective and lyrical resonance.", "Apply 'hubiese' strategically to prevent cacophonic repetition of -ra endings.", "Recognize stylistic register differences between fast journalism and classical narrative."])
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
        "id": "lesson.b2.16.consolidation",
        "title": "Consolidación: El pluscuamperfecto de subjuntivo e Ifigenia",
        "level": "B2",
        "goal": "Synthesize all aspects of the pluperfect subjunctive through classical psychological and feminist analysis of Teresa de la Parra's Ifigenia.",
        "grammar": "síntesis del pluscuamperfecto de subjuntivo: deseos pasados, de haber + participio y juicio crítico",
        "sections": [
            {"type": "goal", "items": [
                "Deploy retrospective past wishes and regrets with '¡Ojalá!' and pluperfect subjunctive.",
                "Abbreviate counterfactual conditions elegantly with 'de haber + participio'.",
                "Analyze literary and social dilemmas (emancipation vs. conventionalism) using nuanced counterfactual prose."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{l6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Conjuga con fluidez el pluscuamperfecto de subjuntivo en sus dos variantes (hubiera / hubiese).",
                "Formula lamentos y anhelos retrospectivos irreversibles mediante '¡Ojalá!'.",
                "Utiliza la construcción culta 'de haber + participio' en cláusulas condicionales contrafácticas.",
                "Aplica fórmulas de evaluación crítica sobre alternativas históricas ('más nos hubiera valido')."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-venezuelasabana-01", "lesson.b2.venezuelasabana.01", "Los Llanos del Orinoco: Joropo, ganado y poesía llanera",
         "Explore the vast savannas of Apure and Barinas, cattle culture, UNESCO intangible cattle work songs, and joropo music.",
         "geografía de los Llanos, cantos de vaquería de la UNESCO y organología del joropo",
         ["Trace the climatic rhythm between flooded winter marshes and dry summer grasslands.", "Analyze the ethnographic and lyrical value of the cattle herding work songs.", "Deploy pastoral, folkloric, and musicological vocabulary (sabana, vaquería, joropo, coplero)."]),
        ("b2-venezuelasabana-02", "lesson.b2.venezuelasabana.02", "La Gran Sabana, Canaima y el reino de los tepuyes",
         "Investigate the Precambrian geology of Canaima National Park, sacred Pemón tepui plateaus, and Angel Falls (Kerepakupai Vená).",
         "geología precámbrica del Escudo Guayanés, cosmovisión Pemón e hidrografía de cataratas",
         ["Analyze the ecological isolation and high endemism of sandstone tepui summits.", "Explore the Pemón spiritual relationship with Auyán-tepui, Roraima, and ancestral Mawari.", "Deploy geological, evolutionary, and geographic vocabulary (tepuy, meseta, catarata, precámbrico)."]),
        ("b2-venezuelasabana-03", "lesson.b2.venezuelasabana.03", "La crisis macroeconómica, la hiperinflación y el colapso del modelo rentista",
         "Examine the contemporary socioeconomic crisis in Venezuela: oil production collapse, hyperinflation, de facto dollarization, and civic resilience.",
         "economía política de la crisis, hiperinflación contemporánea y resiliencia social",
         ["Analyze the macroeconomic causes of hyperinflation and the breakdown of oil revenue.", "Examine the spontaneous de facto dollarization and the lifeline of diaspora remittances.", "Deploy macroeconomic, sociological, and resilience vocabulary (hiperinflación, colapso, resiliencia, remesas)."]),
        ("b2-venezuelasabana-04", "lesson.b2.venezuelasabana.04", "El éxodo venezolano: La mayor migración en la historia de América Latina",
         "Examine the continental displacement of over 7 million Venezuelans, the ordeal of the 'caminantes', and Colombia's landmark Temporary Protection Statute.",
         "sociología de las migraciones forzadas, rutas transcontinentales y derecho humanitario",
         ["Trace the migration routes across Andean alpine passes (páramo de Berlín) and the Darién jungle.", "Analyze the landmark humanitarian framework of Colombia's 10-year Temporary Protection Statute (ETPV).", "Deploy migration, human rights, and refugee reception vocabulary (éxodo, caminante, regularización, acogida)."]),
        ("b2-venezuelasabana-05", "lesson.b2.venezuelasabana.05", "La diáspora y la reinvención de la identidad venezolana en el exterior",
         "Analyze the transcontinental reinvention of Venezuelan identity abroad: global arepa diplomacy, music, and professional integration.",
         "antropología de la diáspora, diplomacia culinaria y patrimonio inmaterial transcontinental",
         ["Explore the culinary history and global expansion of the arepa (reina pepiada, pelúa, pabellón).", "Analyze the active civic, professional, and cultural contributions of the diaspora across host nations.", "Deploy diaspora, gastronomy, and cultural identity vocabulary (diáspora, arepa, arraigo, transcultural)."])
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
    write_json(f"lessons/b2/{rc_con}.json", {
        "id": "lesson.b2.venezuelasabana.consolidation",
        "title": "Consolidación: Paisajes inmemoriales y diáspora viva",
        "level": "B2",
        "goal": "Consolidate regional studies on Venezuela's southern territories, cattle culture, ancient tepuis, macroeconomic transitions, and transcontinental diaspora.",
        "grammar": "síntesis de estudios regionales venezolanos: llanos, tepuyes de Canaima y diáspora transcontinental",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize the cultural richness of the Venezuelan Llanos and Canaima's Precambrian geology.",
                "Reflect on the humanitarian resilience developed by civil society and the diaspora during the crisis.",
                "Appreciate the enduring, borderless vitality of Venezuelan identity across Latin America and the world."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{rc_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{rc_con}-ex.json", "exerciseRefs": [f"{rc_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la importancia etnográfica de los cantos de vaquería y la organología del joropo llanero.",
                "Reconozco el valor geológico universal de los tepuyes de Canaima y el Salto Ángel.",
                "Analizo las causas y respuestas solidarias frente a la hiperinflación y el éxodo migratorio.",
                "Valoro la reinvención de la identidad venezolana transcontinental a través del trabajo y la cultura."
            ]}
        ]
    })
    print("Completed LatAm Unit 16 (Venezuela Sabana) generation!")

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
            "title": "The Pluperfect Subjunctive in Independence",
            "stems": unit_stems_core,
            "track": "core"
        })

    existing_reg = next((u for u in b2_units if u.get("stems") == unit_stems_reg), None)
    if not existing_reg:
        b2_units.append({
            "title": "Venezuela II: The Llanos, Tepuis & Modern Diaspora",
            "stems": unit_stems_reg,
            "track": "regional"
        })

    with open(b2_units_path, "w", encoding="utf-8") as f:
        json.dump(b2_units, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated curriculum/units/b2.json with Unit 16!")

    # ----------------------------------------------------
    # 5. Programmatic Word Count Audit
    # ----------------------------------------------------
    stories = {
        "story_core_16": story_core_16,
        "story_ven2_01": story_ven2_01,
        "story_ven2_02": story_ven2_02,
        "story_ven2_03": story_ven2_03,
        "story_ven2_04": story_ven2_04,
        "story_ven2_05": story_ven2_05,
        "story_ven2_capstone": story_ven2_capstone
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
