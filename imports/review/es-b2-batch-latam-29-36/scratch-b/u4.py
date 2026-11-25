import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-latin-america-global-vocab'
T=lambda t,c:{"type":t,"content":c}
def ex(items): return {"type":"examples","title":"In context","items":[{"spanish":a,"english":b} for a,b in items]}
def wc(stem,paras): print(stem,words(paras))

s='b2-futuro-01'
lesson(s,"Latin American cinema in the 21st century: Mexico, Argentina, Colombia, Chile and Brazil","I can make a guess about the present or the past with the future and the conditional of probability.")
grammar(s,"Probably: Guessing With the Future and the Conditional",[
 {"type":"text","title":"What you already know","content":"You know *estará* and *serían* from B1 Unit 22: the future can be a guess about the present (*Estará en casa*: \"He is probably at home\") and the conditional a guess about the past (*Serían las ocho cuando llegó el tren*: \"It was probably about eight\"). You use them when you do not know a fact and say what seems likely: when a film starts, how long it lasts, who is at the cinema."},
 ex([("Mi amiga no contesta; estará en el cine.","My friend is not answering; she is probably at the cinema."),
     ("No sé cuánto dura la película; durará unas dos horas.","I do not know how long the film is; it probably lasts about two hours."),
     ("Serán las nueve, porque ya hay mucha gente en la sala.","It is probably nine o'clock, because there are already many people in the theatre."),
     ("Serían las diez cuando terminó la película.","It was probably about ten when the film ended.")]),
 T("tip","Do not use these forms for facts you know. *Roma es de 2018* is a fact; *Roma será de 2018* would mean \"it is probably from 2018\". The conditional guesses about the past: use it with a past event, as in *Serían las diez cuando terminó*.")])
exercises(s,[
 mc(1,s,"grammar","future-probability","Which sentence means \"My friend is probably at the cinema\"?",
  ["Mi amiga estará en el cine.","Mi amiga está en el cine.","Mi amiga estuvo en el cine."],0,{1:"present-tense",2:"preterito-indefinido"}),
 fb(2,s,"future-probability","__ las diez cuando terminó la película.","Serían","It was probably about ten when the film ended."),
 mt(3,s,V,[("cineasta","filmmaker"),("rodaje","filming"),("estreno","first showing"),("guion","script")]),
 mc(4,s,"reading","","Which Brazilian film won the Oscar for best international film in 2025, according to the text?",
  ["Aún estoy aquí.","La forma del agua.","Pájaros de verano."],0)])
vocab(s,"Cinema",[("cineasta","filmmaker","noun"),("rodaje","filming","noun"),("estreno","first showing","noun"),("guion","script","noun")])
P=["En el siglo XXI, el cine latinoamericano ha ganado premios en los grandes festivales y en los Óscar. Estas películas se ven hoy en salas, en festivales y en plataformas digitales.",
"En México, tres directores han llegado a Hollywood sin dejar su país como tema. Alfonso Cuarón dirigió Roma (2018), que ganó el León de Oro en Venecia y tres Óscar en 2019. La película cuenta la vida de una empleada doméstica indígena en la Ciudad de México a comienzos de los años setenta, está filmada en blanco y negro y se inspira en la infancia del director. Guillermo del Toro ganó los Óscar a la mejor película y a la mejor dirección con La forma del agua, y Alejandro González Iñárritu ganó el de mejor película con Birdman en 2015.",
"En Argentina, Lucrecia Martel dirigió La ciénaga (2001) y La niña santa (2004), películas ambientadas en el norte del país, y en 2017 estrenó Zama, basada en la novela de Antonio Di Benedetto.",
"En Colombia, Ciro Guerra estrenó El abrazo de la serpiente en 2015, una película filmada en la Amazonía y hablada en varias lenguas, entre ellas lenguas indígenas. Fue candidata al Óscar a la mejor película extranjera. Con Cristina Gallego dirigió después Pájaros de verano, ambientada en La Guajira.",
"Chile ganó el Óscar a la mejor película extranjera en 2018 con Una mujer fantástica, de Sebastián Lelio. En marzo de 2025, Brasil ganó por primera vez el Óscar a la mejor película internacional con Aún estoy aquí, de Walter Salles."]
wc(s,P)
story(s,"El cine latinoamericano del siglo XXI","Latin American films and filmmakers that won major prizes in the 21st century: Cuarón, del Toro and González Iñárritu in Mexico, Martel in Argentina, Guerra in Colombia, and Oscar wins for Chile and Brazil.",P,[
 ("Where does Roma take place, according to the text?",["En la Ciudad de México.","En Buenos Aires.","En La Guajira."],0,"The second paragraph says so."),
 ("Which novel is Lucrecia Martel's Zama based on, according to the text?",["Una novela de Antonio Di Benedetto.","Una novela de García Márquez.","Una obra de teatro."],0,"The third paragraph says so."),
 ("Which film won the Oscar for Chile in 2018, according to the text?",["Una mujer fantástica.","La forma del agua.","Pájaros de verano."],0,"The last paragraph says so.")])

s='b2-futuro-02'
lesson(s,"New Latin American writers after the Boom: Argentina, Ecuador, Chile and Mexico","I can grant a point and then make my own, with *si bien* + indicative.")
grammar(s,"Although It Is True That: Si Bien and the Boom",[
 {"type":"text","title":"What you already know","content":"You know *si bien* \"although it is true that\" from B2 Unit 8. It is formal, it takes the indicative, and the clause that follows says what matters more. Literary history is full of contrasts: what the Boom was, and what came after it."},
 ex([("Si bien casi todos los autores del Boom eran hombres, hoy muchas escritoras tienen lectores en todo el mundo.","Although almost all the Boom authors were men, today many women writers have readers all over the world."),
     ("Mariana Enríquez, si bien escribe terror, habla de problemas reales de Argentina.","Mariana Enríquez, although she writes horror, speaks about real problems in Argentina."),
     ("Si bien Distancia de rescate es una novela corta, tuvo mucho éxito en el extranjero.","Although Distancia de rescate is a short novel, it was very successful abroad."),
     ("Si bien Zambra escribe sobre su infancia, no cuenta una autobiografía.","Although Zambra writes about his childhood, he does not tell an autobiography.")]),
 T("tip","*Si bien* goes at the start of the sentence or between commas, and it never takes *que*. For \"even if\" (a possibility) use *aunque* + subjunctive, not *si bien*.")])
exercises(s,[
 mc(1,s,"grammar","concesivas-si-bien","Which sentence means \"Although many Boom authors were men, today many women are read around the world\"?",
  ["Si bien muchos autores del Boom eran hombres, hoy leen a muchas mujeres en todo el mundo.","Si bien que muchos autores del Boom eran hombres, hoy leen a muchas mujeres en todo el mundo.","Si bien muchos autores del Boom fueran hombres, hoy leen a muchas mujeres en todo el mundo."],0),
 fb(2,s,"concesivas-si-bien","Si bien muchos autores del Boom __ hombres, hoy escriben muchas mujeres.","eran","Although many Boom authors were men, many women write today."),
 mt(3,s,V,[("escritora","woman writer"),("cuento","short story"),("editorial","publishing house"),("terror","horror")]),
 mc(4,s,"reading","","Which author wrote Distancia de rescate, according to the text?",
  ["Samanta Schweblin.","Mariana Enríquez.","Alejandro Zambra."],0)])
vocab(s,"Literature",[("escritora","woman writer","noun"),("cuento","short story","noun"),("editorial","publishing house","noun"),("terror","horror","noun")])
P=["En los años sesenta, el llamado Boom llevó la literatura latinoamericana a lectores de todo el mundo. Entre sus autores están Gabriel García Márquez, Mario Vargas Llosa, Carlos Fuentes y Julio Cortázar. García Márquez recibió el Premio Nobel de Literatura en 1982, y Vargas Llosa, en 2010. Si bien casi todos los autores del Boom eran hombres, hoy muchas escritoras tienen lectores en todo el mundo.",
"La argentina Mariana Enríquez escribe cuentos y novelas de terror situados en la Argentina actual. En Las cosas que perdimos en el fuego (2016) y Nuestra parte de noche (2019) aparecen la pobreza, la violencia y el recuerdo de la dictadura. La ecuatoriana Mónica Ojeda publicó Nefando (2016) y Mandíbula (2018), novelas de terror con adolescentes e internet.",
"La argentina Samanta Schweblin publicó Distancia de rescate en 2014 y Kentukis en 2018. La primera novela, en su traducción al inglés, fue finalista del Premio Booker Internacional en 2017. Kentukis trata de unos muñecos conectados a internet y de la intimidad.",
"El chileno Alejandro Zambra cuenta en Formas de volver a casa (2011) cómo se crece durante una dictadura, la de Pinochet. La mexicana Valeria Luiselli escribe ensayos y novelas sobre la vida en las ciudades y la migración.",
"Las editoriales independientes de la región publican hoy a muchos autores jóvenes, y algunos libros llegan a lectores de otros países por traducciones al inglés y a otras lenguas."]
wc(s,P)
story(s,"Escritoras y escritores después del Boom","After the Boom of the 1960s, new Latin American authors such as Mariana Enríquez, Mónica Ojeda, Samanta Schweblin, Alejandro Zambra and Valeria Luiselli write about violence, memory and daily life.",P,[
 ("When did García Márquez receive the Nobel Prize, according to the text?",["En 1982.","En 1960.","En 2010."],0,"The first paragraph says so."),
 ("What was Distancia de rescate in 2017, according to the text?",["Finalista del Premio Booker Internacional.","Una película de Cannes.","Una canción famosa."],0,"The third paragraph says so."),
 ("What does Zambra's Formas de volver a casa tell, according to the text?",["Cómo se crece durante una dictadura.","Cómo se viaja a la Luna.","Cómo se cocina una empanada."],0,"The fourth paragraph says so.")])

s='b2-futuro-03'
lesson(s,"Lithium, copper and the world economy: the Andean salt flats and the great powers","I can say what should be done about resources, with *es importante que* and *es necesario que* + subjunctive.")
grammar(s,"It Is Important That: What Should Be Done With Resources",[
 {"type":"text","title":"What you already know","content":"You know *es importante que*, *es necesario que* and *es mejor que* from A2 Unit 27: after a value judgment about what others should do, the verb after *que* is in the present subjunctive. Debates about lithium and copper use them constantly: who should take part in decisions, who should benefit, what should be protected."},
 ex([("Es importante que los países usen el agua con cuidado cuando extraen litio.","It is important that countries use water carefully when they extract lithium."),
     ("Es necesario que las comunidades participen en las decisiones sobre los salares.","It is necessary that communities take part in decisions about the salt flats."),
     ("Es mejor que una parte del valor se quede en la región.","It is better that part of the value stays in the region."),
     ("Es una lástima que se exporte casi todo sin transformar.","It is a pity that almost everything is exported without being processed.")]),
 T("tip","With a new subject, use *que* and the present subjunctive (*usen*, *participen*, *se quede*). With no new subject, the infinitive is enough: *Es importante usar el agua con cuidado*.")])
exercises(s,[
 mc(1,s,"grammar","subjunctive-value-judgments","Which sentence means \"It is necessary that communities take part in the decisions\"?",
  ["Es necesario que las comunidades participen en las decisiones.","Es necesario que las comunidades participan en las decisiones.","Es necesario las comunidades participen en las decisiones."],0,{1:"present-tense"}),
 fb(2,s,"subjunctive-value-judgments","Es importante que los países __ el agua con cuidado.","usen","It is important that countries use water carefully."),
 mt(3,s,V,[("litio","lithium"),("salar","salt flat"),("batería","battery"),("extracción","extraction")]),
 mc(4,s,"reading","","Which three countries make up the \"lithium triangle\", according to the text?",
  ["Bolivia, Argentina y Chile.","Perú, Ecuador y Colombia.","Brasil, Paraguay y Uruguay."],0)])
vocab(s,"Lithium and copper",[("litio","lithium","noun"),("salar","salt flat","noun"),("batería","battery","noun"),("extracción","extraction","noun")])
P=["El litio se usa en las baterías de los vehículos eléctricos y en el almacenamiento de energía. Según el Servicio Geológico de Estados Unidos, Bolivia, Argentina y Chile tienen más de la mitad de los recursos de litio conocidos en el mundo. Estos tres países forman el llamado «triángulo del litio», con los salares de Uyuni (Bolivia), Hombre Muerto y Olaroz (Argentina) y Atacama (Chile). Chile y Perú, además, están entre los mayores productores de cobre del mundo.",
"Cada país eligió su propio camino. En 2023 el gobierno de Chile presentó una estrategia nacional del litio con más participación del Estado. En Bolivia, la explotación está reservada a la empresa estatal Yacimientos de Litio Bolivianos (YLB). En Argentina, las provincias son dueñas de los recursos naturales y negocian con las empresas.",
"En los salares, la extracción del litio usa mucha agua en zonas muy secas. Comunidades indígenas de Argentina y Chile han pedido que se les consulte antes de los proyectos. Según varios analistas, es importante que los países usen el agua con cuidado y que los beneficios se compartan con las comunidades.",
"El litio y el cobre están en el centro de una competencia entre grandes economías. China es hoy el mayor socio comercial de Brasil, Chile y Perú. En enero de 2026 la Unión Europea y el Mercosur firmaron un acuerdo comercial, que se aplica de forma provisional desde mayo de 2026. Brasil es uno de los países fundadores de los BRICS, y en julio de 2025 fue sede de su cumbre en Río de Janeiro. En enero de 2026, según la prensa internacional, fuerzas de Estados Unidos capturaron al presidente venezolano Nicolás Maduro.",
"Varios analistas piden que la región no exporte solo minerales, sino que también fabrique productos con más valor, como baterías. Es necesario que esa discusión incluya a los gobiernos, a las empresas y a las comunidades, dicen."]
wc(s,P)
story(s,"Litio, cobre y poder económico","The lithium triangle of Bolivia, Argentina and Chile, the three national approaches, water and community consultation, and China, the EU–Mercosur agreement, BRICS and the US action in Venezuela in 2026, as reported.",P,[
 ("What is lithium used for, according to the text?",["Para baterías de vehículos eléctricos.","Para hacer pan.","Para construir puentes."],0,"The first paragraph says so."),
 ("Which state company controls lithium in Bolivia, according to the text?",["Yacimientos de Litio Bolivianos.","Petrobras.","Codelco."],0,"The second paragraph names YLB."),
 ("When did the EU and Mercosur sign an agreement, according to the text?",["En enero de 2026.","En marzo de 1991.","En abril de 2011."],0,"The fourth paragraph says so.")])

s='b2-futuro-04'
lesson(s,"Young people and social movements: Ni Una Menos, Chile 2019 and Colombia 2021","I can describe a movement, a place or a group with *en el que*, *con el que* and other relatives with a preposition.")
grammar(s,"The Country In Which, The Group With Which",[
 {"type":"text","title":"What you already know","content":"You know relative clauses with *el que* and a preposition from B1 Unit 20: the preposition goes before *el que*, *la que*, *los que* or *las que*, and the article matches the noun (*el edificio en el que vivimos*). They are the tool for describing movements: the country in which protests began, the group with which a song is linked."},
 ex([("Chile es el país en el que empezaron las protestas de 2019.","Chile is the country in which the 2019 protests began."),
     ("Ni Una Menos es el movimiento en el que participan muchas jóvenes.","Ni Una Menos is the movement in which many young women take part."),
     ("Las Tesis es el colectivo con el que se asocia la canción Un violador en tu camino.","Las Tesis is the group with which the song Un violador en tu camino is associated."),
     ("El pañuelo verde es el símbolo con el que se identifican muchas manifestantes.","The green scarf is the symbol with which many protesters identify.")]),
 T("tip","Keep the preposition that the verb needs (*participar en*, *asociar con*) and match the article to the noun: *el movimiento en el que*, *la marcha en la que*. Without the preposition the sentence is wrong: not *el país que empezaron las protestas*.")])
exercises(s,[
 mc(1,s,"grammar","relativas-preposicion-el-que","Which sentence means \"Chile is the country in which the 2019 protests began\"?",
  ["Chile es el país en el que empezaron las protestas de 2019.","Chile es el país que empezaron las protestas de 2019.","Chile es el país en la que empezaron las protestas de 2019."],0),
 fb(2,s,"relativas-preposicion-el-que","Ni Una Menos es el movimiento __ el que participan muchas jóvenes.","en","Ni Una Menos is the movement in which many young women take part."),
 mt(3,s,V,[("marcha","march"),("pañuelo","scarf"),("colectivo","group, collective"),("plebiscito","plebiscite")]),
 mc(4,s,"reading","","When did the large protests begin in Chile, according to the text?",
  ["En 2019.","En 2015.","En 2021."],0)])
vocab(s,"Movements",[("marcha","march","noun"),("pañuelo","scarf","noun"),("colectivo","group, collective","noun"),("plebiscito","plebiscite","noun")])
P=["En América Latina, una parte grande de la población es joven, y muchos jóvenes participan en la política con marchas, música y redes sociales.",
"El 3 de junio de 2015, una marcha en Argentina contra los asesinatos de mujeres dio origen al movimiento Ni Una Menos, que se extendió a otros países de la región. Las jóvenes que pedían el aborto legal usaron un pañuelo verde como símbolo. En diciembre de 2020 Argentina aprobó una ley que legalizó el aborto, y en 2022 la Corte Constitucional de Colombia lo despenalizó hasta la semana veinticuatro.",
"En Chile, las protestas de octubre de 2019 empezaron con estudiantes contra el aumento del precio del metro de Santiago y crecieron hasta ser protestas contra la desigualdad. En noviembre de 2019, en Valparaíso, el colectivo Las Tesis presentó la intervención Un violador en tu camino, que otros grupos repitieron en muchas ciudades del mundo. En 2020 los chilenos votaron en un plebiscito escribir una nueva constitución, pero en 2022 rechazaron el texto propuesto.",
"En Colombia, el paro nacional empezó el 28 de abril de 2021 contra un proyecto de reforma tributaria, que el gobierno retiró. Las protestas siguieron durante semanas, y el gobierno y las organizaciones de derechos humanos dieron cifras distintas sobre las víctimas.",
"Los jóvenes usan también el rap y otros géneros para contar su vida en los barrios. Las redes sociales les sirven para organizar marchas y para mostrar lo que pasa en la calle."]
wc(s,P)
story(s,"Jóvenes y movimientos sociales","Ni Una Menos in Argentina (2015), the protests in Chile in 2019 and the national strike in Colombia in 2021, with the role of music and social networks among young people.",P,[
 ("Where did Ni Una Menos begin, according to the text?",["En Argentina, en 2015.","En Chile, en 2019.","En Colombia, en 2021."],0,"The second paragraph says so."),
 ("What did the Chilean voters do in 2022, according to the text?",["Rechazaron el texto de la constitución propuesta.","Eligieron un presidente nuevo.","Cerraron la universidad."],0,"The third paragraph says so."),
 ("Against what did the Colombian strike start, according to the text?",["Contra un proyecto de reforma tributaria.","Contra un partido de fútbol.","Contra un festival de música."],0,"The fourth paragraph says so.")])

s='b2-futuro-05'
lesson(s,"What does it mean to be Latin American? Identity and Latin America in today's world","I can use a metaphor, a rhetorical question or repetition to make a point.")
grammar(s,"Metaphor, Question, Repetition: Making a Point",[
 {"type":"text","title":"What you already know","content":"You know *El tiempo es un río* from B2 Unit 36. Three devices are easy to spot: a metaphor says one thing *is* another, without *como* (*El tiempo es un río*); a rhetorical question is asked to make a point, not to get an answer (*¿Quién puede negar que los precios suben?*); repetition stresses an idea (*Trabajo, trabajo y más trabajo*). Writing about identity uses them all."},
 ex([("América Latina es un mosaico de lenguas y culturas.","Latin America is a mosaic of languages and cultures. (metaphor)"),
     ("¿Quién puede negar que la región es diversa?","Who can deny that the region is diverse? (rhetorical question)"),
     ("Lenguas, lenguas y más lenguas: así es el continente.","Languages, languages and more languages: that is the continent. (repetition)"),
     ("La región no es como un mosaico: es un mosaico.","The region is not like a mosaic: it is a mosaic. (the first half is a comparison, the second a metaphor)")]),
 T("tip","Use one device at a time. A sentence with *como* is a comparison, not a metaphor. A rhetorical question works best when the answer is obvious. If a plain sentence says it better, keep the plain sentence.")])
exercises(s,[
 mc(1,s,"grammar","rhetorical-devices","Which sentence is a metaphor, not a comparison?",
  ["América Latina es un mosaico de culturas.","América Latina es como un mosaico de culturas.","¿Quién puede negar que América Latina es diversa?"],0),
 fb(2,s,"rhetorical-devices","¿__ puede negar que la región es diversa?","Quién","Who can deny that the region is diverse?"),
 mt(3,s,V,[("mosaico","mosaic"),("mestizaje","mixing of peoples and cultures"),("herencia","heritage"),("voz","voice")]),
 mc(4,s,"reading","","Where was the COP30 held in November 2025, according to the text?",
  ["En Belém, en la Amazonía brasileña.","En Lima, en la costa del Pacífico.","En Quito, en los Andes."],0)])
vocab(s,"Identity",[("mosaico","mosaic","noun"),("mestizaje","mixing of peoples and cultures","noun"),("herencia","heritage","noun"),("voz","voice","noun")])
P=["¿Qué significa ser latinoamericano? No hay una sola respuesta. Más de seiscientos millones de personas viven en América Latina y el Caribe, y hablan español, portugués y también cientos de lenguas indígenas. La región es un mosaico, y ese mosaico tiene muchas herencias.",
"Entre esas herencias están los pueblos indígenas, que vivían en el continente antes de la llegada de los europeos; los millones de personas de origen africano que llegaron durante la esclavitud; los inmigrantes europeos y asiáticos de los siglos XIX y XX; y las migraciones de los últimos años. ¿Quién puede decir que hay una sola manera de ser latinoamericano?",
"La idea de una región unida tiene una historia larga. Simón Bolívar y otros líderes de la independencia hablaron de unir a los nuevos países, y esa idea todavía aparece en las discusiones sobre integración. Hoy los países de la región tienen caminos distintos y desacuerdos, pero también trabajan juntos en algunos temas.",
"El mundo mira hoy a la región por varias razones. En noviembre de 2025, Belém, una ciudad de la Amazonía brasileña, fue sede de la COP30, la conferencia de las Naciones Unidas sobre el clima. Según la estimación del INPE, la deforestación de la Amazonía brasileña entre agosto de 2025 y julio de 2026 fue de 3335 kilómetros cuadrados, la cifra más baja desde 1988, cuando empezaron los registros.",
"En política, el 25 de octubre de 2026 Luiz Inácio Lula da Silva ganó la segunda vuelta de las elecciones presidenciales de Brasil frente a Flávio Bolsonaro, y asumirá el cargo el 5 de enero de 2027. Mientras tanto, los jóvenes, los artistas, las escritoras y los científicos de la región siguen contando su propia historia: voces, voces y más voces que se oyen en el mundo."]
wc(s,P)
story(s,"¿Qué significa ser latinoamericano?","Latin America as a mosaic of peoples, languages and inheritances, the long idea of regional unity, and some dated facts from 2025 and 2026: the COP30 in Belém, Amazon deforestation figures and Brazil's election.",P,[
 ("How many people live in Latin America and the Caribbean, according to the text?",["Más de seiscientos millones.","Unos seis mil.","Cerca de cien."],0,"The first paragraph says so."),
 ("What did INPE estimate for August 2025 to July 2026, according to the text?",["3335 kilómetros cuadrados de deforestación, la cifra más baja desde 1988.","Más deforestación que nunca.","Ninguna deforestación."],0,"The fourth paragraph says so."),
 ("Who won the run-off of 25 October 2026 in Brazil, according to the text?",["Lula da Silva.","Flávio Bolsonaro.","Nicolás Maduro."],0,"The last paragraph says so.")])

s='b2-futuro-consolidation'
lesson(s,"Review: cinema, books, lithium, movements and identity in Latin America","I can use probability, *si bien*, value judgments, relatives and rhetorical devices to talk about Latin America today.")
exercises(s,[
 mc(1,s,"grammar","future-probability","Which sentence means \"The film was probably about two hours long\"?",
  ["Duraría unas dos horas.","Dura unas dos horas.","Duró unas dos horas."],0,{1:"present-tense",2:"preterito-indefinido"}),
 mc(2,s,"grammar","subjunctive-value-judgments","Which sentence means \"It is important that the money reaches the communities\"?",
  ["Es importante que el dinero llegue a las comunidades.","Es importante que el dinero llega a las comunidades.","Es importante el dinero llegue a las comunidades."],0,{1:"present-tense"}),
 fb(3,s,"relativas-preposicion-el-que","Brasil es el país en el __ se celebró la COP30.","que","Brazil is the country in which the COP30 was held."),
 mc(4,s,"reading","","Which country is a founding member of BRICS, according to the lesson texts?",
  ["Brasil.","Perú.","Chile."],0)])
