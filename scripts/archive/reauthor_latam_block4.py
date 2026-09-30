#!/usr/bin/env python3
"""Re-author Latin America Track Block 4 (Units 19-24, 36 files).

Units:
19. populismo
20. industrializacion
21. revolucioncubana
22. guerrafria
23. eeuu
24. gobiernosmilitares

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
    # UNIT 19: populismo
    # =========================================================================
    "b1-populismo-01-quees.json": [
        "Buenos Aires, 1945. La multitud llena la Plaza de Mayo para aclamar a su líder en un fervor nunca visto.",
        "Un líder carismático sabe conectar con las emociones populares mediante un discurso apasionado y directo.",
        "Los críticos conservadores lo tildan de político oportunista que intenta saltarse las instituciones democráticas.",
        "El presidente busca deslegitimar a la vieja oligarquía extranjerizante que sirve a intereses foráneos.",
        "Este estilo influyente se convirtió en el rasgo característico de la política latinoamericana del siglo veinte."
    ],
    "b1-populismo-02-peron.json": [
        "Juan Domingo Perón era un hábil coronel del ejército que supo ganarse el corazón del trabajador sindicalizado.",
        "Cuando sus rivales intentaron apartar al militar del poder, el pueblo decidió movilizarse masivamente el diecisiete de octubre.",
        "La multitud exigió su inmediata liberación, marcando el nacimiento triunfal del movimiento peronista.",
        "A su lado brillaba Eva Perón, impulsando la ayuda social a los descamisados a través de su fundación benéfica.",
        "La muerte prematuro o temprana de Evita sumió a millones de argentinos en un profundo y doloroso duelo nacional."
    ],
    "b1-populismo-03-cardenas.json": [
        "En México, el presidente Lázaro Cárdenas ofrecía un estilo político muy diferente: sobrio, austero y discreto.",
        "Rechazó el culto a la personalidad y prefirió viajar en tren para escuchar directamente al campesinado humilde.",
        "En 1938 tomó una decisión histórica: expropiar a las compañías petroleras extranjeras para recuperar la soberanía nacional.",
        "Las potencias imperiales amenazaron con sanciones, pero Cárdenas no llegó a temer sus represalias económicas.",
        "A pesar de discrepar con algunos empresarios, su presidencia dejó una huella imborrable en el México contemporáneo."
    ],
    "b1-populismo-04-puebloylider.json": [
        "El populismo clásico construyó un poderoso vínculo emocional directo entre el líder supremo y la masa popular.",
        "Este contacto directo solía debilitar a los partidos tradicionales y eliminar a todo intermediario político habitual.",
        "Para los juristas liberales, la falta de una clara rendición de cuentas resultaba un síntoma sospechoso y preocupante.",
        "La oposición sospechaba que las leyes solo buscaban favorecer a los votantes leales y reducir la influencia opositora.",
        "Los partidarios celebraban que las reformas lograran devolver la dignidad y los derechos a la clase trabajadora."
    ],
    "b1-populismo-05-legado.json": [
        "Hoy en día, el debate sobre el populismo latinoamericano sigue despertando intensas pasiones entre los historiadores.",
        "Nadie puede negar el genuino reconocimiento histórico que estos movimientos otorgaron a millones de obreros marginados.",
        "Los analistas intentan procesar cada particularidad nacional sin pintar al gobernante como un santo o un villano.",
        "Un análisis matizado comprende que estos regímenes supieron negociar con las demandas de su propio tiempo histórico.",
        "Los movimientos políticos actuales siguen considerándose un heredero orgulloso de aquella época de conquistas populares."
    ],
    "b1-populismo.json": [
        "A mediados del siglo veinte, el populismo emergió como una fuerza política decisiva en toda América Latina.",
        "Líderes carismáticos como Juan Domingo Perón en Argentina y Lázaro Cárdenas en México movilizaron a las masas obreras y campesinas.",
        "Estos gobiernos ampliaron los derechos laborales, nacionalizaron recursos estratégicos y promovieron la industria nacional.",
        "Aunque fueron criticados por autoritarios y personalistas, otorgaron reconocimiento y dignidad a sectores históricamente postergados.",
        "La herencia del populismo continúa siendo un referente central en las identidades y debates políticos de la región."
    ],

    # =========================================================================
    # UNIT 20: industrializacion
    # =========================================================================
    "b1-industrializacion-01-producirencasa.json": [
        "Durante la Segunda Guerra Mundial, el comercio internacional de mercancías pacíficas quedó paralizado por completo.",
        "Cada potencia industrial tuvo que volcar toda su maquinaria fabril en el esfuerzo bélico militar.",
        "América Latina no podía importar bienes de consumo, sufriendo un desabastecimiento forzado y repentino.",
        "Lo que comenzó como una respuesta forzada ante una crisis coyuntural terminó por profundizar la industrialización nacional.",
        "Los gobiernos abandonaron su tímido apoyo inicial y decidieron promover fábricas nacionales con créditos baratos."
    ],
    "b1-industrializacion-02-nuevasindustrias.json": [
        "Medellín, São Paulo y Monterrey se transformaron en vibrantes motores de la nueva industria pesada continental.",
        "Los presidentes acudían orgullosos a inaugurar la primera gran acería nacional y modernas plantas textiles.",
        "El estado asumió un modelo mixto con fuerte respaldo público para financiar la producción de acero y energía eléctrica.",
        "Pronto comenzaron a fabricar cada electrodoméstico doméstico y a crear talleres de ensamblaje de automóviles.",
        "Estas fábricas lograron ilustrar el orgullo de naciones decididas a producir con sus propias manos."
    ],
    "b1-industrializacion-03-migracion.json": [
        "El crecimiento vertiginoso de las fábricas urbanas desató una gigantesca ola migratoria desde el campo a la ciudad.",
        "Cada habitante rural que buscaba empleo llegaba a capitales que no estaban preparadas para este cambio demográfico.",
        "La falta de vivienda adecuada y de agua potable obligó a las familias a levantar chozas en colinas y pantanos.",
        "Nació así el nuevo asentamiento informal: la barriada en Lima, la villa miseria en Buenos Aires o la favela en Río.",
        "Este crecimiento urbano abrupto transformó para siempre el paisaje social y geográfico de las grandes metrópolis."
    ],
    "b1-industrializacion-04-sociedadesurbanas.json": [
        "La llegada masiva de campesinos a la ciudad alteró por completo el mercado laboral y la cultura popular urbana.",
        "Muchos obreros lograron incorporarse como trabajador asalariado con sueldo fijo en la industria manufacturera formal.",
        "Pero una gran multitud quedó en el sector ambulante, atrapado en la economía informal para alimentar a sus familias.",
        "Surgió una incipiente clase media que buscaba reorganizar su vida y cumplir la aspiración del ascenso social.",
        "A pesar del peso heredado de la pobreza, la metrópoli moderna ofrecía escuelas y oportunidades desconocidas en el campo."
    ],
    "b1-industrializacion-05-continenteindustrial.json": [
        "Hacia 1970, América Latina podía exhibir un impresionante logro en su proceso de desarrollo productivo.",
        "Un sector manufacturero ya consolidado producía bienes de consumo a pesar de la persistente pobreza en el campo.",
        "Sin embargo, el progreso técnico creció de forma desproporcionadamente desigual en favor de las grandes capitales.",
        "Muchos gobiernos cometieron el error de confiar ciegamente en préstamos extranjeros baratos para tapar sus déficits.",
        "La enorme deuda externa acumulada dejó el camino sembrado de peligros financieros para las siguientes décadas."
    ],
    "b1-industrializacion.json": [
        "El modelo de sustitución de importaciones impulsó la creación de acerías, refinerías y fábricas manufactureras en toda la región.",
        "El crecimiento fabril atrajo a millones de campesinos a las ciudades, transformando a América Latina en un continente urbano.",
        "Surgieron enormes barriadas y favelas ante la incapacidad estatal de proveer vivienda y servicios de agua potable a tiempo.",
        "Nacieron sindicatos combativos y una clase media que exigió mayor participación política y educación universitaria.",
        "Pese a los logros industriales, los déficits fiscales y el endeudamiento externo prepararon el terreno para futuras crisis."
    ],

    # =========================================================================
    # UNIT 21: revolucioncubana
    # =========================================================================
    "b1-revolucioncubana-01-cubaantes.json": [
        "La Habana, 1955. La capital cubana brilla bajo las luces de los hoteles de lujo, los casinos y el juego nocturno.",
        "La economía de la isla dependía absolutamente de la cuota azucarera vendida al mercado de Estados Unidos.",
        "Aunque el ingreso per cápita cubano era alto para la época, el desempleo azotaba al campesino al terminar la zafra.",
        "La corrupción del régimen militar de Fulgencio Batista era un hecho notorio que indignaba a la juventud educada.",
        "El dictador se volvió cada vez más impopular por censurar a la prensa y reprimir violentamente toda protesta pacífica."
    ],
    "b1-revolucioncubana-02-fidelcastro.json": [
        "El veintiséis de julio de 1953, un grupo de jóvenes intentó asaltar el cuartel Moncada para derrocar a Batista.",
        "La audaz operación militar resultó un intento suicida que terminó por fracasar con decenas de combatientes muertos.",
        "Fidel Castro fue capturado, pero tras ser amnistiado partió a México para preparar una nueva expedición libertadora.",
        "En 1956, el pequeño yate Granma logró desembarcar en las costas orientales con ochenta y dos guerrilleros a bordo.",
        "Un puñado de sobrevivientes subió a la Sierra Maestra para combatir contra el desprestigiado ejército de la dictadura."
    ],
    "b1-revolucioncubana-03-socialista.json": [
        "Primero de enero de 1959. Batista huye cobardemente en avión y los barbudos entran triunfantes en La Habana.",
        "El nuevo gobierno revolucionario aprobó la reforma agraria y estuvo dispuesto a expropiar cada gran ingenio azucarero sin pagar compensación.",
        "Cuando Washington impuso una dura sanción comercial, Cuba comenzó a nacionalizar cada refinería de petróleo norteamericana.",
        "La Unión Soviética ofreció suministrar combustible barato y comprar todo el azúcar cubano a precios preferenciales.",
        "En 1961, Fidel Castro declaró el carácter socialista de la revolución, desafiando abiertamente al bloque occidental."
    ],
    "b1-revolucioncubana-04-bahiacochinos.json": [
        "Abril de 1961. La CIA decidió entrenar a una brigada armada de exiliados cubanos para invadir la isla caribeña.",
        "La invasión de Bahía de Cochinos buscaba provocar un levantamiento popular inmediato para derrocar al régimen revolucionario.",
        "Sin embargo, el ejército cubano y las milicias populares lograron derrotar a los invasores en menos de setenta y dos horas.",
        "Fue una victoria humillante para el presidente Kennedy y elevó el prestigio político de la revolución en todo el mundo.",
        "Poco después, la crisis de los misiles en 1962 llevó a la superpotencia soviética y a Estados Unidos a una peligrosa negociación."
    ],
    "b1-revolucioncubana-05-cubayamericalatina.json": [
        "El triunfo cubano logró encender la imaginación de miles de jóvenes revolucionarios en toda América Latina.",
        "El Che Guevara decidió promover la teoría del foco guerrillero para multiplicar la insurrección en las selvas andinas.",
        "Muchos movimientos armados nacieron inspirados por la hazaña de los guerrilleros de la Sierra Maestra.",
        "Washington respondió logrando que Cuba fuera expulsado de la OEA e imponiendo un estricto aislamiento sobre la isla.",
        "La sombra de la revolución se proyectó sobre el continente, vista por unos como esperanza y por otros como una amenaza mortal."
    ],
    "b1-revolucioncubana.json": [
        "En 1959, la Revolución cubana derrocó la corrupta dictadura de Fulgencio Batista, transformando la geopolítica del continente.",
        "Las expropiaciones de tierras y empresas estadounidenses llevaron a la confrontación directa con el gobierno de Washington.",
        "Tras derrotar la invasión de Bahía de Cochinos en 1961, Cuba se declaró socialista y se alió estrechamente con la Unión Soviética.",
        "La crisis de los misiles de 1962 colocó al mundo al borde de una guerra nuclear entre las dos superpotencias de la época.",
        "El ejemplo cubano inspiró guerrillas armadas en toda la región, desatando una era de polarización ideológica y violencia política."
    ],

    # =========================================================================
    # UNIT 22: guerrafria
    # =========================================================================
    "b1-guerrafria-01-dosbloques.json": [
        "Tras la Segunda Guerra Mundial, el planeta quedó como un mundo enfrentado entre dos bloques irreconciliables.",
        "Cada superpotencia defendía una doctrina opuesta: el libre mercado frente al comunismo planificado.",
        "Cada bando forjó una alianza militar y se lanzó a una desenfrenada carrera armamentística con un temible arsenal nuclear.",
        "América Latina se convirtió en un escenario activo de la disputa global entre Washington y Moscú.",
        "Cualquier conflicto interno de la región quedó condicionado por la lógica implacable de la rivalidad este-oeste."
    ],
    "b1-guerrafria-02-americalatina.json": [
        "Las élites miraban temerosamente cualquier protesta y Washington decidió lanzar una ofensiva política continental.",
        "Para mantener a raya al comunismo, el gobierno estadounidense exigió a cada país receptor alinearse con sus directivas.",
        "Cada mandatario tuvo que implementar medidas de seguridad y comprometer sus recursos en la lucha antisoviética.",
        "Cualquier intento de cambio social profundo corría el riesgo de ser calificado como una amenaza castrista.",
        "La ayuda económica prometida llegó condicionada a la subordinación militar de las fuerzas armadas locales."
    ],
    "b1-guerrafria-03-revolucionoanticomunismo.json": [
        "La sociedad latinoamericana se polarizó de forma extrema entre la revolución social y el anticomunismo armado.",
        "Miles de estudiantes y cada activista sindical comenzaron a empujar reformas democráticas profundas en la calle.",
        "En las universidades y la academia se debatían apasionadamente las teorías del imperialismo y la liberación nacional.",
        "Las élites oligárquicas decidieron respaldar a los militares para bloquear cualquier conflicto interno que amenazara sus privilegios.",
        "El ejército adoptó una doctrina de guerra preventiva contra sus propios ciudadanos considerados enemigos del estado."
    ],
    "b1-guerrafria-04-intervencionextranjera.json": [
        "En 1954, Guatemala tenía un presidente constitucional que intentó devolver tierras baldías a los campesinos pobres.",
        "Un vecino poderoso como Estados Unidos consideró que esto amenazaba su esfera de influencia geopolítica.",
        "La CIA decidió proporcionar armas a mercenarios para derrocar a Árbenz y restaurar el viejo orden oligárquico.",
        "Fue una clara jugada en el tablero internacional para advertir a otros mandatarios que la autodeterminación tenía límites estrictos.",
        "La soberanía popular latinoamericana quedó subordinada a los intereses estratégicos de las corporaciones de Washington."
    ],
    "b1-guerrafria-05-continentedividido.json": [
        "Hacia 1970, la Guerra Fría llegó a reproducir su violencia en cada ámbito de la sociedad latinoamericana.",
        "El estado militar comenzó a redefinir la seguridad nacional persiguiendo a cada sindicato y partido opositor.",
        "El continente tuvo que atravesar un período doloroso de dictaduras sangrientas y persecuciones sistemáticas.",
        "Al repasar aquellos años, la sociedad comprende que la represión llegó a tocar a miles de familias inocentes.",
        "La Guerra Fría en América Latina no fue fría en absoluto; fue un conflicto sangriento que costó miles de vidas humanas."
    ],
    "b1-guerrafria.json": [
        "La Guerra Fría polarizó a América Latina en un tablero de confrontación ideológica entre Estados Unidos y la Unión Soviética.",
        "Washington impulsó doctrinas de seguridad nacional para contener cualquier intento de reforma social considerado procomunista.",
        "Intervenciones clandestinas de la CIA, como el golpe contra Árbenz en Guatemala en 1954, frenaron procesos democráticos reformistas.",
        "Sindicatos, partidos de izquierda y movimientos estudiantiles fueron reprimidos con creciente dureza militar en toda la región.",
        "La polarización geopolítica canceló los espacios democráticos, abriendo la puerta a dictaduras militares en el cono sur y Centroamérica."
    ],

    # =========================================================================
    # UNIT 23: eeuu
    # =========================================================================
    "b1-eeuu-01-vecinodelnorte.json": [
        "En 1823, el presidente James Monroe decidió formular una célebre advertencia diplomática: América para los americanos.",
        "La doctrina pretendía oponerse a cualquier intento de las monarquías europeas de reconquistar sus antiguas colonias.",
        "Con el paso del tiempo, esta política llegó a transformarse en una justificación del dominio de Washington sobre el continente.",
        "La enorme asimetría de poder militar y económico impidió que el vecino del norte y el del sur negociaran mutuamente en igualdad.",
        "América Latina se convirtió en el mercado natural de las inversiones y productos manufacturados de Estados Unidos."
    ],
    "b1-eeuu-02-intervenciones.json": [
        "A principios del siglo veinte, el presidente Theodore Roosevelt formuló su famoso corolario a la Doctrina Monroe.",
        "Estados Unidos se arrogaba el derecho de actuar como policía internacional si un país se mostraba incapaz de pagar sus deudas.",
        "Tropas de marines desembarcaron repetidamente para ocupar puertos y tomar el control de cada aduana en el Caribe.",
        "En Nicaragua, el general Augusto C. Sandino encabezó una guerrilla heroica contra las tropas ocupantes norteamericanas.",
        "Un siglo después de independizarse de España, este combate fue decisivo para despertar la conciencia antiimperialista en toda la región."
    ],
    "b1-eeuu-03-economiaydependencia.json": [
        "A través de la diplomacia del dólar, las compañías norteamericanas pasaron a dominar sectores estratégicos de la economía regional.",
        "La inversión de capital estadounidense controlaba el negocio bananero en Centroamérica y el sector minero en Chile y Perú.",
        "Las multinacionales solían fijar el precio de compra en el mercado mundial, reduciendo las ganancias de los productores locales.",
        "Muchos gobiernos debían garantizar el pago de cada préstamo bancario externo antes que atender las necesidades de su propio ciudadano.",
        "La riqueza salía del continente hacia los bancos de Nueva York, consolidando un patrón estructural de dependencia económica."
    ],
    "b1-eeuu-04-alianzaparaelprogreso.json": [
        "Tras el triunfo de la Revolución cubana, el presidente John F. Kennedy propuso una nueva estrategia para el continente.",
        "En 1961 nació la Alianza para el Progreso con la meta de aportar ayuda económica millonaria a América Latina.",
        "El plan buscaba construir escuelas, mejorar la vivienda y aumentar el ingreso de cada habitante rural empobrecido.",
        "El objetivo era absorber el descontento popular para disminuir la simpatía hacia la guerrilla socialista en un plan sin precedente.",
        "Sin embargo, la ayuda se desvió a burocracias ineficientes y el proyecto terminó por disolverse tras el asesinato de Kennedy."
    ],
    "b1-eeuu-05-unarelacioncompleja.json": [
        "Hoy en día, la relación entre Estados Unidos y América Latina abarca mucho más que acuerdos políticos o disputas militares.",
        "Millones de migrantes latinoamericanos deciden cruzar la frontera norte cada año buscando trabajo y bienestar familiar.",
        "El constante turismo y las remesas logran circular dinero e ideas, manteniendo un destino entrelazado entre ambas sociedades.",
        "Un análisis matizado comprende que las dos regiones comparten un vínculo cultural que late al margen de los discursos oficiales.",
        "Lejos de simplificaciones, el destino de las Américas sigue construyéndose a través de este diálogo complejo y permanente."
    ],
    "b1-eeuu-latinoamerica.json": [
        "Las relaciones entre Estados Unidos y América Latina han estado marcadas por una profunda asimetría de poder geopolítico.",
        "A través del Corolario Roosevelt y la diplomacia del cañonero, tropas estadounidenses intervinieron repetidamente en el Caribe.",
        "Las corporaciones multinacionales norteamericanas dominaron enclaves agrícolas y mineros decisivos en toda la región.",
        "Iniciativas como la Alianza para el Progreso combinaron ayuda al desarrollo económico con estrategias de seguridad anticomunista.",
        "Hoy en día, la migración masiva, el comercio y el intercambio cultural entrelazan el destino de ambos lados del continente."
    ],

    # =========================================================================
    # UNIT 24: gobiernosmilitares
    # =========================================================================
    "b1-gobiernosmilitares-01-losgolpesdeestado.json": [
        "En las décadas de 1960 y 1970, una ola de violencia autoritaria arrasó con las democracias de América Latina.",
        "Las fuerzas armadas recurrieron al golpe de Estado para derrocar presidentes electos e instalar una dictadura represiva.",
        "El politólogo Guillermo O'Donnell acuñó el término de estado burocrático-autoritario para describir a estos nuevos regímenes.",
        "Los generales contaron con el respaldo activo de élites empresariales para censurar a la prensa y disolver todo sindicato.",
        "Un equipo de tecnócratas civiles asumió el manejo de la economía para imponer planes de ajuste y apertura comercial."
    ],
    "b1-gobiernosmilitares-02-brasil.json": [
        "Río de Janeiro, marzo de 1964. Los tanques militares marchan sobre la capital para derrocar al presidente João Goulart.",
        "Los golpistas decidieron acusar al mandatario electo de simpatías comunistas por su intento de reforma agraria y fiscal.",
        "El régimen militar comenzó a gobernar mediante el decreto autoritario conocido como Acta Institucional Número Cinco para suspender garantías.",
        "El gobierno procedió a restringir los derechos constitucionales, imponer una estricta censura y atraer capital extranjero.",
        "A pesar del crecimiento económico, la dictadura dejó un saldo terrible de torturas antes de la gradual apertura y la amnistía final."
    ],
    "b1-gobiernosmilitares-03-chile.json": [
        "Santiago de Chile, once de septiembre de 1973. Aviones de combate deciden bombardear el Palacio de La Moneda.",
        "El presidente Salvador Allende murió en su puesto defendiendo el mandato democrático que le había otorgado el pueblo.",
        "El general Augusto Pinochet asumió el mando supremo de la junta militar para combatir a toda la izquierda chilena.",
        "Alegando frenar la inestabilidad política, desató una feroz persecución contra cada opositor en centros clandestinos.",
        "El controvertido manejo económico de los Chicago Boys desmanteló el estado social para imponer un modelo neoliberal radical."
    ],
    "b1-gobiernosmilitares-04-argentina.json": [
        "Buenos Aires, marzo de 1976. Las tres armas deciden encabezar un golpe para derrocar al débil gobierno civil de Isabel Perón.",
        "La dictadura militar comenzó a impulsar el terrorismo de estado con miles de secuestros ilegales y desapariciones forzadas.",
        "El plan económico provocó un gigantesco endeudamiento externo y una acelerada desindustrialización del aparato productivo nacional.",
        "En 1982, en un intento desesperado por ganar popularidad, el régimen decidió invadir las islas Malvinas contra el Reino Unido.",
        "La aplastante derrota militar precipitó el colapso definitivo de la dictadura y obligó a convocar a elecciones democráticas."
    ],
    "b1-gobiernosmilitares-05-elpodermilitar.json": [
        "Las dictaduras militares del cono sur llegaron a compartir una misma visión represiva: la doctrina de seguridad nacional.",
        "Los generales decidieron optar por la violencia clandestina durante un mando casi ininterrumpido en el continente.",
        "Sin embargo, los regímenes no lograron sostenerse sin legitimidad cuando la crisis económica provocó una enorme presión popular.",
        "El retorno a la democracia fue un proceso abrupto que devolvió la legitimidad a las urnas y a la soberanía ciudadana.",
        "La memoria de las víctimas y la búsqueda incansable de justicia siguen siendo el mayor imperativo moral de toda la región."
    ],
    "b1-gobiernosmilitares.json": [
        "Entre 1964 y 1985, dictaduras militares de seguridad nacional derrocaron gobiernos democráticos en la mayor parte de Sudamérica.",
        "En Brasil, Chile, Argentina y Uruguay, las juntas armadas disolvieron parlamentos y prohibieron las actividades sindicales.",
        "El terrorismo de estado utilizó secuestros clandestinos, tortura y desapariciones forzadas para aniquilar a la oposición política.",
        "Equipos de tecnócratas civiles aplicaron programas de ajuste neoliberal que aumentaron la deuda externa y la pobreza social.",
        "Las crisis económicas y la movilización popular por los derechos humanos precipitaron la caída de los regímenes castrenses."
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

    print(f"\nTotal Block 4 stories successfully re-authored: {updated}/36")

if __name__ == "__main__":
    update_stories()
