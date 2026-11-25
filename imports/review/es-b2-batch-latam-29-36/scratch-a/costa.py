import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
V='b2-peru-coast-lima-vocab'
S='b2-perucosta'

s=f'{S}-01'
gr(s,"The Humboldt Current: Formal Cause Connectors",
 "You know *debido a* from B1 Unit 6, and *a raíz de* with it: formal ways to say \"because of\" and \"as a result of\". Both take a noun, never a verb: *debido a la corriente*, *a raíz de El Niño*. With a verb you use *porque*; you know *porque* from A1 Unit 2. Both connectors are ideal for explaining the natural causes behind a coast.",
 [("Debido a la corriente fría, casi no llueve en la costa.","*debido a* + noun: the cause comes first"),
  ("Hay muchos peces debido al afloramiento.","*debido a* + *el* = *debido al*"),
  ("A raíz de El Niño de 1997 hubo lluvias fuertes en el norte.","*a raíz de* + noun: as a result of an event"),
  ("Hay niebla porque el aire sobre el mar es frío.","*porque* + verb: with a verb, use *porque*")],
 [("Debido a la corriente fría, casi no llueve en la costa.","Because of the cold current, it hardly rains on the coast."),
  ("Debido al afloramiento, hay muchos peces frente a la costa.","Because of the upwelling, there are many fish off the coast."),
  ("A raíz de El Niño de 1997 hubo lluvias fuertes en el norte.","As a result of the 1997 El Niño there were heavy rains in the north."),
  ("Hay niebla en invierno porque el aire sobre el mar es frío.","There is fog in winter because the air over the sea is cold.")],
 "After *debido a* and *a raíz de* put a noun, not a verb: *debido a la corriente*, not *debido a que la corriente*... For a whole clause with a verb use *porque*. Write *debido al*, not *debido a el*.")
voc(s,"Sea and coast",[("la corriente","current (of water)","noun"),("el afloramiento","upwelling of cold, deep water","noun"),("la garúa","fine coastal drizzle and fog","noun"),("la anchoveta","anchoveta, small fish of the Pacific","noun")],"Peru: the Humboldt Current")
lesson(s,"Peru's coast: the Humboldt Current and a desert by the sea","Explain the desert coast and the rich sea of Peru with formal cause connectors.","formal cause connectors like debido a and a raíz de",
 ["I can explain a cause formally with *debido a* and *a raíz de* + noun.","I can say why Peru's coast is a desert and why its sea is rich in fish.","I can use the new words for the coast: *corriente*, *afloramiento*, *garúa*, *anchoveta*."])
story(s,"La corriente de Humboldt y la costa del Perú","The cold Humboldt Current explains why Peru's coast is a desert with winter fog, why its sea is rich in anchoveta, and how El Niño disturbs both.",
["La costa de Perú es un desierto: en Lima casi no llueve. Una de las razones es la corriente de Humboldt, una corriente de agua fría que viene del sur y sigue la costa hacia el norte. También se la llama corriente peruana. Su nombre recuerda a Alexander von Humboldt, que midió la temperatura del agua cerca del Callao en 1802.",
 "Debido a esa agua fría, el aire sobre el mar también es frío y casi no se forman lluvias. En cambio, durante el invierno la costa central se cubre de niebla y de una llovizna muy fina, la garúa. Por eso Lima tiene muchos días grises en esa época del año.",
 "La corriente también hace rico el mar. Frente a la costa, el agua fría y profunda sube a la superficie, un fenómeno que se llama afloramiento. Debido al afloramiento, el plancton y los peces tienen mucho alimento, y hay enormes cardúmenes de anchoveta, un pez pequeño. Según los expertos, la pesca de la anchoveta es una de las más grandes del mundo, y gran parte de lo que se pesca se convierte en harina y aceite de pescado.",
 "Cada pocos años aparece El Niño, un calentamiento del agua del Pacífico. A raíz de El Niño, la anchoveta se aleja de la costa y se pesca mucho menos. En el norte del país, el fenómeno trae lluvias fuertes, como en 1997 y 1998.",
 "A principios de los años setenta la pesca de la anchoveta cayó mucho. Según los expertos, esto ocurrió debido a la sobrepesca y a un fuerte Niño, el de 1972. Desde entonces se limita cada temporada cuánto se puede pescar."],
[("Why does Lima have so many grey days in winter?",["Porque la costa central se cubre de niebla y llovizna, la garúa.","Porque llueve con fuerza desde junio.","Porque la corriente de Humboldt es de agua caliente."],"The second paragraph describes the garúa."),
 ("What is upwelling, according to the text?",["El agua fría y profunda que sube a la superficie.","El agua caliente que se aleja de la costa.","La lluvia que cae sobre el desierto."],"The third paragraph defines it."),
 ("What happens to the anchoveta because of El Niño?",["Se aleja de la costa y se pesca mucho menos.","Aparece en enormes cardúmenes cerca de Lima.","Se convierte en harina de pescado."],"The fourth paragraph describes the effect.")])
ex(s,[
 match([("la corriente","current of water"),("el afloramiento","rising of deep cold water"),("la garúa","fine drizzle and fog"),("la anchoveta","small fish of the Pacific")],V),
 fill("Debido __ la corriente fría, casi no llueve en la costa.","a","Because of the cold current, it hardly rains on the coast.","formal-cause-connectors"),
 mc("Which sentence says \"Because of El Niño, the anchoveta moves away from the coast\"?",["Debido a El Niño, la anchoveta se aleja de la costa.","Debido a que El Niño, la anchoveta se aleja de la costa.","Debido El Niño, la anchoveta se aleja de la costa."],"formal-cause-connectors"),
 build("A raíz de El Niño de 1997 hubo lluvias fuertes en el norte.","As a result of the 1997 El Niño there were heavy rains in the north.","formal-cause-connectors"),
 dlg([("Meg","¿Qué es la garúa?"),("Carlos","_____")],["Es una niebla que hay en la costa en invierno.","Es un animal pequeño que vive en el mar frío.","Es una corriente caliente que llega cada pocos años."],V),
 dic("Debido al afloramiento, hay muchos peces frente a la costa.","Because of the upwelling, there are many fish off the coast.","formal-cause-connectors")])

s=f'{S}-02'
gr(s,"Viceregal Lima: The Passive with Ser",
 "You know the passive with *ser* + past participle from B1 Unit 18: *fue fundada*, *fueron incluidos*. The participle agrees with the thing or person that receives the action. Dates of founding, listings and proclamations are the usual place for it in history and in the news.",
 [("Lima fue fundada el 18 de enero de 1535.","*fue fundada*: feminine singular, like *Lima*"),
  ("La Universidad de San Marcos fue fundada en 1551.","*fue fundada*: agrees with *la Universidad*"),
  ("Los balcones fueron cerrados con celosías de madera.","*fueron cerrados*: masculine plural"),
  ("Santa Rosa fue canonizada por la Iglesia en 1671.","*por* + the doer, when you want to name it")],
 [("Lima fue fundada por Francisco Pizarro el 18 de enero de 1535.","Lima was founded by Francisco Pizarro on 18 January 1535."),
  ("La Universidad de San Marcos fue fundada en 1551.","The University of San Marcos was founded in 1551."),
  ("El centro histórico de Lima fue incluido en la lista de la UNESCO en 1988.","The historic centre of Lima was added to the UNESCO list in 1988."),
  ("Keiko Fujimori fue proclamada presidenta electa en 2026.","Keiko Fujimori was proclaimed president-elect in 2026.")],
 "Check the ending of the participle: *fue fundada*, *fueron incluidos*. Use *fue* for a single event in the past; *es* or *son* describes what happens now or in general.")
voc(s,"Colonial Lima",[("el virrey","viceroy, the king's governor","noun"),("el virreinato","viceroyalty","noun"),("el balcón","balcony","noun"),("la celosía","wooden lattice screen","noun")],"Peru: viceregal Lima")
lesson(s,"Viceregal Lima: a capital of balconies and viceroys","Tell the story of colonial Lima and say what was founded or declared, using the ser passive.","the passive with ser + past participle",
 ["I can say what was founded, listed or proclaimed with the passive (*fue fundada*, *fueron incluidos*).","I can say what Lima was in colonial times and what remains of it.","I can use the new words for colonial Lima: *virrey*, *virreinato*, *balcón*, *celosía*."])
story(s,"Lima virreinal","Lima was founded in 1535 and became the capital of the Viceroyalty of Peru; its wooden balconies, its university and Santa Rosa mark colonial history, and in June 2026 Keiko Fujimori was proclaimed president-elect.",
["Lima fue fundada el 18 de enero de 1535 por Francisco Pizarro, que la llamó Ciudad de los Reyes. Está en la costa, junto al río Rímac, en un valle del desierto.",
 "Desde 1542 Lima fue la capital del virreinato del Perú, que incluía gran parte de la América del Sur española. Allí vivían el virrey, los funcionarios y los comerciantes más ricos. En 1551 fue fundada la Universidad de San Marcos, una de las más antiguas de América.",
 "La Lima colonial tenía plazas, iglesias y conventos, y casas con grandes balcones de madera cerrados con celosías, que permitían mirar la calle sin ser vistos. El centro histórico conserva muchos de esos balcones, y en 1988 fue incluido en la lista del Patrimonio Mundial de la UNESCO.",
 "Según descripciones de viajeros de la época, en las calles se veía a las tapadas, mujeres que cubrían la cara con un manto y dejaban ver solo un ojo. También en Lima nació Rosa de Lima, en 1586; fue canonizada en 1671 y se la considera la primera santa de América.",
 "Hoy Lima es la capital de la república. En junio de 2026, Keiko Fujimori ganó la segunda vuelta de las elecciones presidenciales por un margen estrecho frente a Roberto Sánchez, y fue proclamada presidenta electa para el período 2026-2031."],
[("When was Lima founded?",["El 18 de enero de 1535.","En 1551.","En junio de 2026."],"The first paragraph gives the date."),
 ("What was the Universidad de San Marcos, according to the text?",["Una de las universidades más antiguas de América, fundada en 1551.","Una iglesia con balcones de madera en el Rímac.","Un convento fundado por Santa Rosa."],"The second paragraph mentions the university."),
 ("What happened in June 2026?",["Keiko Fujimori fue proclamada presidenta electa.","Lima fue fundada por Pizarro.","El centro histórico fue incluido en la lista de la UNESCO."],"The last paragraph gives the 2026 election result.")])
ex(s,[
 match([("el virrey","king's governor in the colonies"),("el virreinato","territory ruled by a viceroy"),("el balcón","balcony"),("la celosía","wooden lattice screen")],V),
 fill("Lima __ fundada el 18 de enero de 1535.","fue","Lima was founded on 18 January 1535.","ser-passive"),
 mc("Which sentence says \"The University of San Marcos was founded in 1551\"?",["La Universidad de San Marcos fue fundada en 1551.","La Universidad de San Marcos fue fundado en 1551.","La Universidad de San Marcos fueron fundada en 1551."],"ser-passive"),
 build("El centro histórico de Lima fue incluido en la lista de la UNESCO en 1988.","The historic centre of Lima was added to the UNESCO list in 1988.","ser-passive"),
 dlg([("Meg","¿Qué es una celosía?"),("Carlos","_____")],["Es una pantalla de madera que cierra un balcón.","Es una plaza con iglesias y conventos.","Es una persona que manda en nombre del rey."],V),
 dic("La ciudad fue fundada junto al río Rímac.","The city was founded next to the Rímac river.","ser-passive")])

s=f'{S}-03'
gr(s,"Afro-Peruvian Heritage: Even When",
 "You know *aun cuando* from B2 Unit 8: it works like *aunque*, only more formal. After it you use the subjunctive for a possibility or a point you grant without confirming (*aun cuando no se sepa*), and the indicative for a fact (*aun cuando la esclavitud terminó*). History and music offer both: some facts are known, and some, like the exact origin of an instrument, are not.",
 [("Aun cuando no se sepa su origen exacto, el cajón es muy popular.","subjunctive: the origin is uncertain"),
  ("Aun cuando la esclavitud fue abolida en 1854, esa historia sigue presente en la música.","indicative: a fact, *fue abolida*"),
  ("Aun cuando llueva, el festival seguirá en Chincha.","subjunctive: a possible obstacle in the future"),
  ("Aunque llueva, el festival seguirá en Chincha.","the everyday version with *aunque*")],
 [("Aun cuando no se sepa su origen exacto, el cajón es muy popular.","Even if its exact origin is not known, the cajón is very popular."),
  ("Aun cuando la esclavitud fue abolida en 1854, esa historia sigue presente en la música.","Even though slavery was abolished in 1854, that history is still present in the music."),
  ("Aun cuando llueva, el festival seguirá en Chincha.","Even if it rains, the festival will go on in Chincha."),
  ("Aun cuando se discuta su origen, el cajón es parte de la música peruana.","Even if its origin is debated, the cajón is part of Peruvian music.")],
 "Write *aun* without an accent in *aun cuando*. Ask whether you present the point as a fact (indicative) or as a possibility or an open question (subjunctive).")
voc(s,"Afro-Peruvian culture",[("el cajón","wooden box drum","noun"),("la décima","poem of ten lines","noun"),("la esclavitud","slavery","noun"),("el tambor","drum","noun")],"Peru: Afro-Peruvian heritage")
lesson(s,"Afro-Peruvian heritage: Chincha, the cajón and the décima","Talk about Afro-Peruvian history and music, granting points with aun cuando.","concessive clauses with aun cuando and the subjunctive",
 ["I can grant a point with *aun cuando* + indicative or subjunctive.","I can say what Chincha, the cajón and the décima are in Afro-Peruvian culture.","I can use the new words for the culture: *cajón*, *décima*, *esclavitud*, *tambor*."])
story(s,"La herencia afroperuana","Africans were enslaved in Peru until 1854; Chincha is a well-known centre of Afro-Peruvian culture, the cajón comes from that tradition, and Nicomedes Santa Cruz wrote décimas about it.",
["Los primeros africanos esclavizados llegaron a Perú en el siglo XVI, y durante la época colonial trabajaron en Lima, en las haciendas de la costa y en las casas de los ricos. La esclavitud fue abolida en 1854.",
 "La provincia de Chincha, en la costa sur, tiene una de las comunidades afroperuanas más conocidas. En el distrito de El Carmen, las familias mantienen música, danzas y fiestas que vienen de sus antepasados.",
 "El cajón es una caja de madera sobre la que se sienta el músico y que se toca con las manos. Se desarrolló en la cultura afroperuana de la costa, y hoy se usa en el vals criollo, en el festejo y en otros géneros. Según una explicación muy repetida, se tocaban cajas porque estaban prohibidos los tambores, pero los historiadores discuten cómo nació exactamente. Aun cuando no se sepa con exactitud su origen, el cajón fue declarado en 2001 Patrimonio Cultural de la Nación.",
 "Según se cuenta, en 1977 el guitarrista español Paco de Lucía recibió un cajón en Lima y lo llevó al flamenco, donde hoy es habitual.",
 "Nicomedes Santa Cruz (1925-1992) fue un poeta y músico peruano conocido por sus décimas, poemas de diez versos. En ellas escribió sobre la historia y la cultura afroperuanas."],
[("When was slavery abolished in Peru?",["En 1854.","En 1977.","En 2001."],"The first paragraph gives the year."),
 ("What is the cajón?",["Una caja de madera que se toca con las manos.","Un poema de diez versos.","Un baile típico de Chincha."],"The third paragraph describes the instrument."),
 ("What is a décima, according to the text?",["Un poema de diez versos.","Una caja de madera.","Una fiesta de Chincha."],"The last paragraph defines it.")])
ex(s,[
 match([("el cajón","wooden box drum"),("la décima","poem of ten lines"),("la esclavitud","slavery"),("el tambor","drum")],V),
 fill("Aun __ no se sepa su origen exacto, el cajón es parte de la música peruana.","cuando","Even if its exact origin is not known, the cajón is part of Peruvian music.","concesivas-aun-cuando"),
 mc("Which sentence says \"Even if it rains, the festival will go on in Chincha\"?",["Aun cuando llueva, el festival seguirá en Chincha.","Aun cuando que llueva, el festival seguirá en Chincha.","Aun cuando llovería, el festival seguirá en Chincha."],"concesivas-aun-cuando"),
 build("Aun cuando la esclavitud fue abolida en 1854, esa historia sigue presente en la música.","Even though slavery was abolished in 1854, that history is still present in the music.","concesivas-aun-cuando"),
 dlg([("Meg","¿Qué es un cajón?"),("Carlos","_____")],["Es una caja de madera que se toca con las manos.","Es un poema de diez versos sobre el mar.","Es una fiesta que se celebra en Chincha."],V),
 dic("Aun cuando se discuta su origen, el cajón es muy popular.","Even if its origin is debated, the cajón is very popular.","concesivas-aun-cuando")])

s=f'{S}-04'
gr(s,"Cebiche, Chifa and Nikkei: Passive Se or Impersonal Se?",
 "You know passive *se* and impersonal *se* from B1 Unit 6, and the personal *a* from A1 Unit 24, and you know that you must tell them apart (B2 Unit 19): *se* + a noun, and the verb agrees with it (*Se sirven los cebiches fríos*); *se* with no noun, and the verb stays singular (*En Lima se come muy bien*); *se* + a particular person with *a*, and the verb stays singular too (*Se invitó a los vecinos*). Food writing uses all three.",
 [("Se prepara el cebiche con pescado crudo y limón.","a thing, singular: *se prepara*"),
  ("Se sirven los cebiches fríos.","a thing, plural: *se sirven*"),
  ("En Lima se come muy bien.","no noun: the verb stays singular"),
  ("Se invitó a los vecinos a probar el cebiche.","particular people with *a*: the verb stays singular")],
 [("Se prepara el cebiche con pescado crudo y limón.","Cebiche is prepared with raw fish and lime."),
  ("Se sirven los cebiches fríos.","Cebiches are served cold."),
  ("En Lima se come muy bien.","In Lima people eat very well."),
  ("Se invitó a los vecinos a probar el cebiche.","The neighbours were invited to try the cebiche.")],
 "Ask what follows the verb. A thing: the verb agrees (*se sirven los cebiches*). A particular person: *a* and a singular verb (*se invitó a los vecinos*). Nothing: singular (*se come bien*). Do not write *se invitaron a los vecinos*.")
voc(s,"Food",[("el cebiche","raw fish dish cured in lime juice","noun"),("el ají","chilli pepper","noun"),("el camote","sweet potato","noun"),("el inmigrante","immigrant","noun")],"Peru: cebiche, chifa and nikkei")
lesson(s,"Cebiche, chifa and nikkei: how Peru eats","Describe Peruvian food and its immigrant roots, choosing between the passive se and the impersonal se.","distinguishing the passive se from impersonal se constructions",
 ["I can choose between passive and impersonal *se* (*se sirven los cebiches*, *se invitó a los vecinos*).","I can say what cebiche, chifa and nikkei cooking are and where they come from.","I can use the new words for food: *cebiche*, *ají*, *camote*, *inmigrante*."])
story(s,"Cebiche, chifa y cocina nikkei","Cebiche was added to UNESCO's list in 2023; Chinese workers arriving from 1849 and Japanese migrants from 1899 gave Peru chifa and nikkei cooking.",
["El cebiche es un plato de pescado crudo que se prepara con jugo de limón, sal, cebolla y ají. Se sirve frío, con camote y maíz. En diciembre de 2023 la UNESCO inscribió el cebiche en su lista del patrimonio cultural inmaterial. Su origen exacto es objeto de debate entre los historiadores.",
 "A partir de 1849 llegaron a Perú muchos trabajadores chinos, la mayoría de la región de Cantón, para trabajar en haciendas y en otros oficios. Con el tiempo se abrieron en Lima restaurantes de comida china adaptada a los productos peruanos, y así nació la cocina chifa. Se cree que la palabra chifa viene del cantonés. Un plato muy conocido, el lomo saltado, se considera de influencia china.",
 "En 1899 llegaron los primeros inmigrantes japoneses, que trabajaron al principio en haciendas de caña de azúcar de la costa. Sus descendientes y otros cocineros combinaron técnicas japonesas con ingredientes peruanos, y así nació la cocina nikkei. La palabra nikkei designa a los emigrantes japoneses y a sus descendientes.",
 "Hoy en Lima se come de formas muy distintas: en una misma ciudad hay cebicherías, chifas y restaurantes nikkei."],
[("What did UNESCO do in December 2023?",["Inscribió el cebiche en su lista del patrimonio inmaterial.","Declaró Lima capital del virreinato.","Fundó la primera cebichería de Perú."],"The first paragraph gives the UNESCO decision."),
 ("Where did the first chifa workers come from?",["De la región china de Cantón.","De la costa de Japón.","De las haciendas de Chincha."],"The second paragraph says most came from Canton."),
 ("What does nikkei mean?",["Los emigrantes japoneses y sus descendientes.","Un plato de pescado con limón.","Un restaurante chino de Lima."],"The third paragraph explains the word.")])
ex(s,[
 match([("el cebiche","raw fish dish with lime"),("el ají","chilli pepper"),("el camote","sweet potato"),("el inmigrante","person who comes to live in another country")],V),
 fill("Se invitó __ los vecinos a probar el cebiche.","a","The neighbours were invited to try the cebiche.","se-pasivo-vs-impersonal"),
 mc("Which sentence says \"Cebiches are served cold\"?",["Se sirven los cebiches fríos.","Se sirve los cebiches fríos.","Se sirve a los cebiches fríos."],"se-pasivo-vs-impersonal"),
 build("Se prepara el cebiche con pescado crudo y limón.","Cebiche is prepared with raw fish and lime.","se-pasivo-vs-impersonal"),
 dlg([("Meg","¿Qué es el camote?"),("Carlos","_____")],["Es una raíz dulce que se sirve con el cebiche.","Es un animal del mar que se sirve con limón.","Es una salsa roja que lleva mucho ají."],V),
 dic("En Lima se come muy bien, y se sirven cebiches en muchos lugares.","In Lima people eat very well, and cebiches are served in many places.","se-pasivo-vs-impersonal")])

s=f'{S}-05'
gr(s,"Iquitos and the Rubber Boom: Regrets and Reproaches",
 "You know *debería haber* + participle from B2 Unit 10: the modal stays in the conditional and *haber* carries the past, so *Deberíamos haber viajado* means \"we should have travelled\". Said about yourself it is a regret, said about someone else it is a reproach. *Me arrepiento de* + *haber* + participle is a plain regret. Here you use it for your own trip and reading, and you keep judgements about history to attributed sources.",
 [("Deberíamos haber viajado a Iquitos en barco.","regret: *deberíamos haber* + participle"),
  ("Deberías haber visitado la Casa de Fierro.","reproach: *deberías haber* + participle"),
  ("Tendríamos que haber leído el informe antes.","*tendríamos que haber* + participle"),
  ("Me arrepiento de no haber leído antes el informe de Casement.","*me arrepiento de* + *haber* + participle")],
 [("Deberíamos haber llegado a Iquitos en barco, porque no hay carretera.","We should have arrived in Iquitos by boat, because there is no road."),
  ("Deberías haber visitado la Casa de Fierro en Iquitos.","You should have visited the Iron House in Iquitos."),
  ("Tendríamos que haber leído el informe de Casement antes del viaje.","We should have read Casement's report before the trip."),
  ("Me arrepiento de no haber leído antes el informe de Casement.","I regret not having read Casement's report earlier.")],
 "The modal carries the person and the conditional (*deberíamos*); *haber* never changes and the participle never changes: *haber llegado*. Compare *Deberías visitar* (advice for now) with *Deberías haber visitado* (you did not).")
voc(s,"Rubber and the Amazon",[("el caucho","rubber","noun"),("la carretera","road, highway","noun"),("el informe","report","noun"),("la selva","rainforest","noun")],"Peru: Iquitos and rubber")
lesson(s,"Iquitos and the rubber boom: a city in the rainforest","Talk about Iquitos and the rubber boom, using regrets and reproaches about your own trip and reading.","regrets and reproaches about the past",
 ["I can express regrets and reproaches with *debería haber* and *me arrepiento de haber* + participle.","I can say why Iquitos has no road and what the rubber boom was.","I can use the new words for the Amazon: *caucho*, *carretera*, *informe*, *selva*."])
story(s,"Iquitos y el auge del caucho","Iquitos, in the Peruvian Amazon, has no road to the rest of the country; it grew during the rubber boom, whose abuses in the Putumayo were described in Roger Casement's 1912 report.",
["Iquitos es la capital de la región de Loreto, en la Amazonía peruana, a orillas del río Amazonas. No hay carreteras que unan la ciudad con el resto del país: a Iquitos se llega en barco por el río o en avión. Se suele decir que es la ciudad más grande del mundo a la que no se puede llegar por carretera.",
 "A finales del siglo XIX el caucho, un látex que se extrae de ciertos árboles de la selva, se hizo muy valioso, porque la industria lo necesitaba, por ejemplo, para las llantas. Desde finales del siglo XIX hasta 1912, más o menos, Iquitos creció gracias al comercio del caucho, y llegaron comerciantes y empresas de varios países.",
 "De esa época se conserva en la plaza de Armas de Iquitos la llamada Casa de Fierro, una casa de metal que se atribuye al ingeniero francés Gustave Eiffel; no todos los historiadores están de acuerdo con esa atribución.",
 "El auge del caucho tuvo un lado oscuro. En la región del Putumayo, en la frontera con Colombia, trabajaba la Peruvian Amazon Company, dirigida por Julio César Arana. En 1912 el diplomático británico Roger Casement publicó un informe en el que, según su investigación, describió torturas, asesinatos y trabajo forzoso de indígenas. Arana negó esas acusaciones.",
 "Después de 1912 el precio del caucho cayó, porque llegó al mercado el caucho de las plantaciones de Asia, y Iquitos perdió gran parte de su riqueza. Hoy es un puerto fluvial y un punto de partida para visitar la selva. A lo largo del río Ucayali viven los shipibo-konibo, un pueblo que decora telas y cerámica con diseños geométricos llamados kené."],
[("How do people reach Iquitos?",["En barco por el río o en avión.","Por una carretera desde Lima.","En tren desde Cusco."],"The first paragraph says there are no roads."),
 ("What did Roger Casement publish in 1912?",["Un informe sobre el trato a los trabajadores indígenas del Putumayo.","Un libro sobre la Casa de Fierro.","Un mapa de la región de Loreto."],"The fourth paragraph describes his report."),
 ("What happened to the price of rubber after 1912?",["Cayó, porque llegó el caucho de Asia.","Subió, porque llegaron más empresas.","No cambió en toda la región."],"The last paragraph explains the fall in price.")])
ex(s,[
 match([("el caucho","rubber"),("la carretera","road"),("el informe","report"),("la selva","rainforest")],V),
 fill("Deberíamos __ llegado a Iquitos en barco, porque no hay carretera.","haber","We should have arrived in Iquitos by boat, because there is no road.","regrets-reproaches"),
 mc("Which sentence says \"I regret not having read Casement's report earlier\"?",["Me arrepiento de no haber leído antes el informe de Casement.","Me arrepiento de no haber leer antes el informe de Casement.","Me arrepiento de que no haber leído antes el informe de Casement."],"regrets-reproaches"),
 build("Deberías haber visitado la Casa de Fierro en Iquitos.","You should have visited the Iron House in Iquitos.","regrets-reproaches"),
 dlg([("Meg","¿Qué es el caucho?"),("Carlos","_____")],["Es un material que sale de árboles de la selva.","Es un pez que vive en el río Amazonas.","Es una casa de metal que está en la plaza."],V),
 dic("Tendríamos que haber leído el informe de Casement antes del viaje.","We should have read Casement's report before the trip.","regrets-reproaches")])

s=f'{S}-consolidation'
ex(s,[
 match([("la garúa","fine drizzle and fog"),("la celosía","wooden lattice screen"),("el cajón","wooden box drum"),("la carretera","road")],V),
 fill("Debido __ El Niño, hubo menos anchoveta en la costa.","a","Because of El Niño, there was less anchoveta on the coast.","formal-cause-connectors"),
 mc("Which sentence says \"The balconies were closed with wooden screens\"?",["Los balcones fueron cerrados con celosías de madera.","Los balcones fue cerrados con celosías de madera.","Los balcones fueron cerrado con celosías de madera."],"ser-passive"),
 mc("Which sentence says \"Even if it is debated, the cajón is popular\"?",["Aun cuando se discuta su origen, el cajón es popular.","Aun cuando que se discuta su origen, el cajón es popular.","Aun cuando se discutiría su origen, el cajón es popular."],"concesivas-aun-cuando"),
 mc("Which sentence says \"The neighbours were invited to the restaurant\"?",["Se invitó a los vecinos al restaurante.","Se invitaron a los vecinos al restaurante.","Se invitó los vecinos al restaurante."],"se-pasivo-vs-impersonal"),
 fill("Me arrepiento de no __ visitado Iquitos antes.","haber","I regret not having visited Iquitos earlier.","regrets-reproaches"),
 mc("According to the texts, what did Roger Casement publish in 1912?",["Un informe sobre los abusos en el Putumayo.","Un libro de poemas sobre la costa y el mar.","Un mapa de los caminos incas del imperio."],None,cat="reading"),
 {"type":"sentence-order","category":"grammar","sentences":["Lima fue fundada en 1535. [Lima was founded in 1535.]","En 1854 fue abolida la esclavitud. [In 1854 slavery was abolished.]","En 1912 se publicó el informe de Casement. [In 1912 Casement's report was published.]","En 2023 la UNESCO inscribió el cebiche en su lista. [In 2023 UNESCO added cebiche to its list.]"],"solution":[0,1,2,3],"teaches":["preterito-indefinido"]}])
lesson(s,"Peru's coast and Amazon: Unit Review","Review the Humboldt Current, viceregal Lima, Afro-Peruvian heritage, Peruvian food and Iquitos, with the grammar you used to talk about them.","review: formal cause connectors, the ser passive, aun cuando, passive and impersonal se, regrets and reproaches",
 ["I can review what I learned about Peru's coast and Amazon, from the Humboldt Current to Iquitos.","I can use *debido a*, the *ser* passive, *aun cuando*, passive and impersonal *se*, and regrets with *haber*.","I can put events from 1535 to 2023 in order.","I can say who says what when a matter is disputed."],
 ["I can explain a cause formally with *debido a* and *a raíz de* + noun.","I can say what was founded or proclaimed with the passive (*fue fundada*).","I can grant a point with *aun cuando* + indicative or subjunctive.","I can choose between passive and impersonal *se*.","I can express regrets and reproaches with *debería haber* + participle."])
