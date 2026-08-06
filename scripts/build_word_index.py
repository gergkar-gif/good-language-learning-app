#!/usr/bin/env python3
"""
Build a non-verb inflected-form -> lemma index.

The dictionary (imports/dictionary/spanish-en.json) is keyed by lemma, so
a learner tapping "días" or "veces" finds nothing without a way back to
"día" / "vez". This index provides that mapping for nouns, adjectives,
adverbs and other non-verb words.

Verbs are deliberately excluded — scripts/build_verb_index.py already
covers them with much richer output (mood, tense, person, number), built
from the local conjugation data in imports/verbs/.

Real inflection data is used rather than suffix rules on purpose: Spanish
plurals shift written accents in ways simple rules get wrong
(nación->naciones, joven->jóvenes, vez->veces, lápiz->lápices).

Source: https://github.com/doozan/spanish_data (CC-BY-4.0), es_allforms.csv
    Row format: form,pos,lemma[,lemma...]

Usage:
    python scripts/build_word_index.py

Output:
    generated/indexes/word-index.json
    { "<inflected form>": [ { "lemma": "<lemma>", "pos": "<pos>" }, ... ] }
"""
import csv
import gzip
import json
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/doozan/spanish_data/master/es_allforms.csv"

CACHE_DIR = Path("imports/dictionary")
RAW_CACHE = CACHE_DIR / "es_allforms.csv.raw"
OUTPUT_DIR = Path("generated/indexes")
OUTPUT_FILE = OUTPUT_DIR / "word-index.json"

# Verbs are covered by build_verb_index.py with full grammatical analysis.
# The rest are categories a tapped word in a story will never usefully hit
# (affixes, multi-word phrases, punctuation, proper nouns).
SKIP_POS = {
    "v", "prop", "name", "suffix", "prefix", "infix", "interfix",
    "phrase", "proverb", "punct", "symbol", "character",
}

# csv module's default field limit is too small for a few pathological rows
csv.field_size_limit(min(sys.maxsize, 2**31 - 1))


def download():
    print(f"Downloading {SOURCE_URL} ...")
    print("This file is ~72MB; it is cached and gitignored after the first run.")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)
    print(f"Downloaded {RAW_CACHE.stat().st_size:,} bytes")


def build_index():
    index = defaultdict(list)
    stats = {"rows": 0, "identity": 0, "skipped_pos": 0, "skipped_shape": 0}

    with open(RAW_CACHE, encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if len(row) < 3:
                continue
            stats["rows"] += 1
            form, pos, lemmas = row[0], row[1], row[2:]

            if pos in SKIP_POS:
                stats["skipped_pos"] += 1
                continue
            # affixes and multi-word entries can't be produced by tapping a
            # single word in a story
            if form.startswith("-") or form.endswith("-") or " " in form:
                stats["skipped_shape"] += 1
                continue
            # if the form IS its own lemma, the dictionary already resolves
            # it directly — no indirection needed, and skipping these keeps
            # the index roughly a third smaller
            if lemmas == [form]:
                stats["identity"] += 1
                continue

            key = form.lower()
            for lemma in lemmas:
                entry = {"lemma": lemma, "pos": pos}
                if entry not in index[key]:
                    index[key].append(entry)

    return index, stats


def main():
    if RAW_CACHE.exists():
        print(f"Reusing cached {RAW_CACHE} ({RAW_CACHE.stat().st_size:,} bytes)")
    else:
        download()

    index, stats = build_index()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

    raw_size = OUTPUT_FILE.stat().st_size
    gz_size = len(gzip.compress(OUTPUT_FILE.read_bytes(), compresslevel=9))
    ambiguous = sum(1 for v in index.values() if len(v) > 1)

    print(f"Rows read:       {stats['rows']:,}")
    print(f"  skipped (pos):   {stats['skipped_pos']:,} (verbs handled by build_verb_index.py)")
    print(f"  skipped (shape): {stats['skipped_shape']:,} (affixes / multi-word)")
    print(f"  identity forms:  {stats['identity']:,} (dictionary resolves these directly)")
    print(f"Index entries:   {len(index):,} ({ambiguous:,} with more than one reading)")
    print(f"Output:          {OUTPUT_FILE} ({raw_size:,} bytes, {gz_size/1024:.0f} KB gzipped)")


if __name__ == "__main__":
    main()
