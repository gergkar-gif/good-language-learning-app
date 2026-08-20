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
# match these — they're multi-word or purely grammatical particles).
# "letter" is here too: the source gives the name of the alphabet letter
# ("A" -> "letter") its own pos block, which otherwise wins by being first —
# see LETTER_GLOSS_RE below for the other place the same sense hides.
# Multi-word entries ("mucho gusto", "hasta luego", "me llamo") are kept on
# purpose: translating them word by word is actively misleading, and the
# reader detects them when a learner taps any word inside one.
SKIP_POS = {
    "suffix", "prefix", "infix", "interfix", "particle",
    "punct", "symbol", "character", "contraction", "name", "letter",
}

# "de" and "te" — among the most common function words in the language —
# both parse with a pos:n block ("letter: d" / "letter: t", the name of the
# alphabet letter) ahead of their real pos:prep/pos:pron block, because the
# source lists pos blocks in the order Wiktionary happens to store them, not
# by frequency. Any (pos, gloss) matching this is scored worst so a real
# sense from another pos block wins instead. See
# [[dictionary-sense-collision-issue]] in project memory.
LETTER_GLOSS_RE = re.compile(r"^(letter:|letter$|name of the letter\b)", re.IGNORECASE)
RARE_RE = re.compile(r"\brare\b", re.IGNORECASE)

# Confirmed-wrong entries that the scoring below still can't fix: the
# upstream source itself mislabels the common sense as "rare" while leaving
# the actually-obscure one untagged (tranquilar), or simply doesn't carry
# the requested surface form's sense under this headword at all (mía has
# only a military-historical noun sense; the possessive-pronoun sense lives
# under mío and isn't cross-linked). Hand-fixed rather than left broken.
MANUAL_OVERRIDES = {
    "tranquilar": {"en": "to calm down", "type": "verb"},
    "mía": {"en": "mine (feminine)", "type": "pronoun"},
}


def download():
    print(f"Downloading {SOURCE_URL} ...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)
    print(f"Downloaded {RAW_CACHE.stat().st_size:,} bytes")


def parse_block(block):
    """Parse one headword block into every usable (pos, gender, gloss)
    sense it contains — one entry per pos block, taking that block's first
    gloss unless a later gloss in the same block is scored better (see
    below). Returns (word, senses) with senses possibly empty, or None if
    the block itself is unusable (blank/missing headword line).

    Each sense carries a score used to pick the best one across pos blocks
    in build_dictionary(): 0 normal, 1 the picked gloss turned out to be
    tagged rare and a later gloss in the same block wasn't, 2 the "name of
    this letter of the alphabet" sense (see LETTER_GLOSS_RE) — almost never
    what a learner means, but not skip-listed outright because some
    headwords (the letters themselves) have nothing else to offer."""
    lines = block.split("\n")
    if not lines or not lines[0].strip():
        return None
    word = lines[0].strip()

    senses = []
    pos = gender = gloss = score = None

    def flush():
        if pos and gloss:
            senses.append((pos, gender, gloss, score))

    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("pos:"):
            flush()
            pos = gender = gloss = score = None
            raw_pos = stripped[4:].strip()
            if raw_pos in SKIP_POS:
                pos = None
                continue
            pos = POS_MAP.get(raw_pos, raw_pos)
        elif stripped.startswith("g:") and gender is None and pos:
            gender = stripped[2:].strip() or None
        elif stripped.startswith("gloss:") and pos:
            candidate = stripped[len("gloss:"):].strip()
            candidate_score = 2 if LETTER_GLOSS_RE.search(candidate) else 0
            if gloss is None or candidate_score < score:
                gloss = candidate
                score = candidate_score
        elif stripped.startswith("q:") and pos and gloss is not None and score == 0 \
                and RARE_RE.search(stripped):
            score = 1  # demote so a later, untagged gloss in this block can win

    flush()
    return word, senses


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
        if not parsed or not parsed[1]:
            skipped += 1
            continue
        word, senses = parsed
        key = word.lower()
        is_lowercase_headword = (word == key)
        candidates.setdefault(key, []).append((is_lowercase_headword, word, senses))

    dictionary = {}
    for key, entries in candidates.items():
        entries.sort(key=lambda e: not e[0])  # lowercase-headword entries first
        _, word, senses = entries[0]
        # Lowest score wins; min() is stable so among equal scores the
        # earliest pos block in the source still wins, same as before.
        pos, gender, gloss, _ = min(senses, key=lambda s: s[3])
        entry = {"en": gloss, "type": pos}
        if gender:
            entry["gender"] = gender
        dictionary[key] = entry

    for key, override in MANUAL_OVERRIDES.items():
        dictionary[key] = override

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
