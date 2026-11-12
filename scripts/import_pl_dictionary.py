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
    "proper noun": "proper noun",
    "name": "proper noun",
    "particle": "particle"
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
    "słyszeć", "oglądać", "obejrzeć", "pomagać", "pomóc", "grać", "grać", "podróżować",
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

def build_verb_file(lemma, forms_dict, aspect):
    stem = lemma[:-3] if lemma.endswith("ać") or lemma.endswith("eć") or lemma.endswith("ić") or lemma.endswith("yć") else lemma[:-2]

    # Present regular fallback
    if lemma.endswith("ać"):
        pres = { "ja": stem + "am", "ty": stem + "asz", "on": stem + "a", "my": stem + "amy", "wy": stem + "acie", "oni": stem + "ają" }
    elif lemma.endswith("ować"):
        pres = { "ja": stem[:-2] + "uję", "ty": stem[:-2] + "ujesz", "on": stem[:-2] + "uje", "my": stem[:-2] + "ujemy", "wy": stem[:-2] + "ujecie", "oni": stem[:-2] + "ują" }
    elif lemma.endswith("ić") or lemma.endswith("yć"):
        pres = { "ja": stem + "ę", "ty": stem + "isz" if lemma.endswith("ić") else stem + "ysz", "on": stem + "i" if lemma.endswith("ić") else stem + "y", "my": stem + "imy" if lemma.endswith("ić") else stem + "ymy", "wy": stem + "icie" if lemma.endswith("ić") else stem + "ycie", "oni": stem + "ą" }
    else:
        pres = { "ja": stem + "ę", "ty": stem + "esz", "on": stem + "e", "my": stem + "emy", "wy": stem + "ecie", "oni": stem + "ą" }

    # Past regular fallback
    past = {
        "ja_m": stem + "ałem" if lemma.endswith("ać") else stem + "iłem" if lemma.endswith("ić") else stem + "yłem" if lemma.endswith("yć") else stem + "ałem",
        "ja_f": stem + "ałam" if lemma.endswith("ać") else stem + "iłam" if lemma.endswith("ić") else stem + "yłam" if lemma.endswith("yć") else stem + "ałam",
        "ty_m": stem + "ałeś" if lemma.endswith("ać") else stem + "iłeś" if lemma.endswith("ić") else stem + "yłeś" if lemma.endswith("yć") else stem + "ałeś",
        "ty_f": stem + "ałaś" if lemma.endswith("ać") else stem + "iłaś" if lemma.endswith("ić") else stem + "yłaś" if lemma.endswith("yć") else stem + "ałaś",
        "on": stem + "ał" if lemma.endswith("ać") else stem + "ił" if lemma.endswith("ić") else stem + "ył" if lemma.endswith("yć") else stem + "ał",
        "ona": stem + "ała" if lemma.endswith("ać") else stem + "iła" if lemma.endswith("ić") else stem + "yła" if lemma.endswith("yć") else stem + "ała",
        "ono": stem + "ało" if lemma.endswith("ać") else stem + "iło" if lemma.endswith("ić") else stem + "yło" if lemma.endswith("yć") else stem + "ało",
        "my_vir": stem + "aliśmy" if lemma.endswith("ać") else stem + "iliśmy" if lemma.endswith("ić") else stem + "yliśmy" if lemma.endswith("yć") else stem + "aliśmy",
        "my_nonvir": stem + "ałyśmy" if lemma.endswith("ać") else stem + "iłyśmy" if lemma.endswith("ić") else stem + "yłyśmy" if lemma.endswith("yć") else stem + "ałyśmy",
        "wy_vir": stem + "aliście" if lemma.endswith("ać") else stem + "iliście" if lemma.endswith("ić") else stem + "yliście" if lemma.endswith("yć") else stem + "aliście",
        "wy_nonvir": stem + "ałyście" if lemma.endswith("ać") else stem + "iłyście" if lemma.endswith("ić") else stem + "yłyście" if lemma.endswith("yć") else stem + "ałyście",
        "oni": stem + "ali" if lemma.endswith("ać") else stem + "ili" if lemma.endswith("ić") else stem + "yli" if lemma.endswith("yć") else stem + "ali",
        "one": stem + "ały" if lemma.endswith("ać") else stem + "iły" if lemma.endswith("ić") else stem + "yły" if lemma.endswith("yć") else stem + "ały"
    }

    # Future regular
    if aspect == "perfective":
        fut = pres
    else:
        fut = {
            "ja": f"będę {lemma}", "ty": f"będziesz {lemma}", "on": f"będzie {lemma}",
            "my": f"będziemy {lemma}", "wy": f"będziecie {lemma}", "oni": f"będą {lemma}"
        }

    cond = {
        "ja": past["on"] + "bym", "ty": past["on"] + "byś", "on": past["on"] + "by",
        "my": past["oni"] + "byśmy", "wy": past["oni"] + "byście", "oni": past["oni"] + "by"
    }

    imperative = {
        "ty": stem + "aj" if lemma.endswith("ać") else stem,
        "my": stem + "ajmy" if lemma.endswith("ać") else stem + "my",
        "wy": stem + "ajcie" if lemma.endswith("ać") else stem + "cie"
    }

    indicativo = {
        "presente": forms_dict.get("indicativo.presente", pres),
        "przeszly": forms_dict.get("indicativo.przeszly", past),
        "przyszly": forms_dict.get("indicativo.przyszly", fut)
    }

    # Apply canonical overrides
    if lemma in CANONICAL_VERBS:
        c = CANONICAL_VERBS[lemma]
        indicativo["presente"] = c.get("indicativo.presente", indicativo["presente"])
        indicativo["przeszly"] = c.get("indicativo.przeszly", indicativo["przeszly"])
        indicativo["przyszly"] = c.get("indicativo.przyszly", indicativo["przyszly"])
        cond = c.get("tryb.przypuszczajacy", cond)
        imperative = c.get("tryb.rozkazujacy", imperative)
        aspect = c.get("aspect", aspect)

    return {
        "regular": lemma not in CANONICAL_VERBS,
        "infinitive": lemma,
        "infinitivo": lemma,
        "aspect": aspect,
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

    dictionary = {}
    word_index = defaultdict(list)
    verb_index = defaultdict(list)
    verb_data = defaultdict(lambda: {"forms": defaultdict(dict), "aspect": "imperfective"})

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
                    senses = item.get("senses", [])
                    item_tags = set(item.get("tags", []))

                    # Dictionary headword glosses
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

                    # Process forms
                    forms = item.get("forms", [])
                    for fi in forms:
                        form = fi.get("form", "").strip().lower()
                        ftags = set(fi.get("tags", []))
                        if not form or form == word:
                            continue

                        if mapped_pos == "verb":
                            if "present" in ftags and "indicative" in ftags:
                                if "first-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["ja"] = form
                                    verb_index[form].append({"lemma": word, "tense": "presente", "person": "1s"})
                                elif "second-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["ty"] = form
                                    verb_index[form].append({"lemma": word, "tense": "presente", "person": "2s"})
                                elif "third-person" in ftags and "singular" in ftags:
                                    verb_data[word]["forms"]["indicativo.presente"]["on"] = form
                                    verb_index[form].append({"lemma": word, "tense": "presente", "person": "3s"})
                        elif mapped_pos in ("noun", "adjective"):
                            case = None
                            for c in ["nominative", "genitive", "dative", "accusative", "instrumental", "locative", "vocative"]:
                                if c in ftags:
                                    case = c
                                    break
                            number = "singular" if "singular" in ftags else "plural" if "plural" in ftags else None
                            if case:
                                word_index[form].append({"lemma": word, "pos": mapped_pos, "case": case, "number": number})

        except Exception as e:
            print(f"Error while parsing Kaikki: {e}")

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
        "nie": {"en": "no, not", "type": "particle"}
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

    # Save word-index (filter to top 40k frequent lemmas to keep bundle under 10 MB for mobile)
    freq_set = set(freq_list[:40000]) if freq_list else set(dictionary.keys())
    filtered_word_index = {}
    for form, entries in word_index.items():
        kept = [e for e in entries if e.get("lemma") in freq_set]
        if kept:
            filtered_word_index[form] = kept

    print(f"Writing {len(filtered_word_index):,} word index forms to {WORD_INDEX_OUTPUT} ...")
    with open(WORD_INDEX_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(filtered_word_index, f, ensure_ascii=False, separators=(',', ':'))

    # Save verb-index
    print(f"Writing verb index to {VERB_INDEX_OUTPUT} ...")
    with open(VERB_INDEX_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(dict(verb_index), f, ensure_ascii=False, separators=(',', ':'))

    # Save frequency list
    if not freq_list:
        freq_list = list(dictionary.keys())
    print(f"Writing frequency ranking to {FREQUENCY_OUTPUT} ...")
    with open(FREQUENCY_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(freq_list[:50000], f, ensure_ascii=False, separators=(',', ':'))

    # Generate top verbs files
    saved_verbs = []
    print(f"Generating verb files for {len(PRIORITY_VERBS)} Polish verbs...")
    for lemma in PRIORITY_VERBS:
        v_info = verb_data.get(lemma, {"forms": {}, "aspect": "imperfective"})
        aspect = "perfective" if (lemma.startswith(("z", "po", "na", "wy", "prze", "u", "od", "do")) and lemma not in ("znać", "żyć")) else "imperfective"
        verb_file_data = build_verb_file(lemma, v_info["forms"], aspect)
        
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
