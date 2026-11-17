#!/usr/bin/env python3
"""
Import comprehensive Czech-English dictionary, morphology indexes, and verb library
from Kaikki.org (Wiktionary extract) and HermitDave OpenSubtitles Frequency list.

Attribution & Licensing:
- Kaikki.org / Wiktionary: CC BY-SA 3.0 & GFDL (Tatu Ylonen / Wiktionary contributors)
- HermitDave FrequencyWords: CC BY-SA 3.0 (HermitDave / OpenSubtitles)
- Svobodné slovníky: GNU FDL (svobodneslovniky.cz)

Outputs:
  imports/dictionary/czech-en.json
  content/cs/indexes/word-index.json
  content/cs/indexes/verb-index.json
  content/cs/indexes/frequency.json
  imports/verbs/cs/<lemma>.json (Conjugation tables for top verbs)
  imports/verbs/cs/verb-list-cs.js (ALL_CZECH_VERBS list)
"""
import gzip
import json
import os
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

KAIKKI_URL = "https://kaikki.org/dictionary/Czech/kaikki.org-dictionary-Czech.jsonl.gz"
FREQ_URL = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/cs/cs_50k.txt"

CACHE_DIR = Path("imports/dictionary")
KAIKKI_FILE = CACHE_DIR / "kaikki-cs.jsonl.gz"
FREQ_FILE = CACHE_DIR / "frequency-cs.txt"
ADDITIONS_FILE = CACHE_DIR / "additions-cs.json"

DICT_OUTPUT = CACHE_DIR / "czech-en.json"
WORD_INDEX_OUTPUT = Path("content/cs/indexes/word-index.json")
VERB_INDEX_OUTPUT = Path("content/cs/indexes/verb-index.json")
FREQUENCY_OUTPUT = Path("content/cs/indexes/frequency.json")
VERBS_DIR = Path("imports/verbs/cs")
VERB_LIST_OUTPUT = VERBS_DIR / "verb-list-cs.js"

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
    "být", "mít", "moct", "moci", "chtít", "vědět", "znát", "říct", "říkat",
    "dělat", "udělat", "vidět", "uvidět", "myslet", "pomyslet", "jít", "přijít",
    "odejít", "jet", "přijet", "odjet", "brát", "vzít", "dávat", "dát", "rozumět",
    "porozumět", "čekat", "počkat", "ptát", "zeptat", "odpovídat", "odpovědět",
    "hledat", "najít", "pracovat", "učit", "pamatovat", "zapomenout", "muset",
    "žít", "milovat", "číst", "přečíst", "psát", "napsat", "pít", "vypít", "jíst",
    "sníst", "spát", "kupovat", "koupit", "prodávat", "prodat", "potkat", "začínat",
    "začít", "končit", "skončit", "otevírat", "otevřít", "zavírat", "zavřít",
    "poslouchat", "slyšet", "dívat", "podívat", "pomáhat", "pomoct", "hrát",
    "cestovat", "bydlet", "stát", "platit", "zaplatit", "cítit", "poděkovat",
    "omluvit", "prosit", "poprosit", "vracet", "vrátit", "zůstávat", "zůstat",
    "potřebovat", "bát", "těšit", "sedět", "sednout", "ležet", "běhat", "běžet",
    "chodit", "plavat", "jezdit", "vařit", "ukázat", "ukazovat", "ztratit",
    "ztrácet", "zavolat", "volat"
]

CANONICAL_VERBS = {
    "být": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "jsem", "ty": "jsi", "on": "je", "my": "jsme", "vy": "jste", "oni": "jsou" },
        "indicativo.minuly": {
            "on": "byl", "ona": "byla", "ono": "bylo",
            "oni_anim": "byli", "ony_inanim": "byly", "ona_neut": "byla"
        },
        "indicativo.budouci": { "ja": "budu", "ty": "budeš", "on": "bude", "my": "budeme", "vy": "budete", "oni": "budou" },
        "podminovaci": { "ja": "byl bych", "ty": "byl bys", "on": "byl by", "my": "byli bychom", "vy": "byli byste", "oni": "byli by" },
        "rozkazovaci": { "ty": "buď", "my": "buďme", "vy": "buďte" }
    },
    "mít": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "mám", "ty": "máš", "on": "má", "my": "máme", "vy": "máte", "oni": "mají" },
        "indicativo.minuly": {
            "on": "měl", "ona": "měla", "ono": "mělo",
            "oni_anim": "měli", "ony_inanim": "měly", "ona_neut": "měla"
        },
        "indicativo.budouci": { "ja": "budu mít", "ty": "budeš mít", "on": "bude mít", "my": "budeme mít", "vy": "budete mít", "oni": "budou mít" },
        "podminovaci": { "ja": "měl bych", "ty": "měl bys", "on": "měl by", "my": "měli bychom", "vy": "měli byste", "oni": "měli by" },
        "rozkazovaci": { "ty": "měj", "my": "mějme", "vy": "mějte" }
    },
    "moct": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "můžu", "ty": "můžeš", "on": "může", "my": "můžeme", "vy": "můžete", "oni": "můžou" },
        "indicativo.minuly": {
            "on": "mohl", "ona": "mohla", "ono": "mohlo",
            "oni_anim": "mohli", "ony_inanim": "mohly", "ona_neut": "mohla"
        },
        "indicativo.budouci": { "ja": "budu moct", "ty": "budeš moct", "on": "bude moct", "my": "budeme moct", "vy": "budete moct", "oni": "budou moct" },
        "podminovaci": { "ja": "mohl bych", "ty": "mohl bys", "on": "mohl by", "my": "mohli bychom", "vy": "mohli byste", "oni": "mohli by" },
        "rozkazovaci": {}
    },
    "chtít": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "chci", "ty": "chceš", "on": "chce", "my": "chceme", "vy": "chcete", "oni": "chtějí" },
        "indicativo.minuly": {
            "on": "chtěl", "ona": "chtěla", "ono": "chtělo",
            "oni_anim": "chtěli", "ony_inanim": "chtěly", "ona_neut": "chtěla"
        },
        "indicativo.budouci": { "ja": "budu chtít", "ty": "budeš chtít", "on": "bude chtít", "my": "budeme chtít", "vy": "budete chtít", "oni": "budou chtít" },
        "podminovaci": { "ja": "chtěl bych", "ty": "chtěl bys", "on": "chtěl by", "my": "chtěli bychom", "vy": "chtěli byste", "oni": "chtěli by" },
        "rozkazovaci": { "ty": "chtěj", "my": "chtějme", "vy": "chtějte" }
    },
    "vědět": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "vím", "ty": "víš", "on": "ví", "my": "víme", "vy": "víte", "oni": "vědí" },
        "indicativo.minuly": {
            "on": "věděl", "ona": "věděla", "ono": "vědělo",
            "oni_anim": "věděli", "ony_inanim": "věděly", "ona_neut": "věděla"
        },
        "indicativo.budouci": { "ja": "budu vědět", "ty": "budeš vědět", "on": "bude vědět", "my": "budeme vědět", "vy": "budete vědět", "oni": "budou vědět" },
        "podminovaci": { "ja": "věděl bych", "ty": "věděl bys", "on": "věděl by", "my": "věděli bychom", "vy": "věděli byste", "oni": "věděli by" },
        "rozkazovaci": { "ty": "věz", "my": "vězme", "vy": "vězte" }
    },
    "jít": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "jdu", "ty": "jdeš", "on": "jde", "my": "jdeme", "vy": "jdete", "oni": "jdou" },
        "indicativo.minuly": {
            "on": "šel", "ona": "šla", "ono": "šlo",
            "oni_anim": "šli", "ony_inanim": "šly", "ona_neut": "šla"
        },
        "indicativo.budouci": { "ja": "půjdu", "ty": "půjdeš", "on": "půjde", "my": "půjdeme", "vy": "půjdete", "oni": "půjdou" },
        "podminovaci": { "ja": "šel bych", "ty": "šel bys", "on": "šel by", "my": "šli bychom", "vy": "šli byste", "oni": "šli by" },
        "rozkazovaci": { "ty": "jdi", "my": "jděme", "vy": "jděte" }
    },
    "jet": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "jedu", "ty": "jedeš", "on": "jede", "my": "jedeme", "vy": "jedete", "oni": "jedou" },
        "indicativo.minuly": {
            "on": "jel", "ona": "jela", "ono": "jelo",
            "oni_anim": "jeli", "ony_inanim": "jely", "ona_neut": "jela"
        },
        "indicativo.budouci": { "ja": "pojedu", "ty": "pojedeš", "on": "pojede", "my": "pojedeme", "vy": "pojedete", "oni": "pojedou" },
        "podminovaci": { "ja": "jel bych", "ty": "jel bys", "on": "jel by", "my": "jeli bychom", "vy": "jeli byste", "oni": "jeli by" },
        "rozkazovaci": { "ty": "jeď", "my": "jeďme", "vy": "jeďte" }
    },
    "dělat": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "dělám", "ty": "děláš", "on": "dělá", "my": "děláme", "vy": "děláte", "oni": "dělají" },
        "indicativo.minuly": {
            "on": "dělal", "ona": "dělala", "ono": "dělalo",
            "oni_anim": "dělali", "ony_inanim": "dělaly", "ona_neut": "dělala"
        },
        "indicativo.budouci": { "ja": "budu dělat", "ty": "budeš dělat", "on": "bude dělat", "my": "budeme dělat", "vy": "budete dělat", "oni": "budou dělat" },
        "podminovaci": { "ja": "dělal bych", "ty": "dělal bys", "on": "dělal by", "my": "dělali bychom", "vy": "dělali byste", "oni": "dělali by" },
        "rozkazovaci": { "ty": "dělej", "my": "dělejme", "vy": "dělejte" }
    },
    "udělat": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "udělám", "ty": "uděláš", "on": "udělá", "my": "uděláme", "vy": "uděláte", "oni": "udělají" },
        "indicativo.minuly": {
            "on": "udělal", "ona": "udělala", "ono": "udělalo",
            "oni_anim": "udělali", "ony_inanim": "udělaly", "ona_neut": "udělala"
        },
        "indicativo.budouci": { "ja": "udělám", "ty": "uděláš", "on": "udělá", "my": "uděláme", "vy": "uděláte", "oni": "udělají" },
        "podminovaci": { "ja": "udělal bych", "ty": "udělal bys", "on": "udělal by", "my": "udělali bychom", "vy": "udělali byste", "oni": "udělali by" },
        "rozkazovaci": { "ty": "udělej", "my": "udělejme", "vy": "udělejte" }
    },
    "říct": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "řeknu", "ty": "řekneš", "on": "řekne", "my": "řekneme", "vy": "řeknete", "oni": "řeknou" },
        "indicativo.minuly": {
            "on": "řekl", "ona": "řekla", "ono": "řeklo",
            "oni_anim": "řekli", "ony_inanim": "řekly", "ona_neut": "řekla"
        },
        "indicativo.budouci": { "ja": "řeknu", "ty": "řekneš", "on": "řekne", "my": "řekneme", "vy": "řeknete", "oni": "řeknou" },
        "podminovaci": { "ja": "řekl bych", "ty": "řekl bys", "on": "řekl by", "my": "řekli bychom", "vy": "řekli byste", "oni": "řekli by" },
        "rozkazovaci": { "ty": "řekni", "my": "řekněme", "vy": "řekněte" }
    },
    "říkat": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "říkám", "ty": "říkáš", "on": "říká", "my": "říkáme", "vy": "říkáte", "oni": "říkají" },
        "indicativo.minuly": {
            "on": "říkal", "ona": "říkala", "ono": "říkalo",
            "oni_anim": "říkali", "ony_inanim": "říkaly", "ona_neut": "říkala"
        },
        "indicativo.budouci": { "ja": "budu říkat", "ty": "budeš říkat", "on": "bude říkat", "my": "budeme říkat", "vy": "budete říkat", "oni": "budou říkat" },
        "podminovaci": { "ja": "říkal bych", "ty": "říkal bys", "on": "říkal by", "my": "říkali bychom", "vy": "říkali byste", "oni": "říkali by" },
        "rozkazovaci": { "ty": "říkej", "my": "říkejme", "vy": "říkejte" }
    },
    "psát": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "píšu", "ty": "píšeš", "on": "píše", "my": "píšeme", "vy": "píšete", "oni": "píšou" },
        "indicativo.minuly": {
            "on": "psal", "ona": "psala", "ono": "psalo",
            "oni_anim": "psali", "ony_inanim": "psaly", "ona_neut": "psala"
        },
        "indicativo.budouci": { "ja": "budu psát", "ty": "budeš psát", "on": "bude psát", "my": "budeme psát", "vy": "budete psát", "oni": "budou psát" },
        "podminovaci": { "ja": "psal bych", "ty": "psal bys", "on": "psal by", "my": "psali bychom", "vy": "psali byste", "oni": "psali by" },
        "rozkazovaci": { "ty": "piš", "my": "pišme", "vy": "pište" }
    },
    "číst": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "čtu", "ty": "čteš", "on": "čte", "my": "čteme", "vy": "čtete", "oni": "čtou" },
        "indicativo.minuly": {
            "on": "četl", "ona": "četla", "ono": "četlo",
            "oni_anim": "četli", "ony_inanim": "četly", "ona_neut": "četla"
        },
        "indicativo.budouci": { "ja": "budu číst", "ty": "budeš číst", "on": "bude číst", "my": "budeme číst", "vy": "budete číst", "oni": "budou číst" },
        "podminovaci": { "ja": "četl bych", "ty": "četl bys", "on": "četl by", "my": "četli bychom", "vy": "četli byste", "oni": "četli by" },
        "rozkazovaci": { "ty": "čti", "my": "čtěme", "vy": "čtěte" }
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
        urllib.request.urlretrieve(FREQ_URL, FREQ_FILE)
        print(f"Saved frequency list to {FREQ_FILE}")
    else:
        print(f"Frequency list already cached at {FREQ_FILE}")

    if not KAIKKI_FILE.exists():
        print(f"Downloading Kaikki Czech dictionary extract from {KAIKKI_URL}...")
        urllib.request.urlretrieve(KAIKKI_URL, KAIKKI_FILE)
        print(f"Saved Kaikki Czech dictionary to {KAIKKI_FILE}")
    else:
        print(f"Kaikki Czech extract already cached at {KAIKKI_FILE}")

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

CS_VERB_EN_OVERRIDES = {
    "být": "to be",
    "mít": "to have",
    "brát": "to take",
    "začínat": "to begin, to start",
    "zůstávat": "to stay, to remain",
    "stát": "to stand; to cost",
    "bát": "to fear, to be afraid",
    "dostat": "to get, to receive",
    "držet": "to hold, to keep",
}

def clean_cs_verb_en(lemma, raw_en):
    if lemma in CS_VERB_EN_OVERRIDES:
        return CS_VERB_EN_OVERRIDES[lemma]
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

def build_verb_payload(lemma, forms_dict, aspect_found="imperfective", en_gloss=""):
    aspect = aspect_found or "imperfective"
    pres = dict(forms_dict.get("indicativo.presente", {}))
    past = dict(forms_dict.get("indicativo.minuly", {}))
    fut = dict(forms_dict.get("indicativo.budouci", {}))
    cond = dict(forms_dict.get("podminovaci", {}))
    imperative = dict(forms_dict.get("rozkazovaci", {}))

    # Synthesize compound future for imperfective verbs, or mirror present for perfective
    if aspect == "perfective":
        if not fut:
            fut = dict(pres)
    elif not fut:
        fut = {
            "ja": f"budu {lemma}",
            "ty": f"budeš {lemma}",
            "on": f"bude {lemma}",
            "my": f"budeme {lemma}",
            "vy": f"budete {lemma}",
            "oni": f"budou {lemma}"
        }

    # Synthesize conditional from L-participle if missing
    if not cond and past.get("on") and past.get("oni_anim"):
        cond = {
            "ja": f"{past['on']} bych",
            "ty": f"{past['on']} bys",
            "on": f"{past['on']} by",
            "my": f"{past['oni_anim']} bychom",
            "vy": f"{past['oni_anim']} byste",
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

    # Populate VerbsTable/VerbsSpeed defaultPersons ('ja', 'ty', 'my', 'vy', 'oni') on indicativo.minuly
    minuly = indicativo["minuly"]
    on_m = minuly.get("on", "")
    ona_f = minuly.get("ona", "")
    oni_a = minuly.get("oni_anim") or minuly.get("oni", "")
    ony_i = minuly.get("ony_inanim", "")
    if on_m:
        minuly.setdefault("ja", f"{on_m} jsem/{ona_f} jsem" if ona_f and ona_f != on_m else f"{on_m} jsem")
        minuly.setdefault("ty", f"{on_m} jsi/{ona_f} jsi" if ona_f and ona_f != on_m else f"{on_m} jsi")
    if oni_a:
        minuly.setdefault("my", f"{oni_a} jsme/{ony_i} jsme" if ony_i and ony_i != oni_a else f"{oni_a} jsme")
        minuly.setdefault("vy", f"{oni_a} jste/{ony_i} jste" if ony_i and ony_i != oni_a else f"{oni_a} jste")
        minuly.setdefault("oni", oni_a)

    return {
        "regular": lemma not in CANONICAL_VERBS,
        "infinitive": lemma,
        "infinitivo": lemma,
        "aspect": aspect,
        "english": {
            "infinitivo": clean_cs_verb_en(lemma, en_gloss)
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

    lemma_candidates = defaultdict(lambda: defaultdict(lambda: {"senses": [], "gender": None, "aspect": None, "deprioritised": True}))
    word_index = defaultdict(list)
    verb_index = defaultdict(list)
    verb_data = defaultdict(lambda: {"forms": defaultdict(dict), "aspect": None})
    verb_glosses = {}

    if KAIKKI_FILE.exists():
        print(f"Parsing Kaikki Czech extract from {KAIKKI_FILE}...")
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
                                if not ((item_tags | stags) & DEPRIORITISE_TAGS):
                                    cand["deprioritised"] = False

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
                                if tf == "future present":
                                    table_aspect = "perfective"
                                elif tf == "future":
                                    table_aspect = "imperfective"
                                break
                        if not table_aspect:
                            for fi in forms:
                                ft = set(fi.get("tags") or [])
                                if ft == {"perfective"}:
                                    table_aspect = "imperfective"
                                    break
                                elif ft == {"imperfective"}:
                                    table_aspect = "perfective"
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

                            if "colloquial" in ftags:
                                continue

                            # Extract person/tense forms for verb library
                            if "present" in ftags and "indicative" in ftags and "imperative" not in ftags:
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
                                    if table_aspect == "perfective":
                                        verb_data[word]["forms"]["indicativo.budouci"].setdefault(pslot, form)

                            if ("past" in ftags or "participle" in ftags) and "passive" not in ftags and "adjectival" not in ftags and "transgressive" not in ftags:
                                if "masculine" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("on", form)
                                elif "feminine" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("ona", form)
                                elif "neuter" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("ono", form)
                                elif "masculine" in ftags and "plural" in ftags:
                                    if "inanimate" in ftags and "animate" not in ftags:
                                        verb_data[word]["forms"]["indicativo.minuly"].setdefault("ony_inanim", form)
                                    else:
                                        verb_data[word]["forms"]["indicativo.minuly"].setdefault("oni_anim", form)
                                elif "feminine" in ftags and "plural" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"].setdefault("ony_inanim", form)

                            if "imperative" in ftags:
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
            entry = {"en": ", ".join(info["senses"][:3]), "type": best_pos}
            if info["gender"]:
                entry["gender"] = info["gender"]
            if info["aspect"]:
                entry["aspect"] = info["aspect"]
            dictionary[word] = entry

        FOUNDATIONAL_DICT = {
        "to": {"en": "it, this, that", "type": "pronoun"},
        "je": {"en": "is (3rd sg); them", "type": "verb"},
        "si": {"en": "oneself (reflexive dative)", "type": "pronoun"},
        "jsem": {"en": "I am (1st sg of být)", "type": "verb"},
        "jsi": {"en": "you are (2nd sg of být)", "type": "verb"},
        "jsme": {"en": "we are (1st pl of být)", "type": "verb"},
        "jste": {"en": "you are (2nd pl of být)", "type": "verb"},
        "jsou": {"en": "they are (3rd pl of být)", "type": "verb"},
        "není": {"en": "is not", "type": "verb"},
        "tady": {"en": "here", "type": "adverb"},
        "tak": {"en": "so, thus, like this", "type": "adverb"},
        "už": {"en": "already, anymore", "type": "adverb"},
        "tohle": {"en": "this (here)", "type": "pronoun"},
        "co": {"en": "what", "type": "pronoun"},
        "že": {"en": "that (conjunction)", "type": "conjunction"}
        }
        for k, v in FOUNDATIONAL_DICT.items():
            if k not in dictionary:
                dictionary[k] = v

        # Merge curated additions
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

    # Build verb catalog (only genuine infinitives with verb tables)
    print("Generating verb library...")
    BAD_CS_VERB_FORMS = {"bejt", "pět", "je", "jsem", "jsi", "jsme", "jsou", "jste", "není"}
    all_verbs_set = set(PRIORITY_VERBS)
    for w in freq_list:
        if len(all_verbs_set) >= 120:
            break
        if w in BAD_CS_VERB_FORMS:
            continue
        if w in dictionary and dictionary[w].get("type") == "verb" and w.endswith(("t", "ci")) and w in verb_data and verb_data[w]["forms"]:
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

    # Save verb-list-cs.js
    with open(VERB_LIST_OUTPUT, "w", encoding="utf-8") as f:
        f.write("// Czech Verb Catalog for Verb Practice Driller\n")
        f.write("const ALL_CZECH_VERBS = [\n")
        for i, v in enumerate(final_verb_list):
            comma = "," if i < len(final_verb_list) - 1 else ""
            f.write(f"    '{v}'{comma}\n")
        f.write("];\n\n")
        f.write("if (typeof window !== 'undefined') {\n")
        f.write("    window.ALL_CZECH_VERBS = ALL_CZECH_VERBS;\n")
        f.write("}\n")
        f.write("if (typeof global !== 'undefined') {\n")
        f.write("    global.ALL_CZECH_VERBS = ALL_CZECH_VERBS;\n")
        f.write("}\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("    module.exports = ALL_CZECH_VERBS;\n")
        f.write("}\n")
    print(f"Saved {VERB_LIST_OUTPUT} with {len(final_verb_list)} verbs.")

if __name__ == "__main__":
    process_all()
