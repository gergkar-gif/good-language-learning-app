#!/usr/bin/env python3
"""
Build a reverse conjugation index from imports/verbs/*.json.

imports/verbs/*.json maps lemma -> conjugated forms. For tap-to-translate
in the Reader, we need the opposite: given a conjugated word a learner
taps, find its lemma and grammatical analysis (mood, tense, person,
number). This script inverts the whole dataset into that lookup.

Data source: Fred Jehle's Spanish verb conjugation database (see the
`attribution` field in each imports/verbs/*.json file) — CC BY-NC-SA 3.0,
non-commercial use only.

Output: generated/indexes/verb-index.json
    { "<surface form>": [ { lemma, mood, tense, person, number, ... }, ... ] }

A form can map to more than one analysis — Spanish conjugation is
genuinely ambiguous in places (e.g. "hablaba" is both yo and él/ella
imperfecto indicative). Callers should treat the list as candidates,
not assume there's exactly one right answer.

Usage:
    python scripts/build_verb_index.py
"""
import json
import gzip
from pathlib import Path
from collections import defaultdict

VERBS_DIR = Path("imports/verbs")
OUTPUT_DIR = Path("generated/indexes")
OUTPUT_FILE = OUTPUT_DIR / "verb-index.json"

# Matches the person-label convention already used in engine/verbs/speed.js
PERSON_META = {
    "yo":       {"person": 1, "number": "singular"},
    "tu":       {"person": 2, "number": "singular"},
    "ud":       {"person": 3, "number": "singular"},
    "nosotros": {"person": 1, "number": "plural"},
    "vosotros": {"person": 2, "number": "plural"},
    "uds":      {"person": 3, "number": "plural"},
}

# These tenses store "<auxiliary> <participle>" (e.g. "he abandonado",
# "hubiese bañado"). The auxiliary is just a conjugated form of haber,
# already indexed in its own right when haber.json is processed; only the
# participle is worth indexing here, and it's person-invariant (the
# person/number lives in the auxiliary, not the participle) so it only
# needs recording once per verb, not once per person.
COMPOUND_TENSES = {
    "presentePerfecto", "futuroPerfecto", "pluscuamperfecto",
    "preteritoAnterior", "condicionalPerfecto", "pluscuamperfectoAlt",
}

REFLEXIVE_PREFIXES = ["me ", "te ", "se ", "nos ", "os "]
REFLEXIVE_SUFFIXES = ["se", "te", "nos", "os"]


def strip_reflexive(form, is_reflexive):
    """Strip a leading or trailing reflexive pronoun so the index key
    matches the single word a learner actually taps, not the full phrase.
    Prefix forms (regular tenses, e.g. "me baño" -> "baño") are exact.
    Suffix forms (infinitive/gerund/affirmative imperative, e.g.
    "báñate") are approximate: Spanish shifts the stress accent on those
    forms in a way plain suffix-stripping can't undo, so these entries
    are flagged approx=True rather than silently trusted."""
    if not is_reflexive:
        return form, False
    for p in REFLEXIVE_PREFIXES:
        if form.startswith(p):
            return form[len(p):], False
    for s in REFLEXIVE_SUFFIXES:
        if form.endswith(s) and len(form) > len(s) + 2:
            return form[:-len(s)], True
    return form, False


def add(index, key, analysis, approx=False):
    if not key:
        return
    key = key.lower()
    if approx:
        analysis = dict(analysis, approx=True)
    if analysis not in index[key]:
        index[key].append(analysis)


def build_index():
    index = defaultdict(list)
    stats = {"verbs": 0, "errors": 0}

    for f in sorted(VERBS_DIR.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            stats["errors"] += 1
            continue
        stats["verbs"] += 1

        lemma = data.get("infinitivo", f.stem)
        is_reflexive = lemma.endswith("se")

        if lemma:
            key, approx = strip_reflexive(lemma, is_reflexive)
            add(index, key, {"lemma": lemma, "form": "infinitive"}, approx)

        for slot, form_type in [("gerundio", "gerund"), ("participioPasado", "participle")]:
            form = data.get(slot)
            if not form:
                continue
            key, approx = strip_reflexive(form, is_reflexive)
            add(index, key, {"lemma": lemma, "form": form_type}, approx)

        for mood in ("indicativo", "subjuntivo"):
            for tense, persons in (data.get(mood) or {}).items():
                if tense in COMPOUND_TENSES:
                    sample = next((v for v in persons.values() if v and " " in v), None)
                    if sample:
                        participle = sample.split(" ")[-1]
                        add(index, participle, {"lemma": lemma, "form": "participle"})
                    continue
                for person, form in persons.items():
                    if not form:
                        continue
                    key, approx = strip_reflexive(form, is_reflexive)
                    meta = PERSON_META.get(person, {})
                    add(index, key, {
                        "lemma": lemma, "mood": mood, "tense": tense,
                        "person": meta.get("person"), "number": meta.get("number")
                    }, approx)

        for polarity in ("afirmativo", "negativo"):
            for person, form in (data.get(polarity) or {}).items():
                if not form:
                    continue
                key, approx = strip_reflexive(form, is_reflexive)
                meta = PERSON_META.get(person, {})
                add(index, key, {
                    "lemma": lemma, "mood": "imperative", "polarity": polarity,
                    "person": meta.get("person"), "number": meta.get("number")
                }, approx)

    return index, stats


def main():
    index, stats = build_index()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

    raw_size = OUTPUT_FILE.stat().st_size
    gz_size = len(gzip.compress(OUTPUT_FILE.read_bytes(), compresslevel=9))
    ambiguous = sum(1 for v in index.values() if len(v) > 1)
    approx = sum(1 for v in index.values() for a in v if a.get("approx"))

    print(f"Verbs processed: {stats['verbs']} (errors: {stats['errors']})")
    print(f"Unique forms:    {len(index)}")
    print(f"Ambiguous forms: {ambiguous} ({100*ambiguous/len(index):.1f}%)")
    print(f"Approx forms:    {approx} (reflexive suffix cases)")
    print(f"Output:          {OUTPUT_FILE} ({raw_size:,} bytes, {gz_size/1024:.0f} KB gzipped)")


if __name__ == "__main__":
    main()
