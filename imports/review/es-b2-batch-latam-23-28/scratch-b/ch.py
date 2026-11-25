import json,sys
def C(title,scenario,prompt,cues,target,english,canDo):
    return {"tier":"tier1","level":"B2","title":"Communicative Challenge: "+title,"scenario":scenario,"prompt":prompt,"cues":cues,"target":target,"english":english,"canDo":canDo}
def dump(path,d): open(path,'w').write(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
