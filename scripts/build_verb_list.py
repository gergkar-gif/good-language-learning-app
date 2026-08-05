import os
import json

verbos_folder = 'imports/verbs'
verbs = []

for filename in os.listdir(verbos_folder):
    if filename.endswith('.json'):
        verb_name = filename[:-5]
        verbs.append(verb_name)

verbs.sort()

with open('imports/verbs/verb-list.js', 'w', encoding='utf-8') as f:
    f.write('const ALL_VERBS = ' + json.dumps(verbs, ensure_ascii=False) + ';\n')

print(f"Done! Generated imports/verbs/verb-list.js with {len(verbs)} verbs.")