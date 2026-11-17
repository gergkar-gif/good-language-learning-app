import json, re, os
ROOT='/home/user/parlour-read-a/content/hu'
def load(p): return json.load(open(p,encoding='utf-8'))
def dump(p,d):
    with open(p,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=2); f.write('\n')

def mc(id,stage,cat,teach,q,opts,correct,ds=None):
    e={'id':id,'type':'multiple-choice','category':cat,'stage':stage,'question':q,'options':opts,'correct':correct,'teaches':[teach]}
    if ds: e['distractor_skills']={str(k):v for k,v in ds.items()}
    return e
def fb(id,stage,cat,teach,sent,english,answers,hint=None):
    e={'id':id,'type':'fill-blank','category':cat,'stage':stage,'sentence':sent}
    if hint: e['hint']=hint
    e['english']=english; e['teaches']=[teach]
    if len(answers)==1: e['answer']=answers[0]
    else: e['answers']=answers
    return e
def mt(id,stage,teach,pairs):
    return {'id':id,'type':'matching','category':'vocabulary','stage':stage,'pairs':[list(p) for p in pairs],'teaches':[teach]}
def sb(id,stage,teach,sol,english):
    toks=sol.split()
    return {'id':id,'type':'sentence-builder','category':'grammar','stage':stage,'tiles':toks,'solution':toks,'english':english,'teaches':[teach]}
def dl(id,teach,turns,opts,correct,ds=None):
    e={'id':id,'type':'dialogue-complete','category':'dialogue','stage':'dialogue','prompt':[{'speaker':s,'text':t} for s,t in turns],'options':opts,'correct':correct,'teaches':[teach]}
    if ds: e['distractor_skills']={str(k):v for k,v in ds.items()}
    return e
def sw(id,stage,teach,prompt,answer):
    return {'id':id,'type':'structured-writing','category':'writing','stage':stage,'template':[{'prompt':prompt,'answer':answer}],'teaches':[teach]}

def write_unit(U):
    """U: dict with stem,id,unit_no,title,stories(list of dicts),lessons(list of dicts)"""
    stem=U['stem']
    # unit title
    p=f'{ROOT}/curriculum/units/c1.json'
    raw=open(p,encoding='utf-8').read()
    d=json.loads(raw)
    for u in d:
        if u['id']==U['id']: u['title']=U['title']
    dump(p,d)
    for i,L in enumerate(U['lessons']):
        s=L['s']  # '01'..'consolidation'
        lp=f'{ROOT}/lessons/c1/c1-{stem}-{s}.json'
        les=load(lp)
        les['title']=L['title']
        if 'grammar_name' in L: les['grammar']=L['grammar_name']
        les['goal']=L['goals']
        for sec in les['sections']:
            t=sec['type']
            if t=='intro': sec['title']=f"Unit {U['unit_no']}: {U['title']}"; sec['body']=U['intro']
            elif t=='goal': sec['items']=L['goals']
            elif t=='checklist': sec['items']=L['goals']
            elif t=='grammar': sec['title']=L['gr']['title']
            elif t=='story':
                st=U['stories'][i]; sec['title']='Story: '+st['title']
        dump(lp,les)
        if 'gr' in L:
            gp=f'{ROOT}/grammar/c1/c1-{stem}-{s}-a-gr.json'
            g=load(gp); g['title']=L['gr']['title']; g['sections']=L['gr']['sections']
            if 'gid' in L['gr']: g['id']=L['gr']['gid']
            dump(gp,g)
            vp=f'{ROOT}/vocabulary/c1/c1-{stem}-{s}-voc.json'
            v=load(vp); v['title']='C1 Vocabulary — '+L['title']; v['theme']=U['title']; v['words']=[{'lemma':a,'translation':b,'pos':c} for a,b,c in L['vocab']]
            dump(vp,v)
        ep=f'{ROOT}/exercises/c1/c1-{stem}-{s}-ex.json'
        ex=load(ep); ex['exercises']=L['ex']; dump(ep,ex)
    for i,st in enumerate(U['stories']):
        sp=f"{ROOT}/stories/world/c1/{st['file']}.json"
        d=load(sp)
        d['title']=st['title']; d['summary']=st['summary']
        d['vocabularyTopics']=[U['title'],U['lessons'][i]['title']]
        d['paragraphs']=[{'type':'narration','text':t} for t in st['paras']]
        for k in ('questions',):
            if k in st: d[k]=st[k]
        dump(sp,d)
def wc(t): return len(t.split())
