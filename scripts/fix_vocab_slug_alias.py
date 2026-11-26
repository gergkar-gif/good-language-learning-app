#!/usr/bin/env python3
"""Replace a unit-vocabulary alias slug (built from the file prefix) by the real one (ES B1 latam, 2026-11-26).

    python scripts/fix_vocab_slug_alias.py <course> <level> <unit id> [<unit id> ...] [--write]

The unit vocabulary skill is `<level>-<unit id>-vocab` (`b1-nation-nationalism-vocab`). Agents
sometimes build it from the lesson file prefix instead (`b1-nacionnacionalismo-vocab`), which the
validator rejects as an alias: two units of batch 7–12 did. For each unit this rewrites the alias in
the unit's exercise files. It only touches the exact alias string `"<level>-<prefix>-vocab"`, and only
when the prefix differs from the unit id. Re-lock the unit after (`lock_tags.py … --update`).
Without --write it prints the counts.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    if len(args) < 3:
        sys.exit(__doc__)
    course, level, uids = args[0], args[1].lower(), args[2:]
    units = {u["id"]: u for u in json.loads((ROOT / f"content/{course}/curriculum/units/{level}.json").read_text(encoding="utf-8"))}
    for uid in uids:
        prefix = units[uid]["stems"][0].rsplit("-", 1)[0]          # b1-nacionnacionalismo
        alias, real = f'"{prefix}-vocab"', f'"{level}-{uid}-vocab"'
        if alias == real:
            print(f"{uid}: prefix equals unit id, nothing to do")
            continue
        total = 0
        for stem in units[uid]["stems"]:
            f = ROOT / f"content/{course}/exercises/{level}/{stem}-ex.json"
            if not f.is_file():
                continue
            t = f.read_text(encoding="utf-8")
            n = t.count(alias)
            total += n
            if n and write:
                f.write_text(t.replace(alias, real), encoding="utf-8")
        print(f"{uid}: {total} alias(es) {alias} -> {real}" + ("" if write else " (dry run)"))


if __name__ == "__main__":
    main()
