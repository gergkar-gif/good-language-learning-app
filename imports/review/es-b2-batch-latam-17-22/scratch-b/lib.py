import json,os
R='/home/user/parlour-read-b/content/es-latam/'
def jd(p,d):
    with open(R+p,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')
def jl(p): return json.load(open(R+p,encoding='utf-8'))
def vocab(stem,words,title=None):
    p=f'vocabulary/b2/{stem}-voc.json'; d=jl(p)
    if title: d['title']=title
    d['words']=[{'lemma':l,'translation':t,'pos':pos} for l,t,pos in words]
    jd(p,d)
def grammar(stem,title,sections):
    p=f'grammar/b2/{stem}-a-gr.json'; d=jl(p); d['title']=title; d['sections']=sections; jd(p,d)
def lesson(stem,title,goal,gram,goalitems,checklist=None):
    p=f'lessons/b2/{stem}.json'; d=jl(p); d['title']=title; d['goal']=goal; d['grammar']=gram
    for s in d['sections']:
        if s['type']=='goal': s['items']=goalitems
        if s['type']=='checklist' and checklist: s['items']=checklist
    jd(p,d)
def story(stem,title,summary,paras,qs):
    p=f'stories/world/b2/{stem}.json'; d=jl(p)
    d['title']=title; d['summary']=summary; d['characters']=[]
    d['paragraphs']=[{'type':'narration','text':t} for t in paras]
    d['narration']['pedagogical']['comprehensionQuestions']=[
      {'question':q,'options':o,'correctIndex':0,'explanation':e} for q,o,e in qs]
    jd(p,d)
    n=sum(len(t.split()) for t in paras); print(stem,'words',n)
def ex(stem,items):
    p=f'exercises/b2/{stem}-ex.json'; d=jl(p); d['exercises']=items; jd(p,d)
def eid(stem,n): return f'{stem}.ex{n:02d}'
def match(stem,n,pairs,skill):
    return {'id':eid(stem,n),'type':'matching','category':'vocabulary','pairs':pairs,'teaches':[skill]}
def fill(stem,n,sentence,answer,english,skill,hint=None,answers=None,cat='grammar'):
    d={'id':eid(stem,n),'type':'fill-blank','category':cat,'sentence':sentence}
    if hint: d['hint']=hint
    if answers: d['answers']=answers
    else: d['answer']=answer
    d['english']=english; d['teaches']=[skill]; return d
def mc(stem,n,q,opts,skill,ds=None,cat='grammar'):
    d={'id':eid(stem,n),'type':'multiple-choice','category':cat,'question':q,'options':opts,'correct':0}
    if skill: d['teaches']=[skill]
    if ds: d['distractor_skills']={str(k):v for k,v in ds.items()}
    return d
def build(stem,n,sentence,english,skill):
    t=sentence.split()
    return {'id':eid(stem,n),'type':'sentence-builder','category':'grammar','tiles':t,'solution':t,'english':english,'teaches':[skill]}
def dlg(stem,n,lines,opts,skill,ds=None):
    d={'id':eid(stem,n),'type':'dialogue-complete','category':'dialogue','prompt':[{'speaker':s,'text':t} for s,t in lines],'options':opts,'correct':0,'teaches':[skill]}
    if ds: d['distractor_skills']={str(k):v for k,v in ds.items()}
    return d
def dict_(stem,n,sentence,english,skill):
    return {'id':eid(stem,n),'type':'dictation','category':'listening','sentence':sentence,'english':english,'teaches':[skill]}
def chall(unit,entries):
    p=f'/home/user/parlour-read-b/challenges-{unit}.json'
    json.dump(entries,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
def C(title,scenario,prompt,cues,target,english,canDo):
    return {'tier':'tier1','level':'B2','title':'Communicative Challenge: '+title,'scenario':scenario,'prompt':prompt,'cues':cues,'target':target,'english':english,'canDo':canDo}
