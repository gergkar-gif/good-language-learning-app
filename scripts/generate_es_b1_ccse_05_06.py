#!/usr/bin/env python3
"""Generate Spain CCSE Units 5 & 6 (content/es-es, B1, track: cultura).

Unit 5: El Poder Judicial y el Tribunal Constitucional
Unit 6: Las Instituciones Autonómicas y Locales
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def write_json(rel_path: str, data: dict):
    target = ROOT / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {rel_path}")

def generate_unit_5():
    # Stems: b1-ccse-judicial-01 .. 05, b1-ccse-judicial-consolidation
    
    # 1. Lessons
    lessons_meta = [
        {
            "num": "01",
            "title": "Principios del Poder Judicial y los Jueces",
            "grammar": "Pasiva de estado y adjetivos participiales en el ámbito judicial",
            "goal": "Conocer los principios de independencia, inamovilidad y sometimiento a la ley de jueces y magistrados.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-judicial-01-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-judicial-01-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-judicial-01-ex.json",
            "ex_refs": [
                "ex.b1.ccse.judicial.01.1",
                "ex.b1.ccse.judicial.01.2",
                "ex.b1.ccse.judicial.01.3"
            ]
        },
        {
            "num": "02",
            "title": "El Consejo General del Poder Judicial (CGPJ)",
            "grammar": "Oraciones de relativo especificativas con preposición",
            "goal": "Aprender la composición, elección y funciones del órgano de gobierno de los jueces.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-judicial-02-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-judicial-02-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-judicial-02-ex.json",
            "ex_refs": [
                "ex.b1.ccse.judicial.02.1",
                "ex.b1.ccse.judicial.02.2",
                "ex.b1.ccse.judicial.02.3"
            ]
        },
        {
            "num": "03",
            "title": "El Tribunal Supremo y la Organización Judicial",
            "grammar": "Comparativos y superlativos relativos de jerarquía jurisdiccional",
            "goal": "Comprender la estructura de los tribunales españoles: Tribunal Supremo, Audiencia Nacional y TSJ.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-judicial-03-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-judicial-03-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-judicial-03-ex.json",
            "ex_refs": [
                "ex.b1.ccse.judicial.03.1",
                "ex.b1.ccse.judicial.03.2",
                "ex.b1.ccse.judicial.03.3"
            ]
        },
        {
            "num": "04",
            "title": "El Ministerio Fiscal",
            "grammar": "Perífrasis verbales de finalidad y tutela de la legalidad",
            "goal": "Estudiar la misión del Ministerio Fiscal, el Fiscal General del Estado y sus principios rectores.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-judicial-04-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-judicial-04-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-judicial-04-ex.json",
            "ex_refs": [
                "ex.b1.ccse.judicial.04.1",
                "ex.b1.ccse.judicial.04.2",
                "ex.b1.ccse.judicial.04.3"
            ]
        },
        {
            "num": "05",
            "title": "El Tribunal Constitucional",
            "grammar": "Construcciones de legitimación procesal y recursos constitucionales",
            "goal": "Conocer la composición del Tribunal Constitucional, el recurso de amparo y el control de constitucionalidad.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-judicial-05-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-judicial-05-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-judicial-05-ex.json",
            "ex_refs": [
                "ex.b1.ccse.judicial.05.1",
                "ex.b1.ccse.judicial.05.2",
                "ex.b1.ccse.judicial.05.3"
            ]
        }
    ]

    for lm in lessons_meta:
        n = lm["num"]
        stem = f"b1-ccse-judicial-{n}"
        lesson_data = {
            "id": f"lesson.b1.ccse.judicial.{n}",
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
                    "content": {
                        "ref": lm["vocab_ref"]
                    }
                },
                {
                    "type": "grammar",
                    "title": lm["grammar"],
                    "content": {
                        "ref": lm["grammar_ref"]
                    }
                },
                {
                    "type": "exercise-group",
                    "title": "Práctica y Preguntas CCSE",
                    "exerciseRefs": lm["ex_refs"],
                    "content": {
                        "ref": lm["ex_ref"]
                    }
                }
            ]
        }
        write_json(f"content/es-es/lessons/b1/{stem}.json", lesson_data)

    # Consolidation Lesson
    write_json("content/es-es/lessons/b1/b1-ccse-judicial-consolidation.json", {
        "id": "lesson.b1.ccse.judicial.consolidation",
        "level": "b1",
        "title": "El Poder Judicial y el Tribunal Constitucional — Consolidación",
        "grammar": "Repaso CCSE: El Poder Judicial y las Garantías Jurisdiccionales",
        "goal": "Consolidar los conocimientos sobre tribunales, jueces, el CGPJ, el Ministerio Fiscal y el Tribunal Constitucional.",
        "track": "cultura",
        "metadata": {
            "estimatedMinutes": 15
        },
        "sections": [
            {
                "type": "exercise-group",
                "title": "Simulacro CCSE: Poder Judicial y Tribunal Constitucional",
                "exerciseRefs": [
                    "ex.b1.ccse.judicial.consolidation.1",
                    "ex.b1.ccse.judicial.consolidation.2",
                    "ex.b1.ccse.judicial.consolidation.3"
                ],
                "content": {
                    "ref": "exercises/b1/b1-ccse-judicial-consolidation-ex.json"
                }
            }
        ]
    })

    # 2. Vocabulary Files
    voc_data_list = [
        {
            "num": "01",
            "title": "Principios del Poder Judicial",
            "words": [
                {"lemma": "juez", "translation": "judge", "pos": "noun"},
                {"lemma": "magistrado", "translation": "magistrate / senior judge", "pos": "noun"},
                {"lemma": "inamovible", "translation": "unremovable / possessing security of tenure", "pos": "adjective"},
                {"lemma": "justicia gratuita", "translation": "free legal aid / free justice", "pos": "expression"},
                {"lemma": "jurisdicción", "translation": "jurisdiction / judicial authority", "pos": "noun"}
            ]
        },
        {
            "num": "02",
            "title": "El Consejo General del Poder Judicial",
            "words": [
                {"lemma": "vocal", "translation": "board member / council member", "pos": "noun"},
                {"lemma": "jurista", "translation": "jurist / legal scholar", "pos": "noun"},
                {"lemma": "gobierno judicial", "translation": "judicial governance", "pos": "expression"},
                {"lemma": "competencia", "translation": "jurisdiction / remit", "pos": "noun"},
                {"lemma": "ascenso", "translation": "promotion", "pos": "noun"}
            ]
        },
        {
            "num": "03",
            "title": "Tribunal Supremo y Estructura Judicial",
            "words": [
                {"lemma": "casación", "translation": "cassation / appeal on points of law", "pos": "noun"},
                {"lemma": "sala", "translation": "chamber / court division", "pos": "noun"},
                {"lemma": "orden jurisdiccional", "translation": "jurisdictional branch (civil, criminal, etc.)", "pos": "expression"},
                {"lemma": "instancia", "translation": "instance / court level", "pos": "noun"},
                {"lemma": "sentencia", "translation": "court ruling / judicial sentence", "pos": "noun"}
            ]
        },
        {
            "num": "04",
            "title": "El Ministerio Fiscal",
            "words": [
                {"lemma": "fiscal", "translation": "public prosecutor", "pos": "noun"},
                {"lemma": "fiscalía", "translation": "public prosecution service / prosecutor's office", "pos": "noun"},
                {"lemma": "legalidad", "translation": "legality / rule of law", "pos": "noun"},
                {"lemma": "acusación", "translation": "prosecution / accusation", "pos": "noun"},
                {"lemma": "imparcialidad", "translation": "impartiality", "pos": "noun"}
            ]
        },
        {
            "num": "05",
            "title": "El Tribunal Constitucional",
            "words": [
                {"lemma": "constitucional", "translation": "constitutional", "pos": "adjective"},
                {"lemma": "recurso de amparo", "translation": "appeal for constitutional protection of fundamental rights", "pos": "expression"},
                {"lemma": "inconstitucionalidad", "translation": "unconstitutionality", "pos": "noun"},
                {"lemma": "garantía", "translation": "guarantee / safeguard", "pos": "noun"},
                {"lemma": "intérprete", "translation": "interpreter", "pos": "noun"}
            ]
        }
    ]

    for vd in voc_data_list:
        n = vd["num"]
        stem = f"b1-ccse-judicial-{n}"
        write_json(f"content/es-es/vocabulary/b1/{stem}-voc.json", {
            "id": f"vocab.b1.ccse.judicial.{n}",
            "lesson": stem,
            "title": vd["title"],
            "words": vd["words"]
        })

    # 3. Grammar Files
    gr_data_list = [
        {
            "num": "01",
            "title": "Pasiva de estado y adjetivos participiales en el ámbito judicial",
            "text": "La condición institucional de jueces y tribunales se expresa a menudo con el verbo 'estar' seguido de participios adjetivados ('estar sometidos a la ley', 'estar reconocidos').",
            "examples": [
                {
                    "spanish": "Los jueces están sometidos únicamente al imperio de la ley.",
                    "english": "Judges are subject solely to the rule of law."
                },
                {
                    "spanish": "La justicia es administrada en nombre del Rey por jueces independientes.",
                    "english": "Justice is administered in the name of the King by independent judges."
                }
            ],
            "tip": "Pregunta CCSE frecuente: La justicia emana del pueblo y se administra en nombre del Rey (artículo 117.1 de la Constitución)."
        },
        {
            "num": "02",
            "title": "Oraciones de relativo especificativas con preposición",
            "text": "Para detallar los requisitos y procedimientos de selección de órganos colegiados se emplean relativos precedidos de preposición ('entre los cuales', 'de los que', 'ante el cual').",
            "examples": [
                {
                    "spanish": "El CGPJ está integrado por veinte miembros, de los cuales doce son jueces o magistrados.",
                    "english": "The CGPJ is composed of twenty members, of whom twelve are judges or magistrates."
                },
                {
                    "spanish": "Los vocales son juristas de reconocida competencia entre los que se nombra al Presidente.",
                    "english": "The council members are jurists of recognized standing from among whom the President is named."
                }
            ],
            "tip": "El CGPJ es el órgano de gobierno de los jueces, pero no juzga ni dicta sentencias (no ejerce potestad jurisdiccional)."
        },
        {
            "num": "03",
            "title": "Comparativos y superlativos relativos de jerarquía jurisdiccional",
            "text": "La jerarquía de los tribunales se organiza con superlativos relativos ('el órgano superior', 'la instancia más alta') para delimitar el alcance de sus fallos.",
            "examples": [
                {
                    "spanish": "El Tribunal Supremo es el órgano jurisdiccional superior en todos los órdenes.",
                    "english": "The Supreme Court is the highest judicial body in all jurisdictional branches."
                },
                {
                    "spanish": "El Tribunal Superior de Justicia es el tribunal más alto de la comunidad autónoma.",
                    "english": "The High Court of Justice is the highest court of the autonomous community."
                }
            ],
            "tip": "El Tribunal Supremo tiene jurisdicción en toda España en los órdenes civil, penal, contencioso-administrativo, social y militar, salvo en materia constitucional."
        },
        {
            "num": "04",
            "title": "Perífrasis verbales de finalidad y tutela de la legalidad",
            "text": "La actuación de la Fiscalía se redacta formalmente con perífrasis de custodia y objetivo institucional ('velar por + infinitivo', 'promover la defensa de').",
            "examples": [
                {
                    "spanish": "El Ministerio Fiscal debe velar por la independencia de los tribunales.",
                    "english": "The Public Prosecution Service must ensure the independence of the courts."
                },
                {
                    "spanish": "Su función consiste en promover la acción de la justicia en defensa de la legalidad.",
                    "english": "Its function consists in promoting the action of justice in defense of the rule of law."
                }
            ],
            "tip": "El Fiscal General del Estado es nombrado por el Rey, a propuesta del Gobierno, oído previamente el CGPJ."
        },
        {
            "num": "05",
            "title": "Construcciones de legitimación procesal y recursos constitucionales",
            "text": "El acceso a la justicia constitucional se articula con fórmulas de legitimación activa ('estar legitimado para', 'tener derecho a interponer').",
            "examples": [
                {
                    "spanish": "El Defensor del Pueblo y cincuenta diputados están legitimados para interponer el recurso de inconstitucionalidad.",
                    "english": "The Ombudsman and fifty deputies have standing to lodge an appeal of unconstitutionality."
                },
                {
                    "spanish": "Cualquier ciudadano puede interponer el recurso de amparo ante la vulneración de derechos fundamentales.",
                    "english": "Any citizen may lodge an amparo appeal against violations of fundamental rights."
                }
            ],
            "tip": "El Tribunal Constitucional cuenta con 12 magistrados nombrados por el Rey por un mandato de 9 años: 4 por el Congreso, 4 por el Senado, 2 por el Gobierno y 2 por el CGPJ."
        }
    ]

    for gd in gr_data_list:
        n = gd["num"]
        stem = f"b1-ccse-judicial-{n}"
        write_json(f"content/es-es/grammar/b1/{stem}-gr.json", {
            "id": f"grammar.b1.ccse.judicial.{n}",
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
            "stem": "b1-ccse-judicial-01",
            "exercises": [
                {
                    "id": "ex.b1.ccse.judicial.01.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿En nombre de quién se administra la justicia en España según la Constitución?",
                    "options": [
                        "Del Rey",
                        "Del Presidente del Gobierno",
                        "Del pueblo soberano"
                    ],
                    "correct": 0,
                    "teaches": ["poder-judicial", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.01.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los jueces y magistrados son independientes, responsables e _____ en el ejercicio de su función.",
                    "answer": "inamovibles",
                    "english": "Judges and magistrates are independent, accountable, and possess security of tenure in office.",
                    "teaches": ["poder-judicial", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.01.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "Justice emanates from the people and is administered in the name of the King.",
                    "tiles": ["La", "justicia", "emana", "del", "pueblo", "y", "se", "administra", "en", "nombre", "del", "Rey."],
                    "solution": ["La", "justicia", "emana", "del", "pueblo", "y", "se", "administra", "en", "nombre", "del", "Rey."],
                    "teaches": ["poder-judicial", "ccse"]
                }
            ]
        },
        {
            "num": "02",
            "stem": "b1-ccse-judicial-02",
            "exercises": [
                {
                    "id": "ex.b1.ccse.judicial.02.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es el órgano de gobierno del Poder Judicial en España?",
                    "options": [
                        "El Consejo General del Poder Judicial",
                        "El Ministerio de Justicia",
                        "El Tribunal Supremo"
                    ],
                    "correct": 0,
                    "teaches": ["cgpj", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.02.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los miembros del Consejo General del Poder Judicial son nombrados para un mandato de _____ años.",
                    "answer": "cinco",
                    "english": "The members of the General Council of the Judiciary are appointed for a term of five years.",
                    "teaches": ["cgpj", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.02.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The CGPJ is the governing body of judges.",
                    "tiles": ["El", "CGPJ", "es", "el", "órgano", "de", "gobierno", "de", "los", "jueces."],
                    "solution": ["El", "CGPJ", "es", "el", "órgano", "de", "gobierno", "de", "los", "jueces."],
                    "teaches": ["cgpj", "ccse"]
                }
            ]
        },
        {
            "num": "03",
            "stem": "b1-ccse-judicial-03",
            "exercises": [
                {
                    "id": "ex.b1.ccse.judicial.03.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es el órgano jurisdiccional superior en todos los órdenes judiciales, salvo en materia constitucional?",
                    "options": [
                        "El Tribunal Supremo",
                        "La Audiencia Nacional",
                        "El Tribunal Superior de Justicia"
                    ],
                    "correct": 0,
                    "teaches": ["tribunal-supremo", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.03.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "El Tribunal _____ de Justicia culmina la organización judicial en el ámbito de la comunidad autónoma.",
                    "answer": "Superior",
                    "english": "The High Court of Justice culminates the judicial organization within the autonomous community.",
                    "teaches": ["tribunal-supremo", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.03.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Supreme Court has jurisdiction across the whole territory of Spain.",
                    "tiles": ["El", "Tribunal", "Supremo", "tiene", "jurisdicción", "en", "toda", "España."],
                    "solution": ["El", "Tribunal", "Supremo", "tiene", "jurisdicción", "en", "toda", "España."],
                    "teaches": ["tribunal-supremo", "ccse"]
                }
            ]
        },
        {
            "num": "04",
            "stem": "b1-ccse-judicial-04",
            "exercises": [
                {
                    "id": "ex.b1.ccse.judicial.04.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién propone formalmente el nombramiento del Fiscal General del Estado?",
                    "options": [
                        "El Gobierno",
                        "El Congreso de los Diputados",
                        "El Consejo de Estado"
                    ],
                    "correct": 0,
                    "teaches": ["ministerio-fiscal", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.04.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "El Ministerio Fiscal actúa conforme a los principios de unidad de actuación y dependencia _____.",
                    "answer": "jerárquica",
                    "english": "The Public Prosecution Service acts in accordance with the principles of unity of action and hierarchical subordination.",
                    "teaches": ["ministerio-fiscal", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.04.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Prosecutor General is appointed by the King on a proposal from the Government.",
                    "tiles": ["El", "Fiscal", "General", "es", "nombrado", "por", "el", "Rey", "a", "propuesta", "del", "Gobierno."],
                    "solution": ["El", "Fiscal", "General", "es", "nombrado", "por", "el", "Rey", "a", "propuesta", "del", "Gobierno."],
                    "teaches": ["ministerio-fiscal", "ccse"]
                }
            ]
        },
        {
            "num": "05",
            "stem": "b1-ccse-judicial-05",
            "exercises": [
                {
                    "id": "ex.b1.ccse.judicial.05.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuántos magistrados componen el Tribunal Constitucional de España?",
                    "options": [
                        "12",
                        "15",
                        "20"
                    ],
                    "correct": 0,
                    "teaches": ["tribunal-constitucional", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.05.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los magistrados del Tribunal Constitucional son nombrados por un mandato de _____ años.",
                    "answer": "nueve",
                    "english": "The magistrates of the Constitutional Court are appointed for a term of nine years.",
                    "teaches": ["tribunal-constitucional", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.judicial.05.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Constitutional Court is the supreme interpreter of the Constitution.",
                    "tiles": ["El", "Tribunal", "Constitucional", "es", "el", "intérprete", "supremo", "de", "la", "Constitución."],
                    "solution": ["El", "Tribunal", "Constitucional", "es", "el", "intérprete", "supremo", "de", "la", "Constitución."],
                    "teaches": ["tribunal-constitucional", "ccse"]
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
    write_json("content/es-es/exercises/b1/b1-ccse-judicial-consolidation-ex.json", {
        "lesson": "b1-ccse-judicial-consolidation",
        "exercises": [
            {
                "id": "ex.b1.ccse.judicial.consolidation.1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién es el intérprete supremo de la Constitución en España?",
                "options": [
                    "El Tribunal Constitucional",
                    "El Tribunal Supremo",
                    "El Consejo General del Poder Judicial"
                ],
                "correct": 0,
                "teaches": ["tribunal-constitucional", "ccse"]
            },
            {
                "id": "ex.b1.ccse.judicial.consolidation.2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué recurso pueden presentar los ciudadanos ante el Tribunal Constitucional para defender sus derechos fundamentales?",
                "options": [
                    "El recurso de amparo",
                    "El recurso de casación",
                    "El recurso de inconstitucionalidad"
                ],
                "correct": 0,
                "teaches": ["tribunal-constitucional", "ccse"]
            },
            {
                "id": "ex.b1.ccse.judicial.consolidation.3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién preside el Consejo General del Poder Judicial?",
                "options": [
                    "El Presidente del Tribunal Supremo",
                    "El Ministro de Justicia",
                    "El Fiscal General del Estado"
                ],
                "correct": 0,
                "teaches": ["cgpj", "ccse"]
            }
        ]
    })

def generate_unit_6():
    # Stems: b1-ccse-autonomias-inst-01 .. 05, b1-ccse-autonomias-inst-consolidation
    
    # 1. Lessons
    lessons_meta = [
        {
            "num": "01",
            "title": "La Organización Territorial: Comunidades y Ciudades Autónomas",
            "grammar": "Estructuras de distribución y descentralización administrativa",
            "goal": "Conocer la estructura territorial de España: 17 Comunidades Autónomas y 2 Ciudades Autónomas.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-autonomias-inst-01-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-autonomias-inst-01-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-autonomias-inst-01-ex.json",
            "ex_refs": [
                "ex.b1.ccse.autonomias.inst.01.1",
                "ex.b1.ccse.autonomias.inst.01.2",
                "ex.b1.ccse.autonomias.inst.01.3"
            ]
        },
        {
            "num": "02",
            "title": "Los Estatutos de Autonomía",
            "grammar": "Fórmulas de obligatoriedad y contenido normativo básico",
            "goal": "Comprender la naturaleza de los Estatutos de Autonomía como norma institucional básica.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-autonomias-inst-02-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-autonomias-inst-02-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-autonomias-inst-02-ex.json",
            "ex_refs": [
                "ex.b1.ccse.autonomias.inst.02.1",
                "ex.b1.ccse.autonomias.inst.02.2",
                "ex.b1.ccse.autonomias.inst.02.3"
            ]
        },
        {
            "num": "03",
            "title": "Las Instituciones Autonómicas: Asamblea, Presidente y Gobierno",
            "grammar": "Verbos de investidura y representación ordinaria del Estado",
            "goal": "Aprender el funcionamiento de los parlamentos autonómicos, el Presidente y los Consejeros.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-autonomias-inst-03-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-autonomias-inst-03-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-autonomias-inst-03-ex.json",
            "ex_refs": [
                "ex.b1.ccse.autonomias.inst.03.1",
                "ex.b1.ccse.autonomias.inst.03.2",
                "ex.b1.ccse.autonomias.inst.03.3"
            ]
        },
        {
            "num": "04",
            "title": "La Administración Local: Los Municipios y Ayuntamientos",
            "grammar": "Léxico de proximidad vecinal y administración municipal",
            "goal": "Conocer la elección de concejales y alcaldes y las competencias de los ayuntamientos.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-autonomias-inst-04-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-autonomias-inst-04-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-autonomias-inst-04-ex.json",
            "ex_refs": [
                "ex.b1.ccse.autonomias.inst.04.1",
                "ex.b1.ccse.autonomias.inst.04.2",
                "ex.b1.ccse.autonomias.inst.04.3"
            ]
        },
        {
            "num": "05",
            "title": "Las Provincias, Diputaciones, Cabildos y Consejos Insulares",
            "grammar": "Estructuras distributivas y excepciones territoriales",
            "goal": "Diferenciar la Diputación Provincial, los Cabildos canarios, los Consejos insulares baleares y las autonomías uniprovinciales.",
            "minutes": 12,
            "vocab_ref": "vocabulary/b1/b1-ccse-autonomias-inst-05-voc.json",
            "grammar_ref": "grammar/b1/b1-ccse-autonomias-inst-05-gr.json",
            "ex_ref": "exercises/b1/b1-ccse-autonomias-inst-05-ex.json",
            "ex_refs": [
                "ex.b1.ccse.autonomias.inst.05.1",
                "ex.b1.ccse.autonomias.inst.05.2",
                "ex.b1.ccse.autonomias.inst.05.3"
            ]
        }
    ]

    for lm in lessons_meta:
        n = lm["num"]
        stem = f"b1-ccse-autonomias-inst-{n}"
        lesson_data = {
            "id": f"lesson.b1.ccse.autonomias.inst.{n}",
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
                    "content": {
                        "ref": lm["vocab_ref"]
                    }
                },
                {
                    "type": "grammar",
                    "title": lm["grammar"],
                    "content": {
                        "ref": lm["grammar_ref"]
                    }
                },
                {
                    "type": "exercise-group",
                    "title": "Práctica y Preguntas CCSE",
                    "exerciseRefs": lm["ex_refs"],
                    "content": {
                        "ref": lm["ex_ref"]
                    }
                }
            ]
        }
        write_json(f"content/es-es/lessons/b1/{stem}.json", lesson_data)

    # Consolidation Lesson
    write_json("content/es-es/lessons/b1/b1-ccse-autonomias-inst-consolidation.json", {
        "id": "lesson.b1.ccse.autonomias.inst.consolidation",
        "level": "b1",
        "title": "Las Instituciones Autonómicas y Locales — Consolidación",
        "grammar": "Repaso CCSE: Organización Territorial, Comunidades y Entidades Locales",
        "goal": "Consolidar los conocimientos sobre comunidades autónomas, estatutos, ayuntamientos, diputaciones y cabildos.",
        "track": "cultura",
        "metadata": {
            "estimatedMinutes": 15
        },
        "sections": [
            {
                "type": "exercise-group",
                "title": "Simulacro CCSE: Instituciones Autonómicas y Locales",
                "exerciseRefs": [
                    "ex.b1.ccse.autonomias.inst.consolidation.1",
                    "ex.b1.ccse.autonomias.inst.consolidation.2",
                    "ex.b1.ccse.autonomias.inst.consolidation.3"
                ],
                "content": {
                    "ref": "exercises/b1/b1-ccse-autonomias-inst-consolidation-ex.json"
                }
            }
        ]
    })

    # 2. Vocabulary Files
    voc_data_list = [
        {
            "num": "01",
            "title": "Organización Territorial del Estado",
            "words": [
                {"lemma": "comunidad autónoma", "translation": "autonomous community", "pos": "expression"},
                {"lemma": "solidaridad", "translation": "solidarity / inter-territorial cohesion", "pos": "noun"},
                {"lemma": "autogobierno", "translation": "self-government / regional autonomy", "pos": "noun"},
                {"lemma": "descentralización", "translation": "decentralization", "pos": "noun"},
                {"lemma": "estatuto de autonomía", "translation": "statute of autonomy", "pos": "expression"}
            ]
        },
        {
            "num": "02",
            "title": "Los Estatutos de Autonomía",
            "words": [
                {"lemma": "estatuto", "translation": "statute / charter", "pos": "noun"},
                {"lemma": "norma institucional", "translation": "basic institutional law / standard", "pos": "expression"},
                {"lemma": "delimitación", "translation": "demarcation / boundary definition", "pos": "noun"},
                {"lemma": "transferencia", "translation": "devolution / transfer of powers", "pos": "noun"},
                {"lemma": "ordenamiento", "translation": "legal system / body of laws", "pos": "noun"}
            ]
        },
        {
            "num": "03",
            "title": "Las Instituciones Autonómicas",
            "words": [
                {"lemma": "asamblea legislativa", "translation": "regional legislative assembly / parliament", "pos": "expression"},
                {"lemma": "presidente autonómico", "translation": "regional president", "pos": "expression"},
                {"lemma": "consejero", "translation": "regional minister / cabinet member", "pos": "noun"},
                {"lemma": "consejo de gobierno", "translation": "regional government council", "pos": "expression"},
                {"lemma": "competencia exclusiva", "translation": "exclusive competence / jurisdiction", "pos": "expression"}
            ]
        },
        {
            "num": "04",
            "title": "La Administración Municipal",
            "words": [
                {"lemma": "municipio", "translation": "municipality", "pos": "noun"},
                {"lemma": "ayuntamiento", "translation": "town hall / municipal council", "pos": "noun"},
                {"lemma": "alcalde", "translation": "mayor", "pos": "noun"},
                {"lemma": "concejal", "translation": "town councillor", "pos": "noun"},
                {"lemma": "vecino", "translation": "resident / local citizen", "pos": "noun"}
            ]
        },
        {
            "num": "05",
            "title": "Provincias, Diputaciones e Islas",
            "words": [
                {"lemma": "diputación provincial", "translation": "provincial council", "pos": "expression"},
                {"lemma": "cabildo", "translation": "island council (Canary Islands)", "pos": "noun"},
                {"lemma": "consejo insular", "translation": "island council (Balearic Islands)", "pos": "expression"},
                {"lemma": "uniprovincial", "translation": "single-province (autonomous community)", "pos": "adjective"},
                {"lemma": "corporación", "translation": "corporation / local authority body", "pos": "noun"}
            ]
        }
    ]

    for vd in voc_data_list:
        n = vd["num"]
        stem = f"b1-ccse-autonomias-inst-{n}"
        write_json(f"content/es-es/vocabulary/b1/{stem}-voc.json", {
            "id": f"vocab.b1.ccse.autonomias.inst.{n}",
            "lesson": stem,
            "title": vd["title"],
            "words": vd["words"]
        })

    # 3. Grammar Files
    gr_data_list = [
        {
            "num": "01",
            "title": "Estructuras de distribución y descentralización administrativa",
            "text": "La descripción del mapa territorial español se formula con verbos de estructuración espacial y política ('organizarse en', 'gozar de autonomía', 'garantizar la solidaridad').",
            "examples": [
                {
                    "spanish": "El Estado se organiza territorialmente en municipios, en provincias y en Comunidades Autónomas.",
                    "english": "The State is organized territorially into municipalities, provinces, and Autonomous Communities."
                },
                {
                    "spanish": "Todas las entidades gozan de autonomía para la gestión de sus respectivos intereses.",
                    "english": "All entities enjoy autonomy for the management of their respective interests."
                }
            ],
            "tip": "Dato CCSE: España cuenta con 17 Comunidades Autónomas y 2 Ciudades Autónomas (Ceuta y Melilla, situadas en el norte de África)."
        },
        {
            "num": "02",
            "title": "Fórmulas de obligatoriedad y contenido normativo básico",
            "text": "Los requisitos formales de los textos normativos se estructuran con verbos de obligatoriedad legal ('debe contener', 'deberá incluir', 'formar parte de').",
            "examples": [
                {
                    "spanish": "El Estatuto de Autonomía debe contener la denominación y delimitación territorial de la comunidad.",
                    "english": "The Statute of Autonomy must contain the name and territorial boundaries of the community."
                },
                {
                    "spanish": "Los estatutos forman parte del ordenamiento jurídico del Estado y se aprueban por ley orgánica.",
                    "english": "The statutes form part of the State's legal system and are approved by organic law."
                }
            ],
            "tip": "El Estatuto de Autonomía es la 'norma institucional básica' de cada Comunidad Autónoma en España."
        },
        {
            "num": "03",
            "title": "Verbos de investidura y representación ordinaria del Estado",
            "text": "Para las figuras de autogobierno autonómico se emplean verbos de régimen estatutario ('ostentar la representación', 'ser elegido de entre sus miembros').",
            "examples": [
                {
                    "spanish": "El Presidente autonómico ostenta la suprema representación de la comunidad y la ordinaria del Estado.",
                    "english": "The regional President holds supreme representation of the community and ordinary representation of the State."
                },
                {
                    "spanish": "La asamblea legislativa elige al Presidente de la Comunidad de entre sus diputados.",
                    "english": "The legislative assembly elects the President of the Community from among its members."
                }
            ],
            "tip": "Pregunta CCSE habitual: El Presidente de una Comunidad Autónoma es elegido por su parlamento autonómico y nombrado formalmente por el Rey."
        },
        {
            "num": "04",
            "title": "Léxico de proximidad vecinal y administración municipal",
            "text": "En el régimen local se emplean fórmulas de sufragio vecinal y colegialidad representativa ('ser elegido por los vecinos', 'estar integrado por').",
            "examples": [
                {
                    "spanish": "Los concejales del ayuntamiento son elegidos por los vecinos del municipio.",
                    "english": "The town councillors are elected by the residents of the municipality."
                },
                {
                    "spanish": "El ayuntamiento está presidido por el alcalde y gestiona los servicios públicos básicos.",
                    "english": "The town hall is presided over by the mayor and manages basic public services."
                }
            ],
            "tip": "El gobierno y la administración del municipio corresponden al Ayuntamiento, formado por el Alcalde y los Concejales."
        },
        {
            "num": "05",
            "title": "Estructuras distributivas y excepciones territoriales",
            "text": "Las singularidades territoriales de España se explican con conectores distributivos y comparativos ('mientras que en los archipiélagos', 'en el caso de las comunidades uniprovinciales').",
            "examples": [
                {
                    "spanish": "En las islas Canarias el gobierno insular corresponde a los Cabildos, mientras que en Baleares corresponde a los Consejos Insulares.",
                    "english": "In the Canary Islands island governance belongs to the Cabildos, whereas in the Balearic Islands it belongs to the Island Councils."
                },
                {
                    "spanish": "En las comunidades uniprovinciales como Madrid o Murcia no existe diputación provincial independiente.",
                    "english": "In single-province communities like Madrid or Murcia there is no separate provincial council."
                }
            ],
            "tip": "Órganos insulares CCSE: 'Cabildos' en las islas Canarias; 'Consejos Insulares' (Consells Insulars) en las islas Baleares."
        }
    ]

    for gd in gr_data_list:
        n = gd["num"]
        stem = f"b1-ccse-autonomias-inst-{n}"
        write_json(f"content/es-es/grammar/b1/{stem}-gr.json", {
            "id": f"grammar.b1.ccse.autonomias.inst.{n}",
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
            "stem": "b1-ccse-autonomias-inst-01",
            "exercises": [
                {
                    "id": "ex.b1.ccse.autonomias.inst.01.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuántas Comunidades Autónomas y Ciudades Autónomas componen el Estado español?",
                    "options": [
                        "17 Comunidades Autónomas y 2 Ciudades Autónomas",
                        "15 Comunidades Autónomas y 3 Ciudades Autónomas",
                        "19 Comunidades Autónomas sin ciudades autónomas"
                    ],
                    "correct": 0,
                    "teaches": ["autonomias", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.01.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Las dos Ciudades Autónomas de España situadas en el norte de África son Ceuta y _____.",
                    "answer": "Melilla",
                    "english": "The two Autonomous Cities of Spain situated in North Africa are Ceuta and Melilla.",
                    "teaches": ["autonomias", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.01.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Spanish State is organized into municipalities, provinces and Autonomous Communities.",
                    "tiles": ["España", "se", "organiza", "en", "municipios,", "provincias", "y", "Comunidades", "Autónomas."],
                    "solution": ["España", "se", "organiza", "en", "municipios,", "provincias", "y", "Comunidades", "Autónomas."],
                    "teaches": ["autonomias", "ccse"]
                }
            ]
        },
        {
            "num": "02",
            "stem": "b1-ccse-autonomias-inst-02",
            "exercises": [
                {
                    "id": "ex.b1.ccse.autonomias.inst.02.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la norma institucional básica de cada Comunidad Autónoma en España?",
                    "options": [
                        "El Estatuto de Autonomía",
                        "La Ley de Régimen Local",
                        "La Constitución Autonómica"
                    ],
                    "correct": 0,
                    "teaches": ["estatutos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.02.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los Estatutos de Autonomía deben ser aprobados por las Cortes Generales mediante ley _____.",
                    "answer": "orgánica",
                    "english": "Statutes of Autonomy must be approved by the Cortes Generales through an organic law.",
                    "teaches": ["estatutos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.02.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The Statute of Autonomy is the basic institutional norm of the region.",
                    "tiles": ["El", "Estatuto", "es", "la", "norma", "institucional", "básica", "de", "la", "comunidad."],
                    "solution": ["El", "Estatuto", "es", "la", "norma", "institucional", "básica", "de", "la", "comunidad."],
                    "teaches": ["estatutos", "ccse"]
                }
            ]
        },
        {
            "num": "03",
            "stem": "b1-ccse-autonomias-inst-03",
            "exercises": [
                {
                    "id": "ex.b1.ccse.autonomias.inst.03.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién elige al Presidente de una Comunidad Autónoma en España?",
                    "options": [
                        "La Asamblea Legislativa de la Comunidad Autónoma",
                        "El Presidente del Gobierno de la Nación",
                        "El cuerpo electoral en circunscripción única nacional"
                    ],
                    "correct": 0,
                    "teaches": ["gobierno-autonomico", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.03.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "El Presidente autonómico ostenta la suprema representación de la comunidad y la ordinaria del _____ en ella.",
                    "answer": "Estado",
                    "english": "The regional President holds supreme representation of the community and ordinary representation of the State within it.",
                    "teaches": ["gobierno-autonomico", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.03.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The regional parliament exercises the legislative power of the community.",
                    "tiles": ["El", "parlamento", "autonómico", "ejerce", "la", "potestad", "legislativa", "de", "la", "comunidad."],
                    "solution": ["El", "parlamento", "autonómico", "ejerce", "la", "potestad", "legislativa", "de", "la", "comunidad."],
                    "teaches": ["gobierno-autonomico", "ccse"]
                }
            ]
        },
        {
            "num": "04",
            "stem": "b1-ccse-autonomias-inst-04",
            "exercises": [
                {
                    "id": "ex.b1.ccse.autonomias.inst.04.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué órgano colegiado gobierna y administra el municipio?",
                    "options": [
                        "El Ayuntamiento",
                        "La Diputación Provincial",
                        "El Consejo Comarcal"
                    ],
                    "correct": 0,
                    "teaches": ["ayuntamientos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.04.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Los concejales del Ayuntamiento son elegidos por los _____ del municipio mediante sufragio universal.",
                    "answer": "vecinos",
                    "english": "The town councillors are elected by the residents of the municipality through universal suffrage.",
                    "teaches": ["ayuntamientos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.04.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The town hall is made up of the mayor and the councillors.",
                    "tiles": ["El", "Ayuntamiento", "está", "integrado", "por", "el", "Alcalde", "y", "los", "Concejales."],
                    "solution": ["El", "Ayuntamiento", "está", "integrado", "por", "el", "Alcalde", "y", "los", "Concejales."],
                    "teaches": ["ayuntamientos", "ccse"]
                }
            ]
        },
        {
            "num": "05",
            "stem": "b1-ccse-autonomias-inst-05",
            "exercises": [
                {
                    "id": "ex.b1.ccse.autonomias.inst.05.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cómo se denominan los órganos de gobierno y administración insular en las Islas Canarias?",
                    "options": [
                        "Cabildos",
                        "Consejos Insulares",
                        "Diputaciones Provinciales"
                    ],
                    "correct": 0,
                    "teaches": ["cabildos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.05.2",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "En las Islas Baleares, el gobierno propio de cada isla corresponde a los _____ Insulares.",
                    "answer": "Consejos",
                    "english": "In the Balearic Islands, the governance of each island corresponds to the Island Councils.",
                    "teaches": ["cabildos", "ccse"]
                },
                {
                    "id": "ex.b1.ccse.autonomias.inst.05.3",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "english": "The provincial council coordinates public services among the municipalities.",
                    "tiles": ["La", "Diputación", "Provincial", "coordina", "los", "servicios", "en", "la", "provincia."],
                    "solution": ["La", "Diputación", "Provincial", "coordina", "los", "servicios", "en", "la", "provincia."],
                    "teaches": ["cabildos", "ccse"]
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
    write_json("content/es-es/exercises/b1/b1-ccse-autonomias-inst-consolidation-ex.json", {
        "lesson": "b1-ccse-autonomias-inst-consolidation",
        "exercises": [
            {
                "id": "ex.b1.ccse.autonomias.inst.consolidation.1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién elige al Alcalde en el régimen municipal general en España?",
                "options": [
                    "Los concejales elegidos por los vecinos",
                    "El Presidente de la Diputación Provincial",
                    "El Gobernador Civil de la provincia"
                ],
                "correct": 0,
                "teaches": ["administracion-local", "ccse"]
            },
            {
                "id": "ex.b1.ccse.autonomias.inst.consolidation.2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué entidad local tiene encomendado el gobierno y administración de la provincia?",
                "options": [
                    "La Diputación Provincial",
                    "El Ayuntamiento de la capital",
                    "La Mancomunidad de Municipios"
                ],
                "correct": 0,
                "teaches": ["administracion-local", "ccse"]
            },
            {
                "id": "ex.b1.ccse.autonomias.inst.consolidation.3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿En qué comunidades autónomas no existe Diputación Provincial porque sus funciones las asume la propia comunidad?",
                "options": [
                    "En las comunidades autónomas uniprovinciales (Madrid, Murcia, etc.)",
                    "En todas las comunidades autónomas históricas",
                    "En las comunidades limítrofes con Francia y Portugal"
                ],
                "correct": 0,
                "teaches": ["administracion-local", "ccse"]
            }
        ]
    })

if __name__ == "__main__":
    generate_unit_5()
    generate_unit_6()
    print("Units 5 and 6 generated successfully.")
