import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-uruguay-vocab'
def S(n): return f'b2-uruguay-{n}'
def I(n,k): return f'{S(n)}.ex{k:02d}'
def std(n,title,T,ex):
    exfile(S(n),ex); lesson(S(n),title,[f'ex0{k}' for k in range(1,7)],dlg=['ex05'])

# ---------- 01
n='01'
story(S(n),'El batllismo y el Estado laico','José Batlle y Ordóñez, president in 1903–1907 and 1911–1915, led reforms such as public companies, the eight-hour day and easier divorce, and the 1917 constitution separated Church and State.',[
"José Batlle y Ordóñez fue presidente de Uruguay de 1903 a 1907 y de 1911 a 1915. Su partido, el Colorado, impulsó reformas sociales y económicas que se conocen como batllismo.",
"En esos años el Estado creó empresas públicas, como el Banco de Seguros (1911) y la empresa estatal de electricidad (1912). En 1915 se aprobó la ley de ocho horas de trabajo. En 1907 se aprobó el divorcio, y una ley de 1913 permitió que la mujer pidiera el divorcio sin explicar sus razones.",
"La escuela pública, gratuita y obligatoria venía de antes: la reforma de José Pedro Varela es de 1877. En 1909 se eliminó la enseñanza religiosa obligatoria de las escuelas públicas. La Constitución aprobada en 1917 separó la Iglesia del Estado.",
"Por eso Uruguay es hoy un Estado laico. Un ejemplo son los nombres oficiales de algunas fiestas: la Navidad se llama «Día de la Familia» y la Semana Santa, «Semana de Turismo».",
"Muchos historiadores consideran que esas reformas ayudaron a crear una sociedad más igualitaria; otros recuerdan que sectores de la Iglesia y propietarios rurales las resistieron.",
],[
("When was Batlle president, according to the text?",["De 1903 a 1907 y de 1911 a 1915.","De 1877 a 1881.","Solo en el año 1917."],"The first paragraph gives both periods."),
("What did the law of 1913 allow?",["Que la mujer pidiera el divorcio sin explicar sus razones.","Que los obreros trabajaran más de ocho horas.","Que la Iglesia controlara las escuelas públicas."],"The second paragraph describes the law."),
("What happened in 1917, according to the text?",["Se aprobó una Constitución que separó la Iglesia del Estado.","Se creó el Banco de Seguros.","Se aprobó la ley de ocho horas de trabajo."],"The third paragraph says the constitution separated Church and State."),
])
grammar(S(n),'grammar.b2.uruguay.01.debido-a-batllismo','Reasons for Reforms: Debido a and A Raíz de',
"You know the formal cause connectors *debido a* and *a raíz de* from B1 Unit 6, and *porque* from A1. They give the reason or starting point of an event and take a noun. The reforms of Batlle and the Constitution of 1917 are good places to use them: each event led to the next.",
[["Debido a la ley de 1915, los obreros trabajaban ocho horas al día.","*debido a* + noun: because of"],["A raíz de la reforma de 1877, la escuela pública es gratuita y obligatoria.","*a raíz de* + noun: as a result of"],["Debido a la Constitución de 1917, la Iglesia y el Estado quedaron separados.","*debido a* + noun (*a* + *la*: no change)"],["La escuela pública es laica porque la ley lo establece.","*porque* + verb: a whole clause"]],
'Reason + result',
[("Debido a la ley de 1915, los obreros trabajaban ocho horas al día.","Because of the law of 1915, workers worked eight hours a day."),("A raíz de la reforma de 1877, la escuela pública es gratuita y obligatoria.","As a result of the reform of 1877, public school is free and compulsory."),("Debido a la Constitución de 1917, la Iglesia y el Estado quedaron separados.","Because of the Constitution of 1917, Church and State were separated."),("La escuela pública es laica porque la ley lo establece.","Public school is secular because the law says so.")],
"After *debido a* and *a raíz de* put a noun, never a verb: *debido a la ley*, not *debido a se aprobó la ley*. With a masculine noun, *a* + *el* becomes *al*: *debido al divorcio*. Use *porque* before a verb.")
vocab(S(n),'Batlle and the secular state',[('laico','secular, not religious','adjective'),('reforma','reform','noun'),('divorcio','divorce','noun'),('jornada','working day','noun'),('iglesia','church','noun'),('obligatorio','compulsory','adjective')])
T='formal-cause-connectors'
ex=[
mc(I(n,1),"Which sentence says that, because of the Constitution of 1917, the Church and the State were separated?",["Debido a la Constitución de 1917, la Iglesia y el Estado quedaron separados.","Debido de la Constitución de 1917, la Iglesia y el Estado quedaron separados.","Debido a se aprobó la Constitución de 1917, la Iglesia y el Estado quedaron separados."],0,T),
fb(I(n,2),"A __ de la reforma de Varela, la escuela pública es gratuita y obligatoria.","raíz","As a result of Varela's reform, public school is free and compulsory.",T),
sb(I(n,3),"Debido a la ley de 1915, los obreros trabajaban ocho horas al día.","Because of the law of 1915, workers worked eight hours a day.",T),
mt(I(n,4),[["laico","secular"],["el divorcio","divorce"],["la jornada","working day"],["la reforma","reform"]],V),
dc(I(n,5),[("Meg","¿Qué nombre tiene la Navidad en Uruguay?"),("Carlos","_____"),("Meg","Qué curioso, es un nombre laico.")],["Se llama «Día de la Familia».","Se llama «Día de la Playa».","Se llama «Semana de Turismo»."],0,V,cat='dialogue'),
rdg(I(n,6),"What does the text say about the law of 1913?",["La mujer podía pedir el divorcio sin dar razones.","El divorcio quedó prohibido en el país.","Solo los hombres podían pedir el divorcio."],0),
]
std(n,'Uruguay: Batlle, the reforms and the secular state',T,ex)

# ---------- 02
n='02'
story(S(n),'El candombe y las comparsas de Montevideo','Candombe, an Afro-Uruguayan drumming tradition of Montevideo, is played by comparsas in the Llamadas parade each February; UNESCO listed it in 2009.',[
"El candombe es una música y una danza de origen africano que se desarrolló en Montevideo entre los descendientes de las personas esclavizadas que llegaron al Río de la Plata en la época colonial. Se toca con tres tambores de distinto tamaño: el chico, que es el más agudo, el repique y el piano, que es el más grave. Antes de tocar, los tamborileros afinan los parches acercándolos al fuego.",
"Los grupos que tocan y bailan en la calle se llaman comparsas. Cada febrero, dentro del carnaval, las comparsas desfilan en las Llamadas por los barrios Sur y Palermo, y mucha gente sale a mirarlas.",
"En esos barrios había muchos conventillos, casas grandes donde vivían varias familias. Durante la dictadura, que duró de 1973 a 1985, muchos conventillos fueron demolidos y sus vecinos tuvieron que mudarse a la periferia. Uno de los más conocidos era el Medio Mundo, en la calle Cuareim.",
"En 2009 la UNESCO incluyó el candombe en su Lista Representativa del Patrimonio Cultural Inmaterial de la Humanidad, con el fin de ayudar a proteger la tradición. Hoy el candombe se toca en las calles de Montevideo durante todo el año, y no solo en las Llamadas.",
],[
("How many drums are used in candombe, according to the text?",["Tres tambores: el chico, el repique y el piano.","Un solo tambor grande.","Cinco guitarras y un tambor."],"The first paragraph lists the three drums."),
("What happens in the Llamadas?",["Las comparsas desfilan por los barrios Sur y Palermo.","Los vecinos demuelen los conventillos.","La UNESCO elige el mejor tambor."],"The second paragraph describes the parade."),
("What did UNESCO do in 2009?",["Incluyó el candombe en su lista del patrimonio inmaterial.","Eligió a Montevideo como capital del carnaval.","Prohibió tocar candombe en la calle."],"The last paragraph gives the UNESCO decision."),
])
grammar(S(n),'grammar.b2.uruguay.02.con-miras-a-candombe','Purpose: Con Miras A, Con Vistas A and Con el Fin de',
"You know *con el fin de* from B1 Unit 32 and the phrases of purpose *con miras a* and *con vistas a* (\"with a view to\") from B2 Unit 12. They name what you do something for, with an infinitive or a noun. The candombe tradition is full of that kind of thinking: people prepare and protect with a goal in mind.",
[["Las comparsas ensayan con miras a las Llamadas de febrero.","*con miras a* + noun: with a view to"],["Los tamborileros ensayan con vistas a desfilar en febrero.","*con vistas a* + infinitive: with a view to doing"],["La UNESCO incluyó el candombe con el fin de ayudar a protegerlo.","*con el fin de* + infinitive: in order to"],["Con miras al desfile, las comparsas afinan los tambores.","*con miras a* + *el* = *con miras al*"]],
'Purpose phrases',
[("Las comparsas ensayan con miras a las Llamadas de febrero.","The comparsas rehearse with the February Llamadas in view."),("Los tamborileros ensayan con vistas a desfilar en febrero.","The drummers rehearse with a view to marching in February."),("La UNESCO incluyó el candombe con el fin de ayudar a protegerlo.","UNESCO listed candombe in order to help protect it."),("Con miras al desfile, las comparsas afinan los tambores.","With the parade in view, the comparsas tune the drums.")],
"The preposition is always *a* after *miras* and *vistas*, and always *de* after *con el fin*: never *con el fin por* or *con miras en*. After *con el fin de* use an infinitive when the subject is the same. These phrases sound planned and a little formal; for simple purposes *para* is still the natural word.")
vocab(S(n),'Candombe, comparsas and Barrio Sur',[('candombe','Afro-Uruguayan drum music and dance','noun'),('comparsa','group that plays and dances in the street','noun'),('tamborilero','drummer','noun'),('conventillo','large old house where many families live','noun'),('tambor','drum','noun'),('llamada','parade of candombe drummers in February','noun')])
T='purpose-connectors'
ex=[
mc(I(n,1),"Which sentence says that UNESCO listed candombe in order to help protect it?",["La UNESCO incluyó el candombe con el fin de protegerlo.","La UNESCO incluyó el candombe con el fin de que protegerlo.","La UNESCO incluyó el candombe con el fin por protegerlo."],0,T),
fb(I(n,2),"Las comparsas ensayan con miras __ las Llamadas de febrero.","a","The comparsas rehearse with the February Llamadas in view.",T),
sb(I(n,3),"Los tamborileros ensayan con vistas a desfilar en febrero.","The drummers rehearse with a view to marching in February.",T),
mt(I(n,4),[["el candombe","Afro-Uruguayan drum music"],["la comparsa","group that plays and dances"],["el tamborilero","drummer"],["el conventillo","large house for many families"]],V),
dc(I(n,5),[("Meg","¿Qué son las Llamadas de febrero?"),("Carlos","_____"),("Meg","Me gustaría ver ese desfile algún día.")],["Son los desfiles de comparsas por los barrios Sur y Palermo.","Son las casas grandes donde vivían varias familias.","Son los tambores más graves del candombe."],0,V,cat='dialogue'),
rdg(I(n,6),"Which drums does the text name?",["El chico, el repique y el piano.","El chico, el repique y la guitarra.","El bombo, el piano y la guitarra."],0),
]
std(n,'Uruguay: candombe, comparsas and the Barrio Sur',T,ex)

# ---------- 03
n='03'
story(S(n),'La dictadura uruguaya y el plebiscito de 1980','After the coup of 1973 Uruguay lived under a civic-military dictatorship until 1985; in 1980 voters rejected the military constitution in a plebiscite, and civilian rule returned after the 1984 elections.',[
"En 1973 Uruguay tenía un presidente elegido, Juan María Bordaberry. El 27 de junio de 1973 Bordaberry, con el apoyo de las fuerzas armadas, disolvió el Parlamento. Los sindicatos respondieron con una huelga general que duró unos quince días. La dictadura cívico-militar duró hasta 1985. Durante esos años se prohibieron partidos y sindicatos, hubo censura, miles de personas fueron presas por motivos políticos y otras salieron del país.",
"En 1980 los militares quisieron aprobar una nueva Constitución mediante un plebiscito. El 30 de noviembre de 1980 votaron los ciudadanos y ganó el «No», con cerca del 57 % de los votos. Fue un resultado importante, porque el gobierno controlaba los medios de comunicación y la oposición tenía poco acceso a ellos.",
"Después del plebiscito, los militares y los partidos negociaron una salida. En noviembre de 1984 hubo elecciones, y el 1 de marzo de 1985 asumió como presidente Julio María Sanguinetti.",
"En 1986 el Parlamento aprobó la ley de caducidad, que limitó los juicios contra militares y policías por delitos de la dictadura; en 1989 un referéndum mantuvo esa ley. Desde 1996, cada 20 de mayo se hace en Montevideo la Marcha del Silencio en memoria de las personas desaparecidas.",
],[
("What happened on 27 June 1973?",["El presidente disolvió el Parlamento con el apoyo de las fuerzas armadas.","Los uruguayos votaron en un plebiscito.","Sanguinetti asumió la presidencia."],"The first paragraph describes the coup."),
("What was the result of the plebiscite of 30 November 1980?",["Ganó el «No», con cerca del 57 % de los votos.","Ganó el «Sí», con cerca del 57 % de los votos.","El plebiscito no se hizo."],"The second paragraph gives the result."),
("What happened on 1 March 1985?",["Julio María Sanguinetti asumió como presidente.","Bordaberry disolvió el Parlamento.","Los militares aprobaron una Constitución."],"The third paragraph gives the date."),
])
grammar(S(n),'grammar.b2.uruguay.03.mediante-plebiscito','By Means of: Mediante',
"You know the formal prepositional phrase *mediante* (\"by means of\") from B1 Unit 24: *Mediante este sistema, se reduce el consumo de energía*. A noun follows it directly. In political history it is useful to say how something was done: by a vote, by a strike, by a law.",
[["Los militares quisieron aprobar una Constitución mediante un plebiscito.","*mediante* + noun: by means of a plebiscite"],["Los uruguayos expresaron su rechazo mediante el voto.","*mediante el voto*: by voting"],["En 1984 volvió el gobierno civil mediante elecciones.","*mediante elecciones*: by elections"],["El gobierno militar controlaba la información mediante la censura.","*mediante la censura*: by censorship"]],
'Mediante + noun',
[("Los militares quisieron aprobar una Constitución mediante un plebiscito.","The military wanted to approve a constitution by means of a plebiscite."),("Los uruguayos expresaron su rechazo mediante el voto.","Uruguayans expressed their rejection by voting."),("En 1984 volvió el gobierno civil mediante elecciones.","In 1984 civilian government returned by means of elections."),("El gobierno militar controlaba la información mediante la censura.","The military government controlled information by means of censorship.")],
"*Mediante* is followed by a noun, never by *de* (*mediante de*) or by a verb. It is formal: in everyday Spanish you say *con* or *por* (*con el voto*). It often opens the sentence, followed by a comma: *Mediante el voto, los uruguayos…*.")
vocab(S(n),'Dictatorship and plebiscite',[('plebiscito','plebiscite, vote on a proposal','noun'),('huelga','strike','noun'),('parlamento','parliament','noun'),('censura','censorship','noun'),('preso','prisoner','noun'),('rechazo','rejection','noun')])
T='prepositional-phrases'
ex=[
mc(I(n,1),"Which sentence says that the military government controlled information by means of censorship?",["El gobierno militar controlaba la información mediante la censura.","El gobierno militar controlaba la información mediante de la censura.","El gobierno militar controlaba la información por mediante la censura."],0,T),
fb(I(n,2),"Los militares quisieron aprobar una Constitución __ un plebiscito.","mediante","The military wanted to approve a constitution by means of a plebiscite.",T),
sb(I(n,3),"Los uruguayos expresaron su rechazo mediante el voto.","Uruguayans expressed their rejection by voting.",T),
mt(I(n,4),[["el plebiscito","vote on a proposal"],["la huelga","strike"],["el parlamento","parliament"],["el preso","prisoner"]],V),
dc(I(n,5),[("Meg","¿Qué pasó el 27 de junio de 1973 en Uruguay?"),("Carlos","_____"),("Meg","Entonces empezó la dictadura.")],["El presidente disolvió el Parlamento con el apoyo de los militares.","Los militares aceptaron un plebiscito sobre una Constitución nueva.","Julio María Sanguinetti asumió como presidente de Uruguay."],0,V,cat='dialogue'),
rdg(I(n,6),"What does the text say about the years of the dictatorship?",["Miles de personas fueron presas por motivos políticos.","Los sindicatos pudieron hacer huelgas con libertad.","La censura no existió durante esos años."],0),
]
std(n,'Uruguay: the dictatorship and the plebiscite of 1980',T,ex)

# ---------- 04
n='04'
story(S(n),'Derechos, energía y escuela: un Uruguay de leyes nuevas','In 2012–2013 Uruguay passed laws on abortion, same-sex marriage and cannabis; it invested in renewable electricity after a 2010 cross-party agreement and began the Plan Ceibal in 2007.',[
"Entre 2012 y 2013 el Parlamento uruguayo aprobó tres leyes que se discutieron mucho dentro y fuera del país. En 2012 se aprobó una ley que permite interrumpir el embarazo dentro de las primeras doce semanas, con un proceso previo de consulta. En abril de 2013 se aprobó el matrimonio entre personas del mismo sexo. En diciembre de 2013 se aprobó una ley que regula la producción, la venta y el consumo de cannabis; según muchos medios, Uruguay fue el primer país del mundo en hacerlo. Las tres leyes tuvieron apoyo y también oposición.",
"En 2010 los partidos políticos firmaron un acuerdo sobre la política energética. Después de la energía hidráulica, el país pasó a invertir en energía eólica, solar y de biomasa. En la mayoría de los años recientes, más del 90 % de la electricidad se generó con fuentes renovables, aunque la cifra cambia según las lluvias.",
"En 2007 comenzó el Plan Ceibal: Uruguay fue uno de los primeros países en dar una computadora a cada alumno de las escuelas públicas. Con el tiempo, el plan pasó a incluir también a los alumnos de secundaria.",
"Desde el 1 de marzo de 2025 el presidente de Uruguay es Yamandú Orsi, del Frente Amplio.",
],[
("When was the law on same-sex marriage approved, according to the text?",["En abril de 2013.","En 2007.","En marzo de 2025."],"The first paragraph gives the date."),
("What does the text say about Uruguay's electricity?",["En la mayoría de los años recientes, más del 90 % salió de fuentes renovables.","Casi toda viene del petróleo importado.","Uruguay no produce nada de electricidad."],"The second paragraph gives the dated figure."),
("What did the Plan Ceibal do, according to the text?",["Dio una computadora a cada alumno de las escuelas públicas.","Reguló el consumo de cannabis.","Firmó un acuerdo sobre la política energética."],"The third paragraph describes the plan."),
])
grammar(S(n),'grammar.b2.uruguay.04.pasar-a-leyes-energia','Moving On: Pasar A',
"You know *pasar a* + infinitive from B2 Unit 23: it means to move on to the next step, after something came before (*Ahora pasemos a ver los resultados*). It fits the story of Uruguay's recent changes, where one project led to the next one: first hydroelectric power, then wind; first primary school, then secondary.",
[["Después de la energía hidráulica, el país pasó a invertir en energía eólica.","*pasó a invertir*: went on to invest"],["Con el tiempo, el plan pasó a incluir a los alumnos de secundaria.","*pasó a incluir*: went on to include"],["Ahora pasemos a hablar de la energía renovable.","*pasemos a hablar*: let us move on to talking"],["Primero se aprobó la ley; después, el Parlamento pasó a discutir otra.","a first step, then *pasó a discutir*"]],
'Pasar a + infinitive',
[("Después de la energía hidráulica, el país pasó a invertir en energía eólica.","After hydroelectric power, the country went on to invest in wind power."),("Con el tiempo, el plan pasó a incluir a los alumnos de secundaria.","In time, the plan went on to include secondary students."),("Ahora pasemos a hablar de la energía renovable.","Now let us move on to talking about renewable energy."),("Primero se aprobó la ley; después, el Parlamento pasó a discutir otra.","First the law was passed; then Parliament moved on to discuss another.")],
"*Pasar a* needs an earlier step to move on from, and always has *a* + infinitive. If nothing came before, use *empezar a*. It does not mean \"to pass\" or \"to go by\" here. With *ser* it says what something became: *pasó a ser*.")
vocab(S(n),'New laws, green energy and the Plan Ceibal',[('matrimonio','marriage','noun'),('cannabis','cannabis','noun'),('eólico','wind (energy)','adjective'),('renovable','renewable','adjective'),('computadora','computer','noun'),('alumno','pupil, student','noun')])
T='perifrasis-pasar-a'
ex=[
mc(I(n,1),"Which sentence says that the plan later moved on to include secondary school students?",["Con el tiempo, el plan pasó a incluir a los alumnos de secundaria.","Con el tiempo, el plan pasó incluir a los alumnos de secundaria.","Con el tiempo, el plan pasó en incluir a los alumnos de secundaria."],0,T),
fb(I(n,2),"Después de la energía hidráulica, el país pasó __ invertir en energía eólica.","a","After hydroelectric power, the country went on to invest in wind power.",T),
sb(I(n,3),"Ahora pasemos a hablar de la energía renovable.","Now let us move on to talking about renewable energy.",T),
mt(I(n,4),[["el matrimonio","marriage"],["la computadora","computer"],["eólico","wind (energy)"],["renovable","renewable"]],V),
dc(I(n,5),[("Meg","¿Qué es el Plan Ceibal?"),("Carlos","_____"),("Meg","Es una idea interesante para las escuelas.")],["Un plan que da una computadora a los alumnos desde 2007.","Una ley de 2013 que regula el consumo de cannabis.","Un acuerdo entre políticos para invertir en energía eólica."],0,V,cat='dialogue'),
rdg(I(n,6),"What does the text say about electricity in Uruguay?",["En varios años recientes, más del 90 % venía de fuentes renovables.","En varios años recientes, casi toda venía del petróleo importado.","En varios años recientes, el país compró casi toda a sus vecinos."],0),
]
std(n,'Uruguay: new rights, green energy and the Plan Ceibal',T,ex)

# ---------- 05
n='05'
story(S(n),'Montevideo: la rambla, el mate y las murgas','Montevideo life is shown through its coastal promenade, the habit of mate, its name "oriental", and the carnival murgas that sing about politics and society on neighbourhood stages.',[
"Montevideo está en la costa del Río de la Plata. La rambla, el paseo que recorre la costa de la ciudad, es un lugar de encuentro para muchos montevideanos: por la tarde la gente pasea, hace deporte o se sienta a mirar el río.",
"Muchos uruguayos llevan el termo bajo el brazo para cebar el mate durante el día. Según distintas estimaciones, los uruguayos están entre los mayores consumidores de mate del mundo. Es habitual que un grupo comparta un solo mate, que pasa de mano en mano.",
"El nombre oficial del país es República Oriental del Uruguay, y algunos uruguayos se llaman a sí mismos «orientales». La palabra viene de la Banda Oriental, el territorio al este del río Uruguay.",
"Cada año, entre enero y febrero, hay carnaval. Según se suele decir, es uno de los más largos del mundo, porque dura más de un mes. En los tablados, escenarios al aire libre de los barrios, actúan las murgas: grupos de cantantes que, con canciones llamadas cuplés, hablan con humor de la vida política y social. En el carnaval también desfilan las comparsas de candombe.",
"Los visitantes se acostumbran pronto a ver gente con un termo en la rambla y a escuchar murgas en los barrios.",
],[
("What is the rambla, according to the text?",["Un paseo que recorre la costa de la ciudad.","Un escenario al aire libre de un barrio.","Un recipiente para llevar agua caliente."],"The first paragraph defines it."),
("What do many Uruguayans carry during the day?",["Un termo para cebar el mate.","Un tambor de candombe.","Una computadora de la escuela."],"The second paragraph describes the habit."),
("What do the murgas do, according to the text?",["Cantan con humor sobre la vida política y social.","Desfilan solo en las Llamadas de febrero.","Venden mate en la rambla."],"The fourth paragraph describes the murgas."),
])
grammar(S(n),'grammar.b2.uruguay.05.acostumbrarse-a-rambla','Fixed Prepositions: Acostumbrarse A, Darse Cuenta De',
"You know *darse cuenta de* from B1 Unit 29: many verbs need a fixed preposition, like *acostumbrarse a*, *adaptarse a*, *empezar a* + infinitive and *darse cuenta de*. Visitors to Montevideo use them all: they get used to the mate, they notice the thermos, they adapt to the rhythm of the rambla.",
[["Los visitantes se acostumbran pronto a ver gente con un termo.","*acostumbrarse a* + infinitive or noun"],["Muchos montevideanos empiezan a cebar el mate por la mañana.","*empezar a* + infinitive"],["Un turista se da cuenta de que casi todos llevan un termo.","*darse cuenta de* + noun or *que* clause"],["Los visitantes se adaptan a la tranquilidad de la rambla.","*adaptarse a* + noun"]],
'Verb + preposition',
[("Los visitantes se acostumbran pronto a ver gente con un termo.","Visitors soon get used to seeing people with a thermos."),("Muchos montevideanos empiezan a cebar el mate por la mañana.","Many people in Montevideo begin to prepare mate in the morning."),("Un turista se da cuenta de que casi todos llevan un termo.","A tourist realises that almost everyone carries a thermos."),("Los visitantes se adaptan a la tranquilidad de la rambla.","Visitors adapt to the calm of the rambla.")],
"Learn each verb together with its preposition and do not copy the English one: *acostumbrarse a*, *adaptarse a*, *empezar a*, *darse cuenta de*. The preposition stays the same before a noun, an infinitive or a *que* clause: *darse cuenta de* + *que* becomes *de que*.")
vocab(S(n),'Montevideo: rambla, mate and murga',[('rambla','coastal promenade','noun'),('termo','thermos flask','noun'),('mate','mate (herbal drink)','noun'),('cebar','to prepare and serve mate','verb'),('murga','carnival group that sings with humour about society','noun'),('tablado','open-air stage','noun')])
T='verbos-regimen-preposicional'
ex=[
mc(I(n,1),"Which sentence says that visitors soon get used to seeing people with a thermos?",["Los visitantes se acostumbran pronto a ver gente con un termo.","Los visitantes se acostumbran pronto de ver gente con un termo.","Los visitantes se acostumbran pronto en ver gente con un termo."],0,T),
fb(I(n,2),"Un turista se da __ de que casi todos llevan un termo.","cuenta","A tourist realises that almost everyone carries a thermos.",T),
sb(I(n,3),"Muchos montevideanos empiezan a cebar el mate por la mañana.","Many people in Montevideo begin to prepare mate in the morning.",T),
mt(I(n,4),[["la rambla","coastal promenade"],["el termo","thermos flask"],["el tablado","open-air stage"],["la murga","carnival group that sings about society"]],V),
dc(I(n,5),[("Meg","¿Qué es un tablado?"),("Carlos","_____"),("Meg","Entiendo cómo funciona el carnaval.")],["Un escenario al aire libre de un barrio donde actúan las murgas.","Un termo donde se lleva el agua caliente del mate.","Un paseo que recorre la costa de la ciudad."],0,V,cat='dialogue'),
rdg(I(n,6),"What is a murga, according to the text?",["Un grupo que canta sobre la vida política.","Un paseo que recorre toda la costa.","Una bebida que pasa de mano en mano."],0),
]
std(n,'Uruguay: Montevideo, the rambla, mate and murgas',T,ex)

# ---------- consolidation
n='consolidation'
ex=[
mc(I(n,1),"Which sentence says that, because of the reform of Varela, public school is free?",["Debido a la reforma de Varela, la escuela pública es gratuita.","Debido la reforma de Varela, la escuela pública es gratuita.","Debido a fue la reforma de Varela, la escuela pública es gratuita."],0,'formal-cause-connectors'),
fb(I(n,2),"El gobierno aprobó la ley con miras __ las elecciones de noviembre.","a","The government passed the law with the November elections in view.",'purpose-connectors'),
mc(I(n,3),"Which sentence says that the citizens elected the president by means of an election?",["Los ciudadanos eligieron al presidente mediante elecciones.","Los ciudadanos eligieron al presidente mediante de elecciones.","Los ciudadanos eligieron al presidente por mediante elecciones."],0,'prepositional-phrases'),
fb(I(n,4),"Después del primer año, el plan pasó __ incluir más escuelas.","a","After the first year, the plan went on to include more schools.",'perifrasis-pasar-a'),
mc(I(n,5),"Which sentence says that a visitor realises that mate is everywhere?",["Un visitante se da cuenta de que el mate está en todas partes.","Un visitante se da cuenta que el mate está en todas partes.","Un visitante se da cuenta en que el mate está en todas partes."],0,'verbos-regimen-preposicional'),
mt(I(n,6),[["el candombe","Afro-Uruguayan drum music"],["el plebiscito","vote on a proposal"],["el termo","thermos flask"],["el divorcio","divorce"]],V),
rdg(I(n,7),"According to the readings of this unit, what did the Constitution approved in 1917 do?",["Separó la Iglesia del Estado.","Disolvió el Parlamento.","Creó el Plan Ceibal."],0),
sb(I(n,8),"Los uruguayos rechazaron la Constitución de los militares en 1980.","Uruguayans rejected the military's constitution in 1980.",V),
]
exfile(S(n),ex)
d=rd('lessons/b2/b2-uruguay-consolidation.json')
d['title']='Uruguay: review of reforms, candombe, the dictatorship and Montevideo'
for s in d['sections']:
    if s['type']=='goal': s['items']=["I can review cause connectors, purpose phrases, *mediante*, *pasar a* and fixed prepositions on Uruguayan topics.","I can use the words for Batlle's reforms, candombe, the dictatorship, new laws and Montevideo life.","I can read about Uruguay and answer questions about what the texts say."]
    if s['type']=='checklist': s['items']=["I can say how something was done in politics with *mediante*.","I can give reasons for the reforms of the 1900s with *debido a* and *a raíz de*.","I can say what a tradition or a decision is for with *con miras a* and *con el fin de*.","I can say what a policy went on to include with *pasar a* + infinitive.","I can describe getting used to life in Montevideo with *acostumbrarse a* and *darse cuenta de*."]
wr('lessons/b2/b2-uruguay-consolidation.json',d)
