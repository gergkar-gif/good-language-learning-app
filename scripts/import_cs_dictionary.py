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
    "proper noun": "proper noun",
    "name": "proper noun",
    "particle": "particle"
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
            "ja": f"budu {lemma}",
            "ty": f"budeš {lemma}",
            "on": f"bude {lemma}",
            "my": f"budeme {lemma}",
            "vy": f"budete {lemma}",
            "oni": f"budou {lemma}"
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
                                elif "masculine" in ftags and "plural" in ftags:
                                    verb_data[word]["forms"]["indicativo.minuly"]["oni_anim"] = form
                                elif "feminine" in ftags and "plural" in ftags:
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
