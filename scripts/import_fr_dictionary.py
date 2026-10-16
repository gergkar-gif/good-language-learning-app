#!/usr/bin/env python3
"""
Import comprehensive French-English dictionary from Wiktionary (Vuizur export)
and FreeDict, supplemented with additions-fr.json.

Outputs:
  imports/dictionary/french-en.json
Format:
  { "<lemma>": { "en": "<translation>", "type": "<pos>", "gender": "m"|"f"|null } }
"""
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

WIKTIONARY_TSV_URL = "https://raw.githubusercontent.com/Vuizur/Wiktionary-Dictionaries/master/French-English%20Wiktionary%20dictionary.tsv"
FREEDICT_URL = "https://raw.githubusercontent.com/freedict/fd-dictionaries/master/fra-eng/fra-eng.tei"

CACHE_DIR = Path("imports/dictionary")
RAW_TSV = CACHE_DIR / "French-English Wiktionary dictionary.tsv"
RAW_TEI = CACHE_DIR / "fra-eng.tei"
OUTPUT_FILE = CACHE_DIR / "french-en.json"
ADDITIONS_FILE = CACHE_DIR / "additions-fr.json"
WORD_INDEX_FILE = Path("content/fr/indexes/word-index.json")

POS_MAP = {
    "noun": "noun", "n": "noun", "nom": "noun", "s": "noun",
    "verb": "verb", "v": "verb", "ver": "verb",
    "adj": "adjective", "adjective": "adjective",
    "adv": "adverb", "adverb": "adverb",
    "prep": "preposition", "preposition": "preposition",
    "pron": "pronoun", "pronoun": "pronoun",
    "conj": "conjunction", "conjunction": "conjunction",
    "det": "determiner", "determiner": "determiner",
    "art": "article", "article": "article",
    "num": "numeral", "numeral": "numeral",
    "interj": "interjection",
    "name": "proper noun", "prop": "proper noun"
}

def download():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not RAW_TSV.exists():
        print(f"Downloading French Wiktionary TSV from {WIKTIONARY_TSV_URL} ...")
        req = urllib.request.Request(WIKTIONARY_TSV_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            RAW_TSV.write_bytes(resp.read())
        print(f"Downloaded {RAW_TSV.stat().st_size:,} bytes")
    else:
        print(f"Using cached {RAW_TSV}")

    if not RAW_TEI.exists():
        print(f"Downloading FreeDict fra-eng from {FREEDICT_URL} ...")
        urllib.request.urlretrieve(FREEDICT_URL, RAW_TEI)
        print(f"Downloaded {RAW_TEI.stat().st_size:,} bytes")
    else:
        print(f"Using cached {RAW_TEI}")

def clean_gloss(raw):
    text = re.sub(r'<[^>]+>', '', raw)
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_wiktionary():
    download()
    print("Parsing French Wiktionary TSV...")
    dictionary = {}
    extra_surface_forms = {}

    with open(RAW_TSV, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t", 1)
            if len(parts) != 2:
                continue
            raw_keys, raw_html = parts
            keys = [k.strip().lower() for k in raw_keys.split("|") if k.strip()]
            if not keys:
                continue

            # Parse POS and definitions
            blocks = re.findall(r'<i>(.*?)</i><br><ol>(.*?)</ol>', raw_html)
            if not blocks:
                defs = [clean_gloss(d) for d in re.findall(r'<li>(.*?)</li>', raw_html)]
                pos_m = re.search(r'<i>(.*?)</i>', raw_html)
                pos = POS_MAP.get(pos_m.group(1).lower(), 'noun') if pos_m else 'noun'
                if defs:
                    blocks = [(pos, ''.join(f'<li>{d}</li>' for d in defs))]

            if not blocks:
                continue

            best_pos = 'noun'
            best_defs = []
            gender = None
            for raw_pos, ol_content in blocks:
                p_lower = raw_pos.strip().lower()
                p = POS_MAP.get(p_lower, '')
                if not p:
                    continue
                if 'masculine' in p_lower:
                    gender = 'm'
                elif 'feminine' in p_lower:
                    gender = 'f'
                defs = [clean_gloss(d) for d in re.findall(r'<li>(.*?)</li>', ol_content)]
                defs = [d for d in defs if d and not d.startswith('alternative form of') and not d.startswith('synonym of')][:3]
                if defs:
                    best_pos = p
                    best_defs = defs
                    break

            if not best_defs:
                continue

            trans = '; '.join(best_defs)
            primary_lemma = keys[0]

            if primary_lemma not in dictionary:
                dictionary[primary_lemma] = {
                    "en": trans,
                    "type": best_pos,
                    "gender": gender
                }

            # Function words (pronouns, determiners, articles, prepositions, conjunctions)
            # get their inflected forms directly indexed in dictionary for instant resolution
            if best_pos in ('pronoun', 'determiner', 'article', 'preposition', 'conjunction'):
                for k in keys[1:]:
                    if len(k) >= 2 and k not in dictionary:
                        dictionary[k] = {
                            "en": trans,
                            "type": best_pos,
                            "gender": gender
                        }

            # Record surface forms for word-index fallback
            for k in keys[1:]:
                if len(k) >= 2 and ' ' not in k and k != primary_lemma:
                    if k not in extra_surface_forms:
                        extra_surface_forms[k] = primary_lemma

    print(f"Extracted {len(dictionary):,} entries from Wiktionary")
    return dictionary, extra_surface_forms

def supplement_freedict(dictionary):
    print("Supplementing from FreeDict...")
    tree = ET.parse(RAW_TEI)
    root = tree.getroot()
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    added = 0

    for entry in root.findall('.//tei:entry', ns):
        orth_el = entry.find('.//tei:orth', ns)
        if orth_el is None or not orth_el.text:
            continue
        lemma = orth_el.text.strip().lower()
        if lemma in dictionary:
            continue

        pos_el = entry.find('.//tei:pos', ns)
        raw_pos = (pos_el.text or '').strip().lower() if pos_el is not None else ''
        pos = POS_MAP.get(raw_pos, 'noun' if not raw_pos else raw_pos)

        gen_el = entry.find('.//tei:gen', ns)
        gender = None
        if gen_el is not None and gen_el.text:
            g_text = gen_el.text.strip().lower()
            if 'm' in g_text: gender = 'm'
            elif 'f' in g_text: gender = 'f'

        quotes = [q.text.strip() for q in entry.findall('.//tei:cit[@type="trans"]/tei:quote', ns) if q.text and q.text.strip()]
        if not quotes:
            defs = [d.text.strip() for d in entry.findall('.//tei:def', ns) if d.text and d.text.strip()]
            quotes = defs
        if not quotes:
            continue

        dictionary[lemma] = {
            "en": ', '.join(quotes[:3]),
            "type": pos,
            "gender": gender
        }
        added += 1

    print(f"Added {added:,} new entries from FreeDict")

def supplement_additions(dictionary):
    if not ADDITIONS_FILE.exists():
        return
    print(f"Applying additions from {ADDITIONS_FILE}...")
    try:
        with open(ADDITIONS_FILE, "r", encoding="utf-8") as f:
            additions = json.load(f)
        count = 0
        for word, senses in additions.items():
            if isinstance(senses, list) and senses:
                primary = senses[0]
                dictionary[word.lower()] = {
                    "en": primary.get("en", ""),
                    "type": primary.get("type", "noun"),
                    "gender": primary.get("gender")
                }
                count += 1
            elif isinstance(senses, dict):
                dictionary[word.lower()] = senses
                count += 1
        print(f"Merged {count} entries from additions-fr.json")
    except Exception as e:
        print(f"Warning: could not read additions: {e}")

def update_word_index(extra_surface_forms):
    if not WORD_INDEX_FILE.exists():
        return
    print(f"Enriching {WORD_INDEX_FILE} with surface forms...")
    try:
        with open(WORD_INDEX_FILE, "r", encoding="utf-8") as f:
            word_index = json.load(f)
        before = len(word_index)
        for form, lemma in extra_surface_forms.items():
            if form not in word_index:
                word_index[form] = [{"lemma": lemma, "pos": "noun"}]
        after = len(word_index)
        with open(WORD_INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(word_index, f, ensure_ascii=False, separators=(',', ':'))
        print(f"Enriched word-index from {before:,} to {after:,} surface forms (+{after - before:,})")
    except Exception as e:
        print(f"Warning: could not enrich word index: {e}")

def main():
    dictionary, extra_surface = parse_wiktionary()
    supplement_freedict(dictionary)
    supplement_additions(dictionary)

    # Core French grammar tokens that must be guaranteed
    CORE_WORDS = {
        "au": {"en": "to the, at the", "type": "contraction", "gender": None},
        "aux": {"en": "to the, at the (plural)", "type": "contraction", "gender": None},
        "du": {"en": "of the, from the, some", "type": "contraction", "gender": None},
        "des": {"en": "of the, some (plural)", "type": "contraction", "gender": None},
        "cette": {"en": "this, that", "type": "determiner", "gender": "f"},
        "ces": {"en": "these, those", "type": "determiner", "gender": None},
        "telles": {"en": "such", "type": "adjective", "gender": "f"},
        "tels": {"en": "such", "type": "adjective", "gender": "m"},
        "telle": {"en": "such", "type": "adjective", "gender": "f"},
        "tel": {"en": "such", "type": "adjective", "gender": "m"},
        "cents": {"en": "hundreds", "type": "numeral", "gender": "m"},
        "eux": {"en": "them", "type": "pronoun", "gender": "m"},
        "se": {"en": "himself, herself, themselves, oneself", "type": "pronoun", "gender": None},
        "ne": {"en": "not (negative particle)", "type": "adverb", "gender": None},
        "y": {"en": "there, to it", "type": "pronoun", "gender": None},
        "en": {"en": "in, of it, from there", "type": "pronoun", "gender": None}
    }
    for w, entry in CORE_WORDS.items():
        if w not in dictionary:
            dictionary[w] = entry

    print(f"Saving final dictionary with {len(dictionary):,} entries to {OUTPUT_FILE} ...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, separators=(',', ':'))
    print(f"Saved {OUTPUT_FILE.stat().st_size:,} bytes")

    update_word_index(extra_surface)

if __name__ == "__main__":
    main()
