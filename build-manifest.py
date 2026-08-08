#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

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


def build_curriculum(lang="es"):
    """Build the curriculum.json structure (what the Learn tab actually reads)
    straight from each lesson's own JSON file — lesson files are the single
    source of truth; curriculum.json is a generated index over them."""
    lang_path = BASE_LESSONS / lang / "lessons"
    if not lang_path.exists():
        return None

    levels = {}
    for level_id, meta in LEVEL_META.items():
        level_path = lang_path / level_id
        level_lessons = []

        if level_path.exists():
            for f in sorted(level_path.glob("*.json")):
                if f.name in SKIP_FILENAMES:
                    continue
                try:
                    with open(f, 'r', encoding='utf-8') as fh:
                        data = json.load(fh)
                    new_words, exercise_counts = lesson_teaching_counts(lang, data)
                    level_lessons.append({
                        "id": data.get("id", f"lesson.{level_id}.{f.stem}"),
                        # The number shown on the lesson row. Taken from the
                        # filename rather than the row's position, because a
                        # lesson split into parts (a1-03a, a1-03b, a1-03c)
                        # must keep slot 3 instead of pushing 04 down to 06.
                        "label": f.stem.split("-", 1)[-1],
                        "title": data.get("title", f.stem),
                        "grammar": data.get("grammar", ""),
                        "goal": data.get("goal", ""),
                        # Shown on the lesson row in the Learn tab, so the
                        # index carries it rather than fetching 20 lessons.
                        "estimatedMinutes": (data.get("metadata") or {}).get("estimatedMinutes"),
                        # Read by My Journey to total up coverage.
                        "newWords": new_words,
                        "exercises": exercise_counts
                    })
                except (OSError, json.JSONDecodeError):
                    pass

        levels[level_id.upper()] = {
            "title": meta["title"],
            "description": meta["description"],
            "lessons": level_lessons
        }

    curr_meta = CURRICULUM_META.get(lang, {
        "id": f"curriculum.{lang}.a1-c1",
        "title": f"{lang.upper()} Mastery"
    })

    return {
        "id": curr_meta["id"],
        "title": curr_meta["title"],
        "levels": levels
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
        total_lessons = sum(len(lvl['lessons']) for lvl in curriculum['levels'].values())
        print(f"Curriculum for {lang}: {total_lessons} lessons across {len(curriculum['levels'])} levels")

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
