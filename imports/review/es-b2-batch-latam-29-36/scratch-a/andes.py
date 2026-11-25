import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
V='b2-peru-cusco-andes-vocab'
S='b2-peruandino'

s=f'{S}-01'
gr(s,"The Cordillera Blanca: Cleft Sentences",
 "You know *Lo que dijo fue revelador* from B2 Unit 1, a cleft sentence: you split an idea into two halves joined by *ser* so that one piece stands in the spotlight (*Lo que dijo fue revelador*, *Fue en Lima donde se conocieron*). They work well for mountains and disasters, where one fact is what you want the listener to remember.",
 [("Lo que más llama la atención de la cordillera son sus glaciares.","*lo que* + verb + *ser* + focus; *son* agrees with the plural focus"),
  ("Lo que más preocupa a los científicos es el deshielo.","*lo que* spotlights an idea or a thing"),
  ("Fue en 1970 cuando un terremoto sacudió Áncash.","*fue* + time + *cuando* spotlights when"),
  ("Fue en el valle del río Santa donde nació este proyecto.","*fue* + place + *donde* spotlights where")],
 [("Lo que más llama la atención de la cordillera Blanca son sus glaciares.","What is most striking about the Cordillera Blanca is its glaciers."),
  ("Lo que más preocupa a los científicos es el deshielo.","What worries scientists most is the melting."),
  ("Fue en mayo de 1970 cuando un terremoto sacudió Áncash.","It was in May 1970 that an earthquake shook Áncash."),
  ("Fue en 1941 cuando un aluvión destruyó parte de Huaraz.","It was in 1941 that a flood destroyed part of Huaraz.")],
 "A cleft sentence is a spotlight: use it for the one idea you want to remember. The tense of *ser* follows the other verb: *fue* for the past, *es* for the present.")
voc(s,"Glaciers and mountain risk",[("el glaciar","glacier","noun"),("la laguna","lake in the mountains","noun"),("el aluvión","flood of water, mud and rock","noun"),("el deshielo","melting of ice and snow","noun")],"Peru: the Cordillera Blanca")
lesson(s,"The Cordillera Blanca: glaciers, floods and an earthquake","Talk about the glaciers of the Cordillera Blanca and the disasters of 1941 and 1970, putting one idea in the spotlight with cleft sentences.","cleft sentences and focus constructions",
 ["I can put one idea in the spotlight with a cleft sentence (*Lo que..., Fue en... cuando...*).","I can say where the Cordillera Blanca is and why its glaciers matter.","I can use the new words for the mountains: *glaciar*, *laguna*, *aluvión*, *deshielo*."])
story(s,"La cordillera Blanca y sus glaciares","The Cordillera Blanca in northern Peru has the country's highest peak and tropical glaciers that feed rivers; melting ice, a flood in 1941 and the earthquake of 1970 show how dangerous the mountains can be.",
["La cordillera Blanca, en la región de Áncash, en el norte de Perú, se considera la cordillera tropical más alta del mundo. Su cumbre más alta, el Huascarán, mide 6.768 metros. Entre la cordillera Blanca y la cordillera Negra corre hacia el Pacífico el río Santa, en un valle llamado Callejón de Huaylas.",
 "Lo que más llama la atención de la cordillera Blanca son sus glaciares. En la temporada seca, el agua del deshielo ayuda a mantener el caudal de los ríos, y de ese agua dependen el riego, el agua potable y algunas centrales eléctricas, como la del Cañón del Pato, en el río Santa. Según varios estudios, los glaciares de Perú han perdido una parte importante de su superficie desde la década de 1960, y los científicos lo relacionan con el aumento de la temperatura.",
 "Cuando el hielo se derrite, se forman lagunas en la montaña. Si una masa de hielo cae en una laguna, el agua puede desbordarse y bajar por la quebrada como un aluvión. Fue en 1941 cuando un aluvión de la laguna Palcacocha destruyó parte de la ciudad de Huaraz y causó muchas muertes. Hoy se vigilan varias lagunas de la cordillera.",
 "El 31 de mayo de 1970 un terremoto de magnitud 7,9 sacudió la costa y la sierra de Áncash. En la montaña, una masa de hielo y roca se desprendió del Huascarán y bajó como un alud hacia el valle. Enterró la ciudad de Yungay, y murieron miles de personas.",
 "Para proteger la zona, en 1975 se creó el Parque Nacional Huascarán, que la UNESCO incluyó en la lista del Patrimonio Mundial en 1985."],
[("What do the glaciers of the Cordillera Blanca do in the dry season?",["Su agua ayuda a mantener el caudal de los ríos.","Su hielo cierra los caminos hacia la costa.","Su agua baja solo hacia el océano Atlántico."],"The second paragraph explains the role of the meltwater."),
 ("What happened in 1941?",["Un aluvión de la laguna Palcacocha destruyó parte de Huaraz.","Un terremoto enterró la ciudad de Yungay.","Se creó el Parque Nacional Huascarán."],"The third paragraph describes the 1941 flood."),
 ("What happened to the city of Yungay in 1970?",["Un alud de hielo y roca la enterró.","Un aluvión la destruyó en 1941.","La UNESCO la incluyó en su lista."],"The fourth paragraph tells how the avalanche buried Yungay.")])
ex(s,[
 match([("el glaciar","glacier"),("la laguna","mountain lake"),("el aluvión","flood of water, mud and rock"),("el deshielo","melting of ice and snow")],V),
 fill("__ en mayo de 1970 cuando un terremoto sacudió Áncash.","Fue","It was in May 1970 that an earthquake shook Áncash.","oraciones-hendidas-enfasis"),
 mc("Which sentence says \"What worries scientists most is the melting\"?",["Lo que más preocupa a los científicos es el deshielo.","Lo que más preocupa a los científicos son el deshielo.","Que más preocupa a los científicos es el deshielo."],"oraciones-hendidas-enfasis"),
 build("Lo que más llama la atención de la cordillera son sus glaciares.","What is most striking about the mountain range is its glaciers.","oraciones-hendidas-enfasis"),
 dlg([("Meg","¿Qué es un aluvión?"),("Carlos","_____")],["Es agua con barro y piedras que baja por una quebrada.","Es una laguna alta que se forma con la nieve.","Es un camino de piedra que sube a la montaña."],V),
 dic("Fue en 1941 cuando un aluvión destruyó parte de la ciudad de Huaraz.","It was in 1941 that a flood destroyed part of the city of Huaraz.","oraciones-hendidas-enfasis")])

s=f'{S}-02'
gr(s,"Caral and Chavín: Before and After",
 "You know *antes de que* and *después de que* from B2 Unit 7: *antes de que* always takes the subjunctive, and *después de que* takes the indicative for something that happened and the subjunctive for something still to come. When the same person does both actions you use *antes de* or *después de* + infinitive, as in A2 Unit 4. They are the natural tools for the order of events in history.",
 [("Antes de que llegaran los incas, ya existían ciudades en los Andes.","*antes de que* + imperfect subjunctive after a past main verb"),
  ("Antes de que empiecen las excavaciones, hay que pedir permiso.","*antes de que* + present subjunctive for what has not happened yet"),
  ("Después de que empezaron las excavaciones, se conoció mejor Caral.","*después de que* + indicative: it happened"),
  ("Después de excavar, los arqueólogos estudian lo que encuentran.","same subject: *después de* + infinitive")],
 [("Antes de que los incas construyeran su imperio, ya había ciudades en los Andes.","Before the Incas built their empire, there were already cities in the Andes."),
  ("Después de que empezaron las excavaciones en 1994, se conoció mejor la ciudad de Caral.","After the excavations began in 1994, the city of Caral became better known."),
  ("Antes de que llegaran los incas, ya existía el centro religioso de Chavín.","Before the Incas arrived, the religious centre of Chavín already existed."),
  ("Después de excavar, los arqueólogos estudian lo que encuentran.","After digging, the archaeologists study what they find.")],
 "After *antes de que* the verb is always subjunctive: *antes de que llegaran*, never *antes de que llegaron*. After *después de que*, ask whether it happened: yes, indicative; not yet, subjunctive.")
voc(s,"Archaeology",[("el arqueólogo","archaeologist","noun"),("el templo","temple","noun"),("la pirámide","pyramid","noun"),("la tumba","tomb, grave","noun")],"Peru: before the Incas")
lesson(s,"Caral, Chavín and Sipán: Peru before the Incas","Tell what existed in Peru before the Incas, ordering events with antes de que and después de que.","clauses with antes de que and después de que",
 ["I can order events with *antes de que* and *después de que* and the right mood.","I can say what Caral, Chavín and Sipán were and where they are.","I can use the new words for archaeology: *arqueólogo*, *templo*, *pirámide*, *tumba*."])
story(s,"Caral, Chavín y Sipán","Long before the Incas, Peru had the city of Caral, about five thousand years old, the religious centre of Chavín and the Moche tomb of Sipán on the north coast.",
["Antes de que los incas construyeran su imperio, en el siglo XV, ya había habido en Perú ciudades, templos y reinos durante miles de años. Los arqueólogos conocen varios de ellos: Caral, Chavín y la cultura moche.",
 "Caral está en el valle de Supe, a unos 180 kilómetros al norte de Lima. Según los arqueólogos, fue habitada hace unos cinco mil años, entre más o menos el 3000 y el 1800 antes de Cristo, y es una de las ciudades más antiguas de América. Allí hay plazas y grandes templos con forma de pirámide. Después de que la arqueóloga Ruth Shady empezó a excavar en 1994, el sitio se hizo famoso, y en 2009 la UNESCO lo incluyó en la lista del Patrimonio Mundial.",
 "Chavín de Huántar, en Áncash, fue un centro religioso hace unos tres mil años. Según los arqueólogos, llegaban peregrinos de lugares lejanos. Debajo de los templos hay galerías de piedra, y en una de ellas está el Lanzón, una piedra tallada de más de cuatro metros de altura, con una figura que mezcla rasgos humanos y de felino.",
 "En la costa norte, y no en las montañas, vivieron los moches, entre más o menos los siglos I y VIII después de Cristo. En 1987 el arqueólogo Walter Alva descubrió en Sipán, en la región de Lambayeque, la tumba de un gobernante moche, con joyas de oro y plata. Desde entonces se le conoce como el Señor de Sipán.",
 "Todos estos sitios se pueden visitar hoy y muestran que, antes de que existiera el Tawantinsuyu, los pueblos de los Andes y de la costa ya construían templos, ciudades y tumbas de gran riqueza."],
[("Where is Caral?",["En el valle de Supe, al norte de Lima.","En Lambayeque, en la costa sur.","En Áncash, cerca de Chavín."],"The second paragraph places Caral in the Supe valley."),
 ("What is the Lanzón?",["Una piedra tallada que está en una galería de Chavín.","Una joya de oro de la tumba de Sipán.","Un templo de Caral con forma de pirámide."],"The third paragraph describes the Lanzón."),
 ("What did Walter Alva find in 1987?",["La tumba de un gobernante moche en Sipán.","La ciudad de Caral en el valle de Supe.","Las galerías de piedra de Chavín."],"The fourth paragraph describes the discovery.")])
ex(s,[
 match([("el arqueólogo","archaeologist"),("el templo","temple"),("la pirámide","pyramid"),("la tumba","tomb")],V),
 fill("Antes de __ llegaran los incas, ya existían ciudades en los Andes.","que","Before the Incas arrived, there were already cities in the Andes.","antes-despues-de-que"),
 mc("Which sentence says \"Before the Incas built their empire, there were already cities in the Andes\"?",["Antes de que los incas construyeran su imperio, ya había ciudades en los Andes.","Antes de que los incas construyen su imperio, ya había ciudades en los Andes.","Antes de los incas construyeran su imperio, ya había ciudades en los Andes."],"antes-despues-de-que"),
 build("Después de que empezaron las excavaciones en 1994, se conoció mejor la ciudad de Caral.","After the excavations began in 1994, the city of Caral became better known.","antes-despues-de-que"),
 dlg([("Meg","¿Qué es un arqueólogo?"),("Carlos","_____")],["Es una persona que estudia el pasado con restos como tumbas y templos.","Es una persona que pinta imágenes religiosas para las iglesias.","Es un guía que enseña las ciudades a los turistas."],V),
 dic("Antes de que llegaran los incas, ya existía el centro religioso de Chavín.","Before the Incas arrived, the religious centre of Chavín already existed.","antes-despues-de-que")])

s=f'{S}-03'
gr(s,"Tawantinsuyu and the Qhapaq Ñan: The Se Passive",
 "You know the passive with *se* from B1 Unit 6: *se* + a verb in the third person, which agrees with the thing that receives the action (*Se venden casas*). It is the usual way to say what is built, used or recorded without naming who did it, which suits the history of an empire.",
 [("Se construyeron puentes colgantes de fibra vegetal.","plural thing, plural verb: *puentes* → *construyeron*"),
  ("Se usaba el quipu para anotar números.","singular thing, singular verb: *el quipu* → *usaba*"),
  ("En 2014 se inscribió el Qhapaq Ñan en la lista de la UNESCO.","a one-off event in the past"),
  ("Se guardaban alimentos en depósitos del Estado.","a habit in the past: imperfect")],
 [("En el Qhapaq Ñan se construyeron escaleras y puentes en las montañas.","Stairs and bridges were built in the mountains along the Qhapaq Ñan."),
  ("En el imperio inca se usaban quipus para anotar números.","In the Inca empire quipus were used to record numbers."),
  ("En 2014 se inscribió el Qhapaq Ñan en la lista de la UNESCO.","In 2014 the Qhapaq Ñan was added to the UNESCO list."),
  ("Se guardaban alimentos en depósitos del Estado.","Food was stored in state storehouses.")],
 "The verb agrees with the thing, not with *se*: *se usaban quipus*, not *se usaba quipus*. If you want to name the doer, switch to the *ser* passive: *fue construido por los incas*.")
voc(s,"The Inca empire",[("el chasqui","relay runner who carried messages","noun"),("el quipu","cord with knots used for recording numbers","noun"),("el imperio","empire","noun"),("el puente","bridge","noun")],"Peru: the Inca empire")
lesson(s,"Tawantinsuyu and the Qhapaq Ñan: the Inca empire and its roads","Say how the Inca empire was organised and connected, using the se passive.","the passive se construction",
 ["I can say what was built, used or kept with the passive *se* (*se construyeron*, *se usaban*).","I can say what Tawantinsuyu and the Qhapaq Ñan were.","I can use the new words for the empire: *chasqui*, *quipu*, *imperio*, *puente*."])
story(s,"Tawantinsuyu y el Qhapaq Ñan","The Inca empire called Tawantinsuyu was linked by a network of roads, the Qhapaq Ñan, with relay runners and knotted-cord records; UNESCO listed the road system in 2014.",
["Los incas llamaban a su imperio Tawantinsuyu, una palabra quechua que significa «las cuatro regiones». Su capital era Cusco. El imperio creció sobre todo en el siglo XV y llegó a ocupar una gran parte de los Andes, desde el sur de Colombia hasta el centro de Chile y el noroeste de Argentina.",
 "Para unir esa región se construyó una red de caminos, el Qhapaq Ñan, que en quechua quiere decir «camino principal». Según la UNESCO, la red tenía más de treinta mil kilómetros. En las montañas se hicieron escaleras de piedra y puentes colgantes de fibra vegetal, y a lo largo de los caminos había casas de descanso para los viajeros.",
 "Por esos caminos corrían los chasquis, mensajeros que se turnaban en postas para llevar noticias y órdenes. Los funcionarios del Estado anotaban cantidades de personas y de productos en quipus, cuerdas con nudos. Se sabe que los quipus servían para registrar números, y todavía se discute si también servían para otras cosas.",
 "El Estado inca no usaba monedas. Las comunidades trabajaban por turnos para el Estado, en un sistema llamado mit'a, y se guardaban alimentos en depósitos del Estado. En 1532 los españoles capturaron al Inca Atahualpa en Cajamarca, y los caminos siguieron usándose durante la época colonial.",
 "En 2014 se inscribió el Qhapaq Ñan, un sistema de caminos compartido por seis países, en la lista del Patrimonio Mundial de la UNESCO. Hoy las comunidades de la zona todavía renuevan cada año el puente colgante de Q'eswachaka, que se teje con hierba."],
[("What does Tawantinsuyu mean?",["«Las cuatro regiones».","«Camino principal».","«Ciudad de Cusco»."],"The first paragraph gives the meaning of the word."),
 ("What did the chasquis do?",["Llevaban noticias y órdenes por los caminos.","Anotaban números en cuerdas con nudos.","Construían puentes de hierba."],"The third paragraph describes the chasquis and the quipus separately."),
 ("What happened in 2014?",["Se inscribió el Qhapaq Ñan en la lista de la UNESCO.","Los españoles capturaron a Atahualpa.","Se creó el Parque Nacional Huascarán."],"The last paragraph gives the UNESCO listing.")])
ex(s,[
 match([("el chasqui","relay runner"),("el quipu","cord with knots for numbers"),("el imperio","empire"),("el puente","bridge")],V),
 fill("En 2014 __ inscribió el Qhapaq Ñan en la lista de la UNESCO.","se","In 2014 the Qhapaq Ñan was added to the UNESCO list.","pasiva-refleja"),
 mc("Which sentence says \"Hanging bridges of plant fibre were built\"?",["Se construyeron puentes colgantes de fibra vegetal.","Se construyó puentes colgantes de fibra vegetal.","Construyeron se puentes colgantes de fibra vegetal."],"pasiva-refleja"),
 build("En el imperio inca se usaban quipus para anotar números.","In the Inca empire quipus were used to record numbers.","pasiva-refleja"),
 dlg([("Meg","¿Qué hacía un chasqui?"),("Carlos","_____")],["Llevaba mensajes por los caminos.","Anotaba los números con un quipu.","Construía puentes para los caminos."],V),
 dic("En el Qhapaq Ñan se construyeron escaleras y puentes en las montañas.","Stairs and bridges were built in the mountains along the Qhapaq Ñan.","pasiva-refleja")])

s=f'{S}-04'
gr(s,"Cusco School: Stance Adverbs",
 "You know *lamentablemente* from B2 Unit 1, and the other stance adverbs: *francamente*, *en rigor*, *precisamente* and *apenas*. A stance adverb steps outside the sentence and shows how you see a fact, or how exact it is. In writing about art and history you use them to say what is a pity, what is exact, and what is barely known.",
 [("Lamentablemente, el terremoto de 1650 dañó muchos edificios de Cusco.","*lamentablemente*: your feeling about a fact"),
  ("En rigor, la Escuela Cusqueña no era solo de Cusco.","*en rigor*: strictly speaking, the exact truth"),
  ("Precisamente en la catedral está la Última Cena de Zapata.","*precisamente*: exactly there"),
  ("De muchos pintores apenas se conoce el nombre.","*apenas*: barely; no commas, right before the verb")],
 [("Lamentablemente, el terremoto de 1650 dañó muchos edificios de Cusco.","Unfortunately, the 1650 earthquake damaged many buildings in Cusco."),
  ("En rigor, la Escuela Cusqueña no era solo de Cusco: sus obras se vendían por toda la región.","Strictly speaking, the Cusco School was not only from Cusco: its works were sold throughout the region."),
  ("Precisamente en la catedral de Cusco está la Última Cena de Marcos Zapata.","It is exactly in Cusco cathedral that Marcos Zapata's Last Supper hangs."),
  ("De muchos pintores apenas se conoce el nombre.","Of many painters the name is barely known.")],
 "A stance adverb takes a comma after it at the start of a sentence: *Lamentablemente, ...*. Use it to give your own view or to make a fact exact, and keep the rest of the sentence factual.")
voc(s,"Painting and colonial Cusco",[("el pintor","painter","noun"),("el cuadro","painting","noun"),("la catedral","cathedral","noun"),("el gremio","guild, association of people with the same trade","noun")],"Peru: the Cusco School")
lesson(s,"Cusco: colonial painting on Inca walls","Describe colonial Cusco and its school of painting, showing your attitude with stance adverbs.","stance adverbs",
 ["I can show my attitude to a fact with stance adverbs (*lamentablemente*, *en rigor*, *precisamente*, *apenas*).","I can say what the Cusco School of painting was and what it mixed.","I can use the new words for art: *pintor*, *cuadro*, *catedral*, *gremio*."])
story(s,"Cusco y la Escuela Cusqueña","In colonial Cusco churches rose on Inca walls, and Indigenous and mestizo painters created the Cusco School, which mixed European models with Andean plants, animals and gold.",
["Cusco fue la capital del imperio inca, y cuando llegaron los españoles construyeron sus iglesias sobre muros incas. El convento de Santo Domingo se levantó sobre el Qorikancha, el templo principal del Sol. Lamentablemente, los terremotos de 1650 y de 1950 dañaron gran parte de la ciudad, pero muchos muros incas siguieron en pie.",
 "La catedral de Cusco, en la Plaza de Armas, se construyó entre 1559 y 1654. Precisamente allí se conservan muchos cuadros de la época colonial.",
 "Durante los siglos XVII y XVIII se desarrolló en Cusco la llamada Escuela Cusqueña de pintura. Pintores indígenas y mestizos pintaban imágenes religiosas para iglesias y conventos de los Andes. Usaban modelos europeos, pero añadían elementos de la región: plantas, aves, frutas y paisajes andinos. A menudo decoraban la ropa de las figuras con láminas de oro, una técnica llamada brocateado. De muchos pintores apenas se conoce el nombre. En rigor, la escuela no era solo de Cusco, porque sus obras se vendían por toda la región.",
 "Según algunos historiadores, la forma triangular de ciertas imágenes de la Virgen recuerda una montaña sagrada de los Andes. En 1688 un grupo de pintores indígenas se separó del gremio de pintores de la ciudad.",
 "Uno de los cuadros más conocidos es la Última Cena que pintó Marcos Zapata hacia 1753 para la catedral. En la mesa de Jesús y los apóstoles hay un cuy asado, un animal típico de los Andes."],
[("On which Inca building was the convent of Santo Domingo built?",["Sobre el Qorikancha.","Sobre la catedral de la Plaza de Armas.","Sobre el puente de Q'eswachaka."],"The first paragraph names the Qorikancha."),
 ("What did the painters of the Cusco School add to European models?",["Plantas, aves, frutas y paisajes andinos.","Barcos, caballos y castillos de Europa.","Mapas de los caminos incas."],"The third paragraph lists the local elements."),
 ("What is unusual about Marcos Zapata's Last Supper?",["En la mesa hay un cuy asado.","Los apóstoles llevan ropa inca.","Jesús está en la montaña."],"The last paragraph mentions the roast guinea pig.")])
ex(s,[
 match([("el pintor","painter"),("el cuadro","painting"),("la catedral","cathedral"),("el gremio","trade association")],V),
 fill("En __, la Escuela Cusqueña no era solo de Cusco: sus obras se vendían por toda la región.","rigor","Strictly speaking, the Cusco School was not only from Cusco: its works were sold throughout the region.","stance-adverbs"),
 mc("Which sentence says \"Unfortunately, the name of many painters is barely known\"?",["Lamentablemente, de muchos pintores apenas se conoce el nombre.","Lamentable, de muchos pintores apenas se conoce el nombre.","Lamentando, de muchos pintores apenas se conoce el nombre."],"stance-adverbs"),
 build("Precisamente en la catedral de Cusco está la Última Cena de Marcos Zapata.","It is exactly in Cusco cathedral that Marcos Zapata's Last Supper hangs.","stance-adverbs"),
 dlg([("Meg","¿Qué es un gremio?"),("Carlos","_____")],["Es una asociación de personas que tienen el mismo oficio.","Es un cuadro con una imagen religiosa para una iglesia.","Es un templo de los incas para el Sol."],V),
 dic("Lamentablemente, el terremoto de 1650 dañó muchos edificios de Cusco.","Unfortunately, the 1650 earthquake damaged many buildings in Cusco.","stance-adverbs")])

s=f'{S}-05'
gr(s,"Quechua Today: Reporting Verbs",
 "You know *afirmar* from B2 Unit 18, and the other reporting verbs (*advertir*, *recordar*, *señalar*, *negar*): they say not only that someone spoke but how. A fact the speaker states takes the indicative; a claim that is rejected, a suggestion or an order takes the subjunctive. They are what you need to report what experts and defenders of a language say.",
 [("Varios lingüistas señalan que el quechua pierde hablantes jóvenes.","*señalar que* + indicative: a fact they point out"),
  ("Los defensores de la lengua afirman que muchos artistas la usan.","*afirmar que* + indicative: states it firmly"),
  ("Los lingüistas recuerdan que se asoció con la discriminación.","*recordar que* + indicative: reminds of a fact"),
  ("Nadie niega que el quechua sea una lengua viva.","*negar que* + subjunctive: a claim that is rejected")],
 [("Varios lingüistas señalan que el quechua pierde hablantes jóvenes en las ciudades.","Several linguists point out that Quechua is losing young speakers in the cities."),
  ("Los defensores de la lengua afirman que algunos artistas jóvenes la usan en su música.","The defenders of the language say that some young artists use it in their music."),
  ("Los lingüistas recuerdan que durante mucho tiempo el quechua se asoció con la discriminación.","Linguists remind us that for a long time Quechua was associated with discrimination."),
  ("Nadie niega que el quechua sea una lengua viva.","Nobody denies that Quechua is a living language.")],
 "Name who says it: a reporting verb makes the source clear, so the reader can see what is a fact and what is a claim. Tense follows B2 Unit 17: after a past verb, shift the tense back.")
voc(s,"Language and speakers",[("la lengua","language; tongue","noun"),("el hablante","speaker of a language","noun"),("el sufijo","suffix","noun"),("el censo","census","noun")],"Peru: Quechua")
lesson(s,"Quechua today: a living language in Peru","Report what linguists and speakers say about Quechua, using reporting verbs.","reporting verbs like afirmar, advertir and negar",
 ["I can report what experts and speakers say with reporting verbs (*señalar*, *afirmar*, *recordar*, *negar*).","I can say how many people speak Quechua in Peru, according to the census.","I can use the new words for language: *lengua*, *hablante*, *sufijo*, *censo*."])
story(s,"El quechua hoy","Quechua is the most widely spoken Indigenous language in the Americas; in Peru almost four million people said in the 2017 census that they learned it as children, and linguists and defenders of the language describe both loss and revival.",
["El quechua es la lengua indígena más hablada de América, según los lingüistas. Según el censo de 2017, casi cuatro millones de personas en Perú dijeron que habían aprendido quechua en la infancia. También se habla en Bolivia y en Ecuador, donde se llama kichwa.",
 "En Perú, la Constitución de 1993 reconoce el quechua como lengua oficial, junto con el castellano, en las zonas donde predomina. En 2016 un programa de la televisión pública, Ñuqanchik, empezó a emitirse en quechua.",
 "El quechua se construye añadiendo sufijos a una raíz, y una sola palabra puede decir lo que en español necesita una frase entera. Además, tiene dos formas para «nosotros»: ñuqanchik incluye a la persona que escucha, y ñuqayku no la incluye.",
 "Varios lingüistas señalan que el quechua pierde hablantes jóvenes en las ciudades, y recuerdan que durante mucho tiempo se asoció con la discriminación. Los defensores de la lengua afirman, en cambio, que algunos artistas jóvenes la usan en su música y que quieren que se enseñe en las escuelas.",
 "El escritor José María Arguedas, que creció entre hablantes de quechua, escribió sus novelas en castellano, y en ellas se nota la influencia de esa lengua. Su novela más conocida es Los ríos profundos, publicada en 1958. También publicó poemas en quechua."],
[("What did almost four million people in Peru say in the 2017 census?",["Que habían aprendido quechua en la infancia.","Que hablaban solo castellano en casa.","Que vivían en Bolivia y en Ecuador."],"The first paragraph reports the census."),
 ("What is special about «nosotros» in Quechua?",["Tiene una forma que incluye a quien escucha y otra que no.","Tiene una sola forma para todos los casos.","Se escribe siempre con un sufijo de plural."],"The third paragraph describes the two forms."),
 ("What do the defenders of the language say?",["Que algunos artistas jóvenes la usan en su música.","Que el quechua ya no tiene hablantes jóvenes.","Que la Constitución prohíbe usarla."],"The fourth paragraph reports their claim.")])
ex(s,[
 match([("la lengua","language"),("el hablante","speaker of a language"),("el sufijo","ending added to a word"),("el censo","count of the people of a country")],V),
 fill("Varios lingüistas __ que el quechua pierde hablantes jóvenes en las ciudades.","señalan","Several linguists point out that Quechua is losing young speakers in the cities.","reporting-verbs",hint="point out"),
 mc("Which sentence says \"The linguists warn that Quechua is losing young speakers\"?",["Los lingüistas advierten que el quechua pierde hablantes jóvenes.","Los lingüistas advierten que el quechua pierda hablantes jóvenes.","Los lingüistas advierten de que el quechua pierde hablantes jóvenes."],"reporting-verbs"),
 build("Los defensores de la lengua afirman que algunos artistas jóvenes la usan en su música.","The defenders of the language say that some young artists use it in their music.","reporting-verbs"),
 dlg([("Meg","¿Qué es un sufijo?"),("Carlos","_____")],["Es una parte que se añade al final de un nombre.","Es una persona que habla dos lenguas muy bien.","Es una lista de las personas de un país."],V),
 dic("Los lingüistas recuerdan que durante mucho tiempo el quechua se asoció con la discriminación.","Linguists remind us that for a long time Quechua was associated with discrimination.","reporting-verbs")])

s=f'{S}-consolidation'
ex(s,[
 match([("el glaciar","glacier"),("la tumba","tomb"),("el chasqui","relay runner"),("el censo","count of the people of a country")],V),
 fill("Lo que más llama la atención del Qhapaq Ñan __ su historia.","es","What is most striking about the Qhapaq Ñan is its history.","oraciones-hendidas-enfasis"),
 mc("Which sentence says \"Before the Spaniards arrived, the Inca roads already existed\"?",["Antes de que llegaran los españoles, ya existían los caminos incas.","Antes de que llegan los españoles, ya existían los caminos incas.","Antes de los españoles llegaran, ya existían los caminos incas."],"antes-despues-de-que"),
 mc("Which sentence says \"Stone stairs were built in the mountains\"?",["Se hicieron escaleras de piedra en las montañas.","Se hizo escaleras de piedra en las montañas.","Hicieron se escaleras de piedra en las montañas."],"pasiva-refleja"),
 mc("Which sentence says \"Strictly speaking, the Cusco School was not only from Cusco\"?",["En rigor, la Escuela Cusqueña no era solo de Cusco.","En rigor de, la Escuela Cusqueña no era solo de Cusco.","Rigor, la Escuela Cusqueña no era solo de Cusco."],"stance-adverbs"),
 fill("Los lingüistas __ que el quechua pierde hablantes jóvenes.","advierten","The linguists warn that Quechua is losing young speakers.","reporting-verbs",hint="warn"),
 mc("According to the texts, what happened in May 1970?",["Un terremoto sacudió Áncash.","Un aluvión destruyó Huaraz.","Empezó la Escuela Cusqueña."],None,cat="reading"),
 {"type":"sentence-order","category":"grammar","sentences":["Caral fue habitada hace unos cinco mil años. [Caral was inhabited about five thousand years ago.]","Chavín de Huántar fue un centro religioso hace unos tres mil años. [Chavín de Huántar was a religious centre about three thousand years ago.]","En 1532 los españoles capturaron al Inca Atahualpa. [In 1532 the Spaniards captured the Inca Atahualpa.]","En 1970 un terremoto sacudió Áncash. [In 1970 an earthquake shook Áncash.]"],"solution":[0,1,2,3],"teaches":["preterito-indefinido"]}])
lesson(s,"Peru's Andes: Unit Review","Review the Cordillera Blanca, Caral and Chavín, the Inca empire, Cusco painting and Quechua, with the grammar you used to talk about them.","review: cleft sentences, antes de que, the se passive, stance adverbs, reporting verbs",
 ["I can review what I learned about the Peruvian Andes, from the glaciers to Quechua.","I can use cleft sentences, *antes de que* and *después de que*, the *se* passive, stance adverbs and reporting verbs.","I can put events from five thousand years ago to 1970 in order.","I can say who says what when a matter is disputed."],
 ["I can put one idea in the spotlight with a cleft sentence (*Lo que..., Fue en... cuando...*).","I can order events with *antes de que* and *después de que* and the right mood.","I can say what was built or used with the passive *se*.","I can show my attitude to a fact with stance adverbs.","I can report what experts say with reporting verbs (*señalar*, *afirmar*, *recordar*, *negar*)."])
