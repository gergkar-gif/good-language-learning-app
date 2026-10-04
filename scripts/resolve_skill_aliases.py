#!/usr/bin/env python3
"""Rewrite alias skill slugs to their canonical skill everywhere content refers to skills.

Run this after an approved merge or rename in skills/<lang>.json (the old slug
becomes an alias there). It touches only skill references:

    exercises/*/*.json         `teaches` (duplicates removed, order kept) and `distractor_skills` values
    tests/*.json               every `teaches` list or string
    <course>/*.json            every `targetSkills` list (conversation scenarios, writing exchanges, ...)
    indexes/verb-tense-skills.json   the skill lists per tense

It changes nothing else in a file and keeps its line endings, so the diff is
only the slugs that changed.

    python scripts/resolve_skill_aliases.py          # rewrite
    python scripts/resolve_skill_aliases.py --dry    # report counts only
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def alias_map(src):
    amap = {}
    for slug, s in {**src["skills"], **src.get("retired", {})}.items():
        for a in s.get("aliases", []):
            amap[a] = slug
    return amap


def fix_list(values, amap):
    out, seen = [], set()
    for v in values:
        v = amap.get(v, v) if isinstance(v, str) else v
        if isinstance(v, str):
            if v in seen:
                continue
            seen.add(v)
        out.append(v)
    return out


def walk_keys(obj, keys, amap):
    """Resolve aliases under any key in `keys`, anywhere in obj."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in keys:
                if isinstance(v, list):
                    obj[k] = fix_list(v, amap)
                elif isinstance(v, str):
                    obj[k] = amap.get(v, v)
            else:
                walk_keys(v, keys, amap)
    elif isinstance(obj, list):
        for v in obj:
            walk_keys(v, keys, amap)


def rewrite(path, mutate, dry):
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    before = json.dumps(data, ensure_ascii=False, sort_keys=True)
    mutate(data)
    if json.dumps(data, ensure_ascii=False, sort_keys=True) == before:
        return False
    if not dry:
        text = json.dumps(data, ensure_ascii=False, indent=2)
        if raw.endswith("\n"):
            text += "\n"
        if "\r\n" in raw:
            text = text.replace("\n", "\r\n")
        path.write_bytes(text.encode("utf-8"))
    return True


def main():
    dry = "--dry" in sys.argv[1:]
    total = 0
    for src_path in sorted((ROOT / "skills").glob("*.json")):
        if src_path.name == "families.json" or src_path.name.startswith("frozen-"):
            continue
        src = json.loads(src_path.read_text(encoding="utf-8"))
        amap = alias_map(src)

        def fix_exercises(data):
            for ex in data.get("exercises", []):
                if isinstance(ex.get("teaches"), list):
                    ex["teaches"] = fix_list(ex["teaches"], amap)
                ds = ex.get("distractor_skills")
                if isinstance(ds, dict):
                    for k, v in ds.items():
                        ds[k] = amap.get(v, v)

        def fix_verb_tenses(data):
            for k, v in data.items():
                if isinstance(v, list):
                    data[k] = fix_list(v, amap)

        for course in src["courses"]:
            base = ROOT / "content" / course
            jobs = [(p, fix_exercises) for p in sorted(base.glob("exercises/*/*.json"))]
            jobs += [(p, lambda d: walk_keys(d, {"teaches"}, amap)) for p in sorted(base.glob("tests/*.json"))]
            jobs += [(p, lambda d: walk_keys(d, {"targetSkills"}, amap)) for p in sorted(base.glob("*.json"))]
            vts = base / "indexes" / "verb-tense-skills.json"
            if vts.is_file():
                jobs.append((vts, fix_verb_tenses))
            changed = sum(rewrite(p, fn, dry) for p, fn in jobs)
            total += changed
            print(f"{course}: {changed} file(s) {'would change' if dry else 'changed'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
