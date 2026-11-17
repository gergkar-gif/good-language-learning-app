#!/usr/bin/env python3
"""
Import comprehensive Polish-English dictionary, morphology indexes, and verb library
from Kaikki.org (Wiktionary extract) and HermitDave OpenSubtitles Frequency list.

Attribution & Licensing:
- Kaikki.org / Wiktionary: CC BY-SA 3.0 & GFDL (Tatu Ylonen / Wiktionary contributors)
- HermitDave FrequencyWords: CC BY-SA 3.0 (HermitDave / OpenSubtitles)
- PoliMorf / Morfologik: 2-Clause BSD (Saloni, Woliński, Miłkowski et al.)

Outputs:
  imports/dictionary/polish-en.json
  content/pl/indexes/word-index.json
  content/pl/indexes/verb-index.json
  content/pl/indexes/frequency.json
  imports/verbs/pl/<lemma>.json (Conjugation tables for top verbs)
  imports/verbs/pl/verb-list-pl.js (ALL_POLISH_VERBS list)
"""
import gzip
import json
import os
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

KAIKKI_URL = "https://kaikki.org/dictionary/Polish/kaikki.org-dictionary-Polish.jsonl.gz"
FREQ_URL = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/pl/pl_50k.txt"

CACHE_DIR = Path("imports/dictionary")
KAIKKI_FILE = CACHE_DIR / "kaikki-pl.jsonl.gz"
FREQ_FILE = CACHE_DIR / "frequency-pl.txt"
ADDITIONS_FILE = CACHE_DIR / "additions-pl.json"

DICT_OUTPUT = CACHE_DIR / "polish-en.json"
WORD_INDEX_OUTPUT = Path("content/pl/indexes/word-index.json")
VERB_INDEX_OUTPUT = Path("content/pl/indexes/verb-index.json")
FREQUENCY_OUTPUT = Path("content/pl/indexes/frequency.json")
VERBS_DIR = Path("imports/verbs/pl")
VERB_LIST_OUTPUT = VERBS_DIR / "verb-list-pl.js"

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
NOISE_FORM_TAGS = {'table-tags', 'inflection-template', 'class', 'auxiliary', 'alternative', 'archaic', 'obsolete', 'dated', 'dialectal', 'rare', 'Middle'}
POS_PRIORITY = {
    'preposition': 1, 'conjunction': 1, 'pronoun': 2, 'determiner': 2, 'particle': 2,
    'interjection': 3, 'adverb': 4, 'verb': 5, 'noun': 6, 'adjective': 7, 'numeral': 8
}

# Priority Polish verbs catalog (100+ most frequent and pedagogically essential verbs)
PRIORITY_VERBS = [
    "być", "mieć", "móc", "chcieć", "wiedzieć", "znać", "mówić", "powiedzieć",
    "robić", "zrobić", "widzieć", "zobaczyć", "myśleć", "pomyśleć", "iść", "pójść",
    "jechać", "pojechać", "brać", "wziąć", "dawać", "dać", "rozumieć", "zrozumieć",
    "czekać", "poczekać", "pytać", "zapytać", "odpowiadać", "odpowiedzieć", "szukać", "znaleźć",
    "pracować", "uczyć", "pamiętać", "zapomnieć", "musieć", "woleć", "żyć", "kochać",
    "lubić", "czytać", "przeczytać", "pisać", "napisać", "pić", "wypić", "jeść",
    "zjeść", "spać", "kupować", "kupić", "sprzedawać", "sprzedać", "spotkać", "zaczynać",
    "zacząć", "kończyć", "skończyć", "otwierać", "otworzyć", "zamykać", "zamknąć", "słuchać",
    "słyszeć", "oglądać", "obejrzeć", "pomagać", "pomóc", "grać", "podróżować",
    "mieszkać", "kosztować", "tracić", "stracić", "płacić", "zapłacić", "czuć", "poczuć",
    "dziękować", "podziękować", "przepraszać", "przeprosić", "prosić", "poprosić", "wracać", "wrócić",
    "zostawać", "zostać", "braknąć", "potrzebować", "bać", "cieszyć", "stawać", "stać",
    "siadać", "usiąść", "leżeć", "biegać", "biec", "chodzić", "pływać", "jeździć"
]

CANONICAL_VERBS = {
    "być": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "jestem", "ty": "jesteś", "on": "jest", "my": "jesteśmy", "wy": "jesteście", "oni": "są" },
        "indicativo.przeszly": {
            "ja_m": "byłem", "ja_f": "byłam", "ty_m": "byłeś", "ty_f": "byłaś",
            "on": "był", "ona": "była", "ono": "było",
            "my_vir": "byliśmy", "my_nonvir": "byłyśmy", "wy_vir": "byliście", "wy_nonvir": "byłyście",
            "oni": "byli", "one": "były"
        },
        "indicativo.przyszly": { "ja": "będę", "ty": "będziesz", "on": "będzie", "my": "będziemy", "wy": "będziecie", "oni": "będą" },
        "tryb.przypuszczajacy": { "ja": "byłbym", "ty": "byłbyś", "on": "byłby", "my": "bylibyśmy", "wy": "bylibyście", "oni": "byliby" },
        "tryb.rozkazujacy": { "ty": "bądź", "my": "bądźmy", "wy": "bądźcie" }
    },
    "mieć": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "mam", "ty": "masz", "on": "ma", "my": "mamy", "wy": "macie", "oni": "mają" },
        "indicativo.przeszly": {
            "ja_m": "miałem", "ja_f": "miałam", "ty_m": "miałeś", "ty_f": "miałaś",
            "on": "miał", "ona": "miała", "ono": "miało",
            "my_vir": "mieliśmy", "my_nonvir": "miałyśmy", "wy_vir": "mieliście", "wy_nonvir": "miałyście",
            "oni": "mieli", "one": "miały"
        },
        "indicativo.przyszly": { "ja": "będę mieć", "ty": "będziesz mieć", "on": "będzie mieć", "my": "będziemy mieć", "wy": "będziecie mieć", "oni": "będą mieć" },
        "tryb.przypuszczajacy": { "ja": "miałbym", "ty": "miałbyś", "on": "miałby", "my": "mielibyśmy", "wy": "mielibyście", "oni": "mieliby" },
        "tryb.rozkazujacy": { "ty": "miej", "my": "miejmy", "wy": "miejcie" }
    },
    "móc": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "mogę", "ty": "możesz", "on": "może", "my": "możemy", "wy": "możecie", "oni": "mogą" },
        "indicativo.przeszly": {
            "ja_m": "mogłem", "ja_f": "mogłam", "ty_m": "mogłeś", "ty_f": "mogłaś",
            "on": "mógł", "ona": "mogła", "ono": "mogło",
            "my_vir": "mogliśmy", "my_nonvir": "mogłyśmy", "wy_vir": "mogliście", "wy_nonvir": "mogłyście",
            "oni": "mogli", "one": "mogły"
        },
        "indicativo.przyszly": { "ja": "będę mógł", "ty": "będziesz mógł", "on": "będzie mógł", "my": "będziemy mogli", "wy": "będziecie mogli", "oni": "będą mogli" },
        "tryb.przypuszczajacy": { "ja": "mógłbym", "ty": "mógłbyś", "on": "mógłby", "my": "moglibyśmy", "wy": "moglibyście", "oni": "mogliby" },
        "tryb.rozkazujacy": {}
    },
    "chcieć": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "chcę", "ty": "chcesz", "on": "chce", "my": "chcemy", "wy": "chcecie", "oni": "chcą" },
        "indicativo.przeszly": {
            "ja_m": "chciałem", "ja_f": "chciałam", "ty_m": "chciałeś", "ty_f": "chciałaś",
            "on": "chciał", "ona": "chciała", "ono": "chciało",
            "my_vir": "chcieliśmy", "my_nonvir": "chciałyśmy", "wy_vir": "chcieliście", "wy_nonvir": "chciałyście",
            "oni": "chcieli", "one": "chciały"
        },
        "indicativo.przyszly": { "ja": "będę chciał", "ty": "będziesz chciał", "on": "będzie chciał", "my": "będziemy chcieli", "wy": "będziecie chcieli", "oni": "będą chcieli" },
        "tryb.przypuszczajacy": { "ja": "chciałbym", "ty": "chciałbyś", "on": "chciałby", "my": "chcielibyśmy", "wy": "chcielibyście", "oni": "chcieliby" },
        "tryb.rozkazujacy": { "ty": "chciej", "my": "chciejmy", "wy": "chciejcie" }
    },
    "wiedzieć": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "wiem", "ty": "wiesz", "on": "wie", "my": "wiemy", "wy": "wiecie", "oni": "wiedzą" },
        "indicativo.przeszly": {
            "ja_m": "wiedziałem", "ja_f": "wiedziałam", "ty_m": "wiedziałeś", "ty_f": "wiedziałaś",
            "on": "wiedział", "ona": "wiedziała", "ono": "wiedziało",
            "my_vir": "wiedzieliśmy", "my_nonvir": "wiedziałyśmy", "wy_vir": "wiedzieliście", "wy_nonvir": "wiedziałyście",
            "oni": "wiedzieli", "one": "wiedziały"
        },
        "indicativo.przyszly": { "ja": "będę wiedzieć", "ty": "będziesz wiedzieć", "on": "będzie wiedzieć", "my": "będziemy wiedzieć", "wy": "będziecie wiedzieć", "oni": "będą wiedzieć" },
        "tryb.przypuszczajacy": { "ja": "wiedziałbym", "ty": "wiedziałbyś", "on": "wiedziałby", "my": "wiedzielibyśmy", "wy": "wiedzielibyście", "oni": "wiedzieliby" },
        "tryb.rozkazujacy": { "ty": "wiedz", "my": "wiedzmy", "wy": "wiedzcie" }
    },
    "iść": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "idę", "ty": "idziesz", "on": "idzie", "my": "idziemy", "wy": "idziecie", "oni": "idą" },
        "indicativo.przeszly": {
            "ja_m": "szedłem", "ja_f": "szłam", "ty_m": "szedłeś", "ty_f": "szłaś",
            "on": "szedł", "ona": "szła", "ono": "szło",
            "my_vir": "szliśmy", "my_nonvir": "szłyśmy", "wy_vir": "szliście", "wy_nonvir": "szłyście",
            "oni": "szli", "one": "szły"
        },
        "indicativo.przyszly": { "ja": "będę iść", "ty": "będziesz iść", "on": "będzie iść", "my": "będziemy iść", "wy": "będziecie iść", "oni": "będą iść" },
        "tryb.przypuszczajacy": { "ja": "szedłbym", "ty": "szedłbyś", "on": "szedłby", "my": "szlibyśmy", "wy": "szlibyście", "oni": "szliby" },
        "tryb.rozkazujacy": { "ty": "idź", "my": "idźmy", "wy": "idźcie" }
    },
    "pójść": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "pójdę", "ty": "pójdziesz", "on": "pójdzie", "my": "pójdziemy", "wy": "pójdziecie", "oni": "pójdą" },
        "indicativo.przeszly": {
            "ja_m": "poszedłem", "ja_f": "poszłam", "ty_m": "poszedłeś", "ty_f": "poszłaś",
            "on": "poszedł", "ona": "poszła", "ono": "poszło",
            "my_vir": "poszliśmy", "my_nonvir": "poszłyśmy", "wy_vir": "poszliście", "wy_nonvir": "poszłyście",
            "oni": "poszli", "one": "poszły"
        },
        "indicativo.przyszly": { "ja": "pójdę", "ty": "pójdziesz", "on": "pójdzie", "my": "pójdziemy", "wy": "pójdziecie", "oni": "pójdą" },
        "tryb.przypuszczajacy": { "ja": "poszedłbym", "ty": "poszedłbyś", "on": "poszedłby", "my": "poszlibyśmy", "wy": "poszlibyście", "oni": "poszliby" },
        "tryb.rozkazujacy": { "ty": "pójdź", "my": "pójdźmy", "wy": "pójdźcie" }
    },
    "robić": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "robię", "ty": "robisz", "on": "robi", "my": "robimy", "wy": "robicie", "oni": "robią" },
        "indicativo.przeszly": {
            "ja_m": "robiłem", "ja_f": "robiłam", "ty_m": "robiłeś", "ty_f": "robiłaś",
            "on": "robił", "ona": "robiła", "ono": "robiło",
            "my_vir": "robiliśmy", "my_nonvir": "robiłyśmy", "wy_vir": "robiliście", "wy_nonvir": "robiłyście",
            "oni": "robili", "one": "robiły"
        },
        "indicativo.przyszly": { "ja": "będę robić", "ty": "będziesz robić", "on": "będzie robić", "my": "będziemy robić", "wy": "będziecie robić", "oni": "będą robić" },
        "tryb.przypuszczajacy": { "ja": "robiłbym", "ty": "robiłbyś", "on": "robiłby", "my": "robilibyśmy", "wy": "robilibyście", "oni": "robiliby" },
        "tryb.rozkazujacy": { "ty": "rób", "my": "róbmy", "wy": "róbcie" }
    },
    "zrobić": {
        "aspect": "perfective",
        "indicativo.presente": { "ja": "zrobię", "ty": "zrobisz", "on": "zrobi", "my": "zrobimy", "wy": "zrobicie", "oni": "zrobią" },
        "indicativo.przeszly": {
            "ja_m": "zrobiłem", "ja_f": "zrobiłam", "ty_m": "zrobiłeś", "ty_f": "zrobiłaś",
            "on": "zrobił", "ona": "zrobiła", "ono": "zrobiło",
            "my_vir": "zrobiliśmy", "my_nonvir": "zrobiłyśmy", "wy_vir": "zrobiliście", "wy_nonvir": "zrobiłyście",
            "oni": "zrobili", "one": "zrobiły"
        },
        "indicativo.przyszly": { "ja": "zrobię", "ty": "zrobisz", "on": "zrobi", "my": "zrobimy", "wy": "zrobicie", "oni": "zrobią" },
        "tryb.przypuszczajacy": { "ja": "zrobiłbym", "ty": "zrobiłbyś", "on": "zrobiłby", "my": "zrobilibyśmy", "wy": "zrobilibyście", "oni": "zrobiliby" },
        "tryb.rozkazujacy": { "ty": "zrób", "my": "zróbmy", "wy": "zróbcie" }
    },
    "mówić": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "mówię", "ty": "mówisz", "on": "mówi", "my": "mówimy", "wy": "mówicie", "oni": "mówią" },
        "indicativo.przeszly": {
            "ja_m": "mówiłem", "ja_f": "mówiłam", "ty_m": "mówiłeś", "ty_f": "mówiłaś",
            "on": "mówił", "ona": "mówiła", "ono": "mówiło",
            "my_vir": "mówiliśmy", "my_nonvir": "mówiłyśmy", "wy_vir": "mówiliście", "wy_nonvir": "mówiłyście",
            "oni": "mówili", "one": "mówiły"
        },
        "indicativo.przyszly": { "ja": "będę mówić", "ty": "będziesz mówić", "on": "będzie mówić", "my": "będziemy mówić", "wy": "będziecie mówić", "oni": "będą mówić" },
        "tryb.przypuszczajacy": { "ja": "mówiłbym", "ty": "mówiłbyś", "on": "mówiłby", "my": "mówilibyśmy", "wy": "mówilibyście", "oni": "mówiliby" },
        "tryb.rozkazujacy": { "ty": "mów", "my": "mówmy", "wy": "mówcie" }
    },
    "czytać": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "czytam", "ty": "czytasz", "on": "czyta", "my": "czytamy", "wy": "czytacie", "oni": "czytają" },
        "indicativo.przeszly": {
            "ja_m": "czytałem", "ja_f": "czytałam", "ty_m": "czytałeś", "ty_f": "czytałaś",
            "on": "czytał", "ona": "czytała", "ono": "czytało",
            "my_vir": "czytaliśmy", "my_nonvir": "czytałyśmy", "wy_vir": "czytaliście", "wy_nonvir": "czytałyście",
            "oni": "czytali", "one": "czytały"
        },
        "indicativo.przyszly": { "ja": "będę czytać", "ty": "będziesz czytać", "on": "będzie czytać", "my": "będziemy czytać", "wy": "będziecie czytać", "oni": "będą czytać" },
        "tryb.przypuszczajacy": { "ja": "czytałbym", "ty": "czytałbyś", "on": "czytałby", "my": "czytalibyśmy", "wy": "czytalibyście", "oni": "czytaliby" },
        "tryb.rozkazujacy": { "ty": "czytaj", "my": "czytajmy", "wy": "czytajcie" }
    },
    "pisać": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "piszę", "ty": "piszesz", "on": "pisze", "my": "piszemy", "wy": "piszecie", "oni": "piszą" },
        "indicativo.przeszly": {
            "ja_m": "pisałem", "ja_f": "pisałam", "ty_m": "pisałeś", "ty_f": "pisałaś",
            "on": "pisał", "ona": "pisała", "ono": "pisało",
            "my_vir": "pisaliśmy", "my_nonvir": "pisałyśmy", "wy_vir": "pisaliście", "wy_nonvir": "pisałyście",
            "oni": "pisali", "one": "pisały"
        },
        "indicativo.przyszly": { "ja": "będę pisać", "ty": "będziesz pisać", "on": "będzie pisać", "my": "będziemy pisać", "wy": "będziecie pisać", "oni": "będą pisać" },
        "tryb.przypuszczajacy": { "ja": "pisałbym", "ty": "pisałbyś", "on": "pisałby", "my": "pisalibyśmy", "wy": "pisalibyście", "oni": "pisaliby" },
        "tryb.rozkazujacy": { "ty": "pisz", "my": "piszmy", "wy": "piszcie" }
    },
    "stać": {
        "aspect": "imperfective",
        "indicativo.presente": { "ja": "stoję", "ty": "stoisz", "on": "stoi", "my": "stoimy", "wy": "stoicie", "oni": "stoją" },
        "indicativo.przeszly": {
            "ja_m": "stałem", "ja_f": "stałam", "ty_m": "stałeś", "ty_f": "stałaś",
            "on": "stał", "ona": "stała", "ono": "stało",
            "my_vir": "staliśmy", "my_nonvir": "stałyśmy", "wy_vir": "staliście", "wy_nonvir": "stałyście",
            "oni": "stali", "one": "stały"
        },
        "indicativo.przyszly": { "ja": "będę stać", "ty": "będziesz stać", "on": "będzie stać", "my": "będziemy stać", "wy": "będziecie stać", "oni": "będą stać" },
        "tryb.przypuszczajacy": { "ja": "stałbym", "ty": "stałbyś", "on": "stałby", "my": "stalibyśmy", "wy": "stalibyście", "oni": "staliby" },
        "tryb.rozkazujacy": { "ty": "stój", "my": "stójmy", "wy": "stójcie" }
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
    if len(parts) > 3:
        text = ', '.join(parts[:3])
    return text

def download_sources():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not FREQ_FILE.exists():
        print(f"Downloading Polish frequency list from {FREQ_URL} ...")
        try:
            req = urllib.request.Request(FREQ_URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as resp:
                FREQ_FILE.write_bytes(resp.read())
            print(f"Downloaded {FREQ_FILE.stat().st_size:,} bytes")
        except Exception as e:
            print(f"Could not download frequency file: {e}")
    else:
        print(f"Using cached {FREQ_FILE}")

    if not KAIKKI_FILE.exists():
        print(f"Downloading Kaikki Polish JSONL.gz from {KAIKKI_URL} (~89MB) ...")
        try:
            req = urllib.request.Request(KAIKKI_URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as resp:
                KAIKKI_FILE.write_bytes(resp.read())
            print(f"Downloaded {KAIKKI_FILE.stat().st_size:,} bytes")
        except Exception as e:
            print(f"Could not download Kaikki Polish file: {e}")
    else:
        print(f"Using cached {KAIKKI_FILE}")

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

PL_VERB_EN_OVERRIDES = {
    "być": "to be",
    "mieć": "to have",
    "móc": "to be able, can",
    "chcieć": "to want",
    "wiedzieć": "to know (a fact)",
    "znać": "to know (person/place)",
    "mówić": "to speak, to say",
    "powiedzieć": "to say, to tell",
    "robić": "to do, to make",
    "zrobić": "to do, to make",
    "widzieć": "to see",
    "zobaczyć": "to see, to catch sight of",
    "myśleć": "to think",
    "pomyśleć": "to think, to consider",
    "bać": "to fear, to be afraid",
    "cieszyć": "to gladden; to enjoy",
    "stać": "to stand; to afford",
    "braknąć": "to lack, to run out",
}

def clean_verb_en(word, raw_en):
    if word in PL_VERB_EN_OVERRIDES:
        return PL_VERB_EN_OVERRIDES[word]
    if not raw_en:
        return ""
    parts = []
    for p in re.split(r'[;,]', raw_en):
        p = p.strip()
        low = p.lower()
        if not p or low.startswith(('used ', 'synonym of', 'expressing ', 'with ', 'indicates ', 'see ')):
            continue
        if p.endswith(')') and '(' not in p:
            p = p.rstrip(')').strip()
        if p not in parts:
            parts.append(p)
        if len(", ".join(parts)) > 40 or len(parts) >= 2:
            break
    return ", ".join(parts) if parts else raw_en.split(",")[0].strip()

def build_verb_file(lemma, forms_dict, aspect, en_gloss=""):
    base_inf = lemma[:-2] if lemma.endswith("ć") else lemma
    stem_c = lemma[:-3] if lemma.endswith(("ać", "eć", "ić", "yć")) else lemma[:-2]

    # Present regular fallback
    if lemma.endswith("ować"):
        o_stem = lemma[:-4]
        pres = { "ja": o_stem + "uję", "ty": o_stem + "ujesz", "on": o_stem + "uje", "my": o_stem + "ujemy", "wy": o_stem + "ujecie", "oni": o_stem + "ują" }
    elif lemma.endswith("ać"):
        pres = { "ja": stem_c + "am", "ty": stem_c + "asz", "on": stem_c + "a", "my": stem_c + "amy", "wy": stem_c + "acie", "oni": stem_c + "ają" }
    elif lemma.endswith(("ić", "yć")):
        iv = "i" if lemma.endswith("ić") else "y"
        pres = { "ja": stem_c + "ę", "ty": stem_c + iv + "sz", "on": stem_c + iv, "my": stem_c + iv + "my", "wy": stem_c + iv + "cie", "oni": stem_c + "ą" }
    else:
        pres = { "ja": base_inf + "ę", "ty": base_inf + "esz", "on": base_inf + "e", "my": base_inf + "emy", "wy": base_inf + "ecie", "oni": base_inf + "ą" }

    # Past regular fallback
    past_stem = lemma[:-2] if lemma.endswith("ć") else lemma
    past = {
        "ja_m": past_stem + "łem", "ja_f": past_stem + "łam",
        "ty_m": past_stem + "łeś", "ty_f": past_stem + "łaś",
        "on": past_stem + "ł", "ona": past_stem + "ła", "ono": past_stem + "ło",
        "my_vir": (stem_c + "eliśmy" if lemma.endswith("eć") else past_stem[:-1] + "liśmy" if past_stem.endswith(("a", "i", "y")) else past_stem + "liśmy"),
        "my_nonvir": past_stem + "łyśmy",
        "wy_vir": (stem_c + "eliście" if lemma.endswith("eć") else past_stem[:-1] + "liście" if past_stem.endswith(("a", "i", "y")) else past_stem + "liście"),
        "wy_nonvir": past_stem + "łyście",
        "oni": (stem_c + "eli" if lemma.endswith("eć") else past_stem[:-1] + "li" if past_stem.endswith(("a", "i", "y")) else past_stem + "li"),
        "one": past_stem + "ły"
    }

    parsed_pres = forms_dict.get("indicativo.presente") or pres
    parsed_past = forms_dict.get("indicativo.przeszly") or past
    # Merge fallback keys if Kaikki missed any gender/number subkey
    for pk, pv in past.items():
        parsed_past.setdefault(pk, pv)

    # Future: perfective uses simple present/future stem; imperfective uses będą + inf
    if aspect == "perfective":
        fut = dict(forms_dict.get("indicativo.przyszly") or parsed_pres)
        if not forms_dict.get("indicativo.presente"):
            parsed_pres = fut
    else:
        fut = {
            "ja": f"będę {lemma}", "ty": f"będziesz {lemma}", "on": f"będzie {lemma}",
            "my": f"będziemy {lemma}", "wy": f"będziecie {lemma}", "oni": f"będą {lemma}"
        }

    on_p = parsed_past.get("on", past["on"])
    oni_p = parsed_past.get("oni", past["oni"])
    reg_cond = {
        "ja": on_p + "bym", "ty": on_p + "byś", "on": on_p + "by",
        "my": oni_p + "byśmy", "wy": oni_p + "byście", "oni": oni_p + "by"
    }
    cond = dict(forms_dict.get("tryb.przypuszczajacy") or reg_cond)
    for ck, cv in reg_cond.items():
        cond.setdefault(ck, cv)

    reg_imp = {
        "ty": stem_c + "aj" if lemma.endswith("ać") else stem_c,
        "my": stem_c + "ajmy" if lemma.endswith("ać") else stem_c + "my",
        "wy": stem_c + "ajcie" if lemma.endswith("ać") else stem_c + "cie"
    }
    imperative = dict(forms_dict.get("tryb.rozkazujacy") or reg_imp)
    for ik, iv in reg_imp.items():
        imperative.setdefault(ik, iv)

    indicativo = {
        "presente": parsed_pres,
        "przeszly": parsed_past,
        "przyszly": fut
    }

    # Apply canonical overrides
    if lemma in CANONICAL_VERBS:
        c = CANONICAL_VERBS[lemma]
        indicativo["presente"] = dict(c.get("indicativo.presente", indicativo["presente"]))
        indicativo["przeszly"] = dict(c.get("indicativo.przeszly", indicativo["przeszly"]))
        indicativo["przyszly"] = dict(c.get("indicativo.przyszly", indicativo["przyszly"]))
        cond = dict(c.get("tryb.przypuszczajacy", cond))
        imperative = dict(c.get("tryb.rozkazujacy", imperative))
        aspect = c.get("aspect", aspect)

    # Ensure VerbsTable / VerbsSpeed defaultPersons ('ja', 'ty', 'my', 'wy') exist on przeszly
    przeszly = indicativo["przeszly"]
    if "ja" not in przeszly and przeszly.get("ja_m"):
        przeszly["ja"] = f"{przeszly['ja_m']}/{przeszly['ja_f']}" if przeszly.get("ja_f") else przeszly["ja_m"]
    if "ty" not in przeszly and przeszly.get("ty_m"):
        przeszly["ty"] = f"{przeszly['ty_m']}/{przeszly['ty_f']}" if przeszly.get("ty_f") else przeszly["ty_m"]
    if "my" not in przeszly and przeszly.get("my_vir"):
        przeszly["my"] = f"{przeszly['my_vir']}/{przeszly['my_nonvir']}" if przeszly.get("my_nonvir") else przeszly["my_vir"]
    if "wy" not in przeszly and przeszly.get("wy_vir"):
        przeszly["wy"] = f"{przeszly['wy_vir']}/{przeszly['wy_nonvir']}" if przeszly.get("wy_nonvir") else przeszly["wy_vir"]

    return {
        "regular": lemma not in CANONICAL_VERBS,
        "infinitive": lemma,
        "infinitivo": lemma,
        "aspect": aspect,
        "english": {
            "infinitivo": clean_verb_en(lemma, en_gloss)
        },
        "indicativo": indicativo,
        "tryb": {
            "przypuszczajacy": cond,
            "rozkazujacy": imperative
        },
        "tenses": {
            "indicativo.presente": indicativo["presente"],
            "indicativo.przeszly": indicativo["przeszly"],
            "indicativo.przyszly": indicativo["przyszly"]
        }
    }

def process_all():
    download_sources()
    freq_rank, freq_list = parse_frequency()

    WORD_INDEX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    VERBS_DIR.mkdir(parents=True, exist_ok=True)

    verbs_only = "--verbs-only" in sys.argv
    priority_set = set(PRIORITY_VERBS)

    dictionary = {}
    if verbs_only and DICT_OUTPUT.exists():
        with open(DICT_OUTPUT, "r", encoding="utf-8") as df:
            dictionary = json.load(df)

    lemma_candidates = defaultdict(lambda: defaultdict(lambda: {"senses": [], "gender": None, "aspect": None, "deprioritised": True}))
    word_index = defaultdict(list)
    verb_index = defaultdict(list)
    verb_data = defaultdict(lambda: {"forms": defaultdict(dict), "aspect": None})
    verb_glosses = {}

    # Check if Kaikki file is available
    if KAIKKI_FILE.exists():
        print(f"Parsing Kaikki Polish extract from {KAIKKI_FILE}...")
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
                    if verbs_only and (mapped_pos != "verb" or word not in priority_set):
                        continue
                    senses = item.get("senses", [])
                    item_tags = set(item.get("tags", []))

                    # Dictionary headword glosses
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

                    if mapped_pos == "verb" and word in priority_set and word not in verb_glosses and 'form-of' not in item_tags:
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

                    # Process forms
                    forms = item.get("forms", [])
                    table_aspect = None
                    skip_verb_table = False
                    if mapped_pos == "verb":
                        for fi in forms:
                            if "table-tags" in (fi.get("tags") or []):
                                tf = (fi.get("form") or "").strip().lower()
                                if tf == "no-table-tags":
                                    skip_verb_table = True
                                elif tf in ("imperfective", "perfective"):
                                    table_aspect = tf
                                break
                        if word in priority_set and table_aspect and not verb_data[word]["aspect"]:
                            verb_data[word]["aspect"] = table_aspect

                    seen_counts = defaultdict(int)
                    for fi in forms:
                        form = fi.get("form", "").strip().lower()
                        ftags = set(fi.get("tags", []))
                        if not form or '-' in form or '(' in form or not any(ch.isalpha() for ch in form) or (ftags & NOISE_FORM_TAGS):
                            continue

                        if mapped_pos == "verb" and not skip_verb_table and word in priority_set and ' ' not in form and "impersonal" not in ftags and "passive" not in ftags and "participle" not in ftags and "noun-from-verb" not in ftags and "infinitive" not in ftags:
                            entry_forms = verb_data[word]["forms"]
                            is_perf_fut = (table_aspect == "perfective" and "future" in ftags)
                            if ("present" in ftags or is_perf_fut) and "imperative" not in ftags and "conditional" not in ftags and "past" not in ftags:
                                tkeys = ["indicativo.presente", "indicativo.przyszly"] if is_perf_fut else ["indicativo.presente"]
                                if "third-person" in ftags:
                                    p_key = "on" if "singular" in ftags else ("oni" if "plural" in ftags else None)
                                elif "first-person" in ftags:
                                    p_key = "ja" if "singular" in ftags else ("my" if "plural" in ftags else None)
                                elif "second-person" in ftags:
                                    p_key = "ty" if "singular" in ftags else ("wy" if "plural" in ftags else None)
                                elif "singular" in ftags:
                                    seen_counts["pres_sg"] += 1
                                    p_key = "ja" if seen_counts["pres_sg"] == 1 else ("ty" if seen_counts["pres_sg"] == 2 else None)
                                elif "plural" in ftags:
                                    seen_counts["pres_pl"] += 1
                                    p_key = "my" if seen_counts["pres_pl"] == 1 else ("wy" if seen_counts["pres_pl"] == 2 else None)
                                else:
                                    p_key = None
                                if p_key:
                                    for tk in tkeys:
                                        entry_forms[tk].setdefault(p_key, form)

                            elif "past" in ftags and "conditional" not in ftags:
                                slot = None
                                if "third-person" in ftags:
                                    if "singular" in ftags:
                                        slot = "on" if "masculine" in ftags else ("ona" if "feminine" in ftags else ("ono" if "neuter" in ftags else None))
                                    elif "plural" in ftags:
                                        slot = "oni" if "virile" in ftags else ("one" if "nonvirile" in ftags else None)
                                elif "singular" in ftags:
                                    g_tag = "m" if "masculine" in ftags else ("f" if "feminine" in ftags else None)
                                    if g_tag:
                                        seen_counts[f"past_sg_{g_tag}"] += 1
                                        idx = seen_counts[f"past_sg_{g_tag}"]
                                        slot = f"ja_{g_tag}" if idx == 1 else (f"ty_{g_tag}" if idx == 2 else None)
                                elif "plural" in ftags:
                                    g_tag = "vir" if "virile" in ftags else ("nonvir" if "nonvirile" in ftags else None)
                                    if g_tag:
                                        seen_counts[f"past_pl_{g_tag}"] += 1
                                        idx = seen_counts[f"past_pl_{g_tag}"]
                                        slot = f"my_{g_tag}" if idx == 1 else (f"wy_{g_tag}" if idx == 2 else None)
                                if slot:
                                    entry_forms["indicativo.przeszly"].setdefault(slot, form)

                            elif "conditional" in ftags:
                                cslot = None
                                if "third-person" in ftags:
                                    if "singular" in ftags and "masculine" in ftags:
                                        cslot = "on"
                                    elif "plural" in ftags and "virile" in ftags:
                                        cslot = "oni"
                                elif "singular" in ftags and "masculine" in ftags:
                                    seen_counts["cond_sg"] += 1
                                    cslot = "ja" if seen_counts["cond_sg"] == 1 else ("ty" if seen_counts["cond_sg"] == 2 else None)
                                elif "plural" in ftags and "virile" in ftags:
                                    seen_counts["cond_pl"] += 1
                                    cslot = "my" if seen_counts["cond_pl"] == 1 else ("wy" if seen_counts["cond_pl"] == 2 else None)
                                if cslot:
                                    entry_forms["tryb.przypuszczajacy"].setdefault(cslot, form)

                            elif "imperative" in ftags and "third-person" not in ftags:
                                islot = None
                                if "singular" in ftags:
                                    islot = "ty"
                                elif "plural" in ftags:
                                    seen_counts["imp_pl"] += 1
                                    islot = "my" if seen_counts["imp_pl"] == 1 else ("wy" if seen_counts["imp_pl"] == 2 else None)
                                if islot:
                                    entry_forms["tryb.rozkazujacy"].setdefault(islot, form)

                        if verbs_only or form == word or ' ' in form:
                            continue

                        if mapped_pos == "verb":
                            tense = (
                                "presente" if "present" in ftags else
                                "przeszly" if "past" in ftags else
                                "przyszly" if "future" in ftags else
                                "przypuszczajacy" if "conditional" in ftags else
                                "rozkazujacy" if "imperative" in ftags else
                                "participle" if "participle" in ftags else
                                "gerund" if "noun-from-verb" in ftags else None
                            )
                            if tense:
                                person = "1" if "first-person" in ftags else "2" if "second-person" in ftags else "3" if "third-person" in ftags else None
                                number = "singular" if "singular" in ftags else "plural" if "plural" in ftags else None
                                gender = "m" if "masculine" in ftags else "f" if "feminine" in ftags else "n" if "neuter" in ftags else "vir" if "virile" in ftags else "nonvir" if "nonvirile" in ftags else None
                                entry = {"lemma": word, "tense": tense}
                                if person and number:
                                    entry["person"] = f"{person}{'s' if number == 'singular' else 'p'}"
                                elif number:
                                    entry["number"] = number
                                if gender:
                                    entry["gender"] = gender
                                if entry not in verb_index[form]:
                                    verb_index[form].append(entry)

                            if "present" in ftags and "imperative" not in ftags:
                                if "first-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["ja"] = form
                                elif "second-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["ty"] = form
                                elif "third-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["on"] = form
                        elif mapped_pos in ("noun", "adjective"):
                            case = None
                            for c in ["nominative", "genitive", "dative", "accusative", "instrumental", "locative", "vocative"]:
                                if c in ftags:
                                    case = c
                                    break
                            number = "singular" if "singular" in ftags else "plural" if "plural" in ftags else None
                            if case:
                                entry = {"lemma": word, "pos": mapped_pos, "case": case, "number": number}
                                if entry not in word_index[form]:
                                    word_index[form].append(entry)

        except Exception as e:
            print(f"Error while parsing Kaikki: {e}")

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

        # Fallback foundational dictionary if Kaikki was unavailable or incomplete
        FOUNDATIONAL_DICT = {
        "być": {"en": "to be", "type": "verb"},
        "mieć": {"en": "to have", "type": "verb"},
        "móc": {"en": "can, to be able to", "type": "verb"},
        "chcieć": {"en": "to want", "type": "verb"},
        "wiedzieć": {"en": "to know (a fact)", "type": "verb"},
        "znać": {"en": "to know (a person or place)", "type": "verb"},
        "mówić": {"en": "to speak, to say", "type": "verb"},
        "powiedzieć": {"en": "to say, to tell", "type": "verb"},
        "robić": {"en": "to do, to make", "type": "verb"},
        "zrobić": {"en": "to do, to make (completed)", "type": "verb"},
        "widzieć": {"en": "to see", "type": "verb"},
        "zobaczyć": {"en": "to see, to catch sight of", "type": "verb"},
        "myśleć": {"en": "to think", "type": "verb"},
        "pomyśleć": {"en": "to think of, to consider", "type": "verb"},
        "iść": {"en": "to go on foot", "type": "verb"},
        "pójść": {"en": "to go, to set off on foot", "type": "verb"},
        "jechać": {"en": "to go by vehicle, to drive", "type": "verb"},
        "pojechać": {"en": "to go by vehicle (completed)", "type": "verb"},
        "brać": {"en": "to take", "type": "verb"},
        "wziąć": {"en": "to take (completed)", "type": "verb"},
        "dawać": {"en": "to give", "type": "verb"},
        "dać": {"en": "to give (completed)", "type": "verb"},
        "rozumieć": {"en": "to understand", "type": "verb"},
        "zrozumieć": {"en": "to understand (completed)", "type": "verb"},
        "pracować": {"en": "to work", "type": "verb"},
        "uczyć": {"en": "to teach, to learn", "type": "verb"},
        "czytać": {"en": "to read", "type": "verb"},
        "przeczytać": {"en": "to read through", "type": "verb"},
        "pisać": {"en": "to write", "type": "verb"},
        "napisać": {"en": "to write (completed)", "type": "verb"},
        "pić": {"en": "to drink", "type": "verb"},
        "jeść": {"en": "to eat", "type": "verb"},
        "stół": {"en": "table", "type": "noun", "gender": "m"},
        "krzesło": {"en": "chair", "type": "noun", "gender": "n"},
        "dom": {"en": "house, home", "type": "noun", "gender": "m"},
        "mieszkanie": {"en": "apartment, flat", "type": "noun", "gender": "n"},
        "miasto": {"en": "city, town", "type": "noun", "gender": "n"},
        "ulica": {"en": "street", "type": "noun", "gender": "f"},
        "pies": {"en": "dog", "type": "noun", "gender": "m"},
        "kot": {"en": "cat", "type": "noun", "gender": "m"},
        "kawa": {"en": "coffee", "type": "noun", "gender": "f"},
        "herbata": {"en": "tea", "type": "noun", "gender": "f"},
        "woda": {"en": "water", "type": "noun", "gender": "f"},
        "chleb": {"en": "bread", "type": "noun", "gender": "m"},
        "polska": {"en": "Poland", "type": "proper noun", "gender": "f"},
        "warszawa": {"en": "Warsaw", "type": "proper noun", "gender": "f"},
        "kraków": {"en": "Kraków", "type": "proper noun", "gender": "m"},
        "dzień": {"en": "day", "type": "noun", "gender": "m"},
        "noc": {"en": "night", "type": "noun", "gender": "f"},
        "rano": {"en": "morning", "type": "noun", "gender": "n"},
        "wieczór": {"en": "evening", "type": "noun", "gender": "m"},
        "dobry": {"en": "good", "type": "adjective"},
        "duży": {"en": "big, large", "type": "adjective"},
        "mały": {"en": "small, little", "type": "adjective"},
        "nowy": {"en": "new", "type": "adjective"},
        "stary": {"en": "old", "type": "adjective"},
        "piękny": {"en": "beautiful", "type": "adjective"},
        "drogi": {"en": "expensive, dear", "type": "adjective"},
        "tani": {"en": "cheap, inexpensive", "type": "adjective"},
        "proszę": {"en": "please, you are welcome", "type": "particle"},
        "dziękuję": {"en": "thank you", "type": "particle"},
        "przepraszam": {"en": "excuse me, I am sorry", "type": "particle"},
        "tak": {"en": "yes", "type": "particle"},
        "nie": {"en": "no, not", "type": "particle"},
        "i": {"en": "and", "type": "conjunction"}
        }
        for k, v in FOUNDATIONAL_DICT.items():
            if k not in dictionary:
                dictionary[k] = v

        # Additions overlay
        if ADDITIONS_FILE.exists():
            try:
                with open(ADDITIONS_FILE, "r", encoding="utf-8") as f:
                    adds = json.load(f)
                    for k, v in adds.items():
                        dictionary[k.lower()] = v
            except Exception:
                pass

        # Save dictionary
        print(f"Writing {len(dictionary):,} entries to {DICT_OUTPUT} ...")
        with open(DICT_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=2)

        # Save word-index (filter to top 40k frequent lemmas present in dictionary)
        freq_set = set(freq_list[:40000]) if freq_list else set(dictionary.keys())
        filtered_word_index = {}
        for form, entries in word_index.items():
            kept = [e for e in entries if e.get("lemma") in freq_set and e.get("lemma") in dictionary]
            if kept:
                filtered_word_index[form] = kept[:4]

        print(f"Writing {len(filtered_word_index):,} word index forms to {WORD_INDEX_OUTPUT} ...")
        with open(WORD_INDEX_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(filtered_word_index, f, ensure_ascii=False, separators=(',', ':'))

        # Filter & save verb-index
        verb_freq_set = (set(freq_list[:40000]) | set(PRIORITY_VERBS)) if freq_list else set(dictionary.keys())
        filtered_verb_index = {}
        for form, entries in verb_index.items():
            kept = [e for e in entries if e.get("lemma") in verb_freq_set and e.get("lemma") in dictionary]
            if kept:
                filtered_verb_index[form] = kept[:4]

        print(f"Writing {len(filtered_verb_index):,} verb index forms to {VERB_INDEX_OUTPUT} ...")
        with open(VERB_INDEX_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(filtered_verb_index, f, ensure_ascii=False, separators=(',', ':'))

        # Save frequency list
        if not freq_list:
            freq_list = list(dictionary.keys())
        print(f"Writing frequency ranking to {FREQUENCY_OUTPUT} ...")
        with open(FREQUENCY_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(freq_list[:50000], f, ensure_ascii=False, separators=(',', ':'))
    else:
        print("Skipping dictionary/index writes (--verbs-only).")

    if "--indexes-only" in sys.argv:
        print("Skipping verb files generation (--indexes-only).")
        return

    # Generate top verbs files
    saved_verbs = []
    print(f"Generating verb files for {len(PRIORITY_VERBS)} Polish verbs...")
    for lemma in PRIORITY_VERBS:
        v_info = verb_data.get(lemma, {"forms": {}, "aspect": None})
        aspect = v_info.get("aspect") or ("perfective" if (lemma.startswith(("z", "po", "na", "wy", "prze", "u", "od", "do")) and lemma not in ("znać", "żyć", "pomagać", "podróżować", "potrzebować", "zaczynać", "zamykać", "zostawać", "dziękować", "przepraszać")) else "imperfective")
        raw_en = verb_glosses.get(lemma) or (dictionary.get(lemma, {}).get("en", ""))
        verb_file_data = build_verb_file(lemma, v_info["forms"], aspect, raw_en)
        
        v_path = VERBS_DIR / f"{lemma}.json"
        with open(v_path, "w", encoding="utf-8") as f:
            json.dump(verb_file_data, f, ensure_ascii=False, indent=2)
        saved_verbs.append(lemma)

    # Save verb-list-pl.js
    verb_list_content = (
        "// ALL_POLISH_VERBS - High-frequency verbs for Polish Verb Drills\n"
        f"var ALL_POLISH_VERBS = {json.dumps(saved_verbs, ensure_ascii=False, indent=2)};\n\n"
        "if (typeof window !== 'undefined') {\n"
        "  window.ALL_POLISH_VERBS = ALL_POLISH_VERBS;\n"
        "}\n"
        "if (typeof global !== 'undefined') {\n"
        "  global.ALL_POLISH_VERBS = ALL_POLISH_VERBS;\n"
        "}\n"
        "if (typeof module !== 'undefined' && module.exports) {\n"
        "  module.exports = ALL_POLISH_VERBS;\n"
        "}\n"
    )
    with open(VERB_LIST_OUTPUT, "w", encoding="utf-8") as f:
        f.write(verb_list_content)

    print(f"Saved {len(saved_verbs)} verbs to {VERBS_DIR} and {VERB_LIST_OUTPUT}")
    print("Polish dictionary and index ingestion complete.")

if __name__ == "__main__":
    process_all()
