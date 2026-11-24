#!/usr/bin/env python3
"""Plant an es-latam level test into es-es (ES C1 test, 2026-11-24).

A level test is written once in es-latam and planted in es-es with Spain's words,
like the C1 units (scripts/plant_es_es_c1.py). Unlike a unit, a test's `question`,
`prompt` and section `title` fields are Spanish, so every string is converted except
the English `intro` and the test's own `title`. It refuses rather than guesses: words
convert() refuses, *ustedes* and a preterite with a recent-past marker are listed,
never changed.

    python scripts/plant_es_es_test.py <level> [--force]

Worksheet: imports/review/es-es-tests/<level>-test.md
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import plant_es_es_b2 as b2  # noqa: E402  (cv, cc, USTEDES)

# Words kept as written: es-es lists *sala* (C1 Unit 31) and *sala de estudio* is standard in Spain,
# but convert() turns it into *salón* (and broke *el salón se queda pequeña*, C1 test, 2026-11-24)
KEEP = re.compile(r"\b(sala|salas)\b")
SKIP = {"id", "type", "teaches", "correct", "level", "passMark", "speaker", "gender", "intro"}


def walk(node, notes, path=""):
    if isinstance(node, str):
        kept = KEEP.findall(node)
        guarded = KEEP.sub("\u0000", node)
        new, changes, refused = b2.cv.convert(guarded, "es-es")
        for w in kept:
            new = new.replace("\u0000", w, 1)
        changes = [c for c in changes if "\u0000" not in str(c)]
        for c in changes:
            notes.append((path, "changed", f"{c}: {new[:140]}"))
        for r in refused:
            notes.append((path, "refused", f"{r}: {node[:140]}"))
        if b2.USTEDES.search(new):
            notes.append((path, "ustedes", new[:140]))
        if b2.cc.perfecto_marker(new):
            notes.append((path, "perfecto", new[:140]))
        return new
    if isinstance(node, list):
        return [walk(v, notes, f"{path}[{i}]") for i, v in enumerate(node)]
    if isinstance(node, dict):
        return {k: (v if k in SKIP or (k == "title" and not path) else walk(v, notes, f"{path}.{k}" if path else k))
                for k, v in node.items()}
    return node


def main(argv):
    force = "--force" in argv
    levels = [a.lower() for a in argv if not a.startswith("--")]
    if len(levels) != 1:
        sys.exit(__doc__)
    lv = levels[0]
    src = b2.SRC / f"tests/{lv}-test.json"
    dst = b2.DST / f"tests/{lv}-test.json"
    if not src.exists():
        sys.exit(f"{src.relative_to(ROOT)} does not exist")
    if dst.exists() and not force:
        sys.exit(f"{dst.relative_to(ROOT)} exists: rerun with --force to overwrite")
    raw = src.read_text(encoding="utf-8")
    notes = []
    new = walk(json.loads(raw), notes)
    # the reading section's id names the course
    rs = new.get("readingSection")
    if rs and rs.get("id", "").endswith("-es-latam"):
        rs["id"] = rs["id"][: -len("-es-latam")] + "-es-es"
    dst.write_text(json.dumps(new, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    out = ROOT / f"imports/review/es-es-tests/{lv}-test.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# es-es {lv.upper()} test plant: what changed and what to check by hand", "",
             "| kind | where | text |", "|---|---|---|"]
    lines += [f"| {k} | `{p}` | {t.replace('|', '/')} |" for p, k, t in notes]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    kinds = {}
    for _p, k, _t in notes:
        kinds[k] = kinds.get(k, 0) + 1
    print(f"{dst.relative_to(ROOT)} written; {kinds or 'no changes'}; worksheet {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
