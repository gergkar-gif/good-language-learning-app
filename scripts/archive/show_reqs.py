import json, sys

block_num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
filename = f"scripts/block{block_num}_requirements.json"

data = json.load(open(filename, encoding='utf-8'))
for unit, lessons in data.items():
    print(f"\n==================================================")
    print(f" UNIT: {unit} ")
    print(f"==================================================")
    for num, l in lessons.items():
        print(f"\n--- {unit}-{num} (story: {l['story_ref']}) ---")
        print("  GRAMMAR TITLE:", l['grammar_title'])
        for ge in l['grammar_examples']:
            print(f"    GR: {ge}")
        print("  VOCAB:", ", ".join(l['vocab']))
        for q in l['questions']:
            print(f"    Q: {q['q']}")
            if q['opts']:
                print(f"       OPTS: {q['opts']}")
