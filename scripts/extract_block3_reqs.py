import json, glob

block_units = ['economiasexportacion', 'cambiosocial', 'revolucion', 'revolucionmexicana', 'nacionalismo', 'grandepresion']

data = {}
for unit in block_units:
    data[unit] = {}
    for i in range(1, 6):
        num = f"{i:02d}"
        gr_files = glob.glob(f"content/es-latam/grammar/b1/b1-{unit}-{num}-*.json")
        ex_files = glob.glob(f"content/es-latam/exercises/b1/b1-{unit}-{num}-ex.json")
        voc_files = glob.glob(f"content/es-latam/vocabulary/b1/b1-{unit}-{num}-voc.json")
        lesson_files = glob.glob(f"content/es-latam/lessons/b1/b1-{unit}-{num}.json")
        
        lesson_data = {
            "story_ref": "",
            "grammar_title": "",
            "grammar_examples": [],
            "vocab": [],
            "questions": []
        }
        
        if lesson_files:
            ld = json.load(open(lesson_files[0], encoding='utf-8'))
            for sec in ld.get('sections', []):
                if sec.get('type') == 'story':
                    lesson_data['story_ref'] = sec.get('ref')
        
        if gr_files:
            gr = json.load(open(gr_files[0], encoding='utf-8'))
            lesson_data["grammar_title"] = gr.get('title', '')
            for sec in gr.get('sections', []):
                if sec.get('type') == 'examples':
                    for item in sec.get('items', []):
                        lesson_data["grammar_examples"].append(item.get('spanish', '').strip())
                        
        if voc_files:
            voc = json.load(open(voc_files[0], encoding='utf-8'))
            lesson_data["vocab"] = [w.get('lemma') or w.get('word') for w in voc.get('words', [])]
            
        if ex_files:
            ex_data = json.load(open(ex_files[0], encoding='utf-8'))
            for ex in ex_data.get('exercises', []):
                if ex.get('type') in ['multiple-choice', 'reading']:
                    lesson_data["questions"].append({
                        "q": ex.get('question'),
                        "opts": ex.get('options', []),
                        "ans": ex.get('answer')
                    })
        data[unit][num] = lesson_data

with open("scripts/block3_requirements.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved block3_requirements.json successfully!")
