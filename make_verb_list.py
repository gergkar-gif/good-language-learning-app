import os
import json

verbos_folder = 'verbos'
verbs = []

for filename in os.listdir(verbos_folder):
    if filename.endswith('.json'):
        verb_name = filename[:-5]
        verbs.append(verb_name)

verbs.sort()

with open('verb-list.js', 'w', encoding='utf-8') as f:
    f.write('const ALL_VERBS = ' + json.dumps(verbs, ensure_ascii=False) + ';\n')

print(f"Done! Found {len(verbs)} verbs.")