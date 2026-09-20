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
    { "pairs": [ { spanish, english, level, source, topic?, track? }, ... ] }

`track` (added 2026-09-04, for the Translation Driller's dual-track split;
generalized across languages 2026-09-09) is only ever set to "core" or the
language's own second-track name (see _SLUG_TRACK_NAME), and only for B1 --
the one level that's dual-track today. ES B1 pairs its regular
grammar-progression "core" track with a cultural-history "latam" track; HU
B1 pairs the same "core" shape with a citizenship-exam "citizenship" track
-- each numbered 1-36 independently within its language. It's derived the
same way `topic` is: a slug filename means the language's second-track
name, a numeric unit/lesson filename means "core". Every other level has no
dual track, so its pairs simply carry no `track` key at all -- the driller
treats "no track" as "core" rather than requiring every non-dual-track
course to be retrofitted with the field. The pattern (a per-pair `track`,
absent unless a level genuinely has more than one) is meant to be reused
as-is for any future dual-track content.

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
    "orszagma": "Hungary Today: Land & Symbols",
    "karpatmedence": "The Carpathian Basin Before the Magyars",
    "honfoglalas": "The Honfoglalás (895)",
    "istvankiraly": "Saint Stephen & the Founding of the State (1000)",
    "arpadhaz": "The Árpád Dynasty",
    "tatarjaras": "The Mongol Invasion (1241–42)",
    "anjouk": "The Angevin & Later Medieval Kings",
    "matyas": "Matthias Corvinus & the Renaissance Court",
    "mohacs": "The Battle of Mohács (1526)",
    "haromresz": "Three Parts of Hungary",
    "erdelyaranykora": "Transylvania's Golden Age",
    "torokkiuzese": "Driving Out the Ottomans",
    "rakoczi": "Rákóczi's War of Independence (1703–11)",
    "mariaterezia": "The 18th Century: Rebuilding",
    "reformkor": "The Reform Age",
    "szabadsagharc": "The 1848–49 Revolution",
    "kiegyezes": "The 1867 Compromise & Dualism",
    "millennium": "The Millennium & Turn of the Century",
    "elsovh": "World War I & the Revolutions",
    "trianon": "The Treaty of Trianon (1920)",
    "horthykorszak": "The Interwar Years",
    "masodikvh": "World War II in Hungary",
    "rakosikorszak": "The Communist Takeover & Rákosi Era",
    "otvenhat": "The 1956 Revolution",
    "kadarkorszak": "The Kádár Era & Goulash Communism",
    "rendszervaltas": "The Regime Change: From Communism to Democracy",
    "demokracia": "Modern Democratic Hungary & Euro-Atlantic Integration",
    "nemzetijelkepek": "National Symbols",
    "nemzetiunnepek": "National Holidays & Remembrance Days",
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


# Each dual-track level's second (slug-named) track, keyed by language --
# ES B1 pairs its grammar-progression "core" track with a cultural-history
# "latam" track; HU B1 pairs the same "core" shape with a citizenship-exam
# "citizenship" track (chronological history + civics, same slug-filename
# convention as LatAm). A language with no dual-track content simply has no
# entry here, and _track_for returns None for it same as for non-B1 levels.
_SLUG_TRACK_NAME = {
    "es": "latam",
    "hu": "citizenship",
}


def _track_for(stem, level, lang):
    """The slug-named second track's own name (see _SLUG_TRACK_NAME) for B1's
    slug-named files, "core" for B1's numeric-unit files, None everywhere
    else -- only B1 is dual-track today. A1 also has a handful of slug
    filenames (see SLUG_TOPIC_LABELS' "8 A1 entries"), but those are just
    A1's own topic-naming convention, not a second track, so this
    deliberately only fires for B1."""
    if level != "B1":
        return None
    if _SLUG_RE.match(stem):
        return _SLUG_TRACK_NAME.get(lang)
    if _UNIT_RE.match(stem) or _LESSON_ACROSS_LEVEL_RE.match(stem):
        return "core"
    return None


def _load_known_skills(lang):
    path = Path(f"content/{lang}/indexes/grammar-index.json")
    if not path.is_file():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return set(data.get("bySkill", {}).keys())
    except (json.JSONDecodeError, OSError):
        return set()


def _skills_for_grammar(stem, known_skills):
    if not known_skills:
        return []
    clean = stem.replace("-gr", "")
    if clean in known_skills:
        return [clean]
    parts = clean.split("-")
    if len(parts) >= 4:
        suffix = "-".join(parts[3:])
        if suffix in known_skills:
            return [suffix]
    matches = [s for s in known_skills if clean.endswith(f"-{s}")]
    if matches:
        return [max(matches, key=len)]
    return []


def from_grammar(grammar_dir, by_unit_num, by_lesson_num, lang, known_skills):
    pairs = []
    for f in sorted(grammar_dir.glob("*/*.json")):
        level = f.parent.name.upper()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        topic = _topic_for(f.stem, level, by_unit_num, by_lesson_num)
        track = _track_for(f.stem, level, lang)
        skills = _skills_for_grammar(f.stem, known_skills)
        base_id = data.get("id") or f.stem
        for section in data.get("sections", []):
            if section.get("type") != "examples":
                continue
            for idx, item in enumerate(section.get("items", [])):
                spanish = item.get("spanish")
                english = item.get("english")
                # A grammar screen's contrastive "before -> after" example
                # (e.g. "Compre la flor -> La compre.") demonstrates a
                # transformation for a reader looking at a table; read aloud
                # or translated on its own by the Speaking/Translation
                # Drillers, which reuse this same pool, it's neither a
                # natural sentence nor answerable -- exclude it instead.
                if spanish and "→" in spanish:
                    continue
                if spanish and english:
                    pair = {
                        "id": f"{base_id}#{idx}",
                        "spanish": spanish,
                        "english": english,
                        "level": level,
                        "source": "grammar"
                    }
                    if skills:
                        pair["skillIds"] = skills
                    if topic:
                        pair["topic"] = topic
                    if track:
                        pair["track"] = track
                    pairs.append(pair)
    return pairs


def from_exercises(exercises_dir, by_unit_num, by_lesson_num, lang):
    pairs = []
    for f in sorted(exercises_dir.glob("*/*.json")):
        level = f.parent.name.upper()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        topic = _topic_for(f.stem, level, by_unit_num, by_lesson_num)
        track = _track_for(f.stem, level, lang)
        for ex in data.get("exercises", []):
            if ex.get("type") != "sentence-builder":
                continue
            english = ex.get("english")
            solution = ex.get("solution")
            if english and solution:
                pair = {
                    "spanish": _join_tiles(solution),
                    "english": english,
                    "level": level,
                    "source": "exercises"
                }
                ex_id = ex.get("id")
                if ex_id:
                    pair["id"] = ex_id
                teaches = ex.get("teaches")
                if teaches:
                    pair["skillIds"] = teaches
                if topic:
                    pair["topic"] = topic
                if track:
                    pair["track"] = track
                pairs.append(pair)
    return pairs


def from_backfill(backfill_dir):
    pairs = []
    if not backfill_dir.is_dir():
        return pairs
    for f in sorted(backfill_dir.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            items = data if isinstance(data, list) else data.get("sentences", [])
            for it in items:
                sp = it.get("spanish") or it.get("hungarian") or it.get("target") or it.get("sentence")
                en = it.get("english") or it.get("translation")
                lvl = (it.get("level") or "A1").upper()
                if sp and en:
                    pair = {
                        "spanish": sp,
                        "english": en,
                        "level": lvl,
                        "source": "backfill"
                    }
                    if it.get("topic"):
                        pair["topic"] = it["topic"]
                    pairs.append(pair)
        except (json.JSONDecodeError, OSError):
            continue
    return pairs


def main():
    langs = sys.argv[1:] or ["es", "hu"]

    for lang in langs:
        grammar_dir = Path(f"content/{lang}/grammar")
        exercises_dir = Path(f"content/{lang}/exercises")
        backfill_dir = Path(f"content/{lang}/backfill_sentences")
        if not grammar_dir.is_dir() and not exercises_dir.is_dir() and not backfill_dir.is_dir():
            print(f"[{lang}] no grammar/exercises/backfill dirs, skipping")
            continue

        by_unit_num, by_lesson_num = _load_curriculum_lookups(lang)
        known_skills = _load_known_skills(lang)
        pairs = (
            from_grammar(grammar_dir, by_unit_num, by_lesson_num, lang, known_skills)
            + from_exercises(exercises_dir, by_unit_num, by_lesson_num, lang)
            + from_backfill(backfill_dir)
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
        by_track = {}
        for p in pairs:
            if p.get("track"):
                by_track[p["track"]] = by_track.get(p["track"], 0) + 1

        raw_size = output_file.stat().st_size
        print(f"[{lang}] Pairs total:  {len(pairs)}")
        print(f"[{lang}] By level:     {dict(sorted(by_level.items()))}")
        print(f"[{lang}] With topic:   {with_topic}/{len(pairs)} ({topic_count} distinct topics)")
        if by_track:
            print(f"[{lang}] By track:     {dict(sorted(by_track.items()))}")
        print(f"[{lang}] Output:       {output_file} ({raw_size:,} bytes)")


if __name__ == "__main__":
    main()
