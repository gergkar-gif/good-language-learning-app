#!/usr/bin/env python3
"""Set `taught_in` for the skills a new unit teaches, from their planned screens.

A skill signed off before its screen exists carries no `taught_in` (the
validator fails a `taught_in` whose screen is missing); its planned screen is
recorded in skills/frozen-<lang>.json as "planned taught_in <screen>"
(ES C1, 2026-11-18). A writer working through several units sets the skills
of each unit when it starts that unit, so the screens of later units are
never required early. Tool-written, so writers may run it; rebuilds the
registry.

    python scripts/set_planned_taught_in.py <lang> <level> <unit id>

Refuses a skill whose `taught_in` is already set to a different screen.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv):
    if len(argv) != 3:
        sys.exit(__doc__)
    lang, level, uid = argv
    courses = json.loads((ROOT / f"skills/{lang}.json").read_text(encoding="utf-8"))["courses"]
    table = json.loads((ROOT / f"content/{courses[0]}/curriculum/units/{level}.json").read_text(encoding="utf-8"))
    unit = next((u for u in table if u.get("id") == uid), None)
    if not unit:
        sys.exit(f"no unit {uid!r} in {level}")
    stems = set(unit["stems"])
    p = ROOT / f"skills/{lang}.json"
    raw = p.read_text(encoding="utf-8")
    data = json.loads(raw)
    frozen = json.loads((ROOT / f"skills/frozen-{lang}.json").read_text(encoding="utf-8"))["skills"]
    changed = []
    for slug, note in frozen.items():
        m = re.search(r"planned taught_in (\S+)", note)
        if not m:
            continue
        screen = m.group(1)
        stem = re.sub(r"-[a-z]-gr$|-gr$", "", screen)
        if stem not in stems:
            continue
        sk = data["skills"][slug]
        if sk.get("taught_in") == screen:
            continue
        if sk.get("taught_in"):
            sys.exit(f"{slug}: taught_in is {sk['taught_in']!r}, planned {screen!r}: settle it by hand")
        sk["taught_in"] = screen
        changed.append(f"{slug} -> {screen}")
    if changed:
        ind = 1 if raw.startswith('{\n "') else 2
        p.write_text(json.dumps(data, ensure_ascii=False, indent=ind) + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "scripts/build_skill_registry.py")], check=True, stdout=subprocess.DEVNULL)
    print(f"{uid}: " + ("; ".join(changed) if changed else "nothing to set"))


if __name__ == "__main__":
    main(sys.argv[1:])
