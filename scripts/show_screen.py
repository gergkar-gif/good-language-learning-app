#!/usr/bin/env python3
"""Print grammar screens as plain text: title, text, table rows, examples, tip.

For writers and readers who need the wording of a recapped screen (its unit
and what it taught) without loading the JSON (ES C1 writers, 2026-11-18).

    python scripts/show_screen.py <course> <screen id> [<screen id> ...]
    python scripts/show_screen.py es-latam b2-26-05-a-gr b2-18-01-a-gr
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    course = argv[0]
    for sid in argv[1:]:
        hits = list((ROOT / "content" / course / "grammar").glob(f"*/{sid}.json"))
        if not hits:
            print(f"== {sid}: not found\n")
            continue
        d = json.loads(hits[0].read_text(encoding="utf-8"))
        print(f"== {sid}: {d.get('title')}")
        for s in d.get("sections", []):
            t = s.get("type")
            if t in ("text", "tip"):
                print(f"[{t}] {s.get('content')}")
            elif t == "table":
                print(f"[table] {s.get('title') or ''}")
                for row in s.get("rows", []):
                    print("   | " + " | ".join(map(str, row)))
            elif t == "examples":
                for it in s.get("items", []):
                    print(f"   - {it.get('spanish')} = {it.get('english')}")
        print()


if __name__ == "__main__":
    main(sys.argv[1:])
