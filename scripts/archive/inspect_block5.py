import json

reqs = json.load(open('scripts/block5_all_reqs.json', encoding='utf-8'))
for k in sorted(reqs.keys()):
    v = reqs[k]
    print(f"=== {k} ({v['st_file']}) ===")
    print("Title:", v['st_title'])
    print("Grammar count:", len(v['grammar_sentences']))
    for idx, g in enumerate(v['grammar_sentences']):
        print(f"  G[{idx}]: {repr(g)}")
