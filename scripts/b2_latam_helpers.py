#!/usr/bin/env python3
"""
Common helper utilities for generating Spanish (LatAm) B2 content files.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "content" / "es-latam"


def write_json(rel_path: str, data: dict):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def make_lesson(
    stem: str,
    unit_num: int,
    title: str,
    goal: str,
    grammar_desc: str,
    grammar_ref: str,
    vocab_ref: str,
    ex_ref: str,
    ex_ids: list,
    goals: list,
    story_ref: str = None,
    intro_body: list = None,
    intro_title: str = None,
) -> dict:
    parts = stem.split("-")
    if len(parts) == 3 and parts[1].isdigit():
        lesson_id = f"lesson.b2.{parts[1]}.{parts[2]}"
    elif len(parts) == 3:
        lesson_id = f"lesson.b2.{parts[1]}.{parts[2]}"
    else:
        lesson_id = f"lesson.b2.{stem}"

    sections = []
    if intro_body:
        sections.append({
            "type": "intro",
            "title": intro_title or title,
            "body": intro_body
        })

    sections.append({
        "type": "goal",
        "items": goals
    })
    sections.append({
        "type": "recycle",
        "count": 3
    })

    if story_ref:
        sections.append({
            "type": "story",
            "ref": story_ref
        })

    sections.append({
        "type": "grammar",
        "ref": grammar_ref
    })
    sections.append({
        "type": "vocabulary",
        "ref": vocab_ref
    })

    practice_ids = [eid for eid in ex_ids if not eid.endswith(".ex06") and not eid.endswith(".ex05")]
    sections.append({
        "type": "exercise-group",
        "title": "Practice",
        "ref": ex_ref,
        "exerciseRefs": practice_ids if practice_ids else ex_ids[:4]
    })

    if any(eid.endswith(".ex06") for eid in ex_ids):
        sections.append({
            "type": "exercise-group",
            "title": "Listening",
            "ref": ex_ref,
            "exerciseRefs": [eid for eid in ex_ids if eid.endswith(".ex06")]
        })

    if any(eid.endswith(".ex05") for eid in ex_ids):
        sections.append({
            "type": "exercise-group",
            "title": "Dialogue",
            "ref": ex_ref,
            "exerciseRefs": [eid for eid in ex_ids if eid.endswith(".ex05")]
        })

    return {
        "id": lesson_id,
        "title": title,
        "level": "B2",
        "goal": goal,
        "grammar": grammar_desc,
        "sections": sections
    }


def make_consolidation_lesson(
    stem: str,
    unit_num: int,
    title: str,
    goal: str,
    grammar_desc: str,
    ex_ref: str,
    ex_ids: list,
    goals: list,
    checklist_items: list,
    story_ref: str = None,
) -> dict:
    parts = stem.split("-")
    if len(parts) >= 2 and parts[1].isdigit():
        lesson_id = f"lesson.b2.{parts[1]}.consolidation"
    elif len(parts) >= 2:
        lesson_id = f"lesson.b2.{parts[1]}.consolidation"
    else:
        lesson_id = f"lesson.b2.{stem}"

    sections = [
        {
            "type": "goal",
            "items": goals
        },
        {
            "type": "recycle",
            "count": 3
        }
    ]

    if story_ref:
        sections.append({
            "type": "story",
            "ref": story_ref
        })

    sections.append({
        "type": "exercise-group",
        "title": "Review",
        "ref": ex_ref,
        "exerciseRefs": ex_ids
    })

    sections.append({
        "type": "checklist",
        "items": checklist_items
    })

    return {
        "id": lesson_id,
        "title": title,
        "level": "B2",
        "goal": goal,
        "grammar": grammar_desc,
        "sections": sections
    }
