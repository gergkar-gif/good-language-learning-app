import json,sys,glob
stem=sys.argv[1]
base='content/es-latam/'
def L(p):
    try: return json.load(open(base+p))
    except Exception as e: return None
l=L(f'lessons/b2/{stem}.json')
print('LESSON',l['title'],'|',l['goal'],'|',l['grammar'])
for s in l['sections']:
    if s['type'] in('intro','goal','checklist'): print(' ',s['type'],s.get('title'),s.get('body') or s.get('items'))
    else: print(' ',s['type'],s.get('ref'),s.get('exerciseRefs'),s.get('count'))
g=L(f'grammar/b2/{stem}-a-gr.json')
if g: print('GRAMMAR',g['id'],g['title']); [print('  ',json.dumps(s,ensure_ascii=False)[:600]) for s in g['sections']]
v=L(f'vocabulary/b2/{stem}-voc.json')
if v: print('VOC',[ (w['lemma'],w['translation']) for w in v['words']])
e=L(f'exercises/b2/{stem}-ex.json')
if e:
  for x in e['exercises']: print('EX',json.dumps(x,ensure_ascii=False))
s=L(f'stories/world/b2/{stem}.json')
if s:
  print('STORY',s['title'],'|',s['summary'],s.get('grammar'))
  for p in s['paragraphs']: print('  P',p['text'])
  for q in s['narration']['pedagogical']['comprehensionQuestions']: print('  Q',q['question'])
