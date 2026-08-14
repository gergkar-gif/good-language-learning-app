#!/usr/bin/env python3
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(".")
BASE_STORIES = Path("content")
BASE_LESSONS = Path("content")

CATEGORIES = ["original", "classics", "world"]
SKIP_FILENAMES = {"manifest.json", "lessons-manifest.json"}

def build_stories(lang="es"):
    stories = []
    lang_path = BASE_STORIES / lang / "stories"
    if not lang_path.exists():
        return stories

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

            stories.append({
                "id": data.get("id", f"story.{cat}.{f.stem}"),
                "title": data.get("title", f.stem),
                "level": data.get("level", "Unknown"),
                "lesson": data.get("lesson"),
                "type": cat,
                "source": cat,
                # relative to content/{lang}/stories/, matching what
                # Content.story() fetches: content/{lang}/stories/${path}
                "path": f.relative_to(lang_path).as_posix(),
                "estimatedMinutes": data.get("estimatedMinutes"),
                "characters": data.get("characters", []),
                "location": data.get("location")
            })
    return stories

LEVEL_META = {
    "a1": {"title": "Fundamentals", "description": "Survival skills"},
    "a2": {"title": "Basic", "description": "Manage basic interactions"},
    "b1": {"title": "Intermediate", "description": "Express opinions, handle complex topics"},
    "b2": {"title": "Upper Intermediate", "description": "Complex arguments, abstract topics"},
    "c1": {"title": "Advanced", "description": "Fluency. Politics, philosophy, art, science"}
}

CURRICULUM_META = {
    "es": {"id": "curriculum.spanish.dele-a1-c1", "title": "Spanish — DELE aligned"}
}

# Level -> Unit -> Lesson. Explicit rather than inferred from filenames,
# because the mapping is a curriculum decision (which topic sits where, and
# in what order) and reads as one here rather than being reverse-engineered
# from a naming convention. Each entry is the unit title and the lesson file
# stems it owns, in teaching order.
#
# Unit 1 is the only unit actually split into several lessons so far — every
# other unit still wraps the one pre-restructure lesson file it always had,
# just reordered and retitled to its approved position. Splitting those into
# their own 4-6 lesson sets happens unit by unit as that content is authored;
# nothing else here changes when it does.
UNIT_TABLES = {
    "a1": [
        ("Greetings & Introductions", ["a1-01-01", "a1-01-02", "a1-01-03", "a1-01-04", "a1-01-05", "a1-01-consolidation"]),
        ("Meeting Someone New", ["a1-02-01", "a1-02-02", "a1-02-03", "a1-02-04", "a1-02-05", "a1-02-consolidation"]),
        ("Naming Things", ["a1-03-01", "a1-03-02", "a1-03-03", "a1-03-04", "a1-03-05", "a1-03-consolidation"]),
        ("Describing People", ["a1-03c-01", "a1-03c-02", "a1-03c-03", "a1-03c-04", "a1-03c-05", "a1-03c-consolidation"]),
        ("Family", ["a1-05-01", "a1-05-02", "a1-05-03", "a1-05-04", "a1-05-05", "a1-05-consolidation"]),
        ("Daily Routine", ["a1-06-01", "a1-06-02", "a1-06-03", "a1-06-04", "a1-06-05", "a1-06-consolidation"]),
        ("At Home", ["a1-07-01", "a1-07-02", "a1-07-03", "a1-07-04", "a1-07-05", "a1-07-consolidation"]),
        ("At the Supermarket", ["a1-08-01", "a1-08-02", "a1-08-03", "a1-08-04", "a1-08-05", "a1-08-consolidation"]),
        # "a1-cafe", not "a1-09" — old lesson slot 9 is Kitchen (still
        # unsplit), and a1-09 would collide with it the moment Kitchen's own
        # split arrives.
        ("Ordering at a Café", ["a1-cafe-01", "a1-cafe-02", "a1-cafe-03", "a1-cafe-04", "a1-cafe-05", "a1-cafe-consolidation"]),
        ("Birthdays & Celebrations", ["a1-10"]),
        # "a1-kitchen", not "a1-11" — a1-11 is Hobbies' old slot (still
        # unsplit), same reasoning as the Café rename above.
        ("In the Kitchen", ["a1-kitchen-01", "a1-kitchen-02", "a1-kitchen-03", "a1-kitchen-04", "a1-kitchen-05", "a1-kitchen-consolidation"]),
        ("Numbers, Time & Schedules", ["a1-12-01", "a1-12-02", "a1-12-03", "a1-12-04", "a1-12-05", "a1-12-consolidation"]),
        ("Around Town", ["a1-04-01", "a1-04-02", "a1-04-03", "a1-04-04", "a1-04-05", "a1-04-consolidation"]),
        # "a1-directions", not "a1-14" — a1-14 is Weather's old slot.
        ("Directions", ["a1-directions-01", "a1-directions-02", "a1-directions-03", "a1-directions-04", "a1-directions-05", "a1-directions-consolidation"]),
        # "a1-weather", not "a1-15" — a1-15 is Work & Obligations' old slot.
        ("Weather", ["a1-weather-01", "a1-weather-02", "a1-weather-03", "a1-weather-04", "a1-weather-05", "a1-weather-consolidation"]),
        # "a1-work", not "a1-16" — a1-16 is Health's old slot.
        ("Work & Obligations", ["a1-work-01", "a1-work-02", "a1-work-03", "a1-work-04", "a1-work-05", "a1-work-consolidation"]),
        # "a1-health", not "a1-17" — a1-17 is Future Plans' old slot.
        ("Health", ["a1-health-01", "a1-health-02", "a1-health-03", "a1-health-04", "a1-health-05", "a1-health-consolidation"]),
        # "a1-hobbies", not "a1-18" — a1-18 was Review 1's old slot.
        ("Hobbies & Free Time", ["a1-hobbies-01", "a1-hobbies-02", "a1-hobbies-03", "a1-hobbies-04", "a1-hobbies-05", "a1-hobbies-consolidation"]),
        # "a1-future", not "a1-19" — a1-19 was Review 2's old slot.
        ("Future Plans", ["a1-future-01", "a1-future-02", "a1-future-03", "a1-future-04", "a1-future-05", "a1-future-consolidation"]),
        # Old Review 1/2/Final are fully retired now — their readings live on,
        # reused by lessons 20.4 (a1-19's reflection scene) and 20.5 (a1-20's
        # dating-decision resolution). a1-18's reading has no home in the new
        # unit and sits unused rather than deleted.
        ("Travel & Getting Away", ["a1-20-01", "a1-20-02", "a1-20-03", "a1-20-04", "a1-20-05", "a1-20-consolidation"]),
    ],
    "a2": [
        ("Talking About Your Trip", ["a2-01-01", "a2-01-02", "a2-01-03", "a2-01-04", "a2-01-05", "a2-01-consolidation"]),
        ("Talking About What You Have Done", ["a2-02-01", "a2-02-02", "a2-02-03", "a2-02-04", "a2-02-05", "a2-02-consolidation"]),
        ("Talking About a Day Out", ["a2-03-01", "a2-03-02", "a2-03-03", "a2-03-04", "a2-03-05", "a2-03-consolidation"]),
        ("Following Instructions", ["a2-04-01", "a2-04-02", "a2-04-03", "a2-04-04", "a2-04-05", "a2-04-consolidation"]),
        ("Giving Reasons and Opinions", ["a2-05-01", "a2-05-02", "a2-05-03", "a2-05-04", "a2-05-05", "a2-05-consolidation"]),
        ("Comparing Trips and Memories", ["a2-06-01", "a2-06-02", "a2-06-03", "a2-06-04", "a2-06-05", "a2-06-consolidation"]),
        ("Talking About How Long", ["a2-07-01", "a2-07-02", "a2-07-03", "a2-07-04", "a2-07-05", "a2-07-consolidation"]),
        ("Making and Responding to Invitations", ["a2-08-01", "a2-08-02", "a2-08-03", "a2-08-04", "a2-08-05", "a2-08-consolidation"]),
        ("Talking About Experiences", ["a2-09-01", "a2-09-02", "a2-09-03", "a2-09-04", "a2-09-05", "a2-09-consolidation"]),
        ("Keeping in Touch", ["a2-10-01", "a2-10-02", "a2-10-03", "a2-10-04", "a2-10-05", "a2-10-consolidation"]),
        ("Talking About What Happened", ["a2-11-01", "a2-11-02", "a2-11-03", "a2-11-04", "a2-11-05", "a2-11-consolidation"]),
        ("Giving and Receiving Things", ["a2-12-01", "a2-12-02", "a2-12-03", "a2-12-04", "a2-12-05", "a2-12-consolidation"]),
        ("Describing Events in Time", ["a2-13-01", "a2-13-02", "a2-13-03", "a2-13-04", "a2-13-05", "a2-13-consolidation"]),
        ("Asking About What Happened", ["a2-14-01", "a2-14-02", "a2-14-03", "a2-14-04", "a2-14-05", "a2-14-consolidation"]),
        ("Explaining What Happened", ["a2-15-01", "a2-15-02", "a2-15-03", "a2-15-04", "a2-15-05", "a2-15-consolidation"]),
        ("Talking About Plans", ["a2-16-01", "a2-16-02", "a2-16-03", "a2-16-04", "a2-16-05", "a2-16-consolidation"]),
        ("Reviewing A2 Experiences", ["a2-17-01", "a2-17-02", "a2-17-03", "a2-17-04", "a2-17-05", "a2-17-consolidation"]),
        ("Talking About Travel and Goodbyes", ["a2-18-01", "a2-18-02", "a2-18-03", "a2-18-04", "a2-18-05", "a2-18-consolidation"]),
        ("Talking About the Future", ["a2-19-01", "a2-19-02", "a2-19-03", "a2-19-04", "a2-19-05", "a2-19-consolidation"]),
        ("Looking Back and Moving Forward", ["a2-20-01", "a2-20-02", "a2-20-03", "a2-20-04", "a2-20-05", "a2-20-consolidation"]),
    ],
    # B1 runs two parallel tracks — Core Spanish (the language progression)
    # and Latin America (a Spanish-language history course) — that appear
    # side by side in the Learn tab and are numbered independently within
    # their own track. A table entry here is (title, stems, track); a1/a2
    # entries above stay 2-tuples and are read as a single implicit track,
    # so nothing about them changes. See content/es/guides/b1-content-spec.md
    # section 1a for why Latin America units use a word slug (here,
    # "precolombina") instead of a number in their lesson-file stems.
    "b1": [
        ("Telling Stories",
         ["b1-01-01", "b1-01-02", "b1-01-03", "b1-01-04", "b1-01-05", "b1-01-consolidation"],
         "core"),
        ("Pre-Columbian America",
         ["b1-precolombina-01", "b1-precolombina-02", "b1-precolombina-03",
          "b1-precolombina-04", "b1-precolombina-05", "b1-precolombina-consolidation"],
         "latam"),
    ],
}

# Track metadata for levels that run more than one — id, display title, and
# the order tracks should render in the Learn tab. A level absent here (or a
# unit table entry with no third element) is single-track, and the Learn tab
# falls back to today's flat unit list.
LEVEL_TRACKS = {
    "b1": [
        {"id": "core", "title": "Core Spanish"},
        {"id": "latam", "title": "Latin America"},
    ],
}

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

    Level -> Unit -> Lesson. A level with an entry in UNIT_TABLES is built
    from that table, in the order given. A level without one (nothing past
    A1 has content yet) falls back to one unit per lesson file, in filename
    order, so the shape stays the same everywhere even before a level has a
    real unit plan."""
    lang_path = BASE_LESSONS / lang / "lessons"
    if not lang_path.exists():
        return None

    levels = {}
    for level_id, meta in LEVEL_META.items():
        level_path = lang_path / level_id
        units = []

        if level_path.exists():
            table = UNIT_TABLES.get(level_id)
            if table:
                # Position is counted per track, not across the whole table,
                # so two tracks each start their own unit numbering at 1
                # rather than interleaving into a single shared sequence.
                track_position = {}
                for entry in table:
                    title, stems, track = entry if len(entry) == 3 else (*entry, None)
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
        if level_id in LEVEL_TRACKS:
            level_entry["tracks"] = LEVEL_TRACKS[level_id]
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

# The dictionary's first sense for a handful of very common words is the name
# of the letter — 'de' glossed as "letter: d" — because that entry sorts first.
# Those are exactly the words a frequency deck opens with, so they are given
# the sense a learner actually needs.
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


def short_gloss(text):
    """A flashcard wants a translation, not a dictionary entry.

    The dictionary explains as much as it defines — "she, her (used
    subjectively and after prepositions)", "comparative of malo: worse" — and
    a card carrying that is harder to read than the Spanish it glosses."""
    first = str(text or "").split(";")[0]
    first = re.sub(r"\([^)]*\)", " ", first)              # asides, not meaning
    first = re.sub(r"^(comparative|superlative|diminutive|augmentative)"
                   r"\s+of\s+[^:]*:\s*", "", first, flags=re.I)
    first = re.sub(r"\s+", " ", first).strip(" ,")
    if len(first) > 56:
        first = first[:53].rstrip(" ,") + "…"
    return first


def build_decks(lang="es"):
    """Every deck the Decks tab can offer, built from content that already
    exists rather than maintained by hand.

    A deck is a named list of words, not a schedule. The same word turns up in
    its lesson deck, a frequency band and a topic — scheduling it three times
    would mean reviewing it three times and would wreck the SM-2 interval, so
    the card store stays single and decks only select from it.

    Words are written once into a shared table and decks refer to them by
    lemma, because a word that belongs to three decks should not be stored
    three times."""
    base = BASE_LESSONS / lang
    vocab_dir = base / "vocabulary"
    if not vocab_dir.exists():
        return None

    words = {}          # lemma -> {en, pos}
    lesson_decks, by_theme = [], {}

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

            # A vocabulary file's title names the story; the deck should carry
            # the lesson's own title, which is what the learner picked from.
            lesson_file = base / "lessons" / level_dir.name / (lesson_key + ".json")
            lesson_title = data.get("title", lesson_key)
            if lesson_file.exists():
                try:
                    lesson_title = json.loads(
                        lesson_file.read_text(encoding="utf-8")).get("title", lesson_title)
                except (OSError, json.JSONDecodeError):
                    pass

            lesson_decks.append({
                "id": "lesson:" + lesson_key,
                "kind": "lesson",
                "name": lesson_title,
                "label": lesson_key.split("-", 1)[-1],
                "level": level_dir.name.upper(),
                "lemmas": lemmas
            })

            theme = data.get("theme")
            if theme:
                by_theme.setdefault(theme, []).extend(lemmas)

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

    # Frequency decks are the most common words in Spanish, full stop — not
    # the course's words sorted by frequency, which was the earlier mistake:
    # it produced a deck called "Top 100 words" holding seventeen, none of
    # them the actual top hundred. Translations come from the dictionary.
    frequency_decks = []
    ranks_path = ROOT / "generated" / "indexes" / "frequency.json"
    dict_path = ROOT / "imports" / "dictionary" / "spanish-en.json"

    if ranks_path.exists() and dict_path.exists():
        try:
            ranked = json.loads(ranks_path.read_text(encoding="utf-8"))
            lexicon = json.loads(dict_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            ranked, lexicon = [], {}

        for low, high in FREQUENCY_BANDS:
            band = []
            for lemma in ranked[low - 1:high]:
                gloss = FREQUENCY_GLOSS.get(lemma)
                pos = "unknown"

                entry = lexicon.get(lemma)
                if entry:
                    pos = entry.get("type", "unknown")
                    if not gloss:
                        candidate = short_gloss(entry.get("en"))
                        # A description of the word is not a translation.
                        if candidate and not JUNK_GLOSS.match(candidate):
                            gloss = candidate
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

    # Build stories manifest for each language that actually has a stories folder
    for lang in ["es", "fr", "hu"]:
        stories_dir = BASE_STORIES / lang / "stories"
        if not stories_dir.exists():
            print(f"Skipping stories manifest for {lang}: no {stories_dir} folder yet")
            continue
        stories = build_stories(lang)
        with open(stories_dir / "manifest.json", "w", encoding='utf-8') as f:
            json.dump({"generated": generated, "stories": stories}, f, indent=2, ensure_ascii=False)
        print(f"Stories manifest for {lang}: {len(stories)} stories")

    # Build curriculum.json for each language — this is what the Learn tab
    # actually reads (engine/curriculum.js, engine/init.js), generated
    # directly from each lesson file rather than hand-maintained separately.
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
        with open(curriculum_dir / "curriculum.json", "w", encoding='utf-8') as f:
            json.dump(curriculum, f, indent=2, ensure_ascii=False)
        total_units = sum(len(lvl['units']) for lvl in curriculum['levels'].values())
        total_lessons = sum(len(u['lessons']) for lvl in curriculum['levels'].values() for u in lvl['units'])
        print(f"Curriculum for {lang}: {total_lessons} lessons in {total_units} units across {len(curriculum['levels'])} levels")

    # Decks: named word lists over the single card store
    for lang in ["es", "fr", "hu"]:
        decks = build_decks(lang)
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
