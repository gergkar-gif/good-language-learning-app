#!/usr/bin/env python3
"""
Import a Hungarian-English dictionary and a noun/adjective case-form index
from Kaikki's Wiktionary extraction.

Unlike Spanish (scripts/import_dictionary.py, sourced from an already-cleaned
doozan/spanish_data export), no pre-cleaned Hungarian-English dataset exists,
so this reads the raw Wiktionary extraction directly. Source:
https://kaikki.org/dictionary/Hungarian/ (English Wiktionary, Hungarian
entries; CC-BY-SA 4.0 + GFDL — see https://kaikki.org for details).

Both outputs come from a single pass over the same 583MB source file rather
than two scripts each re-reading it:

  imports/dictionary/hungarian-en.json  lemma -> { en, pos }
      One real (non-form-of) entry per lemma, mirroring spanish-en.json's
      shape. "Real" excludes Wiktionary pages that exist only to point at
      an inflected form of another word (see FORM_OF_TAG below) — those
      carry no independent gloss worth surfacing as a translation.

  content/hu/indexes/word-index.json  surface form -> [ { lemma, pos,
      case?, number?, person?, ownerNumber? }, ... ]
      Harvested from each noun/adjective's own declension table (source
      wiktextract already generates: 18 cases x singular/plural, plus the
      12 possessive-nominative slots — person x owner-number x number),
      but only for lemmas within FREQ_CUTOFF of content/hu/indexes/
      frequency.json (run build_hu_frequency.py first). Indexing every
      dictionary lemma's full ~30-form paradigm would put this file at
      well over 100MB uncompressed — the brief is explicit that Hungarian's
      productive morphology shouldn't be exhaustively enumerated. Common
      words dominate real reading by a wide margin (Zipf's law), so this
      still covers the bulk of ordinary text; anything outside the cutoff
      still resolves via the dictionary (which is NOT rank-limited) plus
      engine/morphology/hungarian.js's runtime suffix stripping — it just
      skips the pre-baked friendly case label for rarer words.
      Verbs are deliberately excluded: Wiktionary's Hungarian conjugation
      template ("hu-conj-ok") mistags which surface form goes with which
      person for this dataset (e.g. "olvasok" turns up tagged as
      2nd-person) even though the surface forms themselves are correct.
      Regular verb conjugation is handled instead by the rule-based
      analyser in engine/morphology/hungarian.js, which the A1 curriculum's
      own grammar lessons already describe as regular endings — a better
      fit than trusting a mistagged table. This index only ever needs to
      resolve what's actually regular and declension-table-clean; anything
      else (irregular stems, case+possessive stacking) falls to that same
      runtime analyser.

Usage:
    python scripts/import_hu_dictionary.py

Both files are cached/gitignored raw data — see .gitignore.
"""
import gzip
import json
import urllib.request
from pathlib import Path

SOURCE_URL = "https://kaikki.org/dictionary/Hungarian/kaikki.org-dictionary-Hungarian.jsonl"

CACHE_DIR = Path("imports/dictionary")
RAW_CACHE = CACHE_DIR / "hu-wiktionary.jsonl.raw"
DICT_OUTPUT = CACHE_DIR / "hungarian-en.json"
INDEX_OUTPUT_DIR = Path("content/hu/indexes")
INDEX_OUTPUT = INDEX_OUTPUT_DIR / "word-index.json"
FREQUENCY_FILE = INDEX_OUTPUT_DIR / "frequency.json"

# Only lemmas ranked within this cutoff get their case/possessive paradigm
# pre-baked into word-index.json. Run build_hu_frequency.py before this
# script. See the module docstring for why this is capped at all.
FREQ_CUTOFF = 8000

# Kaikki/wiktextract POS tags -> the vocabulary the app already uses
# (matches import_dictionary.py's POS_MAP for the Spanish side).
POS_MAP = {
    "noun": "noun", "verb": "verb", "adj": "adjective", "adv": "adverb",
    "pron": "pronoun", "num": "numeral", "intj": "interjection",
    "conj": "conjunction", "postp": "postposition", "det": "determiner",
    "article": "article", "prep": "preposition", "particle": "particle",
    "phrase": "phrase", "proverb": "proverb",
}
# Not useful as a primary tap-lookup target: affixes, punctuation, proper
# names (a name dictionary entry is almost never what a learner wants when
# tapping running text), symbols.
SKIP_POS = {
    "suffix", "prefix", "infix", "interfix", "punct", "symbol",
    "character", "contraction", "name",
}

# Wiktextract marks a sense as pointing at another word's inflected form
# with this tag (e.g. "nominative plural of ház"). These aren't primary
# definitions and would pollute the dictionary with glosses like
# "accusative plural of ház" instead of an actual translation.
FORM_OF_TAG = "form-of"

# Senses tagged like this are deprioritised but not dropped outright — a
# rare/dated sense is still better than no dictionary entry.
DEPRIORITISE_TAGS = {"obsolete", "archaic", "dated", "rare"}

# Declension-table rows that describe the template itself rather than an
# actual inflected form (see the "ház" example: 'no-table-tags',
# 'hu-infl-nom', 'back harmony', '-a-' all show up as fake "forms" with
# these tags).
META_FORM_TAGS = {"table-tags", "inflection-template", "class"}

CASE_MAP = {
    "nominative": "nom", "accusative": "acc", "dative": "dat",
    "instrumental": "ins", "causal-final": "cfi", "translative": "tra",
    "terminative": "ter", "essive-formal": "esf", "essive-modal": "esm",
    "inessive": "ine", "superessive": "sup", "adessive": "ade",
    "illative": "ill", "sublative": "sub", "allative": "all",
    "elative": "ela", "delative": "del", "ablative": "abl",
}
PERSON_TAGS = {"first-person": 1, "second-person": 2, "third-person": 3}


def download():
    print(f"Downloading {SOURCE_URL} ...")
    print("This file is ~583MB; it is cached and gitignored after the first run.")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)
    print(f"Downloaded {RAW_CACHE.stat().st_size:,} bytes")


def primary_gloss(senses):
    """First usable gloss from a non-form-of sense, preferring one that
    isn't flagged obsolete/archaic/dated/rare if a better one exists."""
    candidates = []
    for sense in senses or []:
        tags = set(sense.get("tags") or [])
        if FORM_OF_TAG in tags:
            continue
        glosses = sense.get("glosses") or []
        if not glosses:
            continue
        candidates.append((bool(tags & DEPRIORITISE_TAGS), glosses[0]))
    if not candidates:
        return None
    candidates.sort(key=lambda c: c[0])  # non-deprioritised first
    return candidates[0][1]


def extract_case_forms(entry, lemma, pos):
    """Noun/adjective declension-table rows -> word-index entries. Only
    'declension' rows are used (see module docstring on why verb
    'conjugation' rows are skipped)."""
    out = []
    for f in entry.get("forms") or []:
        if f.get("source") != "declension":
            continue
        tags = set(f.get("tags") or [])
        if tags & META_FORM_TAGS or "error-unrecognized-form" in tags:
            continue
        form = f.get("form")
        if not form or form == "-" or " " in form:
            continue

        analysis = {"lemma": lemma, "pos": pos}
        case = next((CASE_MAP[t] for t in tags if t in CASE_MAP), None)
        if case:
            analysis["case"] = case
        person = next((PERSON_TAGS[t] for t in tags if t in PERSON_TAGS), None)
        if person:
            analysis["person"] = person
            analysis["ownerNumber"] = "pl" if "plural" in tags else "sg"
            analysis["number"] = "pl" if "possessed-many" in tags else "sg"
        elif "plural" in tags or "possessed-many" in tags:
            analysis["number"] = "pl"
        elif "singular" in tags or "possessed-single" in tags:
            analysis["number"] = "sg"

        if not case and person is None and "number" not in analysis:
            continue  # a form row we don't recognise; skip rather than guess
        out.append((form.lower(), analysis))
    return out


def is_form_entry(entry):
    """True for a page that exists only to point at another word's
    inflected form (Wiktionary calls these e.g. "noun form" rather than
    "noun" in the page's head template). "házam" is one of these: its own
    gloss reads "first-person singular single-possession possessive of
    ház" with no 'form-of' tag on the sense to catch it by — the head
    template is the reliable signal, confirmed against both "házak" and
    "házam" while building this importer."""
    for t in entry.get("head_templates") or []:
        if str(t.get("args", {}).get("2", "")).endswith(" form"):
            return True
    return False


def load_frequent_lemmas():
    if not FREQUENCY_FILE.exists():
        print(f"Warning: {FREQUENCY_FILE} not found — run build_hu_frequency.py "
              f"first. Proceeding with no frequency cutoff (word-index.json "
              f"will be much larger than intended).")
        return None
    ranked = json.loads(FREQUENCY_FILE.read_text(encoding="utf-8"))
    return set(ranked[:FREQ_CUTOFF])


def build():
    frequent_lemmas = load_frequent_lemmas()
    dictionary = {}
    dict_is_lowercase_headword = {}
    word_index = {}

    stats = {"lines": 0, "hu_entries": 0, "dict_entries": 0,
              "form_of_only": 0, "no_gloss": 0, "skipped_pos": 0,
              "case_forms": 0}

    with open(RAW_CACHE, encoding="utf-8") as f:
        for line in f:
            stats["lines"] += 1
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("lang_code") != "hu":
                continue
            stats["hu_entries"] += 1

            raw_pos = entry.get("pos")
            word = entry.get("word")
            if not word:
                continue

            if raw_pos in SKIP_POS or raw_pos not in POS_MAP:
                stats["skipped_pos"] += 1
            elif is_form_entry(entry):
                stats["form_of_only"] += 1
            else:
                pos = POS_MAP[raw_pos]
                gloss = primary_gloss(entry.get("senses"))
                if gloss is None:
                    stats["no_gloss"] += 1
                else:
                    key = word.lower()
                    is_lower = word == key
                    # Prefer a lowercase headword over an incidental
                    # capitalised homograph, same tie-break as the Spanish
                    # importer; otherwise first-seen wins.
                    if key not in dictionary or (is_lower and not dict_is_lowercase_headword.get(key)):
                        dictionary[key] = {"en": gloss, "type": pos}
                        dict_is_lowercase_headword[key] = is_lower
                        stats["dict_entries"] += 1

                in_scope = frequent_lemmas is None or word.lower() in frequent_lemmas
                if raw_pos in ("noun", "adj") and in_scope:
                    for form_key, analysis in extract_case_forms(entry, word, pos):
                        bucket = word_index.setdefault(form_key, [])
                        if analysis not in bucket:
                            bucket.append(analysis)
                            stats["case_forms"] += 1

    return dictionary, word_index, stats


def main():
    if RAW_CACHE.exists():
        print(f"Reusing cached {RAW_CACHE} ({RAW_CACHE.stat().st_size:,} bytes)")
    else:
        download()

    dictionary, word_index, stats = build()

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with open(DICT_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, separators=(",", ":"))

    INDEX_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(word_index, f, ensure_ascii=False, separators=(",", ":"))

    dict_size = DICT_OUTPUT.stat().st_size
    dict_gz = len(gzip.compress(DICT_OUTPUT.read_bytes(), compresslevel=9))
    idx_size = INDEX_OUTPUT.stat().st_size
    idx_gz = len(gzip.compress(INDEX_OUTPUT.read_bytes(), compresslevel=9))

    print(f"Lines read:       {stats['lines']:,}")
    print(f"Hungarian entries:{stats['hu_entries']:,}")
    print(f"  skipped (pos):    {stats['skipped_pos']:,}")
    print(f"  skipped (form-of):{stats['form_of_only']:,} (inflected-form pages, not primary lemmas)")
    print(f"  skipped (gloss):  {stats['no_gloss']:,} (form-of only or no usable gloss)")
    print(f"Dictionary:       {len(dictionary):,} lemmas")
    print(f"  Output:           {DICT_OUTPUT} ({dict_size:,} bytes, {dict_gz/1024:.0f} KB gzipped)")
    print(f"Word index:       {len(word_index):,} surface forms ({stats['case_forms']:,} analyses)")
    print(f"  Output:           {INDEX_OUTPUT} ({idx_size:,} bytes, {idx_gz/1024:.0f} KB gzipped)")


if __name__ == "__main__":
    main()
