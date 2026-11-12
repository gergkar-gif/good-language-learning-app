#!/usr/bin/env python3
"""
Import comprehensive Slovak-English dictionary, morphology indexes, and verb library
from Kaikki.org (Wiktionary extract) and HermitDave OpenSubtitles Frequency list.

Attribution & Licensing:
- Kaikki.org / Wiktionary: CC BY-SA 3.0 & GFDL (Tatu Ylonen / Wiktionary contributors)
- HermitDave FrequencyWords: CC BY-SA 3.0 (HermitDave / OpenSubtitles)
- FreeDict (slk-eng): GNU GPL v3+ (freedict.org)

Outputs:
  imports/dictionary/slovak-en.json
  content/sk/indexes/word-index.json
  content/sk/indexes/verb-index.json
  content/sk/indexes/frequency.json
  imports/verbs/sk/<lemma>.json (Conjugation tables for top verbs)
  imports/verbs/sk/verb-list-sk.js (ALL_SLOVAK_VERBS list)
"""
import gzip
import json
import os
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

KAIKKI_URL = "https://kaikki.org/dictionary/Slovak/kaikki.org-dictionary-Slovak.jsonl.gz"
FREQ_URL = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/sk/sk_50k.txt"
LEMMAS_URL = "https://raw.githubusercontent.com/michmech/lemmatization-lists/master/lemmatization-sk.txt"

CACHE_DIR = Path("imports/dictionary")
KAIKKI_FILE = CACHE_DIR / "kaikki-sk.jsonl.gz"
FREQ_FILE = CACHE_DIR / "frequency-sk.txt"
LEMMAS_FILE = CACHE_DIR / "lemmatization-sk.txt"
ADDITIONS_FILE = CACHE_DIR / "additions-sk.json"

DICT_OUTPUT = CACHE_DIR / "slovak-en.json"
WORD_INDEX_OUTPUT = Path("content/sk/indexes/word-index.json")
VERB_INDEX_OUTPUT = Path("content/sk/indexes/verb-index.json")
FREQUENCY_OUTPUT = Path("content/sk/indexes/frequency.json")
VERBS_DIR = Path("imports/verbs/sk")
VERB_LIST_OUTPUT = VERBS_DIR / "verb-list-sk.js"

POS_MAP = {
    "noun": "noun",
    "verb": "verb",
    "adj": "adjective",
    "adjective": "adjective",
    "adv": "adverb",
    "adverb": "adverb",
    "prep": "preposition",
    "preposition": "preposition",
    "pron": "pronoun",
    "pronoun": "pronoun",
    "conj": "conjunction",
    "conjunction": "conjunction",
    "det": "determiner",
    "determiner": "determiner",
    "num": "numeral",
    "numeral": "numeral",
    "interj": "interjection",
    "proper noun": "proper noun",
    "name": "proper noun",
    "particle": "particle"
}

PRIORITY_VERBS = [
    "byť", "mať", "môcť", "chcieť", "vedieť", "poznať", "povedať", "hovoriť",
    "robiť", "urobiť", "vidieť", "uvidieť", "myslieť", "pomyslieť", "ísť", "prísť",
    "odísť", "ísť", "cestovať", "brať", "vziať", "dávať", "dať", "rozumieť",
    "porozumieť", "čakať", "počkať", "pýtať", "opýtať", "odpovedať", "odpovedať",
    "hľadať", "nájsť", "pracovať", "učiť", "pamätať", "zabudnúť", "musieť",
    "žiť", "ľúbiť", "milovať", "čítať", "prečítať", "písať", "napísať", "piť", "vypiť", "jesť",
    "zjesť", "spať", "kupovať", "kúpiť", "predávať", "predať", "stretnúť", "začínať",
    "začať", "končiť", "skončiť", "otvárať", "otvoriť", "zatvárať", "zatvoriť",
    "počúvať", "počuť", "pozerať", "pozrieť", "pomáhať", "pomôcť", "hrať",
    "bývať", "stáť", "platiť", "zaplatiť", "cítiť", "poďakovať",
    "ospravedlniť", "prosiť", "poprosiť", "vracať", "vrátiť", "zostávať", "zostať",
    "potrebovať", "báť", "tešiť", "sedieť", "sadnúť", "ležať", "behať", "bežať",
    "chodiť", "plávať", "jazdiť", "variť", "ukázať", "ukazovať", "stratiť",
    "strácať", "zavolať", "volať"
]

CANONICAL_VERBS = {
    "byť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "som", "ty": "si", "on": "je", "my": "sme", "vy": "ste", "oni": "sú" },
        "indicativo.minuly": {
            "on": "bol", "ona": "bola", "ono": "bolo",
            "oni_anim": "boli", "ony_inanim": "boli", "ona_neut": "boli"
        },
        "indicativo.budouci": { "ja": "budem", "ty": "budeš", "on": "bude", "my": "budeme", "vy": "budete", "oni": "budú" },
        "podminovaci": { "ja": "bol by som", "ty": "bol by si", "on": "bol by", "my": "boli by sme", "vy": "boli by ste", "oni": "boli by" },
        "rozkazovaci": { "ty": "buď", "my": "buďme", "vy": "buďte" }
    },
    "mať": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "mám", "ty": "máš", "on": "má", "my": "máme", "vy": "máte", "oni": "majú" },
        "indicativo.minuly": {
            "on": "mal", "ona": "mala", "ono": "malo",
            "oni_anim": "mali", "ony_inanim": "mali", "ona_neut": "mali"
        },
        "indicativo.budouci": { "ja": "budem mať", "ty": "budeš mať", "on": "bude mať", "my": "budeme mať", "vy": "budete mať", "oni": "budú mať" },
        "podminovaci": { "ja": "mal by som", "ty": "mal by si", "on": "mal by", "my": "mali by sme", "vy": "mali by ste", "oni": "mali by" },
        "rozkazovaci": { "ty": "maj", "my": "majme", "vy": "majte" }
    },
    "môcť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "môžem", "ty": "môžeš", "on": "môže", "my": "môžeme", "vy": "môžete", "oni": "môžu" },
        "indicativo.minuly": {
            "on": "mohol", "ona": "mohla", "ono": "mohlo",
            "oni_anim": "mohli", "ony_inanim": "mohli", "ona_neut": "mohli"
        },
        "indicativo.budouci": { "ja": "budem môcť", "ty": "budeš môcť", "on": "bude môcť", "my": "budeme môcť", "vy": "budete môcť", "oni": "budú môcť" },
        "podminovaci": { "ja": "mohol by som", "ty": "mohol by si", "on": "mohol by", "my": "mohli by sme", "vy": "mohli by ste", "oni": "mohli by" },
        "rozkazovaci": { "ty": "môž", "my": "môžme", "vy": "môžte" }
    },
    "chcieť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "chcem", "ty": "chceš", "on": "chce", "my": "chceme", "vy": "chcete", "oni": "chcú" },
        "indicativo.minuly": {
            "on": "chcel", "ona": "chcela", "ono": "chcelo",
            "oni_anim": "chceli", "ony_inanim": "chceli", "ona_neut": "chceli"
        },
        "indicativo.budouci": { "ja": "budem chcieť", "ty": "budeš chcieť", "on": "bude chcieť", "my": "budeme chcieť", "vy": "budete chcieť", "oni": "budú chcieť" },
        "podminovaci": { "ja": "chcel by som", "ty": "chcel by si", "on": "chcel by", "my": "chceli by sme", "vy": "chceli by ste", "oni": "chceli by" },
        "rozkazovaci": { "ty": "chci", "my": "chcime", "vy": "chcite" }
    },
    "vedieť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "viem", "ty": "vieš", "on": "vie", "my": "vieme", "vy": "viete", "oni": "vedia" },
        "indicativo.minuly": {
            "on": "vedel", "ona": "vedela", "ono": "vedelo",
            "oni_anim": "vedeli", "ony_inanim": "vedeli", "ona_neut": "vedeli"
        },
        "indicativo.budouci": { "ja": "budem vedieť", "ty": "budeš vedieť", "on": "bude vedieť", "my": "budeme vedieť", "vy": "budete vedieť", "oni": "budú vedieť" },
        "podminovaci": { "ja": "vedel by som", "ty": "vedel by si", "on": "vedel by", "my": "vedeli by sme", "vy": "vedeli by ste", "oni": "vedeli by" },
        "rozkazovaci": { "ty": "vedz", "my": "vedzme", "vy": "vedzte" }
    },
    "ísť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "idem", "ty": "ideš", "on": "ide", "my": "ideme", "vy": "idete", "oni": "idú" },
        "indicativo.minuly": {
            "on": "išiel", "ona": "išla", "ono": "išlo",
            "oni_anim": "išli", "ony_inanim": "išli", "ona_neut": "išli"
        },
        "indicativo.budouci": { "ja": "pôjdem", "ty": "pôjdeš", "on": "pôjde", "my": "pôjdeme", "vy": "pôjdete", "oni": "pôjdu" },
        "podminovaci": { "ja": "išiel by som", "ty": "išiel by si", "on": "išiel by", "my": "išli by sme", "vy": "išli by ste", "oni": "išli by" },
        "rozkazovaci": { "ty": "choď", "my": "poďme", "vy": "choďte" }
    },
    "prísť": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "prídem", "ty": "prídeš", "on": "príde", "my": "prídeme", "vy": "prídete", "oni": "prídu" },
        "indicativo.minuly": {
            "on": "prišiel", "ona": "prišla", "ono": "prišlo",
            "oni_anim": "prišli", "ony_inanim": "prišli", "ona_neut": "prišli"
        },
        "indicativo.budouci": { "ja": "prídem", "ty": "prídeš", "on": "príde", "my": "prídeme", "vy": "prídete", "oni": "prídu" },
        "podminovaci": { "ja": "prišiel by som", "ty": "prišiel by si", "on": "prišiel by", "my": "prišli by sme", "vy": "prišli by ste", "oni": "prišli by" },
        "rozkazovaci": { "ty": "príď", "my": "príďme", "vy": "príďte" }
    },
    "odísť": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "odídem", "ty": "odídeš", "on": "odíde", "my": "odídeme", "vy": "odídete", "oni": "odídu" },
        "indicativo.minuly": {
            "on": "odišiel", "ona": "odišla", "ono": "odišlo",
            "oni_anim": "odišli", "ony_inanim": "odišli", "ona_neut": "odišli"
        },
        "indicativo.budouci": { "ja": "odídem", "ty": "odídeš", "on": "odíde", "my": "odídeme", "vy": "odídete", "oni": "odídu" },
        "podminovaci": { "ja": "odišiel by som", "ty": "odišiel by si", "on": "odišiel by", "my": "odišli by sme", "vy": "odišli by ste", "oni": "odišli by" },
        "rozkazovaci": { "ty": "odíď", "my": "odíďme", "vy": "odíďte" }
    },
    "jesť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "jem", "ty": "ješ", "on": "je", "my": "jeme", "vy": "jete", "oni": "jedia" },
        "indicativo.minuly": {
            "on": "jedol", "ona": "jedla", "ono": "jedlo",
            "oni_anim": "jedli", "ony_inanim": "jedli", "ona_neut": "jedli"
        },
        "indicativo.budouci": { "ja": "budem jesť", "ty": "budeš jesť", "on": "bude jesť", "my": "budeme jesť", "vy": "budete jesť", "oni": "budú jesť" },
        "podminovaci": { "ja": "jedol by som", "ty": "jedol by si", "on": "jedol by", "my": "jedli by sme", "vy": "jedli by ste", "oni": "jedli by" },
        "rozkazovaci": { "ty": "jedz", "my": "jedzme", "vy": "jedzte" }
    },
    "piť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "pijem", "ty": "piješ", "on": "pije", "my": "pijeme", "vy": "pijete", "oni": "pijú" },
        "indicativo.minuly": {
            "on": "pil", "ona": "pila", "ono": "pilo",
            "oni_anim": "pili", "ony_inanim": "pili", "ona_neut": "pili"
        },
        "indicativo.budouci": { "ja": "budem piť", "ty": "budeš piť", "on": "bude piť", "my": "budeme piť", "vy": "budete piť", "oni": "budú piť" },
        "podminovaci": { "ja": "pil by som", "ty": "pil by si", "on": "pil by", "my": "pili by sme", "vy": "pili by ste", "oni": "pili by" },
        "rozkazovaci": { "ty": "pi", "my": "pime", "vy": "pite" }
    },
    "robiť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "robím", "ty": "robíš", "on": "robí", "my": "robíme", "vy": "robíte", "oni": "robia" },
        "indicativo.minuly": {
            "on": "robil", "ona": "robila", "ono": "robilo",
            "oni_anim": "robili", "ony_inanim": "robili", "ona_neut": "robili"
        },
        "indicativo.budouci": { "ja": "budem robiť", "ty": "budeš robiť", "on": "bude robiť", "my": "budeme robiť", "vy": "budete robiť", "oni": "budú robiť" },
        "podminovaci": { "ja": "robil by som", "ty": "robil by si", "on": "robil by", "my": "robili by sme", "vy": "robili by ste", "oni": "robili by" },
        "rozkazovaci": { "ty": "rob", "my": "robme", "vy": "robte" }
    },
    "urobiť": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "urobím", "ty": "urobíš", "on": "urobí", "my": "urobíme", "vy": "urobíte", "oni": "urobia" },
        "indicativo.minuly": {
            "on": "urobil", "ona": "urobila", "ono": "urobilo",
            "oni_anim": "urobili", "ony_inanim": "urobili", "ona_neut": "urobili"
        },
        "indicativo.budouci": { "ja": "urobím", "ty": "urobíš", "on": "urobí", "my": "urobíme", "vy": "urobíte", "oni": "urobia" },
        "podminovaci": { "ja": "urobil by som", "ty": "urobil by si", "on": "urobil by", "my": "urobili by sme", "vy": "urobili by ste", "oni": "urobili by" },
        "rozkazovaci": { "ty": "urob", "my": "urobme", "vy": "urobte" }
    },
    "hovoriť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "hovorím", "ty": "hovoríš", "on": "hovorí", "my": "hovoríme", "vy": "hovoríte", "oni": "hovoria" },
        "indicativo.minuly": {
            "on": "hovoril", "ona": "hovorila", "ono": "hovorilo",
            "oni_anim": "hovorili", "ony_inanim": "hovorili", "ona_neut": "hovorili"
        },
        "indicativo.budouci": { "ja": "budem hovoriť", "ty": "budeš hovoriť", "on": "bude hovoriť", "my": "budeme hovoriť", "vy": "budete hovoriť", "oni": "budú hovoriť" },
        "podminovaci": { "ja": "hovoril by som", "ty": "hovoril by si", "on": "hovoril by", "my": "hovorili by sme", "vy": "hovorili by ste", "oni": "hovorili by" },
        "rozkazovaci": { "ty": "hovor", "my": "hovorme", "vy": "hovorte" }
    },
    "povedať": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "poviem", "ty": "povieš", "on": "povie", "my": "povieme", "vy": "poviete", "oni": "povedia" },
        "indicativo.minuly": {
            "on": "povedal", "ona": "povedala", "ono": "povedalo",
            "oni_anim": "povedali", "ony_inanim": "povedali", "ona_neut": "povedali"
        },
        "indicativo.budouci": { "ja": "poviem", "ty": "povieš", "on": "povie", "my": "povieme", "vy": "poviete", "oni": "povedia" },
        "podminovaci": { "ja": "povedal by som", "ty": "povedal by si", "on": "povedal by", "my": "povedali by sme", "vy": "povedali by ste", "oni": "povedali by" },
        "rozkazovaci": { "ty": "povedz", "my": "povedzme", "vy": "povedzte" }
    },
    "písať": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "píšem", "ty": "píšeš", "on": "píše", "my": "píšeme", "vy": "píšete", "oni": "píšu" },
        "indicativo.minuly": {
            "on": "písal", "ona": "písala", "ono": "písalo",
            "oni_anim": "písali", "ony_inanim": "písali", "ona_neut": "písali"
        },
        "indicativo.budouci": { "ja": "budem písať", "ty": "budeš písať", "on": "bude písať", "my": "budeme písať", "vy": "budete písať", "oni": "budú písať" },
        "podminovaci": { "ja": "písal by som", "ty": "písal by si", "on": "písal by", "my": "písali by sme", "vy": "písali by ste", "oni": "písali by" },
        "rozkazovaci": { "ty": "píš", "my": "píšme", "vy": "píšte" }
    },
    "čítať": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "čítam", "ty": "čítaš", "on": "číta", "my": "čítame", "vy": "čítate", "oni": "čítajú" },
        "indicativo.minuly": {
            "on": "čítal", "ona": "čítala", "ono": "čítalo",
            "oni_anim": "čítali", "ony_inanim": "čítali", "ona_neut": "čítali"
        },
        "indicativo.budouci": { "ja": "budem čítať", "ty": "budeš čítať", "on": "bude čítať", "my": "budeme čítať", "vy": "budete čítať", "oni": "budú čítať" },
        "podminovaci": { "ja": "čítal by som", "ty": "čítal by si", "on": "čítal by", "my": "čítali by sme", "vy": "čítali by ste", "oni": "čítali by" },
        "rozkazovaci": { "ty": "čítaj", "my": "čítajme", "vy": "čítajte" }
    },
    "dať": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "dám", "ty": "dáš", "on": "dá", "my": "dáme", "vy": "dáte", "oni": "dajú" },
        "indicativo.minuly": {
            "on": "dal", "ona": "dala", "ono": "dalo",
            "oni_anim": "dali", "ony_inanim": "dali", "ona_neut": "dali"
        },
        "indicativo.budouci": { "ja": "dám", "ty": "dáš", "on": "dá", "my": "dáme", "vy": "dáte", "oni": "dajú" },
        "podminovaci": { "ja": "dal by som", "ty": "dal by si", "on": "dal by", "my": "dali by sme", "vy": "dali by ste", "oni": "dali by" },
        "rozkazovaci": { "ty": "daj", "my": "dajme", "vy": "dajte" }
    },
    "dávať": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "dávam", "ty": "dávaš", "on": "dáva", "my": "dávame", "vy": "dávate", "oni": "dávajú" },
        "indicativo.minuly": {
            "on": "dával", "ona": "dávala", "ono": "dávalo",
            "oni_anim": "dávali", "ony_inanim": "dávali", "ona_neut": "dávali"
        },
        "indicativo.budouci": { "ja": "budem dávať", "ty": "budeš dávať", "on": "bude dávať", "my": "budeme dávať", "vy": "budete dávať", "oni": "budú dávať" },
        "podminovaci": { "ja": "dával by som", "ty": "dával by si", "on": "dával by", "my": "dávali by sme", "vy": "dávali by ste", "oni": "dávali by" },
        "rozkazovaci": { "ty": "dávaj", "my": "dávajme", "vy": "dávajte" }
    },
    "vidieť": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "vidím", "ty": "vidíš", "on": "vidí", "my": "vidíme", "vy": "vidíte", "oni": "vidia" },
        "indicativo.minuly": {
            "on": "videl", "ona": "videla", "ono": "videlo",
            "oni_anim": "videli", "ony_inanim": "videli", "ona_neut": "videli"
        },
        "indicativo.budouci": { "ja": "budem vidieť", "ty": "budeš vidieť", "on": "bude vidieť", "my": "budeme vidieť", "vy": "budete vidieť", "oni": "budú vidieť" },
        "podminovaci": { "ja": "videl by som", "ty": "videl by si", "on": "videl by", "my": "videli by sme", "vy": "videli by ste", "oni": "videli by" },
        "rozkazovaci": { "ty": "viď", "my": "viďme", "vy": "viďte" }
    }
}

def clean_gloss(text):
    if not text:
        return ""
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'See Category:.*', '', text, flags=re.I)
    text = re.sub(r'See also:.*', '', text, flags=re.I)
    text = re.sub(r'\s+', ' ', text).strip(' ,;:')
    parts = [p.strip() for p in text.split(',') if p.strip()]
    return ", ".join(parts[:3])

def download_sources():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not FREQ_FILE.exists():
        print(f"Downloading frequency list from {FREQ_URL}...")
        req = urllib.request.Request(FREQ_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(FREQ_FILE, 'wb') as out:
            out.write(resp.read())
        print(f"Saved frequency list to {FREQ_FILE}")
    else:
        print(f"Frequency list already cached at {FREQ_FILE}")

    if not KAIKKI_FILE.exists():
        print(f"Downloading Kaikki Slovak dictionary extract from {KAIKKI_URL}...")
        req = urllib.request.Request(KAIKKI_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(KAIKKI_FILE, 'wb') as out:
            out.write(resp.read())
        print(f"Saved Kaikki Slovak dictionary to {KAIKKI_FILE}")
    else:
        print(f"Kaikki Slovak extract already cached at {KAIKKI_FILE}")

    if not LEMMAS_FILE.exists():
        print(f"Downloading MichMech lemmatization list from {LEMMAS_URL}...")
        req = urllib.request.Request(LEMMAS_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(LEMMAS_FILE, 'wb') as out:
            out.write(resp.read())
        print(f"Saved MichMech lemmatization list to {LEMMAS_FILE}")
    else:
        print(f"MichMech lemmatization list already cached at {LEMMAS_FILE}")

def parse_frequency():
    freq_rank = {}
    freq_list = []
    if FREQ_FILE.exists():
        with open(FREQ_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    word = parts[0].lower()
                    try:
                        count = int(parts[1])
                    except ValueError:
                        continue
                    if word not in freq_rank:
                        freq_rank[word] = count
                        freq_list.append(word)
    return freq_rank, freq_list

def build_verb_payload(lemma, forms_dict, aspect_found="imperfective"):
    aspect = aspect_found or "imperfective"
    pres = forms_dict.get("indicativo.presente", {})
    past = forms_dict.get("indicativo.minuly", {})
    fut = forms_dict.get("indicativo.budouci", {})
    cond = forms_dict.get("podminovaci", {})
    imperative = forms_dict.get("rozkazovaci", {})

    # Auto-generate compound future for imperfective verbs if missing
    if aspect == "imperfective" and not fut:
        fut = {
            "ja": f"budem {lemma}",
            "ty": f"budeš {lemma}",
            "on": f"bude {lemma}",
            "my": f"budeme {lemma}",
            "vy": f"budete {lemma}",
            "oni": f"budú {lemma}"
        }
    elif aspect == "perfective" and not fut:
        fut = pres.copy()

    indicativo = {
        "presente": pres,
        "minuly": past,
        "budouci": fut
    }

    if lemma in CANONICAL_VERBS:
        c = CANONICAL_VERBS[lemma]
        indicativo["presente"] = c.get("indicativo.presente", indicativo["presente"])
        indicativo["minuly"] = c.get("indicativo.minuly", indicativo["minuly"])
        indicativo["budouci"] = c.get("indicativo.budouci", indicativo["budouci"])
        cond = c.get("podminovaci", cond)
        imperative = c.get("rozkazovaci", imperative)
        aspect = c.get("aspect", aspect)

    return {
        "regular": lemma not in CANONICAL_VERBS,
        "infinitive": lemma,
        "infinitivo": lemma,
        "aspect": aspect,
        "indicativo": indicativo,
        "podminovaci": cond,
        "rozkazovaci": imperative,
        "tenses": {
            "indicativo.presente": indicativo["presente"],
            "indicativo.minuly": indicativo["minuly"],
            "indicativo.budouci": indicativo["budouci"]
        }
    }

def process_all():
    download_sources()
    freq_rank, freq_list = parse_frequency()

    WORD_INDEX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    VERBS_DIR.mkdir(parents=True, exist_ok=True)

    dictionary = {}
    word_index = defaultdict(list)
    verb_index = defaultdict(list)
    verb_data = defaultdict(lambda: {"forms": defaultdict(dict), "aspect": "imperfective"})

    if KAIKKI_FILE.exists():
        print(f"Parsing Kaikki Slovak extract from {KAIKKI_FILE}...")
        try:
            with gzip.open(KAIKKI_FILE, "rt", encoding="utf-8", errors="ignore") as f:
                count = 0
                for line in f:
                    count += 1
                    if count % 100000 == 0:
                        print(f"Processed {count:,} entries...")
                    try:
                        item = json.loads(line)
                    except Exception:
                        continue

                    word = item.get("word", "").strip().lower()
                    pos = item.get("pos", "")
                    mapped_pos = POS_MAP.get(pos, pos)
                    senses = item.get("senses", [])
                    item_tags = set(item.get("tags", []))

                    # Dictionary headwords
                    if word and mapped_pos in POS_MAP and 'form-of' not in item_tags:
                        gender = "m" if "masculine" in item_tags else "f" if "feminine" in item_tags else "n" if "neuter" in item_tags else None
                        aspect = "perfective" if "perfective" in item_tags else "imperfective" if "imperfective" in item_tags else None

                        glosses = []
                        for s in senses:
                            if 'form-of' in set(s.get("tags", [])):
                                continue
                            for g in s.get("glosses", []):
                                cg = clean_gloss(g)
                                if cg and len(cg) >= 2 and cg not in glosses:
                                    glosses.append(cg)
                                    if len(glosses) >= 3:
                                        break
                            if len(glosses) >= 3:
                                break

                        if glosses and (word not in dictionary or len(dictionary[word].get("en", "")) < len(", ".join(glosses))):
                            entry = {
                                "en": ", ".join(glosses),
                                "type": mapped_pos
                            }
                            if gender:
                                entry["gender"] = gender
                            if aspect:
                                entry["aspect"] = aspect
                            dictionary[word] = entry

                    # Process inflected forms
                    forms = item.get("forms", [])
                    for fi in forms:
                        form = fi.get("form", "").strip().lower()
                        ftags = set(fi.get("tags", []))
                        if not form or form == word:
                            continue

                        if mapped_pos == "verb":
                            if word not in verb_index[form]:
                                verb_index[form].append(word)

                            # Extract person/tense forms for verb library
                            if "present" in ftags:
                                if "first-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["ja"] = form
                                elif "second-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["ty"] = form
                                elif "third-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["on"] = form
                                elif "first-person" in ftags and "plural" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["my"] = form
                                elif "second-person" in ftags and "plural" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["vy"] = form
                                elif "third-person" in ftags and "plural" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["oni"] = form

                            if "past" in ftags or "participle" in ftags:
                                if "masculine" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"]["on"] = form
                                elif "feminine" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"]["ona"] = form
                                elif "neuter" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"]["ono"] = form
                                elif "plural" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"]["oni_anim"] = form
                                    verb_data[word]["forms"]["indicativo.minuly"]["ony_inanim"] = form

                            if "imperative" in ftags:
                                if "singular" in ftags and "second-person" in ftags:
                                    verb_data[word]["forms"]["rozkazovaci"]["ty"] = form
                                elif "plural" in ftags and "first-person" in ftags:
                                    verb_data[word]["forms"]["rozkazovaci"]["my"] = form
                                elif "plural" in ftags and "second-person" in ftags:
                                    verb_data[word]["forms"]["rozkazovaci"]["vy"] = form

                        else:
                            if word not in word_index[form]:
                                word_index[form].append(word)

                print(f"Finished parsing Kaikki. Total raw entries: {count:,}")
        except Exception as e:
            print(f"Warning: error parsing Kaikki extract: {e}")

    # Incorporate MichMech high-coverage lemmatization dataset
    if LEMMAS_FILE.exists():
        print(f"Parsing MichMech lemmatization list from {LEMMAS_FILE}...")
        try:
            with open(LEMMAS_FILE, "r", encoding="utf-8", errors="ignore") as f:
                pair_count = 0
                for line in f:
                    parts = line.strip().split("\t")
                    if len(parts) >= 2:
                        lemma = parts[0].strip().lower()
                        form = parts[1].strip().lower()
                        if form and lemma and form != lemma:
                            if lemma in dictionary or lemma in freq_rank:
                                if lemma not in word_index[form]:
                                    word_index[form].append(lemma)
                                pair_count += 1
                print(f"Added {pair_count:,} lemma-token mappings from MichMech.")
        except Exception as e:
            print(f"Warning parsing MichMech lemmatization list: {e}")

    # Merge additions if present
    if ADDITIONS_FILE.exists():
        print(f"Merging additions from {ADDITIONS_FILE}...")
        with open(ADDITIONS_FILE, "r", encoding="utf-8") as f:
            additions = json.load(f)
            for k, v in additions.items():
                dictionary[k.lower()] = v

    print(f"Total headwords in dictionary: {len(dictionary):,}")
    print(f"Saving dictionary to {DICT_OUTPUT}...")
    with open(DICT_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

    # Save frequency index
    print(f"Saving frequency rankings to {FREQUENCY_OUTPUT}...")
    with open(FREQUENCY_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(freq_rank, f, ensure_ascii=False)

    # Filter & compact word index to frequent words
    print("Compacting word-index.json...")
    compact_word_index = {}
    top_lemmas_set = set(freq_list[:40000]) if freq_list else set(list(dictionary.keys())[:40000])
    for form, lemmas in word_index.items():
        vetted = [l for l in lemmas if l in top_lemmas_set or l in dictionary]
        if vetted:
            compact_word_index[form] = vetted[:2]

    print(f"Saving word-index ({len(compact_word_index):,} forms) to {WORD_INDEX_OUTPUT}...")
    with open(WORD_INDEX_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(compact_word_index, f, ensure_ascii=False)

    # Save verb index
    print(f"Saving verb-index ({len(verb_index):,} forms) to {VERB_INDEX_OUTPUT}...")
    compact_verb_index = {f: v[:2] for f, v in verb_index.items()}
    with open(VERB_INDEX_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(compact_verb_index, f, ensure_ascii=False)

    # Build verb catalog
    print("Generating verb library...")
    all_verbs_set = set(PRIORITY_VERBS)
    for v in PRIORITY_VERBS:
        all_verbs_set.add(v)
    for w in freq_list:
        if len(all_verbs_set) >= 120:
            break
        if w in dictionary and dictionary[w].get("type") == "verb":
            all_verbs_set.add(w)

    final_verb_list = sorted(list(all_verbs_set))
    for vlemma in final_verb_list:
        v_payload = build_verb_payload(
            vlemma,
            verb_data[vlemma]["forms"],
            verb_data[vlemma]["aspect"]
        )
        verb_path = VERBS_DIR / f"{vlemma}.json"
        with open(verb_path, "w", encoding="utf-8") as f:
            json.dump(v_payload, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(final_verb_list)} individual verb files to {VERBS_DIR}")

    # Save verb-list-sk.js
    with open(VERB_LIST_OUTPUT, "w", encoding="utf-8") as f:
        f.write("// Slovak Verb Catalog for Verb Practice Driller\n")
        f.write("const ALL_SLOVAK_VERBS = [\n")
        for i, v in enumerate(final_verb_list):
            comma = "," if i < len(final_verb_list) - 1 else ""
            f.write(f"    '{v}'{comma}\n")
        f.write("];\n\n")
        f.write("if (typeof window !== 'undefined') {\n")
        f.write("    window.ALL_SLOVAK_VERBS = ALL_SLOVAK_VERBS;\n")
        f.write("}\n")
        f.write("if (typeof global !== 'undefined') {\n")
        f.write("    global.ALL_SLOVAK_VERBS = ALL_SLOVAK_VERBS;\n")
        f.write("}\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("    module.exports = ALL_SLOVAK_VERBS;\n")
        f.write("}\n")
    print(f"Saved {VERB_LIST_OUTPUT} with {len(final_verb_list)} verbs.")

if __name__ == "__main__":
    process_all()
