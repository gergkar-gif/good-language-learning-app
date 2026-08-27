#!/usr/bin/env python3
"""
Build a Spanish/English sentence-pair pool for Workshop's Translation Driller
(and the Context mode of the Vocabulary Driller, which samples the same pool
for sentences containing a given word).

Two sources, both already authored for other purposes:
  - content/<lang>/grammar/**/*.json  -- every `examples` part's
    {spanish, english} pairs (the worked examples on a grammar screen; the
    "spanish" key just means "target language" — reused as-is for Hungarian).
  - content/<lang>/exercises/**/*.json -- `sentence-builder` exercises that
    carry an `english` field (most of them do; a few omit it and are
    skipped).

Output: content/<lang>/indexes/translation-index.json
    { "pairs": [ { spanish, english, level, source, topic? }, ... ] }

`level` is the a1/a2/... directory each file already lives in -- content is
organised one directory per level, so no per-file field to read.

`topic` (added 2026-08-27, for the Translation Driller's "practice by topic"
mode) is derived per source file, three ways depending on how that file is
named -- content grew several different filename conventions over time, not
one:
  - Slug filenames ({level}-{slug}-{lesson|consolidation}...), e.g.
    "a1-hobbies-03-..." or "b1-nacionalismo-03-...": the slug already *is*
    the topic (English ones already read fine; the 36 Spanish LatAm-history
    slugs from B1's cultural track get a hand-written label in
    SLUG_TOPIC_LABELS below).
  - Numeric unit filenames ({level}-{unit:2d}-{lesson:2d}-...), e.g.
    "a1-01-02-ser-..." — most of ES: looked up against curriculum.json's
    `unit.<level>.<NN>` ids for that unit's title.
  - Numeric lesson-across-level filenames ({level}-{lesson}-{variant}...),
    e.g. "a1-130-b-..." — all of HU (currently A1-only): HU's curriculum
    numbers lessons sequentially across the whole level rather than
    restarting per unit (`lesson.<level>.<NN>`, no unit segment in the id at
    all), so a HU file's lesson number is looked up against *that* id shape
    instead, walking each unit's lessons to find which unit it belongs to.
A handful of files (B1's five irregular "03c" grammar screens and their
exercise siblings) match none of the three and simply get no topic — they
still appear in the driller, just not under any topic filter.

Usage:
    python scripts/build_translation_index.py [lang ...]   (default: es hu)
"""
import json
import re
import sys
from pathlib import Path

_PUNCTUATION_TILE = re.compile(r"^[,.!?;:]+$")

# Slugs seen in content filenames that aren't already a usable English label
# on their own. The 8 A1 entries are already English and pass through
# unchanged (still listed for completeness/documentation); the 36 B1 entries
# are the LatAm cultural-history track's Spanish topic names.
SLUG_TOPIC_LABELS = {
    "cafe": "At the Café",
    "directions": "Directions",
    "future": "Future Plans",
    "health": "Health",
    "hobbies": "Hobbies",
    "kitchen": "In the Kitchen",
    "weather": "Weather",
    "work": "Work & Study",
    "americalatinadosmil": "Latin America in the 2000s",
    "cambiosocial": "Social Change",
    "caudillismo": "Caudillismo",
    "centroamerica": "Central America",
    "civilizaciones": "Pre-Columbian Civilizations",
    "conosur": "The Southern Cone",
    "conquista": "The Conquest",
    "crisisdeuda": "The Debt Crisis",
    "democratizacion": "Democratization",
    "economiacolonial": "Colonial Economy",
    "economiasexportacion": "Export Economies",
    "eeuu": "The United States",
    "finalguerrafria": "End of the Cold War",
    "gobiernosmilitares": "Military Governments",
    "grandepresion": "The Great Depression",
    "guerrafria": "The Cold War",
    "independencia": "Independence",
    "industrializacion": "Industrialization",
    "integracionregional": "Regional Integration",
    "latamnoventa": "Latin America in the 1990s",
    "legadosigloveinte": "20th-Century Legacy",
    "liberalismomodernizacion": "Liberalism & Modernization",
    "llegadaeuropeos": "Arrival of the Europeans",
    "movimientosindigenas": "Indigenous Movements",
    "nacionalismo": "Nationalism",
    "nacionnacionalismo": "Nation & Nationalism",
    "neoliberalismo": "Neoliberalism",
    "nuevasrepublicas": "New Republics",
    "populismo": "Populism",
    "precolombina": "Pre-Columbian Era",
    "razaclasepoder": "Race, Class & Power",
    "represionpolitica": "Political Repression",
    "revolucion": "Revolution",
    "revolucioncubana": "The Cuban Revolution",
    "revolucionmexicana": "The Mexican Revolution",
    "sociedadcolonial": "Colonial Society",
}

# Order matters: these are mutually exclusive by construction (slug requires
# letters where the numeric patterns require digits), but slug is tried
# first regardless since it's the most specific match.
_SLUG_RE = re.compile(r"^[abc]\d-([a-z]+)-(?:\d+|consolidation)")
_UNIT_RE = re.compile(r"^[abc]\d-(\d{2})-(?:\d{2}-|consolidation)")
_LESSON_ACROSS_LEVEL_RE = re.compile(r"^[abc]\d-(\d+)-")


def _join_tiles(tiles):
    """Join sentence-builder tiles into one sentence. A tile that's pure
    punctuation (",", ".", "?", ...) attaches directly to the previous word
    instead of getting its own leading space — plain " ".join(tiles) used to
    produce "Tegnap tanultam ." for any exercise that tiles punctuation
    separately, which most Hungarian ones do."""
    out = []
    for tile in tiles:
        if out and _PUNCTUATION_TILE.match(tile):
            out[-1] += tile
        else:
            out.append(tile)
    return " ".join(out)


def _load_curriculum_lookups(lang):
    """Two lookups out of content/<lang>/curriculum/curriculum.json, keyed
    (LEVEL, number) -> unit title:
      - by_unit_num: from each unit's own `unit.<level>.<NN>` id.
      - by_lesson_num: from each lesson's `lesson.<level>.<NN>` id (only
        present where a course numbers lessons across the whole level
        rather than restarting per unit — currently just HU)."""
    path = Path(f"content/{lang}/curriculum/curriculum.json")
    if not path.is_file():
        return {}, {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}, {}

    by_unit_num = {}
    by_lesson_num = {}
    for level_key, level in data.get("levels", {}).items():
        for unit in level.get("units", []):
            title = unit.get("title", "")
            # B1 units carry a third "track" id segment (unit.b1.core.05,
            # unit.b1.latam.32) since it's dual-track — core and latam each
            # number 1-36, so bare numbers collide between them. Numeric
            # filenames only ever belong to core (latam's are the slug
            # filenames handled by SLUG_TOPIC_LABELS instead), so only
            # "core" (or no track segment at all, i.e. A1/A2) is registered
            # here; latam is deliberately left out to avoid that collision.
            m = re.match(r"unit\.[a-z]\d\.(?:core\.)?(\d+)$", unit.get("id", ""))
            if m:
                by_unit_num[(level_key, int(m.group(1)))] = title
            for lesson in unit.get("lessons", []):
                m2 = re.match(r"lesson\.[a-z]\d\.(\d+)$", lesson.get("id", ""))
                if m2:
                    by_lesson_num[(level_key, int(m2.group(1)))] = title
    return by_unit_num, by_lesson_num


def _topic_for(stem, level, by_unit_num, by_lesson_num):
    m = _SLUG_RE.match(stem)
    if m:
        return SLUG_TOPIC_LABELS.get(m.group(1))

    m = _UNIT_RE.match(stem)
    if m:
        topic = by_unit_num.get((level, int(m.group(1))))
        if topic:
            return topic

    m = _LESSON_ACROSS_LEVEL_RE.match(stem)
    if m:
        return by_lesson_num.get((level, int(m.group(1))))

    return None


def from_grammar(grammar_dir, by_unit_num, by_lesson_num):
    pairs = []
    for f in sorted(grammar_dir.glob("*/*.json")):
        level = f.parent.name.upper()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        topic = _topic_for(f.stem, level, by_unit_num, by_lesson_num)
        for section in data.get("sections", []):
            if section.get("type") != "examples":
                continue
            for item in section.get("items", []):
                spanish = item.get("spanish")
                english = item.get("english")
                if spanish and english:
                    pair = {"spanish": spanish, "english": english, "level": level, "source": "grammar"}
                    if topic:
                        pair["topic"] = topic
                    pairs.append(pair)
    return pairs


def from_exercises(exercises_dir, by_unit_num, by_lesson_num):
    pairs = []
    for f in sorted(exercises_dir.glob("*/*.json")):
        level = f.parent.name.upper()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        topic = _topic_for(f.stem, level, by_unit_num, by_lesson_num)
        for ex in data.get("exercises", []):
            if ex.get("type") != "sentence-builder":
                continue
            english = ex.get("english")
            solution = ex.get("solution")
            if english and solution:
                pair = {"spanish": _join_tiles(solution), "english": english, "level": level, "source": "exercises"}
                if topic:
                    pair["topic"] = topic
                pairs.append(pair)
    return pairs


def main():
    langs = sys.argv[1:] or ["es", "hu"]

    for lang in langs:
        grammar_dir = Path(f"content/{lang}/grammar")
        exercises_dir = Path(f"content/{lang}/exercises")
        if not grammar_dir.is_dir() and not exercises_dir.is_dir():
            print(f"[{lang}] no grammar/exercises dirs, skipping")
            continue

        by_unit_num, by_lesson_num = _load_curriculum_lookups(lang)
        pairs = (
            from_grammar(grammar_dir, by_unit_num, by_lesson_num)
            + from_exercises(exercises_dir, by_unit_num, by_lesson_num)
        )

        output_dir = Path(f"content/{lang}/indexes")
        output_file = output_dir / "translation-index.json"
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"pairs": pairs}, f, ensure_ascii=False, separators=(",", ":"))

        by_level = {}
        for p in pairs:
            by_level[p["level"]] = by_level.get(p["level"], 0) + 1
        with_topic = sum(1 for p in pairs if p.get("topic"))
        topic_count = len({p["topic"] for p in pairs if p.get("topic")})

        raw_size = output_file.stat().st_size
        print(f"[{lang}] Pairs total:  {len(pairs)}")
        print(f"[{lang}] By level:     {dict(sorted(by_level.items()))}")
        print(f"[{lang}] With topic:   {with_topic}/{len(pairs)} ({topic_count} distinct topics)")
        print(f"[{lang}] Output:       {output_file} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
