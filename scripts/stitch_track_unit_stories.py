#!/usr/bin/env python3
"""
Stitch the 5 per-lesson world readings (01..05) of each added-track unit
into its single consolidated Library reading (stories/world/<level>/<stem>.json),
with the main title set to the unit's title from curriculum/units/<level>.json.

Applies to:
  - es-latam B1 (track: 'latam', 36 units)
  - es-latam B2 (tracks: 'latam' + 'regional', 36 units each)
  - hu       B1 (track: 'citizenship', 36 units)
  - es-es    B1 (track: 'cultura', 6 authored units so far)

Run with no arguments, it restitches every track above, which also rewrites
unit stories that were edited by hand (e.g. HU C1). To restitch one unit only:
  python scripts/stitch_track_unit_stories.py --unit es-latam b1 latam <unit id>
"""

import json
import re
import sys
from pathlib import Path


def stitch_language_track(lang: str, level: str, track_id: str, lang_audio_code: str, only_unit: str = None):
    level_lc = level.lower()
    units_path = Path(f"content/{lang}/curriculum/units/{level_lc}.json")
    lessons_dir = Path(f"content/{lang}/lessons/{level_lc}")
    world_dir = Path(f"content/{lang}/stories/world/{level_lc}")

    if not units_path.exists():
        print(f"{lang} {level} ({track_id}): no units file at {units_path}, skipping")
        return
    if not world_dir.exists():
        print(f"{lang} {level} ({track_id}): no world dir at {world_dir}, skipping")
        return

    units = json.loads(units_path.read_text(encoding="utf-8"))
    track_units = [u for u in units if u.get("track") == track_id]

    updated_count = 0
    for order_idx, unit in enumerate(track_units, start=1):
        if only_unit and unit.get("id") != only_unit:
            continue
        unit_title = unit["title"]
        stems = [s for s in unit.get("stems", []) if not s.endswith("-consolidation")]
        if not stems:
            continue

        # Collect the per-lesson story files via the lesson files' story sections
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

        # Find the corresponding combined story file in world_dir.
        # Derive slug from first stem: e.g. b1-independencia-01 -> b1-independencia
        #                              or b2-amazoniapan-01 -> b2-amazoniapan
        m = re.match(rf"^({level_lc}-[a-z0-9-]+)-\d{{2}}$", stems[0])
        if not m:
            print(f"  [WARN] Could not parse stem prefix from {stems[0]}")
            continue
        unit_prefix = m.group(1)
        combined_path = world_dir / f"{unit_prefix}.json"

        if not combined_path.exists():
            # Check hyphen-insensitive or prefix fallback (e.g. b1-represionpolitica vs
            # b1-represion-politica, or b1-eeuu vs b1-eeuu-latinoamerica, or c1-bioetika vs bioetika)
            norm_target = unit_prefix.replace("-", "")
            raw_target = unit_prefix[len(level_lc)+1:].replace("-", "") if unit_prefix.startswith(f"{level_lc}-") else norm_target
            candidates = [
                f for f in world_dir.glob("*.json")
                if not re.search(r"-\d{2}(-|$)|-consolidation", f.stem)
                and (f.stem.replace("-", "") in (norm_target, raw_target)
                     or f.stem.replace("-", "").startswith((norm_target, raw_target)))
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
        clean_slug = unit_prefix[len(level_lc)+1:] if unit_prefix.startswith(f"{level_lc}-") else unit_prefix
        combined["id"] = f"story.{level_lc}.{clean_slug}"
        if not combined.get("title"):
            combined["title"] = unit_title
        combined["level"] = level.upper()
        combined["type"] = "world"
        combined["order"] = order_idx
        combined["lesson"] = 5
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

    print(f"{lang} {level} ({track_id}): stitched {updated_count} consolidated unit stories")


def main():
    if sys.argv[1:2] == ["--unit"]:
        if len(sys.argv) != 6:
            sys.exit("usage: stitch_track_unit_stories.py --unit <lang> <level> <track> <unit id>")
        lang, level, track_id, unit_id = sys.argv[2:6]
        stitch_language_track(lang, level, track_id, lang.split("-")[0], only_unit=unit_id)
        return
    # B1 tracks
    stitch_language_track("es-latam", "b1", "latam", "es")
    stitch_language_track("hu", "b1", "citizenship", "hu")
    stitch_language_track("es-es", "b1", "cultura", "es")
    # B2 tracks
    stitch_language_track("es-latam", "b2", "latam", "es")
    stitch_language_track("es-latam", "b2", "regional", "es")
    # C1 tracks
    stitch_language_track("hu", "c1", "culture", "hu")


if __name__ == "__main__":
    main()
