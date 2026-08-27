#!/usr/bin/env python3
"""
Build a Spanish/English sentence-pair pool for Workshop's Translation Driller
(and the Context mode of the Vocabulary Driller, which samples the same pool
for sentences containing a given word).

Two sources, both already authored for other purposes:
  - content/<lang>/grammar/**/*.json  -- every `examples` part's
    {spanish, english} pairs (the worked examples on a grammar screen; the
    "spanish" key just means "target language" — reused as-is for Hungarian).
  - content/<lang>/exercises/**/*.json -- `sentence-builder` exercises that
    carry an `english` field (most of them do; a few omit it and are
    skipped).

Output: content/<lang>/indexes/translation-index.json
    { "pairs": [ { spanish, english, level, source }, ... ] }

`level` is the a1/a2/... directory each file already lives in -- content is
organised one directory per level, so no per-file field to read.

Usage:
    python scripts/build_translation_index.py [lang ...]   (default: es hu)
"""
import json
import re
import sys
from pathlib import Path

_PUNCTUATION_TILE = re.compile(r"^[,.!?;:]+$")


def _join_tiles(tiles):
    """Join sentence-builder tiles into one sentence. A tile that's pure
    punctuation (",", ".", "?", ...) attaches directly to the previous word
    instead of getting its own leading space — plain " ".join(tiles) used to
    produce "Tegnap tanultam ." for any exercise that tiles punctuation
    separately, which most Hungarian ones do."""
    out = []
    for tile in tiles:
        if out and _PUNCTUATION_TILE.match(tile):
            out[-1] += tile
        else:
            out.append(tile)
    return " ".join(out)


def from_grammar(grammar_dir):
    pairs = []
    for f in sorted(grammar_dir.glob("*/*.json")):
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


def from_exercises(exercises_dir):
    pairs = []
    for f in sorted(exercises_dir.glob("*/*.json")):
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
                pairs.append({"spanish": _join_tiles(solution), "english": english, "level": level, "source": "exercises"})
    return pairs


def main():
    langs = sys.argv[1:] or ["es", "hu"]

    for lang in langs:
        grammar_dir = Path(f"content/{lang}/grammar")
        exercises_dir = Path(f"content/{lang}/exercises")
        if not grammar_dir.is_dir() and not exercises_dir.is_dir():
            print(f"[{lang}] no grammar/exercises dirs, skipping")
            continue

        pairs = from_grammar(grammar_dir) + from_exercises(exercises_dir)

        output_dir = Path(f"content/{lang}/indexes")
        output_file = output_dir / "translation-index.json"
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"pairs": pairs}, f, ensure_ascii=False, separators=(",", ":"))

        by_level = {}
        for p in pairs:
            by_level[p["level"]] = by_level.get(p["level"], 0) + 1

        raw_size = output_file.stat().st_size
        print(f"[{lang}] Pairs total:  {len(pairs)}")
        print(f"[{lang}] By level:     {dict(sorted(by_level.items()))}")
        print(f"[{lang}] Output:       {output_file} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
