#!/usr/bin/env python3
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(".")
BASE_STORIES = Path("content")
BASE_LESSONS = Path("content")

CATEGORIES = ["original", "classics", "world", "current"]
SKIP_FILENAMES = {"manifest.json", "lessons-manifest.json"}

def build_stories(lang="es", ref_to_unit=None):
    stories = []
    lang_path = BASE_STORIES / lang / "stories"
    if not lang_path.exists():
        return stories
    ref_to_unit = ref_to_unit or {}

    for cat in CATEGORIES:
        cat_path = lang_path / cat
        if not cat_path.exists():
            continue
        # rglob: story files live nested under a level folder,
        # e.g. content/es/stories/original/a1/a1-01.json
        for f in sorted(cat_path.rglob("*.json")):
            if f.name in SKIP_FILENAMES:
                continue
            try:
                with open(f, "r", encoding="utf-8") as fh:
                    data = json.load(fh)
            except (OSError, json.JSONDecodeError):
                continue

            # A story's own "type" field (e.g. "classic"/"original") says what
            # it actually is; the folder it lives in only says the default for
            # files that don't specify one. Stories were being shelved by
            # folder alone, so every file under stories/classics/ showed up
            # under "Classics" even where its own type field said "original".
            file_type = data.get("type")
            if file_type == "classic":
                file_type = "classics"
            story_type = file_type if file_type in CATEGORIES else cat

            # A lesson's own `story` section ref is relative to
            # content/{lang}/ ("stories/classics/b1/..."), one directory up
            # from this file's own `path` below (relative to
            # content/{lang}/stories/) -- prefix it back on to look up.
            rel_path = f.relative_to(lang_path).as_posix()
            unit = ref_to_unit.get("stories/" + rel_path)

            summary = data.get("summary") or data.get("description") or ""
            author = data.get("author") or ""
            work = data.get("work") or ""

            raw_topics = data.get("vocabularyTopics", []) + data.get("topics", []) + data.get("grammar", []) + data.get("tags", [])
            clean_topics = []
            seen_topics = set()
            for t in raw_topics:
                if isinstance(t, str) and t.strip():
                    t_str = t.strip()
                    if t_str.lower() not in seen_topics:
                        seen_topics.add(t_str.lower())
                        clean_topics.append(t_str)

            # Extract distinct thematic keywords from paragraphs
            paras = data.get("paragraphs", [])
            para_texts = [p.get("text", "") for p in paras if isinstance(p, dict)]
            if not para_texts and "text" in data and isinstance(data["text"], str):
                para_texts = [data["text"]]
            full_text = " ".join(para_texts)

            words = re.findall(r'[\wáéíóúüñöüóőúűí]+', full_text.lower(), re.UNICODE)
            stop_words = {
                'para', 'como', 'pero', 'este', 'esta', 'estos', 'estas', 'todo', 'toda',
                'todos', 'todas', 'sobre', 'entre', 'hacer', 'tener', 'estar', 'cuando',
                'donde', 'porque', 'aunque', 'después', 'despues', 'también', 'tambien',
                'hogy', 'volt', 'nem', 'mint', 'vagy', 'csak', 'mert', 'után', 'utan', 'pedig'
            }
            keywords = []
            seen_kw = set()
            for w in words:
                if len(w) >= 4 and w not in stop_words and w not in seen_kw:
                    seen_kw.add(w)
                    keywords.append(w)
                    if len(keywords) >= 80:
                        break

            entry = {
                "id": data.get("id", f"story.{cat}.{f.stem}"),
                "title": data.get("title", f.stem),
                "level": data.get("level", "Unknown"),
                "lesson": data.get("lesson"),
                "type": story_type,
                "source": story_type,
                # relative to content/{lang}/stories/, matching what
                # Content.story() fetches: content/{lang}/stories/${path}
                "path": rel_path,
                "estimatedMinutes": data.get("estimatedMinutes"),
                "characters": data.get("characters", []),
                "location": data.get("location"),
                # Which unit this story is taught in, for the reader's
                # "this is the reading for Level X, Unit Y" line -- None
                # for a story no lesson currently links to (e.g. an old
                # original kept in the library after a classics rewrite).
                # See _story_unit_index()/_apply_story_unit_families().
                "unit": unit
            }
            if summary:
                entry["summary"] = summary
            if author:
                entry["author"] = author
            if work:
                entry["work"] = work
            if clean_topics:
                entry["topics"] = clean_topics
            if keywords:
                entry["keywords"] = keywords
            if data.get("narration"):
                entry["hasAudio"] = True
                if data["narration"].get("durationSeconds"):
                    entry["audioDuration"] = data["narration"].get("durationSeconds")

            stories.append(entry)

    _apply_story_unit_families(stories)
    return stories

LEVEL_META = {
    "a1": {"title": "Fundamentals", "description": "Survival skills"},
    "a2": {"title": "Basic", "description": "Manage basic interactions"},
    "b1": {"title": "Intermediate", "description": "Express opinions, handle complex topics"},
    "b2": {"title": "Upper Intermediate", "description": "Complex arguments, abstract topics"},
    "c1": {"title": "Advanced", "description": "Fluency. Politics, philosophy, art, science"}
}

CURRICULUM_META = {
    "es": {"id": "curriculum.spanish.dele-a1-c1", "title": "Spanish — DELE aligned"},
    "hu": {"id": "curriculum.hungarian.a1-c1", "title": "Hungarian"}
}

# Level -> Unit -> Lesson. A level's unit titles, ordering, and lesson-stem
# grouping are a curriculum decision (which topic sits where) that can't be
# derived from lesson filenames alone, so it lives in
# content/<lang>/curriculum/units/<level>.json (schema:
# content/<lang>/schemas/units.schema.json) -- one file per level that has
# an explicit table, an ordered array of {title, stems, track?}. Adding a
# unit to an already-tabled level means appending one entry to that JSON
# file; no code change needed. A level with no such file falls back to
# auto_group_units() below (plain-numbered lesson files, e.g. Hungarian
# A1/A2, where the grouping really can be derived from disk).
def load_unit_table(lang, level_id):
    """A level's unit table, in order, or None if this lang/level has no
    content/<lang>/curriculum/units/<level_id>.json -- build_curriculum()
    falls back to auto_group_units() in that case."""
    path = Path(f"content/{lang}/curriculum/units/{level_id}.json")
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


# Track metadata for levels that run more than one — id, display title, and
# the order tracks should render in the Learn tab. Keyed by language first,
# same reasoning as the unit tables above: a level absent for this language
# (or a unit table entry with no "track") is single-track, and the
# Learn tab falls back to today's flat unit list. Before 2026-09-09 this was
# keyed by level_id alone, which meant a future language's own B1 dual-track
# would have silently inherited Spanish's "Core Spanish"/"Latin America"
# labels — caught while scoping HU B1's Core/Citizenship tracks.
LEVEL_TRACKS = {
    "es": {
        "b1": [
            {"id": "core", "title": "Core Spanish"},
            {"id": "latam", "title": "Latin America"},
        ],
    },
    "hu": {
        "b1": [
            {"id": "core", "title": "Core Hungarian"},
            {"id": "citizenship", "title": "Citizenship"},
        ],
    },
}

# Unit titles, in order, for a lang/level using auto_group_units() (no
# content/<lang>/curriculum/units/<level>.json). This is the ONE thing auto-grouping can't derive
# from the files themselves — a unit's thematic name ("Greetings & Basic
# Interaction") only ever existed in that content package's own
# UNIT_N_MANIFEST.json, which isn't part of the committed repo. Add one
# title here, in position, when a new unit's lessons land. Forgetting costs
# a generic "Unit N" label (auto_group_units() falls back to that), not a
# unit silently missing lessons or vanishing from the count — unlike the
# old stems-table approach, where a missed/mistyped entry meant
# curriculum.json quietly kept reporting the previous lesson total.
LANG_UNIT_TITLES = {
    "hu": {
        "a1": [
            "Learning to Read Hungarian",
            "Greetings & Basic Interaction",
            "Introducing Yourself",
            "Numbers & Personal Information",
            # Units 5-20 shipped with no UNIT_N_MANIFEST.json (unlike 1-4),
            # so these titles are inferred from each unit's own lesson
            # titles/grammar fields and consolidation goals rather than
            # sourced from the content package itself — check with whoever
            # is generating the content if a more authoritative title exists.
            "Objects & Locations",
            "Family",
            "Describing People",
            "Plurals & Quantities",
            "Possession",
            "Foundations Review",
            "Where Things Are",
            "Going Places",
            "Everyday Actions",
            "Questions & Negation",
            "Daily Routine",
            "Time & Dates",
            "Frequency & Word Order",
            "At Home",
            "Food & Drink",
            "Everyday Hungarian Review",
            # Units 21-30 shipped with real UNIT_N_MANIFEST.json titles.
            "Buying Food",
            "At the Market",
            "At the Café",
            "At the Restaurant",
            "Shopping",
            "Clothes & Appearance",
            "The City",
            "Transport & Directions",
            "Hobbies & Free Time",
            "Friends & Making Plans",
        ],
        "a2": [
            "Daily Life & Routines",
            "Time, Dates & Schedules",
            "Family & Family Life",
            "People & Personality",
            "Friends & Relationships",
            "Home & Housing",
            "Neighbourhood & City",
            "Shopping & Prices",
            "Food & Eating Habits",
            "Cooking",
            "Leisure & Hobbies",
            "Culture & Going Out",
            "Weather & Seasons",
            "Transport & Getting Around",
            "Travel & Holidays",
            "Hotels & Accommodation",
            "Health & the Body",
            "Healthy Living & Advice",
            "School & Language Learning",
            "Review 1: Life, Leisure & Health",
            "Work & Professions",
            "Verb Prefixes",
            "Ability, Possibility & Permission",
            "Talking About the Past I",
            "Talking About the Past II",
            "Telling Stories",
            "Future Plans",
            "Suggestions & Conditional",
            "Opinions, Preferences & Comparisons",
            "Review 2: Work, Past & Opinions",
            "Problems, Requests & Everyday Communication",
            "Living in Hungarian",
        ],
    },
}


def auto_group_units(lang, level_id, level_path):
    """Fallback for a lang/level with no content/<lang>/curriculum/units/<level>.json:
    groups plain-numbered lesson files (a1-06, a1-07, ... — no word-slug ids, no
    multi-track split) into blocks of 5 in numeric order, folding in a
    trailing "{lastlesson}-consolidation" file for that block when one
    exists on disk. Titles come from LANG_UNIT_TITLES by position; running
    past the end of that list yields a generic "Unit N" rather than
    dropping the unit. Returns None (not a real fallback) if no lesson in
    this level matches the plain-numbered pattern at all — a word-slug-id
    level should never have reached here, since every level using those
    already has an explicit units.json, but this keeps that assumption
    from silently producing an empty curriculum if it's ever wrong."""
    plain = []
    for f in sorted(level_path.glob(f"{level_id}-*.json")):
        if f.name in SKIP_FILENAMES:
            continue
        m = re.match(rf"^{re.escape(level_id)}-(\d+)$", f.stem)
        if m:
            plain.append((int(m.group(1)), f.stem))
    if not plain:
        return None
    plain.sort()

    titles = LANG_UNIT_TITLES.get(lang, {}).get(level_id, [])
    units = []
    for block_index, start in enumerate(range(0, len(plain), 5)):
        position = block_index + 1
        chunk = plain[start:start + 5]
        stems = [stem for _, stem in chunk]
        consolidation_stem = f"{chunk[-1][1]}-consolidation"
        if (level_path / f"{consolidation_stem}.json").exists():
            stems.append(consolidation_stem)
        lessons = [e for e in
                   (load_lesson_entry(lang, level_id, level_path, s) for s in stems)
                   if e is not None]
        title = titles[block_index] if block_index < len(titles) else f"Unit {position}"
        units.append({
            "id": f"unit.{level_id}.{position:02d}",
            "label": str(position),
            "title": title,
            "lessons": lessons,
        })
    return units

def lesson_teaching_counts(lang, data):
    """How many new words a lesson introduces, and how many exercises it has
    of each category. My Journey needs these for every lesson at once; without
    them here it would fetch forty content files to draw one screen."""
    base = BASE_LESSONS / lang
    words = 0
    exercises = {}

    for section in data.get("sections", []):
        ref = section.get("ref")
        if not ref:
            continue
        path = base / ref
        if not path.exists():
            continue
        try:
            content = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue

        if section.get("type") == "vocabulary":
            words += len(content.get("words", []))

        elif section.get("type") == "exercise-group":
            by_id = {e.get("id"): e for e in content.get("exercises", [])}
            for ex_id in section.get("exerciseRefs", []):
                exercise = by_id.get(ex_id)
                if not exercise:
                    continue
                category = exercise.get("category", "other")
                exercises[category] = exercises.get(category, 0) + 1

    return words, exercises


def load_lesson_entry(lang, level_id, level_path, stem):
    """One lesson's row for the curriculum index, read from its own file.
    Returns None if the file is missing or broken rather than raising —
    a unit table can name a lesson before its file exists."""
    f = level_path / f"{stem}.json"
    if not f.exists():
        return None
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    new_words, exercise_counts = lesson_teaching_counts(lang, data)
    # The last hyphen segment: "03a" for an unsplit lesson, "01" for a unit
    # part, "consolidation" for the lesson that closes a unit — rsplit rather
    # than split so a1-01-01's label is "01", not "01-01".
    label = stem.rsplit("-", 1)[-1]
    if label == "consolidation":
        label = "Review"
    return {
        "id": data.get("id", f"lesson.{level_id}.{stem}"),
        "label": label,
        "title": data.get("title", stem),
        "grammar": data.get("grammar", ""),
        "goal": data.get("goal", ""),
        # Shown on the lesson row in the Learn tab, so the index carries it
        # rather than fetching every lesson.
        "estimatedMinutes": (data.get("metadata") or {}).get("estimatedMinutes"),
        # Read by My Journey to total up coverage.
        "newWords": new_words,
        "exercises": exercise_counts
    }


def build_curriculum(lang="es"):
    """Build the curriculum.json structure (what the Learn tab actually reads)
    straight from each lesson's own JSON file — lesson files are the single
    source of truth; curriculum.json is a generated index over them.

    Level -> Unit -> Lesson. A level with a content/<lang>/curriculum/units/<level>.json
    is built from that table, in the order given. A level without one falls
    back to auto_group_units(), or to one unit per lesson file in filename
    order if even that doesn't apply, so the shape stays the same everywhere
    even before a level has a real unit plan."""
    lang_path = BASE_LESSONS / lang / "lessons"
    if not lang_path.exists():
        return None

    levels = {}
    for level_id, meta in LEVEL_META.items():
        level_path = lang_path / level_id
        units = []

        if level_path.exists():
            table = load_unit_table(lang, level_id)
            if table:
                # Position is counted per track, not across the whole table,
                # so two tracks each start their own unit numbering at 1
                # rather than interleaving into a single shared sequence.
                track_position = {}
                for entry in table:
                    title, stems, track = entry["title"], entry["stems"], entry.get("track")
                    track_position[track] = track_position.get(track, 0) + 1
                    position = track_position[track]
                    lessons = [e for e in
                               (load_lesson_entry(lang, level_id, level_path, s) for s in stems)
                               if e is not None]
                    unit_id = (f"unit.{level_id}.{track}.{position:02d}" if track
                               else f"unit.{level_id}.{position:02d}")
                    unit = {
                        "id": unit_id,
                        "label": str(position),
                        "title": title,
                        "lessons": lessons
                    }
                    if track:
                        unit["track"] = track
                    units.append(unit)
            else:
                auto_units = auto_group_units(lang, level_id, level_path)
                if auto_units is not None:
                    units = auto_units
                else:
                    for position, f in enumerate(
                            (p for p in sorted(level_path.glob("*.json")) if p.name not in SKIP_FILENAMES),
                            start=1):
                        entry = load_lesson_entry(lang, level_id, level_path, f.stem)
                        if entry is None:
                            continue
                        units.append({
                            "id": f"unit.{level_id}.{position:02d}",
                            "label": str(position),
                            "title": entry["title"],
                            "lessons": [entry]
                        })

        level_entry = {
            "title": meta["title"],
            "description": meta["description"],
            "units": units
        }
        lang_tracks = LEVEL_TRACKS.get(lang, {})
        if level_id in lang_tracks:
            level_entry["tracks"] = lang_tracks[level_id]
        levels[level_id.upper()] = level_entry

    curr_meta = CURRICULUM_META.get(lang, {
        "id": f"curriculum.{lang}.a1-c1",
        "title": f"{lang.upper()} Mastery"
    })

    return {
        "id": curr_meta["id"],
        "title": curr_meta["title"],
        "levels": levels
    }

FREQUENCY_BANDS = [(1, 100), (101, 250), (251, 500), (501, 1000)]

# Where each language's frequency deck sources from. The ranked list and the
# dictionary both have to be for the same language — es's ranks/dictionary
# have always lived in these locations (not under content/es/), while hu's
# ranks were generated straight into content/hu/indexes/ alongside its other
# indexes. Missing entirely for a language just skips its frequency decks,
# the same as a missing file already did before this map existed.
FREQUENCY_SOURCES = {
    "es": (ROOT / "generated" / "indexes" / "frequency.json",
           ROOT / "imports" / "dictionary" / "spanish-en.json"),
    "hu": (ROOT / "content" / "hu" / "indexes" / "frequency.json",
           ROOT / "imports" / "dictionary" / "hungarian-en.json"),
}

# The dictionary's first sense for a handful of very common Spanish words is
# the name of the letter — 'de' glossed as "letter: d" — because that entry
# sorts first. Those are exactly the words a frequency deck opens with, so
# they are given the sense a learner actually needs. Spanish-only: these are
# overrides for specific Spanish dictionary entries, applied by lemma, and a
# handful of them (a, e, o, su, mi, tu...) collide with unrelated Hungarian
# words that happen to share the same spelling.
FREQUENCY_GLOSS = {
    # Letter names, where the dictionary's first sense is the letter itself.
    "de": "of, from", "a": "to, at", "y": "and", "o": "or", "e": "and",
    "ese": "that", "del": "of the", "al": "to the", "u": "or",
    # Grammatical descriptions, where the dictionary names the part of speech
    # instead of translating it — accurate for a dictionary, useless on a card.
    "el": "the", "la": "the", "lo": "it, the", "los": "the", "las": "the",
    "un": "a, an", "una": "a, an", "unos": "some", "unas": "some",
    "yo": "I", "se": "himself, herself, itself", "me": "me, myself",
    "te": "you, yourself", "nos": "us, ourselves", "le": "him, her, to them",
    "su": "his, her, their", "mi": "my", "tu": "your",
}

# A gloss that begins like this is describing the word rather than translating
# it, and makes a useless flashcard.
JUNK_GLOSS = re.compile(
    r"^(letter|abbreviation|obsolete|pronunciation spelling|alternative form"
    r"|apocopic|misspelling|eye dialect|initialism|acronym)", re.I)


def _strip_balanced(text, open_ch, close_ch):
    r"""Remove every top-level open_ch...close_ch span, including anything
    nested inside it.

    A naive `re.sub(r"\([^)]*\)", ...)` only eats up to the *first* close_ch
    it finds — on a gloss with real nesting ("dog (# ... (sometimes ...),
    domesticated ...)") that first close_ch belongs to the *inner* paren, so
    the regex leaves the rest of the outer aside dangling as stray text.
    Tracking depth handles nesting properly; unbalanced input (Wiktionary
    template leakage sometimes ships mismatched brackets) degrades gracefully
    rather than throwing, since a stray close_ch at depth 0 is just dropped."""
    out = []
    depth = 0
    for ch in text:
        if ch == open_ch:
            depth += 1
        elif ch == close_ch:
            if depth > 0:
                depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def short_gloss(text):
    """A flashcard wants a translation, not a dictionary entry.

    The dictionary explains as much as it defines — "she, her (used
    subjectively and after prepositions)", "comparative of malo: worse" — and
    a card carrying that is harder to read than the Spanish it glosses."""
    first = str(text or "").split(";")[0]
    first = _strip_balanced(first, "(", ")")               # asides, not meaning
    first = _strip_balanced(first, "[", "]")               # stray wiki-link/template leakage
    first = re.sub(r"^(comparative|superlative|diminutive|augmentative)"
                   r"\s+of\s+[^:]*:\s*", "", first, flags=re.I)
    first = re.sub(r"\s+", " ", first).strip(" ,")

    # Cap to the first 3 synonyms, not just a character count — Wiktionary
    # glosses often keep piling on near-synonyms well past what fits the
    # 56-char limit below, and a card with "to gather, to collect, to bring
    # together, to assemble, to get together..." reads as noise, not a
    # definition. Three is usually enough to triangulate the meaning.
    parts = first.split(", ")
    if len(parts) > 3:
        first = ", ".join(parts[:3]) + "…"

    if len(first) > 56:
        # Cut at the last synonym boundary before the limit rather than
        # mid-word — a card reading "...of high…" is worse than one that
        # just drops the last synonym in the list cleanly.
        truncated = first[:56]
        cut = truncated.rfind(", ")
        first = (truncated[:cut] if cut > 20 else truncated[:53]).rstrip(" ,") + "…"
    return first


def _lesson_id_to_unit(curriculum):
    """lesson id -> {id, title, label, level} for every lesson in a built
    curriculum, so decks can be grouped exactly the way the Learn tab
    already groups the same lessons — one source of truth for "what unit is
    this lesson in" instead of re-deriving it from filenames a second way."""
    index = {}
    if not curriculum:
        return index
    for level_id, level in curriculum.get("levels", {}).items():
        for unit in level.get("units", []):
            for lesson in unit.get("lessons", []):
                index[lesson["id"]] = {
                    "id": unit["id"],
                    "title": unit["title"],
                    "label": unit["label"],
                    "level": level_id
                }
    return index


_FAMILY_SUFFIX_RE = re.compile(r"\.\d+$")


def _story_unit_index(lang, curriculum):
    """story ref path (as it appears in a lesson's `story` section, e.g.
    'stories/classics/b1/b1-01-janosvitez.json') -> {id, title, label,
    level}, so the reader can show "this is the reading for Level X, Unit
    Y" the same way a classics reading already shows its source. Derived
    by finding which lesson actually embeds each story (its `story`
    section `ref`), then resolving that lesson to its unit via
    _lesson_id_to_unit() -- one more read of the same lesson files
    build_curriculum() already walked, not a new source of truth.

    A world-type "combined" story (see content/*/stories/world/*.json's own
    convention) is never itself embedded in a lesson -- only its five
    per-lesson segments are -- so it would never resolve this way on its
    own. It shares an id "family" with those segments instead (segment ids
    end in '.01'..'.05', the combined id has no such suffix), so once any
    family member resolves via direct lesson linkage, every other member
    of that family borrows the same unit."""
    lesson_unit = _lesson_id_to_unit(curriculum)
    ref_to_unit = {}
    lang_path = BASE_LESSONS / lang
    lessons_dir = lang_path / "lessons"
    if not lessons_dir.exists():
        return ref_to_unit

    for level_dir in sorted(p for p in lessons_dir.iterdir() if p.is_dir()):
        for f in sorted(level_dir.glob("*.json")):
            if f.name in SKIP_FILENAMES or f.stat().st_size == 0:
                continue
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            unit = lesson_unit.get(data.get("id"))
            if not unit:
                continue
            for section in data.get("sections", []):
                if section.get("type") == "story" and section.get("ref"):
                    ref_to_unit[section["ref"]] = unit
    return ref_to_unit


def _apply_story_unit_families(stories):
    """Second pass over an already-built stories list: for any story with
    no resolved unit, borrow one from another story that shares its id
    family (see _story_unit_index's docstring) and did resolve. Mutates
    each story dict's "unit" key in place.

    Restricted to type "world" stories on both sides: that's the only
    category where a combined story and its five per-lesson segments are
    genuinely siblings sharing one unit. A classics/original reading is
    always its own single story with no such family, and its id can
    reduce to something far too generic once the trailing ".NN" is
    stripped (e.g. "story.b1.01" -> "story.b1", which is a prefix of
    nearly every other B1 story id) -- applying this to non-world stories
    was matching completely unrelated readings to whatever unit happened
    to iterate first.

    Exact family match first (fast, covers almost everything), then a
    hyphen-insensitive prefix fallback for the handful of older units
    where a combined story's own slug drifted from its segments' slug —
    e.g. segments "story.b1.represionpolitica.01".."05" (family
    "story.b1.represionpolitica") vs their combined sibling's own id
    "story.b1.represion-politica": same slug, one extra hyphen."""
    world = [s for s in stories if s.get("type") == "world"]

    family_unit = {}
    for s in world:
        if s.get("unit"):
            family_unit.setdefault(_FAMILY_SUFFIX_RE.sub("", s["id"]), s["unit"])

    unresolved = [s for s in world if not s.get("unit")]
    for s in unresolved:
        fam = _FAMILY_SUFFIX_RE.sub("", s["id"])
        if fam in family_unit:
            s["unit"] = family_unit[fam]
            continue
        fam_norm = fam.replace("-", "")
        for rid_fam, unit in family_unit.items():
            rid_fam_norm = rid_fam.replace("-", "")
            if rid_fam_norm and fam_norm.startswith(rid_fam_norm):
                s["unit"] = unit
                break


def build_decks(lang="es", curriculum=None):
    """Every deck the Decks tab can offer, built from content that already
    exists rather than maintained by hand.

    A deck is a named list of words, not a schedule. The same word turns up in
    its lesson deck, a frequency band and a topic — scheduling it three times
    would mean reviewing it three times and would wreck the SM-2 interval, so
    the card store stays single and decks only select from it.

    Words are written once into a shared table and decks refer to them by
    lemma, because a word that belongs to three decks should not be stored
    three times.

    "Lesson" decks are grouped by unit, not by individual lesson file — a
    single lesson's vocabulary (4-8 words) was too thin to be a useful review
    deck on its own; a unit's (5-6 lessons pooled) lands close to the ~20
    words a deck is meant to hold. Unit membership comes from the same
    curriculum structure the Learn tab uses, not re-derived from filenames."""
    base = BASE_LESSONS / lang
    vocab_dir = base / "vocabulary"
    if not vocab_dir.exists():
        return None

    if curriculum is None:
        curriculum = build_curriculum(lang)
    lesson_to_unit = _lesson_id_to_unit(curriculum)

    words = {}          # lemma -> {en, pos}
    by_unit, unit_order, by_theme = {}, [], {}

    def remember(lemma, translation, pos):
        if lemma not in words:
            words[lemma] = {"en": translation or "", "pos": pos or "unknown"}

    for level_dir in sorted(p for p in vocab_dir.iterdir() if p.is_dir()):
        for f in sorted(level_dir.glob("*-voc.json")):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue

            lemmas = []
            for w in data.get("words", []):
                lemma = w.get("lemma")
                if not lemma:
                    continue
                remember(lemma, w.get("translation"), w.get("pos"))
                lemmas.append(lemma)
            if not lemmas:
                continue

            lesson_key = data.get("lesson", f.stem.replace("-voc", ""))
            lesson_id = "lesson." + lesson_key.replace("-", ".")
            unit = lesson_to_unit.get(lesson_id)

            # A lesson whose unit can't be found (missing from the
            # curriculum, e.g. a stray vocab file with no matching lesson)
            # still gets a deck of its own rather than being silently
            # dropped — same fallback shape, just scoped to that one lesson.
            if unit:
                key, name, label, level = unit["id"], unit["title"], unit["label"], unit["level"]
            else:
                key = lesson_key
                name = data.get("title", lesson_key)
                label = lesson_key.split("-", 1)[-1]
                level = level_dir.name.upper()

            if key not in by_unit:
                by_unit[key] = {"name": name, "label": label, "level": level, "lemmas": [], "seen": set()}
                unit_order.append(key)
            bucket = by_unit[key]
            for lemma in lemmas:
                if lemma not in bucket["seen"]:
                    bucket["seen"].add(lemma)
                    bucket["lemmas"].append(lemma)

            theme = data.get("theme")
            if theme:
                by_theme.setdefault(theme, []).extend(lemmas)

    lesson_decks = []
    for key in unit_order:
        bucket = by_unit[key]
        lesson_decks.append({
            "id": "lesson:" + key,
            "kind": "lesson",
            "name": bucket["name"],
            "label": bucket["label"],
            "level": bucket["level"],
            "lemmas": bucket["lemmas"]
        })

    # Topic decks pool every lesson that teaches the same theme, so "City &
    # places" stays one deck however many lessons contribute to it.
    topic_decks = []
    for theme in sorted(by_theme):
        seen, lemmas = set(), []
        for lemma in by_theme[theme]:
            if lemma in seen:
                continue
            seen.add(lemma)
            lemmas.append(lemma)
        topic_decks.append({
            "id": "topic:" + re.sub(r"[^a-z0-9]+", "-", theme.lower()).strip("-"),
            "kind": "topic",
            "name": theme,
            "lemmas": lemmas
        })

    # Frequency decks are the most common words in the language, full stop —
    # not the course's words sorted by frequency, which was the earlier
    # mistake: it produced a deck called "Top 100 words" holding seventeen,
    # none of them the actual top hundred. Translations come from the
    # dictionary. Every language builds from its own ranked list and its own
    # dictionary — mismatching them (e.g. Hungarian ranks against the
    # Spanish dictionary) was the later mistake this replaced: it silently
    # produced Spanish frequency decks for every language.
    frequency_decks = []
    sources = FREQUENCY_SOURCES.get(lang)

    if sources and sources[0].exists() and sources[1].exists():
        ranks_path, dict_path = sources
        try:
            ranked = json.loads(ranks_path.read_text(encoding="utf-8"))
            lexicon = json.loads(dict_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            ranked, lexicon = [], {}

        gloss_overrides = FREQUENCY_GLOSS if lang == "es" else {}

        for low, high in FREQUENCY_BANDS:
            band = []
            for lemma in ranked[low - 1:high]:
                gloss = gloss_overrides.get(lemma)
                pos = "unknown"

                # spanish-en.json stores one sense per lemma (a dict); the
                # Hungarian dictionary stores several (a list, ordered by
                # source frequency, not usefulness — "a" 's own first sense
                # is fine, but plenty of others open on an "alternative
                # form of..." or similarly useless entry). Normalise to a
                # list either way and take the first sense that isn't junk.
                entry = lexicon.get(lemma)
                senses = entry if isinstance(entry, list) else ([entry] if entry else [])
                for sense in senses:
                    pos = sense.get("type", "unknown")
                    if gloss:
                        break
                    candidate = short_gloss(sense.get("en"))
                    # A description of the word is not a translation.
                    if candidate and not JUNK_GLOSS.match(candidate):
                        gloss = candidate
                        break
                if not gloss:
                    continue

                remember(lemma, gloss, pos)
                band.append(lemma)

            if band:
                frequency_decks.append({
                    "id": "frequency:%d-%d" % (low, high),
                    "kind": "frequency",
                    "name": ("Top %d words" % high) if low == 1
                            else ("Words %d–%d" % (low, high)),
                    "lemmas": band
                })

    return {
        "generated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "words": words,
        "decks": lesson_decks + topic_decks + frequency_decks
    }


def validate_lessons(lang="es"):
    """Check that every ref inside each lesson file actually resolves to a
    real file, and that every exercise-group's exerciseRefs id actually
    exists inside the exercises file it points at. Content refs fail
    silently at runtime (loadContent() just falls back to a "Coming soon"
    placeholder), so this is the only place broken refs get surfaced.
    Returns a list of human-readable issue strings; never raises."""
    issues = []
    lang_path = BASE_LESSONS / lang
    lessons_dir = lang_path / "lessons"
    if not lessons_dir.exists():
        return issues

    for level_dir in sorted(p for p in lessons_dir.iterdir() if p.is_dir()):
        for f in sorted(level_dir.glob("*.json")):
            if f.name in SKIP_FILENAMES or f.stat().st_size == 0:
                continue
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                issues.append(f"{f}: invalid JSON ({e})")
                continue

            label = f"{f} ({data.get('id', '?')})"

            # Content paths used to be duplicated into metadata.*Ref(s) as well
            # as sections[].ref. They now live only on the section that uses
            # them, so there is one path to check and one place to fix it.

            # sections[].ref, and exercise-group exerciseRefs
            for i, section in enumerate(data.get("sections", [])):
                ref = section.get("ref")
                if not ref:
                    continue
                ref_path = lang_path / ref
                if not ref_path.exists():
                    issues.append(f"{label}: sections[{i}] ({section.get('type')}) ref '{ref}' does not exist")
                    continue

                if section.get("type") == "exercise-group" and section.get("exerciseRefs"):
                    try:
                        ref_data = json.loads(ref_path.read_text(encoding="utf-8"))
                        available_ids = {ex.get("id") for ex in ref_data.get("exercises", [])}
                    except json.JSONDecodeError:
                        available_ids = set()
                    for ex_id in section["exerciseRefs"]:
                        if ex_id not in available_ids:
                            issues.append(f"{label}: sections[{i}] exerciseRefs '{ex_id}' not found in {ref}")

    return issues

def main():
    generated = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # Build curriculum.json for each language first — this is what the Learn
    # tab actually reads (engine/curriculum.js, engine/init.js), generated
    # directly from each lesson file rather than hand-maintained separately.
    # Kept around so both the stories pass below (which unit is a reading
    # taught in?) and the decks pass further down can group by the same
    # units without rebuilding the curriculum a second time.
    curricula = {}
    for lang in ["es", "fr", "hu"]:
        lessons_dir = BASE_LESSONS / lang / "lessons"
        curriculum_dir = BASE_LESSONS / lang / "curriculum"
        if not lessons_dir.exists():
            print(f"Skipping curriculum for {lang}: no {lessons_dir} folder yet")
            continue
        if not curriculum_dir.exists():
            print(f"Skipping curriculum for {lang}: no {curriculum_dir} folder yet")
            continue
        curriculum = build_curriculum(lang)
        curricula[lang] = curriculum
        with open(curriculum_dir / "curriculum.json", "w", encoding='utf-8') as f:
            json.dump(curriculum, f, indent=2, ensure_ascii=False)
        total_units = sum(len(lvl['units']) for lvl in curriculum['levels'].values())
        total_lessons = sum(len(u['lessons']) for lvl in curriculum['levels'].values() for u in lvl['units'])
        print(f"Curriculum for {lang}: {total_lessons} lessons in {total_units} units across {len(curriculum['levels'])} levels")

    # Build stories manifest for each language that actually has a stories folder
    for lang in ["es", "fr", "hu"]:
        stories_dir = BASE_STORIES / lang / "stories"
        if not stories_dir.exists():
            print(f"Skipping stories manifest for {lang}: no {stories_dir} folder yet")
            continue
        ref_to_unit = _story_unit_index(lang, curricula.get(lang))
        stories = build_stories(lang, ref_to_unit)
        with open(stories_dir / "manifest.json", "w", encoding='utf-8') as f:
            json.dump({"generated": generated, "stories": stories}, f, indent=2, ensure_ascii=False)
        with_unit = sum(1 for s in stories if s.get("unit"))
        print(f"Stories manifest for {lang}: {len(stories)} stories ({with_unit} with a resolved unit)")

    # Decks: named word lists over the single card store
    for lang in ["es", "fr", "hu"]:
        decks = build_decks(lang, curriculum=curricula.get(lang))
        if not decks:
            continue
        out_dir = BASE_LESSONS / lang / "decks"
        out_dir.mkdir(parents=True, exist_ok=True)
        with open(out_dir / "decks.json", "w", encoding="utf-8") as f:
            json.dump(decks, f, indent=2, ensure_ascii=False)
        kinds = {}
        for d in decks["decks"]:
            kinds[d["kind"]] = kinds.get(d["kind"], 0) + 1
        print("Decks for %s: %d (%s)" % (
            lang, len(decks["decks"]),
            ", ".join("%d %s" % (n, k) for k, n in sorted(kinds.items()))))

    # Validate lesson content refs — broken refs fail silently in the app
    # (a "Coming soon" placeholder, no error), so surface them here instead.
    print()
    for lang in ["es", "fr", "hu"]:
        issues = validate_lessons(lang)
        if not issues:
            continue
        print(f"Content ref issues for {lang}: {len(issues)}")
        for issue in issues:
            print(f"  - {issue}")

if __name__ == "__main__":
    main()
