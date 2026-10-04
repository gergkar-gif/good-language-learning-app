#!/usr/bin/env python3
"""Validate every content file against its schema.

Schemas that nobody runs are just documentation, and content errors here fail
silently in the app — loadContent() falls back to a "Coming soon" placeholder
and buildSteps() drops an unknown section with a console warning, so a broken
lesson looks merely empty rather than broken.

Cross-file rules (refs resolving, exercise ids existing) are checked by
build-manifest.py instead; see content/es/schemas/README.md for the full list
of what is and isn't enforced.

    python scripts/validate-content.py            # all languages found
    python scripts/validate-content.py es         # one language
    python scripts/validate-content.py --changed  # only files differing from origin/master

Exits non-zero if anything fails, so it can gate a commit.
"""

import glob
import json
import subprocess
import sys
from pathlib import Path

try:
    from jsonschema import Draft7Validator
except ImportError:
    sys.exit("jsonschema is not installed. Run: python -m pip install jsonschema")

# Content is Spanish and error messages quote it back, which the default
# Windows console encoding cannot represent.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent

# schema name -> glob of the files it governs, relative to content/<lang>/
TARGETS = {
    "lesson": "lessons/*/*.json",
    "grammar": "grammar/*/*.json",
    "exercises": "exercises/*/*.json",
    "vocabulary": "vocabulary/*/*.json",
    "story": "stories/**/*.json",
    "drill-bank": "drills/*/*.json",
    "test": "tests/*.json",
    "units": "curriculum/units/*.json",
}

SKIP = {"manifest.json", "lessons-manifest.json", "diagnostic-test.json"}

# The Spain course's CCSE (citizenship exam) track was committed as an
# unfinished scaffold: 210 lessons are empty stubs and the Constitución unit
# uses ids/fields that don't match the schemas. Skipped by name so it doesn't
# block the content-sync workflow; drop this once the track is built for real.
SKIP_STEM_MARKERS = {"es-es": "-ccse-"}

# Flip to True once the exercise metadata backfill (Phases 2-3) is complete
# across all courses so full CI runs enforce `category` + `teaches` everywhere.
METADATA_ENFORCED_EVERYWHERE = True

ALLOWED_EXERCISE_CATEGORIES = {
    "vocabulary",
    "grammar",
    "reading",
    "dialogue",
    "writing",
    "listening",
}


def load_schemas(lang_dir):
    schema_dir = lang_dir / "schemas"
    schemas = {}
    for name in TARGETS:
        path = schema_dir / f"{name}.schema.json"
        if not path.exists():
            continue
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft7Validator.check_schema(schema)
        schemas[name] = schema
    return schemas


import re


def check_title_style(slug, title):
    if not isinstance(title, str) or not title.strip():
        return "empty title"
    if title == "reading":
        return None
    if ":" in title:
        return "contains colon ':'"
    if "(" in title or ")" in title:
        return "contains parentheses"
    if " - " in title or " – " in title or " — " in title:
        return "contains separator dash"
    if " / " in title:
        return "contains slash between phrases (' / ')"
    if "*" in title or '"' in title:
        return "contains asterisk or quote"
    if re.search(r"\bunit\s*-?\s*\d+", title, re.I):
        return "contains unit number"
    if re.search(r"\b(consolidation|unit\d+|translation)\b", title, re.I) or "suffix'" in title.lower():
        return "contains mechanical/fallback token"
    allowed_upper_starts = (
        "España", "América", "Spanish", "Latin", "Hungarian", "DELE", "CCSE",
        "Magyarország", "Budapest", "István", "Mátyás", "Szent"
    )
    if title[0].isupper() and not title.startswith(allowed_upper_starts):
        return f"starts with uppercase '{title[0]}' (must start lowercase unless proper noun)"
    words = title.split()
    if len(words) > 11:
        return f"too long ({len(words)} words; keep concise)"
    allowed_caps = {
        "A1", "A2", "B1", "B2", "C1", "C2", "I",
        "España", "América", "Latina", "Spanish", "Latin", "American",
        "Hungarian", "DELE", "CCSE", "Magyarország", "Budapest",
        "István", "Mátyás", "Szent"
    }
    cap_words = [w.strip(",.;") for w in words if w and w[0].isupper() and w.strip(",.;") not in allowed_caps]
    if cap_words:
        return f"unexpected capitalized word(s): {cap_words}"
    return None


def validate_grammar_titles(lang_dir, lang):
    titles_path = lang_dir / "indexes" / "grammar-titles.json"
    idx_path = lang_dir / "indexes" / "grammar-index.json"
    if not titles_path.is_file():
        return []
    errors = []
    try:
        titles = json.loads(titles_path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{titles_path.relative_to(ROOT)}: invalid JSON ({e})"]

    for slug, title in sorted(titles.items()):
        reason = check_title_style(slug, title)
        if reason:
            errors.append(f"{titles_path.relative_to(ROOT)} :: {slug}\n      title {title!r} violates style: {reason}")

    if idx_path.is_file():
        try:
            by_skill = json.loads(idx_path.read_text(encoding="utf-8")).get("bySkill") or {}
            for skill in sorted(by_skill.keys()):
                if skill not in titles:
                    errors.append(
                        f"{titles_path.relative_to(ROOT)} :: {skill}\n      grammar skill '{skill}' in grammar-index.json has no curated title in grammar-titles.json"
                    )
        except Exception:
            pass

    reg_path = lang_dir / "indexes" / "skill-registry.json"
    if reg_path.is_file():
        try:
            reg_skills = json.loads(reg_path.read_text(encoding="utf-8")).get("skills") or {}
            slug_re = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
            for canon, meta in sorted(reg_skills.items()):
                if not slug_re.match(canon):
                    errors.append(f"{reg_path.relative_to(ROOT)} :: {canon}\n      invalid canonical skill slug '{canon}'")
                for al in (meta.get("aliases") or []) if isinstance(meta, dict) else []:
                    if not isinstance(al, str) or not slug_re.match(al):
                        errors.append(
                            f"{reg_path.relative_to(ROOT)} :: {canon}.aliases\n      invalid alias slug {al!r} (must match ^[a-z0-9]+(-[a-z0-9]+)*$)"
                        )
        except Exception as e:
            errors.append(f"{reg_path.relative_to(ROOT)}: invalid JSON ({e})")

    return errors


def load_skill_registry(lang_dir):
    reg_path = lang_dir / "indexes" / "skill-registry.json"
    if not reg_path.is_file():
        return None, {}, {}
    try:
        data = json.loads(reg_path.read_text(encoding="utf-8"))
        skills_obj = data.get("skills") or {}
        canonical_set = set(skills_obj.keys())
        alias_map = {}
        kind_map = {}
        for canon, meta in skills_obj.items():
            if isinstance(meta, dict):
                if meta.get("kind"):
                    kind_map[canon] = meta["kind"]
                for al in meta.get("aliases") or []:
                    alias_map[al] = canon
        return canonical_set, alias_map, kind_map
    except Exception:
        return None, {}, {}


# ---------------------------------------------------------------------------
# Skill system (ROADMAP 125; docs/skill-tagging-spec.md). The source of truth is
# skills/<lang>.json; the per-course registry, grammar-titles.json and
# skill-prereqs.json are generated from it by scripts/build_skill_registry.py.
# Rules existing content can't meet until the read-through (one tag per
# exercise, a skill no higher than the exercise's level, retired slugs, at
# least 6 exercises per skill) are warnings, and errors for a locked unit.
# ---------------------------------------------------------------------------

LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MIN_EXERCISES_PER_SKILL = 6
WARNINGS = {}          # lang -> {kind: [message, ...]}


def warn(lang, kind, msg):
    WARNINGS.setdefault(lang, {}).setdefault(kind, []).append(msg)


def load_skill_sources():
    """{lang: source dict} for every skills/<lang>.json, plus the families file."""
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        return {}, None
    families = json.loads((skills_dir / "families.json").read_text(encoding="utf-8"))
    sources = {}
    for path in sorted(skills_dir.glob("*.json")):
        if path.name == "families.json" or path.name.startswith("frozen-"):
            continue
        sources[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return sources, families


def course_language(course, sources):
    for lang, src in sources.items():
        if course in src.get("courses", []):
            return lang
    return None


def unit_tables(course):
    """{(LEVEL, unit id): unit entry} for one course, plus duplicate-id errors."""
    units, errors = {}, []
    for path in sorted((ROOT / "content" / course / "curriculum" / "units").glob("*.json")):
        level = path.stem.upper()
        try:
            table = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for entry in table:
            uid = entry.get("id")
            if not uid:
                continue  # the units schema reports a missing id
            if (level, uid) in units:
                errors.append(f"{path.relative_to(ROOT).as_posix()}: unit id {uid!r} is used twice in {level}")
            units[(level, uid)] = entry
    return units, errors


def validate_skill_sources(sources, families):
    """Errors in skills/*.json: fields, families, levels, taught_in, requires, units, frozen list."""
    errors = []
    if not sources:
        return errors
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_skill_registry", ROOT / "scripts" / "build_skill_registry.py")
    bsr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bsr)
    gfam = {f["slug"] for f in families["grammar"]}
    vfam = {f["slug"] for f in families["vocabulary"]}
    for lang, src in sources.items():
        rel = f"skills/{lang}.json"
        skills = src.get("skills", {})
        retired = src.get("retired", {})
        courses = src.get("courses", [])
        # generated course files must match the source
        for course in courses:
            for name, text in bsr.course_files(src).items():
                out = ROOT / "content" / course / name
                if not out.is_file() or out.read_text(encoding="utf-8") != text:
                    errors.append(f"content/{course}/{name}: out of date with {rel} -- run python scripts/build_skill_registry.py "
                                  f"(never edit it by hand)")
        # aliases
        seen = {}
        for slug, s in {**skills, **retired}.items():
            if not SLUG_RE.match(slug):
                errors.append(f"{rel} :: {slug}\n      invalid slug")
            for a in s.get("aliases", []):
                if a in skills or a in retired:
                    errors.append(f"{rel} :: {slug}\n      alias {a!r} is also a skill")
                elif a in seen:
                    errors.append(f"{rel} :: {slug}\n      alias {a!r} also belongs to {seen[a]!r}")
                seen[a] = slug
        units = {}
        for course in courses:
            u, unit_errs = unit_tables(course)
            errors.extend(unit_errs)
            units.update({k: (course, v) for k, v in u.items()})
        vocab_by_unit = {}
        for slug, s in skills.items():
            where = f"{rel} :: {slug}"
            kind, level = s.get("kind"), s.get("level")
            if kind not in ("grammar", "vocabulary"):
                errors.append(f"{where}\n      kind must be 'grammar' or 'vocabulary'")
                continue
            if level not in LEVELS:
                errors.append(f"{where}\n      level {level!r} is not one of {', '.join(LEVELS)}")
            if not s.get("title"):
                errors.append(f"{where}\n      missing title")
            if kind == "grammar":
                if s.get("family") not in gfam:
                    errors.append(f"{where}\n      grammar family {s.get('family')!r} is not in skills/families.json")
                reason = check_title_style(slug, s.get("title"))
                if reason:
                    errors.append(f"{where}\n      title {s.get('title')!r} violates style: {reason}")
                screen = s.get("taught_in")
                if not screen:
                    warn(lang, "grammar skill with no taught_in screen", f"{slug} (write a grammar screen that teaches it)")
                elif not any(any((ROOT / "content" / c).glob(f"grammar/*/{screen}.json")) for c in courses):
                    errors.append(f"{where}\n      taught_in screen {screen!r} does not exist in {', '.join(courses)}")
                for req in s.get("requires", []):
                    r = skills.get(req)
                    if not r or r.get("kind") != "grammar":
                        errors.append(f"{where}\n      requires {req!r}, which is not a grammar skill in {rel}")
                    elif level in LEVELS and r.get("level") in LEVELS and LEVELS.index(r["level"]) > LEVELS.index(level):
                        errors.append(f"{where}\n      requires {req!r} ({r['level']}), above this skill's level ({level})")
            else:
                fam = s.get("family")
                if not isinstance(fam, list) or not 1 <= len(fam) <= 2 or any(f not in vfam for f in fam):
                    errors.append(f"{where}\n      vocabulary family must be a list of 1-2 families from skills/families.json, got {fam!r}")
                uid = s.get("unit")
                if (level, uid) not in units:
                    errors.append(f"{where}\n      unit {uid!r} is not a unit id in any {level} unit table of {', '.join(courses)}")
                elif slug != f"{level.lower()}-{uid}-vocab":
                    errors.append(f"{where}\n      a unit's vocabulary skill must be named {level.lower()}-{uid}-vocab")
                if (level, uid) in vocab_by_unit:
                    errors.append(f"{where}\n      unit {level}/{uid} already has vocabulary skill {vocab_by_unit[(level, uid)]!r}")
                vocab_by_unit[(level, uid)] = slug
        for (level, uid), (course, _) in sorted(units.items()):
            if (level, uid) not in vocab_by_unit:
                errors.append(f"content/{course}/curriculum/units/{level.lower()}.json :: {uid}\n      unit has no vocabulary skill "
                              f"{level.lower()}-{uid}-vocab in {rel}")
        # requires must not loop
        state = {}

        def visit(n, path):
            if state.get(n) == 1:
                errors.append(f"{rel}: requires loop {' -> '.join(path + [n])}")
                return
            if state.get(n) == 2:
                return
            state[n] = 1
            for m in skills.get(n, {}).get("requires", []):
                visit(m, path + [n])
            state[n] = 2

        for n in skills:
            visit(n, [])
        # frozen list
        frozen_path = ROOT / "skills" / f"frozen-{lang}.json"
        frozen = set(json.loads(frozen_path.read_text(encoding="utf-8")).get("skills", {})) if frozen_path.is_file() else set()
        for slug in sorted(set(skills) - frozen):
            errors.append(f"{rel} :: {slug}\n      skill is not in skills/frozen-{lang}.json -- adding, merging, splitting or "
                          f"renaming a skill needs the user's sign-off and an entry there (ROADMAP 125)")
        for slug in sorted(frozen - set(skills)):
            errors.append(f"skills/frozen-{lang}.json :: {slug}\n      frozen skill is missing from {rel} -- removing or renaming "
                          f"a skill needs the user's sign-off and the frozen list updated")
    return errors


def load_tag_lock(lang_dir):
    path = lang_dir / "indexes" / "tags.lock.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("exercises", {})


def check_exercise_skills(data, path, lang, course_src, lock, counts):
    """Skill-system checks for one exercise file. Returns errors; records warnings and per-skill counts."""
    errs = []
    if not course_src:
        return errs
    skills = course_src.get("skills", {})
    retired = course_src.get("retired", {})
    ex_level = path.parent.name.upper()
    for idx, ex in enumerate(data.get("exercises", [])):
        ex_id = ex.get("id", f"exercises[{idx}]")
        where = f"exercises/{idx} ({ex_id})"
        teaches = ex.get("teaches") if isinstance(ex.get("teaches"), list) else []
        locked = lock.get(ex_id)
        if locked is not None:
            now = {"teaches": teaches, "distractor_skills": ex.get("distractor_skills") or {}}
            then = {"teaches": locked.get("teaches", []), "distractor_skills": locked.get("distractor_skills") or {}}
            if now != then:
                errs.append((where, f"locked tags changed (was {then}) -- a reviewed exercise's tags change only with "
                                    f"scripts/lock_tags.py and a reason (indexes/tags.lock.json)"))
        if len(teaches) > 1:
            (errs.append((where, f"teaches {len(teaches)} skills; exactly one is allowed")) if locked is not None
             else warn(lang, "exercise teaches more than one skill", f"{path.name} :: {ex_id}"))
        for slug in teaches:
            if slug in retired:
                warn(lang, "exercise uses a retired slug", f"{path.name} :: {ex_id} ({slug})")
                continue
            s = skills.get(slug)
            if not s:
                continue  # reported by validate_exercise_metadata
            counts[slug] = counts.get(slug, 0) + 1
            if ex_level in LEVELS and s.get("level") in LEVELS and LEVELS.index(s["level"]) > LEVELS.index(ex_level):
                msg = f"{path.name} :: {ex_id} ({slug} is {s['level']}, exercise is {ex_level})"
                (errs.append((where, f"skill {slug!r} is {s['level']}, above this exercise's level ({ex_level})"))
                 if locked is not None else warn(lang, "skill above the exercise's level", msg))
        ds = ex.get("distractor_skills")
        if ds is not None:
            n_opts = len(ex.get("options") or [])
            if not isinstance(ds, dict):
                errs.append((where, "distractor_skills must map an option index to a skill slug"))
            else:
                for k, v in ds.items():
                    if not str(k).isdigit() or int(k) >= n_opts:
                        errs.append((where, f"distractor_skills key {k!r} is not an option index"))
                    if v not in skills or skills[v].get("kind") != "grammar":
                        errs.append((where, f"distractor_skills value {v!r} is not a grammar skill"))
    return errs


def validate_exercise_metadata(data, lang, skill_registry, alias_map=None, kind_map=None):
    meta_errors = []
    alias_map = alias_map or {}
    kind_map = kind_map or {}
    allowed_str = ", ".join(sorted(ALLOWED_EXERCISE_CATEGORIES))
    for idx, ex in enumerate(data.get("exercises", [])):
        ex_id = ex.get("id", f"exercises[{idx}]")
        cat = ex.get("category")
        teaches = ex.get("teaches")

        if not cat:
            meta_errors.append(
                (f"exercises/{idx} ({ex_id})", f"missing required 'category' (must be one of: {allowed_str})")
            )
        elif cat not in ALLOWED_EXERCISE_CATEGORIES:
            meta_errors.append(
                (f"exercises/{idx} ({ex_id})", f"invalid category '{cat}' (must be one of: {allowed_str})")
            )

        if cat != "reading":
            if not isinstance(teaches, list) or len(teaches) == 0:
                meta_errors.append(
                    (f"exercises/{idx} ({ex_id})", "missing or empty 'teaches' (required for all non-reading exercises)")
                )

        if isinstance(teaches, list) and skill_registry is not None:
            for slug in teaches:
                if slug in alias_map:
                    meta_errors.append(
                        (
                            f"exercises/{idx} ({ex_id})",
                            f"teaches slug '{slug}' is an alias; use '{alias_map[slug]}' instead",
                        )
                    )
                elif slug not in skill_registry:
                    meta_errors.append(
                        (
                            f"exercises/{idx} ({ex_id})",
                            f"teaches slug '{slug}' is not in content/{lang}/indexes/skill-registry.json "
                            f"(add it to the registry if it is genuinely new)",
                        )
                    )
                elif cat == "vocabulary" and kind_map.get(slug) == "grammar":
                    meta_errors.append(
                        (
                            f"exercises/{idx} ({ex_id})",
                            f"vocabulary exercise is tagged with grammar skill '{slug}' (kind='grammar'); "
                            f"use a vocabulary theme slug (kind='vocabulary') instead",
                        )
                    )
    return meta_errors


def validate_story_metadata(data, path):
    """Ensure stories have proper tagging and ID conventions so they appear
    correctly in the Library."""
    meta_errors = []
    level = data.get("level")
    story_type = data.get("type") or data.get("category")
    sid = data.get("id", "")

    # C1 stories and any newly added world combined stories must carry topic tags
    if level == "C1":
        has_topics = bool(data.get("vocabularyTopics") or data.get("grammar") or data.get("topics") or data.get("tags"))
        if not has_topics:
            meta_errors.append((
                "topics",
                "missing topic tags (at least one of 'vocabularyTopics', 'grammar', or 'topics' is required for Library discovery)"
            ))

    if story_type == "world":
        # Check if segment or combined
        is_segment = bool(re.search(r"[.\-]\d+([.\-][a-z0-9]+)?$", sid))
        if is_segment:
            if level == "C1" and not sid.startswith("story.") and not re.match(r"^[a-z0-9]+-[a-z0-9]+-\d{2}$", sid):
                meta_errors.append((
                    "id",
                    f"world segment id '{sid}' should follow the segment convention 'story.<level>.<slug>.<num>' or '<level>-<slug>-<num>'"
                ))
        else:
            if level == "C1":
                if not data.get("order"):
                    meta_errors.append(("order", "combined world story must have an 'order' integer field specifying its sequence in the track shelf"))
                if not data.get("estimatedMinutes"):
                    meta_errors.append(("estimatedMinutes", "combined world story must have an 'estimatedMinutes' integer field"))
                if not data.get("vocabularyTopics") and not data.get("grammar"):
                    meta_errors.append(("vocabularyTopics", "combined world story must carry 'vocabularyTopics' or 'grammar' topic tags"))

    return meta_errors


def validate_unit_tracks(data, path):
    """Ensure every non-core track declared in units/*.json is registered in
    engine/reader.js TRACK_SHELF_LABELS so that track shelves display a proper title."""
    meta_errors = []
    reader_js = ROOT / "engine" / "reader.js"
    if not reader_js.exists():
        return meta_errors

    reader_content = reader_js.read_text(encoding="utf-8")
    m = re.search(r"const\s+TRACK_SHELF_LABELS\s*=\s*\{([^}]+)\};", reader_content)
    if not m:
        return meta_errors

    labels_block = m.group(1)
    known_tracks = set(re.findall(r"([a-z0-9_-]+)\s*:", labels_block))

    if isinstance(data, list):
        for idx, u in enumerate(data):
            track = u.get("track")
            if track and track != "core" and track not in known_tracks:
                meta_errors.append((
                    f"units[{idx}] (track='{track}')",
                    f"track '{track}' is not registered in TRACK_SHELF_LABELS in engine/reader.js "
                    f"— register it so the Library can display a human-readable shelf title instead of 'track-{track}'"
                ))
    return meta_errors


# Generated text sometimes slips in letters from another script mid-word
# (Cyrillic "reдукció", katakana "Mキシco", CJK "匿名"). No course content
# uses these scripts, so any occurrence is a generation error.
STRAY_SCRIPT = re.compile(r"[Ѐ-ӿ֐-ۿ฀-๿぀-ヿ㐀-鿿가-힯]+")


def stray_script_errors(path):
    errs = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = STRAY_SCRIPT.search(line)
        if m:
            errs.append((f"line {n}", f"stray non-Latin characters {m.group(0)!r}: {line.strip()[:100]}"))
    return errs


def duplicate_story_id_errors(lang_dir):
    """Two story files with the same id: the Library lists both under one id
    (shared reading progress) and the manifest keeps whichever it reads last.
    Happens when a rewrite adds new files without deleting the old ones."""
    seen = {}
    for path in sorted(lang_dir.glob("stories/**/*.json")):
        if path.name in SKIP:
            continue
        try:
            story_id = json.loads(path.read_text(encoding="utf-8")).get("id")
        except (json.JSONDecodeError, AttributeError):
            continue
        if story_id:
            seen.setdefault(story_id, []).append(path.relative_to(ROOT).as_posix())
    return [f"duplicate story id {sid!r} in: {', '.join(paths)}\n      keep the file a lesson references "
            f"(\"ref\" in content/<course>/lessons) and delete or re-id the other"
            for sid, paths in seen.items() if len(paths) > 1]


def changed_files(ref="origin/master"):
    """Absolute paths of files that differ from `ref`, plus untracked ones."""
    def git(*args):
        out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        return {(ROOT / line).resolve() for line in out.splitlines() if line}
    return git("diff", "--name-only", "--diff-filter=ACMR", ref) | git("ls-files", "--others", "--exclude-standard")


# Every schema a course must carry, and the tag registry its exercises are
# checked against. A new course (Polish, German, ...) copies these from
# content/es-es/ — see AGENTS.md "Adding a new course".
REQUIRED_SCHEMAS = ["lesson", "grammar", "exercises", "vocabulary", "story", "test", "units"]


def has_course_content(lang_dir):
    """True once a course folder holds any lesson or exercise file."""
    return any(lang_dir.glob("lessons/*/*.json")) or any(lang_dir.glob("exercises/*/*.json"))


def course_setup_errors(lang_dir):
    """A course with content but no schemas or tag registry would otherwise be
    skipped silently (nothing validated at all) or have its `teaches` tags
    accepted unchecked. Both must fail loudly instead."""
    errors = []
    rel = lang_dir.relative_to(ROOT)
    missing = [n for n in REQUIRED_SCHEMAS if not (lang_dir / "schemas" / f"{n}.schema.json").is_file()]
    if missing:
        errors.append(
            f"{rel}/schemas: missing {', '.join(m + '.schema.json' for m in missing)} — a course with content "
            f"must carry the full schema set (copy it from content/es-es/schemas; see AGENTS.md \"Adding a new course\")"
        )
    if not (lang_dir / "indexes" / "skill-registry.json").is_file():
        errors.append(
            f"{rel}/indexes/skill-registry.json: missing — every course needs a tag registry so its exercises' "
            f"`teaches` slugs can be checked (see AGENTS.md \"Adding a new course\")"
        )
    return errors


def validate_language(lang, only=None, sources=None):
    lang_dir = ROOT / "content" / lang
    if not has_course_content(lang_dir):
        return 0, 0, []  # an empty or placeholder course folder has nothing to check yet
    touched = only is None or any(str(p).startswith(str(lang_dir.resolve())) for p in only)
    setup_errors = course_setup_errors(lang_dir) if touched else []
    if setup_errors:
        return 0, len(setup_errors), setup_errors

    schemas = load_schemas(lang_dir)
    skill_registry, alias_map, kind_map = load_skill_registry(lang_dir)
    course_src = (sources or {}).get(course_language(lang, sources or {}))
    lock = load_tag_lock(lang_dir)
    skill_counts = {}
    enforce_metadata = METADATA_ENFORCED_EVERYWHERE or (only is not None)
    failures = []
    passed = failed = 0
    skip_marker = SKIP_STEM_MARKERS.get(lang)
    skipped = 0

    if enforce_metadata:
        titles_path = (lang_dir / "indexes" / "grammar-titles.json").resolve()
        if only is None or titles_path in only or any(str(p).startswith(str(lang_dir.resolve())) for p in only):
            title_errs = validate_grammar_titles(lang_dir, lang)
            if title_errs:
                failed += 1
                failures.extend(title_errs)
            elif (lang_dir / "indexes" / "grammar-titles.json").is_file():
                passed += 1

    stories_dir = str((lang_dir / "stories").resolve())
    if only is None or any(str(p).startswith(stories_dir) for p in only):
        dup_errs = duplicate_story_id_errors(lang_dir)
        if dup_errs:
            failed += 1
            failures.extend(dup_errs)

    for name, pattern in TARGETS.items():
        if name not in schemas:
            continue
        validator = Draft7Validator(schemas[name])

        for path in sorted(glob.glob(str(lang_dir / pattern), recursive=True)):
            path = Path(path)
            if path.name in SKIP:
                continue
            if only is not None and path.resolve() not in only:
                continue
            if skip_marker and skip_marker in path.stem:
                skipped += 1
                continue

            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                failed += 1
                failures.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
                continue

            errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
            meta_errors = []
            if name == "exercises" and enforce_metadata:
                meta_errors = validate_exercise_metadata(data, lang, skill_registry, alias_map, kind_map)
                meta_errors += check_exercise_skills(data, path, lang, course_src, lock, skill_counts)
            elif name == "story" and enforce_metadata:
                meta_errors = validate_story_metadata(data, path)
            elif name == "units" and enforce_metadata:
                meta_errors = validate_unit_tracks(data, path)
            meta_errors += stray_script_errors(path)

            if not errors and not meta_errors:
                passed += 1
                continue

            failed += 1
            for err in errors:
                where = "/".join(str(p) for p in err.path) or "(root)"
                failures.append(f"{path.relative_to(ROOT)} :: {where}\n      {err.message}")
            for where, msg in meta_errors:
                failures.append(f"{path.relative_to(ROOT)} :: {where}\n      {msg}")

    if skipped:
        print(f"{lang}: skipped {skipped} unfinished CCSE file(s)")

    # coverage only means something over the whole course, not a --changed subset
    if course_src and only is None and enforce_metadata:
        for slug, s in sorted(course_src.get("skills", {}).items()):
            if s.get("variant") and s["variant"] != lang:
                continue
            n = skill_counts.get(slug, 0)
            if n < MIN_EXERCISES_PER_SKILL:
                warn(lang, f"skill with fewer than {MIN_EXERCISES_PER_SKILL} exercises", f"{slug} ({n})")

    return passed, failed, failures


def main():
    args = sys.argv[1:]
    only = None
    if "--changed" in args:
        args.remove("--changed")
        only = changed_files()
    show_warnings = "--warnings" in args
    if show_warnings:
        args.remove("--warnings")
    langs = args or [p.name for p in (ROOT / "content").iterdir() if p.is_dir()]

    total_failed = 0
    sources, families = load_skill_sources()
    skill_paths = ("/skills/", "/indexes/", "/curriculum/units/", "/grammar/")
    if only is None or any(any(s in p.as_posix() for s in skill_paths) for p in only):
        src_errors = validate_skill_sources(sources, families)
        if src_errors:
            print(f"\nskills: {len(src_errors)} error(s)")
            for e in src_errors:
                print(f"  - {e}")
            total_failed += len(src_errors)
    for lang in sorted(langs):
        passed, failed, failures = validate_language(lang, only, sources)
        if passed == failed == 0:
            continue

        print(f"\n{lang}: {passed} passed, {failed} failed")
        for failure in failures:
            print(f"  - {failure}")
        total_failed += failed

    for lang, kinds in sorted(WARNINGS.items()):
        print(f"\n{lang}: warnings (allowed until the unit is read and locked, ROADMAP 125)")
        for kind, msgs in sorted(kinds.items()):
            print(f"  ~ {kind}: {len(msgs)}")
            for m in (msgs if show_warnings else msgs[:3]):
                print(f"      {m}")
        if not show_warnings:
            print("    (run with --warnings to list them all)")

    print()
    if total_failed:
        print(f"{total_failed} file(s) failed validation")
        return 1

    print("All content files match their schemas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
