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


def validate_language(lang, only=None):
    lang_dir = ROOT / "content" / lang
    if not has_course_content(lang_dir):
        return 0, 0, []  # an empty or placeholder course folder has nothing to check yet
    touched = only is None or any(str(p).startswith(str(lang_dir.resolve())) for p in only)
    setup_errors = course_setup_errors(lang_dir) if touched else []
    if setup_errors:
        return 0, len(setup_errors), setup_errors

    schemas = load_schemas(lang_dir)
    skill_registry, alias_map, kind_map = load_skill_registry(lang_dir)
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

    return passed, failed, failures


def main():
    args = sys.argv[1:]
    only = None
    if "--changed" in args:
        args.remove("--changed")
        only = changed_files()
    langs = args or [p.name for p in (ROOT / "content").iterdir() if p.is_dir()]

    total_failed = 0
    for lang in sorted(langs):
        passed, failed, failures = validate_language(lang, only)
        if passed == failed == 0:
            continue

        print(f"\n{lang}: {passed} passed, {failed} failed")
        for failure in failures:
            print(f"  - {failure}")
        total_failed += failed

    print()
    if total_failed:
        print(f"{total_failed} file(s) failed validation")
        return 1

    print("All content files match their schemas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
