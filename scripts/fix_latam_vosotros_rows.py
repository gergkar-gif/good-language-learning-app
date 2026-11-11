"""Drop the *vosotros* rows from es-latam grammar tables (ROADMAP 153, ES B1).

The core lesson files are shared by es-es and es-latam, so a conjugation
table mirrored from es-es carries a *vosotros* row that es-latam must not
have (check-content `latam-vosotros`). This removes exactly the table rows
whose first cell starts with "vosotros" (or "vosotros, vosotras").

It refuses rather than guesses: a file in which "vosotros"/"vosotras" still
occurs outside such a row after the removal is reported and left untouched
(prose that mentions the form needs a reader, not a script).

    python scripts/fix_latam_vosotros_rows.py <level> <stem prefix> [...] [--apply]

e.g. `b1 b1-03- b1-04-`. Without --apply it only lists what it would do.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROW = re.compile(r'\n[ \t]*\[\s*"vosotr[oa]s\b[^\[\]]*\],?', re.S)


def main():
    args = [a for a in sys.argv[1:] if a != "--apply"]
    apply = "--apply" in sys.argv
    if len(args) < 2:
        sys.exit(__doc__)
    level, prefixes = args[0], args[1:]
    folder = ROOT / "content" / "es-latam" / "grammar" / level
    files = sorted(f for f in folder.glob("*.json") if any(f.name.startswith(p) for p in prefixes))
    if not files:
        sys.exit(f"no grammar files match {prefixes} in {folder}")
    changed = refused = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        if not re.search(r"vosotr[oa]s", text, re.I):
            continue
        new, n = ROW.subn("", text)
        # a removed last row leaves a dangling comma before the closing bracket
        new = re.sub(r",(\s*\n[ \t]*\])", r"\1", new) if n else new
        if re.search(r"vosotr[oa]s", new, re.I) or n == 0:
            print(f"REFUSED {f.name}: vosotros outside a table row (read it by hand)")
            refused += 1
            continue
        import json
        json.loads(new)
        print(f"{'fixed' if apply else 'would fix'} {f.name}: {n} row(s)")
        if apply:
            f.write_text(new, encoding="utf-8")
        changed += 1
    print(f"{changed} file(s) {'fixed' if apply else 'to fix'}, {refused} refused")
    sys.exit(1 if refused else 0)


if __name__ == "__main__":
    main()
