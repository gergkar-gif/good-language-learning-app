#!/usr/bin/env python3
"""Rebase a reader's text fixes that build on earlier fixes to the same text (ROADMAP 153).

Readers write a goal line three times (the goal array, the goal section, the
checklist) and often fix it twice: once alone, once inside a bigger block. The
second fix's `old` still holds the original line, which the first fix has
already changed, so check_fixes.py rejects it ("old text found 0x"). This
happened in three batches (B2 culture 18-24, 58-64 twice); rebasing by hand
is error-prone, so this does it the one safe way:

    python scripts/rebase_fixes.py <fixes.json> [--write]

It walks the list in order per file. A text fix whose `old` is not in the
file as left by the earlier fixes is rebased: every earlier applied
(old -> new) of the same file is applied to its `old` and `new`. If the
rebased `old` then occurs exactly once, the fix is kept rebased; otherwise it
is reported and left as it is. `set` fixes are not touched. Without --write it
only reports.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    path, write = Path(argv[0]), "--write" in argv
    fixes = json.loads(path.read_text(encoding="utf-8"))
    texts, applied = {}, {}
    rebased = failed = 0
    for n, f in enumerate(fixes):
        if "old" not in f or "file" not in f:
            continue
        fp = f["file"]
        if fp not in texts:
            p = ROOT / fp
            if not p.is_file():
                continue
            texts[fp] = p.read_text(encoding="utf-8")
            applied[fp] = []
        text = texts[fp]
        old, new = f["old"], f["new"]
        if text.count(old) != 1:
            r_old, r_new = old, new
            for a_old, a_new in applied[fp]:
                r_old, r_new = r_old.replace(a_old, a_new), r_new.replace(a_old, a_new)
            if text.count(r_old) == 1 and r_old != old:
                f["old"], f["new"] = r_old, r_new
                old, new = r_old, r_new
                rebased += 1
                print(f"rebased #{n} ({fp})")
            else:
                failed += 1
                print(f"cannot rebase #{n} ({fp}): old text found {text.count(r_old)}x")
                continue
        texts[fp] = text.replace(old, new, 1)
        applied[fp].append((old, new))
    print(f"{rebased} rebased, {failed} left as they are")
    if write and rebased:
        path.write_text(json.dumps(fixes, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
