import sys,json
sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
def chk(id,opts,teaches,ds=None,q="Melyik mondat helyes?"):
    return mc(id,"check","grammar",q,opts,teaches,ds)
def run(c):
    for n in range(1,6):
        stem=c['S'][n-1]; sp=c['LESSONS'][n]
        if n==1: sp=dict(sp,intro=c['INTRO'])
        apply_lesson(sp,stem,n,c['unit'])
        g=c['GR'][n]; gram(g[0],g[1],g[2],g[3],g[4])
        apply_vocab(stem,c['VOC'][n][0],c['TH'],c['VOC'][n][1])
        apply_ex(stem,c['EXS'](n))
        apply_story(c['STORY'][n-1],sp['storytitle'],c['V'],[c['TH'],sp['title']],c['SUMMARY'][n-1],[c['TEXT'][n-1]])
    apply_lesson(dict(c['CONS']),c['prefix']+'-consolidation',6,c['unit'])
    apply_ex(c['prefix']+'-consolidation',c['CEX']())
def counts(c):
    for i,t in enumerate(c['TEXT']): print(i+1,wc(t))
def challenges(c,items,out):
    d={}
    for k,(title,scn,prompt,cues,target,eng) in items.items():
        stem=c['prefix']+'-'+k
        can=(c['CONS']['goals'][0] if k=='consolidation' else c['LESSONS'][int(k)]['goals'][0])
        d[stem]={"tier":"tier1","level":"C1","title":"Communicative Challenge: "+title,"scenario":scn,"prompt":prompt,"cues":cues,"target":target,"english":eng,"canDo":can}
    open(out,'w',encoding='utf-8').write(json.dumps(d,indent=2,ensure_ascii=False)+"\n")
