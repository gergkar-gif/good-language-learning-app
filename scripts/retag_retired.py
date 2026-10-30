#!/usr/bin/env python3
"""Retag exercises that still carry a retired slug (ROADMAP 125, read-through clean-up).

    python scripts/retag_retired.py hu b2 decisions.json [--apply]

decisions.json: {"<exercise id>": {"teaches": "<slug>", "ds": {"<option index>": "<slug>"}}}
("ds" optional; it replaces the item's distractor_skills, an empty {} removes them.)

Retired slugs have no alias to follow, so each item needs a decision by what a
wrong answer shows. The one mechanical rule is applied without a decision:
open writing (`structured-writing`) gets the unit's vocabulary skill
(unit-agent-rules § 3). Every other retired item must have a decision, or the
script refuses and lists the missing ids. It also refuses a decision whose
slug is unknown or retired, above the item's level, or taught (`taught_in`)
after the item's lesson, a `ds` entry naming the item's own skill, and a
decision for an item that carries no retired slug.

`category` follows the new tag on choice, fill-blank and builder items
(vocabulary skill -> "vocabulary", grammar skill -> "grammar"); dialogue,
writing, listening and reading items keep theirs. Dry run by default; --apply
writes. Lock each unit afterwards with lock_tags.py once it has been read.
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]
FOLLOWS_TAG = {"multiple-choice", "fill-blank", "sentence-builder"}


def lesson_order(course):
    """stem -> (level index, unit index, stem index) over every level's unit table."""
    order = {}
    for li, lv in enumerate(LEVELS):
        p = ROOT / "content" / course / "curriculum" / "units" / f"{lv}.json"
        if not p.exists():
            continue
        for ui, u in enumerate(json.loads(p.read_text(encoding="utf-8"))):
            for si, s in enumerate(u["stems"]):
                order[s] = (li, ui, si)
    return order


def stem_of(screen, order):
    """The longest lesson stem that the screen id starts with."""
    best = None
    for s in order:
        if screen.startswith(s + "-") and (best is None or len(s) > len(best)):
            best = s
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("course")
    ap.add_argument("level")
    ap.add_argument("decisions")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    lang = a.course.split("-")[0]
    reg = json.loads((ROOT / "skills" / f"{lang}.json").read_text(encoding="utf-8"))
    skills, retired = reg["skills"], set(reg.get("retired", {}))
    dec = json.loads(Path(a.decisions).read_text(encoding="utf-8"))
    order = lesson_order(a.course)
    lvl_i = LEVELS.index(a.level)
    units = json.loads((ROOT / "content" / a.course / "curriculum" / "units" / f"{a.level}.json").read_text(encoding="utf-8"))
    unit_of = {s: u["id"] for u in units for s in u["stems"]}

    errors, changes, used = [], [], set()
    files = {}
    for p in sorted((ROOT / "content" / a.course / "exercises" / a.level).glob("*-ex.json")):
        raw = p.read_text(encoding="utf-8")
        d = json.loads(raw)
        stem = p.name[: -len("-ex.json")]
        touched = False
        for e in d.get("exercises", []):
            eid = e.get("id")
            old = e.get("teaches") or []
            if not set(old) & retired:
                if eid in dec:
                    errors.append(f"{eid}: has a decision but no retired slug ({old})")
                continue
            if eid in dec:
                dd = dec[eid]
                used.add(eid)
            elif e.get("type") == "structured-writing":
                dd = {"teaches": f"{a.level}-{unit_of[stem]}-vocab"}
            else:
                errors.append(f"{eid}: retired {old}, no decision")
                continue
            new = dd["teaches"]
            sk = skills.get(new)
            if not sk or new in retired:
                errors.append(f"{eid}: {new} is not a live skill")
                continue
            if LEVELS.index(sk["level"].lower()) > lvl_i:
                errors.append(f"{eid}: {new} is {sk['level']}, above {a.level}")
                continue
            if sk.get("taught_in"):
                ts = stem_of(sk["taught_in"], order)
                if ts is None:
                    errors.append(f"{eid}: can't place {new}'s taught_in {sk['taught_in']}")
                    continue
                if order[ts] > order[stem]:
                    errors.append(f"{eid}: {new} is taught in {ts}, after {stem}")
                    continue
            ds = dd.get("ds")
            if ds is not None:
                bad = [s for s in ds.values() if s == new or s not in skills]
                if bad or any(int(i) >= len(e.get("options", [])) or int(i) == e.get("correct") for i in ds):
                    errors.append(f"{eid}: bad ds {ds}")
                    continue
            e["teaches"] = [new]
            if ds is not None:
                if ds:
                    e["distractor_skills"] = ds
                else:
                    e.pop("distractor_skills", None)
            if e.get("type") in FOLLOWS_TAG:
                e["category"] = "vocabulary" if sk["kind"] == "vocabulary" else "grammar"
            changes.append(f"{eid}: {old[0]} -> {new}" + (f" ds {ds}" if ds else ""))
            touched = True
        if touched:
            files[p] = (raw, d)
    for eid in sorted(set(dec) - used):
        if not any(eid in c for c in errors):
            errors.append(f"{eid}: decision for an exercise not found among retired items")

    print("\n".join(changes))
    print(f"{len(changes)} retagged in {len(files)} files")
    if errors:
        print("REFUSED:\n  " + "\n  ".join(errors))
        sys.exit(1)
    if a.apply:
        for p, (raw, d) in files.items():
            nl = "\r\n" if "\r\n" in raw else "\n"
            text = json.dumps(d, ensure_ascii=False, indent=2).replace("\n", nl)
            if raw.endswith("\n"):
                text += nl
            p.write_text(text, encoding="utf-8", newline="")
        print("written")


if __name__ == "__main__":
    main()
