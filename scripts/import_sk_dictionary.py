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
    "intj": "interjection",
    "interjection": "interjection",
    "proper noun": "proper noun",
    "name": "proper noun",
    "particle": "particle"
}

FORM_RE = re.compile(
    r'^(?:(?:first|second|third)-person\s+(?:singular|plural|indicative|subjunctive|imperative|present|past|future|conditional)|(?:singular|plural) of|inflection of|past participle of|present participle of|gerund of|(?:masculine|feminine|neuter) (?:plural|singular) of|alternative (?:form|spelling|letter-case form) of|obsolete (?:form|spelling) of|archaic (?:form|spelling) of|dated (?:form|spelling) of|misspelling of|contraction of|abbreviation of|initialism of|the name of the latin script letter)\b',
    re.I
)
DEPRIORITISE_TAGS = {'obsolete', 'archaic', 'dated', 'rare', 'poetic', 'heraldry', 'dialectal', 'misspelling', 'colloquial'}
NOISE_FORM_TAGS = {'table-tags', 'inflection-template', 'class', 'auxiliary', 'alternative', 'archaic', 'obsolete', 'dated', 'dialectal', 'rare'}
POS_PRIORITY = {
    'preposition': 1, 'conjunction': 1, 'pronoun': 2, 'determiner': 2, 'particle': 2,
    'interjection': 3, 'adverb': 4, 'verb': 5, 'noun': 6, 'adjective': 7, 'numeral': 8
}

PRIORITY_VERBS = [
    "byť", "mať", "môcť", "chcieť", "vedieť", "poznať", "povedať", "hovoriť",
    "robiť", "urobiť", "vidieť", "uvidieť", "myslieť", "pomyslieť", "ísť", "prísť",
    "odísť", "cestovať", "brať", "vziať", "dávať", "dať", "rozumieť",
    "porozumieť", "čakať", "počkať", "pýtať", "opýtať", "odpovedať",
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

SK_PREFIX_PAIRS = {
    "opýtať": ("o", "pýtať", "perfective"),
    "pomyslieť": ("po", "myslieť", "perfective"),
    "poprosiť": ("po", "prosiť", "perfective"),
    "porozumieť": ("po", "rozumieť", "perfective"),
    "skončiť": ("s", "končiť", "perfective"),
    "uvidieť": ("u", "vidieť", "perfective"),
    "vypiť": ("vy", "piť", "perfective"),
    "zaplatiť": ("za", "platiť", "perfective"),
    "zavolať": ("za", "volať", "perfective"),
    "zjesť": ("z", "jesť", "perfective"),
}

SK_IRREGULAR_OR_MISSING = {
    "ležať": {
        "aspect": "imperfective",
        "pres": {"ja": "ležím", "ty": "ležíš", "on": "leží", "my": "ležíme", "vy": "ležíte", "oni": "ležia"},
        "past": {"on": "ležal", "ona": "ležala", "ono": "ležalo", "oni_anim": "ležali"},
        "imp": {"ty": "lež", "my": "ležme", "vy": "ležte"}
    },
    "odpovedať": {
        "aspect": "imperfective",
        "pres": {"ja": "odpovedám", "ty": "odpovedáš", "on": "odpovedá", "my": "odpovedáme", "vy": "odpovedáte", "oni": "odpovedajú"},
        "past": {"on": "odpovedal", "ona": "odpovedala", "ono": "odpovedalo", "oni_anim": "odpovedali"},
        "imp": {"ty": "odpovedaj", "my": "odpovedajme", "vy": "odpovedajte"}
    },
    "pozrieť": {
        "aspect": "perfective",
        "pres": {"ja": "pozriem", "ty": "pozrieš", "on": "pozrie", "my": "pozrieme", "vy": "pozriete", "oni": "pozrú"},
        "past": {"on": "pozrel", "ona": "pozrela", "ono": "pozrelo", "oni_anim": "pozreli"},
        "imp": {"ty": "pozri", "my": "pozrime", "vy": "pozrite"}
    },
    "sadnúť": {
        "aspect": "perfective",
        "pres": {"ja": "sadnem", "ty": "sadneš", "on": "sadne", "my": "sadneme", "vy": "sadnete", "oni": "sadnú"},
        "past": {"on": "sadol", "ona": "sadla", "ono": "sadlo", "oni_anim": "sadli"},
        "imp": {"ty": "sadni", "my": "sadnime", "vy": "sadnite"}
    },
    "cítiť": {
        "aspect": "imperfective",
        "pres": {"ja": "cítim", "ty": "cítiš", "on": "cíti", "my": "cítime", "vy": "cítite", "oni": "cítia"},
        "past": {"on": "cítil", "ona": "cítila", "ono": "cítilo", "oni_anim": "cítili"},
        "imp": {"ty": "cíť", "my": "cíťme", "vy": "cíťte"}
    },
    "prosiť": {
        "aspect": "imperfective",
        "pres": {"ja": "prosím", "ty": "prosíš", "on": "prosí", "my": "prosíme", "vy": "prosíte", "oni": "prosia"},
        "past": {"on": "prosil", "ona": "prosila", "ono": "prosilo", "oni_anim": "prosili"},
        "imp": {"ty": "pros", "my": "prosme", "vy": "proste"}
    },
    "jazdiť": {
        "aspect": "imperfective",
        "pres": {"ja": "jazdím", "ty": "jazdíš", "on": "jazdí", "my": "jazdíme", "vy": "jazdíte", "oni": "jazdia"},
        "past": {"on": "jazdil", "ona": "jazdila", "ono": "jazdilo", "oni_anim": "jazdili"},
        "imp": {"ty": "jazdi", "my": "jazdime", "vy": "jazdite"}
    },
    "ospravedlniť": {
        "aspect": "perfective",
        "pres": {"ja": "ospravedlním", "ty": "ospravedlníš", "on": "ospravedlní", "my": "ospravedlníme", "vy": "ospravedlníte", "oni": "ospravedlnia"},
        "past": {"on": "ospravedlnil", "ona": "ospravedlnila", "ono": "ospravedlnilo", "oni_anim": "ospravedlnili"},
        "imp": {"ty": "ospravedlň", "my": "ospravedlňme", "vy": "ospravedlňte"}
    },
    "stratiť": {
        "aspect": "perfective",
        "pres": {"ja": "stratím", "ty": "stratíš", "on": "stratí", "my": "stratíme", "vy": "stratíte", "oni": "stratia"},
        "past": {"on": "stratil", "ona": "stratila", "ono": "stratilo", "oni_anim": "stratili"},
        "imp": {"ty": "strať", "my": "straťme", "vy": "straťte"}
    },
    "počkať": {"aspect": "perfective"},
    "poďakovať": {"aspect": "perfective"},
}

SK_VERB_EN_OVERRIDES = {
    "byť": "to be",
    "mať": "to have",
    "brať": "to take",
    "stáť": "to stand; to cost",
    "báť": "to fear, to be afraid",
    "cítiť": "to feel, to sense",
    "jazdiť": "to drive, to ride",
    "kupovať": "to buy",
    "ležať": "to lie, to recline",
    "odpovedať": "to answer, to reply",
    "opýtať": "to ask",
    "ospravedlniť": "to excuse, to apologize",
    "otvárať": "to open",
    "pomyslieť": "to think, to consider",
    "pomáhať": "to help, to assist",
    "poprosiť": "to ask politely, to request",
    "porozumieť": "to understand",
    "pozrieť": "to look, to check",
    "počkať": "to wait",
    "poďakovať": "to thank",
    "prečítať": "to read through",
    "prosiť": "to ask, to beg",
    "sadnúť": "to sit down",
    "skončiť": "to finish, to end",
    "stratiť": "to lose",
    "strácať": "to lose (impf.)",
    "ukazovať": "to show, to point",
    "uvidieť": "to see, to catch sight of",
    "vypiť": "to drink up",
    "zaplatiť": "to pay",
    "zatvárať": "to close, to shut",
    "zavolať": "to call",
    "začínať": "to begin, to start",
    "zjesť": "to eat up",
    "zostávať": "to stay, to remain",
}

def clean_sk_verb_en(lemma, raw_en):
    if lemma in SK_VERB_EN_OVERRIDES:
        return SK_VERB_EN_OVERRIDES[lemma]
    if not raw_en:
        return ""
    parts = []
    for p in re.split(r'[;,]', raw_en):
        p = p.strip()
        low = p.lower()
        if not p or low.startswith(('used ', 'synonym of', 'expressing ', 'with ', 'see ')):
            continue
        if p not in parts:
            parts.append(p)
        if len(", ".join(parts)) > 40 or len(parts) >= 2:
            break
    return ", ".join(parts) if parts else raw_en.split(",")[0].strip()

def _synth_sk_regular(lemma):
    """Regular Slovak conjugation fallback for -ovať / -ať / -iť / -ieť."""
    if lemma.endswith("ovať"):
        st = lemma[:-4]
        return (
            {"ja": st + "ujem", "ty": st + "uješ", "on": st + "uje", "my": st + "ujeme", "vy": st + "ujete", "oni": st + "ujú"},
            {"on": lemma[:-1] + "l", "ona": lemma[:-1] + "la", "ono": lemma[:-1] + "lo", "oni_anim": lemma[:-1] + "li"},
            {"ty": st + "uj", "my": st + "ujme", "vy": st + "ujte"},
        )
    if lemma.endswith(("ať", "iať")):
        st = lemma[:-2]
        # Rhythmic law: short final stem syllable takes -ám/-áš/-á/-áme/-áte; long takes -am/-aš/-a/-ame/-ate
        prev = st[:-1] if lemma.endswith("ať") else st
        is_long = any(v in prev[-3:] for v in ("á", "é", "í", "ó", "ú", "ý", "ô", "ŕ", "ĺ", "ia", "ie", "iu"))
        a_v = "a" if is_long else "á"
        return (
            {"ja": st + f"{a_v}m", "ty": st + f"{a_v}š", "on": st + a_v, "my": st + f"{a_v}me", "vy": st + f"{a_v}te", "oni": st + "ajú"},
            {"on": st + "al", "ona": st + "ala", "ono": st + "alo", "oni_anim": st + "ali"},
            {"ty": st + "aj", "my": st + "ajme", "vy": st + "ajte"},
        )
    if lemma.endswith("iť"):
        st = lemma[:-2]
        return (
            {"ja": st + "ím", "ty": st + "íš", "on": st + "í", "my": st + "íme", "vy": st + "íte", "oni": st + "ia"},
            {"on": st + "il", "ona": st + "ila", "ono": st + "ilo", "oni_anim": st + "ili"},
            {"ty": st, "my": st + "me", "vy": st + "te"},
        )
    if lemma.endswith("ieť"):
        st = lemma[:-3]
        return (
            {"ja": st + "iem", "ty": st + "ieš", "on": st + "ie", "my": st + "ieme", "vy": st + "iete", "oni": st + "ejú"},
            {"on": st + "el", "ona": st + "ela", "ono": st + "elo", "oni_anim": st + "eli"},
            {"ty": st + "ej", "my": st + "ejme", "vy": st + "ejte"},
        )
    st = lemma[:-1]
    return (
        {"ja": st + "em", "ty": st + "eš", "on": st + "e", "my": st + "eme", "vy": st + "ete", "oni": st + "ú"},
        {"on": st + "l", "ona": st + "la", "ono": st + "lo", "oni_anim": st + "li"},
        {"ty": st + "i", "my": st + "ime", "vy": st + "ite"},
    )

def build_verb_payload(lemma, forms_dict, aspect_found="imperfective", en_gloss=""):
    aspect = aspect_found or "imperfective"
    pres = dict(forms_dict.get("indicativo.presente", {}))
    past = dict(forms_dict.get("indicativo.minuly", {}))
    fut = dict(forms_dict.get("indicativo.budouci", {}))
    cond = dict(forms_dict.get("podminovaci", {}))
    imperative = dict(forms_dict.get("rozkazovaci", {}))

    if lemma in SK_IRREGULAR_OR_MISSING:
        ov = SK_IRREGULAR_OR_MISSING[lemma]
        aspect = ov.get("aspect", aspect)
        if "pres" in ov and not pres:
            pres = dict(ov["pres"])
        if "past" in ov and not past:
            past = dict(ov["past"])
        if "imp" in ov and not imperative:
            imperative = dict(ov["imp"])

    # Fill missing forms via regular Slovak patterns when Kaikki lacked entries
    if not pres or not past or (not imperative and lemma not in ("môcť", "musieť")):
        reg_p, reg_l, reg_i = _synth_sk_regular(lemma)
        if not pres:
            pres = reg_p
        if not past:
            past = reg_l
        else:
            for k, v in reg_l.items():
                past.setdefault(k, v)
        if not imperative and lemma not in ("môcť", "musieť"):
            imperative = reg_i

    # Synthesize future
    if aspect == "perfective":
        if not fut:
            fut = dict(pres)
    elif not fut:
        fut = {
            "ja": f"budem {lemma}",
            "ty": f"budeš {lemma}",
            "on": f"bude {lemma}",
            "my": f"budeme {lemma}",
            "vy": f"budete {lemma}",
            "oni": f"budú {lemma}"
        }

    # Synthesize conditional from L-participle
    if not cond and past.get("on") and past.get("oni_anim"):
        cond = {
            "ja": f"{past['on']} by som",
            "ty": f"{past['on']} by si",
            "on": f"{past['on']} by",
            "my": f"{past['oni_anim']} by sme",
            "vy": f"{past['oni_anim']} by ste",
            "oni": f"{past['oni_anim']} by"
        }

    indicativo = {
        "presente": pres,
        "minuly": past,
        "budouci": fut
    }

    if lemma in CANONICAL_VERBS:
        c = CANONICAL_VERBS[lemma]
        indicativo["presente"] = dict(c.get("indicativo.presente", indicativo["presente"]))
        indicativo["minuly"] = dict(c.get("indicativo.minuly", indicativo["minuly"]))
        indicativo["budouci"] = dict(c.get("indicativo.budouci", indicativo["budouci"]))
        cond = dict(c.get("podminovaci", cond))
        imperative = dict(c.get("rozkazovaci", imperative))
        aspect = c.get("aspect", aspect)

    # Populate VerbsTable / VerbsSpeed defaultPersons ('ja', 'ty', 'my', 'vy', 'oni') on minuly
    minuly = indicativo["minuly"]
    on_m = minuly.get("on", "")
    ona_f = minuly.get("ona", "")
    oni_a = minuly.get("oni_anim") or minuly.get("oni", "")
    minuly.setdefault("ony_inanim", oni_a)
    minuly.setdefault("ona_neut", oni_a)
    if on_m:
        minuly.setdefault("ja", f"{on_m} som/{ona_f} som" if ona_f and ona_f != on_m else f"{on_m} som")
        minuly.setdefault("ty", f"{on_m} si/{ona_f} si" if ona_f and ona_f != on_m else f"{on_m} si")
    if oni_a:
        minuly.setdefault("my", f"{oni_a} sme")
        minuly.setdefault("vy", f"{oni_a} ste")
        minuly.setdefault("oni", oni_a)

    return {
        "regular": lemma not in CANONICAL_VERBS,
        "infinitive": lemma,
        "infinitivo": lemma,
        "aspect": aspect,
        "english": {
            "infinitivo": clean_sk_verb_en(lemma, en_gloss)
        },
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

    verbs_only = "--verbs-only" in sys.argv
    dictionary = {}
    if verbs_only and DICT_OUTPUT.exists():
        with open(DICT_OUTPUT, "r", encoding="utf-8") as df:
            dictionary = json.load(df)

    lemma_candidates = defaultdict(lambda: defaultdict(lambda: {"primary": [], "senses": [], "gender": None, "aspect": None, "deprioritised": True}))
    word_index = defaultdict(list)
    verb_index = defaultdict(list)
    verb_data = defaultdict(lambda: {"forms": defaultdict(dict), "aspect": None})
    verb_glosses = {}

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
                    if verbs_only and mapped_pos != "verb":
                        continue
                    senses = item.get("senses", [])
                    item_tags = set(item.get("tags", []))

                    # Dictionary headwords
                    if not verbs_only and word and pos in POS_MAP and 'form-of' not in item_tags:
                        gender = "m" if "masculine" in item_tags else "f" if "feminine" in item_tags else "n" if "neuter" in item_tags else None
                        aspect = "perfective" if "perfective" in item_tags else "imperfective" if "imperfective" in item_tags else None
                        cand = lemma_candidates[word][mapped_pos]
                        if gender and not cand["gender"]:
                            cand["gender"] = gender
                        if aspect and not cand["aspect"]:
                            cand["aspect"] = aspect

                        for s in senses:
                            stags = set(s.get("tags", []))
                            if 'form-of' in stags or 'misspelling' in stags:
                                continue
                            gloss_list = s.get("glosses", [])
                            if not gloss_list:
                                continue
                            g = gloss_list[-1]
                            if FORM_RE.search(g):
                                continue
                            cg = clean_gloss(g)
                            if cg and len(cg) >= 1 and cg not in cand["senses"]:
                                cand["senses"].append(cg)
                                is_dep = bool((item_tags | stags) & DEPRIORITISE_TAGS)
                                if not is_dep:
                                    cand["deprioritised"] = False
                                    if cg not in cand["primary"]:
                                        cand["primary"].append(cg)

                    if mapped_pos == "verb" and word and word not in verb_glosses and 'form-of' not in item_tags:
                        for s in senses:
                            stags = set(s.get("tags", []))
                            if 'form-of' in stags or 'misspelling' in stags or (stags & DEPRIORITISE_TAGS):
                                continue
                            gloss_list = s.get("glosses", [])
                            if not gloss_list:
                                continue
                            g = gloss_list[-1]
                            if FORM_RE.search(g):
                                continue
                            cg = clean_gloss(g)
                            if cg:
                                verb_glosses[word] = cg
                                break

                    # Process inflected forms
                    forms = item.get("forms", [])
                    table_aspect = None
                    if mapped_pos == "verb":
                        for fi in forms:
                            if "table-tags" in (fi.get("tags") or []):
                                tf = (fi.get("form") or "").strip().lower()
                                if tf in ("imperfective", "perfective"):
                                    table_aspect = tf
                                break
                        if table_aspect and not verb_data[word]["aspect"]:
                            verb_data[word]["aspect"] = table_aspect

                    for fi in forms:
                        form = fi.get("form", "").strip().lower()
                        ftags = set(fi.get("tags", []))
                        if not form or form == word or ' ' in form or '-' in form or '(' in form or not any(ch.isalpha() for ch in form) or (ftags & NOISE_FORM_TAGS):
                            continue

                        if mapped_pos == "verb":
                            if not verbs_only and word not in verb_index[form]:
                                verb_index[form].append(word)

                            if "colloquial" in ftags or "noun-from-verb" in ftags or "passive" in ftags or "participle" in ftags:
                                continue

                            # Extract person/tense forms for verb library
                            if "present" in ftags and "indicative" in ftags and "imperative" not in ftags and "past" not in ftags:
                                pslot = None
                                if "first-person" in ftags and "singular" in ftags:
                                    pslot = "ja"
                                elif "second-person" in ftags and "singular" in ftags:
                                    pslot = "ty"
                                elif "third-person" in ftags and "singular" in ftags:
                                    pslot = "on"
                                elif "first-person" in ftags and "plural" in ftags:
                                    pslot = "my"
                                elif "second-person" in ftags and "plural" in ftags:
                                    pslot = "vy"
                                elif "third-person" in ftags and "plural" in ftags:
                                    pslot = "oni"
                                if pslot:
                                    verb_data[word]["forms"]["indicativo.presente"].setdefault(pslot, form)

                            # Slovak Kaikki past tags are shifted off-by-one; identify bare L-participle by ending
                            elif "past" in ftags and "perfect" not in ftags and "conditional" not in ftags:
                                if form.endswith("la"):
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("ona", form)
                                elif form.endswith("lo"):
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("ono", form)
                                elif form.endswith("li"):
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("oni_anim", form)
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("ony_inanim", form)
                                elif form.endswith("l"):
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("on", form)

                            elif "imperative" in ftags:
                                if "singular" in ftags and "second-person" in ftags:
                                    verb_data[word]["forms"]["rozkazovaci"].setdefault("ty", form)
                                elif "plural" in ftags and "first-person" in ftags:
                                    verb_data[word]["forms"]["rozkazovaci"].setdefault("my", form)
                                elif "plural" in ftags and "second-person" in ftags:
                                    verb_data[word]["forms"]["rozkazovaci"].setdefault("vy", form)

                        elif not verbs_only:
                            if word not in word_index[form]:
                                word_index[form].append(word)

                print(f"Finished parsing Kaikki. Total raw entries: {count:,}")
        except Exception as e:
            print(f"Warning: error parsing Kaikki extract: {e}")

    if not verbs_only:
        for word, pos_entries in lemma_candidates.items():
            valid_pos = {p: info for p, info in pos_entries.items() if info["senses"]}
            if not valid_pos:
                continue
            best_pos = min(valid_pos.keys(), key=lambda p: (1 if valid_pos[p]["deprioritised"] else 0, POS_PRIORITY.get(p, 99)))
            info = valid_pos[best_pos]
            chosen = info["primary"] or info["senses"]
            entry = {"en": ", ".join(chosen[:3]), "type": best_pos}
            if info["gender"]:
                entry["gender"] = info["gender"]
            if info["aspect"]:
                entry["aspect"] = info["aspect"]
            dictionary[word] = entry

        FOUNDATIONAL_DICT = {
        "a": {"en": "and", "type": "conjunction"},
        "i": {"en": "and also, even", "type": "conjunction"},
        "v": {"en": "in, at, inside", "type": "preposition"},
        "vo": {"en": "in, at, inside", "type": "preposition"},
        "na": {"en": "on, onto, for", "type": "preposition"},
        "do": {"en": "to, into, until", "type": "preposition"},
        "z": {"en": "from, out of", "type": "preposition"},
        "zo": {"en": "from, out of", "type": "preposition"},
        "s": {"en": "with", "type": "preposition"},
        "so": {"en": "with", "type": "preposition"},
        "k": {"en": "to, toward", "type": "preposition"},
        "o": {"en": "about, at", "type": "preposition"},
        "u": {"en": "at (someone's place), by", "type": "preposition"},
        "pre": {"en": "for, because of", "type": "preposition"},
        "po": {"en": "after, along, per", "type": "preposition"},
        "pri": {"en": "by, near, during", "type": "preposition"},
        "od": {"en": "from, since", "type": "preposition"},
        "to": {"en": "it, this, that", "type": "pronoun"},
        "sa": {"en": "oneself (reflexive)", "type": "pronoun"},
        "si": {"en": "to oneself (reflexive)", "type": "pronoun"},
        "ale": {"en": "but, however", "type": "conjunction"},
        "že": {"en": "that (conjunction)", "type": "conjunction"},
        "aj": {"en": "also, too, even", "type": "particle"},
        "tak": {"en": "so, thus, this way", "type": "adverb"},
        "tu": {"en": "here", "type": "adverb"},
        "už": {"en": "already, anymore", "type": "adverb"},
        "ešte": {"en": "still, yet, more", "type": "adverb"},
        "čo": {"en": "what", "type": "pronoun"},
        "kto": {"en": "who", "type": "pronoun"},
        "kde": {"en": "where", "type": "adverb"},
        "keď": {"en": "when", "type": "conjunction"},
        "prečo": {"en": "why", "type": "adverb"},
        "ako": {"en": "how, like, as", "type": "adverb"},
        "je": {"en": "is (3rd sg of byť)", "type": "verb"},
        "som": {"en": "I am (1st sg of byť)", "type": "verb"},
        "sme": {"en": "we are (1st pl of byť)", "type": "verb"},
        "ste": {"en": "you are (2nd pl of byť)", "type": "verb"},
        "sú": {"en": "they are (3rd pl of byť)", "type": "verb"},
        "bol": {"en": "was (masc. past of byť)", "type": "verb"},
        "ma": {"en": "me, to me; has (3rd sg of mať)", "type": "pronoun"},
        "mi": {"en": "to me", "type": "pronoun"},
        "ho": {"en": "him, it", "type": "pronoun"},
        "ti": {"en": "to you (sg)", "type": "pronoun"},
        "ťa": {"en": "you (acc. sg)", "type": "pronoun"},
        "toto": {"en": "this (here)", "type": "pronoun"},
        "aby": {"en": "so that, in order to", "type": "conjunction"},
        "za": {"en": "behind, beyond; for", "type": "preposition"},
        "no": {"en": "well; but", "type": "particle"}
        }
        for k, v in FOUNDATIONAL_DICT.items():
            if k not in dictionary:
                dictionary[k] = v

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
                            if form and lemma and form != lemma and ' ' not in form and '-' not in form and form.isalpha():
                                if lemma in dictionary:
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
            json.dump(freq_list, f, ensure_ascii=False)

        # Filter & compact word/verb indexes to lemmas present in dictionary
        print("Compacting word-index.json and verb-index.json...")
        top_lemmas_set = (set(freq_list[:40000]) & set(dictionary.keys())) if freq_list else set(dictionary.keys())
        compact_word_index = {}
        for form, lemmas in word_index.items():
            vetted = [l for l in lemmas if l in top_lemmas_set or l in dictionary]
            if vetted:
                compact_word_index[form] = vetted[:2]

        print(f"Saving word-index ({len(compact_word_index):,} forms) to {WORD_INDEX_OUTPUT}...")
        with open(WORD_INDEX_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(compact_word_index, f, ensure_ascii=False, separators=(',', ':'))

        compact_verb_index = {}
        verb_filter = top_lemmas_set | set(PRIORITY_VERBS)
        for form, lemmas in verb_index.items():
            vetted = [l for l in lemmas if l in verb_filter and l in dictionary]
            if vetted:
                compact_verb_index[form] = vetted[:2]
        print(f"Saving verb-index ({len(compact_verb_index):,} forms) to {VERB_INDEX_OUTPUT}...")
        with open(VERB_INDEX_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(compact_verb_index, f, ensure_ascii=False, separators=(',', ':'))
    else:
        print("Skipping dictionary/index writes (--verbs-only).")

    if "--indexes-only" in sys.argv:
        print("Skipping verb files generation (--indexes-only).")
        return

    # Derive prefix-inherited verb tables from Kaikki base / canonical verbs
    for deriv, (px, base, p_asp) in SK_PREFIX_PAIRS.items():
        if not verb_data[deriv]["forms"]:
            src = CANONICAL_VERBS.get(base) or verb_data.get(base, {}).get("forms", {})
            for tkey in ("indicativo.presente", "indicativo.minuly", "rozkazovaci"):
                if src.get(tkey):
                    verb_data[deriv]["forms"][tkey] = {pk: f"{px}{pv}" for pk, pv in src[tkey].items()}
            verb_data[deriv]["aspect"] = p_asp

    # Build verb catalog (only genuine -ť infinitives)
    print("Generating verb library...")
    all_verbs_set = set(PRIORITY_VERBS)
    for w in freq_list:
        if len(all_verbs_set) >= 120:
            break
        if w in dictionary and dictionary[w].get("type") == "verb" and w.endswith("ť") and w != "ďakujem":
            all_verbs_set.add(w)

    final_verb_list = sorted(list(all_verbs_set))
    for stale in VERBS_DIR.glob("*.json"):
        if stale.stem not in all_verbs_set:
            stale.unlink()
    for vlemma in final_verb_list:
        raw_en = verb_glosses.get(vlemma) or (dictionary.get(vlemma, {}).get("en", ""))
        v_payload = build_verb_payload(
            vlemma,
            verb_data[vlemma]["forms"],
            verb_data[vlemma]["aspect"] or "imperfective",
            raw_en
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
