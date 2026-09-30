import json, sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('content/hu/curriculum/units/b1.json', encoding='utf-8'))
cz = [u for u in data if u.get('track') == 'citizenship']
for i, u in enumerate(cz):
    prefix = u['stems'][0].split('-')[1]
    print(f"{i+1:2d}: {prefix:<25} | {u['title']}")

