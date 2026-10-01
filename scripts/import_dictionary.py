#!/usr/bin/env python3
"""
Import a compact Spanish-English dictionary from doozan/spanish_data.

That project extracts and cleans Spanish-Wiktionary data into a simple
per-headword block format (es-en.data), updated monthly. It replaces an
earlier version of this script that targeted the full Kaikki Wiktionary
dump (~1GB) — far too large to ship to a browser/mobile app. This source
is ~18MB raw and produces a compact one-entry-per-lemma dictionary.

Source: https://github.com/doozan/spanish_data (CC-BY-4.0)

Usage:
    python scripts/import_dictionary.py

Output:
    imports/dictionary/spanish-en.json
    { "<lemma>": { "en": "<translation>", "type": "<pos>", "gender": "m"|"f"|null } }

One entry per lemma with its primary sense — this dictionary is meant to
be looked up by lemma (e.g. after resolving a conjugated verb form via
generated/indexes/verb-index.json), not by every inflected surface form.
"""
import json
import re
import urllib.request
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/doozan/spanish_data/master/es-en.data"

OUTPUT_DIR = Path("imports/dictionary")
OUTPUT_FILE = OUTPUT_DIR / "spanish-en.json"
RAW_CACHE = OUTPUT_DIR / "es-en.data.raw"

# Short POS codes used by the source -> normalized names used in the app
POS_MAP = {
    "n": "noun", "v": "verb", "adj": "adjective", "adv": "adverb",
    "pron": "pronoun", "prep": "preposition", "conj": "conjunction",
    "interj": "interjection", "article": "article", "num": "numeral",
    "determiner": "determiner", "prop": "proper noun",
}
# Categories not useful for word-tap lookup (single tapped words never
# match these — they're multi-word or purely grammatical particles).
# "letter" is here too: the source gives the name of the alphabet letter
# ("A" -> "letter") its own pos block, which otherwise wins by being first —
# see LETTER_GLOSS_RE below for the other place the same sense hides.
# Multi-word entries ("mucho gusto", "hasta luego", "me llamo") are kept on
# purpose: translating them word by word is actively misleading, and the
# reader detects them when a learner taps any word inside one.
SKIP_POS = {
    "suffix", "prefix", "infix", "interfix", "particle",
    "punct", "symbol", "character", "contraction", "name", "letter",
}

# "de" and "te" — among the most common function words in the language —
# both parse with a pos:n block ("letter: d" / "letter: t", the name of the
# alphabet letter) ahead of their real pos:prep/pos:pron block, because the
# source lists pos blocks in the order Wiktionary happens to store them, not
# by frequency. Any (pos, gloss) matching this is scored worst so a real
# sense from another pos block wins instead. See
# [[dictionary-sense-collision-issue]] in project memory.
LETTER_GLOSS_RE = re.compile(r"^(letter:|letter$|name of the letter\b)", re.IGNORECASE)
RARE_RE = re.compile(r"\brare\b", re.IGNORECASE)

# Confirmed-wrong entries that the scoring below still can't fix: the
# upstream source itself mislabels the common sense as "rare" while leaving
# the actually-obscure one untagged (tranquilar), or simply doesn't carry
# the requested surface form's sense under this headword at all (mía has
# only a military-historical noun sense; the possessive-pronoun sense lives
# under mío and isn't cross-linked). Hand-fixed rather than left broken.
#
# haber/taco/mexicano/gustar/chica (bug reports #126-#128): the scoring
# picked technically-real senses that are still bad for a learner — an
# obscure "peg" sense of taco over the food, gender-agreement wording on
# haber's perfect aspect that doesn't apply to Spanish at all (that's a
# different Romance language's rule bleeding into this gloss), an
# academic "compare mexiquense" aside, a multi-language cross-reference
# dump on gustar, and an indirect "female equivalent of chico" phrasing
# for chica where a direct gloss reads better.
MANUAL_OVERRIDES = {
    "tranquilar": {"en": "to calm down", "type": "verb"},
    "mía": {"en": "mine (feminine)", "type": "pronoun"},
    "haber": {
        "en": "to have (auxiliary verb used with a past participle to form "
              "the perfect tenses: he comido = I have eaten); impersonal "
              "form 'hay' means 'there is/are'",
        "type": "verb",
    },
    "taco": {"en": "taco (folded or rolled tortilla with a filling)", "type": "noun", "gender": "m"},
    "mexicano": {"en": "Mexican", "type": "adjective"},
    "gustar": {
        "en": "to like, literally 'to please': the thing liked is the "
              "subject and the person is the indirect object, e.g. "
              "'me gusta' = 'I like it' (lit. 'it pleases me')",
        "type": "verb",
    },
    "chica": {"en": "girl; young woman", "type": "noun", "gender": "f"},
    "llamas": {
        "en": "you call, you're called (from llamar — used reflexively in "
              "'¿cómo te llamas?', 'what's your name?'); also the plural of "
              "llama, meaning 'flames' or the South American animal",
        "type": "verb",
    },
    # ROADMAP 92 audit (2026-10-01): top-3000 frequency forms whose own
    # headword is an unrelated homograph, surname, place or niche sense.
    # The dictionary keys on the exact string, so these are what a manually
    # added deck word or an un-glossed card would show.
    "a": {"en": "to, at", "type": "preposition"},
    "al": {"en": "to the (a + el)", "type": "preposition"},
    "una": {"en": "a, an (feminine); one", "type": "determiner"},
    "sí": {"en": "yes; oneself (after a preposition: para sí)", "type": "adverb"},
    "u": {"en": "or (replaces 'o' before a word starting with o-/ho-)", "type": "conjunction"},
    "ha": {"en": "has (from haber, auxiliary: ha comido = he/she has eaten)", "type": "verb"},
    "he": {"en": "I have (from haber, auxiliary: he comido = I have eaten)", "type": "verb"},
    "hay": {"en": "there is, there are (from haber)", "type": "verb"},
    "haya": {"en": "there is / has (subjunctive of haber); also 'beech tree'", "type": "verb"},
    "son": {"en": "they are, you (plural) are (from ser); also 'tune, sound'", "type": "verb"},
    "era": {"en": "was, used to be (from ser); also 'era, age'", "type": "verb"},
    "van": {"en": "they go, you (plural) go (from ir)", "type": "verb"},
    "ve": {"en": "go! (from ir); he/she sees (from ver)", "type": "verb"},
    "dan": {"en": "they give, you (plural) give (from dar)", "type": "verb"},
    "hace": {"en": "he/she does, makes (from hacer); 'ago' in 'hace dos años'", "type": "verb"},
    "mira": {"en": "he/she looks, look! (from mirar)", "type": "verb"},
    "pasa": {"en": "it happens, he/she passes (from pasar); also 'raisin'", "type": "verb"},
    "podemos": {"en": "we can (from poder)", "type": "verb"},
    "dije": {"en": "I said, I told (from decir)", "type": "verb"},
    "espera": {"en": "he/she waits, wait! (from esperar); also 'a wait'", "type": "verb"},
    "vale": {"en": "okay, all right; it costs, it's worth (from valer)", "type": "verb"},
    "deja": {"en": "he/she leaves, lets (from dejar)", "type": "verb"},
    "trata": {"en": "he/she tries, deals with (from tratar)", "type": "verb"},
    "llama": {"en": "he/she calls, is called (from llamar); also 'flame', 'llama'", "type": "verb"},
    "toma": {"en": "he/she takes, take! (from tomar)", "type": "verb"},
    "habla": {"en": "he/she speaks (from hablar); also 'speech'", "type": "verb"},
    "escucha": {"en": "he/she listens, listen! (from escuchar)", "type": "verb"},
    "queda": {"en": "it remains, is left; it fits (from quedar)", "type": "verb"},
    "acerca": {"en": "about (in 'acerca de'); he/she brings closer (from acercar)", "type": "adverb"},
    "pienso": {"en": "I think (from pensar); also 'animal feed'", "type": "verb"},
    "acabo": {"en": "I finish; 'acabo de' = I have just (from acabar)", "type": "verb"},
    "pase": {"en": "come in!; that he/she passes (from pasar); also 'a pass'", "type": "verb"},
    "busca": {"en": "he/she looks for (from buscar)", "type": "verb"},
    "anda": {"en": "he/she walks, goes; come on! (from andar)", "type": "verb"},
    "juro": {"en": "I swear (from jurar)", "type": "verb"},
    "dejo": {"en": "I leave, I let (from dejar); also 'accent, aftertaste'", "type": "verb"},
    "deje": {"en": "that he/she leaves, lets (subjunctive of dejar)", "type": "verb"},
    "verme": {"en": "to see me (ver + me)", "type": "verb"},
    "sepa": {"en": "that he/she knows (subjunctive of saber)", "type": "verb"},
    "llegue": {"en": "that he/she arrives (subjunctive of llegar)", "type": "verb"},
    "ama": {"en": "he/she loves (from amar); also 'lady of the house'", "type": "verb"},
    "toca": {"en": "he/she touches, plays; it's your turn (from tocar)", "type": "verb"},
    "salga": {"en": "that he/she goes out (subjunctive of salir)", "type": "verb"},
    "gana": {"en": "he/she wins, earns (from ganar); 'tener ganas' = to feel like", "type": "verb"},
    "cuesta": {"en": "it costs (from costar); also 'slope'", "type": "verb"},
    "bebe": {"en": "he/she drinks (from beber); 'bebé' = baby", "type": "verb"},
    "paga": {"en": "he/she pays (from pagar); also 'pay, wages'", "type": "verb"},
    "harán": {"en": "they will do, will make (from hacer)", "type": "verb"},
    "mata": {"en": "he/she kills (from matar); also 'shrub'", "type": "verb"},
    "tomé": {"en": "I took (from tomar)", "type": "verb"},
    "saca": {"en": "he/she takes out (from sacar)", "type": "verb"},
    "cae": {"en": "he/she falls (from caer)", "type": "verb"},
    "quedo": {"en": "I stay, I remain (from quedar)", "type": "verb"},
    "pongo": {"en": "I put (from poner)", "type": "verb"},
    "tomo": {"en": "I take (from tomar); also 'volume, tome'", "type": "verb"},
    "consigo": {"en": "I get, I achieve (from conseguir); also 'with himself/herself'", "type": "verb"},
    "tira": {"en": "he/she throws, pulls (from tirar); also 'strip'", "type": "verb"},
    "ruego": {"en": "I beg, I ask (from rogar); also 'plea'", "type": "verb"},
    "dado": {"en": "given (from dar); also 'a die, dice'", "type": "verb"},
    "oído": {"en": "heard (from oír); also 'ear, hearing'", "type": "verb"},
    "vuelto": {"en": "returned (from volver); also 'change (money)'", "type": "verb"},
    "hechos": {"en": "facts; done, made (from hacer)", "type": "noun"},
    "sola": {"en": "alone, only (feminine of solo)", "type": "adjective"},
    "segura": {"en": "sure, safe (feminine of seguro)", "type": "adjective"},
    "hermosa": {"en": "beautiful (feminine of hermoso)", "type": "adjective"},
    "bonita": {"en": "pretty (feminine of bonito)", "type": "adjective"},
    "rara": {"en": "strange, rare (feminine of raro)", "type": "adjective"},
    "antigua": {"en": "old, ancient, former (feminine of antiguo)", "type": "adjective"},
    "hecha": {"en": "done, made (feminine of hecho)", "type": "adjective"},
    "primera": {"en": "first (feminine of primero)", "type": "adjective"},
    "segunda": {"en": "second (feminine of segundo)", "type": "adjective"},
    "tercera": {"en": "third (feminine of tercero)", "type": "adjective"},
    "nueva": {"en": "new (feminine of nuevo)", "type": "adjective"},
    "alta": {"en": "tall, high (feminine of alto)", "type": "adjective"},
    "baja": {"en": "short, low (feminine of bajo)", "type": "adjective"},
    "blanca": {"en": "white (feminine of blanco)", "type": "adjective"},
    "clara": {"en": "clear, light (feminine of claro); also 'egg white'", "type": "adjective"},
    "corta": {"en": "short (feminine of corto); he/she cuts (from cortar)", "type": "adjective"},
    "fría": {"en": "cold (feminine of frío)", "type": "adjective"},
    "limpia": {"en": "clean (feminine of limpio); he/she cleans (from limpiar)", "type": "adjective"},
    "abierta": {"en": "open (feminine of abierto)", "type": "adjective"},
    "directa": {"en": "direct (feminine of directo)", "type": "adjective"},
    "pasada": {"en": "past, last (feminine of pasado): la semana pasada = last week", "type": "adjective"},
    "privada": {"en": "private (feminine of privado)", "type": "adjective"},
    "mala": {"en": "bad (feminine of malo)", "type": "adjective"},
    "vieja": {"en": "old (feminine of viejo); also 'old woman'", "type": "adjective"},
    "querida": {"en": "dear, beloved (feminine of querido)", "type": "adjective"},
    "negra": {"en": "black (feminine of negro)", "type": "adjective"},
    "roja": {"en": "red (feminine of rojo)", "type": "adjective"},
    "extraña": {"en": "strange (feminine of extraño)", "type": "adjective"},
    "guapo": {"en": "handsome, good-looking", "type": "adjective"},
    "cerdo": {"en": "pig, pork", "type": "noun", "gender": "m"},
    "japón": {"en": "Japan", "type": "proper noun"},
    "casas": {"en": "houses (plural of casa)", "type": "noun", "gender": "f"},
    "fuentes": {"en": "fountains, sources (plural of fuente)", "type": "noun", "gender": "f"},
    "pasos": {"en": "steps (plural of paso)", "type": "noun", "gender": "m"},
    "campos": {"en": "fields, countryside (plural of campo)", "type": "noun", "gender": "m"},
    "paredes": {"en": "walls (plural of pared)", "type": "noun", "gender": "f"},
    "números": {"en": "numbers (plural of número)", "type": "noun", "gender": "m"},
    "negros": {"en": "black (masculine plural of negro)", "type": "adjective"},
    "tales": {"en": "such (plural of tal)", "type": "adjective"},
    "ciudadanos": {"en": "citizens (plural of ciudadano)", "type": "noun", "gender": "m"},
}


def download():
    print(f"Downloading {SOURCE_URL} ...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(SOURCE_URL, RAW_CACHE)
    print(f"Downloaded {RAW_CACHE.stat().st_size:,} bytes")


def parse_block(block):
    """Parse one headword block into every usable (pos, gender, gloss)
    sense it contains — one entry per pos block, taking that block's first
    gloss unless a later gloss in the same block is scored better (see
    below). Returns (word, senses) with senses possibly empty, or None if
    the block itself is unusable (blank/missing headword line).

    Each sense carries a score used to pick the best one across pos blocks
    in build_dictionary(): 0 normal, 1 the picked gloss turned out to be
    tagged rare and a later gloss in the same block wasn't, 2 the "name of
    this letter of the alphabet" sense (see LETTER_GLOSS_RE) — almost never
    what a learner means, but not skip-listed outright because some
    headwords (the letters themselves) have nothing else to offer."""
    lines = block.split("\n")
    if not lines or not lines[0].strip():
        return None
    word = lines[0].strip()

    senses = []
    pos = gender = gloss = score = None

    def flush():
        if pos and gloss:
            senses.append((pos, gender, gloss, score))

    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("pos:"):
            flush()
            pos = gender = gloss = score = None
            raw_pos = stripped[4:].strip()
            if raw_pos in SKIP_POS:
                pos = None
                continue
            pos = POS_MAP.get(raw_pos, raw_pos)
        elif stripped.startswith("g:") and gender is None and pos:
            gender = stripped[2:].strip() or None
        elif stripped.startswith("gloss:") and pos:
            candidate = stripped[len("gloss:"):].strip()
            candidate_score = 2 if LETTER_GLOSS_RE.search(candidate) else 0
            if gloss is None or candidate_score < score:
                gloss = candidate
                score = candidate_score
        elif stripped.startswith("q:") and pos and gloss is not None and score == 0 \
                and RARE_RE.search(stripped):
            score = 1  # demote so a later, untagged gloss in this block can win

    flush()
    return word, senses


def build_dictionary():
    text = RAW_CACHE.read_text(encoding="utf-8")
    blocks = text.split("_____\n")

    # Collect every parsed entry first rather than picking "first occurrence
    # wins" while streaming — the source sorts case-sensitively, so a
    # capitalized proper-noun block (e.g. "Bueno", the surname) can appear
    # before the far more useful lowercase common-word block ("bueno", the
    # adjective). Preferring the entry whose headword is already lowercase
    # avoids common words getting shadowed by incidental capitalized
    # homographs.
    candidates = {}
    skipped = 0
    for block in blocks:
        parsed = parse_block(block)
        if not parsed or not parsed[1]:
            skipped += 1
            continue
        word, senses = parsed
        key = word.lower()
        is_lowercase_headword = (word == key)
        candidates.setdefault(key, []).append((is_lowercase_headword, word, senses))

    dictionary = {}
    for key, entries in candidates.items():
        entries.sort(key=lambda e: not e[0])  # lowercase-headword entries first
        _, word, senses = entries[0]
        # Lowest score wins; min() is stable so among equal scores the
        # earliest pos block in the source still wins, same as before.
        pos, gender, gloss, _ = min(senses, key=lambda s: s[3])
        entry = {"en": gloss, "type": pos}
        if gender:
            entry["gender"] = gender
        dictionary[key] = entry

    for key, override in MANUAL_OVERRIDES.items():
        dictionary[key] = override

    return dictionary, skipped


def main():
    if not RAW_CACHE.exists():
        download()
    else:
        print(f"Reusing cached {RAW_CACHE} ({RAW_CACHE.stat().st_size:,} bytes)")

    dictionary, skipped = build_dictionary()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

    raw_size = OUTPUT_FILE.stat().st_size
    print(f"Entries:   {len(dictionary):,} (skipped {skipped:,} — no usable pos/gloss)")
    print(f"Output:    {OUTPUT_FILE} ({raw_size:,} bytes, {raw_size/1024/1024:.2f} MB)")
    print(f"Cache:     {RAW_CACHE} kept for reuse — delete it to force a fresh download")


if __name__ == "__main__":
    main()
