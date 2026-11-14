"""Prepare a batch's two-stage apply when readers wrote extra lists (ROADMAP 153).

A reader's extra list (`extra-<unit>.json`, after check_fixes.py has split it
into `.auto.json` / `.review.json`) rewrites some of its own earlier `set`
fixes. Stage 1 applies the base lists minus the ids an extra replaces; stage 2
applies the extras. An extra `set` that carries only the fields it changed
used to drop the rest of the base fix (HU C1 core batch 1-8, 2026-11-14: 19
items lost their reviewed question, tag or category and reverted to the
generator's text). This script folds the base fix's fields under each extra
`set` (the extra's own fields win) and lists every field it carried, so
nothing is lost silently.

    python scripts/stage_extras.py <batch dir>

Reads <batch dir>/fixes-*.{auto,review}.json and extra-*.{auto,review}.json;
writes <batch dir>/base-<unit>.{auto,review}.json and
<batch dir>/staged-extra-<unit>.{auto,review}.json. Then:

    python scripts/merge_fixes.py <batch>/merged-1.json <batch>/base-*.json
    python scripts/merge_fixes.py <batch>/merged-2.json <batch>/staged-extra-*.json
    python scripts/apply_replacements.py <batch>/merged-1.json
    python scripts/apply_replacements.py <batch>/merged-2.json

Refuses (writes nothing) when one id has a `set` fix in two base lists or two
extra lists: that is merge_fixes.py's collision, settle it first.
"""
import json
import re
import sys
from pathlib import Path

KINDS = ("auto", "review")


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    batch = Path(sys.argv[1])
    base_files = sorted(p for k in KINDS for p in batch.glob(f"fixes-*.{k}.json"))
    extra_files = sorted(p for k in KINDS for p in batch.glob(f"extra-*.{k}.json"))
    if not extra_files:
        sys.exit(f"no extra-*.auto/review.json in {batch}: run check_fixes.py on the extra lists first")

    def index(files, label):
        out = {}
        for p in files:
            for f in load(p):
                if f.get("id") and f.get("set") is not None:
                    if f["id"] in out:
                        sys.exit(f"refused: {f['id']} has a set fix in two {label} lists ({out[f['id']][0].name}, {p.name})")
                    out[f["id"]] = (p, f)
        return out

    base = index(base_files, "base")
    extra = index(extra_files, "extra")

    written = []
    for p in base_files:
        keep = [f for f in load(p) if not (f.get("id") in extra and f.get("set") is not None)]
        out = batch / p.name.replace("fixes-", "base-", 1)
        out.write_text(json.dumps(keep, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        written.append(out)

    carried = 0
    for p in extra_files:
        fixes = load(p)
        for f in fixes:
            i = f.get("id")
            if i in base and f.get("set") is not None:
                bset = base[i][1]["set"]
                miss = {k: v for k, v in bset.items() if k not in f["set"]}
                if miss:
                    f["set"] = {**miss, **f["set"]}
                    carried += 1
                    print(f"  carried into {i}: {', '.join(sorted(miss))}")
        out = batch / ("staged-" + p.name)
        out.write_text(json.dumps(fixes, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        written.append(out)

    print(f"{len(extra)} extra set fix(es) replace base ones; base fields carried into {carried}; wrote {len(written)} file(s)")


if __name__ == "__main__":
    main()
