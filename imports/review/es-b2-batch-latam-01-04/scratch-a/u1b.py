import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
# ---------------- LESSON 03
s='b2-mexicocentro-03'
items=["I can use a stance adverb such as en realidad or indudablemente to show how I see a fact about the colonial city.",
"I can place a stance adverb and its commas correctly.",
"I can say who Sor Juana was and what the casta system was.",
"I can use the lesson's words for the viceroyalty, the convent and the baroque church."]
lesson_update(s,"The colonial city: viceroys, castes and Sor Juana","Use stance adverbs to show how you see the facts about colonial Mexico City, its society and Sor Juana.","stance adverbs (recap)",items)
story_update(s,"La capital del virreinato y Sor Juana","Mexico City was the capital of the viceroyalty of New Spain for three centuries; the text describes its institutions, its caste system, the writer Sor Juana Inés de la Cruz and its baroque architecture.",[
"Durante casi tres siglos, desde la conquista hasta 1821, la Ciudad de México fue la capital de Nueva España; el virreinato propiamente dicho empezó en 1535. Allí vivían el virrey y el arzobispo, funcionaba la Real y Pontificia Universidad y, desde 1539, había una imprenta, la primera de América. Por el puerto de Acapulco llegaban productos de Asia, traídos de Manila por el galeón, y la plata de minas como las de Zacatecas se enviaba a España.",
"La sociedad estaba organizada en castas, categorías basadas en el origen de las personas: españoles, indígenas, africanos y sus descendientes. Según varios historiadores, en realidad la vida de la calle era mucho más mezclada que esas categorías, y las pinturas de castas del siglo dieciocho muestran más la mirada de las élites que la vida diaria. El mestizaje fue constante.",
"En esa ciudad vivió Sor Juana Inés de la Cruz, indudablemente una de las figuras más importantes de la literatura colonial. Nació en Nepantla, cerca de la capital, y en 1669 entró en el convento de San Jerónimo. Según ella misma explicó años después, no sentía deseos de casarse y quería tener tiempo para estudiar.",
"En el convento escribió poemas, villancicos y obras de teatro. Uno de sus poemas más conocidos es Primero sueño. En 1691 escribió la Respuesta a Sor Filotea de la Cruz, una carta famosa en la que defendió el derecho de las mujeres a estudiar. Murió en 1695, cuidando a sus hermanas enfermas durante una epidemia.",
"La arquitectura barroca de la capital muestra la riqueza de esa época. En iglesias y colegios hay retablos dorados, y muchos edificios usan el tezontle, una piedra volcánica rojiza, y la cantera clara. Lamentablemente, mucho de lo que se construyó entonces ha sufrido daños con los sismos y con el hundimiento del suelo."])
vocab_update(s,"The colonial city: viceroys, castes and Sor Juana: vocabulary",[
("el virreinato","viceroyalty","noun"),("el virrey","viceroy","noun"),("el convento","convent","noun"),("la imprenta","printing press","noun"),("el retablo","altarpiece","noun"),("la casta","caste, social category by origin","noun"),("el mestizaje","cultural and ethnic blending","noun")])
grammar_update(s,"Stance Adverbs in the Colonial City",[
T("What you already know","You know *francamente*, *indudablemente*, *en realidad*, *en rigor*, *propiamente dicho* and *lamentablemente* from B2 Unit 1: these are stance adverbs. A stance adverb steps outside the action and comments on the whole sentence: how sure, how exact or how sad the writer is. In writing about the colonial past they do two jobs: they mark a correction (*en realidad*) and they say how certain you are (*indudablemente*)."),
TAB("Stance adverbs on colonial Mexico City",[
["en realidad","Actually: you correct what people assume. En realidad, la vida de la calle era más mezclada que las castas. (Actually, life in the street was more mixed than the castes.)"],
["indudablemente","Undoubtedly: you are sure. Indudablemente, Sor Juana fue una de las figuras más importantes de su época. (Undoubtedly, Sor Juana was one of the most important figures of her time.)"],
["en rigor","Strictly speaking: the exact fact. En rigor, el virreinato empezó en 1535. (Strictly speaking, the viceroyalty began in 1535.)"],
["lamentablemente","Unfortunately: your feeling about a fact. Lamentablemente, muchos documentos de la época se perdieron. (Unfortunately, many documents from that time were lost.)"],
["propiamente dicho","In the strict sense; it follows the noun. El virreinato propiamente dicho empezó en 1535. (The viceroyalty in the strict sense began in 1535.)"]]),
T("Where they go, and the commas","A stance adverb can open the sentence, sit in the middle or close it, and a comma marks each edge: *En realidad, la calle era más mezclada.* / *La calle, en realidad, era más mezclada.* Right after the verb with no commas, the same word usually describes how something was done: *Sor Juana defendió rotundamente el derecho de las mujeres a estudiar*. *Apenas* and *precisamente* take no commas, because they point at the word right after them."),
EX("In context",[
("En realidad, las castas no describían bien la vida de la calle.","Actually, the castes did not describe life in the street well."),
("Sor Juana, indudablemente, quería tener tiempo para estudiar.","Sor Juana undoubtedly wanted to have time to study."),
("En rigor, la capital del virreinato era la Ciudad de México.","Strictly speaking, the capital of the viceroyalty was Mexico City."),
("Lamentablemente, no se conservan todos los retablos de aquella época.","Unfortunately, not all the altarpieces of that time have survived."),
("Precisamente en el convento tuvo Sor Juana tiempo para estudiar.","It was precisely in the convent that Sor Juana had time to study.")]),
TIP("Try the comma test: if you can put commas round the adverb and pause, it comments on the whole sentence. Use one stance adverb per sentence; two in a row sound heavy.")])
ex_write(s,[
match(s+'.ex01',[("el virreinato","viceroyalty"),("el convento","convent"),("la imprenta","printing press"),("el retablo","altarpiece")]),
mc_read(s+'.ex02',"According to the text, what do several historians say about the castes and life in the street?",[
"Que el mestizaje hacía la vida de la calle más mezclada que las categorías oficiales.",
"Que las categorías de las castas describían bien la vida de la calle.",
"Que en la calle las personas vivían separadas según su casta."]),
fill(s+'.ex03',"____, Sor Juana fue una de las figuras más importantes de su época.","Indudablemente","Undoubtedly, Sor Juana was one of the most important figures of her time.",'stance-adverbs',hint="undoubtedly"),
mc_read(s+'.ex04',"According to the text, what did Sor Juana say about her reasons for entering the convent?",[
"Que no quería casarse y quería tener tiempo para estudiar.",
"Que su familia necesitaba dinero y por eso entró en el convento.",
"Que quería ser la profesora de los hijos del virrey de la capital."]),
build(s+'.ex05',["En","realidad,","la","vida","de","la","calle","era","más","mezclada","que","las","castas."],"Actually, life in the street was more mixed than the castes.",'stance-adverbs'),
listen(s+'.ex06',"Indudablemente, Sor Juana fue una de las grandes figuras de su época.",[
"Undoubtedly, Sor Juana was one of the great figures of her time.",
"Frankly, Sor Juana was one of the great figures of her time.",
"Fortunately, Sor Juana was one of the great figures of her time."],'stance-adverbs'),
dial(s+'.ex07',[("Guía","¿Cómo era la vida en la calle de la capital del virreinato?"),("Tú","_____"),("Guía","Es decir, la vida real no seguía las categorías oficiales.")],[
"En realidad, era más mezclada de lo que decían las castas.",
"Apenas, era más mezclada de lo que decían las castas.",
"Propiamente dicho, era más mezclada de lo que decían las castas."],'stance-adverbs'),
write(s+'.ex08',[("Say that, in fact, life in the street was more mixed than the caste categories. Start with 'En realidad'.","En realidad, la vida de la calle era más mezclada que las categorías de las castas.")],'stance-adverbs')])
# virrey must be used: put it in ex04 option 2 (done)

# ---------------- LESSON 04
s='b2-mexicocentro-04'
items=["I can correct an idea with no ... sino and no ... sino que when I talk about the murals.",
"I can choose between sino, sino que and pero.",
"I can say who paid for the murals and who the best-known painters were.",
"I can use the lesson's words for murals, scaffolds and fresco."]
lesson_update(s,"Muralism: walls that teach history","Use no ... sino and no ... sino que to correct ideas about Mexican muralism and what the murals were for.","no ... sino (recap)",items)
story_update(s,"Los muros que enseñan historia","After the Mexican Revolution the government paid artists such as Rivera, Orozco and Siqueiros to paint murals on public buildings, so that history could be seen by everyone.",[
"La fase armada de la Revolución Mexicana empezó en 1910 y terminó hacia 1920. En 1921 se creó la Secretaría de Educación Pública, y su primer titular fue José Vasconcelos. Una gran parte de la población no sabía leer, y Vasconcelos quiso llevar el arte a los edificios públicos, para que todos pudieran verlo.",
"El gobierno encargó murales a varios artistas jóvenes. Los más conocidos son Diego Rivera, José Clemente Orozco y David Alfaro Siqueiros, a quienes se conoce como los tres grandes. Dejaron los lienzos y subieron a los andamios de edificios como el Antiguo Colegio de San Ildefonso y el Palacio Nacional. Su propósito no era solo decorar, sino contar la historia de México a un pueblo que en gran parte no sabía leer.",
"En la escalinata del Palacio Nacional, Rivera pintó, a partir de 1929, una gran historia de México que va del mundo prehispánico al siglo veinte. Usó la técnica del fresco, es decir, pintura sobre una pared con la cal todavía húmeda, pero con temas mexicanos: mercados, trabajadores y pueblos indígenas.",
"Orozco miró la violencia de la Revolución con más dureza, y pintó, entre otros lugares, en el Hospicio Cabañas de Guadalajara. Siqueiros experimentó con pinturas industriales y quiso que el espectador se moviera frente a la obra. No todos vieron el pasado de la misma manera: lo que cambia de un pintor a otro es la mirada, no el muro.",
"El Estado pagó muchos de estos murales, y por eso algunos críticos han discutido hasta qué punto eran arte libre o propaganda oficial. Aun así, los murales de esos años son conocidos en todo el mundo, y muchos pueden verse hoy en edificios públicos de la capital y de otras ciudades."])
vocab_update(s,"Muralism: walls that teach history: vocabulary",[
("el muralismo","muralism, the mural movement","noun"),("el andamio","scaffold","noun"),("el lienzo","canvas","noun"),("el fresco","fresco","noun"),("la escalinata","grand staircase","noun"),("pintar","to paint","verb"),("el mural","mural","noun"),("analfabeto","illiterate","adjective"),("el mecenazgo","patronage, funding of the arts","noun")])
grammar_update(s,"No ... sino in the Story of Muralism",[
T("What you already know","You know *sino* and *sino que* from B1 Unit 40 (*No quiero té, sino café*; *No rechazaron la propuesta, sino que pidieron más detalles*), and the contrastive cleft *No fue X, sino Y lo que ...* from B2 Unit 1. *No ... sino* names the wrong idea first and then puts the right one in the spotlight. That suits the story of the murals, which is full of corrections: not decoration but teaching, not canvas but wall."),
TAB("Three ways to correct",[
["No + X, sino + Y","No pintaron en lienzos, sino en las paredes. (They did not paint on canvas but on walls.)"],
["No + verb, sino que + verb","No se quedaron en los museos, sino que pintaron en edificios públicos. (They did not stay in museums; they painted on public buildings.)"],
["No fue X, sino Y lo que ...","No fue el lienzo, sino la pared lo que eligieron. (It was not the canvas but the wall that they chose.)"]]),
T("Sino, sino que, pero or si no?","*Sino* replaces the idea you deny: it follows a negative and gives the right one. Before a conjugated verb use *sino que*. *Pero* adds a contrast without cancelling the first idea (*No es famoso, pero es bueno*). And *si no* in two words opens a condition: *Si no pintan hoy, pintarán mañana*."),
EX("In context",[
("Los murales no eran un adorno, sino una lección de historia para el pueblo.","The murals were not an ornament but a history lesson for the people."),
("No pintaron en lienzos, sino directamente en las paredes.","They did not paint on canvas but directly on walls."),
("Los muralistas no se quedaron en los museos, sino que pintaron en edificios públicos.","The muralists did not stay in museums; they painted on public buildings."),
("No era arte para coleccionistas, sino arte para la calle.","It was not art for collectors but art for the street."),
("No fue el lienzo, sino la pared lo que eligieron los muralistas.","It was not the canvas but the wall that the muralists chose.")]),
TIP("In a debate, correct the idea, not the person: *No fue una moda, sino un proyecto del gobierno* names the thing you correct and keeps the tone calm.")])
ex_write(s,[
match(s+'.ex01',[("el muralismo","muralism, the mural movement"),("el andamio","scaffold"),("el lienzo","canvas"),("el fresco","fresco")]),
mc_read(s+'.ex02',"According to the text, who paid for many of the murals?",[
"El Estado, con su mecenazgo, y no los coleccionistas privados.",
"Los coleccionistas privados, con su mecenazgo, y no el Estado.",
"La Iglesia, con su mecenazgo, y no los coleccionistas privados."]),
fill(s+'.ex03',"Los muralistas no pintaban en lienzos, ____ directamente en las paredes.","sino","The muralists did not paint on canvas but directly on walls.",'sino-vs-pero'),
mc_read(s+'.ex04',"According to the text, what was the purpose of the murals?",[
"Contar la historia de México a un pueblo que en gran parte no sabía leer.",
"Decorar las casas de las familias ricas con paisajes de Europa.",
"Vender cuadros a coleccionistas de otros países por mucho dinero."]),
build(s+'.ex05',["No","pintaron","en","lienzos,","sino","en","las","paredes","de","los","edificios","públicos."],"They did not paint on canvas but on the walls of public buildings.",'sino-vs-pero'),
listen(s+'.ex06',"Rivera no pintó en un lienzo, sino en la escalinata del Palacio Nacional.",[
"Rivera did not paint on a canvas but on the grand staircase of the National Palace.",
"Rivera painted on a canvas and also on the grand staircase of the National Palace.",
"Rivera did not paint on the grand staircase but on a canvas in the National Palace."],'sino-vs-pero'),
dial(s+'.ex07',[("Guía","¿Por qué pintaron los muralistas en edificios públicos?"),("Tú","_____"),("Guía","Entiendo: querían que todos vieran la historia.")],[
"No querían decorar, sino que querían enseñar la historia a gente analfabeta.",
"No querían decorar, sino querían enseñar la historia a gente analfabeta.",
"No querían decorar, si no que querían enseñar la historia a gente analfabeta."],'sino-vs-pero'),
write(s+'.ex08',[("Say that the murals were not for decoration but for teaching history. Use 'no ..., sino'.","Los murales no eran para decorar, sino para enseñar la historia.")],'sino-vs-pero')])
