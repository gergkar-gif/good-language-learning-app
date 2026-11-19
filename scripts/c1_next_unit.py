#!/usr/bin/env python3
"""The next ES C1 core unit to write, for an unattended writer (2026-11-19).

Prints the first unit of content/es-latam/curriculum/units/c1.json that has no lesson
file yet: its number, id, title, the new C1 skills it teaches (planned screens in
skills/frozen-es.json), and whether its notes exist. Exit 0 with "NEXT …", 2 when
every unit is written, 3 when the next unit teaches a new skill but has no notes
(only Claude writes those: stop and report).

    python scripts/c1_next_unit.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    table = json.loads((ROOT / "content/es-latam/curriculum/units/c1.json").read_text(encoding="utf-8"))
    frozen = json.loads((ROOT / "skills/frozen-es.json").read_text(encoding="utf-8"))["skills"]
    for i, u in enumerate(table):
        if (ROOT / f"content/es-latam/lessons/c1/{u['stems'][0]}.json").exists():
            continue
        new = sorted(slug for slug, note in frozen.items()
                     if (m := re.search(r"planned taught_in (\S+)", note))
                     and re.sub(r"-[a-z]-gr$", "", m.group(1)) in u["stems"])
        notes = ROOT / f"imports/review/es-c1-plan/notes/{u['id']}.md"
        print(f"NEXT Unit {i + 1} `{u['id']}` ({u['title']}); new skills: {', '.join(new) or 'none (topic unit)'}; "
              f"notes: {'yes' if notes.exists() else 'MISSING'}")
        if new and not notes.exists():
            print("STOP: this unit teaches a new skill and has no notes; only Claude writes those. Report to the user.")
            sys.exit(3)
        if not notes.exists():
            print(f"Draft the notes first: {notes.relative_to(ROOT)}, following imports/review/es-c1-plan/notes/README.md.")
        return
    print("DONE: every C1 unit has its lessons.")
    sys.exit(2)


if __name__ == "__main__":
    main()
