from lib import *
U='b2-nicaragua-vocab'
# ---------- 01 ----------
s='b2-nicaragua-01'; T='porque-y-por-eso'
lesson(s,'Lake Cocibolca and Ometepe: a freshwater sea with two volcanoes',
 'Explain why Lake Cocibolca and the island of Ometepe are special, with porque and por eso.',
 'giving reasons and results with porque and por eso (review)',
 ['In this lesson you read about Lake Cocibolca (also called Lake Nicaragua), the island of Ometepe and its two volcanoes. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for giving a reason and a result: *porque* and *por eso*.'],
 ['I can give a reason with *porque* and a result with *por eso*.','I can explain why Lake Cocibolca was called a sea.','I can say why the island of Ometepe has the shape of an eight.'])
grammar(s,'Reasons and Results at the Lake',[
 {'type':'text','title':'What you already know','content':'You know *porque* from A1 Unit 2 and *por eso* from A2 Unit 5. *Porque* gives the reason ("because"); *por eso* gives the result ("that is why"). They are the simplest tools for explaining nature: why a lake has waves, why an island has a strange shape.'},
 {'type':'table','title':'Reason or result?','rows':[
  ['Ometepe tiene forma de ocho porque la forman dos volcanes.','reason: Ometepe is shaped like an eight because two volcanoes form it'],
  ['El lago es muy grande; por eso a veces tiene olas como el mar.','result: the lake is very big; that is why it sometimes has waves like the sea'],
  ['La isla es de origen volcánico; por eso su tierra es fértil.','result: the island is volcanic; that is why its soil is fertile'],
  ['¿Por qué lo llamaron «la Mar Dulce»? Porque parecía un mar.','question and answer: why did they call it "the Sweet Sea"? Because it looked like a sea']]},
 {'type':'examples','title':'At the lake','items':[
  {'spanish':'Los españoles lo llamaron «la Mar Dulce» porque parecía un mar, pero su agua era dulce.','english':'The Spaniards called it "the Sweet Sea" because it looked like a sea, but its water was fresh.'},
  {'spanish':'El volcán Concepción está activo; por eso se vigila con cuidado.','english':'The Concepción volcano is active; that is why it is watched carefully.'},
  {'spanish':'En el lago hay tiburones porque el río San Juan lo une con el mar Caribe.','english':'There are sharks in the lake because the San Juan river joins it to the Caribbean Sea.'},
  {'spanish':'Hay muchas islas pequeñas cerca de Granada porque un volcán cambió el paisaje hace miles de años.','english':'There are many small islands near Granada because a volcano changed the landscape thousands of years ago.'}]},
 {'type':'tip','content':'*Porque* (one word, no accent) gives a reason; *por qué* (two words, with an accent) asks "why?". *Por eso* starts a new clause, after a semicolon or a full stop: not *…; porque a veces tiene olas*, when you mean "that is why".'}])
vocab(s,'Lake, island and volcano','Lake Cocibolca, Ometepe and the volcanoes',[
 ('el cráter','crater','noun'),('el petroglifo','petroglyph, rock carving','noun'),('el tiburón','shark','noun'),('la ola','wave','noun'),
 ('fértil','fertile','adjective'),('la isleta','small island','noun'),('vigilar','to watch over, to monitor','verb')])
ex(s,[
 match(s+'.ex01',[['el cráter','crater'],['el petroglifo','petroglyph, rock carving'],['el tiburón','shark'],['la isleta','small island']],U),
 mc(s+'.ex02','Which sentence says "The lake is very big; that is why it sometimes has waves like the sea"?',
  ['El lago es muy grande; por eso a veces tiene olas como el mar.','El lago es muy grande; porque a veces tiene olas como el mar.','El lago es muy grande; por qué a veces tiene olas como el mar.'],teaches=T,ds={2:'por-que-y-porque'}),
 fb(s+'.ex03','Ometepe es de origen volcánico; __ eso su tierra es muy fértil.','por','Ometepe is volcanic in origin; that is why its soil is very fertile.',T),
 sb(s+'.ex04',['Ometepe','tiene','forma','de','ocho','porque','la','forman','dos','volcanes.'],'Ometepe is shaped like an eight because two volcanoes form it.',T),
 dlg(s+'.ex05',[('Meg','¿Por qué los españoles llamaron al lago «la Mar Dulce»?'),('Carlos','_____'),('Meg','Ahora entiendo el nombre.')],
  ['Porque parecía un mar, pero su agua era dulce.','Porque el río San Juan trae agua del mar Caribe.','Porque los volcanes de Ometepe son muy grandes.'],U),
 dic(s+'.ex06','El volcán Concepción está activo; por eso la gente lo vigila con cuidado.','The Concepción volcano is active; that is why people watch it carefully.',T)])
story(s,'El lago Cocibolca y la isla de Ometepe','Lake Cocibolca is the largest lake in Central America; the island of Ometepe, formed by two volcanoes, rises from it, and sharks swim in its fresh water.',
 ['El gran lago','Volcanes','Fauna y reserva'],['porque','por eso'],[
 'El lago Cocibolca, también llamado Gran Lago de Nicaragua, tiene unos ocho mil doscientos kilómetros cuadrados y es el lago más grande de Centroamérica. Es tan grande que a veces tiene olas como el mar. Por eso los cronistas españoles del siglo XVI lo llamaron «la Mar Dulce»: parecía un mar, pero su agua era dulce.',
 'En el centro del lago está la isla de Ometepe, que tiene forma de ocho porque la forman dos volcanes. El Concepción, al norte, es un volcán activo y casi perfecto. El Maderas, al sur, tiene en su cráter una laguna. Como la isla es de origen volcánico, su tierra es fértil, y en ella se cultivan plátanos y café. En la isla hay muchos petroglifos, tallados por pueblos que vivieron allí antes de la llegada de los europeos. En 2010 la UNESCO declaró Ometepe reserva de la biosfera.',
 'El lago está unido al mar Caribe por el río San Juan. Por eso en sus aguas hay tiburones toro, que pueden vivir en agua dulce; el Cocibolca es uno de los pocos lagos de agua dulce con tiburones. Cerca de la ciudad de Granada hay cientos de isletas, que según los geólogos se formaron cuando una parte del volcán Mombacho se desprendió hace miles de años.',
 'Durante siglos, varias potencias soñaron con abrir un canal entre el Caribe y el Pacífico por el lago y el río San Juan. En 2013 el gobierno dio una concesión para construir un canal, y muchos campesinos protestaron porque temían perder sus tierras. El canal no se construyó.'],
 [('Why did the Spanish chroniclers call the lake "the Sweet Sea"?',['Porque parecía un mar, pero su agua era dulce.','Porque estaba en el Caribe.','Porque tenía agua salada.','Porque era muy pequeño.'],0,'The text says it looked like a sea, but its water was fresh.'),
  ('Why is Ometepe shaped like an eight?',['Porque la forman dos volcanes.','Porque tiene dos ríos.','Porque tiene dos puertos.','Porque es muy grande.'],0,'The text says two volcanoes form the island.'),
  ('How do sharks get into the lake, according to the text?',['Por el río San Juan.','Por el volcán Concepción.','Por el canal de 2013.','Por la ciudad de Granada.'],0,'The San Juan river joins the lake with the Caribbean.')])

# ---------- 02 ----------
s='b2-nicaragua-02'; T='inversion-enfasis-fronting'
lesson(s,'Rubén Darío: the poet who changed Spanish poetry',
 'Tell the life and work of Rubén Darío and put the important piece first, with fronting.',
 'emphatic fronting: Decisiva fue…, En León murió… (review)',
 ['In this lesson you read about Rubén Darío, the Nicaraguan poet. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for putting the important piece first: *Decisiva fue la influencia de Darío*.'],
 ['I can put an adjective, a place or a time first to stress it, as in *Decisiva fue…*.','I can tell where and when Darío was born, published and died.','I can name three of his books.'])
grammar(s,'Putting the Important Piece First',[
 {'type':'text','title':'What you already know','content':'You know *fronting* from B2 Unit 1: you move the piece you want to stress to the front, and the subject goes behind the verb. *Decisiva fue la influencia de Darío* stresses *decisiva*. A life story is a good place to use it, once in a paragraph: a place (*En León murió…*), a quality (*Importante fue…*).'},
 {'type':'table','title':'What can go first','rows':[
  ['Adjective + ser + subject','Decisiva fue la influencia de Darío.'],
  ['Place + verb + subject','En León murió Rubén Darío.'],
  ['De + noun + ser + subject','De gran importancia fue el libro «Azul…».'],
  ['Normal order, no stress','La influencia de Darío fue decisiva.']]},
 {'type':'examples','title':'In the life of Darío','items':[
  {'spanish':'En Metapa nació Darío, en enero de 1867.','english':'In Metapa Darío was born, in January 1867.'},
  {'spanish':'Importante fue su libro «Azul…», publicado en Chile en 1888.','english':'Important was his book Azul…, published in Chile in 1888.'},
  {'spanish':'De gran influencia fueron sus poemas en España y en América.','english':'Of great influence were his poems in Spain and in America.'},
  {'spanish':'En León murió Rubén Darío, en febrero de 1916.','english':'In León Rubén Darío died, in February 1916.'}]},
 {'type':'tip','content':'The verb agrees with the subject that comes after it: *Decisiva fue la influencia*, *Decisivos fueron los versos*. Do not put the subject first again: *Decisiva la influencia fue* sounds unnatural. Use fronting once in a paragraph.'}])
vocab(s,'Poetry and books','A poet, his books and his symbols',[
 ('el poeta','poet','noun'),('el verso','line of poetry','noun'),('el cisne','swan','noun'),('el modernismo','Modernism (a literary movement)','noun'),
 ('publicar','to publish','verb'),('el cuento','short story','noun'),('influir','to influence','verb')])
ex(s,[
 match(s+'.ex01',[['el verso','line of poetry'],['el cisne','swan'],['el modernismo','Modernism (a literary movement)'],['el cuento','short story']],U),
 mc(s+'.ex02','Which sentence puts "decisive" first: "The influence of Darío was decisive"?',
  ['Decisiva fue la influencia de Darío.','Decisivo fue la influencia de Darío.','Decisiva la influencia de Darío fue.'],teaches=T),
 fb(s+'.ex03','De gran importancia __ los poemas de Rubén Darío.','fueron','Of great importance were the poems of Rubén Darío.',T),
 sb(s+'.ex04',['En','León','murió','Rubén','Darío','en','febrero','de','1916.'],'In León Rubén Darío died, in February 1916.',T),
 dlg(s+'.ex05',[('Meg','¿Qué libro publicó Darío en Chile en 1888?'),('Carlos','_____'),('Meg','Quiero leerlo.')],
  ['Importante fue «Azul…», que publicó en Valparaíso.','Importante fue un libro que publicó en Buenos Aires en 1896.','Importante fue un libro que publicó en Madrid en 1905.'],U),
 dic(s+'.ex06','En Valparaíso publicó Darío su libro Azul en 1888.','In Valparaíso Darío published his book Azul in 1888.',T)])
story(s,'Rubén Darío, el poeta de Nicaragua','Rubén Darío, born in Nicaragua in 1867, published Azul… in Chile in 1888 and became the best-known poet of Modernism, which changed poetry in Spanish.',
 ['Rubén Darío','Modernismo','Obras'],['anteposición enfática'],[
 'Rubén Darío nació en enero de 1867 en Metapa, un pueblo de Nicaragua que hoy se llama Ciudad Darío. Creció en la ciudad de León. Según sus biógrafos, desde niño leía mucho y escribía versos. En Nicaragua trabajó como escritor de periódicos antes de viajar a otros países.',
 'En 1888, en Valparaíso, Chile, publicó el libro «Azul…», con cuentos y poemas. Importante fue el elogio del escritor español Juan Valera, que le dedicó unas cartas muy favorables. Con «Azul…» se suele empezar la historia del Modernismo, un movimiento literario que, según muchos críticos, fue el primero nacido en América Latina que influyó en la literatura de España.',
 'Los poetas modernistas cuidaban mucho la música de los versos y usaban imágenes de colores, sonidos y objetos bellos. Uno de sus símbolos preferidos era el cisne. En 1896 Darío publicó en Buenos Aires «Prosas profanas», un libro lleno de música y de imágenes elegantes.',
 'En 1905 apareció «Cantos de vida y esperanza». Este libro tiene poemas sobre la identidad de los pueblos hispanos y sobre la política de Estados Unidos en América Latina. De gran influencia fueron sus versos entre los poetas de España; según los críticos, escritores como Antonio Machado y Juan Ramón Jiménez le deben mucho.',
 'Darío vivió muchos años lejos de Nicaragua, como periodista y diplomático, en Argentina, Francia y España, entre otros países. En León murió en febrero de 1916. Hoy se le recuerda como uno de los grandes poetas en lengua española.'],
 [('Where was Azul… published, and when?',['En Valparaíso, en 1888.','En Buenos Aires, en 1896.','En León, en 1916.','En Madrid, en 1905.'],0,'The text says Azul… was published in Valparaíso in 1888.'),
  ('What does the text say about Modernist poets?',['Cuidaban la música de los versos.','Escribían solo sobre política.','Odiaban los colores.','No usaban símbolos.'],0,'The text says they took great care over the music of verses.'),
  ('Where did Darío die?',['En León.','En Chile.','En Buenos Aires.','En Metapa.'],0,'The text says he died in León in February 1916.')])

# ---------- 03 ----------
s='b2-nicaragua-03'; T='pluscuamperfecto-subjuntivo-si'
lesson(s,'Sandino: the fight against the US Marines, 1927-1934',
 'Tell the story of Augusto C. Sandino and imagine what would have happened, with si + hubiera + participle.',
 'past conditions with si + pluperfect subjunctive (review)',
 ['In this lesson you read about Augusto C. Sandino and the war in the mountains of Nicaragua between 1927 and 1933. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for talking about what did not happen: *si* + *hubiera* + participle, then *habría* + participle.'],
 ['I can say what would have happened if something had been different, with *si hubiera… habría…*.','I can tell why Sandino refused the pact of Tipitapa.','I can give the main dates of Sandino\'s story.'])
grammar(s,'If Sandino Had Accepted…',[
 {'type':'text','title':'What you already know','content':'You know *si* + *hubiera* + past participle, with *habría* + past participle, from B1 Unit 35. It describes a past that did not happen: *Si Sandino hubiera aceptado el pacto, no habría luchado en las montañas*. Both parts use *haber*: *hubiera* after *si*, *habría* in the result. Historians do this to explain why a choice mattered.'},
 {'type':'table','title':'The two parts','rows':[
  ['si + hubiera + participle','Si Sandino hubiera aceptado el pacto, …'],
  ['habría + participle','… no habría luchado en las montañas.'],
  ['si + hubieran + participle','Si los soldados no hubieran salido, …'],
  ['not *si habría*','Never: Si habría aceptado el pacto…']]},
 {'type':'examples','title':'What if?','items':[
  {'spanish':'Si Sandino hubiera aceptado el pacto de Tipitapa, no habría empezado su guerra en las montañas.','english':'If Sandino had accepted the Tipitapa pact, he would not have begun his war in the mountains.'},
  {'spanish':'Si los campesinos no hubieran ayudado a los guerrilleros, la guerra habría sido más difícil.','english':'If the peasants had not helped the guerrillas, the war would have been harder.'},
  {'spanish':'Si Sandino no hubiera ido a Managua, no lo habrían detenido esa noche.','english':'If Sandino had not gone to Managua, they would not have arrested him that night.'},
  {'spanish':'Si el gobierno de Estados Unidos hubiera decidido quedarse, la guerra habría seguido.','english':'If the United States government had decided to stay, the war would have continued.'}]},
 {'type':'tip','content':'Use this form for what did not happen: it is a way to imagine, not a way to state facts. Never put *habría* after *si*: *Si hubiera aceptado*, not *Si habría aceptado*.'}])
vocab(s,'War in the mountains','Sandino, the Marines and the Guard',[
 ('el pacto','pact, agreement','noun'),('la montaña','mountain','noun'),('el guerrillero','guerrilla fighter','noun'),('rechazar','to refuse, to reject','verb'),
 ('el soldado','soldier','noun'),('la guardia','guard, national guard','noun'),('asesinar','to murder, to assassinate','verb')])
ex(s,[
 match(s+'.ex01',[['el pacto','pact, agreement'],['el guerrillero','guerrilla fighter'],['rechazar','to refuse, to reject'],['la guardia','guard, national guard']],U),
 mc(s+'.ex02','Which sentence says "If Sandino had not gone to the mountains, he would not have begun that war"?',
  ['Si Sandino no hubiera ido a las montañas, no habría empezado esa guerra.','Si Sandino no habría ido a las montañas, no habría empezado esa guerra.','Si Sandino no fue a las montañas, no habría empezado esa guerra.'],teaches=T,ds={2:'preterito-indefinido'}),
 (lambda x:(x.pop('answer'),x.update(answers=['hubieran','hubiesen']),x)[2])(fb(s+'.ex03','Si los soldados __ encontrado a Sandino, la guerra habría terminado antes.','hubieran','If the soldiers had found Sandino, the war would have ended earlier.',T)),
 sb(s+'.ex04',['Si','Sandino','hubiera','aceptado','el','pacto,','no','habría','luchado','en','las','montañas.'],'If Sandino had accepted the pact, he would not have fought in the mountains.',T),
 dlg(s+'.ex05',[('Meg','¿Qué le pasó a Sandino en 1934?'),('Carlos','_____'),('Meg','Qué final tan triste.')],
  ['Lo asesinaron en Managua por orden de Somoza García.','Firmó el pacto de Tipitapa con los soldados de Estados Unidos.','Ganó las elecciones y fue presidente hasta 1979.'],U),
 dic(s+'.ex06','Si los campesinos no hubieran ayudado a los guerrilleros, la guerra habría sido más difícil.','If the peasants had not helped the guerrillas, the war would have been harder.',T)])
story(s,'Sandino y la guerra en las montañas','Augusto C. Sandino refused the pact of 1927 and fought the US Marines in the mountains until 1933; he was killed in 1934 on the order of Somoza García.',
 ['Sandino','Intervención de Estados Unidos','La Guardia Nacional'],['si + pluscuamperfecto de subjuntivo'],[
 'En 1927, Nicaragua vivía una guerra entre liberales y conservadores, y soldados de Estados Unidos estaban en el país. El 4 de mayo de 1927, en Tipitapa, el general liberal José María Moncada aceptó un acuerdo con el representante de Washington, Henry L. Stimson: los dos bandos entregaron las armas y Estados Unidos vigiló las próximas elecciones.',
 'Augusto C. Sandino, un trabajador de minas, rechazó el pacto. Si hubiera aceptado, no habría empezado su guerra. Salió a las montañas del norte con un pequeño grupo de mineros y campesinos y formó el Ejército Defensor de la Soberanía Nacional. Según Sandino, Nicaragua no podía aceptar soldados extranjeros en su territorio.',
 'Entre 1927 y 1933, los guerrilleros pelearon contra la Infantería de Marina de Estados Unidos. En Ocotal, en julio de 1927, los aviones estadounidenses hicieron uno de los primeros bombardeos aéreos en picada de la historia. Los campesinos de la región ayudaron a los guerrilleros con comida e información; si no la hubieran dado, la guerra habría sido más difícil.',
 'A finales de 1932 hubo elecciones, y en enero de 1933 los últimos Marines salieron del país. Sandino firmó un acuerdo de paz con el presidente Juan Bautista Sacasa y organizó una cooperativa agrícola cerca del río Coco. La Guardia Nacional, una fuerza creada con ayuda de Estados Unidos y dirigida por Anastasio Somoza García, desconfiaba de él.',
 'El 21 de febrero de 1934, después de una cena en Managua, Sandino fue detenido y asesinado por soldados de la Guardia Nacional por orden de Somoza García. Somoza se convirtió después en presidente, y su familia gobernó Nicaragua hasta 1979. El Frente Sandinista de Liberación Nacional, que derrotó a esa dinastía, tomó su nombre.'],
 [('What did Sandino do after the pact of Tipitapa?',['Salió a las montañas con un pequeño grupo.','Aceptó el pacto.','Viajó a Estados Unidos.','Fue presidente.'],0,'The text says he refused the pact and went to the mountains.'),
  ('When did the last US Marines leave Nicaragua?',['En enero de 1933.','En mayo de 1927.','En febrero de 1934.','En 1979.'],0,'The text says the last Marines left in January 1933.'),
  ('What happened to Sandino on 21 February 1934?',['Fue detenido y asesinado.','Firmó un pacto en Tipitapa.','Ganó unas elecciones.','Salió del país.'],0,'The text says he was arrested and killed.')])
