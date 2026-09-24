#!/usr/bin/env python3
"""
Stitch the 5 per-lesson world readings (01..05) of each B1 added-track unit
into its single consolidated Library reading (stories/world/b1/b1-<slug>.json),
with the main title set to the unit's title from curriculum/units/b1.json.

Applies to:
  - es-latam (track: 'latam', 36 units)
  - hu       (track: 'citizenship', 36 units)
  - es-es    (track: 'cultura', 6 authored units so far)
"""

import json
import re
from pathlib import Path


def stitch_language_track(lang: str, track_id: str, lang_audio_code: str):
    units_path = Path(f"content/{lang}/curriculum/units/b1.json")
    lessons_dir = Path(f"content/{lang}/lessons/b1")
    world_dir = Path(f"content/{lang}/stories/world/b1")

    units = json.loads(units_path.read_text(encoding="utf-8"))
    track_units = [u for u in units if u.get("track") == track_id]

    updated_count = 0
    for order_idx, unit in enumerate(track_units, start=1):
        unit_title = unit["title"]
        stems = [s for s in unit.get("stems", []) if not s.endswith("-consolidation")]
        if not stems:
            continue

        # Collect the 5 lesson story files via the lesson files' story sections
        segment_files = []
        for stem in stems:
            lesson_file = lessons_dir / f"{stem}.json"
            if not lesson_file.exists():
                continue
            ldata = json.loads(lesson_file.read_text(encoding="utf-8"))
            for sec in ldata.get("sections", []):
                if sec.get("type") == "story" and sec.get("ref"):
                    ref_path = Path(f"content/{lang}") / sec["ref"]
                    if ref_path.exists():
                        segment_files.append(ref_path)

        if not segment_files:
            # Skip unauthored stub units (e.g. es-es units 7..36)
            continue

        # Find the corresponding combined story file in world_dir
        # Derive slug from first stem: e.g. b1-independencia-01 -> b1-independencia
        m = re.match(r"^(b1-[a-z0-9-]+)-\d{2}$", stems[0])
        if not m:
            print(f"  [WARN] Could not parse stem prefix from {stems[0]}")
            continue
        unit_prefix = m.group(1)
        combined_path = world_dir / f"{unit_prefix}.json"

        if not combined_path.exists():
            # Check hyphen-insensitive or prefix fallback (e.g. b1-represionpolitica vs b1-represion-politica,
            # or b1-eeuu vs b1-eeuu-latinoamerica, matching build-manifest.py's _apply_story_unit_families)
            norm_target = unit_prefix.replace("-", "")
            candidates = [
                f for f in world_dir.glob("b1-*.json")
                if not re.search(r"-\d{2}(-|$)", f.stem)
                and (f.stem.replace("-", "") == norm_target or f.stem.replace("-", "").startswith(norm_target))
            ]
            if candidates:
                combined_path = candidates[0]
            else:
                print(f"  [WARN] Missing combined file for {unit_prefix} in {lang}")
                continue

        combined = json.loads(combined_path.read_text(encoding="utf-8"))

        all_paras = []
        all_qs = []
        all_vocab = []
        seen_lemmas = set()
        all_grammar = []
        all_topics = []

        for sf in segment_files:
            sdata = json.loads(sf.read_text(encoding="utf-8"))
            all_paras.extend(sdata.get("paragraphs", []))

            for g in sdata.get("grammar", []):
                if g not in all_grammar:
                    all_grammar.append(g)
            for vt in sdata.get("vocabularyTopics", []):
                if vt not in all_topics:
                    all_topics.append(vt)

            ped = (sdata.get("narration") or {}).get("pedagogical") or {}
            for q in ped.get("comprehensionQuestions", []):
                all_qs.append(q)
            for kv in ped.get("keyVocabulary", []):
                lemma = kv.get("lemma")
                if lemma and lemma not in seen_lemmas:
                    seen_lemmas.add(lemma)
                    all_vocab.append(kv)

        # Build continuous narration segments for all stitched paragraphs
        segments = []
        t = 0.0
        for idx, p in enumerate(all_paras):
            words = len((p.get("text") or "").split())
            dur = round(max(4.5, words / 2.4), 1)
            segments.append({
                "paraIndex": idx,
                "startTime": round(t, 1),
                "endTime": round(t + dur, 1),
                "speaker": p.get("speaker") or "Narrator",
                "lang": lang_audio_code,
                "cues": [{"type": "pause", "durationMs": 250, "reason": "clause-boundary"}] if idx > 0 else [],
                "pronunciations": []
            })
            t += dur

        total_words = sum(len((p.get("text") or "").split()) for p in all_paras)
        est_minutes = max(8, round(total_words / 110))

        combined["title"] = unit_title
        combined["level"] = "B1"
        combined["type"] = "world"
        combined["order"] = order_idx
        combined["estimatedMinutes"] = est_minutes
        if all_grammar:
            combined["grammar"] = all_grammar
        if all_topics:
            combined["vocabularyTopics"] = all_topics
        combined["paragraphs"] = all_paras

        narration = combined.get("narration") or {}
        narration["durationSeconds"] = round(t, 1)
        narration.setdefault("pacing", {
            "speedMultiplier": 1.0,
            "rate_str": "+0%",
            "rate_wpm": 145,
            "style": "natural, expressive"
        })
        narration.setdefault("speakers", {
            "Narrator": {
                "role": "narrator",
                "gender": "neutral",
                "tone": "clear, warm, steady storytelling guide"
            }
        })
        narration["segments"] = segments

        ped = narration.get("pedagogical") or {}
        if all_vocab:
            ped["keyVocabulary"] = all_vocab[:15]
        elif not ped.get("keyVocabulary"):
            ped["keyVocabulary"] = []
        if all_qs:
            ped["comprehensionQuestions"] = all_qs
        narration["pedagogical"] = ped
        combined["narration"] = narration

        combined_path.write_text(
            json.dumps(combined, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8"
        )
        updated_count += 1

    print(f"{lang} ({track_id}): stitched {updated_count} consolidated unit stories")


def main():
    stitch_language_track("es-latam", "latam", "es")
    stitch_language_track("hu", "citizenship", "hu")
    stitch_language_track("es-es", "cultura", "es")


if __name__ == "__main__":
    main()
