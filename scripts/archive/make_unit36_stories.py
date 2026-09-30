"""
make_unit36_stories.py
Defines the 8 stories for Unit 36 and tests word counts.
"""
import re
import json

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

STORIES = {
  "classics/b2/b2-36": {
    "id": "b2-36",
    "title": "El Aleph (Jorge Luis Borges, 1949)",
    "level": "B2",
    "lesson": 1,
    "type": "classics",
    "estimatedMinutes": 15,
    "summary": "Estudio literario y metafísico de la obra maestra de Jorge Luis Borges: la muerte de Beatriz Viterbo, la rivalidad irónica con Carlos Argentino Daneri, el descenso al sótano de la calle Garay y la visión mística del Aleph, el punto infinitesimal que contiene simultáneamente todo el universo sin superposición ni confusión.",
    "characters": [
      "Borges (narrador y protagonista, enamorado melancólico de Beatriz)",
      "Beatriz Viterbo (figura femenina inalcanzable, cuya muerte abre el relato)",
      "Carlos Argentino Daneri (primo de Beatriz, poeta pedante y mediocre que custodia el Aleph)"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Publicado en Buenos Aires en 1949 por la editorial Losada, 'El Aleph' constituye la cumbre indiscutible de la narrativa fantástica y ensayística de Jorge Luis Borges y uno de los monumentos estéticos más perdurables de la literatura universal del siglo XX. El relato parte de una elegía íntima: la desgarradora mañana de febrero en que la amada Beatriz Viterbo fallece tras una agonía atroz, provocando en el narrador —llamado también Borges— la obsesión melancólica de preservar intacto cada recuerdo, cada fotografía y cada detalle vinculado a su memoria frente al avance indiferente del tiempo. Para no cortar el lazo con la difunta, el protagonista adopta el hábito devoto de visitar puntualmente cada treinta de abril, día de su cumpleaños, la vieja casona familiar de la calle Garay, donde traba relación con su primo hermano, Carlos Argentino Daneri, un funcionario pedante y mediocre que encarna la caricatura del versificador pretencioso."
      },
      {
        "type": "narration",
        "text": "A lo largo de sucesivas visitas, Daneri somete a Borges a la lectura tediosa y soporífera de fragmentos de un poema monumental titulado 'La Tierra', mediante el cual pretende describir prolijamente cada rincón del planeta, versificando desde las tarifas portuarias de Marsella hasta las tabernas de Australia sin omitir digresiones pedantes ni retoricismos vacíos. Pese al desdén intelectual que le suscita la impericia poética de su anfitrión, el narrador soporta las lecturas para mantener abierto el santuario memorial de Beatriz. La trama se acelera de manera insospechada cuando Daneri llama a Borges al borde del colapso nervioso: los propietarios de la confitería contigua planean demoler la casa señorial para ampliar sus instalaciones comerciales, lo que destruiría irremediablemente el sótano donde se oculta su mayor secreto: el Aleph, el único punto en el espacio que le permite componer su obra."
      },
      {
        "type": "narration",
        "text": "Con una mezcla de escepticismo burlón y curiosidad mórbida, sospechando que Daneri ha caído en la demencia clínica, Borges acude a la casa condenada y desciende solo por la estrecha escalera hacia la oscuridad absoluta del sótano. Siguiendo las instrucciones rituales del pariente, se recuesta sobre el piso de baldosas frías, apoya la cabeza en un costal áspero y fija la mirada en el ángulo superior del rincón. Tras unos instantes de angustiosa inquietud, sobreviene la epifanía estética más deslumbrante jamás concebida en prosa castellana: en un disco infinitesimal de dos o tres centímetros de diámetro, resplandeciente con fulgor casi intolerable, Borges contempla el Aleph, el prodigio supremo donde todos los lugares de la Tierra, vistos desde todos los ángulos posibles, coexisten en un mismo instante sin superponerse ni perder su nitidez."
      },
      {
        "type": "narration",
        "text": "En una célebre enumeración caótica que desafía los límites del lenguaje humano —el cual, por ser sucesivo en el tiempo, resulta trágicamente impotente para transmitir una revelación cósmica simultánea—, Borges ve el mar populoso, el alba y el poniente, las muchedumbres de América, una plateada telaraña en el centro de una pirámide negra, cartas obscenas dirigidas a Beatriz que revelan secretos dolorosos, su propia sangre y el engranaje del amor y de la muerte. Al contemplar la totalidad del cosmos concentrada en un vértice íntimo, el narrador experimenta un pavor sagrado y una infinita conmiseración hacia el género humano, comprendiendo que toda tentativa de abarcar el infinito mediante palabras convencionales está irremediablemente condenada a la alusión imperfecta y a la derrota expresiva."
      },
      {
        "type": "narration",
        "text": "Tras emerger del sótano y fingir con refinada crueldad una educada indiferencia ante el angustiado Daneri para negarle el consuelo de validar su maravilla, Borges abandona la calle Garay sabiendo que el edificio será demolido y que el Aleph quedará sepultado para siempre bajo los escombros de la modernidad urbana. En la posdata melancólica de 1943 que clausura el relato, el autor reflexiona sobre la trágica condición del olvido humano: así como los rasgos de Beatriz se van desvaneciendo inexorablemente en la niebla de su memoria, sospecha que el propio universo es un Aleph ilusorio y que todo lo que vive está destinado a borrarse en el flujo incesante de los días. 'El Aleph' perdura así como una metáfora perfecta del genio borgeano: la certidumbre de que en la minúscula casilla de la palabra habita el misterio infinito de todas las cosas."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué es 'el Aleph' según la revelación que experimenta el narrador en el sótano de la calle Garay?",
            "options": [
              "Un telescopio astronómico importado de Alemania por la universidad.",
              "Un punto infinitesimal del espacio donde se encuentran, simultáneamente y sin confundirse, todos los lugares del universo.",
              "Un manuscrito medieval en pergamino árabe hallado en Córdoba.",
              "Una gema preciosa robada de una catedral europea."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Por qué visita el narrador cada año la casona de Carlos Argentino Daneri?",
            "options": [
              "Para cobrar una deuda monetaria contraída por la familia.",
              "Para rendir devoto homenaje a la memoria de Beatriz Viterbo el día de su cumpleaños.",
              "Para ayudar a redactar las leyes de aduanas del puerto de Buenos Aires.",
              "Para comprar cuadros renacentistas que estaban en venta."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué dilema estilístico y filosófico plantea Borges ante la contemplación del Aleph?",
            "options": [
              "La imposibilidad del lenguaje sucesivo para capturar una experiencia cósmica absoluta y simultánea.",
              "La falta de tinta adecuada para imprimir libros en las editoriales argentinas.",
              "La prohibición religiosa de mirar objetos circulares en la oscuridad.",
              "El desacuerdo sobre el precio del alquiler del sótano."
            ],
            "correctIndex": 0
          }
        ]
      }
    }
  },
  "world/b2/b2-futuro-01": {
    "id": "b2-futuro-01",
    "title": "El nuevo cine y las narrativas audiovisuales de América Latina",
    "level": "B2",
    "lesson": 1,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "La madurez estética y la proyección global del cine latinoamericano contemporáneo: de Alfonso Cuarón y Guillermo del Toro a Lucrecia Martel y Ciro Guerra; autoría, memoria histórica y descolonización de la mirada audiovisual.",
    "characters": [
      "Cineastas, directores de fotografía y documentalistas de la región",
      "Críticos cinematográficos y curadores de festivales internacionales"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "A lo largo de las primeras décadas del siglo XXI, el cine latinoamericano ha experimentado una de las revoluciones estéticas y narrativas más fecundas de su historia, transitando con aplomo desde la precariedad de las producciones independientes locales hacia la conquista indiscutible de los máximos certámenes cinematográficos globales como Cannes, Venecia, Berlín y los premios de la Academia. Esta eclosión creativa no es fruto del azar comercial, sino de la confluencia virtuosa entre nuevas legislaciones de fomento audiovisual en países como México, Argentina, Colombia, Chile y Brasil, y la irrupción de una generación deslumbrante de cineastas formados con rigor que han sabido fundir la memoria histórica, la experimentación formal y la urgencia social en obras de asombrosa madurez visual. Aunado a ello, la proliferación de escuelas universitarias de cine y talleres comunitarios en barrios populares ha permitido democratizar el acceso a las técnicas de guion, montaje sonoro y postproducción digital, generando una polifonía visual sin precedentes."
      },
      {
        "type": "narration",
        "text": "En México, la célebre tríada conformada por Alfonso Cuarón, Guillermo del Toro y Alejandro González Iñárritu demostró la capacidad de los autores hispanoamericanos para dialogar de igual a igual con los grandes presupuestos globales sin resignar sus raíces identitarias. Obras cumbre como 'Roma' de Cuarón constituyen un monumento cinematográfico al recuerdo autobiográfico, la memoria urbana de la capital y la reivindicación amorosa de la mujer indígena trabajadora del hogar, capturada en un blanco y negro soberbio que transforma la nostalgia íntima en una meditación universal sobre la desigualdad de clases. Asimismo, Del Toro ha reinventado la fábula gótica y fantástica como una trinchera ética en defensa de la otredad y los marginados. En efecto, el reconocimiento internacional conquistado por estos directores abrió las puertas de los circuitos de distribución mundial a coproducciones independientes que antes quedaban confinadas al ámbito local."
      },
      {
        "type": "narration",
        "text": "En el Cono Sur, la cineasta argentina Lucrecia Martel ha fundado una poética visual y sonora irrepetible que dinamita las convenciones del drama realista burgués. Con películas hipnóticas como 'La ciénaga', 'La niña santa' y su monumental adaptación de 'Zama', Martel explora la decadencia moral de las élites provincianas y las heridas abiertas del orden colonial a través de encuadres oblicuos, elipsis narrativas inquietantes y una atmósfera sonora densa que sumerge al espectador en un estado de duermevela lúcida. Su cine desconfía de las moralejas fáciles y reivindica la experiencia sensorial pura como vía privilegiada para interrogar la ambigüedad del deseo y la culpa histórica. Asimismo, el cine del Cono Sur desafía los relatos complacientes sobre el progreso económico, visibilizando las grietas íntimas de sociedades que aún procesan las heridas de las dictaduras y las crisis financieras."
      },
      {
        "type": "narration",
        "text": "En la región andina y amazónica, el colombiano Ciro Guerra deslumbró al mundo con 'El abrazo de la serpiente' y 'Pájaros de verano', filmadas en lenguas originarias con comunidades locales de la selva y la península de La Guajira. Al invertir la mirada etnográfica eurocéntrica de los exploradores occidentales, Guerra convierte al chamán Karamakate en el eje moral y filosófico del relato, denunciando el ecocidio desatado por la fiebre del caucho y revelando que la sabiduría indígena custodia una comprensión cosmológica infinitamente superior a la arrogancia tecnocrática moderna. Esta descolonización de la pantalla ha abierto una senda luminosa para documentalistas de toda la región. Por consiguiente, filmar en lenguas ancestrales y en parajes selváticos no constituye un mero adorno pintoresco, sino un acto de reparación histórica que devuelve a los pueblos originarios la potestad sobre su propia imagen."
      },
      {
        "type": "narration",
        "text": "En la actualidad, las plataformas digitales y la democratización tecnológica de las cámaras digitales permiten que realizadoras indígenas, colectivos afrodescendientes y jóvenes de las periferias urbanas relaten sus propias vivencias sin intermediarios paternalistas. El cine latinoamericano del siglo XXI no persigue mimetizar las fórmulas estandarizadas de Hollywood, sino erigir un espejo polifónico donde el dolor, la esperanza y la belleza de nuestras tierras se proyecten al mundo con voz propia. Cada fotograma concebido desde el sur reafirma la certidumbre de que contar nuestras historias con autenticidad es un acto irrenunciable de soberanía cultural y memoria democrática."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué innovación temática y formal destaca en la película 'Roma' de Alfonso Cuarón?",
            "options": [
              "Un filme de ciencia ficción sobre invasiones espaciales en el norte de México.",
              "Un retrato autobiográfico en blanco y negro que visibiliza la dignidad de una trabajadora indígena del hogar en la capital de los años setenta.",
              "Un documental técnico sobre la industria automotriz en Monterrey.",
              "Una comedia ligera sobre las playas turísticas de Cancún."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cómo transforma el cineasta colombiano Ciro Guerra la narrativa de exploración en 'El abrazo de la serpiente'?",
            "options": [
              "Celebrando el triunfo comercial de las empresas caucheras extranjeras.",
              "Descolonizando la mirada audiovisual al colocar la cosmovisión chamánica indígena como eje moral y filosófico del relato amazónico.",
              "Filmando enteramente en idioma inglés en estudios cerrados de California.",
              "Sustituyendo a los actores locales por marionetas digitales."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué rasgo singular define la poética cinematográfica de la directora argentina Lucrecia Martel?",
            "options": [
              "El uso exclusivo de planos generales sin sonido ambiente.",
              "El uso virtuoso de encuadres oblicuos, elipsis narrativas y paisajes sonoros envolventes para explorar la decadencia señorial y las tensiones coloniales.",
              "La imitación estricta de las comedias románticas de Broadway.",
              "La eliminación total de los actores profesionales en todos sus filmes."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-futuro-02": {
    "id": "b2-futuro-02",
    "title": "Literatura posboom, autoficción y nuevas voces urbanas",
    "level": "B2",
    "lesson": 2,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "La ebullición de la narrativa latinoamericana contemporánea tras el legado del Boom: la primacía de las escritoras, el nuevo gótico andino y pampeano, la ciencia ficción distópica y la autoficción intimista frente a las violencias cotidianas.",
    "characters": [
      "Escritoras y narradores contemporáneos de América Latina",
      "Críticos literarios y editores independientes"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Tras el deslumbramiento planetario del Boom latinoamericano de los años sesenta —dominado casi exclusivamente por figuras masculinas monumentales como García Márquez, Vargas Llosa, Fuentes y Cortázar—, la narrativa de nuestra región en el siglo XXI vive una segunda edad de oro caracterizada por una profunda transformación estética, temática y demográfica. Lejos de las sagas patriarcales de dictadores míticos y pueblos rurales mágicos, la literatura posboom ha trasladado el foco hacia la intimidad fracturada de las megalópolis contemporáneas, las secuelas psicológicas de las dictaduras y la violencia cotidiana, erigiendo a una pléyade extraordinaria de escritoras en la vanguardia literaria indiscutible del continente. Aunado a ello, la superación de las etiquetas paternalistas del realismo mágico ha permitido a las nuevas generaciones explorar libremente el ensayo híbrido, la distopía climática y la narrativa policial no binaria."
      },
      {
        "type": "narration",
        "text": "Autoras como la argentina Mariana Enríquez han revolucionado el género fantástico y el terror gótico, arraigándolo en las pesadillas reales de la sociedad del Cono Sur: los centros clandestinos de detención, la pobreza marginal de las barriadas y la violencia machista. En obras maestras como 'Nuestra parte de noche' o 'Las cosas que perdimos en el fuego', Enríquez demuestra que los monstruos más aterradores no provienen de castillos medievales europeos, sino de las sombras impunes de la historia nacional y la indiferencia social. Del mismo modo, la ecuatoriana Mónica Ojeda ha forjado con 'Mandíbula' y 'Nefando' un 'gótico andino' visceral y poético que indaga en el miedo, los secretos adolescentes y la perturbadora dimensión del ciberespacio. En efecto, el terror sociopolítico practicado por las narradoras actuales desentraña los miedos soterrados de una clase media acechada por la precariedad económica, la crisis de los cuidados y la degradación institucional."
      },
      {
        "type": "narration",
        "text": "Paralelamente, la escritora argentina Samanta Schweblin ha deslumbrado a la crítica internacional con novelas de tensión psicológica asfixiante como 'Distancia de rescate' y 'Kentukis'. A través de una prosa milimétrica desprovista de artificios superfluos, Schweblin examina la vulnerabilidad biológica ante la catástrofe ambiental provocada por los agrotóxicos en el campo pampeano, así como la perturbadora alienación tecnológica de una humanidad hiperconectada que trafica voluntariamente con su propia intimidad. Su narrativa prescinde de explicaciones científicas para sumergir al lector en una atmósfera enrarecida donde lo siniestro acecha en la cotidianidad más familiar. Asimismo, la indagación en los desastres ecológicos provocados por el agronegocio revela la interdependencia trágica entre el cuerpo humano y el entorno natural devastado por la codicia corporativa. Cada relato de Samanta Schweblin opera como una punzada de advertencia moral ante la fragilidad de nuestros lazos afectivos."
      },
      {
        "type": "narration",
        "text": "En el terreno de la autoficción y la memoria íntima, autores como el chileno Alejandro Zambra ('Formas de volver a casa', 'Poeta chileno') exploran la experiencia de crecer a la sombra de la dictadura militar, interrogando el rol de los 'personajes secundarios' de la historia que asistieron mudos a la tragedia política. Con una ironía tierna y una concisión poética admirable, Zambra despoja a la literatura de solemnidad grandilocuente para celebrar los libros, la paternidad afectuosa y las vacilaciones de la vida cotidiana. Su escritura dialoga fluidamente con las crónicas urbanas de la mexicana Valeria Luiselli o la boliviana Giovanna Rivero. Por consiguiente, la memoria íntima y los recuerdos familiares de la infancia en dictadura se transforman en documentos poéticos invaluables para conjurar el olvido y la impunidad histórica."
      },
      {
        "type": "narration",
        "text": "Esta primavera literaria se sustenta en un vibrante ecosistema de editoriales independientes dispersas por todo el continente, que han roto los monopolios corporativos internacionales para descubrir y difundir voces periféricas, experimentales y disidentes. La literatura latinoamericana del siglo XXI ya no necesita pedir permiso ni acomodarse a etiquetas exóticas impuestas desde el extranjero; con audacia formal insobornable, honestidad brutal y empatía luminosa, sus creadores exploran los abismos del presente y demuestran que la palabra escrita sigue siendo el espejo más certero de nuestra condición humana. La vitalidad del panorama editorial independiente garantiza que la experimentación formal y la diversidad de voces sigan floreciendo al margen de las modas comerciales efímeras."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuál es uno de los rasgos distintivos más destacados de la narrativa latinoamericana contemporánea del siglo XXI frente al Boom clásico?",
            "options": [
              "El abandono total de la lectura y la clausura de las editoriales.",
              "El liderazgo protagónico de una generación excepcional de escritoras que exploran el terror cotidiano, la intimidad urbana y la violencia sociopolítica.",
              "La obligación de escribir exclusivamente obras en verso rimado tradicional.",
              "La prohibición de traducir libros latinoamericanos a otros idiomas."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cómo utiliza Mariana Enríquez el género de terror en novelas como 'Nuestra parte de noche'?",
            "options": [
              "Para relatar fábulas de príncipes medievales nórdicos desvinculados de la realidad.",
              "Para canalizar los horrores reales de la historia argentina: la represión dictatorial, la marginación y la violencia sistémica.",
              "Para promocionar parques de atracciones infantiles.",
              "Para defender la privatización de las bibliotecas populares."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué temática examina Samanta Schweblin con maestría en su aclamada novela 'Distancia de rescate'?",
            "options": [
              "La intoxicación ambiental silenciosa por agrotóxicos en el campo y la angustia maternal ante la fragilidad de la vida.",
              "La construcción de rascacielos financieros en el centro de Londres.",
              "Un manual técnico de pilotaje de helicópteros comerciales.",
              "La historia de los tratados arancelarios del siglo XIX."
            ],
            "correctIndex": 0
          }
        ]
      }
    }
  },
  "world/b2/b2-futuro-03": {
    "id": "b2-futuro-03",
    "title": "Transición ecológica, litio y soberanía en el tablero multipolar",
    "level": "B2",
    "lesson": 3,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "La encrucijada geopolítica de los recursos estratégicos en América Latina: el triángulo del litio (Bolivia, Argentina, Chile), el cobre, las tierras raras y la urgencia de superar el extractivismo mediante la industrialización soberana y el valor agregado regional.",
    "characters": [
      "Ministros de minería y energía, científicos en almacenamiento electroquímico",
      "Comunidades originarias de los salares andinos y diplomáticos"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "La transición energética global hacia la descarbonización y el abandono de los combustibles fósiles ha colocado a América Latina en el epicentro de la geopolítica mundial del siglo XXI. El 'oro blanco' de la era digital —el litio indispensable para las baterías de iones de litio de los vehículos eléctricos y el almacenamiento de energías renovables intermitentes— se concentra en un sesenta por ciento en los inmensos salares de altura del altiplano andino, en el denominado 'triángulo del litio' que comparten Bolivia (Salar de Uyuni), Argentina (Salar del Hombre Muerto y Olaroz) y Chile (Salar de Atacama). A esta riqueza se suma el liderazgo mundial de Chile y Perú en la producción de cobre, el mineral conductor insustituible para electrificar la economía planetaria. Aunado a ello, la demanda exponencial de minerales estratégicos coincide con un momento de profunda reconfiguración del orden internacional, donde las potencias globales compiten ferozmente por asegurar sus cadenas de suministro."
      },
      {
        "type": "narration",
        "text": "Sin embargo, esta bendición geológica reactiva el fantasma secular de la 'maldición de los recursos naturales' y el riesgo inminente de una nueva subordinación neocolonial. A lo largo de cinco siglos, desde la plata colonial del Cerro Rico de Potosí hasta el caucho amazónico y el petróleo del siglo XX, América Latina operó como mera exportadora de materias primas brutas hacia las metrópolis industriales, reteniendo en sus territorios la devastación ambiental y la desigualdad social mientras el valor añadido y el desarrollo tecnológico se acumulaban en el norte global. El desafío civilizatorio ineludible consiste hoy en romper este patrón extractivista mediante la soberanía industrial. En efecto, la historia económica de la región advierte con crudeza sobre las consecuencias desastrosas de depender de los ciclos de precios de las materias primas sin diversificar el tejido productivo ni invertir en ciencia y tecnología."
      },
      {
        "type": "narration",
        "text": "Frente a las presiones competitivas de superpotencias como China y Estados Unidos, cada nación del altiplano ha ensayado modelos de gobernanza diferenciados. Mientras Chile promovió una estrategia nacional público-privada con control estatal mayoritario y exigencia de tecnologías de extracción directa menos lesivas para las cuencas hídricas, Bolivia optó por la nacionalización estratégica a través de la empresa estatal Yacimientos de Litio Bolivianos (YLB), buscando fabricar cátodos y baterías en territorio nacional, y Argentina descentralizó las concesiones en sus provincias cordilleranas atrayendo inversiones directas globales en una carrera acelerada de producción. Asimismo, la coordinación diplomática entre las naciones del altiplano resulta indispensable para negociar transferencias efectivas de tecnología, formación de científicos locales y participación estatal en la renta minera."
      },
      {
        "type": "narration",
        "text": "En el plano socioambiental, la extracción masiva de litio plantea graves encrucijadas ecológicas en ecosistemas desérticos extremadamente frágiles, donde cada tonelada de mineral extraída mediante piscinas de evaporación solar tradicional consume cientos de miles de litros de agua dulce subterránea. Las comunidades originarias que habitan los bordes de los salares desde tiempos inmemoriales denuncian la desertificación de sus bofedales, la merma de las poblaciones de flamencos andinos y la pérdida de agua para el pastoreo de llamas. De ahí la urgencia ética de implementar tecnologías de extracción directa limpia y respetar de forma irrestricta la consulta libre, previa e informada. Por añadidura, la sustitución progresiva de las piscinas de evaporación por métodos de extracción directa con reinyección de salmuera es una exigencia ética inaplazable para salvaguardar el agua de los pueblos."
      },
      {
        "type": "narration",
        "text": "Para evitar que la región sea fragmentada y manipulada por intereses foráneos, analistas y líderes políticos postulan la creación de una 'OPEP del litio' o una alianza tecnológica sudamericana que fije estándares ambientales comunes, armonice regalías fiscales y promueva cadenas de valor regionales integradas. América Latina posee el sol del desierto de Atacama, los vientos huracanados de la Patagonia, la energía hidroeléctrica del Paraná y los minerales estratégicos del porvenir. Si logra articular esta riqueza con visión soberana, educación científica de vanguardia y justicia distributiva, la transición ecológica no será un nuevo saqueo, sino el motor de su definitiva emancipación. El porvenir de la transición energética en América Latina dependerá de su capacidad para demostrar que la protección de la naturaleza y la soberanía industrial pueden caminar de la mano."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué países conforman el denominado 'triángulo del litio' en América del Sur?",
            "options": [
              "Colombia, Venezuela y Ecuador.",
              "Bolivia, Argentina y Chile.",
              "Uruguay, Paraguay y Brasil.",
              "Guyana, Surinam y Belice."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cuál es el riesgo histórico que busca evitar América Latina en la explotación de minerales estratégicos para la transición verde?",
            "options": [
              "El agotamiento del combustible para cohetes espaciales.",
              "La repetición del patrón extractivista colonial de exportar materia prima bruta sin generar valor agregado, tecnología ni bienestar local.",
              "El exceso de ingenieros químicos en las universidades públicas.",
              "La sustitución del cobre por plástico sintético en las redes eléctricas."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cuál es el mayor impacto ambiental asociado a la técnica tradicional de evaporación en los salares de altura?",
            "options": [
              "La emisión masiva de humo negro a la atmósfera.",
              "El consumo intensivo de agua subterránea que amenaza la subsistencia de bofedales y fauna andina en ecosistemas frágiles.",
              "El enfriamiento de las aguas marinas en el océano Pacífico.",
              "La proliferación de plantas invasoras en la tundra antártica."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-futuro-04": {
    "id": "b2-futuro-04",
    "title": "Cultura juvenil, redes y nuevos movimientos sociales ciudadanos",
    "level": "B2",
    "lesson": 4,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "El protagonismo de las juventudes latinoamericanas en la transformación de la esfera pública: la marea verde feminista, el estallido social, la música urbana contestataria y el activismo digital como herramientas de democratización radical.",
    "characters": [
      "Líderes estudiantiles y colectivos juveniles urbanos",
      "Músicos de la escena urbana independiente y activistas digitales"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "En un continente donde más de la mitad de la población tiene menos de treinta años, las juventudes latinoamericanas han irrumpido con una fuerza transformadora sin precedentes, redefiniendo las formas de participación política, la estética de la protesta y los consensos éticos de la sociedad contemporánea. Desencantados de las estructuras partidarias tradicionales y los pactos cupulares de las élites, los movimientos juveniles han ocupado las calles y las redes sociales con una vitalidad horizontal, festiva y radicalmente democrática, demostrando que la apatía no es un rasgo generacional, sino la respuesta lúcida ante un sistema institucional anquilosado que postergaba sus anhelos de futuro. Aunado a ello, la juventud actual ha forjado redes transnacionales de colaboración instantánea que trascienden las fronteras nacionales, compartiendo estrategias de autoprotección, consignas de movilización y herramientas de comunicación comunitaria."
      },
      {
        "type": "narration",
        "text": "Uno de los fenómenos más luminosos y de mayor irradiación global de esta primavera ciudadana ha sido la 'marea verde' feminista, nacida en Argentina al calor de la consigna 'Ni Una Menos' y expandida con velocidad fulgurante a Chile, México, Colombia y toda la región. Con pañuelos verdes anudados al cuello, cánticos corales y movilizaciones masivas que desbordaron las avenidas, millones de jóvenes lograron despenalizar la interrupción voluntaria del embarazo y consagrar la educación sexual integral, interpelando las raíces patriarcales de la sociedad y situando el cuidado, la autonomía corporal y la erradicación del feminicidio en el centro insoslayable del debate de Estado. En efecto, la fuerza desbordante de la marea verde demostró que las demandas de género no son reclamos sectoriales aislados, sino la piedra angular de una transformación democrática integral de la sociedad."
      },
      {
        "type": "narration",
        "text": "Asimismo, las movilizaciones estudiantiles y los estallidos sociales en Chile (2019) y Colombia (2021) pusieron de manifiesto el hartazgo colectivo frente a la desigualdad estructural, el encarecimiento de la educación superior y la precarización laboral juvenil. En Santiago y Bogotá, las marchas combinaron expresiones artísticas de asombrosa potencia poética —como la performance global 'Un violador en tu camino' del colectivo Las Tesis o las batucadas de resistencia en la 'Primera Línea'— con una firmeza cívica que obligó a iniciar procesos constituyentes y reformas sociales de calado histórico, demostrando que el arte urbano y la protesta pacífica son armas insustituibles de emancipación. Asimismo, la confluencia entre arte urbano, música experimental y demandas de justicia social ha revitalizado el espacio público metropolitano, transformando las plazas en laboratorios de ciudadanía activa y deliberación fraterna."
      },
      {
        "type": "narration",
        "text": "En el plano cultural, la música urbana contemporánea —desde el rap contestatario y el trap con identidad barrial hasta el neoperreo y la música de fusión afroindígena— se ha convertido en la banda sonora cotidiana de esta juventud rebelde. Artistas independientes rechazan la complacencia frívola para rimar sobre la violencia policial, la precariedad de las periferias metropolitanas, el orgullo de las raíces morenas y la salud mental. Lejos de ser un producto efímero de consumo masivo, esta expresión musical canaliza el pulso emocional de barrios donde la creatividad y el compañerismo triunfan cotidianamente sobre la exclusión. Por consiguiente, la apropiación creativa de las tecnologías digitales por parte de brigadas juveniles ha neutralizado las campañas de desinformación mediática, devolviendo a los ciudadanos el control sobre el relato público."
      },
      {
        "type": "narration",
        "text": "El activismo digital y el uso sagaz de las redes sociales han democratizado el acceso a la información, permitiendo a colectivos de derechos humanos y brigadas ambientales registrar abusos policiales en tiempo real y coordinar acciones de solidaridad comunitaria instantáneas. Las juventudes de nuestra América no esperan pasivamente que el futuro llegue de manos ajenas; lo están construyendo activamente con cada asamblea, cada mural callejero, cada verso rapeado y cada clic solidario. Su energía creadora es el latido más esperanzador de un continente que se niega a resignarse y avanza con valentía hacia un mañana de justicia y dignidad compartida. La rebeldía pacífica y la sensibilidad solidaria de las nuevas generaciones son la garantía más firme de que América Latina continuará marchando hacia un porvenir de libertad y equidad."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Qué representa la 'marea verde' nacida en el Cono Sur y expandida a toda América Latina?",
            "options": [
              "Un movimiento ecologista enfocado exclusivamente en la reforestación de pinos extranjeros.",
              "Una movilización feminista juvenil masiva por los derechos reproductivos, la autonomía corporal y el fin de la violencia machista.",
              "Una huelga de trabajadores de la industria del té verde.",
              "Un campeonato juvenil de vela deportiva."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué impacto decisivo tuvieron los estallidos sociales juveniles en Chile y Colombia?",
            "options": [
              "La clausura inmediata de todas las facultades universitarias.",
              "Visibilizar el malestar ante la desigualdad estructural y forzar debates constitucionales y reformas institucionales profundas.",
              "El traspaso de los fondos de pensiones a bancos privados extranjeros.",
              "La prohibición de las artes visuales en el espacio público."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Cómo se vincula la nueva música urbana independiente con las realidades de la juventud latinoamericana?",
            "options": [
              "Promoviendo el aislamiento individualista y el lujo desmedido sin conciencia social.",
              "Canalizando con honestidad el orgullo identitario barrial, la denuncia de la violencia y la resiliencia colectiva frente a la marginación.",
              "Traduciendo canciones comerciales anglosajonas de los años cincuenta.",
              "Eliminando los instrumentos acústicos y la percusión tradicional."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-futuro-05": {
    "id": "b2-futuro-05",
    "title": "¿Qué significa ser latinoamericano en el siglo XXI? Identidad y horizonte",
    "level": "B2",
    "lesson": 5,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Meditación filosófica y cultural sobre la identidad latinoamericana en la era global: mestizaje, pluriculturalidad, hospitalidad solidaria y la construcción de un destino común en un mundo multipolar e interconectado.",
    "characters": [
      "Pensadores, sociólogos y ciudadanos de la América Latina diversa"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Al culminar este periplo monumental a lo largo de las geografías, historias, letras y pueblos de nuestra América, la pregunta sobre la identidad continental adquiere una resonancia existencial y política ineludible: ¿qué significa ser latinoamericano en el umbral del siglo XXI? Lejos de las viejas definiciones esencialistas que buscaban encorsetar nuestra condición en una raza mítica, una religión uniforme o una pureza cultural inexistente, el ser latinoamericano se revela hoy como un proyecto abierto, híbrido, polifónico y en perpetua recreación, cuya mayor fortaleza estriba precisamente en su asombrosa capacidad para abrazar la diversidad viva sin fragmentarse. Aunado a ello, la experiencia latinoamericana desmiente categóricamente que la modernidad exija renunciar a las tradiciones milenarias o uniformizar las vivencias comunitarias bajo patrones consumistas foráneos."
      },
      {
        "type": "narration",
        "text": "Somos la tierra donde confluyen las raíces milenarias de civilizaciones indígenas que domesticaron el maíz y la papa en comunión sagrada con los astros; el dolor y la luminosa resistencia creadora de millones de afrodescendientes que trajeron el candombe, la cumbia, la santería y el sentido comunitario de la libertad; la herencia de la lengua de Cervantes modulada con la cadencia de cientos de lenguas originarias; y el aliento generoso de oleadas inmigratorias que hallaron en nuestras costas refugio frente a las guerras del Viejo Mundo. Esta aleación irrepetible convierte a nuestra región en el laboratorio del mestizaje cultural más fértil del planeta. En efecto, la capacidad de nuestros pueblos para fundir saberes ancestrales con innovaciones contemporáneas constituye una fortaleza civilizatoria inestimable en un mundo aquejado por la incertidumbre y el desencanto. La sabiduría del Buen Vivir ofrece un horizonte ético deslumbrante frente a la crisis ecológica planetaria, recordando que la fraternidad humana es la mayor conquista espiritual."
      },
      {
        "type": "narration",
        "text": "Pero la identidad no es solo memoria del pasado; es sobre todo una ética del presente y un compromiso fraternal hacia el porvenir. En un mundo desgarrado por el resurgimiento de nacionalismos xenófobos, muros fronterizos y guerras geopolíticas fratricidas, América Latina ofrece una reserva moral de convivencia solidaria: la tradición inquebrantable del asilo político, la capacidad comunitaria de acoger al hermano migrante compartiendo el pan en las barriadas populares y la convicción de que los conflictos deben resolverse mediante el diálogo diplomático y el respeto irrestricto al derecho internacional. Asimismo, la vocación pacífica y diplomática de la región, libre de armas nucleares y comprometida con el multilateralismo solidario, es un faro de sensatez en medio de las tormentas geopolíticas globales."
      },
      {
        "type": "narration",
        "text": "Asimismo, el siglo XXI demanda consolidar la vieja utopía de la Patria Grande soñada por Bolívar, San Martín, Martí y Morazán, despojándola de retóricas vacías para traducirla en integración material concreta: redes universitarias compartidas, libre movilidad ciudadana, armonización ambiental de las cuencas transfronterizas y una sola voz coordinada en los foros globales frente al cambio climático y las turbulencias financieras. El destino de cada una de nuestras patrias chicas está indisolublemente atado a la suerte del continente entero; ninguna nación por sí sola podrá enfrentar los desafíos de la inteligencia artificial o el orden multipolar sin la fuerza colectiva de sus hermanas. Por consiguiente, la integración continental no es un anhelo nostálgico, sino la condición indispensable de soberanía para que nuestra América haga oír su voz en el concierto de las naciones."
      },
      {
        "type": "narration",
        "text": "Ser latinoamericano hoy significa reconocerse heredero de una épica de resistencia y esperanza inextinguible. Es hablar una lengua que se canta, se baila y se debate con pasión volcánica; es saber que la ternura y la dignidad no son debilidades, sino la fuerza que mantiene en pie a nuestros pueblos ante la adversidad. Con la mirada limpia puesta en el horizonte, América Latina se yergue no como la periferia pasiva del mundo, sino como el corazón palpitante de una nueva humanidad posible: más justa, más libre, más compasiva y profundamente reconciliada con la belleza de la Tierra. Reconocerse latinoamericano es asumir con orgullo la herencia de un continente que ha hecho de la resiliencia comunitaria y la belleza poética su más alta bandera de dignidad humana."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cómo se define la identidad latinoamericana en el siglo XXI frente a las viejas visiones esencialistas?",
            "options": [
              "Como un dogma cerrado impuesto por decretos militares.",
              "Como una experiencia abierta, híbrida y polifónica que sintetiza raíces indígenas, afrodescendientes, hispánicas y cosmopolitas en perpetua recreación.",
              "Como la negación total de todas las tradiciones previas a la era digital.",
              "Como la copia fiel de las instituciones parlamentarias europeas."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué aporte ético universal ofrece América Latina frente a las crisis de xenofobia global?",
            "options": [
              "La construcción de barreras arancelarias prohibitivas.",
              "Una tradición histórica de asilo, hospitalidad solidaria, acogida al migrante y resolución diplomática pacífica de controversias.",
              "La renuncia voluntaria al derecho internacional humanitario.",
              "La militarización permanente de las fronteras interiores."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué dimensión práctica exige la consolidación contemporánea de la 'Patria Grande'?",
            "options": [
              "La disolución de los idiomas nacionales en favor de una lengua artificial.",
              "La integración real en educación superior, libre movilidad ciudadana, protección ambiental compartida y voz unificada en el tablero mundial.",
              "La sustitución de los parlamentos por algoritmos financieros internacionales.",
              "El aislamiento económico del resto de los continentes."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-futuro-consolidation": {
    "id": "b2-futuro-consolidation",
    "title": "Consolidación: Síntesis final de los Estudios Regionales Latinoamericanos",
    "level": "B2",
    "lesson": 6,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Consolidación final de la trayectoria de 36 unidades de Estudios Regionales de América Latina: balance panorámico de la diversidad continental, conquistas democráticas, madurez artística y horizonte de integración soberana en el siglo XXI.",
    "characters": [
      "Estudiantes, investigadores y ciudadanos de la América Latina integrada"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "Alcanzar la culminación de este curso superior de Estudios Regionales de América Latina a nivel B2 representa un logro intelectual, cultural y lingüístico de primer orden. A lo largo de setenta y dos unidades duales, el estudiante ha recorrido minuciosamente cada rincón de la geografía continental: desde el Valle de Anáhuac en México y los volcanes de Centroamérica hasta el Caribe musical, los páramos andinos, los ríos amazónicos, las pampas ganaderas y los glaciares patagónicos de Tierra del Fuego. Esta inmersión exhaustiva ha demostrado que la región no constituye una masa homogénea de estereotipos folclóricos, sino un mosaico deslumbrante de historias complejas, geografías portentosas y creaciones humanas universales. Aunado a ello, este itinerario formativo ha dotado al estudiante de una competencia sociolingüística y cultural de nivel superior, capaz de apreciar la sutileza del voseo rioplatense, la riqueza léxica andina y la musicalidad caribeña sin barreras comunicativas. Esta soltura pragmática permite transitar con naturalidad entre la conversación cotidiana y el debate ensayístico formal."
      },
      {
        "type": "narration",
        "text": "En el ámbito sociopolítico, el balance de las últimas décadas revela un continente resiliente que ha sabido sobreponerse a dictaduras sangrientas, crisis financieras devastadoras y secuelas coloniales para refundar sus democracias sobre bases plurinacionales, participativas e inclusivas. Las conquistas del pluralismo jurídico, los derechos inalienables de los pueblos originarios, el reconocimiento biocéntrico de la Naturaleza como sujeto de derecho y la vitalidad de las luchas feministas y estudiantiles sitúan a nuestra América a la vanguardia de la imaginación institucional planetaria, ofreciendo modelos de convivencia comunitaria que inspiran a juristas y activistas de todo el orbe. En efecto, el examen riguroso de las constituciones plurinacionales y los tratados ambientales demuestra que la región es un laboratorio de vanguardia en la creación de derechos para la comunidad humana y la naturaleza. Cada pueblo aporta una perspectiva insustituible sobre la justicia social y el bien común."
      },
      {
        "type": "narration",
        "text": "En la dimensión cultural y artística, la trayectoria recorrida evidencia una madurez estética insuperable. Desde las páginas fundacionales del Boom y el pensamiento ensayístico clásico hasta la brillantez audaz de las nuevas escritoras del posboom, el cine descolonizador premiado en los festivales más exigentes y la música urbana que resuena en las esquinas de todo el globo, la voz latinoamericana dialoga con el mundo sin complejos de inferioridad. Nuestra narrativa domina el lenguaje universal sin renunciar a sus cadencias vernáculas, transformando el dolor histórico en belleza redentora y sabiduría poética. Asimismo, la fecundidad de la literatura posboom y el cine descolonizador ratifica que la cultura latinoamericana posee una madurez estética universal capaz de interpelar a lectores y espectadores de todos los continentes. La imaginación artística es un baluarte insustituible de la memoria histórica."
      },
      {
        "type": "narration",
        "text": "Frente a las encrucijadas críticas del presente —la transición ecológica, la custodia de la Amazonía como pulmón hídrico continental, la gobernanza soberana del litio y el cobre, y la gestión humanitaria de los flujos migratorios—, la respuesta ineludible radica en acelerar la integración regional. Ningún país aislado podrá salvaguardar su destino en el escenario multipolar del siglo XXI; solo la articulación mancomunada de nuestras capacidades científicas, industriales y diplomáticas permitirá a la América del Sur, Centroamérica y el Caribe negociar con dignidad frente a las grandes potencias mundiales. Por consiguiente, el dominio de los registros académicos, ensayísticos y diplomáticos permite al hablante articular ideas complejas con precisión, elegancia y sensibilidad intercultural."
      },
      {
        "type": "narration",
        "text": "Al dominar el español en este nivel superior B2 con todas sus modulaciones pragmáticas, registros ensayísticos y matices dialectales, el estudiante no solo ha adquirido una formidable herramienta de comunicación internacional, sino que se ha convertido en un puente vivo de entendimiento intercultural. Felicidades por culminar con rigor y pasión este itinerario transformador: que la voz de América Latina, con su inquebrantable sed de justicia, su fraternidad solidaria y su belleza inextinguible, continúe iluminando su camino personal, profesional y humano. Que este conocimiento adquirido sea el cimiento sólido para seguir descubriendo, debatiendo y celebrando la grandeza inagotable de nuestra América en todos los ámbitos de la vida contemporánea."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuál es la conclusión principal sobre la naturaleza cultural de América Latina tras el recorrido de 36 unidades regionales?",
            "options": [
              "Que es una región monocultural uniforme sin variaciones geográficas ni históricas.",
              "Que constituye un mosaico deslumbrante de gran diversidad histórica, geográfica y lingüística, dotado de una vibrante voz propia en el mundo contemporáneo.",
              "Que carece de producciones artísticas y literarias de alcance universal.",
              "Que todos sus problemas deben resolverse mediante intervenciones militares extranjeras."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Por qué es decisiva la integración regional ante los retos del siglo XXI?",
            "options": [
              "Porque permite negociar con soberanía colectiva ante las potencias globales y coordinar la protección ecológica y tecnológica del continente.",
              "Porque obliga a cerrar los puertos al comercio internacional.",
              "Porque prohíbe la libre circulación de ideas y personas.",
              "Porque encarece los trámites universitarios interregionales."
            ],
            "correctIndex": 0
          },
          {
            "question": "¿Qué representa para el estudiante alcanzar la competencia B2 superior en español con enfoque panhispánico?",
            "options": [
              "Haber memorizado listas de palabras sin comprender su contexto cultural.",
              "Haber conquistado una voz propia con rigor argumentativo, sensibilidad intercultural y dominio de los registros formales y regionales.",
              "Poder redactar exclusivamente documentos mercantiles simples.",
              "La obligación de olvidar la lengua materna."
            ],
            "correctIndex": 1
          }
        ]
      }
    }
  },
  "world/b2/b2-futuro": {
    "id": "b2-futuro",
    "title": "América Latina contemporánea: Identidad, soberanía y porvenir global",
    "level": "B2",
    "lesson": 1,
    "type": "world",
    "estimatedMinutes": 15,
    "summary": "Visión panorámica de cierre sobre la contemporaneidad latinoamericana: el cine de autor, la narrativa posboom, los minerales estratégicos de la transición energética, la vitalidad juvenil y el horizonte de la Patria Grande en el siglo XXI.",
    "characters": [
      "Pueblos, intelectuales y juventudes de la América Latina global"
    ],
    "paragraphs": [
      {
        "type": "narration",
        "text": "América Latina ingresa en la tercera década del siglo XXI no como un continente atrapado en nostalgias coloniales o fatalismos trágicos, sino como un protagonista vibrante y decisivo de la geopolítica, la cultura y la ética planetarias. En un escenario mundial convulso, marcado por tensiones multipolares, emergencias climáticas globales y aceleradas transformaciones tecnológicas, la región exhibe una singular fortaleza: la memoria acumulada de siglos de resistencia comunitaria, un capital ecológico indispensable para la supervivencia de la biosfera y una juventud creativa que interpela las injusticias del presente con valentía insobornable. Aunado a ello, la riqueza cultural y la diversidad biológica de nuestras tierras constituyen una reserva de esperanza para el planeta entero en una era marcada por la crisis ecológica y la polarización social. Cada bioma, desde los páramos hasta la selva profunda, custodia un equilibrio vital irremplazable."
      },
      {
        "type": "narration",
        "text": "En el terreno de las artes y las ideas, la madurez alcanzada es deslumbrante. El nuevo cine latinoamericano no solicita validación complaciente; con obras rigurosas y descolonizadoras, interpela la mirada global desde la intimidad de los pueblos andinos, las selvas amazónicas y las barriadas metropolitanas. A su vez, la literatura posboom liderada por escritoras excepcionales indaga en las pesadillas de la violencia contemporánea con un lenguaje de precisión quirúrgica y hondura poética, desmantelando los clichés folclorizantes para ofrecer un testimonio desgarrador y esperanzador de nuestra condición humana. En efecto, el dinamismo creador de nuestras cineastas, escritoras y artistas urbanos proyecta al mundo una imagen de dignidad indómita que desmantela los viejos estereotipos coloniales. La narrativa contemporánea desafía las fronteras y conmueve a auditorios de todo el globo."
      },
      {
        "type": "narration",
        "text": "En el tablero económico y ambiental, la posesión del triángulo del litio, las mayores reservas de cobre y agua dulce, y la mayor biodiversidad del planeta sitúan a Suramérica en una posición estratégica inigualable. El imperativo histórico ineludible consiste en desterrar para siempre la vieja trampa extractivista, agregando valor tecnológico mediante alianzas científicas interregionales que generen empleo calificado y respeten escrupulosamente los derechos territoriales de las comunidades locales y la integridad de los ecosistemas fluviales y cordilleranos. Asimismo, la custodia soberana y sustentable de las fuentes de energía limpia, el litio y las cuencas fluviales será el pilar sobre el cual se edifique el bienestar de las próximas generaciones. La cooperación tecnológica entre nuestros países permitirá superar el atraso productivo y garantizar un desarrollo armónico."
      },
      {
        "type": "narration",
        "text": "La voz de las juventudes urbanas y rurales, con su defensa incondicional de los derechos de las mujeres, el activismo ambiental contra el cambio climático y la vitalidad de la música independiente, confirma que el impulso democrático de América Latina sigue más vivo que nunca. Las calles y las redes se han transformado en ágoras de deliberación horizontal donde la ciudadanía se ejerce no como una formalidad electoral quinquenal, sino como una práctica cotidiana de solidaridad, dignidad y cuidado colectivo. Por añadidura, el compromiso inquebrantable de las juventudes con la defensa de los derechos humanos y la igualdad social asegura la renovación permanente de la vida democrática. Las plazas y aulas son espacios vivos de construcción colectiva y esperanza compartida."
      },
      {
        "type": "narration",
        "text": "Al proyectar la mirada hacia el futuro, el sueño de la Patria Grande compartida se reafirma como el único horizonte de viabilidad soberana. Unidos por una lengua de asombrosa ductilidad expresiva, por un pasado común de luchas compartidas y por la certidumbre de un destino solidario, los pueblos de nuestra América avanzan con paso firme. Que este aprendizaje lingüístico y cultural en el nivel B2 sea para el estudiante la llave maestra para tender puentes fraternos con un continente que, fiel a su historia, no cesa de cantar a la libertad, a la justicia y a la dignidad humana. Avanzar hoy con decisión inquebrantable hacia la integración definitiva de la Patria Grande es honrar la memoria viva de nuestros libertadores y garantizar que el porvenir de América Latina se escriba con letras indelebles de justicia social, paz duradera y fraternidad universal."
      }
    ],
    "narration": {
      "pedagogical": {
        "comprehensionQuestions": [
          {
            "question": "¿Cuál es la posición estratégica fundamental de América Latina en la transición ecológica planetaria?",
            "options": [
              "Ser el principal consumidor de carbón mineral del mundo.",
              "Custodiar las mayores reservas de litio, cobre, agua dulce y biodiversidad indispensables para la descarbonización global con justicia socioambiental.",
              "Cerrar todas las centrales hidroeléctricas binacionales.",
              "Depender enteramente de la importación de alimentos básicos del exterior."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Qué rasgo caracteriza la participación política de las juventudes latinoamericanas del siglo XXI?",
            "options": [
              "La indiferencia total ante los problemas medioambientales y de género.",
              "Una acción horizontal, creativa y solidaria que sitúa la justicia climática, los derechos feministas y la dignidad comunitaria en el centro del debate público.",
              "La defensa de los viejos pactos de élites oligárquicas.",
              "La renuncia voluntaria al uso de medios digitales de comunicación."
            ],
            "correctIndex": 1
          },
          {
            "question": "¿Por qué es indispensable consolidar la 'Patria Grande' en el orden multipolar actual?",
            "options": [
              "Porque garantiza la soberanía, la articulación científica y la negociación equilibrada frente a las grandes superpotencias globales.",
              "Porque elimina las fronteras marítimas de la región con la Antártica.",
              "Porque obliga a adoptar un único dialecto local en todo el continente.",
              "Porque sustituye a las Naciones Unidas en todas sus competencias."
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
