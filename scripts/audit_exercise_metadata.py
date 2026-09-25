#!/usr/bin/env python3
"""Audit exercise metadata (`category` and `teaches`) across courses and levels.

Reports per course and level:
- exercise count
- missing `teaches` (excluding `category == "reading"`)
- missing `category`
- off-list `category` (not in the 6 standard categories)
- off-registry `teaches` (if content/<course>/indexes/skill-registry.json exists)
- distinct tags and tags used once (per course and per level)

Usage:
    python scripts/audit_exercise_metadata.py
    python scripts/audit_exercise_metadata.py --files
    python scripts/audit_exercise_metadata.py es-es hu --files
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
# Every course folder, so a new language is audited without editing this list.
COURSES = sorted(p.name for p in (ROOT / "content").iterdir() if p.is_dir())
ALLOWED_CATEGORIES = {"vocabulary", "grammar", "reading", "dialogue", "writing", "listening"}
SKIP_STEM_MARKERS = {"es-es": "-ccse-"}


def load_skill_registry(course):
    reg_path = ROOT / "content" / course / "indexes" / "skill-registry.json"
    if not reg_path.is_file():
        return None
    try:
        data = json.loads(reg_path.read_text(encoding="utf-8"))
        return set((data.get("skills") or {}).keys())
    except Exception:
        return None


def audit_course(course, show_files=False):
    ex_dir = ROOT / "content" / course / "exercises"
    if not ex_dir.is_dir():
        return None

    skip_marker = SKIP_STEM_MARKERS.get(course)
    registry = load_skill_registry(course)

    course_tags = Counter()
    level_stats = {}
    failing_files = defaultdict(list)

    for level_dir in sorted(p for p in ex_dir.iterdir() if p.is_dir()):
        level = level_dir.name.upper()
        stats = {
            "files": 0,
            "exercises": 0,
            "missing_teaches": 0,
            "missing_category": 0,
            "offlist_category": 0,
            "offregistry_tags": 0,
            "tags": Counter(),
            "offlist_categories": Counter(),
        }

        for path in sorted(level_dir.glob("*.json")):
            if skip_marker and skip_marker in path.stem:
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                failing_files[level].append((path.relative_to(ROOT).as_posix(), f"invalid JSON: {exc}"))
                continue

            stats["files"] += 1
            file_issues = []
            for ex in data.get("exercises", []):
                stats["exercises"] += 1
                cat = ex.get("category")
                teaches = ex.get("teaches")

                if not cat:
                    stats["missing_category"] += 1
                    file_issues.append(f"{ex.get('id', '?')}: missing category")
                elif cat not in ALLOWED_CATEGORIES:
                    stats["offlist_category"] += 1
                    stats["offlist_categories"][cat] += 1
                    file_issues.append(f"{ex.get('id', '?')}: off-list category '{cat}'")

                if cat != "reading":
                    if not isinstance(teaches, list) or len(teaches) == 0:
                        stats["missing_teaches"] += 1
                        file_issues.append(f"{ex.get('id', '?')}: missing teaches")

                if isinstance(teaches, list):
                    for slug in teaches:
                        if isinstance(slug, str) and slug:
                            stats["tags"][slug] += 1
                            course_tags[slug] += 1
                            if registry is not None and slug not in registry:
                                stats["offregistry_tags"] += 1
                                file_issues.append(f"{ex.get('id', '?')}: unregistered tag '{slug}'")

            if file_issues:
                failing_files[level].append((path.relative_to(ROOT).as_posix(), f"{len(file_issues)} issue(s): " + "; ".join(file_issues[:4]) + (" ..." if len(file_issues) > 4 else "")))

        level_stats[level] = stats

    return {
        "course": course,
        "levels": level_stats,
        "course_tags": course_tags,
        "failing_files": failing_files,
        "has_registry": registry is not None,
    }


def main():
    parser = argparse.ArgumentParser(description="Audit exercise metadata across courses.")
    parser.add_argument("courses", nargs="*", default=COURSES, help="Courses to audit (default: every folder under content/)")
    parser.add_argument("--files", "--show-files", dest="show_files", action="store_true", help="Print files that fail checks")
    args = parser.parse_args()

    total_issues = 0

    for course in args.courses:
        result = audit_course(course, show_files=args.show_files)
        if not result:
            continue

        course_tags = result["course_tags"]
        single_use_course = sum(1 for _, c in course_tags.items() if c == 1)
        total_ex = sum(s["exercises"] for s in result["levels"].values())
        total_miss_t = sum(s["missing_teaches"] for s in result["levels"].values())
        total_miss_c = sum(s["missing_category"] for s in result["levels"].values())
        total_off_c = sum(s["offlist_category"] for s in result["levels"].values())
        total_off_r = sum(s["offregistry_tags"] for s in result["levels"].values())

        total_issues += total_miss_t + total_miss_c + total_off_c + total_off_r

        print(f"=== {course} (total exercises: {total_ex:,} | distinct tags: {len(course_tags):,} | single-use tags: {single_use_course:,}) ===")
        header = f"  {'Level':<6} {'Files':>6} {'Exercises':>10} {'MissTeaches':>12} {'MissCat':>9} {'OffListCat':>11}"
        if result["has_registry"]:
            header += f" {'OffRegTag':>10}"
        header += f" {'DistinctTags':>13} {'UsedOnce':>9}"
        print(header)

        for level, s in sorted(result["levels"].items()):
            used_once_lvl = sum(1 for _, c in s["tags"].items() if c == 1)
            row = (
                f"  {level:<6} {s['files']:>6} {s['exercises']:>10,} "
                f"{s['missing_teaches']:>12,} {s['missing_category']:>9,} {s['offlist_category']:>11,}"
            )
            if result["has_registry"]:
                row += f" {s['offregistry_tags']:>10,}"
            row += f" {len(s['tags']):>13,} {used_once_lvl:>9,}"
            print(row)

            if s["offlist_categories"]:
                top_off = ", ".join(f"{k}({v})" for k, v in s["offlist_categories"].most_common(10))
                print(f"         off-list categories: {top_off}")

        if args.show_files:
            for level, items in sorted(result["failing_files"].items()):
                if items:
                    print(f"  -- Failing files in {course}/{level} ({len(items)}):")
                    for rel_path, summary in items:
                        print(f"     {rel_path}: {summary}")
        print()

    return 1 if total_issues > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
