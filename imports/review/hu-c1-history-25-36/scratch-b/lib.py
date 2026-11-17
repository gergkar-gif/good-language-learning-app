import json, re, os
R="/home/user/parlour-read-b/"
def rj(p): return json.load(open(R+p,encoding="utf-8"))
def wj(p,d):
    p=p[len(R):] if p.startswith(R) else p
    open(R+p,"w",encoding="utf-8").write(json.dumps(d,ensure_ascii=False,indent=2)+"\n")
def mc(id,cat,stage,q,opts,tag,pos=0):
    """opts[0] is correct; placed at index pos"""
    o=list(opts[1:]); o.insert(pos,opts[0])
    return {"id":id,"type":"multiple-choice","category":cat,"stage":stage,"question":q,"options":o,"correct":pos,"teaches":[tag]}
def fb(id,stage,sentence,ans,english,tag,hint=None,cat="grammar"):
    d={"id":id,"type":"fill-blank","category":cat,"stage":stage,"sentence":sentence}
    if hint: d["hint"]=hint
    if isinstance(ans,list): d["answers"]=ans
    else: d["answer"]=ans
    d["english"]=english; d["teaches"]=[tag]; return d
def match(id,stage,pairs,tag):
    return {"id":id,"type":"matching","category":"vocabulary","stage":stage,"pairs":[list(p) for p in pairs],"teaches":[tag]}
def sb(id,stage,sent,english,tag,cat="grammar"):
    t=sent.split()
    return {"id":id,"type":"sentence-builder","category":cat,"stage":stage,"tiles":t,"solution":t,"english":english,"teaches":[tag]}
def dlg(id,turns,opts,tag,pos=0,cat="dialogue"):
    o=list(opts[1:]); o.insert(pos,opts[0])
    return {"id":id,"type":"dialogue-complete","category":cat,"stage":"dialogue","prompt":[{"speaker":s,"text":t} for s,t in turns],"options":o,"correct":pos,"teaches":[tag]}
def wr(id,stage,prompt,answer,tag):
    return {"id":id,"type":"structured-writing","category":"writing","stage":stage,"template":[{"prompt":prompt,"answer":answer}],"teaches":[tag]}

def apply_unit(S):
    """S: dict with stem, unit_title, intro, lessons{ '01':{...}, 'consolidation':{...}}"""
    st=S["stem"]
    for n,L in S["lessons"].items():
        lp=f"content/hu/lessons/c1/{st}-{n}.json"; les=rj(lp)
        les["title"]=L["title"]
        if "grammar_title" in L: les["grammar"]=L["grammar_title"]
        les["goal"]=L["goal"]
        for s in les["sections"]:
            t=s["type"]
            if t=="intro":
                s["title"]=L["intro_title"]; s["body"]=L["intro"]
            elif t=="goal": s["items"]=L["goal"]
            elif t=="checklist": s["items"]=L["goal"]
            elif t=="grammar": s["title"]=L["grammar_title"]
            elif t=="story": s["title"]="Story: "+L["story"]["title"]
        wj(lp,les)
        ep=f"content/hu/exercises/c1/{st}-{n}-ex.json"; ex=rj(ep)
        old=[e["id"] for e in ex["exercises"]]; new=[e["id"] for e in L["items"]]
        assert old==new,(n,old,new)
        ex["exercises"]=L["items"]; wj(ep,ex)
        if n!="consolidation":
            gp=f"content/hu/grammar/c1/{st}-{n}-a-gr.json"; g=rj(gp)
            g["title"]=L["grammar_title"]; g["sections"]=L["grammar"]; wj(gp,g)
            vp=f"content/hu/vocabulary/c1/{st}-{n}-voc.json"; v=rj(vp)
            v["title"]="Vocabulary: "+L["title"]; v["theme"]=S["unit_title"]
            v["words"]=[{"lemma":a,"translation":b,"pos":c} for a,b,c in L["vocab"]]; wj(vp,v)
            sp=f"content/hu/stories/world/c1/{L['story']['file']}.json"; s=rj(sp)
            s["title"]=L["story"]["title"]; s["summary"]=L["story"]["summary"]
            s["grammar"]=[L["story"]["skill"]]
            s["vocabularyTopics"]=[S["unit_title"],L["title"]]
            s["paragraphs"]=[{"type":"narration","text":t} for t in L["story"]["text"]]
            wj(sp,s)
    # unit title
    up="content/hu/curriculum/units/c1.json"; u=rj(up)
    us=u["units"] if isinstance(u,dict) else u
    for x in us:
        if x["id"]==S["unit_id"]: x["title"]=S["unit_title"]
    wj(up,u)
    # challenges
    ch={}
    for n,L in S["lessons"].items():
        c=L["challenge"]; c=dict(c); c["canDo"]=L["goal"][0]
        ch[f"{st}-{n}"]=dict([("tier","tier1"),("level","C1")]+list(c.items()))
    wj(S["chfile"],ch)
def words(s): return len(s.split())
