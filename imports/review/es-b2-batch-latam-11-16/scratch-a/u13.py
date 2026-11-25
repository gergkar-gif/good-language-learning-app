from lib import *
V='b2-colombia-andes-vocab'
# ---------- 01
s='b2-colombiaandina-01'
paras=[
"En Colombia la cordillera de los Andes se divide en tres ramas: la Occidental, la Central y la Oriental. Entre ellas corren los valles de los ríos Cauca y Magdalena.",
"En las zonas altas de estas montañas, por encima del bosque, está el páramo. Es un paisaje frío y húmedo, con niebla casi todos los días, que se encuentra por encima de los 3000 metros de altura. Se calcula que Colombia tiene la mayor extensión de páramos del mundo.",
"La planta más conocida del páramo es el frailejón, que tiene hojas cubiertas de pelos suaves. Crece muy despacio, unos pocos centímetros al año. Según los científicos, sus hojas atrapan la humedad de la niebla, y el agua baja luego por el suelo hasta los arroyos.",
"El páramo es importante porque guarda agua. Gran parte del agua de Bogotá viene del páramo de Chingaza, y el páramo de Sumapaz, al sur de la capital, se considera el más grande del mundo.",
"Estos lugares están amenazados por la agricultura, el ganado y la minería. Muchas organizaciones ambientales piden leyes que protejan los páramos, y en 2018 el Congreso aprobó una ley sobre ellos. Los campesinos que viven en el páramo dicen que necesitan alternativas que les permitan vivir sin dañar el agua.",
"Buscar un cultivo que no dañe el páramo no es solo un problema ambiental. También es un problema social, porque en esas montañas viven familias."]
put_story(s,"Los páramos de los Andes colombianos","Colombia's Andes have three ranges, and above the forest lie the páramos, cold misty highlands that store water for cities like Bogotá and are threatened by farming, cattle and mining.",paras,[
("According to the text, why are the páramos important?",["Porque guardan agua, y gran parte del agua de Bogotá viene del páramo de Chingaza.","Porque allí se produce la mayor parte del café de Colombia.","Porque allí viven muchas personas de las ciudades grandes."],"The fourth paragraph explains that páramos store water."),
("What does the text say about the frailejón?",["Tiene hojas cubiertas de pelos suaves y crece muy despacio.","Es un animal que vive en la niebla de las montañas.","Es una planta que crece muy rápido en los arroyos."],"The third paragraph describes the plant."),
("What do many environmental organisations ask for, according to the text?",["Leyes que protejan los páramos.","Más minas en las zonas altas.","Más ganado en las montañas."],"The fifth paragraph says so.")])
put_voc(s,"","Páramos and mountain water","Words about Colombia's high Andes",[("el páramo","páramo (high, cold, misty highland)","noun"),("el frailejón","frailejón (plant of the páramo)","noun"),("la niebla","fog, mist","noun"),("el arroyo","stream","noun")])
put_gr(s,"Relative Clauses with the Subjunctive: Laws and Crops That Do Not Exist Yet",[
T("You know relative clauses with *que* and the subjunctive from B2 Unit 13. If you can point at the thing, the verb after *que* is in the indicative; if the thing is only wanted, needed or imagined, or you say it does not exist, the verb goes into the subjunctive. Debates about the páramos are full of such things: laws, crops and guides that people ask for and that may not exist yet.","What you already know"),
TB("Real, or not found yet?",[
["Piden leyes que protejan los páramos.","laws that people want: *protejan* (subjunctive)"],
["Existe una ley que protege los páramos.","a real law: *protege* (indicative)"],
["No hay nadie que conozca todo el páramo.","nobody exists: *conozca* (subjunctive)"],
["Conozco a un guía que conoce el páramo.","a real person: *conoce* (indicative)"]]),
EX("In context",[
("Buscamos un guía que conozca bien el páramo de Chingaza.","We are looking for a guide who knows the Chingaza páramo well."),
("Los campesinos necesitan cultivos que no dañen el agua del páramo.","The farmers need crops that do not harm the water of the páramo."),
("En el páramo hay plantas que guardan el agua de la niebla.","In the páramo there are plants that store the water of the mist."),
("No existe ningún cultivo que no cambie el paisaje.","There is no crop that does not change the landscape.")]),
TIP("Ask one question: can I point at it? If you can name it, see it or hold it, use the indicative. If it is only wanted, needed or imagined, or if you say it does not exist, use the subjunctive. Keep the personal *a* before a person: *Busco a un guía que…*.")])
put_lesson(s,"The páramos: the high mountains of Colombia","Describe the páramos and what people ask for to protect them, with relative clauses and the subjunctive (*leyes que protejan*).","relative clauses with the subjunctive, applied to the páramos",[
"I can say what I am looking for or what does not exist with *que* + subjunctive (*Busco un guía que conozca…*).",
"I can say what the páramos are and why they matter for water.",
"I can use the new words for the páramo, the frailejón, the mist and the stream."])
put_ex(s,[
match(s+'.ex01',[["el páramo","páramo (high, cold, misty highland)"],["el frailejón","frailejón (plant of the páramo)"],["la niebla","fog, mist"],["el arroyo","stream"]],V),
mc(s+'.ex02',"grammar",'Which sentence says that environmental groups ask for laws, any laws, that would protect the páramos?',["Piden leyes que protejan los páramos.","Piden leyes que protegen los páramos.","Piden leyes que protegieran los páramos."],"relativas-subjuntivo",ds={"1":"present-tense","2":"imperfect-subjunctive-forms"}),
fill(s+'.ex03',"Buscamos un guía que __ bien el páramo de Chingaza.","conozca","We are looking for a guide who knows the Chingaza páramo well.","relativas-subjuntivo",hint="conocer"),
build(s+'.ex04',"Los campesinos necesitan cultivos que no dañen el agua del páramo.","The farmers need crops that do not harm the water of the páramo.","relativas-subjuntivo"),
dlg(s+'.ex05',"¿Qué es un frailejón?","","¡Qué planta tan curiosa!",["Es una planta que crece muy despacio en el páramo.","Es un animal pequeño que vive en la niebla del bosque.","Es un arroyo que baja de las montañas hacia el valle."],V),
dict_(s+'.ex06',"Piden una ley que proteja el agua del páramo.","They are asking for a law that protects the water of the páramo.","relativas-subjuntivo")])
# ---------- 02
s='b2-colombiaandina-02'
paras=[
"Bogotá, la capital de Colombia, está en una llanura alta de los Andes, la Sabana de Bogotá, a unos 2600 metros de altura. Fue fundada el 6 de agosto de 1538 por Gonzalo Jiménez de Quesada. Hoy tiene más de siete millones de habitantes. El hecho de que la ciudad esté tan alta sorprende a muchos visitantes, que notan el aire más fino.",
"Es la sede del gobierno nacional. Desde el 7 de agosto de 2026 el presidente es Abelardo de la Espriella, que ganó la segunda vuelta del 21 de junio y sucedió a Gustavo Petro.",
"En 2012 la UNESCO nombró a Bogotá Ciudad de la Literatura. La ciudad tiene muchas bibliotecas y librerías, y cada año se celebra la Feria Internacional del Libro. En el Museo del Oro se pueden ver miles de piezas de oro de los pueblos que vivían en el país antes de la llegada de los españoles.",
"Desde 1974, los domingos y días festivos se cierran muchas calles a los carros para que la gente ande en bicicleta, camine o patine. Es la Ciclovía, y otras ciudades del mundo han tomado la idea de Bogotá. El hecho de que cada domingo se cierren tantas calles muestra que el espacio de la ciudad puede usarse de otra manera.",
"El tráfico es uno de los grandes problemas de la ciudad. Desde 2000 funciona TransMilenio, un sistema de autobuses con carriles propios, y las obras de la primera línea de metro empezaron en 2020. Algunos usuarios critican que los autobuses van muy llenos."]
put_story(s,"Bogotá, una capital a 2600 metros","Bogotá lies on a high plain, has been a UNESCO City of Literature since 2012, closes streets to cars on Sundays with the Ciclovía, and works on its traffic with buses and a future metro.",paras,[
("According to the text, what happens in Bogotá on Sundays and holidays?",["Se cierran muchas calles a los carros para que la gente ande en bicicleta o camine.","Se cierra el Museo del Oro para toda la ciudad.","Se celebra la Feria Internacional del Libro."],"The fourth paragraph describes the Ciclovía."),
("What did UNESCO do in 2012?",["Nombró a Bogotá Ciudad de la Literatura.","Inscribió el Paisaje Cultural Cafetero.","Declaró los páramos Patrimonio de la Humanidad."],"The third paragraph gives the date."),
("What does the text say about public transport?",["Desde 2000 funciona TransMilenio, y las obras del metro empezaron en 2020.","El metro funciona desde 1974 en toda la ciudad.","Los autobuses desaparecieron cuando llegó la Ciclovía."],"The fifth paragraph describes it.")])
put_voc(s,"","City life in Bogotá","Words about the plain, cycling and fairs",[("la sabana","high plain, savannah","noun"),("la ciclovía","Sunday cycleway (streets closed to cars)","noun"),("la feria","fair","noun"),("el carril","lane","noun")])
put_gr(s,"El Hecho de Que: Commenting on a Known Fact",[
T("You know *el hecho de que* from B2 Unit 6: you start with a fact both people already know, and the comment after it takes the subjunctive. Bogotá is a good place for it: the height, the Sunday street closures and the traffic are facts that everyone knows and that people comment on.","What you already know"),
TB("Fact first, comment after",[
["El hecho de que la ciudad esté a 2600 metros sorprende a muchos visitantes.","*esté* (subjunctive): the fact is known, the comment follows"],
["El hecho de que cada domingo se cierren las calles permite andar en bicicleta.","*se cierren*: subjunctive after *el hecho de que*"],
["El hecho de que el tráfico sea tan intenso preocupa a muchas personas.","the comment *preocupa* stays singular, like *el hecho*"]]),
EX("In context",[
("El hecho de que Bogotá esté en una llanura alta sorprende a muchos visitantes.","The fact that Bogotá is on a high plain surprises many visitors."),
("El hecho de que haya una Ciclovía desde 1974 muestra que la idea es antigua.","The fact that there has been a Ciclovía since 1974 shows that the idea is old."),
("El hecho de que los autobuses vayan llenos preocupa a algunos usuarios.","The fact that the buses are full worries some users."),
("El hecho de que tenga tantas bibliotecas explica el título de Ciudad de la Literatura.","The fact that it has so many libraries helps to explain the title of City of Literature.")]),
TIP("Always write *el hecho de que*, with *de*. The comment agrees with *el hecho*, which is singular: *El hecho de que lleguen tarde me molesta*, not *me molestan*. After a past verb use the imperfect subjunctive: *El hecho de que lloviera…*.")])
put_lesson(s,"Bogotá: a capital on a high plain","Talk about Bogotá and comment on facts about it with *el hecho de que* + subjunctive.","el hecho de que with the subjunctive, applied to Bogotá",[
"I can comment on a known fact with *el hecho de que* + subjunctive.",
"I can say where Bogotá is, what the Ciclovía is and what the city does about traffic.",
"I can use the new words for the high plain, the Sunday cycleway, the fair and the lane."])
put_ex(s,[
match(s+'.ex01',[["la sabana","high plain, savannah"],["la ciclovía","Sunday cycleway"],["la feria","fair"],["el carril","lane"]],V),
mc(s+'.ex02',"grammar",'Which sentence says "The fact that the city is at 2,600 metres surprises many visitors"?',["El hecho de que la ciudad esté a 2600 metros sorprende a muchos visitantes.","El hecho que la ciudad esté a 2600 metros sorprende a muchos visitantes.","El hecho de que la ciudad esté a 2600 metros sorprenden a muchos visitantes."],"el-hecho-de-que-subjuntivo"),
fill(s+'.ex03',"El hecho de que cada domingo se __ muchas calles a los carros permite andar en bicicleta.","cierren","The fact that many streets are closed to cars every Sunday makes it possible to cycle.","el-hecho-de-que-subjuntivo",hint="cerrar"),
build(s+'.ex04',"El hecho de que el tráfico sea tan intenso preocupa a muchas personas.","The fact that the traffic is so heavy worries many people.","el-hecho-de-que-subjuntivo"),
dlg(s+'.ex05',"¿Qué es la Ciclovía?","","¡Qué buena idea!",["Es el día en que se cierran calles a los carros para andar en bicicleta.","Es una feria del libro que se celebra todos los años.","Es un carril especial para los autobuses de TransMilenio."],V),
dict_(s+'.ex06',"El hecho de que la ciudad tenga una Ciclovía desde 1974 sorprende a muchos visitantes.","The fact that the city has had a Ciclovía since 1974 surprises many visitors.","el-hecho-de-que-subjuntivo")])
# ---------- 03
s='b2-colombiaandina-03'
paras=[
"Medellín, capital del departamento de Antioquia, está en el valle de Aburrá, a unos 1500 metros de altura. Su clima es templado todo el año, y por eso se la llama la ciudad de la eterna primavera. No es que haga mucho calor, sino que la temperatura casi no cambia.",
"En los años ochenta y noventa la ciudad sufrió una violencia muy grave, ligada al narcotráfico, a las guerrillas y a los grupos paramilitares. Según datos de la policía de la época, en 1991 Medellín tuvo una de las tasas de homicidios más altas del mundo. Pablo Escobar, jefe del cártel de Medellín, murió en diciembre de 1993.",
"En 1995 se inauguró el Metro de Medellín, y en 2004 el Metrocable, un sistema de cabinas aéreas que conecta barrios de ladera con el metro. Muchos presentan el Metrocable como uno de los primeros transportes por cable de este tipo en una ciudad.",
"Algunos barrios de ladera, como la Comuna 13, vivieron episodios muy duros. En octubre de 2002 el ejército hizo la Operación Orión en ese barrio; organizaciones de derechos humanos denunciaron muertes y desapariciones de civiles, y las autoridades de la época defendieron la operación. En 2011 se inauguraron escaleras eléctricas al aire libre, que hoy visitan muchos turistas.",
"La ciudad ha construido también parques biblioteca en barrios populares. En 2013 un concurso organizado por el Wall Street Journal, Citi y el Urban Land Institute eligió a Medellín como la ciudad más innovadora del año. No es que los problemas hayan desaparecido, sino que la ciudad ha cambiado mucho: según las cifras oficiales, los homicidios han bajado desde 1991, pero los críticos señalan que la desigualdad sigue siendo grande."]
put_story(s,"Medellín, de la violencia al metro","Medellín has a mild climate, lived through severe violence in the 1980s and 1990s, and built a metro, a cable system and library parks; the text gives dates and attributes each judgement.",paras,[
("According to the text, why is Medellín called the city of eternal spring?",["Porque su clima es templado todo el año.","Porque hace mucho calor en todas las estaciones.","Porque tiene flores de colores durante todo el año."],"The first paragraph explains the nickname."),
("What happened in Comuna 13 in October 2002?",["El ejército hizo la Operación Orión, y organizaciones de derechos humanos denunciaron muertes de civiles.","Se inauguró el Metrocable que conecta los barrios con el metro.","Se construyeron escaleras eléctricas al aire libre."],"The fourth paragraph attributes the claims."),
("What do critics say about Medellín today, according to the text?",["Que la desigualdad sigue siendo grande.","Que la violencia es peor que en 1991.","Que el metro no funciona."],"The last paragraph gives the critics' view.")])
put_voc(s,"","Medellín's slopes and districts","Words about the city and its neighbourhoods",[("la ladera","hillside, slope","noun"),("la comuna","district (of Medellín)","noun"),("la escalera","staircase, stairs","noun"),("el homicidio","homicide, killing","noun")])
put_gr(s,"No Es Que… Sino Que…: Correcting a Reason About Medellín",[
T("You know *no es que* + subjunctive, *sino que* + indicative from B2 Unit 5: you reject a reason people might assume and give the real one. Medellín's story is full of assumptions to correct, about its climate, its past and its change. The first part is a reason you say is not true, so it takes the subjunctive; the second part is the real reason, in the indicative.","What you already know"),
TB("Reject one reason, give the real one",[
["No es que haga mucho calor, sino que la temperatura casi no cambia.","*haga* (subjunctive) rejects; *cambia* (indicative) states"],
["No es que los problemas hayan desaparecido, sino que la ciudad ha cambiado mucho.","*hayan desaparecido* + *ha cambiado*"],
["No es que Medellín sea fría, sino que su clima es templado.","*sea* + *es*"]]),
EX("In context",[
("No es que Medellín tenga mucho calor, sino que su clima es templado todo el año.","It is not that Medellín is very hot, but that its climate is mild all year."),
("No es que la violencia haya terminado, sino que, según las cifras oficiales, ha bajado desde 1991.","It is not that violence has ended, but that, according to official figures, it has fallen since 1991."),
("No es que el Metrocable sea solo un transporte, sino que conecta barrios con el metro.","It is not that the Metrocable is only a means of transport, but that it connects districts with the metro."),
("No era que la ciudad no tuviera problemas, sino que ya no era la de los años noventa.","It was not that the city had no problems, but that it was no longer the city of the 1990s.")]),
TIP("Use this pattern when you expect someone to draw a wrong conclusion. It corrects a reason, not a person. *Sino que* always keeps its *que* and takes the indicative. On a painful topic, attribute the judgement (*según las cifras oficiales*, *según los críticos*) instead of stating it as your own.")])
put_lesson(s,"Medellín: the city of eternal spring","Talk about Medellín and correct assumptions about it with *no es que… sino que…*, attributing each judgement.","no es que… sino que…, applied to Medellín",[
"I can reject a reason and give the real one with *no es que* + subjunctive and *sino que* + indicative.",
"I can say why Medellín is called the city of eternal spring and give the dates of the metro and the Metrocable.",
"I can use the new words for hillside, district, staircase and killing."])
put_ex(s,[
match(s+'.ex01',[["la ladera","hillside, slope"],["la comuna","district (of Medellín)"],["la escalera","staircase, stairs"],["el homicidio","homicide, killing"]],V),
mc(s+'.ex02',"grammar",'Which sentence says "It is not that it is hot, but that the climate is mild all year"?',["No es que haga calor, sino que el clima es templado todo el año.","No es que hace calor, sino que el clima es templado todo el año.","No es que haga calor, sino que el clima sea templado todo el año."],"refutacion-no-es-que-sino",ds={"1":"present-tense","2":"subjuntivo-morfologia"}),
fill(s+'.ex03',"No es que Medellín sea una ciudad fría, __ que su clima es templado.","sino","It is not that Medellín is a cold city, but that its climate is mild.","refutacion-no-es-que-sino"),
build(s+'.ex04',"No es que los problemas hayan desaparecido, sino que la ciudad ha cambiado.","It is not that the problems have disappeared, but that the city has changed.","refutacion-no-es-que-sino"),
dlg(s+'.ex05',"¿Qué es una comuna?","","Entonces Medellín tiene muchas comunas.",["Es una zona de la ciudad con varios barrios.","Es una calle larga con muchas escaleras.","Es una montaña con casas en la ladera."],V),
dict_(s+'.ex06',"No es que Medellín sea fría, sino que tiene un clima templado.","It is not that Medellín is cold, but that it has a mild climate.","refutacion-no-es-que-sino")])
# ---------- 04
s='b2-colombiaandina-04'
paras=[
"El Eje Cafetero es una región de las montañas de Colombia, en la que se cultiva café desde hace más de un siglo. En 2011 la UNESCO inscribió el Paisaje Cultural Cafetero de Colombia en la lista del Patrimonio Mundial. Abarca zonas de los departamentos de Caldas, Quindío, Risaralda y Valle del Cauca.",
"En este paisaje, el café se cultiva en pequeñas fincas familiares, en laderas muy inclinadas. Como el terreno es difícil, el café se recoge a mano, grano maduro por grano maduro. Después, los granos se despulpan, se lavan y se secan, muchas veces al sol.",
"En los pueblos de la región todavía se conservan casas de bahareque, un sistema de construcción con cañas y barro, y de colores brillantes. Para transportar a las personas y los productos se usan todavía las chivas, autobuses coloridos de madera.",
"En el Valle de Cocora, cerca de Salento, en Quindío, crecen palmas de cera del Quindío. Son una de las palmas más altas del mundo y el árbol nacional de Colombia.",
"Colombia es uno de los mayores productores de café del mundo. La Federación Nacional de Cafeteros, que se fundó en 1927, representa a los productores. En la región, muchas familias dependen de la cosecha, y por eso les preocupan los cambios del clima y de los precios, según las organizaciones de cafeteros. Hoy muchos turistas visitan las fincas, donde se explica cómo se produce el café."]
put_story(s,"El Eje Cafetero, un paisaje de café","The Coffee Cultural Landscape of Colombia was added to UNESCO's World Heritage list in 2011; the text describes how coffee is picked and processed, the houses, the buses and the wax palms of the region.",paras,[
("What did UNESCO do in 2011, according to the text?",["Inscribió el Paisaje Cultural Cafetero de Colombia en la lista del Patrimonio Mundial.","Nombró a Bogotá Ciudad de la Literatura.","Aprobó una ley sobre los páramos."],"The first paragraph gives the date."),
("According to the text, how is coffee harvested in this landscape?",["Se recoge a mano, porque el terreno es difícil.","Se recoge con máquinas grandes en las llanuras.","Se recoge en barcos y se seca en el mar."],"The second paragraph explains the harvest."),
("What are the chivas, according to the text?",["Autobuses coloridos de madera.","Casas de cañas y barro.","Palmas altas del Valle de Cocora."],"The third paragraph describes the chivas.")])
put_voc(s,"","Coffee, houses and buses","Words for the coffee landscape",[("el cafetal","coffee plantation","noun"),("el bahareque","bahareque (cane-and-mud construction)","noun"),("la chiva","chiva (colourful wooden country bus)","noun"),("despulpar","to pulp (remove the fruit from coffee beans)","verb")])
put_gr(s,"The Passive With Se: How Coffee Is Made",[
T("You know the passive *se* from B1 Unit 6: *se* + a verb that agrees with the thing, when who does the action is unimportant or general (*se busca una persona*, *se buscan personas*). A process like coffee growing is told this way: the beans, the houses and the buses matter more than the people who handle them.","What you already know"),
TB("Singular thing, singular verb; plural thing, plural verb",[
["El café se recoge a mano.","*café* is singular: *se recoge*"],
["Los granos se despulpan, se lavan y se secan.","*granos* is plural: *se despulpan*, *se lavan*, *se secan*"],
["En los pueblos se conservan casas de bahareque.","*casas* is plural: *se conservan*"]]),
EX("In context",[
("El café se recoge a mano en laderas muy inclinadas.","The coffee is picked by hand on very steep slopes."),
("Después de la cosecha, los granos se secan al sol.","After the harvest, the beans are dried in the sun."),
("En el Eje Cafetero todavía se usan las chivas.","In the Eje Cafetero the chivas are still used."),
("En las fincas se explica cómo se produce el café.","On the farms they explain how coffee is produced.")]),
TIP("The verb agrees with the thing: *se recoge el café*, *se recogen los granos*. When you want to name who does the action, use the passive with *ser* instead (B1 Unit 18). Do not drop *se*: *los granos recogen a mano* would mean that the beans pick something.")])
put_lesson(s,"The Coffee Landscape: a UNESCO site since 2011","Describe the coffee landscape of Colombia and how coffee is made with the passive *se* (*se recoge*, *se secan*).","the passive se construction, applied to the Coffee Cultural Landscape",[
"I can describe how something is done with the passive *se* (*se recoge*, *se secan*).",
"I can say what UNESCO recognised in 2011 and what the chivas and the bahareque houses are.",
"I can use the new words for the coffee plantation, bahareque, the chiva and to pulp."])
put_ex(s,[
match(s+'.ex01',[["el cafetal","coffee plantation"],["el bahareque","bahareque (cane-and-mud construction)"],["la chiva","chiva (colourful wooden country bus)"],["despulpar","to pulp (coffee beans)"]],V),
mc(s+'.ex02',"grammar",'Which sentence says "The beans are picked by hand"?',["Los granos se recogen a mano.","Los granos se recoge a mano.","Los granos recogen a mano."],"pasiva-refleja"),
fill(s+'.ex03',"Después de la cosecha, los granos se __ al sol.","secan","After the harvest, the beans are dried in the sun.","pasiva-refleja",hint="secar"),
build(s+'.ex04',"En el Eje Cafetero todavía se conservan casas de bahareque de colores.","In the Eje Cafetero houses of bahareque in many colours are still preserved.","pasiva-refleja"),
dlg(s+'.ex05',"¿Qué es una chiva?","","Me gustaría viajar en una.",["Es un autobús de madera pintado de colores.","Es una casa de barro y cañas de la región cafetera.","Es un cafetal pequeño en una ladera."],V),
dict_(s+'.ex06',"Se despulpan, se lavan y se secan los granos de café.","The coffee beans are pulped, washed and dried.","pasiva-refleja")])
# ---------- 05
s='b2-colombiaandina-05'
paras=[
"Gabriel García Márquez nació el 6 de marzo de 1927 en Aracataca, un pueblo de la costa caribe de Colombia, y murió el 17 de abril de 2014 en Ciudad de México, donde vivió muchos años. Muchos lo llaman Gabo.",
"En realidad, empezó su carrera como periodista. En los años cincuenta trabajó en el periódico El Espectador, de Bogotá, donde en 1955 se publicó en varios capítulos Relato de un náufrago. Afortunadamente, sus textos periodísticos se han reunido en libros y todavía se pueden leer.",
"Su primera novela, La hojarasca, es de 1955. En 1967 se publicó en Buenos Aires Cien años de soledad, la novela que lo hizo famoso en todo el mundo y que se sitúa en Macondo, un pueblo imaginario. Entre sus otras obras están Crónica de una muerte anunciada, de 1981, y El amor en los tiempos del cólera, de 1985.",
"En rigor, Macondo no es Aracataca: es un lugar de ficción, aunque algunos lectores ven en él rasgos del pueblo donde nació el autor. A su obra se le asocia con el llamado realismo mágico, un término que algunos críticos discuten.",
"En 1982 recibió el Premio Nobel de Literatura. Según la Academia Sueca, lo premió por novelas y cuentos en los que lo fantástico y lo real se unen en un mundo imaginario que refleja la vida y los conflictos de un continente.",
"En 1994 fundó en Cartagena de Indias la Fundación para un Nuevo Periodismo Iberoamericano, que forma a periodistas. Muchos lectores y críticos lo consideran uno de los grandes escritores en lengua española."]
put_story(s,"Gabriel García Márquez, el escritor y periodista","A short text about Gabriel García Márquez: his birth in Aracataca in 1927, his early journalism, the novel of 1967, the Nobel Prize of 1982 and his foundation for journalism.",paras,[
("According to the text, where and when was García Márquez born?",["En Aracataca, en 1927.","En Bogotá, en 1955.","En Ciudad de México, en 1982."],"The first paragraph gives the place and date."),
("What does the text say about his first years as a writer?",["Empezó su carrera como periodista y trabajó en El Espectador.","Empezó su carrera como profesor en Cartagena de Indias.","Empezó su carrera como director de una fundación."],"The second paragraph describes his journalism."),
("What happened in 1982?",["Recibió el Premio Nobel de Literatura.","Se publicó Cien años de soledad.","Fundó la Fundación para un Nuevo Periodismo Iberoamericano."],"The fifth paragraph gives the date of the prize.")])
put_voc(s,"","A writer and journalist","Words about the author and his work",[("el relato","account, story","noun"),("el náufrago","castaway, shipwreck survivor","noun"),("el premio","prize","noun"),("el rasgo","trait, feature","noun")])
put_gr(s,"Stance Adverbs: Commenting on Facts About a Writer",[
T("You know stance adverbs such as *afortunadamente*, *lamentablemente*, *en realidad* and *en rigor* from B2 Unit 1. They step outside the sentence and show how the speaker sees a fact, and a comma marks each edge. A text about a writer's life is a good place for them: they correct what readers expect (*en realidad*), give the exact truth (*en rigor*) or show a feeling about a fact (*afortunadamente*).","What you already know"),
TB("Four stance adverbs",[
["En realidad, empezó su carrera como periodista.","*en realidad*: in fact, correcting what people expect"],
["En rigor, Macondo no es Aracataca.","*en rigor*: strictly speaking"],
["Afortunadamente, sus textos periodísticos se han reunido en libros.","*afortunadamente*: your feeling about a fact"],
["Lamentablemente, no todos sus textos se conservan.","*lamentablemente*: unfortunately"]]),
EX("In context",[
("En realidad, García Márquez empezó su carrera como periodista.","In fact, García Márquez began his career as a journalist."),
("En rigor, Macondo no es un pueblo real, sino un lugar de ficción.","Strictly speaking, Macondo is not a real town but a place in fiction."),
("Afortunadamente, el periódico conserva los textos que se publicaron en 1955.","Fortunately, the newspaper keeps the texts that were published in 1955."),
("El autor, en realidad, nació en un pueblo pequeño de la costa caribe.","The author, in fact, was born in a small town on the Caribbean coast.")]),
TIP("Try the comma test: if you can pause and put commas round the adverb, it is commenting on the whole sentence. Use one stance adverb per sentence; two in a row sound heavy. This text is about the writer and his work: it states facts and attributes judgements.")])
put_lesson(s,"García Márquez: a writer and journalist from Colombia","Talk about García Márquez and his work with stance adverbs (*en realidad*, *en rigor*, *afortunadamente*).","stance adverbs, applied to García Márquez",[
"I can comment on a fact with a stance adverb such as *en realidad*, *en rigor* or *afortunadamente*.",
"I can give the main dates of García Márquez: 1927, 1955, 1967 and 1982.",
"I can use the new words for an account, a castaway, a prize and a trait."])
put_ex(s,[
match(s+'.ex01',[["el relato","account, story"],["el náufrago","castaway"],["el premio","prize"],["el rasgo","trait, feature"]],V),
mc(s+'.ex02',"grammar",'Which sentence says "Fortunately, his journalism has been collected in books"?',["Afortunadamente, sus textos periodísticos se han reunido en libros.","Afortunadamente que sus textos periodísticos se han reunido en libros.","Afortunadamente, sus textos periodísticos se hayan reunido en libros."],"stance-adverbs",ds={"2":"subjuntivo-perfecto"}),
fill(s+'.ex03',"En __, Macondo no es Aracataca, sino un lugar de ficción.","rigor","Strictly speaking, Macondo is not Aracataca but a place of fiction.","stance-adverbs"),
build(s+'.ex04',"En realidad, empezó su carrera como periodista.","In fact, he began his career as a journalist.","stance-adverbs"),
dlg(s+'.ex05',"¿Qué es Relato de un náufrago?","","Entonces escribía antes de las novelas.",["Es un texto que se publicó en 1955 en un periódico de Bogotá.","Es la novela que le dio el Premio Nobel en 1982.","Es el pueblo de ficción donde ocurren sus novelas."],V),
dict_(s+'.ex06',"En rigor, Macondo es un pueblo de ficción.","Strictly speaking, Macondo is a fictional town.","stance-adverbs")])
# ---------- consolidation
s='b2-colombiaandina-consolidation'
put_lesson(s,"Unit 13 Review: the Colombian Andes","Review the páramos, Bogotá, Medellín, the coffee landscape and García Márquez, with relative clauses and the subjunctive, *el hecho de que*, *no es que… sino que…*, the passive *se* and stance adverbs.","review: relative clauses with the subjunctive, el hecho de que, no es que sino que, passive se, stance adverbs",[
"I can review what I learned about the Colombian Andes, from the páramos to Gabo.",
"I can use relative clauses with the subjunctive, *el hecho de que*, *no es que… sino que…*, the passive *se* and stance adverbs.",
"I can put events from 1538 to 2018 in order.",
"I can attribute a judgement about Medellín instead of stating it as my own."],
checklist=[
"I can say what I am looking for or what does not exist with *que* + subjunctive.",
"I can comment on a fact everyone knows with *el hecho de que* + subjunctive.",
"I can reject a reason and give the real one with *no es que* + subjunctive and *sino que* + indicative.",
"I can describe how something is done with the passive *se* (*se recoge*, *se secan*).",
"I can comment on a fact with a stance adverb such as *en realidad*, *en rigor* or *afortunadamente*."])
put_ex(s,[
match(s+'.ex01',[["el frailejón","frailejón (plant of the páramo)"],["la ciclovía","Sunday cycleway"],["la ladera","hillside, slope"],["el cafetal","coffee plantation"]],V),
mc(s+'.ex02',"grammar",'Which sentence says "There is nobody who knows the whole páramo"?',["No hay nadie que conozca todo el páramo.","No hay nadie que conoce todo el páramo.","No hay nadie que conocerá todo el páramo."],"relativas-subjuntivo",ds={"1":"present-tense","2":"futuro-simple"}),
mc(s+'.ex03',"reading","According to the texts, what happened in 2012?",["Bogotá recibió el título de Ciudad de la Literatura.","El Paisaje Cultural Cafetero entró en una lista de la UNESCO.","Se inauguró el Metrocable de Medellín."],None),
fill(s+'.ex04',"El hecho de que la región __ famosa por su café explica por qué vienen muchos turistas.","sea","The fact that the region is famous for its coffee explains why many tourists come.","el-hecho-de-que-subjuntivo",hint="ser"),
{"id":s+".ex05","type":"sentence-order","category":"grammar","sentences":["En 1538 se fundó Bogotá. [Bogotá was founded in 1538.]","En 1995 se inauguró el Metro de Medellín. [The Medellín Metro was opened in 1995.]","En 2011 se inscribió el Paisaje Cultural Cafetero en la lista de la UNESCO. [The Coffee Cultural Landscape was added to UNESCO's list in 2011.]","En 2018 se aprobó una ley sobre los páramos. [A law on the páramos was passed in 2018.]"],"solution":[0,1,2,3],"teaches":["pasiva-refleja"]},
dlg(s+'.ex06',"¿Qué es el Metrocable?","","Me gustaría subir algún día.",["Es un transporte que conecta barrios de ladera con el metro.","Es una calle cerrada a los carros los domingos y días festivos.","Es un autobús de madera pintado de colores."],V),
dict_(s+'.ex07',"Lamentablemente, muchos páramos están en peligro.","Unfortunately, many páramos are in danger.","stance-adverbs"),
{"id":s+".ex08","type":"structured-writing","category":"writing","template":[{"prompt":"Say that it is not that Medellín is cold, but that its climate is mild. Start with \"No es que Medellín\".","answer":"No es que Medellín sea fría, sino que tiene un clima templado."}],"teaches":["refutacion-no-es-que-sino"]}])
