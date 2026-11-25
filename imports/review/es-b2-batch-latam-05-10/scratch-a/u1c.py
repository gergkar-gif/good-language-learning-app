from lib import *
U='b2-el-salvador-honduras-vocab'
# ---------- 04 ----------
s='b2-salvadorhonduras-04'; T='formal-cause-connectors'
lesson(s,'Migration and remittances: families between Central America and the United States',
 'Explain why people leave El Salvador and Honduras and what remittances do, with debido a and a raíz de.',
 'formal cause connectors: debido a, a raíz de (review)',
 ['In this lesson you read about migration from El Salvador and Honduras and about the money migrants send home. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for giving a cause in a formal way: *debido a* and *a raíz de*.'],
 ['I can give a cause with *debido a* and *a raíz de* and a noun.','I can say why many people leave El Salvador and Honduras.','I can explain what remittances are and what families use them for.'])
grammar(s,'Because of the War, Because of the Storm',[
 {'type':'text','title':'What you already know','content':'You know *debido a* and *a raíz de* from B1 Unit 6, and *porque* from A1 and *por eso* from A2 Unit 5. *Debido a* and *a raíz de* are formal and take a noun, never a verb. With a verb, use *porque*. They are useful when you explain why people move: a war, a storm, a lack of work.'},
 {'type':'table','title':'Cause + noun','rows':[
  ['Debido a la guerra, muchas familias salieron del país.','Because of the war, many families left the country.'],
  ['A raíz del huracán Mitch, muchos hondureños emigraron.','As a result of Hurricane Mitch, many Hondurans emigrated.'],
  ['Debido a la sequía, las familias perdieron sus cosechas.','Because of the drought, families lost their harvests.'],
  ['Muchos emigraron porque no había trabajo.','Many emigrated because there was no work.']]},
 {'type':'examples','title':'On the road north','items':[
  {'spanish':'A raíz de la guerra civil, muchos salvadoreños viajaron a Estados Unidos.','english':'As a result of the civil war, many Salvadorans travelled to the United States.'},
  {'spanish':'Debido a la violencia y a la pobreza, algunas familias decidieron salir.','english':'Because of violence and poverty, some families decided to leave.'},
  {'spanish':'Debido a las remesas, muchas familias pueden pagar la comida y la escuela.','english':'Because of remittances, many families can pay for food and school.'},
  {'spanish':'Muchos niños viven con sus abuelos porque sus padres trabajan lejos.','english':'Many children live with their grandparents because their parents work far away.'}]},
 {'type':'tip','content':'*Debido a* needs *a* and *a raíz de* needs *de*: not *debido de*, not *a raíz la guerra*. Before a verb, use *porque*: not *debido a hubo una sequía*.'}])
vocab(s,'Leaving and sending money home','Migration, remittances and the journey',[
 ('la remesa','remittance, money sent home','noun'),('emigrar','to emigrate','verb'),('el migrante','migrant','noun'),('el huracán','hurricane','noun'),
 ('la sequía','drought','noun'),('el albergue','shelter, hostel','noun'),('la pandilla','gang','noun')])
ex(s,[
 match(s+'.ex01',[['la remesa','remittance, money sent home'],['la sequía','drought'],['el huracán','hurricane'],['el albergue','shelter, hostel']],U),
 mc(s+'.ex02','Which sentence says "Because of the drought, many families lost their harvests"?',
  ['Debido a la sequía, muchas familias perdieron sus cosechas.','Debido a hubo una sequía, muchas familias perdieron sus cosechas.','Debido de la sequía, muchas familias perdieron sus cosechas.'],teaches=T),
 fb(s+'.ex03','A __ de la guerra, muchas familias salieron del país.','raíz','As a result of the war, many families left the country.',T),
 sb(s+'.ex04',['Debido','a','la','pobreza','y','a','la','violencia,','muchas','personas','emigran.'],'Because of poverty and violence, many people emigrate.',T),
 dlg(s+'.ex05',[('Meg','¿Por qué emigraron tantos hondureños en 1998 y 1999?'),('Carlos','_____'),('Meg','Ahora entiendo mejor la historia.')],
  ['A raíz del huracán Mitch, muchas familias perdieron sus casas y sus cosechas.','A raíz de la huelga de 1954, los trabajadores pidieron mejores salarios.','A raíz del golfo de Fonseca, tres países compartieron sus aguas.'],U),
 dic(s+'.ex06','Debido a la violencia de las pandillas, muchos migrantes salen del país.','Because of gang violence, many migrants leave the country.',T)])
story(s,'Migración y remesas: familias entre dos países','Many people left El Salvador and Honduras because of war, hurricanes, drought and violence; the money they send home is a large part of both economies, and many families live apart.',
 ['Migración','Remesas','Familias separadas'],['debido a','a raíz de'],[
 'A raíz de la guerra civil, que empezó en 1980, muchos salvadoreños salieron de su país, y muchos viajaron a Estados Unidos. En Honduras, el huracán Mitch destruyó casas, puentes y cultivos en 1998. A raíz de ese desastre, más hondureños emigraron.',
 'Después llegaron otras razones. Debido a la pobreza, a la falta de trabajo y a la violencia de las pandillas, muchas familias decidieron salir. En el llamado Corredor Seco de Centroamérica, que incluye zonas de los dos países, la sequía arruinó cosechas de maíz y de frijoles. En noviembre de 2020, los huracanes Eta e Iota golpearon Honduras.',
 'Muchos migrantes cruzan México para llegar a Estados Unidos. El viaje es largo y peligroso. Según organizaciones de ayuda a los migrantes, muchas personas sufren robos, secuestros o accidentes en el camino. Algunos albergues de iglesias y de organizaciones civiles les dan comida, medicinas y consejos.',
 'Ya en Estados Unidos, muchos trabajan en la construcción, en restaurantes o en la limpieza, y envían dinero a sus familias. Ese dinero se llama «remesa». Según el Banco Mundial, en 2023 las remesas equivalían a cerca de una cuarta parte de la economía de cada uno de los dos países. Con ellas, las familias pagan comida, medicinas y escuela, y algunas construyen una casa.',
 'Pero el dinero no lo resuelve todo. Muchos niños crecen con sus abuelos o sus tíos mientras sus padres trabajan lejos, y hablan con ellos por videollamada. Al mismo tiempo, la cultura de los dos países viaja: las pupusas, unas tortillas rellenas típicas de El Salvador, se comen hoy en muchas ciudades de Estados Unidos.'],
 [('Why did more Hondurans emigrate after 1998?',['Un huracán destruyó casas, puentes y cultivos.','Cerraron las plantaciones de banano.','Empezó la guerra civil.','Terminó la huelga.'],0,'The text says Hurricane Mitch destroyed houses, bridges and crops.'),
  ('What are remittances, according to the text?',['Dinero que los migrantes envían a sus familias.','Un tipo de visa.','Un tren de carga.','Una ley de México.'],0,'The text says it is money sent to their families.'),
  ('What happens to many children, according to the text?',['Crecen con sus abuelos o sus tíos.','Viajan solos a Copán.','Trabajan en las plantaciones.','Estudian en México.'],0,'The text says many grow up with grandparents or aunts and uncles.')])

# ---------- 05 ----------
s='b2-salvadorhonduras-05'; T='ser-passive'
lesson(s,'El Salvador and Honduras today: security, money and elections',
 'Describe, with dates and sources, what happened recently in El Salvador and Honduras, using the passive with ser.',
 'passive with ser + past participle (review)',
 ['In this lesson you read about recent events in El Salvador and Honduras: the state of exception, bitcoin and the 2025 election. The text is in Spanish; the screens and instructions are in English. The facts are dated and attributed.',
  'The grammar is the one you know for saying what was done without making the doer the subject: *fue aprobado*, *fueron detenidas*.'],
 ['I can say what was approved, declared or announced, with *ser* + past participle.','I can name who says what about recent events in El Salvador and Honduras.','I can give the date of an event with the passive.'])
grammar(s,'Was Approved, Were Detained',[
 {'type':'text','title':'What you already know','content':'You know the passive with *ser* from B1 Unit 18: *ser* + past participle, and the participle agrees with the subject: *fue aprobada*, *fueron aprobados*. *Por* names who did it, but you can leave it out. For news about politics this is useful, because you can give the fact and the date without saying more. The surest way to talk about the present is to date it: *en marzo de 2022*, *en 2025*.'},
 {'type':'table','title':'Ser + past participle','rows':[
  ['El régimen fue aprobado por la Asamblea.','The regime was approved by the Assembly.'],
  ['La ley fue cambiada en enero de 2025.','The law was changed in January 2025.'],
  ['Los votos fueron contados durante semanas.','The votes were counted for weeks.'],
  ['Las elecciones fueron organizadas por el Consejo Nacional Electoral.','The elections were organised by the National Electoral Council.']]},
 {'type':'examples','title':'Recent events','items':[
  {'spanish':'El estado de excepción fue aprobado en marzo de 2022.','english':'The state of exception was approved in March 2022.'},
  {'spanish':'Según el Gobierno, más de noventa mil personas fueron detenidas.','english':'According to the government, more than ninety thousand people were detained.'},
  {'spanish':'El bitcoin fue declarado moneda de curso legal en 2021.','english':'Bitcoin was declared legal tender in 2021.'},
  {'spanish':'Nasry Asfura fue declarado ganador el 24 de diciembre de 2025.','english':'Nasry Asfura was declared the winner on 24 December 2025.'}]},
 {'type':'tip','content':'The participle agrees with the subject: *la ley fue cambiada*, *las personas fueron detenidas*. Add the date and the source, and the news stays factual: *según el Gobierno*, *según organizaciones de derechos humanos*.'}])
vocab(s,'Recent news','The state of exception, bitcoin and the election',[
 ('el estado de excepción','state of exception','noun'),('detener','to detain, to arrest','verb'),('el recuento','count, recount (of votes)','noun'),
 ('el voto','vote','noun'),('la moneda','currency','noun'),('el ganador','winner','noun'),('aprobar','to approve','verb')])
ex(s,[
 match(s+'.ex01',[['el estado de excepción','state of exception'],['el recuento','count, recount (of votes)'],['la moneda','currency'],['el ganador','winner']],U),
 mc(s+'.ex02','Which sentence says "The law was changed in January 2025"?',
  ['La ley fue cambiada en enero de 2025.','La ley fue cambiado en enero de 2025.','La ley fueron cambiada en enero de 2025.'],teaches=T),
 fb(s+'.ex03','Los votos __ contados durante varias semanas.','fueron','The votes were counted for several weeks.',T),
 sb(s+'.ex04',['El','estado','de','excepción','fue','aprobado','en','marzo','de','2022.'],'The state of exception was approved in March 2022.',T),
 dlg(s+'.ex05',[('Meg','¿Cuándo fue declarado ganador Nasry Asfura?'),('Carlos','_____'),('Meg','Gracias, ahora tengo la fecha.')],
  ['Fue declarado ganador el 24 de diciembre de 2025, después de un recuento largo.','Fue declarado ganador en marzo de 2022, junto con el estado de excepción.','Fue declarado ganador en 1992, cuando se firmó la paz en México.'],U),
 dic(s+'.ex06','Según el Gobierno, más de noventa mil personas fueron detenidas.','According to the government, more than ninety thousand people were detained.',T)])
story(s,'El Salvador y Honduras hoy: seguridad, dinero y elecciones','Recent events, dated and attributed: El Salvador\'s state of exception and bitcoin law, and Honduras\'s 2025 election and its disputed count.',
 ['Estado de excepción','Bitcoin','Elecciones en Honduras'],['pasiva con ser'],[
 'Durante años, las pandillas, como la Mara Salvatrucha y el Barrio 18, cobraron dinero a comerciantes y vecinos en muchos barrios de El Salvador. En marzo de 2022, después de un fin de semana de muchos asesinatos, la Asamblea Legislativa aprobó un estado de excepción, y desde entonces ha sido prorrogado cada mes; en 2026 sigue vigente.',
 'Según el Gobierno de Nayib Bukele, más de noventa mil personas fueron detenidas hasta 2026, y los homicidios bajaron mucho. Según organizaciones de derechos humanos, algunas de las personas detenidas no tenían relación con las pandillas, y varias murieron bajo custodia. El Gobierno rechaza esas críticas.',
 'En septiembre de 2021, El Salvador fue el primer país en declarar el bitcoin moneda de curso legal, junto con el dólar. En enero de 2025, la ley fue cambiada: desde entonces nadie está obligado a aceptar bitcoin como pago.',
 'En Honduras, las elecciones presidenciales fueron el 30 de noviembre de 2025. El recuento de los votos duró semanas, y hubo acusaciones de irregularidades. El 24 de diciembre, el candidato del Partido Nacional, Nasry Asfura, fue declarado ganador por un margen estrecho frente a Salvador Nasralla. La presidenta saliente, Xiomara Castro, habló de fraude. Asfura asumió la presidencia el 27 de enero de 2026.'],
 [('According to the text, what happened in El Salvador in March 2022?',['La Asamblea aprobó un estado de excepción.','Se firmó la paz.','Se cambió el nombre del país.','Se cerró el golfo.'],0,'The text says the Assembly approved a state of exception.'),
  ('What changed about bitcoin in January 2025?',['Nadie está obligado a aceptarlo como pago.','Fue declarado moneda legal por primera vez.','Fue prohibido.','Fue cambiado por el lempira.'],0,'The text says the law was changed so that no one is obliged to accept it.'),
  ('What does the text say about Honduras after the 2025 election?',['El recuento duró semanas y hubo acusaciones de irregularidades.','Hubo un solo candidato.','Las elecciones fueron en 2022.','Nadie quiso asumir la presidencia.'],0,'The text says the count lasted weeks and several candidates alleged irregularities.')])

# ---------- consolidation ----------
s='b2-salvadorhonduras-consolidation'
lesson(s,'Unit 5 Consolidation: El Salvador and Honduras',
 'Review Copán, northern Honduras, Romero and the war, migration, and recent events, with the grammar you used to talk about them.',
 'review: cuyo, dijo que and según, sin embargo and no obstante, debido a and a raíz de, the passive with ser',
 [],
 ['I can review what I learned about El Salvador and Honduras, from Copán to recent events.',
  'I can use *cuyo*, *dijo que* and *según*, *sin embargo* and *no obstante*, *debido a* and *a raíz de*, and the passive with *ser*.',
  'I can put events from Copán to the 2025 election in order.',
  'I can cite a source when I talk about recent events.'],
 ['I can say whose monuments or coasts I mean, with *cuyo*.','I can report what people said and name my source, with *dijo que* and *según*.','I can show a contrast with *sin embargo* and *no obstante*.','I can give a cause with *debido a* and *a raíz de*, and a dated fact with the passive with *ser*.'])
ex(s,[
 match(s+'.ex01',[['la estela','stela, carved stone slab'],['la huelga','strike'],['la remesa','remittance, money sent home'],['el arzobispo','archbishop']],U),
 {'id':s+'.ex02','type':'multiple-choice','category':'reading','question':'According to the texts, what did the Peace Accords of 1992 do?','options':['Crearon una nueva policía civil.','Dieron la presidencia a Nasry Asfura.','Cerraron las plantaciones de fruta.','Cambiaron el nombre del país.'],'correct':0},
 mc(s+'.ex03','Which sentence says "Because of the drought, families lost their harvests"?',
  ['Debido a la sequía, las familias perdieron sus cosechas.','Debido a hubo una sequía, las familias perdieron sus cosechas.','Debido de la sequía, las familias perdieron sus cosechas.'],teaches='formal-cause-connectors'),
 fb(s+'.ex04','Copán es una ciudad __ estelas fueron talladas en piedra.','cuyas','Copán is a city whose stelae were carved in stone.','relativo-posesivo-cuyo'),
 {'id':s+'.ex05','type':'sentence-order','category':'grammar','sentences':[
  'En 1797 los británicos llevaron a los garífunas a Roatán. [In 1797 the British took the Garífuna to Roatán.]',
  'En 1954 los trabajadores bananeros hicieron una huelga. [In 1954 the banana workers went on strike.]',
  'En 1992 se firmó la paz en Ciudad de México. [In 1992 peace was signed in Mexico City.]',
  'En 2001 la UNESCO proclamó la cultura garífuna. [In 2001 UNESCO proclaimed Garífuna culture.]'],'solution':[0,1,2,3],'teaches':['preterito-indefinido']},
 dlg(s+'.ex06',[('Meg','¿Qué dijeron los garífunas sobre sus tierras?'),('Carlos','_____'),('Meg','Entonces es un tema muy importante.')],
  ['Dijeron que habían perdido tierras de la costa.','Dijeron que el golfo tenía manglares.','Dijeron que la guerra había durado doce años.'],U),
 dic(s+'.ex07','Los garífunas dijeron que habían perdido tierras de la costa.','The Garífuna said that they had lost land on the coast.','estilo-indirecto-informacion'),
 {'id':s+'.ex08','type':'structured-writing','category':'writing','template':[
  {'prompt':'Say that the war lasted twelve years but peace was signed in 1992. Use "Sin embargo".','answer':'La guerra duró doce años. Sin embargo, en 1992 se firmó la paz.'},
  {'prompt':'Say that the workers said they wanted better wages. Start with "Los trabajadores dijeron".','answer':'Los trabajadores dijeron que querían mejores salarios.'},
  {'prompt':'Say that, because of the war, many families left the country. Start with "Debido a".','answer':'Debido a la guerra, muchas familias salieron del país.'}],'teaches':[U]}])
