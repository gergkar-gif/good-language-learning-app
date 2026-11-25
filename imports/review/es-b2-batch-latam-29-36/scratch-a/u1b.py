import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
V='b2-chile-atacama-patagonia-vocab'
s='b2-chileextremos-consolidation'
p='lessons/b2/%s.json'%s
d=jl(p)
d['title']='Review: from the Atacama Desert to the ice of Patagonia'
d['goal']='Review the north and the south of Chile: astronomy, copper, the Mapuche, glaciers and energy.'
d['grammar']='review of cleft sentences, the passive with se, reported statements, volver a + infinitive and hypothetical conditions'
goals=['I can talk about the extreme landscapes of Chile, from Atacama to Patagonia.','I can use cleft sentences, the passive *se*, *según* and *dice que*, *volver a* and *si* + imperfect subjunctive on these topics.','I can use the words for observatories, copper mining, Mapuche culture, glaciers and energy.']
for x in d['sections']:
    if x['type']=='goal': x['items']=goals
    if x['type']=='checklist': x['items']=goals
jw(p,d)
items=[
 matching(s+'.ex01',[['el salar','salt flat'],['el rajo','open-pit mine, the pit itself'],['la machi','Mapuche healer and spiritual authority'],['el fiordo','fjord, long narrow inlet of the sea between mountains'],['el litio','lithium']],V),
 fill(s+'.ex02','Lo que __ a Atacama tan especial para la astronomía es su cielo claro.','hace','What makes Atacama so special for astronomy is its clear sky.','oraciones-hendidas-enfasis'),
 mc(s+'.ex03','Which sentence says: "Solar plants are built in the desert"?',['Se construyen plantas solares en el desierto.','Se construye plantas solares en el desierto.','Plantas solares se construye en el desierto.'],0,'pasiva-refleja'),
 build(s+'.ex04',['Según','los','científicos,','los','glaciares','son','cada','vez','más','pequeños.'],'According to the scientists, the glaciers are getting smaller and smaller.','estilo-indirecto-informacion'),
 fill(s+'.ex05','Los visitantes __ a mirar el glaciar antes de irse.','vuelven','The visitors look at the glacier again before leaving.','volver-a-infinitivo'),
 mc(s+'.ex06','Which sentence says: "If there were more sun, we would produce more electricity"?',['Si hubiera más sol, produciríamos más electricidad.','Si habría más sol, produciríamos más electricidad.','Si hubiera más sol, produciremos más electricidad.'],0,'hypothetical-structures'),
 dlg(s+'.ex07',[('Carlos','¿Qué quieres ver en el norte de Chile?'),('Meg','_____'),('Carlos','Yo también.')],['Quiero visitar un observatorio y ver el cielo del desierto.','Quiero ver un témpano y un ventisquero en el desierto.','Quiero conocer un fiordo y una turbera en el norte de Chile.'],0,V),
 dic(s+'.ex08','Fue en Atacama donde se construyó el radiotelescopio ALMA.','It was in Atacama that the ALMA radio telescope was built.','oraciones-hendidas-enfasis'),
]
jw('exercises/b2/%s-ex.json'%s,dict(lesson=s,exercises=items))
import json
ch={}
def C(stem,title,scen,prompt,cues,target,eng,cando):
    ch[stem]=dict(tier='tier1',level='B2',title='Communicative Challenge: '+title,scenario=scen,prompt=prompt,cues=cues,target=target,english=eng,canDo=cando)
C('b2-chileextremos-01','The Sky of Atacama','You are Meg. You and Carlos are watching a documentary about the Atacama Desert, and he asks why astronomers work there.','Tell Carlos what makes Atacama special for astronomy.',['Say what makes the desert special for astronomers','Stress it with a cleft sentence'],'Lo que hace especial a Atacama es su cielo despejado.','What makes Atacama special is its clear sky.',goals and None)
C('b2-chileextremos-02','How Copper Is Obtained','You are Carlos. You and Meg are reading an article about copper mining in northern Chile, and she asks how the copper is obtained.','Tell Meg one step of how copper is obtained.',['Say what is done with the rock first','Do not say who does it'],'Primero se rompe la roca y después se aplica la lixiviación.','First the rock is broken, and then leaching is applied.',None)
C('b2-chileextremos-03','Who Says What','You are Meg. You and Carlos are watching a documentary about the Mapuche, and he asks you what the organisations in the film want.','Tell Carlos what the Mapuche organisations say about the land.',['Name who says it','Say what they want'],'Las organizaciones mapuche dicen que el Estado debe devolver las tierras.','Mapuche organisations say that the state must return the land.',None)
C('b2-chileextremos-04','Again in Patagonia','You are Carlos. You and Meg are planning a trip to southern Chile, and she asks if people visit Torres del Paine more than once.','Tell Meg that many travellers go to the park again.',['Say that many travellers do it','Say that they visit the park a second time'],'Muchos viajeros vuelven a visitar Torres del Paine.','Many travellers visit Torres del Paine again.',None)
C('b2-chileextremos-05','If There Were More Lines','You are Meg. You and Carlos are reading an article about solar energy in Chile, and he asks what the problem is.','Tell Carlos what would happen with more transmission lines.',['Imagine more lines','Say what would improve'],'Si hubiera más líneas de transmisión, se aprovecharía mejor la energía solar.','If there were more transmission lines, solar energy would be used better.',None)
C('b2-chileextremos-consolidation','From Atacama to Patagonia','You are Carlos. You and Meg have watched a whole documentary about Chile, and she asks what surprised you most.','Tell Meg one fact you learned, using a cleft sentence.',['Say where something is','Stress the place'],'Fue en el llano de Chajnantor donde se instaló ALMA.','It was on the Chajnantor plateau that ALMA was built.',None)
# canDo = first goal line
for stem in ch:
    l=jl('lessons/b2/%s.json'%stem)
    g=[x for x in l['sections'] if x['type']=='goal'][0]['items'][0]
    ch[stem]['canDo']=g
json.dump(ch,open('/home/user/parlour-read-a/challenges-chile-atacama-patagonia.json','w'),ensure_ascii=False,indent=2)
