#!/usr/bin/env python3
"""Generate Spain CCSE Units 3 & 4 (content/es-es, B1, track: cultura).

Unit 3: Las Cortes Generales: Congreso y Senado
Unit 4: El Gobierno y la Administración del Estado
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def write_json(rel_path: str, data: dict):
    target = ROOT / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {rel_path}")

def generate_unit_3():
    # Stems: b1-ccse-cortes-01 .. 05, b1-ccse-cortes-consolidation
    
    # 1. Lessons
    lessons_meta = [
        {
            "num": "01",
            "title": "El Congreso de los Diputados",
            "grammar": "Estructuras pasivas con 'se' y representación popular",
            "goal": "Conocer la composición, elección y funciones del Congreso de los Diputados.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-cortes-01-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-cortes-01-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-cortes-01-ex.json",
            "ex_refs": [
                "ex.b1.ccse.cortes.01.1",
                "ex.b1.ccse.cortes.01.2",
                "ex.b1.ccse.cortes.01.3"
            ]
        },
        {
            "num": "02",
            "title": "El Senado y la Representación Territorial",
            "grammar": "Conectores de contraste y adición institucional",
            "goal": "Aprender el papel del Senado como cámara de representación territorial.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-cortes-02-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-cortes-02-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-cortes-02-ex.json",
            "ex_refs": [
                "ex.b1.ccse.cortes.02.1",
                "ex.b1.ccse.cortes.02.2",
                "ex.b1.ccse.cortes.02.3"
            ]
        },
        {
            "num": "03",
            "title": "La Función Legislativa y el Control al Gobierno",
            "grammar": "Perífrasis de obligación y control parlamentario",
            "goal": "Comprender la potestad legislativa y los mecanismos de control al ejecutivo.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-cortes-03-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-cortes-03-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-cortes-03-ex.json",
            "ex_refs": [
                "ex.b1.ccse.cortes.03.1",
                "ex.b1.ccse.cortes.03.2",
                "ex.b1.ccse.cortes.03.3"
            ]
        },
        {
            "num": "04",
            "title": "Estatuto de los Parlamentarios: Inviolabilidad e Inmunidad",
            "grammar": "Expresiones de protección jurídica y excepción",
            "goal": "Estudiar las prerrogativas de los diputados y senadores en el ejercicio de su función.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-cortes-04-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-cortes-04-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-cortes-04-ex.json",
            "ex_refs": [
                "ex.b1.ccse.cortes.04.1",
                "ex.b1.ccse.cortes.04.2",
                "ex.b1.ccse.cortes.04.3"
            ]
        },
        {
            "num": "05",
            "title": "Elaboración de Leyes y Presupuestos Generales",
            "grammar": "Oraciones consecutivas y finales en el proceso legislativo",
            "goal": "Diferenciar entre proyectos y proposiciones de ley y conocer la tramitación de los PGE.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-cortes-05-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-cortes-05-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-cortes-05-ex.json",
            "ex_refs": [
                "ex.b1.ccse.cortes.05.1",
                "ex.b1.ccse.cortes.05.2",
                "ex.b1.ccse.cortes.05.3"
            ]
        }
    ]

    for lm in lessons_meta:
        n = lm["num"]
        stem = f"b1-ccse-cortes-{n}"
        lesson_data = {
            "id": f"lesson.b1.ccse.cortes.{n}",
            "level": "b1",
            "title": lm["title"],
            "grammar": lm["grammar"],
            "goal": lm["goal"],
            "track": "cultura",
            "metadata": {
                "estimatedMinutes": lm["minutes"]
            },
            "sections": [
                {
                    "type": "vocabulary",
                    "title": "Vocabulario Cívico",
                    "ref": lm["vocab_ref"]
                },
                {
                    "type": "grammar",
                    "title": lm["grammar"],
                    "ref": lm["grammar_ref"]
                },
                {
                    "type": "exercise-group",
                    "title": "Práctica y Preguntas CCSE",
                    "exerciseRefs": lm["ex_refs"],
                    "ref": lm["ex_ref"]
                }
            ]
        }
        write_json(f"content/es-es/lessons/b1/{stem}.json", lesson_data)

    # Consolidation Lesson
    write_json("content/es-es/lessons/b1/b1-ccse-cortes-consolidation.json", {
        "id": "lesson.b1.ccse.cortes.consolidation",
        "level": "b1",
        "title": "Las Cortes Generales: Congreso y Senado — Consolidación",
        "grammar": "Repaso CCSE: El Poder Legislativo y las Cortes Generales",
        "goal": "Consolidar los conocimientos sobre el Congreso, el Senado, la potestad legislativa y el control parlamentario.",
        "track": "cultura",
        "metadata": {
            "estimatedMinutes": 15
        },
        "sections": [
            {
                "type": "exercise-group",
                "title": "Simulacro CCSE: Las Cortes Generales",
                "exerciseRefs": [
                    "ex.b1.ccse.cortes.consolidation.1",
                    "ex.b1.ccse.cortes.consolidation.2",
                    "ex.b1.ccse.cortes.consolidation.3"
                ],
                "ref": "exercises/b1/b1-ccse-cortes-consolidation-ex.json"
            }
        ]
    })

    # 2. Vocabulary Files
    voc_data_list = [
        {
            "num": "01",
            "title": "El Congreso de los Diputados",
            "words": [
                {"lemma": "diputado", "translation": "member of parliament / deputy", "pos": "noun"},
                {"lemma": "escaño", "translation": "parliamentary seat", "pos": "noun"},
                {"lemma": "legislatura", "translation": "legislative term / legislature", "pos": "noun"},
                {"lemma": "sufragio", "translation": "suffrage / vote", "pos": "noun"},
                {"lemma": "mandato", "translation": "mandate / term of office", "pos": "noun"}
            ]
        },
        {
            "num": "02",
            "title": "El Senado y la Representación Territorial",
            "words": [
                {"lemma": "senador", "translation": "senator", "pos": "noun"},
                {"lemma": "cámara alta", "translation": "upper house", "pos": "expression"},
                {"lemma": "territorial", "translation": "territorial", "pos": "adjective"},
                {"lemma": "autonómico", "translation": "regional / autonomic", "pos": "adjective"},
                {"lemma": "veto", "translation": "veto", "pos": "noun"}
            ]
        },
        {
            "num": "03",
            "title": "La Función Legislativa y el Control al Gobierno",
            "words": [
                {"lemma": "control", "translation": "oversight / monitoring / control", "pos": "noun"},
                {"lemma": "sesión", "translation": "session / sitting", "pos": "noun"},
                {"lemma": "pleno", "translation": "plenary session", "pos": "noun"},
                {"lemma": "interpelación", "translation": "interpellation / formal parliamentary question", "pos": "noun"},
                {"lemma": "comisión", "translation": "parliamentary committee / commission", "pos": "noun"}
            ]
        },
        {
            "num": "04",
            "title": "Estatuto de los Parlamentarios",
            "words": [
                {"lemma": "inviolabilidad", "translation": "inviolability", "pos": "noun"},
                {"lemma": "inmunidad", "translation": "immunity", "pos": "noun"},
                {"lemma": "suplicatorio", "translation": "petition to waive parliamentary immunity", "pos": "noun"},
                {"lemma": "prerrogativa", "translation": "prerogative / parliamentary privilege", "pos": "noun"},
                {"lemma": "aforamiento", "translation": "legal immunity / trial before higher court", "pos": "noun"}
            ]
        },
        {
            "num": "05",
            "title": "Elaboración de Leyes y Presupuestos",
            "words": [
                {"lemma": "proyecto de ley", "translation": "government bill", "pos": "expression"},
                {"lemma": "proposición de ley", "translation": "parliamentary / private member's bill", "pos": "expression"},
                {"lemma": "enmienda", "translation": "amendment", "pos": "noun"},
                {"lemma": "presupuesto", "translation": "budget", "pos": "noun"},
                {"lemma": "promulgación", "translation": "promulgation / enactment", "pos": "noun"}
            ]
        }
    ]

    for vd in voc_data_list:
        n = vd["num"]
        stem = f"b1-ccse-cortes-{n}"
        write_json(f"content/es-es/vocabulary/b1/{stem}-voc.json", {
            "id": f"vocab.b1.ccse.cortes.{n}",
            "lesson": stem,
            "title": vd["title"],
            "words": vd["words"]
        })

    # 3. Grammar Files
    gr_data_list = [
        {
            "num": "01",
            "title": "Estructuras pasivas con 'se' y representación popular",
            "text": "En el lenguaje institucional español, la pasiva refleja con 'se' se utiliza frecuentemente para describir procesos electorales y composiciones de órganos sin personalizar la acción.",
            "examples": [
                {
                    "spanish": "Los diputados se eligen por sufragio universal, libre, igual, directo y secreto.",
                    "english": "Deputies are elected by universal, free, equal, direct and secret suffrage."
                },
                {
                    "spanish": "El Congreso se compone actualmente de 350 diputados.",
                    "english": "Congress currently consists of 350 deputies."
                }
            ],
            "tip": "Recuerda que la Constitución fija entre 300 y 400 diputados, pero la ley electoral (LOREG) establece el número actual en 350."
        },
        {
            "num": "02",
            "title": "Conectores de contraste y adición institucional",
            "text": "Para comparar las funciones y la composición de ambas Cámaras se emplean conectores como 'mientras que', 'a diferencia de' y 'asimismo'.",
            "examples": [
                {
                    "spanish": "El Congreso representa al pueblo, mientras que el Senado es la cámara de representación territorial.",
                    "english": "Congress represents the people, whereas the Senate is the chamber of territorial representation."
                },
                {
                    "spanish": "En cada provincia peninsular se eligen cuatro senadores; asimismo, las comunidades autónomas designan senadores adicionales.",
                    "english": "In each mainland province four senators are elected; likewise, autonomous communities designate additional senators."
                }
            ],
            "tip": "En el examen CCSE es esencial recordar la definición exacta del Senado: 'cámara de representación territorial'."
        },
        {
            "num": "03",
            "title": "Perífrasis de obligación y control parlamentario",
            "text": "El control al Gobierno se formula mediante perífrasis verbales como 'deber + infinitivo' y expresiones formales de fiscalización como 'someter a control'.",
            "examples": [
                {
                    "spanish": "El Gobierno debe responder a las preguntas que se le formulan en las Cámaras.",
                    "english": "The Government must answer the questions put to it in the Chambers."
                },
                {
                    "spanish": "Las Cortes Generales controlan la acción del poder ejecutivo.",
                    "english": "The Cortes Generales oversee the action of the executive power."
                }
            ],
            "tip": "El artículo 66 de la Constitución enumera las tres grandes funciones de las Cortes: potestad legislativa, aprobación de presupuestos y control al Gobierno."
        },
        {
            "num": "04",
            "title": "Expresiones de protección jurídica y excepción",
            "text": "Las prerrogativas parlamentarias regulan protecciones especiales utilizando conectores restrictivos como 'salvo en caso de' y 'sin previa autorización'.",
            "examples": [
                {
                    "spanish": "Los diputados y senadores no pueden ser detenidos salvo en caso de flagrante delito.",
                    "english": "Deputies and senators cannot be detained except in cases of flagrante delicto."
                },
                {
                    "spanish": "No podrán ser procesados sin la previa autorización de su respectiva Cámara.",
                    "english": "They may not be prosecuted without prior authorization from their respective Chamber."
                }
            ],
            "tip": "La solicitud formal que envía el Tribunal Supremo a la Cámara para procesar a un parlamentario se llama 'suplicatorio'."
        },
        {
            "num": "05",
            "title": "Oraciones consecutivas y finales en el proceso legislativo",
            "text": "El procedimiento legislativo describe las fases de tramitación con conectores de finalidad ('para que + subjuntivo') y consecuencia ('de modo que').",
            "examples": [
                {
                    "spanish": "El Gobierno presenta los proyectos de ley para que el Congreso los debata y apruebe.",
                    "english": "The Government submits bills so that Congress may debate and approve them."
                },
                {
                    "spanish": "Las leyes orgánicas exigen mayoría absoluta, de modo que requieren un amplio consenso parlamentario.",
                    "english": "Organic laws require an absolute majority, so that they require a broad parliamentary consensus."
                }
            ],
            "tip": "Diferencia CCSE clave: los 'proyectos de ley' los presenta el Gobierno; las 'proposiciones de ley' provienen del Congreso, Senado o iniciativa popular (500.000 firmas)."
        }
    ]

    for gd in gr_data_list:
        n = gd["num"]
        stem = f"b1-ccse-cortes-{n}"
        write_json(f"content/es-es/grammar/b1/{stem}-gr.json", {
            "id": f"grammar.b1.ccse.cortes.{n}",
            "title": gd["title"],
            "sections": [
                {
                    "type": "text",
                    "content": gd["text"]
                },
                {
                    "type": "examples",
                    "items": gd["examples"]
                },
                {
                    "type": "tip",
                    "content": gd["tip"]
                }
            ]
        })

    # 4. Exercises Files
    ex_data_list = [
        {
            "num": "01",
            "stem": "b1-ccse-cortes-01",
            "exercises": [
                {
                    "id": "ex.b1.ccse.cortes.01.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuántos diputados componen actualmente el Congreso de los Diputados en España?",
                    "options": [
                        "350",
                        "400",
                        "300"
                    ],
                    "correct": 0,
                    "teaches": ["cortes", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.01.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los diputados del Congreso son elegidos para un mandato de _____ años.",
                    "answer": "cuatro",
                    "english": "Deputies of Congress are elected for a term of four years.",
                    "teaches": ["cortes", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.01.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "Congress represents the Spanish people.",
                    "tiles": ["El", "Congreso", "representa", "al", "pueblo", "español."],
                    "solution": ["El", "Congreso", "representa", "al", "pueblo", "español."],
                    "teaches": ["cortes", "ccse"]
                }
            ]
        },
        {
            "num": "02",
            "stem": "b1-ccse-cortes-02",
            "exercises": [
                {
                    "id": "ex.b1.ccse.cortes.02.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cómo define la Constitución Española al Senado?",
                    "options": [
                        "Como la cámara de representación territorial",
                        "Como el órgano supremo del poder judicial",
                        "Como la cámara de representación municipal"
                    ],
                    "correct": 0,
                    "teaches": ["senado", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.02.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "En cada provincia peninsular se eligen _____ senadores.",
                    "answer": "cuatro",
                    "english": "In each peninsular province four senators are elected.",
                    "teaches": ["senado", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.02.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Senate is the upper house of parliament.",
                    "tiles": ["El", "Senado", "es", "la", "cámara", "alta."],
                    "solution": ["El", "Senado", "es", "la", "cámara", "alta."],
                    "teaches": ["senado", "ccse"]
                }
            ]
        },
        {
            "num": "03",
            "stem": "b1-ccse-cortes-03",
            "exercises": [
                {
                    "id": "ex.b1.ccse.cortes.03.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿A quién corresponde la potestad legislativa del Estado según la Constitución?",
                    "options": [
                        "A las Cortes Generales",
                        "Al Presidente del Gobierno",
                        "Al Tribunal Supremo"
                    ],
                    "correct": 0,
                    "teaches": ["cortes", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.03.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Las sesiones plenarias de las Cámaras son normalmente _____ salvo acuerdo en contrario.",
                    "answer": "públicas",
                    "english": "Plenary sessions of the Chambers are normally public unless otherwise agreed.",
                    "teaches": ["cortes", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.03.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "Parliament oversees the actions of the government.",
                    "tiles": ["Las", "Cortes", "controlan", "la", "acción", "del", "Gobierno."],
                    "solution": ["Las", "Cortes", "controlan", "la", "acción", "del", "Gobierno."],
                    "teaches": ["cortes", "ccse"]
                }
            ]
        },
        {
            "num": "04",
            "stem": "b1-ccse-cortes-04",
            "exercises": [
                {
                    "id": "ex.b1.ccse.cortes.04.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿En qué único supuesto puede ser detenido un diputado o senador sin autorización previa?",
                    "options": [
                        "En caso de flagrante delito",
                        "Por decisión de cualquier juez de instrucción",
                        "Por orden directa del Ministro del Interior"
                    ],
                    "correct": 0,
                    "teaches": ["inmunidad", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.04.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los parlamentarios gozan de _____ por las opiniones manifestadas en el ejercicio de sus funciones.",
                    "answer": "inviolabilidad",
                    "english": "Parliamentarians enjoy inviolability for opinions expressed in the performance of their duties.",
                    "teaches": ["inviolabilidad", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.04.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "A suplicatorio is required to prosecute a deputy.",
                    "tiles": ["Se", "requiere", "un", "suplicatorio", "para", "procesar", "a", "un", "diputado."],
                    "solution": ["Se", "requiere", "un", "suplicatorio", "para", "procesar", "a", "un", "diputado."],
                    "teaches": ["inmunidad", "ccse"]
                }
            ]
        },
        {
            "num": "05",
            "stem": "b1-ccse-cortes-05",
            "exercises": [
                {
                    "id": "ex.b1.ccse.cortes.05.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuántas firmas acreditadas se requieren como mínimo para una iniciativa legislativa popular?",
                    "options": [
                        "500.000",
                        "250.000",
                        "1.000.000"
                    ],
                    "correct": 0,
                    "teaches": ["leyes", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.05.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "La aprobación de una ley orgánica requiere mayoría _____ del Congreso en una votación final.",
                    "answer": "absoluta",
                    "english": "The approval of an organic law requires an absolute majority of Congress in a final vote.",
                    "teaches": ["leyes", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.cortes.05.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Government presents bills to the Congress of Deputies.",
                    "tiles": ["El", "Gobierno", "presenta", "proyectos", "de", "ley", "al", "Congreso."],
                    "solution": ["El", "Gobierno", "presenta", "proyectos", "de", "ley", "al", "Congreso."],
                    "teaches": ["leyes", "ccse"]
                }
            ]
        }
    ]

    for ed in ex_data_list:
        stem = ed["stem"]
        write_json(f"content/es-es/exercises/b1/{stem}-ex.json", {
            "lesson": stem,
            "exercises": ed["exercises"]
        })

    # Consolidation Exercises
    write_json("content/es-es/exercises/b1/b1-ccse-cortes-consolidation-ex.json", {
        "lesson": "b1-ccse-cortes-consolidation",
        "exercises": [
            {
                "id": "ex.b1.ccse.cortes.consolidation.1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cómo se llama el parlamento español formado por el Congreso y el Senado?",
                "options": [
                    "Las Cortes Generales",
                    "La Asamblea Nacional",
                    "El Consejo General"
                ],
                "correct": 0,
                "teaches": ["cortes", "ccse"]
            },
            {
                "id": "ex.b1.ccse.cortes.consolidation.2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿A quién corresponde examinar, enmendar y aprobar los Presupuestos Generales del Estado?",
                "options": [
                    "A las Cortes Generales",
                    "Al Tribunal de Cuentas",
                    "Al Banco de España"
                ],
                "correct": 0,
                "teaches": ["cortes", "ccse"]
            },
            {
                "id": "ex.b1.ccse.cortes.consolidation.3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Por cuánto tiempo son elegidos los miembros de las Cortes Generales?",
                "options": [
                    "4 años",
                    "5 años",
                    "6 años"
                ],
                "correct": 0,
                "teaches": ["cortes", "ccse"]
            }
        ]
    })

def generate_unit_4():
    # Stems: b1-ccse-gobierno-01 .. 05, b1-ccse-gobierno-consolidation
    
    # 1. Lessons
    lessons_meta = [
        {
            "num": "01",
            "title": "El Presidente del Gobierno y la Investidura",
            "grammar": "Oraciones temporales con subjuntivo en procedimientos institucionales",
            "goal": "Conocer el proceso de investidura, votaciones y nombramiento del Presidente del Gobierno.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-gobierno-01-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-gobierno-01-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-gobierno-01-ex.json",
            "ex_refs": [
                "ex.b1.ccse.gobierno.01.1",
                "ex.b1.ccse.gobierno.01.2",
                "ex.b1.ccse.gobierno.01.3"
            ]
        },
        {
            "num": "02",
            "title": "El Consejo de Ministros y el Poder Ejecutivo",
            "grammar": "Verbos de atribución y competencia institucional",
            "goal": "Aprender la estructura del Gobierno, el papel de los ministros y la función ejecutiva.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-gobierno-02-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-gobierno-02-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-gobierno-02-ex.json",
            "ex_refs": [
                "ex.b1.ccse.gobierno.02.1",
                "ex.b1.ccse.gobierno.02.2",
                "ex.b1.ccse.gobierno.02.3"
            ]
        },
        {
            "num": "03",
            "title": "Moción de Censura y Cuestión de Confianza",
            "grammar": "Estructuras condicionales e hipotéticas en Derecho parlamentario",
            "goal": "Comprender los mecanismos constitucionales de exigencia de responsabilidad política.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-gobierno-03-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-gobierno-03-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-gobierno-03-ex.json",
            "ex_refs": [
                "ex.b1.ccse.gobierno.03.1",
                "ex.b1.ccse.gobierno.03.2",
                "ex.b1.ccse.gobierno.03.3"
            ]
        },
        {
            "num": "04",
            "title": "La Administración Pública y el Principio de Legalidad",
            "grammar": "Oraciones de relativo con preposición en textos jurídicos",
            "goal": "Conocer los principios de la Administración y la figura del Delegado del Gobierno.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-gobierno-04-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-gobierno-04-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-gobierno-04-ex.json",
            "ex_refs": [
                "ex.b1.ccse.gobierno.04.1",
                "ex.b1.ccse.gobierno.04.2",
                "ex.b1.ccse.gobierno.04.3"
            ]
        },
        {
            "num": "05",
            "title": "Órganos Consultivos: El Consejo de Estado",
            "grammar": "Construcciones valorativas y de obligatoriedad legal",
            "goal": "Estudiar la función consultiva del Consejo de Estado y otros órganos de asesoramiento.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-gobierno-05-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-gobierno-05-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-gobierno-05-ex.json",
            "ex_refs": [
                "ex.b1.ccse.gobierno.05.1",
                "ex.b1.ccse.gobierno.05.2",
                "ex.b1.ccse.gobierno.05.3"
            ]
        }
    ]

    for lm in lessons_meta:
        n = lm["num"]
        stem = f"b1-ccse-gobierno-{n}"
        lesson_data = {
            "id": f"lesson.b1.ccse.gobierno.{n}",
            "level": "b1",
            "title": lm["title"],
            "grammar": lm["grammar"],
            "goal": lm["goal"],
            "track": "cultura",
            "metadata": {
                "estimatedMinutes": lm["minutes"]
            },
            "sections": [
                {
                    "type": "vocabulary",
                    "title": "Vocabulario Cívico",
                    "ref": lm["vocab_ref"]
                },
                {
                    "type": "grammar",
                    "title": lm["grammar"],
                    "ref": lm["grammar_ref"]
                },
                {
                    "type": "exercise-group",
                    "title": "Práctica y Preguntas CCSE",
                    "exerciseRefs": lm["ex_refs"],
                    "ref": lm["ex_ref"]
                }
            ]
        }
        write_json(f"content/es-es/lessons/b1/{stem}.json", lesson_data)

    # Consolidation Lesson
    write_json("content/es-es/lessons/b1/b1-ccse-gobierno-consolidation.json", {
        "id": "lesson.b1.ccse.gobierno.consolidation",
        "level": "b1",
        "title": "El Gobierno y la Administración del Estado — Consolidación",
        "grammar": "Repaso CCSE: El Poder Ejecutivo y la Administración Pública",
        "goal": "Consolidar los conocimientos sobre la investidura, el Consejo de Ministros, la moción de censura y la función pública.",
        "track": "cultura",
        "metadata": {
            "estimatedMinutes": 15
        },
        "sections": [
            {
                "type": "exercise-group",
                "title": "Simulacro CCSE: El Gobierno y la Administración",
                "exerciseRefs": [
                    "ex.b1.ccse.gobierno.consolidation.1",
                    "ex.b1.ccse.gobierno.consolidation.2",
                    "ex.b1.ccse.gobierno.consolidation.3"
                ],
                "ref": "exercises/b1/b1-ccse-gobierno-consolidation-ex.json"
            }
        ]
    })

    # 2. Vocabulary Files
    voc_data_list = [
        {
            "num": "01",
            "title": "El Presidente y la Investidura",
            "words": [
                {"lemma": "investidura", "translation": "investiture / parliamentary vote of confidence", "pos": "noun"},
                {"lemma": "candidato", "translation": "candidate", "pos": "noun"},
                {"lemma": "mayoría absoluta", "translation": "absolute majority (more than half of total seats)", "pos": "expression"},
                {"lemma": "mayoría simple", "translation": "simple majority (more yes than no votes)", "pos": "expression"},
                {"lemma": "nombramiento", "translation": "appointment", "pos": "noun"}
            ]
        },
        {
            "num": "02",
            "title": "El Consejo de Ministros",
            "words": [
                {"lemma": "ministro", "translation": "minister / cabinet member", "pos": "noun"},
                {"lemma": "vicepresidente", "translation": "vice president / deputy prime minister", "pos": "noun"},
                {"lemma": "gabinete", "translation": "cabinet", "pos": "noun"},
                {"lemma": "decreto", "translation": "decree", "pos": "noun"},
                {"lemma": "ejecutivo", "translation": "executive", "pos": "adjective"}
            ]
        },
        {
            "num": "03",
            "title": "Moción de Censura y Cuestión de Confianza",
            "words": [
                {"lemma": "moción de censura", "translation": "motion of no confidence", "pos": "expression"},
                {"lemma": "cuestión de confianza", "translation": "vote of confidence", "pos": "expression"},
                {"lemma": "destitución", "translation": "dismissal / removal from office", "pos": "noun"},
                {"lemma": "respaldo", "translation": "backing / parliamentary endorsement", "pos": "noun"},
                {"lemma": "dimisión", "translation": "resignation", "pos": "noun"}
            ]
        },
        {
            "num": "04",
            "title": "La Administración Pública",
            "words": [
                {"lemma": "administración", "translation": "public administration / civil service", "pos": "noun"},
                {"lemma": "funcionario", "translation": "civil servant / public employee", "pos": "noun"},
                {"lemma": "delegado", "translation": "delegate", "pos": "noun"},
                {"lemma": "jerarquía", "translation": "hierarchy", "pos": "noun"},
                {"lemma": "competencia", "translation": "competence / official jurisdiction", "pos": "noun"}
            ]
        },
        {
            "num": "05",
            "title": "Órganos Consultivos",
            "words": [
                {"lemma": "consultivo", "translation": "advisory / consultative", "pos": "adjective"},
                {"lemma": "dictamen", "translation": "official opinion / expert report", "pos": "noun"},
                {"lemma": "preceptivo", "translation": "mandatory / legally required to request", "pos": "adjective"},
                {"lemma": "vinculante", "translation": "binding", "pos": "adjective"},
                {"lemma": "asesoramiento", "translation": "legal counseling / advice", "pos": "noun"}
            ]
        }
    ]

    for vd in voc_data_list:
        n = vd["num"]
        stem = f"b1-ccse-gobierno-{n}"
        write_json(f"content/es-es/vocabulary/b1/{stem}-voc.json", {
            "id": f"vocab.b1.ccse.gobierno.{n}",
            "lesson": stem,
            "title": vd["title"],
            "words": vd["words"]
        })

    # 3. Grammar Files
    gr_data_list = [
        {
            "num": "01",
            "title": "Oraciones temporales con subjuntivo en procedimientos institucionales",
            "text": "Los trámites constitucionales se ordenan temporalmente con conectores como 'después de que', 'hasta que' o 'una vez que', seguidos de subjuntivo cuando expresan acciones futuras o hipotéticas.",
            "examples": [
                {
                    "spanish": "El Rey nombra al Presidente después de que obtenga la confianza del Congreso.",
                    "english": "The King appoints the President after they obtain the confidence of Congress."
                },
                {
                    "spanish": "Si no hay acuerdo en dos meses, las Cámaras se disuelven para que se convoquen nuevas elecciones.",
                    "english": "If there is no agreement in two months, the Chambers are dissolved so that new elections are called."
                }
            ],
            "tip": "Dato CCSE: en la primera votación de investidura se exige mayoría absoluta (176 votos); 48 horas después, basta mayoría simple (más síes que noes)."
        },
        {
            "num": "02",
            "title": "Verbos de atribución y competencia institucional",
            "text": "Para definir las competencias del Gobierno y sus miembros se emplean verbos de régimen preposicional formal como 'corresponder a', 'incumbir a' y 'dirigir'.",
            "examples": [
                {
                    "spanish": "Corresponde al Presidente del Gobierno proponer el nombramiento de los ministros.",
                    "english": "It is the responsibility of the President of the Government to propose the appointment of ministers."
                },
                {
                    "spanish": "El Gobierno dirige la política interior y exterior y la administración militar.",
                    "english": "The Government directs domestic and foreign policy and military administration."
                }
            ],
            "tip": "El Consejo de Ministros es un órgano colegiado que se reúne semanalmente (habitualmente los martes) en el Palacio de la Moncloa en Madrid."
        },
        {
            "num": "03",
            "title": "Estructuras condicionales e hipotéticas en Derecho parlamentario",
            "text": "Las normas parlamentarias prevén situaciones de crisis con oraciones condicionales formales ('si el Congreso aprobase...', 'en el caso de que se plantee...').",
            "examples": [
                {
                    "spanish": "Si el Congreso aprueba una moción de censura, el Gobierno presenta su dimisión al Rey.",
                    "english": "If Congress approves a motion of no confidence, the Government tenders its resignation to the King."
                },
                {
                    "spanish": "La moción debe incluir un candidato alternativo para que sea admitida a trámite.",
                    "english": "The motion must include an alternative candidate in order to be admitted for processing."
                }
            ],
            "tip": "En España la moción de censura es 'constructiva': no basta con derribar al Gobierno actual, hay que votar simultáneamente a un candidato alternativo."
        },
        {
            "num": "04",
            "title": "Oraciones de relativo con preposición en textos jurídicos",
            "text": "En el Derecho administrativo se utilizan pronombres relativos precedidos de preposición y artículo determinado ('conforme al cual', 'mediante el cual', 'en el que').",
            "examples": [
                {
                    "spanish": "La Administración actúa según el principio de legalidad, conforme al cual debe someterse a la ley.",
                    "english": "The Public Administration acts according to the principle of legality, pursuant to which it must submit to the law."
                },
                {
                    "spanish": "El Delegado del Gobierno es la autoridad a través de la cual se coordina la administración estatal en la comunidad autónoma.",
                    "english": "The Government Delegate is the authority through whom state administration is coordinated in the autonomous community."
                }
            ],
            "tip": "El artículo 103 de la Constitución establece que la Administración sirve con objetividad los intereses generales y sus funcionarios son seleccionados por mérito y capacidad."
        },
        {
            "num": "05",
            "title": "Construcciones valorativas y de obligatoriedad legal",
            "text": "Para explicar la función consultiva se emplean adjetivos valorativos en oraciones impersonales con subjuntivo ('es preceptivo que', 'resulta vinculante').",
            "examples": [
                {
                    "spanish": "Es preceptivo que el Gobierno consulte al Consejo de Estado en proyectos de ley orgánica.",
                    "english": "It is mandatory for the Government to consult the Council of State on organic bills."
                },
                {
                    "spanish": "Aunque el dictamen sea preceptivo, sus conclusiones no suelen ser vinculantes.",
                    "english": "Although the ruling is mandatory to request, its conclusions are generally not binding."
                }
            ],
            "tip": "Pregunta frecuente CCSE: El supremo órgano consultivo del Gobierno es el Consejo de Estado (artículo 107 de la Constitución)."
        }
    ]

    for gd in gr_data_list:
        n = gd["num"]
        stem = f"b1-ccse-gobierno-{n}"
        write_json(f"content/es-es/grammar/b1/{stem}-gr.json", {
            "id": f"grammar.b1.ccse.gobierno.{n}",
            "title": gd["title"],
            "sections": [
                {
                    "type": "text",
                    "content": gd["text"]
                },
                {
                    "type": "examples",
                    "items": gd["examples"]
                },
                {
                    "type": "tip",
                    "content": gd["tip"]
                }
            ]
        })

    # 4. Exercises Files
    ex_data_list = [
        {
            "num": "01",
            "stem": "b1-ccse-gobierno-01",
            "exercises": [
                {
                    "id": "ex.b1.ccse.gobierno.01.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué mayoría requiere el candidato a Presidente del Gobierno en la primera votación de investidura?",
                    "options": [
                        "Mayoría absoluta",
                        "Mayoría simple",
                        "Dos tercios de los diputados"
                    ],
                    "correct": 0,
                    "teaches": ["gobierno", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.01.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "En la segunda votación de investidura, 48 horas después, se requiere únicamente mayoría _____.",
                    "answer": "simple",
                    "english": "In the second investiture vote, 48 hours later, only a simple majority is required.",
                    "teaches": ["gobierno", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.01.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The King proposes a candidate for the Presidency of the Government.",
                    "tiles": ["El", "Rey", "propone", "un", "candidato", "a", "la", "Presidencia."],
                    "solution": ["El", "Rey", "propone", "un", "candidato", "a", "la", "Presidencia."],
                    "teaches": ["gobierno", "ccse"]
                }
            ]
        },
        {
            "num": "02",
            "stem": "b1-ccse-gobierno-02",
            "exercises": [
                {
                    "id": "ex.b1.ccse.gobierno.02.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién propone formalmente el nombramiento y cese de los ministros al Rey?",
                    "options": [
                        "El Presidente del Gobierno",
                        "El Presidente del Congreso",
                        "El Tribunal Constitucional"
                    ],
                    "correct": 0,
                    "teaches": ["gobierno", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.02.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "El Gobierno ejerce la función _____ y la potestad reglamentaria.",
                    "answer": "ejecutiva",
                    "english": "The Government exercises executive power and regulatory authority.",
                    "teaches": ["gobierno", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.02.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Council of Ministers meets at the Moncloa Palace.",
                    "tiles": ["El", "Consejo", "de", "Ministros", "se", "reúne", "en", "la", "Moncloa."],
                    "solution": ["El", "Consejo", "de", "Ministros", "se", "reúne", "en", "la", "Moncloa."],
                    "teaches": ["gobierno", "ccse"]
                }
            ]
        },
        {
            "num": "03",
            "stem": "b1-ccse-gobierno-03",
            "exercises": [
                {
                    "id": "ex.b1.ccse.gobierno.03.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué característica obligatoria tiene la moción de censura en España?",
                    "options": [
                        "Es constructiva: debe incluir un candidato a la Presidencia",
                        "Se vota en sesión conjunta del Congreso y Senado",
                        "La aprueba directamente el Tribunal Constitucional"
                    ],
                    "correct": 0,
                    "teaches": ["censura", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.03.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Para ser aprobada, una moción de censura necesita el voto de la mayoría _____ del Congreso.",
                    "answer": "absoluta",
                    "english": "To be approved, a motion of no confidence needs the vote of the absolute majority of Congress.",
                    "teaches": ["censura", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.03.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The motion of no confidence must be proposed by at least thirty-five deputies.",
                    "tiles": ["La", "moción", "debe", "ser", "propuesta", "por", "al", "menos", "treinta", "y", "cinco", "diputados."],
                    "solution": ["La", "moción", "debe", "ser", "propuesta", "por", "al", "menos", "treinta", "y", "cinco", "diputados."],
                    "teaches": ["censura", "ccse"]
                }
            ]
        },
        {
            "num": "04",
            "stem": "b1-ccse-gobierno-04",
            "exercises": [
                {
                    "id": "ex.b1.ccse.gobierno.04.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién representa a la administración del Estado en el territorio de una Comunidad Autónoma?",
                    "options": [
                        "El Delegado del Gobierno",
                        "El Presidente autonómico",
                        "El Alcalde de la capital"
                    ],
                    "correct": 0,
                    "teaches": ["administracion", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.04.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "El acceso a la función pública se rige por los principios constitucionales de mérito y _____.",
                    "answer": "capacidad",
                    "english": "Access to the civil service is governed by the constitutional principles of merit and capacity.",
                    "teaches": ["administracion", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.04.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "Public Administration serves general interests with objectivity.",
                    "tiles": ["La", "Administración", "Pública", "sirve", "con", "objetividad", "los", "intereses", "generales."],
                    "solution": ["La", "Administración", "Pública", "sirve", "con", "objetividad", "los", "intereses", "generales."],
                    "teaches": ["administracion", "ccse"]
                }
            ]
        },
        {
            "num": "05",
            "stem": "b1-ccse-gobierno-05",
            "exercises": [
                {
                    "id": "ex.b1.ccse.gobierno.05.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es el supremo órgano consultivo del Gobierno de España?",
                    "options": [
                        "El Consejo de Estado",
                        "El Defensor del Pueblo",
                        "El Tribunal de Cuentas"
                    ],
                    "correct": 0,
                    "teaches": ["organos-consultivos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.05.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los dictámenes del Consejo de Estado suelen ser preceptivos pero no _____.",
                    "answer": "vinculantes",
                    "english": "The opinions of the Council of State are usually mandatory to request but not binding.",
                    "teaches": ["organos-consultivos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.gobierno.05.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Council of State emits opinions on bills and draft decrees.",
                    "tiles": ["El", "Consejo", "de", "Estado", "emite", "dictámenes", "sobre", "proyectos", "normativos."],
                    "solution": ["El", "Consejo", "de", "Estado", "emite", "dictámenes", "sobre", "proyectos", "normativos."],
                    "teaches": ["organos-consultivos", "ccse"]
                }
            ]
        }
    ]

    for ed in ex_data_list:
        stem = ed["stem"]
        write_json(f"content/es-es/exercises/b1/{stem}-ex.json", {
            "lesson": stem,
            "exercises": ed["exercises"]
        })

    # Consolidation Exercises
    write_json("content/es-es/exercises/b1/b1-ccse-gobierno-consolidation-ex.json", {
        "lesson": "b1-ccse-gobierno-consolidation",
        "exercises": [
            {
                "id": "ex.b1.ccse.gobierno.consolidation.1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién dirige la política interior y exterior de España según la Constitución?",
                "options": [
                    "El Gobierno",
                    "El Rey",
                    "El Presidente del Congreso"
                ],
                "correct": 0,
                "teaches": ["gobierno", "ccse"]
            },
            {
                "id": "ex.b1.ccse.gobierno.consolidation.2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién nombra formalmente al Presidente del Gobierno?",
                "options": [
                    "El Rey, previa investidura por el Congreso",
                    "El Presidente del Senado",
                    "Los ciudadanos por sufragio directo"
                ],
                "correct": 0,
                "teaches": ["gobierno", "ccse"]
            },
            {
                "id": "ex.b1.ccse.gobierno.consolidation.3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿A quién corresponde la iniciativa de plantear una cuestión de confianza?",
                "options": [
                    "Al Presidente del Gobierno, previa deliberación del Consejo de Ministros",
                    "A la décima parte de los diputados del Congreso",
                    "Al Rey como Jefe del Estado"
                ],
                "correct": 0,
                "teaches": ["gobierno", "ccse"]
            }
        ]
    })

if __name__ == "__main__":
    generate_unit_3()
    generate_unit_4()
    print("Units 3 and 4 generated successfully.")
