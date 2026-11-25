import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
V='b2-ecuador-vocab'
def unit(stem,n): return f'{stem}-0{n}'
S='b2-ecuador'

# ---------- 01
s=f'{S}-01'
gr(s,"The Avenue of Volcanoes: Relative Clauses",
 "You know relative clauses with *que* and *quien* from B1 Unit 5. A relative clause adds information about a noun: *que* works for people and things, and *quien* can follow a comma when the noun is a person. This is the grammar you need to describe a landscape: which volcano, which valley, which city.",
 [("Humboldt es el naturalista que visitó la región en 1802.","*que* = who: it points back to a person"),
  ("El Cotopaxi es un volcán que sigue activo.","*que* = that/which: it points back to a thing"),
  ("Humboldt, quien midió las montañas, dibujó las plantas por altitud.","*quien* after a comma: extra information about a person"),
  ("El Chimborazo es la montaña que Humboldt intentó subir.","*que* can be the object: the mountain (that) Humboldt tried to climb")],
 [("Quito es la ciudad que está al pie del volcán Pichincha.","Quito is the city that lies at the foot of the Pichincha volcano."),
  ("El páramo es un paisaje que guarda el agua.","The páramo is a landscape that stores water."),
  ("Humboldt, quien visitó Ecuador en 1802, dibujó las plantas por altitud.","Humboldt, who visited Ecuador in 1802, drew the plants by altitude."),
  ("El volcán que se ve desde Quito es el Pichincha.","The volcano you can see from Quito is the Pichincha.")],
 "English often leaves *that* out (*the volcano we can see*). Spanish never leaves out *que*: *el volcán que vemos*. Do not repeat the noun inside the clause either: *la montaña que Humboldt intentó subir*, not *la montaña que Humboldt la intentó subir*.")
voc(s,"The Ecuadorian highlands",[("el callejón","corridor between two mountain ranges, valley","noun"),("el nevado","snow-capped mountain","noun"),("el estratovolcán","cone-shaped volcano built of layers of lava and ash","noun"),("el páramo","high moorland above the tree line","noun")],"Ecuador: the highlands")
lesson(s,"Ecuador's highlands: the avenue of volcanoes","Describe the volcanoes, cities and moorlands of the Ecuadorian highlands with relative clauses.","relative clauses with que and quien",
 ["I can describe a place or a person with a relative clause (*que*, *quien*).","I can say what the avenue of volcanoes is and what Humboldt did there.","I can use the new words for the highlands: *callejón*, *nevado*, *estratovolcán*, *páramo*."])
story(s,"La avenida de los volcanes","Between two mountain ranges Ecuador has a long valley full of volcanoes, where Humboldt measured peaks in 1802, Quito and Cuenca are protected cities, and the moorlands store water.",
["Entre dos cordilleras paralelas de los Andes, la Occidental y la Real, se extiende en Ecuador el callejón interandino, un valle largo y alto con muchos volcanes. En 1802 el naturalista alemán Alexander von Humboldt recorrió la región, y según la tradición fue él quien la llamó la «avenida de los volcanes». Humboldt midió la altura de las montañas y dibujó cómo cambian las plantas a medida que se sube.",
 "El volcán más conocido del callejón es el Chimborazo, un nevado que hace muchos siglos no entra en erupción y que mide 6.263 metros. Humboldt intentó subirlo en 1802, pero no llegó a la cumbre. Como la Tierra es más ancha en el ecuador, la cumbre del Chimborazo es el punto de la superficie terrestre más alejado del centro del planeta, aunque no es la montaña más alta sobre el nivel del mar.",
 "Al sur de Quito está el Cotopaxi, un estratovolcán de forma casi perfecta que sigue activo y que volvió a dar señales de actividad en 2015. Sus erupciones han cubierto los valles de ceniza, pero esa ceniza también hace fértil la tierra.",
 "En el callejón hay dos ciudades que figuran en la lista del Patrimonio Mundial de la UNESCO. Quito, a unos 2.800 metros de altura, fue en 1978 uno de los primeros sitios de esa lista; su centro histórico conserva iglesias y conventos de la época colonial. Cuenca, en el sur, entró en la lista en 1999 y está atravesada por cuatro ríos.",
 "En las partes altas de la sierra se extiende el páramo, un paisaje de hierbas altas donde hay niebla con frecuencia. El páramo funciona como una esponja: guarda el agua de la lluvia y de la niebla y la deja salir poco a poco hacia los ríos. Por eso se dice que proteger el páramo es proteger el agua."],
[("Who is said to have called the Ecuadorian highland valley the avenue of volcanoes?",["El naturalista Alexander von Humboldt, en 1802.","Los técnicos de la UNESCO, en 1978.","Los agricultores del páramo, en 2015."],"The first paragraph says Humboldt visited in 1802 and, according to tradition, gave the name."),
 ("What is special about the summit of Chimborazo?",["Es el punto de la superficie terrestre más alejado del centro del planeta.","Es la montaña más alta del mundo sobre el nivel del mar.","Es el volcán más activo del callejón."],"The second paragraph explains this with the width of the Earth at the equator."),
 ("Why do people say that protecting the páramo means protecting water?",["Porque el páramo guarda agua y la deja salir poco a poco hacia los ríos.","Porque el páramo es un gran lago en la costa.","Porque el páramo está lleno de volcanes activos."],"The last paragraph compares the páramo to a sponge.")])
ex(s,[
 match([("el callejón","corridor between two mountain ranges"),("el nevado","snow-capped mountain"),("el estratovolcán","cone-shaped volcano"),("el páramo","high moorland")],V),
 fill("El Cotopaxi es un volcán __ sigue activo.","que","Cotopaxi is a volcano that is still active.","relative-clauses"),
 mc("Which sentence says \"Humboldt is the naturalist who visited Ecuador in 1802\"?",["Humboldt es el naturalista que visitó Ecuador en 1802.","Humboldt es el naturalista que lo visitó Ecuador en 1802.","Humboldt es el naturalista que visitaron Ecuador en 1802."],"relative-clauses"),
 build("El Chimborazo es la montaña que Humboldt intentó subir.","Chimborazo is the mountain that Humboldt tried to climb.","relative-clauses"),
 dlg([("Meg","¿Qué es el páramo?"),("Carlos","_____")],["Es un paisaje alto que guarda el agua de la lluvia y de la niebla.","Es una ciudad que tiene cuatro ríos y muchas iglesias.","Es un volcán que hace muchos siglos no entra en erupción."],V),
 dic("Quito es la ciudad que está al pie del volcán Pichincha.","Quito is the city that lies at the foot of the Pichincha volcano.","relative-clauses")])

# ---------- 02
s=f'{S}-02'
gr(s,"The Galápagos: The Passive with Ser",
 "You know the passive with *ser* + past participle from B1 Unit 18: *La ley fue aprobada*. The participle agrees with the thing or person that receives the action, and the doer, if you name it, comes after *por*. The passive is common in writing about history and protected places, because what was done to the place matters more than who did it.",
 [("Las islas fueron declaradas parque nacional en 1959.","*fueron declaradas*: plural and feminine, like *las islas*"),
  ("El archipiélago fue declarado Patrimonio de la Humanidad en 1978.","*fue declarado*: singular and masculine, like *el archipiélago*"),
  ("La reserva marina Hermandad fue creada en 2022.","*fue creada*: feminine singular"),
  ("El libro de Darwin fue publicado en 1859.","*fue publicado*; add *por* + the doer if you want it: *por Darwin*")],
 [("Las islas fueron declaradas parque nacional en 1959.","The islands were declared a national park in 1959."),
  ("El archipiélago fue declarado Patrimonio de la Humanidad en 1978.","The archipelago was declared a World Heritage Site in 1978."),
  ("La reserva marina Hermandad fue creada en 2022.","The Hermandad marine reserve was created in 2022."),
  ("El libro de Darwin fue publicado en 1859.","Darwin's book was published in 1859.")],
 "Check the ending of the participle: *las islas fueron declaradas*, not *declarado*. With *fue* the passive tells what happened at a moment in the past; with *es* or *son* it describes what happens now: *Las especies son protegidas por la ley*.")
voc(s,"The Galápagos Islands",[("el archipiélago","group of islands","noun"),("la especie","species","noun"),("el pinzón","finch, small songbird","noun"),("la iguana","iguana","noun")],"Ecuador: the Galápagos")
lesson(s,"The Galápagos Islands: where Darwin saw nature change","Say what was done to the Galápagos and what Darwin observed there, using the passive with ser.","the passive with ser + past participle",
 ["I can say what was done to a place with the passive (*fue declarada*, *fueron creadas*).","I can say what Darwin did in the Galápagos and how the islands are protected today.","I can use the new words for the islands: *archipiélago*, *especie*, *pinzón*, *iguana*."])
story(s,"Las islas Galápagos","The Galápagos are volcanic islands far out in the Pacific where Darwin spent a few weeks in 1835, where many animals live nowhere else, and which have been protected since 1959.",
["El archipiélago de Galápagos está en el océano Pacífico, a unos mil kilómetros de la costa de Ecuador. Las islas nacieron de erupciones volcánicas y nunca estuvieron unidas al continente. En algunas, como Fernandina e Isabela, hay volcanes activos. El nombre del archipiélago viene de los galápagos, las tortugas gigantes que viven en sus islas.",
 "En septiembre de 1835 llegó a las islas el barco británico Beagle, con el joven naturalista Charles Darwin, que tenía veintiséis años. Darwin pasó unas cinco semanas en el archipiélago y observó que algunas plantas y animales eran distintos de una isla a otra. Años después, en 1859, fue publicado su libro El origen de las especies, donde explicó la teoría de la selección natural.",
 "Muchos animales de Galápagos solo se encuentran allí. Las iguanas marinas son los únicos lagartos del mundo que buscan su comida en el mar, donde comen algas. Los pinzones, unos pájaros pequeños que hoy se llaman pinzones de Darwin, tienen picos de formas distintas según lo que comen.",
 "Las islas fueron declaradas parque nacional en 1959, y en 1978 el archipiélago fue incluido entre los primeros sitios de la lista del Patrimonio Mundial de la UNESCO. Hoy la mayor parte de la superficie de tierra de las islas forma parte del parque nacional.",
 "El mar que rodea las islas también es muy rico. Cerca del archipiélago se encuentran corrientes de agua fría y de agua cálida, y por eso viven allí muchísimos peces, tiburones y otros animales marinos. En 2022 fue creada la reserva marina Hermandad, que protege unos 60.000 kilómetros cuadrados de mar al norte de las islas."],
[("How long did Darwin stay in the Galápagos in 1835?",["Unas cinco semanas.","Más de diez años.","Solo un día."],"The second paragraph says he spent about five weeks there."),
 ("What is special about the marine iguanas?",["Son los únicos lagartos del mundo que buscan su comida en el mar.","Son las tortugas gigantes que dieron nombre a las islas.","Son los pájaros que tienen picos de formas distintas."],"The third paragraph describes the marine iguanas."),
 ("What happened to the islands in 1959?",["Fueron declaradas parque nacional.","Fue publicado el libro de Darwin.","Llegó el barco Beagle."],"The fourth paragraph gives the year of the national park.")])
ex(s,[
 match([("el archipiélago","group of islands"),("la especie","species"),("el pinzón","finch"),("la iguana","iguana")],V),
 fill("Las islas __ declaradas parque nacional en 1959.","fueron","The islands were declared a national park in 1959.","ser-passive"),
 mc("Which sentence says \"Darwin's book was published in 1859\"?",["El libro de Darwin fue publicado en 1859.","El libro de Darwin fue publicada en 1859.","El libro de Darwin fueron publicado en 1859."],"ser-passive"),
 build("La reserva marina Hermandad fue creada en 2022.","The Hermandad marine reserve was created in 2022.","ser-passive"),
 dlg([("Meg","¿Qué animal es especial en Galápagos?"),("Carlos","_____")],["La iguana marina, que busca su comida en el mar.","El pinzón, que vive en los volcanes activos.","La especie que llegó con el barco Beagle."],V),
 dic("El archipiélago fue declarado Patrimonio de la Humanidad en 1978.","The archipelago was declared a World Heritage Site in 1978.","ser-passive")])

# ---------- 03
s=f'{S}-03'
gr(s,"The CONAIE: Retelling with Time and Place Words",
 "You know *ese día*, *el día anterior*, *al día siguiente* and *allí* from B2 Unit 17: they replace *hoy*, *ayer*, *mañana* and *aquí* when you retell what someone said. The verb also moves back, as in *dijo que* from B1 Unit 13. You need this whenever you retell what a person said about a past event.",
 [("Carlos dijo: «Hoy leo sobre la CONAIE».","Carlos dijo que ese día leía sobre la CONAIE. (*hoy* → *ese día*)"),
  ("Meg dijo: «Ayer leí sobre el levantamiento».","Meg dijo que el día anterior había leído sobre el levantamiento. (*ayer* → *el día anterior*)"),
  ("Carlos dijo: «Mañana busco más información».","Carlos dijo que al día siguiente buscaría más información. (*mañana* → *al día siguiente*)"),
  ("Meg dijo: «Aquí empezó el levantamiento».","Meg dijo que allí había empezado el levantamiento. (*aquí* → *allí*)")],
 [("Carlos dijo que ese día leía sobre la CONAIE.","Carlos said that that day he was reading about the CONAIE."),
  ("Meg dijo que el día anterior había leído sobre el levantamiento de 1990.","Meg said that the day before she had read about the 1990 uprising."),
  ("Carlos dijo que al día siguiente buscaría más información.","Carlos said that the next day he would look for more information."),
  ("Meg dijo que allí había empezado el levantamiento.","Meg said that the uprising had begun there.")],
 "Ask yourself where and when you are speaking now. If you retell the same day, in the same place, the words can stay: *Dijo que llegaba hoy*. If not, move them.")
voc(s,"The indigenous movement",[("el levantamiento","uprising","noun"),("la nacionalidad","people, nation (used of indigenous peoples in Ecuador)","noun"),("plurinacional","plurinational, made up of several nations","adjective"),("el combustible","fuel","noun"),("indígena","indigenous","adjective")],"Ecuador: the indigenous movement")
lesson(s,"Ecuador's indigenous movement: the CONAIE and the 1990 uprising","Retell what people said about the CONAIE and its uprisings, shifting time and place words.","shifting time and place words in reported speech",
 ["I can retell what someone said, shifting the time and place words (*ese día*, *el día anterior*, *allí*).","I can say what the CONAIE is and what happened in 1990.","I can use the new words for the movement: *levantamiento*, *nacionalidad*, *plurinacional*, *combustible*."])
story(s,"La CONAIE y el levantamiento de 1990","Ecuador's indigenous organisations founded the CONAIE in 1986, led a national uprising in 1990 and later protests, and the 2008 constitution calls Ecuador a plurinational state.",
["Los pueblos indígenas de Ecuador viven sobre todo en la sierra y en la Amazonía, y hablan lenguas como el kichwa y el shuar. Hasta la reforma agraria de 1964, muchas familias indígenas de la sierra trabajaban en haciendas ajenas.",
 "En 1986 se fundó la CONAIE, la Confederación de Nacionalidades Indígenas del Ecuador, que reúne a organizaciones de la sierra, la Amazonía y la costa. Allí la palabra nacionalidad se usa para hablar de los pueblos indígenas con su lengua y su cultura.",
 "En junio de 1990 comenzó el llamado levantamiento del Inti Raymi. Durante varios días miles de personas bloquearon caminos y marcharon hacia las ciudades. Entre sus demandas estaban la entrega de tierras, la educación en lenguas indígenas y el reconocimiento de Ecuador como un país de varias nacionalidades.",
 "Desde entonces hubo otras movilizaciones importantes. En enero de 2000, junto con un grupo de militares, la CONAIE participó en las protestas que terminaron con la salida del presidente Jamil Mahuad. En octubre de 2019 y en junio de 2022 hubo protestas contra el aumento del precio de los combustibles; duraron varios días y terminaron con acuerdos con el gobierno.",
 "En 1995 nació el movimiento político Pachakutik, ligado a la CONAIE, que ha presentado candidatos en elecciones nacionales y locales. La Constitución de 2008 define a Ecuador como un Estado intercultural y plurinacional, y reconoce el kichwa y el shuar, junto con el castellano, como idiomas oficiales de relación intercultural."],
[("When did the Inti Raymi uprising begin?",["En junio de 1990.","En enero de 2000.","En octubre de 2019."],"The third paragraph gives June 1990."),
 ("What does the CONAIE bring together?",["Organizaciones indígenas de la sierra, la Amazonía y la costa.","Solo a empresas de petróleo de Quito.","Solo a militares y presidentes."],"The second paragraph says it brings together organisations from the three regions."),
 ("What does the 2008 constitution say about Ecuador?",["Que es un Estado intercultural y plurinacional.","Que tiene un solo idioma oficial.","Que no reconoce el kichwa ni el shuar."],"The last paragraph describes the constitution.")])
ex(s,[
 match([("el levantamiento","uprising"),("la nacionalidad","indigenous people with its own language and culture"),("plurinacional","made up of several nations"),("el combustible","fuel")],V),
 fill("Carlos dijo que el día __ había leído sobre la CONAIE.","anterior","Carlos said that the day before he had read about the CONAIE.","discurso-indirecto-deicticos",hint="he said ayer"),
 mc("Meg says: \"Aquí empezó el levantamiento.\" Which sentence retells this later, somewhere else?",["Meg dijo que allí había empezado el levantamiento.","Meg dijo que aquí había empezado el levantamiento.","Meg dijo que allí empezaría el levantamiento."],"discurso-indirecto-deicticos"),
 build("Meg dijo que el día anterior había leído sobre el levantamiento.","Meg said that the day before she had read about the uprising.","discurso-indirecto-deicticos"),
 dlg([("Meg","¿Qué es la CONAIE?"),("Carlos","_____")],["Es una organización de pueblos indígenas de Ecuador.","Es un volcán que sigue activo cerca de Quito.","Es una reserva marina al norte de Galápagos."],V),
 dic("Carlos dijo que ese día había leído sobre el levantamiento de 1990.","Carlos said that that day he had read about the 1990 uprising.","discurso-indirecto-deicticos")])

# ---------- 04
s=f'{S}-04'
gr(s,"The 2008 Constitution: The Fact That...",
 "You know *el hecho de que* from B2 Unit 6: you start a sentence with a fact that both people already know and then comment on it, so the verb after *que* is in the subjunctive. The 2008 constitution and the rights of nature are full of such facts that people comment on.",
 [("El hecho de que la naturaleza tenga derechos es nuevo para muchos países.","present subjunctive: *tenga*; the comment agrees with *el hecho* (singular)"),
  ("El hecho de que el pueblo aprobara el texto le dio apoyo.","imperfect subjunctive after a past comment: *aprobara*"),
  ("El hecho de que los jueces hayan aceptado el caso es importante.","perfect subjunctive: *hayan aceptado*"),
  ("El hecho de que un río tenga derechos no significa que nadie pueda usarlo.","*no significa que* + subjunctive, as in B2 Unit 6")],
 [("El hecho de que la naturaleza tenga derechos es una idea de la Constitución de 2008.","The fact that nature has rights is an idea of the 2008 constitution."),
  ("El hecho de que el pueblo aprobara el texto en un referéndum fue importante.","The fact that the people approved the text in a referendum was important."),
  ("El hecho de que los jueces hayan aceptado el caso es importante para los defensores del bosque.","The fact that the judges have accepted the case is important for the defenders of the forest."),
  ("El hecho de que un río tenga derechos no significa que nadie pueda usarlo.","The fact that a river has rights does not mean that nobody can use it.")],
 "Always write *el hecho de que*, with *de*. The comment agrees with *el hecho*, so it is singular: *es importante*, not *son importantes*.")
voc(s,"Constitution and courts",[("el referéndum","referendum","noun"),("el juez","judge","noun"),("la asamblea","assembly","noun"),("el derecho","right; law","noun")],"Ecuador: the 2008 constitution")
lesson(s,"Ecuador's 2008 constitution: the rights of nature","Comment on the 2008 constitution and the rights of nature with el hecho de que.","el hecho de que with the subjunctive",
 ["I can comment on a known fact with *el hecho de que* + subjunctive.","I can say how the 2008 constitution was approved and what it says about nature.","I can use the new words for law: *referéndum*, *juez*, *asamblea*, *derecho*."])
story(s,"La Constitución de 2008 y la naturaleza","Ecuador approved a new constitution by referendum in 2008 that speaks of buen vivir and gives rights to nature, which courts have applied in cases such as Vilcabamba and Los Cedros, while critics say the rights are often not respected.",
["En 2007 los ecuatorianos eligieron una Asamblea Constituyente, que trabajó en la ciudad de Montecristi, en la costa, y redactó una nueva constitución. El 28 de septiembre de 2008 el texto fue aprobado en un referéndum, y entró en vigor el 20 de octubre de 2008.",
 "La Constitución de 2008 habla del sumak kawsay, una expresión kichwa que suele traducirse como «buen vivir». La idea es que el desarrollo no consiste solo en tener más dinero, sino también en vivir bien con otras personas y en armonía con la naturaleza.",
 "Además, la Constitución dedica varios artículos a los derechos de la naturaleza, a la que llama también Pacha Mama. En resumen, dice que la naturaleza tiene derecho a que se respeten su existencia y la regeneración de sus ciclos vitales, y que cualquier persona o comunidad puede pedir a las autoridades que cumplan esos derechos. Se la considera la primera constitución nacional que reconoce derechos a la naturaleza.",
 "Los jueces ya han aplicado esos artículos. En 2011 un tribunal de la provincia de Loja dio la razón al río Vilcabamba en un caso sobre una carretera que se construía sin estudio ambiental. En diciembre de 2021 la Corte Constitucional decidió, en el caso del bosque protector Los Cedros, que las concesiones mineras en esa zona violaban los derechos de la naturaleza.",
 "No todos opinan que la ley se cumple en la práctica. Algunas organizaciones ambientales dicen que la minería y el petróleo siguen amenazando zonas protegidas; otras personas sostienen que Ecuador necesita esos recursos para su economía."],
[("When was the 2008 constitution approved by referendum?",["El 28 de septiembre de 2008.","El 20 de agosto de 2023.","En junio de 1990."],"The first paragraph gives the referendum date; the constitution came into force on 20 October."),
 ("What does the constitution say about nature?",["Que tiene derechos y que cualquier persona puede pedir que se cumplan.","Que no tiene derechos porque no es una persona.","Que pertenece solo al gobierno de Quito."],"The third paragraph summarises the articles on nature."),
 ("What did the Constitutional Court decide in December 2021?",["Que las concesiones mineras en Los Cedros violaban los derechos de la naturaleza.","Que el río Vilcabamba debía tener una carretera nueva.","Que la Constitución de 2008 no era válida."],"The fourth paragraph describes the Los Cedros case.")])
ex(s,[
 match([("el referéndum","referendum"),("el juez","judge"),("la asamblea","assembly that writes or debates"),("el derecho","right")],V),
 fill("El hecho de que la naturaleza __ derechos no significa que nadie pueda usar un río.","tenga","The fact that nature has rights does not mean that nobody can use a river.","el-hecho-de-que-subjuntivo"),
 mc("Which sentence says \"The fact that the judges have accepted the case is important\"?",["El hecho de que los jueces hayan aceptado el caso es importante.","El hecho que los jueces hayan aceptado el caso es importante.","El hecho de que los jueces hayan aceptado el caso son importantes."],"el-hecho-de-que-subjuntivo"),
 build("El hecho de que el pueblo aprobara el texto en un referéndum fue importante.","The fact that the people approved the text in a referendum was important.","el-hecho-de-que-subjuntivo"),
 dlg([("Meg","¿Qué es un referéndum?"),("Carlos","_____")],["Es una votación en la que los ciudadanos deciden una cuestión importante.","Es un tribunal que decide los casos sobre los ríos.","Es una reunión de personas que escriben una constitución."],V),
 dic("El hecho de que la naturaleza tenga derechos es una idea de la Constitución de 2008.","The fact that nature has rights is an idea of the 2008 constitution.","el-hecho-de-que-subjuntivo")])

# ---------- 05
s=f'{S}-05'
gr(s,"Yasuní: Granting a Point with Si Bien",
 "You know *si bien* from B2 Unit 8: it is a formal way to say \"although it is true that\", and it takes the indicative because you confirm the fact before you give the point that matters more. It suits reports and news, which is where the Yasuní debate lives.",
 [("Si bien el Yasuní es un parque nacional, también tiene petróleo bajo el suelo.","*si bien* + indicative: the true point you grant first"),
  ("Si bien la consulta fue clara, su aplicación lleva años.","the main clause says what you really want to say"),
  ("El parque, si bien es grande, tiene zonas muy frágiles.","*si bien* can sit between commas in the middle"),
  ("Si bien muchos votaron a favor, otros piensan distinto.","both clauses are facts, so both verbs are indicative")],
 [("Si bien el Yasuní es un parque nacional, también tiene petróleo bajo el suelo.","Although Yasuní is a national park, it also has oil under the ground."),
  ("Si bien la consulta fue clara, su aplicación lleva años.","Although the vote was clear, applying it is taking years."),
  ("El parque, si bien es grande, tiene zonas muy frágiles.","The park, although it is large, has very fragile areas."),
  ("Si bien muchos votaron a favor, otros piensan distinto.","Although many voted in favour, others think differently.")],
 "Do not add *que* after *si bien*, and do not write *sí bien*. With friends use *aunque*; in a report or an essay *si bien* sounds right.")
voc(s,"Oil and the rainforest",[("el petróleo","oil, petroleum","noun"),("el pozo","well","noun"),("la biodiversidad","biodiversity","noun"),("la consulta","vote, public consultation","noun")],"Ecuador: Yasuní")
lesson(s,"Yasuní: oil, rainforest and the 2023 vote","Talk about the Yasuní park, its oil and the 2023 vote, granting points with si bien.","concessive clauses with si bien and the indicative",
 ["I can grant a point formally with *si bien* + indicative.","I can say what Yasuní is and what Ecuadorians voted on in August 2023.","I can use the new words for the debate: *petróleo*, *pozo*, *biodiversidad*, *consulta*."])
story(s,"Yasuní y la consulta de 2023","Yasuní is an Amazonian park rich in species and with oil beneath it; in August 2023 about 59 % of Ecuadorian voters chose to leave the ITT oil underground, and its application is disputed.",
["El Parque Nacional Yasuní está en la Amazonía ecuatoriana, en las provincias de Orellana y Pastaza. Fue declarado parque nacional en 1979 y en 1989 la UNESCO lo reconoció como reserva de la biosfera. Muchos científicos lo consideran uno de los lugares con más biodiversidad del planeta.",
 "En el parque viven pueblos indígenas como los waorani. Además, los tagaeri y los taromenane viven en aislamiento voluntario, lo que significa que no tienen contacto regular con otras personas. Para proteger su territorio fue creada una zona intangible.",
 "Bajo el suelo del Yasuní hay petróleo. Una parte, el bloque ITT, que toma su nombre de los campos Ishpingo, Tambococha y Tiputini, está dentro del parque. En 2007 el presidente Rafael Correa propuso dejar ese petróleo bajo tierra si otros países daban dinero a cambio. En 2013 el gobierno terminó la iniciativa, porque, según dijo, llegó mucho menos dinero del esperado.",
 "Colectivos ciudadanos, entre ellos Yasunidos, pidieron una consulta popular. La Corte Constitucional la aprobó en 2023, y el 20 de agosto de 2023 los ecuatorianos votaron. Según el resultado oficial, alrededor del 59 % votó a favor de dejar el petróleo del ITT bajo tierra. Varios medios y organizaciones presentaron el resultado como el primer caso en que un país decidía algo así en las urnas.",
 "La consulta ordenó cerrar el bloque. El gobierno del presidente Daniel Noboa, elegido en 2023 y reelegido en abril de 2025, empezó a cerrar pozos en agosto de 2024 y presentó un calendario de cierre que llega hasta 2029; en 2026 la producción seguía. Si bien el gobierno empezó a cerrar pozos, Yasunidos y, en agosto de 2025, Human Rights Watch afirmaron que el resultado de la consulta no se está respetando."],
[("What did Ecuadorians vote on on 20 August 2023?",["Si dejar bajo tierra el petróleo del bloque ITT.","Si construir un aeropuerto en Galápagos.","Si cambiar el nombre del parque nacional."],"The fourth paragraph describes the vote."),
 ("Who live in voluntary isolation in Yasuní?",["Los tagaeri y los taromenane.","Los técnicos del bloque ITT.","Los científicos de la UNESCO."],"The second paragraph names the peoples in isolation."),
 ("What do Yasunidos and Human Rights Watch say, according to the text?",["Que el resultado de la consulta no se está respetando.","Que el gobierno cerró todos los pozos en 2024.","Que el petróleo del Yasuní ya no existe."],"The last paragraph reports their claim.")])
ex(s,[
 match([("el petróleo","oil"),("el pozo","well"),("la biodiversidad","variety of plant and animal life"),("la consulta","public vote")],V),
 fill("Si __ la consulta fue clara, su aplicación lleva años.","bien","Although the vote was clear, applying it is taking years.","concesivas-si-bien"),
 mc("Which sentence says \"Although the vote was clear, closing the wells takes time\"?",["Si bien el resultado fue claro, cerrar los pozos lleva tiempo.","Si bien que el resultado fue claro, cerrar los pozos lleva tiempo.","Si bien el resultado fuera claro, cerrar los pozos lleva tiempo."],"concesivas-si-bien"),
 build("Si bien el Yasuní es un parque nacional, también tiene petróleo bajo el suelo.","Although Yasuní is a national park, it also has oil under the ground.","concesivas-si-bien"),
 dlg([("Meg","¿Qué es la biodiversidad?"),("Carlos","_____")],["Es la gran variedad de plantas y animales que viven en un lugar.","Es la cantidad de petróleo que hay bajo la tierra.","Es el dinero que un país recibe por una votación."],V),
 dic("Si bien el Yasuní tiene mucha biodiversidad, también tiene petróleo bajo el suelo.","Although Yasuní has great biodiversity, it also has oil under the ground.","concesivas-si-bien")])

# ---------- consolidation
s=f'{S}-consolidation'
ex(s,[
 match([("el callejón","corridor between two mountain ranges"),("el archipiélago","group of islands"),("el levantamiento","uprising"),("el pozo","well")],V),
 fill("La ciudad __ tiene cuatro ríos es Cuenca.","que","The city that has four rivers is Cuenca.","relative-clauses"),
 mc("Which sentence says \"The constitution was approved on 28 September 2008\"?",["La Constitución fue aprobada el 28 de septiembre de 2008.","La Constitución fue aprobado el 28 de septiembre de 2008.","La Constitución fueron aprobada el 28 de septiembre de 2008."],"ser-passive"),
 fill("Meg dijo que __ día había leído sobre el Yasuní.","ese","Meg said that that day she had read about Yasuní.","discurso-indirecto-deicticos",hint="she said hoy",answers=["ese","aquel"]),
 mc("Which sentence says \"The fact that the vote was clear does not mean that it was applied\"?",["El hecho de que el resultado fuera claro no significa que se aplicara.","El hecho que el resultado fuera claro no significa que se aplicara.","El hecho de que el resultado fuera claro no significan que se aplicara."],"el-hecho-de-que-subjuntivo"),
 mc("Which sentence says \"Although the park is protected, it also has oil\"?",["Si bien el parque está protegido, también tiene petróleo.","Si bien que el parque está protegido, también tiene petróleo.","Si bien el parque esté protegido, también tiene petróleo."],"concesivas-si-bien"),
 mc("According to the texts, what happened on 20 August 2023?",["Se votó sobre el petróleo del bloque ITT.","El Beagle llegó a las islas Galápagos.","Empezó el levantamiento del Inti Raymi."],None,cat="reading"),
 {"type":"sentence-order","category":"grammar","sentences":["En 1802 Humboldt recorrió el callejón interandino. [In 1802 Humboldt travelled through the inter-Andean valley.]","En 1835 llegó a Galápagos el barco de Darwin. [In 1835 Darwin's ship reached the Galápagos.]","En 1990 comenzó el levantamiento del Inti Raymi. [In 1990 the Inti Raymi uprising began.]","En 2008 fue aprobada una nueva constitución. [In 2008 a new constitution was approved.]"],"solution":[0,1,2,3],"teaches":["preterito-indefinido"]}])
lesson(s,"Ecuador: Unit Review","Review the highlands, the Galápagos, the indigenous movement, the 2008 constitution and Yasuní, with the grammar you used to talk about them.","review: relative clauses, the ser passive, retelling with time and place words, el hecho de que, si bien",
 ["I can review what I learned about Ecuador, from the volcanoes to Yasuní.","I can use relative clauses, the passive with *ser*, retelling words, *el hecho de que* and *si bien*.","I can put events from 1802 to 2023 in order.","I can say who says what when a matter is disputed."],
 ["I can describe a place with a relative clause (*que*, *quien*).","I can say what was done to a place with the passive (*fue declarado*).","I can retell what someone said, shifting the time and place words.","I can comment on a fact with *el hecho de que* + subjunctive.","I can grant a point formally with *si bien* + indicative."])
