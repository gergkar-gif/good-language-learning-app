#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Pair 11:
  - Core Unit 11: Mixed Conditionals & Restrictive Conditions (b2-11)
  - Regional Unit 11: Dominican Republic: The First European Settlement, Merengue & Transnational Identity (b2-dominicana)
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
        "b2-unit11-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "prerequisites, stipulations, contractual conditions, and temporal transitions"
        },
        "condicionales-mixtas-pasado-presente": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "mixed conditionals connecting past hypothetical causes to present realities"
        },
        "condicionales-mixtas-presente-pasado": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "mixed conditionals connecting ongoing general traits to past consequences"
        },
        "condicionales-restrictivas-con-tal-de-que": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "restrictive conditional connectors requiring subjunctive (con tal de que, siempre que)"
        },
        "condicionales-exceptivas-a-no-ser-que": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "exceptive conditional clauses requiring subjunctive (a no ser que, a menos que, salvo que)"
        },
        "condicionales-parenteticas-cortesia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "parenthetical conditional remarks and polite institutional mitigation"
        },
        "b2-dominicana-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "dominican geography, colonial heritage, music, border relations, and diaspora"
        },
        "dominicana-geografia-cordillera-bahias": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "descriptive complex sentences on the topography and ecology of the dominican republic"
        },
        "dominicana-santo-domingo-primada-america": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "historical reporting and colonial architecture of early santo domingo"
        },
        "dominicana-merengue-bachata-patrimonio": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "cultural analysis and musicological criticism of merengue and bachata"
        },
        "dominicana-frontera-haiti-convivencia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "discourse on shared border history, migration, and binational relations with haiti"
        },
        "dominicana-beisbol-diaspora-nueva-york": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "sociological analysis of baseball academies and the new york diaspora nexus"
        }
    }

    for k, v in new_skills.items():
        if k not in skill_reg["skills"]:
            skill_reg["skills"][k] = v

    with open(skill_reg_path, "w", encoding="utf-8") as f:
        json.dump(skill_reg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated skill-registry.json for Unit 11")

    grammar_titles_path = BASE / "indexes" / "grammar-titles.json"
    with open(grammar_titles_path, "r", encoding="utf-8") as f:
        grammar_titles = json.load(f)

    new_titles = {
        "condicionales-mixtas-pasado-presente": "mixed conditionals with past condition and present outcome",
        "condicionales-mixtas-presente-pasado": "mixed conditionals with general condition and past consequence",
        "condicionales-restrictivas-con-tal-de-que": "restrictive conditionals with subjunctive",
        "condicionales-exceptivas-a-no-ser-que": "exceptive conditionals with subjunctive",
        "condicionales-parenteticas-cortesia": "parenthetical conditional remarks and polite mitigation",
        "dominicana-geografia-cordillera-bahias": "topography and coastal biodiversity in the dominican republic",
        "dominicana-santo-domingo-primada-america": "colonial heritage and early institutions in santo domingo",
        "dominicana-merengue-bachata-patrimonio": "musical evolution of merengue and bachata in dominicana",
        "dominicana-frontera-haiti-convivencia": "border dynamics and shared island history with haiti",
        "dominicana-beisbol-diaspora-nueva-york": "baseball talent and transnational diaspora in the dominican republic"
    }

    for k, v in new_titles.items():
        grammar_titles[k] = v

    with open(grammar_titles_path, "w", encoding="utf-8") as f:
        json.dump(grammar_titles, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated grammar-titles.json for Unit 11")

    # -------------------------------------------------------------------------
    # CORE UNIT 11 (b2-11): Mixed Conditionals & Restrictive Conditions
    # -------------------------------------------------------------------------

    # Lesson 1: b2-11-01 - Condicionales mixtas: pasado con presente
    l1 = "b2-11-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.11.01",
        "lesson": l1,
        "title": "Requisitos, condiciones y repercusiones actuales",
        "theme": "Vocabulario de requisitos indispensables y consecuencias presentes",
        "words": [
            {"lemma": "el requisito", "translation": "requirement, prerequisite", "pos": "noun"},
            {"lemma": "la prerrogativa", "translation": "prerogative, privilege", "pos": "noun"},
            {"lemma": "subordinar", "translation": "to subordinate", "pos": "verb"},
            {"lemma": "indispensable", "translation": "indispensable, essential", "pos": "adjective"},
            {"lemma": "el escollo", "translation": "stumbling block, hurdle", "pos": "noun"},
            {"lemma": "condicionar", "translation": "to condition, to determine", "pos": "verb"},
            {"lemma": "la cláusula", "translation": "clause, stipulation", "pos": "noun"},
            {"lemma": "el compromiso", "translation": "commitment, compromise", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.11.01.mixtas-pasado-presente",
        "title": "Condicionales mixtas: condición en pasado y repercusión en presente",
        "sections": [
            {
                "type": "text",
                "title": "Cruce temporal entre hipótesis pasada y realidad presente",
                "content": "Las oraciones condicionales mixtas de tipo pasado-presente conectan una acción irreal ocurrida en el pasado con una consecuencia que subsiste en el presente o futuro. Se construyen mediante la fórmula: 'Si + pluscuamperfecto de subjuntivo (pasado), condicional simple (presente)': 'Si hubieras aceptado la beca en París el año pasado, ahora trabajarías como diplomático'."
            },
            {
                "type": "table",
                "title": "Esquema comparativo del condicional mixto",
                "rows": [
                    ["Tercer condicional puro (pasado-pasado)", "'Si hubieras estudiado, habrías aprobado el examen ayer'"],
                    ["Condicional mixto (pasado-presente)", "'Si hubieras estudiado aquella carrera, hoy tendrías más oportunidades'"],
                    ["Alternativa de apódosis con gerundio", "'Si hubiésemos tomado esa ruta, ahora estaríamos llegando a la costa'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el discurso formal y biográfico",
                "items": [
                    {"spanish": "Si el ministerio hubiera invertido en infraestructura hospitalaria hace cinco años, el sistema de salud no colapsaría hoy.", "english": "If the ministry had invested in hospital infrastructure five years ago, the healthcare system would not collapse today."},
                    {"spanish": "Si no nos hubiesen otorgado ese crédito inicial, no estaríamos celebrando el décimo aniversario de la empresa.", "english": "If they had not granted us that initial loan, we would not be celebrating the company's tenth anniversary."},
                    {"spanish": "Si el tratado comercial se hubiera ratificado en 2010, nuestro país tendría una posición arancelaria preferente.", "english": "If the trade agreement had been ratified in 2010, our country would have a preferential tariff position."}
                ]
            },
            {
                "type": "tip",
                "content": "Presta suma atención a los adverbios temporales como 'ahora', 'hoy', 'en la actualidad' o 'en estos momentos' en la apódosis, ya que actúan como la señal inequívoca para elegir condicional simple en lugar de compuesto."
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
                    ["el requisito", "requirement, prerequisite"],
                    ["el escollo", "stumbling block, hurdle"],
                    ["indispensable", "indispensable, essential"],
                    ["la cláusula", "clause, stipulation"]
                ],
                "teaches": ["b2-unit11-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si la empresa no hubiera diversificado sus inversiones en 2018, hoy __ al borde de la bancarrota. (estar - condicional simple)",
                "answer": "estaría",
                "english": "If the company had not diversified its investments in 2018, today it would be on the brink of bankruptcy.",
                "teaches": ["condicionales-mixtas-pasado-presente"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué se utiliza condicional simple en 'Si hubieras nacido en el siglo XIX, hoy no disfrutarías de estos derechos'?",
                "options": [
                    "Porque la prótasis alude a un hecho pasado no verificado y la apódosis a una consecuencia en el presente del hablante.",
                    "Porque en las oraciones condicionales mixtas nunca se admiten formas del modo subjuntivo.",
                    "Porque el verbo 'disfrutar' solo admite desinencias de condicional simple en registros literarios."
                ],
                "correct": 0,
                "teaches": ["condicionales-mixtas-pasado-presente"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Si", "hubiéramos", "firmado", "el", "acuerdo,", "hoy", "tendríamos", "mayores", "beneficios."],
                "solution": ["Si", "hubiéramos", "firmado", "el", "acuerdo,", "hoy", "tendríamos", "mayores", "beneficios."],
                "english": "If we had signed the agreement, today we would have greater benefits.",
                "teaches": ["condicionales-mixtas-pasado-presente"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Analista", "text": "¿Qué consecuencias tuvo la postergación de la reforma energética aprobada en 2015?"},
                    {"speaker": "Consultora", "text": "_____"},
                    {"speaker": "Analista", "text": "Esa miopía estratégica nos ata a combustibles fósiles sumamente costosos."}
                ],
                "options": [
                    "Si el congreso hubiera aprobado la ley en su momento, el país contaría hoy con una matriz eléctrica enteramente limpia.",
                    "Las turbinas eólicas generan energía mecánica a través de la fuerza del viento costero.",
                    "El precio del barril de petróleo crudo fluctúa según las tensiones geopolíticas globales."
                ],
                "correct": 0,
                "teaches": ["condicionales-mixtas-pasado-presente"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si hubiésemos tomado esa decisión a tiempo, hoy no enfrentaríamos esta crisis.",
                "english": "If we had made that decision in time, today we would not be facing this crisis.",
                "teaches": ["condicionales-mixtas-pasado-presente"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=11,
        title="Condicionales mixtas: pasado con presente",
        goal="Master mixed conditional sentences connecting past hypothetical causes (pluperfect subjunctive) to present realities (conditional simple).",
        grammar_desc="condicionales mixtas de pasado a presente: si hubiera hecho... hoy tendría",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Construct mixed conditionals linking past decisions to ongoing current realities.",
            "Use temporal markers (hoy, ahora, actualmente) to select the correct mood and tense in apodosis.",
            "Deploy vocabulary of prerequisites and commitments (requisito, cláusula, escollo, subordinar)."
        ]
    ))

    # Lesson 2: b2-11-02 - Condicionales mixtas: rasgo permanente con consecuencia pasada
    l2 = "b2-11-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.11.02",
        "lesson": l2,
        "title": "Condiciones permanentes y consecuencias retrospectivas",
        "theme": "Vocabulario de rasgos permanentes, salvedades y nulidades",
        "words": [
            {"lemma": "la salvedad", "translation": "qualification, exception, caveat", "pos": "noun"},
            {"lemma": "el agravio", "translation": "offense, grievance", "pos": "noun"},
            {"lemma": "restringir", "translation": "to restrict, to curtail", "pos": "verb"},
            {"lemma": "estipular", "translation": "to stipulate", "pos": "verb"},
            {"lemma": "el plazo perentorio", "translation": "peremptory deadline, strict term", "pos": "noun"},
            {"lemma": "vincular", "translation": "to bind, to link", "pos": "verb"},
            {"lemma": "la nulidad", "translation": "nullity, invalidity", "pos": "noun"},
            {"lemma": "sensato", "translation": "sensible, wise", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.11.02.mixtas-presente-pasado",
        "title": "Condicionales mixtas: condición general y consecuencia en el pasado",
        "sections": [
            {
                "type": "text",
                "title": "Rasgo permanente o intemporal con resultado pretérito",
                "content": "La segunda variante de condicional mixto expresa una condición intemporal o un rasgo permanente del sujeto (imperfecto de subjuntivo) que condicionó un hecho pasado específico (condicional compuesto o pluscuamperfecto de subjuntivo): 'Si fueras más prudente (rasgo permanente actual), no habrías firmado ese contrato fraudulento la semana pasada'."
            },
            {
                "type": "table",
                "title": "Estructura del condicional mixto presente-pasado",
                "rows": [
                    ["Prótasis (rasgo permanente)", "'Si fuera bilingüe...' / 'Si tuviera paciencia...'"],
                    ["Apódosis (resultado pasado)", "'...habría postulado al cargo en la embajada el año pasado'"],
                    ["Variante estilística de apódosis", "'...hubiera postulado al cargo en la embajada el año pasado'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate crítico y judicial",
                "items": [
                    {"spanish": "Si el magistrado fuera verdaderamente independiente, no habría dictado esa sentencia tan parcializada.", "english": "If the magistrate were truly independent, he would not have handed down such a biased ruling."},
                    {"spanish": "Si no amáramos tanto la libertad de cátedra, habríamos claudicado ante las presiones ministeriales.", "english": "If we did not love academic freedom so much, we would have yielded to ministerial pressures."},
                    {"spanish": "Si nuestra economía fuera menos vulnerable a los mercados externos, la devaluación de 1999 no habría causado tanto estrago.", "english": "If our economy were less vulnerable to external markets, the 1999 devaluation would not have wreaked such havoc."}
                ]
            },
            {
                "type": "tip",
                "content": "Distingue claramente entre un estado temporal ('si hubieras estado cansado ayer') y un rasgo definitorio o permanente ('si fueras una persona meticulosa'). Los rasgos permanentes exigen imperfecto de subjuntivo."
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
                    ["la salvedad", "qualification, caveat"],
                    ["restringir", "to restrict, to curtail"],
                    ["el plazo perentorio", "strict term, peremptory deadline"],
                    ["sensato", "sensible, wise"]
                ],
                "teaches": ["b2-unit11-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si el director fuera más prudente, no se __ involucrado en aquel litigio comercial el año pasado. (haber - condicional compuesto)",
                "answer": "habría",
                "english": "If the director were more prudent, he would not have gotten involved in that commercial litigation last year.",
                "teaches": ["condicionales-mixtas-presente-pasado"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué tipo de relación expresa 'Si no fuéramos tan exigentes, habríamos aceptado su oferta'?",
                "options": [
                    "Un rasgo permanente de personalidad en la condición que influyó en una decisión pretérita específica.",
                    "Una orden directa de un superior jerárquico que debe cumplirse en el futuro.",
                    "Una hipótesis matemática comprobada mediante experimentos de laboratorio."
                ],
                "correct": 0,
                "teaches": ["condicionales-mixtas-presente-pasado"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Si", "fueras", "más", "sensato,", "no", "habrías", "firmado", "ese", "documento."],
                "solution": ["Si", "fueras", "más", "sensato,", "no", "habrías", "firmado", "ese", "documento."],
                "english": "If you were more sensible, you would not have signed that document.",
                "teaches": ["condicionales-mixtas-presente-pasado"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Abogada", "text": "¿Por qué el testigo incurrió en tantas contradicciones durante el juicio oral?"},
                    {"speaker": "Fiscal", "text": "_____"},
                    {"speaker": "Abogada", "text": "Esa predisposición al engaño destruyó por completo su credibilidad ante el tribunal."}
                ],
                "options": [
                    "Si ese individuo fuera honesto por naturaleza, no habría falseado las declaraciones juradas en la instrucción penal.",
                    "Los códigos procesales civiles se actualizan mediante reformas votadas en el parlamento.",
                    "La sala de audiencias cuenta con micrófonos para registrar el testimonio de los peritos."
                ],
                "correct": 0,
                "teaches": ["condicionales-mixtas-presente-pasado"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si fueran más prudentes, no habrían desatendido las recomendaciones técnicas.",
                "english": "If they were more prudent, they would not have neglected the technical recommendations.",
                "teaches": ["condicionales-mixtas-presente-pasado"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=11,
        title="Condicionales mixtas: condición general y consecuencia en el pasado",
        goal="Construct mixed conditionals combining an ongoing trait or general condition (imperfect subjunctive) with a past result (compound conditional).",
        grammar_desc="condicionales mixtas de rasgo general a pasado: si fuera más prudente, no habría firmado...",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Formulate mixed conditionals where a timeless condition accounts for a specific past decision.",
            "Differentiate transient past conditions from persistent character traits.",
            "Deploy legal and deliberative vocabulary (salvedad, estipular, plazo perentorio, vincular)."
        ]
    ))

    # Lesson 3: b2-11-03 - Nexos condicionales restrictivos: siempre que, con tal de que, a condición de que
    l3 = "b2-11-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.11.03",
        "lesson": l3,
        "title": "Negociación contractual y condiciones estrictas",
        "theme": "Vocabulario de pactos, salvaguardas y acuerdos formales",
        "words": [
            {"lemma": "pactar", "translation": "to agree upon, to covenant", "pos": "verb"},
            {"lemma": "la contrapartida", "translation": "counterpart, quid pro quo", "pos": "noun"},
            {"lemma": "la salvaguarda", "translation": "safeguard, protection", "pos": "noun"},
            {"lemma": "la anuencia", "translation": "consent, concurrence", "pos": "noun"},
            {"lemma": "el canje", "translation": "exchange, trade", "pos": "noun"},
            {"lemma": "la fianza", "translation": "bail, security deposit, bond", "pos": "noun"},
            {"lemma": "conmutar", "translation": "to commute, to exchange", "pos": "verb"},
            {"lemma": "vinculante", "translation": "binding", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.11.03.condicionales-restrictivas",
        "title": "Nexos condicionales restrictivos: siempre que, con tal de que, a condición de que",
        "sections": [
            {
                "type": "text",
                "title": "Estipulación de requisitos indispensables con subjuntivo",
                "content": "Los nexos condicionales restrictivos expresan condiciones sine qua non: la apódosis solo se cumplirá si se verifica de modo estricto la circunstancia introducida por el conector. Exigen obligatoriamente el modo subjuntivo tanto en presente como en pasado: 'con tal de que', 'siempre que', 'siempre y cuando', 'a condición de que', 'con la condición de que'."
            },
            {
                "type": "table",
                "title": "Matices de los nexos restrictivos",
                "rows": [
                    ["'Con tal de que' (concesión interesada)", "'Firmaremos el pacto con tal de que garanticen la estabilidad laboral'"],
                    ["'A condición de que' (exigencia contractual)", "'El banco otorgará el préstamo a condición de que presenten avales bancarios'"],
                    ["'Siempre que / Siempre y cuando' (requisito estricto)", "'Aprobaremos la moción siempre y cuando se respeten los plazos legales'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en la diplomacia y el derecho",
                "items": [
                    {"spanish": "La oposición apoyará la reforma tributaria siempre y cuando los recursos se destinen a la salud pública.", "english": "The opposition will support the tax reform provided that the resources are allocated to public health."},
                    {"spanish": "El sindicato aceptó congelar los salarios con tal de que no se despidiera a ningún trabajador.", "english": "The union agreed to freeze wages provided that no worker was dismissed."},
                    {"spanish": "El presidente firmó el tratado a condición de que se resguardara la soberanía marítima de la nación.", "english": "The president signed the treaty on the condition that the nation's maritime sovereignty was protected."}
                ]
            },
            {
                "type": "tip",
                "content": "Cuidado con 'siempre que': cuando tiene valor temporal significa 'cada vez que' y rige indicativo para hechos habituales ('Siempre que viaja a Santo Domingo visita la Zona Colonial'). Solo rige subjuntivo cuando tiene valor condicional restrictivo ('Te prestaré el libro siempre que lo cuides')."
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
                    ["pactar", "to agree upon, to covenant"],
                    ["la contrapartida", "counterpart, quid pro quo"],
                    ["la salvaguarda", "safeguard, protection"],
                    ["vinculante", "binding"]
                ],
                "teaches": ["b2-unit11-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La delegación suscribirá el protocolo ambiental a condición de que los países industrializados __ fondos de mitigación. (aportar - presente subjuntivo)",
                "answer": "aporten",
                "english": "The delegation will sign the environmental protocol on the condition that industrialized nations provide mitigation funds.",
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo verbal exigen obligatoriamente las locuciones 'con tal de que' y 'a condición de que'?",
                "options": [
                    "Modo subjuntivo siempre, tanto en pasado como en presente.",
                    "Modo indicativo si la acción se considera segura o evidente.",
                    "Modo infinitivo compuesto únicamente."
                ],
                "correct": 0,
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Aceptaremos", "el", "trato", "con", "tal", "de", "que", "haya", "garantías."],
                "solution": ["Aceptaremos", "el", "trato", "con", "tal", "de", "que", "haya", "garantías."],
                "english": "We will accept the deal provided that there are guarantees.",
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministro", "text": "¿Bajo qué condiciones apoyará su bancada el presupuesto general del Estado?"},
                    {"speaker": "Portavoz parlamentario", "text": "_____"},
                    {"speaker": "Ministro", "text": "Tomamos nota de esa exigencia irrenunciable para incorporarla al articulado."}
                ],
                "options": [
                    "Daremos nuestra anuencia siempre y cuando se congelen las tarifas de servicios básicos para los sectores vulnerables.",
                    "El edificio del senado cuenta con alfombras rojas en las escalinatas principales.",
                    "Las sesiones legislativas ordinarias comienzan a las diez de la mañana los días martes."
                ],
                "correct": 0,
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Suscribiremos el acuerdo a condición de que se establezcan salvaguardas claras.",
                "english": "We will sign the agreement on the condition that clear safeguards are established.",
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=11,
        title="Nexos condicionales restrictivos: siempre que, con tal de que, a condición de que",
        goal="Master restrictive conditional connectors ('con tal de que', 'a condición de que', 'siempre que') requiring subjunctive in negotiations and formal treaties.",
        grammar_desc="condicionales restrictivas con subjuntivo: siempre y cuando, con tal de que, a condición de que",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Formulate contractual prerequisites using 'a condición de que' and 'con tal de que'.",
            "Distinguish conditional 'siempre que' (+ subj) from temporal 'siempre que' (+ ind).",
            "Deploy negotiation vocabulary (contrapartida, salvaguarda, anuencia, vinculante)."
        ]
    ))

    # Lesson 4: b2-11-04 - Nexos condicionales exceptivos y negativos: a no ser que, a menos que, salvo que
    l4 = "b2-11-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.11.04",
        "lesson": l4,
        "title": "Excepciones formales, dispensas y exoneraciones",
        "theme": "Vocabulario de causales de fuerza mayor y exenciones jurídicas",
        "words": [
            {"lemma": "la dispensa", "translation": "dispensation, exemption", "pos": "noun"},
            {"lemma": "la salvedad", "translation": "caveat, reservation", "pos": "noun"},
            {"lemma": "eximir", "translation": "to exempt, to excuse", "pos": "verb"},
            {"lemma": "la causal", "translation": "grounds, legal cause", "pos": "noun"},
            {"lemma": "la fuerza mayor", "translation": "force majeure, act of God", "pos": "noun"},
            {"lemma": "la exoneración", "translation": "exoneration, waiver", "pos": "noun"},
            {"lemma": "incurrir", "translation": "to incur, to fall into", "pos": "verb"},
            {"lemma": "perentorio", "translation": "peremptory, urgent, unappealable", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.11.04.condicionales-exceptivas",
        "title": "Nexos condicionales exceptivos y negativos: a no ser que, a menos que, salvo que",
        "sections": [
            {
                "type": "text",
                "title": "Formulación de la única excepción que invalidaría una regla",
                "content": "Los conectores condicionales exceptivos introducen el único acontecimiento capaz de impedir que se cumpla lo afirmado en la oración principal. Equivalen a 'si no...' y exigen obligatoriamente modo subjuntivo: 'a menos que', 'a no ser que', 'salvo que', 'excepto que': 'La huelga continuará a menos que la patronal presente una propuesta razonable'."
            },
            {
                "type": "table",
                "title": "Conectores exceptivos y alternancias de registro",
                "rows": [
                    ["'A menos que' / 'A no ser que'", "Formas estándar y formales: 'No habrá juicio a no ser que se presenten pruebas nuevas'"],
                    ["'Salvo que' / 'Excepto que'", "Frecuentes en el registro normativo: 'El plazo vencerá hoy, salvo que medie causa fortuita'"],
                    ["'Salvo si' / 'Excepto si'", "Rigen modo indicativo o imperfecto subjuntivo: 'Iré a la reunión, salvo si llueve demasiado'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en reglamentos institucionales",
                "items": [
                    {"spanish": "Los contratos de obra pública no podrán suspenderse a menos que intervenga una orden judicial fundada.", "english": "Public works contracts may not be suspended unless a well-founded court order intervenes."},
                    {"spanish": "El imputado no podrá abandonar el territorio nacional a no ser que el tribunal conceda una fianza especial.", "english": "The accused may not leave the national territory unless the court grants special bail."},
                    {"spanish": "La sesión parlamentaria continuará por tiempo indefinido salvo que la mayoría vote un receso.", "english": "The parliamentary session will continue indefinitely unless the majority votes for a recess."}
                ]
            },
            {
                "type": "tip",
                "content": "No confundas 'salvo que' (+ subjuntivo: 'salvo que cambie el clima') con 'salvo si' (+ indicativo: 'salvo si cambia el clima'). Ambos giros son correctos, pero la presencia de 'si' exige el indicativo en el presente."
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
                    ["la dispensa", "dispensation, exemption"],
                    ["eximir", "to exempt, to excuse"],
                    ["la causal", "legal cause, grounds"],
                    ["la fuerza mayor", "force majeure, act of God"]
                ],
                "teaches": ["b2-unit11-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La exportación de granos quedará prohibida a menos que las empresas __ el abastecimiento del mercado interno. (garantizar - presente subjuntivo)",
                "answer": "garanticen",
                "english": "Grain export will be prohibited unless companies guarantee supply to the domestic market.",
                "teaches": ["condicionales-exceptivas-a-no-ser-que"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿A qué formulación equivale exactamente 'No suspenderemos el desalojo a no ser que medie una orden judicial'?",
                "options": [
                    "A 'No suspenderemos el desalojo si no media una orden judicial'.",
                    "A 'Suspenderemos el desalojo aunque medie una orden judicial'.",
                    "A 'Suspenderemos el desalojo porque medió una orden judicial'."
                ],
                "correct": 0,
                "teaches": ["condicionales-exceptivas-a-no-ser-que"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "habrá", "acuerdo", "a", "menos", "que", "cedan", "en", "sus", "demandas."],
                "solution": ["No", "habrá", "acuerdo", "a", "menos", "que", "cedan", "en", "sus", "demandas."],
                "english": "There will be no agreement unless they yield on their demands.",
                "teaches": ["condicionales-exceptivas-a-no-ser-que"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Comisario", "text": "¿Bajo qué circunstancias se autorizaría el desembarco de la tripulación en cuarentena?"},
                    {"speaker": "Inspectora sanitaria", "text": "_____"},
                    {"speaker": "Comisario", "text": "De acuerdo; el buque permanecerá fondeado en la bahía hasta nuevo aviso."}
                ],
                "options": [
                    "Nadie podrá descender a tierra firme a menos que los médicos certifiquen la ausencia total de síntomas infecciosos.",
                    "Las gaviotas anidan en los acantilados rocosos durante los meses de primavera.",
                    "El puerto deportivo ofrece amarres seguros para yates de recreo."
                ],
                "correct": 0,
                "teaches": ["condicionales-exceptivas-a-no-ser-que"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "No modificaremos el contrato a no ser que intervenga una causal de fuerza mayor.",
                "english": "We will not modify the contract unless a force majeure event intervenes.",
                "teaches": ["condicionales-exceptivas-a-no-ser-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=11,
        title="Nexos condicionales exceptivos y negativos: a no ser que, a menos que, salvo que",
        goal="Master exceptive conditional clauses ('a no ser que', 'a menos que', 'salvo que') with subjunctive to formulate exceptions in formal regulations.",
        grammar_desc="condicionales exceptivas y negativas con subjuntivo: a menos que, a no ser que, salvo que",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Formulate negative exceptions using 'a menos que' and 'a no ser que' + subjunctive.",
            "Distinguish 'salvo que' (+ subj) from 'salvo si' (+ ind).",
            "Deploy administrative and legal vocabulary (dispensa, eximir, causal, fuerza mayor)."
        ]
    ))

    # Lesson 5: b2-11-05 - Condicionales parentéticas, atenuadas y de cortesía institucional
    l5 = "b2-11-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.11.05",
        "lesson": l5,
        "title": "Atenuación retórica, reservas y cortesía diplomática",
        "theme": "Vocabulario de reservas formales, objeciones y anuencias",
        "words": [
            {"lemma": "la objeción", "translation": "objection, challenge", "pos": "noun"},
            {"lemma": "la reserva", "translation": "reservation, caveat", "pos": "noun"},
            {"lemma": "el reparo", "translation": "qualm, objection, faultfinding", "pos": "noun"},
            {"lemma": "sopesar", "translation": "to weigh up, to ponder", "pos": "verb"},
            {"lemma": "la venia", "translation": "permission, leave, nod", "pos": "noun"},
            {"lemma": "la discrepancia", "translation": "discrepancy, disagreement", "pos": "noun"},
            {"lemma": "atenuar", "translation": "to attenuate, to tone down", "pos": "verb"},
            {"lemma": "legítimo", "translation": "legitimate, rightful", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.11.05.parenteticas-cortesia",
        "title": "Condicionales parentéticas, atenuadas y de cortesía institucional",
        "sections": [
            {
                "type": "text",
                "title": "Fórmulas condicionales de atenuación discursiva",
                "content": "En la oratoria parlamentaria, diplomática y académica, las cláusulas condicionales parentéticas sirven para matizar asertos categóricos, solicitar la anuencia del auditorio y formular críticas sin herir susceptibilidades: 'si se me permite la expresión', 'si no me equivoco', 'si cupiera alguna duda', 'si bien se mira'."
            },
            {
                "type": "table",
                "title": "Fórmulas canónicas de atenuación condicional",
                "rows": [
                    ["Permiso para opinar", "'Si se me permite la observación, el presupuesto adolece de imprecisiones'"],
                    ["Modestia epistemológica", "'Si no estoy en un error, la jurisprudencia avala nuestra postura'"],
                    ["Hipótesis de ponderación", "'Si bien se mira, ambas partes persiguen el mismo objetivo de fondo'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate parlamentario y académico",
                "items": [
                    {"spanish": "Si cupiera alguna objeción a este proyecto de ley, radicaría exclusivamente en su régimen transitorio.", "english": "If any objection to this bill were conceivable, it would lie exclusively in its transitional regime."},
                    {"spanish": "Con la venia de la presidencia, si se me permite intervenir, quisiera plantear un reparo de orden reglamentario.", "english": "With the chair's permission, if I may intervene, I would like to raise a point of order."},
                    {"spanish": "Si se analizan los resultados con ecuanimidad, salta a la vista que el crecimiento económico ha sido asimétrico.", "english": "If the results are analyzed with impartiality, it is evident that economic growth has been asymmetric."}
                ]
            },
            {
                "type": "tip",
                "content": "Estas fórmulas condicionales se aíslan obligatoriamente entre comas al redactar, marcando una pausa entonativa en el discurso oral formal."
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
                    ["la objeción", "objection, challenge"],
                    ["el reparo", "qualm, objection"],
                    ["sopesar", "to weigh up, to ponder"],
                    ["la venia", "permission, leave, nod"]
                ],
                "teaches": ["b2-unit11-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si se me __ intervenir en este debate, sugeriría posponer la votación hasta mañana. (permitir - presente indicativo)",
                "answer": "permite",
                "english": "If I am permitted to intervene in this debate, I would suggest postponing the vote until tomorrow.",
                "teaches": ["condicionales-parenteticas-cortesia"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función pragmática cumple el giro 'si bien se mira' en una exposición formal?",
                "options": [
                    "Atenúa una afirmación e invita al auditorio a reconsiderar el asunto desde una perspectiva más ecuánime.",
                    "Indica una duda absoluta sobre la veracidad de los hechos observados visualmente.",
                    "Exige la presentación obligatoria de fotografías como prueba pericial."
                ],
                "correct": 0,
                "teaches": ["condicionales-parenteticas-cortesia"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Si", "se", "me", "permite,", "quisiera", "hacer", "un", "breve", "reparo."],
                "solution": ["Si", "se", "me", "permite,", "quisiera", "hacer", "un", "breve", "reparo."],
                "english": "If I may, I would like to make a brief objection.",
                "teaches": ["condicionales-parenteticas-cortesia"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Senador", "text": "El dictamen de la comisión fue aprobado por mayoría absoluta."},
                    {"speaker": "Senadora opositora", "text": "_____"},
                    {"speaker": "Senador", "text": "Tiene usted la palabra para fundar su voto en contra."}
                ],
                "options": [
                    "Con la venia de la mesa directiva, si se me permite una precisión, desearía dejar asentada una reserva fundamental.",
                    "El reloj del recinto marca exactamente las cuatro y cuarto de la tarde.",
                    "Los diarios nacionales publicaron resúmenes de la jornada de ayer."
                ],
                "correct": 0,
                "teaches": ["condicionales-parenteticas-cortesia"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Si cupiera alguna objeción a la propuesta, convendría formularla con prontitud.",
                "english": "If any objection to the proposal were conceivable, it would be advisable to formulate it promptly.",
                "teaches": ["condicionales-parenteticas-cortesia"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=11,
        title="Condicionales parentéticas, atenuadas y de cortesía institucional",
        goal="Master parenthetical conditional formulas ('si se me permite', 'si bien se mira', 'si cupiera alguna duda') for diplomatic mitigation in institutional discourse.",
        grammar_desc="condicionales de cortesía y atenuación retórica en debates institucionales y académicos",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Deploy polite mitigation formulas in speeches ('si no me equivoco', 'si se me permite').",
            "Punctuate parenthetical conditional clauses properly with commas in formal prose.",
            "Use diplomatic vocabulary of reservation and consensus (reparo, venia, sopesar, discrepar)."
        ]
    ))

    # Consolidation: b2-11-consolidation
    l_con = "b2-11-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el requisito", "requirement, prerequisite"],
                    ["la salvedad", "qualification, caveat"],
                    ["la salvaguarda", "safeguard, protection"],
                    ["la causal", "legal cause, grounds"]
                ],
                "teaches": ["b2-unit11-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué esquema temporal caracteriza a la condicional mixta 'Si hubiéramos aceptado aquel plan, hoy tendríamos estabilidad'?",
                "options": [
                    "Condición irreal situada en el pasado que produce una consecuencia visible en el presente.",
                    "Condición habitual en presente que genera un resultado consumado en el pasado.",
                    "Mandato imperativo que exige cumplimiento inmediato en el futuro próximo."
                ],
                "correct": 0,
                "teaches": ["condicionales-mixtas-pasado-presente"]
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones contiene un nexo condicional restrictivo correctamente construido?",
                "options": [
                    "Aceptaremos el pacto a condición de que se garanticen los derechos adquiridos.",
                    "Aceptaremos el pacto a condición de que se garantizarán los derechos adquiridos.",
                    "Aceptaremos el pacto a condición de que se garantizan los derechos adquiridos."
                ],
                "correct": 0,
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No levantaremos el estado de emergencia a menos que la corte suprema __ la legalidad de los decretos. (avalar - presente subjuntivo)",
                "answer": "avale",
                "english": "We will not lift the state of emergency unless the supreme court endorses the legality of the decrees.",
                "teaches": ["condicionales-exceptivas-a-no-ser-que"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Si no hubiéramos negociado las cláusulas a tiempo, hoy estaríamos desprotegidos. [If we had not negotiated the clauses in time, today we would be unprotected.]",
                    "Si fuéramos más flexibles, habríamos alcanzado un acuerdo en aquella reunión. [If we were more flexible, we would have reached an agreement in that meeting.]",
                    "Firmaremos el contrato siempre y cuando respeten las salvaguardas pactadas. [We will sign the contract provided that they respect the agreed safeguards.]",
                    "La asamblea continuará a menos que la mayoría solicite un receso de cortesía. [The assembly will continue unless the majority requests a courtesy recess.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": [
                    "condicionales-mixtas-pasado-presente",
                    "condicionales-mixtas-presente-pasado",
                    "condicionales-restrictivas-con-tal-de-que",
                    "condicionales-exceptivas-a-no-ser-que"
                ]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Lector", "text": "¿Cómo definiría el sentido del destino en La tregua de Mario Benedetti?"},
                    {"speaker": "Crítica", "text": "_____"},
                    {"speaker": "Lector", "text": "Un conmovedor testimonio sobre la fragilidad de la felicidad cotidiana."}
                ],
                "options": [
                    "Martín Santomé vive atrapado en una condicional mixta desgarradora: si el amor de Laura no hubiera iluminado su tedio burocrático, hoy sería un anciano amargado sin memoria luminosa.",
                    "Los tranvías de Montevideo circulaban por la avenida 18 de Julio hasta la medianoche.",
                    "El puerto comercial del Río de la Plata conecta con las rutas fluviales del Paraná."
                ],
                "correct": 0,
                "teaches": ["condicionales-mixtas-pasado-presente"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aprobaremos el pliego de condiciones siempre que se respeten los plazos estipulados.",
                "english": "We will approve the specifications provided that the stipulated deadlines are respected.",
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta una cláusula contractual o directriz formal empleando un nexo restrictivo ('siempre y cuando', 'a condición de que') o un período condicional mixto.",
                        "answer": "La junta directiva autorizará el financiamiento del proyecto siempre y cuando los auditores externos avalen el balance contable sin reservas."
                    }
                ],
                "teaches": ["condicionales-restrictivas-con-tal-de-que"]
            }
        ]
    })

    # Classic Story for Unit 11: Mario Benedetti - La tregua
    story_core_11 = {
        "id": "story.b2.11.benedetti",
        "title": "Mario Benedetti: La tregua",
        "level": "B2",
        "lesson": 6,
        "type": "classic",
        "estimatedMinutes": 8,
        "characters": [
            "Martín Santomé",
            "Laura Avellaneda",
            "Jaime Santomé"
        ],
        "summary": "Adaptación pedagógica para nivel B2 de la célebre novela de Mario Benedetti: el diario íntimo de un oficinista a punto de jubilarse, el inesperado despertar del amor frente a la monotonía y la contingencia implacable del destino.",
        "author": "Mario Benedetti (Uruguay, 1920–2009)",
        "work": "La tregua (1960)",
        "source": "Adaptado para estudiantes de nivel B2 a partir de la novela clásica de Mario Benedetti",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Martín Santomé es un hombre de cuarenta y nueve años que cuenta los días con precisión burocrática para jubilarse como jefe contable en Montevideo. Viudo desde hacía dos décadas tras la muerte de su esposa Isabel, su existencia se había reducido a una rutina gris: revisar balances en un despacho oscuro, tomar café con leche y convivir con sus tres hijos adultos en una atmósfera de respetuosa distancia emocional. Santomé sentía que si el tedio no hubiera gobernado su vida durante tantos años, hoy no miraría el porvenir con semejante escepticismo cansado, temiendo que el retiro desnudara su absoluta soledad interior."
            },
            {
                "type": "narration",
                "text": "Para conjurar el vacío y ordenar sus pensamientos dispersos, Martín decide iniciar un diario personal donde anota sus reflexiones cotidianas sobre el paso del tiempo, la rutina de la oficina y las manías de sus subalternos. Todo parecía destinado a transcurrir por los mismos cauces previsibles hasta una mañana lluviosa de febrero en que ingresa al departamento contable un grupo de nuevos empleados jóvenes. Entre ellos destaca Laura Avellaneda, una mujer de veinticuatro años, de mirada serena, modales discretos y una inteligencia luminosa que contrasta de inmediato con la vulgaridad y la holgazanería imperantes entre los antiguos empleados. Desde el primer instante, Martín observa con asombro que la presencia silenciosa de la joven altera la pesada respiración de la oficina."
            },
            {
                "type": "narration",
                "text": "A medida que pasan las semanas, la admiración profesional de Santomé se transforma en una apasionada conmoción afectiva. Descubre que Laura no solo es una contable meticulosa, sino un ser humano dotado de calidez espiritual y profunda capacidad de comprensión. A pesar de los veinticinco años de diferencia de edad y del temor al ridículo social, Martín reúne el coraje para invitarla a conversar a un café de la plaza Independencia. Allí descubren una complicidad construida sobre confidencias pausadas y una mutua necesidad de afecto que desmorona las reservas que él había alzado contra el mundo."
            },
            {
                "type": "narration",
                "text": "Poco después, deciden alquilar un modesto departamento en un viejo edificio de la calle Coronel Brandzen para resguardar su intimidad del escrutinio de los colegas de trabajo y de las miradas censuradoras de la sociedad provinciana. En ese refugio soleado, adornado apenas con un par de sillas y una mesa de pino, florece entre ambos un amor luminoso, tierno y sincero que devuelve a Martín una vitalidad que creía extinta para siempre. En las páginas de su diario, el contable escribe conmovido que Dios o el destino le han concedido una 'tregua': un paréntesis inesperado de felicidad plena y redención en medio del largo y áspero combate de la monotonía cotidiana."
            },
            {
                "type": "narration",
                "text": "Martín comprende entonces que si Laura no hubiera aparecido en su oficina aquella mañana de invierno, hoy seguiría siendo un autómata gris condenado a vegetar entre libros mayores y facturas sin memoria de belleza. El amor de la joven le devuelve la alegría de los sentidos y la fe en el porvenir; juntos planifican viajes por el interior del país y sueñan con la vida compartida que inaugurarán en cuanto se concrete su jubilación definitiva. Santomé se siente transformado: sus relaciones familiares con sus hijos mejoran gracias a una nueva tolerancia, y en la oficina sus antiguos empleados notan que la severidad adusta del jefe ha dejado paso a una mirada comprensiva y benevolente."
            },
            {
                "type": "narration",
                "text": "Sin embargo, la felicidad humana suele estar condicionada por una fragilidad desgarradora que ninguna cautela puede conjurar. A comienzos de junio, Laura contrae un fuerte resfriado que la obliga a guardar reposo en su casa familiar. Pasan los días sin que regrese a la oficina y las cartas que Martín le envía no reciben respuesta. Desesperado por la incertidumbre y obligado a mantener la reserva para no comprometer el honor de la muchacha ante su familia conservadora, Santomé vive semanas de angustia indecible hasta que una tarde recibe la llamada devastadora del tío de Laura: la joven había sufrido un ataque repentino de gripe agravado por una complicación pulmonar irreversible, falleciendo en el sanatorio en la más absoluta soledad clínica."
            },
            {
                "type": "narration",
                "text": "El impacto de la noticia desmorona el mundo de Martín de manera fulminante. Al regresar a su departamento vacío, comprende con amarga lucidez que la tregua ha concluido para siempre y que la rutina implacable reclama de nuevo sus derechos legítimos sobre su vida. No obstante, mientras cierra su diario con mano temblorosa frente al horizonte plomizo del Río de la Plata, sabe que nada podrá arrebatarle el milagro de haber sido amado con tanta pureza: si no hubiera conocido a Laura Avellaneda, jamás habría sabido que la felicidad existía, y esa certeza luminosa, aun teñida por el dolor del duelo irreparable, será el escudo secreto que lo acompañará hasta el último de sus días."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿En qué circunstancias vitales y anímicas se encontraba Martín Santomé antes de conocer a Laura Avellaneda?",
                        "options": [
                            "Llevaba una existencia rutinaria y solitaria como jefe contable viudo, esperando con escepticismo una inminente jubilación.",
                            "Acababa de regresar del exilio político en Europa tras fundar una editorial de poesía vanguardista.",
                            "Administraba una estancia ganadera en el departamento de Tacuarembó amenazada por la sequía.",
                            "Preparaba su candidatura política para el consejo de administración municipal de la capital uruguaya."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 detalla que Santomé era un viudo de 49 años que vivía sumido en la rutina contable y el aislamiento emocional, esperando su jubilación."
                    },
                    {
                        "question": "¿Qué significado otorgaba Santomé al concepto de 'la tregua' en las páginas de su diario íntimo?",
                        "options": [
                            "Un paréntesis inesperado de felicidad y amor luminoso concedido por el destino en medio de la monotonía cotidiana.",
                            "Un armisticio diplomático firmado entre las facciones gremiales de los empleados de comercio.",
                            "Una prórroga legal concedida por el tribunal de apelaciones para evitar el desahucio de su vivienda.",
                            "Un descanso médico temporal que le permitía ausentarse de la oficina durante los meses de verano."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 explica que Santomé definió su relación con Laura como una tregua providencial de plenitud afectiva frente a la aspereza de la vida gris."
                    },
                    {
                        "question": "¿A qué certeza íntima llega Martín Santomé tras el trágico fallecimiento de Laura al final del relato?",
                        "options": [
                            "Que el dolor del duelo no borra el milagro de haber descubierto la felicidad auténtica a través del amor.",
                            "Que debe renunciar de inmediato a sus derechos jubilatorios para marcharse a vivir a Buenos Aires.",
                            "Que las cartas y memorias escritas en su diario deben ser destruidas para no despertar suspicacias familiares.",
                            "Que el trabajo en la oficina es la única salvación moral frente a la fragilidad de las ilusiones humanas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 7 subraya que, pese a la desolación de la pérdida, la certeza de haber amado y sido amado será el consuelo imperecedero de su existencia."
                    }
                ]
            }
        }
    }
    write_json(f"stories/classics/b2/b2-11.json", story_core_11)

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=11,
        title="Unit 11 Consolidation: Mixed Conditionals & Restrictive Conditions",
        goal="Consolidate mixed conditionals, restrictive connectors (con tal de que, siempre que), and exceptive clauses through literary analysis of Benedetti's 'La tregua'.",
        grammar_desc="síntesis de condicionales mixtas (pasado-presente y presente-pasado), nexos restrictivos con subjuntivo y atenuación de cortesía",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Formulate cross-temporal mixed conditionals connecting past events to present realities.",
            "Deploy restrictive and exceptive conditional connectors ('con tal de que', 'a no ser que') with subjunctive.",
            "Apply parenthetical polite formulas ('si se me permite', 'si bien se mira') in formal prose.",
            "Analyze the existential turning points in Mario Benedetti's 'La tregua'."
        ],
        checklist_items=[
            "I can formulate mixed conditionals linking past unfulfilled events to present consequences.",
            "I can connect general/permanent traits to specific past results with mixed conditionals.",
            "I can deploy restrictive conditional connectors ('con tal de que', 'siempre que') requiring subjunctive.",
            "I can use exceptive clauses ('a no ser que', 'salvo que') in administrative and legal writing."
        ],
        story_ref=f"stories/classics/b2/b2-11.json"
    ))
    print("Completed Core Unit 11 generation!")

    # -------------------------------------------------------------------------
    # REGIONAL TRACK UNIT 11 (b2-dominicana): Dominican Republic: The First Settlement, Merengue & Diaspora
    # -------------------------------------------------------------------------

    # Lesson 1: b2-dominicana-01 - De la cordillera Central a las bahías caribeñas
    lc1 = "b2-dominicana-01"
    write_json(f"vocabulary/b2/{lc1}-voc.json", {
        "id": "vocab.b2.dominicana.01",
        "lesson": lc1,
        "title": "Geografía física dominicana y biodiversidad antillana",
        "theme": "Vocabulario de orografía caribeña, cordilleras y santuarios marinos",
        "words": [
            {"lemma": "el mogote", "translation": "limestone hill, mogote", "pos": "noun"},
            {"lemma": "el cayo", "translation": "cay, key, small sandy island", "pos": "noun"},
            {"lemma": "el manglar", "translation": "mangrove swamp", "pos": "noun"},
            {"lemma": "el santuario", "translation": "sanctuary, reserve", "pos": "noun"},
            {"lemma": "la cordillera", "translation": "mountain range", "pos": "noun"},
            {"lemma": "el arrecife", "translation": "reef", "pos": "noun"},
            {"lemma": "la ensenada", "translation": "cove, small bay", "pos": "noun"},
            {"lemma": "endémico", "translation": "endemic, native", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{lc1}-a-gr.json", {
        "id": "grammar.b2.dominicana.01.geografia-cordillera",
        "title": "De la cordillera Central a las bahías caribeñas",
        "sections": [
            {
                "type": "text",
                "title": "Descripción geográfica y oraciones subordinadas de relativo complejo",
                "content": "La caracterización física y ambiental de la República Dominicana en nivel B2 integra construcciones relativas con preposición ('en cuyas cumbres se registran temperaturas bajo cero'), participios adjetivales concertados ('resguardada por densos manglares costeros') y conectores de contraste geográfico ('mientras que en el sur árido...')."
            },
            {
                "type": "table",
                "title": "Recursos descriptivos del relieve antillano",
                "rows": [
                    ["Relativo compuesto 'en cuyo'", "'La cordillera Central, en cuyas faldas nacen los principales ríos del país'"],
                    ["Participio concertado", "'El banco de la Plata, declarado santuario de mamíferos marinos en 1986'"],
                    ["Contraste climático", "'Frente a la frondosidad de Samaná, el valle de Neiba ostenta una aridez desértica'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en estudios geográficos dominicanos",
                "items": [
                    {"spanish": "El Pico Duarte, con 3087 metros de altitud, constituye el techo geográfico indiscutible de todas las Antillas.", "english": "Pico Duarte, at 3,087 meters above sea level, constitutes the undisputed geographical roof of all the Antilles."},
                    {"spanish": "Cada invierno, miles de ballenas jorobadas migran desde el Atlántico norte hacia la bahía de Samaná para aparearse.", "english": "Every winter, thousands of humpback whales migrate from the North Atlantic to Samaná Bay to mate."},
                    {"spanish": "Los humedales del parque nacional Los Haitises albergan cavernas kársticas con petroglifos de la cultura taína.", "english": "The wetlands of Los Haitises National Park shelter karst caves with Taíno culture petroglyphs."}
                ]
            },
            {
                "type": "tip",
                "content": "Para describir altitudes y microclimas de montaña en el Caribe, recurre a términos orográficos precisos: 'piso altitudinal', 'estribación montañosa', 'vegetación de páramo', 'bosque nublado'."
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
                    ["el cayo", "cay, small sandy island"],
                    ["el manglar", "mangrove swamp"],
                    ["el arrecife", "reef"],
                    ["endémico", "endemic, native"]
                ],
                "teaches": ["b2-dominicana-vocab"]
            },
            {
                "id": f"{lc1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué récord geográfico ostenta el Pico Duarte en el territorio de la República Dominicana?",
                "options": [
                    "Es la cumbre más alta de todas las Antillas y de toda la región insular del Caribe.",
                    "Es el volcán activo con el lago de lava más profundo del océano Atlántico.",
                    "Es la meseta submarina más extensa situada frente a las costas de Sudamérica."
                ],
                "correct": 0,
                "teaches": ["dominicana-geografia-cordillera-bahias"]
            },
            {
                "id": f"{lc1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La bahía de Samaná alberga aguas templadas donde las ballenas jorobadas __ sus crías cada invierno. (dar a luz - presente indicativo)",
                "answer": "dan a luz",
                "english": "Samaná Bay harbors temperate waters where humpback whales give birth to their calves every winter.",
                "teaches": ["dominicana-geografia-cordillera-bahias"]
            },
            {
                "id": f"{lc1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Pico", "Duarte", "es", "la", "cumbre", "más", "alta", "del", "Caribe."],
                "solution": ["El", "Pico", "Duarte", "es", "la", "cumbre", "más", "alta", "del", "Caribe."],
                "english": "Pico Duarte is the highest peak in the Caribbean.",
                "teaches": ["dominicana-geografia-cordillera-bahias"]
            },
            {
                "id": f"{lc1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Bióloga", "text": "¿Qué importancia ecológica reviste el parque nacional Los Haitises?"},
                    {"speaker": "Guía ambiental", "text": "_____"},
                    {"speaker": "Bióloga", "text": "Un auténtico tesoro hidrográfico y arqueológico que debemos preservar sin concesiones."}
                ],
                "options": [
                    "Constituye un formidable laberinto kárstico de mogotes y manglares que recarga los acuíferos subterráneos de la región oriental.",
                    "Dispone de pistas pavimentadas para el aterrizaje de aeronaves de carga pesada.",
                    "Es el principal centro de refinación de azúcar mascabado de toda la isla."
                ],
                "correct": 0,
                "teaches": ["dominicana-geografia-cordillera-bahias"]
            },
            {
                "id": f"{lc1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las ballenas jorobadas acuden puntualmente a las aguas templadas de Samaná.",
                "english": "Humpback whales arrive punctually to the warm waters of Samaná.",
                "teaches": ["dominicana-geografia-cordillera-bahias"]
            }
        ]
    })

    # Regional Story 1: b2-dominicana-01.json
    story_dom_01 = {
        "id": "b2-dominicana-01",
        "title": "De la cordillera Central a las bahías caribeñas",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica geográfica y ecológica de nivel B2 sobre la República Dominicana: la orografía de la cordillera Central, las cumbres del Pico Duarte, el santuario marino de Samaná y el laberinto kárstico de Los Haitises.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Ocupando las dos terceras partes orientales de la isla de La Española, la República Dominicana despliega una diversidad orográfica y ecosistémica que desafía el estereotipo simplista del Caribe como un mero rosario de playas de arena blanca bordeadas de cocoteros. Con una superficie de más de cuarenta y ocho mil kilómetros cuadrados, este territorio insular alberga el relieve más accidentado, abrupto y espectacular de todas las Antillas Mayores. Su columna vertebral está constituida por la imponente cordillera Central, un formidable macizo geológico de origen cretácico cuyas cumbres escarpadas se elevan por encima de los tres mil metros, erigiéndose en el auténtico corazón hidrográfico del cual nacen los ríos más caudalosos del país, tales como el Yaque del Norte y el Yaque del Sur, arterias vitales que fertilizan los valles agrícolas más productivos de la nación."
            },
            {
                "type": "narration",
                "text": "En el epicentro de este macizo montañoso se alza el Pico Duarte, que con sus 3087 metros de altitud sobre el nivel del mar representa el techo geográfico indiscutible de toda la cuenca del Caribe insular. Ascender por sus senderos empinados, flanqueados por densos bosques de pino criollo (Pinus occidentalis) y helechos arborescentes milenarios, introduce al viajero en un mundo donde el clima tropical de las llanuras costeras cede su paso a un microclima alpino templado. En altiplanos contiguos como Valle Nuevo, situado a más de dos mil doscientos metros de altura, las temperaturas descienden con frecuencia por debajo del punto de congelación durante las madrugadas invernales, cubriendo la vegetación de páramo con una delicada capa de escarcha plateada que sorprende a quienes asocian el Caribe únicamente con el calor perpetuo."
            },
            {
                "type": "narration",
                "text": "Hacia el noreste, la geografía insular se transforma radicalmente al encontrarse con la península y bahía de Samaná, uno de los enclaves marítimos más sobrecogedores y biológicamente ricos de todo el Atlántico occidental. Protegida por una estrecha lengua de tierra tapizada de palmeras y colinas exuberantes, esta bahía resguarda el Santuario de Mamíferos Marinos de los Bancos de la Plata y la Navidad. Cada año, entre los meses de enero y marzo, más de tres mil ballenas jorobadas (Megaptera novaeangliae) completan una migración épica de miles de kilómetros desde las aguas gélidas de Groenlandia e Islandia para cortejarse, aparearse y dar a luz a sus ballenatos en las aguas cálidas y protegidas de la bahía dominicana, brindando un espectáculo majestuoso de saltos acrobáticos que atrae a científicos y observadores del mundo entero."
            },
            {
                "type": "narration",
                "text": "En el extremo sur de la misma bahía emerge otro prodigio de la naturaleza antillana: el parque nacional Los Haitises. Con una toponimia de origen taíno que significa 'tierra de colinas' o 'tierra alta', este parque constituye un colosal karst tropical de colinas cónicas o mogotes de piedra caliza que emergen verticalmente del agua entre cuarenta y cien metros de altura. Tapizados por una vegetación selvática impenetrable de orquídeas silvestres y bejucos, estos mogotes forman un dédalo acuático de canales estrechos flanqueados por la mayor concentración de manglares rojos y negros del Caribe, ecosistema primordial que sirve de criadero natural a innumerables especies de peces, moluscos y colonias de aves marinas como pelícanos y fragatas."
            },
            {
                "type": "narration",
                "text": "El laberinto kárstico de Los Haitises atesora asimismo una dimensión histórica y espiritual invaluable en sus innumerables grutas subterráneas, tales como la Cueva de la Línea y la Cueva de San Gabriel. En sus paredes umbrías de caliza fosilífera se conservan cientos de pictografías y petroglifos trazados con carbón vegetal y resinas por los aborígenes taínos hace más de un milenio, representaciones estilizadas de lechuzas sagradas, peces míticos y chamanes en trance que testimonian la profunda comunión religiosa que los pueblos originarios mantenían con este entorno sagrado."
            },
            {
                "type": "narration",
                "text": "En agudo contraste con la exuberancia húmeda de Samaná y el verdor de la cordillera Central, el suroeste dominicano despliega la singular aridez de la hoya de Enriquillo. En esta profunda depresión tectónica se encuentra el lago Enriquillo, el cuerpo de agua más extenso de las Antillas y el punto más bajo de la región insular caribeña, situado a más de cuarenta metros por debajo del nivel del mar. Sus aguas hipersalinas albergan una población extraordinaria de cocodrilos americanos (Crocodylus acutus) y grandes bandadas de flamencos rosados que anidan en las inmediaciones de la isla Cabritos, confirmando la fascinante multiplicidad climática y biológica de la geografía dominicana."
            },
            {
                "type": "narration",
                "text": "Esta deslumbrante variedad territorial ha condicionado históricamente los patrones de asentamiento humano y el desarrollo socioeconómico de la República Dominicana. Desde los valles tabacaleros y arroceros del Cibao hasta las plantaciones azucareras del Este y los enclaves turísticos de Punta Cana y Puerto Plata, la nación quisqueyana ha aprendido a convivir con una naturaleza tan generosa como imponente, cuyo resguardo ambiental representa hoy una prioridad ineludible para garantizar la sostenibilidad de su patrimonio hídrico y su riqueza ecológica ante los desafíos del cambio climático global."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué rasgo orográfico singular distingue al Pico Duarte en el contexto geográfico de las Antillas?",
                        "options": [
                            "Es la montaña más elevada de todas las Antillas con más de tres mil metros de altitud.",
                            "Es la única cima insular del Caribe que conserva un glaciar de hielo perpetuo.",
                            "Es un cráter basáltico que alberga una laguna termal sulfurosa en su caldera.",
                            "Es una meseta kárstica plana utilizada como pista de aterrizaje militar durante el siglo XIX."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 subraya que con 3087 metros de altura, el Pico Duarte es la cumbre más alta de todas las Antillas y del Caribe insular."
                    },
                    {
                        "question": "¿Por qué la bahía de Samaná es considerada un santuario marino de trascendencia mundial?",
                        "options": [
                            "Porque miles de ballenas jorobadas migran cada invierno desde el Atlántico norte para reproducirse en sus aguas.",
                            "Porque alberga el arrecife coralino más profundo del planeta donde habitan calamares gigantes.",
                            "Porque es la única ensenada del Caribe donde no existen mareas ni corrientes oceánicas.",
                            "Porque fue el puerto de abastecimiento exclusivo de la flota ballenera del Pacífico sur."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 explica que miles de ballenas jorobadas migran anualmente desde el Atlántico norte hacia Samaná para aparearse y tener a sus crías."
                    },
                    {
                        "question": "¿Qué singularidad física caracteriza al lago Enriquillo en el suroeste dominicano?",
                        "options": [
                            "Es un lago hipersalino situado a más de cuarenta metros bajo el nivel del mar que alberga cocodrilos americanos.",
                            "Es una laguna de agua dulce alimentada exclusivamente por manantiales geotérmicos.",
                            "Es un estuario artificial dragado a comienzos del siglo XX para el cultivo del arroz.",
                            "Es una represa hidroeléctrica que suministra energía a la capital haitiana."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 describe el lago Enriquillo como una depresión hipersalina situada bajo el nivel del mar con fauna de cocodrilos y flamencos."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc1}.json", story_dom_01)

    write_json(f"lessons/b2/{lc1}.json", make_lesson(
        stem=lc1,
        unit_num=11,
        title="De la cordillera Central a las bahías caribeñas",
        goal="Analyze the physical geography, alpine microclimates, and marine biodiversity of the Dominican Republic using relative and contrasting structures.",
        grammar_desc="oraciones relativas complejas, adjetivación orográfica y léxico ambiental dominicano",
        grammar_ref=f"grammar/b2/{lc1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc1}-voc.json",
        ex_ref=f"exercises/b2/{lc1}-ex.json",
        ex_ids=[f"{lc1}.ex01", f"{lc1}.ex02", f"{lc1}.ex03", f"{lc1}.ex04", f"{lc1}.ex05", f"{lc1}.ex06"],
        goals=[
            "Examine the orographic dominance of the Cordillera Central and Pico Duarte.",
            "Analyze the ecological role of the Samaná whale sanctuary and Los Haitises karst.",
            "Deploy geographical and biodiversity vocabulary (cayo, manglar, arrecife, ensenada, endémico)."
        ],
        story_ref=f"stories/world/b2/{lc1}.json"
    ))

    # Lesson 2: b2-dominicana-02 - La Isabela y Santo Domingo: El primer cabildo y universidad de América
    lc2 = "b2-dominicana-02"
    write_json(f"vocabulary/b2/{lc2}-voc.json", {
        "id": "vocab.b2.dominicana.02",
        "lesson": lc2,
        "title": "La primada de América, cabildos coloniales y debates teológicos",
        "theme": "Vocabulario de instituciones virreinales, arquitectura colonial y derechos tempranos",
        "words": [
            {"lemma": "el cabildo", "translation": "town council, chapterhouse", "pos": "noun"},
            {"lemma": "la primada", "translation": "first/primate cathedral or university", "pos": "noun"},
            {"lemma": "el alcázar", "translation": "fortified palace, alcazar", "pos": "noun"},
            {"lemma": "el sermón", "translation": "sermon", "pos": "noun"},
            {"lemma": "la encomienda", "translation": "encomienda (colonial labor/tribute system)", "pos": "noun"},
            {"lemma": "el fraile", "translation": "friar, monk", "pos": "noun"},
            {"lemma": "la bula", "translation": "papal bull", "pos": "noun"},
            {"lemma": "inquisitivo", "translation": "inquisitive, probing", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{lc2}-a-gr.json", {
        "id": "grammar.b2.dominicana.02.santo-domingo-primada",
        "title": "La Isabela y Santo Domingo: El primer cabildo y universidad de América",
        "sections": [
            {
                "type": "text",
                "title": "Narración historiográfica y régimen discursivo colonial",
                "content": "El análisis de los orígenes coloniales de Santo Domingo en nivel B2 articula oraciones temporales e históricas ('tras ser fundada en 1496 por Bartolomé Colón', 'habiendo sido consagrada como la primera sede episcopal del Nuevo Mundo') y discurso referido sobre los tempranos debates de los derechos humanos encabezados por la orden de los dominicos."
            },
            {
                "type": "table",
                "title": "Términos institucionales primados en América",
                "rows": [
                    ["Primera catedral", "'Catedral Primada de América (Santa María de la Encarnación), iniciada en 1512'"],
                    ["Primera universidad", "'Universidad Santo Tomás de Aquino, fundada mediante bula papal en 1538'"],
                    ["Primera corte virreinal", "'La Real Audiencia de Santo Domingo, primer tribunal de apelaciones de las Indias'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en crónicas del siglo XVI",
                "items": [
                    {"spanish": "En diciembre de 1511, fray Antón de Montesinos pronunció el célebre sermón de adviento en defensa de los indígenas taínos.", "english": "In December 1511, Friar Antón de Montesinos delivered the celebrated Advent sermon in defense of the Taíno people."},
                    {"spanish": "El Alcázar de Colón, residencia del virrey Diego Colón, fue edificado con piedra caliza coralina extraída de las canteras locales.", "english": "The Alcázar de Colón, residence of Viceroy Diego Colón, was built with coralline limestone extracted from local quarries."},
                    {"spanish": "Fray Bartolomé de las Casas escuchó conmovido aquel sermón dominico y dedicó el resto de su vida a combatir la encomienda.", "english": "Friar Bartolomé de las Casas listened moved to that Dominican sermon and devoted the rest of his life to fighting the encomienda."}
                ]
            },
            {
                "type": "tip",
                "content": "Al aludir a las instituciones coloniales tempranas de Santo Domingo, se utiliza habitualmente el adjetivo femenino 'primada' para denotar su condición de pionera en el continente americano ('la catedral primada', 'la ciudad primada')."
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
                    ["el cabildo", "town council, chapterhouse"],
                    ["la primada", "first/primate institution"],
                    ["el alcázar", "fortified palace, alcazar"],
                    ["la encomienda", "colonial labor tribute system"]
                ],
                "teaches": ["b2-dominicana-vocab"]
            },
            {
                "id": f"{lc2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué trascendencia histórica tuvo el sermón de adviento de fray Antón de Montesinos en Santo Domingo en 1511?",
                "options": [
                    "Constituyó el primer clamor público institucional en defensa de la dignidad humana y los derechos de los pueblos indígenas.",
                    "Fue una proclama militar que declaró la guerra a las comunidades taínas de la cordillera Central.",
                    "Fue un decreto comercial que autorizó la libre exportación de café y tabaco hacia los puertos europeos."
                ],
                "correct": 0,
                "teaches": ["dominicana-santo-domingo-primada-america"]
            },
            {
                "id": f"{lc2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La ciudad de Santo Domingo __ el título de Primada de América por haber albergado la primera catedral, universidad y corte virreinal. (ostentar - presente indicativo)",
                "answer": "ostenta",
                "english": "The city of Santo Domingo holds the title of Primate of America for having housed the first cathedral, university, and viceregal court.",
                "teaches": ["dominicana-santo-domingo-primada-america"]
            },
            {
                "id": f"{lc2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Santo", "Domingo", "albergó", "el", "primer", "cabildo", "español", "de", "América."],
                "solution": ["Santo", "Domingo", "albergó", "el", "primer", "cabildo", "español", "de", "América."],
                "english": "Santo Domingo housed the first Spanish town council in America.",
                "teaches": ["dominicana-santo-domingo-primada-america"]
            },
            {
                "id": f"{lc2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Cómo influyó el sermón de Montesinos en la trayectoria de Bartolomé de las Casas?"},
                    {"speaker": "Profesora", "text": "_____"},
                    {"speaker": "Historiador", "text": "Un hito fundacional del pensamiento humanista moderno nacido en el Caribe."}
                ],
                "options": [
                    "Despertó su conciencia ética, llevándolo a renunciar a sus encomiendas y a convertirse en el gran cronista y defensor de los indígenas.",
                    "Lo motivó a fundar una compañía naviera de vapores mercantes entre La Española y las Antillas Menores.",
                    "Lo convenció de redactar los primeros manuales de contabilidad agrícola para los ingenios de azúcar."
                ],
                "correct": 0,
                "teaches": ["dominicana-santo-domingo-primada-america"]
            },
            {
                "id": f"{lc2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El sermón de Montesinos denunció la tiranía ejercida contra los indígenas taínos.",
                "english": "Montesinos' sermon denounced the tyranny exercised against the Taíno people.",
                "teaches": ["dominicana-santo-domingo-primada-america"]
            }
        ]
    })

    # Regional Story 2: b2-dominicana-02.json
    story_dom_02 = {
        "id": "b2-dominicana-02",
        "title": "La Isabela y Santo Domingo: El primer cabildo y universidad de América",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica histórica de nivel B2 sobre la génesis del dominio colonial europeo en el Nuevo Mundo: las ruinas de La Isabela, la fundación de Santo Domingo como Ciudad Primada y el sermón de Montesinos.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "La historia moderna del hemisferio americano como confluencia entre civilizaciones tiene su punto de partida en las costas septentrionales de La Española. Tras el naufragio de la Santa María en 1492 y la destrucción del fuerte de La Navidad levantado con sus maderos, Cristóbal Colón regresó a fines de 1493 al frente de diecisiete navíos y mil quinientos colonos para fundar La Isabela, en Puerto Plata. Concebida como factoría comercial fortificada, la primera villa europea edificada en el Nuevo Mundo resultó efímera: azotada por fiebres tropicales, huracanes y rebeliones de hombres desesperados que no hallaban el oro prometido, sus ruinas de piedra caliza permanecen hoy como testimonio de aquel accidentado ensayo fundacional."
            },
            {
                "type": "narration",
                "text": "Comprendiendo la inviabilidad logística de La Isabela, Bartolomé Colón, hermano del almirante, trasladó la capital hacia la costa sur de la isla, fundando en 1496 en la margen oriental del río Ozama la ciudad de Santo Domingo de Guzmán, el asentamiento urbano europeo más antiguo de América que ha permanecido habitado de manera ininterrumpida hasta nuestros días. Tras ser arrasada por un feroz ciclón tropical en 1502, el nuevo gobernador fray Nicolás de Ovando decidió refundarla en la margen occidental del río, trazando una cuadrícula geométrica regular de calles rectas y manzanas amplias que serviría como prototipo urbanístico para cientos de fundaciones coloniales desde México hasta el Río de la Plata."
            },
            {
                "type": "narration",
                "text": "Bajo el mandato de Ovando y la posterior llegada en 1509 del virrey don Diego Colón, Santo Domingo floreció como el epicentro político y eclesiástico de la expansión hispana en el continente. La Zona Colonial, declarada Patrimonio de la Humanidad por la UNESCO en 1990, atesora las instituciones 'primadas' del Nuevo Mundo: la primera corte virreinal en el Alcázar de Colón con su arquería gótica y mudéjar; el primer hospital (San Nicolás de Bari, 1503); la fortaleza Ozama con su torre del Homenaje; y la Catedral Primada de América, cuya fachada renacentista tardó décadas en construirse."
            },
            {
                "type": "narration",
                "text": "Asimismo, la ciudad se erigió tempranamente en el faro intelectual de las Indias con la fundación de la Universidad Santo Tomás de Aquino en 1538, autorizada por la bula papal 'In Apostolatus Culmine' del papa Paulo III en el convento de los dominicos. En sus aulas de teología, cánones y filosofía se formaron los primeros letrados y obispos que luego difundirían el pensamiento escolástico y renacentista por todo el continente, consolidando la vocación universitaria pionera de la capital dominicana casi un siglo antes de que se inaugurara la Universidad de Harvard en las colonias anglosajonas del norte."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el hito más universal y conmovedor que Santo Domingo legó a la historia de la civilización se produjo el cuarto domingo de adviento de 1511 bajo el techo de paja del primitivo templo de la orden de los dominicos. Subiendo al púlpito ante las máximas autoridades virreinales congregadas, entre las que figuraba el propio virrey Diego Colón y los hacendados más opulentos de la colonia, fray Antón de Montesinos pronunció en nombre de su comunidad un sermón que sacudió los cimientos del imperio: 'Decid, ¿con qué derecho y con qué justicia tenéis en tan cruel y horrible servidumbre aquestos indios? ¿Con qué autoridad habéis hecho tan detestables guerras a estas gentes que estaban en sus tierras mansas y pacíficas? ¿Estos, no son hombres? ¿No tienen ánimas racionales? ¿No sois obligados a amallos como a vosotros mismos?'."
            },
            {
                "type": "narration",
                "text": "Aquel grito profético en defensa de los pueblos originarios taínos, diezmados por el sistema de encomiendas y el trabajo forzado en los lavaderos de oro, representó la primera denuncia pública institucional de la dignidad humana y los derechos naturales en la historia moderna de Occidente. Entre los feligreses que escucharon atónitos la recriminación de Montesinos se encontraba un joven encomendero español llamado Bartolomé de las Casas. La interpelación caló de manera tan profunda en su conciencia que años más tarde renunció a sus tierras e indígenas, tomó los hábitos sacerdotales y consagró el resto de su longeva vida a viajar incansablemente entre América y la corte imperial para defender la causa indígena, inspirando la promulgación de las históricas Leyes Nuevas de 1542."
            },
            {
                "type": "narration",
                "text": "De este modo, Santo Domingo se proyecta en la memoria universal no solo como la cuna de la arquitectura de piedra coralina y de los primeros cabildos municipales del continente, sino ante todo como el escenario donde germinó la primera gran batalla ética por la universalidad de los derechos humanos. Caminar hoy por las calles empedradas de Las Damas o El Conde supone pisar la encrucijada primordial donde Europa conoció la grandeza y la tragedia de su propio destino en el Nuevo Mundo."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué fracasó el asentamiento inicial de La Isabela fundado por Colón en 1493?",
                        "options": [
                            "Debido a epidemias de fiebres tropicales, huracanes devastadores y rebeliones por la escasez de oro fácil.",
                            "Por un ataque coordinado de la armada naval de la corona francesa en el mar Caribe.",
                            "Por la falta de madera adecuada para construir viviendas y almacenes de almacenamiento.",
                            "Porque el rey Fernando ordenó la evacuación inmediata de todos los colonos hacia Jamaica."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 relata que La Isabela sucumbió ante enfermedades tropicales, tempestades y rebeliones de colonos decepcionados."
                    },
                    {
                        "question": "¿Qué innovación urbanística introdujo fray Nicolás de Ovando al refundar Santo Domingo en 1502?",
                        "options": [
                            "Una cuadrícula regular de calles rectas y manzanas amplias que sirvió de modelo en toda Hispanoamérica.",
                            "Un sistema concéntrico de murallas circulares copiado de las fortalezas medievales alemanas.",
                            "La edificación de canales navegables que sustituyeron por completo las calles para peatones.",
                            "La prohibición de utilizar piedra coralina en la construcción de edificios administrativos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 describe el trazado en cuadrícula ortogonal de Ovando como el prototipo urbanístico adoptado en el resto del continente."
                    },
                    {
                        "question": "¿Qué trascendental impacto personal tuvo el sermón de adviento de Montesinos sobre Bartolomé de las Casas?",
                        "options": [
                            "Lo llevó a renunciar a sus encomiendas, ordenarse fraile y consagrar su vida a la defensa de los derechos indígenas.",
                            "Lo impulsó a armar una milicia privada para capturar a los líderes rebeldes en las serranías.",
                            "Lo convenció de regresar a España para dedicarse al comercio de paños en la ciudad de Sevilla.",
                            "Lo motivó a escribir manuales de minería de oro para los banqueros de Augsburgo."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 detalla cómo la prédica de Montesinos transformó la conciencia de Las Casas, convirtiéndolo en el gran defensor universal de los pueblos originarios."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc2}.json", story_dom_02)

    write_json(f"lessons/b2/{lc2}.json", make_lesson(
        stem=lc2,
        unit_num=11,
        title="La Isabela y Santo Domingo: El primer cabildo y universidad de América",
        goal="Examine the early colonial foundations of Santo Domingo, the viceregal court, and Montesinos' 1511 human rights sermon using historical narrative registers.",
        grammar_desc="narrativa historiográfica colonial, adjetivación institucional primada y discurso sobre derechos tempranos",
        grammar_ref=f"grammar/b2/{lc2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc2}-voc.json",
        ex_ref=f"exercises/b2/{lc2}-ex.json",
        ex_ids=[f"{lc2}.ex01", f"{lc2}.ex02", f"{lc2}.ex03", f"{lc2}.ex04", f"{lc2}.ex05", f"{lc2}.ex06"],
        goals=[
            "Trace the urban and institutional origins of Santo Domingo as Ciudad Primada.",
            "Analyze the ethical and philosophical impact of Friar Antón de Montesinos' 1511 sermon.",
            "Deploy colonial institutions vocabulary (cabildo, primada, alcázar, encomienda, bula)."
        ],
        story_ref=f"stories/world/b2/{lc2}.json"
    ))

    # Lesson 3: b2-dominicana-03 - El merengue y la bachata: De la marginación a patrimonio de la humanidad
    lc3 = "b2-dominicana-03"
    write_json(f"vocabulary/b2/{lc3}-voc.json", {
        "id": "vocab.b2.dominicana.03",
        "lesson": lc3,
        "title": "Música patrimonial dominicana: merengue típico y bachata de amargue",
        "theme": "Vocabulario de organología antillana, compás sincopado y evolución musical",
        "words": [
            {"lemma": "la güira", "translation": "guira (metal scraper)", "pos": "noun"},
            {"lemma": "la tambora", "translation": "tambora (two-headed drum)", "pos": "noun"},
            {"lemma": "el amargue", "translation": "bitterness, lovesickness (bachata theme)", "pos": "noun"},
            {"lemma": "el perico ripiao", "translation": "traditional rural merengue trio/style", "pos": "noun"},
            {"lemma": "el estribillo", "translation": "chorus, refrain", "pos": "noun"},
            {"lemma": "el requinto", "translation": "lead guitar in bachata, smaller acoustic guitar", "pos": "noun"},
            {"lemma": "folclórico", "translation": "folkloric, folk", "pos": "adjective"},
            {"lemma": "la cadencia", "translation": "cadence, rhythmic flow", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{lc3}-a-gr.json", {
        "id": "grammar.b2.dominicana.03.merengue-bachata",
        "title": "El merengue y la bachata: De la marginación a patrimonio de la humanidad",
        "sections": [
            {
                "type": "text",
                "title": "Crítica musicológica y evolución sociocultural",
                "content": "El análisis de las tradiciones musicales dominicanas en nivel B2 moviliza estructuras de valoración estética y evolución social ('si bien durante décadas la bachata fue estigmatizada como música marginal de cabaret', 'resulta revelador que la instrumentación del merengue típico condense el mestizaje triétnico antillano: la güira taína, la tambora africana y el acordeón europeo')."
            },
            {
                "type": "table",
                "title": "Organología y tríada fundacional del merengue típico",
                "rows": [
                    ["Güira metálica", "Herencia taína: raspador de metal que dicta el compás vertiginoso"],
                    ["Tambora bimembranófona", "Herencia africana: tambor de madera con cuero de chivo percutido con mazo"],
                    ["Acordeón diatónico", "Herencia europea: instrumento melódico incorporado a fines del siglo XIX"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en ensayos musicológicos",
                "items": [
                    {"spanish": "Juan Luis Guerra revolucionó el merengue y la bachata al fusionarlos con el jazz, la salsa y la lírica poética culta.", "english": "Juan Luis Guerra revolutionized merengue and bachata by fusing them with jazz, salsa, and educated poetic lyrics."},
                    {"spanish": "La UNESCO declaró tanto el merengue (2016) como la bachata (2019) Patrimonio Cultural Inmaterial de la Humanidad.", "english": "UNESCO declared both merengue (2016) and bachata (2019) Intangible Cultural Heritage of Humanity."},
                    {"spanish": "El punteo metálico del requinto en la bachata expresa el desconsuelo amoroso con una intensidad inconfundible.", "english": "The metallic plucking of the requinto in bachata expresses romantic heartbreak with unmistakable intensity."}
                ]
            },
            {
                "type": "tip",
                "content": "Para describir géneros musicales tradicionales, recurre a términos técnicos de ritmo y forma: 'compás binario sincopado', 'diálogo de llamada y respuesta', 'bordón de guitarra', 'patrón percusivo'."
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
                    ["la güira", "metal scraper (guira)"],
                    ["la tambora", "two-headed drum (tambora)"],
                    ["el amargue", "lovesickness, romantic bitterness"],
                    ["el perico ripiao", "traditional rural merengue style"]
                ],
                "teaches": ["b2-dominicana-vocab"]
            },
            {
                "id": f"{lc3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué tríada instrumental tradicional personifica la síntesis cultural del merengue típico dominicano?",
                "options": [
                    "La güira metálica aborigen, la tambora africana y el acordeón diatónico europeo.",
                    "El violín clásico, el piano de cola y las castañuelas andaluzas de madera.",
                    "La flauta de pan andina, el charango indígena y el arpa llanera."
                ],
                "correct": 0,
                "teaches": ["dominicana-merengue-bachata-patrimonio"]
            },
            {
                "id": f"{lc3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La bachata pasó de los suburbios marginados a los escenarios mundiales gracias a compositores que __ su lírica y orquestación. (refinar - pretérito indefinido)",
                "answer": "refinaron",
                "english": "Bachata moved from marginalized suburbs to world stages thanks to composers who refined its lyrics and orchestration.",
                "teaches": ["dominicana-merengue-bachata-patrimonio"]
            },
            {
                "id": f"{lc3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "merengue", "y", "la", "bachata", "son", "patrimonio", "de", "la", "humanidad."],
                "solution": ["El", "merengue", "y", "la", "bachata", "son", "patrimonio", "de", "la", "humanidad."],
                "english": "Merengue and bachata are intangible heritage of humanity.",
                "teaches": ["dominicana-merengue-bachata-patrimonio"]
            },
            {
                "id": f"{lc3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Musicólogo", "text": "¿Por qué fue tan crucial el álbum 'Bachata Rosa' de Juan Luis Guerra en 1990?"},
                    {"speaker": "Crítica musical", "text": "_____"},
                    {"speaker": "Musicólogo", "text": "Fue la consagración definitiva de un género que hasta entonces era despreciado por las élites."}
                ],
                "options": [
                    "Despojó al género de prejuicios sociales al vestir el sentimiento popular del amargue con refinadas armonías de jazz y poesía universal.",
                    "Sustituyó los instrumentos de percusión acústica por sintetizadores digitales japoneses.",
                    "Fue grabado exclusivamente para ser transmitido en programas infantiles matutinos."
                ],
                "correct": 0,
                "teaches": ["dominicana-merengue-bachata-patrimonio"]
            },
            {
                "id": f"{lc3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La tambora y la güira marcan el compás acelerado del merengue típico.",
                "english": "The tambora and the guira mark the accelerated tempo of typical merengue.",
                "teaches": ["dominicana-merengue-bachata-patrimonio"]
            }
        ]
    })

    # Regional Story 3: b2-dominicana-03.json
    story_dom_03 = {
        "id": "b2-dominicana-03",
        "title": "El merengue y la bachata: De la marginación a patrimonio de la humanidad",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica musical sobre los dos géneros identitarios de la República Dominicana: el merengue y la bachata. Su génesis campesina y suburbana, su organología mestiza y su consagración global como Patrimonio Inmaterial de la UNESCO.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Pocos fenómenos culturales expresan con tanta fidelidad el alma, las vicisitudes históricas y la inagotable alegría de vivir del pueblo dominicano como su música popular bailable, encarnada de manera señera en dos géneros de resonancia planetaria: el merengue y la bachata. Aunque hoy en día ambos estilos son celebrados en los festivales más encumbrados del orbe y ostentan el reconocimiento de la UNESCO como Patrimonio Cultural Inmaterial de la Humanidad —el merengue consagrado en 2016 y la bachata en 2019—, sus trayectorias históricas estuvieron marcadas durante largo tiempo por la estigmatización moral de las élites letradas, que los relegaban con desdén a la condición de expresiones rústicas o vulgares propias de las clases desposeídas."
            },
            {
                "type": "narration",
                "text": "Nacido a mediados del siglo XIX en los campos fértiles del valle del Cibao, en la región septentrional de la isla, el merengue típico o 'perico ripiao' constituye un prodigio antropológico de síntesis triétnica. Su estructura instrumental condensa de modo deslumbrante las tres vertientes fundamentales que forjaron la identidad nacional quisqueyana: la güira metálica de superficie raspada, herencia directa de los raspadores de calabaza aborígenes taínos; la tambora bimembranófona de madera de roble o corazón de pino, revestida con parches de cuero de chivo y percutida con mazo y mano desnuda, aporte rítmico inconfundible de los africanos esclavizados; y el acordeón diatónico de botones, incorporado por comerciantes alemanes a fines del siglo XIX para aportar la armonía melódica europea."
            },
            {
                "type": "narration",
                "text": "Durante la prolongada y sangrienta dictadura de Rafael Leónidas Trujillo (1930-1961), el merengue experimentó una manipulación política decisiva. El tirano, oriundo de un estrato campesino modesto de San Cristóbal, impuso el merengue como música nacional obligatoria en los salones aristocráticos que antaño le cerraban las puertas, obligando a las orquestas de salón a componer cientos de piezas laudatorias que glorificaban su régimen megalómano. Tras la caída de la tiranía, pioneros legendarios como Joseíto Mateo, Johnny Ventura —el 'Caballo Mayor'— y Wilfrido Vargas aceleraron el tempo del ritmo, introdujeron secciones de metales vibrantes con saxofones y trompetas virtuosas e incorporaron coreografías electrizantes, convirtiendo al merengue en un huracán bailable que dominó las pistas de toda América Latina y el Caribe en los años setenta y ochenta."
            },
            {
                "type": "narration",
                "text": "Por su parte, la bachata recorrió un sendero de redención social aún más tortuoso y dramático. Emergida a principios de los años sesenta en los arrabales marginales de Santo Domingo y en los cafetines de prostitución y juego de las zonas rurales, esta expresión musical nació de la lenta desaceleración del bolero campesino, enriquecido con la síncopa de las maracas y el bongó y el tañido lastimero de la guitarra española. Conocida inicialmente de manera despectiva como 'música de guardia' o 'música de amargue', sus letras desgarradas hablaban sin tapujos de la traición conyugal, el abandono amoroso, el desamparo económico y la embriaguez desesperada, lo que motivó que la burguesía urbana y las emisoras de radio comerciales prohibieran su difusión durante décadas por considerarla procaz e inmoral."
            },
            {
                "type": "narration",
                "text": "Pese a la censura institucional implacable, la bachata pervivió con fuerza indomable en las cantinas populares, donde cantantes pioneros como José Manuel Calderón, Luis Segura y Leonardo Paniagua grababan discos independientes de escaso presupuesto que se vendían de mano en mano entre los sectores obreros. La sonoridad distintiva del género descansaba sobre el punteo metálico agudo y virtuoso del 'requinto', una guitarra acústica templada para obtener notas brillantes que dialogaba en un contrapunto desgarrador con la voz quejumbrosa del intérprete."
            },
            {
                "type": "narration",
                "text": "La metamorfosis definitiva de la bachata hacia la consagración universal se produjo en 1990 con el lanzamiento de 'Bachata Rosa', el álbum cumbre de Juan Luis Guerra y su agrupación 4.40. El compositor dominicano, formado en el prestigioso Berklee College of Music de Boston, vistió el sentimiento popular del amargue con refinadas armonías de jazz, letras de deslumbrante vuelo poético inspiradas en Pablo Neruda y una producción acústica impecable, vendiendo millones de copias en los cinco continentes y abriendo las puertas para que nuevas figuras como Antony Santos, Luis Vargas y, posteriormente, el grupo Aventura y Romeo Santos transformaran la bachata en un fenómeno global de masas que llena estadios desde Tokio hasta Nueva York."
            },
            {
                "type": "narration",
                "text": "Hoy en día, el merengue y la bachata constituyen mucho más que dos géneros de entretenimiento bailable: representan los latidos sonoros gemelos de una nación caribeña que ha sabido convertir el dolor de sus heridas históricas y las penurias de su cotidianidad en un manantial inagotable de belleza, poesía y cadencia rítmica, ofreciendo al mundo una lección magistral de cómo la cultura de los humildes puede trascender cualquier marginación para convertirse en patrimonio imperecedero de la humanidad entera."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué tres raíces étnicas y culturales están representadas en los instrumentos del merengue típico dominicano?",
                        "options": [
                            "La taína en la güira, la africana en la tambora y la europea en el acordeón.",
                            "La maya en el tamboril, la hispana en la guitarra y la árabe en el laúd.",
                            "La incaica en la quena, la portuguesa en el cavaquinho y la caribeña en las maracas.",
                            "La francesa en el clarinete, la holandesa en el violín y la africana en el yembé."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que la güira aborigen, la tambora africana y el acordeón europeo sintetizan la herencia triétnica dominicana."
                    },
                    {
                        "question": "¿Por qué la bachata fue marginada y censurada por las emisoras comerciales durante sus primeras décadas?",
                        "options": [
                            "Porque se asociaba con arrabales, cafetines y temáticas de amargue consideradas vulgares por las élites.",
                            "Porque utilizaba exclusivamente letras en lenguas africanas que las autoridades no comprendían.",
                            "Porque estaba prohibido el uso de guitarras de cuerda metálica en los espectáculos públicos.",
                            "Porque era un ritmo exclusivo de las ceremonias fúnebres de la alta jerarquía eclesiástica."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 expone que la bachata fue estigmatizada como música de cabaret y arrabal por sus letras desgarradas sobre desengaño y pobreza."
                    },
                    {
                        "question": "¿Qué hito musical marcó la aceptación y consagración internacional de la bachata en 1990?",
                        "options": [
                            "El álbum 'Bachata Rosa' de Juan Luis Guerra, que fusionó el género con jazz y alta poesía.",
                            "La victoria de una orquesta dominicana en el festival de música folclórica de Viena.",
                            "La inclusión obligatoria de la bachata en los manuales de educación secundaria de la capital.",
                            "La prohibición legal del merengue en las estaciones de radio de Santo Domingo."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 destaca que 'Bachata Rosa' de Juan Luis Guerra dotó al género de refinamiento lírico y jazzístico, logrando éxito mundial."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc3}.json", story_dom_03)

    write_json(f"lessons/b2/{lc3}.json", make_lesson(
        stem=lc3,
        unit_num=11,
        title="El merengue y la bachata: De la marginación a patrimonio de la humanidad",
        goal="Analyze the organology, social evolution, and global prestige of merengue and bachata using musicological criticism and cultural history registers.",
        grammar_desc="crítica musicológica, oraciones concesivas de evolución social y terminología rítmica caribeña",
        grammar_ref=f"grammar/b2/{lc3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc3}-voc.json",
        ex_ref=f"exercises/b2/{lc3}-ex.json",
        ex_ids=[f"{lc3}.ex01", f"{lc3}.ex02", f"{lc3}.ex03", f"{lc3}.ex04", f"{lc3}.ex05", f"{lc3}.ex06"],
        goals=[
            "Explain the tri-ethnic instrumentation of typical merengue (güira, tambora, accordion).",
            "Trace the social trajectory of bachata from marginalized brothels to UNESCO recognition.",
            "Deploy musicological and cultural vocabulary (güira, tambora, amargue, perico ripiao, requinto)."
        ],
        story_ref=f"stories/world/b2/{lc3}.json"
    ))

    # Lesson 4: b2-dominicana-04 - La frontera con Haití: Historia compartida, desencuentros y migración
    lc4 = "b2-dominicana-04"
    write_json(f"vocabulary/b2/{lc4}-voc.json", {
        "id": "vocab.b2.dominicana.04",
        "lesson": lc4,
        "title": "Frontera domínico-haitiana, bateyes y convivencia insular",
        "theme": "Vocabulario de dinámicas fronterizas, industria azucarera y binacionalidad",
        "words": [
            {"lemma": "el batey", "translation": "sugar cane worker settlement, batey", "pos": "noun"},
            {"lemma": "el bracero", "translation": "agricultural day laborer, cane cutter", "pos": "noun"},
            {"lemma": "la demarcación", "translation": "demarcation, boundary line", "pos": "noun"},
            {"lemma": "el mercado binacional", "translation": "binational market (Dajabón/Jimaní)", "pos": "noun"},
            {"lemma": "la convivencia", "translation": "coexistence, living together", "pos": "noun"},
            {"lemma": "el jornalero", "translation": "day laborer, field hand", "pos": "noun"},
            {"lemma": "la zafra", "translation": "sugar cane harvest", "pos": "noun"},
            {"lemma": "interdependiente", "translation": "interdependent", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{lc4}-a-gr.json", {
        "id": "grammar.b2.dominicana.04.frontera-haiti",
        "title": "La frontera con Haití: Historia compartida, desencuentros y migración",
        "sections": [
            {
                "type": "text",
                "title": "Discurso sobre geopolítica fronteriza y sociología migratoria",
                "content": "El análisis de la frontera insular entre la República Dominicana y Haití en nivel B2 requiere estructurar debates sobre interdependencia económica, memoria histórica y derechos laborales mediante períodos concesivos ('si bien las tensiones políticas han sido recurrentes', 'a pesar de las diferencias lingüísticas e históricas') y fórmulas de equilibrio causal."
            },
            {
                "type": "table",
                "title": "Conceptos clave de la realidad fronteriza insular",
                "rows": [
                    ["Tratado de Aranjuez (1777)", "División colonial formal entre la parte francesa (Saint-Domingue) y la española"],
                    ["Los bateyes azucareros", "Asentamientos de trabajadores cañeros donde conviven generaciones de origen haitiano"],
                    ["Mercados binacionales", "Intercambio comercial vital en pasos fronterizos como Dajabón, Elías Piña y Jimaní"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en estudios sociológicos de la frontera",
                "items": [
                    {"spanish": "El mercado binacional de Dajabón congrega dos veces por semana a miles de comerciantes dominicanos y haitianos.", "english": "The Dajabón binational market gathers thousands of Dominican and Haitian traders twice a week."},
                    {"spanish": "La industria de la construcción y la agricultura dominicanas dependen en gran medida de la mano de obra migrante.", "english": "The Dominican construction industry and agriculture rely heavily on migrant labor."},
                    {"spanish": "A pesar de las discrepancias diplomáticas, ambos pueblos comparten un territorio insular ecológicamente interdependiente.", "english": "Despite diplomatic disagreements, both nations share an ecologically interdependent island territory."}
                ]
            },
            {
                "type": "tip",
                "content": "Para abordar temas sensibles de migración e historia fronteriza con el rigor del nivel B2, evita generalizaciones valorativas y emplea conceptos analíticos precisos: 'asimetría económica', 'flujo migratorio laboral', 'estatus migratorio regular', 'cooperación transfronteriza'."
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
                    ["el batey", "sugar cane worker settlement"],
                    ["el bracero", "cane cutter, agricultural day laborer"],
                    ["la demarcación", "demarcation, boundary line"],
                    ["interdependiente", "interdependent"]
                ],
                "teaches": ["b2-dominicana-vocab"]
            },
            {
                "id": f"{lc4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función económica cumplen los mercados binacionales fronterizos como el de Dajabón?",
                "options": [
                    "Canalizan el intercambio comercial formal e informal de alimentos y manufacturas entre ambas poblaciones insulares.",
                    "Son recintos militares exclusivos para el cobro de aranceles sobre el petróleo refinado.",
                    "Son ferias científicas donde se presentan patentes tecnológicas agroindustriales."
                ],
                "correct": 0,
                "teaches": ["dominicana-frontera-haiti-convivencia"]
            },
            {
                "id": f"{lc4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ambos países comparten cuencas hidrográficas que __ una gestión ambiental concertada para evitar la deforestación. (exigir - presente indicativo)",
                "answer": "exigen",
                "english": "Both countries share river basins that require concerted environmental management to prevent deforestation.",
                "teaches": ["dominicana-frontera-haiti-convivencia"]
            },
            {
                "id": f"{lc4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "convivencia", "fronteriza", "requiere", "diálogo", "y", "cooperación", "mutua."],
                "solution": ["La", "convivencia", "fronteriza", "requiere", "diálogo", "y", "cooperación", "mutua."],
                "english": "Border coexistence requires dialogue and mutual cooperation.",
                "teaches": ["dominicana-frontera-haiti-convivencia"]
            },
            {
                "id": f"{lc4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Cómo ha evolucionado la situación de las familias en los bateyes de la caña de azúcar?"},
                    {"speaker": "Defensora de derechos", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Un desafío urgente de justicia social y reconocimiento civil."}
                ],
                "options": [
                    "Si bien el declive de la industria azucarera redujo la zafra tradicional, miles de descendientes nacidos en la isla demandan documentación y acceso a la seguridad social.",
                    "Los ingenios de caña utilizan exclusivamente molinos de viento traídos de los Países Bajos.",
                    "El precio del azúcar refinada en el mercado internacional se fija en francos suizos."
                ],
                "correct": 0,
                "teaches": ["dominicana-frontera-haiti-convivencia"]
            },
            {
                "id": f"{lc4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El mercado binacional dinamiza la economía de las comunidades fronterizas.",
                "english": "The binational market dynamizes the economy of border communities.",
                "teaches": ["dominicana-frontera-haiti-convivencia"]
            }
        ]
    })

    # Regional Story 4: b2-dominicana-04.json
    story_dom_04 = {
        "id": "b2-dominicana-04",
        "title": "La frontera con Haití: Historia compartida, desencuentros y migración",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociológica de nivel B2 sobre las complejas relaciones domínico-haitianas en la isla de La Española: orígenes de la partición colonial, los trágicos sucesos de 1937, la vida en los bateyes y la interdependencia económica fronteriza.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "La isla de La Española presenta la singularidad geográfica e histórica de ser el único territorio insular del continente americano compartido por dos Estados soberanos independientes: la República Dominicana en su porción oriental y la República de Haití en su tercio occidental. Separadas por una frontera terrestre de casi cuatrocientos kilómetros que serpentea entre montañas agrestes y valles áridos desde la desembocadura del río Dajabón en el norte hasta la costa de Pedernales en el sur, ambas naciones encarnan historias, idiomas, instituciones jurídicas y trayectorias identitarias profundamente divergentes nacidas de las disputas coloniales que enfrentaron a las coronas de España y Francia durante los siglos XVII y XVIII."
            },
            {
                "type": "narration",
                "text": "La partición de la isla se consagró formalmente en el Tratado de Aranjuez de 1777, que delimitó las posesiones entre la colonia española de Santo Domingo y la próspera colonia esclavista francesa de Saint-Domingue. Tras la gloriosa Revolución haitiana de 1804 —la primera república negra libre del planeta y la primera nación en abolir la esclavitud en el Nuevo Mundo—, las tensiones geopolíticas alcanzaron un punto culminante con la ocupación militar haitiana de la parte este entre 1822 y 1844, encabezada por el presidente Jean-Pierre Boyer. Aunque este período abolió formalmente la esclavitud en todo el territorio insular, generó una profunda resistencia entre la población hispanoparlante, que proclamó la independencia dominicana el 27 de febrero de 1844 bajo el liderazgo de Juan Pablo Duarte y la sociedad secreta La Trinitaria."
            },
            {
                "type": "narration",
                "text": "El siglo XX heredó estas heridas históricas, que fueron exacerbadas de manera criminal por la dictadura de Rafael Leónidas Trujillo. En octubre de 1937, obsesionado por un ideario autoritario de 'blanqueamiento' demográfico y afianzamiento violento de la demarcación limítrofe, el régimen trujillista perpetró la infame 'Matanza del Perejil', en la que miles de campesinos y trabajadores haitianos desarmados fueron asesinados por el ejército en la franja fronteriza. La masacre dejó una huella traumática imborrable en la memoria colectiva de ambos pueblos, evidenciando los peligros letales del ultranacionalismo excluyente y la manipulación del odio racial."
            },
            {
                "type": "narration",
                "text": "Paralelamente a estas fricciones políticas, la economía dominicana desarrolló a lo largo del siglo XX una dependencia estructural de la mano de obra haitiana, concentrada inicialmente en la industria azucarera. A través de convenios bilaterales entre gobiernos, decenas de miles de braceros haitianos fueron reclutados para cortar caña en las plantaciones dominicanas, viviendo en condiciones precarias en los 'bateyes', comunidades rurales aisladas levantadas alrededor de los ingenios azucareros. Con el paso de las décadas, varias generaciones de descendientes nacieron y crecieron en estos bateyes, construyendo una identidad bicultural y enfrentando complejos litigios jurídicos relativos a su reconocimiento civil y derecho a la nacionalidad dominicana."
            },
            {
                "type": "narration",
                "text": "Con el declive paulatino de la zafra azucarera en los años noventa y la profunda inestabilidad política y desastres naturales que asolaron a Haití —incluido el devastador terremoto de 2010—, la inmigración haitiana se diversificó masivamente hacia las ciudades dominicanas, asumiendo un rol protagónico en los sectores de la construcción civil, la agricultura intensiva de banano y hortalizas y el trabajo doméstico y de servicios. Hoy en día, la mano de obra migrante representa un engranaje insustituible para el dinamismo de la economía dominicana, aunque persiste el reto impostergable de garantizar contratos formales, salarios dignos y acceso a la salud pública."
            },
            {
                "type": "narration",
                "text": "En la franja fronteriza, la vida cotidiana desafía con frecuencia los discursos de confrontación política a través de una vibrante dinámica de intercambio comercial y coexistencia pacífica. Los mercados binacionales que funcionan periódicamente en cruces fronterizos clave como Dajabón, Elías Piña y Jimaní congregan a miles de comerciantes de ambos lados que intercambian pacíficamente productos agrícolas, textiles y enseres domésticos, demostrando la interdependencia material ineludible que vincula a las poblaciones locales por encima de cualquier retórica oficial."
            },
            {
                "type": "narration",
                "text": "La República Dominicana y Haití están indisolublemente condenadas a entenderse. Compartiendo una geografía frágil amenazada por huracanes, sequías y la degradación de sus cuencas hidrográficas compartidas como la del río Artibonito, el porvenir de la isla entera depende de la capacidad de ambos pueblos para superar los prejuicios heredados del pasado y forjar una cooperación respetuosa y pragmática fundada en la solidaridad humanitaria, el desarrollo compartido y el respeto inviolable a la soberanía de cada nación."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singularidad política e insular distingue a la isla de La Española en el continente americano?",
                        "options": [
                            "Es la única isla del continente compartida por dos Estados soberanos independientes: República Dominicana y Haití.",
                            "Es la única isla antillana que permanece bajo un régimen de protectorado conjunto de la Unión Europea.",
                            "Es el único territorio marítimo del Caribe donde rige una constitución de federación binacional rotativa.",
                            "Es la única isla caribeña que carece por completo de pasos aduaneros terrestres habilitados."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 señala que La Española es la única isla americana que alberga a dos repúblicas soberanas independientes."
                    },
                    {
                        "question": "¿Qué trágico acontecimiento represivo ordenado por Trujillo en 1937 enlutó la historia fronteriza domínico-haitiana?",
                        "options": [
                            "La masacre masiva de miles de campesinos y trabajadores haitianos conocida como la Matanza del Perejil.",
                            "El bombardeo aéreo naval de los almacenes aduaneros en el puerto de cabo Haitiano.",
                            "La expulsión forzosa de los miembros de las órdenes religiosas de las misiones fronterizas.",
                            "La confiscación militar de todas las cosechas de caña de azúcar en la provincia de Dajabón."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 describe la 'Matanza del Perejil' de 1937 perpetrada por el ejército trujillista contra la población haitiana indefensa."
                    },
                    {
                        "question": "¿Cómo se manifiesta la interdependencia cotidiana pacífica entre ambas naciones en la franja fronteriza?",
                        "options": [
                            "A través de mercados binacionales periódicos como el de Dajabón donde comerciantes de ambos lados intercambian bienes.",
                            "Mediante la adopción de una moneda binacional única emitida por un banco central conjunto.",
                            "A través de elecciones legislativas simultáneas administradas por comisiones mixtas de cascos azules.",
                            "Mediante la construcción de un oleoducto conjunto que transporta combustible refinado hacia el norte."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 relata que en los mercados binacionales de Dajabón y Jimaní las poblaciones de ambos países conviven e intercambian mercancías pacíficamente."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc4}.json", story_dom_04)

    write_json(f"lessons/b2/{lc4}.json", make_lesson(
        stem=lc4,
        unit_num=11,
        title="La frontera con Haití: Historia compartida, desencuentros y migración",
        goal="Analyze border dynamics, shared island ecology, sugar cane bateyes, and binational markets between the Dominican Republic and Haiti with sociological objectivity.",
        grammar_desc="discurso analítico fronterizo, períodos concesivos sobre migración y léxico de binacionalidad",
        grammar_ref=f"grammar/b2/{lc4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc4}-voc.json",
        ex_ref=f"exercises/b2/{lc4}-ex.json",
        ex_ids=[f"{lc4}.ex01", f"{lc4}.ex02", f"{lc4}.ex03", f"{lc4}.ex04", f"{lc4}.ex05", f"{lc4}.ex06"],
        goals=[
            "Trace the historical roots of the border partition and the 1937 events.",
            "Analyze the socioeconomic conditions of Haitian cane cutters in the bateyes.",
            "Deploy border sociology vocabulary (batey, bracero, demarcación, mercado binacional, convivencia)."
        ],
        story_ref=f"stories/world/b2/{lc4}.json"
    ))

    # Lesson 5: b2-dominicana-05 - Béisbol, turismo y el puente diaspórico con Nueva York
    lc5 = "b2-dominicana-05"
    write_json(f"vocabulary/b2/{lc5}-voc.json", {
        "id": "vocab.b2.dominicana.05",
        "lesson": lc5,
        "title": "Béisbol profesional, economía turística y el nexo con Nueva York",
        "theme": "Vocabulario de Grandes Ligas, remesas diaspóricas y transnacionalismo",
        "words": [
            {"lemma": "el pelotero", "translation": "baseball player", "pos": "noun"},
            {"lemma": "el prospecto", "translation": "baseball prospect, scouted talent", "pos": "noun"},
            {"lemma": "la remesa", "translation": "remittance", "pos": "noun"},
            {"lemma": "el cuadrangular", "translation": "home run (béisbol)", "pos": "noun"},
            {"lemma": "la academia", "translation": "training academy", "pos": "noun"},
            {"lemma": "el enclave", "translation": "enclave, resort hub", "pos": "noun"},
            {"lemma": "la transnacionalidad", "translation": "transnationality", "pos": "noun"},
            {"lemma": "el retorno", "translation": "return, homecoming", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{lc5}-a-gr.json", {
        "id": "grammar.b2.dominicana.05.beisbol-diaspora",
        "title": "Béisbol, turismo y el puente diaspórico con Nueva York",
        "sections": [
            {
                "type": "text",
                "title": "Análisis sociológico de la transnacionalidad y el deporte global",
                "content": "El examen de la diáspora dominicana y el fenómeno deportivo en nivel B2 requiere estructurar oraciones que conecten identidades biculturales ('el puente humano y financiero tendido entre Quisqueya y Washington Heights'), balances económicos ('si bien las remesas representan el segundo rubro de divisas') e hipótesis sobre movilidad social ('de no existir las academias de Grandes Ligas...')."
            },
            {
                "type": "table",
                "title": "Pilares de la proyección contemporánea dominicana",
                "rows": [
                    ["Cantera de béisbol", "San Pedro de Macorís, cuna mundial de peloteros de Grandes Ligas (MLB)"],
                    ["Puente transnacional", "Más de dos millones de dominicanos en EE. UU., concentrados en Nueva York"],
                    ["Motor turístico", "Enclaves de Punta Cana, Puerto Plata y Bayahíbe como receptores masivos de divisas"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en sociología cultural contemporánea",
                "items": [
                    {"spanish": "Figuras legendarias como Juan Marichal, Pedro Martínez y David Ortiz alcanzaron la inmortalidad en el Salón de la Fama de Cooperstown.", "english": "Legendary figures such as Juan Marichal, Pedro Martínez, and David Ortiz achieved immortality in Cooperstown's Hall of Fame."},
                    {"spanish": "El barrio de Washington Heights en Manhattan funciona como la segunda capital cultural de la nación dominicana.", "english": "The neighborhood of Washington Heights in Manhattan functions as the second cultural capital of the Dominican nation."},
                    {"spanish": "Las remesas familiares enviadas por la diáspora representan un sostén fundamental para cientos de miles de hogares en la isla.", "english": "Family remittances sent by the diaspora represent a fundamental support for hundreds of thousands of households on the island."}
                ]
            },
            {
                "type": "tip",
                "content": "Al analizar la transnacionalidad dominicana, emplea expresiones sociológicas precisas: 'comunidad desterritorializada', 'flujo circular de capitales', 'bilingüismo aditivo', 'doble ciudadanía'."
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
                    ["el pelotero", "baseball player"],
                    ["el prospecto", "scouted talent, prospect"],
                    ["la remesa", "remittance"],
                    ["el cuadrangular", "home run"]
                ],
                "teaches": ["b2-dominicana-vocab"]
            },
            {
                "id": f"{lc5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué ciudad dominicana es reconocida mundialmente como la mayor cantera de peloteros reclutados por las Grandes Ligas (MLB)?",
                "options": [
                    "San Pedro de Macorís, en la región oriental del país.",
                    "San Fernando de Montecristi, en el extremo noroeste.",
                    "Santa Cruz de Barahona, en la península suroccidental."
                ],
                "correct": 0,
                "teaches": ["dominicana-beisbol-diaspora-nueva-york"]
            },
            {
                "id": f"{lc5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las academias de béisbol instaladas en la isla __ a cientos de jóvenes con el anhelo de firmar un contrato profesional. (formar - presente indicativo)",
                "answer": "forman",
                "english": "The baseball academies established on the island train hundreds of young people with the dream of signing a professional contract.",
                "teaches": ["dominicana-beisbol-diaspora-nueva-york"]
            },
            {
                "id": f"{lc5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "béisbol", "es", "la", "pasión", "nacional", "del", "pueblo", "dominicano."],
                "solution": ["El", "béisbol", "es", "la", "pasión", "nacional", "del", "pueblo", "dominicano."],
                "english": "Baseball is the national passion of the Dominican people.",
                "teaches": ["dominicana-beisbol-diaspora-nueva-york"]
            },
            {
                "id": f"{lc5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Qué rol desempeña la comunidad dominicana de Washington Heights en Nueva York?"},
                    {"speaker": "Antropóloga", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Un auténtico puente transnacional que redefine las fronteras de la identidad quisqueyana."}
                ],
                "options": [
                    "Constituye un enclave diaspórico vibrante donde se preserva el idioma, la gastronomía y la música mientras se nutre la economía insular con remesas.",
                    "Es un centro financiero donde se cotizan exclusivamente acciones de compañías de navegación fluvial.",
                    "Fue una colonia agrícola fundada en el siglo XVIII por cultivadores de trigo holandeses."
                ],
                "correct": 0,
                "teaches": ["dominicana-beisbol-diaspora-nueva-york"]
            },
            {
                "id": f"{lc5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los peloteros dominicanos han conquistado los máximos honores en las Grandes Ligas.",
                "english": "Dominican baseball players have conquered top honors in Major League Baseball.",
                "teaches": ["dominicana-beisbol-diaspora-nueva-york"]
            }
        ]
    })

    # Regional Story 5: b2-dominicana-05.json
    story_dom_05 = {
        "id": "b2-dominicana-05",
        "title": "Béisbol, turismo y el puente diaspórico con Nueva York",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociológica de nivel B2 sobre la proyección transnacional de la República Dominicana: el fervor colectivo por el béisbol, las academias de Grandes Ligas, la expansión turística y el puente identitario con la diáspora en Washington Heights.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Si se pretendiera identificar la institución profana que aglutina con mayor fervor el orgullo colectivo, las aspiraciones de ascenso social y la identidad compartida de los dominicanos de todas las edades y estratos, la respuesta inequívoca sería el béisbol, conocido popularmente en la isla como 'la pelota'. Introducido a finales del siglo XIX por marineros cubanos que huían de las guerras de independencia de su patria y por empresarios azucareros estadounidenses, el juego de bate y guante echó raíces con una fuerza avasalladora en los llanos costeros del este y en el fértil valle del Cibao, desplazando rápidamente a cualquier otra disciplina deportiva hasta convertirse en una auténtica religión civil y en el mayor espectáculo pasional de la República."
            },
            {
                "type": "narration",
                "text": "La primacía dominicana en el béisbol mundial contemporáneo resulta sencillamente apabullante: la República Dominicana es el país extranjero que más peloteros aporta a las Grandes Ligas de los Estados Unidos (Major League Baseball, MLB), superando holgadamente a naciones con poblaciones diez veces mayores. Ciudades legendarias como San Pedro de Macorís, otrora opulenta capital del azúcar de caña en el siglo XIX, se han transformado en la mayor cantera de talento beisbolístico del planeta, de donde surgieron estrellas inmortales de la talla de George Bell, Rico Carty, Sammy Sosa y Robinson Canó. Las treinta franquicias profesionales estadounidenses han edificado en suelo dominicano modernos complejos y academias de desarrollo deportivo donde miles de jóvenes 'prospectos' de catorce a dieciocho años entrenan bajo riguroso régimen técnico y nutricional soñando con firmar contratos millonarios que rescaten a sus familias de la pobreza."
            },
            {
                "type": "narration",
                "text": "La cumbre de esta epopeya deportiva se consagró con la inducción en el prestigioso Salón de la Fama de Cooperstown de héroes legendarios que constituyen leyendas vivas de la patria: el lanzador Juan Marichal en 1983, Pedro Martínez en 2015, Vladimir Guerrero en 2018, David Ortiz ('Big Papi') en 2022 y Adrián Beltré en 2024. Cada exaltación en el templo del béisbol en Nueva York paralizó la vida nacional en la isla, celebrándose con fiestas populares espontáneas en las calles y plazas públicas donde el merengue y las banderas tricolores expresaban la emoción de ver a hijos de humildes aldeas rurales alcanzar la cima del deporte profesional mundial."
            },
            {
                "type": "narration",
                "text": "Paralelamente a esta fábrica de estrellas deportivas, el país experimentó a partir de los años ochenta una vertiginosa reconversión económica que lo catapultó a la vanguardia del turismo en el Caribe. Enclaves paradisíacos como Punta Cana, Bávaro, Bayahíbe y Las Terrenas atrajeron miles de millones de dólares en inversiones hoteleras internacionales, desarrollando un modelo de complejos turísticos de playa que recibe anualmente a más de diez millones de visitantes extranjeros. Esta formidable industria de la hospitalidad se ha transformado en el principal motor de generación de divisas y empleo formal del país, aunque plantea continuos desafíos ambientales en torno a la preservación de los arrecifes de coral y el uso sostenible de los acuíferos subterráneos."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el fenómeno sociológico más profundo que redefine la identidad dominicana contemporánea es su poderosa dimensión diaspórica. Más de dos millones de dominicanos —equivalentes a casi el veinte por ciento de la población insular— residen fuera de su tierra natal, con una concentración colosal en los Estados Unidos, particularmente en el área metropolitana de Nueva York, Boston, Miami y Providence. Enclaves urbanos emblemáticos como Washington Heights en el Alto Manhattan, cariñosamente apodado 'Quisqueya Heights', funcionan como una auténtica extensión desterritorializada de la nación: allí se escuchan los pregones callejeros en castellano caribeño, los colmados abastecen de plátanos y salami criollo y los murales conmemoran tanto a Juan Pablo Duarte como a las estrellas de los Yankees y los Mets."
            },
            {
                "type": "narration",
                "text": "Este puente transnacional genera un flujo continuo y multidireccional de capitales, ideas y afectos de trascendencia económica colosal. Las remesas familiares enviadas por los emigrantes superan los diez mil millones de dólares anuales, representando más del ocho por ciento del producto interno bruto y constituyendo un colchón financiero insustituible para costear la educación, la alimentación y la salud de cientos de miles de hogares en Santo Domingo, Santiago y los pueblos del interior. Al mismo tiempo, la comunidad diaspórica ha conquistado una notable influencia política y cultural en los Estados Unidos, eligiendo concejales, legisladores estatales y congresistas federales que defienden los intereses de su comunidad binacional."
            },
            {
                "type": "narration",
                "text": "Así, la dominicanidad en el siglo XXI se ha transformado en una identidad sin fronteras rígidas, un puente vibrante tendido sobre las aguas del Atlántico donde el bate de los peloteros en los estadios estadounidenses, las remesas que llegan puntuales a los barrios populares y la memoria imperecedera de la tierra amada confluyen en una misma afirmación de orgullo, resiliencia y vocación universal."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué estatus ostenta la República Dominicana en el reclutamiento internacional del béisbol de Grandes Ligas (MLB)?",
                        "options": [
                            "Es el país extranjero que más jugadores aporta al béisbol profesional estadounidense de las Grandes Ligas.",
                            "Es la única nación donde los jugadores extranjeros no pueden firmar contratos de liga menor.",
                            "Es la sede permanente del comité organizador de la Serie Mundial de Béisbol.",
                            "Es el único país del Caribe que carece de academias de entrenamiento para talentos jóvenes."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 subraya que la República Dominicana es el país extranjero que aporta más peloteros a las Grandes Ligas de EE. UU."
                    },
                    {
                        "question": "¿Qué peso económico representan las remesas enviadas por la diáspora dominicana según el texto?",
                        "options": [
                            "Superan los diez mil millones de dólares anuales y representan más del 8% del PIB nacional.",
                            "Apenas alcanzan para financiar las primas de seguros marítimos en el puerto de Santo Domingo.",
                            "Cubren exclusivamente los gastos de viaje de los atletas olímpicos de alto rendimiento.",
                            "Representan menos del uno por ciento de las divisas captadas por el banco central."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 precisa que las remesas superan los diez mil millones de dólares anuales, equivalentes a más del 8% del PIB de la isla."
                    },
                    {
                        "question": "¿Qué barrio neoyorquino es considerado la capital cultural de la diáspora dominicana en los Estados Unidos?",
                        "options": [
                            "Washington Heights en el Alto Manhattan, conocido popularmente como 'Quisqueya Heights'.",
                            "Chinatown en el bajo Manhattan junto al puente de Brooklyn.",
                            "Astoria en el distrito de Queens junto a las orillas del East River.",
                            "Staten Island frente a las terminales portuarias de Nueva Jersey."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 describe a Washington Heights en Manhattan como el corazón transnacional y cultural de la comunidad dominicana en Nueva York."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc5}.json", story_dom_05)

    write_json(f"lessons/b2/{lc5}.json", make_lesson(
        stem=lc5,
        unit_num=11,
        title="Béisbol, turismo y el puente diaspórico con Nueva York",
        goal="Examine Dominican baseball culture, MLB academies, resort tourism, and the transnational diaspora in New York using sociological and economic registers.",
        grammar_desc="sociología de la transnacionalidad, balances económicos de remesas y terminología deportiva del béisbol",
        grammar_ref=f"grammar/b2/{lc5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc5}-voc.json",
        ex_ref=f"exercises/b2/{lc5}-ex.json",
        ex_ids=[f"{lc5}.ex01", f"{lc5}.ex02", f"{lc5}.ex03", f"{lc5}.ex04", f"{lc5}.ex05", f"{lc5}.ex06"],
        goals=[
            "Analyze the sociological phenomenon of Dominican baseball academies and Cooperstown legends.",
            "Evaluate the economic significance of tourism hubs (Punta Cana) and diaspora remittances.",
            "Deploy transnational and sports vocabulary (pelotero, prospecto, remesa, cuadrangular, transnacionalidad)."
        ],
        story_ref=f"stories/world/b2/{lc5}.json"
    ))

    # Consolidation: b2-dominicana-consolidation
    lc_con = "b2-dominicana-consolidation"
    write_json(f"exercises/b2/{lc_con}-ex.json", {
        "lesson": lc_con,
        "exercises": [
            {
                "id": f"{lc_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el cayo", "cay, small sandy island"],
                    ["el cabildo", "town council, chapterhouse"],
                    ["la güira", "metal scraper (guira)"],
                    ["el pelotero", "baseball player"]
                ],
                "teaches": ["b2-dominicana-vocab"]
            },
            {
                "id": f"{lc_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la trascendencia histórica universal de fray Antón de Montesinos y su sermón de 1511 en Santo Domingo?",
                "options": [
                    "Constituyó la primera defensa pública de los derechos humanos y la dignidad de los indígenas en la historia moderna.",
                    "Fue la primera misa solemne oficiada en lengua taína en el continente americano.",
                    "Inauguró la construcción del primer puerto pesquero de altura en las Antillas Mayores."
                ],
                "correct": 0,
                "teaches": ["dominicana-santo-domingo-primada-america"]
            },
            {
                "id": f"{lc_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el merengue típico encarna la síntesis cultural de la nación dominicana?",
                "options": [
                    "Porque su instrumentación tradicional reúne la güira taína, la tambora africana y el acordeón europeo.",
                    "Porque fue compuesto por diplomáticos españoles e italianos en la corte de Santo Domingo.",
                    "Porque sus melodías se basan en canciones gregorianas medievales traducidas al inglés."
                ],
                "correct": 0,
                "teaches": ["dominicana-merengue-bachata-patrimonio"]
            },
            {
                "id": f"{lc_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El mercado binacional de Dajabón se celebra dos veces por semana a menos que un conflicto diplomático __ el paso fronterizo. (cerrar - presente subjuntivo)",
                "answer": "cierre",
                "english": "The Dajabón binational market is held twice a week unless a diplomatic conflict closes the border crossing.",
                "teaches": ["dominicana-frontera-haiti-convivencia"]
            },
            {
                "id": f"{lc_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "La cordillera Central alberga el Pico Duarte, techo geográfico de todas las Antillas. [The Cordillera Central shelters Pico Duarte, geographical roof of all the Antilles.]",
                    "Santo Domingo fue fundada en 1496 como la primera ciudad europea permanente en América. [Santo Domingo was founded in 1496 as the first permanent European city in America.]",
                    "El merengue y la bachata fueron consagrados por la UNESCO como patrimonio de la humanidad. [Merengue and bachata were enshrined by UNESCO as intangible heritage of humanity.]",
                    "La comunidad diaspórica en Nueva York mantiene un puente transnacional vital con la isla. [The diaspora community in New York maintains a vital transnational bridge with the island.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": [
                    "dominicana-geografia-cordillera-bahias",
                    "dominicana-santo-domingo-primada-america",
                    "dominicana-merengue-bachata-patrimonio",
                    "dominicana-beisbol-diaspora-nueva-york"
                ]
            },
            {
                "id": f"{lc_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Socióloga", "text": "¿Cómo definiría el dinamismo contemporáneo de Quisqueya ante el mundo?"},
                    {"speaker": "Ensayista", "text": "_____"},
                    {"speaker": "Socióloga", "text": "Una vitalidad caribeña desbordante que conjuga memoria primada y vocación universal."}
                ],
                "options": [
                    "Es la historia de un pueblo que convirtió su primacía histórica, sus ritmos musicales patrimoniales y su pasión deportiva en un puente transnacional de enorme potencia cultural.",
                    "Las importaciones de trigo y cebada han crecido moderadamente en el último trimestre contable.",
                    "El servicio postal insular entrega encomiendas en todas las oficinas distritales de correos."
                ],
                "correct": 0,
                "teaches": ["dominicana-beisbol-diaspora-nueva-york"]
            },
            {
                "id": f"{lc_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La bachata y el merengue representan la alegría y el sentimiento del pueblo dominicano.",
                "english": "Bachata and merengue represent the joy and feeling of the Dominican people.",
                "teaches": ["dominicana-merengue-bachata-patrimonio"]
            },
            {
                "id": f"{lc_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta una síntesis analítica sobre la proyección cultural dominicana empleando una cláusula restrictiva ('siempre y cuando') o un nexo exceptivo ('a menos que').",
                        "answer": "La identidad cultural dominicana continuará expandiéndose por el mundo siempre y cuando las nuevas generaciones de la diáspora preserven su música, su idioma y sus lazos familiares con la isla."
                    }
                ],
                "teaches": ["dominicana-beisbol-diaspora-nueva-york"]
            }
        ]
    })

    # Regional Capstone Story: b2-dominicana.json
    story_dom_capstone = {
        "id": "b2-dominicana",
        "title": "Consolidación: Quisqueya la bella",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica panorámica de nivel B2 sobre la República Dominicana: síntesis de su geografía montañosa y costera, su primacía histórica colonial, su riqueza musical, la encrucijada fronteriza y su vibrante proyección diaspórica.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Conocida afectuosamente por sus habitantes con el vocablo indígena ancestral de 'Quisqueya' —que en lengua taína evoca la 'madre de todas las tierras'—, la República Dominicana ocupa un sitial absolutamente insustituible en el tablero histórico, ecológico y cultural de las Américas. Asentada en las dos terceras partes orientales de la isla de La Española, esta nación caribeña desafía cualquier encasillamiento reductor: lejos de constituir un mero enclave de resorts costeros, Quisqueya representa un territorio fascinante donde convergen las cumbres más elevadas de las Antillas, la memoria de las primeras instituciones europeas del Nuevo Mundo, una síntesis musical declarada patrimonio universal y una de las comunidades transnacionales más dinámicas del planeta."
            },
            {
                "type": "narration",
                "text": "En el orden geográfico, la isla sorprende por una diversidad de paisajes y microclimas que abarca desde las heladas cumbres alpinas del Pico Duarte —techo geográfico antillano que sobrepasa los tres mil metros en la cordillera Central— hasta la profunda depresión hipersalina del lago Enriquillo, situado a más de cuarenta metros bajo el nivel del mar. Sus costas albergan santuarios marinos de relevancia planetaria, como la bahía de Samaná, adonde millares de ballenas jorobadas acuden puntualmente cada invierno para aparearse y dar a luz, mientras que en el litoral oriental los laberintos kársticos y manglares del parque nacional Los Haitises resguardan grutas sagradas donde aún relumbran los petroglifos de la extinta civilización taína."
            },
            {
                "type": "narration",
                "text": "En el plano histórico, Santo Domingo ostenta con orgullo indiscutible el título de Ciudad Primada de América. Fundada en 1496 por Bartolomé Colón a orillas del río Ozama y reedificada con cuadrícula renacentista por Nicolás de Ovando tras el ciclón de 1502, la capital dominicana fue el crisol donde se ensayaron las primeras estructuras del imperio colonial: la primera catedral gótica, el primer alcázar virreinal, el primer hospital público y la primera universidad de Indias, fundada en 1538. Fue allí también donde la comunidad de los frailes dominicos, encabezada por Antón de Montesinos y continuada por Bartolomé de las Casas, alzó en 1511 la primera denuncia profética contra los abusos de la encomienda, inaugurando la batalla por la dignidad humana y los derechos naturales en la modernidad occidental."
            },
            {
                "type": "narration",
                "text": "La identidad sonora dominicana constituye otro de sus legados más deslumbrantes. En el merengue típico, el pueblo campesino del Cibao forjó una síntesis armónica irrepetible: la güira de los aborígenes taínos, la tambora de los cautivos africanos y el acordeón diatónico de los navegantes europeos dialogan en un compás acelerado y festivo que sobrevoló dictaduras y fronteras para conquistar los salones del orbe. Décadas más tarde, la bachata recorrió un sendero de reivindicación heroica: desde las cantinas y cafetines marginales de arrabal donde nació como expresión del 'amargue' popular hasta su consagración sinfónica de la mano de Juan Luis Guerra, ambos géneros han sido proclamados por la UNESCO Patrimonio Cultural Inmaterial de la Humanidad, consagrando la alegría y el lirismo como señas inmutables del alma nacional."
            },
            {
                "type": "narration",
                "text": "Esta vocación de convivencia y supervivencia adquiere un matiz complejo en la franja fronteriza que separa a la República Dominicana de la vecina República de Haití. Marcada por memorias traumáticas como la invasión haitiana del siglo XIX o la matanza trujillista de 1937, la relación insular convive hoy con una densa interdependencia cotidiana. En los bateyes azucareros y en las obras urbanas, la fuerza de trabajo migrante dinamiza la economía dominicana, mientras que en mercados binacionales como el de Dajabón el comercio fluido demuestra que el destino de ambos pueblos exige diálogo, respeto mutuo a la soberanía y cooperación ambiental para preservar las cuencas fluviales que dan vida a la isla compartida."
            },
            {
                "type": "narration",
                "text": "En el siglo XXI, la República Dominicana se proyecta con fuerza irresistible a través de dos embajadores globales: su cantera inagotable de peloteros de béisbol y su formidable comunidad diaspórica. Desde San Pedro de Macorís hasta Cooperstown, figuras como Marichal, Pedro Martínez y David Ortiz han transformado 'la pelota' en un estandarte de excelencia y superación social. Al mismo tiempo, los más de dos millones de dominicanos afincados en el exterior, con su epicentro señero en Washington Heights en Nueva York, han tejido un puente transnacional de remesas, bilingüismo y participación cívica que inyecta vitalidad financiera a la isla mientras enriquece la sociedad estadounidense con su inconfundible sabor antillano."
            },
            {
                "type": "narration",
                "text": "Así, Quisqueya la bella se afirma ante el mundo como una tierra bendecida por la naturaleza y curtida por los vientos de la historia. Una nación que supo transformar los desgarros coloniales y las vicisitudes del presente en una cultura luminosa, hospitalaria y musical, recordándonos que en este rincón del Caribe donde comenzó el encuentro entre continentes sigue latiendo con fuerza indomable la fe en la dignidad humana, la poesía del amor correspondido y la esperanza de un porvenir próspero y compartido."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singularidades geográficas e históricas sintetizan la identidad de Quisqueya según la lección de consolidación?",
                        "options": [
                            "Albergar la cumbre más alta de las Antillas (Pico Duarte), las primeras instituciones coloniales y una música declarada patrimonio de la humanidad.",
                            "Ser el único país antillano donde rige un sistema de gobierno monárquico parlamentario federado.",
                            "Poseer las mayores reservas de gas licuado y carbón mineral de la cuenca del Atlántico norte.",
                            "Haber sido fundado como un protectorado exclusivo de navegantes y comerciantes holandeses en el siglo XVII."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los párrafos 1, 2 y 3 resumen la conjunción de geografía extrema (Pico Duarte), primacía colonial (Santo Domingo) y riqueza musical (merengue y bachata)."
                    },
                    {
                        "question": "¿De qué manera dialogan la güira, la tambora y el acordeón en el merengue típico dominicano?",
                        "options": [
                            "Representan la síntesis armónica de las tres raíces culturales de la nación: taína, africana y europea.",
                            "Fueron impuestos por decreto ministerial durante la ocupación militar extranjera de 1916.",
                            "Son instrumentos importados recientemente de las orquestas de cámara de Europa central.",
                            "Se utilizan exclusivamente en celebraciones litúrgicas católicas de la semana santa."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 detalla cómo la güira taína, la tambora africana y el acordeón europeo condensan la tríada étnica de la dominicanidad."
                    },
                    {
                        "question": "¿Cómo se articula la dimensión transnacional de la República Dominicana en el siglo XXI?",
                        "options": [
                            "A través del éxito de sus peloteros en las Grandes Ligas y el puente económico y cultural tendido por la diáspora en Nueva York.",
                            "Mediante la anexión formal de nuevos territorios marítimos en el archipiélago de las Lucayas.",
                            "A través de la sustitución del español por el inglés como idioma vehicular de la administración pública.",
                            "Mediante la renuncia voluntaria al comercio internacional para promover una economía de autosuficiencia cerrada."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 destaca la trascendencia global del béisbol profesional y la pujanza de la comunidad dominicana radicada en EE. UU., especialmente en Nueva York."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc_con}.json", story_dom_capstone)
    write_json(f"stories/world/b2/b2-dominicana.json", story_dom_capstone)

    write_json(f"lessons/b2/{lc_con}.json", make_consolidation_lesson(
        stem=lc_con,
        unit_num=11,
        title="Unit 11 Consolidation: Dominican Republic",
        goal="Consolidate Dominican geographical, colonial, musical, border, and baseball themes through advanced concessive, restrictive, and mixed conditional discourse.",
        grammar_desc="síntesis discursiva sobre la República Dominicana: geografía montañosa, primacía colonial, bachata, relaciones fronterizas y transnacionalidad",
        ex_ref=f"exercises/b2/{lc_con}-ex.json",
        ex_ids=[f"{lc_con}.ex01", f"{lc_con}.ex02", f"{lc_con}.ex03", f"{lc_con}.ex04", f"{lc_con}.ex05", f"{lc_con}.ex06", f"{lc_con}.ex07", f"{lc_con}.ex08"],
        goals=[
            "Synthesize Dominican physical geography from Pico Duarte to Samaná Bay.",
            "Evaluate Santo Domingo's colonial primacy and Montesinos' 1511 human rights sermon.",
            "Analyze the cultural trajectories of merengue and bachata as UNESCO heritage.",
            "Debate border dynamics with Haiti and the transnational baseball nexus in New York."
        ],
        checklist_items=[
            "I can analyze Dominican topography and coastal biodiversity with precise vocabulary.",
            "I can discuss early colonial institutions in Santo Domingo and early human rights debates.",
            "I can evaluate the organology and social evolution of merengue and bachata.",
            "I can analyze border relations with Haiti and the bateyes with objective sociological discourse.",
            "I can discuss baseball academies and the New York diaspora bridge using restrictive and mixed conditional structures."
        ],
        story_ref=f"stories/world/b2/b2-dominicana.json"
    ))
    print("Completed LatAm Unit 11 (Dominican Republic) generation!")

    # -------------------------------------------------------------------------
    # CURRICULUM UNITS WIRING (content/es-latam/curriculum/units/b2.json)
    # -------------------------------------------------------------------------
    units_file = BASE / "curriculum" / "units" / "b2.json"
    with open(units_file, "r", encoding="utf-8") as f:
        units_data = json.load(f)

    existing_stems = set()
    for u in units_data:
        for s in u.get("stems", []):
            existing_stems.add(s)

    if "b2-11-01" not in existing_stems:
        units_data.append({
            "title": "Mixed Conditionals & Restrictive Conditions",
            "stems": [
                "b2-11-01",
                "b2-11-02",
                "b2-11-03",
                "b2-11-04",
                "b2-11-05",
                "b2-11-consolidation"
            ],
            "track": "core"
        })

    if "b2-dominicana-01" not in existing_stems:
        units_data.append({
            "title": "Dominican Republic: The First European Settlement, Merengue & Transnational Identity",
            "stems": [
                "b2-dominicana-01",
                "b2-dominicana-02",
                "b2-dominicana-03",
                "b2-dominicana-04",
                "b2-dominicana-05",
                "b2-dominicana-consolidation"
            ],
            "track": "latam"
        })

    with open(units_file, "w", encoding="utf-8") as f:
        json.dump(units_data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated curriculum/units/b2.json with Unit 11!")

    # -------------------------------------------------------------------------
    # VERIFY WORD COUNTS FOR ALL STORIES
    # -------------------------------------------------------------------------
    all_stories = [
        ("story_core_11", story_core_11),
        ("story_dom_01", story_dom_01),
        ("story_dom_02", story_dom_02),
        ("story_dom_03", story_dom_03),
        ("story_dom_04", story_dom_04),
        ("story_dom_05", story_dom_05),
        ("story_dom_capstone", story_dom_capstone),
    ]
    print("\n--- Story Word Count Audit ---")
    for name, s in all_stories:
        wc = count_words(s)
        status = "OK (650-825)" if 650 <= wc <= 825 else f"OUT OF RANGE: {wc}"
        print(f"{name:20s}: {wc:4d} words -> {status}")
        assert 650 <= wc <= 825, f"Word count {wc} out of range for {name}!"


if __name__ == "__main__":
    run()
