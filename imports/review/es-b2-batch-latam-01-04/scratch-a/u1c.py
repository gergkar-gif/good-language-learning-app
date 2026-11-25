import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
# ---------------- LESSON 05
s='b2-mexicocentro-05'
items=["I can tell what happened in Mexico City in 1985, using clefts, fronting and no ... sino together.",
"I can choose the right tool for each job: a cleft for the key fact, fronting for a quality, no ... sino for a correction.",
"I can use a stance adverb to say how I feel about a fact of the recent past.",
"I can use the lesson's words for the earthquake, the rubble and the victims."]
lesson_update(s,"Mexico City: the 1985 earthquake and civil society","Use clefts, fronting, stance adverbs and no ... sino together to tell what the 1985 earthquake changed in Mexico City.","clefts, fronting, stance adverbs and no ... sino together (recap)",items)
story_update(s,"El sismo de 1985 y la sociedad civil","The 1985 earthquake destroyed buildings in Mexico City, and the neighbours' rescue work is often seen as the start of modern civil society; the text then follows the city's political changes up to 2017.",[
"El 2 de octubre de 1968, en la Plaza de las Tres Culturas de Tlatelolco, las fuerzas del Estado dispararon contra una manifestación de estudiantes, diez días antes de los Juegos Olímpicos. Lamentablemente, el número de muertos sigue siendo motivo de discusión, y no existe una cifra que todos acepten.",
"Diecisiete años después, el 19 de septiembre de 1985, un sismo de magnitud 8,1 sacudió el centro del país. En la capital se cayeron cientos de edificios, entre ellos hospitales, oficinas y bloques de viviendas, en colonias como la Roma, la Doctores y Tlatelolco. Los daños fueron mayores en las zonas del antiguo lago, donde el suelo es blando.",
"Según muchos testimonios, el gobierno tardó en reaccionar. En muchos barrios, no fueron las autoridades, sino los vecinos quienes organizaron la ayuda al principio. Miles de personas, sobre todo jóvenes, formaron brigadas para sacar a otras de los escombros, y se abrieron albergues y se repartió comida para los damnificados. Enorme fue la solidaridad entre desconocidos.",
"El cronista Carlos Monsiváis sostuvo que en 1985 nació la sociedad civil moderna de México. De aquella solidaridad surgieron organizaciones de damnificados que pedían viviendas y reconstrucción. Según muchos relatos, la ayuda no llegó de arriba, sino de los propios vecinos.",
"Los cambios políticos llegaron después. En 1997 los habitantes de la capital eligieron por primera vez a su jefe de gobierno, y ganó Cuauhtémoc Cárdenas. En 2016 una reforma constitucional convirtió el Distrito Federal en la Ciudad de México, y en 2017 se aprobó la constitución de la ciudad."])
vocab_update(s,"Mexico City: the 1985 earthquake and civil society: vocabulary",[
("el sismo","earthquake","noun"),("el damnificado","victim, person affected by a disaster","noun"),("la brigada","brigade, rescue team","noun"),("el escombro","rubble, debris","noun"),("la solidaridad","solidarity","noun"),("el albergue","shelter","noun")])
grammar_update(s,"The Three Tools Together: the 1985 Earthquake",[
T("What you already know","You know *Lo que más nos sorprendió fue su serenidad*, *Crucial fue la intervención del mediador*, *en realidad* and *No es un fracaso, sino más bien una lección* from B2 Unit 1: this unit's emphasis tools (cleft, fronting, stance adverb, *no ... sino*). You also know *sino* and *sino que* from B1 Unit 40. When you tell the story of the 1985 earthquake, give each tool its own job: a cleft names the key fact, fronting stresses a quality at the high point, *no ... sino* corrects a first idea, and a stance adverb says how you see the fact."),
TAB("The four tools in the story of 1985",[
["Cleft sentence","Lo que más recuerdan muchos testigos es la solidaridad de los vecinos. (What many witnesses remember most is the solidarity of the neighbours.)"],
["Fronting","Enorme fue la solidaridad de los vecinos con los damnificados. (Enormous was the neighbours' solidarity with the victims.)"],
["No ... sino","No fueron las autoridades, sino los vecinos quienes organizaron la ayuda. (It was not the authorities but the neighbours who organised the help.)"],
["Stance adverb","Lamentablemente, el número de muertos de 1968 sigue en discusión. (Unfortunately, the number of deaths in 1968 is still disputed.)"]]),
EX("More examples",[
("Fue el 19 de septiembre de 1985 cuando un sismo sacudió el centro del país.","It was on 19 September 1985 that an earthquake shook the centre of the country."),
("Cientos de edificios se cayeron en pocos minutos.","Hundreds of buildings collapsed in a few minutes."),
("Los vecinos no esperaron a las autoridades, sino que formaron brigadas.","The neighbours did not wait for the authorities; they formed rescue teams."),
("En realidad, los daños fueron mayores en las zonas del antiguo lago.","In fact, the damage was greater in the areas of the old lake.")]),
TIP("Vary your sentences: alternate plain order with a cleft, a fronted phrase or a correction. Two emphatic structures in a paragraph shape the reading; one in every sentence tires the reader.")])
ex_write(s,[
match(s+'.ex01',[("el sismo","earthquake"),("el damnificado","victim, person affected by a disaster"),("la brigada","brigade, rescue team"),("el escombro","rubble, debris")]),
mc_read(s+'.ex02',"According to the text, what did many neighbours do after the 1985 earthquake?",[
"Formaron brigadas para sacar a personas de los escombros y abrieron albergues.",
"Esperaron en sus casas hasta que llegaron las brigadas del gobierno.",
"Salieron de la ciudad para buscar ayuda en otros países y volvieron años después."]),
fill(s+'.ex03',"____, el número de muertos de 1968 todavía no está claro.","Lamentablemente","Unfortunately, the number of deaths in 1968 is still not clear.",'stance-adverbs',hint="unfortunately"),
mc_read(s+'.ex04',"According to the text, what happened to the buildings in the capital in 1985?",[
"Se cayeron cientos de edificios, con más daños donde el suelo es blando.",
"Se cayeron pocos edificios nuevos, con más daños en las montañas.",
"No se cayó ningún edificio, pero hubo muchos daños en los hospitales."]),
build(s+'.ex05',["Enorme","fue","la","solidaridad","de","los","vecinos","con","los","damnificados."],"Enormous was the neighbours' solidarity with the victims.",'inversion-enfasis-fronting'),
listen(s+'.ex06',"En muchos barrios, no fueron las autoridades, sino los vecinos quienes organizaron la ayuda.",[
"In many neighbourhoods, it was not the authorities but the neighbours who organised the help.",
"In many neighbourhoods, it was not the neighbours but the authorities who organised the help.",
"In many neighbourhoods, it was the authorities and the neighbours who organised the help."],'sino-vs-pero'),
dial(s+'.ex07',[("Guía","¿Quién organizó la ayuda en muchos barrios al principio?"),("Tú","_____"),("Guía","Por eso se dice que ahí empezó la sociedad civil.")],[
"Fueron los vecinos quienes organizaron la ayuda.",
"Fue los vecinos quienes organizaron la ayuda.",
"Fue en los barrios donde organizaron la ayuda."],'oraciones-hendidas-enfasis'),
write(s+'.ex08',[("Say that what the neighbours organised was help for the victims. Start with 'Lo que'.","Lo que organizaron los vecinos fue la ayuda para los damnificados.")],'oraciones-hendidas-enfasis')])

# ---------------- CONSOLIDATION
s='b2-mexicocentro-consolidation'
items=["I can recall the main facts about central Mexico: the lake basin, Tenochtitlan, the colonial city, muralism and the 1985 earthquake.",
"I can review the unit's words for the basin, the city and the murals.",
"I can use clefts, fronting, stance adverbs and no ... sino on these topics.",
"I can write two sentences about central Mexico, one with a cleft and one with no ... sino."]
lesson_update(s,"Unit 1 Consolidation","Review the facts and the emphasis tools of the central Mexico unit: clefts, fronting, stance adverbs and no ... sino.","emphasis tools on central Mexico (review)",items)
ex_write(s,[
match(s+'.ex01',[("la cuenca","basin"),("la chinampa","chinampa, floating garden"),("el virrey","viceroy"),("el muralismo","muralism, the mural movement")]),
match(s+'.ex02',[("el hundimiento","subsidence, sinking"),("el asedio","siege"),("el retablo","altarpiece"),("el sismo","earthquake")]),
mc_read(s+'.ex03',"According to the readings of this unit, what was the colonial city built on?",[
"Sobre los restos de Tenochtitlan, la ciudad que cayó en 1521.",
"Sobre un valle sin lagos, lejos de los volcanes y de las montañas.",
"Sobre las montañas del norte, lejos del lago y de la capital."]),
fill(s+'.ex04',"Lo que protegía a la ciudad ____ el albarradón de Nezahualcóyotl.",None,"What protected the city was the dike of Nezahualcóyotl.",'oraciones-hendidas-enfasis',hint="ser",answers=["era","fue"]),
build(s+'.ex05',["Muy","famosos","son","los","murales","de","Rivera","en","el","Palacio","Nacional."],"Very famous are Rivera's murals in the National Palace.",'inversion-enfasis-fronting'),
fill(s+'.ex06',"Los murales no eran para decorar, ____ para enseñar historia.","sino","The murals were not for decoration but for teaching history.",'sino-vs-pero',hint="but rather"),
dial(s+'.ex07',[("Guía","¿Se sabe cuántas personas murieron en Tlatelolco en 1968?"),("Tú","_____"),("Guía","Entonces la discusión sigue abierta.")],[
"Lamentablemente, no hay un número que todos acepten.",
"Apenas, no hay un número que todos acepten.",
"Propiamente dicho, no hay un número que todos acepten."],'stance-adverbs'),
write(s+'.ex08',[("Say that what the neighbours formed were rescue teams. Start with 'Lo que'.","Lo que formaron los vecinos fueron brigadas.")],'oraciones-hendidas-enfasis'),
write(s+'.ex09',[("Say that the neighbours did not wait for the authorities but formed rescue teams. Use 'no ..., sino que'.","Los vecinos no esperaron a las autoridades, sino que formaron brigadas.")],'sino-vs-pero')])
l=rj('lessons/b2/b2-mexicocentro-consolidation.json')
for sec in l['sections']:
    if sec['type']=='exercise-group': sec['exerciseRefs'].append(s+'.ex09')
wj('lessons/b2/b2-mexicocentro-consolidation.json',l)
