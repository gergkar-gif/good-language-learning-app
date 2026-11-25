#!/usr/bin/env python3
"""Make shared checklist lines distinct (check-content `checklist-shared`).

    python scripts/fix_shared_checklists.py <course> <level> <unit id> [<unit id> ...] [--write]

A checklist line used by more than one lesson is kept as it is in the first lesson
(table order) and given a suffix in every later one: in a consolidation lesson
" (review)"; in a teaching lesson " (<place>)", the unit title before its colon
("Cuba", "Panamá"). The same line in the lesson's `goal` section and the `canDo` of
its challenge in curriculum/challenges.json change with it, so add_challenges and
the walk stay in step. Without --write it prints the changes. It refuses (writes
nothing) when a new line would still be shared or the suffix would not make it
distinct. Seen twice (HU C1 culture 2026-11-18, ES B2 latam 5-10 2026-11-25).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    if len(args) < 3:
        sys.exit(__doc__)
    course, level, unit_ids = args[0], args[1].lower(), args[2:]
    units = json.loads((ROOT / f"content/{course}/curriculum/units/{level}.json").read_text(encoding="utf-8"))
    units = units if isinstance(units, list) else units["units"]
    by_id = {u["id"]: u for u in units}
    missing = [u for u in unit_ids if u not in by_id]
    if missing:
        sys.exit(f"no such unit: {missing}")
    order = [s for u in units for s in u["stems"]]
    place = {s: re.split(r"\s*:\s*", u.get("title", ""))[0].strip() for u in units for s in u["stems"]}

    # check-content reads one unit id per run
    out = "".join(subprocess.run([sys.executable, "scripts/check-content.py", course, level, u],
                                 cwd=ROOT, capture_output=True, text=True).stdout for u in unit_ids)
    stems = {m.group(1) for m in re.finditer(r"checklist-shared\s+(\S+)\s", out)}
    if not stems:
        print("no checklist-shared findings")
        return

    lines = {}   # line -> [stems in table order]
    data = {}
    for s in sorted(stems, key=order.index):
        p = ROOT / f"content/{course}/lessons/{level}/{s}.json"
        data[s] = (p, json.loads(p.read_text(encoding="utf-8")))
        for sec in data[s][1]["sections"]:
            if sec.get("type") == "checklist":
                for it in sec.get("items", []):
                    lines.setdefault(it, []).append(s)
    # every checklist line in the whole level, to test the new lines against
    all_lines = {}
    for f in (ROOT / f"content/{course}/lessons/{level}").glob("*.json"):
        for sec in json.loads(f.read_text(encoding="utf-8")).get("sections", []):
            if sec.get("type") == "checklist":
                for it in sec.get("items", []):
                    all_lines.setdefault(it, set()).add(f.stem)

    changes = []  # (stem, old, new)
    for line, ss in lines.items():
        holders = sorted(all_lines.get(line, set()), key=lambda x: order.index(x) if x in order else 10**6)
        for s in holders[1:]:
            if s not in data:
                continue
            suffix = " (review)" if s.endswith("-consolidation") else f" ({place[s]})"
            base = line[:-1] if line.endswith(".") else line
            new = base + suffix + "."
            if new in all_lines:
                sys.exit(f"refused: {s}: {new!r} is already a checklist line elsewhere")
            changes.append((s, line, new))
    if not changes:
        print("nothing to change")
        return

    chal_path = ROOT / f"content/{course}/curriculum/challenges.json"
    chal = json.loads(chal_path.read_text(encoding="utf-8"))
    for s, old, new in changes:
        print(f"{s}: {old!r} -> {new!r}")
        p, lesson = data[s]
        for sec in lesson["sections"]:
            if sec.get("type") in ("checklist", "goal"):
                sec["items"] = [new if it == old else it for it in sec.get("items", [])]
        c = chal.get("challenges", {}).get(s)
        if c and c.get("canDo") == old:
            c["canDo"] = new
            print(f"  challenge {s}: canDo updated")
    if write:
        for s, (p, lesson) in data.items():
            p.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        chal_path.write_text(json.dumps(chal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {len(changes)} change(s)")
    else:
        print("(dry run: --write to apply)")


if __name__ == "__main__":
    main()
