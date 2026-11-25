import json,re,os
R='/home/user/parlour-read-b/content/es-latam/'
def wj(path,obj):
    with open(path,'w',encoding='utf-8') as f:
        json.dump(obj,f,ensure_ascii=False,indent=2)
def rj(path): return json.load(open(path,encoding='utf-8'))

def mc(i,q,opts,cat='grammar',teaches=None,ds=None):
    e={'id':i,'type':'multiple-choice','category':cat,'question':q,'options':opts,'correct':0}
    if teaches: e['teaches']=[teaches]
    if ds: e['distractor_skills']=ds
    return e
def match(i,pairs,teaches):
    return {'id':i,'type':'matching','category':'vocabulary','pairs':[list(p) for p in pairs],'teaches':[teaches]}
def fill(i,sent,ans,eng,teaches,hint=None,answers=None,cat='grammar'):
    e={'id':i,'type':'fill-blank','category':cat,'sentence':sent}
    if hint: e['hint']=hint
    if answers: e['answers']=answers
    else: e['answer']=ans
    e['english']=eng; e['teaches']=[teaches]; return e
def build(i,sentence,eng,teaches,cat='grammar'):
    t=sentence.split()
    return {'id':i,'type':'sentence-builder','category':cat,'tiles':t,'solution':t,'english':eng,'teaches':[teaches]}
def dlg(i,meg,reply_line,after,opts,teaches,first='Meg',second='Carlos'):
    return {'id':i,'type':'dialogue-complete','category':'dialogue','prompt':[{'speaker':first,'text':meg},{'speaker':second,'text':'_____'},{'speaker':first,'text':after}],'options':opts,'correct':0,'teaches':[teaches]}
def dict_(i,s,eng,teaches):
    return {'id':i,'type':'dictation','category':'listening','sentence':s,'english':eng,'teaches':[teaches]}

def write_ex(stem,exs):
    wj(R+f'exercises/b2/{stem}-ex.json',{'lesson':stem,'exercises':exs})
def write_voc(stem,vid,title,theme,words):
    vid=rj(R+f'vocabulary/b2/{stem}-voc.json')['id']
    wj(R+f'vocabulary/b2/{stem}-voc.json',{'id':vid,'lesson':stem,'title':title,'theme':theme,'words':[{'lemma':a,'translation':b,'pos':c} for a,b,c in words]})
def write_gr(stem,gid,title,secs):
    gid=rj(R+f'grammar/b2/{stem}-a-gr.json')['id']
    wj(R+f'grammar/b2/{stem}-a-gr.json',{'id':gid,'title':title,'sections':secs})
def T(content,title=None):
    d={'type':'text'}
    if title: d['title']=title
    d['content']=content; return d
def TB(title,rows): return {'type':'table','title':title,'rows':[list(r) for r in rows]}
def EX(items,title='In context'): return {'type':'examples','title':title,'items':[{'spanish':a,'english':b} for a,b in items]}
def TIP(c): return {'type':'tip','content':c}

def lesson(stem,title,goal,grammar,intro,goals,checklist=None):
    p=R+f'lessons/b2/{stem}.json'; d=rj(p)
    d['title']=title; d['goal']=goal; d['grammar']=grammar
    for s in d['sections']:
        if s['type']=='intro': s['title']=title; s['body']=intro
        if s['type']=='goal': s['items']=goals
        if s['type']=='checklist' and checklist: s['items']=checklist
    wj(p,d)

def story(stem,title,summary,paras,qs):
    p=R+f'stories/world/b2/{stem}.json'; d=rj(p)
    d['title']=title; d['summary']=summary
    d['paragraphs']=[{'type':'narration','text':t} for t in paras]
    d['narration']={'pedagogical':{'comprehensionQuestions':[{'question':q,'options':o,'correctIndex':0,'explanation':x} for q,o,x in qs]}}
    wj(p,d)
    return sum(len(t.split()) for t in paras)
