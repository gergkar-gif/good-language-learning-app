"""Check a reader's fix list before anyone applies it (ROADMAP 153).

The reader writes its fixes as JSON (format: scripts/apply_replacements.py),
one object per fix, with two more keys:

    "sure": false      the reader is unsure
    "kind": "target"   the fix changes target-language text (a sentence,
                       option, form or screen example), as opposed to an
                       English gloss, prompt, tag, challenge or screen
                       wording ("hungarian", the HU pass's name, is the same)

This applies the whole list to the working tree, runs check-content on the
unit, and always restores the files. Each fix ends up in one of three lists:

- rejected: its old text or id doesn't match once, it brings a new
  check-content finding on its exercise (a length give-away, an unmet word,
  a copied item…), or it leaves its exercise invalid under the course's
  schema (a `hint` or `english` on a multiple-choice item: es A1 units 2-5
  and 6-11, found only by validate-content after applying);
- review: it applies cleanly, but it is unsure or changes Hungarian; only
  these need the reviewer's eye (readers propose wrong target-language
  text a few times a level);
- auto: everything else.

    python scripts/check_fixes.py <course> <level> <unit id> <fixes.json> [--overwrite]

Writes <fixes>.auto.json and <fixes>.review.json next to the input; it
refuses to replace a review list that differs from the new one (the
reviewer's edits) unless --overwrite is given. Apply
with scripts/apply_replacements.py (auto as is; review after deleting what
the reviewer doesn't take), then lock_tags / check-content / freeze as usual.
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import apply_replacements as ar  # noqa: E402

spec = importlib.util.spec_from_file_location("check_content", ROOT / "scripts/check-content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


def schema_errors(texts):
    """{exercise id or file: message} for changed files their schema rejects
    (validate-content.py's TARGETS and schemas, one file at a time)."""
    from fnmatch import fnmatch
    from jsonschema import Draft7Validator
    spec_v = importlib.util.spec_from_file_location("validate_content", ROOT / "scripts/validate-content.py")
    vc = importlib.util.module_from_spec(spec_v)
    spec_v.loader.exec_module(vc)
    out = {}
    for rel, text in texts.items():
        parts = Path(rel).parts
        if len(parts) < 3 or parts[0] != "content":
            continue
        inner = Path(*parts[2:]).as_posix()
        name = next((n for n, g in vc.TARGETS.items() if fnmatch(inner, g)), None)
        path = ROOT / "content" / parts[1] / "schemas" / f"{name}.schema.json"
        if not name or not path.is_file():
            continue
        data = json.loads(text)
        for err in Draft7Validator(json.loads(path.read_text(encoding="utf-8"))).iter_errors(data):
            node, eid = data, None
            for step in err.absolute_path:
                node = node[step]
                if isinstance(node, dict) and node.get("id"):
                    eid = node["id"]
            out.setdefault(eid or rel, f"schema: {err.message[:160]}")
    return out


def findings(course, level, unit):
    return {(f[3], f[4], f[5]) for f in cc.run(cc.Source(), course, [level], unit)}


def unmet(course, level, unit):
    """{(item id, word)} from unmet-words.js for the unit's stems, from B1
    on, where check-content runs no `unmet-word` (HU B1 batches 43-53, 55-65
    and cit-08-14: the readers' own new options brought 17-85 unmet words a
    batch, found only after applying)."""
    if level in ("a1", "a2"):
        return set()
    units = json.loads((ROOT / f"content/{course}/curriculum/units/{level}.json").read_text(encoding="utf-8"))
    stems = next((u["stems"] for u in units if u["id"] == unit), None)
    if not stems:
        return set()
    r = subprocess.run(["node", str(ROOT / "scripts/unmet-words.js"), course, level, "--stems", ",".join(stems)],
                       cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    try:
        return {(h["id"], h["word"]) for h in json.loads(r.stdout or "[]")}
    except json.JSONDecodeError:
        return set()


def main():
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 4:
        sys.exit(__doc__)
    course, level, unit, fix_path = args[0], args[1].lower(), args[2], Path(args[3])
    fixes = [ar.norm(f) for f in json.loads(fix_path.read_text(encoding="utf-8"))]
    texts, errors = ar.apply(fixes)
    rejected = {n: e for n, e in errors.items()}

    before = findings(course, level, unit)
    unmet_before = unmet(course, level, unit)
    # a fix that adds a word to a vocabulary list makes it met for the other
    # fixes only once the word index is rebuilt (es A2 units 4, 10, 24 had a
    # fix rejected for a word another fix in the same list had just listed)
    voc = any(p.endswith("-voc.json") for p in texts)
    index = f"content/{course}/indexes/word-lesson-index.json"
    originals = {p: (ROOT / p).read_text(encoding="utf-8") for p in list(texts) + ([index] if voc else [])}
    try:
        for p, t in texts.items():
            (ROOT / p).write_text(t, encoding="utf-8")
        if voc:
            subprocess.run([sys.executable, str(ROOT / "scripts/build_word_lesson_index.py"), course],
                           cwd=ROOT, capture_output=True, check=True)
        after = findings(course, level, unit)
        unmet_after = unmet(course, level, unit)
    finally:
        for p, t in originals.items():
            (ROOT / p).write_text(t, encoding="utf-8")
    new = sorted(after - before)
    for eid, msg in schema_errors(texts).items():
        owners = [n for n, f in enumerate(fixes) if f.get("id") == eid]
        for n in owners:
            rejected.setdefault(n, msg)
        if not owners:
            new.append(("schema", eid, msg))

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
        (review if f.get("sure") is False or f.get("kind") in ("target", "hungarian") else auto).append(f)
    stem = fix_path.with_suffix("")
    out = json.dumps(review, ensure_ascii=False, indent=1) + "\n"
    old = Path(f"{stem}.review.json")
    if old.exists() and old.read_text(encoding="utf-8") != out and "--overwrite" not in flags:
        # a rerun once the reviewer has edited the review list would silently
        # undo the review (HU B1 batch 31-41: a Unit 37 rejection came back)
        sys.exit(f"{old} exists and differs (edited by the reviewer?); nothing written. "
                 "Check a new list under another name, or pass --overwrite.")
    Path(f"{stem}.auto.json").write_text(json.dumps(auto, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    Path(f"{stem}.review.json").write_text(json.dumps(review, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"{len(fixes)} fixes: {len(auto)} auto, {len(review)} to review, {len(rejected)} rejected")
    for n in sorted(rejected):
        print(f"  rejected #{n} ({fixes[n].get('id') or '-'}): {rejected[n]} :: {ar.describe(fixes[n])}")
    if unclaimed:
        print("  new findings no fix names by id (give text fixes an \"id\"; check these by hand):")
        for u in unclaimed:
            print("    " + u)
    brought = sorted(unmet_after - unmet_before)
    if brought:
        # reported, not rejected: citizenship units keep their words and list
        # them (user, 2026-10-22); core units rewrite them
        by = {}
        for eid, word in brought:
            by.setdefault(eid, []).append(word)
        print(f"  unmet words the fixes bring ({len(brought)}; list each on the first lesson using it, "
              "or rewrite it in a core unit; lookup misses of split verbs and names included):")
        for eid, words in by.items():
            print(f"    {eid}: {', '.join(words)}")
    print(f"wrote {stem}.auto.json, {stem}.review.json")


if __name__ == "__main__":
    main()
