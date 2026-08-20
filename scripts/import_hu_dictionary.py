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

  imports/dictionary/hungarian-en.json  lemma -> [ { en, pos }, ... ]
      Every real (non-form-of) POS sense for that spelling, not just one —
      "él" is genuinely both a noun ("edge") and a verb ("to live"), "nő"
      both a noun ("woman") and a verb ("to grow"). An earlier version of
      this script picked a single "primary" sense per spelling and threw
      the rest away, which is fine for genuinely unrelated capitalisation
      collisions but actively wrong for real cross-POS homographs: a verb
      reading would get labelled with noun-only grammar ("nőtt" = "nő" +
      accusative, instead of "nő" the verb, past tense) because the sense
      that could have explained it had already been discarded at import
      time. Multiple senses under the SAME POS are still collapsed to one
      (see primary_gloss) — that's a genuine "pick the best definition"
      call, not a lost distinction the reader needs. "Real" excludes
      Wiktionary pages that exist only to point at an inflected form of
      another word (see FORM_OF_TAG below) — those carry no independent
      gloss worth surfacing as a translation.

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
import re
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
# "accusative plural of ház" instead of an actual translation — EXCEPT
# for FORM_OF_EXCEPTION_TAGS below, which use the same "form-of" tag for
# something categorically different: a DERIVED word with its own
# independent meaning, not an inflected form of the same word. "alvás"
# ("sleep") is tagged form-of + noun-from-verb pointing at "alszik" ("to
# sleep") — a learner reading "Jó az alvás" needs "alvás" defined as its
# own noun, not silently dropped the way "házak" (mechanically, "ház" +
# plural, exactly what engine/morphology/hungarian.js already resolves at
# runtime) correctly is. Confirmed via a coverage comparison against
# github.com/tdulcet/compact-dictionaries' independently-built Hungarian
# dictionary (2026-08-19): ~200 common words its build kept that this
# script was dropping were overwhelmingly this exact pattern.
FORM_OF_TAG = "form-of"
FORM_OF_EXCEPTION_TAGS = {"noun-from-verb"}

# Hand-corrected glosses for specific (lemma, pos) senses whose Wiktionary
# entry is accurate but unusually verbose/clinical for a learner-facing
# dictionary — same idea as build-manifest.py's FREQUENCY_GLOSS for Spanish.
# "marha"'s real primary sense is "head of cattle, animal of the species Bos
# taurus": correct, but nobody says it like that. "jó"'s adjective sense
# spells out which case suffix each nuance takes ("good for something
# -ra/-re, good at something -ban/-ben, ...") — real grammar info, but too
# much for a reader tap-popup meant for a quick glance, not a usage note.
#
# This is deliberately NOT a general regex (checked: most animal headwords
# — kutya "dog", macska "cat", ló "horse", róka "fox" — already have plain
# glosses; this phrasing isn't a systematic Wiktionary pattern, just these
# specific entries), so fix them by name rather than writing pattern-
# matching logic for a handful of one-offs.
#
# Matched by a distinctive PREFIX of the original gloss, not the full text
# or an exact (lemma, pos) pair — a word can have more than one sense under
# the same POS ("jó" has two distinct adjective senses: "good" and "quite
# (some), fair (amount of)"), so keying on (lemma, pos) alone would
# overwrite every sense sharing that POS with the same replacement text
# instead of just the one being fixed. Each (lemma, pos, prefix) is checked
# against the ORIGINAL gloss before any override is applied.
GLOSS_OVERRIDES = [
    ("marha", "noun", "head of cattle", "cattle, ox"),
    ("jó", "adjective", "good (good for something", "good"),
    ("ház", "noun", "house, building (closed structure", "house, building"),
    ("ház", "noun", "home (the place of one", "home"),
    ("köszönöm", "interjection", "thank you (an expression of gratitude", "thank you"),
    ("köszönöm", "interjection", "keep the change (if said with some emphasis",
     "keep the change (said when overpaying)"),
]


def apply_gloss_override(lemma, pos, gloss):
    for l, p, prefix, replacement in GLOSS_OVERRIDES:
        if lemma == l and pos == p and gloss.startswith(prefix):
            return replacement
    return gloss

# Senses tagged like this are deprioritised but not dropped outright — a
# rare/dated sense is still better than no dictionary entry. Also used
# ACROSS competing POS entries for the same lemma (see build()'s
# dict_deprioritised tracking) — "igen" has three separate Wiktionary
# entries (adv "quite/very/rather", tagged literary; intj "yes"; noun
# "yes"), and without this, first-in-file-order picked the literary
# adverb sense over the everyday "yes" a learner actually needs.
DEPRIORITISE_TAGS = {"obsolete", "archaic", "dated", "rare", "literary"}

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


# "verbal noun of alszik: sleep" -> "sleep" — see FORM_OF_EXCEPTION_TAGS.
VERBAL_NOUN_PREFIX = re.compile(r"^verbal noun of [^:]+:\s*", re.I)


# How many distinct senses a single (lemma, pos) keeps at most — see
# all_glosses()'s own docstring on why more than one at all. 2 wasn't
# enough: "kormány" has three real senses under noun — "steering wheel",
# "helm", "government" — in exactly that Wiktionary order, so a cap of 2
# silently dropped "government", the one a learner most needs.
MAX_SENSES_PER_POS = 3


# A noun sense whose gloss is just its own capitalised headword plus a
# parenthetical ("Kér (one of the seven Hungarian tribes...)") is Wiktionary
# mistagging a proper noun (tribe/place/personal name) as a common noun —
# SKIP_POS's "name" filter exists for exactly this but only catches it when
# the page's OWN pos field says so, and this one says "noun". Found via
# "kérem" (the common verb form "I ask for it") wrongly explaining its "-em"
# as a possessive ("my Kér") once MAX_SENSES_PER_POS made this 3rd, obscure
# sense of "kér" reachable at all.
MISTAGGED_PROPER_NOUN = re.compile(r"^([A-ZÁÉÍÓÖŐÚÜŰ]\w*)\s*\(")


def all_glosses(senses, word=None):
    """Up to MAX_SENSES_PER_POS (gloss, is_deprioritised) pairs, most
    useful first — not just the single best one. "kormány" has three
    senses under the same noun POS: "steering wheel", "helm", "government"
    — genuinely different concepts sharing a word, not nuances of one
    meaning (unlike "ház"'s many senses, which are all recognisably "a
    house" in some extended way). Collapsing to one sense per POS, this
    script's original design, is right for a real nuance list but wrong
    here: "government" was silently unreachable because "steering wheel"
    happened to be listed first on the Wiktionary page. is_deprioritised
    is also used by build() to choose between an entry's BEST sense and a
    competing entry for the same lemma under a different POS (see
    DEPRIORITISE_TAGS's docstring on "igen") — only the first pair's
    flag matters for that, since it's always the non-deprioritised one
    when any exist."""
    candidates = []
    for sense in senses or []:
        tags = set(sense.get("tags") or [])
        glosses = sense.get("glosses") or []
        if not glosses:
            continue
        gloss = glosses[0]
        if FORM_OF_TAG in tags:
            if not (tags & FORM_OF_EXCEPTION_TAGS):
                continue
            stripped = VERBAL_NOUN_PREFIX.sub("", gloss)
            if stripped == gloss or not stripped:
                continue  # exception tag present but no clean translation to extract
            gloss = stripped
        m = MISTAGGED_PROPER_NOUN.match(gloss)
        if m and word and m.group(1).lower() == word.lower():
            continue
        candidates.append((bool(tags & DEPRIORITISE_TAGS), gloss))
    if not candidates:
        return []
    candidates.sort(key=lambda c: c[0])  # non-deprioritised first

    kept = []
    seen_text = set()
    for deprioritised, gloss in candidates:
        if gloss in seen_text:
            continue
        seen_text.add(gloss)
        kept.append((gloss, deprioritised))
        if len(kept) >= MAX_SENSES_PER_POS:
            break
    return kept


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
    # key -> {pos -> {"en", "type", "_deprioritised", "_is_lower"}} while
    # building, so a same-POS collision (capitalised homograph, duplicate
    # page) still ties-breaks the way it always did; flattened to
    # key -> [sense, ...] (dropping the private "_" fields) at the end,
    # which is the actual output shape — see the module docstring.
    senses_by_key = {}
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
                glosses = all_glosses(entry.get("senses"), word)
                if not glosses:
                    stats["no_gloss"] += 1
                else:
                    key = word.lower()
                    is_lower = word == key
                    by_pos = senses_by_key.setdefault(key, {})
                    # gloss text -> sense dict, so a second distinct sense
                    # for the same (lemma, pos) — "kormány" = "government"
                    # alongside "steering wheel" — accumulates instead of
                    # overwriting; MAX_SENSES_PER_POS is enforced later, at
                    # flatten time, once every page has contributed.
                    pos_senses = by_pos.setdefault(pos, {})
                    for gloss, deprioritised in glosses:
                        existing = pos_senses.get(gloss)
                        # Tie-break for the SAME gloss text under the SAME
                        # (lemma, pos) — a capitalised homograph or duplicate
                        # page restating the identical sense. A non-
                        # deprioritised sense always beats a deprioritised
                        # one; only when that's tied does the lowercase-
                        # headword preference apply; otherwise first-seen
                        # wins. A DIFFERENT pos for the same spelling is
                        # never a competitor — see the module docstring on
                        # why both are kept.
                        if existing is None:
                            replace = True
                        elif deprioritised != existing["_deprioritised"]:
                            replace = existing["_deprioritised"] and not deprioritised
                        else:
                            replace = is_lower and not existing["_is_lower"]
                        if replace:
                            if existing is None:
                                stats["dict_entries"] += 1
                            pos_senses[gloss] = {
                                "en": gloss, "type": pos,
                                "_deprioritised": deprioritised, "_is_lower": is_lower,
                            }

                in_scope = frequent_lemmas is None or word.lower() in frequent_lemmas
                if raw_pos in ("noun", "adj") and in_scope:
                    for form_key, analysis in extract_case_forms(entry, word, pos):
                        bucket = word_index.setdefault(form_key, [])
                        if analysis not in bucket:
                            bucket.append(analysis)
                            stats["case_forms"] += 1

    # Flatten to the actual output shape: lemma -> [sense, ...], dropping
    # the private tie-break bookkeeping fields. Non-deprioritised senses
    # sort first — the sense a bare-lemma lookup (no suffix at all) shows
    # as primary should be the everyday one, not e.g. an archaic noun use
    # sitting ahead of the common verb sense purely by file order. Python's
    # sort is stable, so ties keep encounter order beyond that. Each POS
    # contributes at most MAX_SENSES_PER_POS of its own accumulated senses.
    dictionary = {}
    for key, by_pos in senses_by_key.items():
        all_senses = []
        for pos_senses in by_pos.values():
            ordered = sorted(pos_senses.values(), key=lambda s: s["_deprioritised"])
            all_senses.extend(ordered[:MAX_SENSES_PER_POS])
        all_senses.sort(key=lambda s: s["_deprioritised"])
        dictionary[key] = [
            {"en": apply_gloss_override(key, s["type"], s["en"]), "type": s["type"]}
            for s in all_senses
        ]

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
    homographs = sum(1 for senses in dictionary.values() if len(senses) > 1)
    print(f"Dictionary:       {len(dictionary):,} lemmas, {stats['dict_entries']:,} senses "
          f"({homographs:,} spellings with >1 POS sense, e.g. noun+verb homographs)")
    print(f"  Output:           {DICT_OUTPUT} ({dict_size:,} bytes, {dict_gz/1024:.0f} KB gzipped)")
    print(f"Word index:       {len(word_index):,} surface forms ({stats['case_forms']:,} analyses)")
    print(f"  Output:           {INDEX_OUTPUT} ({idx_size:,} bytes, {idx_gz/1024:.0f} KB gzipped)")


if __name__ == "__main__":
    main()
