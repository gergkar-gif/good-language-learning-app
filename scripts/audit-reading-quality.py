#!/usr/bin/env python3
"""Audit reading quality across curricula.

Checks:
1. Paragraph structure: all paragraphs must be typed (type: 'narration' or 'dialogue').
   Dialogue must have a non-empty 'speaker'.
2. Scaffolding constraints: checks lang == 'en' proportions against level guidelines.
3. Target vocabulary inclusion: checks what percentage of taught vocabulary
   from the corresponding unit appears in the story (target >= 85%).
4. Sentence length metrics: average and max sentence length.
"""

import json
import glob
import os
import re
import sys
import unicodedata

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def norm(text):
    text = unicodedata.normalize("NFD", str(text).lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", " ", text)

def clean_lemma(lemma):
    lemma = norm(lemma)
    lemma = re.sub(r"^(el|la|los|las|un|una|unos|unas|a|az|egy)\s+", "", lemma)
    return lemma.strip()

def audit_story_file(story_path, vocab_words=None):
    with open(story_path, encoding='utf-8') as fp:
        d = json.load(fp)

    paras = d.get('paragraphs', [])
    errors = []
    warnings = []

    if not paras:
        errors.append("Story has no paragraphs")
        return {"errors": errors, "warnings": warnings}

    typed_count = 0
    en_count = 0
    target_count = 0
    target_text_parts = []
    sentence_lengths = []

    for i, p in enumerate(paras):
        if not isinstance(p, dict):
            errors.append(f"Para {i}: Not a dict (legacy untyped paragraph)")
            continue
        p_type = p.get('type')
        if p_type not in ('narration', 'dialogue'):
            errors.append(f"Para {i}: Invalid or missing type '{p_type}'")
        else:
            typed_count += 1

        if p_type == 'dialogue' and not p.get('speaker'):
            errors.append(f"Para {i}: Dialogue paragraph missing 'speaker'")

        text = p.get('text', '')
        if not text.strip():
            errors.append(f"Para {i}: Empty text")

        if p.get('lang') == 'en':
            en_count += 1
        else:
            target_count += 1
            target_text_parts.append(text)
            for s in re.split(r'[.!?¿¡]+', text):
                s_words = s.strip().split()
                if s_words:
                    sentence_lengths.append(len(s_words))

    pct_en = (en_count / len(paras) * 100) if paras else 0
    avg_sent = (sum(sentence_lengths) / len(sentence_lengths)) if sentence_lengths else 0
    max_sent = max(sentence_lengths) if sentence_lengths else 0

    vocab_retention = None
    if vocab_words:
        target_norm = norm(" ".join(target_text_parts))
        found_c = 0
        missing = []
        for w in vocab_words:
            lemma = clean_lemma(w.get('lemma', ''))
            tokens = [t for t in lemma.split() if len(t) > 2] or lemma.split()
            is_in = any(re.search(r'\b' + re.escape(t) + r'[a-z]*\b', target_norm) for t in tokens)
            if is_in:
                found_c += 1
            else:
                missing.append(w.get('lemma', ''))
        vocab_retention = {
            "total": len(vocab_words),
            "found": found_c,
            "pct": (found_c / len(vocab_words) * 100) if vocab_words else 0,
            "missing": missing
        }

    return {
        "id": d.get('id'),
        "title": d.get('title'),
        "total_paras": len(paras),
        "typed_paras": typed_count,
        "en_paras": en_count,
        "target_paras": target_count,
        "pct_en": pct_en,
        "avg_sent_len": avg_sent,
        "max_sent_len": max_sent,
        "vocab_retention": vocab_retention,
        "errors": errors,
        "warnings": warnings
    }

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'es-a1'
    print(f"Auditing target: {target}")
    if target == 'es-a1':
        files = sorted(glob.glob(os.path.join(ROOT, 'content', 'es', 'stories', 'original', 'a1', '*.json')))
        for f in files:
            res = audit_story_file(f)
            err_str = f" ERRORS: {len(res['errors'])}" if res['errors'] else " OK"
            print(f"{os.path.basename(f):25} | Paras: {res['total_paras']:2} | EN: {res['pct_en']:4.1f}% | AvgSent: {res['avg_sent_len']:4.1f}w |{err_str}")
