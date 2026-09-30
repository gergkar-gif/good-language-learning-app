#!/usr/bin/env python3
"""
fix_consolidation_exercise_types.py
-------------------------------------
Adds two fill-blank exercises to each consolidation exercise file that
currently only has 4 distinct types (dialogue-complete, matching,
multiple-choice, structured-writing), bringing them to 5+ types.

Also appends the new exercise IDs to the corresponding lesson file's
exerciseRefs list.

Each pair of fill-blank exercises is topic-specific to the unit.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
EX_DIR = ROOT / "content" / "es" / "exercises" / "a1"
LESSON_DIR = ROOT / "content" / "es" / "lessons" / "a1"

# New fill-blank exercises per lesson.
# format: (exercise_file_base, lesson_file_base, [new_exercises])
NEW_EXERCISES = {
    "a1-07-consolidation": {
        "teaches_context": ["home", "hay", "estar"],
        "exercises": [
            {
                "id": "a1.07.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "En mi casa _____ tres habitaciones. (there is/are)",
                "answer": "hay",
                "teaches": ["hay"]
            },
            {
                "id": "a1.07.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "El sofá _____ en la sala. (estar — 3rd person sing.)",
                "answer": "está",
                "teaches": ["estar"]
            },
        ],
    },
    "a1-08-consolidation": {
        "exercises": [
            {
                "id": "a1.08.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "_____ comprar pan en la tienda. (I want — querer)",
                "answer": "Quiero",
                "teaches": ["querer"]
            },
            {
                "id": "a1.08.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "¿Cuánto _____ las manzanas? (cost — costar, 3rd person plural)",
                "answer": "cuestan",
                "teaches": ["numbers-prices"]
            },
        ],
    },
    "a1-12-consolidation": {
        "exercises": [
            {
                "id": "a1.12.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Son las tres y _____ de la tarde. (half)",
                "answer": "media",
                "teaches": ["telling-time"]
            },
            {
                "id": "a1.12.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "El tren llega _____ las nueve. (at — time preposition)",
                "answer": "a",
                "teaches": ["schedule"]
            },
        ],
    },
    "a1-20-consolidation": {
        "exercises": [
            {
                "id": "a1.20.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Mañana _____ viajar en tren. (we have to — tener que)",
                "answer": "tenemos que",
                "teaches": ["tener-que"]
            },
            {
                "id": "a1.20.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "El vuelo _____ a las seis de la mañana. (to leave — salir, 3rd sing.)",
                "answer": "sale",
                "teaches": ["travel"]
            },
        ],
    },
    "a1-cafe-consolidation": {
        "exercises": [
            {
                "id": "a1.cafe.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "_____ un café con leche, por favor. (I would like — querer, 1st sing.)",
                "answer": "Quiero",
                "teaches": ["querer"]
            },
            {
                "id": "a1.cafe.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Ella _____ un bocadillo en la barra. (eat — comer, 3rd sing.)",
                "answer": "come",
                "teaches": ["comer"]
            },
        ],
    },
    "a1-directions-consolidation": {
        "exercises": [
            {
                "id": "a1.directions.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "El banco _____ a la derecha de la farmacia. (estar — 3rd sing.)",
                "answer": "está",
                "teaches": ["directions"]
            },
            {
                "id": "a1.directions.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "_____ todo recto y luego gira a la izquierda. (Go — tú command of ir)",
                "answer": "Ve",
                "teaches": ["directions"]
            },
        ],
    },
    "a1-future-consolidation": {
        "exercises": [
            {
                "id": "a1.future.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Esta tarde _____ a estudiar en la biblioteca. (I am going — ir a, 1st sing.)",
                "answer": "voy",
                "teaches": ["ir-a-infinitivo"]
            },
            {
                "id": "a1.future.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "_____ que terminar el trabajo antes del viernes. (we have to — tener que, 1st plural)",
                "answer": "Tenemos",
                "teaches": ["tener-que"]
            },
        ],
    },
    "a1-health-consolidation": {
        "exercises": [
            {
                "id": "a1.health.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Me _____ la cabeza. Tengo dolor de cabeza. (hurt — doler, 3rd sing.)",
                "answer": "duele",
                "teaches": ["doler"]
            },
            {
                "id": "a1.health.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Ella _____ fiebre y necesita descansar. (have — tener, 3rd sing.)",
                "answer": "tiene",
                "teaches": ["tener-expressions"]
            },
        ],
    },
    "a1-hobbies-consolidation": {
        "exercises": [
            {
                "id": "a1.hobbies.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Los fines de semana me _____ leer libros. (like — gustar, 3rd sing.)",
                "answer": "gusta",
                "teaches": ["gustar"]
            },
            {
                "id": "a1.hobbies.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Nosotros _____ al fútbol todos los sábados. (play — jugar, 1st plural)",
                "answer": "jugamos",
                "teaches": ["hobbies"]
            },
        ],
    },
    "a1-kitchen-consolidation": {
        "exercises": [
            {
                "id": "a1.kitchen.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "_____ el horno a 200 grados, por favor. (Put on / turn on — encender, tú command)",
                "answer": "Enciende",
                "teaches": ["imperativo"]
            },
            {
                "id": "a1.kitchen.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Hay una sartén y un cuchillo en la _____. (kitchen)",
                "answer": "cocina",
                "teaches": ["kitchen-vocab"]
            },
        ],
    },
    "a1-weather-consolidation": {
        "exercises": [
            {
                "id": "a1.weather.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Hoy _____ mucho viento en la ciudad. (there is — hay)",
                "answer": "hay",
                "teaches": ["weather"]
            },
            {
                "id": "a1.weather.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Cuando _____ frío, me pongo un abrigo. (it is — hacer, 3rd sing.)",
                "answer": "hace",
                "teaches": ["weather"]
            },
        ],
    },
    "a1-work-consolidation": {
        "exercises": [
            {
                "id": "a1.work.06.ex19",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "Ella _____ que entregar el informe mañana. (have to — tener que, 3rd sing.)",
                "answer": "tiene",
                "teaches": ["tener-que"]
            },
            {
                "id": "a1.work.06.ex20",
                "category": "grammar",
                "type": "fill-blank",
                "sentence": "_____ que llegar puntual al trabajo. (It is necessary — hay que)",
                "answer": "Hay",
                "teaches": ["hay-que"]
            },
        ],
    },
}


def add_exercises(lesson_key, spec):
    ex_path = EX_DIR / (lesson_key + "-ex.json")
    lesson_path = LESSON_DIR / (lesson_key + ".json")

    if not ex_path.exists():
        print(f"  MISS {lesson_key} exercise file")
        return
    if not lesson_path.exists():
        print(f"  MISS {lesson_key} lesson file")
        return

    new_exs = spec["exercises"]
    new_ids = [e["id"] for e in new_exs]

    # Update exercise file - add or update exercises
    ex_text = ex_path.read_text(encoding="utf-8")
    ex_data = json.loads(ex_text)
    existing_by_id = {e["id"]: i for i, e in enumerate(ex_data["exercises"])}
    added = 0
    updated = 0
    for ex in new_exs:
        if ex["id"] not in existing_by_id:
            ex_data["exercises"].append(ex)
            added += 1
        else:
            idx = existing_by_id[ex["id"]]
            ex_data["exercises"][idx] = ex
            updated += 1
    if added or updated:
        ex_path.write_text(json.dumps(ex_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Update lesson file - add new IDs to the Review exerciseRefs
    lesson_text = lesson_path.read_text(encoding="utf-8")
    lesson_data = json.loads(lesson_text)
    changed = False
    for section in lesson_data.get("sections", []):
        if section.get("type") == "exercise-group" and section.get("title") == "Review":
            existing_refs = section.get("exerciseRefs", [])
            for eid in new_ids:
                if eid not in existing_refs:
                    existing_refs.append(eid)
                    changed = True
            section["exerciseRefs"] = existing_refs
    if changed:
        lesson_path.write_text(json.dumps(lesson_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"  FIX  {lesson_key} -- added {added} exercises to ex file, {sum(1 for e in new_ids)} refs to lesson")


def main():
    for lesson_key, spec in NEW_EXERCISES.items():
        add_exercises(lesson_key, spec)


if __name__ == "__main__":
    main()
