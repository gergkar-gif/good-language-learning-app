"""Reviewer's changes to reader B's review lists (edit new/set only, never old)."""
import json,sys
B=sys.argv[1]
def load(u,k='review'): return json.load(open(f'{B}/fixes-{u}.{k}.json'))
def save(u,d,k='review'): json.dump(d,open(f'{B}/fixes-{u}.{k}.json','w'),ensure_ascii=False,indent=1)
def by_old(d,frag):
    m=[f for f in d if frag in f.get('old','')]; assert len(m)==1,(frag,len(m)); return m[0]
def by_id(d,i):
    m=[f for f in d if f.get('id')==i and 'set' in f]; assert len(m)==1,(i,len(m)); return m[0]
# urban-satire: 'szovjet megszállás' is the standard historical term; keep it
d=load('urban-satire')
by_old(d,'szovjet megszállást és rákosista elnyomást')['new']='szovjet megszállást és a Rákosi-korszak elnyomását'
by_old(d,'az 1956 utáni szovjet megszállásról szól')['new']='sok néző úgy értette, hogy a darab a saját korára, az 1956 utáni szovjet megszállásra is utal.'
by_id(d,'c1-pestiironia-consolidation-4')['set'].update({"sentence":"Karinthy Így írtok ti című kötete _____ gyűjteménye.","hint":"style parody, plural","answers":["stílusparódiák","paródiák"],"answer":None,"english":"Karinthy's volume That's How You Write is a collection of style parodies."})
by_id(d,'c1-pestiironia-consolidation-5')['set']['hint']="stage asides (plural, 'with his')"
by_id(d,'c1-pestiironia-consolidation-7')['set']['hint']="allusions (plural, 'its')"
save('urban-satire',d)
# hungarian-metaphors
d=load('hungarian-metaphors')
p=by_id(d,'c1-metaforak-05-dialogue-5')['set']['prompt']
p[1]['text']="Egyes nyelvészek szerint csak akkor, ha nem tűrjük passzívan a változást, hanem a nyelvet folyamatosan és _____."
by_id(d,'c1-metaforak-consolidation-6')['set']['hint']="moral backbone (plural, 'their')"
save('hungarian-metaphors',d)
# rule-of-law: 'anyajog' is from 8/1990 (IV. 23.) AB, before 23/1990: not 'később'
d=load('rule-of-law')
f=by_old(d,'1990-ben a rendszerváltó Magyarország')
f['new']=f['new'].replace("a testület az emberi méltóságot később 'anyajognak' is nevezte.","a testület az emberi méltósághoz való jogot 'anyajognak' is nevezte.")
assert 'később' not in f['new']
save('rule-of-law',d)
print('ok')
