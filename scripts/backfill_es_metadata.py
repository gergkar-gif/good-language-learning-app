#!/usr/bin/env python3
"""Backfill missing `category` and `teaches` in es-es and es-latam B1 exercises (Phase 3.1).

Ensures consistency across es-es and es-latam where the same exercise ID exists in both.
"""

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
ALLOWED_CATEGORIES = {"vocabulary", "grammar", "reading", "dialogue", "writing", "listening"}
SKIP_STEM_MARKERS = {"es-es": "-ccse-"}


def build_section_category_map(course):
    """Map exercise ID -> category based on lesson sections."""
    ex_cat = {}
    for lp in (ROOT / "content" / course / "lessons").glob("*/*.json"):
        try:
            ld = json.loads(lp.read_text(encoding="utf-8"))
        except Exception:
            continue
        for sec in ld.get("sections", []):
            title = (sec.get("title") or "").lower()
            cat = None
            if "reading" in title or "lectura" in title or "comprensión" in title:
                cat = "reading"
            elif "dialogue" in title or "diálogo" in title:
                cat = "dialogue"
            elif "writing" in title or "escritura" in title or "producción" in title:
                cat = "writing"
            elif "listening" in title or "escucha" in title or "auditiva" in title:
                cat = "listening"
            elif "vocab" in title or "léxico" in title:
                cat = "vocabulary"
            elif "practice" in title or "práctica" in title or "grammar" in title or "gramática" in title:
                cat = "grammar"
            if cat:
                for eid in sec.get("exerciseRefs", []):
                    ex_cat[eid] = cat
    return ex_cat


def infer_category(ex, sec_cat_map, peer_ex):
    if peer_ex and peer_ex.get("category") in ALLOWED_CATEGORIES:
        return peer_ex["category"]
    eid = ex.get("id", "")
    if eid in sec_cat_map:
        return sec_cat_map[eid]
    ex_type = ex.get("type", "")
    if ex_type == "matching":
        return "vocabulary"
    if ex_type in ("listening-choice", "dictation"):
        return "listening"
    if ex_type == "dialogue-complete":
        return "dialogue"
    if ex_type == "structured-writing":
        return "writing"
    if "reading" in eid or "read" in eid:
        return "reading"
    return "grammar"


def dominant_teaches(exercises, target_cat):
    same_cat = Counter()
    any_cat = Counter()
    for ex in exercises:
        t = ex.get("teaches")
        if isinstance(t, list) and t:
            key = tuple(t)
            any_cat[key] += 1
            if ex.get("category") == target_cat:
                same_cat[key] += 1
    if same_cat:
        return list(same_cat.most_common(1)[0][0])
    if any_cat:
        return list(any_cat.most_common(1)[0][0])
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    # Load registries
    registries = {}
    for c in ("es-es", "es-latam"):
        rp = ROOT / "content" / c / "indexes" / "skill-registry.json"
        registries[c] = json.loads(rp.read_text(encoding="utf-8"))

    # Index all exercises by (relative_file_stem, exercise_id) across both courses
    course_files = {"es-es": {}, "es-latam": {}}
    ex_by_id = {"es-es": {}, "es-latam": {}}
    sec_maps = {c: build_section_category_map(c) for c in ("es-es", "es-latam")}

    for c in ("es-es", "es-latam"):
        skip = SKIP_STEM_MARKERS.get(c)
        for p in sorted((ROOT / "content" / c / "exercises").glob("*/*.json")):
            if skip and skip in p.stem:
                continue
            data = json.loads(p.read_text(encoding="utf-8"))
            rel = p.relative_to(ROOT / "content" / c).as_posix()
            course_files[c][rel] = (p, data)
            for ex in data.get("exercises", []):
                if ex.get("id"):
                    ex_by_id[c][ex["id"]] = ex

    samples = []
    stats = {c: Counter() for c in ("es-es", "es-latam")}
    reg_changed = {"es-es": False, "es-latam": False}

    for c in ("es-es", "es-latam"):
        peer_c = "es-latam" if c == "es-es" else "es-es"
        for rel, (path, data) in course_files[c].items():
            changed = False
            exercises = data.get("exercises", [])
            # First pass: fix missing categories or untagged exercises in a Reading section
            for ex in exercises:
                if ex.get("category") not in ALLOWED_CATEGORIES:
                    peer_ex = ex_by_id[peer_c].get(ex.get("id"))
                    new_cat = infer_category(ex, sec_maps[c], peer_ex)
                    ex["category"] = new_cat
                    stats[c]["fixed_category"] += 1
                    changed = True
                elif not ex.get("teaches") and sec_maps[c].get(ex.get("id")) == "reading":
                    ex["category"] = "reading"
                    stats[c]["fixed_reading_category"] += 1
                    changed = True

            # Second pass: fix missing teaches on non-reading exercises
            for ex in exercises:
                cat = ex.get("category")
                if cat == "reading":
                    continue
                t = ex.get("teaches")
                if isinstance(t, list) and len(t) > 0:
                    continue

                peer_ex = ex_by_id[peer_c].get(ex.get("id"))
                peer_t = peer_ex.get("teaches") if peer_ex else None
                if isinstance(peer_t, list) and len(peer_t) > 0:
                    new_t = list(peer_t)
                    source = f"peer_{peer_c}"
                else:
                    new_t = dominant_teaches(exercises, cat)
                    source = "sibling_dominant"

                if not new_t:
                    stats[c]["unresolved_teaches"] += 1
                    continue

                # Ensure every slug in new_t is in registries[c]
                for slug in new_t:
                    if slug not in registries[c]["skills"]:
                        peer_skill = registries[peer_c]["skills"].get(slug, {"title": "", "kind": "grammar"})
                        registries[c]["skills"][slug] = dict(peer_skill)
                        reg_changed[c] = True

                ex["teaches"] = new_t
                stats[c]["fixed_teaches"] += 1
                changed = True
                prompt_text = ex.get("question") or ex.get("sentence") or ex.get("english") or str(ex.get("pairs", "")[:2])
                samples.append((c, rel, ex.get("id"), cat, new_t, source, prompt_text))

            if changed and args.write:
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
                stats[c]["files_written"] += 1

    if args.write:
        for c in ("es-es", "es-latam"):
            if reg_changed[c]:
                rp = ROOT / "content" / c / "indexes" / "skill-registry.json"
                registries[c]["skills"] = dict(sorted(registries[c]["skills"].items()))
                with open(rp, "w", encoding="utf-8", newline="\n") as f:
                    f.write(json.dumps(registries[c], ensure_ascii=False, indent=2) + "\n")
                print(f"[{c}] Updated skill-registry.json with peer skills")

    for c in ("es-es", "es-latam"):
        print(f"=== {c}: {dict(stats[c])} ===")

    rng = random.Random(42)
    picked = rng.sample(samples, min(30, len(samples)))
    print("\n=== 30 Random Tagged Spanish Exercises ===")
    for c, rel, eid, cat, new_t, src, txt in picked:
        print(f"  [{c} :: {eid}] ({cat}, {src}) -> teaches={new_t} | {txt[:80]}")


if __name__ == "__main__":
    main()
