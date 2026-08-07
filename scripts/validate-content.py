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

Exits non-zero if anything fails, so it can gate a commit.
"""

import glob
import json
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
}

SKIP = {"manifest.json", "lessons-manifest.json"}


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


def validate_language(lang):
    lang_dir = ROOT / "content" / lang
    if not (lang_dir / "schemas").exists():
        return 0, 0, []

    schemas = load_schemas(lang_dir)
    failures = []
    passed = failed = 0

    for name, pattern in TARGETS.items():
        if name not in schemas:
            continue
        validator = Draft7Validator(schemas[name])

        for path in sorted(glob.glob(str(lang_dir / pattern), recursive=True)):
            path = Path(path)
            if path.name in SKIP:
                continue

            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                failed += 1
                failures.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
                continue

            errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
            if not errors:
                passed += 1
                continue

            failed += 1
            for err in errors:
                where = "/".join(str(p) for p in err.path) or "(root)"
                failures.append(f"{path.relative_to(ROOT)} :: {where}\n      {err.message}")

    return passed, failed, failures


def main():
    langs = sys.argv[1:] or [p.name for p in (ROOT / "content").iterdir() if p.is_dir()]

    total_failed = 0
    for lang in sorted(langs):
        passed, failed, failures = validate_language(lang)
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
