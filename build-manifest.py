#!/usr/bin/env python3
import json
import os
from pathlib import Path

BASE_STORIES = Path("content/stories")
BASE_LESSONS = Path("content/lessons")
CATEGORIES = ["original", "classics", "world"]

def extract_level(name):
    parts = name.split("-")
    return parts[0].upper() if parts else "Unknown"

def extract_number(name):
    parts = name.split("-")
    return parts[1] if len(parts) > 1 else "00"

def build_stories():
    stories = []
    for cat in CATEGORIES:
        cat_path = BASE_STORIES / cat
        if not cat_path.exists():
            continue
        for f in sorted(cat_path.glob("*.json")):
            if f.name == "manifest.json":
                continue
            stem = f.stem
            parts = stem.split("-", 2)
            level = parts[0].upper() if len(parts) > 0 else "Unknown"
            number = parts[1] if len(parts) > 1 else "00"
            title_part = parts[2].replace("-", " ").title() if len(parts) > 2 else stem
            
            stories.append({
                "id": f"story.{cat}.{level.lower()}.{number}",
                "title": title_part,
                "level": level,
                "path": f"{cat}/{f.name}",
                "source": cat
            })
    return stories

def build_lessons():
    lessons = []
    levels = {
        "a1": {"name": "Fundamentals", "color": "#1B4B5A"},
        "a2": {"name": "Basic", "color": "#3E7986"},
        "b1": {"name": "Intermediate", "color": "#8FB4BA"},
        "b2": {"name": "Upper Intermediate", "color": "#2E2A26", "comingSoon": True},
        "c1": {"name": "Advanced", "color": "#E4572E", "comingSoon": True}
    }
    
    for level_id, meta in levels.items():
        level_path = BASE_LESSONS / level_id
        if not level_path.exists():
            continue
        
        level_lessons = []
        for f in sorted(level_path.glob("*.json")):
            try:
                with open(f, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                level_lessons.append({
                    "id": data.get("id", f"lesson.{level_id}.{f.stem}"),
                    "emoji": data.get("emoji", "📚"),
                    "title": data.get("title", f.stem),
                    "description": data.get("description", "")
                })
            except:
                pass
        
        if level_lessons or meta.get("comingSoon"):
            lessons.append({
                "id": level_id,
                "name": meta["name"],
                "subtitle": meta.get("subtitle", ""),
                "color": meta["color"],
                "comingSoon": meta.get("comingSoon", False),
                "lessons": level_lessons
            })
    
    return lessons

def main():
    # Build stories manifest
    stories = build_stories()
    with open(BASE_STORIES / "manifest.json", "w", encoding="utf-8") as f:
        json.dump({"stories": stories}, f, indent=2, ensure_ascii=False)
    print(f"Stories manifest: {len(stories)} stories")
    
    # Build lessons manifest
    lessons = build_lessons()
    with open(BASE_LESSONS / "manifest.json", "w", encoding="utf-8") as f:
        json.dump({"levels": lessons}, f, indent=2, ensure_ascii=False)
    print(f"Lessons manifest: {sum(len(l['lessons']) for l in lessons)} lessons")

if __name__ == "__main__":
    main()