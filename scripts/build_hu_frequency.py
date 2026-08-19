#!/usr/bin/env python3
"""
Build a lemma frequency ranking for disambiguating Hungarian word lookups.

Mirrors scripts/build_frequency.py's role for Spanish: Lexicon.lookup() uses
this to rank ambiguous readings by how common the underlying lemma actually
is, rather than showing whichever reading happens to come first.

Source: https://github.com/petyaracz/hungarian-word-frequencies (Rácz 2025,
Hungarian Webcorpus 2, spellchecked lemmata only), distributed as a SQLite
database on Hugging Face. Row-per-surface-form with a repeated lemma_freq
column, so this pulls the distinct top lemmas by that column.

Output: content/hu/indexes/frequency.json
    ["a", "és", "hogy", ...]  most common first; position is the rank.

Usage:
    python scripts/build_hu_frequency.py
"""
import gzip
import json
import sqlite3
import urllib.request
from pathlib import Path

SOURCE_URL = "https://huggingface.co/datasets/petyaracz/hungarian-word-frequencies/resolve/main/frequencies.db"

CACHE_DIR = Path("imports/dictionary")
RAW_CACHE = CACHE_DIR / "hu-frequencies.db.raw"
OUTPUT_DIR = Path("content/hu/indexes")
OUTPUT_FILE = OUTPUT_DIR / "frequency.json"

# Matches build_frequency.py's cutoff — separates common words from rare
# ones; the tail beyond this is noise and treated as equally rare.
MAX_LEMMAS = 20000


def main():
    if RAW_CACHE.exists():
        print(f"Reusing cached {RAW_CACHE} ({RAW_CACHE.stat().st_size:,} bytes)")
    else:
        print(f"Downloading {SOURCE_URL} ...")
        print("This file is ~585MB; it is cached and gitignored after the first run.")
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)

    con = sqlite3.connect(str(RAW_CACHE))
    cur = con.cursor()
    cur.execute(
        "SELECT lemma FROM words GROUP BY lemma "
        "ORDER BY MAX(lemma_freq) DESC LIMIT ?",
        (MAX_LEMMAS,),
    )
    lemmas = [row[0] for row in cur.fetchall() if row[0]]
    con.close()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(lemmas, f, ensure_ascii=False, separators=(",", ":"))

    raw_size = OUTPUT_FILE.stat().st_size
    gz_size = len(gzip.compress(OUTPUT_FILE.read_bytes(), compresslevel=9))
    print(f"Lemmas ranked: {len(lemmas):,}")
    print(f"Output:        {OUTPUT_FILE} ({raw_size:,} bytes, {gz_size/1024:.0f} KB gzipped)")


if __name__ == "__main__":
    main()
