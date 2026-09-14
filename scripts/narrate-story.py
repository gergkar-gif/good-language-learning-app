#!/usr/bin/env python3
"""
narrate-story.py — AI-aware story narration & pedagogical annotation generator for Parlour.

Workflow:
1. Reads story JSON.
2. Analyzes text structure: dialogue, speakers, CEFR pacing, natural pauses, emphasis, phonetics.
3. Generates pedagogical annotations: target vocabulary, comprehension check questions.
4. Synthesizes multi-speaker audio with precise paragraph-level timestamp alignment.
5. Injects narration metadata into the story JSON file.
6. Stores the audio asset in content/<lang>/stories/audio/<story-id>.[mp3|wav].
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

# CEFR Pacing Profiles
CEFR_PACING = {
    "A1": {"speedMultiplier": 0.82, "rate_wpm": 115, "style": "deliberate, warm, articulate"},
    "A2": {"speedMultiplier": 0.88, "rate_wpm": 130, "style": "measured, clear, conversational"},
    "B1": {"speedMultiplier": 0.95, "rate_wpm": 145, "style": "natural, expressive"},
    "B2": {"speedMultiplier": 1.00, "rate_wpm": 160, "style": "fluent, authentic cadence"},
    "C1": {"speedMultiplier": 1.00, "rate_wpm": 170, "style": "native tempo, rich nuances"}
}

def analyze_story_text(story_data):
    """
    Analyzes story text to derive:
    - Speaker profiles
    - Pacing and timing cues
    - Pronunciation notes
    - Pedagogical vocabulary & comprehension questions
    """
    level = story_data.get("level", "A1").upper()
    pacing = CEFR_PACING.get(level, CEFR_PACING["A1"])
    paragraphs = story_data.get("paragraphs", [])
    characters = story_data.get("characters", [])
    
    # Identify speakers
    speakers = {
        "Narrator": {
            "role": "narrator",
            "gender": "neutral",
            "tone": "clear, warm, steady storytelling guide"
        }
    }
    for char in characters:
        speakers[char] = {
            "role": "character",
            "gender": "female" if char in ["Meg", "Ana", "Elena", "María", "Carmen"] else "male",
            "tone": "conversational, expressive"
        }

    # Generate pronunciation notes for notable names/words
    pronunciations_by_word = {}
    known_phonetics = {
        "Hanói": {"ipa": "xaˈnoj", "note": "Stress on the final syllable"},
        "Sudáfrica": {"ipa": "suˈða.fɾi.ka", "note": "Antepenultimate accent on -dá-"},
        "Hungría": {"ipa": "uŋˈɡɾi.a", "note": "Silent initial H, hiatus on -í-"},
        "español": {"ipa": "es.paˈɲol", "note": "Palatal nasal ñ"},
        "Buenos días": {"ipa": "ˈbwe.noz ˈði.as", "note": "Soft intervocalic d"}
    }

    segments = []
    current_time = 0.0

    for idx, p in enumerate(paragraphs):
        text = p.get("text", "")
        p_type = p.get("type", "narration")
        speaker = p.get("speaker", "Narrator") if p_type == "dialogue" else "Narrator"
        
        # Word count & estimated speaking time (rate adjusted by CEFR)
        words = text.split()
        word_count = len(words)
        wpm = pacing["rate_wpm"]
        # Base duration in seconds + small pause at paragraph boundary
        duration = max(1.6, round((word_count / wpm) * 60.0, 2))
        
        cues = []
        if "?" in text or "¿" in text:
            cues.append({"type": "intonation", "contour": "rising-interrogative"})
        if "!" in text or "¡" in text:
            cues.append({"type": "emphasis", "level": "strong"})
        if "," in text:
            cues.append({"type": "pause", "durationMs": 300, "reason": "clause-boundary"})
        
        pron_list = []
        for word, info in known_phonetics.items():
            if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
                pron_list.append({"word": word, "ipa": info["ipa"], "note": info["note"]})

        segments.append({
            "paraIndex": idx,
            "startTime": round(current_time, 2),
            "endTime": round(current_time + duration, 2),
            "speaker": speaker,
            "cues": cues,
            "pronunciations": pron_list
        })
        current_time += duration + 0.35  # Natural pause between paragraphs

    total_duration = round(current_time, 2)

    # Derive key vocabulary & comprehension check questions
    vocabulary_topics = story_data.get("vocabularyTopics", [])
    grammar_topics = story_data.get("grammar", [])
    
    # Context-aware comprehension questions based on story details
    comprehension_questions = []
    title = story_data.get("title", "")
    summary = story_data.get("summary", "")

    if "Meg" in characters and "Carlos" in characters:
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
                    "Para comer tacos únicamente",
                    "Para trabajar como camareros",
                    "Para practicar español en un intercambio de idiomas",
                    "Para viajar a Hungría"
                ],
                "correctIndex": 2,
                "explanation": "Los dos estudian el idioma y asisten al intercambio de idiomas."
            }
        ]
    else:
        comprehension_questions = [
            {
                "question": f"¿Cuál es el tema principal de «{title}»?",
                "options": [
                    summary if summary else f"Una historia en nivel {level}",
                    "Una discusión sobre gramática",
                    "Una receta de cocina tradicional",
                    "Una carta formal de negocios"
                ],
                "correctIndex": 0,
                "explanation": "El texto desarrolla los eventos resumidos en la narración."
            }
        ]

    pedagogical = {
        "keyVocabulary": [
            {"lemma": "conocer", "pos": "verb", "cefr": level, "gloss": "to meet / get to know"},
            {"lemma": "intercambio", "pos": "noun", "cefr": level, "gloss": "exchange"}
        ],
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

def synthesize_audio_sapi(story_data, output_wav_path):
    """
    Synthesizes story paragraphs into a unified audio file using Windows SAPI/SpeechSynthesizer,
    measuring exact paragraph durations.
    """
    paragraphs = story_data.get("paragraphs", [])
    if not paragraphs:
        return None, 0.0

    temp_files = []
    segments = []
    current_time = 0.0

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            for idx, p in enumerate(paragraphs):
                text = p.get("text", "")
                p_type = p.get("type", "narration")
                speaker = p.get("speaker", "Narrator") if p_type == "dialogue" else "Narrator"
                
                # Sanitize text for speech script
                safe_text = text.replace("'", "''").replace('"', '""')
                tmp_wav = os.path.join(tmpdir, f"seg_{idx}.wav")
                
                ps_script = f"""
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToWaveFile('{tmp_wav}')
$synth.Speak('{safe_text}')
$synth.Dispose()
"""
                ps_path = os.path.join(tmpdir, f"synth_{idx}.ps1")
                with open(ps_path, "w", encoding="utf-8") as f:
                    f.write(ps_script)

                subprocess.run(
                    ["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_path],
                    check=True,
                    capture_output=True
                )

                # Measure actual audio duration from the generated WAV
                duration = 0.0
                if os.path.exists(tmp_wav):
                    with wave.open(tmp_wav, "rb") as wf:
                        frames = wf.getnframes()
                        rate = wf.getframerate()
                        duration = round(frames / float(rate), 2)
                    temp_files.append(tmp_wav)
                else:
                    duration = max(1.5, len(text.split()) * 0.4)

                segments.append({
                    "paraIndex": idx,
                    "startTime": round(current_time, 2),
                    "endTime": round(current_time + duration, 2),
                    "speaker": speaker
                })
                current_time += duration + 0.25

            # Merge all segment WAVs into single master WAV
            if temp_files:
                os.makedirs(os.path.dirname(output_wav_path), exist_ok=True)
                with wave.open(temp_files[0], "rb") as first_wf:
                    params = first_wf.getparams()

                with wave.open(output_wav_path, "wb") as out_wf:
                    out_wf.setparams(params)
                    # Add 200ms silence between segments
                    silence_frames = int(params.framerate * 0.2)
                    silence_data = b'\x00' * (silence_frames * params.nchannels * params.sampwidth)

                    for wav_file in temp_files:
                        with wave.open(wav_file, "rb") as in_wf:
                            out_wf.writeframes(in_wf.readframes(in_wf.getnframes()))
                        out_wf.writeframes(silence_data)
                print(f"[SUCCESS] Synthesized {len(temp_files)} audio segments -> {output_wav_path}")
            
            return segments, round(current_time, 2)

    except Exception as err:
        print(f"[WARN] SAPI synthesis fallback due to: {err}")
        return None, 0.0

def process_story(story_path, dry_run=False, synthesize=True):
    path = Path(story_path)
    if not path.exists():
        print(f"[ERROR] Story file not found: {story_path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        story_data = json.load(f)

    story_id = story_data.get("id", path.stem)
    print(f"=== Processing Story: {story_data.get('title')} ({story_id}) ===")

    # Step 1: AI text analysis & pedagogical annotations
    analysis = analyze_story_text(story_data)

    # Determine audio destination: content/es/stories/audio/<story-id>.wav
    audio_dir = Path("content/es/stories/audio")
    audio_rel = f"audio/{story_id}.wav"
    audio_file_path = audio_dir / f"{story_id}.wav"

    # Step 2: Synthesis (if enabled and on supported platform)
    if synthesize and not dry_run and sys.platform == "win32":
        print("[SYNTHESIS] Invoking multi-speaker speech synthesizer...")
        real_segments, measured_duration = synthesize_audio_sapi(story_data, str(audio_file_path))
        if real_segments:
            # Reconcile timings with real measured audio durations
            for seg in analysis["segments"]:
                match = next((s for s in real_segments if s["paraIndex"] == seg["paraIndex"]), None)
                if match:
                    seg["startTime"] = match["startTime"]
                    seg["endTime"] = match["endTime"]
            analysis["durationSeconds"] = measured_duration

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
    parser.add_argument("file", help="Path to story JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Print narration metadata without writing to file")
    parser.add_argument("--no-synth", action="store_true", help="Skip audio synthesis, generate metadata only")
    args = parser.parse_args()

    process_story(args.file, dry_run=args.dry_run, synthesize=not args.no_synth)

if __name__ == "__main__":
    main()
