import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
V2='b2-mexico-north-vocab'
def match2(i,pairs): return {'id':i,'type':'matching','category':'vocabulary','pairs':[list(p) for p in pairs],'teaches':[V2]}
def dict_(i,s,eng,skill): return {'id':i,'type':'dictation','category':'listening','sentence':s,'english':eng,'teaches':[skill]}
def lesson2(stem,title,goal,gram,items,intro=None):
    p=f'lessons/b2/{stem}.json'; l=rj(p)
    l['title']=title; l['goal']=goal; l['grammar']=gram
    for s in l['sections']:
        if s['type'] in('goal','checklist'): s['items']=items
        if s['type']=='intro' and intro: s['title']=intro[0]; s['body']=intro[1]
    wj(p,l)
CO='conectores-temporales-narrativos'
# ---------- 01
s='b2-mexiconorte-01'
items=["I can use conforme to say that something changes little by little, as in Conforme se sube a la sierra, el clima cambia.",
"I can describe the deserts, canyons and mountains of northern Mexico.",
"I can say who the Rarámuri are and what they are known for.",
"I can use the lesson's words for the desert, the canyon and the ravine."]
lesson2(s,"Northern Mexico: deserts, canyons and the Rarámuri","Use conforme and other time connectors from B2 Unit 2 to describe how the landscape, the climate and the north's cities change.","time connectors: conforme (recap)",items,
("Latin America Unit 2: Northern Mexico",[
"This is Unit 2 of the B2 Latin America track. As in every unit of the track, you learn no new grammar: each lesson applies a skill you already know to the region and teaches the words for the topic. The instructions and grammar screens are in English; the readings are in Spanish.",
"This unit is about northern Mexico: its deserts and canyons, vaquero culture, the industrial city of Monterrey, the border with the United States and the factories that export to it.",
"In this first lesson you recap the time connectors from B2 Unit 2, above all conforme, and use them to describe how the landscape changes and how the north's cities grow."]))
story_update(s,"El norte: desiertos, barrancas y rarámuris","Northern Mexico has deserts, mountains and canyons; the Rarámuri live in the Copper Canyon region, and the north's distance from the capital shaped its history.",[
"El norte de México ocupa gran parte del territorio del país, y no es un paisaje uniforme. Hay desiertos, como el de Sonora y el de Chihuahua, y también sierras, cañones y grandes llanuras. En Chihuahua están las dunas de Samalayuca. Llueve poco, y el agua es un recurso escaso en casi toda la región.",
"En la Sierra Madre Occidental, en el estado de Chihuahua, se encuentran las Barrancas del Cobre, un sistema de cañones muy extenso. Conforme se sube de las barrancas a la sierra, el clima cambia: en el fondo hace mucho calor, y en las partes altas hay bosques de pino y en invierno hace frío. Allí vive el pueblo rarámuri, también llamado tarahumara. Muchos rarámuri son conocidos por correr distancias muy largas, a veces con sandalias sencillas, en fiestas y juegos tradicionales de la comunidad.",
"Durante la época colonial, el norte estaba lejos de la capital. Conforme se descubrían minas de plata, llegaban colonos y se fundaban pueblos y ciudades, pero muchas zonas seguían casi vacías. Según muchos historiadores, la distancia, el clima duro y la poca presencia del gobierno ayudaron a formar una identidad regional con fuerte autonomía. Hoy, conforme crecen las ciudades, la falta de agua preocupa en varias zonas del norte."])
vocab_update(s,"Northern Mexico: deserts, canyons and the Rarámuri: vocabulary",[
("la aridez","dryness, aridity","noun"),("la sierra","mountain range","noun"),("el barranco","ravine, gorge","noun"),("el cañón","canyon","noun"),("inhóspito","inhospitable","adjective"),("la llanura","plain","noun")])
grammar_update(s,"Conforme and Time Connectors in Northern Mexico",[
T("What you already know","You know *conforme* and *al cabo de* from B2 Unit 2, and *a medida que* from B1 Unit 2. In a story, *conforme* shows two things changing together, little by little: *Conforme pasaban los días, se sentía mejor*. It is not only for stories about people: it is just as useful for a landscape that changes as you move through it, or for a region that changes as it grows. This lesson applies it to northern Mexico."),
TAB("Gradual, skipped or immediate",[
["Conforme + verb","Two changes together, little by little: Conforme se sube a la sierra, el clima cambia. (As you go up into the mountains, the climate changes.)"],
["A medida que + verb","The same meaning: A medida que crecen las ciudades, hay menos agua. (As the cities grow, there is less water.)"],
["Al cabo de + a length of time","A stretch of time is skipped: Al cabo de varios días, llegaron a la sierra. (After several days, they reached the mountains.)"],
["Apenas + verb","The second event follows at once: Apenas salió el sol, empezó el calor. (As soon as the sun came up, the heat began.)"]]),
T("Mood and tense","With a real, repeated or past change, *conforme* takes the indicative: *Conforme se sube, hace menos calor* (a general fact), *Conforme pasaban los siglos, aprendieron a vivir con poca agua* (past, with the *imperfecto*). Unlike *apenas* and *al cabo de*, *conforme* does not mean that something happens at once or after a time: it means that the two things grow together."),
EX("In context",[
("Conforme se sube a la sierra, el clima cambia.","As you go up into the mountains, the climate changes."),
("Conforme pasaban los siglos, los pueblos del desierto aprendieron a vivir con poca agua.","As the centuries passed, the peoples of the desert learned to live with little water."),
("Conforme se descubrían minas de plata, llegaban colonos al norte.","As silver mines were discovered, settlers came to the north."),
("Conforme crecen las ciudades del norte, la falta de agua preocupa más.","As the cities of the north grow, the lack of water causes more concern."),
("Al cabo de varios días de viaje, llegaron a las barrancas.","After several days of travel, they reached the ravines.")]),
TIP("*Conforme* also means \"in accordance with\" (*conforme a la ley*). When a verb follows, as here, it means \"as\".")])
ex_write(s,[
match2(s+'.ex01',[("la aridez","dryness, aridity"),("el barranco","ravine, gorge"),("el cañón","canyon"),("inhóspito","inhospitable")]),
mc(s+'.ex02',"Which sentence says that the climate changes little by little as you go up into the mountains?",[
"Conforme se sube a la sierra, el clima cambia.",
"Apenas se sube a la sierra, el clima cambia.",
"Al cabo de subir a la sierra, el clima cambia."],CO),
fill(s+'.ex03',"____ pasaban los siglos, los pueblos del desierto aprendieron a vivir con poca agua.",None,"As the centuries passed, the peoples of the desert learned to live with little water.",CO,answers=["Conforme","A medida que"]),
build(s+'.ex04',["Conforme","se","sube","a","la","sierra,","el","clima","cambia."],"As you go up into the mountains, the climate changes.",CO),
dial(s+'.ex05',[("Viajero","¿Qué pasa con el clima durante la subida a la sierra?"),("Guía","_____"),("Viajero","Entonces arriba el paisaje es muy diferente.")],[
"Conforme se sube, hace menos calor y las noches son más frías.",
"Al cabo de la subida, hace menos calor y las noches son más frías.",
"Conforme se sube, hacía menos calor y las noches son más frías."],CO),
dict_(s+'.ex06',"Conforme se sube de la llanura a la sierra, el clima cambia poco a poco.","As you go up from the plain to the mountains, the climate changes little by little.",CO)])
