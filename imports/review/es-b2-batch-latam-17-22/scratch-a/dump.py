import json,sys,glob
stems=sys.argv[1:]
base='content/es-latam/'
for s in stems:
    print('=====',s)
    for kind,suf in [('lessons',''),('vocabulary','-voc'),('exercises','-ex')]:
        p=f'{base}{kind}/b2/{s}{suf}.json'
        try: d=json.load(open(p))
        except Exception as e: print('missing',p); continue
        if kind=='lessons':
            print('LESSON',d['title'],'|',d['goal'],'|',d.get('grammar'))
            for sec in d['sections']:
                print('  sec',sec['type'],sec.get('ref',''),sec.get('exerciseRefs',''),sec.get('items',''))
        elif kind=='vocabulary':
            print('VOC',json.dumps(d,ensure_ascii=False))
        else:
            for e in d['exercises']:
                print(json.dumps(e,ensure_ascii=False))
