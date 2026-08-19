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

Output: content/<lang>/indexes/grammar-index.json
    { "bySkill": { "<teaches slug>": [ { id, ref, type }, ... ] } }

`ref` is the path engine/content-loader.js's Content fetcher expects, relative
to content/<lang>/ (e.g. "exercises/a1/a1-02-02-ex.json") — the same shape
already used by a lesson's `sections[].ref`.

Usage:
    python scripts/build_grammar_index.py [lang ...]   (default: es hu)
"""
import json
import sys
from pathlib import Path
from collections import defaultdict


def build_index(exercises_dir):
    by_skill = defaultdict(list)
    stats = {"files": 0, "exercises": 0, "errors": 0}

    for f in sorted(exercises_dir.glob("*/*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            stats["errors"] += 1
            continue
        stats["files"] += 1

        ref = f.relative_to(exercises_dir.parent).as_posix()

        for ex in data.get("exercises", []):
            if ex.get("category") != "grammar":
                continue
            stats["exercises"] += 1
            entry = {"id": ex["id"], "ref": ref, "type": ex["type"]}
            for skill in ex.get("teaches", []):
                by_skill[skill].append(entry)

    return by_skill, stats


def main():
    langs = sys.argv[1:] or ["es", "hu"]

    for lang in langs:
        exercises_dir = Path(f"content/{lang}/exercises")
        if not exercises_dir.is_dir():
            print(f"[{lang}] no exercises dir, skipping")
            continue

        by_skill, stats = build_index(exercises_dir)

        output_dir = Path(f"content/{lang}/indexes")
        output_file = output_dir / "grammar-index.json"
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"bySkill": by_skill}, f, ensure_ascii=False, separators=(",", ":"))

        raw_size = output_file.stat().st_size

        print(f"[{lang}] Exercise files scanned: {stats['files']} (errors: {stats['errors']})")
        print(f"[{lang}] Grammar exercises:      {stats['exercises']}")
        print(f"[{lang}] Distinct skills:        {len(by_skill)}")
        print(f"[{lang}] Output:                 {output_file} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
