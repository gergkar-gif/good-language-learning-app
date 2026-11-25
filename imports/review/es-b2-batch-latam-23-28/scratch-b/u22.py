from lib import *
U='b2-chilecentro'; V='b2-chile-central-vocab'
def S(n): return f'{U}-{n}'
# ---------- 01 fronting
s=S('01')
vocab(s,[('la cordillera','mountain range','noun'),('el valle','valley','noun'),('el viñedo','vineyard','noun'),('el esmog','smog','noun'),('la uva','grape','noun')],'The Central Valley')
grammar(s,'Emphasis First: Describing the Central Valley',[
 {'type':'text','title':'What you already know','content':"You know fronting with *Crucial fue…* and *En aquella ciudad comenzó…* from B2 Unit 1: you move the piece you want to stress to the front, and the subject goes behind the verb. *De gran importancia son los viñedos* puts the quality first. A place or time phrase can go first too: *Entre las dos cordilleras se extiende el valle*. It works like a climax, so use it once in a paragraph. Here you use it to describe the Central Valley of Chile."},
 {'type':'table','title':'What can go first','rows':[
  ['De gran importancia son los viñedos del valle.','*De* + noun first: the vineyards of the valley are of great importance.'],
  ['Entre dos cordilleras se extiende el Valle Central.','Place first: between two mountain ranges lies the Central Valley.'],
  ['En invierno aumenta la contaminación en Santiago.','Time first: in winter the pollution in Santiago increases.'],
  ['Muy importantes son los ríos que bajan de los Andes.','Adjective first: the rivers that come down from the Andes are very important. (the verb agrees with *los ríos*)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Al este de Santiago se levantan los Andes.','english':'To the east of Santiago the Andes rise.'},
  {'spanish':'De gran importancia son los viñedos del Valle Central.','english':'The vineyards of the Central Valley are of great importance.'},
  {'spanish':'En verano llueve muy poco en el centro de Chile.','english':'In summer it rains very little in central Chile.'}]},
 {'type':'tip','content':"The verb agrees with the subject, which now stands after it: *Importantes son los ríos*, not *Importantes es los ríos*. Keep the subject behind the verb: *Importantes los ríos son* sounds unnatural."}])
lesson(s,'The Central Valley: between the Andes and the Coastal Range','Describe the Central Valley of Chile, its climate and Santiago, putting the important idea first.','emphatic fronting and word order inversion',
 ['I can put a place, a time or a quality first to stress it when I describe the Central Valley.','I can say where most Chileans live and what the climate is like.','I can name the main words for the mountains, the valley and the vineyards in Spanish.'])
ex(s,[
 match(s,1,[['la cordillera','mountain range'],['el valle','valley'],['el viñedo','vineyard'],['el esmog','smog'],['la uva','grape']],V),
 fill(s,2,'De gran importancia __ los viñedos del Valle Central para el país.','son','The vineyards of the Central Valley are of great importance for the country.','inversion-enfasis-fronting'),
 mc(s,3,'Which sentence puts the quality first: "The vineyards of the valley are of great importance"?',['De gran importancia son los viñedos del valle.','De gran importancia es los viñedos del valle.','De gran importancia los viñedos del valle son.','En gran importancia son los viñedos del valle.'],'inversion-enfasis-fronting'),
 build(s,4,'Entre dos cordilleras se extiende el Valle Central de Chile.','Between two mountain ranges lies the Central Valley of Chile.','inversion-enfasis-fronting'),
 dlg(s,5,[('Meg','¿Qué hay entre las dos cordilleras?'),('Carlos','Entre ellas _____ el Valle Central, donde vive la mayor parte de los chilenos.')],['se extiende','se extienden','extiende'],'inversion-enfasis-fronting'),
 dict_(s,6,'En invierno aumenta la contaminación en Santiago.','In winter the pollution in Santiago increases.','inversion-enfasis-fronting')])
story(s,'El Valle Central de Chile','The Central Valley lies between the Andes and the Coastal Range; it has a Mediterranean climate, vineyards and fruit, and holds Santiago, where winter smog is a problem.',[
 "Chile es un país largo y angosto entre la cordillera de los Andes y el océano Pacífico. En el centro, entre los Andes y la cordillera de la Costa, se extiende el Valle Central, la zona donde vive la mayor parte de la población del país.",
 "El clima es de tipo mediterráneo: los veranos son secos y calurosos, y la lluvia cae sobre todo en invierno. Los ríos que bajan de los Andes, alimentados por la nieve, permiten regar los campos.",
 "En el valle se cultivan uvas, frutas y verduras. De gran importancia son los viñedos: el vino chileno se vende en muchos países, y valles como el del Maipo y el de Colchagua son conocidos por su vino.",
 "Santiago, fundada en 1541 por Pedro de Valdivia, está en este valle y tiene unos siete millones de habitantes en su área metropolitana. Como está rodeada de montañas, en invierno el aire contaminado se queda sobre la ciudad. Para reducir la contaminación, la ciudad ha incorporado buses eléctricos; según se informa, su flota es una de las más grandes del mundo fuera de China.",
 "Chile está en una zona de terremotos, y por eso los edificios se construyen con normas especiales. En los días claros de invierno, desde Santiago se ven los Andes con nieve."],
 [("Where does most of the population of Chile live?",["En el Valle Central.","En el desierto del norte.","En las islas del sur."],"The first paragraph."),
  ("When does most of the rain fall in central Chile?",["En invierno.","En verano.","En primavera."],"The second paragraph."),
  ("Why does polluted air stay over Santiago in winter?",["Porque la ciudad está rodeada de montañas.","Porque la ciudad está en la costa.","Porque no hay buses eléctricos."],"The fourth paragraph.")])
# ---------- 02 relativas con preposición
s=S('02')
vocab(s,[('el funicular','funicular, cable railway','noun'),('el cerro','hill','noun'),('porteño','of the port; person from Valparaíso','adjective'),('el mural','mural','noun'),('la escalera','staircase','noun')],'Valparaíso')
grammar(s,'The City on the Hills: Relative Clauses with a Preposition',[
 {'type':'text','title':'What you already know','content':"You know relative clauses with *que* from B1 Unit 5, and with a preposition + *el que* from B1 Unit 20: *el edificio en el que vivimos*. The article matches the noun you are describing (*el, la, los, las*) and the preposition stays in front. A city built on hills like Valparaíso is full of places, ways and years that you can describe this way."},
 {'type':'table','title':'Preposition + article + que','rows':[
  ['Valparaíso es una ciudad en la que hay muchos cerros.','Valparaíso is a city in which there are many hills. (*la ciudad*: *en la que*)'],
  ['Los ascensores son el medio con el que los porteños suben a los cerros.','The funiculars are the means with which the people of Valparaíso go up the hills. (*el medio*: *con el que*)'],
  ['La casa en la que Neruda pasó temporadas se llama La Sebastiana.','The house in which Neruda spent time is called La Sebastiana.'],
  ['Las escaleras por las que se sube a los cerros son muy empinadas.','The stairs by which you go up the hills are very steep. (*las escaleras*: *por las que*)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'El año en el que la UNESCO declaró el casco histórico fue 2003.','english':'The year in which UNESCO declared the historic quarter was 2003.'},
  {'spanish':'El puerto por el que llegaban los barcos está al pie de los cerros.','english':'The port through which the ships arrived is at the foot of the hills.'},
  {'spanish':'Los murales son las obras de arte de las que más se habla en la ciudad.','english':'The murals are the works of art that people talk about most in the city.'}]},
 {'type':'tip','content':"Match the article to the noun before it, and keep the preposition the verb needs: *la ciudad de la que hablamos* (*hablar de*). Without the preposition the sentence is wrong: not *la ciudad que hablamos*."}])
lesson(s,'Valparaíso: a port city built on hills','Describe Valparaíso, its hills and funiculars and its World Heritage listing, using relative clauses with a preposition.','relative clauses with prepositions and el que or lo que',
 ['I can describe the places and ways of Valparaíso with *en la que*, *con el que* and other prepositions with *el que*.','I can say when the first funicular opened and when UNESCO listed the city.','I can name the main words for the hills, the funiculars and the murals in Spanish.'])
ex(s,[
 match(s,1,[['el funicular','funicular, cable railway'],['el cerro','hill'],['porteño','of the port; person from Valparaíso'],['el mural','mural'],['la escalera','staircase']],V),
 fill(s,2,'Valparaíso es una ciudad en la __ hay muchos cerros.','que','Valparaíso is a city in which there are many hills.','relativas-preposicion-el-que'),
 mc(s,3,'Which sentence says: "The funiculars are the means with which the people of Valparaíso go up the hills"?',['Los ascensores son el medio con el que los porteños suben a los cerros.','Los ascensores son el medio con la que los porteños suben a los cerros.','Los ascensores son el medio el que los porteños suben a los cerros.'],'relativas-preposicion-el-que'),
 build(s,4,'La casa en la que Neruda pasó temporadas se llama La Sebastiana.','The house in which Neruda spent time is called La Sebastiana.','relativas-preposicion-el-que'),
 dlg(s,5,[('Meg','¿Qué es La Sebastiana?'),('Carlos','Es la casa en _____ Neruda pasaba temporadas en Valparaíso.')],['la que','lo que','quien'],'relativas-preposicion-el-que'),
 dict_(s,6,'El año en el que la UNESCO declaró el casco histórico fue 2003.','The year in which UNESCO declared the historic quarter was 2003.','relativas-preposicion-el-que')])
story(s,'Valparaíso, el puerto de los cerros','Valparaíso is a port city on steep hills linked by funiculars since 1883; its historic quarter was listed by UNESCO in 2003 and it is known for its murals and for Neruda\'s house.',[
 "Valparaíso es uno de los puertos más importantes de Chile y está a unas dos horas de Santiago. La ciudad se extiende por muchos cerros que rodean la bahía, como un anfiteatro frente al mar. Sus habitantes se llaman porteños.",
 "En el siglo XIX, el puerto recibía barcos de muchos países, en especial los que viajaban entre el Atlántico y el Pacífico por el sur del continente. Según muchos historiadores, la apertura del canal de Panamá en 1914 redujo ese tráfico, y el puerto perdió parte de su importancia.",
 "Como los cerros son muy empinados, la ciudad tiene escaleras y ascensores, que son pequeños funiculares. El primero, el ascensor Concepción, se abrió en 1883. Varios siguen funcionando hoy y son el medio con el que muchos porteños suben a su casa.",
 "En 2003, la UNESCO declaró Patrimonio de la Humanidad el casco histórico de Valparaíso. Las casas de colores, los murales y las calles estrechas son parte de su paisaje. En la ciudad está La Sebastiana, la casa en la que el poeta Pablo Neruda pasó temporadas y que hoy es un museo.",
 "La ciudad también ha sufrido desastres. En 1906 un terremoto destruyó gran parte de ella, y en 2014 un incendio muy grande afectó a varios cerros. Después de cada desastre, los porteños reconstruyeron sus casas."],
 [("What is an ascensor in Valparaíso?",["Un pequeño funicular que sube a los cerros.","Un tipo de mural.","Una casa de Neruda."],"The third paragraph."),
  ("When did UNESCO declare the historic quarter of Valparaíso a World Heritage Site?",["En 2003.","En 1883.","En 1914."],"The fourth paragraph."),
  ("What happened in Valparaíso in 1906?",["Un terremoto destruyó gran parte de la ciudad.","Se abrió el canal de Panamá.","Se declaró Patrimonio de la Humanidad."],"The fifth paragraph.")])
# ---------- 03 stance adverbs
s=S('03')
vocab(s,[('el poeta','poet','noun'),('la poesía','poetry','noun'),('el premio','prize','noun'),('el poema','poem','noun'),('la casa museo','house that is now a museum','noun')],'Gabriela Mistral and Pablo Neruda')
grammar(s,'Showing Your Attitude: Two Chilean Nobel Poets',[
 {'type':'text','title':'What you already know','content':"You know *lamentablemente*, *afortunadamente*, *indudablemente*, *en realidad*, *en rigor* and *precisamente* from B2 Unit 1. They stand outside the action and comment on the whole sentence: how sure, how glad or how exact you are. They are useful when you talk about writers, because you often correct a fact or show a feeling. Here they are used for Gabriela Mistral and Pablo Neruda."},
 {'type':'table','title':'Stance adverbs in action','rows':[
  ['En realidad, Gabriela Mistral se llamaba Lucila Godoy Alcayaga.','In fact, Gabriela Mistral was called Lucila Godoy Alcayaga. (you correct what someone may assume)'],
  ['En rigor, Neruda no nació en Isla Negra, sino en Parral.','Strictly speaking, Neruda was not born in Isla Negra but in Parral. (the exact truth)'],
  ['Lamentablemente, Mistral vivió muchos años lejos de Chile.','Unfortunately, Mistral lived many years far from Chile. (your feeling)'],
  ['Precisamente en 1971 Neruda recibió el Nobel.','Precisely in 1971 Neruda received the Nobel Prize. (it points at the year)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Indudablemente, los dos poetas son muy leídos en Chile.','english':'Undoubtedly, both poets are widely read in Chile.'},
  {'spanish':'Mistral, lamentablemente, murió lejos de su país.','english':'Mistral, unfortunately, died far from her country.'},
  {'spanish':'Neruda, en realidad, tenía tres casas en Chile.','english':'Neruda, in fact, had three houses in Chile.'}]},
 {'type':'tip','content':"Use the comma test: if you can put commas around the adverb, it comments on the whole sentence. *Precisamente* takes no commas because it points at the word after it. Use one stance adverb per sentence."}])
lesson(s,'Gabriela Mistral and Pablo Neruda: two Chilean Nobel poets','Talk about the two Chilean Nobel poets, Gabriela Mistral and Pablo Neruda, showing your attitude with stance adverbs.','focus and stance adverbs like precisamente and francamente',
 ['I can show my attitude to a fact about the poets with stance adverbs such as *en realidad*, *en rigor* and *lamentablemente*.','I can say when and where each poet was born and when each received the Nobel Prize.','I can name the main words for poet, poem, prize and poetry in Spanish.'])
ex(s,[
 match(s,1,[['el poeta','poet'],['la poesía','poetry'],['el premio','prize'],['el poema','poem'],['la casa museo','house that is now a museum']],V),
 fill(s,2,'En __, Neruda no nació en Isla Negra, sino en Parral.','rigor','Strictly speaking, Neruda was not born in Isla Negra but in Parral.','stance-adverbs'),
 mc(s,3,'Which sentence says: "Strictly speaking, Neruda was not born in Isla Negra but in Parral"?',['En rigor, Neruda no nació en Isla Negra, sino en Parral.','Apenas, Neruda no nació en Isla Negra, sino en Parral.','Lamentablemente, Neruda no nació en Isla Negra, sino en Parral.'],'stance-adverbs'),
 build(s,4,'En realidad, Gabriela Mistral se llamaba Lucila Godoy Alcayaga.','In fact, Gabriela Mistral was called Lucila Godoy Alcayaga.','stance-adverbs'),
 dlg(s,5,[('Meg','¿Neruda nació en Isla Negra?'),('Carlos','_____, nació en Parral, pero tenía una casa en Isla Negra.')],['En realidad','Apenas','Precisamente'],'stance-adverbs'),
 dict_(s,6,'Lamentablemente, Gabriela Mistral vivió muchos años lejos de Chile.','Unfortunately, Gabriela Mistral lived many years far from Chile.','stance-adverbs')])
story(s,'Gabriela Mistral y Pablo Neruda','Chile has two Nobel Prize winners in literature: Gabriela Mistral (1945), the first Latin American to win it, and Pablo Neruda (1971); both are widely read today.',[
 "Chile tiene dos premios Nobel de Literatura: Gabriela Mistral, que lo recibió en 1945, y Pablo Neruda, que lo recibió en 1971. Mistral fue la primera persona de América Latina que ganó ese premio.",
 "Gabriela Mistral nació en 1889 en Vicuña, en el valle del Elqui. En realidad, su nombre era Lucila Godoy Alcayaga. Trabajó como maestra desde muy joven y escribió sobre los niños, el dolor y la naturaleza. Entre sus libros están Desolación, Ternura y Tala. Vivió muchos años fuera de Chile y murió en Nueva York en 1957.",
 "Pablo Neruda nació en 1904 en Parral; su nombre verdadero era Ricardo Eliécer Neftalí Reyes Basoalto. A los veinte años publicó Veinte poemas de amor y una canción desesperada. Más tarde escribió sobre el mar, la política y las cosas de todos los días, por ejemplo en las Odas elementales. También fue diplomático y político.",
 "Neruda tuvo tres casas en Chile: La Chascona, en Santiago, La Sebastiana, en Valparaíso, y una casa en Isla Negra, junto al mar. Hoy las tres están abiertas al público como casas museo. Neruda murió en septiembre de 1973, pocos días después del golpe de Estado.",
 "Los poemas de los dos autores se leen en las escuelas de Chile y se han traducido a muchos idiomas. Sus libros se siguen publicando y estudiando hoy."],
 [("Who was the first Latin American to win the Nobel Prize in Literature?",["Gabriela Mistral.","Pablo Neruda.","Víctor Jara."],"The first paragraph."),
  ("Where was Pablo Neruda born?",["En Parral.","En Vicuña.","En Isla Negra."],"The third paragraph."),
  ("What are the three houses of Neruda today?",["Casas museo abiertas al público.","Escuelas de Valparaíso.","Casas de Gabriela Mistral."],"The fourth paragraph.")])
# ---------- 04 antes/despues de que
s=S('04')
vocab(s,[('el golpe de Estado','coup d\'état','noun'),('la dictadura','dictatorship','noun'),('el desaparecido','person who disappeared (a victim of forced disappearance)','noun'),('la memoria','memory','noun'),('el informe','report','noun'),('bombardear','to bomb','verb')],'11 September 1973')
grammar(s,'Before and After: 11 September 1973',[
 {'type':'text','title':'What you already know','content':"You know *antes de que* and *después de que* from B2 Unit 7. *Antes de que* always takes the subjunctive: after a past verb, the imperfect subjunctive (*antes de que llegaran*). *Después de que* takes the indicative for something that happened (*después de que llegaron*) and the subjunctive for something still to come. The two are ideal for putting the events of a single day in order."},
 {'type':'table','title':'Ordering the events of the day','rows':[
  ['Allende habló por radio antes de que los aviones bombardearan el palacio.','Allende spoke on the radio before the planes bombed the palace. (*antes de que* + imperfect subjunctive)'],
  ['Después de que los aviones bombardearon el palacio, los soldados entraron.','After the planes bombed the palace, the soldiers went in. (*después de que* + indicative: it happened)'],
  ['Antes de que terminara la dictadura, muchas familias buscaban a sus desaparecidos.','Before the dictatorship ended, many families were looking for their disappeared. (*antes de que* + subjunctive)'],
  ['Después de que terminó la dictadura, se publicaron informes sobre las víctimas.','After the dictatorship ended, reports about the victims were published. (indicative)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Antes de que llegara la noche, el centro de Santiago estaba vacío.','english':'Before night came, the centre of Santiago was empty.'},
  {'spanish':'Después de que terminó el golpe, empezó la dictadura.','english':'After the coup ended, the dictatorship began.'},
  {'spanish':'Hablamos del museo antes de que lo visitáramos.','english':'We talked about the museum before we visited it.'}]},
 {'type':'tip','content':"Two questions decide the verb. After *antes de que*: always the subjunctive, so *antes de que llegara*, never *antes de que llegó*. After *después de que*: has it happened? Yes: indicative (*después de que llegó*). Not yet: subjunctive."}])
lesson(s,'11 September 1973: the coup, the dictatorship and memory','Tell the events of 11 September 1973 and how they are remembered, ordering them with antes de que and después de que.','clauses with antes de que and después de que',
 ['I can put events in order with *antes de que* + subjunctive and *después de que* + indicative.','I can tell what happened on 11 September 1973, attributing figures to the reports.','I can name the main words for the coup, the dictatorship and memory in Spanish.'])
ex(s,[
 match(s,1,[['el golpe de Estado',"coup d'état"],['la dictadura','dictatorship'],['el desaparecido','person who disappeared (a victim of forced disappearance)'],['la memoria','memory'],['el informe','report'],['bombardear','to bomb']],V),
 fill(s,2,'Allende habló por radio antes de que el palacio __ bombardeado.','fuera','Allende spoke on the radio before the palace was bombed.','antes-despues-de-que',answers=['fuera','fuese']),
 mc(s,3,'Which sentence says: "Allende spoke on the radio before the planes bombed the palace"?',['Allende habló por radio antes de que los aviones bombardearan el palacio.','Allende habló por radio antes de que los aviones bombardearon el palacio.','Allende habló por radio antes de que los aviones bombardeen el palacio.'],'antes-despues-de-que',ds={2:'subjuntivo-morfologia'}),
 build(s,4,'Después de que los aviones bombardearon el palacio, los soldados entraron.','After the planes bombed the palace, the soldiers went in.','antes-despues-de-que'),
 dlg(s,5,[('Meg','¿Cuándo habló Allende por radio?'),('Carlos','Habló antes de que _____ el ataque contra el palacio.')],['empezara','empezó','empezaba'],'antes-despues-de-que',ds={1:'preterito-indefinido',2:'imperfect'}),
 dict_(s,6,'Antes de que terminara la dictadura, muchas familias buscaban a sus familiares desaparecidos.','Before the dictatorship ended, many families were looking for their disappeared relatives.','antes-despues-de-que')])
story(s,'El 11 de septiembre de 1973','On 11 September 1973 the armed forces overthrew President Salvador Allende, starting a dictatorship under Augusto Pinochet that lasted until 1990; the Rettig and Valech reports record the victims, and the years are remembered in different ways.',[
 "El 11 de septiembre de 1973, las Fuerzas Armadas y Carabineros derrocaron al presidente Salvador Allende, que había sido elegido en 1970. Ese día, antes de que los aviones bombardearan el palacio de La Moneda, Allende habló por radio a los chilenos: dijo que no iba a renunciar y se despidió de ellos.",
 "Poco antes del mediodía, aviones de la Fuerza Aérea bombardearon La Moneda. Después de que los soldados entraron en el palacio, Allende ya estaba muerto. Según la investigación judicial de 2011, se quitó la vida.",
 "Después del golpe, se instaló una dictadura militar encabezada por el general Augusto Pinochet, que duró hasta marzo de 1990. Miles de personas fueron detenidas, muchas de ellas en estadios como el Estadio Nacional. Entre ellas estaba el cantante Víctor Jara, que murió ese mismo mes. Según el Informe Rettig, más de dos mil personas murieron o desaparecieron por razones políticas. Según el Informe Valech, de 2004, más de veinte mil personas sufrieron prisión política y tortura; informes posteriores ampliaron esa cifra.",
 "Después de que terminó la dictadura, Chile empezó a buscar la verdad sobre esos años. En 2010 se abrió en Santiago el Museo de la Memoria y los Derechos Humanos. Lugares como Villa Grimaldi y Londres 38, que fueron centros de detención, son hoy espacios de memoria.",
 "Todavía hoy, las opiniones sobre esos años son distintas: algunas personas defendieron el gobierno militar y otras lo condenan. Cada 11 de septiembre hay ceremonias y actos en recuerdo de las víctimas."],
 [("What did Allende do before the planes bombed La Moneda?",["Habló por radio a los chilenos.","Salió del país.","Firmó un tratado de paz."],"The first paragraph."),
  ("According to the Rettig Report, how many people died or disappeared for political reasons?",["Más de dos mil.","Más de veinte mil.","Menos de cien."],"The third paragraph."),
  ("What opened in Santiago in 2010?",["El Museo de la Memoria y los Derechos Humanos.","El Estadio Nacional.","La Moneda."],"The fourth paragraph.")])
# ---------- 05 si bien
s=S('05')
vocab(s,[('el plebiscito','plebiscite, national vote','noun'),('el estallido','outburst, sudden outbreak','noun'),('la protesta','protest','noun'),('el voto','vote','noun'),('rechazar','to reject','verb')],'The transition and the constitutional votes')
grammar(s,'Si Bien: Granting a Point in Chile\'s Recent History',[
 {'type':'text','title':'What you already know','content':"You know *si bien* from B2 Unit 8: it means \"although it is true that\", takes the indicative and belongs to formal writing, such as reports and news. First you grant a true point, then you say what matters more. Recent Chilean history is full of such pairs: a vote that was won but did not change everything at once, or a text that was rejected while the process went on."},
 {'type':'table','title':'Si bien and what matters more','rows':[
  ['Si bien el plebiscito de 1988 lo ganó el No, Pinochet siguió en el cargo hasta 1990.','Although the No won the 1988 plebiscite, Pinochet stayed in office until 1990.'],
  ['Si bien el estallido empezó por el metro, las protestas pedían más cambios.','Although the outburst began over the metro, the protests asked for more changes.'],
  ['Si bien los chilenos votaron por una nueva constitución en 2020, rechazaron el primer texto en 2022.','Although Chileans voted for a new constitution in 2020, they rejected the first draft in 2022.'],
  ['La transición, si bien fue pacífica, dejó temas pendientes.','The transition, although peaceful, left open issues. (in the middle, between commas)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Si bien la dictadura terminó en 1990, el debate sobre ese pasado continúa.','english':'Although the dictatorship ended in 1990, the debate about that past continues.'},
  {'spanish':'Si bien el segundo texto también fue rechazado, el proceso constitucional terminó.','english':'Although the second draft was also rejected, the constitutional process ended.'},
  {'spanish':'Si bien muchos votaron, otros no fueron a las urnas.','english':'Although many voted, others did not go to the polls.'}]},
 {'type':'tip','content':"*Si bien* takes the indicative and no *que*: *si bien fue*, not *si bien que fue* and not *si bien fuera*. It is two words: do not confuse it with *sí* (yes) or *si* (if). In everyday speech say *aunque*."}])
lesson(s,'From the 1988 plebiscite to the constitutional votes','Tell how Chile moved from the 1988 plebiscite to the protests of 2019 and the constitutional votes, granting points with si bien.','formal concessive clauses with si bien and the indicative',
 ['I can grant a point and say what matters more with *si bien* + indicative.','I can say what happened in the votes of 1988, 2020, 2022 and 2023.','I can name the main words for the plebiscite, the protests and the vote in Spanish.'])
ex(s,[
 match(s,1,[['el plebiscito','plebiscite, national vote'],['el estallido','outburst, sudden outbreak'],['la protesta','protest'],['el voto','vote'],['rechazar','to reject']],V),
 fill(s,2,'Si __ el plebiscito de 1988 lo ganó el No, Pinochet siguió en el cargo hasta 1990.','bien','Although the No won the 1988 plebiscite, Pinochet stayed in office until 1990.','concesivas-si-bien'),
 mc(s,3,'Which sentence says: "Although the first draft was rejected in 2022, the process continued with a second draft"?',['Si bien el primer texto fue rechazado en 2022, el proceso continuó con un segundo texto.','Si bien que el primer texto fue rechazado en 2022, el proceso continuó con un segundo texto.','Si bien el primer texto fuera rechazado en 2022, el proceso continuó con un segundo texto.'],'concesivas-si-bien',ds={2:'imperfect-subjunctive-forms'}),
 build(s,4,'Si bien el estallido empezó por el metro, las protestas pedían más cambios.','Although the outburst began over the metro, the protests asked for more changes.','concesivas-si-bien'),
 dlg(s,5,[('Meg','¿Qué pasó con el primer texto de la nueva constitución?'),('Carlos','Si bien votaron por una nueva constitución en 2020, _____ el primer texto en 2022.')],['rechazaron','rechacen','rechazarían'],'concesivas-si-bien',ds={1:'subjuntivo-morfologia',2:'condicional-regular'}),
 dict_(s,6,'Si bien la dictadura terminó en 1990, el debate sobre ese pasado continúa.','Although the dictatorship ended in 1990, the debate about that past continues.','concesivas-si-bien')])
story(s,'De la transición a las votaciones constitucionales','From the 1988 plebiscite through the protests of October 2019 to the constitutional votes of 2020, 2022 and 2023, ending with José Antonio Kast as president since March 2026.',[
 "El 5 de octubre de 1988, los chilenos votaron en un plebiscito si el general Augusto Pinochet seguía en el poder ocho años más. Ganó la opción No, con alrededor del 56 % de los votos. Una canción de la campaña, «Chile, la alegría ya viene», se hizo muy conocida. Si bien el No ganó, Pinochet siguió como presidente hasta marzo de 1990, cuando asumió Patricio Aylwin.",
 "Entre 1990 y 2010 gobernaron los presidentes de la Concertación, y la economía creció. Los defensores del modelo económico recuerdan que la pobreza bajó mucho en esas décadas. Sus críticos dicen que la privatización de servicios como la educación y las pensiones aumentó la desigualdad.",
 "El 18 de octubre de 2019, estudiantes protestaron en el metro de Santiago contra el aumento del precio del pasaje, y las protestas se extendieron por todo el país. Una consigna decía que no eran treinta pesos, sino treinta años. Según las autoridades, el 25 de octubre más de un millón doscientas mil personas marcharon en Santiago. Organismos de derechos humanos denunciaron lesiones graves, entre ellas muchas lesiones oculares.",
 "El 15 de noviembre de 2019, los partidos políticos firmaron un acuerdo para votar sobre una nueva constitución. En octubre de 2020, alrededor del 78 % de los votantes aprobó escribir una. Si bien esa votación fue muy clara, en septiembre de 2022 los chilenos rechazaron el primer texto, con alrededor del 62 %, y en diciembre de 2023 rechazaron también el segundo, con alrededor del 56 %. La Constitución de 1980, con varias reformas, sigue en vigor.",
 "Desde el 11 de marzo de 2026, el presidente de Chile es José Antonio Kast."],
 [("What was voted on in the plebiscite of 5 October 1988?",["Si Pinochet seguía en el poder ocho años más.","Si Chile entraba en una guerra.","Si Santiago cambiaba de nombre."],"The first paragraph."),
  ("What happened on 15 November 2019?",["Los partidos firmaron un acuerdo para votar sobre una nueva constitución.","Se abrió el metro de Santiago.","Terminó la dictadura."],"The fourth paragraph."),
  ("What did the voters decide in December 2023?",["Rechazaron el segundo texto.","Aprobaron el segundo texto.","Eligieron a Aylwin."],"The fourth paragraph.")])
# ---------- consolidation
s=S('consolidation')
lesson(s,'Central Chile: unit review','Review the Central Valley, Valparaíso, Mistral and Neruda, 11 September 1973 and the recent votes, with the grammar you used to talk about them.','review: fronting, relative clauses with a preposition, stance adverbs, antes de que and después de que, si bien',
 ['I can review what I learned about central Chile, from the Central Valley to the constitutional votes.','I can use fronting, relative clauses with a preposition, stance adverbs, *antes de que* and *si bien*.','I can say what happened in the votes of 1988, 2020, 2022 and 2023.'],
 ['I can put a place, a time or a quality first to stress it when I describe the Central Valley.','I can describe the places and ways of Valparaíso with *en la que*, *con el que* and other prepositions with *el que*.','I can show my attitude to a fact about the poets with stance adverbs such as *en realidad*, *en rigor* and *lamentablemente*.','I can put events in order with *antes de que* + subjunctive and *después de que* + indicative.','I can grant a point and say what matters more with *si bien* + indicative.'])
items=[
 match(s,1,[['la cordillera','mountain range'],['el funicular','funicular, cable railway'],['el golpe de Estado',"coup d'état"],['el plebiscito','plebiscite, national vote']],V),
 fill(s,2,'Entre los Andes y la cordillera de la Costa se __ el Valle Central.','extiende','The Central Valley lies between the Andes and the Coastal Range.','inversion-enfasis-fronting'),
 mc(s,3,'Which sentence says: "Valparaíso is the city in which La Sebastiana, Neruda\'s house, stands"?',['Valparaíso es la ciudad en la que está La Sebastiana, la casa de Neruda.','Valparaíso es la ciudad en el que está La Sebastiana, la casa de Neruda.','Valparaíso es la ciudad la que está La Sebastiana, la casa de Neruda.'],'relativas-preposicion-el-que'),
 mc(s,4,'Which sentence says: "Neruda received the Nobel Prize precisely in 1971"?',['Neruda recibió el Nobel precisamente en 1971.','Neruda recibió el Nobel indudablemente en 1971.','Neruda recibió el Nobel lamentablemente en 1971.'],'stance-adverbs'),
 fill(s,5,'Allende habló por radio antes de que los soldados __ en el palacio.','entraran','Allende spoke on the radio before the soldiers entered the palace.','antes-despues-de-que',answers=['entraran','entrasen']),
 build(s,6,'Si bien el primer texto fue rechazado, el proceso continuó con un segundo texto.','Although the first draft was rejected, the process continued with a second draft.','concesivas-si-bien'),
 dict_(s,7,'Valparaíso es una ciudad en la que hay muchas escaleras.','Valparaíso is a city in which there are many staircases.','relativas-preposicion-el-que'),
 mc(s,8,'According to the texts of this unit, what did Chilean voters decide in October 2020?',['Aprobaron escribir una nueva constitución.','Rechazaron el primer texto constitucional.','Eligieron a José Antonio Kast presidente.','Terminaron con la dictadura militar.'],None,cat='reading')]
for it in items: it['id']=it['id'].replace('consolidation.','con.')
ex(s,items)
