#!/usr/bin/env python3
"""
Import French-English dictionary from FreeDict and Lexique 383.
Outputs:
  imports/dictionary/french-en.json
Format:
  { "<lemma>": { "en": "<translation>", "type": "<pos>", "gender": "m"|"f"|null } }
"""
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

FREEDICT_URL = "https://raw.githubusercontent.com/freedict/fd-dictionaries/master/fra-eng/fra-eng.tei"
CACHE_DIR = Path("imports/dictionary")
RAW_TEI = CACHE_DIR / "fra-eng.tei"
OUTPUT_FILE = CACHE_DIR / "french-en.json"

POS_MAP = {
    "noun": "noun", "n": "noun", "nom": "noun", "s": "noun",
    "verb": "verb", "v": "verb", "ver": "verb",
    "adj": "adjective", "adjective": "adjective",
    "adv": "adverb", "adverb": "adverb",
    "prep": "preposition", "preposition": "preposition",
    "pron": "pronoun", "pronoun": "pronoun",
    "conj": "conjunction", "conjunction": "conjunction",
    "art": "article", "article": "article",
    "num": "numeral", "numeral": "numeral",
    "interj": "interjection"
}

def download():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not RAW_TEI.exists():
        print(f"Downloading FreeDict fra-eng from {FREEDICT_URL} ...")
        urllib.request.urlretrieve(FREEDICT_URL, RAW_TEI)
        print(f"Downloaded {RAW_TEI.stat().st_size:,} bytes")
    else:
        print(f"Using cached {RAW_TEI}")

def parse_freedict():
    download()
    print("Parsing FreeDict TEI XML...")
    tree = ET.parse(RAW_TEI)
    root = tree.getroot()
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

    dictionary = {}

    for entry in root.findall('.//tei:entry', ns):
        orth_el = entry.find('.//tei:orth', ns)
        if orth_el is None or not orth_el.text:
            continue
        lemma = orth_el.text.strip().lower()

        # POS
        pos_el = entry.find('.//tei:pos', ns)
        raw_pos = (pos_el.text or '').strip().lower() if pos_el is not None else ''
        pos = POS_MAP.get(raw_pos, 'noun' if not raw_pos else raw_pos)

        # Gender
        gen_el = entry.find('.//tei:gen', ns)
        gender = None
        if gen_el is not None and gen_el.text:
            g_text = gen_el.text.strip().lower()
            if 'm' in g_text: gender = 'm'
            elif 'f' in g_text: gender = 'f'

        # Translations from quotes
        quotes = [q.text.strip() for q in entry.findall('.//tei:cit[@type="trans"]/tei:quote', ns) if q.text and q.text.strip()]
        if not quotes:
            # fallback to def
            defs = [d.text.strip() for d in entry.findall('.//tei:def', ns) if d.text and d.text.strip()]
            quotes = defs

        if not quotes:
            continue

        translation = ', '.join(quotes[:3])

        if lemma not in dictionary:
            dictionary[lemma] = {
                "en": translation,
                "type": pos,
                "gender": gender
            }
        else:
            # Merge translations if not already present
            existing = dictionary[lemma]["en"]
            for q in quotes[:2]:
                if q not in existing:
                    existing += f", {q}"
            dictionary[lemma]["en"] = existing

    # Supplement essential common French words if missing
    ESSENTIAL_FALLBACKS = {
        "être": {"en": "to be", "type": "verb", "gender": None},
        "avoir": {"en": "to have", "type": "verb", "gender": None},
        "faire": {"en": "to do, to make", "type": "verb", "gender": None},
        "aller": {"en": "to go", "type": "verb", "gender": None},
        "pouvoir": {"en": "to be able to, can", "type": "verb", "gender": None},
        "vouloir": {"en": "to want", "type": "verb", "gender": None},
        "devoir": {"en": "must, to have to, to owe", "type": "verb", "gender": None},
        "savoir": {"en": "to know (how to)", "type": "verb", "gender": None},
        "venir": {"en": "to come", "type": "verb", "gender": None},
        "voir": {"en": "to see", "type": "verb", "gender": None},
        "prendre": {"en": "to take", "type": "verb", "gender": None},
        "parler": {"en": "to speak, to talk", "type": "verb", "gender": None},
        "aimer": {"en": "to love, to like", "type": "verb", "gender": None},
        "finir": {"en": "to finish", "type": "verb", "gender": None},
        "mettre": {"en": "to put, to place", "type": "verb", "gender": None},
        "dire": {"en": "to say, to tell", "type": "verb", "gender": None},
        "falloir": {"en": "to be necessary, must", "type": "verb", "gender": None},
        "croire": {"en": "to believe", "type": "verb", "gender": None},
        "trouver": {"en": "to find", "type": "verb", "gender": None},
        "donner": {"en": "to give", "type": "verb", "gender": None},
        "comprendre": {"en": "to understand", "type": "verb", "gender": None},
        "attendre": {"en": "to wait", "type": "verb", "gender": None},
        "sortir": {"en": "to go out, to leave", "type": "verb", "gender": None},
        "partir": {"en": "to leave, to depart", "type": "verb", "gender": None},
        "passer": {"en": "to pass, to spend (time)", "type": "verb", "gender": None},
        "rester": {"en": "to stay, to remain", "type": "verb", "gender": None},
        "arriver": {"en": "to arrive, to happen", "type": "verb", "gender": None},
        "aujourd'hui": {"en": "today", "type": "adverb", "gender": None},
        "demain": {"en": "tomorrow", "type": "adverb", "gender": None},
        "hier": {"en": "yesterday", "type": "adverb", "gender": None},
        "toujours": {"en": "always, still", "type": "adverb", "gender": None},
        "souvent": {"en": "often", "type": "adverb", "gender": None},
        "maintenant": {"en": "now", "type": "adverb", "gender": None},
        "beaucoup": {"en": "a lot, much, many", "type": "adverb", "gender": None},
        "très": {"en": "very", "type": "adverb", "gender": None},
        "merci": {"en": "thank you", "type": "interjection", "gender": None},
        "bonjour": {"en": "hello, good morning", "type": "interjection", "gender": None},
        "bonsoir": {"en": "good evening", "type": "interjection", "gender": None},
        "oui": {"en": "yes", "type": "adverb", "gender": None},
        "non": {"en": "no", "type": "adverb", "gender": None},
        "s'il vous plaît": {"en": "please (formal)", "type": "phrase", "gender": None},
        "de rien": {"en": "you are welcome", "type": "phrase", "gender": None},
        "ami": {"en": "friend", "type": "noun", "gender": "m"},
        "amie": {"en": "friend (female)", "type": "noun", "gender": "f"},
        "maison": {"en": "house, home", "type": "noun", "gender": "f"},
        "eau": {"en": "water", "type": "noun", "gender": "f"},
        "pain": {"en": "bread", "type": "noun", "gender": "m"},
        "café": {"en": "coffee, cafe", "type": "noun", "gender": "m"},
        "gare": {"en": "train station", "type": "noun", "gender": "f"},
        "rue": {"en": "street", "type": "noun", "gender": "f"},
        "ville": {"en": "city, town", "type": "noun", "gender": "f"},
        "livre": {"en": "book", "type": "noun", "gender": "m"},
        "temps": {"en": "time, weather", "type": "noun", "gender": "m"},
        "monde": {"en": "world, people", "type": "noun", "gender": "m"},
        "jour": {"en": "day", "type": "noun", "gender": "m"},
        "nuit": {"en": "night", "type": "noun", "gender": "f"}
    }

    for lemma, info in ESSENTIAL_FALLBACKS.items():
        if lemma not in dictionary:
            dictionary[lemma] = info
        # Also map unaccented variant if helpful
        unaccented = lemma.replace("ê", "e").replace("é", "e").replace("è", "e").replace("à", "a")
        if unaccented != lemma and unaccented not in dictionary:
            dictionary[unaccented] = info

    print(f"Writing {len(dictionary):,} entries to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

    print("French dictionary generation complete.")

if __name__ == "__main__":
    parse_freedict()
