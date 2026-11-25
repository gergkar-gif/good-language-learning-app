import json,os
B='/home/user/parlour-read-b/content/es-latam/'
def rj(p): return json.load(open(p,encoding='utf-8'))
def wj(p,o): open(p,'w',encoding='utf-8').write(json.dumps(o,indent=2,ensure_ascii=False))
def grammar(stem,title,sections):
    p=B+f'grammar/b2/{stem}-a-gr.json'; d=rj(p); d['title']=title; d['sections']=sections; wj(p,d)
def mc(n,stem,cat,teach,q,opts,correct,ds=None):
    x={"id":f"{stem}.ex{n:02d}","type":"multiple-choice","category":cat}
    if teach: x["teaches"]=[teach]
    x["question"]=q; x["options"]=opts; x["correct"]=correct
    if ds: x["distractor_skills"]={str(k):v for k,v in ds.items()}
    return x
def fb(n,stem,teach,sent,ans,eng,hint=None,answers=None):
    x={"id":f"{stem}.ex{n:02d}","type":"fill-blank","category":"grammar","teaches":[teach],"sentence":sent}
    if hint: x["hint"]=hint
    if answers: x["answers"]=answers
    else: x["answer"]=ans
    x["english"]=eng; return x
def mt(n,stem,voc,pairs):
    return {"id":f"{stem}.ex{n:02d}","type":"matching","category":"vocabulary","teaches":[voc],"pairs":[list(p) for p in pairs]}
def exercises(stem,items):
    wj(B+f'exercises/b2/{stem}-ex.json',{"lesson":stem,"exercises":items})
def vocab(stem,title,words):
    p=B+f'vocabulary/b2/{stem}-voc.json'; d=rj(p); d['title']=title
    d['words']=[{"lemma":a,"translation":b,"pos":c} for a,b,c in words]; wj(p,d)
def story(stem,title,summary,paras,qs):
    p=B+f'stories/world/b2/{stem}.json'; d=rj(p)
    d['title']=title; d['summary']=summary; d['characters']=[]
    d['paragraphs']=[{"type":"narration","text":t} for t in paras]
    d['narration']['pedagogical']['comprehensionQuestions']=[{"question":q,"options":o,"correctIndex":c,"explanation":e} for q,o,c,e in qs]
    wj(p,d)
def lesson(stem,title,goal):
    p=B+f'lessons/b2/{stem}.json'; d=rj(p)
    new={}
    for k,v in d.items():
        new[k]=title if k=='title' else v
        if k=='level': new['goal']=goal
    wj(p,new)
def words(paras): return sum(len(t.split()) for t in paras)
def challenges(unit,ch):
    wj(f'/home/user/parlour-read-b/challenges-{unit}.json',ch)
def chal(title,scen,prompt,cues,target,eng,cando):
    return {"tier":"tier1","level":"B2","title":"Communicative Challenge: "+title,"scenario":scen,"prompt":prompt,"cues":cues,"target":target,"english":eng,"canDo":cando}
