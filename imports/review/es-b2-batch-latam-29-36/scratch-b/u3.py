import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-legal-pluralism-vocab'
T=lambda t,c:{"type":t,"content":c}
def ex(items): return {"type":"examples","title":"In context","items":[{"spanish":a,"english":b} for a,b in items]}
def wc(stem,paras): print(stem,words(paras))

s='b2-pluralismo-01'
lesson(s,"Indigenous rights in Latin America: from ILO Convention 169 to the new constitutions","I can contrast two facts with *sin embargo* and *no obstante*.")
grammar(s,"However, Nevertheless: Contrasting Two Facts",[
 {"type":"text","title":"What you already know","content":"You know *sin embargo* from A2 Unit 28 and *no obstante* from B1 Unit 1: both introduce a fact that goes against what you have just said. *No obstante* is a little more formal. The recognition of indigenous rights is full of such contrasts: a law is passed, \"however\" its application is hard."},
 ex([("El Convenio 169 es de 1989; no obstante, muchos conflictos por la consulta siguen abiertos.","Convention 169 dates from 1989; nevertheless, many conflicts over consultation remain open."),
     ("La Declaración de 2007 no es un tratado; sin embargo, se cita con frecuencia.","The 2007 Declaration is not a treaty; however, it is often cited."),
     ("Ecuador aprobó su Constitución en 2008; sin embargo, algunas comunidades piden más participación.","Ecuador approved its Constitution in 2008; however, some communities ask for more participation."),
     ("Colombia reconoció la diversidad en 1991; no obstante, la aplicación sigue siendo discutida.","Colombia recognised diversity in 1991; nevertheless, its application is still debated.")]),
 T("tip","*Sin embargo* and *no obstante* usually start the second clause and take a comma after them: *…; sin embargo, …*. Do not use *por eso* or *además* in their place: they do not contrast.")])
exercises(s,[
 mc(1,s,"grammar","contrast-concession-connectors","Which sentence means \"The convention was approved in 1989; nevertheless, many conflicts remain\"?",
  ["El convenio se aprobó en 1989; no obstante, todavía hay muchos conflictos.","El convenio se aprobó en 1989; por eso, todavía hay muchos conflictos.","El convenio se aprobó en 1989; además, todavía hay muchos conflictos."],0,{1:"porque-y-por-eso",2:"ordering-markers"}),
 fb(2,s,"contrast-concession-connectors","La Declaración de 2007 no es un tratado; sin __, se cita con frecuencia.","embargo","The 2007 Declaration is not a treaty; however, it is often cited."),
 mt(3,s,V,[("pueblo indígena","indigenous people"),("consulta","consultation"),("convenio","convention (agreement)"),("tribunal","court")]),
 mc(4,s,"reading","","When did the ILO approve Convention 169, according to the text?",
  ["En 1989.","En 1957.","En 2007."],0)])
vocab(s,"Indigenous rights",[("pueblo indígena","indigenous people","expression"),("consulta","consultation","noun"),("convenio","convention (agreement)","noun"),("tribunal","court","noun")])
P=["Durante buena parte del siglo XX, muchos Estados latinoamericanos querían integrar a los pueblos indígenas en la vida nacional y no siempre respetaban sus instituciones propias. Esa idea aparece en el Convenio 107 de la Organización Internacional del Trabajo (OIT), de 1957.",
"Desde los años setenta, las organizaciones indígenas pidieron otro trato. En Ecuador se fundó en 1986 la CONAIE, la Confederación de Nacionalidades Indígenas del Ecuador.",
"En 1989 la OIT aprobó el Convenio 169, que reemplazó al 107. El convenio exige consultar a los pueblos indígenas antes de tomar medidas que los afecten, y reconoce su derecho a mantener sus costumbres e instituciones. En 2007 la Asamblea General de las Naciones Unidas aprobó la Declaración sobre los Derechos de los Pueblos Indígenas. La Declaración no es un tratado; no obstante, se cita con frecuencia como referencia.",
"Varias constituciones cambiaron. Colombia, en 1991, reconoció la diversidad étnica y cultural de la nación y permitió a las autoridades indígenas aplicar su propia justicia. Ecuador, con una Constitución aprobada por referéndum el 28 de septiembre de 2008, y Bolivia, con la de 2009, se declararon Estados plurinacionales.",
"Sin embargo, aplicar estas normas no es fácil. Muchos conflictos giran en torno a proyectos mineros y petroleros en territorios indígenas, y según organizaciones indígenas la consulta no siempre se hace antes de que empiece el proyecto."]
wc(s,P)
story(s,"De la integración a los derechos indígenas","From the ILO's integration approach of 1957 to Convention 169 (1989), the UN Declaration (2007) and the plurinational constitutions of Colombia, Ecuador and Bolivia, with the difficulty of applying them.",P,[
 ("Which ILO convention did Convention 169 replace, according to the text?",["El Convenio 107.","El Convenio 100.","El Convenio 200."],0,"The third paragraph says it replaced Convention 107."),
 ("How was Ecuador's Constitution of 2008 approved, according to the text?",["Por referéndum el 28 de septiembre de 2008.","Por decreto del presidente.","Por una orden de la ONU."],0,"The fourth paragraph says so."),
 ("What do indigenous organisations say about consultation, according to the text?",["No siempre se hace antes de que empiece el proyecto.","Siempre se hace demasiado pronto.","Ya no hace falta."],0,"The last paragraph says so.")])

s='b2-pluralismo-02'
lesson(s,"Indigenous justice in the Andes: assemblies, patrols and jurisdiction","I can describe a place, a law or an institution with *en la que*, *con la que* and other relatives with a preposition.")
grammar(s,"The Place In Which, The Law With Which",[
 {"type":"text","title":"What you already know","content":"You know relative clauses with *el que* and a preposition from B1 Unit 20: the preposition goes before *el que*, *la que*, *los que* or *las que*, and the article matches the noun (*el edificio en el que vivimos*). They are the tool for describing institutions: the place in which a community decides, the law with which a country recognises its patrols."},
 ex([("La asamblea es el lugar en el que la comunidad discute los casos.","The assembly is the place in which the community discusses cases."),
     ("La Constitución de 1991 reconoce a las comunidades indígenas, a las que permite aplicar su propia justicia en su territorio.","The 1991 Constitution recognises the indigenous communities, which it allows to apply their own justice in their territory."),
     ("Las rondas campesinas son organizaciones de las que forman parte muchos campesinos.","The peasant patrols are organisations that many peasants belong to."),
     ("La ley de 2003 es la norma con la que Perú reconoció a las rondas.","The 2003 law is the rule with which Peru recognised the patrols.")]),
 T("tip","Keep the preposition that the verb or noun needs, and match the article: *la ley con la que*, *los vecinos con los que*. Without the preposition the sentence is wrong: not *el lugar que la comunidad discute los casos*.")])
exercises(s,[
 mc(1,s,"grammar","relativas-preposicion-el-que","Which sentence means \"The assembly is the place in which the community discusses cases\"?",
  ["La asamblea es el lugar en el que la comunidad discute los casos.","La asamblea es el lugar que la comunidad discute los casos.","La asamblea es el lugar en la que la comunidad discute los casos."],0),
 fb(2,s,"relativas-preposicion-el-que","La ley de 2003 es la norma __ la que Perú reconoció a las rondas.","con","The 2003 law is the rule with which Peru recognised the patrols."),
 mt(3,s,V,[("asamblea","assembly"),("jurisdicción","jurisdiction"),("ronda campesina","peasant patrol"),("costumbre","custom")]),
 mc(4,s,"reading","","What does the Peruvian Constitution of 1993 allow, according to the text?",
  ["Que las comunidades apliquen justicia en su territorio.","Que las comunidades cambien las leyes del país.","Que las comunidades cobren los impuestos del Estado."],0)])
vocab(s,"Indigenous justice",[("asamblea","assembly","noun"),("jurisdicción","jurisdiction","noun"),("ronda campesina","peasant patrol","expression"),("costumbre","custom","noun")])
P=["En muchos países de América Latina, las comunidades indígenas y campesinas tienen formas propias de resolver los conflictos. Suelen usar la asamblea, un lugar en el que los vecinos discuten el caso y buscan una solución que repare el daño y mantenga la paz en la comunidad.",
"En Colombia, la Constitución de 1991 reconoce a las autoridades de los pueblos indígenas, a las que permite aplicar su propia justicia dentro de su territorio, siempre que no sea contraria a la Constitución y a las leyes.",
"En Perú, las rondas campesinas nacieron en 1976 en la provincia de Chota, en Cajamarca, para proteger el campo contra el robo de ganado. Hoy son organizaciones de las que forman parte muchos campesinos. La Constitución de 1993 permite a las comunidades campesinas y nativas ejercer funciones de justicia dentro de su territorio, y una ley de 2003 reconoció a las rondas.",
"En Bolivia, la Constitución de 2009 reconoce la justicia indígena originaria campesina con la misma jerarquía que la justicia ordinaria. En 2010 una ley de deslinde jurisdiccional dijo qué casos puede resolver cada una.",
"Una discusión frecuente es hasta dónde llega cada justicia y cómo coordinarse con los tribunales del Estado. Las constituciones de estos países ponen como límite los derechos humanos."]
wc(s,P)
story(s,"Justicia indígena y justicia del Estado","How indigenous and peasant communities in Colombia, Peru and Bolivia apply their own justice: assemblies, the rondas campesinas, the constitutions of 1991, 1993 and 2009, and the limit of human rights.",P,[
 ("Where were the rondas campesinas born in 1976, according to the text?",["En Chota, en Cajamarca.","En Lima, en la capital.","En Cusco, en el sur."],0,"The third paragraph says so."),
 ("Why did the first rondas start, according to the text?",["Para proteger el campo contra el robo de ganado.","Para cobrar impuestos.","Para abrir escuelas."],0,"The third paragraph says so."),
 ("What limit do the constitutions set, according to the text?",["Los derechos humanos.","El precio del ganado.","El número de vecinos."],0,"The last paragraph says so.")])

s='b2-pluralismo-03'
lesson(s,"Rights of nature: the Atrato river, the Colombian Amazon and Los Cedros","I can say what should happen to rivers and forests, with *es importante que* and *es necesario que* + subjunctive.")
grammar(s,"It Is Important That: Rights for Rivers and Forests",[
 {"type":"text","title":"What you already know","content":"You know *es importante que*, *es necesario que* and *es mejor que* from A2 Unit 27: after a value judgment about what someone should do, the verb after *que* is in the present subjunctive. Court rulings about rivers and forests are full of what the State, the communities and the courts should do."},
 ex([("Es importante que los ríos tengan protección legal.","It is important that rivers have legal protection."),
     ("Es necesario que el Estado cumpla las órdenes de la sentencia.","It is necessary that the State carries out the orders of the ruling."),
     ("Es mejor que las comunidades participen en la decisión.","It is better that the communities take part in the decision."),
     ("Es una lástima que algunas sentencias se apliquen despacio.","It is a pity that some rulings are applied slowly.")]),
 T("tip","With a new subject, use *que* and the present subjunctive (*cumpla*, *tengan*). With no new subject, use the infinitive: *Es importante proteger los ríos*.")])
exercises(s,[
 mc(1,s,"grammar","subjunctive-value-judgments","Which sentence means \"It is important that rivers have legal protection\"?",
  ["Es importante que los ríos tengan protección legal.","Es importante que los ríos tienen protección legal.","Es importante que los ríos tener protección legal."],0,{1:"present-tense"}),
 fb(2,s,"subjunctive-value-judgments","Es necesario que el Estado __ las órdenes de la sentencia sobre el río Atrato.","cumpla","It is necessary that the State carries out the orders of the ruling on the Atrato river."),
 mt(3,s,V,[("sentencia","court ruling"),("cuenca","river basin"),("guardián","guardian"),("selva","jungle")]),
 mc(4,s,"reading","","Which river did Colombia's Constitutional Court declare a subject of rights in 2016, according to the text?",
  ["El río Atrato.","El río Orinoco.","El río Magdalena."],0)])
vocab(s,"Rights of nature",[("sentencia","court ruling","noun"),("cuenca","river basin","noun"),("guardián","guardian","noun"),("selva","jungle","noun")])
P=["Durante mucho tiempo, el derecho trató los ríos y los bosques como recursos. Desde hace unos años, en América Latina algunas normas y sentencias los tratan como sujetos de derechos. La Constitución de Ecuador de 2008 reconoce derechos a la naturaleza, que llama Pacha Mama, y Bolivia aprobó en 2010 una ley de derechos de la Madre Tierra.",
"En noviembre de 2016 la Corte Constitucional de Colombia declaró al río Atrato, su cuenca y sus afluentes sujetos de derechos. El caso llegó a la Corte por una acción de comunidades afrodescendientes e indígenas del Chocó, que se quejaban de la minería ilegal y de la contaminación del río.",
"La sentencia nombró guardianes del río: un representante del gobierno nacional y representantes de las comunidades de la cuenca. Según organizaciones y observadores, la aplicación de las órdenes de la sentencia ha sido lenta.",
"En 2018 la Corte Suprema de Colombia reconoció a la Amazonía colombiana como sujeto de derechos y ordenó al Estado preparar un plan contra la deforestación. En Ecuador, la Corte Constitucional protegió en 2021 el bosque de Los Cedros frente a un proyecto minero, con base en los derechos de la naturaleza.",
"Algunos juristas dicen que es necesario que estas sentencias se cumplan con más rapidez para que la protección sea real; otros recuerdan que cada caso depende de lo que decida cada tribunal."]
wc(s,P)
story(s,"Ríos y bosques con derechos","Colombia's Constitutional Court declared the Atrato river a subject of rights in 2016, its Supreme Court did the same for the Amazon in 2018, and Ecuador's court protected Los Cedros in 2021, with the question of how well rulings are applied.",P,[
 ("Which region of Colombia do the communities in the Atrato case come from, according to the text?",["Del Chocó.","De Bogotá.","De San Andrés."],0,"The second paragraph says so."),
 ("Whom did the Atrato ruling name as guardians, according to the text?",["Representantes del gobierno y de las comunidades.","Solo a los jueces.","Solo a las empresas mineras."],0,"The third paragraph says so."),
 ("What did Ecuador's Constitutional Court protect in 2021, according to the text?",["El bosque de Los Cedros.","El lago Titicaca.","El río Amazonas."],0,"The fourth paragraph says so.")])

s='b2-pluralismo-04'
lesson(s,"Intercultural bilingual education: Quechua, Guaraní and digital tools","I can give a cause with *debido a* and *a raíz de*.")
grammar(s,"Because Of, As a Result Of: Causes in Education",[
 {"type":"text","title":"What you already know","content":"You know *debido a* \"because of\" and *a raíz de* \"as a result of\" from B1 Unit 6. Both take a noun (*debido a la migración*), never a verb; with a verb, use *porque*. They suit the story of languages: what made speakers fewer, and what changed after a law."},
 ex([("Debido a la migración a las ciudades, muchos niños ya no aprenden la lengua de sus abuelos.","Because of migration to the cities, many children no longer learn their grandparents' language."),
     ("A raíz de la Constitución de 1992, el guaraní es lengua oficial de Paraguay junto al castellano.","As a result of the 1992 Constitution, Guaraní is an official language of Paraguay together with Spanish."),
     ("Muchas familias dejaron de hablar la lengua porque la escuela enseñaba solo en castellano.","Many families stopped speaking the language because school taught only in Spanish."),
     ("Debido a las aplicaciones y a los cursos, hay más personas que estudian quechua.","Because of apps and courses, more people study Quechua.")]),
 T("tip","*Debido a* and *a raíz de* are followed by a noun phrase. Do not write *debido a se mudan* or *a raíz a la ley*: the second part of *a raíz de* is always *de*.")])
exercises(s,[
 mc(1,s,"grammar","formal-cause-connectors","Which sentence means \"Because of migration to the cities, many children no longer learn their grandparents' language\"?",
  ["Debido a la migración a las ciudades, muchos niños ya no aprenden la lengua de sus abuelos.","Debido a muchas familias se mudan a las ciudades, muchos niños ya no aprenden la lengua de sus abuelos.","A raíz a la migración a las ciudades, muchos niños ya no aprenden la lengua de sus abuelos."],0),
 fb(2,s,"formal-cause-connectors","A __ de la Constitución de 1992, el guaraní es lengua oficial de Paraguay junto al castellano.","raíz","As a result of the 1992 Constitution, Guaraní is an official language of Paraguay together with Spanish."),
 mt(3,s,V,[("lengua originaria","native language"),("hablante","speaker"),("bilingüe","bilingual"),("aplicación","app")]),
 mc(4,s,"reading","","Which languages are official in Paraguay, according to the text?",
  ["El castellano y el guaraní.","El castellano y el quechua.","El castellano y el inglés."],0)])
vocab(s,"Languages and school",[("lengua originaria","native language","expression"),("hablante","speaker","noun"),("bilingüe","bilingual","adjective"),("aplicación","app","noun")])
P=["Muchas lenguas originarias de América Latina tienen cada vez menos hablantes. Según muchos lingüistas, la escuela enseñó durante décadas solo en castellano, y por eso muchas familias dejaron de transmitir su lengua a los hijos. Debido a la migración a las ciudades, además, muchos niños ya no aprenden la lengua de sus abuelos.",
"La educación intercultural bilingüe intenta cambiar esto: los niños aprenden en su lengua y en castellano, y muchos programas buscan que lean primero en la lengua que hablan en casa. Así la escuela deja de ser un lugar donde solo se usa el castellano. En Ecuador, una dirección nacional de educación intercultural bilingüe existe desde 1988.",
"A raíz de la Constitución de 1992, el guaraní es lengua oficial de Paraguay junto al castellano. En Bolivia, la Constitución de 2009 declaró oficiales el castellano y las lenguas de los pueblos indígenas. Perú reconoce oficialmente 48 lenguas originarias, entre ellas el quechua y el aimara.",
"Hoy también ayuda la tecnología. Existen versiones de Wikipedia en quechua y en guaraní, y hay aplicaciones y cursos en línea para aprender estas lenguas.",
"Los lingüistas advierten, sin embargo, que la tecnología sola no basta. Hacen falta maestros que hablen la lengua, libros en esa lengua y familias que la usen en casa."]
wc(s,P)
story(s,"Lenguas originarias y escuela","Why many native languages have fewer speakers, how intercultural bilingual education and official-language laws in Ecuador, Paraguay, Bolivia and Peru respond, and what digital tools add.",P,[
 ("Why did many families stop passing on their language, according to linguists in the text?",["La escuela enseñó durante décadas solo en castellano.","Los niños no querían jugar.","No había papel."],0,"The first paragraph says so."),
 ("Since when is Guaraní an official language of Paraguay, according to the text?",["Desde la Constitución de 1992.","Desde 1500.","Desde 2024."],0,"The third paragraph says so."),
 ("What exists in Quechua and Guaraní, according to the text?",["Versiones de Wikipedia.","Aviones.","Bancos centrales."],0,"The fourth paragraph says so.")])

s='b2-pluralismo-05'
lesson(s,"Indigenous women and the defence of the land: leaders, courts and the Escazú Agreement","I can say what must be done, in a formal register, with *han de*, *has de* and other *haber de* + infinitive forms.")
grammar(s,"Must, Was to: Haber de + Infinitive",[
 {"type":"text","title":"What you already know","content":"You know *haber de* + infinitive from B2 Unit 26: a formal way to say a duty (*han de*, *he de*) and, in stories, *había de* or *habría de* for what was going to happen later. Agreements and rulings use it for what States must do, and it also fits the history of a struggle."},
 ex([("Los Estados han de proteger a las personas que defienden el territorio.","States must protect the people who defend the land."),
     ("Las comunidades han de ser consultadas antes de un proyecto.","Communities must be consulted before a project."),
     ("He de reconocer que la información es todavía limitada.","I must admit that the information is still limited."),
     ("Aquel caso habría de llegar al tribunal de Pastaza en 2019.","That case was to reach the court of Pastaza in 2019.")]),
 T("tip","*Haber de* changes with the person (*he de*, *has de*, *ha de*, *hemos de*, *han de*); *hay que* never does. Do not drop the *de*: not *los Estados han proteger*.")])
exercises(s,[
 mc(1,s,"grammar","perifrasis-haber-de-infinitivo","Which sentence means \"States must protect the people who defend the land\"?",
  ["Los Estados han de proteger a las personas que defienden el territorio.","Los Estados ha de proteger a las personas que defienden el territorio.","Los Estados han proteger a las personas que defienden el territorio."],0),
 fb(2,s,"perifrasis-haber-de-infinitivo","Las comunidades __ de ser consultadas antes de un proyecto.","han","Communities must be consulted before a project.",hint="haber, they"),
 mt(3,s,V,[("lideresa","woman leader"),("semilla","seed"),("defensor","defender"),("territorio","territory")]),
 mc(4,s,"reading","","When did the Escazú Agreement come into force, according to the text?",
  ["En 2021.","En 2018.","En 2016."],0)])
vocab(s,"Women and the land",[("lideresa","woman leader","noun"),("semilla","seed","noun"),("defensor","defender","noun"),("territorio","territory","noun")])
P=["En muchas comunidades indígenas, las mujeres cuidan las semillas, el agua y la memoria de la comunidad. Muchas son lideresas y defienden el territorio frente a proyectos mineros, petroleros o agrícolas.",
"En 1992, la guatemalteca Rigoberta Menchú, de origen maya k'iche', recibió el Premio Nobel de la Paz.",
"Según Global Witness, una organización que registra los asesinatos de personas defensoras del ambiente, América Latina es la región donde más defensores son asesinados. Uno de los casos más conocidos es el de Berta Cáceres, lideresa del pueblo lenca de Honduras y fundadora del COPINH, que recibió el Premio Ambiental Goldman en 2015. Fue asesinada en marzo de 2016; en 2018 un tribunal condenó a siete hombres, y en 2021 condenó también a un directivo de una empresa.",
"El Acuerdo de Escazú, adoptado en 2018 y vigente desde 2021, dice que los Estados han de proteger a las personas defensoras del ambiente y han de garantizar el acceso a la información ambiental.",
"En Ecuador, un grupo de mujeres de la nación waorani presentó un caso contra un plan de licitación de bloques petroleros en su territorio. En abril de 2019 un tribunal de Pastaza decidió a favor de los waorani, porque no se había hecho la consulta previa. Aquel caso habría de ser una referencia para otras comunidades."]
wc(s,P)
story(s,"Mujeres indígenas y defensa del territorio","Indigenous women as leaders: Rigoberta Menchú, Berta Cáceres, the Escazú Agreement on defenders of the environment and the Waorani court case of 2019 in Ecuador.",P,[
 ("To which people does Berta Cáceres belong, according to the text?",["Al pueblo lenca de Honduras.","Al pueblo maya de México.","Al pueblo guaraní de Paraguay."],0,"The third paragraph says so."),
 ("What does the Escazú Agreement say States must do, according to the text?",["Proteger a las personas defensoras del ambiente.","Cerrar las fronteras.","Vender el agua."],0,"The fourth paragraph says so."),
 ("Why did the court of Pastaza decide for the Waorani in 2019, according to the text?",["Porque no se había hecho la consulta previa.","Porque la empresa ganó.","Porque no había petróleo."],0,"The last paragraph says so.")])

s='b2-pluralismo-consolidation'
lesson(s,"Review: indigenous rights, nature and languages in Latin America","I can use contrast and cause connectors, relatives, value judgments and *haber de* to talk about indigenous rights.")
exercises(s,[
 mc(1,s,"grammar","formal-cause-connectors","Which sentence means \"As a result of the 2008 Constitution, Ecuador recognises the rights of nature\"?",
  ["A raíz de la Constitución de 2008, Ecuador reconoce los derechos de la naturaleza.","A raíz que la Constitución de 2008, Ecuador reconoce los derechos de la naturaleza.","A raíz a la Constitución de 2008, Ecuador reconoce los derechos de la naturaleza."],0),
 mc(2,s,"grammar","perifrasis-haber-de-infinitivo","Which sentence means \"Governments must consult indigenous peoples\"?",
  ["Los gobiernos han de consultar a los pueblos indígenas.","Los gobiernos ha de consultar a los pueblos indígenas.","Los gobiernos han consultar a los pueblos indígenas."],0),
 fb(3,s,"relativas-preposicion-el-que","La Constitución de 1991 es la norma en la __ Colombia reconoció la justicia indígena.","que","The 1991 Constitution is the rule in which Colombia recognised indigenous justice."),
 mc(4,s,"reading","","Which court declared the Atrato river a subject of rights in 2016, according to the lesson texts?",
  ["La Corte Constitucional de Colombia.","La Corte Constitucional de Ecuador.","El tribunal de Pastaza, en Ecuador."],0)])
