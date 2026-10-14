"""Merge the filtered fix lists of one batch into one list (ROADMAP 153).

Two readers each write fixes for their own units, but a reader sometimes
fixes an item outside them (an earlier unit's consolidation, a shared
screen), so the same fix can come from both. apply_replacements.py would
apply both `set` fixes silently (the second overwrites the first) and fail
on a repeated text fix only if the first one removed the text. This joins
the lists and refuses rather than guesses when two fixes collide:

- two `set` fixes on the same file and id that set the same field;
- two text fixes on the same file with the same old text;
- two text fixes from different lists on the same file where one old text
  contains the other (within one list, later fixes may build on earlier
  ones, as apply_replacements.py applies them in order).

An exact duplicate (same file, id/old and same new value) is kept once and
reported. Nothing is written if anything collides; delete or merge the
colliding fixes by hand and run it again.

    python scripts/merge_fixes.py <out.json> <fixes.json> [<fixes.json> ...]

Then: python scripts/apply_replacements.py <out.json>
"""
import json
import sys
from pathlib import Path


def norm(fix):
    if isinstance(fix, list):
        return {"file": fix[0], "old": fix[1], "new": fix[2]}
    return fix


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    out, srcs = sys.argv[1], sys.argv[2:]
    merged, seen_set, seen_old = [], {}, {}
    problems, dupes = [], 0
    for src in srcs:
        for n, fix in enumerate(json.loads(Path(src).read_text(encoding="utf-8"))):
            fix = norm(fix)
            where = f"{Path(src).name}#{n}"
            f = fix.get("file")
            if "set" in fix:
                clash = False
                for field, value in fix["set"].items():
                    key = (f, fix.get("id"), field)
                    if key in seen_set:
                        prev_where, prev_value = seen_set[key]
                        if prev_value == value:
                            continue
                        problems.append(f"{where} and {prev_where} both set {field} on {fix.get('id')} ({f}) to different values")
                        clash = True
                if all((f, fix.get("id"), k) in seen_set and seen_set[(f, fix.get("id"), k)][1] == v
                       for k, v in fix["set"].items()):
                    dupes += 1
                    continue
                if not clash:
                    for field, value in fix["set"].items():
                        seen_set[(f, fix.get("id"), field)] = (where, value)
                    merged.append(fix)
            elif "old" in fix:
                old = fix["old"]
                same = seen_old.get((f, old))
                if same:
                    prev_where, prev_new = same
                    if prev_new == fix["new"]:
                        dupes += 1
                        continue
                    problems.append(f"{where} and {prev_where} both replace the same text in {f}: {old[:60]!r}")
                    continue
                # within one list, later fixes may build on earlier ones (applied in order)
                overlap = [w for (ff, o), (w, _) in seen_old.items()
                           if ff == f and (o in old or old in o) and not w.startswith(Path(src).name + "#")]
                if overlap:
                    problems.append(f"{where} overlaps {overlap[0]} in {f}: {old[:60]!r}")
                    continue
                seen_old[(f, old)] = (where, fix["new"])
                merged.append(fix)
            else:
                problems.append(f"{where}: neither `set` nor `old`")
    if problems:
        print(f"{len(problems)} collision(s); nothing written:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    Path(out).write_text(json.dumps(merged, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {out}: {len(merged)} fix(es) from {len(srcs)} list(s)" + (f", {dupes} exact duplicate(s) dropped" if dupes else ""))


if __name__ == "__main__":
    main()
