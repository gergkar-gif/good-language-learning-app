"""Apply a filtered fix list as exact text replacements (ROADMAP 153).

Each old string must occur exactly once in its file, or nothing at all is
written; so a fix list item that no longer matches, or matches twice (the
same option text in two items), is caught before any file changes. Edit by
id with a short JSON script instead when the text isn't unique.

    python scripts/apply_replacements.py <fixes.json>

fixes.json: [["<file>", "<old>", "<new>"], ...]  (paths from the repo root)
"""
import json
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    fixes = json.load(open(sys.argv[1], encoding="utf-8"))
    texts, bad = {}, []
    for path, old, new in fixes:
        if path not in texts:
            texts[path] = open(path, encoding="utf-8").read()
        n = texts[path].count(old)
        if n != 1:
            bad.append(f"{n}x in {path}: {old[:70]}")
            continue
        texts[path] = texts[path].replace(old, new)
    if bad:
        sys.exit("nothing written; fix these first:\n  " + "\n  ".join(bad))
    for path, text in texts.items():
        open(path, "w", encoding="utf-8").write(text)
    print(f"applied {len(fixes)} replacement(s) in {len(texts)} file(s)")


if __name__ == "__main__":
    main()
