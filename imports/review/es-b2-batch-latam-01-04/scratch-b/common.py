import json,os
R='/home/user/parlour-read-b/content/es-latam/'
def jl(p):
    return json.load(open(R+p))
def jw(p,d):
    with open(R+p,'w') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')

def gr(slug_id, title, recap, table_title, rows, tip_title, examples, tip, mid=None):
    secs=[{"type":"text","title":"What you already know","content":recap},
          {"type":"table","title":table_title,"rows":[list(r) for r in rows]}]
    if mid: secs.append({"type":"text","title":mid[0],"content":mid[1]})
    secs.append({"type":"examples","title":"In context","items":[{"spanish":a,"english":b} for a,b in examples]})
    secs.append({"type":"tip","content":tip})
    return {"id":slug_id,"title":title,"sections":secs}

def vocab(stem,theme,title,words):
    return {"id":"vocab."+stem.replace('b2-','b2.').replace('-','.',1) if False else None,"lesson":stem,"title":title,"theme":theme,"words":[{"lemma":l,"translation":t,"pos":p} for l,t,p in words]}

def apply_lesson(stem,title,goal,grammar,goal_items,intro=None):
    p=f'lessons/b2/{stem}.json'
    d=jl(p)
    d['title']=title; d['goal']=goal; d['grammar']=grammar
    for s in d['sections']:
        if s['type']=='goal': s['items']=goal_items
        if s['type']=='intro' and intro: s['title'],s['body']=intro
    jw(p,d)

def apply_story(stem,title,summary,grammar,paras):
    p=f'stories/world/b2/{stem}.json'
    d=jl(p)
    d['title']=title; d['summary']=summary; d['grammar']=grammar
    d['paragraphs']=[{"text":t,"type":"narration"} for t in paras]
    jw(p,d)
    return sum(len(t.split()) for t in paras)

def apply_gr(stem,g):
    p=f'grammar/b2/{stem}-a-gr.json'
    jw(p,g)

def apply_voc(stem,words,title=None,theme=None):
    p=f'vocabulary/b2/{stem}-voc.json'
    d=jl(p)
    d['words']=[{"lemma":l,"translation":t,"pos":p_} for l,t,p_ in words]
    if title: d['title']=title
    if theme: d['theme']=theme
    jw(p,d)

def apply_ex(stem,exs,fname=None):
    p=f'exercises/b2/{fname or stem+"-ex"}.json'
    d=jl(p); d['exercises']=exs; jw(p,d)

def mc(i,stem,cat,q,opts,teaches=None,ds=None):
    e={"id":i,"type":"multiple-choice","category":cat,"question":q,"options":opts,"correct":0}
    if teaches: e["teaches"]=[teaches]
    if ds: e["distractor_skills"]=ds
    return e
def match(i,pairs,v):
    return {"id":i,"type":"matching","category":"vocabulary","pairs":[list(p) for p in pairs],"teaches":[v]}
def fill(i,sent,ans,eng,t,hint=None,answers=None):
    e={"id":i,"type":"fill-blank","category":"grammar","sentence":sent}
    if hint: e["hint"]=hint
    if answers: e["answers"]=answers
    else: e["answer"]=ans
    e["english"]=eng; e["teaches"]=[t]; return e
def build(i,sol,eng,t):
    return {"id":i,"type":"sentence-builder","category":"grammar","tiles":list(sol),"solution":list(sol),"english":eng,"teaches":[t]}
def dlg(i,lines,opts,t,cat="dialogue",ds=None):
    pr=[{"speaker":s,"text":x} for s,x in lines]
    e={"id":i,"type":"dialogue-complete","category":cat,"prompt":pr,"options":opts,"correct":0,"teaches":[t]}
    if ds: e["distractor_skills"]=ds
    return e
def dict_(i,s,eng,t):
    return {"id":i,"type":"dictation","category":"listening","sentence":s,"english":eng,"teaches":[t]}
