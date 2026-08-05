#!/usr/bin/env python3
"""
Import Spanish-English dictionary from Kaikki (parsed Wiktionary).

Downloads the latest Spanish dictionary dump from kaikki.org,
processes it into a simplified JSON format, and saves to
imports/dictionary/spanish-en.json.

Usage:
    python scripts/import_dictionary.py

Output:
    imports/dictionary/spanish-en.json
"""

import json
import urllib.request
import os
import sys

# Kaikki Spanish dictionary URL
KAIKKI_URL = "https://kaikki.org/dictionary/Spanish/kaikki.org-dictionary-Spanish.jsonl"

# Output paths
OUTPUT_DIR = "imports/dictionary"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "spanish-en.json")

# Optional: limit to most common words for a smaller file
# Set to 0 to include all words
MAX_WORDS = 0

# Word types we care about (skip phrases, proverbs, etc.)
ALLOWED_POS = {
    "noun", "verb", "adjective", "adverb", "pronoun", "preposition",
    "conjunction", "interjection", "article", "numeral", "proper noun"
}


def download_dictionary():
    """Download the Kaikki Spanish dictionary JSONL file."""
    print(f"Downloading from {KAIKKI_URL}...")
    print("This is a large file (~50-100MB). Please wait.")

    temp_file = os.path.join(OUTPUT_DIR, "kaikki-raw.jsonl")
    urllib.request.urlretrieve(KAIKKI_URL, temp_file)
    print(f"✓ Downloaded to {temp_file}")
    return temp_file


def process_entry(raw_entry):
    """Extract useful fields from a Kaikki entry."""
    word = raw_entry.get("word", "").lower().strip()
    pos = raw_entry.get("pos", "unknown")

    if not word or pos not in ALLOWED_POS:
        return None

    # Get the first/main sense
    senses = raw_entry.get("senses", [])
    if not senses:
        return None

    # Build English definition from glosses
    glosses = []
    for sense in senses[:3]:  # Limit to first 3 senses
        sense_glosses = sense.get("glosses", [])
        if sense_glosses:
            glosses.append(sense_glosses[0])

    if not glosses:
        return None

    english = "; ".join(glosses)

    # Extract examples if available
    examples = []
    for sense in senses[:2]:
        for ex in sense.get("examples", [])[:2]:
            if isinstance(ex, dict):
                examples.append({
                    "es": ex.get("text", ""),
                    "en": ex.get("translation", "")
                })
            elif isinstance(ex, str):
                examples.append({"es": ex, "en": ""})

    # Extract pronunciation
    sounds = raw_entry.get("sounds", [])
    pronunciation = ""
    for sound in sounds:
        if "ipa" in sound:
            pronunciation = sound["ipa"]
            break

    return {
        "en": english,
        "type": pos,
        "pronunciation": pronunciation,
        "examples": examples[:3],
        "source": "kaikki"
    }


def build_dictionary(temp_file):
    """Process the raw JSONL into our simplified format."""
    dictionary = {}
    count = 0
    skipped = 0

    print("Processing entries...")
    with open(temp_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                skipped += 1
                continue

            processed = process_entry(entry)
            if processed:
                word = entry["word"].lower().strip()
                # Skip duplicates (keep first occurrence which is usually most common)
                if word not in dictionary:
                    dictionary[word] = processed
                    count += 1

                    if MAX_WORDS > 0 and count >= MAX_WORDS:
                        print(f"Reached limit of {MAX_WORDS} words.")
                        break
            else:
                skipped += 1

            if count % 5000 == 0 and count > 0:
                print(f"  ...{count} words processed")

    print(f"✓ Processed {count} words ({skipped} skipped)")
    return dictionary


def save_dictionary(dictionary):
    """Save the processed dictionary to JSON."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

    file_size = os.path.getsize(OUTPUT_FILE)
    print(f"✓ Saved {len(dictionary)} entries to {OUTPUT_FILE}")
    print(f"  File size: {file_size:,} bytes ({file_size / 1024 / 1024:.1f} MB)")


def main():
    print("=" * 60)
    print("Spanish Dictionary Import (Kaikki)")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    temp_file = os.path.join(OUTPUT_DIR, "kaikki-raw.jsonl")

    # Check if we already have the raw file
    if os.path.exists(temp_file):
        reuse = input(f"Found existing download: {temp_file}. Reuse? [Y/n]: ").strip().lower()
        if reuse == "n":
            temp_file = download_dictionary()
    else:
        temp_file = download_dictionary()

    dictionary = build_dictionary(temp_file)
    save_dictionary(dictionary)

    # Optional: clean up raw file
    cleanup = input(f"
Delete raw download {temp_file}? [y/N]: ").strip().lower()
    if cleanup == "y":
        os.remove(temp_file)
        print(f"✓ Deleted {temp_file}")

    print("\nDone! The engine will load this dictionary on startup.")


if __name__ == "__main__":
    main()
