import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-paraguay-vocab'
def S(n): return f'b2-paraguay-{n}'
def I(n,k): return f'{S(n)}.ex{k:02d}'
def std(n,title,ex):
    exfile(S(n),ex); lesson(S(n),title,[f'ex0{k}' for k in range(1,7)],dlg=['ex05'])

# ---------- 01
n='01'
story(S(n),'El guaraní y el español en Paraguay','Paraguay has two official languages since the 1992 constitution; Guaraní, an indigenous language older than Spanish in the region, is spoken by most people, and jopara mixes the two.',[
"En Paraguay se hablan dos lenguas principales: el español y el guaraní. El guaraní es una lengua indígena que ya se hablaba en la región antes de la llegada de los españoles. Asunción fue fundada en 1537, y desde esa época los dos idiomas conviven.",
"Durante mucho tiempo el español fue la única lengua oficial. En la Constitución de 1967 el guaraní pasó a ser «lengua nacional», y la Constitución de 1992 declaró oficiales las dos lenguas.",
"Según los censos y las encuestas, la mayoría de los paraguayos habla guaraní, solo o junto con el español. Con frecuencia se dice que Paraguay es el único país hispanoamericano en el que la mayoría de la población habla una lengua indígena.",
"Muchas personas mezclan las dos lenguas en la misma conversación. Esa mezcla se llama jopara. Además, algunas palabras del guaraní entraron al español, como mandioca o ñandú. Hoy hay radios, periódicos y libros en guaraní, y también se enseña en las escuelas.",
],[
("What did the Constitution of 1992 do, according to the text?",["Declaró oficiales el español y el guaraní.","Declaró oficial solo el español.","Prohibió el jopara en las escuelas."],"The second paragraph gives the 1992 decision."),
("What does the text say about the majority of Paraguayans?",["Según los censos y las encuestas, habla guaraní, solo o con el español.","Según los censos, habla solo español.","Según las encuestas, no habla ninguna lengua indígena."],"The third paragraph attributes the statement to censuses and surveys."),
("What is jopara?",["Una mezcla de guaraní y español en la misma conversación.","Una palabra del español para la mandioca.","El nombre de una radio en guaraní."],"The last paragraph defines jopara."),
])
grammar(S(n),'grammar.b2.paraguay.01.adverbios-de-postura-guarani','Your Stance on the Facts: Adverbs Like En Realidad',
"You know *lamentablemente*, *en realidad* and *en rigor* from B2 Unit 1: stance adverbs that comment on a whole sentence. They are useful for the story of two languages in Paraguay, where people often assume things that are not exactly true. Here they correct an idea, show how sure you are or give the exact fact.",
[["En realidad, Paraguay tiene dos lenguas oficiales.","*en realidad*: you correct what someone assumed"],["Indudablemente, el guaraní forma parte de la vida diaria.","*indudablemente*: you are sure"],["En rigor, el guaraní es lengua oficial desde 1992.","*en rigor*: strictly speaking, the exact fact"],["Lamentablemente, algunos hablantes sienten vergüenza de mezclar las lenguas.","*lamentablemente*: your feeling about a fact"]],
'Stance adverbs at work',
[("En realidad, Paraguay tiene dos lenguas oficiales.","In fact, Paraguay has two official languages."),("Indudablemente, el guaraní forma parte de la vida diaria.","Undoubtedly, Guaraní is part of daily life."),("En rigor, el guaraní es lengua oficial desde 1992.","Strictly speaking, Guaraní has been an official language since 1992."),("Los hablantes, indudablemente, cambian de lengua según la situación.","Speakers, undoubtedly, change language depending on the situation.")],
"Remember the comma test: you can pause and put commas around a stance adverb. When you write about a language, use *en rigor* and *en realidad* for exact facts and keep a feeling like *lamentablemente* for what you really think; give the opinion to someone when it is history.")
vocab(S(n),'Guaraní, Spanish and jopara',[('bilingüismo','bilingualism','noun'),('jopara','mix of Guaraní and Spanish','noun'),('indígena','indigenous','adjective'),('oficial','official','adjective'),('mezcla','mixture','noun'),('constitución','constitution','noun')])
T='stance-adverbs'
ex=[
mc(I(n,1),"You are sure that Guaraní is part of daily life in Paraguay. Which sentence says this?",["Indudablemente, el guaraní forma parte de la vida diaria en Paraguay.","Apenas, el guaraní forma parte de la vida diaria en Paraguay.","Lamentablemente, el guaraní forma parte de la vida diaria en Paraguay."],0,T),
fb(I(n,2),"__, mucha gente en Paraguay habla guaraní, solo o con el español.","Indudablemente","Undoubtedly, many people in Paraguay speak Guaraní, alone or with Spanish.",T),
sb(I(n,3),"En rigor, el guaraní es lengua oficial desde 1992.","Strictly speaking, Guaraní has been an official language since 1992.",T),
mt(I(n,4),[["el bilingüismo","bilingualism"],["la mezcla","mixture"],["la constitución","constitution"],["indígena","indigenous"]],V),
dc(I(n,5),[("Meg","¿Qué lenguas son oficiales en Paraguay desde 1992?"),("Carlos","_____"),("Meg","Entonces el guaraní no es solo una lengua de la casa.")],["El español y el guaraní son lenguas oficiales.","El guaraní y el portugués son lenguas oficiales.","Solo el español es lengua oficial."],0,V,cat='dialogue'),
rdg(I(n,6),"What does the text say about the Constitution of 1992?",["Declaró oficiales el español y el guaraní.","Declaró oficial solo el español.","Prohibió el jopara en las escuelas."],0),
]
std(n,'Paraguay: Guaraní and Spanish, two official languages',ex)

# ---------- 02
n='02'
story(S(n),'Las misiones jesuíticas guaraníes','From 1609 Jesuits founded about thirty missions among the Guaraní; two of them in Paraguay, Trinidad and Jesús, are UNESCO World Heritage sites since 1993, and historians judge the missions differently.',[
"Desde 1609 los jesuitas fundaron misiones, llamadas reducciones, entre los guaraníes de lo que hoy es Paraguay, el noreste de Argentina y el sur de Brasil. En total fueron unas treinta, y en su mejor época vivieron en ellas más de cien mil personas.",
"En cada reducción había una plaza central, una iglesia, talleres y campos de cultivo. Los guaraníes tocaban violines y arpas, y tallaban madera y piedra en el estilo barroco que llegó de Europa. Los jesuitas enseñaban también en guaraní.",
"Los historiadores no coinciden sobre las misiones. Según algunos, las reducciones protegieron a los guaraníes de la esclavitud y de los colonos; según otros, los jesuitas controlaban la vida de los indígenas. Los dos puntos de vista se discuten hasta hoy.",
"En 1767 el rey de España expulsó a los jesuitas de sus dominios, y las misiones perdieron su organización. Con el tiempo, muchas fueron abandonadas. No obstante, algunas ruinas se conservan: en Paraguay, las de La Santísima Trinidad del Paraná y las de Jesús de Tavarangüé, cuya iglesia quedó sin terminar en 1767. La UNESCO las declaró Patrimonio de la Humanidad en 1993.",
],[
("When did the Jesuits start founding missions among the Guaraní?",["Desde 1609.","Desde 1993.","Desde 1864."],"The first paragraph gives the starting year."),
("What do historians say about the missions, according to the text?",["Algunos creen que protegieron a los guaraníes, y otros que los jesuitas controlaban su vida.","Todos creen que fueron un error total.","Todos creen que no tuvieron ninguna escuela."],"The third paragraph gives both points of view."),
("What did UNESCO do in 1993?",["Declaró Patrimonio de la Humanidad las ruinas de Trinidad y de Jesús.","Expulsó a los jesuitas de Paraguay.","Fundó la reducción de Jesús."],"The last paragraph gives the UNESCO decision."),
])
grammar(S(n),'grammar.b2.paraguay.02.sin-embargo-misiones','Two Views of the Missions: Sin Embargo, No Obstante and Aunque',
"You know *sin embargo* from A2 Unit 28 and *no obstante* from B1 Unit 1, and *aunque* from A2 Unit 28. They introduce an idea that goes against the first one. The Jesuit missions are a topic where historians disagree, so they are very useful to put two views side by side.",
[["Las misiones protegieron a los guaraníes; sin embargo, los jesuitas controlaban su vida.","*sin embargo*: however"],["Los jesuitas fueron expulsados en 1767; no obstante, las ruinas siguen en pie.","*no obstante*: nevertheless (more formal)"],["Aunque la iglesia de Jesús quedó sin terminar, hoy es patrimonio de la humanidad.","*aunque*: although"],["La música barroca llegó de Europa; sin embargo, los guaraníes la hicieron suya.","contrast with the expected"]],
'Contrast connectors',
[("Las misiones protegieron a los guaraníes; sin embargo, los jesuitas controlaban su vida.","The missions protected the Guaraní; however, the Jesuits controlled their lives."),("Los jesuitas fueron expulsados en 1767; no obstante, las ruinas siguen en pie.","The Jesuits were expelled in 1767; nevertheless, the ruins are still standing."),("Aunque la iglesia de Jesús quedó sin terminar, hoy es patrimonio de la humanidad.","Although the church of Jesús was left unfinished, it is a world heritage site today."),("La música barroca llegó de Europa; sin embargo, los guaraníes la hicieron suya.","Baroque music came from Europe; however, the Guaraní made it their own.")],
"Use a contrast connector only when the second idea goes against the first; for a result use *por eso* or *así que*. *Sin embargo* and *no obstante* take a comma after them. When historians disagree, say who holds each view (*según algunos historiadores*).")
vocab(S(n),'The Jesuit missions: church, baroque and heritage',[('reducción','Jesuit mission settlement for the Guaraní','noun'),('jesuita','Jesuit','noun'),('tallar','to carve','verb'),('patrimonio','heritage','noun'),('ruina','ruin','noun'),('expulsar','to expel','verb')])
T='contrast-concession-connectors'
ex=[
mc(I(n,1),"Some historians say the missions protected the Guaraní, but others say the Jesuits controlled their lives. Which sentence joins the two ideas as a contrast?",["Las misiones protegieron a los guaraníes; no obstante, según otros, los jesuitas controlaban su vida.","Las misiones protegieron a los guaraníes; por eso, según otros, los jesuitas controlaban su vida.","Las misiones protegieron a los guaraníes; así que, según otros, los jesuitas controlaban su vida."],0,T,ds={"1":"porque-y-por-eso"}),
fb(I(n,2),"Los jesuitas fueron expulsados en 1767; no __, las ruinas de las misiones siguen en pie.","obstante","The Jesuits were expelled in 1767; nevertheless, the ruins of the missions are still standing.",T),
sb(I(n,3),"La iglesia de Jesús quedó sin terminar; sin embargo, hoy es patrimonio de la humanidad.","The church of Jesús was left unfinished; however, it is a world heritage site today.",T),
mt(I(n,4),[["la reducción","Jesuit mission settlement"],["el jesuita","Jesuit"],["tallar","to carve"],["el patrimonio","heritage"]],V),
dc(I(n,5),[("Meg","¿Qué pasó con las misiones en 1767?"),("Carlos","_____"),("Meg","Por eso hoy solo quedan ruinas.")],["El rey de España expulsó a los jesuitas.","El rey de España fundó más reducciones jesuitas.","La UNESCO declaró las ruinas patrimonio de la humanidad."],0,V,cat='dialogue'),
rdg(I(n,6),"Which two sites in Paraguay does the text say UNESCO declared World Heritage in 1993?",["Trinidad y Jesús de Tavarangüé.","Asunción y Humaitá.","Filadelfia y Loma Plata."],0),
]
std(n,'Paraguay: the Jesuit missions and the Guaraní baroque',ex)

# ---------- 03
n='03'
story(S(n),'La Guerra de la Triple Alianza (1864–1870)','The war between Paraguay and Brazil, Argentina and Uruguay lasted from 1864 to 1870, ended with Francisco Solano López killed at Cerro Corá, and left Paraguay with fewer people and less land; the number of dead is still disputed.',[
"La Guerra de la Triple Alianza, que enfrentó a Paraguay con Brasil, Argentina y Uruguay, duró de 1864 a 1870. El presidente paraguayo era Francisco Solano López. El tratado de la Triple Alianza fue firmado por los otros tres países en mayo de 1865.",
"Durante los primeros años, Paraguay tuvo un ejército importante y una fortaleza fuerte sobre el río Paraguay, en Humaitá. Esa fortaleza fue tomada por las fuerzas aliadas en 1868. En enero de 1869 la capital, Asunción, fue ocupada por tropas brasileñas.",
"López siguió luchando con su ejército en el norte del país. Murió el 1 de marzo de 1870 en Cerro Corá, y con su muerte terminó la guerra.",
"Las consecuencias fueron muy graves para Paraguay. Perdió territorio frente a Argentina y Brasil, y su población bajó mucho. Las estimaciones del número de muertos varían mucho según los historiadores, y todavía se discuten.",
"En la reconstrucción del país tuvieron un papel muy importante las mujeres. Se las recuerda como «las residentas», un nombre que viene de las mujeres que vivieron y trabajaron durante la guerra. Los historiadores también discuten las causas de la guerra: unos subrayan las decisiones de López, otros los intereses de Brasil y Argentina.",
],[
("When did the Triple Alliance War take place?",["De 1864 a 1870.","De 1932 a 1935.","De 1609 a 1767."],"The first paragraph gives the dates."),
("What does the text say about the number of victims?",["Las estimaciones varían mucho según los historiadores.","Todos los historiadores dan la misma cifra.","No hubo víctimas entre los paraguayos."],"The fourth paragraph says the estimates vary."),
("What happened at Cerro Corá on 1 March 1870?",["Murió Francisco Solano López y terminó la guerra.","Fue firmado el tratado de la Triple Alianza.","Fue ocupada la ciudad de Asunción."],"The third paragraph describes it."),
])
grammar(S(n),'grammar.b2.paraguay.03.ser-participio-guerra','Naming What Happened: The Passive with Ser',
"You know the passive with *ser* + past participle from B1 Unit 18: *La ley fue aprobada por el Parlamento*. The participle agrees with the subject and *por* names who did the action. In writing about a war it keeps the focus on the places and documents: what was signed, taken or occupied.",
[["El tratado fue firmado en mayo de 1865.","*fue firmado*: singular, masculine (*el tratado*)"],["La fortaleza de Humaitá fue tomada en 1868.","*fue tomada*: singular, feminine"],["La capital fue ocupada por tropas brasileñas.","*fue ocupada por*: *por* names the agent"],["Muchas ciudades fueron destruidas durante la guerra.","*fueron destruidas*: plural, feminine"]],
'Ser + participle',
[("El tratado fue firmado en mayo de 1865.","The treaty was signed in May 1865."),("La fortaleza de Humaitá fue tomada en 1868.","The fortress of Humaitá was taken in 1868."),("La capital fue ocupada por tropas brasileñas.","The capital was occupied by Brazilian troops."),("Muchas ciudades fueron destruidas durante la guerra.","Many towns were destroyed during the war.")],
"Make the participle agree with the subject (*firmado*, *tomada*, *destruidas*) and put *ser* in the right tense. Name the agent with *por* only when it matters. If you want to leave it out in a general statement, you can use the *se* passive, as in *se firmó el tratado*.")
vocab(S(n),'The Triple Alliance War',[('guerra','war','noun'),('alianza','alliance','noun'),('fortaleza','fortress','noun'),('tratado','treaty','noun'),('residenta','woman who lived and worked in Paraguay during the war','noun'),('víctima','victim','noun')])
T='ser-passive'
ex=[
mc(I(n,1),"Which sentence says that the treaty of the Triple Alliance was signed in 1865?",["El tratado de la Triple Alianza fue firmado en 1865.","El tratado de la Triple Alianza fue firmada en 1865.","El tratado de la Triple Alianza fue firmado por 1865."],0,T),
fb(I(n,2),"La fortaleza de Humaitá __ tomada en 1868.","fue","The fortress of Humaitá was taken in 1868.",T),
sb(I(n,3),"La capital fue ocupada por tropas brasileñas en 1869.","The capital was occupied by Brazilian troops in 1869.",T),
mt(I(n,4),[["la guerra","war"],["la alianza","alliance"],["la fortaleza","fortress"],["el tratado","treaty"]],V),
dc(I(n,5),[("Meg","¿Quiénes eran las residentas?"),("Carlos","_____"),("Meg","Ahora entiendo por qué se las recuerda.")],["Mujeres que vivieron y trabajaron durante la guerra.","Soldados que firmaron el tratado de la Triple Alianza.","Jesuitas que construyeron las reducciones."],0,V,cat='dialogue'),
rdg(I(n,6),"How does the text describe the number of victims of the war?",["Las cifras varían mucho entre los historiadores.","Los historiadores coinciden en una cifra exacta.","Casi no hubo víctimas en la guerra."],0),
]
std(n,'Paraguay: the Triple Alliance War, 1864–1870',ex)

# ---------- 04
n='04'
story(S(n),'El Gran Chaco paraguayo','The Paraguayan Chaco, west of the Paraguay River, is a dry plain with few inhabitants, quebracho wood and tannin, indigenous peoples and Mennonite settlers since 1927; Bolivia and Paraguay fought there in 1932–1935.',[
"El Chaco paraguayo es la región del oeste de Paraguay, al otro lado del río Paraguay. Es una llanura caliente, con bosques bajos y zonas secas, y ocupa una parte muy grande del territorio del país, pero tiene muy pocos habitantes en comparación con el este.",
"Allí viven pueblos indígenas como los enxet, los nivaclé y los ayoreo. Desde finales del siglo XIX se explotó el quebracho colorado, un árbol de madera muy dura de la que se extrae el tanino, una sustancia que se usa para curtir cuero. Varias comunidades indígenas reclaman hoy ante la justicia la devolución de tierras.",
"Entre 1932 y 1935 Bolivia y Paraguay se enfrentaron en la Guerra del Chaco. Según el tratado de paz de 1938, Paraguay mantuvo la mayor parte de la región.",
"En 1927 llegaron al Chaco los primeros menonitas, un grupo religioso de origen europeo que venía de Canadá, y fundaron la colonia Menno. Más tarde llegaron otros grupos. Hoy en el Chaco central hay ciudades como Filadelfia y Loma Plata, y cooperativas menonitas que producen leche y carne.",
],[
("Where is the Paraguayan Chaco?",["En el oeste de Paraguay.","En el sureste de Paraguay.","En el norte de Uruguay."],"The first paragraph places it west of the Paraguay River."),
("What is tannin used for, according to the text?",["Para curtir cuero.","Para hacer papel.","Para preparar tereré."],"The second paragraph gives its use."),
("When did the first Mennonites arrive in the Chaco?",["En 1927.","En 1938.","En 1609."],"The last paragraph gives the year."),
])
grammar(S(n),'grammar.b2.paraguay.04.digresiones-chaco','Side Remarks: Por Cierto, A Propósito and Dicho Sea de Paso',
"You know *por cierto* and *volviendo a lo que decíamos* from B2 Unit 28, with *a propósito (de)* and *dicho sea de paso*: phrases that mark a side remark and the way back. They are for speaking and talks. Imagine you are telling a friend about the Chaco: you want to add a detail, and then return to your point.",
[["El Chaco tiene pocos habitantes; por cierto, ¿has visto el mapa?","*por cierto*: by the way (a new thought)"],["A propósito de los menonitas, llegaron al Chaco en 1927.","*a propósito de* + noun: speaking of"],["El quebracho, dicho sea de paso, tiene mucho tanino.","*dicho sea de paso*: incidentally, between commas"],["Volviendo a lo que decíamos, el Chaco es una región muy seca.","*volviendo a lo que decíamos*: back to the main line"]],
'Side remarks and the way back',
[("El Chaco tiene pocos habitantes; por cierto, ¿has visto el mapa?","The Chaco has few inhabitants; by the way, have you seen the map?"),("A propósito de los menonitas, llegaron al Chaco en 1927.","Speaking of the Mennonites, they arrived in the Chaco in 1927."),("El quebracho, dicho sea de paso, tiene mucho tanino.","The quebracho, incidentally, has a lot of tannin."),("Volviendo a lo que decíamos, el Chaco es una región muy seca.","Going back to what we were saying, the Chaco is a very dry region.")],
"A side remark is short and you should come back to the main line afterwards. To add a main point, use *además* (A2 Unit 28), not these phrases. *A propósito* alone means \"by the way\"; *a propósito de* needs a noun.")
vocab(S(n),'The Chaco: quebracho, tannin and the Mennonites',[('quebracho','quebracho tree, very hard wood','noun'),('tanino','tannin, a substance used to tan leather','noun'),('menonita','Mennonite','noun'),('cooperativa','cooperative','noun'),('seco','dry','adjective'),('madera','wood','noun')])
T='marcadores-digresion'
ex=[
mc(I(n,1),"You are talking about the quebracho and want to add a quick side remark about tannin. Which sentence does that?",["El quebracho tiene madera dura; dicho sea de paso, de él se extrae el tanino.","El quebracho tiene madera dura; volviendo a lo que decíamos, de él se extrae el tanino.","El quebracho tiene madera dura; por lo tanto, de él se extrae el tanino."],0,T),
fb(I(n,2),"A __ de los menonitas, llegaron al Chaco en 1927.","propósito","Speaking of the Mennonites, they arrived in the Chaco in 1927.",T),
sb(I(n,3),"Volviendo a lo que decíamos, el Chaco es un lugar muy seco.","Going back to what we were saying, the Chaco is a very dry place.",T),
mt(I(n,4),[["el quebracho","very hard wood tree"],["el tanino","tannin"],["el menonita","Mennonite"],["la cooperativa","cooperative"]],V),
dc(I(n,5),[("Meg","¿Qué es el quebracho?"),("Carlos","_____"),("Meg","Es una planta muy útil.")],["Un árbol del Chaco con madera muy dura y mucho tanino.","Una cooperativa de los menonitas en Filadelfia.","Una guerra entre Bolivia y Paraguay."],0,V,cat='dialogue'),
rdg(I(n,6),"What does the text say about the Chaco War?",["Fue una guerra entre Bolivia y Paraguay, de 1932 a 1935.","Fue una guerra entre Paraguay y Brasil, de 1864 a 1870.","Fue una guerra ganada por los menonitas en 1927."],0),
]
std(n,'Paraguay: the Gran Chaco, quebracho and the Mennonites',ex)

# ---------- 05
n='05'
story(S(n),'El tereré y la guarania','Tereré, a cold mate infusion shared in a circle, was inscribed by UNESCO in December 2020; the guarania, a slow musical genre created by José Asunción Flores in 1925, is played with the Paraguayan harp.',[
"El tereré es la bebida más común de muchas casas paraguayas, sobre todo en los días de calor. Se prepara con yerba mate y agua fría, y a menudo con hierbas medicinales, que en guaraní se llaman pohã ñana. Se sirve en un vaso llamado guampa, hecho de cuerno de vaca o de madera, y se bebe con una bombilla, un tubo de metal con un filtro.",
"Lo normal es tomar el tereré en grupo: una persona sirve el agua y la guampa pasa de mano en mano. Por eso el tereré se asocia con la amistad y la conversación. En diciembre de 2020 la UNESCO incluyó los conocimientos y las prácticas del tereré en la Lista Representativa del Patrimonio Cultural Inmaterial de la Humanidad.",
"Dos géneros muy populares de la música paraguaya son la polca paraguaya, rápida y alegre, y la guarania, lenta y melancólica. El compositor José Asunción Flores creó la guarania en 1925. Se toca con guitarra y con el arpa paraguaya, un instrumento muy ligado a esta música.",
"Hoy muchos paraguayos consideran la guarania un símbolo de su identidad.",
],[
("How is tereré prepared, according to the text?",["Con yerba mate y agua fría.","Con yerba mate y agua hirviendo.","Con café y leche caliente."],"The first paragraph describes the preparation."),
("What happened in December 2020?",["La UNESCO incluyó el tereré en su lista del patrimonio inmaterial.","José Asunción Flores creó la guarania.","Se firmó el tratado de la Triple Alianza."],"The second paragraph gives the UNESCO decision."),
("What is the guarania, according to the text?",["Un género musical lento y melancólico.","Una bebida fría con hierbas.","Un tubo de metal con un filtro."],"The third paragraph defines it."),
])
grammar(S(n),'grammar.b2.paraguay.05.el-que-terere','Which One? Relative Clauses with Preposition + El Que',
"You know *un servicio del que dependen muchas personas* from B1 Unit 20: in a relative clause the preposition goes before *el que*, *la que*, *los que* or *las que*. They help to describe the objects and the music of Paraguay: the cup in which tereré is served, the genre of which Flores is the creator.",
[["La guampa es el vaso en el que se sirve el tereré.","*en el que*: in which (*vaso* is masculine)"],["La guarania es un género del que Flores es considerado el creador.","*del que*: of which (*de* + *el que*)"],["El tereré es una bebida con la que se comparte tiempo entre amigos.","*con la que*: with which (*bebida* is feminine)"],["Estas son las hierbas con las que se prepara el tereré.","*con las que*: with which (plural feminine)"]],
'Preposition + el que',
[("La guampa es el vaso en el que se sirve el tereré.","The guampa is the cup in which tereré is served."),("La guarania es un género del que Flores es considerado el creador.","The guarania is a genre of which Flores is considered the creator."),("El tereré es una bebida con la que se comparte tiempo entre amigos.","Tereré is a drink with which people spend time together."),("Estas son las hierbas con las que se prepara el tereré.","These are the herbs with which tereré is prepared.")],
"Match the article to the noun (*el vaso*: *en el que*; *la bebida*: *con la que*) and keep the preposition the verb needs. Without the preposition the sentence is wrong: not *el vaso que se sirve el tereré*.")
vocab(S(n),'Tereré and guarania',[('tereré','cold mate drink of Paraguay','noun'),('guampa','cup made of horn or wood for tereré','noun'),('bombilla','metal straw with a filter','noun'),('arpa','harp','noun'),('guarania','slow Paraguayan musical genre','noun'),('yerba','yerba mate (herb for the drink)','noun')])
T='relativas-preposicion-el-que'
ex=[
mc(I(n,1),"Which sentence correctly says that the guampa is the cup in which tereré is served?",["La guampa es el vaso en el que se sirve el tereré.","La guampa es el vaso en la que se sirve el tereré.","La guampa es el vaso que se sirve el tereré."],0,T),
fb(I(n,2),"La guarania es un género del __ Flores es considerado el creador.","que","The guarania is a genre of which Flores is considered the creator.",T),
sb(I(n,3),"El tereré es una bebida con la que se comparte tiempo entre amigos.","Tereré is a drink with which people spend time together as friends.",T),
mt(I(n,4),[["el tereré","cold mate drink"],["la guampa","cup of horn or wood"],["la bombilla","metal straw with a filter"],["el arpa","harp"]],V),
dc(I(n,5),[("Meg","¿Qué es la guarania?"),("Carlos","_____"),("Meg","Quiero escucharla.")],["Una música lenta creada por Flores.","Una bebida fría que se prepara con yerba.","Un árbol del Chaco con madera muy dura."],0,V,cat='dialogue'),
rdg(I(n,6),"How is the tereré usually drunk, according to the text?",["En grupo, y la guampa pasa de mano en mano.","Solo, en la cama, con la bombilla.","En un estadio, con una bombilla de papel."],0),
]
std(n,'Paraguay: tereré and the guarania',ex)

# ---------- consolidation
n='consolidation'
ex=[
mc(I(n,1),"You want to correct the idea that Spanish is the only official language in Paraguay. Which sentence does that?",["En realidad, Paraguay tiene dos lenguas oficiales.","Apenas, Paraguay tiene dos lenguas oficiales.","Propiamente dicho, Paraguay tiene dos lenguas oficiales."],0,'stance-adverbs'),
fb(I(n,2),"Los guaraníes ya tenían su lengua; sin __, el español llegó a ser la lengua oficial.","embargo","The Guaraní already had their language; however, Spanish became the official language.",'contrast-concession-connectors'),
mc(I(n,3),"Which sentence says that the capital was occupied by Brazilian troops?",["La capital fue ocupada por tropas brasileñas.","La capital fue ocupado por tropas brasileñas.","La capital fue ocupada de tropas brasileñas."],0,'ser-passive'),
fb(I(n,4),"Los menonitas llegaron en 1927; a __ de eso, el Chaco tiene pocos habitantes.","propósito","The Mennonites arrived in 1927; speaking of that, the Chaco has few inhabitants.",'marcadores-digresion'),
mc(I(n,5),"Which sentence says that the bombilla is the straw with which tereré is drunk?",["La bombilla es el tubo con el que se bebe el tereré.","La bombilla es el tubo con la que se bebe el tereré.","La bombilla es el tubo que se bebe el tereré."],0,'relativas-preposicion-el-que'),
mt(I(n,6),[["el guaraní","indigenous language of Paraguay"],["la reducción","Jesuit mission settlement"],["el quebracho","very hard wood tree"],["la guarania","slow Paraguayan genre"]],V),
rdg(I(n,7),"According to the readings of this unit, when was the Triple Alliance War?",["De 1864 a 1870.","De 1932 a 1935.","De 1927 a 1938."],0),
sb(I(n,8),"Aunque la iglesia quedó sin terminar, hoy es patrimonio de la humanidad.","Although the church was left unfinished, it is a world heritage site today.",'contrast-concession-connectors'),
]
exfile(S(n),ex)
d=rd('lessons/b2/b2-paraguay-consolidation.json')
d['title']='Paraguay: review of languages, missions, the war, the Chaco and tereré'
for s in d['sections']:
    if s['type']=='goal': s['items']=["I can review stance adverbs, contrast connectors, the passive, side remarks and relative clauses on Paraguayan topics.","I can use the words for Guaraní, the missions, the war, the Chaco and tereré.","I can read about Paraguay and answer questions about what the texts say."]
    if s['type']=='checklist': s['items']=["I can correct an assumption about Guaraní and Spanish with stance adverbs such as *en realidad* and *en rigor*.","I can set two views of the Jesuit missions side by side with *sin embargo*, *no obstante* and *aunque*.","I can say what was signed, taken or occupied in the Triple Alliance War with *ser* + participle.","I can add a side remark about the Chaco with *por cierto* or *a propósito de* and come back to my point.","I can describe tereré and the guarania with *en el que*, *con la que* and *del que*."]
wr('lessons/b2/b2-paraguay-consolidation.json',d)
