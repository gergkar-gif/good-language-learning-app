"""
Generates rich, detailed narrative stories for Block 3 (Units 13-18, 30 lessons).
Embeds every grammar sentence directly from reqs JSON to ensure 100% verbatim accuracy.
"""

import json
import os

reqs = json.load(open('scripts/block3_all_reqs.json', encoding='utf-8'))

# Helper to get the exact grammar sentences for a lesson
def G(lesson_key, idx):
    return reqs[lesson_key]['grammar_sentences'][idx]

STORIES = {}

# =============================================================================
# UNIT 13: economiasexportacion
# =============================================================================

# 13.01: economiasexportacion-01
k = "economiasexportacion-01"
# Grammar (8):
# 0: El comercio se volvió más libre que antes, pero la región siguió exportando sobre todo materias primas.
# 1: Esta especialización resultó mucho más rentable que cualquier intento anterior de desarrollar una industria local diversificada.
# 2: El modelo exportador resultaba, comparado con la economía colonial, mucho más dinámico en términos de ingresos totales.
# 3: Cuanto más dependía un país de un solo producto, más expuesto quedaba a cualquier caída repentina de su precio.
# 4: Durante la segunda mitad del siglo diecinueve, América Latina se integró plenamente en la economía global.
# 5: La demanda internacional de materias primas impulsó el crecimiento de las exportaciones.
# 6: Las inversiones extranjeras financiaron puertos y ferrocarriles para facilitar el comercio.
# 7: El modelo agroexportador transformó profundamente la vida social y económica de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El auge del modelo agroexportador",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Entre 1870 y 1914, la economía mundial experimentó una aceleración sin precedentes impulsada por la Segunda Revolución Industrial en Gran Bretaña, Alemania y Estados Unidos. {G(k, 4)} Las fábricas europeas demandaban minerales, caucho y fibras a gran escala, mientras sus crecientes poblaciones urbanas requerían cereales, café y carnes congeladas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 1)} Gobiernos liberales en Argentina, Brasil, Chile y México eliminaron antiguos monopolios y abrieron sus aduanas, atrayendo capitales británicos y estadounidenses que redefinieron el mapa productivo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} En las pampas argentinas, millones de hectáreas fueron sembradas de trigo y maíz, al tiempo que en el estado de São Paulo los cafetales avanzaban sobre las selvas tropicales con una fuerza arrolladora."
        },
        {
            "type": "narration",
            "text": f"Las élites oligárquicas acumularon fortunas fabulosas, construyendo palacetes de estilo parisino y teatros de ópera en Buenos Aires y Río de Janeiro. {G(k, 6)} Sin embargo, este esquema de inserción internacional entrañaba una fragilidad extrema. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} Aunque generó una modernización deslumbrante en puertos y capitales, consolidó una dependencia estructural respecto a las potencias del Atlántico Norte que condicionaría las crisis políticas del siglo veinte."
        }
    ]
}

# 13.02: economiasexportacion-02
k = "economiasexportacion-02"
# Grammar (8):
# 0: Los productos que tenían demanda internacional podían generar ingresos importantes.
# 1: Cuando aumentaba la demanda, los productores ampliaban la producción.
# 2: Si los precios bajaban, los ingresos de los productores podían disminuir.
# 3: La materia prima que se exportaba dependía de las condiciones del mercado internacional.
# 4: Los países latinoamericanos exportaban materias primas que necesitaban las economías industriales.
# 5: El café era el producto principal en varios países de la región.
# 6: El salitre y el cobre fueron minerales que impulsaron la economía chilena.
# 7: La carne y los cereales eran los productos que más se exportaban desde el Río de la Plata.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Monocultivos y enclaves: el mapa de las materias primas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A finales del siglo diecinueve, cada república latinoamericana quedó encasillada en la exportación de uno o dos bienes primarios. {G(k, 4)} {G(k, 0)} Esta especialización productiva determinó la prosperidad fiscal de los Estados y el destino cotidiano de millones de trabajadores rurales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} En Brasil, Colombia y varios países centroamericanos, el grano aromático representaba más de la mitad del valor exportado. {G(k, 1)} Los hacendados talaban bosques vírgenes y contrataban legiones de jornaleros e inmigrantes para multiplicar los cafetales."
        },
        {
            "type": "narration",
            "text": f"En el Pacífico sur, tras la Guerra del Pacífico (1879-1884), la riqueza minera reconfiguró las finanzas públicas. {G(k, 6)} En las desoladas 'oficinas salitreras' del desierto de Atacama, decenas de miles de obreros extraían el 'oro blanco' que fertilizaba los campos europeos y suministraba nitratos para la industria química."
        },
        {
            "type": "narration",
            "text": f"En el extremo meridional del continente, los barcos frigoríficos revolucionaron el comercio ultramarino. {G(k, 7)} Mientras tanto, en el Caribe y Centroamérica, gigantescas corporaciones extranjeras como la United Fruit Company establecieron enclaves bananeros autónomos que controlaban ferrocarriles, puertos y plantaciones."
        },
        {
            "type": "narration",
            "text": f"Esta prosperidad descansaba sobre bases sumamente precarias. {G(k, 2)} {G(k, 3)} Cualquier recesión en Londres o Nueva York bastaba para paralizar puertos enteros y desatar el desempleo masivo."
        }
    ]
}

# 13.03: economiasexportacion-03
k = "economiasexportacion-03"
# Grammar (8):
# 0: Aunque resulte tentador imaginar los ferrocarriles como simples símbolos de progreso nacional, la mayoría fueron construidos por empresas extranjeras.
# 1: Aunque estas empresas generaran empleo local, buena parte de sus ganancias salía directamente del país.
# 2: Su influencia se extendía incluso sobre la política chilena, aunque nunca ocupara ningún cargo oficial en el gobierno.
# 3: Los puertos se expandieron enormemente, aunque su función principal siguiera siendo la salida de materias primas.
# 4: Para transportar estas mercancías de manera eficiente, se construyeron redes ferroviarias extensas.
# 5: La mayor parte de estas infraestructuras se financió con capital británico.
# 6: Se instalaron líneas de telégrafo que conectaban las zonas de producción con los centros urbanos.
# 7: Los puertos fueron modernizados para permitir la llegada de barcos de mayor tamaño.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Ferrocarriles, capital británico y puertos modernos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El vertiginoso auge agroexportador requirió una colosal transformación técnica en el transporte y las comunicaciones. {G(k, 4)} {G(k, 6)} Entre 1880 y 1910, la red férrea de Argentina pasó de 2.500 a más de 30.000 kilómetros, mientras en México el Porfiriato tendió casi 20.000 kilómetros de vías."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 5)} Banqueros y contratistas de Londres financiaron locomotoras, rieles, muelles y compañías de gas, obteniendo concesiones estatales con ganancias mínimas garantizadas por ley."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} En el norte de Chile, magnates extranjeros como John Thomas North, el célebre 'Rey del Salitre', dominaron los ferrocarriles salitreros, el agua potable y los bancos. {G(k, 2)} North utilizó su inmensa riqueza para influir en ministros y parlamentarios durante las crisis institucionales de 1891."
        },
        {
            "type": "narration",
            "text": f"El trazado de las vías férreas dibujaba un claro patrón en abanico que conectaba el interior productivo directamente con el océano. {G(k, 7)} En Buenos Aires se construyó Puerto Madero con dársenas de hormigón y grúas a vapor, mientras el puerto de Santos en Brasil procesaba millones de sacos de café."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Esta portentosa infraestructura modernizó las costas y facilitó la extracción masiva de recursos, pero dejó a las regiones interiores desconectadas entre sí y subordinadas a las rutas del comercio marítimo."
        }
    ]
}

# 13.04: economiasexportacion-04
k = "economiasexportacion-04"
# Grammar (8):
# 0: Aunque las exportaciones generaban riqueza, los beneficios no siempre se distribuían de manera igual.
# 1: Los grandes propietarios podían obtener beneficios mientras los trabajadores recibían ingresos menores.
# 2: Como consecuencia de la concentración de la tierra, aumentó la desigualdad en algunas regiones.
# 3: El crecimiento económico no significaba necesariamente una distribución igual de la riqueza.
# 4: Varios países habían concentrado su producción en un solo producto antes de que llegara la crisis de precios.
# 5: Habían dependido de los préstamos británicos para financiar las grandes obras antes de que cambiaran las condiciones internacionales.
# 6: Muchos campesinos habían perdido el acceso a las tierras comunales antes de que el modelo alcanzara su apogeo.
# 7: Las economías locales habían abandonado la producción de alimentos básicos para dedicarse al monocultivo antes de que los precios cayeran en los mercados mundiales.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La fragilidad social del crecimiento hacia afuera",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Hacia principios del siglo veinte, los datos estadísticos mostraban un crecimiento macroeconómico sin igual en América Latina. {G(k, 0)} {G(k, 3)} La opulencia de las oligarquías terratenientes contrastaba de manera dramática con la precariedad de las mayorías campesinas y peonadas."
        },
        {
            "type": "narration",
            "text": f"La expansión de las haciendas se realizó a costa de las propiedades tradicionales de los pueblos originarios. {G(k, 6)} {G(k, 2)} En México, Morelos vio cómo las haciendas azucareras devoraban los pueblos campesinos, mientras en los Andes peruanos los latifundios ganaderos acaparaban pastizales comunales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} En las plantaciones de henequén de Yucatán y en los ingenios azucareros caribeños, los peones permanecían atados de por vida mediante deudas hereditarias en las tiendas de raya. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"En el plano macroeconómico, los gobiernos cayeron en trampas financieras peligrosas. {G(k, 4)} {G(k, 5)} Cuando los ingresos aduaneros fluctuaban, el pago del servicio de la deuda externa asfixiaba los presupuestos nacionales."
        },
        {
            "type": "narration",
            "text": f"Este modelo de 'crecimiento hacia afuera' generó profundas fracturas sociales. La concentración de la tierra, la pauperización rural y la vulnerabilidad financiera acumularon tensiones explosivas que desatarían violentas revoluciones en las décadas siguientes."
        }
    ]
}

# 13.05: economiasexportacion-05
k = "economiasexportacion-05"
# Grammar (8):
# 0: Si esos ingresos se hubieran invertido de manera sistemática en infraestructura, la historia económica del país habría sido muy distinta.
# 1: Si el Perú hubiera diversificado su economía durante estas décadas, habría estado mucho mejor preparado para lo que vino después.
# 2: Si esos sustitutos hubieran tardado unas décadas más en desarrollarse, es posible que Perú hubiera tenido más tiempo para adaptarse.
# 3: Si cualquiera de estos países hubiera dependido de dos o tres exportaciones, probablemente habría amortiguado mejor cada una de estas crisis.
# 4: El modelo exportador transformó la economía, pero también dejó una fuerte dependencia exterior.
# 5: La experiencia de estos años influyó en las políticas económicas posteriores.
# 6: El debate sobre el papel de las exportaciones continuó durante las décadas siguientes.
# 7: El modelo agroexportador fue fundamental para entender el desarrollo económico de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El ciclo del guano y las lecciones del monocultivo",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Para comprender los dilemas estructurales de América Latina, el caso del Perú en el siglo diecinueve ofrece una lección paradigmática. Entre 1840 y 1875, el Estado peruano exportó más de doce millones de toneladas de guano de las islas de Chincha hacia Europa, generando ingresos fiscales astronómicos. {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} En lugar de crear industrias manufactureras o agricultura tecnificada, la fabulosa renta guanera fue absorbida por la burocracia civil, la especulación financiera y la importación desmedida de bienes de lujo. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Hacia 1870, los yacimientos de guano de alta calidad comenzaron a agotarse y los científicos europeos sintetizaron fertilizantes químicos. {G(k, 2)} La bancarrota fiscal sobrevino en 1876 y dejó al país en una situación de indefensión financiera cuando estalló la Guerra del Pacífico en 1879."
        },
        {
            "type": "narration",
            "text": f"Patrones similares de euforia y colapso se repitieron con el auge del caucho en la Amazonía de Manaos e Iquitos, y más tarde con el salitre chileno. {G(k, 3)} La ilusión de riqueza fácil impidió el desarrollo de bases industriales autónomas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} {G(k, 5)} {G(k, 6)} Los economistas de mediados del siglo veinte recordarían amargamente estos ciclos para fundamentar la necesidad de una industrialización dirigida por el Estado."
        }
    ]
}

# =============================================================================
# UNIT 14: cambiosocial
# =============================================================================

# 14.01: cambiosocial-01
k = "cambiosocial-01"
# Grammar (8):
# 0: Buenos Aires era, según la describían sus propios habitantes, poco más que una "gran aldea".
# 1: No existía todavía un sistema de alcantarillado adecuado, y buena parte de la ciudad carecía de alumbrado público confiable.
# 2: Con la llegada masiva de migrantes, la ciudad creció a un ritmo que sus servicios básicos apenas podían soportar.
# 3: Esta transformación no solo cambió el aspecto de las ciudades, sino también la estructura misma de su sociedad.
# 4: El crecimiento de las ciudades aceleró la demanda de servicios públicos y transporte.
# 5: En muchas ciudades se construyeron avenidas amplias y edificios administrativos.
# 6: La expansión urbana transformó la vida cotidiana de las clases populares.
# 7: Las ciudades se convirtieron en centros de actividad política y social.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La gran explosión urbana y la metamorfosis de las capitales",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Hacia 1870, las capitales latinoamericanas conservaban todavía su fisonomía colonial de casas bajas y calles empedradas. {G(k, 0)} {G(k, 1)} Sin embargo, la vertiginosa inserción de la región en el comercio mundial desató un proceso de urbanización sin precedentes en la historia del continente."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} En Buenos Aires, Santiago, Río de Janeiro y la Ciudad de México, las élites gobernantes buscaron erradicar el pasado hispánico e imitar las reformas parisinas del barón Haussmann. {G(k, 5)} Se trazaron imponentes bulevares arbolados como la Avenida de Mayo y el Paseo de la Reforma, flanqueados por palacios de mármol y teatros de ópera."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Cientos de miles de inmigrantes ultramarinos y campesinos despojados se concentraron en las zonas céntricas y portuarias. En Buenos Aires y Montevideo proliferaron los conventillos, mientras en Río de Janeiro surgían los cortiços y las primeras favelas en los morros."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} El hacinamiento, la falta de agua potable y las epidemias de cólera y fiebre amarilla castigaron duramente a los barrios obreros, forzando a los higienistas y planificadores a impulsar obras de saneamiento y redes de tranvías eléctricos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 7)} Las urbes dejaron de ser simples mercados comarcales para convertirse en calderos sociales donde las nuevas clases populares comenzarían a disputar el poder político."
        }
    ]
}

# 14.02: cambiosocial-02
k = "cambiosocial-02"
# Grammar (8):
# 0: Se formó una clase media urbana que buscaba nuevas oportunidades profesionales.
# 1: Se concentraba una parte importante de la clase obrera en las ciudades industriales.
# 2: En algunos países se fortaleció la burguesía vinculada al comercio y a la industria.
# 3: Se produjeron cambios sociales a medida que crecían las ciudades.
# 4: La llegada de inmigrantes transformó la composición social de varias regiones.
# 5: Se organizaron sindicatos que defendían los intereses de los trabajadores.
# 6: Crecieron los sectores medios vinculados a la administración pública y la educación.
# 7: La sociedad se volvió más diversa y compleja durante este periodo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Inmigración masiva y surgimiento de las clases medias",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Entre 1880 y 1930, una inmensa corriente migratoria transformó la demografía de América Latina, concentrándose con especial intensidad en Argentina, Uruguay y el sur de Brasil. {G(k, 4)} Más de cuatro millones de italianos, españoles, portugueses, alemanes, sirio-libaneses y polacos cruzaron el Atlántico en busca de tierras y progreso."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} {G(k, 3)} {G(k, 0)} Hijos de inmigrantes y artesanos completaron estudios secundarios y universitarios, convirtiéndose en contadores, médicos, abogados, pequeños comerciantes y profesores."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Paralelamente, {G(k, 2)} Estos empresarios modernizadores chocaban a menudo con las rancias oligarquías agrarias que monopolizaban el crédito y las aduanas."
        },
        {
            "type": "narration",
            "text": f"Al mismo tiempo, {G(k, 1)} En frigoríficos de carne, talleres ferroviarios, hilanderías textiles y puertos, miles de obreros fabriles experimentaban jornadas agotadoras y pésimas condiciones de higiene. {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"La vieja sociedad estamental colonial de señores de la tierra y peones analfabetos se desintegró en las grandes metrópolis. Las emergentes clases medias y obreras comenzaron a organizarse en partidos reformistas, exigiendo sufragio universal y el fin del fraude electoral oligárquico."
        }
    ]
}

# 14.03: cambiosocial-03
k = "cambiosocial-03"
# Grammar (8):
# 0: La inmigración aumentó mientras las ciudades necesitaban más trabajadores.
# 1: Los migrantes llegaron buscando empleo y construyendo nuevos asentamientos.
# 2: Las huelgas se multiplicaron mientras los obreros exigían mejores salarios.
# 3: Los sindicatos crecieron organizando a los trabajadores de diferentes sectores.
# 4: La movilización obrera creció mientras las fábricas aumentaban su producción.
# 5: Durante estas décadas se consolidó un movimiento obrero con demandas claras.
# 6: Los trabajadores se organizaron para conseguir mejores condiciones de trabajo.
# 7: La cuestión social se convirtió en un tema central del debate público.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El nacimiento del movimiento obrero y la cuestión social",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A principios del siglo veinte, el vertiginoso crecimiento industrial generó un profundo malestar en las barriadas trabajadoras. {G(k, 0)} {G(k, 1)} Familias enteras vivían en cuartos húmedos y sin ventilación, carentes de cualquier tipo de cobertura médica o seguro ante accidentes laborales."
        },
        {
            "type": "narration",
            "text": f"Con los barcos inmigrantes llegaron también militantes anarquistas, socialistas y sindicalistas revolucionarios que traían en sus maletas folletos de Proudhon, Bakunin y Marx. {G(k, 5)} {G(k, 6)} Se fundaron sociedades de resistencia por oficio, bibliotecas populares y periódicos combativos como 'La Protesta' en Argentina."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} En 1901 se fundó la Federación Obrera Regional Argentina (FORA) y en Chile la Federación Obrera de Chile (FOCH). {G(k, 2)} {G(k, 4)} Los trabajadores paralizaron talleres mecánicos, minas de carbón y muelles exigiendo la jornada de ocho horas y el descanso dominical."
        },
        {
            "type": "narration",
            "text": f"Las oligarquías gobernantes respondieron inicialmente considerando las protestas como simples conspiraciones foráneas. {G(k, 7)} Gobiernos en Buenos Aires, Santiago y Río de Janeiro aprobaron leyes de residencia para expulsar a líderes anarquistas extranjeros, recurriendo al estado de sitio y la intervención policial."
        },
        {
            "type": "narration",
            "text": f"A pesar del hostigamiento policial, la organización obrera demostró una tenacidad inquebrantable. La clase trabajadora forjó una identidad solidaria que obligaría a las autoridades a abandonar el laissez-faire y promulgar las primeras leyes laborales del continente."
        }
    ]
}

# 14.04: cambiosocial-04
k = "cambiosocial-04"
# Grammar (8):
# 0: Estas ideas encontraron eco entre los trabajadores, hasta que se convirtieron en organización sindical concreta.
# 1: Esperaban allí, pacíficamente, hasta que el gobierno respondiera a sus peticiones.
# 2: El conflicto no hizo más que intensificarse antes de que terminara la década.
# 3: Nunca se estableció una cifra exacta antes de que el hecho quedara, durante décadas, prácticamente silenciado.
# 4: Las huelgas obreras desafiaron el orden establecido por las élites gobernantes.
# 5: La respuesta del Estado combinó la represión con las primeras leyes laborales.
# 6: Varios acontecimientos marcaron la historia del movimiento obrero en la región.
# 7: La lucha sindical logró importantes conquistas para los trabajadores.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Jornadas de lucha, huelgas generales y tragedias obreras",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El choque frontal entre las demandas proletarias y la intransigencia patronal desató dramáticos episodios de confrontación en todo el continente. {G(k, 0)} {G(k, 4)} {G(k, 6)} Las huelgas generales paralizaron ciudades enteras y desnudaron la complicidad de los Estados con los grandes consorcios."
        },
        {
            "type": "narration",
            "text": f"Uno de los hechos más luctuosos ocurrió en el norte de Chile en diciembre de 1907. Miles de mineros del salitre marcharon junto a sus esposas e hijos hacia la costa y se congregaron en la Escuela Santa María de Iquique. {G(k, 1)} En lugar de dialogar, las tropas del general Roberto Silva Renard abrieron fuego de ametralladora contra la multitud desarmada."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Cientos de obreros pampinos perecieron en la matanza de Santa María de Iquique. Una tragedia similar se repitió en Colombia en 1928 durante la Masacre de las Bananeras en Ciénaga, cuando el ejército disparó contra los trabajadores en huelga de la United Fruit Company."
        },
        {
            "type": "narration",
            "text": f"En Buenos Aires, durante enero de 1919, la represión de una huelga en los talleres metalúrgicos Vasena desembocó en la sangrienta 'Semana Trágica'. {G(k, 2)} Bandas de jóvenes de la élite formaron la 'Liga Patriótica' para cazar huelguistas y asaltar barrios obreros."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 7)} A costa de enormes sacrificios y mártires, las movilizaciones obreras conquistaron la regulación del trabajo de mujeres y menores, la indemnización por accidentes y la jornada legal de ocho horas."
        }
    ]
}

# 14.05: cambiosocial-05
k = "cambiosocial-05"
# Grammar (8):
# 0: América Latina no solo había transformado el aspecto de sus ciudades, sino también la propia composición de su población.
# 1: El movimiento no solo cuestionó a las autoridades locales, sino que generó una ola de solidaridad en otras universidades.
# 2: Las mujeres no solo participaron en las organizaciones obreras, sino que comenzaron a exigir derechos políticos propios.
# 3: Las tensiones sociales no solo provocaron huelgas y protestas, sino que obligaron al Estado a intervenir en las relaciones laborales.
# 4: Las transformaciones sociales de estas décadas cambiaron profundamente la región.
# 5: Nuevos actores sociales comenzaron a reclamar un papel más activo en la política.
# 6: La sociedad urbana se volvió más compleja y plural que en el siglo diecinueve.
# 7: Los cambios de este periodo sentaron las bases de las transformaciones políticas del siglo veinte.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Reforma Universitaria, el feminismo y la sociedad plural",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Hacia 1920, el panorama social de América Latina era irreconocible en comparación con el orden cerrado del siglo diecinueve. {G(k, 0)} {G(k, 4)} {G(k, 6)} La expansión educativa y la vida cívica crearon nuevas corrientes culturales de alcance continental."
        },
        {
            "type": "narration",
            "text": f"En junio de 1918 estalló en Argentina la histórica Reforma Universitaria de Córdoba, con su célebre 'Manifiesto Liminar' redactado por Deodoro Roca. Los estudiantes expulsaron a las camarillas clericales y exigieron cogobierno, autonomía universitaria y docencia libre. {G(k, 1)} El ideario reformista se expandió rápidamente por Lima, La Habana, Santiago y la Ciudad de México."
        },
        {
            "type": "narration",
            "text": f"En las fábricas textiles, escuelas y redacciones periodísticas, las mujeres rompieron las barreras tradicionales del hogar. {G(k, 2)} Pioneras como Alicia Moreau de Justo en Argentina, Paulina Luisi en Uruguay y Bertha Lutz en Brasil fundaron ligas feministas para conquistar el sufragio femenino y la igualdad civil."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 3)} Los ministerios de trabajo comenzaron a crearse para mediar en las negociaciones colectivas y reglamentar las cajas de jubilación obrera."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} La irrupción coordinada de obreros, estudiantes universitarios, sectores medios y movimientos de mujeres quebró definitivamente el monopolio de las oligarquías patricias, allanando el camino hacia la democratización masiva."
        }
    ]
}

# =============================================================================
# UNIT 15: revolucion
# =============================================================================

# 15.01: revolucion-01
k = "revolucion-01"
# Grammar (8):
# 0: Se ampliaron las demandas de participación social.
# 1: Se organizaron movimientos para transformar las instituciones políticas.
# 2: Se cuestionó la concentración de la tierra en pocas manos.
# 3: A raíz del conflicto, se propusieron reformas que cambiaron las instituciones.
# 4: No es lo mismo un simple cambio de gobernante que una revolución.
# 5: No es lo mismo derrocar a un presidente que transformar por completo la estructura social de un país.
# 6: Esta distinción entre revolución política y revolución social resulta fundamental.
# 7: No es lo mismo un nuevo presidente que un nuevo país.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El concepto de revolución en el siglo veinte",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante el siglo diecinueve, la historia política de América Latina estuvo plagada de asonadas militares, motines y pronunciamientos caudillistas. Sin embargo, al iniciarse el siglo veinte surgió un fenómeno cualitativamente distinto. {G(k, 4)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Mientras un golpe palaciego se limita a sustituir a una facción de la élite por otra sin alterar las relaciones económicas, una revolución social destruye el aparato del Estado anterior, redistribuye la propiedad y moviliza a millones de personas desposeídas. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"A medida que las contradicciones del modelo exportador y los regímenes dictatoriales se agudizaron, {G(k, 0)} {G(k, 1)} Las masas campesinas y proletarias dejaron de ser espectadores pasivos para reclamar voz en el destino nacional."
        },
        {
            "type": "narration",
            "text": f"En el centro de las convulsiones populares se situó la cuestión de la propiedad agraria y el control de los recursos estratégicos. {G(k, 2)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"El concepto de revolución se convirtió así en la brújula teórica y política de toda una época, inspirando a generaciones de dirigentes campesinos, líderes obreros e intelectuales comprometidos con la transformación profunda de sus sociedades."
        }
    ]
}

# 15.02: revolucion-02
k = "revolucion-02"
# Grammar (8):
# 0: Debido a que las leyes liberales de privatización habían despojado a muchas comunidades de sus tierras comunales, millones de personas se encontraron trabajando tierras que antes eran suyas.
# 1: A causa de que este despojo se repitió en prácticamente todos los países, la reivindicación de la tierra se convirtió en la demanda revolucionaria más extendida del continente.
# 2: En algunos países, este descontento permaneció contenido durante décadas, debido a que los gobiernos combinaban represión selectiva con concesiones menores.
# 3: La cuestión agraria fue uno de sus motores centrales, precisamente a causa de que esta tensión llevaba ya décadas acumulándose sin resolverse.
# 4: Se exigió una distribución más justa de la tierra.
# 5: Se cuestionaron los derechos de los grandes propietarios.
# 6: Se organizaron protestas en varias comunidades rurales.
# 7: Se reclamaron nuevas formas de propiedad agrícola.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La cuestión agraria y el clamor campesino",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En toda América Latina, el detonante principal de las mayores insurrecciones populares del siglo veinte no se originó en los salones urbanos, sino en los campos. {G(k, 0)} Las reformas liberales del siglo diecinueve habían abolido las tierras comunales e indígenas con el pretexto de crear propietarios modernos, pero en la práctica alimentaron latifundios colosales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 4)} {G(k, 7)} Desde los valles cañeros de Morelos en México hasta los altiplanos de Bolivia y Guatemala, las comunidades campesinas exigían la restitución de sus títulos ancestrales y el autogobierno comunal."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Las haciendas mantenían a los peones en servidumbre por deudas, apoyadas por guardias privadas y cuerpos de policía rural. {G(k, 5)} {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"Cuando las vías institucionales y los tribunales de justicia se cerraron sistemáticamente ante las demandas de los pueblos, la vía armada se tornó inevitable. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"El campesinado en armas aportó a los procesos revolucionarios una fuerza telúrica y una tenacidad moral incomparables, convirtiendo la consigna de 'Tierra y Libertad' en el grito de guerra más poderoso de la historia latinoamericana."
        }
    ]
}

# 15.03: revolucion-03
k = "revolucion-03"
# Grammar (8):
# 0: Los trabajadores protestaron, reclamando mejores salarios.
# 1: Los obreros se organizaron, formando sindicatos en las fábricas.
# 2: Los mineros participaron en huelgas, exigiendo mejores condiciones laborales.
# 3: Los trabajadores se movilizaron, defendiendo sus derechos laborales.
# 4: El movimiento obrero no logró articularse con el movimiento campesino sin que existieran profundas diferencias culturales entre ambos grupos.
# 5: Estos sindicatos organizaron huelgas generales de gran escala, sin que estos movimientos consiguieran aliarse de manera duradera con las demandas campesinas.
# 6: Esta separación no ocurrió sin que hubiera intentos genuinos de unirlos.
# 7: Ningún movimiento revolucionario logró triunfar de manera duradera sin que se produjera una alianza efectiva entre el descontento rural y el urbano.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Obreros, huelgas y el desafío de la alianza obrero-campesina",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Al compás de la industrialización temprana y la minería a gran escala, las ciudades y los enclaves extractivos vieron emerger una clase obrera combativa y disciplinada. {G(k, 0)} {G(k, 1)} {G(k, 3)} Talleres metalúrgicos, hilanderías y puertos se convirtieron en trincheras de agitación política."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} En las minas de Cananea en México, las salitreras chilenas y los campamentos petroleros venezolanos, las huelgas desafiaron a consorcios multinacionales que contaban con la complicidad directa de los ejércitos nacionales."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, la articulación entre el proletariado urbano y las masas campesinas tropezó con inmensos obstáculos. {G(k, 4)} Los obreros de las capitales a menudo desconfiaban de los ejércitos campesinos tradicionales, percibiéndolos erróneamente como fuerzas anárquicas o arcaicas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 6)} Dirigentes socialistas y líderes agrarios buscaron puentes de diálogo a través de periódicos obreros y asambleas populares, reconociendo que compartían un mismo enemigo en la oligarquía dominante."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} Allí donde prevaleció la división, las élites burguesas lograron neutralizar las insurrecciones por separado; pero donde obreros y campesinos unieron sus fuerzas, el viejo régimen resultó barrido de la historia."
        }
    ]
}

# 15.04: revolucion-04
k = "revolucion-04"
# Grammar (8):
# 0: El verdadero desafío comenzará después: construir un nuevo Estado capaz de gobernar un país profundamente fracturado.
# 1: Los movimientos revolucionarios exitosos tendrán que enfrentar preguntas que ninguna consigna previa a la victoria logra responder por sí sola.
# 2: La fase que sigue a una victoria revolucionaria será, con frecuencia, más violenta que la propia lucha por el poder.
# 3: Esta tensión explicará por qué tantos movimientos terminarán derivando hacia formas de gobierno alejadas de sus ideales fundacionales.
# 4: A raíz del triunfo revolucionario, se propusieron nuevas reformas institucionales.
# 5: Como consecuencia del conflicto, se redactó una nueva constitución.
# 6: Sin embargo, la transformación política fue gradual.
# 7: A lo largo del proceso, surgieron nuevos conflictos políticos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La toma del poder y el reto de construir el nuevo Estado",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Derrocar a una dictadura odiada y entrar triunfante en la capital constituye el clímax heroico de toda gesta insurreccional. No obstante, {G(k, 0)} {G(k, 1)} Una vez que el ejército enemigo es derrotado, la reconstrucción económica y el restablecimiento del orden plantean dilemas desgarradores."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Las distintas facciones de la coalición revolucionaria —ala moderada constitucionalista frente a sectores radicales campesinos y socialistas— entran con frecuencia en sangrientas guerras civiles por el rumbo del nuevo régimen. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} {G(k, 6)} La redacción de una carta magna permite plasmar los derechos sociales, pero su aplicación efectiva tropieza con la resistencia de terratenientes y la hostilidad de potencias extranjeras que amenazan con invasiones o bloqueos."
        },
        {
            "type": "narration",
            "text": f"Para defender las conquistas populares y centralizar el mando militar, los líderes triunfantes a menudo imponen una rígida disciplina partidaria y burocrática. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"Construir un Estado revolucionario requiere conciliar la soberanía popular originaria con la eficacia administrativa, un equilibrio precario que definiría las mayores victorias y las más dolorosas frustraciones del siglo veinte."
        }
    ]
}

# 15.05: revolucion-05
k = "revolucion-05"
# Grammar (8):
# 0: Se puede considerar que la revolución abrió nuevas posibilidades políticas.
# 1: Se puede afirmar que el proceso produjo cambios importantes.
# 2: Se puede interpretar que la revolución también generó violencia.
# 3: Se puede señalar que sus consecuencias fueron contradictorias.
# 4: Tanto la concentración extrema de la tierra como la existencia de un movimiento obrero organizado resultan condiciones casi siempre presentes.
# 5: Tanto los países con enorme desigualdad de tierra como los países con fuertes movimientos sindicales experimentaron décadas de tensión.
# 6: Lo que distingue un país donde estalla una revolución es tanto la debilidad del Estado como la capacidad de las fuerzas de oposición para actuar coordinadamente.
# 7: Con estas herramientas conceptuales -tanto la definición de revolución como sus precondiciones estructurales- estamos ya preparados para examinar el caso mexicano.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Precondiciones estructurales y debates sobre el cambio social",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Al estudiar los grandes estallidos sociales de América Latina, los historiadores y sociólogos analizan las precondiciones que convierten el descontento latente en una insurrección triunfante. {G(k, 4)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"Sin embargo, la desigualdad por sí sola no explica por qué estalla una revolución en un país específico y no en otro. {G(k, 6)} La incapacidad del régimen para cooptar a las clases medias y la ruptura interna de las fuerzas armadas resultan factores desencadenantes indispensables."
        },
        {
            "type": "narration",
            "text": f"La evaluación histórica de estos procesos genera encendidas controversias hasta el día de hoy. {G(k, 0)} {G(k, 1)} Millones de familias campesinas accedieron a la tierra y a la educación básica, al tiempo que se forjó una nueva identidad ciudadana."
        },
        {
            "type": "narration",
            "text": f"Por otro lado, {G(k, 2)} {G(k, 3)} El costo humano en guerras fratricidas, destrucción de infraestructura y consolidación de regímenes autoritarios forma parte insoslayable del balance histórico."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} El cataclismo revolucionario de 1910 en México ofrece el laboratorio más fascinante para observar estas dinámicas en toda su grandeza y complejidad."
        }
    ]
}

# =============================================================================
# UNIT 16: revolucionmexicana
# =============================================================================

# 16.01: revolucionmexicana-01
k = "revolucionmexicana-01"
# Grammar (7):
# 0: Durante el Porfiriato se ampliaron los ferrocarriles, aunque el poder político permaneció muy concentrado.
# 1: La modernización económica fue impulsada por inversiones que transformaron distintas regiones.
# 2: La reelección de Díaz permitió que su gobierno continuara durante décadas.
# 3: En 1910, Porfirio Díaz llevaba ya gobernando México, casi sin interrupción, treinta y cuatro años.
# 4: México llevaba décadas atrayendo inversión extranjera masiva y modernizando sus principales ciudades.
# 5: Este mismo periodo llevaba concentrando la propiedad de la tierra en muy pocas manos a una velocidad extraordinaria.
# 6: Esta combinación llevaba funcionando con éxito durante más de tres décadas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El ocaso del Porfiriato y las tensiones del Centenario",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} En septiembre de 1910, el dictador celebró el Centenario de la Independencia con fastuosas recepciones diplomáticas en la Ciudad de México, exhibiendo palacios de mármol y avenidas iluminadas ante emisarios de todo el mundo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 0)} {G(k, 1)} Capitales británicos y estadounidenses controlaban minas de plata en Sonora, pozos petroleros en Veracruz y extensas redes ferroviarias en el norte."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} El poder residía en una camarilla de ancianos tecnócratas conocidos como 'los Científicos', liderados por José Yves Limantour, quienes concebían el progreso como un asunto reservado a las élites ilustradas."
        },
        {
            "type": "narration",
            "text": f"Bajo esa fachada de opulencia, la realidad rural era aterradora. {G(k, 5)} Hacendados como los Terrazas en Chihuahua poseían millones de hectáreas, mientras los pueblos indígenas eran despojados y los yaquis deportados a campos de trabajo forzado en Yucatán."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} mediante el uso sistemático del ejército y la policía de rurales. Pero cuando el anciano dictador cumplió ochenta años, el orden porfirista se reveló incapaz de contener las presiones democráticas y el clamor campesino."
        }
    ]
}

# 16.02: revolucionmexicana-02
k = "revolucionmexicana-02"
# Grammar (7):
# 0: Madero denunció la falta de elecciones libres y llamó a la población a levantarse en armas.
# 1: Después de que Díaz cayó, continuaron los conflictos porque distintos grupos tenían objetivos diferentes.
# 2: Se inició una nueva etapa política, aunque las tensiones sociales no desaparecieron.
# 3: El Plan de San Luis Potosí pedía que el pueblo mexicano se levantara en armas el 20 de noviembre de 1910.
# 4: Madero exigía que se anularan las elecciones y que se convocaran nuevos comicios verdaderamente libres.
# 5: Ante el avance imparable de las fuerzas revolucionarias, Díaz pidió que se negociara su salida del poder.
# 6: El propio Madero pronto exigiría de sus antiguos aliados algo que muchos de ellos no estaban dispuestos a aceptar: paciencia.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La insurrección maderista y el derrocamiento del dictador",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En 1908, Porfirio Díaz afirmó en una entrevista con James Creelman que México estaba maduro para la alternancia democrática. Francisco I. Madero, un hacendado liberal y espiritista de Coahuila, fundó el Partido Nacional Antirreeleccionista y recorrió el país atrayendo multitudes bajo la consigna 'Sufragio Efectivo, No Reelección'."
        },
        {
            "type": "narration",
            "text": f"Tras ser encarcelado por el régimen durante las fraudulentas elecciones de 1910, Madero escapó a Texas y proclamó su manifiesto revolucionario. {G(k, 3)} {G(k, 4)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En Chihuahua, Pascual Orozco y Pancho Villa tomaron Ciudad Juárez, mientras en Morelos las partidas campesinas de Emiliano Zapata capturaban Cuautla. {G(k, 5)} En mayo de 1911 se firmaron los Tratados de Ciudad Juárez y Díaz partió al exilio en el vapor 'Ypiranga', advirtiendo premonitoriamente: 'Madero ha soltado al tigre; a ver si puede domarlo'."
        },
        {
            "type": "narration",
            "text": f"Madero asumió la presidencia en noviembre de 1911 en medio de un inmenso júbilo popular. {G(k, 2)} {G(k, 6)} Madero priorizó la legalidad institucional y mantuvo intactos al ejército federal porfirista y a los tribunales agrarios."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} La negativa de Madero a decretar el reparto agrario inmediato provocó la ruptura con los zapatistas, debilitando fatalmente a su gobierno frente a las conspiraciones conservadoras."
        }
    ]
}

# 16.03: revolucionmexicana-03
k = "revolucionmexicana-03"
# Grammar (7):
# 0: El hecho de que Madero no atendiera con suficiente urgencia la reforma agraria explica la ruptura casi inmediata con Zapata.
# 1: El hecho de que Zapata y Villa tuvieran objetivos y estilos tan distintos no impidió que, en 1914, ambos ejércitos ocuparan juntos la Ciudad de México.
# 2: El hecho de que esta alianza careciera de un programa político unificado explica por qué resultó tan efímera.
# 3: Tanto Zapata como Villa acabarían siendo asesinados, sin haber logrado nunca imponer plenamente su visión particular de la revolución.
# 4: Mientras avanzaban los ejércitos revolucionarios, cambiaban las alianzas políticas.
# 5: Zapata defendía el reparto agrario, mientras sus seguidores reclamaban cambios en la propiedad de la tierra.
# 6: Villa dirigía un ejército revolucionario que tenía una fuerte presencia en el norte.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Zapata, Villa y la guerra de facciones",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} En noviembre de 1911, Emiliano Zapata proclamó el Plan de Ayala, desconociendo a Madero y exigiendo la devolución inmediata de los campos comunales a los pueblos originarios. {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"En febrero de 1913, el general porfirista Victoriano Huerta perpetró un sangriento golpe de Estado durante la 'Decena Trágica', asesinando a Madero y al vicepresidente Pino Suárez. Para derrocar a Huerta, Venustiano Carranza convocó al Ejército Constitucionalista. {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La temible 'División del Norte' de Villa contaba con trenes blindados, hospitales móviles y caballería pesada, aplastando al ejército federal en la batalla de Torreón y la toma de Zacatecas en 1914."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} En diciembre de 1914, los caudillos populares se encontraron en Xochimilco y se fotografiaron en Palacio Nacional con Villa sentado en la silla presidencial. {G(k, 2)} Villa y Zapata no deseaban gobernar el Estado central y abandonaron la capital a sus destinos locales."
        },
        {
            "type": "narration",
            "text": f"El genio militar de Álvaro Obregón reorganizó al Ejército Constitucionalista y destrozó a la caballería villista en las batallas de Celaya (1915) empleando trincheras y ametralladoras. {G(k, 3)} Sin embargo, la sangre derramada por sus hombres forzó la inclusión irreversible de sus banderas en la nueva carta magna."
        }
    ]
}

# 16.04: revolucionmexicana-04
k = "revolucionmexicana-04"
# Grammar (7):
# 0: A raíz de la revolución, la Constitución incorporó demandas relacionadas con la tierra y el trabajo.
# 1: El artículo constitucional estableció derechos que podían utilizarse para impulsar reformas.
# 2: En el marco de la nueva etapa política, el Estado asumió nuevas responsabilidades sociales.
# 3: Lo que se redactó en la ciudad de Querétaro, en 1917, superó ampliamente cualquier expectativa moderada.
# 4: Lo que hizo verdaderamente radical a esta nueva constitución fueron dos artículos en particular.
# 5: Lo que distinguió a esta constitución de la mayoría de las constituciones liberales del siglo diecinueve fue su ambición social explícita.
# 6: Lo que hace de la Constitución de 1917 un documento tan estudiado, incluso un siglo después, es precisamente esa combinación.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Constitución de Querétaro de 1917: vanguardia jurídica mundial",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A finales de 1916, Venustiano Carranza convocó a un Congreso Constituyente en el Teatro Iturbide de la ciudad de Querétaro con el propósito original de reformar la constitución liberal de 1857. No obstante, los diputados 'jacobinos' radicales liderados por Francisco J. Múgica tomaron la iniciativa política. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 0)} {G(k, 2)} El texto consagró por primera vez en la historia del derecho universal las garantías sociales por encima del individualismo contractualista clásico."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} El histórico Artículo 27 declaró que la propiedad originaria de tierras, aguas y recursos del subsuelo correspondía a la Nación, facultando al Estado para fraccionar latifundios y restituir tierras ejidales a los pueblos. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Asimismo, el Artículo 123 consagró conquistas laborales insólitas para su época: jornada máxima de ocho horas, salario mínimo vital, prohibición del trabajo nocturno para mujeres y niños, descanso semanal y derecho inalienable a la huelga y a la sindicalización."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La Constitución de 1917 articuló el respeto a las libertades democráticas con una enérgica soberanía nacional sobre los recursos naturales, sentando el marco jurídico para las transformaciones que definirían el México del siglo veinte."
        }
    ]
}

# 16.05: revolucionmexicana-05
k = "revolucionmexicana-05"
# Grammar (7):
# 0: Se produjeron cambios institucionales importantes, aunque muchas demandas continuaron pendientes.
# 1: El legado revolucionario incluyó reformas que cambiaron la relación entre el Estado y la sociedad.
# 2: Se puede hablar de una reconstrucción política gradual, porque las transformaciones no ocurrieron de inmediato.
# 3: El legado institucional de esta revolución no fue tanto una transformación completa e inmediata de la sociedad como la creación de un partido político dominante.
# 4: El resultado no fue tanto una sociedad plenamente igualitaria como una estabilidad política notable.
# 5: México evitó el ciclo de golpes de Estado y dictaduras militares que sufrieron muchos de sus vecinos.
# 6: El legado de la Revolución mexicana no fue tanto un final feliz y definitivo como el comienzo de un experimento institucional único.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La institucionalización de la Revolución y el cardenismo",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Tras una década de violencia armada que costó la vida a más de un millón de personas, los gobiernos sonorenses de Álvaro Obregón y Plutarco Elías Calles emprendieron la pacificación del país. {G(k, 0)} {G(k, 2)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Para poner fin al caudillismo y dirimir las disputas sucesorias sin derramamiento de sangre, Calles fundó en 1929 el Partido Nacional Revolucionario (PNR). {G(k, 3)} Esta maquinaria política integró corporativamente a campesinos, obreros, militares y burócratas bajo la égida estatal."
        },
        {
            "type": "narration",
            "text": f"El apogeo de las reformas revolucionarias llegó con el general Lázaro Cárdenas (1934-1940). Cárdenas repartió más de veinte millones de hectáreas a comunidades ejidales en La Laguna y Yucatán, impulsó la educación socialista y decretó el 18 de marzo de 1938 la histórica expropiación de las compañías petroleras extranjeras fundando PEMEX."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Gracias a la fortaleza de sus instituciones corporativas y al relevo civil de presidentes cada seis años, {G(k, 5)} en América del Sur."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La Revolución forjó un Estado árbitro poderoso, una rica cultura nacionalista y una mitología popular que moldearon la identidad mexicana contemporánea."
        }
    ]
}

# =============================================================================
# UNIT 17: nacionalismo
# =============================================================================

# 17.01: nacionalismo-01
k = "nacionalismo-01"
# Grammar (7):
# 0: Durante este proceso se fortalecieron las instituciones, aunque la autoridad central no llegó a todas las regiones de la misma manera.
# 1: La administración estatal fue ampliada porque los gobiernos buscaban ejercer mayor autoridad.
# 2: Las instituciones fueron reorganizadas mientras cambiaban las relaciones entre el Estado y las regiones.
# 3: Los Estados latinoamericanos han emprendido un proceso de fortalecimiento institucional que contrasta con la debilidad crónica del siglo diecinueve.
# 4: Los gobiernos han profesionalizado sus ejércitos, sustituyendo las antiguas montoneras por fuerzas armadas nacionales.
# 5: Muchos gobiernos han creado, por primera vez, sistemas de recaudación de impuestos relativamente eficaces.
# 6: Este Estado ha dejado de limitarse a la capital para extenderse hacia el resto del territorio nacional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La forja del Estado centralizado y la profesionalización institucional",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A lo largo de las primeras décadas del siglo veinte, las repúblicas latinoamericanas superaron la fragmentación que había caracterizado su época posindependentista. {G(k, 3)} Las viejas disputas entre facciones provinciales dieron paso a un poder central cohesionado."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Misiones militares alemanas y francesas llegaron a Chile, Perú, Argentina y Bolivia para fundar academias de guerra y estados mayores profesionales, subordinando a los caudillos armados a la constitución nacional."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 2)} Se crearon ministerios especializados en fomento, agricultura, sanidad y educación pública, reclutando burocracias permanentes mediante concursos y carreras administrativas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 6)} Aduanas interiores fueron abolidas y se implementaron impuestos directos a la renta y al timbre fiscal para sostener los servicios públicos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} Aunque persistían bolsones de atraso en selvas y cordilleras remotas, los Estados latinoamericanos contaban ahora con la capacidad técnica y militar requerida para conducir el destino nacional."
        }
    ]
}

# 17.02: nacionalismo-02
k = "nacionalismo-02"
# Grammar (7):
# 0: A pesar de que la construcción de un Estado más fuerte podría parecer un asunto puramente administrativo, estuvo acompañada por un ambicioso proyecto cultural.
# 1: El indigenismo buscaba incorporar el pasado prehispánico a la identidad nacional, a pesar de que las comunidades indígenas vivas siguieran sufriendo pobreza extrema.
# 2: La Semana de Arte Moderno buscó, a pesar de las resistencias de los sectores más conservadores, definir una identidad artística genuinamente brasileña.
# 3: Esta paradoja -celebrar el pasado indígena a pesar de que se ignoraran las condiciones reales de los pueblos indígenas contemporáneos- resultaría cada vez más visible.
# 4: Se difundieron símbolos nacionales porque se buscaba construir una identidad compartida.
# 5: El patrimonio fue presentado como parte de una historia común, aunque existían distintas experiencias regionales.
# 6: Se puede interpretar el nacionalismo cultural como un proceso de selección y debate.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Nacionalismo cultural, indigenismo y vanguardias artísticas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} Intelectuales, poetas, músicos y pintores abandonaron la reverente copia de los cánones europeos decimonónicos para buscar las raíces vernáculas de sus pueblos. {G(k, 4)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"En los países andinos y en México surgió con fuerza la corriente indigenista. {G(k, 1)} En Perú, pensadores como José Carlos Mariátegui y Luis E. Valcárcel denunciaron el gamonalismo terrateniente y ensalzaron el ayllu comunal como raíz de la nacionalidad."
        },
        {
            "type": "narration",
            "text": f"En México, los muralistas Diego Rivera, David Alfaro Siqueiros y José Clemente Orozco pintaron los muros de palacios y escuelas públicas con la epopeya mestiza. {G(k, 3)} {G(k, 6)} mientras se construía una mitología estatal homogeneizadora."
        },
        {
            "type": "narration",
            "text": f"En Brasil, la ruptura vanguardista estalló en febrero de 1922 en el Teatro Municipal de São Paulo. {G(k, 2)} Artistas como Tarsila do Amaral, Anita Malfatti y Oswald de Andrade lanzaron el 'Manifiesto Antropófago', proponiendo deglutir las técnicas modernas europeas para reinventar el alma mestiza brasileña."
        },
        {
            "type": "narration",
            "text": f"Esta formidable eclosión artística y literaria dotó a América Latina de un lenguaje estético propio y rebelde, proclamando ante el mundo la dignidad cultural de sus pueblos originarios y mestizos."
        }
    ]
}

# 17.03: nacionalismo-03
k = "nacionalismo-03"
# Grammar (7):
# 0: Mientras crecían las escuelas públicas, aumentaba también el interés por formar ciudadanos.
# 1: Los gobiernos impulsaron la alfabetización porque consideraban que la educación fortalecía la ciudadanía.
# 2: La escuela pública transmitía conocimientos mientras difundía una idea de nación.
# 3: Dado el número de misiones organizadas, estas seguramente habrán alcanzado, hacia finales de la década de 1920, a una parte considerable de la población rural.
# 4: Para entonces se habrá construido, solo en México, un número de escuelas rurales varias veces superior al que existía antes de la revolución.
# 5: Quienes hayan revisado su impacto real habrán confirmado que la educación pública resultó decisiva para construir un sentido de pertenencia nacional.
# 6: La escuela, el maestro y el idioma nacional se habrán convertido, en la práctica, en la cara más visible del propio Estado.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La escuela pública y las misiones culturales",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Para los líderes del nacionalismo latinoamericano, la integración ciudadana era imposible sin arrancar a millones de personas del analfabetismo. {G(k, 0)} {G(k, 1)} Las aulas se convirtieron en el taller cívico donde se forjaban los nuevos ideales patrios."
        },
        {
            "type": "narration",
            "text": f"En México, José Vasconcelos encabezó desde 1921 una épica pedagógica como secretario de Educación Pública. Creó las 'misiones culturales', enviando a miles de maestros rurales a caballo por sierras y desiertos para enseñar lectura, técnicas agronómicas, higiene y civismo. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 2)} En las escuelas se cantaba el himno patrio, se izaba la bandera y se aprendía una historia compartida que superaba los viejos localismos feudales."
        },
        {
            "type": "narration",
            "text": f"Experiencias similares de expansión escolar se vivieron en Uruguay bajo el legado de José Pedro Varela, y en Argentina con la ley 1420 de educación común, laica y obligatoria. {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"En aldeas donde jamás había llegado un juez ni un médico, {G(k, 6)} El maestro rural asumió el papel de consejero comunitario, líder civil y baluarte de la soberanía nacional."
        }
    ]
}

# 17.04: nacionalismo-04
k = "nacionalismo-04"
# Grammar (7):
# 0: A lo largo del proceso, los gobiernos intentaron reforzar las fronteras y ampliar la administración.
# 1: En el marco de la integración territorial, algunas comunidades negociaron su posición.
# 2: Como consecuencia de una mayor integración, el Estado podía ejercer autoridad sobre regiones más amplias.
# 3: Amplias regiones del interior ya no estaban físicamente desconectadas del resto del territorio nacional, gracias al ferrocarril.
# 4: Muchas comunidades rurales que antes gestionaban sus propios asuntos ya no podían hacerlo sin la intervención de alguna autoridad estatal.
# 5: Poblaciones enteras ya no podían permanecer invisibles para el aparato estadístico del Estado.
# 6: Las regiones más remotas del país ya no podían considerarse, con propiedad, territorios ajenos a la autoridad efectiva del Estado nacional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Integración territorial, cartografía y fronteras vivas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante el siglo diecinueve, vastas extensiones de la geografía sudamericana y centroamericana permanecían como territorios ignotos donde el poder estatal era una simple ficción cartográfica. {G(k, 0)} Ingenieros militares y geógrafos trazaron mapas topográficos precisos y delimitaron hitos fronterizos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Carreteras para automóviles y líneas de telégrafo comenzaron a conectar valles aislados con los puertos marítimos y las capitales administrativas. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} A través del registro civil obligatorio, las campañas de vacunación y los censos nacionales de población, {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"El servicio militar obligatorio convocó por primera vez a jóvenes de diversas etnias y clases sociales a cuarteles comunes. {G(k, 1)} Caciques locales y gobernadores tuvieron que someterse a la ley federal o negociar cupos de representación."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Esta consolidación espacial cohesionó las fronteras republicanas y clausuró definitivamente la era de las guerras civiles intestinas."
        }
    ]
}

# 17.05: nacionalismo-05
k = "nacionalismo-05"
# Grammar (7):
# 0: A medida que avanzaban las primeras décadas del siglo veinte, el propio significado de la palabra "Estado" fue transformándose.
# 1: A medida que se profesionalizaban los ejércitos y crecía la presencia burocrática cotidiana, el Estado dejaba de depender de la lealtad personal hacia un caudillo.
# 2: A medida que este proceso avanzaba, también lo hacía un proyecto cultural paralelo destinado a dar sentido simbólico al Estado.
# 3: A medida que la escuela, el censo y el servicio militar alcanzaban regiones cada vez más remotas, la experiencia de ser ciudadano se volvía más concreta.
# 4: El Estado-nación fue construido mediante reformas, aunque la integración política siguió siendo desigual.
# 5: La modernización fortaleció instituciones que aumentaron la capacidad administrativa del Estado.
# 6: La legitimidad se construía mientras el Estado intentaba integrar poblaciones diversas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El nuevo rostro del Estado-nación en América Latina",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} La concepción decimonónica del 'Estado gendarme' —limitado a cobrar impuestos aduaneros y reprimir revueltas— fue reemplazada por una visión interventora, social y educadora."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 5)} Ministerios técnicos, bancos centrales y departamentos de estadística sustituyeron el arbitrio personal de los presidentes por reglas jurídicas uniformes."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Artistas plásticos, escritores y maestros tejieron una narrativa patriótica que enaltecía el mestizaje y la soberanía sobre el territorio patrio. {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 4)} Los habitantes del interior dejaron de verse únicamente como miembros de un valle o una aldea para concebirse como partícipes de una colectividad política soberana."
        },
        {
            "type": "narration",
            "text": f"Este vigoroso Estado-nación nacionalista, dotado de instituciones profesionales y legitimidad popular, constituiría la herramienta decisiva para enfrentar el vendaval económico que se desataría en 1929."
        }
    ]
}

# =============================================================================
# UNIT 18: grandepresion
# =============================================================================

# 18.01: grandepresion-01
k = "grandepresion-01"
# Grammar (8):
# 0: Los inversores, que apenas acababan de disfrutar de casi una década de crecimiento aparentemente imparable, entraron en pánico.
# 1: Millones de personas que acababan de perder buena parte de sus ahorros se lanzaron a retirar dinero de los bancos.
# 2: Los bancos estadounidenses apenas acababan de vivir una década prestando generosamente a gobiernos y empresas de todo el mundo.
# 3: El resultado fue una crisis que, aunque había comenzado en Nueva York, no tardaría en sentirse en cualquier rincón del planeta.
# 4: A raíz del colapso financiero, disminuyeron la producción y el comercio internacional.
# 5: A lo largo de los primeros años de la crisis, numerosos países experimentaron una fuerte recesión.
# 6: Como consecuencia de la crisis, la demanda internacional se redujo considerablemente.
# 7: Aunque la crisis comenzó en Estados Unidos, sus efectos se extendieron a otras economías.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El crac de Wall Street y la onda expansiva mundial",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En octubre de 1929, la Bolsa de Valores de Wall Street en Nueva York colapsó en los catastróficos 'Jueves Negro' y 'Martes Negro'. {G(k, 0)} {G(k, 1)} Cientos de instituciones financieras quebraron de la noche a la mañana, desatando una contracción crediticia mundial."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} De repente, Wall Street cortó en seco la refinanciación de préstamos a los gobiernos latinoamericanos, exigiendo la repatriación urgente de capitales. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} Fábricas en Detroit, Birmingham y el Ruhr cerraron sus puertas, arrojando al paro a decenas de millones de obreros en los países industrializados."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Las potencias industriales erigieron murallas proteccionistas como el arancel Smoot-Hawley en Estados Unidos y los acuerdos de preferencia imperial británicos en Ottawa, cerrando sus aduanas a los productos ultramarinos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} Para las economías latinoamericanas, cuya prosperidad dependía del comercio libre y del crédito externo, el impacto fue demoledor e inmediato."
        }
    ]
}

# 18.02: grandepresion-02
k = "grandepresion-02"
# Grammar (8):
# 0: Tan pronto como la crisis financiera estadounidense comenzó a extenderse por el mundo, América Latina descubrió su vulnerabilidad estructural.
# 1: Tan pronto como la demanda mundial de café, cobre y salitre se desplomó, los precios de estos productos cayeron en picado.
# 2: Tan pronto como los bancos estadounidenses y europeos dejaron de prestar dinero, varios gobiernos se vieron obligados a suspender el pago de su deuda externa.
# 3: Tan pronto como los gobiernos comprendieron la magnitud de lo que estaba ocurriendo, quedó claro que el modelo exportador no podría sobrevivir sin cambios.
# 4: Las economías latinoamericanas fueron afectadas por la contracción del comercio mundial.
# 5: Los ingresos por exportación fueron reducidos por la caída de la demanda internacional.
# 6: Las materias primas fueron vendidas a precios mucho más bajos durante la crisis.
# 7: Nuevas políticas económicas fueron adoptadas cuando los mercados exteriores dejaron de ofrecer los mismos ingresos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El impacto devastador en América Latina",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 4)} Entre 1929 y 1932, el valor de las exportaciones de la región se redujo en más del sesenta por ciento, desbaratando los presupuestos nacionales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 5)} {G(k, 6)} En Brasil, el café perdió dos tercios de su valor, forzando al gobierno a comprar y quemar millones de sacos en calderas de locomotoras para evitar la ruina total de los caficultores."
        },
        {
            "type": "narration",
            "text": f"En Chile, según determinó la Sociedad de Naciones, el golpe fue el más catastrófico del planeta: las ventas de salitre y cobre cayeron un 85%, provocando el cierre masivo de oficinas salitreras en Atacama y arrojando a la mendicidad a 40.000 mineros que marcharon hacia Santiago."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Bolivia fue el primer país en declarar la moratoria en 1931, seguida rápidamente por Perú, Chile, Colombia, Brasil y México. Las reservas de oro y divisas de los bancos centrales se evaporaron."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 7)} El colapso reveló con brutal crudeza que el crecimiento basado exclusivamente en vender materias primas a potencias extranjeras era insostenible."
        }
    ]
}

# 18.03: grandepresion-03
k = "grandepresion-03"
# Grammar (8):
# 0: Se redujeron las importaciones cuando disminuyeron los ingresos procedentes de las exportaciones.
# 1: Se aumentaron algunos aranceles para proteger la producción nacional.
# 2: En varios países se adoptaron medidas para estimular la demanda interna.
# 3: Se buscó reducir la dependencia del comercio exterior mediante nuevas políticas económicas.
# 4: La Gran Depresión fue la peor crisis económica que América Latina había sufrido jamás hasta ese momento.
# 5: Esta caída resultó ser la mayor contracción comercial que sus economías jamás habían experimentado.
# 6: La caída del comercio se tradujo en la peor crisis fiscal que estos gobiernos jamás habían enfrentado.
# 7: Esta combinación resultó la prueba más severa que los Estados latinoamericanos recién fortalecidos jamás habían enfrentado.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Asfixia fiscal, quiebre del libre comercio y agitación social",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} La parálisis de los puertos marítimos y la sequía crediticia desarticularon los circuitos comerciales que habían operado con fluidez durante medio siglo."
        },
        {
            "type": "narration",
            "text": f"Como los ingresos de las tesorerías públicas dependían casi exclusivamente de los impuestos a las aduanas exteriores, {G(k, 6)} Los gobiernos no tenían recursos para pagar a los maestros, soldados ni funcionarios públicos, provocando deserciones y huelgas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} Sin divisas extranjeras, las tiendas y almacenes quedaron desabastecidos de productos manufacturados, herramientas y vestimenta importada. {G(k, 1)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Se implementaron controles de cambios de monedas y subsidios de emergencia para sostener el consumo popular y frenar el hambre en las barriadas urbanas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} La debacle quebró la fe ciega en el libre mercado y obligó a las sociedades latinoamericanas a emprender una reestructuración económica radical."
        }
    ]
}

# 18.04: grandepresion-04
k = "grandepresion-04"
# Grammar (8):
# 0: ¿Por qué seguir dependiendo de importar manufacturas en lugar de producirlas dentro del propio país?
# 1: En lugar de exportar materias primas baratas para importar después productos caros, los países debían fabricar ellos mismos buena parte de lo que compraban.
# 2: En lugar de simplemente esperar a que la demanda internacional se recuperara, países como Brasil, México y Argentina comenzaron a levantar barreras arancelarias.
# 3: En lugar de limitarse a recaudar impuestos y mantener el orden, muchos gobiernos comenzaron a invertir directamente en industrias estratégicas.
# 4: Los gobiernos respondieron a la crisis impulsando la producción nacional.
# 5: Las industrias crecieron sustituyendo algunos productos que antes se importaban.
# 6: Los Estados ampliaron su intervención buscando reducir los efectos de la crisis.
# 7: Las economías cambiaron adaptándose a un contexto en el que el comercio internacional era menor.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El viraje hacia la Industrialización por Sustitución de Importaciones (ISI)",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Ante la imposibilidad material de importar bienes del extranjero por falta de divisas, una pregunta crucial se impuso en los debates económicos continentales: {G(k, 0)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Así comenzó el modelo de Industrialización por Sustitución de Importaciones (ISI). {G(k, 4)} {G(k, 5)} Talleres y fábricas textiles, alimentarias, metalmecánicas y farmacéuticas proliferaron en los suburbios de São Paulo, Buenos Aires, Medellín y la Ciudad de México."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} {G(k, 3)} Se fundaron corporaciones públicas de desarrollo como la CORFO en Chile (1939), y se nacionalizaron o crearon empresas estatales de acero, energía eléctrica y refinerías petroleras como Volta Redonda en Brasil y PEMEX en México."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} El mercado interno y el empleo industrial se convirtieron en el motor primordial del crecimiento económico, desplazando a las tradicionales oligarquías terratenientes de la cúspide de las decisiones."
        },
        {
            "type": "narration",
            "text": f"El modelo ISI sentó las bases de una pujante clase obrera industrial y una burguesía fabril nacional, reconfigurando para siempre el mapa sociopolítico de la región."
        }
    ]
}

# 18.05: grandepresion-05
k = "grandepresion-05"
# Grammar (8):
# 0: La crisis expuso brutalmente la vulnerabilidad del modelo exportador. De ahí que muchos historiadores consideren 1929 uno de los verdaderos puntos de inflexión.
# 1: La crisis demostró que ese modelo ya no bastaba. De ahí que resultara tan difícil, después de 1929, defender seriamente su continuidad.
# 2: Se abrió un espacio político para nuevas ideas. De ahí que surgieran figuras políticas de un tipo nuevo, capaces de apelar directamente a las masas.
# 3: La industrialización comenzó casi por necesidad. De ahí que se convirtiera, en las siguientes décadas, en la política económica dominante de la región.
# 4: A lo largo de la década, la crisis produjo una transformación de las políticas económicas de varios países.
# 5: Como consecuencia de la caída de las exportaciones, los gobiernos tuvieron que buscar nuevas fuentes de crecimiento.
# 6: La crisis puso de manifiesto una dependencia exterior que había sido menos visible durante los años anteriores.
# 7: Aunque la recuperación fue desigual, el periodo contribuyó a fortalecer la intervención del Estado en la economía.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "1929 como punto de inflexión histórica y antesala del populismo",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 6)} La catástrofe económica de 1929 no fue una mera recesión cíclica, sino el cierre definitivo del largo siglo diecinueve liberal en América Latina."
        },
        {
            "type": "narration",
            "text": f"El terremoto social derribó regímenes políticos en cadena. En el fatídico año de 1930, una ola de revoluciones y golpes de Estado sacudió a Argentina, Brasil, Perú, Bolivia y Guatemala. En Brasil, la Revolución de 1930 llevó al poder a Getúlio Vargas, desmantelando el monopolio oligárquico de la 'República Velha'. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} {G(k, 7)} Los viejos dogmas del libre cambio y la no intervención estatal quedaron sepultados bajo las urgencias del desempleo masivo y la demanda de soberanía productiva."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Líderes carismáticos como Getúlio Vargas en Brasil, Lázaro Cárdenas en México y más tarde Juan Domingo Perón en Argentina articularon alianzas policlasistas entre obreros fabriles, sectores medios e industriales nacionales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} La Gran Depresión clausuró la era del libre comercio agroexportador e inauguró la época de la industrialización soberana, el Estado de bienestar y el populismo clásico latinoamericano."
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
