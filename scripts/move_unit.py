"""Move a unit to another position in its level and renumber "Unit N" (ROADMAP 153).

Unit ids and stems never change; a unit's number is its position in
content/<course>/curriculum/units/<level>.json. Moving one changes the
numbers of the units between its old and new place, so every "Unit N" in
that level's content (screens, exercises, lessons, vocabulary lists,
stories, challenges of the level) is renumbered to match. Other levels
are not touched: an A2 screen's "Unit 12" is an A2 unit.

It refuses a unit id that isn't in the table or a position out of range.
Afterwards: build-manifest.py (curriculum.json), the knowledge sheets, and
refreeze any frozen unit whose text changed (scripts/refreeze_changed.py).

    python scripts/move_unit.py <course> <level> <unit id> <new position (1-based)> [--write]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Recap phrases only ("You know … from Unit 6"): "the Unit 12 schedule" in a
# question names a lesson file (a1-12), not a unit, and stays.
UNIT_REF = re.compile(r"\b((?:from|in) (?:A1 |A2 )?Units?) (\d+)\b")
TITLE = re.compile(r"^Unit \d+")


def load(p):
    text = p.read_text(encoding="utf-8")
    m = re.search(r'\n( +)"', text)
    return json.loads(text), (len(m.group(1)) if m else 2), text.endswith("\n")


def dump(p, data, indent, nl):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=indent) + ("\n" if nl else ""), encoding="utf-8")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 4:
        sys.exit(__doc__)
    course, level, uid, pos = args[0], args[1].lower(), args[2], int(args[3])
    write = "--write" in sys.argv
    table = ROOT / "content" / course / "curriculum" / "units" / f"{level}.json"
    units, indent, nl = load(table)
    old = next((i for i, u in enumerate(units) if u.get("id") == uid), None)
    if old is None or not 1 <= pos <= len(units):
        sys.exit(f"refused: {uid} not in {table.name}, or position {pos} outside 1..{len(units)}")
    order = [u["id"] for u in units]
    moved = units.pop(old)
    units.insert(pos - 1, moved)
    new_num = {order.index(u["id"]) + 1: i + 1 for i, u in enumerate(units)}  # old number -> new number

    def renumber(s):
        return UNIT_REF.sub(lambda m: f"{m.group(1)} {new_num.get(int(m.group(2)), int(m.group(2)))}", s)

    changes = []

    stem_unit = {s: i + 1 for i, u in enumerate(units) for s in u.get("stems", [])}

    def walk(x, where):
        if isinstance(x, str):
            y = renumber(x)
            if y != x:
                changes.append(f"{where}: {x[:90]!r} -> {y[:90]!r}")
            return y
        if isinstance(x, list):
            return [walk(v, where) for v in x]
        if isinstance(x, dict):
            return {k: walk(v, where) for k, v in x.items()}
        return x

    base = ROOT / "content" / course
    files = [p for d in ("exercises", "grammar", "lessons", "vocabulary", "stories", "drills")
             for p in sorted((base / d).rglob(f"{level}/*.json"))]
    for p in files:
        try:
            data, ind, n = load(p)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        before = len(changes)
        new = walk(data, p.relative_to(ROOT).as_posix())
        # a lesson title "Unit 13 Consolidation" gets its unit's real number
        if "/lessons/" in p.as_posix() and isinstance(new, dict) and TITLE.match(new.get("title", "")) and p.stem in stem_unit:
            t = TITLE.sub(f"Unit {stem_unit[p.stem]}", new["title"])
            if t != new["title"]:
                changes.append(f"{p.relative_to(ROOT).as_posix()}: title {new['title']!r} -> {t!r}")
                new["title"] = t
        if write and len(changes) > before:
            dump(p, new, ind, n)
    cp = base / "curriculum" / "challenges.json"
    data, ind, n = load(cp)
    before = len(changes)
    for k in list(data.get("challenges", {})):
        if k.startswith(level + "-"):
            data["challenges"][k] = walk(data["challenges"][k], f"{cp.relative_to(ROOT).as_posix()} {k}")
    if write:
        if len(changes) > before:
            dump(cp, data, ind, n)
        dump(table, units, indent, nl)
    print(f"{course} {level}: {uid} from Unit {old + 1} to Unit {pos}; {len(changes)} 'Unit N' string(s) "
          f"{'renumbered' if write else 'to renumber'}")
    for c in changes:
        print("  " + c)


if __name__ == "__main__":
    main()
