#!/usr/bin/env python3
"""Re-author Latin America Track Block 2 (Units 07-12, 36 files).

Units:
07. razaclasepoder
08. independencia
09. nuevasrepublicas
10. caudillismo
11. nacionnacionalismo
12. liberalismomodernizacion

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
    # UNIT 07: razaclasepoder
    # =========================================================================
    "b1-razaclasepoder-01-castas.json": [
        "Ciudad de México, siglo dieciocho. Las élites coloniales vivían obsesionadas con la pureza de sangre y la ascendencia familiar.",
        "Para clasificar a la población, los pintores solían encargar series enteras de cuadros llamados pinturas de castas.",
        "Cada pintura mostraba una cuadrícula con parejas mixtas y sus hijos. Cada mezcla recibía una etiqueta social fija.",
        "Algunos nombres populares eran abiertamente insultantes, como torna atrás o salta atrás.",
        "Estas categorías determinaban qué privilegio legal tenía una persona, qué oficio podía ejercer y qué ropa o armas podía portar en la calle."
    ],
    "b1-razaclasepoder-02-elites.json": [
        "En la cima del poder colonial estaban los peninsulares y los criollos ricos. Controlaban las minas, las haciendas y el fondo público.",
        "Para no dispersar sus fortunas, las familias nobles solían restringir los matrimonios de sus hijos con otras castas.",
        "El mayorazgo aseguraba que la mayor proporción de la herencia pasara intacta al hijo primogénito.",
        "A finales del siglo dieciocho, el vínculo entre criollos y la Corona española comenzó a mostrar una seria ruptura.",
        "El criollo se sentía degradado ante los españoles recién llegados, pero mantenía un diálogo entreabierto para jurar su lealtad al rey."
    ],
    "b1-razaclasepoder-03-posicion.json": [
        "En la base de la pirámide colonial vivía el pueblo oprimido: indígenas, africanos esclavizados y trabajadores mestizos.",
        "Para un hombre manumitido o libre de color, alistarse en la milicia urbana era la única vía para moldear su destino.",
        "El servicio militar ofrecía una codiciada exención de tributos que mejoraba su prestigio social.",
        "Otros esclavos preferían escapar a la selva para convertirse en un cimarrón rebelde.",
        "En las montañas fundaron su propio asentamiento libre o palenque, donde vivían protegidos bajo sus propias leyes."
    ],
    "b1-razaclasepoder-04-mestizaje.json": [
        "La rígida jerarquía de castas parecía inamovible sobre el papel. Pero la realidad cotidiana del mestizaje era mucho más fluida.",
        "La mezcla constante entre grupos llegó a constituir la mayoría de la población en las grandes ciudades virreinales.",
        "Para subir de estatus, algunos individuos ricos decidieron sostener un largo trámite burocrático de gracias al sacar.",
        "Por una tarifa considerable, el rey podía declarar legalmente blanco a un súbdito mestizo adinerado.",
        "Este insólito documento resultaba muy revelador: demostraba que el estatus en la cúspide era en el fondo negociable."
    ],
    "b1-razaclasepoder-05-herencias.json": [
        "Cuando las guerras de independencia comenzaron a estallar en 1810, los nuevos líderes prometieron igualdad para todos los ciudadanos.",
        "Las nuevas repúblicas decidieron abolir la esclavitud y derogar el viejo sistema colonial de castas.",
        "Sin embargo, el cambio legal no logró disolverse en una transformación social inmediata.",
        "El racismo y el prejuicio continuaron pesando sobre las comunidades indígenas y afrodescendientes.",
        "Durante décadas, la sociedad republicana tendió a reproducir la antigua correlación entre color de piel y pobreza, mostrando una dura continuidad histórica."
    ],
    "b1-razaclasepoder.json": [
        "La sociedad colonial hispanoamericana desarrolló un complejo sistema de castas que intentó clasificar a la población según su origen étnico.",
        "Las élites blancas monopolizaban los privilegios y la riqueza, mientras indígenas y afrodescendientes soportaban la mayor carga laboral y fiscal.",
        "Pese a la rigidez oficial, mecanismos como las milicias o la compra de blancura permitieron cierta movilidad social a sectores acomodados.",
        "La independencia abolió legalmente las castas, pero no eliminó las profundas desigualdades heredadas del período colonial.",
        "Ese legado de discriminación y jerarquía continuó marcando la historia social de las repúblicas latinoamericanas independientes."
    ],

    # =========================================================================
    # UNIT 08: independencia
    # =========================================================================
    "b1-independencia-01-mundocambia.json": [
        "Madrid, 1808. Napoleón Bonaparte invade España y encarcela al rey Fernando VII. El trono imperial queda vacante.",
        "La forzada abdicación del monarca cautivo fue el verdadero detonante de la crisis política en toda América hispana.",
        "A pesar de la censura oficial, cada panfleto clandestino circulaba con una clara advertencia contra la tiranía francesa.",
        "En las capitales coloniales, los cabildos decidieron imitar a las juntas provinciales españolas para asumir el gobierno provisional.",
        "Este vacío de poder logró desatar un debate revolucionario: si el rey no gobernaba, la soberanía volvía al pueblo."
    ],
    "b1-independencia-02-guerras.json": [
        "Lo que comenzó como una protesta leal al rey se transformó rápidamente en una cruenta guerra de independencia continental.",
        "El conflicto armado llegó a prolongarse durante años, superando un largo estancamiento militar entre patriotas y el ejército realista.",
        "En México, el levantamiento popular insurgente fue derrotado y las autoridades coloniales decidieron fusilar a sus principales líderes.",
        "En el sur, el general José de San Martín preparó un audaz ejército para cruzar la imponente cordillera de los Andes.",
        "Tras varias victorias en un ataque simultáneo, la batalla de Ayacucho en 1824 logró sellar definitivamente la libertad americana."
    ],
    "b1-independencia-03-lideres.json": [
        "Simón Bolívar soñaba con una patria grande unida desde el Caribe hasta el estrecho de Magallanes.",
        "Acompañado por el general Sucre, logró su mayor hazaña militar al vencer al último bastión realista en el Perú.",
        "El Libertador vio descender su prestigio político cuando las rivalidades locales dividieron a sus propios generales.",
        "A pesar de tener un objetivo coincidente con otros patriotas, fue testigo de la disolución de la Gran Colombia.",
        "Enfermo y con un amargo dolor en el alma, Bolívar decidió renunciar al poder antes de exiliarse hacia la costa."
    ],
    "b1-independencia-04-republicas.json": [
        "Las nuevas naciones nacieron con el campo devastado y el tesoro público inundado de deudas urgentes.",
        "Para financiar sus ejércitos, cada gobierno solicitó un cuantioso préstamo a bancos de Londres.",
        "La especulación financiera desató una burbuja en el mercado bursátil británico con promesas sobre minas de oro inexistentes.",
        "Pronto el negocio fraudulento provocó el pánico y el mercado comenzó a desplomarse con rapidez.",
        "El impago generalizado obligó a renegociar las cuotas bajo un presupuesto improvisado y lleno de carencias."
    ],
    "b1-independencia-05-paraquien.json": [
        "En cada plaza mayor, los líderes se reunieron para proclamar con entusiasmo solemne la independencia y la libertad ciudadana.",
        "Los congresos se apresuraron a sancionar constituciones liberales que prometían derechos universales y división de poderes.",
        "Sin embargo, para los campesinos e indígenas, muchas de estas promesas resultaron ser un discurso puramente retórico.",
        "Los nuevos gobiernos comenzaron a desmantelar la propiedad comunal de los pueblos nativos para acelerar las ventas privadas.",
        "La igualdad prometida en los textos legales era prácticamente inexistente en la vida cotidiana de las clases populares."
    ],
    "b1-independencia.json": [
        "La invasión napoleónica de España en 1808 desató una crisis de legitimidad que desembocó en las guerras de independencia hispanoamericanas.",
        "Líderes militares como Simón Bolívar y José de San Martín coordinaron campañas continentales para derrotar al ejército realista.",
        "Tras quince años de sangrientas batallas, las colonias españolas lograron su emancipación política, sellada en la batalla de Ayacucho.",
        "Las nuevas repúblicas nacieron arruinadas por la guerra, endeudadas con bancos extranjeros y fragmentadas por rivalidades regionales.",
        "Aunque se proclamaron constituciones liberales modernas, las jerarquías sociales tradicionales se mantuvieron casi intactas para la mayoría."
    ],

    # =========================================================================
    # UNIT 09: nuevasrepublicas
    # =========================================================================
    "b1-nuevasrepublicas-01-estado.json": [
        "Construir un estado moderno desde la nada fue una tarea titánica para las élites criollas victoriosas.",
        "Cada nueva república intentó redactar su propia constitución, crear una moneda nacional y organizar un servicio de correo postal.",
        "La falta de dinero era crítica: sin aduanas eficientes, cobrar el impuesto resultaba casi imposible en provincias lejanas.",
        "El sueño de mantener una gran federación continental fracasó cuando Centroamérica y la Gran Colombia terminaron por disolverse.",
        "Cada facción armada defendía sus propios intereses locales, dejando al joven país en un rumbo sumamente incierto."
    ],
    "b1-nuevasrepublicas-02-fronteras.json": [
        "Durante tres siglos coloniales, la Corona española nunca se preocupó por trazar un límite exacto en selvas despobladas.",
        "Al nacer las repúblicas independientes, cartografiar el territorio nacional se convirtió en una prioridad urgente de soberanía.",
        "Muchos documentos antiguos tenían un trazado impreciso sobre cada tramo de la frontera internacional.",
        "Los diplomáticos decidieron renegociar los tratados limítrofes y posponer las decisiones conflictivas para evitar la guerra.",
        "A pesar de la diplomacia, las disputas territoriales provocaron tensiones constantes entre cada país vecino."
    ],
    "b1-nuevasrepublicas-03-liberales.json": [
        "La vida política hispanoamericana se dividió pronto en dos bandos irreconciliables: liberales y conservadores.",
        "Ambos grupos solían discrepar agriamente sobre el papel de la Iglesia católica como pilar de la sociedad tradicional.",
        "Los liberales querían despojar al clero de sus bienes para estimular el mercado de tierras y el libre comercio.",
        "Los conservadores preferían desechar las ideas extranjeras para proteger la religión católica y el orden jerárquico establecido.",
        "La política oscilaba constantemente entre guerras civiles y acuerdos frágiles sin alcanzar un matiz de paz definitivo."
    ],
    "b1-nuevasrepublicas-04-inestabilidad.json": [
        "El mayor drama de las nuevas repúblicas fue la constante inestabilidad de sus gobiernos ejecutivos.",
        "Ningún ejército regular estaba verdaderamente subordinado al poder civil ni respetaba el orden constitucional vigente.",
        "Cualquier militar con suficiente rango y tropas leales podía encabezar un golpe de estado y derrocar al presidente de turno.",
        "Pocos mandatarios lograban respaldar las leyes y completar su mandato presidencial de forma pacífica y constitucional.",
        "La guerra civil parecía inevitable y la violencia partidista llegó a perdurar como el método habitual para acceder al poder."
    ],
    "b1-nuevasrepublicas-05-desafios.json": [
        "Hacia mediados del siglo diecinueve, el desafío fundamental de América Latina seguía siendo la integración nacional.",
        "Muchos pueblos del interior permanecían en un rincón aislado por falta de caminos transitables.",
        "Las constituciones tenían a menudo un efecto efímero, dejando como único precedente la violencia de los cuartelazos.",
        "El comercio exterior dependía de la venta de material bruto agrícola sin valor industrial agregado.",
        "Con un préstamo impagado y un presupuesto con éxito apenas parcial, el estado tuvo que movilizar tropas para sobrevivir."
    ],
    "b1-nuevasrepublicas.json": [
        "Tras la independencia, las repúblicas hispanoamericanas enfrentaron la difícil tarea de construir instituciones estatales sólidas y legítimas.",
        "La ausencia de límites fronterizos claros generó disputas diplomáticas y conflictos armados entre países vecinos recién independizados.",
        "El enfrentamiento ideológico entre liberales y conservadores polarizó a las sociedades en torno a los privilegios de la Iglesia y el federalismo.",
        "Los continuos golpes de estado y la falta de subordinación militar convirtieron la inestabilidad política en la norma general.",
        "Pese a los constantes desafíos económicos y la fragmentación territorial, las jóvenes naciones lograron consolidar su soberanía nacional."
    ],

    # =========================================================================
    # UNIT 10: caudillismo
    # =========================================================================
    "b1-caudillismo-01-caudillo.json": [
        "Buenos Aires, 1835. La atmósfera en la ciudad es densa y asfixiante. Un solo hombre domina el destino de Argentina: Juan Manuel de Rosas.",
        "En el siglo diecinueve, un caudillo no necesita leyes escritas. Gobierna con su carisma personal y sus tropas leales. Su poder es una realidad de facto.",
        "La legislatura provincial le otorga facultades extraordinarias con poderes prácticamente ilimitados sobre la vida y la hacienda de todos.",
        "Rosas organiza a la temida Mazorca para intimidar a los rivales. Exige lealtad absoluta y castiga con rigor cualquier señal de disidencia.",
        "El caudillo utiliza la fuerza para sofocar rebeliones provinciales, llenando el vacío dejado por la caída de las instituciones coloniales."
    ],
    "b1-caudillismo-02-poderpersonal.json": [
        "¿De dónde venía el enorme poder de estos hombres fuertes de las pampas y los valles americanos?",
        "El caudillo solía ser un rico hacendado que controlaba miles de cabezas de ganado y cientos de peones leales.",
        "Los peones eran excelentes jinetes acostumbrados a obedecer ciegamente la voz de mando de su patrón.",
        "Cuando el líder vencía a un rival peligroso, repartía el terreno confiscado entre sus aliados más fieles.",
        "Todo funcionario sabía que su puesto dependía de un vínculo frágil; si el líder decidía retirar su protección, caía en desgracia."
    ],
    "b1-caudillismo-03-ejercitopolitica.json": [
        "En un continente en guerra civil permanente, quien dominaba la caballería armada dominaba las decisiones del país.",
        "El caudillo sabía reclutar a cientos de lanceros en pocos días para marchar directamente sobre la capital.",
        "Muchos líderes comenzaron su carrera al ostentar un modesto rango militar en las guerras de independencia.",
        "Eran maestros en preparar la emboscada perfecta en el monte, causando el colapso instantáneo de los ejércitos regulares.",
        "Las investigaciones históricas buscan esclarecer cómo estos jefes guerreros lograron construir un poder tan duradero."
    ],
    "b1-caudillismo-04-ordeninestabilidad.json": [
        "Para las élites letradas de las capitales, el caudillo representaba un mundo rural atrasado y salvaje.",
        "Cualquier opositor político corría el riesgo de terminar exiliado en el extranjero o en una celda oscura.",
        "Sin embargo, para el campesino humilde, el caudillo garantizaba un mínimo orden frente al caos de bandoleros.",
        "Los intelectuales solían amenazar con leyes y poner la etiqueta de tirano a todo líder popular que desafiara su control.",
        "La mirada revisionista moderna comprende que estos líderes respondían a las demandas reales de sectores antes ignorados."
    ],
    "b1-caudillismo-05-legado.json": [
        "Hacia finales del siglo diecinueve, el avance de los ferrocarriles y el comercio exterior comenzó a debilitar al caudillismo tradicional.",
        "Un estado nacional consolidado requería leyes estables y un consenso institucional, no milicias guiadas por un mando personalista.",
        "El politólogo contemporáneo analiza cómo el caudillismo decimonónico dejó una profunda huella en la cultura política latinoamericana.",
        "La tradición del líder autoritario demostró ser un fenómeno poroso que logró sobrevivir bajo nuevas formas presidenciales.",
        "El peso de esta herencia personalista sigue influyendo con fuerza y suele pesar en las democracias de toda la región."
    ],
    "b1-caudillismo.json": [
        "El caudillismo surgió como respuesta al vacío de poder y a la anarquía política que siguieron a las guerras de independencia.",
        "Líderes rurales apoyados en su carisma, su riqueza ganadera y sus tropas leales se convirtieron en árbitros indiscutibles de la política.",
        "Caudillos como Rosas en Argentina o Santa Anna en México gobernaron mediante redes personales de lealtad, violencia y patronazgo.",
        "Aunque eran criticados por las élites ilustradas como tiranos violentos, muchos sectores populares los apoyaron porque imponían orden.",
        "Con la modernización económica de finales del siglo diecinueve, los caudillos dieron paso a estados más centralizados y organizados."
    ],

    # =========================================================================
    # UNIT 11: nacionnacionalismo
    # =========================================================================
    "b1-nacionnacionalismo-01-nacion.json": [
        "Lograda la independencia, los gobernantes descubrieron que tener un territorio no significaba automáticamente tener una nación.",
        "Hacía falta forjar un fuerte sentimiento de pertenencia en poblaciones profundamente divididas por origen étnico y geografía.",
        "Un modesto artesano del interior poco tenía en común con un rico comerciante porteño educado en Europa.",
        "Para estrechar el vínculo cívico, los gobiernos diseñaron un ritual patriótico obligatorio en cada fiesta nacional.",
        "Construir un destino común fue un acto deliberado que nadie podía dar por sentado de antemano."
    ],
    "b1-nacionnacionalismo-02-simbolos.json": [
        "Para que la patria cobrara vida en los corazones, los nuevos países crearon un poderoso repertorio de símbolos patrios.",
        "Se organizó un concurso público para elegir la letra del himno y el diseño del escudo nacional oficial.",
        "Bajo un cielo despejado, la multitud entonaba cantos que parecían brotar como un sentimiento espontáneo.",
        "Los poetas buscaron la esencia de la nacionalidad, imaginando raíces en un pasado glorioso y a menudo milenario.",
        "La bandera tricolor se convirtió en un objeto sagrado que debía venerarse con reverencia patriótica en cada escuela."
    ],
    "b1-nacionnacionalismo-03-identidad.json": [
        "La historia patria se convirtió en la herramienta educativa más eficaz para enseñar civismo a las nuevas generaciones.",
        "El historiador oficial intentaba presentar un relato convincente que narrara fielmente las glorias de los próceres militares.",
        "Este discurso buscaba despertar un sincero orgullo nacional, pero su contenido resultaba muy revelador sobre las exclusiones del país.",
        "El pueblo indígena sufría una constante marginación social y veía su cultura considerada como un elemento perjudicado y atrasado.",
        "El debate democrático quedaba clausurado por un patriotismo arraigado que no aceptaba críticas a los mitos fundacionales."
    ],
    "b1-nacionnacionalismo-04-pueblosfronteras.json": [
        "En los valles altos de los Andes, la nueva geografía republicana partió en dos a comunidades ancestrales que compartían la misma lengua.",
        "En el altiplano andino, los pueblos aymaras y quechuas mantuvieron un comercio transfronterizo tradicional sin importar las líneas divisorias.",
        "La soberanía estatal intentó imponer un discurso coherente y crear un ciudadano culturalmente homogéneo mediante la escuela.",
        "Sin embargo, la realidad solía contradecir las fronteras oficiales: cada festividad patronal seguía uniendo a pueblos vecinos a ambos lados.",
        "La identidad local compartida no siempre lograba coincidir con los límites dibujados por los mapas oficiales de los gobiernos."
    ],
    "b1-nacionnacionalismo-05-imaginarnacion.json": [
        "A finales del siglo diecinueve, los estados latinoamericanos lograron consolidar una idea de patriotismo en toda la población.",
        "El ambicioso proyecto de modernización sirvió como telón de fondo para recorrer el territorio con ferrocarriles y escuelas públicas.",
        "El gobierno se presentaba como el único líder legítimo, promoviendo un amor patrio que debía ser eterno y sagrado.",
        "Los opositores denunciaban la mentira de los discursos oficiales, acusando al presidente de ser un político manipulador.",
        "A pesar de los conflictos, el resultado previsto se cumplió: millones de personas comenzaron a sentirse parte de una misma patria."
    ],
    "b1-nacionnacionalismo.json": [
        "Durante el siglo diecinueve, los gobiernos latinoamericanos construyeron activamente una identidad nacional para unir a sus habitantes.",
        "Símbolos patrios como himnos, banderas y escudos fueron inventados para despertar orgullo y lealtad hacia la patria naciente.",
        "La escuela pública y la historia oficial enseñaron relatos heroicos que exaltaban a los próceres de la independencia.",
        "Este nacionalismo oficial a menudo ignoró la diversidad de los pueblos indígenas, imponiendo una identidad homogénea desde las capitales.",
        "Pese a las tensiones fronterizas y regionales, el sentimiento de pertenencia nacional terminó por arraigarse profundamente en toda la región."
    ],

    # =========================================================================
    # UNIT 12: liberalismomodernizacion
    # =========================================================================
    "b1-liberalismomodernizacion-01-ideas.json": [
        "Hacia mediados del siglo diecinueve, una nueva generación de políticos liberales llegó al poder en gran parte de América Latina.",
        "Inspirados por las ideas del progreso, impulsaron un conjunto de leyes para modernizar la economía y la sociedad.",
        "Soñaban con un orden igualitario, pero en la práctica mantenían el estricto requisito de alfabetización para votar.",
        "La gran mayoría campesina e indígena quedaba como un sector excluido del derecho al sufragio universal en las elecciones.",
        "Este cambio ideológico radical no pasó desapercibido y provocó la feroz resistencia armada de los sectores conservadores tradicionales."
    ],
    "b1-liberalismomodernizacion-02-reformar.json": [
        "El golpe más audaz de las reformas liberales estuvo dirigido contra el inmenso patrimonio de la Iglesia católica.",
        "En México, las Leyes de Reforma impulsadas por Benito Juárez decidieron nacionalizar los bienes eclesiásticos y crear el registro civil.",
        "El estado asumió el control de los nacimientos, actas de defunción y matrimonios, que antes dependían del sacramento parroquial.",
        "Este controvertido proceso desató un conflicto sangriento que llegó a prolongarse durante años entre creyentes y tropas del gobierno.",
        "Muchos liberales llegaron a dar por sentado el triunfo del laicismo, pero las tierras confiscadas pasaron a manos de un nuevo propietario rico."
    ],
    "b1-liberalismomodernizacion-03-iglesiayestado.json": [
        "La Iglesia católica había sido durante tres siglos el pilar espiritual y moral indiscutible del continente americano.",
        "Los conservadores defendían el antiguo concordato con Roma para otorgar a la Iglesia el control total sobre la educación pública.",
        "Los liberales querían un estado laico y consideraban que el progreso difícilmente podía avanzar bajo el dominio eclesiástico.",
        "En Ecuador, las tensiones llegaron a su punto máximo con el sangriento asesinato del presidente conservador Gabriel García Moreno.",
        "Separar el altar del gobierno fue una tarea titánica que ningún mandatario posterior logró revertir por completo."
    ],
    "b1-liberalismomodernizacion-04-modernizar.json": [
        "Para los gobernantes de la época, la palabra mágica era una sola: progreso a través de la tecnología moderna.",
        "Las compañías extranjeras aportaron el capital necesario para tender miles de kilómetros de vía férrea hacia los puertos.",
        "Los ingenieros se dedicaron a trazar líneas telegráficas para conectar zonas que antes vivían en un aislamiento incomunicado.",
        "El auge minero del salitre en el desierto enriqueció al estado, que decidió no posponer sus grandes obras de infraestructura.",
        "El célebre lema de orden y progreso se convirtió en la guía indiscutible de las nuevas élites oligárquicas gobernantes."
    ],
    "b1-liberalismomodernizacion-05-nuevomodelo.json": [
        "El impacto económico de las reformas liberales fue un hecho innegable en toda América Latina a finales del siglo diecinueve.",
        "El nuevo modelo económico comenzó a depender casi exclusivamente de la exportación masiva de materia prima hacia el mercado exterior.",
        "El gobierno buscó integrar a las regiones productivas en las rutas mundiales, pero dejó al margen a las comunidades campesinas pobres.",
        "Este crecimiento rápido generó un ritmo comercial vertiginoso, aunque con un desarrollo sumamente divergente y desigual entre el campo y la ciudad.",
        "La prosperidad de las élites exportadoras sentó las bases materiales de los estados modernos latinoamericanos."
    ],
    "b1-liberalismomodernizacion.json": [
        "En la segunda mitad del siglo diecinueve, los gobiernos liberales impulsaron reformas radicales para modernizar a sus países.",
        "Leyes laicas separaron la Iglesia del Estado, nacionalizando bienes eclesiásticos y creando registros civiles de nacimiento y matrimonio.",
        "Inversiones extranjeras británicas y estadounidenses financiaron la construcción de ferrocarriles, puertos y redes de telégrafo.",
        "Las economías se orientaron a la exportación masiva de materias primas agrícolas y minerales hacia los mercados de Europa y Estados Unidos.",
        "Aunque las ciudades se modernizaron con rapidez, este modelo de desarrollo desigual aumentó la brecha social con el campesinado."
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
        print(f"Updated: {filename} ({len(new_paragraphs)} paragraphs)")

    print(f"\nTotal Block 2 stories successfully re-authored: {updated}/36")

if __name__ == "__main__":
    update_stories()
