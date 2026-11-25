import json,os
C='/home/user/parlour-read-a/content/es-latam/'
def rd(p): return json.load(open(C+p,encoding='utf8'))
def wr(p,o):
    open(C+p,'w',encoding='utf8').write(json.dumps(o,indent=2,ensure_ascii=False))
def mc(id,cat,q,opts,teaches=None,ds=None,correct=0):
    e={"id":id,"type":"multiple-choice","category":cat,"question":q,"options":opts,"correct":correct}
    if teaches: e["teaches"]=[teaches]
    if ds: e["distractor_skills"]=ds
    return e
def match(id,pairs,t): return {"id":id,"type":"matching","category":"vocabulary","pairs":pairs,"teaches":[t]}
def fill(id,s,ans,en,t,hint=None,answers=None):
    e={"id":id,"type":"fill-blank","category":"grammar","sentence":s}
    if hint: e["hint"]=hint
    if answers: e["answers"]=answers
    else: e["answer"]=ans
    e["english"]=en; e["teaches"]=[t]; return e
def build(id,sent,en,t):
    toks=sent.split(' ')
    return {"id":id,"type":"sentence-builder","category":"grammar","tiles":toks,"solution":toks,"english":en,"teaches":[t]}
def dlg(id,l1,l2,l3,opts,t,sp=("Meg","Carlos")):
    return {"id":id,"type":"dialogue-complete","category":"dialogue","prompt":[{"speaker":sp[0],"text":l1},{"speaker":sp[1],"text":"_____"},{"speaker":sp[0],"text":l3}],"options":opts,"correct":0,"teaches":[t]}
def dict_(id,s,en,t): return {"id":id,"type":"dictation","category":"listening","sentence":s,"english":en,"teaches":[t]}
def put_ex(stem,exs):
    wr(f'exercises/b2/{stem}-ex.json',{"lesson":stem,"exercises":exs})
def put_voc(stem,idn,title,theme,words):
    try: idn=rd(f'vocabulary/b2/{stem}-voc.json')['id']
    except Exception: pass
    wr(f'vocabulary/b2/{stem}-voc.json',{"id":idn,"lesson":stem,"title":title,"theme":theme,"words":[{"lemma":l,"translation":t,"pos":p} for l,t,p in words]})
def put_gr(stem,title,secs):
    d=rd(f'grammar/b2/{stem}-a-gr.json'); d['title']=title; d['sections']=secs; wr(f'grammar/b2/{stem}-a-gr.json',d)
def put_lesson(stem,title,goal,grammar,items,checklist=None):
    d=rd(f'lessons/b2/{stem}.json'); d['title']=title; d['goal']=goal; d['grammar']=grammar
    for s in d['sections']:
        if s['type']=='goal': s['items']=items
        if s['type']=='checklist' and checklist: s['items']=checklist
    wr(f'lessons/b2/{stem}.json',d)
def put_story(stem,title,summary,paras,qs):
    d=rd(f'stories/world/b2/{stem}.json'); d['title']=title; d['summary']=summary; d['characters']=[]
    d['paragraphs']=[{"type":"narration","text":t} for t in paras]
    d['narration']={"pedagogical":{"comprehensionQuestions":[{"question":q,"options":o,"correctIndex":0,"explanation":e} for q,o,e in qs]}}
    wr(f'stories/world/b2/{stem}.json',d)
def T(c,title=None):
    d={"type":"text"}
    if title: d["title"]=title
    d["content"]=c; return d
def TB(title,rows): return {"type":"table","title":title,"rows":rows}
def EX(title,items): return {"type":"examples","title":title,"items":[{"spanish":a,"english":b} for a,b in items]}
def TIP(c): return {"type":"tip","content":c}
def wordcount(paras): return sum(len(p.split()) for p in paras)
