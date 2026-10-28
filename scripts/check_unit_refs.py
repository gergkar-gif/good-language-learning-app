"""Check the "You know *X* from A2 Unit 13" recaps on grammar screens
(ROADMAP 153, HU B1 batch 31-41, 2026-10-27: readers write these recaps,
and 2 of 10 in Unit 35 named a unit where the word isn't, one in Unit 39 a
form that is new on that screen; checking the words found 5 more in Units 19-35, where
the recap follows a skill title that names a word its screen never shows).

    python scripts/check_unit_refs.py <course> <level> [<unit id> ...]

For each italic word or phrase directly before "from <level> Unit <n>" or
"*X* (<level> Unit <n>)" right after it (reader B, batch 43-53), it
finds the first unit (in course order) that teaches it, as an italicised
form on a grammar screen other than the recapped word itself or as a vocabulary lemma, and reports the recap when that unit is
later than the one claimed, or when the word appears nowhere. Matching is by
text, so a recap of a form rather than a word (*adjuk hozzá* for the
imperative taught in A2 Unit 10, *kapcsolataimat* for plural possessed nouns)
can be a false positive: read each hit.
Exit 1 when anything is reported.
"""
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORDER = ["a1", "a2", "b1", "b2", "c1"]
REF = re.compile(r"\*([^*]+)\*(?:[^*]{0,40}?\bfrom | \()(A1|A2|B1|B2|C1) Unit (\d+)")
LETTER = "a-záéíóöőúüű"


def stem_of(f, pos=None):
    b = re.sub(r"-(voc|ex)$|-[abc]-gr$|-gr$", "", Path(f).stem)
    # citizenship screens carry a topic after the stem
    # (b1-karpatmedence-03-mig-egyidejuseg-gr is lesson b1-karpatmedence-03)
    while pos is not None and b not in pos and "-" in b:
        b = b.rsplit("-", 1)[0]
    return b


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    course, level, only = sys.argv[1], sys.argv[2].lower(), set(sys.argv[3:])
    pos, stems_of = {}, {}
    for li, lvl in enumerate(ORDER):
        p = ROOT / f"content/{course}/curriculum/units/{lvl}.json"
        if not p.exists():
            continue
        for i, u in enumerate(json.loads(p.read_text(encoding="utf-8"))):
            stems_of[(lvl, u["id"])] = u["stems"]
            for st in u["stems"]:
                pos[st] = (li, i + 1)
    texts = {}
    # where a word is taught: an italicised form on a grammar screen (the recapped
    # words themselves left out, they teach nothing) or a vocabulary-list lemma. A
    # passing use in an exercise is not teaching it (*bár* turns up in B1
    # Unit 5 items; its screen is Unit 29, so "*bár* from B1 Unit 9" was wrong).
    for f in glob.glob(str(ROOT / f"content/{course}/grammar/*/*.json")):
        p = pos.get(stem_of(f, pos))
        if p:
            text = REF.sub("", Path(f).read_text(encoding="utf-8"))
            texts.setdefault(p, []).append(" | ".join(re.findall(r"\*([^*]+)\*", text)).lower())
    for f in glob.glob(str(ROOT / f"content/{course}/vocabulary/*/*.json")):
        p = pos.get(stem_of(f, pos))
        if p:
            words = json.loads(Path(f).read_text(encoding="utf-8")).get("words", [])
            texts.setdefault(p, []).append(" | ".join(w.get("lemma", "") for w in words).lower())

    def first(word):
        pat = re.compile(rf"(?<![{LETTER}]){re.escape(word.lower())}")
        return next((p for p in sorted(texts) if any(pat.search(t) for t in texts[p])), None)

    wanted = None
    if only:
        wanted = {st for (lvl, uid), sts in stems_of.items() if lvl == level and uid in only for st in sts}
    hits = 0
    for f in sorted(glob.glob(str(ROOT / f"content/{course}/grammar/{level}/*.json"))):
        if wanted is not None and stem_of(f) not in wanted:
            continue
        for m in REF.finditer(Path(f).read_text(encoding="utf-8")):
            word = re.split(r"\.\.\.|…", m.group(1))[0].strip(" ,.'")
            if len(word) < 3 or word.startswith("-"):
                continue
            claim = (ORDER.index(m.group(2).lower()), int(m.group(3)))
            seen = first(word)
            if seen is None or seen > claim:
                where = "nowhere" if seen is None else f"{ORDER[seen[0]].upper()} Unit {seen[1]}"
                print(f"{Path(f).name}: *{word}* claimed from {m.group(2)} Unit {m.group(3)}, first appears {where}")
                hits += 1
    print(f"{hits} recap reference(s) to check")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
