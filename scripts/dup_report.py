#!/usr/bin/env python3
"""List exact lesson-to-lesson copies inside one unit (ROADMAP 143 dedupe pass).

    python scripts/dup_report.py <course> <level> <unit id>      # one unit
    python scripts/dup_report.py <course> <level> --summary      # all units, counts only

An exercise is a copy when an earlier lesson of the same unit holds an exercise with
identical content (everything except its id, tags and explanation). The first
occurrence stays; later non-consolidation occurrences are the ones to rewrite.
Consolidation lessons are meant to recycle earlier items and are never listed.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CK = ("question", "sentence", "options", "pairs", "solution", "prompt", "template",
      "answer", "answers", "correct", "text", "english", "words", "tiles", "sentences", "solutions")


def key(e):
    s = json.dumps({k: e.get(k) for k in CK if k in e}, ensure_ascii=False, sort_keys=True)
    return re.sub(r"\s*\((?:Lesson|Lecke|Lección) ?\d+\)", "", s)  # "(Lesson 3)" labels do not make an item new


def copies(course, level, unit):
    seen, out = {}, []
    for stem in unit["stems"]:
        p = ROOT / "content" / course / "exercises" / level / f"{stem}-ex.json"
        if not p.exists():
            continue
        for e in json.loads(p.read_text(encoding="utf-8"))["exercises"]:
            k = key(e)
            if "consolidation" in stem:
                continue
            if k in seen:
                out.append((stem, e, seen[k]))
            else:
                seen[k] = e["id"]
    return out


def main():
    course, level = sys.argv[1], sys.argv[2].lower()
    table = json.loads((ROOT / "content" / course / "curriculum" / "units" / f"{level}.json").read_text(encoding="utf-8"))
    if sys.argv[3] == "--summary":
        for u in table:
            c = copies(course, level, u)
            if c:
                print(f"{len(c):4d}  {u['id']}")
        return
    unit = next(u for u in table if u["id"] == sys.argv[3])
    for stem, e, first in copies(course, level, unit):
        print(json.dumps({"lesson": stem, "id": e["id"], "copy_of": first, "type": e.get("type"),
                          "teaches": e.get("teaches"), "content": {k: e[k] for k in CK if k in e}},
                         ensure_ascii=False))


if __name__ == "__main__":
    main()
