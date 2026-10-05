#!/usr/bin/env python3
"""Compact review view of a unit's read-through decisions (ROADMAP 125 step 3).

    python scripts/readthrough_review.py hu b1 <unit id> <decisions.json>          # filtered
    python scripts/readthrough_review.py hu b1 <unit id> <decisions.json> --all    # every item

One line per exercise: id, category, tag, ds, and the item's content. By default
it hides the lines a reviewer almost always agrees with (a vocabulary tag on a
gloss or matching item whose tag didn't change), so review time goes to grammar
tags, changed tags and anything readthrough_check.py flags. Tag counts are
printed for the whole unit either way.
"""
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def describe(e):
    q = e.get("question") or e.get("sentence") or ""
    if isinstance(e.get("prompt"), list):
        q = " / ".join(x.get("text", "") for x in e["prompt"])
    if e.get("pairs"):
        q = "; ".join("=".join(map(str, x)) for x in e["pairs"])
    if e.get("solution"):
        q = " ".join(map(str, e["solution"])) + f"  [{e.get('english', '')}]"
    if e.get("template"):
        q = " | ".join(f"{t.get('prompt')} -> {t.get('answer')}" for t in e["template"])
    if e.get("options"):
        c = e.get("correct")
        q += "  {" + " / ".join(("*" if i == c else "") + str(o) for i, o in enumerate(e["options"])) + "}"
    if e.get("answer") or e.get("answers"):
        q += f"  => {e.get('answer') or e.get('answers')}"
    return q


def main():
    lang, level, uid, dec_path = sys.argv[1], sys.argv[2].lower(), sys.argv[3], sys.argv[4]
    show_all = "--all" in sys.argv
    course = ROOT / "content" / lang
    unit = next(u for u in load(course / "curriculum" / "units" / f"{level}.json") if u["id"] == uid)
    reg = load(ROOT / "skills" / f"{lang.split('-')[0]}.json")["skills"]
    dec = load(dec_path)

    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "readthrough_check.py"), lang, level, uid, dec_path],
                         capture_output=True, text=True, encoding="utf-8").stdout
    flagged = set(re.findall(r"^(?:warn|error)\s+(\S+?):", out, re.M))

    cnt, hidden = Counter(), 0
    for stem in unit["stems"]:
        p = course / "exercises" / level / f"{stem}-ex.json"
        if not p.exists():
            continue
        lines = []
        for e in load(p)["exercises"]:
            d = dec[e["id"]]
            tag = d["teaches"]
            cnt[tag] += 1
            old = (e.get("teaches") or [None])[0]
            is_vocab = reg.get(tag, {}).get("kind") != "grammar"
            boring = is_vocab and tag == old and not d.get("ds") and e["id"] not in flagged
            if boring and not show_all:
                hidden += 1
                continue
            mark = "!" if e["id"] in flagged else ("~" if tag != old else " ")
            ds = d.get("ds") or {}
            dss = (" ds=" + ",".join(f"{k}:{v}" for k, v in ds.items())) if ds else ""
            cat = d.get("category", e.get("category", ""))
            lines.append(f"{mark} {e['id'].replace(stem + '-', ''):16} {cat[:5]:5} {tag}{dss} | {describe(e)[:220]}")
        if lines:
            print(f"--- {stem}")
            print("\n".join(lines))
    print()
    if hidden:
        print(f"({hidden} unchanged vocabulary items hidden; --all shows them)")
    print("! flagged by readthrough_check.py   ~ tag changed")
    print(", ".join(f"{k} {v}" for k, v in cnt.most_common()))


if __name__ == "__main__":
    main()
