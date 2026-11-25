import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
exec(open('/home/user/parlour-read-a/.scratch/u2b.py').read().split("# ---------- 02")[0])
# ---------- 04
s='b2-mexiconorte-04'
items=["I can use a preposition + el que / la que / los que / las que to describe places, songs and people on the border.",
"I can match the article to the noun, as in la garita por la que cruzan.",
"I can say what the border is like and what a corrido is.",
"I can use the lesson's words for the border crossing and the corrido."]
lesson2(s,"The border: two cultures side by side","Use relative clauses with a preposition (en el que, por la que) to describe the border, its twin cities and the corrido.","relative clauses with a preposition (recap)",items)
story_update(s,"Una frontera de dos culturas","The border between Mexico and the United States is more than 3,000 km long; the text describes the twin cities, the San Ysidro crossing and the corrido, a song in which stories are told.",[
"La frontera entre México y Estados Unidos mide más de tres mil kilómetros. En varios lugares, las ciudades de los dos países están una al lado de la otra: Tijuana y San Diego, Ciudad Juárez y El Paso. La garita de San Ysidro, en Tijuana, es uno de los cruces terrestres más transitados del mundo. Muchas personas cruzan allí cada día para trabajar, estudiar o visitar a su familia.",
"La frontera no es solo una línea en el mapa: es un lugar en el que se mezclan dos culturas. Muchos habitantes hablan español e inglés y pasan de un idioma a otro en la misma conversación. Hay familias con parientes a los dos lados, y por eso la frontera aparece también en la música. El corrido es un género musical en el que se cuentan historias de migrantes, de viajes y de la vida en la frontera.",
"La migración es el tema del que más se habla en esta región, y las opiniones sobre cómo manejarla son muy distintas, tanto en México como en Estados Unidos."])
vocab_update(s,"The border: two cultures side by side: vocabulary",[
("la garita","checkpoint, border booth","noun"),("el cruce","crossing","noun"),("el corrido","corrido, narrative ballad","noun"),("cotidiano","daily, everyday","adjective")])
grammar_update(s,"Relative Clauses with a Preposition on the Border",[
T("What you already know","You know *un servicio del que dependen muchas personas* and *el edificio en el que vivimos* from B1 Unit 20: when a relative clause needs a preposition, the preposition goes before *el que, la que, los que* or *las que*, matching the noun. On the border this pattern is everywhere: the checkpoint *por la que* people cross, the song *en la que* stories are told, the city *en la que* two cultures mix."),
TAB("Preposition + article + que",[
["por + la que","La garita por la que cruzan miles de personas está en Tijuana. (The checkpoint through which thousands of people cross is in Tijuana.)"],
["en + el que","El corrido es un género en el que se cuentan historias. (The corrido is a genre in which stories are told.)"],
["en + la que","Tijuana es una ciudad en la que se mezclan dos culturas. (Tijuana is a city in which two cultures mix.)"],
["de + los que","Los vecinos con los que hablé viven en El Paso. (The neighbours I talked to live in El Paso.)"]]),
T("Two things to watch","Match the article to the noun it replaces (*la garita* gives *la que*, *los parientes* gives *los que*) and keep the preposition the verb needs (*hablar con*: *los vecinos con los que hablé*). Do not drop the preposition: not *una canción que se cuentan historias*."),
EX("In context",[
("La garita por la que cruzan miles de personas está en Tijuana.","The checkpoint through which thousands of people cross is in Tijuana."),
("El corrido es una canción en la que se cuentan historias de migrantes.","The corrido is a song in which stories of migrants are told."),
("Tijuana es una ciudad en la que se mezclan dos culturas.","Tijuana is a city in which two cultures mix."),
("La migración es el tema del que más se habla en la frontera.","Migration is the subject people talk about most on the border."),
("Los parientes con los que habla viven al otro lado de la frontera.","The relatives he talks to live on the other side of the border.")]),
TIP("*Lo que* stands for a whole idea (*lo que más preocupa*), while *el que, la que* replace a noun: *la ciudad en la que vivo*.")])
ex_write(s,[
match2(s+'.ex01',[("la garita","checkpoint, border booth"),("el cruce","crossing"),("el corrido","corrido, narrative ballad"),("cotidiano","daily, everyday")]),
mc(s+'.ex02',"Which option completes the sentence: La garita por ____ cruzan miles de personas está en Tijuana?",[
"la que","el que","las que"],RL),
fill(s+'.ex03',"El corrido es una canción en la ____ se cuentan historias de la frontera.","que","The corrido is a song in which stories of the border are told.",RL),
build(s+'.ex04',["Tijuana","es","una","ciudad","en","la","que","se","mezclan","dos","culturas."],"Tijuana is a city in which two cultures mix.",RL),
dial(s+'.ex05',[("Antropóloga","¿Qué es un corrido?"),("Investigador","_____"),("Antropóloga","Entonces es una forma de contar la vida de cada día.")],[
"Es una canción en la que se cuentan historias de migrantes.",
"Es una canción en el que se cuentan historias de migrantes.",
"Es una canción que se cuentan historias de migrantes."],RL),
dict_(s+'.ex06',"La frontera es un lugar en el que se mezclan dos culturas.","The border is a place in which two cultures mix.",RL)])
# ---------- 05
s='b2-mexiconorte-05'
items=["I can use se + a third-person verb to say what is made, exported or agreed in the north, as in Se fabrican vehículos.",
"I can make the verb agree with the plural noun: se exportan vehículos, not se exporta vehículos.",
"I can say what NAFTA and the T-MEC are and what the maquiladoras do.",
"I can use the lesson's words for factories, tariffs and treaties."]
lesson2(s,"Treaties, maquiladoras and nearshoring","Use the passive with se to say what is made, exported and agreed in the factories of northern Mexico.","passive with se (recap)",items)
story_update(s,"Del TLCAN al T-MEC: las fábricas del norte","Since NAFTA in 1994, replaced by the T-MEC in 2020, northern Mexico has made products for export, mainly to the United States; the text explains maquiladoras and nearshoring.",[
"El Tratado de Libre Comercio de América del Norte, o TLCAN, entró en vigor en 1994 y unió las economías de México, Estados Unidos y Canadá. En 2020 fue sustituido por un nuevo acuerdo, el T-MEC, que prevé una revisión conjunta en 2026. La mayor parte de las exportaciones mexicanas va a Estados Unidos, y gran parte de ellas sale del norte del país.",
"Las primeras maquiladoras, fábricas que ensamblan productos para exportar, aparecieron en la frontera en los años sesenta. Hoy, en ciudades como Monterrey y Saltillo, se fabrican vehículos, aparatos electrónicos y otros productos. En el tratado se establecen reglas sobre aranceles y sobre el origen de las piezas.",
"En los últimos años se habla mucho del nearshoring: algunas empresas han trasladado parte de su producción a México, más cerca de su mercado. Según varios analistas, se han combinado dos razones: las tensiones comerciales y los problemas de transporte durante la pandemia. Para recibir más inversión se necesitan, según esos mismos analistas, más electricidad, más agua y más personal técnico."])
vocab_update(s,"Treaties, maquiladoras and nearshoring: vocabulary",[
("la maquiladora","export assembly plant","noun"),("el arancel","tariff","noun"),("el tratado","treaty","noun"),("el ensamblaje","assembly","noun"),("exportar","to export","verb"),("fabricar","to make, to manufacture","verb")])
grammar_update(s,"The Passive with se in the Factories of the North",[
T("What you already know","You know the passive *se* from B1 Unit 6: *Se busca una persona*, *Se buscan personas*, *En esta oficina se organizan reuniones todos los lunes*. With a noun, the verb agrees with it; with no noun it stays singular (*se trabaja mucho aquí*). The passive *se* is the natural way to talk about trade and industry, where it matters what is made or agreed, not who does it."),
TAB("Singular, plural, no noun",[
["se + singular verb + singular noun","Se firmó un tratado en 1992 y entró en vigor en 1994. (A treaty was signed in 1992 and came into force in 1994.)"],
["se + plural verb + plural noun","Se fabrican vehículos y aparatos electrónicos en el norte. (Vehicles and electronic devices are made in the north.)"],
["se + singular verb, no noun","Se trabaja mucho en las fábricas. (People work a lot in the factories.)"]]),
T("The agreement to watch","The noun that follows is the subject, so the verb agrees with it: *se exportan vehículos*, never *se exporta vehículos*. With a person as object, the verb stays singular and takes *a*: *Se contrató a los operarios*. When you stress the product, you can put it first: *Los vehículos se exportan a Estados Unidos*."),
EX("In context",[
("En el norte se fabrican vehículos y aparatos electrónicos.","In the north vehicles and electronic devices are made."),
("En el tratado se establecen reglas sobre los aranceles.","In the treaty rules about tariffs are established."),
("Se exportan vehículos a Estados Unidos.","Vehicles are exported to the United States."),
("Con el tratado se redujeron los aranceles entre los tres países.","With the treaty the tariffs between the three countries were reduced."),
("En las maquiladoras se ensamblan productos para exportar.","In the maquiladoras products are assembled for export.")]),
TIP("Ask what the noun after the verb is: if it is plural, the verb is plural. *Se habla español* but *Se hablan dos idiomas*.")])
ex_write(s,[
match2(s+'.ex01',[("la maquiladora","export assembly plant"),("el arancel","tariff"),("el tratado","treaty"),("el ensamblaje","assembly")]),
mc(s+'.ex02',"Which sentence says that vehicles are exported to the United States, with the verb in the right form?",[
"Se exportan vehículos a Estados Unidos.",
"Se exporta vehículos a Estados Unidos.",
"Exportan se vehículos a Estados Unidos."],PR),
fill(s+'.ex03',"En las maquiladoras se ____ aparatos electrónicos para exportar.","fabrican","Electronic devices for export are made in the maquiladoras.",PR,hint="fabricar, present"),
build(s+'.ex04',["En","el","tratado","se","establecen","reglas","sobre","los","aranceles."],"In the treaty rules on tariffs are established.",PR),
dial(s+'.ex05',[("Empresaria","¿Qué se fabrica en el norte de México?"),("Consultor","_____"),("Empresaria","Entonces el norte es muy importante para la industria.")],[
"Se fabrican vehículos y aparatos electrónicos.",
"Se fabrica vehículos y aparatos electrónicos.",
"Fabrican se vehículos y aparatos electrónicos."],PR),
dict_(s+'.ex06',"Con el tratado se redujeron los aranceles entre los tres países.","With the treaty the tariffs between the three countries were reduced.",PR)])
# ---------- CONSOLIDATION
s='b2-mexiconorte-consolidation'
items=["I can recall the main facts about northern Mexico: the deserts and canyons, vaquero culture, Monterrey, the border and the factories.",
"I can review the unit's words for the desert, the ranch, the factory and the border.",
"I can use conforme, fronting, si-clauses, relative clauses with a preposition and the passive with se on these topics.",
"I can write a short sentence about the north with a relative clause."]
lesson2(s,"Unit 2 Consolidation","Review the facts and the grammar of the northern Mexico unit: time connectors, fronting, si-clauses, relative clauses and the passive with se.","review of Unit 2 grammar",items)
ex_write(s,[
match2(s+'.ex01',[("la aridez","dryness, aridity"),("el agostadero","grazing land"),("la acería","steelworks"),("la maquiladora","export assembly plant")]),
mc_read(s+'.ex02',"According to the unit's texts, what do many historians say helped to form a strong regional identity in the north?",[
"Que la capital estaba lejos, el clima era duro y el gobierno estaba poco presente.",
"Que la capital estaba muy cerca y mandaba en todos los pueblos del norte.",
"Que llovía mucho en toda la región y no hacía falta ayuda de otras zonas."]),
mc(s+'.ex03',"Which sentence says what would happen if there were more rain?",[
"Si hubiera más lluvia, el problema del agua sería menor.",
"Si habría más lluvia, el problema del agua sería menor.",
"Si hubiera más lluvia, el problema del agua fuera menor."],HY),
fill(s+'.ex04',"____ crecen las ciudades del norte, la falta de agua preocupa más.",None,"As the cities of the north grow, the lack of water causes more concern.",CO,answers=["Conforme","A medida que"]),
build(s+'.ex05',["Muy","larga","era","la","jornada","de","los","vaqueros."],"The vaqueros' working day was very long.",FR),
dial(s+'.ex06',[("Antropóloga","¿Qué es la garita de San Ysidro?"),("Investigador","_____"),("Antropóloga","Entonces es un lugar muy importante para muchas familias.")],[
"Es una garita por la que cruzan muchas personas cada día.",
"Es una garita por el que cruzan muchas personas cada día.",
"Es una garita que cruzan por muchas personas cada día."],RL),
dict_(s+'.ex07',"En el norte se fabrican vehículos que se exportan a Estados Unidos.","In the north vehicles are made that are exported to the United States.",PR),
write(s+'.ex08',[("Say that the corrido is a song in which stories are told. Use 'en la que'.","El corrido es una canción en la que se cuentan historias.")],RL)])
