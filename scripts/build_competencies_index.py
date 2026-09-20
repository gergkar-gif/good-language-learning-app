#!/usr/bin/env python3
"""
Build the flat CEFR "I can..." competency list My Journey's Can-Do Passport
reads (engine/learnerModel.js's loadCompetenciesIndex(), engine/journey.js's
can-do portfolio card).

Walks content/<lang>/curriculum/curriculum.json's units -> lessons, loads
each lesson's own content file, and pulls the "I can..." lines from its
`checklist`-type step (the same items a `goal`-type step shows at the start
of the lesson, restated at the end) — no new content to author, this is a
mechanical extraction of what's already in every lesson.

A lesson id like "lesson.a1.01" maps to content/<lang>/lessons/a1/a1-01.json
(level = the id's second segment, filename = the id with "lesson." stripped
and remaining dots turned into dashes). A lesson whose file doesn't exist at
that path, or has no checklist step, is skipped and counted, not treated as
an error — some lesson types (e.g. pure consolidation/review) may not carry
their own checklist.

Output: content/<lang>/indexes/competencies-index.json
    [ { id, text, lessonId, lessonTitle, level, unitId, unitLabel, unitTitle }, ... ]

Usage:
    python scripts/build_competencies_index.py [lang ...]   (default: es hu)
"""
import json
import sys
from pathlib import Path


def lesson_path(lang, lesson_id):
    # "lesson.a1.01" -> level "a1", filename "a1-01.json"
    parts = lesson_id.split(".")
    if len(parts) < 3 or parts[0] != "lesson":
        return None
    level = parts[1]
    filename = "-".join(parts[1:]) + ".json"
    return Path(f"content/{lang}/lessons/{level}/{filename}")


def build_index(lang):
    curriculum_path = Path(f"content/{lang}/curriculum/curriculum.json")
    if not curriculum_path.is_file():
        return None, None

    curriculum = json.loads(curriculum_path.read_text(encoding="utf-8"))
    levels = curriculum.get("levels", {})
    units = [u for level in levels.values() for u in level.get("units", [])]

    entries = []
    stats = {"units": 0, "lessons": 0, "missing_file": 0, "no_checklist": 0, "items": 0}

    for unit in units:
        lessons = unit.get("lessons", [])
        if not lessons:
            continue
        stats["units"] += 1
        unit_id = unit.get("id", "")
        unit_label = unit.get("label", "")
        unit_title = unit.get("title", "")

        for lesson_ref in lessons:
            lesson_id = lesson_ref.get("id", "")
            stats["lessons"] += 1
            path = lesson_path(lang, lesson_id)
            if not path or not path.is_file():
                stats["missing_file"] += 1
                continue

            try:
                lesson_data = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                stats["missing_file"] += 1
                continue

            checklist_items = []
            for section in lesson_data.get("sections", []):
                if section.get("type") == "checklist":
                    checklist_items = section.get("items", [])
                    break

            if not checklist_items:
                stats["no_checklist"] += 1
                continue

            lesson_title = lesson_data.get("title", lesson_ref.get("title", ""))
            level = lesson_data.get("level", unit_id.split(".")[1].upper() if "." in unit_id else "")

            for i, text in enumerate(checklist_items, start=1):
                entries.append({
                    "id": f"{lesson_id}.c{i}",
                    "text": text,
                    "lessonId": lesson_id,
                    "lessonTitle": lesson_title,
                    "level": level,
                    "unitId": unit_id,
                    "unitLabel": unit_label,
                    "unitTitle": unit_title
                })
                stats["items"] += 1

    return entries, stats


def main():
    langs = sys.argv[1:] or ["es-latam", "es-es", "hu"]

    for lang in langs:
        entries, stats = build_index(lang)
        if entries is None:
            print(f"[{lang}] no curriculum.json, skipping")
            continue

        output_dir = Path(f"content/{lang}/indexes")
        output_file = output_dir / "competencies-index.json"
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))

        raw_size = output_file.stat().st_size
        print(f"[{lang}] Units: {stats['units']}, Lessons: {stats['lessons']} "
              f"(missing file: {stats['missing_file']}, no checklist: {stats['no_checklist']})")
        print(f"[{lang}] Competency items: {stats['items']}")
        print(f"[{lang}] Output: {output_file} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
