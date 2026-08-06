#!/usr/bin/env python3
"""
Build a lemma frequency ranking for disambiguating word lookups.

Many Spanish surface forms have several valid readings, and without any
notion of which is more common the reader can lead with a rare one:
"veces" resolved to an obscure preposition rather than the plural of
"vez", and "casas" to a surname rather than "houses". Ranking readings by
how common their lemma actually is fixes that class of problem generally.

Source: https://github.com/doozan/spanish_data (CC-BY-4.0), frequency.csv
    Row format: count,spanish,pos,flags,usage

Output: generated/indexes/frequency.json
    ["de", "que", "no", ...]  most common first; position is the rank.
    Stored as a plain array rather than {lemma: rank} because it is a
    third of the size and the runtime builds the map on load anyway.

Usage:
    python scripts/build_frequency.py
"""
import csv
import gzip
import json
import sys
import urllib.request
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/doozan/spanish_data/master/frequency.csv"

CACHE_DIR = Path("imports/dictionary")
RAW_CACHE = CACHE_DIR / "frequency.csv.raw"
OUTPUT_DIR = Path("generated/indexes")
OUTPUT_FILE = OUTPUT_DIR / "frequency.json"

# Ranking only needs to separate common words from rare ones; beyond this
# the tail is noise and everything unranked is treated as equally rare.
MAX_LEMMAS = 20000

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))


def main():
    if RAW_CACHE.exists():
        print(f"Reusing cached {RAW_CACHE} ({RAW_CACHE.stat().st_size:,} bytes)")
    else:
        print(f"Downloading {SOURCE_URL} ...")
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)

    lemmas = []
    seen = set()
    with open(RAW_CACHE, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # count,spanish,pos,flags,usage
        for row in reader:
            if len(row) < 2:
                continue
            lemma = row[1].strip().lower()
            if not lemma or lemma in seen:
                continue
            seen.add(lemma)
            lemmas.append(lemma)
            if len(lemmas) >= MAX_LEMMAS:
                break

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(lemmas, f, ensure_ascii=False, separators=(",", ":"))

    raw_size = OUTPUT_FILE.stat().st_size
    gz_size = len(gzip.compress(OUTPUT_FILE.read_bytes(), compresslevel=9))
    print(f"Lemmas ranked: {len(lemmas):,}")
    print(f"Output:        {OUTPUT_FILE} ({raw_size:,} bytes, {gz_size/1024:.0f} KB gzipped)")


if __name__ == "__main__":
    main()
