#!/usr/bin/env python3
"""Re-author Latin America Track Block 5 (Units 25-30, 36 files).

Units:
25. represionpolitica (unit story: b1-represion-politica.json)
26. centroamerica
27. conosur
28. crisisdeuda
29. neoliberalismo
30. democratizacion

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
    # UNIT 25: represionpolitica
    # =========================================================================
    "b1-represionpolitica-01-elestadorepresivo.json": [
        "Buenos Aires, 1976. La junta militar declara un estado de sitio permanente para suspender toda garantía constitucional.",
        "Las patrullas nocturnas comienzan a vigilar cada esquina y a detener a ciudadanos sin orden judicial previa.",
        "El régimen militar convierte cada viejo cuartel y garaje en un centro clandestino de tortura y exterminio.",
        "Un sofisticado aparato represivo estatal persigue sin tregua a cualquier disidente político considerado peligroso.",
        "El terror se instala en el silencio temeroso de una sociedad paralizada por el miedo cotidiano."
    ],
    "b1-represionpolitica-02-censurraypersecucion.json": [
        "Para controlar el pensamiento público, los militares decidieron prohibir cientos de libros, canciones y obras de teatro.",
        "Los censores llegaron a quemar montañas de literatura universal en hogueras públicas frente a las universidades.",
        "La dictadura decidió expulsar a profesores sospechosos y quitar el empleo público a todo opositor ideológico.",
        "La vigilancia constante de los servicios secretos obligó a miles de intelectuales a partir a un amargo exilio.",
        "A pesar del peligro mortal, muchas voces valientes lograron denunciar las violaciones de derechos humanos desde el extranjero."
    ],
    "b1-represionpolitica-03-desaparecidos.json": [
        "En la oscuridad de la noche, bandas armadas solían secuestrar a jóvenes militantes en sus propias casas.",
        "Las autoridades militares decidieron negar los hechos y hacer desaparecer cualquier rastro del paradero de las víctimas.",
        "Frente a la Casa Rosada, un grupo de madres valientes comenzó a exigir justicia y noticias de sus hijos secuestrados.",
        "Llevaban sobre la cabeza un pañuelo blanco bordado que se transformó en el símbolo inmortal de la resistencia moral.",
        "Años más tarde, los tribunales democráticos lograron procesar a los generales culpables ante la mirada del mundo entero."
    ],
    "b1-represionpolitica-04-resistencia.json": [
        "La lucha por los derechos humanos exigió un esfuerzo titánico de abogados, sacerdotes y familiares de las víctimas.",
        "A pesar de las amenazas, los activistas lograron documentar cada crimen clandestino y fundar comités de solidaridad internacional.",
        "La sociedad descubrió que la represión no apuntaba solo al guerrillero armado, sino a todo pensamiento crítico y social.",
        "La voz de las víctimas rompió el cerco del silencio y obtuvo el reconocimiento unánime de las Naciones Unidas.",
        "Esta red de solidaridad salvó cientos de vidas y sentó las bases para el futuro juicio a los dictadores."
    ],
    "b1-represionpolitica-05-memoriayjusticia.json": [
        "Con la vuelta de la democracia, los tribunales pudieron condenar a las cúpulas militares por crímenes de lesa humanidad.",
        "Aunque los gobiernos intentaron aprobar leyes de perdón para limitar los juicios, el clamor popular no se detuvo.",
        "Años después, la justicia logró anular las leyes de impunidad y reabrir cada causa penal contra los represores.",
        "Cada testimonio desgarrador de los sobrevivientes sirvió para marcar la memoria colectiva con una consigna eterna: Nunca Más.",
        "La verdadera reconciliación nacional demostró que solo puede construirse sobre los cimientos firmes de la verdad y la justicia."
    ],
    "b1-represion-politica.json": [
        "Durante las décadas de 1970 y 1980, el cono sur vivió la era más oscura del terrorismo de estado y la represión militar.",
        "Las juntas militares disolvieron los derechos constitucionales, persiguieron a la oposición e hicieron desaparecer a miles de personas.",
        "Organizaciones heroicas como las Madres de Plaza de Mayo desafiaron la censura y la muerte para exigir la aparición de sus hijos.",
        "La solidaridad internacional y la documentación clandestina permitieron romper el cerco de impunidad de los dictadores.",
        "El juicio histórico a las juntas y la anulación de las leyes de amnistía convirtieron a la región en un referente mundial de memoria y justicia."
    ],

    # =========================================================================
    # UNIT 26: centroamerica
    # =========================================================================
    "b1-centroamerica-01-nicaragua.json": [
        "Managua, julio de 1979. La dictadura de la dinastía Somoza llega a su fin tras medio siglo de tiranía.",
        "Un pueblo indignado por la corrupción y la miseria decidió apoyar la lucha armada del Frente Sandinista de Liberación Nacional.",
        "El general Anastasio Somoza tuvo que huir en avión y los comandantes guerrilleros entraron triunfantes a gobernar el país.",
        "La revolución lanzó una célebre campaña nacional de alfabetización que redujo el analfabetismo a niveles históricos en pocos meses.",
        "Los nuevos líderes prometieron asumir un régimen de pluralismo político y consolidar una economía mixta para todos."
    ],
    "b1-centroamerica-02-elsalvador.json": [
        "San Salvador, marzo de 1980. El arzobispo Óscar Arnulfo Romero celebra misa en la capilla de un hospital.",
        "El prelado suplicaba a los soldados no obedecer órdenes de matar a sus hermanos campesinos.",
        "Un certero disparo de un francotirador decidió asesinar al pastor frente al altar mayor de su capilla.",
        "La masacre obligó al pueblo a enfrentar a un ejército dispuesto a violar derechos y destruir cada aldea.",
        "Una estimación oficial calculó más de setenta mil muertos en doce años de cruenta guerra civil."
    ],
    "b1-centroamerica-03-guatemala.json": [
        "En las montañas boscosas de Guatemala, la guerra contrainsurgente llegó a prolongarse durante más de tres décadas sangrientas.",
        "Los generales aplicaron una salvaje doctrina militar de tierra arrasada contra la población indígena maya del altiplano.",
        "El ejército decidió cometer un mortífero genocidio que destruyó más de cuatrocientas comunidades campesinas ancestrales.",
        "La Comisión para el Esclarecimiento Histórico concluyó que el terrorismo estatal fue responsable de la inmensa mayoría de las masacres.",
        "La líder maya Rigoberta Menchú alzó su voz valiente ante el mundo, logrando un merecido y reconocido Premio Nobel de la Paz."
    ],
    "b1-centroamerica-04-intervencionyguerrafria.json": [
        "Durante la presidencia de Ronald Reagan, Washington decidió financiar y armar a los rebeldes de la Contra nicaragüense.",
        "La CIA organizó un plan secreto para entrenar a tropas irregulares y minar puertos civiles en Centroamérica.",
        "Cuando el Congreso norteamericano prohibió la ayuda militar, la Casa Blanca ideó un turbio desvío encubierto de dinero.",
        "El escándalo Irán-Contra reveló que el gobierno vendía armas a Teherán para proporcionar fondos ilegales a la guerrilla antisandinista.",
        "A pesar de los millones invertidos, la estrategia militar de derrocar por la fuerza al gobierno nicaragüense volvió a fallar."
    ],
    "b1-centroamerica-05-losacuerdosdepaz.json": [
        "A finales de los ochenta, los mandatarios decidieron reunirse para atravesar el camino hacia la reconciliación.",
        "Bajo la mediación diplomática regional, se acordó poner fin a una violencia que solía alimentar el odio.",
        "Los combatientes de cada bando aceptaron entregar las armas a cambio de plenas garantías democráticas.",
        "La región logró celebrar elecciones limpias y superar el bloqueo económico que asfixiaba a las comunidades.",
        "El legado de estos acuerdos demostró que la vía pacífica podía triunfar sobre los fusiles."
    ],
    "b1-centroamerica.json": [
        "En las décadas de 1970 y 1980, Centroamérica se convirtió en el epicentro de sangrientas guerras civiles y revoluciones populares.",
        "La Revolución sandinista derrocó a la dinastía Somoza en Nicaragua, provocando la intervención encubierta de Estados Unidos mediante la Contra.",
        "En El Salvador, el asesinato del arzobispo Romero desató un conflicto armado de doce años entre la guerrilla del FMLN y el ejército.",
        "En Guatemala, la política militar de tierra arrasada cometió actos de genocidio contra las comunidades indígenas mayas del altiplano.",
        "Los acuerdos de paz de Esquipulas permitieron desmovilizar a las guerrillas e iniciar una difícil transición hacia la democracia."
    ],

    # =========================================================================
    # UNIT 27: conosur
    # =========================================================================
    "b1-conosur-01-chile.json": [
        "Santiago de Chile, 1988. Augusto Pinochet decide convocar un plebiscito nacional para dirigir el país ocho años más.",
        "El general aspiraba a permanecer en el poder como comandante en jefe y mandatario vitalicio.",
        "La dictadura había logrado redactar una constitución a su medida para controlar las futuras instituciones civiles.",
        "Todos los pronósticos oficiales daban por seguro el triunfo del régimen a través del miedo.",
        "Pero la campaña del NO logró superar el terror y la ciudadanía votó para rechazar la dictadura militar."
    ],
    "b1-conosur-02-argentina.json": [
        "Buenos Aires, 1983. Tras el desastre de Malvinas, las crisis comenzaron a sucederse sin tregua.",
        "La situación social empezó a deteriorarse rápidamente bajo el gobierno de facto de los militares.",
        "El descontento popular logró desplazar a la cúpula castrense que pretendía mantener el control estatal.",
        "La sociedad exigía reemplazar a los generales y buscar una salida democrática a través del voto popular.",
        "Los partidos políticos construyeron un frente unificado que llevó a Raúl Alfonsín a la presidencia nacional."
    ],
    "b1-conosur-03-uruguay.json": [
        "En Uruguay, el autogolpe de 1973 impuso una feroz militarización en todas las instituciones públicas.",
        "El país llegó a registrar la tasa más alta de presos políticos de todo el continente sudamericano.",
        "Los generales intentaron someter la voluntad del pueblo convocando un plebiscito en 1980.",
        "La ciudadanía uruguaya desafió la censura y dio un inesperado y rotundo triunfo al voto negativo.",
        "La movilización pacífica logró culminar en 1985 con la liberación de los presos y el retorno democrático."
    ],
    "b1-conosur-04-operacioncondor.json": [
        "En 1975, los jefes de inteligencia de varias dictaduras del cono sur decidieron reunirse en Santiago.",
        "Varios países acordaron sumarse a una red secreta y coordinarse para perseguir a los disidentes exiliados.",
        "Los comandos lograban localizar a los opositores refugiados en el extranjero con ayuda policial encubierta.",
        "Muchos activistas fueron llevados a una comisaría secreta para luego partir con rumbo y destino desconocido.",
        "Años después, los célebres Archivos del Terror lograron probar la existencia de este plan de exterminio."
    ],
    "b1-conosur-05-democraciaymemoria.json": [
        "El retorno de las libertades civiles abrió un singular debate ético sobre la memoria y la verdad.",
        "Cada gobierno creó una comisión nacional para investigar a cada ciudadano torturado o ejecutado.",
        "La sociedad civil exigió ampliar las investigaciones para no dejar ningún crimen estatal en la oscuridad.",
        "Con los años, los tribunales decidieron declarar nulas las amnistías y ratificar los tratados de derechos humanos.",
        "Esta decisión permitió la reapertura de cada juicio penal contra los comandantes y torturadores militares."
    ],
    "b1-conosur.json": [
        "En la década de 1980, las dictaduras del cono sur comenzaron a colapsar bajo el peso del desastre económico y la protesta social.",
        "Argentina inauguró la transición democrática con el histórico Juicio a las Juntas Militares presidido por Raúl Alfonsín en 1985.",
        "En Uruguay y Chile, movilizaciones masivas y victorias electorales en plebiscitos obligaron a los militares a entregar el poder.",
        "La revelación de los crímenes coordinados bajo el Plan Cóndor expuso el carácter transnacional del terrorismo de estado en la región.",
        "Pese a los pactos de impunidad iniciales, las comisiones de la verdad y los juicios penales consolidaron la cultura de los derechos humanos."
    ],

    # =========================================================================
    # UNIT 28: crisisdeuda
    # =========================================================================
    "b1-crisisdeuda-01-ladeudacrece.json": [
        "Durante los años setenta, los bancos internacionales buscaron colocar miles de millones de petrodólares.",
        "Las entidades financieras decidieron otorgar créditos con gran facilidad a las dictaduras y gobiernos de la región.",
        "Los países comenzaron a acumular préstamos para depositar recursos en grandes obras y destinar fondos a cuarteles.",
        "El valor de la deuda comenzó a multiplicarse debido al incremento del tipo de interés bancario internacional.",
        "Este endeudamiento masivo dejó al continente sumamente expuesto a cualquier cambio en la economía mundial."
    ],
    "b1-crisisdeuda-02-lacrisisde1982.json": [
        "Agosto de 1982. El ministro de México debe anunciar que su país no puede cumplir los pagos de la deuda.",
        "Washington había decidido elevar las tasas de interés, provocando que los compromisos financieros volvieran a dispararse.",
        "El gobierno mexicano tuvo que reconocer la bancarrota inminente ante la falta total de reservas en dólares.",
        "Los analistas salieron a señalar que el pánico financiero no tardaría en extenderse por todo el continente.",
        "La suspensión de pagos cerró el crédito internacional y desató la peor tormenta económica de la historia moderna."
    ],
    "b1-crisisdeuda-03-austeridad.json": [
        "Para evitar la quiebra del sistema bancario mundial, los gobiernos tuvieron que recurrir al Fondo Monetario Internacional.",
        "El FMI impuso programas de ajuste estructural que exigían un severo recorte del gasto social y de la inversión pública.",
        "Los presidentes tuvieron que devaluar la moneda nacional, eliminar los subsidios a los alimentos básicos y subir los impuestos.",
        "Los economistas solían argumentar que el sacrificio era indispensable para restaurar la disciplina fiscal y la confianza externa.",
        "Sin embargo, las condiciones impuestas por los acreedores extranjeros desataron una profunda crisis de soberanía nacional."
    ],
    "b1-crisisdeuda-04-elcostesocial.json": [
        "El impacto social de los programas de austeridad fue devastador para las clases trabajadoras y medias de toda la región.",
        "La hiperinflación comenzó a erosionar el poder adquisitivo del salario y el desempleo formal alcanzó cifras récord.",
        "Millones de familias tuvieron que volcarse al comercio ambulante e informal para asegurar el pan cotidiano de sus hijos.",
        "En febrero de 1989, el aumento del transporte desató en Caracas una ola masiva de disturbios y saqueos conocida como el Caracazo.",
        "La violenta represión militar en las calles caraqueñas demostró que la paciencia popular ante el ajuste había llegado a su límite."
    ],
    "b1-crisisdeuda-05-unadecadaperdida.json": [
        "Los economistas de la CEPAL decidieron referirse a los años ochenta con una expresión trágica: la década perdida de América Latina.",
        "Una década entera de crisis logró borrar los avances sociales y el crecimiento del ingreso logrado en los años anteriores.",
        "El estancamiento económico crónico solo comenzó a ceder a fines de la década mediante el Plan Brady de renegociación de bonos.",
        "Los países pudieron canjear su vieja deuda bancaria por nuevos bonos garantizados por el tesoro norteamericano.",
        "América Latina cerró una etapa traumática para entrar de lleno en la era de las reformas de libre mercado y las privatizaciones."
    ],
    "b1-crisisdeuda.json": [
        "La crisis de la deuda externa estalló en 1982 cuando México anunció su incapacidad de pagar los intereses a los bancos internacionales.",
        "El brusco aumento de las tasas de interés en Estados Unidos cerró el crédito barato e hizo impagable el endeudamiento acumulado.",
        "Programas de austeridad dictados por el FMI provocaron devaluaciones masivas, hiperinflación y recortes brutales en el gasto social.",
        "El deterioro del poder adquisitivo desató estallidos sociales como el Caracazo en 1989, exponiendo el límite humano del ajuste.",
        "La década perdida de los ochenta frenó el desarrollo regional y abrió el camino a las reformas estructurales del Consenso de Washington."
    ],

    # =========================================================================
    # UNIT 29: neoliberalismo
    # =========================================================================
    "b1-neoliberalismo-01-lasideasneoliberales.json": [
        "Washington, 1989. El economista John Williamson decide acuñar el término de Consenso de Washington para resumir las nuevas recetas económicas.",
        "Frente al agotamiento del viejo modelo estatal, los tecnócratas propusieron adoptar el libre mercado como el único camino al progreso.",
        "El nuevo credo exigía una estricta disciplina fiscal, una reforma del sistema tributario y la desregulación total del comercio.",
        "Los gobiernos debían reducir el gasto público y promover la eficiencia privada para atraer capitales extranjeros a la región.",
        "La receta prometía superar el atraso, pero implicaba desmantelar las conquistas laborales y sociales de medio siglo anterior."
    ],
    "b1-neoliberalismo-02-privatizacion.json": [
        "En los años noventa, una ola de reformas llevó a privatizar la mayoría de las empresas estatales.",
        "Los gobiernos decidieron vender servicios de telefonía, luz, agua y cada aerolínea que antes se decidió nacionalizar.",
        "Los tecnócratas denunciaban la corrupción de los funcionarios y la ineficiente gestión de las burocracias públicas.",
        "Se afirmaba que el estado tenía un aparato sobredimensionado y una plantilla de trabajadores excesivamente costosa.",
        "La venta atrajo a cada inversor extranjero, pero miles de empleados públicos perdieron su puesto de trabajo."
    ],
    "b1-neoliberalismo-03-elmercadoyelestado.json": [
        "El nuevo paradigma económico retiró al estado de su papel histórico como motor del desarrollo nacional y la producción.",
        "Se redujo drásticamente el arancel aduanero para abrir las fronteras a la competencia de los productos importados.",
        "El banco central obtuvo su plena independencia técnica para controlar la emisión monetaria y frenar la inflación.",
        "Los tecnócratas creían con fervor ciego en el incentivo del mercado libre y en la iniciativa de cada propietario privado.",
        "La desconfianza hacia la planificación pública se convirtió en la norma incuestionable de toda la política económica oficial."
    ],
    "b1-neoliberalismo-04-desigualdadypobreza.json": [
        "Las reformas lograron domar la hiperinflación y retomar el crecimiento económico en los primeros años de la década de 1990.",
        "Pero la riqueza generada no logró traducirse en un reparto justo ni en un mayor bienestar para toda la población.",
        "El coeficiente de Gini se disparó, situando a América Latina como la región más desigual y con menor equidad del planeta.",
        "El trabajo formal y justamente remunerado escaseaba, empujando a millones de jóvenes al empleo precario y la informalidad.",
        "El descontento social comenzó a crecer en los barrios pobres ante la falta de oportunidades y el deterioro de la educación pública."
    ],
    "b1-neoliberalismo-05-ellegadoneoliberal.json": [
        "A finales de los años noventa, las reformas que lograron domar la inflación revelaron una gran fragilidad.",
        "En Argentina, la decisión de fijar el tipo de cambio un peso por dólar impuso una extrema rigidez económica.",
        "Esta política provocó el colapso financiero de 2001, obligando al presidente a huir en medio de disturbios.",
        "Los economistas reconocieron una falla de diseño estructural cuando la recesión comenzó a asolar a la población.",
        "El ciclo neoliberal cerró con la certeza de que el mercado no solucionaba la miseria y el hambre social."
    ],
    "b1-neoliberalismo.json": [
        "En los años noventa, el Consenso de Washington transformó la economía de América Latina mediante reformas neoliberales profundas.",
        "Se privatizaron masivamente empresas públicas de servicios, telecomunicaciones y transporte para atraer inversión extranjera.",
        "La apertura comercial y la disciplina fiscal lograron domar la inflación, pero desindustrializaron ramas enteras de la producción nacional.",
        "Las reformas aumentaron la desigualdad social y la precariedad laboral, situando a la región con la peor distribución de la riqueza mundial.",
        "El colapso de la convertibilidad argentina en 2001 expuso los límites del modelo y abrió la puerta al giro político hacia la izquierda."
    ],

    # =========================================================================
    # UNIT 30: democratizacion
    # =========================================================================
    "b1-democratizacion-01-volveravotar.json": [
        "El retorno a las urnas fue una de las fiestas cívicas más emotivas en la historia moderna de América Latina.",
        "Tras años de dictaduras, millones de ciudadanos acudieron con orgullo a elegir libremente a sus nuevas autoridades en elecciones limpias.",
        "La transición democrática se logró negociar en medio de un contexto económico adverso heredado de las juntas militares.",
        "Los nuevos mandatarios tuvieron que enfrentar presiones armadas de cuarteles que pretendían conservar su viejo poder interno.",
        "A pesar de los temores de un nuevo golpe, la ciudadanía demostró un compromiso inquebrantable con la defensa de las instituciones."
    ],
    "b1-democratizacion-02-nuevasinstituciones.json": [
        "Para consolidar las nuevas libertades, varios países decidieron convocar a una asamblea constituyente.",
        "Los delegados lograron redactar y promulgar nuevas leyes para modernizar el sistema judicial y administrativo.",
        "Se buscó diseñar un marco institucional sólido que pudiera perdurar más allá de los gobiernos de turno.",
        "Los legisladores debatieron con firmeza sobre la reelección del presidente y los controles al poder ejecutivo.",
        "El objetivo principal consistía en frenar la tentación autoritaria y garantizar la división efectiva de los poderes del estado."
    ],
    "b1-democratizacion-03-democraciayjusticia.json": [
        "Los mandos militares pretendían mantener su poder intacto y exigían un indulto o perdón recíproco a la sociedad.",
        "Bajo amenazas de rebelión castrense, algunos congresos mantuvieron vigente una legislación de impunidad.",
        "Sin embargo, la sociedad civil consideró totalmente incompatible perdonar crímenes atroces sin conocer la verdad.",
        "Los organismos de derechos humanos mantuvieron la demanda popular de un juicio y procesamiento penal justo.",
        "Décadas de lucha permitieron anular las amnistías y dictar una sentencia condenatoria contra los genocidas."
    ],
    "b1-democratizacion-04-lasdificultadesdelatransicion.json": [
        "Los generales no aceptaban huir al exilio ni retirar a sus tropas sin asegurarse una total inmunidad.",
        "En Chile, el general Pinochet usó las normas militares para designar senadores y condicionar al parlamento.",
        "Los nuevos mandatarios tenían muy escaso margen presupuestario debido al déficit económico acumulado.",
        "El descontento social creció con rapidez frente al rechazo ciudadano ante la falta de reformas sociales inmediatas.",
        "A pesar del poder que conservaban los cuarteles, la democracia logró ganar terreno paso a paso."
    ],
    "b1-democratizacion-05-democraciasimperfectas.json": [
        "Al comenzar el nuevo siglo, las instituciones democráticas aún no lograban desarrollarse plenamente en la región.",
        "Cada encuesta de opinión revelaba una alarmante pérdida de confianza en el congreso y los partidos políticos.",
        "La incapacidad de resolver la pobreza obligaba a la ciudadanía a cargar con el peso del desempleo.",
        "Esta crisis social amenazaba con debilitar a los gobiernos y acortar el mandato de varios presidentes electos.",
        "Los líderes tuvieron que proponer reformas profundas para reconstruir la base de apoyo popular de sus administraciones."
    ],
    "b1-democratizacion.json": [
        "Entre 1980 y 2000, América Latina completó una histórica transición desde dictaduras militares hacia regímenes democráticos constitucionales.",
        "Los nuevos gobiernos aprobaron constituciones garantistas y reconstruyeron los poderes judiciales para defender los derechos ciudadanos.",
        "El conflicto entre la demanda de justicia por los crímenes del pasado y las amenazas militares marcó los primeros años de la transición.",
        "Aunque el voto popular se consolidó de forma pacífica, la corrupción y la desigualdad mantuvieron un alto nivel de descontento social.",
        "Al comenzar el siglo veintiuno, las democracias de la región enfrentaban el desafío de combinar libertad política con justicia social."
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

    print(f"\nTotal Block 5 stories successfully re-authored: {updated}/36")

if __name__ == "__main__":
    update_stories()
