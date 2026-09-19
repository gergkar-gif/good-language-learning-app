#!/usr/bin/env python3
"""Re-author Latin America Track Block 3 (Units 13-18, 36 files).

Units:
13. economiasexportacion
14. cambiosocial
15. revolucion
16. revolucionmexicana
17. nacionalismo
18. grandepresion

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
    # UNIT 13: economiasexportacion
    # =========================================================================
    "b1-economiasexportacion-01-modelo.json": [
        "A finales del siglo diecinueve, América Latina entró de lleno en la red mercantil mundial.",
        "Cada país decidió especializarse en el producto agrícola o minero más rentable para generar un ingreso extraordinario.",
        "El puerto de la metrópoli europea recibía toneladas de café, azúcar y guano como fertilizante natural para sus campos.",
        "Bancos británicos aportaron el financiamiento necesario para construir muelles modernos y líneas de ferrocarril.",
        "Sin embargo, este modelo dejaba a toda la economía nacional sumamente expuesta a las crisis financieras internacionales."
    ],
    "b1-economiasexportacion-02-productos.json": [
        "El mapa económico del continente se dividió según los recursos naturales de cada región.",
        "En el norte de Chile, el auge del salitre impulsó la explotación de cada yacimiento para fabricar fertilizantes y explosivos.",
        "En las pampas argentinas, la invención de barcos con refrigeración permitió exportar carne fresca además del tradicional cuero.",
        "En Centroamérica y Brasil, el cultivo del café y del banano requería una enorme disponibilidad de mano de obra barata.",
        "El valor de las exportaciones no tardó en superar ampliamente a las viejas industrias locales del interior."
    ],
    "b1-economiasexportacion-03-ferrocarriles.json": [
        "Para los gobiernos de la época, entregar concesiones a compañías extranjeras parecía una oferta sumamente tentadora.",
        "El empresario foráneo solía administrar puertos y ferrocarriles bajo un régimen cerrado de enclave económico.",
        "Las vías conectaban directamente las minas con los barcos, sin trazar ninguna ruta hacia los pueblos vecinos.",
        "La mayor ganancia salía directamente al exterior, impidiendo el crecimiento de una verdadera industria nacional de manufactura.",
        "El país construyó una red de transporte moderna, pero diseñada para servir a mercados lejanos antes que a su propia gente."
    ],
    "b1-economiasexportacion-04-trabajo.json": [
        "Detrás del fabuloso auge exportador se escondía una dura realidad de explotación humana en el campo.",
        "Para reclutar trabajadores, los terratenientes usaban el sistema de enganche con un pequeño adelanto en dinero.",
        "La tienda de raya lograba atar al peón mediante deudas impagables que pasaban de padres a hijos.",
        "El patrón poderoso aprovechó las leyes liberales para despojar a los campesinos de sus tierras comunales.",
        "De este modo, la gran extensión del latifundio creció a costa de la ruina de miles de familias rurales."
    ],
    "b1-economiasexportacion-05-dependencia.json": [
        "La exportación masiva generó una bonanza económica sin precedentes para las élites oligárquicas.",
        "El gobierno decidió destinar gran parte de los ingresos fiscales al lujo urbano y a palacios de gobierno.",
        "Nadie pensó en ahorrar para amortiguar futuras crisis o inventar un sustituto productivo nacional.",
        "El peligro permanecía oculto tras las estadísticas de aduana hasta que ocurrió lo imprevisible.",
        "En última instancia, cuando los precios mundiales cayeron en picada, toda la economía nacional se derrumbó."
    ],
    "b1-economiasexportacion.json": [
        "Entre 1870 y 1914, América Latina se integró plenamente al mercado mundial como proveedora de materias primas.",
        "Cada nación se especializó en productos específicos: café, carne congelada, cobre, salitre o azúcar para Europa.",
        "El capital extranjero financió puertos y ferrocarriles que operaron a menudo como enclaves desconectados del interior.",
        "En el campo, el crecimiento del latifundio y el sistema de enganche endeudaron a millones de peones indígenas.",
        "Esta bonanza exportadora enriqueció a las élites, pero dejó a los países en una peligrosa dependencia exterior."
    ],

    # =========================================================================
    # UNIT 14: cambiosocial
    # =========================================================================
    "b1-cambiosocial-01-ciudades.json": [
        "Buenos Aires, 1900. La antigua aldea colonial se ha convertido en una metrópoli deslumbrante con avenidas monumentales.",
        "El centro urbano cuenta con bulevares arbolados, alumbrado eléctrico moderno y un nuevo alcantarillado subterráneo.",
        "El intendente de la capital ordena abrir amplias calles con adoquín pavimentado para imitar a París.",
        "Pero al otro lado de las avenidas, la periferia obrera crece sin agua potable ni servicios básicos.",
        "Las familias humildes habitan chozas precarias que suelen carecer por completo de higiene y luz natural."
    ],
    "b1-cambiosocial-02-clases.json": [
        "El crecimiento económico transformó profundamente la estructura social de las grandes capitales latinoamericanas.",
        "La oligarquía tradicional de terratenientes y hacendados compartía ahora el poder con el comerciante adinerado.",
        "Surgió una nueva clase media formada por el funcionario de aduana, el maestro de escuela y el médico profesional.",
        "En las fábricas comenzó a instalarse una clase obrera moderna con el obrero metalúrgico y el trabajador portuario.",
        "Las industrias comenzaron a emplear a miles de hombres, mujeres y jóvenes en jornadas laborales agotadoras."
    ],
    "b1-cambiosocial-03-inmigracion.json": [
        "Para poblar las ciudades y el campo, los gobiernos impulsaron una célebre política de inmigración europea masiva.",
        "La promesa de tierra y trabajo logró atraer a millones de italianos, españoles y alemanes hacia el cono sur.",
        "Muchos campesinos llegaron como colonos agrícolas, pero la mayoría terminó hacinada en el puerto de llegada.",
        "En Buenos Aires y Montevideo nació el conventillo superpoblado, donde decenas de familias compartían un solo patio.",
        "Para sobrevivir a la miseria, los inmigrantes organizaron sociedades de socorro mutuo para proteger a su comunidad."
    ],
    "b1-cambiosocial-04-conflicto.json": [
        "Las pésimas condiciones laborales no tardaron en despertar un profundo descontento en los talleres y fábricas.",
        "Las ideas anarquistas y socialistas encontraron un fuerte eco entre los trabajadores recién llegados de Europa.",
        "El sindicato obrero organizó la huelga general para exigir mejores salarios y una jornada laboral digna.",
        "La respuesta de los gobiernos fue enviar a la tropa militar para reprimir y deportar a los líderes sindicales sin juicio.",
        "Tragedias como la matanza de la escuela Santa María de Iquique en 1907 mostraron la brutalidad estatal contra el pueblo."
    ],
    "b1-cambiosocial-05-transformacion.json": [
        "Al comenzar el siglo veinte, la sociedad latinoamericana logró alcanzar una transformación profunda y rápida.",
        "Cualquier observador atento notaba que el mundo urbano comenzaba a predominar en la vida de la nación.",
        "En el ritmo cotidiano de la ciudad se abrió una marcada brecha social entre los palacios y los conventillos.",
        "En un futuro cercano, este descontento popular estallaría en demandas de participación democrática.",
        "El obrero y el hacendado compartían la misma patria como compatriotas, pero habitaban mundos opuestos."
    ],
    "b1-cambiosocial.json": [
        "La bonanza agroexportadora impulsó una rápida urbanización en las principales capitales de América Latina.",
        "Llegaron millones de inmigrantes europeos al cono sur, transformando la cultura urbana y poblando los conventillos.",
        "Junto a la vieja oligarquía terrateniente crecieron nuevas clases medias educadas y un proletariado industrial combativo.",
        "El descontento obrero dio origen a las primeras huelgas organizadas, reprimidas con dureza por los gobiernos de la época.",
        "A inicios del siglo veinte, las profundas desigualdades sociales anunciaban una era de rebeliones y grandes reformas."
    ],

    # =========================================================================
    # UNIT 15: revolucion
    # =========================================================================
    "b1-revolucion-01-quees.json": [
        "¿Qué significa realmente una revolución social en la historia contemporánea de América Latina?",
        "No se trata de un simple cuartelazo militar para derrocar a un presidente y sustituir a un gobernante por otro amigo.",
        "Una revolución auténtica busca abolir las viejas jerarquías y transformar la tenencia de la tierra de raíz.",
        "Cuando el pueblo decide sublevarse con las armas, nada del viejo orden político permanece intacto.",
        "Es un proceso doloroso y exigente que redefine quién debe poseer la riqueza y el poder del estado."
    ],
    "b1-revolucion-02-tierraypoder.json": [
        "En el campo latinoamericano, el conflicto por la tierra era una bomba de tiempo lista para estallar.",
        "El despojo constante de tierras comunales por las haciendas azucareras acumuló una insoportable tensión campesina.",
        "Las comunidades indígenas reclamaron colectivamente sus tierras ancestrales robadas durante el siglo diecinueve.",
        "La famosa consigna de Tierra y Libertad sintetizó la demanda histórica de millones de campesinos sin tierra.",
        "Frente a la represión armada de la policía rural, el descontento contenido terminó por quebrar toda neutralidad política."
    ],
    "b1-revolucion-03-trabajadores.json": [
        "En las ciudades, la corriente obrera creció al calor de las fábricas textiles, minas y puertos comerciales.",
        "Los trabajadores comenzaron a organizarse y lograron articularse a escala nacional para exigir derechos laborales y dignidad.",
        "Los líderes sindicales aprendieron que para derrotar al enemigo oligárquico era necesario aliarse con los campesinos del interior.",
        "Juntos buscaron tender un puente político sólido para lograr un cambio estructural y duradero en el país.",
        "La unión de obreros y campesinos alteró para siempre el equilibrio de fuerzas en la política continental."
    ],
    "b1-revolucion-04-estado.json": [
        "El estallido revolucionario provocó la caída del antiguo régimen y dejó un estado completamente fracturado.",
        "Distintas facciones armadas comenzaron a disputar el poder, y el conflicto llegó a derivar en una guerra sangrienta.",
        "El país tomó un rumbo alejado de la moderación política hasta que los líderes lograron estabilizar el gobierno.",
        "Aprobaron un texto constitucional fundacional que examinó las demandas populares para fijar el costo de las reformas.",
        "El enorme costo humano de la violencia revolucionaria dejó una marca indeleble en la memoria de toda la sociedad."
    ],
    "b1-revolucion-05-cuandocambia.json": [
        "Las revoluciones no ocurren por capricho. Requieren que coincidan varias condiciones históricas excepcionales.",
        "Hacía falta que un descontento popular acumulado lograra estallar ante la debilidad visible del régimen gobernante.",
        "Un liderazgo oportuno y coordinado era indispensable para reunir a sectores sociales diversos en un solo frente.",
        "Cuando las autoridades no hicieron ninguna concesión democrática, el sistema se volvió vulnerable a la insurrección armada.",
        "La historia demostró que un pueblo decidido puede derribar las estructuras más poderosas si lucha unido."
    ],
    "b1-revolucion.json": [
        "Una revolución social en América Latina significó mucho más que un cambio de gobernante o un golpe de estado.",
        "El despojo de tierras comunales campesinas y la explotación obrera crearon condiciones para rebeliones masivas.",
        "La alianza entre campesinos armados y obreros organizados desafió con éxito a las oligarquías exportadoras tradicionales.",
        "El colapso de los antiguos estados oligárquicos dio paso a constituciones pioneras en materia de derechos sociales.",
        "Estas transformaciones radicales demostraron que la presión popular organizada podía transformar las estructuras del poder."
    ],

    # =========================================================================
    # UNIT 16: revolucionmexicana
    # =========================================================================
    "b1-revolucionmexicana-01-porfiriato.json": [
        "México, 1910. El general Porfirio Díaz lleva más de tres décadas en el poder absoluto gracias a reelegirse continuamente.",
        "El régimen exhibe con orgullo cada notable indicador de crecimiento económico: ferrocarriles, minas e inversiones extranjeras.",
        "Sin embargo, la implacable miseria campesina y la falta de libertades políticas crearon la precondición de la tormenta.",
        "Cuando Díaz decidió encarcelar al candidato opositor Francisco Madero tras unos comicios cuestionados, encendió la mecha definitiva.",
        "El llamado a la rebelión armada encontró una respuesta inmediata en todo el territorio mexicano."
    ],
    "b1-revolucionmexicana-02-madero.json": [
        "Francisco I. Madero era un acaudalado hacendado del norte de convicciones democráticas sinceras.",
        "Desde el exilio decidió redactar el Plan de San Luis, declarando ilegítimo al gobierno de Porfirio Díaz.",
        "La insurrección armada convocada para el veinte de noviembre de 1910 se convirtió en una ola popular imparable.",
        "Sitiado por guerrilleros campesinos en todo el país, el viejo dictador tuvo que firmar su renuncia y partir al exilio.",
        "Madero asumió el poder, pero su intento de reforma gradual terminó por sembrar dudas entre los campesinos impacientes."
    ],
    "b1-revolucionmexicana-03-zapatayvilla.json": [
        "En el sur campesino de Morelos, Emiliano Zapata decidió proclamar la ruptura con Madero mediante el Plan de Ayala.",
        "Exigió devolver de inmediato cada campo que había sido arrebatado a los pueblos indígenas por los hacendados.",
        "En el norte, el temido Pancho Villa lideraba la División del Norte para impedir el regreso de los viejos generales porfiristas.",
        "El triunfo de los caudillos campesinos en la capital fue efímero frente al avance del ejército constitucionalista.",
        "Aunque ambos líderes murieron asesinados, su memoria se transformó en un símbolo inmortal de la justicia popular."
    ],
    "b1-revolucionmexicana-04-constitucion.json": [
        "Querétaro, 1917. Tras un conflicto sangriento y feroz, los diputados debaten una nueva carta magna para pacificar la patria.",
        "La Constitución de 1917 creó un marco legal vanguardista que asombró a los juristas de todo el mundo.",
        "El artículo 27 estableció que las tierras pertenecían originariamente a la nación para redistribuir los recursos y el subsuelo.",
        "El artículo 123 fijó la jornada máxima de ocho horas y un salario digno para construir un país industrializado.",
        "Fue la primera constitución de la historia que consagró derechos sociales para el campesinado y la clase obrera."
    ],
    "b1-revolucionmexicana-05-legado.json": [
        "La Revolución mexicana dejó una terrible cifra de más de un millón de muertos por la violencia y el hambre.",
        "Para consolidar la paz y absorber la disidencia armada, los vencedores crearon un sistema político institucional.",
        "El partido oficial gobernó el país de forma ininterrumpida durante décadas, buscando un equilibrio definitivo.",
        "La herencia cultural de la gesta armada se reflejó con orgullo en los muros de las escuelas y palacios públicos.",
        "La memoria de aquella lucha popular sigue siendo un ejemplo único de patriotismo y resistencia en América Latina."
    ],
    "b1-revolucionmexicana.json": [
        "En 1910, el fraude electoral del régimen porfirista desató la primera gran revolución social del siglo veinte en América Latina.",
        "Madero inició la rebelión política, pero líderes campesinos como Zapata y Villa exigieron una profunda reforma agraria.",
        "Diez años de sangrientos combates destruyeron el viejo ejército federal y fracturaron las estructuras oligárquicas tradicionales.",
        "La Constitución de 1917 consagró derechos laborales históricos y el control nacional sobre los recursos del subsuelo.",
        "El nuevo estado institucionalizó el legado revolucionario a través de la reforma agraria, la educación y el arte muralista."
    ],

    # =========================================================================
    # UNIT 17: nacionalismo
    # =========================================================================
    "b1-nacionalismo-01-estadosmasfuertes.json": [
        "Durante las décadas de 1920 y 1930, los gobiernos latinoamericanos decidieron emprender una profunda modernización estatal.",
        "Había que poner fin al déficit crónico mediante una eficaz recaudación de tributos en aduanas y puertos.",
        "Los ministros se esforzaron por profesionalizar las fuerzas armadas y crear bancos centrales independientes.",
        "Cada nuevo ministerio gubernamental comenzó a recopilar rigurosas estadísticas para planificar el desarrollo.",
        "El poder público quedó estrechamente entrelazado con las metas económicas del desarrollo industrial nacional."
    ],
    "b1-nacionalismo-02-cultural.json": [
        "El nacionalismo de entreguerras no fue solo administrativo; fue una auténtica revolución cultural y artística.",
        "El gobierno aprobó un presupuesto destinado a contratar a destacados pintores para cubrir los muros públicos.",
        "El muralismo rindió un emotivo homenaje al pasado prehispánico y a la dignidad del trabajador humilde.",
        "Cada escritor e intelectual apoyó el proyecto oficial para combatir la marginación cultural en todo rincón alejado de la patria.",
        "La cultura oficial integró con orgullo las raíces indígenas en el corazón de la identidad nacional."
    ],
    "b1-nacionalismo-03-educacion.json": [
        "Llevar la escuela a cada rincón remoto de la patria se convirtió en una verdadera misión cívica nacional.",
        "Bajo el liderazgo de José Vasconcelos en México, miles de maestros rurales viajaron a la sierra para alfabetizar al pueblo.",
        "La meta era extender la lengua nacional y despertar un fuerte sentido de pertenencia en cada niño campesino.",
        "El estado aumentó su esfuerzo fiscal para construir escuelas, bibliotecas populares y centros de salud comunitaria.",
        "El historiador moderno reconoce que este proyecto educativo fue decisivo para consolidar las identidades nacionales."
    ],
    "b1-nacionalismo-04-poblaciones.json": [
        "Para gobernar con eficacia, el estado moderno necesitaba conocer con precisión a cada habitante de su territorio.",
        "El gobierno organizó el primer censo nacional sistemático para registrar nacimientos, oficios y lenguas habladas.",
        "Los funcionarios comenzaron a gestionar el reclutamiento militar obligatorio y a enviar al recaudador a pueblos lejanos.",
        "Las comunidades indígenas que antes gozaban de un gobierno local autónomo pasaron a depender del poder de la capital.",
        "El alcance del estado dejó de ser nominal y se transformó en una presencia cotidiana en la vida de todos los ciudadanos."
    ],
    "b1-nacionalismo-05-estadomoderno.json": [
        "Hacia 1940, los países latinoamericanos eran casi irreconocibles en comparación con las caóticas repúblicas del siglo anterior.",
        "El viejo caudillismo personalista dio paso a una burocracia civil organizada, y el estado logró sostenerse con leyes estables.",
        "En un proceso paralelo, la idea de la patria dejó de ser un concepto abstracto y se convirtió en un servicio concreto de salud y caminos.",
        "A pesar de sus avances, muchos estados seguían teniendo un andamiaje frágil que no podía depender de un plan improvisado.",
        "Sin embargo, la presencia del estado nacional quedó firmemente asentada como árbitro de la economía y la sociedad."
    ],
    "b1-nacionalismo.json": [
        "En las décadas de 1920 y 1930, América Latina fortaleció las capacidades burocráticas y fiscales de sus estados nacionales.",
        "El nacionalismo cultural exaltó el pasado indígena y la identidad popular a través del muralismo, la literatura y la música.",
        "Campañas de alfabetización masiva llevaron la educación pública a comunidades rurales aisladas de todo el continente.",
        "El estado amplió su presencia mediante censos, recaudación impositiva directa y servicios públicos de salud y transporte.",
        "Estas reformas consolidaron instituciones modernas que sustituyeron al viejo poder informal de los caudillos locales."
    ],

    # =========================================================================
    # UNIT 18: grandepresion
    # =========================================================================
    "b1-grandepresion-01-crisis1929.json": [
        "Nueva York, octubre de 1929. El desplome de la bolsa de Wall Street desata una ola de pánico financiero en todo el planeta.",
        "El precio de cada acción bancaria se derrumbó en pocas horas y miles de inversores lo perdieron absolutamente todo.",
        "La gente corrió a los bancos para retirar sus ahorros antes de que declararan la quiebra definitiva.",
        "El cierre masivo de industrias dejó a millones de obreros desempleados en las principales potencias industriales.",
        "Esta catástrofe económica internacional no tardó en agravar la situación de los países exportadores de América Latina."
    ],
    "b1-grandepresion-02-americalatina.json": [
        "La Gran Depresión expuso de golpe la tremenda vulnerabilidad del modelo económico agroexportador latinoamericano.",
        "Los mercados de Europa y Estados Unidos dejaron de comprar café, cobre, azúcar y carne al instante.",
        "El valor de las exportaciones comenzó a desplomarse con una magnitud devastadora para las finanzas públicas.",
        "Los bancos extranjeros cortaron de raíz los préstamos y se negaron a prestar más dinero a los gobiernos de la región.",
        "Sin ingresos en el presupuesto, muchos presidentes se vieron forzados a anunciar la suspensión del pago de la deuda externa."
    ],
    "b1-grandepresion-03-menoscomercio.json": [
        "Entre 1929 y 1932, el volumen del comercio internacional sufrió una contracción dramática y sin precedentes.",
        "Las pérdidas económicas vinieron a coincidir con el cierre de las minas en Chile y los campos de café en Brasil.",
        "El desplome de las ventas llegó a traducirse en un desempleo severo que golpeó drásticamente a la clase trabajadora.",
        "A pesar del enorme esfuerzo de los gobiernos, la crisis arruinó a las familias recién llegadas a las ciudades.",
        "La crisis mundial demostró con crudeza que el continente no podía seguir dependiendo de la venta de un solo producto."
    ],
    "b1-grandepresion-04-cambiarmodelo.json": [
        "Ante la falta de divisas para comprar en el extranjero, los líderes tuvieron que plantearse una alternativa radical.",
        "Nació así el modelo de sustitución de importaciones: si no podíamos comprar manufacturas afuera, había que fabricar adentro.",
        "Los estados levantaron una sólida barrera y un nuevo arancel aduanero para proteger a las nuevas industrias nacionales.",
        "El gobierno asumió el control de sectores estratégicos, dando un giro decisivo y aplicando un duro ajuste económico general.",
        "Este nuevo modelo industrial transformó para siempre la estructura productiva de toda América Latina."
    ],
    "b1-grandepresion-05-transformoregion.json": [
        "La crisis económica de 1929 representó un auténtico punto de inflexión en la historia contemporánea de América Latina.",
        "La estabilidad de los gobiernos colgaba de un hilo delgado ante la indignación popular y las huelgas masivas.",
        "Los líderes comprendieron que no bastaba con apelar a viejas promesas ante un colapso que no era pasajero.",
        "Para superar el punto de quiebre, las naciones necesitaron un nuevo tipo de liderazgo político e industrial.",
        "De las cenizas de la Gran Depresión nació la era del populismo y de una fuerte intervención estatal en la economía."
    ],
    "b1-grandepresion.json": [
        "El colapso financiero de Wall Street en 1929 provocó la caída inmediata de los precios y de la demanda de exportaciones latinoamericanas.",
        "La interrupción de créditos internacionales obligó a casi todos los países a suspender el pago de sus deudas externas.",
        "El desempleo masivo y la caída de ingresos fiscales causaron una ola de golpes de estado e inestabilidad política en 1930.",
        "Para enfrentar la emergencia, los gobiernos adoptaron el modelo de industrialización por sustitución de importaciones.",
        "La Gran Depresión marcó el fin del modelo oligárquico tradicional y aceleró la intervención estatal en la economía y la sociedad."
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

    print(f"Total Block 3 stories successfully re-authored: {updated}/36")

if __name__ == "__main__":
    update_stories()
