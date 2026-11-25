import json,os
R='/home/user/parlour-read-a/content/es-latam/'
def rj(p): return json.load(open(R+p))
def wj(p,d):
    with open(R+p,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')
def lesson_update(stem,title,goal,gram,items,intro=None,extra_refs=None):
    p=f'lessons/b2/{stem}.json'; l=rj(p)
    l['title']=title; l['goal']=goal; l['grammar']=gram
    for s in l['sections']:
        if s['type'] in('goal','checklist'): s['items']=items
        if s['type']=='intro' and intro: s['title']=intro[0]; s['body']=intro[1]
    wj(p,l)
def story_update(stem,title,summary,paras):
    p=f'stories/world/b2/{stem}.json'; s=rj(p)
    s['title']=title; s['summary']=summary
    s['paragraphs']=[{'type':'narration','text':t} for t in paras]
    wj(p,s)
def vocab_update(stem,title,words):
    p=f'vocabulary/b2/{stem}-voc.json'; v=rj(p)
    v['title']=title; v['words']=[{'lemma':a,'translation':b,'pos':c} for a,b,c in words]
    wj(p,v)
def grammar_update(stem,title,sections):
    p=f'grammar/b2/{stem}-a-gr.json'; g=rj(p); g['title']=title; g['sections']=sections; wj(p,g)
def T(title,content): return {'type':'text','title':title,'content':content}
def TAB(title,rows): return {'type':'table','title':title,'rows':rows}
def EX(title,pairs): return {'type':'examples','title':title,'items':[{'spanish':a,'english':b} for a,b in pairs]}
def TIP(c): return {'type':'tip','content':c}
def ex_write(stem,items):
    wj(f'exercises/b2/{stem}-ex.json',{'lesson':stem,'exercises':items})
V='b2-mexico-central-vocab'
def match(i,pairs): return {'id':i,'type':'matching','category':'vocabulary','pairs':[list(p) for p in pairs],'teaches':[V]}
def mc_read(i,q,opts): return {'id':i,'type':'multiple-choice','category':'reading','question':q,'options':opts,'correct':0}
def mc(i,q,opts,skill,ds=None):
    d={'id':i,'type':'multiple-choice','category':'grammar','question':q,'options':opts,'correct':0,'teaches':[skill]}
    if ds: d['distractor_skills']=ds
    return d
def fill(i,sent,ans,eng,skill,hint=None,answers=None,cat='grammar'):
    d={'id':i,'type':'fill-blank','category':cat,'sentence':sent}
    if hint: d['hint']=hint
    if answers: d['answers']=answers
    else: d['answer']=ans
    d['english']=eng; d['teaches']=[skill]; return d
def build(i,sol,eng,skill):
    return {'id':i,'type':'sentence-builder','category':'grammar','tiles':sol,'solution':sol,'english':eng,'teaches':[skill]}
def listen(i,s,opts,skill): return {'id':i,'type':'listening-choice','category':'listening','sentence':s,'options':opts,'correct':0,'teaches':[skill]}
def dial(i,prompt,opts,skill,ds=None):
    d={'id':i,'type':'dialogue-complete','category':'dialogue','prompt':[{'speaker':a,'text':b} for a,b in prompt],'options':opts,'correct':0,'teaches':[skill]}
    if ds:d['distractor_skills']=ds
    return d
def write(i,tpl,skill): return {'id':i,'type':'structured-writing','category':'writing','template':[{'prompt':a,'answer':b} for a,b in tpl],'teaches':[skill]}
