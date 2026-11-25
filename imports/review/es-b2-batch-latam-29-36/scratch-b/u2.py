import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-south-american-migration-vocab'
T=lambda t,c:{"type":t,"content":c}
def ex(items): return {"type":"examples","title":"In context","items":[{"spanish":a,"english":b} for a,b in items]}
def wc(stem,paras): print(stem,words(paras))

# ---- 01
s='b2-migracion-01'
lesson(s,"Waves of migration in South America: from Europe to the cities","I can say when something will happen, with *cuando*, *en cuanto* and *hasta que* + subjunctive.")
grammar(s,"When It Happens: Time Clauses and the Subjunctive",[
 {"type":"text","title":"What you already know","content":"You know *cuando*, *en cuanto* and *hasta que* from A2 Unit 27. For a habit or a past fact they take the indicative (*cuando llegó*, *cuando termina*). For something that has not happened yet they take the present subjunctive (*cuando termine*). The history of migration has both: the arrivals of the past and the plans of today."},
 ex([("Cuando llegó el barco a Buenos Aires, muchos inmigrantes buscaron trabajo en el puerto.","When the ship reached Buenos Aires, many immigrants looked for work at the port."),
     ("Muchos trabajadores del campo van a la ciudad cuando termina la cosecha.","Many farm workers go to the city when the harvest ends."),
     ("Cuando termine la cosecha, los trabajadores irán a la ciudad.","When the harvest ends, the workers will go to the city."),
     ("En cuanto lleguen a la ciudad, buscarán trabajo.","As soon as they arrive in the city, they will look for work.")]),
 T("tip","Ask yourself: has it happened yet? Past or habit: indicative (*llegó*, *termina*). Not yet: present subjunctive (*llegue*, *termine*), even when English says \"will\" or uses the present.")])
exercises(s,[
 mc(1,s,"grammar","cuando-subjuntivo","Which sentence means \"When the harvest ends, the workers will go to the city\"?",
  ["Cuando termine la cosecha, los trabajadores irán a la ciudad.","Cuando termina la cosecha, los trabajadores irán a la ciudad.","Cuando terminó la cosecha, los trabajadores irán a la ciudad."],0,{1:"present-tense",2:"preterito-indefinido"}),
 fb(2,s,"cuando-subjuntivo","En cuanto los migrantes __ a la ciudad, buscarán trabajo.","lleguen","As soon as the migrants arrive in the city, they will look for work."),
 mt(3,s,V,[("inmigrante","immigrant"),("oleada","wave"),("éxodo rural","move from the countryside to the cities"),("asentarse","to settle")]),
 mc(4,s,"reading","","Where did many European immigrants go between the middle of the 19th century and the early 20th, according to the text?",
  ["A Argentina, Uruguay y Brasil.","A México, Cuba y Costa Rica.","A Perú, Ecuador y Bolivia."],0)])
vocab(s,"Migration waves",[("inmigrante","immigrant","noun"),("oleada","wave","noun"),("éxodo rural","move from the countryside to the cities","expression"),("asentarse","to settle","verb")])
P=["Según los historiadores, entre mediados del siglo XIX y comienzos del XX llegaron a Argentina, Uruguay y Brasil varios millones de europeos, sobre todo italianos y españoles. La Constitución argentina de 1853 favorecía la inmigración europea. Cuando llegaba un barco al puerto de Buenos Aires, muchos inmigrantes buscaban trabajo en la ciudad o en el campo.",
"En 1908 llegó a Brasil el barco Kasato Maru, con los primeros inmigrantes japoneses, que trabajaron al principio en las plantaciones de café.",
"En el siglo XX, muchas personas dejaron el campo para vivir en las grandes ciudades, como São Paulo o Buenos Aires. En Brasil, muchos habitantes del nordeste se fueron al sudeste, donde estaban las fábricas. Muchos trabajadores del campo van a la ciudad cuando termina la cosecha, y vuelven en cuanto empieza un nuevo ciclo de trabajo.",
"Más tarde, el sentido de la migración cambió. En los años setenta, por ejemplo, muchos colombianos fueron a Venezuela, que tenía ingresos del petróleo, y muchos paraguayos y bolivianos fueron a Argentina. En varios países, en esa misma época, también hubo personas que salieron por motivos políticos durante las dictaduras.",
"Hoy los países de la región reciben migrantes de otros países de la región, y muchos sudamericanos viven en Estados Unidos o en España. Muchas familias mantienen lazos entre dos países: cuando llegan las fiestas, algunos emigrantes envían dinero o regresan de visita."]
wc(s,P)
story(s,"Oleadas de migración en Sudamérica","South American migration moved from European arrivals in the 19th and early 20th centuries, through the move from the countryside to the cities, to movement between countries of the region and emigration abroad.",P,[
 ("Which ship brought the first Japanese immigrants to Brazil in 1908, according to the text?",["El Kasato Maru.","El Titanic.","El Santa María."],0,"The second paragraph names the ship."),
 ("Where did many Colombians go in the 1970s, according to the text?",["A Venezuela.","A Chile.","A Paraguay."],0,"The fourth paragraph says so."),
 ("What do many farm workers do when the harvest ends, according to the text?",["Van a la ciudad.","Compran un barco.","Estudian en Europa."],0,"The third paragraph says so.")])

# ---- 02
s='b2-migracion-02'
lesson(s,"The Venezuelan exodus: how the region responded","I can say what governments and aid agencies should do, with *es necesario que* and *es importante que* + subjunctive.")
grammar(s,"It Is Necessary That: What the Region Should Do",[
 {"type":"text","title":"What you already know","content":"You know *es necesario que*, *es importante que* and *es mejor que* from A2 Unit 27. After a value judgment about what others should do, the verb after *que* is in the present subjunctive. Debates about refugees and migration use them all the time: what governments, border offices and schools should provide."},
 ex([("Es necesario que los países den documentos a las personas que llegan.","It is necessary that countries give papers to the people who arrive."),
     ("Es importante que los niños migrantes vayan a la escuela.","It is important that migrant children go to school."),
     ("Es mejor que los trámites sean claros y rápidos.","It is better that the paperwork is clear and quick."),
     ("Es una lástima que haya tantas familias sin ayuda.","It is a pity that so many families are without help.")]),
 T("tip","When the idea is general, use the infinitive: *Es importante dar documentos*. When it names who should do it, use *que* and the subjunctive: *Es importante que los países den documentos*.")])
exercises(s,[
 mc(1,s,"grammar","subjunctive-value-judgments","Which sentence means \"It is necessary that the countries give papers to the people who arrive\"?",
  ["Es necesario que los países den documentos a las personas que llegan.","Es necesario que los países dan documentos a las personas que llegan.","Es necesario los países den documentos a las personas que llegan."],0,{1:"present-tense"}),
 fb(2,s,"subjunctive-value-judgments","Es importante que los niños migrantes __ a la escuela.","vayan","It is important that migrant children go to school."),
 mt(3,s,V,[("albergue","shelter"),("permiso","permit"),("solicitud","application"),("menor","child, minor")]),
 mc(4,s,"reading","","What did Colombia create in February 2021, according to the text?",
  ["Un estatuto temporal para venezolanos.","Una frontera nueva con Venezuela.","Un puente entre Colombia y Brasil."],0)])
vocab(s,"Shelter and papers",[("albergue","shelter","noun"),("permiso","permit","noun"),("solicitud","application","noun"),("menor","child, minor","noun")])
P=["Según ACNUR, la agencia de la ONU para los refugiados, a finales de 2025 había unos 7,9 millones de venezolanos fuera de su país. La mayor parte se quedó en América Latina y el Caribe. Las causas de la salida se discuten: el gobierno venezolano culpa a las sanciones, y sus críticos culpan a la política económica.",
"En septiembre de 2018, varios gobiernos de la región empezaron en Quito un proceso para coordinar su respuesta, el Proceso de Quito. Cada país eligió sus propias medidas. Perú creó en 2017 un permiso temporal de permanencia, y Ecuador abrió en 2019 una visa de excepción por razones humanitarias. Brasil organizó desde 2018 la Operación Acogida, que ayuda a las personas que entran por el estado de Roraima y las lleva a otras ciudades.",
"En febrero de 2021 Colombia creó el Estatuto Temporal de Protección para Migrantes Venezolanos, que permite a muchas personas vivir y trabajar legalmente en el país durante diez años. Según R4V, la plataforma de la ONU y otras organizaciones, en 2026 Colombia acoge a unos dos millones y medio de venezolanos.",
"Organizaciones humanitarias han pedido que los niños migrantes puedan ir a la escuela y que las familias reciban ayuda en albergues cuando llegan. Es importante que los niños sigan estudiando, dicen, aunque la familia no tenga todavía sus documentos.",
"Los gobiernos que reciben a más personas han pedido más apoyo internacional. Es necesario que ese apoyo llegue, según ACNUR, para que los servicios de salud y de educación puedan atender a más personas."]
wc(s,P)
story(s,"La respuesta de la región al éxodo venezolano","About 7.9 million Venezuelans were abroad at the end of 2025, according to UNHCR; the text covers the Quito Process, national permits in Peru, Ecuador, Brazil and Colombia, and calls for schooling and international support.",P,[
 ("How many Venezuelans were outside their country at the end of 2025, according to UNHCR in the text?",["Unos 7,9 millones.","Unos 790 000.","Unos 79 millones."],0,"The first paragraph gives the figure."),
 ("Where did governments start the Quito Process, according to the text?",["En Quito, en septiembre de 2018.","En Lima, en 2011.","En Asunción, en 1991."],0,"The second paragraph says so."),
 ("How long does the Colombian statute of 2021 allow people to live and work in the country, according to the text?",["Durante diez años.","Durante un mes.","Solo durante un fin de semana."],0,"The third paragraph says ten years.")])

# ---- 03
s='b2-migracion-03'
lesson(s,"Borders and crossings: Cúcuta, Pacaraima, Pisiga and the Darién","I can talk about any person, place or route, with *cualquiera que*, *quienquiera que* and *dondequiera que* + subjunctive.")
grammar(s,"Whoever, Wherever: Borders and Routes",[
 {"type":"text","title":"What you already know","content":"You know *cualquiera que*, *quienquiera que* and *dondequiera que* from B2 Unit 14. They say \"whichever\", \"whoever\" and \"wherever\", and they take the subjunctive because the answer is left open. Borders are a good place for them: whoever arrives, wherever they cross, whatever route they take."},
 ex([("Cualquier persona que llegue a la frontera necesita información clara.","Anyone who reaches the border needs clear information."),
     ("Quienquiera que cruce sin documentos corre más riesgos.","Whoever crosses without papers runs more risks."),
     ("Dondequiera que vayan los migrantes, necesitan documentos.","Wherever migrants go, they need documents."),
     ("Cualquiera que sea la ruta, el viaje es largo.","Whatever the route, the journey is long.")]),
 T("tip","Before a noun use *cualquier* (*cualquier persona que llegue*), never *cualquiera persona*. The subjunctive says \"it does not matter which\"; for a known person, use the indicative: *La persona que llegó pidió ayuda.*")])
exercises(s,[
 mc(1,s,"grammar","relativas-universales-quiera","Which sentence means \"Anyone who reaches the border needs clear information\"?",
  ["Cualquier persona que llegue a la frontera necesita información clara.","Cualquiera persona que llegue a la frontera necesita información clara.","Cualquier persona que llega a la frontera necesita información clara."],0,{2:"present-tense"}),
 fb(2,s,"relativas-universales-quiera","Dondequiera que __ los migrantes, necesitan documentos.","vayan","Wherever migrants go, they need documents."),
 mt(3,s,V,[("aduana","customs office"),("cruce","crossing"),("selva","jungle"),("altiplano","high plateau")]),
 mc(4,s,"reading","","Which jungle between Colombia and Panama did more than half a million people cross in 2023, according to the text?",
  ["La selva del Darién.","La selva de Roraima.","La selva del Chaco."],0)])
vocab(s,"Borders and crossings",[("aduana","customs office","noun"),("cruce","crossing","noun"),("selva","jungle","noun"),("altiplano","high plateau","noun")])
P=["Las fronteras de América del Sur no son solo líneas en un mapa. En muchas hay ciudades gemelas, donde las personas cruzan todos los días para trabajar, comprar o visitar a su familia. En ellas, las aduanas, los controles y los horarios de apertura cambian la vida de la gente.",
"Cúcuta, en Colombia, está unida a San Antonio del Táchira, en Venezuela, por el Puente Internacional Simón Bolívar. Según ACNUR, ha sido uno de los pasos más usados por quienes salen de Venezuela hacia Colombia. Venezuela cerró esa frontera en 2015, y en septiembre de 2022 los dos países la reabrieron.",
"Pacaraima, en el estado brasileño de Roraima, está junto a Santa Elena de Uairén, en Venezuela. Es una de las puertas de entrada de los venezolanos a Brasil, y allí funciona parte de la Operación Acogida.",
"En el altiplano andino, el paso de Pisiga, en Bolivia, da a Colchane, en Chile. Está a más de tres mil quinientos metros de altura, con frío y poco oxígeno. Allí llegan muchas personas que vienen caminando.",
"Entre Colombia y Panamá está la selva del Darién, sin carreteras. Según las autoridades panameñas, más de quinientas mil personas la cruzaron en 2023, y el número cayó mucho en 2025. Cualquiera que sea la ruta, quienes viajan sin documentos corren más riesgos, según organizaciones humanitarias."]
wc(s,P)
story(s,"Fronteras y pasos de migrantes","Twin border towns and routes: Cúcuta and San Antonio del Táchira, Pacaraima and Santa Elena de Uairén, Pisiga and Colchane at high altitude, and the Darién jungle between Colombia and Panama.",P,[
 ("Which bridge joins Cúcuta and San Antonio del Táchira, according to the text?",["El Puente Internacional Simón Bolívar.","El puente de Brooklyn.","El puente de Carmelo Peralta."],0,"The second paragraph names it."),
 ("How high is the Pisiga pass, according to the text?",["A más de tres mil quinientos metros.","A cien metros.","A nivel del mar."],0,"The fourth paragraph gives the height."),
 ("What do humanitarian organisations say about people who travel without papers, according to the text?",["Corren más riesgos.","Viajan más rápido.","No necesitan ayuda."],0,"The last paragraph says so.")])

# ---- 04
s='b2-migracion-04'
lesson(s,"Remittances: money sent home by migrants","I can grant a point and then make my own, with *si bien* + indicative.")
grammar(s,"Although It Is True That: Si Bien and Remittances",[
 {"type":"text","title":"What you already know","content":"You know *si bien* \"although it is true that\" from B2 Unit 8. It is formal, it takes the indicative, and the clause that follows says what matters more. Money that migrants send home is a topic with two sides, so it suits this pattern."},
 ex([("Si bien las remesas ayudan a muchas familias, no sustituyen la inversión pública.","Although remittances help many families, they do not replace public investment."),
     ("Las remesas, si bien llegan por celular, no siempre llegan rápido.","Remittances, although they arrive by mobile phone, do not always arrive quickly."),
     ("Si bien muchos profesionales emigran, algunos vuelven con nuevas ideas.","Although many professionals emigrate, some come back with new ideas."),
     ("Si bien la familia vive lejos, mantiene el contacto todos los días.","Although the family lives far away, it keeps in touch every day.")]),
 T("tip","Choose by register: *aunque* in everyday speech, *si bien* in a report or an essay. Both take the indicative for a fact, and *si bien* never takes *que*.")])
exercises(s,[
 mc(1,s,"grammar","concesivas-si-bien","Which sentence means \"Although remittances help many families, they do not replace public investment\"?",
  ["Si bien las remesas ayudan a muchas familias, no sustituyen la inversión pública.","Si bien que las remesas ayudan a muchas familias, no sustituyen la inversión pública.","Si bien las remesas ayuden a muchas familias, no sustituyen la inversión pública."],0),
 fb(2,s,"concesivas-si-bien","Si bien las remesas __ a muchas familias, no sustituyen la inversión pública.","ayudan","Although remittances help many families, they do not replace public investment."),
 mt(3,s,V,[("remesa","remittance"),("emigrante","emigrant"),("transferencia","transfer"),("deportado","deported person")]),
 mc(4,s,"reading","","How do many people send money today, according to the text?",
  ["Por celular, con aplicaciones.","Solo en persona, en un banco.","Por carta, en un sobre."],0)])
vocab(s,"Remittances",[("remesa","remittance","noun"),("emigrante","emigrant","noun"),("transferencia","transfer","noun"),("deportado","deported person","noun")])
P=["Cuando una persona emigra, a menudo sigue ayudando a su familia: envía dinero desde el extranjero. Ese dinero se llama remesa.",
"Según el Banco Interamericano de Desarrollo, las remesas son una fuente de ingresos muy importante en varios países de América Latina y el Caribe. No vienen solo de Estados Unidos y España: dentro de Sudamérica, muchas personas envían dinero desde países vecinos a sus familias en otros países de la región.",
"Hoy muchas personas envían dinero por celular, con aplicaciones de bancos o de empresas de pagos. Para algunas familias, esto ha sido una razón para abrir una cuenta bancaria por primera vez.",
"Los economistas señalan que las remesas ayudan a las familias a pagar comida, alquiler y estudios, pero que no sustituyen la inversión pública en salud, escuelas y empleo. Si bien las remesas ayudan a muchas familias, no sustituyen la inversión pública.",
"También se habla de la salida de profesionales, como médicos o ingenieros. Si bien muchos emigran, algunos vuelven con nuevas ideas. Desde 2025, según informó la prensa, Estados Unidos ha endurecido su política migratoria y ha devuelto a personas a varios países de América Latina, y los efectos de esta política sobre las remesas se están discutiendo."]
wc(s,P)
story(s,"Remesas: dinero que cruza fronteras","Migrants send money to their families; the text covers where remittances come from, how they are sent by phone, what economists say they cannot replace, and the 2025 change in US migration policy as reported by the press.",P,[
 ("What is a remesa, according to the text?",["Dinero que un emigrante envía a su familia.","Un tipo de visa de turista.","Un impuesto sobre los viajes."],0,"The first paragraph defines it."),
 ("What do economists say remittances cannot replace, according to the text?",["La inversión pública.","El trabajo de la familia.","El idioma."],0,"The fourth paragraph says so."),
 ("What do some people do for the first time because of phone transfers, according to the text?",["Abren una cuenta bancaria.","Compran un carro.","Aprenden inglés."],0,"The third paragraph says so.")])

# ---- 05
s='b2-migracion-05'
lesson(s,"Living together: identity, rights and the city","I can say what is done, sold or recognised without naming who does it, with *se* + verb.")
grammar(s,"What Is Done: The Se Construction",[
 {"type":"text","title":"What you already know","content":"You know the passive *se* from B1 Unit 6: *se* + a verb in the third person, when who does it is not important. The verb agrees with the thing: *se vende una arepa*, *se venden arepas*. Laws, markets and neighbourhoods are described this way, which is why it suits a lesson on living together in the city."},
 ex([("Se venden arepas venezolanas en muchas ciudades.","Venezuelan arepas are sold in many cities."),
     ("En Brasil se aprobó una nueva ley de migración en 2017.","A new migration law was approved in Brazil in 2017."),
     ("En Argentina se reconoce la migración como un derecho.","In Argentina migration is recognised as a right."),
     ("En el barrio se celebran fiestas de varios países.","In the neighbourhood festivals from several countries are celebrated.")]),
 T("tip","With a plural thing, the verb is plural too: *se venden arepas*, not *se vende arepas*. The *se* sentence names the thing, not the person who does it.")])
exercises(s,[
 mc(1,s,"grammar","pasiva-refleja","Which sentence means \"Venezuelan arepas are sold in many cities\"?",
  ["Se venden arepas venezolanas en muchas ciudades.","Se vende arepas venezolanas en muchas ciudades.","Se vendieron arepas venezolanas en muchas ciudades."],0,{2:"preterito-indefinido"}),
 fb(2,s,"pasiva-refleja","En Brasil se __ una nueva ley de migración en 2017.","aprobó","A new migration law was approved in Brazil in 2017."),
 mt(3,s,V,[("convivencia","living together"),("xenofobia","xenophobia"),("derecho","right"),("ley","law")]),
 mc(4,s,"reading","","What does the text say about Argentina's migration law of 2003?",
  ["Reconoce la migración como un derecho.","Prohíbe la entrada de turistas.","Cierra todas las fronteras."],0)])
vocab(s,"Living together",[("convivencia","living together","noun"),("xenofobia","xenophobia","noun"),("derecho","right","noun"),("ley","law","noun")])
P=["En las grandes ciudades de Sudamérica, los barrios muestran la historia de la migración. En el Bom Retiro, en São Paulo, viven y trabajan personas de varias comunidades, entre ellas coreanas y bolivianas. En Buenos Aires hay una gran comunidad boliviana, y se celebran fiestas de varios países en los barrios.",
"La comida también cambia. En ciudades como Bogotá, Lima y Santiago se venden arepas venezolanas, y en São Paulo y Buenos Aires se cocinan platos de muchos países.",
"Las leyes han cambiado también. La ley de migraciones argentina, de 2003, reconoce la migración como un derecho. En Brasil se aprobó una nueva ley de migración en 2017, que reemplazó al Estatuto del Extranjero. Los dos países usan en sus textos fórmulas como «se reconoce» y «se garantiza».",
"La convivencia no siempre es fácil. En agosto de 2018, en Pacaraima, un grupo de vecinos atacó los campamentos de migrantes venezolanos, según informó la prensa de entonces. Organizaciones de derechos humanos han señalado que la xenofobia aumenta cuando falta información y cuando los servicios públicos están saturados.",
"Muchas organizaciones de migrantes trabajan para mostrar su cultura y defender sus derechos. En varias ciudades se organizan ferias, se enseñan idiomas y se ofrece ayuda legal a quienes acaban de llegar."]
wc(s,P)
story(s,"Convivir en la ciudad","How migration shapes South American cities: neighbourhoods, food, the migration laws of Argentina and Brazil, the attack in Pacaraima in 2018 and the work of migrant organisations.",P,[
 ("Which food is sold in Bogotá, Lima and Santiago, according to the text?",["Arepas venezolanas.","Tacos mexicanos solamente.","Pizza italiana solamente."],0,"The second paragraph says so."),
 ("What happened in Pacaraima in August 2018, according to the text?",["Un grupo de vecinos atacó los campamentos de migrantes venezolanos.","Se abrió un nuevo puente.","Se firmó un tratado de comercio."],0,"The fourth paragraph says so."),
 ("What do migrant organisations do in several cities, according to the text?",["Organizan ferias, enseñan idiomas y ofrecen ayuda legal.","Cierran las escuelas.","Venden casas."],0,"The last paragraph says so.")])

# ---- consolidation
s='b2-migracion-consolidation'
lesson(s,"Review: migration, borders and living together in South America","I can use time clauses, value judgments, whoever-clauses, *si bien* and *se* to talk about migration in South America.")
exercises(s,[
 mc(1,s,"grammar","cuando-subjuntivo","Which sentence means \"As soon as the families arrive, they will ask for a permit\"?",
  ["En cuanto lleguen las familias, pedirán un permiso.","En cuanto llegan las familias, pedirán un permiso.","En cuanto llegaron las familias, pedirán un permiso."],0,{1:"present-tense",2:"preterito-indefinido"}),
 mc(2,s,"grammar","relativas-universales-quiera","Which sentence means \"Whoever arrives needs help\"?",
  ["Quienquiera que llegue necesita ayuda.","Quienquiera que llega necesita ayuda.","Quien quiera llegue necesita ayuda."],0,{1:"present-tense"}),
 fb(3,s,"concesivas-si-bien","Si bien muchos migrantes __ lejos de su familia, la mantienen cerca por teléfono.","viven","Although many migrants live far from their family, they keep it close by phone."),
 mc(4,s,"reading","","How long does the Colombian statute of 2021 allow Venezuelans to live and work in the country, according to the lesson texts?",
  ["Durante diez años.","Durante dos años.","Durante un año."],0)])
