import json, glob, os

def get_grammar_examples(unit, num):
    gr_files = glob.glob(f"content/es-latam/grammar/b1/b1-{unit}-{num}-*.json")
    if not gr_files:
        return []
    gr = json.load(open(gr_files[0], encoding='utf-8'))
    examples = []
    for sec in gr.get('sections', []):
        if sec.get('type') == 'examples':
            for item in sec.get('items', []):
                examples.append(item.get('spanish', '').strip())
    return examples

# Let's inspect each lesson in block 3 and write the stories
print("Block 3 Grammar examples:")
for unit in ['economiasexportacion', 'cambiosocial', 'revolucion', 'revolucionmexicana', 'nacionalismo', 'grandepresion']:
    for i in range(1, 6):
        num = f"{i:02d}"
        exs = get_grammar_examples(unit, num)
        print(f"{unit}-{num}: {len(exs)} examples")
        for e in exs:
            print(f"   * {repr(e)}")
