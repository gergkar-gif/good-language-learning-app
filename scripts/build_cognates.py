#!/usr/bin/env python3
"""Build the Spanish cognate allowance (ES B2, user's decision 2026-11-13).

From B2, a word no lesson lists counts as met when it is a transparent English
cognate (*crisis*, *modelo*, *transparencia*): scripts/unmet-words.js reads
imports/dictionary/cognates-es.json and skips those lemmas.

    python scripts/build_cognates.py <course> <level> [--write]

Runs `unmet-words.js <course> <level> --detail` on the level's visible units and
keeps a lemma only when EVERY dictionary reading of the word it was found as has
an English gloss word that the Spanish lemma predicts by spelling (suffix rules,
then a similarity of at least 0.84 with the same first letter). The comparison
is with the lemma's own gloss, so a false friend (*actual* "current", *éxito*
"success") can never pass; a cognate with a second, unrelated meaning passes
only if that meaning is cognate too. Lemmas under five letters are left out.
The reviewer reads the printed list before --write: remove a wrong line by
adding the lemma to "never" in the JSON file (kept across rebuilds). Without
--write it prints the candidates that are new.
"""
import difflib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "imports/dictionary/cognates-es.json"
SUFFIX = [("amiento", "ment"), ("imiento", "ment"), ("ización", "ization"), ("ización", "isation"), ("ción", "tion"),
          ("sión", "sion"), ("idad", "ity"), ("edad", "ety"), ("tad", "ty"), ("mente", "ly"), ("ificar", "ify"),
          ("izar", "ize"), ("izar", "ise"), ("ico", "ic"), ("ica", "ic"), ("ico", "ical"), ("ica", "ical"),
          ("oso", "ous"), ("osa", "ous"), ("ivo", "ive"), ("iva", "ive"), ("ancia", "ance"), ("encia", "ence"),
          ("encia", "ency"), ("ario", "ary"), ("aria", "ary"), ("orio", "ory"), ("oria", "ory"), ("ismo", "ism"),
          ("ista", "ist"), ("ía", "y"), ("ia", "y"), ("io", "y"), ("ura", "ure"), ("ante", "ant"), ("ente", "ent"),
          ("ado", "ate"), ("ar", "ate"), ("ar", "e"), ("ar", ""), ("er", ""), ("ir", ""), ("ir", "e"), ("o", ""),
          ("a", ""), ("e", ""), ("o", "e"), ("a", "e"), ("", "")]


def plain(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def predictions(lemma):
    out = set()
    for a, b in SUFFIX:
        if lemma.endswith(a):
            base = plain(lemma[:len(lemma) - len(a)] + b) if a else plain(lemma)
            for v in {base, re.sub(r"^es(?=[cpt])", "s", base)}:
                out |= {v, v.replace("f", "ph"), v.replace("cu", "qu"), v.replace("t", "th", 1), v.replace("i", "y", 1)}
    return out


def gloss_words(gloss):
    g = re.sub(r"\([^)]*\)", " ", gloss or "").lower()
    return {w for part in re.split(r"[,;/]", g) for w in [re.sub(r"^(to|a|an|the) ", "", part.strip())] if w and " " not in w}


def cognate(lemma, gloss):
    lemma = re.sub(r"^(el|la|los|las) ", "", lemma.lower())
    if len(lemma) < 5 or " " in lemma:
        return False
    preds = predictions(lemma)
    for w in gloss_words(gloss):
        w2 = plain(w)
        if w2 in preds:
            return True
        if w2[:1] == plain(lemma)[:1] or (plain(lemma).startswith("es") and w2[:1] == "s"):
            if max(difflib.SequenceMatcher(None, p, w2).ratio() for p in preds) >= 0.84:
                return True
    return False


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    course, level = args
    cur = json.loads((ROOT / f"content/{course}/curriculum/curriculum.json").read_text(encoding="utf-8"))
    stems = [l["id"].replace("lesson.", "").replace(".", "-") for u in cur["levels"][level.upper()]["units"]
             if not u.get("hidden") for l in u["lessons"]]
    old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.is_file() else {"from_level": "b2", "lemmas": [], "never": []}
    never = set(old.get("never", []))
    # the list must not hide its own candidates: run with the allowance moved aside
    backup = OUT.read_text(encoding="utf-8") if OUT.is_file() else None
    if backup is not None:
        OUT.unlink()
    try:
        r = subprocess.run(["node", "scripts/unmet-words.js", course, level, "--stems", ",".join(stems), "--detail"],
                           cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    finally:
        if backup is not None:
            OUT.write_text(backup, encoding="utf-8")
    if r.returncode:
        sys.exit(r.stderr)
    found = {}
    for h in json.loads(r.stdout):
        rs = h.get("readings") or []
        if rs and all(cognate(x["lemma"], x.get("gloss")) for x in rs):
            for x in rs:
                found[x["lemma"].lower()] = x.get("gloss") or ""
    lemmas = sorted((set(old.get("lemmas", [])) | set(found)) - never)
    new = sorted(set(found) - set(old.get("lemmas", [])) - never)
    for l in new:
        print(f"{l} | {found[l]}")
    print(f"{len(new)} new, {len(lemmas)} in all, {len(never)} never", file=sys.stderr)
    if "--write" in sys.argv:
        OUT.write_text(json.dumps({"_comment": "Spanish words that count as met from from_level because they are "
                                   "transparent English cognates (scripts/build_cognates.py; user, 2026-11-13). "
                                   "'never' lists lemmas the reviewer struck out.",
                                   "from_level": old.get("from_level", "b2"), "lemmas": lemmas,
                                   "never": sorted(never)}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
