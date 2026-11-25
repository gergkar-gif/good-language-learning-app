import json,sys
u=sys.argv[1]; n=sys.argv[2]
b='content/es-latam/'
stem=f'b2-{u}-{n}'
L=json.load(open(b+f'lessons/b2/{stem}.json'))
print('LESSON',L.get('title'),'| goal:',L.get('goal'),'| grammar:',L.get('grammar'), [s['type'] for s in L['sections']])
import os
g=b+f'grammar/b2/{stem}-a-gr.json'
if os.path.exists(g):
    G=json.load(open(g)); print('GR',G['title'])
    for s in G['sections']: print(' ',json.dumps(s,ensure_ascii=False)[:1500])
e=b+f'exercises/b2/{stem}-ex.json'
E=json.load(open(e))
for x in E['exercises']:
    print(json.dumps(x,ensure_ascii=False))
v=b+f'vocabulary/b2/{stem}-voc.json'
if os.path.exists(v):
    V=json.load(open(v)); print('VOC',[w['lemma']+'='+w['translation'] for w in V['words']])
s=b+f'stories/world/b2/{stem}.json'
if os.path.exists(s):
    S=json.load(open(s)); print('STORY',S['title'],'|',S['summary'],'|',S.get('characters'))
    for p in S['paragraphs']: print(' P:',p['text'])
    for q in S['narration']['pedagogical']['comprehensionQuestions']: print(' Q:',json.dumps(q,ensure_ascii=False))
