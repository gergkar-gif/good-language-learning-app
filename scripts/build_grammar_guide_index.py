#!/usr/bin/env python3
"""
Build a flat, course-wide index of every grammar topic for the Grammar
Guide's global search (engine/curriculum.js's globalGrammarGuideHtml()).

Walking every unit's lessons live in the browser (collectUnitGrammarTopics())
is exactly what the per-unit Grammar Guide already does, and is fine at that
scale (~6 lessons). Doing it for every unit in the whole course on every
search-screen open is not: a full course runs to 100+ units, each with its
own lesson + grammar-section fetches, which fans out to hundreds of
individual requests. This script does that walk once at build time instead,
mirroring loadLesson()'s id -> path resolution (engine/lessons.js) and
collectUnitGrammarTopics()'s section-walk (engine/curriculum.js) exactly, so
the two never teach a different topic list for the same unit.

Output: content/<lang>/indexes/grammar-guide-index.json
    [ { "level": "A1", "unitId": "unit.a1.01", "unitTitle": "...",
        "title": "..." }, ... ]

Usage:
    python scripts/build_grammar_guide_index.py [lang ...]   (default: es hu)
"""
import json
import sys
from pathlib import Path


def lesson_path(lang, lesson_id):
    # Mirrors loadLesson() in engine/lessons.js exactly.
    parts = lesson_id[len("lesson."):].split(".") if lesson_id.startswith("lesson.") else lesson_id.split(".")
    level = parts[0]
    rest = "-".join(parts[1:])
    return Path(f"content/{lang}/lessons/{level}/{level}-{rest}.json")


def build_index(lang, curriculum):
    index = []
    stats = {"units": 0, "lessons_missing": 0, "grammar_missing": 0}

    for level_key, level_data in curriculum.get("levels", {}).items():
        for unit in level_data.get("units", []):
            stats["units"] += 1
            for lesson_ref in unit.get("lessons", []):
                lf = lesson_path(lang, lesson_ref["id"])
                if not lf.is_file():
                    stats["lessons_missing"] += 1
                    continue
                try:
                    lesson = json.loads(lf.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, OSError):
                    stats["lessons_missing"] += 1
                    continue

                for section in lesson.get("sections", []):
                    if section.get("type") != "grammar" or not section.get("ref"):
                        continue
                    gf = Path(f"content/{lang}") / section["ref"]
                    title = section.get("title", "Grammar")
                    if gf.is_file():
                        try:
                            grammar = json.loads(gf.read_text(encoding="utf-8"))
                            title = grammar.get("title") or title
                        except (json.JSONDecodeError, OSError):
                            stats["grammar_missing"] += 1
                    else:
                        stats["grammar_missing"] += 1

                    index.append({
                        "level": level_key,
                        "unitId": unit["id"],
                        "unitTitle": unit.get("title", ""),
                        "title": title
                    })

    return index, stats


def main():
    langs = sys.argv[1:] or sorted(p.name for p in Path("content").iterdir() if p.is_dir())  # every course folder

    for lang in langs:
        curriculum_path = Path(f"content/{lang}/curriculum/curriculum.json")
        if not curriculum_path.is_file():
            print(f"[{lang}] no curriculum.json, skipping")
            continue

        curriculum = json.loads(curriculum_path.read_text(encoding="utf-8"))
        index, stats = build_index(lang, curriculum)

        output_dir = Path(f"content/{lang}/indexes")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / "grammar-guide-index.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

        print(f"[{lang}] {len(index)} grammar topics across {stats['units']} units "
              f"-> {output_file} ({output_file.stat().st_size} bytes)"
              + (f"  [{stats['lessons_missing']} lessons, {stats['grammar_missing']} grammar files unresolved]"
                 if stats["lessons_missing"] or stats["grammar_missing"] else ""))


if __name__ == "__main__":
    main()
