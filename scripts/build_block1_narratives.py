"""
Generates rich, detailed narrative stories for Block 1 (Units 01-06, 30 lessons).
Units:
01: precolombina
02: civilizaciones
03: llegadaeuropeos
04: conquista
05: sociedadcolonial
06: economiacolonial

Embeds every grammar sentence directly from reqs JSON to ensure 100% verbatim accuracy.
"""

import json
import os

reqs = json.load(open('scripts/block1_all_reqs.json', encoding='utf-8'))

def G(lesson_key, idx):
    return reqs[lesson_key]['grammar_sentences'][idx]

STORIES = {}

# =============================================================================
# UNIT 01: precolombina
# =============================================================================

# 01.01: precolombina-01
k = "precolombina-01"
# Grammar (4):
# 0: A lo largo de casi quince mil kilómetros, cientos de pueblos distintos habían desarrollado formas de vida adaptadas a paisajes completamente diferentes.
# 1: Las enfermedades mataron a tanta gente, y tan rápido, que ni siquiera hubo tiempo de contarla.
# 2: El maíz terminó cultivándose a lo largo de todo el continente, mientras que la papa se convirtió en la base de la alimentación andina.
# 3: Mucho antes de que existieran los mayas, los mexica o los incas, ya se habían desarrollado civilizaciones influyentes.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Los orígenes del poblamiento americano y los primeros cultivos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante la última glaciación del Pleistoceno, hace más de quince mil años, bandas de cazadores-recolectores cruzaron el puente terrestre de Beringia entre Siberia y Alaska. En su marcha milenaria hacia el sur, estos primeros pobladores se adaptaron a selvas tropicales, desiertos áridos y altiplanos andinos. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En Mesoamérica y en los valles interandinos, la domesticación de plantas silvestres desató una revolución agrícola fundamental para la humanidad. {G(k, 2)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"En las tierras altas de Perú y Bolivia, la papa y la quinua permitieron sustentar densas poblaciones en alturas donde el maíz no maduraba. Los agricultores precolombinos desarrollaron una botánica sofisticada sin herramientas de hierro ni animales de tiro."
        },
        {
            "type": "narration",
            "text": f"Siglos más tarde, la llegada europea interrumpiría de forma trágica esta trayectoria milenaria autónoma. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": "Esta rica despensa biológica y civilizatoria sentó las bases para el surgimiento de las grandes civilizaciones urbanas del continente."
        }
    ]
}

# 01.02: precolombina-02
k = "precolombina-02"
# Grammar (5):
# 0: Los mayas se organizaron en decenas de ciudades-estado independientes.
# 1: Muchas ciudades mayas del sur fueron abandonadas repentinamente.
# 2: Todavía se debate por qué fueron abandonadas.
# 3: Cuzco se convirtió en el centro político y religioso de todo el imperio.
# 4: La información de los quipus todavía no se ha logrado descifrar del todo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Mesoamérica y los Andes: ciudades de piedra y quipus",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Entre el 1500 antes de Cristo y la llegada europea, florecieron en América complejas sociedades estatales con arquitectura monumental y precisos conocimientos astronómicos."
        },
        {
            "type": "narration",
            "text": f"En las selvas de Guatemala, Honduras y la península de Yucatán, {G(k, 0)} como Tikal, Palenque, Calakmul y Copán, gobernadas por dinastías divinas de reyes 'k'uhul ajaw'."
        },
        {
            "type": "narration",
            "text": f"Hacia el siglo nueve de nuestra era, {G(k, 1)} en las tierras bajas. {G(k, 2)} Sequías prolongadas, sobrepoblación y guerras endémicas figuran entre las causas más analizadas por los arqueólogos."
        },
        {
            "type": "narration",
            "text": f"En el ámbito andino, el Tahuantinsuyo incaico articuló un territorio de más de cuatro mil kilómetros a lo largo de la cordillera. {G(k, 3)} Los administradores registraban censos y tributos mediante un sofisticado sistema de cuerdas anudadas. {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": "A través del sistema de correos de chasquis y terrazas de cultivo, las civilizaciones precolombinas dominaron los ecosistemas más hostiles del planeta."
        }
    ]
}

# 01.03: precolombina-03
k = "precolombina-03"
# Grammar (4):
# 0: En el imperio inca, el poder se organizaba de forma muy distinta.
# 1: Se exigía tributo a las ciudades sometidas, pero rara vez se sustituía a sus gobernantes locales.
# 2: La sangre derramada se ofrecía a los dioses.
# 3: El ritual se representaba en estelas de piedra que todavía pueden verse hoy.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Cosmovisión, dioses y rituales sagrados",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Para los pueblos precolombinos, el universo era un organismo vivo en constante equilibrio entre fuerzas cósmicas complementarias. En Mesoamérica, los mexicas creían que los sacrificios humanos mantenían el movimiento del Quinto Sol. {G(k, 2)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"En el panteón mesoamericano, deidades como Quetzalcóatl y Tláloc regían las lluvias, el viento y la fertilidad de la tierra. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} El Sapa Inca gobernaba como hijo sagrado del Sol (Inti) y articulaba el imperio mediante lazos de reciprocidad y redistribución con los curacas de cada ayllu."
        },
        {
            "type": "narration",
            "text": "En los Andes, la Pachamama y los Apus recibían ofrendas de chicha, coca y camélidos en reciprocidad por las cosechas agrícolas."
        },
        {
            "type": "narration",
            "text": "El calendario sagrado regía cada actividad humana, entrelazando el tiempo cósmico con los ciclos agrícolas y las ceremonias comunitarias."
        }
    ]
}

# 01.04: precolombina-04
k = "precolombina-04"
# Grammar (4):
# 0: Cocinando los granos con cal o ceniza, los pueblos mesoamericanos liberaban nutrientes que el maíz crudo no ofrece.
# 1: El chocolate se preparaba batiendo cacao molido con agua, chile y especias hasta formar espuma.
# 2: Masticando hojas de coca, los habitantes de las alturas combatían el hambre, el frío y el mal de altura.
# 3: Comerciando, tejiendo o cultivando, la mayoría de la gente también encontraba tiempo para el juego de pelota.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Tecnología agrícola: chinampas, andenes y domesticación botánica",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El florecimiento demográfico de Mesoamérica y los Andes fue posible gracias a extraordinarias obras de ingeniería hidráulica y agronómica. En el valle de México, los mexicas inventaron la nixtamalización. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"El cacao era un grano sagrado de altísimo valor que servía como moneda y bebida ritual de la élite. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"En la accidentada cordillera de los Andes, los incas transformaron las laderas verticales en andenes escalonados de piedra con canales de riego por gravedad. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Este deporte sagrado representaba la lucha cósmica entre los astros en canchas de piedra presentes desde el norte de México hasta Centroamérica."
        },
        {
            "type": "narration",
            "text": "Esta maestría ecológica demostró que las civilizaciones americanas desarrollaron modelos de sostenibilidad ambiental de avanzada sofisticación técnica."
        }
    ]
}

# 01.05: precolombina-05
k = "precolombina-05"
# Grammar (4):
# 0: A pesar de que los mayas escribían con un sistema jeroglífico completo, hoy solo sobreviven cuatro libros mayas originales.
# 1: A raíz de ese acto, y de otras destrucciones similares durante la conquista, casi toda la literatura maya escrita desapareció para siempre.
# 2: A pesar de las lagunas y las pérdidas, cada fuente aporta una pieza distinta.
# 3: A raíz de descubrimientos recientes, la imagen del mundo precolombino sigue cambiando.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Fuentes, códices y debates arqueológicos contemporáneos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Reconstruir la historia del mundo precolombino plantea fascinantes desafíos metodológicos a la ciencia histórica y a la arqueología moderna. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En julio de 1562, fray Diego de Landa ordenó el trágico Auto de Fe de Maní, donde decenas de códices de corteza de amate fueron arrojados a las llamas. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Crónicas indígenas como las de Guaman Poma de Ayala y el Popol Vuh maya quiché dialogan con testimonios epigráficos tallados en estelas de piedra."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} La tecnología LiDAR ha revelado en la selva del Petén y en el Amazonas inmensas ciudades y calzadas antes invisibles bajo la densa vegetación."
        },
        {
            "type": "narration",
            "text": "Cada nuevo hallazgo confirma que América precolombina no era un desierto virgen, sino un continente densamente poblado y profundamente transformado por civilizaciones deslumbrantes."
        }
    ]
}

# =============================================================================
# UNIT 02: civilizaciones
# =============================================================================

# 02.01: civilizaciones-01
k = "civilizaciones-01"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Los olmecas: cultura madre de Mesoamérica",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En las llanuras costeras del golfo de México, entre Veracruz y Tabasco, floreció entre el 1200 y el 400 antes de Cristo la cultura olmeca. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En centros ceremoniales como San Lorenzo, La Venta y Tres Zapotes, los olmecas esculpieron colosales cabezas de basalto de hasta veinte toneladas de peso transportadas desde las montañas de los Tuxtlas. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Los olmecas idearon el juego de pelota ritual, el culto al jaguar y las primeras nociones del calendario ritual mesoamericano de 260 días. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"Redes de intercambio de jade y obsidiana difundieron su estilo artístico hasta los valles de Oaxaca y el altiplano central. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "La herencia olmeca definió las pautas estéticas, religiosas y urbanísticas que heredarían mayas, zapotecos y teotihuacanos."
        }
    ]
}

# 02.02: civilizaciones-02
k = "civilizaciones-02"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Teotihuacan y los mayas: metrópolis del periodo Clásico",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante el primer milenio de nuestra era, Mesoamérica alcanzó su edad de oro urbanística y científica. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En el altiplano central, Teotihuacan albergó a más de 125.000 habitantes en una cuadrícula perfecta dominada por la Pirámide del Sol, la Pirámide de la Luna y la Calzada de los Muertos. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Simultáneamente, en las tierras bajas mayas, astrónomos y matemáticos desarrollaron el concepto del cero y el sistema vigesimal posicional. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"En ciudades como Copán y Palenque, el rey K'inich Janaab' Pakal erigió templos funerarios con textos jeroglíficos que narraban su linaje sagrado. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "El colapso del Clásico reconfiguraría el equilibrio geopolítico mesoamericano hacia nuevas confederaciones militaristas."
        }
    ]
}

# 02.03: civilizaciones-03
k = "civilizaciones-03"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Horizonte Chavín, Moche y Wari en los Andes",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En los Andes centrales, siglos antes del surgimiento incaico, diversas culturas desarrollaron complejas tradiciones artísticas y arquitectónicas. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En la sierra norte del Perú, el centro ceremonial de Chavín de Huántar funcionó como un gran oráculo panandino. {G(k, 1)} El Lanzón Monolítico y las Cabezas Clavas infundían pavor sagrado a los peregrinos."
        },
        {
            "type": "narration",
            "text": f"En la costa desértica norteña, los moches dominaron la metalurgia del oro y la cerámica escultórica realista. {G(k, 2)} El hallazgo de la tumba intacta del Señor de Sipán en 1987 deslumbró al mundo por su suntuosidad áurea."
        },
        {
            "type": "narration",
            "text": f"Más tarde, el Imperio Wari y Tiwanaku en el lago Titicaca sentaron el modelo de red vial y centros administrativos provinciales. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Esta milenaria acumulación de saberes agrícolas, textiles e hidráulicos proporcionó el cimiento sobre el cual los incas edificarían su imperio."
        }
    ]
}

# 02.04: civilizaciones-04
k = "civilizaciones-04"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Imperio mexica: la hegemonía de la Triple Alianza",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Tras una larga peregrinación desde Aztlán, los mexicas fundaron México-Tenochtitlan en 1325 en un islote pantanoso del lago de Texcoco. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En 1428, bajo el mando de Itzcóatl, los mexicas formaron la Triple Alianza con Texcoco y Tlacopan, derrotando a los tepanecas de Azcapotzalco. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"En su apogeo bajo Moctezuma II, Tenochtitlan era una metrópolis deslumbrante de más de 200.000 habitantes comunicada por calzadas elevadas, acueductos y diques. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"En el inmenso mercado de Tlatelolco, más de cincuenta mil personas comerciaban cacao, plumas de quetzal, mantas de algodón y jade. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Sin embargo, el cobro despiadado de tributos y la captura de cautivos para las 'guerras floridas' generaron un profundo rencor en pueblos sometidos como los tlaxcaltecas y totonacas."
        }
    ]
}

# 02.05: civilizaciones-05
k = "civilizaciones-05"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Tahuantinsuyo incaico: organización, mita y redistribución",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A partir de la victoria de Pachacútec sobre los chancas en 1438, el reino del Cuzco se transformó en el mayor imperio de la América precolombina: el Tahuantinsuyo. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"El imperio se dividió en cuatro suyos articulados por el Qhapaq Ñan, una colosal red vial pavimentada de más de treinta mil kilómetros con puentes colgantes de ichu. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"La economía incaica no utilizaba moneda ni mercados privados. {G(k, 2)} Funcionaba bajo los principios andinos de reciprocidad (ayni y minka) y redistribución estatal a través de almacenes imperiales (colcas)."
        },
        {
            "type": "narration",
            "text": f"Mediante la 'mita', las comunidades tributaban trabajo por turnos en obras públicas, templos y andenerías a cambio de protección y banquetes ceremoniales. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Santuarios como Machu Picchu y la fortaleza de Sacsayhuamán evidenciaron una maestría en el tallado y ensamble de bloques ciclópeos de piedra sin argamasa que desafía el paso de los siglos."
        }
    ]
}

# =============================================================================
# UNIT 03: llegadaeuropeos
# =============================================================================

# 03.01: llegadaeuropeos-01
k = "llegadaeuropeos-01"
# Grammar (4):
# 0: Cristóbal Colón partió del puerto de Palos de la Frontera el 3 de agosto de 1492 con tres barcos.
# 1: El 12 de octubre, un marinero de la Pinta llamado Rodrigo de Triana avistó tierra por primera vez.
# 2: Colón murió en 1506 sin admitir jamás que no había llegado a Asia.
# 3: En 1507, un cartógrafo alemán llamado Martin Waldseemüller publicó un mapa que bautizó el nuevo continente.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "1492: la travesía del Atlántico y el encuentro de dos mundos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En el siglo quince, la caída de Constantinopla en manos del Imperio Otomano en 1453 forzó a las monarquías ibéricas a buscar rutas marítimas alternativas hacia las especias y sedas de Asia."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} la Santa María, la Pinta y la Niña, tras convencer a los Reyes Católicos Isabel de Castilla y Fernando de Aragón en las Capitulaciones de Santa Fe."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} en la isla de Guanahaní (Bahamas), bautizada por los españoles como San Salvador y habitada por el pacífico pueblo taíno."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} convencido de haber arribado a las costas del Cipango o de las Indias orientales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} con el nombre de 'América' en honor al navegante florentino Américo Vespucio, quien reconoció que se trataba de una 'Mundus Novus'."
        }
    ]
}

# 03.02: llegadaeuropeos-02
k = "llegadaeuropeos-02"
# Grammar (4):
# 0: Al principio, el encuentro fue relativamente pacífico. Sin embargo, esa primera impresión cambió con rapidez.
# 1: Mientras los españoles buscaban oro, empezaron a exigir a los taínos que entregaran una cantidad fija de metal.
# 2: Al mismo tiempo, se estableció un sistema conocido como encomienda.
# 3: Después llegó un factor todavía más devastador que la violencia directa: las enfermedades europeas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Los taínos de las Antillas y el choque inicial",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A la llegada de los europeos en 1492, las islas del Caribe estaban densamente pobladas por el pueblo taíno, una sociedad agrícola organizada en cacicazgos. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"Los taínos cultivaban yuca en montones de tierra fertilizada (conucos), maíz, tabaco y batatas, y vivían en armonía comunitaria en bohíos y caneyes. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Los colonos impusieron el tributo del 'cascabel de Flandes' lleno de polvo de oro y el trabajo forzado en lavaderos de ríos. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"La quiebra de la agricultura tradicional, las hambrunas y el desarraigo provocaron una crisis humanitaria fulminante. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "En pocas décadas, la población taína de La Española, Cuba y Puerto Rico fue diezmada casi por completo, marcando el inicio del mayor colapso demográfico de la historia."
        }
    ]
}

# 03.03: llegadaeuropeos-03
k = "llegadaeuropeos-03"
# Grammar (4):
# 0: Al ver cómo se maltrataba a su pueblo, Hatuey huyó a Cuba con un grupo de seguidores.
# 1: Allí se organizó una resistencia armada contra los españoles.
# 2: Se cuenta que Hatuey preguntó si los españoles también iban a ese cielo.
# 3: En 1533 se firmó un acuerdo de paz que reconocía la libertad de Enriquillo y de su gente.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Resistencia indígena en el Caribe: Hatuey y Enriquillo",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Frente a la violencia y el despojo de los conquistadores, los pueblos caribeños ofrecieron una tenaz resistencia armada. {G(k, 0)} {G(k, 1)} en la región oriental de la isla, emboscando a las tropas de Diego Velázquez."
        },
        {
            "type": "narration",
            "text": f"Capturado tras una traición en 1512, Hatuey fue condenado a morir quemado vivo en la hoguera en Yara. Un sacerdote franciscano le ofreció bautizarse para ir al paraíso cristiano. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": "Ante la respuesta afirmativa del fraile, el cacique respondió que prefería ir al infierno para no encontrarse de nuevo con hombres tan crueles."
        },
        {
            "type": "narration",
            "text": f"Años más tarde, en las montañas de Bahoruco en La Española, el cacique Enriquillo encabezó una rebelión guerrillera de catorce años (1519-1533). {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "La dignidad de Hatuey y Enriquillo demostró que los pueblos originarios defendieron su libertad hasta las últimas consecuencias."
        }
    ]
}

# 03.04: llegadaeuropeos-04
k = "llegadaeuropeos-04"
# Grammar (4):
# 0: Debido a que la población indígena del Caribe ya se había reducido drásticamente, los colonos recurrieron al tráfico de personas esclavizadas desde África.
# 1: Por eso, muchos historiadores consideran la caña de azúcar uno de los motores principales detrás del comercio transatlántico de esclavos.
# 2: La población indígena no tenía ninguna inmunidad, ya que estos patógenos habían evolucionado junto a los animales domesticados de Eurasia.
# 3: Como resultado de esta catástrofe demográfica, millones de hectáreas de tierras de cultivo volvieron a cubrirse de bosque.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La catástrofe demográfica y el intercambio colombino",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El contacto entre el Viejo y el Nuevo Mundo desencadenó una profunda transformación biológica y ecológica conocida como el 'Intercambio Colombino'. {G(k, 2)} La viruela, el sarampión, el tifus y la gripe se propagaron con velocidad fulminante."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 1)} Las grandes plantaciones de azúcar exigían miles de brazos para el corte de caña en los trópicos caribeños y brasileños."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} provocando una alteración climática global en el siglo diecisiete."
        },
        {
            "type": "narration",
            "text": "El maíz, la papa, el tomate, el cacao y el tabaco enriquecieron las dietas de Europa y Asia, mientras caballos, vacas, trigo y enfermedades redefinían la ecología americana."
        },
        {
            "type": "narration",
            "text": "El choque biológico constituyó una de las fuerzas más determinantes y silenciosas en el desenlace de la conquista colonial."
        }
    ]
}

# 03.05: llegadaeuropeos-05
k = "llegadaeuropeos-05"
# Grammar (4):
# 0: Durante siglos se habló de 'descubrimiento', una palabra que asumía que América no existía realmente hasta que Europa la encontró.
# 1: Los primeros cálculos fueron publicados por historiadores a quienes hoy se llama 'contadores bajos'.
# 2: Investigaciones posteriores, cuyos autores revisaron fuentes coloniales con más detalle, elevaron esa cifra a cien millones.
# 3: Un ejemplo célebre es la Virgen de Guadalupe, cuya aparición se sitúa en 1531 en el cerro del Tepeyac.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Debates demográficos y sincretismo cultural",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"La magnitud del impacto de la conquista europea ha sido objeto de apasionadas controversias historiográficas a lo largo del último siglo. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} como Ángel Rosenblat, quienes sostenían que la población prehispánica no superaba los trece millones de habitantes en 1492."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} La Escuela de Berkeley estimó que solo el México central albergaba veinticinco millones de personas, reducidas a poco más de un millón hacia 1600."
        },
        {
            "type": "narration",
            "text": f"En el plano religioso y simbólico, los pueblos indígenas respondieron a la evangelización forzosa mediante un sofisticado sincretismo cultural. {G(k, 3)} sobre el antiguo templo de la diosa Tonantzin."
        },
        {
            "type": "narration",
            "text": "Bajo los ropajes del santoral católico, las comunidades preservaron secretamente sus cultos a los antepasados y a las fuerzas sagradas de la naturaleza."
        }
    ]
}

# =============================================================================
# UNIT 04: conquista
# =============================================================================

# 04.01: conquista-01
k = "conquista-01"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La caída de México-Tenochtitlan: Cortés y la alianza tlaxcalteca",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En febrero de 1519, Hernán Cortés zarpó de Cuba con quinientos hombres, dieciséis caballos y once barcos, desembarcando en las costas de Veracruz. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"Con la ayuda de Malintzin (doña Marina), Cortés comprendió las profundas fracturas políticas del imperio mexica. {G(k, 1)} Los tlaxcaltecas aportaron más de cien mil guerreros al ejército invasor."
        },
        {
            "type": "narration",
            "text": f"Tras la matanza del Templo Mayor y la expulsión española en la 'Noche Triste' en junio de 1520, la viruela segó la vida del tlatoani Cuitláhuac. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"Cortés botó trece bergantines armados con cañones en el lago y sitió Tenochtitlan durante noventa y tres días. {G(k, 3)} El 13 de agosto de 1521, el último gobernante mexica, Cuauhtémoc, fue capturado."
        },
        {
            "type": "narration",
            "text": "Sobre las ruinas humeantes de los templos piramidales se levantaron los cimientos de la Ciudad de México virreinal."
        }
    ]
}

# 04.02: conquista-02
k = "conquista-02"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Cajamarca y el colapso del Tahuantinsuyo: Pizarro y Atahualpa",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En 1532, Francisco Pizarro y Diego de Almagro desembarcaron en el norte del Perú al frente de ciento sesenta y ocho soldados de fortuna. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"El imperio incaico acababa de desangrarse en una fratricida guerra sucesoria entre Huáscar y su medio hermano Atahualpa, desatada tras la muerte del emperador Huayna Cápac por viruela. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"El 16 de noviembre de 1532 en la plaza de Cajamarca, fray Vicente de Valverde leyó el Requerimiento. Tras rechazar el fraile la Biblia arrojada al suelo, la caballería española emboscó al cortejo incaico. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"Prisionero, Atahualpa ofreció llenar una habitación de oro y dos de plata a cambio de su libertad. A pesar de entregarse el fabuloso tesoro, el Inca fue ejecutado en julio de 1533. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Pizarro marchó sobre el Cuzco y fundó la Ciudad de los Reyes (Lima) en la costa en 1535."
        }
    ]
}

# 04.03: conquista-03
k = "conquista-03"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Fronteras indómitas: la Guerra de Arauco y los chichimecas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A diferencia de los imperios centralizados de Tenochtitlan y Cuzco, los pueblos descentralizados opusieron una resistencia feroz e infranqueable. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En el sur de Chile, en las selvas y humedales del río Biobío, el pueblo mapuche enfrentó a las huestes de Pedro de Valdivia. {G(k, 1)} Líderes como Lautaro y Caupolicán adoptaron el caballo europeo y diseñaron tácticas de caballería ligera."
        },
        {
            "type": "narration",
            "text": f"En la batalla de Tucapel en 1553, Valdivia fue derrotado y ejecutado, y en el Desastre de Curalaba en 1598 los mapuches expulsaron a los españoles al norte del Biobío, forzando a la Corona a reconocer una frontera soberana en los 'Parlamentos'. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"En los áridos desiertos del norte de México, la Guerra Chichimeca (1550-1600) paralizó las rutas de la plata hacia Zacatecas. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "La conquista fue un proceso desigual e inacabado que tardó siglos en someter las periferias del continente."
        }
    ]
}

# 04.04: conquista-04
k = "conquista-04"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La controversia de Valladolid: Bartolomé de las Casas y Sepúlveda",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Los abusos sistemáticos contra las poblaciones indígenas desataron una profunda crisis moral y jurídica en el seno de la monarquía hispánica. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En 1511 en Santo Domingo, el fraile dominico Antonio de Montesinos tronó desde el púlpito contra la servidumbre impuesta a los indígenas. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"En 1550, el emperador Carlos V suspendió todas las conquistas y convocó a un debate formal en el Colegio de San Gregorio de Valladolid. {G(k, 2)} Juan Ginés de Sepúlveda defendió la guerra justa y la servidumbre natural aristotélica."
        },
        {
            "type": "narration",
            "text": f"Fray Bartolomé de las Casas argumentó que todos los pueblos del mundo son plenamente humanos y que la única vía legítima era la evangelización pacífica. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Aunque las Leyes Nuevas de 1542 intentaron abolir la encomienda hereditaria, en América los colonos se rebelaron bajo el lema 'Se acata pero no se cumple'."
        }
    ]
}

# 04.05: conquista-05
k = "conquista-05"
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Leyenda Negra y la Leyenda Rosa: mitos y realidades",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"La memoria histórica sobre la conquista de América ha estado profundamente polarizada desde el siglo dieciséis hasta nuestros días. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"Por un lado, la 'Leyenda Negra', promovida por Inglaterra y Holanda a través de grabados de Theodor de Bry, retrató a los conquistadores como crueles y fanáticos. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Por otro lado, la 'Leyenda Rosa' hispanista ensalzó la empresa colonial como una misión civilizadora desinteresada que llevó el cristianismo y el idioma a pueblos bárbaros. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} La historiografía contemporánea rechaza ambas simplificaciones propagandísticas."
        },
        {
            "type": "narration",
            "text": "Comprender la conquista exige analizar la violencia descarnada, la catástrofe epidemiológica, el protagonismo de las alianzas indígenas y el surgimiento de una sociedad mestiza compleja y contradictoria."
        }
    ]
}

# =============================================================================
# UNIT 05: sociedadcolonial
# =============================================================================

# 05.01: sociedadcolonial-01
k = "sociedadcolonial-01"
# Grammar (4):
# 0: El virreinato de Nueva España fue creado en 1535; el virreinato del Perú fue establecido en 1542.
# 1: Fueron creados dos virreinatos adicionales, el de Nueva Granada y el del Río de la Plata.
# 2: Todo el comercio con las colonias estaba controlado por una sola institución, la Casa de Contratación.
# 3: Este sistema fue diseñado para mantener el control sobre un territorio enorme.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La administración imperial: virreinatos, audiencias y cabildos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Para gobernar un continente situado a miles de kilómetros de distancia, la Corona española construyó un formidable andamiaje burocrático centralizado."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} con sede en la Ciudad de México y en Lima, encabezados por virreyes que gobernaban como alter ego del monarca. En el siglo dieciocho, las Reformas Borbónicas impulsaron cambios: {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Las Reales Audiencias funcionaron como tribunales superiores de justicia y órganos de control gubernativo. {G(k, 2)} en Sevilla y luego en Cádiz."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} En el ámbito local, los Cabildos representaban a los vecinos propietarios de las ciudades, encargándose del abasto de trigo, la policía y los aranceles urbanos."
        },
        {
            "type": "narration",
            "text": "A través de los 'juicios de residencia', los altos funcionarios debían rendir cuentas públicas al concluir sus mandatos."
        }
    ]
}

# 05.02: sociedadcolonial-02
k = "sociedadcolonial-02"
# Grammar (4):
# 0: En la práctica, se favorecía sistemáticamente a la 'república de españoles' sobre la 'república de indios'.
# 1: Para acceder a la universidad o a un cargo público, se exigía presentar un certificado de 'limpieza de sangre'.
# 2: Se reservaban los cargos más altos casi exclusivamente para los peninsulares.
# 3: Con el tiempo, se acumuló tanto resentimiento en torno a esta exclusión que buena parte del liderazgo independentista saldría de esas familias.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La sociedad estamental: 'República de Españoles' y 'República de Indios'",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El orden jurídico colonial dividió formalmente a la población en dos estamentos separados. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En la cúspide se situaban los peninsulares nacidos en España. {G(k, 2)} Los criollos, hijos de españoles nacidos en América, poseían haciendas y minas pero padecían discriminación burocrática."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Los indígenas habitaban pueblos de indios con cabildos propios y tierras comunales protegidas, pagando tributo al rey y sujetos a la mita."
        },
        {
            "type": "narration",
            "text": "En el fondo de la escala estamental, cientos de miles de africanos esclavizados y sus descendientes carecían de derechos civiles y sostenían las plantaciones."
        }
    ]
}

# 05.03: sociedadcolonial-03
k = "sociedadcolonial-03"
# Grammar (4):
# 0: Enseñando la doctrina cristiana mientras aprendían y usaban el idioma guaraní, los jesuitas lograron una relación menos violenta.
# 1: Estas comunidades, produciendo tejidos y ganado mientras desarrollaban una notable tradición musical, llegaron a ser económicamente prósperas.
# 2: Las reducciones, dependiendo casi por completo de la administración jesuita, entraron en rápida decadencia tras la expulsión.
# 3: Vigilando la ortodoxia religiosa mientras construía hospitales, escuelas y universidades, la Iglesia funcionó como una de las instituciones más poderosas del imperio.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Iglesia católica, las órdenes religiosas y las misiones jesuíticas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Mediante el Real Patronato Indiano concedido por el Papa, los reyes de España ejercieron un control casi absoluto sobre la Iglesia católica en América."
        },
        {
            "type": "narration",
            "text": f"Franciscanos, dominicos y agustinos bautizaron a millones de indígenas y construyeron majestuosos conventos-fortaleza en el siglo dieciséis. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"En las selvas del Paraguay y los ríos Paraná y Uruguay, la Compañía de Jesús fundó treinta reducciones guaraníes. {G(k, 0)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"En 1767, la expulsión de los jesuitas decretada por Carlos III desarticuló las misiones. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": "El Tribunal del Santo Oficio de la Inquisición persiguió la herejía en Lima, México y Cartagena, consolidando la hegemonía doctrinaria colonial."
        }
    ]
}

# 05.04: sociedadcolonial-04
k = "sociedadcolonial-04"
# Grammar (4):
# 0: A raíz de las Leyes de Indias, promulgadas en 1573, prácticamente todas las nuevas ciudades siguieron el mismo patrón.
# 1: A lo largo del día, esa plaza y sus alrededores se llenaban de actividad.
# 2: Como consecuencia de esa actividad constante, la plaza funcionaba como el verdadero centro social de la ciudad.
# 3: La vida cotidiana colonial, a raíz de sus propias tensiones de género, de clase y de costumbre, generaba conflictos tan reales como los grandes debates políticos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La ciudad colonial: cuadrícula, plaza mayor y vida cotidiana",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"La fundación de ciudades fue el instrumento primordial de ocupación y control del territorio americano por parte de la Corona hispánica. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"El trazado en damero con calles rectas nacía de una gran Plaza Mayor donde se emplazaban la catedral, el palacio virreinal y el cabildo. {G(k, 1)} {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"Las casonas señoriales de piedra con patios interiores contrastaban con las modestas viviendas de adobe y paja de los arrabales periféricos."
        },
        {
            "type": "narration",
            "text": f"Campanas de iglesias marcaban el ritmo de las horas, las procesiones y las fiestas reales. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Las urbes virreinales fueron el crisol donde nació el mestizaje lingüístico, culinario y musical que define a la cultura hispanoamericana."
        }
    ]
}

# 05.05: sociedadcolonial-05
k = "sociedadcolonial-05"
# Grammar (4):
# 0: Los territorios fueron administrados mediante virreinatos y audiencias que respondían a una corona lejana.
# 1: Las oportunidades económicas y políticas fueron distribuidas de forma muy desigual entre peninsulares, criollos, indígenas y africanos.
# 2: Las estructuras educativas y sanitarias fueron mantenidas, en gran medida, por una Iglesia que actuaba casi como un segundo gobierno.
# 3: Buena parte del trazado urbano actual fue diseñado directamente por una ley real de 1573.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El sistema de castas y el legado institucional colonial",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El orden virreinal hispanoamericano dejó una huella profunda e indeleble en las estructuras sociales y territoriales de América Latina. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} La pigmentocracia colonial consagró privilegios de linaje que perdurarían mucho después de la independencia."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Colegios mayores, universidades y hospitales dependían de órdenes religiosas que acumulaban inmensos patrimonios territoriales."
        },
        {
            "type": "narration",
            "text": f"En el plano urbanístico, {G(k, 3)} conservándose la plaza central como corazón cívico de pueblos y metrópolis."
        },
        {
            "type": "narration",
            "text": "Comprender la sociedad colonial resulta indispensable para analizar las tensiones de clase, etnia y poder que definirían el siglo diecinueve republicano."
        }
    ]
}

# =============================================================================
# UNIT 06: economiacolonial
# =============================================================================

# 06.01: economiacolonial-01
k = "economiacolonial-01"
# Grammar (4):
# 0: En 1545 fue descubierto el yacimiento de plata del Cerro Rico de Potosí.
# 1: A partir de 1554, la producción de plata fue transformada por un nuevo método inventado por Bartolomé de Medina.
# 2: Gran parte de esa plata fue acuñada en monedas, los llamados 'reales de a ocho'.
# 3: La minería colonial fue organizada para abastecer de metales preciosos a la metrópoli.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El cerro de Potosí y las venas abiertas de la plata",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"La minería de metales preciosos constituyó el motor indiscutido y la razón de ser de la economía colonial hispanoamericana. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} en el Alto Perú (actual Bolivia), un cerro cónico a más de cuatro mil metros de altura que albergaba las mayores vetas argentíferas de la historia."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Este método de amalgamación con mercurio o 'beneficio de patio' redujo drásticamente los costos de extracción del mineral. El mercurio de Huancavelica alimentó los hornos de Potosí."
        },
        {
            "type": "narration",
            "text": f"Hacia 1650, Potosí contaba con 160.000 habitantes, superando a Londres o Sevilla. En su Casa de la Moneda, {G(k, 2)} que se convirtieron en la primera moneda de curso legal global desde Madrid hasta Pekín."
        },
        {
            "type": "narration",
            "text": "La plata americana financió las guerras imperiales de los Austrias en Europa mientras miles de mitayos perecían en las profundidades de las galerías."
        }
    ]
}

# 06.02: economiacolonial-02
k = "economiacolonial-02"
# Grammar (4):
# 0: En la encomienda se concedía a un colono español el derecho a la mano de obra de una comunidad indígena.
# 1: En 1542 se promulgaron las Leyes Nuevas, que intentaron limitar el poder de los encomenderos.
# 2: Con el tiempo, se fue sustituyendo la encomienda por el repartimiento.
# 3: En 1550, en Valladolid, se organizó un debate formal sobre si los indígenas tenían plena condición humana.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Trabajo forzado: encomienda, mita y repartimiento",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Para extraer la riqueza mineral y cultivar los campos, la Corona implantó diversos sistemas de explotación y tributación de la mano de obra indígena."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} con la obligación teórica de protegerlos y cristianizarlos. {G(k, 1)} para frenar el feudalismo de los encomenderos y evitar la extinción de los tributarios."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} En los Andes, el virrey Francisco de Toledo reglamentó en 1572 la mita minera: una séptima parte de los varones indígenas de dieciséis provincias debía marchar anualmente a Potosí."
        },
        {
            "type": "narration",
            "text": f"Los abusos generaron intensos debates teológicos. {G(k, 3)} Las Casas defendió la libertad indígena frente a Ginés de Sepúlveda."
        },
        {
            "type": "narration",
            "text": "La extracción de riqueza colonial descansó sobre el sufrimiento y la resistencia silenciosa de millones de trabajadores originarios."
        }
    ]
}

# 06.03: economiacolonial-03
k = "economiacolonial-03"
# Grammar (4):
# 0: El azúcar fue el producto más importante, aumentando constantemente la demanda europea a medida que el consumo se popularizaba.
# 1: El ingenio azucarero, combinando maquinaria pesada, grandes hornos y mano de obra intensiva, funcionaba casi como una fábrica temprana.
# 2: Un pequeño grupo de familias acumuló fortunas cultivando y exportando cacao, convirtiéndose en una de las élites más influyentes.
# 3: En las vegas cubanas se cultivaba un tabaco que, produciendo cosechas de gran calidad, se ganaría fama mundial.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Plantaciones y haciendas: azúcar, cacao y tabaco",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Junto a la minería, la agricultura de exportación a gran escala conformó el segundo gran pilar productivo del imperio."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} en los valles costeros del noreste de Brasil (Pernambuco y Bahía) y en las Antillas mayores. {G(k, 1)} sostenido por el trabajo forzoso de millones de cautivos africanos."
        },
        {
            "type": "narration",
            "text": f"En los valles de Caracas y Guayaquil, {G(k, 2)} los 'grandes cacaos', terratenientes criollos que controlaban los cabildos y comerciaban con Nueva España y Europa."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} La Corona estableció el estanco real del tabaco para monopolizar sus jugosas rentas impositivas."
        },
        {
            "type": "narration",
            "text": "La hacienda y la plantación modelaron el paisaje rural y fijaron una estructura agraria desigual que condicionaría el desarrollo económico del continente."
        }
    ]
}

# 06.04: economiacolonial-04
k = "economiacolonial-04"
# Grammar (4):
# 0: A lo largo de casi todo el periodo colonial, el comercio legal estuvo organizado mediante un sistema de flotas.
# 1: Como consecuencia de restricciones tan estrictas, se desarrolló un comercio ilegal, o contrabando.
# 2: A lo largo de dos siglos y medio, el llamado Galeón de Manila navegó anualmente entre Acapulco y Manila.
# 3: Como consecuencia directa de esta ruta, ciudades como Acapulco se transformaron en mercados temporales enormes.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Monopolio comercial, flotas y galeones y contrabando",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Para asegurarse el control exclusivo de los tesoros indianos, la monarquía hispánica instauró un rígido monopolio comercial mediante el régimen de puerto único en Sevilla y Cádiz."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} Los convoyes de navíos mercantes escoltados por galeones de guerra zarpaban dos veces al año hacia Veracruz y Portobelo para protegerse de piratas ingleses, franceses y holandeses."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Comerciantes británicos y holandeses desembarcaban sedas, herramientas y esclavos en el Río de la Plata y las costas venezolanas burlando las aduanas reales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} la Nao de China intercambió plata mexicana por porcelanas finas, especias y sedas asiáticas. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "El sistema monopólico mercantilista ahogó la industria local americana y convirtió a las colonias en un apetecido botín para las potencias marítimas rivales."
        }
    ]
}

# 06.05: economiacolonial-05
k = "economiacolonial-05"
# Grammar (4):
# 0: Cantidades históricamente inéditas de plata y oro fueron enviadas desde América hacia España.
# 1: Buena parte de la plata fue simplemente utilizada para pagar deudas de guerra.
# 2: Los precios de bienes y servicios fueron empujados al alza durante generaciones.
# 3: Los beneficios de esta economía fueron distribuidos de forma extremadamente desigual.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El impacto global: la Revolución de los Precios y el legado colonial",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El masivo flujo de metales preciosos extraídos de América transformó las finanzas y el comercio del planeta entero."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} En el siglo dieciséis, más de dieciséis mil toneladas de plata arribaron a los muelles de Sevilla. {G(k, 1)} con banqueros genoveses y flamencos sin fomentar la manufactura interna española."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} en lo que los economistas denominaron la 'Revolución de los Precios', cuadruplicando el costo de vida en Europa."
        },
        {
            "type": "narration",
            "text": f"En América, la economía colonial dejó una impronta imborrable de concentración de tierras, primarización productiva y dependencia externa. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": "Comprender la economía virreinal resulta indispensable para explicar los dilemas estructurales de subdesarrollo y desigualdad que marcarían la historia republicana de América Latina."
        }
    ]
}

OUTPUT_DIR = "content/es-latam/stories/world/b1"

def main():
    for fname, data in STORIES.items():
        path = os.path.join(OUTPUT_DIR, fname)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        words = sum(len(p["text"].split()) for p in data["paragraphs"])
        print(f"Wrote {fname}: {words} words, {len(data['paragraphs'])} paras")

if __name__ == "__main__":
    main()
