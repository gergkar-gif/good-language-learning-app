import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-venezuela-oil-caracas-vocab'
P='b2-venezuelapetroleo'
L={}

L['01']=dict(
 title='Caracas and El Ávila: a city in a valley below a mountain',
 goal="Describe Caracas and El Ávila, putting the place or the quality first for emphasis.",
 grammar_label='emphatic fronting and inversion',
 goal_items=["I can put a place or a quality first for emphasis, as in *En un valle estrecho fue fundada Caracas*.",
  "I can say where Caracas was founded and what separates it from the sea.",
  "I can use the new words for valley, mountain range and peak."],
 screen=screen('x','Emphasis First: Caracas and El Ávila',
  "You know *Crucial fue la intervención* and fronting from B2 Unit 1: you move a quality or a place to the front of the sentence, and the subject goes behind the verb (*Crucial fue la intervención del mediador*). It works like \"Narrow is the valley\" in formal English. A city in a narrow valley below a mountain gives plenty of chances to use it.",
  'Normal order and fronted order',
  [("La vista de El Ávila es impresionante.","Impresionante es la vista de El Ávila. (quality first)"),
   ("Caracas fue fundada en un valle estrecho en 1567.","En un valle estrecho fue fundada Caracas en 1567. (place first)"),
   ("El Ávila se levanta entre la ciudad y el mar.","Entre la ciudad y el mar se levanta El Ávila. (place first)"),
   ("Humboldt subió a la Silla de Caracas en 1800.","En 1800 subió Humboldt a la Silla de Caracas. (time first)")],
  [("Estrecho es el valle donde está Caracas.","The valley where Caracas lies is narrow."),
   ("En un valle estrecho fue fundada Caracas en 1567.","Caracas was founded in 1567 in a narrow valley."),
   ("Entre la ciudad y el mar se levanta El Ávila.","El Ávila rises between the city and the sea."),
   ("En 1800 subió Humboldt a la Silla de Caracas.","In 1800 Humboldt climbed the Silla de Caracas.")],
  "The verb and the participle agree with the subject that comes after them: *fue fundada Caracas*, *fueron fundadas las ciudades*. Use fronting once in a paragraph, at the moment you want to stress something; if every sentence starts with its adjective, the text sounds heavy."),
 vocab_title='Caracas and El Ávila: valley, range and peak',
 vocab_theme='The valley of Caracas and the mountain El Ávila',
 vocab=[('valle','valley','noun'),('cordillera','mountain range','noun'),('pico','peak','noun'),('ladera','slope, hillside','noun'),('caraqueño','person from Caracas','noun')],
 exercises=[
  match('E.ex01',[('el valle','valley'),('la cordillera','mountain range'),('el pico','peak'),('la ladera','slope, hillside')],V),
  fb('E.ex02','Impresionantes __ las vistas desde la Silla de Caracas.','son','The views from the Silla de Caracas are impressive.','inversion-enfasis-fronting'),
  mc('E.ex03','Which sentence means "In a narrow valley Caracas was founded", with the place stressed?',['En un valle estrecho fue fundada Caracas.','En un valle estrecho fue fundado Caracas.','En un valle estrecho fueron fundada Caracas.'],'inversion-enfasis-fronting'),
  sb('E.ex04','Estrecho es el valle donde viven los caraqueños.','The valley where the people of Caracas live is narrow.','inversion-enfasis-fronting'),
  dlg('E.ex05',[('Meg','¿Qué es la cordillera de la Costa?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es el grupo de montañas que está entre Caracas y el mar.','Es el río más largo que pasa por el centro de Caracas.','Es un barrio nuevo que está al norte del lago.'],V),
  dic('E.ex06','En un valle estrecho fue fundada Caracas en 1567.','Caracas was founded in 1567 in a narrow valley.','inversion-enfasis-fronting'),
  reading('E.ex07','Who climbed the Silla de Caracas in 1800, according to the text?',['Alexander von Humboldt, durante su viaje por América.','Diego de Losada, que fundó la ciudad.','Carlos Raúl Villanueva, que hizo la universidad.']),
 ],
 story=dict(title='Caracas y El Ávila',
  summary='Caracas lies in a narrow valley between the Cordillera de la Costa and the sea, below El Ávila, a national park since 1958, and it has grown up the hillsides since oil arrived.',
  paras=[
  "Caracas fue fundada en 1567 por el capitán español Diego de Losada, con el nombre de Santiago de León de Caracas. Está en un valle estrecho de la cordillera de la Costa, a poca distancia del mar Caribe. Entre la ciudad y el mar se levanta El Ávila, una montaña que los caraqueños ven desde casi cualquier barrio.",
  "El Ávila es parque nacional desde 1958. También se le llama con su nombre indígena, Waraira Repano. Su pico más alto, el Naiguatá, tiene más de dos mil setecientos metros. Muchos caraqueños caminan por sus senderos los fines de semana.",
  "En 1800 el naturalista alemán Alexander von Humboldt subió a la Silla de Caracas, una de las cumbres de El Ávila, durante su viaje por América. Humboldt escribió después sobre el paisaje de la ciudad y de la montaña.",
  "El valle ha cambiado mucho. En el siglo XX, con el dinero del petróleo, la ciudad creció muy rápido y las casas subieron por las laderas de las montañas. Hoy viven en la zona de Caracas millones de personas.",
  "La montaña también ha sido peligrosa. En diciembre de 1999 unas lluvias muy fuertes provocaron deslizamientos de tierra en el estado Vargas, al otro lado de El Ávila, y causaron una de las mayores catástrofes naturales de la historia del país."],
  qs=[("When was Caracas founded, and by whom?",["Fue fundada en 1567 por Diego de Losada.","Fue fundada en 1958 por Humboldt.","Fue fundada en 1800 por el gobierno."],"The first paragraph gives both."),
      ("What happened in 1958, according to the text?",["El Ávila se convirtió en parque nacional.","Humboldt subió a la Silla de Caracas.","Se fundó la ciudad de Caracas."],"The second paragraph says so."),
      ("Why did houses climb the hillsides in the twentieth century?",["Porque la ciudad creció muy rápido con el dinero del petróleo.","Porque el gobierno prohibió construir en el valle.","Porque la montaña se hizo más baja."],"The fourth paragraph explains it.")]))

L['02']=dict(
 title='Zumaque I and Barroso II: the first oil wells',
 goal="Tell what happened before and after the first oil wells, using antes de que and después de que.",
 grammar_label='antes de que and después de que',
 goal_items=["I can say what was true before something happened with *antes de que* and the subjunctive.",
  "I can tell when the first oil wells were opened in Zulia and what changed afterwards.",
  "I can use the new words for well, barrel and concession."],
 screen=screen('x','Before and After: The First Oil Wells',
  "You know *antes de que* and *después de que* from B2 Unit 7: *antes de que* is always followed by the subjunctive, and *después de que* takes the indicative for what happened and the subjunctive for what is still to come. The first oil wells divide the history of Venezuela into a before and an after, so the two connectors fit the topic.",
  'Before and after',
  [("Antes de que se descubriera el petróleo, Venezuela vivía del café y del cacao.","*antes de que* + imperfect subjunctive after a past verb"),
   ("Después de que se abrió el pozo, llegaron muchas empresas.","*después de que* + indicative: it happened"),
   ("Antes de que llegue la lluvia, cerramos las válvulas.","*antes de que* + present subjunctive: it has not happened yet"),
   ("Después de que termine la visita, hablaremos del petróleo.","*después de que* + subjunctive: still to come")],
  [("Antes de que se descubriera el petróleo, Venezuela vivía del café y del cacao.","Before oil was discovered, Venezuela lived from coffee and cacao."),
   ("Después de que se abrió el pozo, llegaron muchas empresas.","After the well was opened, many companies arrived."),
   ("Antes de que llegara la empresa, el pueblo era tranquilo.","Before the company arrived, the village was quiet."),
   ("Hablaremos después de que termine la visita.","We will talk after the visit ends.")],
  "Two questions decide everything. After *antes de que* the verb is always in the subjunctive: *antes de que llegara*, never *antes de que llegó*. After *después de que* ask whether it has happened: yes means indicative, not yet means subjunctive. If the same person does both actions, use the infinitive: *antes de salir*."),
 vocab_title='The first oil wells: well, barrel and concession',
 vocab_theme='Early oil industry in Zulia',
 vocab=[('pozo','well','noun'),('petróleo','oil, petroleum','noun'),('barril','barrel','noun'),('concesión','concession, permission given by the state to a company','noun'),('descubrir','to discover','verb'),('exportar','to export','verb')],
 exercises=[
  match('E.ex01',[('el pozo','well'),('el petróleo','oil'),('el barril','barrel'),('la concesión','permission given by the state to a company')],V),
  fb('E.ex02','Antes de que se __ el petróleo, Venezuela vivía del café y del cacao.',None,'Before oil was discovered, Venezuela lived from coffee and cacao.','antes-despues-de-que',hint='descubrir',answers=['descubriera','descubriese']),
  mc('E.ex03','Which sentence means "Before the company arrived, the village was quiet"?',['Antes de que llegara la empresa, el pueblo era tranquilo.','Antes de que llegó la empresa, el pueblo era tranquilo.','Antes de que llegaba la empresa, el pueblo era tranquilo.'],'antes-despues-de-que',ds={1:'preterito-indefinido',2:'imperfect'}),
  sb('E.ex04','Antes de que llegara el petróleo, Venezuela exportaba sobre todo café.','Before oil arrived, Venezuela exported mainly coffee.','antes-despues-de-que'),
  dlg('E.ex05',[('Meg','¿Qué es una concesión petrolera?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es un permiso del Estado para que una empresa busque petróleo.','Es un barril que se usa para vender petróleo en el puerto.','Es una torre que ayuda a sacar el petróleo de un pozo.'],V),
  dic('E.ex06','Después de que descubrieron el petróleo, la economía cambió.','After they discovered oil, the economy changed.','antes-despues-de-que'),
  reading('E.ex07','What did Venezuela live from before oil, according to the text?',['Vivía sobre todo del café y del cacao.','Vivía sobre todo de las minas de oro.','Vivía sobre todo del turismo en las playas.']),
 ],
 story=dict(title='Zumaque I y Barroso II',
  summary='Venezuela was an agricultural country until the first commercial oil well opened in Zulia in 1914; by 1928 it was the second producer in the world, and in 1936 Arturo Uslar Pietri called for "sowing the oil".',
  paras=[
  "Antes de que se descubriera el petróleo, Venezuela era un país agrícola que vivía sobre todo del café y del cacao. Todo cambió en el estado Zulia, cerca del lago de Maracaibo. El 31 de julio de 1914 el pozo Zumaque I, en Mene Grande, empezó a producir petróleo. Fue el primer pozo comercial del país, y muchos historiadores lo consideran el comienzo de la industria petrolera venezolana.",
  "En esos años gobernaba Juan Vicente Gómez, que estuvo en el poder desde 1908 hasta su muerte en 1935. Su gobierno dio concesiones a empresas extranjeras, sobre todo estadounidenses, británicas y holandesas, para buscar y sacar petróleo.",
  "En diciembre de 1922, en Cabimas, en la orilla oriental del lago de Maracaibo, el pozo Barroso II echó petróleo sin control durante varios días. Los historiadores consideran que ese accidente mostró al mundo la riqueza del subsuelo venezolano. Después de que ocurrió, llegaron más empresas a la región.",
  "En 1928 Venezuela ya era el segundo productor de petróleo del mundo, después de Estados Unidos, y el petróleo pasó a ser su principal exportación. La agricultura perdió importancia, y mucha gente del campo se fue a las ciudades.",
  "En 1936 el escritor Arturo Uslar Pietri publicó un artículo en el diario Ahora con una idea famosa: «sembrar el petróleo». Quería decir que el dinero del petróleo debía usarse para desarrollar otras actividades del país. Desde entonces, esa frase se repite en los debates sobre la economía venezolana."],
  qs=[("When did the well Zumaque I begin to produce oil?",["El 31 de julio de 1914.","En diciembre de 1922.","En 1936."],"The first paragraph gives the date."),
      ("What happened at Barroso II in December 1922?",["El pozo echó petróleo sin control durante varios días.","El pozo se cerró para siempre.","Se firmó la primera concesión."],"The third paragraph describes it."),
      ("What did Uslar Pietri mean by \"sembrar el petróleo\"?",["Que el dinero del petróleo debía servir para desarrollar otras actividades.","Que había que plantar café en los pozos.","Que había que vender todo el petróleo a Estados Unidos."],"The last paragraph explains the idea.")]))

L['03']=dict(
 title="Villanueva's Ciudad Universitaria: a campus that is a World Heritage site",
 goal="Describe the Ciudad Universitaria of Caracas with comparisons that use como si.",
 grammar_label='como si + imperfect subjunctive',
 goal_items=["I can make a comparison with something unreal using *como si* and the imperfect subjunctive.",
  "I can say who designed the Ciudad Universitaria and what UNESCO decided in 2000.",
  "I can use the new words for architect, mural and sculpture."],
 screen=screen('x','As If: The Ciudad Universitaria',
  "You know *como si* from B2 Unit 15: it introduces a comparison with something unreal, and the verb that follows is always in the imperfect subjunctive (*Habla como si lo supiera todo*), whether the first verb is in the present or in the past. A campus that is also a gallery is full of such comparisons.",
  'Como si with the imperfect subjunctive',
  [("Las nubes cuelgan del techo como si fueran nubes de verdad.","*como si fueran*: it is not true, it only looks like it"),
   ("Los estudiantes caminan por el campus como si estuvieran en una ciudad.","*como si estuvieran*: imperfect subjunctive of *estar*"),
   ("El guía habla del arquitecto como si lo conociera.","*como si conociera*: he does not know him"),
   ("Hablaba de arte como si fuera un experto.","after a past verb the rule is the same")],
  [("Las Nubes de Calder cuelgan del techo como si fueran nubes de verdad.","Calder's Clouds hang from the ceiling as if they were real clouds."),
   ("Los estudiantes caminan por el campus como si estuvieran en una ciudad.","The students walk across the campus as if they were in a city."),
   ("El arquitecto diseñó el campus como si fuera una ciudad.","The architect designed the campus as if it were a city."),
   ("Habla de arte como si fuera un experto.","He talks about art as if he were an expert.")],
  "After *como si* never use the indicative or the present subjunctive: *como si son* and *como si sean* are mistakes. The imperfect subjunctive marks the distance from reality, just as English says \"as if it were\"."),
 vocab_title='The Ciudad Universitaria: architect, mural and sculpture',
 vocab_theme='Villanueva and the campus of the Central University of Venezuela',
 vocab=[('arquitecto','architect','noun'),('mural','mural, large painting on a wall','noun'),('escultura','sculpture','noun'),('aula','lecture hall, classroom','noun'),('nube','cloud','noun'),('techo','ceiling, roof','noun')],
 exercises=[
  match('E.ex01',[('el arquitecto','architect'),('el mural','large painting on a wall'),('la escultura','sculpture'),('la nube','cloud')],V),
  fb('E.ex02','Los estudiantes caminan por el campus como si __ en una ciudad.',None,'The students walk across the campus as if they were in a city.','como-si',hint='estar',answers=['estuvieran','estuviesen']),
  mc('E.ex03','Which sentence means "The clouds hang from the ceiling as if they were real clouds"?',['Las nubes cuelgan del techo como si fueran nubes de verdad.','Las nubes cuelgan del techo como si son nubes de verdad.','Las nubes cuelgan del techo como si sean nubes de verdad.'],'como-si',ds={1:'present-tense',2:'subjuntivo-morfologia'}),
  sb('E.ex04','El arquitecto diseñó el campus como si fuera una ciudad.','The architect designed the campus as if it were a city.','como-si'),
  dlg('E.ex05',[('Meg','¿Qué es un mural?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es una pintura grande hecha sobre una pared.','Es una escultura pequeña que se pone sobre una mesa.','Es un techo de madera que está encima de un aula.'],V),
  dic('E.ex06','El campus parece una ciudad pequeña, como si tuviera sus propias calles.','The campus looks like a small city, as if it had its own streets.','como-si'),
  reading('E.ex07','What did UNESCO do in 2000, according to the text?',['Declaró la Ciudad Universitaria de Caracas Patrimonio de la Humanidad.','Declaró el pozo Zumaque I Patrimonio de la Humanidad.','Declaró el parque nacional El Ávila Patrimonio de la Humanidad.']),
 ],
 story=dict(title='La Ciudad Universitaria de Caracas',
  summary="The Ciudad Universitaria of Caracas, designed by Carlos Raúl Villanueva with artists from several countries, became a UNESCO World Heritage site in 2000.",
  paras=[
  "La Ciudad Universitaria de Caracas es el campus de la Universidad Central de Venezuela, una universidad que existe desde 1721. Fue diseñada por el arquitecto Carlos Raúl Villanueva, que empezó el proyecto en los años cuarenta y trabajó en él durante décadas.",
  "En 2000 la UNESCO declaró el campus Patrimonio de la Humanidad. Según la UNESCO, es una obra maestra de la arquitectura, del urbanismo y del arte modernos.",
  "Villanueva quería unir la arquitectura con otras artes. Por eso trabajó con artistas de varios países, entre ellos el estadounidense Alexander Calder, el francés Fernand Léger y Victor Vasarely, nacido en Hungría, además de artistas venezolanos. Sus murales y esculturas están dentro de los edificios y en las plazas, y no solo en los museos.",
  "En el Aula Magna, una gran sala para actos y conciertos, cuelgan del techo las Nubes de Calder, unos paneles que ayudan al sonido de la sala. Parecen nubes de verdad, como si flotaran sobre el público.",
  "Los pasillos cubiertos y las plazas permiten caminar por el campus protegido del sol y de la lluvia, casi como si fuera una pequeña ciudad. Esa idea de ciudad dentro de la ciudad aparece incluso en el nombre: Ciudad Universitaria."],
  qs=[("Who designed the Ciudad Universitaria?",["El arquitecto Carlos Raúl Villanueva.","El escritor Arturo Uslar Pietri.","El naturalista Alexander von Humboldt."],"The first paragraph names him."),
      ("What are the Nubes de Calder?",["Son paneles que cuelgan del techo del Aula Magna y ayudan al sonido.","Son pinturas de nubes en los pasillos.","Son los nombres de los edificios del campus."],"The fourth paragraph describes them."),
      ("What did Villanueva want to unite with architecture?",["Otras artes, como la pintura y la escultura.","La industria del petróleo.","La agricultura del valle."],"The third paragraph explains his idea.")]))

L['04']=dict(
 title='Kinetic art: Cruz-Diez, Soto and the art of movement',
 goal="Give your attitude to facts about Venezuelan kinetic art with stance adverbs.",
 grammar_label='stance adverbs',
 goal_items=["I can show my attitude to a fact with stance adverbs such as *en realidad* and *lamentablemente*.",
  "I can say who Cruz-Diez and Soto were and what kinetic art is.",
  "I can use the new words for kinetic, work of art and movement."],
 screen=screen('x','Your Attitude: Stance Adverbs and Kinetic Art',
  "You know *francamente* and stance adverbs from B2 Unit 1: *francamente*, *lamentablemente*, *en realidad*, *en rigor*. They step outside the sentence and say how the speaker feels about the fact, and a comma marks each edge. Talking about art invites opinions, so they are useful here.",
  'Adverbs that show your attitude',
  [("En realidad, Soto nació en Ciudad Bolívar, no en Caracas.","*en realidad*: you correct what someone assumed"),
   ("En rigor, Cruz-Diez nació en Caracas.","*en rigor*: you give the exact truth"),
   ("Lamentablemente, no puedo ver la exposición esta semana.","*lamentablemente*: your feeling about a fact"),
   ("Francamente, la obra de Cruz-Diez me parece fascinante.","*francamente*: you are direct about your opinion")],
  [("En realidad, Soto nació en Ciudad Bolívar.","Actually, Soto was born in Ciudad Bolívar."),
   ("Lamentablemente, no puedo ver la exposición esta semana.","Unfortunately, I cannot see the exhibition this week."),
   ("Francamente, la obra de Cruz-Diez me parece fascinante.","Frankly, Cruz-Diez's work seems fascinating to me."),
   ("En Ciudad Bolívar, precisamente su ciudad natal, está el Museo Soto.","In Ciudad Bolívar, precisely his home town, is the Soto Museum.")],
  "Try the comma test: if you can pause and put commas around the adverb, it comments on the whole sentence. *Precisamente* takes no commas, because it points at the word after it. Use one stance adverb per sentence; two in a row sound heavy."),
 vocab_title='Kinetic art: movement, colour and light',
 vocab_theme='Cruz-Diez, Soto and kinetic art',
 vocab=[('cinético','kinetic, of movement','adjective'),('obra','work (of art)','noun'),('movimiento','movement','noun'),('penetrable','"penetrable", a work you can walk into','noun'),('color','colour','noun'),('luz','light','noun')],
 exercises=[
  match('E.ex01',[('cinético','of movement'),('la obra','work of art'),('el movimiento','movement'),('el penetrable','work you can walk into')],V),
  fb('E.ex02','En Ciudad Bolívar, __ su ciudad natal, está el Museo Soto.','precisamente','In Ciudad Bolívar, precisely his home town, is the Soto Museum.','stance-adverbs',hint='exactly'),
  mc('E.ex03','Which sentence means "Unfortunately, I cannot see the exhibition this week"?',['Lamentablemente, no puedo ver la exposición esta semana.','Lamentable, no puedo ver la exposición esta semana.','Lamentando, no puedo ver la exposición esta semana.'],'stance-adverbs'),
  sb('E.ex04','En realidad, Soto nació en Ciudad Bolívar.','Actually, Soto was born in Ciudad Bolívar.','stance-adverbs'),
  dlg('E.ex05',[('Meg','¿Qué es una obra cinética?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es una obra con movimiento que cambia de color.','Es una obra que solo se puede ver en un museo de París.','Es una obra que está hecha con petróleo y con luz.'],V),
  dic('E.ex06','Francamente, la obra de Cruz-Diez me parece fascinante.','Frankly, Cruz-Diez\'s work seems fascinating to me.','stance-adverbs'),
  reading('E.ex07','Where is the museum with Jesús Soto\'s name, according to the text?',['Está en Ciudad Bolívar, su ciudad natal.','Está en Caracas, junto a la Ciudad Universitaria.','Está en París, donde murió.']),
 ],
 story=dict(title='El arte cinético: Cruz-Diez y Soto',
  summary="Kinetic art is the art of movement, and two of its best-known artists, Carlos Cruz-Diez and Jesús Rafael Soto, were born in Venezuela in 1923 and lived for years in Paris.",
  paras=[
  "El arte cinético es un arte del movimiento: sus obras se mueven o parecen moverse, o cambian cuando el público se mueve delante de ellas. Dos de los artistas más conocidos de este movimiento son venezolanos: Carlos Cruz-Diez, nacido en Caracas en 1923, y Jesús Rafael Soto, nacido en Ciudad Bolívar el mismo año.",
  "Los dos vivieron muchos años en París, y allí murieron: Soto en 2005 y Cruz-Diez en 2019. Sus obras están hoy en museos y en espacios públicos de muchos países.",
  "Cruz-Diez investigó cómo cambia el color según la luz y según el lugar desde donde lo miramos. En sus obras, el color parece cambiar cuando el público camina delante de ellas. Para él, el color no era solo una pintura sobre una superficie, sino algo que ocurre en el espacio.",
  "Soto es conocido por sus «penetrables», obras formadas por muchos hilos de colores entre los que las personas pueden entrar y caminar. En Ciudad Bolívar, su ciudad natal, hay un museo con su nombre.",
  "Según muchos críticos, el dinero del petróleo y la modernización de los años cincuenta ayudaron a que el arte cinético tuviera tanta fuerza en Venezuela, porque se construyeron edificios nuevos, como la Ciudad Universitaria, que necesitaban obras de arte. Otros críticos dicen que fue sobre todo el talento de los artistas, y que su carrera se hizo en gran parte en Europa."],
  qs=[("What is kinetic art?",["Es un arte cuyas obras se mueven o cambian cuando el público se mueve.","Es un arte hecho solo con petróleo.","Es un arte que solo existe en Caracas."],"The first paragraph defines it."),
      ("What are Soto's \"penetrables\"?",["Son obras con hilos de colores en las que se puede entrar.","Son pinturas pequeñas de nubes.","Son esculturas de piedra del Ávila."],"The fourth paragraph describes them."),
      ("Why did kinetic art have so much strength in Venezuela, according to many critics?",["Por el dinero del petróleo y la modernización de los años cincuenta.","Por una ley que obligaba a pintar con colores.","Por la falta de museos en Europa."],"The last paragraph gives their view.")]))

L['05']=dict(
 title='The oil boom of the 1970s and its end',
 goal="Talk about what Venezuela should have done in the years of high oil prices, using deber + haber + past participle.",
 grammar_label='regrets and reproaches with debería haber + participle',
 goal_items=["I can say what should have been done with *debería haber* + past participle.",
  "I can tell what happened in Venezuela between 1973 and 1983.",
  "I can use the new words for boom, debt and devaluation."],
 screen=screen('x','Should Have: The Oil Boom and Its End',
  "You know *Deberías haber llamado* and regrets and reproaches from B2 Unit 10: the modal stays in the conditional and *haber* + past participle carries the past (*Deberías haber llamado*, *Me arrepiento de haber dicho eso*). Economists use the same pattern to look back at the years of high oil prices and say what the country should have done. Remember that these are opinions of people, not facts.",
  'Looking back',
  [("Deberíamos haber ahorrado más.","We should have saved more. (regret about ourselves)"),
   ("El país debería haber ahorrado más dinero.","The country should have saved more money. (reproach)"),
   ("Tendrían que haber usado el dinero para otras industrias.","They should have used the money for other industries."),
   ("Me arrepiento de no haber ahorrado más.","I regret not having saved more.")],
  [("Según varios economistas, el país debería haber ahorrado más en los años de precios altos.","According to several economists, the country should have saved more in the years of high prices."),
   ("Deberían haber usado el dinero para otras industrias, dicen algunos analistas.","They should have used the money for other industries, say some analysts."),
   ("Deberíamos haber ahorrado más.","We should have saved more."),
   ("Me arrepiento de no haber ahorrado más.","I regret not having saved more.")],
  "Compare *Deberíamos ahorrar más* (advice about now) with *Deberíamos haber ahorrado más* (a reproach about the past). Only *haber* carries the past: the modal stays *debería*, and the participle never changes: *haber ahorrado*. When you report a view like this, say whose it is."),
 vocab_title='The oil boom: boom, debt and devaluation',
 vocab_theme='Venezuela in the 1970s and early 1980s',
 vocab=[('auge','boom','noun'),('deuda','debt','noun'),('devaluación','devaluation, fall in the value of a currency','noun'),('moneda','currency','noun'),('ahorrar','to save (money)','verb'),('precio','price','noun')],
 exercises=[
  match('E.ex01',[('el auge','boom'),('la deuda','debt'),('la devaluación','fall in the value of a currency'),('la moneda','currency')],V),
  fb('E.ex02','El país debería haber __ más dinero en los años de precios altos.','ahorrado','The country should have saved more money in the years of high prices.','regrets-reproaches',hint='ahorrar'),
  mc('E.ex03','Which sentence means "We should have saved more"?',['Deberíamos haber ahorrado más.','Deberíamos ahorrar más.','Deberíamos haber ahorrar más.'],'regrets-reproaches',ds={1:'deber-vs-tener-que'}),
  sb('E.ex04','Me arrepiento de no haber ahorrado más.','I regret not having saved more.','regrets-reproaches'),
  dlg('E.ex05',[('Meg','¿Qué es una devaluación?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es cuando la moneda de un país pierde valor.','Es cuando un país vende más petróleo que antes.','Es cuando el gobierno pide dinero a otros países.'],V),
  dic('E.ex06','Deberían haber ahorrado más cuando el petróleo era caro.','They should have saved more when oil was expensive.','regrets-reproaches'),
  reading('E.ex07','What happened on 18 February 1983, according to the text?',['El gobierno bajó el valor de la moneda, el bolívar.','El Estado se hizo cargo de la industria petrolera.','Se fundó la OPEP en Bagdad.']),
 ],
 story=dict(title='La bonanza petrolera y su final',
  summary="High oil prices after 1973 and the nationalisation of 1976 brought a boom to Venezuela, which ended with the devaluation of 1983, and economists still disagree about what the country should have done differently.",
  paras=[
  "En 1960 Venezuela fue uno de los cinco países fundadores de la OPEP, la organización de países productores de petróleo, junto con Irak, Irán, Kuwait y Arabia Saudita. En 1973 los precios internacionales del petróleo subieron mucho, y los ingresos de Venezuela crecieron con ellos.",
  "El presidente Carlos Andrés Pérez, que gobernó de 1974 a 1979, nacionalizó la industria petrolera: el 1 de enero de 1976 el Estado tomó el control de las empresas extranjeras y empezó a funcionar Petróleos de Venezuela, PDVSA. Con el dinero del petróleo, el gobierno construyó carreteras, escuelas y hospitales, y muchos venezolanos viajaron y compraron productos importados. Muchos recuerdan esos años como una época de abundancia.",
  "Pero el país también pidió mucho dinero prestado, y a comienzos de los años ochenta bajaron los precios del petróleo. Durante años el dólar había costado 4,30 bolívares. El 18 de febrero de 1983, un día que se llamó «Viernes Negro», el gobierno del presidente Luis Herrera Campíns devaluó el bolívar y estableció un control de cambios.",
  "Según varios economistas, el país debería haber ahorrado más en los años de precios altos y haber ayudado a otros sectores de la economía, como pedía la idea de «sembrar el petróleo». Otros analistas responden que los precios dependían del mercado mundial, que ningún gobierno controlaba.",
  "En 2026 la situación política del país cambió: el 3 de enero fuerzas de Estados Unidos capturaron a Nicolás Maduro, y desde entonces Delcy Rodríguez gobierna como presidenta encargada. Ella ha prometido elecciones, pero todavía sin fecha."],
  qs=[("Which country was a founder of OPEC in 1960, according to the text?",["Venezuela.","Colombia.","Cuba."],"The first paragraph names the founders."),
      ("What happened on 1 January 1976?",["El Estado tomó el control de las empresas petroleras y empezó a funcionar PDVSA.","Se devaluó el bolívar.","Se descubrió el pozo Zumaque I."],"The second paragraph gives the date."),
      ("What do several economists say, according to the text?",["Que el país debería haber ahorrado más en los años de precios altos.","Que el país debería haber vendido menos petróleo en 2026.","Que el país nunca tuvo un auge petrolero."],"The fourth paragraph gives their opinion.")]))

L['consolidation']=dict(
 title='Review: the valley of Caracas, oil, art and the boom',
 goal="Review fronting, antes de que and después de que, como si, stance adverbs and regrets on the themes of this unit.",
 goal_items=["I can use fronting, *antes de que*, *como si*, stance adverbs and *debería haber* about Venezuela.",
  "I can tell Caracas, the first oil wells, the Ciudad Universitaria, kinetic art and the boom apart.",
  "I can read short Spanish texts about these topics and answer questions."],
 checklist_items=["I can put a place or a quality first for emphasis.",
  "I can say what was true before or after something with *antes de que* and *después de que*.",
  "I can make a comparison with something unreal using *como si*.",
  "I can show my attitude with stance adverbs and say what should have been done."],
 exercises=[
  match('E.ex01',[('el valle','valley'),('el pozo','well'),('el mural','large painting on a wall'),('la devaluación','fall in the value of a currency')],V),
  mc('E.ex02','Which sentence means "In 1800 Humboldt climbed the Silla de Caracas", with the year stressed?',['En 1800 subió Humboldt a la Silla de Caracas.','En 1800 subieron Humboldt a la Silla de Caracas.','En 1800 sube Humboldt a la Silla de Caracas.'],'inversion-enfasis-fronting',ds={2:'present-tense'}),
  fb('E.ex03','Subiremos a El Ávila antes de que __ a llover.','empiece','We will climb El Ávila before it starts to rain.','antes-despues-de-que',hint='empezar'),
  fb('E.ex04','El guía habla de Caracas como si la __ de memoria.',None,'The guide talks about Caracas as if he knew it by heart.','como-si',hint='conocer',answers=['conociera','conociese']),
  mc('E.ex05','Which sentence means "Frankly, the exhibition did not convince me"?',['Francamente, la exposición no me convenció.','Franco, la exposición no me convenció.','Franqueza, la exposición no me convenció.'],'stance-adverbs'),
  mc('E.ex06','Which sentence means "You should have warned us"?',['Deberías haber avisado.','Deberías avisar.','Deberías haber avisar.'],'regrets-reproaches',ds={1:'deber-vs-tener-que'}),
  reading('E.ex07','According to the texts, in which year did UNESCO declare the Ciudad Universitaria a World Heritage site?',['Se declaró en 2000.','Se declaró en 1958.','Se declaró en 1914.']),
  sw('E.ex08',[('Say that the guide talks as if he knew the whole city. Start with "El guía habla".','El guía habla como si conociera toda la ciudad.'),('Say that the students talk about art as if they were experts. Start with "Los estudiantes hablan".','Los estudiantes hablan de arte como si fueran expertos.')],'como-si'),
 ])

spec=dict(pre=P,uid='venezuela-oil-caracas',lessons={})
for n,l in L.items():
    stem=f'{P}-{n}'
    for e in l['exercises']: e['id']=e['id'].replace('E',stem,1)
    spec['lessons'][n]=l
build_unit(spec)
print('built')

M=lambda t,sc,pr,cu,tg,en,cd: dict(tier='tier1',level='B2',title='Communicative Challenge: '+t,scenario=sc,prompt=pr,cues=cu,target=tg,english=en,canDo=cd)
c={}
g=lambda n: L[n]['goal_items'][0]
c[P+'-01']=M('The Valley of Caracas','You are Meg. You and Carlos are watching a documentary about Caracas, and he asks where the city was founded.','Tell Carlos where Caracas was founded, putting the place first.',['Put the place at the start of the sentence','Say that the city was founded there'],'En un valle estrecho fue fundada Caracas en 1567.','Caracas was founded in 1567 in a narrow valley.',g('01'))
c[P+'-02']=M('Before the Oil','You are Carlos. You have read an article about the first oil wells, and Meg asks what Venezuela lived from before oil.','Tell Meg what Venezuela lived from before oil was discovered.',['Start with a "before" clause','Say what the country lived from'],'Antes de que se descubriera el petróleo, Venezuela vivía del café y del cacao.','Before oil was discovered, Venezuela lived from coffee and cacao.',g('02'))
c[P+'-03']=M('Clouds in the Aula Magna','You are Meg. You and Carlos are looking at photographs of the Ciudad Universitaria in Caracas, and he asks about the Calder panels.','Tell Carlos what the Calder panels look like.',['Say that they hang from the ceiling','Compare them to real clouds'],'Las Nubes de Calder cuelgan del techo como si fueran nubes de verdad.',"Calder's Clouds hang from the ceiling as if they were real clouds.",g('03'))
c[P+'-04']=M('Where Was Soto Born','You are Meg. Carlos says that Jesús Soto was born in Caracas, but the article you read says something else.','Correct Carlos politely, with a stance adverb.',['Start with a stance adverb','Say where Soto was born'],'En realidad, Soto nació en Ciudad Bolívar, no en Caracas.','Actually, Soto was born in Ciudad Bolívar, not in Caracas.',g('04'))
c[P+'-05']=M('What the Country Should Have Done','You are Carlos. You are telling Meg what economists say about the years of high oil prices.','Tell Meg what several economists say the country should have done.',['Say whose opinion it is','Say what the country should have done'],'Según varios economistas, el país debería haber ahorrado más en los años de precios altos.','According to several economists, the country should have saved more in the years of high prices.',g('05'))
c[P+'-consolidation']=M('A Short Summary','You are Meg. You are telling Carlos what you remember about the Ciudad Universitaria.','Say what UNESCO decided in 2000, and compare the campus to something.',['Say what UNESCO decided','Compare the campus to a city'],'En 2000 la UNESCO declaró la Ciudad Universitaria Patrimonio de la Humanidad. Parece una ciudad pequeña, como si tuviera sus propias calles.','In 2000 UNESCO declared the Ciudad Universitaria a World Heritage site. It looks like a small city, as if it had its own streets.',L['consolidation']['checklist_items'][0])
import json
json.dump(c,open('/home/user/parlour-read-b/challenges-venezuela-oil-caracas.json','w'),indent=2,ensure_ascii=False)
