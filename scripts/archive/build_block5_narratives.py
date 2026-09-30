"""
Generates rich, detailed narrative stories for Block 5 (Units 25-30, 30 lessons).
Units:
25: represionpolitica
26: centroamerica
27: conosur
28: crisisdeuda
29: neoliberalismo
30: democratizacion

Embeds every grammar sentence directly from reqs JSON to ensure 100% verbatim accuracy.
"""

import json
import os

reqs = json.load(open('scripts/block5_all_reqs.json', encoding='utf-8'))

def G(lesson_key, idx):
    return reqs[lesson_key]['grammar_sentences'][idx]

STORIES = {}

# =============================================================================
# UNIT 25: represionpolitica
# =============================================================================

# 25.01: represionpolitica-01
k = "represionpolitica-01"
# Grammar (8):
# 0: Un Estado represivo utiliza instituciones y fuerzas de seguridad para limitar la oposición política, aunque la intensidad de la represión puede variar.
# 1: Las detenciones y la tortura pueden utilizarse para intimidar a la población mientras el gobierno intenta mantener el control.
# 2: Los prisioneros políticos pueden permanecer detenidos durante años, incluso cuando no han cometido delitos violentos.
# 3: Durante el período, se detuvo a numerosos opositores políticos.
# 4: El estado de sitio suspendía derechos constitucionales básicos, en virtud de una supuesta emergencia nacional.
# 5: En virtud de estos decretos, las fuerzas de seguridad podían detener a cualquier persona sin necesidad de una orden judicial.
# 6: En virtud de su supuesta legalidad, el régimen presentaba estas medidas como una simple respuesta a una amenaza real.
# 7: En virtud del control que ejercía sobre el poder judicial, el régimen se aseguraba de que ningún tribunal cuestionara estas prácticas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El engranaje del Estado represivo",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante las décadas de 1970 y 1980, varios regímenes del Cono Sur y Centroamérica perfeccionaron maquinarias de coerción estatal sin precedentes. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} Patrullas policiales y grupos de tareas militares allanaban domicilios en plena noche en vehículos sin placas identificatorias, sembrando el pánico en barrios enteros."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} {G(k, 1)} El tormento físico y psicológico en centros clandestinos se convirtió en la herramienta sistemática de los servicios de inteligencia para desarticular redes disidentes."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} Jueces y magistrados cómplices rechazaban por millares los recursos de hábeas corpus presentados desesperadamente por abogados defensores y madres de familia."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Esta institucionalización del terrorismo de Estado vulneró las garantías jurídicas fundamentales y quebró el pacto democrático en toda la región."
        }
    ]
}

# 25.02: represionpolitica-02
k = "represionpolitica-02"
# Grammar (8):
# 0: La censura limita la libertad de expresión, mientras la persecución política puede dirigirse contra periodistas, estudiantes y activistas.
# 1: Los medios de comunicación fueron controlados, aunque algunos periodistas continuaron denunciando los abusos.
# 2: La persecución podía afectar también a las familias de los opositores, que vivían bajo presión y vigilancia.
# 3: La prensa fue censurada durante el período de control político.
# 4: Con el fin de controlar la información que llegaba a la población, estos regímenes impusieron censores oficiales en los principales medios.
# 5: Muchos libros fueron prohibidos y quemados, con el fin de eliminar cualquier material considerado subversivo.
# 6: Ciertos programas académicos quedaron bajo vigilancia militar, con el fin de impedir cualquier organización política dentro de las universidades.
# 7: Muchos exiliados continuaron denunciando la situación de sus países, con el fin de mantener viva la atención internacional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Censura ideológica, purga cultural y exilio forzoso",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El control del pensamiento y la asfixia del debate cultural formaron parte medular de la estrategia autoritaria. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Redacciones de periódicos, canales de televisión y emisoras radiales recibieron directivas secretas con listas de palabras, nombres y noticias terminantemente prohibidas. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} En plazas públicas y cuarteles ardieron obras de sociología, filosofía marxista, psicología freudiana e incluso cuentos infantiles que aludían a la solidaridad comunitaria."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Rectores interventores de las fuerzas armadas expulsaron a miles de profesores y estudiantes de las universidades públicas. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"Centenares de miles de intelectuales, artistas y científicos se vieron obligados a huir al extranjero. {G(k, 7)} desde México, París, Estocolmo y Madrid, construyendo un vasto movimiento de solidaridad humanitaria."
        }
    ]
}

# 25.03: represionpolitica-03
k = "represionpolitica-03"
# Grammar (8):
# 0: El gobierno negaba cualquier conocimiento de su paradero, aun cuando la familia había presenciado el propio arresto.
# 1: Las Madres de Plaza de Mayo siguieron marchando, aun cuando el régimen intentó reprimir sus protestas.
# 2: Aun cuando hizo desaparecer a algunas de sus propias fundadoras, el movimiento no dejó de exigir respuestas.
# 3: Muchísimos casos permanecen sin resolver, aun cuando la desaparición forzada ya es reconocida como un crimen de lesa humanidad.
# 4: La desaparición forzada consiste en detener a una persona y ocultar información sobre su paradero, dejando a su familia sin respuestas.
# 5: Muchas personas fueron llevadas a centros de detención clandestina, mientras sus familiares buscaban información.
# 6: Los familiares de los desaparecidos exigían saber qué había ocurrido, aunque durante años recibieron poca información oficial.
# 7: Las familias continuaron buscando información sobre sus seres queridos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La tragedia de los desaparecidos y el dolor de las familias",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 4)} Esta metodología represiva pretendió evitar el costo político de fusilamientos públicos mediante la eliminación física secreta de los prisioneros políticos. {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"En ministerios, comisarías y hospitales militares, {G(k, 0)} {G(k, 6)} El dictador Jorge Rafael Videla llegó a declarar con cinismo en 1979 que el desaparecido 'no tiene entidad, no está vivo ni muerto, es una incógnita'."
        },
        {
            "type": "narration",
            "text": f"Ante la indiferencia judicial y el terror generalizado, {G(k, 1)} {G(k, 2)} El secuestro y asesinato de fundadoras como Azucena Villaflor, Esther Ballestrino y María Ponce en diciembre de 1977 no logró doblegar la dignidad de sus rondas semanales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} {G(k, 3)} gracias a la labor incansable del Equipo Argentino de Antropología Forense (EAAF), que ha identificado restos en fosas comunes en toda América Latina."
        },
        {
            "type": "narration",
            "text": "La herida abierta de la desaparición forzada convirtió la consigna 'Aparición con vida y castigo a los culpables' en un mandato ético irrenunciable para la memoria democrática del continente."
        }
    ]
}

# 25.04: represionpolitica-04
k = "represionpolitica-04"
# Grammar (8):
# 0: Cabe destacar que, en 1980, Adolfo Pérez Esquivel recibió el Premio Nobel de la Paz por su trabajo en defensa de los derechos humanos.
# 1: Cabe destacar que buena parte de esta resistencia dependió también de redes internacionales de solidaridad.
# 2: Cabe destacar que la Vicaría de la Solidaridad fue fundada directamente por la Iglesia católica, no por un partido político.
# 3: Cabe destacar que estos movimientos guerrilleros fueron, en general, minoritarios dentro del conjunto de la resistencia.
# 4: Frente a la represión surgieron distintas formas de resistencia, desde protestas públicas hasta organizaciones de derechos humanos.
# 5: Los familiares de las víctimas presentaron denuncias, mientras grupos civiles documentaban los abusos.
# 6: La resistencia podía ser peligrosa, aunque permitió mantener visibles las demandas de justicia.
# 7: Frente a la represión, varias organizaciones comenzaron a documentar los abusos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Redes de resistencia, derechos humanos y solidaridad civil",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 7)} A pesar de los riesgos extremos de detención y muerte, ciudadanos de diversas convicciones éticas desafiaron la censura para salvar vidas. {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"En Chile, bajo la égida del cardenal Raúl Silva Henríquez, {G(k, 2)} La Vicaría prestó asistencia jurídica a más de 250.000 personas y compiló un archivo documental minucioso que desnudó los crímenes de la DINA y la CNI ante los tribunales internacionales."
        },
        {
            "type": "narration",
            "text": f"En Argentina, el Servicio Paz y Justicia (SERPAJ) promovió la no violencia activa frente a la dictadura militar. {G(k, 0)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Organizaciones como Amnistía Internacional, sindicatos europeos y comités de exiliados presionaron a gobiernos democráticos para condicionar créditos y ayuda externa a los regímenes militares."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} La verdadera muralla que desgastó la legitimidad de las dictaduras fue la movilización moral no violenta de la sociedad civil y el movimiento ecuménico de derechos humanos."
        }
    ]
}

# 25.05: represionpolitica-05
k = "represionpolitica-05"
# Grammar (8):
# 0: A día de hoy, tras la anulación de estas leyes de amnistía, cientos de nuevos juicios se han reabierto en Argentina.
# 1: En Chile, la ley de amnistía de 1978 sigue generando, a día de hoy, un intenso debate legal y político.
# 2: A día de hoy, la tensión entre memoria, justicia y reconciliación sigue sin resolverse completamente.
# 3: A día de hoy, ese antiguo centro de detención es un sitio de memoria abierto al público.
# 4: Después de las dictaduras, la memoria histórica se convirtió en un tema central para muchas sociedades, aunque existían diferentes formas de recordar el pasado.
# 5: Las víctimas y sus familias reclamaron justicia, mientras los gobiernos debatían cómo investigar los crímenes.
# 6: La impunidad continuó siendo un problema cuando los responsables de abusos no fueron juzgados, pero las organizaciones de derechos humanos siguieron trabajando.
# 7: A lo largo de la transición democrática, continuaron los debates sobre memoria y justicia.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Memoria histórica, justicia transicional y verdad",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 7)} Durante los años de transición democrática, las sociedades sudamericanas enfrentaron el dilema de castigar a los culpables o ceder al chantaje militar de la impunidad. {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"Leyes de impunidad como las de Punto Final y Obediencia Debida en Argentina, o la ley de caducidad en Uruguay, buscaron clausurar los procesos penales. {G(k, 6)} {G(k, 0)} con más de mil represores condenados por delitos de lesa humanidad."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Aunque los jueces chilenos aplicaron la doctrina de que los secuestros permanentes no prescriben, el debate sobre las responsabilidades civiles de la dictadura continúa encendido en la sociedad."
        },
        {
            "type": "narration",
            "text": f"En Buenos Aires, la antigua Escuela de Mecánica de la Armada (ESMA) fue recuperada como Espacio Memoria y declarada Patrimonio de la Humanidad por la UNESCO. {G(k, 3)} donde miles de jóvenes conocen la historia reciente."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Preservar la memoria colectiva y defender los derechos humanos se consolidó como la única garantía para que las páginas más oscuras del autoritarismo no vuelvan a repetirse jamás."
        }
    ]
}

# =============================================================================
# UNIT 26: centroamerica
# =============================================================================

# 26.01: centroamerica-01
k = "centroamerica-01"
# Grammar (8):
# 0: La estructura agraria concentró la tierra en pocas familias, mientras la mayoría campesina vivía en la pobreza.
# 1: Los regímenes autoritarios gobernaron varios países de la región mediante el control militar y el fraude electoral.
# 2: Las tensiones sociales aumentaron cuando las vías pacíficas de cambio quedaron bloqueadas.
# 3: La región centroamericana presentaba una de las estructuras agrarias más desiguales de todo el continente.
# 4: Unas pocas familias oligárquicas, apodadas las "catorce familias" en El Salvador, controlaban la mayor parte de las tierras fértiles.
# 5: La producción de café, banano y algodón generaba enormes fortunas para una minoría diminuta.
# 6: El analfabetismo, la desnutrición infantil y la servidumbre laboral constituían la realidad cotidiana de la inmensa mayoría de la población rural.
# 7: La concentración de la tierra y la falta de libertades políticas provocaron fuertes tensiones sociales.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Las raíces de la crisis centroamericana: oligarquía y latifundio",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Hacia la década de 1970, el istmo centroamericano constituía una de las zonas más volátiles y socialmente injustas del planeta. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} Estas élites agroexportadoras estaban estrechamente aliadas con consorcios estadounidenses y monopolizaban los ingenios, puertos y bancos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Los jornaleros e indígenas mayas en Guatemala, campesinos sin tierra en El Salvador y peones en Nicaragua vivían atados a jornales miserables durante las temporadas de cosecha."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 7)} Dinastías como los Somoza en Nicaragua y juntas militares en El Salvador y Guatemala recurrieron al fraude electoral sistemático y al asesinato de líderes opositores."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} El cierre de las vías democráticas y la miseria extrema empujaron a sectores campesinos, estudiantiles y religiosos hacia la organización insurreccional armada."
        }
    ]
}

# 26.02: centroamerica-02
k = "centroamerica-02"
# Grammar (8):
# 0: El FSLN derrocó a la dinastía de los Somoza en julio de 1979.
# 1: El gobierno sandinista impulsó una campaña masiva de alfabetización y una reforma agraria.
# 2: Estados Unidos financió a los grupos armados conocidos como los "contras" para combatir al nuevo gobierno.
# 3: El 19 de julio de 1979, las columnas del Frente Sandinista de Liberación Nacional (FSLN) entraron victoriosas en Managua.
# 4: La caída de Anastasio Somoza Debayle puso fin a más de cuatro décadas de tiranía familiar en Nicaragua.
# 5: La Cruzada Nacional de Alfabetización de 1980 redujo el analfabetismo del cincuenta al doce por ciento en pocos meses.
# 6: La administración de Ronald Reagan impuso un embargo comercial y financió clandestinamente a la contrarrevolución.
# 7: La guerra civil afectó profundamente la economía y la sociedad nicaragüense.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Revolución Sandinista en Nicaragua (1979-1990)",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 4)} La insurrección popular generalizada y la unión de empresarios, obreros y la Iglesia pusieron fin al régimen somocista."
        },
        {
            "type": "narration",
            "text": f"La Junta de Gobierno de Reconstrucción Nacional, integrada por figuras como Daniel Ortega y el escritor Sergio Ramírez, emprendió ambiciosas reformas sociales. {G(k, 1)} {G(k, 5)} Miles de jóvenes brigadistas enseñaron a leer en chozas campesinas y valles aislados."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, el gobierno de Washington vio en Managua una peligrosa cabeza de playa soviética en Centroamérica. {G(k, 6)} {G(k, 2)} El escándalo Irán-Contra reveló que la Casa Blanca vendía armas secretas a Irán para financiar a los rebeldes contras."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} El minado de puertos, los atentados contra cooperativas campesinas y el servicio militar obligatorio desgastaron al país, cobrándose más de 30.000 vidas."
        },
        {
            "type": "narration",
            "text": "En febrero de 1990, en unas elecciones supervisadas internacionalmente, la coalición opositora UNO liderada por Violeta Barrios de Chamorro triunfó en las urnas, realizándose la primera transferencia pacífica del poder en la historia nicaragüense."
        }
    ]
}

# 26.03: centroamerica-03
k = "centroamerica-03"
# Grammar (8):
# 0: La guerra civil salvadoreña enfrentó al ejército gubernamental con la guerrilla del FMLN durante más de una década.
# 1: El asesinato de monseñor Óscar Arnulfo Romero en 1980 conmocionó al país y a la comunidad internacional.
# 2: Los Acuerdos de Paz de Chapultepec de 1992 pusieron fin al conflicto armado mediante reformas políticas.
# 3: El 24 de marzo de 1980, un francotirador de los escuadrones de la muerte asesinó a monseñor Romero mientras celebraba misa.
# 4: El conflicto armado salvadoreño se prolongó durante doce años con un saldo de más de setenta y cinco mil muertos.
# 5: La masacre de El Mozote en diciembre de 1981 demostró la brutalidad extrema de los batallones de contrainsurgencia.
# 6: Los Acuerdos de Paz de 1992 transformaron al FMLN en un partido político legal y disolvieron los cuerpos de seguridad represivos.
# 7: El conflicto salvadoreño provocó miles de víctimas y obligó a muchas personas a desplazarse.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La guerra civil en El Salvador y la voz de monseñor Romero",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 4)} {G(k, 7)} El Frente Farabundo Martí para la Liberación Nacional (FMLN) coordinó a cinco organizaciones guerrilleras que controlaron amplias zonas rurales en Morazán y Chalatenango."
        },
        {
            "type": "narration",
            "text": f"En medio del terror de los escuadrones de la muerte dirigidos por Roberto d'Aubuisson, el arzobispo de San Salvador se convirtió en 'la voz de los sin voz'. {G(k, 1)} El 23 de marzo de 1980, monseñor Romero ordenó en su homilía dominical: 'En nombre de Dios, ¡cese la represión!'. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} El Batallón Atlacatl, entrenado por asesores estadounidenses, ejecutó a más de novecientos campesinos desarmados, en su mayoría niños y mujeres, en la mayor matanza civil de la historia contemporánea de la región."
        },
        {
            "type": "narration",
            "text": f"Tras la gran ofensiva guerrillera 'Hasta el Tope' de noviembre de 1989 y la mediación de las Naciones Unidas, ambas partes reconocieron que la victoria militar era imposible. {G(k, 2)} en el Castillo de Chapultepec en México."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Se creó la Policía Nacional Civil y se abrió paso a la democratización institucional, cerrando una década de inmenso sufrimiento popular."
        }
    ]
}

# 26.04: centroamerica-04
k = "centroamerica-04"
# Grammar (8):
# 0: El conflicto armado interno en Guatemala afectó de manera desproporcionada a las comunidades mayas.
# 1: La política de "tierra arrasada" implementada por el ejército destruyó cientos de aldeas indígenas.
# 2: Rigoberta Menchú recibió el Premio Nobel de la Paz en 1992 por su denuncia de los abusos contra los pueblos indígenas.
# 3: El informe "Memoria del Silencio" de la Comisión para el Esclarecimiento Histórico documentó más de doscientos mil muertos y desaparecidos.
# 4: La dictadura del general Efraín Ríos Montt (1982-1983) ejecutó actos de genocidio sistemático contra el pueblo maya ixil.
# 5: Cientos de miles de campesinos indígenas huyeron a través de la frontera hacia campos de refugiados en el sur de México.
# 6: Los Acuerdos de Paz de 1996 reconocieron la identidad y los derechos de los pueblos indígenas como fundamento del Estado guatemalteco.
# 7: La violencia en Guatemala tuvo un impacto profundo en las comunidades rurales e indígenas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Guatemala: el conflicto armado, el genocidio maya y la búsqueda de la paz",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Entre 1960 y 1996, Guatemala vivió el conflicto armado más prolongado y devastador del hemisferio occidental. {G(k, 0)} {G(k, 7)} Guerrillas como el EGP y la ORPA operaron en el altiplano frente a un ejército implacable."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 1)} Bajo la doctrina de 'quitarle el agua al pez', tropas gubernamentales arrasaron más de 400 aldeas mayas, ejecutando masacres sistemáticas como las de Plan de Sánchez y Dos Erres."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} en Chiapas y Quintana Roo. Desde el exilio, líderes comunitarias alzaron la voz ante los foros internacionales. {G(k, 2)} dando visibilidad global a la resistencia maya."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} La comisión respaldada por la ONU concluyó que el 83% de las víctimas pertenecían a pueblos mayas y que el 93% de las atrocidades fueron cometidas por el Estado."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La firma de la 'Paz Firme y Duradera' en diciembre de 1996 consagró el carácter multiétnico, pluricultural y multilingüe de la nación guatemalteca."
        }
    ]
}

# 26.05: centroamerica-05
k = "centroamerica-05"
# Grammar (8):
# 0: Los Acuerdos de Paz de Esquipulas impulsaron una solución negociada para los conflictos de la región.
# 1: El presidente costarricense Óscar Arias Sánchez recibió el Premio Nobel de la Paz por su liderazgo diplomático.
# 2: Las transiciones a la paz abrieron procesos de desmilitarización y democratización en Centroamérica.
# 3: El Grupo de Contadora, integrado por México, Colombia, Venezuela y Panamá, sentó las bases de la diplomacia regional autónoma.
# 4: El plan de paz de Esquipulas II de 1987 demostró que los presidentes centroamericanos podían resolver sus diferencias sin interferencia extranjera.
# 5: La desmovilización de las fuerzas guerrilleras permitió su integración a la vida política constitucional de sus respectivos países.
# 6: Los desafíos pendientes incluyen la pobreza estructural, la violencia criminal de las pandillas y la debilidad de las instituciones democráticas.
# 7: La reconstrucción económica y social continúa siendo un desafío para los países centroamericanos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El proceso de paz de Esquipulas y los desafíos del posconflicto",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Frente al peligro inminente de que las guerras centroamericanas derivaran en una invasión militar regional de Estados Unidos, los líderes del continente tomaron la iniciativa diplomática. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Los cinco mandatarios de Guatemala, El Salvador, Honduras, Nicaragua y Costa Rica firmaron el histórico acuerdo de cese al fuego y democratización. {G(k, 1)} en 1987 por su decisivo liderazgo pacificador."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} Miles de excombatientes entregaron sus fusiles ante observadores de la ONU (ONUSAL y ONUVEN), transformando las armas en papeletas de voto."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, el fin de los tiroteos no resolvió automáticamente las causas profundas de la marginación. {G(k, 6)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": "La proliferación de pandillas juveniles (maras), el narcotráfico y la emigración masiva hacia el norte revelan que la paz verdadera exige no solo el silencio de las armas, sino una auténtica justicia social y oportunidades para la juventud."
        }
    ]
}

# =============================================================================
# UNIT 27: conosur
# =============================================================================

# 27.01: conosur-01
k = "conosur-01"
# Grammar (8):
# 0: El Cono Sur compartía una historia de relativa estabilidad democrática antes de la ola de golpes militares.
# 1: Argentina, Chile y Uruguay contaban con altos niveles de urbanización y una clase media extensa.
# 2: Las crisis políticas de los años sesenta y setenta transformaron profundamente a estas sociedades.
# 3: A mediados del siglo veinte, el Cono Sur se distinguía del resto de América Latina por sus elevados índices de desarrollo humano.
# 4: Chile y Uruguay se enorgullecían de tradiciones institucionales ininterrumpidas durante décadas de gobiernos civiles.
# 5: La polarización política y las crisis económicas erosionaron rápidamente los consensos democráticos tradicionales.
# 6: La caída de estas democracias representó una ruptura traumática para sociedades que se consideraban inmunes al autoritarismo militar.
# 7: La región del Cono Sur experimentó profundas transformaciones sociales y políticas en este periodo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La ilusión de la excepcionalidad democrática en el Cono Sur",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 1)} Tasas de alfabetización superiores al 90%, sistemas de salud universales y sindicatos organizados asemejaban a estas naciones al sur de Europa."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Uruguay era aclamado internacionalmente como 'la Suiza de América' por su Estado de bienestar batllista, mientras Chile presumía de un Congreso Nacional centenario y fuerzas armadas profesionalizadas ajenas a la deliberación política."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, el estancamiento económico de la posguerra y el impacto de la Revolución cubana desgastaron la convivencia cívica. {G(k, 5)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Sectores oligárquicos y mandos castrenses adoptaron la Doctrina de la Seguridad Nacional, convencidos de que las libertades parlamentarias abrían las puertas al comunismo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} El derrumbe institucional de la década de 1970 demostró que ninguna sociedad estaba a salvo del horror dictatorial cuando se fractura la tolerancia política."
        }
    ]
}

# 27.02: conosur-02
k = "conosur-02"
# Grammar (8):
# 0: El golpe militar de 1973 en Uruguay puso fin a una de las democracias más antiguas del continente.
# 1: El presidente Juan María Bordaberry disolvió el Parlamento con el respaldo de las fuerzas armadas.
# 2: La dictadura uruguaya encarceló a miles de ciudadanos, registrando la tasa de presos políticos más alta de la región.
# 3: El 27 de junio de 1973, el presidente civil Bordaberry encabezó un autogolpe militar clausurando las cámaras legislativas.
# 4: La huelga general de quince días convocada por la central obrera CNT constituyó un acto ejemplar de resistencia civil.
# 5: El penal de Libertad se convirtió en el símbolo siniestro de un régimen que convirtió a Uruguay en una prisión a cielo abierto.
# 6: El plebiscito constitucional de 1980 propinó una derrota histórica al proyecto autoritario de las fuerzas armadas.
# 7: La dictadura uruguaya afectó profundamente la vida política y social del país.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La dictadura cívico-militar en Uruguay (1973-1985)",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 3)} {G(k, 1)} El régimen militar impuso una férrea censura de prensa y proscribió a los partidos de izquierda y sindicatos."
        },
        {
            "type": "narration",
            "text": f"La respuesta obrera fue inmediata y contundente. {G(k, 4)} Fábricas, facultades y bancos fueron ocupados pacíficamente durante dos semanas antes de ser desalojados por tanques militares."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Uno de cada quinientos habitantes pasó por calabozos y centros de tortura. {G(k, 5)} donde líderes de los Tupamaros como Raúl Sendic y Pepe Mujica permanecieron recluidos durante más de una década en condiciones infrahumanas como 'rehenes' del régimen."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} Sin embargo, la vocación democrática del pueblo oriental permaneció intacta. En noviembre de 1980, en un referéndum cuidadosamente controlado por los militares, {G(k, 6)} con un rotundo 57% de votos por el NO."
        },
        {
            "type": "narration",
            "text": "Esta histórica bofetada cívica obligó a los generales al diálogo del Pacto del Club Naval en 1984 y abrió el retorno a la democracia con la asunción presidencial de Julio María Sanguinetti en marzo de 1985."
        }
    ]
}

# 27.03: conosur-03
k = "conosur-03"
# Grammar (8):
# 0: La dictadura de Alfredo Stroessner en Paraguay se prolongó durante treinta y cinco años (1954-1989).
# 1: El régimen combinó represión selectiva, control del Partido Colorado y corrupción generalizada.
# 2: La oposición fue perseguida sistemáticamente mientras el régimen mantenía una fachada de elecciones periódicas.
# 3: El "stronismo" constituyó la dictadura personalista más prolongada de toda la historia sudamericana moderna.
# 4: Stroessner gobernó apoyado en la trilogía corporativa integrada por las Fuerzas Armadas, el Partido Colorado y el aparato estatal.
# 5: La construcción de la gigantesca represa de Itaipú generó un auge económico que enriqueció a la camarilla gobernante.
# 6: El descubrimiento de los "Archivos del Terror" en 1992 desnudó la participación central de Asunción en el Plan Cóndor.
# 7: El régimen autoritario paraguayo dejó una profunda huella en las instituciones del país.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El 'Stronismo' en Paraguay: treinta y cinco años de tiranía (1954-1989)",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En mayo de 1954, el general Alfredo Stroessner tomó el poder mediante un golpe de Estado en Asunción. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 1)} La afiliación al Partido Colorado era obligatoria para maestros, militares, policías y cualquier empleado público, mientras el contrabando y el narcotráfico eran tolerados como prebendas para la lealtad de los oficiales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} El estado de sitio se renovaba cada noventa días en Asunción, mientras en el Departamento de Investigaciones de la Policía Nacional los opositores eran sometidos a la pileta de tormentos."
        },
        {
            "type": "narration",
            "text": f"En la década de 1970, {G(k, 5)} junto a Brasil en el río Paraná, inyectando millones de dólares que alimentaron una burbuja de especulación inmobiliaria. {G(k, 6)} en una comisaría de Lambaré."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} Stroessner fue derrocado en febrero de 1989 por su propio consuegro, el general Andrés Rodríguez, iniciando una compleja transición hacia la democracia."
        }
    ]
}

# 27.04: conosur-04
k = "conosur-04"
# Grammar (8):
# 0: La dictadura de Hugo Banzer gobernó Bolivia entre 1971 y 1978 tras derrocar a Juan José Torres.
# 1: El régimen reprimió con dureza al movimiento minero y a las organizaciones campesinas indígenas.
# 2: Las huelgas mineras y la resistencia popular forzaron la apertura política hacia finales de la década.
# 3: El coronel Hugo Banzer Suárez encabezó un sangriento golpe militar en agosto de 1971 apoyado por sectores conservadores.
# 4: La masacre de Tolata y Epizana en 1974 evidenció la ruptura del pacto militar-campesino tradicional en el valle de Cochabamba.
# 5: La histórica huelga de hambre iniciada por cuatro mujeres mineras en 1977 desató una ola de desobediencia civil imparable.
# 6: Bolivia atravesó una década de profunda inestabilidad política antes de consolidar su transición democrática en 1982.
# 7: La resistencia obrera y campesina jugó un papel clave en el desgaste del régimen militar boliviano.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Bolivia: dictadura militar, resistencia minera y el coraje de las cuatro mujeres",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} Banzer desmanteló la Asamblea Popular revolucionaria y proscribió a la Central Obrera Boliviana (COB). {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} cuando el ejército acribilló a decenas de quechuas que bloqueaban carreteras contra la devaluación de la moneda, alienando el respaldo rural al régimen."
        },
        {
            "type": "narration",
            "text": f"En diciembre de 1977, un hecho conmovedor cambió el curso de la historia. {G(k, 5)} encabezadas por Domitila Barrios de Chungara en el palacio arzobispal de La Paz. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"En pocas semanas, más de 1.300 sacerdotes, estudiantes y obreros se sumaron al ayuno en todo el país. {G(k, 2)} obligando a Banzer a decretar una amnistía general irrestricta y convocar a elecciones."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} que culminó en octubre de 1982 con la asunción constitucional de Hernán Siles Zuazo al frente de la UDP."
        }
    ]
}

# 27.05: conosur-05
k = "conosur-05"
# Grammar (8):
# 0: Las transiciones democráticas en el Cono Sur enfrentaron el desafío de subordinar a los militares al poder civil.
# 1: La recuperación de las libertades públicas permitió el resurgimiento de la vida partidaria y sindical.
# 2: Las comisiones de verdad desempeñaron un papel fundamental en la documentación de los crímenes dictatoriales.
# 3: El Cono Sur completó la recuperación democrática entre 1982 y 1990 en un contexto de grave crisis económica.
# 4: Los informes "Nunca Más" en Argentina y "Rettig" en Chile transformaron la conciencia moral de las nuevas democracias.
# 5: Las presiones de las cúpulas militares forzaron negociaciones y pactos que condicionaron los primeros años constitucionales.
# 6: La subordinación efectiva de las fuerzas armadas a las autoridades electas constituyó el logro institucional más trascendental.
# 7: La reconstrucción de las instituciones democráticas fue un proceso complejo en toda la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El retorno a la democracia y el imperativo del 'Nunca Más'",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 7)} Gobiernos constitucionales asumieron en medio de hiperinflaciones galopantes y deudas externas asfixiantes."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Millones de personas salieron a las calles a votar, debatir en asambleas universitarias y refundar sindicatos clausurados durante años por la bota militar."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 4)} El testimonio de miles de sobrevivientes ante la CONADEP en Argentina y la Comisión Rettig en Chile reveló al mundo la magnitud escalofriante del terrorismo de Estado."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Sublevaciones militares 'carapintadas' en Argentina y amenazas de 'acuartelamiento' en Chile exigieron una enorme firmeza cívica por parte de los presidentes Raúl Alfonsín y Patricio Aylwin."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La consolidación de la supremacía de la ley civil y el compromiso irreductible con los derechos humanos forjaron el patrimonio democrático más valioso de la región contemporánea."
        }
    ]
}

# =============================================================================
# UNIT 28: crisisdeuda
# =============================================================================

# 28.01: crisisdeuda-01
k = "crisisdeuda-01"
# Grammar (8):
# 0: Los petrodólares generaron una gran liquidez internacional durante la década de 1970.
# 1: Los bancos extranjeros ofrecieron créditos abundantes a bajas tasas de interés a los gobiernos latinoamericanos.
# 2: La deuda externa de la región se multiplicó rápidamente durante este período de endeudamiento fácil.
# 3: Tras los shocks petroleros de 1973 y 1979, los países de la OPEP depositaron miles de millones de dólares en la banca internacional.
# 4: Los bancos comerciales de Wall Street y Londres inundaron a América Latina de préstamos a tasas de interés variables.
# 5: Gran parte del dinero prestado se destinó a compras de armamento militar, obras faraónicas y especulación financiera.
# 6: La ilusión del crédito barato y abundante ocultó la tremenda trampa financiera que se estaba construyendo.
# 7: El endeudamiento fácil aumentó la vulnerabilidad financiera de los países de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La fiesta de los petrodólares y la trampa del endeudamiento fácil",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 3)} Las entidades financieras globales se encontraron saturadas de capitales excedentes que debían colocar con urgencia en el mercado mundial."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 4)} Agentes de crédito visitaban los ministerios de hacienda en Buenos Aires, Brasilia, Santiago, México y Lima, ofreciendo créditos masivos con escasas exigencias de viabilidad técnica."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 7)} Entre 1970 y 1982, la deuda externa total de América Latina se disparó de 27.000 millones a más de 330.000 millones de dólares."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} En lugar de financiar industrialización reproductiva, miles de millones se esfumaron en importaciones suntuarias y en la fuga masiva de capitales privados hacia paraísos fiscales en Suiza y Miami."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Cuando la Reserva Federal de Estados Unidos decidiera alterar abruptamente las reglas del juego financiero global, el castillo de naipes se derrumbaría con violencia inusitada."
        }
    ]
}

# 28.02: crisisdeuda-02
k = "crisisdeuda-02"
# Grammar (8):
# 0: La Reserva Federal de Estados Unidos aumentó drásticamente las tasas de interés en 1979 bajo la presidencia de Paul Volcker.
# 1: El aumento de las tasas encareció de manera exorbitante el servicio de la deuda externa para los países deudores.
# 2: Los precios internacionales de las materias primas cayeron al mismo tiempo, reduciendo los ingresos de exportación.
# 3: El "shock Volcker" de 1979 elevó las tasas de interés en Estados Unidos hasta niveles cercanos al veinte por ciento anual.
# 4: El costo de refinanciar la deuda externa latinoamericana se multiplicó de la noche a la mañana.
# 5: La combinación de tasas de interés astronómicas y precios de exportación deprimidos estranguló las finanzas públicas de toda la región.
# 6: Esta doble tenaza financiera convirtió una deuda manejable en una carga absolutamente impagable para las economías de la región.
# 7: La subida de los tipos de interés provocó graves problemas de pago a los gobiernos deudores.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El 'Shock Volcker' y el estrangulamiento de los deudores",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En octubre de 1979, decidido a extirpar la inflación en Estados Unidos cueste lo que cueste, {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"Dado que la inmensa mayoría de los contratos de préstamo suscritos por América Latina estaban pactados a tasas de interés flotantes ligadas a la tasa Prime o Libor, {G(k, 4)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Para agravar la situación, la recesión económica en los países industrializados provocó un desplome en la demanda de cobre, café, petróleo y cereales. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 7)} Las reservas de divisas en los bancos centrales se agotaron a un ritmo vertiginoso para atender el pago de intereses vencidos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} En agosto de 1982, la mecha financiera llegó a su fin y desató la mayor crisis de pagos de la historia moderna de América Latina."
        }
    ]
}

# 28.03: crisisdeuda-03
k = "crisisdeuda-03"
# Grammar (8):
# 0: México declaró la moratoria del pago de su deuda externa en agosto de 1982, desatando la crisis continental.
# 1: Los bancos internacionales suspendieron inmediatamente el crédito a todos los países de la región.
# 2: La crisis se extendió con rapidez a casi todas las economías latinoamericanas que compartían un alto nivel de endeudamiento.
# 3: El 12 de agosto de 1982, el secretario de Hacienda mexicano Jesús Silva-Herzog comunicó al FMI que México carecía de dólares para pagar.
# 4: El anuncio mexicano desató un efecto dominó que cortó de inmediato el financiamiento externo para toda América Latina.
# 5: Brasil, Argentina, Venezuela, Chile y Perú se vieron obligados sucesivamente a suspender o renegociar sus compromisos de deuda.
# 6: Los bancos centrales sufrieron una hemorragia imparable de reservas que forzó masivas devaluaciones de sus monedas nacionales.
# 7: La declaración de moratoria provocó una crisis de liquidez en el sistema financiero internacional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Agosto de 1982: el crac mexicano y el efecto dominó",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} El presidente José López Portillo, quien pocos meses antes prometiera 'defender el peso como un perro', decretó la nacionalización de la banca privada."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 1)} {G(k, 7)} De pronto, los bancos extranjeros trataron a toda la región como un territorio insolvente de alto riesgo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} El producto interno bruto cayó en picada mientras las empresas privadas con deudas en dólares quebraban en masa."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} En Argentina y Brasil las monedas perdieron su valor en cuestión de semanas, empujando los precios al alza y pulverizando los salarios obreros."
        },
        {
            "type": "narration",
            "text": "La crisis de la deuda inauguró una larga década de parálisis productiva, austeridad draconiana y sufrimiento social en todo el continente."
        }
    ]
}

# 28.04: crisisdeuda-04
k = "crisisdeuda-04"
# Grammar (8):
# 0: El Fondo Monetario Internacional impuso programas de ajuste estructural a cambio de préstamos de rescate.
# 1: Las políticas de austeridad redujeron el gasto público en salud, educación e infraestructura.
# 2: Las devaluaciones continuas provocaron hiperinflaciones descontroladas en varios países de la región.
# 3: El FMI y el Banco Mundial actuaron como auditores estrictos de la economía latinoamericana en beneficio de los bancos acreedores.
# 4: Los programas de ajuste exigieron drásticos recortes presupuestarios, privatizaciones y congelamiento de salarios reales.
# 5: Países como Bolivia, Argentina, Perú y Brasil experimentaron episodios de hiperinflación que devoraron los ahorros populares.
# 6: La fuga de capitales y el pago del servicio de la deuda convirtieron a América Latina en exportadora neta de capitales.
# 7: Los programas de ajuste provocaron fuertes protestas sociales en varias capitales.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El FMI, el ajuste estructural y el flagelo de la hiperinflación",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Sin acceso a préstamos voluntarios en los mercados privados, los gobiernos latinoamericanos no tuvieron más opción que acudir a Washington. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 1)} Escuelas públicas quedaron sin materiales, hospitales sin medicinas y los subsidios al transporte y alimentos básicos fueron eliminados de cuajo. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} En Bolivia en 1985 la inflación anual superó el 20.000%, y en Perú en 1989 rebasó el 7.000%, obligando a la gente a hacer compras con fajos de billetes que perdían valor cada hora."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Entre 1982 y 1990, la región transfirió al exterior más de 200.000 millones de dólares en pagos netos a sus acreedores extranjeros."
        },
        {
            "type": "narration",
            "text": "La paradoja era trágica e inmoral: los países pobres de América Latina estaban descapitalizándose para salvar de la quiebra a los grandes bancos de Wall Street y Londres."
        }
    ]
}

# 28.05: crisisdeuda-05
k = "crisisdeuda-05"
# Grammar (8):
# 0: La CEPAL bautizó la década de 1980 como la "década perdida" debido al retroceso económico y social de la región.
# 1: El ingreso por habitante retrocedió a niveles de principios de la década de 1970 en muchos países.
# 2: La crisis forzó el abandono definitivo del modelo de industrialización por sustitución de importaciones.
# 3: El ingreso por habitante de América Latina cayó más del ocho por ciento a lo largo de los años ochenta.
# 4: La inversión productiva y el gasto social sufrieron un colapso que hipotecó el bienestar de toda una generación.
# 5: La crisis de la deuda clausuró definitivamente medio siglo de desarrollo basado en el Estado de bienestar y la ISI.
# 6: El Plan Brady de 1989 ofreció finalmente una reestructuración parcial de la deuda mediante títulos respaldados por el Tesoro estadounidense.
# 7: La crisis de la deuda aceleró transformaciones profundas en el modelo económico de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La 'Década Perdida' y el agotamiento del modelo desarrollista",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 3)} {G(k, 1)} Diez años de esfuerzos productivos quedaron completamente borrados por el colapso financiero."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} El desempleo, el empleo informal y la pobreza urbana se dispararon hasta alcanzar a casi la mitad de la población continental. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} Los Estados ya no contaban con recursos fiscales para subsidiar fábricas nacionales, financiar empresas públicas deficitarias o sostener tipos de cambio preferenciales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} diseñado por el secretario del Tesoro Nicholas Brady, permitió canjear viejos préstamos por 'Bonos Brady' a largo plazo, aliviando la asfixia inmediata."
        },
        {
            "type": "narration",
            "text": "La 'década perdida' dejó a una América Latina empobrecida y exhausta, dejándola indefensa ante la ola privatizadora y desreguladora que traería el Consenso de Washington en la década de 1990."
        }
    ]
}

# =============================================================================
# UNIT 29: neoliberalismo
# =============================================================================

# 29.01: neoliberalismo-01
k = "neoliberalismo-01"
# Grammar (8):
# 0: El Consenso de Washington sintetizó diez recomendaciones de política económica formuladas por organismos financieros internacionales.
# 1: Las políticas promovían la disciplina fiscal, la apertura comercial y la desregulación de los mercados.
# 2: Las reformas buscaban reducir el déficit público y controlar la inflación crónica.
# 3: El economista británico John Williamson formuló en 1989 el célebre decálogo conocido como el "Consenso de Washington".
# 4: Este conjunto de recetas resumía las recomendaciones compartidas por el FMI, el Banco Mundial y el Departamento del Tesoro de Estados Unidos.
# 5: Las reformas postulaban que el libre mercado y la iniciativa privada debían sustituir al Estado como motor del desarrollo.
# 6: La apertura irrestricta a las importaciones y a las inversiones extranjeras se presentó como la única vía para modernizar las economías latinoamericanas.
# 7: El Consenso de Washington marcó un cambio fundamental en las políticas económicas de América Latina.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Consenso de Washington y el nuevo credo del libre mercado",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 2)} Se exigió una rigurosa austeridad fiscal, la eliminación de aranceles de protección, la privatización de empresas públicas y la total liberalización financiera."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 6)} Bajo la premisa del TINA ('There Is No Alternative' / No hay alternativa), los tecnócratas aseguraban que cualquier retraso en las reformas condenaría al país al atraso."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} Presidentes de diversas tendencias políticas —desde Carlos Menem en Argentina hasta Alberto Fujimori en Perú y Carlos Salinas de Gortari en México— aplicaron con rigor este paquete de reformas."
        },
        {
            "type": "narration",
            "text": "El giro neoliberal desmanteló el modelo de desarrollo nacionalista edificado durante medio siglo, abriendo una era de transformaciones radicales y hondas fracturas sociales."
        }
    ]
}

# 29.02: neoliberalismo-02
k = "neoliberalismo-02"
# Grammar (8):
# 0: Los gobiernos privatizaron cientos de empresas estatales de telecomunicaciones, energía y transporte.
# 1: La venta de activos públicos permitió recaudar ingresos extraordinarios para reducir la deuda pública.
# 2: Las privatizaciones generaron controversia por el despido masivo de trabajadores y el aumento de las tarifas de los servicios.
# 3: El programa de privatizaciones transfirió activos públicos por más de cien mil millones de dólares a consorcios privados y transnacionales.
# 4: Empresas emblemáticas como YPF en Argentina, Telmex en México, Telebras en Brasil y Entel en varios países pasaron a manos privadas.
# 5: La desregulación financiera atrajo una marea de capitales especulativos de corto plazo que alimentaron burbujas financieras.
# 6: Miles de trabajadores calificados fueron despedidos mientras las tarifas de agua, luz y gas se dolarizaban y aumentaban bruscamente.
# 7: La venta de empresas públicas transformó profundamente el papel del Estado en la economía.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La ola privatizadora y el desmantelamiento de los bienes públicos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante la década de 1990, América Latina protagonizó la mayor transferencia de propiedad pública a manos privadas de la historia moderna. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Líneas aéreas de bandera como Aerolíneas Argentinas y redes ferroviarias centenarias fueron vendidas a corporaciones extranjeras a precios de liquidación. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 7)} {G(k, 2)} El argumento oficial de mayor eficiencia técnica chocó con la realidad de tarifas dolarizadas que golpearon con crudeza los presupuestos familiares."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Ciudades del interior que dependían del ferrocarril o de refinerías estatales quedaron convertidas de la noche a la mañana en pueblos fantasma desolados por el desempleo."
        },
        {
            "type": "narration",
            "text": "La venta del patrimonio público redujo transitoriamente los déficits fiscales pero despojó a los Estados de instrumentos estratégicos para conducir el desarrollo nacional."
        }
    ]
}

# 29.03: neoliberalismo-03
k = "neoliberalismo-03"
# Grammar (8):
# 0: La apertura comercial expuso a la industria nacional a la competencia de productos importados.
# 1: Muchas fábricas locales no pudieron competir y cerraron, aumentando el desempleo industrial.
# 2: La reducción de aranceles benefició a los consumidores con productos más baratos y variados.
# 3: La rebaja unilateral de aranceles inundó los mercados locales de manufacturas baratas de Asia y Norteamérica.
# 4: Sectores industriales enteros como el textil, el calzado y la metalmecánica sufrieron una destrucción masiva.
# 5: El desempleo formal se disparó mientras proliferaba la economía informal de venta ambulante y trabajo precarizado.
# 6: Se amplió el papel del sector privado mientras el Estado se retiraba de ciertas funciones.
# 7: Se debatió mucho sobre los límites de estas reformas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Apertura comercial, desindustrialización y precarización laboral",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"La eliminación fulminante de los aranceles de importación provocó un choque demoledor sobre la estructura productiva interna. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Los centros comerciales de las capitales se llenaron de electrodomésticos, prendas de vestir y alimentos importados a precios convenientes."
        },
        {
            "type": "narration",
            "text": f"No obstante, el costo productivo fue colosal. {G(k, 4)} {G(k, 1)} Miles de pequeñas y medianas empresas familiares que no contaban con subsidios ni crédito blando quebraron sin remedio."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 6)} La flexibilización laboral eliminó las indemnizaciones por despido y precarizó los contratos juveniles a través de agencias de empleo temporal."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} La desindustrialización temprana transformó a las orgullosas metrópolis obreras en urbes fragmentadas con enormes bolsones de exclusión y comercio informal."
        }
    ]
}

# 29.04: neoliberalismo-04
k = "neoliberalismo-04"
# Grammar (8):
# 0: Muchos países retomaron cierto crecimiento económico; aun así, este crecimiento no se tradujo en una reducción de la desigualdad.
# 1: El producto interno bruto regional crecía, aun así, sin generar suficientes empleos formales bien remunerados.
# 2: Las cifras de pobreza extrema mejoraron; aun así, la riqueza se concentró todavía más en los sectores más ricos.
# 3: Este contraste alimentaría, aun así, un creciente descontento popular durante la década siguiente.
# 4: Las reformas modernizaron algunos sectores, aumentando al mismo tiempo la desigualdad social.
# 5: Muchas familias enfrentaban la pobreza, buscando nuevas formas de generar ingresos.
# 6: El empleo formal disminuía en algunas regiones, creciendo en cambio el trabajo informal.
# 7: La desigualdad seguía siendo un problema central.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Crecimiento excluyente, desigualdad y la nueva pobreza urbana",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A mediados de los años noventa, los organismos multilaterales celebraban la estabilidad de precios y el regreso de los capitales foráneos. {G(k, 0)} {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 6)} Los sectores financieros, de telecomunicaciones y de agronegocios exportadores acumularon rentabilidades extraordinarias, mientras los salarios reales de los trabajadores se estancaban."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 7)} América Latina consolidó su triste condición de ser la región más desigual del planeta, medida por los coeficientes de Gini más desfavorables del mundo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Familias de clase media empobrecidas abrieron pequeños comercios de subsistencia en sus garajes o dependieron de comedores comunitarios y ollas populares en las barriadas periféricas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} La brecha abismal entre las promesas de bienestar del modelo neoliberal y la amarga realidad de la exclusión social preparó el terreno para los grandes estallidos del nuevo milenio."
        }
    ]
}

# 29.05: neoliberalismo-05
k = "neoliberalismo-05"
# Grammar (8):
# 0: Dicho de otro modo, estas reformas rescataron a la región de una espiral inflacionaria que amenazaba con destruirlo todo.
# 1: Dicho de otro modo, muchos analistas resumen el legado neoliberal como una paradoja.
# 2: El modelo logró domar la inflación; dicho de otro modo, resolvió un problema mientras dejaba otro sin resolver.
# 3: Dicho de otro modo, la estabilidad macroeconómica no garantizó, por sí sola, ni equidad ni resiliencia frente a futuras crisis.
# 4: A pesar de los avances en algunos indicadores, el legado del modelo neoliberal sigue siendo objeto de debate.
# 5: Como consecuencia de estas políticas, el balance entre crecimiento económico y justicia social sigue siendo desigual.
# 6: A raíz de estas experiencias, muchos países revisaron su modelo económico en las décadas siguientes.
# 7: El legado neoliberal incluye tanto logros como críticas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El balance histórico del neoliberalismo y sus paradojas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 7)} Por un lado, {G(k, 0)} Modernizó sistemas de telecomunicaciones, expandió el crédito bancario al consumo y disciplined las cuentas fiscales."
        },
        {
            "type": "narration",
            "text": f"Por otro lado, {G(k, 1)} {G(k, 2)} La desarticulación del tejido industrial, el desempleo estructural masivo y la vulnerabilidad extrema ante los vaivenes de los mercados financieros internacionales desataron violentas crisis de deuda."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Episodios traumáticos como el 'Efecto Tequila' en México (1994) y el colapso de la convertibilidad argentina en 2001 desnudaron la extrema fragilidad del modelo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 6)} La indignación de las mayorías desfavorecidas contra el Consenso de Washington impulsó el surgimiento de nuevos movimientos populares en todo el continente."
        },
        {
            "type": "narration",
            "text": "La búsqueda de un nuevo equilibrio entre eficiencia de mercado, soberanía estatal y justicia distributiva se convirtió en el desafío político central del siglo veintiuno."
        }
    ]
}

# =============================================================================
# UNIT 30: democratizacion
# =============================================================================

# 30.01: democratizacion-01
k = "democratizacion-01"
# Grammar (8):
# 0: La tercera ola de democratización transformó el panorama político latinoamericano entre 1978 y 1990.
# 1: Los regímenes militares cedieron el poder tras perder legitimidad por el fracaso económico y la presión social.
# 2: Las elecciones libres permitieron el retorno de gobiernos civiles elegidos democráticamente.
# 3: El politólogo Samuel Huntington denominó "tercera ola de democratización" a la transición global hacia gobiernos constitucionales.
# 4: En América Latina, este proceso comenzó en República Dominicana en 1978 y en Ecuador en 1979.
# 5: La bancarrota económica, las derrotas militares y la movilización civil socavaron irreversiblemente el poder de las dictaduras.
# 6: Millones de ciudadanos acudieron a las urnas con una mezcla de emoción cívica y fundadas esperanzas de cambio social.
# 7: La transición a la democracia se extendió por la mayoría de los países de América Latina.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Tercera Ola de democratización en América Latina",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Jaime Roldós Aguilera asumió la presidencia ecuatoriana jurando sobre la nueva constitución y proclamando una era de derechos humanos y justicia para los sectores postergados."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 5)} En Perú con Fernando Belaúnde Terry (1980), en Bolivia con Hernán Siles Zuazo (1982) y en Argentina con Raúl Alfonsín (1983), las urnas desplazaron definitivamente a los comandantes militares."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 6)} Filas interminables de votantes conmovidos depositaron sus boletas, poniendo fin a años de toque de queda, censura y terror estatal."
        },
        {
            "type": "narration",
            "text": "La recuperación democrática constituyó una hazaña cívica colectiva, pero los nuevos mandatarios debieron gobernar sobre las ruinas de economías hipotecadas por la crisis de la deuda."
        }
    ]
}

# 30.02: democratizacion-02
k = "democratizacion-02"
# Grammar (8):
# 0: Las transiciones políticas tomaron caminos distintos según el grado de control que mantuvieron las fuerzas armadas.
# 1: En algunos países las dictaduras colapsaron rápidamente tras derrotas militares o crisis internas.
# 2: En otros casos las transiciones fueron negociadas mediante pactos que limitaron el alcance de las reformas.
# 3: La transición argentina fue una "transición por colapso" precipitada por el desastre militar en las islas Malvinas.
# 4: En Chile y Brasil, los mandos militares controlaron y tutelaron el cronograma de apertura durante varios años.
# 5: Los "enclaves autoritarios" y los senadores designados por Pinochet condicionaron la democracia chilena durante más de una década.
# 6: La negociación entre élites políticas y mandos castrenses garantizó la paz pero dejó intactas muchas prerrogativas militares.
# 7: Los diferentes caminos hacia la democracia influyeron en la solidez de las nuevas instituciones.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Transiciones pactadas versus transiciones por colapso",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"La ciencia política comparada ha estudiado con detalle las distintas modalidades de regreso al orden constitucional. {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 3)} La humillante rendición militar en junio de 1982 forzó la retirada desordenada de la junta de Videla y Galtieri, permitiendo a la sociedad juzgar a los comandantes sin condiciones previas."
        },
        {
            "type": "narration",
            "text": f"Por el contrario, {G(k, 2)} {G(k, 4)} En Brasil, la ley de amnistía de 1979 y la elección indirecta de 1985 permitieron a los militares preservar amplias cuotas de poder corporativo."
        },
        {
            "type": "narration",
            "text": f"En Chile, el triunfo del 'NO' en el plebiscito de 1988 abrió paso a la presidencia de Patricio Aylwin, pero {G(k, 5)} Pinochet retuvo la comandancia en jefe del Ejército hasta 1998 y la senaduría vitalicia."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Desmontar gradualmente esas herencias autoritarias requirió décadas de reformas constitucionales y una paciencia cívica formidable."
        }
    ]
}

# 30.03: democratizacion-03
k = "democratizacion-03"
# Grammar (8):
# 0: Varios países promulgaron nuevas constituciones para fundar un nuevo orden democrático.
# 1: La Constitución brasileña de 1988 consagró amplios derechos sociales y garantías individuales.
# 2: La Constitución colombiana de 1991 reconoció la diversidad étnica y creó la figura de la tutela.
# 3: La Constitución brasileña de 1988, bautizada como la "Constitución Ciudadana", refundó el pacto social democrático del país.
# 4: La Asamblea Nacional Constituyente de Colombia de 1991 incorporó a exguerrilleros desmovilizados, indígenas y minorías religiosas.
# 5: La acción de tutela en Colombia se convirtió en el instrumento jurídico más popular y eficaz para la defensa de derechos fundamentales.
# 6: Estas nuevas cartas magnas transformaron el derecho constitucional latinoamericano mediante un constitucionalismo social avanzado.
# 7: Las nuevas constituciones buscaron fortalecer los derechos ciudadanos y limitar el poder autoritario.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El nuevo constitucionalismo y la refundación de los derechos ciudadanos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Para clausurar definitivamente el legado dictatorial y sentar las bases de un Estado de derecho moderno, {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 1)} El texto promulgado por Ulysses Guimarães consagró el Sistema Único de Salud (SUS), la protección de las tierras indígenas y el sufragio para los analfabetos."
        },
        {
            "type": "narration",
            "text": f"En Colombia, en medio de la violencia del narcoterrorismo de Pablo Escobar, el movimiento estudiantil de la 'Séptima Papeleta' forzó la convocatoria a una asamblea plural. {G(k, 4)} {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Cualquier ciudadano podía exigir ante cualquier juez la protección inmediata de su salud, educación o dignidad sin necesidad de abogados costosos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Estas cartas fundamentales convirtieron a los tribunales constitucionales en arenas activas para la ampliación de la ciudadanía."
        }
    ]
}

# 30.04: democratizacion-04
k = "democratizacion-04"
# Grammar (8):
# 0: Las instituciones democráticas mostraron fragilidad frente a crisis económicas y conflictos de poderes.
# 1: Los presidentes enfrentaron juicios políticos y destituciones parlamentarias en varios países.
# 2: La corrupción y el descontento popular provocaron caídas de gobiernos antes del fin de su mandato.
# 3: Los juicios políticos contra Fernando Collor de Mello en Brasil (1992) y Carlos Andrés Pérez en Venezuela (1993) demostraron la activación de los controles parlamentarios.
# 4: En Ecuador y Argentina, masivas protestas populares forzaron la renuncia de presidentes en medio de graves crisis económicas.
# 5: El colapso del sistema de partidos tradicionales en varios países abrió el camino para el surgimiento de nuevos liderazgos de protesta.
# 6: A pesar de estas turbulencias institucionales, los países evitaron el retorno a los golpes militares clásicos del pasado.
# 7: Las crisis políticas pusieron a prueba la estabilidad de las nuevas instituciones democráticas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Juicios políticos, 'golpes de calle' y la resiliencia institucional",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante los años noventa y los primeros años dos mil, las democracias latinoamericanas fueron puestas a prueba por severas tormentas políticas. {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 1)} La movilización de los jóvenes 'caras pintadas' en Brasil empujó al Congreso a destituir a Collor por corrupción patrimonial."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 2)} En Ecuador cayeron Abdalá Bucaram (1997) y Jamil Mahuad (2000), mientras en Argentina las jornadas del 19 y 20 de diciembre de 2001 culminaron con la renuncia del presidente Fernando de la Rúa bajo el grito popular '¡Que se vayan todos!'."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} que canalizaron la profunda indignación cívica frente a la corrupción de las élites tradicionales."
        },
        {
            "type": "narration",
            "text": f"Lo más significativo de esta era fue que, {G(k, 6)} Las crisis se canalizaron por vías civiles y constitucionales, demostrando que la democracia se había arraigado en la conciencia de los pueblos."
        }
    ]
}

# 30.05: democratizacion-05
k = "democratizacion-05"
# Grammar (8):
# 0: La democracia electoral se consolidó en la región, aunque persisten desafíos en la calidad de las instituciones.
# 1: La participación ciudadana aumentó a través de movimientos sociales, organizaciones indígenas y colectivos de mujeres.
# 2: La consolidación democrática requiere profundizar la igualdad social, el Estado de derecho y la transparencia pública.
# 3: A comienzos del siglo veintiuno, América Latina celebraba el periodo más prolongado de continuidad democrática de su historia.
# 4: El desafío principal ya no consistía en evitar golpes de Estado militares, sino en construir democracias con equidad social efectiva.
# 5: La irrupción de movimientos indígenas, feministas y ambientales amplió la agenda política con demandas de soberanía y dignidad.
# 6: La democracia latinoamericana continúa siendo un proyecto en construcción permanente que exige la vigilancia activa de la ciudadanía.
# 7: La consolidación democrática sigue siendo un objetivo central para todos los países de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El balance democrático: ciudadanía activa y desafíos del siglo veintiuno",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 7)} Las elecciones periódicas, transparentes y competitivas se convirtieron en la única fuente indiscutida de legitimidad política."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Una democracia que no garantiza hospitales dignos, escuelas de calidad y salarios justos corre el peligro de defraudar las expectativas de las mayorías trabajadoras."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 5)} El levantamiento zapatista del EZLN en México (1994), la CONAIE en Ecuador y las movilizaciones cocaleras en Bolivia redefinieron la política nacional."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} El combate a la corrupción, la independencia judicial y la desmilitarización de la seguridad ciudadana constituyen tareas impostergables."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} El aprendizaje de décadas de luchas y sacrificios confirmó que solo una ciudadanía consciente y movilizada puede asegurar un futuro de paz, libertad y justicia para América Latina."
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
