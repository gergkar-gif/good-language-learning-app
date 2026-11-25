import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
# ---------------- LESSON 01
s='b2-mexicocentro-01'
intro=("Latin America Unit 1: Central Mexico",[
 "Welcome to the B2 Latin America track: 36 units, each about one region of Latin America, with a reading in Spanish about the place in every lesson.",
 "This track teaches no new grammar. Each lesson takes a skill you already know and uses it on the region's history, geography and culture, and it teaches the words for the topic. The instructions and the grammar screens are in English; the readings are in Spanish.",
 "This first unit is about central Mexico: the lake basin, Tenochtitlan, the colonial city, muralism and the 1985 earthquake. You start by recapping cleft sentences, from B2 Unit 1, on the Valley of Mexico."])
items=["I can use a cleft sentence with lo que to put a key cause or fact about the Valley of Mexico in the spotlight.",
"I can spotlight a place or a time with fue ... donde or fue ... cuando.",
"I can say why the valley is a closed basin and why the ground is sinking.",
"I can use the lesson's words for the basin, the lakes and the sinking ground."]
lesson_update(s,"The Valley of Mexico: a lake basin that is sinking","Use cleft sentences to say what makes the Valley of Mexico special, how its lakes were drained and why the ground is sinking.","cleft sentences (recap)",items,intro)
story_update(s,"La cuenca de los lagos y el suelo que se hunde","The Valley of Mexico is a closed basin where five lakes once lay; they were drained after the conquest, and today the soft ground of the city is sinking.",[
"El Valle de México es una cuenca cerrada: el agua de lluvia que baja de las montañas no tiene salida al mar. Está a más de dos mil doscientos metros de altura, rodeado de volcanes como el Popocatépetl y el Iztaccíhuatl. Lo que hizo especial a este valle fue que el agua se quedó dentro. Durante milenios formó cinco lagos poco profundos: Zumpango, Xaltocan, Texcoco, Xochimilco y Chalco.",
"El agua de los lagos del sur era dulce, pero la del lago de Texcoco era salada, porque el agua se evaporaba y las sales se quedaban. Los pueblos que vivieron allí construyeron diques y calzadas para protegerse de las inundaciones y cultivaron chinampas, pequeños campos sobre el agua.",
"Después de la conquista de 1521, las autoridades coloniales decidieron sacar el agua del valle en lugar de vivir con ella. A principios del siglo diecisiete abrieron el Tajo de Nochistongo, y en 1900 se terminó el Gran Canal del Desagüe. Poco a poco los lagos se secaron casi por completo, aunque todavía quedan canales en Xochimilco. Lo que antes era un mundo de canoas y chinampas se convirtió en un suelo seco y salado.",
"Hoy la ciudad está construida sobre el antiguo fondo de los lagos, un suelo blando de arcilla. Gran parte del agua potable viene de acuíferos subterráneos, y cuando se saca más agua de la que entra, el suelo se hunde. No se hunde igual en todas partes: en algunas zonas, más de veinte centímetros al año. Los edificios, las calles y las tuberías sufren las consecuencias.",
"El suelo blando tiene otro efecto: amplifica las ondas de los terremotos. El sismo de 1985, con epicentro en la costa del Pacífico, causó muchos daños en la capital. En la zona metropolitana del valle viven hoy más de veinte millones de personas, y por eso entender el suelo del valle no es solo una cuestión de historia, sino también de seguridad diaria."])
vocab_update(s,"The Valley of Mexico: a lake basin that is sinking: vocabulary",[
("la cuenca","basin","noun"),("el hundimiento","subsidence, sinking","noun"),("lacustre","lacustrine, lake-related","adjective"),("la cordillera","mountain range","noun"),("el acuífero","aquifer","noun"),("la desecación","drying out, draining","noun"),("el valle","valley","noun"),("sísmico","seismic, to do with earthquakes","adjective"),("hundirse","to sink","verb"),("blando","soft","adjective")])
grammar_update(s,"Cleft Sentences on the Valley of Mexico",[
T("What you already know","You know *Lo que más nos sorprendió fue su serenidad*, *Fue Mariana quien escribió el informe* and *Fue en Lima donde se conocieron* from B2 Unit 1: these are cleft sentences. A cleft sentence splits one idea in two halves joined by *ser*, so that the piece you want to stress comes last, or right after *fue*. This lesson uses them on the geography of the Valley of Mexico, a closed basin where the water had no way out: a cleft sentence is the natural way to name the one cause that matters."),
TAB("Three clefts at work on the valley",[
["Lo que + verb + ser + focus","Lo que distingue a este valle es que no tiene salida natural al mar. (What sets this valley apart is that it has no natural outlet to the sea.)"],
["Fue / Es + person + quien / los que","Fueron los pueblos antiguos quienes construyeron diques y calzadas. (It was the ancient peoples who built dikes and causeways.)"],
["Fue / Es + place or time + donde / cuando","Fue en 1900 cuando se terminó el Gran Canal del Desagüe. (It was in 1900 that the Gran Canal del Desagüe was finished.)"]]),
T("Details to get right","The tense of *ser* follows the other verb: *Lo que más preocupa hoy es el hundimiento* (present), *Lo que formó los lagos fueron las lluvias* (past). When the spotlighted piece is plural, careful writing makes *ser* agree with it: *fueron las lluvias*, *son los acuíferos*. In Latin American speech you will also hear *que* instead of *cuando* or *donde* (*Fue en 1900 que se terminó*); in careful writing, keep *cuando* and *donde*."),
EX("In context",[
("Lo que más preocupa hoy es el hundimiento del suelo.","What worries people most today is the sinking of the ground."),
("Fue en el lago de Texcoco donde el agua era salada.","It was in Lake Texcoco that the water was salty."),
("Lo que formó los cinco lagos fueron las lluvias que bajaban de las montañas.","What formed the five lakes was the rain that ran down from the mountains."),
("Fue después de la conquista cuando las autoridades empezaron a secar los lagos.","It was after the conquest that the authorities began to drain the lakes."),
("Lo que protegía la ciudad eran los diques y las calzadas.","What protected the city were the dikes and the causeways.")]),
TIP("A cleft sentence is a spotlight: keep it for the one cause or fact you want the reader to remember, not for every sentence of a paragraph.")])
ex_write(s,[
match(s+'.ex01',[("la cuenca","basin"),("el hundimiento","subsidence, sinking"),("lacustre","lacustrine, lake-related"),("la cordillera","mountain range")]),
mc_read(s+'.ex02',"According to the text, why did water collect at the bottom of the Valley of Mexico?",[
"Porque es una cuenca cerrada y el agua no tiene salida al mar.",
"Porque un gran río del norte termina allí y deja su agua en el valle.",
"Porque los pueblos antiguos construyeron un canal para traer agua al valle."]),
fill(s+'.ex03',"Lo ____ más preocupa hoy es el hundimiento del suelo.","que","What worries people most today is the sinking of the ground.",'oraciones-hendidas-enfasis'),
mc_read(s+'.ex04',"According to the text, what did the colonial authorities decide to do after 1521?",[
"Empezar la desecación de los lagos en lugar de vivir con el agua.",
"Ampliar los lagos con diques nuevos para tener más agua dulce.",
"Llevar la capital a las montañas para estar lejos de las lluvias."]),
build(s+'.ex05',["Fue","en","1900","cuando","se","terminó","el","Gran","Canal","del","Desagüe."],"It was in 1900 that the Gran Canal del Desagüe was finished.",'oraciones-hendidas-enfasis'),
listen(s+'.ex06',"Cuando se saca más agua de los acuíferos de la que entra, el suelo se hunde.",[
"When more water is taken from the aquifers than flows in, the ground sinks.",
"When more water flows into the aquifers than is taken out, the ground rises.",
"When water is taken from the lakes instead of the aquifers, the ground sinks."],'oraciones-hendidas-enfasis'),
dial(s+'.ex07',[("Guía","¿Por qué es tan peligrosa para la ciudad la actividad sísmica?"),("Tú","_____"),("Guía","Entonces el suelo del antiguo lago es el problema.")],[
"Lo que la hace peligrosa es el suelo blando del antiguo lago.",
"Lo que la hace peligrosa son el suelo blando del antiguo lago.",
"Lo que la hace peligrosa fue el suelo blando del antiguo lago."],'oraciones-hendidas-enfasis'),
write(s+'.ex08',[("Say that what worries people today is the sinking of the ground. Start with 'Lo que'.","Lo que preocupa hoy es el hundimiento del suelo.")],'oraciones-hendidas-enfasis')])

# ---------------- LESSON 02
s='b2-mexicocentro-02'
items=["I can put a quality or a place first, as in Importante fue ..., to stress it when I tell about Tenochtitlan.",
"I can make the verb agree with the subject that comes after it.",
"I can describe how Tenochtitlan was built on the lake and how it fell in 1521.",
"I can use the lesson's words for causeways, dikes and the siege."]
lesson_update(s,"Tenochtitlan: a city on a lake and the conquest of 1521","Use fronting to stress what mattered most in the city the Mexica built on a lake and in the siege of 1521.","fronting for emphasis (recap)",items)
story_update(s,"Tenochtitlan: una ciudad sobre el agua","Tradition says the Mexica founded Tenochtitlan on an islet in Lake Texcoco around 1325; the city fell to Cortés and his allies in 1521.",[
"Según la tradición, hacia 1325 los mexicas, un pueblo llegado del norte, fundaron su ciudad en un islote del lago de Texcoco. Su dios les había señalado el lugar: un águila sobre un nopal, devorando una serpiente. México-Tenochtitlan se convirtió en la ciudad más poderosa de una alianza de tres ciudades, y muchos pueblos le pagaban tributo.",
"Para unir la isla con tierra firme, los mexicas hicieron tres calzadas: la de Tepeyac, al norte, la de Tlacopan, al oeste, y la de Iztapalapa, al sur. En las calzadas había tramos con puentes de madera que se podían quitar. El agua potable llegaba desde Chapultepec por un acueducto con dos canales, de modo que se podía limpiar uno mientras el otro seguía en uso.",
"Muy importante fue también el albarradón de Nezahualcóyotl, un dique de varios kilómetros construido hacia mediados del siglo quince. Separaba el agua salada del lago de Texcoco de las aguas dulces, ayudaba a proteger la ciudad de las inundaciones y mantenía el agua dulce cerca de las chinampas.",
"En noviembre de 1519, Hernán Cortés y sus soldados entraron en la ciudad por la calzada del sur, acompañados de aliados indígenas, sobre todo tlaxcaltecas. El soldado Bernal Díaz del Castillo contó años después que la ciudad sobre el agua les parecía una de las cosas encantadas de los libros de caballerías, como el Amadís de Gaula.",
"Los españoles y sus aliados rodearon la ciudad en 1521. Durante el asedio, las epidemias, sobre todo la viruela, mataron a muchos habitantes. Tenochtitlan cayó el 13 de agosto de 1521 y sufrió el saqueo. Los historiadores discuten cuánto pesó cada causa: los aliados indígenas, las armas o las enfermedades. Sobre los restos de Tenochtitlan se construyó la ciudad colonial, y junto a la catedral aparecieron en 1978 los restos del Templo Mayor."])
vocab_update(s,"Tenochtitlan: a city on a lake and the conquest of 1521: vocabulary",[
("la calzada","causeway","noun"),("el acueducto","aqueduct","noun"),("la chinampa","chinampa, floating garden","noun"),("el albarradón","dike, embankment","noun"),("el islote","islet","noun"),("el asedio","siege","noun"),("el saqueo","looting, sack","noun")])
grammar_update(s,"Fronting in the Story of Tenochtitlan",[
T("What you already know","You know *Crucial fue la intervención del mediador* and *En aquella ciudad comenzó la rebelión* from B2 Unit 1: this is fronting. You also know *resultar* + adjective from B1 Unit 15. Fronting moves the piece you want to stress to the front of the sentence, and the subject then usually comes after the verb. Writers of history use it to mark the high point of a paragraph. This lesson applies it to Tenochtitlan: the city on the lake, its causeways and dike, and the siege."),
TAB("What can go first",[
["Adjective + ser / resultar + subject","Importante fue el albarradón de Nezahualcóyotl. (Important was the dike of Nezahualcóyotl.)"],
["Place or time phrase + verb + subject","En un islote del lago de Texcoco fundaron los mexicas su ciudad. (On an islet in Lake Texcoco the Mexica founded their city.)"],
["De + noun phrase + ser + subject","De gran importancia fueron las calzadas para la vida de la ciudad. (Of great importance were the causeways for the life of the city.)"]]),
T("Two rules to keep","The verb and the adjective agree with the subject that comes after them: *Importante fue el albarradón*, *Importantes fueron las calzadas* (not *fue las calzadas*). And the subject stays behind the verb: *Importantes las calzadas fueron* sounds unnatural. The usual order is still fine and more common: fronting is for the moment you want to stress."),
EX("In context",[
("Muy importante fue el albarradón de Nezahualcóyotl para proteger la ciudad.","The dike of Nezahualcóyotl was very important for protecting the city."),
("Junto a la catedral aparecieron los restos del Templo Mayor.","Next to the cathedral the remains of the Templo Mayor appeared."),
("Por la calzada del sur entraron en la ciudad los soldados de Cortés.","By the southern causeway Cortés's soldiers entered the city."),
("Terrible fue la epidemia de viruela que mató a muchos habitantes.","Terrible was the smallpox epidemic that killed many inhabitants."),
("Sobre los restos de Tenochtitlan se construyó la ciudad colonial.","On the remains of Tenochtitlan the colonial city was built.")]),
TIP("Fronting works as a climax: use it once in a paragraph, at the point you want to stress. If every sentence starts with its adjective, the text sounds heavy.")])
ex_write(s,[
match(s+'.ex01',[("la calzada","causeway"),("el acueducto","aqueduct"),("la chinampa","chinampa, floating garden"),("el albarradón","dike, embankment")]),
mc_read(s+'.ex02',"According to the text, how did drinking water reach Tenochtitlan from Chapultepec?",[
"Por un acueducto con dos canales, y se limpiaba uno mientras el otro funcionaba.",
"Por un acueducto con un solo canal, que se cerraba para limpiarlo.",
"Por barcas que cruzaban el lago con agua dulce cada mañana."]),
fill(s+'.ex03',"Muy importante ____ el albarradón de Nezahualcóyotl para proteger la ciudad.",None,"The dike of Nezahualcóyotl was very important for protecting the city.",'inversion-enfasis-fronting',answers=["fue","resultó"]),
mc_read(s+'.ex04',"According to the text, what happened to Tenochtitlan in 1521?",[
"Cayó el 13 de agosto, después de un asedio, y sufrió el saqueo.",
"Cayó sin lucha, porque los habitantes abrieron las puertas a Cortés.",
"Cayó en el mismo mes en que Cortés y sus soldados llegaron a la ciudad."]),
build(s+'.ex05',["Junto","a","la","catedral","aparecieron","los","restos","del","Templo","Mayor."],"Next to the cathedral the remains of the Templo Mayor appeared.",'inversion-enfasis-fronting'),
listen(s+'.ex06',"En un islote del lago de Texcoco fundaron los mexicas su ciudad.",[
"On an islet in Lake Texcoco the Mexica founded their city.",
"On a hill beside Lake Texcoco the Mexica founded their city.",
"On an islet in Lake Chalco the Mexica founded their city."],'inversion-enfasis-fronting'),
dial(s+'.ex07',[("Guía","¿Qué obra protegía a la ciudad de las inundaciones?"),("Tú","_____"),("Guía","Entonces esa obra cuidaba la ciudad.")],[
"Importante fue el albarradón de Nezahualcóyotl, una obra muy larga.",
"Importante fueron el albarradón de Nezahualcóyotl, una obra muy larga.",
"Importante el albarradón fue de Nezahualcóyotl, una obra muy larga."],'inversion-enfasis-fronting'),
write(s+'.ex08',[("Say that the aqueduct from Chapultepec was very important for the city. Start with 'Muy importante fue'.","Muy importante fue el acueducto de Chapultepec para la ciudad.")],'inversion-enfasis-fronting')])
