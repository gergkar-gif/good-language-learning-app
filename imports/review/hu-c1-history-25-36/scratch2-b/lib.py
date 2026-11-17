import json, os
R='/home/user/parlour-read-b/content/hu/'
def load(p): return json.load(open(R+p,encoding='utf-8'))
def save(p,d):
    open(R+p,'w',encoding='utf-8').write(json.dumps(d,indent=2,ensure_ascii=False)+"\n")

def mc(id,stage,cat,q,opts,teaches,ds=None):
    d={"id":id,"type":"multiple-choice","category":cat,"stage":stage,"question":q,"options":opts,"correct":0,"teaches":[teaches]}
    if ds: d["distractor_skills"]=ds
    return d
def fb(id,stage,cat,sent,eng,teaches,ans=None,answers=None,hint=None):
    d={"id":id,"type":"fill-blank","category":cat,"stage":stage,"sentence":sent}
    if hint: d["hint"]=hint
    d["english"]=eng; d["teaches"]=[teaches]
    if answers: d["answers"]=answers
    else: d["answer"]=ans
    return d
def match(id,stage,pairs,teaches):
    return {"id":id,"type":"matching","category":"vocabulary","stage":stage,"pairs":pairs,"teaches":[teaches]}
def sb(id,stage,sentence,eng,teaches):
    t=sentence.split()
    return {"id":id,"type":"sentence-builder","category":"grammar","stage":stage,"tiles":t,"solution":list(t),"english":eng,"teaches":[teaches]}
def dlg(id,turns,opts,teaches):
    return {"id":id,"type":"dialogue-complete","category":"dialogue","stage":"dialogue","prompt":[{"speaker":s,"text":t} for s,t in turns],"options":opts,"correct":0,"teaches":[teaches]}
def wr(id,stage,prompt,answer,teaches):
    return {"id":id,"type":"structured-writing","category":"writing","stage":stage,"template":[{"prompt":prompt,"answer":answer}],"teaches":[teaches]}

def gram(g,title,how,example,rows):
    d=load(g)
    d['title']=title
    d['sections']=[{"type":"text","title":"How it works","content":how},{"type":"text","title":"Example","content":"Example: *"+example+"*"},{"type":"table","title":"Patterns in Context","rows":[list(r) for r in rows]}]
    save(g,d)

def apply_lesson(spec, stem, n, unitno):
    """spec: dict with title, gram_short(top-level grammar), gram_title (section), goals, storytitle, intro (opt)"""
    p=f'lessons/c1/{stem}.json'
    d=load(p)
    d['title']=spec['title']; d['grammar']=spec['grammar']; d['goal']=spec['goals']
    for s in d['sections']:
        t=s['type']
        if t=='goal': s['items']=spec['goals']
        elif t=='checklist': s['items']=spec['goals']
        elif t=='grammar' and 'gtitle' in spec: s['title']=spec['gtitle']
        elif t=='story' and 'storytitle' in spec: s['title']='Story: '+spec['storytitle']
        elif t=='intro' and 'intro' in spec: s['title']=spec['intro'][0]; s['body']=spec['intro'][1]
    save(p,d)

def apply_vocab(stem,title,theme,words):
    p=f'vocabulary/c1/{stem}-voc.json'
    d=load(p); d['title']='C1 Vocabulary — '+title; d['theme']=theme
    d['words']=[{"lemma":l,"translation":t,"pos":pos} for l,t,pos in words]
    save(p,d)

def apply_story(path,title,grammar,topics,summary,paras):
    d=load(path)
    d['title']=title; d['grammar']=[grammar]; d['vocabularyTopics']=topics; d['summary']=summary
    d['paragraphs']=[{"type":"narration","text":t} for t in paras]
    save(path,d)

def apply_ex(stem,exs):
    p=f'exercises/c1/{stem}-ex.json'
    d=load(p); d['exercises']=exs; save(p,d)

def wc(t): return len(t.split())
