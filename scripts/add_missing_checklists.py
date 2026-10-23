"""Give a lesson that has no "Can you do this?" checklist one, built from
its own goal lines, with the "Add to Review" step before it, as every other
lesson has (ROADMAP 153, HU B1 2026-10-23: 51 lesson groups from B1 Unit 25
on lack both). A challenge's `canDo` must be the lesson's first checklist
line (scripts/add_challenges.py), so these lessons can't take a challenge
until they have one.

    python scripts/add_missing_checklists.py <course> <level> <unit id> [<unit id> ...]
        [--from-challenges <drafts.json>]

A lesson with no goal section (the consolidations) takes the `canDo` line
of its challenge draft with --from-challenges; without one it is refused
rather than given invented lines. A lesson that already has a checklist
is left alone.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    args = sys.argv[1:]
    drafts = {}
    if "--from-challenges" in args:
        i = args.index("--from-challenges")
        drafts = json.loads(Path(args[i + 1]).read_text(encoding="utf-8"))
        del args[i:i + 2]
    if len(args) < 3:
        sys.exit(__doc__)
    course, level, uids = args[0], args[1].lower(), args[2:]
    units = {u["id"]: u for u in json.loads((ROOT / f"content/{course}/curriculum/units/{level}.json").read_text(encoding="utf-8"))}
    done, refused = [], []
    for uid in uids:
        for stem in units[uid]["stems"]:
            p = ROOT / f"content/{course}/lessons/{level}/{stem}.json"
            text = p.read_text(encoding="utf-8")
            data = json.loads(text)
            secs = data["sections"]
            if any(s.get("type") == "checklist" for s in secs):
                continue
            goal = next((s for s in secs if s.get("type") == "goal" and s.get("items")), None)
            items = list(goal["items"]) if goal else ([drafts[stem]["canDo"]] if stem in drafts else None)
            if not items:
                refused.append(stem)
                continue
            if not any(s.get("type") == "srs" for s in secs):
                secs.append({"type": "srs", "title": "Add to Review"})
            secs.append({"type": "checklist", "title": "Can you do this?", "items": items})
            m = re.search(r'\n( +)"', text)
            p.write_text(json.dumps(data, ensure_ascii=False, indent=len(m.group(1)) if m else 2) + "\n", encoding="utf-8")
            done.append(stem)
    print(f"added a checklist to {len(done)} lesson(s)" + (f"; refused (no goal lines): {', '.join(refused)}" if refused else ""))
    if refused:
        sys.exit(1)


if __name__ == "__main__":
    main()
