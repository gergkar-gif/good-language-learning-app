import json,os
R='/home/user/parlour-read-b/content/es-latam/'
def rd(p): return json.load(open(R+p))
def wr(p,d):
    with open(R+p,'w') as f: json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')
def mc(id,q,opts,cor,teach,cat='grammar',ds=None):
    d={'id':id,'type':'multiple-choice','category':cat,'question':q,'options':opts,'correct':cor}
    if teach: d['teaches']=[teach]
    if ds: d['distractor_skills']=ds
    return d
def fb(id,s,a,en,teach,cat='grammar',hint=None,answers=None):
    d={'id':id,'type':'fill-blank','category':cat,'sentence':s,'english':en}
    if answers: d['answers']=answers
    else: d['answer']=a
    if hint: d['hint']=hint
    d['teaches']=[teach]; return d
def sb(id,sent,en,teach,cat='grammar'):
    t=sent.split()
    return {'id':id,'type':'sentence-builder','category':cat,'tiles':t,'solution':t,'english':en,'teaches':[teach]}
def mt(id,pairs,teach):
    return {'id':id,'type':'matching','category':'vocabulary','pairs':pairs,'teaches':[teach]}
def dc(id,prompt,opts,cor,teach,cat='dialogue'):
    return {'id':id,'type':'dialogue-complete','category':cat,'prompt':[{'speaker':s,'text':t} for s,t in prompt],'options':opts,'correct':cor,'teaches':[teach]}
def rdg(id,q,opts,cor):
    return {'id':id,'type':'multiple-choice','category':'reading','question':q,'options':opts,'correct':cor}
def story(stem,title,summary,paras,qs):
    d=rd(f'stories/world/b2/{stem}.json')
    d['title']=title; d['summary']=summary; d['characters']=[]
    d['paragraphs']=[{'type':'narration','text':t} for t in paras]
    d['narration']={'pedagogical':{'comprehensionQuestions':[{'question':q,'options':o,'correctIndex':0,'explanation':e} for q,o,e in qs]}}
    wr(f'stories/world/b2/{stem}.json',d)
def grammar(stem,gid,title,recap,rows,rtitle,exs,tip,extra=None):
    secs=[{'type':'text','title':'What you already know','content':recap},{'type':'table','title':rtitle,'rows':rows},{'type':'examples','title':'In context','items':[{'spanish':a,'english':b} for a,b in exs]},{'type':'tip','content':tip}]
    wr(f'grammar/b2/{stem}-a-gr.json',{'id':gid,'title':title,'sections':secs})
def vocab(stem,title,words):
    d=rd(f'vocabulary/b2/{stem}-voc.json'); d['title']=title
    d['words']=[{'lemma':l,'translation':t,'pos':p} for l,t,p in words]; wr(f'vocabulary/b2/{stem}-voc.json',d)
def exfile(stem,items):
    wr(f'exercises/b2/{stem}-ex.json',{'lesson':stem,'exercises':items})
def lesson(stem,title,ids,dlg=None):
    d=rd(f'lessons/b2/{stem}.json'); d['title']=title
    secs=[s for s in d['sections'] if s['type']!='exercise-group']
    main=[i for i in ids if i not in (dlg or [])]
    secs.append({'type':'exercise-group','title':'Practice','ref':f'exercises/b2/{stem}-ex.json','exerciseRefs':[f'{stem}.{i}' for i in main]})
    if dlg: secs.append({'type':'exercise-group','title':'Dialogue','ref':f'exercises/b2/{stem}-ex.json','exerciseRefs':[f'{stem}.{i}' for i in dlg]})
    d['sections']=secs; wr(f'lessons/b2/{stem}.json',d)
