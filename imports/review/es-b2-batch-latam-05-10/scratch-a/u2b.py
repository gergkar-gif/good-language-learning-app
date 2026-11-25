from lib import *
U='b2-nicaragua-vocab'
# ---------- 04 ----------
s='b2-nicaragua-04'; T='a-pesar-de'
lesson(s,'The 1979 revolution, the literacy crusade and Solentiname',
 'Tell what happened in Nicaragua after 1979 and say what continued in spite of difficulties, with a pesar de and pese a.',
 'concession with a pesar de que and pese a (review)',
 ['In this lesson you read about the Sandinista revolution of 1979, the 1980 literacy crusade, the Contra war and the painters of Solentiname. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for saying that something went on in spite of a difficulty: *a pesar de* and *pese a*.'],
 ['I can say that something continued in spite of a difficulty, with *a pesar de* and *pese a*.','I can tell what the literacy crusade of 1980 was.','I can explain who the painters of Solentiname were.'])
grammar(s,'In Spite of Everything',[
 {'type':'text','title':'What you already know','content':'You know *a pesar de que* and *pese a* from B1 Unit 32, and *aunque* from A2 Unit 28. They say that something happened or went on in spite of a difficulty. With a real fact the verb is in the indicative. That is the story of the Nicaraguan 1980s: a campaign that went on in spite of attacks, a community that painted in spite of poverty.'},
 {'type':'table','title':'Forms with a pesar de and pese a','rows':[
  ['A pesar de los ataques, la campaña siguió.','*a pesar de* + noun: in spite of the attacks, the campaign went on'],
  ['A pesar de ser muy pobres, empezaron a pintar.','*a pesar de* + infinitive: although they were very poor, they began to paint'],
  ['A pesar de que había guerra, hubo elecciones en 1990.','*a pesar de que* + a full clause: although there was war, there were elections in 1990'],
  ['Pese a la guerra, la escuela siguió abierta.','*pese a* + noun: despite the war, the school stayed open']]},
 {'type':'examples','title':'In Nicaragua','items':[
  {'spanish':'A pesar de los ataques, miles de jóvenes enseñaron a leer a campesinos.','english':'In spite of the attacks, thousands of young people taught peasants to read.'},
  {'spanish':'Los campesinos de Solentiname empezaron a pintar a pesar de no tener estudios de arte.','english':'The peasants of Solentiname began to paint although they had no art training.'},
  {'spanish':'A pesar de que la comunidad fue destruida en 1977, las pinturas de Solentiname son famosas.','english':'Although the community was destroyed in 1977, the paintings of Solentiname are famous.'},
  {'spanish':'Pese a los años de guerra, en 1990 hubo elecciones en Nicaragua.','english':'Despite the years of war, there were elections in Nicaragua in 1990.'}]},
 {'type':'tip','content':'Before a full clause you need *que*: *a pesar de que había guerra*. Before a noun or an infinitive you do not: *a pesar de la guerra*, *a pesar de ser pobres*. Not *a pesar que*, and not *a pesar de había guerra*.'}])
vocab(s,'Revolution, reading and painting','The revolution, the crusade and Solentiname',[
 ('la alfabetización','teaching people to read and write','noun'),('el brigadista','volunteer teacher in the 1980 crusade','noun'),
 ('la pintura','painting','noun'),('el campesino','farmer, peasant','noun'),('el ataque','attack','noun'),('destruir','to destroy','verb')])
ex(s,[
 match(s+'.ex01',[['la alfabetización','teaching people to read and write'],['el brigadista','volunteer teacher in the 1980 crusade'],['la pintura','painting'],['destruir','to destroy']],U),
 mc(s+'.ex02','Which sentence says "In spite of the attacks, the literacy campaign went on"?',
  ['A pesar de los ataques, la campaña de alfabetización siguió.','A pesar los ataques, la campaña de alfabetización siguió.','A pesar de hubo ataques, la campaña de alfabetización siguió.'],teaches=T),
 fb(s+'.ex03','A pesar de __ muy pobres, los campesinos de Solentiname empezaron a pintar.','ser','Although they were very poor, the peasants of Solentiname began to paint.',T),
 sb(s+'.ex04',['A','pesar','de','que','la','comunidad','fue','destruida','en','1977,','sus','pinturas','son','famosas.'],'Although the community was destroyed in 1977, its paintings are famous.',T),
 dlg(s+'.ex05',[('Meg','¿Qué pasó con la campaña de alfabetización de 1980?'),('Carlos','_____'),('Meg','Fue una campaña muy importante.')],
  ['A pesar de los ataques, miles de jóvenes enseñaron a leer a campesinos.','La campaña terminó en 1990, cuando Violeta Chamorro ganó las elecciones.','La campaña fue organizada por soldados de Estados Unidos.'],U),
 dic(s+'.ex06','Pese a los años de guerra, en 1990 hubo elecciones en Nicaragua.','Despite the years of war, there were elections in Nicaragua in 1990.',T)])
story(s,'La revolución de 1979, la alfabetización y Solentiname','After the 1979 revolution Nicaragua held a literacy crusade, fought the Contra war and became known for the peasant painters of Solentiname.',
 ['La revolución de 1979','Cruzada de Alfabetización','Solentiname'],['a pesar de','pese a'],[
 'El 19 de julio de 1979, el Frente Sandinista de Liberación Nacional (FSLN) entró en Managua. Terminaba así la dinastía de la familia Somoza, que había gobernado el país durante más de cuarenta años. Muchos nicaragüenses celebraron el cambio, aunque otros lo miraron con temor.',
 'En 1980, el nuevo gobierno organizó la Cruzada Nacional de Alfabetización. Decenas de miles de jóvenes, los brigadistas, viajaron a pueblos y montañas para enseñar a leer y escribir a campesinos. A pesar de los ataques de grupos armados, la cruzada siguió, aunque algunos brigadistas fueron asesinados. Según el gobierno de entonces, el analfabetismo bajó de un 50,3 % a un 12,9 %. Ese año la UNESCO le dio a Nicaragua un premio por esta campaña.',
 'Desde 1981 comenzó la guerra de los «contras», grupos armados que recibieron dinero y armas de Estados Unidos y que combatían contra el gobierno sandinista. Murieron decenas de miles de personas. En 1986, la Corte Internacional de Justicia dijo que Estados Unidos había violado el derecho internacional. A pesar de que seguía la guerra, hubo elecciones en 1984 y en 1990. En febrero de 1990, Violeta Chamorro ganó las elecciones al sandinista Daniel Ortega, y él entregó el poder.',
 'En el archipiélago de Solentiname, en el lago Cocibolca, el poeta y sacerdote Ernesto Cardenal fundó en 1966 una comunidad con campesinos y pescadores. A pesar de no tener estudios de arte, muchos de ellos empezaron a pintar paisajes, animales y fiestas con colores muy vivos, y se hicieron famosos como pintores. En 1977, después de un ataque a un cuartel de la Guardia Nacional en San Carlos, la Guardia destruyó la comunidad. Sin embargo, sus pinturas siguen siendo conocidas hoy.'],
 [('What did the brigadistas do in 1980?',['Enseñaron a leer y escribir a campesinos.','Pintaron cuadros en Solentiname.','Ganaron las elecciones.','Firmaron la paz con Sandino.'],0,'The text says they taught peasants to read and write.'),
  ('Who won the elections of February 1990, according to the text?',['Violeta Chamorro.','Daniel Ortega.','Ernesto Cardenal.','Anastasio Somoza.'],0,'The text says Violeta Chamorro won.'),
  ('Who founded the community of Solentiname, and when?',['Ernesto Cardenal, en 1966.','Sandino, en 1927.','Rubén Darío, en 1888.','Violeta Chamorro, en 1990.'],0,'The text says Ernesto Cardenal founded it in 1966.')])

# ---------- 05 ----------
s='b2-nicaragua-05'; T='estilo-indirecto-informacion'
lesson(s,'The 2018 protests, exile and Nicaragua today',
 'Report what the UN, the IACHR and the government said about Nicaragua since 2018, naming each source, with según and dijo que.',
 'reported statements and sources: según, dijo que (review)',
 ['In this lesson you read about the protests of 2018, the exile of writers and the government of Nicaragua today. The text is in Spanish; the screens and instructions are in English. Disputed claims are always given with their source.',
  'The grammar is the one you know for saying who said what: *según* and *dijo que*.'],
 ['I can say who said what, with *según* and *dijo que*.','I can tell what happened in Nicaragua in April 2018, with its sources.','I can say what happened to Sergio Ramírez and Gioconda Belli in 2023.'])
grammar(s,'According to Whom?',[
 {'type':'text','title':'What you already know','content':'You know *según* + the source and *decir que* from B1 Unit 13. After a past verb such as *dijo*, the verb inside moves back: *hay* becomes *había*, *hemos cometido* becomes *habían cometido*. When two sides disagree about the same events, each statement gets its own source. That keeps your voice out of it: you say who said what.'},
 {'type':'table','title':'Who said what','rows':[
  ['Según la ONU, murieron más de trescientas personas.','source first: According to the UN, more than three hundred people died.'],
  ['Los expertos dijeron que había violaciones graves.','dijo que + imperfect: The experts said there were serious violations.'],
  ['El gobierno dijo que las protestas eran un intento de golpe de Estado.','the other side, with its own source'],
  ['Según el gobierno, la protesta fue ilegal.','the other side, with según']]},
 {'type':'examples','title':'About Nicaragua','items':[
  {'spanish':'Según la Comisión Interamericana de Derechos Humanos, murieron más de trescientas personas en las protestas de 2018.','english':'According to the Inter-American Commission on Human Rights, more than three hundred people died in the 2018 protests.'},
  {'spanish':'Expertos de la ONU dijeron que el gobierno había cometido graves violaciones de derechos humanos.','english':'UN experts said that the government had committed serious human rights violations.'},
  {'spanish':'El gobierno dijo que las protestas eran un intento de golpe de Estado.','english':'The government said that the protests were an attempt at a coup.'},
  {'spanish':'Según Sergio Ramírez, los escritores en el exilio siguen escribiendo sobre Nicaragua.','english':'According to Sergio Ramírez, writers in exile keep writing about Nicaragua.'}]},
 {'type':'tip','content':'After *decir* there is no *de*: *dijeron que había*, not *dijeron de que había*. With *según* you do not need *que*. Always give each side its own source, and put no opinion of your own in the sentence.'}])
vocab(s,'Protest and exile','The protests, the exile and the sources',[
 ('la protesta','protest','noun'),('el exilio','exile','noun'),('la nacionalidad','nationality, citizenship','noun'),
 ('el derecho','right; law','noun'),('el gobierno','government','noun'),('el experto','expert','noun')])
ex(s,[
 match(s+'.ex01',[['la protesta','protest'],['el exilio','exile'],['la nacionalidad','nationality, citizenship'],['el experto','expert']],U),
 mc(s+'.ex02','In 2018 the students said: "Queremos justicia." Which sentence reports this correctly?',
  ['Los estudiantes dijeron que querían justicia.','Los estudiantes dijeron querían justicia.','Los estudiantes dijeron de que querían justicia.'],teaches=T),
 fb(s+'.ex03','__ la ONU, murieron más de trescientas personas durante las protestas de 2018.','Según','According to the UN, more than three hundred people died during the 2018 protests.',T),
 sb(s+'.ex04',['El','gobierno','dijo','que','las','protestas','eran','un','intento','de','golpe','de','Estado.'],'The government said that the protests were an attempt at a coup.',T),
 dlg(s+'.ex05',[('Meg','¿Qué dijeron los expertos de la ONU sobre Nicaragua?'),('Carlos','_____'),('Meg','Y el gobierno, ¿qué dijo?')],
  ['Dijeron que el gobierno había violado derechos humanos.','Dijeron que Rubén Darío había publicado «Azul…» en Chile.','Dijeron que el lago Cocibolca tenía tiburones.'],U),
 dic(s+'.ex06','Según la ONU, murieron más de trescientas personas durante las protestas.','According to the UN, more than three hundred people died during the protests.',T)])
story(s,'Nicaragua desde 2018: protestas, exilio y gobierno','Since April 2018 Nicaragua has seen protests, repression, the loss of nationality of more than three hundred people in 2023 and a 2025 constitutional reform; each claim is given with its source.',
 ['Protestas de 2018','Exilio','Gobierno actual'],['según','dijo que'],[
 'En abril de 2018 hubo en Nicaragua protestas contra una reforma de la seguridad social. Al principio protestaron sobre todo estudiantes y jubilados; después se sumaron muchas personas más, que pedían cambios políticos. Según la Comisión Interamericana de Derechos Humanos (CIDH), murieron más de trescientas personas durante las protestas, y la mayoría de las muertes fue causada por la policía y por grupos armados que apoyaban al gobierno.',
 'El gobierno de Daniel Ortega dijo que las protestas eran un intento de golpe de Estado y que había defendido el orden. Expertos de la ONU y la CIDH dijeron después que el gobierno había cometido graves violaciones de derechos humanos, como detenciones arbitrarias; el gobierno rechaza esas acusaciones.',
 'Desde 2018, el gobierno cerró muchas organizaciones civiles, medios de comunicación y universidades. En febrero de 2023 envió a Estados Unidos a 222 presos políticos y les quitó la nacionalidad nicaragüense; días después, otras 94 personas, entre ellas los escritores Sergio Ramírez y Gioconda Belli, perdieron también la nacionalidad. Según el gobierno, eran «traidores a la patria».',
 'Ramírez, que recibió el Premio Cervantes en 2017, y Belli siguen escribiendo desde el exilio. En 2025 una reforma de la Constitución convirtió a Daniel Ortega y a su esposa, Rosario Murillo, en copresidentes del país. Según el gobierno, la reforma fortalece al Estado; según organismos de derechos humanos y expertos de la ONU, aumenta la concentración del poder.'],
 [('What does the text say the Inter-American Commission reported about the 2018 protests?',['Murieron más de trescientas personas.','No murió nadie.','Ganó el gobierno las elecciones.','Terminaron en un día.'],0,'The text says more than three hundred people died.'),
  ('What did the government say about the protests?',['Dijo que eran un intento de golpe de Estado.','Dijo que eran una fiesta.','Dijo que no existieron.','Dijo que las pidió la ONU.'],0,'The text says the government called them an attempt at a coup.'),
  ('What happened in 2025, according to the text?',['Una reforma convirtió a Ortega y Murillo en copresidentes.','Se firmó el pacto de Tipitapa.','Se cerró el lago Cocibolca.','Sandino volvió al país.'],0,'The text says a constitutional reform made them co-presidents.')])

# ---------- consolidation ----------
s='b2-nicaragua-consolidation'
lesson(s,'Unit 6 Consolidation: Nicaragua',
 'Review the lake and volcanoes, Darío, Sandino, the revolution and the 2018 protests, with the grammar you used to talk about them.',
 'review: porque and por eso, fronting, si + hubiera, a pesar de, según and dijo que',
 [],
 ['I can review what I learned about Nicaragua, from Lake Cocibolca to the present day.',
  'I can use *porque* and *por eso*, fronting, *si hubiera… habría…*, *a pesar de* and *según*.',
  'I can put events from Darío to the 2023 exile in order.',
  'I can say who said what about recent events.'],
 ['I can give a reason with *porque* and a result with *por eso*.','I can put the important piece first, as in *Decisiva fue…*.','I can say what would have happened if something had been different, with *si hubiera… habría…*.','I can say that something went on in spite of a difficulty with *a pesar de*, and name my source with *según*.'])
ex(s,[
 match(s+'.ex01',[['el cráter','crater'],['el verso','line of poetry'],['el guerrillero','guerrilla fighter'],['el exilio','exile']],U),
 {'id':s+'.ex02','type':'multiple-choice','category':'reading','question':'According to the texts, where did Rubén Darío die?','options':['En León.','En Managua.','En Valparaíso.','En Granada.'],'correct':0},
 mc(s+'.ex03','Which sentence says "In spite of being very poor, the peasants began to paint"?',
  ['A pesar de ser muy pobres, los campesinos empezaron a pintar.','A pesar de eran muy pobres, los campesinos empezaron a pintar.','A pesar que eran muy pobres, los campesinos empezaron a pintar.'],teaches='a-pesar-de'),
 fb(s+'.ex04','Ometepe tiene forma de ocho __ la forman dos volcanes.','porque','Ometepe is shaped like an eight because two volcanoes form it.','porque-y-por-eso'),
 {'id':s+'.ex05','type':'sentence-order','category':'grammar','sentences':[
  'En 1888 Darío publicó «Azul…» en Chile. [In 1888 Darío published Azul… in Chile.]',
  'En 1927 Sandino rechazó el pacto de Tipitapa. [In 1927 Sandino rejected the Tipitapa pact.]',
  'En 1980 empezó la cruzada de alfabetización. [In 1980 the literacy crusade began.]',
  'En 2018 hubo grandes protestas en Nicaragua. [In 2018 there were big protests in Nicaragua.]'],'solution':[0,1,2,3],'teaches':['preterito-indefinido']},
 dlg(s+'.ex06',[('Meg','¿Qué dijo el gobierno sobre las protestas de 2018?'),('Carlos','_____'),('Meg','Y los expertos de la ONU dijeron otra cosa.')],
  ['Dijo que eran un intento de golpe de Estado.','Dijo que Sandino había rechazado el pacto.','Dijo que el lago tenía tiburones de agua dulce.'],U),
 dic(s+'.ex07','Si Sandino no hubiera ido a las montañas, no habría empezado esa guerra.','If Sandino had not gone to the mountains, he would not have begun that war.','pluscuamperfecto-subjuntivo-si'),
 {'id':s+'.ex08','type':'structured-writing','category':'writing','template':[
  {'prompt':'Say that the lake is very big and that is why it sometimes has waves. Use "por eso".','answer':'El lago es muy grande; por eso a veces tiene olas.'},
  {'prompt':'Say that, according to the UN, more than three hundred people died. Start with "Según".','answer':'Según la ONU, murieron más de trescientas personas.'},
  {'prompt':'Say that in León Rubén Darío died. Put "En León" first.','answer':'En León murió Rubén Darío.'}],'teaches':[U]}])
