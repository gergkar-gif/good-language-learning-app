#!/usr/bin/env python3
"""Backfill the remaining 495 Hungarian B1 consolidation exercises (Phase 3.4).

Inherits the unit's vocabulary-theme slug for `vocabulary` exercises and the unit's
lesson grammar skill slugs (from lessons 01..05 of the same unit) for `grammar`,
`dialogue`, `writing`, and `listening` exercises.
"""

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent


def collect_unit_skills(unit_stem):
    """Collect primary grammar slugs and vocabulary slugs from lessons 01..05 of `unit_stem`."""
    ex_dir = ROOT / "content/hu/exercises/b1"
    gr_dir = ROOT / "content/hu/grammar/b1"
    grammar_slugs = []
    vocab_slugs = []

    for i in range(1, 6):
        lesson_stem = f"{unit_stem}-{i:02d}"
        lp = ex_dir / f"{lesson_stem}-ex.json"
        if not lp.is_file():
            continue

        # Prefer the lesson's grammar file IDs if present
        gr_files = sorted(gr_dir.glob(f"{lesson_stem}*-gr.json"))
        lesson_gr = []
        for gf in gr_files:
            try:
                gd = json.loads(gf.read_text(encoding="utf-8"))
                gid = gd.get("id", "")
                if gid:
                    slug = gid.split(".")[-1]
                    if slug == "synthesis":
                        slug = f"{unit_stem.replace('b1-', '')}-relative-clause-synthesis"
                    lesson_gr.append(slug)
            except Exception:
                pass

        data = json.loads(lp.read_text(encoding="utf-8"))
        gr_counter = Counter()
        for ex in data.get("exercises", []):
            cat = ex.get("category")
            for t in ex.get("teaches") or []:
                if cat == "vocabulary":
                    if t not in vocab_slugs:
                        vocab_slugs.append(t)
                elif cat in ("grammar", "dialogue", "writing", "listening"):
                    gr_counter[t] += 1

        if not lesson_gr and gr_counter:
            lesson_gr = [slug for slug, _ in gr_counter.most_common(2)]
        if lesson_gr:
            grammar_slugs.append(lesson_gr[:2])

    return grammar_slugs, vocab_slugs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    samples = []
    files_written = 0
    tagged_count = Counter()

    for p in sorted((ROOT / "content/hu/exercises/b1").glob("*-consolidation-ex.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        exs = data.get("exercises", [])
        if not any(ex.get("category") != "reading" and not ex.get("teaches") for ex in exs):
            continue

        unit_stem = p.stem.replace("-consolidation-ex", "")
        grammar_slug_groups, vocab_slugs = collect_unit_skills(unit_stem)
        if not grammar_slug_groups:
            continue

        voc_tag = [vocab_slugs[0]] if vocab_slugs else grammar_slug_groups[0][:1]
        changed = False
        gr_idx = 0

        for ex in exs:
            cat = ex.get("category")
            if cat == "reading":
                continue
            t = ex.get("teaches")
            if isinstance(t, list) and len(t) > 0:
                continue

            if cat == "vocabulary":
                new_t = list(voc_tag)
            else:
                # Assign the corresponding lesson's grammar skill(s) from the unit
                new_t = list(grammar_slug_groups[gr_idx % len(grammar_slug_groups)])
                gr_idx += 1

            ex["teaches"] = new_t
            changed = True
            tagged_count[cat] += 1
            prompt_text = ex.get("question") or ex.get("sentence") or ex.get("english") or str(ex.get("pairs", "")[:2])
            samples.append((p.name, ex.get("id"), cat, new_t, prompt_text))

        if changed and args.write:
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            files_written += 1

    print(f"=== Phase 3.4 Consolidation Backfill Summary: {dict(tagged_count)} (total: {sum(tagged_count.values())}, files: {files_written}) ===")
    rng = random.Random(42)
    picked = rng.sample(samples, min(30, len(samples)))
    print("\n=== 30 Random Tagged Exercises (Phase 3.4) ===")
    for fname, eid, cat, new_t, txt in picked:
        print(f"  [b1/{fname} :: {eid}] ({cat}) -> teaches={new_t} | {txt[:80]}")


if __name__ == "__main__":
    main()
