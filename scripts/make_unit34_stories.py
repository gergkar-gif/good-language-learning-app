"""
make_unit34_stories.py
Defines the 8 stories for Unit 34 and tests word counts.
"""
import re
import json

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

STORIES = {
  "classics/b2/b2-34": {
    "id": "b2-34",
    "title": "Redoble por Rancas (Manuel Scorza, 1970)",
    "level": "B2",
    "lesson": 1,
    "type": "classics",
    "estimatedMinutes": 15,
    "summary": "Estudio literario e histórico de la novela 'Redoble por Rancas' de Manuel Scorza: la insurrección de los campesinos comuneros de Rancas en Cerro de Pasco, el mito del cercado de alambre de púas de la compañía norteamericana, el heroísmo de Héctor Chacón 'el Nictálope', y la denuncia del gamonalismo judicial y terrateniente en los Andes peruanos.",
    "characters": [
      "Héctor Chacón, 'el Nictálope' (jinete comunero dotado de visión nocturna y líder rebelde)",
      "Fortunato (comunero anciano símbolo de la memoria y la dignidad de la tierra)",
      "El Juez Montenegro (magistrado despótico que personifica la arbitrariedad gamonal)",
      "Los comuneros de Rancas, Yanahuanca y las punas de Cerro de Pasco",
      "La Cerro de Pasco Copper Corporation y los destacamentos de la Guardia Republicana"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Publicada en Barcelona en 1970 tras años de exilio político, 'Redoble por Rancas' constituye la primera entrega del célebre ciclo narrativo 'La Guerra Callada' del insigne poeta y novelista peruano Manuel Scorza. En esta obra cumbre del neoindigenismo hispanoamericano, Scorza rescata del olvido deliberado de la historia oficial la heroica y trágica rebelión campesina ocurrida a inicios de los años sesenta en las gélidas punas mineras del departamento de Pasco, en los Andes centrales del Perú. Lejos de concebir su relato como un panfleto sociológico frío o un testimonio documental ascético, el autor funde con maestría poética el rigor histórico más documentado con la exuberancia mitológica del imaginario andino, creando una atmósfera de realismo mágico combatiente donde la naturaleza, los presagios y la cosmovisión quechua participan activamente en la resistencia desesperada de los comuneros frente a la voracidad del despojo."
      },
      {
        "type": "narration",
        "text": "El conflicto central de la novela estalla con la llegada insidiosa, casi sobrenatural, de un enemigo metálico y desmesurado: el gigantesco cerco de alambre de púas desplegado por la poderosa compañía minera transnacional Cerro de Pasco Copper Corporation. Como si fuera una serpiente de acero dotada de apetito insaciable y vida propia autónoma, el cercado avanza día y noche por las mesetas de Rancas devorando pastizales comunales milenarios, cerrando caminos de herradura ancestrales, secando manantiales vitales y encarcelando a los rebaños de ovejas y alpacas de los indígenas bajo la vigilancia armada de capataces foráneos. De pronto, los comuneros descubren con angustia e indignación que para transitar de una choza a otra o para llevar a abrevar a su ganado deben pagar peajes abusivos o resignarse a contemplar cómo sus animales mueren electrocutados o atrapados en las púas del alambre."
      },
      {
        "type": "narration",
        "text": "Frente a esta invasión capitalista rapaz, el poder estatal y judicial no actúa como un árbitro ecuánime ni como un protector de los desposeídos, sino como el cómplice servil y despiadado del despojo de tierras. Esta opresión institucional se encarna de manera grotesca e hiperbólica en la temible figura del Juez de Primera Instancia Francisco Montenegro: un gamonal despótico y soberbio que tiraniza a toda la provincia de Yanahuanca con arbitrariedad monárquica. Es célebre en la trama el episodio de la moneda caída en el fango de la plaza mayor: cuando el juez Montenegro pierde una moneda de plata al descender de su caballo, nadie en el pueblo se atreve a tocarla ni a recogerla durante meses por temor a ser acusado de insolencia o desacato, transformando aquel objeto olvidado en un monumento silencioso al terror reverencial y la sumisión colonial."
      },
      {
        "type": "narration",
        "text": "Cansados de acudir en vano a despachos ministeriales en Lima para exhibir títulos virreinales de propiedad comunal firmados por reyes españoles que la burocracia limeña ignora con desprecio racista, los campesinos de Rancas deciden empuñar las armas bajo la conducción de un jinete legendario: Héctor Chacón, apodado 'el Nictálope' por su asombrosa facultad fisiológica de ver en la oscuridad más cerrada de las noches andinas. Guiados por Chacón y por el anciano Fortunato, los comuneros cortan el alambre opresor con cizallas improvisadas y recuperan a medianoche sus tierras ancestrales en una gesta colectiva de soberanía popular. Durante semanas luminosas, las familias campesinas siembran y pastan en libertad, desafiando a las autoridades prefecturales y reanudando los ritos comunitarios de hermandad agraria que el cercado había interrumpido brutalmente."
      },
      {
        "type": "narration",
        "text": "Empero, la represalia oligárquica no tarda en desencadenarse con ferocidad implacable: en marzo de 1962, batallones fuertemente pertrechados de la Guardia Republicana y policías de asalto cercan las alturas de Rancas y desatan una masacre sangrienta contra hombres, mujeres y niños desarmados que resisten ondeando banderas peruanas y sosteniendo terrones de tierra entre sus manos. Héctor Chacón es capturado y condenado a décadas de reclusión en la siniestra prisión insular de El Frontón, mientras Fortunato cae acribillado en la cumbre del cerro. No obstante la derrota militar inmediata, 'Redoble por Rancas' trasciende la crónica del martirio para erigirse en un canto triunfal a la dignidad imperecedera del campesinado andino: la certeza poética y política de que la sangre de los caídos fecunda la memoria colectiva y prepara el redoble definitivo de la justicia en todas las cordilleras de América."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué simboliza el gigantesco 'cercado de alambre de púas' en la novela de Manuel Scorza?",
            "options": [
              "Un adorno festivo instalado por los párrocos de Yanahuanca para celebrar la Semana Santa.",
              "La invasión territorial despiadada de la corporación minera transnacional que confisca pastizales y caminos ancestrales.",
              "Un experimento agrícola de riego por goteo financiado por la universidad.",
              "Una muralla defensiva construida por los comuneros para protegerse de los bandoleros."
            ],
            "correctIndex": 1,
            "explanation": "El cercado representa la voracidad del despojo capitalista transnacional y la privatización forzosa de la tierra comunal."
          },
          {
            "question": "¿Qué singular facultad posee Héctor Chacón, 'el Nictálope', líder de la rebelión comunera?",
            "options": [
              "La capacidad de volar sobre las cumbres nevadas.",
              "La facultad fisiológica extraordinaria de ver con nitidez en la oscuridad de la noche.",
              "El don de transformar las rocas en lingotes de oro puro.",
              "El poder de comunicarse telepáticamente con los diplomáticos de Lima."
            ],
            "correctIndex": 1,
            "explanation": "Chacón es llamado el Nictálope porque puede ver en la noche profunda, liderando ataques sorpresa nocturnos contra el cercado."
          },
          {
            "question": "¿Qué refleja el célebre episodio de la moneda caída del Juez Montenegro en la plaza de Yanahuanca?",
            "options": [
              "La generosidad caritativa del magistrado hacia los mendigos de la provincia.",
              "El clima asfixiante de terror, arbitrariedad y sumisión reverencial impuesto por el poder gamonal sobre la población indígena.",
              "La prosperidad económica y abundancia de plata en el comercio local.",
              "La celebración de una competencia deportiva infantil en el pueblo."
            ],
            "correctIndex": 1,
            "explanation": "Nadie toca la moneda durante meses por temor a represalias brutales, ilustrando el absolutismo despótico del gamonalismo judicial."
          }
        ]
      }
    }
  },
  "world/b2/b2-migracion-01": {
    "id": "b2-migracion-01",
    "title": "Corrientes migratorias históricas e intrarregionales en el Cono Sur",
    "level": "B2",
    "lesson": 1,
    "type": "world",
    "estimatedMinutes": 8,
    "summary": "La evolución de las corrientes migratorias en América del Sur: de la gran inmigración transatlántica europea de fines del siglo XIX y principios del XX a los intensos flujos migratorios intrarregionales y laborales entre países vecinos del Cono Sur y la región andina.",
    "characters": [
      "Demógrafos e historiadores de las migraciones suramericanas",
      "Familias de origen inmigrante italiano, español, boliviano y paraguayo en Buenos Aires y São Paulo",
      "Investigadores sociales de la CEPAL y comisionados de movilidad humana"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "A lo largo de los dos últimos siglos, la fisonomía demográfica, cultural y productiva de América del Sur ha sido moldeada de forma determinante por dos grandes oleadas de movilidad humana de signo y dirección disímiles: por un lado, la colosal inmigración transatlántica de ultramar que arribó masivamente a los puertos de Buenos Aires, Montevideo, Santos y Río de Janeiro entre fines del siglo diecinueve y la primera mitad del siglo veinte; por otro, los intensos y dinámicos flujos migratorios intrarregionales que, desde mediados del siglo pasado hasta la actualidad, han conectado estrechamente los destinos laborales y familiares de millones de ciudadanos entre repúblicas vecinas del Cono Sur y el espacio andino. Aunado a ello, las dinámicas migratorias estuvieron íntimamente vinculadas con las transformaciones de las economías primario-exportadoras y los procesos de industrialización sustitutiva de importaciones en las grandes urbes del continente."
      },
      {
        "type": "narration",
        "text": "Aquella primera epopeya atlántica estuvo impulsada por las políticas de colonización y poblamiento promovidas por estadistas que concebían a la inmigración europea como el motor indispensable para modernizar la agricultura pampeana y edificar metrópolis cosmopolitas. Entre 1880 y 1930, más de cuatro millones de campesinos, obreros y artesanos italianos, españoles, portugueses, alemanes y levantinos desembarcaron en las márgenes del Plata y en las haciendas cafetaleras paulistas huyendo de la pobreza agraria y las guerras europeas. Su presencia vigorosa transformó las lenguas locales a través de jergas urbanas como el cocoliche y el lunfardo, enriqueció la gastronomía con pastas y pizzas populares y cimentó el mutualismo obrero que dio origen a los primeros sindicatos y federaciones gremiales organizadas. En efecto, la apertura de vías férreas y caminos troncales facilitó el flujo incesante de familias campesinas e indígenas hacia las periferias metropolitanas, transformando irreversiblemente el mapa demográfico y cultural."
      },
      {
        "type": "narration",
        "text": "Sin embargo, a medida que avanzaba la segunda mitad del siglo veinte y se consolidaban los polos fabriles y de servicios en las principales capitales suramericanas, el eje migratorio predominante viró de lo transatlántico hacia lo intrarregional y fronterizo. Centenares de miles de familias paraguayas, bolivianas, chilenas y uruguayas comenzaron a radicarse en el Gran Buenos Aires y en las provincias de frontera agraria atraídas por la demanda incesante de mano de obra en la construcción civil, la industria textil, la cosecha vitivinícola y el cinturón hortícola de la pampa húmeda. De manera paralela, trabajadores colombianos cruzaban la frontera venezolana durante el 'boom' petrolero de los años setenta para laborar en el comercio y la ganadería de los llanos occidentales."
      },
      {
        "type": "narration",
        "text": "Lejos de constituir un fenómeno transitorio o meramente contingente, esta migración intrarregional consolidó densas redes de parentesco transnacional, asociaciones comunitarias de ayuda mutua y una intensa circulación de remesas familiares que dinamizó las economías rurales de origen en los valles andinos y las cuencas fluviales. Asimismo, los migrantes fundaron festivales folclóricos de gran arraigo público, como las multitudinarias celebraciones de la Virgen de Copacabana en Charrúa o la fiesta de Caacupé en los suburbios bonaerenses, demostrando que la movilidad humana no diluye las identidades originarias, sino que las recrea y fertiliza en diálogo fraterno con las sociedades de acogida. Del mismo modo, las escuelas públicas se transformaron en laboratorios vivos de integración pluricultural cotidiana. Por consiguiente, los centros de residentes provincianos y extranjeros cumplieron un rol insustituible al ofrecer asesoría jurídica gratuita, auxilio mutual ante enfermedades imprevistas y espacios recreativos para preservar las danzas tradicionales."
      },
      {
        "type": "narration",
        "text": "En conclusión, la historia de América del Sur es indisolublemente una historia de migraciones entrecruzadas, donde ningún pueblo puede arrogarse una pureza identitaria excluyente frente a sus vecinos hermanos. Todos los países de la región han sido alternativamente tierras de emigración desgarradora, puertos generosos de acogida solidaria y territorios de tránsito fecundo. En última instancia, reconocer que las raíces de nuestras sociedades están entretejidas con los sacrificios, los cantos y los sudores de millones de trabajadores migrantes constituye el fundamento ético más sólido para edificar una ciudadanía suramericana inclusiva, donde la diversidad cultural sea celebrada como la mayor de nuestras riquezas compartidas."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuáles fueron los dos grandes momentos migratorios que transformaron la demografía suramericana?",
            "options": [
              "La colonización ártica y la inmigración procedente de Oceanía exclusivamente.",
              "La gran inmigración transatlántica de ultramar (1880-1930) y los flujos migratorios intrarregionales y fronterizos contemporáneos.",
              "La emigración hacia la Antártida y la repatriación forzosa colonial.",
              "El éxodo masivo hacia las islas del Pacífico sur."
            ],
            "correctIndex": 1,
            "explanation": "América del Sur experimentó primero la gran oleada europea y luego una profunda integración migratoria entre países vecinos."
          },
          {
            "question": "¿En qué sectores productivos se insertaron primordialmente los migrantes intrarregionales en el Cono Sur?",
            "options": [
              "La construcción civil, la industria textil, la cosecha agropecuaria y los servicios urbanos.",
              "La navegación espacial y la astronomía de observatorios de alta montaña.",
              "La exportación exclusiva de piedras preciosas hacia Europa.",
              "La dirección monárquica de empresas extranjeras."
            ],
            "correctIndex": 0,
            "explanation": "La fuerza de trabajo migrante fue indispensable en la infraestructura urbana, los talleres textiles y la producción de alimentos."
          },
          {
            "question": "¿Qué demuestran festivales populares como el de Copacabana o Caacupé en las metrópolis suramericanas?",
            "options": [
              "La pérdida definitiva de la memoria cultural de los antepasados.",
              "Que las identidades originarias se recrean y florecen enriqueciendo la vida cultural y comunitaria de las sociedades receptoras.",
              "La imposición de leyes de aislamiento religioso obligatorio.",
              "La prohibición de la música autóctona en espacios públicos."
            ],
            "correctIndex": 1,
            "explanation": "Las tradiciones migrantes se integran al tejido urbano demostrando que la migración aporta vitalidad cultural y fraternidad comunitaria."
          }
        ]
      }
    }
  },
  "world/b2/b2-migracion-02": {
    "id": "b2-migracion-02",
    "title": "El éxodo venezolano y la respuesta humanitaria regional: El Proceso de Quito",
    "level": "B2",
    "lesson": 2,
    "type": "world",
    "estimatedMinutes": 8,
    "summary": "La mayor crisis de movilidad humana en la historia contemporánea de América del Sur: el éxodo de más de siete millones de venezolanos, la respuesta multilateral a través del Proceso de Quito, los mecanismos de regularización temporal (PPT, PTP) y los desafíos de inclusión socioeconómica.",
    "characters": [
      "Familias y profesionales venezolanos en Colombia, Perú, Ecuador, Chile y Brasil",
      "Delegados gubernamentales y cancilleres de las conferencias del Proceso de Quito",
      "Representantes de ACNUR, OIM y organizaciones de derechos humanos"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Durante la segunda década del siglo veintiuno, América del Sur fue testigo y protagonista del mayor desplazamiento forzado de población en su historia republicana contemporánea: la salida de más de siete millones de venezolanos de su tierra natal como consecuencia de una severa crisis económica, política, institucional y humanitaria. Familias enteras, profesionales universitarios, artesanos, jóvenes y ancianos debieron emprender travesías terrestres dramáticas a través de miles de kilómetros de cordilleras, selvas y valles, caminando con mochilas al hombro por el páramo andino de Berlín en Colombia o cruzando las sabanas de Pacaraima en la frontera norte brasileña en busca de alimentos, medicamentos, seguridad jurídica y horizontes de futuro digno para sus hijos. Incluso en condiciones orográficas inclementes, miles de madres con bebés en brazos desafiaron las trochas clandestinas ('caminos verdes') controladas por grupos armados irregulares, arriesgando sus vidas para escapar del desabastecimiento de alimentos."
      },
      {
        "type": "narration",
        "text": "Ante una conmoción demográfica de semejante magnitud, que desbordó con rapidez las capacidades ordinarias de recepción y asistencia de los sistemas de asilo tradicionales, los países suramericanos adoptaron una postura multilateral solidaria pionera en el concierto internacional: el denominado 'Proceso de Quito'. Iniciado en septiembre de 2018 por convocatoria del gobierno ecuatoriano y con el acompañamiento técnico de la Agencia de la ONU para los Refugiados (ACNUR) y la Organización Internacional para las Migraciones (OIM), este mecanismo intergubernamental reunió periódicamente a catorce Estados de la región para coordinar directrices comunes de acogida humanitaria, regularización migratoria ágil, acceso a la educación escolar y combate conjunto contra las redes de trata de personas."
      },
      {
        "type": "narration",
        "text": "El fruto más luminoso y valiente de esta doctrina humanitaria se materializó en programas nacionales de regularización extraordinaria a gran escala. Destaca de modo paradigmático el caso de Colombia, principal país receptor con cerca de tres millones de refugiados y migrantes, que implementó en 2021 el histórico 'Estatuto Temporal de Protección para Migrantes Venezolanos' (ETPV), otorgando un Permiso por Protección Temporal (PPT) con vigencia de diez años a casi dos millones de personas. Este estatus legal permitió a los beneficiarios acceder al empleo formal, cotizar en el sistema de pensiones, afiliarse al régimen de salud y abrir cuentas bancarias en igualdad de condiciones con los ciudadanos nacionales, desarticulando las redes de explotación laboral clandestina. Asimismo, las duras jornadas a pie por páramos gélidos y selvas pantanosas provocaron cuadros graves de deshidratación e hipotermia que requirieron la intervención urgente de brigadas médicas de emergencia de la Cruz Roja."
      },
      {
        "type": "narration",
        "text": "Mecanismos análogos de acogida se desplegaron en Perú mediante el Permiso Temporal de Permanencia (PTP), en Ecuador a través de las visas de regularización extraordinaria 'Virte', y en Brasil mediante la elogiada 'Operación Acogida' ('Operação Acolhida') liderada por las fuerzas armadas y organismos civiles en Roraima, que combinó atención médica fronteriza, documentación inmediata y un programa masivo de 'interiorización' que trasladó voluntariamente a decenas de miles de migrantes hacia ciudades del centro y sur de Brasil con empleo asegurado. Con todo, la inclusión plena aún enfrenta barreras complejas, como la exigencia de legalizaciones apostilladas inaccesibles, el subempleo profesional y brotes esporádicos de estigmatización mediática. Del mismo modo, la cooperación técnica internacional apoyó el fortalecimiento de los sistemas nacionales de registro civil e identificación biométrica, facilitando la emisión de partidas de nacimiento a menores nacidos en tránsito para prevenir la apatridia."
      },
      {
        "type": "narration",
        "text": "En suma, la respuesta suramericana ante el éxodo venezolano ha sentado un precedente universal de fraternidad y responsabilidad compartida que contrasta éticamente con las políticas de cierre de fronteras aplicadas en otras latitudes del planeta. Al abrir sus puertas y regularizar a millones de compatriotas continentales, las repúblicas de la región no solo honraron la histórica deuda moral con una Venezuela que en décadas pasadas acogió con generosidad a perseguidos políticos y exiliados de todo el Cono Sur, sino que reafirmaron el principio supremo de que la dignidad humana está por encima de cualquier coyuntura fronteriza o bandería partidaria. Gracias a esta articulación multilateral, se logró mitigar la vulnerabilidad extrema de miles de núcleos familiares en los corredores humanitarios más transitados de la región."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué mecanismo intergubernamental se creó en 2018 para coordinar la respuesta regional al éxodo venezolano?",
            "options": [
              "El Tratado de Versalles migratorio.",
              "El Proceso de Quito, que reunió a catorce Estados con apoyo de ACNUR y OIM.",
              "El Protocolo Antártico de Reasentamiento.",
              "La Conferencia Petrolera de Viena."
            ],
            "correctIndex": 1,
            "explanation": "El Proceso de Quito articula políticas de acogida y regularización técnica entre los países receptores de la región."
          },
          {
            "question": "¿Qué beneficio esencial otorgó el Estatuto Temporal de Protección implementado por Colombia en 2021?",
            "options": [
              "Un permiso de permanencia temporal por diez años que garantiza empleo formal, salud, educación y bancarización.",
              "La obligación de permanecer confinado en campamentos cerrados de frontera.",
              "La prohibición de alquilar viviendas en las ciudades capitales.",
              "La pérdida definitiva de la nacionalidad de origen."
            ],
            "correctIndex": 0,
            "explanation": "El ETPV regularizó a cerca de dos millones de personas otorgándoles estabilidad legal y plenos derechos sociales por una década."
          },
          {
            "question": "¿En qué consistió la 'Operación Acogida' ('Operação Acolhida') implementada por Brasil?",
            "options": [
              "En la construcción de un muro de cemento en la frontera selvática.",
              "En un modelo humanitario que combinó recepción fronteriza, documentación ágil e interiorización laboral hacia diversas ciudades del país.",
              "En la deportación sumaria de todas las familias recién llegadas.",
              "En el cobro de peaje obligatorio en dólares a quienes cruzaban el río."
            ],
            "correctIndex": 1,
            "explanation": "Brasil integró atención humanitaria en Roraima con vuelos de interiorización voluntaria hacia metrópolis con oferta de trabajo."
          }
        ]
      }
    }
  },
  "world/b2/b2-migracion-03": {
    "id": "b2-migracion-03",
    "title": "Ciudades de frontera y corredores de acogida: De Pacaraima y Cúcuta a Tumbes y Pisiga",
    "level": "B2",
    "lesson": 3,
    "type": "world",
    "estimatedMinutes": 8,
    "summary": "La geografía viva de las fronteras suramericanas como espacios de tránsito, auxilio y choque humanitario: los pasos de Cúcuta-Villa del Rosario (Colombia-Venezuela), Pacaraima (Brasil-Venezuela), Tumbes (Perú-Ecuador) y Pisiga-Colchane (Bolivia-Chile), y la resiliencia de las comunidades ribereñas y andinas de acogida.",
    "characters": [
      "Trabajadores humanitarios, médicos y voluntarios de albergues fronterizos",
      "Alcaldes y autoridades locales de municipios de frontera",
      "Caminantes y familias migrantes que transitan los corredores andinos y amazónicos"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "A lo largo de los miles de kilómetros de líneas limítrofes que surcan las geografías andinas, llaneras y selváticas de América del Sur, un conjunto de ciudades y poblados fronterizos —históricamente postergados por las políticas centralistas de las capitales nacionales lejanas— se convirtió de la noche a la mañana en el epicentro humano, logístico y ético de la mayor encrucijada de acogida del continente. Enclaves limítrofes emblemáticos como Cúcuta y Villa del Rosario en el departamento colombiano de Norte de Santander, Pacaraima en el extremo norte del estado brasileño de Roraima, Aguas Verdes y Tumbes en la costa norte peruana, y el gélido paso altiplánico de Pisiga y Colchane entre Bolivia y Chile atestiguaron cotidianamente el paso incesante de miles de personas que desafiaban la fatiga extrema en pos de refugio y esperanza. Asimismo, estos pasos limítrofes pusieron de relieve las profundas interdependencias históricas entre comunidades vecinas que comparten dialectos, lazos matrimoniales y circuitos comerciales cotidianos más allá de las aduanas oficiales."
      },
      {
        "type": "narration",
        "text": "En el paso de Cúcuta, conectado con la venezolana San Antonio del Táchira a través del célebre Puente Internacional Simón Bolívar, el flujo humano adquirió dimensiones sobrecogedoras. Durante años, más de cuarenta mil personas cruzaron a diario este viaducto sobre el río Táchira para abastecerse de víveres básicos, adquirir medicinas vitales o iniciar la prolongada travesía a pie rumbo al sur. En las orillas de la carretera que asciende hacia Bucaramanga, organizaciones comunitarias, parroquias locales y brigadas de la Cruz Roja instalaron comedores solidarios, puntos de hidratación y carpas de auxilio médico para asistir a los 'caminantes' exhaustos por las bajas temperaturas del páramo, demostrando la inagotable generosidad del pueblo fronterizo frente al sufrimiento ajeno."
      },
      {
        "type": "narration",
        "text": "Una realidad de similar dramatismo logístico se vivió en Pacaraima, un pequeño municipio de doce mil habitantes rodeado por reservas indígenas en la frontera amazónica entre Brasil y Venezuela. La llegada masiva de hasta mil personas por día puso a prueba la capacidad de los servicios de salud y saneamiento locales, pero motivó la instalación de una moderna ciudadela humanitaria con puestos de triaje biométrico, vacunación universal y módulos de albergue temporal gestionados por agencias de Naciones Unidas y personal del ejército brasileño. Gracias a este corredor de acogida organizado, las familias recién llegadas recibían su CPF (número de identificación tributaria brasileña) y autorización de residencia en cuestión de horas, facilitando su inserción legal inmediata. Por añadidura, la dotación de generadores solares y plantas potabilizadoras de agua en los puestos fronterizos permitió garantizar condiciones sanitarias dignas para miles de niños y lactantes en tránsito."
      },
      {
        "type": "narration",
        "text": "En las alturas desérticas y gélidas del altiplano andino, a casi cuatro mil metros sobre el nivel del mar, el paso de Pisiga hacia la comuna chilena de Colchane planteó desafíos humanitarios extremos derivados de los rigores climáticos. Con temperaturas nocturnas que caen con frecuencia por debajo de los diez grados bajo cero, vientos huracanados y escasez crítica de oxígeno, el cruce irregular por trochas desérticas cobró decenas de vidas humanas por hipotermia y mal de montaña severo. Frente a esta tragedia recurrente, las comunidades aymaras locales y los socorristas habilitaron albergues de emergencia comunales y postas térmicas para salvar a niños y mujeres expuestos a las inclemencias del desierto de altura."
      },
      {
        "type": "narration",
        "text": "En conclusión, las ciudades de frontera y los corredores humanitarios suramericanos revelan tanto las tensiones de la precariedad institucional como la grandeza solidaria de las comunidades receptoras. Lejos de ser simples cicatrices territoriales de separación militar, las fronteras son espacios vivos de encuentro intercultural donde se libra la batalla más decisiva por la dignidad humana. En última instancia, fortalecer las capacidades presupuestarias de estos municipios periféricos y dotarlos de infraestructura de acogida permanente constituye un imperativo de justicia territorial para toda la región, ratificando que el rostro más noble de América del Sur brilla en las manos extendidas que reciben con calidez fraterna al viajero desamparado. De esta manera, la cooperación binacional se afianza como el único camino viable para garantizar una gobernanza migratoria ordenada, segura y respetuosa de los derechos humanos fundamentales."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué viaducto internacional sobre el río Táchira se convirtió en el principal corredor peatonal de frontera colombo-venezolana?",
            "options": [
              "El Puente de la Amistad.",
              "El Puente Internacional Simón Bolívar, entre Cúcuta y San Antonio del Táchira.",
              "El Viaducto de los Andes.",
              "El Paso de Jama."
            ],
            "correctIndex": 1,
            "explanation": "El Puente Simón Bolívar canalizó el tránsito diario de decenas de miles de personas durante los picos de la crisis migratoria."
          },
          {
            "question": "¿Qué peligro mortal enfrentan los migrantes que cruzan el paso altiplánico entre Pisiga y Colchane?",
            "options": [
              "Inundaciones fluviales monzónicas en la selva baja.",
              "Hipotermia y mal agudo de montaña debido a temperaturas bajo cero y altitudes superiores a los cuatro mil metros.",
              "Ataques de animales carnívoros selváticos en las trochas.",
              "Fiebre amarilla tropical en los pantanos costeros."
            ],
            "correctIndex": 1,
            "explanation": "El cruce altiplánico a casi cuatro mil metros entraña temperaturas extremas bajo cero que provocan muertes por hipotermia."
          },
          {
            "question": "¿Qué labor destacada cumplen las comunidades y organizaciones locales en los corredores fronterizos?",
            "options": [
              "Expulsar a los caminantes hacia las cordilleras desiertas.",
              "Habilitar comedores populares, carpas de auxilio médico y albergues térmicos solidarios para asistir a las familias en tránsito.",
              "Clausurar los hospitales públicos a personas foráneas.",
              "Cobrar comisiones ilegales de tránsito en dólares."
            ],
            "correctIndex": 1,
            "explanation": "La sociedad civil y los municipios de frontera organizan redes de auxilio vital con alimentos, abrigo y atención médica básica."
          }
        ]
      }
    }
  },
  "world/b2/b2-migracion-04": {
    "id": "b2-migracion-04",
    "title": "Remesas, familias transnacionales y el tejido económico de la diáspora",
    "level": "B2",
    "lesson": 4,
    "type": "world",
    "estimatedMinutes": 8,
    "summary": "El impacto macroeconómico y humano de las remesas en América del Sur: los flujos financieros que sostienen la seguridad alimentaria en hogares de origen, la bancarización e inclusión financiera digital a través de aplicaciones móviles, y la resistencia de las familias transnacionales unidas a través de la distancia.",
    "characters": [
      "Trabajadores migrantes que envían remesas mensuales desde las capitales de acogida",
      "Abuelas y cuidadores que administran los recursos del hogar en las comunidades de origen",
      "Economistas de bancos centrales y desarrolladores de plataformas 'fintech' transfronterizas"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Detrás de los discursos políticos sobre la integración regional y las complejas estadísticas de los balances de pagos nacionales, late una realidad económica microscópica pero colosal que constituye el verdadero sostén vital de millones de hogares en América del Sur: el flujo ininterrumpido de las remesas familiares. Mes tras mes, con un sacrificio cotidiano ejemplar que implica prolongadas jornadas laborales en la construcción, el comercio minorista, el cuidado domiciliario o las entregas por aplicaciones digitales, los trabajadores migrantes apartan una porción significativa de sus magros ingresos para transferirla religiosamente a sus padres, cónyuges e hijos que permanecieron en sus pueblos y ciudades natales. Incluso en períodos de recesión o desempleo en los países de acogida, los remitentes ajustan sus propios gastos de subsistencia al mínimo indispensable antes de recortar los envíos monetarios a sus familias."
      },
      {
        "type": "narration",
        "text": "En términos macroeconómicos, el volumen acumulado de estas transferencias personales ha alcanzado cotas históricas en la región, rebasando con holgura los cincuenta mil millones de dólares anuales en el conjunto de América Latina y representando en países como Bolivia, Colombia, Ecuador, Paraguay y Venezuela entre el tres y el quince por ciento de su Producto Interno Bruto (PIB). A diferencia de los flujos de inversión extranjera directa o de los préstamos multilaterales de desarrollo —que a menudo quedan atrapados en burocracias estatales o gastos administrativos intermedios—, las remesas llegan de forma directa, líquida e inmediata a los bolsillos de las familias más vulnerables, operando como una red de seguridad social descentralizada que financia alimentación nutritiva, medicamentos vitales y cuotas escolares básicas. Este flujo continuo de divisas familiares ha permitido a miles de hogares superar la línea de indigencia y costear tratamientos médicos de alta complejidad que el sistema público no cubre."
      },
      {
        "type": "narration",
        "text": "Asimismo, este fenómeno financiero ha desencadenado una profunda revolución en la bancarización y la inclusión digital de amplios sectores populares tradicionalmente marginados de los sistemas bancarios comerciales. La proliferación de empresas de tecnología financiera ('fintech'), billeteras móviles interoperables y plataformas de transferencias transfronterizas basadas en códigos QR redujo drásticamente las comisiones abusivas cobradas por las agencias de cambio tradicionales, permitiendo que un obrero en Santiago de Chile envíe fondos instantáneamente a un teléfono móvil en una aldea rural de Cochabamba o Barquisimeto con comisiones inferiores al dos por ciento y a tipos de cambio transparentes de mercado. Por su parte, los bancos comunales y cooperativas agrícolas en los valles de origen canalizan una fracción de estos ahorros hacia la compra de semillas mejoradas, sistemas de riego tecnificado y paneles fotovoltaicos."
      },
      {
        "type": "narration",
        "text": "Empero, la dimensión más conmovedora de este entramado económico radica en la forja de las 'familias transnacionales': unidades afectivas indestructibles que reconfiguran los lazos de parentesco a través de miles de kilómetros de distancia geográfica. Madres que crían a sus hijos a través de videollamadas nocturnas por teléfonos inteligentes, abuelas que asumen con abnegación el cuidado cotidiano de nietos cuyos progenitores trabajan en el extranjero, y adolescentes que maduran precozmente comprendiendo el valor del esfuerzo paterno en tierras lejanas demuestran que el hogar no se circunscribe a cuatro paredes de cemento, sino al compromiso inquebrantable de amor y auxilio mutuo que desafía las fronteras."
      },
      {
        "type": "narration",
        "text": "En conclusión, las remesas familiares y las redes de la diáspora desmienten definitivamente el prejuicio xenófobo que retrata al migrante como una carga gravosa para las sociedades receptoras. Por el contrario, los trabajadores foráneos dinamizan la economía del país donde residen mediante su fuerza productiva y el pago de tributos locales, al tiempo que rescatan de la miseria extrema a sus comunidades de origen en un circuito virtuoso de solidaridad transfronteriza. En última instancia, este tejido financiero y afectivo demuestra que el verdadero corazón integrador de América del Sur no palpita en las bolsas de valores ni en los gabinetes ministeriales, sino en el sudor noble y la generosidad imperecedera de sus familias trabajadoras. En consecuencia, las remesas no solo sustentan el consumo básico inmediato, sino que catalizan procesos productivos que fijan población en sus comunidades de origen."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué impacto directo producen las remesas familiares en las comunidades de origen de los migrantes?",
            "options": [
              "Financian armamento pesado para disputas territoriales fronterizas.",
              "Llegan directamente a los hogares vulnerables financiando alimentación, salud, educación y vivienda básica.",
              "Generan una deuda externa impagable con los organismos multilaterales.",
              "Provocan el cierre inmediato de todas las escuelas rurales."
            ],
            "correctIndex": 1,
            "explanation": "Las remesas operan como una red social directa de protección que garantiza la subsistencia y el progreso familiar."
          },
          {
            "question": "¿Cómo ha transformado la tecnología 'fintech' el envío de remesas en América del Sur?",
            "options": [
              "Ha prohibido el uso de teléfonos celulares en las áreas rurales.",
              "Ha reducido sustancialmente los costos de comisión y acelerado las transferencias inmediatas a través de billeteras móviles.",
              "Ha sustituido el dinero electrónico por intercambio de sal marina.",
              "Ha obligado a los migrantes a viajar en persona para entregar el efectivo en mano."
            ],
            "correctIndex": 1,
            "explanation": "Las plataformas digitales reducen drásticamente las comisiones bancarias tradicionales y facilitan envíos instantáneos."
          },
          {
            "question": "¿Qué caracteriza a las denominadas 'familias transnacionales' en la experiencia migratoria?",
            "options": [
              "La ruptura total de los lazos afectivos y el olvido deliberado de los hijos.",
              "La preservación de lazos de afecto, cuidado y corresponsabilidad económica a través de la distancia con apoyo digital.",
              "La obligación de contraer matrimonio exclusivamente con diplomáticos extranjeros.",
              "La prohibición de comunicarse por canales electrónicos."
            ],
            "correctIndex": 1,
            "explanation": "Las familias transnacionales mantienen su cohesión afectiva y apoyo económico diario desafiando la lejanía física."
          }
        ]
      }
    }
  },
  "world/b2/b2-migracion-05": {
    "id": "b2-migracion-05",
    "title": "Interculturalidad, combate a la xenofobia y el mosaico urbano suramericano",
    "level": "B2",
    "lesson": 5,
    "type": "world",
    "estimatedMinutes": 8,
    "summary": "La integración social y cultural en las grandes metrópolis de América del Sur: la superación de prejuicios y narrativas xenófobas, la fecundación mutua de la gastronomía, la música y las artes populares, las escuelas públicas como crisoles de ciudadanía intercultural y el horizonte de la convivencia fraterna.",
    "characters": [
      "Líderes comunitarios y colectivos artísticos de barrios interculturales de Lima, Bogotá, Santiago y São Paulo",
      "Docentes de escuelas públicas que implementan proyectos de integración pedagógica pluricultural",
      "Activistas por los derechos humanos y sociólogos urbanos"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Al recorrer las calles arboladas de barrios cosmopolitas y populares como el Bom Retiro y Mooca en São Paulo, Recoleta y Flores en Buenos Aires, Estación Central e Independencia en Santiago de Chile, o La Victoria y Los Olivos en Lima, cualquier observador atento percibe de inmediato que las grandes metrópolis suramericanas se han convertido en hervideros vibrantes de convivencia intercultural. En estos espacios urbanos donde convergen acentos caribeños, quechuas, guaraníes y rioplatenses, las fronteras idiomáticas y geográficas se difuminan para dar nacimiento a un tejido social mestizo, resiliente y creativo que redefine la identidad colectiva de nuestras ciudades en el siglo veintiuno. Aunado a ello, la mezcla de modismos lingüísticos y giros coloquiales enriquece el habla urbana cotidiana, generando un castellano suramericano híbrido, musical y de asombrosa ductilidad expresiva."
      },
      {
        "type": "narration",
        "text": "El ámbito más sabroso, inmediato y elocuente de este mestizaje cotidiano se manifiesta en la gastronomía popular, donde las tradiciones culinarias de la diáspora han enriquecido de forma deslumbrante los hábitos de consumo de las sociedades receptoras. En las esquinas de Santiago y Bogotá proliferan locales donde se hornean arepas de maíz tierno, tequeños dorados y cachapas con queso de mano, mientras que en Lima y Buenos Aires el ceviche peruano, las salteñas bolivianas y la sopa paraguaya de chipa guazú conviven armónicamente con las empanadas criollas y las parrilladas tradicionales. Esta fusión de sabores no es un simple fenómeno mercantil, sino un puente de diálogo cultural donde compartir un plato preparado con cariño derriba prejuicios ancestrales con mayor eficacia que mil discursos doctrinales. Incluso las celebraciones religiosas patronales como la procesión del Señor de los Milagros o las festividades de Urkupiña convocan hoy a feligreses de todas las nacionalidades en un solo abrazo de fe y hermandad comunitaria."
      },
      {
        "type": "narration",
        "text": "De manera simultánea, la música, las artes visuales y la literatura urbana han experimentado una renovación extraordinaria gracias al talento creador de los artistas migrantes. Orquestas sinfónicas juveniles integradas por músicos venezolanos formados en el célebre 'Sistema' enriquecen la oferta cultural de Medellín y Santiago; compañías de danza folclórica boliviana tiñen de comparsas de caporales y morenadas las avenidas porteñas; y muralistas transnacionales plasman en los muros de las favelas y comunas mensajes poéticos de fraternidad continental. A través del arte compartido, los jóvenes resignifican el dolor del desarraigo, transformando la memoria de la migración en un himno colectivo de esperanza y afirmación comunitaria."
      },
      {
        "type": "narration",
        "text": "No obstante esta vitalidad creadora, la consolidación de una convivencia verdaderamente armónica enfrenta el desafío tóxico de la xenofobia, atizada a menudo por discursos políticos irresponsables y titulares sensacionalistas que criminalizan al forastero atribuyéndole falsamente la culpa de la inseguridad ciudadana o el deterioro de los servicios públicos. Frente a esta hostilidad estigmatizante, las escuelas públicas se han erigido en los baluartes democráticos más eficaces: aulas pluriculturales donde maestras y maestros enseñan a niñas y niños a celebrar la diversidad de orígenes, erradicar el acoso escolar discriminatorio y reconocer en el compañero recién llegado a un hermano entrañable con quien construir el porvenir común. Del mismo modo, las clínicas jurídicas universitarias ofrecen patrocinio gratuito contra actos de discriminación arbitraria, consolidando una red defensora de la igualdad de trato ante los tribunales locales."
      },
      {
        "type": "narration",
        "text": "En conclusión, el florecimiento del mosaico urbano suramericano ratifica la vocación universal de nuestro continente como tierra de acogida, refugio y mestizaje creador. Las ciudades del mañana no se miden por la altura de sus rascacielos ni por la frialdad de sus centros financieros, sino por su capacidad ética de abrazar al otro, proteger al vulnerable y hacer de la diferencia una fuente inagotable de solidaridad y belleza compartida. En última instancia, la convivencia intercultural en las barriadas del continente demuestra que la Patria Grande soñada por los libertadores no es una utopía inalcanzable, sino una realidad cotidiana que se amasa día a día en el calor fraterno de nuestros pueblos. La interculturalidad viva se transforma así en un motor de cohesión social que desarma los prejuicios etnocéntricos y construye ciudadanía plena."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿De qué manera contribuye la gastronomía migrante al proceso de integración intercultural urbana?",
            "options": [
              "Obligando a los restaurantes a servir un menú único decretado por el Estado.",
              "Enriqueciendo los hábitos culinarios locales y funcionando como un puente accesible de diálogo, conocimiento y encuentro fraterno.",
              "Prohibiendo los ingredientes agrícolas tradicionales de la región.",
              "Cerrando los mercados populares al público extranjero."
            ],
            "correctIndex": 1,
            "explanation": "La gastronomía compartida derriba barreras y genera empatía cultural a través de la convivencia y el sabor cotidiano."
          },
          {
            "question": "¿Qué amenaza social combate la escuela pública como espacio de ciudadanía intercultural?",
            "options": [
              "El aprendizaje de la historia universal.",
              "La xenofobia y la estigmatización discriminatoria fomentada por discursos sensacionalistas.",
              "La práctica de actividades deportivas al aire libre.",
              "La enseñanza de materias científicas y matemáticas."
            ],
            "correctIndex": 1,
            "explanation": "La escuela pública educa en valores democráticos erradicando el acoso xenófobo y celebrando la diversidad cultural."
          },
          {
            "question": "¿Cuál es la premisa ética que define a las ciudades interculturales suramericanas?",
            "options": [
              "Construir murallas perimetrales alrededor de los barrios céntricos.",
              "Medir su grandeza por su capacidad de acoger con dignidad al otro y hacer de la diversidad una fuente de solidaridad colectiva.",
              "Expulsar a todos los artistas y músicos de los espacios públicos.",
              "Prohibir el uso de expresiones y dialectos regionales."
            ],
            "correctIndex": 1,
            "explanation": "La grandeza urbana radica en la inclusión fraterna, la convivencia democrática y el respeto irrestricto a los derechos humanos."
          }
        ]
      }
    }
  },
  "world/b2/b2-migracion-consolidation": {
    "id": "b2-migracion-consolidation",
    "title": "La marcha solidaria: El corazón caminante de América del Sur",
    "level": "B2",
    "lesson": 6,
    "type": "world",
    "estimatedMinutes": 8,
    "summary": "Síntesis reflexiva sobre las migraciones y la solidaridad humana en América del Sur: las raíces históricas de las corrientes transatlánticas e intrarregionales, la respuesta humanitaria al éxodo venezolano, la resiliencia en ciudades fronterizas, el tejido financiero de las remesas y el florecimiento del mosaico intercultural.",
    "characters": [
      "Cronistas y ensayistas de la movilidad humana suramericana",
      "Comunidades migrantes, voluntarias y pueblos de acogida como protagonistas colectivos"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Al contemplar en su conjunto la historia profunda y las vicisitudes del continente suramericano, se impone una verdad luminosa e incontestable: América del Sur es una tierra de caminos abiertos y pies incansables, una patria forjada en el movimiento fecundo de hombres y mujeres que jamás se resignaron a la desesperanza del encierro. En primer término, la movilidad humana no constituye una anomalía patológica que deba ser reprimida con alambres de púas o decretos punitivos de expulsión; es el río vivo que irriga la historia de nuestras repúblicas, la savia nutricia que une a los valles andinos con las costas atlánticas y a las llanuras amazónicas con las megalópolis urbanas en un solo y mismo latido civilizatorio. Por consiguiente, la memoria histórica de las migraciones constituye un baluarte insustituible frente a los discursos del odio y las derivas autoritarias que pretenden fragmentar a nuestros pueblos."
      },
      {
        "type": "narration",
        "text": "A través de las corrientes migratorias históricas —desde las familias de ultramar que poblaron los conventillos de La Boca y los barrios paulistas hasta los millones de trabajadores hermanos que cruzaron fronteras limítrofes para levantar rascacielos y labrar viñedos—, la región aprendió que la identidad no es una fortaleza pétrea inmutable, sino una polifonía en permanente recreación. Cuando en la última década el éxodo forzado de más de siete millones de venezolanos interpeló la conciencia moral del continente, Suramérica no respondió levantando muros de hormigón ni campos de concentración militarizados, sino articulando el Proceso de Quito y promulgando estatutos de protección temporal valientes que consagraron el derecho a la regularización con dignidad. Cada testimonio de exilio o bienvenida custodia una lección imborrable sobre la fragilidad de la democracia y la necesidad perentoria de salvaguardar el asilo como conquista civilizatoria irrenunciable."
      },
      {
        "type": "narration",
        "text": "Asimismo, la geografía de las ciudades fronterizas —como el puente Simón Bolívar en Cúcuta, las sabanas de Pacaraima, las arenas de Tumbes o el altiplano gélido de Pisiga y Colchane— demostró que en los confines periféricos de la patria palpita la generosidad más conmovedora de nuestros pueblos. Allí donde los presupuestos estatales escaseaban y los albergues desbordaban sus capacidades, fueron las manos solidarias de maestras, párrocos, vecinos y voluntarios comunitarios las que cocinaron ollas populares, curaron heridas de caminantes exhaustos y abrigaron a niños ateridos de frío, ratificando que la fraternidad suramericana no es una consigna diplomática hueca, sino una práctica cotidiana indestructible. A la par, el intercambio constante de saberes pedagógicos y tradiciones orales enriquece las aulas escolares donde conviven estudiantes de múltiples procedencias geográficas."
      },
      {
        "type": "narration",
        "text": "Del mismo modo, el impacto fecundo de las remesas familiares y la resistencia de las familias transnacionales evidencian la enorme vitalidad productiva y afectiva de la diáspora. Los miles de millones de dólares transferidos mes tras mes con honradez y sacrificio por los trabajadores foráneos sostienen la salud, la alimentación y la educación de comunidades enteras, al tiempo que billeteras digitales interoperables y plataformas 'fintech' demuestran que la tecnología puede democratizarse al servicio de los sectores populares. Lejos de empobrecer a los países receptores, los migrantes aportan su fuerza laboral, dinamizan el consumo interno y fertilizan las economías urbanas con su creatividad incansable. Asimismo, la convalidación de títulos técnicos y profesionales favorece la fertilización cruzada de la ciencia, la medicina y la educación superior en todos los rincones del Cono Sur."
      },
      {
        "type": "narration",
        "text": "En suma, quien escucha los sones de una orquesta juvenil en Medellín, saborea una arepa en el centro de Santiago o contempla una comparsa de morenada en las calles de Buenos Aires comprende que la diversidad cultural es el mayor tesoro de la Patria Grande. La convivencia intercultural en los barrios populares enseña que derribar la xenofobia y abrazar al forastero es el camino más noble para conquistar la plenitud ciudadana. En última instancia, la marcha solidaria de los pueblos del sur nos recuerda que todos somos pasajeros temporales de una misma tierra sagrada, convocados a construir juntos un hogar continental donde ningún ser humano sea jamás llamado extranjero y donde la justicia, la fraternidad y la paz florezcan para siempre."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Por qué se define a la movilidad humana como un motor civilizatorio en la historia suramericana?",
            "options": [
              "Porque provoca la desaparición inmediata de todas las instituciones públicas.",
              "Porque irriga y conecta las culturas, une los esfuerzos productivos y recrea permanentemente la identidad mestiza del continente.",
              "Porque está restringida por completo a las corporaciones privadas de transporte aéreo.",
              "Porque impide el crecimiento económico de las capitales nacionales."
            ],
            "correctIndex": 1,
            "explanation": "La migración es concebida como un río creador de fraternidad, dinamismo productivo e interculturalidad viva."
          },
          {
            "question": "¿Qué valor ético demostraron las comunidades de frontera durante las crisis migratorias contemporáneas?",
            "options": [
              "El rechazo hostil y la persecución armada a los caminantes vulnerables.",
              "La generosidad solidaria incondicional ofreciendo alimento, albergue y atención médica a las familias en tránsito.",
              "La venta especulativa de agua potable a precios prohibitivos.",
              "La clausura total de escuelas y parroquias comunitarias."
            ],
            "correctIndex": 1,
            "explanation": "Los pueblos fronterizos organizaron redes populares de asistencia humanitaria salvando vidas de personas exhaustas."
          },
          {
            "question": "¿Cuál es la lección suprema que aporta la convivencia intercultural en las metrópolis suramericanas?",
            "options": [
              "Que la diversidad cultural es una debilidad que debe suprimirse con leyes punitivas.",
              "Que abrazar al otro y derribar prejuicios xenófobos enriquece la sociedad y forja la verdadera fraternidad de la Patria Grande.",
              "Que los ciudadanos deben abandonar el uso del idioma español.",
              "Que las ciudades del futuro deben aislarse en murallas territoriales."
            ],
            "correctIndex": 1,
            "explanation": "La inclusión intercultural demuestra que la diversidad humana es la máxima fortaleza para la paz y la justicia continental."
          }
        ]
      }
    }
  },
  "world/b2/b2-migracion": {
    "id": "b2-migracion",
    "title": "Migraciones suramericanas y diáspora: Desplazamientos, refugio y comunidades transnacionales",
    "level": "B2",
    "lesson": 1,
    "type": "world",
    "estimatedMinutes": 20,
    "summary": "Compendio general y panorámico sobre las migraciones y la diáspora en América del Sur: la evolución desde las corrientes atlánticas e intrarregionales hasta el éxodo forzado venezolano, la arquitectura diplomática del Proceso de Quito y los estatutos temporales, la resiliencia en ciudades fronterizas, el tejido financiero de las remesas y el florecimiento del mosaico intercultural.",
    "characters": [
      "Familias migrantes y refugiadas de diversas nacionalidades suramericanas",
      "Líderes de Estado, ministros y comisionados del Proceso de Quito",
      "Trabajadores humanitarios, médicos de frontera y defensores de derechos humanos",
      "Docentes, artistas y comunidades receptoras en las metrópolis del continente"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "A lo largo de las vastas geografías de América del Sur, donde la imponente cordillera de los Andes custodia los pasos de frontera y las planicies fluviales unen a repúblicas hermanas en un continuo territorial indivisible, la movilidad humana se erige como uno de los hilos conductores más hondos, determinantes y conmovedores de nuestra historia colectiva. Lejos de constituir un fenómeno contingente o periférico, las corrientes migratorias han tejido la urdimbre misma sobre la que se asientan las identidades nacionales de nuestro subcontinente. Desde las grandes oleadas de ultramar que a fines del siglo diecinueve poblaron las márgenes del Plata y los campos paulistas hasta las dinámicas migraciones intrarregionales contemporáneas, el continente ha demostrado una vocación indeleble de hospitalidad, resiliencia y mestizaje enriquecedor. Aunado a ello, la experiencia compartida del éxodo y la acogida consolida una sensibilidad común en las nuevas generaciones que conciben a Suramérica como su patria grande sin fronteras."
      },
      {
        "type": "narration",
        "text": "En el siglo veintiuno, este legado histórico de puertas abiertas fue puesto a prueba de manera descomunal ante el éxodo de más de siete millones de ciudadanos venezolanos, obligados a abandonar su tierra natal debido a un severo colapso económico y político. Frente a esta tragedia humanitaria sin parangón, las repúblicas suramericanas no sucumbieron a la tentación securitista de blindar sus fronteras con alambradas ni recurrieron a deportaciones masivas sumarias. Por el contrario, a través de la concertación multilateral del Proceso de Quito y la promulgación de audaces estatutos de protección temporal —como el ETPV en Colombia, el PTP en Perú y la Operación Acogida en Brasil—, los Estados de la región confirieron estatus legal, acceso a la salud, educación formal y derecho al trabajo digno a millones de hermanos forasteros."
      },
      {
        "type": "narration",
        "text": "De manera paralela, la geografía viva de las ciudades fronterizas —desde Cúcuta y Villa del Rosario en los valles del Táchira hasta Pacaraima en la selva norte brasileña, Tumbes en el litoral peruano y el árido paso de Pisiga en el altiplano boliviano-chileno— funcionó como el primer bastión de auxilio y resistencia humana. En estos enclaves limítrofes, a menudo postergados por el centralismo de las capitales, la generosidad comunitaria de parroquias populares, comités vecinales y brigadas médicas voluntarias transformó los corredores de tránsito en espacios de dignidad, brindando un plato caliente de comida, calzado resistente y orientación jurídica a caminantes extenuados por la fatiga y el frío de las alturas. Por ende, las inversiones públicas en infraestructura de frontera benefician directamente a las poblaciones autóctonas que históricamente carecían de hospitales y carreteras pavimentadas."
      },
      {
        "type": "narration",
        "text": "Asimismo, el tejido económico de las remesas familiares y la emergencia de las familias transnacionales revelan la inagotable fuerza productiva y ética de la diáspora. Con decenas de miles de millones de dólares transferidos anualmente de forma directa y descentralizada a través de plataformas financieras digitales y aplicaciones móviles interoperables, los trabajadores migrantes rescatan de la precariedad alimentaria a sus seres queridos y dinamizan las economías de sus países de origen, al tiempo que tributan y generan riqueza formal en las sociedades receptoras. Esta circulación virtuosa de afectos y recursos demuestra que los lazos familiares son inmunes a las distancias kilométricas y que la solidaridad transfronteriza es un motor económico insustituible."
      },
      {
        "type": "narration",
        "text": "En conclusión, el mosaico cultural y humano que florece hoy en las barriadas populares de Lima, Bogotá, Santiago, São Paulo y Buenos Aires ratifica que en América del Sur late el sueño sagrado de la integración de los pueblos. A través de la gastronomía compartida, los ritmos musicales mestizos y las aulas escolares pluriculturales, nuestras sociedades derrotan cotidianamente los cantos de sirena de la xenofobia, transformando la diversidad de orígenes en la más bella promesa de futuro. Al asumir con orgullo este mandato de fraternidad imperecedero, las naciones del sur declaran al mundo entero que en la Patria Grande nadie es forastero y que la dignidad del migrante es la garantía irrenunciable de nuestra propia libertad colectiva. Reconocer al migrante como sujeto pleno de derechos y constructor de riqueza colectiva es la piedra basal sobre la cual se edifica el porvenir democrático de nuestra América."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué rasgo ético fundamental distinguió la respuesta de los países suramericanos ante el éxodo venezolano?",
            "options": [
              "El cierre militar absoluto de todos los pasos fronterizos con muros de hormigón.",
              "La articulación multilateral mediante el Proceso de Quito y la concesión de estatutos de protección y regularización masiva.",
              "La confiscación obligatoria de todos los bienes de los refugiados.",
              "La prohibición de prestar auxilio médico a los caminantes en las carreteras."
            ],
            "correctIndex": 1,
            "explanation": "América del Sur respondió con políticas pioneras de regularización temporal que otorgaron derechos laborales, educativos y de salud."
          },
          {
            "question": "¿Qué papel decisivo desempeñan las remesas familiares enviadas por la diáspora suramericana?",
            "options": [
              "Financian exclusivamente la especulación bursátil en plazas financieras del norte.",
              "Sostienen de forma directa y líquida la alimentación, la salud y la educación en millones de hogares vulnerables en los países de origen.",
              "Provocan la quiebra obligatoria de los bancos centrales locales.",
              "Impiden el uso de la moneda nacional en los comercios populares."
            ],
            "correctIndex": 1,
            "explanation": "Las remesas operan como una red directa de protección social que llega sin intermediarios a las familias necesitadas."
          },
          {
            "question": "¿Por qué se afirma que en la Patria Grande suramericana 'nadie es forastero'?",
            "options": [
              "Porque se reconoce que la historia continental está entretejida por el mestizaje y la solidaridad inalienable entre pueblos hermanos.",
              "Porque se exige la renuncia obligatoria a la nacionalidad de nacimiento a todos los ciudadanos.",
              "Porque se suprimen los pasaportes para viajar fuera del planeta Tierra.",
              "Porque las fronteras se reemplazan por barreras comerciales punitivas."
            ],
            "correctIndex": 0,
            "explanation": "La doctrina de la Patria Grande afirma que ningún habitante suramericano debe ser considerado extranjero en suelo continental común."
          }
        ]
      }
    }
  }
}

if __name__ == "__main__":
    for k, v in STORIES.items():
        full_text = " ".join(p["text"] for p in v["paragraphs"])
        cnt = word_count(full_text)
        print(f"{k}: {cnt} words (valid: {650 <= cnt <= 825})")
