#!/usr/bin/env python3
"""Plant es-latam B2 core into es-es (user, 2026-11-14).

The user's rule: core stays largely the same in both courses, apart from the
regional varieties; the culture tracks are where the two courses differ. So
this copies the 36 B2 core units (unit table rows, lessons, screens,
exercises, vocabulary, unit texts, challenges) from es-latam into es-es and
puts every string into Spain's words with course_variants.convert().

It refuses rather than guesses:
- a word convert() refuses (a gendered neighbour would also change) is left
  and listed;
- *ustedes* (Spain often wants *vosotros*) and a preterite with a
  recent-past marker (Spain wants the present perfect: *hoy he ido*) are
  listed, never changed;
- Unit 34 (dialect-variation-register) is copied unconverted: it teaches
  Latin American usage on purpose and is recast by hand for Spain.

Writes the list to imports/review/es-es-b2-plant/worksheet.md.

    python scripts/plant_es_es_b2.py [--force]

--force overwrites es-es B2 files that already exist (refuses otherwise).
"""
import glob
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import course_variants as cv  # noqa: E402

SRC, DST = ROOT / "content/es-latam", ROOT / "content/es-es"
HAND = {"dialect-variation-register"}          # recast by hand, not converted
SKIP = ("id", "unitIds", "targetSkills", "cefrLevel", "interlocutorVoice", "teaches",
        "distractor_skills", "ref", "exerciseRefs", "path", "stem", "stems")
# keys whose text is English: converted words there are left alone and not listed
ENGLISH = {"english", "explanation", "question", "goal", "title", "canDo", "scenario",
           "prompt", "cues", "hint", "translation", "tip", "body", "summary_en"}

spec = importlib.util.spec_from_file_location("cc", ROOT / "scripts/check-content.py")
cc = importlib.util.module_from_spec(spec)
_argv, sys.argv = sys.argv, ["check-content"]
spec.loader.exec_module(cc)
sys.argv = _argv

USTEDES = re.compile(r"\bustedes\b", re.I)
notes = []          # (file, json path, kind, text)


def walk(node, where, path=""):
    """Convert a JSON value to es-es words; note what must be checked by hand."""
    if isinstance(node, str):
        key = path.rsplit(".", 1)[-1].split("[")[0]
        if key in ENGLISH:
            return node
        new, changes, refused = cv.convert(node, "es-es")
        for r in refused:
            notes.append((where, path, "refused", f"{r}: {node[:120]}"))
        if USTEDES.search(new):
            notes.append((where, path, "ustedes", new[:140]))
        if cc.perfecto_marker(new):
            notes.append((where, path, "perfecto", new[:140]))
        return new
    if isinstance(node, list):
        return [walk(v, where, f"{path}[{i}]") for i, v in enumerate(node)]
    if isinstance(node, dict):
        return {k: (v if k in SKIP else walk(v, where, f"{path}.{k}" if path else k)) for k, v in node.items()}
    return node


def dump(obj, raw_sample):
    ind = 1 if raw_sample.startswith('{\n "') or raw_sample.startswith('[\n {') else 2
    return json.dumps(obj, ensure_ascii=False, indent=ind) + "\n"


def main():
    force = "--force" in sys.argv
    units = json.loads((SRC / "curriculum/units/b2.json").read_text(encoding="utf-8"))
    core = [u for u in units if u.get("track") == "core"]
    dst_table = DST / "curriculum/units/b2.json"
    if dst_table.exists() and not force:
        sys.exit(f"{dst_table} exists: rerun with --force to overwrite")

    files = []
    for u in core:
        for st in u["stems"]:
            for pat in (f"lessons/b2/{st}.json", f"exercises/b2/{st}-ex.json",
                        f"grammar/b2/{st}-*.json", f"vocabulary/b2/{st}-voc.json"):
                files += [(Path(p), u["id"]) for p in glob.glob(str(SRC / pat))]
        n = u["stems"][0][3:5]
        files.append((SRC / f"stories/classics/b2/b2-{n}.json", u["id"]))

    copied = converted = 0
    for src, uid in files:
        if not src.exists():
            notes.append((str(src.relative_to(ROOT)), "", "missing", "source file not found"))
            continue
        dst = DST / src.relative_to(SRC)
        dst.parent.mkdir(parents=True, exist_ok=True)
        raw = src.read_text(encoding="utf-8")
        if uid in HAND:
            shutil.copy2(src, dst)
        else:
            old = json.loads(raw)
            new = walk(old, str(dst.relative_to(ROOT)))
            if new == old:          # nothing to convert: keep the file byte for byte
                shutil.copy2(src, dst)
            else:
                converted += 1
                dst.write_text(dump(new, raw), encoding="utf-8")
        copied += 1

    dst_table.write_text(dump(core, "[\n {"), encoding="utf-8")

    # challenges: one entry per core stem, converted like the rest
    stems = {st for u in core for st in u["stems"]}
    hand_stems = {st for u in core if u["id"] in HAND for st in u["stems"]}
    sc = json.loads((SRC / "curriculum/challenges.json").read_text(encoding="utf-8"))
    dp = DST / "curriculum/challenges.json"
    draw = dp.read_text(encoding="utf-8")
    dc = json.loads(draw)
    added = 0
    for k, v in sc["challenges"].items():
        if k in stems:
            if k in dc["challenges"] and not force:
                sys.exit(f"es-es challenge {k} exists: rerun with --force")
            dc["challenges"][k] = v if k in hand_stems else walk(v, "content/es-es/curriculum/challenges.json", k)
            added += 1
    dp.write_text(dump(dc, draw), encoding="utf-8")

    out = ROOT / "imports/review/es-es-b2-plant/worksheet.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# es-es B2 plant: items to check by hand", "",
             f"Copied {copied} files from es-latam B2 core ({converted} changed by the word conversion), "
             f"{added} challenges, unit table of {len(core)} core units.",
             "Unit 34 (`dialect-variation-register`) copied unconverted: recast for Spain by hand.", "",
             "| kind | file | where | text |", "|---|---|---|---|"]
    lines += [f"| {k} | `{f}` | `{p}` | {t.replace('|', '/')} |" for f, p, k, t in notes]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    kinds = {}
    for *_, k, _t in notes:
        kinds[k] = kinds.get(k, 0) + 1
    print(f"copied {copied} files ({converted} converted), {added} challenges; to check by hand: {kinds or 'none'}")
    print(f"worksheet: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
