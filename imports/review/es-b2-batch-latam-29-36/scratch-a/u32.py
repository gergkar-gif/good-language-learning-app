import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
U='b2-amazon-basin-vocab'
CH={}
# ---- 01 OTCA para que
s='b2-amazoniapan-01'
grammar(s,'grammar.b2.amazoniapan.01.paraque','The Amazon Treaty: What It Is For',
 "You know *para que* + subjunctive from B1 Unit 4: it says the purpose of an action when the second clause has a new subject (*Te llamo para que vengas*). With the same subject you use *para* + infinitive. Treaties and summits exist for a purpose, so this pattern is at home here. Here it works on the Amazon Cooperation Treaty.",
 "Purpose with para que",
 [("Los países crearon una secretaría para que la cooperación fuera permanente.","*para que* + imperfect subjunctive after a past verb"),
  ("Los pueblos indígenas participan en los diálogos para que sus propuestas lleguen a los gobiernos.","*para que* + present subjunctive: a new subject"),
  ("Los gobiernos firmaron el tratado para proteger la cuenca.","same subject: *para* + infinitive"),
  ("Se reúnen cada cierto tiempo para que los acuerdos se cumplan.","*para que* + *se* + subjunctive")],
 "In context",
 [("Los ocho países firmaron el tratado para que la región tuviera una política común.","The eight countries signed the treaty so that the region would have a common policy."),
  ("Los científicos miden la deforestación para que los gobiernos conozcan los datos.","Scientists measure deforestation so that governments know the figures."),
  ("Los países se reúnen para decidir acciones conjuntas.","The countries meet to decide joint actions.")],
 "After *para que* the verb is always subjunctive: present for a present or future purpose, imperfect after a past verb. If the same person does both actions, use *para* + infinitive, never *para que*.")
x=Ex(s)
x.mc("Which sentence says \"The countries created a secretariat so that cooperation would be permanent\"?",
 "Los países crearon una secretaría para que la cooperación fuera permanente.",
 ["Los países crearon una secretaría para que la cooperación es permanente.","Los países crearon una secretaría para la cooperación ser permanente."],2,'subjuntivo-de-finalidad-para-que',
 ds={"Los países crearon una secretaría para que la cooperación es permanente.":'present-tense'})
x.fb("Los pueblos indígenas participan en los diálogos para ____ sus propuestas lleguen a los gobiernos.","que","Indigenous peoples take part in the dialogues so that their proposals reach the governments.",'subjuntivo-de-finalidad-para-que')
x.mt([("el tratado","treaty"),("la cumbre","summit"),("la cuenca","river basin"),("la secretaría","secretariat")],U)
x.read("According to the text, in which year was the Amazon Cooperation Treaty signed?",
 "En 1978.",["En 2023.","En 2025."],1)
ids=x.write()
vocab(s,"The Amazon Treaty and the Belém summit",[("tratado","treaty","noun"),("cumbre","summit","noun"),("cuenca","river basin","noun"),("secretaría","secretariat","noun")])
lesson(s,"The Amazon basin: eight countries and one treaty","I can say what an agreement or a meeting is for with *para que* + subjunctive, about the Amazon Treaty.","recap: purpose with para que + subjunctive and para + infinitive",ids)
n=story(s,"Ocho países, un tratado","Eight countries share the Amazon basin; they signed the Amazon Cooperation Treaty in 1978, met in Belém in 2023, and in 2026 INPE reported the lowest deforestation estimate since 1988.",
["La cuenca amazónica no pertenece a un solo país. Bolivia, Brasil, Colombia, Ecuador, Guyana, Perú, Surinam y Venezuela comparten su territorio, y la Guayana Francesa, que es territorio de Francia, también forma parte de la región. El 3 de julio de 1978 los ocho países firmaron en Brasília el Tratado de Cooperación Amazónica. Más tarde crearon la Organización del Tratado de Cooperación Amazónica, la OTCA, con una secretaría permanente en Brasília, para que la cooperación fuera continua.",
 "En agosto de 2023 los ocho países se reunieron en Belém, en la cuarta cumbre amazónica, y aprobaron la Declaración de Belém. Acordaron, entre otras cosas, cooperar contra la minería ilegal y la deforestación. Antes de la cumbre hubo los Diálogos Amazónicos, en los que participaron pueblos indígenas y otras organizaciones para que sus propuestas llegaran a los gobiernos.",
 "Según el Instituto Nacional de Investigaciones Espaciales de Brasil, el INPE, la deforestación en la Amazonía brasileña entre agosto de 2025 y julio de 2026 fue de 3.335 kilómetros cuadrados según su estimación PRODES, el nivel más bajo desde que empezaron los registros, en 1988.",
 "En noviembre de 2025 Belém fue la sede de la COP30, la conferencia de las Naciones Unidas sobre el cambio climático. El 25 de octubre de 2026 Lula ganó la segunda vuelta de las elecciones presidenciales de Brasil, y asumirá su cuarto mandato el 5 de enero de 2027."],
[("How many countries signed the Amazon Cooperation Treaty in 1978?",["Ocho.","Tres.","Nueve."],0,"The first paragraph says eight."),
 ("Where did the countries meet in August 2023?",["En Belém.","En Manaus.","En Leticia."],0,"The second paragraph says so."),
 ("What did INPE's estimate for August 2025 to July 2026 show?",["El nivel más bajo de deforestación desde 1988.","El nivel más alto desde 1978.","Ninguna deforestación."],0,"The third paragraph says so.")])
print(s,n)
CH[s]=chal("Why a Treaty","You are Meg. You and Carlos are reading about the Amazon Cooperation Treaty, and he asks why the countries created a permanent secretariat.","Tell Carlos that the countries created a secretariat so that cooperation would be permanent.",["Say they created a secretariat","Give the purpose with *para que*"],"Los países crearon una secretaría para que la cooperación fuera permanente.","The countries created a secretariat so that cooperation would be permanent.","I can say what an agreement or a meeting is for with *para que* + subjunctive, about the Amazon Treaty.")

# ---- 02 triple frontier: relativas subjuntivo
s='b2-amazoniapan-02'
grammar(s,'grammar.b2.amazoniapan.02.relativas','Three Countries on One River: Real or Not?',
 "You know *que* + subjunctive for something unknown or non-existent from B2 Unit 13: if the thing is real and you can point at it, *que* takes the indicative; if you are only looking for it, or it does not exist, it takes the subjunctive. At the point where Colombia, Brazil and Peru meet, the border works in surprising ways. Here the pattern works on Leticia and Tabatinga.",
 "Real, or only wanted?",
 [("Leticia y Tabatinga son dos ciudades que forman una zona continua.","a real thing: indicative"),
  ("No hay ninguna valla que separe las dos ciudades.","nothing like that exists: subjunctive"),
  ("Un viajero busca un lugar donde se hablen español y portugués.","only looking for it: subjunctive"),
  ("En el mercado hay personas que hablan los dos idiomas.","real people: indicative")],
 "In context",
 [("Hay una isla que pertenece a Perú.","There is an island that belongs to Peru."),
  ("No hay ningún puente que una las dos orillas en ese punto.","There is no bridge that joins the two banks at that point."),
  ("Necesitamos una escuela que enseñe en los dos idiomas.","We need a school that teaches in both languages.")],
 "Ask one question: can I point at it? If yes, indicative. If it is only wanted, needed or imagined, or if you say it does not exist (*no hay ninguna ... que*), use the subjunctive. Keep the personal *a* before a person: *Busco a alguien que ...*.")
x=Ex(s)
x.mc("Which sentence says \"There is no fence that separates the two cities\"?",
 "No hay ninguna valla que separe las dos ciudades.",
 ["No hay ninguna valla que separa las dos ciudades.","No hay ninguna valla que separar las dos ciudades."],1,'relativas-subjuntivo',
 ds={"No hay ninguna valla que separa las dos ciudades.":'present-tense'})
x.fb("Un viajero busca un lugar donde se ____ español y portugués.","hablen","A traveller is looking for a place where Spanish and Portuguese are spoken.",'relativas-subjuntivo')
x.mt([("la isla","island"),("la valla","fence"),("la orilla","bank, shore"),("la moneda","currency")],U)
x.read("According to the text, which three countries meet at the Amazon tri-border point?",
 "Colombia, Brasil y Perú.",["Brasil, Chile y Perú.","Colombia, Bolivia y Brasil."],0)
ids=x.write()
vocab(s,"Leticia, Tabatinga and the peoples of the border",[("isla","island","noun"),("valla","fence","noun"),("orilla","bank, shore","noun"),("moneda","currency","noun")])
lesson(s,"Peoples and cities on the borders of the Amazon","I can tell a real thing from one that is only wanted or does not exist with *que* + indicative or subjunctive, about the Amazon borders.","recap: relative clauses with indicative or subjunctive",ids)
n=story(s,"Una frontera que se cruza a pie","Colombia, Brazil and Peru meet on the Amazon: Leticia and Tabatinga form one urban area, Ticuna communities live on all three sides, and the Yanomami live across the Brazil-Venezuela border.",
["En el punto donde se encuentran Colombia, Brasil y Perú, la frontera se cruza a pie. Leticia, en Colombia, y Tabatinga, en Brasil, forman una zona urbana continua: no hay ninguna valla que separe las dos ciudades, y la gente pasa de un país a otro por una avenida. Frente a ellas, en el río, está la isla de Santa Rosa, que pertenece a Perú.",
 "Aquí se hablan español y portugués, y las personas cambian de idioma, a veces dentro de una misma frase. En los mercados se usan pesos colombianos, reales brasileños y soles peruanos.",
 "Los ticunas son uno de los pueblos indígenas más numerosos de la Amazonía y viven en Brasil, Colombia y Perú. Muchas comunidades ticunas tienen familiares en los tres países. Una de sus ceremonias más conocidas es la fiesta de la pelazón, que marca el paso de una joven a la vida adulta.",
 "Otro pueblo cuyo territorio está en dos países es el yanomami, en la frontera entre Brasil y Venezuela. Viven en grandes casas colectivas circulares, los shabonos. Su territorio en Brasil se reconoció oficialmente en 1992. En enero de 2023 el gobierno brasileño declaró una emergencia de salud en ese territorio, donde hay minería ilegal de oro."],
[("Which country does the island of Santa Rosa belong to?",["A Perú.","A Colombia.","A Brasil."],0,"The first paragraph says so."),
 ("Which currencies are used in the markets?",["Pesos, reales y soles.","Euros y dólares.","Solo reales."],0,"The second paragraph names them."),
 ("In which year was the Yanomami territory in Brazil officially recognised?",["En 1992.","En 2023.","En 1978."],0,"The fourth paragraph gives the year.")])
print(s,n)
CH[s]=chal("The Open Border","You are Carlos. You and Meg are reading about Leticia and Tabatinga, and she asks whether a fence divides the cities.","Tell Meg that there is no fence that separates the two cities.",["Say there is no fence","Use *que* + subjunctive"],"No hay ninguna valla que separe las dos ciudades.","There is no fence that separates the two cities.","I can tell a real thing from one that is only wanted or does not exist with *que* + indicative or subjunctive, about the Amazon borders.")

# ---- 03 flying rivers: formal cause
s='b2-amazoniapan-03'
grammar(s,'grammar.b2.amazoniapan.03.cause','Flying Rivers: Giving the Cause',
 "You know *debido a* and *a raíz de* from B1 Unit 6: formal ways to give a cause, always followed by a noun (*debido a un error*). Scientific texts explain causes all the time. Here the connectors work on the flying rivers of the Amazon.",
 "Formal causes",
 [("Debido a la transpiración de los árboles, el aire sobre la selva es muy húmedo.","*debido a* + noun: because of the transpiration"),
  ("Debido a los Andes, el aire húmedo se desvía hacia el sur.","*debido a* + noun: because of the Andes"),
  ("A raíz de un artículo de 2018, se habla más del punto de no retorno.","*a raíz de* + noun: as a result of an article"),
  ("Se habla de ríos voladores porque el vapor se mueve en la atmósfera.","*porque* + verb: because the vapour moves")],
 "In context",
 [("Debido a la deforestación, algunos científicos temen menos lluvia.","Because of deforestation, some scientists fear less rain."),
  ("A raíz de los estudios del INPE, se conocen mejor los datos de la selva.","As a result of INPE's studies, the data on the forest are better known."),
  ("Debido a la humedad de la selva, llueve casi todos los días en algunas zonas.","Because of the forest's humidity, it rains almost every day in some areas.")],
 "*Debido a* and *a raíz de* take a noun, never a verb: *debido a la lluvia*, not *debido a que llovió*. With a verb use *porque*. They sound formal, so they suit a report or an article.")
x=Ex(s)
x.mc("Which sentence is correct?",
 "Debido a la lluvia, el aire es muy húmedo.",
 ["Debido a llueve mucho, el aire es muy húmedo.","Debido que la lluvia, el aire es muy húmedo."],0,'formal-cause-connectors')
x.fb("A ____ de un artículo de 2018, se habla más del punto de no retorno.","raíz","As a result of an article of 2018, people talk more about the tipping point.",'formal-cause-connectors')
x.mt([("el vapor","vapour"),("la lluvia","rain"),("la cordillera","mountain range"),("el árbol","tree")],U)
x.read("According to the text, which mountain range makes the humid air turn south?",
 "Los Andes.",["Los Alpes.","Los Pirineos."],2)
ids=x.write()
vocab(s,"Flying rivers and the forest's water",[("vapor","vapour","noun"),("lluvia","rain","noun"),("cordillera","mountain range","noun"),("árbol","tree","noun")])
lesson(s,"Flying rivers: how the forest moves water","I can give a cause in a formal way with *debido a* and *a raíz de*, about the Amazon's water cycle.","recap: formal cause connectors (debido a, a raíz de)",ids)
n=story(s,"Los ríos voladores","Scientists call the water vapour moving over the Amazon flying rivers; trees release it, the Andes redirect it south, and some scientists warn of a tipping point.",
["Los científicos llaman ríos voladores a las masas de vapor de agua que se mueven por la atmósfera sobre la Amazonía. Según una estimación, en la selva amazónica hay unos 390.000 millones de árboles. Los árboles absorben agua por las raíces y la liberan por las hojas: es la transpiración. Según algunos científicos, un árbol grande puede transpirar más de mil litros de agua al día.",
 "Debido a la cordillera de los Andes, el aire húmedo que viene del Atlántico no pasa al otro lado y se desvía hacia el sur. Así, según varios estudios, la humedad de la Amazonía contribuye a las lluvias de regiones como el centro y el sur de Brasil, Paraguay y el norte de Argentina. El investigador brasileño Antonio Nobre ha defendido que los bosques ayudan a atraer la lluvia, la llamada bomba biótica; otros científicos discuten hasta qué punto funciona así.",
 "A raíz de la deforestación, algunos científicos advierten de un posible punto de no retorno. En 2018 los científicos Thomas Lovejoy y Carlos Nobre escribieron que, si se pierde entre el 20 y el 25 % del bosque, la selva podría dejar de recuperarse y convertirse en sabana en algunas zonas. Otros investigadores creen que el límite puede ser distinto, y la cifra exacta se sigue estudiando."],
[("What do scientists call the masses of water vapour over the Amazon?",["Ríos voladores.","Ríos negros.","Mares dulces."],0,"The first paragraph says so."),
 ("Why does the humid air turn south?",["Debido a la cordillera de los Andes.","Debido al río Negro.","Debido al océano Pacífico."],0,"The second paragraph says so."),
 ("Who wrote in 2018 about a possible tipping point?",["Thomas Lovejoy y Carlos Nobre.","Lula y Kubitschek.","Oscar Niemeyer y Lúcio Costa."],0,"The third paragraph names them.")])
print(s,n)
CH[s]=chal("The Andes and the Rain","You are Meg. You and Carlos are watching a talk about the Amazon's water cycle, and he asks why the humid air goes south.","Tell Carlos that, because of the Andes, the humid air turns south.",["Use *debido a* + noun","Say where the air goes"],"Debido a los Andes, el aire húmedo se desvía hacia el sur.","Because of the Andes, the humid air turns south.","I can give a cause in a formal way with *debido a* and *a raíz de*, about the Amazon's water cycle.")

# ---- 04 mercury: modal probability
s='b2-amazoniapan-04'
grammar(s,'grammar.b2.amazoniapan.04.modal','Mining and Mercury: How Sure Are You?',
 "You know *puede* (maybe), *debe de* (probably) and *tiene que* (almost sure) + infinitive from B2 Unit 26, and *haber* + participle for the past. A text about illegal gold mining has to say what is known and what is only likely. Here the guesses work on mercury in the rivers.",
 "From less sure to more sure",
 [("El mercurio puede llegar a los peces del río.","*puede*: it is possible"),
  ("Si los peces tienen mercurio, debe de haber minas cerca.","*debe de*: a good guess from a sign"),
  ("Si los análisis muestran mercurio y no hay fábricas cerca, tiene que venir de la minería.","*tiene que*: almost sure, no other explanation"),
  ("Los peces pueden haber recibido el mercurio de las aguas río arriba.","*puede haber* + participle: a possible cause in the past")],
 "In context",
 [("Un pez que come otros peces puede tener más mercurio.","A fish that eats other fish may have more mercury."),
  ("Debe de haber mucho mercurio en ese tramo del río.","There must be a lot of mercury in that stretch of the river."),
  ("Tiene que ser mercurio: el análisis lo muestra.","It has to be mercury: the analysis shows it.")],
 "*Tiene que ser* is a guess because the verb is *ser* or *estar*. *Tiene que salir* is a need, not a guess. For a guess about the past add *haber* + participle (*debe de haber llegado*). Say who gives the information when you report a figure or a diagnosis.")
x=Ex(s)
x.mc("Which sentence says \"There must be mines nearby\" as a good guess?",
 "Debe de haber minas cerca.",
 ["Debe haber minas cerca de.","Debe de hay minas cerca."],0,'perifrasis-modales-probabilidad-epistemica')
x.fb("Si los peces tienen mercurio, ____ de haber minas cerca.","debe","If the fish have mercury, there must be mines nearby.",'perifrasis-modales-probabilidad-epistemica')
x.mt([("el mercurio","mercury"),("el pez","fish"),("la mina","mine"),("el oro","gold")],U)
x.read("According to the text, what is mercury used for in small-scale gold mining?",
 "Para separar el oro.",["Para limpiar el agua.","Para lavar la ropa."],1)
ids=x.write()
vocab(s,"Gold mining, mercury and fish",[("mercurio","mercury","noun"),("pez","fish","noun"),("mina","mine","noun"),("oro","gold","noun")])
lesson(s,"Illegal mining and mercury in the rivers","I can say how sure I am with *puede*, *debe de* and *tiene que* + infinitive, about mercury in the Amazon rivers.","recap: epistemic modal periphrases (puede, debe de, tiene que + infinitive)",ids)
n=story(s,"El oro y el mercurio en los ríos","Small-scale gold mining uses mercury, which reaches rivers and fish; communities that eat fish are most exposed, and the Belém Declaration of 2023 included cooperation against illegal mining.",
["En muchas zonas de la Amazonía hay minería de oro, y una parte de ella es ilegal. En la minería a pequeña escala se usa mercurio para separar el oro de la arena del río. Parte de ese mercurio llega al agua. Allí, bacterias lo transforman en metilmercurio, una sustancia tóxica que pasa a los peces. Un pez que come otros peces puede tener más mercurio en el cuerpo.",
 "Las personas que comen pescado todos los días están más expuestas. Según varios estudios en comunidades de Brasil, Perú y Colombia, se ha encontrado mercurio en el pelo de habitantes de zonas cercanas a la minería. El mercurio puede dañar el sistema nervioso, sobre todo en los niños pequeños y en el embarazo.",
 "En enero de 2023, Brasil declaró una emergencia de salud en el territorio yanomami, donde hay minería ilegal. La minería se asocia allí con casos de malaria y desnutrición, además de la contaminación de los ríos. La Convención de Minamata, adoptada en 2013, es un tratado internacional para reducir el uso del mercurio.",
 "En la Declaración de Belém de 2023, los países de la cuenca acordaron cooperar contra la minería ilegal. Sin embargo, los gobiernos reconocen que es difícil controlar una zona tan grande y con tantos ríos."],
[("What do bacteria do to mercury in river water?",["Lo transforman en metilmercurio.","Lo convierten en oro.","Lo sacan del agua."],0,"The first paragraph says so."),
 ("Who is more exposed to mercury through fish?",["Las personas que comen pescado todos los días.","Las personas que viven lejos del río.","Los mineros que no comen pescado."],0,"The second paragraph says so."),
 ("What did Brazil declare in the Yanomami territory in January 2023?",["Una emergencia de salud.","Una nueva ciudad.","Un parque de oro."],0,"The third paragraph says so.")])
print(s,n)
CH[s]=chal("Mercury in the River","You are Carlos. You and Meg are reading a report about mercury, and she asks what the presence of mercury in fish suggests.","Tell Meg that if the fish have mercury there must be mines nearby, as a guess.",["Say the fish have mercury","Give your guess with *debe de*"],"Si los peces tienen mercurio, debe de haber minas cerca.","If the fish have mercury, there must be mines nearby.","I can say how sure I am with *puede*, *debe de* and *tiene que* + infinitive, about mercury in the Amazon rivers.")

# ---- 05 bioeconomy: mixed conditionals
s='b2-amazoniapan-05'
grammar(s,'grammar.b2.amazoniapan.05.mixed','A Standing Forest: If the Past Had Been Different',
 "You know *si hubiera* + participle with the simple conditional from B2 Unit 11 (the mixed conditional): *si hubiera* + participle for a past that did not happen, with the simple conditional for a result in the present (*Si hubiera estudiado, ahora sería médica*). It is the natural tool for \"if we had ..., today there would be ...\". Here it works on the Amazon and its standing-forest economy.",
 "A past cause, a present result",
 [("Si no se hubieran talado tantos árboles en el siglo XX, hoy habría más bosque.","*si hubieran talado* ... *habría*: a different past, a different present"),
  ("Si hubiera visitado Belém en octubre, ahora recordaría la procesión.","an imagined past visit, a present memory"),
  ("Si hubiéramos protegido antes la selva, hoy tendríamos más árboles.","*hubiéramos protegido* ... *tendríamos*"),
  ("Si los exploradores no hubieran conocido la quina, hoy sabríamos menos sobre ese árbol.","a past event, a present result")],
 "In context",
 [("Si el caucho no se hubiera producido en Asia, hoy Manaus quizá tendría otra economía.","If rubber had not been produced in Asia, Manaus might have a different economy today."),
  ("Si hubieras comprado castañas en Belém, ahora tendrías un buen recuerdo.","If you had bought nuts in Belém, you would have a good souvenir now."),
  ("Si no hubiera existido la minería, los ríos estarían hoy más limpios.","If mining had not existed, the rivers would be cleaner today.")],
 "Look at the result: a word such as *hoy* or *ahora* means the simple conditional (*habría* + participle is for a past result). In the *si* clause *habría* never appears: *si hubiera estudiado*, not *si habría estudiado*. These are imagined situations, not facts.")
x=Ex(s)
x.mc("Which sentence says \"If we had protected the forest earlier, we would have more trees today\"?",
 "Si hubiéramos protegido antes la selva, hoy tendríamos más árboles.",
 ["Si habríamos protegido antes la selva, hoy tendríamos más árboles.","Si hubiéramos protegido antes la selva, hoy habríamos tenido más árboles."],1,'mixed-conditionals')
x.fb("Si no se hubieran talado tantos árboles, hoy ____ más bosque.","habría","If so many trees had not been cut down, there would be more forest today.",'mixed-conditionals')
x.mt([("la castaña","Brazil nut"),("el açaí","açaí berry"),("la quina","cinchona tree"),("el bosque","forest")],U)
x.read("According to the text, which medicine comes from the bark of the cinchona tree?",
 "La quinina.",["El curare.","La aspirina."],0)
ids=x.write()
vocab(s,"Standing forest: nuts, açaí and medicine",[("castaña","Brazil nut","noun"),("açaí","açaí berry","noun"),("quina","cinchona tree","noun"),("bosque","forest","noun")])
lesson(s,"The standing forest: products, medicines and fair sharing","I can say how a different past would change the present with *si hubiera* + participle and the conditional, about the Amazon.","recap: mixed conditionals (si + pluperfect subjunctive, simple conditional)",ids)
n=story(s,"El bosque en pie","The idea of a bioeconomy of the standing forest: products such as açaí and Brazil nuts, medicines such as curare and quinine, and the Nagoya Protocol on sharing the benefits of genetic resources.",
["Durante mucho tiempo se pensó que la riqueza de la selva estaba en sus árboles cortados o en la tierra para ganado. Hoy muchas personas hablan de una bioeconomía del bosque en pie: productos que se obtienen sin talar el bosque. Algunos ejemplos son el açaí, el cacao silvestre y la castaña de Pará, que se recoge de árboles que crecen en la selva. Muchas familias de recolectores los venden en cooperativas.",
 "La selva ha sido también una fuente de medicinas. El curare, que los pueblos indígenas usaban en sus flechas, dio origen a medicamentos que se emplean en la anestesia. De la corteza de la quina, un árbol de los bosques andinos, se obtuvo la quinina, que durante siglos se usó contra la malaria. Si las poblaciones indígenas no hubieran conservado estos saberes, hoy sabríamos mucho menos sobre esas plantas.",
 "Hay también un debate sobre quién se beneficia. Algunas empresas han patentado productos basados en conocimientos tradicionales, sin pedir permiso a los pueblos que los desarrollaron. Esa práctica se llama biopiratería, según sus críticos. El Protocolo de Nagoya, de 2010, establece reglas para que los beneficios de los recursos genéticos se compartan de forma justa con los países y comunidades de origen.",
 "Si no se hubieran talado tantos árboles en el siglo XX, hoy habría más bosque. Por eso muchos investigadores y organizaciones defienden que el bosque en pie tenga valor económico, aunque no hay acuerdo sobre cuál es el mejor modelo."],
[("What is the Brazil nut collected from, according to the text?",["De árboles que crecen en la selva.","De plantaciones de Asia.","De cultivos de soja."],0,"The first paragraph says so."),
 ("What was obtained from the bark of the cinchona tree?",["La quinina.","El curare.","El açaí."],0,"The second paragraph says so."),
 ("What does the Nagoya Protocol set rules for?",["Compartir de forma justa los beneficios de los recursos genéticos.","Construir puentes entre países.","Cortar árboles con permiso."],0,"The third paragraph says so.")])
print(s,n)
CH[s]=chal("A Different Past","You are Meg. You and Carlos are reading about the standing forest, and he asks what difference less logging would have made.","Tell Carlos that if fewer trees had been cut down in the last century there would be more forest today.",["Use *si hubiera* + participle","Say what there would be today"],"Si no se hubieran talado tantos árboles en el siglo XX, hoy habría más bosque.","If so many trees had not been cut down in the 20th century, there would be more forest today.","I can say how a different past would change the present with *si hubiera* + participle and the conditional, about the Amazon.")

# ---- consolidation
s='b2-amazoniapan-consolidation'
x=Ex(s)
x.mc("Which sentence says \"There is no fence that separates the two cities\"?",
 "No hay ninguna valla que separe las dos ciudades.",
 ["No hay ninguna valla que separa las dos ciudades.","No hay ninguna valla que separar las dos ciudades."],2,'relativas-subjuntivo',
 ds={"No hay ninguna valla que separa las dos ciudades.":'present-tense'})
x.mc("Which sentence gives the cause in a formal way?",
 "Debido a los Andes, el aire húmedo se desvía hacia el sur.",
 ["Debido a se desvía el aire húmedo, llueve hacia el sur.","Debido que los Andes, el aire húmedo se desvía hacia el sur."],0,'formal-cause-connectors')
x.fb("Si no hubiéramos talado tantos árboles, hoy ____ más bosque.","habría","If we had not cut down so many trees, there would be more forest today.",'mixed-conditionals')
x.read("According to the texts, in which year did the eight countries sign the Amazon Cooperation Treaty?",
 "En 1978.",["En 2023.","En 1992."],2)
ids=x.write()
consolidation2(s,"Review: the Amazon basin, from treaty to standing forest","Review the Amazon Treaty, the three-border area, the flying rivers, mercury and the standing forest, with the grammar you used to talk about them.","review: para que, relative clauses with subjunctive, formal causes, modal guesses, mixed conditionals",ids)
CH[s]=chal("The Amazon in Review","You are Carlos. You and Meg are preparing a short talk about the Amazon basin, and she asks you to describe the border between the two cities.","Tell Meg that there is no fence that separates Leticia and Tabatinga.",["Say there is no fence","Use *que* + subjunctive"],"No hay ninguna valla que separe Leticia y Tabatinga.","There is no fence that separates Leticia and Tabatinga.","I can review what I learned about the Amazon basin, from the treaty to the standing forest.")
challenges(ROOT+'/challenges-amazon-basin.json',CH)
