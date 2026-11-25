import json, os
R='/home/user/parlour-read-a/content/es-latam/'
def jl(p):
    return json.load(open(R+p,encoding='utf8'))
def jw(p,d):
    with open(R+p,'w',encoding='utf8') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')

def matching(i,pairs,skill): return dict(id=i,type='matching',category='vocabulary',pairs=pairs,teaches=[skill])
def fill(i,sent,ans,eng,skill,cat='grammar',hint=None,answers=None):
    d=dict(id=i,type='fill-blank',category=cat,sentence=sent,answer=ans,english=eng,teaches=[skill])
    if hint: d['hint']=hint
    if answers: d['answers']=answers; del d['answer']
    return d
def mc(i,q,opts,correct,skill,cat='grammar',ds=None):
    d=dict(id=i,type='multiple-choice',category=cat,question=q,options=opts,correct=correct,teaches=[skill])
    if ds: d['distractor_skills']=ds
    return d
def build(i,sol,eng,skill):
    return dict(id=i,type='sentence-builder',category='grammar',tiles=list(sol),solution=list(sol),english=eng,teaches=[skill])
def dlg(i,lines,opts,correct,skill):
    return dict(id=i,type='dialogue-complete',category='dialogue',prompt=[dict(speaker=s,text=t) for s,t in lines],options=opts,correct=correct,teaches=[skill])
def dic(i,sent,eng,skill): return dict(id=i,type='dictation',category='listening',sentence=sent,english=eng,teaches=[skill])

def story(stem,title,summary,paras,qs,num):
    return dict(id=stem,title=title,level='B2',lesson=num,type='world',estimatedMinutes=8,summary=summary,characters=[],
      paragraphs=[dict(type='narration',text=t) for t in paras],
      narration=dict(pedagogical=dict(comprehensionQuestions=[dict(question=q,options=o,correctIndex=c,explanation=e) for q,o,c,e in qs])))

def gram(stem,title,know,tabletitle,rows,examples,tip,gid=None):
    old=jl(f'grammar/b2/{stem}-a-gr.json')
    return dict(id=old['id'],title=title,sections=[
      dict(type='text',title='What you already know',content=know),
      dict(type='table',title=tabletitle,rows=[list(r) for r in rows]),
      dict(type='examples',title='In context',items=[dict(spanish=s,english=e) for s,e in examples]),
      dict(type='tip',content=tip)])

def vocab(stem,title,words):
    old=jl(f'vocabulary/b2/{stem}-voc.json')
    old['title']=title
    old['words']=[dict(lemma=l,translation=t,pos=p) for l,t,p in words]
    return old

def write_lesson(stem,title,goal,gramtxt,goals):
    p=f'lessons/b2/{stem}.json'
    d=jl(p); d['title']=title; d['goal']=goal
    if gramtxt: d['grammar']=gramtxt
    for s in d['sections']:
        if s['type']=='goal' and goals: s['items']=goals
    jw(p,d)

def write_all(stem,num,L):
    write_lesson(stem,L['title'],L['goal'],L['gramtxt'],L['goals'])
    jw(f'stories/world/b2/{stem}.json',story(stem,L['stitle'],L['summary'],L['paras'],L['qs'],num))
    jw(f'grammar/b2/{stem}-a-gr.json',gram(stem,L['gtitle'],L['know'],L['tabletitle'],L['rows'],L['examples'],L['tip']))
    jw(f'vocabulary/b2/{stem}-voc.json',vocab(stem,L['vtitle'],L['words']))
    jw(f'exercises/b2/{stem}-ex.json',dict(lesson=stem,exercises=L['items']))
