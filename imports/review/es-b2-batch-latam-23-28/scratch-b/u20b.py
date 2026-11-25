from lib import *
U='b2-boliviaaltiplano'; V='b2-bolivia-altiplano-vocab'
def S(n): return f'{U}-{n}'
# ---------- 04
s=S('04')
vocab(s,[('la coca','coca plant','noun'),('la hoja','leaf','noun'),('el acullico','chewing of coca leaves','noun'),('el narcotráfico','drug trafficking','noun'),('el cocalero','coca grower','noun')],'The coca leaf')
grammar(s,'Reporting What Others Say: The Coca Debate',[
 {'type':'text','title':'What you already know','content':"You know *según* + a source and reporting verbs such as *decir que* and *informar de que* from B1 Unit 13. Reporting keeps what a source says apart from what you say yourself. The coca leaf is a topic where people disagree, so it is useful to say clearly who says what."},
 {'type':'table','title':'Who says what about coca','rows':[
  ['Según la Constitución de 2009, la coca es patrimonio cultural de Bolivia.','According to the 2009 Constitution, coca is a cultural heritage of Bolivia.'],
  ['El gobierno boliviano dice que la coca no es cocaína.','The Bolivian government says that coca is not cocaine.'],
  ['Según Naciones Unidas, parte de la coca llega al narcotráfico.','According to the United Nations, part of the coca ends up in drug trafficking.'],
  ['Los cocaleros explican que la coca tiene usos tradicionales.','The coca growers explain that coca has traditional uses.']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'El gobierno informó de que la coca se vende legalmente en algunos mercados.','english':'The government reported that coca is sold legally in some markets.'},
  {'spanish':'Según la ley boliviana, la hoja de coca se puede usar en la vida diaria.','english':'According to Bolivian law, the coca leaf can be used in daily life.'},
  {'spanish':'Naciones Unidas dice que el control del cultivo es importante.','english':'The United Nations says that controlling the crop is important.'}]},
 {'type':'tip','content':"After *decir* and *explicar* use *que*, never *de que*: *dice que*. After *informar* use *de que*: *informó de que*. Put the source first (*según…*) so the reader knows whose words they are."}])
lesson(s,'The coca leaf: tradition, law and drug trafficking','Report what the government, the United Nations and coca growers say about the coca leaf, using según and reporting verbs.','reported statements and citing sources with según',
 ['I can say who says what about the coca leaf, using *según* and *dice que*.','I can tell the difference between the coca leaf and cocaine as people present it.','I can name the main words for coca and its traditional use in Spanish.'])
ex(s,[
 match(s,1,[['la coca','coca plant'],['la hoja','leaf'],['el acullico','chewing of coca leaves'],['el narcotráfico','drug trafficking'],['el cocalero','coca grower']],V),
 fill(s,2,'El gobierno dice __ la coca tiene usos tradicionales.','que','The government says that coca has traditional uses.','estilo-indirecto-informacion'),
 mc(s,3,'Which sentence says: "The government said that coca is not cocaine"?',['El gobierno dijo que la coca no es cocaína.','El gobierno dijo la coca no es cocaína.','El gobierno dijo que la coca no son cocaína.','El gobierno dijo de que la coca no es cocaína.'],'estilo-indirecto-informacion'),
 build(s,4,'Según la Constitución, la coca es patrimonio cultural de Bolivia.','According to the Constitution, coca is a cultural heritage of Bolivia.','estilo-indirecto-informacion'),
 dlg(s,5,[('Meg','¿Qué dice el gobierno de la coca?'),('Carlos','Dice _____ la coca no es cocaína.')],['que','de que','lo que'],'estilo-indirecto-informacion',ds={2:'relativas-preposicion-el-que'}),
 dict_(s,6,'Según el gobierno de Bolivia, la hoja de coca no es lo mismo que la cocaína.','According to the government of Bolivia, the coca leaf is not the same as cocaine.','estilo-indirecto-informacion')])
story(s,'La hoja de coca','The coca leaf has been used in the Andes for thousands of years; Bolivia protects its traditional use, while the United Nations reports that part of the crop feeds drug trafficking.',[
 "La hoja de coca se usa en los Andes desde hace miles de años. Muchas personas la mastican, una práctica llamada acullico, o la toman en infusión. Según quienes la usan, ayuda a soportar el trabajo y la altura. También se ofrece a la Pachamama, la madre tierra, en fiestas y ceremonias.",
 "La coca no es cocaína, pero la cocaína se fabrica a partir de la planta, y por eso el cultivo está regulado. Según Naciones Unidas, parte de la coca que se cultiva en la región llega al narcotráfico. El gobierno boliviano sostiene que la coca tiene usos tradicionales y que no debe confundirse con la cocaína.",
 "En 1961, una convención de Naciones Unidas puso la hoja de coca entre las sustancias controladas y pidió que, con el tiempo, se terminara con su masticación. En 2011 Bolivia salió de esa convención y en 2013 volvió a entrar con una reserva que permite el uso tradicional de la hoja en su territorio.",
 "La Constitución de 2009 protege la coca originaria y ancestral como patrimonio cultural. Evo Morales, que había sido dirigente de los cocaleros del Chapare, fue presidente de Bolivia de 2006 a 2019.",
 "Hoy el tema sigue en debate. Algunas personas defienden la tradición y el cultivo legal; otras piden más control para frenar el narcotráfico."],
 [("What is the acullico?",["Masticar hojas de coca.","Un tipo de moneda.","Una fiesta de El Alto."],"The first paragraph."),
  ("What does the Bolivian government say about coca, according to the text?",["Que tiene usos tradicionales y no debe confundirse con la cocaína.","Que debe desaparecer por completo del país.","Que es una planta traída de Europa."],"The second paragraph."),
  ("What did Bolivia do in 2013?",["Volvió a la convención de Naciones Unidas con una reserva.","Prohibió el cultivo de coca.","Salió de la convención de Naciones Unidas."],"The third paragraph.")])
# ---------- 05
s=S('05')
vocab(s,[('la wiphala','square flag of the Andean peoples','noun'),('plurinacional','plurinational, of many nations','adjective'),('la asamblea','assembly','noun'),('el referéndum','referendum','noun'),('el idioma','language','noun'),('la bandera','flag','noun')],'The Plurinational State')
grammar(s,'No Matter How Much: The Constitution of 2009',[
 {'type':'text','title':'What you already know','content':"You know *por más que* from B2 Unit 8: it means \"however much\" and takes the subjunctive when the amount or effort is open. *Por mucho que* and *por muy* + adjective + *que* work in the same way. When you tell something that really happened in the past, you may use the indicative. Here you use it for the Bolivian constitution of 2009 and the languages it recognises."},
 {'type':'table','title':'However much…','rows':[
  ['Por más que se hable castellano en las ciudades, los idiomas indígenas también son oficiales.','However much Spanish is spoken in the cities, the indigenous languages are official too.'],
  ['Por más que se discuta, la wiphala es uno de los símbolos del Estado.','However much it is discussed, the wiphala is one of the symbols of the State.'],
  ['Por muy antiguas que sean las costumbres de una comunidad, la Constitución las reconoce.','However old a community\'s customs are, the Constitution recognises them.'],
  ['Por más que hubo desacuerdos, el texto se aprobó en un referéndum en enero de 2009.','Although there were disagreements, the text was approved in a referendum in January 2009. (it really happened: indicative)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Por más que se hable de la ley, mucha gente no conoce su texto.','english':'However much the law is talked about, many people do not know its text.'},
  {'spanish':'Por mucho que cambie el gobierno, la Constitución sigue siendo la base del Estado.','english':'However much the government changes, the Constitution remains the basis of the State.'},
  {'spanish':'Por más que lo pidieron, la asamblea no cambió ese artículo.','english':'However much they asked for it, the assembly did not change that article.'}]},
 {'type':'tip','content':"*Por más que* often comes with a main clause that says the result stays the same. For the future or for general statements use the subjunctive (*por más que se hable*); for a past event that really happened you may use the indicative (*por más que hubo*)."}])
lesson(s,'The Plurinational State: the Constitution of 2009','Describe the Bolivian Constitution of 2009 and the Plurinational State, using por más que for concession.','concessive clauses with por más que + subjunctive',
 ['I can grant a point and still state my main idea with *por más que* + subjunctive.','I can say what the Constitution of 2009 recognises and where it was promulgated.','I can name the main words for the constitution, the assembly and the wiphala.'])
ex(s,[
 match(s,1,[['la wiphala','square flag of the Andean peoples'],['plurinacional','plurinational, of many nations'],['la asamblea','assembly'],['el referéndum','referendum'],['el idioma','language'],['la bandera','flag']],V),
 fill(s,2,'Por más que se __ castellano en las ciudades, los idiomas indígenas también son oficiales.','hable','However much Spanish is spoken in the cities, the indigenous languages are official too.','concesivas-por-mas-que',hint='hablar'),
 mc(s,3,'Which sentence says: "However much they disagree, the Constitution recognises 36 indigenous languages"?',['Por más que no estén de acuerdo, la Constitución reconoce 36 idiomas indígenas.','Por más que no estar de acuerdo, la Constitución reconoce 36 idiomas indígenas.','Por más no estén de acuerdo, la Constitución reconoce 36 idiomas indígenas.','Por más que no estarían de acuerdo, la Constitución reconoce 36 idiomas indígenas.'],'concesivas-por-mas-que',ds={3:'condicional-regular'}),
 build(s,4,'Por más que se discuta, la wiphala es uno de los símbolos del Estado.','However much it is discussed, the wiphala is one of the symbols of the State.','concesivas-por-mas-que'),
 dlg(s,5,[('Meg','¿Los idiomas indígenas se usan también en las ciudades?'),('Carlos','Sí, por más que _____ castellano en las ciudades, también se hablan aymara y quechua.')],['se hable','se hablaba','se hablaría'],'concesivas-por-mas-que',ds={1:'imperfect',2:'condicional-regular'}),
 dict_(s,6,'La Constitución de 2009 reconoce el castellano y 36 idiomas indígenas como oficiales.','The Constitution of 2009 recognises Spanish and 36 indigenous languages as official.','concesivas-por-mas-que')])
story(s,'El Estado Plurinacional','Bolivia\'s Constitution of 2009 defines the country as a Plurinational State and recognises 36 indigenous languages; the MAS governed for almost twenty years, and Rodrigo Paz became president in November 2025.',[
 "En 2006, una Asamblea Constituyente empezó a escribir una nueva constitución para Bolivia. La presidió Silvia Lazarte, una dirigente indígena. El texto se aprobó en un referéndum en enero de 2009 y se promulgó el 7 de febrero de 2009 en la ciudad de El Alto.",
 "La nueva Constitución define al país como un Estado Plurinacional. Reconoce como idiomas oficiales el castellano y los idiomas de los pueblos indígenas, que son treinta y seis. También reconoce que las comunidades indígenas pueden aplicar su propia justicia, dentro de los límites que fija la Constitución.",
 "Entre los símbolos del Estado, además de la bandera tricolor, el himno y el escudo, figura la wiphala, una bandera cuadrada de muchos colores. La Constitución también recoge ideas andinas, como el «vivir bien» (suma qamaña), entre los principios del Estado.",
 "Evo Morales, el primer presidente de origen indígena del país, gobernó de 2006 a 2019. Después de casi veinte años de gobiernos del MAS, con una interrupción en 2019 y 2020, Bolivia eligió en 2025 a un nuevo presidente.",
 "En noviembre de 2025 asumió la presidencia Rodrigo Paz, que ganó las elecciones en una segunda vuelta. En 2026 la Constitución de 2009 sigue en vigor."],
 [("Where was the Constitution promulgated?",["En El Alto.","En Potosí.","En Copacabana."],"The first paragraph."),
  ("How many indigenous languages does the Constitution recognise as official?",["Treinta y seis.","Seis.","Doscientos."],"The second paragraph."),
  ("Who became president in November 2025?",["Rodrigo Paz.","Evo Morales.","Silvia Lazarte."],"The fifth paragraph.")])
# ---------- consolidation
s=S('consolidation')
lesson(s,'Bolivia: the highlands, unit review','Review the Bolivian highlands, from Lake Titicaca to the Constitution of 2009, with the grammar you used to talk about them.','review: relative clauses, estar + participle, no es que… sino que, reported information, por más que',
 ['I can review what I learned about the Bolivian highlands, from Lake Titicaca to the Constitution of 2009.','I can use relative clauses, *estar* + participle, *no es que… sino que*, *según* and *por más que*.','I can say who says what about the coca leaf.'],
 ['I can describe the high plateau and Lake Titicaca with relative clauses introduced by *que* and *quien*.','I can say what Potosí looks like today with *estar* + participle.','I can correct a wrong idea about La Paz and El Alto with *no es que… sino que…*.','I can say who says what about the coca leaf, using *según* and *dice que*.','I can grant a point and still state my main idea with *por más que* + subjunctive.'])
ex(s,[
 match(s,1,[['el altiplano','high plateau'],['el socavón','mine tunnel'],['el cholet','brightly coloured building of El Alto'],['la wiphala','square flag of the Andean peoples']],V),
 fill(s,2,'La ciudad de Potosí __ situada al pie del Cerro Rico.','está','The city of Potosí is situated at the foot of the Cerro Rico.','pasiva-estado-estar-participio'),
 mc(s,3,'Which sentence says: "Titicaca is the lake that Bolivia shares with Peru"?',['El Titicaca es el lago que Bolivia comparte con Perú.','El Titicaca es el lago quien Bolivia comparte con Perú.','El Titicaca es el lago Bolivia comparte con Perú.','El Titicaca es el lago que Bolivia compartes con Perú.'],'relative-clauses'),
 fill(s,4,'No es que Sucre __ la sede del gobierno, sino que es la capital constitucional.','sea','It is not that Sucre is the seat of government; it is the constitutional capital.','refutacion-no-es-que-sino',hint='ser'),
 mc(s,5,'Which sentence says: "According to the government, coca has traditional uses"?',['Según el gobierno, la coca tiene usos tradicionales.','Según el gobierno, de que la coca tiene usos tradicionales.','Según el gobierno, la coca tener usos tradicionales.','Según al gobierno, la coca tiene usos tradicionales.'],'estilo-indirecto-informacion'),
 build(s,6,'Por más que se discuta, la Constitución reconoce treinta y seis idiomas indígenas.','However much it is discussed, the Constitution recognises thirty-six indigenous languages.','concesivas-por-mas-que'),
 dict_(s,7,'Las terrazas de la Isla del Sol están hechas con piedra.','The terraces of the Island of the Sun are made of stone.','pasiva-estado-estar-participio'),
 mc(s,8,'According to the texts of this unit, what is the wiphala?',['Una bandera de muchos colores.','Un sombrero que llevan las cholitas.','Una moneda de plata que se acuñaba en Potosí.','Un edificio de colores vivos de El Alto.'],None,cat='reading')])
