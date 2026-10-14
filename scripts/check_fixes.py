"""Check a reader's fix list before anyone applies it (ROADMAP 153).

The reader writes its fixes as JSON (format: scripts/apply_replacements.py),
one object per fix, with two more keys:

    "sure": false      the reader is unsure
    "kind": "hungarian"  the fix changes Hungarian text (a sentence, option,
                         form or screen example), as opposed to an English
                         gloss, prompt, tag, challenge or screen wording

This applies the whole list to the working tree, runs check-content on the
unit, and always restores the files. Each fix ends up in one of three lists:

- rejected: its old text or id doesn't match once, or it brings a new
  check-content finding on its exercise (a length give-away, an unmet word,
  a copied item…);
- review: it applies cleanly, but it is unsure or changes Hungarian; only
  these need the reviewer's eye (readers propose wrong Hungarian a few
  times a level);
- auto: everything else.

    python scripts/check_fixes.py <course> <level> <unit id> <fixes.json>

Writes <fixes>.auto.json and <fixes>.review.json next to the input. Apply
with scripts/apply_replacements.py (auto as is; review after deleting what
the reviewer doesn't take), then lock_tags / check-content / freeze as usual.
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import apply_replacements as ar  # noqa: E402

spec = importlib.util.spec_from_file_location("check_content", ROOT / "scripts/check-content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


def findings(course, level, unit):
    return {(f[3], f[4], f[5]) for f in cc.run(cc.Source(), course, [level], unit)}


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    course, level, unit, fix_path = sys.argv[1], sys.argv[2].lower(), sys.argv[3], Path(sys.argv[4])
    fixes = [ar.norm(f) for f in json.loads(fix_path.read_text(encoding="utf-8"))]
    texts, errors = ar.apply(fixes)
    rejected = {n: e for n, e in errors.items()}

    before = findings(course, level, unit)
    originals = {p: (ROOT / p).read_text(encoding="utf-8") for p in texts}
    try:
        for p, t in texts.items():
            (ROOT / p).write_text(t, encoding="utf-8")
        after = findings(course, level, unit)
    finally:
        for p, t in originals.items():
            (ROOT / p).write_text(t, encoding="utf-8")
    new = sorted(after - before)

    unclaimed = []
    for check, eid, msg in new:
        owners = [n for n, f in enumerate(fixes) if f.get("id") == eid]
        if not owners:
            unclaimed.append(f"{check} {eid}: {msg}")
        for n in owners:
            rejected.setdefault(n, f"brings {check}: {msg}")

    auto, review = [], []
    for n, f in enumerate(fixes):
        if n in rejected:
            continue
        (review if f.get("sure") is False or f.get("kind") == "hungarian" else auto).append(f)
    stem = fix_path.with_suffix("")
    Path(f"{stem}.auto.json").write_text(json.dumps(auto, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    Path(f"{stem}.review.json").write_text(json.dumps(review, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"{len(fixes)} fixes: {len(auto)} auto, {len(review)} to review, {len(rejected)} rejected")
    for n in sorted(rejected):
        print(f"  rejected #{n} ({fixes[n].get('id') or '-'}): {rejected[n]} :: {ar.describe(fixes[n])}")
    if unclaimed:
        print("  new findings no fix names by id (give text fixes an \"id\"; check these by hand):")
        for u in unclaimed:
            print("    " + u)
    print(f"wrote {stem}.auto.json, {stem}.review.json")


if __name__ == "__main__":
    main()
