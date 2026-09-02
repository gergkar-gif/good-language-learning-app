#!/usr/bin/env python3
"""
Build a lemma -> lesson id reverse index: "which lesson taught this word?"

Powers the Tier 2 cross-links (Decks' word-list rows, the Reader's word-tap
popup) that point a word back to where it was first taught, the same way
scripts/build_grammar_index.py already powers Workshop's Grammar Driller by
skill. Neither Decks nor the Reader otherwise has any notion of "which
lesson" a word belongs to — an SRS card only remembers which deck it came
from (see engine/decks.js's addWordToDeck()), never a lesson.

A word can genuinely be taught more than once (checked directly: 138
Hungarian lemmas appear in 2+ vocabulary files, e.g. a word reinforced in a
later unit) — the FIRST lesson in course order wins, since "where did I
learn this" should mean where a learner first met it, not every later
reappearance. That's why this walks curriculum.json's actual level -> unit
-> lesson order rather than globbing vocabulary/*.json and sorting
filenames: Hungarian's lesson numbers aren't zero-padded past 2 digits
(a1-99 vs a1-100), so a plain filename sort would silently put lesson 100
before lesson 99 -- curriculum.json's authored order is the only source of
truth for "first".

Output: content/<lang>/indexes/word-lesson-index.json
    { "byLemma": { "<lemma>": "<lesson id>" } }

Deliberately minimal — no cached title/level, just the lesson id. The
consumer resolves title/unit from window._curriculumData, already loaded
everywhere, so a lesson rename can never leave a stale title sitting in
this index (same reasoning as every other generated index in this repo).

Usage:
    python scripts/build_word_lesson_index.py [lang ...]   (default: es hu)
"""
import json
import sys
from pathlib import Path


# Same level -> unit -> lesson order every other index/screen in this app
# already walks (see LEVEL_ORDER in engine/curriculum.js).
LEVEL_ORDER = ["A1", "A2", "B1", "B2", "C1"]


def lesson_file_path(lesson_id, lang):
    """'lesson.a1.23' -> lessons/a1/a1-23.json ; 'lesson.a1.01.05' ->
    lessons/a1/a1-01-05.json. Same level/rest split loadLesson() in
    engine/lessons.js and exerciseRefFor() in engine/home.js already use."""
    parts = lesson_id[len("lesson."):].split(".") if lesson_id.startswith("lesson.") else lesson_id.split(".")
    level = parts[0]
    rest = "-".join(parts[1:])
    return Path(f"content/{lang}/lessons/{level}/{level}-{rest}.json")


def build_index(lang):
    curriculum_path = Path(f"content/{lang}/curriculum/curriculum.json")
    if not curriculum_path.is_file():
        return None, {"lessons": 0, "vocab_files": 0, "lemmas": 0, "errors": 0}

    curriculum = json.loads(curriculum_path.read_text(encoding="utf-8"))
    levels = curriculum.get("levels", {})

    by_lemma = {}
    stats = {"lessons": 0, "vocab_files": 0, "lemmas": 0, "errors": 0}

    for level_key in LEVEL_ORDER:
        level = levels.get(level_key)
        if not level:
            continue
        for unit in level.get("units", []):
            for lesson in unit.get("lessons", []):
                lesson_id = lesson.get("id")
                if not lesson_id:
                    continue
                stats["lessons"] += 1

                lesson_path = lesson_file_path(lesson_id, lang)
                try:
                    lesson_data = json.loads(lesson_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    stats["errors"] += 1
                    continue

                for section in lesson_data.get("sections", []):
                    if section.get("type") != "vocabulary":
                        continue
                    voc_ref = section.get("ref")
                    if not voc_ref:
                        continue
                    voc_path = Path(f"content/{lang}") / voc_ref
                    try:
                        voc_data = json.loads(voc_path.read_text(encoding="utf-8"))
                    except (OSError, json.JSONDecodeError):
                        stats["errors"] += 1
                        continue
                    stats["vocab_files"] += 1

                    for word in voc_data.get("words", []):
                        lemma = word.get("lemma")
                        if not lemma or lemma in by_lemma:
                            continue
                        by_lemma[lemma] = lesson_id
                        stats["lemmas"] += 1

    return {"byLemma": by_lemma}, stats


def main():
    langs = sys.argv[1:] or ["es", "hu"]

    for lang in langs:
        if not Path(f"content/{lang}").is_dir():
            print(f"[{lang}] no content dir, skipping")
            continue

        index, stats = build_index(lang)
        if index is None:
            print(f"[{lang}] no curriculum.json, skipping")
            continue

        output_dir = Path(f"content/{lang}/indexes")
        output_file = output_dir / "word-lesson-index.json"
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

        raw_size = output_file.stat().st_size
        print(f"[{lang}] Lessons walked:     {stats['lessons']} (errors: {stats['errors']})")
        print(f"[{lang}] Vocabulary files:   {stats['vocab_files']}")
        print(f"[{lang}] Distinct lemmas:    {stats['lemmas']}")
        print(f"[{lang}] Output:             {output_file} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
