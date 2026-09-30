"""
make_unit33_stories.py
Defines the 8 stories for Unit 33 and tests word counts.
"""
import re

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

STORIES = {
    "classics/b2/b2-33": {
        "id": "b2-33",
        "title": "Rayuela (Julio Cortázar, 1963)",
        "level": "B2",
        "lesson": 1,
        "type": "classics",
        "estimatedMinutes": 15,
        "summary": "Estudio literario y ontológico de la obra cumbre de Julio Cortázar: Horacio Oliveira, La Maga y el Club de la Serpiente en París; el regreso a Buenos Aires con Traveler y Talita; el Tablero de Dirección y la revolución formal de la contranovela que desafía la razón cartesiana burguesa en pos del centro existencial.",
        "characters": [
            "Horacio Oliveira (intelectual argentino errante y escéptico)",
            "Lucía, 'La Maga' (mujer uruguaya intuitiva, libre y espontánea)",
            "Manolo Traveler y Talita (amigos porteños en la segunda etapa)",
            "Morelli (escritor de culto y alter ego teórico de Cortázar)",
            "Los miembros del Club de la Serpiente (bohemios y melómanos en París)"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Publicada en Buenos Aires en junio de 1963 por la editorial Sudamericana, 'Rayuela' constituye un cataclismo estético irrepetible que dinamitó para siempre los cánones narrativos de la novela tradicional hispanoamericana. Con una audacia vanguardista sin parangón, el escritor argentino Julio Cortázar concibió este artefacto literario no como una historia lineal pasiva para el lector tradicional —al que calificaba provocadoramente de 'lector-hembra' por su apego al orden cronológico sumiso—, sino como un juego participativo abierto y desafiante que requiere de un 'lector cómplice' capaz de cocrear el sentido del texto. Ya desde su célebre 'Tablero de Dirección' inicial, Cortázar advierte que su libro contiene múltiples libros: el primero se lee de corrido desde el capítulo 1 hasta el 56, prescindiendo del resto; el segundo propone un laberinto hipertextual alternativo que salta a través de noventa y nueve capítulos prescindibles entretejiendo reflexiones teóricas, recortes periodísticos y aforismos poéticos."
            },
            {
                "type": "narration",
                "text": "La primera parte de la novela, titulada 'Del lado de allá', sumerge al lector en la bohemia errante del París de los años cincuenta, donde el protagonista Horacio Oliveira —un intelectual porteño corroído por la hiperlucidez racionalista, la angustia metafísica y la incapacidad de entregarse al fluir espontáneo de la vida— deambula sin rumbo fijo por los muelles del Sena, los puentes solitarios y los cafés brumosos del Barrio Latino. En este laberinto urbano se encuentra con Lucía, 'La Maga', una joven uruguaya desprovista de armaduras académicas pero dotada de una sabiduría poética directa, intuitiva y salvaje que desafía constantemente los pedantes silogismos de Horacio. Junto a un grupo cosmopolita de artistas marginales, exiliados y melómanos conocido como el 'Club de la Serpiente', debaten noches enteras sobre jazz, filosofía zen, literatura y pintura entre volutas de tabaco negro y tragos de vodka barato."
            },
            {
                "type": "narration",
                "text": "Sin embargo, la armonía precaria de este universo bohemio se desmorona de manera trágica ante la enfermedad y agonía silenciosa de Rocamadour, el pequeño hijo de La Maga, en una sórdida buhardilla parisina durante una velada donde los amigos discuten abstractamente sobre metafísica mientras el niño muere sin que nadie ose quebrar la ficción intelectual. Incapaz de asumir la culpa y el dolor desgarrador, Oliveira asiste a la desaparición definitiva de La Maga, quien se desvanece en las aguas del Sena o en la niebla europea, dejándolo atrapado en un remordimiento insoportable. Desesperado por reencontrar esa gracia perdida que la razón cartesiana no puede aprehender, Horacio es deportado de Francia y emprende el regreso forzoso hacia su Argentina natal, cerrando la etapa europea para ingresar en la dimensión introspectiva del desarraigo austral."
            },
            {
                "type": "narration",
                "text": "En la segunda sección, bautizada 'Del lado de acá', la acción se traslada a un Buenos Aires sofocante y surrealista donde Horacio se reencuentra con su viejo camarada Manolo Traveler —a quien llama su 'doble' irónico— y la esposa de este, Talita, en cuyos ojos y gestos Oliveira cree percibir obsesivamente la reencarnación espectral de La Maga. Trabajando sucesivamente en un circo ambulante y luego en un manicomio provincial regido por el doctor Ovejero, los personajes protagonizan episodios de una comicidad absurda teñida de delirio existencial, como la célebre escena del tablón tendido entre dos ventanas de edificios vecinos sobre la calle para pasarse un paquete de yerba mate y clavos. En el clímax dramático de la novela, instalado en su habitación del psiquiátrico rodeado de una compleja telaraña de hilos protectores y jofainas con agua, Horacio contempla desde la ventana el patio embaldosado donde una rayuela infantil dibuja el camino hacia el cielo prometido."
            },
            {
                "type": "narration",
                "text": "A través de las notas teóricas del viejo escritor Morelli diseminadas en la tercera parte ('De otros lados'), Cortázar formula una implacable teoría de la 'contranovela': la urgencia de demoler el lenguaje burgués anquilosado, lleno de lugares comunes y trampas sintácticas que adormecen la conciencia humana, para inventar una prosa libre capaz de acceder al 'kibbutz del deseo' o a la iluminación total del ser. 'Rayuela' no busca consolar con resoluciones morales cómodas ni clausuras dogmáticas; al dejar a Oliveira oscilando peligrosamente entre saltar al vacío sobre el patio del manicomio o reconciliarse con la locura lúcida, Cortázar convierte la lectura en una experiencia vital transformadora. En definitiva, la obra perdura como un monumento supremo a la libertad creadora: la certidumbre inextinguible de que vivir auténticamente exige arrojar el tejo con valentía y saltar sin miedo de casilla en casilla hasta conquistar la trascendencia espiritual de la Tierra al Cielo."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué innovación formal decisiva propone Julio Cortázar en el 'Tablero de Dirección' de Rayuela?",
                        "options": [
                            "La obligación de leer el libro traducido simultáneamente al francés.",
                            "La propuesta de múltiples itinerarios de lectura, combinando una lectura lineal con un recorrido hipertextual no lineal de capítulos alternos.",
                            "La inclusión obligatoria de grabaciones fonográficas de tango en cada página.",
                            "La eliminación total de los signos de puntuación y las mayúsculas."
                        ],
                        "correctIndex": 1,
                        "explanation": "El Tablero de Dirección invita al lector a elegir entre una lectura secuencial o un itinerario alternado que transforma la arquitectura de la obra."
                    },
                    {
                        "question": "¿Qué representa la figura de 'La Maga' en contraste con el temperamento intelectual de Horacio Oliveira?",
                        "options": [
                            "Una rica banquera que financia los viajes del Club de la Serpiente.",
                            "Una intuición poética, fresca y espontánea que accede directamente a la vida sin las mediaciones racionalistas burguesas de Horacio.",
                            "Una inspectora de policía que vigila a los artistas extranjeros en París.",
                            "Una cantante de ópera clásica que desprecia el jazz norteamericano."
                        ],
                        "correctIndex": 1,
                        "explanation": "La Maga encarna la pureza vivencial y la intuición lírica frente a la hiperracionalidad asfixiante y escéptica de Oliveira."
                    },
                    {
                        "question": "¿Cuál es el propósito central de la 'contranovela' teorizada por el personaje de Morelli en la obra?",
                        "options": [
                            "Imitar servilmente las novelas de caballería de la Edad Media española.",
                            "Destruir las fórmulas lingüísticas gastadas y las convenciones burguesas para despertar al lector como cocreador cómplice del sentido vital.",
                            "Escribir textos destinados exclusivamente a manuales escolares oficiales.",
                            "Prohibir la publicación de literatura experimental en América Latina."
                        ],
                        "correctIndex": 1,
                        "explanation": "Morelli propugna quebrar el lenguaje fossilizado y la pasividad del lector tradicional para refundar la percepción estética del mundo."
                    }
                ]
            }
        }
    },
    "world/b2/b2-integracion-01": {
        "id": "b2-integracion-01",
        "title": "Del Tratado de Asunción al Mercosur: Comercio, asimetrías y unión aduanera",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La génesis institucional y las contradicciones económicas del Mercado Común del Sur: el Tratado de Asunción de 1991, el Arancel Externo Común, las asimetrías estructurales entre potencias industriales y economías menores, y los mecanismos de compensación del FOCEM.",
        "characters": [
            "Delegados y cancilleres de Argentina, Brasil, Paraguay y Uruguay",
            "Economistas de la Secretaría del Mercosur con sede en Montevideo",
            "Empresarios industriales y agropecuarios de la cuenca del Plata"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "El 26 de marzo de 1991, en la histórica capital paraguaya, los presidentes de Argentina, Brasil, Paraguay y Uruguay estamparon sus firmas en el Tratado de Asunción, dando nacimiento formal al Mercado Común del Sur (Mercosur), el proyecto de integración interestatal más ambicioso y de mayor envergadura económica emprendido en el Cono Sur durante el siglo veinte. Inspirado en el anhelo de consolidar las frágiles democracias recién recuperadas tras décadas de dictaduras militares en la región y responder a la conformación de megabloques comerciales mundiales tras el fin de la Guerra Fría, el tratado fijó como meta fundacional la libre circulación de bienes, servicios y factores productivos entre los cuatro Estados partes, acompañada por el establecimiento de un Arancel Externo Común (AEC) y la coordinación concertada de políticas macroeconómicas y sectoriales."
            },
            {
                "type": "narration",
                "text": "Durante su primera década de vigencia, el bloque experimentó una expansión vertiginosa del comercio intrazona, multiplicando los flujos de intercambio manufacturero y agropecuario a un ritmo anual sin precedentes en la historia del continente. Sin embargo, este dinamismo mercantil inicial no tardó en toparse con las profundas asimetrías estructurales preexistentes entre sus miembros: por un lado, el coloso industrial de São Paulo y el complejo agroexportador argentino concentraban la inmensa mayoría de la inversión extranjera directa y la capacidad productiva de escala; por otro, economías más pequeñas como las de Paraguay y Uruguay denunciaban que la unión aduanera imperfecta las convertía en mercados cautivos de los gigantes vecinos, encareciendo sus importaciones de bienes de capital del resto del mundo sin abrirles mercados preferenciales suficientes. De igual manera, sectores sensibles como la industria automotriz y el azúcar debieron ser regulados mediante protocolos especiales de excepción administrada para amortiguar impactos laborales traumáticos."
            },
            {
                "type": "narration",
                "text": "Para mitigar estas disparidades que amenazaban con erosionar la cohesión política del bloque, los Estados partes crearon en 2004 el Fondo para la Convergencia Estructural del Mercosur (FOCEM), un mecanismo solidario pionero mediante el cual Brasil y Argentina aportan más del ochenta y cinco por ciento de los recursos financieros no reembolsables, mientras que Paraguay y Uruguay reciben la mayor parte de las asignaciones para financiar proyectos de infraestructura vial, electrificación rural, saneamiento básico y modernización aduanera. Gracias a estas obras conjuntas, se construyeron puentes internacionales estratégicos sobre el río Paraná y líneas de transmisión eléctrica de alta tensión que vincularon a las comunidades periféricas con los nodos fabriles más pujantes del hemisferio. Del mismo modo, estos proyectos de convergencia han promovido cadenas productivas de lácteos y granos que permiten a las pequeñas cooperativas campesinas colocar sus cosechas en mercados urbanos de países vecinos."
            },
            {
                "type": "narration",
                "text": "Asimismo, el Mercosur debió enfrentar recurrentes turbulencias arancelarias y disputas diplomáticas desatadas por devaluaciones monetarias unilaterales, barreras paraarancelarias fitosanitarias encubiertas y desacuerdos estratégicos en torno a la negociación de acuerdos de libre comercio con terceros países o bloques extrarregionales como la Unión Europea y China. Mientras algunos gobiernos promovían una mayor flexibilización normativa para permitir negociaciones bilaterales autónomas sin requerir el consenso unánime de los socios, otros defendían la preservación irrenunciable del Arancel Externo Común como el único escudo soberano capaz de resguardar el tejido manufacturero regional frente a la competencia desleal de manufacturas foráneas subsidiadas. Por consiguiente, la consolidación del Protocolo de Olivos y el funcionamiento del Tribunal Permanente de Revisión con sede en Asunción ofrecieron cauces jurídicos previsibles para resolver querellas comerciales complejas entre los Estados socios."
            },
            {
                "type": "narration",
                "text": "En conclusión, la trayectoria histórica del Mercosur demuestra que la integración regional no es una senda lineal exenta de fricciones ideológicas o intereses corporativos contrapuestos, sino una construcción colectiva constante que exige perseverancia diplomática y generosidad institucional. Más allá de sus periódicas crisis arancelarias, el bloque ha cumplido una labor civilizatoria invaluable al desterrar definitivamente las hipótesis de conflicto bélico entre las fuerzas armadas de las naciones partes, cimentando una zona de paz indestructible en el corazón de América del Sur. En última instancia, el destino del Cono Sur radica en perfeccionar sus cadenas de valor compartidas, demostrando que solo una integración solidaria entre iguales permitirá a nuestros pueblos hablar con voz propia y soberana en el tablero multipolar del siglo veintiuno."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿En qué año y mediante qué documento fundacional se constituyó el Mercado Común del Sur (Mercosur)?",
                        "options": [
                            "En 1980 mediante el Tratado de Montevideo de la ALADI.",
                            "En 1991 mediante la firma del Tratado de Asunción por parte de cuatro repúblicas del Cono Sur.",
                            "En 2010 mediante el Protocolo de Ushuaia sobre compromiso democrático.",
                            "En 1973 a través del Acuerdo de Cartagena para la integración andina."
                        ],
                        "correctIndex": 1,
                        "explanation": "El Mercosur se fundó formalmente el 26 de marzo de 1991 con la suscripción del Tratado de Asunción por Argentina, Brasil, Paraguay y Uruguay."
                    },
                    {
                        "question": "¿Cuál es la función primordial del Fondo para la Convergencia Estructural del Mercosur (FOCEM)?",
                        "options": [
                            "Financiar campañas electorales en las capitales de los Estados partes.",
                            "Aportar recursos financieros solidarios para reducir las asimetrías de infraestructura y desarrollo entre economías grandes y pequeñas del bloque.",
                            "Comprar armamento naval para patrullar el Atlántico sur.",
                            "Monopolizar el comercio exterior de trigo y soja entre los países miembros."
                        ],
                        "correctIndex": 1,
                        "explanation": "El FOCEM financia infraestructura y desarrollo social en los socios menores (Paraguay y Uruguay) con aportes mayoritarios de Brasil y Argentina."
                    },
                    {
                        "question": "¿Qué debate recurrente divide las posturas de los socios respecto al Arancel Externo Común (AEC)?",
                        "options": [
                            "La conveniencia de flexibilizar el bloque para pactar tratados bilaterales extrarregionales frente a la defensa de la unión aduanera unificada.",
                            "La sustitución inmediata de todas las monedas nacionales por el dólar estadounidense.",
                            "La prohibición total del comercio agropecuario entre los cuatro países.",
                            "La demolición de todos los puentes fluviales fronterizos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El debate central gira entre flexibilizar la regla de consenso para pactar con terceros países o mantener la unión aduanera como bloque común."
                    }
                ]
            }
        }
    },
    "world/b2/b2-integracion-02": {
        "id": "b2-integracion-02",
        "title": "La Alianza del Pacífico y la integración abierta al Asia",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "El modelo de integración pragmática y abierta de la Alianza del Pacífico: la Declaración de Lima de 2011 entre Chile, Colombia, México y Perú, la libre circulación de bienes, capitales y personas, el Mercado Integrado Latinoamericano (MILA) y el viraje estratégico hacia la cuenca del Asia-Pacífico.",
        "characters": [
            "Ministros de Relaciones Exteriores y de Comercio Exterior de los cuatro países fundadores",
            "Inversionistas y analistas de las bolsas de valores agrupadas en el MILA",
            "Exportadores de productos agroindustriales y minerales hacia los puertos asiáticos"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "El 28 de abril de 2011, en la histórica capital peruana, los jefes de Estado de Chile, Colombia, México y Perú suscribieron la Declaración de Lima, sentando las bases constitutivas de la Alianza del Pacífico, una iniciativa de integración económica de nuevo cuño orientada decididamente hacia el libre comercio, la atracción masiva de inversiones foráneas y la articulación competitiva con la dinámica cuenca del Asia-Pacífico. A diferencia de los esquemas integracionistas tradicionales de corte estatista y proteccionista que habían predominado en América Latina durante el siglo precedente, este bloque nació con una estructura deliberadamente ágil, flexible y desprovista de pesadas burocracias supranacionales permanentes, apostando por la desgravación arancelaria universal e inmediata de más del noventa y dos por ciento del universo de bienes y servicios comerciados entre las cuatro naciones partes."
            },
            {
                "type": "narration",
                "text": "Los pilares esenciales consagrados en el Protocolo Adicional de la Alianza abarcan cuatro libertades fundamentales: la libre circulación de bienes, servicios, capitales y personas a través de las fronteras compartidas. En el ámbito migratorio y turístico, los Estados miembros acordaron la exoneración total de visas de corta duración para sus ciudadanos respectivos y establecieron mecanismos de cooperación consular mancomunada, permitiendo que una embajada de cualquiera de los cuatro países en el extranjero preste asistencia diplomática a los nacionales de los otros tres socios. Asimismo, en el plano educativo, la creación de la Plataforma de Movilidad Estudiantil y Académica ha otorgado miles de becas completas para que jóvenes universitarios cursen semestres en prestigiosas facultades de los países socios, mientras que la apertura de embajadas y oficinas comerciales conjuntas en capitales de África y Asia optimizó significativamente los gastos del servicio exterior compartido."
            },
            {
                "type": "narration",
                "text": "Uno de los hitos financieros más vanguardistas del mecanismo fue la creación y puesta en marcha del Mercado Integrado Latinoamericano (MILA), una plataforma bursátil interconectada que integró en una sola pantalla electrónica las operaciones de las bolsas de valores de Santiago, Bogotá, Lima y la Bolsa Mexicana de Valores. A través de este sistema transfronterizo, cualquier inversionista particular o fondo de pensiones de los países miembros puede comprar y vender acciones listadas en las cuatro plazas financieras locales en moneda nacional y en tiempo real, dotando a la región del mercado bursátil de renta variable más grande de América Latina por número de emisores cotizados y atrayendo ingentes capitales institucionales globales interesados en diversificar sus carteras. Asimismo, los supervisores bancarios avanzaron en la homologación de marcos regulatorios para las tecnologías financieras ('fintech') y en el reconocimiento mutuo de firmas digitales transfronterizas para el comercio electrónico."
            },
            {
                "type": "narration",
                "text": "No obstante sus notables avances mercantiles y su reputación internacional de eficiencia institucional, la Alianza del Pacífico no ha permanecido inmune a tensiones geopolíticas derivadas de las alternancias partidarias y discrepancias ideológicas entre los gobiernos de turno en Lima, Bogotá y Ciudad de México. Además, diversos analistas y líderes gremiales han advertido que el bloque debe superar el extractivismo primario-exportador que aún caracteriza sus envíos hacia China, Japón y Corea del Sur —concentrados primordialmente en cobre refinado, petróleo crudo y harinas de pescado— para fomentar cadenas regionales de valor con mayor densidad tecnológica, innovación digital compartida y valor agregado científico en sectores estratégicos como la biotecnología médica y las energías limpias. Por ende, los ministros acordaron crear un fondo de capital de riesgo compartido para financiar emprendimientos de base tecnológica orientados a la exportación de servicios digitales a mercados del sudeste asiático."
            },
            {
                "type": "narration",
                "text": "En suma, la Alianza del Pacífico constituye un laboratorio imprescindible de modernización económica que ha demostrado la viabilidad de un regionalismo abierto, pragmático y orientado hacia los grandes motores del crecimiento mundial del siglo veintiuno. Al conjugar la disciplina fiscal con la libertad comercial y la armonización regulatoria, los cuatro países ribereños del océano Pacífico han construido un puente transoceánico de prosperidad que complementa fructíferamente los esfuerzos integracionistas de la cuenca atlántica. En última instancia, la convergencia virtuosa entre la Alianza del Pacífico y el Mercosur representará la clave maestra para que América del Sur y México actúen como un verdadero bloque bioceánico unido, capaz de liderar el diálogo global sobre el desarrollo sostenible y la paz."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué cuatro países fundaron la Alianza del Pacífico en 2011 mediante la Declaración de Lima?",
                        "options": [
                            "Argentina, Brasil, Bolivia y Uruguay.",
                            "Chile, Colombia, México y Perú.",
                            "Venezuela, Ecuador, Cuba y Nicaragua.",
                            "Costa Rica, Panamá, Honduras y Guatemala."
                        ],
                        "correctIndex": 1,
                        "explanation": "La Alianza del Pacífico fue conformada por Chile, Colombia, México y Perú como bloque de libre comercio orientado a la cuenca asiática."
                    },
                    {
                        "question": "¿En qué consiste la plataforma bursátil denominada Mercado Integrado Latinoamericano (MILA)?",
                        "options": [
                            "En una moneda física única de oro acuñada conjuntamente por los cuatro bancos centrales.",
                            "En la integración electrónica de las bolsas de valores de Santiago, Bogotá, Lima y México para operar acciones de forma cruzada.",
                            "En una compañía naviera estatal que transporta contenedores hacia Tokio.",
                            "En un impuesto aduanero especial que penaliza las inversiones extranjeras."
                        ],
                        "correctIndex": 1,
                        "explanation": "El MILA unifica los mercados de capitales de los cuatro socios facilitando la compraventa cruzada de acciones sin barreras cambiarias."
                    },
                    {
                        "question": "¿Cuál es uno de los principales retos estructurales señalados por los expertos para la Alianza del Pacífico?",
                        "options": [
                            "Acelerar la venta de materias primas sin procesar hacia los mercados de Asia.",
                            "Diversificar sus exportaciones hacia productos manufacturados con mayor valor agregado tecnológico e innovación compartida.",
                            "Cerrar las fronteras marítimas al transporte comercial internacional.",
                            "Imponer visados obligatorios de entrada a todos los turistas del bloque."
                        ],
                        "correctIndex": 1,
                        "explanation": "El reto consiste en superar la matriz primario-exportadora minera y agrícola mediante cadenas de valor tecnológicas regionales."
                    }
                ]
            }
        }
    },
    "world/b2/b2-integracion-03": {
        "id": "b2-integracion-03",
        "title": "Corredores bioceánicos: Uniendo el Atlántico y el Pacífico",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La infraestructura física y los corredores multimodales que vencen la barrera geográfica andina: la ferrovía bioceánica Paranaguá-Santos-Santa Cruz-Ilo/Matarani, la Carretera Interoceánica Brasil-Perú, los pasos cordilleranos de alta montaña y el megapuerto de Chancay como nuevo nodo transpacífico.",
        "characters": [
            "Ingenieros viales y ferroviarios de los proyectos bioceánicos de América del Sur",
            "Capitanes de navíos de carga y operadores portuarios de Chancay y Santos",
            "Transportistas internacionales que cruzan los pasos cordilleranos andinos"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A lo largo de cinco siglos de historia compartida, la monumental geografía física de América del Sur —dominada por la colosal muralla geológica de la cordillera de los Andes que se eleva a más de seis mil metros de altitud y por la inmensidad selvática de la llanura amazónica— funcionó como una barrera orográfica formidable que mantuvo a los países del Atlántico y del Pacífico de espaldas entre sí, obligando a las flotas comerciales a circunnavegar las gélidas y peligrosas aguas del cabo de Hornos o a cruzar el canal de Panamá para acceder a los mercados mundiales. Sin embargo, en el siglo veintiuno, la necesidad inaplazable de abaratar costos logísticos y acelerar los plazos de envío hacia los puertos de China, Japón y el sudeste asiático impulsó una de las transformaciones de ingeniería civil más titánicas del planeta: la construcción de los corredores bioceánicos de integración física multimodal."
            },
            {
                "type": "narration",
                "text": "Entre las iniciativas de mayor envergadura estratégica destaca el Corredor Ferroviario Bioceánico Central (CFBC), una ambiciosa red ferroviaria diseñada para conectar el puerto brasileño de Santos sobre el océano Atlántico con los puertos peruanos de Ilo y Matarani en el océano Pacífico, transitando a lo largo de más de tres mil setecientos kilómetros a través del territorio mediterráneo de Bolivia. Al atravesar los llanos de Santa Cruz de la Sierra, ascender por el altiplano andino y descender hacia la costa peruana, este ferrocarril multimodal permitirá reducir en más de quince días el trayecto marítimo de millones de toneladas de soja, carnes refrigeradas y minerales brasileños y bolivianos destinados a Shanghái, evitando el cuello de botella del canal de Panamá y democratizando el acceso marítimo soberano del corazón continental. Asimismo, la integración del sistema ferroviario con la Hidrovía Paraguay-Paraná facilitará el trasbordo eficiente de barcazas graneleras procedentes de los valles agrícolas más fértiles del Cono Sur."
            },
            {
                "type": "narration",
                "text": "De manera paralela, la Carretera Interoceánica que vincula el estado brasileño de Acre con los terminales costeros de San Juan de Marcona, Matarani e Ilo en el sur del Perú representó un hito histórico de integración vial asfaltada a través de la selva de Madre de Dios y los pasos andinos de más de cuatro mil setecientos metros en Puno y Cusco. Si bien este corredor carretero requirió ingentes inversiones financieras y demandó medidas de mitigación socioambiental rigurosas para salvaguardar las reservas indígenas y los bosques vírgenes colindantes, demostró de forma concluyente que las fronteras fluviales y montañosas pueden transformarse en avenidas dinámicas de tránsito comercial y turismo recíproco que dinamizan las economías locales más apartadas."
            },
            {
                "type": "narration",
                "text": "En el sector meridional del continente, los pasos cordilleranos de alta montaña como el Paso Internacional Los Libertadores (entre Santiago de Chile y Mendoza, Argentina) y el Paso de Jama (entre el norte argentino y el puerto chileno de Antofagasta) canalizan cotidianamente caravanas interminables de camiones de carga pesada que transportan granos, manufacturas industriales y ganado en pie. No obstante, las intensas nevadas invernales que clausuran temporalmente estos pasos viales a gran altura han reactivado el interés por construir túneles de baja altura que perforen la roca andina a cota constante, asegurando un flujo de mercancías ininterrumpido durante los trescientos sesenta y cinco días del año independientemente de los rigores climáticos extremos. Proyectos emblemáticos como el túnel binacional de Agua Negra entre la provincia argentina de San Juan y la región chilena de Coquimbo simbolizan esta determinación técnica de horadar la montaña para unir a los pueblos."
            },
            {
                "type": "narration",
                "text": "La cúspide de esta nueva geografía logística se materializa en la inauguración del megapuerto de Chancay, ubicado a ochenta kilómetros al norte de Lima: una terminal portuaria multipropósito de aguas profundas dotada de un calado de casi dieciocho metros y grúas automatizadas de última generación capaces de recibir a los portacontenedores más descomunales del mundo. Al constituirse en el principal puerto 'hub' concentrador de la costa pacífica suramericana con conexión directa hacia Asia sin escalas intermedias, Chancay magnetiza las cargas de todo el continente, reduciendo los tiempos de travesía transpacífica a solo veinticinco días. En definitiva, los corredores bioceánicos no son meras cintas de asfalto o acero; son los puentes fraternos que integran físicamente a América del Sur en una sola patria continental abierta a los vientos del porvenir."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué objetivo primordial persiguen los corredores bioceánicos en América del Sur?",
                        "options": [
                            "Aislar por completo a los países andinos del comercio marítimo internacional.",
                            "Unir físicamente los puertos del océano Atlántico con los del océano Pacífico para abaratar costos logísticos y acelerar exportaciones hacia Asia.",
                            "Construir murallas fronterizas en la cima de la cordillera de los Andes.",
                            "Sustituir el transporte marítimo de contenedores por avionetas privadas de pasajeros."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los corredores bioceánicos unen ambos océanos reduciendo semanas de navegación hacia los mercados del Pacífico y Asia."
                    },
                    {
                        "question": "¿Qué país suramericano sin litoral marítimo ocupa una posición geográfica clave en el Corredor Ferroviario Bioceánico Central?",
                        "options": [
                            "Paraguay.",
                            "Bolivia, al vincular las redes de Brasil con los puertos del sur del Perú.",
                            "Uruguay.",
                            "Guyana."
                        ],
                        "correctIndex": 1,
                        "explanation": "Bolivia articula el trayecto ferroviario entre los estados agrícolas de Brasil y los puertos del Pacífico peruano."
                    },
                    {
                        "question": "¿Qué ventaja logística decisiva aporta el megapuerto de Chancay en la costa pacífica suramericana?",
                        "options": [
                            "Es un puerto exclusivo para la pesca de truchas de agua dulce.",
                            "Ofrece aguas profundas para gigantescos buques y conexión directa hacia Asia, reduciendo la travesía transpacífica a solo veinticinco días.",
                            "Prohíbe el atraque de buques mercantes con bandera extranjera.",
                            "Opera únicamente con carretas de tracción animal sobre la arena."
                        ],
                        "correctIndex": 1,
                        "explanation": "Chancay opera como puerto concentrador de aguas profundas reduciendo en diez o más días la ruta directa hacia Asia."
                    }
                ]
            }
        }
    },
    "world/b2/b2-integracion-04": {
        "id": "b2-integracion-04",
        "title": "Energía compartida: Itaipú, Yacyretá y las redes binacionales",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La integración energética continental a través de colosos hidroeléctricos binacionales: la central de Itaipú (Brasil-Paraguay) sobre el río Paraná, la represa de Yacyretá (Argentina-Paraguay), la renegociación del Anexo C del tratado, el gasoducto GASBOL y la interconexión de redes eléctricas.",
        "characters": [
            "Ingenieros directores de Itaipú Binacional y de la Entidad Binacional Yacyretá",
            "Diplomáticos y técnicos del sector energético de Brasil, Paraguay y Argentina",
            "Especialistas en redes eléctricas de alta tensión y transición hacia energías limpias"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el corazón hídrico de la cuenca del Plata, donde el majestuoso río Paraná marca el límite soberano entre repúblicas hermanas, se alzan dos de los monumentos de ingeniería hidroeléctrica más imponentes y prolíficos de la civilización contemporánea: la central hidroeléctrica de Itaipú, administrada en condominio indiviso por Brasil y Paraguay, y la represa de Yacyretá, gestionada de forma binacional entre Argentina y Paraguay. Nacidas de tratados diplomáticos pioneros suscritos en la década de 1970 —en momentos en que la geopolítica regional estaba dominada por viejas desconfianzas territoriales y rivalidades por el control de las aguas—, estas megaestructuras demostraron que los caudales compartidos no debían ser motivo de discordia militar, sino la fuente más formidable de energía renovable, limpia y barata para encender el desarrollo industrial de millones de hogares sudamericanos."
            },
            {
                "type": "narration",
                "text": "Con una capacidad instalada de catorce mil megavatios distribuidos en veinte gigantescas unidades generadoras y una producción acumulada que rebasa con holgura los tres mil millones de megavatios-hora desde su inauguración, Itaipú satisface históricamente cerca del ochenta y cinco por ciento de la demanda eléctrica total del Paraguay y alrededor del diez por ciento del consumo voraz del coloso brasileño. En virtud del Tratado de 1973, la energía generada se reparte estrictamente al cincuenta por ciento entre ambas naciones soberanas; sin embargo, al no poder absorber Paraguay la totalidad de su cuota debido a su menor desarrollo fabril, el país cede obligatoriamente su excedente energético al sistema interconectado brasileño a cambio de compensaciones financieras y regalías estipuladas en el tratado bilateral. Asimismo, la construcción de la línea de transmisión de quinientos kilovoltios entre Itaipú y la subestación de Villa Hayes ha permitido dotar al área metropolitana de Asunción de energía estable para alimentar flamantes parques industriales manufactureros."
            },
            {
                "type": "narration",
                "text": "En años recientes, el cumplimiento del plazo quincuagenario del tratado abrió un proceso histórico de renegociación diplomática en torno a las disposiciones financieras contenidas en el denominado 'Anexo C'. Las autoridades y la sociedad civil paraguaya han reclamado con firmeza el derecho soberano a comercializar libremente su excedente eléctrico en el mercado abierto brasileño a precios justos de mercado o a terceros países del Cono Sur, así como a utilizar esa energía limpia y abundante para atraer industrias electrointensivas de alta tecnología a su propio territorio. Por su parte, los negociadores brasileños coinciden en la conveniencia de preservar una tarifa competitiva que asegure la estabilidad financiera de la entidad binacional mientras se financian inversiones de modernización tecnológica digital en las turbinas."
            },
            {
                "type": "narration",
                "text": "De manera complementaria, la integración energética regional se fortaleció notablemente en el sector de los hidrocarburos a través del célebre Gasoducto Bolivia-Brasil (GASBOL), una arteria subterránea de más de tres mil ciento cincuenta kilómetros que desde fines de la década de 1990 transportó miles de millones de metros cúbicos de gas natural boliviano hacia los complejos termoeléctricos e industriales de São Paulo, Porto Alegre y Curitiba. Asimismo, los anillos de interconexión eléctrica de alta tensión construidos entre Argentina, Brasil, Uruguay y Paraguay han permitido realizar transferencias de socorro energético recíproco durante temporadas de sequía extrema o picos de frío invernal, evitando apagones masivos y garantizando la seguridad del suministro continental. En la actualidad, parques eólicos en la Patagonia argentina y colosales plantas solares fotovoltaicas en el desierto de Atacama se conectan progresivamente a estas mallas regionales, diversificando la matriz con fuentes no convencionales."
            },
            {
                "type": "narration",
                "text": "En conclusión, las hidroeléctricas binacionales y las redes interconectadas de gas y electricidad constituyen el sistema circulatorio que bombea vida y productividad a América del Sur. En una era planetaria signada por la urgencia de descarbonizar la matriz económica para frenar la catástrofe climática, nuestro continente goza del privilegio inmenso de poseer una de las matrices eléctricas más verdes y limpias del mundo gracias a sus caudales fluviales. En última instancia, avanzar hacia una verdadera gobernanza energética solidaria —donde la energía no sea una mercancía especulativa sino un derecho humano fundamental— representará la garantía más sólida para que nuestros pueblos alcancen la soberanía tecnológica y la justicia social en un Cono Sur fraternalmente integrado."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuáles son las dos grandes centrales hidroeléctricas binacionales situadas sobre el río Paraná?",
                        "options": [
                            "Guri (Venezuela) y Salto Grande (Uruguay).",
                            "Itaipú (Brasil-Paraguay) y Yacyretá (Argentina-Paraguay).",
                            "El Chocón (Argentina) y Furnas (Brasil).",
                            "Tres Gargantas y Asuán."
                        ],
                        "correctIndex": 1,
                        "explanation": "Itaipú y Yacyretá son los dos grandes colosos hidroeléctricos binacionales ubicados en el curso del río Paraná."
                    },
                    {
                        "question": "¿Qué establece el Tratado de Itaipú sobre la distribución y cesión de la energía generada?",
                        "options": [
                            "Que Brasil se queda con el cien por ciento de la electricidad sin pagar compensación alguna.",
                            "Que la energía se divide en partes iguales (cincuenta por ciento para cada socio) y Paraguay cede su excedente no utilizado a Brasil.",
                            "Que Paraguay debe vender su energía obligatoriamente a clientes de Europa.",
                            "Que la represa solo funciona durante los meses de primavera."
                        ],
                        "correctIndex": 1,
                        "explanation": "El tratado asigna el 50% a cada país y estipula la cesión del remanente paraguayo al mercado de Brasil."
                    },
                    {
                        "question": "¿Cuál es el debate neurálgico en la renegociación del 'Anexo C' del Tratado de Itaipú?",
                        "options": [
                            "La demolición inmediata del muro de hormigón de la central.",
                            "Las condiciones financieras de venta del excedente energético paraguayo y la fijación de tarifas de energía competitivas.",
                            "La privatización forzosa de los recursos pesqueros del lago artificial.",
                            "El desvío del cauce del río Paraná hacia el océano Pacífico."
                        ],
                        "correctIndex": 1,
                        "explanation": "El debate del Anexo C gira sobre el valor justo de compensación, la libre comercialización de excedentes y las tarifas."
                    }
                ]
            }
        }
    },
    "world/b2/b2-integracion-05": {
        "id": "b2-integracion-05",
        "title": "Hacia la ciudadanía suramericana: De UNASUR a la movilidad humana",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La construcción de una ciudadanía regional y la libre movilidad humana en América del Sur: el legado diplomático de UNASUR y la CELAC, el Acuerdo de Residencia del Mercosur, el libre tránsito con documento de identidad nacional, la convalidación universitaria de títulos y el sueño de la Patria Grande.",
        "characters": [
            "Trabajadores y profesionales migrantes beneficiarios del Acuerdo de Residencia",
            "Rectores y comisiones académicas de homologación universitaria suramericana",
            "Defensores de derechos humanos y juristas expertos en migración regional"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Más allá de las cifras macroeconómicas del comercio aduanero, las tarifas arancelarias preferenciales y las colosales obras de ingeniería energética o vial, la dimensión más noble, humanista y trascendente de cualquier proceso integrador radica en la condición concreta de las personas de carne y hueso: los millones de hombres y mujeres que cruzan las fronteras de América del Sur en busca de empleo digno, estudio superior, refugio político o reencuentro familiar. A diferencia de otras regiones del globo que reaccionan ante los flujos migratorios levantando muros de hormigón, vallas electrificadas y campos de detención securitizados, Suramérica forjó a lo largo del siglo veintiuno una doctrina migratoria pionera y progresista sustentada en el reconocimiento de la movilidad humana como un derecho inalienable."
            },
            {
                "type": "narration",
                "text": "La piedra angular jurídica de esta doctrina fue el histórico 'Acuerdo sobre Residencia para Nacionales de los Estados Partes del Mercosur y Asociados', adoptado en 2002 e incorporado gradualmente por Argentina, Brasil, Paraguay, Uruguay, Bolivia, Chile, Colombia, Ecuador y Perú. En virtud de este instrumento multilateral revolucionario, cualquier ciudadano oriundo de uno de estos países puede solicitar y obtener un permiso de residencia temporal por dos años en el territorio de cualquier otro Estado miembro acreditando simplemente su nacionalidad y la carencia de antecedentes penales graves, con derecho a transformarla en residencia permanente. Este estatus garantiza el acceso irrestricto al trabajo formal, a la seguridad social previsional, a la educación pública gratuita y a la salud hospitalaria en pie de igualdad con los ciudadanos nativos. Asimismo, el Convenio Multilateral de Seguridad Social del Mercosur consagró el principio de la totalización de aportes jubilatorios, garantizando que los años cotizados por un obrero en distintos países se reconozcan al calcular su pensión de retiro."
            },
            {
                "type": "narration",
                "text": "De forma simultánea, los convenios de facilitación fronteriza desterraron la exigencia decimonónica del pasaporte y la visa consular para el tránsito turístico y comercial ordinario dentro de la región. Hoy en día, un ciudadano suramericano puede viajar sin trabas burocráticas desde Bogotá o Lima hasta Buenos Aires, Montevideo o Río de Janeiro portando exclusivamente su cédula o documento nacional de identidad expedido por su país de origen. Del mismo modo, la instauración de la Patente Mercosur para automóviles particulares y camiones comerciales unificó el diseño de las matrículas vehiculares en todo el Cono Sur, facilitando la fiscalización vial conjunta, mientras que las Tarjetas Vecinales Fronterizas permiten a los pobladores de ciudades gemelas cruzar puentes binacionales por carriles aduaneros ágiles y exclusivos. A su vez, las defensorías del pueblo de los países miembros crearon una red conjunta para monitorear y garantizar el debido proceso legal a los ciudadanos detenidos en puestos de frontera."
            },
            {
                "type": "narration",
                "text": "En el terreno educativo y profesional, la integración avanzó mediante convenios de convalidación automática de títulos de grado y posgrado universitario, tales como el sistema ARCU-SUR (Acreditación Regional de Carreras Universitarias del Mercosur). Gracias a este riguroso marco de acreditación académica común, ingenieros, médicos, agrónomos y docentes egresados de facultades acreditadas en un país miembro pueden ejercer su profesión o continuar estudios de especialización en las universidades de los demás Estados sin tener que padecer extenuantes y costosos litigios de homologación burocrática, favoreciendo la circulación del talento científico y la fertilización cruzada del conocimiento en el continente. Asimismo, la armonización de normativas sobre ejercicio profesional y bioética médica permite a brigadas sanitarias actuar con celeridad ante desastres naturales en zonas limítrofes sin trabas de habilitación colegiada."
            },
            {
                "type": "narration",
                "text": "En conclusión, el camino hacia la ciudadanía suramericana y la integración de los pueblos rescata el sueño bicentenario de libertadores como Simón Bolívar, José de San Martín y José Gervasio Artigas: la visión imperecedera de una Patria Grande fraterna donde ningún latinoamericano sea tratado jamás como extranjero indeseable en su propia tierra ancestral. A pesar de los vaivenes ideológicos de los gobiernos y las disoluciones o reconstitución de organismos como UNASUR o la CELAC, los lazos humanos, culturales, familiares y afectivos que unen a nuestras sociedades son indestructibles. En última instancia, la ciudadanía compartida recuerda al mundo entero que la verdadera soberanía continental no se erige aislando a las naciones tras alambradas, sino abriendo los brazos fraternalmente para construir juntos un porvenir de dignidad, igualdad y paz."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué derecho trascendental consagra el Acuerdo sobre Residencia del Mercosur para los ciudadanos suramericanos?",
                        "options": [
                            "La exención vitalicia de cualquier pago de impuestos en su país natal.",
                            "La posibilidad de obtener residencia temporal y permanente en cualquier país suscriptor, accediendo al trabajo legal, la educación y la salud.",
                            "La obligación de servir en las fuerzas armadas del país receptor.",
                            "La prohibición de enviar remesas de dinero a sus familias de origen."
                        ],
                        "correctIndex": 1,
                        "explanation": "El acuerdo permite radicarse legalmente con plenos derechos laborales y sociales acreditando nacionalidad y carencia de antecedentes."
                    },
                    {
                        "question": "¿Qué documento basta presentar a un ciudadano suramericano para viajar por la mayor parte del subcontinente?",
                        "options": [
                            "Una visa consular de turista expedida en Ginebra.",
                            "Únicamente su cédula o documento nacional de identidad expedido por su país de origen.",
                            "Un certificado bancario de solvencia económica millonaria.",
                            "Una carta de recomendación de un presidente extranjero."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los acuerdos de facilitación suprimen el pasaporte y visados, exigiendo solo la cédula o DNI nacional para el libre tránsito."
                    },
                    {
                        "question": "¿Cuál es el objetivo del mecanismo ARCU-SUR en el ámbito educativo universitario?",
                        "options": [
                            "Cerrar las universidades públicas para reemplazarlas por academias privadas extranjeras.",
                            "Acreditar la calidad académica de las carreras para facilitar el reconocimiento y ejercicio profesional entre las naciones socias.",
                            "Prohibir el intercambio internacional de profesores y estudiantes.",
                            "Imponer un único manual de historia dictado por decreto ministerial."
                        ],
                        "correctIndex": 1,
                        "explanation": "ARCU-SUR acredita estándares universitarios para homologar títulos y promover la libre circulación de profesionales calificados."
                    }
                ]
            }
        }
    },
    "world/b2/b2-integracion-consolidation": {
        "id": "b2-integracion-consolidation",
        "title": "La arquitectura de la unidad suramericana: Puentes, tratados y porvenir",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Síntesis reflexiva sobre la integración integral de América del Sur: la complementariedad entre la unión aduanera del Mercosur y el regionalismo abierto de la Alianza del Pacífico, la superación física andina mediante corredores bioceánicos, la soberanía energética hidroeléctrica y el horizonte de la ciudadanía suramericana.",
        "characters": [
            "Ensayistas y cronistas del proceso de integración suramericano",
            "Trabajadores, científicos y comunidades ciudadanas como protagonistas de la integración"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al contemplar en su conjunto el mapa contemporáneo de América del Sur, con sus ríos colosales interconectados por represas binacionales, sus cordilleras andinas atravesadas por carreteras bioceánicas y sus ciudades fronterizas unidas por puentes de libre circulación ciudadana, se hace evidente que nuestro subcontinente ha dejado atrás para siempre la época de los compartimentos estancos y los recelos nacionalistas heredados de las fronteras coloniales. En primer término, la integración regional ya no es concebida como un experimento doctrinario abstracto reservado a las cancillerías ilustradas, sino como un imperativo geoeconómico, ecológico y social impostergable para garantizar la soberanía de cuatrocientos cincuenta millones de latinoamericanos en un orden mundial multipolar y convulso. Pensadores señeros del desarrollo como Raúl Prebisch y Celso Furtado desde la CEPAL ya advirtieron en su tiempo que la fragmentación periférica perpetuaba el deterioro de los términos de intercambio comercial."
            },
            {
                "type": "narration",
                "text": "A través de la dialéctica fructífera entre el modelo aduanero productivo del Mercosur y el esquema de apertura comercial y facilitación bursátil de la Alianza del Pacífico, la región ha madurado sus herramientas de inserción global. Lejos de constituir proyectos antagónicos e irreconciliables, ambas iniciativas demuestran una complementariedad estratégica indispensable: mientras el Mercosur aporta la densidad de su mercado interno fabril y agroalimentario en la cuenca del Plata, la Alianza del Pacífico proyecta las cadenas de valor compartidas hacia las economías más dinámicas de Asia. Por añadidura, mecanismos de convergencia estructural como el FOCEM evidencian que el crecimiento económico genuino solo es duradero si se acompaña de solidaridad activa hacia las regiones y economías con mayores asimetrías de partida. Asimismo, el diálogo entre los organismos de integración técnica y los parlamentos regionales consolida una diplomacia parlamentaria plural que canaliza las demandas ciudadanas hacia las cumbres presidenciales periódicas."
            },
            {
                "type": "narration",
                "text": "Asimismo, la integración física y energética ha dejado de ser una quimera técnica para encarnarse en realidades de hormigón, acero y electricidad limpia que transforman cotidianamente la vida material de los pueblos. Corredores bioceánicos de vanguardia, ferrovías transcontinentales y terminales marítimas de clase mundial como el megapuerto de Chancay acortan drásticamente las distancias con los centros del consumo global, permitiendo al corazón continental de Bolivia y el Chaco superar su histórico aislamiento mediterráneo. Del mismo modo, colosos hidroeléctricos como Itaipú y Yacyretá, sumados a las redes interconectadas de gas y líneas de alta tensión, aseguran una matriz energética limpia, soberana y solidaria que protege a los países del Cono Sur frente a las crisis de abastecimiento internacional. Por si fuera poco, el despliegue de cables de fibra óptica submarinos y terrestres que interconectan a las capitales suramericanas asegura soberanía comunicacional digital a escala regional."
            },
            {
                "type": "narration",
                "text": "No obstante la solidez de estas infraestructuras materiales, el alma imperecedera del proyecto integracionista reside en la progresiva consagración de la ciudadanía suramericana y la libre movilidad humana. El Acuerdo de Residencia del Mercosur, el tránsito fronterizo sin pasaportes y la convalidación universitaria de títulos a través de redes como ARCU-SUR demuestran que las fronteras nacionales pueden transformarse de barreras represivas en umbrales fraternos de encuentro y cooperación. En este horizonte humano, el migrante no es un intruso amenazante, sino un compatriota continental que aporta su esfuerzo laboral, su creatividad científica y su riqueza cultural a la construcción de un destino colectivo compartido. Por añadidura, el enriquecimiento mutuo de las literaturas, el cine y la música popular teje una sensibilidad compartida que reconoce la unidad profunda en la deslumbrante diversidad cultural del continente."
            },
            {
                "type": "narration",
                "text": "En suma, quien recorre hoy las avenidas de Asunción, las orillas del Plata en Montevideo y Buenos Aires, las alturas de La Paz o los muelles de Santos y Chancay comprende que en América del Sur late con fuerza inextinguible el mandato de los libertadores de nuestra primera emancipación. La unidad regional no implica la uniformidad asfixiante de las identidades locales, sino la polifonía armónica de culturas hermanadas por una memoria común y una vocación compartida de libertad, democracia y justicia social. En última instancia, perfeccionar esta arquitectura integradora —derribando los prejuicios del pasado y tendiendo puentes de solidaridad entre el Atlántico y el Pacífico— es la tarea más excelsa a la que pueden consagrarse las nuevas generaciones de la Patria Grande."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué relación estratégica virtuosa se percibe hoy entre el Mercosur y la Alianza del Pacífico?",
                        "options": [
                            "Una guerra comercial destructiva que paraliza todas las aduanas del continente.",
                            "Una complementariedad entre la fuerza del mercado interno atlántico y la proyección comercial pacífica hacia los mercados de Asia.",
                            "La fusión inmediata en una sola monarquía parlamentaria absolutista.",
                            "La cancelación de todos los acuerdos arancelarios previos."
                        ],
                        "correctIndex": 1,
                        "explanation": "Ambos bloques se complementan uniendo la potencia productiva del Cono Sur con la apertura transpacífica hacia los mercados asiáticos."
                    },
                    {
                        "question": "¿De qué manera benefician los corredores bioceánicos a los países mediterráneos como Bolivia?",
                        "options": [
                            "Obligándolos a importar exclusivamente mercancías transportadas en aviones supersónicos.",
                            "Proporcionándoles una salida multimodal eficiente y económica hacia los puertos del Pacífico y del Atlántico para sus exportaciones.",
                            "Clausurando todas sus conexiones carreteras con los países limítrofes.",
                            "Exigiéndoles el pago de aranceles punitivos en cada frontera fluvial."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los corredores ferroviarios y viales otorgan salida soberana y competitiva a los productos bolivianos hacia ambos océanos."
                    },
                    {
                        "question": "¿Cuál es la premisa ética fundamental que sustenta la ciudadanía suramericana y el Acuerdo de Residencia?",
                        "options": [
                            "Considerar al habitante migrante suramericano como un compatriota continental con plenos derechos en una Patria Grande compartida.",
                            "Restringir la educación y la salud exclusivamente a quienes hayan nacido dentro de la capital receptora.",
                            "Exigir visados millonarios y expulsar a los trabajadores extranjeros de escasos recursos.",
                            "Prohibir el matrimonio entre personas de distintas nacionalidades de la región."
                        ],
                        "correctIndex": 0,
                        "explanation": "La ciudadanía regional concibe al migrante como titular inalienable de derechos en un espacio continental de dignidad compartida."
                    }
                ]
            }
        }
    },
    "world/b2/b2-integracion": {
        "id": "b2-integracion",
        "title": "Integración regional, corredores bioceánicos y energía compartida",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 20,
        "summary": "Compendio general y panorámico sobre la integración integral de América del Sur: la evolución institucional desde el Mercosur y la Alianza del Pacífico, la superación de la barrera andina mediante corredores bioceánicos, la soberanía hidroeléctrica compartida de Itaipú y Yacyretá, y el avance hacia una ciudadanía suramericana fraterna.",
        "characters": [
            "Líderes de Estado y ministros de los países suramericanos",
            "Ingenieros viales, portuarios y energéticos de las obras binacionales",
            "Operadores financieros y comerciales de las redes de integración",
            "Ciudadanos y estudiantes en libre movilidad transfronteriza"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A lo largo de las vastas geografías de América del Sur, donde la cordillera de los Andes se eleva como un espinazo colosal entre dos océanos infinitos y los ríos titánicos de las cuencas del Amazonas, del Orinoco y del Plata riegan millones de kilómetros cuadrados de tierras feraces, florece hoy una de las transformaciones geopolíticas más trascendentes de nuestro tiempo: la integración integral suramericana. Superando siglos de fragmentación política, aislamiento territorial y viejas hipótesis de recelo militar alimentadas durante los períodos autoritarios, los pueblos y Estados de la región han comprendido que en el escenario multipolar del siglo veintiuno ningún país aislado puede aspirar al desarrollo pleno. Por consiguiente, articular esfuerzos productivos, infraestructuras físicas y soberanías compartidas constituye la única garantía irrenunciable para asegurar el bienestar colectivo y la paz continental."
            },
            {
                "type": "narration",
                "text": "En el terreno institucional y comercial, esta vocación mancomunada se expresa a través de dos vertientes complementarias que tienden puentes fecundos entre ambas costas marítimas: el Mercado Común del Sur (Mercosur), fundado en 1991 mediante el Tratado de Asunción para edificar una unión aduanera sólida y solidaria respaldada por el Fondo de Convergencia Estructural (FOCEM), y la Alianza del Pacífico, surgida en 2011 como un bloque ágil y pragmático orientado hacia el libre comercio, la integración bursátil del MILA y la proyección competitiva hacia la cuenca del Asia-Pacífico. Al coordinar normativas aduaneras, armonizar normas de origen y promover la acumulación productiva transfronteriza, ambos esquemas demuestran que el comercio regional debe funcionar como un motor distributivo que estimule la industrialización limpia y el empleo formal digno. De igual manera, programas de fomento a las pequeñas y medianas empresas (PyMEs) facilitan la inserción de cooperativas campesinas y manufactureras locales en las cadenas transandinas de exportación."
            },
            {
                "type": "narration",
                "text": "De manera paralela, la integración física vence el desafío histórico de la orografía mediante los ambiciosos corredores bioceánicos de transporte multimodal, diseñados para unir los puertos atlánticos como Santos y Paranaguá con las dársenas del Pacífico como Ilo, Matarani y el megapuerto de Chancay. La ferrovía bioceánica central que atraviesa los llanos y el altiplano de Bolivia, junto a los pasos andinos asfaltados como Los Libertadores y Jama, reduce en semanas los fletes marítimos hacia las metrópolis asiáticas, rompiendo el secular enclaustramiento de los territorios mediterráneos. Asimismo, terminales de aguas profundas dotadas de automatización tecnológica de última generación convierten a la costa pacífica suramericana en un nodo logístico planetario de primera línea capaz de canalizar el dinamismo agropecuario y manufacturero del continente."
            },
            {
                "type": "narration",
                "text": "En el sector de los recursos estratégicos, la soberanía energética compartida se erige como un baluarte de resiliencia civilizatoria a través de hidroeléctricas binacionales sin paralelo mundial: la represa de Itaipú entre Brasil y Paraguay, y la central de Yacyretá entre Argentina y Paraguay, ambas situadas sobre el caudal portentoso del río Paraná. Al aportar energía limpia, renovable y de bajísimo impacto de carbono a los sistemas productivos metropolitanos, estos colosos fluviales —junto a los gasoductos binacionales como el GASBOL y las redes de interconexión eléctrica de socorro mutuo— garantizan la seguridad energética de cientos de millones de latinoamericanos, demostrando que la cooperación interestatal genera beneficios colectivos infinitamente superiores a la explotación individualista de los recursos. En años recientes, alianzas trilaterales para la industrialización sostenible del litio en el triángulo salinero andino y proyectos de hidrógeno verde consolidan la vanguardia de la transición ecológica justa."
            },
            {
                "type": "narration",
                "text": "En conclusión, el cimiento ético y la cumbre luminosa de esta epopeya integradora descansa en la consagración de la ciudadanía suramericana y la libre movilidad de las personas de nuestra Patria Grande. El Acuerdo de Residencia del Mercosur, la supresión de visas y pasaportes para el tránsito ordinario con cédula de identidad, y la convalidación de títulos universitarios a través del sistema ARCU-SUR demuestran que la integración verdadera no se reduce al movimiento de mercancías y capitales financieros, sino a la fraternidad indivisible entre seres humanos que comparten raíces, anhelos y esperanzas. Al asumir unidos este legado histórico bolivariano y sanmartiniano, las naciones suramericanas declaran al mundo entero que su destino es marchar unidas hacia un porvenir de dignidad, igualdad y paz indestructible."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis estratégica define hoy la articulación económica entre el Atlántico y el Pacífico en América del Sur?",
                        "options": [
                            "La clausura total de las rutas de navegación fluvial entre países vecinos.",
                            "La convergencia entre la solidez productiva del Mercosur y la apertura transpacífica de la Alianza del Pacífico apoyada en corredores bioceánicos.",
                            "El abandono de todas las iniciativas comerciales a favor de corporaciones privadas foráneas.",
                            "La instauración de aranceles punitivos del cien por ciento a todos los productos agropecuarios."
                        ],
                        "correctIndex": 1,
                        "explanation": "La articulación regional combina la fuerza manufacturera del Cono Sur con la proyección bioceánica hacia el comercio global."
                    },
                    {
                        "question": "¿Qué aporte vital ofrecen las represas binacionales de Itaipú y Yacyretá a la matriz energética suramericana?",
                        "options": [
                            "Generan hidroelectricidad limpia, renovable y masiva para alimentar el desarrollo fabril y residencial de varias naciones hermanas.",
                            "Consumen carbón mineral altamente contaminante importado del Polo Norte.",
                            "Operan como refinerías exclusivas de petróleo pesado para la exportación.",
                            "Desecan los cursos de agua provocando la pérdida permanente de caudales fluviales."
                        ],
                        "correctIndex": 0,
                        "explanation": "Itaipú y Yacyretá proveen energía renovable a gran escala a Brasil, Paraguay y Argentina descarbonizando la matriz productiva."
                    },
                    {
                        "question": "¿Por qué se afirma que la ciudadanía suramericana y la libre movilidad son la cumbre ética del proceso de integración?",
                        "options": [
                            "Porque colocan la dignidad y los derechos fundamentales de las personas y familias por encima de las meras transacciones mercantiles y aduaneras.",
                            "Porque obligan a todos los ciudadanos a renunciar a sus tradiciones culturales locales.",
                            "Porque suprimen los idiomas originarios de los pueblos indígenas.",
                            "Porque restringen la educación a los sectores más adinerados de las capitales."
                        ],
                        "correctIndex": 0,
                        "explanation": "La ciudadanía regional prioriza la fraternidad humana, el libre tránsito y el acceso equitativo a derechos laborales y sociales."
                    }
                ]
            }
        }
    }
}

print("Testing all 8 stories in make_unit33_stories:")
all_valid = True
for k, v in STORIES.items():
    full_text = " ".join(p["text"] for p in v["paragraphs"])
    cnt = word_count(full_text)
    is_valid = 650 <= cnt <= 825
    if not is_valid:
        all_valid = False
    print(f"  {k}: {cnt} words (valid: {is_valid})")

print(f"All stories valid: {all_valid}")
