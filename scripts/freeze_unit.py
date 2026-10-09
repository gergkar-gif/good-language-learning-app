"""Freeze a finished unit, so nobody works on it again (ROADMAP 153).

    python scripts/freeze_unit.py <course> <level> <unit> --reason "..." \
        [--accept "<check>:<exercise id>:<why it stays>" ...]
    python scripts/freeze_unit.py --unfreeze <course> <level> <unit> --reason "..."
    python scripts/freeze_unit.py --status [course]

A unit freezes only when `check-content.py` reports nothing for it. A finding
that a reader checked and decided to keep is passed with --accept and a reason;
only the suspects and the two tell checks can be accepted, never an error such
as a length give-away or a form used before its screen. Accepted findings are
stored with the unit and not reported again. Once frozen, `check-content.py
--changed` blocks any edit to the unit unless the same change unfreezes it.
"""
import datetime
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_content", ROOT / "scripts/check-content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

ACCEPTABLE = set(cc.SUSPECTS) | {"tell-absolute", "tell-time-word"}


def path(course):
    return ROOT / "content" / course / "frozen-units.json"


def load(course):
    p = path(course)
    if p.is_file():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"_comment": "Finished units (ROADMAP 153). Written only by scripts/freeze_unit.py; "
                        "check-content.py --changed blocks edits to a unit listed here.",
            "units": {}, "unfrozen": []}


def save(course, data):
    data["units"] = dict(sorted(data["units"].items()))
    path(course).write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def opt(args, name, many=False):
    vals = []
    while name in args:
        i = args.index(name)
        vals.append(args[i + 1])
        del args[i:i + 2]
    return vals if many else (vals[0] if vals else None)


def status(courses):
    for course in courses:
        frozen = load(course)["units"]
        for level in cc.LEVELS:
            units = cc.units_of(cc.Source(), course, level)
            if not units:
                continue
            done = [u["id"] for u in units if f"{level}/{u['id']}" in frozen]
            print(f"{course:9} {level}: {len(done):3} / {len(units):3} frozen")


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--status":
        status(args[1:] or sorted(cc.LEGACY_COURSES))
        return
    unfreeze = args[0] == "--unfreeze"
    if unfreeze:
        args = args[1:]
    reason = opt(args, "--reason")
    accepts = opt(args, "--accept", many=True)
    if len(args) != 3 or not reason:
        sys.exit(__doc__)
    course, level, unit = args[0], args[1].lower(), args[2]
    if not any(u.get("id") == unit for u in cc.units_of(cc.Source(), course, level)):
        sys.exit(f"no unit {unit!r} in content/{course}/curriculum/units/{level}.json")
    data, key, today = load(course), f"{level}/{unit}", datetime.date.today().isoformat()

    if unfreeze:
        if key not in data["units"]:
            sys.exit(f"{course} {key} is not frozen")
        del data["units"][key]
        data["unfrozen"].append({"unit": key, "date": today, "reason": reason})
        save(course, data)
        print(f"unfroze {course} {key}. Fix it, then freeze it again.")
        return

    accepted = []
    for a in accepts:
        check, eid, why = (a.split(":", 2) + ["", ""])[:3]
        if check not in ACCEPTABLE:
            sys.exit(f"--accept {check}: only {', '.join(sorted(ACCEPTABLE))} can be accepted; fix the rest")
        if not why.strip():
            sys.exit(f"--accept {check}:{eid}: give the reason it stays")
        accepted.append({"check": check, "id": eid, "why": why.strip()})

    found = cc.run(cc.Source(), course, [level], unit)
    keep = {(a["check"], a["id"]) for a in accepted}
    left = [x for x in found if (x[3], x[4]) not in keep]
    unused = keep - {(x[3], x[4]) for x in found}
    if unused:
        sys.exit("accepted but not reported (typo, or already fixed): "
                 + ", ".join(f"{c}:{i}" for c, i in sorted(unused)))
    if left:
        cc.show(left)
        sys.exit(f"\n{course} {key} is not clean: {len(left)} finding(s) above. Fix them, "
                 "or --accept a checked suspect / tell with its reason.")
    data["units"][key] = {"frozen": today, "reason": reason, "accepted": accepted}
    save(course, data)
    print(f"froze {course} {key} ({len(accepted)} accepted finding(s)).")


if __name__ == "__main__":
    main()
