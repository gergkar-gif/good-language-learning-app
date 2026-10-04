#!/usr/bin/env python3
"""Lock a reviewed unit's exercise tags (ROADMAP 125).

Run once a unit has been read and every exercise in it has its single
`teaches` slug (and its `distractor_skills`). From then on the validator fails
any change to those tags that isn't recorded here, and the one-tag and level
rules become errors for the unit instead of warnings.

    python scripts/lock_tags.py hu a1/family --reason "read-through, all 5 lessons"
    python scripts/lock_tags.py hu a1/family --reason "..." --update   # re-lock after a deliberate change

Refuses to lock a unit whose exercises still break a rule (more than one tag, a
retired slug, a skill above the exercise's level), so a locked unit is always clean.
"""

import argparse
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("course")
    ap.add_argument("unit", help="<level>/<unit id>, e.g. a1/family")
    ap.add_argument("--reason", required=True)
    ap.add_argument("--update", action="store_true", help="allow re-locking an already locked unit")
    args = ap.parse_args()

    level, uid = args.unit.lower().split("/", 1)
    course = ROOT / "content" / args.course
    table = json.loads((course / "curriculum" / "units" / f"{level}.json").read_text(encoding="utf-8"))
    entry = next((u for u in table if u.get("id") == uid), None)
    if not entry:
        sys.exit(f"no unit {uid!r} in content/{args.course}/curriculum/units/{level}.json")
    stems = set(entry["stems"])

    lang = next(p.stem for p in (ROOT / "skills").glob("*.json")
                if not p.stem.startswith("frozen-") and p.stem != "families"
                and args.course in json.loads(p.read_text(encoding="utf-8")).get("courses", []))
    src = json.loads((ROOT / "skills" / f"{lang}.json").read_text(encoding="utf-8"))
    skills, retired = src["skills"], src.get("retired", {})

    lock_path = course / "indexes" / "tags.lock.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    key = f"{level.upper()}/{uid}"
    if key in lock["units"] and not args.update:
        sys.exit(f"{key} is already locked; pass --update with a reason to re-lock it after a deliberate change")

    problems, locked = [], {}
    for path in sorted(course.glob(f"exercises/{level}/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("lesson") not in stems:
            continue
        for ex in data.get("exercises", []):
            teaches = ex.get("teaches") or []
            ex_id = ex.get("id")
            if ex.get("category") != "reading" and len(teaches) != 1:
                problems.append(f"{ex_id}: teaches {len(teaches)} skills")
            for t in teaches:
                if t in retired:
                    problems.append(f"{ex_id}: retired slug {t}")
                elif t in skills and LEVELS.index(skills[t]["level"]) > LEVELS.index(level.upper()):
                    problems.append(f"{ex_id}: {t} is {skills[t]['level']}, above {level.upper()}")
            locked[ex_id] = {"teaches": teaches, "distractor_skills": ex.get("distractor_skills") or {}}
    if problems:
        print(f"Not locked: {len(problems)} problem(s) in {key}:")
        for p in problems[:40]:
            print(f"  {p}")
        return 1
    if not locked:
        sys.exit(f"no exercises found for {key}")

    lock["exercises"].update(locked)
    lock["units"][key] = {"locked": datetime.date.today().isoformat(), "exercises": len(locked), "reason": args.reason}
    lock["units"] = dict(sorted(lock["units"].items()))
    lock["exercises"] = dict(sorted(lock["exercises"].items()))
    lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"locked {key}: {len(locked)} exercise(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
