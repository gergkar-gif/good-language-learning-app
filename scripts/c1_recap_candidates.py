#!/usr/bin/env python3
"""Known B1/B2 grammar skills an ES C1 topic unit can recap, least used in C1 first.

A C1 unit without a new skill recaps known skills in its domain (Units 5, 9). This
lists every core B1/B2 grammar skill (with the screen and the unit that teaches it,
so a recap names the right unit) and how many C1 items already tag it, so a writer
drafting a topic unit's notes picks skills C1 has not drilled much yet (2026-11-19).

    python scripts/c1_recap_candidates.py [--family <family>] [--top 40]
"""
import glob
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import unit_numbers as un  # noqa: E402


def main(argv):
    fam = argv[argv.index("--family") + 1] if "--family" in argv else None
    top = int(argv[argv.index("--top") + 1]) if "--top" in argv else 40
    skills = json.loads((ROOT / "skills/es.json").read_text(encoding="utf-8"))["skills"]
    used = Counter()
    for f in glob.glob(str(ROOT / "content/es-latam/exercises/c1/*.json")):
        for e in json.loads(Path(f).read_text(encoding="utf-8")).get("exercises", []):
            used.update(e.get("teaches") or [])
    where = {}
    for lv in ("b1", "b2"):
        for i, u in enumerate(json.loads((ROOT / f"content/es-latam/curriculum/units/{lv}.json").read_text(encoding="utf-8"))):
            if u.get("track", "core") != "core":
                continue
            for st in u["stems"]:
                where[st] = (lv, i)
    rows = []
    for slug, s in skills.items():
        if s.get("kind") != "grammar" or s.get("level") not in ("B1", "B2") or (fam and s.get("family") != fam):
            continue
        scr = s.get("taught_in") or ""
        stem = next((st for st in sorted(where, key=len, reverse=True) if scr.startswith(st)), None)
        if not stem:
            continue        # taught only on a hidden track: not known
        lv, i = where[stem]
        rows.append((used[slug], slug, s["level"], s.get("family"), s["title"], scr, un.name("es-latam", lv, i)))
    rows.sort()
    for n, slug, lvl, f, title, scr, unit in rows[:top]:
        print(f"{n:3d} C1 items | `{slug}` [{lvl}, {f}] {title} | {scr} ({unit})")


if __name__ == "__main__":
    main(sys.argv[1:])
