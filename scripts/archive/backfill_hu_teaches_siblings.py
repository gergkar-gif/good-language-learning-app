#!/usr/bin/env python3
"""Backfill Hungarian exercises with tagged siblings in the same file (Phase 3.2)."""

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent


def dominant_teaches(exercises, target_cat):
    same_cat = Counter()
    any_cat = Counter()
    for ex in exercises:
        t = ex.get("teaches")
        if isinstance(t, list) and t:
            key = tuple(t)
            any_cat[key] += 1
            if ex.get("category") == target_cat:
                same_cat[key] += 1
    if same_cat:
        return list(same_cat.most_common(1)[0][0])
    if any_cat:
        return list(any_cat.most_common(1)[0][0])
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    samples = []
    files_written = 0
    tagged_count = Counter()

    for p in sorted((ROOT / "content/hu/exercises").glob("*/*.json")):
        lvl = p.parent.name
        data = json.loads(p.read_text(encoding="utf-8"))
        exs = data.get("exercises", [])
        has_tagged_sibling = any(isinstance(ex.get("teaches"), list) and len(ex.get("teaches")) > 0 for ex in exs)
        if not has_tagged_sibling:
            continue

        changed = False
        for ex in exs:
            cat = ex.get("category")
            if cat == "reading":
                continue
            t = ex.get("teaches")
            if isinstance(t, list) and len(t) > 0:
                continue

            new_t = dominant_teaches(exs, cat)
            if not new_t:
                continue

            ex["teaches"] = new_t
            changed = True
            tagged_count[lvl] += 1
            prompt_text = ex.get("question") or ex.get("sentence") or ex.get("english") or str(ex.get("pairs", "")[:2])
            samples.append((lvl, p.name, ex.get("id"), cat, new_t, prompt_text))

        if changed and args.write:
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            files_written += 1

    print(f"=== Phase 3.2 Sibling Backfill Summary: {dict(tagged_count)} (total: {sum(tagged_count.values())}, files: {files_written}) ===")
    rng = random.Random(42)
    picked = rng.sample(samples, min(30, len(samples)))
    print("\n=== 30 Random Tagged Exercises (Phase 3.2) ===")
    for lvl, fname, eid, cat, new_t, txt in picked:
        print(f"  [{lvl}/{fname} :: {eid}] ({cat}) -> teaches={new_t} | {txt[:80]}")


if __name__ == "__main__":
    main()
