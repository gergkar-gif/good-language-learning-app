from lib import *
U='b2-boliviaaltiplano'; V='b2-bolivia-altiplano-vocab'
def S(n): return f'{U}-{n}'
EN='You know *%s* from %s.'
# ---------- 01
s=S('01')
vocab(s,[('el altiplano','high plateau','noun'),('la totora','reed that grows in the lake','noun'),('el bofedal','high wetland where animals graze','noun'),('la embarcación','boat','noun'),('la helada','night frost','noun')],'The high plateau and Lake Titicaca')
grammar(s,'Who and Which: Relative Clauses on the High Plateau',[
 {'type':'text','title':'What you already know','content':"You know relative clauses with *que* and *quien* from B1 Unit 5. A relative clause adds information about a noun without starting a new sentence: *la planta que crece en el agua*. *Que* works for things, animals and people. *Quien* is only for people, and it is most useful after a preposition: *la guía con quien viajamos*. Here you use them to describe the high plateau and Lake Titicaca."},
 {'type':'table','title':'Que and quien at work','rows':[
  ['El lago Titicaca, que está entre Bolivia y Perú, es muy alto.','Lake Titicaca, which is between Bolivia and Peru, is very high. (*que* + a comma: extra information)'],
  ['La totora es una planta que crece en el agua.','Totora is a plant that grows in the water. (*que* says which plant)'],
  ['Los aymaras que viven junto al lago cultivan papa.','The Aymara people who live next to the lake grow potatoes. (*que* for people)'],
  ['La guía con quien viajamos conoce bien la isla.','The guide we travelled with knows the island well. (*quien* after a preposition)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Las llamas pastan en los bofedales, que son humedales de altura.','english':'Llamas graze in the bofedales, which are high wetlands.'},
  {'spanish':'Las comunidades que viven junto al lago cultivan papa y quinua.','english':'The communities that live next to the lake grow potatoes and quinoa.'},
  {'spanish':'La Isla del Sol, que se visita en barco, tiene ruinas de piedra.','english':'The Island of the Sun, which you visit by boat, has stone ruins.'}]},
 {'type':'tip','content':"Never leave *que* out, as English sometimes does: *the plants we saw* is *las plantas que vimos*. The verb after *que* agrees with the noun before it: *los aymaras que viven*, not *que vive*."}])
lesson(s,'The high plateau and Lake Titicaca: a lake that keeps the frost away','Describe the Bolivian high plateau and Lake Titicaca, using relative clauses with que and quien.','relative clauses with que and quien',
 ['I can describe the high plateau and Lake Titicaca with relative clauses introduced by *que* and *quien*.','I can say why families by the lake can grow crops at that altitude.','I can name what totora, bofedales and llamas are in Spanish.'])
ex(s,[
 match(s,1,[['el altiplano','high plateau'],['la totora','reed that grows in the lake'],['el bofedal','high wetland where animals graze'],['la embarcación','boat'],['la helada','night frost']],V),
 fill(s,2,'La totora es una planta __ crece en el agua del lago.','que','Totora is a plant that grows in the water of the lake.','relative-clauses'),
 mc(s,3,'Which sentence says: "The Aymara people who live next to the lake grow potatoes"?',['Los aymaras que viven junto al lago cultivan papa.','Los aymaras viven junto al lago cultivan papa.','Los aymaras que vive junto al lago cultivan papa.','Los aymaras lo que viven junto al lago cultivan papa.'],'relative-clauses',ds={3:'relativas-preposicion-el-que'}),
 build(s,4,'El lago Titicaca, que está entre Bolivia y Perú, es muy alto.','Lake Titicaca, which is between Bolivia and Peru, is very high.','relative-clauses'),
 dlg(s,5,[('Meg','En el documental hablan de los bofedales. ¿Qué son?'),('Carlos','Son humedales _____ están a mucha altura.')],['que','quien','cuyo'],'relative-clauses',ds={2:'relativo-posesivo-cuyo'}),
 dict_(s,6,'Las comunidades que viven junto al lago cultivan papa y quinua.','The communities that live next to the lake grow potatoes and quinoa.','relative-clauses')])
story(s,'El altiplano y el lago Titicaca','The Bolivian high plateau lies about four thousand metres up; Lake Titicaca softens the frosts, and totora reed, llamas and the Aymara people shape life around it.',[
 "El altiplano es una meseta alta que se extiende entre dos cordilleras de los Andes, la Occidental y la Real. Está a unos cuatro mil metros sobre el nivel del mar. Por eso el aire tiene poco oxígeno, el sol es muy fuerte durante el día y las noches son muy frías: la temperatura baja de cero grados.",
 "En el norte del altiplano está el lago Titicaca, que Bolivia comparte con Perú. Tiene más de ocho mil kilómetros cuadrados y, según se dice con frecuencia, es el lago navegable más alto del mundo. El agua guarda el calor del día y suaviza las heladas de las orillas. Por eso las familias que viven cerca del lago pueden cultivar papa, quinua, habas y cebada.",
 "Para los incas, el lago era un lugar sagrado. Según una tradición inca, Manco Cápac y Mama Ocllo salieron del lago para fundar su imperio. La Isla del Sol, que se visita en barco desde Copacabana, conserva terrazas de cultivo y ruinas de piedra de esa época.",
 "En las orillas crece la totora, una planta que se usa desde hace siglos para hacer techos y embarcaciones. En el lado peruano del lago, el pueblo uro vive en islas hechas con esa misma planta.",
 "Lejos del lago, en los bofedales, que son zonas húmedas de altura, comen las llamas y las alpacas. Con la lana de estos animales se hacen mantas, ponchos y otras prendas. Los aymaras, que viven en esta región desde hace siglos, mantienen su idioma y sus fiestas."],
 [("Why can families near Lake Titicaca grow potatoes and barley?",["El agua del lago guarda el calor y suaviza las heladas.","El lago está a nivel del mar.","En el altiplano nunca hace frío."],"The second paragraph explains it."),
  ("What is totora used for?",["Para hacer techos y embarcaciones.","Para hacer monedas de plata.","Para hacer lana de llama."],"The fourth paragraph."),
  ("According to an Inca tradition, who came out of the lake?",["Manco Cápac y Mama Ocllo.","Los uros y los aymaras.","Los primeros españoles."],"The third paragraph.")])
# ---------- 02
s=S('02')
vocab(s,[('el socavón','mine tunnel','noun'),('la mita','forced labour system of the colonial period','noun'),('la plata','silver','noun'),('el minero','miner','noun'),('acuñar','to mint (coins)','verb')],'Potosí and the Cerro Rico')
grammar(s,'Estar + Participle: What Potosí Looks Like Today',[
 {'type':'text','title':'What you already know','content':"You know *estar* + participle from B2 Unit 20. *Ser* + participle tells the action (*Potosí fue fundada en 1545*), and *estar* + participle tells the result you can see now (*La casa está convertida en museo*). The participle agrees with the subject, like an adjective. The history of Potosí gives you both: what happened, and what is left today."},
 {'type':'table','title':'Action and result in Potosí','rows':[
  ['Potosí fue fundada en 1545.','Potosí was founded in 1545. (the action)'],
  ['La Casa de la Moneda está convertida en museo.','The Mint is turned into a museum. (the result, now)'],
  ['El cerro está perforado por muchos túneles.','The hill is riddled with tunnels. (the result)'],
  ['La ciudad está inscrita en la lista de la UNESCO desde 1987.','The city has been on the UNESCO list since 1987. (the result)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'La ciudad está situada al pie del Cerro Rico.','english':'The city is situated at the foot of the Cerro Rico.'},
  {'spanish':'Muchas iglesias coloniales están conservadas.','english':'Many colonial churches are preserved.'},
  {'spanish':'La plata fue llevada a la Casa de la Moneda.','english':'The silver was taken to the Mint. (the action)'}]},
 {'type':'tip','content':"Ask yourself: am I telling what happened, or what I can see now? *Fue convertida* is an event; *está convertida* is the state. A time word such as *hoy*, *ahora* or *desde* points to *estar*."}])
lesson(s,'Potosí and the Cerro Rico: the silver mountain','Tell the story of Potosí and the silver of the Cerro Rico, using estar + participle for the result.','resultative state passive with estar + participle',
 ['I can say what Potosí looks like today with *estar* + participle.','I can tell what the mita was and where the silver went.','I can name the main words for mining and coins in Spanish.'])
ex(s,[
 match(s,1,[['el socavón','mine tunnel'],['la mita','forced labour system of the colonial period'],['la plata','silver'],['el minero','miner'],['acuñar','to mint (coins)']],V),
 fill(s,2,'Hoy la Casa de la Moneda de Potosí __ convertida en museo.','está','Today the Mint of Potosí is turned into a museum.','pasiva-estado-estar-participio'),
 mc(s,3,'Which sentence tells you that the mint is a museum right now?',['La Casa de la Moneda está convertida en museo.','La Casa de la Moneda fue convertida en museo.','La Casa de la Moneda estaba convertida en museo.','La Casa de la Moneda será convertida en museo.'],'pasiva-estado-estar-participio',ds={1:'ser-passive',3:'ser-passive'}),
 build(s,4,'La ciudad de Potosí está inscrita en la lista de la UNESCO.','The city of Potosí is on the UNESCO list.','pasiva-estado-estar-participio'),
 dlg(s,5,[('Meg','¿Podemos entrar ahora al museo?'),('Carlos','Sí, el museo _____ hasta las seis.')],['está abierto','fue abierto','está abriendo','está abierta'],'pasiva-estado-estar-participio',ds={1:'ser-passive',2:'progressive'}),
 dict_(s,6,'El centro histórico de Potosí está protegido por la UNESCO.','The historic centre of Potosí is protected by UNESCO.','pasiva-estado-estar-participio')])
story(s,'Potosí y el Cerro Rico','Silver found in the Cerro Rico in 1545 made Potosí one of the largest cities of its time, at the cost of the mita, and the city is now a UNESCO World Heritage Site.',[
 "Potosí es una ciudad de Bolivia que está a más de cuatro mil metros de altura, al pie del Cerro Rico. En 1545 los españoles encontraron plata en esa montaña, y ese mismo año fundaron la Villa Imperial.",
 "En pocos años la ciudad creció muchísimo. Según algunas estimaciones, hacia 1650 tenía unos ciento sesenta mil habitantes y era una de las ciudades más grandes del mundo de su época. De allí viene la expresión «valer un Potosí», que se usa para hablar de algo de mucho valor.",
 "La plata se sacaba con trabajo indígena. En la década de 1570, el virrey Francisco de Toledo organizó la mita, un sistema por el que las comunidades indígenas de la región debían enviar por turnos a un grupo de hombres a trabajar en las minas. Muchos de ellos murieron o se enfermaron por las duras condiciones de los socavones.",
 "El metal se llevaba a la Casa de la Moneda, donde se acuñaban monedas, entre ellas el «real de a ocho», que se usó en muchos países. El edificio actual se construyó en el siglo XVIII y hoy está convertido en museo.",
 "La ciudad conserva muchas iglesias y casas de la época colonial, y desde 1987 está en la lista del Patrimonio Mundial de la UNESCO. En el Cerro Rico todavía trabajan mineros, muchos de ellos en cooperativas. Antes de entrar en el socavón, algunos dejan hojas de coca, alcohol o cigarrillos a una figura llamada el Tío, a quien piden protección."],
 [("When was silver found in the Cerro Rico, according to the text?",["En 1545.","En 1650.","En 1987."],"The first paragraph."),
  ("What was the mita?",["Un sistema de trabajo por turnos en las minas.","Una moneda de plata de ocho reales.","Una iglesia colonial de Potosí."],"The third paragraph."),
  ("What is the Mint of Potosí today?",["Un museo.","Una iglesia.","Una mina."],"The fourth paragraph.")])
# ---------- 03
s=S('03')
vocab(s,[('el teleférico','cable car','noun'),('el cholet','brightly coloured building of El Alto','noun'),('la cholita','Aymara woman in traditional dress','noun'),('la pollera','wide pleated skirt','noun'),('el bombín','bowler hat','noun')],'La Paz and El Alto')
grammar(s,'It Is Not That…, It Is That…: Correcting an Idea',[
 {'type':'text','title':'What you already know','content':"You know *no es que* + subjunctive, *sino que* + indicative from B2 Unit 5. It rejects a reason or an idea someone might assume, and gives the true one: *No es que no quiera, sino que no puedo*. The first part is not stated as a fact, so it takes the subjunctive; the second part is a fact, so it takes the indicative. It suits La Paz and El Alto, two cities people often mix up."},
 {'type':'table','title':'Correcting ideas about La Paz and El Alto','rows':[
  ['No es que El Alto sea un barrio de La Paz, sino que es otra ciudad.','It is not that El Alto is a district of La Paz; it is another city.'],
  ['No es que el teleférico sea solo para turistas, sino que lo usan muchas personas para ir al trabajo.','It is not that the cable car is only for tourists; many people use it to go to work.'],
  ['No es que se vistan así solo en las fiestas, sino que muchas llevan pollera todos los días.','It is not that they dress like this only at festivals; many wear the *pollera* every day.'],
  ['No era que estuvieran lejos, sino que la cuesta hacía largo el viaje.','It was not that they were far apart; the slope made the journey long. (past: imperfect subjunctive, then imperfect)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'No es que El Alto sea una ciudad pequeña, sino que ha crecido muy rápido.','english':'It is not that El Alto is a small city; it has grown very fast.'},
  {'spanish':'No es que La Paz sea la capital constitucional, sino que es la sede del gobierno.','english':'It is not that La Paz is the constitutional capital; it is the seat of government.'},
  {'spanish':'No es que los cholets sean solo casas, sino que tienen tiendas y salas.','english':'It is not that cholets are only houses; they have shops and halls.'}]},
 {'type':'tip','content':"Use *sino que* before a conjugated verb. If you only change one word, *sino* alone is enough: *No es un barrio, sino una ciudad*. *Pero* would only add a limit; *sino que* replaces the wrong idea."}])
lesson(s,'La Paz and El Alto: two cities, one cable-car system','Describe La Paz, El Alto, the cholets and the cholitas, correcting ideas with no es que… sino que….','refutation with no es que… sino que',
 ['I can correct a wrong idea about La Paz and El Alto with *no es que… sino que…*.','I can say what Mi Teleférico and the cholets are.','I can name the traditional dress of the cholitas in Spanish.'])
ex(s,[
 match(s,1,[['el teleférico','cable car'],['el cholet','brightly coloured building of El Alto'],['la cholita','Aymara woman in traditional dress'],['la pollera','wide pleated skirt'],['el bombín','bowler hat']],V),
 fill(s,2,'No es que El Alto sea un barrio de La Paz, __ que es otra ciudad.','sino','It is not that El Alto is a district of La Paz; it is another city.','refutacion-no-es-que-sino'),
 mc(s,3,'Which sentence says: "It is not that the cable car is only for tourists; many people use it to go to work"?',['No es que el teleférico sea solo para turistas, sino que lo usan muchas personas para ir al trabajo.','No es que el teleférico es solo para turistas, sino que lo usan muchas personas para ir al trabajo.','No es que el teleférico sea solo para turistas, sino que lo usen muchas personas para ir al trabajo.','No es que el teleférico sea solo para turistas, pero lo usan muchas personas para ir al trabajo.'],'refutacion-no-es-que-sino',ds={3:'sino-vs-pero'}),
 build(s,4,'No es que El Alto sea un barrio, sino que es una ciudad.','It is not that El Alto is a district; it is a city.','refutacion-no-es-que-sino'),
 dlg(s,5,[('Meg','¿Las cholitas se visten así solo para las fiestas?'),('Carlos','No es que se _____ así solo en las fiestas, sino que muchas llevan pollera todos los días.')],['vistan','visten','vistieran'],'refutacion-no-es-que-sino',ds={2:'imperfect-subjunctive-forms'}),
 dict_(s,6,'No es que El Alto sea una ciudad pequeña, sino que ha crecido muy rápido.','It is not that El Alto is a small city; it has grown very fast.','refutacion-no-es-que-sino')])
story(s,'La Paz y El Alto','La Paz sits in a deep valley and El Alto above it on the plateau; a cable-car network links them, and El Alto is known for its colourful cholets and for the Aymara women who wear the pollera.',[
 "La Paz está en un valle profundo de los Andes, a unos tres mil seiscientos metros de altura, y sobre la ciudad se ve el nevado Illimani. Es la sede del gobierno de Bolivia, aunque la capital constitucional del país es Sucre.",
 "Encima del valle, en el borde del altiplano, está El Alto, a más de cuatro mil metros. No es un barrio de La Paz, sino una ciudad con su propio gobierno municipal. Muchos de sus habitantes son aymaras o descendientes de familias que llegaron del campo. En octubre de 2003, las protestas de El Alto tuvieron un papel importante en la crisis que terminó con la renuncia del presidente de entonces.",
 "Durante años, ir de una ciudad a otra por carretera era lento. En 2014 se abrieron las primeras líneas de Mi Teleférico, un sistema de cabinas colgadas de cables. Se presenta como la red urbana de teleféricos más larga del mundo, y lo usan muchas personas para ir al trabajo o a estudiar.",
 "En El Alto hay edificios de colores muy vivos que se llaman «cholets», una palabra que viene de «cholo» y «chalé». El arquitecto Freddy Mamani ayudó a hacerlos famosos. Tienen varios pisos: abajo suele haber tiendas y arriba, salas para fiestas. Sus formas geométricas recuerdan los diseños de los tejidos andinos.",
 "Muchas mujeres aymaras, las cholitas, llevan pollera, un chal y un sombrero bombín. Para algunas es la ropa de todos los días, y para otras, la ropa de las fiestas. Hoy se las ve en los mercados, en la política y en el deporte."],
 [("What is El Alto, according to the text?",["Una ciudad con su propio gobierno municipal.","Un barrio de La Paz.","La capital constitucional de Bolivia."],"The second paragraph."),
  ("When did the first lines of Mi Teleférico open?",["En 2014.","En 2003.","En 1987."],"The third paragraph."),
  ("What is on the lower floors of many cholets?",["Tiendas.","Salas de fiestas.","Minas de plata."],"The fourth paragraph.")])
