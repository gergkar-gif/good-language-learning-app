import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
U='b2-brazil-amazonia-brasilia-vocab'
CH={}
# ---- 01 Brasília: consecutivas
s='b2-brasilinterior-01'
grammar(s,'grammar.b2.brasilinterior.01.consec','Brasília: So Much That...',
 "You know *tan ... que*, *tanto ... que* and *de tal manera que* from B2 Unit 31: they measure how much, or in what way, something happened, and say what resulted. A planned capital that was built fast and then grew beyond its plan gives you plenty of \"so ... that\" sentences. Here they work on Brasília.",
 "Results in Brasília",
 [("La ciudad se construyó tan rápido que se inauguró en 1960.","*tan* + adverb + *que*: so fast that"),
  ("Llegaron tantos trabajadores que hubo que construir nuevos barrios.","*tantos* + noun + *que*: so many ... that"),
  ("La ciudad creció tanto que hoy vive más gente fuera del Plano Piloto.","verb + *tanto que*: grew so much that"),
  ("Lúcio Costa trazó el plano de tal manera que los ejes forman una cruz.","*de tal manera que*: in such a way that")],
 "In context",
 [("El Congreso es tan conocido que aparece en muchas fotografías.","The Congress is so well known that it appears in many photographs."),
  ("Había tanta gente en la inauguración que las calles estaban llenas.","There were so many people at the inauguration that the streets were full."),
  ("Niemeyer proyectó la catedral de tal modo que la luz entra por el techo.","Niemeyer designed the cathedral in such a way that light enters through the roof.")],
 "*Tan* goes only before an adjective or an adverb and never changes. Before a noun use *tanto* and make it agree (*tantos trabajadores*). After a verb use *tanto*: *creció tanto que ...*.")
x=Ex(s)
x.mc("Which sentence says \"The city grew so much that more people now live outside the Pilot Plan\"?",
 "La ciudad creció tanto que hoy vive más gente fuera del Plano Piloto.",
 ["La ciudad creció tan que hoy vive más gente fuera del Plano Piloto.","La ciudad creció tantos que hoy vive más gente fuera del Plano Piloto."],1,'consecutivas-de-tal-manera')
x.fb("La ciudad se construyó ____ rápido que se inauguró en 1960.","tan","The city was built so fast that it was inaugurated in 1960.",'consecutivas-de-tal-manera')
x.mt([("el plano","plan, layout"),("el eje","axis, main avenue"),("el concurso","competition"),("la catedral","cathedral")],U)
x.read("According to the text, what shape does the plan of Brasília have?",
 "Una cruz, o un avión.",["Un río largo.","Una estrella de mar."],1)
ids=x.write()
vocab(s,"Brasília: plan, axes and competition",[("plano","plan, layout","noun"),("eje","axis, main avenue","noun"),("concurso","competition","noun"),("catedral","cathedral","noun")])
lesson(s,"Brasília: a capital built in the interior","I can say how much, or in what way, something happened and what resulted, with *tan ... que*, *tanto ... que* and *de tal manera que*, about Brasília.","recap: result clauses with tan/tanto ... que and de tal manera que",ids)
n=story(s,"Brasília, la capital del interior","Brasília became the capital on 21 April 1960; Lúcio Costa planned it, Oscar Niemeyer designed its main buildings, and it grew beyond the original plan.",
["Brasília es la capital de Brasil desde el 21 de abril de 1960. Hasta entonces la capital era Río de Janeiro, en la costa. Desde el siglo XIX había propuestas para llevar el gobierno al interior, y el presidente Juscelino Kubitschek las hizo realidad. Su lema era cincuenta años de progreso en cinco.",
 "El plan de la ciudad, el Plano Piloto, es obra del urbanista Lúcio Costa, que ganó el concurso de 1957. Tiene forma de cruz, o de avión, con dos ejes: el Eje Monumental, donde están los ministerios y los edificios del gobierno, y el Eje Rodoviario, con las zonas de viviendas, llamadas superquadras. El arquitecto Oscar Niemeyer proyectó los principales edificios públicos, como el Congreso, el Palacio del Planalto y la catedral.",
 "La ciudad se construyó tan rápido que se inauguró solo unos años después del concurso. Muchos de los trabajadores, llamados candangos, llegaron de otras regiones del país, sobre todo del Nordeste. En 1987 la Unesco declaró Patrimonio Mundial el conjunto urbano.",
 "Con el tiempo, la ciudad creció tanto que hoy vive más gente en las ciudades satélite que en el Plano Piloto. Algunos críticos dicen que el plan está pensado de tal manera que es difícil moverse sin automóvil; otras personas valoran sus espacios abiertos y sus edificios."],
[("When did Brasília become the capital?",["El 21 de abril de 1960.","En 1957.","En 1987."],0,"The first paragraph gives the date."),
 ("Who won the competition for the city plan?",["Lúcio Costa.","Oscar Niemeyer.","Juscelino Kubitschek."],0,"The second paragraph says so."),
 ("Where do more people live today, according to the text?",["En las ciudades satélite.","En el Plano Piloto.","En Río de Janeiro."],0,"The fourth paragraph says so.")])
print(s,n)
CH[s]=chal("The New Capital","You are Carlos. You and Meg are planning a trip and reading about Brasília, and she asks whether the city was built slowly.","Tell Meg that the city was built so fast that it was inaugurated in 1960.",["Say that it was built fast","Use *tan ... que* and give the year"],"La ciudad se construyó tan rápido que se inauguró en 1960.","The city was built so fast that it was inaugurated in 1960.","I can say how much, or in what way, something happened and what resulted, with *tan ... que*, *tanto ... que* and *de tal manera que*, about Brasília.")

# ---- 02 Amazon: cuando/mientras
s='b2-brasilinterior-02'
grammar(s,'grammar.b2.brasilinterior.02.cuando','The Amazon: When and While',
 "You know *cuando* + preterite and *mientras* from A2 Unit 13: *cuando* links an event to the moment another happened, and *mientras* links two things that go on at the same time. The Amazon, with its rubber boom and its river life, is full of \"when\" and \"while\". Here they work on Manaus and Belém.",
 "When and while on the river",
 [("Cuando bajó el precio del caucho, la economía de la región entró en crisis.","*cuando* + preterite: an event, then its result"),
  ("Mientras el caucho valía mucho, Manaus crecía.","*mientras* + imperfect: two things going on together"),
  ("Los pasajeros descansan en hamacas mientras el barco avanza.","*mientras* + present: now, at the same time"),
  ("Cuando llegaron los viajeros a Manaus, vieron el Encuentro de las Aguas.","*cuando* can also open the sentence for a sequence")],
 "In context",
 [("Cuando se inauguró el Teatro Amazonas, Manaus vivía el auge del caucho.","When the Teatro Amazonas was inaugurated, Manaus was living the rubber boom."),
  ("Mientras la lluvia caía, el río subía.","While the rain fell, the river rose."),
  ("Se vende pescado en el mercado mientras la gente compra frutas.","Fish is sold at the market while people buy fruit.")],
 "With *cuando* + preterite, one event follows or triggers another. With *mientras*, both actions continue together, so imperfect (past) or present (now) is normal. When *cuando* opens the sentence, put a comma after its clause.")
x=Ex(s)
x.mc("Which sentence says \"While the rain fell, the river rose\"?",
 "Mientras la lluvia caía, el río subía.",
 ["Cuando la lluvia cayó, el río subía.","Aunque la lluvia caía, el río subía."],2,'cuando-mientras')
x.fb("____ bajó el precio del caucho, la economía de la región entró en crisis.","Cuando","When the price of rubber fell, the economy of the region went into crisis.",'cuando-mientras')
x.mt([("el caucho","rubber"),("la hamaca","hammock"),("el mercado","market"),("la procesión","procession")],U)
x.read("According to the text, in which year was the Teatro Amazonas inaugurated?",
 "En 1896.",["En 1616.","En 2025."],2)
ids=x.write()
vocab(s,"The Amazon: rubber, rivers and markets",[("caucho","rubber","noun"),("hamaca","hammock","noun"),("mercado","market","noun"),("procesión","procession","noun")])
lesson(s,"The Amazon basin: Manaus, Belém and the rivers","I can link two events or two actions in the Amazon with *cuando* and *mientras*.","recap: cuando + preterite and mientras for simultaneous actions",ids)
n=story(s,"Manaus y Belém, ciudades del río","The Amazon basin covers more than six million square kilometres; Manaus grew with rubber, Belém is the gateway at the river mouth, and COP30 was held there in 2025.",
["La cuenca del Amazonas ocupa más de seis millones de kilómetros cuadrados y se reparte entre nueve países y territorios. En Brasil, el río es también una carretera: en muchas zonas se viaja durante días en barcos de dos o tres pisos, con hamacas. Según las estimaciones habituales, el Amazonas lleva al océano Atlántico cerca de la quinta parte del agua dulce que los ríos vierten al mar.",
 "Manaus está en la orilla del río Negro, cerca de donde se une con el Solimões. Allí se ve el llamado Encuentro de las Aguas: durante varios kilómetros, el agua oscura del río Negro y el agua marrón y barrosa del Solimões corren una al lado de la otra sin mezclarse, porque tienen distinta temperatura, velocidad y densidad.",
 "A fines del siglo XIX el caucho hizo rica a Manaus. Mientras el caucho valía mucho en el mercado mundial, la ciudad crecía, y en 1896 se inauguró el Teatro Amazonas. Cuando bajó el precio del caucho, a comienzos del siglo XX, porque se producía en plantaciones de Asia, la economía de la región entró en crisis.",
 "Belém, en la desembocadura del río, se fundó en 1616. Allí está el mercado Ver-o-Peso, donde se venden pescado, hierbas y frutas. Cada octubre, la procesión del Círio de Nazaré reúne a cientos de miles de personas. En noviembre de 2025 Belém fue la sede de la COP30, la conferencia de las Naciones Unidas sobre el cambio climático."],
[("How many countries and territories share the Amazon basin?",["Nueve.","Tres.","Treinta."],0,"The first paragraph says nine."),
 ("Why did the Amazon economy go into crisis in the early 20th century?",["Bajó el precio del caucho, que se producía en plantaciones de Asia.","Se cerró el Teatro Amazonas.","Se secó el río Negro."],0,"The third paragraph explains it."),
 ("Where was COP30 held in November 2025?",["En Belém.","En Manaus.","En Brasília."],0,"The fourth paragraph says so.")])
print(s,n)
CH[s]=chal("Rubber and the Theatre","You are Meg. You and Carlos are watching a documentary about Manaus, and he asks what happened to the city when rubber lost its price.","Tell Carlos what happened to the economy of the region when the price of rubber fell.",["Use *cuando* + preterite","Say the economy went into crisis"],"Cuando bajó el precio del caucho, la economía de la región entró en crisis.","When the price of rubber fell, the economy of the region went into crisis.","I can link two events or two actions in the Amazon with *cuando* and *mientras*.")

# ---- 03 indigenous: haber de
s='b2-brasilinterior-03'
grammar(s,'grammar.b2.brasilinterior.03.haberde','Indigenous Lands: A Formal Duty',
 "You know *haber de* + infinitive from B2 Unit 26, the formal pattern for a duty (*He de reconocer ...*) and for \"was to\" in a story (*había de cambiar ...*). Texts about laws and about history use it. Here it works on indigenous lands and the Xingu park.",
 "haber de + infinitive",
 [("El Estado ha de proteger las tierras indígenas.","a duty: the State must protect"),
  ("Los visitantes han de pedir permiso para entrar en una tierra indígena.","a duty for visitors"),
  ("Los hermanos Villas-Bôas habían de crear el Parque del Xingu en 1961.","in a story: they were to create"),
  ("Aquella decisión había de cambiar la política hacia los pueblos indígenas.","in a story: it was to change")],
 "In context",
 [("La Funai ha de vigilar los territorios de los pueblos aislados.","Funai must watch over the territories of isolated peoples."),
  ("Los poderes públicos han de respetar la Constitución de 1988.","Public authorities must respect the Constitution of 1988."),
  ("El parque había de ser un refugio para varios pueblos.","The park was to be a refuge for several peoples.")],
 "*Haber de* changes with the person (*he de*, *ha de*, *han de*, *habían de*), but *hay que* never does. It is formal: in everyday speech people say *tiene que* or *debe*. Do not leave out *de*.")
x=Ex(s)
x.mc("Which sentence says, formally, \"The State must protect indigenous lands\"?",
 "El Estado ha de proteger las tierras indígenas.",
 ["El Estado ha que proteger las tierras indígenas.","El Estado hay de proteger las tierras indígenas."],1,'perifrasis-haber-de-infinitivo',
 ds={"El Estado ha que proteger las tierras indígenas.":'hay-que'})
x.fb("Los hermanos Villas-Bôas ____ de crear el Parque del Xingu en 1961.","habían","The Villas-Bôas brothers were to create the Xingu Park in 1961.",'perifrasis-haber-de-infinitivo')
x.mt([("la reserva","reserve"),("el pueblo","people, nation"),("el aislamiento","isolation"),("el territorio","territory")],U)
x.read("According to the text, in which year was the Xingu Indigenous Park created?",
 "En 1961.",["En 1988.","En 1943."],0)
ids=x.write()
vocab(s,"Indigenous lands and isolated peoples",[("reserva","reserve","noun"),("pueblo","people, nation","noun"),("aislamiento","isolation","noun"),("territorio","territory","noun")])
lesson(s,"Indigenous lands and peoples in isolation","I can state a duty or a story's \"was to\" formally with *haber de* + infinitive, about indigenous lands.","recap: formal haber de + infinitive",ids)
n=story(s,"Tierras indígenas y pueblos aislados","Brazil's 1988 Constitution recognised indigenous rights to their lands; Funai follows a no-contact policy for isolated peoples, and illegal mining puts pressure on the territories.",
["En la Amazonía brasileña viven pueblos indígenas que casi no tienen contacto con el resto de la sociedad. Según la Funai, el organismo del Estado para los pueblos indígenas, hay registros de más de cien grupos aislados, y de solo una parte se ha confirmado su existencia. Desde 1987 la política de la Funai es no iniciar el contacto: el Estado ha de proteger sus territorios, pero no ha de buscar a esos pueblos.",
 "En 1943 empezó la expedición Roncador-Xingu, en la que participaron los hermanos Orlando, Cláudio y Leonardo Villas-Bôas. Los hermanos defendieron que los indígenas no fueran obligados a abandonar su cultura, y en 1961 se creó el Parque Indígena del Xingu, en el estado de Mato Grosso. Según varios historiadores, fue la primera gran reserva indígena de América Latina.",
 "La Constitución de 1988 reconoce, en sus artículos 231 y 232, los derechos originarios de los indígenas sobre las tierras que ocupan tradicionalmente. Esas tierras son propiedad de la Unión, el Estado federal, y las comunidades tienen el uso exclusivo.",
 "Hoy esas tierras sufren presiones de la minería ilegal de oro, de la tala y de la ocupación ilegal de tierras. En enero de 2023 el gobierno federal declaró una emergencia de salud pública en el territorio yanomami, en el norte del país, donde la minería ilegal se asocia con casos de malaria y desnutrición. Varios estudios indican, además, que hay menos deforestación dentro de las tierras indígenas que fuera de ellas."],
[("What has been Funai's policy towards isolated peoples since 1987?",["No iniciar el contacto con ellos.","Llevarlos a las ciudades.","Abrir escuelas en sus tierras."],0,"The first paragraph says so."),
 ("Which article numbers of the 1988 Constitution does the text mention?",["Los artículos 231 y 232.","Los artículos 1 y 2.","Los artículos 1943 y 1961."],0,"The third paragraph gives them."),
 ("What did the federal government declare in the Yanomami territory in January 2023?",["Una emergencia de salud pública.","Un nuevo parque nacional.","Una fiesta nacional."],0,"The fourth paragraph says so.")])
print(s,n)
CH[s]=chal("The Xingu Park","You are Carlos. You and Meg are preparing a talk on indigenous lands, and she asks what the Villas-Bôas brothers achieved.","Tell Meg that the brothers were to create the Xingu Park in 1961, using the formal pattern.",["Say who the brothers were","Use *habían de* and the year"],"Los hermanos Villas-Bôas habían de crear el Parque del Xingu en 1961.","The Villas-Bôas brothers were to create the Xingu Park in 1961.","I can state a duty or a story's \"was to\" formally with *haber de* + infinitive, about indigenous lands.")

# ---- 04 Cerrado: contrast markers
s='b2-brasilinterior-04'
grammar(s,'grammar.b2.brasilinterior.04.contrast','The Cerrado: Two Sides of Farming',
 "You know *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien* from B2 Unit 30. Each sets one idea against another in its own way. The Cerrado, a savanna that became a farming giant, has a productive side and an environmental side. Here the markers work on the Cerrado.",
 "Contrast markers in the Cerrado",
 [("Durante siglos se consideró un suelo pobre; en cambio, hoy produce mucha soja.","*en cambio*: a comparison, then and now"),
  ("La agricultura no destruyó el Cerrado de golpe; por el contrario, avanzó poco a poco.","*por el contrario*: the opposite of what was said"),
  ("La soja trajo ingresos; no obstante, se perdió gran parte de la vegetación nativa.","*no obstante*: a fact that does not cancel the first"),
  ("El Cerrado produce mucha soja. Ahora bien, de allí nacen también grandes ríos.","*ahora bien*: adds a point that limits what you accepted")],
 "In context",
 [("Los productores defienden la agricultura; los ambientalistas, en cambio, piden proteger lo que queda.","Producers defend farming; environmentalists, on the other hand, ask to protect what is left."),
  ("El Cerrado no es una región vacía; al contrario, tiene muchas especies.","The Cerrado is not an empty region; on the contrary, it has many species."),
  ("La región exporta mucho; no obstante, el agua es un tema de debate.","The region exports a lot; nevertheless, water is a subject of debate.")],
 "*Pero* is the everyday word. These markers usually start a new clause, after a full stop or a semicolon, with a comma after them. Choose by the kind of contrast: a comparison (*en cambio*), the opposite (*por el contrario*, *al contrario*), a fact that does not stop you (*no obstante*) or a limit (*ahora bien*).")
x=Ex(s)
x.mc("Which sentence compares what producers and environmentalists want?",
 "Los productores defienden la agricultura; los ambientalistas, en cambio, piden proteger el bosque.",
 ["Los productores defienden la agricultura; los ambientalistas, es decir, piden proteger el bosque.","Los productores defienden la agricultura; los ambientalistas, por eso, piden proteger el bosque."],0,'contrast-markers',
 ds={"Los productores defienden la agricultura; los ambientalistas, es decir, piden proteger el bosque.":'reformulation-markers',"Los productores defienden la agricultura; los ambientalistas, por eso, piden proteger el bosque.":'porque-y-por-eso'})
x.fb("El Cerrado produce mucha soja. Ahora ____, de allí nacen también grandes ríos.","bien","The Cerrado produces a lot of soy. That said, great rivers also rise there.",'contrast-markers')
x.mt([("la sabana","savanna"),("la soja","soy"),("el suelo","soil"),("el productor","producer")],U)
x.read("According to the text, which institution developed soy varieties for the tropical climate?",
 "Embrapa.",["Funai.","Itamaraty."],1)
ids=x.write()
vocab(s,"The Cerrado: savanna, soy and soil",[("sabana","savanna","noun"),("soja","soy","noun"),("suelo","soil","noun"),("productor","producer","noun")])
lesson(s,"The Cerrado: savanna, farming and water","I can set one idea about the Cerrado against another with *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien*.","recap: contrast markers (en cambio, por el contrario, al contrario, no obstante, ahora bien)",ids)
n=story(s,"El Cerrado, entre la soja y el agua","The Cerrado is a tropical savanna that became a major soy-growing region after the 1970s, with a large loss of native vegetation and a role as a source of rivers.",
["El Cerrado es una sabana tropical que ocupa casi una cuarta parte del territorio de Brasil, unos dos millones de kilómetros cuadrados. Tiene árboles bajos y retorcidos, y sus suelos son rojizos y ácidos. Durante mucho tiempo se consideró una región poco útil para la agricultura. Hoy, en cambio, es una de las grandes regiones agrícolas del mundo.",
 "El cambio empezó en los años setenta. Embrapa, la empresa estatal de investigación agropecuaria creada en 1973, desarrolló variedades de soja adaptadas al clima tropical, y los agricultores corrigieron la acidez del suelo con cal. En los últimos años Brasil ha sido el mayor productor y exportador de soja del mundo, y gran parte de la soja se cultiva en el Cerrado, sobre todo en el estado de Mato Grosso.",
 "No obstante, la expansión agrícola tuvo un costo. Según estimaciones de varios institutos de investigación, cerca de la mitad de la vegetación nativa del Cerrado ya se ha perdido. Ahora bien, esta región importa también por el agua: allí nacen ríos de grandes cuencas del país, como el São Francisco, el Tocantins-Araguaia y el Paraná.",
 "Sobre qué hacer, no hay acuerdo. Los productores defienden la agricultura como motor de las exportaciones; los ambientalistas, en cambio, piden proteger lo que queda del bioma. En el Cerrado viven además comunidades tradicionales, como los geraizeiros, que recogen frutos nativos como el pequi."],
[("What fraction of Brazil's territory does the Cerrado cover, roughly?",["Casi una cuarta parte.","Casi la mitad.","Una centésima parte."],0,"The first paragraph says so."),
 ("When did Embrapa develop soy varieties for the tropics?",["Desde los años setenta.","Desde 1987.","Desde 2025."],0,"The second paragraph says the change began in the 1970s."),
 ("Which rivers does the text name as born in the Cerrado?",["El São Francisco, el Tocantins-Araguaia y el Paraná.","El Amazonas, el Negro y el Solimões.","El Tajo, el Ebro y el Duero."],0,"The third paragraph names them.")])
print(s,n)
CH[s]=chal("Soy and Water","You are Meg. You and Carlos are reading about the Cerrado, and he says it was always a rich farming region.","Correct Carlos: for centuries it was thought poor, but today it produces a lot of soy, as a comparison.",["Say that it was thought poor","Compare it with today"],"Durante siglos se consideró una región pobre; hoy, en cambio, produce mucha soja.","For centuries it was considered a poor region; today, on the other hand, it produces a lot of soy.","I can set one idea about the Cerrado against another with *en cambio*, *por el contrario*, *al contrario*, *no obstante* and *ahora bien*.")

# ---- 05 Itamaraty: contrast concession
s='b2-brasilinterior-05'
grammar(s,'grammar.b2.brasilinterior.05.concession','Itamaraty and Brazil in the World: However, Although',
 "You know *sin embargo* from A2 Unit 28, *aunque* from A2 Unit 28 and *no obstante* from B1 Unit 1: they put a fact against another, or concede a point. Diplomacy and trade agreements are full of \"agreed, but...\". Here they work on Itamaraty and Brazil's present-day links, with dated facts.",
 "However, although, nevertheless",
 [("El acuerdo se firmó en enero de 2026; sin embargo, solo su parte comercial se aplica desde mayo.","*sin embargo*: a contrast, with a comma after it"),
  ("Aunque el puente ya se unió, faltan los accesos.","*aunque* + indicative: a fact you grant"),
  ("Brasil tiene muchas fronteras; no obstante, resolvió casi todas sus disputas por negociación.","*no obstante*: more formal than *sin embargo*"),
  ("Hay defensores del acuerdo; sin embargo, otros lo critican.","two opinions, each attributed")],
 "In context",
 [("El palacio de Itamaraty es de Niemeyer; sin embargo, sus jardines son de Burle Marx.","The Itamaraty palace is by Niemeyer; however, its gardens are by Burle Marx."),
  ("Aunque Lula ganó en octubre de 2026, asumirá el cargo en enero de 2027.","Although Lula won in October 2026, he will take office in January 2027."),
  ("El corredor une dos países; no obstante, todavía no está terminado.","The corridor joins two countries; nevertheless, it is not yet finished.")],
 "*Sin embargo* and *no obstante* usually start a new clause, with a comma after them. *Aunque* joins two clauses in one sentence; with a fact (*aunque llueve*) it takes the indicative. When you give a present-day fact, add the date: the situation can change.")
x=Ex(s)
x.mc("Which sentence correctly contrasts the two facts?",
 "El acuerdo se firmó en enero; sin embargo, su parte comercial se aplica desde mayo.",
 ["El acuerdo se firmó en enero; por eso, su parte comercial se aplica desde mayo.","El acuerdo se firmó en enero; es decir, su parte comercial se aplica desde mayo."],2,'contrast-concession-connectors',
 ds={"El acuerdo se firmó en enero; por eso, su parte comercial se aplica desde mayo.":'porque-y-por-eso',"El acuerdo se firmó en enero; es decir, su parte comercial se aplica desde mayo.":'reformulation-markers'})
x.fb("Brasil tiene muchas fronteras; no ____, resolvió casi todas sus disputas por negociación.","obstante","Brazil has many borders; nevertheless, it settled almost all its disputes by negotiation.",'contrast-concession-connectors')
x.mt([("la frontera","border"),("el acuerdo","agreement"),("el puente","bridge"),("las elecciones","elections")],U)
x.read("According to the text, when does Lula take office after the 2026 elections?",
 "El 5 de enero de 2027.",["El 25 de octubre de 2026.","El 21 de abril de 1960."],0)
ids=x.write()
vocab(s,"Itamaraty, borders and agreements",[("frontera","border","noun"),("acuerdo","agreement","noun"),("puente","bridge","noun"),("elecciones","elections","noun")])
lesson(s,"Itamaraty and Brazil in the world: borders, trade and elections","I can set facts against each other with *sin embargo*, *aunque* and *no obstante*, about Brazil and its neighbours.","recap: contrast and concession connectors (sin embargo, aunque, no obstante)",ids)
n=story(s,"Itamaraty y Brasil en 2026","Itamaraty is Brazil's foreign ministry; Rio Branco settled border disputes in 1902-1912; in 2026 the EU-Mercosur deal, a bioceanic bridge and the presidential election are in the news.",
["Itamaraty es el nombre popular del Ministerio de Relaciones Exteriores de Brasil, por el palacio donde tiene su sede en Brasília. El edificio, con sus arcos y sus espejos de agua, es obra de Oscar Niemeyer, y los jardines son de Roberto Burle Marx. El barón de Rio Branco fue ministro entre 1902 y 1912 y resolvió varias disputas de fronteras con países vecinos por medio de negociaciones y arbitrajes. En 1903, por ejemplo, el Tratado de Petrópolis incorporó a Brasil el territorio de Acre, que estaba en disputa con Bolivia.",
 "En enero de 2026 el Mercosur y la Unión Europea firmaron un acuerdo comercial; sin embargo, solo su parte comercial se aplica de forma provisional desde mayo de 2026, y hay un recurso pendiente ante el Tribunal de Justicia de la Unión Europea. Sus defensores esperan más comercio; sus críticos, entre ellos organizaciones agrarias y ambientales en Europa, temen efectos negativos para la agricultura y los bosques.",
 "El corredor bioceánico por carretera quiere unir Brasil con puertos del Pacífico a través de Paraguay, Argentina y Chile. En julio de 2026 se unieron los dos lados del puente entre Carmelo Peralta, en Paraguay, y Porto Murtinho, en Brasil. Aunque el puente ya está unido, los accesos por carretera terminarán en 2027.",
 "El 25 de octubre de 2026 Luiz Inácio Lula da Silva ganó la segunda vuelta de las elecciones presidenciales, con alrededor del 51,8 % de los votos, frente a Flávio Bolsonaro. Será su cuarto mandato, y asumirá el cargo el 5 de enero de 2027."],
[("Who designed the Itamaraty palace in Brasília?",["Oscar Niemeyer.","Roberto Burle Marx.","El barón de Rio Branco."],0,"The first paragraph says so."),
 ("What did the Treaty of Petrópolis add to Brazil in 1903?",["El territorio de Acre.","El Parque del Xingu.","El puerto de Santos."],0,"The first paragraph says so."),
 ("Between which two places was the bridge of the bioceanic corridor joined in July 2026?",["Carmelo Peralta y Porto Murtinho.","Manaus y Belém.","Brasília y Río de Janeiro."],0,"The third paragraph names them.")])
print(s,n)
CH[s]=chal("Bridge and Roads","You are Carlos. You and Meg are following the news about the bioceanic corridor, and she asks whether the road is finished.","Tell Meg that the bridge was joined in July 2026 but the access roads are due in 2027.",["Say the bridge is joined","Contrast it with the access roads, using *aunque*"],"Aunque el puente se unió en julio de 2026, los accesos terminarán en 2027.","Although the bridge was joined in July 2026, the access roads will be finished in 2027.","I can set facts against each other with *sin embargo*, *aunque* and *no obstante*, about Brazil and its neighbours.")

# ---- consolidation
s='b2-brasilinterior-consolidation'
x=Ex(s)
x.mc("Which sentence says, formally, \"Funai must watch over the territories\"?",
 "La Funai ha de vigilar los territorios.",
 ["La Funai ha que vigilar los territorios.","La Funai hay de vigilar los territorios."],0,'perifrasis-haber-de-infinitivo')
x.mc("Which sentence compares the past and the present of the Cerrado?",
 "Antes se consideró un suelo pobre; hoy, en cambio, produce mucha soja.",
 ["Antes se consideró un suelo pobre; hoy, es decir, produce mucha soja.","Antes se consideró un suelo pobre; hoy, por eso, produce mucha soja."],1,'contrast-markers',
 ds={"Antes se consideró un suelo pobre; hoy, es decir, produce mucha soja.":'reformulation-markers',"Antes se consideró un suelo pobre; hoy, por eso, produce mucha soja.":'porque-y-por-eso'})
x.fb("La ciudad creció ____ que hoy vive más gente en las ciudades satélite.","tanto","The city grew so much that more people now live in the satellite cities.",'consecutivas-de-tal-manera')
x.read("According to the texts, in which year did UNESCO declare Brasília a World Heritage Site?",
 "En 1987.",["En 1960.","En 1957."],1)
ids=x.write()
consolidation2(s,"Review: Brasília, the Amazon, the Cerrado and Itamaraty","Review Brasília, the Amazon basin, indigenous lands, the Cerrado and Itamaraty, with the grammar you used to talk about them.","review: result clauses, cuando and mientras, haber de, contrast markers, contrast and concession connectors",ids)
CH[s]=chal("Brazil's Interior in Review","You are Meg. You and Carlos are preparing a short talk about Brazil's interior, and he asks what you remember about Brasília.","Tell Carlos that the city grew so much that more people live in the satellite cities than in the Pilot Plan.",["Say that the city grew a lot","Use *tanto ... que* for the result"],"La ciudad creció tanto que hoy vive más gente en las ciudades satélite que en el Plano Piloto.","The city grew so much that more people now live in the satellite cities than in the Pilot Plan.","I can review what I learned about Brasília, the Amazon, the Cerrado and Itamaraty.")
challenges(ROOT+'/challenges-brazil-amazonia-brasilia.json',CH)
