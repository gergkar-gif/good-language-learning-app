#!/usr/bin/env python3
"""
narrate-story.py — AI-aware story narration & pedagogical annotation generator for Parlour.

Metadata only, no audio synthesis: actual playback goes through ParlourTTS
(engine/tts.js -> cloudflare-worker/tts-worker.js -> Google Cloud TTS) live in
the app, not a pre-generated file, so this script never produces one — no
Neural TTS dependency, nothing written to content/<lang>/stories/audio/.

Workflow:
1. Reads story JSON.
2. Analyzes text structure: dialogue, speakers, CEFR pacing, pauses, emphasis, phonetics.
3. Generates pedagogical annotations: target vocabulary, comprehension check questions.
4. Estimates paragraph-level timing from word count and CEFR pacing (not measured audio).
5. Injects narration metadata into the story JSON file.
"""

import argparse
import json
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# CEFR Pacing Profiles (Default to 100% natural, un-stretched native human tempo)
CEFR_PACING = {
    "A1": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 140, "style": "natural, articulate"},
    "A2": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 145, "style": "natural, clear, conversational"},
    "B1": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 150, "style": "natural, expressive"},
    "B2": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 160, "style": "fluent, authentic cadence"},
    "C1": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 170, "style": "native tempo, rich nuances"}
}

KNOWN_PHONETICS = {
    # Spanish
    "Hanói": {"ipa": "xaˈnoj", "note": "Stress on the final syllable"},
    "Sudáfrica": {"ipa": "suˈða.fɾi.ka", "note": "Antepenultimate accent on -dá-"},
    "Hungría": {"ipa": "uŋˈɡɾi.a", "note": "Silent initial H, hiatus on -í-"},
    "español": {"ipa": "es.paˈɲol", "note": "Palatal nasal ñ"},
    "Buenos días": {"ipa": "ˈbwe.noz ˈði.as", "note": "Soft intervocalic d"},
    # Hungarian
    "Budapest": {"ipa": "ˈbudɒpɛʃt", "note": "s is pronounced 'sh' (/ʃ/), a is short open back vowel (/ɒ/)"},
    "Károly": {"ipa": "ˈkaːroj", "note": "Stress strictly on first syllable, ly pronounced /j/"},
    "Szia": {"ipa": "ˈsiɒ", "note": "Informal greeting ('hi/hello')"},
    "könyv": {"ipa": "ˈkøɲv", "note": "ö is front rounded /ø/, ny is palatal /ɲ/"},
    "kávé": {"ipa": "ˈkaːveː", "note": "Long á and long é vowels"},
    "víz": {"ipa": "ˈviːz", "note": "Long vowel í"},
    "ház": {"ipa": "ˈhaːz", "note": "Long vowel á"}
}

def detect_course_lang(story_path, story_data):
    """Detects primary course language from path or story data."""
    p_str = str(story_path).replace("\\", "/")
    if "/hu/" in p_str:
        return "hu"
    if "/es/" in p_str:
        return "es"
    return "es"

def analyze_story_text(story_data, course_lang="es"):
    """
    Analyzes story text to derive:
    - Speaker profiles
    - Pacing and timing cues
    - Segment language tags
    - Pronunciation notes
    - Pedagogical vocabulary & comprehension questions
    """
    level = story_data.get("level", "A1").upper()
    pacing = CEFR_PACING.get(level, CEFR_PACING["A1"])
    paragraphs = story_data.get("paragraphs", [])
    characters = story_data.get("characters", [])

    # Identify speakers with role and tone. Gender is guessed from a fixed
    # name list — reader.js's ParlourTTS voice assignment reads this field,
    # so a character name outside this list gets miscategorised as male;
    # authoring a real per-character gender in the story JSON instead would
    # fix that, but isn't done here.
    speakers = {
        "Narrator": {
            "role": "narrator",
            "gender": "neutral",
            "tone": "clear, warm, steady storytelling guide"
        }
    }
    for char in characters:
        is_female = char in ["Meg", "Ana", "Elena", "María", "Carmen", "Kati", "Zsuzsa", "Eszter", "Emma"]
        speakers[char] = {
            "role": "character",
            "gender": "female" if is_female else "male",
            "tone": "conversational, expressive"
        }

    segments = []
    current_time = 0.0

    for idx, p in enumerate(paragraphs):
        text = p.get("text", "")
        p_type = p.get("type", "narration")
        speaker = p.get("speaker", "Narrator") if p_type == "dialogue" else "Narrator"
        para_lang = p.get("lang") or course_lang

        # Word count & estimated speaking time
        words = text.split()
        word_count = len(words)
        # English scaffolding paragraphs use natural ~145 wpm
        wpm = 145 if para_lang == "en" else pacing["rate_wpm"]
        duration = max(1.6, round((word_count / wpm) * 60.0, 2))

        cues = []
        if "?" in text or "¿" in text:
            cues.append({"type": "intonation", "contour": "rising-interrogative"})
        if "!" in text or "¡" in text:
            cues.append({"type": "emphasis", "level": "strong"})
        if "," in text:
            cues.append({"type": "pause", "durationMs": 250, "reason": "clause-boundary"})

        pron_list = []
        for word, info in KNOWN_PHONETICS.items():
            if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
                pron_list.append({"word": word, "ipa": info["ipa"], "note": info["note"]})

        segments.append({
            "paraIndex": idx,
            "startTime": round(current_time, 2),
            "endTime": round(current_time + duration, 2),
            "speaker": speaker,
            "lang": para_lang,
            "cues": cues,
            "pronunciations": pron_list
        })
        current_time += duration

    total_duration = round(current_time, 2)

    # Key vocabulary & comprehension questions
    grammar_topics = story_data.get("grammar", [])
    title = story_data.get("title", "")
    summary = story_data.get("summary", "")

    if course_lang == "hu":
        key_vocab = [
            {"lemma": "könyv", "pos": "noun", "cefr": "A1", "gloss": "book"},
            {"lemma": "telefon", "pos": "noun", "cefr": "A1", "gloss": "telephone"},
            {"lemma": "ház", "pos": "noun", "cefr": "A1", "gloss": "house"}
        ]
        comprehension_questions = [
            {
                "question": "Hol van Meg és Károly?",
                "options": [
                    "Budapesten",
                    "Londonban",
                    "Bécsben",
                    "Madridban"
                ],
                "correctIndex": 0,
                "explanation": "Meg Budapesten van Károllyal (Meg is in Budapest with Károly)."
            },
            {
                "question": "Mi van az asztalon?",
                "options": [
                    "Egy könyv és egy telefon",
                    "Egy autó és egy kulcs",
                    "Egy kutya és egy macska",
                    "Csak egy pohár tej"
                ],
                "correctIndex": 0,
                "explanation": "Károly rámutat egy könyvre és egy telefonra az asztalon (Ez egy könyv, az egy telefon)."
            },
            {
                "question": "Milyen nyelven beszélnek a párbeszédekben?",
                "options": [
                    "Magyarul",
                    "Spanyolul",
                    "Németül",
                    "Olaszul"
                ],
                "correctIndex": 0,
                "explanation": "Meg magyarul gyakorolja az alapvető szavakat Károllyal."
            }
        ]
    elif "Meg" in characters and "Carlos" in characters:
        key_vocab = [
            {"lemma": "conocer", "pos": "verb", "cefr": level, "gloss": "to meet / get to know"},
            {"lemma": "intercambio", "pos": "noun", "cefr": level, "gloss": "exchange"}
        ]
        comprehension_questions = [
            {
                "question": "¿Dónde se encuentran Carlos y Meg?",
                "options": [
                    "En un restaurante mexicano",
                    "En la universidad de Hanói",
                    "En una estación de tren",
                    "En una fiesta en Madrid"
                ],
                "correctIndex": 0,
                "explanation": "Carlos va a un restaurante mexicano por la mañana para practicar español."
            },
            {
                "question": "¿De dónde es Meg?",
                "options": [
                    "De Hungría",
                    "De Sudáfrica",
                    "De España",
                    "De México"
                ],
                "correctIndex": 1,
                "explanation": "Meg responde explícitamente: 'Soy de Sudáfrica'."
            },
            {
                "question": "¿Por qué están allí los dos?",
                "options": [
                    "Para practicar español en un intercambio de idiomas",
                    "Para comer tacos únicamente",
                    "Para trabajar como camareros",
                    "Para viajar a Hungría"
                ],
                "correctIndex": 0,
                "explanation": "Los dos estudian el idioma y asisten al intercambio de idiomas."
            }
        ]
    else:
        key_vocab = [
            {"lemma": "historia", "pos": "noun", "cefr": level, "gloss": "story"}
        ]
        comprehension_questions = [
            {
                "question": f"¿Cuál es el tema principal de «{title}»?",
                "options": [
                    summary if summary else f"Una lectura en nivel {level}",
                    "Una discusión sobre gramática",
                    "Una receta de cocina tradicional",
                    "Una carta formal de negocios"
                ],
                "correctIndex": 0,
                "explanation": "El texto desarrolla los eventos descritos en la narración."
            }
        ]

    pedagogical = {
        "keyVocabulary": key_vocab,
        "targetGrammar": grammar_topics,
        "comprehensionQuestions": comprehension_questions
    }

    return {
        "pacing": pacing,
        "speakers": speakers,
        "segments": segments,
        "durationSeconds": total_duration,
        "pedagogical": pedagogical
    }

def process_story(story_path, dry_run=False):
    path = Path(story_path)
    if not path.exists():
        print(f"[ERROR] Story file not found: {story_path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        story_data = json.load(f)

    story_id = story_data.get("id", path.stem)
    course_lang = detect_course_lang(path, story_data)
    print(f"=== Processing Story: {story_data.get('title')} ({story_id}) [{course_lang.upper()}] ===")

    analysis = analyze_story_text(story_data, course_lang=course_lang)

    narration_block = {
        "durationSeconds": analysis["durationSeconds"],
        "pacing": analysis["pacing"],
        "speakers": analysis["speakers"],
        "segments": analysis["segments"],
        "pedagogical": analysis["pedagogical"]
    }

    story_data["narration"] = narration_block

    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(story_data, f, ensure_ascii=False, indent=2)
        print(f"[SUCCESS] Updated story with narration metadata: {path}")
    else:
        print("[DRY-RUN] Narration metadata preview:")
        print(json.dumps(narration_block, indent=2, ensure_ascii=False))

    return narration_block

def main():
    parser = argparse.ArgumentParser(description="Generate story narration timing and pedagogical metadata.")
    parser.add_argument("file", nargs="?", default=None, help="Path to story JSON file")
    parser.add_argument("--batch", help="Glob pattern or directory of story JSON files to narrate (e.g. content/es/stories/original/a1/*.json)")
    parser.add_argument("--dry-run", action="store_true", help="Print narration metadata without writing to file")
    args = parser.parse_args()

    files = []
    if args.batch:
        p = Path(args.batch)
        if p.is_dir():
            files = sorted(list(p.rglob("*.json")))
        else:
            files = sorted([Path(f) for f in Path(".").glob(args.batch)])
    elif args.file:
        files = [Path(args.file)]
    else:
        parser.print_help()
        sys.exit(1)

    print(f"Narrating {len(files)} story file(s)...")
    for story_file in files:
        process_story(str(story_file), dry_run=args.dry_run)

if __name__ == "__main__":
    main()
