#!/usr/bin/env python3
"""
Export vocabulary words lacking example sentences in translation-index.json.
Generates prompt-ready text files grouped by CEFR level for LLM backfill.

Usage:
    python scripts/export_missing_vocab_sentences.py [lang]
Default lang: es
"""

import json
import re
import sys
from pathlib import Path

CONTENT_POS = {'noun', 'verb', 'adjective', 'adverb'}
WORD_RE = re.compile(r'\w+', re.UNICODE)


def load_lexicon(lang):
    verb_idx = {}
    word_idx = {}
    if lang == 'es':
        vp = Path('generated/indexes/verb-index.json')
        wp = Path('generated/indexes/word-index.json')
        if vp.exists():
            with open(vp, encoding='utf-8') as f:
                verb_idx = json.load(f)
        if wp.exists():
            with open(wp, encoding='utf-8') as f:
                word_idx = json.load(f)
    elif lang == 'hu':
        wp = Path('content/hu/indexes/word-index.json')
        if wp.exists():
            with open(wp, encoding='utf-8') as f:
                word_idx = json.load(f)

    def get_lemmas(token):
        t_low = token.lower()
        lemmas = set()
        if t_low in verb_idx:
            for entry in verb_idx[t_low]:
                lemmas.add(entry['lemma'].lower())
        if t_low in word_idx:
            for entry in word_idx[t_low]:
                lemmas.add(entry['lemma'].lower())
        if not lemmas:
            lemmas.add(t_low)
        return lemmas

    return get_lemmas


def main():
    lang = sys.argv[1] if len(sys.argv) > 1 else 'es'
    decks_path = Path(f'content/{lang}/decks/decks.json')
    trans_path = Path(f'content/{lang}/indexes/translation-index.json')

    if not decks_path.exists() or not trans_path.exists():
        print(f"[{lang}] Missing decks.json or translation-index.json")
        return

    with open(decks_path, encoding='utf-8') as f:
        deck_data = json.load(f)
    with open(trans_path, encoding='utf-8') as f:
        trans_data = json.load(f)

    get_lemmas = load_lexicon(lang)

    # Build context lemmas from sentences with >= 5 words
    context_lemmas = set()
    for pair in trans_data.get('pairs', []):
        text = pair.get('spanish', '')
        tokens = WORD_RE.findall(text)
        if len(tokens) < 5:
            continue
        for t in tokens:
            for lem in get_lemmas(t):
                context_lemmas.add(lem)
            context_lemmas.add(t.lower())

    # Map words to levels from lesson decks
    lemma_levels = {}
    for d in deck_data.get('decks', []):
        lvl = d.get('level')
        for lem in d.get('lemmas', []):
            if lem not in lemma_levels and lvl:
                lemma_levels[lem] = lvl

    words = deck_data.get('words', {})
    missing_by_level = {}

    for word, info in words.items():
        if info.get('pos') not in CONTENT_POS:
            continue
        lvl = lemma_levels.get(word, 'other')
        if lvl not in missing_by_level:
            missing_by_level[lvl] = []

        w_clean = word.lower().strip()
        matched = False
        parts = [p.strip() for p in re.split(r'[/,()]', w_clean) if p.strip()]
        for p in parts:
            if p in context_lemmas or any(l in context_lemmas for l in get_lemmas(p)):
                matched = True
                break

        if not matched:
            missing_by_level[lvl].append({
                'word': word,
                'en': info.get('en', ''),
                'pos': info.get('pos', ''),
                'level': lvl
            })

    out_dir = Path(f'content/{lang}/backfill_prompts')
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== {lang.upper()} Missing Vocabulary Sentences Summary ===")
    total_missing = sum(len(v) for v in missing_by_level.values())
    print(f"Total missing: {total_missing}")

    level_instructions = {
        'A1': "Keep sentences strictly at CEFR A1 level: present tense (presente de indicativo), simple subject-verb-object structures, basic everyday vocabulary.",
        'A2': "Keep sentences at CEFR A2 level: preterite (pretérito indefinido) and imperfect (pretérito imperfecto) tenses, simple compound sentences with 'porque', 'cuando', 'pero'.",
        'B1': "Keep sentences at CEFR B1 level: subjunctive mood where natural (presente de subjuntivo), conditional, future, relative clauses, intermediate vocabulary."
    }

    BATCH_SIZE = 100

    for lvl in sorted(missing_by_level.keys()):
        items = missing_by_level[lvl]
        print(f"  Level {lvl}: {len(items)} words")

        instr = level_instructions.get(lvl, f"Keep sentences natural and appropriate for level {lvl}.")

        for batch_idx in range(0, len(items), BATCH_SIZE):
            chunk = items[batch_idx:batch_idx + BATCH_SIZE]
            batch_num = (batch_idx // BATCH_SIZE) + 1
            total_batches = (len(items) + BATCH_SIZE - 1) // BATCH_SIZE

            filename = f"{lvl.lower()}_batch_{batch_num:02d}_of_{total_batches:02d}.txt"
            filepath = out_dir / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("SYSTEM PROMPT / INSTRUCTIONS:\n")
                f.write("You are an expert Spanish curriculum writer for a language learning application.\n")
                f.write("Your task is to generate ONE natural example sentence for each of the Spanish vocabulary words below.\n\n")
                f.write("RULES:\n")
                f.write(f"1. LEVEL: {instr}\n")
                f.write("2. MINIMUM LENGTH: The Spanish sentence MUST contain at least 6 to 12 words (minimum 5 words strictly required). Do not write short fragments like 'Él es alto.'\n")
                f.write("3. INFERABLE CONTEXT: The sentence must provide enough context that the meaning of the target word is clear and makes sense in context.\n")
                f.write("4. USAGE: Use the target word naturally (conjugated or inflected form is welcome if it's a verb or adjective).\n")
                f.write("5. TRANSLATION: Provide an accurate, natural English translation for the full sentence.\n")
                f.write("6. OUTPUT FORMAT: Output ONLY a valid JSON array of objects, with NO markdown commentary. Each object must have:\n")
                f.write('   {\n     "word": "<target word as listed>",\n     "spanish": "<full Spanish sentence>",\n     "english": "<full English translation>",\n     "level": "' + lvl + '"\n   }\n\n')
                f.write(f"VOCABULARY WORDS ({len(chunk)} words):\n")
                for it in chunk:
                    f.write(f"- {it['word']} ({it['pos']}): {it['en']}\n")

    print(f"\nPrompt files generated in: {out_dir}")


if __name__ == '__main__':
    main()
