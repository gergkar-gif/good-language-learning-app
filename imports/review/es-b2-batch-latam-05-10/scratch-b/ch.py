import json
def C(title,scn,prompt,cues,target,eng,cando):
    return {'tier':'tier1','level':'B2','title':'Communicative Challenge: '+title,'scenario':scn,'prompt':prompt,'cues':cues,'target':target,'english':eng,'canDo':cando}
def save(path,d): json.dump(d,open(path,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
