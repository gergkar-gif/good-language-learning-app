#!/usr/bin/env python3
"""
Import a compact Spanish-English dictionary from doozan/spanish_data.

That project extracts and cleans Spanish-Wiktionary data into a simple
per-headword block format (es-en.data), updated monthly. It replaces an
earlier version of this script that targeted the full Kaikki Wiktionary
dump (~1GB) — far too large to ship to a browser/mobile app. This source
is ~18MB raw and produces a compact one-entry-per-lemma dictionary.

Source: https://github.com/doozan/spanish_data (CC-BY-4.0)

Usage:
    python scripts/import_dictionary.py

Output:
    imports/dictionary/spanish-en.json
    { "<lemma>": { "en": "<translation>", "type": "<pos>", "gender": "m"|"f"|null } }

One entry per lemma with its primary sense — this dictionary is meant to
be looked up by lemma (e.g. after resolving a conjugated verb form via
generated/indexes/verb-index.json), not by every inflected surface form.
"""
import json
import re
import urllib.request
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/doozan/spanish_data/master/es-en.data"

OUTPUT_DIR = Path("imports/dictionary")
OUTPUT_FILE = OUTPUT_DIR / "spanish-en.json"
RAW_CACHE = OUTPUT_DIR / "es-en.data.raw"

# Short POS codes used by the source -> normalized names used in the app
POS_MAP = {
    "n": "noun", "v": "verb", "adj": "adjective", "adv": "adverb",
    "pron": "pronoun", "prep": "preposition", "conj": "conjunction",
    "interj": "interjection", "article": "article", "num": "numeral",
    "determiner": "determiner", "prop": "proper noun",
}
# Categories not useful for word-tap lookup (single tapped words never
# match these — they're multi-word or purely grammatical particles)
# Multi-word entries ("mucho gusto", "hasta luego", "me llamo") are kept on
# purpose: translating them word by word is actively misleading, and the
# reader detects them when a learner taps any word inside one.
SKIP_POS = {
    "suffix", "prefix", "infix", "interfix", "particle",
    "punct", "symbol", "character", "contraction", "name",
}


def download():
    print(f"Downloading {SOURCE_URL} ...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)
    print(f"Downloaded {RAW_CACHE.stat().st_size:,} bytes")


def parse_block(block):
    """Parse one headword block. Returns (word, pos, gender, gloss) using
    the first pos/gloss pair found (the primary sense), or None if the
    block has no usable entry (skip-listed pos, or no gloss at all)."""
    lines = block.split("\n")
    if not lines or not lines[0].strip():
        return None
    word = lines[0].strip()

    pos = gender = gloss = None
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("pos:"):
            if gloss:
                break  # already captured a primary sense from an earlier pos block
            raw_pos = stripped[4:].strip()
            if raw_pos in SKIP_POS:
                pos = None
                continue
            pos = POS_MAP.get(raw_pos, raw_pos)
        elif stripped.startswith("g:") and gender is None and pos:
            gender = stripped[2:].strip() or None
        elif stripped.startswith("gloss:") and gloss is None and pos:
            gloss = stripped[len("gloss:"):].strip()

    if not pos or not gloss:
        return None
    return word, pos, gender, gloss


def build_dictionary():
    text = RAW_CACHE.read_text(encoding="utf-8")
    blocks = text.split("_____\n")

    # Collect every parsed entry first rather than picking "first occurrence
    # wins" while streaming — the source sorts case-sensitively, so a
    # capitalized proper-noun block (e.g. "Bueno", the surname) can appear
    # before the far more useful lowercase common-word block ("bueno", the
    # adjective). Preferring the entry whose headword is already lowercase
    # avoids common words getting shadowed by incidental capitalized
    # homographs.
    candidates = {}
    skipped = 0
    for block in blocks:
        parsed = parse_block(block)
        if not parsed:
            skipped += 1
            continue
        word, pos, gender, gloss = parsed
        key = word.lower()
        is_lowercase_headword = (word == key)
        candidates.setdefault(key, []).append((is_lowercase_headword, word, pos, gender, gloss))

    dictionary = {}
    for key, entries in candidates.items():
        entries.sort(key=lambda e: not e[0])  # lowercase-headword entries first
        _, word, pos, gender, gloss = entries[0]
        entry = {"en": gloss, "type": pos}
        if gender:
            entry["gender"] = gender
        dictionary[key] = entry

    return dictionary, skipped


def main():
    if not RAW_CACHE.exists():
        download()
    else:
        print(f"Reusing cached {RAW_CACHE} ({RAW_CACHE.stat().st_size:,} bytes)")

    dictionary, skipped = build_dictionary()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

    raw_size = OUTPUT_FILE.stat().st_size
    print(f"Entries:   {len(dictionary):,} (skipped {skipped:,} — no usable pos/gloss)")
    print(f"Output:    {OUTPUT_FILE} ({raw_size:,} bytes, {raw_size/1024/1024:.2f} MB)")
    print(f"Cache:     {RAW_CACHE} kept for reuse — delete it to force a fresh download")


if __name__ == "__main__":
    main()
