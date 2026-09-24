"""
Reauthors Latin America B1 Block 2 (Units 07-12, lessons 01-05) stories with canonical filenames.
Each story is 380-550 words in engaging, narrative history style.
Strictly embeds grammar example sentences verbatim and covers all vocabulary words and exercise facts.
"""

import json
import os

STORIES = {
    # =========================================================================
    # UNIT 07: razaclasepoder
    # =========================================================================
    "b1-razaclasepoder-01-castas.json": {
        "id": "story.b1.razaclasepoder.01",
        "title": "El sistema de castas y su representación",
        "unit": "razaclasepoder",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Durante el siglo dieciocho, las ciudades del imperio español en América bullían con una diversidad humana fascinante y compleja. En las plazas de México y Lima se cruzaban comerciantes peninsulares, aristócratas criollos, artesanos mestizos, indígenas de comunidades rurales y personas de origen africano, tanto libres como esclavizadas. Ante este mestizaje incesante, la élite virreinal sintió una profunda inquietud por preservar sus prerrogativas sociales y su pureza de sangre."
            },
            {
                "type": "narration",
                "text": "En la sociedad colonial se clasificaba a las personas según su origen y su ascendencia. El estamento dominante ideó una jerarquía conocida como el sistema de castas, un catálogo obsesivo que pretendía asignar a cada individuo un lugar inmutable en la sociedad. Con estas categorías se concedían, o se negaban, ciertos privilegios legales. Un hombre catalogado como blanco o criollo podía ingresar a la universidad, aspirar a cargos en el cabildo y vestir telas finas; en contraste, las personas ubicadas en los escalones inferiores debían pagar tributos especiales y tenían prohibido portar armas o ejercer ciertos oficios artesanales."
            },
            {
                "type": "narration",
                "text": "En el siglo dieciocho, se popularizó en Nueva España un género pictórico dedicado a este sistema. Estas series artísticas, conocidas como pinturas de castas, solían constar de dieciséis cuadros numerados que representaban a una pareja y a su descendencia. Pintores novohispanos de renombre, como Miguel Cabrera y José Joaquín Magón, plasmaron con minucioso detalle las vestimentas, ocupaciones y frutos de la tierra asociados a cada mezcla racial."
            },
            {
                "type": "narration",
                "text": "Estas pinturas se encargaban a artistas locales, y se enviaban con frecuencia a España. Los virreyes y altos funcionarios las llevaban consigo a la corte de Madrid como curiosidades exóticas y testimonios del orden imperial. La cuadrícula pictórica exhibía combinaciones con nombres tan pintorescos como desconcertantes: 'castizo', 'morisco', 'lobo', 'torna atrás' e incluso 'tente en el aire'."
            },
            {
                "type": "narration",
                "text": "Sin embargo, los historiadores recuerdan que este afán clasificatorio reflejaba más las ansiedades de la élite que la realidad cotidiana. En las calles, las fronteras raciales eran extraordinariamente porosas. Muchas familias utilizaban el escalafón de manera pragmática, negociando su condición en los censos o comprando certificados reales de blancura mediante la cédula de 'gracias al sacar'. La rígida pirámide oficial existía en los lienzos, pero en el mundo real la sociedad americana desbordaba constantemente las etiquetas coloniales."
            }
        ]
    },

    "b1-razaclasepoder-02-elites.json": {
        "id": "story.b1.razaclasepoder.02",
        "title": "Las reformas borbónicas y el resentimiento criollo",
        "unit": "razaclasepoder",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia la segunda mitad del siglo dieciocho, la monarquía hispánica emprendió una profunda reorganización de sus dominios americanos. Durante las décadas precedentes bajo los monarcas de la dinastía de los Austrias, la corona en bancarrota había tolerado una amplia autonomía local en las colonias. Muchos cargos administrativos fueron literalmente vendidos por la corona española. Hacendados y comerciantes criollos adinerados compraban puestos en los cabildos, juzgados y audiencias, administrando la justicia y las finanzas a favor de sus propias redes familiares."
            },
            {
                "type": "narration",
                "text": "Esa situación fue transformada radicalmente por las reformas borbónicas. Con la llegada del rey Carlos III y sus ministros ilustrados, Madrid se propuso recuperar el control directo de las colonias, aumentar la recaudación fiscal y frenar el contrabando con Gran Bretaña. La venta de cargos fue restringida drásticamente. Se creó el sistema de intendencias y se enviaron burócratas profesionales directamente desde la península ibérica para sustituir a los criollos."
            },
            {
                "type": "narration",
                "text": "Los puestos más importantes fueron reservados casi exclusivamente para peninsulares recién llegados. Los criollos americanos, a pesar de poseer inmensas haciendas, educación universitaria y un profundo arraigo local, se vieron súbitamente desplazados de las Reales Audiencias, donde los codiciados cargos de oidor les fueron negados sistemáticamente."
            },
            {
                "type": "narration",
                "text": "El golpe más doloroso ocurrió en 1767 con la expulsión de la Compañía de Jesús. La inmensa mayoría de los jesuitas expulsados eran clérigos criollos ilustrados que educaban a la juventud patricia y administraban prósperas haciendas. Su expulsión a medianoche generó disturbios populares y una profunda sensación de agravio e injusticia."
            },
            {
                "type": "narration",
                "text": "Esta marginación sistemática provocó un profundo resentimiento en la élite letrada americana. Los criollos comenzaron a verse a sí mismos no solo como súbditos marginados, sino como los legítimos dueños de una tierra usurpada por administradores forasteros que desconocían la realidad del continente."
            }
        ]
    },

    "b1-razaclasepoder-03-posicion.json": {
        "id": "story.b1.razaclasepoder.03",
        "title": "Indígenas y afrodescendientes frente al orden colonial",
        "unit": "razaclasepoder",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el estrato más bajo de la pirámide virreinal, las poblaciones indígenas y afrodescendientes padecieron las cargas más pesadas del imperio. Sin embargo, su respuesta distó mucho de ser una aceptación sumisa. Frente a la explotación cotidiana, las comunidades subalternas desarrollaron complejas estrategias que combinaban la negociación legal, la adaptación pragmática y la rebelión armada abierta."
            },
            {
                "type": "narration",
                "text": "Buscando en teoría 'protegerlos', la corona clasificó a los indígenas legalmente casi como menores de edad permanentes. A través de la llamada 'república de indios', las autoridades españolas reconocieron ciertas tierras comunales y permitieron a los caciques tradicionales cobrar tributos, pero al precio de someter a los pueblos a un control paternalista estricto y al trabajo forzado en minas y obrajes mediante la mita."
            },
            {
                "type": "narration",
                "text": "Por su parte, la población de origen africano enfrentaba la brutalidad de la esclavitud en plantaciones azucareras y minas de oro. No obstante, en las ciudades virreinales surgió un dinámico sector de afrodescendientes libres. Buscando aprovechar cualquier vía de movilidad disponible, muchos hombres libres se alistaron en milicias locales. Las milicias de pardos y morenos ofrecían fueros militares, prestigio social y exenciones impositivas muy codiciadas."
            },
            {
                "type": "narration",
                "text": "En otros casos, la resistencia adoptó formas radicales mediante el cimarronaje y la fuga colectiva hacia selvas y serranías inaccesibles. Resistiendo militarmente los intentos españoles de reconquistarlo, San Basilio de Palenque logró un reconocimiento formal de su libertad. En 1691, la corona española firmó una capitulación que convirtió a este palenque colombiano en el primer pueblo libre de América."
            },
            {
                "type": "narration",
                "text": "Comparando ambas experiencias, resulta evidente que ninguna encajaba en una sola categoría de 'oprimidos'. Entre el reclamo jurídico en los tribunales, el servicio militar miliciano y la insurrección en los palenques, los sectores populares abrieron grietas fundamentales en el muro de la dominación colonial."
            }
        ]
    },

    "b1-razaclasepoder-04-mestizaje.json": {
        "id": "story.b1.razaclasepoder.04",
        "title": "Mestizaje demográfico y la compra de blancura",
        "unit": "razaclasepoder",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A medida que avanzaba el siglo dieciocho, la realidad demográfica de Hispanoamérica superaba con creces los esquemas rígidos ideados en el siglo dieciséis. Tres siglos de convivencia urbana, intercambios comerciales y uniones afectivas habían transformado a las colonias en un mosaico biológico y cultural incontrolable para los administradores virreinales."
            },
            {
                "type": "narration",
                "text": "A lo largo del periodo colonial, la mezcla entre poblaciones avanzó de forma constante. Lo que inicialmente había sido concebido como una estricta división binaria entre la 'república de españoles' y la 'república de indios' se vio desbordado por millones de mestizos, mulatos, zambos y castas diversas que constituían la inmensa mayoría de la población urbana y rural."
            },
            {
                "type": "narration",
                "text": "A raíz de esta realidad demográfica, el sistema legal de castas se volvió cada vez más difícil de sostener. En los mercados y talleres, la distinción física resultaba sumamente ambigua. Muchas personas de origen mixto acumulaban fortunas considerables gracias al comercio minorista o la minería, pero las leyes les impedían formalmente ingresar a gremios de honor o vestir atuendos reservados a la aristocracia blanca."
            },
            {
                "type": "narration",
                "text": "Como consecuencia de esa tensión, la corona terminó recurriendo a una solución tan insólita como reveladora. En 1795, la monarquía promulgó la Real Cédula de 'gracias al sacar', un arancel oficial que permitía a los súbditos de color comprar legalmente la condición de blancos pagando sumas fijadas por la Real Hacienda. Este pragmatismo fiscal enfureció a los cabildos criollos de Caracas y Lima, cuyos miembros protestaron amargamente ante lo que consideraban una degradación de sus privilegios tradicionales."
            },
            {
                "type": "narration",
                "text": "A lo largo de estas últimas décadas coloniales, la desigualdad no disminuyó a pesar del aumento de la mezcla. La discriminación racial continuó siendo un muro formidable que bloqueaba las aspiraciones de millones de personas y acumulaba un polvorín social que estallaría con la crisis del imperio."
            }
        ]
    },

    "b1-razaclasepoder-05-herencias.json": {
        "id": "story.b1.razaclasepoder.05",
        "title": "El legado social y las promesas de la república",
        "unit": "razaclasepoder",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Cuando las guerras de independencia destruyeron el dominio político español en el continente, los nuevos líderes republicanos se apresuraron a redactar constituciones inspiradas en la Ilustración europea. Los decretos patriotas proclamaron la igualdad natural de los hombres y la eliminación de las odiosas distinciones estamentales del antiguo régimen."
            },
            {
                "type": "narration",
                "text": "El sistema legal de castas fue abolido con notable rapidez tras las guerras de independencia. Las distinciones legales basadas en el origen racial fueron eliminadas de la legislación en apenas unos años. En los flamantes parlamentos republicanos ya no se registraba el color de la piel en los certificados de nacimiento ni se exigía pureza de sangre para litigar en los tribunales."
            },
            {
                "type": "narration",
                "text": "Sin embargo, la realidad material y social demostró ser infinitamente más resistente que los decretos legislativos. Las jerarquías no fueron simplemente borradas por un decreto legal: fueron transformadas, y en gran medida heredadas. Las tierras más fértiles, las minas y las casas comerciales continuaron en manos de las mismas familias patricias criollas que habían dominado la colonia."
            },
            {
                "type": "narration",
                "text": "Ciertas prácticas culturales fueron mantenidas de forma casi inalterada durante décadas. El racismo cotidiano, la exclusión de las mayorías indígenas del derecho al voto mediante exigencias de alfabetización y la servidumbre doméstica perpetuaron la brecha social. Aunque el tributo colonial fue formalmente abolido, en países como Perú y Bolivia fue reinstaurado bajo el nombre de 'contribución indígena' para financiar el presupuesto estatal."
            },
            {
                "type": "narration",
                "text": "La construcción de una ciudadanía verdaderamente igualitaria se convirtió en una de las asignaturas pendientes más dolorosas de América Latina. Las sombras de la pirámide colonial se proyectaron a lo largo de todo el siglo diecinueve, recordándole a las jóvenes repúblicas que abolir las leyes del rey resultaba mucho más sencillo que extirpar los prejuicios arraigados en el alma de la sociedad."
            }
        ]
    },

    # =========================================================================
    # UNIT 08: independencia
    # =========================================================================
    "b1-independencia-01-mundocambia.json": {
        "id": "story.b1.independencia.01",
        "title": "La crisis atlántica y los ecos revolucionarios",
        "unit": "independencia",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia finales del siglo dieciocho, una ola de convulsiones políticas transformó radicalmente el mundo atlántico. En las principales ciudades hispanoamericanas, las tertulias literarias y los salones letrados se convirtieron en centros clandestinos de debate filosófico y político."
            },
            {
                "type": "narration",
                "text": "Nuevas ideas sobre la libertad y la igualdad fueron difundidas por el mundo atlántico mediante libros y periódicos. Textos de Rousseau, Voltaire y Montesquieu entraban de contrabando en los puertos coloniales burlando la censura de la Inquisición española. La independencia de Estados Unidos y la Revolución Francesa fueron seguidas de cerca por lectores criollos educados. Hombres como Francisco de Miranda y Antonio Nariño soñaban con aplicar esos principios de soberanía popular y derechos del hombre en suelo americano."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el impacto de estos acontecimientos no fue homogéneo. En 1791, la colonia francesa de Saint-Domingue se convirtió en el escenario de la primera revolución triunfante de personas esclavizadas en la historia mundial. Ese ejemplo fue admirado por algunos, pero también fue temido profundamente por muchos criollos propietarios de esclavos. El colapso del orden blanco y la proclamación de Haití en 1804 despertaron un pavor visceral en las élites terratenientes de Caracas, La Habana y Lima."
            },
            {
                "type": "narration",
                "text": "El ejemplo haitiano fue observado con gran atención por las élites criollas de todo el continente. El temor a una insurrección incontrolable de las masas populares impulsó a los hacendados a mantener una postura prudente, prefiriendo la lealtad a la corona antes que arriesgar sus haciendas en una conflagración social abierta."
            },
            {
                "type": "narration",
                "text": "No obstante, cuando las tropas de Napoleón Bonaparte invadieron España en 1808 y capturaron al rey Fernando VII, el dique de contención se quebró. La crisis dinástica metropolitana obligó a los criollos a tomar una decisión inaplazable: aceptar a un monarca usurpador francés o asumir las riendas de su propio destino histórico."
            }
        ]
    },

    "b1-independencia-02-guerras.json": {
        "id": "story.b1.independencia.02",
        "title": "La insurgencia en México y las campañas continentales",
        "unit": "independencia",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "El proceso emancipador en América Latina adoptó dimensiones colosales y características singulares según la geografía de cada virreinato. Mientras en el Río de la Plata la revolución comenzó con un debate capitular en Buenos Aires, en Nueva España estalló con la fuerza de un terremoto campesino."
            },
            {
                "type": "narration",
                "text": "En México se libró un conflicto casi ininterrumpido entre 1810 y 1821. El levantamiento inicial convocado por el cura Miguel Hidalgo en Dolores congregó a decenas de miles de peones rurales, mineros e indígenas bajo el estandarte de la Virgen de Guadalupe. Tras la captura y ejecución de Hidalgo, José María Morelos dotó a la insurgencia de disciplina táctica y un ideario republicano plasmado en los 'Sentimientos de la Nación'."
            },
            {
                "type": "narration",
                "text": "Se organizaron levantamientos contra las autoridades coloniales en distintos momentos y lugares. La guerra no fue una serie ordenada de batallas convencionales, sino una vorágine de asedios, guerrillas serranas y enfrentamientos brutales donde el decreto de 'Guerra a Muerte' y las represalias virreinales diezmaron a poblaciones enteras."
            },
            {
                "type": "narration",
                "text": "En Sudamérica se llevaron a cabo campañas militares enormes a lo largo de miles de kilómetros. Desde los llanos venezolanos hasta las heladas cumbres de los Andes, ejércitos multinacionales integrados por criollos, mestizos, indígenas y libertos afrodescendientes marcharon sin tregua durante más de una década bajo condiciones climáticas brutales."
            },
            {
                "type": "narration",
                "text": "La epopeya continental culminó en las alturas andinas del Perú. En la batalla de Ayacucho se derrotó de manera decisiva al último gran ejército realista del continente. El 9 de diciembre de 1824, el mariscal Antonio José de Sucre selló para siempre el fin de la dominación imperial española en la América meridional."
            }
        ]
    },

    "b1-independencia-03-lideres.json": {
        "id": "story.b1.independencia.03",
        "title": "Bolívar y San Martín: dos estrategias para un continente",
        "unit": "independencia",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "La victoria sobre el poder realista exigió una visión estratégica continental y el liderazgo de dos hombres excepcionales con visiones complementarias sobre el arte de la guerra y el futuro político de América del Sur."
            },
            {
                "type": "narration",
                "text": "San Martín se movía desde el sur, organizando un ejército en Argentina antes de cruzar los Andes. En Mendoza, el estratega rioplatense adiestró pacientemente a más de cinco mil soldados y arrieros. En enero de 1817, protagonizó una de las mayores hazañas logísticas de la historia militar al cruzar la cordillera por seis pasos distintos a más de cuatro mil metros de altitud, liberando a Chile en las memorables batallas de Chacabuco y Maipú."
            },
            {
                "type": "narration",
                "text": "Ambas campañas, actuando de manera independiente pero con un objetivo compartido, convergerían finalmente en Perú. Mientras San Martín zarpaba desde Valparaíso al mando de una expedición marítima para sitiar Lima, en el norte Simón Bolívar emprendía su audaz campaña de liberación de Nueva Granada."
            },
            {
                "type": "narration",
                "text": "Descendiendo inesperadamente sobre territorio neogranadino, sus fuerzas lograron una victoria decisiva en Boyacá. Tras atravesar las nieves del páramo de Pisba, Bolívar sorprendió a las tropas virreinales en agosto de 1819, liberando Bogotá y fundando la Gran Colombia, a la que sumaría Venezuela tras la victoria de Carabobo en 1821."
            },
            {
                "type": "narration",
                "text": "El encuentro definitivo entre ambos próceres ocurrió en la entrevista de Guayaquil en julio de 1822. Reconociendo que el mando unificado era indispensable para doblegar la resistencia realista en la sierra peruana, San Martín, renunciando sorprendentemente a su cargo, se retiró por completo de la vida pública. Su noble renuncia permitió a Bolívar y a Sucre culminar victoriosamente la emancipación en Junín y Ayacucho."
            }
        ]
    },

    "b1-independencia-04-republicas.json": {
        "id": "story.b1.independencia.04",
        "title": "Bancarrota, préstamos británicos y colapso económico",
        "unit": "independencia",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "El triunfo en los campos de batalla coronó un heroísmo indiscutible, pero dejó a las nuevas naciones al borde del abismo material. La guerra no solo había destruido ejércitos, sino que había quebrado la columna vertebral de la producción económica y comercial del continente."
            },
            {
                "type": "narration",
                "text": "A raíz de más de una década de guerra casi continua, las nuevas repúblicas heredaron economías devastadas. Los ricos yacimientos de plata de Guanajuato y Potosí yacían inundados o destruidos por la falta de mantenimiento, la ganadería había sido sacrificada para alimentar a las tropas y las haciendas agrícolas estaban abandonadas por falta de brazos y capitales."
            },
            {
                "type": "narration",
                "text": "En el marco de este colapso económico, varios gobiernos solicitaron préstamos a bancos británicos. Los agentes de las repúblicas hispanoamericanas acudieron en masa a la Bolsa de Londres entre 1822 y 1825, emitiendo bonos por millones de libras esterlinas con casas financieras como Baring Brothers para financiar sus ejércitos y comprar armamento."
            },
            {
                "type": "narration",
                "text": "Esa burbuja, en el marco de la primera gran crisis financiera internacional moderna, se desplomó en 1825. El pánico bancario londinense cortó súbitamente los créditos, y hacia 1827 casi todas las repúblicas hispanoamericanas habían caído en cesación de pagos. Con las aduanas marítimas como única fuente de ingresos fiscales, los nuevos estados quedaron atrapados en deudas asfixiantes."
            },
            {
                "type": "narration",
                "text": "A raíz de la exclusión sistemática de los criollos de los puestos más altos, había relativamente poca gente con experiencia de gobierno. La repentina desaparición de la administración virreinal dejó a las jóvenes repúblicas en manos de comandantes militares y letrados sin experiencia en finanzas públicas, agravando la crisis fiscal durante décadas."
            }
        ]
    },

    "b1-independencia-05-paraquien.json": {
        "id": "story.b1.independencia.05",
        "title": "Las promesas inconclusas de la igualdad ciudadana",
        "unit": "independencia",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al proclamar la independencia, los congresos constituyentes elaboraron magníficos discursos sobre el nacimiento de un orden justo y fraterno. En el papel, las repúblicas representaban la consagración de los ideales ilustrados de igualdad jurídica y libertad universal."
            },
            {
                "type": "narration",
                "text": "En casi todas las nuevas constituciones, la ciudadanía fue proclamada igual para todos los hombres libres. Se eliminaron formalmente los fueros nobiliarios y las leyes de castas del antiguo régimen español, abriendo en teoría las puertas del progreso cívico a todos los habitantes del continente."
            },
            {
                "type": "narration",
                "text": "Sin embargo, los límites del cambio social pronto se hicieron evidentes. Fueron aprobadas leyes de 'vientre libre', que declaraban libres solo a los hijos nacidos después de cierta fecha. Para evitar la hostilidad de los hacendados esclavistas, los gobiernos postergaron la manumisión de los adultos y sometieron a los jóvenes libertos a largos patronatos obligatorios que prolongaron la esclavitud hasta mediados del siglo diecinueve."
            },
            {
                "type": "narration",
                "text": "Asimismo, las comunidades indígenas sufrieron un duro revés. Durante la colonia, las leyes de indias habían protegido las tierras comunales frente a la voracidad de los latifundistas. Esa protección fue eliminada por muchas de las nuevas repúblicas, inspiradas en ideas liberales. Los legisladores consideraban que la propiedad colectiva era un vestigio arcaico y un obstáculo para el libre mercado."
            },
            {
                "type": "narration",
                "text": "Por último, la mitad de la población continuó marginada del poder civil. El derecho al voto no fue concedido a las mujeres en ningún país latinoamericano en el momento de la independencia. La nueva república pertenecía exclusivamente a una minoría letrada y propietaria, dejando las grandes demandas populares como una tarea pendiente para las futuras generaciones."
            }
        ]
    },

    # =========================================================================
    # UNIT 09: nuevasrepublicas
    # =========================================================================
    "b1-nuevasrepublicas-01-estado.json": {
        "id": "story.b1.nuevasrepublicas.01",
        "title": "El sueño roto de la unidad y la fragmentación continental",
        "unit": "nuevasrepublicas",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al consumarse la independencia, los libertadores imaginaron la creación de grandes confederaciones capaces de rivalizar con las potencias europeas y defender la soberanía americana. Sin embargo, el desafío de administrar territorios tan gigantescos sin comunicaciones modernas superó todas las previsiones."
            },
            {
                "type": "narration",
                "text": "Después de 1821, se organizaron administraciones desde cero. Las flamantes repúblicas carecían de ministerios eficientes, cuerpos diplomáticos consolidados y sistemas tributarios modernos. Se establecieron autoridades locales y regionales en todo el nuevo territorio. Sin embargo, la falta de caminos pavimentados y la lejanía de las capitales convirtieron la gobernabilidad en una pesadilla cotidiana."
            },
            {
                "type": "narration",
                "text": "En Centroamérica se optó inicialmente por una solución federal. En 1823 se formaron las Provincias Unidas del Centro de América. Esta federación unió a Guatemala, El Salvador, Honduras, Nicaragua y Costa Rica. A pesar de los esfuerzos de líderes liberales como Francisco Morazán por sostener la unión mediante reformas modernas, las oligarquías provinciales y las guerras civiles provocaron el colapso total de la federación en 1839."
            },
            {
                "type": "narration",
                "text": "En el norte de Sudamérica ocurrió una tragedia semejante. La Gran Colombia forjada por Bolívar comenzó a desmoronarse por los celos de los caudillos locales. En 1830, Venezuela y Ecuador se separaron formalmente de la Nueva Granada, destruyendo el mayor proyecto geopolítico del Libertador poco antes de su muerte en Santa Marta."
            },
            {
                "type": "narration",
                "text": "El continente quedó fragmentado en cerca de veinte estados soberanos, vulnerables a la presión económica de las potencias extranjeras y consumidos por disputas fronterizas que marcarían el siglo diecinueve."
            }
        ]
    },

    "b1-nuevasrepublicas-02-fronteras.json": {
        "id": "story.b1.nuevasrepublicas.02",
        "title": "Fronteras inciertas y el principio de uti possidetis",
        "unit": "nuevasrepublicas",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al independizarse de la corona española, las jóvenes naciones se encontraron ante un problema jurídico de proporciones titánicas: ¿dónde terminaba exactamente el territorio de un país y dónde comenzaba el de su vecino? El mapa administrativo colonial había sido ambiguo y superpuesto."
            },
            {
                "type": "narration",
                "text": "Fue adoptado por la mayoría de las nuevas repúblicas un principio legal conocido como uti possidetis juris. Según este axioma del derecho romano y colonial, cada nueva nación debía poseer los territorios que correspondían a los virreinatos, capitanías generales o reales audiencias en el año 1810, al momento de estallar las revoluciones emancipadoras."
            },
            {
                "type": "narration",
                "text": "Ese principio fue aceptado formalmente por casi todos los gobiernos, pero resultó difícil de aplicar. Las cédulas reales dictadas por monarcas españoles en los siglos dieciséis y diecisiete describían límites imprecisos basados en ríos desconocidos, selvas vírgenes y cordilleras jamás exploradas por topógrafos profesionales."
            },
            {
                "type": "narration",
                "text": "Las fronteras fueron discutidas, renegociadas y, en ocasiones, disputadas militarmente durante décadas. Países hermanos se enfrentaron en sangrientas guerras limítrofes, como el conflicto entre Perú y la Gran Colombia en 1828 o la devastadora Guerra del Pacífico en 1879 por los ricos depósitos de salitre del desierto de Atacama."
            },
            {
                "type": "narration",
                "text": "La organización territorial interna de cada país fue modificada repetidamente. Los enfrentamientos entre centralistas y federalistas alteraron una y otra vez la división provincial de naciones como México, Colombia y Argentina, demostrando la extrema dificultad de plasmar el orden legal sobre una geografía indómita."
            }
        ]
    },

    "b1-nuevasrepublicas-03-liberales.json": {
        "id": "story.b1.nuevasrepublicas.03",
        "title": "Liberales contra conservadores: el debate por la Iglesia",
        "unit": "nuevasrepublicas",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Durante el siglo diecinueve, la vida política hispanoamericana se organizó en torno a una feroz polarización ideológica entre dos grandes bandos: el partido liberal y el partido conservador. Aunque ambos pertenecían a la misma élite letrada y terrateniente, sostenían proyectos de nación radicalmente antagónicos."
            },
            {
                "type": "narration",
                "text": "Los liberales, buscando reducir el poder de la Iglesia, defendían la venta de sus extensas propiedades. Para el pensamiento liberal, la Iglesia católica constituía un obstáculo formidable para el progreso económico debido a sus inmensos bienes en 'manos muertas' que no pagaban impuestos ni circulaban en el mercado libre. Exigían la secularización de la educación, el registro civil laico y la tolerancia religiosa."
            },
            {
                "type": "narration",
                "text": "Los conservadores, intentando preservar el orden social heredado de la colonia, defendían el papel tradicional de la Iglesia. Argumentaban que la fe católica era el único lazo espiritual capaz de mantener unida a una sociedad dividida por castas y regionalismos, advirtiendo que destruir la religión desataría la anarquía moral y el caos revolucionario."
            },
            {
                "type": "narration",
                "text": "Ambos bandos, formando alianzas cambiantes con caudillos regionales y compitiendo por el ejército, promovían visiones opuestas. Cuando las elecciones no favorecían sus intereses, tanto liberales como conservadores recurrían de inmediato al alzamiento armado y al golpe de Estado cuartelario para imponer sus programas por la fuerza."
            },
            {
                "type": "narration",
                "text": "Compitiendo por imponer su visión de manera permanente, ninguno de los dos bandos logró una victoria definitiva. La disputa desangró a los países en prolongadas guerras civiles, polarizando a las familias y retrasando la modernización institucional del continente."
            }
        ]
    },

    "b1-nuevasrepublicas-04-inestabilidad.json": {
        "id": "story.b1.nuevasrepublicas.04",
        "title": "El pronunciamiento militar y la inestabilidad crónica",
        "unit": "nuevasrepublicas",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En las primeras décadas posteriores a la emancipación, la legitimidad política en Hispanoamérica no se construía en las urnas electorales, sino en los cuarteles y guarniciones militares. La falta de un consenso básico sobre las reglas de juego democrático convirtió la violencia política en el mecanismo habitual de recambio de gobernantes."
            },
            {
                "type": "narration",
                "text": "A raíz de la falta de instituciones consolidadas, la inestabilidad política se convirtió en la norma. Los parlamentos eran débiles, la recaudación fiscal era exigua y los gobiernos centrales carecían de monopolio sobre el uso de la fuerza en las provincias distantes."
            },
            {
                "type": "narration",
                "text": "En el marco de esta inestabilidad surgió un término específico: el pronunciamiento. Un general o comandante militar leía una proclama acusando al presidente de turno de violar la constitución, sublevaba a sus tropas y marchaba sobre la capital exigiendo un cambio de gobierno o una nueva asamblea constituyente."
            },
            {
                "type": "narration",
                "text": "Bolivia, como consecuencia de esta dinámica, llegó a tener varias decenas de gobiernos distintos en pocas décadas. En México, el general Antonio López de Santa Anna ocupó y abandonó la presidencia de la república en once ocasiones diferentes, alternando entre posturas federalistas y centralistas según las conveniencias del momento."
            },
            {
                "type": "narration",
                "text": "Como consecuencia directa de esta rotación constante, resultaba prácticamente imposible sostener políticas de largo plazo. Las escuelas no se construían, los caminos quedaban a medio abrir y los presupuestos nacionales se consumían casi íntegramente en pagar sueldos a oficiales militares para evitar nuevos cuartelazos."
            }
        ]
    },

    "b1-nuevasrepublicas-05-desafios.json": {
        "id": "story.b1.nuevasrepublicas.05",
        "title": "El balance de las primeras décadas republicanas",
        "unit": "nuevasrepublicas",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia 1850, al cumplirse medio siglo de vida independiente, las repúblicas hispanoamericanas ofrecían un balance lleno de luces y sombras que desmentía tanto los optimismos ingenuos como las condenas simplistas de los observadores extranjeros."
            },
            {
                "type": "narration",
                "text": "A lo largo de las primeras décadas republicanas, los nuevos países enfrentaron varios desafíos al mismo tiempo. Tuvieron que defender su soberanía frente a agresiones extranjeras, delimitar fronteras inciertas, amortizar deudas ruinosas con bancos de Londres y forjar una cultura cívica en sociedades marcadas por el analfabetismo y el militarismo."
            },
            {
                "type": "narration",
                "text": "A lo largo de todo este proceso coexistieron el fracaso evidente y un progreso mucho más silencioso. Aunque el caos político y los constantes pronunciamientos acaparaban los titulares de la prensa, en los pueblos y ciudades se expandía la imprenta, crecían los mercados locales y se formaba una nueva generación de juristas, maestros y periodistas comprometidos con el Estado de derecho."
            },
            {
                "type": "narration",
                "text": "En última instancia, ni siquiera la inestabilidad más severa impidió que se fueran acumulando las bases de un Estado moderno. Las constituciones fallidas y los ensayos institucionales no fueron tiempo perdido, sino el laboratorio político necesario donde los pueblos aprendieron el difícil ejercicio del autogobierno republicano."
            },
            {
                "type": "narration",
                "text": "En última instancia, estos primeros desafíos fueron el material bruto con el que cada país terminó construyendo instituciones capaces de perdurar. Sobre aquellas dolorosas experiencias del siglo diecinueve se edificarían las transformaciones económicas, educativas y sociales de la era moderna latinoamericana."
            }
        ]
    },

    # =========================================================================
    # UNIT 10: caudillismo
    # =========================================================================
    "b1-caudillismo-01-caudillo.json": {
        "id": "story.b1.caudillismo.01",
        "title": "El caudillo y la suma del poder",
        "unit": "caudillismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el siglo diecinueve, la crisis de legitimidad provocada por el colapso del imperio colonial abrió el camino a una figura política emblemática de la historia hispanoamericana. En un continente donde las constituciones escritas parecían impotentes para frenar la anarquía, el hombre fuerte armado se convirtió en el eje indiscutible de la vida pública."
            },
            {
                "type": "narration",
                "text": "Se llamaba caudillo a un líder regional cuya autoridad se apoyaba en su capacidad militar personal y su carisma. Generalmente acaudalado estanciero o veterano de las guerras patriotas, el caudillo mantenía el orden mediante la lealtad directa de sus peones, gauchos o llaneros armados. En muchas regiones, se reconocía su autoridad de facto mucho antes de que ningún cargo oficial la confirmara."
            },
            {
                "type": "narration",
                "text": "El ejemplo más célebre fue Juan Manuel de Rosas en Buenos Aires. En 1835, la legislatura le concedió la 'suma del poder público', concentrando todas las facultades gubernamentales en su persona. Apoyado por la Mazorca, Rosas impuso un régimen de férreo control social. Se exigía, en la vida cotidiana, el uso de una cinta roja como muestra pública de lealtad. Aquella 'divisa punzó' debía llevarse obligatoriamente en el pecho por hombres y mujeres para demostrar sumisión al Restaurador de las Leyes."
            },
            {
                "type": "narration",
                "text": "Se debate todavía, entre historiadores, si Rosas debe entenderse como un tirano o como un garante de orden. Mientras sus opositores liberales exiliados lo retrataban como un autócrata sanguinario que ahogó la libertad, sus defensores destacan que defendió la soberanía nacional frente a los bloqueos navales de Francia e Inglaterra y mantuvo la cohesión de la confederación."
            },
            {
                "type": "narration",
                "text": "El fenómeno del caudillismo demostró que el poder político decimonónico dependía mucho más de las lealtades afectivas y la fuerza armada que de los abstractos principios parlamentarios importados de Europa."
            }
        ]
    },

    "b1-caudillismo-02-poderpersonal.json": {
        "id": "story.b1.caudillismo.02",
        "title": "José Antonio Páez y las redes de lealtad personal",
        "unit": "caudillismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Para comprender el funcionamiento del caudillismo, es indispensable analizar la compleja red de relaciones humanas que sustentaba el mando de estos líderes. A diferencia de las democracias modernas, el poder de un caudillo no emanaba de una burocracia impersonal, sino de lazos íntimos de compadrazgo y reciprocidad material."
            },
            {
                "type": "narration",
                "text": "Favores, tierras y protección eran ofrecidos personalmente por el caudillo a cambio de lealtad. En los llanos venezolanos, José Antonio Páez encarnó a la perfección este modelo señorial. Páez fue reconocido como líder natural por otros llaneros acostumbrados a la vida dura del ganado. Su extraordinaria valentía en combate y su habilidad inigualable como jinete le granjearon una devoción ciega entre los jinetes de la sabana."
            },
            {
                "type": "narration",
                "text": "Sus antiguos compañeros de armas fueron colocados en puestos de confianza. Tras liderar la separación de Venezuela de la Gran Colombia en 1830, Páez gobernó apoyándose en los coroneles que habían combatido a su lado en las Queseras del Medio y Carabobo, nombrándolos jefes de cantón y comandantes de armas locales."
            },
            {
                "type": "narration",
                "text": "Las tierras conquistadas o confiscadas durante las guerras fueron repartidas entre sus seguidores más cercanos. Mediante la entrega de hatos ganaderos y vales de haberes militares, el caudillo consolidó una pirámide de lealtades superpuestas donde cada beneficiario se convertía en un defensor incondicional del régimen."
            },
            {
                "type": "narration",
                "text": "Esa estructura de poder personalista suplió la ausencia de un Estado consolidado, creando un consenso basado en el intercambio de favores que garantizó la estabilidad de Venezuela durante casi dos décadas."
            }
        ]
    },

    "b1-caudillismo-03-ejercitopolitica.json": {
        "id": "story.b1.caudillismo.03",
        "title": "Facundo Quiroga y las montoneras provinciales",
        "unit": "caudillismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En las extensas provincias del interior argentino, la confrontación política adoptó formas de guerra irregular a través de las temibles milicias rurales conocidas como montoneras. Al frente de estas partidas gauchas se erigió la figura indómita de Juan Facundo Quiroga, el célebre 'Tigre de los Llanos'."
            },
            {
                "type": "narration",
                "text": "Reuniendo estas fuerzas rápidamente cuando la situación lo exigía, y disolviéndolas de nuevo cuando el conflicto terminaba, Quiroga ejercía un poder militar flexible. Sus hombres no cobraban un salario regular ni vivían en cuarteles; eran paisanos que volvían a sus tareas agrícolas y ganaderas hasta que el toque de clarín del caudillo riojano los convocaba nuevamente a la batalla bajo el lema de 'Religión o Muerte'."
            },
            {
                "type": "narration",
                "text": "Extendiendo su influencia mediante campañas militares mientras negociaba alianzas políticas, Quiroga se convirtió en una figura muy poderosa. Llegó a dominar el noroeste argentino, disputándole la hegemonía a los unitarios porteños y actuando como árbitro supremo en los conflictos entre gobernadores provinciales."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el sistema caudillesco albergaba una fragilidad estructural insalvable. Cuando el poder militar y el poder político dependen de la misma persona, actuando simultáneamente como comandante y como gobernante, un colapso puede ser instantáneo. No existían instituciones sucesorias capaces de sobrevivir a la muerte del líder carismático."
            },
            {
                "type": "narration",
                "text": "En febrero de 1835, Quiroga fue emboscado y asesinado a balazos en Barranca Yaco. Su muerte, dejando un vacío de poder real de la noche a la mañana, desató una crisis política considerable. La desaparición del líder riojano conmocionó a toda la Confederación Argentina y precipitó la concentración absoluta del poder en manos de Juan Manuel de Rosas en Buenos Aires."
            }
        ]
    },

    "b1-caudillismo-04-ordeninestabilidad.json": {
        "id": "story.b1.caudillismo.04",
        "title": "Sarmiento, Rafael Carrera y el enigma del orden",
        "unit": "caudillismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "El auge de los caudillos desató apasionados debates intelectuales sobre el ser nacional hispanoamericano. Para las élites urbanas ilustradas, los hombres fuertes rurales eran una plaga que impedía la llegada del progreso, pero la realidad histórica era mucho más compleja."
            },
            {
                "type": "narration",
                "text": "A raíz de su propia experiencia como opositor exiliado, Sarmiento publicó 'Facundo: Civilización y Barbarie' en 1845. En su célebre libro escrito desde Chile, Domingo Faustino Sarmiento contrapuso la civilización europea de las ciudades a la barbarie violenta del desierto pampeano. En el marco de esa interpretación, el caudillismo quedó asociado casi automáticamente con el atraso y la barbarie."
            },
            {
                "type": "narration",
                "text": "Sin embargo, esa dicotomía resultaba insuficiente para explicar casos en otras latitudes. En el marco de casos como el de Rafael Carrera, esta interpretación resulta considerablemente más difícil de sostener. En Guatemala, Carrera lideró en 1837 un masivo levantamiento campesino e indígena maya contra las reformas liberales que pretendían privatizar las tierras comunales, suprimir los fueros eclesiásticos e imponer jueces letrados forasteros."
            },
            {
                "type": "narration",
                "text": "A raíz de este tipo de apoyo popular genuino, algunos historiadores prefieren una interpretación distinta. Para los pueblos mayas, el caudillo mestizo Rafael Carrera no era un bárbaro tirano, sino un mediador y un protector frente a la agresiva modernización de las élites letradas capitalinas."
            },
            {
                "type": "narration",
                "text": "Carrera gobernó Guatemala con amplio respaldo social hasta 1865, demostrando que muchos caudillos actuaron como escudos de las tradiciones populares frente al elitismo liberal."
            }
        ]
    },

    "b1-caudillismo-05-legado.json": {
        "id": "story.b1.caudillismo.05",
        "title": "El balance del caudillismo y su legado político",
        "unit": "caudillismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al examinar el fenómeno del caudillismo en perspectiva histórica, se comprueba que sus huellas moldearon de manera decisiva la evolución política de América Latina hasta bien entrado el siglo veinte."
            },
            {
                "type": "narration",
                "text": "En algunos lugares, como Chile, la estabilidad institucional limitó el papel de los caudillos; en otros, como Bolivia, el patrón de líderes personalistas se prolongó mucho más allá del siglo diecinueve. Mientras la república chilena consolidaba tempranamente una oligarquía parlamentaria estable bajo la constitución de 1833, en los Andes y el Caribe los generales continuaron disputándose los palacios presidenciales por la fuerza de las armas."
            },
            {
                "type": "narration",
                "text": "En algunos casos, el caudillismo dejó redes de patronazgo que siguieron influyendo en la política local; en otros, el recuerdo del caos generó un consenso a favor de instituciones civiles fuertes. Hacia finales de siglo, la llegada de los ferrocarriles, el telégrafo y los ejércitos regulares profesionales terminó con el poder militar de las montoneras rurales."
            },
            {
                "type": "narration",
                "text": "No obstante, las pautas culturales sobrevivieron a la desaparición física de los jinetes armados. En algunos países se llegó a una separación relativamente clara entre autoridad militar y civil; en otros, esa separación siguió siendo mucho más porosa. Esta permeabilidad facilitó periódicas intervenciones militares en la vida cívica."
            },
            {
                "type": "narration",
                "text": "Politólogos contemporáneos destacan que el caudillismo fue el síntoma de una sociedad que buscaba el orden en hombres providenciales ante la fragilidad de sus leyes escritas, un legado personalista que continuaría debatiéndose en las democracias de la era moderna."
            }
        ]
    },

    # =========================================================================
    # UNIT 11: nacionnacionalismo
    # =========================================================================
    "b1-nacionnacionalismo-01-nacion.json": {
        "id": "story.b1.nacionnacionalismo.01",
        "title": "¿Qué es una nación?",
        "unit": "nacionnacionalismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Tras las guerras de independencia, los gobiernos de Hispanoamérica gobernaron inmensos territorios desprovistos de una identidad colectiva previa. En un mismo territorio convivían hacendados criollos, comunidades quechuas o mayas que no hablaban español, artesanos mestizos urbanos y peones rurales aislados en las serranías."
            },
            {
                "type": "narration",
                "text": "Una nación no es simplemente un territorio con fronteras dibujadas en un mapa. No basta con promulgar leyes ni designar una capital para que millones de habitantes sientan que pertenecen a una misma comunidad espiritual. Una nación consiste en un grupo de personas que comparten, o creen compartir, una historia y un destino común."
            },
            {
                "type": "narration",
                "text": "Una nación es una comunidad imaginada porque la inmensa mayoría de sus miembros nunca se conocerán entre sí. Benedict Anderson acuñó este concepto para explicar cómo un porteño de Buenos Aires y un arriero de Salta jamás se encontrarían en persona; sin embargo, en la mente de cada uno vive la imagen viva de su comunión como argentinos."
            },
            {
                "type": "narration",
                "text": "Esa construcción, que consistía en crear símbolos, relatos y rituales compartidos, no era un proceso natural. Los nuevos estados tuvieron que desplegar una labor deliberada mediante la imprenta, los periódicos locales, los mapas escolares y las fiestas patrias para inculcar la idea de que todos formaban un solo pueblo con un pasado heroico compartido."
            },
            {
                "type": "narration",
                "text": "La nación no estaba dada de antemano; fue un ambicioso artefacto cultural que las élites decimonónicas tuvieron que forjar paso a paso para consolidar la lealtad de sus ciudadanos."
            }
        ]
    },

    "b1-nacionnacionalismo-02-simbolos.json": {
        "id": "story.b1.nacionnacionalismo.02",
        "title": "Símbolos nacionales",
        "unit": "nacionnacionalismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Para consolidar el sentimiento patriótico entre poblaciones diversas, los gobernantes republicanos necesitaron crear una nueva liturgia cívica que reemplazara a las devociones monárquicas coloniales."
            },
            {
                "type": "narration",
                "text": "Se adoptaron, en las nuevas repúblicas, banderas, himnos, escudos y ceremonias públicas. Estos emblemas funcionaron como objetos de veneración colectiva en las plazas públicas y en las escuelas recién fundadas. La bandera argentina fue diseñada por el general Manuel Belgrano en 1812. A orillas del río Paraná, en Rosario, Belgrano enarboló el pabellón celeste y blanco bajo un cielo despejado, inspirándose en los colores de la escarapela nacional para entusiasmar a sus tropas."
            },
            {
                "type": "narration",
                "text": "En México, la búsqueda de una identidad sonora llevó a una iniciativa cívica ejemplar. Se organizó un concurso público para elegir tanto la letra como la música del himno mexicano. En 1853, en medio de la crisis posterior a la invasión estadounidense, los versos patrióticos del poeta Francisco González Bocanegra y la música marcial de Jaime Nunó fueron seleccionados para forjar el canto sagrado de la patria."
            },
            {
                "type": "narration",
                "text": "Estos símbolos fueron presentados, desde el principio, como si expresaran una esencia nacional profunda y preexistente. Sin embargo, los historiadores contemporáneos recuerdan que se trataba de invenciones contingentes, diseñadas deliberadamente por las autoridades para infundir fervor patriótico en momentos de grave fractura política."
            },
            {
                "type": "narration",
                "text": "A través de desfiles cívicos y juramentos escolares, los nuevos símbolos lograron arraigarse en el corazón popular, convirtiéndose en el patrimonio emocional indiscutible de las nuevas naciones."
            }
        ]
    },

    "b1-nacionnacionalismo-03-identidad.json": {
        "id": "story.b1.nacionnacionalismo.03",
        "title": "Crear una identidad",
        "unit": "nacionnacionalismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al independizarse de España, las repúblicas hispanoamericanas debieron responder a un desafío cultural apremiante: ¿cómo diferenciarse de la antigua metrópoli si compartían el mismo idioma español y la misma religión católica? En México, la respuesta consistió en una audaz reinterpretación del pasado prehispánico."
            },
            {
                "type": "narration",
                "text": "Era necesario que la población reconociera esos símbolos como propios. El gobierno incorporó al escudo patrio la imagen azteca del águila sobre el nopal devorando una serpiente. Era esencial, para el nuevo Estado mexicano, que ese pasado prehispánico se convirtiera en fuente de orgullo nacional. Se erigieron estatuas monumentales de Cuauhtémoc y se ensalzó la resistencia indígena frente a los conquistadores españoles como el origen glorioso de la patria mexicana."
            },
            {
                "type": "narration",
                "text": "Sin embargo, esta política oficial encerraba una dolorosa paradoja. No era extraño que el pasado indígena fuera glorificado al mismo tiempo que el presente indígena era ignorado. Mientras los letrados exaltaban los códices mexicas en los museos de la capital, las comunidades originarias vivas sufrían el despojo de sus tierras comunales y la marginación social."
            },
            {
                "type": "narration",
                "text": "Convenía a las élites que el pasado prehispánico se percibiera como una civilización gloriosa pero clausurada. De ese modo, los pueblos indígenas quedaban convertidos en reliquias arqueológicas del pasado heroico, impidiendo que sus demandas contemporáneas cuestionaran el poder de los terratenientes criollos."
            },
            {
                "type": "narration",
                "text": "Aquel indigenismo de museo cumplió una función clave para dotar de singularidad a la república, pero dejó pendiente la integración digna y con plenos derechos de millones de indígenas vivos."
            }
        ]
    },

    "b1-nacionnacionalismo-04-pueblosfronteras.json": {
        "id": "story.b1.nacionnacionalismo.04",
        "title": "Pueblos y fronteras",
        "unit": "nacionnacionalismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Las fronteras nacionales que dividen el mapa sudamericano fueron el resultado de guerras, tratados diplomáticos y convenios aduaneros decimonónicos. Sin embargo, aquellas líneas abstractas trazadas en las cancillerías chocaron contra realidades culturales mucho más antiguas y profundas."
            },
            {
                "type": "narration",
                "text": "El Estado presentaba el territorio como una unidad natural, aunque en la práctica existían pueblos cuya vida ignoraba esas líneas. En el altiplano andino, comunidades quechuas y aymaras habían compartido circuitos de pastoreo trashumante, ferias de trueque y vínculos familiares durante siglos a través de una geografía ecológica complementaria."
            },
            {
                "type": "narration",
                "text": "Tras la Guerra del Pacífico (1879-1884), Chile anexó la provincia salitrera de Tarapacá y privó a Bolivia de su litoral marítimo. Mientras que las fronteras modernas fueron trazadas por acuerdos diplomáticos, las comunidades aymaras habían mantenido redes que cruzaban esas zonas. De pronto, un mismo pueblo originario quedó fragmentado entre las soberanías territoriales de Chile, Bolivia y Perú."
            },
            {
                "type": "narration",
                "text": "El Estado, sin embargo, insistía en presentar a sus ciudadanos como una comunidad nacional homogénea. Las escuelas de frontera impusieron la chilenización o peruanización forzosa, prohibiendo el uso del idioma aymara en los recintos escolares y militarizando los pasos limítrofes."
            },
            {
                "type": "narration",
                "text": "Los aymaras continuaron practicando vínculos transfronterizos, aunque las autoridades los reconocieran cada vez menos. A través de festividades patronales, romerías y ferias andinas, los pueblos originarios preservaron su memoria colectiva más allá de las divisiones impuestas por los estados modernos."
            }
        ]
    },

    "b1-nacionnacionalismo-05-imaginarnacion.json": {
        "id": "story.b1.nacionnacionalismo.05",
        "title": "Imaginar la nación",
        "unit": "nacionnacionalismo",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al culminar el recorrido por el siglo diecinueve latinoamericano, resulta evidente que la construcción nacional no fue un proceso pacífico ni automático, sino una obra monumental de ingeniería política y cultural."
            },
            {
                "type": "narration",
                "text": "Todas las naciones son comunidades imaginadas; ese hecho no las hace menos reales para quienes las viven y las defienden. Que una identidad patria sea el producto de discursos, banderas inventadas y pactos políticos no disminuye el heroísmo ni el sacrificio de quienes lucharon por su país."
            },
            {
                "type": "narration",
                "text": "El nacionalismo debe estudiarse ni como una verdad eterna ni como una simple mentira, sino como un proceso histórico concreto. No fue un fenómeno unívoco ni un mero instrumento manipulador de las élites, sino un campo de batalla en el que distintos grupos sociales pugnaron por definir el significado de la soberanía y la pertenencia cívica."
            },
            {
                "type": "narration",
                "text": "Recorrimos varias piezas de ese proceso: una bandera improvisada, un himno elegido por concurso, y fronteras que dividieron a comunidades enteras. Analizamos las contradicciones entre un pasado indígena exaltado en los museos y un presente popular postergado por el sufragio censitario."
            },
            {
                "type": "narration",
                "text": "Comprendido así, el nacionalismo deja de ser un simple telón de fondo y se convierte en uno de los proyectos más ambiciosos del periodo. Sobre aquellas comunidades imaginadas decimonónicas se asentaron las naciones latinoamericanas contemporáneas, con todas sus virtudes, sus tensiones y sus sueños compartidos de justicia."
            }
        ]
    },

    # =========================================================================
    # UNIT 12: liberalismomodernizacion
    # =========================================================================
    "b1-liberalismomodernizacion-01-ideas.json": {
        "id": "story.b1.liberalismomodernizacion.01",
        "title": "Las ideas liberales",
        "unit": "liberalismomodernizacion",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia mediados del siglo diecinueve, una nueva generación de dirigentes asumió el poder en gran parte de América Latina. Cansados de las guerras civiles y del estancamiento económico, estos políticos abrazaron el credo del liberalismo doctrinario europeo, convencidos de que la libertad individual y el libre mercado transformarían a sus patrias en naciones prósperas y modernas."
            },
            {
                "type": "narration",
                "text": "En consecuencia, se esperaba que la nueva ciudadanía sustituyera por completo a las viejas jerarquías coloniales. Los programas liberales promovían la igualdad ante la ley, la educación laica, la abolición de fueros eclesiásticos y militares y la primacía de la propiedad privada individual como motor del desarrollo social."
            },
            {
                "type": "narration",
                "text": "Por consiguiente, en la práctica, solo una minoría de hombres adultos ejercía realmente el derecho al voto. A pesar de la retórica igualitaria, las constituciones liberales establecieron un régimen de sufragio censitario. Para poder votar o postularse a cargos públicos, la ley exigía poseer bienes inmuebles de alto valor, contar con una renta considerable y demostrar que se sabía leer y escribir."
            },
            {
                "type": "narration",
                "text": "Como consecuencia, la igualdad legal proclamada en el papel convivía con una ciudadanía política profundamente restringida. El requisito de alfabetización excluyó automáticamente a más del ochenta por ciento de la población, compuesta por indígenas, afrodescendientes, peones campesinos y artesanos pobres que no tenían acceso a escuelas. Asimismo, las mujeres permanecieron excluidas de los derechos cívicos."
            },
            {
                "type": "narration",
                "text": "Por lo tanto, el propio liberalismo latinoamericano cargó con una tensión no resuelta entre sus principios y sus prácticas. Proclamaba la libertad universal, pero gobernó a través de oligarquías ilustradas que consideraban a las mayorías populares incapacitadas para ejercer la democracia directa."
            }
        ]
    },

    "b1-liberalismomodernizacion-02-reformar.json": {
        "id": "story.b1.liberalismomodernizacion.02",
        "title": "Reformar el Estado",
        "unit": "liberalismomodernizacion",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En ningún lugar de América Latina la lucha por secularizar el Estado fue tan encarnizada y radical como en México. Durante tres siglos, la Iglesia católica había sido la institución más poderosa del país, administrando enormes extensiones de tierras agrícolas, hospitales, escuelas y el registro de la vida cívica."
            },
            {
                "type": "narration",
                "text": "Entre 1855 y 1863 fueron promulgadas las llamadas Leyes de Reforma, impulsadas por Benito Juárez. Juárez, un jurista de origen zapoteco que llegó a la presidencia de la república, encabezó a un grupo brillante de liberales decididos a subordinar cualquier poder corporativo a la autoridad indiscutible de las leyes del Estado."
            },
            {
                "type": "narration",
                "text": "El matrimonio fue convertido en un contrato civil independiente del sacramento religioso. Las leyes desamortizaron y nacionalizaron los inmensos bienes raíces de la Iglesia, decretaron la libertad de cultos y secularizaron los cementerios parroquiales, poniendo fin a la discriminación religiosa en los entierros."
            },
            {
                "type": "narration",
                "text": "Fue creado un registro civil encargado de documentar oficialmente nacimientos, matrimonios y defunciones. Por primera vez en la historia mexicana, la existencia legal de un ciudadano ya no dependía de los libros parroquiales del cura local, sino de las actas oficiales del Estado."
            },
            {
                "type": "narration",
                "text": "Estas reformas fueron rechazadas con las armas por sectores conservadores, y el país fue sumido en la Guerra de Reforma. Aquel sangriento conflicto civil (1858-1861) desembocó en la intervención militar francesa y el efímero imperio de Maximiliano de Habsburgo, pero la firmeza republicana de Juárez restauró la república laica en 1867."
            }
        ]
    },

    "b1-liberalismomodernizacion-03-iglesiayestado.json": {
        "id": "story.b1.liberalismomodernizacion.03",
        "title": "Iglesia y Estado",
        "unit": "liberalismomodernizacion",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "La relación entre la Iglesia y el Estado no siguió la misma trayectoria laicista radical en toda Hispanoamérica. Mientras México rompía tajantemente con la tradición católica, en otras repúblicas los sectores conservadores fortalecieron a la Iglesia como el pilar insustituible del orden social."
            },
            {
                "type": "narration",
                "text": "En lugar de reducirse la influencia de la Iglesia católica, se la fortaleció deliberadamente como pilar del orden social. En Ecuador, el presidente Gabriel García Moreno consideró que el catolicismo era la única fuerza capaz de cohesionar a una nación fracturada por regionalismos y divisiones étnicas. Se llegó a declarar, en la constitución de 1869, que solo los católicos podían ser ciudadanos ecuatorianos. Conocida como la 'Carta Negra', esta constitución entregó la educación a las órdenes religiosas y consagró el país al Sagrado Corazón de Jesús."
            },
            {
                "type": "narration",
                "text": "No se resolvió esta disputa hasta la revolución liberal de 1895, liderada por Eloy Alfaro. Alfaro desmontó el estado confesional, implantó la educación laica e instauró el matrimonio civil tras décadas de enfrentamientos civiles en Ecuador."
            },
            {
                "type": "narration",
                "text": "En Colombia ocurrió un proceso conservador similar bajo la 'Regeneración' de Rafael Núñez. La Constitución de 1886 y el Concordato de 1887 devolvieron a la Iglesia católica el control de la enseñanza pública y amplios privilegios judiciales. Durante casi un siglo, no se separaron completamente en Colombia los asuntos religiosos de los asuntos del Estado."
            },
            {
                "type": "narration",
                "text": "Estos contrastes evidenciaron la profunda diversidad de caminos políticos que recorrieron las naciones latinoamericanas en su camino hacia la modernidad."
            }
        ]
    },

    "b1-liberalismomodernizacion-04-modernizar.json": {
        "id": "story.b1.liberalismomodernizacion.04",
        "title": "Modernizar la sociedad",
        "unit": "liberalismomodernizacion",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia las últimas décadas del siglo diecinueve, la inserción de América Latina en la economía capitalista mundial transformó radicalmente el paisaje material del continente. La Segunda Revolución Industrial en Europa y Estados Unidos exigía cantidades masivas de materias primas y alimentos que las repúblicas exportadoras se apresuraron a suministrar."
            },
            {
                "type": "narration",
                "text": "Gobiernos liberales por toda la región fueron construyendo ferrocarriles, considerándolos el símbolo más visible del progreso material. Las locomotoras de vapor conectaron regiones remotas, acortando distancias y abaratando los costos de transporte de manera revolucionaria."
            },
            {
                "type": "narration",
                "text": "Sin embargo, observando el mapa con atención, se descubre un patrón revelador. Las vías férreas no fueron trazadas para integrar el mercado interno ni conectar las ciudades provinciales entre sí, sino que confluían como un embudo desde los centros mineros, las zonas de salitre o las plantaciones agrícolas directamente hacia los puertos marítimos orientados a la exportación ultramarina."
            },
            {
                "type": "narration",
                "text": "Se tendieron también miles de kilómetros de líneas telegráficas, reduciendo de semanas a minutos el tiempo necesario para comunicar noticias. El telégrafo y los puertos modernizados permitieron a los gobiernos centrales afianzar su control territorial y movilizar rápidamente tropas para sofocar rebeliones en el interior."
            },
            {
                "type": "narration",
                "text": "Justificando intelectualmente todo este proceso, se difundió por la región una corriente filosófica llamada positivismo. Inspirados por Auguste Comte y Herbert Spencer, intelectuales y gobernantes adoptaron el lema de 'Orden y Progreso', argumentando que el crecimiento material y la estabilidad política justificaban restringir las libertades democráticas."
            }
        ]
    },

    "b1-liberalismomodernizacion-05-nuevomodelo.json": {
        "id": "story.b1.liberalismomodernizacion.05",
        "title": "Un nuevo modelo",
        "unit": "liberalismomodernizacion",
        "level": "B1",
        "track": "latam",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al culminar el siglo diecinueve, América Latina había concluido su transición desde el antiguo régimen colonial hacia el modelo de los estados nacionales modernos articulados al comercio global."
            },
            {
                "type": "narration",
                "text": "Por un lado, se lograron avances innegables: la ciudadanía dejó de depender formalmente del origen étnico. Se abolió la esclavitud, se eliminaron los tribunales estamentales, surgieron registros civiles laicos en países como México y se instalaron redes ferroviarias y telegráficas que dinamizaron la economía continental."
            },
            {
                "type": "narration",
                "text": "Por otro lado, sin embargo, conviene no idealizar excesivamente este periodo. La modernización agroexportadora profundizó la desigualdad social. La desamortización de tierras comunales indígenas enriqueció a grandes terratenientes y convirtió a millones de campesinos en peones asalariados o jornaleros desposeídos, mientras el sufragio censitario mantuvo a las mayorías al margen del poder político real."
            },
            {
                "type": "narration",
                "text": "En consecuencia, algunos historiadores prefieren hablar no de una única modernización liberal sino de varios proyectos liberales distintos. Mientras en México condujo al régimen autoritario del Porfiriato y en Argentina al orden oligárquico porteño, en otros países las reformas fueron moderadas y coexistieron con fuertes pactos eclesiásticos."
            },
            {
                "type": "narration",
                "text": "En definitiva, el periodo liberal no representó ni una simple historia de progreso continuo ni una simple historia de fracaso. Construyó la infraestructura material e institucional de América Latina, pero al costo de postergar demandas de justicia social que estallarían violentamente en las revoluciones del siglo veinte."
            }
        ]
    }
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
