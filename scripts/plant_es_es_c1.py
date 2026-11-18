#!/usr/bin/env python3
"""Plant finished es-latam C1 core units into es-es (user, 2026-11-18).

C1 core is written once in es-latam and planted in es-es: mostly identical,
with Spain's words and small differences where relevant (imports/review/
es-c1-plan/level-plan.md). Same conversion as the B2 plant
(scripts/plant_es_es_b2.py: course_variants.convert on every Spanish string,
English fields left alone), but per unit, since C1 is written unit by unit,
and the unit's text is found through lesson 05's story section.

It refuses rather than guesses: a word convert() refuses, *ustedes* (Spain
may want *vosotros*) and a preterite with a recent-past marker (Spain wants
the present perfect) are listed in the worksheet, never changed. Fix those by
hand in es-es after planting.

    python scripts/plant_es_es_c1.py <unit id> [<unit id> ...] [--force]

The es-es unit table already holds every C1 unit (identical to es-latam's).
--force overwrites es-es files and challenges that already exist.
Worksheet: imports/review/es-es-c1-plant/<unit id>.md
"""
import glob
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import plant_es_es_b2 as b2  # noqa: E402  (walk, dump, notes)

SRC, DST = b2.SRC, b2.DST
LEVEL = "c1"
# Sentence-builder tiles are converted one by one, so the gender guard of
# convert() never sees the article on the next tile (*la* + *sala* became
# *la salón*, c1-02-consolidation.ex11, 2026-11-18). Tiles and solutions are
# copied unchanged and listed when they hold a course-variant word.
b2.SKIP = tuple(b2.SKIP) + ("tiles", "solution")


def note_tiles(node, where, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("tiles", "solution") and isinstance(v, list):
                found = [w for t in v if isinstance(t, str) for w in b2.cv.find(t, "es-es")]
                if found:
                    b2.notes.append((where, f"{path}.{k}", "tiles", ", ".join(dict.fromkeys(found))))
            else:
                note_tiles(v, where, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            note_tiles(v, where, f"{path}[{i}]")


def unit_files(u):
    files = []
    for st in u["stems"]:
        for pat in (f"lessons/{LEVEL}/{st}.json", f"exercises/{LEVEL}/{st}-ex.json",
                    f"grammar/{LEVEL}/{st}-*.json", f"vocabulary/{LEVEL}/{st}-voc.json"):
            files += [Path(p) for p in glob.glob(str(SRC / pat))]
        lesson = SRC / f"lessons/{LEVEL}/{st}.json"
        if lesson.exists():
            for s in json.loads(lesson.read_text(encoding="utf-8")).get("sections", []):
                if s.get("type") == "story" and s.get("ref"):
                    files.append(SRC / s["ref"])
    return files


def plant(u, force):
    b2.notes.clear()
    copied = converted = 0
    for src in unit_files(u):
        dst = DST / src.relative_to(SRC)
        if dst.exists() and not force:
            sys.exit(f"{dst.relative_to(ROOT)} exists: rerun with --force to overwrite")
        dst.parent.mkdir(parents=True, exist_ok=True)
        raw = src.read_text(encoding="utf-8")
        old = json.loads(raw)
        new = b2.walk(old, str(dst.relative_to(ROOT)))
        note_tiles(old, str(dst.relative_to(ROOT)))
        if new == old:              # nothing to convert: keep the file byte for byte
            shutil.copy2(src, dst)
        else:
            converted += 1
            dst.write_text(b2.dump(new, raw), encoding="utf-8")
        copied += 1
    if not copied:
        sys.exit(f"{u['id']}: no es-latam files to plant")

    sc = json.loads((SRC / "curriculum/challenges.json").read_text(encoding="utf-8"))
    dp = DST / "curriculum/challenges.json"
    draw = dp.read_text(encoding="utf-8")
    dc = json.loads(draw)
    added = 0
    for st in u["stems"]:
        if st in sc["challenges"]:
            if st in dc["challenges"] and not force:
                sys.exit(f"es-es challenge {st} exists: rerun with --force")
            dc["challenges"][st] = b2.walk(sc["challenges"][st], "content/es-es/curriculum/challenges.json", st)
            added += 1
    dp.write_text(b2.dump(dc, draw), encoding="utf-8")

    out = ROOT / f"imports/review/es-es-c1-plant/{u['id']}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# es-es C1 plant, {u['id']}: items to check by hand", "",
             f"Copied {copied} files ({converted} changed by the word conversion), {added} challenges.", "",
             "| kind | file | where | text |", "|---|---|---|---|"]
    lines += [f"| {k} | `{f}` | `{p}` | {t.replace('|', '/')} |" for f, p, k, t in b2.notes]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    kinds = {}
    for *_, k, _t in b2.notes:
        kinds[k] = kinds.get(k, 0) + 1
    print(f"{u['id']}: copied {copied} files ({converted} converted), {added} challenges; "
          f"to check by hand: {kinds or 'none'}; worksheet {out.relative_to(ROOT)}")


def main(argv):
    force = "--force" in argv
    ids = [a for a in argv if not a.startswith("--")]
    if not ids:
        sys.exit(__doc__)
    table = json.loads((SRC / f"curriculum/units/{LEVEL}.json").read_text(encoding="utf-8"))
    dst_ids = {u["id"] for u in json.loads((DST / f"curriculum/units/{LEVEL}.json").read_text(encoding="utf-8"))}
    by_id = {u["id"]: u for u in table}
    for uid in ids:
        if uid not in by_id or uid not in dst_ids:
            sys.exit(f"unit {uid!r} is not in both C1 unit tables")
        plant(by_id[uid], force)


if __name__ == "__main__":
    main(sys.argv[1:])
