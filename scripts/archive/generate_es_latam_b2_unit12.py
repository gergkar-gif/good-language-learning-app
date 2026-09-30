#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Pair 12:
  - Core Unit 12: Finality, Purpose & Institutional Goals (b2-12)
  - Regional Unit 12: Puerto Rico: Boricua Identity, Sovereignty & Cultural Defiance (b2-puertorico)
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
        "b2-unit12-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "institutional missions, strategic objectives, mandates, and prospective planning"
        },
        "finales-subjuntivo-a-fin-de-que": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "purpose clauses with subjunctive using formal connectors"
        },
        "finalidad-infinitivo-correferencia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "purpose clauses with infinitive under subject coreference"
        },
        "finales-con-vistas-a-miras-a": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "prospective and institutional purpose with compound locutions"
        },
        "finales-negativas-para-que-no": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "negative purpose clauses preventing undesired outcomes"
        },
        "finalidad-condicional-proposito": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "purpose clauses in hypothetical and conditional frames"
        },
        "b2-puertorico-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "puerto rican geography, history, commonwealth status, music, and civic resistance"
        },
        "puertorico-biodiversidad-yunque-bioluminiscencia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "ecosystems and geological heritage in puerto rico"
        },
        "puertorico-grito-lares-cesion-1898": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "19th-century independence and the colonial cession of 1898"
        },
        "puertorico-estado-libre-asociado-debate": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "the commonwealth status debate and political parties in puerto rico"
        },
        "puertorico-bomba-plena-salsa-urbano": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "evolution of afro-boricua musical genres and urban music"
        },
        "puertorico-huracan-maria-deuda-resistencia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "the debt crisis and civic resilience in puerto rico"
        }
    }

    for k, v in new_skills.items():
        if k not in skill_reg["skills"]:
            skill_reg["skills"][k] = v

    with open(skill_reg_path, "w", encoding="utf-8") as f:
        json.dump(skill_reg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated skill-registry.json for Unit 12")

    grammar_titles_path = BASE / "indexes" / "grammar-titles.json"
    with open(grammar_titles_path, "r", encoding="utf-8") as f:
        grammar_titles = json.load(f)

    new_titles = {
        "finales-subjuntivo-a-fin-de-que": "purpose clauses with subjunctive using formal connectors",
        "finalidad-infinitivo-correferencia": "purpose clauses with infinitive under subject coreference",
        "finales-con-vistas-a-miras-a": "prospective and institutional purpose with compound locutions",
        "finales-negativas-para-que-no": "negative purpose clauses preventing undesired outcomes",
        "finalidad-condicional-proposito": "purpose clauses in hypothetical and conditional frames",
        "puertorico-biodiversidad-yunque-bioluminiscencia": "ecosystems and geological heritage in puerto rico",
        "puertorico-grito-lares-cesion-1898": "19th-century independence and the colonial cession of 1898",
        "puertorico-estado-libre-asociado-debate": "the commonwealth status debate and political parties in puerto rico",
        "puertorico-bomba-plena-salsa-urbano": "evolution of afro-boricua musical genres and urban music",
        "puertorico-huracan-maria-deuda-resistencia": "the debt crisis and civic resilience in puerto rico"
    }

    for k, v in new_titles.items():
        grammar_titles[k] = v

    with open(grammar_titles_path, "w", encoding="utf-8") as f:
        json.dump(grammar_titles, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated grammar-titles.json for Unit 12")

    # -------------------------------------------------------------------------
    # CORE UNIT 12 (b2-12): Finality, Purpose & Institutional Goals
    # -------------------------------------------------------------------------

    # Lesson 1: b2-12-01 - Oraciones finales con subjuntivo: a fin de que, para que, con el objeto de que
    l1 = "b2-12-01"
    write_json(f"vocabulary/b2/{l1}-voc.json", {
        "id": "vocab.b2.12.01",
        "lesson": l1,
        "title": "Misión institucional, finalidades y metas estratégicas",
        "theme": "Vocabulario de objetivos programáticos, directrices y propósitos",
        "words": [
            {"lemma": "el propósito", "translation": "purpose, aim", "pos": "noun"},
            {"lemma": "la finalidad", "translation": "end, ultimate purpose", "pos": "noun"},
            {"lemma": "encaminar", "translation": "to direct, to channel towards", "pos": "verb"},
            {"lemma": "el cometido", "translation": "task, mandate, mission", "pos": "noun"},
            {"lemma": "la directriz", "translation": "guideline, directive", "pos": "noun"},
            {"lemma": "perseguir", "translation": "to pursue, to seek", "pos": "verb"},
            {"lemma": "programático", "translation": "programmatic", "pos": "adjective"},
            {"lemma": "la meta", "translation": "goal, target", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l1}-a-gr.json", {
        "id": "grammar.b2.12.01.finales-subjuntivo",
        "title": "Oraciones finales con subjuntivo: a fin de que, para que, con el objeto de que",
        "sections": [
            {
                "type": "text",
                "title": "Estructuras de finalidad con cambio de sujeto",
                "content": "Las oraciones subordinadas finales expresan la meta, el propósito o la intención que orienta la acción de la oración principal. Cuando existe cambio de sujeto entre el verbo principal y el subordinado, exigen de manera categórica el modo subjuntivo: 'para que', 'a fin de que', 'con el objeto de que', 'con el propósito de que', 'con la intención de que'."
            },
            {
                "type": "table",
                "title": "Conectores finales en registro formal",
                "rows": [
                    ["'Para que' (estándar universal)", "'El ministerio aprobó la partida para que los hospitales compren insumos'"],
                    ["'A fin de que' (registro institucional)", "'Se reformó el reglamento a fin de que la comisión delibere con celeridad'"],
                    ["'Con el objeto de que' (registro legislativo)", "'Se dictó la orden con el objeto de que las partes resuelvan la disputa'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el discurso institucional y corporativo",
                "items": [
                    {"spanish": "La comisión redactó nuevas directrices a fin de que los auditores evalúen el gasto público con total transparencia.", "english": "The commission drafted new guidelines so that auditors may evaluate public spending with total transparency."},
                    {"spanish": "El director convocó a la asamblea con el objeto de que los accionistas voten la ampliación de capital.", "english": "The director convened the assembly in order for shareholders to vote on the capital increase."},
                    {"spanish": "Diseñamos un plan de capacitación integral para que los docentes incorporen herramientas digitales en el aula.", "english": "We designed a comprehensive training plan so that teachers incorporate digital tools in the classroom."}
                ]
            },
            {
                "type": "tip",
                "content": "En la correlación temporal, el verbo final adopta presente de subjuntivo tras presentes o futuros ('convoca para que voten'), e imperfecto o pluscuamperfecto de subjuntivo tras tiempos del pasado ('convocó para que votaran / votasen')."
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
                    ["el propósito", "purpose, aim"],
                    ["el cometido", "task, mandate, mission"],
                    ["encaminar", "to channel, to direct towards"],
                    ["la directriz", "guideline, directive"]
                ],
                "teaches": ["b2-unit12-vocab"]
            },
            {
                "id": f"{l1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El parlamento aprobó la ley a fin de que los ciudadanos __ sus derechos fundamentales ante los tribunales. (poder - presente subjuntivo)",
                "answer": "puedan",
                "english": "Parliament passed the law so that citizens can exercise their fundamental rights before the courts.",
                "teaches": ["finales-subjuntivo-a-fin-de-que"]
            },
            {
                "id": f"{l1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la oración 'El canciller intervino para que se reanude el diálogo' exige modo subjuntivo?",
                "options": [
                    "Porque expresa una intención o finalidad prospectiva con sujetos gramaticales distintos en ambas cláusulas.",
                    "Porque la conjunción 'para que' es un conector causal que describe hechos ya consumados.",
                    "Porque el verbo 'reanudar' pertenece a la tercera conjugación de verbos reflexivos."
                ],
                "correct": 0,
                "teaches": ["finales-subjuntivo-a-fin-de-que"]
            },
            {
                "id": f"{l1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "gobierno", "legisló", "a", "fin", "de", "que", "hubiera", "justicia."],
                "solution": ["El", "gobierno", "legisló", "a", "fin", "de", "que", "hubiera", "justicia."],
                "english": "The government legislated so that there would be justice.",
                "teaches": ["finales-subjuntivo-a-fin-de-que"]
            },
            {
                "id": f"{l1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Rectora", "text": "¿Con qué propósito se fundó el nuevo centro de investigaciones bioéticas?"},
                    {"speaker": "Investigador principal", "text": "_____"},
                    {"speaker": "Rectora", "text": "Un cometido esencial para asegurar la dimensión humanista de la ciencia."}
                ],
                "options": [
                    "Se creó a fin de que los académicos evalúen el impacto de las tecnologías emergentes sobre los derechos ciudadanos.",
                    "El laboratorio central dispone de tres microscopios electrónicos adquiridos en Japón.",
                    "Las clases presenciales de biología general comienzan puntualmente a las ocho de la mañana."
                ],
                "correct": 0,
                "teaches": ["finales-subjuntivo-a-fin-de-que"]
            },
            {
                "id": f"{l1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se reformó el estatuto con el objeto de que se garantice la equidad interna.",
                "english": "The statute was reformed in order for internal equity to be guaranteed.",
                "teaches": ["finales-subjuntivo-a-fin-de-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1}.json", make_lesson(
        stem=l1,
        unit_num=12,
        title="Oraciones finales con subjuntivo: a fin de que, para que, con el objeto de que",
        goal="Master purpose clauses requiring the subjunctive (para que, a fin de que, con el objeto de que) under subject change in formal institutional prose.",
        grammar_desc="oraciones subordinadas finales con subjuntivo: para que, a fin de que, con el objeto de que",
        grammar_ref=f"grammar/b2/{l1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l1}-voc.json",
        ex_ref=f"exercises/b2/{l1}-ex.json",
        ex_ids=[f"{l1}.ex01", f"{l1}.ex02", f"{l1}.ex03", f"{l1}.ex04", f"{l1}.ex05", f"{l1}.ex06"],
        goals=[
            "Formulate institutional purpose clauses with 'a fin de que' and 'con el objeto de que'.",
            "Apply sequence of tenses between main verb and subjunctive purpose verb.",
            "Deploy strategic vocabulary (cometido, directriz, encaminar, programático)."
        ]
    ))

    # Lesson 2: b2-12-02 - Finalidad con infinitivo: correferencia y preposiciones
    l2 = "b2-12-02"
    write_json(f"vocabulary/b2/{l2}-voc.json", {
        "id": "vocab.b2.12.02",
        "lesson": l2,
        "title": "Correferencia, planes de acción y ejecución directa",
        "theme": "Vocabulario de ejecución estratégica, competencias y cometidos",
        "words": [
            {"lemma": "la prerrogativa", "translation": "prerogative, privilege", "pos": "noun"},
            {"lemma": "acatar", "translation": "to comply with, to abide by", "pos": "verb"},
            {"lemma": "la atribución", "translation": "power, authority, attribution", "pos": "noun"},
            {"lemma": "propiciar", "translation": "to foster, to facilitate", "pos": "verb"},
            {"lemma": "el afán", "translation": "eagerness, zeal, keen desire", "pos": "noun"},
            {"lemma": "viabilizar", "translation": "to make viable, to facilitate", "pos": "verb"},
            {"lemma": "la competencia", "translation": "jurisdiction, competence", "pos": "noun"},
            {"lemma": "diligente", "translation": "diligent", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l2}-a-gr.json", {
        "id": "grammar.b2.12.02.finalidad-infinitivo",
        "title": "Finalidad con infinitivo: correferencia y locuciones prepositivas",
        "sections": [
            {
                "type": "text",
                "title": "Regla de correferencia de sujeto en oraciones finales",
                "content": "Cuando el sujeto de la acción principal y el de la finalidad coinciden (correferencia subjetiva), la norma gramatical exige el uso del infinitivo precedido de preposición: 'para', 'a fin de', 'con el objeto de', 'al objeto de', 'con miras a', 'con el propósito de': 'El ministro viajó a Ginebra para exponer la postura nacional' (nunca *'para que él exponga'*)."
            },
            {
                "type": "table",
                "title": "Construcciones de finalidad con infinitivo",
                "rows": [
                    ["'Para + infinitivo'", "'Los delegados se reunieron para debatir la moción'"],
                    ["'A fin de + infinitivo'", "'La empresa redujo costos a fin de evitar despidos masivos'"],
                    ["'Con el objeto de + infinitivo'", "'Presentamos la solicitud con el objeto de obtener la licencia ambiental'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en resoluciones y actas de acuerdos",
                "items": [
                    {"spanish": "La junta directiva sesionó con el objeto de evaluar el plan financiero del próximo bienio.", "english": "The board of directors convened in order to evaluate the financial plan for the next biennium."},
                    {"spanish": "El presidente creó una comisión especial a fin de investigar los sobreprecios en la licitación.", "english": "The president created a special commission in order to investigate price overruns in the bidding process."},
                    {"spanish": "Adoptamos protocolos estrictos para garantizar la trazabilidad de los fondos públicos.", "english": "We adopted strict protocols to guarantee the traceability of public funds."}
                ]
            },
            {
                "type": "tip",
                "content": "El uso de la subordinada con 'para que' cuando hay correferencia de sujeto (*'Trabajo duro para que yo pueda comprar una casa'*) es un error estilístico grave en español; debe decirse siempre: 'Trabajo duro para comprar una casa'."
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
                    ["propiciar", "to foster, to facilitate"],
                    ["la atribución", "power, authority, attribution"],
                    ["el afán", "eagerness, keen desire"],
                    ["viabilizar", "to make viable, to facilitate"]
                ],
                "teaches": ["b2-unit12-vocab"]
            },
            {
                "id": f"{l2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El canciller solicitó una reunión urgente a fin de __ los términos del acuerdo de paz. (negociar - infinitivo)",
                "answer": "negociar",
                "english": "The foreign minister requested an urgent meeting in order to negotiate the terms of the peace agreement.",
                "teaches": ["finalidad-infinitivo-correferencia"]
            },
            {
                "id": f"{l2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué es incorrecto decir 'El abogado fue al tribunal para que él presentara la demanda'?",
                "options": [
                    "Porque al haber correferencia de sujeto entre el verbo principal y la finalidad debe emplearse infinitivo: 'para presentar la demanda'.",
                    "Porque el verbo 'presentar' solo admite subjuntivo cuando va precedido de adverbios de duda.",
                    "Porque en las oraciones jurídicas está prohibido el uso de pronombres personales de tercera persona."
                ],
                "correct": 0,
                "teaches": ["finalidad-infinitivo-correferencia"]
            },
            {
                "id": f"{l2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "expertos", "viajaron", "para", "evaluar", "los", "daños", "del", "sismo."],
                "solution": ["Los", "expertos", "viajaron", "para", "evaluar", "los", "daños", "del", "sismo."],
                "english": "The experts traveled in order to evaluate the earthquake damage.",
                "teaches": ["finalidad-infinitivo-correferencia"]
            },
            {
                "id": f"{l2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Contralor", "text": "¿Con qué propósito comparece la directiva ante la comisión parlamentaria?"},
                    {"speaker": "Abogado corporativo", "text": "_____"},
                    {"speaker": "Contralor", "text": "Escucharemos sus descargos con la debida atención reglamentaria."}
                ],
                "options": [
                    "Comparecemos con el objeto de aclarar los informes contables y disipar cualquier sombra de duda.",
                    "Las actas de la sesión anterior están encuadernadas en piel de color verde oscuro.",
                    "El ascensor del parlamento tiene capacidad para seis personas simultáneamente."
                ],
                "correct": 0,
                "teaches": ["finalidad-infinitivo-correferencia"]
            },
            {
                "id": f"{l2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El comité se congregó a fin de dirimir las discrepancias sobre el proyecto.",
                "english": "The committee convened in order to resolve discrepancies regarding the project.",
                "teaches": ["finalidad-infinitivo-correferencia"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2}.json", make_lesson(
        stem=l2,
        unit_num=12,
        title="Finalidad con infinitivo: correferencia y preposiciones",
        goal="Master infinitive purpose clauses under subject coreference (para + inf, a fin de + inf) in official resolutions and administrative reports.",
        grammar_desc="construcciones finales con infinitivo bajo correferencia: para, a fin de, con el objeto de",
        grammar_ref=f"grammar/b2/{l2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l2}-voc.json",
        ex_ref=f"exercises/b2/{l2}-ex.json",
        ex_ids=[f"{l2}.ex01", f"{l2}.ex02", f"{l2}.ex03", f"{l2}.ex04", f"{l2}.ex05", f"{l2}.ex06"],
        goals=[
            "Apply the coreference rule selecting infinitive over subjunctive in purpose clauses.",
            "Utilize compound prepositional locutions ('con el objeto de', 'a fin de') with infinitive.",
            "Deploy institutional mandate vocabulary (atribución, propiciar, viabilizar, diligente)."
        ]
    ))

    # Lesson 3: b2-12-03 - Finales con miras a, con vistas a y de modo que
    l3 = "b2-12-03"
    write_json(f"vocabulary/b2/{l3}-voc.json", {
        "id": "vocab.b2.12.03",
        "lesson": l3,
        "title": "Prospectiva estratégica, horizontes y metas institucionales",
        "theme": "Vocabulario de proyección a largo plazo, prospectiva y horizontes",
        "words": [
            {"lemma": "el horizonte", "translation": "horizon, outlook", "pos": "noun"},
            {"lemma": "la prospectiva", "translation": "foresight, forward-looking analysis", "pos": "noun"},
            {"lemma": "proyectar", "translation": "to project, to plan", "pos": "verb"},
            {"lemma": "la envergadura", "translation": "scope, magnitude, scale", "pos": "noun"},
            {"lemma": "estratégico", "translation": "strategic", "pos": "adjective"},
            {"lemma": "articular", "translation": "to articulate, to coordinate", "pos": "verb"},
            {"lemma": "la previsión", "translation": "forecast, foresight", "pos": "noun"},
            {"lemma": "el hito", "translation": "milestone, landmark", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l3}-a-gr.json", {
        "id": "grammar.b2.12.03.con-vistas-a-miras-a",
        "title": "Finales con miras a, con vistas a y de modo que",
        "sections": [
            {
                "type": "text",
                "title": "Locuciones finales de prospección y planificación",
                "content": "Para expresar propósitos enmarcados en planes estratégicos de mediano y largo plazo, el registro culto recurre a locuciones complejas como 'con miras a', 'con vistas a', 'en orden a' (con sustantivo o infinitivo: 'con miras a consolidar la integración') y 'de modo que / de manera que' (con valor final exigiendo subjuntivo: 'redactamos el informe de modo que todos comprendan las conclusiones')."
            },
            {
                "type": "table",
                "title": "Matices de prospección estratégica",
                "rows": [
                    ["'Con miras a + inf / sust'", "'El gobierno suscribió el convenio con miras a abrir nuevos mercados asiáticos'"],
                    ["'Con vistas a + inf / sust'", "'Se construyó el parque tecnológico con vistas a la transición energética'"],
                    ["'De modo que + subjuntivo'", "'Organizamos los turnos de manera que nadie trabaje más de ocho horas'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en planes estratégicos de desarrollo",
                "items": [
                    {"spanish": "El banco central ajustó las tasas de interés con miras a frenar la inflación en el segundo semestre.", "english": "The central bank adjusted interest rates with a view to curbing inflation in the second semester."},
                    {"spanish": "Se diseñó el plan de infraestructura con vistas a modernizar la red ferroviaria nacional.", "english": "The infrastructure plan was designed with a view to modernizing the national railway network."},
                    {"spanish": "Distribuimos los recursos de modo que los municipios más rezagados reciban prioridad inmediata.", "english": "We distributed resources so that the most lagging municipalities receive immediate priority."}
                ]
            },
            {
                "type": "tip",
                "content": "Cuidado con 'de modo que': si va seguido de indicativo tiene valor consecutivo ('Llegó tarde, de modo que perdió el tren'). Solo tiene valor final cuando va seguido de subjuntivo ('Explicó las reglas de modo que todos las cumplieran')."
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
                    ["el horizonte", "horizon, outlook"],
                    ["la prospectiva", "foresight, forward-looking analysis"],
                    ["la envergadura", "scope, scale, magnitude"],
                    ["el hito", "milestone, landmark"]
                ],
                "teaches": ["b2-unit12-vocab"]
            },
            {
                "id": f"{l3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La cumbre internacional sesionó con miras a __ un tratado vinculante sobre biodiversidad marina. (aprobar - infinitivo)",
                "answer": "aprobar",
                "english": "The international summit met with a view to approving a binding treaty on marine biodiversity.",
                "teaches": ["finales-con-vistas-a-miras-a"]
            },
            {
                "id": f"{l3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué diferencia semántica existe entre 'Habló de modo que todos se enteraron' y 'Habló de modo que todos se enteraran'?",
                "options": [
                    "La primera es consecutiva (constata un hecho real en indicativo) y la segunda es final (expresa el propósito o intención en subjuntivo).",
                    "Ambas expresan exactamente lo mismo sin ningún cambio de significado.",
                    "La primera expresa una orden obligatoria y la segunda un deseo irrealizable."
                ],
                "correct": 0,
                "teaches": ["finales-con-vistas-a-miras-a"]
            },
            {
                "id": f"{l3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Trabajamos", "con", "miras", "a", "consolidar", "la", "paz", "continental."],
                "solution": ["Trabajamos", "con", "miras", "a", "consolidar", "la", "paz", "continental."],
                "english": "We work with a view to consolidating continental peace.",
                "teaches": ["finales-con-vistas-a-miras-a"]
            },
            {
                "id": f"{l3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministra de Comercio", "text": "¿Con qué horizonte temporal se negoció el acuerdo aduanero regional?"},
                    {"speaker": "Negociador jefe", "text": "_____"},
                    {"speaker": "Ministra de Comercio", "text": "Una meta ambiciosa que potenciará nuestras exportaciones hacia el Pacífico."}
                ],
                "options": [
                    "Se estructuró con vistas a eliminar los aranceles industriales de forma progresiva en un plazo de diez años.",
                    "Los puertos fluviales del continente registran variaciones estacionales en el calado de los barcos.",
                    "El salón de recepciones de la cancillería fue remodelado en el año 2012."
                ],
                "correct": 0,
                "teaches": ["finales-con-vistas-a-miras-a"]
            },
            {
                "id": f"{l3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se coordinaron los esfuerzos de modo que se optimizaran los recursos disponibles.",
                "english": "Efforts were coordinated so that available resources would be optimized.",
                "teaches": ["finales-con-vistas-a-miras-a"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3}.json", make_lesson(
        stem=l3,
        unit_num=12,
        title="Finales con miras a, con vistas a y de modo que",
        goal="Master prospective purpose locutions ('con miras a', 'con vistas a', 'de modo que + subj') in strategic planning and multilateral agreements.",
        grammar_desc="locuciones de finalidad prospectiva y estratégica: con miras a, con vistas a, de modo que + subjuntivo",
        grammar_ref=f"grammar/b2/{l3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l3}-voc.json",
        ex_ref=f"exercises/b2/{l3}-ex.json",
        ex_ids=[f"{l3}.ex01", f"{l3}.ex02", f"{l3}.ex03", f"{l3}.ex04", f"{l3}.ex05", f"{l3}.ex06"],
        goals=[
            "Formulate long-term strategic aims using 'con miras a' and 'con vistas a'.",
            "Differentiate final 'de modo que' (+ subj) from consecutive 'de modo que' (+ ind).",
            "Deploy forward-looking planning vocabulary (horizonte, prospectiva, envergadura, articular)."
        ]
    ))

    # Lesson 4: b2-12-04 - Finales negativas e inhibición de consecuencias indeseadas
    l4 = "b2-12-04"
    write_json(f"vocabulary/b2/{l4}-voc.json", {
        "id": "vocab.b2.12.04",
        "lesson": l4,
        "title": "Prevención de riesgos, cautelas y salvaguardas",
        "theme": "Vocabulario de mitigación de daños, cautela e inhibición de riesgos",
        "words": [
            {"lemma": "la cautela", "translation": "caution, prudence", "pos": "noun"},
            {"lemma": "soslayar", "translation": "to avoid, to sidestep", "pos": "verb"},
            {"lemma": "la contingencia", "translation": "contingency, risk", "pos": "noun"},
            {"lemma": "precaver", "translation": "to prevent, to guard against", "pos": "verb"},
            {"lemma": "el blindaje", "translation": "shielding, legal safeguard", "pos": "noun"},
            {"lemma": "disuadir", "translation": "to deter, to dissuade", "pos": "verb"},
            {"lemma": "la salvaguardia", "translation": "safeguard, protection", "pos": "noun"},
            {"lemma": "preventivo", "translation": "preventive", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l4}-a-gr.json", {
        "id": "grammar.b2.12.04.finales-negativas",
        "title": "Finales negativas e inhibición de consecuencias indeseadas",
        "sections": [
            {
                "type": "text",
                "title": "Estructuras para evitar un resultado adverso",
                "content": "Cuando la finalidad de una acción consiste en impedir, evitar o prevenir que ocurra un evento perjudicial, el español recurre a oraciones finales negativas o preventivas: 'para que no', 'a fin de que no', 'con el objeto de que no' (con subjuntivo) o locuciones prepositivas de valor prohibitivo como 'para no + inf' o 'a fin de no + inf' cuando hay correferencia."
            },
            {
                "type": "table",
                "title": "Esquemas de finalidad preventiva y disuasoria",
                "rows": [
                    ["'Para que no + subjuntivo'", "'Reforzaron los terraplenes para que el río no desborde la ciudad'"],
                    ["'A fin de que no + subjuntivo'", "'Se blindaron los archivos a fin de que no se filtren datos confidenciales'"],
                    ["'Para no + infinitivo' (correferencia)", "'El testigo usó un seudónimo para no sufrir represalias'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en gestión de crisis y protocolos de seguridad",
                "items": [
                    {"spanish": "El banco central intervino en el mercado cambiario para que no se desatara una corrida especulativa.", "english": "The central bank intervened in the foreign exchange market so that a speculative run would not break out."},
                    {"spanish": "Los diplomáticos redactaron el comunicado con suma cautela a fin de no herir susceptibilidades regionales.", "english": "Diplomats drafted the communiqué with great caution in order not to hurt regional sensitivities."},
                    {"spanish": "Se instalaron cortafuegos digitales para que los atacantes no vulneren los servidores electorales.", "english": "Digital firewalls were installed so that attackers do not breach the electoral servers."}
                ]
            },
            {
                "type": "tip",
                "content": "Evita el calco innecesario del inglés 'in order not to' traducido como *'de orden a no'*. Usa con naturalidad 'a fin de no + inf' o 'para no + inf'."
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
                    ["la cautela", "caution, prudence"],
                    ["soslayar", "to avoid, to sidestep"],
                    ["precaver", "to guard against, to prevent"],
                    ["disuadir", "to deter, to dissuade"]
                ],
                "teaches": ["b2-unit12-vocab"]
            },
            {
                "id": f"{l4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las autoridades evacuaron las poblaciones costeras a fin de que el huracán no __ pérdidas de vidas humanas. (cobrarse - imperfecto subjuntivo)",
                "answer": "se cobrara",
                "english": "Authorities evacuated coastal populations so that the hurricane would not claim human lives.",
                "teaches": ["finales-negativas-para-que-no"]
            },
            {
                "id": f"{l4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué valor pragmático aporta la construcción 'para que no se malinterprete mi postura'?",
                "options": [
                    "Una finalidad preventiva que busca despejar dudas y precaver equívocos en la comunicación.",
                    "Una prohibición legal imperativa de carácter sancionatorio.",
                    "Una hipótesis contrafáctica imposible sobre el pasado histórico."
                ],
                "correct": 0,
                "teaches": ["finales-negativas-para-que-no"]
            },
            {
                "id": f"{l4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Tomaron", "medidas", "para", "que", "no", "se", "repitiera", "el", "desastre."],
                "solution": ["Tomaron", "medidas", "para", "que", "no", "se", "repitiera", "el", "desastre."],
                "english": "They took measures so that the disaster would not repeat itself.",
                "teaches": ["finales-negativas-para-que-no"]
            },
            {
                "id": f"{l4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministro de Salud", "text": "¿Por qué se declaró la cuarentena preventiva en los puertos de desembarco?"},
                    {"speaker": "Epidemióloga", "text": "_____"},
                    {"speaker": "Ministro de Salud", "text": "Una salvaguarda indispensable para proteger a toda la población insular."}
                ],
                "options": [
                    "Se procedió al aislamiento preventivo para que el virus no se propagara de manera comunitaria hacia los centros urbanos.",
                    "Los almacenes aduaneros resguardan cargamentos de café en sacos de yute natural.",
                    "Las gaviotas marinas sobrevuelan las bahías durante la bajamar."
                ],
                "correct": 0,
                "teaches": ["finales-negativas-para-que-no"]
            },
            {
                "id": f"{l4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se reforzó el blindaje legal a fin de que no prosperen demandas fraudulentas.",
                "english": "Legal shielding was reinforced so that fraudulent lawsuits do not succeed.",
                "teaches": ["finales-negativas-para-que-no"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4}.json", make_lesson(
        stem=l4,
        unit_num=12,
        title="Finales negativas e inhibición de consecuencias indeseadas",
        goal="Master negative purpose clauses ('para que no', 'a fin de que no') in risk prevention, security protocols, and crisis management.",
        grammar_desc="oraciones finales negativas y preventivas: para que no + subjuntivo, a fin de no + infinitivo",
        grammar_ref=f"grammar/b2/{l4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l4}-voc.json",
        ex_ref=f"exercises/b2/{l4}-ex.json",
        ex_ids=[f"{l4}.ex01", f"{l4}.ex02", f"{l4}.ex03", f"{l4}.ex04", f"{l4}.ex05", f"{l4}.ex06"],
        goals=[
            "Formulate preventive purpose clauses inhibiting unwanted events with 'para que no'.",
            "Use coreferent negative infinitive structures ('a fin de no + inf').",
            "Deploy risk mitigation vocabulary (cautela, precaver, blindaje, disuadir, salvaguardia)."
        ]
    ))

    # Lesson 5: b2-12-05 - Finalidad en marcos hipotéticos y condicionales
    l5 = "b2-12-05"
    write_json(f"vocabulary/b2/{l5}-voc.json", {
        "id": "vocab.b2.12.05",
        "lesson": l5,
        "title": "Finalidades hipotéticas, retórica de intenciones y dilemas morales",
        "theme": "Vocabulario de motivaciones ocultas, teleología y juicio ético",
        "words": [
            {"lemma": "el móvil", "translation": "motive, driving reason", "pos": "noun"},
            {"lemma": "inconfesable", "translation": "unmentionable, unconfessable", "pos": "adjective"},
            {"lemma": "la coartada", "translation": "alibi, pretext", "pos": "noun"},
            {"lemma": "dilucidar", "translation": "to elucidate, to shed light on", "pos": "verb"},
            {"lemma": "la teleología", "translation": "teleology, doctrine of purpose", "pos": "noun"},
            {"lemma": "el dilema", "translation": "dilemma", "pos": "noun"},
            {"lemma": "desentrañar", "translation": "to unravel, to decipher", "pos": "verb"},
            {"lemma": "inconfeso", "translation": "unconfessed, covert", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l5}-a-gr.json", {
        "id": "grammar.b2.12.05.finalidad-condicional",
        "title": "Finalidad en marcos hipotéticos y condicionales",
        "sections": [
            {
                "type": "text",
                "title": "Intersección de finalidad e hipótesis en la literatura y el debate moral",
                "content": "En la prosa reflexiva, psicológica y jurídica, las oraciones finales se subordinan frecuentemente a períodos condicionales e hipótesis sobre intenciones humanas: 'Si hubiera actuado de ese modo, habría sido únicamente para que lo perdonaran'; 'Pintó aquel cuadro al solo efecto de que alguien se asomara a su soledad interior'."
            },
            {
                "type": "table",
                "title": "Esquemas de finalidad subordinada a hipótesis",
                "rows": [
                    ["Finalidad en apódosis condicional", "'Si tuviera los recursos, crearía una fundación para que los niños huérfanos estudien'"],
                    ["Finalidad contrafáctica de pasado", "'De haber aceptado el soborno, habría sido con el fin de salvar a su familia'"],
                    ["Finalidad exclusiva ('al solo efecto de')", "'Declaró ante la prensa al solo efecto de que se conociera la verdad'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en crítica literaria y análisis psicológico",
                "items": [
                    {"spanish": "En El túnel de Sabato, Juan Pablo Castel confiesa que pintó la ventanita para que una sola persona comprendiera su angustia.", "english": "In Sabato's The Tunnel, Juan Pablo Castel confesses that he painted the little window so that one single person would understand his anguish."},
                    {"spanish": "Si el protagonista hubiera ocultado el manuscrito, habría sido para que la posteridad juzgara sus verdaderos móviles.", "english": "If the protagonist had hidden the manuscript, it would have been so that posterity would judge his true motives."},
                    {"spanish": "El juez interrogó al testigo al solo efecto de dilucidar si existía premeditación en sus actos.", "english": "The judge questioned the witness for the sole purpose of determining whether premeditation existed in his actions."}
                ]
            },
            {
                "type": "tip",
                "content": "La fórmula 'al solo efecto de + inf' o 'al solo fin de que + subj' denota un propósito exclusivo, descartando cualquier otra motivación secundaria."
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
                    ["el móvil", "motive, driving reason"],
                    ["la coartada", "alibi, pretext"],
                    ["dilucidar", "to elucidate, to clarify"],
                    ["la teleología", "doctrine of purpose, teleology"]
                ],
                "teaches": ["b2-unit12-vocab"]
            },
            {
                "id": f"{l5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Castel afirmó que pintó aquella ventanita al solo efecto de que María Iribarne __ su mensaje secreto. (descifrar - imperfecto subjuntivo)",
                "answer": "descifrara",
                "english": "Castel stated that he painted that little window for the sole purpose of María Iribarne deciphering his secret message.",
                "teaches": ["finalidad-condicional-proposito"]
            },
            {
                "id": f"{l5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz expresa la locución 'al solo efecto de' frente al conector estándar 'para'?",
                "options": [
                    "Enfatiza la exclusividad absoluta del propósito, descartando cualquier otra motivación colateral.",
                    "Indica una consecuencia no deseada provocada por un descuido fortuito.",
                    "Expresa una condición matemática aplicable únicamente a magnitudes físicas."
                ],
                "correct": 0,
                "teaches": ["finalidad-condicional-proposito"]
            },
            {
                "id": f"{l5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Pintó", "el", "cuadro", "para", "que", "alguien", "comprendiera", "su", "soledad."],
                "solution": ["Pintó", "el", "cuadro", "para", "que", "alguien", "comprendiera", "su", "soledad."],
                "english": "He painted the picture so that someone would understand his loneliness.",
                "teaches": ["finalidad-condicional-proposito"]
            },
            {
                "id": f"{l5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítico literario", "text": "¿Cuál era la verdadera finalidad de Castel al escribir su confesión desde la cárcel?"},
                    {"speaker": "Profesora", "text": "_____"},
                    {"speaker": "Crítico literario", "text": "Una trágica búsqueda de justificación ante un mundo que juzga impenetrable."}
                ],
                "options": [
                    "Escribió su relato al solo fin de que al menos una persona entendiera los móviles de su crimen y la desesperación de su alma.",
                    "Los talleres de encuadernación de Buenos Aires utilizaban cuero vacuno repujado.",
                    "El tranvía de la plaza San Martín circulaba cada quince minutos durante los días laborables."
                ],
                "correct": 0,
                "teaches": ["finalidad-condicional-proposito"]
            },
            {
                "id": f"{l5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Actuó de esa manera al solo fin de que se conociera la verdad oculta.",
                "english": "He acted in that manner for the sole purpose that the hidden truth be known.",
                "teaches": ["finalidad-condicional-proposito"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5}.json", make_lesson(
        stem=l5,
        unit_num=12,
        title="Finalidad en marcos hipotéticos y condicionales",
        goal="Master purpose clauses embedded within hypothetical frames, exclusive purpose locutions ('al solo efecto de'), and moral motive analysis.",
        grammar_desc="finalidad en períodos hipotéticos y locuciones de propósito exclusivo: al solo efecto de, al solo fin de que",
        grammar_ref=f"grammar/b2/{l5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{l5}-voc.json",
        ex_ref=f"exercises/b2/{l5}-ex.json",
        ex_ids=[f"{l5}.ex01", f"{l5}.ex02", f"{l5}.ex03", f"{l5}.ex04", f"{l5}.ex05", f"{l5}.ex06"],
        goals=[
            "Embed purpose clauses inside counterfactual and conditional periods.",
            "Deploy exclusive purpose formulas ('al solo efecto de + inf', 'al solo fin de que + subj').",
            "Analyze literary and psychological motives using teleological vocabulary (móvil, teleología, dilema)."
        ]
    ))

    # Consolidation: b2-12-consolidation
    l_con = "b2-12-consolidation"
    write_json(f"exercises/b2/{l_con}-ex.json", {
        "lesson": l_con,
        "exercises": [
            {
                "id": f"{l_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el cometido", "task, mandate, mission"],
                    ["la directriz", "guideline, directive"],
                    ["la cautela", "caution, prudence"],
                    ["el móvil", "motive, driving reason"]
                ],
                "teaches": ["b2-unit12-vocab"]
            },
            {
                "id": f"{l_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuándo debe utilizarse infinitivo en lugar de subjuntivo en una oración de finalidad?",
                "options": [
                    "Cuando el sujeto del verbo principal y el sujeto de la finalidad coinciden (correferencia).",
                    "Cuando la acción subordinada se sitúa en un pasado remoto.",
                    "Cuando el verbo principal es de mandato o influencia imperativa."
                ],
                "correct": 0,
                "teaches": ["finalidad-infinitivo-correferencia"]
            },
            {
                "id": f"{l_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo exige la locución 'a fin de que' cuando hay cambio de sujeto?",
                "options": [
                    "Modo subjuntivo siempre, rigiéndose por la correlación temporal de tiempos.",
                    "Modo indicativo si la meta ya ha sido alcanzada satisfactoriamente.",
                    "Modo imperativo afirmativo en oraciones exhortativas."
                ],
                "correct": 0,
                "teaches": ["finales-subjuntivo-a-fin-de-que"]
            },
            {
                "id": f"{l_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Se adoptaron salvaguardas estrictas para que la crisis financiera no __ el tejido productivo nacional. (destruir - imperfecto subjuntivo)",
                "answer": "destruyera",
                "english": "Strict safeguards were adopted so that the financial crisis would not destroy the national productive fabric.",
                "teaches": ["finales-negativas-para-que-no"]
            },
            {
                "id": f"{l_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "El ministerio legisló a fin de que los ciudadanos contaran con garantías plenas. [The ministry legislated so that citizens would have full guarantees.]",
                    "La directiva sesionó con el objeto de evaluar el plan de inversiones bienal. [The board met in order to evaluate the biennial investment plan.]",
                    "Se diseñó el protocolo con miras a consolidar la transición energética nacional. [The protocol was designed with a view to consolidating national energy transition.]",
                    "Se tomaron precauciones para que no se filtrara información estratégica. [Precautions were taken so that strategic information would not be leaked.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": [
                    "finales-subjuntivo-a-fin-de-que",
                    "finalidad-infinitivo-correferencia",
                    "finales-con-vistas-a-miras-a",
                    "finales-negativas-para-que-no"
                ]
            },
            {
                "id": f"{l_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Lectora", "text": "¿Cómo interpreta la obsesión de Castel por María Iribarne en El túnel?"},
                    {"speaker": "Ensayista", "text": "_____"},
                    {"speaker": "Lectora", "text": "Un desgarramiento trágico donde el deseo de comunión termina en destrucción."}
                ],
                "options": [
                    "Castel concibió su pintura con el único propósito de que alguien rescatara su alma del aislamiento absoluto del túnel existencial.",
                    "Las galerías de pintura del centro de Buenos Aires abrían de martes a sábado.",
                    "Los marcos de madera dorada se fabricaban en pequeños talleres de artesanos italianos."
                ],
                "correct": 0,
                "teaches": ["finalidad-condicional-proposito"]
            },
            {
                "id": f"{l_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se redactaron las directrices con miras a optimizar el rendimiento del equipo.",
                "english": "Guidelines were drafted with a view to optimizing team performance.",
                "teaches": ["finales-con-vistas-a-miras-a"]
            },
            {
                "id": f"{l_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta una declaración de objetivos institucionales empleando una cláusula final con subjuntivo ('a fin de que') o una locución prospectiva ('con miras a').",
                        "answer": "La institución implementó nuevos protocolos de fiscalización a fin de que los recursos públicos se asignen con absoluta transparencia y probidad."
                    }
                ],
                "teaches": ["finales-subjuntivo-a-fin-de-que"]
            }
        ]
    })

    # Classic Story for Unit 12: Ernesto Sabato - El túnel
    story_core_12 = {
        "id": "story.b2.12.sabato",
        "title": "Ernesto Sabato: El túnel",
        "level": "B2",
        "lesson": 6,
        "type": "classic",
        "estimatedMinutes": 8,
        "characters": [
            "Juan Pablo Castel",
            "María Iribarne",
            "Allende"
        ],
        "summary": "Adaptación pedagógica para nivel B2 de la célebre novela existencialista de Ernesto Sabato: la confesión de Juan Pablo Castel desde la cárcel, los propósitos inconfesables de su arte y la soledad incurable del alma humana.",
        "author": "Ernesto Sabato (Argentina, 1911–2011)",
        "work": "El túnel (1948)",
        "source": "Adaptado para estudiantes de nivel B2 a partir de la novela clásica de Ernesto Sabato",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Bastará decir que soy Juan Pablo Castel, el pintor que mató a María Iribarne. Supongo que el proceso judicial está en el recuerdo de todos y que no se necesitan mayores explicaciones sobre mi persona. Aunque ni los más benevolentes críticos de arte comprendieron jamás el sentido profundo de mis cuadros, redacto estas páginas desde mi celda con el solo propósito de que al menos una persona en este mundo entienda los móviles íntimos de mi crimen, a fin de que mi aislamiento espiritual no sea absoluto. Desprecio la vanidad mezquina de quienes escriben para vanagloriarse; mi confesión persigue un fin estrictamente teleológico: dilucidar cómo una búsqueda desesperada de comunión humana terminó desembocando en una tragedia irreparable."
            },
            {
                "type": "narration",
                "text": "Todo comenzó en el Salón de Primavera de 1946, donde expuse un cuadro titulado 'Maternidad'. Era una composición aparentemente clásica, pero en la esquina superior izquierda, a través de una ventanita diminuta, se abría una escena solitaria y desolada: una playa vacía y una mujer que contemplaba el mar embravecido como esperando algo inaccesible. Pinté esa ventanita con el objeto de que alguien descifrara la soledad que me devoraba por dentro, para que un alma afín supiera que aquel detalle marginal constituía el mensaje verdadero de mi existencia. Nadie pareció advertirlo; los críticos pasaban de largo prodigando elogios técnicos vacíos, hasta que vi a una muchacha desconocida que se detuvo fijamente ante la pequeña ventana, mirando el mar con una concentración que delataba un estremecimiento idéntico al mío."
            },
            {
                "type": "narration",
                "text": "Durante meses la busqué obsesivamente por las calles de Buenos Aires. Caminaba sin descanso entre la multitud de la calle San Martín y la plaza San Martín con el afán de encontrarla, ensayando mentalmente cientos de diálogos a fin de no espantarla en cuanto la viera. Cuando por fin tropecé con ella a la salida de un edificio de oficinas, la abordé con una mezcla de furia y torpeza, exigiéndole que me hablara de la ventanita. María Iribarne —así se llamaba— palideció y admitió con voz temblorosa que recordaba la pintura constantemente, revelándome que ella también vivía atrapada en un abismo de incomunicación."
            },
            {
                "type": "narration",
                "text": "A partir de aquel encuentro, iniciamos una relación tormentosa y desigual. Visité a María en su casona señorial, donde descubrí con estupor que estaba casada con un hombre ciego llamado Allende, individuo sereno y lúcido que aceptaba la amistad de su esposa con generosa benevolencia. Mis celos patológicos comenzaron a torturarme sin tregua: necesitaba someter a María a interrogatorios despiadados con el propósito de arrancarle certezas absolutas, a fin de que no quedara el menor resquicio de duda sobre la exclusividad de su amor. Cada una de sus vacilaciones se transformaba en una herida sangrante en mi orgullo, empujándome a redactar cartas cargadas de veneno y reproches para herirla hasta lo más profundo."
            },
            {
                "type": "narration",
                "text": "En una estancia remota donde María solía refugiarse, frente a los mismos acantilados y el mar tempestuoso que yo había pintado en mi ventanita, creí por breves instantes alcanzar la redención. Paseamos por la playa con vistas a sellar un pacto indestructible que nos protegiera de la hostilidad del mundo. Sin embargo, mi mente hiperlúcida y destructiva no podía tolerar el misterio: sospeché de inmediato que María mantenía vínculos inconfesables con su primo Hunter, interpretando cada gesto inocente como una coartada hipócrita para burlarse de mi devoción ciega."
            },
            {
                "type": "narration",
                "text": "La convicción febril de que María engañaba a todos —a su esposo ciego, a Hunter y a mí— selló su destino y el mío. Regresé a Buenos Aires como un autómata consumido por el insomnio y la desesperación. Conseguí un cuchillo de carnicero y conduje bajo la lluvia torrencial hacia la estancia con el solo fin de consumar el desenlace inevitable. Al subir a su dormitorio en la penumbra de la medianoche, le clavé el acero en el pecho susurrándole que debía matarla para que nadie más mancillara aquel secreto que solo a los dos pertenecía. Su mirada agonizante no contenía odio, sino una compasión infinita que me persigue noche y día en el encierro."
            },
            {
                "type": "narration",
                "text": "Ahora comprendo la verdad atroz que rigió mi destino: todos los seres humanos habitan sus propios túneles individuales, oscuros y paralelos, a lo largo de los cuales transitamos desde la infancia hasta la muerte. Yo había creído ingenuamente que María viajaba por otro túnel paralelo al mío y que nuestras ventanas se habían cruzado por un prodigio del destino; pero en realidad mi túnel siempre estuvo cerrado por murallas de cristal impenetrable. Escribo estas memorias para que quede constancia de mi desastre, sabiendo que mientras los muros de la prisión me resguardan del mundo exterior, mi espíritu continuará encerrado para siempre en la soledad más implacable."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál era la verdadera finalidad de la ventanita en el cuadro 'Maternidad' de Juan Pablo Castel?",
                        "options": [
                            "Transmitir su soledad interior para que un alma afín descifrara el mensaje profundo de su existencia.",
                            "Demostrar a los críticos académicos su maestría en la perspectiva óptica geométrica.",
                            "Publicitar las playas vírgenes del sur bonaerense para incentivar el turismo.",
                            "Cumplir con un encargo religioso contratado por una cofradía de la catedral."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que Castel pintó la escena marginal de la ventana para que alguien sintiera la misma soledad y descifrara su verdadero ser."
                    },
                    {
                        "question": "¿Qué patología psicológica destruyó la posibilidad de comunión entre Castel y María Iribarne?",
                        "options": [
                            "Sus celos obsesivos e interrogatorios despiadados para exigir certezas de fidelidad absoluta.",
                            "Su adicción incontrolable al juego de cartas en los clubes del puerto de Buenos Aires.",
                            "Su negativa absoluta a vender obras de arte a coleccionistas extranjeros.",
                            "Su fobia insuperable a viajar en ferrocarril hacia la campiña pampeana."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 detalla cómo los celos patológicos de Castel y sus inquisiciones constantes arruinaron la relación al buscar una exclusividad asfixiante."
                    },
                    {
                        "question": "¿Qué metáfora existencial sintetiza la desolada conclusión de Castel al final de su relato?",
                        "options": [
                            "La certidumbre de que cada ser humano vive recluido en su propio túnel oscuro e impenetrable.",
                            "La comparación de la sociedad con un tablero de ajedrez donde el azar decide los destinos.",
                            "La visión de la historia humana como un laberinto circular sin salida ética posible.",
                            "La convicción de que el arte pictórico reemplaza plenamente a la justicia de los tribunales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 7 expone la célebre metáfora del túnel: la imposibilidad de salir del aislamiento individual y la incomunicación radical entre las almas."
                    }
                ]
            }
        }
    }
    write_json(f"stories/classics/b2/b2-12.json", story_core_12)

    write_json(f"lessons/b2/{l_con}.json", make_consolidation_lesson(
        stem=l_con,
        unit_num=12,
        title="Unit 12 Consolidation: Finality, Purpose & Institutional Goals",
        goal="Consolidate purpose clauses (para que, a fin de que), infinitive coreference, negative purpose, and prospective planning through literary analysis of Sabato's 'El túnel'.",
        grammar_desc="síntesis de oraciones de finalidad con subjuntivo e infinitivo, locuciones prospectivas (con miras a) y propósitos exclusivos",
        ex_ref=f"exercises/b2/{l_con}-ex.json",
        ex_ids=[f"{l_con}.ex01", f"{l_con}.ex02", f"{l_con}.ex03", f"{l_con}.ex04", f"{l_con}.ex05", f"{l_con}.ex06", f"{l_con}.ex07", f"{l_con}.ex08"],
        goals=[
            "Formulate complex purpose clauses differentiating coreference (infinitive) from change of subject (subjunctive).",
            "Deploy forward-looking locutions ('con miras a', 'con vistas a') and exclusive purpose ('al solo efecto de').",
            "Construct negative preventive purpose structures ('para que no + subj').",
            "Analyze teleological and existential motives in Ernesto Sabato's 'El túnel'."
        ],
        checklist_items=[
            "I can formulate purpose clauses with 'a fin de que' and 'para que' using correct subjunctive sequence.",
            "I can apply the coreference rule with 'para + infinitivo' and 'con el objeto de + infinitivo'.",
            "I can employ prospective connectors ('con miras a', 'con vistas a') in strategic planning.",
            "I can express preventive caution using negative purpose clauses ('para que no')."
        ],
        story_ref=f"stories/classics/b2/b2-12.json"
    ))
    print("Completed Core Unit 12 generation!")

    # -------------------------------------------------------------------------
    # REGIONAL TRACK UNIT 12 (b2-puertorico): Puerto Rico: Boricua Identity, Sovereignty & Defiance
    # -------------------------------------------------------------------------

    # Lesson 1: b2-puertorico-01 - El Yunque, los carso norteños y las bahías bioluminiscentes
    lc1 = "b2-puertorico-01"
    write_json(f"vocabulary/b2/{lc1}-voc.json", {
        "id": "vocab.b2.puertorico.01",
        "lesson": lc1,
        "title": "Ecosistemas boricuas: bosque pluvial, carso y bioluminiscencia",
        "theme": "Vocabulario de bosque nublado, dinoflagelados y geomorfología caribeña",
        "words": [
            {"lemma": "el mogote", "translation": "karst limestone hill", "pos": "noun"},
            {"lemma": "el coquí", "translation": "coqui (endemic Puerto Rican tree frog)", "pos": "noun"},
            {"lemma": "la bioluminiscencia", "translation": "bioluminescence", "pos": "noun"},
            {"lemma": "el carso", "translation": "karst topography", "pos": "noun"},
            {"lemma": "el sumidero", "translation": "sinkhole", "pos": "noun"},
            {"lemma": "la laurisilva", "translation": "laurel forest, rain cloud forest", "pos": "noun"},
            {"lemma": "endémico", "translation": "endemic, native", "pos": "adjective"},
            {"lemma": "el estuario", "translation": "estuary", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{lc1}-a-gr.json", {
        "id": "grammar.b2.puertorico.01.yunque-bioluminiscencia",
        "title": "El Yunque, los carso norteños y las bahías bioluminiscentes",
        "sections": [
            {
                "type": "text",
                "title": "Descripción científica y geomorfológica del patrimonio boricua",
                "content": "La caracterización del patrimonio natural puertorriqueño en nivel B2 moviliza recursos de precisión descriptiva y ecológica: oraciones adjetivas compuestas ('en cuyos cursos fluviales habita el coquí dorado'), pasivas reflejas de proceso ambiental ('se protegen los manglares para que los dinoflagelados prosperen') y adjetivación técnica de relieve."
            },
            {
                "type": "table",
                "title": "Santuarios naturales emblemáticos de Puerto Rico",
                "rows": [
                    ["El Yunque (Sierra de Luquillo)", "Único bosque pluvial tropical del Sistema Nacional de Bosques de EE. UU."],
                    ["Carso norteño y Río Camuy", "Red de cavernas kársticas y sumideros gigantes entre las más extensas del planeta"],
                    ["Bahía Mosquito (Vieques)", "La bahía bioluminiscente más brillante del mundo, poblada por Pyrodinium bahamense"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en estudios botánicos y oceanográficos",
                "items": [
                    {"spanish": "El canto nocturno del coquí (Eleutherodactylus coqui) constituye el símbolo sonoro más amado de la identidad boricua.", "english": "The nocturnal call of the coqui (Eleutherodactylus coqui) constitutes the most beloved sound symbol of Boricua identity."},
                    {"spanish": "En la bahía de Puerto Mosquito en Vieques, cada litro de agua alberga más de ciento sesenta mil dinoflagelados luminiscentes.", "english": "In Puerto Mosquito Bay in Vieques, each liter of water harbors over one hundred and sixty thousand luminescent dinoflagellates."},
                    {"spanish": "El parque de las Cavernas del Río Camuy protege un laberinto subterráneo horadado por aguas milenarias en la caliza.", "english": "The Rio Camuy Cave Park protects an underground labyrinth carved by ancient waters into the limestone."}
                ]
            },
            {
                "type": "tip",
                "content": "Para enriquecer la prosa descriptiva científica, sustituye adjetivos comunes por términos botánicos y geológicos específicos: 'pluviosidad torrencial', 'estratificación arbórea', 'formación kárstica', 'organismo bioluminiscente'."
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
                    ["el coquí", "endemic Puerto Rican tree frog"],
                    ["la bioluminiscencia", "bioluminescence"],
                    ["el carso", "karst topography"],
                    ["el sumidero", "sinkhole"]
                ],
                "teaches": ["b2-puertorico-vocab"]
            },
            {
                "id": f"{lc1}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué singularidad ecológica distingue a la bahía de Mosquito en la isla municipio de Vieques?",
                "options": [
                    "Es reconocida como la bahía bioluminiscente más brillante del planeta debido a la densidad de dinoflagelados.",
                    "Es el único cráter de impacto de meteorito submarino accesible para buceadores deportivos.",
                    "Es una laguna hipersalina habitada exclusivamente por colonias de pingüinos antárticos."
                ],
                "correct": 0,
                "teaches": ["puertorico-biodiversidad-yunque-bioluminiscencia"]
            },
            {
                "id": f"{lc1}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El bosque nacional El Yunque __ una biodiversidad vegetal única con más de doscientas especies de árboles autóctonos. (albergar - presente indicativo)",
                "answer": "alberga",
                "english": "El Yunque National Forest harbors a unique plant biodiversity with over two hundred native tree species.",
                "teaches": ["puertorico-biodiversidad-yunque-bioluminiscencia"]
            },
            {
                "id": f"{lc1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "canto", "del", "coquí", "resuena", "en", "las", "noches", "boricuas."],
                "solution": ["El", "canto", "del", "coquí", "resuena", "en", "las", "noches", "boricuas."],
                "english": "The call of the coqui resonates in Puerto Rican nights.",
                "teaches": ["puertorico-biodiversidad-yunque-bioluminiscencia"]
            },
            {
                "id": f"{lc1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ecóloga", "text": "¿Por qué es tan delicado el equilibrio ecológico de las bahías bioluminiscentes?"},
                    {"speaker": "Oceanógrafo", "text": "_____"},
                    {"speaker": "Ecóloga", "text": "Una razón contundente para regular con rigor el turismo y proteger los manglares."}
                ],
                "options": [
                    "Porque los dinoflagelados requieren aguas protegidas con aporte constante de nutrientes de los mangles y ausencia de contaminación lumínica.",
                    "Porque los arrecifes de coral crecen más rápido cuando las corrientes marinas son cálidas y profundas.",
                    "Porque las lanchas de motor aumentan la visibilidad de los peces durante las faenas de pesca artesanal."
                ],
                "correct": 0,
                "teaches": ["puertorico-biodiversidad-yunque-bioluminiscencia"]
            },
            {
                "id": f"{lc1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las aguas de Vieques resplandecen en la noche gracias a microorganismos marinos.",
                "english": "The waters of Vieques glow at night thanks to marine microorganisms.",
                "teaches": ["puertorico-biodiversidad-yunque-bioluminiscencia"]
            }
        ]
    })

    # Regional Story 1: b2-puertorico-01.json
    story_pr_01 = {
        "id": "b2-puertorico-01",
        "title": "El Yunque, los carso norteños y las bahías bioluminiscentes",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica ecológica y geográfica de nivel B2 sobre los santuarios naturales de Puerto Rico: la selva pluvial de El Yunque, las cavernas del río Camuy en el carso norteño y el milagro nocturno de las bahías bioluminiscentes en Vieques.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Conocida poéticamente por sus habitantes ancestrales como 'Borikén' —la 'tierra del altivo señor' que daría origen al gentilicio entrañable de boricua—, la isla de Puerto Rico despliega en sus apenas nueve mil kilómetros cuadrados una densidad ecológica y geológica verdaderamente asombrosa. Situada en el arco oriental de las Antillas Mayores, entre el profundo abismo atlántico de la fosa de Puerto Rico y las aguas templadas del mar Caribe, la isla alberga una extraordinaria variedad de microclimas que transitan desde el verdor perpetuo de sus selvas pluviales de montaña hasta la extrema sequedad de los bosques espinosos del litoral suroeste en Guánica."
            },
            {
                "type": "narration",
                "text": "En el extremo nororiental de la cordillera insular se alza la sierra de Luquillo, hogar del legendario Bosque Nacional El Yunque, el único bosque pluvial tropical integrado en el Sistema Forestal Nacional de los Estados Unidos. Bautizado por los indígenas taínos como el trono sagrado de su dios benévolo Yuquiyú, este santuario montañoso recibe precipitaciones torrenciales que superan los cinco mil milímetros anuales, alimentando cascadas majestuosas como La Mina y arroyos de aguas cristalinas que descienden entre helechos gigantes de diez metros de altura y palmas de sierra milenarias. En las copas frondosas de sus árboles habita la críticamente amenazada cotorra puertorriqueña (Amazona vittata) y el diminuto 'coquí' (Eleutherodactylus coqui), anfibio endémico cuyo canto nocturno inconfundible —un agudo y melodioso '¡co-quí, co-quí!'— resuena como el latido sonoro primordial de la noche insular."
            },
            {
                "type": "narration",
                "text": "Hacia el noroeste de la isla, la geografía cede su paso a un prodigio geomorfológico absolutamente singular: la franja del carso norteño. Formada por depósitos de caliza marina del período Terciario levantados por fuerzas tectónicas y esculpidos durante millones de años por la disolución implacable de las lluvias tropicales, esta región presenta un laberinto sobrecogedor de 'mogotes' cónicos cubiertos de selva y colosales 'sumideros' que se abren como simas profundas en la tierra. En este karst se encuentra el parque de las Cavernas del Río Camuy, uno de los sistemas de cuevas subterráneas más extensos del hemisferio occidental, por cuyas galerías ciclópeas discurre el tercer río subterráneo más caudaloso del mundo entre catedrales de estalagmitas y abismos naturales que cortan la respiración del visitante."
            },
            {
                "type": "narration",
                "text": "La riqueza natural de Puerto Rico alcanza su cota más mágica y poética en sus litorales marítimos a través del fenómeno de la bioluminiscencia marina. Aunque existen tres bahías bioluminiscentes permanentes en el archipiélago —Laguna Grande en Fajardo, La Parguera en Lajas y Puerto Mosquito en la isla municipio de Vieques—, es esta última la que ostenta el récord mundial Guinness como la más brillante del planeta. Protegida por una estrecha boca de entrada que impide la dispersión de sus aguas hacia el mar abierto y rodeada por densos bosques de mangle rojo, la bahía alberga una concentración asombrosa de dinoflagelados (Pyrodinium bahamense), microorganismos unicelulares que emiten un destello azul verdoso brillante cuando el agua se agita por el movimiento de los peces o el avance silencioso de los remos."
            },
            {
                "type": "narration",
                "text": "Bañarse o navegar en Puerto Mosquito durante una noche sin luna supone adentrarse en una experiencia casi sobrenatural: cada brazada desata estelas de luz plateada que parecen estrellas líquidas, mientras los bancos de peces huyen dejando trazos luminosos en la oscuridad abisal como relámpagos bajo el agua. La subsistencia de este ecosistema depende de un equilibrio ecológico sumamente frágil: las hojas en descomposición del mangle rojo aportan los taninos y nutrientes esenciales que alimentan a los microorganismos, exigiendo una protección ambiental inflexible contra la contaminación química y la intrusión lumínica costera."
            },
            {
                "type": "narration",
                "text": "En el extremo opuesto, en la costa suroeste de Guánica, se extiende el Bosque Seco, declarado Reserva de la Biosfera por la UNESCO en 1981. En marcado contraste con la pluviosidad de El Yunque, este ecosistema semiárido recibe menos de ochocientos milímetros de lluvia al año debido a la barrera orográfica de la cordillera Central, albergando una vegetación espinosa adaptada a la sequía extrema donde proliferan cactáceas columnares y una rica avifauna endémica como el guabairo y el zumbador verde."
            },
            {
                "type": "narration",
                "text": "Esta fascinante diversidad biogeográfica constituye el sustrato material sobre el cual se forjó la sensibilidad del pueblo puertorriqueño: una profunda devoción por la tierra fértil, un orgullo visceral por su fauna endémica y un compromiso creciente con la preservación de un patrimonio natural que, frente a las presiones de la especulación inmobiliaria y los embates de huracanes atlánticos cada vez más intensos, demanda una férrea custodia colectiva para asegurar el porvenir de las futuras generaciones boricuas."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singularidad institucional y ecológica distingue al bosque pluvial de El Yunque?",
                        "options": [
                            "Es el único bosque pluvial tropical integrado en el Sistema Forestal Nacional de los Estados Unidos.",
                            "Es el único bosque caribeño donde no existen cursos fluviales ni cascadas naturales.",
                            "Es un parque gestionado exclusivamente por la marina de guerra para ejercicios tácticos.",
                            "Es un volcán activo cuya cumbre permanece nevada durante los meses de invierno."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 precisa que El Yunque es el único bosque tropical lluvioso del Sistema de Bosques de EE. UU."
                    },
                    {
                        "question": "¿Por qué la bahía de Puerto Mosquito en Vieques está registrada como la más brillante del mundo?",
                        "options": [
                            "Por la altísima concentración de dinoflagelados luminiscentes protegidos por manglares en una bahía de boca estrecha.",
                            "Por la instalación de reflectores solares submarinos para promover la investigación nocturna.",
                            "Por la presencia de minerales radiactivos naturales en la arena de sus playas vírgenes.",
                            "Por el reflejo artificial de los rascacielos residenciales construidos en su litoral."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 detalla que la bahía alberga una densidad récord de dinoflagelados alimentados por los nutrientes del mangle rojo."
                    },
                    {
                        "question": "¿Qué contraste climático extremo existe entre El Yunque y el Bosque Seco de Guánica en Puerto Rico?",
                        "options": [
                            "El Yunque recibe más de 5000 mm de lluvia al año, mientras Guánica es un ecosistema semiárido con menos de 800 mm.",
                            "El Yunque es una llanura desértica salina y Guánica es un glaciar de alta montaña.",
                            "El Yunque carece de vegetación arbórea y Guánica es una selva impenetrable de bambú gigante.",
                            "El Yunque sufre heladas continuas y Guánica mantiene una temperatura constante bajo cero."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los párrafos 2 y 6 contraponen la extrema pluviosidad tropical de El Yunque con la aridez orográfica del Bosque Seco de Guánica."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc1}.json", story_pr_01)

    write_json(f"lessons/b2/{lc1}.json", make_lesson(
        stem=lc1,
        unit_num=12,
        title="El Yunque, los carso norteños y las bahías bioluminiscentes",
        goal="Analyze Puerto Rico's tropical rainforest ecosystems, karst cave systems, and bioluminescent bays using precise ecological and descriptive registers.",
        grammar_desc="oraciones adjetivas de relieve, pasivas reflejas de procesos ambientales y terminología ecológica boricua",
        grammar_ref=f"grammar/b2/{lc1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc1}-voc.json",
        ex_ref=f"exercises/b2/{lc1}-ex.json",
        ex_ids=[f"{lc1}.ex01", f"{lc1}.ex02", f"{lc1}.ex03", f"{lc1}.ex04", f"{lc1}.ex05", f"{lc1}.ex06"],
        goals=[
            "Examine the biodiversity of El Yunque rainforest and the endemic coquí tree frog.",
            "Analyze the karst topography of Rio Camuy cave system and the limestone mogotes.",
            "Deploy environmental vocabulary (coquí, bioluminiscencia, carso, sumidero, estuario)."
        ],
        story_ref=f"stories/world/b2/{lc1}.json"
    ))

    # Lesson 2: b2-puertorico-02 - El Grito de Lares y la cesión colonial de 1898
    lc2 = "b2-puertorico-02"
    write_json(f"vocabulary/b2/{lc2}-voc.json", {
        "id": "vocab.b2.puertorico.02",
        "lesson": lc2,
        "title": "Emancipación boricua, el Grito de Lares y el impacto de 1898",
        "theme": "Vocabulario de insurrección patriótica, cesión territorial y tratados internacionales",
        "words": [
            {"lemma": "el grito", "translation": "revolutionary call/cry (Grito de Lares)", "pos": "noun"},
            {"lemma": "la cesión", "translation": "cession, transfer of sovereignty", "pos": "noun"},
            {"lemma": "el botín", "translation": "booty, spoils of war", "pos": "noun"},
            {"lemma": "la soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "la abolición", "translation": "abolition", "pos": "noun"},
            {"lemma": "el insurrecto", "translation": "insurgent, rebel", "pos": "noun"},
            {"lemma": "tutelar", "translation": "tutelar, supervisory", "pos": "adjective"},
            {"lemma": "despojar", "translation": "to strip, to dispossess", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{lc2}-a-gr.json", {
        "id": "grammar.b2.puertorico.02.grito-lares-cesion",
        "title": "El Grito de Lares y la cesión colonial de 1898",
        "sections": [
            {
                "type": "text",
                "title": "Discurso historiográfico y análisis de transiciones imperiales",
                "content": "El examen histórico de la rebelión independentista de 1868 y la posterior invasión militar estadounidense de 1898 en nivel B2 articula relaciones de causa y desenlace ('tras el armisticio de la guerra hispano-estadounidense', 'en virtud del Tratado de París firmado en diciembre de 1898') e hipótesis contrafácticas sobre la autonomía insular frustrada."
            },
            {
                "type": "table",
                "title": "Hitos decisivos de la historia política decimonónica",
                "rows": [
                    ["El Grito de Lares (23 de septiembre de 1868)", "Insurrección independentista liderada ideológicamente por Ramón Emeterio Betances"],
                    ["La Carta Autonómica (1897)", "Régimen de autogobierno democrático concedido por la corona española a la isla"],
                    ["El Tratado de París (1898)", "Cesión forzosa de Puerto Rico, Guam y Filipinas a los Estados Unidos como botín bélico"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en ensayos historiográficos puertorriqueños",
                "items": [
                    {"spanish": "Ramón Emeterio Betances proclamó desde el exilio los 'Diez Mandamientos de los Hombres Libres' en favor de la abolición y la libertad.", "english": "Ramón Emeterio Betances proclaimed from exile the 'Ten Commandments of Free Men' in favor of abolition and liberty."},
                    {"spanish": "Lola Rodríguez de Tió bordó la bandera de Lares y escribió los versos revolucionarios del himno patrio La Borinqueña.", "english": "Lola Rodríguez de Tió embroidered the Lares flag and wrote the revolutionary verses of the patriotic anthem La Borinqueña."},
                    {"spanish": "De no haberse producido la intervención militar de 1898, Puerto Rico habría consolidado su régimen autonómico parlamentario.", "english": "Had the 1898 military intervention not occurred, Puerto Rico would have consolidated its parliamentary autonomic regime."}
                ]
            },
            {
                "type": "tip",
                "content": "Para relatar hechos de soberanía y diplomacia internacional en registro formal, utiliza sustantivos jurídicos de precisión: 'tratado de paz', 'cesión territorial incondicional', 'administración militar tutelar', 'estatus no incorporado'."
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
                    ["la cesión", "cession, transfer of sovereignty"],
                    ["el botín", "spoils of war, booty"],
                    ["el insurrecto", "insurgent, rebel"],
                    ["tutelar", "tutelar, supervisory"]
                ],
                "teaches": ["b2-puertorico-vocab"]
            },
            {
                "id": f"{lc2}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué trascendencia histórica tuvo el Grito de Lares del 23 de septiembre de 1868 en Puerto Rico?",
                "options": [
                    "Fue la primera insurrección armada que proclamó la República de Puerto Rico y la abolición inmediata de la esclavitud.",
                    "Fue una huelga marítima organizada por los pescadores de langostas de la bahía de San Juan.",
                    "Fue una asamblea constituyente que aprobó la anexión voluntaria al imperio británico."
                ],
                "correct": 0,
                "teaches": ["puertorico-grito-lares-cesion-1898"]
            },
            {
                "id": f"{lc2}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En virtud del Tratado de París de 1898, España __ la soberanía de Puerto Rico a los Estados Unidos sin consultar a la población insular. (ceder - pretérito indefinido)",
                "answer": "cedió",
                "english": "Under the Treaty of Paris of 1898, Spain ceded sovereignty of Puerto Rico to the United States without consulting the island population.",
                "teaches": ["puertorico-grito-lares-cesion-1898"]
            },
            {
                "id": f"{lc2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Grito", "de", "Lares", "proclamó", "la", "libertad", "de", "la", "patria."],
                "solution": ["El", "Grito", "de", "Lares", "proclamó", "la", "libertad", "de", "la", "patria."],
                "english": "The Grito de Lares proclaimed the freedom of the homeland.",
                "teaches": ["puertorico-grito-lares-cesion-1898"]
            },
            {
                "id": f"{lc2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora", "text": "¿Por qué el año 1898 representó una ruptura tan traumática para Puerto Rico?"},
                    {"speaker": "Profesor", "text": "_____"},
                    {"speaker": "Historiadora", "text": "Una paradoja colonial que postergó indefinidamente la autodeterminación democrática del pueblo boricua."}
                ],
                "options": [
                    "Porque la isla acababa de inaugurar su Carta Autonómica democrática cuando fue ocupada militarmente y transferida como botín de guerra sin consulta popular.",
                    "Porque se produjo un eclipse solar que dañó las cosechas de plátanos y café en la cordillera.",
                    "Porque el puerto comercial de Ponce fue clausurado para el tránsito de barcos veleros."
                ],
                "correct": 0,
                "teaches": ["puertorico-grito-lares-cesion-1898"]
            },
            {
                "id": f"{lc2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Betances defendió incansablemente la emancipación de las Antillas desde el exilio.",
                "english": "Betances tirelessly defended the emancipation of the Antilles from exile.",
                "teaches": ["puertorico-grito-lares-cesion-1898"]
            }
        ]
    })

    # Regional Story 2: b2-puertorico-02.json
    story_pr_02 = {
        "id": "b2-puertorico-02",
        "title": "El Grito de Lares y la cesión colonial de 1898",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica histórica de nivel B2 sobre las encrucijadas de la soberanía puertorriqueña: la gesta libertaria del Grito de Lares en 1868, el pensamiento emancipador de Betances, la Carta Autonómica y el trauma de la cesión imperial de 1898.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A lo largo de cuatro centurias de dominación imperial española, la sociedad puertorriqueña fue forjando una conciencia identitaria singular que maduró lentamente entre las plantaciones cafetaleras de la cordillera Central y los puertos mercantiles del litoral. A diferencia de las colonias del continente sudamericano que alcanzaron su independencia en las primeras décadas del siglo XIX, las Antillas hispanas permanecieron atadas a la metrópoli bajo un régimen militar restrictivo. Sin embargo, el descontento ante las exacciones fiscales de la corona, la imposición del opresivo 'régimen de la libreta' que obligaba a los jornaleros libres a trabajar forzosamente para los terratenientes y la persistencia atroz de la esclavitud negra terminaron por prender la mecha de la rebelión armada."
            },
            {
                "type": "narration",
                "text": "La noche del 23 de septiembre de 1868 estalló en el poblado montañoso de Lares la gesta libertaria más emblemática de la historia patria boricua: el 'Grito de Lares'. Planificado minuciosamente desde el destierro por el médico, cirujano y patriota Ramón Emeterio Betances —considerado el 'Padre de la Patria'— y por el hacendado Segundo Ruiz Belvis, varios cientos de patriotas armados con machetes y viejos fusiles asaltaron la alcaldía, derrocaron a las autoridades españolas y proclamaron en la plaza pública la República de Puerto Rico, enarbolando por primera vez la bandera tricolor tejida por la insigne poeta Mariana Bracetti con una cruz blanca sobre campos azul y rojo y una estrella solitaria."
            },
            {
                "type": "narration",
                "text": "Entre los primeros decretos promulgados por el gobierno republicano provisional de Lares figuró la abolición inmediata de la libreta de jornaleros y la emancipación automática de todos los esclavos que se sumaran a la lucha patriótica. Aunque la sublevación fue sofocada apenas veinticuatro horas después por las tropas regulares del ejército español en las inmediaciones del pueblo de San Sebastián, el sacrificio heroico de los insurrectos dejó una huella imborrable en el alma colectiva, forzando a la metrópoli a conceder reformas políticas urgentes y acelerando la abolición definitiva de la esclavitud en la isla en marzo de 1873."
            },
            {
                "type": "narration",
                "text": "Tres décadas de intensa lucha parlamentaria y cívica liderada por figuras ilustres como Luis Muñoz Rivera culminaron a fines de 1897 con un triunfo democrático sin precedentes: la promulgación por la reina regente María Cristina de la Carta Autonómica de Puerto Rico. Este estatuto de autogobierno de vanguardia dotó a la isla de un parlamento bicameral insular con plenos poderes legislativos, presupuesto propio y representación con voz y voto en las Cortes de Madrid, alcanzando la mayor cuota de soberanía política de su historia colonial."
            },
            {
                "type": "narration",
                "text": "Aquel florecimiento democrático autónomo resultó dolorosamente efímero. Apenas ocho meses después de instalarse el gobierno parlamentario insular, en el contexto de la guerra hispano-estadounidense desatada tras la misteriosa explosión del acorazado Maine en el puerto de La Habana, tropas de infantería de la armada de los Estados Unidos al mando del general Nelson A. Miles desembarcaron por sorpresa en la bahía sureña de Guánica el 25 de julio de 1898, iniciando la ocupación militar de Puerto Rico bajo la promesa solemne de 'traer las libertades de las instituciones americanas'."
            },
            {
                "type": "narration",
                "text": "Sin embargo, las esperanzas de quienes acogieron a las tropas extranjeras como liberadoras se desvanecieron con crudeza cuando las superpotencias negociaron la paz en Europa. Mediante el Tratado de París suscrito el 10 de diciembre de 1898 a espaldas del pueblo boricua y sin la presencia de un solo delegado insular en la mesa de negociaciones, España cedió formalmente la soberanía de Puerto Rico, Guam y Filipinas a los Estados Unidos como indemnización y botín de guerra, clausurando la naciente autonomía democrática y sustituyéndola por un régimen de tutela militar administrado directamente desde Washington."
            },
            {
                "type": "narration",
                "text": "La posterior aprobación de la Ley Foraker en 1900 consagró la condición jurídica de Puerto Rico como un 'territorio no incorporado' perteneciente a, pero no parte de, los Estados Unidos, doctrina convalidada cínicamente por la Corte Suprema estadounidense en los célebres 'Casos Insulares' al calificar a los puertorriqueños como 'habitantes de una isla habitada por razas foráneas'. Así se inauguró una prolongada y dolorosa encrucijada colonial que, transitando de un imperio declinante a una potencia hegemónica en ascenso, ha condicionado hasta el presente la incansable búsqueda del pueblo boricua por conquistar su plena autodeterminación y dignidad soberana."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Quién fue el principal ideólogo y organizador de la gesta patriótica del Grito de Lares en 1868?",
                        "options": [
                            "El médico y patriota Ramón Emeterio Betances desde el destierro internacional.",
                            "El general confederado Robert E. Lee tras refugiarse en la cordillera Central.",
                            "El almirante español Cristóbal Colón a través de cartas testadas desde Sevilla.",
                            "El líder sindical minero Santiago Iglesias Pantín desde las minas de carbón."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 identifica al doctor Ramón Emeterio Betances como el gran organizador e ideólogo del Grito de Lares."
                    },
                    {
                        "question": "¿Qué importante conquista política representó la Carta Autonómica de 1897 para Puerto Rico?",
                        "options": [
                            "Dotó a la isla de un parlamento bicameral con plenas facultades de autogobierno y presupuesto propio.",
                            "Estableció la venta obligatoria de todas las plantaciones de tabaco a bancos de Londres.",
                            "Impuso el servicio militar obligatorio exclusivo en los cuarteles de las islas Filipinas.",
                            "Clausuró las elecciones municipales y designó alcaldes vitalicios nombrados por el Vaticano."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 destaca que la Carta Autonómica de 1897 otorgó a la isla un régimen parlamentario propio con amplia soberanía democrática."
                    },
                    {
                        "question": "¿Cómo se definió el destino político de Puerto Rico en el Tratado de París de diciembre de 1898?",
                        "options": [
                            "España cedió la soberanía de la isla a los Estados Unidos como botín de guerra sin consultar al pueblo boricua.",
                            "Se declaró la independencia inmediata bajo la protección armada de la confederación antillana.",
                            "Se acordó un plebiscito supervisado por diplomáticos suizos para elegir la anexión a Francia.",
                            "Se reconoció la soberanía del parlamento autonómico insular como república asociada."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 relata que en el Tratado de París de 1898 España traspasó la isla a EE. UU. como indemnización bélica a espaldas de la ciudadanía insular."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc2}.json", story_pr_02)

    write_json(f"lessons/b2/{lc2}.json", make_lesson(
        stem=lc2,
        unit_num=12,
        title="El Grito de Lares y la cesión colonial de 1898",
        goal="Analyze the 1868 Grito de Lares insurrection, Betances' anti-colonial thought, and the 1898 Treaty of Paris using historical and legal registers.",
        grammar_desc="narrativa historiográfica sobre soberanía, análisis del derecho colonial y oraciones de transición imperial",
        grammar_ref=f"grammar/b2/{lc2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc2}-voc.json",
        ex_ref=f"exercises/b2/{lc2}-ex.json",
        ex_ids=[f"{lc2}.ex01", f"{lc2}.ex02", f"{lc2}.ex03", f"{lc2}.ex04", f"{lc2}.ex05", f"{lc2}.ex06"],
        goals=[
            "Trace the causes and ideals of the 1868 Grito de Lares.",
            "Analyze the democratic scope of the 1897 Carta Autonómica and the impact of the 1898 invasion.",
            "Deploy sovereignty and legal terminology (grito, cesión, botín, tutela, despojar)."
        ],
        story_ref=f"stories/world/b2/{lc2}.json"
    ))

    # Lesson 3: b2-puertorico-03 - El Estado Libre Asociado: El debate insular interminable
    lc3 = "b2-puertorico-03"
    write_json(f"vocabulary/b2/{lc3}-voc.json", {
        "id": "vocab.b2.puertorico.03",
        "lesson": lc3,
        "title": "El Estado Libre Asociado, partidos políticos y dilemas de estatus",
        "theme": "Vocabulario de derecho constitucional insular, estadidad e independencia",
        "words": [
            {"lemma": "el estatus", "translation": "political status", "pos": "noun"},
            {"lemma": "la estadidad", "translation": "statehood (pro-US state position)", "pos": "noun"},
            {"lemma": "el plebiscito", "translation": "plebiscite, referendum", "pos": "noun"},
            {"lemma": "la soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "la ciudadanía", "translation": "citizenship", "pos": "noun"},
            {"lemma": "el pacto", "translation": "compact, covenant", "pos": "noun"},
            {"lemma": "el nacionalismo", "translation": "nationalism", "pos": "noun"},
            {"lemma": "anexionista", "translation": "annexationist, pro-statehood", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{lc3}-a-gr.json", {
        "id": "grammar.b2.puertorico.03.estado-libre-asociado",
        "title": "El Estado Libre Asociado: El debate insular interminable",
        "sections": [
            {
                "type": "text",
                "title": "Análisis constitucional y debate sobre fórmulas descolonizadoras",
                "content": "El examen del estatus político puertorriqueño en nivel B2 requiere articular estructuras argumentativas complejas y períodos condicionales hipotéticos: 'si Puerto Rico fuera admitido como el estado 51 de la unión, sus representantes tendrían plenos derechos de voto en el Congreso federal'; 'si bien la Constitución de 1952 dotó a la isla de autogobierno interno, el poder plenario del Congreso estadounidense permanece intacto en virtud de la cláusula territorial'."
            },
            {
                "type": "table",
                "title": "Las tres posturas tradicionales del estatus insular",
                "rows": [
                    ["Estado Libre Asociado (ELA)", "Defendido por el PPD: autogobierno interno con pacto de unión permanente y ciudadanía"],
                    ["Estadidad (Statehood)", "Defendida por el PNP: integración plena como estado federado con representación congresional"],
                    ["Independencia / Soberanía libre", "Defendida por el PIP y movimientos soberanistas: república libre e independiente"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate constitucional boricua",
                "items": [
                    {"spanish": "Luis Muñoz Marín impulsó la creación del Estado Libre Asociado en 1952 para modernizar la economía insular.", "english": "Luis Muñoz Marín championed the creation of the Commonwealth in 1952 to modernize the island economy."},
                    {"spanish": "Pedro Albizu Campos lideró el Partido Nacionalista defendiendo la tesis de que la cesión de 1898 carecía de validez jurídica.", "english": "Pedro Albizu Campos led the Nationalist Party arguing that the 1898 cession lacked legal validity."},
                    {"spanish": "Los sucesivos plebiscitos sobre el estatus han reflejado una sociedad profundamente dividida sobre su destino político.", "english": "Successive plebiscites on status have reflected a society deeply divided over its political destiny."}
                ]
            },
            {
                "type": "tip",
                "content": "Para analizar debates de estatus con la neutralidad exigida por el nivel B2, utiliza conectores de ponderación imparcial: 'por una parte los partidarios sostienen que', 'en contraposición los sectores críticos argumentan que'."
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
                    ["el estatus", "political status"],
                    ["la estadidad", "statehood (US state)"],
                    ["el plebiscito", "plebiscite, referendum"],
                    ["anexionista", "annexationist, pro-statehood"]
                ],
                "teaches": ["b2-puertorico-vocab"]
            },
            {
                "id": f"{lc3}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué fórmula jurídica e institucional se consagró en Puerto Rico con la Constitución de 1952?",
                "options": [
                    "El Estado Libre Asociado (Commonwealth), que otorgó autogobierno interno en unión permanente con EE. UU.",
                    "La independencia absoluta y la proclamación de una república presidencialista no alineada.",
                    "La cesión temporal de la administración a una comisión militar mixta de las Naciones Unidas."
                ],
                "correct": 0,
                "teaches": ["puertorico-estado-libre-asociado-debate"]
            },
            {
                "id": f"{lc3}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los sectores independentistas sostienen que la plena soberanía es indispensable a fin de que la nación __ su propio modelo económico. (diseñar - presente subjuntivo)",
                "answer": "diseñe",
                "english": "Pro-independence sectors maintain that full sovereignty is essential so that the nation designs its own economic model.",
                "teaches": ["puertorico-estado-libre-asociado-debate"]
            },
            {
                "id": f"{lc3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "debate", "del", "estatus", "define", "la", "política", "en", "Puerto", "Rico."],
                "solution": ["El", "debate", "del", "estatus", "define", "la", "política", "en", "Puerto", "Rico."],
                "english": "The status debate defines politics in Puerto Rico.",
                "teaches": ["puertorico-estado-libre-asociado-debate"]
            },
            {
                "id": f"{lc3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Politólogo", "text": "¿Por qué el debate sobre el estatus sigue sin resolverse tras tantas décadas de consultas?"},
                    {"speaker": "Jurista", "text": "_____"},
                    {"speaker": "Politólogo", "text": "Una paradoja constitucional que mantiene a la isla en un limbo jurídico interminable."}
                ],
                "options": [
                    "Porque cualquier resultado plebiscitario carece de carácter vinculante a menos que el Congreso de los Estados Unidos decida actuar bajo su cláusula territorial.",
                    "Porque las papeletas electorales se imprimen exclusivamente en papel bond de alto gramaje.",
                    "Porque los colegios electorales cierran sus puertas a las cuatro de la tarde los días feriados."
                ],
                "correct": 0,
                "teaches": ["puertorico-estado-libre-asociado-debate"]
            },
            {
                "id": f"{lc3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La cláusula territorial subordina el autogobierno a la autoridad del Congreso federal.",
                "english": "The territorial clause subordinates self-government to the authority of the federal Congress.",
                "teaches": ["puertorico-estado-libre-asociado-debate"]
            }
        ]
    })

    # Regional Story 3: b2-puertorico-03.json
    story_pr_03 = {
        "id": "b2-puertorico-03",
        "title": "El Estado Libre Asociado: El debate insular interminable",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica política de nivel B2 sobre el dilema del estatus en Puerto Rico: la fundación del Estado Libre Asociado en 1952 por Muñoz Marín, la resistencia nacionalista de Albizu Campos y las posturas irreconciliables entre estadidad, ELA e independencia.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Pocas sociedades en el mundo contemporáneo han dedicado tantas energías intelectuales, pasiones cívicas y debates jurídicos a desentrañar la naturaleza de su propia condición política como el pueblo de Puerto Rico. Desde la invasión estadounidense de 1898 y la concesión unilateral de la ciudadanía estadounidense en 1917 mediante la Ley Jones —aprobada apenas un mes antes de que los jóvenes boricuas comenzaran a ser reclutados para combatir en los campos de batalla de la Primera Guerra Mundial—, la isla ha vivido atrapada en una controversia existencial irresuelta sobre su soberanía, su identidad nacional y su relación permanente con los Estados Unidos de América."
            },
            {
                "type": "narration",
                "text": "La primera mitad del siglo XX estuvo marcada por el enfrentamiento frontal entre dos proyectos antagónicos. Por un lado, el Partido Nacionalista Puertorriqueño, liderado con oratoria mesiánica por Pedro Albizu Campos, denunció que la dominación extranjera constituía una tiranía militar ilegítima y llamó a la insurrección armada revolucionaria, protagonizando acontecimientos sangrientos como la Masacre de Ponce en 1937 y la revuelta armada de 1950 en Jayuya, que culminó con el asalto al palacio de La Fortaleza y un tiroteo en el Congreso en Washington. Por otro lado, el Partido Popular Democrático (PPD), encabezado por el carismático líder campesino y poeta Luis Muñoz Marín, optó por una estrategia pragmática de modernización acelerada bautizada como 'Operación Manos a la Obra', promoviendo la industrialización mediante incentivos fiscales para atraer corporaciones manufactureras foráneas."
            },
            {
                "type": "narration",
                "text": "El proyecto institucional de Muñoz Marín cristalizó solemnemente el 25 de julio de 1952 con la proclamación de la Constitución de Puerto Rico y la fundación del Estado Libre Asociado (ELA), formalmente denominado en inglés 'Commonwealth of Puerto Rico'. Este pacto político pionero dotó a la isla de un autogobierno democrático interno completo con gobernador electo, poder judicial autónomo y legislatura propia, permitiendo al país ondear su bandera monoestrellada y cantar su himno oficial. En virtud de esta fórmula, Washington retiró a Puerto Rico de la lista de territorios no autónomos de la Organización de las Naciones Unidas en 1953, proclamando al mundo que la isla había alcanzado un estatus libremente concertado mediante referéndum popular."
            },
            {
                "type": "narration",
                "text": "Sin embargo, los límites jurídicos del ELA se convirtieron muy pronto en motivo de agria disputa. Mientras los defensores del modelo sostenían que se trataba de un pacto bilateral irrevocable y mutuamente acordado entre dos pueblos, los sectores críticos denunciaron que la Cláusula Territorial de la Constitución estadounidense continuaba rigiendo sobre la isla, otorgando al Congreso federal poderes plenarios absolutos sobre el archipiélago sin que los tres millones de ciudadanos residentes en la isla tuvieran derecho a votar por el presidente de los Estados Unidos ni contaran con senadores o congresistas con voto en el Capitolio de Washington."
            },
            {
                "type": "narration",
                "text": "Frente a esta encrucijada, el escenario político insular se estructuró a lo largo de décadas en torno a tres trincheras ideológicas irreconciliables. Los partidarios de la 'estadidad', agrupados en el Partido Nuevo Progresista (PNP), abogan por la integración plena como el estado 51 de la unión estadounidense, argumentando que solo la igualdad federada garantizará la plenitud de los derechos cívicos y la igualdad presupuestaria en programas federales de asistencia social. Por su parte, el Partido Independentista Puertorriqueño (PIP) y los movimientos soberanistas defienden la ruptura anticolonial definitiva, sosteniendo que solo una república soberana dotará al pueblo de las herramientas aduaneras, monetarias y diplomáticas necesarias para forjar su propio destino en el concierto latinoamericano y mundial."
            },
            {
                "type": "narration",
                "text": "A partir de 2016, el espejismo de la autonomía plena del ELA sufrió un colapso demoledor. Tras la quiebra financiera del gobierno insular con una deuda pública colosal de más de setenta mil millones de dólares, el Congreso federal aprobó la Ley PROMESA, imponiendo una Junta de Control Fiscal no electa integrada por siete miembros que asumió el poder supremo sobre las finanzas, los presupuestos y las políticas públicas del país por encima de los gobernadores y legisladores electos democráticamente por el pueblo puertorriqueño, desnudando con crudeza la persistencia de una tutela colonial indiscutible."
            },
            {
                "type": "narration",
                "text": "Así, tras más de siete décadas de plebiscitos no vinculantes, marchas multitudinarias y promesas electorales incumplidas por Washington, el debate sobre el estatus sigue constituyendo la gran herida abierta de la sociedad boricua: una cuestión existencial que no solo define la economía y las instituciones públicas del archipiélago, sino que desafía diariamente a cada generación a responder si la nación puertorriqueña desea continuar en la ambigüedad tutelada o dar el paso definitivo hacia la plenitud de sus derechos democráticos y soberanos."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito institucional se proclamó el 25 de julio de 1952 bajo el liderazgo de Luis Muñoz Marín?",
                        "options": [
                            "La promulgación de la Constitución insular y la creación del Estado Libre Asociado (ELA).",
                            "La adhesión formal de Puerto Rico como el estado cincuenta y uno de los Estados Unidos.",
                            "La declaración de independencia absoluta y el retiro de todas las bases navales foráneas.",
                            "La disolución del poder judicial y el establecimiento de una monarquía constitucional hereditaria."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 relata que el 25 de julio de 1952 se proclamó la Constitución y se fundó formalmente el Estado Libre Asociado."
                    },
                    {
                        "question": "¿Cuál es la principal crítica de los sectores soberanistas e independentistas contra la fórmula del ELA?",
                        "options": [
                            "Que el Congreso de EE. UU. mantiene poderes plenarios sobre la isla bajo la cláusula territorial sin representación con voto.",
                            "Que la isla está obligada a mantener embajadas independientes en todas las capitales europeas.",
                            "Que los ciudadanos puertorriqueños carecen de pasaporte para viajar a otros países latinoamericanos.",
                            "Que la Constitución prohíbe la enseñanza de las ciencias y las matemáticas en las escuelas públicas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 expone que el Congreso federal retiene el control plenario sobre la isla sin que los residentes tengan representación legislativa con voto."
                    },
                    {
                        "question": "¿Qué medida impuso el Congreso de EE. UU. en 2016 a través de la Ley PROMESA tras la crisis de la deuda?",
                        "options": [
                            "Una Junta de Control Fiscal no electa que asumió el poder supremo sobre las finanzas del país por encima de los funcionarios locales.",
                            "La condonación automática de toda la deuda bancaria con fondos de la reserva federal.",
                            "La inmediata concesión de la estadidad plena y la designación de dos senadores federales.",
                            "El traspaso de la administración de los puertos comerciales a la Organización de Estados Americanos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 explica que la Ley PROMESA instauró una Junta de Control Fiscal no electa que subordinó las decisiones del gobierno insular."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc3}.json", story_pr_03)

    write_json(f"lessons/b2/{lc3}.json", make_lesson(
        stem=lc3,
        unit_num=12,
        title="El Estado Libre Asociado: El debate insular interminable",
        goal="Analyze the constitutional nature of the Commonwealth (ELA), pro-statehood and pro-independence ideologies, and the PROMESA fiscal board using political and legal registers.",
        grammar_desc="discurso constitucional analítico, ponderación de opciones de estatus y léxico de soberanía insular",
        grammar_ref=f"grammar/b2/{lc3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc3}-voc.json",
        ex_ref=f"exercises/b2/{lc3}-ex.json",
        ex_ids=[f"{lc3}.ex01", f"{lc3}.ex02", f"{lc3}.ex03", f"{lc3}.ex04", f"{lc3}.ex05", f"{lc3}.ex06"],
        goals=[
            "Examine the 1952 Constitution and the political foundations of the Estado Libre Asociado.",
            "Compare the arguments for statehood (estadidad), enhanced commonwealth, and full independence.",
            "Deploy constitutional and political vocabulary (estatus, estadidad, plebiscito, anexionista, soberanía)."
        ],
        story_ref=f"stories/world/b2/{lc3}.json"
    ))

    # Lesson 4: b2-puertorico-04 - De la bomba y plena a la revolución global de la música urbana
    lc4 = "b2-puertorico-04"
    write_json(f"vocabulary/b2/{lc4}-voc.json", {
        "id": "vocab.b2.puertorico.04",
        "lesson": lc4,
        "title": "Música afroboricua, salsa brava de Fania y reguetón global",
        "theme": "Vocabulario de tamboril afrocaribeño, salsa neoyorquina y música urbana",
        "words": [
            {"lemma": "el barril", "translation": "bomba drum (barrel drum)", "pos": "noun"},
            {"lemma": "la plena", "translation": "plena (narrative folk rhythm, el periódico cantado)", "pos": "noun"},
            {"lemma": "la salsa", "translation": "salsa music", "pos": "noun"},
            {"lemma": "el cuá", "translation": "cuá (percussion sticks on wooden body)", "pos": "noun"},
            {"lemma": "el requinto", "translation": "requinto drum in plena, solo improvisation drum", "pos": "noun"},
            {"lemma": "el soneo", "translation": "vocal improvisation in salsa/son", "pos": "noun"},
            {"lemma": "el cadencioso", "translation": "rhythmic, having a pleasing cadence", "pos": "adjective"},
            {"lemma": "la pista", "translation": "track, beat, dance floor", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{lc4}-a-gr.json", {
        "id": "grammar.b2.puertorico.04.bomba-plena-urbano",
        "title": "De la bomba y plena a la revolución global de la música urbana",
        "sections": [
            {
                "type": "text",
                "title": "Crítica musicológica y genealogía de las sonoridades boricuas",
                "content": "La evolución sonora de Puerto Rico en nivel B2 moviliza recursos de crítica artística y sociología musical ('desde el diálogo desafiante entre el tamborilero y el bailador en la bomba tradicional hasta la eclosión global del reguetón boricua en las plataformas digitales streaming', 'resulta innegable que figuras pioneras como Ismael Rivera y Tego Calderón tendieron un puente ininterrumpido de orgullo afrodiaspórico')."
            },
            {
                "type": "table",
                "title": "Genealogía de los ritmos fundamentales boricuas",
                "rows": [
                    ["Bomba afroboricua", "Tambores de barril de ron: diálogo improvisado donde el bailador desafía al tamborilero 'subidor'"],
                    ["Plena puertorriqueña", "Conocida como 'el periódico cantado': relata sucesos cotidianos con panderos y güiro"],
                    ["Salsa brava de Nueva York", "La diáspora boricua (Fania All-Stars, Héctor Lavoe, Willie Colón) fusiona ritmos antillanos"],
                    ["Música urbana contemporánea", "Reguetón y trap latino: desde Daddy Yankee y Don Omar hasta Bad Bunny como fenómeno planetario"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en estudios sobre cultura popular caribeña",
                "items": [
                    {"spanish": "En la bomba, el percusionista del barril 'primo' debe seguir meticulosamente cada quiebre corporal del bailador.", "english": "In bomba, the percussionist on the 'primo' barrel drum must meticulously follow every bodily break of the dancer."},
                    {"spanish": "Héctor Lavoe y Willie Colón crearon himnos salseros que narraban las penurias de los migrantes en los barrios neoyorquinos.", "english": "Héctor Lavoe and Willie Colón created salsa anthems that narrated the hardships of migrants in New York neighborhoods."},
                    {"spanish": "El fenómeno mundial de Bad Bunny demostró la potencia arrolladora del español boricua en la industria musical universal.", "english": "Bad Bunny's worldwide phenomenon demonstrated the overwhelming power of Boricua Spanish in the global music industry."}
                ]
            },
            {
                "type": "tip",
                "content": "Al analizar géneros modernos como el reguetón y el trap, emplea conceptos musicológicos precisos: 'patrón rítmico dembow', 'lírica contestataria', 'hibridación genérica', 'producción electrónica secuenciada'."
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
                    ["el barril", "bomba barrel drum"],
                    ["la plena", "plena (narrative folk rhythm)"],
                    ["el cuá", "percussion rhythm sticks"],
                    ["el soneo", "vocal improvisation in salsa"]
                ],
                "teaches": ["b2-puertorico-vocab"]
            },
            {
                "id": f"{lc4}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué singularidad coreográfica y rítmica define a la danza tradicional de la bomba afroboricua?",
                "options": [
                    "El bailador lidera la improvisación corporal y el tamborilero debe responder con golpes precisos a cada paso del danzante.",
                    "Los bailarines ejecutan una coreografía estricta memorizada sin admitir ninguna improvisación personal.",
                    "La música se interpreta exclusivamente con instrumentos de viento metal sin ningún tambor de percusión."
                ],
                "correct": 0,
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            },
            {
                "id": f"{lc4}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La plena puertorriqueña fue bautizada como el periódico cantado porque sus versos __ las noticias y vicisitudes del pueblo. (narrar - imperfecto indicativo)",
                "answer": "narraban",
                "english": "Puerto Rican plena was nicknamed the sung newspaper because its verses narrated the news and hardships of the people.",
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            },
            {
                "id": f"{lc4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "bomba", "y", "la", "plena", "son", "raíces", "de", "nuestra", "identidad."],
                "solution": ["La", "bomba", "y", "la", "plena", "son", "raíces", "de", "nuestra", "identidad."],
                "english": "Bomba and plena are roots of our identity.",
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            },
            {
                "id": f"{lc4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Musicóloga", "text": "¿Cómo conecta la salsa brava de los años setenta con la música urbana contemporánea?"},
                    {"speaker": "Crítico", "text": "_____"},
                    {"speaker": "Musicóloga", "text": "Una misma crónica callejera de resistencia y orgullo afrocaribeño que trasciende épocas."}
                ],
                "options": [
                    "Ambas nacieron de la calle y del barrio popular como crónica de la supervivencia, fusionando la percusión antillana con el descaro lírico urbano.",
                    "Los directores de orquesta de salsa utilizaban partituras compuestas exclusivamente por la filarmónica de Londres.",
                    "El reguetón se grabó inicialmente en cintas magnéticas de bobina abierta para exportarse a los países escandinavos."
                ],
                "correct": 0,
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            },
            {
                "id": f"{lc4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El sonero improvisa versos brillantes sobre el compás cadencioso de los tambores.",
                "english": "The salsa singer improvises brilliant verses over the rhythmic beat of the drums.",
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            }
        ]
    })

    # Regional Story 4: b2-puertorico-04.json
    story_pr_04 = {
        "id": "b2-puertorico-04",
        "title": "De la bomba y plena a la revolución global de la música urbana",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica musical sobre los motores sonoros de Puerto Rico: la resistencia ancestral de la bomba afroboricua, el periodismo popular de la plena, la eclosión de la salsa brava en Nueva York y la hegemonía planetaria del reguetón.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Si se pretendiera calibrar la potencia creadora de Puerto Rico en el imaginario planetario, resultaría imposible soslayar su condición de superpotencia musical indiscutible. Desde las plantaciones azucareras coloniales del siglo XVII hasta los escenarios multitudinarios y las plataformas digitales de streaming del siglo XXI, la pequeña isla antillana ha engendrado una sucesión vertiginosa de géneros rítmicos que no solo han conquistado los cuerpos de millones de bailadores en los cinco continentes, sino que han servido como el escudo espiritual más inexpugnable para preservar la identidad boricua frente a las tempestades de la asimilación foránea."
            },
            {
                "type": "narration",
                "text": "En el origen de esta estirpe rítmica resuena con fuerza telúrica la bomba afroboricua, nacida en los barracones de esclavos de Loíza, Guayama, Mayagüez y Ponce como un lenguaje sagrado de resistencia, escape y afirmación comunitaria frente a la crueldad del amo. Construida sobre la base rítmica de tambores de madera elaborados a partir de barriles de ron —el 'buleador' que sostiene el compás grave y el 'subidor' o 'primo' que dialoga en agudo—, la bomba presenta una fascinante singularidad coreográfica: a diferencia de la inmensa mayoría de las danzas universales donde el bailarín sigue pasivamente la música, en la bomba es la bailadora o el bailador quien reta al tamborilero mediante 'piquetes' o quiebres corporales improvisados, obligando al percusionista a reproducir con exactitud milimétrica sobre el cuero cada giro, faldeo y estocada del cuerpo danzante."
            },
            {
                "type": "narration",
                "text": "A comienzos del siglo XX, en los arrabales obreros de San Antón en Ponce, floreció la 'plena', bautizada entrañablemente por el pueblo como 'el periódico cantado'. Desprovista de instrumentos armónicos y armada únicamente con un coro fervoroso, un güiro de calabaza y una batería de 'panderos' redondos sin sonajas —el seguidor, el punteador y el virtuoso 'requinto' que solea sobre el coro—, la plena se convirtió en el noticiero oral de los desposeídos: sus estribillos narraban crónicas vecinales, amores prohibidos, catástrofes naturales y huelgas portuarias, elevando los acontecimientos cotidianos a la categoría de crónica épica popular."
            },
            {
                "type": "narration",
                "text": "A mediados del siglo XX, el legendario percusionista y compositor Rafael Cortijo junto a la voz inimitable de Ismael Rivera —'El Sonero Mayor'— transformaron la escena cultural al introducir la bomba y la plena en los salones de baile aristocráticos y en la incipiente televisión insular, rompiendo con desparpajo las barreras de marginación racial que confinaban a la música negra a los sectores marginales. Aquella revolución rítmica cruzó el océano con la masiva emigración boricua hacia Nueva York, donde en los barrios marginales del Spanish Harlem y el Bronx los músicos boricuas fusionaron los ritmos antillanos con las armonías del jazz y la rumba cubana para fundar, bajo el mítico sello Fania Records, el fenómeno arrollador de la 'salsa brava'."
            },
            {
                "type": "narration",
                "text": "Liderada por orquestas legendarias encabezadas por Willie Colón, Ray Barretto, Bobby Valentín y las voces monumentales de Cheo Feliciano y Héctor Lavoe —'El Cantante de los Cantantes'—, la salsa neoyorquina no fue un mero género bailable, sino el himno de lucha y desarraigo de los migrantes latinos que sobrevivían a la discriminación en los rascacielos gélidos del norte. Canciones inmortales como 'El día de mi suerte', 'Anacaona' y 'Calle Luna, Calle Sol' combinaban la furia rítmica de los trombones con una poesía callejera de hondura existencial que hermanó a toda la América hispanoparlante."
            },
            {
                "type": "narration",
                "text": "A fines del siglo XX, esa misma juventud urbana y marginada protagonizó otra mutación revolucionaria en los caseríos de vivienda pública de San Juan y Carolina: el nacimiento del reguetón. Tomando como base el 'dembow' del dancehall jamaiquino y la métrica rapeada del hip hop neoyorquino, pioneros como DJ Playero, Vico C, The Noise y más tarde Daddy Yankee, Tego Calderón y Don Omar convirtieron el underground boricua en un tsunami comercial planetario, demostrando que la calle insular era capaz de dictar el compás de la industria musical global."
            },
            {
                "type": "narration",
                "text": "En la actualidad, figuras planetarias como Bad Bunny han llevado la música urbana a cotas de influencia cultural inauditas, encabezando las listas globales de reproducción durante años consecutivos sin renunciar en ningún momento a su acento boricua, su jerga local y su compromiso político contra la corrupción y la precariedad insular. De la cadencia ancestral de los barriles de bomba a los sintetizadores de la música urbana contemporánea, Puerto Rico ha demostrado que su música constituye su mayor soberanía: un caudal sonoro infinito que trasciende fronteras territoriales para afirmar ante el planeta entero la vitalidad indomable de la nación boricua."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué relación coreográfica y comunicativa singular caracteriza a la danza de la bomba afroboricua?",
                        "options": [
                            "El bailador desafía al tamborilero subidor mediante quiebres corporales que el percusionista debe imitar con el cuero.",
                            "Los músicos interpretan una partitura clásica sin mirar a los bailarines en ningún momento de la velada.",
                            "Los integrantes del coro danzan en círculos cerrados sosteniendo velas encendidas de cera de abejas.",
                            "Los tambores permanecen inmóviles y la música se produce exclusivamente con las palmadas del público."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 explica que en la bomba es el danzante quien improvisa los movimientos que el tamborilero subidor debe sincronizar al instante."
                    },
                    {
                        "question": "¿Por qué el género tradicional de la plena puertorriqueña fue apodado popularmente como 'el periódico cantado'?",
                        "options": [
                            "Porque sus letras narraban los sucesos cotidianos, noticias vecinales, crónicas y tragedias populares del pueblo.",
                            "Porque los cantantes debían leer las estrofas directamente de las páginas de los diarios matutinos de Ponce.",
                            "Porque era una música financiada exclusivamente por los dueños de imprentas de la capital insular.",
                            "Porque estaba prohibido cantar sobre cualquier tema que no hubiera sido publicado en boletines oficiales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 detalla que la plena funcionaba como noticiero oral de la comunidad al relatar acontecimientos locales e incidentes sociales."
                    },
                    {
                        "question": "¿Qué papel cumplió la orquesta de Cortijo y su cantante Ismael Rivera en la evolución musical de la isla en los años cincuenta?",
                        "options": [
                            "Llevaron la bomba y la plena a la radio, la televisión y los salones aristocráticos, rompiendo la discriminación racial.",
                            "Sustituyeron los tambores tradicionales por orquestaciones exclusivas de música de cámara barroca.",
                            "Fundaron una academia de ballet clásico en el municipio montañoso de Utuado.",
                            "Prohibieron la interpretación de música en español para favorecer temas cantados en inglés."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 expone que Cortijo e Ismael Rivera rompieron las barreras de exclusión racial al introducir los ritmos afrocubanos y boricuas en los medios masivos."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc4}.json", story_pr_04)

    write_json(f"lessons/b2/{lc4}.json", make_lesson(
        stem=lc4,
        unit_num=12,
        title="De la bomba y plena a la revolución global de la música urbana",
        goal="Examine Afro-Boricua musical traditions (bomba, plena), the New York salsa revolution (Fania), and contemporary urban music (reggaeton, Bad Bunny) using musicological criticism.",
        grammar_desc="crítica musicológica contemporánea, genealogía de ritmos afrodiaspóricos y léxico de la música urbana",
        grammar_ref=f"grammar/b2/{lc4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc4}-voc.json",
        ex_ref=f"exercises/b2/{lc4}-ex.json",
        ex_ids=[f"{lc4}.ex01", f"{lc4}.ex02", f"{lc4}.ex03", f"{lc4}.ex04", f"{lc4}.ex05", f"{lc4}.ex06"],
        goals=[
            "Trace the Afro-Boricua roots of bomba and plena as communal resistance tools.",
            "Analyze the New York Fania All-Stars salsa movement and its sociopolitical lyrics.",
            "Deploy musicological and cultural vocabulary (barril, plena, salsa, cuá, requinto, soneo)."
        ],
        story_ref=f"stories/world/b2/{lc4}.json"
    ))

    # Lesson 5: b2-puertorico-05 - El huracán María, la crisis de la deuda y la resistencia ciudadana
    lc5 = "b2-puertorico-05"
    write_json(f"vocabulary/b2/{lc5}-voc.json", {
        "id": "vocab.b2.puertorico.05",
        "lesson": lc5,
        "title": "Crisis fiscal, el huracán María y el Verano del 19",
        "theme": "Vocabulario de resiliencia comunitaria, colapso de infraestructuras y movilización cívica",
        "words": [
            {"lemma": "la resiliencia", "translation": "resilience", "pos": "noun"},
            {"lemma": "el apagón", "translation": "blackout, power outage", "pos": "noun"},
            {"lemma": "la autogestión", "translation": "community self-management", "pos": "noun"},
            {"lemma": "la austeridad", "translation": "austerity", "pos": "noun"},
            {"lemma": "el reclamo", "translation": "demand, public claim", "pos": "noun"},
            {"lemma": "derrocar", "translation": "to overthrow, to oust", "pos": "verb"},
            {"lemma": "el colapso", "translation": "collapse, breakdown", "pos": "noun"},
            {"lemma": "inédito", "translation": "unprecedented, unpublished", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{lc5}-a-gr.json", {
        "id": "grammar.b2.puertorico.05.maria-deuda-resistencia",
        "title": "El huracán María, la crisis de la deuda y la resistencia ciudadana",
        "sections": [
            {
                "type": "text",
                "title": "Discurso sobre catástrofes climáticas, gestión de crisis y poder ciudadano",
                "content": "El análisis sociológico de los eventos contemporáneos puertorriqueños en nivel B2 integra oraciones causales y temporales complejas ('tras el paso devastador del huracán María en septiembre de 2017', 'habiendo colapsado la red eléctrica durante casi un año') y períodos que describen la movilización cívica del 'Verano del 19', hito en que la ciudadanía forzó la renuncia de un gobernador por primera vez en la historia insular."
            },
            {
                "type": "table",
                "title": "Factores de la crisis y respuesta ciudadana",
                "rows": [
                    ["Huracán María (2017)", "Ciclón categoría 4 que destruyó la infraestructura eléctrica y causó miles de víctimas"],
                    ["Autogestión comunitaria", "Centros de apoyo mutuo que suplieron la inacción gubernamental con energía solar y comedores"],
                    ["Verano del 19", "Protestas masivas autoconvocadas que forzaron la renuncia del gobernador Ricardo Rosselló"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el ensayo sociológico contemporáneo",
                "items": [
                    {"spanish": "El colapso de la red energética demostró la vulnerabilidad estructural de una infraestructura pública privatizada y precaria.", "english": "The collapse of the power grid demonstrated the structural vulnerability of precarious and privatized public infrastructure."},
                    {"spanish": "Las comunidades rurales se organizaron mediante comedores sociales a fin de que ninguna familia quedara desamparada.", "english": "Rural communities organized through community kitchens so that no family would be left abandoned."},
                    {"spanish": "Las multitudinarias marchas del Verano del 19 congregaron a más de medio millón de personas en el expreso Las Américas.", "english": "The massive marches of the Summer of 2019 gathered over half a million people on the Las Américas expressway."}
                ]
            },
            {
                "type": "tip",
                "content": "Para narrar protestas sociales y crisis institucionales en registro culto, utiliza sustantivos abstractos de acción cívica: 'movilización autoconvocada', 'indignación colectiva', 'reclamo de probidad', 'dimisión forzosa'."
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
                    ["la resiliencia", "resilience"],
                    ["el apagón", "blackout, power outage"],
                    ["la autogestión", "community self-management"],
                    ["la austeridad", "austerity"]
                ],
                "teaches": ["b2-puertorico-vocab"]
            },
            {
                "id": f"{lc5}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué hito político inédito en la historia de Puerto Rico se produjo durante el denominado 'Verano del 19'?",
                "options": [
                    "La renuncia forzosa del gobernador de la isla tras semanas de protestas cívicas pacíficas multitudinarias.",
                    "La firma de un tratado de unión comercial preferencial con la República Dominicana.",
                    "La disolución del tribunal supremo insular por decisión del departamento de estado federal."
                ],
                "correct": 0,
                "teaches": ["puertorico-huracan-maria-deuda-resistencia"]
            },
            {
                "id": f"{lc5}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las comunidades montañosas organizaron centros de apoyo mutuo a fin de que los ancianos __ alimentos calientes y agua potable tras el huracán. (recibir - imperfecto subjuntivo)",
                "answer": "recibieran",
                "english": "Mountain communities organized mutual support centers so that the elderly would receive hot meals and drinking water after the hurricane.",
                "teaches": ["puertorico-huracan-maria-deuda-resistencia"]
            },
            {
                "id": f"{lc5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "pueblo", "boricua", "demostró", "una", "resiliencia", "inquebrantable", "ante", "la", "adversidad."],
                "solution": ["El", "pueblo", "boricua", "demostró", "una", "resiliencia", "inquebrantable", "ante", "la", "adversidad."],
                "english": "The Puerto Rican people demonstrated unshakeable resilience in the face of adversity.",
                "teaches": ["puertorico-huracan-maria-deuda-resistencia"]
            },
            {
                "id": f"{lc5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Qué lección fundamental dejó la respuesta comunitaria tras el paso del huracán María?"},
                    {"speaker": "Líder comunitaria", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Una muestra heroica de dignidad colectiva que transformó la conciencia del país."}
                ],
                "options": [
                    "Demostró que ante la lentitud y el abandono institucional del Estado, la autogestión solidaria del pueblo fue la que salvó miles de vidas.",
                    "Los generadores eléctricos de gasolina requieren cambio periódico de bujías y filtros de aire.",
                    "Las rutas aéreas comerciales hacia Miami operan con frecuencias diarias regulares."
                ],
                "correct": 0,
                "teaches": ["puertorico-huracan-maria-deuda-resistencia"]
            },
            {
                "id": f"{lc5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La autogestión comunitaria suplió las deficiencias del aparato estatal tras el desastre.",
                "english": "Community self-management made up for the state apparatus deficiencies after the disaster.",
                "teaches": ["puertorico-huracan-maria-deuda-resistencia"]
            }
        ]
    })

    # Regional Story 5: b2-puertorico-05.json
    story_pr_05 = {
        "id": "b2-puertorico-05",
        "title": "El huracán María, la crisis de la deuda y la resistencia ciudadana",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociológica de nivel B2 sobre las pruebas extremas de Puerto Rico en el siglo XXI: el impacto devastador del huracán María en 2017, la autogestión comunitaria frente al apagón prolongado y la insurrección cívica pacífica del Verano del 19.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "La mañana del 20 de septiembre de 2017 quedará grabada como una de las fechas más oscuras, trágicas y transformadoras en la memoria contemporánea del pueblo puertorriqueño. Con vientos sostenidos de más de doscientos cincuenta kilómetros por hora y ráfagas huracanadas apocalípticas, el ojo del huracán María —un ciclón de categoría cuatro de ferocidad inaudita— atravesó diagonalmente la isla desde el municipio suroriental de Yabucoa hasta salir por Arecibo en el norte. Durante más de doce horas interminables de rugido atronador, las lluvias bíblicas desgajaron montañas enteras, desbordaron los ríos costeros y arrasaron miles de viviendas campesinas, arrancando de cuajo la red de transmisión eléctrica y sumiendo al país entero en una parálisis absoluta."
            },
            {
                "type": "narration",
                "text": "Las secuelas inmediatas del cataclismo revelaron la extrema vulnerabilidad de un territorio que ya se encontraba asfixiado por una década de recesión económica y sometido a los recortes de austeridad de la Junta de Control Fiscal. El sistema electroenergético insular colapsó al cien por cien de forma instantánea, provocando el mayor y más prolongado apagón en la historia de los Estados Unidos: amplias zonas rurales de la cordillera permanecieron a oscuras durante casi un año entero. La falta de energía paralizó los hospitales, inutilizó los sistemas de bombeo de agua potable y desató una crisis humanitaria dantesca que, según estudios rigurosos de la Universidad de Harvard validados posteriormente por el gobierno insular, cobró la vida de casi tres mil personas debido a la imposibilidad de operar respiradores, conservar medicinas de refrigeración o acceder a tratamientos de diálisis."
            },
            {
                "type": "narration",
                "text": "Ante la lentitud exasperante de la respuesta gubernamental local y la negligencia evidente de las agencias federales de socorro, fue el propio pueblo boricua quien protagonizó una gesta épica de solidaridad y resiliencia comunitaria. En barrios marginales y pueblos de la montaña nacieron espontáneamente 'Centros de Apoyo Mutuo' organizados por maestros, líderes barriales y estudiantes: se instalaron comedores comunitarios que servían comidas calientes diarias a miles de ancianos desamparados, se habilitaron techos de lona azul provisionales y se crearon sistemas pioneros de energía solar comunitaria, demostrando que la autogestión popular era la única fuerza capaz de salvar vidas frente al abandono institucional del Estado."
            },
            {
                "type": "narration",
                "text": "Esta profunda acumulación de duelo, rabia contenida y dignidad herida eclosionó de manera telúrica en julio de 2019, desatando la mayor insurrección cívica pacífica en la historia política de Puerto Rico: el denominado 'Verano del 19'. El detonante fue la filtración pública de casi novecientas páginas de un chat privado de la aplicación Telegram en el que el gobernador Ricardo Rosselló y su círculo íntimo de colaboradores se burlaban con cinismo despiadado de los cadáveres acumulados por el huracán María, proferían insultos misóginos y homofóbicos contra opositores y tramaban esquemas de corrupción con fondos públicos."
            },
            {
                "type": "narration",
                "text": "La reacción popular fue un estallido ciudadano de dimensiones inéditas. Durante quince días consecutivos, cientos de miles de puertorriqueños de todas las generaciones se congregaron pacíficamente en las calles del Viejo San Juan, desafiando los gases lacrimógenos de la policía antimotines frente al palacio de La Fortaleza. Artistas de renombre planetario como Ricky Martin, Residente y Bad Bunny regresaron a la isla para marchar en la primera fila junto a jubilados, estudiantes y familias enteras, culminando el 22 de julio con una huelga general que paralizó por completo el expreso Las Américas con más de medio millón de manifestantes bajo el lema inapelable de '¡Ricky, renuncia!'."
            },
            {
                "type": "narration",
                "text": "La presión ciudadana fue tan colosal e incontestable que la medianoche del 24 de julio de 2019, en una alocución televisada histórica, Ricardo Rosselló se vio forzado a anunciar su renuncia al cargo de gobernador, convirtiéndose en el primer mandatario en la historia de Puerto Rico en ser depuesto por la voluntad directa de su propio pueblo. La victoria popular consagró el poder de la movilización autoconvocada y demostró que la ciudadanía boricua no estaba dispuesta a seguir tolerando la impunidad ni la degradación ética de su clase dirigente."
            },
            {
                "type": "narration",
                "text": "A pesar de que persisten graves desafíos estructurales —la privatización controvertida de la red eléctrica, el encarecimiento de la vivienda provocado por leyes de exención contributiva para millonarios extranjeros y la persistente sangría de la emigración juvenil—, las lecciones del huracán María y el Verano del 19 transformaron para siempre la conciencia de la nación boricua: un pueblo que descubrió en su propia solidaridad comunitaria y en su coraje cívico la fuerza inextinguible necesaria para resistir cualquier tempestad y refundar su patria sobre los cimientos de la justicia y la dignidad."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué impacto humano y estructural devastador provocó el paso del huracán María en septiembre de 2017?",
                        "options": [
                            "El colapso total de la red eléctrica durante casi un año y la pérdida de casi tres mil vidas humanas.",
                            "La evaporación completa de las aguas de todas las bahías bioluminiscentes de la isla.",
                            "La demolición planificada de las fortalezas coloniales de piedra caliza en el Viejo San Juan.",
                            "El traslado forzoso de la capital gubernamental hacia la ciudad costera de Mayagüez."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 relata que el huracán María destruyó la red eléctrica, dejó sin luz a zonas rurales durante un año y causó casi tres mil muertes."
                    },
                    {
                        "question": "¿Cómo suplió la sociedad civil boricua la inacción gubernamental tras el desastre del huracán?",
                        "options": [
                            "Mediante Centros de Apoyo Mutuo comunitarios con comedores sociales y autogestión de energía solar.",
                            "Contratando batallones de mercenarios extranjeros para resguardar los almacenes portuarios.",
                            "Esperando pacientemente la llegada de buques de carga de combustible procedentes de Europa.",
                            "Abandonando definitivamente todos los poblados montañosos de la cordillera Central."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 destaca que las comunidades organizaron comedores populares y redes de apoyo mutuo para salvar vidas ante la falta de auxilio estatal."
                    },
                    {
                        "question": "¿Cuál fue el desenlace histórico de las multitudinarias protestas ciudadanas del 'Verano del 19'?",
                        "options": [
                            "La renuncia forzosa del gobernador Ricardo Rosselló, depuesto por primera vez por la movilización popular.",
                            "La disolución del parlamento insular y la convocatoria a elecciones generales anticipadas.",
                            "La declaración de un estado de sitio permanente supervisado por tropas de la marina federal.",
                            "La prohibición absoluta de la música urbana y de los conciertos masivos en el archipiélago."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 precisa que la presión masiva forzó la dimisión de Ricardo Rosselló, hito sin precedentes en la historia de la isla."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc5}.json", story_pr_05)

    write_json(f"lessons/b2/{lc5}.json", make_lesson(
        stem=lc5,
        unit_num=12,
        title="El huracán María, la crisis de la deuda y la resistencia ciudadana",
        goal="Analyze the devastation of Hurricane María, community self-management, and the historic Summer of 2019 civic uprising using sociological and political discourse.",
        grammar_desc="discurso sobre catástrofes climáticas, movilización ciudadana y léxico de resiliencia comunitaria",
        grammar_ref=f"grammar/b2/{lc5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{lc5}-voc.json",
        ex_ref=f"exercises/b2/{lc5}-ex.json",
        ex_ids=[f"{lc5}.ex01", f"{lc5}.ex02", f"{lc5}.ex03", f"{lc5}.ex04", f"{lc5}.ex05", f"{lc5}.ex06"],
        goals=[
            "Evaluate the human toll and structural breakdown caused by Hurricane María in 2017.",
            "Analyze community self-management mechanisms (Centros de Apoyo Mutuo) in disaster response.",
            "Deploy civic crisis vocabulary (resiliencia, apagón, autogestión, austeridad, derrocar)."
        ],
        story_ref=f"stories/world/b2/{lc5}.json"
    ))

    # Consolidation: b2-puertorico-consolidation
    lc_con = "b2-puertorico-consolidation"
    write_json(f"exercises/b2/{lc_con}-ex.json", {
        "lesson": lc_con,
        "exercises": [
            {
                "id": f"{lc_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el coquí", "endemic Puerto Rican tree frog"],
                    ["la cesión", "cession, transfer of sovereignty"],
                    ["el barril", "bomba barrel drum"],
                    ["la autogestión", "community self-management"]
                ],
                "teaches": ["b2-puertorico-vocab"]
            },
            {
                "id": f"{lc_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué acontecimiento histórico frustró el régimen autonómico democrático de la Carta Autonómica de 1897 en Puerto Rico?",
                "options": [
                    "La invasión militar estadounidense de julio de 1898 y la posterior cesión colonial en el Tratado de París.",
                    "La erupción de un volcán submarino en el pasaje de la Mona.",
                    "La decisión voluntaria del parlamento insular de disolverse para convocar a elecciones militares."
                ],
                "correct": 0,
                "teaches": ["puertorico-grito-lares-cesion-1898"]
            },
            {
                "id": f"{lc_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la bomba afroboricua es considerada una danza de rebelión y soberanía corporal?",
                "options": [
                    "Porque es el danzante quien improvisa los movimientos que el tamborilero subidor debe sincronizar al instante sobre el cuero.",
                    "Porque los participantes deben recitar oraciones en latín antes de iniciar el compás.",
                    "Porque fue compuesta por corsarios franceses para burlar el bloqueo naval de la corona española."
                ],
                "correct": 0,
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            },
            {
                "id": f"{lc_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las comunidades boricuas forjaron redes de solidaridad a fin de que ninguna familia __ desamparada tras el paso de los huracanes. (quedar - imperfecto subjuntivo)",
                "answer": "quedara",
                "english": "Boricua communities forged solidarity networks so that no family would be left abandoned after the hurricanes.",
                "teaches": ["puertorico-huracan-maria-deuda-resistencia"]
            },
            {
                "id": f"{lc_con}.ex05",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "El Yunque y las bahías de Vieques resguardan santuarios de biodiversidad única. [El Yunque and Vieques bays shelter sanctuaries of unique biodiversity.]",
                    "El Grito de Lares de 1868 proclamó la república y la abolición de la esclavitud. [The 1868 Grito de Lares proclaimed the republic and the abolition of slavery.]",
                    "La música afroboricua y la salsa conquistaron los escenarios de todo el planeta. [Afro-Boricua music and salsa conquered stages across the entire planet.]",
                    "El Verano del 19 demostró la potencia invencible de la movilización cívica pacífica. [The Summer of 19 demonstrated the invincible power of peaceful civic mobilization.]"
                ],
                "solution": [0, 1, 2, 3],
                "teaches": [
                    "puertorico-biodiversidad-yunque-bioluminiscencia",
                    "puertorico-grito-lares-cesion-1898",
                    "puertorico-bomba-plena-salsa-urbano",
                    "puertorico-huracan-maria-deuda-resistencia"
                ]
            },
            {
                "id": f"{lc_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Socióloga", "text": "¿Cómo definiría el núcleo irreductible de la identidad boricua ante los desafíos contemporáneos?"},
                    {"speaker": "Ensayista", "text": "_____"},
                    {"speaker": "Socióloga", "text": "Una afirmación vibrante de soberanía cultural que no acepta la derrota histórica."}
                ],
                "options": [
                    "Es la inagotable dignidad de un pueblo que convirtió su naturaleza sagrada, su música libertaria y su resistencia solidaria en un estandarte universal de supervivencia.",
                    "Las terminales de cruceros del puerto de San Juan reciben embarcaciones de hasta doce pisos de altura.",
                    "El café cosechado en Maricao se tuesta mediante procesos industriales mecanizados."
                ],
                "correct": 0,
                "teaches": ["puertorico-huracan-maria-deuda-resistencia"]
            },
            {
                "id": f"{lc_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La cultura boricua ha resistido los embates coloniales con orgullo y alegría.",
                "english": "Boricua culture has resisted colonial onslaughts with pride and joy.",
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            },
            {
                "id": f"{lc_con}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Redacta una reflexión analítica sobre la resistencia cultural puertorriqueña empleando una cláusula final con subjuntivo ('a fin de que') o preventiva ('para que no').",
                        "answer": "La sociedad civil puertorriqueña preserva con devoción sus tradiciones sonoras y su lengua a fin de que ninguna imposición foránea borre su identidad nacional."
                    }
                ],
                "teaches": ["puertorico-bomba-plena-salsa-urbano"]
            }
        ]
    })

    # Regional Capstone Story: b2-puertorico.json
    story_pr_capstone = {
        "id": "b2-puertorico",
        "title": "Consolidación: La isla del encanto en la encrucijada",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica panorámica de nivel B2 sobre Puerto Rico: síntesis de su ecología tropical y kárstica, su heroica trayectoria libertaria, su soberanía musical de la bomba al reguetón y su inquebrantable resistencia cívica contemporánea.",
        "characters": [],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Conocida en el orbe entero por el apelativo luminoso de la 'Isla del Encanto' y reivindicada por sus hijos con el entrañable nombre taíno de 'Borikén', Puerto Rico constituye uno de los territorios culturales, ecológicos y políticos más singulares, complejos y apasionantes de las Américas. Enclavada en el umbral del mar de las Antillas, esta isla caribeña condensa en sus dimensiones geográficas compactas una historia de resistencia inagotable: un país sin soberanía política formal que, sin embargo, ha forjado una de las identidades nacionales más firmes, orgullosas y universalmente reconocidas de todo el mundo hispanoparlante."
            },
            {
                "type": "narration",
                "text": "El primer testimonio de esta grandeza descansa en su portentoso patrimonio natural. Desde las brumas templadas y cascadas cristalinas del Bosque Nacional El Yunque —hogar del árbol de tabonuco, la cotorra amenazada y el canto nocturno del coquí— hasta los mogotes kársticos de Camuy y el resplandor de las aguas de Puerto Mosquito en Vieques, la geografía boricua desafía la uniformidad. En sus bahías bioluminiscentes, la simbiosis entre los manglares rojos y millones de dinoflagelados alumbra un espectáculo de luz marina sin parangón en el planeta, recordándole a sus habitantes que la belleza y la fragilidad suelen caminar de la mano en los ecosistemas insulares."
            },
            {
                "type": "narration",
                "text": "En el terreno de la memoria patria, Puerto Rico ha librado un combate secular por su dignidad y autodeterminación. Desde la clarinada libertaria del Grito de Lares en 1868 inspirada por Ramón Emeterio Betances —donde se abolió por primera vez la libreta de jornaleros y la esclavitud— hasta la efímera plenitud democrática de la Carta Autonómica de 1897, la isla demostró una temprana vocación de soberanía. La posterior invasión militar de 1898 y la cesión forzosa en el Tratado de París truncaron aquella primavera autonómica, subordinando el destino nacional a la tutela de Washington bajo la doctrina del 'territorio no incorporado' que perdura hasta hoy."
            },
            {
                "type": "narration",
                "text": "Frente a las incertidumbres del estatus político que dividieron a la sociedad entre la defensa del Estado Libre Asociado fundado en 1952 por Muñoz Marín, el anhelo anexionista de la estadidad y la dignidad irreductible del nacionalismo de Albizu Campos, la nación puertorriqueña encontró en la música su trinchera más inexpugnable. En la bomba afroboricua, el diálogo entre los tambores de barril y el cuerpo desafiante del bailador convirtió el dolor del esclavo en soberanía estética; en la plena campesina de San Antón, los panderos se transformaron en el periódico cantado de los humildes; y en las calles del Bronx neoyorquino, la diáspora boricua fundó la salsa brava junto a la Fania All-Stars, regalando al continente una banda sonora inmortal de lucha y orgullo caribeño."
            },
            {
                "type": "narration",
                "text": "Esa misma fuerza creadora popular eclosionó en los caseríos de San Juan a fines del siglo XX para engendrar la revolución planetaria de la música urbana. Del 'dembow' underground de los noventa a la hegemonía global de Daddy Yankee y Bad Bunny, los artistas boricuas han colonizado las listas de éxitos mundiales sin renunciar a su lengua vernácula ni a la crónica descarnada de su realidad social, convirtiendo el español caribeño en el idioma sonoro indiscutible de la juventud de nuestro tiempo."
            },
            {
                "type": "narration",
                "text": "En el siglo XXI, las pruebas de la historia han puesto a prueba la fortaleza moral del pueblo puertorriqueño con una dureza extrema. La bancarrota fiscal, la imposición tutelar de la Junta de Control Fiscal bajo la Ley PROMESA y la devastación sísmica del huracán María en 2017 golpearon la infraestructura insular con crudeza apocalíptica; no obstante, fue la solidaridad comunitaria de los Centros de Apoyo Mutuo la que salvó miles de vidas frente a la negligencia estatal. Aquella dignidad colectiva explotó en el Verano del 19, cuando medio millón de ciudadanos pacíficos paralizaron las avenidas de San Juan hasta forzar la histórica dimisión del gobernador, escribiendo una lección magistral de poder popular democrático."
            },
            {
                "type": "narration",
                "text": "Así, Puerto Rico se proyecta hacia el porvenir en una encrucijada crucial pero cargada de esperanza. Lejos de ser una colonia resignada, Borikén se afirma ante el mundo como una nación viva, vibrante e indomeñable, cuyo mayor tesoro no reside en los tratados jurídicos que otros redactaron a sus espaldas, sino en el corazón solidario de sus gentes, la poesía de su música y su invencible determinación de seguir existiendo en libertad y alegría."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis define la paradoja de la identidad puertorriqueña según la crónica de consolidación?",
                        "options": [
                            "Ser una nación sin soberanía política formal que ostenta una identidad cultural reconocida en todo el mundo.",
                            "Ser un territorio continental desértico gobernado por una confederación de cacicazgos taínos.",
                            "Haber sido fundada en el siglo XVIII como un protectorado exclusivo de navegantes holandeses.",
                            "Haber renunciado por plebiscito a su idioma español para adoptar el inglés como lengua obligatoria."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 subraya la singularidad de Puerto Rico como un país sin autodeterminación política jurídica que conserva una firme soberanía cultural."
                    },
                    {
                        "question": "¿De qué manera la música funcionó como trinchera y escudo de la identidad boricua a lo largo de su historia?",
                        "options": [
                            "Articuló la resistencia antiesclavista en la bomba, la crónica popular en la plena y la afirmación diaspórica en la salsa brava y el reguetón.",
                            "Fue prohibida en los barrios urbanos para promover exclusivamente cantos corales gregorianos.",
                            "Se limitó a imitar partituras orquestales procedentes de las cortes virreinales europeas.",
                            "Funcionó como un código militar secreto para dirigir la navegación fluvial hacia los Estados Unidos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los párrafos 4 y 5 relatan cómo la bomba, la plena, la salsa de Fania y el género urbano fueron vehículos de dignidad, orgullo y resistencia social."
                    },
                    {
                        "question": "¿Qué demostró la respuesta del pueblo puertorriqueño tras el huracán María y durante las marchas del Verano del 19?",
                        "options": [
                            "La fuerza invencible de la autogestión comunitaria y el poder democrático pacífico para derrocar gobernantes corruptos.",
                            "La conveniencia de privatizar todos los servicios de agua potable y hospitales públicos.",
                            "La necesidad urgente de suprimir las elecciones municipales para instaurar una administración castrense.",
                            "La indiferencia de la ciudadanía frente a la gestión fiscal y la quiebra financiera."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 destaca la solidaridad comunitaria de los Centros de Apoyo Mutuo y el coraje cívico de la movilización popular de 2019."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{lc_con}.json", story_pr_capstone)
    write_json(f"stories/world/b2/b2-puertorico.json", story_pr_capstone)

    write_json(f"lessons/b2/{lc_con}.json", make_consolidation_lesson(
        stem=lc_con,
        unit_num=12,
        title="Unit 12 Consolidation: Puerto Rico",
        goal="Consolidate Puerto Rican biodiversity, 1898 colonial history, musical evolution (bomba to reggaeton), and civic resistance through advanced purpose, concessive, and restrictive discourse.",
        grammar_desc="síntesis discursiva sobre Puerto Rico: ecosistemas insulares, soberanía colonial, genealogía musical y poder ciudadano",
        ex_ref=f"exercises/b2/{lc_con}-ex.json",
        ex_ids=[f"{lc_con}.ex01", f"{lc_con}.ex02", f"{lc_con}.ex03", f"{lc_con}.ex04", f"{lc_con}.ex05", f"{lc_con}.ex06", f"{lc_con}.ex07", f"{lc_con}.ex08"],
        goals=[
            "Synthesize Puerto Rican ecological heritage from El Yunque to Vieques bioluminescent bay.",
            "Analyze the 1868 Grito de Lares, the 1898 Treaty of Paris, and the Commonwealth status question.",
            "Trace the Afro-Boricua musical lineage through salsa brava to global urban music.",
            "Debate civic resilience following Hurricane María and the historic Summer of 2019 uprising."
        ],
        checklist_items=[
            "I can analyze Puerto Rican ecosystems and bioluminescent bays with precise vocabulary.",
            "I can discuss the 1898 cession and the constitutional status debate using formal discourse.",
            "I can trace the cultural evolution of bomba, plena, salsa, and urban reggaeton.",
            "I can evaluate disaster response and civic mobilization (Verano del 19) using advanced purpose structures."
        ],
        story_ref=f"stories/world/b2/b2-puertorico.json"
    ))
    print("Completed LatAm Unit 12 (Puerto Rico) generation!")

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

    if "b2-12-01" not in existing_stems:
        units_data.append({
            "title": "Finality, Purpose & Institutional Goals",
            "stems": [
                "b2-12-01",
                "b2-12-02",
                "b2-12-03",
                "b2-12-04",
                "b2-12-05",
                "b2-12-consolidation"
            ],
            "track": "core"
        })

    if "b2-puertorico-01" not in existing_stems:
        units_data.append({
            "title": "Puerto Rico: Boricua Identity, Sovereignty & Cultural Defiance",
            "stems": [
                "b2-puertorico-01",
                "b2-puertorico-02",
                "b2-puertorico-03",
                "b2-puertorico-04",
                "b2-puertorico-05",
                "b2-puertorico-consolidation"
            ],
            "track": "latam"
        })

    with open(units_file, "w", encoding="utf-8") as f:
        json.dump(units_data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Updated curriculum/units/b2.json with Unit 12!")

    # -------------------------------------------------------------------------
    # VERIFY WORD COUNTS FOR ALL STORIES
    # -------------------------------------------------------------------------
    all_stories = [
        ("story_core_12", story_core_12),
        ("story_pr_01", story_pr_01),
        ("story_pr_02", story_pr_02),
        ("story_pr_03", story_pr_03),
        ("story_pr_04", story_pr_04),
        ("story_pr_05", story_pr_05),
        ("story_pr_capstone", story_pr_capstone),
    ]
    print("\n--- Story Word Count Audit ---")
    for name, s in all_stories:
        wc = count_words(s)
        status = "OK (650-825)" if 650 <= wc <= 825 else f"OUT OF RANGE: {wc}"
        print(f"{name:20s}: {wc:4d} words -> {status}")
        assert 650 <= wc <= 825, f"Word count {wc} out of range for {name}!"


if __name__ == "__main__":
    run()
