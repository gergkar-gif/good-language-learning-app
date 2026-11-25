import json,os,re
ROOT='/home/user/parlour-read-a'
C=ROOT+'/content/es-latam'
def wj(path,d):
    with open(path,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n' if False else '')
def rj(p): return json.load(open(p,encoding='utf-8'))

class Ex:
    def __init__(s,stem): s.stem=stem; s.items=[]
    def _id(s): return f"{s.stem}.ex{len(s.items)+1:02d}"
    def mc(s,q,right,wrongs,pos,teaches=None,cat='grammar',ds=None):
        opts=list(wrongs); opts.insert(pos,right)
        e={'id':s._id(),'type':'multiple-choice','category':cat,'question':q,'options':opts,'correct':pos}
        if teaches: e['teaches']=[teaches]
        if ds:
            e['distractor_skills']={str(opts.index(k)):v for k,v in ds.items()}
        s.items.append(e)
    def read(s,q,right,wrongs,pos):
        s.mc(q,right,wrongs,pos,None,'reading')
    def fb(s,sent,ans,eng,teaches,cat='grammar',hint=None,answers=None):
        e={'id':s._id(),'type':'fill-blank','category':cat,'sentence':sent,'answer':ans,'english':eng}
        if answers: e['answers']=answers
        if hint: e['hint']=hint
        e['teaches']=[teaches]; s.items.append(e)
    def mt(s,pairs,teaches):
        s.items.append({'id':s._id(),'type':'matching','category':'vocabulary','pairs':[list(p) for p in pairs],'teaches':[teaches]})
    def sb(s,sent,eng,teaches,cat='grammar'):
        t=sent.split()
        s.items.append({'id':s._id(),'type':'sentence-builder','category':cat,'tiles':t,'solution':list(t),'english':eng,'teaches':[teaches]})
    def write(s):
        wj(f"{C}/exercises/b2/{s.stem}-ex.json",{'lesson':s.stem,'exercises':s.items})
        return [e['id'] for e in s.items]

def grammar(stem,gid,title,recap,table_title,rows,ex_title,examples,tip,recap_title="What you already know",extra=None):
    secs=[{'type':'text','title':recap_title,'content':recap},
          {'type':'table','title':table_title,'rows':[list(r) for r in rows]},
          {'type':'examples','title':ex_title,'items':[{'spanish':a,'english':b} for a,b in examples]}]
    if extra: secs+=extra
    secs.append({'type':'tip','content':tip})
    wj(f"{C}/grammar/b2/{stem}-a-gr.json",{'id':gid,'title':title,'sections':secs})

def vocab(stem,title,words):
    old=rj(f"{C}/vocabulary/b2/{stem}-voc.json")
    old['title']=title
    old['words']=[{'lemma':l,'translation':t,'pos':p} for l,t,p in words]
    wj(f"{C}/vocabulary/b2/{stem}-voc.json",old)

def story(stem,title,summary,paras,qs,lessonno=None):
    p=f"{C}/stories/world/b2/{stem}.json"
    d=rj(p)
    d['title']=title; d['summary']=summary; d['characters']=[]
    d['paragraphs']=[{'type':'narration','text':t} for t in paras]
    d['narration']['pedagogical']['comprehensionQuestions']=[
        {'question':q,'options':o,'correctIndex':i,'explanation':ex} for q,o,i,ex in qs]
    wj(p,d)
    return sum(len(t.split()) for t in paras)

def lesson(stem,title,goal,grammar_str,ids):
    p=f"{C}/lessons/b2/{stem}.json"
    d=rj(p)
    new={}
    for k,v in d.items():
        new[k]=v
        if k=='title':
            new['goal']=goal; new['grammar']=grammar_str
    new['title']=title; new['goal']=goal; new['grammar']=grammar_str
    for s in new['sections']:
        if s['type']=='exercise-group': s['exerciseRefs']=ids
    wj(p,new)

def consolidation(stem,title,goal,grammar_str,goals,checklist,ids):
    p=f"{C}/lessons/b2/{stem}.json"
    d=rj(p); new={}
    for k,v in d.items():
        new[k]=v
        if k=='level': new['goal']=goal; new['grammar']=grammar_str
    new['title']=title
    for s in new['sections']:
        if s['type']=='goal': s['items']=goals
        if s['type']=='checklist': s['items']=checklist; s.setdefault('title','Can you do this?')
        if s['type']=='exercise-group': s['exerciseRefs']=ids
    wj(p,new)

def challenges(path,d):
    wj(path,d)
def chal(title,scenario,prompt,cues,target,english,canDo):
    return {'tier':'tier1','level':'B2','title':'Communicative Challenge: '+title,'scenario':scenario,'prompt':prompt,'cues':cues,'target':target,'english':english,'canDo':canDo}

def consolidation2(stem,title,goal,grammar_str,ids):
    p=f"{C}/lessons/b2/{stem}.json"
    d=rj(p); new={}
    for k,v in d.items():
        new[k]=v
        if k=='level': new['goal']=goal; new['grammar']=grammar_str
    new['title']=title
    for s in new['sections']:
        if s['type']=='exercise-group': s['exerciseRefs']=ids
    wj(p,new)
