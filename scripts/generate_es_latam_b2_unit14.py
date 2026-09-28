#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Pair 14:
  - Core Unit 14: Universal & Indefinite Relatives (b2-14)
  - Regional Unit 14: Colombia II: The Caribbean, Pacific, Afro-Colombian Heritage & Peace (b2-colombiaperiferias)
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
        "b2-unit14-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "universal principles, categorical imperatives, civic rights, and philosophical generalizations"
        },
        "relativas-universales-quiera": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "universal relatives with cualquiera and quienquiera"
        },
        "concesivas-intensivas-por-mas-que": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "intensive concessive clauses with por mas que"
        },
        "subjuntivo-reduplicado-indiferencia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "reduplicated subjunctive structures of indifference"
        },
        "cuantificadores-universales-cuanto": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "universal relative quantifiers with cuanto and todo aquel"
        },
        "generalizaciones-eticas-juridicas": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "categorical generalizations in legal and ethical registers"
        },
        "b2-colombiaperiferias-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "caribbean and pacific afro-colombian culture, palenque, collective land rights, peace accords, and amazonian conservation"
        },
        "colombia-caribe-palenque-cumbia": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "caribbean identity fortifications and palenque heritage"
        },
        "colombia-pacifico-marimba-currulao": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "pacific rainforest afro-colombian music and ecology"
        },
        "colombia-ley-setenta-derechos-etnicos": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "ancestral collective land rights and ethnic legislation"
        },
        "colombia-paz-justicia-transicional": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "peacebuilding transitional justice and memory in colombia"
        },
        "colombia-amazonia-chiribiquete-clima": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "colombian amazonia chiribiquete and environmental transition"
        }
    }
    skill_reg["skills"].update(new_skills)
    with open(skill_reg_path, "w", encoding="utf-8") as f:
        json.dump(skill_reg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated skill-registry.json for Unit 14")

    grammar_titles_path = BASE / "indexes" / "grammar-titles.json"
    with open(grammar_titles_path, "r", encoding="utf-8") as f:
        grammar_titles = json.load(f)

    new_titles = {
        "relativas-universales-quiera": "universal relatives with cualquiera and quienquiera",
        "concesivas-intensivas-por-mas-que": "intensive concessive clauses with por mas que",
        "subjuntivo-reduplicado-indiferencia": "reduplicated subjunctive structures of indifference",
        "cuantificadores-universales-cuanto": "universal relative quantifiers with cuanto and todo aquel",
        "generalizaciones-eticas-juridicas": "categorical generalizations in legal and ethical registers",
        "colombia-caribe-palenque-cumbia": "caribbean identity fortifications and palenque heritage",
        "colombia-pacifico-marimba-currulao": "pacific rainforest afro-colombian music and ecology",
        "colombia-ley-setenta-derechos-etnicos": "ancestral collective land rights and ethnic legislation",
        "colombia-paz-justicia-transicional": "peacebuilding transitional justice and memory in colombia",
        "colombia-amazonia-chiribiquete-clima": "colombian amazonia chiribiquete and environmental transition"
    }
    grammar_titles.update(new_titles)
    with open(grammar_titles_path, "w", encoding="utf-8") as f:
        json.dump(grammar_titles, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated grammar-titles.json for Unit 14")

    # =========================================================================
    # CORE UNIT 14: UNIVERSAL & INDEFINITE RELATIVES (b2-14)
    # =========================================================================

    # Lesson 1: b2-14-01 - Universal Relatives with -quiera
    c1 = "b2-14-01"
    write_json(f"vocabulary/b2/{c1}-voc.json", {
        "id": "vocab.b2.14.01",
        "lesson": c1,
        "title": "Principios universales y mandatos éticos",
        "theme": "Léxico de deontología, universalidad y preceptos inmutables",
        "words": [
            {"lemma": "precepto", "translation": "precept, rule, command", "pos": "noun"},
            {"lemma": "imperativo", "translation": "imperative, absolute duty", "pos": "noun"},
            {"lemma": "contingencia", "translation": "contingency, uncertainty", "pos": "noun"},
            {"lemma": "universalidad", "translation": "universality", "pos": "noun"},
            {"lemma": "prescribir", "translation": "to prescribe, to lay down", "pos": "verb"},
            {"lemma": "acatar", "translation": "to comply with, to abide by", "pos": "verb"},
            {"lemma": "categórico", "translation": "categorical, unconditional", "pos": "adjective"},
            {"lemma": "inalienable", "translation": "inalienable, non-transferable", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c1}-a-gr.json", {
        "id": "grammar.b2.14.01.relativas-universales-quiera",
        "title": "Oraciones relativas universales con indefinidos en -quiera",
        "sections": [
            {
                "type": "text",
                "title": "Universalidad y modo subjuntivo con pronombres y adverbios compuestos",
                "content": "Los indefinidos y relativos compuestos con '-quiera' ('quienquiera que', 'cualquiera que', 'dondequiera que', 'comoquiera que', 'cuandoquiera que') introducen cláusulas relativas o concesivas de alcance universal. Al proyectar una regla o principio que no depende de las circunstancias contingentes de un individuo o lugar concreto, seleccionan obligatoriamente el modo subjuntivo ('Dondequiera que vayas, debes acatar la ley', 'Cualquiera que sea el desenlace, mantendremos la postura')."
            },
            {
                "type": "table",
                "title": "Relativos universales y construcciones subordinadas",
                "rows": [
                    ["quienquiera que", "Quienquiera que asuma la presidencia respetará los pactos."],
                    ["cualquiera que", "Cualquiera que sea el costo político, diremos la verdad."],
                    ["dondequiera que", "Dondequiera que se vulneren derechos, habrá resistencia cívica."],
                    ["comoquiera que", "Comoquiera que se interprete la norma, el espíritu es claro."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c1}-ex.json", {
        "lesson": c1,
        "exercises": [
            {
                "id": f"{c1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el precepto", "rule, precept"],
                    ["el imperativo", "absolute duty, imperative"],
                    ["acatar", "to abide by, to comply with"],
                    ["inalienable", "non-transferable, inalienable"]
                ],
                "teaches": ["b2-unit14-vocab"]
            },
            {
                "id": f"{c1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Cualquiera que __ el fallo judicial, deberá ser acatado por todas las partes involucradas. (ser)",
                "answer": "sea",
                "english": "Whatever the judicial ruling may be, it must be abided by by all parties involved.",
                "teaches": ["relativas-universales-quiera"]
            },
            {
                "id": f"{c1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué enunciado formula un principio universal en modo subjuntivo?",
                "options": [
                    "Dondequiera que se cometan injusticias, la comunidad internacional tiene el deber de intervenir.",
                    "Dondequiera que se cometen injusticias en el pasado, hubo quejas diplomáticas.",
                    "El tribunal sesionó en el recinto donde los delegados firmaron el acta de paz."
                ],
                "correct": 0,
                "teaches": ["relativas-universales-quiera"]
            },
            {
                "id": f"{c1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Quienquiera", "que", "viole", "el", "tratado", "responderá", "ante", "los", "tribunales."],
                "solution": ["Quienquiera", "que", "viole", "el", "tratado", "responderá", "ante", "los", "tribunales."],
                "english": "Whoever violates the treaty will answer before the courts.",
                "teaches": ["relativas-universales-quiera"]
            },
            {
                "id": f"{c1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Defensor del pueblo", "text": "¿Cómo responderá el organismo si surgen presiones políticas durante la misión?"},
                    {"speaker": "Comisionada", "text": "_____"},
                    {"speaker": "Defensor del pueblo", "text": "Esa firmeza garantiza la independencia moral de la delegación."}
                ],
                "options": [
                    "Dondequiera que vayamos y cualquiera que sea la presión externa, denunciaremos las infracciones.",
                    "El informe preliminar consta de setenta páginas impresas en papel membretado.",
                    "Los vuelos hacia las capitales andinas despegan puntualmente al mediodía."
                ],
                "correct": 0,
                "teaches": ["relativas-universales-quiera"]
            },
            {
                "id": f"{c1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Cualquiera que sea el origen del litigio, debemos privilegiar el diálogo civilizado.",
                "english": "Whatever the origin of the litigation may be, we must prioritize civilized dialogue.",
                "teaches": ["relativas-universales-quiera"]
            }
        ]
    })

    write_json(f"lessons/b2/{c1}.json", make_lesson(
        stem=c1,
        unit_num=14,
        title="Relativas universales con indefinidos en -quiera",
        goal="Master the use of universal and concessive relative pronouns in -quiera with subjunctive to state categorical principles.",
        grammar_desc="oraciones relativas y concesivas universales: quienquiera que, cualquiera que, dondequiera que con subjuntivo",
        grammar_ref=f"grammar/b2/{c1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c1}-voc.json",
        ex_ref=f"exercises/b2/{c1}-ex.json",
        ex_ids=[f"{c1}.ex01", f"{c1}.ex02", f"{c1}.ex03", f"{c1}.ex04", f"{c1}.ex05", f"{c1}.ex06"],
        goals=[
            "Formulate universal ethical principles using 'quienquiera que' and 'cualquiera que'.",
            "Express spatial and modal universality with 'dondequiera que' and 'comoquiera que'.",
            "Deploy categorical duty vocabulary (precepto, imperativo, acatar)."
        ]
    ))

    # Lesson 2: b2-14-02 - Intensive Concessive Clauses with por más que
    c2 = "b2-14-02"
    write_json(f"vocabulary/b2/{c2}-voc.json", {
        "id": "vocab.b2.14.02",
        "lesson": c2,
        "title": "Obstáculos insalvables y persistencia argumentativa",
        "theme": "Léxico de tenacidad, factores adversos e ineficacia de obstáculos",
        "words": [
            {"lemma": "empeño", "translation": "determination, endeavor, effort", "pos": "noun"},
            {"lemma": "escollo", "translation": "pitfall, stumbling block", "pos": "noun"},
            {"lemma": "adversidad", "translation": "adversity, hardship", "pos": "noun"},
            {"lemma": "resistencia", "translation": "resistance, endurance", "pos": "noun"},
            {"lemma": "obstaculizar", "translation": "to hinder, to obstruct", "pos": "verb"},
            {"lemma": "persistir", "translation": "to persist, to endure", "pos": "verb"},
            {"lemma": "infructuoso", "translation": "fruitless, futile", "pos": "adjective"},
            {"lemma": "recalcitrante", "translation": "recalcitrant, stubborn", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c2}-a-gr.json", {
        "id": "grammar.b2.14.02.concesivas-intensivas-por-mas-que",
        "title": "Oraciones concesivas intensivas con por más que y por mucho que",
        "sections": [
            {
                "type": "text",
                "title": "Gradación concesiva y selección modal",
                "content": "Las estructuras concesivas intensivas ('por más que', 'por mucho que', 'por muy + adjetivo + que', 'por más + sustantivo + que') cuantifican al máximo el grado de un obstáculo para manifestar que resulta ineficaz para impedir la acción principal. Cuando el obstáculo es hipotético, futuro o irrelevante para el hablante, rige subjuntivo ('Por más que intenten intimidarnos, no cederemos'); cuando alude a un hecho real constatado en el presente o pasado, puede admitir indicativo ('Por más que se esforzó, no aprobó')."
            },
            {
                "type": "table",
                "title": "Estructuras concesivas intensivas y alternancia modal",
                "rows": [
                    ["por más que + subjuntivo", "Por más que insistan, no modificaremos los estatutos."],
                    ["por muy + adjetivo + que", "Por muy complejo que sea el reto, encontraremos una salida."],
                    ["por mucho que + indicativo", "Por mucho que protestaron, la ley fue ratificada ayer."],
                    ["por más dinero que + subjuntivo", "Por más recursos que ofrezcan, la dignidad no está en venta."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c2}-ex.json", {
        "lesson": c2,
        "exercises": [
            {
                "id": f"{c2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el escollo", "stumbling block, obstacle"],
                    ["el empeño", "effort, determination"],
                    ["obstaculizar", "to hinder, to obstruct"],
                    ["infructuoso", "fruitless, futile"]
                ],
                "teaches": ["b2-unit14-vocab"]
            },
            {
                "id": f"{c2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Por muy difícil que __ la negociación, la delegación no abandonará la mesa de concertación. (parecer)",
                "answer": "parezca",
                "english": "However difficult the negotiation may seem, the delegation will not abandon the agreement table.",
                "teaches": ["concesivas-intensivas-por-mas-que"]
            },
            {
                "id": f"{c2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la formulación concesiva intensiva más adecuada para expresar un obstáculo ineficaz futuro?",
                "options": [
                    "Por más que intenten descalificar los testimonios, la verdad histórica saldrá a la luz.",
                    "Por más que intentaban ayer descalificar los testimonios, nadie los oyó.",
                    "A pesar de que no vinieron la semana pasada a la audiencia preliminar."
                ],
                "correct": 0,
                "teaches": ["concesivas-intensivas-por-mas-que"]
            },
            {
                "id": f"{c2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Por", "mucho", "que", "presionen,", "la", "comisión", "mantendrá", "su", "independencia."],
                "solution": ["Por", "mucho", "que", "presionen,", "la", "comisión", "mantendrá", "su", "independencia."],
                "english": "However much they pressure, the commission will maintain its independence.",
                "teaches": ["concesivas-intensivas-por-mas-que"]
            },
            {
                "id": f"{c2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministra", "text": "Los sectores conservadores anuncian demandas contra el decreto ambiental. ¿Nos retractamos?"},
                    {"speaker": "Director jurídico", "text": "_____"},
                    {"speaker": "Ministra", "text": "Totalmente de acuerdo; defenderemos la constitucionalidad del decreto."}
                ],
                "options": [
                    "De ningún modo; por más recursos legales que interpongan, la protección de las selvas prevalecerá.",
                    "El presupuesto general de la nación fue aprobado en sesión extraordinaria.",
                    "Los edificios ministeriales cuentan con vigilancia privada en los accesos peatonales."
                ],
                "correct": 0,
                "teaches": ["concesivas-intensivas-por-mas-que"]
            },
            {
                "id": f"{c2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Por muy intrincado que sea el camino, persistiremos en la búsqueda de la verdad.",
                "english": "However intricate the path may be, we will persist in the search for truth.",
                "teaches": ["concesivas-intensivas-por-mas-que"]
            }
        ]
    })

    write_json(f"lessons/b2/{c2}.json", make_lesson(
        stem=c2,
        unit_num=14,
        title="Concesivas intensivas con por más que y por muy",
        goal="Deploy intensive concessive structures ('por más que', 'por mucho que', 'por muy + adj + que') with subjunctive in debate and policy analysis.",
        grammar_desc="oraciones concesivas intensivas y de gradación extrema con modo subjuntivo e indicativo",
        grammar_ref=f"grammar/b2/{c2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c2}-voc.json",
        ex_ref=f"exercises/b2/{c2}-ex.json",
        ex_ids=[f"{c2}.ex01", f"{c2}.ex02", f"{c2}.ex03", f"{c2}.ex04", f"{c2}.ex05", f"{c2}.ex06"],
        goals=[
            "Construct gradient concessives with 'por muy + adjetivo + que'.",
            "Differentiate indicative vs subjunctive in 'por más que' according to reality status.",
            "Articulate firm counter-arguments against political and procedural pressure."
        ]
    ))

    # Lesson 3: b2-14-03 - Reduplicated Subjunctive Structures of Indifference
    c3 = "b2-14-03"
    write_json(f"vocabulary/b2/{c3}-voc.json", {
        "id": "vocab.b2.14.03",
        "lesson": c3,
        "title": "Indiferencia retórica y determinación inquebrantable",
        "theme": "Léxico de resolución ética, firmeza cívica y neutralización de alternativas",
        "words": [
            {"lemma": "determinación", "translation": "determination, resolve", "pos": "noun"},
            {"lemma": "resolución", "translation": "resolution, steadfastness", "pos": "noun"},
            {"lemma": "veredicto", "translation": "verdict, judicial decision", "pos": "noun"},
            {"lemma": "inquebrantable", "translation": "unwavering, unbreakable", "pos": "adjective"},
            {"lemma": "dirimir", "translation": "to resolve, to settle a dispute", "pos": "verb"},
            {"lemma": "asumir", "translation": "to assume, to take on", "pos": "verb"},
            {"lemma": "inmutable", "translation": "immutable, unchangeable", "pos": "adjective"},
            {"lemma": "inexorable", "translation": "inexorable, relentless", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c3}-a-gr.json", {
        "id": "grammar.b2.14.03.subjuntivo-reduplicado-indiferencia",
        "title": "Estructuras reduplicadas de subjuntivo e indiferencia retórica",
        "sections": [
            {
                "type": "text",
                "title": "El esquema de reduplicación disyuntiva en nivel B2",
                "content": "Las fórmulas reduplicadas con subjuntivo ('haga lo que haga', 'diga lo que diga', 'pase lo que pase', 'sea como sea', 'venga quien venga') combinan la misma forma verbal en subjuntivo antes y después de un relativo o conector disyuntivo. Estas locuciones expresan que la determinación o el principio rector del sujeto permanecerá inalterable frente a cualquier contingencia o curso de acción que adopten terceros."
            },
            {
                "type": "table",
                "title": "Fórmulas reduplicadas de subjuntivo de alta frecuencia",
                "rows": [
                    ["diga lo que diga", "Diga lo que diga la oposición, mantendremos el compromiso social."],
                    ["haga lo que haga", "Haga lo que haga el acusado, las pruebas son concluyentes."],
                    ["cueste lo que cueste", "Cueste lo que cueste, restituiremos las tierras a las víctimas."],
                    ["sea como fuere / sea", "Sea como sea, el acuerdo firmado debe ser respetado."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c3}-ex.json", {
        "lesson": c3,
        "exercises": [
            {
                "id": f"{c3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el veredicto", "verdict, decision"],
                    ["la determinación", "resolve, determination"],
                    ["dirimir", "to settle, to resolve"],
                    ["inquebrantable", "unwavering, unbreakable"]
                ],
                "teaches": ["b2-unit14-vocab"]
            },
            {
                "id": f"{c3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Pase lo que __ en las elecciones, la política de restitución de tierras no se suspenderá. (pasar)",
                "answer": "pase",
                "english": "Whatever happens in the elections, the land restitution policy will not be suspended.",
                "teaches": ["subjuntivo-reduplicado-indiferencia"]
            },
            {
                "id": f"{c3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura reduplicada expresa resolución incondicional de forma idiomática?",
                "options": [
                    "Cueste lo que cueste, garantizaremos la seguridad de los defensores de derechos humanos.",
                    "Cuesta lo que cuesta, garantizamos ayer la seguridad de todos los delegados.",
                    "Si costara mucho dinero, abandonaríamos el proyecto inmediatamente."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-reduplicado-indiferencia"]
            },
            {
                "id": f"{c3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Diga", "lo", "que", "diga", "el", "portavoz,", "la", "comunidad", "exigirá", "justicia."],
                "solution": ["Diga", "lo", "que", "diga", "el", "portavoz,", "la", "comunidad", "exigirá", "justicia."],
                "english": "Whatever the spokesperson says, the community will demand justice.",
                "teaches": ["subjuntivo-reduplicado-indiferencia"]
            },
            {
                "id": f"{c3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Corresponsal", "text": "¿Habrá cambios en la política de memoria histórica tras el relevo ministerial?"},
                    {"speaker": "Portavoz oficial", "text": "_____"},
                    {"speaker": "Corresponsal", "text": "Un mensaje de tranquilidad para las asociaciones de víctimas."}
                ],
                "options": [
                    "Venga quien venga al ministerio, el compromiso estatal con el esclarecimiento de la verdad es innegociable.",
                    "Las salas de prensa cuentan con conexión de alta velocidad y micrófonos inalámbricos.",
                    "El archivo fotográfico fue digitalizado por técnicos del archivo general."
                ],
                "correct": 0,
                "teaches": ["subjuntivo-reduplicado-indiferencia"]
            },
            {
                "id": f"{c3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Haga lo que haga el consorcio minero, la consulta previa con los pueblos originarios es obligatoria.",
                "english": "Whatever the mining consortium does, prior consultation with indigenous peoples is mandatory.",
                "teaches": ["subjuntivo-reduplicado-indiferencia"]
            }
        ]
    })

    write_json(f"lessons/b2/{c3}.json", make_lesson(
        stem=c3,
        unit_num=14,
        title="Subjuntivo reduplicado y fórmulas de indiferencia retórica",
        goal="Master reduplicated subjunctive structures of indifference ('haga lo que haga', 'cueste lo que cueste') in asserting unwavering principles.",
        grammar_desc="estructuras reduplicadas con subjuntivo: pase lo que pase, diga lo que diga, sea como sea",
        grammar_ref=f"grammar/b2/{c3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c3}-voc.json",
        ex_ref=f"exercises/b2/{c3}-ex.json",
        ex_ids=[f"{c3}.ex01", f"{c3}.ex02", f"{c3}.ex03", f"{c3}.ex04", f"{c3}.ex05", f"{c3}.ex06"],
        goals=[
            "Formulate resolute stances with 'cueste lo que cueste' and 'pase lo que pase'.",
            "Neutralize counter-arguments using 'diga lo que diga' and 'sea como sea'.",
            "Deploy firmness and commitment vocabulary in political discourse."
        ]
    ))

    # Lesson 4: b2-14-04 - Universal Relative Quantifiers with cuanto and todo aquel
    c4 = "b2-14-04"
    write_json(f"vocabulary/b2/{c4}-voc.json", {
        "id": "vocab.b2.14.04",
        "lesson": c4,
        "title": "Cuantificación universal y colectividades jurídicas",
        "theme": "Léxico de representatividad, colectivos amparados y cuantificación legal",
        "words": [
            {"lemma": "colectividad", "translation": "collectivity, community group", "pos": "noun"},
            {"lemma": "amparo", "translation": "protection, constitutional relief", "pos": "noun"},
            {"lemma": "titularidad", "translation": "ownership, legal title", "pos": "noun"},
            {"lemma": "beneficiario", "translation": "beneficiary", "pos": "noun"},
            {"lemma": "acoger", "translation": "to welcome, to grant shelter/protection", "pos": "verb"},
            {"lemma": "abarcar", "translation": "to encompass, to cover", "pos": "verb"},
            {"lemma": "omnicomprensivo", "translation": "all-encompassing, overarching", "pos": "adjective"},
            {"lemma": "vinculado", "translation": "linked, bound", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c4}-a-gr.json", {
        "id": "grammar.b2.14.04.cuantificadores-universales-cuanto",
        "title": "Cuantificadores relativos universales: cuanto, todo aquel que y todo lo que",
        "sections": [
            {
                "type": "text",
                "title": "Sintaxis de la cuantificación distributiva universal en textos normativos",
                "content": "Los relativos cuantitativos universales ('cuanto/a/os/as', 'todo cuanto', 'todo aquel que', 'todo lo que') abarcan la totalidad de una clase o colectivo. Cuando refieren a un conjunto fáctico ya determinado, seleccionan indicativo ('Agradecemos a cuantos colaboraron'); cuando establecen una regla abstracta, condicional o hipotética aplicable a futuros beneficiarios o afectados, exigen de forma rigurosa el subjuntivo ('Se indemnizará a cuantos acrediten daños directos')."
            },
            {
                "type": "table",
                "title": "Cuantificadores universales y alternancia modal",
                "rows": [
                    ["cuantos + subjuntivo", "Se brindará amparo a cuantos huyan de la violencia armada."],
                    ["todo cuanto + indicativo", "Consignamos en el informe todo cuanto vimos durante la visita."],
                    ["todo aquel que + subjuntivo", "Todo aquel que reclame tierras ancestrales será escuchado."],
                    ["cuanta ayuda + subjuntivo", "Movilizaremos cuanta ayuda humanitaria sea necesaria."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c4}-ex.json", {
        "lesson": c4,
        "exercises": [
            {
                "id": f"{c4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el amparo", "protection, constitutional relief"],
                    ["la titularidad", "ownership, legal title"],
                    ["abarcar", "to cover, to encompass"],
                    ["omnicomprensivo", "all-encompassing"]
                ],
                "teaches": ["b2-unit14-vocab"]
            },
            {
                "id": f"{c4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El fondo de reparación asistirá a cuantos __ afectados por el despojo forzado de tierras. (resultar)",
                "answer": "resulten",
                "english": "The reparation fund will assist all those who turn out to be affected by the forced dispossession of lands.",
                "teaches": ["cuantificadores-universales-cuanto"]
            },
            {
                "id": f"{c4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración establece una norma universal abstracta con cuantificador relativo?",
                "options": [
                    "Se garantizará el derecho a la salud a cuantos habiten en los territorios colectivos.",
                    "Se atendió ayer en el hospital a cuantos llegaron heridos del combate.",
                    "Los médicos visitaron las veredas donde viven las familias campesinas."
                ],
                "correct": 0,
                "teaches": ["cuantificadores-universales-cuanto"]
            },
            {
                "id": f"{c4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Todo", "aquel", "que", "acredite", "desplazamiento", "recibirá", "asistencia", "humanitaria."],
                "solution": ["Todo", "aquel", "que", "acredite", "desplazamiento", "recibirá", "asistencia", "humanitaria."],
                "english": "Anyone who proves displacement will receive humanitarian assistance.",
                "teaches": ["cuantificadores-universales-cuanto"]
            },
            {
                "id": f"{c4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Líder comunitaria", "text": "¿Quiénes tendrán derecho a participar en las asambleas del consejo comunitario?"},
                    {"speaker": "Abogado étnico", "text": "_____"},
                    {"speaker": "Líder comunitaria", "text": "Así aseguramos la legitimidad de las decisiones de autogobierno."}
                ],
                "options": [
                    "Cuantos pertenezcan al censo ancestral y reconozcan las autoridades tradicionales tendrán voz y voto.",
                    "El salón comunal dispone de sillas plásticas y pizarra acrílica para las reuniones.",
                    "Los barcos de carga atracan dos veces por semana en el muelle fluvial."
                ],
                "correct": 0,
                "teaches": ["cuantificadores-universales-cuanto"]
            },
            {
                "id": f"{c4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La ley amparará a cuantas familias campesinas hayan sido víctimas del despojo.",
                "english": "The law will protect all peasant families that have been victims of dispossession.",
                "teaches": ["cuantificadores-universales-cuanto"]
            }
        ]
    })

    write_json(f"lessons/b2/{c4}.json", make_lesson(
        stem=c4,
        unit_num=14,
        title="Cuantificadores relativos universales: cuanto y todo aquel que",
        goal="Master the use of universal quantifiers ('cuanto', 'todo aquel que', 'todo cuanto') in formulating inclusive legal and constitutional frameworks.",
        grammar_desc="cuantificadores relativos universales (cuanto/a/os/as, todo aquel que) en subjuntivo e indicativo",
        grammar_ref=f"grammar/b2/{c4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c4}-voc.json",
        ex_ref=f"exercises/b2/{c4}-ex.json",
        ex_ids=[f"{c4}.ex01", f"{c4}.ex02", f"{c4}.ex03", f"{c4}.ex04", f"{c4}.ex05", f"{c4}.ex06"],
        goals=[
            "Formulate inclusive statutory rights using 'cuantos' and 'todo aquel que'.",
            "Distinguish factual past assertions (indicative) from general legal entitlements (subjunctive).",
            "Synthesize community rights vocabulary (amparo, titularidad, beneficiario)."
        ]
    ))

    # Lesson 5: b2-14-05 - Categorical Generalizations in Legal and Ethical Registers
    c5 = "b2-14-05"
    write_json(f"vocabulary/b2/{c5}-voc.json", {
        "id": "vocab.b2.14.05",
        "lesson": c5,
        "title": "Generalizaciones éticas y mandatos constitucionales",
        "theme": "Léxico de jurisprudencia constitucional, derechos humanos y dignidad",
        "words": [
            {"lemma": "jurisprudencia", "translation": "jurisprudence, case law", "pos": "noun"},
            {"lemma": "bloque", "translation": "constitutional block, body of law", "pos": "noun"},
            {"lemma": "ponderación", "translation": "proportionality test, balancing of rights", "pos": "noun"},
            {"lemma": "intangibilidad", "translation": "intangibility, inviolability", "pos": "noun"},
            {"lemma": "vulnerar", "translation": "to infringe, to violate", "pos": "verb"},
            {"lemma": "amparar", "translation": "to protect, to grant constitutional shelter", "pos": "verb"},
            {"lemma": "imprescriptible", "translation": "imprescriptible, not subject to statute of limitations", "pos": "adjective"},
            {"lemma": "vinculante", "translation": "binding, compulsory", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c5}-a-gr.json", {
        "id": "grammar.b2.14.05.generalizaciones-eticas-juridicas",
        "title": "Generalizaciones categóricas en el discurso jurídico y ético",
        "sections": [
            {
                "type": "text",
                "title": "El estilo sentencioso y la formulación de principios constitucionales",
                "content": "En la prosa jurídica de alto nivel (sentencias de cortes constitucionales, tratados de derecho internacional humanitario, manifiestos ciudadanos), las oraciones relativas universales e indefinidas se articulan con verbos modales de obligación ('debe', 'habrá de') y formas de subjuntivo para enunciar principios categóricos inmunes al arbitrio de coyunturas políticas temporales."
            },
            {
                "type": "table",
                "title": "Fórmulas de generalización en jurisprudencia de derechos humanos",
                "rows": [
                    ["Toda norma que vulnerare...", "Toda norma que vulnere la dignidad humana carece de validez."],
                    ["Cualquier acto que lesione...", "Cualquier acto que lesione derechos fundamentales debe ser anulado."],
                    ["Los crímenes que constituyan...", "Los crímenes que constituyan lesa humanidad son imprescriptibles."],
                    ["El Estado amparará a quien...", "El Estado amparará a quien denuncie violaciones de derechos."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c5}-ex.json", {
        "lesson": c5,
        "exercises": [
            {
                "id": f"{c5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la jurisprudencia", "case law, jurisprudence"],
                    ["la ponderación", "balancing of rights, proportionality test"],
                    ["vulnerar", "to violate, to infringe"],
                    ["imprescriptible", "not subject to statute of limitations"]
                ],
                "teaches": ["b2-unit14-vocab"]
            },
            {
                "id": f"{c5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Cualquier decreto que __ derechos inalienables será declarado inexequible por la Corte Constitucional. (vulnerar)",
                "answer": "vulnere",
                "english": "Any decree that infringes inalienable rights will be declared unconstitutional by the Constitutional Court.",
                "teaches": ["generalizaciones-eticas-juridicas"]
            },
            {
                "id": f"{c5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la formulación jurisprudencial más rigurosa para establecer la nulidad de un acto arbitrario?",
                "options": [
                    "Cualquier disposición administrativa que contradiga los tratados de derechos humanos carece de validez jurídica.",
                    "Cualquier disposición administrativa que contradijo los tratados el año pasado no tuvo consecuencias.",
                    "El tribunal analizó un decreto firmado durante la emergencia económica."
                ],
                "correct": 0,
                "teaches": ["generalizaciones-eticas-juridicas"]
            },
            {
                "id": f"{c5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "crímenes", "que", "constituyan", "lesa", "humanidad", "son", "absolutamente", "imprescriptibles."],
                "solution": ["Los", "crímenes", "que", "constituyan", "lesa", "humanidad", "son", "absolutamente", "imprescriptibles."],
                "english": "Crimes that constitute crimes against humanity are absolutely imprescriptible.",
                "teaches": ["generalizaciones-eticas-juridicas"]
            },
            {
                "id": f"{c5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Magistrada ponente", "text": "¿Cómo debe redactarse el principio rector de la sentencia de tutela?"},
                    {"speaker": "Secretario judicial", "text": "_____"},
                    {"speaker": "Magistrada ponente", "text": "Excelente formulación; recoge el canon constitucional universal."}
                ],
                "options": [
                    "Se dejará sentado que todo acto estatal que desatienda la dignidad intrínseca de la persona es nulo de pleno derecho.",
                    "Las resoluciones judiciales se publican diariamente en la secretaría del tribunal.",
                    "La biblioteca de la corte custodia ejemplares de constituciones latinoamericanas."
                ],
                "correct": 0,
                "teaches": ["generalizaciones-eticas-juridicas"]
            },
            {
                "id": f"{c5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El bloque de constitucionalidad ampara a cuantas personas se encuentren bajo la jurisdicción nacional.",
                "english": "The constitutional block protects all persons found under national jurisdiction.",
                "teaches": ["generalizaciones-eticas-juridicas"]
            }
        ]
    })

    write_json(f"lessons/b2/{c5}.json", make_lesson(
        stem=c5,
        unit_num=14,
        title="Generalizaciones éticas y mandatos constitucionales",
        goal="Apply universal relative clauses and generalizing subjunctive structures to formulate binding constitutional and human rights principles.",
        grammar_desc="generalizaciones categóricas y sentenciosas en el discurso jurídico y constitucional",
        grammar_ref=f"grammar/b2/{c5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c5}-voc.json",
        ex_ref=f"exercises/b2/{c5}-ex.json",
        ex_ids=[f"{c5}.ex01", f"{c5}.ex02", f"{c5}.ex03", f"{c5}.ex04", f"{c5}.ex05", f"{c5}.ex06"],
        goals=[
            "Formulate binding constitutional imperatives with relative clauses in subjunctive.",
            "Analyze universal human rights norms using formal jurisprudence terminology.",
            "Synthesize philosophical generalizations in institutional debate."
        ]
    ))

    # Consolidation Unit 14 (Core): b2-14-consolidation
    c_con = "b2-14-consolidation"
    write_json(f"exercises/b2/{c_con}-ex.json", {
        "lesson": c_con,
        "exercises": [
            {
                "id": f"{c_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el imperativo", "categorical duty, imperative"],
                    ["el escollo", "obstacle, stumbling block"],
                    ["el amparo", "constitutional protection"],
                    ["inquebrantable", "unbreakable, unwavering"]
                ],
                "teaches": ["b2-unit14-vocab"]
            },
            {
                "id": f"{c_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la estructura 'Cualquiera que sea el resultado' exige modo subjuntivo?",
                "options": [
                    "Porque 'cualquiera que' introduce una relatividad universal o concesiva ante un resultado aún no verificado empíricamente.",
                    "Porque el verbo 'ser' carece de conjugación en modo indicativo tras sustantivos.",
                    "Porque las oraciones de relativo siempre se construyen en pretérito perfecto."
                ],
                "correct": 0,
                "teaches": ["relativas-universales-quiera"]
            },
            {
                "id": f"{c_con}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Por más recursos que __ los monopolios, la soberanía territorial de los pueblos originarios es inalienable. (invertir)",
                "answer": "inviertan",
                "english": "However many resources monopolies invest, the territorial sovereignty of indigenous peoples is inalienable.",
                "teaches": ["concesivas-intensivas-por-mas-que"]
            },
            {
                "id": f"{c_con}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Pase", "lo", "que", "pase,", "la", "comisión", "publicará", "su", "informe", "final."],
                "solution": ["Pase", "lo", "que", "pase,", "la", "comisión", "publicará", "su", "informe", "final."],
                "english": "Whatever happens, the commission will publish its final report.",
                "teaches": ["subjuntivo-reduplicado-indiferencia"]
            },
            {
                "id": f"{c_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué diferencia existe entre 'Ayudaremos a cuantos soliciten amparo' y 'Ayudamos a cuantos solicitaron amparo'?",
                "options": [
                    "La primera formula una regla abstracta prospectiva (subjuntivo); la segunda describe una acción empírica realizada en el pasado (indicativo).",
                    "Ambas expresan una hipótesis irreal sobre el presente sin distinción de significado.",
                    "La primera es un uso incorrecto que debe sustituirse por el tiempo futuro de indicativo."
                ],
                "correct": 0,
                "teaches": ["cuantificadores-universales-cuanto"]
            },
            {
                "id": f"{c_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Observador internacional", "text": "¿Qué garantía tienen los líderes sociales amenazados en las zonas rurales?"},
                    {"speaker": "Procuradora", "text": "_____"},
                    {"speaker": "Observador internacional", "text": "Esa es la postura categórica que demandan los estándares internacionales."}
                ],
                "options": [
                    "Dondequiera que se encuentren y cueste lo que cueste, el Estado tiene el deber ineludible de salvaguardar sus vidas.",
                    "Los vehículos de transporte rural operan con combustibles convencionales.",
                    "La capital departamental cuenta con hoteles para los visitantes diplomáticos."
                ],
                "correct": 0,
                "teaches": ["relativas-universales-quiera"]
            },
            {
                "id": f"{c_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Cualquier ley que menoscabe la consulta previa con las comunidades será declarada inconstitucional.",
                "english": "Any law that undermines prior consultation with communities will be declared unconstitutional.",
                "teaches": ["generalizaciones-eticas-juridicas"]
            },
            {
                "id": f"{c_con}.ex08",
                "type": "sentence-builder",
                "category": "writing",
                "tiles": ["Por", "muy", "ardua", "que", "sea", "la", "tarea,", "construiremos", "una", "paz", "duradera."],
                "solution": ["Por", "muy", "ardua", "que", "sea", "la", "tarea,", "construiremos", "una", "paz", "duradera."],
                "english": "However arduous the task may be, we will build an enduring peace.",
                "teaches": ["concesivas-intensivas-por-mas-que"]
            }
        ]
    })

    # Classic Story for Unit 14: José Eustasio Rivera - La vorágine
    story_core_14 = {
        "id": "b2-14",
        "title": "José Eustasio Rivera: La vorágine",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de nivel B2 de La vorágine de José Eustasio Rivera: la fuga novelesca de Arturo Cova y Alicia hacia los Llanos del Orinoco, el descenso dantesco a la selva amazónica y la denuncia implacable del holocausto cauchero en las barracas de la Casa Arana.",
        "characters": [
            "Arturo Cova",
            "Alicia",
            "Clemente Silva",
            "La Selva"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "'Antes de que me hubiera apasionado por mujer alguna, jugué mi corazón al azar y me lo ganó la violencia'. Con esta confesión desgarradora y lapidaria abre Arturo Cova, poeta bogotano de temperamento arrebatado e inestable, el manuscrito en el que consignó su descenso a los infiernos del mundo amazónico. Acompañado por Alicia, una joven de buena familia que huyó con él para eludir un matrimonio impuesto por las convenciones asfixiantes de la sociedad andina, Cova galopó durante semanas a través de las inmensas planicies de los Llanos del Casanare. Bajo un horizonte infinito donde el cielo y la hierba brava se fundían en tempestades eléctricas, los amantes creyeron hallar un refugio heroico y salvaje; sin embargo, aquel espejismo pastoril apenas constituyó el preludio de una pesadilla mucho más honda y colosal."
            },
            {
                "type": "narration",
                "text": "La traición de hacendados inescrupulosos y la desaparición de Alicia empujaron al poeta a traspasar el límite donde terminan los llanos abiertos y comienza la maraña impenetrable de la selva tropical. Al internarse en el territorio tenebroso de los ríos Vichada, Guaviare y Amazonas, la naturaleza dejó de ser el idílico paisaje contemplado por los románticos para transformarse en una entidad viva, devoradora y trágica: una catedral vegetal atestada de miasmas fétidos, lianas parasitarias, fiebres palúdicas y una perpetua semipenumbra donde los árboles gigantescos libraban una lucha despiadada por alcanzar una rendija de sol. Dondequiera que fijaran la mirada los extraviados expedicionarios, la selva proclamaba su soberanía hostil sobre la debilidad humana."
            },
            {
                "type": "narration",
                "text": "Allí, en el corazón verde del continente, Cova descubrió un horror infinitamente más atroz que las alimañas o las ciénagas ponzoñosas: la explotación salvaje de la fiebre del caucho. Empresas transnacionales y capataces desalmados habían instaurado en las cuencas del Putumayo y del Caquetá un régimen siniestro de esclavitud moderna. Miles de indígenas huitotos, boras y ocainas eran cazados en sus malocas ancestrales, encadenados y obligados bajo tortura a sangrar los troncos de las siringuillas para extraer el 'oro blanco' que alimentaba la voracidad industrial de Europa y Norteamérica. Quienquiera que no entregara la cuota semanal de látex era azotado sin piedad, mutilado en el cepo o condenado a morir de hambre en las barracas del exterminio."
            },
            {
                "type": "narration",
                "text": "En medio de aquella vorágine de degradación moral emergió la figura conmovedora de Don Clemente Silva, un viejo cauchero mestizo de paso cansino y mirada noble que recorría los ríos amazónicos desde hacía dieciséis años. Don Clemente no buscaba riquezas ni látex; buscaba incansablemente los huesos de su hijo Luciano, asesinado en las trochas del caucho, para darles cristiana sepultura en su tierra natal. Guiado por ese amor paternal inquebrantable, el anciano conocía cada meandro de río, cada sendero secreto de siringal y cada engaño de los enganchadores de peones, encarnando la dignidad moral y la memoria herida de un pueblo sojuzgado por la codicia desmedida."
            },
            {
                "type": "narration",
                "text": "Conmovido por el testimonio de Don Clemente y enloquecido por la sed de justicia y venganza, Arturo Cova transformó su pluma lírica en un instrumento de acusación inapelable. En las páginas febriles de su diario denunció los crímenes de lesa humanidad perpetrados por la infame Casa Arana, documentando los nombres de los verdugos, los abusos contra las mujeres nativas y el despoblamiento sistemático de cuencas fluviales enteras. Comprendió con lúcida amargura que, por más que la civilización urbana presumiera de progreso y refinamiento en los salones de las capitales, sus cimientos materiales reposaban sobre la sangre inocente derramada en las tinieblas de la manigua."
            },
            {
                "type": "narration",
                "text": "El desenlace de la epopeya condensó el destino trágico de quienes osaron desafiar a la selva amazónica sin dominar sus misterios sagrados. Tras rescatar a Alicia y a su pequeño hijo recién nacido en un campamento abandonado, Cova y su mermado grupo de fugitivos se internaron desesperadamente en las profundidades del bosque fluvial para eludir a sus perseguidores. Meses después, un cónsul colombiano enviado a la frontera fluvial remitió un telegrama escueto y desolador al ministerio en Bogotá que selló para siempre la memoria literaria de América Latina: 'Los buscó inútilmente el cónsul. ¡Ni rastro de ellos! ¡Los devoró la selva!'. La gran novela de José Eustasio Rivera pervivió así como un grito universal de denuncia y una advertencia eterna sobre los abismos a los que conduce la ambición ciega del hombre."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué motivó inicialmente la huida de Arturo Cova y Alicia hacia los Llanos del Casanare?",
                        "options": [
                            "El deseo de eludir una boda concertada por la familia de Alicia y romper con las asfixiantes convenciones sociales andinas.",
                            "Una misión militar oficial encomendada por el gobierno para vigilar la frontera con Venezuela.",
                            "La búsqueda deliberada de yacimientos de caucho para enriquecerse con el comercio internacional.",
                            "Una invitación para fundar una colonia científica en las cabeceras del río Orinoco."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 relata que Alicia huyó con Cova para evitar un matrimonio impuesto por su familia según las normas asfixiantes de la sociedad andina."
                    },
                    {
                        "question": "¿Cuál es la misión fundamental que impulsa a Don Clemente Silva en la selva amazónica?",
                        "options": [
                            "Buscar incansablemente los restos mortales de su hijo Luciano para darles sepultura digna.",
                            "Acumular toneladas de caucho para comprar una hacienda ganadera en los llanos.",
                            "Construir un aserradero industrial en las márgenes del río Putumayo.",
                            "Guiar a los ejércitos coloniales hacia las ciudades perdidas del Dorado."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 explica que el viejo cauchero llevaba dieciséis años recorriendo los ríos para encontrar los huesos de su hijo asesinado."
                    },
                    {
                        "question": "¿Qué denuncia de orden histórico y social encierra la obra *La vorágine* de José Eustasio Rivera?",
                        "options": [
                            "Denuncia el régimen de esclavitud, tortura y exterminio sistemático sufrido por los pueblos indígenas durante la fiebre del caucho.",
                            "Critica la falta de caminos pavimentados entre Bogotá y las capitales de provincia.",
                            "Sostiene que la selva amazónica debía ser talada por completo para el desarrollo agropecuario.",
                            "Advierte que la poesía lírica carece de valor frente a los tratados de comercio marítimo."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 y 5 detallan que la novela expone el régimen atroz de esclavitud y las atrocidades de la Casa Arana contra los indígenas amazónicos."
                    }
                ]
            }
        }
    }
    write_json(f"stories/classics/b2/{c_con.replace('-consolidation', '')}.json", story_core_14)

    write_json(f"lessons/b2/{c_con}.json", make_consolidation_lesson(
        stem=c_con,
        unit_num=14,
        title="Consolidación: Universalidad, principios inmutables y la selva devoradora",
        goal="Consolidate upper-intermediate mastery of universal relatives, intensive concessives, and reduplicated subjunctive structures in philosophical and classical literary discourse.",
        grammar_desc="repaso integral de relativas universales (-quiera), concesivas de gradación extrema y fórmulas de determinación",
        ex_ref=f"exercises/b2/{c_con}-ex.json",
        ex_ids=[f"{c_con}.ex01", f"{c_con}.ex02", f"{c_con}.ex03", f"{c_con}.ex04", f"{c_con}.ex05", f"{c_con}.ex06", f"{c_con}.ex07", f"{c_con}.ex08"],
        goals=[
            "Synthesize universal relatives ('cualquiera que', 'quienquiera que', 'dondequiera que').",
            "Deploy intensive concessives ('por más que', 'por muy + adj + que') in high-level argumentation.",
            "Analyze literary and humanitarian themes using categorical ethical frameworks."
        ],
        checklist_items=[
            "Formulo principios categóricos con pronombres en '-quiera' y subjuntivo.",
            "Utilizo estructuras concesivas intensivas ('por más que', 'por mucho que').",
            "Manejo las fórmulas reduplicadas de resolución ('cueste lo que cueste', 'pase lo que pase').",
            "Aplico cuantificadores universales ('cuanto', 'todo aquel que') en contextos normativos."
        ],
        story_ref=f"stories/classics/b2/{c_con.replace('-consolidation', '')}.json"
    ))
    print("Completed Core Unit 14 generation!")

    # =========================================================================
    # REGIONAL UNIT 14: COLOMBIA II: CARIBBEAN, PACIFIC, AFRO-COLOMBIAN & PEACE (b2-colombiaperiferias)
    # =========================================================================

    # Lesson 1: b2-colombiaperiferias-01 - Cartagena y el Caribe: Palenque y cumbia
    r1 = "b2-colombiaperiferias-01"
    write_json(f"vocabulary/b2/{r1}-voc.json", {
        "id": "vocab.b2.colombiaperiferias.01",
        "lesson": r1,
        "title": "Cartagena y el Caribe: Murallas, cimarronaje y cumbia",
        "theme": "Historia colonial cartagenera, San Basilio de Palenque, tambores y vallenato",
        "words": [
            {"lemma": "cimarronaje", "translation": "marronage, flight from slavery", "pos": "noun"},
            {"lemma": "baluarte", "translation": "bastion, bulwark, stronghold", "pos": "noun"},
            {"lemma": "palenque", "translation": "palenque (walled maroon community of freed slaves)", "pos": "noun"},
            {"lemma": "tambora", "translation": "tambora (traditional Afro-Caribbean bass drum)", "pos": "noun"},
            {"lemma": "manumitir", "translation": "to manumit, to legally emancipate", "pos": "verb"},
            {"lemma": "sublevarse", "translation": "to revolt, to rise up", "pos": "verb"},
            {"lemma": "fortificado", "translation": "fortified", "pos": "adjective"},
            {"lemma": "ancestral", "translation": "ancestral, traditional", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r1}-a-gr.json", {
        "id": "grammar.b2.colombiaperiferias.01.colombia-caribe-palenque-cumbia",
        "title": "Cartagena colonial, San Basilio de Palenque y la herencia afrocaribeña",
        "sections": [
            {
                "type": "text",
                "title": "Discurso histórico de resistencia cimarrona y patrimonio inmaterial",
                "content": "El estudio del Caribe colombiano en nivel B2 articula el esplendor militar de Cartagena de Indias con la gesta emancipadora de San Basilio de Palenque (primer pueblo libre de América, fundado por Benkos Biohó en el siglo XVII y declarado patrimonio oral e inmaterial por la UNESCO). Se analizan estructuras relativas y concesivas que subrayan la supervivencia de la lengua criolla palenquera y los ritmos de cumbia y bullerengue."
            },
            {
                "type": "table",
                "title": "Hitos culturales e históricos del Caribe afrocolombiano",
                "rows": [
                    ["Benkos Biohó", "Líder cimarrón que forzó a la corona a firmar la paz en 1691."],
                    ["San Basilio de Palenque", "Primer pueblo libre de América que conservó su lengua criolla."],
                    ["Murallas de Cartagena", "Fortificaciones pétreas construidas con mano de obra esclava."],
                    ["Cumbia y bullerengue", "Ritmos ancestrales en los que el tambor dialoga con el canto."]
                ]
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
                    ["el cimarronaje", "flight from slavery, marronage"],
                    ["el baluarte", "bastion, bulwark"],
                    ["el palenque", "walled maroon community"],
                    ["sublevarse", "to revolt, to rise up"]
                ],
                "teaches": ["b2-colombiaperiferias-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "San Basilio de Palenque fue el primer poblado de América en el que los esclavizados __ su libertad legal. (conquistar)",
                "answer": "conquistaron",
                "english": "San Basilio de Palenque was the first settlement in the Americas in which enslaved people conquered their legal freedom.",
                "teaches": ["colombia-caribe-palenque-cumbia"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué singularidad sociolingüística distingue a San Basilio de Palenque según la UNESCO?",
                "options": [
                    "Es el único palenque colonial donde se preservó intacta una lengua criolla de base léxica española con gramática bantú.",
                    "Es una fortaleza donde se hablaba exclusivamente el latín eclesiástico.",
                    "Es una comunidad donde se prohibió el uso de tambores e instrumentos africanos."
                ],
                "correct": 0,
                "teaches": ["colombia-caribe-palenque-cumbia"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Las", "murallas", "de", "Cartagena", "fueron", "levantadas", "frente", "a", "los", "piratas."],
                "solution": ["Las", "murallas", "de", "Cartagena", "fueron", "levantadas", "frente", "a", "los", "piratas."],
                "english": "The walls of Cartagena were erected against pirates.",
                "teaches": ["colombia-caribe-palenque-cumbia"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora antillana", "text": "¿Por qué el tratado de paz de 1691 entre la corona española y Palenque es tan revolucionario?"},
                    {"speaker": "Antropólogo palenquero", "text": "_____"},
                    {"speaker": "Historiadora antillana", "text": "Un hito precursor de la libertad más de un siglo antes de las independencias republicanas."}
                ],
                "options": [
                    "Porque reconoció la autonomía territorial y la libertad incondicional de los cimarrones liderados por Benkos Biohó.",
                    "El puerto comercial de Cartagena movilizaba cargamentos de café hacia los mercados europeos.",
                    "Las playas de Bocagrande cuentan con modernos complejos turísticos frente al mar Caribe."
                ],
                "correct": 0,
                "teaches": ["colombia-caribe-palenque-cumbia"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La cumbia y el bullerengue expresan la resiliencia y la alegría creadora del pueblo afrocaribeño.",
                "english": "Cumbia and bullerengue express the resilience and creative joy of the Afro-Caribbean people.",
                "teaches": ["colombia-caribe-palenque-cumbia"]
            }
        ]
    })

    story_col2_01 = {
        "id": "b2-colombiaperiferias-01",
        "title": "Cartagena y Palenque: El eco de los tambores libertarios",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica histórica y etnomusical de nivel B2 sobre el Caribe colombiano: la imponencia de las fortificaciones coloniales de Cartagena de Indias, la gesta heroica de Benkos Biohó, el legado de San Basilio de Palenque como primer pueblo libre de América y la vitalidad de la cumbia ancestral.",
        "characters": [
            "Maestro Rafael Cassiani",
            "Soraya",
            "Profesor Valdelamar"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Frente a las aguas turquesas del mar Caribe, la silueta monumental de Cartagena de Indias se recorta como una formidable coraza de piedra y caliza. Sus baluartes, almenas y murallas ciclópeas —que requirieron más de dos siglos de fatigas constructivas para blindar al principal puerto del imperio español contra los asaltos despiadados de corsarios ingleses y franceses— encierran un pasado de grandezas palaciegas y crueles dolores humanos. Por estas mismas dársenas donde hoy pasean turistas cosmopolitas entraron durante centurias encadenados en las bodegas inmundas de los galeones negreros más de un millón de seres humanos secuestrados en las costas de África occidental, destinados a alimentar con su sudor las minas de oro del interior andino y las plantaciones azucareras del litoral."
            },
            {
                "type": "narration",
                "text": "Sin embargo, en este mismo rincón caribeño floreció la respuesta más altiva y conmovedora que conoció el continente frente a la ignominia de la esclavitud: el cimarronaje. Hombres y mujeres de indomable coraje rompieron sus cadenas, huyeron hacia las ciénagas intrincadas y los bosques cerrados de los Montes de María, y levantaron 'palenques', aldeas fortificadas con empalizadas invisibles donde se juramentaron vivir en absoluta libertad o perecer en el empeño. A la cabeza de aquella gesta libertaria descolló la figura legendaria de Benkos Biohó, un monarca africano originario de la región de Guinea-Bisáu que desafió con éxito militar a sucesivos gobernadores virreinales."
            },
            {
                "type": "narration",
                "text": "El resultado supremo de esa resistencia indoblegable fue San Basilio de Palenque, ubicado a escasos sesenta kilómetros de Cartagena. En 1691, abrumada por la imposibilidad militar de someter a los rebeldes y forzada por constantes escaramuzas guerrilleras, la corona española se vio obligada a emitir una Real Cédula que reconoció la libertad incondicional y la soberanía territorial de los palenqueros. San Basilio se convirtió así en el primer pueblo libre de toda América, anticipándose en más de un siglo a la gesta independentista de Haití y a las campañas republicanas de Simón Bolívar."
            },
            {
                "type": "narration",
                "text": "Caminar hoy por las calles polvorientas de San Basilio de Palenque supone adentrarse en un santuario vivo de la memoria ancestral, declarado en 2005 por la UNESCO como Obra Maestra del Patrimonio Oral e Inmaterial de la Humanidad. Es el único enclave del hemisferio occidental donde sobrevive intacta una lengua criolla singular —el palenquero—, articulada sobre una base léxica castellana pero estructurada mediante la sintaxis y la morfología tonal de las lenguas de la familia bantú del centro de África, preservada celosamente por los mayores a través de cantos fúnebres de 'lumbalú' y relatos comunitarios transmitidos de generación en generación."
            },
            {
                "type": "narration",
                "text": "El maestro Rafael Cassiani, veterano director del legendario Sexteto Tabalá, afina el cuero curtido de su tambora mientras Soraya, una joven investigadora palenquera, traduce frases del criollo para el profesor Valdelamar. 'Los blancos creyeron que al despojarnos de la tierra natal nos habían arrebatado el alma; ignoraban que la libertad venía escondida en los ritmos secretos de nuestros tambores pechiche y alegre, y en las trenzas de nuestras abuelas, que dibujaban en sus cabezas los mapas de fuga hacia el monte', proclama el maestro Cassiani con una sonrisa sabia que ilumina su rostro curtido."
            },
            {
                "type": "narration",
                "text": "Asimismo, las comunidades palenqueras han consolidado una organización social única basada en los 'ma-kuagro', redes solidarias de ayuda mutua divididas por grupos de edad que garantizan el cuidado colectivo de los niños, el trabajo agrícola compartido y la protección de los ancianos sabedores. En los callejones de tierra de Palenque, el saludo cotidiano en lengua materna reafirma una soberanía comunitaria que resistió siglos de olvido estatal: aquí cada palabra pronunciada y cada dulce de coco y panela elaborado por las 'palenqueras' con sus tradicionales bateas de aluminio sobre la cabeza constituye un testimonio vivo de dignidad y soberanía cultural."
            },
            {
                "type": "narration",
                "text": "De esa matriz de resistencia y mestizaje brotaron los compases hipnóticos de la cumbia, el bullerengue y el vallenato tradicional, músicas donde la gaita indígena de caña de millo se funde en un abrazo fecundo con el repique impetuoso del tambor africano y la copla lírica española. Cartagena y Palenque confirman que el alma del Caribe colombiano no se reduce a sus murallas pétreas ni a sus atardeceres de postal, sino que vibra en la voz altiva de un pueblo que transformó el grito del despojo en una sinfonía inextinguible de libertad, dignidad y memoria compartida ante el mundo."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito histórico continental protagonizó San Basilio de Palenque en 1691?",
                        "options": [
                            "Se convirtió en el primer pueblo libre de América al lograr que la corona española reconociera legalmente su libertad y autonomía.",
                            "Fue el puerto donde desembarcaron las primeras tropas aliadas británicas para apoyar la independencia.",
                            "Fue la sede del primer congreso continental de gobernadores coloniales del Caribe.",
                            "Fue una fortaleza construida por los corsarios holandeses para atacar Cartagena."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 explica que en 1691 la corona española emitió una cédula reconociendo la libertad de Palenque, convirtiéndolo en el primer pueblo libre de América."
                    },
                    {
                        "question": "¿Qué singularidad lingüística distingue a la lengua palenquera según el texto?",
                        "options": [
                            "Es una lengua criolla con base léxica española pero estructurada con la sintaxis y morfología de las lenguas africanas bantúes.",
                            "Es un dialecto derivado exclusivamente del francés colonial antillano.",
                            "Es una variante arcaica del latín clásico conservada por órdenes monásticas.",
                            "Es un sistema de comunicación basado únicamente en señas sin componentes orales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 precisa que el palenquero combina vocabulario español con la estructura gramatical y tonal de las lenguas bantúes de África central."
                    },
                    {
                        "question": "¿Qué función cumplían las trenzas en el cabello de las mujeres esclavizadas según el testimonio del maestro Cassiani?",
                        "options": [
                            "Dibujaban mapas secretos de caminos y rutas de escape hacia los palenques y guardaban pequeñas semillas para sembrar.",
                            "Eran adornos estéticos obligatorios exigidos por las autoridades de la inquisición colonial.",
                            "Servían para distinguir a las familias reales de las comunidades comerciales del puerto.",
                            "Eran códigos numéricos para llevar la contabilidad del comercio de telas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 resalta que las trenzas de las abuelas trazaban los mapas de fuga hacia el monte para alcanzar la libertad."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r1}.json", story_col2_01)

    write_json(f"lessons/b2/{r1}.json", make_lesson(
        stem=r1,
        unit_num=14,
        title="Cartagena y la costa Caribe: Fortificaciones, San Basilio de Palenque y cumbia",
        goal="Explore Cartagena's colonial fortifications, the maroon revolution of San Basilio de Palenque, and the Afro-Caribbean musical heritage.",
        grammar_desc="narrativa histórica del cimarronaje y patrimonio afrocaribeño",
        grammar_ref=f"grammar/b2/{r1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r1}-voc.json",
        ex_ref=f"exercises/b2/{r1}-ex.json",
        ex_ids=[f"{r1}.ex01", f"{r1}.ex02", f"{r1}.ex03", f"{r1}.ex04", f"{r1}.ex05", f"{r1}.ex06"],
        goals=[
            "Trace the historical importance of San Basilio de Palenque as the first free town in the Americas.",
            "Analyze the linguistic uniqueness of the Palenquero Creole language.",
            "Deploy Afro-Caribbean historical and musical vocabulary (cimarronaje, palenque, tambora)."
        ],
        story_ref=f"stories/world/b2/{r1}.json"
    ))

    # Lesson 2: b2-colombiaperiferias-02 - El Pacífico colombiano: Selva húmeda, currulao y marimba
    r2 = "b2-colombiaperiferias-02"
    write_json(f"vocabulary/b2/{r2}-voc.json", {
        "id": "vocab.b2.colombiaperiferias.02",
        "lesson": r2,
        "title": "El Pacífico: Biodiversidad selvática, marimba y cantos de boga",
        "theme": "Chocó biogeográfico, currulao, marimba de chonta, manglares y cantadoras",
        "words": [
            {"lemma": "chonta", "translation": "chonta (hard palm wood used for marimba keys)", "pos": "noun"},
            {"lemma": "currulao", "translation": "currulao (traditional Afro-Pacific marimba rhythm and dance)", "pos": "noun"},
            {"lemma": "cantadora", "translation": "traditional female Pacific singer / keeper of oral songs", "pos": "noun"},
            {"lemma": "manglar", "translation": "mangrove forest, tidal wetland", "pos": "noun"},
            {"lemma": "pluvial", "translation": "rainy, pluvial, high precipitation", "pos": "adjective"},
            {"lemma": "enarbolar", "translation": "to raise up, to hold high as a banner", "pos": "verb"},
            {"lemma": "biogeográfico", "translation": "biogeographical", "pos": "adjective"},
            {"lemma": "ancestral", "translation": "ancestral, traditional", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r2}-a-gr.json", {
        "id": "grammar.b2.colombiaperiferias.02.colombia-pacifico-marimba-currulao",
        "title": "El Pacífico colombiano: Ecosistemas de lluvia, marimba y cantos tradicionales",
        "sections": [
            {
                "type": "text",
                "title": "Etnomusicología del Pacífico y discurso de conservación selvática",
                "content": "La región del Pacífico colombiano (que abarca los departamentos de Chocó, Valle del Cauca, Cauca y Nariño) integra una de las selvas pluviales más húmedas y biodiversas del planeta con la música tradicional de marimba y los cantos ancestrales (declarados patrimonio inmaterial por la UNESCO). Se despliegan oraciones descriptivas complejas y relativas para analizar la relación simbiótica entre comunidad afrodescendiente y selva húmeda."
            },
            {
                "type": "table",
                "title": "Símbolos del Pacífico biogeográfico y musical",
                "rows": [
                    ["Marimba de chonta", "Instrumento de percusión apodado 'el piano de la selva'."],
                    ["Festival Petronio Álvarez", "Mayor encuentro de músicas tradicionales afro del Pacífico."],
                    ["Chocó biogeográfico", "Región con precipitaciones anuales superiores a diez mil milímetros."],
                    ["Alabaos y gualíes", "Cantos fúnebres y espirituales entonados por cantadoras."]
                ]
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
                    ["la chonta", "hard palm wood for marimbas"],
                    ["el currulao", "traditional Pacific marimba rhythm"],
                    ["la cantadora", "traditional female singer"],
                    ["el manglar", "mangrove forest"]
                ],
                "teaches": ["b2-colombiaperiferias-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La marimba de chonta es un instrumento sagrado que __ las cadencias del agua y la lluvia en la selva pacífica. (reproducir)",
                "answer": "reproduce",
                "english": "The chonta marimba is a sacred instrument that reproduces the cadences of water and rain in the Pacific jungle.",
                "teaches": ["colombia-pacifico-marimba-currulao"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo climatológico singular distingue a la selva pluvial del Chocó biogeográfico?",
                "options": [
                    "Es una de las zonas con mayor pluviosidad del planeta, superando en algunos puntos los diez mil milímetros de lluvia al año.",
                    "Es una meseta desértica donde casi nunca se registran precipitaciones.",
                    "Es un glaciar polar donde la nieve cubre los manglares marítimos."
                ],
                "correct": 0,
                "teaches": ["colombia-pacifico-marimba-currulao"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Las", "cantadoras", "del", "Pacífico", "custodian", "la", "memoria", "ancestral", "del", "río."],
                "solution": ["Las", "cantadoras", "del", "Pacífico", "custodian", "la", "memoria", "ancestral", "del", "río."],
                "english": "The traditional Pacific singers guard the ancestral memory of the river.",
                "teaches": ["colombia-pacifico-marimba-currulao"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Musicólogo francés", "text": "¿Qué dimensión social convoca cada año el Festival Petronio Álvarez en Cali?"},
                    {"speaker": "Gestora cultural de Buenaventura", "text": "_____"},
                    {"speaker": "Musicólogo francés", "text": "Un auténtico templo de hermandad afrodescendiente."}
                ],
                "options": [
                    "Es la fiesta de afirmación comunitaria donde los sonidos de marimba, guasá y cununo unen a miles de familias del litoral.",
                    "La feria de tecnología automotriz presenta modelos eléctricos de exportación.",
                    "El puerto fluvial de Magangué recibe lanchas procedentes del bajo Cauca."
                ],
                "correct": 0,
                "teaches": ["colombia-pacifico-marimba-currulao"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El sonido de la marimba de chonta dialoga con el murmullo incesante de las mareas pacíficas.",
                "english": "The sound of the chonta marimba dialogues with the incessant murmur of the Pacific tides.",
                "teaches": ["colombia-pacifico-marimba-currulao"]
            }
        ]
    })

    story_col2_02 = {
        "id": "b2-colombiaperiferias-02",
        "title": "El Pacífico: La selva de la lluvia y el piano de chonta",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica geográfica y musical de nivel B2 sobre el litoral Pacífico colombiano: el Chocó biogeográfico como una de las regiones más lluviosas y biodiversas de la Tierra, la navegación por los ríos caudalosos como el Atrato y el San Juan, la marimba de chonta como piano de la selva y el vibrante rito del currulao.",
        "characters": [
            "Baudilio Cuero",
            "Maura Hinestroza",
            "Yulimar"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Aislada durante siglos tras la imponente muralla de la cordillera Occidental andina, la franja costera del Pacífico colombiano se despliega como un universo esmeralda donde el océano y la selva pluvial tropical se funden en una comunión sobrecogedora. Abarcando los territorios litorales de los departamentos de Chocó, Valle del Cauca, Cauca y Nariño, el Chocó biogeográfico constituye una de las ecorregiones más exuberantes, vírgenes y complejas de todo el globo terráqueo. En municipios selváticos como Lloró o López de Micay, las nubes empujadas incansablemente por los vientos húmedos del océano descargan precipitaciones que superan con holgura los diez mil milímetros anuales, situando a este rincón como una de las mecas pluviales indiscutibles de la Tierra."
            },
            {
                "type": "narration",
                "text": "En esta geografía anfibia donde no existen carreteras terrestres pavimentadas y el transporte depende enteramente de la marea marina y de los meandros caudalosos de ríos colosales como el Atrato, el San Juan o el Patía, las comunidades afrodescendientes e indígenas emberá y wounaan desarrollaron un modo de habitar respetuoso con la exuberancia natural. Casas levantadas sobre pilotes de madera de mangle para evitar las crecientes súbitas, canoas o 'potrillos' esculpidos en un solo tronco de cedro y una agricultura tradicional de pancoger en terrazas inundables confirman la sabiduría de pueblos que no intentaron doblegar a la selva, sino armonizar sus ritmos biológicos con sus ciclos inmemoriales."
            },
            {
                "type": "narration",
                "text": "El alma espiritual y musical de este territorio palpita con fuerza inigualable en la marimba de chonta, prodigio organológico conocido con justicia como 'el piano de la selva' y proclamado por la UNESCO como Patrimonio Cultural Inmaterial de la Humanidad. Construida de forma enteramente artesanal, sus teclas son elaboradas a partir de la madera fibrosa y durísima de la palma de chonta (*Bactris gasipaes*), la cual debe ser curada y afinada a fuego lento bajo la luz de la luna menguante para obtener una resonancia limpia y aterciopelada. Debajo de cada tablilla de madera cuelgan tubos resonadores de bambú guadua que amplifican las notas percutidas con mazos forrados de caucho natural."
            },
            {
                "type": "narration",
                "text": "Cuando en los poblados fluviales como Guapi o Timbiquí suena el golpe cadencioso del currulao, el tiempo ordinario queda suspendido. Dos marimberos se alternan sobre el mismo teclado ejecutando el 'bordeón' —base rítmica grave y constante— y la 'revuelta' —improvisaciones agudas y vertiginosas que imitan el rumor de las cascadas—. A su lado, los tambores cununos macho y hembra marcan el pulso sincopado, las 'cantadoras' baten los guasás de semillas secas y entonan coplas polifónicas con voces desgarradoras y potentes que narran historias de navegación, amores de orilla y dolores de la memoria cimarrona."
            },
            {
                "type": "narration",
                "text": "Don Baudilio Cuero, veterano lutier y maestro marimbero de Buenaventura, enseña los secretos de la afinación tradicional a su nieta Yulimar mientras la renombrada cantadora Maura Hinestroza entona un 'alabao' sagrado. 'Esta marimba no suena a metal ni a fábrica; suena al agua cristalina golpeando las piedras de la quebrada y al viento nocturno colándose entre las hojas de los manglares', reflexiona Don Baudilio conmovido. 'Nuestros antepasados nos legaron este sonido para que nunca olvidáramos que la música es nuestra mayor trinchera de dignidad y resistencia espiritual'."
            },
            {
                "type": "narration",
                "text": "El universo del Pacífico se enriquece además con una cosmovisión ribereña donde las mareas altas y bajas, bautizadas como 'pujas' y 'quiebras', dictan el ritmo de las labores agrícolas, la recolección de moluscos en los lodazales y las faenas de pesca artesanal. Las parteras tradicionales de los ríos, portadoras de saberes botánicos ancestrales sobre las plantas medicinales de la selva profunda, traen al mundo a las nuevas generaciones mientras entonan versos protectores, asegurando que el cordón umbilical de cada recién nacido sea sembrado simbólicamente bajo un árbol tutelar para sellar su lealtad perpetua con la tierra y el río."
            },
            {
                "type": "narration",
                "text": "Cada mes de agosto, en la ciudad de Cali, más de cien mil personas se congregan en el Festival de Música del Pacífico Petronio Álvarez, la mayor celebración de cultura afrodescendiente de América Latina. Entre pañuelos blancos ondeados al viento, aroma a licor tradicional viche y estofados de piangua, el Pacífico demuestra a la nación entera que su mayor tesoro no reside en la madera ni en los minerales de sus entrañas, sino en la inquebrantable vitalidad de su pueblo, capaz de convertir el aguacero eterno en un cántico sagrado de fraternidad y esperanza para el mundo."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singularidad pluviométrica distingue a la región selvática del Chocó biogeográfico?",
                        "options": [
                            "Es una de las zonas más húmedas de la Tierra, con precipitaciones que superan los diez mil milímetros anuales.",
                            "Es un territorio semiárido donde la lluvia aparece una sola vez cada década.",
                            "Es un valle interandino protegido de las nubes marinas por murallas desérticas.",
                            "Es un páramo glaciar donde el agua solo existe en estado de nieve perpetua."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 detalla que municipios como Lloró registran precipitaciones anuales superiores a los diez mil milímetros, situándolo como meca pluvial del planeta."
                    },
                    {
                        "question": "¿De qué material tradicional se construyen las teclas de la marimba del Pacífico?",
                        "options": [
                            "De la madera fibrosa y resistente de la palma de chonta curada al fuego.",
                            "De aleaciones de bronce y cobre fundidas en los astilleros portuarios.",
                            "De piedras volcánicas pulidas procedentes de los nevados andinos.",
                            "De caparazones fosilizados de tortugas marinas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 especifica que las teclas son elaboradas artesanalmente con la madera durísima de la palma de chonta."
                    },
                    {
                        "question": "¿Qué significado cultural tiene el Festival Petronio Álvarez que se celebra anualmente en Cali?",
                        "options": [
                            "Es el mayor encuentro de afirmación y celebración de las músicas y saberes tradicionales afrodescendientes del Pacífico en América Latina.",
                            "Es un congreso empresarial exclusivo para la venta de embarcaciones de carga pesada.",
                            "Es una feria gastronómica internacional dedicada a la comida rápida europea.",
                            "Es un festival ecuestre para premiar caballos de paso fino andino."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 6 describe el Festival Petronio Álvarez como la mayor celebración de cultura afrodescendiente de la región, reuniendo a más de cien mil personas."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r2}.json", story_col2_02)

    write_json(f"lessons/b2/{r2}.json", make_lesson(
        stem=r2,
        unit_num=14,
        title="El Pacífico colombiano: Biodiversidad selvática, marimba y currulao",
        goal="Analyze the biogeographical uniqueness of the Colombian Pacific, the craftsmanship of the chonta marimba, and the communal power of currulao.",
        grammar_desc="discurso ecológico y musical del litoral Pacífico colombiano",
        grammar_ref=f"grammar/b2/{r2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r2}-voc.json",
        ex_ref=f"exercises/b2/{r2}-ex.json",
        ex_ids=[f"{r2}.ex01", f"{r2}.ex02", f"{r2}.ex03", f"{r2}.ex04", f"{r2}.ex05", f"{r2}.ex06"],
        goals=[
            "Describe the pluvial and riverine geography of Chocó Biogeográfico.",
            "Understand the organology and cultural value of the chonta marimba.",
            "Appreciate the oral tradition of Pacific cantadoras and the Petronio Álvarez Festival."
        ],
        story_ref=f"stories/world/b2/{r2}.json"
    ))

    # Lesson 3: b2-colombiaperiferias-03 - Las comunidades afrodescendientes e indígenas: La Ley 70 de 1993
    r3 = "b2-colombiaperiferias-03"
    write_json(f"vocabulary/b2/{r3}-voc.json", {
        "id": "vocab.b2.colombiaperiferias.03",
        "lesson": r3,
        "title": "Derechos étnicos, titulación colectiva y autogobierno",
        "theme": "Ley 70 de 1993, consulta previa, consejos comunitarios y resguardos indígenas",
        "words": [
            {"lemma": "resguardo", "translation": "indigenous collective reserve, resguardo", "pos": "noun"},
            {"lemma": "etnodesarrollo", "translation": "ethno-development, culturally autonomous progress", "pos": "noun"},
            {"lemma": "titulación", "translation": "land titling, conferral of collective deeds", "pos": "noun"},
            {"lemma": "ancestralidad", "translation": "ancestral heritage, ancestral possession", "pos": "noun"},
            {"lemma": "inembargable", "translation": "unattachable, exempt from seizure/foreclosure", "pos": "adjective"},
            {"lemma": "adjudicar", "translation": "to award, to allocate formally", "pos": "verb"},
            {"lemma": "autodeterminación", "translation": "self-determination", "pos": "noun"},
            {"lemma": "inalienable", "translation": "inalienable, non-transferable", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r3}-a-gr.json", {
        "id": "grammar.b2.colombiaperiferias.03.colombia-ley-setenta-derechos-etnicos",
        "title": "La Ley 70 de 1993 y los derechos territoriales étnicos en Colombia",
        "sections": [
            {
                "type": "text",
                "title": "Marco constitucional de la diversidad étnica y la propiedad colectiva",
                "content": "La Constitución de 1991 reconoció el carácter pluriétnico y multicultural de Colombia, y la histórica Ley 70 de 1993 reconoció a las comunidades negras del Pacífico y de todo el país la propiedad colectiva sobre sus territorios ancestrales. Estos títulos colectivos se caracterizan por ser inalienables, imprescriptibles e inembargables. En nivel B2, se estudian estructuras formales que definen la consulta previa libre e informada frente a proyectos extractivos."
            },
            {
                "type": "table",
                "title": "Pilares de la legislación territorial étnica colombiana",
                "rows": [
                    ["Tierras colectivas", "Títulos ancestrales que son inalienables, inembargables e imprescriptibles."],
                    ["Consulta previa", "Derecho fundamental a ser consultados antes de obras extractivas."],
                    ["Consejos comunitarios", "Autoridades tradicionales que administran los territorios afro."],
                    ["Guardia cívica", "Estructuras comunitarias que ejercen control territorial pacífico."]
                ]
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
                    ["el resguardo", "indigenous collective reserve"],
                    ["la titulación", "conferral of land deeds, titling"],
                    ["inembargable", "exempt from seizure, unattachable"],
                    ["la autodeterminación", "self-determination"]
                ],
                "teaches": ["b2-colombiaperiferias-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La Ley 70 de 1993 consagró que las tierras adjudicadas a las comunidades afro son __ y no pueden venderse. (inalienable)",
                "answer": "inalienables",
                "english": "Law 70 of 1993 established that lands awarded to Afro communities are inalienable and cannot be sold.",
                "teaches": ["colombia-ley-setenta-derechos-etnicos"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué garantía jurídica protege a los territorios étnicos frente a embargos o ventas privadas?",
                "options": [
                    "Su carácter legal de bienes colectivos inalienables, inembargables e imprescriptibles.",
                    "La posibilidad de hipotecarlos libremente en bancos comerciales extranjeros.",
                    "Su conversión automática en parques industriales municipales."
                ],
                "correct": 0,
                "teaches": ["colombia-ley-setenta-derechos-etnicos"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "consulta", "previa", "es", "un", "derecho", "fundamental", "de", "los", "pueblos."],
                "solution": ["La", "consulta", "previa", "es", "un", "derecho", "fundamental", "de", "los", "pueblos."],
                "english": "Prior consultation is a fundamental right of the peoples.",
                "teaches": ["colombia-ley-setenta-derechos-etnicos"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Abogada constitucionalista", "text": "¿Por qué es tan trascendental el Convenio 169 de la OIT en Colombia?"},
                    {"speaker": "Líder afrocolombiano", "text": "_____"},
                    {"speaker": "Abogada constitucionalista", "text": "Una garantía esencial para la supervivencia de las culturas ancestrales."}
                ],
                "options": [
                    "Porque fundamenta el deber estatal de realizar consulta previa libre e informada ante cualquier medida legislativa o proyecto que afecte los territorios.",
                    "Los puertos fluviales del río Magdalena requieren dragado continuo durante el verano.",
                    "El café colombiano se exporta en sacos de sesenta kilogramos hacia el extranjero."
                ],
                "correct": 0,
                "teaches": ["colombia-ley-setenta-derechos-etnicos"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los consejos comunitarios ejercen el autogobierno territorial en defensa de la vida y el bosque.",
                "english": "Community councils exercise territorial self-government in defense of life and the forest.",
                "teaches": ["colombia-ley-setenta-derechos-etnicos"]
            }
        ]
    })

    story_col2_03 = {
        "id": "b2-colombiaperiferias-03",
        "title": "Ley 70: La conquista de la tierra ancestral y el autogobierno",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociopolítica y jurídica de nivel B2 sobre el reconocimiento de los derechos colectivos en Colombia: el artículo transitorio 55 de la Constitución de 1991, la promulgación de la histórica Ley 70 de 1993, la titulación de más de cinco millones de hectáreas a los consejos comunitarios del Pacífico y la defensa de la consulta previa.",
        "characters": [
            "Zulia Mena",
            "Don Eustaquio Palacios",
            "Abogado Hurtado"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "La promulgación de la Constitución Política de 1991 representó un giro copernicano en la historia jurídica de Colombia. Al declarar formalmente en su artículo séptimo que 'el Estado reconoce y protege la diversidad étnica y cultural de la Nación colombiana', el país sepultó más de un siglo de doctrina asimilacionista impuesta por la carta conservadora de 1886, la cual concebía a la república como una nación homogénea, hispánica y católica. Por primera vez en la vida republicana, los pueblos originarios y las comunidades negras obtuvieron un asiento protagónico en el pacto constitucional, conquistando el reconocimiento explícito de sus territorios ancestrales y de sus sistemas propios de autogobierno."
            },
            {
                "type": "narration",
                "text": "El instrumento legislativo cumbre de esa transformación histórica fue la Ley 70 de 1993, fruto de una movilización comunitaria sin precedentes encabezada por líderes y lideresas del litoral pacífico. Inspirada en el Artículo Transitorio 55 de la nueva Carta Magna, la ley reconoció a las comunidades negras que venían ocupando tierras baldías en las zonas ribereñas de los ríos de la cuenca del Pacífico la propiedad colectiva sobre sus territorios ancestrales. Este reconocimiento legal no operó como una graciosa concesión gubernamental, sino como un acto de reparación histórica que reconoció que aquellos bosques y manglares habían sido preservados y habitados de forma sostenible durante más de tres siglos de presencia cimarrona."
            },
            {
                "type": "narration",
                "text": "La arquitectura jurídica de la Ley 70 consagró una figura de propiedad comunitaria de una solidez excepcional. Los títulos colectivos adjudicados por el Estado a través de los Consejos Comunitarios fueron revestidos de tres atributos constitucionales determinantes: son inalienables —lo que significa que jamás pueden ser vendidos a particulares ni desmembrados comercialmente—, son inembargables —quedando protegidos frente a quiebras o demandas financieras— y son imprescriptibles —impidiendo que terceros puedan apropiarse de ellos por el mero paso del tiempo—. Gracias a este marco normativo, más de cinco millones de hectáreas de selvas pluviales y ríos fueron tituladas colectivamente a favor de cientos de comunidades afrocolombianas."
            },
            {
                "type": "narration",
                "text": "Zulia Mena, una de las históricas lideresas chocoanas que batalló incansablemente en los debates del Congreso para la aprobación de la ley, recuerda con emoción aquellos días de huelgas pacíficas y tomas pacíficas de oficinas gubernamentales. En la sede del Consejo Comunitario Mayor del Medio Atrato (ACIA), Zulia dialoga con Don Eustaquio Palacios, un anciano sabedor del río Beté. 'La tierra para nosotros no es una mercancía que se pesa en metros cuadrados o se cotiza en la bolsa; es la casa grande donde reposan los ombligos de nuestros hijos y los huesos de nuestros mayores. Sin territorio colectivo no hay cultura, y sin cultura el pueblo negro perece', explica Don Eustaquio mientras desenrolla el mapa satelital del título comunal."
            },
            {
                "type": "narration",
                "text": "El abogado Hurtado, especialista en litigio estratégico ante la Corte Constitucional, subraya cómo la jurisprudencia colombiana convirtió el Convenio 169 de la Organización Internacional del Trabajo en parte integral del bloque de constitucionalidad. A través de emblemáticas sentencias de tutela, el alto tribunal amparó de manera reiterada el derecho fundamental a la consulta previa, libre e informada, exigiendo que cualquier proyecto de megaminería, dragado portuario o construcción vial en territorios étnicos cuente obligatoriamente con el consentimiento previo de los consejos comunitarios y resguardos indígenas afectados."
            },
            {
                "type": "narration",
                "text": "En ese horizonte de autonomía jurídica, los consejos comunitarios no se limitan a la administración pasiva de las tierras, sino que diseñan planes de etnodesarrollo basados en la soberanía alimentaria, la pesca artesanal responsable y la conservación de cuencas hidrográficas. Estas estructuras de autogobierno demuestran en la práctica cotidiana que la gobernanza comunitaria constituye una de las barreras más eficaces frente al avance descontrolado de la deforestación y la especulación territorial, consolidando a las comunidades afrocolombianas como guardianas insustituibles de la biodiversidad global frente a la crisis climática."
            },
            {
                "type": "narration",
                "text": "A pesar de estos avances legislativos de vanguardia, los territorios colectivos enfrentan hoy agresiones brutales provocadas por la minería ilegal de oro que envenena los ríos con mercurio, los cultivos ilícitos y la presencia violenta de grupos armados que desafían a las autoridades tradicionales. Sin embargo, la dignidad de la guardia cimarrona e indígena, que patrulla los ríos armados únicamente con bastones de mando y banderas de paz, demuestra que la conquista de la Ley 70 sigue viva en cada vereda donde el pueblo afrocolombiano custodia el río, la selva y el derecho irrenunciable al porvenir."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué cambio paradigmático introdujo la Constitución de 1991 respecto a la identidad nacional colombiana?",
                        "options": [
                            "Reconoció formalmente el carácter pluriétnico y multicultural de la nación, superando la doctrina de homogeneidad cultural previa.",
                            "Declaró al español como el único idioma permitido para trámites administrativos y educativos.",
                            "Eliminó los resguardos indígenas para convertirlos en propiedades agrícolas privadas.",
                            "Estableció que las leyes mineras tenían supremacía absoluta sobre los derechos de las comunidades."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 expone que la Carta de 1991 reconoció la diversidad étnica y cultural del país, rompiendo con el modelo asimilacionista homogéneo anterior."
                    },
                    {
                        "question": "¿Cuáles son los tres atributos jurídicos protectores de los títulos colectivos de tierras según la Ley 70 de 1993?",
                        "options": [
                            "Son inalienables (no se pueden vender), inembargables (no se pueden embargar) e imprescriptibles (no se pierden con el tiempo).",
                            "Son temporales, sujetos a renovación anual y gravados con impuestos mercantiles.",
                            "Son propiedades transferibles a empresas transnacionales mediante subastas públicas.",
                            "Son concesiones turísticas administradas directamente por el ministerio de comercio."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 especifica que los títulos colectivos son inalienables, inembargables e imprescriptibles para salvaguardar a las comunidades."
                    },
                    {
                        "question": "¿Qué papel cumple el derecho a la consulta previa libre e informada amparado por la Corte Constitucional?",
                        "options": [
                            "Garantizar que ningún proyecto de megaminería o infraestructura se ejecute en territorios étnicos sin el diálogo y consentimiento de las comunidades.",
                            "Autorizar a las empresas a ocupar tierras ancestrales sin necesidad de estudios de impacto ambiental.",
                            "Obligar a las comunidades a vender sus derechos territoriales en un plazo máximo de treinta días.",
                            "Permitir la privatización de las fuentes de agua dulce por parte de consorcios hidroeléctricos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 destaca que la consulta previa es un derecho fundamental obligatorio para evaluar y acordar cualquier proyecto extractivo o vial en territorios étnicos."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r3}.json", story_col2_03)

    write_json(f"lessons/b2/{r3}.json", make_lesson(
        stem=r3,
        unit_num=14,
        title="Las comunidades afrodescendientes e indígenas: La Ley 70 de 1993",
        goal="Understand Colombia's ethnic constitutional framework, collective land titles under Law 70 of 1993, and prior consultation jurisprudence.",
        grammar_desc="discurso de derecho constitucional étnico, propiedad colectiva y consulta previa",
        grammar_ref=f"grammar/b2/{r3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r3}-voc.json",
        ex_ref=f"exercises/b2/{r3}-ex.json",
        ex_ids=[f"{r3}.ex01", f"{r3}.ex02", f"{r3}.ex03", f"{r3}.ex04", f"{r3}.ex05", f"{r3}.ex06"],
        goals=[
            "Trace the transformation from the 1886 monocultural constitution to the 1991 pluricentric model.",
            "Analyze the legal protections of collective titles (inalienables, inembargables, imprescriptibles).",
            "Deploy human rights and territorial autonomy vocabulary."
        ],
        story_ref=f"stories/world/b2/{r3}.json"
    ))

    # Lesson 4: b2-colombiaperiferias-04 - El conflicto armado y el largo camino hacia la paz
    r4 = "b2-colombiaperiferias-04"
    write_json(f"vocabulary/b2/{r4}-voc.json", {
        "id": "vocab.b2.colombiaperiferias.04",
        "lesson": r4,
        "title": "Memoria histórica, justicia transicional y construcción de paz",
        "theme": "Acuerdo de Paz de 2016, JEP, Comisión de la Verdad, no repetición y víctimas",
        "words": [
            {"lemma": "esclarecimiento", "translation": "clarification, shedding light on the truth", "pos": "noun"},
            {"lemma": "transicional", "translation": "transitional (justice framework)", "pos": "adjective"},
            {"lemma": "compareciente", "translation": "appearing party, respondent before a court", "pos": "noun"},
            {"lemma": "desmovilización", "translation": "demobilization, laying down of arms", "pos": "noun"},
            {"lemma": "resarcir", "translation": "to compensate, to make amends to victims", "pos": "verb"},
            {"lemma": "reconciliar", "translation": "to reconcile", "pos": "verb"},
            {"lemma": "imprescriptible", "translation": "imprescriptible", "pos": "adjective"},
            {"lemma": "restaurativo", "translation": "restorative (justice focused on healing)", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r4}-a-gr.json", {
        "id": "grammar.b2.colombiaperiferias.04.colombia-paz-justicia-transicional",
        "title": "El conflicto armado colombiano y la justicia transicional",
        "sections": [
            {
                "type": "text",
                "title": "Discurso de resolución de conflictos, memoria y verdad restaurativa",
                "content": "El análisis del conflicto armado interno de más de medio siglo en Colombia y la firma del histórico Acuerdo de Paz de La Habana en 2016 articula conceptos de justicia transicional restaurativa (la Jurisdicción Especial para la Paz - JEP, la Comisión de la Verdad y la Unidad de Búsqueda de Personas Desaparecidas). En nivel B2, se utilizan oraciones complejas para evaluar las garantías de no repetición, la centralidad de las víctimas y el deber de esclarecimiento de la verdad."
            },
            {
                "type": "table",
                "title": "Componentes del Sistema Integral de Paz en Colombia",
                "rows": [
                    ["JEP (Justicia Especial)", "Tribunal de justicia restaurativa que juzga a comparecientes."],
                    ["Comisión de la Verdad", "Órgano extrajudicial que redactó el informe final sobre el conflicto."],
                    ["No repetición", "Garantía ética e institucional de que las atrocidades no se repetirán."],
                    ["Centralidad de víctimas", "Principio según el cual las víctimas son el corazón de la paz."]
                ]
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
                    ["el esclarecimiento", "clarification, shedding light on truth"],
                    ["transicional", "transitional (justice framework)"],
                    ["el compareciente", "appearing party before a court"],
                    ["restaurativo", "restorative, focused on healing"]
                ],
                "teaches": ["b2-colombiaperiferias-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La Jurisdicción Especial para la Paz exige que los comparecientes __ la verdad plena para acceder a sanciones restaurativas. (aportar)",
                "answer": "aporten",
                "english": "The Special Jurisdiction for Peace requires appearing parties to provide full truth to access restorative sanctions.",
                "teaches": ["colombia-paz-justicia-transicional"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es el objetivo primordial de la justicia restaurativa aplicada en el proceso de paz colombiano?",
                "options": [
                    "Sanar el daño colectivo, dignificar a las víctimas y esclarecer la verdad por encima del castigo carcelario retributivo.",
                    "Otorgar amnistías generales incondicionales sin investigar ningún delito.",
                    "Disolver los tribunales ordinarios para reemplazarlos por cortes marciales."
                ],
                "correct": 0,
                "teaches": ["colombia-paz-justicia-transicional"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "verdad", "histórica", "es", "el", "fundamento", "ético", "de", "la", "no", "repetición."],
                "solution": ["La", "verdad", "histórica", "es", "el", "fundamento", "ético", "de", "la", "no", "repetición."],
                "english": "Historical truth is the ethical foundation of non-repetition.",
                "teaches": ["colombia-paz-justicia-transicional"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Corresponsal de la ONU", "text": "¿Por qué el informe final de la Comisión de la Verdad es considerado un hito continental?"},
                    {"speaker": "Comisionada de paz", "text": "_____"},
                    {"speaker": "Corresponsal de la ONU", "text": "Un legado indispensable para transformar la cultura ciudadana."}
                ],
                "options": [
                    "Porque escuchó a más de treinta mil víctimas y analizó las causas estructurales del conflicto para que el país no repita su tragedia.",
                    "Los cuarteles militares fueron remodelados con presupuestos extraordinarios de infraestructura.",
                    "Las importaciones de bienes manufacturados crecieron durante el último trimestre."
                ],
                "correct": 0,
                "teaches": ["colombia-paz-justicia-transicional"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La reconciliación nacional exige escuchar el clamor de las víctimas en los territorios más olvidados.",
                "english": "National reconciliation requires listening to the clamor of victims in the most forgotten territories.",
                "teaches": ["colombia-paz-justicia-transicional"]
            }
        ]
    })

    story_col2_04 = {
        "id": "b2-colombiaperiferias-04",
        "title": "El camino hacia la paz: Verdad, memoria y dignidad restaurada",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociopolítica de nivel B2 sobre la superación del conflicto armado en Colombia: el impacto humanitario de más de cincuenta años de confrontación, la firma del histórico Acuerdo de Paz de 2016, la labor pionera de la Jurisdicción Especial para la Paz (JEP) y el coraje de las víctimas como guardianas de la memoria y la reconciliación.",
        "characters": [
            "Luz Marina Bernal",
            "Magistrado Cifuentes",
            "Danilo"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Durante más de medio siglo de confrontación armada ininterrumpida, Colombia padeció el conflicto bélico interno más prolongado y desgarrador de todo el hemisferio occidental. Un entramado trágico de guerrillas insurgentes de orientación marxista, sanguinarios escuadrones paramilitares de extrema derecha, agentes estatales corruptos y redes transnacionales del narcotráfico dejó un saldo estremecedor de más de nueve millones de víctimas reconocidas en el registro oficial: cientos de miles de muertos, más de cien mil personas desaparecidas forzadamente en fosas clandestinas y el éxodo forzado de más de siete millones de campesinos, indígenas y afrodescendientes despojados de sus parcelas ancestrales."
            },
            {
                "type": "narration",
                "text": "Aquella pesadilla que parecía condenar a la nación a una espiral perpetua de violencia dio un paso trascendental hacia la esperanza en noviembre de 2016 con la firma en el Teatro Colón de Bogotá del Acuerdo Final de Paz entre el Estado colombiano y la guerrilla de las FARC-EP, tras cuatro intensos años de negociaciones diplomáticas en La Habana con el acompañamiento de garantes internacionales como Noruega y Cuba. El acuerdo no solo contempló la entrega y fundición de más de nueve mil armas bajo la estricta verificación de la ONU, sino que articuló una ambiciosa reforma rural integral y colocó por primera vez en la historia de los pactos de paz a las víctimas en el centro absoluto de las soluciones."
            },
            {
                "type": "narration",
                "text": "La columna vertebral ética de este proceso fue la creación del Sistema Integral de Verdad, Justicia, Reparación y No Repetición, destacándose como tribunal inédito la Jurisdicción Especial para la Paz (JEP). A diferencia de los modelos judiciales punitivos tradicionales orientados exclusivamente al encierro penitenciario en celdas cerradas, la JEP implementó un paradigma vanguardista de 'justicia transicional restaurativa'. Bajo este modelo, los antiguos comandantes guerrilleros y los altos oficiales militares comparecientes están obligados a aportar verdad exhaustiva y detallada sobre sus crímenes, reconocer públicamente su responsabilidad frente a los deudos y ejecutar obras tangibles de desminado humanitario o construcción de escuelas para resarcir el daño causado."
            },
            {
                "type": "narration",
                "text": "En las salas de audiencias solemnes de la JEP, el dolor histórico se transforma en verdad liberadora. Luz Marina Bernal, una de las admiradas 'Madres de Soacha' cuyo hijo con discapacidad fue secuestrado por soldados y asesinado para presentarlo falsamente como un guerrillero abatido en combate —en el marco del siniestro escándalo de los 'falsos positivos'—, mira a los ojos a los militares retirados. Con una dignidad que conmueve al país entero, Luz Marina sostiene la fotografía de su hijo mientras los oficiales confiesan la verdad y piden perdón de rodillas: 'No buscamos venganza ni deseamos que sus madres lloren lo que nosotras lloramos; exigimos la verdad plena para que ninguna otra madre colombiana tenga que buscar a su hijo en un cementerio anónimo'."
            },
            {
                "type": "narration",
                "text": "Simultáneamente, la Comisión para el Esclarecimiento de la Verdad, liderada por el jesuita Francisco de Roux, recorrió los confines más remotos de la patria escuchando más de treinta mil testimonios de víctimas, soldados, campesinos y expresidentes para alumbrar un monumental Informe Final titulado 'Hay futuro si hay verdad'. El documento reveló que el conflicto no fue una fatalidad inevitable ni una locura abstracta, sino el desenlace de profundas desigualdades territoriales, la exclusión política y la incapacidad de una sociedad para tramitar sus diferencias sin recurrir al exterminio del adversario."
            },
            {
                "type": "narration",
                "text": "Paralelamente, la Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD) despliega una labor humanitaria y extrajudicial incansable a lo largo y ancho de la geografía nacional, exhumando cuerpos en cementerios clandestinos y riberas fluviales para devolver la paz espiritual a familias que buscaron a sus seres queridos durante décadas enteras. Cada entrega digna de restos óseos representa el cierre de un duelo postergado y un triunfo de la compasión humana sobre el olvido burocrático, recordando que no habrá reconciliación auténtica mientras una sola familia permanezca en la incertidumbre sobre el destino de sus desaparecidos."
            },
            {
                "type": "narration",
                "text": "El camino hacia la reconciliación plena sigue estando sembrado de formidables escollos: disidencias armadas, el asesinato sistemático de firmantes de paz y líderes comunitarios en zonas de periferia y la polarización retórica de sectores recalcitrantes. Sin embargo, en cada rincón donde una víctima perdona sin olvidar, donde excombatientes siembran café y tejen prendas de vestir junto a sus antiguos adversarios y donde la juventud abraza la memoria histórica en las escuelas, Colombia demuestra al planeta que la paz no es un decreto gubernamental, sino un pacto sagrado y colectivo por la preservación de la vida digna."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál es la cifra aproximada de víctimas registradas oficialmente a lo largo del conflicto armado colombiano?",
                        "options": [
                            "Más de nueve millones de víctimas reconocidas en el registro estatal oficial.",
                            "Menos de diez mil personas en algunas provincias aisladas.",
                            "Cincuenta mil personas exclusivamente pertenecientes a las fuerzas militares.",
                            "No se cuenta con ningún registro oficial sobre las víctimas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 detalla que el conflicto dejó un saldo estremecedor de más de nueve millones de víctimas registradas oficialmente."
                    },
                    {
                        "question": "¿En qué consiste el modelo de 'justicia transicional restaurativa' aplicado por la JEP?",
                        "options": [
                            "En exigir a los comparecientes que aporten verdad plena y reparen a las víctimas mediante obras sociales de desminado o reconstrucción, priorizando sanar el daño sobre el castigo carcelario retributivo.",
                            "En aplicar la pena de muerte automática a todos los guerrilleros y militares desmovilizados.",
                            "En archivar todos los expedientes sin realizar juicios ni audiencias testimoniales.",
                            "En trasladar a todos los acusados a prisiones de máxima seguridad en el extranjero sin derecho a defensa."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 define la justicia restaurativa de la JEP: verdad plena y obras tangibles de reparación a las víctimas para resarcir el daño."
                    },
                    {
                        "question": "¿Cuál fue la conclusión central del Informe Final de la Comisión de la Verdad liderada por Francisco de Roux?",
                        "options": [
                            "Que el conflicto armado fue producto de profundas desigualdades, despojos territoriales y exclusión política, y que la paz exige asumir la verdad colectiva para garantizar la no repetición.",
                            "Que la violencia armada se debió exclusivamente a invasiones militares extranjeras no deseadas.",
                            "Que las víctimas debían renunciar a conocer el paradero de sus familiares desaparecidos.",
                            "Que la sociedad colombiana no tiene posibilidad alguna de reconciliación pacífica."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 analiza las conclusiones del Informe Final: el conflicto no fue una fatalidad abstracta sino el resultado de exclusiones estructurales que deben ser subsanadas con verdad."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r4}.json", story_col2_04)

    write_json(f"lessons/b2/{r4}.json", make_lesson(
        stem=r4,
        unit_num=14,
        title="El conflicto armado y el largo camino hacia la paz",
        goal="Examine Colombia's 2016 Peace Accords, transitional restorative justice (JEP), the Truth Commission, and victims' leadership in historical memory.",
        grammar_desc="discurso de justicia transicional, resolución de conflictos y memoria histórica",
        grammar_ref=f"grammar/b2/{r4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r4}-voc.json",
        ex_ref=f"exercises/b2/{r4}-ex.json",
        ex_ids=[f"{r4}.ex01", f"{r4}.ex02", f"{r4}.ex03", f"{r4}.ex04", f"{r4}.ex05", f"{r4}.ex06"],
        goals=[
            "Understand the historical dimensions and human toll of Colombia's armed conflict.",
            "Analyze the innovative restorative justice mechanisms of the JEP.",
            "Synthesize reconciliation and historical memory discourse at an advanced B2 level."
        ],
        story_ref=f"stories/world/b2/{r4}.json"
    ))

    # Lesson 5: b2-colombiaperiferias-05 - Transición ecológica, Amazonia colombiana y nuevo liderazgo
    r5 = "b2-colombiaperiferias-05"
    write_json(f"vocabulary/b2/{r5}-voc.json", {
        "id": "vocab.b2.colombiaperiferias.05",
        "lesson": r5,
        "title": "Amazonia, Chiribiquete y diplomacia climática",
        "theme": "Parque Chiribiquete, biodiversidad amazónica, deforestación y transición verde",
        "words": [
            {"lemma": "tepuy", "translation": "tepui, flat-topped table mountain", "pos": "noun"},
            {"lemma": "pictograma", "translation": "pictogram, rock art painting", "pos": "noun"},
            {"lemma": "deforestación", "translation": "deforestation", "pos": "noun"},
            {"lemma": "descarbonización", "translation": "decarbonization", "pos": "noun"},
            {"lemma": "mitigar", "translation": "to mitigate, to reduce impact", "pos": "verb"},
            {"lemma": "salvaguardar", "translation": "to safeguard, to protect", "pos": "verb"},
            {"lemma": "inmemorial", "translation": "immemorial, ancient beyond memory", "pos": "adjective"},
            {"lemma": "bioclimático", "translation": "bioclimatic", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r5}-a-gr.json", {
        "id": "grammar.b2.colombiaperiferias.05.colombia-amazonia-chiribiquete-clima",
        "title": "La Amazonia colombiana: Chiribiquete, biodiversidad y transición ecológica",
        "sections": [
            {
                "type": "text",
                "title": "Discurso de diplomacia climática, arte rupestre y preservación amazónica",
                "content": "La cuenca amazónica colombiana (que cubre más del cuarenta por ciento del territorio continental nacional) alberga joyas biológicas y culturales como el Parque Nacional Natural Serranía de Chiribiquete —el mayor parque de selva tropical protegida del mundo y patrimonio mixto de la UNESCO—. En nivel B2, se estudian estructuras argumentativas y concesivas que articulan la diplomacia de descarbonización, la lucha contra la deforestación y la protección de pueblos originarios en aislamiento voluntario."
            },
            {
                "type": "table",
                "title": "Patrimonio biocultural amazónico y diplomacia verde",
                "rows": [
                    ["Serranía de Chiribiquete", "Parque natural con tepuyes y miles de pinturas rupestres milenarias."],
                    ["Pictogramas de jaguar", "Arte rupestre sagrado que data de más de doce mil años de antigüedad."],
                    ["Transición ecológica", "Propuesta de sustituir economías extractivas por bioeconomía."],
                    ["Pueblos en aislamiento", "Comunidades amazónicas que eligen vivir sin contacto foráneo."]
                ]
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
                    ["el tepuy", "table mountain, flat plateau"],
                    ["el pictograma", "rock art painting, pictogram"],
                    ["salvaguardar", "to safeguard, to protect"],
                    ["la descarbonización", "decarbonization"]
                ],
                "teaches": ["b2-colombiaperiferias-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Chiribiquete es un santuario mixto de la UNESCO que __ la mayor colección de arte rupestre del planeta. (albergar)",
                "answer": "alberga",
                "english": "Chiribiquete is a UNESCO mixed heritage site that houses the largest collection of rock art on the planet.",
                "teaches": ["colombia-amazonia-chiribiquete-clima"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué singularidad histórica y arqueológica distingue a la Serranía de Chiribiquete?",
                "options": [
                    "Alberga más de setenta mil pinturas rupestres sobre paredes de tepuyes sagrados que datan de hace más de doce mil años.",
                    "Fue una base militar construida por ingenieros durante la Guerra Fría.",
                    "Es un complejo de minas de sal marina explotadas desde la época colonial."
                ],
                "correct": 0,
                "teaches": ["colombia-amazonia-chiribiquete-clima"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "protección", "de", "la", "Amazonia", "es", "vital", "para", "el", "equilibrio", "climático."],
                "solution": ["La", "protección", "de", "la", "Amazonia", "es", "vital", "para", "el", "equilibrio", "climático."],
                "english": "The protection of the Amazon is vital for climate balance.",
                "teaches": ["colombia-amazonia-chiribiquete-clima"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministra de Ambiente", "text": "¿Cuál es la postura de Colombia en las cumbres climáticas globales?"},
                    {"speaker": "Delegado internacional", "text": "_____"},
                    {"speaker": "Ministra de Ambiente", "text": "Una diplomacia ambiental de vanguardia para salvar la selva amazónica."}
                ],
                "options": [
                    "Promover un canje global de deuda externa por acción climática y blindar la Amazonia contra la deforestación extractivista.",
                    "Los muelles del puerto de Barranquilla reciben buques portacontenedores de gran calado.",
                    "La red de telecomunicaciones satelitales cubre las capitales de los departamentos andinos."
                ],
                "correct": 0,
                "teaches": ["colombia-amazonia-chiribiquete-clima"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los pueblos amazónicos en aislamiento voluntario son los verdaderos guardianes de la selva virgen.",
                "english": "Amazonian peoples in voluntary isolation are the true guardians of the virgin forest.",
                "teaches": ["colombia-amazonia-chiribiquete-clima"]
            }
        ]
    })

    story_col2_05 = {
        "id": "b2-colombiaperiferias-05",
        "title": "Chiribiquete y la Amazonia: El templo sagrado de los tepuyes",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica ambiental y arqueológica de nivel B2 sobre la Amazonia colombiana: la majestuosidad de la Serranía de Chiribiquete como el mayor parque protegido de selva tropical de la Tierra, los murales rupestres del jaguar de más de doce mil años de antigüedad y el liderazgo de Colombia en la diplomacia climática global.",
        "characters": [
            "Carlos Castaño-Uribe",
            "Diana Trujillo",
            "Don Benjamín"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Ocupando más del cuarenta por ciento de la superficie continental de Colombia, la inmensa cuenca amazónica se despliega como un océano verde de prodigiosa complejidad biológica y cultural. En medio de esta llanura selvática impenetrable, donde los ríos Caquetá, Putumayo, Guaviare y Apaporis serpentean como venas colosales que nutren el sistema hidrológico del planeta, se yergue una de las formaciones geológicas más antiguas y enigmáticas del continente: la Serranía de Chiribiquete. Con más de cuatro millones trescientas mil hectáreas de extensión, este enclave fue declarado en 2018 por la UNESCO como Patrimonio Mixto de la Humanidad (Cultural y Natural), consolidándose formalmente como el parque nacional de selva pluvial tropical protegida más grande del mundo."
            },
            {
                "type": "narration",
                "text": "Emergiendo de la densa canopia vegetal como fortalezas gigantescas esculpidas por el viento a lo largo de mil setecientos millones de años de historia geológica, los tepuyes de Chiribiquete desafían el cielo con paredes verticales que superan los ochocientos metros de altitud. Sobre estos farallones de arenisca de origen precámbrico, exploraciones arqueológicas lideradas por el antropólogo colombiano Carlos Castaño-Uribe sacaron a la luz el más asombroso monumento de arte rupestre del planeta: más de setenta y cinco mil pictogramas trazados con ocre mineral rojo que abarcan más de doce mil años ininterrumpidos de ritualidad chamánica, representando jaguares ceremoniales, figuras humanas danzantes y animales extintos de la megafauna pleistocénica."
            },
            {
                "type": "narration",
                "text": "Para las comunidades indígenas amazónicas de las etnias karijona, uitoto y nukak, Chiribiquete no constituye un parque recreativo ni un museo al aire libre; es la 'Maloca Cósmica del Jaguar', el ombligo sagrado donde reside la fuerza creadora que sostiene el equilibrio energético de la selva entera. En sus valles ocultos y cañones selváticos habitan todavía comunidades de pueblos indígenas en aislamiento voluntario, hombres y mujeres que optaron conscientemente por no establecer contacto con la civilización occidental, preservando un modo de existencia armónico e inmemorial que la legislación colombiana protege de manera taxativa prohibiendo cualquier turismo convencional en el área protegida."
            },
            {
                "type": "narration",
                "text": "Carlos Castaño-Uribe, contemplando los farallones desde un sobrevuelo científico de monitoreo bioclimático junto a la bióloga Diana Trujillo, reflexiona con sobrecogimiento sobre este santuario: 'Chiribiquete es la Capilla Sixtina de la Amazonia prehistórica; nos revela que hace doce milenios los pobladores de este continente ya comprendían que el jaguar y la selva no eran recursos que se explotan, sino divinidades tutelares con las que el ser humano debe convivir en reverente reciprocidad espiritual'. Diana asiente mientras ajusta los sensores de temperatura y cobertura boscosa del satélite de monitoreo forestal."
            },
            {
                "type": "narration",
                "text": "Sin embargo, las fronteras de este paraíso se encuentran asediadas por fuegos provocados, la ganadería extensiva ilegal que devora miles de hectáreas de selva para acaparar tierras y las pistas clandestinas del narcotráfico. Frente a esta tragedia planetaria, Colombia ha enarbolado en los últimos años un audaz liderazgo en la diplomacia climática internacional. Proponiendo en foros multilaterales como las cumbres de la ONU un canje global de deuda externa por acción climática y descarbonización, el país convoca al mundo industrializado a cofinanciar la preservación de la Amazonia entendida como el pulmón bioclimático insustituible que regula las lluvias de todo el continente."
            },
            {
                "type": "narration",
                "text": "La riqueza ecosistémica de Chiribiquete se articula además como un corredor biológico monumental que conecta biomas estratégicos: la Amazonia profunda, los llanos del Orinoco, las estribaciones de la cordillera de los Andes y el Escudo Guayanés. En esta encrucijada geográfica de biodiversidad única conviven jaguares, pumas, delfines rosados de río, nutrias gigantes de agua dulce y miles de especies botánicas endémicas que no habitan en ningún otro punto del globo terráqueo, convirtiendo a cada expedición científica autorizada en el descubrimiento de nuevos prodigios para la ciencia natural contemporánea."
            },
            {
                "type": "narration",
                "text": "La defensa de Chiribiquete y de la selva amazónica trasciende por tanto las fronteras geopolíticas colombianas para erigirse en un imperativo ético de la especie humana. En los trazos rojos de los jaguares que miran desde la piedra precámbrica hacia el dosel verde de la selva virgen, late la advertencia milenaria de que el destino del ser humano es inseparable del destino de los bosques: salvar a la Amazonia es, en última instancia, salvaguardar la posibilidad misma de un futuro habitable sobre la Tierra."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué distinción internacional otorgó la UNESCO a la Serranía de Chiribiquete en 2018?",
                        "options": [
                            "La declaró Patrimonio Mixto de la Humanidad (Cultural y Natural), reconociéndolo como el parque de selva tropical protegida más extenso de la Tierra.",
                            "Lo catalogó como el principal centro de minería a cielo abierto de América del Sur.",
                            "Lo declaró zona franca comercial exenta de regulaciones ambientales nacionales.",
                            "Lo reconoció exclusivamente como observatorio astronómico moderno."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 precisa que en 2018 la UNESCO declaró a Chiribiquete como Patrimonio Mixto de la Humanidad, abarcando más de 4,3 millones de hectáreas."
                    },
                    {
                        "question": "¿Qué singularidad artística y ritual encierran los farallones de los tepuyes de Chiribiquete?",
                        "options": [
                            "Albergan más de setenta y cinco mil pictogramas rupestres en ocre rojo que registran más de doce mil años continuos de culto sagrado al jaguar.",
                            "Contienen esculturas de mármol talladas por artistas del Renacimiento italiano.",
                            "Tienen inscripciones jeroglíficas egipcias traídas en barcos transatlánticos.",
                            "Muestran carteles comerciales de empresas extractivas del caucho."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 describe la existencia de más de setenta y cinco mil pinturas rupestres ceremoniales que datan de doce milenios atrás."
                    },
                    {
                        "question": "¿Qué propuesta de diplomacia climática global ha impulsado Colombia para proteger la Amazonia?",
                        "options": [
                            "Promover un canje de deuda externa por acción ambiental y descarbonización para que el mundo financie la protección de la selva.",
                            "Subastar los derechos de tala de madera amazónica en los mercados financieros internacionales.",
                            "Construir una red de autopistas de ocho carriles para conectar los ríos amazónicos con el Pacífico.",
                            "Prohibir que los científicos nacionales monitoreen la cobertura forestal."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 destaca la propuesta de canjear deuda externa por acción climática en foros internacionales para cofinanciar la preservación de la Amazonia."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r5}.json", story_col2_05)

    write_json(f"lessons/b2/{r5}.json", make_lesson(
        stem=r5,
        unit_num=14,
        title="Transición ecológica, Amazonia colombiana y nuevo liderazgo",
        goal="Explore the Serranía de Chiribiquete, pre-Columbian rock art, Amazonian conservation, and Colombia's global climate diplomacy.",
        grammar_desc="discurso ecológico, diplomacia climática y patrimonio arqueológico amazónico",
        grammar_ref=f"grammar/b2/{r5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r5}-voc.json",
        ex_ref=f"exercises/b2/{r5}-ex.json",
        ex_ids=[f"{r5}.ex01", f"{r5}.ex02", f"{r5}.ex03", f"{r5}.ex04", f"{r5}.ex05", f"{r5}.ex06"],
        goals=[
            "Describe the ancient tepui geology and 12,000-year-old rock art of Chiribiquete.",
            "Understand the legal rights of indigenous peoples living in voluntary isolation.",
            "Analyze international climate diplomacy (debt-for-climate swaps, anti-deforestation)."
        ],
        story_ref=f"stories/world/b2/{r5}.json"
    ))

    # Regional Consolidation: b2-colombiaperiferias-consolidation
    rc_con = "b2-colombiaperiferias-consolidation"
    write_json(f"exercises/b2/{rc_con}-ex.json", {
        "lesson": rc_con,
        "exercises": [
            {
                "id": f"{rc_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el cimarronaje", "flight from slavery, marronage"],
                    ["el resguardo", "indigenous collective reserve"],
                    ["el compareciente", "appearing party before a court"],
                    ["el tepuy", "flat-topped table mountain"]
                ],
                "teaches": ["b2-colombiaperiferias-vocab"]
            },
            {
                "id": f"{rc_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué une cultural y políticamente a las regiones del Caribe, el Pacífico y la Amazonia colombianas?",
                "options": [
                    "Su condición de territorios pluriétnicos que forjaron la autonomía colectiva, la biodiversidad extrema y la paz desde las periferias.",
                    "La adopción uniforme de un modelo industrial idéntico al de las capitales europeas.",
                    "La renuncia voluntaria a sus tradiciones musicales y lenguas ancestrales."
                ],
                "correct": 0,
                "teaches": ["colombia-ley-setenta-derechos-etnicos"]
            },
            {
                "id": f"{rc_con}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Cualquiera que __ los ecosistemas de manglar y selva atenta contra la supervivencia de los pueblos ancestrales. (destruir)",
                "answer": "destruya",
                "english": "Anyone who destroys mangrove and jungle ecosystems threatens the survival of ancestral peoples.",
                "teaches": ["colombia-pacifico-marimba-currulao"]
            },
            {
                "id": f"{rc_con}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "paz", "duradera", "se", "edifica", "reconociendo", "la", "dignidad", "de", "las", "víctimas."],
                "solution": ["La", "paz", "duradera", "se", "edifica", "reconociendo", "la", "dignidad", "de", "las", "víctimas."],
                "english": "Enduring peace is built by recognizing the dignity of the victims.",
                "teaches": ["colombia-paz-justicia-transicional"]
            },
            {
                "id": f"{rc_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué significado tiene la consulta previa en el marco del bloque de constitucionalidad?",
                "options": [
                    "Es un derecho fundamental inalienable de las comunidades étnicas antes de emprender obras extractivas en sus territorios.",
                    "Es una encuesta de opinión informal sin ningún carácter legal vinculante.",
                    "Es un trámite arancelario para la exportación de madera amazónica."
                ],
                "correct": 0,
                "teaches": ["colombia-ley-setenta-derechos-etnicos"]
            },
            {
                "id": f"{rc_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Cómo se define la identidad de la Colombia periférica en este siglo XXI?"},
                    {"speaker": "Investigadora", "text": "_____"},
                    {"speaker": "Sociólogo", "text": "Una lección sublime de dignidad y diversidad para el mundo entero."}
                ],
                "options": [
                    "Como una polifonía indómita de pueblos afro, indígenas y campesinos que defienden el agua, la memoria y la vida.",
                    "Las carreteras de doble calzada comunican los puertos comerciales con los valles andinos.",
                    "El informe anual de finanzas públicas fue presentado ante la comisión legislativa."
                ],
                "correct": 0,
                "teaches": ["colombia-caribe-palenque-cumbia"]
            },
            {
                "id": f"{rc_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "De los manglares del Pacífico a los tepuyes de Chiribiquete, Colombia late como una nación pluriétnica y diversa.",
                "english": "From the mangroves of the Pacific to the tepuis of Chiribiquete, Colombia beats as a multiethnic and diverse nation.",
                "teaches": ["colombia-amazonia-chiribiquete-clima"]
            },
            {
                "id": f"{rc_con}.ex08",
                "type": "sentence-builder",
                "category": "writing",
                "tiles": ["La", "verdad", "plena", "y", "el", "respeto", "mutuo", "son", "las", "claves", "de", "la", "reconciliación."],
                "solution": ["La", "verdad", "plena", "y", "el", "respeto", "mutuo", "son", "las", "claves", "de", "la", "reconciliación."],
                "english": "Full truth and mutual respect are the keys to reconciliation.",
                "teaches": ["colombia-paz-justicia-transicional"]
            }
        ]
    })

    story_col2_capstone = {
        "id": "b2-colombiaperiferias-consolidation",
        "title": "Una nación pluriétnica: Territorios de resistencia y esperanza",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Gran crónica de consolidación de nivel B2 sobre las periferias de Colombia: la epopeya cimarrona de Palenque, el canto de las marimbas en la lluvia del Pacífico, la vigencia de la Ley 70 y los derechos territoriales étnicos, la tenacidad del movimiento de víctimas por la paz y el misterio inmemorial de Chiribiquete en la Amazonia.",
        "characters": [
            "Aminta Carabalí",
            "Darío Cuesta"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Comprender la totalidad de Colombia exige necesariamente descender de las cumbres andinas y adentrarse con respeto y asombro en sus litorales, selvas y llanuras fluviales. Durante más de un siglo, el relato hegemónico del país se escribió desde los altiplanos fríos de la cordillera central y oriental, relegando a las costas del Caribe y del Pacífico y a las inmensidades amazónicas a la condición de 'periferias' exóticas o marginales. Sin embargo, cuando se recorre la geografía viva de estos territorios, se descubre que es precisamente en estas márgenes donde se forjaron los mayores actos de libertad, la mayor riqueza biológica del planeta y las lecciones éticas más conmovedoras de convivencia comunitaria y resistencia cívica."
            },
            {
                "type": "narration",
                "text": "En las costas cálidas del Caribe, la memoria de San Basilio de Palenque nos recuerda que antes de que los próceres criollos soñaran con repúblicas independientes, los cimarrones guiados por Benkos Biohó ya habían conquistado su libertad con la fuerza indomable de sus tambores y la solidez de sus empalizadas. Aquel primer pueblo libre de América salvaguardó en su lengua criolla y en los compases del bullerengue la certeza innegociable de que la dignidad humana no se somete a coronas ni a cadenas mercantiles. Ese legado afrocaribeño impregnó para siempre la cadencia vital de la nación, enseñándole que la alegría festiva no es un descuido frívolo, sino una formidable armadura contra el dolor."
            },
            {
                "type": "narration",
                "text": "Al otro lado de la geografía patria, cruzando las cumbres hacia el océano Pacífico, la selva pluvial del Chocó biogeográfico despliega su manto de lluvias infinitas y manglares laberínticos. En ríos rumorosos donde las cantadoras entonan alabaos y la marimba de chonta vibra como el piano de la selva, los pueblos afrodescendientes e indígenas demostraron al mundo que es posible habitar la floresta tropical más húmeda de la Tierra sin talar sus árboles sagrados ni arrasar sus fuentes de agua. La conquista histórica de la Ley 70 de 1993, que convirtió cinco millones de hectáreas en propiedad colectiva inalienable e inembargable, selló el matrimonio indestructible entre la cultura ancestral y la soberanía del bosque."
            },
            {
                "type": "narration",
                "text": "Esa misma entereza moral iluminó los años más oscuros del conflicto armado interno. En las cuencas más golpeadas por la violencia partidista, guerrillera y paramilitar, fueron las mujeres afrocolombianas, indígenas y campesinas —las eternas guardianas de la vida— quienes levantaron la bandera blanca del perdón y la no repetición. Al exigir verdad plena en las audiencias de la Justicia Especial para la Paz y dignificar a los miles de desaparecidos forzados, las víctimas demostraron al país que la justicia transicional no busca saciar venganzas estériles, sino reconstruir el tejido humano desgarrado para que ninguna otra generación vuelva a padecer el horror de la guerra."
            },
            {
                "type": "narration",
                "text": "Y en el confín suroriental, donde los tepuyes milenarios de la Serranía de Chiribiquete emergen de la densa canopia amazónica como la Maloca Cósmica del Jaguar, los pictogramas rojos de hace doce milenios siguen interpelando nuestra conciencia contemporánea. Como mayor parque de selva tropical protegida del planeta, Chiribiquete custodia a pueblos en aislamiento voluntario y recuerda a la humanidad que la Amazonia no admite dilaciones: descarbonizar las economías, frenar la deforestación y canjear deuda por acción climática son los únicos caminos para asegurar el aire y el agua de las generaciones venideras."
            },
            {
                "type": "narration",
                "text": "Al mismo tiempo, la inmensidad de los llanos orientales de la Orinoquía y el vasto océano verde amazónico complementan este tapiz nacional con lecciones de equilibrio ecológico y arraigo identitario. Desde las faenas ganaderas y los 'cantos de vaquería' que resuenan en los hatos sabaneros hasta los saberes botánicos de los chamanes selváticos que descifran los misterios medicinales del bosque primario, las regiones periféricas enseñan que la soberanía de una patria no se mide por la acumulación de capital en sus capitales financieras, sino por la vitalidad con que sus pueblos custodian la biodiversidad y honran sus orígenes compartidos."
            },
            {
                "type": "narration",
                "text": "De los baluartes de Cartagena al repique de la marimba en Guapi, de las asambleas comunitarias del Atrato a los murales sagrados de Chiribiquete, Colombia late como una nación pluriétnica, diversa e indivisible. En la voz polifónica de sus pueblos periféricos que defienden la vida frente a todas las adversidades resplandece la mayor verdad de esta tierra: que el verdadero corazón de Colombia no reside en un solo centro urbano, sino en la maravillosa pluralidad de sus territorios que tejen a diario la paz, la memoria y la esperanza continental."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué manera el texto sintetiza la importancia de las 'periferias' frente al centro andino de Colombia?",
                        "options": [
                            "Muestra que en los litorales, selvas y llanuras se forjaron los mayores hitos de libertad, diversidad biológica y resistencia comunitaria de la nación.",
                            "Afirma que las regiones litorales no tuvieron ninguna relevancia en la formación cultural de Colombia.",
                            "Sostiene que el país debe centralizar todos sus recursos exclusivamente en las tres cordilleras andinas.",
                            "Propone abandonar las selvas tropicales para concentrar a toda la población en megaciudades."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 destaca que en las regiones litorales y amazónicas reside la mayor riqueza biológica, las lecciones de dignidad y la verdadera libertad histórica del país."
                    },
                    {
                        "question": "¿Qué logro ético fundamental se atribuye al movimiento de víctimas en la superación del conflicto armado?",
                        "options": [
                            "Haber impulsado la verdad plena y la justicia restaurativa sin buscar venganzas estériles, defendiendo la vida y la no repetición.",
                            "Haber exigido la disolución de los acuerdos de paz firmados con la comunidad internacional.",
                            "Haber rechazado participar en las audiencias de esclarecimiento histórico.",
                            "Haber renunciado a la búsqueda de sus familiares desaparecidos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 remarca que las víctimas demostraron que la justicia restaurativa busca sanar el tejido humano con verdad y dignidad para evitar la repetición de la guerra."
                    },
                    {
                        "question": "¿Cuál es el mensaje de cierre sobre la identidad pluriétnica de Colombia?",
                        "options": [
                            "Que el corazón y el futuro de la nación radican en la fecunda pluralidad de sus territorios y culturas que construyen a diario la paz y la memoria.",
                            "Que el país debe imponer una sola cultura homogénea para eliminar las diferencias regionales.",
                            "Que la Amazonia debe ser explotada comercialmente por consorcios extranjeros.",
                            "Que la música de marimba y el arte rupestre deben sustituirse por modelos estéticos europeos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El último párrafo concluye que la mayor verdad de Colombia resplandece en la pluralidad indivisible de sus pueblos periféricos que defienden la vida, la memoria y la paz."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{rc_con}.json", story_col2_capstone)
    write_json("stories/world/b2/b2-colombiaperiferias.json", story_col2_capstone)

    write_json(f"lessons/b2/{rc_con}.json", make_consolidation_lesson(
        stem=rc_con,
        unit_num=14,
        title="Consolidación: Una nación pluriétnica: Territorios de resistencia y esperanza",
        goal="Consolidate communicative and cultural mastery of Colombia's peripheral regions, integrating Caribbean maroon heritage, Pacific marimba traditions, Law 70 collective rights, peacebuilding, and Amazonian ecology.",
        grammar_desc="repaso integral de la diversidad pluriétnica, derechos colectivos y memoria histórica de Colombia",
        ex_ref=f"exercises/b2/{rc_con}-ex.json",
        ex_ids=[f"{rc_con}.ex01", f"{rc_con}.ex02", f"{rc_con}.ex03", f"{rc_con}.ex04", f"{rc_con}.ex05", f"{rc_con}.ex06", f"{rc_con}.ex07", f"{rc_con}.ex08"],
        goals=[
            "Synthesize Caribbean, Pacific, and Amazonian cultural dynamics at an advanced B2 level.",
            "Demonstrate fluency in complex universal relative clauses and legal-ethnic registers.",
            "Articulate nuanced perspectives on transitional justice, collective land rights, and climate diplomacy."
        ],
        checklist_items=[
            "Comprendo la trascendencia de San Basilio de Palenque como primer pueblo libre de América.",
            "Valoro la riqueza etnomusical del Pacífico y el valor de la marimba de chonta.",
            "Domino los principios de la Ley 70 de 1993 y la consulta previa libre e informada.",
            "Analizo el sistema de justicia transicional restaurativa (JEP) y el valor de Chiribiquete."
        ],
        story_ref=f"stories/world/b2/{rc_con}.json"
    ))
    print("Completed LatAm Unit 14 (Colombia Periferias) generation!")

    # -------------------------------------------------------------------------
    # UPDATE CURRICULUM UNITS B2
    # -------------------------------------------------------------------------
    b2_units_path = BASE / "curriculum" / "units" / "b2.json"
    with open(b2_units_path, "r", encoding="utf-8") as f:
        b2_units = json.load(f)

    has_u14_core = any(u.get("title") == "Universal & Indefinite Relatives" for u in b2_units)
    has_u14_reg = any(u.get("title") == "Colombia II: The Caribbean, Pacific, Afro-Colombian Heritage & Peace" for u in b2_units)

    if not has_u14_core:
        b2_units.append({
            "title": "Universal & Indefinite Relatives",
            "stems": [
                "b2-14-01",
                "b2-14-02",
                "b2-14-03",
                "b2-14-04",
                "b2-14-05",
                "b2-14-consolidation"
            ],
            "track": "core"
        })

    if not has_u14_reg:
        b2_units.append({
            "title": "Colombia II: The Caribbean, Pacific, Afro-Colombian Heritage & Peace",
            "stems": [
                "b2-colombiaperiferias-01",
                "b2-colombiaperiferias-02",
                "b2-colombiaperiferias-03",
                "b2-colombiaperiferias-04",
                "b2-colombiaperiferias-05",
                "b2-colombiaperiferias-consolidation"
            ],
            "track": "latam"
        })

    with open(b2_units_path, "w", encoding="utf-8") as f:
        json.dump(b2_units, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated curriculum/units/b2.json with Unit 14!")

    # -------------------------------------------------------------------------
    # WORD COUNT AUDIT
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_14", story_core_14),
        ("story_col2_01", story_col2_01),
        ("story_col2_02", story_col2_02),
        ("story_col2_03", story_col2_03),
        ("story_col2_04", story_col2_04),
        ("story_col2_05", story_col2_05),
        ("story_col2_capstone", story_col2_capstone)
    ]
    print("\n--- Story Word Count Audit ---")
    all_ok = True
    for name, s in stories_to_audit:
        wc = count_words(s)
        status = "OK (650-825)" if 650 <= wc <= 825 else "OUT OF RANGE"
        if "OUT" in status:
            all_ok = False
        print(f"{name:20}: {wc:4} words -> {status}")
    if not all_ok:
        raise ValueError("Some stories failed the word count requirement (650-825 words)!")

if __name__ == "__main__":
    run()
