#!/usr/bin/env python3
"""Author CCSE Unit 2: La Corona y la Jefatura del Estado for Spanish (Spain) es-es."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DST = ROOT / "content" / "es-es"

unit2_slug = "b1-ccse-monarquia"
lessons_dir = DST / "lessons" / "b1"
exercises_dir = DST / "exercises" / "b1"
vocab_dir = DST / "vocabulary" / "b1"
grammar_dir = DST / "grammar" / "b1"

unit2_lessons = [
    {
        "num": "01",
        "title": "El Rey como Jefe del Estado",
        "goal": "Comprender el papel del Rey como Jefe del Estado y símbolo de la unidad nacional.",
        "grammar": "Verbos de representación y función institucional",
        "ccse_q": "El Rey es el Jefe del Estado, símbolo de su unidad y permanencia.",
        "blank_q": ("El Rey es el Jefe del Estado, símbolo de su unidad y _____.", "permanencia", ["permanencia", "cambio", "división"]),
        "vocab": [
            {"lemma": "rey", "translation": "king", "pos": "noun", "gender": "m"},
            {"lemma": "corona", "translation": "crown", "pos": "noun", "gender": "f"},
            {"lemma": "jefatura", "translation": "headship / leadership", "pos": "noun", "gender": "f"},
            {"lemma": "unidad", "translation": "unity", "pos": "noun", "gender": "f"},
            {"lemma": "permanencia", "translation": "permanence", "pos": "noun", "gender": "f"}
        ]
    },
    {
        "num": "02",
        "title": "Funciones Constitucionales del Rey",
        "goal": "Aprender las principales funciones regias: sancionar leyes y convocar elecciones.",
        "grammar": "Perífrasis y verbos de acción legislativa",
        "ccse_q": "Al Rey le corresponde sancionar y promulgar las leyes aprobadas por las Cortes Generales.",
        "blank_q": ("Al Rey le corresponde _____ y promulgar las leyes.", "sancionar", ["sancionar", "redactar", "vetar"]),
        "vocab": [
            {"lemma": "sancionar", "translation": "to sanction / approve officially", "pos": "verb"},
            {"lemma": "promulgar", "translation": "to promulgate / enact", "pos": "verb"},
            {"lemma": "convocar", "translation": "to convene / call (elections)", "pos": "verb"},
            {"lemma": "disolver", "translation": "to dissolve", "pos": "verb"},
            {"lemma": "nombramiento", "translation": "appointment", "pos": "noun", "gender": "m"}
        ]
    },
    {
        "num": "03",
        "title": "Inviolabilidad y Refrendo",
        "goal": "Conocer la condición de inviolabilidad de la Corona y la institución del refrendo.",
        "grammar": "Estructuras pasivas y de responsabilidad jurídica",
        "ccse_q": "La persona del Rey es inviolable y no está sujeta a responsabilidad; sus actos son refrendados.",
        "blank_q": ("La persona del Rey es _____ y no está sujeta a responsabilidad.", "inviolable", ["inviolable", "electa", "reemplazable"]),
        "vocab": [
            {"lemma": "inviolable", "translation": "inviolable", "pos": "adjective"},
            {"lemma": "responsabilidad", "translation": "responsibility / liability", "pos": "noun", "gender": "f"},
            {"lemma": "refrendo", "translation": "countersignature / endorsement", "pos": "noun", "gender": "m"},
            {"lemma": "refrendar", "translation": "to countersign / endorse", "pos": "verb"},
            {"lemma": "ministro", "translation": "minister", "pos": "noun", "gender": "m"}
        ]
    },
    {
        "num": "04",
        "title": "La Sucesión en la Corona",
        "goal": "Entender las reglas de sucesión dinástica y el título del heredero o heredera de la Corona.",
        "grammar": "Oraciones de relativo y líneas sucesorias",
        "ccse_q": "La Corona de España es hereditaria en los sucesores de Don Juan Carlos I de Borbón.",
        "blank_q": ("La Corona de España es _____ en los sucesores legítimos.", "hereditaria", ["hereditaria", "rotativa", "temporal"]),
        "vocab": [
            {"lemma": "hereditario", "translation": "hereditary", "pos": "adjective", "gender": "m"},
            {"lemma": "sucesor", "translation": "successor", "pos": "noun", "gender": "m"},
            {"lemma": "heredero", "translation": "heir", "pos": "noun", "gender": "m"},
            {"lemma": "príncipe", "translation": "prince", "pos": "noun", "gender": "m"},
            {"lemma": "princesa", "translation": "princess", "pos": "noun", "gender": "f"}
        ]
    },
    {
        "num": "05",
        "title": "Mando Supremo de las Fuerzas Armadas",
        "goal": "Conocer las competencias regias en materia militar y relaciones internacionales.",
        "grammar": "Léxico de mando y representación exterior",
        "ccse_q": "El Rey ostenta el mando supremo de las Fuerzas Armadas.",
        "blank_q": ("El Rey ostenta el mando supremo de las Fuerzas _____.", "Armadas", ["Armadas", "Policiales", "Municipales"]),
        "vocab": [
            {"lemma": "mando", "translation": "command", "pos": "noun", "gender": "m"},
            {"lemma": "supremo", "translation": "supreme", "pos": "adjective", "gender": "m"},
            {"lemma": "ejército", "translation": "army", "pos": "noun", "gender": "m"},
            {"lemma": "embajador", "translation": "ambassador", "pos": "noun", "gender": "m"},
            {"lemma": "tratado", "translation": "treaty", "pos": "noun", "gender": "m"}
        ]
    }
]

def main():
    print("Authoring CCSE Unit 2 (La Corona y la Jefatura del Estado)...")
    
    for item in unit2_lessons:
        stem = f"{unit2_slug}-{item['num']}"
        lesson_id = f"lesson.{stem.replace('-', '.')}"
        voc_id = f"voc.{stem.replace('-', '.')}"
        gr_id = f"gr.{stem.replace('-', '.')}"
        ex_id = f"ex.{stem.replace('-', '.')}"

        # 1. Vocab file
        voc_data = {
            "id": voc_id,
            "lesson": stem,
            "title": item["title"],
            "words": item["vocab"]
        }
        with open(vocab_dir / f"{stem}-voc.json", "w", encoding="utf-8") as f:
            json.dump(voc_data, f, indent=2, ensure_ascii=False)

        # 2. Grammar file
        gr_data = {
            "id": gr_id,
            "title": item["grammar"],
            "sections": [
                {
                    "type": "text",
                    "content": f"En este tema analizamos: {item['grammar']}. Aplicado a la Jefatura del Estado y el examen CCSE."
                },
                {
                    "type": "examples",
                    "items": [
                        {
                            "spanish": item["ccse_q"],
                            "english": f"Official CCSE premise: {item['title']}"
                        }
                    ]
                }
            ]
        }
        with open(grammar_dir / f"{stem}-gr.json", "w", encoding="utf-8") as f:
            json.dump(gr_data, f, indent=2, ensure_ascii=False)

        # 3. Exercise file
        words = item["ccse_q"].rstrip(".").split()
        b_sent, b_ans, b_opts = item["blank_q"]
        ex_data = {
            "id": ex_id,
            "exercises": [
                {
                    "id": f"{ex_id}.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": f"¿Qué establece la Constitución Española sobre: {item['title']}?",
                    "options": [item["ccse_q"], "Es elegido cada cuatro años por sufragio universal.", "El cargo no existe en la Constitución."],
                    "answer": item["ccse_q"],
                    "explanation": f"Pregunta oficial del banco CCSE: {item['ccse_q']}",
                    "teaches": ["monarquia", "ccse"]
                },
                {
                    "id": f"{ex_id}.2",
                    "type": "fill-in-blank",
                    "category": "grammar",
                    "sentence": b_sent,
                    "answer": b_ans,
                    "options": b_opts,
                    "explanation": f"Respuesta correcta CCSE: {b_ans}.",
                    "teaches": ["monarquia", "constitucion"]
                },
                {
                    "id": f"{ex_id}.3",
                    "type": "sentence-builder",
                    "category": "syntax",
                    "english": f"Official CCSE premise: {item['title']}",
                    "solution": words + ["."],
                    "pool": words + [".", "gobierno", "presidente"],
                    "teaches": ["monarquia", "ccse"]
                }
            ]
        }
        with open(exercises_dir / f"{stem}-ex.json", "w", encoding="utf-8") as f:
            json.dump(ex_data, f, indent=2, ensure_ascii=False)

        # 4. Lesson file
        lesson_data = {
            "id": lesson_id,
            "level": "b1",
            "title": item["title"],
            "grammar": item["grammar"],
            "goal": item["goal"],
            "track": "cultura",
            "metadata": {
                "estimatedMinutes": 12
            },
            "sections": [
                {
                    "type": "vocabulary",
                    "title": "Vocabulario Cívico",
                    "content": {
                        "ref": f"vocabulary/b1/{stem}-voc.json"
                    }
                },
                {
                    "type": "grammar",
                    "title": item["grammar"],
                    "content": {
                        "ref": f"grammar/b1/{stem}-gr.json"
                    }
                },
                {
                    "type": "exercise-group",
                    "title": "Práctica y Preguntas CCSE",
                    "exerciseRefs": [
                        f"{ex_id}.1",
                        f"{ex_id}.2"
                    ],
                    "content": {
                        "ref": f"exercises/b1/{stem}-ex.json"
                    }
                }
            ]
        }
        with open(lessons_dir / f"{stem}.json", "w", encoding="utf-8") as f:
            json.dump(lesson_data, f, indent=2, ensure_ascii=False)

    # 5. Consolidation lesson and exercise
    cons_stem = f"{unit2_slug}-consolidation"
    cons_lesson_id = f"lesson.{cons_stem.replace('-', '.')}"
    cons_ex_id = f"ex.{cons_stem.replace('-', '.')}"

    cons_ex_data = {
        "id": cons_ex_id,
        "exercises": [
            {
                "id": f"{cons_ex_id}.1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién ostenta el mando supremo de las Fuerzas Armadas en España?",
                "options": ["El Rey", "El Ministro de Defensa", "El Presidente del Gobierno"],
                "answer": "El Rey",
                "explanation": "Según el artículo 62 de la Constitución, al Rey le corresponde el mando supremo de las Fuerzas Armadas.",
                "teaches": ["monarquia", "ccse"]
            },
            {
                "id": f"{cons_ex_id}.2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién refrenda los actos del Rey?",
                "options": ["El Presidente del Gobierno y, en su caso, los ministros competentes", "El Tribunal Constitucional", "El Defensor del Pueblo"],
                "answer": "El Presidente del Gobierno y, en su caso, los ministros competentes",
                "explanation": "Los actos del Rey son siempre refrendados por el Presidente del Gobierno o los ministros.",
                "teaches": ["monarquia", "ccse"]
            }
        ]
    }
    with open(exercises_dir / f"{cons_stem}-ex.json", "w", encoding="utf-8") as f:
        json.dump(cons_ex_data, f, indent=2, ensure_ascii=False)

    cons_lesson_data = {
        "id": cons_lesson_id,
        "level": "b1",
        "title": "La Corona y la Jefatura del Estado — Consolidación",
        "grammar": "Repaso CCSE: La Corona y la Jefatura del Estado",
        "goal": "Consolidar los conocimientos sobre el papel del Rey, la sucesión y el refrendo.",
        "track": "cultura",
        "metadata": {
            "estimatedMinutes": 15
        },
        "sections": [
            {
                "type": "exercise-group",
                "title": "Simulacro CCSE: La Corona",
                "exerciseRefs": [
                    f"{cons_ex_id}.1",
                    f"{cons_ex_id}.2"
                ],
                "content": {
                    "ref": f"exercises/b1/{cons_stem}-ex.json"
                }
            }
        ]
    }
    with open(lessons_dir / f"{cons_stem}.json", "w", encoding="utf-8") as f:
        json.dump(cons_lesson_data, f, indent=2, ensure_ascii=False)

    print("Unit 2 authored successfully!")

if __name__ == "__main__":
    main()
