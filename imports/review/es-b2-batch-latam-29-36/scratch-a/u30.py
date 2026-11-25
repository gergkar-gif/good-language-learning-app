import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
U='b2-brazil-northeast-vocab'
CH={}
# ---------- 01 contrast markers
s='b2-brasilnordeste-01'
grammar(s,'grammar.b2.brasilnordeste.01.contrast','Salvador: Setting One Idea Against Another',
 "You know *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien* from B2 Unit 30. Each sets one idea against another in its own way. Salvador is a good place to use them, because its history has a bright side and a hard side. Here they work on Salvador de Bahía.",
 "Five markers, five jobs in Salvador",
 [("El puerto era un centro del azúcar; en cambio, el interior estaba menos poblado.","*en cambio* compares two things and finds them different"),
  ("El Pelourinho no es solo un barrio turístico; por el contrario, es memoria de la esclavitud.","*por el contrario* gives the opposite of what was said"),
  ("—¿Es una ciudad nueva? —Al contrario, se fundó en 1549.","*al contrario* is the short answer in conversation"),
  ("Fue restaurado en los años noventa; no obstante, muchos vecinos tuvieron que mudarse.","*no obstante* admits a fact and goes on in spite of it"),
  ("El centro histórico es hermoso. Ahora bien, necesita mantenimiento constante.","*ahora bien* adds a point that limits what you accepted")],
 "In context",
 [("La Ciudad Baja es el puerto; la Ciudad Alta, en cambio, está sobre el acantilado.","The Lower City is the port; the Upper City, on the other hand, stands on the cliff."),
  ("Salvador no es una ciudad sin raíces africanas; al contrario, tiene muchas.","Salvador is not a city without African roots; on the contrary, it has many."),
  ("El Pelourinho se restauró; no obstante, hubo críticas por la salida de vecinos.","The Pelourinho was restored; nevertheless, there was criticism about residents leaving.")],
 "*Pero* is still the everyday word and takes no comma after it. These markers usually start a new clause after a full stop or a semicolon, with a comma after them. Choose by the kind of contrast: a comparison (*en cambio*), the opposite (*por el contrario*, *al contrario*), a fact that does not stop you (*no obstante*) or a limit (*ahora bien*).")
x=Ex(s)
x.mc("Which sentence compares two parts of Salvador?",
 "La Ciudad Baja es el puerto; en cambio, la Ciudad Alta está sobre el acantilado.",
 ["La Ciudad Baja es el puerto; por el contrario, la Ciudad Alta está sobre el acantilado.","La Ciudad Baja es el puerto; ahora bien, la Ciudad Alta está sobre el acantilado."],2,'contrast-markers')
x.fb("Salvador no es una ciudad nueva; al ____, se fundó en 1549.","contrario","Salvador is not a new city; on the contrary, it was founded in 1549.",'contrast-markers')
x.mt([("el puerto","port"),("el azúcar","sugar"),("el acantilado","cliff"),("el esclavizado","enslaved person")],U)
x.sb("El centro se restauró; no obstante, hubo críticas.","The centre was restored; nevertheless, there was criticism.",'contrast-markers')
x.fb("Los turistas visitan hoy el Pelourinho. Su nombre recuerda la ____ de piedra donde se castigaba a las personas.","columna","Tourists visit the Pelourinho today. Its name recalls the stone column where people were punished.",U,cat='vocabulary')
x.read("According to the text, in which year did UNESCO declare the historic centre of Salvador a World Heritage Site?",
 "En 1985.",["En 1549.","En 1873."],0)
ids=x.write()
vocab(s,"Salvador: port, sugar and the Pelourinho",[("puerto","port","noun"),("azúcar","sugar","noun"),("acantilado","cliff","noun"),("esclavizado","enslaved person","noun"),("columna","column","noun")])
lesson(s,"Salvador de Bahía: a colonial capital and its African heritage","I can set one idea about Salvador against another with *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien*.","recap: contrast markers (en cambio, por el contrario, al contrario, no obstante, ahora bien)",ids)
n=story(s,"Salvador, la primera capital","Salvador was founded in 1549, was Brazil's first capital, grew on sugar and slavery, and today has a large Afro-Brazilian population and a UNESCO historic centre.",
["Salvador de Bahía se fundó en 1549, por orden del rey Juan III de Portugal, y su primer gobernador general fue Tomé de Sousa. Fue la primera capital de Brasil y lo siguió siendo hasta 1763. La ciudad tiene dos niveles: la Ciudad Baja, junto al puerto, y la Ciudad Alta, sobre un acantilado. Desde 1873 las comunica el Elevador Lacerda.",
 "Durante siglos, Salvador fue un puerto del azúcar y de la trata de personas esclavizadas. Las plantaciones de caña del Recôncavo, la región que rodea la bahía, enviaban azúcar a Europa, y los trabajadores eran africanos esclavizados. El centro histórico se llama Pelourinho, un nombre que recuerda la columna de piedra donde se castigaba a los esclavizados. Allí hay casas coloniales de colores y la iglesia de San Francisco, con el interior cubierto de madera dorada. La Unesco declaró Patrimonio Mundial el centro histórico en 1985.",
 "Hoy Salvador es una de las grandes ciudades brasileñas de población afrodescendiente: según los censos del IBGE, la mayoría de sus habitantes se declara negra o parda. Muchos bahianos descienden de personas llevadas desde regiones como Angola, el Golfo de Benín y la actual Nigeria; a veces se llama a la ciudad la Roma Negra. En las calles se venden acarajés, una fritura que las bahianas preparan con aceite de dendê.",
 "En el Pelourinho nació en 1979 el grupo de percusión Olodum, que mezcla la samba con el reggae en el estilo llamado samba-reggae y tiene también proyectos educativos para jóvenes. Desde los años noventa se restauró el barrio. No obstante, según varios estudios, muchos vecinos tuvieron que mudarse. Los turistas ven hoy un barrio de música y de fiestas; en cambio, para muchas personas de la ciudad sigue siendo también la memoria de la esclavitud."],
[("What was Tomé de Sousa in Salvador?",["El primer gobernador general.","El rey de Portugal.","El primer músico de Olodum."],0,"The first paragraph says so."),
 ("What does the name Pelourinho recall?",["La columna de piedra donde se castigaba a los esclavizados.","Una iglesia con el interior de madera dorada.","Un grupo de percusión."],0,"The second paragraph explains it."),
 ("When did the group Olodum start?",["En 1979.","En 1985.","En 1873."],0,"The fourth paragraph gives the year.")])
print(s,n)
CH[s]=chal("Two Sides of Salvador","You are Meg. You and Carlos are watching a documentary about Salvador, and he says the old port was mostly in the high part of the city.","Correct Carlos: the Lower City is the port, and the Upper City is on the cliff, as a comparison.",["Say that the Lower City is the port","Compare it with the Upper City"],"La Ciudad Baja es el puerto; la Ciudad Alta, en cambio, está sobre el acantilado.","The Lower City is the port; the Upper City, on the other hand, is on the cliff.","I can set one idea about Salvador against another with *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien*.")

# ---------- 02 para que
s='b2-brasilnordeste-02'
grammar(s,'grammar.b2.brasilnordeste.02.paraque','Candomblé and Capoeira: Saying What It Is For',
 "You know *para que* + subjunctive from B1 Unit 4: it says the purpose of an action, with a new subject in the second clause (*Te llamo para que vengas*). When the subject stays the same, you know *para* + infinitive. Purposes are everywhere in Bahian culture: why a drum is played, why a game was disguised. Here the structure works on Candomblé and capoeira.",
 "Purpose with para que",
 [("Se tocan los atabaques para que el orixá llegue al terreiro.","*para que* + present subjunctive: the drums are for the orixá to arrive"),
  ("Los esclavizados practicaban la capoeira como baile para que los capataces no la prohibieran.","*para que* + imperfect subjunctive after a past verb"),
  ("Hoy se enseña capoeira para que los jóvenes conozcan esta historia.","a new subject: the young people"),
  ("Los maestros enseñan capoeira para transmitir esta tradición.","same subject: *para* + infinitive, no *que*")],
 "In context",
 [("Los devotos llevan ofrendas para que la fiesta salga bien.","The devotees bring offerings so that the festival goes well."),
  ("El maestro toca el berimbau para que los jugadores empiecen.","The master plays the berimbau so that the players start."),
  ("Se escondía la lucha bajo el baile para que nadie sospechara.","The fight was hidden under the dance so that nobody would suspect.")],
 "After *para que*, the verb is always subjunctive: present for a present or future purpose, imperfect after a past verb (*para que no la prohibieran*). If the same person does both actions, use *para* + infinitive, not *para que*.")
x=Ex(s)
x.mc("Which sentence says \"The drums are played so that the orixá comes\"?",
 "Se tocan los tambores para que el orixá venga.",
 ["Se tocan los tambores para que el orixá viene.","Se tocan los tambores para el orixá venir."],0,'subjuntivo-de-finalidad-para-que',
 ds={"Se tocan los tambores para que el orixá viene.":'present-tense'})
x.fb("El maestro enseña capoeira para ____ los jóvenes conozcan la historia.","que","The master teaches capoeira so that young people know the history.",'subjuntivo-de-finalidad-para-que')
x.mt([("el tambor","drum"),("el orixá","orixá, Candomblé deity"),("el capataz","overseer"),("la roda","capoeira circle")],U)
x.sb("Se escondía la lucha bajo el baile para que nadie sospechara.","The fight was hidden under the dance so that nobody would suspect.",'subjuntivo-de-finalidad-para-que')
x.fb("En la capoeira, los jugadores forman una ____ y juegan en el centro.","roda","In capoeira, the players form a circle and play in the middle.",U,cat='vocabulary')
x.read("According to the text, in which year did UNESCO add the capoeira circle to its list of intangible cultural heritage?",
 "En 2014.",["En 1888.","En 1932."],0)
ids=x.write()
vocab(s,"Candomblé and capoeira in Bahia",[("tambor","drum","noun"),("orixá","orixá, Candomblé deity","noun"),("capataz","overseer","noun"),("roda","capoeira circle","noun")])
lesson(s,"Candomblé and capoeira: Afro-Brazilian traditions of Bahia","I can say what something is for with *para que* + subjunctive, about Candomblé and capoeira.","recap: purpose with para que + subjunctive and para + infinitive",ids)
n=story(s,"Candomblé y capoeira","Candomblé and capoeira came from the African peoples brought to Bahia; both survived persecution, and capoeira's circle entered UNESCO's list in 2014.",
["El Candomblé es una religión afrobrasileña que se formó en Bahía con tradiciones de pueblos africanos como los yorubas, los fon y los bantúes. Sus divinidades se llaman orixás. Las ceremonias se hacen en los terreiros, los templos de la religión, como Casa Branca, Gantois e Ilê Axé Opô Afonjá. Según la tradición, se tocan los atabaques para que el orixá llegue al terreiro, y los iniciados bailan con los gestos de ese orixá.",
 "Durante mucho tiempo la policía persiguió los terreiros. Para protegerse, los devotos asociaron cada orixá con un santo católico: Oxalá, por ejemplo, con el Señor del Bonfim. Se habla de sincretismo religioso. Cada 2 de febrero, en la playa de Río Vermelho, en Salvador, mucha gente lleva flores y regalos a Iemanjá, la señora del mar. Una de las sacerdotisas más conocidas fue Mãe Menininha do Gantois, que dirigió el terreiro de Gantois durante décadas.",
 "La capoeira es una lucha que parece un baile, con música de berimbau y cantos. Los jugadores forman una roda, un círculo, y juegan en el centro. Se desarrolló entre africanos esclavizados y sus descendientes. Según la explicación más extendida, se practicaba como un baile para que los capataces no la prohibieran. A fines del siglo XIX el código penal brasileño la castigó. En los años treinta Mestre Bimba abrió en Salvador una escuela de capoeira, y Mestre Pastinha defendió otra tradición, la capoeira de Angola.",
 "En 2014 la Unesco incluyó la roda de capoeira en su lista del patrimonio cultural inmaterial de la humanidad. Hoy la capoeira se enseña en Brasil y en muchos otros países."],
[("Where are Candomblé ceremonies held?",["En los terreiros.","En la roda.","En el Elevador Lacerda."],0,"The first paragraph says so."),
 ("Why did devotees link each orixá with a Catholic saint?",["Para protegerse de la persecución.","Para abrir una escuela de capoeira.","Para tocar el berimbau."],0,"The second paragraph says they did it to protect themselves."),
 ("What happened to capoeira in 2014?",["La Unesco incluyó la roda en su lista del patrimonio inmaterial.","La policía la prohibió.","Mestre Bimba abrió una escuela."],0,"The fourth paragraph says so.")])
print(s,n)
CH[s]=chal("What the Drums Are For","You are Carlos. You and Meg are watching a documentary about Candomblé, and she asks why the drums are played in the ceremony.","Tell Meg, as the tradition says, that the drums are played so that the orixá arrives.",["Say that the drums are played","Give the purpose with *para que*"],"Según la tradición, se tocan los atabaques para que el orixá llegue al terreiro.","According to the tradition, the drums are played so that the orixá arrives at the terreiro.","I can say what something is for with *para que* + subjunctive, about Candomblé and capoeira.")

# ---------- 03 pluscuamperfecto subj si
s='b2-brasilnordeste-03'
grammar(s,'grammar.b2.brasilnordeste.03.sihubiera','The Sertão: What Would Have Happened If...',
 "You know *si* + *hubiera* + past participle, with *habría* + past participle in the result, from B1 Unit 35: it talks about a past that did not happen. In the sertão, a dry region of the Northeast, it is natural to ask what would have changed with more rain or a different history. Here the pattern works on the sertão, the cangaço and cordel.",
 "If it had..., it would have...",
 [("Si hubiera llovido más, muchas familias no habrían salido del sertão.","*si hubiera llovido* + *habrían salido*: if it had rained more, they would not have left"),
  ("Si los campesinos hubieran tenido tierra, habrían vivido mejor.","*hubieran tenido* ... *habrían vivido*: if they had had land"),
  ("Si no hubiera existido el cordel, muchas historias no habrían llegado a las ferias.","negative condition with *no hubiera existido*"),
  ("Si hubiera podido, el poeta habría impreso más folletos.","the same pattern in the singular")],
 "In context",
 [("Si hubiéramos visitado el sertão en junio, habríamos oído forró.","If we had visited the sertão in June, we would have heard forró."),
  ("Si la sequía hubiera terminado antes, la gente no habría emigrado.","If the drought had ended earlier, people would not have emigrated."),
  ("Si hubieras comprado un folleto, habrías leído esa historia.","If you had bought a leaflet, you would have read that story.")],
 "Both parts use *haber*: *hubiera* in the *si* clause, *habría* in the result. Never *si habría*. The pattern is for a past that did not happen, so these sentences are guesses about what could have been, not facts.")
x=Ex(s)
x.mc("Which sentence says \"If it had rained more, those families would not have left\"?",
 "Si hubiera llovido más, esas familias no se habrían ido.",
 ["Si habría llovido más, esas familias no se habrían ido.","Si hubiera llovido más, esas familias no se irían."],1,'pluscuamperfecto-subjuntivo-si',
 ds={"Si hubiera llovido más, esas familias no se irían.":'si-clauses'})
x.fb("Si la sequía ____ terminado antes, la gente no habría emigrado.","hubiera","If the drought had ended earlier, people would not have emigrated.",'pluscuamperfecto-subjuntivo-si')
x.mt([("la sequía","drought"),("el campesino","peasant, farmer"),("el folleto","leaflet, pamphlet"),("el cordel","string (literatura de cordel)")],U)
x.sb("Si hubieras comprado un folleto, habrías leído esa historia.","If you had bought a leaflet, you would have read that story.",'pluscuamperfecto-subjuntivo-si')
x.fb("En el sertão, muchas familias emigraron durante la ____ porque no había agua.","sequía","In the sertão, many families emigrated during the drought because there was no water.",U,cat='vocabulary')
x.read("According to the text, in which year did Lampião die?",
 "En 1938.",["En 1930.","En 1877."],1)
ids=x.write()
vocab(s,"The sertão, the cangaço and cordel",[("sequía","drought","noun"),("campesino","peasant, farmer","noun"),("folleto","leaflet, pamphlet","noun"),("cordel","string (literatura de cordel)","noun")])
lesson(s,"The sertão: drought, outlaws and cordel poetry","I can say what would have happened in a different past with *si hubiera* + participle and *habría* + participle, about the sertão.","recap: past hypotheticals with si + pluperfect subjunctive and the conditional perfect",ids)
n=story(s,"El sertão: sequía, cangaço y cordel","The sertão is a dry region where droughts forced people to emigrate; the cangaço produced Lampião, and cordel poetry and woodcuts tell its stories.",
["El sertão es la región semiárida del interior del Nordeste brasileño. Su vegetación típica es la caatinga, palabra de origen tupí que significa más o menos bosque blanco, porque muchos árboles pierden las hojas en la estación seca. Cuando la lluvia falta durante años, hay sequías graves. En una de ellas, entre 1877 y 1879, murieron muchas personas, y desde entonces miles de familias han salido del sertão hacia las ciudades. Si hubiera llovido más, muchas de esas familias no habrían emigrado.",
 "En el interior del Nordeste, entre fines del siglo XIX y 1938, hubo grupos armados llamados cangaceiros. El más famoso fue el de Virgulino Ferreira da Silva, conocido como Lampião, nacido en Pernambuco. Según la tradición, el apodo viene de la luz de sus disparos. Maria Bonita se unió al grupo hacia 1930 y, según se cuenta, fue la primera mujer en hacerlo. Lampião murió en 1938, en Sergipe, en un ataque de la policía. Para algunas personas fue un bandido; para otras, un vengador de los pobres.",
 "La literatura de cordel es una poesía popular que se vende en folletos baratos. Su nombre viene de los cordeles de donde se colgaban los folletos en las ferias. Los poetas contaban en versos rimados las aventuras de los cangaceiros, historias religiosas y noticias. Las portadas suelen llevar xilografías, grabados en madera; un artista muy conocido es J. Borges, que vive en Bezerros, Pernambuco.",
 "La música del sertão es el forró y el baião, con acordeón, triángulo y bombo. El cantante Luiz Gonzaga, nacido en Pernambuco, fue llamado el Rey del Baião. Una de sus canciones más famosas, Asa Branca, habla de la sequía y de la gente que se va. En el sertão ocurrió también la guerra de Canudos, de 1896 y 1897, en el estado de Bahía."],
[("What does the word caatinga mean, according to the text?",["Más o menos bosque blanco.","Río de agua dulce.","Campo de caña de azúcar."],0,"The first paragraph explains it."),
 ("When did Lampião die?",["En 1938.","En 1930.","En 1877."],0,"The second paragraph gives the year."),
 ("Where does the name cordel come from?",["De los cordeles donde se colgaban los folletos.","De una danza de la ciudad de Salvador.","Del nombre de un cangaceiro."],0,"The third paragraph says so.")])
print(s,n)
CH[s]=chal("The Drought","You are Meg. You and Carlos are reading about the sertão, and he asks why so many families left it.","Tell Carlos, as a guess about the past, that if it had rained more many families would not have left.",["Use *si hubiera* + participle","Say what would not have happened"],"Si hubiera llovido más, muchas familias no habrían salido del sertão.","If it had rained more, many families would not have left the sertão.","I can say what would have happened in a different past with *si hubiera* + participle and *habría* + participle, about the sertão.")

# ---------- 04 volver a
s='b2-brasilnordeste-04'
grammar(s,'grammar.b2.brasilnordeste.04.volver','Palmares and Zumbi: Doing It Again',
 "You know *volver a* + infinitive from B2 Unit 23: it means \"to do again\" and works in every tense, and with *no* it means \"not ... again\". The history of Palmares is a history of repeated events: expeditions that came back, a date remembered every year. Here *volver a* works on Palmares and Zumbi.",
 "volver a + infinitive",
 [("Las autoridades volvieron a enviar tropas contra el quilombo.","preterite: they sent troops again"),
  ("Los habitantes del quilombo volvían a levantar sus casas.","imperfect: they used to rebuild their houses again"),
  ("Cada 20 de noviembre se vuelve a recordar a Zumbi.","present: it is remembered again each year"),
  ("Zumbi no volvió a aceptar la propuesta de paz.","with *no*: he did not accept it again")],
 "In context",
 [("El ejército volvió a atacar el quilombo en 1694.","The army attacked the quilombo again in 1694."),
  ("Los fugitivos volvían a formar nuevas aldeas.","The fugitives formed new villages again."),
  ("Brasil no ha vuelto a vivir la esclavitud legal desde 1888.","Brazil has not had legal slavery again since 1888.")],
 "Do not confuse *volver a* + infinitive with *volver a* + place, which means \"to go back to\": *Zumbi volvió a Palmares* is not \"he did it again\". Object pronouns go before *volver* or at the end of the infinitive: *Lo volvieron a atacar* = *Volvieron a atacarlo*.")
x=Ex(s)
x.mc("Which sentence says \"The army attacked the quilombo again\"?",
 "El ejército volvió a atacar el quilombo.",
 ["El ejército volvió atacar el quilombo.","El ejército volvió a atacado el quilombo."],0,'volver-a-infinitivo')
x.fb("Zumbi no ____ a aceptar la propuesta de paz.","volvió","Zumbi did not accept the peace proposal again.",'volver-a-infinitivo')
x.mt([("el quilombo","quilombo, settlement of escaped slaves"),("la tropa","troops"),("el fugitivo","fugitive"),("la esclavitud","slavery")],U)
x.sb("Los fugitivos volvían a formar nuevas aldeas.","The fugitives formed new villages again.",'volver-a-infinitivo')
x.fb("Las personas que se iban de las plantaciones sin permiso eran ____.","fugitivos","The people who left the plantations without permission were fugitives.",U,cat='vocabulary')
x.read("According to the text, when was Zumbi killed?",
 "El 20 de noviembre de 1695.",["El 13 de mayo de 1888.","El 20 de noviembre de 1678."],1)
ids=x.write()
vocab(s,"Palmares, Zumbi and the end of slavery",[("quilombo","quilombo, settlement of escaped slaves","noun"),("tropa","troops","noun"),("fugitivo","fugitive","noun"),("esclavitud","slavery","noun")])
lesson(s,"Palmares and Zumbi: a community of escaped slaves","I can say that something happened again with *volver a* + infinitive, about Palmares and Zumbi.","recap: volver a + infinitive (doing something again)",ids)
n=story(s,"Palmares y Zumbi","Palmares was a large community of escaped slaves in the 17th century; Zumbi became its leader and was killed in 1695; 20 November is remembered as the Day of Black Consciousness.",
["En el siglo XVII, en las sierras del interior del Nordeste, hoy en el estado de Alagoas, existió el Quilombo dos Palmares. Un quilombo era un asentamiento de personas que habían escapado de la esclavitud. Palmares fue una unión de varias aldeas, entre ellas la llamada Macaco. Según algunas estimaciones, llegó a tener miles de habitantes. Allí vivían africanos y sus descendientes, y también otras personas que buscaban refugio. Cultivaban maíz, mandioca y otros productos.",
 "Para las autoridades coloniales, Palmares era una amenaza para el sistema esclavista. Varias expediciones militares atacaron el quilombo, y los habitantes volvían a levantar sus aldeas. En 1678 su jefe, Ganga Zumba, aceptó una propuesta de paz de las autoridades de Pernambuco. Según esa propuesta, serían libres los nacidos en Palmares. Zumbi, un joven jefe militar, la rechazó, y no volvió a aceptar ningún acuerdo parecido.",
 "En 1694 las tropas dirigidas por el bandeirante Domingos Jorge Velho, de São Paulo, tomaron el principal centro del quilombo. Zumbi escapó, pero fue localizado y murió el 20 de noviembre de 1695. Hoy su historia se estudia en Brasil como un símbolo de la resistencia a la esclavitud. Sobre los detalles de la vida de Palmares los historiadores no están de acuerdo, porque muchas fuentes vienen de los enemigos del quilombo.",
 "La esclavitud terminó en Brasil en 1888, con la Lei Áurea; fue el último país de América en abolirla. Desde 2003 una ley incluyó el 20 de noviembre en el calendario escolar como Día de la Conciencia Negra, y desde 2024 es feriado nacional, según una ley de 2023. Cada año se vuelve a recordar esa fecha con actos y debates."],
[("In which state is the Serra da Barriga, where Palmares was, today?",["Alagoas.","São Paulo.","Bahía."],0,"The first paragraph names the state."),
 ("Who rejected the peace proposal of 1678?",["Zumbi.","Ganga Zumba.","Domingos Jorge Velho."],0,"The second paragraph says Zumbi rejected it."),
 ("Since when is 20 November a national holiday in Brazil?",["Desde 2024.","Desde 1888.","Desde 1695."],0,"The fourth paragraph gives the year.")])
print(s,n)
CH[s]=chal("Remembering Zumbi","You are Carlos. You and Meg are reading about Palmares, and she asks what happened after the first expeditions.","Tell Meg that the army attacked the quilombo again in 1694.",["Say that the army attacked","Use *volver a* to say it happened again, with the year"],"El ejército volvió a atacar el quilombo en 1694.","The army attacked the quilombo again in 1694.","I can say that something happened again with *volver a* + infinitive, about Palmares and Zumbi.")

# ---------- 05 formal cause
s='b2-brasilnordeste-05'
grammar(s,'grammar.b2.brasilnordeste.05.cause','Race and Equality: Giving the Cause',
 "You know *debido a* and *a raíz de* from B1 Unit 6: formal ways to give a cause, always followed by a noun (*debido a un error*). A text about racial inequality in Brazil explains causes and results all the time, in a calm, formal tone. Here the connectors work on that topic.",
 "Formal causes",
 [("Debido a la falta de tierras, muchos libertos tuvieron pocas oportunidades.","*debido a* + noun: because of the lack of land"),
  ("A raíz de la ley de 2012, las universidades federales reservan plazas.","*a raíz de* + noun: as a result of the law"),
  ("Hubo debates porque la ley cambió el acceso a la universidad.","*porque* + verb: because the law changed access"),
  ("Los estudios mostraron desigualdades; por eso se crearon nuevas políticas.","*por eso* introduces the consequence")],
 "In context",
 [("Debido a la abolición de 1888, millones de personas dejaron de ser esclavizadas.","Because of the abolition of 1888, millions of people stopped being enslaved."),
  ("A raíz de los estudios de Florestan Fernandes, cambió la imagen de Brasil.","As a result of Florestan Fernandes's studies, the image of Brazil changed."),
  ("Debido a la ley, más estudiantes negros e indígenas entraron a la universidad.","Because of the law, more Black and Indigenous students entered university.")],
 "*Debido a* and *a raíz de* take a noun, never a verb: *debido a la ley*, not *debido a que se aprobó*. With a verb use *porque*. They sound formal, so they suit a report or an article more than a chat.")
x=Ex(s)
x.mc("Which sentence is correct?",
 "Debido a la ley, más estudiantes entraron a la universidad.",
 ["Debido a se aprobó la ley, más estudiantes entraron a la universidad.","Debido que la ley, más estudiantes entraron a la universidad."],1,'formal-cause-connectors')
x.fb("A ____ de la ley de 2012, las universidades federales reservan plazas.","raíz","As a result of the 2012 law, federal universities reserve places.",'formal-cause-connectors')
x.mt([("la ley","law"),("la plaza","place, seat (at a university)"),("la desigualdad","inequality"),("el liberto","freed person")],U)
x.sb("Debido a la abolición de 1888, millones de personas dejaron de ser esclavizadas.","Because of the abolition of 1888, millions of people stopped being enslaved.",'formal-cause-connectors')
x.fb("Las universidades reservan una parte de sus ____ para estudiantes de escuelas públicas.","plazas","Universities reserve part of their places for students from public schools.",U,cat='vocabulary')
x.read("According to the text, who wrote the book Casa-Grande & Senzala?",
 "Gilberto Freyre.",["Florestan Fernandes.","Abdias do Nascimento."],2)
ids=x.write()
vocab(s,"Race, equality and quotas",[("ley","law","noun"),("plaza","place, seat (at a university)","noun"),("desigualdad","inequality","noun"),("liberto","freed person","noun")])
lesson(s,"Race and inequality in Brazil: a debate that changed","I can explain a cause in a formal way with *debido a* and *a raíz de*, about race and equality in Brazil.","recap: formal cause connectors (debido a, a raíz de)",ids)
n=story(s,"La democracia racial y sus críticos","The idea of racial democracy, from Gilberto Freyre in 1933, was questioned by sociologists from the 1950s; Brazil passed a quota law in 2012.",
["En 1933 el sociólogo Gilberto Freyre, nacido en Recife, publicó Casa-Grande & Senzala, un libro sobre la sociedad del Nordeste azucarero. Freyre defendía que la mezcla entre portugueses, indígenas y africanos había creado una convivencia más armoniosa que en otros países. Con el tiempo, la idea se resumió en la expresión democracia racial, y durante décadas se usó para describir a Brasil.",
 "A partir de los años cincuenta, varios investigadores criticaron esa idea. Florestan Fernandes y otros sociólogos de São Paulo participaron en estudios sobre las relaciones raciales financiados por la Unesco. Abdias do Nascimento, activista del movimiento negro, defendió también esa crítica. Según estos autores, la armonía no existía: la esclavitud terminó en 1888 sin políticas de educación, tierra o trabajo para las personas liberadas, y el racismo siguió presente.",
 "Los datos oficiales muestran todavía diferencias. Más de la mitad de los brasileños se declara negra o parda, según el censo del IBGE, pero las personas negras y pardas tienen en promedio menos ingresos y están menos representadas en los cargos más altos. Algunos autores creen que la causa principal es la historia de la esclavitud; otros subrayan también la desigualdad social en general.",
 "A raíz de ese debate, el Congreso aprobó en agosto de 2012 la Ley de Cuotas. La ley obliga a las universidades federales a reservar la mitad de sus plazas para estudiantes que hicieron el bachillerato en escuelas públicas. Dentro de esa mitad hay plazas para estudiantes negros, pardos e indígenas, en proporción a la población de cada estado. La ley se revisó en 2023. Sus defensores dicen que amplió el acceso a la universidad; sus críticos discuten que los criterios sean los más adecuados."],
[("When did Freyre publish Casa-Grande & Senzala?",["En 1933.","En 1888.","En 2012."],0,"The first paragraph gives the year."),
 ("What did Florestan Fernandes and other sociologists do from the 1950s?",["Criticaron la idea de la democracia racial.","Defendieron la idea de la democracia racial.","Escribieron la Ley de Cuotas."],0,"The second paragraph says so."),
 ("What share of university places does the 2012 law reserve for public school students?",["La mitad.","Una décima parte.","Todas."],0,"The fourth paragraph says half.")])
print(s,n)
CH[s]=chal("The Quota Law","You are Meg. You and Carlos are preparing a short talk, and he asks what the law of 2012 changed in universities.","Tell Carlos that, as a result of the 2012 law, federal universities reserve places for public school students.",["Use *a raíz de* + noun","Say what the universities do"],"A raíz de la ley de 2012, las universidades federales reservan plazas para estudiantes de escuelas públicas.","As a result of the 2012 law, federal universities reserve places for public school students.","I can explain a cause in a formal way with *debido a* and *a raíz de*, about race and equality in Brazil.")

# ---------- consolidation
s='b2-brasilnordeste-consolidation'
x=Ex(s)
x.mc("Which sentence sets one idea against another?",
 "El Pelourinho es hoy un barrio turístico; no obstante, recuerda la esclavitud.",
 ["El Pelourinho es hoy un barrio turístico; es decir, recuerda la esclavitud.","El Pelourinho es hoy un barrio turístico; por eso, recuerda la esclavitud."],1,'contrast-markers',
 ds={"El Pelourinho es hoy un barrio turístico; es decir, recuerda la esclavitud.":'reformulation-markers',"El Pelourinho es hoy un barrio turístico; por eso, recuerda la esclavitud.":'porque-y-por-eso'})
x.fb("En la capoeira se juega en una roda para ____ el público vea a los jugadores.","que","In capoeira people play in a circle so that the audience can see the players.",'subjuntivo-de-finalidad-para-que')
x.mc("Which sentence says \"If it had rained more, they would not have left\"?",
 "Si hubiera llovido más, no se habrían ido.",
 ["Si habría llovido más, no se habrían ido.","Si hubiera llovido más, no se van."],0,'pluscuamperfecto-subjuntivo-si')
x.fb("En el sertão ____ a llover después de años de sequía.","volvió","In the sertão it rained again after years of drought.",'volver-a-infinitivo')
x.fb("A ____ de la ley de 2012, las universidades reservan plazas.","raíz","As a result of the 2012 law, universities reserve places.",'formal-cause-connectors')
x.mt([("la sequía","drought"),("el quilombo","quilombo"),("la plaza","place, seat (at a university)"),("el tambor","drum")],U)
x.fb("El Elevador Lacerda comunica la Ciudad Baja, donde está el ____, con la Ciudad Alta.","puerto","The Lacerda Elevator links the Lower City, where the port is, with the Upper City.",U,cat='vocabulary')
x.read("According to the texts, in which year did Salvador's historic centre become a UNESCO World Heritage Site?",
 "En 1985.",["En 1549.","En 2014."],1)
ids=x.write()
consolidation(s,"Review: Salvador, the sertão and the African heritage of the Northeast","Review Salvador, Candomblé and capoeira, the sertão, Palmares and the debate on race, with the grammar you used to talk about them.","review: contrast markers, para que, si hubiera + habría, volver a, debido a and a raíz de",
 ["I can review what I learned about Bahia and the Northeast.","I can use contrast markers, *para que*, past hypotheticals, *volver a* and formal causes.","I can say who explains what about Palmares and the quota law."],
 ["I can set one idea about Salvador against another with *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien*.","I can say what something is for with *para que* + subjunctive, about Candomblé and capoeira.","I can say what would have happened in a different past with *si hubiera* + participle and *habría* + participle, about the sertão.","I can say that something happened again with *volver a* + infinitive, about Palmares and Zumbi.","I can explain a cause in a formal way with *debido a* and *a raíz de*, about race and equality in Brazil."],ids)
CH[s]=chal("The Northeast in Review","You are Carlos. You and Meg are preparing a talk, and she asks you to compare the two levels of Salvador.","Tell Meg that the Lower City is the port and the Upper City is on the cliff, comparing them.",["Say that the Lower City is the port","Compare it with the Upper City"],"La Ciudad Baja es el puerto; la Ciudad Alta, en cambio, está sobre el acantilado.","The Lower City is the port; the Upper City, on the other hand, is on the cliff.","I can set one idea about Salvador against another with *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien*.")
challenges(ROOT+'/challenges-brazil-northeast.json',CH)
