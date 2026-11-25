import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-belize-guianas-vocab'
TAIL='The screens and instructions are in English; the readings are in Spanish.'
NOTE=' (Belize, Guyana and Suriname are not Spanish-speaking countries: their official languages are English and Dutch.)'

# ---------- 01
s='b2-guyanas-01'
lesson(s,'Belize: English, Kriol, Spanish and Garifuna in a small country by the reef',
 'Talk about the languages and the Garifuna heritage of Belize with the passive with ser.',
 'the passive with ser + past participle',
 ['In this lesson you read about Belize, a small country on the Caribbean coast of Central America where English is the official language. You will also read about its barrier reef and about the Garifuna people.',
  'The grammar is one you know: the passive with *ser* + past participle, for saying what was done and by whom. '+TAIL],
 ['I can say what was done, and by whom, with *ser* + past participle and *por*.',
  'I can say which languages are spoken in Belize and which is official.',
  'I can use the new words for reefs, languages and deportation.'])
write_gr(s,None,'Who Was Declared, Who Was Deported: the Passive with Ser',[
 T('You know the passive with *ser* + past participle from B1 Unit 18: *La ley fue aprobada por el Parlamento*. The participle agrees with the subject, and *por* names who did the action. The history of Belize is full of things that were done to a place or a people, so it is a good place to use it.','What you already know'),
 TB('Ser + participle, agreeing with the subject',[
  ('La barrera de coral fue declarada Patrimonio de la Humanidad.','feminine singular: the barrier reef was declared a World Heritage Site'),
  ('Los garífunas fueron deportados por los británicos.','masculine plural: the Garifuna were deported by the British'),
  ('La música garífuna fue proclamada obra maestra por la UNESCO.','*por* names the doer: by UNESCO'),
  ('El criollo es hablado por muchos beliceños.','present tense: Creole is spoken by many Belizeans')]),
 EX([('La barrera de coral fue declarada Patrimonio de la Humanidad en 1996.','The barrier reef was declared a World Heritage Site in 1996.'),
     ('Los garífunas fueron deportados por los británicos a la isla de Roatán en 1797.','The Garifuna were deported by the British to the island of Roatán in 1797.'),
     ('La música garífuna fue proclamada obra maestra por la UNESCO en 2001.','Garifuna music was proclaimed a masterpiece by UNESCO in 2001.'),
     ('Las lenguas mayas son habladas por muchas familias del sur.','The Maya languages are spoken by many families in the south.')]),
 TIP('Use *ser* + participle when you want to name the doer or stress the result; with *se* (B1 Unit 6) you leave the doer out. Do not change *por* into *de* or *para*: *deportados por los británicos*. And remember the agreement: *declarada* goes with *barrera*, *deportados* with *garífunas*.')])
write_voc(s,None,'Belize: reef, languages and the Garifuna','Reef, Creole, drums',[
 ('el arrecife','reef','noun'),('el criollo','Creole (language)','noun'),('deportar','to deport','verb'),('el tambor','drum','noun')])
write_ex(s,[
 match(s+'.ex01',[('el arrecife','reef'),('el criollo','Creole (language)'),('deportar','to deport'),('el tambor','drum')],V),
 mc(s+'.ex02','Which sentence says "The Garifuna were deported by the British to the island of Roatán"?',
  ['Los garífunas fueron deportados por los británicos a la isla de Roatán.','Los garífunas fueron deportadas por los británicos a la isla de Roatán.','Los garífunas fueron deportados de los británicos a la isla de Roatán.'],teaches='ser-passive'),
 fill(s+'.ex03','La música garífuna fue proclamada obra maestra __ la UNESCO en 2001.','por','Garifuna music was proclaimed a masterpiece by UNESCO in 2001.','ser-passive'),
 build(s+'.ex04','La barrera de coral fue declarada Patrimonio de la Humanidad en 1996.','The barrier reef was declared a World Heritage Site in 1996.','ser-passive'),
 dlg(s+'.ex05','¿Qué idiomas se hablan en Belice?','','Entonces es un país muy variado.',
  ['El inglés es oficial, y también se hablan criollo, español y garífuna.','El garífuna es la lengua oficial, y el inglés no se habla en el país.','El criollo es la lengua oficial, y el inglés solo se habla en hoteles.'],V),
 dict_(s+'.ex06','El inglés es la lengua oficial de Belice, pero el criollo es hablado por muchos beliceños.','English is the official language of Belize, but Creole is spoken by many Belizeans.','ser-passive')])
n=story(s,'Belice: una pequeña nación con muchas lenguas','Belize is a small former British colony where English is official and many other languages are spoken; the text covers its reef, the Garifuna and the border dispute with Guatemala.',[
 'Belice es un país pequeño, de unos veintidós mil kilómetros cuadrados, en la costa caribeña de América Central. Fue una colonia británica, Honduras Británica, hasta 1981, y es el único país de América Central donde el inglés es la lengua oficial. El español no es lengua oficial, pero una gran parte de la población lo habla. Se hablan además el criollo beliceño, que muchos usan todos los días, el garífuna, el maya y otras lenguas.',
 'En el mar, Belice tiene una de las barreras de coral más grandes del mundo. La barrera fue declarada Patrimonio de la Humanidad por la UNESCO en 1996. En ella está el Gran Agujero Azul, un círculo de agua oscura de unos trescientos metros de ancho y más de cien de profundidad, que atrae a buceadores de todo el mundo. En el interior, la selva esconde ruinas mayas como Caracol y Xunantunich.',
 'Los garífunas son un pueblo que nació en la isla caribeña de San Vicente, de la mezcla de personas de origen africano con pueblos indígenas del Caribe. Los británicos lucharon contra ellos y, en 1797, los garífunas fueron deportados a la isla de Roatán, hoy parte de Honduras. Después se instalaron en la costa de América Central, también en Belice. Cada 19 de noviembre se celebra su llegada con música, tambores y danzas, sobre todo en Dangriga. En 2001, la UNESCO proclamó el idioma, la danza y la música de los garífunas obra maestra del patrimonio oral e inmaterial de la humanidad.',
 'Belice tiene también una disputa con Guatemala. Guatemala reclama una parte del territorio de Belice, y Belice defiende sus fronteras actuales. Los dos países aprobaron en referendos, en 2018 y en 2019, llevar el caso a la Corte Internacional de Justicia, en La Haya.'],
 [('According to the text, which is the official language of Belize?',['El inglés.','El español.','El criollo.'],'The first paragraph says English is official and Spanish is not.'),
  ('What happened to the Garifuna in 1797?',['Fueron deportados por los británicos a la isla de Roatán.','Fundaron la ciudad de Dangriga.','Llegaron de África a San Vicente.'],'The third paragraph describes the deportation.'),
  ('What did Belize and Guatemala agree in referendums in 2018 and 2019?',['Llevar la disputa a la Corte Internacional de Justicia.','Cambiar su frontera sin ayuda de ningún tribunal.','Hacer del español la lengua oficial de Belice.'],'The fourth paragraph reports the referendums.')])
print(s,n)

# ---------- 02
s='b2-guyanas-02'
lesson(s,'The Guiana Shield: flat-topped mountains older than the Andes',
 'Describe the tepuis and what matters about them, using cleft sentences to put one idea in the spotlight.',
 'cleft sentences and focus constructions',
 ['In this lesson you read about the Guiana Shield, an ancient rock region in the north of South America, and about the tepuis, the flat-topped mountains that rise over the jungle. You also read about the Angel Falls and about the mercury that illegal gold mining puts into the rivers.',
  'The grammar is one you know: cleft sentences, which put one piece of information in the spotlight. '+TAIL],
 ['I can put one idea in the spotlight with *lo que ... es* and *es/fue ... donde*, *quien*, *cuando*.',
  'I can say what a tepuy is and what makes it special.',
  'I can use the new words for plateaus, waterfalls and mercury.'])
write_gr(s,None,'The Spotlight on the Tepuis: Cleft Sentences',[
 T('You know cleft sentences from B2 Unit 1 (*Lo que ... fue ...* and *Fue ... quien / donde / cuando*). They split one idea in two so that the piece you want to stress lands in the spotlight. The tepuis give you plenty to spotlight: what makes them special, where something is, who wrote about them.','What you already know'),
 TB('Three ways to put the spotlight on one idea',[
  ('Lo que hace únicos a los tepuyes es su aislamiento.','*lo que* + verb + *ser*: what makes the tepuis unique is their isolation'),
  ('Es en el Auyantepuy donde empieza el Salto Ángel.','*es/fue* + place + *donde*: it is on the Auyantepuy that the Angel Falls begin'),
  ('Fue Conan Doyle quien escribió una novela sobre una meseta aislada.','*fue* + person + *quien*: it was Conan Doyle who wrote a novel about an isolated plateau')]),
 EX([('Lo que hace únicos a los tepuyes es su aislamiento.','What makes the tepuis unique is their isolation.'),
     ('Es en el Auyantepuy donde empieza el Salto Ángel.','It is on the Auyantepuy that the Angel Falls begin.'),
     ('Fue en 1912 cuando Conan Doyle publicó «El mundo perdido».','It was in 1912 that Conan Doyle published The Lost World.'),
     ('Lo que preocupa a las comunidades es el mercurio de la minería ilegal.','What worries the communities is the mercury from illegal mining.')]),
 TIP('Use a cleft sentence for the one idea you want the listener to remember, not in every sentence. The tense of *ser* follows the other verb (*lo que preocupa es*, *fue en 1912 cuando*), and the spotlighted piece keeps its preposition: *es en el Auyantepuy donde*.')])
write_voc(s,None,'The Guiana Shield','Tepuis, falls and mercury',[
 ('el tepuy','tepui (flat-topped mountain)','noun'),('la meseta','plateau','noun'),('el mercurio','mercury','noun'),('el aislamiento','isolation','noun')])
write_ex(s,[
 match(s+'.ex01',[('el tepuy','tepui (flat-topped mountain)'),('la meseta','plateau'),('el mercurio','mercury'),('el aislamiento','isolation')],V),
 mc(s+'.ex02','Which sentence says "What makes the tepuis unique is their isolation"?',
  ['Lo que hace únicos a los tepuyes es su aislamiento.','Que hace únicos a los tepuyes es su aislamiento.','Lo que hace únicos a los tepuyes su aislamiento es.'],teaches='oraciones-hendidas-enfasis'),
 fill(s+'.ex03','Es en el Auyantepuy __ empieza el Salto Ángel.','donde','It is on the Auyantepuy that the Angel Falls begin.','oraciones-hendidas-enfasis'),
 build(s+'.ex04','Fue Conan Doyle quien escribió una novela sobre una meseta aislada.','It was Conan Doyle who wrote a novel about an isolated plateau.','oraciones-hendidas-enfasis'),
 dlg(s+'.ex05','¿Qué es un tepuy?','','Ahora lo entiendo.',
  ['Es una meseta de piedra aislada en la selva.','Es un río que baja de los Andes hasta el mar Caribe.','Es una ciudad con puerto en la costa de Guyana.'],V),
 dict_(s+'.ex06','Lo que preocupa a las comunidades es el mercurio de la minería ilegal.','What worries the communities is the mercury from illegal mining.','oraciones-hendidas-enfasis')])
n=story(s,'El Escudo Guayanés y los tepuyes','The Guiana Shield is one of the oldest rock regions on Earth; the text describes its tepuis, the Angel Falls, its unusual wildlife and the mercury that illegal gold mining puts into the rivers.',[
 'El Escudo Guayanés es una de las formaciones geológicas más antiguas del planeta. Ocupa partes de Venezuela, Guyana, Surinam, la Guayana Francesa, Brasil y Colombia. Sus rocas tienen más de mil millones de años, mucho más que las de los Andes.',
 'Lo más famoso del escudo son los tepuyes, mesetas de arenisca con paredes casi verticales que se elevan sobre la selva. El Roraima está en la frontera de Venezuela, Guyana y Brasil. En el Auyantepuy, en Venezuela, empieza el Salto Ángel, que con 979 metros es la caída de agua sin interrupciones más alta del mundo. El Parque Nacional Canaima, donde están estos tepuyes, es Patrimonio de la Humanidad desde 1994.',
 'Como la cima de cada tepuy está aislada, allí viven plantas y animales que no existen en otros lugares. Hay plantas carnívoras que atrapan insectos porque el suelo tiene pocos nutrientes, y sapos diminutos que caminan en lugar de saltar. Lo que hace únicos a los tepuyes es precisamente ese aislamiento. En 1912, Arthur Conan Doyle publicó «El mundo perdido», una novela de aventuras sobre una meseta aislada en América del Sur donde sobreviven animales prehistóricos.',
 'Los pueblos indígenas de la región, como los pemón, consideran sagrados los tepuyes. Hoy estas comunidades enfrentan un problema: la minería ilegal de oro. Según organizaciones ambientales y comunidades indígenas, en algunos ríos se usa mercurio para separar el oro, y este metal contamina el agua y los peces. Lo que más preocupa a las comunidades es la salud de las familias que viven junto a esos ríos.'],
 [('How high are the Angel Falls, according to the text?',['979 metros.','Más de mil millones de metros.','Unos trescientos metros.'],'The second paragraph gives 979 metres.'),
  ('Why do unique plants and animals live on the tepuis?',['Porque la cima de cada tepuy está aislada.','Porque los tepuyes están junto al mar Caribe.','Porque los pemón los llevaron allí.'],'The third paragraph links the wildlife to isolation.'),
  ('What worries the indigenous communities, according to the text?',['El mercurio que contamina el agua y los peces por la minería ilegal.','La falta de turistas en el Parque Canaima.','Las lluvias demasiado fuertes en la cima de los tepuyes.'],'The fourth paragraph describes the mercury problem.')])
print(s,n)

# ---------- 03
s='b2-guyanas-03'
lesson(s,'Suriname: maroons, contract workers and many languages',
 'Report what historians and the press say about Suriname, with según and verbs like explicar que.',
 'reported statements and citing sources with según',
 ['In this lesson you read about Suriname: its languages, the maroons who escaped slavery and built free communities in the jungle, the workers who came from Asia after 1863, and Suriname today.',
  'The grammar is one you know: reporting what a source says with *según*, *explicar que* and *informar de que*. '+TAIL+NOTE],
 ['I can report what a source says with *según*, *explicar que* and *informar de que*.',
  'I can say which language is official in Suriname and which one people use to understand each other.',
  'I can use the new words for maroons, plantations and abolition.'])
write_gr(s,None,'Who Says So: Citing Sources',[
 T('You know *según* + a source from B1 Unit 13, and how to report statements with verbs such as *explicar que*, *decir que* and *informar de que*. History is mostly what sources tell us, so this is the grammar of the Suriname lesson: say who claims what, and keep the source apart from your own words.','What you already know'),
 TB('Naming the source',[
  ('Según los historiadores, miles de africanos huyeron de las plantaciones.','*según* + source + statement: according to historians, thousands of Africans escaped'),
  ('Los historiadores explican que los cimarrones firmaron tratados de paz.','*explicar que* + clause: historians explain that the maroons signed peace treaties'),
  ('La prensa informó de que se aprobó un proyecto petrolero en 2024.','*informar de que* + clause: the press reported that an oil project was approved in 2024'),
  ('Según el censo, en Surinam viven comunidades de muchos orígenes.','a document can be the source too: according to the census')]),
 EX([('Según los historiadores, miles de africanos esclavizados huyeron de las plantaciones.','According to historians, thousands of enslaved Africans escaped from the plantations.'),
     ('Los historiadores explican que los cimarrones firmaron tratados de paz con los holandeses.','Historians explain that the maroons signed peace treaties with the Dutch.'),
     ('La prensa informó de que en 2024 se aprobó un gran proyecto de petróleo en el mar.','The press reported that in 2024 a large offshore oil project was approved.'),
     ('Según el texto, el neerlandés es la lengua oficial de Surinam.','According to the text, Dutch is the official language of Suriname.')]),
 TIP('With *informar* you need *de que*: *informó de que*, not *informó que*. After *según* there is no *que*: *según los historiadores*, and the verb that follows is an ordinary indicative. The tense of the reported verb follows the time of the facts: past events in the preterite or the imperfect.')])
write_voc(s,None,'Suriname: maroons and abolition','People, plantations and law',[
 ('el cimarrón','maroon (escaped enslaved person)','noun'),('la plantación','plantation','noun'),('la abolición','abolition','noun'),('el neerlandés','Dutch (language)','noun')])
write_ex(s,[
 match(s+'.ex01',[('el cimarrón','maroon (escaped enslaved person)'),('la plantación','plantation'),('la abolición','abolition'),('el neerlandés','Dutch (language)')],V),
 mc(s+'.ex02','Which sentence says "According to historians, thousands of enslaved Africans escaped from the plantations"?',
  ['Según los historiadores, miles de africanos esclavizados huyeron de las plantaciones.','Según que los historiadores, miles de africanos esclavizados huyeron de las plantaciones.','Según a los historiadores, miles de africanos esclavizados huyeron de las plantaciones.'],teaches='estilo-indirecto-informacion'),
 fill(s+'.ex03','La prensa __ de que en 2024 se aprobó un gran proyecto de petróleo en el mar.','informó','The press reported that in 2024 a large offshore oil project was approved.','estilo-indirecto-informacion',hint='informar'),
 build(s+'.ex04','Los historiadores explican que los cimarrones firmaron tratados de paz con los holandeses.','Historians explain that the maroons signed peace treaties with the Dutch.','estilo-indirecto-informacion'),
 dlg(s+'.ex05','¿Qué lengua oficial tiene Surinam?','','Gracias, ahora lo sé.',
  ['Según el texto, el neerlandés es la lengua oficial de Surinam.','Según el texto, el inglés es la lengua oficial, como en Guyana.','Según el texto, el criollo es la lengua oficial, como en Haití.'],V),
 dict_(s+'.ex06','Según los historiadores, miles de africanos esclavizados huyeron de las plantaciones.','According to historians, thousands of enslaved Africans escaped from the plantations.','estilo-indirecto-informacion')])
n=story(s,'Surinam: cimarrones, trabajadores contratados y muchas lenguas','Suriname is a former Dutch colony where Dutch is official and many languages are spoken; the text reports what historians say about the maroons, the contract workers from Asia and the country today.',[
 'Surinam está en la costa norte de América del Sur, entre Guyana y la Guayana Francesa. Fue una colonia de los Países Bajos hasta 1975, y hoy el neerlandés es su lengua oficial: es el único país independiente de América donde lo es. En la calle, sin embargo, mucha gente habla sranan tongo, una lengua criolla que sirve para entenderse entre comunidades. También se hablan sarnami, javanés, lenguas indígenas y lenguas de los cimarrones.',
 'Durante la época colonial, los holandeses llevaron a Surinam a muchos africanos esclavizados para trabajar en las plantaciones de azúcar. Según los historiadores, miles de ellos huyeron al interior de la selva. Allí formaron comunidades libres: son los cimarrones. Hoy se habla de seis grupos principales, entre ellos los ndyuka, los saramaka y los matawai. Los historiadores explican que en el siglo XVIII varios de estos grupos firmaron tratados de paz con los holandeses y que esos tratados reconocieron su libertad.',
 'La esclavitud se abolió en 1863, pero los antiguos esclavizados tuvieron que seguir trabajando en las plantaciones durante diez años más bajo la supervisión del Estado. Los dueños de las plantaciones buscaron entonces trabajadores contratados en Asia: desde 1873 llegaron personas de la India, y desde 1890, de la isla de Java.',
 'Por eso la población de Surinam es hoy muy diversa. Las comunidades celebran fiestas distintas, como el Divali hindú o el Keti Koti, que recuerda el fin de la esclavitud el 1 de julio. En el centro de Paramaribo, que es Patrimonio de la Humanidad desde 2002, una sinagoga y una mezquita están una al lado de la otra. En 2024 la prensa informó de que se aprobó un gran proyecto de petróleo en el mar frente a la costa, y en julio de 2025 el parlamento eligió presidenta a Jennifer Geerlings-Simons, la primera mujer en el cargo.'],
 [('According to the text, which is the official language of Suriname?',['El neerlandés.','El inglés.','El sranan tongo.'],'The first paragraph says Dutch is official.'),
  ('What do historians explain about the 18th century?',['Que varios grupos de cimarrones firmaron tratados de paz con los holandeses.','Que los cimarrones volvieron a las plantaciones.','Que los holandeses dejaron Surinam.'],'The second paragraph reports the historians\' explanation.'),
  ('Where did the contract workers come from after 1863?',['De la India y de la isla de Java.','De Guyana y de la Guayana Francesa.','De las islas del Caribe y de Brasil.'],'The third paragraph names India and Java.')])
print(s,n)

# ---------- 04
s='b2-guyanas-04'
lesson(s,'Guyana and French Guiana: oil, a spaceport and a border dispute',
 'Talk about Guyana\'s oil, the Essequibo dispute and the spaceport at Kourou, using imagined situations with si + imperfect subjunctive.',
 'hypothetical conditions with si + imperfect subjunctive',
 ['In this lesson you read about two neighbours: Guyana, an English-speaking country that found oil offshore, and French Guiana, part of France, where Europe launches its rockets. You will also read the two positions in the dispute between Venezuela and Guyana over the Essequibo, and the steps of the court case.',
  'The grammar is one you know: *si* + imperfect subjunctive, for imagined situations. '+TAIL+NOTE],
 ['I can say what would happen in an imagined situation with *si* + imperfect subjunctive and the conditional.',
  'I can say what each side claims in the Essequibo dispute, without taking sides.',
  'I can use the new words for rockets, fuel and oil fields.'])
write_gr(s,None,'If the Oil Ran Out: Imagined Situations',[
 T('You know *si* + imperfect subjunctive from B1 Unit 4: *Si yo fuera tú, hablaría con el profesor*. You imagine a situation that is unlikely or contrary to fact, and the result goes in the conditional. Oil economies and rocket launches are full of "what would happen if" questions.','What you already know'),
 TB('If + imperfect subjunctive, then the conditional',[
  ('Si el petróleo se acabara, la economía de Guyana tendría que cambiar.','if the oil ran out, the economy would have to change'),
  ('Si los cohetes salieran de Europa, necesitarían más combustible.','if the rockets left from Europe, they would need more fuel'),
  ('Si no hubiera petróleo, Guyana dependería más del oro.','*hubiera* is the imperfect subjunctive of *haber*: if there were no oil'),
  ('Si el centro espacial estuviera lejos del ecuador, gastaría más combustible.','*estuviera* from *estuvieron*: if the centre were far from the equator')]),
 EX([('Si el petróleo se acabara, la economía de Guyana tendría que cambiar.','If the oil ran out, the economy of Guyana would have to change.'),
     ('Si el centro espacial estuviera en Europa, los cohetes gastarían más combustible.','If the space centre were in Europe, the rockets would use more fuel.'),
     ('Si no hubiera petróleo, la economía de Guyana dependería más del azúcar, del arroz y del oro.','If there were no oil, the economy of Guyana would depend more on sugar, rice and gold.'),
     ('Si Guyana tuviera más ingresos, podría construir más escuelas.','If Guyana had more income, it could build more schools.')]),
 TIP('Never put the conditional after *si*: *si se acabara*, not *si se acabaría*. The verb after *si* agrees with its subject: *si el petróleo se acabara* (singular), *si los cohetes salieran* (plural). For things that are true or likely, use the real *si* clauses you know from B1 Unit 8 instead.')])
write_voc(s,None,'Oil and the spaceport','Rockets, fuel and oil fields',[
 ('el cohete','rocket','noun'),('el combustible','fuel','noun'),('el yacimiento','field, deposit (oil)','noun'),('el barril','barrel','noun')])
write_ex(s,[
 match(s+'.ex01',[('el cohete','rocket'),('el combustible','fuel'),('el yacimiento','field, deposit (oil)'),('el barril','barrel')],V),
 mc(s+'.ex02','Which sentence says "If the rockets left from Europe, they would need more fuel"?',
  ['Si los cohetes salieran de Europa, necesitarían más combustible.','Si los cohetes saldrían de Europa, necesitarían más combustible.','Si los cohetes salieron de Europa, necesitarían más combustible.'],teaches='hypothetical-structures'),
 fill(s+'.ex03','Si el petróleo se __, la economía de Guyana tendría que cambiar.','acabara','If the oil ran out, the economy of Guyana would have to change.','hypothetical-structures',answers=['acabara','acabase']),
 build(s+'.ex04','Si no hubiera petróleo, la economía de Guyana dependería más del azúcar, del arroz y del oro.','If there were no oil, the economy of Guyana would depend more on sugar, rice and gold.','hypothetical-structures'),
 dlg(s+'.ex05','¿Qué hay en Kourou, en la Guayana Francesa?','','Qué interesante.',
  ['Hay un centro espacial desde donde salen cohetes europeos.','Hay un gran lago donde nacen los ríos de Guyana.','Hay un puente que une Brasil con Surinam.'],V),
 dict_(s+'.ex06','Si el centro espacial estuviera en Europa, los cohetes gastarían más combustible.','If the space centre were in Europe, the rockets would use more fuel.','hypothetical-structures')])
n=story(s,'Guyana y la Guayana Francesa: petróleo, cohetes y una disputa','Guyana found oil offshore in 2015 and French Guiana hosts Europe\'s spaceport; the text also presents Venezuela\'s and Guyana\'s positions on the Essequibo and the steps of the court case.',[
 'Guyana es un país independiente desde 1966, y su lengua oficial es el inglés. En 2015 se anunció un gran descubrimiento de petróleo en el mar frente a su costa, en el bloque Stabroek, y la producción empezó en 2019. Las reservas superan los once mil millones de barriles. Según el Fondo Monetario Internacional, la economía de Guyana fue de las que más crecieron en el mundo entre 2022 y 2024. Si el petróleo se acabara, la economía tendría que cambiar; por eso el gobierno creó un fondo para guardar parte de los ingresos.',
 'El petróleo ha reavivado una disputa antigua. Venezuela reclama el Esequibo, una región de unos 160.000 kilómetros cuadrados que Guyana administra y que es casi dos tercios de su territorio. Venezuela dice que el laudo de París de 1899, que fijó la frontera, no es válido, y que el Acuerdo de Ginebra de 1966 pide una solución negociada. Guyana dice que el laudo fijó la frontera y que sigue siendo válido; en 2018 pidió a la Corte Internacional de Justicia que lo confirmara. Venezuela no reconoce la competencia de la Corte. En abril de 2023 la Corte dijo que tenía competencia para examinar el caso. En diciembre de 2023, Venezuela hizo un referendo sobre el Esequibo, y los presidentes de los dos países firmaron en San Vicente la Declaración de Argyle, en la que se comprometieron a no usar la fuerza. El caso continúa en la Corte.',
 'La Guayana Francesa es un departamento de Francia desde 1946: su lengua oficial es el francés y su moneda es el euro. Desde 1968 funciona allí el centro espacial de Kourou, desde donde se lanzan cohetes europeos. Está a unos cinco grados del ecuador, y por eso los cohetes necesitan menos combustible para llegar a órbita que si salieran de Europa.'],
 [('What does Venezuela say about the 1899 award, according to the text?',['Que no es válido, y que el Acuerdo de Ginebra de 1966 pide una solución negociada.','Que fijó la frontera y debe respetarse.','Que lo firmó en 2018 con Guyana.'],'The second paragraph presents Venezuela\'s position.'),
  ('What did Guyana ask the International Court of Justice to do in 2018?',['Confirmar que el laudo de 1899 sigue siendo válido.','Cerrar el centro espacial de Kourou.','Dividir el petróleo con Venezuela.'],'The second paragraph presents Guyana\'s request.'),
  ('Why do rockets launched from Kourou need less fuel?',['Porque Kourou está cerca del ecuador.','Porque Kourou está junto al Esequibo.','Porque los cohetes son más pequeños que en Europa.'],'The third paragraph links the location to fuel.')])
print(s,n)

# ---------- 05
s='b2-guyanas-05'
lesson(s,'CARICOM, bridges and borders: Belize and the Guianas look outward',
 'Describe how Belize and the Guianas connect with their neighbours, and where borders are still in question, with aun cuando.',
 'concessive clauses with aun cuando and the subjunctive',
 ['In this lesson you read about how Belize, Guyana and Suriname belong to CARICOM, the Caribbean community, and how bridges and agreements are starting to link them with Brazil and with the Amazon countries. You also read where borders are still in question.',
  'The grammar is one you know: *aun cuando* "even when, even if". '+TAIL+NOTE],
 ['I can grant a point with *aun cuando* and the indicative for a fact, or the subjunctive for a possibility.',
  'I can say where CARICOM has its headquarters and which bridges were opened in 2009 and 2017.',
  'I can use the new words for headquarters, bridges and borders.'])
write_gr(s,None,'Even When: Aun Cuando',[
 T('You know *aun cuando* "even when, even if" from B2 Unit 8. It follows the same rule as *aunque*: the indicative for a fact, the subjunctive for a possibility. It is more formal and more emphatic, which suits the language of treaties, bridges and borders.','What you already know'),
 TB('Fact or possibility?',[
  ('Aun cuando Guyana y Surinam están cerca de Brasil, durante mucho tiempo no tuvieron carreteras hacia él.','a fact: indicative (they are close)'),
  ('Aun cuando se construyan más puentes, la selva seguirá siendo difícil de cruzar.','a possibility: subjunctive (more bridges may be built)'),
  ('Aun cuando tienen idiomas distintos, los países de CARICOM trabajan juntos.','a fact: indicative (they have different languages)'),
  ('Aunque tienen idiomas distintos, los países de CARICOM trabajan juntos.','the everyday version, with *aunque*')]),
 EX([('Aun cuando Brasil y Guyana son vecinos, hasta 2009 no hubo un puente sobre el río Takutu.','Even though Brazil and Guyana are neighbours, until 2009 there was no bridge over the Takutu river.'),
     ('Aun cuando se construyan más puentes, la selva seguirá siendo difícil de cruzar.','Even if more bridges are built, the jungle will remain hard to cross.'),
     ('Aun cuando tienen idiomas distintos, los países de CARICOM trabajan juntos.','Even though they have different languages, the CARICOM countries work together.'),
     ('Los dos países seguirán hablando aun cuando no estén de acuerdo.','The two countries will keep talking even if they do not agree.')]),
 TIP('Ask whether the speaker presents the obstacle as a real fact (indicative) or as something possible that will not change the plan (subjunctive). Write *aun* without an accent in *aun cuando*; with an accent, *aún* means "still".')])
write_voc(s,None,'Bridges and borders','Headquarters, bridges, borders',[
 ('la sede','headquarters, seat','noun'),('el puente','bridge','noun'),('la frontera','border','noun'),('el bloque','bloc, block','noun')])
write_ex(s,[
 match(s+'.ex01',[('la sede','headquarters, seat'),('el puente','bridge'),('la frontera','border'),('el bloque','bloc, block')],V),
 mc(s+'.ex02','Which sentence says "Even if more bridges are built, the jungle will remain hard to cross"?',
  ['Aun cuando se construyan más puentes, la selva seguirá siendo difícil de cruzar.','Aun cuando se construyen más puentes, la selva seguirá siendo difícil de cruzar.','Aun cuando se construyeran más puentes, la selva seguirá siendo difícil de cruzar.'],teaches='concesivas-aun-cuando'),
 fill(s+'.ex03','Aun cuando Guyana y Surinam __ cerca de Brasil, durante mucho tiempo no tuvieron carreteras hacia él.','están','Even though Guyana and Suriname are close to Brazil, for a long time they had no roads to it.','concesivas-aun-cuando'),
 build(s+'.ex04','Aun cuando tienen idiomas distintos, los países de CARICOM trabajan juntos.','Even though they have different languages, the CARICOM countries work together.','concesivas-aun-cuando'),
 dlg(s+'.ex05','¿Dónde está la sede de CARICOM?','','Gracias, ahora lo sé.',
  ['Está en Georgetown, la capital de Guyana.','Está en Paramaribo, la capital de Surinam.','Está en Kourou, junto al centro espacial.'],V),
 dict_(s+'.ex06','Aun cuando Brasil y Guyana son vecinos, hasta 2009 no hubo un puente sobre el río Takutu.','Even though Brazil and Guyana are neighbours, until 2009 there was no bridge over the Takutu river.','concesivas-aun-cuando')])
n=story(s,'CARICOM, puentes y fronteras','Belize, Guyana and Suriname belong to CARICOM, new bridges link the Guianas with Brazil, and several border disputes are before courts or were settled by arbitration.',[
 'Belice, Guyana y Surinam están en América Latina por su geografía, pero tienen otras historias: fueron colonias británicas o neerlandesas, y sus lenguas oficiales son el inglés y el neerlandés. Por eso, durante mucho tiempo miraron hacia el Caribe más que hacia sus vecinos de lengua española o portuguesa.',
 'Los tres son miembros de la Comunidad del Caribe, CARICOM, que se fundó en 1973 y tiene su sede en Georgetown, la capital de Guyana. Belice entró en 1974 y Surinam en 1995. Los países de CARICOM tratan juntos temas como el comercio, la salud y el cambio climático. Aun cuando tienen idiomas distintos, trabajan juntos.',
 'Brasil, que comparte frontera con Guyana, Surinam y la Guayana Francesa, ha empezado a cambiar la situación. En 2009 se abrió un puente sobre el río Takutu, entre las ciudades de Bonfim, en Brasil, y Lethem, en Guyana. En 2017 se inauguró otro sobre el río Oiapoque, entre Brasil y la Guayana Francesa. Aun cuando la selva sigue siendo una barrera, estas obras abrieron conexiones por carretera entre Brasil y la costa atlántica de las Guayanas.',
 'Los países de la Amazonia también cooperan en la Organización del Tratado de Cooperación Amazónica, que reúne a ocho países, entre ellos Guyana y Surinam, para proteger la selva.',
 'Las fronteras siguen siendo motivo de disputa. Guatemala reclama una parte del territorio de Belice, y Venezuela reclama el Esequibo a Guyana; las dos disputas están en la Corte Internacional de Justicia. Surinam y Guyana discutieron durante años su frontera marítima, y en 2007 un tribunal arbitral internacional resolvió el caso.'],
 [('Where is the headquarters of CARICOM, according to the text?',['En Georgetown, la capital de Guyana.','En Paramaribo, la capital de Surinam.','En Belmopán, la capital de Belice.'],'The second paragraph names Georgetown.'),
  ('What was opened in 2009?',['Un puente sobre el río Takutu, entre Brasil y Guyana.','Un puente sobre el río Oiapoque.','La sede de CARICOM.'],'The third paragraph dates the Takutu bridge to 2009.'),
  ('How was the maritime dispute between Suriname and Guyana resolved?',['En 2007, con la decisión de un tribunal arbitral internacional.','En 2019, con un referendo en los dos países.','En 1973, con la fundación de CARICOM.'],'The last paragraph reports the 2007 arbitration.')])
print(s,n)

# ---------- consolidation
s='b2-guyanas-consolidation'
lesson(s,'Belize, Suriname and the Guianas: Unit Review','Review Belize, the Guiana Shield, Suriname, Guyana and French Guiana, and the links between these countries, with the grammar you used to talk about them.',
 'review: passive with ser, cleft sentences, citing sources, si + imperfect subjunctive, aun cuando',
 [],[],
 ['I can say what was done, and by whom, with *ser* + past participle.',
  'I can put one idea in the spotlight with a cleft sentence.',
  'I can cite a source with *según* and *explicar que*.',
  'I can say what would happen in an imagined situation with *si* + imperfect subjunctive.',
  'I can grant a point with *aun cuando*.'])
p=R+'lessons/b2/b2-guyanas-consolidation.json'; d=rj(p)
for sec in d['sections']:
    if sec['type']=='goal': sec['items']=['I can review what I learned about Belize, Suriname and the Guianas.','I can use the passive with *ser*, cleft sentences, *según*, *si* + imperfect subjunctive and *aun cuando*.','I can say which languages are spoken in these countries.','I can state two sides of a dispute without taking sides.']
wj(p,d)
write_ex(s,[
 match(s+'.ex01',[('el tepuy','tepui (flat-topped mountain)'),('el cimarrón','maroon (escaped enslaved person)'),('el cohete','rocket'),('la sede','headquarters, seat')],V),
 mc(s+'.ex02','Which sentence is correct?',['El centro de Paramaribo fue declarado Patrimonio de la Humanidad en 2002.','El centro de Paramaribo fue declarada Patrimonio de la Humanidad en 2002.','El centro de Paramaribo fue declarado Patrimonio de la Humanidad de 2002.'],teaches='ser-passive'),
 fill(s+'.ex03','Fue en 1975 __ Surinam se hizo independiente.','cuando','It was in 1975 that Suriname became independent.','oraciones-hendidas-enfasis'),
 fill(s+'.ex04','__ los historiadores, los cimarrones firmaron tratados de paz con los neerlandeses.','Según','According to historians, the maroons signed peace treaties with the Dutch.','estilo-indirecto-informacion'),
 build(s+'.ex05','Si no hubiera puentes, el viaje desde Brasil sería mucho más difícil.','If there were no bridges, the journey from Brazil would be much harder.','hypothetical-structures'),
 mc(s+'.ex06','Which sentence is correct?',['Aun cuando haya problemas en la frontera, los dos países seguirán hablando.','Aun cuando hay problemas en la frontera, los dos países seguirán hablando.','Aun cuando hubieran problemas en la frontera, los dos países seguirán hablando.'],teaches='concesivas-aun-cuando'),
 mc(s+'.ex07','According to the texts, what does Venezuela say about the 1899 award on the Essequibo?',['Que no es válido, y que el Acuerdo de Ginebra de 1966 pide una solución negociada.','Que fijó la frontera y que sigue siendo válido.','Que fue confirmado por la Corte Internacional de Justicia en 2018.'],cat='reading'),
 dict_(s+'.ex08','La música garífuna fue proclamada obra maestra por la UNESCO en 2001.','Garifuna music was proclaimed a masterpiece by UNESCO in 2001.','ser-passive')])
