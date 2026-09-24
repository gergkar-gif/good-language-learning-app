import json
import sys

block_num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
reqs = json.load(open(f'scripts/block{block_num}_all_reqs.json', encoding='utf-8'))

missing_total = 0
for k in sorted(reqs.keys()):
    v = reqs[k]
    st_file = f"content/es-latam/stories/world/b1/{v['st_file']}"
    try:
        st = json.load(open(st_file, encoding='utf-8'))
    except Exception as e:
        print(f"Error loading {st_file}: {e}")
        continue
    st_text = ' '.join(p['text'] for p in st.get('paragraphs', []))
    missing = [g for g in v['grammar_sentences'] if g not in st_text]
    if missing:
        print(f"=== {k} missing {len(missing)} ===")
        for m in missing:
            print("  MISSING:", repr(m))
        missing_total += len(missing)

if missing_total == 0:
    print(f"Block {block_num}: 100% PERFECT! 0 missing grammar sentences.")
else:
    print(f"Block {block_num}: Total missing = {missing_total}")
