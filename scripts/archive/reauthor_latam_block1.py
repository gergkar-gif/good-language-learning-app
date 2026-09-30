#!/usr/bin/env python3
"""Re-author Latin America Track Block 1 (Units 01-06, 36 files).

Units:
01. precolombina
02. civilizaciones
03. llegadaeuropeos
04. conquista
05. sociedadcolonial
06. economiacolonial

Pacing: Rest is History narrative style.
Avg sentence length: 11-15 words.
Vocab retention: >= 85%.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "content", "es", "stories", "world", "b1")

STORIES = {
    # =========================================================================
    # UNIT 01: precolombina
    # =========================================================================
    "b1-precolombina-01-continente.json": [
        "1492 marca un antes y un después en la historia humana. Pero antes de las carabelas europeas, el continente americano ya vibraba de vida.",
        "Una extraordinaria diversidad de pueblos habitaba esta inmensa longitud geográfica. Desde el Ártico helado hasta el extremo sur, los humanos dominaron cada rincón.",
        "Cada pueblo aprendió a transformar su propio paisaje natural. En las selvas, valles y montañas, la alimentación dependía de un cultivo esencial: el maíz.",
        "Los antiguos artistas aprendieron a tallar monumentos de piedra duradera. Su legado cultural desafió el paso de los siglos.",
        "Sin embargo, estas poblaciones vivían aisladas del resto del mundo. Desconocían las enfermedades mortales que pronto cruzarían el océano para cambiar su historia."
    ],
    "b1-precolombina-02-civilizaciones.json": [
        "En Mesoamérica y en los Andes, la vida urbana alcanzó niveles deslumbrantes. Florecieron civilizaciones con una compleja escritura basada en el glifo tallado.",
        "En las selvas del sur, los mayas organizaron su territorio en ciudades-estado rivales. Los sacerdotes desarrollaron un calendario solar asombrosamente exacto.",
        "Más al norte, los mexicas construyeron un formidable imperio militar. El náhuatl era la lengua franca que unía a millones de vasallos.",
        "En las alturas andinas, los incas vencieron a la geografía más difícil del planeta. Trazaron un extenso camino real y tendieron puentes colgantes sobre profundos abismos.",
        "Ni siquiera el terremoto más violento destruía sus sólidos muros de piedra. Hoy, millones de descendientes todavía conservan vivas aquellas tradiciones."
    ],
    "b1-precolombina-03-sociedad.json": [
        "En el corazón de estas urbes sagradas, la vida social estaba estrictamente ordenada. En la plaza central, la estela de piedra proclamaba la gloria del rey.",
        "Cada guerrero valiente aspiraba al honor y a la gloria en la batalla. Las victorias militares permitían cierta movilidad social dentro de la comunidad.",
        "Sin embargo, la gran mayoría de la población pagaba un alto tributo o impuesto en granos y telas al palacio.",
        "Quienes caían en la pobreza o contraían una deuda impagable podían terminar en la servidumbre. El poder imperial lograba someter tanto a pueblos vecinos como a sus propios siervos.",
        "El orden del universo dependía de esta rígida pirámide humana. Nadie desafiaba las reglas sin pagar un precio terrible."
    ],
    "b1-precolombina-04-vidacotidiana.json": [
        "¿Cómo era un día cualquiera en una ciudad precolombina? La mañana comenzaba temprano entre los aromas del mercado.",
        "La gente común comía tortillas de maíz con frijoles y especias picantes. Los campesinos solían masticar hojas de coca para resistir la fatiga y evitar la desnutrición.",
        "Los nobles disfrutaban de un lujo especial: una bebida amarga y espumosa hecha con cacao puro. Su elegante vestimenta de plumas indicaba claramente su alto rango social.",
        "Por la tarde, la multitud se reunía alrededor de la cancha del juego de pelota. El deporte tenía un significado cósmico y religioso muy profundo.",
        "En ocasiones solemnes, el ritual terminaba con un sacrificio humano dedicado a los dioses del sol y de la lluvia."
    ],
    "b1-precolombina-05-evidencia.json": [
        "Descubrir el pasado precolombino ha sido una tarea detectivesca llena de obstáculos. Muchos códices antiguos fueron quemados durante la conquista europea.",
        "Solo un puñado de manuscritos logró sobrevivir al fuego y a la humedad de la selva. Por eso, cada nuevo hallazgo arqueológico es motivo de fiesta científica.",
        "La arqueología moderna ofrece una fuente directa y fiable para reconstruir la historia. Las tumbas intactas y los templos ocultos aportan la evidencia más sólida.",
        "Los científicos analizan cada vasija y cada hueso como una prueba fundamental de aquel mundo perdido.",
        "El legado de estas culturas sigue asombrando al mundo entero por su belleza, su misterio y su conocimiento astronómico."
    ],
    "b1-precolombina.json": [
        "Mucho antes del arribo europeo, América era un continente vibrante con millones de habitantes y una asombrosa diversidad de pueblos.",
        "En Mesoamérica y en los Andes, grandes civilizaciones construyeron ciudades monumentales, templos sagrados, calendarios solares y amplios caminos de piedra.",
        "La sociedad combinaba una agricultura innovadora con rígidas jerarquías gobernadas por sacerdotes, guerreros y monarcas poderosos.",
        "La vida diaria transcurría entre mercados bulliciosos, canchas ceremoniales de juego de pelota y rituales dedicados a las fuerzas de la naturaleza.",
        "Aunque muchas crónicas fueron destruidas, la evidencia arqueológica moderna rescata el impresionante legado de este continente ancestral."
    ],

    # =========================================================================
    # UNIT 02: civilizaciones
    # =========================================================================
    "b1-civilizaciones-01-mayas.json": [
        "En las densas selvas de Centroamérica, los mayas lograron algo extraordinario. Levantaron grandes pirámides de piedra rodeadas por una vegetación salvaje.",
        "Los sabios inventaron un elaborado sistema de glifos jeroglíficos. Durante décadas, los arqueólogos lucharon para descifrar el significado de cada símbolo tallado.",
        "A pesar de un terreno desigual y pantanoso, sus ciudades lograron prosperar durante siglos gracias a complejas obras de riego.",
        "Sin embargo, hacia el siglo noveno, una prolongada sequía golpeó la región. Las cosechas fallaron y la escasez de agua se volvió desesperada.",
        "La falta de alimentos comenzó a despoblar los grandes centros ceremoniales. La selva avanzó silenciosa sobre los templos abandonados."
    ],
    "b1-civilizaciones-02-mexicas.json": [
        "Tenochtitlan, 1500. En medio de un lago salado brilla una ciudad deslumbrante con canales y puentes levadizos.",
        "Los mexicas dominaban el valle central mediante una poderosa triple alianza militar. Ningún vecino se atrevía a desafiar su fuerza.",
        "El emperador solía exigir un cuantioso tributo a los pueblos conquistados. Cada año llegaban miles de mantas, oro, plumas y ricas cosechas de maíz.",
        "Algunos cronistas antiguos solían exagerar las cifras de las batallas para impresionar al rey de España.",
        "Pero la reciente excavación del Templo Mayor y cada nuevo hallazgo arqueológico confirman el poder real que logró sostener este imperio."
    ],
    "b1-civilizaciones-03-incas.json": [
        "En las alturas heladas de los Andes, el Imperio Inca creó un estado perfectamente coordinado. No tenían escritura alfabética, pero no la necesitaban.",
        "Un hábil mensajero corría velozmente por los caminos de montaña llevando un quipu: un complejo sistema de cuerdas de colores y nudos.",
        "Para cultivar la empinada ladera andina, construyeron terrazas escalonadas de muros concéntricos. Aprovecharon cada nivel de altitud para distintos cultivos.",
        "Cada nuevo emperador debía conquistar sus propias tierras, porque no podía heredar directamente la finca real de su padre difunto.",
        "Este asombroso ingenio agrícola y arquitectónico permitió alimentar a millones de súbditos en el paisaje más empinado del mundo."
    ],
    "b1-civilizaciones-04-religion.json": [
        "En todas estas civilizaciones, el mundo visible estaba íntimamente conectado con las fuerzas de la naturaleza. Cada montaña y cada río era un lugar sagrado.",
        "El sumo sacerdote y el escriba instruido pertenecían a la casta más respetada y temida de la sociedad.",
        "Los sacerdotes observaban las estrellas para determinar el momento más propicio para la siembra o para declarar la guerra.",
        "Cuando una terrible enfermedad o una sequía azotaba a la población, el pueblo buscaba aplacar el enojo de los dioses.",
        "El templo lograba acumular enormes tesoros, asegurando así la legitimidad divina de los reyes ante sus súbditos."
    ],
    "b1-civilizaciones-05-legado.json": [
        "Las grandes civilizaciones precolombinas sufrieron el violento choque de la conquista, pero sus raíces nunca fueron borradas del mapa.",
        "En los Andes, la papa evitó que una plaga o una hambruna generalizada matara de hambre a las clases populares europeas.",
        "Los campesinos indígenas sabían cómo extraer el veneno de la yuca brava para transformar una raíz venenosa en pan nutritivo.",
        "Pese a siglos de desconfianza y a los castigos impuestos por el tribunal colonial, las lenguas indígenas lograron transmitir saberes milenarios.",
        "Hoy, estas culturas milenarias ya no están en peligro de olvido. Sus descendientes reclaman con orgullo su lugar en el mundo moderno."
    ],
    "b1-civilizaciones.json": [
        "Las tres grandes civilizaciones americanas —mayas, mexicas e incas— desarrollaron respuestas geniales a los desafíos de sus respectivos entornos naturales.",
        "Los mayas descifraron los misterios del tiempo en la selva, mientras los mexicas levantaron una metrópoli lacustre sostenida por alianzas y tributos.",
        "En las alturas andinas, los incas unieron miles de kilómetros mediante caminos de piedra, mensajeros veloces y terrazas agrícolas concéntricas.",
        "Sacerdotes y escribas organizaban el culto sagrado, acumulando conocimientos astronómicos y legitimando el poder político de sus gobernantes.",
        "Su herencia perdura en los alimentos globales que domesticaron, en sus lenguas vivas y en la resistencia cultural de sus millones de descendientes."
    ],

    # =========================================================================
    # UNIT 03: llegadaeuropeos
    # =========================================================================
    "b1-llegadaeuropeos-01-viaje.json": [
        "Palos de la Frontera, agosto de 1492. Tres carabelas de madera se preparan para zarpar hacia lo desconocido en el océano Atlántico.",
        "Cristóbal Colón había pasado años intentando financiar su arriesgado proyecto. Varios reyes europeos decidieron rechazar su propuesta por considerarla disparatada.",
        "Tras semanas navegando sin ver tierra firme, el miedo se apoderó de la tripulación. El capitán temió un motín violento en alta mar.",
        "En la madrugada del doce de octubre, un marinero logró avistar tierra en el horizonte y reclamó la recompensa prometida.",
        "Colón bajó a tierra para desembarcar en una pequeña isla del Caribe, a la que decidió bautizar con el nombre de San Salvador."
    ],
    "b1-llegadaeuropeos-02-encuentro.json": [
        "En las playas del Caribe, los primeros encuentros entre taínos y españoles estuvieron marcados por la curiosidad mutua y la sorpresa.",
        "Los isleños recibieron a los recién llegados con generosa hospitalidad. Hubo un continuo intercambio de comida fresca, loros y pequeños adornos de oro.",
        "Pronto la actitud de los europeos cambió radicalmente. Exigieron oro a la fuerza y comenzaron a castigar severamente a quienes se resistían.",
        "Los conquistadores convirtieron a los indígenas en mano de obra forzada para buscar oro en los ríos. Poco después, la viruela desató el caos.",
        "La población nativa comenzó a reducirse drásticamente. Algunos frailes valientes decidieron presenciar el horror y denunciar las injusticias ante la Corona."
    ],
    "b1-llegadaeuropeos-03-resistencia.json": [
        "La conquista del Caribe no fue un paseo pacífico. Los pueblos originarios lucharon valientemente para defender su libertad y sus tierras.",
        "En la isla de La Española, el cacique Hatuey vio morir a su gente. Decidió huir a la vecina Cuba en canoas para advertir a otras tribus.",
        "A pesar de sus esfuerzos, los soldados españoles lograron capturar al rebelde en el monte.",
        "Los conquistadores condenaron a Hatuey a morir quemado en la hoguera. Antes de morir, el líder indígena prefirió la muerte a la sumisión.",
        "Muchos otros caciques decidieron rebelarse y refugiarse en las montañas, pero las armas de acero y los perros de guerra lograron aplastar la resistencia."
    ],
    "b1-llegadaeuropeos-04-nuevosmundos.json": [
        "El desembarco europeo desató una de las mayores transformaciones ecológicas y humanas en la historia del planeta Tierra.",
        "Miles de hectáreas de selva fueron taladas para introducir ganado vacuno, ovejas, caballos y caña de azúcar.",
        "Al mismo tiempo, nuevos patógenos invisibles provocaron una auténtica catástrofe demográfica entre los pueblos originarios.",
        "Comunidades enteras vieron extinguirse a sus ancianos y sabios. Los sobrevivientes tuvieron que desplazarse a zonas remotas para salvar sus vidas.",
        "El planeta comenzó a absorber los efectos de este intercambio biológico duradero que conectó para siempre a los dos hemisferios."
    ],
    "b1-llegadaeuropeos-05-transformacion.json": [
        "Hacia mediados del siglo dieciséis, el mundo caribeño se había transformado de forma radical y definitiva.",
        "A pesar del continuo desacuerdo entre historiadores sobre las cifras iniciales, cada nuevo cálculo científico suele elevar las pérdidas humanas.",
        "Sobre las ruinas del mundo taíno surgió una nueva sociedad de carácter mestizo, donde se mezclaron sangres y costumbres diversas.",
        "La religión católica se impuso en cada rincón sagrado. Pronto surgió una devoción popular única con la aparición de imágenes sincréticas.",
        "América y Europa quedaron entrelazadas para siempre en un doloroso proceso de nacimiento cultural que cambiaría el rumbo del mundo."
    ],
    "b1-llegadaeuropeos.json": [
        "En 1492, la expedición financiada por Castilla llegó a las Antillas, dando inicio a un encuentro tan fascinante como devastador.",
        "La curiosidad inicial y el intercambio comercial pronto dieron paso a la explotación laboral minera y a la violencia colonial.",
        "Líderes indígenas como el cacique Hatuey encabezaron valientes focos de resistencia armada antes de ser aplastados por la superioridad militar europea.",
        "Las epidemias desatadas por nuevos gérmenes diezmaron a las poblaciones nativas, transformando profundamente el paisaje ecológico de las islas.",
        "De este cataclismo biológico y cultural nació un nuevo continente mestizo, marcado por el dolor, el sincretismo religioso y la supervivencia."
    ],

    # =========================================================================
    # UNIT 04: conquista
    # =========================================================================
    "b1-conquista-01-mexico.json": [
        "Veracruz, 1519. Hernán Cortés toma una decisión desesperada para evitar la fuga de sus soldados: decide inutilizar sus propios navíos.",
        "Los españoles avanzaron hacia el interior buscando aliados indígenas. Encontraron a los tlaxcaltecas, enemigos jurados del emperador azteca.",
        "En Tenochtitlan, Cortés capturó a Moctezuma como rehén. La situación comenzó a deteriorarse con rapidez por el malestar del pueblo mexica.",
        "Durante la Noche Triste, los rebeldes lograron expulsar a los invasores de la ciudad con enormes pérdidas para los europeos.",
        "Cortés reorganizó a sus tropas y sometió la metrópoli a un implacable asedio de noventa días, cortando el suministro de agua y conspirando con sus aliados nativos."
    ],
    "b1-conquista-02-peru.json": [
        "Cajamarca, noviembre de 1532. Dos hermanos incas, Huáscar y Atahualpa, acababan de disputarse el trono imperial en una sangrienta guerra fratricida.",
        "Francisco Pizarro aprovechó el caos interno. Usó como pretexto el rechazo de una biblia para atacar por sorpresa y masacrar a los guardias desarmados.",
        "Atahualpa fue tomado prisionero en su propio campamento. Para obtener su libertad, prometió recolectar un fabuloso rescate en oro y plata.",
        "A pesar de llenar dos cuartos con metales preciosos, el Inca fue ejecutado tras bautizarse forzosamente para evitar la hoguera.",
        "Pizarro nombró a un soberano títere, pero la resistencia andina logró organizarse para sitiar la ciudad del Cuzco durante largos meses."
    ],
    "b1-conquista-03-alianzas.json": [
        "¿Cómo pudieron unos cientos de soldados europeos derrotar a imperios con millones de habitantes? La respuesta reside en la política nativa.",
        "El número de guerreros indígenas solía superar por mucho a los invasores con armaduras de acero.",
        "Los mexicas consideraron una traición imperdonable que sus vasallos apoyaran a Cortés. Pero estos pueblos estaban resentidos por el duro tributo.",
        "Cortés prometió conceder privilegios y eximir de cargas fiscales a quienes lo ayudaran en la batalla final.",
        "Los caciques buscaron un margen de maniobra propio, sin sospechar que su alianza facilitaría la futura reubicación de sus comunidades."
    ],
    "b1-conquista-04-violencia.json": [
        "El choque militar entre ambos mundos estuvo marcado por una táctica implacable. Los españoles dominaban el arte de preparar la emboscada perfecta.",
        "Los exploradores veteranos sabían advertir el menor movimiento enemigo. Usaban los caballos y los perros para intimidar a multitudes que jamás los habían visto.",
        "Frente al terror de las armas de fuego, muchas ciudades decidieron someterse sin presentar batalla para evitar la destrucción total.",
        "Para frenar al jinete blindado, los defensores cavaron zanjas profundas disimuladas con ramas para ocultar el foso mortal.",
        "Cada bando intentaba legitimar su violencia en nombre de sus propios dioses y de sus leyes ancestrales."
    ],
    "b1-conquista-05-catastrofe.json": [
        "Al terminar los combates, los vencedores se apresuraron a redactar cartas oficiales de victoria dirigidas al rey Carlos V.",
        "Los cronistas españoles intentaron recopilar testimonios heroicos, presentándose a menudo como hombres con un corazón benévolo y civilizador.",
        "Pero el balance humano para la población indígena fue devastador. El alimento se volvió muy escaso en los campos abandonados.",
        "La hambruna y las enfermedades importadas quebraron la capacidad de resistir de millones de familias.",
        "Muchos pueblos sabían de antemano que la derrota significaría el fin de su mundo y el inicio de una era de servidumbre colonial."
    ],
    "b1-conquista.json": [
        "La caída de los imperios azteca e inca no se debió solo a las armas de pólvora, sino a divisiones internas y alianzas con pueblos descontentos.",
        "Cortés supo aprovechar el resentimiento contra Tenochtitlan, mientras Pizarro se benefició de la sangrienta guerra civil entre los príncipes incas.",
        "La superioridad técnica de las armas europeas y la caballería causaron un enorme impacto psicológico en las primeras batallas.",
        "La guerra interrumpió la agricultura tradicional, desatando una terrible hambruna que potenció la mortalidad de las epidemias recién llegadas.",
        "La conquista militar sentó las bases de un orden colonial impuesto sobre las cenizas de las más brillantes civilizaciones autóctonas."
    ],

    # =========================================================================
    # UNIT 05: sociedadcolonial
    # =========================================================================
    "b1-sociedadcolonial-01-imperio.json": [
        "Para gobernar un territorio tan inmenso, la Corona española creó el virreinato como la máxima unidad política y administrativa en América.",
        "A la cabeza de cada jurisdicción estaba el virrey, representante directo del monarca en aquel vasto continente.",
        "Junto al virrey funcionaba la Real Audiencia, máximo tribunal de justicia cuya sede se ubicaba en las principales capitales coloniales.",
        "El sistema comercial monopolista obligaba a que cada mercancía pasara exclusivamente por puertos autorizados en España.",
        "Esta rígida política resultaba muy perjudicial para las provincias periféricas, que quedaban al margen de las grandes rutas de abastecimiento."
    ],
    "b1-sociedadcolonial-02-jerarquia.json": [
        "En la sociedad virreinal, el color de la piel y el origen familiar determinaban la posición de cada individuo en la esfera pública.",
        "Solo los peninsulares nacidos en España ocupaban los puestos más altos en el tribunal y en el gobierno colonial.",
        "Los criollos, hijos de españoles nacidos en América, veían con frustración cómo su influencia política solía descender frente a los recién llegados.",
        "En las ciudades, cada gremio de artesanos controlaba los oficios, mientras algunos comerciantes intentaban falsificar títulos de hidalguía.",
        "Este profundo agravio social y el fuerte arraigo a la tierra americana comenzaron a acumularse en el corazón de las élites locales."
    ],
    "b1-sociedadcolonial-03-iglesia.json": [
        "La Iglesia católica fue el pilar ideológico y espiritual más poderoso de todo el período virreinal en América.",
        "Cada orden religiosa —como los franciscanos, dominicos y jesuitas— organizó misiones y pueblos de indios de carácter semiautónomo.",
        "La Iglesia se convirtió en un próspero terrateniente que controlaba haciendas, escuelas y hospitales, tejiendo un sólido tejido social.",
        "Para combatir la herejía y proteger la ortodoxia de la fe, la Inquisición vigilaba de cerca las lecturas y conductas de los vecinos.",
        "Nadie podía carecer de sacramentos sin ser marginado; el poder eclesiástico regulaba cada hora de la vida cotidiana."
    ],
    "b1-sociedadcolonial-04-vidacotidiana.json": [
        "Las ciudades coloniales se diseñaron siguiendo un modelo geométrico en forma de cuadrícula perfecta alrededor de una plaza mayor.",
        "El cabildo solía promulgar leyes sobre la limpieza de las calles y el mantenimiento del acueducto que traía agua fresca desde los cerros.",
        "Por las mañanas, el mercado bullicioso se llenaba de vendedores ambulantes pregonando frutas, velas, leche y carbón.",
        "Las barreras entre los grupos sociales tendían a difuminarse en las fiestas populares, a pesar del disgusto de las autoridades.",
        "Los señores temían la debilidad de sus defensas y vivían escandalizados ante rumores de criados acusados de envenenar a sus amos."
    ],
    "b1-sociedadcolonial-05-vivir.json": [
        "El tiempo colonial parecía transcurrir al ritmo pausado de las campanas de las iglesias y los calendarios religiosos.",
        "La vida cotidiana parecía encajar en las normas de la Iglesia, y cada bautismo quedaba anotado en el registro parroquial.",
        "El trazado urbano combinaba un orden geométrico oficial con el crecimiento orgánico de los barrios populares extramuros.",
        "Los gobernantes intentaron moldear una sociedad jerárquica perfecta, pero la realidad del mestizaje superó cualquier intento de control.",
        "A finales del siglo dieciocho, este mundo superpuesto de castas y privilegios mostraba signos evidentes de agotamiento estructural."
    ],
    "b1-sociedadcolonial.json": [
        "La América hispana se estructuró en virreinatos gobernados por virreyes y audiencias que aplicaban las leyes dictadas desde Madrid.",
        "La sociedad colonial instauró una estricta jerarquía de castas dominada por españoles peninsulares en detrimento de los criollos y mestizos.",
        "La Iglesia católica dominaba la educación, la moral y la economía territorial a través de sus órdenes religiosas y parroquias.",
        "Las ciudades virreinales florecieron con plazas regulares, acueductos y un dinámico comercio callejero protagonizado por el pueblo llano.",
        "Bajo la aparente calma de los ritos religiosos, el descontento criollo y la complejidad del mestizaje preparaban el terreno para futuros cambios."
    ],

    # =========================================================================
    # UNIT 06: economiacolonial
    # =========================================================================
    "b1-economiacolonial-01-plataoro.json": [
        "Potosí, 1600. A más de cuatro mil metros de altura, el Cerro Rico albergaba el mayor yacimiento de plata del mundo conocido.",
        "Miles de trabajadores eran forzados a extraer el mineral en túneles asfixiantes y oscuros donde no llegaba la luz del sol.",
        "El mercurio utilizado en el beneficio de la plata era extremadamente tóxico y arruinaba la salud de los mineros en pocos años.",
        "Cualquier temblor en la montaña provocaba derrumbes catastróficos que sepultaban a cuadrillas enteras bajo las rocas.",
        "Durante el auge minero, la plata se usó para acuñar millones de monedas que comenzaron a circular por los mercados de todo el planeta."
    ],
    "b1-economiacolonial-02-trabajo.json": [
        "Para garantizar la mano de obra minera y agrícola, la Corona decidió conceder mercedes de tierra y encomiendas a los conquistadores.",
        "La mita era un sistema rotativo de trabajo obligatorio. Las autoridades decidieron sustituir viejas costumbres por turnos forzados en las minas.",
        "Los corregidores solían convocar a miles de indígenas de provincias enteras para cumplir con su servicio en pleno invierno.",
        "Los mitayos vivían en pleno sometimiento y subordinación a las órdenes del capataz colonial.",
        "El vencedor europeo imponía sus reglas sin piedad, obligando a las comunidades a recurrir a sus últimos ahorros comunales para subsistir."
    ],
    "b1-economiacolonial-03-plantaciones.json": [
        "En las costas tropicales del Caribe y de Brasil, la riqueza no venía de los metales, sino del cultivo de la caña de azúcar.",
        "El modelo se basaba en el monocultivo intensivo a gran escala, procesado en un complejo ingenio azucarero con grandes hornos de leña.",
        "El colapso de la población nativa llevó al rápido reemplazo de trabajadores mediante el brutal tráfico de esclavos africanos.",
        "Los terratenientes lograron acumular una inmensa fortuna vendiendo azúcar y tabaco de primera calidad a las metrópolis europeas.",
        "La gran finca esclavista se convirtió en la unidad económica fundamental de la economía costera colonial americana."
    ],
    "b1-economiacolonial-04-comercio.json": [
        "Para proteger las riquezas coloniales de los asaltos en alta mar, la Corona española creó el sistema de flotas y galeones.",
        "Cada año, convoyes armados navegaban juntos por el Atlántico para evitar que cualquier pirata audaz interceptara los lingotes de plata.",
        "El monopolio comercial fomentó un gigantesco mercado de contrabando practicado con la abierta complicidad de comerciantes y funcionarios locales.",
        "Desde las Filipinas, el Galeón de Manila cruzaba el océano Pacífico cargado de lujosa seda oriental, especias finas y porcelana china.",
        "Las potencias rivales como Inglaterra y Holanda intentaban constantemente rivalizar con España por el control de estas fabulosas rutas marinas."
    ],
    "b1-economiacolonial-05-precio.json": [
        "La fabulosa masa de metales preciosos extraída de América provocó un fenómeno económico inédito en los mercados del Viejo Mundo.",
        "La plata americana financió las guerras imperiales de los monarcas españoles, pero no pudo evitar que la Corona cayera en la deuda.",
        "La avalancha de monedas desató una fuerte inflación de precios en toda Europa, debilitando la manufactura nacional castellana.",
        "En América, el rápido ascenso del hacendado local le permitió acaparar las mejores tierras agrícolas y el agua de riego.",
        "Fueron los campesinos indígenas y los esclavos africanos quienes tuvieron que soportar el costo más pesado de este engranaje mercantil global."
    ],
    "b1-economiacolonial.json": [
        "La economía colonial americana estuvo estructurada en torno a la extracción minera masiva de plata en centros como Potosí y Zacatecas.",
        "Sistemas de trabajo forzoso como la mita y la encomienda diezmaron a las comunidades indígenas en beneficio de la Corona y los encomenderos.",
        "En las regiones cálidas florecieron las grandes plantaciones azucareras y cacaoteras sostenidas por la inhumana trata de esclavos africanos.",
        "El estricto monopolio comercial español intentó controlar todo el tráfico mediante convoyes de flotas, pero desató un enorme contrabando rival.",
        "La riqueza americana transformó las finanzas de Europa, pero dejó en el continente un legado de explotación y desigualdades extremas."
    ]
}

def update_stories():
    updated = 0
    for filename, paragraph_texts in STORIES.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        new_paragraphs = [{"type": "narration", "text": text} for text in paragraph_texts]
        data["paragraphs"] = new_paragraphs

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        updated += 1

    print(f"Total Block 1 stories successfully re-authored: {updated}/36")

if __name__ == "__main__":
    update_stories()
