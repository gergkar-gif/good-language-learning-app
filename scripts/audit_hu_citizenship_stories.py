import sys, os, glob, json
sys.stdout.reconfigure(encoding='utf-8')
from importlib.machinery import SourceFileLoader
audit_mod = SourceFileLoader('audit', 'scripts/audit-reading-quality.py').load_module()

units = ['anjouk', 'matyas', 'mohacs', 'haromresz', 'erdelyaranykora', 'torokkiuzese']
for u in units:
    print(f'=== UNIT: b1-{u} ===')
    for i in range(1, 6):
        story_f = f'content/hu/stories/world/b1/b1-{u}-0{i}-*.json'
        matches = glob.glob(story_f)
        if not matches:
            continue
        sf = matches[0]
        vf = f'content/hu/vocabulary/b1/b1-{u}-0{i}-voc.json'
        with open(vf, encoding='utf-8') as fp:
            v_data = json.load(fp)
        res = audit_mod.audit_story_file(sf, v_data.get('words', []))
        ret = res['vocab_retention']
        pct = ret['pct'] if ret else 0
        missing = ret['missing'] if ret else []
        print(f"  {os.path.basename(sf):40} | AvgSent: {res['avg_sent_len']:4.1f}w | MaxSent: {res['max_sent_len']:2}w | Vocab: {pct:5.1f}% | Missing: {missing}")
    omni_f = f'content/hu/stories/world/b1/b1-{u}.json'
    if os.path.exists(omni_f):
        res = audit_mod.audit_story_file(omni_f)
        print(f"  {os.path.basename(omni_f):40} | AvgSent: {res['avg_sent_len']:4.1f}w | MaxSent: {res['max_sent_len']:2}w")
