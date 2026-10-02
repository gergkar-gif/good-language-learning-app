#!/usr/bin/env python3
"""
Shared helpers and building blocks for Hungarian C1 generation.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
BASE = ROOT / "content" / "hu"


def write_json(rel_path: str, data: dict):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def mc(cat, stage, question, options, correct, teaches=None):
    res = {
        "id": "",
        "type": "multiple-choice",
        "category": cat,
        "stage": stage,
        "question": question,
        "options": options,
        "correct": correct,
    }
    if teaches:
        res["teaches"] = teaches
    return res


def match(cat, stage, pairs, teaches):
    formatted_pairs = []
    for p in pairs:
        if isinstance(p, (list, tuple)):
            formatted_pairs.append([str(p[0]), str(p[1])])
        elif isinstance(p, dict):
            formatted_pairs.append([str(p.get("left", "")), str(p.get("right", ""))])
    return {
        "id": "",
        "type": "matching",
        "category": cat,
        "stage": stage,
        "pairs": formatted_pairs,
        "teaches": teaches,
    }


def fb(cat, stage, sentence, answer, english, teaches):
    assert "____" in sentence, f"Sentence must contain blank '____': {sentence}"
    assert english and len(english.strip()) > 0, "English translation required for fill-blank"
    return {
        "id": "",
        "type": "fill-blank",
        "category": cat,
        "stage": stage,
        "sentence": sentence,
        "answer": answer,
        "english": english,
        "teaches": teaches,
    }


def sb(cat, stage, tiles, solution, english, teaches):
    return {
        "id": "",
        "type": "sentence-builder",
        "category": cat,
        "stage": stage,
        "tiles": tiles,
        "solution": solution,
        "english": english,
        "teaches": teaches,
    }


def dc(stage, dialogue_items, options, correct, teaches):
    assert isinstance(dialogue_items, list) and len(dialogue_items) >= 2, "Dialogue must have at least 2 turns"
    # Ensure exactly one turn contains "_____"
    turns = []
    has_blank = False
    for item in dialogue_items:
        turns.append({"speaker": str(item["speaker"]), "text": str(item["text"])})
        if "____" in item["text"]:
            has_blank = True
    if not has_blank:
        # If no blank was explicitly placed, mark the last speaker's line as "_____"
        turns[-1]["text"] = "_____"

    return {
        "id": "",
        "type": "dialogue-complete",
        "category": "dialogue",
        "stage": stage,
        "prompt": turns,
        "options": options,
        "correct": correct,
        "teaches": teaches,
    }


def sw(stage, template, teaches):
    return {
        "id": "",
        "type": "structured-writing",
        "category": "writing",
        "stage": stage,
        "template": template,
        "teaches": teaches,
    }


def emit_instructional_lesson(unit_num: int, track_type: str, l_data: dict, unit_title: str, unit_intro=None):
    stem = l_data["stem"]
    num = l_data["num"]
    goals = l_data["goals"]
    title = l_data["title"]
    grammar_title = l_data["grammar_title"]
    grammar_skill = l_data["grammar_skill"]
    vocab_list = l_data["vocab"]

    # 1. Vocabulary file
    track_slug = f"{unit_num:02d}" if track_type == "core" else stem.split("-")[1]
    write_json(
        f"vocabulary/c1/{stem}-voc.json",
        {
            "id": f"vocab.c1.{track_slug}.{num:02d}",
            "lesson": stem,
            "title": f"C1 Vocabulary — {title}",
            "theme": unit_title,
            "words": vocab_list,
        },
    )

    # 2. Grammar file
    gr_slug = grammar_skill.replace("c1-", "")
    write_json(
        f"grammar/c1/{stem}-a-gr.json",
        {
            "id": f"grammar.c1.{track_slug}.{num:02d}.{gr_slug}",
            "title": grammar_title,
            "sections": [
                {"type": "text", "title": "The Structural Mechanism", "content": l_data["gr_text1"]},
                {"type": "text", "title": "Rhetorical Application & Stance", "content": l_data["gr_text2"]},
                {"type": "table", "title": "Patterns in Context", "rows": l_data["gr_table"]},
            ],
        },
    )

    # 3. Exercises file
    ex_list = []
    for idx, ex in enumerate(l_data["exercises"], start=1):
        ex_copy = dict(ex)
        if ex_copy["category"] == "reading":
            ex_copy["id"] = f"{stem}-reading-{idx}"
        else:
            stage = ex_copy.get("stage", "practice")
            ex_copy["id"] = f"{stem}-{stage}-{idx}"
        ex_list.append(ex_copy)

    write_json(f"exercises/c1/{stem}-ex.json", {"lesson": stem, "exercises": ex_list})

    # 4. Stories
    if "classic_story" in l_data:
        s = l_data["classic_story"]
        write_json(
            f"stories/classics/c1/{s['slug']}.json",
            {
                "id": f"story.c1.classics.{s['slug']}",
                "title": s["title"],
                "level": "C1",
                "type": "classic",
                "author": s["author"],
                "work": s["work"],
                "summary": s["summary"],
                "characters": s.get("characters", []),
                "paragraphs": s["paragraphs"],
            },
        )
    elif "world_story_seg" in l_data:
        s = l_data["world_story_seg"]
        write_json(
            f"stories/world/c1/{stem}-{s['seg_slug']}.json",
            {
                "id": f"story.c1.world.{stem}-{s['seg_slug']}",
                "title": s["title"],
                "level": "C1",
                "lesson": num,
                "order": num,
                "type": "world",
                "summary": s["summary"],
                "paragraphs": s["paragraphs"],
            },
        )

    # 5. Lesson JSON
    sections = []
    if num == 1 and unit_intro:
        sections.append({"type": "intro", "title": f"Unit {unit_num}: {unit_title}", "body": unit_intro})
    sections.append({"type": "goal", "title": "Lesson Goals", "items": goals})
    sections.append({"type": "recycle", "title": "Quick Review"})
    sections.append({"type": "grammar", "title": grammar_title, "ref": f"grammar/c1/{stem}-a-gr.json"})
    sections.append({"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/c1/{stem}-voc.json"})

    # Groups
    intro_refs = [e["id"] for e in ex_list if e.get("stage") == "introduce"]
    if intro_refs:
        sections.append({"type": "exercise-group", "title": "Introduce", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": intro_refs})

    controlled_refs = [e["id"] for e in ex_list if e.get("stage") == "controlled"]
    if controlled_refs:
        sections.append({"type": "exercise-group", "title": "Controlled", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": controlled_refs})

    practice_refs = [e["id"] for e in ex_list if e.get("stage") == "practice" and e.get("category") != "reading"]
    if practice_refs:
        sections.append({"type": "exercise-group", "title": "Practice", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": practice_refs})

    if "classic_story" in l_data:
        sections.append({"type": "story", "title": f"Reading: {l_data['classic_story']['title']}", "ref": f"stories/classics/c1/{l_data['classic_story']['slug']}.json"})
        reading_refs = [e["id"] for e in ex_list if e.get("category") == "reading"]
        if reading_refs:
            sections.append({"type": "exercise-group", "title": "Reading Comprehension", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": reading_refs})
    elif "world_story_seg" in l_data:
        s = l_data["world_story_seg"]
        sections.append({"type": "story", "title": f"Story: {s['title']}", "ref": f"stories/world/c1/{stem}-{s['seg_slug']}.json"})

    dialogue_refs = [e["id"] for e in ex_list if e.get("stage") == "dialogue" or e.get("category") == "dialogue"]
    if dialogue_refs:
        sections.append({"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": dialogue_refs})

    prod_refs = [e["id"] for e in ex_list if e.get("stage") == "production" or e.get("category") == "writing"]
    if prod_refs:
        sections.append({"type": "exercise-group", "title": "Production", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": prod_refs})

    sections.append({"type": "srs", "title": "Add to Review"})

    check_refs = [e["id"] for e in ex_list if e.get("stage") == "check"]
    if check_refs:
        sections.append({"type": "exercise-group", "title": "Check", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": check_refs})

    sections.append({"type": "checklist", "title": "Can you do this?", "items": goals})

    lesson_json = {
        "id": f"lesson.c1.{stem[3:]}",
        "unit": unit_num,
        "title": title,
        "level": "C1",
        "grammar": grammar_title,
        "goal": goals,
        "sections": sections,
    }
    write_json(f"lessons/c1/{stem}.json", lesson_json)


def emit_consolidation_lesson(unit_num: int, track_type: str, cons_stem: str, unit_title: str, cons_goals: list, cons_exercises: list):
    c_ex_list = []
    for idx, ex in enumerate(cons_exercises, start=1):
        ex_copy = dict(ex)
        ex_copy["id"] = f"{cons_stem}-{idx}"
        c_ex_list.append(ex_copy)

    write_json(f"exercises/c1/{cons_stem}-ex.json", {"lesson": cons_stem, "exercises": c_ex_list})

    rec_refs = [c_ex_list[i]["id"] for i in range(min(3, len(c_ex_list)))]
    recall_refs = [c_ex_list[i]["id"] for i in range(3, min(6, len(c_ex_list)))]
    context_refs = [c_ex_list[i]["id"] for i in range(6, min(9, len(c_ex_list)))]
    produce_refs = [c_ex_list[i]["id"] for i in range(9, len(c_ex_list))]

    cons_sections = [
        {"type": "goal", "title": "Consolidation Goals", "items": cons_goals},
        {"type": "recycle", "title": "Quick Review"},
        {"type": "exercise-group", "title": "Recognize", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": rec_refs},
        {"type": "exercise-group", "title": "Recall", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": recall_refs},
        {"type": "exercise-group", "title": "In Context", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": context_refs},
        {"type": "exercise-group", "title": "Produce", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": produce_refs},
        {"type": "checklist", "title": "Can you do this?", "items": cons_goals},
    ]

    write_json(
        f"lessons/c1/{cons_stem}.json",
        {
            "id": f"lesson.c1.{cons_stem[3:]}",
            "unit": unit_num,
            "title": f"Unit {unit_num} Consolidation: {unit_title}",
            "level": "C1",
            "grammar": "Review and Capstone Integration",
            "goal": cons_goals,
            "sections": cons_sections,
        },
    )
