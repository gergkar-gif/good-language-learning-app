import json,sys,glob
for st in sys.argv[1:]:
    d=json.load(open(f'exercises/b2/{st}-ex.json'))
    for e in d['exercises']:
        print(e['id'],e['type'],e['category'],e.get('teaches'),e.get('distractor_skills'),[k for k in e if k not in('id','type','category','teaches','question','options','correct','sentence','answer','english','pairs')])
