#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 First Dual Unit:
  - Track 1 (Core): Unit 1 — "Nuance, Precision & Emphasis" (b2-01)
  - Track 2 (LatAm): Unit 1 — "Mexico I: Central Mexico & the Valley of Anáhuac" (b2-mexicocentro)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "content" / "es-latam"


def write_json(rel_path: str, data: dict):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


# ==============================================================================
# 1. CORE B2 UNIT 1: Nuance, Precision & Emphasis
# ==============================================================================

def generate_core_unit_1():
    # Vocab skill: b2-unit01-vocab
    # Grammar skills:
    #   - oraciones-hendidas-enfasis
    #   - adverbios-intensificadores
    #   - inversion-enfasis-fronting
    #   - enfasis-contrastivo-sino

    # Lesson 1: Cleft sentences with "Lo que... es / fue"
    l1_stem = "b2-01-01"
    write_json(f"vocabulary/b2/{l1_stem}-voc.json", {
        "id": "vocab.b2.01.01",
        "lesson": l1_stem,
        "title": "Estructuras de énfasis y foco",
        "theme": "Matices y precisión argumentativa",
        "words": [
            {"lemma": "el matiz", "translation": "nuance", "pos": "noun"},
            {"lemma": "el hincapié", "translation": "emphasis", "pos": "noun"},
            {"lemma": "destacar", "translation": "to highlight", "pos": "verb"},
            {"lemma": "precisamente", "translation": "precisely", "pos": "adverb"},
            {"lemma": "enfatizar", "translation": "to emphasize", "pos": "verb"},
            {"lemma": "el trasfondo", "translation": "background, subtext", "pos": "noun"},
            {"lemma": "radicar", "translation": "to lie in, to reside in", "pos": "verb"},
            {"lemma": "crucial", "translation": "crucial", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{l1_stem}-a-gr.json", {
        "id": "grammar.b2.01.01.oraciones-hendidas",
        "title": "Las oraciones hendidas: lo que... es",
        "sections": [
            {
                "type": "text",
                "title": "¿Qué son las oraciones hendidas?",
                "content": "Las oraciones hendidas (cleft sentences) dividen una proposición en dos partes mediante una perífrasis de relativo y el verbo 'ser' para destacar un elemento específico: 'Lo que realmente importa es su actitud'."
            },
            {
                "type": "text",
                "title": "Mecanismo y concordancia",
                "content": "En el español culto latinoamericano, cuando el elemento focalizado es plural, el verbo 'ser' tiende a concordar con el predicado en registro formal: 'Lo que necesitamos son soluciones concretas'."
            },
            {
                "type": "table",
                "title": "Estructuras hendidas comunes",
                "rows": [
                    ["Lo que + verbo + es/fue...", "Focaliza una acción o idea abstracta: 'Lo que dijo fue revelador'"],
                    ["Es/Fue... quien/el que...", "Focaliza al sujeto o agente: 'Fue Mariana la que redactó el informe'"],
                    ["Es/Fue... cuando/donde...", "Focaliza tiempo o lugar: 'Fue en Lima donde se conocieron'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en contexto",
                "items": [
                    {"spanish": "Lo que más nos sorprendió fue su serenidad.", "english": "What surprised us most was his calmness."},
                    {"spanish": "Fue precisamente en ese momento cuando comprendió el peligro.", "english": "It was precisely at that moment that she understood the danger."},
                    {"spanish": "Lo que conviene destacar es la solidez de los argumentos.", "english": "What is worth highlighting is the soundness of the arguments."}
                ]
            },
            {
                "type": "tip",
                "content": "Evita el queísmo en oraciones hendidas temporales o locativas: en español culto se dice 'Fue allí donde ocurrió' o 'Fue en 1990 cuando nació', no 'Fue allí que' ni 'Fue en 1990 que'."
            }
        ]
    })

    write_json(f"exercises/b2/{l1_stem}-ex.json", {
        "lesson": l1_stem,
        "exercises": [
            {
                "id": "b2-01-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el matiz", "nuance"],
                    ["el hincapié", "emphasis"],
                    ["destacar", "to highlight"],
                    ["el trasfondo", "background, subtext"]
                ],
                "teaches": ["b2-unit01-vocab"]
            },
            {
                "id": "b2-01-01.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones utiliza una estructura hendida para focalizar el motivo principal?",
                "options": [
                    "Lo que realmente motivó su renuncia fue la falta de transparencia.",
                    "Él renunció porque no había suficiente transparencia en el equipo.",
                    "A causa de la falta de transparencia, decidió renunciar."
                ],
                "correct": 0,
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-01.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Lo que conviene __ en este análisis es la coherencia de los datos. (destacar)",
                "answer": "destacar",
                "english": "What is worth highlighting in this analysis is the consistency of the data.",
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-01.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Lo", "que", "más", "nos", "preocupa", "es", "el", "trasfondo", "económico."],
                "solution": ["Lo", "que", "más", "nos", "preocupa", "es", "el", "trasfondo", "económico."],
                "english": "What worries us most is the economic background.",
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Fue precisamente en el Congreso __ se debatió la ley fundamental. (donde)",
                "answer": "donde",
                "english": "It was precisely in Congress where the fundamental law was debated.",
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-01.ex06",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "Lo que intentamos demostrar es que existe un matiz crucial entre ambas posturas.",
                "options": [
                    "What we are trying to show is that a crucial nuance exists between both positions.",
                    "We do not understand the differences between the two positions.",
                    "Both positions are completely identical in every respect."
                ],
                "correct": 0,
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-01.ex07",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Valeria", "text": "¿Qué te pareció la exposición del profesor sobre la crisis?"},
                    {"speaker": "Tú", "text": "_____"},
                    {"speaker": "Valeria", "text": "Totalmente de acuerdo, ese detalle cambió toda la perspectiva."}
                ],
                "options": [
                    "Lo que me pareció más valioso fue cómo explicó el trasfondo histórico.",
                    "El profesor habló durante dos horas seguidas sin parar.",
                    "No recuerdo exactamente a qué hora terminó la conferencia."
                ],
                "correct": 0,
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-01.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": "Formulate a statement emphasizing what really matters in this negotiation using 'Lo que realmente importa...'", "answer": "Lo que realmente importa es alcanzar un acuerdo sostenible."},
                    {"prompt": "Emphasize who led the initiative using 'Fue... quien...'", "answer": "Fue la comisión directiva quien impulsó el diálogo."}
                ],
                "teaches": ["oraciones-hendidas-enfasis", "b2-unit01-vocab"]
            }
        ]
    })

    write_json(f"lessons/b2/{l1_stem}.json", {
        "id": "lesson.b2.01.01",
        "title": "Focus & Cleft Structures",
        "level": "B2",
        "goal": "Use cleft sentences with 'lo que' and 'fue... quien/donde' to emphasize specific information in complex speech.",
        "grammar": "oraciones hendidas",
        "sections": [
            {
                "type": "intro",
                "title": "Unit 1: Nuance, Precision & Emphasis",
                "body": [
                    "Welcome to Spanish B2 Core. At this level, communicative competence expands from reporting facts to shaping perspective, controlling emphasis, and crafting nuanced arguments.",
                    "In this first unit, you will master the rhetorical tools that sophisticated speakers use to direct attention: cleft sentences ('lo que realmente importa es...'), adverbial intensifiers ('propiamente dicho', 'en rigor'), fronting and inversion, and contrastive focus with 'no... sino'."
                ]
            },
            {
                "type": "goal",
                "items": [
                    "Identify and construct cleft sentences using 'lo que es/fue'.",
                    "Emphasize agents, locations, and timeframes with focused 'ser'.",
                    "Use B2 vocabulary to discuss nuances and underlying motives.",
                    "Maintain correct agreement between cleft clauses and plural predicates."
                ]
            },
            {
                "type": "recycle",
                "count": 3
            },
            {
                "type": "grammar",
                "ref": f"grammar/b2/{l1_stem}-a-gr.json"
            },
            {
                "type": "vocabulary",
                "ref": f"vocabulary/b2/{l1_stem}-voc.json"
            },
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": f"exercises/b2/{l1_stem}-ex.json",
                "exerciseRefs": [
                    "b2-01-01.ex01",
                    "b2-01-01.ex02",
                    "b2-01-01.ex03",
                    "b2-01-01.ex04",
                    "b2-01-01.ex05"
                ]
            },
            {
                "type": "exercise-group",
                "title": "Listening",
                "ref": f"exercises/b2/{l1_stem}-ex.json",
                "exerciseRefs": ["b2-01-01.ex06"]
            },
            {
                "type": "exercise-group",
                "title": "Dialogue",
                "ref": f"exercises/b2/{l1_stem}-ex.json",
                "exerciseRefs": ["b2-01-01.ex07"]
            },
            {
                "type": "exercise-group",
                "title": "Writing",
                "ref": f"exercises/b2/{l1_stem}-ex.json",
                "exerciseRefs": ["b2-01-01.ex08"]
            },
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can identify and construct cleft sentences using 'lo que es/fue'.",
                    "I can emphasize agents, locations, and timeframes with focused 'ser'.",
                    "I can use B2 vocabulary to discuss nuances and underlying motives.",
                    "I can maintain correct agreement between cleft clauses and plural predicates."
                ]
            }
        ]
    })

    # Lesson 2: Adverbial Intensifiers & Nuance
    l2_stem = "b2-01-02"
    write_json(f"vocabulary/b2/{l2_stem}-voc.json", {
        "id": "vocab.b2.01.02",
        "lesson": l2_stem,
        "title": "Adverbios de matiz y precisión",
        "theme": "Matices y precisión argumentativa",
        "words": [
            {"lemma": "francamente", "translation": "frankly", "pos": "adverb"},
            {"lemma": "propiamente", "translation": "properly, strictly speaking", "pos": "adverb"},
            {"lemma": "en rigor", "translation": "strictly speaking", "pos": "expression"},
            {"lemma": "rotundamente", "translation": "categorically, flatly", "pos": "adverb"},
            {"lemma": "apenas", "translation": "scarcely, barely", "pos": "adverb"},
            {"lemma": "notablemente", "translation": "notably, remarkably", "pos": "adverb"},
            {"lemma": "indudablemente", "translation": "undoubtedly", "pos": "adverb"},
            {"lemma": "deliberadamente", "translation": "deliberately", "pos": "adverb"}
        ]
    })

    write_json(f"grammar/b2/{l2_stem}-a-gr.json", {
        "id": "grammar.b2.01.02.adverbios-intensificadores",
        "title": "Adverbios de matiz y precisión discursiva",
        "sections": [
            {
                "type": "text",
                "title": "El papel de los adverbios modales en B2",
                "content": "A nivel B2, los adverbios no solo modifican al verbo; actúan sobre toda la oración como modificadores oracionales o marcadores de actitud epistémica: 'Francamente, no me convence la propuesta' o 'En rigor, no se trata de un fenómeno nuevo'."
            },
            {
                "type": "table",
                "title": "Adverbios de matiz y precisión",
                "rows": [
                    ["Propiamente dicho", "Aclara si un término se aplica con exactitud: 'No es una ley propiamente dicha'"],
                    ["En rigor", "Introduce una delimitación formal o técnica: 'En rigor, la fecha límite expiró ayer'"],
                    ["Rotundamente", "Expresa convicción o rechazo categórico: 'Negó rotundamente las acusaciones'"],
                    ["Notablemente", "Indica un grado visible de intensidad o cambio: 'Las condiciones mejoraron notablemente'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en prosa formal",
                "items": [
                    {"spanish": "En rigor, el problema radica en la distribución de los recursos.", "english": "Strictly speaking, the problem lies in the distribution of resources."},
                    {"spanish": "El informe desmiente rotundamente cualquier irregularidad.", "english": "The report flatly refutes any irregularity."},
                    {"spanish": "Aquella medida influyó notablemente en el desarrollo posterior.", "english": "That measure notably influenced subsequent development."}
                ]
            },
            {
                "type": "tip",
                "content": "Los modificadores oracionales como 'francamente', 'indudablemente' o 'en rigor' van aislados entre comas cuando inician o se intercalan en la oración: 'El acuerdo, en rigor, aún no tiene validez legal'."
            }
        ]
    })

    write_json(f"exercises/b2/{l2_stem}-ex.json", {
        "lesson": l2_stem,
        "exercises": [
            {
                "id": "b2-01-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["francamente", "frankly"],
                    ["en rigor", "strictly speaking"],
                    ["rotundamente", "categorically, flatly"],
                    ["indudablemente", "undoubtedly"]
                ],
                "teaches": ["b2-unit01-vocab"]
            },
            {
                "id": "b2-01-02.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué adverbio expresa un rechazo categórico y absoluto?",
                "options": [
                    "Rotundamente",
                    "Apenas",
                    "Propiamente"
                ],
                "correct": 0,
                "teaches": ["adverbios-intensificadores"]
            },
            {
                "id": "b2-01-02.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En __, no podemos calificar este resultado como un fracaso total. (rigor)",
                "answer": "rigor",
                "english": "Strictly speaking, we cannot describe this result as a complete failure.",
                "teaches": ["adverbios-intensificadores"]
            },
            {
                "id": "b2-01-02.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "ministro", "rechazó", "rotundamente", "las", "acusaciones", "de", "corrupción."],
                "solution": ["El", "ministro", "rechazó", "rotundamente", "las", "acusaciones", "de", "corrupción."],
                "english": "The minister flatly rejected the corruption accusations.",
                "teaches": ["adverbios-intensificadores"]
            },
            {
                "id": "b2-01-02.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las condiciones de vida han mejorado __ en la última década. (notable)",
                "answer": "notablemente",
                "english": "Living conditions have remarkably improved over the last decade.",
                "teaches": ["adverbios-intensificadores"]
            },
            {
                "id": "b2-01-02.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sebastián", "text": "¿Crees que ya podemos dar por terminado el proyecto?"},
                    {"speaker": "Tú", "text": "_____"},
                    {"speaker": "Sebastián", "text": "Tienes razón, faltan las revisiones finales."}
                ],
                "options": [
                    "En rigor, todavía queda pendiente la auditoría externa.",
                    "Ayer almorzamos en el centro con todo el equipo.",
                    "A lo mejor el próximo año compramos computadoras nuevas."
                ],
                "correct": 0,
                "teaches": ["adverbios-intensificadores"]
            },
            {
                "id": "b2-01-02.ex07",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": "Express your candid opinion about a policy using 'Francamente...'", "answer": "Francamente, considero que la medida llega con demasiado retraso."},
                    {"prompt": "Qualify a technical concept using 'En rigor...'", "answer": "En rigor, el documento requiere una ratificación parlamentaria."}
                ],
                "teaches": ["adverbios-intensificadores", "b2-unit01-vocab"]
            }
        ]
    })

    write_json(f"lessons/b2/{l2_stem}.json", {
        "id": "lesson.b2.01.02",
        "title": "Adverbial Intensifiers & Nuance",
        "level": "B2",
        "goal": "Qualify assertions and express stance using sentence-level adverbs like 'francamente', 'en rigor', and 'rotundamente'.",
        "grammar": "adverbios de matiz",
        "sections": [
            {
                "type": "goal",
                "items": [
                    "Use sentence-level adverbs to calibrate certainty and epistemic stance.",
                    "Differentiate between technical qualification ('en rigor') and candid stance ('francamente').",
                    "Punctuate sentence adverbs accurately with commas.",
                    "Apply targeted vocabulary for formal debate and assessment."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l2_stem}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l2_stem}-voc.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": f"exercises/b2/{l2_stem}-ex.json",
                "exerciseRefs": [
                    "b2-01-02.ex01",
                    "b2-01-02.ex02",
                    "b2-01-02.ex03",
                    "b2-01-02.ex04",
                    "b2-01-02.ex05"
                ]
            },
            {
                "type": "exercise-group",
                "title": "Dialogue",
                "ref": f"exercises/b2/{l2_stem}-ex.json",
                "exerciseRefs": ["b2-01-02.ex06"]
            },
            {
                "type": "exercise-group",
                "title": "Writing",
                "ref": f"exercises/b2/{l2_stem}-ex.json",
                "exerciseRefs": ["b2-01-02.ex07"]
            },
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can use sentence-level adverbs to calibrate certainty and epistemic stance.",
                    "I can differentiate between technical qualification ('en rigor') and candid stance ('francamente').",
                    "I can punctuate sentence adverbs accurately with commas.",
                    "I can apply targeted vocabulary for formal debate and assessment."
                ]
            }
        ]
    })

    # Lesson 3: Emphatic Inversion & Fronting
    l3_stem = "b2-01-03"
    write_json(f"vocabulary/b2/{l3_stem}-voc.json", {
        "id": "vocab.b2.01.03",
        "lesson": l3_stem,
        "title": "Inversión y relieve discursivo",
        "theme": "Matices y precisión argumentativa",
        "words": [
            {"lemma": "la relevancia", "translation": "relevance", "pos": "noun"},
            {"lemma": "primordial", "translation": "paramount, essential", "pos": "adjective"},
            {"lemma": "prevalecer", "translation": "to prevail", "pos": "verb"},
            {"lemma": "el giro", "translation": "turn, shift", "pos": "noun"},
            {"lemma": "insólito", "translation": "unheard of, unusual", "pos": "adjective"},
            {"lemma": "la premisa", "translation": "premise", "pos": "noun"},
            {"lemma": "concluyente", "translation": "conclusive", "pos": "adjective"},
            {"lemma": "subyacer", "translation": "to underlie", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l3_stem}-a-gr.json", {
        "id": "grammar.b2.01.03.inversion-enfasis",
        "title": "La anteposición enfática y la inversión verbo-sujeto",
        "sections": [
            {
                "type": "text",
                "title": "¿En qué consiste la anteposición enfática?",
                "content": "En la prosa formal y académica, colocar un adjetivo o complemento circunstancial al principio de la oración crea relieve informativo y fuerza la inversión del sujeto: 'Crucial fue la intervención del mediador' en lugar de 'La intervención del mediador fue crucial'."
            },
            {
                "type": "table",
                "title": "Patrones de anteposición y relieve",
                "rows": [
                    ["Adjetivo antepuesto + ser + sujeto", "Enfatiza la cualidad: 'Incalculable fue el daño sufrido'"],
                    ["Complemento adverbial + verbo + sujeto", "Enfatiza las circunstancias: 'En aquella ciudad comenzó la rebelión'"],
                    ["Objeto directo focalizado sin reduplicación", "Enfoca el objeto como tema exclusivo: 'Tres cartas escribió el autor aquel día'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el discurso formal",
                "items": [
                    {"spanish": "Primordial resultó el acuerdo firmado entre ambos países.", "english": "The agreement signed between both countries turned out to be paramount."},
                    {"spanish": "Bajo esa premisa trabajaron los investigadores durante años.", "english": "Under that premise the researchers worked for years."},
                    {"spanish": "De enorme relevancia son los hallazgos recientes.", "english": "Of immense relevance are the recent findings."}
                ]
            },
            {
                "type": "tip",
                "content": "La inversión enfática debe usarse con moderación para marcar momentos culminantes en un argumento o narración. Si se sobreutiliza, el texto puede sonar recargado o artificial."
            }
        ]
    })

    write_json(f"exercises/b2/{l3_stem}-ex.json", {
        "lesson": l3_stem,
        "exercises": [
            {
                "id": "b2-01-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la relevancia", "relevance"],
                    ["primordial", "paramount, essential"],
                    ["prevalecer", "to prevail"],
                    ["insólito", "unheard of, unusual"]
                ],
                "teaches": ["b2-unit01-vocab"]
            },
            {
                "id": "b2-01-03.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes oraciones presenta una anteposición enfática con inversión del sujeto?",
                "options": [
                    "Decisiva fue la intervención del cuerpo diplomático.",
                    "La intervención del cuerpo diplomático fue decisiva.",
                    "El cuerpo diplomático intervino de forma muy decisiva."
                ],
                "correct": 0,
                "teaches": ["inversion-enfasis-fronting"]
            },
            {
                "id": "b2-01-03.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "De suma importancia __ las conclusiones del último congreso científico. (ser)",
                "answer": "fueron",
                "english": "Of utmost importance were the conclusions of the latest scientific congress.",
                "teaches": ["inversion-enfasis-fronting"]
            },
            {
                "id": "b2-01-03.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Insólito", "resultó", "el", "giro", "político", "en", "aquella", "región."],
                "solution": ["Insólito", "resultó", "el", "giro", "político", "en", "aquella", "región."],
                "english": "Unprecedented was the political turn in that region.",
                "teaches": ["inversion-enfasis-fronting"]
            },
            {
                "id": "b2-01-03.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Camila", "text": "¿Por qué le dieron tanta cobertura al informe de auditoría?"},
                    {"speaker": "Tú", "text": "_____"},
                    {"speaker": "Camila", "text": "Por eso todo el gabinete estuvo presente en la lectura."}
                ],
                "options": [
                    "Concluyentes fueron las pruebas presentadas por la fiscalía.",
                    "Ayer compramos varios periódicos en la esquina.",
                    "El informe tenía más de quinientas páginas en total."
                ],
                "correct": 0,
                "teaches": ["inversion-enfasis-fronting"]
            },
            {
                "id": "b2-01-03.ex06",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": "Transform 'El papel de los docentes fue fundamental' using emphatic fronting", "answer": "Fundamental fue el papel de los docentes en todo el proceso."},
                    {"prompt": "State a key finding using 'De enorme relevancia...'", "answer": "De enorme relevancia resultaron las conclusiones del estudio."}
                ],
                "teaches": ["inversion-enfasis-fronting", "b2-unit01-vocab"]
            }
        ]
    })

    write_json(f"lessons/b2/{l3_stem}.json", {
        "id": "lesson.b2.01.03",
        "title": "Emphatic Inversion & Fronting",
        "level": "B2",
        "goal": "Employ emphatic word order fronting and subject-verb inversion to add rhetorical weight to key adjectives and clauses.",
        "grammar": "inversión enfática",
        "sections": [
            {
                "type": "goal",
                "items": [
                    "Recognize and construct fronted emphatic structures with verb-subject inversion.",
                    "Apply fronting to highlight adjectives of evaluation ('crucial fue', 'insólito resultó').",
                    "Maintain subject-verb agreement when the inverted subject is plural.",
                    "Integrate formal academic vocabulary into persuasive rhetoric."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l3_stem}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l3_stem}-voc.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": f"exercises/b2/{l3_stem}-ex.json",
                "exerciseRefs": [
                    "b2-01-03.ex01",
                    "b2-01-03.ex02",
                    "b2-01-03.ex03",
                    "b2-01-03.ex04"
                ]
            },
            {
                "type": "exercise-group",
                "title": "Dialogue",
                "ref": f"exercises/b2/{l3_stem}-ex.json",
                "exerciseRefs": ["b2-01-03.ex05"]
            },
            {
                "type": "exercise-group",
                "title": "Writing",
                "ref": f"exercises/b2/{l3_stem}-ex.json",
                "exerciseRefs": ["b2-01-03.ex06"]
            },
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can recognize and construct fronted emphatic structures with verb-subject inversion.",
                    "I can apply fronting to highlight adjectives of evaluation ('crucial fue', 'insólito resultó').",
                    "I can maintain subject-verb agreement when the inverted subject is plural.",
                    "I can integrate formal academic vocabulary into persuasive rhetoric."
                ]
            }
        ]
    })

    # Lesson 4: Contrastive Focus with "No... Sino"
    l4_stem = "b2-01-04"
    write_json(f"vocabulary/b2/{l4_stem}-voc.json", {
        "id": "vocab.b2.01.04",
        "lesson": l4_stem,
        "title": "Contraste y refutación",
        "theme": "Matices y precisión argumentativa",
        "words": [
            {"lemma": "la discrepancia", "translation": "discrepancy", "pos": "noun"},
            {"lemma": "refutar", "translation": "to refute", "pos": "verb"},
            {"lemma": "la paradoja", "translation": "paradox", "pos": "noun"},
            {"lemma": "antagónico", "translation": "antagonistic, opposing", "pos": "adjective"},
            {"lemma": "la sutileza", "translation": "subtlety", "pos": "noun"},
            {"lemma": "soslayar", "translation": "to bypass, to evade", "pos": "verb"},
            {"lemma": "más bien", "translation": "rather, instead", "pos": "expression"},
            {"lemma": "contraponer", "translation": "to contrast, to counterpose", "pos": "verb"}
        ]
    })

    write_json(f"grammar/b2/{l4_stem}-a-gr.json", {
        "id": "grammar.b2.01.04.enfasis-contrastivo-sino",
        "title": "Foco contrastivo: no... sino (que)",
        "sections": [
            {
                "type": "text",
                "title": "Estructuras contrastivas de corrección",
                "content": "Para refutar un supuesto previo y sustituirlo por el verdadero elemento focalizado, el español emplea la correlación 'no... sino': 'No fue el cansancio, sino la falta de tiempo lo que nos impidió viajar'."
            },
            {
                "type": "text",
                "title": "Sino frente a sino que",
                "content": "Cuando el segundo elemento contiene un verbo conjugado, se requiere obligatoriamente 'sino que': 'No se desentendieron del problema, sino que propusieron una reforma estructural'."
            },
            {
                "type": "table",
                "title": "Variaciones de corrección y matiz",
                "rows": [
                    ["No solo... sino también...", "Adición enfática: 'No solo analizó las causas, sino también las consecuencias'"],
                    ["No... sino más bien...", "Matiz atenuado: 'No es un error grave, sino más bien una imprecisión'"],
                    ["No fue X quien/el que...", "Cleft contrastiva: 'No fue el gobierno, sino las comunidades quienes actuaron'"]
                ]
            },
            {
                "type": "examples",
                "title": "Ejemplos en el debate argumentativo",
                "items": [
                    {"spanish": "El objetivo no es soslayar el conflicto, sino resolverlo de raíz.", "english": "The objective is not to sidestep the conflict, but to resolve it at its root."},
                    {"spanish": "No fue la casualidad, sino años de disciplina lo que le dio el triunfo.", "english": "It was not chance, but years of discipline that brought him triumph."},
                    {"spanish": "No rechazaron la propuesta, sino que solicitaron mayores precisiones.", "english": "They did not reject the proposal, but rather requested greater clarification."}
                ]
            },
            {
                "type": "tip",
                "content": "No confundas 'sino' (conjunción adversativa) con 'si no' (condicional negativa). 'Sino' sustituye o añade; 'si no' introduce una hipótesis negativa: 'No quiero té, sino café' frente a 'Si no vienes hoy, no te veré'."
            }
        ]
    })

    write_json(f"exercises/b2/{l4_stem}-ex.json", {
        "lesson": l4_stem,
        "exercises": [
            {
                "id": "b2-01-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la discrepancia", "discrepancy"],
                    ["refutar", "to refute"],
                    ["la paradoja", "paradox"],
                    ["soslayar", "to bypass, to evade"]
                ],
                "teaches": ["b2-unit01-vocab"]
            },
            {
                "id": "b2-01-04.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la forma correcta cuando el segundo término introduce un verbo conjugado?",
                "options": [
                    "No desestimaron la queja, sino que abrieron una investigación de inmediato.",
                    "No desestimaron la queja, sino abrieron una investigación de inmediato.",
                    "No desestimaron la queja, pero que abrieron una investigación de inmediato."
                ],
                "correct": 0,
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-04.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No buscamos eludir el problema, __ enfrentarlo con absoluta franqueza. (sino)",
                "answer": "sino",
                "english": "We do not seek to evade the problem, but rather to face it with absolute frankness.",
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-04.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "fue", "el", "miedo,", "sino", "la", "prudencia", "lo", "que", "guió", "sus", "pasos."],
                "solution": ["No", "fue", "el", "miedo,", "sino", "la", "prudencia", "lo", "que", "guió", "sus", "pasos."],
                "english": "It was not fear, but prudence that guided their steps.",
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-04.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No rechazaron el plan inicial, sino __ exigieron ciertas garantías adicionales. (que)",
                "answer": "que",
                "english": "They did not reject the initial plan, but rather demanded certain additional guarantees.",
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-04.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Mateo", "text": "¿Afirmaron los directivos que los resultados fueron un fracaso?"},
                    {"speaker": "Tú", "text": "_____"},
                    {"speaker": "Mateo", "text": "Ah, entiendo, fue un ajuste de expectativas."}
                ],
                "options": [
                    "No dijeron que fue un fracaso, sino que las metas eran demasiado ambiciosas.",
                    "Los directivos se fueron a almorzar antes de terminar la sesión.",
                    "Mañana vamos a revisar las cifras con el contador."
                ],
                "correct": 0,
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-04.ex07",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": "Contrast two causes using 'No fue... sino...'", "answer": "No fue la falta de recursos, sino la falta de coordinación lo que retrasó la obra."},
                    {"prompt": "Correct a misinterpretation using 'sino que...'", "answer": "El ponente no criticó el modelo, sino que propuso actualizar sus variables."}
                ],
                "teaches": ["enfasis-contrastivo-sino", "b2-unit01-vocab"]
            }
        ]
    })

    write_json(f"lessons/b2/{l4_stem}.json", {
        "id": "lesson.b2.01.04",
        "title": "Contrastive Focus with 'No... Sino'",
        "level": "B2",
        "goal": "Refute misconceptions and articulate contrastive focus using 'no... sino' and 'sino que' in formal argumentative prose.",
        "grammar": "foco contrastivo",
        "sections": [
            {
                "type": "goal",
                "items": [
                    "Refute assertions and specify correct alternatives with 'no... sino'.",
                    "Distinguish syntactically between 'sino' (phrase) and 'sino que' (finite clause).",
                    "Construct contrastive cleft sentences ('no fue X sino Y lo que...').",
                    "Use precise vocabulary for academic debate and critique."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "grammar", "ref": f"grammar/b2/{l4_stem}-a-gr.json"},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l4_stem}-voc.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": f"exercises/b2/{l4_stem}-ex.json",
                "exerciseRefs": [
                    "b2-01-04.ex01",
                    "b2-01-04.ex02",
                    "b2-01-04.ex03",
                    "b2-01-04.ex04",
                    "b2-01-04.ex05"
                ]
            },
            {
                "type": "exercise-group",
                "title": "Dialogue",
                "ref": f"exercises/b2/{l4_stem}-ex.json",
                "exerciseRefs": ["b2-01-04.ex06"]
            },
            {
                "type": "exercise-group",
                "title": "Writing",
                "ref": f"exercises/b2/{l4_stem}-ex.json",
                "exerciseRefs": ["b2-01-04.ex07"]
            },
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can refute assertions and specify correct alternatives with 'no... sino'.",
                    "I can distinguish syntactically between 'sino' (phrase) and 'sino que' (finite clause).",
                    "I can construct contrastive cleft sentences ('no fue X sino Y lo que...').",
                    "I can use precise vocabulary for academic debate and critique."
                ]
            }
        ]
    })

    # Lesson 5: Narrative Nuance & Synthesis (with Classic Story: El jardín de senderos que se bifurcan)
    l5_stem = "b2-01-05"
    story_rel = "stories/classics/b2/b2-01.json"
    write_json(f"stories/classics/b2/b2-01.json", {
        "id": "story.b2.01",
        "title": "El enigma del jardín",
        "level": "B2",
        "lesson": 5,
        "order": 1,
        "type": "classic",
        "estimatedMinutes": 6,
        "characters": ["Dr. Yu Tsun", "Stephen Albert"],
        "summary": "Adaptación pedagógica para nivel B2 del célebre relato metafísico de Jorge Luis Borges sobre el tiempo, el laberinto y el destino.",
        "author": "Jorge Luis Borges",
        "work": "Ficciones: El jardín de senderos que se bifurcan (1941)",
        "source": "Adaptado para estudiantes de nivel B2 a partir del texto clásico de Jorge Luis Borges",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Aquella tarde lluviosa en los suburbios de Ashgrove, Yu Tsun sentía que cada segundo pesaba como una eternidad. Lo que realmente guiaba sus pasos no era el miedo a la captura, sino una necesidad implacable de transmitir un secreto antes de que el capitán Richard Madden le diera alcance. En rigor, toda su vida parecía haberse reducido a esa última misión desesperada."
            },
            {
                "type": "narration",
                "text": "Al llegar al portón de hierro de la vieja casa de campo, fue una extraña melodía oriental lo que lo detuvo en seco. Stephen Albert, el erudito sinólogo inglés, lo recibió con una serenidad insólita, como si lo hubiera esperado durante décadas. No lo invitó a pasar como a un enemigo, sino como a un interlocutor largamente anhelado."
            },
            {
                "type": "narration",
                "text": "—Usted habrá venido a ver el jardín de senderos que se bifurcan —dijo Albert con voz reposada—. Lo que casi nadie comprende es que el libro y el laberinto son un solo y mismo objeto. Ts'ui Pên no dejó dos obras inconclusas, sino un solo proyecto infinito."
            },
            {
                "type": "narration",
                "text": "Yu Tsun escuchaba fascinado mientras el anciano desplegaba los manuscritos sobre la mesa de caoba. Decisiva resultó aquella explicación para desentrañar el enigma de sus propios antepasados. Ts'ui Pên no creía en un tiempo uniforme y absoluto, sino en una red infinita de tiempos divergentes y paralelos que se bifurcan perpetuamente."
            },
            {
                "type": "narration",
                "text": "—En la mayoría de esos tiempos —susurró Albert mirándolo fijamente—, nosotros no existimos; en otros, usted es mi amigo y yo su discípulo; en este, por desgracia, el destino nos ha colocado en bandos opuestos. Yu Tsun comprendió entonces que no era el azar, sino el tiempo inexorable lo que había sellado aquel encuentro."
            }
        ]
    })

    write_json(f"vocabulary/b2/{l5_stem}-voc.json", {
        "id": "vocab.b2.01.05",
        "lesson": l5_stem,
        "title": "Vocabulario de la narración filosófica",
        "theme": "Matices y precisión argumentativa",
        "words": [
            {"lemma": "la bifurcación", "translation": "fork, branching", "pos": "noun"},
            {"lemma": "el enigma", "translation": "enigma, puzzle", "pos": "noun"},
            {"lemma": "el laberinto", "translation": "labyrinth, maze", "pos": "noun"},
            {"lemma": "la conjetura", "translation": "conjecture, guess", "pos": "noun"},
            {"lemma": "el indicio", "translation": "clue, indication", "pos": "noun"},
            {"lemma": "perplejo", "translation": "perplexed", "pos": "adjective"},
            {"lemma": "vislumbrar", "translation": "to glimpse, to discern", "pos": "verb"},
            {"lemma": "la resolución", "translation": "resolution, outcome", "pos": "noun"}
        ]
    })

    write_json(f"grammar/b2/{l5_stem}-a-gr.json", {
        "id": "grammar.b2.01.05.sintesis-enfasis",
        "title": "Síntesis del relieve discursivo en la prosa literaria",
        "sections": [
            {
                "type": "text",
                "title": "La alternancia estilística en la narración",
                "content": "Los grandes prosistas hispanoamericanos combinan oraciones hendidas ('lo que realmente guiaba sus pasos era...'), anteposiciones enfáticas ('decisiva resultó aquella explicación') y estructuras contrastivas ('no creía en un tiempo uniforme, sino en una red infinita') para crear ritmo, tensión dramática y profundidad filosófica."
            },
            {
                "type": "table",
                "title": "Integración de recursos enfáticos",
                "rows": [
                    ["Oración hendida", "Lo que casi nadie comprende es que el libro y el laberinto son lo mismo."],
                    ["Inversión de predicado", "Decisiva resultó aquella conversación para revelar el secreto."],
                    ["Foco contrastivo", "No buscaba el poder terrenal, sino la inmortalidad literaria."]
                ]
            },
            {
                "type": "examples",
                "title": "Modelos literarios de B2",
                "items": [
                    {"spanish": "Fue en el silencio del estudio donde vislumbró la verdad.", "english": "It was in the silence of the study where he glimpsed the truth."},
                    {"spanish": "No era el cansancio, sino una honda perplejidad lo que nublaba su mente.", "english": "It was not fatigue, but deep perplexity that clouded his mind."}
                ]
            },
            {
                "type": "tip",
                "content": "Al redactar ensayos o narraciones complejas, varía la estructura sintáctica: alterna oraciones de orden canónico (sujeto-verbo-objeto) con oraciones hendidas o invertidas para destacar giros argumentales."
            }
        ]
    })

    write_json(f"exercises/b2/{l5_stem}-ex.json", {
        "lesson": l5_stem,
        "exercises": [
            {
                "id": "b2-01-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la bifurcación", "fork, branching"],
                    ["el enigma", "enigma, puzzle"],
                    ["perplejo", "perplexed"],
                    ["vislumbrar", "to glimpse, to discern"]
                ],
                "teaches": ["b2-unit01-vocab"]
            },
            {
                "id": "b2-01-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según el relato, ¿cuál era la verdadera naturaleza de la obra de Ts'ui Pên?",
                "options": [
                    "El libro y el laberinto eran un solo y mismo objeto infinito sobre el tiempo.",
                    "Ts'ui Pên había abandonado la novela para construir un laberinto de piedra.",
                    "El manuscrito era un diario militar sin ningún valor literario ni filosófico."
                ],
                "correct": 0
            },
            {
                "id": "b2-01-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cómo concebía el tiempo el antepasado de Yu Tsun según Albert?",
                "options": [
                    "Como una red infinita de tiempos divergentes y paralelos que se bifurcan.",
                    "Como una línea recta implacable que marcha hacia un único final.",
                    "Como una ilusión óptica sin ninguna trascendencia para el ser humano."
                ],
                "correct": 0
            },
            {
                "id": "b2-01-05.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Lo que realmente conmovió al protagonista __ la lucidez con la que Albert explicaba el laberinto. (ser)",
                "answer": "fue",
                "english": "What truly moved the protagonist was the lucidity with which Albert explained the labyrinth.",
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-05.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Decisiva", "resultó", "la", "conversación", "para", "desentrañar", "aquel", "enigma."],
                "solution": ["Decisiva", "resultó", "la", "conversación", "para", "desentrañar", "aquel", "enigma."],
                "english": "Decisive was the conversation in unravelling that enigma.",
                "teaches": ["inversion-enfasis-fronting"]
            },
            {
                "id": "b2-01-05.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No perseguía la gloria militar, __ comprender la naturaleza del tiempo. (sino)",
                "answer": "sino",
                "english": "He did not seek military glory, but rather to understand the nature of time.",
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-05.ex07",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Profesora", "text": "¿Qué función cumple la estructura 'No fue... sino...' en el clímax del relato?"},
                    {"speaker": "Tú", "text": "_____"},
                    {"speaker": "Profesora", "text": "Exacto, concentra la atención en la tesis filosófica central."}
                ],
                "options": [
                    "Permite corregir una falsa interpretación y destacar que el laberinto es temporal, no físico.",
                    "Sirve para indicar que los personajes cambiaron de lugar geográfico.",
                    "Indica que el narrador se equivocó de interlocutor al llegar a la estación."
                ],
                "correct": 0,
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-05.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": "Summarize the core philosophical revelation of the story using a cleft sentence", "answer": "Lo que Ts'ui Pên descubrió fue que el tiempo se bifurca perpetuamente."},
                    {"prompt": "Contrast the nature of the labyrinth using 'no... sino'", "answer": "El laberinto no era un dédalo de arbustos, sino una novela infinita."}
                ],
                "teaches": ["oraciones-hendidas-enfasis", "enfasis-contrastivo-sino", "b2-unit01-vocab"]
            }
        ]
    })

    write_json(f"lessons/b2/{l5_stem}.json", {
        "id": "lesson.b2.01.05",
        "title": "Narrative Nuance & Synthesis",
        "level": "B2",
        "goal": "Read and analyze nuanced literary prose, integrating cleft sentences, inversion, and contrastive focus.",
        "grammar": "síntesis de relieve discursivo",
        "sections": [
            {
                "type": "goal",
                "items": [
                    "Analyze an adapted classic narrative by Jorge Luis Borges for nuanced syntactic emphasis.",
                    "Combine cleft sentences, fronted adjectives, and contrastive 'sino' in analytical commentary.",
                    "Express philosophical and abstract conjectures with B2 precision.",
                    "Synthesize the unit's vocabulary and rhetorical structures."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": story_rel},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{l5_stem}-voc.json"},
            {"type": "grammar", "ref": f"grammar/b2/{l5_stem}-a-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": f"exercises/b2/{l5_stem}-ex.json",
                "exerciseRefs": [
                    "b2-01-05.ex01",
                    "b2-01-05.ex02",
                    "b2-01-05.ex03",
                    "b2-01-05.ex04",
                    "b2-01-05.ex05",
                    "b2-01-05.ex06"
                ]
            },
            {
                "type": "exercise-group",
                "title": "Dialogue",
                "ref": f"exercises/b2/{l5_stem}-ex.json",
                "exerciseRefs": ["b2-01-05.ex07"]
            },
            {
                "type": "exercise-group",
                "title": "Writing",
                "ref": f"exercises/b2/{l5_stem}-ex.json",
                "exerciseRefs": ["b2-01-05.ex08"]
            },
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can analyze an adapted classic narrative by Jorge Luis Borges for nuanced syntactic emphasis.",
                    "I can combine cleft sentences, fronted adjectives, and contrastive 'sino' in analytical commentary.",
                    "I can express philosophical and abstract conjectures with B2 precision.",
                    "I can synthesize the unit's vocabulary and rhetorical structures."
                ]
            }
        ]
    })

    # Consolidation Lesson: b2-01-consolidation
    c_stem = "b2-01-consolidation"
    write_json(f"exercises/b2/{c_stem}-ex.json", {
        "lesson": c_stem,
        "exercises": [
            {
                "id": "b2-01-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el trasfondo", "background, subtext"],
                    ["prevalecer", "to prevail"],
                    ["soslayar", "to bypass, to evade"],
                    ["vislumbrar", "to glimpse, to discern"]
                ],
                "teaches": ["b2-unit01-vocab"]
            },
            {
                "id": "b2-01-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Lo que verdaderamente nos interesa __ profundizar en las causas estructurales. (ser)",
                "answer": "es",
                "english": "What truly interests us is to delve deeper into the structural causes.",
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-consolidation.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la opción que califica rigurosamente un término técnico?",
                "options": [
                    "En rigor, el tratado todavía no ha entrado en vigor.",
                    "Apenas el tratado entre en vigor, avisaremos.",
                    "Francamente, el tratado es muy largo de leer."
                ],
                "correct": 0,
                "teaches": ["adverbios-intensificadores"]
            },
            {
                "id": "b2-01-consolidation.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Primordial", "resultó", "el", "respaldo", "de", "las", "comunidades", "locales."],
                "solution": ["Primordial", "resultó", "el", "respaldo", "de", "las", "comunidades", "locales."],
                "english": "Paramount was the backing of the local communities.",
                "teaches": ["inversion-enfasis-fronting"]
            },
            {
                "id": "b2-01-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No fue la suerte, __ la constancia lo que aseguró el éxito. (sino)",
                "answer": "sino",
                "english": "It was not luck, but perseverance that ensured success.",
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-consolidation.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No ocultaron los errores, sino __ presentaron un plan de remediación inmediato. (que)",
                "answer": "que",
                "english": "They did not hide the mistakes, but rather presented an immediate remediation plan.",
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-01-consolidation.ex07",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "En un debate formal sobre políticas públicas, ¿cómo responderías para centrar el debate en lo esencial?",
                "options": [
                    "Lo que no debemos soslayar es la sostenibilidad fiscal a largo plazo.",
                    "Creo que todos deberíamos irnos a descansar porque ya es tarde.",
                    "Ayer leí en las noticias que llovió mucho en el sur."
                ],
                "correct": 0,
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-01-consolidation.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": "State an argument emphasizing the real root of an issue using cleft focus and 'sino'", "answer": "Lo que debemos atender no son los síntomas, sino las causas fundamentales."}
                ],
                "teaches": ["oraciones-hendidas-enfasis", "enfasis-contrastivo-sino", "b2-unit01-vocab"]
            }
        ]
    })

    write_json(f"lessons/b2/{c_stem}.json", {
        "id": "lesson.b2.01.consolidation",
        "title": "Unit 1 Consolidation",
        "level": "B2",
        "goal": "Consolidate cleft sentences, emphatic word order, adverbial intensifiers, and contrastive focus.",
        "grammar": "matices y énfasis",
        "sections": [
            {
                "type": "goal",
                "items": [
                    "Consolidate cleft sentences with 'lo que' and focused 'ser'.",
                    "Employ sentence-level adverbs ('en rigor', 'rotundamente') with precision.",
                    "Apply fronting and subject-verb inversion in rhetorical evaluation.",
                    "Construct refined contrastive arguments using 'no... sino (que)'."
                ]
            },
            {"type": "recycle", "count": 3},
            {
                "type": "exercise-group",
                "title": "Review",
                "ref": f"exercises/b2/{c_stem}-ex.json",
                "exerciseRefs": [
                    "b2-01-consolidation.ex01",
                    "b2-01-consolidation.ex02",
                    "b2-01-consolidation.ex03",
                    "b2-01-consolidation.ex04",
                    "b2-01-consolidation.ex05",
                    "b2-01-consolidation.ex06",
                    "b2-01-consolidation.ex07",
                    "b2-01-consolidation.ex08"
                ]
            },
            {
                "type": "checklist",
                "items": [
                    "I can consolidate cleft sentences with 'lo que' and focused 'ser'.",
                    "I can employ sentence-level adverbs ('en rigor', 'rotundamente') with precision.",
                    "I can apply fronting and subject-verb inversion in rhetorical evaluation.",
                    "I can construct refined contrastive arguments using 'no... sino (que)'."
                ]
            }
        ]
    })
    print("Generated Core B2 Unit 1 successfully.")


# ==============================================================================
# 2. LATAM REGIONAL STUDIES B2 UNIT 1: Mexico I: Central Mexico & Valley of Anáhuac
# ==============================================================================

def generate_latam_unit_1():
    # Slug: mexicocentro
    # Vocab skill: b2-mexicocentro-vocab
    # Grammar skills integrated:
    #   - oraciones-hendidas-enfasis
    #   - inversion-enfasis-fronting
    #   - adverbios-intensificadores
    #   - enfasis-contrastivo-sino

    lessons_meta = [
        {
            "num": 1,
            "title": "El Valle de México: Cuenca lacustre y geología",
            "goal": "Describe the geological formation of the Valley of Mexico, Lake Texcoco, and the ongoing challenge of urban subsidence.",
            "seg_slug": "geografia",
            "story_title": "La cuenca lacustre y el valle hundido",
            "story_summary": "Análisis geográfico e hidrográfico de la cuenca endorreica del Valle de México, el anillo volcánico y el fenómeno contemporáneo del hundimiento del terreno.",
            "words": [
                {"lemma": "la cuenca", "translation": "basin", "pos": "noun"},
                {"lemma": "el hundimiento", "translation": "subsidence, sinking", "pos": "noun"},
                {"lemma": "lacustre", "translation": "lacustrine, lake-related", "pos": "adjective"},
                {"lemma": "la cordillera", "translation": "mountain range", "pos": "noun"},
                {"lemma": "el acuífero", "translation": "aquifer", "pos": "noun"},
                {"lemma": "la desecación", "translation": "drainage, desiccation", "pos": "noun"},
                {"lemma": "el valle", "translation": "valley", "pos": "noun"},
                {"lemma": "sísmico", "translation": "seismic", "pos": "adjective"}
            ],
            "grammar_title": "Oraciones hendidas en la geografía física",
            "grammar_slug": "hendidas-geografia",
            "grammar_text1": "Al describir la geografía del Valle de México, las oraciones hendidas permiten aislar las causas geológicas determinantes: 'Lo que convirtió a este valle en un espacio singular fue su condición de cuenca endorreica, rodeada por un cinturón de volcanes activos'.",
            "grammar_table": [
                ["Lo que define la cuenca...", "Es la ausencia de una salida natural de agua hacia el mar."],
                ["Fue en el lecho arcilloso...", "Donde se levantaron las primeras cimentaciones coloniales."],
                ["Lo que agrava el hundimiento...", "Es la sobreexplotación intensiva de los mantos acuíferos."]
            ],
            "grammar_examples": [
                {"spanish": "Lo que asombra a los geólogos es la velocidad del hundimiento del suelo en el centro histórico.", "english": "What astonishes geologists is the speed of soil subsidence in the historic center."},
                {"spanish": "Fue precisamente la desecación sistemática de los cinco lagos lo que transformó el microclima del valle.", "english": "It was precisely the systematic desiccation of the five lakes that transformed the valley's microclimate."}
            ],
            "grammar_tip": "Recuerda que en el registro formal escrito, cuando el elemento enfocado por 'ser' es plural, la concordancia en plural es preferida: 'Lo que explica la vulnerabilidad sísmica son los antiguos sedimentos lacustres'.",
            "teaches_gr": "oraciones-hendidas-enfasis",
            "paragraphs": [
                {"type": "narration", "text": "Rodeado por las cumbres nevadas del Popocatépetl y el Iztaccíhuatl, el Valle de México se extiende a más de dos mil doscientos metros sobre el nivel del mar como una cuenca cerrada y endorreica. Durante milenios, las aguas pluviales descendían de las sierras para formar un sistema interconectado de cinco lagos someros: Zumpango, Xaltocan, Texcoco, Xochimilco y Chalco. Lo que convirtió a esta altiplanicie en un imán civilizatorio fue su extraordinaria riqueza biológica y microclimática."},
                {"type": "narration", "text": "El agua de los lagos meridionales era dulce, mientras que la del lago central de Texcoco se caracterizaba por su elevada salinidad debido a la evaporación continua sin salida fluvial. Para habitar este ecosistema lacustre sin sucumbir a las inundaciones periódicas, las civilizaciones originarias tuvieron que desarrollar una hidráulica de asombrosa precisión, con diques separadores y calzadas elevadas."},
                {"type": "narration", "text": "Tras la conquista española de 1521, la visión colonial optó por desecar los lagos en lugar de convivir con el agua. El Tajo de Nochistongo y, siglos más tarde, el Gran Canal del Desagüe vaciaron paulatinamente los vasos reguladores naturales. Lo que alguna vez fue un archipiélago lacustre de canoas y chinampas se convirtió en una inmensa llanura de polvo salitroso y arcilla seca."},
                {"type": "narration", "text": "Sobre ese lecho de lodo y cenizas volcánicas se levanta hoy una de las mayores aglomeraciones urbanas del planeta. La extracción incesante de agua potable de los acuíferos subterráneos ha provocado un fenómeno geológico crítico: el hundimiento diferencial del suelo, que en ciertas zonas de la ciudad supera los cuarenta centímetros al año."},
                {"type": "narration", "text": "Asimismo, las características físicas del subsuelo arcilloso actúan como una caja de resonancia acústica que amplifica las ondas sísmicas procedentes de la costa del Pacífico. Comprender la geología lacustre del Valle de México no es solo un ejercicio histórico, sino una necesidad vital para la sustentabilidad futura de más de veinte millones de habitantes."}
            ]
        },
        {
            "num": 2,
            "title": "Tenochtitlan y el choque colonial",
            "goal": "Analyze the urban planning of Mexico-Tenochtitlan, the hydraulic engineering of Nezahualcóyotl, and the 1521 colonial conquest.",
            "seg_slug": "tenochtitlan",
            "story_title": "Tenochtitlan: La fundación en el agua",
            "story_summary": "Historia de la fundación mexica en 1325, las calzadas monumentales, el albarradón de Nezahualcóyotl y el asedio militar de 1521.",
            "words": [
                {"lemma": "la calzada", "translation": "causeway", "pos": "noun"},
                {"lemma": "el acueducto", "translation": "aqueduct", "pos": "noun"},
                {"lemma": "la chinampa", "translation": "chinampa, floating garden", "pos": "noun"},
                {"lemma": "el palimpsesto", "translation": "palimpsest", "pos": "noun"},
                {"lemma": "el tributo", "translation": "tribute", "pos": "noun"},
                {"lemma": "el saqueo", "translation": "looting, sack", "pos": "noun"},
                {"lemma": "el islote", "translation": "islet", "pos": "noun"},
                {"lemma": "el teocalli", "translation": "pyramid temple", "pos": "noun"}
            ],
            "grammar_title": "Anteposición enfática en la historiografía",
            "grammar_slug": "inversion-historiografia",
            "grammar_text1": "La anteposición enfática del predicado o de complementos circunstanciales es un rasgo estilístico prominente en la crónica histórica: 'Magna fue la obra del albarradón diseñado por Nezahualcóyotl para proteger la capital mexica'.",
            "grammar_table": [
                ["Incomparable fue el asombro...", "De los soldados españoles al divisar las torres blancas sobre el lago."],
                ["En aquel islote pantanoso...", "Fundaron los mexicas el centro de un imperio continental."],
                ["Cruenta y prolongada resultó...", "La resistencia de los defensores de Tlatelolco en 1521."]
            ],
            "grammar_examples": [
                {"spanish": "Extraordinaria resultó la ingeniería hidráulica de las chinampas para alimentar a trescientos mil habitantes.", "english": "Extraordinary proved to be the hydraulic engineering of the chinampas in feeding three hundred thousand inhabitants."},
                {"spanish": "Bajo las piedras de la catedral metropolitana yacen los restos del Templo Mayor azteca.", "english": "Beneath the stones of the metropolitan cathedral lie the remains of the Aztec Templo Mayor."}
            ],
            "grammar_tip": "Al invertir el verbo y el sujeto, asegúrate de mantener la concordancia de número entre el verbo y el sujeto pospuesto: 'Innumerables fueron las bajas sufridas durante el asedio'.",
            "teaches_gr": "inversion-enfasis-fronting",
            "paragraphs": [
                {"type": "narration", "text": "Hacia 1325, una tribu migrante del norte conocida como los mexicas encontró sobre un islote del lago de Texcoco la señal prometida por sus deidades: un águila posada sobre un nopal devorando una serpiente. En ese espacio inhóspito y pantanoso comenzó la edificación de México-Tenochtitlan, una urbe que en dos siglos se convertiría en el corazón político y ceremonial de Mesoamérica."},
                {"type": "narration", "text": "Para conectar la isla con tierra firme, los ingenieros mexicas construyeron tres calzadas monumentales de piedra y madera: Tepeyac al norte, Tlacopan al poniente e Iztapalapa al sur, dotadas de puentes levadizos defensivos. El agua potable llegaba desde los manantiales de Chapultepec mediante un acueducto de doble cañería que permitía limpiar un conducto mientras el otro permanecía en servicio continuo."},
                {"type": "narration", "text": "Magna resultó la obra del albarradón de Nezahualcóyotl, una represa de más de doce kilómetros construida a mediados del siglo quince para separar las aguas saladas de Texcoco de las dulces de México, evitando inundaciones devastadoras y garantizando la viabilidad de la agricultura chinampera en las riberas."},
                {"type": "narration", "text": "En noviembre de 1519, las tropas castellanas de Hernán Cortés y sus aliados indígenas tlaxcaltecas penetraron por la calzada sur. Bernal Díaz del Castillo anotó en su crónica que la visión de los teocallis reflejados en el agua parecía un encantamiento sacado del libro de Amadís de Gaula. El asombro inicial dio paso pronto al conflicto bélico."},
                {"type": "narration", "text": "Tras meses de un asedio naval implacable con bergantines construidos en la orilla del lago, Tenochtitlan cayó el 13 de agosto de 1521. Sobre los escombros de los templos mexicas, los conquistadores erigieron palacios barrocos y conventos franciscanos, creando el palimpsesto urbano que define hasta hoy el Centro Histórico de la Ciudad de México."}
            ]
        },
        {
            "num": 3,
            "title": "La sociedad novohispana y el mestizaje barroco",
            "goal": "Examine the colonial social order of New Spain, baroque syncretism, and the intellectual legacy of Sor Juana Inés de la Cruz.",
            "seg_slug": "virreinato",
            "story_title": "La corte virreinal y la pluma de Sor Juana",
            "story_summary": "La vida cultural de la capital de Nueva España en el siglo XVII, el sistema de castas y la defensa del saber femenino en el convento de San Jerónimo.",
            "words": [
                {"lemma": "el mestizaje", "translation": "cultural and ethnic blending", "pos": "noun"},
                {"lemma": "el convento", "translation": "convent", "pos": "noun"},
                {"lemma": "el virreinato", "translation": "viceroyalty", "pos": "noun"},
                {"lemma": "el claustro", "translation": "cloister", "pos": "noun"},
                {"lemma": "el retablo", "translation": "altarpiece", "pos": "noun"},
                {"lemma": "la casta", "translation": "caste", "pos": "noun"},
                {"lemma": "la imprenta", "translation": "printing press", "pos": "noun"},
                {"lemma": "la opulencia", "translation": "opulence", "pos": "noun"}
            ],
            "grammar_title": "Adverbios de matiz en la crítica cultural",
            "grammar_slug": "adverbios-critica-cultural",
            "grammar_text1": "Al evaluar la complejidad social novohispana, los adverbios de precisión discursiva evitan simplificaciones anacrónicas: 'En rigor, el barroco novohispano no fue una mera copia del modelo peninsular, sino un lenguaje artístico profundamente sincrético'.",
            "grammar_table": [
                ["Propiamente dicho", "No era una sociedad homogénea, sino un complejo mosaico de fueros y privilegios."],
                ["Indudablemente", "Sor Juana representa la cumbre del pensamiento humanista del siglo XVII americano."],
                ["Francamente", "Las restricciones eclesiásticas limitaban severamente el acceso femenino a los estudios universitarios."]
            ],
            "grammar_examples": [
                {"spanish": "En rigor, las pinturas de castas reflejan más las ansiedades clasificatorias de las élites que la realidad fluida de la calle.", "english": "Strictly speaking, the casta paintings reflect the elite's classificatory anxieties more than the fluid reality of the street."},
                {"spanish": "Sor Juana defendió rotundamente el derecho de las mujeres al conocimiento científico y teológico.", "english": "Sor Juana categorically defended the right of women to scientific and theological knowledge."}
            ],
            "grammar_tip": "Coloca comas antes y después de locuciones como 'en rigor' o 'a nuestro juicio' para conferir pausas reflexivas a tu argumentación escrita.",
            "teaches_gr": "adverbios-intensificadores",
            "paragraphs": [
                {"type": "narration", "text": "Durante los tres siglos de dominación virreinal, la Ciudad de México fungió como la metrópoli más opulenta y cosmopolita del continente americano. Sede del virrey, del arzobispado, de la Real y Pontificia Universidad y de la primera imprenta de América, la urbe centralizaba el comercio transoceánico que enlazaba las sedas y porcelanas de Manila con la plata de Zacatecas y los puertos europeos."},
                {"type": "narration", "text": "En ese escenario de contrastes estridentes, la sociedad se estratificaba mediante un rígido sistema de castas que pretendía codificar el mestizaje biológico entre españoles, indígenas y africanos esclavizados. Sin embargo, en la práctica cotidiana de los mercados y las fiestas patronales, las fronteras étnicas se desdibujaban continuamente al ritmo de la música popular y la cocina criolla."},
                {"type": "narration", "text": "En el corazón de esa ciudad barroca floreció la figura intelectual más deslumbrante de la época: Sor Juana Inés de la Cruz. Nacida en Nepantla y autodidacta desde su infancia, ingresó en 1669 en el convento de San Jerónimo, no por vocación religiosa estricta, sino para disponer de silencio, biblioteca y libertad para el estudio sistemático."},
                {"type": "narration", "text": "En su célebre celda conventual, rodeada de instrumentos astronómicos y volúmenes de matemáticas y filosofía, Sor Juana compuso villancicos polifónicos, comedias teatrales y su poema cumbre, 'Primero sueño'. En rigor, su Respuesta a Sor Filotea de la Cruz constituye el primer manifiesto razonado en defensa del derecho universal de las mujeres a la educación superior en lengua castellana."},
                {"type": "narration", "text": "El barroco novohispano alcanzó en la arquitectura de templos y colegios jesuitas una suntuosidad desbordante. El dorado de los retablos churriguerescos y el uso del tezontle volcánico y la cantera chiluca plasmaron en piedra la identidad de una élite criolla que comenzaba a sentirse distinta y soberana frente a la corona española."}
            ]
        },
        {
            "num": 4,
            "title": "El muralismo y la revolución cultural",
            "goal": "Evaluate the 20th-century Mexican Muralist movement (Rivera, Orozco, Siqueiros) as a post-revolutionary civic education project.",
            "seg_slug": "muralismo",
            "story_title": "Muros que educan al pueblo",
            "story_summary": "El proyecto educativo de José Vasconcelos tras la Revolución Mexicana, los andamios del Palacio Nacional y la pintura mural como discurso cívico.",
            "words": [
                {"lemma": "el muralismo", "translation": "muralism", "pos": "noun"},
                {"lemma": "la vanguardia", "translation": "avant-garde", "pos": "noun"},
                {"lemma": "el mecenazgo", "translation": "patronage", "pos": "noun"},
                {"lemma": "el andamio", "translation": "scaffold", "pos": "noun"},
                {"lemma": "el lienzo", "translation": "canvas", "pos": "noun"},
                {"lemma": "la reivindicación", "translation": "vindication, social claim", "pos": "noun"},
                {"lemma": "el fresco", "translation": "fresco", "pos": "noun"},
                {"lemma": "la cosmovisión", "translation": "worldview", "pos": "noun"}
            ],
            "grammar_title": "Foco contrastivo con no... sino en el análisis artístico",
            "grammar_slug": "contraste-muralismo",
            "grammar_text1": "El arte muralista postrevolucionario se prestaba expresamente a la contraposición ideológica: 'El arte de Diego Rivera no buscaba decorar salones aristocráticos privados, sino educar a las masas populares en los muros públicos'.",
            "grammar_table": [
                ["No fue un movimiento burgués...", "Sino una revolución estética al servicio de los trabajadores."],
                ["No pintaban en caballete...", "Sino directamente al fresco sobre los muros del Estado."],
                ["No ocultaban las contradicciones...", "Sino que denunciaban abiertamente la opresión del campesinado."]
            ],
            "grammar_examples": [
                {"spanish": "El objetivo de los muralistas no era complacer al mercado comercial, sino forjar una memoria visual compartida.", "english": "The objective of the muralists was not to please the commercial market, but to forge a shared visual memory."},
                {"spanish": "No pintaron alegorías mitológicas europeas, sino las luchas concretas de Zapata y los obreros fabriles.", "english": "They did not paint European mythological allegories, but the concrete struggles of Zapata and factory workers."}
            ],
            "grammar_tip": "Emplea 'sino que' cuando el segundo miembro de la antítesis contenga un verbo en forma personal conjugada: 'No se limitó a pintar figuras, sino que investigó a fondo las técnicas prehispánicas del estuco'.",
            "teaches_gr": "enfasis-contrastivo-sino",
            "paragraphs": [
                {"type": "narration", "text": "Al concluir la fase armada de la Revolución Mexicana en 1920, el país emergía devastado pero con una urgente voluntad de refundación nacional. En 1921, el recién creado Ministerio de Educación Pública, bajo el liderazgo del intelectual José Vasconcelos, convocó a los artistas jóvenes más talentosos para emprender una cruzada pedagógica sin precedentes: llevar el arte de los museos privados a los muros públicos de la nación."},
                {"type": "narration", "text": "Diego Rivera, José Clemente Orozco y David Alfaro Siqueiros —los llamados 'tres grandes'— abandonaron los lienzos de caballete para subirse a los andamios del Antiguo Colegio de San Ildefonso, la Escuela Nacional Preparatoria y el Palacio Nacional. Su propósito no era adornar recintos oficiales, sino ilustrar la historia mexicana para un pueblo mayoritariamente analfabeto mediante un lenguaje plástico monumental."},
                {"type": "narration", "text": "Rivera concibió en la gran escalinata del Palacio Nacional una épica visual que abarca desde la civilización tolteca y el mercado de Tlatelolco hasta las huelgas proletarias del siglo veinte. Su técnica del fresco recuperaba recetas renacentistas aplicadas a pigmentos y temas puramente americanos, donde la dignidad de los pueblos originarios ocupaba el primer plano."},
                {"type": "narration", "text": "En contraste con la visión armónica e indigenista de Rivera, José Clemente Orozco plasmó una mirada trágica y descarnada sobre la violencia revolucionaria, visible en los muros desgarradores del Hospicio Cabañas y San Ildefonso. Siqueiros, por su parte, experimentó con polímeros industriales, piroxilina y perspectivas cinéticas dinámicas que transformaban al espectador en un participante activo."},
                {"type": "narration", "text": "Junto a ellos, Frida Kahlo creó paralelamente una obra introspectiva y visceral que dialogaba con el arte popular, el traje tradicional tehuano y el dolor físico. El movimiento muralista mexicano demostró al mundo que la vanguardia estética del siglo veinte no emanaba únicamente de París o Nueva York, sino también de la apasionada reinterpretación de las raíces latinoamericanas."}
            ]
        },
        {
            "num": 5,
            "title": "La capital contemporánea: Democracia, sismos y ciudadanía activa",
            "goal": "Examine the political and civic evolution of contemporary Mexico City through the lens of 1968, the 1985 earthquake, and modern autonomy.",
            "seg_slug": "capitalmoderna",
            "story_title": "El despertar cívico de la gran metrópolis",
            "story_summary": "La masacre estudiantil de Tlatelolco en 1968, la solidaridad ciudadana tras el terremoto de 1985 y la conquista de la autonomía democrática en la CDMX.",
            "words": [
                {"lemma": "el sismo", "translation": "earthquake", "pos": "noun"},
                {"lemma": "el damnificado", "translation": "victim, affected person", "pos": "noun"},
                {"lemma": "la brigada", "translation": "brigade, rescue team", "pos": "noun"},
                {"lemma": "la urbe", "translation": "metropolis, city", "pos": "noun"},
                {"lemma": "la autogestión", "translation": "self-management", "pos": "noun"},
                {"lemma": "la movilización", "translation": "mobilization", "pos": "noun"},
                {"lemma": "el escombro", "translation": "rubble, debris", "pos": "noun"},
                {"lemma": "la solidaridad", "translation": "solidarity", "pos": "noun"}
            ],
            "grammar_title": "Integración de recursos de énfasis en el análisis sociopolítico",
            "grammar_slug": "sintesis-politica-cdmx",
            "grammar_text1": "El análisis de la transición democrática en la Ciudad de México exige articular relieve y matiz: 'Lo que catalizó el despertar cívico no fue una concesión gubernamental, sino la autoorganización de los vecinos frente a los escombros de 1985'.",
            "grammar_table": [
                ["Oración hendida", "Lo que transformó la conciencia urbana fue la respuesta de los brigadistas voluntarios."],
                ["Inversión enfática", "Determinante resultó la movilización estudiantil del 68 para la apertura democrática."],
                ["Foco contrastivo", "No esperaron las órdenes del ejército, sino que rescataron a sus vecinos con sus propias manos."]
            ],
            "grammar_examples": [
                {"spanish": "Fue precisamente en Tlatelolco donde se fracturó el discurso oficial de estabilidad autoritaria.", "english": "It was precisely in Tlatelolco where the official discourse of authoritarian stability fractured."},
                {"spanish": "Lo que conquistó la ciudadanía en 1997 fue el derecho histórico a elegir democráticamente a su propio gobernante.", "english": "What the citizenry won in 1997 was the historic right to democratically elect their own governor."}
            ],
            "grammar_tip": "Al redactar conclusiones sociopolíticas, emplea oraciones hendidas para jerarquizar el factor más determinante antes de enumerar causas accesorias.",
            "teaches_gr": "oraciones-hendidas-enfasis",
            "paragraphs": [
                {"type": "narration", "text": "El 2 de octubre de 1968 marcó un antes y un después en la biografía cívica de México. En la Plaza de las Tres Culturas de Tlatelolco, la represión violenta de una multitud pacífica de estudiantes, profesores y obreros derribó el mito de la paz autoritaria promovido por el régimen del partido hegemónico ante los inminentes Juegos Olímpicos. Aquella herida abierta inauguró décadas de exigencia democrática."},
                {"type": "narration", "text": "Diecisiete años después, la mañana del 19 de septiembre de 1985, un devastador sismo de magnitud 8.1 sacudió los cimientos del Valle de México. Cientos de edificios de oficinas, hospitales y conjuntos multifamiliares en colonias como Tlatelolco, Roma y Doctores se desplomaron en cuestión de minutos sobre el subsuelo arcilloso."},
                {"type": "narration", "text": "Ante la parálisis inicial de las autoridades gubernamentales, que tardaron días en calibrar la magnitud del desastre, miles de jóvenes, trabajadores y amas de casa formaron brigadas ciudadanas espontáneas. Con palas, picos y sus propias manos, la población civil removió escombros para rescatar a personas atrapadas y organizar comedores populares y albergues."},
                {"type": "narration", "text": "Los cronistas como Carlos Monsiváis señalaron que en los escombros de 1985 nació la sociedad civil contemporánea mexicana. De aquella solidaridad barrial surgieron organizaciones comunitarias de damnificados y movimientos vecinales que aprendieron a negociar directamente con el poder y a demandar transparencia y vivienda digna."},
                {"type": "narration", "text": "Esa maduración cívica culminó en 1997, cuando los habitantes de la capital votaron por primera vez a su Jefe de Gobierno, rompiendo el control presidencial directo. En 2016, la reforma constitucional transformó al Distrito Federal en la Ciudad de México (CDMX), dotándola de una constitución vanguardista que consagra libertades civiles, derechos ambientales y una vocación democrática inquebrantable."}
            ]
        }
    ]

    all_story_paragraphs = []

    # Generate the 5 lessons
    for les in lessons_meta:
        l_num = les["num"]
        stem = f"b2-mexicocentro-{l_num:02d}"
        story_rel = f"stories/world/b2/{stem}.json"

        # Story file
        story_data = {
            "id": f"story.b2.mexicocentro.{l_num:02d}",
            "title": les["story_title"],
            "level": "B2",
            "lesson": l_num,
            "type": "world",
            "estimatedMinutes": 5,
            "summary": les["story_summary"],
            "characters": [],
            "paragraphs": les["paragraphs"]
        }
        write_json(f"stories/world/b2/{stem}.json", story_data)
        all_story_paragraphs.extend(les["paragraphs"])

        # Vocabulary file
        write_json(f"vocabulary/b2/{stem}-voc.json", {
            "id": f"vocab.b2.mexicocentro.{l_num:02d}",
            "lesson": stem,
            "title": f"{les['title']} - Vocabulario",
            "theme": "México: Centro y Valle de Anáhuac",
            "words": les["words"]
        })

        # Grammar file
        write_json(f"grammar/b2/{stem}-a-gr.json", {
            "id": f"grammar.b2.mexicocentro.{l_num:02d}.{les['grammar_slug']}",
            "title": les["grammar_title"],
            "sections": [
                {"type": "text", "title": "¿Cómo funciona en el contexto regional?", "content": les["grammar_text1"]},
                {"type": "table", "title": "Modelos sintácticos", "rows": les["grammar_table"]},
                {"type": "examples", "title": "Ejemplos en el texto histórico", "items": les["grammar_examples"]},
                {"type": "tip", "content": les["grammar_tip"]}
            ]
        })

        # Exercise file
        ex_list = [
            {
                "id": f"{stem}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    [les["words"][0]["lemma"], les["words"][0]["translation"]],
                    [les["words"][1]["lemma"], les["words"][1]["translation"]],
                    [les["words"][2]["lemma"], les["words"][2]["translation"]],
                    [les["words"][3]["lemma"], les["words"][3]["translation"]]
                ],
                "teaches": ["b2-mexicocentro-vocab"]
            },
            {
                "id": f"{stem}.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": f"Según el texto de esta lección, ¿cuál es la idea central de '{les['story_title']}'?",
                "options": [
                    les["story_summary"].split(".")[0] + ".",
                    "La región no contaba con ningún asentamiento humano relevante.",
                    "El clima árido impidió el desarrollo de cualquier tecnología o arte."
                ],
                "correct": 0
            },
            {
                "id": f"{stem}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": les["grammar_examples"][0]["spanish"].replace(les["grammar_examples"][0]["spanish"].split()[1], "____", 1),
                "answer": les["grammar_examples"][0]["spanish"].split()[1],
                "english": les["grammar_examples"][0]["english"],
                "teaches": [les["teaches_gr"]]
            },
            {
                "id": f"{stem}.ex04",
                "type": "multiple-choice",
                "category": "reading",
                "question": f"¿Qué aspecto destaca el texto respecto a la historia de '{les['title']}'?",
                "options": [
                    les["paragraphs"][1]["text"][:120] + "...",
                    "La ciudad fue abandonada completamente tras pocos años de fundación.",
                    "No existen fuentes escritas ni arqueológicas sobre este período."
                ],
                "correct": 0
            },
            {
                "id": f"{stem}.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": les["grammar_examples"][1]["spanish"].split(),
                "solution": les["grammar_examples"][1]["spanish"].split(),
                "english": les["grammar_examples"][1]["english"],
                "teaches": [les["teaches_gr"]]
            },
            {
                "id": f"{stem}.ex06",
                "type": "listening-choice",
                "category": "listening",
                "sentence": les["paragraphs"][0]["text"][:140] + ".",
                "options": [
                    les["story_summary"][:100] + "...",
                    "The text describes a completely uninhabited and barren desert landscape.",
                    "The region was solely established as a temporary trading outpost."
                ],
                "correct": 0,
                "teaches": [les["teaches_gr"]]
            },
            {
                "id": f"{stem}.ex07",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Estudiante", "text": f"¿Qué aprendiste sobre {les['title']}?"},
                    {"speaker": "Tú", "text": "_____"},
                    {"speaker": "Estudiante", "text": "Es fascinante ver cómo la historia modela el presente de la ciudad."}
                ],
                "options": [
                    les["grammar_examples"][0]["spanish"],
                    "No recuerdo ningún detalle relevante sobre el tema.",
                    "Ayer fuimos a comprar billetes para el tren en la estación central."
                ],
                "correct": 0,
                "teaches": [les["teaches_gr"]]
            },
            {
                "id": f"{stem}.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": f"Write an analytical summary sentence about {les['title']} using the grammar taught", "answer": les["grammar_examples"][1]["spanish"]}
                ],
                "teaches": [les["teaches_gr"], "b2-mexicocentro-vocab"]
            }
        ]
        write_json(f"exercises/b2/{stem}-ex.json", {
            "lesson": stem,
            "exercises": ex_list
        })

        # Lesson file
        sections = []
        if l_num == 1:
            sections.append({
                "type": "intro",
                "title": "Welcome to Latin American Regional Studies",
                "body": [
                    "Welcome to the B2 Latin American Regional Studies track. This 36-unit upper-intermediate course takes you on an immersive journey across every country and territory of Latin America and the South American continent.",
                    "Taught entirely in Spanish, each unit examines a country's physical geography, founding historical narratives, social and indigenous fabric, artistic revolutions, and modern political economy. Larger powers like Mexico, Brazil, and Argentina receive multiple in-depth units, alongside comprehensive coverage of Central America, the Caribbean, the Andes, the Southern Cone, and neighboring frontier enclaves.",
                    "Every lesson is anchored in an authentic narrative text, integrated with B2 vocabulary and the corresponding grammar point from Core Spanish. We begin in the heart of Mesoamerica: Mexico City and the sacred Valley of Anáhuac."
                ]
            })

        sections.extend([
            {
                "type": "goal",
                "items": [
                    les["goal"],
                    f"Master 8 key vocabulary terms relating to {les['title'].lower()}.",
                    f"Apply {les['grammar_title'].lower()} in analytical discourse.",
                    "Analyze authentic regional readings with B2 reading comprehension."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": story_rel},
            {"type": "vocabulary", "ref": f"vocabulary/b2/{stem}-voc.json"},
            {"type": "grammar", "ref": f"grammar/b2/{stem}-a-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": f"exercises/b2/{stem}-ex.json",
                "exerciseRefs": [f"{stem}.ex01", f"{stem}.ex02", f"{stem}.ex03", f"{stem}.ex04", f"{stem}.ex05"]
            },
            {
                "type": "exercise-group",
                "title": "Listening",
                "ref": f"exercises/b2/{stem}-ex.json",
                "exerciseRefs": [f"{stem}.ex06"]
            },
            {
                "type": "exercise-group",
                "title": "Dialogue",
                "ref": f"exercises/b2/{stem}-ex.json",
                "exerciseRefs": [f"{stem}.ex07"]
            },
            {
                "type": "exercise-group",
                "title": "Writing",
                "ref": f"exercises/b2/{stem}-ex.json",
                "exerciseRefs": [f"{stem}.ex08"]
            },
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    les["goal"],
                    f"Master 8 key vocabulary terms relating to {les['title'].lower()}.",
                    f"Apply {les['grammar_title'].lower()} in analytical discourse.",
                    "Analyze authentic regional readings with B2 reading comprehension."
                ]
            }
        ])

        write_json(f"lessons/b2/{stem}.json", {
            "id": f"lesson.b2.mexicocentro.{l_num:02d}",
            "title": les["title"],
            "level": "B2",
            "goal": les["goal"],
            "grammar": les["grammar_title"].lower(),
            "sections": sections
        })

    # Consolidated Unit Story: stories/world/b2/b2-mexicocentro.json
    write_json("stories/world/b2/b2-mexicocentro.json", {
        "id": "story.b2.mexicocentro",
        "title": "Mexico I: Central Mexico & the Valley of Anáhuac",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 10,
        "characters": [],
        "source": "Estudios regionales latinoamericanos: síntesis histórica y geográfica del Valle de México",
        "paragraphs": all_story_paragraphs
    })

    # Consolidation Lesson: b2-mexicocentro-consolidation
    c_stem = "b2-mexicocentro-consolidation"
    write_json(f"exercises/b2/{c_stem}-ex.json", {
        "lesson": c_stem,
        "exercises": [
            {
                "id": "b2-mexicocentro-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la cuenca", "basin"],
                    ["la chinampa", "floating garden"],
                    ["el claustro", "cloister"],
                    ["el muralismo", "muralism"]
                ],
                "teaches": ["b2-mexicocentro-vocab"]
            },
            {
                "id": "b2-mexicocentro-consolidation.ex02",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el hundimiento", "subsidence, sinking"],
                    ["el palimpsesto", "palimpsest"],
                    ["el retablo", "altarpiece"],
                    ["el sismo", "earthquake"]
                ],
                "teaches": ["b2-mexicocentro-vocab"]
            },
            {
                "id": "b2-mexicocentro-consolidation.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Por qué se describe a la Ciudad de México como un 'palimpsesto urbano'?",
                "options": [
                    "Porque sus estructuras coloniales y modernas fueron edificadas directamente sobre las ruinas prehispánicas.",
                    "Porque fue trazada según un plano urbanístico completamente homogéneo en el siglo diecinueve.",
                    "Porque carece de cualquier testimonio monumental de épocas previas a la industrialización."
                ],
                "correct": 0
            },
            {
                "id": "b2-mexicocentro-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Lo que definió la resistencia en Tlatelolco __ la determinación de no ceder ante el asedio. (ser)",
                "answer": "fue",
                "english": "What defined the resistance in Tlatelolco was the determination not to yield to the siege.",
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-mexicocentro-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Decisiva", "fue", "la", "participación", "ciudadana", "tras", "el", "sismo", "de", "1985."],
                "solution": ["Decisiva", "fue", "la", "participación", "ciudadana", "tras", "el", "sismo", "de", "1985."],
                "english": "Decisive was the citizen participation after the 1985 earthquake.",
                "teaches": ["inversion-enfasis-fronting"]
            },
            {
                "id": "b2-mexicocentro-consolidation.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los muralistas no pretendían aislarse en estudios cerrados, __ salir a las calles y plazas públicas. (sino)",
                "answer": "sino",
                "english": "The muralists did not intend to isolate themselves in closed studios, but to go out to the streets and public squares.",
                "teaches": ["enfasis-contrastivo-sino"]
            },
            {
                "id": "b2-mexicocentro-consolidation.ex07",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Profesor", "text": "¿Cómo resumirías la trayectoria cívica de la Ciudad de México en el siglo veinte?"},
                    {"speaker": "Tú", "text": "_____"},
                    {"speaker": "Profesor", "text": "Exactamente, esa fue la base que transformó a la capital en un bastión de libertades."}
                ],
                "options": [
                    "Lo que catalizó la democracia moderna no fue una dádiva del poder, sino la movilización comunitaria.",
                    "La ciudad creció mucho en habitantes pero la gente no se interesaba por los temas cívicos.",
                    "El metro de la ciudad se construyó en varias líneas subterráneas en la década del setenta."
                ],
                "correct": 0,
                "teaches": ["oraciones-hendidas-enfasis"]
            },
            {
                "id": "b2-mexicocentro-consolidation.ex08",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {"prompt": "Synthesize the importance of Mexican muralism using contrastive focus with 'sino que'", "answer": "El muralismo no solo decoró los muros oficiales, sino que forjó una identidad visual para el pueblo."},
                    {"prompt": "State the ongoing environmental challenge of the valley using a cleft sentence", "answer": "Lo que más preocupa a los ingenieros es el hundimiento continuo por la extracción de agua."}
                ],
                "teaches": ["enfasis-contrastivo-sino", "oraciones-hendidas-enfasis", "b2-mexicocentro-vocab"]
            }
        ]
    })

    write_json(f"lessons/b2/{c_stem}.json", {
        "id": "lesson.b2.mexicocentro.consolidation",
        "title": "Unit 1 Consolidation",
        "level": "B2",
        "goal": "Consolidate knowledge of Central Mexican geography, Mesoamerican foundations, colonial New Spain, muralism, and civic resilience.",
        "grammar": "síntesis de estudios regionales",
        "sections": [
            {
                "type": "goal",
                "items": [
                    "Consolidate geographic, historical, and cultural insights on the Valley of Mexico.",
                    "Review 40 key vocabulary terms spanning lacustrine geography, colonial institutions, and public art.",
                    "Apply rhetorical emphasis and contrastive focus to historical case studies.",
                    "Synthesize the civic trajectory of contemporary Mexico City."
                ]
            },
            {"type": "recycle", "count": 3},
            {
                "type": "exercise-group",
                "title": "Review",
                "ref": f"exercises/b2/{c_stem}-ex.json",
                "exerciseRefs": [
                    "b2-mexicocentro-consolidation.ex01",
                    "b2-mexicocentro-consolidation.ex02",
                    "b2-mexicocentro-consolidation.ex03",
                    "b2-mexicocentro-consolidation.ex04",
                    "b2-mexicocentro-consolidation.ex05",
                    "b2-mexicocentro-consolidation.ex06",
                    "b2-mexicocentro-consolidation.ex07",
                    "b2-mexicocentro-consolidation.ex08"
                ]
            },
            {
                "type": "checklist",
                "items": [
                    "I can consolidate geographic, historical, and cultural insights on the Valley of Mexico.",
                    "I can review 40 key vocabulary terms spanning lacustrine geography, colonial institutions, and public art.",
                    "I can apply rhetorical emphasis and contrastive focus to historical case studies.",
                    "I can synthesize the civic trajectory of contemporary Mexico City."
                ]
            }
        ]
    })
    print("Generated LatAm Regional Studies B2 Unit 1 successfully.")


# ==============================================================================
# 3. UPDATE REGISTRIES & UNIT TABLE
# ==============================================================================

def update_registries():
    # 1. skill-registry.json
    sr_path = BASE / "indexes" / "skill-registry.json"
    sr = json.loads(sr_path.read_text(encoding="utf-8"))
    skills = sr.setdefault("skills", {})

    new_skills = {
        "b2-unit01-vocab": {"kind": "vocabulary"},
        "b2-mexicocentro-vocab": {"kind": "vocabulary"},
        "oraciones-hendidas-enfasis": {"kind": "grammar"},
        "adverbios-intensificadores": {"kind": "grammar"},
        "inversion-enfasis-fronting": {"kind": "grammar"},
        "enfasis-contrastivo-sino": {"kind": "grammar"}
    }
    for k, v in new_skills.items():
        skills[k] = v
    sr_path.write_text(json.dumps(sr, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Updated skill-registry.json")

    # 2. grammar-titles.json
    gt_path = BASE / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))
    new_titles = {
        "b2-unit01-vocab": "reading",
        "b2-mexicocentro-vocab": "reading",
        "oraciones-hendidas-enfasis": "cleft sentences and focus constructions",
        "adverbios-intensificadores": "adverbial intensifiers and stance markers",
        "inversion-enfasis-fronting": "emphatic fronting and word order inversion",
        "enfasis-contrastivo-sino": "contrastive focus with no sino"
    }
    for k, v in new_titles.items():
        gt[k] = v
    gt_path.write_text(json.dumps(gt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json")

    # 3. curriculum/units/b2.json
    unit_table = [
        {
            "title": "Nuance, Precision & Emphasis",
            "stems": [
                "b2-01-01",
                "b2-01-02",
                "b2-01-03",
                "b2-01-04",
                "b2-01-05",
                "b2-01-consolidation"
            ],
            "track": "core"
        },
        {
            "title": "Mexico I: Central Mexico & the Valley of Anáhuac",
            "stems": [
                "b2-mexicocentro-01",
                "b2-mexicocentro-02",
                "b2-mexicocentro-03",
                "b2-mexicocentro-04",
                "b2-mexicocentro-05",
                "b2-mexicocentro-consolidation"
            ],
            "track": "latam"
        }
    ]
    u_path = BASE / "curriculum" / "units" / "b2.json"
    u_path.parent.mkdir(parents=True, exist_ok=True)
    u_path.write_text(json.dumps(unit_table, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Wrote curriculum/units/b2.json")


if __name__ == "__main__":
    update_registries()
    generate_core_unit_1()
    generate_latam_unit_1()
