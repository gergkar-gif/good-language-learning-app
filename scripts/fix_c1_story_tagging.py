#!/usr/bin/env python3
"""
Fix C1 story tagging, metadata, and IDs across Hungarian C1 readings:
- 12 C1 Classics stories: add order, lesson, estimatedMinutes, type='classics', source, grammar, vocabularyTopics
- 59 C1 World segment stories: standardize IDs to story.c1.{slug}.{num:02d}, add order, lesson, estimatedMinutes, grammar, vocabularyTopics
- 12 C1 World combined stories: standardize filenames to c1-{slug}.json, IDs to story.c1.{slug}, add order, lesson, estimatedMinutes, grammar, vocabularyTopics
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HU_DIR = ROOT / "content" / "hu"
UNITS_FILE = HU_DIR / "curriculum" / "units" / "c1.json"
LESSONS_DIR = HU_DIR / "lessons" / "c1"
GRAMMAR_DIR = HU_DIR / "grammar" / "c1"
VOCAB_DIR = HU_DIR / "vocabulary" / "c1"
EX_DIR = HU_DIR / "exercises" / "c1"
CLASSICS_DIR = HU_DIR / "stories" / "classics" / "c1"
WORLD_DIR = HU_DIR / "stories" / "world" / "c1"


def get_lesson_grammar_skill(stem):
    ex_file = EX_DIR / f"{stem}-ex.json"
    if ex_file.exists():
        ex_data = json.loads(ex_file.read_text(encoding="utf-8"))
        for ex in ex_data.get("exercises", []):
            if ex.get("category") == "grammar" and ex.get("teaches"):
                return ex["teaches"][0]
    gr_file = GRAMMAR_DIR / f"{stem}-a-gr.json"
    if gr_file.exists():
        gr_data = json.loads(gr_file.read_text(encoding="utf-8"))
        # id like grammar.c1.01.05.concessives
        parts = gr_data.get("id", "").split(".")
        if len(parts) >= 5:
            return f"c1-{parts[-1]}"
    return "c1-advanced-grammar"


def get_lesson_vocab_theme(stem, fallback_unit_title):
    voc_file = VOCAB_DIR / f"{stem}-voc.json"
    if voc_file.exists():
        voc_data = json.loads(voc_file.read_text(encoding="utf-8"))
        theme = voc_data.get("theme") or fallback_unit_title
        title = voc_data.get("title", "").replace("C1 Vocabulary — ", "")
        return theme, title
    return fallback_unit_title, stem


def fix_c1_classics(core_units):
    print("Fixing C1 Classics stories...")
    for idx, unit in enumerate(core_units, 1):
        unit_title = unit["title"]
        stems = [s for s in unit.get("stems", []) if not s.endswith("-consolidation")]
        lesson_stem = stems[-1] if stems else f"c1-{idx:02d}-05"
        
        # Look for classic story in lesson or by index
        lesson_file = LESSONS_DIR / f"{lesson_stem}.json"
        story_rel = None
        if lesson_file.exists():
            ldata = json.loads(lesson_file.read_text(encoding="utf-8"))
            for sec in ldata.get("sections", []):
                if sec.get("type") == "story" and sec.get("ref"):
                    story_rel = sec["ref"]
                    break

        classic_path = None
        if story_rel:
            classic_path = HU_DIR / story_rel
        if not classic_path or not classic_path.exists():
            # Try matching c1-{idx:02d}-*.json
            candidates = list(CLASSICS_DIR.glob(f"c1-{idx:02d}-*.json"))
            if candidates:
                classic_path = candidates[0]

        if not classic_path or not classic_path.exists():
            print(f"  [WARN] Missing classic story for Unit {idx}")
            continue

        data = json.loads(classic_path.read_text(encoding="utf-8"))
        words = sum(len((p.get("text") or "").split()) for p in data.get("paragraphs", []))
        gr_skill = get_lesson_grammar_skill(lesson_stem)
        author = data.get("author", "Unknown Author")
        work = data.get("work", "")

        data["order"] = idx
        data["lesson"] = 5
        data["type"] = "classics"
        data["estimatedMinutes"] = max(5, round(words / 120))
        data["source"] = f"Adapted for C1 learners from {author}, {work}" if work else f"Adapted for C1 learners from {author}"
        data["grammar"] = [gr_skill]
        data["vocabularyTopics"] = [unit_title]

        classic_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  Updated classic: {classic_path.name} (order={idx}, grammar={gr_skill})")


def fix_c1_world(disc_units):
    print("\nFixing C1 World segment and combined stories...")
    for idx, unit in enumerate(disc_units, 1):
        unit_title = unit["title"]
        stems = [s for s in unit.get("stems", []) if not s.endswith("-consolidation")]
        if not stems:
            continue

        slug = stems[0].split("-")[1]
        all_paras = []
        all_grammar = []
        all_topics = [unit_title]

        # 1. Update segment stories
        for num, stem in enumerate(stems, 1):
            lesson_file = LESSONS_DIR / f"{stem}.json"
            if not lesson_file.exists():
                continue
            ldata = json.loads(lesson_file.read_text(encoding="utf-8"))
            seg_rel = None
            for sec in ldata.get("sections", []):
                if sec.get("type") == "story" and sec.get("ref"):
                    seg_rel = sec["ref"]
                    break

            if not seg_rel:
                continue

            seg_path = HU_DIR / seg_rel
            if not seg_path.exists():
                print(f"  [WARN] Missing segment file at {seg_path}")
                continue

            seg_data = json.loads(seg_path.read_text(encoding="utf-8"))
            words = sum(len((p.get("text") or "").split()) for p in seg_data.get("paragraphs", []))
            gr_skill = get_lesson_grammar_skill(stem)
            theme, lesson_title = get_lesson_vocab_theme(stem, unit_title)

            # Standard segment ID: story.c1.{slug}.{num:02d}
            seg_data["id"] = f"story.c1.{slug}.{num:02d}"
            seg_data["order"] = num
            seg_data["lesson"] = num
            seg_data["type"] = "world"
            seg_data["estimatedMinutes"] = max(3, round(words / 120))
            seg_data["grammar"] = [gr_skill]
            seg_data["vocabularyTopics"] = [theme, lesson_title]

            seg_path.write_text(json.dumps(seg_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"  Updated segment: {seg_path.name} -> ID {seg_data['id']}")

            all_paras.extend(seg_data.get("paragraphs", []))
            if gr_skill not in all_grammar:
                all_grammar.append(gr_skill)
            if lesson_title not in all_topics:
                all_topics.append(lesson_title)

        # 2. Update combined story
        combined_candidates = [
            WORLD_DIR / f"c1-{slug}.json",
            WORLD_DIR / f"{slug}.json"
        ]
        target_path = WORLD_DIR / f"c1-{slug}.json"
        existing_combined = None
        old_path = None

        for c in combined_candidates:
            if c.exists():
                existing_combined = json.loads(c.read_text(encoding="utf-8"))
                old_path = c
                break

        if not existing_combined:
            print(f"  [WARN] Missing combined story for {slug}")
            continue

        # Use the combined story's paragraphs if it has a custom cohesive narrative,
        # or stitched paragraphs if combined is empty/short
        comb_paras = existing_combined.get("paragraphs", [])
        if len(comb_paras) < 3 and all_paras:
            comb_paras = all_paras

        total_words = sum(len((p.get("text") or "").split()) for p in comb_paras)

        combined_data = {
            "id": f"story.c1.{slug}",
            "title": existing_combined.get("title") or unit_title,
            "level": "C1",
            "type": "world",
            "order": idx,
            "lesson": 5,
            "estimatedMinutes": max(8, round(total_words / 110)),
            "summary": existing_combined.get("summary", ""),
            "grammar": all_grammar,
            "vocabularyTopics": all_topics,
            "paragraphs": comb_paras
        }

        # Save to target c1-{slug}.json
        target_path.write_text(json.dumps(combined_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  Updated combined: {target_path.name} -> ID {combined_data['id']} (order={idx})")

        # Clean up old slug.json if different from target_path
        if old_path and old_path != target_path and old_path.exists():
            old_path.unlink()
            print(f"  Removed obsolete duplicate {old_path.name}")


def main():
    units = json.loads(UNITS_FILE.read_text(encoding="utf-8"))
    core_units = [u for u in units if u.get("track") == "core"]
    disc_units = [u for u in units if u.get("track") == "discourse"]
    print(f"Loaded {len(core_units)} core units and {len(disc_units)} discourse units")
    fix_c1_classics(core_units)
    fix_c1_world(disc_units)
    print("\nMigration complete.")


if __name__ == "__main__":
    main()
