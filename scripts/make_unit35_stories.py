"""
make_unit35_stories.py
Defines the 8 stories for Unit 35 and tests word counts.
"""
import re
import json

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

STORIES = {
  "classics/b2/b2-35": {
    "id": "b2-35",
    "title": "Los ríos profundos (José María Arguedas, 1958)",
    "level": "B2",
    "lesson": 1,
    "type": "classics",
    "estimatedMinutes": 15,
    "summary": "Estudio literario de la obra cumbre de José María Arguedas: el viaje iniciático de Ernesto entre el mundo quechua y la rigidez señorial hispánica; el internado religioso de Abancay, el zumbayllu mágico, la revuelta de las chicheras y la peste como purificación cósmica.",
    "characters": [
      "Ernesto (adolescente mestizo escindido entre el quechua y el castellano)",
      "El Viejo (terrateniente avaro, tío de Ernesto y personificación del orden feudal)",
      "El Padre Director (sacerdote rector del colegio religioso de Abancay)",
      "Doña Felipa (líder mestiza de la revuelta popular de las chicheras)",
      "Los internos del colegio (jóvenes de diversas clases y procedencias geográficas)"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Publicada en Buenos Aires en 1958 por la editorial Losada, 'Los ríos profundos' constituye la cima indiscutible de la narrativa de José María Arguedas y una de las exploraciones poéticas más deslumbrantes sobre el desgarramiento cultural en las letras universales. A través de la mirada sensible del joven Ernesto, alter ego autobiográfico del autor, la novela escenifica el drama íntimo de un muchacho educado con ternura infinita por los comuneros indios de los Andes, que es arrancado intempestivamente de ese paraíso animista y solidario para ser internado en un colegio religioso en la calurosa ciudad de Abancay. En este recinto cerrado, regido por una disciplina eclesiástica autoritaria y atravesado por violentas tensiones raciales, Ernesto experimenta la soledad del desarraigo mientras busca tender puentes afectivos entre la cosmovisión mágica quechua y el hermético mundo señorial hispánico. Aunado a ello, la novela indaga con sobrecogedora lucidez en las contradicciones lingüísticas y psicológicas del mestizaje, donde cada vocablo quechua reverbera como un manantial de afecto maternal mientras el castellano oficial opera como la lengua áspera de la ley y el escarnio."
      },
      {
        "type": "narration",
        "text": "El periplo se abre con la llegada de Ernesto y su padre errante a la monumental ciudad del Cusco, donde contemplan el muro incaico del palacio de Inca Roca y visitan al 'Viejo', un hacendado despótico, avaro e hipócrita que encarna la decadencia moral del feudalismo andino. Ante las piedras milenarias que parecen palpitar con vida propia bajo el sol implacable de la sierra, Ernesto descubre que la arquitectura autóctona no es una reliquia arqueológica inerte, sino una fuerza telúrica viva que resiste silenciosamente el paso de los siglos y la opresión colonial. Esta revelación mística marca el despertar ontológico del protagonista: la convicción inquebrantable de que la naturaleza, los ríos torrenciales y las piedras venerables poseen un lenguaje sagrado que solo los espíritus limpios y empáticos pueden descifrar en medio del caos social."
      },
      {
        "type": "narration",
        "text": "Instalado ya en el colegio de Abancay, Ernesto debe convivir con un microcosmos de alumnos que reproducen a escala menor las jerarquías despiadadas, los prejuicios étnicos y la crueldad soterrada de la sociedad peruana republicana. Frente a la hostilidad reinante, el trompo tradicional andino ('el zumbayllu') irrumpe en el patio como un objeto fascinante de reconciliación colectiva: su zumbido hipnótico, capaz de atrapar la luz y modular cantos celestiales, suspende momentáneamente las reyertas entre los muchachos y conecta a Ernesto con la música secreta de los valles andinos. El trompo no es un simple juguete infantil, sino un talismán poético que restablece la armonía cósmica y actúa como mensajero invisible hacia los seres queridos distantes, desafiando el aislamiento emocional de la reclusión escolar. Incluso en los momentos de mayor agobio y soledad, el zumbido cristalino del trompo infunde en el ánimo de Ernesto la certidumbre de que la poesía y la ternura poseen una fuerza redentora superior a cualquier despotismo."
      },
      {
        "type": "narration",
        "text": "La aparente tranquilidad del internado salta por los aires cuando estalla la revuelta popular de las chicheras, encabezada por la valerosa doña Felipa, quienes asaltan los almacenes de sal acaparada por las autoridades locales para repartirla entre los campesinos hambrientos de las alturas. Cautivado por la dignidad indómita de estas mujeres, Ernesto huye momentáneamente del colegio para unirse al coro insurgente, descubriendo en la rebeldía colectiva una fuerza moral limpia que desmiente la supuesta pasividad indígena. La posterior llegada del ejército para reprimir a las sublevadas y la cobarde sumisión del clero local ante los fusiles confirman en el muchacho la imposibilidad de conciliar la fe evangélica pura con las instituciones corruptas que legitiman el despojo secular de los más humildes."
      },
      {
        "type": "narration",
        "text": "Hacia el desenlace sobrecogedor, una epidemia devastadora de tifus azota el pueblo y diezma a las poblaciones pobres, desatando el pánico entre los señores de Abancay que huyen despavoridos de sus haciendas mientras los campesinos bajan en multitud silenciosa a exigir que se celebre una misa solemne por las almas de los afligidos. Abandonado en el internado vacío junto a los peones moribundos, Ernesto decide finalmente emprender la marcha solitaria hacia las tierras altas de su infancia, contemplando desde las riberas el imponente río Pachachaca que arrastra las aguas profundas hacia el mar infinito. En la prosa luminosa de Arguedas, el río purificador simboliza la resistencia invencible de los pueblos andinos, cuyo canto milenario jamás podrá ser silenciado por la injusticia humana."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué simboliza el trompo mágico ('el zumbayllu') en la vida de los alumnos del internado de Abancay?",
            "options": [
              "Un arma de fuego clandestina para amedrentar a las autoridades eclesiásticas.",
              "Un objeto poético y ritual capaz de suspender las discordias y conectar el alma con las fuerzas cósmicas andinas.",
              "Un instrumento científico utilizado por los profesores para impartir clases de física.",
              "Una moneda de cambio prohibida para comprar tabaco en las chicherías."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cuál es la causa del levantamiento popular liderado por doña Felipa en la ciudad de Abancay?",
            "options": [
              "La clausura gubernamental del río Pachachaca a los pescadores.",
              "El acaparamiento injusto de la sal por los grandes comerciantes en perjuicio de los campesinos humildes.",
              "La expulsión definitiva de los sacerdotes católicos de las escuelas públicas.",
              "El cobro de impuestos a las danzas folclóricas de carnaval."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cómo concluye la trayectoria de Ernesto en el desenlace de la novela?",
            "options": [
              "Consagrándose como sacerdote dominico en el convento de Santo Domingo.",
              "Emprendiendo la marcha solitaria hacia la cordillera junto al río purificador que arrastra las impurezas del mundo.",
              "Heredando las haciendas del Viejo en el valle del Cusco.",
              "Emigrando a Europa a bordo de un vapor comercial transatlántico."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-pluralismo-01": {
    "id": "b2-pluralismo-01",
    "title": "Del indigenismo tutelar a la autodeterminación comunitaria",
    "level": "B2",
    "lesson": 1,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Evolución histórica de los derechos indígenas en América Latina: el fin de las políticas asimilacionistas tutelares y la conquista de la autodeterminación territorial y comunitaria en el marco internacional del Convenio 169 de la OIT.",
    "characters": [
      "Líderes indígenas comunitarios y defensores de derechos colectivos",
      "Juristas especializados en derecho constitucional e internacional",
      "Autoridades comunales y representantes del Convenio 169 de la OIT"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Durante la mayor parte del siglo XX, las políticas públicas de los Estados hispanoamericanos hacia las naciones originarias estuvieron condicionadas por el paradigma del 'indigenismo tutelar'. Esta corriente ideológica, bienintencionada en sus postulados teóricos pero profundamente paternalista en sus aplicaciones prácticas, concebía al indígena como un menor de edad civil al que era menester 'civilizar', aculturar e integrar compulsivamente a la matriz económica criollo-mestiza a través de la castellanización forzosa y la parcelación individual de las tierras colectivas. Lejos de emancipar a las comunidades, este modelo institucional erosionó las autoridades tradicionales, desarticuló las formas ancestrales de propiedad comunal y relegó los saberes ancestrales al plano folclórico exótico. Aunado a ello, las constituciones republicanas consagraron durante décadas el principio de la homogeneidad cultural monocultural, negando de plano la existencia jurídica previa de las naciones que habitaban el continente desde hacía milenios. En efecto, los censos oficiales invisibilizaban sistemáticamente a las comunidades originarias bajo la categoría genérica de 'campesinos', pretendiendo despojar a los colectivos de su memoria identitaria para convertirlos en fuerza de trabajo asalariada desprovista de raíces."
      },
      {
        "type": "narration",
        "text": "Sin embargo, a partir de la década de 1970 emergió con fuerza imparable una nueva ola de movilización étnica y política que rechazó abiertamente el amparo tutelar de los ministerios estatales para exigir el reconocimiento incondicional de la libre autodeterminación de los pueblos. Impulsadas por federaciones amazónicas y andinas como la Confederación de Nacionalidades Indígenas del Ecuador (CONAIE) o las organizaciones quechuas y aymaras de Bolivia, estas luchas desplazaron el foco del asistencialismo individual hacia la titularidad colectiva de derechos inalienables sobre el territorio, la lengua y el gobierno propio. Los pueblos originarios afirmaron con rotundidad que no eran simples minorías marginadas necesitadas de caridad benéfica, sino naciones históricas dotadas de cosmovisiones soberanas y soberanía comunitaria plena sobre sus bienes comunes territoriales. Aunado a ello, las marchas históricas por la dignidad y el territorio que descendieron desde las cumbres andinas y las selvas orientales hacia las capitales metropolitanas quebraron para siempre la indiferencia ciudadana, forzando a los gobernantes a sentarse a deliberar de igual a igual."
      },
      {
        "type": "narration",
        "text": "Un hito jurídico de trascendencia universal se produjo en 1989 con la aprobación del Convenio 169 de la Organización Internacional del Trabajo (OIT) sobre Pueblos Indígenas y Tribales en Países Independientes, complementado posteriormente por la Declaración de las Naciones Unidas de 2007. Este cuerpo normativo internacional revolucionó el derecho público continental al establecer formalmente la obligación irrenunciable del consentimiento libre, previo e informado ante cualquier iniciativa legislativa o proyecto extractivo que pudiera alterar el hábitat comunal. A despecho de las persistentes resistencias de corporaciones transnacionales y sectores conservadores, el Convenio 169 blindó jurídicamente la posesión colectiva de las tierras ancestrales como condición sine qua non para la supervivencia física y espiritual de los pueblos."
      },
      {
        "type": "narration",
        "text": "En el plano constitucional, las reformas democráticas de finales del siglo XX y principios del siglo XXI en países como Colombia (1991), Bolivia (2009) y Ecuador (2008) redefinieron la naturaleza misma del Estado republicano, consagrando la doctrina del Estado pluricultural y plurinacional. Esta metamorfosis institucional reconoció a los resguardos y territorios indígenas el rango de entidades territoriales autónomas dotadas de facultades gubernativas, fiscales y ambientales propias. Asimismo, se establecieron circunscripciones electorales especiales y escaños reservados para asegurar que la voz indígena tuviera representación decisiva en los congresos legislativos nacionales, quebrando el monopolio histórico de las élites urbanas tradicionales sobre la esfera pública. Por consiguiente, la consolidación de estos avances jurídicos inauguró una nueva época republicana en la que la soberanía nacional se concibe indisolublemente ligada a la diversidad de los pueblos que integran el cuerpo social."
      },
      {
        "type": "narration",
        "text": "Hoy en día, la autodeterminación comunitaria enfrenta complejos dilemas contemporáneos, tales como la presión incesante de la minería aurífera ilegal, el narcotráfico y la expansión de la frontera agroindustrial sobre selvas vírgenes y cabeceras de cuenca. Frente a estos flagelos, las guardias indígenas desarmadas ejercen un control territorial pacífico admirable pero sumamente arriesgado, custodiando los linderos ancestrales con bastones de mando y sabiduría ancestral comunitaria. La transición desde el indigenismo asimilacionista hacia la soberanía comunitaria emancipada demuestra que el futuro democrático de América Latina no reside en la imposición uniformizadora, sino en el respeto reverente a la pluralidad viva de sus naciones fundacionales. Reconocer la autodeterminación comunitaria no debilita la cohesión democrática, sino que la refunde sobre cimientos de equidad, reconocimiento recíproco y fraternidad viva."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿En qué consistía el enfoque del 'indigenismo tutelar' predominante en el siglo XX?",
            "options": [
              "En promover la independencia militar inmediata de todas las comunidades originarias.",
              "En tratar al indígena como un menor de edad civil al que se debía integrar y aculturar compulsivamente al modelo nacional.",
              "En prohibir el uso del idioma castellano en los tribunales de justicia.",
              "En transferir todas las industrias petroleras a cooperativas rurales sin control estatal."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué garantía sustantiva consagra el Convenio 169 de la OIT frente a proyectos en tierras ancestrales?",
            "options": [
              "La venta forzosa de los recursos minerales al mejor postor privado.",
              "El derecho inalienable a la consulta y consentimiento libre, previo e informado de las comunidades afectadas.",
              "El desmantelamiento de las escuelas bilingües rurales.",
              "La disolución de los concejos de ancianos comunales."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué instrumento pacífico emplean las guardias indígenas para ejercer control territorial frente a invasiones ilegales?",
            "options": [
              "Armamento pesado suministrado por ejércitos extranjeros.",
              "Bastones de mando tradicionales, vigilancia comunitaria y movilización colectiva desarmada.",
              "Tratados comerciales firmados en bolsas de valores internacionales.",
              "Drones de combate no tripulados."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-pluralismo-02": {
    "id": "b2-pluralismo-02",
    "title": "Sistemas de justicia indígena y pluralismo jurídico en los Andes",
    "level": "B2",
    "lesson": 2,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Análisis comparativo de los sistemas de justicia indígena consuetudinaria: principios de sanación y reparación frente al derecho punitivo estatal; deslinde jurisdiccional, coordinación interjurisdiccional y respeto irrestricto a los derechos humanos.",
    "characters": [
      "Jueces comunales y autoridades de rondas campesinas",
      "Magistrados de cortes constitucionales nacionales",
      "Comuneros y mediadores comunitarios andinos"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "El pluralismo jurídico constituye uno de los avances más revolucionarios en el derecho contemporáneo de América Latina, al poner fin al dogma decimonónico del monismo jurídico según el cual solo el Estado tiene el monopolio legítimo de dictar y administrar justicia. En países con densas poblaciones originarias como Bolivia, Perú, Ecuador, Colombia y Guatemala, los sistemas jurídicos indígenas —arraigados en el derecho consuetudinario y en prácticas inmemoriales de autorregulación social— operan cotidianamente con plena validez vinculante en sus jurisdicciones territoriales. Este reconocimiento no representa una concesión graciosa del poder central, sino la legitimación formal de instituciones normativas ancestrales que han garantizado el orden pacífico y la cohesión comunitaria durante siglos frente al abandono o la violencia del aparato judicial formal. Asimismo, este reconocimiento constitucional consagra el derecho fundamental de los comuneros a ser juzgados según sus propias costumbres por sus autoridades naturales, preservando la identidad colectiva frente a la despersonalización del litigio formal."
      },
      {
        "type": "narration",
        "text": "A diferencia del sistema penal ordinario, caracterizado por una lógica punitiva, carcelaria y retributiva orientada a aislar al infractor mediante el encierro carcelario oneroso, la justicia indígena privilegia la reparación del daño moral y material, la sanación comunitaria y la reintegración plena de la persona al tejido social. Cuando un miembro de la comunidad comete un delito o genera una discordia grave, las autoridades originarias convocan a la asamblea comunal para escuchar a todas las partes en un diálogo público transparente. Las sanciones impuestas —que pueden abarcar trabajos comunitarios intensivos, devolución del ganado hurtado, baños de purificación con hierbas amargas o amonestaciones públicas solemnes ante los ancianos— buscan restablecer el equilibrio armónico entre la persona, la comunidad y las energías de la naturaleza. En efecto, mientras el encierro penitenciario desintegra el núcleo familiar y deja desamparadas a las víctimas, la asamblea comunal asegura que el agresor asuma personalmente la reparación del daño mediante la siembra de parcelas o el levantamiento de cercos comunales."
      },
      {
        "type": "narration",
        "text": "Un ejemplo elocuente de este pluralismo normativo lo constituyen las célebres Rondas Campesinas del norte del Perú, surgidas en la década de 1970 para combatir el abigeato y la delincuencia en valles olvidados por la policía republicana. Dotadas de legitimidad comunitaria indiscutible y amparadas hoy por la Constitución de 1993 y la Ley Especial de Rondas Campesinas, estas organizaciones administran justicia rápida, gratuita y eficaz en sus territorios. Las decisiones adoptadas en sus asambleas gozan de valor de cosa juzgada para los tribunales ordinarios, siempre y cuando no vulneren los derechos humanos fundamentales consagrados en los tratados internacionales, tales como el derecho a la vida, la integridad física y la prohibición absoluta de la tortura. Por añadidura, la ausencia de costos procesales y la inmediatez de las deliberaciones orales impiden que los litigios se dilaten indefinidamente durante décadas en anaqueles polvorientos."
      },
      {
        "type": "narration",
        "text": "Sin embargo, la coexistencia armónica entre la justicia ordinaria y la justicia comunitaria exige resolver complejos desafíos procesales englobados bajo la doctrina del 'deslinde jurisdiccional'. Con frecuencia, fiscales y jueces ordinarios, formados en una dogmática positivista rígida y eurocéntrica, intentan criminalizar a las autoridades indígenas que aplican justicia consuetudinaria, acusándolas indebidamente de secuestro o usurpación de funciones. Para subsanar estos roces, tribunales de vanguardia como la Corte Constitucional de Colombia o el Tribunal Constitucional Plurinacional de Bolivia han desarrollado una rica jurisprudencia intercultural que establece pautas claras de respeto mutuo, no intromisión y colaboración interjurisdiccional armónica. Del mismo modo, las comisiones mixtas de coordinación interjurisdiccional han permitido canalizar casos complejos de violencia de género y narcotráfico hacia fiscalías especializadas, respetando los ámbitos competenciales propios."
      },
      {
        "type": "narration",
        "text": "En última instancia, el pluralismo jurídico demuestra que la justicia no se agota en códigos decimonónicos redactados en latín ni en fríos despachos judiciales burocráticos ajenos a las realidades humanas de la periferia. Al colocar la verdad material, la reconciliación comunitaria y la palabra empeñada en el centro del acto de juzgar, los sistemas normativos indígenas ofrecen una lección inspiradora de sabiduría procesal y efectividad democrática. Lejos de fragmentar el orden constitucional, el diálogo honesto entre tradiciones jurídicas diversas fortalece la legitimidad global del Estado de derecho y acerca la justicia a las vivencias cotidianas de la ciudadanía plural. La sabiduría procesal andina recuerda que la paz comunitaria es un bien supremo que jamás puede alcanzarse mediante la simple imposición punitiva de una condena."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuál es la premisa fundamental que diferencia a la justicia comunitaria indígena del derecho penal ordinario?",
            "options": [
              "La aplicación obligatoria de penas de prisión perpetua en recintos de máxima seguridad.",
              "La búsqueda primordial de la reparación del daño, la sanación colectiva y la reconciliación comunitaria frente a la lógica punitiva carcelaria.",
              "La exclusión de los testimonios orales durante los juicios.",
              "El pago obligatorio de honorarios a abogados colegiados en moneda extranjera."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué límite inexcusable imponen los tratados internacionales a las decisiones de la justicia consuetudinaria?",
            "options": [
              "La obligación de celebrar todos los juicios en idioma latín.",
              "El respeto irrestricto a los derechos humanos fundamentales, como el derecho a la vida y la prohibición absoluta de la tortura.",
              "La supervisión militar obligatoria de cada asamblea comunal.",
              "La prohibición de aplicar trabajos comunitarios como sanción reparadora."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué fenómeno histórico motivó el nacimiento de las Rondas Campesinas en el Perú?",
            "options": [
              "La necesidad comunitaria de combatir el robo de ganado (abigeato) y la indefensión ante la ausencia policial en zonas rurales.",
              "Un decreto ministerial dictado por el Banco Central de Reserva.",
              "La construcción de una red de ferrocarriles transatlánticos.",
              "La regulación de las exportaciones de harina de pescado."
            ],
            "correctIndex": 0
          }
        ]
      }
    }
  },
  "world/b2/b2-pluralismo-03": {
    "id": "b2-pluralismo-03",
    "title": "Los ríos y bosques como sujetos de derecho: La jurisprudencia ecológica",
    "level": "B2",
    "lesson": 3,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "La revolución de la jurisprudencia biocéntrica en Suramérica: el reconocimiento de ríos como el Atrato y la Amazonía como sujetos de derechos; la superación del antropocentrismo legal inspirada en el Sumak Kawsay andino-amazónico.",
    "characters": [
      "Magistrados constitucionales y relatores ambientales",
      "Guardianes comunitarios de ríos y cuencas hidrográficas",
      "Activistas ecologistas y peritos científicos en biodiversidad"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "En las primeras décadas del siglo XXI, América Latina se ha consolidado a la vanguardia jurídica planetaria mediante una transformación paradigmática sin precedentes: el paso del antropocentrismo jurídico tradicional hacia el biocentrismo y el reconocimiento formal de la Naturaleza como sujeto de derechos inalienables. Históricamente, el derecho occidental concibió a los ríos, selvas y montañas como meros 'recursos naturales' u objetos inanimados susceptibles de explotación económica, apropiación mercantil y degradación ambiental sin límites éticos. Frente a esta visión extractivista depredadora, la incorporación del principio andino del 'Buen Vivir' (*Sumak Kawsay* en quechua, *Suma Qamaña* en aymara) en las constituciones de Ecuador y Bolivia abrió una senda jurídica inédita que concibe a la Tierra como un organismo vivo dotado de dignidad moral intrínseca. Aunado a ello, la acelerada degradación de los ecosistemas globales exige superar las categorías antropocéntricas heredadas del derecho romano, reconociendo que los seres humanos somos parte indisociable de la trama de la vida y no sus dueños absolutos."
      },
      {
        "type": "narration",
        "text": "El pronunciamiento judicial más influyente de esta corriente emancipadora se materializó en Colombia con la histórica Sentencia T-622 de 2016 de la Corte Constitucional, que declaró al río Atrato, su cuenca y sus afluentes como 'sujeto de derechos' a la protección, conservación, mantenimiento y restauración integral. Esta decisión paradigmática no surgió de un laboratorio académico abstracto, sino de la acción de tutela interpuesta por comunidades afrodescendientes e indígenas del departamento del Chocó, cuyas vidas, tradiciones pesqueras y salud colectiva se hallaban gravemente amenazadas por el vertimiento descontrolado de mercurio y cianuro procedente de la minería ilegal y la deforestación mecanizada de las riberas. En efecto, el dragado indiscriminado y el vertimiento masivo de mercurio no solo devastaban las faenas artesanales de pesca, sino que envenenaban la leche materna y generaban graves anomalías congénitas en los infantes de las comunidades ribereñas."
      },
      {
        "type": "narration",
        "text": "La innovación más fecunda de la sentencia radicó en la creación de un modelo de gobernanza ecológica compartida: la designación formal de un cuerpo colegiado de 'guardianes del río Atrato', conformado de manera paritaria por un delegado del Gobierno nacional y representantes de las comunidades étnicas ribereñas. De esta manera, el río deja de ser un espacio inerte administrado por burócratas lejanos para convertirse en una entidad jurídica viva cuya voz y bienestar son tutelados activamente por quienes han convivido ancestralmente con sus aguas. Este modelo de ecoderecho garantiza que las decisiones sobre remediación ambiental,Dragado y descontaminación fluvial se adopten con la participación protagónica de los pueblos locales. Asimismo, este esquema de gobernanza participativa convoca a científicos independientes, peritos botánicos y líderes espirituales a sesionar conjuntamente para vigilar la calidad de los afluentes y la reforestación de las cuencas."
      },
      {
        "type": "narration",
        "text": "Siguiendo esta luminosa estela jurisprudencial, la Corte Suprema de Justicia de Colombia reconoció en 2018 a la Amazonía colombiana en su conjunto como sujeto de derechos, ordenando al Estado formular un pacto intergeneracional urgente para detener la deforestación y salvaguardar el equilibrio climático global. Pronunciamientos similares han florecido a lo largo del continente: en Ecuador, la Corte Constitucional protegió los bosques nubosos de Los Cedros frente a la gran minería basándose en los derechos de la Naturaleza; en Argentina, los tribunales ampararon a grandes primates como personas no humanas dotadas de libertad fundamental; y en el Perú se multiplican las demandas para proteger al río Marañón y sus nacientes sagradas. Por consiguiente, las decisiones de las altas cortes latinoamericanas han sentado precedentes insoslayables citados hoy con admiración en tribunales de Nueva Zelanda, Canadá, la India y la Unión Europea."
      },
      {
        "type": "narration",
        "text": "Esta fecundación cruzada entre la sabiduría milenaria de los pueblos originarios y los instrumentos del constitucionalismo moderno demuestra que el derecho no es un monumento estático al servicio de la dominación, sino una herramienta viva capaz de ensanchar los horizontes de la compasión y la supervivencia planetaria. Al proclamar que los ríos, selvas y glaciares tienen derecho a fluir limpios y a regenerar sus ciclos vitales con autonomía, la jurisprudencia suramericana desafía la soberbia humana y postula un nuevo pacto civilizatorio: comprender que defender la dignidad de la Tierra es, en última instancia, salvaguardar el porvenir de la propia especie humana. Reconocer a los ríos como seres vivos con derechos propios es la manifestación jurídica más elevada de nuestra responsabilidad moral hacia la comunidad de la vida planetaria."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué innovación jurídica decisiva consagró la Sentencia T-622 de la Corte Constitucional colombiana respecto al río Atrato?",
            "options": [
              "La privatización de todas sus aguas para embotelladoras transnacionales.",
              "La declaración del río, su cuenca y sus afluentes como sujeto de derechos a la protección, conservación y restauración.",
              "La prohibición total de la navegación comunitaria en canoas.",
              "La construcción de una autopista de ocho carriles sobre el cauce fluvial."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Quiénes integran el cuerpo colegiado de 'guardianes' creado para velar por los derechos del río Atrato?",
            "options": [
              "Representantes paritarios del Estado y delegados de las comunidades afrodescendientes e indígenas ribereñas.",
              "Exclusivamente auditores de bancos financieros internacionales.",
              "Agentes de seguridad privada contratados por empresas mineras.",
              "Compañías de seguros de transporte marítimo extranjero."
            ],
            "correctIndex": 0
          },
          {
            "question": "¿Qué concepto filosófico andino inspiró la consagración de los Derechos de la Naturaleza en las constituciones suramericanas?",
            "options": [
              "El materialismo dialéctico soviético.",
              "El Sumak Kawsay o Buen Vivir, que concibe a la Tierra como un ser vivo dotado de dignidad moral y equilibrio cósmico.",
              "El individualismo utilitarista de la Escuela de Chicago.",
              "La doctrina mercantilista colonial del siglo XVI."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-pluralismo-04": {
    "id": "b2-pluralismo-04",
    "title": "Educación intercultural bilingüe y revitalización lingüística digital",
    "level": "B2",
    "lesson": 4,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Políticas públicas de educación intercultural bilingüe (EIB) en América Latina: rescate de lenguas originarias amenazadas, producción curricular descolonizadora y uso de tecnologías digitales y aplicaciones móviles para la soberanía lingüística.",
    "characters": [
      "Maestros bilingües rurales y pedagogos interculturales",
      "Activistas lingüísticos digitales y desarrolladores de software comunitario",
      "Jóvenes hablantes de lenguas indígenas originarias"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Durante décadas, la escuela pública rural en América Latina operó como el principal instrumento homogeneizador y desindianizador del Estado republicano. Mediante castigos físicos humillantes, burlas y la prohibición estricta de hablar idiomas originarios en el aula, generaciones enteras de niños quechuas, aymaras, mayas, guaraníes y mapuches fueron forzadas a olvidar sus lenguas maternas para adoptar el castellano estándar como única vía de ascenso social y ciudadanía. Esta violencia epistémica provocó una pérdida lingüística catastrófica, induciendo a muchos padres campesinos a no transmitir su lengua a sus hijos para evitarles el dolor de la discriminación racial en las urbes. Frente a esta tragedia civilizatoria, la emergencia de la Educación Intercultural Bilingüe (EIB) a finales del siglo XX supuso una victoria histórica irrenunciable. Aunado a ello, la discriminación escolar infundía en los alumnos un doloroso sentimiento de vergüenza lingüística que fracturaba los lazos afectivos intergeneracionales en el seno de las familias indígenas."
      },
      {
        "type": "narration",
        "text": "La EIB se fundamenta en un principio pedagógico y ético elemental: ningún niño debe ser despojado de su lengua materna para acceder al conocimiento universal, pues el idioma es la morada íntima del pensamiento, la memoria histórica y la afectividad humana. Lejos de reducirse a un mero método transicional para acelerar la castellanización, los programas modernos de educación bilingüe conciben el bilingüismo aditivo como una fortaleza cognitiva suprema: los estudiantes aprenden a leer, escribir, razonar matemáticamente y reflexionar críticamente tanto en su idioma originario como en castellano. Asimismo, la EIB descoloniza los contenidos escolares, incorporando a los libros de texto los saberes ancestrales sobre botánica medicinal, astronomía andina, manejo de cuencas y calendarios agrícolas comunitarios. En efecto, los estudios psicolingüísticos modernos confirman que los niños que consolidan la lectoescritura en su lengua vernácula aprenden una segunda lengua con mayor rapidez, flexibilidad conceptual y rendimiento académico sobresaliente."
      },
      {
        "type": "narration",
        "text": "El marco normativo contemporáneo en países como Paraguay —donde el guaraní goza de estatus cooficial pleno y es impartido obligatoriamente en todas las escuelas— o en Bolivia y Perú, donde se han normalizado y oficializado decenas de alfabetos indígenas, respalda esta primavera pedagógica. Sin embargo, los desafíos materiales continúan siendo abrumadores: persiste la escasez crónica de docentes bilingües acreditados, la asignación presupuestaria estatal para materiales didácticos impresos suele ser deficiente y muchas comunidades rurales carecen de infraestructura básica adecuada. Aun así, la tenacidad de maestras y maestros rurales mantiene encendida la llama de la enseñanza comunitaria en los rincones más apartados de la geografía continental. Por consiguiente, la formación continua de formadores bilingües y la producción de textos pedagógicos adaptados a la realidad cultural de cada cuenca fluvial constituyen inversiones estratégicas insustituibles."
      },
      {
        "type": "narration",
        "text": "En el siglo XXI, una vibrante vanguardia de jóvenes activistas lingüísticos ha trasladado la defensa de las lenguas originarias al ciberespacio y a las plataformas digitales, quebrando el prejuicio de que los idiomas indígenas son reliquias arcaicas incompatibles con la modernidad tecnológica. En Perú, México, Guatemala y Colombia florecen aplicaciones móviles para el aprendizaje gamificado de lenguas como el quechua collao, el zapoteco o el náhuatl; canales de YouTube y pódcasts juveniles donde se difunden canciones de hip-hop y cumbia en aymara; y colectivos de traductores voluntarios que han localizado sistemas operativos de código abierto y navegadores web a lenguas ancestrales. Asimismo, estas iniciativas juveniles desmantelan los estereotipos folklorizantes, demostrando que la cultura originaria posee un dinamismo estético y una inventiva técnica capaces de enriquecer las vanguardias globales."
      },
      {
        "type": "narration",
        "text": "Esta alianza fecunda entre la memoria oral inmemorial y la interactividad digital demuestra que las lenguas originarias poseen una vitalidad y plasticidad expresiva asombrosas, capaces de nombrar los dilemas de la inteligencia artificial, el cambio climático y la vida metropolitana contemporánea. Revitalizar una lengua no es solo conservar un vocabulario exótico en diccionarios académicos, sino salvaguardar una ventana única e irrepetible para comprender el misterio del universo y el valor de la dignidad comunitaria. En una América Latina plenamente consciente de su riqueza plural, cada palabra recuperada en una lengua originaria es un himno a la libertad y a la resistencia humana. La lengua es el cauce donde navegan los sueños y las esperanzas de los pueblos, y su preservación fortalece la pluralidad del conocimiento universal."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuál es el postulado central que diferencia a la Educación Intercultural Bilingüe moderna del viejo modelo escolar rural?",
            "options": [
              "La sustitución inmediata de todas las asignaturas por clases de gimnasia.",
              "El fomento del bilingüismo aditivo, donde el alumno aprende en su lengua materna y en castellano valorando sus saberes ancestrales.",
              "La prohibición de enseñar ciencias exactas y matemáticas en las escuelas comunitarias.",
              "La obligación de hablar exclusivamente dialectos europeos antiguos."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿En qué país suramericano goza el idioma guaraní de reconocimiento cooficial pleno y enseñanza obligatoria generalizada?",
            "options": [
              "En el Uruguay.",
              "En el Paraguay.",
              "En Surinam.",
              "En Chile."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cómo contribuyen los jóvenes activistas indígenas actuales a la revitalización de sus lenguas ancestrales?",
            "options": [
              "Creando aplicaciones móviles, pódcasts, música urbana contemporánea y localizando software digital en idiomas originarios.",
              "Clausurando el acceso a internet en las comunidades rurales.",
              "Renunciando por completo a la escritura alfabética.",
              "Exigiendo que no se traduzcan libros a otros idiomas."
            ],
            "correctIndex": 0
          }
        ]
      }
    }
  },
  "world/b2/b2-pluralismo-05": {
    "id": "b2-pluralismo-05",
    "title": "Mujeres indígenas en la primera línea de la defensa territorial",
    "level": "B2",
    "lesson": 5,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "El liderazgo insustituible de las lideresas indígenas en la protección de los ecosistemas latinoamericanos: ecofeminismo comunitario, preservación de semillas nativas y resistencia pacífica ante la violencia extractivista.",
    "characters": [
      "Lideresas y sabias comunitarias indígenas",
      "Defensoras ambientales y guardianas de semillas nativas",
      "Relatoras de derechos humanos y juristas de género"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "En el complejo tablero de las disputas socioambientales que sacuden a América Latina, las mujeres indígenas se han erigido en la vanguardia moral, política y organizativa más valiente de la resistencia comunitaria frente al avance desmedido de los megaproyectos extractivistas, la tala ilegal de maderas preciosas y la contaminación industrial de las cuencas fluviales. Articulando lo que en la teoría crítica contemporánea se denomina 'ecofeminismo comunitario' o feminismo territorial, estas lideresas sostienen con lucidez que la violencia patriarcal que oprime el cuerpo de las mujeres y la explotación capitalista depredadora que desgarra el cuerpo de la Madre Tierra son dos caras inseparables de una misma lógica de dominación y despojo. Aunado a ello, las lideresas comunitarias denuncian que la instalación no consensuada de campamentos mineros altera profundamente la vida cotidiana, disparando los índices de violencia intrafamiliar y precarizando los medios de subsistencia de las mujeres."
      },
      {
        "type": "narration",
        "text": "Históricamente marginadas tanto por las estructuras coloniales del Estado como por ciertas prácticas patriarcales arraigadas en el interior de sus propias comunidades, las mujeres indígenas han transformado los roles tradicionales de cuidado familiar en poderosos instrumentos de defensa colectiva del territorio. Al ser las depositarias consuetudinarias de la soberanía alimentaria, la custodia de los bancos comunitarios de semillas nativas, la recolección de plantas medicinales y la transmisión oral de las historias fundacionales a los infantes, ellas son las primeras en advertir cómo el secado de una vertiente o la intoxicación de un río con metales pesados destruye irremediablemente la vida comunitaria. En efecto, la protección de las variedades nativas de papa, quinua, frijol y maíz criollo ante la contaminación de semillas transgénicas constituye un pilar esencial de la soberanía alimentaria de todo el continente."
      },
      {
        "type": "narration",
        "text": "Liderazgos emblemáticos como el de la mártir lenca Berta Cáceres en Honduras —asesinada impunemente en 2016 por su férrea oposición pacífica a la construcción de una represa hidroeléctrica en el sagrado río Gualcarque—, o la voz firme de la líder waorani Nemonte Nenquimo en la Amazonía ecuatoriana, quien lideró una histórica demanda judicial que protegió medio millón de acres de selva virgen frente a la explotación petrolera, han conmovido la conciencia global y demostrado que la resistencia pacífica de las mujeres puede doblegar a gigantes corporativos y gobiernos indolentes. Incluso en contextos de persecución judicial y campañas sistemáticas de difamación mediática, las mujeres indígenas han tejido alianzas transnacionales ejemplares con universidades, asambleas ciudadanas y redes feministas globales."
      },
      {
        "type": "narration",
        "text": "Sin embargo, el costo humano de esta entrega sigue siendo desoladoramente elevado: según informes de organismos internacionales de derechos humanos, América Latina es la región más mortífera del planeta para los defensores de la tierra y del medio ambiente, recayendo sobre las mujeres una violencia diferenciada que combina el hostigamiento judicial, la estigmatización misógina y la amenaza constante de violencia sexual o feminicidio territorial. Frente a este panorama hostil, la entrada en vigor del Acuerdo de Escazú en 2021 —el primer tratado ambiental regional que consagra disposiciones vinculantes para la protección de personas defensoras de derechos humanos en asuntos ambientales— representa un escudo jurídico multilateral fundamental que debe ser implementado con urgencia. Por consiguiente, la exigibilidad del Acuerdo de Escazú no solo demanda reformas penales, sino la dotación de refugios seguros, medidas cautelares inmediatas y apoyo psicosocial integral para las lideresas amenazadas."
      },
      {
        "type": "narration",
        "text": "La voz inextinguible de las guardianas de la tierra nos recuerda con urgencia poética que la supervivencia de la humanidad no dependerá de fórmulas tecno-económicas frías, sino de nuestra capacidad para restablecer una relación de ternura, reciprocidad y respeto sagrado con los ciclos vitales de la naturaleza. Al marchar con sus hijos a cuestas, entonar cánticos ancestrales en las audiencias judiciales y proteger los ríos con sus propios cuerpos frente a las maquinarias pesadas, las mujeres indígenas de nuestra América siembran la semilla de un porvenir donde la dignidad humana y el latido del planeta florezcan en indivisible armonía. Custodiar la vida silvestre y los manantiales no es una opción secundaria, sino la labor más urgente y digna a la que puede consagrarse la inteligencia humana en este cambio de época."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué postula el concepto de 'ecofeminismo comunitario' abanderado por las mujeres indígenas?",
            "options": [
              "Que la protección ambiental debe delegarse exclusivamente en empresas extranjeras de seguros.",
              "Que la dominación violenta del cuerpo de las mujeres y la explotación destructiva de la Madre Tierra forman parte de una misma lógica de opresión.",
              "Que las mujeres no deben participar en la administración de la justicia comunitaria.",
              "Que los recursos hídricos deben privatizarse mediante subastas públicas."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué logro histórico alcanzó la lideresa waorani Nemonte Nenquimo en los tribunales ecuatorianos?",
            "options": [
              "La autorización para construir refinerías petroleras en el corazón del Parque Yasuní.",
              "Una sentencia judicial que protegió medio millón de acres de selva amazónica ancestral contra licitaciones petroleras.",
              "La compra privada de una flota de aviones de carga comercial.",
              "La expulsión definitiva de los biólogos de la cuenca amazónica."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué avance trascendental consagra el Acuerdo de Escazú ratificado en 2021?",
            "options": [
              "Disposiciones jurídicas vinculantes para la protección efectiva y garantías de seguridad de personas defensoras del medio ambiente.",
              "La prohibición de celebrar tratados de derechos humanos en el continente.",
              "La reducción de impuestos a las industrias mineras a cielo abierto.",
              "La clausura de todas las organizaciones indígenas de base."
            ],
            "correctIndex": 0
          }
        ]
      }
    }
  },
  "world/b2/b2-pluralismo-consolidation": {
    "id": "b2-pluralismo-consolidation",
    "title": "Síntesis: Raíces ancestrales y justicia comunitaria del siglo XXI",
    "level": "B2",
    "lesson": 6,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Estudio sintético sobre las conquistas del pluralismo jurídico y la autodeterminación indígena en Suramérica: balance de la gobernanza biocéntrica, educación bilingüe y desafíos contemporáneos frente a la globalización.",
    "characters": [
      "Líderes indígenas, juristas constitucionales y pedagogos interculturales"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "El balance panorámico de las transformaciones jurídicas, políticas y culturales analizadas a lo largo de esta unidad revela que América Latina ha transitado un camino civilizatorio extraordinario en sus últimas cuatro décadas de vida democrática. Del viejo paradigma asimilacionista republicano, que soñaba con borrar la pluralidad étnica en aras de una homogeneidad mestiza forzada, el continente ha evolucionado hacia la consagración del Estado plurinacional, el pluralismo jurídico y la autodeterminación comunitaria. Este cambio de rumbo no solo ha dignificado a más de ochocientos pueblos indígenas que custodian casi la mitad de los bosques primarios del continente, sino que ha enriquecido la teoría constitucional universal con aportes conceptuales de incalculable valor ético y pedagógico. Aunado a ello, el protagonismo de las organizaciones originarias en los debates constitucionales ha demostrado que la descolonización del Estado no es una quimera retórica, sino una práctica institucional cotidiana en permanente construcción."
      },
      {
        "type": "narration",
        "text": "En el terreno de la administración de justicia, la legitimación de los sistemas consuetudinarios ha evidenciado que la resolución de conflictos no requiere necesariamente de barrocos códigos procesales ni de la frialdad punitiva del encierro carcelario masivo. Al situar la reparación del daño tangible, la armonía espiritual y la reintegración comunitaria en el corazón del acto decisorio, los jueces y autoridades ancestrales ofrecen una respuesta mucho más humana, rápida y efectiva a los problemas de convivencia cotidiana que la lenta y a menudo inaccesible justicia ordinaria. La coexistencia coordinada de ambos órdenes, bajo el marco orientador de los derechos humanos universales, sienta las bases de un Estado verdaderamente plural y cercano al ciudadano. En efecto, las audiencias comunales al aire libre, donde toda la comunidad escucha, reflexiona y delibera serenamente sobre las causas profundas del disenso, devuelven a la justicia su sentido primigenio de reconciliación fraterna."
      },
      {
        "type": "narration",
        "text": "Asimismo, la revolucionaria doctrina de los Derechos de la Naturaleza y el nombramiento de ríos sagrados como sujetos jurídicos tutelados por guardianes comunitarios sitúan a nuestra región a la vanguardia de la gobernanza biocéntrica planetaria. Frente a la emergencia climática global y la extinción masiva de especies provocada por el extractivismo voraz, la jurisprudencia suramericana demuestra que los bienes comunes como el agua limpia, la biodiversidad de los páramos y la integridad de las selvas no son mercancías transables, sino patrimonios biológicos sagrados cuya conservación es un deber moral indelegable hacia las generaciones venideras. Asimismo, la consideración de los ecosistemas como sujetos jurídicos titulares de protección inaugura una ética del cuidado intergeneracional indispensable para conjurar el colapso ecológico de la biosfera."
      },
      {
        "type": "narration",
        "text": "En el ámbito de la transmisión cultural y la educación, la consolidación de la Educación Intercultural Bilingüe, reforzada por la audacia de los nuevos activismos digitales comunitarios, está desarmando los prejuicios coloniales que confinaban las lenguas originarias al silencio de los valles apartados. Ver hoy a jóvenes quechuas, mayas o guaraníes debatir sobre tecnología, componer música contemporánea y crear aplicaciones móviles en sus idiomas nativos es la prueba irrebatible de que la tradición y la innovación no son fuerzas antagónicas, sino vertientes complementarias que nutren la soberanía cultural y la autoestima de los pueblos. Por consiguiente, la difusión de plataformas digitales comunitarias en lenguas ancestrales garantiza que los saberes milenarios sobre medicina y conservación del suelo se transmitan con orgullo a las generaciones del siglo XXI."
      },
      {
        "type": "narration",
        "text": "Finalmente, el heroico testimonio de las mujeres indígenas en la defensa comunitaria del territorio nos interroga sobre el modelo de desarrollo que deseamos forjar para el siglo XXI. Su resistencia cotidiana demuestra que no hay justicia social posible sin justicia ambiental, ni reconciliación democrática duradera sin escuchar la voz de quienes han protegido la Tierra desde el principio de los tiempos. América Latina camina así hacia su madurez histórica: abrazando con orgullo sus raíces milenarias para proyectar desde el sur un mensaje de esperanza, sabiduría plural y fraternidad universal para toda la humanidad. Reconocer la sabiduría de los pueblos originarios es el acto de madurez histórica que permitirá a América Latina edificar un porvenir democrático, solidario y en comunión con la Madre Tierra."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuál es la lección primordial que aporta el pluralismo jurídico al constitucionalismo contemporáneo?",
            "options": [
              "Que la justicia formal debe imponer penas de cárcel a cualquier manifestación de disenso.",
              "Que la armonía social y la resolución de conflictos se fortalecen mediante la reparación del daño y el reconocimiento de tradiciones jurídicas ancestrales.",
              "Que todos los tribunales deben abolir los tratados internacionales de derechos humanos.",
              "Que el derecho civil debe redactarse exclusivamente en un idioma extranjero."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Por qué es crucial la doctrina biocéntrica de los Derechos de la Naturaleza ante la crisis climática?",
            "options": [
              "Porque permite subastar los ríos al mejor postor corporativo.",
              "Porque reconoce que los ecosistemas son entidades vivas con derecho a la regeneración y conservación más allá de su utilidad mercantil.",
              "Porque clausura la investigación científica en las universidades públicas.",
              "Porque prohíbe el uso de energías limpias renovables."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué demuestra la combinación de educación bilingüe y tecnologías digitales comunitarias?",
            "options": [
              "Que las lenguas originarias poseen una vitalidad contemporánea plena capaz de convivir y florecer con la innovación moderna.",
              "Que el ciberespacio debe prohibir el uso de idiomas distintos al inglés.",
              "Que la juventud rural abandona irreversiblemente todas sus tradiciones orales.",
              "Que los diccionarios impresos deben quemarse por obsoletos."
            ],
            "correctIndex": 0
          }
        ]
      }
    }
  },
  "world/b2/b2-pluralismo": {
    "id": "b2-pluralismo",
    "title": "Visión general: El pluralismo jurídico y la autodeterminación en Suramérica",
    "level": "B2",
    "lesson": 1,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Panorama exhaustivo de las innovaciones jurídicas y políticas indígenas en América Latina: autodeterminación, justicia consuetudinaria, derechos de la naturaleza, educación intercultural y liderazgo de las mujeres en la protección planetaria.",
    "characters": [
      "Pueblos originarios y autoridades comunales de América Latina",
      "Guardianes biocéntricos y magistrados constitucionales"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "El siglo XXI asiste a una refundación conceptual y política de América Latina impulsada por el vigor inextinguible de los pueblos originarios, quienes tras siglos de silenciamiento, colonialismo y despojo han conquistado un lugar central en la definición de la identidad continental. La noción misma de soberanía estatal ha sido interpelada profundamente: frente al viejo Estado republicano monocultural y centralista, herencia de las élites decimonónicas que concebían la unidad nacional como uniformidad obligatoria, emerge hoy la concepción del Estado plurinacional y pluricultural, donde la diversidad lingüística, jurídica y epistémica se reconoce no como un problema a resolver, sino como el mayor tesoro civilizatorio de nuestra América. Aunado a ello, la emergencia de las guardias indígenas comunitarias y los consejos territoriales autónomos consolida un modelo de seguridad ciudadana preventiva, desarmada y sustentada en la autoridad moral de las asambleas populares."
      },
      {
        "type": "narration",
        "text": "En esta encrucijada histórica, el pluralismo jurídico se erige como un baluarte insustituible para garantizar el acceso efectivo a la justicia de millones de campesinos y comuneros que habitan en las geografías andinas, amazónicas y centroamericanas. Lejos de constituir un régimen arcaico, la justicia consuetudinaria indígena destaca por su celeridad, transparencia asamblearia y vocación eminentemente reparadora, orientada a restaurar el equilibrio social quebrantado antes que a destruir al infractor mediante la deshumanización del sistema penitenciario tradicional. Esta complementariedad interjurisdiccional oxigena el derecho público y enriquece la convivencia democrática. En efecto, la complementariedad entre los tribunales constitucionales y la justicia indígena consuetudinaria demuestra que el pluralismo normativo enriquece y fortalece la solidez del Estado social de derecho."
      },
      {
        "type": "narration",
        "text": "Paralelamente, la irrupción de la jurisprudencia biocéntrica inspirada en el Sumak Kawsay o Buen Vivir ha desarmado las premisas utilitaristas del derecho occidental. Al declarar que ríos sagrados como el Atrato, bosques nubosos y biomas enteros como la Amazonía son sujetos de derecho titulares de protección, la justicia latinoamericana ofrece una respuesta ética de vanguardia a la encrucijada climática que amenaza a la biosfera terrestre. La creación de cuerpos colegiados de guardianes territoriales, integrados por autoridades estatales y sabios comunitarios, materializa una gobernanza ambiental participativa donde el cuidado de las cuencas es asunto de supervivencia colectiva. Asimismo, la designación paritaria de sabios comunitarios como guardianes colegiados de las cuencas fluviales asegura una supervisión transparente e incorruptible de las tareas de remediación ambiental."
      },
      {
        "type": "narration",
        "text": "Asimismo, el florecimiento de la Educación Intercultural Bilingüe y la entusiasta apropiación de las herramientas digitales por parte de las nuevas generaciones desmienten el fatídico augurio de la extinción lingüística. Hoy el quechua, el aymara, el guaraní, el maya y decenas de lenguas amazónicas se escuchan con orgullo no solo en las escuelas comunitarias, sino en emisoras radiales, plataformas de mensajería instantánea, redes sociales y festivales juveniles de música urbana. Cada generación que recupera su lengua materna reconquista también la dignidad de su mirada sobre el mundo y su soberanía discursiva. Por consiguiente, la proliferación de contenidos digitales en lenguas vernáculas rompe las brechas de exclusión y sitúa a la juventud originaria en el corazón de la sociedad de la información global. Por añadidura, el amparo jurídico a los saberes botánicos ancestrales previene la biopiratería transnacional sobre las plantas medicinales y fármacos tradicionales."
      },
      {
        "type": "narration",
        "text": "El liderazgo luminoso de las mujeres indígenas en la primera línea de la resistencia territorial nos recuerda, en definitiva, que la lucha por los derechos colectivos es inseparable de la defensa de la vida misma. Su entrega generosa, sustentada en el cuidado recíproco de la comunidad y en el respeto sagrado hacia la Madre Tierra, traza el horizonte de un nuevo pacto social más justo, solidario y compasivo. Al honrar la memoria de sus ancestros y proyectar sus saberes hacia el porvenir, los pueblos originarios de Suramérica enseñan al mundo entero que solo cuidando la diversidad viva de la Tierra seremos capaces de asegurar un destino libre y digno para toda la humanidad. Defender los derechos inalienables de los pueblos originarios y la dignidad sagrada de la Naturaleza es el camino ineludible hacia una América unida, pacífica y verdaderamente emancipadora."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuál es la transformación medular que propone la concepción del Estado plurinacional frente al modelo monocultural tradicional?",
            "options": [
              "La sustitución del castellano por un código numérico binario.",
              "El reconocimiento de la diversidad étnica, lingüística y jurídica como un valor fundacional y no como un obstáculo a homogenizar.",
              "La abolición del derecho al voto ciudadano en las grandes urbes.",
              "La centralización de todas las decisiones judiciales en capitales extranjeras."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué valor diferencial aporta la gobernanza biocéntrica a la protección de los ríos y bosques?",
            "options": [
              "La consideración de la naturaleza como un sujeto de derechos custodiado activamente por comunidades y Estado, superando la visión de mercancía explotable.",
              "El cierre definitivo de las vías de navegación fluvial para pequeñas embarcaciones.",
              "La delegación de los recursos naturales en corporaciones privadas sin control público.",
              "La eliminación de los estudios de impacto ambiental en proyectos de infraestructura."
            ],
            "correctIndex": 0
          },
          {
            "question": "¿Cómo se articula el liderazgo de las mujeres indígenas en la defensa comunitaria del territorio?",
            "options": [
              "Vinculando la protección del cuerpo y la dignidad femenina con la defensa sagrada de la Madre Tierra y la soberanía alimentaria.",
              "Promoviendo la tala intensiva de bosques para urbanizaciones privadas.",
              "Abandonando definitivamente las labores de custodia de semillas nativas.",
              "Exigiendo la disolución de los consejos comunales de ancianos."
            ],
            "correctIndex": 0
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
