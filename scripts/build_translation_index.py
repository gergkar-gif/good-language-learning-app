#!/usr/bin/env python3
"""
Build a Spanish/English sentence-pair pool for Workshop's Translation Driller
(and the Context mode of the Vocabulary Driller, which samples the same pool
for sentences containing a given word).

Two sources, both already authored for other purposes:
  - content/es/grammar/**/*.json  -- every `examples` part's {spanish, english}
    pairs (the worked examples on a grammar screen).
  - content/es/exercises/**/*.json -- `sentence-builder` exercises that carry
    an `english` field (most of them do; a few omit it and are skipped).

Output: generated/indexes/translation-index.json
    { "pairs": [ { spanish, english, level, source }, ... ] }

`level` is the a1/a2/... directory each file already lives in -- content is
organised one directory per level, so no per-file field to read.

Usage:
    python scripts/build_translation_index.py
"""
import json
from pathlib import Path

GRAMMAR_DIR = Path("content/es/grammar")
EXERCISES_DIR = Path("content/es/exercises")
OUTPUT_DIR = Path("generated/indexes")
OUTPUT_FILE = OUTPUT_DIR / "translation-index.json"


def from_grammar():
    pairs = []
    for f in sorted(GRAMMAR_DIR.glob("*/*.json")):
        level = f.parent.name.upper()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for section in data.get("sections", []):
            if section.get("type") != "examples":
                continue
            for item in section.get("items", []):
                spanish = item.get("spanish")
                english = item.get("english")
                if spanish and english:
                    pairs.append({"spanish": spanish, "english": english, "level": level, "source": "grammar"})
    return pairs


def from_exercises():
    pairs = []
    for f in sorted(EXERCISES_DIR.glob("*/*.json")):
        level = f.parent.name.upper()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for ex in data.get("exercises", []):
            if ex.get("type") != "sentence-builder":
                continue
            english = ex.get("english")
            solution = ex.get("solution")
            if english and solution:
                pairs.append({"spanish": " ".join(solution), "english": english, "level": level, "source": "exercises"})
    return pairs


def main():
    pairs = from_grammar() + from_exercises()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"pairs": pairs}, f, ensure_ascii=False, separators=(",", ":"))

    by_level = {}
    for p in pairs:
        by_level[p["level"]] = by_level.get(p["level"], 0) + 1

    raw_size = OUTPUT_FILE.stat().st_size
    print(f"Pairs total:  {len(pairs)}")
    print(f"By level:     {dict(sorted(by_level.items()))}")
    print(f"Output:       {OUTPUT_FILE} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
