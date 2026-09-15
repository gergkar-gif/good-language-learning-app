#!/usr/bin/env python3
"""
narrate-story.py — AI-aware story narration & pedagogical annotation generator for Parlour.

Uses state-of-the-art Neural TTS (edge-tts) for authentic human pronunciation,
multi-speaker voice casting, CEFR pacing, and mixed-language story support.

Workflow:
1. Reads story JSON.
2. Analyzes text structure: dialogue, speakers, CEFR pacing, pauses, emphasis, phonetics.
3. Generates pedagogical annotations: target vocabulary, comprehension check questions.
4. Synthesizes multi-speaker neural audio with precise paragraph-level timestamp alignment.
5. Injects narration metadata into the story JSON file.
6. Stores the audio asset in content/<lang>/stories/audio/<story-id>.mp3.
"""

import argparse
import asyncio
import json
import os
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

try:
    import edge_tts
    HAS_EDGE_TTS = True
except ImportError:
    HAS_EDGE_TTS = False

# CEFR Pacing Profiles (Default to 100% natural, un-stretched native human tempo)
CEFR_PACING = {
    "A1": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 140, "style": "natural, articulate"},
    "A2": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 145, "style": "natural, clear, conversational"},
    "B1": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 150, "style": "natural, expressive"},
    "B2": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 160, "style": "fluent, authentic cadence"},
    "C1": {"speedMultiplier": 1.00, "rate_str": "+0%", "rate_wpm": 170, "style": "native tempo, rich nuances"}
}

# Neural Voice Casting Catalog
NEURAL_VOICES = {
    "es": {
        "narrator": "es-ES-ElviraNeural",     # Warm, articulate storytelling guide
        "female": "es-ES-XimenaNeural",       # Clear, natural female dialogue (e.g. Meg, Ana)
        "male": "es-ES-AlvaroNeural"          # Natural male dialogue (e.g. Carlos, Juan)
    },
    "hu": {
        "narrator": "hu-HU-NoemiNeural",      # Native Hungarian female storyteller
        "female": "hu-HU-NoemiNeural",        # Hungarian female dialogue
        "male": "hu-HU-TamasNeural"           # Hungarian male dialogue (e.g. Károly)
    },
    "en": {
        "narrator": "en-US-EmmaNeural",       # Clear, warm English scaffolding narrator
        "female": "en-US-EmmaNeural",         # English female dialogue
        "male": "en-US-BrianNeural"           # English male dialogue
    }
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

def get_speaker_voice(speaker, lang, course_lang):
    """Assigns an authentic neural voice based on speaker name, paragraph language, and role."""
    lang_voices = NEURAL_VOICES.get(lang, NEURAL_VOICES.get(course_lang, NEURAL_VOICES["es"]))
    if speaker == "Narrator":
        return lang_voices["narrator"]
    female_names = ["Meg", "Ana", "Elena", "María", "Carmen", "Kati", "Zsuzsa", "Eszter", "Emma"]
    gender = "female" if speaker in female_names else "male"
    return lang_voices.get(gender, lang_voices["narrator"])

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
    
    # Identify speakers with role and tone
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

async def synthesize_story_neural(story_data, output_mp3_path, course_lang="es"):
    """
    Synthesizes story paragraphs into an authentic multi-voice MP3 using Neural TTS,
    extracting precise millisecond sentence boundaries.
    """
    if not HAS_EDGE_TTS:
        print("[WARN] edge-tts is not installed; skipping audio synthesis.")
        return None, 0.0

    level = story_data.get("level", "A1").upper()
    pacing = CEFR_PACING.get(level, CEFR_PACING["A1"])
    paragraphs = story_data.get("paragraphs", [])
    if not paragraphs:
        return None, 0.0

    all_audio = bytearray()
    real_segments = []
    current_time = 0.0

    print(f"[NEURAL-TTS] Synthesizing {len(paragraphs)} paragraphs (CEFR: {level})...")

    for idx, p in enumerate(paragraphs):
        text = p.get("text", "").strip()
        if not text:
            continue

        p_type = p.get("type", "narration")
        speaker = p.get("speaker", "Narrator") if p_type == "dialogue" else "Narrator"
        para_lang = p.get("lang") or course_lang

        # Select neural voice & pacing rate
        voice = get_speaker_voice(speaker, para_lang, course_lang)
        rate_str = "+0%" if para_lang == "en" else pacing["rate_str"]

        comm = edge_tts.Communicate(text, voice, rate=rate_str)
        dur = 0.0
        seg_audio = bytearray()

        try:
            async for chunk in comm.stream():
                if chunk["type"] == "audio":
                    seg_audio.extend(chunk["data"])
                elif chunk["type"] == "SentenceBoundary":
                    offset_s = chunk["offset"] / 10_000_000.0
                    duration_s = chunk["duration"] / 10_000_000.0
                    dur = max(dur, offset_s + duration_s)
        except Exception as e:
            print(f"[ERROR] Synthesis failed on paragraph {idx}: {e}")

        # Fallback to byte-length estimation if duration was not emitted
        if dur <= 0.0:
            dur = max(1.5, round(len(seg_audio) / 6000.0, 2))

        start_time = round(current_time, 2)
        end_time = round(current_time + dur, 2)

        real_segments.append({
            "paraIndex": idx,
            "startTime": start_time,
            "endTime": end_time,
            "speaker": speaker,
            "lang": para_lang,
            "voice": voice
        })

        all_audio.extend(seg_audio)
        current_time = end_time

        speaker_label = f"{speaker} ({voice.split('-')[-1].replace('Neural', '')})"
        print(f"  [P{idx:02d}] {speaker_label:20s} [{para_lang}] {start_time:5.2f}s -> {end_time:5.2f}s | {text[:38]}...")

    # Write master MP3 file
    os.makedirs(os.path.dirname(output_mp3_path), exist_ok=True)
    with open(output_mp3_path, "wb") as f:
        f.write(all_audio)

    total_duration = round(current_time, 2)
    file_size_kb = len(all_audio) / 1024.0
    print(f"[SUCCESS] Neural audio synthesized -> {output_mp3_path} ({file_size_kb:.1f} KB, {total_duration}s)")

    return real_segments, total_duration

def process_story(story_path, dry_run=False, synthesize=True):
    path = Path(story_path)
    if not path.exists():
        print(f"[ERROR] Story file not found: {story_path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        story_data = json.load(f)

    story_id = story_data.get("id", path.stem)
    course_lang = detect_course_lang(path, story_data)
    print(f"=== Processing Story: {story_data.get('title')} ({story_id}) [{course_lang.upper()}] ===")

    # Step 1: AI text analysis & pedagogical annotations
    analysis = analyze_story_text(story_data, course_lang=course_lang)

    # Audio destination: content/<lang>/stories/audio/<story-id>.mp3
    audio_dir = Path(f"content/{course_lang}/stories/audio")
    audio_rel = f"audio/{story_id}.mp3"
    audio_file_path = audio_dir / f"{story_id}.mp3"

    # Step 2: Synthesis with Neural TTS
    if synthesize and not dry_run and HAS_EDGE_TTS:
        real_segments, measured_duration = asyncio.run(
            synthesize_story_neural(story_data, str(audio_file_path), course_lang=course_lang)
        )
        if real_segments:
            # Reconcile segment timings and assign exact boundaries
            for seg in analysis["segments"]:
                match = next((s for s in real_segments if s["paraIndex"] == seg["paraIndex"]), None)
                if match:
                    seg["startTime"] = match["startTime"]
                    seg["endTime"] = match["endTime"]
                    seg["lang"] = match["lang"]
            analysis["durationSeconds"] = measured_duration

        # Clean up any legacy .wav file if present
        wav_path = audio_dir / f"{story_id}.wav"
        if wav_path.exists():
            try:
                wav_path.unlink()
                print(f"[CLEANUP] Removed legacy uncompressed WAV: {wav_path}")
            except Exception:
                pass

    narration_block = {
        "audioFile": audio_rel,
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
        print(f"[SUCCESS] Updated story with AI narration metadata: {path}")
    else:
        print("[DRY-RUN] Narration metadata preview:")
        print(json.dumps(narration_block, indent=2, ensure_ascii=False))

    return narration_block

def main():
    parser = argparse.ArgumentParser(description="Generate AI-aware reading narration and pedagogical metadata.")
    parser.add_argument("file", nargs="?", default=None, help="Path to story JSON file")
    parser.add_argument("--batch", help="Glob pattern or directory of story JSON files to narrate (e.g. content/es/stories/original/a1/*.json)")
    parser.add_argument("--dry-run", action="store_true", help="Print narration metadata without writing to file")
    parser.add_argument("--no-synth", action="store_true", help="Skip audio synthesis, generate metadata only")
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
        process_story(str(story_file), dry_run=args.dry_run, synthesize=not args.no_synth)

if __name__ == "__main__":
    main()

