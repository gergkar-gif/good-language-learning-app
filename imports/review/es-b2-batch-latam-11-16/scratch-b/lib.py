import json, os, re
W='/home/user/parlour-read-b/content/es-latam/'
def rj(p): return json.load(open(W+p))
def wj(p,o):
    with open(W+p,'w') as f:
        json.dump(o,f,indent=2,ensure_ascii=False); f.write('\n')
def match(i,pairs,vocab): return dict(id=i,type='matching',category='vocabulary',pairs=[list(p) for p in pairs],teaches=[vocab])
def mc(i,q,opts,teaches,ds=None,cat='grammar'):
    e=dict(id=i,type='multiple-choice',category=cat,question=q,options=opts,correct=0)
    if teaches: e['teaches']=[teaches]
    if ds: e['distractor_skills']={str(k):v for k,v in ds.items()}
    return e
def reading(i,q,opts): return mc(i,q,opts,None,cat='reading')
def fb(i,sent,ans,eng,teaches,hint=None,cat='grammar',answers=None):
    e=dict(id=i,type='fill-blank',category=cat,sentence=sent)
    if hint: e['hint']=hint
    if answers: e['answers']=answers
    else: e['answer']=ans
    e['english']=eng; e['teaches']=[teaches]; return e
def sb(i,sent,eng,teaches,cat='grammar'):
    t=sent.split(' ')
    return dict(id=i,type='sentence-builder',category=cat,tiles=t,solution=t,english=eng,teaches=[teaches])
def dlg(i,lines,opts,teaches,ds=None,cat='dialogue'):
    pr=[dict(speaker=s,text=t) for s,t in lines]
    e=dict(id=i,type='dialogue-complete',category=cat,prompt=pr,options=opts,correct=0,teaches=[teaches])
    if ds: e['distractor_skills']={str(k):v for k,v in ds.items()}
    return e
def dic(i,sent,eng,teaches): return dict(id=i,type='dictation',category='listening',sentence=sent,english=eng,teaches=[teaches])
def sw(i,tpl,teaches): return dict(id=i,type='structured-writing',category='writing',template=[dict(prompt=p,answer=a) for p,a in tpl],teaches=[teaches])
def screen(gid,title,know,table_title,rows,examples,tip,extra=None):
    secs=[dict(type='text',title='What you already know',content=know),dict(type='table',title=table_title,rows=[list(r) for r in rows])]
    if extra: secs.append(dict(type='text',title=extra[0],content=extra[1]))
    secs+= [dict(type='examples',title='In context',items=[dict(spanish=s,english=e) for s,e in examples]),dict(type='tip',content=tip)]
    return dict(id=gid,title=title,sections=secs)
def build_unit(spec):
    pre=spec['pre']; uid=spec['uid']
    for n,L in spec['lessons'].items():
        stem=f'{pre}-{n}'
        lp=f'lessons/b2/{stem}.json'; l=rj(lp)
        l['title']=L['title']; l['goal']=L['goal']
        if 'grammar_label' in L: l['grammar']=L['grammar_label']
        for s in l['sections']:
            if s['type']=='goal': s['items']=L['goal_items']
            if s['type']=='checklist': s['items']=L.get('checklist_items',L['goal_items'])
        # exercise refs
        exs=L['exercises']
        ids=[e['id'] for e in exs]
        if n=='consolidation':
            for s in l['sections']:
                if s['type']=='exercise-group': s['exerciseRefs']=ids
        else:
            for s in l['sections']:
                if s['type']=='exercise-group' and s.get('title')=='Practice':
                    s['exerciseRefs']=[i for i in ids if i[-4:] in('ex01','ex02','ex03','ex04','ex07')]
        wj(lp,l)
        wj(f'exercises/b2/{stem}-ex.json',dict(lesson=stem,exercises=exs))
        if 'screen' in L:
            g=L['screen']; p=f'grammar/b2/{stem}-a-gr.json'
            old=rj(p); g['id']=old['id']; wj(p,g)
        if 'vocab' in L:
            vp=f'vocabulary/b2/{stem}-voc.json'; v=rj(vp)
            v['title']=L['vocab_title']; v['theme']=L['vocab_theme']
            v['words']=[dict(lemma=a,translation=b,pos=c) for a,b,c in L['vocab']]
            wj(vp,v)
        if 'story' in L and n!='consolidation':
            sp=f'stories/world/b2/{stem}.json'; s=rj(sp); S=L['story']
            s['title']=S['title']; s['summary']=S['summary']; s['characters']=[]
            s['paragraphs']=[dict(type='narration',text=t) for t in S['paras']]
            s['narration']['pedagogical']['comprehensionQuestions']=[dict(question=q,options=o,correctIndex=0,explanation=ex) for q,o,ex in S['qs']]
            wj(sp,s)
