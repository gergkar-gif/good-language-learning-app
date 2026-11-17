import json, os, glob
ROOT='/home/user/parlour-read-a/content/hu/'
def load(p):
    return json.load(open(ROOT+p,encoding='utf8'))
def save(p,d):
    s=json.dumps(d,ensure_ascii=False,indent=2)
    open(ROOT+p,'w',encoding='utf8').write(s)
import random, zlib
def _shuf(id,opts):
    idx=list(range(len(opts)))
    r=random.Random(zlib.crc32(id.encode()))
    r.shuffle(idx)
    return idx
def mc(id,cat,stage,q,opts,correct,teaches,ds=None):
    """opts: correct option FIRST (correct arg ignored); shuffled deterministically"""
    idx=_shuf(id,opts)
    new=[opts[i] for i in idx]
    d={"id":id,"type":"multiple-choice","category":cat,"stage":stage,"question":q,"options":new,"correct":idx.index(0),"teaches":[teaches]}
    if ds: d["distractor_skills"]={str(idx.index(k)):v for k,v in sorted(ds.items())}
    return d
def fb(id,cat,stage,sent,eng,teaches,ans,hint=None):
    d={"id":id,"type":"fill-blank","category":cat,"stage":stage,"sentence":sent}
    if hint: d["hint"]=hint
    d["english"]=eng; d["teaches"]=[teaches]
    if isinstance(ans,list): d["answers"]=ans
    else: d["answer"]=ans
    return d
def mt(id,stage,pairs,teaches):
    return {"id":id,"type":"matching","category":"vocabulary","stage":stage,"pairs":[list(p) for p in pairs],"teaches":[teaches]}
def sb(id,cat,stage,tiles,eng,teaches):
    return {"id":id,"type":"sentence-builder","category":cat,"stage":stage,"tiles":tiles,"solution":list(tiles),"english":eng,"teaches":[teaches]}
def dl(id,cat,stage,turns,opts,correct,teaches):
    idx=_shuf(id,opts)
    new=[opts[i] for i in idx]
    return {"id":id,"type":"dialogue-complete","category":"dialogue","stage":stage,"prompt":[{"speaker":s,"text":t} for s,t in turns],"options":new,"correct":idx.index(0),"teaches":[teaches]}
def sw(id,stage,prompt,answer,teaches):
    return {"id":id,"type":"structured-writing","category":"writing","stage":stage,"template":[{"prompt":prompt,"answer":answer}],"teaches":[teaches]}

def build_unit(U):
    """U: dict with stem, short(unit id), unit_no, unit_title_en, vocab_slug, lessons[list], consol{}"""
    stem=U['stem']
    c1=load('curriculum/units/c1.json')
    for u in c1:
        if u['id']==U['uid']: u['title']=U['unit_title_en']
    save('curriculum/units/c1.json',c1)
    for i,L in enumerate(U['lessons'],1):
        n=f'{i:02d}'
        base=f'c1-{stem}-{n}'
        # story
        sp=[f for f in glob.glob(ROOT+f'stories/world/c1/{base}-*.json')]
        assert len(sp)==1,sp
        sp=os.path.relpath(sp[0],ROOT)
        s=load(sp)
        s['title']=L['story_title']; s['summary']=L['summary']
        s['grammar']=[U['vocab_slug']]
        s['vocabularyTopics']=[U['unit_title_en'],L['title_en']]
        s['paragraphs']=[{"type":"narration","text":L['text']}]
        save(sp,s)
        # grammar
        g=load(f'grammar/c1/{base}-a-gr.json')
        g['id']=f'grammar.c1.{stem}.{n}.'+L['gid']
        g['title']=L['gtitle']
        g['sections']=[
          {"type":"text","title":"How it works","content":L['how']},
          {"type":"text","title":"Example","content":"Example: *"+L['example']+"*"},
          {"type":"table","title":"Patterns in Context","rows":[list(r) for r in L['rows']]}]
        save(f'grammar/c1/{base}-a-gr.json',g)
        # vocab
        v=load(f'vocabulary/c1/{base}-voc.json')
        v['title']='C1 Vocabulary — '+L['title_en']; v['theme']=U['unit_title_en']
        v['words']=[{"lemma":a,"translation":b,"pos":c} for a,b,c in L['vocab']]
        save(f'vocabulary/c1/{base}-voc.json',v)
        # exercises
        e=load(f'exercises/c1/{base}-ex.json')
        e['exercises']=L['ex']
        save(f'exercises/c1/{base}-ex.json',e)
        # lesson
        l=load(f'lessons/c1/{base}.json')
        l['title']=L['title_en']; l['grammar']=L['gtitle'] if False else L['grammar_line']
        l['goal']=L['goals']
        for sec in l['sections']:
            t=sec['type']
            if t=='intro':
                sec['title']=f"Unit {U['unit_no']}: {U['unit_title_en']}"; sec['body']=U['intro']
            elif t=='goal': sec['items']=L['goals']
            elif t=='grammar': sec['title']=L['gtitle']
            elif t=='story': sec['title']='Story: '+L['story_title']
            elif t=='checklist': sec['items']=L['goals']
        save(f'lessons/c1/{base}.json',l)
    # consolidation
    C=U['consol']
    base=f'c1-{stem}-consolidation'
    e=load(f'exercises/c1/{base}-ex.json'); e['exercises']=C['ex']; save(f'exercises/c1/{base}-ex.json',e)
    l=load(f'lessons/c1/{base}.json')
    l['title']=f"Unit {U['unit_no']} Consolidation: {U['unit_title_en']}"; l['grammar']=C['grammar_line']; l['goal']=C['goals']
    for sec in l['sections']:
        if sec['type'] in ('goal','checklist'): sec['items']=C['goals']
    save(f'lessons/c1/{base}.json',l)
