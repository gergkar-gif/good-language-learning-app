import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from common import *
V='b2-mexico-south-vocab'
wc={}
# ---------------- 01
s='b2-mexicosur-01'
apply_lesson(s,"Cenotes, Jungles and Mountains: The Geography of the South",
 "Describe the cenotes of Yucatán, the Lacandon jungle and the cloud forests of Oaxaca with relative clauses.",
 "relative clauses with que, donde and a preposition + el que",
 ["I can describe a place or a thing with a relative clause (*que*, *donde*, *en el que*).",
  "I can say what a cenote is and why the Maya held it sacred.",
  "I can explain why the water of the Yucatán peninsula is easy to pollute."],
 ("Unit 3: The South: Indigenous Peoples and Biodiversity",
  ["This unit is about southern Mexico: Oaxaca, Chiapas and the Yucatán peninsula. You will read about the landscape, the Zapotec, Mixtec and Maya peoples, community government in Oaxaca, the Zapatista uprising of 1994 and the debate about the Maya Train.",
   "The screens and instructions are in English; the texts and exercises are in Spanish. There is no new grammar here: each lesson uses a skill you already know to talk about the region, and teaches you the words you need for it."]))
wc[s]=apply_story(s,"Los cenotes de Yucatán y las selvas de Chiapas",
 "The limestone of Yucatán hides rivers and cenotes that the Maya held sacred, while Chiapas and Oaxaca have jungle and cloud forests that are under pressure.",
 ["relative clauses","vocabulary of the southern landscape"],
 ["La península de Yucatán es una gran plataforma de roca caliza. Allí casi no hay ríos en la superficie, porque el agua de la lluvia pasa por la roca y corre por debajo de la tierra. En algunos lugares, el techo de la roca se ha caído y deja ver el agua: así nacen los cenotes, que hoy atraen a muchos visitantes. Los científicos llaman karst a este tipo de paisaje.",
  "Para los mayas, los cenotes eran una fuente de agua, pero también un lugar sagrado. Muchos pueblos mayas creían que eran una entrada al inframundo, que llamaban Xibalbá. Según los arqueólogos, en el Cenote Sagrado de Chichén Itzá se dejaron ofrendas durante siglos.",
  "Más al sur, en Chiapas, está la Selva Lacandona, una de las mayores selvas tropicales que quedan en México. Allí viven el jaguar y la guacamaya roja, y también el pueblo lacandón. En Oaxaca, la Sierra Norte tiene bosques de niebla, donde las nubes mantienen la humedad durante gran parte del año. Algunas especies de estas montañas no se encuentran en otras partes del mundo.",
  "Estos paisajes están en peligro. En la Selva Lacandona, la ganadería y la agricultura han reducido la selva en las últimas décadas. En Yucatán, el agua que se bebe viene de un acuífero que se contamina con facilidad, porque la roca deja pasar rápido todo lo que cae al suelo. Por eso muchos científicos piden que se cuide el agua de los cenotes y de las cuevas."])
g=gr("grammar.b2.mexicosur.01.relative-clauses","Describing a Place with Relative Clauses",
 "You know relative clauses with *que* and *donde* from B1 Unit 5, and a preposition before *el que* from B1 Unit 20. In this lesson they let you describe the landscape of the south: a cenote, a jungle, an aquifer. When you describe something real, the verb of the relative clause is in the indicative.",
 "The relative word you need",
 [("una región que tiene muchas selvas","a region that has many jungles (*que* for a thing or a person)"),
  ("la selva donde viven los jaguares","the jungle where jaguars live (*donde* for a place)"),
  ("un acuífero del que dependen muchas personas","an aquifer that many people depend on (*depender de* gives *del que*)"),
  ("los cenotes en los que se puede nadar","the cenotes where you can swim (*en* + *los que*)")],None,
 [("Yucatán es una península que no tiene ríos en la superficie.","Yucatán is a peninsula that has no rivers on the surface."),
  ("En Chiapas está la Selva Lacandona, donde viven el jaguar y la guacamaya roja.","In Chiapas is the Lacandon Jungle, where the jaguar and the scarlet macaw live."),
  ("El agua viene de un acuífero del que dependen muchas personas.","The water comes from an aquifer that many people depend on."),
  ("Los mayas visitaban cenotes en los que dejaban ofrendas.","The Maya visited cenotes where they left offerings.")],
 "Keep the preposition the verb needs and put it before *el que*, *la que*, *los que* or *las que*, matching the noun: *el acuífero del que dependen*, *la cueva en la que entramos*. Without it the sentence is wrong: not *el acuífero que dependen*.")
apply_gr(s,g)
apply_voc(s,[("el cenote","cenote, natural sinkhole","noun"),("el acuífero","aquifer","noun"),("la selva","jungle, rainforest","noun"),("sagrado","sacred","adjective"),("la caliza","limestone","noun"),("la superficie","surface","noun")],
 "The landscape of the south","Cenotes, jungles and aquifers")
apply_ex(s,[
 match(s+".ex01",[("el cenote","cenote, natural sinkhole"),("el acuífero","aquifer"),("la caliza","limestone"),("sagrado","sacred")],V),
 mc(s+".ex02","", "grammar","Which sentence is correct?",
   ["El acuífero del que depende la ciudad está bajo la selva.","El acuífero que depende la ciudad está bajo la selva.","El acuífero de la que depende la ciudad está bajo la selva."],"relativas-preposicion-el-que"),
 fill(s+".ex03","La Selva Lacandona, __ viven el jaguar y la guacamaya roja, está en Chiapas.","donde","The Lacandon Jungle, where the jaguar and the scarlet macaw live, is in Chiapas.","relative-clauses",answers=["donde","en la que"]),
 build(s+".ex04",["Yucatán","es","una","península","que","no","tiene","ríos","en","la","superficie."],"Yucatán is a peninsula that has no rivers on the surface.","relative-clauses"),
 dlg(s+".ex05",[("Carlos","¿Qué es un cenote?"),("Meg","_____"),("Carlos","Entonces es un lugar muy especial.")],
   ["Es un pozo natural en el que se ve el agua que corre bajo la tierra.","Es un pozo natural el que se ve el agua que corre bajo la tierra.","Es un pozo natural en la que se ve el agua que corre bajo la tierra."],"relativas-preposicion-el-que"),
 dict_(s+".ex06","Los cenotes se forman en la caliza, que deja pasar el agua de la lluvia.","Cenotes form in limestone, which lets rainwater through.","relative-clauses"),
])
# ---------------- 02
s='b2-mexicosur-02'
apply_lesson(s,"Zapotecs, Mixtecs and Maya: Peoples Who Are Still Here",
 "Talk about living indigenous cultures and the backstrap loom with a pesar de, pese a and aunque.",
 "concession with a pesar de que, pese a and aunque",
 ["I can say that something continues in spite of a difficulty, with *a pesar de*, *a pesar de que* and *pese a*.",
  "I can say where the Zapotec, Mixtec and Maya peoples live.",
  "I can describe the backstrap loom and say why indigenous languages are still spoken."])
wc[s]=apply_story(s,"Zapotecos, mixtecos y mayas: pueblos vivos",
 "The Zapotec, Mixtec and Maya peoples are not only a part of the past: their languages and weaving traditions have lasted in spite of school policy.",
 ["a pesar de que, pese a","vocabulary of weaving and languages"],
 ["Los zapotecos, los mixtecos y los mayas no son solo pueblos del pasado. Los zapotecos y los mixtecos viven sobre todo en Oaxaca, y los mayas, en Chiapas y en la península de Yucatán. En México se hablan 68 lenguas indígenas, y muchas de ellas se oyen todos los días en Oaxaca y en Chiapas. Hace más de dos mil años, los zapotecos ya habían construido Monte Albán, una de sus ciudades más importantes, cerca de la actual ciudad de Oaxaca.",
  "El telar de cintura es una de las tradiciones que más han durado. La tejedora ata un extremo del telar a un árbol o a un poste y el otro a su cintura, y trabaja así durante horas. En Teotitlán del Valle, un pueblo zapoteco, se hacen tapetes de lana. En San Juan Chamula, en Chiapas, las mujeres tzotziles tejen huipiles con diseños propios de su comunidad. Muchas tejedoras dicen que sus diseños cuentan historias de la naturaleza y del universo.",
  "En el siglo veinte, las escuelas del Estado enseñaban casi siempre en español, porque el Gobierno buscaba unir al país con un solo idioma. A pesar de que la escuela no usaba sus lenguas, muchas familias siguieron hablándolas en casa y en el campo. Desde 2003, una ley reconoce las lenguas indígenas como lenguas nacionales, igual que el español. Aun así, algunas lenguas tienen hoy muy pocos hablantes, y varias comunidades trabajan para que los niños las aprendan."])
g=gr("grammar.b2.mexicosur.02.a-pesar-de","In Spite of the Difficulties",
 "You know *aunque* from A2 Unit 28, and *a pesar de que* and *pese a* from B1 Unit 32. They let you say that something continues in spite of an obstacle, which is exactly the story of the peoples of the south and their languages. With a real fact, the verb stays in the indicative.",
 "Four ways to concede",
 [("A pesar de las presiones, siguieron hablando zapoteco.","*a pesar de* + noun: In spite of the pressure, they kept speaking Zapotec."),
  ("A pesar de ser un trabajo lento, muchas mujeres tejen.","*a pesar de* + infinitive: Although it is slow work, many women weave."),
  ("A pesar de que la escuela enseñaba en español, hablaban su lengua en casa.","*a pesar de que* + a full clause: Although the school taught in Spanish, they spoke their language at home."),
  ("Pese a las dificultades, la tradición continúa.","*pese a* + noun: Despite the difficulties, the tradition continues.")],None,
 [("A pesar de que el trabajo es lento, el telar de cintura perdura en muchos pueblos.","Although the work is slow, the backstrap loom lasts in many villages."),
  ("Pese a las presiones, los pueblos mixtecos conservan su lengua.","Despite the pressures, the Mixtec peoples keep their language."),
  ("Aunque la escuela enseñaba en español, muchas familias siguieron hablando su lengua.","Although the school taught in Spanish, many families kept speaking their language."),
  ("A pesar de ser muy antiguo, el huipil sigue en uso.","Although it is very old, the huipil is still in use.")],
 "*A pesar de* and *pese a* take a noun or an infinitive; before a full clause you need *que*: *a pesar de que la escuela enseñaba en español*. Not *a pesar que*, and not *a pesar de la escuela enseñaba*. *Aunque* also takes a full clause and means nearly the same.")
apply_gr(s,g)
apply_voc(s,[("el telar","loom","noun"),("la tejedora","weaver","noun"),("el huipil","huipil, traditional embroidered blouse or tunic","noun"),("el hablante","speaker (of a language)","noun"),("perdurar","to last, to endure","verb")],
 "Peoples, languages and weaving","Loom, weavers and languages")
apply_ex(s,[
 match(s+".ex01",[("el telar","loom"),("la tejedora","weaver"),("el huipil","huipil, traditional embroidered blouse or tunic"),("el hablante","speaker (of a language)")],V),
 mc(s+".ex02","","grammar","Which sentence says \"Although the school taught in Spanish, many families kept speaking Zapotec at home\"?",
   ["A pesar de que la escuela enseñaba en español, muchas familias siguieron hablando zapoteco en casa.","A pesar que la escuela enseñaba en español, muchas familias siguieron hablando zapoteco en casa.","A pesar de la escuela enseñaba en español, muchas familias siguieron hablando zapoteco en casa."],"a-pesar-de"),
 fill(s+".ex03","A pesar de __ un trabajo lento, muchas tejedoras usan todavía el telar de cintura.","ser","Although it is slow work, many weavers still use the backstrap loom.","a-pesar-de"),
 build(s+".ex04",["Pese","a","las","dificultades,","los","pueblos","mixtecos","hablan","todavía","su","lengua."],"Despite the difficulties, the Mixtec peoples still speak their language.","a-pesar-de"),
 dlg(s+".ex05",[("Meg","¿Todavía se habla zapoteco en Oaxaca?"),("Carlos","_____"),("Meg","Entonces la lengua sigue viva.")],
   ["Sí, pese a las presiones de la escuela, muchas familias lo siguen hablando.","Sí, pese las presiones de la escuela, muchas familias lo siguen hablando.","Sí, pese a que las presiones de la escuela, muchas familias lo siguen hablando."],"a-pesar-de"),
 dict_(s+".ex06","A pesar de que el trabajo es lento, el telar de cintura perdura en muchos pueblos.","Although the work is slow, the backstrap loom lasts in many villages.","a-pesar-de"),
])
# ---------------- 03
s='b2-mexicosur-03'
apply_lesson(s,"Communities, Tequio and Self-Government in Oaxaca",
 "Describe how Oaxacan communities decide and work together using passive se and impersonal se.",
 "passive se and impersonal se",
 ["I can say what is done in a community, without saying who does it, with *se*.",
  "I can explain what an assembly, a cargo and tequio are.",
  "I can say that Oaxaca's municipalities choose their authorities in different ways."])
wc[s]=apply_story(s,"El tequio y las asambleas de Oaxaca",
 "Many Oaxacan municipalities choose their authorities in assemblies, share unpaid communal work called tequio, and use a system of service posts.",
 ["passive se and impersonal se","vocabulary of community government"],
 ["Oaxaca tiene 570 municipios, más que cualquier otro estado de México. En más de cuatrocientos de ellos, las autoridades se eligen según las reglas de cada comunidad, sin partidos políticos. Antes este sistema se llamaba «usos y costumbres»; hoy se llama oficialmente sistemas normativos indígenas.",
  "En estos pueblos, la máxima autoridad suele ser la asamblea, donde se reúnen los ciudadanos de la comunidad. En la asamblea se discuten los problemas del pueblo, se nombran las autoridades y se toman las decisiones. Se busca llegar a un consenso y no solo ganar una votación.",
  "Otra tradición importante es el tequio, un trabajo colectivo que no se paga. Gracias al tequio se arreglan los caminos, se construyen escuelas y se cuidan los bosques de la comunidad. En muchos pueblos, quien no participa sin una buena razón puede recibir una sanción, que decide la propia asamblea.",
  "Muchas comunidades tienen también un sistema de cargos: son servicios al pueblo que se pagan poco o no se pagan. En muchas comunidades, antes de llegar a presidente municipal, una persona sirve durante años en cargos más pequeños. Pensadores indígenas de Oaxaca, como Floriberto Díaz y Jaime Martínez Luna, hablan de «comunalidad»: la idea de que la tierra, la asamblea, el trabajo y la fiesta forman un solo modo de vida.",
  "El sistema también se discute. Algunas personas piden que las mujeres y los jóvenes participen más en las asambleas, y otras defienden las reglas tal como son."])
g=gr("grammar.b2.mexicosur.03.se-impersonal","What Is Done in the Community",
 "You know passive *se* and impersonal *se* from B1 Unit 6. *Se* lets you say what is done without saying who does it, which is how people describe community rules: *en la asamblea se toman las decisiones*. With a noun, the verb agrees with it. With no noun, the verb stays singular.",
 "Passive se and impersonal se",
 [("Se discute un problema. / Se discuten los problemas.","passive *se*: the verb agrees with the noun (a problem is discussed / problems are discussed)"),
  ("Con el tequio se arreglan los caminos.","passive *se*, plural noun, plural verb (roads are repaired)"),
  ("En la asamblea se decide por consenso.","impersonal *se*, no noun, singular verb (things are decided by consensus)"),
  ("En estos pueblos se trabaja para la comunidad.","impersonal *se* (people work for the community)")],None,
 [("En la asamblea se discuten los problemas del pueblo.","In the assembly the problems of the village are discussed."),
  ("Con el tequio se arreglan los caminos y se construyen escuelas.","With tequio roads are repaired and schools are built."),
  ("En muchos pueblos se vota en la asamblea.","In many villages people vote in the assembly."),
  ("Se busca llegar a un consenso.","They try to reach a consensus.")],
 "Singular noun, singular verb (*se nombra una autoridad*); plural noun, plural verb (*se nombran las autoridades*); no noun, singular verb (*se trabaja*). Do not put *a* before a thing: *se discuten los problemas*, not *se discuten a los problemas*.")
apply_gr(s,g)
apply_voc(s,[("el tequio","tequio, unpaid communal work","noun"),("la asamblea","assembly, community meeting","noun"),("el cargo","community post, service duty","noun"),("la autoridad","authority","noun"),("el consenso","consensus","noun"),("el municipio","municipality","noun")],
 "Community government","Tequio, assemblies and posts of service")
apply_ex(s,[
 match(s+".ex01",[("el tequio","tequio, unpaid communal work"),("la asamblea","assembly, community meeting"),("el cargo","community post, service duty"),("la autoridad","authority")],V),
 mc(s+".ex02","","grammar","Which sentence is correct?",
   ["En la asamblea se discuten los problemas del pueblo.","En la asamblea se discute los problemas del pueblo.","En la asamblea se discuten a los problemas del pueblo."],"pasiva-refleja"),
 fill(s+".ex03","Con el tequio se __ los caminos de la comunidad.","arreglan","With tequio the community's roads are repaired.","pasiva-refleja",hint="arreglar"),
 build(s+".ex04",["En","la","asamblea","se","decide","por","consenso."],"In the assembly, things are decided by consensus.","se-impersonal"),
 dlg(s+".ex05",[("Meg","¿Cómo se eligen las autoridades en esos pueblos?"),("Carlos","_____"),("Meg","Es muy interesante.")],
   ["Se eligen en la asamblea, donde vota toda la comunidad.","Se come muy bien en los mercados, donde hay comida de todo el estado.","Se viaja por carretera, y el viaje dura muchas horas desde la capital."],V),
 dict_(s+".ex06","En muchos municipios de Oaxaca se hacen trabajos para la comunidad que no se pagan.","In many municipalities of Oaxaca, work is done for the community that is not paid.","pasiva-refleja"),
])
# ---------------- 04
s='b2-mexicosur-04'
apply_lesson(s,"The Zapatista Uprising of 1994",
 "Explain what the Zapatistas did and why using para que with the subjunctive, and put the events in order.",
 "para que + subjunctive, present and imperfect",
 ["I can say what someone did so that something would happen, with *para que* and the subjunctive.",
  "I can put the main events of the Zapatista story in order, with their dates.",
  "I can say who said what, attributing it with *según*."])
wc[s]=apply_story(s,"El levantamiento zapatista de 1994",
 "On 1 January 1994 the EZLN rose up in Chiapas; the text follows the uprising, the talks of 1996 and the autonomous government the Zapatistas built.",
 ["para que + subjunctive","vocabulary of the Zapatista movement"],
 ["El 1 de enero de 1994, el mismo día en que entró en vigor el Tratado de Libre Comercio de América del Norte, un grupo armado de indígenas ocupó varias ciudades y pueblos de Chiapas, entre ellos San Cristóbal de las Casas. Se llamaba Ejército Zapatista de Liberación Nacional (EZLN). Sus miembros eran, en su mayoría, indígenas mayas, y muchos llevaban el rostro cubierto con pasamontañas.",
  "El EZLN explicó que se levantaba en armas porque, según sus comunicados, los pueblos indígenas vivían en la pobreza, sin tierra suficiente y sin derechos. Su lema fue «¡Ya basta!». El Gobierno federal envió al ejército y hubo combates durante unos doce días. El 12 de enero se declaró un alto el fuego, y después empezaron las negociaciones.",
  "En 1996, en San Andrés Larráinzar, el EZLN y el Gobierno firmaron los Acuerdos de San Andrés sobre derechos y cultura indígenas. Según el EZLN, el Gobierno no cumplió lo acordado. En 2001, el Congreso aprobó una reforma sobre derechos indígenas, pero el EZLN la rechazó porque, decía, no respetaba esos acuerdos.",
  "Los zapatistas decidieron organizar su propio gobierno en las comunidades donde tenían apoyo. En 2003 crearon los Caracoles, centros regionales, y las Juntas de Buen Gobierno. Según el EZLN, los crearon para que las comunidades decidieran cómo organizar la educación y la salud, con el principio de «mandar obedeciendo». Las Juntas de Buen Gobierno existieron hasta noviembre de 2023, cuando el EZLN anunció que las sustituía por Gobiernos Autónomos Locales."])
g=gr("grammar.b2.mexicosur.04.subjuntivo-de-finalidad-para-que","Doing Something So That Something Happens",
 "You know *para que* + the subjunctive from B1 Unit 4, and the imperfect subjunctive after a past verb from B1 Unit 38. They say what someone did so that something else would happen, which is how the Zapatista story explains its aims. The subjects are different; if the subject is the same, use *para* + infinitive (A2 Unit 30).",
 "Present and past purpose",
 [("Se reúnen para que todos puedan opinar.","present: main verb in the present, subjunctive in the present (they meet so that everyone can speak)"),
  ("Crearon escuelas para que los niños aprendieran en su lengua.","past: main verb in the past, imperfect subjunctive (they created schools so that the children would learn in their language)"),
  ("Hablaron con la prensa para que el mundo conociera su situación.","past: *conociera* after *hablaron* (they spoke to the press so that the world would know their situation)"),
  ("Lucharon para defender sus tierras.","same subject: *para* + infinitive (they fought to defend their lands)")],None,
 [("Los zapatistas se organizaron para que el Gobierno los escuchara.","The Zapatistas organised so that the government would listen to them."),
  ("Según el EZLN, crearon los Caracoles para que las comunidades decidieran por sí mismas.","According to the EZLN, they created the Caracoles so that the communities would decide for themselves."),
  ("Las comunidades se reúnen para que todos puedan hablar.","The communities meet so that everyone can speak."),
  ("Escribieron comunicados para que otras personas conocieran su situación.","They wrote communiqués so that other people would know their situation.")],
 "After *para que* the verb is always in the subjunctive: present (*puedan*) when the main verb is in the present, imperfect (*decidieran*, *conociera*) when the main verb is in the past. Never the indicative: not *para que decidían*.")
apply_gr(s,g)
apply_voc(s,[("el levantamiento","uprising","noun"),("la autonomía","autonomy, self-government","noun"),("el lema","slogan, motto","noun"),("el pasamontañas","balaclava, ski mask","noun"),("el comunicado","communiqué, official statement","noun")],
 "The Zapatista movement","Uprising, autonomy and talks")
apply_ex(s,[
 match(s+".ex01",[("el levantamiento","uprising"),("la autonomía","autonomy, self-government"),("el lema","slogan, motto"),("el pasamontañas","balaclava, ski mask")],V),
 mc(s+".ex02","","grammar","Which sentence says \"The communities organised so that the government would listen to them\"?",
   ["Las comunidades se organizaron para que el Gobierno las escuchara.","Las comunidades se organizaron para que el Gobierno las escucharía.","Las comunidades se organizaron para que el Gobierno las escuchó."],"subjuntivo-de-finalidad-para-que",{"1":"condicional-regular","2":"preterito-indefinido"}),
 fill(s+".ex03","Crearon escuelas propias para que los niños __ en su lengua.","aprendieran","They created their own schools so that the children would learn in their language.","subjuntivo-de-finalidad-para-que",hint="aprender, the children"),
 build(s+".ex04",["Se","reunieron","para","que","todos","pudieran","hablar."],"They met so that everyone could speak.","subjuntivo-de-finalidad-para-que"),
 dlg(s+".ex05",[("Carlos","¿Por qué escribían comunicados los zapatistas?"),("Meg","_____"),("Carlos","Entonces querían hablar con el mundo.")],
   ["Los escribían para que otras personas conocieran su situación.","Los escribían para que otras personas conocen su situación.","Los escribían para otras personas conocieran su situación."],"subjuntivo-de-finalidad-para-que",ds={"1":"present-tense"}),
 dict_(s+".ex06","Los zapatistas crearon los Caracoles para que las comunidades decidieran por sí mismas.","The Zapatistas created the Caracoles so that the communities would decide for themselves.","subjuntivo-de-finalidad-para-que"),
])
# ---------------- 05
s='b2-mexicosur-05'
apply_lesson(s,"The Maya Train, the Milpa and the Future of the South",
 "Present two sides of a debate about the Maya Train and the milpa with aunque, sin embargo and no obstante.",
 "aunque + indicative, sin embargo and no obstante",
 ["I can concede a point and then give another with *aunque*, *sin embargo* and *no obstante*.",
  "I can say who defends the Maya Train and who criticises it.",
  "I can describe the milpa and say what it grows."])
wc[s]=apply_story(s,"El Tren Maya y la milpa",
 "The Maya Train, opened in stages from December 2023, is defended by the federal government and criticised by some scientists and communities, while many families keep planting the traditional milpa.",
 ["aunque and contrast connectors","vocabulary of the debate on the south"],
 ["El sur de México vive un debate sobre su futuro. El Tren Maya es un ferrocarril de más de mil quinientos kilómetros que pasa por Chiapas, Tabasco, Campeche, Yucatán y Quintana Roo. El Gobierno federal lo impulsó y se inauguró por tramos desde diciembre de 2023.",
  "Según el Gobierno, el tren ayuda a regiones pobres, crea empleos y atrae turismo. Aunque estos argumentos son importantes para muchas personas, científicos, organizaciones ambientales y algunas comunidades mayas han criticado la obra. Dicen que puede dañar la selva, las cuevas y los cenotes, y que la consulta a las comunidades indígenas no cumplió las normas del Convenio 169 de la Organización Internacional del Trabajo. El Gobierno ha dicho que sí hizo consultas y que la obra cuida el medio ambiente.",
  "Otra forma de usar la tierra es la milpa, un sistema de cultivo muy antiguo. En el mismo terreno se siembran maíz, frijol y calabaza: el frijol da nitrógeno a la tierra y las hojas de la calabaza cubren el suelo. El maíz tiene su origen en México, y muchas familias campesinas mayas siguen sembrando milpa y guardan semillas de maíz criollo de una cosecha a otra.",
  "Para algunas personas, el tren y la milpa son dos maneras distintas de pensar el futuro; otras creen que pueden convivir. Sin embargo, el debate sigue abierto, y cada grupo defiende su punto de vista."])
g=gr("grammar.b2.mexicosur.05.concesivas-aunque","Giving Both Sides of a Debate",
 "You know *aunque* from A2 Unit 28, and *sin embargo* and *no obstante* from B1 Unit 1. A debate about the Maya Train needs both: you grant one side's point and then give the other. *Aunque* joins two clauses in one sentence; *sin embargo* and *no obstante* start a new sentence or clause.",
 "Three ways to give the other side",
 [("Aunque el tren crea empleos, algunas comunidades lo critican.","*aunque* + indicative in one sentence (although the train creates jobs, some communities criticise it)"),
  ("El tren crea empleos; sin embargo, algunas comunidades lo critican.","*sin embargo* after a semicolon or full stop (however)"),
  ("El tren crea empleos. No obstante, algunas comunidades lo critican.","*no obstante* starts a new sentence (nevertheless)")],None,
 [("Aunque la milpa necesita mucho trabajo, muchas familias la siguen sembrando.","Although the milpa needs a lot of work, many families keep planting it."),
  ("El Gobierno defiende el tren; sin embargo, algunos científicos temen por los cenotes.","The government defends the train; however, some scientists fear for the cenotes."),
  ("El tren llega a sitios arqueológicos. No obstante, algunas comunidades piden más consultas.","The train reaches archaeological sites. Nevertheless, some communities ask for more consultations."),
  ("Aunque el maíz es la base de la milpa, también se siembran frijol y calabaza.","Although maize is the base of the milpa, beans and squash are also planted.")],
 "*Sin embargo* and *no obstante* are followed by a comma. *Aunque* can come first or second: *aunque el tren crea empleos, algunas comunidades lo critican* means the same as *algunas comunidades lo critican aunque el tren crea empleos*.")
apply_gr(s,g)
apply_voc(s,[("la milpa","milpa, traditional field of maize, beans and squash","noun"),("el maíz","maize, corn","noun"),("el frijol","bean","noun"),("la calabaza","squash, pumpkin","noun"),("la consulta","consultation","noun"),("el impacto","impact","noun")],
 "The Maya Train and the milpa","Debate, milpa and consultation")
apply_ex(s,[
 match(s+".ex01",[("la milpa","milpa, traditional field of maize, beans and squash"),("el frijol","bean"),("la calabaza","squash, pumpkin"),("la consulta","consultation")],V),
 mc(s+".ex02","","grammar","Which sentence says \"Although the train creates jobs, some communities criticise it\"?",
   ["Aunque el tren crea empleos, algunas comunidades lo critican.","Porque el tren crea empleos, algunas comunidades lo critican.","Si el tren crea empleos, algunas comunidades lo critican."],"concesivas-aunque",{"1":"por-que-y-porque","2":"si-clauses"}),
 fill(s+".ex03","__ la milpa necesita mucho trabajo, muchas familias la siguen sembrando.","Aunque","Although the milpa needs a lot of work, many families keep planting it.","concesivas-aunque"),
 build(s+".ex04",["Aunque","el","tren","crea","empleos,","algunos","científicos","temen","su","impacto."],"Although the train creates jobs, some scientists fear its impact.","concesivas-aunque"),
 dlg(s+".ex05",[("Meg","¿Qué piensa la gente del Tren Maya?"),("Carlos","_____"),("Meg","Entonces hay varias opiniones.")],
   ["Aunque crea empleos, algunas personas temen su impacto en la selva.","Sale de Cancún por la mañana y llega a la ciudad por la tarde.","Necesita agua, sol y mucho trabajo durante todo el año."],V),
 dict_(s+".ex06","El Gobierno defiende el tren; sin embargo, algunas comunidades piden más consultas.","The government defends the train; however, some communities ask for more consultations.","contrast-concession-connectors"),
])
# ---------------- consolidation
s='b2-mexicosur-consolidation'
d=jl('lessons/b2/'+s+'.json')
d['goal']="Review the geography, peoples, community government, Zapatista history and debates of southern Mexico, and the grammar you used to talk about them."
d['grammar']="review: relative clauses, a pesar de, se, para que and aunque"
for sec in d['sections']:
    if sec['type']=='goal':
        sec['items']=["I can review what I learned about the landscape and peoples of the south.","I can use relative clauses, *a pesar de*, *se*, *para que* and *aunque* to talk about the south.","I can put the main events of the Zapatista story in order.","I can give both sides of the debate about the Maya Train."]
    if sec['type']=='checklist':
        sec['items']=["I can describe a cenote or a jungle with a relative clause.","I can say that a tradition continues in spite of pressure, with *a pesar de*.","I can explain what tequio and the assembly are, with *se*.","I can say what the Zapatistas did so that something would happen, with *para que*."]
jw('lessons/b2/'+s+'.json',d)
apply_ex(s,[
 match(s+".ex01",[("el cenote","cenote, natural sinkhole"),("el telar","loom"),("el tequio","tequio, unpaid communal work"),("la milpa","milpa, traditional field of maize, beans and squash")],V),
 mc(s+".ex02","","reading","According to the text, what is the tequio?",
   ["Un trabajo colectivo que la comunidad hace sin pago.","Un trabajo que el Gobierno paga a cada familia.","Una fiesta que se celebra una vez al año."]),
 mc(s+".ex03","","grammar","Which sentence is correct?",
   ["La selva en la que viven los jaguares está en Chiapas.","La selva que viven los jaguares está en Chiapas.","La selva en el que viven los jaguares está en Chiapas."],"relativas-preposicion-el-que"),
 fill(s+".ex04","El EZLN habló con la prensa para que el mundo __ su situación.","conociera","The EZLN spoke to the press so that the world would know its situation.","subjuntivo-de-finalidad-para-que",hint="conocer, the world"),
 {"id":s+".ex05","type":"sentence-order","category":"grammar","sentences":[
  "El 1 de enero de 1994 el EZLN ocupó varias ciudades de Chiapas. [On 1 January 1994 the EZLN occupied several towns in Chiapas.]",
  "El 12 de enero se declaró un alto el fuego. [On 12 January a ceasefire was declared.]",
  "En 1996 se firmaron los Acuerdos de San Andrés. [In 1996 the San Andrés Accords were signed.]",
  "En 2003 se crearon los Caracoles y las Juntas de Buen Gobierno. [In 2003 the Caracoles and the Juntas de Buen Gobierno were created.]"],
  "solution":[0,1,2,3],"teaches":["preterito-indefinido"]},
 dlg(s+".ex06",[("Carlos","¿Qué piensas del debate sobre el tren?"),("Meg","_____"),("Carlos","Sí, hay argumentos de los dos lados.")],
   ["Aunque el tren crea empleos, algunas comunidades lo critican.","Se arreglan los caminos con el tequio y se construyen escuelas.","Pese a las presiones, los pueblos hablan todavía su lengua en casa."],V),
 dict_(s+".ex07","Pese a las críticas, el tren empezó a funcionar en 2023.","Despite the criticism, the train began to operate in 2023.","a-pesar-de"),
 {"id":s+".ex08","type":"structured-writing","category":"writing","template":[
  {"prompt":"Say that Oaxaca is a state that has 570 municipalities, using que.","answer":"Oaxaca es un estado que tiene 570 municipios."},
  {"prompt":"Say that roads are repaired with tequio, using se.","answer":"Con el tequio se arreglan los caminos."},
  {"prompt":"Say that, despite the difficulties, the weavers still use their loom. Start with 'A pesar de'.","answer":"A pesar de las dificultades, las tejedoras usan todavía su telar."}],
  "teaches":[V]},
],"b2-mexicosur-consolidation-ex")
print(wc)
