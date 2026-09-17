#!/usr/bin/env python3
"""
One-time import: turn the user's ChatGPT-sourced CEFR exam-style prompt
text files into content/<lang>/writing-prompts.json (appended) and
content/<lang>/speaking-prompts.json (new dedicated file — Speaking Studio
previously reused writing-prompts.json for lack of anything better; see
ROADMAP.md item 28).

Source format (one file per language/level combo the user hand-produced
via ChatGPT, each with a WRITING and a SPEAKING section):

    A1-W01 | Some Title
    Situation:
    <one or more lines>

    Task:
    <task line(s)>
    In your message: / Talk about: / Consider: / Include: (bullet-list
    header — dropped, the bullets below carry the content)
    - point one
    - point two

    Write approximately 40-50 words.   (or: Speak for approximately 1-2 minutes.)

Usage:
    python scripts/import_cefr_exam_prompts.py <file1.txt> [file2.txt ...]

Existing entries in writing-prompts.json are never touched — this only
appends new ones (by id) and is safe to re-run on the same source files
(re-running replaces same-id entries rather than duplicating them).
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ENTRY_RE = re.compile(r'^([A-Za-z0-9]+-[WS]\d+)\s*\|\s*(.+)$')
LEVEL_HEADER_RE = re.compile(r'^(HUNGARIAN|SPANISH)\s+([A-C]\d)$')
TARGET_WORDS_RE = re.compile(r'Write approximately (\d+)-(\d+) words', re.IGNORECASE)
TARGET_TIME_RANGE_RE = re.compile(r'approximately (\d+)-(\d+) minutes', re.IGNORECASE)
TARGET_TIME_SINGLE_RE = re.compile(r'approximately (\d+) minutes?', re.IGNORECASE)

HU_TRANSLIT = str.maketrans({
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ő': 'o',
    'ú': 'u', 'ü': 'u', 'ű': 'u', 'Á': 'a', 'É': 'e', 'Í': 'i',
    'Ó': 'o', 'Ö': 'o', 'Ő': 'o', 'Ú': 'u', 'Ü': 'u', 'Ű': 'u'
})


def slugify(text, max_len=40):
    text = text.translate(HU_TRANSLIT)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-zA-Z0-9]+', '_', text).strip('_').lower()
    return text[:max_len].rstrip('_')


def parse_file(path):
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    entries = []
    current_lang = None
    current_level = None
    current_type = None
    i, n = 0, len(lines)

    while i < n:
        line = lines[i].strip()

        m = LEVEL_HEADER_RE.match(line)
        if m:
            current_lang = 'hu' if m.group(1) == 'HUNGARIAN' else 'es'
            current_level = m.group(2)
            i += 1
            continue
        if line == 'WRITING':
            current_type = 'writing'
            i += 1
            continue
        if line == 'SPEAKING':
            current_type = 'speaking'
            i += 1
            continue

        em = ENTRY_RE.match(line)
        if em:
            code, title = em.group(1), em.group(2).strip()
            i += 1
            situation_lines, task_lines, points = [], [], []
            target_min = target_max = None
            mode = None

            while i < n:
                l = lines[i].strip()
                if ENTRY_RE.match(l) or LEVEL_HEADER_RE.match(l) or l in ('WRITING', 'SPEAKING'):
                    break
                if l == 'Situation:':
                    mode = 'situation'; i += 1; continue
                if l == 'Task:':
                    mode = 'task'; i += 1; continue
                if l.startswith('- '):
                    points.append(l[2:].strip()); i += 1; continue
                wm = TARGET_WORDS_RE.search(l)
                if wm:
                    target_min, target_max = int(wm.group(1)), int(wm.group(2)); i += 1; continue
                tm = TARGET_TIME_RANGE_RE.search(l)
                if tm:
                    target_min, target_max = int(tm.group(1)), int(tm.group(2)); i += 1; continue
                tsm = TARGET_TIME_SINGLE_RE.search(l)
                if tsm and target_min is None:
                    v = int(tsm.group(1)); target_min, target_max = v, v; i += 1; continue
                if l == '':
                    i += 1; continue
                if l.endswith(':') and len(l) < 60:
                    i += 1; continue
                (situation_lines if mode == 'situation' else task_lines).append(l)
                i += 1

            entries.append({
                'lang': current_lang, 'level': current_level, 'type': current_type,
                'code': code, 'title': title,
                'situation': ' '.join(situation_lines).strip(),
                'task': ' '.join(task_lines).strip(),
                'points': points,
                'target_min': target_min, 'target_max': target_max,
            })
            continue
        i += 1

    return entries


def compose_prompt_text(e):
    points_str = '; '.join(e['points'])
    task_full = e['task']
    if points_str:
        task_full = f"{task_full} Include: {points_str}."
    if e['type'] == 'writing':
        target_line = f"Write approximately {e['target_min']}-{e['target_max']} words." if e['target_min'] else ''
    else:
        target_line = (f"Speak for approximately {e['target_min']} minutes."
                        if e['target_min'] == e['target_max']
                        else f"Speak for approximately {e['target_min']}-{e['target_max']} minutes.")
    return f"Situation: {e['situation']}\n\nTask: {task_full}\n\n{target_line}".strip()


def to_content_entry(e):
    entry = {
        'id': f"{e['lang']}-{e['code'].lower()}",
        'cefrLevel': e['level'],
        'taskType': slugify(e['title']),
        'title': e['title'],
        'situation': e['situation'],
        'task': e['task'],
        'points': e['points'],
        'prompt': compose_prompt_text(e),
    }
    if e['type'] == 'writing':
        entry['minWords'] = e['target_min']
        entry['targetWords'] = round((e['target_min'] + e['target_max']) / 2)
        entry['maxWords'] = e['target_max']
    else:
        entry['minSeconds'] = e['target_min'] * 60
        entry['targetSeconds'] = round((e['target_min'] + e['target_max']) / 2 * 60)
        entry['maxSeconds'] = e['target_max'] * 60 + 30
    return entry


def merge_prompts(existing_path, new_entries, entries_key='prompts'):
    if existing_path.is_file():
        data = json.loads(existing_path.read_text(encoding='utf-8'))
    else:
        lang = existing_path.parent.name
        data = {'language': lang, entries_key: []}
    by_id = {p['id']: p for p in data[entries_key]}
    for e in new_entries:
        by_id[e['id']] = e
    data[entries_key] = list(by_id.values())
    existing_path.parent.mkdir(parents=True, exist_ok=True)
    existing_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    return len(new_entries), len(data[entries_key])


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    all_entries = []
    for path in sys.argv[1:]:
        all_entries.extend(parse_file(path))

    by_lang_type = {}
    for e in all_entries:
        content = to_content_entry(e)
        by_lang_type.setdefault((e['lang'], e['type']), []).append(content)

    for (lang, etype), entries in sorted(by_lang_type.items()):
        filename = 'writing-prompts.json' if etype == 'writing' else 'speaking-prompts.json'
        path = Path(f'content/{lang}/{filename}')
        added, total = merge_prompts(path, entries)
        print(f"[{lang}/{etype}] {added} entries merged into {path} (now {total} total)")


if __name__ == '__main__':
    main()
