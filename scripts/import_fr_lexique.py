#!/usr/bin/env python3
"""
Import French Lexique 383 dataset from OpenLexicon / CNRS.
Source: http://www.lexique.org / https://github.com/chrplr/openlexicon (CC BY-SA 4.0)

Generates:
  content/fr/indexes/word-index.json
  content/fr/indexes/frequency.json
"""
import csv
import gzip
import json
import urllib.request
from collections import defaultdict
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/chrplr/openlexicon/master/datasets-info/Lexique383/Lexique383.tsv"
CACHE_DIR = Path("imports/dictionary")
RAW_CACHE = CACHE_DIR / "Lexique383.tsv"

OUTPUT_WORD_INDEX = Path("content/fr/indexes/word-index.json")
OUTPUT_FREQUENCY = Path("content/fr/indexes/frequency.json")

# Map Lexique cgram to Parlour pos names
CGRAM_MAP = {
    'NOM': 'noun',
    'VER': 'verb',
    'ADJ': 'adjective',
    'ADV': 'adverb',
    'PRE': 'preposition',
    'ART': 'article',
    'PRO': 'pronoun',
    'CON': 'conjunction',
    'ONO': 'interjection',
    'AUX': 'verb'
}

def download():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not RAW_CACHE.exists():
        print(f"Downloading Lexique 383 from {SOURCE_URL} ...")
        try:
            urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)
            print(f"Downloaded {RAW_CACHE.stat().st_size:,} bytes")
        except Exception as e:
            print(f"Could not download directly ({e}). Checking alternative mirror...")
            alt_url = "http://www.lexique.org/databases/Lexique383/Lexique383.tsv"
            urllib.request.urlretrieve(alt_url, RAW_CACHE)
            print(f"Downloaded {RAW_CACHE.stat().st_size:,} bytes")
    else:
        print(f"Using cached {RAW_CACHE}")

def process():
    download()
    OUTPUT_WORD_INDEX.parent.mkdir(parents=True, exist_ok=True)

    print("Processing Lexique 383...")
    word_index = defaultdict(list)
    lemma_freq = defaultdict(float)

    with open(RAW_CACHE, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            ortho = (row.get("ortho") or "").strip().lower()
            lemme = (row.get("lemme") or "").strip().lower()
            cgram = (row.get("cgram") or "").strip()
            genre = (row.get("genre") or "").strip() # m, f
            nombre = (row.get("nombre") or "").strip() # s, p
            freq_films = float(row.get("freqfilms2") or row.get("freqfilms") or 0.0)
            freq_livres = float(row.get("freqlivres") or 0.0)

            total_freq = freq_films + freq_livres
            if lemme:
                lemma_freq[lemme] = max(lemma_freq[lemme], total_freq)

            pos = CGRAM_MAP.get(cgram, cgram.lower())
            # Only record inflections that differ from lemma or non-verb inflections
            if ortho and lemme and ortho != lemme:
                entry = {"lemma": lemme, "pos": pos}
                if genre:
                    entry["gender"] = "masculine" if genre == "m" else "feminine"
                if nombre:
                    entry["number"] = "singular" if nombre == "s" else "plural"
                
                # Deduplicate entries
                if entry not in word_index[ortho]:
                    word_index[ortho].append(entry)

    # Sort frequency by descending freq, skipping elided fragments and single-letter alphabet noise
    fr_skip = {"c", "d", "j", "l", "m", "n", "qu", "s", "t", "b", "f", "g", "h", "k", "p", "q", "r", "v", "w", "x", "z"}
    sorted_lemmas = [
        lemma for lemma, _ in sorted(lemma_freq.items(), key=lambda x: -x[1])
        if lemma and "'" not in lemma and "’" not in lemma and lemma not in fr_skip
    ]

    print(f"Writing {len(word_index):,} word-index surface forms to {OUTPUT_WORD_INDEX}...")
    with open(OUTPUT_WORD_INDEX, "w", encoding="utf-8") as f:
        json.dump(word_index, f, ensure_ascii=False, indent=2)

    print(f"Writing {len(sorted_lemmas):,} frequency-ranked lemmas to {OUTPUT_FREQUENCY}...")
    with open(OUTPUT_FREQUENCY, "w", encoding="utf-8") as f:
        json.dump(sorted_lemmas[:15000], f, ensure_ascii=False, indent=2)

    print("Lexique 383 processing complete.")

if __name__ == "__main__":
    process()
