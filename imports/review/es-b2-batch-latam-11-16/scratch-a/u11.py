from lib import *
V='b2-dominican-republic-vocab'
# ---------- 01
s='b2-dominicana-01'
paras=[
"La República Dominicana ocupa alrededor de dos tercios de la isla de La Española, que comparte con Haití. En el centro del país está la cordillera Central, que es la más alta de las Antillas. De sus montañas bajan varios ríos importantes, como el Yaque del Norte, que riega los valles agrícolas del norte.",
"El Pico Duarte, que mide más de tres mil metros, es la montaña más alta del Caribe. En la cordillera hay altiplanos como Valle Nuevo, que está a más de dos mil metros de altura. Allí el clima no se parece al de la costa, que es cálido todo el año: en algunas noches de invierno la temperatura baja de cero grados y aparece escarcha sobre la hierba.",
"En el noreste está la bahía de Samaná. Entre enero y marzo llegan a sus aguas ballenas jorobadas que vienen del Atlántico norte, donde pasan el resto del año. Las hembras tienen sus crías en la bahía, y cada año viajan hasta allí visitantes que quieren verlas. En mar abierto, al norte de la costa, hay además un santuario de mamíferos marinos, el Banco de la Plata.",
"En el sur de la bahía está el parque nacional Los Haitises, que protege colinas de roca caliza, llamadas mogotes, y grandes manglares donde viven muchas aves marinas. En algunas de sus cuevas se conservan dibujos que hicieron los taínos, el pueblo que habitaba la isla antes de la llegada de los europeos.",
"En el suroeste el paisaje es muy distinto, porque la región es seca. Allí está el lago Enriquillo, que es de agua salada y se encuentra bajo el nivel del mar. Es el lago más grande de las Antillas. En la isla Cabritos, que está en medio del lago, viven cocodrilos y se ven flamencos.",
"Así, en un país muy conocido por sus playas, hay también montañas con escarcha, una bahía adonde llegan las ballenas a tener sus crías y un lago que está bajo el nivel del mar."]
put_story(s,"La República Dominicana: montañas, ballenas y bahías","The Dominican Republic has the highest mountains in the Caribbean, a bay where humpback whales have their calves, a national park of limestone hills and mangroves, and a salt lake below sea level.",paras,[
("According to the text, what is Pico Duarte?",["Es la montaña más alta del Caribe y mide más de tres mil metros.","Es una isla pequeña en medio de un lago de agua salada.","Es un parque nacional con cuevas y dibujos de los taínos."],"The second paragraph says it is the highest mountain in the Caribbean."),
("What happens in Samaná Bay between January and March?",["Llegan ballenas jorobadas que vienen del Atlántico norte.","Aparece escarcha sobre la hierba durante las noches.","Los cocodrilos salen del lago hacia el mar."],"The third paragraph describes the whales."),
("What does the text say about Lake Enriquillo?",["Es un lago de agua salada que está bajo el nivel del mar.","Es un lago de agua dulce que está en lo alto de la cordillera.","Es una bahía donde nacen las ballenas jorobadas."],"The fifth paragraph describes the lake.")])
put_voc(s,"vocab.b2.dominicana.01","Mountains, bays and wetlands","Landscape words for the Dominican Republic",[("la cordillera","mountain range","noun"),("el mogote","limestone hill, mogote","noun"),("el manglar","mangrove swamp","noun"),("el santuario","sanctuary, nature reserve","noun"),("la escarcha","frost","noun")])
put_gr(s,"Relative Clauses: Places and Things That…",[
T("You know relative clauses with *que* and *quien* from B1 Unit 5: *que* joins a description to a noun (*la amiga que vive al lado*), and *quien* is for people, often after a preposition (*el vecino con quien hablamos*). The Dominican landscape is easy to describe this way: each mountain, bay or lake gets a clause that says where it is or what it does.","What you already know"),
TB("One noun, one clause",[
["La bahía de Samaná, que está en el noreste, recibe ballenas.","*que* after a place: Samaná Bay, which is in the north-east"],
["Las ballenas que llegan en enero vienen del Atlántico norte.","*que* with no commas says which whales: the whales that arrive in January"],
["El guía con quien hablamos conoce el parque.","*quien* after a preposition, for a person: the guide we spoke with"]]),
EX("In context",[
("El Pico Duarte, que mide más de tres mil metros, es la montaña más alta del Caribe.","Pico Duarte, which is over three thousand metres high, is the highest mountain in the Caribbean."),
("Los Haitises es un parque que protege manglares y colinas de roca caliza.","Los Haitises is a park that protects mangroves and limestone hills."),
("El lago Enriquillo, que es de agua salada, está bajo el nivel del mar.","Lake Enriquillo, which is a salt lake, is below sea level."),
("La guía con quien visitamos las cuevas conoce muy bien la historia de los taínos.","The guide we visited the caves with knows the history of the Taíno people very well.")]),
TIP("With commas, the clause adds extra information (*El lago Enriquillo, que es de agua salada, …*). Without commas, it says which one you mean (*las ballenas que llegan en enero*). *Quien* is only for people: for things and animals use *que*.")])
put_lesson(s,"The Dominican Republic: mountains, whales and bays","Describe the Dominican Republic's mountains, bays and wildlife with relative clauses (*que* and *quien*).","relative clauses with que and quien, applied to the Dominican landscape",[
"I can describe a mountain, a bay or a lake with a relative clause (*que*, *quien*).",
"I can say what makes Pico Duarte, Samaná Bay, Los Haitises and Lake Enriquillo different from each other.",
"I can use the new words for mountains, mangroves and frost."])
put_ex(s,[
match(s+'.ex01',[["la cordillera","mountain range"],["el mogote","limestone hill, mogote"],["el manglar","mangrove swamp"],["el santuario","sanctuary, nature reserve"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "Pico Duarte, which is over three thousand metres high, is the highest mountain in the Caribbean"?',["El Pico Duarte, que mide más de tres mil metros, es la montaña más alta del Caribe.","El Pico Duarte, quien mide más de tres mil metros, es la montaña más alta del Caribe.","El Pico Duarte, donde mide más de tres mil metros, es la montaña más alta del Caribe."],"relative-clauses"),
fill(s+'.ex03',"El guía con __ hablamos conoce muy bien el parque de Los Haitises.","quien","The guide we spoke with knows the park of Los Haitises very well.","relative-clauses"),
build(s+'.ex04',"El lago Enriquillo, que es de agua salada, está bajo el nivel del mar.","Lake Enriquillo, which is a salt lake, is below sea level.","relative-clauses"),
dlg(s+'.ex05',"¿Qué es Los Haitises?","","Me gustaría verlo algún día.",["Es un parque que protege manglares y colinas de roca caliza.","Es la montaña más alta del Caribe, que supera los tres mil metros.","Es un lago de agua salada que está bajo el nivel del mar."],V),
dict_(s+'.ex06',"En Valle Nuevo, que está en la cordillera, aparece escarcha en las noches frías.","In Valle Nuevo, which is in the mountain range, frost appears on cold nights.","relative-clauses")])
# ---------- 02
s='b2-dominicana-02'
paras=[
"Santo Domingo se considera la ciudad europea más antigua de las Américas. La primera población española de la isla, La Isabela, en la costa norte, fue fundada por Cristóbal Colón en 1494, pero fue abandonada pocos años después.",
"Santo Domingo fue fundada a finales del siglo XV por Bartolomé Colón, hermano de Cristóbal, en la orilla este del río Ozama. En 1502 un huracán destruyó la ciudad, y fue reconstruida en la orilla oeste por el nuevo gobernador, Nicolás de Ovando. En esos años fueron construidos también el hospital de San Nicolás de Bari y la fortaleza Ozama. Más tarde se levantó la catedral, que se considera la más antigua de América.",
"El Alcázar de Colón, un palacio que fue construido para Diego Colón, hijo de Cristóbal, a principios del siglo XVI, y la universidad Santo Tomás de Aquino, que fue creada en 1538 por una bula del papa Paulo III, completan el centro de la ciudad colonial. La universidad se suele considerar la primera de América. La Zona Colonial fue declarada Patrimonio de la Humanidad por la UNESCO en 1990.",
"En diciembre de 1511 el fraile dominico Antón de Montesinos dio en Santo Domingo un sermón famoso. Según el relato de Bartolomé de las Casas, preguntó a los colonos con qué derecho trataban con tanta dureza a los indígenas y los tenían en servidumbre. Los colonos recibían el trabajo de grupos de indígenas por el sistema de la encomienda.",
"Los historiadores explican que la población taína disminuyó mucho en esos años, sobre todo por las enfermedades llegadas de Europa y por el trabajo forzado. Después del sermón, la Corona española promulgó las Leyes de Burgos, en 1512. Estas leyes regularon el trato a los indígenas, pero no abolieron las encomiendas. Las Casas, que más tarde se convirtió en defensor de los indígenas, contó el sermón en su Historia de las Indias."]
put_story(s,"Santo Domingo, la primera ciudad española de las Américas","Santo Domingo was founded in the 1490s and rebuilt after a hurricane in 1502; its colonial centre holds early institutions, and in 1511 a friar's sermon criticised the treatment of the Taíno people.",paras,[
("According to the text, why was Santo Domingo rebuilt on the west bank of the Ozama in 1502?",["Porque un huracán destruyó la ciudad.","Porque Colón quería una ciudad en la costa norte.","Porque la universidad necesitaba más espacio."],"The second paragraph says a hurricane destroyed the city in 1502."),
("What does the text say about the university Santo Domingo had from 1538?",["Fue creada por una bula del papa Paulo III y se suele considerar la primera de América.","Fue construida para Diego Colón en el siglo XVI.","Fue fundada por Bartolomé Colón en la orilla este del río."],"The third paragraph describes the university."),
("What did the friar Antón de Montesinos do in December 1511?",["Dio un sermón en el que preguntó con qué derecho trataban a los indígenas con dureza.","Fundó la ciudad de La Isabela en la costa norte.","Promulgó las Leyes de Burgos en nombre de la Corona."],"The fourth paragraph describes the sermon.")])
put_voc(s,"vocab.b2.dominicana.02","Colonial Santo Domingo","Palaces, friars, sermons and laws of the early colony",[("el alcázar","fortified palace, alcázar","noun"),("el fraile","friar","noun"),("el sermón","sermon","noun"),("la encomienda","encomienda (colonial system of forced labour)","noun"),("la bula","papal bull","noun")])
put_gr(s,"The Passive with *Ser*: What Was Founded, Built and Created",[
T("You know the passive with *ser* from B1 Unit 18: *ser* + past participle, with *por* naming who did the action, and the participle agrees with the subject. The history of Santo Domingo is told this way because the buildings and the city matter more than the people who made them.","What you already know"),
TB("Fue + participle",[
["Santo Domingo fue fundada por Bartolomé Colón.","*fue fundada*: the city is feminine singular, so the participle ends in *-a*"],
["El Alcázar fue construido para Diego Colón.","*fue construido*: masculine singular; *por* is not needed when the doer is not the point"],
["Las leyes fueron promulgadas en 1512.","*fueron promulgadas*: feminine plural subject, plural *ser* and participle"],
["Los dos edificios fueron destruidos por un huracán.","*fueron destruidos* + *por*: naming what did it"]]),
EX("In context",[
("La Isabela fue fundada por Cristóbal Colón en 1494.","La Isabela was founded by Christopher Columbus in 1494."),
("La universidad fue creada en 1538 por una bula del papa.","The university was created in 1538 by a papal bull."),
("Después del huracán, la ciudad fue reconstruida en la otra orilla del río.","After the hurricane, the city was rebuilt on the other bank of the river."),
("Las Leyes de Burgos fueron promulgadas en 1512.","The Laws of Burgos were issued in 1512.")]),
TIP("The participle agrees with the subject: *fundada* (*la ciudad*), *construido* (*el palacio*), *destruidos* (*los edificios*). Use *fue* or *fueron* for a finished event in the past. Add *por* + the doer only when you want to name it.")])
put_lesson(s,"Santo Domingo: the first Spanish city in the Americas","Tell the early history of Santo Domingo with the passive with *ser* (*fue fundada*, *fueron construidos*).","the passive with ser, applied to colonial Santo Domingo",[
"I can say who founded, built or created something with *fue* / *fueron* + participle.",
"I can say what happened in Santo Domingo in 1502, 1538 and 1511.",
"I can use the new words for palace, friar, sermon and papal bull."])
put_ex(s,[
match(s+'.ex01',[["el alcázar","fortified palace, alcázar"],["el fraile","friar"],["el sermón","sermon"],["la encomienda","encomienda (forced-labour system)"]],V),
mc(s+'.ex02',"grammar",'Which sentence says that the city was founded by Bartolomé Colón?',["Santo Domingo fue fundada por Bartolomé Colón.","Santo Domingo fue fundado por Bartolomé Colón.","Santo Domingo fueron fundada por Bartolomé Colón."],"ser-passive"),
fill(s+'.ex03',"En 1502 la ciudad fue __ por un huracán.","destruida","In 1502 the city was destroyed by a hurricane.","ser-passive",hint="destruir"),
build(s+'.ex04',"El alcázar fue construido para Diego Colón, hijo de Cristóbal.","The palace was built for Diego Colón, Christopher's son.","ser-passive"),
dlg(s+'.ex05',"¿Quién fue Antón de Montesinos?","","Entonces su sermón fue muy importante.",["Fue un fraile que dio un sermón famoso en 1511.","Fue el hombre que reconstruyó la ciudad en 1502.","Fue un hermano de Colón que fundó la ciudad."],V),
dict_(s+'.ex06',"La universidad fue creada en 1538 por una bula del papa Paulo III.","The university was created in 1538 by a papal bull of Pope Paul III.","ser-passive")])
# ---------- 03
s='b2-dominicana-03'
paras=[
"El merengue y la bachata son los dos géneros musicales más conocidos de la República Dominicana. La UNESCO incluyó el merengue en su lista del patrimonio cultural inmaterial en 2016, y la bachata en 2019.",
"El merengue típico, llamado también perico ripiao, nació en el siglo XIX en el valle del Cibao, en el norte del país. Se toca con una güira, una tambora y un acordeón. Se suele explicar que cada instrumento viene de una herencia distinta: la güira, de los taínos; la tambora, de África; y el acordeón, de Europa.",
"Rafael Trujillo gobernó el país como dictador entre 1930 y 1961, y su régimen promovió el merengue como símbolo nacional. Después de 1961, músicos de orquesta como Johnny Ventura y Wilfrido Vargas lo hicieron más rápido y le añadieron instrumentos de metal. En los años setenta y ochenta el merengue se volvió popular en gran parte de América Latina.",
"La bachata nació en los años sesenta en barrios pobres de las ciudades y en zonas rurales. Viene del bolero, y sus canciones suelen hablar de amor, de abandono y de penas. Por eso se llamó también música de amargue. El sonido de la bachata se apoya en la guitarra, sobre todo en el requinto, una guitarra de notas agudas. Según muchos estudiosos, durante años se consideraba música de gente pobre, y muchas emisoras de radio no la ponían.",
"En 1990 el grupo 4.40, dirigido por Juan Luis Guerra, publicó el disco Bachata Rosa. El disco mezcló la bachata con el jazz y otros ritmos, se vendió en muchos países y ganó un premio Grammy en 1992. Más tarde, el grupo Aventura, con su cantante Romeo Santos, llevó la bachata a un público aún mayor.",
"Hoy el merengue y la bachata se bailan en todo el mundo. Cada uno se hizo conocido de una manera distinta: el merengue, con el apoyo de un gobierno; la bachata, a pesar de muchos prejuicios."]
put_story(s,"El merengue y la bachata","Merengue and bachata, the two best-known Dominican music styles, were added by UNESCO to its intangible heritage list in 2016 and 2019, after very different histories.",paras,[
("According to the text, which instruments play typical merengue?",["Una güira, una tambora y un acordeón.","Un requinto, un violín y un piano.","Una guitarra, un saxofón y una trompeta."],"The second paragraph names the three instruments."),
("What does the text say about bachata in its first years?",["Se consideraba música de gente pobre y muchas emisoras no la ponían.","Se bailaba en los actos oficiales del régimen de Trujillo.","Se tocaba solo con güira, tambora y acordeón."],"The fourth paragraph says so, according to many scholars."),
("What happened in 1990?",["El grupo 4.40 publicó el disco Bachata Rosa.","La UNESCO incluyó la bachata en su lista.","Terminó la dictadura de Trujillo."],"The fifth paragraph gives the date of the album.")])
put_voc(s,"vocab.b2.dominicana.03","Merengue and bachata","Instruments, sounds and radio",[("la güira","güira (metal scraper)","noun"),("la tambora","tambora (two-headed drum)","noun"),("el requinto","requinto (small guitar with high notes)","noun"),("el amargue","bitterness, lovesickness (a bachata theme)","noun"),("la emisora","radio station","noun")])
put_gr(s,"Verbs of Change: How Music Became Popular",[
T("You know the verbs of change *ponerse*, *volverse*, *hacerse* and *quedarse* from B1 Unit 25. *Ponerse* + adjective is a mood or state that can pass; *volverse* + adjective is a deeper change; *hacerse* + noun is a change you reach with time or effort; *quedarse* is a result; and *convertirse en* is a bigger change. The stories of merengue and bachata are stories of change.","What you already know"),
TB("Which verb of change?",[
["Los bailarines se ponen contentos al oír un merengue.","*ponerse* + adjective: a mood that passes"],
["La bachata se volvió popular en muchos países.","*volverse* + adjective: a deeper change"],
["Con los años, el merengue se hizo música nacional.","*hacerse* + noun: a change over time"],
["Cuando acabó la canción, la sala se quedó en silencio.","*quedarse*: the result of something"]]),
EX("In context",[
("Algunos bailarines se ponen tristes al oír una bachata de amargue.","Some dancers become sad when they hear a bachata of heartbreak."),
("Después de 1990, la bachata se volvió popular en muchos países.","After 1990, bachata became popular in many countries."),
("Con los años, el merengue se convirtió en un símbolo nacional.","Over the years, merengue became a national symbol."),
("Al terminar el concierto, el público se quedó sin voz.","When the concert ended, the audience was left without a voice.")]),
TIP("Choose the verb by the kind of change: *ponerse* and *quedarse* for a state that can pass or a result, *volverse* for a deeper change, *hacerse* and *convertirse en* + noun for a change over time. These verbs are reflexive, so they always have *se*.")])
put_lesson(s,"Merengue and bachata: music of the Dominican Republic","Tell how merengue and bachata changed over the years with the verbs of change (*ponerse*, *volverse*, *hacerse*, *quedarse*).","verbs of change, applied to merengue and bachata",[
"I can say how something changed with *ponerse*, *volverse*, *hacerse* or *quedarse*.",
"I can say which instruments play typical merengue and where bachata comes from.",
"I can use the new words for the güira, the tambora, the requinto and the radio."])
put_ex(s,[
match(s+'.ex01',[["la güira","güira (metal scraper)"],["la tambora","tambora (two-headed drum)"],["el requinto","requinto (small guitar with high notes)"],["la emisora","radio station"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "Over the years, merengue became a national symbol"?',["Con los años, el merengue se convirtió en un símbolo nacional.","Con los años, el merengue se quedó un símbolo nacional.","Con los años, el merengue se puso un símbolo nacional."],"verbs-of-change"),
fill(s+'.ex03',"Cuando se acabó la música, la sala se __ en silencio.","quedó","When the music ended, the room fell silent.","verbs-of-change"),
build(s+'.ex04',"La bachata se volvió popular en muchos países después de 1990.","Bachata became popular in many countries after 1990.","verbs-of-change"),
dlg(s+'.ex05',"¿Por qué llamaban a la bachata «música de amargue»?","","Ahora entiendo el nombre.",["Porque sus canciones hablaban de penas y de abandono.","Porque se tocaba solo con güira y tambora.","Porque nació en las fiestas del gobierno."],V),
dict_(s+'.ex06',"Los bailarines se ponen contentos cuando empieza el merengue.","The dancers get happy when the merengue starts.","verbs-of-change")])
# ---------- 04
s='b2-dominicana-04'
paras=[
"La Española es una isla compartida por dos países: la República Dominicana, al este, y Haití, al oeste. La frontera entre ellos mide unos 380 kilómetros. En 1697 España reconoció el dominio francés sobre la parte occidental, y el Tratado de Aranjuez, de 1777, fijó una frontera entre las dos colonias.",
"Haití se independizó de Francia en 1804. Entre 1822 y 1844 todo el territorio de la isla estuvo bajo el gobierno haitiano, y el 27 de febrero de 1844 los dominicanos proclamaron su independencia. En la memoria dominicana esos años se recuerdan como una ocupación.",
"En octubre de 1937, durante la dictadura de Rafael Trujillo, el ejército dominicano mató a miles de personas, la mayoría haitianas, en la región de la frontera. Se la conoce como la masacre del Perejil. Los historiadores no están de acuerdo sobre la cifra exacta de muertos.",
"Durante el siglo XX miles de haitianos llegaron para trabajar en la zafra, la cosecha de la caña de azúcar. Muchos vivían en bateyes, comunidades cerca de las plantaciones, y muchos de sus hijos nacieron en la República Dominicana.",
"En septiembre de 2013 el Tribunal Constitucional dominicano dictó la sentencia 168-13. Según el tribunal, los hijos de extranjeros que no residían legalmente en el país no tenían derecho a la nacionalidad dominicana, y esa regla se aplicaba también a los nacidos desde 1929. La Comisión Interamericana de Derechos Humanos expresó su preocupación, porque la decisión podía dejar sin nacionalidad a muchas personas. El gobierno defendió el derecho del país a decidir quiénes son sus nacionales, y en 2014 se aprobó una ley para regularizar a una parte de los afectados.",
"Hoy la frontera es también un lugar de comercio. Los lunes y los viernes se celebra en Dajabón un mercado binacional donde vendedores haitianos y dominicanos intercambian productos. El gobierno de Luis Abinader, presidente desde 2020 y reelegido en 2024, explica que quiere controlar mejor la frontera; organizaciones de derechos humanos han criticado algunas expulsiones."]
put_story(s,"La frontera con Haití","The island of Hispaniola is shared by the Dominican Republic and Haiti; the text gives dated facts about their history, the 1937 massacre, the workers of the sugar harvest and the 2013 court ruling on nationality, with each judgement attributed.",paras,[
("According to the text, what was the sentence 168-13?",["Una decisión del Tribunal Constitucional de 2013 sobre el derecho a la nacionalidad.","Un acuerdo de 1777 entre España y Francia sobre la frontera.","Una ley de 2014 para contratar braceros haitianos."],"The fifth paragraph describes the ruling."),
("What does the text say about the number of deaths in 1937?",["Los historiadores no están de acuerdo sobre la cifra exacta.","Todos los historiadores hablan de la misma cifra.","El texto da una cifra oficial de la Comisión Interamericana."],"The third paragraph says historians disagree."),
("What happens in Dajabón on Mondays and Fridays?",["Se celebra un mercado donde vendedores haitianos y dominicanos intercambian productos.","Se celebra la zafra de la caña de azúcar.","Se reúne el Tribunal Constitucional."],"The last paragraph describes the market.")])
put_voc(s,"vocab.b2.dominicana.04","The border and its history","Sugar, workers and rulings",[("el batey","batey (settlement near a sugar plantation)","noun"),("el bracero","farm labourer, cane cutter","noun"),("la zafra","sugar-cane harvest","noun"),("la sentencia","court ruling, sentence","noun")])
put_gr(s,"Reporting Information: Who Says What",[
T("You know how to report what a source says with *según* from B1 Unit 13: *según* + the source, *informó de que*, *explica que*. The history of the border is a topic where it matters who says what: a court, a commission, historians, a government. A sentence with a source keeps a judgement attached to the person or institution that made it.","What you already know"),
TB("Naming the source",[
["Según el Tribunal Constitucional, los hijos de extranjeros sin residencia legal no tenían derecho a la nacionalidad.","*según* + source: according to the court"],
["La Comisión Interamericana informó de que la decisión le preocupaba.","*informó de que* + a clause: reported that"],
["El gobierno explica que quiere controlar mejor la frontera.","*explica que* + a clause: explains that"],
["Según los historiadores, la cifra de muertos de 1937 se discute todavía.","*según* + a group of people"]]),
EX("In context",[
("Según los historiadores, murieron miles de personas en 1937.","According to historians, thousands of people died in 1937."),
("Según la Comisión Interamericana, la sentencia podía dejar sin nacionalidad a muchas personas.","According to the Inter-American Commission, the ruling could leave many people without a nationality."),
("El gobierno dominicano explica que quiere controlar mejor la frontera.","The Dominican government explains that it wants to control the border better."),
("La prensa informó de que el mercado de Dajabón había abierto de nuevo.","The press reported that the Dajabón market had opened again.")]),
TIP("Use *según* + source to separate what a source says from your own view. On a painful topic, give the date and the source, and let each side speak: *según el tribunal*, *según la Comisión*, *según el gobierno*. In *informó de que*, keep both words: *de que*.")])
put_lesson(s,"The border with Haiti: a shared island","Report facts about the border with Haiti and say who gives each explanation (*según*, *informó de que*, *explica que*).","reporting information and citing sources, applied to the Dominican–Haitian border",[
"I can say who reports or judges something with *según* and *explica que*.",
"I can give the dates of 1844, 1937 and 2013 and say who disagrees about what.",
"I can use the new words for sugar-cane workers, the harvest and a court ruling."])
put_ex(s,[
match(s+'.ex01',[["el batey","batey (settlement near a plantation)"],["el bracero","farm labourer, cane cutter"],["la zafra","sugar-cane harvest"],["la sentencia","court ruling"]],V),
mc(s+'.ex02',"grammar",'Which sentence says "According to historians, thousands of people died in 1937"?',["Según los historiadores, murieron miles de personas en 1937.","Los historiadores según murieron miles de personas en 1937.","Según los historiadores, que murieron miles de personas en 1937."],"estilo-indirecto-informacion"),
fill(s+'.ex03',"__ el tribunal, los hijos de extranjeros sin residencia legal no tenían derecho a la nacionalidad.","Según","According to the court, the children of foreigners without legal residence had no right to nationality.","estilo-indirecto-informacion"),
build(s+'.ex04',"El gobierno explica que quiere controlar mejor la frontera.","The government explains that it wants to control the border better.","estilo-indirecto-informacion"),
dlg(s+'.ex05',"¿Qué es un batey?","","Ahora entiendo mejor la historia de la zafra.",["Es una comunidad cerca de las plantaciones donde vivían los braceros.","Es un mercado donde venden productos de los dos países.","Es una decisión del tribunal sobre la nacionalidad."],V),
dict_(s+'.ex06',"Según los historiadores, la cifra de muertos de 1937 se discute todavía.","According to historians, the number of deaths in 1937 is still debated.","estilo-indirecto-informacion")])
# ---------- 05
s='b2-dominicana-05'
paras=[
"El béisbol, que los dominicanos llaman la pelota, es el deporte más popular del país. Según la tradición, llegó a finales del siglo XIX con inmigrantes cubanos que se instalaron en las plantaciones de azúcar del este.",
"La República Dominicana es el país extranjero que más jugadores aporta a las Grandes Ligas de Estados Unidos. Muchos nacieron en San Pedro de Macorís, una ciudad pequeña que dio peloteros como Sammy Sosa y Robinson Canó. Los equipos de las Grandes Ligas tienen academias en el país, donde adolescentes entrenan con la esperanza de firmar un contrato.",
"Hasta 2024, cinco dominicanos habían entrado en el Salón de la Fama del Béisbol, en Cooperstown: Juan Marichal, el primero, en 1983; Pedro Martínez, en 2015; Vladimir Guerrero, en 2018; David Ortiz, en 2022; y Adrián Beltré, en 2024.",
"Desde finales del siglo XX, el turismo es otra fuente importante de ingresos. Playas como las de Punta Cana y Puerto Plata reciben cada año a millones de visitantes extranjeros, y muchos dominicanos trabajan en hoteles y restaurantes. Según algunos ambientalistas, el turismo masivo puede dañar los arrecifes de coral.",
"Una gran comunidad dominicana vive en el extranjero, sobre todo en Estados Unidos. En Nueva York, el barrio de Washington Heights, en Manhattan, es conocido por su población dominicana: allí hay restaurantes, colmados y emisoras de radio dominicanos.",
"Muchos emigrantes envían dinero a sus familias, y estas remesas son una parte importante de los ingresos de muchos hogares. Para muchas familias la pregunta es la misma: si sus abuelos no hubieran emigrado, hoy ellos vivirían en la isla. Así, la pelota, el turismo y la diáspora unen al país con el resto del mundo."]
put_story(s,"Béisbol, turismo y diáspora","Baseball, tourism and the large Dominican community abroad connect the Dominican Republic with the world; the text gives dated facts and one question many families ask.",paras,[
("According to the text, where were many Dominican baseball players born?",["En San Pedro de Macorís, una ciudad pequeña del este.","En Washington Heights, en Manhattan.","En Punta Cana, en la costa del este."],"The second paragraph names San Pedro de Macorís."),
("Who was the first Dominican in the Hall of Fame in Cooperstown, according to the text?",["Juan Marichal, en 1983.","Pedro Martínez, en 2015.","Adrián Beltré, en 2024."],"The third paragraph gives the list."),
("What are remittances, according to the text?",["Dinero que los emigrantes envían a sus familias.","Visitantes extranjeros que llegan a las playas.","Contratos que firman los jóvenes peloteros."],"The last paragraph explains them.")])
put_voc(s,"vocab.b2.dominicana.05","Baseball, tourism and the diaspora","Words for the ball game, the corner shop and money sent home",[("el pelotero","baseball player","noun"),("la pelota","baseball (the game)","noun"),("la remesa","remittance (money sent home)","noun"),("el colmado","corner shop","noun")])
put_gr(s,"Mixed Conditionals: A Past Choice, a Present Result",[
T("You know mixed conditionals with *si hubiera* from B2 Unit 11: *si* + *hubiera* + participle looks back at a past choice (the pattern of B1 Unit 35), and the result takes the simple conditional because it is about now (the conditional *viviría*, from A2 Unit 26). Emigration is full of such thoughts: the move happened once, and its result lasts.","What you already know"),
TB("Same past, present result",[
["Si mis abuelos no hubieran emigrado, hoy yo viviría en la isla.","past choice (*no hubieran emigrado*) + result now (*viviría*)"],
["Si hubiera nacido en San Pedro de Macorís, ahora sería pelotero.","*hubiera nacido* + *sería*: I was not born there, and I am not a player"],
["Si hubiéramos reservado el hotel en enero, ahora estaríamos en Punta Cana.","*hubiéramos reservado* + *estaríamos*"]]),
EX("In context",[
("Si mis abuelos no hubieran emigrado a Nueva York, hoy yo viviría en Santo Domingo.","If my grandparents had not emigrated to New York, I would live in Santo Domingo today."),
("Si hubiera firmado aquel contrato, ahora jugaría en las Grandes Ligas.","If I had signed that contract, I would be playing in the major leagues now."),
("Si hubiéramos reservado el hotel en enero, ahora estaríamos en Punta Cana.","If we had booked the hotel in January, we would be in Punta Cana now."),
("Si no hubieras comprado el boleto, hoy no verías el mar.","If you had not bought the ticket, you would not be seeing the sea today.")]),
TIP("Look at the result clause. A word that points to now (*ahora*, *hoy*) usually means the simple conditional (*viviría*). If the result also belongs to the past, you are back in B1 Unit 35 and need *habría* + participle. In the *si* clause, *habría* never appears: say *si hubiera nacido*, not *si habría nacido*.")])
put_lesson(s,"Baseball, tourism and the diaspora","Talk about baseball, tourism and Dominicans abroad, and imagine different pasts with mixed conditionals.","mixed conditionals, applied to baseball, tourism and the diaspora",[
"I can say what would be different today if a past choice had been different.",
"I can say why San Pedro de Macorís and Washington Heights are well known.",
"I can use the new words for baseball players, remittances and the corner shop."])
put_ex(s,[
match(s+'.ex01',[["el pelotero","baseball player"],["la pelota","baseball (the game)"],["la remesa","remittance (money sent home)"],["el colmado","corner shop"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "If I had been born in San Pedro de Macorís, I would be a baseball player now"?',["Si hubiera nacido en San Pedro de Macorís, ahora sería pelotero.","Si hubiera nacido en San Pedro de Macorís, ahora habría sido pelotero.","Si naciera en San Pedro de Macorís, ahora sería pelotero."],"mixed-conditionals",ds={"1":"pluscuamperfecto-subjuntivo-si","2":"hypothetical-structures"}),
fill(s+'.ex03',"Si mis abuelos no hubieran emigrado, hoy yo __ en la isla.","viviría","If my grandparents had not emigrated, I would live on the island today.","mixed-conditionals",hint="vivir (yo)"),
build(s+'.ex04',"Si hubiéramos reservado el hotel en enero, ahora estaríamos en Punta Cana.","If we had booked the hotel in January, we would be in Punta Cana now.","mixed-conditionals"),
dlg(s+'.ex05',"¿Qué es un colmado?","","Entonces voy a entrar en uno.",["Es una tienda pequeña de barrio donde se compra comida y bebida.","Es una academia donde los jóvenes entrenan para ser peloteros.","Es dinero que envían a sus familias las personas que viven fuera."],V),
dict_(s+'.ex06',"Si hubiera aceptado el contrato, ahora jugaría en las Grandes Ligas.","If I had accepted the contract, I would be playing in the major leagues now.","mixed-conditionals")])
# ---------- consolidation
s='b2-dominicana-consolidation'
put_lesson(s,"Unit 11 Review: Dominican Republic","Review the Dominican Republic from its mountains to its diaspora, with relative clauses, the passive with *ser*, verbs of change, reported information and mixed conditionals.","review: relative clauses, passive with ser, verbs of change, reporting information, mixed conditionals",[
"I can review what I learned about the Dominican Republic, from Pico Duarte to Washington Heights.",
"I can use relative clauses, the passive with *ser*, verbs of change, reported information and mixed conditionals.",
"I can put events from 1494 to 2019 in order.",
"I can say who gives which judgement when a matter is disputed."],
checklist=[
"I can describe a place or a thing with a relative clause (*que*, *quien*).",
"I can say what was founded, built or created with *fue* / *fueron* + participle.",
"I can say how something changed with *ponerse*, *volverse*, *hacerse* or *quedarse*.",
"I can report what a source says with *según* and *explica que*.",
"I can imagine a different past and its result today with *si hubiera* + participle and the conditional."])
put_ex(s,[
match(s+'.ex01',[["el mogote","limestone hill, mogote"],["el alcázar","fortified palace, alcázar"],["la güira","güira (metal scraper)"],["el pelotero","baseball player"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "The whales that arrive in January come from the North Atlantic"?',["Las ballenas que llegan en enero vienen del Atlántico norte.","Las ballenas quienes llegan en enero vienen del Atlántico norte.","Las ballenas donde llegan en enero vienen del Atlántico norte."],"relative-clauses"),
mc(s+'.ex03',"reading","According to the texts, what happened in 1538?",["Fue creada la universidad Santo Tomás de Aquino.","Fue fundada la ciudad de La Isabela.","Fue reconstruida la ciudad de Santo Domingo."],None),
fill(s+'.ex04',"Si hubiéramos llegado a Santo Domingo ayer, hoy __ la catedral.","visitaríamos","If we had arrived in Santo Domingo yesterday, we would be visiting the cathedral today.","mixed-conditionals",hint="visitar (nosotros)"),
{"id":s+".ex05","type":"sentence-order","category":"grammar","sentences":["La Isabela fue fundada por Colón en 1494. [La Isabela was founded by Columbus in 1494.]","Santo Domingo fue reconstruida en 1502 en la orilla oeste. [Santo Domingo was rebuilt in 1502 on the west bank.]","La universidad fue creada en 1538 por una bula del papa. [The university was created in 1538 by a papal bull.]","La bachata fue incluida en 2019 en la lista de la UNESCO. [Bachata was added to UNESCO's list in 2019.]"],"solution":[0,1,2,3],"teaches":["ser-passive"]},
dlg(s+'.ex06',"¿Qué se celebra los lunes y los viernes en Dajabón?","","Me gustaría verlo algún día.",["Un mercado donde vendedores de los dos países intercambian productos.","Una ceremonia en la catedral, donde los frailes dan un sermón.","Un juego de pelota donde juegan peloteros de las academias."],V),
dict_(s+'.ex07',"El merengue fue incluido en 2016 y la bachata en 2019.","Merengue was added in 2016 and bachata in 2019.","ser-passive"),
{"id":s+".ex08","type":"structured-writing","category":"writing","template":[{"prompt":"Say that if your grandparents had not emigrated, you would live on the island today. Start with \"Si mis abuelos no\".","answer":"Si mis abuelos no hubieran emigrado, hoy yo viviría en la isla."}],"teaches":["mixed-conditionals"]}])
