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


def load_skill_registry(lang_dir):
    reg_path = lang_dir / "indexes" / "skill-registry.json"
    if not reg_path.is_file():
        return None
    try:
        data = json.loads(reg_path.read_text(encoding="utf-8"))
        return set((data.get("skills") or {}).keys())
    except Exception:
        return None


def validate_exercise_metadata(data, lang, skill_registry):
    meta_errors = []
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
                if slug not in skill_registry:
                    meta_errors.append(
                        (
                            f"exercises/{idx} ({ex_id})",
                            f"teaches slug '{slug}' is not in content/{lang}/indexes/skill-registry.json "
                            f"(add it to the registry if it is genuinely new)",
                        )
                    )
    return meta_errors


def changed_files(ref="origin/master"):
    """Absolute paths of files that differ from `ref`, plus untracked ones."""
    def git(*args):
        out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        return {(ROOT / line).resolve() for line in out.splitlines() if line}
    return git("diff", "--name-only", "--diff-filter=ACMR", ref) | git("ls-files", "--others", "--exclude-standard")


def validate_language(lang, only=None):
    lang_dir = ROOT / "content" / lang
    if not (lang_dir / "schemas").exists():
        return 0, 0, []

    schemas = load_schemas(lang_dir)
    skill_registry = load_skill_registry(lang_dir)
    enforce_metadata = METADATA_ENFORCED_EVERYWHERE or (only is not None)
    failures = []
    passed = failed = 0
    skip_marker = SKIP_STEM_MARKERS.get(lang)
    skipped = 0

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
                meta_errors = validate_exercise_metadata(data, lang, skill_registry)

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
