#!/usr/bin/env python3
"""
Build a flat, course-wide index of every grammar topic for the Grammar
Guide's global search (engine/curriculum.js's globalGrammarGuideHtml()).

Walking every unit's lessons live in the browser (collectUnitGrammarTopics())
is exactly what the per-unit Grammar Guide already does, and is fine at that
scale (~6 lessons). Doing it for every unit in the whole course on every
search-screen open is not: a full course runs to 100+ units, each with its
own lesson + grammar-section fetches, which fans out to hundreds of
individual requests. This script does that walk once at build time instead,
mirroring loadLesson()'s id -> path resolution (engine/lessons.js) and
collectUnitGrammarTopics()'s section-walk (engine/curriculum.js) exactly, so
the two never teach a different topic list for the same unit.

Output: content/<lang>/indexes/grammar-guide-index.json
    [ { "level": "A1", "unitId": "unit.a1.01", "unitTitle": "...",
        "title": "...", "keywords": "..." }, ... ]

`keywords` lets the search find a topic in either language whatever
language its title is in: English from the topic id and section headings,
target-language forms from the *italicised* terms in its explanation
(house style italicises every embedded target-language word). Full prose
and examples are left out on purpose, or "verb" would match everything.

A topic's own words only find it in the language it happens to use, so
GRAMMAR_TERM_SYNONYMS bridges grammar terms: a topic that mentions any term
of a group also gets the rest of the group in its keywords ("subjunctive"
topics become findable by "subjuntivo" and the other way round).

Usage:
    python scripts/build_grammar_guide_index.py [lang ...]   (default: es hu)
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

# Word- or phrase-sized italics only; italicised whole sentences add bulk
# to the index without making anything findable that its words don't.
ITALIC = re.compile(r"\*([^*\n]{1,30})\*")

# Per language family (es-es and es-latam share "es"). A term matches at the
# start of a word, accent- and case-insensitively, so "pronoun" also covers
# "pronouns". Keep every group to terms that mean the same thing.
GRAMMAR_TERM_SYNONYMS = {
    "es": [
        ["subjunctive", "subjuntivo"],
        ["preterite", "pretérito indefinido", "pretérito perfecto simple", "simple past"],
        ["present perfect", "pretérito perfecto compuesto"],
        ["imperfect", "imperfecto"],
        ["pluperfect", "past perfect", "pluscuamperfecto"],
        ["conditional", "condicional"],
        ["future", "futuro"],
        ["imperative", "imperativo"],
        ["direct object", "objeto directo", "complemento directo"],
        ["indirect object", "objeto indirecto", "complemento indirecto"],
        ["reflexive", "reflexivo"],
        ["gerund", "gerundio"],
        ["participle", "participio"],
        ["passive", "pasiva"],
        ["relative pronoun", "pronombre relativo"],
        ["comparative", "comparativo"],
        ["superlative", "superlativo"],
        ["infinitive", "infinitivo"],
        ["article", "artículo"],
        ["pronoun", "pronombre"],
        ["adjective", "adjetivo"],
        ["adverb", "adverbio"],
        ["preposition", "preposición"],
        ["possessive", "posesivo"],
        ["demonstrative", "demostrativo"],
    ],
    "hu": [
        ["accusative", "tárgyeset"],
        ["dative", "részes eset"],
        ["possessive", "birtokos"],
        ["imperative", "felszólító mód"],
        ["conditional", "feltételes mód"],
        ["past tense", "múlt idő"],
        ["future", "jövő idő"],
        ["present tense", "jelen idő"],
        ["definite conjugation", "határozott ragozás", "tárgyas ragozás"],
        ["indefinite conjugation", "határozatlan ragozás", "alanyi ragozás"],
        ["preverb", "verbal prefix", "igekötő"],
        ["postposition", "névutó"],
        ["plural", "többes szám"],
        ["vowel harmony", "hangrendi illeszkedés"],
        ["infinitive", "főnévi igenév"],
        ["participle", "melléknévi igenév"],
        ["adverbial participle", "határozói igenév"],
        ["causative", "műveltető"],
        ["comparative", "középfok"],
        ["superlative", "felsőfok"],
        ["adjective", "melléknév"],
        ["pronoun", "névmás"],
        ["article", "névelő"],
    ],
}


def _norm(text):
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^\w\s]", " ", text).split())


def add_term_synonyms(lang, title, keywords):
    haystack = " " + _norm(title + " " + keywords)
    extra = []
    for group in GRAMMAR_TERM_SYNONYMS.get(lang.split("-")[0], []):
        if any(" " + _norm(t) in haystack for t in group):
            extra += [t for t in group if " " + _norm(t) not in haystack]
    return " · ".join([keywords] + extra if keywords else extra)


def topic_keywords(grammar):
    # "grammar.b1.08.01.future-intention" -> "future intention"; ids ending
    # in a bare letter or number ("grammar.a1.01.b") carry no words.
    slug = grammar.get("id", "").rsplit(".", 1)[-1]
    terms = [slug.replace("-", " ")] if len(slug) > 2 and not slug.isdigit() else []
    for section in grammar.get("sections", []):
        if section.get("title"):
            terms.append(section["title"].replace("*", ""))
        if isinstance(section.get("content"), str):
            terms += ITALIC.findall(section["content"])
    seen, out = set(), []
    for t in (t.strip() for t in terms):
        if t and t.lower() not in seen:
            seen.add(t.lower())
            out.append(t)
    return " · ".join(out)


def lesson_path(lang, lesson_id):
    # Mirrors loadLesson() in engine/lessons.js exactly.
    parts = lesson_id[len("lesson."):].split(".") if lesson_id.startswith("lesson.") else lesson_id.split(".")
    level = parts[0]
    rest = "-".join(parts[1:])
    return Path(f"content/{lang}/lessons/{level}/{level}-{rest}.json")


def build_index(lang, curriculum):
    index = []
    stats = {"units": 0, "lessons_missing": 0, "grammar_missing": 0}

    for level_key, level_data in curriculum.get("levels", {}).items():
        for unit in level_data.get("units", []):
            stats["units"] += 1
            for lesson_ref in unit.get("lessons", []):
                lf = lesson_path(lang, lesson_ref["id"])
                if not lf.is_file():
                    stats["lessons_missing"] += 1
                    continue
                try:
                    lesson = json.loads(lf.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, OSError):
                    stats["lessons_missing"] += 1
                    continue

                for section in lesson.get("sections", []):
                    if section.get("type") != "grammar" or not section.get("ref"):
                        continue
                    gf = Path(f"content/{lang}") / section["ref"]
                    title = section.get("title", "Grammar")
                    keywords = ""
                    if gf.is_file():
                        try:
                            grammar = json.loads(gf.read_text(encoding="utf-8"))
                            title = grammar.get("title") or title
                            keywords = topic_keywords(grammar)
                        except (json.JSONDecodeError, OSError):
                            stats["grammar_missing"] += 1
                    else:
                        stats["grammar_missing"] += 1

                    index.append({
                        "level": level_key,
                        "unitId": unit["id"],
                        "unitTitle": unit.get("title", ""),
                        "title": title,
                        "keywords": add_term_synonyms(lang, title, keywords)
                    })

    return index, stats


def main():
    langs = sys.argv[1:] or sorted(p.name for p in Path("content").iterdir() if p.is_dir())  # every course folder

    for lang in langs:
        curriculum_path = Path(f"content/{lang}/curriculum/curriculum.json")
        if not curriculum_path.is_file():
            print(f"[{lang}] no curriculum.json, skipping")
            continue

        curriculum = json.loads(curriculum_path.read_text(encoding="utf-8"))
        index, stats = build_index(lang, curriculum)

        output_dir = Path(f"content/{lang}/indexes")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / "grammar-guide-index.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

        print(f"[{lang}] {len(index)} grammar topics across {stats['units']} units "
              f"-> {output_file} ({output_file.stat().st_size} bytes)"
              + (f"  [{stats['lessons_missing']} lessons, {stats['grammar_missing']} grammar files unresolved]"
                 if stats["lessons_missing"] or stats["grammar_missing"] else ""))


if __name__ == "__main__":
    main()
