from lib import *
V='b2-puerto-rico-vocab'
# ---------- 01
s='b2-puertorico-01'
paras=[
"Puerto Rico es una isla del Caribe que pertenece a Estados Unidos como territorio. En el noreste está el Bosque Nacional del Caribe, más conocido como El Yunque, el único bosque lluvioso tropical del sistema de bosques nacionales de Estados Unidos. Lo que más sorprende a muchos visitantes es la cantidad de lluvia: en las zonas altas llueve con frecuencia.",
"Fue en 1876 cuando la corona española declaró protegida esta región, y por eso El Yunque se considera una de las reservas forestales más antiguas del hemisferio occidental.",
"En el bosque vive el coquí, una rana muy pequeña que se oye sobre todo de noche; su nombre imita su canto. También vive allí la cotorra puertorriqueña, un ave en grave peligro de extinción que se protege con programas especiales.",
"Puerto Rico tiene además tres bahías bioluminiscentes: la bahía Mosquito, en la isla de Vieques; la Laguna Grande, en Fajardo; y La Parguera, en Lajas. Sus aguas brillan de noche cuando algo las mueve. Lo que produce la luz son unos organismos microscópicos. En 2008 el Libro Guinness de los Récords consideró la bahía Mosquito la más brillante del mundo.",
"En el suroeste el paisaje es muy distinto. El bosque seco de Guánica, que la UNESCO declaró reserva de la biosfera en 1981, recibe poca lluvia y tiene plantas adaptadas a la sequía. En el norte, el carso forma colinas de roca caliza y cuevas, como las del río Camuy.",
"Lo que hace especial a esta isla pequeña es la variedad de paisajes en poco espacio: en pocas horas se puede pasar del bosque lluvioso a una bahía que brilla de noche."]
put_story(s,"El Yunque y las bahías que brillan","Puerto Rico has a protected rainforest, bays whose water glows at night, a dry forest and a limestone region with caves, all on one small island.",paras,[
("According to the text, what is El Yunque?",["Es el único bosque lluvioso tropical del sistema de bosques nacionales de Estados Unidos.","Es una bahía de Vieques cuyas aguas brillan de noche.","Es un bosque seco del suroeste declarado reserva de la biosfera."],"The first paragraph describes El Yunque."),
("What produces the light in the bioluminescent bays?",["Unos organismos microscópicos.","Unas ranas muy pequeñas.","Las cuevas del carso."],"The fourth paragraph says tiny organisms produce the light."),
("What does the text say about the dry forest of Guánica?",["Recibe poca lluvia, y la UNESCO lo declaró reserva de la biosfera en 1981.","Es el bosque más antiguo, protegido por la corona española en 1876.","Es el lugar donde vive la cotorra puertorriqueña."],"The fifth paragraph describes it.")])
put_voc(s,"","Rainforest, bays and karst","Nature words for Puerto Rico",[("el coquí","coquí (tiny tree frog)","noun"),("la cotorra","parrot","noun"),("el carso","karst (limestone landscape)","noun"),("el bosque lluvioso","rainforest","noun")])
put_gr(s,"Cleft Sentences: Putting One Idea in the Spotlight",[
T("You know cleft sentences with *lo que* from B2 Unit 1: *lo que* + verb + *ser* + the idea you stress (*Lo que más nos sorprendió fue su serenidad*), and *fue* + person, place or time + *quien*, *donde* or *cuando*. Nature writing uses them to point at the one fact worth remembering: what surprises visitors, where something happens, when it began.","What you already know"),
TB("Three spotlights on Puerto Rico",[
["Lo que más sorprende a los visitantes es la cantidad de lluvia.","*lo que* + verb + *es*: the spotlight is the rain"],
["Fue la corona española la que protegió esta región.","*fue* + who + *la que*: the spotlight is who did it"],
["Fue en 1876 cuando se protegió esta región.","*fue* + time + *cuando*: the spotlight is when"]]),
EX("In context",[
("Lo que produce la luz son unos organismos microscópicos.","What produces the light is tiny organisms."),
("Fue en Vieques donde se midió el mayor brillo de una bahía.","It was in Vieques that the brightest bay was measured."),
("Fue en 1876 cuando la corona española declaró protegida esta región.","It was in 1876 that the Spanish crown declared this region protected."),
("Lo que hace especial a la isla es la variedad de paisajes.","What makes the island special is the variety of landscapes.")]),
TIP("The tense of *ser* follows the other verb: *Lo que sorprende es…* (present), *Fue en 1876 cuando…* (past). When the spotlighted piece is plural, careful writing makes *ser* agree: *Lo que produce la luz son unos organismos*. Use a cleft sentence for the one idea you want remembered, not in every sentence.")])
put_lesson(s,"Puerto Rico: El Yunque and the bays that glow","Describe the rainforest, bioluminescent bays and karst of Puerto Rico with cleft sentences (*Lo que…*, *Fue … cuando*).","cleft sentences, applied to Puerto Rico's nature",[
"I can put one idea in the spotlight with a cleft sentence (*Lo que… es…*, *Fue… cuando…*).",
"I can say what El Yunque and the bioluminescent bays are and why they are special.",
"I can use the new words for the coquí, the parrot and the karst."])
put_ex(s,[
match(s+'.ex01',[["el coquí","coquí (tiny tree frog)"],["la cotorra","parrot"],["el carso","karst (limestone landscape)"],["el bosque lluvioso","rainforest"]],V),
mc(s+'.ex02',"grammar","Which sentence puts the spotlight on the Spanish crown as the one who protected the region in 1876?",["Fue la corona española la que protegió esta región en 1876.","Fue la corona española el que protegió esta región en 1876.","Fue la corona española la que protegieron esta región en 1876."],"oraciones-hendidas-enfasis"),
fill(s+'.ex03',"Lo __ más sorprende a los visitantes es la cantidad de lluvia.","que","What surprises visitors most is the amount of rain.","oraciones-hendidas-enfasis"),
build(s+'.ex04',"Lo que produce la luz son unos organismos microscópicos.","What produces the light is tiny organisms.","oraciones-hendidas-enfasis"),
dlg(s+'.ex05',"¿Qué es el coquí?","","¡Qué curioso!",["Es un animal muy pequeño que se oye sobre todo de noche.","Es un ave rara que se protege en El Yunque.","Es una roca caliza con colinas y cuevas en el norte."],V),
dict_(s+'.ex06',"Fue en 1876 cuando la corona española protegió esta región.","It was in 1876 that the Spanish crown protected this region.","oraciones-hendidas-enfasis")])
# ---------- 02
s='b2-puertorico-02'
paras=[
"El 23 de septiembre de 1868 un grupo de puertorriqueños se levantó contra el dominio español en el pueblo de Lares. Es el episodio que se conoce como el Grito de Lares. La rebelión se había preparado en parte desde el exterior, con líderes como Ramón Emeterio Betances, que vivía fuera de la isla.",
"Los rebeldes proclamaron la República de Puerto Rico y pidieron el fin de la esclavitud. En pocos días las fuerzas españolas derrotaron el levantamiento. La esclavitud se abolió en la isla en 1873, cinco años después de que ocurrió el Grito de Lares.",
"En 1897 España concedió a Puerto Rico una carta de autonomía, antes de que empezara la guerra con Estados Unidos. El nuevo gobierno de la isla empezó a trabajar a principios de 1898, meses antes de que llegaran las tropas estadounidenses.",
"Las tropas estadounidenses desembarcaron en Guánica, en el sur de la isla, el 25 de julio de 1898. Después de que terminó la guerra, el Tratado de París, firmado el 10 de diciembre de 1898, cedió Puerto Rico a Estados Unidos. Por el mismo tratado, España cedió Guam, vendió Filipinas y renunció a Cuba. Los puertorriqueños no participaron en la negociación.",
"En 1900 la Ley Foraker estableció un gobierno civil, con un gobernador nombrado por el presidente de Estados Unidos. Hasta 1948 los gobernadores fueron nombrados desde Washington; el primero elegido por los puertorriqueños fue Luis Muñoz Marín, en 1948.",
"Los historiadores valoran estos hechos de manera distinta: unos ven en 1868 el origen del movimiento independentista, y otros destacan la autonomía de 1897 y los cambios que trajo 1898."]
put_story(s,"Del Grito de Lares a 1898","In 1868 an uprising in Lares was defeated, in 1897 Spain granted autonomy, and in 1898 the war and the Treaty of Paris placed Puerto Rico under United States rule.",paras,[
("What happened in Lares on 23 September 1868?",["Un grupo de puertorriqueños se levantó contra el dominio español.","Las tropas estadounidenses desembarcaron en la isla.","España concedió una carta de autonomía a Puerto Rico."],"The first paragraph describes the Grito de Lares."),
("According to the text, when did autonomy arrive?",["España concedió una carta de autonomía en 1897, antes de la guerra con Estados Unidos.","Estados Unidos concedió la autonomía en 1900, con la Ley Foraker.","La autonomía llegó en 1873, con el fin de la esclavitud."],"The third paragraph gives the date."),
("What did the Treaty of Paris of 10 December 1898 do with Puerto Rico?",["Lo cedió a Estados Unidos.","Lo declaró una república independiente.","Lo devolvió a la corona española."],"The fourth paragraph describes the treaty.")])
put_voc(s,"","Uprising, treaty and rule","Words about 1868 and 1898",[("el levantamiento","uprising","noun"),("la cesión","cession, handing over","noun"),("la esclavitud","slavery","noun"),("el tratado","treaty","noun")])
put_gr(s,"Antes de que and Después de que: Ordering 1868 and 1898",[
T("You know *antes de que* and *después de que* from B2 Unit 7. After *antes de que* the verb is always in the subjunctive. After *después de que* it is the indicative for something that happened and the subjunctive for something still to come. With the same subject, *antes de* and *después de* + infinitive (A2 Unit 4) are enough. The Spanish–American War is a story of one event before or after another.","What you already know"),
TB("Before and after",[
["Antes de que empezara la guerra, España concedió la autonomía.","*antes de que* + imperfect subjunctive: always the subjunctive"],
["Después de que terminó la guerra, se firmó el tratado.","*después de que* + indicative: it happened"],
["Después de que leas sobre 1898, entenderás el tratado.","*después de que* + subjunctive: not yet happened"],
["Antes de viajar a San Juan, leemos sobre su historia.","same subject: *antes de* + infinitive"]]),
EX("In context",[
("España concedió la autonomía antes de que empezara la guerra con Estados Unidos.","Spain granted autonomy before the war with the United States began."),
("El gobierno de la isla empezó a trabajar meses antes de que llegaran las tropas estadounidenses.","The island's government began to work months before the American troops arrived."),
("Después de que terminó la guerra, el tratado cedió Puerto Rico a Estados Unidos.","After the war ended, the treaty handed Puerto Rico over to the United States."),
("La esclavitud se abolió en 1873, cinco años después de que ocurrió el Grito de Lares.","Slavery was abolished in 1873, five years after the Grito de Lares happened.")]),
TIP("Two questions decide everything. Who does the second action? The same person: infinitive. Someone else: *que* + verb. And for *después de que*, has it happened? Yes: indicative. Not yet: subjunctive. After *antes de que* there is no second question: *antes de que empezó* is always wrong.")])
put_lesson(s,"The Grito de Lares and 1898","Tell what happened in 1868 and 1898 and put events in order with *antes de que* and *después de que*.","antes de que and después de que, applied to 1868 and 1898",[
"I can say that one event happened before or after another with *antes de que* and *después de que*.",
"I can say what happened in Lares in 1868 and what the Treaty of Paris did in 1898.",
"I can use the new words for uprising, cession, slavery and treaty."])
put_ex(s,[
match(s+'.ex01',[["el levantamiento","uprising"],["la cesión","cession, handing over"],["la esclavitud","slavery"],["el tratado","treaty"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "Spain granted autonomy before the war with the United States began"?',["España concedió la autonomía antes de que empezara la guerra con Estados Unidos.","España concedió la autonomía antes de que empezó la guerra con Estados Unidos.","España concedió la autonomía antes de que empiece la guerra con Estados Unidos."],"antes-despues-de-que",ds={"1":"preterito-indefinido","2":"subjuntivo-morfologia"}),
fill(s+'.ex03',"La esclavitud se abolió en 1873, cinco años después de que __ el Grito de Lares.","ocurrió","Slavery was abolished in 1873, five years after the Grito de Lares happened.","antes-despues-de-que",hint="ocurrir"),
build(s+'.ex04',"Después de que terminó la guerra, el tratado cedió Puerto Rico a Estados Unidos.","After the war ended, the treaty handed Puerto Rico over to the United States.","antes-despues-de-que"),
dlg(s+'.ex05',"¿Qué fue el Grito de Lares?","","Entonces es una fecha importante.",["Fue un levantamiento contra España, en 1868.","Fue el tratado que cedió la isla a Estados Unidos en 1898.","Fue la ley que creó un gobierno civil en 1900."],V),
dict_(s+'.ex06',"Antes de que llegaran las tropas estadounidenses, el nuevo gobierno de la isla ya trabajaba.","Before the American troops arrived, the island's new government was already working.","antes-despues-de-que")])
# ---------- 03
s='b2-puertorico-03'
paras=[
"Puerto Rico pertenece a Estados Unidos desde 1898, y desde 1917, por la Ley Jones, los puertorriqueños son ciudadanos estadounidenses. En 1952 entró en vigor la Constitución de Puerto Rico, aprobada antes por los votantes, y la isla pasó a llamarse Estado Libre Asociado, o Commonwealth en inglés.",
"En 1953 la ONU dejó de incluir a Puerto Rico en la lista de territorios sin gobierno propio, después de que Estados Unidos dejó de enviar informes sobre la isla. Desde entonces se discute si el estatus cambió realmente, y las posturas son distintas: algunos partidos y organizaciones puertorriqueños dicen que no; el gobierno de Estados Unidos y otros partidos afirman que los puertorriqueños ejercieron su derecho a decidir.",
"Los puertorriqueños que viven en la isla no votan en las elecciones generales para presidente de Estados Unidos, y su comisionado residente en el Congreso no tiene voto en el pleno. Por eso el estatus político es un tema central en la política de la isla.",
"Se discuten cuatro opciones: mantener el Estado Libre Asociado, convertirse en estado, ser independiente o elegir la libre asociación, una relación pactada entre dos países. Si Puerto Rico fuera un estado, sus ciudadanos elegirían senadores con voto. Si fuera independiente, tendría su propia política exterior. Si eligiera la libre asociación, firmaría un acuerdo con Estados Unidos.",
"Los puertorriqueños han votado en varias consultas sobre el estatus, entre ellas las de 1967, 1993, 1998, 2012, 2017, 2020 y 2024. Ninguna es vinculante, porque la decisión final corresponde al Congreso de Estados Unidos. En 2017 ganó la estadidad, pero votó solo una parte pequeña del electorado, porque varios partidos pidieron no participar. En noviembre de 2024 hubo otra consulta no vinculante, y la estadidad obtuvo más votos que las otras opciones.",
"Jenniffer González, que apoya la estadidad, gobierna la isla desde enero de 2025. Otros partidos defienden el Estado Libre Asociado o la independencia."]
put_story(s,"El estatus de Puerto Rico","Puerto Ricans are United States citizens, the island is a Commonwealth since 1952, and the options for its status (state, independence, free association, the current status) are debated; the text gives the options and the votes without a verdict.",paras,[
("According to the text, why are the status votes not binding?",["Porque la decisión final corresponde al Congreso de Estados Unidos.","Porque solo votan los puertorriqueños que viven fuera de la isla.","Porque la ONU no las reconoce como elecciones."],"The fifth paragraph explains this."),
("What does the text say happened in 2017?",["Ganó la estadidad, pero votó solo una parte pequeña del electorado.","Ganó la independencia con la mayoría de los votos.","No se celebró ninguna consulta sobre el estatus."],"The fifth paragraph describes the vote."),
("Which options does the text list for the island's status?",["Mantener el ELA, convertirse en estado, ser independiente o elegir la libre asociación.","Solo mantener el ELA o convertirse en estado.","Solo la independencia o volver a la corona española."],"The fourth paragraph lists four options.")])
put_voc(s,"","Status and votes","Words for the status debate",[("la estadidad","statehood","noun"),("la consulta","vote, referendum","noun"),("vinculante","binding","adjective"),("el comisionado","commissioner, delegate","noun")])
put_gr(s,"Si + Imperfect Subjunctive: Imagining Each Option",[
T("You know the imagined *si* from B1 Unit 4: *si* + the imperfect subjunctive, with the conditional in the result (*Si yo fuera tú, hablaría con el profesor*). It is the natural way to describe what each status option would mean, because each one is a situation that does not exist yet. The sentences here describe the options without taking sides.","What you already know"),
TB("One option, one imagined result",[
["Si Puerto Rico fuera un estado, sus ciudadanos elegirían senadores con voto.","*fuera* (imperfect subjunctive) + *elegirían* (conditional)"],
["Si fuera independiente, tendría su propia política exterior.","*fuera* + *tendría*"],
["Si eligiera la libre asociación, firmaría un acuerdo con Estados Unidos.","*eligiera* + *firmaría*"]]),
EX("In context",[
("Si Puerto Rico fuera un estado, tendría dos senadores en el Congreso.","If Puerto Rico were a state, it would have two senators in Congress."),
("Si la isla fuera independiente, tendría su propia política exterior.","If the island were independent, it would have its own foreign policy."),
("Si los resultados fueran vinculantes, el Congreso tendría que respetarlos.","If the results were binding, Congress would have to respect them."),
("Si eligieran la libre asociación, firmarían un acuerdo con Estados Unidos.","If they chose free association, they would sign an agreement with the United States.")]),
TIP("Never put the conditional after *si*: say *si fuera*, not *si sería*. The *-ra* and *-se* forms are the same (*fuera* and *fuese*). Say each option the same way, with a *si* clause and a result, and the sentence describes it without judging it.")])
put_lesson(s,"The status of Puerto Rico: the options and the votes","Give the options for Puerto Rico's political status and the votes, with *si* + imperfect subjunctive and no verdict.","hypothetical conditions with si + imperfect subjunctive, applied to Puerto Rico's status",[
"I can describe what an imagined situation would mean with *si* + imperfect subjunctive and the conditional.",
"I can say what the four status options are and how the votes went, without taking sides.",
"I can use the new words for statehood, a binding vote and the resident commissioner."])
put_ex(s,[
match(s+'.ex01',[["la estadidad","statehood"],["la consulta","vote, referendum"],["vinculante","binding"],["el comisionado","commissioner, delegate"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "If Puerto Rico were a state, its citizens would elect senators with a vote"?',["Si Puerto Rico fuera un estado, sus ciudadanos elegirían senadores con voto.","Si Puerto Rico es un estado, sus ciudadanos elegirían senadores con voto.","Si Puerto Rico sería un estado, sus ciudadanos elegirían senadores con voto."],"hypothetical-structures",ds={"1":"present-tense","2":"condicional-regular"}),
fill(s+'.ex03',"Si Puerto Rico __ un país independiente, tendría su propia política exterior.","fuera","If Puerto Rico were an independent country, it would have its own foreign policy.","hypothetical-structures",answers=["fuera","fuese"],hint="ser"),
build(s+'.ex04',"Si Puerto Rico eligiera la libre asociación, firmaría un acuerdo con Estados Unidos.","If Puerto Rico chose free association, it would sign an agreement with the United States.","hypothetical-structures"),
dlg(s+'.ex05',"¿Qué significa que una consulta no sea vinculante?","","Ahora entiendo por qué importa el Congreso.",["Significa que el resultado no obliga al Congreso a hacer nada.","Significa que solo votan los ciudadanos que viven fuera de la isla.","Significa que la votación es obligatoria para todos los ciudadanos."],V),
dict_(s+'.ex06',"Si la isla fuera independiente, tendría su propia política exterior.","If the island were independent, it would have its own foreign policy.","hypothetical-structures")])
# ---------- 04
s='b2-puertorico-04'
paras=[
"La música de Puerto Rico mezcla herencias africanas y europeas. Esa mezcla se oye en cuatro géneros muy conocidos: la bomba, la plena, la salsa y el reggaetón.",
"La bomba nació entre personas africanas esclavizadas en las plantaciones de caña de azúcar. Se toca con tambores llamados barriles, y la persona que baila dialoga con el tambor principal. Si bien nació en las plantaciones, hoy se baila en festivales de toda la isla; la localidad de Loíza, en la costa norte, es famosa por esta tradición.",
"La plena nació a principios del siglo XX en Ponce, en el sur de la isla. Se toca con panderos, que son tambores de mano, y sus letras cuentan historias y noticias, por eso a veces se la llama el periódico cantado.",
"La salsa se formó en Nueva York en los años sesenta y setenta, entre músicos puertorriqueños, cubanos y de otros países. El sello discográfico Fania ayudó a difundirla por América Latina. Si bien la salsa no nació en la isla, músicos de origen puertorriqueño como Héctor Lavoe y Willie Colón fueron figuras importantes de este género.",
"El reggaetón nació en los años noventa en barrios de San Juan, con influencias del reggae de Panamá, del dancehall de Jamaica y del hip hop. Al principio algunos grupos lo criticaron por sus letras. Si bien fue criticado al principio, desde los años 2000 se escucha en todo el mundo, y la canción «Gasolina», de Daddy Yankee, fue en 2004 uno de sus primeros grandes éxitos internacionales.",
"Así, cuatro géneros nacidos en épocas y lugares distintos muestran partes diferentes de la historia de Puerto Rico y de su diáspora."]
put_story(s,"Bomba, plena, salsa y reggaetón","Four music styles tell parts of Puerto Rico's history: bomba from the plantations, plena from Ponce, salsa from New York and reggaeton from San Juan.",paras,[
("According to the text, where did the plena begin?",["En Ponce, a principios del siglo XX.","En Nueva York, en los años sesenta.","En las plantaciones de Loíza, en el siglo XIX."],"The third paragraph says so."),
("What does the text say about salsa?",["Se formó en Nueva York entre músicos de varios países, y el sello Fania ayudó a difundirla.","Nació en las plantaciones de caña de azúcar de la costa norte.","Nació en los barrios de San Juan en los años noventa."],"The fourth paragraph describes salsa."),
("What influences did reggaeton have, according to the text?",["El reggae de Panamá, el dancehall de Jamaica y el hip hop.","Los panderos de Ponce y los barriles de Loíza.","El sello Fania y la música de Cuba."],"The fifth paragraph lists them.")])
put_voc(s,"","Drums, labels and genres","Words for Puerto Rican music",[("el barril","barrel drum (used in bomba)","noun"),("el pandero","hand drum, tambourine","noun"),("el sello","record label","noun"),("la plena","plena (music of Ponce)","noun")])
put_gr(s,"Si Bien: Granting a Point About Music",[
T("You know *si bien* from B2 Unit 8: a formal way to say \"although it is true that\", with the indicative. The speaker grants a true point and then says what matters more. Music history is full of such points: a style was born in one place and became famous in another, or it was criticised and then loved.","What you already know"),
TB("Grant the point, then say the main idea",[
["Si bien la salsa no nació en la isla, muchos puertorriqueños fueron figuras importantes.","grants a true point (born elsewhere), then the main idea"],
["Si bien el reggaetón fue criticado, hoy se escucha en todo el mundo.","grants the criticism, then the main idea"],
["La bomba, si bien nació en las plantaciones, hoy se baila en festivales.","*si bien* in the middle, between commas"]]),
EX("In context",[
("Si bien la bomba nació en las plantaciones, hoy se baila en festivales de toda la isla.","Although bomba was born on the plantations, today it is danced at festivals all over the island."),
("Si bien la plena nació en Ponce, hoy se toca en toda la isla.","Although plena was born in Ponce, today it is played all over the island."),
("Si bien la salsa se formó en Nueva York, muchos de sus músicos eran de origen puertorriqueño.","Although salsa took shape in New York, many of its musicians were of Puerto Rican origin."),
("El reggaetón, si bien tiene influencias de Panamá y Jamaica, nació en San Juan.","Reggaeton, although it has influences from Panama and Jamaica, was born in San Juan.")]),
TIP("*Si bien* is formal and takes the indicative, because the fact is true. Do not add *que* after it, and do not use the subjunctive: for \"even if\" you need *aunque*. In a message to a friend, *aunque* is more natural; *si bien* fits an article or a talk.")])
put_lesson(s,"Bomba, plena, salsa and reggaeton","Describe four Puerto Rican music styles and grant a point formally with *si bien*.","formal concessive clauses with si bien, applied to Puerto Rican music",[
"I can grant a true point and then give the main idea with *si bien*.",
"I can say where and when bomba, plena, salsa and reggaeton began.",
"I can use the new words for barrel drums, hand drums and record labels."])
put_ex(s,[
match(s+'.ex01',[["el barril","barrel drum (used in bomba)"],["el pandero","hand drum, tambourine"],["el sello","record label"],["la plena","plena (music of Ponce)"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "Although salsa was not born on the island, many Puerto Ricans were important figures in it"?',["Si bien la salsa no nació en la isla, muchos puertorriqueños fueron figuras importantes.","Si bien que la salsa no nació en la isla, muchos puertorriqueños fueron figuras importantes.","Si bien la salsa no naciera en la isla, muchos puertorriqueños fueron figuras importantes."],"concesivas-si-bien",ds={"2":"imperfect-subjunctive-forms"}),
fill(s+'.ex03',"__ bien el reggaetón fue criticado al principio, hoy se escucha en todo el mundo.","Si","Although reggaeton was criticised at first, today it is heard all over the world.","concesivas-si-bien"),
build(s+'.ex04',"Si bien la bomba nació en las plantaciones, hoy se baila en festivales.","Although bomba was born on the plantations, today it is danced at festivals.","concesivas-si-bien"),
dlg(s+'.ex05',"¿Qué es un barril en la bomba?","","Ahora entiendo cómo suena.",["Es un tambor grande con el que se toca la música.","Es un baile popular de la ciudad de Ponce.","Es una empresa de Nueva York que vende música."],V),
dict_(s+'.ex06',"Si bien la plena nació en Ponce, hoy se toca en toda la isla.","Although plena was born in Ponce, today it is played all over the island.","concesivas-si-bien")])
# ---------- 05
s='b2-puertorico-05'
paras=[
"El 20 de septiembre de 2017 el huracán María llegó a Puerto Rico como huracán de categoría 4. Destruyó casas y carreteras y dejó sin electricidad a toda la isla; en algunas zonas la luz tardó meses en volver.",
"Las cifras de muertos se discuten. Según un estudio de la Universidad George Washington, que el gobierno de Puerto Rico adoptó como cifra oficial en 2018, murieron 2975 personas más de lo normal entre septiembre de 2017 y febrero de 2018. Es una estimación, no un recuento.",
"La isla ya vivía una crisis económica. En 2016 el Congreso de Estados Unidos aprobó la ley PROMESA, que creó una Junta de Supervisión Fiscal con el fin de controlar el presupuesto y de negociar la deuda pública, que el gobierno no podía pagar. En 2017 el gobierno pidió protección legal para reestructurar la deuda. Los críticos de la Junta dicen que sus recortes afectan a servicios públicos; otros sostienen que son necesarios para ordenar las cuentas.",
"Después de María, muchas comunidades se organizaron con el fin de repartir agua y comida, y algunas organizaciones, como Casa Pueblo, en Adjuntas, instalaron paneles solares con miras a tener electricidad durante futuros apagones.",
"En julio de 2019, después de muchos días de protestas por la publicación de mensajes privados de funcionarios, renunció el gobernador Ricardo Rosselló.",
"Estos años pusieron en el centro del debate la relación entre la isla y Estados Unidos y la capacidad de las comunidades para organizarse."]
put_story(s,"El huracán María, la deuda y la organización de la gente","Hurricane María in 2017, the debt crisis and the law PROMESA of 2016, and the ways communities organised afterwards; the death toll is given only as an attributed estimate.",paras,[
("According to the text, what is the figure of 2975?",["Una estimación de muertos hecha por la Universidad George Washington, adoptada por el gobierno.","El número de casas que destruyó el huracán María.","La cantidad de personas que protestaron en 2019."],"The second paragraph attributes the figure."),
("What did the law PROMESA do in 2016?",["Creó una Junta de Supervisión Fiscal para controlar el presupuesto y negociar la deuda.","Declaró la independencia de Puerto Rico.","Instaló paneles solares en las comunidades."],"The third paragraph describes the law."),
("What did Casa Pueblo do after María, according to the text?",["Instaló paneles solares con miras a tener electricidad durante futuros apagones.","Negoció la deuda pública con el Congreso.","Pidió la renuncia del gobernador en 2019."],"The fourth paragraph mentions Casa Pueblo.")])
put_voc(s,"","Blackouts, debt and boards","Words after María",[("el apagón","blackout, power cut","noun"),("la deuda","debt","noun"),("la junta","board, council","noun"),("el recorte","cut (in spending)","noun"),("repartir","to hand out, distribute","verb")])
put_gr(s,"Purpose Connectors: Con El Fin de, Con Miras A",[
T("You know the purpose phrases *con miras a* and *con vistas a* from B2 Unit 12: *con el fin de* + infinitive, *con miras a* and *con vistas a* \"with a view to\" + infinitive or noun, and *de modo que* + subjunctive when the subject changes. After a disaster and a debt crisis, people and institutions act for a purpose, and these phrases say what for.","What you already know"),
TB("What is it for?",[
["La ley creó una junta con el fin de controlar el presupuesto.","*con el fin de* + infinitive: in order to"],
["Instalaron paneles solares con miras a tener electricidad durante los apagones.","*con miras a* + infinitive: with a view to"],
["Se preparan con vistas a la próxima temporada de huracanes.","*con vistas a* + noun: with a view to"],
["Repartieron agua de modo que todos los vecinos pudieran beber.","*de modo que* + subjunctive: so that (two subjects)"]]),
EX("In context",[
("Muchas comunidades se organizaron con el fin de repartir agua y comida.","Many communities organised in order to hand out water and food."),
("Casa Pueblo instaló paneles solares con miras a tener electricidad durante los apagones.","Casa Pueblo installed solar panels with a view to having electricity during blackouts."),
("El gobierno publicó la lista con vistas a la reunión de la Junta.","The government published the list with the Board's meeting in mind."),
("Repartieron agua de modo que todos los vecinos pudieran beber.","They handed out water so that all the neighbours could drink.")]),
TIP("The preposition after *fin* is *de*, and after *miras* and *vistas* it is always *a*, never *para* or *en*. After *con el fin de* and *con miras a* use an infinitive when you name the action. Use *de modo que* + subjunctive when a different person does the next action: *de modo que todos pudieran beber*.")])
put_lesson(s,"Hurricane María, the debt and the response","Explain what happened after Hurricane María and what people and institutions did, and for what purpose (*con el fin de*, *con miras a*).","purpose connectors, applied to Hurricane María, the debt and community response",[
"I can say what an action is for with *con el fin de*, *con miras a* and *de modo que*.",
"I can say what happened in 2016, 2017 and 2019 and give the death toll as an attributed estimate.",
"I can use the new words for blackout, debt, board and spending cuts."])
put_ex(s,[
match(s+'.ex01',[["el apagón","blackout, power cut"],["la deuda","debt"],["la junta","board, council"],["el recorte","cut (in spending)"]],V),
mc(s+'.ex02',"grammar",'Which sentence means "The law created a board in order to control the budget"?',["La ley creó una junta con el fin de controlar el presupuesto.","La ley creó una junta con el fin para controlar el presupuesto.","La ley creó una junta con el fin de controla el presupuesto."],"purpose-connectors",ds={"2":"present-tense"}),
fill(s+'.ex03',"Instalaron paneles solares con miras __ tener electricidad durante los apagones.","a","They installed solar panels with a view to having electricity during blackouts.","purpose-connectors"),
build(s+'.ex04',"Muchas comunidades se organizaron con el fin de repartir agua y comida.","Many communities organised in order to hand out water and food.","purpose-connectors"),
dlg(s+'.ex05',"¿Qué es un apagón?","","Entonces no había luz en toda la zona.",["Es un corte de electricidad que deja sin luz a una zona.","Es una deuda que el gobierno no puede pagar.","Es una junta que controla el presupuesto de la isla."],V),
dict_(s+'.ex06',"Repartieron agua de modo que todos los vecinos pudieran beber.","They handed out water so that all the neighbours could drink.","purpose-connectors")])
# ---------- consolidation
s='b2-puertorico-consolidation'
put_lesson(s,"Unit 12 Review: Puerto Rico","Review Puerto Rico from El Yunque to Hurricane María, with cleft sentences, *antes de que* and *después de que*, *si* + imperfect subjunctive, *si bien* and purpose phrases.","review: cleft sentences, antes de que and después de que, hypothetical si, si bien, purpose connectors",[
"I can review what I learned about Puerto Rico, from El Yunque to 2019.",
"I can use cleft sentences, *antes de que*, *si* + imperfect subjunctive, *si bien* and *con el fin de*.",
"I can put events from 1868 to 2017 in order.",
"I can give the options and the votes on the island's status without taking sides."],
checklist=[
"I can put one idea in the spotlight with a cleft sentence (*Lo que… es…*, *Fue… cuando…*).",
"I can say that one event happened before or after another with *antes de que* and *después de que*.",
"I can describe what each option would mean with *si* + imperfect subjunctive and the conditional.",
"I can grant a true point and give the main idea with *si bien*.",
"I can say what an action is for with *con el fin de* and *con miras a*."])
put_ex(s,[
match(s+'.ex01',[["el coquí","coquí (tiny tree frog)"],["el levantamiento","uprising"],["la estadidad","statehood"],["el apagón","blackout, power cut"]],V),
mc(s+'.ex02',"grammar",'Which sentence says "What surprises visitors about the bays is the light"?',["Lo que sorprende a los visitantes de las bahías es la luz.","Lo sorprende a los visitantes de las bahías es la luz.","Que sorprende a los visitantes de las bahías es la luz."],"oraciones-hendidas-enfasis"),
mc(s+'.ex03',"reading","According to the texts, what did the Treaty of Paris of December 1898 do?",["Cedió Puerto Rico a Estados Unidos.","Creó la Junta de Supervisión Fiscal.","Concedió una carta de autonomía a la isla."],None),
fill(s+'.ex04',"Muchos músicos de salsa eran de Puerto Rico, __ bien la salsa se formó en Nueva York.","si","Many salsa musicians were from Puerto Rico, although salsa took shape in New York.","concesivas-si-bien"),
{"id":s+".ex05","type":"sentence-order","category":"grammar","sentences":["En 1868 los rebeldes proclamaron la República en Lares. [In 1868 the rebels proclaimed the Republic in Lares.]","En 1898 las tropas estadounidenses desembarcaron en Guánica. [In 1898 American troops landed at Guánica.]","En 1952 entró en vigor la Constitución del Estado Libre Asociado. [In 1952 the Constitution of the Commonwealth came into force.]","En 2017 el huracán María llegó a la isla. [In 2017 Hurricane María reached the island.]"],"solution":[0,1,2,3],"teaches":["preterito-indefinido"]},
dlg(s+'.ex06',"¿Qué es El Yunque?","","Me gustaría verlo algún día.",["Es un bosque lluvioso protegido en el noreste de la isla.","Es una ciudad del sur donde nació la plena.","Es una junta que controla el presupuesto de la isla."],V),
dict_(s+'.ex07',"Si Puerto Rico fuera un estado, tendría dos senadores en el Congreso.","If Puerto Rico were a state, it would have two senators in Congress.","hypothetical-structures"),
{"id":s+".ex08","type":"structured-writing","category":"writing","template":[{"prompt":"Say that many communities organised in order to hand out water and food. Start with \"Muchas comunidades se organizaron\".","answer":"Muchas comunidades se organizaron con el fin de repartir agua y comida."}],"teaches":["purpose-connectors"]}])
