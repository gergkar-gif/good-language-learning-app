import json
def write(path, stem, U, items):
    """items: list of (title, scenario, prompt, cues, target, english) for lessons 1..5 then consolidation"""
    out={}
    goals=[L['goals'][0] for L in U['lessons']]+[U['consol']['goals'][0]]
    keys=[f"c1-{stem}-{i:02d}" for i in range(1,6)]+[f"c1-{stem}-consolidation"]
    for k,it,g in zip(keys,items,goals):
        t,sc,pr,cues,tg,en=it
        out[k]={"tier":"tier1","level":"C1","title":"Communicative Challenge: "+t,"scenario":sc,"prompt":pr,"cues":cues,"target":tg,"english":en,"canDo":g}
    open(path,'w',encoding='utf8').write(json.dumps(out,ensure_ascii=False,indent=2))
