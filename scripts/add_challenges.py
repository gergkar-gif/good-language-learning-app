"""Add a reader's challenge drafts to challenges.json (ROADMAP 150, 153).

Readers in the HU A2 pass write one challenge per lesson (consolidation
included) to a JSON object keyed by lesson stem, in the shape of the entries
in content/<course>/curriculum/challenges.json. This checks each draft and
adds the good ones; it refuses rather than guesses:

- a stem that is not a lesson of the level, or already has a challenge
  (pass --replace to overwrite one deliberately);
- a missing or empty field, an unknown field, or cues that aren't a list
  of strings;
- `level` not the lesson's level;
- `canDo` not exactly the lesson's first checklist line;
- a target of more than 3 sentences.

Nothing is written if any draft is refused. Unmet words in targets are
reported afterwards by `check-content.py` (scripts/unmet-words.js reads
challenge targets). (Not to be confused with merge_challenges.py, which
resolves git conflicts on the same file.)

    python scripts/add_challenges.py <course> <level> <drafts.json> [--replace]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["tier", "level", "title", "scenario", "prompt", "cues", "target", "english", "canDo"]


def first_checklist_line(lesson):
    for sec in lesson.get("sections", []):
        if sec.get("type") == "checklist":
            items = [i for i in sec.get("items") or [] if isinstance(i, str) and i.strip()]
            return items[0] if items else None
    return None


def problems(stem, c, stems, table, replace, course, level):
    if stem not in stems:
        return ["not a lesson of this level"]
    out = []
    if stem in table and not replace:
        out.append("already has a challenge (use --replace)")
    if not isinstance(c, dict):
        return out + ["not an object"]
    extra = set(c) - set(FIELDS)
    if extra:
        out.append(f"unknown field(s) {sorted(extra)}")
    for f in FIELDS:
        v = c.get(f)
        if f == "cues":
            if not isinstance(v, list) or not v or not all(isinstance(x, str) and x.strip() for x in v):
                out.append("cues must be a non-empty list of strings")
        elif not isinstance(v, str) or not v.strip():
            out.append(f"missing {f}")
    if c.get("level") and c["level"] != level.upper():
        out.append(f"level {c['level']!r}, expected {level.upper()!r}")
    lesson_file = ROOT / f"content/{course}/lessons/{level}/{stem}.json"
    line = first_checklist_line(json.loads(lesson_file.read_text(encoding="utf-8"))) if lesson_file.is_file() else None
    if line is None:
        out.append("lesson has no checklist line to copy into canDo")
    elif c.get("canDo") != line:
        out.append(f"canDo must be the first checklist line: {line!r}")
    # a regnal or ordinal numeral's full stop (II. József, IV. Béla, 1848.
    # március 15.) ends no sentence (HU B1 citizenship batches: refused four
    # three-sentence targets about kings)
    target = re.sub(r"\b([IVXLC]+|\d+)\.(?=\s)", r"\1", c["target"]) if isinstance(c.get("target"), str) else None
    if target is not None and len([s for s in re.split(r"[.!?]+", target) if s.strip()]) > 3:
        out.append("target has more than 3 sentences")
    return out


def main():
    args = sys.argv[1:]
    replace = "--replace" in args
    args = [a for a in args if a != "--replace"]
    if len(args) != 3:
        sys.exit(__doc__)
    course, level, drafts_path = args[0], args[1].lower(), args[2]
    units = json.loads((ROOT / f"content/{course}/curriculum/units/{level}.json").read_text(encoding="utf-8"))
    stems = [s for u in units for s in u.get("stems", [])]
    target_path = ROOT / f"content/{course}/curriculum/challenges.json"
    text = target_path.read_text(encoding="utf-8")
    data = json.loads(text)
    if json.dumps(data, ensure_ascii=False, indent=2) + "\n" != text:
        sys.exit(f"{target_path} doesn't round-trip through JSON (indent 2); fix its formatting first")
    table = data["challenges"]
    drafts = json.loads(Path(drafts_path).read_text(encoding="utf-8"))

    errors = [f"{stem}: {p}" for stem, c in drafts.items()
              for p in problems(stem, c, stems, table, replace, course, level)]
    if errors:
        print("\n".join(errors))
        sys.exit(f"refused: {len(errors)} problem(s); nothing written")

    # Existing entries keep their place (a replaced entry is edited in place);
    # a new one goes right after the nearest earlier lesson of its level that
    # has a challenge, else before the nearest later one, else at the end.
    # (Re-sorting the whole file moved every other level's block and turned
    # an 18-entry change into a 4,600-line diff.)
    order = {s: i for i, s in enumerate(stems)}
    keys = list(table)
    for stem, c in drafts.items():
        entry = {f: c[f] for f in FIELDS}
        if stem not in table:
            earlier = [k for k in keys if k in order and order[k] < order[stem]]
            later = [k for k in keys if k in order and order[k] > order[stem]]
            if earlier:
                keys.insert(keys.index(max(earlier, key=order.get)) + 1, stem)
            elif later:
                keys.insert(keys.index(min(later, key=order.get)), stem)
            else:
                keys.append(stem)
        table[stem] = entry
    data["challenges"] = {k: table[k] for k in keys}
    target_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"added {len(drafts)} challenge(s) to {target_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
