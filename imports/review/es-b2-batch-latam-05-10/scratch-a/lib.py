import json,os
B='/home/user/parlour-read-a/content/es-latam/'
def rd(p): return json.load(open(B+p))
def wr(p,d):
    with open(B+p,'w') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')
def lesson(stem,title,goal,grammar,intro,goalitems,checklist=None):
    p=f'lessons/b2/{stem}.json'; d=rd(p)
    d['title']=title; d['goal']=goal; d['grammar']=grammar
    for s in d['sections']:
        if s['type']=='intro': s['title']=title; s['body']=intro
        elif s['type']=='goal': s['items']=goalitems
        elif s['type']=='checklist' and checklist: s['items']=checklist
    wr(p,d)
def grammar(stem,title,sections):
    p=f'grammar/b2/{stem}-a-gr.json'; d=rd(p); d['title']=title; d['sections']=sections; wr(p,d)
def vocab(stem,title,theme,words):
    p=f'vocabulary/b2/{stem}-voc.json'; d=rd(p); d['title']=title; d['theme']=theme
    d['words']=[{'lemma':a,'translation':b,'pos':c} for a,b,c in words]; wr(p,d)
def ex(stem,items):
    p=f'exercises/b2/{stem}-ex.json'; d=rd(p); d['exercises']=items; wr(p,d)
def story(stem,title,summary,topics,gram,paras,qs):
    p=f'stories/world/b2/{stem}.json'; d=rd(p)
    d['title']=title; d['summary']=summary; d['vocabularyTopics']=topics; d['grammar']=gram
    d['paragraphs']=[{'type':'narration','text':t} for t in paras]
    d['narration']['pedagogical']['comprehensionQuestions']=[
      {'question':q,'options':o,'correctIndex':c,'explanation':e} for q,o,c,e in qs]
    wr(p,d)
    n=sum(len(t.split()) for t in paras); print(stem,'words',n)
def mc(id,q,opts,cat='grammar',teaches=None,ds=None):
    x={'id':id,'type':'multiple-choice','category':cat,'question':q,'options':opts,'correct':0}
    if teaches: x['teaches']=[teaches]
    if ds: x['distractor_skills']={str(k):v for k,v in ds.items()}
    return x
def fb(id,s,a,en,t,hint=None):
    x={'id':id,'type':'fill-blank','category':'grammar','sentence':s}
    if hint: x['hint']=hint
    x['answer']=a; x['english']=en; x['teaches']=[t]; return x
def sb(id,sol,en,t):
    import random
    tiles=list(sol); pass
    return {'id':id,'type':'sentence-builder','category':'grammar','tiles':tiles,'solution':sol,'english':en,'teaches':[t]}
def dlg(id,lines,opts,t):
    return {'id':id,'type':'dialogue-complete','category':'dialogue','prompt':[{'speaker':a,'text':b} for a,b in lines],'options':opts,'correct':0,'teaches':[t]}
def dic(id,s,en,t): return {'id':id,'type':'dictation','category':'listening','sentence':s,'english':en,'teaches':[t]}
def match(id,pairs,t): return {'id':id,'type':'matching','category':'vocabulary','pairs':pairs,'teaches':[t]}
