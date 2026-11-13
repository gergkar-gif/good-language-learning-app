#!/usr/bin/env python3
"""One-time conversion of "Unit N" references written by table position to the
app's numbers (scripts/unit_numbers.py; user, 2026-11-13).

    python scripts/renumber_unit_refs.py <course> [--authored-in <course>] [--apply]

Until 2026-11-13 the knowledge sheets numbered units by their position in the
level's unit table, so readers wrote "from B1 Unit 21" for the unit the app
shows as core Unit 11. Measured before the change: HU fits table positions 312
times and labels 2; es-es 46 and 0; es-latam copies es-es's numbers
(--authored-in es-es: N is resolved in es-es's table, then found in es-latam by
unit id). Only levels with more than one track change. A reference whose unit
is in a track the course hides, or that can't be resolved, is listed, not
changed. Dry run by default. Refuses to run twice on a course
(imports/review/unit-renumber/<course>.json records the run). Refreeze the
touched frozen units afterwards (it prints them).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unit_numbers as un  # noqa: E402

ROOT = un.ROOT
# vocabulary files: their "theme" ("B1 Unit 38" in b1-38) already names the unit by the
# app's number, so it is not a table position
SKIP = ("/indexes/", "/schemas/", "/decks/", "/vocabulary/", "curriculum.json", "manifest")


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    authored = None
    if "--authored-in" in args:
        i = args.index("--authored-in")
        authored = args[i + 1]
        del args[i:i + 2]
    args = [a for a in args if a != "--apply"]
    if len(args) != 1:
        sys.exit(__doc__)
    course = args[0]
    authored = authored or course
    record = ROOT / f"imports/review/unit-renumber/{course}.json"
    if record.exists():
        sys.exit(f"{record} exists: {course} was renumbered already")
    cur = json.loads((ROOT / f"content/{course}/curriculum/curriculum.json").read_text(encoding="utf-8"))
    hidden = {(lk.lower(), u["slug"]) for lk, L in cur["levels"].items() for u in L.get("units", []) if u.get("hidden")}
    tables = {lv: un.table(course, lv) for lv in un.LEVELS}
    src = {lv: un.table(authored, lv) for lv in un.LEVELS}
    stem_unit = {s: (lv, u["id"]) for lv, us in tables.items() for u in us for s in u["stems"]}

    def unit_of(f):
        b = re.sub(r"-(voc|ex)$|-[abc]-gr$|-gr$", "", Path(f).stem)
        while b not in stem_unit and "-" in b:
            b = b.rsplit("-", 1)[0]
        return stem_unit.get(b)

    changes, listed, touched = [], [], set()
    for f in sorted((ROOT / f"content/{course}").rglob("*.json")):
        rel = f.relative_to(ROOT).as_posix()
        if any(s in rel for s in SKIP):
            continue
        text = f.read_text(encoding="utf-8")
        if not un.REF.search(text):
            continue

        def sub(m):
            lv, trname, n = m.group(1).lower(), m.group(2), int(m.group(3))
            if len({u.get("track") for u in tables[lv]}) <= 1 or trname:
                return m.group(0)
            if n > len(src[lv]):
                listed.append((rel, m.group(0), "no such table position"))
                return m.group(0)
            uid = src[lv][n - 1]["id"]
            idx = next((i for i, u in enumerate(tables[lv]) if u["id"] == uid), None)
            if idx is None:
                listed.append((rel, m.group(0), f"{uid} is not in {course}"))
                return m.group(0)
            if (lv, uid) in hidden:
                listed.append((rel, m.group(0), f"points at {uid}, a hidden-track unit"))
                return m.group(0)
            new = un.name(course, lv, idx, tables[lv])
            if new != m.group(0):
                changes.append((rel, m.group(0), new, uid))
            return new

        new_text = un.REF.sub(sub, text)
        if new_text != text:
            u = unit_of(f)
            if u:
                touched.add(u)
            if apply:
                f.write_text(new_text, encoding="utf-8")
    for rel, old, new, uid in changes:
        print(f"{rel}: {old} -> {new} ({uid})")
    for rel, old, why in listed:
        print(f"LISTED {rel}: {old}: {why}")
    print(f"{len(changes)} change(s), {len(listed)} listed, {len(touched)} unit(s) touched"
          + ("" if apply else " (dry run)"), file=sys.stderr)
    if apply:
        record.parent.mkdir(parents=True, exist_ok=True)
        record.write_text(json.dumps({"authored_in": authored, "changes": changes, "listed": listed,
                                      "units": sorted(f"{lv}/{u}" for lv, u in touched)},
                                     ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
