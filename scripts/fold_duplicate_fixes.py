"""Fold a reader's duplicate `set` fixes before check_fixes.py (ROADMAP 153).

A reader sometimes writes two `set` fixes for the same exercise (one early,
one after a later rule change). check_fixes.py then puts one in the auto list
and one in the review list, and merge_fixes.py rightly refuses the pair
(ES B1 batch 17-27, twice). This folds them in the reader's own list: fixes
with the same file and id are merged into the first one, later keys winning,
and `kind`/`sure` take the more careful value (target, unsure).

    python scripts/fold_duplicate_fixes.py <fixes.json>      (rewrites the file)

Text fixes (old/new) are left alone: apply_replacements.py already refuses a
text that no longer matches.
"""
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    fixes = json.loads(path.read_text(encoding="utf-8"))
    first, out, folded = {}, [], 0
    for fix in fixes:
        if isinstance(fix, dict) and "set" in fix and fix.get("id"):
            key = (fix["file"], fix["id"], fix.get("variant"))
            if key in first:
                keep = first[key]
                keep["set"].update(fix["set"])
                if fix.get("kind") == "target":
                    keep["kind"] = "target"
                if fix.get("sure") is False:
                    keep["sure"] = False
                if fix.get("why") and fix["why"] not in keep.get("why", ""):
                    keep["why"] = (keep.get("why", "") + "; " + fix["why"]).strip("; ")
                folded += 1
                continue
            first[key] = fix
        out.append(fix)
    if folded:
        path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{folded} duplicate set fix(es) folded, {len(out)} fix(es) in {path}")


if __name__ == "__main__":
    main()
