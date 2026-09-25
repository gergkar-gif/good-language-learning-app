#!/usr/bin/env python3
"""
Build a skill -> exercise lookup for Workshop's Grammar Driller.

content/es/exercises/**/*.json holds every lesson's exercises inline, each
tagged with the grammar/vocabulary concepts it tests via `teaches` (see
content/es/schemas/exercises.schema.json). engine/recycle.js already walks
this pool at runtime for the Recycle block, scoped to one lesson's earlier
material at a time. The Grammar Driller instead wants every category:grammar
exercise across the whole course, grouped by skill, available up front — so
rather than re-walking every lesson file on every drill session, this script
does it once at build time.

Output: content/<lang>/indexes/grammar-index.json
    { "bySkill": { "<teaches slug>": [ { id, ref, type }, ... ] } }

`ref` is the path engine/content-loader.js's Content fetcher expects, relative
to content/<lang>/ (e.g. "exercises/a1/a1-02-02-ex.json") — the same shape
already used by a lesson's `sections[].ref`.

Usage:
    python scripts/build_grammar_index.py [lang ...]   (default: es hu)
"""
import json
import sys
from pathlib import Path
from collections import defaultdict


def build_index(exercises_dir):
    by_skill = defaultdict(list)
    stats = {"files": 0, "exercises": 0, "errors": 0}

    for f in sorted(exercises_dir.glob("*/*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            stats["errors"] += 1
            continue
        stats["files"] += 1

        ref = f.relative_to(exercises_dir.parent).as_posix()

        for ex in data.get("exercises", []):
            if ex.get("category") != "grammar":
                continue
            stats["exercises"] += 1
            entry = {"id": ex["id"], "ref": ref, "type": ex["type"]}
            for skill in ex.get("teaches", []):
                by_skill[skill].append(entry)

    return by_skill, stats


def resolve_titles(lang, by_skill):
    titles = {}

    # 1. Curated titles from content/<lang>/indexes/grammar-titles.json
    curated_path = Path(f"content/{lang}/indexes/grammar-titles.json")
    if curated_path.is_file():
        try:
            titles.update(json.loads(curated_path.read_text(encoding="utf-8")))
        except Exception:
            pass

    # 2. Bank module titles from content/<lang>/drills/grammar/a1-bank.json
    bank_path = Path(f"content/{lang}/drills/grammar/a1-bank.json")
    if bank_path.is_file():
        try:
            bank_data = json.loads(bank_path.read_text(encoding="utf-8"))
            for m in bank_data.get("modules", []):
                mid = m.get("id")
                mtitle = m.get("title")
                if mid and mtitle and mid not in titles:
                    titles[mid] = mtitle
        except Exception:
            pass

    # 3. Scan grammar files in content/<lang>/grammar/**/*.json
    grammar_dir = Path(f"content/{lang}/grammar")
    if grammar_dir.is_dir():
        grammar_slug_map = {}
        for gf in grammar_dir.rglob("*.json"):
            try:
                gd = json.loads(gf.read_text(encoding="utf-8"))
                gtitle = gd.get("title")
                if not gtitle:
                    continue
                stem = gf.stem.replace("-gr", "")
                grammar_slug_map[stem] = gtitle
            except Exception:
                continue

        for skill in by_skill:
            if skill in titles:
                continue
            for stem, gtitle in grammar_slug_map.items():
                if stem == skill or stem.endswith(f"-{skill}") or f"-{skill}-" in stem:
                    titles[skill] = gtitle
                    break

    # 4. Clean formatting fallback (never silent)
    fallback_skills = []
    minor_words = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor", "of", "on", "or", "so", "the", "to", "up", "vs", "yet", "with"}
    for skill in by_skill:
        if skill not in titles:
            fallback_skills.append(skill)
            text = (skill.replace("-isn-t", " isn't")
                         .replace("-aren-t", " aren't")
                         .replace("-don-t", " don't")
                         .replace("-doesn-t", " doesn't")
                         .replace("-won-t", " won't")
                         .replace("-can-t", " can't")
                         .replace("-s-", "'s ")
                         .replace("-s", "'s"))
            words = text.split("-")
            formatted = []
            for i, w in enumerate(words):
                w_lower = w.lower()
                if i > 0 and w_lower in minor_words:
                    formatted.append(w_lower)
                else:
                    formatted.append(w.capitalize())
            titles[skill] = " ".join(formatted)

    return titles, sorted(fallback_skills)


def main():
    args = [a for a in sys.argv[1:] if a != "--strict"]
    strict = "--strict" in sys.argv[1:]
    langs = args or sorted(p.name for p in Path("content").iterdir() if p.is_dir())  # every course folder, so a new language is indexed without editing this list
    any_failures = False

    for lang in langs:
        exercises_dir = Path(f"content/{lang}/exercises")
        if not exercises_dir.is_dir():
            print(f"[{lang}] no exercises dir, skipping")
            continue

        by_skill, stats = build_index(exercises_dir)
        titles, fallback_skills = resolve_titles(lang, by_skill)

        output_dir = Path(f"content/{lang}/indexes")
        output_file = output_dir / "grammar-index.json"
        output_dir.mkdir(parents=True, exist_ok=True)
        payload = json.dumps({"bySkill": by_skill, "titles": titles}, ensure_ascii=False, separators=(",", ":"))
        for _attempt in range(5):
            try:
                output_file.write_text(payload, encoding="utf-8")
                break
            except OSError:
                import time
                time.sleep(0.3 * (_attempt + 1))

        raw_size = output_file.stat().st_size

        print(f"[{lang}] Exercise files scanned: {stats['files']} (errors: {stats['errors']})")
        print(f"[{lang}] Grammar exercises:      {stats['exercises']}")
        print(f"[{lang}] Distinct skills:        {len(by_skill)}")
        print(f"[{lang}] Output:                 {output_file} ({raw_size:,} bytes)")

        if fallback_skills:
            print(f"[{lang}] WARNING: {len(fallback_skills)} skills fell through to slug->TitleCase fallback: "
                  + ", ".join(fallback_skills))
            any_failures = True

        # Learners see skill names mid-sentence ("You made a few mistakes
        # with ... lately."), so every skill should have a curated name.
        curated_path = Path(f"content/{lang}/indexes/grammar-titles.json")
        curated = json.loads(curated_path.read_text(encoding="utf-8")) if curated_path.is_file() else {}
        uncurated = sorted(s for s in by_skill if s not in curated)
        if uncurated:
            print(f"[{lang}] WARNING: {len(uncurated)} skills have no curated name in {curated_path}: "
                  + ", ".join(uncurated))
            any_failures = True

        # Skill-size sanity check: warn when a grammar skill has >150 exercises or >25 aliases
        reg_path = Path(f"content/{lang}/indexes/skill-registry.json")
        reg_skills = json.loads(reg_path.read_text(encoding="utf-8")).get("skills", {}) if reg_path.is_file() else {}
        oversized = []
        for s in sorted(by_skill):
            ex_cnt = len(by_skill[s])
            al_cnt = len(reg_skills.get(s, {}).get("aliases") or [])
            if ex_cnt > 150 or al_cnt > 25:
                oversized.append(f"{s} ({ex_cnt} exercises, {al_cnt} aliases)")
        if oversized:
            print(f"[{lang}] SIZE WARNING: {len(oversized)} grammar skills exceed 150 exercises or 25 aliases: "
                  + ", ".join(oversized))

    if strict and any_failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
