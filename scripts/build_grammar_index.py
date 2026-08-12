#!/usr/bin/env python3
"""
Build a skill -> exercise lookup for Workshop's Grammar Driller.

content/es/exercises/**/*.json holds every lesson's exercises inline, each
tagged with the grammar/vocabulary concepts it tests via `teaches` (see
content/es/schemas/exercises.schema.json). engine/recycle.js already walks
this pool at runtime for the Recycle block, scoped to one lesson's earlier
material at a time. The Grammar Driller instead wants every category:grammar
exercise across the whole course, grouped by skill, available up front — so
rather than re-walking every lesson file on every drill session, this script
does it once at build time.

Output: generated/indexes/grammar-index.json
    { "bySkill": { "<teaches slug>": [ { id, ref, type }, ... ] } }

`ref` is the path engine/content-loader.js's Content fetcher expects, relative
to content/<lang>/ (e.g. "exercises/a1/a1-02-02-ex.json") — the same shape
already used by a lesson's `sections[].ref`.

Usage:
    python scripts/build_grammar_index.py
"""
import json
from pathlib import Path
from collections import defaultdict

EXERCISES_DIR = Path("content/es/exercises")
OUTPUT_DIR = Path("generated/indexes")
OUTPUT_FILE = OUTPUT_DIR / "grammar-index.json"


def build_index():
    by_skill = defaultdict(list)
    stats = {"files": 0, "exercises": 0, "errors": 0}

    for f in sorted(EXERCISES_DIR.glob("*/*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            stats["errors"] += 1
            continue
        stats["files"] += 1

        ref = f.relative_to(EXERCISES_DIR.parent).as_posix()

        for ex in data.get("exercises", []):
            if ex.get("category") != "grammar":
                continue
            stats["exercises"] += 1
            entry = {"id": ex["id"], "ref": ref, "type": ex["type"]}
            for skill in ex.get("teaches", []):
                by_skill[skill].append(entry)

    return by_skill, stats


def main():
    by_skill, stats = build_index()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"bySkill": by_skill}, f, ensure_ascii=False, separators=(",", ":"))

    raw_size = OUTPUT_FILE.stat().st_size

    print(f"Exercise files scanned: {stats['files']} (errors: {stats['errors']})")
    print(f"Grammar exercises:      {stats['exercises']}")
    print(f"Distinct skills:        {len(by_skill)}")
    print(f"Output:                 {OUTPUT_FILE} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
