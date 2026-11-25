import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from common import *
V='b2-guatemala-vocab'
wc={}
# ---------- 01
s='b2-guatemala-01'
apply_lesson(s,"Tikal and the Petén: A Great Classic Maya City",
 "Describe who built and used Tikal, and what has been done since, with the passive with ser.",
 "passive with ser + past participle + por",
 ["I can say who built or did something with *ser* + participle + *por*.",
  "I can describe Tikal and what happened to it.",
  "I can explain how the people of Tikal collected water."],
 ("Unit 4: Guatemala: the Maya, Highland Communities and Memory",
  ["This unit is about Guatemala: the Maya city of Tikal, the Popol Vuh, colonial Antigua, the armed conflict of 1960 to 1996 and how it is remembered, and community life in the highlands today.",
   "The screens and instructions are in English; the texts and exercises are in Spanish. There is no new grammar here: each lesson uses a skill you already know to talk about Guatemala, and gives you the words you need for it."]))
wc[s]=apply_story(s,"Tikal, una gran ciudad maya del Petén",
 "Tikal, in the Petén jungle, was a powerful Maya city that was abandoned around the year 900 and is now a World Heritage site; nearby communities manage forest concessions.",
 ["passive with ser","vocabulary of archaeology"],
 ["En el norte de Guatemala, en el departamento de Petén, la selva esconde las ruinas de Tikal, una de las grandes ciudades mayas. Durante el período clásico, que va aproximadamente del año 250 al 900, Tikal fue una ciudad poderosa, con decenas de miles de habitantes y alianzas con otras ciudades.",
  "Sus templos y plazas fueron construidos con piedra caliza. En el año 695, el gobernante Jasaw Chan K'awiil I derrotó a Calakmul, una ciudad rival, y Tikal vivió una época de grandes obras. El Templo I, llamado también Templo del Gran Jaguar, fue levantado sobre su tumba, hacia el año 730, durante el reinado de su hijo y sucesor.",
  "En esta región casi no hay ríos, por eso el agua de la lluvia era recogida en grandes depósitos excavados en la roca. Esos depósitos fueron usados durante siglos.",
  "Hacia el año 900, Tikal fue abandonada poco a poco. Muchos investigadores piensan que influyeron varias sequías y los problemas de una población numerosa, pero no hay una sola explicación. La selva cubrió los templos, y la ciudad fue explorada por expediciones a mediados del siglo diecinueve.",
  "Hoy Tikal es parque nacional desde 1955, y fue declarada Patrimonio Mundial por la UNESCO en 1979, por su valor cultural y natural. En 2018, el escaneo láser (LiDAR) mostró muchas estructuras antes desconocidas en la selva del Petén. Cerca de Tikal, en la Reserva de la Biosfera Maya, comunidades como Carmelita y Uaxactún recibieron concesiones para usar el bosque de forma sostenible: aprovechan madera, resina de chicle y hojas de palma de xate sin talar la selva."])
g=gr("grammar.b2.guatemala.01.ser-passive","Who Built It? The Passive with ser",
 "You know the passive with *ser* from B1 Unit 18: *ser* + past participle, with *por* to name who did the action: *La ley fue aprobada por el Parlamento*. It is the natural way to describe monuments and historical events, because it puts the building or the event first and names the builder afterwards.",
 "The participle agrees with the subject",
 [("La ciudad fue construida por los mayas.","feminine singular: *construida*"),
  ("El templo fue levantado por orden del rey.","masculine singular: *levantado*"),
  ("Las estelas fueron talladas por artistas.","feminine plural: *talladas*"),
  ("Los depósitos eran usados durante la sequía.","imperfect *eran* for a habit or a situation in the past")],None,
 [("El Templo I fue levantado sobre la tumba de un gobernante.","Temple I was built over a ruler's tomb."),
  ("El agua de la lluvia era recogida en grandes depósitos.","Rainwater was collected in large reservoirs."),
  ("Las ruinas fueron exploradas por expediciones en el siglo diecinueve.","The ruins were explored by expeditions in the nineteenth century."),
  ("Tikal fue declarada Patrimonio Mundial por la UNESCO en 1979.","Tikal was declared a World Heritage Site by UNESCO in 1979.")],
 "Use *fue / fueron* for a single past event and *era / eran* for a habit or a description. The participle always agrees with the thing: *la ciudad fue construida*, *los templos fueron construidos*. When nobody needs naming, the *se* passive from B1 Unit 6 is shorter: *se construyeron los templos*.")
apply_gr(s,g)
apply_voc(s,[("la estela","stela, carved stone monument","noun"),("el gobernante","ruler","noun"),("el depósito","reservoir, tank","noun"),("la ruina","ruin","noun"),("el templo","temple","noun"),("la tumba","tomb","noun")],
 "Tikal and its ruins","Monuments, rulers and water")
apply_ex(s,[
 match(s+".ex01",[("la estela","stela, carved stone monument"),("el gobernante","ruler"),("el depósito","reservoir, tank"),("la ruina","ruin")],V),
 mc(s+".ex02","","grammar","Which sentence says \"The city was built by the Maya\"?",
   ["La ciudad fue construida por los mayas.","La ciudad fue construido por los mayas.","La ciudad fue construida de los mayas."],"ser-passive"),
 fill(s+".ex03","Tikal __ declarada Patrimonio Mundial por la UNESCO en 1979.","fue","Tikal was declared a World Heritage Site by UNESCO in 1979.","ser-passive"),
 build(s+".ex04",["El","templo","fue","levantado","sobre","la","tumba","de","un","gobernante."],"The temple was built over a ruler's tomb.","ser-passive"),
 dlg(s+".ex05",[("Meg","¿Cómo conseguían agua en Tikal?"),("Carlos","_____"),("Meg","Entonces la lluvia era muy importante.")],
   ["El agua de la lluvia era recogida en grandes depósitos.","Las ruinas fueron exploradas por expediciones a mediados del siglo diecinueve.","La ciudad fue abandonada poco a poco hacia el año 900."],V),
 dict_(s+".ex06","Las estelas de Tikal fueron talladas por artistas mayas hace muchos siglos.","The stelae of Tikal were carved by Maya artists many centuries ago.","ser-passive"),
])
# ---------- 02
s='b2-guatemala-02'
apply_lesson(s,"The Popol Vuh: Creation and Maize",
 "Tell the order of events in the Popol Vuh with antes de and después de + infinitive.",
 "antes de and después de + infinitive",
 ["I can say what came first and what came next with *antes de* and *después de* + infinitive.",
  "I can tell in outline how the gods created people in the Popol Vuh.",
  "I can explain how the Popol Vuh reached us today."],
 ("The Popol Vuh: Creation and Maize",
  ["In this lesson you read about the Popol Vuh, a K'iche' book of the highlands of Guatemala, and its story of how the world and people were made.",
   "The grammar is the one you know for putting events in order: *antes de* and *después de* + infinitive, and *cuando* + subjunctive for the future."]))
wc[s]=apply_story(s,"El Popol Vuh: la creación y el maíz",
 "The Popol Vuh is a K'iche' book that tells how the gods made people from maize and how two twins defeated the lords of the underworld; it reached us through a copy made by a friar around 1700.",
 ["antes de and después de + infinitive","vocabulary of the Popol Vuh"],
 ["El Popol Vuh, o «Libro del Consejo», es un libro del pueblo k'iche', uno de los pueblos mayas de las tierras altas de Guatemala. Fue escrito en k'iche' con letras del alfabeto latino hacia mediados del siglo dieciséis. Cuenta cómo se creó el mundo y también la historia de los antepasados de los k'iche'.",
  "Según el libro, al principio solo había agua y silencio, y los dioses crearon la tierra con la palabra. Antes de crear a los seres humanos, hicieron animales, pero los animales no podían hablar ni adorar a sus creadores. Después de probar con barro, los dioses hicieron figuras de madera, pero tampoco funcionaron. Por fin usaron maíz, y la abuela Ixmukané molió los granos para formar a los primeros seres humanos.",
  "Otra parte del libro cuenta la historia de los gemelos Hunahpú e Ixbalanqué. Antes de subir al cielo, los gemelos bajaron a Xibalbá, el inframundo, y vencieron a los señores de la muerte. Después de vencerlos, según el libro, se convirtieron en el sol y la luna.",
  "El manuscrito original no se conserva. Hacia el año 1700, el fraile dominico Francisco Ximénez copió el texto k'iche' en Chichicastenango y escribió una traducción al español. Gracias a esa copia, el Popol Vuh se conoce hoy en muchos idiomas.",
  "Para muchos pueblos mayas, el maíz es mucho más que un alimento. En algunas comunidades, las familias hacen una ceremonia antes de sembrar, y muchas personas se describen como «gente de maíz», una idea que viene de este libro."])
g=gr("grammar.b2.guatemala.02.antes-despues-infinitive","First This, Then That",
 "You know *antes de* and *después de* + infinitive from A2 Unit 4, and *cuando* + subjunctive for the future from A2 Unit 27. They are the tools for telling a story in order, and the Popol Vuh is a story of things done one after another: the gods try clay, then wood, then maize. When the same person does both actions, the infinitive does not change.",
 "Putting events in order",
 [("Antes de crear a los humanos, los dioses hicieron animales.","*antes de* + infinitive: before creating humans, the gods made animals"),
  ("Después de probar con barro, probaron con madera.","*después de* + infinitive: after trying clay, they tried wood"),
  ("Después de vencer a los señores, los gemelos subieron al cielo.","*después de* + infinitive: after defeating the lords, the twins went up"),
  ("Cuando llegue la lluvia, las familias sembrarán el maíz.","*cuando* + subjunctive for a future time: when the rain comes, the families will plant maize")],None,
 [("Antes de bajar a Xibalbá, los gemelos eran jóvenes.","Before going down to Xibalbá, the twins were young."),
  ("Después de leer el texto k'iche', el fraile escribió una traducción.","After reading the K'iche' text, the friar wrote a translation."),
  ("Antes de sembrar, muchas familias hacen una ceremonia.","Before planting, many families hold a ceremony."),
  ("Cuando termine la cosecha, la familia celebrará una fiesta.","When the harvest is over, the family will hold a celebration.")],
 "*Antes de* and *después de* are followed by the infinitive, never by a conjugated verb: *antes de crear*, not *antes de crearon*. If a different person does the second action, use *cuando* instead (*cuando llegue la lluvia*) or two sentences.")
apply_gr(s,g)
apply_voc(s,[("el barro","clay, mud","noun"),("la madera","wood","noun"),("el gemelo","twin","noun"),("el inframundo","underworld","noun"),("el fraile","friar","noun")],
 "The Popol Vuh","Creation, twins and underworld")
apply_ex(s,[
 match(s+".ex01",[("el barro","clay, mud"),("la madera","wood"),("el gemelo","twin"),("el inframundo","underworld")],V),
 mc(s+".ex02","","grammar","Which sentence says \"After trying clay, the gods tried wood\"?",
   ["Después de probar con barro, los dioses probaron con madera.","Después probar con barro, los dioses probaron con madera.","Después de probaron con barro, los dioses probaron con madera."],"antes-despues-infinitive"),
 fill(s+".ex03","Cuando __ la lluvia, las familias sembrarán el maíz.","llegue","When the rain comes, the families will plant the maize.","cuando-subjuntivo",hint="llegar"),
 build(s+".ex04",["Después","de","vencer","a","los","señores","de","Xibalbá,","los","gemelos","subieron","al","cielo."],"After defeating the lords of Xibalbá, the twins went up to the sky.","antes-despues-infinitive"),
 dlg(s+".ex05",[("Carlos","¿Cómo conocemos hoy el Popol Vuh?"),("Meg","_____"),("Carlos","Entonces el libro llegó hasta nosotros gracias a esa copia.")],
   ["Un fraile copió el texto y escribió una traducción al español.","Los dioses probaron con barro y después con figuras de madera.","Los gemelos bajaron al inframundo antes de subir al cielo."],V),
 dict_(s+".ex06","Antes de crear a los humanos, los dioses probaron con barro y con madera.","Before creating humans, the gods tried clay and wood.","antes-despues-infinitive"),
])
# ---------- 03
s='b2-guatemala-03'
apply_lesson(s,"Antigua: A City Built for Earthquakes",
 "Explain how colonial Antigua was built and what happened in 1773, with a pesar de and pese a.",
 "concession with a pesar de que and pese a",
 ["I can say that something happened in spite of a difficulty, with *a pesar de que* and *pese a*.",
  "I can describe why the churches of Antigua have thick walls and low towers.",
  "I can tell what happened to the capital in 1773."],
 ("Antigua: A City Built for Earthquakes",
  ["In this lesson you walk through Antigua Guatemala, a colonial capital between volcanoes. You will read why its churches were built the way they were, and what the earthquakes of 1773 changed.",
   "The grammar is the one you know for saying that something happened in spite of a difficulty: *a pesar de que* and *pese a*."]))
wc[s]=apply_story(s,"Antigua Guatemala: una ciudad entre volcanes",
 "Antigua was the capital of the Captaincy General of Guatemala; its thick-walled churches were built for earthquakes, and the 1773 quakes led the authorities to move the capital.",
 ["a pesar de que, pese a","vocabulary of colonial architecture"],
 ["Antigua Guatemala está en un valle rodeado por tres volcanes: Agua, Fuego y Acatenango. Su nombre colonial era Santiago de los Caballeros de Guatemala. En 1541, un alud de lodo bajó del volcán de Agua y destruyó la primera capital, en el valle de Almolonga. Por eso, en 1543 se fundó una nueva ciudad en el valle de Panchoy.",
  "Durante más de dos siglos, esta ciudad fue la capital de la Capitanía General de Guatemala, un territorio que iba desde Chiapas hasta Costa Rica. Allí se construyeron iglesias, conventos y palacios.",
  "Como la región tiene muchos terremotos, los constructores levantaron iglesias de un estilo que a veces se llama «barroco sísmico»: muros muy gruesos, torres bajas y contrafuertes que sostenían las paredes. La iglesia de La Merced, con su fachada amarilla y sus adornos de estuco blanco, es un ejemplo conocido. A pesar de que los muros eran muy gruesos, muchos edificios sufrieron daños en los terremotos.",
  "En julio de 1773, los terremotos de Santa Marta dañaron gravemente la ciudad. El capitán general Martín de Mayorga decidió trasladar la capital a otro valle, el de la Ermita, y allí se fundó la actual Ciudad de Guatemala, con el nombre de Nueva Guatemala de la Asunción. Pese a las órdenes de las autoridades, muchas familias se quedaron en la antigua capital, entre las ruinas.",
  "La UNESCO declaró Antigua Guatemala Patrimonio de la Humanidad en 1979. La ciudad sigue viviendo cerca de los volcanes: en junio de 2018, el volcán de Fuego entró en erupción y causó muchos muertos y desaparecidos en las comunidades cercanas."])
g=gr("grammar.b2.guatemala.03.a-pesar-de","In Spite of the Earthquakes",
 "You know *a pesar de que* and *pese a* from B1 Unit 32, and *aunque* from A2 Unit 28. They let you say that something happened or lasted in spite of a difficulty, which is the story of Antigua: thick walls, earthquakes and families who stayed. With a real fact, the verb is in the indicative.",
 "Forms with a pesar de and pese a",
 [("A pesar de los terremotos, la ciudad siguió viva.","*a pesar de* + noun: in spite of the earthquakes, the city lived on"),
  ("A pesar de ser muy sólida, la iglesia sufrió daños.","*a pesar de* + infinitive: although it was very solid, the church was damaged"),
  ("A pesar de que los muros eran gruesos, hubo daños.","*a pesar de que* + a full clause: although the walls were thick, there was damage"),
  ("Pese a las órdenes, muchas familias se quedaron.","*pese a* + noun: despite the orders, many families stayed")],None,
 [("Pese a los terremotos, los constructores siguieron usando piedra.","Despite the earthquakes, the builders kept using stone."),
  ("A pesar de que la capital se trasladó, muchas familias se quedaron.","Although the capital was moved, many families stayed."),
  ("A pesar de ser una ciudad antigua, hoy recibe a muchos visitantes.","Although it is an old city, today it receives many visitors."),
  ("Pese a su fachada sencilla, la iglesia es muy sólida.","Despite its plain facade, the church is very solid.")],
 "Before a full clause you need *que*: *a pesar de que los muros eran gruesos*. Before a noun or an infinitive you do not: *a pesar de los muros*, *a pesar de ser gruesos*. Not *a pesar que*, and not *a pesar de los muros eran gruesos*.")
apply_gr(s,g)
apply_voc(s,[("el contrafuerte","buttress","noun"),("el muro","wall","noun"),("la fachada","facade, front of a building","noun"),("el terremoto","earthquake","noun"),("trasladar","to move, to transfer","verb")],
 "Antigua and its buildings","Walls, earthquakes and volcanoes")
apply_ex(s,[
 match(s+".ex01",[("el contrafuerte","buttress"),("el muro","wall"),("la fachada","facade, front of a building"),("trasladar","to move, to transfer")],V),
 mc(s+".ex02","","grammar","Which sentence says \"Although the walls were very thick, many buildings suffered damage\"?",
   ["A pesar de que los muros eran muy gruesos, muchos edificios sufrieron daños.","A pesar que los muros eran muy gruesos, muchos edificios sufrieron daños.","A pesar de los muros eran muy gruesos, muchos edificios sufrieron daños."],"a-pesar-de"),
 fill(s+".ex03","A pesar de __ muy sólida, la iglesia sufrió daños en el terremoto.","ser","Although it was very solid, the church suffered damage in the earthquake.","a-pesar-de"),
 build(s+".ex04",["Pese","a","las","órdenes","de","las","autoridades,","muchas","familias","se","quedaron."],"Despite the orders of the authorities, many families stayed.","a-pesar-de"),
 dlg(s+".ex05",[("Meg","¿Por qué las iglesias de Antigua tienen muros tan gruesos?"),("Carlos","_____"),("Meg","Ahora lo entiendo.")],
   ["Porque la región tiene terremotos, y los constructores querían edificios más sólidos.","Porque el café de la región es muy bueno y se vende en el mercado.","Porque los gemelos bajaron al inframundo y vencieron a los señores de Xibalbá."],V),
 dict_(s+".ex06","A pesar de que los muros eran muy gruesos, muchos edificios sufrieron daños en 1773.","Although the walls were very thick, many buildings suffered damage in 1773.","a-pesar-de"),
])
# ---------- 04
s='b2-guatemala-04'
apply_lesson(s,"The Armed Conflict, Testimony and Memory",
 "Report what witnesses, commissions and a Nobel laureate said about the armed conflict, with reported speech.",
 "reported speech with tense shifting",
 ["I can report what someone said, with *dijo que* and the verb moved back in time.",
  "I can say what the CEH and the REMHI reports said, attributing each claim.",
  "I can put the main events of 1954 to 1999 in order."],
 ("The Armed Conflict, Testimony and Memory",
  ["This lesson is about the armed conflict in Guatemala (1960 to 1996) and how it has been investigated and remembered. Every claim about the conflict is attributed to the person or the report that makes it.",
   "The grammar is reported speech: you know how to say what someone said (*dijo que vivía con miedo*) and how to cite a source with *según*."]))
wc[s]=apply_story(s,"El conflicto armado y la memoria en Guatemala",
 "Guatemala's armed conflict lasted from 1960 to 1996; the text reports what the CEH and the REMHI reports concluded, what Rigoberta Menchú said and how the dead are still being searched for.",
 ["reported speech","vocabulary of memory and truth commissions"],
 ["En 1954, un golpe de Estado, apoyado por Estados Unidos, derrocó al presidente Jacobo Árbenz, que había aprobado una reforma agraria en 1952. En 1960 empezó un conflicto armado interno entre el ejército y grupos guerrilleros que duró hasta 1996. Los Acuerdos de Paz se firmaron el 29 de diciembre de 1996.",
  "Después de la guerra, dos informes investigaron lo ocurrido. El primero fue el de la Iglesia católica, REMHI, que se presentó en abril de 1998. Dos días después fue asesinado el obispo Juan Gerardi, que había coordinado el trabajo. En febrero de 1999, la Comisión para el Esclarecimiento Histórico (CEH) presentó su informe «Guatemala: memoria del silencio».",
  "La CEH dijo que unas doscientas mil personas habían muerto o desaparecido durante el conflicto. Según la comisión, el 93 % de las violaciones documentadas había sido cometido por el Estado y por grupos paramilitares, y el 3 % por la guerrilla. La CEH también dijo que, en cuatro regiones, el ejército había cometido actos de genocidio contra grupos mayas: los ixiles, los q'anjob'ales y chuj, los k'iche' y los achí. Algunas personas y organizaciones defendían al ejército y no aceptaron esa conclusión.",
  "En 1983 se publicó el libro «Me llamo Rigoberta Menchú y así me nació la conciencia», escrito con la antropóloga Elisabeth Burgos. Menchú, una mujer k'iche', contó que su familia había sufrido la persecución del ejército. En 1992 recibió el Premio Nobel de la Paz. En 1999, el antropólogo David Stoll cuestionó algunos detalles del libro, y el debate duró años.",
  "En 2013, un tribunal de Guatemala condenó por genocidio al exgeneral Efraín Ríos Montt, que había gobernado en 1982 y 1983; unos días después, la Corte de Constitucionalidad anuló la sentencia. Mientras tanto, la Fundación de Antropología Forense de Guatemala exhuma restos de víctimas, y muchas familias los entierran según sus costumbres mayas."])
g=gr("grammar.b2.guatemala.04.estilo-indirecto","Saying What Others Said",
 "You know reported speech with *dijo que* and tense shifting from B1 Unit 13: after a past verb such as *dijo*, the present moves to the imperfect, the past moves to the pluperfect and the future moves to the conditional. You also know *según* + a source from the same unit. They are the tools for writing about a painful period fairly: you say who said what instead of stating a judgement yourself.",
 "From direct words to reported words",
 [("«Vivo con miedo.» → Dijo que vivía con miedo.","present → imperfect"),
  ("«Vi a los soldados.» → Dijo que había visto a los soldados.","past → pluperfect"),
  ("«Hablaré con el juez.» → Dijo que hablaría con el juez.","future → conditional"),
  ("Según la comisión, hubo miles de víctimas.","*según* + source: according to the commission")],None,
 [("La comisión dijo que unas doscientas mil personas habían muerto o desaparecido.","The commission said that about two hundred thousand people had died or disappeared."),
  ("Menchú contó que su familia había sufrido la persecución del ejército.","Menchú said that her family had suffered persecution by the army."),
  ("Según el informe, la mayoría de las violaciones había sido cometida por agentes del Estado.","According to the report, most violations had been committed by agents of the state."),
  ("El tribunal dijo que el exgeneral era culpable.","The court said that the former general was guilty.")],
 "Move the verb back after a past reporting verb, and change the pronouns and time words too: *hoy* becomes *aquel día*, *aquí* becomes *allí*. Say who is speaking: a claim about the conflict is always *según la CEH*, *dijo la comisión* or *contó Menchú*, never a statement in your own voice.")
apply_gr(s,g)
apply_voc(s,[("el testimonio","testimony, account of a witness","noun"),("el informe","report","noun"),("la víctima","victim","noun"),("la comisión","commission","noun"),("el conflicto","conflict","noun"),("la sentencia","sentence, court ruling","noun")],
 "Memory and truth commissions","Testimony, reports and victims")
apply_ex(s,[
 match(s+".ex01",[("el testimonio","testimony, account of a witness"),("el informe","report"),("la víctima","victim"),("la comisión","commission")],V),
 mc(s+".ex02","","grammar","The witness said: \"I live with fear.\" Which sentence reports her words?",
   ["La testigo dijo que vivía con miedo.","La testigo dijo que vivió con miedo.","La testigo dijo que viviría con miedo."],"estilo-indirecto",{"1":"preterito-indefinido","2":"condicional-regular"}),
 fill(s+".ex03","La mujer dijo que su familia __ en un pueblo.","vivía","The woman said that her family lived in a village.","estilo-indirecto",hint="vivir"),
 build(s+".ex04",["La","comisión","dijo","que","había","escuchado","muchos","testimonios."],"The commission said that it had heard many testimonies.","estilo-indirecto"),
 dlg(s+".ex05",[("Carlos","¿Qué dijo la CEH en 1999?"),("Meg","_____"),("Carlos","Es un número muy grande.")],
   ["Dijo que unas doscientas mil personas habían muerto durante el conflicto.","Dijo que unas doscientas mil personas morirán durante el conflicto.","Dijo que unas doscientas mil personas mueren durante el conflicto."],"estilo-indirecto",ds={"1":"futuro-simple","2":"present-tense"}),
 dict_(s+".ex06","La comisión dijo que la mayoría de las violaciones había sido cometida por agentes del Estado.","The commission said that most of the violations had been committed by agents of the state.","estilo-indirecto"),
])
# ---------- 05
s='b2-guatemala-05'
apply_lesson(s,"Coffee, Lake Atitlán and the 48 Cantones",
 "Describe life around Lake Atitlán and the 48 Cantones, combining the passive with ser, reported speech and infinitive or que + subjunctive.",
 "passive with ser, reported speech and infinitive vs que + subjunctive",
 ["I can say who does or grows something with *ser* + participle + *por*.",
  "I can report what the cantones or their representatives said, and cite them with *según*.",
  "I can say who wants what with an infinitive (same person) or *que* + subjunctive (a different person)."],
 ("Coffee, Lake Atitlán and the 48 Cantones",
  ["In this lesson you read about Lake Atitlán, its coffee cooperatives and the 48 Cantones of Totonicapán, a community authority of K'iche' villages.",
   "The grammar brings together three skills you know: the passive with *ser*, reported speech, and the choice between an infinitive and *que* + subjunctive from B2 Unit 4."]))
wc[s]=apply_story(s,"El lago Atitlán y los 48 Cantones",
 "Lake Atitlán sits in a volcanic caldera surrounded by Maya villages and coffee farms, and the 48 Cantones of Totonicapán run community forests and led protests in October 2023.",
 ["passive with ser, reported speech, infinitive vs que + subjunctive","vocabulary of coffee and community authority"],
 ["El lago Atitlán, en el altiplano de Sololá, está dentro de una caldera volcánica y rodeado por tres volcanes: Atitlán, Tolimán y San Pedro. Está a más de mil quinientos metros sobre el nivel del mar. Por la tarde suele soplar un viento llamado Xocomil, que levanta olas en el lago.",
  "Alrededor del lago viven comunidades mayas tz'utujiles y kaqchikeles, en pueblos como Santiago Atitlán, San Juan La Laguna y Santa Catarina Palopó. Muchas mujeres tejen con el telar de cintura y usan tintes naturales. En las laderas, el café es cultivado por pequeñas familias, y muchas de ellas están organizadas en cooperativas que venden su café a un precio justo.",
  "El lago también tiene problemas. En 2009, una floración de cianobacterias cubrió una gran parte del agua. Según los científicos, las aguas residuales y los fertilizantes que llegan al lago ayudan a producir ese fenómeno. Los municipios de la orilla han trabajado juntos para tratar mejor el agua.",
  "Más al norte, en el departamento de Totonicapán, están los 48 Cantones, una organización comunal k'iche'. Según sus representantes, sus autoridades sirven sin recibir un sueldo. Los cantones cuidan los bosques comunales y las fuentes de agua, y sus autoridades llevan una vara como símbolo de su cargo.",
  "En octubre de 2023, los 48 Cantones encabezaron protestas pacíficas y bloqueos de carreteras para defender el resultado de las elecciones presidenciales. Dijeron que querían que se respetara el voto de la población. Bernardo Arévalo asumió la presidencia el 14 de enero de 2024."])
g=gr("grammar.b2.guatemala.05.integracion-discurso-comunal","Putting Three Skills Together",
 "In this lesson you use three skills you already know: the passive with *ser* (B1 Unit 18), reported speech and *según* (B1 Unit 13), and the choice between an infinitive and *que* + subjunctive (B2 Unit 4). Together they let you write a short, careful text about a community and what it says it wants.",
 "Three skills, one text",
 [("El café es cultivado por pequeñas familias.","passive with *ser*: the participle agrees with *café*"),
  ("Los representantes dijeron que defenderían el bosque.","reported speech: future → conditional"),
  ("Los cantones quieren defender el bosque.","same person wants and acts: infinitive"),
  ("Los cantones quieren que el Gobierno respete el voto.","two different people: *que* + subjunctive")],None,
 [("Los bosques comunales son cuidados por los cantones.","The communal forests are looked after by the cantons."),
  ("Según sus representantes, las autoridades sirven sin sueldo.","According to their representatives, the authorities serve without a salary."),
  ("Dijeron que querían que se respetara el voto.","They said that they wanted the vote to be respected."),
  ("Las cooperativas quieren vender el café a un precio justo.","The cooperatives want to sell the coffee at a fair price.")],
 "Ask who does what. If the person who wants and the person who acts are the same, use the infinitive (*quieren defender*); if they differ, use *que* + subjunctive (*quieren que el Gobierno respete*). After a past verb the subjunctive moves back too: *querían que se respetara*.")
apply_gr(s,g)
apply_voc(s,[("el cantón","canton, community division of Totonicapán","noun"),("la cooperativa","cooperative","noun"),("la cosecha","harvest","noun"),("la vara","staff, rod of office","noun"),("el lago","lake","noun")],
 "Atitlán and the cantones","Coffee, lake and community authority")
apply_ex(s,[
 match(s+".ex01",[("el cantón","canton, community division of Totonicapán"),("la cooperativa","cooperative"),("la cosecha","harvest"),("la vara","staff, rod of office")],V),
 mc(s+".ex02","","grammar","Which sentence is correct?",
   ["El café es cultivado por pequeñas cooperativas.","El café es cultivada por pequeñas cooperativas.","El café es cultivado a pequeñas cooperativas."],"ser-passive"),
 fill(s+".ex03","Las familias quieren __ el café a un buen precio.","vender","The families want to sell the coffee at a good price.","infinitive-vs-que-subjunctive"),
 build(s+".ex04",["Los","cantones","dijeron","que","defenderían","el","bosque","comunal."],"The cantons said that they would defend the communal forest.","estilo-indirecto"),
 dlg(s+".ex05",[("Meg","¿Quién cuida el bosque comunal de Totonicapán?"),("Carlos","_____"),("Meg","Entonces es un trabajo de toda la comunidad.")],
   ["El bosque es cuidado por las comunidades de los cantones.","El lago tiene tres volcanes cerca del pueblo.","El café es cultivado por pequeñas familias en las montañas."],V),
 dict_(s+".ex06","Según sus representantes, las autoridades de los cantones sirven sin recibir un sueldo.","According to their representatives, the authorities of the cantons serve without receiving a salary.","estilo-indirecto-informacion"),
])
# ---------- consolidation
s='b2-guatemala-consolidation'
d=jl('lessons/b2/'+s+'.json')
d['goal']="Review Tikal, the Popol Vuh, Antigua, the armed conflict and its memory, and community life in the highlands, with the grammar you used to talk about them."
d['grammar']="review: passive with ser, antes de / después de + infinitive, a pesar de, reported speech"
for sec in d['sections']:
    if sec['type']=='goal':
        sec['items']=["I can review what I learned about Guatemala, from Tikal to the highlands today.","I can use the passive with *ser*, *antes de* and *después de* + infinitive, *a pesar de* and reported speech.","I can put events from the classic Maya to 1999 in order.","I can cite a source with *según* when I talk about the armed conflict."]
    if sec['type']=='checklist':
        sec['items']=["I can say who built or explored a monument with the passive with *ser*.","I can tell events in order with *antes de* and *después de* + infinitive.","I can say that something lasted in spite of difficulties, with *a pesar de* and *pese a*.","I can report what a commission or a witness said, with *dijo que* and *según*."]
jw('lessons/b2/'+s+'.json',d)
apply_ex(s,[
 match(s+".ex01",[("la estela","stela, carved stone monument"),("el barro","clay, mud"),("el contrafuerte","buttress"),("el testimonio","testimony, account of a witness")],V),
 mc(s+".ex02","","reading","According to the text, what happened to Tikal around the year 900?",
   ["Fue abandonada poco a poco.","Fue vendida a otro país en un solo día.","Fue trasladada a otro valle."]),
 mc(s+".ex03","","grammar","Which sentence is correct?",
   ["Después de explorar las ruinas, escribieron un informe.","Después explorar las ruinas, escribieron un informe.","Después de exploraron las ruinas, escribieron un informe."],"antes-despues-infinitive"),
 fill(s+".ex04","__ a las órdenes del capitán general, muchas familias se quedaron en la ciudad.","Pese","Despite the orders of the captain general, many families stayed in the city.","a-pesar-de"),
 {"id":s+".ex05","type":"sentence-order","category":"grammar","sentences":[
  "En el año 695 Tikal derrotó a Calakmul. [In the year 695 Tikal defeated Calakmul.]",
  "En 1773 los terremotos de Santa Marta dañaron Antigua. [In 1773 the Santa Marta earthquakes damaged Antigua.]",
  "En 1996 se firmaron los Acuerdos de Paz. [In 1996 the Peace Accords were signed.]",
  "En 1999 la CEH presentó su informe. [In 1999 the CEH presented its report.]"],
  "solution":[0,1,2,3],"teaches":["preterito-indefinido"]},
 dlg(s+".ex06",[("Meg","¿Qué dijo la CEH sobre las víctimas?"),("Carlos","_____"),("Meg","Entonces el informe da datos importantes.")],
   ["Dijo que muchas de las víctimas eran mayas.","Dijo que los gemelos habían vencido a los señores del inframundo.","Dijo que el agua de lluvia era recogida en grandes depósitos."],V),
 dict_(s+".ex07","El café es cultivado por cooperativas pequeñas cerca del lago Atitlán.","The coffee is grown by small cooperatives near Lake Atitlán.","ser-passive"),
 {"id":s+".ex08","type":"structured-writing","category":"writing","template":[
  {"prompt":"Say that the ruins of Tikal were explored by expeditions. Use the passive with ser.","answer":"Las ruinas de Tikal fueron exploradas por expediciones."},
  {"prompt":"Say that after reading the Popol Vuh you want to visit Guatemala. Start with 'Después de'.","answer":"Después de leer el Popol Vuh, quiero visitar Guatemala."},
  {"prompt":"Say that Menchú said that her family had suffered. Start with 'Menchú dijo'.","answer":"Menchú dijo que su familia había sufrido."}],
  "teaches":[V]},
],"b2-guatemala-consolidation-ex")
print(wc)
