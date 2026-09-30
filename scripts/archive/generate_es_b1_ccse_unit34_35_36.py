#!/usr/bin/env python3
"""Generate Spain CCSE B1 Units 34, 35, and 36 (Transporte y Emergencias 112, Consumo y Banca, Simulacro General CCSE)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict


UNIT_34 = {
    "unit_num": 70,
    "slug": "transporte",
    "title": "Transporte, Comunicaciones y Emergencias 112",
    "theme": "Red ferroviaria (RENFE, AVE y ADIF), aeropuertos (AENA), puertos, carreteras radiales, Correos y Protección Civil 112 en España (Tarea 5 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "El ferrocarril en España: RENFE, la alta velocidad (AVE) y ADIF",
            "objective": "Conocer la organización del transporte ferroviario en España (RENFE y ADIF) y el liderazgo mundial y europeo de la red de Alta Velocidad Española (AVE).",
            "grammar_title": "Superlativos de infraestructura y red («la red de alta velocidad más extensa de Europa»)",
            "grammar_slug": "superlativos-infraestructura-ferroviaria-ave",
            "grammar_Body": """Para describir la red de transporte público en el examen CCSE se emplean **construcciones superlativas** y verbos de conexión espacial (**unir, conectar, enlazar**):

- *España posee **la red de trenes de alta velocidad (AVE) más extensa de la Unión Europea** y la segunda del mundo.*
- ***ADIF** construye y mantiene las vías y estaciones, mientras que **RENFE** opera los trenes de viajeros y mercancías.*""",
            "story_title": "A trescientos kilómetros por hora por la península",
            "paragraphs": [
                "El ferrocarril constituye uno de los grandes emblemas de la modernización de las infraestructuras en España. Desde la inauguración en 1992 de la primera línea de Alta Velocidad Española (AVE) entre Madrid y Sevilla con motivo de la Exposición Universal, España ha construido más de cuatro mil kilómetros de vías de alta velocidad, convirtiéndose en el país con la red de alta velocidad más extensa de toda Europa y el segundo del mundo después de China.",
                "En el sector público ferroviario español, dependiente del Ministerio de Transportes y Movilidad Sostenible, existen dos grandes entidades públicas empresariales con funciones complementarias: por un lado, ADIF (Administrador de Infraestructuras Ferroviarias), que es el organismo encargado de construir, mantener y gestionar las vías férreas, la electrificación y las estaciones de tren; y por otro lado, RENFE (Red Nacional de los Ferrocarriles Españoles), que es la compañía pública que opera los trenes de pasajeros y mercancías.",
                "Los trenes de alta velocidad de RENFE (AVE y Avlo, junto con otros operadores como Ouigo e Iryo tras la liberalización ferroviaria) circulan a velocidades comerciales de hasta trescientos diez kilómetros por hora (310 km/h), conectando Madrid con Barcelona, Valencia, Alicante, Sevilla, Málaga, Córdoba, Zaragoza, Valladolid, León, Ourense, Oviedo, Murcia o Granada en pocas horas.",
                "Para los desplazamientos diarios de millones de trabajadores y estudiantes entre las grandes capitales y los municipios de su área metropolitana, el servicio más utilizado es la red de trenes de «Cercanías» (llamada «Rodalies» en Cataluña), complementada por los trenes regionales de Media Distancia y los ferrocarriles de vía estrecha del norte peninsular.",
                "Además, el Gobierno de España y las comunidades autónomas impulsan abonos de transporte recurrentes y descuentos para jóvenes, familias numerosas y personas mayores de sesenta años (a través de la «Tarjeta Dorada» de RENFE) con el fin de fomentar una movilidad sostenible y reducir las emisiones contaminantes."
            ],
            "questions": [
                ("¿Cómo se llaman los trenes de alta velocidad de RENFE en España, cuya red es la más extensa de Europa?", ["AVE (Alta Velocidad Española)", "TGV francés", "ITV", "BOE"], 0),
                ("¿Cuál es la compañía pública española tradicional encargada de operar los trenes de pasajeros (Cercanías, Media Distancia y AVE)?", ["RENFE", "AENA", "AEMET", "SEPE"], 0),
                ("¿Qué organismo público español construye, mantiene y gestiona las vías del tren y las estaciones ferroviarias?", ["ADIF (Administrador de Infraestructuras Ferroviarias)", "La Dirección General de Tráfico", "El Instituto Cervantes", "Patrimonio Nacional"], 0)
            ],
            "vocab": [
                ("el AVE", "noun", "Spanish High-Speed Train (Alta Velocidad Española)", "El AVE conecta Madrid y Barcelona en apenas dos horas y media."),
                ("RENFE", "noun", "National Network of Spanish Railways (state train operator)", "RENFE opera los trenes de Cercanías, Media Distancia, Alvia y AVE."),
                ("ADIF", "noun", "Railway Infrastructure Administrator (tracks and stations)", "Las grandes estaciones de tren españolas están gestionadas por ADIF."),
                ("el tren de Cercanías", "noun", "commuter / suburban train (Rodalies in Catalonia)", "Millones de trabajadores utilizan a diario el tren de Cercanías para ir al centro."),
                ("la Tarjeta Dorada", "noun", "RENFE senior/disability discount card (for ages 60+)", "Las personas mayores de sesenta años viajan con descuento gracias a la Tarjeta Dorada."),
                ("la alta velocidad", "noun", "high-speed rail", "España cuenta con la red ferroviaria de alta velocidad más larga de Europa."),
                ("el andén", "noun", "station platform", "Los viajeros esperan la llegada del tren detrás de la línea amarilla del andén."),
                ("la movilidad sostenible", "noun", "sustainable mobility", "El transporte público ferroviario es clave para la movilidad sostenible.")
            ],
            "ex_mc": [
                ("¿En qué año se inauguró la primera línea del tren de alta velocidad (AVE) en España, uniendo las ciudades de Madrid y Sevilla?", ["En 1992", "En 1812", "En 1936", "En 2020"], 0),
                ("¿Cómo se llaman los trenes que conectan diariamente el centro de una gran ciudad española con los pueblos y ciudades de su área metropolitana?", ["Trenes de Cercanías (o Rodalies en Cataluña)", "Transatlánticos", "Teleféricos alpinos", "Tranvías de vapor"], 0)
            ],
            "ex_fb": [
                ("La compañía pública española que opera los trenes de viajeros y de alta velocidad se llama ___.", "RENFE", "The Spanish public company that operates passenger and high-speed trains is called RENFE."),
                ("Las siglas ___ significan Alta Velocidad Española y designan a los trenes más rápidos del país.", "AVE", "The acronym AVE stands for Spanish High Speed and designates the fastest trains in the country.")
            ],
            "ex_sb": [
                (["España", "tiene", "la", "mayor", "red", "de", "alta", "velocidad", "de", "Europa."], "Spain has the largest high-speed rail network in Europe.")
            ],
            "ex_dict": [
                ("RENFE opera los trenes de Cercanías y de Alta Velocidad Española en todo el país.", "RENFE operates commuter trains and Spanish High-Speed trains throughout the country.")
            ]
        },
        {
            "num": "02",
            "title": "Aeropuertos (AENA) y Puertos del Estado",
            "objective": "Identificar a AENA como gestora de la red de aeropuertos españoles, conocer los principales aeropuertos (Madrid-Barajas y Barcelona-El Prat) y la red de Puertos del Estado.",
            "grammar_title": "Construcciones apositivas para denominaciones oficiales de infraestructuras",
            "grammar_slug": "apositivas-denominaciones-aeropuertos-aena",
            "grammar_Body": """Los grandes aeropuertos y puertos españoles llevan a menudo una **aposición con el nombre de figuras históricas o culturales**:

- *El **Aeropuerto Adolfo Suárez Madrid-Barajas** es el de mayor tráfico aéreo de España.*
- *El **Aeropuerto Josep Tarradellas Barcelona-El Prat** ocupa el segundo lugar nacional.*
- *La sociedad **AENA** gestiona cuarenta y seis aeropuertos y dos helipuertos de interés general en España.*""",
            "story_title": "Puertas aéreas y marítimas entre tres continentes",
            "paragraphs": [
                "Por su situación geográfica estratégica entre Europa, África y América, así como por su condición de potencia turística mundial y contar con dos archipiélagos (Baleares y Canarias), el transporte aéreo y marítimo desempeña un papel vital en la cohesión territorial y económica de España.",
                "La entidad encargada de gestionar los cuarenta y seis aeropuertos públicos y los dos helipuertos de interés general en España es AENA (Aeropuertos Españoles y Navegación Aérea), el primer operador aeroportuario del mundo por volumen de pasajeros, mientras que la entidad pública ENAIRE se encarga del control del tráfico y la navegación aérea.",
                "El aeropuerto con mayor número de pasajeros y vuelos internacionales del país es el Aeropuerto Adolfo Suárez Madrid-Barajas, principal centro de conexión aérea entre Europa e Iberoamérica. Le siguen en volumen de tráfico el Aeropuerto Josep Tarradellas Barcelona-El Prat, el Aeropuerto de Palma de Mallorca, el Aeropuerto de Málaga-Costa del Sol, el Aeropuerto de Alicante-Elche Miguel Hernández y los grandes aeropuertos canarios de Gran Canaria y Tenerife Sur.",
                "Para garantizar la igualdad de todos los españoles en el derecho a la movilidad, el Estado subvenciona con un descuento del setenta y cinco por ciento (75 %) el precio de los billetes de avión y de barco de los ciudadanos residentes en las Islas Canarias, las Islas Baleares, Ceuta y Melilla en sus viajes con el resto del territorio nacional.",
                "En el ámbito marítimo, el organismo público Puertos del Estado coordina las veintiocho Autoridades Portuarias que administran cuarenta y seis puertos de interés general. Entre ellos destacan el Puerto de Bahía de Algeciras (Cádiz), el Puerto de Valencia y el Puerto de Barcelona —líderes del Mediterráneo en tráfico de contenedores y cruceros—, junto con los puertos de Bilbao, Las Palmas y Santa Cruz de Tenerife."
            ],
            "questions": [
                ("¿Qué empresa de mayoría pública gestiona la red de aeropuertos de interés general en España?", ["AENA (Aeropuertos Españoles y Navegación Aérea)", "RENFE", "ADIF", "ONCE"], 0),
                ("¿Cuál es el aeropuerto con mayor tráfico de pasajeros de España y cómo se llama oficialmente?", ["El Aeropuerto Adolfo Suárez Madrid-Barajas", "El Aeropuerto de Salamanca", "El Aeropuerto de Burgos", "El Aeropuerto de Huesca"], 0),
                ("¿Qué porcentaje de descuento estatal en los billetes de avión y barco hacia el resto de España tienen por ley los residentes en Canarias, Baleares, Ceuta y Melilla?", ["Un descuento del 75 %", "Un descuento del 5 %", "Ningún descuento", "Solo un 1 % en invierno"], 0)
            ],
            "vocab": [
                ("AENA", "noun", "Spanish Airports and Air Navigation (airport operator)", "AENA gestiona cuarenta y seis aeropuertos públicos y dos helipuertos en España."),
                ("Puertos del Estado", "noun", "State Ports agency (Ministry of Transport)", "Puertos del Estado coordina los grandes puertos comerciales y de pasajeros."),
                ("el descuento de residente", "noun", "resident travel discount (75% for islands, Ceuta, and Melilla)", "Con el certificado de empadronamiento se aplica el descuento de residente del setenta y cinco por ciento."),
                ("la tarjeta de embarque", "noun", "boarding pass", "Para subir al avión es necesario mostrar la tarjeta de embarque y el DNI o pasaporte."),
                ("el tráfico aéreo", "noun", "air traffic", "Madrid-Barajas y Barcelona-El Prat concentran la mayor parte del tráfico aéreo español."),
                ("el helipuerto", "noun", "heliport", "Ceuta y Algeciras están conectadas de forma regular mediante un helipuerto de AENA."),
                ("el ferri", "noun", "ferry / passenger ship", "Numerosos ferris conectan diariamente la península con Baleares, Canarias, Ceuta y Melilla."),
                ("el crucero", "noun", "cruise ship", "El puerto de Barcelona es uno de los principales puertos base de cruceros del mundo.")
            ],
            "ex_mc": [
                ("¿Con qué presidente del Gobierno de la Transición española está bautizado oficialmente el Aeropuerto de Madrid-Barajas?", ["Adolfo Suárez (Aeropuerto Adolfo Suárez Madrid-Barajas)", "Felipe González", "José María Aznar", "Leopoldo Calvo-Sotelo"], 0),
                ("¿Cuál de estos puertos españoles es uno de los mayores puertos de mercancías y contenedores de todo el mar Mediterráneo?", ["El Puerto de Bahía de Algeciras (junto con los de Valencia y Barcelona)", "El puerto fluvial de Aranjuez", "El puerto deportivo de Navacerrada", "El embalse de Sanabria"], 0)
            ],
            "ex_fb": [
                ("La entidad encargada de gestionar los aeropuertos públicos españoles se conoce por las siglas ___.", "AENA", "The entity responsible for managing Spanish public airports is known by the acronym AENA."),
                ("El aeropuerto con mayor número de viajeros de España es el Aeropuerto Adolfo Suárez ___-Barajas.", "Madrid", "The airport with the highest number of passengers in Spain is Adolfo Suárez Madrid-Barajas Airport.")
            ],
            "ex_sb": [
                (["AENA", "gestiona", "la", "red", "de", "aeropuertos", "públicos", "de", "España."], "AENA manages the network of public airports in Spain.")
            ],
            "ex_dict": [
                ("Los residentes en Canarias, Baleares, Ceuta y Melilla tienen descuento en el transporte aéreo y marítimo.", "Residents of the Canary Islands, Balearic Islands, Ceuta, and Melilla receive a discount on air and sea transport.")
            ]
        },
        {
            "num": "03",
            "title": "La red de carreteras (autovías A-1 a A-6) y el transporte público urbano",
            "objective": "Conocer la estructura radial de las carreteras del Estado (Kilómetro Cero en la Puerta del Sol y autovías A-1 a A-6), los límites de velocidad y el transporte metropolitano.",
            "grammar_title": "Nomenclatura alfanumérica vial y límites normativos («autovías gratuitas A-», «autopistas de peaje AP-», «120 km/h»)",
            "grammar_slug": "nomenclatura-vial-limites-velocidad-autovias",
            "grammar_Body": """Para responder a las preguntas del CCSE sobre carreteras y circulación es preciso conocer las siglas viales y los límites generales de velocidad de la DGT:

- **Autovías (A-1 a A-6)**: vías de doble calzada de uso público y **gratuitas**, con origen radial en el **Kilómetro Cero de la Puerta del Sol de Madrid**.
- **Autopistas (AP-)**: vías de alta capacidad (algunas con **peaje**).
- **Límites generales de velocidad para turismos**: **120 km/h** en autovías y autopistas; **90 km/h** en carreteras convencionales; y **30 km/h o 50 km/h** en vías urbanas según el número de carriles.""",
            "story_title": "Del Kilómetro Cero de la Puerta del Sol a todos los rincones",
            "paragraphs": [
                "La Red de Carreteras del Estado en España se caracteriza históricamente por una estructura radial cuyo punto de partida simbólico y geográfico se encuentra en el centro de Madrid: la placa del «Kilómetro Cero» situada en la acera de la Puerta del Sol, frente a la Real Casa de Correos.",
                "Desde Madrid parten las seis grandes autovías radiales nacionales numeradas en el sentido de las agujas del reloj de la A-1 a la A-6: la A-1 (Autovía del Norte, hacia Burgos, Vitoria y San Sebastián), la A-2 (Autovía del Nordeste, hacia Zaragoza y Barcelona), la A-3 (Autovía del Este, hacia Valencia), la A-4 (Autovía del Sur o de Andalucía, hacia Córdoba, Sevilla y Cádiz), la A-5 (Autovía del Suroeste, hacia Extremadura y Lisboa) y la A-6 (Autovía del Noroeste, hacia Valladolid, Lugo y A Coruña).",
                "A esta red radial se suman grandes ejes transversales como la Autovía del Mediterráneo (A-7, desde Algeciras hasta la frontera francesa por toda la costa levantina y catalana), la Autovía del Cantábrico (A-8, por el norte) y la Autovía Ruta de la Plata (A-66, de Gijón a Sevilla). En España, las «autovías» (identificadas con la letra A-) son siempre gratuitas, mientras que algunas «autopistas» (identificadas con las letras AP-) pueden requerir el pago de un peaje.",
                "De acuerdo con el Reglamento General de Circulación de la DGT, el límite máximo general de velocidad para automóviles turismos y motocicletas en autovías y autopistas es de ciento veinte kilómetros por hora (120 km/h); en carreteras convencionales fuera de poblado es de noventa kilómetros por hora (90 km/h); y dentro de las ciudades es de treinta kilómetros por hora (30 km/h) en calles de un solo carril por sentido y de cincuenta kilómetros por hora (50 km/h) en avenidas de dos o más carriles.",
                "Dentro de las grandes ciudades españolas, los ciudadanos disponen de modernas redes de transporte público colectivo integradas mediante tarjetas recargables y abonos mensuales: redes de Metro (subterráneo en Madrid, Barcelona, Valencia, Bilbao, Sevilla, Málaga, Palma y Granada), tranvías, autobuses urbanos de bajas emisiones y sistemas públicos municipales de alquiler de bicicletas eléctricas como BiciMAD en Madrid o Bicing en Barcelona."
            ],
            "questions": [
                ("¿En qué plaza de Madrid se encuentra la famosa placa del «Kilómetro Cero», punto de origen de las seis grandes carreteras radiales de España?", ["En la Puerta del Sol", "En la Plaza de Oriente", "En la Plaza de Castilla", "En la Glorieta de Atocha"], 0),
                ("¿Cuál es el límite máximo general de velocidad permitido en España para coches turismos y motocicletas cuando circulan por autovías y autopistas?", ["120 kilómetros por hora (120 km/h)", "160 kilómetros por hora", "80 kilómetros por hora", "No existe límite de velocidad"], 0),
                ("¿Qué diferencia existe en España entre una «autovía» (A-) y una «autopista de peaje» (AP-)?", ["Las autovías son de uso público gratuito y en las autopistas de peaje hay que abonar una tarifa por circular", "Por las autovías solo pueden circular bicicletas", "Las autopistas son caminos de tierra sin asfaltar", "No hay ninguna carretera gratuita en España"], 0)
            ],
            "vocab": [
                ("el Kilómetro Cero", "noun", "Kilometer Zero (origin milestone of Spain's radial roads in Puerta del Sol)", "La placa del Kilómetro Cero en la Puerta del Sol marca el inicio de las carreteras radiales."),
                ("la autovía", "noun", "free dual-carriageway highway (A-1, A-2, etc.)", "Las autovías españolas cuentan con al menos dos carriles por sentido y son gratuitas."),
                ("la autopista de peaje", "noun", "toll motorway (AP-)", "En las autopistas de peaje el conductor abona un importe por el uso de la vía."),
                ("el límite de velocidad", "noun", "speed limit (120 km/h on highways, 90 km/h on conventional roads, 30/50 in town)", "En las autovías españolas el límite de velocidad para turismos es de ciento veinte kilómetros por hora."),
                ("el abono transporte", "noun", "public transport travel pass (monthly/annual)", "El abono transporte permite viajar de forma ilimitada en metro, autobús y cercanías."),
                ("el cinturón de seguridad", "noun", "seatbelt (mandatory in all seats)", "El uso del cinturón de seguridad es obligatorio en todos los asientos del vehículo."),
                ("la Zona de Bajas Emisiones", "noun", "Low Emission Zone (ZBE in cities over 50,000 inhabitants)", "Las ciudades de más de cincuenta mil habitantes cuentan con Zonas de Bajas Emisiones."),
                ("el distintivo ambiental", "noun", "DGT environmental vehicle sticker (Cero, Eco, C, B)", "La DGT clasifica los vehículos según sus emisiones mediante el distintivo ambiental.")
            ],
            "ex_mc": [
                ("¿Es obligatorio llevar abrochado el cinturón de seguridad en los asientos traseros de un coche en España, así como el casco al circular en motocicleta?", ["Sí, el cinturón es obligatorio en todos los asientos (delanteros y traseros) y el casco es siempre obligatorio en moto", "Solo es obligatorio para el conductor en viajes largos", "En los asientos traseros es voluntario", "Solo cuando llueve"], 0),
                ("¿Cuál es la velocidad máxima permitida dentro de las ciudades españolas en las calles que tienen un único carril por sentido de circulación?", ["30 km/h", "100 km/h", "120 km/h", "70 km/h"], 0)
            ],
            "ex_fb": [
                ("El origen de las seis carreteras radiales de España (el Kilómetro Cero) se encuentra en la Puerta del ___ de Madrid.", "Sol", "The origin of Spain's six radial roads (Kilometer Zero) is located in the Puerta del Sol in Madrid."),
                ("La velocidad máxima permitida para un coche turismo en las autovías y autopistas de España es de ___ km/h.", "120", "The maximum speed allowed for a passenger car on dual carriageways and motorways in Spain is 120 km/h.")
            ],
            "ex_sb": [
                (["El", "Kilómetro", "Cero", "se", "encuentra", "en", "la", "Puerta", "del", "Sol."], "Kilometer Zero is located in the Puerta del Sol.")
            ],
            "ex_dict": [
                ("En las autovías y autopistas españolas la velocidad máxima es de ciento veinte kilómetros por hora.", "On Spanish dual carriageways and motorways the maximum speed is one hundred and twenty kilometers per hour.")
            ]
        },
        {
            "num": "04",
            "title": "Correos, códigos postales y telecomunicaciones en España",
            "objective": "Conocer el funcionamiento de la Sociedad Estatal Correos y Telégrafos, la estructura de cinco dígitos del código postal español (01 a 52) y el prefijo telefónico internacional (+34).",
            "grammar_title": "Expresiones de codificación numérica territorial («cinco dígitos», «prefijo internacional más treinta y cuatro»)",
            "grammar_slug": "codificacion-numerica-postal-telefonica",
            "grammar_Body": """En las preguntas prácticas de comunicaciones del examen CCSE destacan tres datos numéricos esenciales:

- **El código postal español**: consta de **cinco dígitos (5 cifras)**. Los **dos primeros dígitos (del 01 al 52)** identifican la **provincia** (por orden alfabético histórico, p. ej. 28 Madrid, 08 Barcelona, 41 Sevilla, 51 Ceuta, 52 Melilla).
- **El prefijo telefónico internacional de España**: es el **+34** (o 0034).
- **Los números de teléfono en España**: tienen **nueve cifras (9 dígitos)**; los fijos comienzan por **9 u 8** y los móviles por **6 o 7**.""",
            "story_title": "Cinco cifras para cada destino y una red que llega a todas partes",
            "paragraphs": [
                "El servicio postal universal en todo el territorio nacional —incluidas las aldeas rurales más pequeñas y las islas— está garantizado por la Sociedad Estatal Correos y Telégrafos, conocida por todos los ciudadanos como «Correos», una empresa cien por cien pública fundada hace más de trescientos años y fácilmente identificable por el color amarillo de sus buzones y su logotipo con la cornamusa coronada.",
                "En las oficinas de Correos no solo se envían y reciben cartas ordinarias, cartas certificadas, paquetes y giros postales, sino que también se realiza un trámite fundamental para la democracia española: la solicitud y el envío gratuito del «voto por correo» en todas las elecciones generales, autonómicas, municipales y europeas, además de funcionar como registro administrativo oficial para enviar documentos a cualquier ministerio o ayuntamiento (mediante el sistema ORVE).",
                "Para clasificar la correspondencia, España utiliza desde 1984 un «código postal» formado por cinco dígitos numéricos (5 cifras). Los dos primeros dígitos (del 01 al 52) identifican siempre la provincia española o ciudad autónoma a la que pertenece la dirección: por ejemplo, todos los códigos postales de la provincia de Madrid empiezan por 28 (como 28001), los de Barcelona por 08, los de Valencia por 46, los de Sevilla por 41, los de Ceuta por 51 y los de Melilla por 52.",
                "En el ámbito de las telecomunicaciones, España es el país de la Unión Europea con mayor cobertura de fibra óptica hasta el hogar (FTTH) y redes móviles 5G. Para llamar a España desde el extranjero es necesario marcar el prefijo telefónico internacional español: el +34 (o 0034).",
                "Dentro de España, todos los números de teléfono ordinarios constan de nueve cifras (9 dígitos): los teléfonos fijos geográficos comienzan siempre por el número 9 o el 8 (seguidos del código de cada provincia, como 91 en Madrid o 93 en Barcelona), los teléfonos móviles comienzan por el 6 o por el 7, y los números que comienzan por 900 u 800 son siempre de llamada totalmente gratuita para el ciudadano."
            ],
            "questions": [
                ("¿De cuántos números consta el código postal en España y qué indican sus dos primeras cifras?", ["Consta de 5 números (cinco dígitos) y sus dos primeras cifras indican la provincia (del 01 al 52)", "Consta de 2 letras y 1 número", "Consta de 10 números elegidos al azar por cada vecino", "En España no existen códigos postales"], 0),
                ("¿Cuál es el prefijo telefónico internacional que hay que marcar para llamar por teléfono a España desde cualquier otro país?", ["+34 (o 0034)", "+44", "+1", "+55"], 0),
                ("¿Dónde se solicita y envía gratuitamente el voto por correo cuando un ciudadano no puede acudir en persona al colegio electoral el día de las elecciones?", ["En cualquier oficina de Correos", "En las farmacias de guardia", "En los talleres mecánicos", "En las taquillas del cine"], 0)
            ],
            "vocab": [
                ("Correos", "noun", "Spanish State Postal Service (Sociedad Estatal Correos y Telégrafos)", "En las oficinas de Correos se puede tramitar gratuitamente el voto por correo."),
                ("el código postal", "noun", "postal / ZIP code (5 digits in Spain; first 2 = province)", "El código postal español tiene cinco cifras y las dos primeras indican la provincia."),
                ("el prefijo internacional", "noun", "international telephone dialing code (+34 for Spain)", "El prefijo internacional de España para llamadas desde el exterior es el más treinta y cuatro."),
                ("la carta certificada", "noun", "registered letter (with official proof of delivery)", "La carta certificada deja constancia legal de la fecha de entrega al destinatario."),
                ("el buzón", "noun", "postbox / mailbox (yellow on Spanish streets)", "Las cartas con sello pueden depositarse en los buzones amarillos de Correos."),
                ("el teléfono fijo", "noun", "landline telephone (9 digits starting with 9 or 8)", "Los números de teléfono fijo en España tienen nueve cifras y empiezan por nueve u ocho."),
                ("el teléfono móvil", "noun", "mobile / cell phone (9 digits starting with 6 or 7)", "Los números de teléfono móvil en España tienen nueve dígitos y empiezan por seis o siete."),
                ("la fibra óptica", "noun", "fiber-optic internet", "España lidera en Europa el despliegue de redes de fibra óptica de alta velocidad.")
            ],
            "ex_mc": [
                ("Si un número de teléfono de atención al cliente en España empieza por el prefijo 900 (o 800), ¿qué coste tiene la llamada para el ciudadano?", ["Es una llamada totalmente gratuita", "Cuesta cinco euros por minuto", "Es un número internacional fuera de Europa", "Solo funciona por fax"], 0),
                ("¿Por qué números empiezan los códigos postales de la provincia de Madrid y de la provincia de Barcelona?", ["Los de Madrid empiezan por 28 y los de Barcelona por 08", "Todos los códigos postales de España empiezan por 99", "Madrid empieza por 00 y Barcelona por 77", "Empiezan por letras romanas"], 0)
            ],
            "ex_fb": [
                ("El código postal en España está formado por ___ dígitos y los dos primeros identifican la provincia.", "cinco", "The postal code in Spain is made up of five digits and the first two identify the province."),
                ("El prefijo telefónico internacional para llamar a España desde otro país es el +___.", "34", "The international telephone prefix to call Spain from another country is +34.")
            ],
            "ex_sb": [
                (["El", "código", "postal", "español", "está", "formado", "por", "cinco", "cifras."], "The Spanish postal code is made up of five digits.")
            ],
            "ex_dict": [
                ("El voto por correo se solicita y se envía gratuitamente desde cualquier oficina de Correos.", "Postal voting is requested and sent free of charge from any Post Office.")
            ]
        },
        {
            "num": "05",
            "title": "Protección Civil, AEMET y los teléfonos de atención ciudadana (112, 016, 060)",
            "objective": "Conocer el sistema de Protección Civil, los avisos meteorológicos de la AEMET y los principales teléfonos públicos gratuitos de emergencia y atención ciudadana en España (112, 016, 060, 011, 024).",
            "grammar_title": "Relación funcional de números abreviados de servicio público («el 112 para emergencias», «el 016 contra la violencia de género»)",
            "grammar_slug": "numeros-abreviados-servicio-publico-emergencias",
            "grammar_Body": """El examen CCSE pregunta con frecuencia por los **teléfonos públicos cortos y gratuitos** de atención e intervención en España:

- **112**: Teléfono único europeo de **emergencias** (sanitarias, bomberos, policía, salvamento).
- **091**: Policía Nacional | **062**: Guardia Civil | **092**: Policía Local.
- **016**: Información y atención a víctimas de **violencia de género** (gratuito, 24 h y **no deja rastro en la factura telefónica**).
- **060**: Información de la **Administración General del Estado** | **010**: Información municipal de los ayuntamientos.
- **024**: Línea de atención a la conducta suicida y salud mental.""",
            "story_title": "Una red permanente de alerta, información y auxilio ciudadano",
            "paragraphs": [
                "Para proteger la vida de las personas y los bienes frente a catástrofes naturales —como inundaciones, incendios forestales, nevadas intensas o erupciones volcánicas—, España cuenta con el Sistema Nacional de Protección Civil, coordinado por el Ministerio del Interior junto con las comunidades autónomas, los ayuntamientos, los cuerpos de bomberos y la Unidad Militar de Emergencias (UME) de las Fuerzas Armadas.",
                "Un organismo científico fundamental para anticiparse a los riesgos climáticos es la Agencia Estatal de Meteorología (AEMET), adscrita al Ministerio para la Transición Ecológica. La AEMET elabora diariamente la predicción del tiempo para todos los municipios españoles y emite avisos meteorológicos oficiales clasificados en tres niveles de riesgo por colores: nivel amarillo (riesgo moderado), nivel naranja (riesgo importante) y nivel rojo (riesgo extremo).",
                "Ante cualquier emergencia real que requiera la intervención inmediata de una ambulancia, de los bomberos, de Salvamento Marítimo o de las fuerzas de seguridad, el ciudadano debe marcar el número único de emergencias 112, gratuito incluso desde teléfonos móviles sin saldo o bloqueados. Además, existen teléfonos directos específicos para la Policía Nacional (091), la Guardia Civil (062) y la Policía Local o Municipal (092).",
                "Dentro de los teléfonos sociales de protección de los derechos fundamentales destaca el 016, servicio público telefónico de información, asesoramiento jurídico y atención psicosocial inmediata para víctimas de violencia de género. El teléfono 016 es totalmente gratuito, funciona las 24 horas en más de cincuenta idiomas, es accesible para personas con discapacidad auditiva y tiene una característica vital de seguridad: las llamadas al 016 no dejan rastro en la factura telefónica.",
                "Por último, para realizar consultas administrativas sin tratarse de una emergencia, los ciudadanos disponen del teléfono 060 para cualquier gestión con la Administración General del Estado (ministerios, DGT, DNI, becas), del teléfono 010 para información municipal de su ayuntamiento y del 011 para información sobre el estado del tráfico en las carreteras."
            ],
            "questions": [
                ("¿Cuál es el teléfono público y gratuito en España que ofrece información y ayuda las 24 horas a las víctimas de violencia de género sin dejar rastro en la factura telefónica?", ["El 016", "El 060", "El 011", "El 1004"], 0),
                ("¿Qué número de teléfono debe marcar un ciudadano para obtener información general sobre trámites y servicios de la Administración General del Estado (ministerios, DNI, DGT)?", ["El 060", "El 112", "El 091", "El 062"], 0),
                ("¿Qué agencia estatal elabora la predicción oficial del tiempo en España y emite los avisos amarillos, naranjas y rojos por fenómenos meteorológicos adversos?", ["La Agencia Estatal de Meteorología (AEMET)", "La Agencia Tributaria (AEAT)", "La Agencia Española de Protección de Datos (AEPD)", "El Instituto Nacional de las Artes Escénicas"], 0)
            ],
            "vocab": [
                ("el 112", "noun", "112 single European emergency number (medical, fire, police)", "El teléfono 112 coordina todas las emergencias sanitarias, de bomberos y policiales."),
                ("el 016", "noun", "016 helpline for victims of gender-based violence (leaves no trace on bill)", "El teléfono 016 atiende a las víctimas de violencia de género y no deja rastro en la factura."),
                ("el 060", "noun", "060 General State Administration information telephone number", "El teléfono 060 informa sobre trámites con los ministerios de la Administración General del Estado."),
                ("la AEMET", "noun", "State Meteorological Agency (Agencia Estatal de Meteorología)", "La AEMET emite avisos naranjas y rojos ante lluvias torrenciales o fuertes olas de calor."),
                ("Protección Civil", "noun", "Civil Protection emergency system", "Los voluntarios de Protección Civil colaboran en los dispositivos de seguridad de los municipios."),
                ("la Unidad Militar de Emergencias", "noun", "Military Emergencies Unit (UME)", "La Unidad Militar de Emergencias interviene en grandes incendios forestales e inundaciones."),
                ("el aviso meteorológico", "noun", "weather warning (yellow, orange, or red alert)", "Un aviso meteorológico de color rojo de la AEMET indica riesgo extremo para la población."),
                ("el 010", "noun", "010 municipal citizen information telephone number (town halls)", "Para consultar horarios e impuestos del ayuntamiento se puede llamar al teléfono municipal 010.")
            ],
            "ex_mc": [
                ("¿Qué color utiliza la Agencia Estatal de Meteorología (AEMET) para indicar el nivel de «riesgo extremo» ante un fenómeno meteorológico muy peligroso?", ["El color rojo (nivel rojo)", "El color verde claro", "El color blanco", "El color rosa"], 0),
                ("¿Qué números directos corresponden específicamente a la Policía Nacional y a la Guardia Civil en España (además del número general 112)?", ["El 091 para la Policía Nacional y el 062 para la Guardia Civil", "El 010 y el 060", "El 900 y el 800", "El 001 y el 002"], 0)
            ],
            "ex_fb": [
                ("El número de teléfono de atención a las víctimas de violencia de género, gratuito y que no deja rastro en la factura, es el ___.", "016", "The telephone number for assistance to victims of gender violence, free and leaving no trace on the bill, is 016."),
                ("El teléfono de información general de la Administración General del Estado es el ___.", "060", "The general information telephone number for the General State Administration is 060.")
            ],
            "ex_sb": [
                (["El", "teléfono", "cero", "dieciséis", "atiende", "a", "las", "víctimas", "de", "violencia", "de", "género."], "The 016 telephone number assists victims of gender violence.")
            ],
            "ex_dict": [
                ("La Agencia Estatal de Meteorología elabora la predicción oficial del tiempo en toda España.", "The State Meteorological Agency prepares the official weather forecast throughout Spain.")
            ]
        }
    ]
}


UNIT_35 = {
    "unit_num": 71,
    "slug": "consumobanca",
    "title": "Consumo, Horarios y Servicios Bancarios",
    "theme": "El euro, el Banco de España, cuentas bancarias (IBAN ES y Bizum), horarios comerciales, derechos del consumidor (hoja de reclamaciones y garantía de 3 años) y ONG en España (Tarea 5 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "El euro, el Banco de España y los servicios bancarios cotidianos (IBAN y Bizum)",
            "objective": "Conocer la moneda oficial de España (el euro desde 2002), el papel del Banco de España y el funcionamiento de las cuentas bancarias (IBAN ES), domiciliaciones y Bizum.",
            "grammar_title": "Léxico financiero y bancario cotidiano («domiciliar un recibo», «código IBAN que empieza por ES»)",
            "grammar_slug": "lexico-financiero-bancario-iban-domiciliacion",
            "grammar_Body": """Para desenvolverse en los servicios bancarios españoles y en el examen CCSE es fundamental conocer estas expresiones:

- **El euro (€)**: moneda oficial de España (en circulación física desde el **1 de enero de 2002**, en sustitución de la **peseta**).
- **El código IBAN de una cuenta española**: comienza siempre por las dos letras **ES** seguidas de **22 dígitos** (24 caracteres en total).
- **Domiciliar la nómina o los recibos**: autorizar que el sueldo se ingrese automáticamente o que las facturas de luz, agua e impuestos se cobren directamente en la cuenta bancaria.""",
            "story_title": "De la peseta al euro y los pagos instantáneos en el móvil",
            "paragraphs": [
                "La moneda oficial de España es el euro (€), compartida con los demás países que integran la eurozona de la Unión Europea. El euro sustituyó a la histórica moneda nacional española —la peseta, creada en 1868— y sus billetes y monedas comenzaron a circular físicamente en los bolsillos de los españoles el 1 de enero del año 2002. Cada euro se divide en cien céntimos (con ocho monedas de 1, 2, 5, 10, 20 y 50 céntimos, y de 1 y 2 euros, y siete billetes de 5, 10, 20, 50, 100, 200 y 500 euros).",
                "La institución pública que actúa como banco central nacional y supervisa la solvencia y el correcto funcionamiento de las entidades financieras en España es el Banco de España, con sede histórica en la Plaza de Cibeles de Madrid e integrado en el Sistema Europeo de Bancos Centrales dirigido por el Banco Central Europeo (BCE). Además, el Fondo de Garantía de Depósitos protege los ahorros de cada titular en cuentas bancarias hasta un límite de cien mil euros (100.000 €) por entidad.",
                "En la vida diaria española, abrir una cuenta corriente o de ahorro en un banco (presentando el DNI, NIE o pasaporte) es esencial para recibir el salario, cobrar pensiones o prestaciones y pagar el alquiler y los impuestos. Toda cuenta bancaria en España se identifica mediante el código internacional IBAN, que en España consta siempre de veinticuatro caracteres (24 caracteres): las dos letras «ES» al inicio seguidas de veintidós números.",
                "La forma más cómoda y habitual de pagar las facturas mensuales del hogar (luz, agua, gas, teléfono, cuota de la comunidad de vecinos o el IBI del ayuntamiento) es la «domiciliación bancaria», mediante la cual el titular autoriza al banco a abonar automáticamente esos recibos con cargo a su cuenta.",
                "Junto con las tarjetas de débito y de crédito y los cajeros automáticos, en España se ha universalizado «Bizum», un sistema gratuito e instantáneo creado por la banca española que permite enviar dinero de una cuenta a otra en segundos entre amigos o pagar en comercios utilizando únicamente el número de teléfono móvil."
            ],
            "questions": [
                ("¿Cuál es la moneda oficial de España y en qué año empezaron a circular físicamente sus billetes y monedas sustituyendo a la peseta?", ["El euro (€), que empezó a circular físicamente el 1 de enero de 2002", "El dólar europeo, desde 1978", "El real de vellón, desde 1992", "La corona ibérica, desde 2010"], 0),
                ("¿Por qué dos letras comienza siempre el código internacional IBAN de todas las cuentas bancarias abiertas en España?", ["Por las letras ES (seguidas de 22 dígitos)", "Por las letras SP", "Por las letras EU", "Por las letras MA"], 0),
                ("¿Qué significa en España la expresión cotidiana «domiciliar un recibo» (como el de la luz o el agua)?", ["Dar orden al banco para que pague automáticamente esa factura cargándola en nuestra cuenta bancaria", "Recibir la factura en un sobre de papel dentro del buzón de casa", "Pagar en monedas en la puerta del edificio", "Pedir que nos perdonen el pago de la factura"], 0)
            ],
            "vocab": [
                ("el euro", "noun", "the euro (€, Spain's official currency since 2002)", "El euro entró en circulación física en España el uno de enero de dos mil dos."),
                ("la peseta", "noun", "the peseta (Spain's former currency from 1868 to 2002)", "Antes de la llegada del euro, la moneda oficial de España era la peseta."),
                ("el Banco de España", "noun", "Bank of Spain (national central bank, integrated into the Eurosystem)", "El Banco de España supervisa a los bancos y forma parte del Eurosistema."),
                ("el código IBAN", "noun", "International Bank Account Number (24 characters starting with ES in Spain)", "El código IBAN de una cuenta española empieza siempre por las letras ES."),
                ("la domiciliación bancaria", "noun", "direct debit (automatic payment of bills from a bank account)", "La mayoría de los hogares paga la luz y el agua mediante domiciliación bancaria."),
                ("el cajero automático", "noun", "ATM / cash machine", "Con la tarjeta de débito se puede retirar dinero en efectivo en el cajero automático."),
                ("la cuenta corriente", "noun", "checking / current bank account", "Para cobrar la nómina mensual es necesario ser titular de una cuenta corriente."),
                ("el extracto bancario", "noun", "bank statement", "El extracto bancario muestra todos los ingresos y pagos realizados en el mes.")
            ],
            "ex_mc": [
                ("¿Cómo se llamaba la moneda oficial de España antes de la implantación del euro en el año 2002?", ["La peseta", "El escudo", "El marco", "El franco"], 0),
                ("¿Cuál es la institución bancaria central de España cuya sede principal se encuentra frente a la fuente de Cibeles en Madrid?", ["El Banco de España", "El Tribunal de Cuentas", "La Bolsa de Comercio de Bilbao", "La Tesorería Municipal"], 0)
            ],
            "ex_fb": [
                ("La moneda oficial de España es el ___, cuyos billetes y monedas circulan desde el año 2002.", "euro", "Spain's official currency is the euro, whose banknotes and coins have been in circulation since 2002."),
                ("El código IBAN de cualquier cuenta bancaria española comienza siempre por las dos letras ___.", "ES", "The IBAN code of any Spanish bank account always starts with the two letters ES.")
            ],
            "ex_sb": [
                (["El", "euro", "es", "la", "moneda", "oficial", "de", "España", "desde", "dos", "mil", "dos."], "The euro has been the official currency of Spain since two thousand and two.")
            ],
            "ex_dict": [
                ("La domiciliación bancaria permite pagar automáticamente los recibos de luz, agua y teléfono.", "Direct debit allows electricity, water, and telephone bills to be paid automatically.")
            ]
        },
        {
            "num": "02",
            "title": "Horarios comerciales, rebajas y costumbres cotidianas en España",
            "objective": "Conocer los horarios habituales del comercio y los bancos en España (horario continuo frente a horario partido) y la diferencia horaria de Canarias (una hora menos).",
            "grammar_title": "Contraste horario y husos horarios («horario partido», «horario continuo», «una hora menos en Canarias»)",
            "grammar_slug": "contraste-horario-partido-continuo-canarias",
            "grammar_Body": """Para describir los horarios comerciales y administrativos en España se distinguen dos modalidades y dos husos horarios oficiales:

- **Horario continuo (o intensivo)**: sin pausa al mediodía (p. ej. centros comerciales y supermercados de **10:00 a 21:30/22:00 h**, o sucursales bancarias y oficinas públicas de **08:30 a 14:00/14:30 h**).
- **Horario partido**: comercios tradicionales de barrio que abren por la mañana (**10:00 a 14:00 h**), cierran a mediodía y vuelven a abrir por la tarde (**17:00 a 20:30 h**).
- **Huso horario**: en la comunidad autónoma de **Canarias siempre es una hora menos** que en la España peninsular, Baleares, Ceuta y Melilla.""",
            "story_title": "El ritmo del día en las calles y comercios españoles",
            "paragraphs": [
                "Comprender los horarios de apertura de las tiendas, los bancos y las oficinas públicas facilita enormemente la adaptación a la vida diaria en España. En las ciudades españolas conviven dos grandes tipos de horario comercial: el «horario continuo» de las grandes superficies y el «horario partido» del pequeño comercio tradicional.",
                "Los grandes almacenes, los centros comerciales y las cadenas de supermercados e hipermercados abren en horario continuo e ininterrumpido desde las nueve o diez de la mañana hasta las nueve y media o diez de la noche (09:30 / 10:00 a 21:30 / 22:00 h), de lunes a sábado (y en zonas de gran afluencia turística o en comunidades como Madrid, también muchos domingos y festivos).",
                "Por el contrario, las pequeñas tiendas de barrio (zapaterías, librerías, ferreterías, peluquerías o tiendas de ropa) suelen tener «horario partido»: abren por la mañana de 10:00 a 14:00 horas, cierran al mediodía durante las horas de la comida y de mayor calor en verano, y vuelven a abrir por la tarde de 17:00 a 20:30 horas de lunes a viernes y los sábados por la mañana.",
                "En cuanto a las sucursales bancarias y las oficinas de atención presencial de las administraciones públicas (ayuntamientos, Hacienda, Seguridad Social), su horario habitual de atención al público es de mañana, generalmente de lunes a viernes entre las 08:30 y las 14:00 o 14:30 horas (aunque algunos bancos y registros abren también una tarde a la semana en invierno y hoy en día casi todas las gestiones requieren solicitar cita previa).",
                "Finalmente, todo residente en España debe recordar un dato geográfico y horario fundamental que aparece en todos los avisos de radio y televisión («son las diez de la mañana, las nueve en Canarias»): debido a su situación geográfica en el océano Atlántico, el archipiélago de las Islas Canarias se rige por el huso horario occidental (WET/GMT) y tiene siempre exactamente una hora menos que la España peninsular, las Islas Baleares, Ceuta y Melilla."
            ],
            "questions": [
                ("Si en Madrid, Barcelona, Palma de Mallorca o Ceuta son las 12:00 del mediodía, ¿qué hora oficial es en ese mismo instante en las Islas Canarias?", ["Las 11:00 de la mañana (una hora menos)", "Las 13:00 de la tarde (una hora más)", "Las 12:00 exactamente igual", "Las 06:00 de la mañana"], 0),
                ("¿En qué franja horaria suelen atender al público de forma presencial la mayoría de las sucursales bancarias y oficinas administrativas en España?", ["Por la mañana, habitualmente de lunes a viernes entre las 08:30 y las 14:00 o 14:30 horas", "Solo de madrugada entre las 02:00 y las 05:00 horas", "Únicamente los domingos por la tarde", "De 20:00 a 24:00 horas"], 0),
                ("¿Qué diferencia existe entre el «horario continuo» de los centros comerciales y el «horario partido» de muchas tiendas pequeñas de barrio?", ["El horario continuo permanece abierto al mediodía (de 10:00 a 21:30/22:00 h) y el horario partido cierra al mediodía (de 14:00 a 17:00 h) para volver a abrir por la tarde", "El horario continuo solo abre un día al mes", "El horario partido solo vende la mitad de los productos", "Son exactamente lo mismo"], 0)
            ],
            "vocab": [
                ("el horario continuo", "noun", "continuous / uninterrupted opening hours (no midday closure)", "Los supermercados y centros comerciales abren en horario continuo de diez a diez."),
                ("el horario partido", "noun", "split schedule (morning and afternoon with a midday break)", "Muchas tiendas tradicionales de barrio tienen horario partido y cierran de dos a cinco."),
                ("una hora menos en Canarias", "noun", "one hour behind in the Canary Islands (WET time zone)", "En todos los programas de radio se recuerda que es una hora menos en Canarias."),
                ("la sucursal bancaria", "noun", "bank branch", "Las sucursales bancarias atienden al público principalmente en horario de mañana."),
                ("las rebajas", "noun", "seasonal sales (traditionally starting in January and July)", "Las grandes campañas de rebajas comerciales en España tienen lugar en invierno y en verano."),
                ("el centro comercial", "noun", "shopping mall / shopping center", "El centro comercial reúne tiendas, supermercados, cines y restaurantes bajo un mismo techo."),
                ("el pequeño comercio", "noun", "small local / neighborhood retail shop", "El pequeño comercio de proximidad da vida y seguridad a las calles de los barrios."),
                ("el día laborable", "noun", "working day / weekday", "Las oficinas administrativas abren al público durante los días laborables de lunes a viernes.")
            ],
            "ex_mc": [
                ("¿En qué dos épocas del año se celebran tradicionalmente las grandes campañas de «rebajas» con descuentos en las tiendas de ropa y comercios de España?", ["En invierno (a partir de enero, tras el Día de Reyes) y en verano (a partir de julio)", "Solo el día 29 de febrero", "Únicamente el Martes Santo", "En España están prohibidas las rebajas"], 0),
                ("¿Cuántos husos horarios oficiales existen en el territorio nacional de España?", ["Dos husos horarios: el horario central europeo (península, Baleares, Ceuta y Melilla) y el horario de Canarias (una hora menos)", "Cinco husos horarios distintos", "Uno para cada una de las 17 comunidades autónomas", "Diez husos horarios"], 0)
            ],
            "ex_fb": [
                ("En la comunidad autónoma de las Islas ___ siempre es una hora menos que en la península y Baleares.", "Canarias", "In the autonomous community of the Canary Islands it is always one hour earlier than on the mainland and the Balearic Islands."),
                ("Las tiendas tradicionales que abren de 10:00 a 14:00 y de 17:00 a 20:30 tienen horario ___.", "partido", "Traditional shops that open from 10:00 to 14:00 and from 17:00 to 20:30 have split opening hours (horario partido).")
            ],
            "ex_sb": [
                (["En", "las", "Islas", "Canarias", "siempre", "es", "una", "hora", "menos."], "In the Canary Islands it is always one hour earlier.")
            ],
            "ex_dict": [
                ("Los grandes centros comerciales abren en horario continuo desde las diez de la mañana hasta las diez de la noche.", "Large shopping centers open continuously from ten in the morning until ten at night.")
            ]
        },
        {
            "num": "03",
            "title": "Derechos del consumidor: ticket de compra, garantía de 3 años y Hojas de Reclamaciones",
            "objective": "Conocer los derechos legales de los consumidores en España (art. 51 CE): la garantía legal de tres años para productos nuevos, el desistimiento de 14 días en compras por internet y las Hojas de Reclamaciones.",
            "grammar_title": "Construcciones de derecho y garantía del consumidor («tener una garantía legal de tres años», «disponer de hojas de reclamaciones»)",
            "grammar_slug": "derechos-garantia-consumidor-reclamaciones",
            "grammar_Body": """La Ley General para la Defensa de los Consumidores y Usuarios en España establece garantías muy claras que suelen preguntarse en el CCSE:

- **Garantía legal de productos nuevos**: todos los bienes duraderos nuevos (electrodomésticos, móviles, coches, ordenadores) tienen en España una **garantía legal obligatoria de 3 años (tres años)** desde su entrega.
- **Derecho de desistimiento en compras a distancia / por internet**: el consumidor dispone de **14 días naturales** para devolver el producto sin necesidad de justificar el motivo.
- **Hojas de Reclamaciones**: todos los comercios y empresas de servicios **están obligados a tenerlas a disposición del cliente**.""",
            "story_title": "Consumidores protegidos en las tiendas y en internet",
            "paragraphs": [
                "El artículo 51 de la Constitución Española ordena a los poderes públicos garantizar la defensa de los consumidores y usuarios, protegiendo mediante procedimientos eficaces su seguridad, su salud y sus legítimos intereses económicos. En España, esta competencia la ejercen conjuntamente el Ministerio de Derechos Sociales, Consumo y Agenda 2030, las direcciones generales de consumo de las comunidades autónomas y las Oficinas Municipales de Información al Consumidor (OMIC) de los ayuntamientos.",
                "Al realizar cualquier compra o contratar un servicio, el primer derecho básico del ciudadano es exigir el «ticket de compra», recibo o factura simplificada, donde deben constar la fecha, el nombre y NIF del establecimiento, el precio total con el IVA incluido y los productos adquiridos. Conservar el ticket o factura es imprescindible para poder cambiar un artículo o hacer valer la garantía.",
                "Desde el año 2022, España cuenta con una de las legislaciones más avanzadas de Europa en protección al comprador: todos los productos nuevos de carácter duradero (como un teléfono móvil, un televisor, una lavadora o un automóvil) tienen por ley una «garantía legal de tres años» (3 años) a partir de la fecha de entrega. Si el producto presenta un defecto de fabricación durante ese plazo, la empresa está obligada a repararlo gratuitamente, sustituirlo por otro nuevo, rebajar el precio o devolver el dinero.",
                "En las compras realizadas por internet, por teléfono o fuera de un establecimiento comercial, el consumidor goza además del «derecho legal de desistimiento», que le permite devolver el producto en un plazo mínimo de catorce días naturales (14 días) desde que lo recibe en casa, sin penalización y sin necesidad de explicar el motivo.",
                "Si surge un conflicto en una tienda, bar, hotel o taller y el cliente considera vulnerados sus derechos, todos los establecimientos abiertos al público en España tienen la obligación legal de poseer y entregar de inmediato y gratuitamente las «Hojas de Reclamaciones» oficiales (compuestas por tres copias: una para la administración de consumo, otra para el consumidor y otra para el comercio)."
            ],
            "questions": [
                ("¿De cuántos años es la garantía legal obligatoria para todos los productos nuevos duraderos (como un electrodoméstico o un ordenador) comprados en España?", ["De 3 años", "De 3 meses únicamente", "De 15 días", "En España no existe garantía obligatoria"], 0),
                ("¿Qué documento oficial están obligados a tener y entregar gratuitamente todos los comercios, bares y empresas de servicios en España si un cliente desea presentar una queja formal ante la administración de consumo?", ["La Hoja de Reclamaciones oficial", "El testamento notarial", "La papeleta del Senado", "El libro de familia"], 0),
                ("Cuando se realiza una compra por internet o a distancia en España, ¿de cuántos días naturales dispone como mínimo el consumidor para ejercer su derecho legal de desistimiento y devolver el producto sin dar explicaciones?", ["De 14 días naturales", "De 2 horas solamente", "De 10 años", "En internet está prohibido devolver productos"], 0)
            ],
            "vocab": [
                ("la Hoja de Reclamaciones", "noun", "official Consumer Complaint Form (mandatory in all shops and bars)", "Todos los establecimientos están obligados a entregar la Hoja de Reclamaciones si el cliente la pide."),
                ("la garantía legal", "noun", "statutory warranty (3 years for new durable goods in Spain)", "Los electrodomésticos y móviles nuevos tienen una garantía legal de tres años en España."),
                ("el ticket de compra", "noun", "purchase receipt / sales slip", "Es necesario guardar el ticket de compra o la factura para ejercer la garantía."),
                ("el derecho de desistimiento", "noun", "right of withdrawal (14 calendar days for online/distance purchases)", "En las compras por internet el cliente tiene catorce días de derecho de desistimiento."),
                ("la OMIC", "noun", "Municipal Consumer Information Office (Oficina Municipal de Información al Consumidor)", "El ciudadano puede presentar su Hoja de Reclamaciones en la OMIC de su ayuntamiento."),
                ("el consumidor", "noun", "consumer", "El artículo cincuenta y uno de la Constitución protege los derechos de los consumidores."),
                ("el etiquetado", "noun", "product labeling (must appear at least in Spanish)", "El etiquetado de los alimentos debe indicar los ingredientes, alérgenos y fecha de caducidad."),
                ("el arbitraje de consumo", "noun", "consumer arbitration (free extrajudicial dispute resolution)", "El Sistema Arbitral de Consumo resuelve conflictos entre clientes y empresas de forma gratuita y rápida.")
            ],
            "ex_mc": [
                ("¿Qué significan las siglas municipales OMIC, presentes en los ayuntamientos españoles para defender a los compradores?", ["Oficina Municipal de Información al Consumidor", "Organización Marítima Internacional de Cruceros", "Oficina Meteorológica de las Islas Canarias", "Ordenanza de Museos de Interés Cultural"], 0),
                ("Si el dueño de un bar o de una tienda se niega a entregar la Hoja de Reclamaciones oficial a un cliente que la solicita, ¿qué puede hacer el cliente?", ["Llamar a la Policía Local o Municipal para que acuda al local y levante acta de la negativa", "Nada, porque tener Hojas de Reclamaciones es voluntario", "Acudir al Tribunal Constitucional directamente", "Pedir permiso al banco"], 0)
            ],
            "ex_fb": [
                ("Si un cliente quiere presentar una queja oficial en un comercio o restaurante, tiene derecho a pedir la ___ de Reclamaciones.", "Hoja", "If a customer wants to file an official complaint in a shop or restaurant, they have the right to ask for the Complaint Form (Hoja de Reclamaciones)."),
                ("En España, todos los productos nuevos duraderos cuentan con una ___ legal de tres años.", "garantía", "In Spain, all new durable goods come with a statutory three-year warranty.")
            ],
            "ex_sb": [
                (["Todos", "los", "comercios", "deben", "tener", "Hojas", "de", "Reclamaciones", "a", "disposición", "del", "público."], "All shops must have Complaint Forms available to the public.")
            ],
            "ex_dict": [
                ("En España los productos nuevos tienen una garantía legal obligatoria de tres años.", "In Spain new products have a mandatory legal warranty of three years.")
            ]
        },
        {
            "num": "04",
            "title": "Impuestos al consumo (IVA, IGIC, IPSI) y medios de comunicación en España",
            "objective": "Repasar los impuestos indirectos al consumo en España (IVA en península y Baleares, IGIC en Canarias, IPSI en Ceuta y Melilla) y conocer los principales medios públicos y privados de comunicación (RTVE, Agencia EFE).",
            "grammar_title": "Distribución territorial de impuestos indirectos y siglas de medios públicos («RTVE», «Agencia EFE»)",
            "grammar_slug": "impuestos-indirectos-medios-comunicacion-rtve",
            "grammar_Body": """Para el examen CCSE conviene relacionar los **impuestos indirectos al consumo** con su territorio y conocer los **medios públicos de comunicación**:

- **IVA (Impuesto sobre el Valor Añadido)**: se aplica en la **Península e Islas Baleares** (tipo general 21 %, reducido 10 %, superreducido 4 %).
- **IGIC (Impuesto General Indirecto Canario)**: sustituye al IVA en las **Islas Canarias** (con tipos más bajos, general del 7 %).
- **IPSI**: sustituye al IVA en las ciudades autónomas de **Ceuta y Melilla**.
- **RTVE (Corporación de Radio y Televisión Española)**: radiotelevisión pública estatal (*La 1, La 2, Canal 24 Horas, Radio Nacional de España - RNE*). **Agencia EFE**: principal agencia de noticias en español del mundo.""",
            "story_title": "Precios con impuestos incluidos y pluralismo informativo",
            "paragraphs": [
                "Cada vez que un ciudadano compra un libro, toma un café en una terraza o adquiere ropa en una tienda española, el precio final que marca la etiqueta incluye ya por ley el impuesto indirecto sobre el consumo. En la España peninsular y en las Islas Baleares este tributo es el Impuesto sobre el Valor Añadido (IVA), que cuenta con tres tipos impositivos: el tipo general del 21 % (para la mayoría de bienes y servicios), el tipo reducido del 10 % (para alimentos elaborados, transporte de viajeros, hostelería y hoteles) y el tipo superreducido del 4 % (para bienes de primera necesidad como pan, leche, huevos, fruta, verdura, medicamentos y libros).",
                "Debido a sus regímenes económicos y fiscales especiales por su lejanía o situación geográfica, existen tres territorios españoles donde no se aplica el IVA: en las Islas Canarias se aplica el Impuesto General Indirecto Canario (IGIC, cuyo tipo general es mucho más bajo, en torno al 7 %), y en las ciudades autónomas de Ceuta y Melilla se aplica el Impuesto sobre la Producción, los Servicios y la Importación (IPSI).",
                "Por otro lado, en una sociedad democrática y avanzada como la española, los ciudadanos se informan diariamente a través de una amplia variedad de medios de comunicación públicos y privados garantizados por el derecho a la libertad de expresión e información (artículo 20 de la Constitución).",
                "El servicio público estatal de radio y televisión está encomendado a la Corporación de Radio y Televisión Española (RTVE), que emite para todo el país y el extranjero a través de cadenas de televisión como La 1, La 2, Teledeporte, Clan (infantil) y el Canal 24 Horas, así como las emisoras de Radio Nacional de España (RNE) y la plataforma digital gratuita RTVE Play. Además, muchas comunidades autónomas cuentan con su propia radiotelevisión pública autonómica (como TV3 en Cataluña, Canal Sur en Andalucía, Telemadrid, TVG en Galicia o ETB en el País Vasco).",
                "Junto a los grandes grupos audiovisuales privados (Atresmedia con Antena 3 y La Sexta; Mediaset con Telecinco y Cuatro; cadenas de radio como la SER, COPE u Onda Cero; y diarios históricos como El País, El Mundo, ABC, La Vanguardia o La Voz de Galicia), España cuenta con la «Agencia EFE», fundada en 1939, que es la primera agencia internacional de noticias en lengua española y la cuarta más grande del mundo."
            ],
            "questions": [
                ("¿Cómo se llama la corporación pública estatal que gestiona los canales públicos nacionales de televisión (La 1, La 2, Canal 24 Horas) y Radio Nacional de España (RNE)?", ["RTVE (Corporación de Radio y Televisión Española)", "AENA", "RENFE", "SEPE"], 0),
                ("¿Cuál es la principal agencia internacional de noticias de España y la primera agencia de noticias en lengua española del mundo?", ["La Agencia EFE", "La Agencia Estatal de Meteorología", "La Agencia Tributaria", "El Boletín Oficial del Registro Mercantil"], 0),
                ("¿Qué impuesto indirecto sobre el consumo sustituye al IVA en el archipiélago de las Islas Canarias?", ["El IGIC (Impuesto General Indirecto Canario)", "El IRPF", "El IBI", "La tasa de basuras"], 0)
            ],
            "vocab": [
                ("RTVE", "noun", "Spanish Public Radio and Television Corporation (La 1, La 2, RNE)", "RTVE es la corporación pública estatal de radio y televisión de España."),
                ("la Agencia EFE", "noun", "EFE News Agency (world's leading Spanish-language news agency)", "La Agencia EFE distribuye noticias en español a medios de comunicación de todo el mundo."),
                ("Radio Nacional de España", "noun", "Spanish National Radio (RNE, part of RTVE)", "Radio Nacional de España ofrece información y cultura sin anuncios publicitarios."),
                ("el IVA superreducido", "noun", "super-reduced VAT rate (4% for bread, milk, books, medicines)", "El pan, la leche, los libros y los medicamentos tienen un IVA superreducido del cuatro por ciento."),
                ("el IGIC", "noun", "Canary Islands General Indirect Tax (replaces VAT in the Canaries)", "En las tiendas de las Islas Canarias no se cobra el IVA, sino el IGIC."),
                ("el IPSI", "noun", "Tax on Production, Services and Importation (replaces VAT in Ceuta and Melilla)", "En las ciudades autónomas de Ceuta y Melilla se aplica el impuesto indirecto IPSI."),
                ("la libertad de prensa", "noun", "freedom of the press (Article 20 of the Constitution)", "El artículo veinte de la Constitución Española protege la libertad de prensa y prohíbe la censura previa."),
                ("la televisión autonómica", "noun", "regional public television broadcaster (e.g., Canal Sur, TV3, TVG, ETB)", "Las televisiones autonómicas promueven la cultura regional y las lenguas cooficiales.")
            ],
            "ex_mc": [
                ("¿Cuál de los siguientes canales de televisión pertenece a la radiotelevisión pública estatal española (RTVE)?", ["La 1 (y La 2 / Canal 24 Horas)", "Antena 3", "Telecinco", "La Sexta"], 0),
                ("¿Qué productos básicos disfrutan en España del tipo superreducido del 4 % de IVA?", ["Alimentos básicos (pan, leche, huevos, fruta, verdura), medicamentos y libros", "Coches deportivos de lujo y joyas", "Entradas de discoteca", "Bebidas alcohólicas de alta graduación"], 0)
            ],
            "ex_fb": [
                ("La corporación pública de radio y televisión de ámbito estatal en España se conoce por las siglas ___.", "RTVE", "The state-wide public radio and television corporation in Spain is known by the acronym RTVE."),
                ("La principal agencia internacional de noticias en lengua española del mundo es la Agencia ___.", "EFE", "The world's leading Spanish-language international news agency is the EFE Agency.")
            ],
            "ex_sb": [
                (["La", "Agencia", "EFE", "es", "la", "principal", "agencia", "de", "noticias", "en", "español."], "The EFE Agency is the main Spanish-language news agency.")
            ],
            "ex_dict": [
                ("Radio Televisión Española es el servicio público estatal de comunicación audiovisual.", "Spanish Radio and Television is the state public audiovisual media service.")
            ]
        },
        {
            "num": "05",
            "title": "Voluntariado, ONG, la ONCE, Cruz Roja y el Tercer Sector en España",
            "objective": "Reconocer la gran fortaleza solidaria del Tercer Sector en España: la ONCE (Organización Nacional de Ciegos Españoles), Cruz Roja Española, Cáritas, los Bancos de Alimentos y la casilla del 0,7 % de fines sociales en el IRPF.",
            "grammar_title": "Oraciones de finalidad social y solidaridad («destinar el 0,7 % a fines sociales», «integrar a personas con discapacidad»)",
            "grammar_slug": "finalidad-social-solidaridad-once-ong",
            "grammar_Body": """Para describir las organizaciones solidarias y del Tercer Sector en el examen CCSE se emplean estructuras de **finalidad social**:

- **La ONCE (Organización Nacional de Ciegos Españoles)**: corporación de derecho público de carácter social que promueve la **inclusión laboral y educativa de las personas ciegas y con discapacidad** (financiada mediante el tradicional **cupón de la ONCE**).
- **Cruz Roja Española, Cáritas y los Bancos de Alimentos**: grandes entidades humanitarias y de acción social.
- **La «X Solidaria» en la Declaración de la Renta (IRPF)**: permite al contribuyente destinar gratuitamente el **0,7 % de sus impuestos** a ONG de acción social y/o a la Iglesia Católica.""",
            "story_title": "El cupón de la solidaridad y el compromiso social de los españoles",
            "paragraphs": [
                "España destaca en las estadísticas europeas por el alto grado de compromiso solidario de su ciudadanía, articulado a través del llamado «Tercer Sector de Acción Social», integrado por cerca de treinta mil Organizaciones No Gubernamentales (ONG), fundaciones y asociaciones sin ánimo de lucro donde colaboran más de cuatro millones de voluntarios.",
                "Una institución española única en el mundo y profundamente querida por todos los ciudadanos es la ONCE (Organización Nacional de Ciegos Españoles), fundada en 1938. La ONCE es una corporación de derecho público de carácter social que garantiza la autonomía personal, la educación inclusiva (en braille y tecnologías adaptadas), el perro guía y el empleo digno de las personas ciegas o con deficiencia visual grave. A través de su Fundación ONCE y del grupo de empresas sociales Ilunion, es además el mayor empleador mundial de personas con todo tipo de discapacidad, financiándose gracias a la venta de sus famosos productos de lotería responsable, como el «cupón de la ONCE».",
                "Junto a la ONCE, desempeñan una labor humanitaria imprescindible en todos los municipios españoles organizaciones como Cruz Roja Española —que atiende emergencias sanitarias, socorrismo en playas, programas de empleo, ayuda a personas mayores solas y acogida de inmigrantes y refugiados—, Cáritas Española, Médicos Sin Fronteras, Manos Unidas y la Federación Española de Bancos de Alimentos (FESBAL), que organiza cada otoño la «Gran Recogida de Alimentos» en los supermercados.",
                "Los ciudadanos españoles también pueden colaborar con estas organizaciones sin que les cueste un solo euro adicional al hacer su Declaración anual de la Renta (IRPF): marcando la casilla de «Actividades de Interés General consideradas de Interés Social» (conocida como la «X Solidaria»), el Estado destina el 0,7 % de los impuestos de ese contribuyente a financiar proyectos de ONG para personas mayores, infancia, discapacidad y cooperación internacional (pudiendo marcarse simultáneamente con la casilla de la Iglesia Católica para aportar un 0,7 % a cada una).",
                "Esta red de solidaridad cotidiana, sumada al liderazgo mundial de España en donación altruista de sangre y de órganos, refleja los valores de convivencia, igualdad y apoyo mutuo que inspiran la ciudadanía española."
            ],
            "questions": [
                ("¿Qué es la ONCE en España y cuál es su misión principal?", ["La Organización Nacional de Ciegos Españoles, dedicada a la inclusión social, educativa y laboral de las personas ciegas y con discapacidad", "Un equipo de fútbol de once jugadores", "El canal público de televisión deportiva", "Un impuesto sobre las viviendas vacías"], 0),
                ("¿Qué porcentaje de sus impuestos puede decidir destinar gratuitamente un ciudadano a «Fines Sociales / ONG» (la llamada X Solidaria) al marcar la casilla correspondiente en su Declaración de la Renta (IRPF)?", ["El 0,7 % de su cuota íntegra del IRPF", "El 50 % de su sueldo", "Cien euros adicionales de su bolsillo", "El 21 % de IVA"], 0),
                ("¿Cuál de las siguientes organizaciones humanitarias realiza en España labores de socorrismo, emergencias, atención a mayores, refugiados y personas vulnerables?", ["Cruz Roja Española", "ADIF", "AENA", "El Registro Mercantil"], 0)
            ],
            "vocab": [
                ("la ONCE", "noun", "National Organization of Spanish Blind People", "La ONCE promueve la plena inclusión laboral y social de las personas ciegas y con discapacidad."),
                ("el cupón de la ONCE", "noun", "ONCE charity lottery ticket", "La venta del cupón de la ONCE financia miles de puestos de trabajo para personas con discapacidad."),
                ("Cruz Roja Española", "noun", "Spanish Red Cross", "Cruz Roja Española cuenta con cientos de miles de voluntarios en todas las provincias."),
                ("la ONG", "noun", "Non-Governmental Organization (Organización No Gubernamental)", "Las ONG desarrollan proyectos de acción social y cooperación al desarrollo sin ánimo de lucro."),
                ("el voluntariado", "noun", "volunteering / volunteer work", "La Ley del Voluntariado reconoce y apoya la labor solidaria de los ciudadanos."),
                ("el Banco de Alimentos", "noun", "Food Bank", "Los Bancos de Alimentos recogen comida no perecedera para distribuirla a familias vulnerables."),
                ("la X Solidaria", "noun", "the 0.7% Social Purposes checkbox on the Spanish income tax return", "Marcar la X Solidaria en la declaración de la renta no cuesta nada al contribuyente y ayuda a las ONG."),
                ("sin ánimo de lucro", "adjective", "non-profit", "Las fundaciones y asociaciones del Tercer Sector son entidades sin ánimo de lucro.")
            ],
            "ex_mc": [
                ("Si un ciudadano marca la casilla de Fines Sociales (0,7 %) en su declaración anual del IRPF, ¿tiene que pagar más impuestos o recibir menos devolución?", ["No, no paga nada más ni recibe menos devolución; simplemente decide que el 0,7 % de sus impuestos vaya a proyectos sociales de ONG", "Sí, le cobran un recargo de 500 euros", "Pierde el derecho a la deducción por maternidad", "Solo pueden marcarla las empresas extranjeras"], 0),
                ("¿Cómo se financia principalmente la labor social de la ONCE para crear empleo e integración para personas ciegas y con discapacidad en España?", ["Mediante la venta de su lotería social y responsable (el tradicional cupón de la ONCE)", "Mediante las multas de la Dirección General de Tráfico", "Con los peajes de las autopistas", "Con las tasas de los pasaportes"], 0)
            ],
            "ex_fb": [
                ("La ___ es la Organización Nacional de Ciegos Españoles, referente mundial en inclusión laboral de personas con discapacidad.", "ONCE", "ONCE is the National Organization of Spanish Blind People, a world benchmark in labor inclusion for people with disabilities."),
                ("En la Declaración de la Renta se puede marcar la casilla para destinar el 0,7 % de los impuestos a fines ___ y ONG.", "sociales", "On the Income Tax Return you can check the box to allocate 0.7% of taxes to social purposes and NGOs.")
            ],
            "ex_sb": [
                (["La", "ONCE", "fomenta", "la", "integración", "laboral", "de", "las", "personas", "con", "discapacidad."], "ONCE promotes the labor integration of people with disabilities.")
            ],
            "ex_dict": [
                ("Cruz Roja Española y la ONCE realizan una gran labor social en toda España.", "The Spanish Red Cross and ONCE carry out great social work throughout Spain.")
            ]
        }
    ]
}


UNIT_36 = {
    "unit_num": 72,
    "slug": "simulacro",
    "title": "Simulacro General de Examen CCSE",
    "theme": "Estructura oficial del examen CCSE del Instituto Cervantes (25 preguntas, 45 minutos, 60 % APTO) y repaso integrador de las 5 Tareas oficiales",
    "lessons": [
        {
            "num": "01",
            "title": "Estructura oficial del examen CCSE: 25 preguntas, 45 minutos y calificación APTO",
            "objective": "Conocer al detalle las normas oficiales del examen CCSE del Instituto Cervantes: número de preguntas (25), tiempo (45 minutos), porcentaje de cada bloque (60 % Gobierno/Leyes y 40 % Cultura/Sociedad), aciertos para aprobar (15 de 25 = 60 %) y validez del certificado (4 años).",
            "grammar_title": "Expresiones de proporción y requisito de superación («quince respuestas correctas sobre veinticinco», «calificación de APTO»)",
            "grammar_slug": "proporcion-requisito-superacion-examen-nacionalidad",
            "grammar_Body": """Para afrontar con total seguridad el día de la prueba oficial, conviene recordar las cifras clave del **examen CCSE administrado por el Instituto Cervantes**:

- **Total de preguntas**: **25 preguntas** cerradas (20 de selección múltiple con 3 opciones A/B/C y 5 de Verdadero/Falso) elegidas entre las 300 preguntas del manual anual.
- **Duración máxima**: **45 minutos**.
- **Distribución por bloques**: **60 % (15 preguntas)** sobre Gobierno, legislación y participación ciudadana (Tareas 1, 2 y 3) y **40 % (10 preguntas)** sobre Cultura, historia y sociedad española (Tareas 4 y 5).
- **Criterio de superación (APTO)**: responder correctamente al menos a **15 de las 25 preguntas (el 60 %)**. Las respuestas erróneas o en blanco **no restan puntos**.""",
            "story_title": "El día de la prueba ante el Instituto Cervantes",
            "paragraphs": [
                "La prueba de Conocimientos Constitucionales y Socioculturales de España (CCSE) es el examen oficial diseñado y administrado desde el año 2015 por el Instituto Cervantes —organismo público adscrito al Ministerio de Asuntos Exteriores— cuya superación es requisito obligatorio para los mayores de dieciocho años que solicitan la nacionalidad española por residencia o por origen sefardí.",
                "El examen CCSE se convoca diez veces al año (el último jueves de cada mes, excepto en los meses de agosto y diciembre, en los que no hay convocatoria) en cientos de centros de examen acreditados por el Instituto Cervantes tanto dentro de España como en el extranjero. En el momento de realizar la inscripción en línea en el portal oficial del Instituto Cervantes, cada candidato tiene derecho a hasta dos oportunidades (dos convocatorias de examen) por el pago de una única tasa de inscripción, en caso de que no supere la primera o no pueda presentarse.",
                "La estructura de la prueba es idéntica en todas las convocatorias: consta de veinticinco preguntas (25 preguntas) de respuesta cerrada que deben contestarse en un tiempo máximo de cuarenta y cinco minutos (45 minutos). Todas las preguntas proceden íntegramente de las trescientas preguntas oficiales publicadas cada año de forma abierta y gratuita en el Manual de preparación del Instituto Cervantes.",
                "Las 25 preguntas se dividen en dos grandes bloques temáticos: el sesenta por ciento de la prueba (60 %, es decir, 15 preguntas) evalúa conocimientos sobre el Gobierno, la legislación y la participación ciudadana en España (Tareas 1, 2 y 3); mientras que el cuarenta por ciento restante (40 %, es decir, 10 preguntas) evalúa conocimientos sobre la cultura, la historia y la sociedad española (Tareas 4 y 5).",
                "Cada respuesta acertada suma un punto (1 punto) y las respuestas incorrectas o dejadas en blanco no descuentan puntuación (0 puntos). Para obtener la calificación oficial de «APTO» es necesario acertar un mínimo de quince preguntas sobre las veinticinco (15 de 25, equivalente al 60 % de la prueba). Una vez obtenido, el certificado electrónico de haber resultado APTO en el examen CCSE tiene una validez de cuatro años (4 años) para presentar la solicitud de nacionalidad española ante el Ministerio de Justicia."
            ],
            "questions": [
                ("¿De cuántas preguntas consta el examen oficial CCSE del Instituto Cervantes y de cuánto tiempo disponen los candidatos para responderlas?", ["Consta de 25 preguntas y el tiempo máximo es de 45 minutos", "Consta de 100 preguntas en 3 horas", "Consta de 10 preguntas en 10 minutos", "Es un examen oral de dos días"], 0),
                ("¿Cuántas respuestas correctas como mínimo (sobre el total de 25 preguntas) son necesarias para aprobar el examen CCSE y obtener la calificación de APTO?", ["15 respuestas correctas (el 60 %)", "25 respuestas correctas obligatorias (el 100 %)", "5 respuestas correctas (el 20 %)", "22 respuestas correctas"], 0),
                ("¿Qué validez temporal tiene el certificado electrónico de haber resultado APTO en la prueba CCSE para presentar el expediente de nacionalidad española?", ["Tiene una validez de 4 años", "Caduca a las 24 horas del examen", "Solo vale durante 15 días", "Vale únicamente durante el mes de enero"], 0)
            ],
            "vocab": [
                ("la prueba CCSE", "noun", "Constitutional and Sociocultural Knowledge of Spain exam", "La prueba CCSE del Instituto Cervantes consta de veinticinco preguntas cerradas."),
                ("la calificación de APTO", "noun", "PASS grade (minimum 15 correct answers out of 25)", "Con quince respuestas correctas sobre veinticinco se obtiene la calificación de APTO."),
                ("la convocatoria", "noun", "official exam session (held every month except August and December)", "El pago de la inscripción da derecho a presentarse hasta en dos convocatorias."),
                ("el centro de examen acreditado", "noun", "accredited examination center (authorized by Instituto Cervantes)", "El candidato elige el centro de examen acreditado y el horario al inscribirse por internet."),
                ("la pregunta de selección múltiple", "noun", "multiple-choice question (3 options: A, B, C)", "Las tareas primera, tercera, cuarta y quinta contienen preguntas de selección múltiple con tres opciones."),
                ("verdadero o falso", "noun", "true or false question (Task 2 of the CCSE exam)", "La Tarea 2 del examen CCSE está formada por cinco preguntas de verdadero o falso."),
                ("el manual de preparación", "noun", "official preparation manual (300 published questions)", "El Instituto Cervantes publica gratuitamente el manual con las trescientas preguntas del año."),
                ("la dispensa de las pruebas", "noun", "official exemption / waiver from taking the exams (e.g. for ESO graduates in Spain or disabilities)", "Quienes han obtenido el título de la ESO en España pueden solicitar la dispensa de las pruebas CCSE y DELE.")
            ],
            "ex_mc": [
                ("Si un candidato falla una pregunta en el examen CCSE, ¿le quitan puntos de las preguntas que ya ha acertado?", ["No, las respuestas incorrectas o en blanco no restan puntos (valen 0 puntos, por lo que conviene responder siempre a las 25 preguntas)", "Sí, cada fallo resta tres puntos", "Sí, queda eliminado automáticamente al primer error", "Le restan medio punto por cada pregunta en blanco"], 0),
                ("¿En qué dos meses del año NO se celebran exámenes de la prueba CCSE?", ["En agosto y en diciembre", "En mayo y en junio", "En marzo y en abril", "En septiembre y en octubre"], 0)
            ],
            "ex_fb": [
                ("El examen CCSE consta de 25 preguntas y para obtener la calificación de APTO hay que acertar al menos ___ preguntas.", "15", "The CCSE exam consists of 25 questions and to obtain a PASS grade you must get at least 15 questions right."),
                ("El tiempo máximo para realizar la prueba oficial CCSE del Instituto Cervantes es de ___ minutos.", "45", "The maximum time to complete the official CCSE test of the Instituto Cervantes is 45 minutes.")
            ],
            "ex_sb": [
                (["Para", "aprobar", "el", "examen", "CCSE", "es", "necesario", "acertar", "quince", "preguntas."], "To pass the CCSE exam it is necessary to answer fifteen questions correctly.")
            ],
            "ex_dict": [
                ("La prueba del Instituto Cervantes consta de veinticinco preguntas y dura cuarenta y cinco minutos.", "The Instituto Cervantes test consists of twenty-five questions and lasts forty-five minutes.")
            ]
        },
        {
            "num": "02",
            "title": "Simulacro Tarea 1: Gobierno, legislación y participación ciudadana (10 preguntas del examen)",
            "objective": "Resolver con éxito las preguntas clave de la Tarea 1 del examen CCSE (10 preguntas de opción múltiple sobre la Constitución de 1978, la Corona, las Cortes Generales, el Gobierno, el Poder Judicial, las autonomías y la Unión Europea).",
            "grammar_title": "Precisión institucional en las atribuciones constitucionales («corresponde al Rey», «reside en el pueblo»)",
            "grammar_slug": "precision-institucional-atribuciones-tarea-uno",
            "grammar_Body": """En la **Tarea 1 del examen CCSE** (que aporta **10 de las 25 preguntas**, el 40 % de toda la prueba), la clave para no dudar entre las tres opciones (A, B, C) es asociar cada institución con su función constitucional exacta:

- **Soberanía nacional**: reside en el **pueblo español** (art. 1.2 CE).
- **Forma política del Estado**: **Monarquía parlamentaria** (art. 1.3 CE).
- **Jefe del Estado**: el **Rey (Felipe VI)**; arbitra y modera las instituciones, pero **no gobierna ni legisla**.
- **Poder Legislativo**: las **Cortes Generales** (Congreso de los Diputados y Senado).
- **Poder Ejecutivo**: el **Gobierno** (Presidente del Gobierno y ministros).
- **Poder Judicial**: jueces y magistrados, gobernados por el **CGPJ**, con el **Tribunal Supremo** en la cúspide jurisdiccional y el **Tribunal Constitucional** como intérprete supremo de la Constitución.""",
            "story_title": "Repaso maestro de las diez preguntas de Gobierno y Leyes",
            "paragraphs": [
                "La Tarea 1 es el bloque de mayor peso en el examen CCSE: incluye diez preguntas de selección múltiple (preguntas 1 a 10 del cuadernillo) con tres opciones de respuesta (A, B y C), de las cuales solo una es verdadera. Dominar esta tarea garantiza prácticamente dos tercios de los aciertos necesarios para aprobar la prueba.",
                "Todo parte de la Constitución Española, aprobada en referéndum por los españoles el 6 de diciembre de 1978 y sancionada el 27 de diciembre. Su artículo 1 define a España como un Estado social y democrático de Derecho que propugna como valores superiores la libertad, la justicia, la igualdad y el pluralismo político; afirma que la soberanía nacional reside en el pueblo español y establece que la forma política del Estado es la Monarquía parlamentaria.",
                "En cuanto a los símbolos e idiomas oficiales, la bandera de España consta de tres franjas horizontales (roja, amarilla y roja, siendo la amarilla de doble anchura que cada una de las rojas), el himno nacional es la Marcha Real (que no tiene letra oficial) y el castellano es la lengua española oficial del Estado, junto con las lenguas cooficiales en sus respectivas comunidades autónomas: catalán, valenciano, gallego, euskera o vasco y aranés.",
                "Respecto a la división de poderes, el Rey (Felipe VI) es el Jefe del Estado y mando supremo de las Fuerzas Armadas (su heredera es la Princesa de Asturias, Leonor); el poder legislativo reside en las Cortes Generales bicamerales (Congreso de los Diputados con 350 diputados y Senado como cámara de representación territorial), que aprueban las leyes y los Presupuestos Generales del Estado; el poder ejecutivo lo ejerce el Gobierno dirigido por el Presidente del Gobierno (con residencia oficial en el Palacio de la Moncloa, mientras que el Rey reside en el Palacio de la Zarzuela); y el poder judicial corresponde a jueces y magistrados independientes.",
                "Finalmente, la Tarea 1 incluye la organización territorial en 17 comunidades autónomas, 2 ciudades autónomas (Ceuta y Melilla), 50 provincias y más de 8.100 municipios gobernados por Ayuntamientos (alcalde y concejales), así como la pertenencia de España a la Unión Europea desde el 1 de enero de 1986, a la OTAN (1982) y a la ONU (1955)."
            ],
            "questions": [
                ("Según la Constitución Española de 1978, ¿cuál es la forma política del Estado español y en quién reside la soberanía nacional?", ["La forma política es la Monarquía parlamentaria y la soberanía nacional reside en el pueblo español", "Es una República federal y la soberanía reside en el Senado", "Es una Monarquía absoluta y la soberanía reside en el Gobierno", "Es un Principado y la soberanía reside en el Tribunal Supremo"], 0),
                ("¿Quién compone las Cortes Generales que ejercen el poder legislativo del Estado en España?", ["El Congreso de los Diputados y el Senado", "El Gobierno y el Consejo de Estado", "Los alcaldes y las diputaciones provinciales", "El Tribunal Constitucional y el Defensor del Pueblo"], 0),
                ("¿En qué fecha entró España a formar parte como Estado miembro de la Unión Europea (entonces Comunidad Económica Europea)?", ["El 1 de enero de 1986", "El 6 de diciembre de 1978", "El 12 de octubre de 1992", "El 2 de mayo de 1808"], 0)
            ],
            "vocab": [
                ("la Monarquía parlamentaria", "noun", "Parliamentary Monarchy (political form of the Spanish State, Art. 1.3 CE)", "La forma política del Estado español es la Monarquía parlamentaria."),
                ("la soberanía nacional", "noun", "national sovereignty (resides in the Spanish people, Art. 1.2 CE)", "La soberanía nacional reside en el pueblo español, del que emanan los poderes del Estado."),
                ("las Cortes Generales", "noun", "General Courts / Spanish Parliament (Congress of Deputies + Senate)", "Las Cortes Generales representan al pueblo español y aprueban las leyes del Estado."),
                ("el Palacio de la Moncloa", "noun", "Moncloa Palace (official residence and office of the Prime Minister)", "La sede de la Presidencia del Gobierno de España se encuentra en el Palacio de la Moncloa."),
                ("el Palacio de la Zarzuela", "noun", "Zarzuela Palace (residence of the King and Royal Family in Madrid)", "El Rey de España tiene su residencia oficial de trabajo en el Palacio de la Zarzuela."),
                ("el Defensor del Pueblo", "noun", "Ombudsman (High Commissioner of the Cortes Generales defending citizens' rights)", "El Defensor del Pueblo protege los derechos fundamentales de los ciudadanos frente a la Administración."),
                ("el Tribunal Constitucional", "noun", "Constitutional Court (12 members; supreme interpreter of the Constitution)", "El Tribunal Constitucional vigila que todas las leyes respeten la Constitución Española."),
                ("el Boletín Oficial del Estado", "noun", "Official State Gazette (BOE, where laws enter into force)", "Las leyes aprobadas por las Cortes Generales se publican en el Boletín Oficial del Estado.")
            ],
            "ex_mc": [
                ("¿Qué institución del Estado elige al Presidente del Gobierno de España mediante la votación de investidura?", ["El Congreso de los Diputados (a propuesta del Rey)", "El Senado exclusivamente", "El Consejo General del Poder Judicial", "Los alcaldes de las capitales de provincia"], 0),
                ("¿Cuál es la tercera autoridad del Estado español (tras el Rey y el Presidente del Gobierno)?", ["El Presidente o Presidenta del Congreso de los Diputados", "El Ministro de Hacienda", "El Gobernador del Banco de España", "El Director de la Guardia Civil"], 0)
            ],
            "ex_fb": [
                ("La forma política del Estado español según el artículo 1 de la Constitución es la ___ parlamentaria.", "Monarquía", "The political form of the Spanish State according to Article 1 of the Constitution is the Parliamentary Monarchy."),
                ("Las leyes entran en vigor en España tras ser publicadas en el Boletín Oficial del ___ (BOE).", "Estado", "Laws enter into force in Spain after being published in the Official State Gazette (BOE).")
            ],
            "ex_sb": [
                (["La", "soberanía", "nacional", "reside", "en", "el", "pueblo", "español."], "National sovereignty resides in the Spanish people.")
            ],
            "ex_dict": [
                ("Las Cortes Generales están formadas por el Congreso de los Diputados y el Senado.", "The Cortes Generales are made up of the Congress of Deputies and the Senate.")
            ]
        },
        {
            "num": "03",
            "title": "Simulacro Tarea 2: Derechos y deberes fundamentales (5 preguntas de Verdadero / Falso)",
            "objective": "Dominar la lógica de las 5 preguntas de Verdadero o Falso de la Tarea 2 del examen CCSE sobre derechos fundamentales, libertades públicas, edades legales y deberes constitucionales.",
            "grammar_title": "Afirmaciones universales y prohibiciones absolutas en ítems de Verdadero o Falso («queda abolida la pena de muerte», «nadie puede ser discriminado»)",
            "grammar_slug": "afirmaciones-prohibiciones-verdadero-falso-tarea-dos",
            "grammar_Body": """La **Tarea 2 del examen CCSE** consta de **5 enunciados (preguntas 11 a 15)** en los que el candidato debe marcar **A) Verdadero** o **B) Falso**. Para acertar las cinco preguntas, ten presentes estas reglas constitucionales invariables:

- **SON VERDADEROS**: La mayoría de edad es a los **18 años**; la enseñanza básica (6-16 años) es **obligatoria y gratuita**; queda abolida la **pena de muerte** (art. 15 CE); la policía solo puede detener preventivamente un máximo de **72 horas** antes de pasar a disposición judicial; **ninguna confesión religiosa tiene carácter estatal** (art. 16 CE); todos deben contribuir a los gastos públicos mediante **impuestos según su capacidad económica** (art. 31 CE).
- **SON FALSOS**: Los enunciados que dicen que se puede abrir la correspondencia ajena sin orden judicial, que se puede entrar en un domicilio sin permiso ni orden judicial (salvo flagrante delito), o que es obligatorio declarar la propia ideología o religión.""",
            "story_title": "Las cinco preguntas de Verdadero o Falso bajo la lupa",
            "paragraphs": [
                "Las preguntas 11 a 15 del examen oficial CCSE constituyen la Tarea 2 y evalúan el conocimiento de los derechos y deberes fundamentales recogidos en el Título I de la Constitución Española. A diferencia del resto del examen, estas cinco preguntas solo tienen dos opciones posibles de respuesta: Opción A (Verdadero) u Opción B (Falso).",
                "Entre los enunciados que son siempre VERDADEROS en el manual oficial del Instituto Cervantes destacan las grandes conquistas de derechos humanos: en España todos los ciudadanos son iguales ante la ley sin que pueda prevalecer discriminación por nacimiento, raza, sexo, religión u opinión (artículo 14); todos tienen derecho a la vida y queda abolida la pena de muerte (artículo 15); se garantiza la libertad ideológica y religiosa, y ninguna confesión tendrá carácter estatal (artículo 16).",
                "También son VERDADEROS los enunciados que afirman que en España la mayoría de edad se alcanza a los dieciocho años (18 años); que la detención preventiva policial no puede durar más del tiempo estrictamente necesario y, en todo caso, en el plazo máximo de setenta y dos horas (72 horas) el detenido deberá ser puesto en libertad o a disposición de la autoridad judicial (artículo 17); y que los ciudadanos tienen derecho a asociarse libremente, a sindicarse, a la huelga y a reunirse pacíficamente y sin armas (no necesitando autorización previa las reuniones pacíficas, sino únicamente comunicación previa a la autoridad cuando se celebren en lugares de tránsito público).",
                "En cuanto a los deberes constitucionales, son VERDADEROS los enunciados que señalan que todos los españoles tienen el derecho y el deber de defender a España (artículo 30, aunque desde el año 2001 el servicio militar obligatorio, la antigua «mili», está suprimido y las Fuerzas Armadas son totalmente profesionales) y que todos contribuirán al sostenimiento de los gastos públicos mediante un sistema tributario justo y progresivo (artículo 31).",
                "Por el contrario, recuerda marcar FALSO ante cualquier enunciado que afirme que un jefe o un propietario puede entrar en el domicilio de una persona sin su consentimiento y sin orden judicial (pues el domicilio es inviolable, art. 18), que se pueden leer las cartas o mensajes privados de otra persona (pues se garantiza el secreto de las comunicaciones) o que la enseñanza obligatoria dura hasta los 18 o 21 años (pues termina a los 16 años)."
            ],
            "questions": [
                ("En la Tarea 2 del examen CCSE (Verdadero o Falso), ¿es VERDADERO o FALSO el enunciado: «La Constitución Española garantiza la libertad religiosa de los individuos y las comunidades, y en España ninguna confesión tiene carácter estatal»?", ["Verdadero", "Falso", "Solo en algunas provincias", "Solo para extranjeros"], 0),
                ("¿Es VERDADERO o FALSO el enunciado: «En España, una persona detenida por la policía puede permanecer en comisaría durante un mes entero sin pasar a disposición de un juez»?", ["Falso (el plazo máximo constitucional de detención preventiva es de 72 horas)", "Verdadero", "Verdadero en verano", "Depende del alcalde"], 0),
                ("¿Es VERDADERO o FALSO el enunciado: «En España el domicilio es inviolable: ninguna entrada o registro podrá hacerse en él sin consentimiento del titular o resolución judicial, salvo en caso de flagrante delito»?", ["Verdadero (artículo 18 de la Constitución Española)", "Falso", "Solo es verdadero para viviendas de compra", "Falso en los bloques de pisos"], 0)
            ],
            "vocab": [
                ("la inviolabilidad del domicilio", "noun", "inviolability of the home (Art. 18.2 CE; requires consent or judicial warrant)", "La inviolabilidad del domicilio impide entrar en una vivienda sin permiso o autorización judicial."),
                ("el secreto de las comunicaciones", "noun", "secrecy of communications (post, telephone, internet; Art. 18.3 CE)", "La Constitución garantiza el secreto de las comunicaciones postales y telefónicas."),
                ("la detención preventiva", "noun", "preventive police detention (maximum 72 hours before going before a judge)", "La detención preventiva no puede superar el plazo máximo de setenta y dos horas."),
                ("la abolición de la pena de muerte", "noun", "abolition of the death penalty (Art. 15 CE)", "El artículo quince de la Constitución establece la abolición de la pena de muerte en España."),
                ("el Estado aconfesional", "noun", "non-denominational / secular state (no state religion, Art. 16.3 CE)", "España es un Estado aconfesional donde se garantiza la libertad religiosa e ideológica."),
                ("el derecho de reunión", "noun", "right of peaceful assembly without weapons (Art. 21 CE)", "El ejercicio del derecho de reunión pacífica y sin armas no necesita autorización previa."),
                ("el derecho a la huelga", "noun", "right to strike for the defense of workers' interests (Art. 28.2 CE)", "La Constitución reconoce el derecho a la huelga manteniendo los servicios esenciales de la comunidad."),
                ("la capacidad económica", "noun", "economic capacity (basis of Spain's progressive tax system, Art. 31 CE)", "Todos contribuyen a los gastos públicos mediante impuestos según su capacidad económica.")
            ],
            "ex_mc": [
                ("¿Existe actualmente en España el servicio militar obligatorio para los jóvenes al cumplir los 18 años?", ["No, en España no existe el servicio militar obligatorio (fue abolido en 2001 y el Ejército es 100 % profesional)", "Sí, es obligatorio durante dos años", "Sí, durante seis meses en la marina", "Solo para los nacidos en años pares"], 0),
                ("¿Se necesita pedir permiso previo al Gobierno para celebrar una reunión pacífica y sin armas en un local cerrado en España?", ["No, el derecho de reunión pacífica y sin armas no necesita autorización previa (en la vía pública solo requiere comunicación previa)", "Sí, hay que pedir autorización al Rey con seis meses de antelación", "Están prohibidas todas las reuniones", "Solo pueden reunirse los diputados"], 0)
            ],
            "ex_fb": [
                ("En España, el plazo máximo legal que un detenido puede permanecer en comisaría antes de ser puesto en libertad o pasar ante el juez es de ___ horas.", "72", "In Spain, the maximum legal period a detainee may remain at a police station before being released or brought before a judge is 72 hours."),
                ("Según el artículo 15 de la Constitución Española, todos tienen derecho a la vida y queda abolida la ___ de muerte.", "pena", "According to Article 15 of the Spanish Constitution, everyone has the right to life and the death penalty is abolished.")
            ],
            "ex_sb": [
                (["En", "España", "ninguna", "confesión", "religiosa", "tiene", "carácter", "estatal."], "In Spain no religious denomination has state character.")
            ],
            "ex_dict": [
                ("Todos los ciudadanos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica.", "All citizens shall contribute to sustaining public expenditure in accordance with their economic capacity.")
            ]
        },
        {
            "num": "04",
            "title": "Simulacro Tarea 3: Organización territorial y geografía física y política (2 preguntas)",
            "objective": "Asegurar los 2 puntos de la Tarea 3 del examen CCSE repasando el mapa autonómico (17 comunidades, 2 ciudades autónomas, 50 provincias y sus capitales) y los grandes accidentes geográficos de España.",
            "grammar_title": "Relaciones geográficas de pertenencia y capitalidad («la capital de... es...», «desemboca en...»)",
            "grammar_slug": "relaciones-geograficas-capitalidad-tarea-tres",
            "grammar_Body": """La **Tarea 3 del examen CCSE** consta de **2 preguntas de selección múltiple (preguntas 16 y 17)** sobre geografía física y política de España. Los puntos más preguntados son:

- **17 comunidades autónomas y 2 ciudades autónomas (Ceuta y Melilla)**, divididas en **50 provincias**.
- **Comunidades autónomas uniprovinciales (7)**: Asturias (capital Oviedo), Cantabria (Santander), La Rioja (Logroño), Navarra (Pamplona), Comunidad de Madrid (Madrid), Región de Murcia (Murcia) e Islas Baleares (Palma).
- **Capitales autonómicas que no son homónimas**: Galicia -> **Santiago de Compostela**; Extremadura -> **Mérida**; Andalucía -> **Sevilla**; Castilla y León -> **Valladolid** (sede de las instituciones); Castilla-La Mancha -> **Toledo**; País Vasco -> **Vitoria-Gasteiz**; Canarias -> **Santa Cruz de Tenerife y Las Palmas de Gran Canaria** (capitalidad compartida).
- **Pico más alto**: el **Teide** (Tenerife, 3.718 m) de España; el **Mulhacén** (Sierra Nevada, Granada, 3.479 m) de la Península. **Río más largo**: el **Tajo**; **río más caudaloso**: el **Ebro**.""",
            "story_title": "Un mapa mental infalible de las diecisiete autonomías y sus paisajes",
            "paragraphs": [
                "Las preguntas 16 y 17 del cuadernillo CCSE corresponden a la Tarea 3 y evalúan el conocimiento de la organización territorial, las capitales autonómicas, las provincias y el relieve, ríos y costas de España. Aunque son dos preguntas, resultan muy sencillas de asegurar si se dominan las asociaciones geográficas fundamentales.",
                "En el mapa político, España se organiza en diecisiete comunidades autónomas, dos ciudades autónomas en el norte de África (Ceuta y Melilla) y cincuenta provincias (50 provincias). Siete comunidades autónomas son uniprovinciales (formadas por una sola provincia): el Principado de Asturias (capital Oviedo), Cantabria (capital Santander), La Rioja (capital Logroño), la Comunidad Foral de Navarra (capital Pamplona), la Comunidad de Madrid, la Región de Murcia y las Islas Baleares (capital Palma en la isla de Mallorca, junto con las islas de Menorca, Ibiza, Formentera y Cabrera).",
                "Entre las comunidades pluriprovinciales es esencial recordar el número de provincias y su capital: Andalucía tiene 8 provincias (Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga y su capital, Sevilla); Castilla y León es la más extensa de España y tiene 9 provincias (Ávila, Burgos, León, Palencia, Salamanca, Segovia, Soria, Valladolid y Zamora); Castilla-La Mancha tiene 5 provincias (Albacete, Ciudad Real, Cuenca, Guadalajara y su capital, Toledo); Galicia tiene 4 provincias (A Coruña, Lugo, Ourense y Pontevedra, con capital autonómica en Santiago de Compostela); Cataluña tiene 4 (Barcelona, Girona, Lleida y Tarragona); la Comunidad Valenciana tiene 3 (Alicante, Castellón y Valencia); Aragón tiene 3 (Huesca, Teruel y Zaragoza); el País Vasco tiene 3 territorios históricos (Álava con la capital Vitoria-Gasteiz, Guipúzcoa con San Sebastián y Vizcaya con Bilbao); Extremadura tiene 2 (Badajoz y Cáceres, con capital en Mérida); y Canarias tiene 2 provincias (Las Palmas y Santa Cruz de Tenerife) y 8 islas habitadas (Tenerife, Gran Canaria, Lanzarote, Fuerteventura, La Palma, La Gomera, El Hierro y La Graciosa).",
                "En el mapa físico, la Península Ibérica está rodeada por el mar Cantábrico al norte, el océano Atlántico al oeste y suroeste y el mar Mediterráneo al este y sureste, y limita por tierra con Francia y Andorra (en la cordillera de los Pirineos), con Portugal al oeste, con el Reino Unido en Gibraltar y con Marruecos en Ceuta y Melilla.",
                "La cumbre más alta de toda España es el volcán del Teide (3.718 m), en la isla de Tenerife (Canarias), mientras que la montaña más alta de la Península Ibérica es el pico Mulhacén (3.479 m), en Sierra Nevada (Granada). En cuanto a los grandes ríos peninsulares, el Miño, el Duero, el Tajo (el río más largo de la península), el Guadiana y el Guadalquivir desembocan en el océano Atlántico, mientras que el Ebro (el río más caudaloso y largo íntegramente español), el Júcar y el Segura desembocan en el mar Mediterráneo."
            ],
            "questions": [
                ("¿Cuál es la montaña más alta de toda España y cuál es el pico más alto de la Península Ibérica?", ["El Teide (en Tenerife, Canarias) es el más alto de toda España y el Mulhacén (en Sierra Nevada, Granada) es el más alto de la Península", "El Aneto en Madrid y el Moncayo en Sevilla", "Los Picos de Europa en Mallorca", "La Sierra de Guadarrama en Cádiz"], 0),
                ("¿Cuáles son las capitales autonómicas de Galicia, de Extremadura y del País Vasco?", ["Santiago de Compostela (Galicia), Mérida (Extremadura) y Vitoria-Gasteiz (País Vasco)", "Vigo, Badajoz y Bilbao", "Lugo, Cáceres y San Sebastián", "Oviedo, Toledo y Santander"], 0),
                ("¿En qué mar u océano desemboca el río Ebro (que pasa por Logroño y Zaragoza) y en cuál desembocan el Tajo, el Duero y el Guadalquivir?", ["El Ebro desemboca en el mar Mediterráneo (en Tarragona), mientras que el Tajo, el Duero y el Guadalquivir desembocan en el océano Atlántico", "Todos desembocan en el mar Cantábrico", "El Ebro desemboca en el Atlántico y el Tajo en el Mediterráneo", "Ninguno llega al mar"], 0)
            ],
            "vocab": [
                ("el pico del Teide", "noun", "Mount Teide (3,718 m volcano in Tenerife; highest peak in Spain)", "El pico del Teide, en la isla de Tenerife, es la montaña más alta de España."),
                ("el Mulhacén", "noun", "Mount Mulhacén (3,479 m in Sierra Nevada, Granada; highest peak on the mainland)", "El Mulhacén se encuentra en Sierra Nevada y es la cumbre más alta de la Península Ibérica."),
                ("el río Tajo", "noun", "Tagus River (longest river on the Iberian Peninsula; flows through Toledo into the Atlantic)", "El río Tajo pasa por Aranjuez, Toledo y Talavera de la Reina y es el más largo de la península."),
                ("el río Ebro", "noun", "Ebro River (highest-flow river in Spain; flows into the Mediterranean in Tarragona)", "El río Ebro nace en Cantabria y desemboca en el mar Mediterráneo formando el Delta del Ebro."),
                ("los Pirineos", "noun", "the Pyrenees mountain range (natural border with France and Andorra)", "La cordillera de los Pirineos forma la frontera natural del norte de España con Francia y Andorra."),
                ("la Meseta Central", "noun", "the Central Plateau (divided by the Sistema Central into Submeseta Norte and Sur)", "El Sistema Central divide la gran Meseta española en dos submesetas."),
                ("la comunidad uniprovincial", "noun", "single-province autonomous community (Asturias, Cantabria, La Rioja, Navarra, Madrid, Murcia, Baleares)", "En las siete comunidades uniprovinciales no existe diputación provincial."),
                ("el Parque Nacional", "noun", "National Park (16 in Spain, such as Doñana, Picos de Europa, Teide, Timanfaya, Ordesa)", "España cuenta con dieciséis Parques Nacionales de extraordinaria riqueza ecológica.")
            ],
            "ex_mc": [
                ("¿Cuántas provincias componen la comunidad autónoma de Andalucía y cuántas componen la de Castilla y León?", ["Andalucía tiene 8 provincias y Castilla y León tiene 9 provincias (de las 50 provincias de España)", "Andalucía tiene 2 y Castilla y León tiene 3", "Ambas son comunidades uniprovinciales", "Tienen 15 provincias cada una"], 0),
                ("¿En qué comunidad autónoma se encuentra el Parque Nacional de Doñana y en cuál se encuentra el Parque Nacional de Timanfaya?", ["Doñana está en Andalucía (Huelva, Sevilla y Cádiz) y Timanfaya está en Canarias (isla de Lanzarote)", "Doñana está en Galicia y Timanfaya en Asturias", "Ambos están en la Comunidad de Madrid", "Están en los Pirineos de Huesca"], 0)
            ],
            "ex_fb": [
                ("El río más largo de la Península Ibérica, que pasa por la ciudad de Toledo y desemboca en el Atlántico, es el río ___.", "Tajo", "The longest river on the Iberian Peninsula, which flows through the city of Toledo and empties into the Atlantic, is the Tagus River (Tajo)."),
                ("La capital de la comunidad autónoma de Extremadura es ___ y la de Galicia es Santiago de Compostela.", "Mérida", "The capital of the autonomous community of Extremadura is Mérida and that of Galicia is Santiago de Compostela.")
            ],
            "ex_sb": [
                (["El", "Teide", "es", "la", "montaña", "más", "alta", "de", "España."], "Mount Teide is the highest mountain in Spain.")
            ],
            "ex_dict": [
                ("España está organizada en diecisiete comunidades autónomas, dos ciudades autónomas y cincuenta provincias.", "Spain is organized into seventeen autonomous communities, two autonomous cities, and fifty provinces.")
            ]
        },
        {
            "num": "05",
            "title": "Simulacro Tareas 4 y 5: Cultura, historia y vida cotidiana en España (8 preguntas finales)",
            "objective": "Completar con éxito el Simulacro General CCSE repasando las 3 preguntas de Cultura e Historia (Tarea 4, preguntas 18-20) y las 5 preguntas de Sociedad y Vida Cotidiana (Tarea 5, preguntas 21-25).",
            "grammar_title": "Síntesis integradora de referentes culturales y cívicos para el pleno en el examen CCSE",
            "grammar_slug": "sintesis-integradora-cultura-sociedad-espanola",
            "grammar_Body": """Las últimas ocho preguntas del examen CCSE (**Tarea 4: preguntas 18 a 20**, y **Tarea 5: preguntas 21 a 25**) cierran la prueba con un recorrido por el patrimonio histórico-artístico y los trámites de la vida diaria en España:

- **Tarea 4 (3 preguntas)**: Cervantes y *El Quijote*, García Lorca, los Premios Cervantes y Princesa de Asturias (en Oviedo), Velázquez (*Las meninas*), Goya, Picasso (*Guernica* en el Museo Reina Sofía), Dalí, Gaudí (Sagrada Familia en Barcelona), el flamenco, los Premios Goya de cine y las grandes fiestas (Fallas de Valencia, San Fermín en Pamplona, Feria de Abril en Sevilla) y gastronomía (dieta mediterránea, aceite de oliva, paella, gazpacho).
- **Tarea 5 (5 preguntas)**: DNI obligatorio a los **14 años** (Policía Nacional), mayoría de edad y carné de conducir a los **18 años**, edad mínima para trabajar a los **16 años**, enseñanza obligatoria de **6 a 16 años** (Primaria y ESO), tarjeta sanitaria y médico de familia, emergencias **112**, violencia de género **016**, empadronamiento en el **Ayuntamiento**, garantía de **3 años** y Hojas de Reclamaciones.""",
            "story_title": "Las ocho preguntas finales hacia la ciudadanía española",
            "paragraphs": [
                "El tramo final del examen oficial CCSE está formado por las tres preguntas de la Tarea 4 (preguntas 18, 19 y 20), dedicadas a la cultura y la historia de España, y por las cinco preguntas de la Tarea 5 (preguntas 21, 22, 23, 24 y 25), dedicadas a la sociedad, la administración y la vida cotidiana.",
                "En la Tarea 4 brillan los grandes hitos de la historia y la creación artística española: la huella romana en el Acueducto de Segovia y el Teatro de Mérida; el legado de Al-Ándalus en la Mezquita de Córdoba y la Alhambra de Granada; el año 1492; la Constitución de Cádiz de 1812 («La Pepa») y la Transición democrática coronada por la Constitución de 1978. Junto a ellos, el Siglo de Oro de Miguel de Cervantes (*Don Quijote de la Mancha*, que da nombre al Premio Cervantes entregado cada 23 de abril en Alcalá de Henares) y de Diego Velázquez (*Las meninas*, en el Museo del Prado), la pintura de Francisco de Goya, el *Guernica* de Pablo Picasso (en el Museo Reina Sofía), el surrealismo de Salvador Dalí y la arquitectura modernista de Antoni Gaudí en Barcelona.",
                "También forman parte esencial de la Tarea 4 los Premios Princesa de Asturias (entregados en el Teatro Campoamor de Oviedo), el flamenco (con maestros como Paco de Lucía y Camarón de la Isla), el cine español premiado con los Goya y los Óscar (Luis Buñuel, José Luis Garci, Pedro Almodóvar, Alejandro Amenábar, Penélope Cruz y Javier Bardem), los premios Nobel científicos Santiago Ramón y Cajal y Severo Ochoa, y las fiestas populares como las Fallas de Valencia en marzo, los Sanfermines de Pamplona en julio o las doce uvas de Nochevieja.",
                "Por último, las cinco preguntas de la Tarea 5 comprueban que el futuro ciudadano conoce perfectamente cómo desenvolverse en España: sabe que al llegar a un municipio debe empadronarse en el Ayuntamiento; que el DNI es obligatorio desde los 14 años y lo expide la Policía Nacional; que la sanidad pública se recibe con la Tarjeta Sanitaria en el centro de salud y las farmacias tienen una cruz verde; que la enseñanza obligatoria y gratuita comprende Primaria y la ESO desde los 6 hasta los 16 años; y que la edad mínima para trabajar es de 16 años.",
                "Con el dominio de estas treinta y seis unidades, el candidato no solo cuenta con todas las herramientas para superar con holgura las 25 preguntas del examen CCSE del Instituto Cervantes y obtener su calificación de APTO, sino también con un conocimiento profundo, humano y vivo de la España democrática que hoy es su hogar."
            ],
            "questions": [
                ("¿En qué museo de Madrid se conserva el cuadro «Las meninas» de Diego Velázquez y en cuál se exhibe el «Guernica» de Pablo Picasso?", ["«Las meninas» de Velázquez está en el Museo Nacional del Prado y el «Guernica» de Picasso está en el Museo Reina Sofía", "Ambos cuadros están en el Museo Guggenheim de Bilbao", "Están en el Teatro Romano de Mérida", "Están en la Sagrada Familia de Barcelona"], 0),
                ("¿En qué ciudad se entregan cada otoño los prestigiosos Premios Princesa de Asturias y en qué universidad se entrega el Premio Cervantes cada 23 de abril?", ["Los Premios Princesa de Asturias se entregan en Oviedo (Teatro Campoamor) y el Premio Cervantes en la Universidad de Alcalá de Henares", "Ambos premios se entregan en Cádiz", "En Vigo y en Badajoz", "En Bruselas y en Estrasburgo"], 0),
                ("Repaso global de edades legales en España para el examen CCSE: ¿a qué edad es obligatorio el DNI, entre qué edades es obligatoria la enseñanza básica (Primaria y ESO), a qué edad se puede empezar a trabajar y a qué edad se alcanza la mayoría de edad (para votar, conducir coches y comprar tabaco o alcohol)?", ["DNI obligatorio: 14 años; enseñanza obligatoria: de 6 a 16 años; edad mínima laboral: 16 años; mayoría de edad: 18 años", "Todo a los 21 años", "Todo a los 12 años", "DNI a los 18 y mayoría de edad a los 14"], 0)
            ],
            "vocab": [
                ("el Premio Cervantes", "noun", "Cervantes Prize (highest award in Spanish-language literature, presented on April 23)", "El Premio Cervantes es el máximo galardón de las letras en lengua española."),
                ("los Premios Princesa de Asturias", "noun", "Princess of Asturias Awards (presented annually in Oviedo)", "Los Premios Princesa de Asturias reconocen la labor científica, cultural y humanitaria internacional."),
                ("el Museo Nacional del Prado", "noun", "Prado National Museum (Madrid; houses Velázquez and Goya)", "El Museo Nacional del Prado conserva las grandes obras de Velázquez, el Greco y Goya."),
                ("el Museo Reina Sofía", "noun", "Reina Sofía National Art Center Museum (Madrid; houses Picasso's Guernica)", "El famoso cuadro Guernica de Pablo Picasso se expone en el Museo Reina Sofía de Madrid."),
                ("los Premios Goya", "noun", "Goya Awards (annual awards of the Spanish Film Academy)", "La Academia de Cine entrega anualmente los Premios Goya a las mejores películas españolas."),
                ("Patrimonio de la Humanidad", "noun", "UNESCO World Heritage (Spain has over 50 World Heritage sites)", "España es uno de los países del mundo con mayor número de bienes declarados Patrimonio de la Humanidad."),
                ("la integración sociocultural", "noun", "sociocultural integration (accredited via the CCSE exam)", "La superación de la prueba CCSE acredita la integración sociocultural en España."),
                ("la ciudadanía española", "noun", "Spanish citizenship", "La ciudadanía española conlleva el pleno ejercicio de los derechos y deberes constitucionales.")
            ],
            "ex_mc": [
                ("¿Quiénes fueron los dos grandes científicos españoles galardonados con el Premio Nobel de Fisiología o Medicina en el siglo XX?", ["Santiago Ramón y Cajal (1906) y Severo Ochoa (1959)", "Camilo José Cela y Vicente Aleixandre", "Isaac Albéniz y Manuel de Falla", "Pau Gasol y Fernando Alonso"], 0),
                ("¿Cuál de las siguientes relaciones entre fiesta tradicional española y ciudad en la que se celebra es totalmente correcta para el examen CCSE?", ["Las Fallas en Valencia (marzo), los Sanfermines en Pamplona (julio) y la Feria de Abril en Sevilla", "Las Fallas en Bilbao y los Sanfermines en Málaga", "La Tomatina en Santiago de Compostela", "El Carnaval de Cádiz en el mes de agosto"], 0)
            ],
            "ex_fb": [
                ("El cuadro «Las meninas» de Diego Velázquez se encuentra en el Museo del ___, y el «Guernica» de Pablo Picasso en el Museo Reina Sofía.", "Prado", "The painting 'Las Meninas' by Diego Velázquez is in the Prado Museum, and 'Guernica' by Pablo Picasso is in the Reina Sofía Museum."),
                ("En España, el DNI es obligatorio a los 14 años, la enseñanza básica dura hasta los ___ años y la mayoría de edad se alcanza a los 18 años.", "16", "In Spain, the DNI is mandatory at age 14, compulsory basic education lasts until age 16, and the age of majority is reached at age 18.")
            ],
            "ex_sb": [
                (["Has", "completado", "con", "éxito", "la", "preparación", "para", "el", "examen", "de", "nacionalidad", "española."], "You have successfully completed the preparation for the Spanish nationality exam.")
            ],
            "ex_dict": [
                ("El conocimiento de la Constitución y de la cultura española abre las puertas a la plena ciudadanía.", "Knowledge of the Constitution and Spanish culture opens the doors to full citizenship.")
            ]
        }
    ]
}


if __name__ == "__main__":
    for u in (UNIT_34, UNIT_35, UNIT_36):
        emit_unit_from_dict(u)
    print("Units 34, 35, and 36 generated successfully.")
