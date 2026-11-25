#!/usr/bin/env python3
"""List Reader stories no unit owns and no track hides (the level checklist's Reader step).

    python scripts/reader_orphans.py <course> [level ...]

A story in content/<course>/stories/manifest.json with no `unit` and no `hidden` flag is open to
learners in the Reader but read by no batch: ES B1 had 29 (false labels, wrong plots); ES B2 latam
had 4 combined readings that no consolidation lesson referenced, so they showed while the track was
hidden (2026-11-25). Fix by attaching the story to its unit's lesson (a `story` section) or by
hiding/removing it. Exits 1 when any are found, so it can gate a level checklist.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    course, levels = sys.argv[1], {l.upper() for l in sys.argv[2:]}
    m = json.loads((ROOT / f"content/{course}/stories/manifest.json").read_text(encoding="utf-8"))
    stories = m if isinstance(m, list) else m.get("stories", m)
    stories = stories if isinstance(stories, list) else list(stories.values())
    found = [s for s in stories
             if not s.get("unit") and not s.get("hidden")
             and (not levels or str(s.get("level", "")).upper() in levels)]
    for s in found:
        print(f"{s.get('level')}  {s.get('path') or s.get('file')}  {s.get('title', '')}")
    print(f"{len(found)} Reader stor{'y' if len(found) == 1 else 'ies'} with no unit and not hidden")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
