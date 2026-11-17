"""Reviewer's changes to reader A's review lists (edit new/set only, never old)."""
import json,sys
B=sys.argv[1]
def load(u,k='review'): return json.load(open(f'{B}/fixes-{u}.{k}.json'))
def save(u,d,k='review'): json.dump(d,open(f'{B}/fixes-{u}.{k}.json','w'),ensure_ascii=False,indent=1)
def by_old(d,frag):
    m=[f for f in d if frag in f.get('old','')]; assert len(m)==1,(frag,len(m)); return m[0]
def by_id(d,i):
    m=[f for f in d if f.get('id')==i and 'set' in f]; assert len(m)==1,(i,len(m)); return m[0]
# language-worldview
d=load('language-worldview')
by_old(d,'~13–15 million')['new']='If a medium-sized language (Hungarian has about 13 million speakers) lacks'
f=by_id(d,'c1-nyelvfilozofia-consolidation.ex08')['set']
f.update({"sentence":"A nemzeti nyelv védelme a digitális korban a nyelv hosszú távú _____ kérdése.","answers":["fennmaradásának"],"answer":None,"hint":"survival, possessed","english":"In the digital age, protecting the national language is a question of the language's long-term survival."})
p=by_id(d,'c1-nyelvfilozofia-04.ex07')['set']['prompt']
p[1]['text']="Egy értelmezés szerint azért, mert a másik embert átvitt értelemben egy _____, a szívünkbe fogadjuk be."
save('language-worldview',d)
# hungarian-essay
d=load('hungarian-essay','auto')
by_old(d,'Stylistic politeness in C1 literary essays')['new']="You know softening from B2 Unit 29 (*célszerű lenne*, *indokolt volna*). Szerb's essays soften assertions in the same spirit: a phrase such as *aligha tévedünk, ha úgy véljük* ('we are hardly wrong if we think') invites"
save('hungarian-essay',d,'auto')
d=load('hungarian-essay')
by_id(d,'c1-esszemuveszet-03-production-6')['set']['template']=[{"prompt":"Write a softened scholarly opinion using 'Aligha tévedünk, ha úgy véljük'.","answer":"Aligha tévedünk, ha úgy véljük, hogy a szerző szórakoztatni és tanítani is akarta az olvasót."}]
save('hungarian-essay',d)
# paradigm-shifts
d=load('paradigm-shifts')
by_old(d,'Thomas Kuhn pedig azzal válaszolt')['new']="Thomas Kuhn pedig a tudományos forradalmakról írt, a tudományfilozófiában heves vita bontakozott ki. Lakatos Imre úgy olvasta Kuhn elméletét, hogy a tudósok irracionálisan ragaszkodnak paradigmáikhoz, és megpróbálta feloldani ezt a vitát."
by_old(d,'Amikor Neumann János a huszadik század negyvenes')['new']="Neumann János a huszadik század negyvenes éveiben leírta a tárolt programú számítógép elvét, amelyet azóta Neumann-architektúraként ismerünk. Az elvet az 1945-ös EDVAC-jelentés fogalmazta meg, de Eckert és Mauchly szerepe is jelentős volt, ezért hogy kié az elsőség, a kutatók vitatják. A tárolt programú gép nem egyszerűen számológép volt, hanem egyetemes információfeldolgozó gépezet."
save('paradigm-shifts',d)
# public-debate
d=load('public-debate')
f=by_old(d,'Deák a passzív ellenállás vezére lett')
f['new']="Deák a passzív ellenállás egyik vezéralakja lett. Nem fogadott el hivatalt, és nem volt hajlandó együttműködni az új rendszerrel; a hagyomány szerint adót sem fizetett önként. Húsvéti cikkében és a feliratokban jogi érvekkel fejtette ki a magyar jogfolytonosság elvét. Egyik ismert gondolata szerint amit erővel elvesznek egy néptől, azt az idő visszahozhatja, de amiről a nemzet önként lemond, azt nehéz visszaszerezni."
by_old(d,'receptkönyveket olvastak fel')['new']="A szónokok órákon keresztül beszéltek a szószékről, hogy megakadályozzák a szavazást; egy anekdota szerint olykor receptkönyvből is olvastak fel. Az ülések hangosak voltak, és a sértések miatt időnként lovagias ügy, vagyis párbaj is lett belőle."
by_old(d,"Gróf Széchenyi István, a 'legnagyobb magyar'")['new']="a pozsonyi országgyűlésen folyt a vita a modern Magyarország jövőjéről. Két jelentős politikus állt a vita két oldalán: gróf Széchenyi István, akit Kossuth 'a legnagyobb magyarnak' nevezett, és Kossuth Lajos, a kor híres szónoka."
save('public-debate',d)
print('ok')
