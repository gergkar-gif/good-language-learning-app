#!/usr/bin/env python3
"""
Import comprehensive Italian-English dictionary, morphology indexes, and verb library
from Kaikki.org (Wiktionary extract) and HermitDave OpenSubtitles Frequency list.

Attribution & Licensing:
- Kaikki.org / Wiktionary: CC BY-SA 3.0 & GFDL (Tatu Ylonen / Wiktionary contributors)
- HermitDave FrequencyWords: CC BY-SA 3.0 (HermitDave / OpenSubtitles)

Outputs:
  imports/dictionary/italian-en.json
  content/it/indexes/word-index.json
  content/it/indexes/verb-index.json
  content/it/indexes/frequency.json
  imports/verbs/it/<lemma>.json (Conjugation tables for top verbs)
  imports/verbs/it/verb-list-it.js (ALL_ITALIAN_VERBS list)
"""
import gzip
import json
import os
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

KAIKKI_URL = "https://kaikki.org/dictionary/Italian/kaikki.org-dictionary-Italian.jsonl.gz"
FREQ_URL = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/it/it_50k.txt"

CACHE_DIR = Path("imports/dictionary")
KAIKKI_FILE = CACHE_DIR / "kaikki-it.jsonl.gz"
FREQ_FILE = CACHE_DIR / "frequency-it.txt"
ADDITIONS_FILE = CACHE_DIR / "additions-it.json"

DICT_OUTPUT = CACHE_DIR / "italian-en.json"
WORD_INDEX_OUTPUT = Path("content/it/indexes/word-index.json")
VERB_INDEX_OUTPUT = Path("content/it/indexes/verb-index.json")
FREQUENCY_OUTPUT = Path("content/it/indexes/frequency.json")
VERBS_DIR = Path("imports/verbs/it")
VERB_LIST_OUTPUT = VERBS_DIR / "verb-list-it.js"

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
    "art": "article",
    "article": "article",
    "num": "numeral",
    "numeral": "numeral",
    "interj": "interjection",
    "proper noun": "proper noun",
    "name": "proper noun",
    "particle": "particle"
}

PERSON_MAP = {
    "first-person": "1s",
    "second-person": "2s",
    "third-person": "3s"
}

def download():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not FREQ_FILE.exists():
        print(f"Downloading Italian frequency list from {FREQ_URL} ...")
        req = urllib.request.Request(FREQ_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            FREQ_FILE.write_bytes(resp.read())
        print(f"Downloaded {FREQ_FILE.stat().st_size:,} bytes")
    else:
        print(f"Using cached {FREQ_FILE}")

    if not KAIKKI_FILE.exists():
        print(f"Downloading Kaikki Italian JSONL.gz from {KAIKKI_URL} (~75MB) ...")
        req = urllib.request.Request(KAIKKI_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            KAIKKI_FILE.write_bytes(resp.read())
        print(f"Downloaded {KAIKKI_FILE.stat().st_size:,} bytes")
    else:
        print(f"Using cached {KAIKKI_FILE}")

FORM_RE = re.compile(
    r'^(?:(?:first|second|third)-person|(?:singular|plural) of|inflection of|past participle of|present participle of|gerund of|feminine (?:plural|singular) of|masculine plural of|alternative (?:form|spelling) of|obsolete (?:form|spelling) of)\b',
    re.I
)
DEPRIORITISE_TAGS = {'obsolete', 'archaic', 'dated', 'rare', 'poetic', 'heraldry', 'dialectal'}
HERALDRY_RE = re.compile(r'\b(?:per pale|divided into two equal parts vertically|fess|chevron|tincture|coat of arms)\b', re.I)

POS_PRIORITY = {
    'verb': 1, 'noun': 2, 'adjective': 3, 'adverb': 4, 'preposition': 5,
    'conjunction': 6, 'pronoun': 7, 'determiner': 8, 'article': 9, 'numeral': 10, 'interjection': 11
}

GLOSS_OVERRIDES = {
    'partito': {'en': 'party, political party', 'type': 'noun', 'gender': 'm'},
    'grande': {'en': 'big, large; tall', 'type': 'adjective', 'gender': None},
    'stato': {'en': 'state; status', 'type': 'noun', 'gender': 'm'},
    'governo': {'en': 'government, administration', 'type': 'noun', 'gender': 'm'},
    'politica': {'en': 'politics; policy', 'type': 'noun', 'gender': 'f'},
    'fronte': {'en': 'front; forehead, brow', 'type': 'noun', 'gender': 'f'},
    'camera': {'en': 'room; chamber, house', 'type': 'noun', 'gender': 'f'},
    'legge': {'en': 'law, statute', 'type': 'noun', 'gender': 'f'},
    'caso': {'en': 'case; chance, coincidence', 'type': 'noun', 'gender': 'm'},
    'tempo': {'en': 'time; weather', 'type': 'noun', 'gender': 'm'},
    'piano': {'en': 'plan, project; floor; slow, flat', 'type': 'noun', 'gender': 'm'},
    'bene': {'en': 'well, good; goods, property', 'type': 'adverb', 'gender': 'm'},
    'forza': {'en': 'strength, force, power', 'type': 'noun', 'gender': 'f'},
    'modo': {'en': 'way, manner', 'type': 'noun', 'gender': 'm'},
    'parte': {'en': 'part, portion; side', 'type': 'noun', 'gender': 'f'},
    'punto': {'en': 'point, spot; full stop', 'type': 'noun', 'gender': 'm'},
    'fine': {'en': 'end; aim, purpose', 'type': 'noun', 'gender': 'm'},
    'storia': {'en': 'story; history', 'type': 'noun', 'gender': 'f'},
    'cittadino': {'en': 'citizen; civic', 'type': 'noun', 'gender': 'm'},
    'svolta': {'en': 'turn, curve; turning point', 'type': 'noun', 'gender': 'f'},
    'elezione': {'en': 'election; choice', 'type': 'noun', 'gender': 'f'},
    'riforma': {'en': 'reform', 'type': 'noun', 'gender': 'f'},
    'avere': {'en': 'to have', 'type': 'verb', 'gender': None},
    'essere': {'en': 'to be', 'type': 'verb', 'gender': None},
    'andare': {'en': 'to go', 'type': 'verb', 'gender': None},
    'fare': {'en': 'to do, to make', 'type': 'verb', 'gender': None},
    'potere': {'en': 'can, to be able to', 'type': 'verb', 'gender': None},
    'volere': {'en': 'to want', 'type': 'verb', 'gender': None},
    'dovere': {'en': 'must, to have to', 'type': 'verb', 'gender': None},
    'sapere': {'en': 'to know', 'type': 'verb', 'gender': None},
    'dire': {'en': 'to say, to tell', 'type': 'verb', 'gender': None},
    'venire': {'en': 'to come', 'type': 'verb', 'gender': None},
    'stare': {'en': 'to stay, to remain; to be', 'type': 'verb', 'gender': None},
    'dare': {'en': 'to give', 'type': 'verb', 'gender': None},
    'vedere': {'en': 'to see', 'type': 'verb', 'gender': None},
    'parlare': {'en': 'to speak, to talk', 'type': 'verb', 'gender': None},
    'prendere': {'en': 'to take, to catch', 'type': 'verb', 'gender': None},
    'trovare': {'en': 'to find', 'type': 'verb', 'gender': None},
    'sentire': {'en': 'to hear, to feel', 'type': 'verb', 'gender': None},
    'pensare': {'en': 'to think', 'type': 'verb', 'gender': None},
    'mettere': {'en': 'to put, to place', 'type': 'verb', 'gender': None},
    'portare': {'en': 'to bring, to carry', 'type': 'verb', 'gender': None},
    'uscire': {'en': 'to go out, to exit', 'type': 'verb', 'gender': None},
    'chiamare': {'en': 'to call', 'type': 'verb', 'gender': None},
    'credere': {'en': 'to believe', 'type': 'verb', 'gender': None},
    'vivere': {'en': 'to live', 'type': 'verb', 'gender': None},
    'lasciare': {'en': 'to leave, to let', 'type': 'verb', 'gender': None},
    'chiedere': {'en': 'to ask', 'type': 'verb', 'gender': None},
    'capire': {'en': 'to understand', 'type': 'verb', 'gender': None},
    'partire': {'en': 'to leave, to depart', 'type': 'verb', 'gender': None}
}

def clean_gloss(text):
    if not text:
        return ""
    text = re.sub(r'\(.*?\)', '', text)  # remove parentheticals
    text = re.sub(r'\[.*?\]', '', text)  # remove bracketed tags
    text = re.sub(r'See Category:.*', '', text, flags=re.I)
    text = re.sub(r'See also:.*', '', text, flags=re.I)
    text = re.sub(r'^of greater physical dimensions or numerosity;?\s*', '', text, flags=re.I)
    text = re.sub(r'\s+', ' ', text).strip(' ,;:')
    if HERALDRY_RE.search(text):
        return ""
    # Cap comma-separated synonyms to at most 3
    parts = [p.strip() for p in text.split(',') if p.strip()]
    if len(parts) > 3:
        text = ', '.join(parts[:3])
    return text

def parse_frequency():
    freq_rank = {}
    ordered_lemmas = []
    if FREQ_FILE.exists():
        with open(FREQ_FILE, "r", encoding="utf-8", errors="ignore") as f:
            rank = 1
            for line in f:
                parts = line.strip().split()
                if parts:
                    word = parts[0].lower()
                    if word not in freq_rank:
                        freq_rank[word] = rank
                        ordered_lemmas.append(word)
                        rank += 1
    return freq_rank, ordered_lemmas

# Essential verbs with essere as auxiliary in compound tenses
ESSERE_VERBS = {
    "essere", "andare", "venire", "arrivare", "partire", "entrare", "uscire",
    "salire", "scendere", "tornare", "ritornare", "restare", "rimanere",
    "stare", "morire", "nascere", "diventare", "cadere", "succedere", "sembrare"
}

ESSERE_PRES = { "io": "sono", "tu": "sei", "lui": "è", "noi": "siamo", "voi": "siete", "loro": "sono" }
AVERE_PRES  = { "io": "ho",   "tu": "hai", "lui": "ha", "noi": "abbiamo", "voi": "avete", "loro": "hanno" }

ESSERE_IMP = { "io": "ero", "tu": "eri", "lui": "era", "noi": "eravamo", "voi": "eravate", "loro": "erano" }
AVERE_IMP  = { "io": "avevo", "tu": "avevi", "lui": "aveva", "noi": "avevamo", "voi": "avevate", "loro": "avevano" }

def strip_internal_accents(s: str) -> str:
    if not s or len(s) <= 1:
        return s
    accent_map = {'à': 'a', 'è': 'e', 'é': 'e', 'ì': 'i', 'ò': 'o', 'ó': 'o', 'ù': 'u'}
    chars = list(s)
    for i in range(len(chars) - 1):
        chars[i] = accent_map.get(chars[i], chars[i])
    return "".join(chars)

CANONICAL_VERBS = {
    "essere": {
        "indicativo.presente": { "io": "sono", "tu": "sei", "lui": "è", "noi": "siamo", "voi": "siete", "loro": "sono" },
        "indicativo.imperfetto": { "io": "ero", "tu": "eri", "lui": "era", "noi": "eravamo", "voi": "eravate", "loro": "erano" },
        "indicativo.futuro_semplice": { "io": "sarò", "tu": "sarai", "lui": "sarà", "noi": "saremo", "voi": "sarete", "loro": "saranno" },
        "condizionale.presente": { "io": "sarei", "tu": "saresti", "lui": "sarebbe", "noi": "saremmo", "voi": "sareste", "loro": "sarebbero" },
        "congiuntivo.presente": { "io": "sia", "tu": "sia", "lui": "sia", "noi": "siamo", "voi": "siate", "loro": "siano" },
        "congiuntivo.imperfetto": { "io": "fossi", "tu": "fossi", "lui": "fosse", "noi": "fossimo", "voi": "foste", "loro": "fossero" },
        "indicativo.passato_remoto": { "io": "fui", "tu": "fosti", "lui": "fu", "noi": "fummo", "voi": "foste", "loro": "furono" },
        "gerundio": "essendo",
        "participioPassato": "stato"
    },
    "avere": {
        "indicativo.presente": { "io": "ho", "tu": "hai", "lui": "ha", "noi": "abbiamo", "voi": "avete", "loro": "hanno" },
        "indicativo.imperfetto": { "io": "avevo", "tu": "avevi", "lui": "aveva", "noi": "avevamo", "voi": "avevate", "loro": "avevano" },
        "indicativo.futuro_semplice": { "io": "avrò", "tu": "avrai", "lui": "avrà", "noi": "avremo", "voi": "avrete", "loro": "avranno" },
        "condizionale.presente": { "io": "avrei", "tu": "avresti", "lui": "avrebbe", "noi": "avremmo", "voi": "avreste", "loro": "avrebbero" },
        "congiuntivo.presente": { "io": "abbia", "tu": "abbia", "lui": "abbia", "noi": "abbiamo", "voi": "abbiate", "loro": "abbiano" },
        "congiuntivo.imperfetto": { "io": "avessi", "tu": "avessi", "lui": "avesse", "noi": "avessimo", "voi": "aveste", "loro": "avessero" },
        "indicativo.passato_remoto": { "io": "ebbi", "tu": "avesti", "lui": "ebbe", "noi": "avemmo", "voi": "aveste", "loro": "ebbero" },
        "gerundio": "avendo",
        "participioPassato": "avuto"
    },
    "andare": {
        "indicativo.presente": { "io": "vado", "tu": "vai", "lui": "va", "noi": "andiamo", "voi": "andate", "loro": "vanno" },
        "indicativo.imperfetto": { "io": "andavo", "tu": "andavi", "lui": "andava", "noi": "andavamo", "voi": "andavate", "loro": "andavano" },
        "indicativo.futuro_semplice": { "io": "andrò", "tu": "andrai", "lui": "andrà", "noi": "andremo", "voi": "andrete", "loro": "andranno" },
        "condizionale.presente": { "io": "andrei", "tu": "andresti", "lui": "andrebbe", "noi": "andremmo", "voi": "andreste", "loro": "andrebbero" },
        "congiuntivo.presente": { "io": "vada", "tu": "vada", "lui": "vada", "noi": "andiamo", "voi": "andiate", "loro": "vadano" },
        "congiuntivo.imperfetto": { "io": "andassi", "tu": "andassi", "lui": "andasse", "noi": "andassimo", "voi": "andaste", "loro": "andassero" },
        "indicativo.passato_remoto": { "io": "andai", "tu": "andasti", "lui": "andò", "noi": "andammo", "voi": "andaste", "loro": "andarono" },
        "gerundio": "andando",
        "participioPassato": "andato"
    },
    "fare": {
        "indicativo.presente": { "io": "faccio", "tu": "fai", "lui": "fa", "noi": "facciamo", "voi": "fate", "loro": "fanno" },
        "indicativo.imperfetto": { "io": "facevo", "tu": "facevi", "lui": "faceva", "noi": "facevamo", "voi": "facevate", "loro": "facevano" },
        "indicativo.futuro_semplice": { "io": "farò", "tu": "farai", "lui": "farà", "noi": "faremo", "voi": "farete", "loro": "faranno" },
        "condizionale.presente": { "io": "farei", "tu": "faresti", "lui": "farebbe", "noi": "faremmo", "voi": "fareste", "loro": "farebbero" },
        "congiuntivo.presente": { "io": "faccia", "tu": "faccia", "lui": "faccia", "noi": "facciamo", "voi": "facciate", "loro": "facciano" },
        "congiuntivo.imperfetto": { "io": "facessi", "tu": "facessi", "lui": "facesse", "noi": "facessimo", "voi": "faceste", "loro": "facessero" },
        "indicativo.passato_remoto": { "io": "feci", "tu": "facesti", "lui": "fece", "noi": "facemmo", "voi": "faceste", "loro": "fecero" },
        "gerundio": "facendo",
        "participioPassato": "fatto"
    }
}

def process_all():
    download()
    freq_rank, freq_list = parse_frequency()

    WORD_INDEX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    VERBS_DIR.mkdir(parents=True, exist_ok=True)

    dictionary = {}
    lemma_candidates = defaultdict(lambda: defaultdict(lambda: {"senses": [], "gender": None, "deprioritised": True}))
    word_index = defaultdict(list)
    verb_index = defaultdict(list)
    verb_data = defaultdict(lambda: {
        "forms": defaultdict(dict),
        "participioPassato": None,
        "gerundio": None,
        "auxiliaire": "avere"
    })

    print("Parsing Kaikki Italian extract...")
    with gzip.open(KAIKKI_FILE, "rt", encoding="utf-8", errors="ignore") as f:
        count = 0
        for line in f:
            count += 1
            if count % 50000 == 0:
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

            # Only harvest dictionary glosses for genuine headwords (skip form-of entries)
            if word and mapped_pos in POS_MAP and 'form-of' not in item_tags:
                gender = "m" if "masculine" in item_tags else "f" if "feminine" in item_tags else None
                cand = lemma_candidates[word][mapped_pos]
                if gender and not cand["gender"]:
                    cand["gender"] = gender

                for s in senses:
                    stags = set(s.get("tags", []))
                    if 'form-of' in stags:
                        continue
                    gloss_list = s.get("glosses", [])
                    if not gloss_list:
                        continue
                    # Wiktextract puts the specific gloss at the end when taxonomic categories precede it
                    g = gloss_list[-1]
                    if FORM_RE.search(g):
                        continue
                    c = clean_gloss(g)
                    if c and len(c) >= 2 and c not in cand["senses"]:
                        cand["senses"].append(c)
                        is_dep = bool((item_tags | stags) & DEPRIORITISE_TAGS)
                        if not is_dep:
                            cand["deprioritised"] = False

            # Process inflected forms
            forms = item.get("forms", [])
            for form_info in forms:
                form = form_info.get("form", "").strip().lower()
                form_tags = form_info.get("tags", [])
                if not form or form == word:
                    continue

                if mapped_pos == "verb":
                    # Check for mood, tense, person, number
                    mood = None
                    tense = None
                    person = None
                    number = None

                    if "indicative" in form_tags:
                        mood = "indicativo"
                    elif "subjunctive" in form_tags:
                        mood = "congiuntivo"
                    elif "conditional" in form_tags:
                        mood = "condizionale"
                    elif "imperative" in form_tags:
                        mood = "imperativo"

                    if "present" in form_tags:
                        tense = "presente"
                    elif "imperfect" in form_tags:
                        tense = "imperfetto"
                    elif "future" in form_tags:
                        tense = "futuro_semplice"
                    elif "historic" in form_tags or "preterite" in form_tags or "past-historic" in form_tags:
                        tense = "passato_remoto"

                    if "first-person" in form_tags:
                        person = "1"
                    elif "second-person" in form_tags:
                        person = "2"
                    elif "third-person" in form_tags:
                        person = "3"

                    if "singular" in form_tags:
                        number = "singular"
                    elif "plural" in form_tags:
                        number = "plural"

                    clean_form = strip_internal_accents(form)
                    is_nonstandard = any(t in form_tags for t in ["archaic", "obsolete", "dialectal", "regional", "poetic", "literary", "rare"])

                    if mood and tense and person and number:
                        p_key = f"{person}-{number}"
                        entry = {
                            "lemma": word,
                            "mood": mood,
                            "tense": tense,
                            "person": p_key
                        }
                        if entry not in verb_index[form]:
                            verb_index[form].append(entry)
                        if clean_form != form and entry not in verb_index[clean_form]:
                            verb_index[clean_form].append(entry)

                        # Track for standalone verb conjugation tables
                        prn = "io" if p_key == "1-singular" else "tu" if p_key == "2-singular" else "lui" if p_key == "3-singular" else "noi" if p_key == "1-plural" else "voi" if p_key == "2-plural" else "loro"
                        if not is_nonstandard and prn not in verb_data[word]["forms"][f"{mood}.{tense}"]:
                            verb_data[word]["forms"][f"{mood}.{tense}"][prn] = clean_form

                    elif "participle" in form_tags and "past" in form_tags:
                        entry = {"lemma": word, "mood": "participle", "tense": "past"}
                        if entry not in verb_index[form]:
                            verb_index[form].append(entry)
                        if clean_form != form and entry not in verb_index[clean_form]:
                            verb_index[clean_form].append(entry)
                        if not is_nonstandard and not verb_data[word]["participioPassato"]:
                            verb_data[word]["participioPassato"] = clean_form
                    elif "gerund" in form_tags:
                        entry = {"lemma": word, "mood": "gerund"}
                        if entry not in verb_index[form]:
                            verb_index[form].append(entry)
                        if clean_form != form and entry not in verb_index[clean_form]:
                            verb_index[clean_form].append(entry)
                        if not is_nonstandard and not verb_data[word]["gerundio"]:
                            verb_data[word]["gerundio"] = clean_form

                elif mapped_pos in ("noun", "adjective"):
                    gender_str = "masculine" if "masculine" in form_tags else "feminine" if "feminine" in form_tags else None
                    number_str = "singular" if "singular" in form_tags else "plural" if "plural" in form_tags else None
                    entry = {"lemma": word, "pos": mapped_pos}
                    if gender_str:
                        entry["gender"] = gender_str
                    if number_str:
                        entry["number"] = number_str
                    clean_form = strip_internal_accents(form)
                    if entry not in word_index[form]:
                        word_index[form].append(entry)
                    if clean_form != form and entry not in word_index[clean_form]:
                        word_index[clean_form].append(entry)

    # Core Italian grammar tokens guarantee
    CORE_TOKENS = {
        "del": {"en": "of the, some (masculine)", "type": "contraction", "gender": "m"},
        "dello": {"en": "of the, some (masculine before z/s+cons)", "type": "contraction", "gender": "m"},
        "della": {"en": "of the, some (feminine)", "type": "contraction", "gender": "f"},
        "dell'": {"en": "of the, some (before vowel)", "type": "contraction", "gender": None},
        "dei": {"en": "of the, some (masculine plural)", "type": "contraction", "gender": "m"},
        "degli": {"en": "of the, some (masculine plural)", "type": "contraction", "gender": "m"},
        "delle": {"en": "of the, some (feminine plural)", "type": "contraction", "gender": "f"},
        "al": {"en": "to the, at the (masculine)", "type": "contraction", "gender": "m"},
        "allo": {"en": "to the, at the (masculine)", "type": "contraction", "gender": "m"},
        "alla": {"en": "to the, at the (feminine)", "type": "contraction", "gender": "f"},
        "all'": {"en": "to the, at the (before vowel)", "type": "contraction", "gender": None},
        "ai": {"en": "to the, at the (masculine plural)", "type": "contraction", "gender": "m"},
        "agli": {"en": "to the, at the (masculine plural)", "type": "contraction", "gender": "m"},
        "alle": {"en": "to the, at the (feminine plural)", "type": "contraction", "gender": "f"},
        "dal": {"en": "from the, by the (masculine)", "type": "contraction", "gender": "m"},
        "dallo": {"en": "from the, by the", "type": "contraction", "gender": "m"},
        "dalla": {"en": "from the, by the", "type": "contraction", "gender": "f"},
        "dall'": {"en": "from the, by the", "type": "contraction", "gender": None},
        "dai": {"en": "from the, by the (plural)", "type": "contraction", "gender": "m"},
        "dagli": {"en": "from the, by the (plural)", "type": "contraction", "gender": "m"},
        "dalle": {"en": "from the, by the (plural)", "type": "contraction", "gender": "f"},
        "nel": {"en": "in the (masculine)", "type": "contraction", "gender": "m"},
        "nello": {"en": "in the (masculine)", "type": "contraction", "gender": "m"},
        "nella": {"en": "in the (feminine)", "type": "contraction", "gender": "f"},
        "nell'": {"en": "in the (before vowel)", "type": "contraction", "gender": None},
        "nei": {"en": "in the (masculine plural)", "type": "contraction", "gender": "m"},
        "negli": {"en": "in the (masculine plural)", "type": "contraction", "gender": "m"},
        "nelle": {"en": "in the (feminine plural)", "type": "contraction", "gender": "f"},
        "sul": {"en": "on the (masculine)", "type": "contraction", "gender": "m"},
        "sullo": {"en": "on the", "type": "contraction", "gender": "m"},
        "sulla": {"en": "on the (feminine)", "type": "contraction", "gender": "f"},
        "sull'": {"en": "on the (before vowel)", "type": "contraction", "gender": None},
        "sui": {"en": "on the (masculine plural)", "type": "contraction", "gender": "m"},
        "sugli": {"en": "on the (masculine plural)", "type": "contraction", "gender": "m"},
        "sulle": {"en": "on the (feminine plural)", "type": "contraction", "gender": "f"},
        "ci": {"en": "there, us, to us, about it", "type": "pronoun", "gender": None},
        "ne": {"en": "of it, of them, from there", "type": "pronoun", "gender": None},
        "mi": {"en": "me, to me, myself", "type": "pronoun", "gender": None},
        "ti": {"en": "you, to you, yourself", "type": "pronoun", "gender": None},
        "lo": {"en": "him, it (masculine direct object); the", "type": "pronoun", "gender": "m"},
        "la": {"en": "her, it (feminine direct object); the", "type": "pronoun", "gender": "f"},
        "gli": {"en": "to him, to them; the (plural)", "type": "pronoun", "gender": "m"},
        "le": {"en": "to her; the (feminine plural); them", "type": "pronoun", "gender": "f"},
        "vi": {"en": "you (plural), to you; there", "type": "pronoun", "gender": None},
        "li": {"en": "them (masculine direct object)", "type": "pronoun", "gender": "m"},
        "si": {"en": "oneself, himself, herself, themselves", "type": "pronoun", "gender": None},
        "glielo": {"en": "it to him / it to her", "type": "pronoun", "gender": "m"},
        "gliela": {"en": "it to him / it to her", "type": "pronoun", "gender": "f"},
        "glieli": {"en": "them to him / them to her", "type": "pronoun", "gender": "m"},
        "gliele": {"en": "them to him / them to her", "type": "pronoun", "gender": "f"},
        "gliene": {"en": "some of it to him / to her", "type": "pronoun", "gender": None},
        "me lo": {"en": "it to me", "type": "pronoun", "gender": "m"},
        "me la": {"en": "it to me", "type": "pronoun", "gender": "f"},
        "te lo": {"en": "it to you", "type": "pronoun", "gender": "m"},
        "te la": {"en": "it to you", "type": "pronoun", "gender": "f"},
        "se lo": {"en": "it to oneself", "type": "pronoun", "gender": "m"},
        "ce lo": {"en": "it to us", "type": "pronoun", "gender": "m"},
        "ce la": {"en": "it to us", "type": "pronoun", "gender": "f"},
        "ve lo": {"en": "it to you all", "type": "pronoun", "gender": "m"},
        "ve la": {"en": "it to you all", "type": "pronoun", "gender": "f"},
        "c'è": {"en": "there is", "type": "verb", "gender": None},
        "c'era": {"en": "there was", "type": "verb", "gender": None},
        "ci sono": {"en": "there are", "type": "verb", "gender": None},
        "c'erano": {"en": "there were", "type": "verb", "gender": None}
    }

    print(f"Building concise dictionary from {len(lemma_candidates):,} lemma candidates...")
    for word, pos_entries in lemma_candidates.items():
        if word in GLOSS_OVERRIDES:
            dictionary[word] = GLOSS_OVERRIDES[word]
            continue

        valid_pos = {p: info for p, info in pos_entries.items() if info["senses"]}
        if not valid_pos:
            continue

        sorted_pos = sorted(
            valid_pos.keys(),
            key=lambda p: (1 if valid_pos[p]["deprioritised"] else 0, POS_PRIORITY.get(p, 99))
        )
        best_pos = sorted_pos[0]
        best_entry = valid_pos[best_pos]

        # Combine up to 2 distinct concise senses
        def_text = "; ".join(best_entry["senses"][:2])
        if len(def_text) > 60:
            cut = def_text[:60].rfind("; ")
            if cut > 20:
                def_text = def_text[:cut]
            else:
                cut_c = def_text[:60].rfind(", ")
                if cut_c > 20:
                    def_text = def_text[:cut_c]

        dictionary[word] = {
            "en": def_text,
            "type": best_pos,
            "gender": best_entry["gender"]
        }

    for w, entry in CORE_TOKENS.items():
        if w not in dictionary:
            dictionary[w] = entry

    # Merge additions-it.json
    if ADDITIONS_FILE.exists():
        try:
            with open(ADDITIONS_FILE, "r", encoding="utf-8") as f:
                additions = json.load(f)
            for w, val in additions.items():
                if isinstance(val, list) and val:
                    dictionary[w.lower()] = val[0]
                elif isinstance(val, dict):
                    dictionary[w.lower()] = val
            print(f"Merged entries from {ADDITIONS_FILE}")
        except Exception as e:
            print(f"Warning: could not read additions: {e}")

    print(f"Saving Italian dictionary with {len(dictionary):,} entries to {DICT_OUTPUT} ...")
    with open(DICT_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, separators=(',', ':'))
    print(f"Saved {DICT_OUTPUT.stat().st_size:,} bytes")

    print(f"Saving word-index with {len(word_index):,} inflected forms to {WORD_INDEX_OUTPUT} ...")
    with open(WORD_INDEX_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(word_index, f, ensure_ascii=False, separators=(',', ':'))

    print(f"Saving verb-index with {len(verb_index):,} forms to {VERB_INDEX_OUTPUT} ...")
    with open(VERB_INDEX_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(verb_index, f, ensure_ascii=False, separators=(',', ':'))

    print(f"Saving frequency ranking with {len(freq_list):,} lemmas to {FREQUENCY_OUTPUT} ...")
    with open(FREQUENCY_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(freq_list, f, ensure_ascii=False, separators=(',', ':'))

    # Build top verbs for Verbs driller (imports/verbs/it/*.json)
    PRIORITY_VERBS = [
        "essere", "avere", "andare", "fare", "potere", "volere", "dovere", "venire",
        "dire", "sapere", "stare", "dare", "parlare", "vedere", "sentire", "prendere",
        "trovare", "capire", "mettere", "pensare", "portare", "uscire", "credere",
        "vivere", "chiamare", "arrivare", "lasciare", "chiedere", "partire", "finire",
        "mangiare", "bere", "dormire", "leggere", "scrivere", "ascoltare", "aprire",
        "chiudere", "comprare", "vendere", "pagare", "cercare", "perdere", "conoscere",
        "ricordare", "dimenticare", "aspettare", "sperare", "cambiare", "lavorare",
        "studiare", "giocare", "guardare", "aiutare", "amare", "preferire", "scegliere",
        "piacere", "sembrare", "diventare", "rimanere", "restare", "morire", "nascere",
        "passare", "tornare", "entrare", "salire", "scendere", "camminare", "correre"
    ]

    # Add other top verbs present in frequency list
    for w in freq_list:
        if len(PRIORITY_VERBS) >= 120:
            break
        if w in verb_data and (w.endswith("are") or w.endswith("ere") or w.endswith("ire")) and w not in PRIORITY_VERBS:
            PRIORITY_VERBS.append(w)

    print(f"Generating verb files for {len(PRIORITY_VERBS)} Italian verbs...")
    saved_verbs = []
    for lemma in PRIORITY_VERBS:
        v_info = verb_data.get(lemma)
        forms = v_info["forms"] if v_info else {}
        pp = (v_info and v_info.get("participioPassato")) or (
            (lemma[:-3] + "ato") if lemma.endswith("are") else (lemma[:-3] + "uto") if lemma.endswith("ere") else (lemma[:-3] + "ito")
        )
        pp = strip_internal_accents(pp)
        ger = (v_info and v_info.get("gerundio")) or (
            (lemma[:-3] + "ando") if lemma.endswith("are") else (lemma[:-3] + "endo")
        )
        ger = strip_internal_accents(ger)
        aux = "essere" if lemma in ESSERE_VERBS else "avere"
        aux_pres = ESSERE_PRES if aux == "essere" else AVERE_PRES
        aux_imp  = ESSERE_IMP  if aux == "essere" else AVERE_IMP

        # Compose Passato Prossimo & Trapassato Prossimo
        passato_prossimo = {}
        for prn in ("io", "tu", "lui", "noi", "voi", "loro"):
            if aux == "essere":
                part_end = "o/a" if prn in ("io", "tu", "lui") else "i/e"
                stem = pp[:-1] if pp.endswith(("o", "a", "i", "e")) else pp
                passato_prossimo[prn] = f"{aux_pres[prn]} {stem}{part_end}"
            else:
                passato_prossimo[prn] = f"{aux_pres[prn]} {pp}"

        indicativo = {
            "presente": forms.get("indicativo.presente", {}),
            "passato_prossimo": passato_prossimo,
            "imperfetto": forms.get("indicativo.imperfetto", {}),
            "futuro_semplice": forms.get("indicativo.futuro_semplice", {}),
            "condizionale_presente": forms.get("condizionale.presente", {}),
            "passato_remoto": forms.get("indicativo.passato_remoto", {})
        }
        congiuntivo = {
            "presente": forms.get("congiuntivo.presente", {}),
            "imperfetto": forms.get("congiuntivo.imperfetto", {})
        }

        # Apply canonical overrides for core irregular verbs
        if lemma in CANONICAL_VERBS:
            canon = CANONICAL_VERBS[lemma]
            ger = canon.get("gerundio", ger)
            pp = canon.get("participioPassato", pp)
            indicativo["presente"] = canon.get("indicativo.presente", indicativo["presente"])
            indicativo["imperfetto"] = canon.get("indicativo.imperfetto", indicativo["imperfetto"])
            indicativo["futuro_semplice"] = canon.get("indicativo.futuro_semplice", indicativo["futuro_semplice"])
            indicativo["condizionale_presente"] = canon.get("condizionale.presente", indicativo["condizionale_presente"])
            indicativo["passato_remoto"] = canon.get("indicativo.passato_remoto", indicativo["passato_remoto"])
            congiuntivo["presente"] = canon.get("congiuntivo.presente", congiuntivo["presente"])
            congiuntivo["imperfetto"] = canon.get("congiuntivo.imperfetto", congiuntivo["imperfetto"])
            passato_prossimo = {}
            for prn in ("io", "tu", "lui", "noi", "voi", "loro"):
                if aux == "essere":
                    part_end = "o/a" if prn in ("io", "tu", "lui") else "i/e"
                    stem = pp[:-1] if pp.endswith(("o", "a", "i", "e")) else pp
                    passato_prossimo[prn] = f"{aux_pres[prn]} {stem}{part_end}"
                else:
                    passato_prossimo[prn] = f"{aux_pres[prn]} {pp}"
            indicativo["passato_prossimo"] = passato_prossimo

        # Regular endings fallback if any missing
        if not indicativo["presente"]:
            stem = lemma[:-3]
            if lemma.endswith("are"):
                indicativo["presente"] = { "io": stem+"o", "tu": stem+"i", "lui": stem+"a", "noi": stem+"iamo", "voi": stem+"ate", "loro": stem+"ano" }
            elif lemma.endswith("ere"):
                indicativo["presente"] = { "io": stem+"o", "tu": stem+"i", "lui": stem+"e", "noi": stem+"iamo", "voi": stem+"ete", "loro": stem+"ono" }
            elif lemma.endswith("ire"):
                indicativo["presente"] = { "io": stem+"o", "tu": stem+"i", "lui": stem+"e", "noi": stem+"iamo", "voi": stem+"ite", "loro": stem+"ono" }

        verb_file_data = {
            "regular": lemma not in ESSERE_VERBS and not lemma in ("fare", "dare", "stare", "dire", "andare", "potere", "volere", "dovere", "bere", "uscire", "scegliere", "piacere"),
            "infinitivo": lemma,
            "infinitive": lemma,
            "gerundio": ger,
            "participioPasado": pp,
            "participioPassato": pp,
            "auxiliaire": aux,
            "indicativo": indicativo,
            "congiuntivo": congiuntivo,
            "tenses": indicativo
        }

        v_path = VERBS_DIR / f"{lemma}.json"
        with open(v_path, "w", encoding="utf-8") as f:
            json.dump(verb_file_data, f, ensure_ascii=False, indent=2)
        saved_verbs.append(lemma)

    # Save verb-list-it.js
    verb_list_content = (
        "// ALL_ITALIAN_VERBS - High-frequency verbs for Italian Verb Drills\n"
        f"var ALL_ITALIAN_VERBS = {json.dumps(saved_verbs, ensure_ascii=False, indent=2)};\n\n"
        "if (typeof window !== 'undefined') {\n"
        "  window.ALL_ITALIAN_VERBS = ALL_ITALIAN_VERBS;\n"
        "}\n"
        "if (typeof global !== 'undefined') {\n"
        "  global.ALL_ITALIAN_VERBS = ALL_ITALIAN_VERBS;\n"
        "}\n"
        "if (typeof module !== 'undefined' && module.exports) {\n"
        "  module.exports = ALL_ITALIAN_VERBS;\n"
        "}\n"
    )
    with open(VERB_LIST_OUTPUT, "w", encoding="utf-8") as f:
        f.write(verb_list_content)
    print(f"Saved {len(saved_verbs)} verbs to {VERB_LIST_OUTPUT}")

    # Write attribution README in imports/dictionary/
    credits_content = """# Dictionary & Linguistic Resource Credits

The Italian course linguistic data in Parlour is built using open-source resources:

1. **Kaikki.org / Wiktionary**:
   - Dictionary lemmas, English glosses, grammatical gender, and morphological inflection tables.
   - Author: Tatu Ylonen & Wiktionary contributors.
   - Website: https://kaikki.org/dictionary/Italian/
   - License: Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) and GNU Free Documentation License (GFDL).

2. **HermitDave FrequencyWords**:
   - Lemma frequency rankings derived from OpenSubtitles 2018.
   - Author: HermitDave
   - Repository: https://github.com/hermitdave/FrequencyWords
   - License: Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0).

3. **Parole Italiane**:
   - Italian word lists and verb validation.
   - Author: Napolux
   - Repository: https://github.com/napolux/paroleitaliane
   - License: MIT / CC0.
"""
    readme_path = CACHE_DIR / "CREDITS-IT.md"
    readme_path.write_text(credits_content, encoding="utf-8")
    print("Wrote CREDITS-IT.md with complete resource attribution.")

if __name__ == "__main__":
    process_all()
