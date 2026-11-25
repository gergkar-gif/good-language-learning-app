from lib import *
U='b2-costa-rica-vocab'
# ---------- 01 ----------
s='b2-costarica-01'; T='oraciones-hendidas-enfasis'
lesson(s,'Costa Rica\'s biodiversity: volcanoes, cloud forests and rainforests',
 'Describe the nature of Costa Rica and put the key piece in the spotlight, with cleft sentences.',
 'cleft sentences: Fue en… donde…, Lo que… es… (review)',
 ['In this lesson you read about the nature of Costa Rica: its volcanoes, its cloud forest of Monteverde, Corcovado and the turtles of Tortuguero. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for putting one piece in the spotlight: *Fue en Monteverde donde…*, *Lo que más sorprende es…*.'],
 ['I can put a place, a time or an idea in the spotlight with *Fue… donde / cuando* and *Lo que… es…*.','I can say where the cloud forest, the rainforest and the turtle beaches of Costa Rica are.','I can explain why such a small country has so many species.'])
grammar(s,'The Spotlight on Nature',[
 {'type':'text','title':'What you already know','content':'You know cleft sentences with *lo que* from B2 Unit 1, and with *fue… donde* and *fue… cuando*. They put one piece of the sentence in the spotlight. Nature texts use them to point at the place or the time that matters: *Fue en Monteverde donde…*, *Fue hace tres millones de años cuando…*.'},
 {'type':'table','title':'Three ways to build the spotlight','rows':[
  ['Lo que + verb + ser + focus','Lo que más sorprende es la variedad de especies.'],
  ['Fue / Es + place + donde','Fue en Monteverde donde se protegió el bosque nuboso.'],
  ['Fue / Es + time + cuando','Fue hace unos tres millones de años cuando el istmo unió las dos Américas.'],
  ['Es + place + donde','Es en Tortuguero donde las tortugas verdes ponen sus huevos.']]},
 {'type':'examples','title':'In Costa Rica','items':[
  {'spanish':'Lo que más sorprende en Costa Rica es la variedad de especies en un país tan pequeño.','english':'What surprises most in Costa Rica is the variety of species in such a small country.'},
  {'spanish':'Fue hace unos tres millones de años cuando el istmo unió América del Norte y América del Sur.','english':'It was about three million years ago that the isthmus joined North and South America.'},
  {'spanish':'Es en la costa del Caribe donde las tortugas verdes ponen sus huevos.','english':'It is on the Caribbean coast that the green turtles lay their eggs.'},
  {'spanish':'Fue en la península de Osa donde se creó el Parque Nacional Corcovado.','english':'It was on the Osa Peninsula that Corcovado National Park was created.'}]},
 {'type':'tip','content':'Use *donde* for a place and *cuando* for a time: not *Fue en Monteverde cuando…*. The spotlight is for the one idea you want the reader to remember; do not use it in every sentence.'}])
vocab(s,'Forests, volcanoes and species','Nature in Costa Rica',[
 ('el bosque nuboso','cloud forest','noun'),('la especie','species','noun'),('el istmo','isthmus','noun'),('la tortuga','turtle','noun'),
 ('el parque nacional','national park','noun'),('la selva','rainforest, jungle','noun'),('desovar','to lay eggs (of turtles, fish)','verb')])
ex(s,[
 match(s+'.ex01',[['el bosque nuboso','cloud forest'],['la especie','species'],['el istmo','isthmus'],['la selva','rainforest, jungle']],U),
 mc(s+'.ex02','Which sentence says "It was in Monteverde that the cloud forest was protected"?',
  ['Fue en Monteverde donde se protegió el bosque nuboso.','Fue en Monteverde cuando se protegió el bosque nuboso.','Fue en Monteverde quien se protegió el bosque nuboso.'],teaches=T),
 fb(s+'.ex03','__ que más sorprende en Costa Rica es la variedad de especies.','Lo','What surprises most in Costa Rica is the variety of species.',T),
 sb(s+'.ex04',['Fue','en','la','península','de','Osa','donde','se','creó','el','parque','nacional','Corcovado.'],'It was on the Osa Peninsula that Corcovado National Park was created.',T),
 dlg(s+'.ex05',[('Meg','¿Dónde desovan las tortugas verdes?'),('Carlos','_____'),('Meg','Qué bonito. Quiero verlas.')],
  ['Es en Tortuguero, en la costa del Caribe, donde desovan.','Es en Monteverde, en el bosque nuboso, donde desovan.','Es en el volcán Arenal, en el norte, donde desovan.'],U),
 dic(s+'.ex06','Lo que más sorprende en Costa Rica es la variedad de especies en un país pequeño.','What surprises most in Costa Rica is the variety of species in a small country.',T)])
story(s,'La naturaleza de Costa Rica','A small country between two oceans, Costa Rica has volcanoes, the cloud forest of Monteverde, the rainforest of Corcovado and the turtle beaches of Tortuguero, and many species.',
 ['Biodiversidad','Volcanes y bosques','Parques nacionales'],['oraciones hendidas'],[
 'Costa Rica es un país pequeño, de poco más de cincuenta mil kilómetros cuadrados, entre el mar Caribe y el océano Pacífico. Según estimaciones que se citan con frecuencia, en su territorio vive alrededor del cinco por ciento de las especies del planeta. Lo que más sorprende es esa variedad en un espacio tan reducido.',
 'Una de las razones es la historia del istmo. Fue hace unos tres millones de años cuando el istmo de Centroamérica unió América del Norte y América del Sur. Por ese puente pasaron plantas y animales de las dos regiones. Hoy el país tiene además cadenas de volcanes, como el Arenal, el Irazú y el Poás, y muchos climas diferentes en distancias cortas.',
 'En la sierra de Tilarán está el bosque nuboso de Monteverde, donde las nubes mantienen húmedos los árboles, cubiertos de musgo y de orquídeas. Fue en Monteverde donde se protegió una parte importante de ese bosque. Más al sur, en la península de Osa, está el Parque Nacional Corcovado, una selva húmeda donde viven jaguares, pumas y monos. La revista National Geographic lo ha descrito como uno de los lugares con más biodiversidad del planeta.',
 'En la costa del Caribe, el parque nacional de Tortuguero tiene canales, lagunas y manglares. Es en esas playas donde las tortugas verdes desovan, sobre todo entre julio y octubre. Cada noche, las hembras salen del mar, hacen un nido en la arena y dejan allí sus huevos.',
 'Según varios científicos, el cambio climático amenaza a algunas especies del bosque nuboso, como ciertas ranas, porque cambia el lugar donde se forman las nubes. Por eso los parques nacionales y los corredores entre ellos son muy importantes para proteger la naturaleza del país.'],
 [('What joined North and South America, according to the text?',['El istmo de Centroamérica.','El mar Caribe.','El volcán Arenal.','El canal de Panamá.'],0,'The text says the isthmus joined the two Americas about three million years ago.'),
  ('Where do the green turtles lay their eggs?',['En Tortuguero, en la costa del Caribe.','En Monteverde.','En el volcán Poás.','En la península de Osa.'],0,'The text says they lay eggs on the beaches of Tortuguero.'),
  ('What lives in Corcovado, according to the text?',['Jaguares, pumas y monos.','Solo aves del mar.','Tiburones de agua dulce.','Ningún animal.'],0,'The text mentions jaguars, pumas and monkeys.')])

# ---------- 02 ----------
s='b2-costarica-02'; T='refutacion-no-es-que-sino'
lesson(s,'1948 and the abolition of the army: a country without an army',
 'Tell how Costa Rica abolished its army in 1948-1949 and correct a wrong reason, with no es que… sino que….',
 'refuting a reason: no es que… sino que… (review)',
 ['In this lesson you read about the civil war of 1948 and the decision to abolish the army in Costa Rica. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for correcting a reason: *No es que… sino que…*.'],
 ['I can correct a reason with *No es que… sino que…*.','I can tell what happened in Costa Rica in 1948 and 1949.','I can explain who guards Costa Rica without an army.'])
grammar(s,'Not That… but That…',[
 {'type':'text','title':'What you already know','content':'You know *No es que* + subjunctive, *sino que* + indicative from B2 Unit 5. It rejects a reason someone might assume and gives the real one. It is useful here, because people often assume that a country without an army has no security: *No es que Costa Rica no tenga seguridad, sino que la dan policías civiles*.'},
 {'type':'table','title':'The pattern','rows':[
  ['No es que + subjunctive','the reason you reject: No es que Costa Rica no tenga policía, …'],
  ['sino que + indicative','the true reason: … sino que no tiene ejército.'],
  ['No era que + imperfect subjunctive','in the past: No era que el país no necesitara seguridad, …'],
  ['… sino que + imperfect','… sino que la daba la policía.']]},
 {'type':'examples','title':'About a country without an army','items':[
  {'spanish':'No es que Costa Rica no tenga policía, sino que no tiene ejército.','english':'It is not that Costa Rica has no police, but that it has no army.'},
  {'spanish':'No es que Costa Rica no necesite seguridad, sino que la da una policía civil.','english':'It is not that Costa Rica does not need security, but that civilian police provide it.'},
  {'spanish':'No es que la guerra civil de 1948 fuera larga, sino que fue muy violenta.','english':'It is not that the 1948 civil war was long, but that it was very violent.'},
  {'spanish':'No es que Figueres quisiera el poder para siempre, sino que prometió una nueva Constitución.','english':'It is not that Figueres wanted power forever, but that he promised a new Constitution.'}]},
 {'type':'tip','content':'Do not use the indicative after *no es que*: not *No es que no tiene*. And do not drop *que* after *sino*: not *sino no tiene*.'}])
vocab(s,'War, army and police','The 1948 civil war and the abolition of the army',[
 ('el ejército','army','noun'),('el cuartel','barracks','noun'),('la policía','police','noun'),
 ('abolir','to abolish','verb'),('la neutralidad','neutrality','noun')])
ex(s,[
 match(s+'.ex01',[['el ejército','army'],['el cuartel','barracks'],['abolir','to abolish'],['la neutralidad','neutrality']],U),
 mc(s+'.ex02','Which sentence says "It is not that Costa Rica has no police, but that it has no army"?',
  ['No es que Costa Rica no tenga policía, sino que no tiene ejército.','No es que Costa Rica no tiene policía, sino que no tiene ejército.','No es que Costa Rica no tenga policía, sino no tiene ejército.'],teaches=T,ds={1:'present-tense'}),
 fb(s+'.ex03','No es que Costa Rica no necesite seguridad, __ que la da una policía civil.','sino','It is not that Costa Rica does not need security, but that a civilian police provides it.',T),
 sb(s+'.ex04',['No','es','que','Costa','Rica','no','tenga','seguridad,','sino','que','la','dan','policías','civiles.'],'It is not that Costa Rica has no security, but that civilian police provide it.',T),
 dlg(s+'.ex05',[('Meg','Costa Rica no tiene ejército. ¿No tiene seguridad?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],
  ['No es que no tenga seguridad, sino que la dan policías civiles.','No es que no tenga seguridad, sino que tiene un ejército pequeño.','No es que no tenga seguridad, sino que la daba el ejército hasta 1983.'],U),
 dic(s+'.ex06','No es que no haya seguridad, sino que la seguridad la da la policía civil.','It is not that there is no security, but that security is provided by the civilian police.',T)])
story(s,'1948: el país que abolió su ejército','After a civil war in 1948, Costa Rica abolished its army; the 1949 Constitution forbids a permanent army and civilian police provide security.',
 ['Guerra civil de 1948','Abolición del ejército','Policía civil'],['no es que… sino que…'],[
 'En 1948, unas elecciones presidenciales en Costa Rica terminaron en una disputa: el Congreso anuló el resultado, y una parte del país no aceptó esa decisión. Siguió una guerra civil de cuarenta y cuatro días, entre marzo y abril de 1948. No es que la guerra fuera larga, sino que dejó muchas muertes y una profunda división.',
 'José Figueres Ferrer dirigió a los rebeldes, y su Junta Fundadora de la Segunda República gobernó el país durante unos dieciocho meses. El 1 de diciembre de 1948, Figueres golpeó simbólicamente una pared del Cuartel Bellavista, en San José, para anunciar el fin del ejército. Más tarde, el cuartel se convirtió en el Museo Nacional.',
 'La Constitución de 1949 lo dejó escrito en su artículo 12: «Se proscribe el Ejército como institución permanente». Según muchos historiadores, el país pudo destinar una parte mayor de su presupuesto a la educación y a la salud. No es que Costa Rica no tenga policía, sino que no tiene ejército: la seguridad la dan la Fuerza Pública y otras fuerzas civiles.',
 'En 1983, el presidente Luis Alberto Monge proclamó la neutralidad perpetua, activa y no armada del país. En 1987, el presidente Óscar Arias recibió el Premio Nobel de la Paz por su papel en un plan de paz para Centroamérica. Hoy el país sigue sin ejército; en los últimos años, sin embargo, hay un debate sobre cómo enfrentar el crimen organizado y el narcotráfico.'],
 [('What did Figueres do on 1 December 1948?',['Golpeó simbólicamente una pared del Cuartel Bellavista.','Firmó la Constitución de 1949.','Ganó el Premio Nobel.','Creó la CCSS.'],0,'The text says he symbolically struck a wall of the Bellavista barracks.'),
  ('What does Article 12 of the 1949 Constitution say?',['Se proscribe el Ejército como institución permanente.','Todos deben hacer servicio militar.','El ejército es neutral.','La policía debe ser militar.'],0,'The text quotes the article.'),
  ('What happened to the Bellavista barracks?',['Se convirtió en el Museo Nacional.','Fue destruido.','Volvió a ser un cuartel.','Se vendió.'],0,'The text says it became the National Museum.')])

# ---------- 03 ----------
s='b2-costarica-03'; T='el-hecho-de-que-subjuntivo'
lesson(s,'The welfare state: the CCSS, EBAIS and education',
 'Describe Costa Rica\'s health and education system and comment on a known fact, with el hecho de que + subjunctive.',
 'commenting on a fact: el hecho de que + subjunctive (review)',
 ['In this lesson you read about the Costa Rican social security system, its neighbourhood health teams and its schools. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for commenting on a fact everyone knows: *el hecho de que* + subjunctive.'],
 ['I can comment on a known fact with *el hecho de que* + subjunctive.','I can say what the CCSS and the EBAIS are.','I can name two challenges of the health system today.'])
grammar(s,'The Fact That…',[
 {'type':'text','title':'What you already know','content':'You know *el hecho de que* + subjunctive from B2 Unit 6. You use it for a fact both people already know, when you want to comment on it: *El hecho de que la CCSS exista desde 1941 no significa que no tenga problemas*. The comment agrees with *el hecho*, which is singular. After a past verb, use the imperfect subjunctive.'},
 {'type':'table','title':'El hecho de que + subjunctive','rows':[
  ['El hecho de que la población envejezca crea nuevos retos.','The fact that the population is getting older creates new challenges.'],
  ['El hecho de que los EBAIS lleguen a los barrios ayuda a los pacientes.','The fact that the EBAIS reach the neighbourhoods helps patients.'],
  ['El hecho de que la CCSS exista desde 1941 no significa que no tenga problemas.','The fact that the CCSS has existed since 1941 does not mean it has no problems.'],
  ['El hecho de que muchos niños fueran a la escuela cambió el país.','The fact that many children went to school changed the country.']]},
 {'type':'examples','title':'In Costa Rica','items':[
  {'spanish':'El hecho de que todos los trabajadores paguen una parte de su salario ayuda a financiar la CCSS.','english':'The fact that all workers pay part of their wages helps to finance the CCSS.'},
  {'spanish':'El hecho de que haya listas de espera preocupa a muchos pacientes.','english':'The fact that there are waiting lists worries many patients.'},
  {'spanish':'El hecho de que la educación primaria sea obligatoria desde el siglo XIX explica parte de la historia del país.','english':'The fact that primary education has been compulsory since the nineteenth century explains part of the country\'s history.'},
  {'spanish':'El hecho de que el sistema llegara a las zonas rurales cambió la vida de muchas familias.','english':'The fact that the system reached rural areas changed the life of many families.'}]},
 {'type':'tip','content':'Write *el hecho de que* with *de*: not *el hecho que*. The verb after *que* is in the subjunctive when you comment on the fact, and the comment stays singular: *El hecho de que lleguen tarde me molesta*, not *me molestan*.'}])
vocab(s,'Health and schools','The CCSS, the EBAIS and education',[
 ('la salud','health','noun'),('el seguro','insurance','noun'),('la enfermera','nurse','noun'),('envejecer','to grow old, to age','verb'),
 ('la lista de espera','waiting list','noun'),('obligatorio','compulsory','adjective')])
ex(s,[
 match(s+'.ex01',[['el seguro','insurance'],['la enfermera','nurse'],['la lista de espera','waiting list'],['obligatorio','compulsory']],U),
 mc(s+'.ex02','Which sentence says "The fact that the population is getting older creates new challenges"?',
  ['El hecho de que la población envejezca crea nuevos retos.','El hecho que la población envejezca crea nuevos retos.','El hecho de que la población envejecer crea nuevos retos.'],teaches=T),
 fb(s+'.ex03','El hecho de que la CCSS __ desde 1941 no significa que no tenga problemas.','exista','The fact that the CCSS has existed since 1941 does not mean it has no problems.',T,hint='existir'),
 sb(s+'.ex04',['El','hecho','de','que','los','EBAIS','lleguen','a','los','barrios','ayuda','a','los','pacientes.'],'The fact that the EBAIS reach the neighbourhoods helps patients.',T),
 dlg(s+'.ex05',[('Meg','¿Qué es un EBAIS?'),('Carlos','_____'),('Meg','Qué buena idea.')],
  ['Es un equipo de salud que visita a las familias del barrio.','Es un volcán de la cordillera de Tilarán, cerca de Monteverde.','Es un programa que paga por proteger los bosques de Costa Rica.'],U),
 dic(s+'.ex06','El hecho de que la población envejezca crea nuevos retos para la CCSS.','The fact that the population is getting older creates new challenges for the CCSS.',T)])
story(s,'El estado de bienestar costarricense','Costa Rica built a social security system in 1941, neighbourhood health teams in the 1990s and free, compulsory schooling; today it faces an ageing population and waiting lists.',
 ['La CCSS','Los EBAIS','Educación'],['el hecho de que + subjuntivo'],[
 'En 1941, durante el gobierno de Rafael Ángel Calderón Guardia, Costa Rica creó la Caja Costarricense de Seguro Social, conocida como la CCSS. Esta institución administra los seguros de salud y de pensiones. Los trabajadores y las empresas pagan una parte del salario, y la atención médica se ofrece a las personas aseguradas. El hecho de que la CCSS exista desde 1941 explica en parte por qué el país tiene hoy una red de salud tan amplia.',
 'En los años noventa, el sistema añadió los EBAIS, equipos básicos de salud de barrio. Un EBAIS tiene un médico, una enfermera y otros técnicos, y no espera a que los pacientes lleguen enfermos: visita a las familias y ofrece vacunas, consejos y controles. El hecho de que estos equipos lleguen a barrios y pueblos pequeños ayuda a que más personas reciban atención.',
 'Según varios investigadores, la península de Nicoya es una de las llamadas «zonas azules» del mundo, es decir, lugares donde muchas personas viven hasta edades muy avanzadas. Los estudios señalan factores como la alimentación, la vida en comunidad y el acceso a la atención de salud.',
 'La educación es otro pilar. La escuela primaria es obligatoria y gratuita desde el siglo XIX, y el sistema incluye universidades públicas, como la Universidad de Costa Rica.',
 'Hoy el sistema tiene retos. El hecho de que la población envejezca aumenta los gastos en salud, y hay listas de espera para algunas operaciones y consultas. También hay debates sobre cómo financiar las pensiones. Aun así, muchas personas consideran la CCSS una institución importante del país.'],
 [('When was the CCSS created?',['En 1941.','En 1948.','En 1983.','En 1996.'],0,'The text says the CCSS was created in 1941.'),
  ('What does an EBAIS do, according to the text?',['Visita a las familias y ofrece vacunas, consejos y controles.','Vigila los parques nacionales.','Paga el salario mínimo.','Organiza elecciones.'],0,'The text says it visits families and offers vaccines, advice and check-ups.'),
  ('What is one challenge of the system today?',['Hay listas de espera para algunas operaciones.','No hay médicos.','No hay escuelas.','No hay pensiones.'],0,'The text mentions waiting lists and an ageing population.')])
