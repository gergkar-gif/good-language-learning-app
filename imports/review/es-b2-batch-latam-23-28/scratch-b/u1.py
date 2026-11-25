import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-argentina-politics-vocab'
def S(n): return f'b2-argentinasociedad-{n}'
def I(n,k): return f'{S(n)}.ex{k:02d}'

# ---------- 01
n='01'
story(S(n),'El peronismo: apoyos y críticas','Peronism began on 17 October 1945 and gave workers new rights and Evita a central role; critics said it limited the press, it was banned after 1955, and it still divides opinion today.',[
"El 17 de octubre de 1945 miles de obreros marcharon hacia la Plaza de Mayo, en Buenos Aires, para pedir la libertad del coronel Juan Domingo Perón, que había sido detenido unos días antes. Perón ganó las elecciones de febrero de 1946 y gobernó hasta 1955.",
"En esos años el Estado compró los ferrocarriles y la red de teléfonos, y se ampliaron derechos laborales como el aguinaldo y las vacaciones pagadas. Muchos trabajadores sintieron que por primera vez el Estado los tenía en cuenta. Sin embargo, los críticos de Perón decían que su gobierno limitaba la libertad de prensa y controlaba a la oposición. En 1951 el diario opositor *La Prensa* fue expropiado.".replace('*',''),
"Eva Duarte de Perón, conocida como Evita, tuvo un papel central. Su fundación ayudó a familias pobres con hospitales, escuelas y viviendas. En 1947 se aprobó la ley del voto femenino, que Evita apoyó, y las mujeres votaron por primera vez en elecciones nacionales en 1951. Evita murió en 1952, a los treinta y tres años.",
"En junio de 1955 aviones de la Armada bombardearon la Plaza de Mayo, y en septiembre un golpe militar derrocó a Perón, que se fue al exilio. Durante casi veinte años el peronismo estuvo prohibido. No obstante, siguió vivo entre los obreros y en los sindicatos. Perón volvió al país en 1973, ganó otra vez las elecciones y murió en julio de 1974.",
"Hoy el peronismo sigue dividiendo opiniones. Para sus partidarios representa la justicia social; para sus críticos, un estilo de gobierno demasiado personalista. En las elecciones de 2023 el candidato peronista perdió frente a Javier Milei, presidente desde diciembre de 2023, cuyo partido ganó las elecciones legislativas de octubre de 2025.",
],[
("What did the workers ask for on 17 October 1945?",["La libertad del coronel Perón.","El voto de las mujeres.","La compra de los ferrocarriles."],"The first paragraph says they marched to ask for Perón's freedom."),
("What did Perón's critics say about his government, according to the text?",["Que limitaba la libertad de prensa.","Que no aprobó ninguna ley laboral.","Que cerró todos los hospitales."],"The second paragraph gives the critics' view."),
("What happened to Peronism after 1955?",["Estuvo prohibido durante casi veinte años.","Gobernó sin cambios hasta 1973.","Desapareció de los sindicatos."],"The fourth paragraph says it was banned but survived among workers."),
])
grammar(S(n),'grammar.b2.argentinasociedad.01.sin-embargo-no-obstante','Two Views of Peronism: Sin Embargo and No Obstante',
"You know *sin embargo* from A2 Unit 28 and *no obstante* (a little more formal) from B1 Unit 1. Both open the second half of a sentence that goes against the first half. Peronism is a topic where supporters and critics disagree, so these connectors help you put two views side by side without taking sides.",
[["Perón tenía el apoyo de los sindicatos; sin embargo, sus críticos decían que limitaba la prensa.","*sin embargo*: however (the second view goes against the first)"],["Se ampliaron los derechos laborales; no obstante, la oposición desconfiaba del gobierno.","*no obstante*: nevertheless (more formal)"],["El peronismo fue prohibido en 1955; sin embargo, siguió vivo entre los obreros.","contrast: what happened is the opposite of what was expected"],["Evita murió en 1952; no obstante, su figura sigue presente.","contrast: a loss, then something that continues"]],
'Contrast connectors',
[("Perón tenía el apoyo de los sindicatos; sin embargo, sus críticos decían que limitaba la prensa.","Perón had the support of the unions; however, his critics said he limited the press."),("Se ampliaron los derechos laborales; no obstante, la oposición desconfiaba del gobierno.","Labour rights were extended; nevertheless, the opposition distrusted the government."),("El peronismo fue prohibido en 1955; sin embargo, siguió vivo entre los obreros.","Peronism was banned in 1955; however, it stayed alive among workers."),("Evita murió en 1952; no obstante, su figura sigue presente.","Evita died in 1952; nevertheless, her figure is still present.")],
"A semicolon or a full stop comes before the connector and a comma after it: *…; sin embargo, …*. Use a contrast connector only when the second idea goes against the first. For a result, use *por eso* or *así que*. When you report a political view, say whose view it is (*sus críticos decían*, *sus partidarios creen*).")
vocab(S(n),'Peronism: workers, press and the vote',[('sindicato','trade union','noun'),('obrero','worker (in a factory)','noun'),('golpe','coup, blow','noun'),('voto','vote','noun'),('aguinaldo','extra month of pay at the end of the year','noun'),('prensa','press, newspapers','noun')])
T='contrast-concession-connectors'
ex=[
mc(I(n,1),"Perón had the support of the unions, but his critics said he limited the press. Which sentence joins the two ideas as a contrast?",["Perón tenía el apoyo de los sindicatos; sin embargo, sus críticos decían que limitaba la prensa.","Perón tenía el apoyo de los sindicatos; por eso, sus críticos decían que limitaba la prensa.","Perón tenía el apoyo de los sindicatos; así que sus críticos decían que limitaba la prensa."],0,T,ds={"1":"porque-y-por-eso"}),
fb(I(n,2),"El gobierno amplió los derechos de los obreros; no __, sus críticos decían que limitaba la prensa.","obstante","The government extended the workers' rights; nevertheless, its critics said it limited the press.",T),
sb(I(n,3),"El peronismo fue prohibido en 1955; sin embargo, siguió vivo entre los obreros.","Peronism was banned in 1955; however, it stayed alive among the workers.",T),
mt(I(n,4),[["el sindicato","trade union"],["el voto","vote"],["el aguinaldo","extra month of pay at year end"],["la prensa","the press, newspapers"]],V),
dc(I(n,5),[("Meg","¿Qué pasó con el peronismo después del golpe de 1955?"),("Carlos","_____"),("Meg","Entonces tenía mucho apoyo entre los obreros.")],["Estuvo prohibido; no obstante, siguió vivo entre los obreros.","Estuvo prohibido; por eso, siguió vivo entre los obreros.","Estuvo prohibido; además, siguió vivo entre los obreros."],0,T),
rdg(I(n,6),"According to the text, what happened in 1947?",["Se aprobó la ley del voto femenino.","Murió Juan Domingo Perón.","Aviones bombardearon la Plaza de Mayo."],0),
]
ex[4]['category']='dialogue'
exfile(S(n),ex); lesson(S(n),'Argentina: Peronism, supporters and critics',[f'ex0{k}' for k in range(1,7)],dlg=['ex05'])

# ---------- 02
n='02'
story(S(n),'La última dictadura militar y la guerra de Malvinas','The military dictatorship of 1976–1983 held thousands of people in secret detention centres; the Malvinas war of 1982 weakened it, and the leaders were put on trial in 1985 and again after 2003.',[
"El 24 de marzo de 1976 una junta militar derrocó a la presidenta María Estela Martínez de Perón y tomó el poder. La dictadura, que se llamó a sí misma «Proceso de Reorganización Nacional», duró hasta 1983. El gobierno suspendió la actividad de los partidos políticos y ejerció la censura sobre la prensa.",
"Durante esos años las fuerzas armadas detuvieron a miles de personas sin orden judicial y las llevaron a centros clandestinos de detención, como el de la Escuela de Mecánica de la Armada, en Buenos Aires. Muchas de esas personas nunca volvieron a aparecer: se las llama desaparecidos.",
"En 1983 el presidente Raúl Alfonsín creó la CONADEP, una comisión para investigar esos casos. Su informe, *Nunca más*, se publicó en 1984 y documentó unos 8.960 casos de desaparición. Los organismos de derechos humanos hablan de 30.000 desaparecidos.".replace('*',''),
"En abril de 1982 el gobierno militar ocupó las islas Malvinas, que están bajo administración británica y que Argentina reclama como propias, y comenzó una guerra con el Reino Unido. Argentina se rindió en junio. La derrota debilitó mucho a los militares, y Raúl Alfonsín ganó las elecciones de octubre de 1983.",
"En 1985 nueve excomandantes de las juntas fueron juzgados en un tribunal civil; Jorge Videla y Emilio Massera recibieron cadena perpetua. Después, las leyes de Punto Final y Obediencia Debida, de 1986 y 1987, y los indultos de 1989 y 1990 frenaron muchos otros juicios. En 2003 el Congreso anuló esas leyes, y los juicios se reabrieron.",
],[
("When did the military take power, according to the text?",["El 24 de marzo de 1976.","En abril de 1982.","En octubre de 1983."],"The first paragraph gives the date of the coup."),
("What does the text say about the number of disappeared people?",["El informe de 1984 documentó unos 8.960 casos, y los organismos de derechos humanos hablan de 30.000.","El informe de 1984 documentó unos 30.000 casos, y los organismos de derechos humanos hablan de 8.960.","Nadie ha dado nunca una cifra."],"The third paragraph gives both figures and says who gives each."),
("What happened in 2003?",["El Congreso anuló las leyes que frenaban los juicios.","Argentina se rindió en la guerra de Malvinas.","Nueve excomandantes recibieron cadena perpetua."],"The last paragraph says the laws were annulled."),
])
grammar(S(n),'grammar.b2.argentinasociedad.02.ser-participio-dictadura','Who Did What to Whom: The Passive with Ser',
"You know the passive with *ser* + past participle from B1 Unit 18: *La ley fue aprobada por el Parlamento*. The participle agrees with the subject, and *por* names who did the action. Reports on the dictatorship use it because the people and the institutions that were affected come first.",
[["Miles de personas fueron detenidas sin orden judicial.","*fueron detenidas*: plural, feminine (*personas*)"],["La CONADEP fue creada por el presidente Alfonsín.","*fue creada*: singular, feminine; *por* names the agent"],["Los excomandantes fueron juzgados en 1985.","*fueron juzgados*: plural, masculine"],["Las leyes fueron anuladas por el Congreso en 2003.","*fueron anuladas*: plural, feminine; *por el Congreso*"]],
'Ser + participle',
[("Miles de personas fueron detenidas sin orden judicial.","Thousands of people were detained without a court order."),("La CONADEP fue creada por el presidente Alfonsín.","The CONADEP was created by President Alfonsín."),("Los excomandantes fueron juzgados en 1985.","The former commanders were tried in 1985."),("Las leyes fueron anuladas por el Congreso en 2003.","The laws were annulled by Congress in 2003.")],
"Put *ser* in the tense you need (*fue*, *fueron*) and make the participle agree: *creada*, *juzgados*. Add *por* + the agent only when you want to name who did it. If the agent does not matter, you can use the *se* passive, as in *se publican las leyes*.")
vocab(S(n),'The dictatorship: repression, trials and defeat',[('dictadura','dictatorship','noun'),('desaparecido','person who disappeared (taken and never seen again)','noun'),('clandestino','secret, hidden','adjective'),('censura','censorship','noun'),('derrota','defeat','noun'),('juicio','trial','noun')])
T='ser-passive'
ex=[
mc(I(n,1),"Which sentence says that the CONADEP was created by President Alfonsín?",["La CONADEP fue creada por el presidente Alfonsín.","La CONADEP fue creado por el presidente Alfonsín.","La CONADEP fue creada al presidente Alfonsín."],0,T),
fb(I(n,2),"Los excomandantes de las juntas __ juzgados en 1985.","fueron","The former commanders of the juntas were tried in 1985.",T),
sb(I(n,3),"Las leyes fueron anuladas por el Congreso en 2003.","The laws were annulled by Congress in 2003.",T),
mt(I(n,4),[["la dictadura","dictatorship"],["el desaparecido","person who disappeared"],["la censura","censorship"],["la derrota","defeat"]],V),
dc(I(n,5),[("Meg","¿Qué pasó en 1985 en Argentina?"),("Carlos","_____"),("Meg","Ahora entiendo por qué se habla tanto de ese juicio.")],["Nueve excomandantes de las juntas fueron juzgados por un tribunal civil.","Nueve excomandantes de las juntas fueron elegidos presidentes por el pueblo.","Nueve excomandantes de las juntas fueron llevados a un centro clandestino."],0,V,cat='dialogue'),
rdg(I(n,6),"According to the text, how many cases of disappearance did the report *Nunca más* document?",["Unos 8.960 casos.","Unos 30.000 casos.","Unos 1.500 casos."],0),
]
exfile(S(n),ex); lesson(S(n),'Argentina: the last dictatorship (1976–1983) and the Malvinas war',[f'ex0{k}' for k in range(1,7)],dlg=['ex05'])

# ---------- 03
n='03'
story(S(n),'Las Madres y las Abuelas de Plaza de Mayo','Mothers and grandmothers of the disappeared began meeting at the Plaza de Mayo in 1977; the Abuelas searched for children taken during the dictatorship, and genetic tests and a national data bank helped to prove their identity.',[
"El 30 de abril de 1977, catorce mujeres se reunieron en la Plaza de Mayo, frente a la Casa Rosada, para pedir noticias de sus hijos desaparecidos. Entre ellas estaba Azucena Villaflor. Como la policía les ordenaba circular, empezaron a caminar en ronda, y desde entonces se reúnen los jueves. Llevan un pañuelo blanco en la cabeza. Azucena Villaflor fue secuestrada en diciembre de 1977.",
"Otras mujeres, las Abuelas de Plaza de Mayo, buscaban a sus nietos. Algunos niños habían sido secuestrados con sus padres, y otros habían nacido en centros clandestinos mientras sus madres estaban detenidas. Según las Abuelas, fueron unos quinientos niños. Muchos de ellos crecieron con otras familias y con otra identidad.",
"Para probar quién era cada persona hacía falta un método científico. En los años ochenta, con la ayuda de genetistas, se desarrolló el «índice de abuelidad», un análisis genético que permite comparar el ADN de un joven con el de sus abuelos y otros parientes. En 1987 se creó el Banco Nacional de Datos Genéticos, que guarda muestras de familiares. En 1984 se formó además el Equipo Argentino de Antropología Forense, que busca e identifica restos de desaparecidos.",
"Los testimonios de familiares también fueron importantes en el juicio de 1985 a las juntas militares. Hoy las Abuelas siguen buscando a las personas que todavía no conocen su verdadero origen, y piden a quienes tengan dudas sobre su identidad que se acerquen a la asociación. Según la asociación, más de cien personas ya han recuperado su identidad.",
],[
("When did the first fourteen women meet at the Plaza de Mayo?",["El 30 de abril de 1977.","El 17 de octubre de 1945.","En diciembre de 2001."],"The first paragraph gives the date."),
("What do the Abuelas say about the number of children involved?",["Según las Abuelas, fueron unos quinientos niños.","Según las Abuelas, fueron solo tres niños.","Las Abuelas no han dado ninguna cifra."],"The second paragraph attributes the figure to the Abuelas."),
("What did the National Genetic Data Bank do, according to the text?",["Guarda muestras de familiares.","Juzga a los comandantes.","Entrega pañuelos blancos."],"The third paragraph says it keeps samples from relatives."),
])
grammar(S(n),'grammar.b2.argentinasociedad.03.subjuntivo-busqueda-nietos','Looking for People Who May Not Be Found: Relative Clauses',
"You know *Busco un apartamento que tenga balcón* from B2 Unit 13: a relative clause with *que* takes the subjunctive when you cannot point at the person or thing: you are looking for it, you do not know if it exists, or it does not exist. The search of the Abuelas de Plaza de Mayo is exactly that: they look for grandchildren who do not yet know who they are.",
[["Las Abuelas buscan a nietos que no conozcan su origen.","subjunctive: they do not know who or where those grandchildren are"],["Las Abuelas conocen a un joven que recuperó su identidad.","indicative: a real person they can name"],["Piden a las personas que tengan dudas que se acerquen.","subjunctive: anyone who might have doubts"],["No hay ningún documento que diga dónde está el niño.","subjunctive: nothing like that exists"]],
'Subjunctive or indicative after que?',
[("Las Abuelas buscan a nietos que no conozcan su origen.","The Abuelas look for grandchildren who may not know their origin."),("Las Abuelas conocen a un joven que recuperó su identidad.","The Abuelas know a young man who recovered his identity."),("Piden a las personas que tengan dudas que se acerquen.","They ask people who have doubts to come forward."),("No hay ningún documento que diga dónde está el niño.","There is no document that says where the child is.")],
"Ask yourself: can I point at it? If yes, the indicative (*un joven que recuperó*). If you are only looking for it, it may not exist or it does not exist, the subjunctive (*que no conozcan*, *que diga*). Keep the personal *a* before people: *buscan a nietos que…*.")
vocab(S(n),'The Madres and Abuelas: memory and identity',[('pañuelo','headscarf, handkerchief','noun'),('nieto','grandson, grandchild','noun'),('ronda','walking in a circle','noun'),('memoria','memory','noun'),('testimonio','testimony, account given by a witness','noun'),('identidad','identity','noun')])
T='relativas-subjuntivo'
ex=[
mc(I(n,1),"The Abuelas do not know who these grandchildren are or whether they can find them. Which sentence says this?",["Las Abuelas buscan a nietos que no conozcan su origen.","Las Abuelas buscan a nietos que no conocen su origen.","Las Abuelas buscan a nietos que no conocerán su origen."],0,T,ds={"2":"futuro-simple"}),
fb(I(n,2),"No hay ningún documento que __ dónde está el niño.","diga","There is no document that says where the child is.",T),
sb(I(n,3),"Las Abuelas buscan a jóvenes que no conozcan su origen.","The Abuelas look for young people who may not know their origin.",T),
mt(I(n,4),[["el pañuelo","headscarf"],["el nieto","grandson"],["la memoria","memory"],["el testimonio","testimony of a witness"]],V),
dc(I(n,5),[("Meg","¿Qué hacen las Madres los jueves en la Plaza de Mayo?"),("Carlos","_____"),("Meg","Entiendo, es una forma de no olvidar.")],["Caminan en ronda con un pañuelo en la cabeza.","Caminan en ronda con un libro en la mano.","Votan en la plaza con un pañuelo en la cabeza."],0,V,cat='dialogue'),
rdg(I(n,6),"According to the text, what did people need a scientific method for?",["Para probar la identidad de cada persona.","Para juzgar a las juntas militares.","Para pedir el voto de los jóvenes."],0),
]
exfile(S(n),ex); lesson(S(n),'Argentina: the Madres and Abuelas de Plaza de Mayo',[f'ex0{k}' for k in range(1,7)],dlg=['ex05'])

# ---------- 04
n='04'
story(S(n),'El fútbol argentino: de los potreros a Qatar','Football reached Argentina in the 19th century and became a mass passion; the text follows Maradona in 1986, Messi in 2022 and how people celebrated.',[
"El fútbol llegó a la Argentina a fines del siglo XIX con los británicos que vivían en Buenos Aires. La Asociación del Fútbol Argentino se fundó en 1893. Pronto los hijos de los inmigrantes jugaban en los potreros, los terrenos vacíos de los barrios, con una pelota y poco más.",
"La selección argentina ganó el Mundial de 1978, que se jugó en el país durante la dictadura, y el de 1986, en México. La figura de ese segundo título fue Diego Armando Maradona (1960–2020). En los cuartos de final contra Inglaterra, el 22 de junio de 1986, hizo dos goles. Al primero, marcado con la mano, lo llamó después «la mano de Dios»; el segundo es considerado por muchos uno de los goles más recordados de la historia. Cuatro años antes, Argentina y el Reino Unido habían estado en guerra por las islas Malvinas, y muchos argentinos vivieron ese partido con un significado especial.",
"Con el Nápoles, Maradona ganó dos veces la liga italiana. Cuando murió, en noviembre de 2020, miles de personas hicieron fila para despedirse de él.",
"En diciembre de 2022, en Qatar, la selección de Lionel Messi, nacido en Rosario en 1987, ganó su tercer Mundial: venció a Francia en los penales después de un 3 a 3. Según distintas estimaciones, millones de personas salieron a las calles de Buenos Aires para festejar.",
"Para muchos argentinos, ir a la cancha con la hinchada y cantar con ella es una parte importante de la vida del fin de semana.",
],[
("What are the \"potreros\" in the text?",["Terrenos vacíos de los barrios donde jugaban los niños.","Estadios grandes de Buenos Aires.","Equipos británicos de fútbol."],"The first paragraph explains the word."),
("What happened on 22 June 1986, according to the text?",["Argentina jugó contra Inglaterra y Maradona hizo dos goles.","Argentina ganó su tercer Mundial en Qatar.","Maradona murió en Buenos Aires."],"The second paragraph describes the quarter-final."),
("How does the text describe the celebrations of December 2022?",["Según distintas estimaciones, millones de personas salieron a las calles.","Nadie salió a festejar porque llovía.","Solo unos cientos de personas fueron al Obelisco."],"The fourth paragraph attributes the figure to different estimates."),
])
grammar(S(n),'grammar.b2.argentinasociedad.04.superlativos-futbol','The Most Remembered Goals: Superlatives',
"You know *la mejor opción* and *utilísimo* from B1 Unit 7: *el/la/los/las más* + adjective (*el gol más famoso*), *el mejor* and *el peor*, and *-ísimo* for \"very\". Football talk is full of them. Remember that *uno de los más…* is a safer way to rank than *el más…*, because it says that something is among the best, not the only best.",
[["Maradona es uno de los jugadores más famosos de la historia.","*uno de los* + plural noun + *más* + adjective: one of the most famous"],["Ese gol es uno de los más recordados del Mundial de 1986.","the noun can be left out after *uno de los más*"],["El estadio estaba llenísimo de hinchas.","*-ísimo*: extremely full (*lleno* → *llenísimo*)"],["El potrero es el lugar más sencillo para jugar.","*el lugar más sencillo*: the simplest place"]],
'Superlatives at work',
[("Maradona es uno de los jugadores más famosos de la historia.","Maradona is one of the most famous players in history."),("Ese gol es uno de los más recordados del Mundial de 1986.","That goal is one of the most remembered of the 1986 World Cup."),("El estadio estaba llenísimo de hinchas.","The stadium was packed with fans."),("El potrero es el lugar más sencillo para jugar.","The vacant lot is the simplest place to play.")],
"After *uno de los*, the noun is plural and so is the adjective: *jugadores más famosos*. Never say *más mejor*. With *-ísimo* the word changes in gender and number too: *llenísima*, *llenísimos*. A superlative is a judgement: give the opinion to someone (*para muchos argentinos*) when you write about history.")
vocab(S(n),'Argentine football: from the potrero to the stadium',[('potrero','vacant lot where children play football','noun'),('hincha','fan, supporter','noun'),('estadio','stadium','noun'),('selección','national team','noun'),('festejar','to celebrate','verb'),('ídolo','idol, hero of the fans','noun')])
T='superlatives'
ex=[
mc(I(n,1),"Which sentence says that Maradona is one of the most famous players in history?",["Maradona es uno de los jugadores más famosos de la historia.","Maradona es uno de los jugadores más famoso de la historia.","Maradona es uno de los jugadores famosos más de la historia."],0,T),
fb(I(n,2),"El estadio estaba __ de hinchas.","llenísimo","The stadium was packed with fans.",T,hint="lleno, extremely"),
sb(I(n,3),"Ese gol es uno de los más recordados del Mundial de 1986.","That goal is one of the most remembered of the 1986 World Cup.",T),
mt(I(n,4),[["el potrero","vacant lot for street football"],["el hincha","fan, supporter"],["la selección","national team"],["el ídolo","idol"]],V),
dc(I(n,5),[("Meg","¿Qué hicieron muchos argentinos cuando la selección ganó en Qatar?"),("Carlos","_____"),("Meg","Debió de ser una noche inolvidable.")],["Salieron a las calles de Buenos Aires para festejar.","Se quedaron en los potreros para jugar con una pelota.","Viajaron a Rosario para ver a Messi."],0,V,cat='dialogue'),
rdg(I(n,6),"What happened in the quarter-final of 1986, according to the text?",["Argentina jugó contra Inglaterra y Maradona hizo dos goles.","Argentina jugó contra Francia y ganó en los penales.","Argentina perdió contra Inglaterra por dos goles."],0),
]
exfile(S(n),ex); lesson(S(n),'Argentina: football, from the vacant lot to Qatar 2022',[f'ex0{k}' for k in range(1,7)],dlg=['ex05'])

# ---------- 05
n='05'
story(S(n),'La crisis de 2001 y la respuesta de la gente','In December 2001 Argentina went through the corralito, mass protests and the resignation of the president; people answered with neighbourhood assemblies, barter clubs and recovered factories, and later crises followed.',[
"En los años noventa, con el plan de convertibilidad, un peso valía un dólar. Pero la economía estaba en recesión desde 1998, la deuda externa era muy grande y mucha gente había perdido su trabajo.",
"A principios de diciembre de 2001, debido a la salida de dinero de los bancos, el gobierno del presidente Fernando de la Rúa limitó los retiros de efectivo: era el «corralito». Muchas personas no podían usar sus ahorros. Las protestas crecieron; el 19 de diciembre se declaró el estado de sitio, y esa noche miles de personas salieron a golpear cacerolas, en el llamado «cacerolazo». En los días 19 y 20 murieron 39 personas en el país, y la justicia investigó después la responsabilidad de funcionarios y policías. De la Rúa renunció el 20 de diciembre, y en pocas semanas pasaron por la presidencia varias personas.",
"La gente buscó sus propias soluciones. Los vecinos se reunieron en asambleas barriales; en los clubes de trueque se intercambiaban productos y servicios sin pesos; y en algunas fábricas cerradas los trabajadores siguieron produciendo: son las fábricas recuperadas. Un lema muy repetido en las calles era «Que se vayan todos». Según el INDEC, en 2002 más de la mitad de la población vivía bajo la línea de pobreza.",
"La economía empezó a recuperarse en 2003, pero los problemas económicos volvieron más tarde. En 2023 la inflación anual superó el 200 %, según el INDEC. Desde diciembre de 2023 el presidente es Javier Milei, que aplicó un fuerte ajuste del gasto público. Según el INDEC, la inflación bajó con fuerza desde 2024 y en 2025 y 2026 rondó el 2 % mensual.",
],[
("What was the \"corralito\", according to the text?",["Una medida que limitó los retiros de dinero de los bancos.","Un plan para que un peso valiera un dólar.","Una fábrica recuperada por sus trabajadores."],"The second paragraph defines it."),
("What did people do in the barter clubs?",["Intercambiaban productos y servicios sin pesos.","Compraban dólares con sus ahorros.","Cerraban las fábricas del barrio."],"The third paragraph describes the clubs."),
("What does the text say about inflation after 2023?",["Según el INDEC, bajó con fuerza desde 2024.","Según el INDEC, superó el 200 % en 2025.","Según el INDEC, desapareció en 2002."],"The last paragraph gives the INDEC view."),
])
grammar(S(n),'grammar.b2.argentinasociedad.05.debido-a-a-raiz-de-crisis','Why It Happened: Debido a and A Raíz de',
"You know *porque* from A1, *por eso* from A2 Unit 5 and *así que* from B1 Unit 1, and you know the formal cause connectors *debido a* and *a raíz de* from B1 Unit 6. They are the natural tools to explain the crisis of December 2001: what caused what.",
[["Debido al corralito, muchas personas no podían usar sus ahorros.","*debido a* + noun: because of"],["A raíz de las protestas, De la Rúa renunció el 20 de diciembre.","*a raíz de* + noun: as a result of"],["Se formaron clubes de trueque porque faltaba dinero.","*porque* + verb: a whole clause"],["Había poco dinero, así que la gente intercambiaba productos.","*así que*: consequence"]],
'Cause and result',
[("Debido al corralito, muchas personas no podían usar sus ahorros.","Because of the corralito, many people could not use their savings."),("A raíz de las protestas, De la Rúa renunció el 20 de diciembre.","As a result of the protests, De la Rúa resigned on 20 December."),("Se formaron clubes de trueque porque faltaba dinero.","Barter clubs formed because money was short."),("Había poco dinero, así que la gente intercambiaba productos.","There was little money, so people exchanged goods.")],
"*Debido a* and *a raíz de* take a noun (*debido al corralito*), never a verb; use *porque* before a verb. *Debido a* + *el* becomes *debido al*. *A raíz de* often points to an event that started something: *a raíz de las protestas*.")
vocab(S(n),'The 2001 crisis: money, protest and barter',[('corralito','limit on bank withdrawals in 2001','noun'),('cacerolazo','protest banging pots and pans','noun'),('trueque','barter, swapping goods','noun'),('ahorros','savings','noun'),('asamblea','assembly, meeting of neighbours','noun'),('inflación','inflation','noun')])
T='formal-cause-connectors'
ex=[
mc(I(n,1),"Which sentence says that, because of the corralito, many people could not use their savings?",["Debido al corralito, muchas personas no podían usar sus ahorros.","Debido el corralito, muchas personas no podían usar sus ahorros.","Debido a fue el corralito, muchas personas no podían usar sus ahorros."],0,T),
fb(I(n,2),"El presidente renunció a __ de las protestas del 19 y 20 de diciembre.","raíz","The president resigned as a result of the protests of 19 and 20 December.",T),
sb(I(n,3),"Debido a la falta de dinero, aparecieron los clubes de trueque.","Because of the lack of money, barter clubs appeared.",T),
mt(I(n,4),[["el corralito","limit on bank withdrawals"],["el cacerolazo","protest banging pots"],["el trueque","barter"],["los ahorros","savings"]],V),
dc(I(n,5),[("Meg","¿Por qué la gente salió a la calle en diciembre de 2001?"),("Carlos","_____"),("Meg","Ahora lo entiendo mejor.")],["Debido al corralito, no podían sacar sus ahorros del banco.","Porque quería festejar el Mundial en el estadio.","Para festejar que la inflación había bajado en 2024."],0,V,cat='dialogue'),
rdg(I(n,6),"What did the neighbours do in the assemblies, according to the text?",["Se reunieron en asambleas para buscar soluciones.","Compraron las fábricas que habían cerrado.","Declararon el estado de sitio en la ciudad."],0),
]
exfile(S(n),ex); lesson(S(n),'Argentina: the 2001 crisis and how people responded',[f'ex0{k}' for k in range(1,7)],dlg=['ex05'])

# ---------- consolidation
n='consolidation'
T1,T2,T3,T4,T5='contrast-concession-connectors','ser-passive','relativas-subjuntivo','superlatives','formal-cause-connectors'
ex=[
mc(I(n,1),"The economy began to recover in 2003, but crises came back later. Which sentence joins the two ideas as a contrast?",["La economía empezó a recuperarse en 2003; sin embargo, las crisis volvieron más tarde.","La economía empezó a recuperarse en 2003; por eso, las crisis volvieron más tarde.","La economía empezó a recuperarse en 2003; así que las crisis volvieron más tarde."],0,T1,ds={"1":"porque-y-por-eso"}),
fb(I(n,2),"El informe *Nunca más* __ publicado en 1984.".replace('*',''),"fue","The report Nunca más was published in 1984.",T2),
mc(I(n,3),"Nobody in the family knows where the grandson is. Which sentence says there is no one who can tell?",["No hay nadie en la familia que sepa dónde está el nieto.","No hay nadie en la familia que sabe dónde está el nieto.","No hay nadie en la familia que supo dónde está el nieto."],0,T3,ds={"2":"preterito-indefinido"}),
fb(I(n,4),"Maradona es uno de los ídolos __ queridos del fútbol argentino.","más","Maradona is one of the most loved idols of Argentine football.",T4),
mc(I(n,5),"Which sentence says that the neighbourhood assemblies appeared as a result of the crisis of 2001?",["A raíz de la crisis de 2001, aparecieron las asambleas de vecinos.","A raíz la crisis de 2001, aparecieron las asambleas de vecinos.","A raíz de se cerraron los bancos, aparecieron las asambleas de vecinos."],0,T5),
mt(I(n,6),[["la dictadura","dictatorship"],["el sindicato","trade union"],["el hincha","fan, supporter"],["el trueque","barter"]],V),
rdg(I(n,7),"According to the readings of this unit, what happened on 24 March 1976?",["Una junta militar tomó el poder.","Perón volvió a la presidencia.","Argentina ganó el Mundial de Qatar."],0),
sb(I(n,8),"El peronismo fue prohibido durante casi veinte años.","Peronism was banned for almost twenty years.",T2),
]
exfile(S(n),ex)
d=rd('lessons/b2/b2-argentinasociedad-consolidation.json')
d['title']='Argentina: review of politics, memory, football and crisis'
for s in d['sections']:
    if s['type']=='goal': s['items']=["I can review contrast, the passive, relative clauses, superlatives and cause connectors on Argentine topics.","I can use the words for Peronism, the dictatorship, football and the 2001 crisis.","I can read about modern Argentina and answer questions about what the texts say."]
    if s['type']=='checklist': s['items']=["I can set two views of Peronism side by side with *sin embargo* and *no obstante*.","I can say what was done to people and institutions under the dictatorship with *ser* + participle.","I can describe the people the Abuelas de Plaza de Mayo are looking for with a relative clause and the subjunctive.","I can rank moments of Argentine football with *uno de los más…*.","I can give the causes of the 2001 crisis with *debido a* and *a raíz de*."]
wr('lessons/b2/b2-argentinasociedad-consolidation.json',d)
