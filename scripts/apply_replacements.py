"""Apply a filtered fix list (ROADMAP 153).

Two kinds of fix, in one JSON list:

    {"file": "<path>", "old": "<text>", "new": "<text>"}        exact text
    {"file": "<path>", "id": "<exercise or challenge id>",
     "set": {"<field>": <value>, ...}}                          JSON fields
    ["<path>", "<old>", "<new>"]                                same as the first

Each old text must occur exactly once in its file (after the fixes before
it), and each id must exist once, or nothing at all is written; so an item
that no longer matches, or matches twice (the same option text in two
items), is caught before any file changes. A `set` value of null deletes
the field (e.g. a stale `distractor_skills`). JSON files keep their
formatting (the indent is detected; a file that wouldn't round-trip is
refused for `set`). Other keys on a fix (`sure`, `kind`, `why`) are ignored
here; scripts/check_fixes.py uses them.

    python scripts/apply_replacements.py <fixes.json>
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(fix):
    if isinstance(fix, list):
        return {"file": fix[0], "old": fix[1], "new": fix[2]}
    return fix


def indent_of(text):
    m = re.search(r'\n( +)"', text)
    return len(m.group(1)) if m else 2


def set_fields(text, fid, fields):
    """Return (new text, error) after setting fields on the item with id fid."""
    data = json.loads(text)
    ind = indent_of(text)
    if json.dumps(data, ensure_ascii=False, indent=ind) + "\n" != text:
        return text, "file doesn't round-trip through JSON; use a text fix"
    hits = []
    items = data.get("exercises") if isinstance(data, dict) else None
    if isinstance(items, list):
        hits = [e for e in items if isinstance(e, dict) and e.get("id") == fid]
    else:
        table = data.get("challenges", data) if isinstance(data, dict) else {}
        if isinstance(table, dict) and isinstance(table.get(fid), dict):
            hits = [table[fid]]
    if len(hits) != 1:
        return text, f"id {fid} found {len(hits)}x"
    for k, v in fields.items():
        if v is None:
            hits[0].pop(k, None)
        else:
            hits[0][k] = v
    return json.dumps(data, ensure_ascii=False, indent=ind) + "\n", None


def apply(fixes):
    """(texts by path, errors by fix index). Writes nothing."""
    texts, errors = {}, {}
    for n, fix in enumerate(map(norm, fixes)):
        path = fix["file"]
        if path not in texts:
            p = ROOT / path
            if Path(path).is_absolute() or ".." in Path(path).parts:
                # a reader's absolute path into its own worktree applied there, not here (2026-10-16)
                errors[n] = f"path must be relative to the repository: {path}"
                continue
            if not p.is_file():
                errors[n] = f"no file {path}"
                continue
            texts[path] = p.read_text(encoding="utf-8")
        if "set" in fix:
            texts[path], err = set_fields(texts[path], fix.get("id"), fix["set"])
            if err:
                errors[n] = err
            continue
        c = texts[path].count(fix["old"])
        if c != 1:
            errors[n] = f"old text found {c}x"
            continue
        new_text = texts[path].replace(fix["old"], fix["new"])
        if path.endswith(".json"):
            # a text fix can break the JSON (an unescaped quote in "new");
            # check-content skips a file it can't parse, so nothing else catches it
            try:
                json.loads(new_text)
            except ValueError as e:
                errors[n] = f"leaves invalid JSON ({e})"
                continue
        texts[path] = new_text
    return texts, errors


def describe(fix):
    fix = norm(fix)
    return f"{fix['file']}: " + (f"{fix.get('id')} set {', '.join(fix['set'])}" if "set" in fix else fix["old"][:70])


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    fixes = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    texts, errors = apply(fixes)
    if errors:
        sys.exit("nothing written; fix these first:\n  " +
                 "\n  ".join(f"#{n} {errors[n]}: {describe(fixes[n])}" for n in sorted(errors)))
    for path, text in texts.items():
        (ROOT / path).write_text(text, encoding="utf-8")
    print(f"applied {len(fixes)} fix(es) in {len(texts)} file(s)")


if __name__ == "__main__":
    main()
