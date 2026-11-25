import json,os
B='/home/user/parlour-read-a/content/es-latam/'
def wj(p,d):
    with open(B+p,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')
def rj(p): return json.load(open(B+p,encoding='utf-8'))
def gr(stem,title,know,rows,exs,tip):
    d=rj(f'grammar/b2/{stem}-a-gr.json')
    d['title']=title
    d['sections']=[
     {"type":"text","title":"What you already know","content":know},
     {"type":"table","title":"At work on the topic","rows":[list(r) for r in rows]},
     {"type":"examples","title":"In context","items":[{"spanish":s,"english":e} for s,e in exs]},
     {"type":"tip","content":tip}]
    wj(f'grammar/b2/{stem}-a-gr.json',d)
def voc(stem,theme,words,title):
    d=rj(f'vocabulary/b2/{stem}-voc.json')
    d['title']=title; d['theme']=theme
    d['words']=[{"lemma":l,"translation":t,"pos":p} for l,t,p in words]
    wj(f'vocabulary/b2/{stem}-voc.json',d)
def lesson(stem,title,goal,grammar,goals,checklist=None):
    d=rj(f'lessons/b2/{stem}.json')
    d['title']=title; d['goal']=goal; d['grammar']=grammar
    for s in d['sections']:
        if s['type']=='goal': s['items']=goals
        if s['type']=='checklist' and checklist: s['items']=checklist
    wj(f'lessons/b2/{stem}.json',d)
def story(stem,title,summary,paras,qs):
    d=rj(f'stories/world/b2/{stem}.json')
    d['title']=title; d['summary']=summary; d['characters']=[]
    d['paragraphs']=[{"type":"narration","text":t} for t in paras]
    d['narration']={"pedagogical":{"comprehensionQuestions":[
      {"question":q,"options":o,"correctIndex":0,"explanation":e} for q,o,e in qs]}}
    wj(f'stories/world/b2/{stem}.json',d)
    n=sum(len(t.split()) for t in paras); print(stem,'words',n)
def ex(stem,items):
    d={"lesson":stem,"exercises":items}
    for i,e in enumerate(items,1):
        e['id']=f'{stem}.ex{i:02d}'
        # key order: id first
    d['exercises']=[{**{'id':e['id']},**{k:v for k,v in e.items() if k!='id'}} for e in items]
    wj(f'exercises/b2/{stem}-ex.json',d)
# item helpers
def match(pairs,skill): return {"type":"matching","category":"vocabulary","pairs":[list(p) for p in pairs],"teaches":[skill]}
def fill(sentence,answer,english,skill,hint=None,answers=None):
    e={"type":"fill-blank","category":"grammar","sentence":sentence}
    if hint: e['hint']=hint
    if answers: e['answers']=answers
    else: e['answer']=answer
    e['english']=english; e['teaches']=[skill]; return e
def mc(q,opts,skill,cat="grammar",ds=None):
    e={"type":"multiple-choice","category":cat,"question":q,"options":opts,"correct":0}
    if skill: e['teaches']=[skill]
    if ds: e['distractor_skills']=ds
    return e
def build(sentence,english,skill):
    t=sentence.split()
    return {"type":"sentence-builder","category":"grammar","tiles":t,"solution":t,"english":english,"teaches":[skill]}
def dlg(lines,opts,skill,cat="dialogue"):
    return {"type":"dialogue-complete","category":cat,"prompt":[{"speaker":s,"text":t} for s,t in lines],"options":opts,"correct":0,"teaches":[skill]}
def dic(sentence,english,skill):
    return {"type":"dictation","category":"listening","sentence":sentence,"english":english,"teaches":[skill]}
