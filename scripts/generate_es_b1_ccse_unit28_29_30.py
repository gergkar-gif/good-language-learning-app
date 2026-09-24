#!/usr/bin/env python3
"""Generate Spain CCSE B1 Units 28, 29, and 30 (Gastronomía, Sanidad, Educación)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict


UNIT_28 = {
    "unit_num": 64,
    "slug": "gastronomia",
    "title": "Gastronomía Española y Dieta Mediterránea",
    "theme": "Tradiciones culinarias, productos con Denominación de Origen y alta cocina en España (Tarea 4 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "La dieta mediterránea y el aceite de oliva virgen extra",
            "objective": "Conocer los pilares de la dieta mediterránea como Patrimonio de la Humanidad y el liderazgo mundial de España en aceite de oliva.",
            "grammar_title": "El superlativo relativo y las construcciones de proporción («el mayor productor del mundo»)",
            "grammar_slug": "superlativo-relativo-proporcion",
            "grammar_Body": """Para destacar el liderazgo de España en la producción agroalimentaria dentro del examen CCSE, se utiliza el **superlativo relativo** (*el/la/los/las + más/menos + adjetivo + de*) o sustantivos cuantificadores seguidos de *de*:

- *España es **el mayor productor de** aceite de oliva **del mundo**.*
- *Andalucía concentra **la producción más elevada de** aceituna **del país**.*
- *La dieta mediterránea está considerada como **uno de los modelos alimentarios más saludables del planeta**.*""",
            "story_title": "El oro líquido de los olivares andaluces",
            "paragraphs": [
                "España es el primer productor y exportador mundial de aceite de oliva, conocido popularmente en toda la península como el «oro líquido». Casi la mitad de todo el aceite de oliva del planeta procede de los campos españoles, con especial concentración en la comunidad autónoma de Andalucía y, muy particularmente, en la provincia de Jaén, cuyos interminables mares de olivos cubren valles y montañas.",
                "El aceite de oliva virgen extra constituye la base grasa fundamental de la dieta mediterránea, reconocida en 2010 por la UNESCO como Patrimonio Cultural Inmaterial de la Humanidad. Este modelo nutricional no solo comprende una lista de ingredientes saludables, sino también una forma social de compartir la mesa, comprar en los mercados de abastos locales y respetar los productos frescos de cada estación.",
                "Los pilares de la dieta mediterránea española combinan el consumo diario de verduras, hortalizas, frutas frescas, cereales, pan y legumbres —como los garbanzos, las lentejas y las alubias— con el consumo frecuente de pescado azul y blanco, huevos, frutos secos y lácteos como el queso o el yogur, reservando las carnes rojas para ocasiones más puntuales.",
                "Numerosos estudios científicos nacionales como el proyecto PREDIMED han demostrado que este patrón alimentario reduce drásticamente las enfermedades cardiovasculares y contribuye a que España posea una de las esperanzas de vida al nacer más altas del mundo, superando los ochenta y tres años de media.",
                "Cocinar con ajo, cebolla, tomate y aceite de oliva —el famoso sofrito español— une desde hace siglos las cocinas de todas las regiones peninsulares e insulares en una misma tradición saludable y sabrosa."
            ],
            "questions": [
                ("¿De qué producto agroalimentario es España el primer productor mundial?", ["De aceite de oliva", "De café en grano", "De té negro", "De mantequilla de vaca"], 0),
                ("¿Qué provincia andaluza destaca como principal productora de aceite de oliva en España?", ["Jaén", "Almería", "Huelva", "Cádiz"], 0),
                ("¿Qué organismo declaró la dieta mediterránea Patrimonio Cultural Inmaterial de la Humanidad?", ["La UNESCO", "El Comité Olímpico Internacional", "El Banco Central Europeo", "La OTAN"], 0)
            ],
            "vocab": [
                ("el aceite de oliva", "noun", "olive oil", "España es el mayor productor mundial de aceite de oliva virgen extra."),
                ("el olivar", "noun", "olive grove", "Los olivares de la provincia de Jaén producen millones de litros de aceite."),
                ("la legumbre", "noun", "legume / pulse", "Las lentejas y los garbanzos son legumbres esenciales en la dieta española."),
                ("la hortaliza", "noun", "vegetable / garden produce", "La huerta mediterránea ofrece hortalizas frescas durante todo el año."),
                ("el sofrito", "noun", "sautéed aromatic base (garlic, onion, tomato)", "El sofrito de ajo, cebolla y tomate es la base de muchos guisos españoles."),
                ("el pescado azul", "noun", "oily fish (sardine, tuna, mackerel)", "La sardina y el boquerón son pescados azules ricos en ácidos grasos saludables."),
                ("la esperanza de vida", "noun", "life expectancy", "Gracias a su dieta y sanidad, España tiene una alta esperanza de vida."),
                ("el mercado de abastos", "noun", "traditional fresh food market", "Muchos ciudadanos compran fruta y pescado fresco en el mercado de abastos.")
            ],
            "ex_mc": [
                ("¿Cómo se conoce popularmente al aceite de oliva en España por su gran valor económico y gastronómico?", ["El oro líquido", "El diamante blanco", "La plata verde", "El ámbar del norte"], 0),
                ("¿Cuál de estos alimentos es una legumbre muy habitual en los platos de cuchara españoles?", ["El garbanzo", "La merluza", "El mejillón", "La naranja"], 0)
            ],
            "ex_fb": [
                ("España es el primer productor mundial de ___ de oliva.", "aceite", "Spanish is the world's leading producer of olive oil."),
                ("La dieta ___ fue declarada Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO.", "mediterránea", "The Mediterranean diet was declared Intangible Cultural Heritage of Humanity by UNESCO.")
            ],
            "ex_sb": [
                (["España", "es", "el", "mayor", "productor", "de", "aceite", "de", "oliva."], "Spain is the largest producer of olive oil.")
            ],
            "ex_dict": [
                ("El aceite de oliva virgen extra es la base de la dieta mediterránea española.", "Extra virgin olive oil is the foundation of the Spanish Mediterranean diet.")
            ]
        },
        {
            "num": "02",
            "title": "Platos emblemáticos de las regiones españolas",
            "objective": "Identificar los platos más representativos de cada comunidad autónoma española para la prueba cultural del CCSE.",
            "grammar_title": "El verbo «elaborarse con» y las pasivas reflejas culinarias",
            "grammar_slug": "elaborarse-con-pasiva-refleja",
            "grammar_Body": """En las preguntas del CCSE sobre gastronomía regional, es muy frecuente el uso de la **pasiva refleja** con verbos como *elaborarse, prepararse, cocinarse* o *servirse* seguidos de las preposiciones **con** (ingredientes), **en** (recipiente o región) o **a base de**:

- *La tortilla de patatas **se elabora con** huevos, patatas y aceite de oliva.*
- *El gazpacho andaluz **se sirve** frío en verano y **se prepara a base de** tomate, pimiento, pepino, ajo y aceite.*
- *La paella **se cocina en** una sartén ancha y plana llamada paella o paellera.*""",
            "story_title": "Un viaje de norte a sur a través de los fogones",
            "paragraphs": [
                "La gastronomía española se caracteriza por una extraordinaria diversidad regional vinculada al clima y a la geografía de cada territorio. Sin embargo, existe un plato que une todos los hogares y bares del país de norte a sur: la tortilla española o tortilla de patatas, elaborada con huevos batidos, patatas fritas a fuego lento en aceite de oliva y, según el gusto de cada cocinero, cebolla picada.",
                "En la Comunidad Valenciana nació el plato español más internacional: la paella. Cocinada tradicionalmente sobre fuego de leña de naranjo en una sartén ancha, redonda y de poca profundidad con dos asas —que recibe precisamente el nombre de «paella»—, la receta clásica de la huerta valenciana lleva arroz redondo, pollo, conejo, judías verdes planas, garrofón y azafrán.",
                "En el sur, Andalucía ha dado al mundo dos sopas frías imprescindibles para combatir el calor estival: el gazpacho y el salmorejo cordobés. Ambos se elaboran triturando tomate maduro, pan, ajo, aceite de oliva virgen extra y sal, aunque el gazpacho añade pepino, pimiento y agua fría para beberse en vaso o tomarse con cuchara, mientras que el salmorejo es más espeso y suele coronarse con jamón picado y huevo duro.",
                "En la España Verde del norte triunfan los grandes platos de cuchara y los productos del mar: en Asturias es célebre la fabada asturiana, guisada con alubias blancas grandes llamadas «fabes», chorizo, morcilla y lacón; en Galicia reinan el pulpo a feira (servido sobre plato de madera con pimentón y aceite) y la empanada; y en el País Vasco destacan el bacalao al pil-pil y la merluza en salsa verde.",
                "Por su parte, en Madrid y las dos Castillas los inviernos fríos se acompañan con el tradicional cocido madrileño de garbanzos servido en tres «vuelcos» (sopa de fideos, garbanzos con verdura y carnes), además de los asados de cochinillo en Segovia y de cordero lechal en Burgos y Valladolid."
            ],
            "questions": [
                ("¿De qué comunidad autónoma es originaria la paella tradicional?", ["De la Comunidad Valenciana", "De Galicia", "De Asturias", "Del País Vasco"], 0),
                ("¿Cuáles son los ingredientes básicos de la tortilla española?", ["Huevos, patatas y aceite de oliva (y opcionalmente cebolla)", "Harina de maíz, queso y frijoles", "Arroz, azafrán y marisco", "Tomate, pepino y pimiento crudo"], 0),
                ("¿Qué plato típico asturiano se elabora con grandes alubias blancas llamadas «fabes», chorizo y morcilla?", ["La fabada asturiana", "El gazpacho andaluz", "El salmorejo cordobés", "El pulpo a feira"], 0)
            ],
            "vocab": [
                ("la tortilla de patatas", "noun", "Spanish potato omelette", "La tortilla de patatas se prepara con huevos, patatas y aceite de oliva."),
                ("la paella", "noun", "Valencian saffron rice dish (and pan)", "El ingrediente principal de la paella valenciana es el arroz redondo."),
                ("el gazpacho", "noun", "Andalusian cold tomato soup", "El gazpacho es una sopa fría de tomate, pepino y pimiento típica de Andalucía."),
                ("el salmorejo", "noun", "thick Cordoban cold tomato and bread purée", "El salmorejo cordobés se sirve frío con jamón serrano y huevo duro."),
                ("la fabada", "noun", "Asturian white bean stew", "La fabada es el plato de cuchara más representativo del Principado de Asturias."),
                ("el cocido madrileño", "noun", "Madrid chickpea and meat stew", "El cocido madrileño se sirve tradicionalmente en tres vuelcos."),
                ("el pulpo a feira", "noun", "Galician-style boiled octopus with paprika", "El pulpo a feira es uno de los platos más famosos de la gastronomía gallega."),
                ("el azafrán", "noun", "saffron", "El azafrán aporta su característico aroma y color amarillo al arroz de la paella.")
            ],
            "ex_mc": [
                ("¿Qué sopa fría típica de Andalucía se elabora con tomate, pepino, pimiento, ajo, pan y aceite de oliva?", ["El gazpacho", "La fabada", "El cocido", "La paella"], 0),
                ("¿Cuál es el ingrediente principal del cocido madrileño?", ["Los garbanzos", "El arroz bomba", "Las lentejas rojas", "El pulpo cocido"], 0)
            ],
            "ex_fb": [
                ("La ___ de patatas se elabora principalmente con huevos, patatas y aceite de oliva.", "tortilla", "Spanish omelette is made mainly with eggs, potatoes, and olive oil."),
                ("La ___ es el plato de arroz más famoso de la Comunidad Valenciana.", "paella", "Paella is the most famous rice dish of the Valencian Community.")
            ],
            "ex_sb": [
                (["El", "gazpacho", "es", "una", "sopa", "fría", "típica", "de", "Andalucía."], "Gazpacho is a cold soup typical of Andalusia.")
            ],
            "ex_dict": [
                ("La fabada asturiana y el cocido madrileño son platos tradicionales de cuchara.", "Asturian fabada and Madrid cocido are traditional spoon stews.")
            ]
        },
        {
            "num": "03",
            "title": "Denominaciones de Origen: jamón ibérico, quesos y vinos",
            "objective": "Conocer el sistema de Denominación de Origen Protegida (DOP) en España y sus productos estrella: jamón ibérico, quesos y vinos.",
            "grammar_title": "Adjetivos relacionales de procedencia geográfica y clasificación («ibérico de bellota», «manchego»)",
            "grammar_slug": "adjetivos-relacionales-procedencia",
            "grammar_Body": """Los productos agroalimentarios protegidos en España se designan mediante **sustantivos + adjetivos relacionales de origen o raza** y complementos con **de**:

- *Jamón **ibérico de bellota** (Guijuelo, Jabugo, Dehesa de Extremadura, Los Pedroches).*
- *Queso **manchego** (Castilla-La Mancha), queso **cabrales** (Asturias), queso **idiazábal** (País Vasco y Navarra).*
- *Vinos con **Denominación de Origen Calificada (DOCa)** como **Rioja** y **Priorat**, o espumosos como el **cava**.*""",
            "story_title": "El sello de calidad de la tierra española",
            "paragraphs": [
                "Para proteger la autenticidad de sus alimentos tradicionales y garantizar al consumidor que un producto ha sido elaborado en una comarca concreta siguiendo métodos históricos, España y la Unión Europea utilizan el sello de Denominación de Origen Protegida (DOP) y la Indicación Geográfica Protegida (IGP). España cuenta con más de trescientas figuras de calidad diferenciada.",
                "La joya más preciada de la charcutería española es el jamón ibérico de bellota, procedente de cerdos de raza ibérica criados en libertad en las dehesas de encinas y alcornoques del suroeste peninsular. Sus cuatro grandes Denominaciones de Origen son Jabugo (Huelva), Guijuelo (Salamanca), Dehesa de Extremadura y Los Pedroches (Córdoba).",
                "En el ámbito quesero, España elabora más de cien variedades artesanales. El más conocido internacionalmente es el queso manchego, elaborado exclusivamente con leche de oveja de raza manchega en Castilla-La Mancha. También gozan de gran prestigio el queso azul de Cabrales madurado en cuevas naturales de Asturias, el queso ahumado de Idiazábal en el País Vasco y Navarra, el queso de Tetilla en Galicia y el queso Majorero en Fuerteventura.",
                "España posee asimismo la mayor superficie de viñedos plantados del mundo y es uno de los tres primeros productores mundiales de vino junto con Italia y Francia. Entre sus cerca de cien denominaciones vitivinícolas destacan los vinos tintos de Rioja y Ribera del Duero, los blancos de Rueda y Rías Baixas (Albariño), los vinos generosos de Jerez en Cádiz y el cava, vino espumoso elaborado por el método tradicional principalmente en Cataluña, pero también en localidades de Extremadura, Aragón o Valencia.",
                "A estos tesoros se suman el azafrán de La Mancha, el pimentón de la Vera, el turrón de Jijona y Alicante —imprescindible en Navidad— y los plátanos de Canarias."
            ],
            "questions": [
                ("¿De qué comunidad autónoma es originario el famoso queso manchego elaborado con leche de oveja?", ["De Castilla-La Mancha", "De Cantabria", "De las Islas Baleares", "De La Rioja"], 0),
                ("¿Cuál de las siguientes es una famosa Denominación de Origen de vino tinto en España?", ["Rioja (y Ribera del Duero)", "Jabugo", "Cabrales", "Jijona"], 0),
                ("¿Qué dulce tradicional elaborado con almendras y miel cuenta con Indicación Geográfica Protegida en Jijona y Alicante y se consume en Navidad?", ["El turrón", "El churro", "La ensaimada", "El roscón salado"], 0)
            ],
            "vocab": [
                ("la Denominación de Origen", "noun", "Protected Designation of Origin (PDO)", "La Denominación de Origen garantiza la calidad y procedencia geográfica de un alimento."),
                ("el jamón ibérico de bellota", "noun", "acorn-fed Iberian ham", "El jamón ibérico de bellota procede de cerdos criados en libertad en la dehesa."),
                ("la dehesa", "noun", "Mediterranean oak pastureland", "Las dehesas de Extremadura, Andalucía y Salamanca alimentan al cerdo ibérico."),
                ("el queso manchego", "noun", "Manchego sheep's milk cheese", "El queso manchego se elabora con leche de oveja en Castilla-La Mancha."),
                ("el viñedo", "noun", "vineyard", "España cuenta con la mayor superficie de viñedos del mundo."),
                ("el cava", "noun", "Spanish sparkling wine (Cava)", "En las celebraciones españolas es tradicional brindar con una copa de cava."),
                ("el turrón", "noun", "traditional almond and honey nougat", "El turrón de Jijona y Alicante es el dulce navideño más típico de España."),
                ("la bodega", "noun", "winery / wine cellar", "Las bodegas de La Rioja y Jerez reciben a miles de visitantes cada año.")
            ],
            "ex_mc": [
                ("¿Con qué tipo de leche se elabora el auténtico queso con Denominación de Origen Manchego?", ["Con leche de oveja", "Con leche de búfala", "Con leche de yegua", "Con leche de soja"], 0),
                ("¿En qué ecosistema de encinas y alcornoques se cría en libertad el cerdo ibérico de bellota?", ["En la dehesa", "En el glaciar pirenaico", "En la marisma salada", "En la laurisilva"], 0)
            ],
            "ex_fb": [
                ("Rioja y Ribera del Duero son dos famosas Denominaciones de Origen de ___ en España.", "vino", "Rioja and Ribera del Duero are two famous Designations of Origin for wine in Spain."),
                ("El ___ de Jijona y Alicante es un dulce tradicional de almendra muy típico de la Navidad.", "turrón", "Jijona and Alicante nougat is a traditional almond sweet very typical of Christmas.")
            ],
            "ex_sb": [
                (["El", "queso", "manchego", "se", "elabora", "con", "leche", "de", "oveja."], "Manchego cheese is made with sheep's milk.")
            ],
            "ex_dict": [
                ("España tiene la mayor superficie de viñedos del mundo y excelentes vinos con Denominación de Origen.", "Spain has the largest vineyard area in the world and excellent wines with Designation of Origin.")
            ]
        },
        {
            "num": "04",
            "title": "Cultura de tapas, horarios de comida y vida social",
            "objective": "Comprender los horarios de las comidas en España, la costumbre del tapeo y el menú del día como rasgos de la vida cotidiana (Tarea 5 CCSE).",
            "grammar_title": "Expresiones temporales de frecuencia y horarios («entre las dos y las cuatro», «ir de tapas»)",
            "grammar_slug": "expresiones-temporales-horarios-comida",
            "grammar_Body": """Para describir costumbres cotidianas y franjas horarias en España se emplean perífrasis de costumbre (**soler + infinitivo**) y locuciones preposicionales (**entre las X y las Y**, **alrededor de las Z**, **ir de + sustantivo plural**):

- *En España **se suele almorzar entre las 14:00 y las 15:30** horas.*
- *La cena **suele servirse a partir de las 21:00** horas.*
- ***Ir de tapas** o **de pintxos** consiste en compartir pequeñas porciones de comida en distintos bares.*""",
            "story_title": "El arte de compartir alrededor de una barra",
            "paragraphs": [
                "Una de las particularidades culturales que más llama la atención a quienes llegan a vivir a España es la distribución horaria de las cinco comidas diarias y su profunda dimensión social. El día comienza con un desayuno ligero a primera hora y continúa a media mañana —hacia las once— con una pausa breve para tomar un café con leche y una tostada con tomate y aceite o un pincho de tortilla.",
                "La comida principal del día es el almuerzo o comida de mediodía, que en España se realiza considerablemente más tarde que en el resto de Europa: habitualmente entre las dos y las tres y media de la tarde (14:00 - 15:30 h). En los días laborables, la inmensa mayoría de los restaurantes ofrece el tradicional «menú del día», una fórmula económica que incluye un primer plato, un segundo plato, pan, bebida y postre o café a precio fijo.",
                "Por la tarde, especialmente para los niños y las personas mayores, existe la costumbre de la merienda (hacia las 17:30 o 18:00 h), mientras que la cena tiene lugar por la noche, generalmente entre las nueve y las diez y media (21:00 - 22:30 h). Este horario está estrechamente relacionado con las horas de sol de España y con su huso horario oficial (CET en la península y Baleares, y una hora menos en Canarias).",
                "Entre el trabajo y la comida o la cena florece una auténtica institución nacional: «ir de tapas», «tapear» o, en el País Vasco y Navarra, «ir de pintxos». Una tapa es una pequeña porción de comida —como aceitunas, patatas bravas, croquetas, calamares o jamón— que acompaña a la bebida (una caña de cerveza, un vino o un mosto). En ciudades como Granada, Almería, Jaén o León, la tapa se sirve gratuitamente con cada consumición.",
                "Más que una simple forma de alimentarse, el tapeo fomenta la conversación intergeneracional en las terrazas y barras de los bares, que funcionan como verdaderas plazas públicas de encuentro vecinal en todos los barrios españoles."
            ],
            "questions": [
                ("¿En qué franja horaria se suele realizar la comida principal de mediodía (el almuerzo) en España?", ["Entre las 14:00 y las 15:30 horas", "Entre las 11:00 y las 12:00 horas", "A las 17:00 horas en punto", "A las 10:30 de la mañana"], 0),
                ("¿Cómo se llama la oferta económica de mediodía en los restaurantes españoles que incluye primer plato, segundo plato, pan, bebida y postre o café?", ["El menú del día", "La carta de gala", "El bono nocturno", "La ración libre"], 0),
                ("¿Qué significa en España la expresión cotidiana «ir de tapas»?", ["Tomar pequeñas porciones de comida acompañadas de una bebida en uno o varios bares con amigos o familiares", "Comprar ollas y sartenes en una ferretería", "Cerrar los comercios a mediodía", "Cenar exclusivamente fruta en casa"], 0)
            ],
            "vocab": [
                ("la tapa", "noun", "tapa (small portion of food served with a drink)", "En muchas ciudades andaluzas sirven una tapa gratuita con cada bebida."),
                ("el pintxo", "noun", "pintxo (Basque skewered or bread-topped bar snack)", "En San Sebastián y Bilbao es tradicional ir de pintxos por el casco viejo."),
                ("el menú del día", "noun", "fixed-price weekday lunch menu", "El menú del día incluye primer plato, segundo plato, pan, bebida y postre."),
                ("el almuerzo", "noun", "lunch / midday meal", "El almuerzo es la comida principal del día en España y se toma hacia las dos."),
                ("la merienda", "noun", "afternoon snack", "Los niños suelen tomar un bocadillo o fruta a la hora de la merienda."),
                ("la caña", "noun", "small glass of draft beer", "Pidieron dos cañas y una ración de croquetas en la terraza."),
                ("la ración", "noun", "full sharing plate of food", "Para cenar en grupo es muy habitual pedir varias raciones para compartir."),
                ("la sobremesa", "noun", "time spent chatting at the table after a meal", "La sobremesa es la conversación tranquila que sigue a una comida familiar.")
            ],
            "ex_mc": [
                ("¿Cómo se llama en España el tiempo de charla tranquila que se comparte en la mesa después de terminar de comer?", ["La sobremesa", "La madrugada", "La víspera", "La prórroga"], 0),
                ("¿A qué hora suele cenarse habitualmente en España?", ["Entre las 21:00 y las 22:30 horas", "Entre las 17:00 y las 18:00 horas", "A las 16:00 horas", "A las 12:00 del mediodía"], 0)
            ],
            "ex_fb": [
                ("En los restaurantes españoles es muy común pedir a mediodía el ___ del día a precio fijo.", "menú", "In Spanish restaurants it is very common at midday to order the fixed-price menu of the day."),
                ("La costumbre de tomar pequeñas porciones de comida con la bebida en los bares se llama ir de ___.", "tapas", "The custom of eating small portions of food with a drink in bars is called going for tapas.")
            ],
            "ex_sb": [
                (["En", "España", "se", "suele", "almorzar", "entre", "las", "dos", "y", "las", "tres."], "In Spain people usually have lunch between two and three o'clock.")
            ],
            "ex_dict": [
                ("El menú del día incluye primer plato, segundo plato, bebida, pan y postre o café.", "The menu of the day includes a first course, second course, drink, bread, and dessert or coffee.")
            ]
        },
        {
            "num": "05",
            "title": "La alta cocina española y los grandes chefs internacionales",
            "objective": "Reconocer la revolución de la alta cocina española contemporánea y a sus cocineros más premiados internacionalmente.",
            "grammar_title": "Construcciones concesivas y aditivas para valorar aportaciones culturales («no solo..., sino también...»)",
            "grammar_slug": "construcciones-concesivas-aditivas-cocina",
            "grammar_Body": """Para destacar cómo la gastronomía española combina tradición y vanguardia se utilizan correlaciones distributivas y aditivas como **no solo..., sino también...** o **tanto... como...**:

- *La cocina española **no solo** conserva sus recetas centenarias, **sino que también** lidera la vanguardia gastronómica mundial.*
- ***Tanto** Ferran Adrià en Cataluña **como** Juan Mari Arzak y Martín Berasategui en el País Vasco revolucionaron la alta cocina contemporánea.*""",
            "story_title": "De la Nueva Cocina Vasca a la vanguardia mundial",
            "paragraphs": [
                "Durante las últimas cuatro décadas, España ha protagonizado una de las mayores revoluciones culinarias de la historia moderna, pasando de ser admirada únicamente por su cocina tradicional casera a situarse a la vanguardia mundial de la alta gastronomía y la innovación científica aplicada a los fogones.",
                "El primer gran impulso nació en la década de 1970 en San Sebastián con el movimiento de la Nueva Cocina Vasca, liderado por maestros como Juan Mari Arzak y Pedro Subijana. Ellos modernizaron las recetas tradicionales vascas aligerando las salsas, perfeccionando los puntos de cocción del pescado y creando una escuela de la que surgieron chefs con numerosas estrellas Michelin como Martín Berasategui y Karlos Arguiñano.",
                "En la década de 1990, el chef catalán Ferran Adrià transformó para siempre el concepto de restaurante desde «elBulli», situado en una cala de Roses (Girona). Con técnicas inéditas como las esferificaciones, las espumas y la deconstrucción de platos tradicionales —por ejemplo, su célebre deconstrucción de la tortilla de patatas—, elBulli fue elegido cinco veces mejor restaurante del mundo y atrajo a cocineros de todos los continentes.",
                "Ese testigo fue recogido en Girona por los tres hermanos Roca —Joan (cocinero), Josep (sumiller) y Jordi (pastelero)— al frente de «El Celler de Can Roca», así como por grandes figuras de diversas comunidades autónomas como Dabiz Muñoz en Madrid, Quique Dacosta en la Comunidad Valenciana, Ángel León (el «Chef del Mar») en Cádiz o Elena Arzak en Guipúzcoa.",
                "Hoy en día, con centenares de restaurantes galardonados con estrellas de la Guía Michelin y Soles de la Guía Repsol, y con instituciones universitarias como el Basque Culinary Center en San Sebastián, la gastronomía es uno de los grandes motores del turismo cultural y de la imagen internacional de España."
            ],
            "questions": [
                ("¿Qué chef español lideró una revolución culinaria mundial desde su famoso restaurante «elBulli» en Girona?", ["Ferran Adrià", "Camilo José Cela", "Paco de Lucía", "Severo Ochoa"], 0),
                ("¿Qué tres hermanos dirigen el prestigioso restaurante «El Celler de Can Roca» en Cataluña?", ["Los hermanos Roca (Joan, Josep y Jordi Roca)", "Los hermanos Gasol", "Los hermanos Almodóvar", "Los hermanos Machado"], 0),
                ("¿En qué ciudad del País Vasco se fundó el movimiento de la Nueva Cocina Vasca con chefs como Juan Mari Arzak y tiene su sede el Basque Culinary Center?", ["En San Sebastián (Donostia)", "En Sevilla", "En Mérida", "En Santa Cruz de Tenerife"], 0)
            ],
            "vocab": [
                ("la alta cocina", "noun", "haute cuisine / fine dining", "La alta cocina española goza de un enorme prestigio internacional."),
                ("la vanguardia", "noun", "avant-garde / forefront", "Ferran Adrià situó la gastronomía española a la vanguardia mundial."),
                ("la estrella Michelin", "noun", "Michelin star", "Muchos restaurantes españoles cuentan con dos y tres estrellas Michelin."),
                ("el sumiller", "noun", "sommelier / wine steward", "Josep Roca es uno de los sumilleres más reconocidos del panorama internacional."),
                ("el pastelero", "noun", "pastry chef", "La repostería creativa ha alcanzado categoría de arte gracias a grandes pasteleros."),
                ("la deconstrucción", "noun", "culinary deconstruction", "La deconstrucción respeta los sabores de un plato tradicional cambiando sus texturas."),
                ("el turismo gastronómico", "noun", "gastronomic / food tourism", "El turismo gastronómico atrae cada año a millones de viajeros a España."),
                ("el fogón", "noun", "stove / hearth (plural: kitchen)", "Los jóvenes cocineros españoles combinan ciencia y respeto al producto en los fogones.")
            ],
            "ex_mc": [
                ("¿Cuál de estos nombres corresponde a un célebre cocinero español de fama internacional?", ["Ferran Adrià (o Juan Mari Arzak / Joan Roca / Martín Berasategui)", "Rafael Nadal", "Santiago Ramón y Cajal", "Antoni Gaudí"], 0),
                ("¿Qué guía española concede los prestigiosos «Soles» a los mejores restaurantes del país?", ["La Guía Repsol", "El Boletín Oficial del Estado", "El Catastro Inmobiliario", "El Padrón Municipal"], 0)
            ],
            "ex_fb": [
                ("Ferran ___ revolucionó la gastronomía mundial desde su restaurante elBulli.", "Adrià", "Ferran Adrià revolutionized world gastronomy from his restaurant elBulli."),
                ("Juan Mari ___ y Martín Berasategui son grandes referentes de la cocina del País Vasco.", "Arzak", "Juan Mari Arzak and Martín Berasategui are great benchmarks of Basque cuisine.")
            ],
            "ex_sb": [
                (["La", "alta", "cocina", "española", "tiene", "un", "gran", "prestigio", "internacional."], "Spanish haute cuisine has great international prestige.")
            ],
            "ex_dict": [
                ("Ferran Adrià, Juan Mari Arzak y los hermanos Roca son grandes referentes de la cocina española.", "Ferran Adrià, Juan Mari Arzak, and the Roca brothers are great benchmarks of Spanish cuisine.")
            ]
        }
    ]
}


UNIT_29 = {
    "unit_num": 65,
    "slug": "sanidad",
    "title": "El Sistema Nacional de Salud y la Tarjeta Sanitaria",
    "theme": "Asistencia sanitaria pública, atención primaria, urgencias 112, farmacias y salud pública en España (Tarea 5 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "El Sistema Nacional de Salud (SNS): universalidad y descentralización",
            "objective": "Comprender el derecho constitucional a la protección de la salud (art. 43 CE) y la organización descentralizada del Sistema Nacional de Salud.",
            "grammar_title": "Oraciones pasivas e impersonales normativas («se garantiza», «es gestionado por»)",
            "grammar_slug": "pasivas-impersonales-normativas-salud",
            "grammar_Body": """Para explicar el funcionamiento legal del sistema sanitario en el examen CCSE se emplean estructuras de **pasiva refleja** (*se garantiza, se financia*) y de **pasiva perifrástica** (*estar transferido a, ser gestionado por*):

- *El derecho a la protección de la salud **está reconocido en** el artículo 43 de la Constitución Española.*
- *El Sistema Nacional de Salud **se financia a través de** los impuestos generales del Estado.*
- *Las competencias sanitarias **están transferidas a** las diecisiete comunidades autónomas.*""",
            "story_title": "Un pilar del Estado del bienestar español",
            "paragraphs": [
                "El artículo 43 de la Constitución Española de 1978 reconoce el derecho a la protección de la salud y encomienda a los poderes públicos organizar y tutelar la salud pública a través de medidas preventivas y de las prestaciones y servicios necesarios. Este mandato constitucional se materializó mediante la Ley General de Sanidad de 1986, que creó el Sistema Nacional de Salud (SNS).",
                "El Sistema Nacional de Salud español se define por ser público, universal y gratuito en el momento del acceso a la asistencia médica, ya que se financia fundamentalmente a través de los impuestos generales que pagan los ciudadanos y residentes, y no únicamente mediante cuotas privadas de seguros.",
                "En consonancia con el Estado autonómico español, la gestión cotidiana de la sanidad pública está descentralizada y transferida a cada una de las diecisiete comunidades autónomas. Por ello, cada región cuenta con su propio servicio autonómico de salud —como el SERMAS en Madrid, el SAS en Andalucía, el CatSalut en Cataluña o el Osakidetza en el País Vasco—, mientras que el Instituto Nacional de Gestión Sanitaria (INGESA) administra directamente la sanidad en las ciudades autónomas de Ceuta y Melilla.",
                "Para garantizar que todos los ciudadanos reciban prestaciones equivalentes con independencia de su lugar de residencia, el Ministerio de Sanidad del Gobierno de España y los consejeros autonómicos del ramo se reúnen periódicamente en el Consejo Interterritorial del Sistema Nacional de Salud, donde se aprueba la cartera común de servicios.",
                "Esta combinación de cobertura universal, alta cualificación de los médicos y personal de enfermería y red pública de hospitales sitúa al sistema sanitario español entre los más eficientes y valorados del mundo."
            ],
            "questions": [
                ("¿Cómo se financia principalmente el Sistema Nacional de Salud (SNS) en España?", ["A través de los impuestos generales de los ciudadanos", "Únicamente mediante donaciones voluntarias en los hospitales", "Con el pago íntegro en efectivo de cada operación quirúrgica", "Con fondos exclusivos de bancos extranjeros"], 0),
                ("¿Qué instituciones tienen transferida la competencia de gestionar los centros de salud y hospitales públicos en España?", ["Las comunidades autónomas", "Los juzgados de primera instancia", "Las cámaras de comercio", "Las universidades privadas"], 0),
                ("¿Qué ministerio del Gobierno de España coordina la política sanitaria general junto con las comunidades autónomas?", ["El Ministerio de Sanidad", "El Ministerio de Fomento", "El Ministerio de Asuntos Exteriores", "El Ministerio de Cultura"], 0)
            ],
            "vocab": [
                ("el Sistema Nacional de Salud", "noun", "National Health System (SNS)", "El Sistema Nacional de Salud ofrece cobertura sanitaria pública y universal."),
                ("la asistencia sanitaria", "noun", "healthcare / medical assistance", "La asistencia sanitaria pública es gratuita en el momento de recibir la consulta."),
                ("el impuesto", "noun", "tax", "La sanidad y la educación públicas se financian con los impuestos de todos."),
                ("la transferencia de competencias", "noun", "devolution / transfer of powers", "La gestión de los hospitales está transferida a las comunidades autónomas."),
                ("la cartera de servicios", "noun", "portfolio of covered healthcare services", "La cartera común de servicios garantiza las mismas prestaciones en toda España."),
                ("la salud pública", "noun", "public health", "El artículo 43 de la Constitución protege el derecho a la salud pública."),
                ("el personal de enfermería", "noun", "nursing staff", "El personal médico y de enfermería atiende a los pacientes en hospitales y centros."),
                ("el bienestar", "noun", "welfare / well-being", "La sanidad universal es uno de los pilares del Estado del bienestar en España.")
            ],
            "ex_mc": [
                ("¿Qué artículo de la Constitución Española reconoce el derecho a la protección de la salud?", ["El artículo 43", "El artículo 1", "El artículo 155", "El artículo 2"], 0),
                ("¿Quién gestiona directamente los hospitales y centros de salud públicos en Ceuta y Melilla?", ["El Instituto Nacional de Gestión Sanitaria (INGESA), dependiente del Ministerio de Sanidad", "La Generalitat de Cataluña", "El Banco de España", "La Real Academia Española"], 0)
            ],
            "ex_fb": [
                ("En España, la gestión de la sanidad pública está transferida a las comunidades ___.", "autónomas", "In Spain, the management of public healthcare is devolved to the autonomous communities."),
                ("El Sistema Nacional de ___ se financia principalmente mediante los impuestos.", "Salud", "The National Health System is financed mainly through taxes.")
            ],
            "ex_sb": [
                (["La", "sanidad", "pública", "española", "se", "financia", "con", "los", "impuestos."], "Spanish public healthcare is funded through taxes.")
            ],
            "ex_dict": [
                ("Las comunidades autónomas gestionan los hospitales y centros de salud de su territorio.", "The autonomous communities manage the hospitals and health centers in their territory.")
            ]
        },
        {
            "num": "02",
            "title": "La Tarjeta Sanitaria Individual y el centro de salud",
            "objective": "Conocer los trámites para obtener la Tarjeta Sanitaria Individual (TSI) y el funcionamiento de la Atención Primaria y el médico de familia.",
            "grammar_title": "Oraciones finales y condicionales para trámites administrativos («para obtener..., es necesario...»)",
            "grammar_slug": "finales-condicionales-tramites-sanitarios",
            "grammar_Body": """Para explicar los pasos necesarios para acceder a un servicio público en España se usan **oraciones finales** (*para + infinitivo*) junto con **expresiones de requisito** (*es necesario, se requiere, hay que + infinitivo*):

- ***Para solicitar** la tarjeta sanitaria **es necesario estar empadronado** en el municipio.*
- ***Si** un paciente **necesita** acudir a un especialista, primero **debe pedir cita con** su médico de cabecera.*""",
            "story_title": "La puerta de entrada a la sanidad pública",
            "paragraphs": [
                "El documento personal e intransferible que acredita el derecho de cada ciudadano o residente a recibir atención médica en el Sistema Nacional de Salud es la Tarjeta Sanitaria Individual (TSI). La expide el servicio de salud de la comunidad autónoma donde reside el titular tras acreditar su identidad (DNI, NIE o pasaporte), su afiliación o derecho a la asistencia sanitaria en el Instituto Nacional de la Seguridad Social (INSS) y el certificado de empadronamiento en su ayuntamiento.",
                "Gracias a la interoperabilidad del sistema digital español, la Tarjeta Sanitaria permite tanto pedir cita médica como retirar medicamentos con receta electrónica en cualquier farmacia y recibir asistencia de urgencia cuando un residente se desplaza temporalmente a otra comunidad autónoma dentro de España. Para viajar por la Unión Europea, los ciudadanos solicitan además la Tarjeta Sanitaria Europea (TSE).",
                "El sistema sanitario español se estructura en dos grandes niveles asistenciales: la Atención Primaria y la Atención Especializada. La puerta de entrada habitual para cualquier problema de salud no urgente es el centro de salud (antiguamente llamado ambulatorio) del barrio o municipio correspondiente al domicilio del paciente.",
                "En el centro de salud cada adulto tiene asignado un médico de familia —también llamado popularmente «médico de cabecera»— y un profesional de enfermería, mientras que los menores de catorce años son atendidos por un médico pediatra. La cita previa puede solicitarse por teléfono, en el mostrador del centro o a través de la aplicación móvil del servicio autonómico de salud.",
                "Si tras la exploración el médico de familia considera que la dolencia requiere pruebas complejas o valoración específica, deriva al paciente mediante un volante a la Atención Especializada (cardiólogo, traumatólogo, oftalmólogo o dermatólogo) en el hospital o centro de especialidades."
            ],
            "questions": [
                ("¿Qué documento personal acredita el derecho de un residente a recibir asistencia en los centros de salud públicos de España?", ["La Tarjeta Sanitaria Individual (TSI)", "El carné de conducir tipo B", "El título de Bachillerato", "El abono de transporte mensual"], 0),
                ("¿A dónde debe acudir en primer lugar un ciudadano cuando tiene un problema de salud común que no es una urgencia grave?", ["Al centro de salud para consultar a su médico de familia (Atención Primaria)", "Directamente al quirófano de un hospital", "Al Ministerio de Justicia", "A la comisaría de Policía Nacional"], 0),
                ("¿Qué médico atiende específicamente a los niños en los centros de salud de Atención Primaria?", ["El pediatra", "El geriatra", "El notario", "El farmacéutico"], 0)
            ],
            "vocab": [
                ("la tarjeta sanitaria", "noun", "health insurance card (TSI)", "La tarjeta sanitaria es imprescindible para acudir al centro de salud y a la farmacia."),
                ("el centro de salud", "noun", "primary care health center", "El centro de salud ofrece atención primaria cerca del domicilio del ciudadano."),
                ("el médico de cabecera", "noun", "family doctor / general practitioner (GP)", "El médico de cabecera o médico de familia realiza el primer diagnóstico."),
                ("el pediatra", "noun", "pediatrician", "El pediatra cuida la salud y las vacunas de los niños hasta los catorce años."),
                ("la atención primaria", "noun", "primary healthcare", "La atención primaria resuelve la mayoría de las consultas médicas cotidianas."),
                ("la cita previa", "noun", "prior appointment", "Se puede pedir cita previa con el médico por teléfono o por internet."),
                ("el especialista", "noun", "medical specialist", "El médico de familia deriva al paciente al médico especialista cuando es necesario."),
                ("la receta electrónica", "noun", "electronic prescription", "Los medicamentos recetados se cargan directamente en la receta electrónica de la tarjeta.")
            ],
            "ex_mc": [
                ("¿Cómo se llama también al médico de familia que atiende en el centro de salud?", ["Médico de cabecera", "Procurador de los tribunales", "Inspector de hacienda", "Concejal de distrito"], 0),
                ("¿Qué tarjeta permite a los residentes en España recibir asistencia sanitaria pública durante una estancia temporal en otro país de la Unión Europea?", ["La Tarjeta Sanitaria Europea (TSE)", "La tarjeta del club de lectura", "El carné joven deportivo", "La tarjeta de embarque"], 0)
            ],
            "ex_fb": [
                ("Para ir a la consulta del médico de familia en el centro de salud hay que pedir ___ previa.", "cita", "To go to the family doctor's office at the health center you have to book a prior appointment."),
                ("La ___ Sanitaria Individual es el documento que identifica al paciente en el sistema público de salud.", "Tarjeta", "The Individual Health Card is the document that identifies the patient in the public health system.")
            ],
            "ex_sb": [
                (["El", "médico", "de", "cabecera", "trabaja", "en", "el", "centro", "de", "salud."], "The family doctor works at the health center.")
            ],
            "ex_dict": [
                ("Para acudir al médico especialista es necesario pasar primero por el médico de familia.", "To see a medical specialist it is necessary to first visit the family doctor.")
            ]
        },
        {
            "num": "03",
            "title": "Hospitales, urgencias médicas (112) y oficinas de farmacia",
            "objective": "Distinguir la atención hospitalaria y el servicio de emergencias 112 del funcionamiento de las farmacias y el copago farmacéutico.",
            "grammar_title": "Expresiones de obligación y gratuidad condicional («solo se dispensan con receta», «es gratuito»)",
            "grammar_slug": "obligacion-gratuidad-condicional-farmacia",
            "grammar_Body": """Para describir las normas de uso de las urgencias y las farmacias en España se emplean estructuras restrictivas con **solo / únicamente + con** y adjetivos de gratuidad:

- *Los antibióticos **solo se dispensan con** receta médica oficial.*
- *El teléfono de emergencias 112 **es totalmente gratuito** y funciona las veinticuatro horas del día.*
- *Las oficinas de farmacia **se identifican mediante** una cruz verde luminosa.*""",
            "story_title": "Cruces verdes y respuesta inmediata ante la emergencia",
            "paragraphs": [
                "Cuando una persona sufre una emergencia médica grave, un accidente de tráfico o un problema de salud repentino que pone en riesgo su vida, debe acudir a los Servicios de Urgencias de los hospitales o llamar de inmediato al número único europeo de emergencias: el 112. La llamada al 112 es gratuita, funciona las veinticuatro horas de los 365 días del año en toda España, atiende en varios idiomas y moviliza de forma coordinada ambulancias del 061 o SUMMA, bomberos y fuerzas de seguridad.",
                "En los hospitales públicos españoles se presta la Atención Especializada de alta complejidad, que incluye las intervenciones quirúrgicas, los ingresos hospitalarios, los partos, las pruebas diagnósticas avanzadas y los tratamientos oncológicos. Mientras el paciente permanece ingresado en un hospital público, toda la medicación y manutención que recibe es completamente gratuita.",
                "Fuera del hospital, los medicamentos solo pueden adquirirse legalmente en las oficinas de farmacia, fácilmente reconocibles en todas las calles y pueblos de España por una cruz de color verde luminosa en su fachada. Todas las farmacias están dirigidas por licenciados o graduados en Farmacia y se organizan mediante turnos rotatorios de «farmacias de guardia» para garantizar que siempre haya establecimientos abiertos por la noche y en días festivos.",
                "En España, medicamentos como los antibióticos, los ansiolíticos o los tratamientos crónicos solo se venden con receta médica. Cuando un medicamento está financiado por el Sistema Nacional de Salud y se retira con la receta electrónica de la Tarjeta Sanitaria, el ciudadano abona únicamente un porcentaje reducido del precio (aportación o copago farmacéutico) en función de su nivel de renta y de si es trabajador en activo o pensionista, estando exentos los colectivos más vulnerables.",
                "Asimismo, las farmacias españolas disponen de contenedores blancos especiales llamados «Puntos SIGRE», donde los ciudadanos depositan los envases vacíos y los medicamentos caducados para proteger el medio ambiente."
            ],
            "questions": [
                ("¿Qué símbolo luminoso identifica a todas las oficinas de farmacia en las calles de España?", ["Una cruz verde", "Un círculo azul con una estrella amarilla", "Un triángulo rojo invertido", "Una bandera blanca y negra"], 0),
                ("¿A qué número de teléfono gratuito hay que llamar en España ante cualquier emergencia médica grave o accidente?", ["Al 112", "Al 010", "Al 902", "Al 1004"], 0),
                ("¿Dónde se pueden comprar legalmente medicamentos con receta médica como los antibióticos en España?", ["Únicamente en las oficinas de farmacia", "En cualquier supermercado de alimentación", "En los quioscos de prensa", "En las gasolineras de carretera"], 0)
            ],
            "vocab": [
                ("la oficina de farmacia", "noun", "pharmacy / chemist's shop", "Las oficinas de farmacia están identificadas con una cruz verde luminosa."),
                ("la farmacia de guardia", "noun", "on-duty / 24-hour pharmacy", "Siempre hay una farmacia de guardia abierta por la noche para urgencias."),
                ("la cruz verde", "noun", "green cross (pharmacy sign)", "La cruz verde encendida indica que la farmacia se encuentra abierta al público."),
                ("el antibiótico", "noun", "antibiotic", "En España está prohibido vender antibióticos sin receta médica."),
                ("el servicio de urgencias", "noun", "emergency room / A&E department", "Los servicios de urgencias de los hospitales atienden las veinticuatro horas."),
                ("el copago farmacéutico", "noun", "pharmaceutical co-payment", "Con la receta de la Seguridad Social, el paciente solo paga una parte del medicamento."),
                ("el pensionista", "noun", "pensioner / retiree", "Los pensionistas tienen una aportación muy reducida o gratuita en las farmacias."),
                ("la ambulancia", "noun", "ambulance", "Al llamar al 112 se envía una ambulancia medicalizada al lugar del accidente.")
            ],
            "ex_mc": [
                ("¿Cómo se llaman las farmacias que permanecen abiertas fuera del horario comercial habitual, durante toda la noche y los días festivos?", ["Farmacias de guardia", "Farmacias de temporada", "Farmacias de aduana", "Farmacias de recreo"], 0),
                ("¿Es necesario presentar receta médica para comprar antibióticos en una farmacia española?", ["Sí, siempre es obligatoria la receta médica", "No, se venden libremente sin receta", "Solo los domingos por la tarde", "Solo para menores de diez años"], 0)
            ],
            "ex_fb": [
                ("Las oficinas de ___ en España se identifican en la calle con una cruz verde.", "farmacia", "Pharmacies in Spain are identified on the street by a green cross."),
                ("El número único y gratuito de teléfono para cualquier emergencia en España y en Europa es el ___.", "112", "The single free telephone number for any emergency in Spain and Europe is 112.")
            ],
            "ex_sb": [
                (["Las", "farmacias", "españolas", "se", "identifican", "con", "una", "cruz", "verde."], "Spanish pharmacies are identified with a green cross.")
            ],
            "ex_dict": [
                ("El teléfono gratuito de emergencias ciento doce funciona las veinticuatro horas del día.", "The free emergency telephone number 112 operates twenty-four hours a day.")
            ]
        },
        {
            "num": "04",
            "title": "La Organización Nacional de Trasplantes (ONT) y el liderazgo mundial",
            "objective": "Conocer el modelo español de donación y trasplante de órganos y el papel de la Organización Nacional de Trasplantes (ONT).",
            "grammar_title": "Construcciones temporales de continuidad («desde hace más de treinta años», «de forma ininterrumpida»)",
            "grammar_slug": "construcciones-temporales-continuidad-ont",
            "grammar_Body": """Para expresar acciones o liderazgos que comenzaron en el pasado y continúan en el presente se emplea el **presente de indicativo + desde hace + cantidad de tiempo** o **llevar + gerundio**:

- *España **es** líder mundial en donación y trasplante de órganos **desde hace más de treinta años**.*
- *La Organización Nacional de Trasplantes **lleva coordinando** el modelo español desde 1989.*""",
            "story_title": "El milagro solidario del modelo español de trasplantes",
            "paragraphs": [
                "Uno de los mayores motivos de orgullo de la sociedad y de la medicina española es su liderazgo mundial ininterrumpido durante más de tres décadas en donación y trasplante de órganos. Este éxito internacional se articula a través de la Organización Nacional de Trasplantes (ONT), un organismo público técnico dependiente del Ministerio de Sanidad creado en 1989 e impulsado por el doctor Rafael Matesanz.",
                "El llamado «modelo español de trasplantes», recomendado por la Organización Mundial de la Salud (OMS) e imitado en decenas de países, se basa en una red de coordinadores hospitalarios de trasplantes —en su mayoría médicos intensivistas y personal de enfermería— presentes dentro de cada hospital público, que detectan posibles donantes y acompañan con enorme sensibilidad a las familias en los momentos más difíciles.",
                "La legislación española sobre trasplantes se sustenta en los principios éticos de altruismo, voluntariedad, anonimato absoluto entre donante y receptor, equidad y gratuidad total. En España está estrictamente prohibido cualquier tipo de comercio o compensación económica por la donación de órganos, tejidos, células o sangre: los órganos se asignan exclusivamente según criterios clínicos de urgencia y compatibilidad médica dentro del Sistema Nacional de Salud.",
                "Más allá del excelente engranaje médico y logístico —que moviliza aviones, helicópteros y equipos quirúrgicos a cualquier hora del día o de la noche—, el factor decisivo del éxito español es la extraordinaria solidaridad ciudadana: más del ochenta y cinco por ciento de las familias españolas consultadas autoriza la donación de órganos de su familiar fallecido para salvar otras vidas.",
                "Cualquier ciudadano mayor de edad puede además manifestar su voluntad de ser donante solicitando gratuitamente la tarjeta de donante de órganos o inscribiéndolo en el Registro de Instrucciones Previas (testamento vital) de su comunidad autónoma."
            ],
            "questions": [
                ("¿En qué ámbito médico es España líder mundial de forma ininterrumpida desde hace más de treinta años?", ["En donación y trasplante de órganos", "En cirugía estética privada", "En fabricación de termómetros de mercurio", "En exportación de gafas de sol"], 0),
                ("¿Qué organismo dependiente del Ministerio de Sanidad coordina las donaciones y los trasplantes en toda España?", ["La Organización Nacional de Trasplantes (ONT)", "La Agencia Estatal de Meteorología (AEMET)", "El Instituto Cervantes", "La Sociedad Estatal de Correos"], 0),
                ("¿Cuáles son los principios legales de la donación de órganos y sangre en España?", ["Es voluntaria, altruista, anónima y totalmente gratuita", "Se paga según el precio del mercado financiero", "El receptor debe conocer y pagar a la familia del donante", "Solo está permitida entre personas del mismo municipio"], 0)
            ],
            "vocab": [
                ("la Organización Nacional de Trasplantes", "noun", "National Transplant Organization (ONT)", "La Organización Nacional de Trasplantes coordina los operativos médicos en toda España."),
                ("el trasplante de órganos", "noun", "organ transplant", "España ocupa el primer puesto mundial en trasplante de órganos por millón de habitantes."),
                ("el donante", "noun", "donor", "La generosidad de los donantes españoles y sus familias salva miles de vidas cada año."),
                ("el altruismo", "noun", "altruism / selflessness", "La donación de órganos y de sangre en España se rige por el principio de altruismo."),
                ("el anonimato", "noun", "anonymity", "La ley española garantiza el anonimato entre el donante de un órgano y su receptor."),
                ("el receptor", "noun", "recipient", "El paciente receptor recibe el trasplante sin ningún coste económico en la sanidad pública."),
                ("el testamento vital", "noun", "living will / advance healthcare directive", "En el testamento vital o documento de instrucciones previas se puede expresar el deseo de donar órganos."),
                ("la solidaridad", "noun", "solidarity", "La solidaridad ciudadana es la clave del liderazgo español en donación de órganos.")
            ],
            "ex_mc": [
                ("¿Qué significan las siglas ONT dentro del sistema sanitario español?", ["Organización Nacional de Trasplantes", "Oficina Nacional de Turismo", "Ordenanza de Nuevas Tecnologías", "Organismo de Navegación Terrestre"], 0),
                ("¿Se recibe dinero en España por donar sangre o donar un órgano?", ["No, la donación en España es siempre voluntaria, altruista y gratuita", "Sí, el hospital paga una tarifa fija por cada donación", "Sí, se descuenta de las multas de tráfico", "Depende de la comunidad autónoma"], 0)
            ],
            "ex_fb": [
                ("España es líder mundial en donación y ___ de órganos gracias a la solidaridad ciudadana y a la ONT.", "trasplante", "Spain is the world leader in organ donation and transplantation thanks to citizen solidarity and the ONT."),
                ("La Organización Nacional de Trasplantes depende del Ministerio de ___.", "Sanidad", "The National Transplant Organization reports to the Ministry of Health.")
            ],
            "ex_sb": [
                (["España", "es", "líder", "mundial", "en", "donación", "y", "trasplante", "de", "órganos."], "Spain is the world leader in organ donation and transplantation.")
            ],
            "ex_dict": [
                ("La donación de órganos y de sangre en España es voluntaria, altruista, anónima y gratuita.", "Organ and blood donation in Spain is voluntary, altruistic, anonymous, and free of charge.")
            ]
        },
        {
            "num": "05",
            "title": "Salud pública, prevención y normas sobre tabaco y alcohol",
            "objective": "Conocer las leyes españolas de salud pública sobre prohibición de fumar en espacios cerrados y prohibición de venta de alcohol y tabaco a menores de 18 años.",
            "grammar_title": "Expresiones de prohibición legal («está prohibido fumar», «se prohíbe la venta a menores de dieciocho años»)",
            "grammar_slug": "expresiones-prohibicion-legal-salud",
            "grammar_Body": """Las normas de salud pública en el examen CCSE se formulan mediante **estructuras de prohibición** (*estar prohibido + infinitivo*, *prohibirse + sustantivo*) y límites de edad (*menores de 18 años*):

- *En España **está prohibido fumar** en todos los espacios públicos cerrados y centros de trabajo.*
- ***Está prohibida la venta** de bebidas alcohólicas y tabaco **a los menores de dieciocho años**.*""",
            "story_title": "Convivencia saludable y protección de los menores",
            "paragraphs": [
                "Dentro de las políticas de salud pública y prevención de enfermedades en España destacan el calendario común de vacunación a lo largo de toda la vida —totalmente gratuito en los centros de salud para niños y adultos—, los programas de detección precoz del cáncer y las leyes reguladoras del consumo de tabaco y bebidas alcohólicas.",
                "Desde la entrada en vigor y ampliación de la Ley antitabaco en 2011, en España está terminantemente prohibido fumar en todos los espacios cerrados de uso público o colectivo: centros de trabajo, oficinas, bares, restaurantes, discotecas, estaciones, aeropuertos, trenes, autobuses y comercios. Tampoco está permitido fumar en espacios al aire libre especialmente sensibles, como los recintos de los hospitales, los centros educativos, los parques infantiles y las zonas de juego para menores.",
                "Asimismo, la legislación española protege de manera estricta a la infancia y la juventud frente a las adicciones: en todo el territorio nacional está prohibida la venta, entrega o suministro de tabaco y de cualquier tipo de bebida alcohólica a los menores de dieciocho años, que es la edad legal de mayoría de edad en España.",
                "En materia de seguridad vial y salud pública, tampoco está permitido conducir vehículos superando las tasas máximas legales de alcoholemia (y con tasa 0,0 para conductores menores de edad) ni bajo los efectos de drogas o estupefacientes, conductas que conllevan fuertes sanciones económicas, pérdida de puntos del carné de conducir e incluso penas de prisión.",
                "Por último, el Ministerio de Sanidad y las comunidades autónomas promueven campañas de alimentación saludable en los comedores escolares y la práctica regular de actividad física para prevenir la obesidad infantil y fomentar el envejecimiento activo."
            ],
            "questions": [
                ("¿Cuál es la edad mínima legal para poder comprar tabaco o bebidas alcohólicas en España?", ["18 años", "16 años", "21 años", "14 años"], 0),
                ("¿En cuál de los siguientes lugares está prohibido fumar en España según la ley vigente?", ["En el interior de bares, restaurantes, centros de trabajo, hospitales y colegios", "En el balcón privado de una vivienda particular", "En medio del campo abierto sin riesgo de incendio", "En una calle peatonal no escolar"], 0),
                ("¿Son gratuitas las vacunas incluidas en el calendario oficial infantil del Sistema Nacional de Salud?", ["Sí, se administran gratuitamente en los centros de salud públicos", "No, deben pagarse íntegramente en clínicas privadas", "Solo son gratuitas en el mes de agosto", "Solo para familias con más de cinco hijos"], 0)
            ],
            "vocab": [
                ("la mayoría de edad", "noun", "legal age of majority (18 in Spain)", "En España la mayoría de edad se alcanza a los dieciocho años."),
                ("el espacio público cerrado", "noun", "enclosed public space", "Está prohibido fumar en cualquier espacio público cerrado y centro de trabajo."),
                ("el calendario de vacunación", "noun", "vaccination schedule", "El calendario de vacunación infantil se administra gratis en el centro de salud."),
                ("la prevención", "noun", "prevention", "La medicina preventiva y las revisiones periódicas evitan enfermedades graves."),
                ("el recinto hospitalario", "noun", "hospital grounds / premises", "No se permite fumar ni siquiera en las zonas al aire libre del recinto hospitalario."),
                ("el parque infantil", "noun", "children's playground", "La ley prohíbe fumar en los parques infantiles y alrededores de los colegios."),
                ("la tasa de alcoholemia", "noun", "blood alcohol level", "La Guardia Civil y la Policía realizan controles de tasa de alcoholemia en carretera."),
                ("el menor de edad", "noun", "minor (person under 18)", "Está prohibido vender bebidas alcohólicas y tabaco a los menores de edad.")
            ],
            "ex_mc": [
                ("¿Está permitido fumar dentro de un restaurante, un bar cerrado o una oficina en España?", ["No, está prohibido en todos los espacios públicos cerrados y centros de trabajo", "Sí, después de las diez de la noche", "Sí, si el propietario del local da permiso verbal", "Sí, en las mesas cercanas a la ventana"], 0),
                ("¿A partir de qué edad se puede comprar alcohol legalmente en España?", ["A partir de los 18 años", "A partir de los 15 años", "A partir de los 16 años con carné de estudiante", "A partir de los 25 años"], 0)
            ],
            "ex_fb": [
                ("En España está prohibida la venta de tabaco y bebidas alcohólicas a los menores de ___ años.", "18", "In Spain the sale of tobacco and alcoholic beverages to minors under 18 years of age is prohibited."),
                ("La ley española prohíbe ___ en el interior de bares, restaurantes, colegios y hospitales.", "fumar", "Spanish law prohibits smoking inside bars, restaurants, schools, and hospitals.")
            ],
            "ex_sb": [
                (["En", "España", "está", "prohibido", "vender", "alcohol", "a", "menores", "de", "dieciocho", "años."], "In Spain it is prohibited to sell alcohol to minors under eighteen years of age.")
            ],
            "ex_dict": [
                ("Está prohibido fumar en todos los espacios públicos cerrados, hospitales y centros educativos.", "Smoking is prohibited in all enclosed public spaces, hospitals, and educational centers.")
            ]
        }
    ]
}


UNIT_30 = {
    "unit_num": 66,
    "slug": "educacion",
    "title": "El Sistema Educativo Español",
    "theme": "Enseñanza obligatoria (Primaria y ESO), Bachillerato, Formación Profesional, Universidad y becas en España (Tarea 5 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "Educación Infantil, Primaria y ESO: la enseñanza obligatoria y gratuita",
            "objective": "Conocer las etapas del sistema educativo español y comprender que la enseñanza básica (de 6 a 16 años: Primaria y ESO) es obligatoria y gratuita (art. 27 CE).",
            "grammar_title": "Expresiones de intervalo de edad y obligatoriedad («desde los seis hasta los dieciséis años», «es obligatoria»)",
            "grammar_slug": "intervalo-edad-obligatoriedad-educacion",
            "grammar_Body": """Para describir las etapas educativas en el examen CCSE se emplean preposiciones de límite temporal (**de... a...** o **desde los... hasta los... años**) y predicados nominales de carácter legal (**ser obligatorio y gratuito**):

- *La enseñanza básica en España **es obligatoria y gratuita desde los 6 hasta los 16 años**.*
- *La Educación Primaria **comprende de los 6 a los 12 años** y la ESO **va de los 12 a los 16 años**.*""",
            "story_title": "Diez años de escuela común para todos",
            "paragraphs": [
                "El artículo 27 de la Constitución Española reconoce el derecho fundamental de todas las personas a la educación y establece que «la enseñanza básica es obligatoria y gratuita». Al igual que ocurre con la sanidad, el Ministerio de Educación, Formación Profesional y Deportes fija las enseñanzas mínimas comunes para todo el Estado, mientras que las comunidades autónomas gestionan los colegios e institutos de su territorio.",
                "La primera etapa del sistema educativo es la Educación Infantil, que atiende a los niños desde el nacimiento hasta los seis años (0 a 6 años) dividida en dos ciclos (de 0 a 3 años en escuelas infantiles o guarderías, y de 3 a 6 años en los colegios). Aunque la Educación Infantil tiene carácter voluntario, el segundo ciclo (3 a 6 años) es gratuito en todos los centros sostenidos con fondos públicos y escolariza a la práctica totalidad de los niños en España.",
                "La enseñanza obligatoria y gratuita comienza a los seis años y se extiende hasta los dieciséis años de edad (de 6 a 16 años), abarcando diez cursos académicos divididos en dos etapas: la Educación Primaria y la Educación Secundaria Obligatoria (ESO).",
                "La Educación Primaria comprende seis cursos académicos, desde los seis hasta los doce años (6 a 12 años), y se imparte en los Colegios de Educación Infantil y Primaria (CEIP). Su objetivo es proporcionar a los alumnos una formación común en expresión y comprensión oral y escrita, lectura, cálculo, ciencias de la naturaleza, ciencias sociales, educación artística, educación física y lengua extranjera.",
                "Al cumplir los doce años, los alumnos pasan al Instituto de Educación Secundaria (IES) para cursar la Educación Secundaria Obligatoria (ESO), que consta de cuatro cursos académicos desde los doce hasta los dieciséis años (12 a 16 años). Quienes superan los cuatro cursos obtienen el título de Graduado en Educación Secundaria Obligatoria."
            ],
            "questions": [
                ("¿Entre qué edades es obligatoria y gratuita la enseñanza básica en España?", ["Desde los 6 hasta los 16 años", "Desde los 3 hasta los 18 años", "Desde los 0 hasta los 12 años", "Desde los 10 hasta los 21 años"], 0),
                ("¿Qué dos etapas educativas forman la enseñanza básica obligatoria en España?", ["La Educación Primaria (6-12 años) y la Educación Secundaria Obligatoria, ESO (12-16 años)", "La Educación Infantil y la Universidad", "El Bachillerato y el Doctorado", "Las Escuelas Oficiales de Idiomas y los Másteres"], 0),
                ("¿Qué carácter tiene la Educación Infantil (de 0 a 6 años) en España?", ["Es de carácter voluntario (no obligatoria)", "Es obligatoria desde los seis meses de vida", "Es exclusiva para mayores de doce años", "Solo existe en universidades"], 0)
            ],
            "vocab": [
                ("la enseñanza obligatoria", "noun", "compulsory education", "La enseñanza obligatoria y gratuita en España va de los seis a los dieciséis años."),
                ("la Educación Primaria", "noun", "Primary Education (ages 6–12)", "La Educación Primaria tiene seis cursos, desde los seis hasta los doce años."),
                ("la ESO", "noun", "Compulsory Secondary Education (ages 12–16)", "La ESO significa Educación Secundaria Obligatoria y dura cuatro cursos."),
                ("la Educación Infantil", "noun", "Early Childhood / Preschool Education (ages 0–6)", "La Educación Infantil se divide en dos ciclos de cero a tres y de tres a seis años."),
                ("el colegio", "noun", "primary school", "Los niños cursan la Educación Infantil y Primaria en el colegio."),
                ("el instituto", "noun", "secondary / high school (IES)", "Los adolescentes estudian la ESO y el Bachillerato en el instituto."),
                ("el curso académico", "noun", "academic year / school grade", "El curso académico escolar en España comienza en septiembre y termina en junio."),
                ("el título de Graduado en ESO", "noun", "Compulsory Secondary Education Certificate", "Al aprobar cuarto de la ESO se obtiene el título de Graduado en ESO.")
            ],
            "ex_mc": [
                ("¿Qué significan las siglas educativas ESO en España?", ["Educación Secundaria Obligatoria", "Escuela Superior de Oficios", "Estudios Sociales Optativos", "Enseñanza Semestral Ordinaria"], 0),
                ("¿Cuántos cursos dura la Educación Primaria en España (de los 6 a los 12 años)?", ["Seis cursos", "Dos cursos", "Cuatro cursos", "Diez cursos"], 0)
            ],
            "ex_fb": [
                ("En España, la enseñanza básica es obligatoria y ___ desde los 6 hasta los 16 años.", "gratuita", "In Spain, basic education is compulsory and free from 6 to 16 years of age."),
                ("La Educación Secundaria Obligatoria, conocida por las siglas ___, se cursa de los 12 a los 16 años.", "ESO", "Compulsory Secondary Education, known by the acronym ESO, is studied from ages 12 to 16.")
            ],
            "ex_sb": [
                (["La", "enseñanza", "básica", "es", "obligatoria", "y", "gratuita", "en", "España."], "Basic education is compulsory and free in Spain.")
            ],
            "ex_dict": [
                ("La Educación Primaria y la ESO forman la enseñanza obligatoria de los seis a los dieciséis años.", "Primary Education and ESO make up compulsory education from ages six to sixteen.")
            ]
        },
        {
            "num": "02",
            "title": "Bachillerato y Formación Profesional (FP)",
            "objective": "Distinguir las opciones educativas postobligatorias tras la ESO: el Bachillerato (16-18 años) y los Ciclos Formativos de Formación Profesional.",
            "grammar_title": "Disyuntivas de itinerario formativo («pueden optar entre... o...», «permite acceder a...»)",
            "grammar_slug": "disyuntivas-itinerario-formativo-fp",
            "grammar_Body": """Para describir los itinerarios académicos al finalizar la enseñanza obligatoria se usan verbos de elección y acceso (**optar por, elegir entre, dar acceso a, permitir cursar**):

- *Al obtener el título de la ESO, los estudiantes **pueden optar entre** cursar el Bachillerato **o** estudiar un Ciclo de Formación Profesional de Grado Medio.*
- *El título de Técnico Superior de FP **permite acceder directamente a** la universidad.*""",
            "story_title": "Dos caminos de excelencia hacia el futuro profesional",
            "paragraphs": [
                "Una vez finalizada la Educación Secundaria Obligatoria a los dieciséis años, se inicia la Educación Secundaria Postobligatoria. Los jóvenes que han obtenido el título de Graduado en ESO pueden elegir principalmente entre dos grandes caminos formativos en los institutos públicos y centros concertados o privados: el Bachillerato o la Formación Profesional (FP).",
                "El Bachillerato tiene una duración de dos cursos académicos, habitualmente entre los dieciséis y los dieciocho años (16 a 18 años). Su finalidad es proporcionar a los alumnos madurez intelectual y humana y prepararlos para acceder a los estudios superiores universitarios o de Formación Profesional de Grado Superior. Se organiza en diversas modalidades: Ciencias y Tecnología, Humanidades y Ciencias Sociales, Artes y modalidad General.",
                "Por su parte, la Formación Profesional (FP) está orientada a la cualificación práctica para el ejercicio de diversas profesiones en sectores como la informática, la sanidad, la hostelería, la electricidad, la administración o la automoción. Se estructura en tres niveles: los Ciclos de Grado Básico, los Ciclos Formativos de Grado Medio (a los que se accede con el título de la ESO y que otorgan el título de Técnico) y los Ciclos Formativos de Grado Superior (a los que se accede desde el Bachillerato o desde un Grado Medio y que otorgan el título de Técnico Superior).",
                "En los últimos años, España ha impulsado con gran éxito la llamada «FP Dual», un modelo que combina la formación teórica en el centro educativo con el aprendizaje práctico remunerado o en régimen de prácticas dentro de empresas reales, logrando tasas de inserción laboral muy elevadas.",
                "Además, el sistema educativo español contempla las Enseñanzas de Régimen Especial, que incluyen las enseñanzas artísticas profesionales de Música y Danza en los conservatorios, las Artes Plásticas y Diseño, las Enseñanzas Deportivas y el aprendizaje oficial de lenguas."
            ],
            "questions": [
                ("¿Cuántos cursos dura el Bachillerato en España (habitualmente entre los 16 y los 18 años)?", ["Dos cursos académicos", "Seis cursos académicos", "Un trimestre", "Cuatro cursos obligatorios"], 0),
                ("¿Qué estudios postobligatorios preparan de forma eminentemente práctica para un oficio o profesión mediante Ciclos Formativos de Grado Medio y de Grado Superior?", ["La Formación Profesional (FP)", "La Educación Infantil", "La Educación Primaria", "El Tribunal de Cuentas"], 0),
                ("¿Es obligatorio estudiar el Bachillerato en España?", ["No, el Bachillerato forma parte de la enseñanza secundaria postobligatoria (voluntaria)", "Sí, es obligatorio hasta los veinticinco años", "Sí, para poder obtener el DNI", "Solo es obligatorio en las ciudades autónomas"], 0)
            ],
            "vocab": [
                ("el Bachillerato", "noun", "Baccalaureate / upper secondary school (ages 16–18)", "El Bachillerato dura dos cursos y prepara para el acceso a la universidad."),
                ("la Formación Profesional", "noun", "Vocational Education and Training (FP)", "La Formación Profesional cuenta con una altísima inserción en el mercado laboral."),
                ("el ciclo formativo", "noun", "vocational training cycle (Grado Medio / Superior)", "Los ciclos formativos de Grado Medio y Grado Superior combinan teoría y práctica."),
                ("la FP Dual", "noun", "Dual Vocational Training (school + company)", "En la FP Dual el estudiante realiza parte de su aprendizaje dentro de una empresa."),
                ("la enseñanza postobligatoria", "noun", "post-compulsory education", "El Bachillerato y la Formación Profesional de Grado Medio son enseñanzas postobligatorias."),
                ("el Técnico Superior", "noun", "Higher Technician diploma (from Grado Superior FP)", "Al superar un ciclo de Grado Superior se obtiene el título de Técnico Superior."),
                ("el conservatorio", "noun", "music or dance conservatory", "Las enseñanzas oficiales de música y danza se imparten en los conservatorios."),
                ("la inserción laboral", "noun", "job placement / labor market integration", "La Formación Profesional facilita una rápida inserción laboral de los jóvenes.")
            ],
            "ex_mc": [
                ("¿Qué dos opciones principales tiene un estudiante en España al terminar la ESO a los 16 años si desea seguir estudiando?", ["Cursar el Bachillerato o un Ciclo Formativo de Formación Profesional (FP) de Grado Medio", "Entrar directamente a un Doctorado o jubilarse", "Volver a Educación Primaria o a Infantil", "Hacer el servicio militar obligatorio"], 0),
                ("¿Qué significan las siglas FP en el sistema educativo español?", ["Formación Profesional", "Facultad de Psicología", "Fondo Público", "Federación Provincial"], 0)
            ],
            "ex_fb": [
                ("El ___ dura dos cursos académicos, generalmente desde los 16 hasta los 18 años.", "Bachillerato", "The Baccalaureate lasts two academic years, generally from 16 to 18 years of age."),
                ("La ___ Profesional (FP) se organiza en ciclos formativos de Grado Básico, Grado Medio y Grado Superior.", "Formación", "Vocational Training (FP) is organized into Basic, Intermediate, and Higher level training cycles.")
            ],
            "ex_sb": [
                (["El", "Bachillerato", "dura", "dos", "cursos", "y", "no", "es", "obligatorio."], "The Baccalaureate lasts two years and is not compulsory.")
            ],
            "ex_dict": [
                ("Al terminar la ESO se puede estudiar el Bachillerato o la Formación Profesional.", "Upon finishing ESO, one can study the Baccalaureate or Vocational Training.")
            ]
        },
        {
            "num": "03",
            "title": "La Universidad española: PAU/EBAU, Grados, Posgrados y la UNED",
            "objective": "Conocer el acceso a la universidad (PAU/EBAU), la estructura de Bolonia (Grado, Máster y Doctorado) y el papel de la UNED.",
            "grammar_title": "Léxico institucional universitario y oraciones relativas explicativas",
            "grammar_slug": "lexico-universitario-relativas-explicativas",
            "grammar_Body": """Para explicar la organización universitaria española adaptada al Espacio Europeo de Educación Superior (EEES) se emplean **oraciones de relativo explicativas** entre comas:

- *Los estudios universitarios se estructuran en tres ciclos: **el Grado, que dura generalmente cuatro años; el Máster; y el Doctorado**.*
- *La **UNED, que es la Universidad Nacional de Educación a Distancia**, depende del Estado y permite estudiar desde cualquier lugar.*""",
            "story_title": "Ocho siglos de tradición académica y enseñanza a distancia",
            "paragraphs": [
                "España cuenta con una de las tradiciones universitarias más antiguas de Europa, iniciada en el siglo XIII con la fundación de la Universidad de Salamanca en 1218. En la actualidad existen en España cerca de noventa universidades —tanto públicas como privadas— integradas en el Espacio Europeo de Educación Superior (EEES o Plan Bolonia), lo que facilita la movilidad de estudiantes mediante programas como las becas europeas Erasmus+.",
                "Para acceder a los estudios de Grado en una universidad española tras haber aprobado el Bachillerato, los estudiantes deben superar una prueba oficial de acceso conocida tradicionalmente como «Selectividad» y denominada oficialmente Prueba de Acceso a la Universidad (PAU o EBAU). La nota de admisión se calcula combinando la calificación media del Bachillerato (60 %) con la nota obtenida en esta prueba (40 %). También existen pruebas específicas de acceso a la universidad para personas mayores de 25, 40 y 45 años.",
                "Las enseñanzas universitarias oficiales se dividen en tres ciclos sucesivos: el primer ciclo es el Grado (que suele tener una duración de cuatro cursos académicos o 240 créditos ECTS, salvo carreras como Medicina o Arquitectura, que son más largas); el segundo ciclo es el Máster Universitario de especialización (de uno o dos años); y el tercer ciclo es el Doctorado, que culmina con la defensa de una tesis doctoral original.",
                "Dentro del sistema público merece una mención especial la Universidad Nacional de Educación a Distancia (UNED), fundada en 1972. Es la única universidad pública de ámbito estatal no transferida a las comunidades autónomas y ofrece estudios universitarios semipresenciales y en línea a través de centros asociados en toda España y en el extranjero, facilitando el estudio a quienes trabajan o tienen responsabilidades familiares.",
                "El máximo órgano de representación e interlocución de las universidades españolas es la Conferencia de Rectores de las Universidades Españolas (CRUE), mientras que en cada universidad la máxima autoridad académica elegida por la comunidad universitaria es el Rector o Rectora."
            ],
            "questions": [
                ("¿Cómo se llama la universidad pública española de ámbito nacional que imparte enseñanza superior a distancia y por internet?", ["La UNED (Universidad Nacional de Educación a Distancia)", "La ESO", "La RENFE", "La ONT"], 0),
                ("¿Cómo se llama la prueba oficial que deben superar los alumnos de Bachillerato para entrar en la universidad española?", ["Prueba de Acceso a la Universidad (PAU / EBAU, conocida como Selectividad)", "Examen CCSE del Instituto Cervantes", "Inspección Técnica de Vehículos", "Oposición a notarías"], 0),
                ("¿Cuáles son los tres niveles o ciclos de los estudios universitarios oficiales en España?", ["Grado, Máster y Doctorado", "Primaria, Secundaria y Bachillerato", "Infantil, Básico y Medio", "Iniciación, Intermedio y Avanzado"], 0)
            ],
            "vocab": [
                ("la Prueba de Acceso a la Universidad", "noun", "University Entrance Exam (PAU / EBAU / Selectividad)", "Para estudiar una carrera tras el Bachillerato hay que aprobar la Prueba de Acceso a la Universidad."),
                ("el Grado universitario", "noun", "Bachelor's degree (4-year university degree)", "Los estudios de Grado universitario suelen durar cuatro años académicos."),
                ("el Máster", "noun", "Master's degree", "El Máster universitario permite especializarse tras finalizar el Grado."),
                ("el Doctorado", "noun", "Doctorate / PhD", "El Doctorado termina con la lectura y defensa de una tesis doctoral."),
                ("la UNED", "noun", "National Distance Education University", "La UNED permite cursar carreras universitarias a distancia desde cualquier ciudad."),
                ("el Rector", "noun", "University Rector / President", "El Rector es la máxima autoridad académica de una universidad española."),
                ("la beca Erasmus", "noun", "Erasmus European mobility scholarship", "España es el país europeo que recibe más estudiantes universitarios con beca Erasmus."),
                ("la matrícula", "noun", "tuition / enrollment fee", "Los estudiantes abonan las tasas de matrícula al inicio del curso universitario.")
            ],
            "ex_mc": [
                ("¿Cuál es la universidad más antigua de España, fundada en el año 1218 en Castilla y León?", ["La Universidad de Salamanca", "La Universidad de La Laguna", "La Universidad Politécnica de Cartagena", "La Universidad Rey Juan Carlos"], 0),
                ("¿Existen en España pruebas especiales de acceso a la universidad para personas adultas que no tienen el Bachillerato?", ["Sí, existen pruebas específicas para mayores de 25, 40 y 45 años", "No, después de los 20 años está prohibido entrar en la universidad", "Solo para deportistas olímpicos", "Solo en universidades extranjeras"], 0)
            ],
            "ex_fb": [
                ("La ___ es la Universidad Nacional de Educación a Distancia de España.", "UNED", "UNED is Spain's National Distance Education University."),
                ("Los tres ciclos de los estudios universitarios en España son el ___, el Máster y el Doctorado.", "Grado", "The three cycles of university studies in Spain are the Bachelor's Degree (Grado), Master's, and Doctorate.")
            ],
            "ex_sb": [
                (["La", "UNED", "es", "la", "Universidad", "Nacional", "de", "Educación", "a", "Distancia."], "UNED is the National Distance Education University.")
            ],
            "ex_dict": [
                ("Para acceder a la universidad desde el Bachillerato es necesario superar la prueba de acceso.", "To enter university from the Baccalaureate it is necessary to pass the entrance exam.")
            ]
        },
        {
            "num": "04",
            "title": "Tipos de centros educativos, becas y participación familiar (AMPA)",
            "objective": "Distinguir entre colegios públicos, concertados y privados, y conocer el sistema de becas públicas y los órganos de participación escolar (Consejo Escolar y AMPA).",
            "grammar_title": "Clasificación tripartita y adjetivos participiales («sostenidos con fondos públicos», «concertados»)",
            "grammar_slug": "clasificacion-tripartita-centros-educativos",
            "grammar_Body": """Para clasificar las instituciones educativas según su titularidad y financiación se emplean **participios adjetivales** y estructuras comparativas:

- *Los **centros públicos** son de titularidad estatal o autonómica y totalmente gratuitos.*
- *Los **centros privados concertados** son de titularidad privada pero están **sostenidos con fondos públicos** mediante conciertos educativos.*
- *Los **centros privados** se financian íntegramente con las cuotas que abonan las familias.*""",
            "story_title": "Comunidad educativa e igualdad de oportunidades",
            "paragraphs": [
                "El sistema educativo español garantiza tanto el derecho a la educación como la libertad de enseñanza y de creación de centros docentes reconocidos en el artículo 27 de la Constitución. Por esta razón, en España conviven tres tipos de centros escolares no universitarios: los centros públicos, los centros privados concertados y los centros privados.",
                "Los colegios e institutos públicos son de titularidad de las administraciones públicas (comunidades autónomas o ayuntamientos), son laicos y gratuitos en todas sus enseñanzas obligatorias. Por su parte, los colegios concertados son de titularidad privada, pero firman un acuerdo o «concierto» con la comunidad autónoma por el cual reciben financiación pública a cambio de impartir gratuitamente la enseñanza obligatoria y aplicar los mismos criterios públicos de admisión de alumnos que los centros públicos.",
                "Finalmente, los colegios privados no concertados son empresas o fundaciones privadas que no reciben subvención pública y se financian íntegramente mediante las mensualidades que abonan las familias de los alumnos matriculados.",
                "Para garantizar que ningún estudiante abandone sus estudios por motivos económicos, el Ministerio de Educación, Formación Profesional y Deportes y las comunidades autónomas convocan anualmente un amplio sistema de becas y ayudas al estudio (las conocidas «becas MEC»), destinadas tanto a estudios postobligatorios (Bachillerato, FP y Universidad) como a ayudas de comedor escolar, transporte y compra de libros de texto para familias con menores ingresos.",
                "La democracia participativa también se vive dentro de cada colegio e instituto a través de dos instituciones fundamentales: el Consejo Escolar —órgano colegiado de gobierno donde están representados la dirección, los profesores, los padres y los propios alumnos— y la AMPA (Asociación de Madres y Padres de Alumnos), que organiza actividades extraescolares y canaliza las propuestas de las familias."
            ],
            "questions": [
                ("¿Qué son los colegios concertados en España?", ["Centros de titularidad privada pero financiados con fondos públicos en las etapas obligatorias", "Colegios exclusivos para músicos profesionales de concierto", "Universidades extranjeras sin sede en España", "Academias nocturnas de conducción"], 0),
                ("¿Qué significan las siglas AMPA en los colegios e institutos españoles?", ["Asociación de Madres y Padres de Alumnos", "Agencia Municipal de Protección Ambiental", "Archivo de Museos del Patrimonio Antiguo", "Asamblea de Médicos de Primer Auxilio"], 0),
                ("¿Qué ministerio convoca cada año las becas generales de estudio para estudiantes de Bachillerato, FP y Universidad en toda España?", ["El Ministerio de Educación, Formación Profesional y Deportes", "El Ministerio de Defensa", "El Ministerio del Interior", "El Ministerio de Transportes"], 0)
            ],
            "vocab": [
                ("el colegio público", "noun", "state / public school", "El colegio público es gratuito y está gestionado por la comunidad autónoma."),
                ("el colegio concertado", "noun", "state-subsidized private school", "El colegio concertado es de titularidad privada pero está financiado con fondos públicos."),
                ("el colegio privado", "noun", "independent private school", "En un colegio privado las familias pagan íntegramente el coste de la enseñanza."),
                ("la beca de estudio", "noun", "study grant / scholarship", "El Ministerio de Educación concede becas de estudio según la renta familiar y el rendimiento."),
                ("la AMPA", "noun", "Parents' Association (Asociación de Madres y Padres de Alumnos)", "La AMPA organiza excursiones y actividades extraescolares en el colegio."),
                ("el Consejo Escolar", "noun", "School Governing Council", "Profesores, padres y alumnos participan en las decisiones del centro a través del Consejo Escolar."),
                ("el comedor escolar", "noun", "school canteen / dining hall", "Las comunidades autónomas ofrecen becas de comedor escolar para las familias."),
                ("la actividad extraescolar", "noun", "extracurricular activity", "El deporte, el teatro y los idiomas son actividades extraescolares muy habituales por la tarde.")
            ],
            "ex_mc": [
                ("¿Cuáles son los tres tipos de centros escolares no universitarios que existen en España según su titularidad y financiación?", ["Públicos, concertados y privados", "Militares, aduaneros y consulares", "Provinciales, insulares y comarcales", "Forales, senatoriales y judiciales"], 0),
                ("¿En qué órgano de gobierno de un colegio o instituto participan conjuntamente el equipo directivo, los profesores, los padres y los alumnos?", ["En el Consejo Escolar", "En el Consejo de Estado", "En la Junta Electoral Central", "En el Tribunal Constitucional"], 0)
            ],
            "ex_fb": [
                ("Los colegios ___ son de titularidad privada pero reciben financiación pública para impartir la enseñanza obligatoria.", "concertados", "State-subsidized schools (concertados) are privately owned but receive public funding to provide compulsory education."),
                ("La ___ es la Asociación de Madres y Padres de Alumnos de un centro educativo.", "AMPA", "The AMPA is the Parents' Association of an educational center.")
            ],
            "ex_sb": [
                (["En", "España", "existen", "colegios", "públicos,", "concertados", "y", "privados."], "In Spain there are public, state-subsidized, and private schools.")
            ],
            "ex_dict": [
                ("El Ministerio de Educación convoca becas y ayudas al estudio para garantizar la igualdad de oportunidades.", "The Ministry of Education announces scholarships and study grants to guarantee equal opportunities.")
            ]
        },
        {
            "num": "05",
            "title": "Homologación de títulos, educación de adultos y Escuelas Oficiales de Idiomas (EOI)",
            "objective": "Conocer el procedimiento de homologación de títulos extranjeros en España y el papel de las Escuelas Oficiales de Idiomas (EOI) y los centros de adultos.",
            "grammar_title": "Sustantivos deverbales de procedimiento administrativo («la homologación», «la convalidación», «la expedición»)",
            "grammar_slug": "sustantivos-deverbales-homologacion",
            "grammar_Body": """En el lenguaje administrativo del examen CCSE abundan los **sustantivos abstractos derivados de verbos** terminados en *-ción* para designar trámites oficiales:

- ***La homologación** de un título extranjero le otorga los mismos efectos académicos y profesionales que el título español equivalente.*
- ***La certificación** oficial de idiomas se realiza en las Escuelas Oficiales de Idiomas (EOI).*""",
            "story_title": "Reconocimiento de estudios y aprendizaje a lo largo de la vida",
            "paragraphs": [
                "Para los ciudadanos extranjeros que se establecen en España o adquieren la nacionalidad española, el reconocimiento oficial de los estudios cursados en su país de origen es un paso clave para trabajar o continuar formándose. Este trámite administrativo se denomina «homologación» o «equivalencia» de títulos extranjeros.",
                "La homologación de títulos no universitarios (como el equivalente al Bachillerato o a la Formación Profesional) corresponde al Ministerio de Educación, Formación Profesional y Deportes o a las comunidades autónomas que tienen transferida esta competencia, mientras que la homologación de títulos universitarios superiores (para ejercer profesiones reguladas como médico, abogado, ingeniero o profesor) es competencia del Ministerio de Ciencia, Innovación y Universidades.",
                "Además, el sistema educativo español promueve el aprendizaje a lo largo de toda la vida mediante los Centros de Educación de Personas Adultas (CEPA), centros públicos y gratuitos donde cualquier persona mayor de dieciocho años puede obtener el título de Graduado en ESO, prepararse para las pruebas de acceso a la Formación Profesional o a la Universidad, o asistir a cursos de español y competencias digitales.",
                "Otro pilar singular y muy valorado de la enseñanza pública en España es la red de Escuelas Oficiales de Idiomas (EOI). Las EOI son centros públicos no universitarios dependientes de las consejerías de educación de las comunidades autónomas dedicados exclusivamente a la enseñanza especializada de lenguas modernas a precios públicos muy reducidos.",
                "En las Escuelas Oficiales de Idiomas se imparten y certifican oficialmente todos los niveles del Marco Común Europeo de Referencia para las Lenguas (desde el nivel básico A1 y A2 hasta los niveles intermedios B1 y B2 y avanzados C1 y C2), incluyendo lenguas extranjeras, las lenguas cooficiales de España y el español como lengua extranjera (cuyos certificados de nivel A2 o superior también eximen de realizar el examen DELE para el trámite de nacionalidad)."
            ],
            "questions": [
                ("¿Cómo se llaman los centros públicos españoles dedicados específicamente a la enseñanza y certificación oficial de lenguas extranjeras, cooficiales y español?", ["Las Escuelas Oficiales de Idiomas (EOI)", "Las Cámaras de Comercio Exterior", "Los Registros de la Propiedad", "Los Colegios de Notarios"], 0),
                ("¿Cómo se llama el trámite oficial mediante el cual España reconoce la validez académica y profesional de un título de estudios obtenido en el extranjero?", ["La homologación (o equivalencia) de títulos", "El empadronamiento municipal", "La declaración de la renta", "La inspección técnica"], 0),
                ("¿Qué nivel mínimo de español del Marco Común Europeo de Referencia se exige acreditar (mediante diploma DELE o certificado de Escuela Oficial de Idiomas) a los solicitantes de nacionalidad española cuya lengua materna no es el español?", ["El nivel A2 (o superior)", "El nivel C2 exclusivamente", "Ningún nivel de idioma", "Solo un examen de latín clásico"], 0)
            ],
            "vocab": [
                ("la homologación de títulos", "noun", "official recognition / homologation of foreign degrees", "La homologación de títulos extranjeros permite ejercer una profesión regulada en España."),
                ("la Escuela Oficial de Idiomas", "noun", "Official School of Languages (EOI)", "Las Escuelas Oficiales de Idiomas son centros públicos que certifican los niveles A1 a C2."),
                ("el Marco Común Europeo", "noun", "Common European Framework of Reference for Languages (CEFR)", "Los niveles A1, A2, B1, B2, C1 y C2 pertenecen al Marco Común Europeo."),
                ("la educación de personas adultas", "noun", "adult education (CEPA)", "Los centros de educación de personas adultas permiten obtener la ESO a mayores de dieciocho años."),
                ("el diploma DELE", "noun", "Diploma of Spanish as a Foreign Language (DELE)", "El diploma DELE A2 o superior acredita el conocimiento de la lengua española para la nacionalidad."),
                ("la profesión regulada", "noun", "regulated profession (doctor, lawyer, engineer)", "Para ejercer una profesión regulada en España es obligatorio homologar el título universitario."),
                ("la convalidación", "noun", "credit transfer / validation of partial studies", "La universidad realiza la convalidación de asignaturas superadas en otro centro."),
                ("el aprendizaje permanente", "noun", "lifelong learning", "Las administraciones educativas fomentan el aprendizaje permanente en todas las edades.")
            ],
            "ex_mc": [
                ("¿Qué significan las siglas EOI dentro del sistema educativo público español?", ["Escuela Oficial de Idiomas", "Estatuto de Organización Industrial", "Estación de Observación Invernal", "Entidad de Obras Internacionales"], 0),
                ("Si un ciudadano extranjero no hispanohablante solicita la nacionalidad española por residencia, ¿qué dos pruebas oficiales del Instituto Cervantes debe superar (salvo exención por título oficial)?", ["La prueba CCSE (conocimientos constitucionales y socioculturales) y el examen de idioma DELE (mínimo A2)", "El examen de conducir y la Selectividad", "La prueba de natación y el examen de contabilidad", "Únicamente una entrevista telefónica en inglés"], 0)
            ],
            "ex_fb": [
                ("El trámite para que un título extranjero tenga validez oficial en España se llama ___ de títulos.", "homologación", "The procedure for a foreign degree to have official validity in Spain is called degree homologation."),
                ("Las Escuelas Oficiales de ___ (EOI) son centros públicos donde se estudian y certifican lenguas modernas.", "Idiomas", "The Official Schools of Languages (EOI) are public centers where modern languages are studied and certified.")
            ],
            "ex_sb": [
                (["Las", "Escuelas", "Oficiales", "de", "Idiomas", "son", "centros", "públicos", "de", "enseñanza."], "Official Schools of Languages are public educational centers.")
            ],
            "ex_dict": [
                ("La homologación de títulos extranjeros permite continuar estudios o ejercer profesiones en España.", "The homologation of foreign degrees makes it possible to continue studies or practice professions in Spain.")
            ]
        }
    ]
}


if __name__ == "__main__":
    for u in (UNIT_28, UNIT_29, UNIT_30):
        emit_unit_from_dict(u)
    print("Units 28, 29, and 30 generated successfully.")
