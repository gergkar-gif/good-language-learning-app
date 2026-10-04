"""Find choice exercises whose correct option gives itself away with " / " (ROADMAP 126).

The pattern: the correct option is two phrases joined by " / "
("hypocrisy / sanctimony") while every wrong option is a single phrase
("generous charity"), so a learner can pick the answer by shape alone.

With --length it checks a second shape give-away instead: the correct
option is at least twice as long as the longest wrong option (and at least
15 characters longer), e.g. a full explanatory sentence beside two short
fragments (ROADMAP 130).

An exercise that is identical in es-es and es-latam is counted once, as
"es-both"; fix it once and apply the same change to both files.

Usage:
    python imports/review/check-slash-giveaway.py                # counts per course/level
    python imports/review/check-slash-giveaway.py --list         # every hit: id, file
    python imports/review/check-slash-giveaway.py hu b2 --list   # one course, one level
    python imports/review/check-slash-giveaway.py --length       # length give-away instead

Exit code 1 if any hit remains in the selected scope.
Files c1-21-* and c1-22-* (Hungarian) are being rewritten under ROADMAP 127
and are skipped here.
"""
import glob
import json
import os
import sys
from collections import Counter

COURSES = ("hu", "es-es", "es-latam")
SKIP_PREFIXES = ("c1-21-", "c1-22-")


def gives_away(o, k, length):
    wrong = [x for j, x in enumerate(o) if j != k]
    if length:
        longest = max(len(x) for x in wrong)
        return len(o[k]) >= 2 * longest and len(o[k]) - longest >= 15
    return " / " in o[k] and not any(" / " in x for x in wrong)


def hits(courses, levels, length=False):
    for course in courses:
        for f in sorted(glob.glob(f"content/{course}/exercises/*/*.json")):
            level = os.path.basename(os.path.dirname(f))
            if levels and level not in levels:
                continue
            if course == "hu" and os.path.basename(f).startswith(SKIP_PREFIXES):
                continue
            data = json.load(open(f, encoding="utf-8"))
            for e in data.get("exercises", []) if isinstance(data, dict) else []:
                o, k = e.get("options"), e.get("correct")
                if not (isinstance(o, list) and all(isinstance(x, str) for x in o)
                        and len(o) > 1 and isinstance(k, int) and 0 <= k < len(o)):
                    continue
                if gives_away(o, k, length):
                    yield course, level, e.get("id"), f.replace(os.sep, "/"), e


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    courses = [a for a in args if a in COURSES] or list(COURSES)
    levels = [a for a in args if a not in COURSES]
    found = list(hits(courses, levels, "--length" in sys.argv))
    # es-es and es-latam share A1/A2 and much of B1. An es-latam hit identical
    # to the es-es exercise in the same file is listed once, as "es-both":
    # fix it once and copy the fix to the other course.
    by = {(c, l, os.path.basename(f), i): e for c, l, i, f, e in found}
    merged = []
    for c, l, i, f, e in found:
        other = {"es-es": "es-latam", "es-latam": "es-es"}.get(c)
        if other and by.get((other, l, os.path.basename(f), i)) == e:
            if c == "es-latam":
                continue
            c, f = "es-both", f + " + es-latam copy"
        merged.append((c, l, i, f))
    found = merged
    counts = Counter((c, l) for c, l, _, _ in found)
    for (c, l), n in sorted(counts.items()):
        print(f"{c:9} {l:3} {n}")
    print(f"total: {len(found)}")
    if "--list" in sys.argv:
        for c, l, i, f in found:
            print(f"  {i}   ({f})")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
