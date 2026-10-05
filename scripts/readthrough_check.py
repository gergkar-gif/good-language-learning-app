#!/usr/bin/env python3
"""Sanity-check a unit's read-through decisions before apply_tags.py (ROADMAP 125 step 3).

    python scripts/readthrough_check.py hu a1 objects-locations decisions.json

Errors: an exercise without a decision (or a decision for one outside the
unit), an unknown or retired slug, a skill above the unit's level, a
`distractor_skills` index that isn't a wrong option or names a non-grammar
skill. Warnings: a grammar skill whose screen comes after the exercise's
lesson, a category that doesn't follow the tag, and identical exercises
given different tags.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]
FOLLOWS = {"multiple-choice", "fill-blank", "sentence-builder", "matching"}
CONTENT_KEYS = ("question", "sentence", "options", "pairs", "solution", "prompt", "template", "answer", "answers")


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def lesson_no(ref):
    m = re.match(r"[a-z]\d-(\d+)", ref or "")
    return int(m.group(1)) if m else None


def main():
    lang, level, uid, dec_path = sys.argv[1], sys.argv[2].lower(), sys.argv[3], sys.argv[4]
    course = ROOT / "content" / lang
    unit = next(u for u in load(course / "curriculum" / "units" / f"{level}.json") if u["id"] == uid)
    reg = load(ROOT / "skills" / f"{lang.split('-')[0]}.json")["skills"]
    dec = load(dec_path)
    errors, warns = [], []
    seen, by_content = set(), defaultdict(set)
    for stem in unit["stems"]:
        ep = course / "exercises" / level / f"{stem}-ex.json"
        if not ep.exists():
            continue
        for e in load(ep)["exercises"]:
            eid = e["id"]
            seen.add(eid)
            d = dec.get(eid)
            if not d:
                errors.append(f"{eid}: no decision")
                continue
            slug = d.get("teaches")
            sk = reg.get(slug)
            if not sk or sk.get("retired"):
                errors.append(f"{eid}: unknown or retired slug {slug!r}")
                continue
            if LEVELS.index(sk["level"]) > LEVELS.index(level.upper()):
                errors.append(f"{eid}: {slug} is {sk['level']}")
            if sk["kind"] == "grammar":
                t, here = lesson_no(sk.get("taught_in")), lesson_no(stem)
                if sk["level"] == level.upper() and t and here and t > here:
                    warns.append(f"{eid}: {slug} is taught at {sk['taught_in']}, after this lesson")
            cat = d.get("category") or e.get("category")
            if (e.get("type") in FOLLOWS or cat in ("vocabulary", "grammar")) and cat != sk["kind"]:
                warns.append(f"{eid}: category {cat} but tag is {sk['kind']}")
            opts = e.get("options") or []
            for i, s2 in (d.get("ds") or {}).items():
                if not str(i).isdigit() or int(i) >= len(opts) or int(i) == e.get("correct"):
                    errors.append(f"{eid}: ds index {i} is not a wrong option")
                if (reg.get(s2) or {}).get("kind") != "grammar" or s2 == slug:
                    errors.append(f"{eid}: ds slug {s2!r} must be another grammar skill")
            key = json.dumps({k: e.get(k) for k in CONTENT_KEYS if k in e}, ensure_ascii=False, sort_keys=True)
            by_content[key].add((eid, slug))
    for eid in set(dec) - seen:
        errors.append(f"{eid}: decision for an exercise outside the unit")
    for group in by_content.values():
        if len({s for _, s in group}) > 1:
            warns.append("identical exercises, different tags: " + ", ".join(f"{i}={s}" for i, s in sorted(group)))
    for w in warns:
        print("warn ", w)
    for x in errors:
        print("ERROR", x)
    print(f"{len(seen)} exercises, {len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
