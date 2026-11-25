import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
U='b2-brazil-rio-sao-paulo-vocab'
CH={}
# ---------------- 01
s='b2-brasilsudeste-01'
grammar(s,'grammar.b2.brasilsudeste.01.reformulation','Saying It Again, Plainly: São Paulo',
 "You know *es decir*, *o sea*, *en otras palabras* and *dicho de otro modo* from B2 Unit 29. Each one says: \"what comes next is the same idea, put another way.\" Writing about a big city needs them often, because a general line (\"the city grew rich\") is clearer once a second line makes it concrete. Here they work on São Paulo.",
 "Restating São Paulo",
 [("São Paulo creció con el café; es decir, el dinero del café pagó el ferrocarril.","*es decir* brings the exact, concrete version"),
  ("Llegaron inmigrantes de Italia y Japón; o sea, la ciudad se llenó de gente de muchos países.","*o sea* is the most spoken one"),
  ("La Avenida Paulista era una calle de mansiones; en otras palabras, allí vivían las familias del café.","*en otras palabras* suits a longer, more careful sentence"),
  ("Los obreros dejaron de trabajar; dicho de otro modo, hicieron huelga.","*dicho de otro modo* gives the idea a new label")],
 "In context",
 [("El museo no tiene columnas en el centro; es decir, la plaza de abajo queda libre.","The museum has no columns in the middle; that is, the square below stays free."),
  ("Los barrios del ABC tienen muchas fábricas; o sea, allí trabajan muchos obreros.","The ABC districts have many factories; I mean, many workers work there."),
  ("São Paulo recibió inmigrantes de muchos países; en otras palabras, es una ciudad de origen mixto.","São Paulo received immigrants from many countries; in other words, it is a city of mixed origins.")],
 "The new wording comes after the marker, and a comma or semicolon comes before it. Do not use these markers to add a new fact: for that you know *además* from A2 Unit 28. If the second part is the opposite of the first, you need a contrast connector such as *sin embargo*, not a restatement.")
x=Ex(s)
x.mc("Which sentence says the same thing again in other words?",
 "La ciudad creció gracias al café; es decir, el dinero del café pagó su crecimiento.",
 ["La ciudad creció gracias al café; sin embargo, el dinero del café pagó su crecimiento.","La ciudad creció gracias al café; además, el dinero del café pagó su crecimiento."],1,'reformulation-markers',
 ds={"La ciudad creció gracias al café; sin embargo, el dinero del café pagó su crecimiento.":'contrast-concession-connectors',"La ciudad creció gracias al café; además, el dinero del café pagó su crecimiento.":'ordering-markers'})
x.fb("Muchos inmigrantes trabajaban en las fábricas; en otras ____, la industria necesitaba obreros.","palabras","Many immigrants worked in the factories; in other words, industry needed workers.",'reformulation-markers')
x.mt([("el ferrocarril","railway"),("el inmigrante","immigrant"),("la huelga","strike"),("el obrero","factory worker")],U)
x.sb("Los obreros dejaron de trabajar; es decir, hicieron huelga.","The workers stopped working; that is, they went on strike.",'reformulation-markers')
x.fb("Los obreros pararon las fábricas con una ____.","huelga","The workers stopped the factories with a strike.",U,cat='vocabulary')
x.read("According to the text, who did the ship Kasato Maru bring to Santos in 1908?",
 "Los primeros inmigrantes de Japón.",["Los primeros inmigrantes de Italia.","Los primeros obreros del Gran ABC."],0)
ids=x.write()
vocab(s,"São Paulo: coffee, immigrants and industry",[("ferrocarril","railway","noun"),("inmigrante","immigrant","noun"),("huelga","strike","noun"),("obrero","factory worker","noun")])
lesson(s,"São Paulo: from coffee town to giant city","I can restate an idea about São Paulo with *es decir*, *o sea* or *en otras palabras*.","restating an idea with es decir, o sea, en otras palabras and dicho de otro modo",ids)
n=story(s,"La ciudad que creció con el café","São Paulo grew from a Jesuit school of 1554 into a huge city through coffee, immigration from Italy and Japan, and industry.",
["La ciudad de São Paulo nació en 1554, cuando los jesuitas Manuel da Nóbrega y José de Anchieta fundaron un colegio en una meseta, a unos setecientos metros sobre el nivel del mar. Durante siglos fue una villa pequeña. En el siglo XIX el café cambió su historia: las plantaciones del interior del estado crecieron mucho y el café viajaba en ferrocarril hasta el puerto de Santos. Es decir, la ciudad se hizo rica con el café y con las vías del tren.",
 "En 1888 se abolió la esclavitud, y las haciendas y las primeras fábricas necesitaban trabajadores. Llegaron muchos inmigrantes italianos, que se instalaron en barrios como Brás, Mooca y Bixiga. En 1908 el barco Kasato Maru llevó a Santos a los primeros inmigrantes japoneses. Según las estimaciones habituales, hoy São Paulo tiene la mayor comunidad de origen japonés fuera de Japón, y su centro es el barrio de Liberdade. En otras palabras, la ciudad se formó con gente de muchos países.",
 "La Avenida Paulista se abrió en 1891 y fue primero una calle de mansiones de familias del café. Hoy hay en ella bancos, oficinas y rascacielos. Allí está también el MASP, el museo que proyectó la arquitecta ítalo-brasileña Lina Bo Bardi; el edificio se inauguró en 1968 y deja libre una gran plaza debajo del museo.",
 "Al sur de la ciudad está el Gran ABC, una zona industrial con fábricas de automóviles: Santo André, São Bernardo do Campo y São Caetano do Sul. A fines de los años setenta, durante la dictadura militar, los obreros metalúrgicos de la zona hicieron grandes huelgas. Uno de sus dirigentes sindicales era Luiz Inácio Lula da Silva, nacido en Pernambuco, en el nordeste. Lula asumió la presidencia de Brasil en 2003. Dicho de otro modo, un obrero de las fábricas del ABC llegó después a presidente."],
[("When did the Kasato Maru bring the first Japanese immigrants to Santos?",["En 1908.","En 1888.","En 1968."],0,"The second paragraph gives the year."),
 ("What was the Avenida Paulista at first?",["Una calle de mansiones de familias del café.","Una zona de fábricas de automóviles.","Un barrio de inmigrantes japoneses."],0,"The third paragraph says so."),
 ("Where were the strikes of the late 1970s?",["En el Gran ABC, al sur de la ciudad.","En el puerto de Santos.","En la Avenida Paulista."],0,"The fourth paragraph places them in the ABC area.")])
print(s,n)
CH[s]=chal("Why São Paulo Grew","You are Carlos. You and Meg are watching a documentary about São Paulo, and she asks how the city got rich in the 19th century.","Tell Meg how São Paulo became rich, then say the same thing more plainly.",["Say that the city grew thanks to coffee","Restate it: coffee money paid for the railway"],"São Paulo creció gracias al café; es decir, el dinero del café pagó el ferrocarril.","São Paulo grew thanks to coffee; that is, the coffee money paid for the railway.","I can restate an idea about São Paulo with *es decir*, *o sea* or *en otras palabras*.")

# ---------------- 02
s='b2-brasilsudeste-02'
grammar(s,'grammar.b2.brasilsudeste.02.relatives','Rio de Janeiro: Who, Which, Where, Whose',
 "You know *que*, *quien*, *donde* and *cuyo* from B1 Unit 5: *que* for people and things, *quien* after a preposition, *donde* for places and *cuyo* for \"whose\". They let one sentence describe a place in detail, which is what a description of Rio needs: hills, bay, districts. Here they work on Rio de Janeiro.",
 "Four relatives at work",
 [("Los morros que rodean la bahía forman un anfiteatro natural.","*que* for things: the hills that surround the bay"),
  ("Los navegantes que llegaron en 1502 creyeron que la bahía era un río.","*que* for people: the sailors who arrived"),
  ("El Corcovado, donde está el Cristo Redentor, mira sobre la ciudad.","*donde* for a place: where the statue stands"),
  ("La bahía de Guanabara, cuyas aguas bañan muchas playas, tiene varias islas.","*cuyas* agrees with *aguas*, the thing owned: whose waters")],
 "In context",
 [("La ciudad donde se instaló la corte portuguesa en 1808 era Río de Janeiro.","The city where the Portuguese court settled in 1808 was Rio de Janeiro."),
  ("El Pan de Azúcar, que se ve desde muchas playas, es uno de sus símbolos.","Sugarloaf Mountain, which can be seen from many beaches, is one of its symbols."),
  ("Hay barrios cuyos vecinos viven en las laderas de los morros.","There are districts whose residents live on the hillsides.")],
 "Without commas, the relative clause says which one you mean (*los morros que rodean la bahía*: only those hills). Between commas, it adds extra information about something already clear (*El Corcovado, donde está el Cristo Redentor, ...*). *Cuyo* agrees with the thing owned, never with the owner, and no article comes after it.")
x=Ex(s)
x.fb("La bahía de Guanabara, ____ aguas bañan muchas playas, tiene varias islas.","cuyas","Guanabara Bay, whose waters wash many beaches, has several islands.",'relativo-posesivo-cuyo')
x.mc("Which sentence says \"The sailors who arrived in 1502 thought the bay was a river\"?",
 "Los navegantes que llegaron en 1502 creyeron que la bahía era un río.",
 ["Los navegantes donde llegaron en 1502 creyeron que la bahía era un río.","Los navegantes cuyos llegaron en 1502 creyeron que la bahía era un río."],2,'relative-clauses',
 ds={"Los navegantes cuyos llegaron en 1502 creyeron que la bahía era un río.":'relativo-posesivo-cuyo'})
x.mt([("el morro","hill (in Rio)"),("la bahía","bay"),("la favela","favela, informal hillside district"),("la ladera","hillside")],U)
x.fb("El Corcovado es la montaña ____ está el Cristo Redentor.","donde","The Corcovado is the mountain where the statue of Christ the Redeemer stands.",'relative-clauses')
x.sb("La ciudad donde se instaló la corte en 1808 era Río.","The city where the court settled in 1808 was Rio.",'relative-clauses')
x.read("According to the text, what happened in Rio in 1808?",
 "La familia real portuguesa se instaló allí.",["Se inauguró el Sambódromo.","Se declaró la independencia de Brasil."],1)
ids=x.write()
vocab(s,"Rio de Janeiro: hills, bay and favelas",[("morro","hill (in Rio)","noun"),("bahía","bay","noun"),("favela","favela, informal hillside district","noun"),("ladera","hillside","noun"),("corte","royal court","noun")])
lesson(s,"Rio de Janeiro: a city between hills and sea","I can describe places in Rio with relative clauses such as *que*, *donde* and *cuyo*.","recap: relative clauses with que, quien, donde and cuyo",ids)
n=story(s,"La ciudad entre los morros y el mar","Rio de Janeiro grew between granite hills and the sea; it was a royal capital from 1808, the capital of Brazil until 1960, and it has favelas, famous beaches and the carnival parades.",
["Río de Janeiro está entre el mar y unas montañas de granito. Los navegantes portugueses que llegaron en enero de 1502 creyeron que la bahía de Guanabara era la desembocadura de un río, y por eso la llamaron río de enero. La ciudad, que se fundó en 1565, creció entre morros, lagunas y playas, sin un plano regular. En 2012 la Unesco declaró Patrimonio Mundial el paisaje carioca entre la montaña y el mar, con el Pan de Azúcar, el Corcovado y el bosque de Tijuca.",
 "En 1808 la familia real portuguesa, que huía de la invasión napoleónica de Portugal, se instaló en Río. La ciudad fue desde entonces la sede de la corte, y después de la independencia de 1822 siguió siendo la capital de Brasil hasta 1960, año en que se inauguró Brasília. En lo alto del Corcovado, donde hay una vista de toda la bahía, se inauguró en 1931 la estatua del Cristo Redentor.",
 "Las favelas son barrios que crecieron sin planificación en las laderas de los morros. Según la historia más conocida, la primera nació a fines del siglo XIX, cuando soldados que volvían de la guerra de Canudos se instalaron en el Morro da Providência para esperar una vivienda que el Estado les había prometido. Hoy muchas favelas tienen escuelas de samba, asociaciones de vecinos y comercios, pero también problemas de violencia y de falta de servicios públicos.",
 "En las playas de Copacabana e Ipanema, que están entre las más famosas del mundo, la vida social se hace al aire libre: se juega al fútbol y al vóley, se toma agua de coco y se escucha música. Cada año, antes de la Cuaresma, las escuelas de samba desfilan en el Sambódromo, que se inauguró en 1984 en la calle Marquês de Sapucaí."],
[("When did Portuguese sailors arrive at Guanabara Bay?",["En enero de 1502.","En 1565.","En 1808."],0,"The first paragraph gives the date."),
 ("Until when was Rio the capital of Brazil?",["Hasta 1960.","Hasta 1822.","Hasta 1931."],0,"The second paragraph says the capital moved with the inauguration of Brasília in 1960."),
 ("According to the best-known story, who settled on the Morro da Providência?",["Soldados que volvían de la guerra de Canudos.","Navegantes portugueses del año 1502.","Músicos de las primeras escuelas de samba."],0,"The third paragraph tells it.")])
print(s,n)
CH[s]=chal("Hills and Bay","You are Meg. You and Carlos are planning a trip and reading about Rio de Janeiro, and he asks what you learned about the royal court.","Tell Carlos which city the Portuguese royal family settled in during 1808.",["Say that it was a city, using a relative clause","Give the year the family arrived"],"La ciudad donde se instaló la familia real portuguesa en 1808 era Río de Janeiro.","The city where the Portuguese royal family settled in 1808 was Rio de Janeiro.","I can describe places in Rio with relative clauses such as *que*, *donde* and *cuyo*.")

# ---------------- 03
s='b2-brasilsudeste-03'
grammar(s,'grammar.b2.brasilsudeste.03.se','The 1922 Modern Art Week: Which Se?',
 "You know the different jobs of *se* from B2 Unit 19: reflexive, reciprocal, passive, impersonal and accidental. A text about an art movement uses several of them in a few lines, so it is a good place to ask \"who does what to whom?\" Here they work on the Modern Art Week of 1922.",
 "Five kinds of se, in São Paulo, 1922",
 [("Reflexive: someone does it to themselves","Los jóvenes artistas se presentaron ante el público. (presented themselves)"),
  ("Reciprocal: two or more do it to each other","Los modernistas se conocían y se escribían cartas. (wrote to each other)"),
  ("Passive: a thing, no doer named","En 1922 se celebró la Semana de Arte Moderna. (was held)"),
  ("Impersonal: nobody in particular","Se dice que el público abucheó a los artistas. (it is said)"),
  ("Accidental: se + me, te, le, nos","Se me perdió el programa de la exposición. (I lost the programme)")],
 "Same word, different jobs",
 [("Se leyeron poemas y se presentaron cuadros durante tres noches.","Poems were read and paintings were shown over three nights."),
  ("Oswald y Tarsila se admiraban mucho.","Oswald and Tarsila admired each other a lot."),
  ("Se nos olvidó el catálogo en casa.","We forgot the catalogue at home.")],
 "Ask what the noun does. If *se* + a plural thing agrees with the verb (*se leyeron poemas*), it is passive. If nobody is named and there is no noun (*se dice que*), it is impersonal. If *me, te, le, nos* follows *se* and the verb agrees with the thing (*se me perdió el programa*), it is accidental.")
x=Ex(s)
x.mc("In which sentence does *se* mean \"each other\"?",
 "Los modernistas se escribían cartas.",
 ["Los modernistas se presentaron ante el público.","En 1922 se celebró una gran exposición."],0,'desambiguacion-valores-se',
 ds={"En 1922 se celebró una gran exposición.":'se-pasivo-vs-impersonal'})
x.fb("En 1922 ____ celebró la Semana de Arte Moderna en São Paulo.","se","The Modern Art Week was held in São Paulo in 1922.",'se-pasivo-vs-impersonal')
x.mt([("la vanguardia","avant-garde"),("el manifiesto","manifesto"),("el abucheo","booing"),("la exposición","exhibition")],U)
x.mc("Which sentence says \"I lost the exhibition programme\"?",
 "Se me perdió el programa de la exposición.",
 ["Me perdí el programa de la exposición.","Se perdió el programa de la exposición."],2,'desambiguacion-valores-se',
 ds={"Se perdió el programa de la exposición.":'pasiva-refleja'})
x.sb("Se dice que el público abucheó a los artistas.","It is said that the public booed the artists.",'desambiguacion-valores-se')
x.read("According to the text, what did Oswald de Andrade publish in 1928?",
 "El Manifiesto Antropófago.",["La novela Macunaíma.","El cuadro Abaporu."],0)
ids=x.write()
vocab(s,"Modernism: the Week of 1922 and the cannibal manifesto",[("vanguardia","avant-garde","noun"),("manifiesto","manifesto","noun"),("abucheo","booing","noun"),("exposición","exhibition","noun")])
lesson(s,"The 1922 Modern Art Week: São Paulo breaks with the academies","I can tell the different jobs of *se* in a text about the Modern Art Week of 1922.","recap: the five jobs of se (reflexive, reciprocal, passive, impersonal, accidental)",ids)
n=story(s,"La Semana de Arte Moderna de 1922","The Modern Art Week of 1922 in São Paulo started Brazilian modernism; in 1928 Oswald de Andrade's cannibal manifesto and Mário de Andrade's Macunaíma followed.",
["En febrero de 1922, cuando Brasil celebraba cien años de independencia, se celebró en el Teatro Municipal de São Paulo la Semana de Arte Moderna. Durante tres noches se leyeron poemas, se dieron conferencias, se tocó música y se mostraron cuadros y esculturas. Participaron escritores y artistas jóvenes, como Mário de Andrade, Anita Malfatti, Di Cavalcanti y el compositor Heitor Villa-Lobos.",
 "Según los relatos de la época, una parte del público reaccionó con burlas y abucheos. En las academias se seguían todavía los modelos europeos, y los modernistas querían otra cosa: un arte que se acercara al lenguaje de la calle, a los temas del país y a la música popular. Algunos historiadores recuerdan que Anita Malfatti ya había expuesto obras modernas en São Paulo en 1917.",
 "En 1928 Oswald de Andrade publicó el Manifiesto Antropófago. Su idea es una metáfora: el artista brasileño no debe copiar la cultura extranjera ni rechazarla, sino devorarla y convertirla en algo propio. Según la historia habitual, el manifiesto se inspiró en el cuadro Abaporu, que Tarsila do Amaral pintó ese año como regalo para su marido, Oswald. El título viene de palabras de la lengua tupí que significan el hombre que come gente.",
 "Ese mismo año Mário de Andrade publicó la novela Macunaíma, cuyo protagonista cambia de aspecto y de lugar a lo largo del libro. Hoy la Semana de 1922 se considera el comienzo del modernismo brasileño. Más tarde el espíritu moderno llegó también a la arquitectura, con Oscar Niemeyer, nacido en Río de Janeiro en 1907, que proyectó edificios de Brasília."],
[("Where was the Modern Art Week held?",["En el Teatro Municipal de São Paulo.","En el Museo de Arte de São Paulo.","En una escuela de samba de Río."],0,"The first paragraph names the theatre."),
 ("What does the Manifiesto Antropófago propose?",["Que el artista brasileño devore la cultura extranjera y la convierta en algo propio.","Que el artista brasileño copie los modelos europeos.","Que el artista brasileño rechace toda influencia extranjera."],0,"The third paragraph explains the metaphor."),
 ("Which book did Mário de Andrade publish in 1928?",["Macunaíma.","Abaporu.","Chega de Saudade."],0,"The fourth paragraph says so.")])
print(s,n)
CH[s]=chal("The Week of 1922","You are Carlos. You and Meg are preparing a short talk on Brazilian modernism, and she asks when the Modern Art Week took place.","Tell Meg when and where the Modern Art Week was held, using a passive with *se*.",["Say that it was held in São Paulo","Give the year"],"La Semana de Arte Moderna se celebró en São Paulo en 1922.","The Modern Art Week was held in São Paulo in 1922.","I can tell the different jobs of *se* in a text about the Modern Art Week of 1922.")

# ---------------- 04
s='b2-brasilsudeste-04'
grammar(s,'grammar.b2.brasilsudeste.04.stance','Samba and Bossa Nova: Adverbs that Show Your View',
 "You know *lamentablemente*, *en realidad*, *en rigor*, *precisamente*, *apenas* and other adverbs from B2 Unit 1. They show how you stand towards a fact, or point at the exact word. Writing about music uses them to correct a common idea (*en realidad*) or to pin down a detail (*precisamente*). Here they work on samba and bossa nova.",
 "Stance and focus adverbs in Brazilian music",
 [("En realidad, la bossa nova no nació en una favela, sino en apartamentos de Copacabana e Ipanema.","*en realidad* corrects what people may assume"),
  ("Precisamente en los morros nacieron muchas escuelas de samba.","*precisamente* points at the place: exactly there"),
  ("Lamentablemente, la dictadura obligó a algunos músicos a salir del país.","*lamentablemente* shows regret about a fact"),
  ("El disco, en rigor, salió en 1959, aunque la canción se grabó en 1958.","*en rigor* gives the exact, technical truth")],
 "In context",
 [("En realidad, la bossa nova toma ideas de la samba.","In fact, bossa nova takes ideas from samba."),
  ("Gilberto cantaba casi susurrando; apenas levantaba la voz.","Gilberto sang almost whispering; he hardly raised his voice."),
  ("Fue precisamente en 1964 cuando los militares tomaron el poder.","It was exactly in 1964 that the military took power.")],
 "Use the comma test from B2 Unit 1: if you can put commas round the adverb, it comments on the whole sentence (*En realidad, ...*). *Precisamente* and *apenas* sit right before the word they point at, with no commas. Use only one stance adverb per sentence.")
x=Ex(s)
x.mc("Which sentence corrects the idea that bossa nova began in the favelas?",
 "En realidad, la bossa nova nació en apartamentos de la zona sur de Río.",
 ["Lamentablemente, la bossa nova nació en apartamentos de la zona sur de Río.","Precisamente, la bossa nova nació en apartamentos de la zona sur de Río."],0,'stance-adverbs')
x.fb("Muchas escuelas de samba nacieron ____ en los morros de Río.","precisamente","Many samba schools were born precisely in the hills of Rio.",'stance-adverbs')
x.mt([("la síncopa","syncopation"),("la guitarra","guitar"),("el disco","record, album"),("el conjunto","group, band")],U)
x.fb("João Gilberto cantaba en voz baja; ____, casi susurraba.","en realidad","João Gilberto sang softly; in fact, he almost whispered.",'stance-adverbs',hint="Two words: it adds a correction.")
x.sb("Fue precisamente en 1964 cuando los militares tomaron el poder.","It was precisely in 1964 that the military took power.",'stance-adverbs')
x.read("According to the text, what did Caetano Veloso and Gilberto Gil do in 1969?",
 "Se fueron a Londres.",["Tocaron en el Carnegie Hall.","Fundaron la escuela de samba de Mangueira."],1)
ids=x.write()
vocab(s,"Samba, bossa nova and Tropicália",[("síncopa","syncopation","noun"),("guitarra","guitar","noun"),("disco","record, album","noun"),("conjunto","group, band","noun"),("susurrar","to whisper","verb")])
lesson(s,"Samba, bossa nova and Tropicália: Brazilian music from Rio","I can add my view of a fact about Brazilian music with adverbs such as *en realidad* and *precisamente*.","recap: stance and focus adverbs (en realidad, precisamente, en rigor, lamentablemente)",ids)
n=story(s,"De la samba a la bossa nova","From samba in the Rio hills to the bossa nova of the 1950s and 60s and the Tropicália of the late 1960s.",
["La samba nació en Río de Janeiro a comienzos del siglo XX, entre la población afrobrasileña de la ciudad. En 1928 Cartola y otros músicos fundaron la escuela de samba de Mangueira, en un morro. Precisamente en los morros y en los barrios populares nacieron muchas de las escuelas que hoy desfilan en el carnaval.",
 "A fines de los años cincuenta, un grupo de jóvenes músicos creó en Río la bossa nova, que significa algo como nueva onda. En realidad, no nació en una favela, sino en los apartamentos de la zona sur, en barrios como Copacabana e Ipanema. En 1958 João Gilberto, nacido en Bahía, grabó Chega de Saudade, una canción de Tom Jobim y del poeta y diplomático Vinicius de Moraes; el disco con ese nombre salió en 1959. Gilberto cantaba en voz baja y tocaba la guitarra con un ritmo nuevo, que tomaba algo de la samba.",
 "En noviembre de 1962 hubo en el Carnegie Hall de Nueva York un concierto de bossa nova con músicos brasileños y estadounidenses, entre ellos el saxofonista Stan Getz. Después, canciones como Garota de Ipanema, de Jobim y Vinicius, se hicieron famosas en muchos países.",
 "En 1964 los militares tomaron el poder en Brasil, y la dictadura duró hasta 1985. A fines de los años sesenta, Caetano Veloso, Gilberto Gil y otros músicos lanzaron el Tropicalismo, que mezclaba la música popular brasileña con la guitarra eléctrica y el rock. Después de pasar un tiempo detenidos, Veloso y Gil se fueron a Londres en 1969."],
[("Who founded the Mangueira samba school in 1928?",["Cartola y otros músicos.","João Gilberto y Tom Jobim.","Caetano Veloso y Gilberto Gil."],0,"The first paragraph says so."),
 ("According to the text, where did bossa nova begin?",["En apartamentos de la zona sur de Río.","En una favela de la zona norte.","En un teatro de São Paulo."],0,"The second paragraph says it was not in a favela."),
 ("What happened in Brazil in 1964?",["Los militares tomaron el poder.","Se grabó Chega de Saudade.","Hubo un concierto en el Carnegie Hall."],0,"The fourth paragraph says so.")])
print(s,n)
CH[s]=chal("Bossa Nova Facts","You are Meg. You and Carlos are listening to bossa nova and he thinks it came from the favelas.","Correct Carlos: bossa nova began in apartments in the south of Rio.",["Correct what he assumes, with a stance adverb","Say where it began"],"En realidad, la bossa nova nació en apartamentos de la zona sur de Río.","In fact, bossa nova began in apartments in the south of Rio.","I can add my view of a fact about Brazilian music with adverbs such as *en realidad* and *precisamente*.")

# ---------------- 05
s='b2-brasilsudeste-05'
grammar(s,'grammar.b2.brasilsudeste.05.cuanto','Spanish and Portuguese: The More..., the More...',
 "You know *cuanto más ..., más ...* and *a medida que* from B1 Unit 2: two changes that go together, one growing as the other grows. Learning a neighbour language is a good case: the more you read, the better you understand. Here they work on Spanish and Portuguese.",
 "Two changes together",
 [("Cuanto más lees en portugués, más palabras entiendes.","*cuanto más ..., más ...*: the more ..., the more ..."),
  ("Cuanto más practicas, mejor entiendes.","*mejor* is used instead of *más bueno*"),
  ("Cuanto menos conoces la lengua, más cuidado necesitas.","*cuanto menos ..., más ...*: the less ..., the more ..."),
  ("A medida que aprendes portugués, ves más diferencias.","*a medida que*: as, while a change goes on")],
 "In context",
 [("Cuanto más viajas por la frontera, más mezclas oyes.","The more you travel along the border, the more mixing you hear."),
  ("A medida que leemos, entendemos mejor los falsos amigos.","As we read, we understand false friends better."),
  ("Cuanto más hablas, menos errores haces.","The more you speak, the fewer mistakes you make.")],
 "*Cuanto* does not change when a verb follows it. Use *mejor* or *peor* (not *más bueno*, *más malo*) in the second part. Both parts use the same tense: *cuanto más leo, más entiendo*.")
x=Ex(s)
x.mc("Which sentence says \"The more you read in Portuguese, the more words you understand\"?",
 "Cuanto más lees en portugués, más palabras entiendes.",
 ["Cuanto más lees en portugués, menos palabras entiendes.","Cuanto menos lees en portugués, más palabras entiendes."],2,'cuanto-mas-tanto-mas')
x.fb("A ____ que aprendes portugués, ves más diferencias con el español.","medida","As you learn Portuguese, you see more differences from Spanish.",'cuanto-mas-tanto-mas')
x.mt([("el falso amigo","false friend"),("la frontera","border"),("el idioma","language"),("el vocabulario","vocabulary")],U)
x.fb("Cuanto ____ practicas, mejor entiendes el portugués.","más","The more you practise, the better you understand Portuguese.",'cuanto-mas-tanto-mas')
x.sb("Cuanto más hablas, menos errores haces.","The more you speak, the fewer mistakes you make.",'cuanto-mas-tanto-mas')
x.read("According to the text, what does *esquisito* mean in Portuguese?",
 "Extraño.",["Delicioso.","Caro."],0)
ids=x.write()
vocab(s,"Spanish and Portuguese: neighbours and false friends",[("falso amigo","false friend","noun"),("frontera","border","noun"),("idioma","language","noun"),("vocabulario","vocabulary","noun"),("extraño","strange","adjective")])
lesson(s,"Spanish and Portuguese: neighbour languages and false friends","I can link two changes about learning Portuguese with *cuanto más ..., más ...* and *a medida que*.","recap: cuanto más ..., más ... and a medida que",ids)
n=story(s,"El español y el portugués, lenguas vecinas","Spanish and Portuguese are close but have false friends; they mix on the borders and are the working languages of Mercosur.",
["Brasil limita con casi todos los países de Sudamérica: con todos, menos con Chile y Ecuador. En esas fronteras se hablan español y portugués, y muchas personas pasan de un idioma al otro. Los dos idiomas vienen del latín y se parecen mucho. Según una estimación lingüística, comparten cerca del 89 % del vocabulario. Por eso un hispanohablante entiende bastante portugués escrito, y un brasileño entiende bastante español. Cuanto más se lee en el otro idioma, más fácil resulta.",
 "Pero hay falsos amigos: palabras casi iguales con otro significado. En portugués, esquisito significa extraño, no delicioso. La palabra apelido es el apodo, no el apellido. Embaraçada significa avergonzada, y escritório es una oficina. En todos estos casos conviene mirar el contexto y no fiarse solo del parecido.",
 "En las zonas de frontera, como la de Uruguay y Brasil, nació el portuñol, una mezcla informal de los dos idiomas. En las ciudades gemelas de Rivera y Santana do Livramento, la frontera es una calle y una plaza, y la gente cambia de idioma con facilidad. Los lingüistas lo consideran un fenómeno de contacto entre lenguas, no un error.",
 "En 1991 Argentina, Brasil, Paraguay y Uruguay firmaron el Tratado de Asunción, que creó el Mercosur. Según el tratado, el español y el portugués son los idiomas de trabajo del bloque. A medida que crece el comercio entre los países vecinos, crece también el interés por aprender el idioma del otro."],
[("Which two countries of South America does Brazil not share a border with?",["Chile y Ecuador.","Uruguay y Paraguay.","Argentina y Bolivia."],0,"The first paragraph says it borders all but Chile and Ecuador."),
 ("What does *apelido* mean in Portuguese, according to the text?",["El apodo.","El apellido.","La oficina."],0,"The second paragraph explains it."),
 ("What did the Treaty of Asunción create in 1991?",["El Mercosur.","El portuñol.","Una escuela de idiomas."],0,"The fourth paragraph says so.")])
print(s,n)
CH[s]=chal("Learning Portuguese","You are Meg. You are telling Carlos how learning Portuguese is going after reading about the neighbour languages.","Tell Carlos that the more you read in Portuguese, the more you understand.",["Use a *cuanto más* structure","Say that you understand more"],"Cuanto más leo en portugués, más entiendo.","The more I read in Portuguese, the more I understand.","I can link two changes about learning Portuguese with *cuanto más ..., más ...* and *a medida que*.")

# ---------------- consolidation
s='b2-brasilsudeste-consolidation'
x=Ex(s)
x.mc("Which sentence restates the first idea in other words?",
 "El café pagó el ferrocarril; es decir, el dinero del café hizo posible el tren.",
 ["El café pagó el ferrocarril; sin embargo, el dinero del café hizo posible el tren.","El café pagó el ferrocarril; además, el dinero del café hizo posible el tren."],1,'reformulation-markers',
 ds={"El café pagó el ferrocarril; sin embargo, el dinero del café hizo posible el tren.":'contrast-concession-connectors',"El café pagó el ferrocarril; además, el dinero del café hizo posible el tren.":'ordering-markers'})
x.fb("La ciudad ____ se instaló la corte portuguesa en 1808 era Río de Janeiro.","donde","The city where the Portuguese court settled in 1808 was Rio de Janeiro.",'relative-clauses')
x.mc("Which sentence says \"The Modern Art Week was held in 1922\"?",
 "En 1922 se celebró la Semana de Arte Moderna.",
 ["En 1922 se celebraron la Semana de Arte Moderna.","En 1922 celebró la Semana de Arte Moderna."],0,'desambiguacion-valores-se',
 ds={"En 1922 se celebraron la Semana de Arte Moderna.":'se-pasivo-vs-impersonal'})
x.fb("La bossa nova no nació en una favela; en ____, nació en apartamentos de la zona sur.","realidad","Bossa nova was not born in a favela; in fact, it was born in apartments in the south zone.",'stance-adverbs')
x.mc("Which sentence says \"The less you read, the less you understand\"?",
 "Cuanto menos lees, menos entiendes.",
 ["Cuanto más lees, menos entiendes.","Cuanto menos lees, más entiendes."],2,'cuanto-mas-tanto-mas')
x.mt([("el obrero","factory worker"),("la bahía","bay"),("la vanguardia","avant-garde"),("el falso amigo","false friend")],U)
x.fb("Los obreros pararon las fábricas; o ____, hicieron huelga.","sea","The workers stopped the factories; I mean, they went on strike.",'reformulation-markers')
x.read("According to the texts, in which year did Brasília become the capital of Brazil instead of Rio de Janeiro?",
 "En 1960.",["En 1808.","En 1922."],0)
ids=x.write()
consolidation(s,"Review: São Paulo, Rio and Brazilian culture","Review São Paulo, Rio de Janeiro, the Modern Art Week, Brazilian music and the neighbour languages, with the grammar you used to talk about them.","review: reformulation markers, relative clauses, se, stance adverbs, cuanto más ..., más ...",
 ["I can review what I learned about São Paulo, Rio and Brazilian culture.","I can restate an idea, add a relative clause and tell the jobs of *se*.","I can use stance adverbs and *cuanto más ..., más ...* about Brazil."],
 ["I can restate an idea about Brazil with *es decir*, *o sea* or *en otras palabras*.","I can describe places in Rio with relative clauses such as *que*, *donde* and *cuyo*.","I can tell the different jobs of *se* in a text about the Modern Art Week of 1922.","I can add my view of a fact about Brazilian music with adverbs such as *en realidad* and *precisamente*.","I can link two changes about learning Portuguese with *cuanto más ..., más ...* and *a medida que*."],ids)
CH[s]=chal("Brazil in Review","You are Carlos. You and Meg are preparing a short talk about Brazil's southeast, and she asks you to explain what the coffee railway meant for São Paulo.","Tell Meg that coffee made São Paulo rich, then say it again in other words.",["Say that coffee made the city rich","Restate it in other words"],"El café hizo rica a São Paulo; en otras palabras, la ciudad creció gracias al café.","Coffee made São Paulo rich; in other words, the city grew thanks to coffee.","I can restate an idea about Brazil with *es decir*, *o sea* or *en otras palabras*.")
challenges(ROOT+'/challenges-brazil-rio-sao-paulo.json',CH)
