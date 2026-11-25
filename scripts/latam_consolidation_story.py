#!/usr/bin/env python3
"""Retire the separate consolidation story of a track unit (ES B2 latam, 2026-11-25).

    python scripts/latam_consolidation_story.py <course> <level> <unit id> [<unit id> ...] [--write]

The B2 latam generator wrote, for 27 units, a sixth text `stories/world/<level>/<stem>-consolidation.json`
(an ornate "gran crónica" of the whole unit, full of invented witnesses). The read-through rewrites the
five lesson texts and rebuilds the unit's combined reading `<stem>.json` from them
(`stitch_track_unit_stories.py --unit`); the consolidation lesson then shows that combined reading, as
the frozen Costa Rica and Cuba units do. Per unit this script:

- points the consolidation lesson's `story` section from `<stem>-consolidation.json` to `<stem>.json`;
- deletes `<stem>-consolidation.json` when no lesson of the course still references it.

It refuses (writes nothing for that unit) when the combined reading does not exist, or the
consolidation lesson's story section names a file other than these two. Rebuild the manifest after
(`python3 build-manifest.py`) so the Reader drops the deleted file. Without --write it prints the plan.
"""
import glob
import json
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
    bad = [u for u in unit_ids if u not in by_id]
    if bad:
        sys.exit(f"no such unit: {bad}")
    refs_of = {}
    for f in glob.glob(str(ROOT / f"content/{course}/lessons/*/*.json")):
        for sec in json.loads(Path(f).read_text(encoding="utf-8")).get("sections", []):
            if sec.get("type") == "story" and sec.get("ref"):
                refs_of.setdefault(sec["ref"], set()).add(Path(f).stem)
    for uid in unit_ids:
        cons = next((s for s in by_id[uid]["stems"] if s.endswith("-consolidation")), None)
        if not cons:
            print(f"{uid}: no consolidation lesson, skipped")
            continue
        stem = cons[: -len("-consolidation")]
        combined = f"stories/world/{level}/{stem}.json"
        old = f"stories/world/{level}/{stem}-consolidation.json"
        if not (ROOT / f"content/{course}/{combined}").is_file():
            print(f"{uid}: refused, no combined reading {combined}")
            continue
        lp = ROOT / f"content/{course}/lessons/{level}/{cons}.json"
        lesson = json.loads(lp.read_text(encoding="utf-8"))
        story = [s for s in lesson["sections"] if s.get("type") == "story"]
        other = [s["ref"] for s in story if s.get("ref") not in (old, combined)]
        if other:
            print(f"{uid}: refused, consolidation story is {other}")
            continue
        changed = False
        for s in story:
            if s.get("ref") == old:
                s["ref"] = combined
                changed = True
        users = refs_of.get(old, set()) - ({cons} if changed else set())
        delete = (ROOT / f"content/{course}/{old}").is_file() and not users
        print(f"{uid}: lesson ref {'→ ' + combined if changed else 'already ' + (story[0]['ref'] if story else 'none')}; "
              f"{'delete ' + old if delete else ('keep ' + old + ' (used by ' + ', '.join(sorted(users)) + ')' if users else 'no old file')}")
        if write:
            if changed:
                lp.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            if delete:
                (ROOT / f"content/{course}/{old}").unlink()
    if not write:
        print("(dry run: --write to apply)")


if __name__ == "__main__":
    main()
