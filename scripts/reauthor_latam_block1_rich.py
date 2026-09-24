#!/usr/bin/env python3
"""Re-author Latin America Track Block 1 (Units 01-06, 30 lesson stories).

Units:
01. precolombina (Pre-Columbian America)
02. civilizaciones (Indigenous Civilizations)
03. llegadaeuropeos (Arrival of the Europeans)
04. conquista (The Conquest)
05. sociedadcolonial (Colonial Society)
06. economiacolonial (Colonial Economy)

Standard:
- Rich narrative storytelling (The Rest is History style)
- 400-600 words per story
- Exact verbatim inclusion of target grammar example sentences
- Full coverage of vocabulary lemmas
- Full narrative context for all exercise reading comprehension questions
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "content" / "es-latam" / "stories" / "world" / "b1"

BLOCK1_STORIES = {
    # =========================================================================
    # UNIT 01: precolombina (Pre-Columbian America)
    # =========================================================================
    "b1-precolombina-01-continente.json": {
        "id": "story.b1.precolombina.01",
        "title": "Un continente antes de Europa",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "A continent-wide picture of the Americas before 1492: how many people lived there, how many languages they spoke, and two influential cultures — the Olmec and the Nazca — that came before the Maya, Mexica and Inca.",
        "characters": [],
        "location": "América, del Ártico a la Patagonia",
        "grammar": ["conectores formales"],
        "vocabularyTopics": ["Un continente antes de Europa"],
        "paragraphs": [
            {"type": "narration", "text": "El año 1492 suele presentarse como el inicio de la historia americana, pero la realidad era profundamente distinta. Mucho antes de la llegada de los europeos, América no era un territorio vacío esperando ser descubierto, sino un continente entero que vibraba de vida, comercio e ingenio humano."},
            {"type": "narration", "text": "A lo largo de casi quince mil kilómetros, cientos de pueblos distintos habían desarrollado formas de vida adaptadas a paisajes completamente diferentes. Desde el hielo del Ártico y los densos bosques boreales hasta la selva amazónica, las altas mesetas andinas y las llanuras de la Patagonia, los seres humanos poblaron y transformaron cada rincón de esta inmensa longitud geográfica."},
            {"type": "narration", "text": "¿Cuántas personas vivían en el continente antes de 1492? Los historiadores y demógrafos todavía debaten intensamente esta cifra. Las estimaciones varían enormemente, desde unos cuarenta millones hasta más de cien millones de habitantes en todo el hemisferio. La razón principal de esta incertidumbre es trágica: las enfermedades que llegaron con los europeos, como la viruela y el sarampión, se propagaron con una velocidad devastadora por las rutas comerciales indígenas. Las enfermedades mataron a tanta gente, y tan rápido, que ni siquiera hubo tiempo de contarla."},
            {"type": "narration", "text": "Esa inmensa población hablaba miles de lenguas distintas agrupadas en docenas de familias lingüísticas no emparentadas entre sí, lo que demuestra una extraordinaria diversidad cultural acumulada durante milenios."},
            {"type": "narration", "text": "La base de estas sociedades fue una auténtica revolución agrícola. En Mesoamérica, los antiguos agricultores domesticaron el maíz a partir de una planta silvestre llamada teocintle. El maíz terminó cultivándose a lo largo de todo el continente, mientras que la papa se convirtió en la base de la alimentación andina tras ser domesticada de forma independiente en las alturas de los Andes. Este cultivo resistía el frío extremo y garantizaba la supervivencia en las montañas."},
            {"type": "narration", "text": "Mucho antes de que existieran los mayas, los mexica o los incas, ya se habían desarrollado civilizaciones influyentes. En las costas tropicales del Golfo de México floreció la cultura olmeca, considerada a menudo la «cultura madre» de Mesoamérica. Los olmecas aprendieron a tallar monumentales cabezas colosales de piedra volcánica que pesaban toneladas, y su legado artístico, religioso y arquitectónico influyó en todas las civilizaciones posteriores."},
            {"type": "narration", "text": "En la costa desértica del actual Perú, la civilización nazca dejó otro asombroso misterio. Los antiguos pobladores trazaron en el suelo gigantescas figuras geométricas y animales —las famosas líneas de Nazca— que solo pueden apreciarse plenamente desde el aire. Los arqueólogos todavía debaten su propósito exacto: existen hipótesis astronómicas, rituales religiosos y teorías vinculadas al culto al agua en el desierto, pero ninguna explicación es definitiva."},
            {"type": "narration", "text": "Así, antes del primer contacto transatlántico, las Américas eran un mosaico fascinante de reinos, ciudades monumentales, aldeas y rutas comerciales, forjado por pueblos que habían dominado su entorno con una sofisticación admirable."}
        ],
        "keyVocab": [
            {"lemma": "la diversidad", "pos": "noun", "cefr": "B1", "gloss": "diversity"},
            {"lemma": "el paisaje", "pos": "noun", "cefr": "B1", "gloss": "landscape"},
            {"lemma": "la enfermedad", "pos": "noun", "cefr": "B1", "gloss": "disease"},
            {"lemma": "el legado", "pos": "noun", "cefr": "B1", "gloss": "legacy"},
            {"lemma": "tallar", "pos": "verb", "cefr": "B1", "gloss": "to carve"},
            {"lemma": "la longitud", "pos": "noun", "cefr": "B1", "gloss": "length"},
            {"lemma": "la alimentación", "pos": "noun", "cefr": "B1", "gloss": "diet, food supply"},
            {"lemma": "el cultivo", "pos": "noun", "cefr": "B1", "gloss": "crop"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué es difícil saber con exactitud cuántas personas vivían en América antes de 1492?",
                "options": [
                    "Porque las enfermedades europeas causaron una gran mortalidad antes de que pudieran contarse.",
                    "Porque nadie vivía en el continente en esa época.",
                    "Porque los pueblos indígenas no tenían ciudades ni asentamientos."
                ],
                "correctIndex": 0,
                "explanation": "Las epidemias diezmaron a las poblaciones indígenas rápidamente antes de los primeros censos coloniales."
            }
        ]
    },

    "b1-precolombina-02-civilizaciones.json": {
        "id": "story.b1.precolombina.02",
        "title": "Tres civilizaciones, tres mundos",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "A closer, fact-rich look at the Maya, Mexica and Inca worlds — what made each one distinctive, what they achieved, and what survives of them today.",
        "characters": [],
        "location": "Mesoamérica y los Andes",
        "grammar": ["se pasiva / impersonal", "voz pasiva"],
        "vocabularyTopics": ["Grandes civilizaciones"],
        "paragraphs": [
            {"type": "narration", "text": "Cuando pensamos en el mundo precolombino, tres grandes nombres dominan la memoria colectiva: los mayas, los mexicas y los incas. Aunque a menudo se estudian juntos, cada una de estas civilizaciones representaba un mundo propio con logros técnicos, políticos y lingüísticos únicos."},
            {"type": "narration", "text": "Los mayas se establecieron en las selvas y montañas de Mesoamérica, en territorios que hoy corresponden a Guatemala, el sur de México, Belice y Honduras. A diferencia de lo que muchos creen, nunca formaron un imperio unificado bajo una sola capital. Los mayas se organizaron en decenas de ciudades-estado independientes, como Tikal, Palenque, Calakmul y Copán, que competían, comerciaban y guerreaban constantemente entre sí."},
            {"type": "narration", "text": "Los sabios mayas desarrollaron una compleja escritura jeroglífica en la que cada glifo tallado combinaba sonidos y significados. Además, crearon un sistema numérico vigesimal con el concepto del cero y un calendario solar asombrosamente exacto. Sin embargo, hacia el siglo noveno, muchas ciudades mayas del sur fueron abandonadas repentinamente. Todavía se debate por qué fueron abandonadas: la evidencia científica apunta a una combinación de sequías prolongadas, agotamiento ecológico del suelo y guerras destructivas entre dinastías rivales."},
            {"type": "narration", "text": "Más al norte, en el valle central de México, los mexicas (conocidos comúnmente como aztecas) construyeron una potencia muy diferente. Según la leyenda, su dios Huitzilopochtli les ordenó fundar su ciudad donde vieran un águila posada sobre un nopal devorando una serpiente: una imagen sagrada que hoy ocupa el centro de la bandera mexicana. En 1325 fundaron Tenochtitlan sobre una isla del lago de Texcoco."},
            {"type": "narration", "text": "En poco más de un siglo, los mexicas construyeron un formidable imperio militar mediante una triple alianza con ciudades vecinas. El náhuatl era la lengua franca que conectaba a millones de personas. Tenochtitlan deslumbraba con sus canales navegables, puentes levadizos y calzadas de piedra, convirtiéndose en una de las urbes más grandes del mundo en su época."},
            {"type": "narration", "text": "Miles de kilómetros al sur, en las alturas andinas de Sudamérica, los incas forjaron el Tawantinsuyu, el imperio más extenso de la América precolombina. Cuzco se convirtió en el centro político y religioso de todo el imperio, concebido como el «ombligo del mundo»."},
            {"type": "narration", "text": "Los incas lograron dominar una geografía vertical extrema. Para conectar su territorio, trazaron el Qhapaq Ñan, un camino real de más de treinta mil kilómetros con puentes colgantes tendidos sobre profundos abismos. Sin caballos ni ruedas, la comunicación descansaba en veloces corredores llamados chasquis, que se turnaban para llevar mensajes oficiales a través de miles de kilómetros en pocos días."},
            {"type": "narration", "text": "La administración incaica no utilizaba escritura alfabética, sino el quipu: un ingenioso sistema de cuerdas de colores y nudos para registrar censos, cosechas y tributos. La información de los quipus todavía no se ha logrado descifrar del todo en sus aspectos narrativos. En la arquitectura, construyeron muros ciclópeos con piedras encajadas con tal precisión que ni el terremoto más violento lograba derribarlos."},
            {"type": "narration", "text": "Hoy en día persiste el mito de que estas civilizaciones desaparecieron por completo. En realidad, millones de descendientes directos de mayas, mexicas e incas mantienen vivas sus tradiciones, y lenguas ancestrales como el maya, el náhuatl y el quechua son habladas a diario por comunidades enteras."}
        ],
        "keyVocab": [
            {"lemma": "el glifo", "pos": "noun", "cefr": "B1", "gloss": "glyph"},
            {"lemma": "la escritura", "pos": "noun", "cefr": "B1", "gloss": "writing (system)"},
            {"lemma": "el imperio", "pos": "noun", "cefr": "B1", "gloss": "empire"},
            {"lemma": "la ciudad-estado", "pos": "noun", "cefr": "B1", "gloss": "city-state"},
            {"lemma": "el calendario", "pos": "noun", "cefr": "B1", "gloss": "calendar"},
            {"lemma": "el camino", "pos": "noun", "cefr": "B1", "gloss": "road"},
            {"lemma": "el puente", "pos": "noun", "cefr": "B1", "gloss": "bridge"},
            {"lemma": "el terremoto", "pos": "noun", "cefr": "B1", "gloss": "earthquake"},
            {"lemma": "el descendiente", "pos": "noun", "cefr": "B1", "gloss": "descendant"},
            {"lemma": "la lengua", "pos": "noun", "cefr": "B1", "gloss": "language"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué los mayas nunca formaron un solo imperio unificado?",
                "options": [
                    "Porque estaban organizados en ciudades-estado independientes que competían entre sí.",
                    "Porque carecían de ejército y de líderes políticos.",
                    "Porque todas sus ciudades fueron destruidas antes del periodo Clásico."
                ],
                "correctIndex": 0,
                "explanation": "El mundo maya estaba compuesto por decenas de reinos y ciudades-estado autónomas."
            }
        ]
    },

    "b1-precolombina-03-sociedad.json": {
        "id": "story.b1.precolombina.03",
        "title": "Sociedad y poder",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How power, rank and religion actually organised Maya, Mexica and Inca society — divine kingship, a labour tax instead of money, and social mobility through war.",
        "characters": [],
        "location": "Mesoamérica y los Andes",
        "grammar": ["voz pasiva", "se pasiva / impersonal"],
        "vocabularyTopics": ["Sociedad y poder"],
        "paragraphs": [
            {"type": "narration", "text": "En las grandes civilizaciones precolombinas, el poder político y el orden religioso eran inseparables. Los gobernantes no solo administraban ciudades y ejércitos, sino que personificaban la conexión sagrada entre los seres humanos y el cosmos."},
            {"type": "narration", "text": "Entre los mayas clásicos, el monarca recibía el título de k'uhul ajaw, es decir, «señor sagrado». Se creía que el cuerpo del rey era un canal directo con los dioses y los antepasados divinizados. Durante ceremonias solemnes, el rey y la reina realizaban autosacrificios de sangre para nutrir a las fuerzas del universo. La sangre derramada se ofrecía a los dioses en tiras de papel de corteza que luego se quemaban. El ritual se representaba en estelas de piedra que todavía pueden verse hoy en plazas ceremoniales de todo el mundo maya."},
            {"type": "narration", "text": "La sociedad mexica, por su parte, combinaba una estricta jerarquía con oportunidades de ascenso social. La base comunitaria eran los calpulli, barrios organizados por parentesco que poseían tierras colectivas. Por encima de los agricultores comunes se encontraba la nobleza hereditaria, pero la guerra ofrecía un camino único para la movilidad social. Un plebeyo que demostraba gran valentía como guerrero y capturaba prisioneros en combate podía ingresar en prestigiosas órdenes militares, como los guerreros águila o los guerreros jaguar, ganando tierras, privilegios y respeto en la corte."},
            {"type": "narration", "text": "El gobierno mexica se basaba en la hegemonía militar y la recaudación de tributos. Se exigía tributo a las ciudades sometidas, pero rara vez se sustituía a sus gobernantes locales. Cada provincia enviaba periódicamente al palacio mantas de algodón finamente tejidas, plumas de quetzal, granos de maíz, frijol y oro en polvo."},
            {"type": "narration", "text": "En el imperio inca, el poder se organizaba de forma muy distinta. Los incas no mantenían a los gobernantes derrotados en la distancia, sino que integraban directamente cada región en una estructura estatal centralizada, imponiendo el culto solar y el quechua como lengua administrativa."},
            {"type": "narration", "text": "La economía incaica no utilizaba dinero, mercados comerciales ni monedas. El Estado cobraba el impuesto a través del mit'a: un sistema de trabajo por turnos obligatorios. Cada comunidad o ayllu aportaba hombres para trabajar en obras públicas, construir terrazas agrícolas, tejer ropa para los almacenes estatales o servir en el ejército imperial. A cambio, el Inca garantizaba protección, ayuda alimentaria en años de malas cosechas y banquetes ceremoniales."},
            {"type": "narration", "text": "En ambos mundos, el rigor social era inflexible. Quienes no podían pagar una deuda o cometían delitos graves podían caer en la servidumbre personal. La pirámide social descansaba en la obediencia, y el poder estatal lograba someter territorios enteros bajo una disciplina meticulosa."}
        ],
        "keyVocab": [
            {"lemma": "sagrado", "pos": "adjective", "cefr": "B1", "gloss": "sacred"},
            {"lemma": "la estela", "pos": "noun", "cefr": "B1", "gloss": "stele"},
            {"lemma": "el guerrero", "pos": "noun", "cefr": "B1", "gloss": "warrior"},
            {"lemma": "la movilidad", "pos": "noun", "cefr": "B1", "gloss": "mobility"},
            {"lemma": "la servidumbre", "pos": "noun", "cefr": "B1", "gloss": "servitude"},
            {"lemma": "la deuda", "pos": "noun", "cefr": "B1", "gloss": "debt"},
            {"lemma": "el impuesto", "pos": "noun", "cefr": "B1", "gloss": "tax"},
            {"lemma": "someter", "pos": "verb", "cefr": "B1", "gloss": "to subjugate"}
        ],
        "compQuestions": [
            {
                "question": "¿Cómo funcionaba el sistema de impuestos en el Imperio Inca?",
                "options": [
                    "Se pagaba mediante el mit'a, un sistema obligatorio de trabajo por turnos en obras públicas y agricultura.",
                    "Se cobraba exclusivamente en monedas de oro y plata.",
                    "Cada familia pagaba un porcentaje fijo de granos en los mercados locales."
                ],
                "correctIndex": 0,
                "explanation": "El imperio inca no usaba moneda; los tributos se pagaban con trabajo físico organizado (mit'a)."
            }
        ]
    },

    "b1-precolombina-04-vidacotidiana.json": {
        "id": "story.b1.precolombina.04",
        "title": "Vida cotidiana",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Everyday life before Europeans arrived: a food-science trick behind maize that Europe didn't understand for centuries, chocolate as a bitter elite drink, coca leaves in the Andes, and a ballgame played across two thousand years.",
        "characters": [],
        "location": "Mesoamérica y los Andes",
        "grammar": ["gerundio para acción paralela"],
        "vocabularyTopics": ["Vida cotidiana"],
        "paragraphs": [
            {"type": "narration", "text": "¿Cómo transcurría un día común en una ciudad o aldea antes de 1492? Lejos de los palacios y los templos monumentales, la vida cotidiana estaba marcada por el trabajo agrícola, los mercados bulliciosos, la gastronomía y las tradiciones familiares."},
            {"type": "narration", "text": "La alimentación popular giraba en torno al maíz, el frijol, la calabaza y el chile. Sin embargo, el secreto fundamental de la nutrición mesoamericana residía en una genial innovación química: la nixtamalización. Cocinando los granos con cal o ceniza, los pueblos mesoamericanos liberaban nutrientes que el maíz crudo no ofrece, especialmente la niacina o vitamina B3 y aminoácidos esenciales. Cuando los europeos llevaron el maíz a su continente pero ignoraron este método tradicional, surgieron durante siglos terribles epidemias de pelagra y desnutrición en poblaciones rurales de Europa."},
            {"type": "narration", "text": "Los alimentos se sazonaban con diversas hierbas y cada especia disponible, como la vainilla y el achiote. En ocasiones especiales, los nobles y guerreros disfrutaban del cacao, considerado un regalo divino. El chocolate se preparaba batiendo cacao molido con agua, chile y especias hasta formar espuma. A diferencia de las golosinas dulces actuales, era una bebida densa y de sabor amargo. Además de su uso ceremonial, los granos de cacao servían como moneda para comprar bienes en los mercados o pagar sanciones."},
            {"type": "narration", "text": "En las altas mesetas de los Andes, la vida diaria exigía una adaptación constante al frío y a la altitud. Masticando hojas de coca, los habitantes de las alturas combatían el hambre, el frío y el mal de altura, aprovechando sus propiedades medicinales y energéticas durante las duras jornadas en las terrazas de cultivo."},
            {"type": "narration", "text": "La vestimenta marcaba con absoluta claridad el rango de cada individuo en la comunidad. Mientras los campesinos vestían telas sencillas de maguey o algodón sin teñir, los nobles lucían mantas ricamente bordadas y tocados con plumas de aves exóticas. En el imperio inca, las telas más finas de lana de vicuña estaban reservadas por ley exclusivamente para el soberano y su familia más cercana."},
            {"type": "narration", "text": "El ocio y la religión se entrelazaban en el juego de pelota, una práctica deportiva practicada durante más de dos milenios en toda Mesoamérica. Comerciando, tejiendo o cultivando, la mayoría de la gente también encontraba tiempo para el juego de pelota. En la cancha de piedra, los jugadores golpeaban una pesada pelota de hule macizo usando solo las caderas, los codos y las rodillas. En algunas ciudades, el juego de pelota se relacionaba con rituales religiosos donde el resultado simbolizaba el movimiento del sol y la lucha cósmica contra las fuerzas del inframundo, culminando en ocasiones solemnes con un sacrificio humano."}
        ],
        "keyVocab": [
            {"lemma": "la desnutrición", "pos": "noun", "cefr": "B1", "gloss": "malnutrition"},
            {"lemma": "amargo", "pos": "adjective", "cefr": "B1", "gloss": "bitter"},
            {"lemma": "la especia", "pos": "noun", "cefr": "B1", "gloss": "spice"},
            {"lemma": "masticar", "pos": "verb", "cefr": "B1", "gloss": "to chew"},
            {"lemma": "la vestimenta", "pos": "noun", "cefr": "B1", "gloss": "clothing, attire"},
            {"lemma": "el rango", "pos": "noun", "cefr": "B1", "gloss": "rank"},
            {"lemma": "la cancha", "pos": "noun", "cefr": "B1", "gloss": "court (sports)"},
            {"lemma": "el sacrificio", "pos": "noun", "cefr": "B1", "gloss": "sacrifice"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué ventaja ofrecía la técnica de la nixtamalización al cocinar el maíz?",
                "options": [
                    "Liberaba nutrientes esenciales y vitaminas que prevenían la desnutrición y la pelagra.",
                    "Hacía que el maíz se conservara durante años sin pudrirse.",
                    "Permitía cocinar el maíz sin necesidad de fuego ni agua."
                ],
                "correctIndex": 0,
                "explanation": "La cocción alcalina del maíz con cal o ceniza liberaba niacina asimilable para el cuerpo humano."
            }
        ]
    },

    "b1-precolombina-05-evidencia.json": {
        "id": "story.b1.precolombina.05",
        "title": "Antes de la conquista",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How do we actually know what we know about the Maya, Mexica and Inca? Surviving codices, a friar who burned most of them, radiocarbon dating, and a sacred text copied down after the conquest.",
        "characters": [],
        "location": "Mesoamérica y los Andes",
        "grammar": ["conectores formales: a pesar de, a raíz de"],
        "vocabularyTopics": ["Antes de la conquista"],
        "paragraphs": [
            {"type": "narration", "text": "¿Cómo podemos reconstruir hoy la historia, el pensamiento y la vida de civilizaciones que florecieron hace siglos? Recuperar la memoria precolombina ha sido una apasionante labor detectivesca en la que los investigadores deben contrastar documentos antiguos, relatos orales y descubrimientos científicos."},
            {"type": "narration", "text": "Antes del siglo dieciséis, las culturas mesoamericanas conservaban sus crónicas, conocimientos astronómicos y calendarios en manuscritos pintados sobre papel de corteza o piel de venado llamados códices. Lamentablemente, durante los primeros años de la conquista, las autoridades eclesiásticas europeas consideraron que estos textos contenían idolatrías diabólicas y ordenaron quemar bibliotecas enteras. El episodio más trágico ocurrió en 1562 en Maní, Yucatán, donde el fraile franciscano Diego de Landa organizó un auto de fe en el que mandó quemar decenas de códices mayas invaluables junto con miles de esculturas sagradas."},
            {"type": "narration", "text": "A raíz de ese acto, y de otras destrucciones similares durante la conquista, casi toda la literatura maya escrita desapareció para siempre. A pesar de que los mayas escribían con un sistema jeroglífico completo, hoy solo sobreviven cuatro libros mayas originales: los códices de Dresde, Madrid, París y el códice Maya de México (antes conocido como Códice Grolier). La autenticidad del códice Grolier fue puesta en duda durante más de cuarenta años por diversos especialistas antes de que exhaustivos análisis químicos y de datación confirmaran que se trataba del manuscrito legible más antiguo del continente americano."},
            {"type": "narration", "text": "A pesar de la destrucción masiva, los propios indígenas buscaron ingeniosas maneras de hacer sobrevivir su memoria y su legado. A mediados del siglo dieciséis, sabios mayas k'iche' en Guatemala transcribieron clandestinamente su gran relato cosmogónico, el Popol Vuh, utilizando el alfabeto latino recién aprendido. Hacia 1701, el fraile dominico Francisco Ximénez localizó este manuscrito en Chichicastenango, lo copió y lo tradujo al castellano, salvando una de las mayores obras literarias de la humanidad."},
            {"type": "narration", "text": "Junto a los textos escritos, la arqueología moderna constituye una fuente directa y fiable para descifrar el pasado. El análisis de inscripciones en estelas con el calendario de Cuenta Larga, la datación por radiocarbono en restos orgánicos y la tecnología de escaneo láser (LiDAR) en la selva ofrecen hoy la evidencia más sólida sobre ciudades enteras que permanecían ocultas bajo la vegetación."},
            {"type": "narration", "text": "A pesar de las lagunas y las pérdidas, cada fuente aporta una pieza distinta del rompecabezas. Los científicos examinan cada monumento, vasija o fragmento como una prueba esencial de aquel mundo fascinante. Cada nuevo hallazgo arqueológico confirma la riqueza de estas culturas. A raíz de descubrimientos recientes, la imagen del mundo precolombino sigue cambiando, revelando una historia mucho más densa, compleja y brillante de lo que jamás imaginamos."}
        ],
        "keyVocab": [
            {"lemma": "el legado", "pos": "noun", "cefr": "B1", "gloss": "legacy"},
            {"lemma": "la fuente", "pos": "noun", "cefr": "B1", "gloss": "source"},
            {"lemma": "la evidencia", "pos": "noun", "cefr": "B1", "gloss": "evidence"},
            {"lemma": "la prueba", "pos": "noun", "cefr": "B1", "gloss": "proof"},
            {"lemma": "quemar", "pos": "verb", "cefr": "B1", "gloss": "to burn"},
            {"lemma": "sobrevivir", "pos": "verb", "cefr": "B1", "gloss": "to survive"},
            {"lemma": "el hallazgo", "pos": "noun", "cefr": "B1", "gloss": "finding, discovery"},
            {"lemma": "fiable", "pos": "adjective", "cefr": "B1", "gloss": "reliable"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué sobrevivieron tan pocos códices mayas originales hasta hoy?",
                "options": [
                    "Porque en 1562 el fraile Diego de Landa y las autoridades coloniales ordenaron quemar decenas de manuscritos.",
                    "Porque los mayas escribían únicamente sobre hojas perecederas que se pudrieron rápidamente.",
                    "Porque los códices fueron escondidos en cuevas secretas que nadie ha podido encontrar."
                ],
                "correctIndex": 0,
                "explanation": "La quema sistemática de códices durante la evangelización colonial destruyó casi toda la literatura escrita."
            }
        ]
    },

    # =========================================================================
    # UNIT 02: civilizaciones (Indigenous Civilizations)
    # =========================================================================
    "b1-civilizaciones-01-mayas.json": {
        "id": "story.b1.civilizaciones.01",
        "title": "Los mayas",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Maya world in depth: deciphering glyph writing, vigesimal mathematics with zero, architectural wonders, and lake-sediment evidence for the Classic collapse.",
        "characters": [],
        "location": "Mesoamérica (tierras bajas y selvas)",
        "grammar": ["voz pasiva en narración histórica"],
        "vocabularyTopics": ["Los mayas"],
        "paragraphs": [
            {"type": "narration", "text": "Durante más de tres milenios, los mayas crearon en las selvas de Centroamérica una de las civilizaciones más deslumbrantes de la antigüedad. En ciudades monumentales como Tikal, Copán, Palenque y Calakmul, levantaron imponentes pirámides de piedra caliza que se elevaban por encima de la densa copa de los árboles."},
            {"type": "narration", "text": "El logro intelectual más extraordinario de los mayas fue su sistema de escritura jeroglífica, el único sistema completamente fonético y desarrollado de la América precolombina. Durante siglos, los sabios mayas grabaron textos históricos y astronómicos en estelas, vasijas de cerámica y códices de corteza."},
            {"type": "narration", "text": "La escritura maya fue finalmente descifrada en el siglo veinte. El lingüista soviético Yuri Knórozov demostró que los glifos combinaban signos fonéticos y logogramas, permitiendo a los arqueólogos leer directamente las voces de los reyes y escribas mayas."},
            {"type": "narration", "text": "En matemáticas y astronomía, los mayas alcanzaron una precisión asombrosa. Inventaron un sistema numérico vigesimal (en base 20) que incorporaba el concepto abstracto del cero siglos antes de que este fuera adoptado en Europa. Sus astrónomos calcularon los ciclos de la Luna, el planeta Venus y los eclipses solares con un margen de error de apenas minutos."},
            {"type": "narration", "text": "Sin embargo, hacia los siglos octavo y noveno, el mundo maya clásico experimentó una profunda crisis. Numerosas ciudades del sur fueron abandonadas por sus habitantes en un lapso relativamente breve. Durante mucho tiempo, este fenómeno se consideró un misterio impenetrable."},
            {"type": "narration", "text": "El colapso de las ciudades del sur fue causado por una combinación de factores. Recientes análisis de sedimentos en lagos y estalagmitas en cuevas han demostrado que la región sufrió prolongadas e intensas sequías. Estas catástrofes climáticas, sumadas a la deforestación agrícola y a guerras dinásticas destructivas, provocaron el colapso de los grandes centros ceremoniales."},
            {"type": "narration", "text": "A pesar de este declive en las tierras bajas del sur, la civilización maya continuó floreciendo en el norte de la península de Yucatán en urbes magníficas como Chichén Itzá y Mayapán, demostrando una notable capacidad de adaptación y resiliencia."}
        ],
        "keyVocab": [
            {"lemma": "el desciframiento", "pos": "noun", "cefr": "B1", "gloss": "decipherment"},
            {"lemma": "el jeroglífico", "pos": "noun", "cefr": "B1", "gloss": "hieroglyph"},
            {"lemma": "la precisión", "pos": "noun", "cefr": "B1", "gloss": "precision"},
            {"lemma": "vigesimal", "pos": "adjective", "cefr": "B1", "gloss": "vigesimal (base-20)"},
            {"lemma": "el colapso", "pos": "noun", "cefr": "B1", "gloss": "collapse"},
            {"lemma": "la sequía", "pos": "noun", "cefr": "B1", "gloss": "drought"},
            {"lemma": "el sedimento", "pos": "noun", "cefr": "B1", "gloss": "sediment"},
            {"lemma": "florecer", "pos": "verb", "cefr": "B1", "gloss": "to flourish"}
        ],
        "compQuestions": [
            {
                "question": "¿Quién demostró que los glifos mayas tenían un valor fonético en el siglo XX?",
                "options": [
                    "El lingüista Yuri Knórozov.",
                    "El arqueólogo Diego de Landa.",
                    "El explorador Francisco Pizarro."
                ],
                "correctIndex": 0,
                "explanation": "Yuri Knórozov descubrió la clave fonética que permitió descifrar la escritura jeroglífica maya."
            }
        ]
    },

    "b1-civilizaciones-02-mexicas.json": {
        "id": "story.b1.civilizaciones.02",
        "title": "Los mexicas",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Mexica empire: the founding of Tenochtitlan, the Triple Alliance, chinampa agriculture, the Codex Mendoza, and the rediscovery of the Templo Mayor.",
        "characters": [],
        "location": "Valle de México",
        "grammar": ["se pasiva / impersonal"],
        "vocabularyTopics": ["Los mexicas"],
        "paragraphs": [
            {"type": "narration", "text": "A principios del siglo catorce, un pueblo nómada de origen norteño llegó al fértil valle de México. Se llamaban a sí mismos mexicas. En 1325, tras una larga peregrinación guiada por augurios religiosos, fundaron su capital, México-Tenochtitlan, sobre un islote pantanoso en medio del lago salado de Texcoco."},
            {"type": "narration", "text": "Para alimentar a una población que pronto superó los doscientos mil habitantes en un lago sin tierra firme disponible, los mexicas desarrollaron una asombrosa ingeniería agrícola: las chinampas. Se construían islas artificiales rectangulares con capas de juncos, barro y ramas fijadas al fondo del lago con raíces de sauces. Estas huertas flotantes permitían obtener hasta cuatro cosechas al año de maíz, frijol, calabaza y flores."},
            {"type": "narration", "text": "En el plano militar y político, los mexicas consolidaron su poder en 1428 mediante la formación de la Triple Alianza junto con las ciudades-estado de Texcoco y Tlacopan. A través de campañas militares expansivas, sometieron a cientos de pueblos desde el centro de México hasta las costas del océano Pacífico y el golfo de México."},
            {"type": "narration", "text": "Se exigían tributos periódicos a las provincias sometidas. El Códice Mendoza, un extraordinario manuscrito colonial, ilustra con detalle los miles de mantas de algodón bordadas, tocados de plumas preciosas, trajes de guerrero, jade, cacao y toneladas de alimentos que llegaban anualmente a los palacios imperiales."},
            {"type": "narration", "text": "En el corazón sagrado de la capital se levantaba el Templo Mayor, una colosal pirámide doble dedicada a Tláloc, dios de la lluvia, y a Huitzilopochtli, dios de la guerra. Durante siglos tras la conquista, sus cimientos quedaron sepultados bajo los edificios de la Ciudad de México."},
            {"type": "narration", "text": "En 1978, trabajadores de la compañía de luz descubrieron accidentalmente el monumental monolito de la diosa Coyolxauhqui en el centro histórico, lo que dio inicio a las excavaciones científicas del Templo Mayor. Cada nuevo hallazgo ha permitido a los historiadores debatir con mayor rigor el significado y la escala real de los rituales religiosos y el sacrificio humano en la sociedad mexica."},
            {"type": "narration", "text": "Tenochtitlan deslumbró a los primeros europeos que la contemplaron. Con sus amplias calzadas de piedra, acueductos de agua dulce, mercados inmensos como el de Tlatelolco y canales donde navegaban miles de canoas, era una de las urbes más ordenadas y limpias del mundo del siglo quince."}
        ],
        "keyVocab": [
            {"lemma": "la chinampa", "pos": "noun", "cefr": "B1", "gloss": "artificial agricultural island"},
            {"lemma": "el islote", "pos": "noun", "cefr": "B1", "gloss": "islet"},
            {"lemma": "la peregrinación", "pos": "noun", "cefr": "B1", "gloss": "pilgrimage"},
            {"lemma": "la alianza", "pos": "noun", "cefr": "B1", "gloss": "alliance"},
            {"lemma": "el tributo", "pos": "noun", "cefr": "B1", "gloss": "tribute"},
            {"lemma": "el monolito", "pos": "noun", "cefr": "B1", "gloss": "monolith"},
            {"lemma": "el acueducto", "pos": "noun", "cefr": "B1", "gloss": "aqueduct"},
            {"lemma": "el cimiento", "pos": "noun", "cefr": "B1", "gloss": "foundation"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué documento colonial registra con detalle los tributos que recibía el imperio mexica?",
                "options": [
                    "El Códice Mendoza.",
                    "El Códice de Dresde.",
                    "El Popol Vuh."
                ],
                "correctIndex": 0,
                "explanation": "El Códice Mendoza es famoso por sus listas pictográficas de tributos provinciales mexicas."
            }
        ]
    },

    "b1-civilizaciones-03-incas.json": {
        "id": "story.b1.civilizaciones.03",
        "title": "Los incas",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Inca empire: Tawantinsuyu, the Qhapaq Ñan road network, quipu accounting, terrace farming, royal mummy cults, and the rediscovery of Machu Picchu.",
        "characters": [],
        "location": "Los Andes (Cuzco, Perú, Bolivia, Ecuador)",
        "grammar": ["voz pasiva y conectores"],
        "vocabularyTopics": ["Los incas"],
        "paragraphs": [
            {"type": "narration", "text": "En las alturas monumentales de la cordillera de los Andes, los incas forjaron el Tawantinsuyu, que en lengua quechua significa «las cuatro regiones unidas». Entre los siglos quince y dieciséis, este imperio llegó a abarcar más de cuatro mil kilómetros a lo largo de los actuales territorios de Perú, Bolivia, Ecuador, el sur de Colombia, el norte de Chile y el noroeste de Argentina."},
            {"type": "narration", "text": "La capital, Cuzco, era el centro neurálgico del imperio. Desde allí, los incas gobernaban a más de diez millones de súbditos mediante una administración estatal de una eficiencia incomparable. Para dominar las escarpadas laderas de las montañas, los agricultores incas construyeron miles de andenes o terrazas agrícolas escalonadas con muros de piedra. En sitios como Moray, diseñaron terrazas circulares concéntricas que creaban microclimas artificiales para experimentar con diferentes variedades de cultivos."},
            {"type": "narration", "text": "Para articular este inmenso territorio montañoso, los incas construyeron el Qhapaq Ñan, una red de caminos empedrados de más de treinta mil kilómetros que cruzaba desiertos costeros, punas heladas y cumbres andinas. La comunicación se realizaba mediante relevos de corredores profesionales llamados chasquis, capaces de transportar mensajes y productos frescos desde la costa hasta Cuzco en pocos días."},
            {"type": "narration", "text": "El registro contable, demográfico y tributario del imperio se llevaba a cabo con el quipu. Este complejo instrumento consistía en una cuerda principal de la que colgaban hilos de algodón o lana de vicuña con nudos dispuestos en un sistema decimal. Aunque los funcionarios incas (los quipucamayocs) leían los quipus con facilidad, su código exacto sigue siendo objeto de investigación científica."},
            {"type": "narration", "text": "La política imperial estaba profundamente marcada por el culto a las momias de los reyes difuntos. Al morir un Inca, su cuerpo era momificado y conservaba todas sus propiedades y palacios. Debido a esto, cada nuevo emperador debía conquistar nuevas tierras y riquezas para financiar su propia corte y garantizar su prestigio."},
            {"type": "narration", "text": "La arquitectura incaica alcanzó su cumbre en fortalezas y ciudadelas como Sacsayhuamán y Machu Picchu. Construida en una cresta montañosa sobre el valle del río Urubamba, Machu Picchu permaneció oculta para los conquistadores españoles hasta su difusión científica internacional en 1911 por el explorador estadounidense Hiram Bingham."},
            {"type": "narration", "text": "Con su ingeniería sísmica de piedras perfectamente ensambladas sin argamasa, sus caminos infinitos y su organización comunitaria, los incas lograron domar el paisaje más empinado y desafiante del planeta."}
        ],
        "keyVocab": [
            {"lemma": "la cordillera", "pos": "noun", "cefr": "B1", "gloss": "mountain range"},
            {"lemma": "el andén", "pos": "noun", "cefr": "B1", "gloss": "agricultural terrace"},
            {"lemma": "el relevo", "pos": "noun", "cefr": "B1", "gloss": "relay"},
            {"lemma": "el quipu", "pos": "noun", "cefr": "B1", "gloss": "knotted cord accounting system"},
            {"lemma": "la momia", "pos": "noun", "cefr": "B1", "gloss": "mummy"},
            {"lemma": "ensamblar", "pos": "verb", "cefr": "B1", "gloss": "to assemble, fit together"},
            {"lemma": "la cumbre", "pos": "noun", "cefr": "B1", "gloss": "summit, peak"},
            {"lemma": "escarpado", "pos": "adjective", "cefr": "B1", "gloss": "steep, rugged"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué cada nuevo emperador inca debía conquistar nuevos territorios?",
                "options": [
                    "Porque las momias de los emperadores anteriores conservaban sus palacios y riquezas.",
                    "Porque las leyes prohibían que los hijos vivieran en la misma ciudad que sus padres.",
                    "Porque el Cuzco era destruido ritualmente tras la muerte de cada soberano."
                ],
                "correctIndex": 0,
                "explanation": "El culto a los ancestros reales otorgaba las propiedades del difunto a su linaje (panaca) para su cuidado perpetuo."
            }
        ]
    },

    "b1-civilizaciones-04-religion.json": {
        "id": "story.b1.civilizaciones.04",
        "title": "Religión y conocimiento",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Sacred cosmology and indigenous science: Andean huacas, Maya scribal castes, Mexica astronomy, and herbal medicine in the Codex De la Cruz-Badiano.",
        "characters": [],
        "location": "Mesoamérica y los Andes",
        "grammar": ["gerundio y conectores"],
        "vocabularyTopics": ["Religión y conocimiento"],
        "paragraphs": [
            {"type": "narration", "text": "Para los pueblos precolombinos, la ciencia, la observación de la naturaleza y la espiritualidad formaban un tejido indivisible. El cosmos no era un espacio inerte, sino un organismo vivo habitado por fuerzas divinas con las que la humanidad debía mantener un equilibrio constante mediante rituales, ofrendas y estudio meticuloso."},
            {"type": "narration", "text": "En el mundo andino, la religión giraba en torno al concepto de la Pachamama (la Madre Tierra) y las huacas. Una huaca podía ser una montaña imponente (un apu), una roca singular, una cueva sagrada o la tumba de un antepasado ilustre. Los sacerdotes andinos se comunicaban con estas entidades sagradas haciendo ofrendas de chicha de maíz, hojas de coca y tejidos finos, buscando asegurar la fertilidad de los campos y la armonía comunitaria."},
            {"type": "narration", "text": "En Mesoamérica, los escribas y sacerdotes pertenecían a castas hereditarias de altísimo prestigio social. Eran los guardianes de los libros sagrados y de la memoria colectiva. Observando el firmamento noche tras noche desde lo alto de los observatorios de piedra, los astrónomos mayas y mexicas registraban con precisión matemática los solsticios, equinoccios y conjunciones planetarias, conocimientos indispensables para determinar las fechas exactas de la siembra y las fiestas rituales."},
            {"type": "narration", "text": "La medicina tradicional indígena alcanzó un desarrollo extraordinario gracias a un profundo conocimiento botánico y farmacológico. Los médicos nahuas (los ticitl) clasificaban cientos de plantas medicinales, resinas y minerales según sus propiedades curativas para tratar heridas, fracturas óseas, fiebres y enfermedades infecciosas."},
            {"type": "narration", "text": "Gran parte de este saber médico quedó plasmado en el Códice De la Cruz-Badiano (o Libellus de Medicinalibus Indorum Herbis), un tratado herbolario redactado en náhuatl y traducido al latín en 1552 por sabios indígenas en el Colegio de Santa Cruz de Tlatelolco. Tras permanecer extraviado durante siglos, el manuscrito fue redescubierto en la Biblioteca Vaticana en 1929, confirmando la sofisticación de la ciencia médica mesoamericana."},
            {"type": "narration", "text": "Así, combinando la observación empírica con una visión sagrada de la naturaleza, los sabios indígenas crearon sistemas de conocimiento que desafiaron el paso del tiempo y dejaron un legado científico y espiritual imperecedero."}
        ],
        "keyVocab": [
            {"lemma": "el cosmos", "pos": "noun", "cefr": "B1", "gloss": "cosmos"},
            {"lemma": "sagrado", "pos": "adjective", "cefr": "B1", "gloss": "sacred"},
            {"lemma": "la ofrenda", "pos": "noun", "cefr": "B1", "gloss": "offering"},
            {"lemma": "la casta", "pos": "noun", "cefr": "B1", "gloss": "caste"},
            {"lemma": "el firmamento", "pos": "noun", "cefr": "B1", "gloss": "firmament, sky"},
            {"lemma": "el solsticio", "pos": "noun", "cefr": "B1", "gloss": "solstice"},
            {"lemma": "la propiedad", "pos": "noun", "cefr": "B1", "gloss": "property, characteristic"},
            {"lemma": "herbolario", "pos": "adjective", "cefr": "B1", "gloss": "herbal"}
        ],
        "compQuestions": [
            {
                "question": "¿Dónde fue redescubierto en 1929 el Códice De la Cruz-Badiano de medicina herbolaria?",
                "options": [
                    "En la Biblioteca Vaticana.",
                    "En una tumba subterránea en Tenochtitlan.",
                    "En el Museo del Prado en Madrid."
                ],
                "correctIndex": 0,
                "explanation": "El famoso tratado médico de 1552 fue localizado en los archivos de la Biblioteca Vaticana en 1929."
            }
        ]
    },

    "b1-civilizaciones-05-legado.json": {
        "id": "story.b1.civilizaciones.05",
        "title": "Un legado vivo",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The enduring living legacy of pre-Columbian civilizations: loanwords in global languages, food sovereignty, and contemporary indigenous rights.",
        "characters": [],
        "location": "América Latina contemporánea",
        "grammar": ["conectores y síntesis"],
        "vocabularyTopics": ["Un legado vivo"],
        "paragraphs": [
            {"type": "narration", "text": "Las civilizaciones precolombinas a menudo se describen como mundos lejanos y extintos, pertenecientes a vitrinas de museo o a ruinas arqueológicas cubiertas por la selva. Sin embargo, su legado no es una reliquia del pasado: sigue vivo y palpitante en el lenguaje, la alimentación, la cosmovisión y la identidad de millones de personas en todo el planeta."},
            {"type": "narration", "text": "El impacto lingüístico de los idiomas originarios en el español y en las lenguas globales es inmenso. El náhuatl aportó vocablos cotidianos como chocolate, tomate, aguacate, cacahuate y coyote. Del quechua adoptamos términos indispensables como cancha, cóndor, pampa, puma y papa. Estas palabras viajaron por todos los continentes, transformando para siempre el vocabulario universal."},
            {"type": "narration", "text": "En la agricultura mundial, la contribución americana fue revolucionaria. Más del sesenta por ciento de los cultivos consumidos hoy en el mundo —incluidos el maíz, la papa, el tomate, la calabaza, el chile, el frijol, el cacao y la mandioca— fueron domesticados y perfeccionados por agricultores indígenas durante milenios. Cuando la papa llegó a Europa, salvó a poblaciones enteras de las hambrunas periódicas, convirtiéndose en el sustento básico de naciones enteras como Irlanda, Polonia y Alemania."},
            {"type": "narration", "text": "En el plano social y político contemporáneo, los pueblos originarios continúan librando una lucha incansable por el reconocimiento de sus derechos colectivos, sus tierras ancestrales y su autonomía cultural. En países como Guatemala, Bolivia, Perú, México y Ecuador, las lenguas indígenas cuentan hoy con estatus oficial y se enseñan en escuelas bilingües."},
            {"type": "narration", "text": "La memoria de los mayas, mexicas e incas no reside únicamente en sus colosales pirámides de piedra o en sus tesoros de oro y jade. Vive en las manos de las tejedoras que conservan patrones milenarios, en los campesinos que cultivan semillas ancestrales y en las voces de millones de hablantes que demuestran que las raíces profundas de América siguen floreciendo en el presente."}
        ],
        "keyVocab": [
            {"lemma": "extinto", "pos": "adjective", "cefr": "B1", "gloss": "extinct"},
            {"lemma": "el vocablo", "pos": "noun", "cefr": "B1", "gloss": "word, term"},
            {"lemma": "la cosmovisión", "pos": "noun", "cefr": "B1", "gloss": "worldview"},
            {"lemma": "el sustento", "pos": "noun", "cefr": "B1", "gloss": "sustenance"},
            {"lemma": "ancestral", "pos": "adjective", "cefr": "B1", "gloss": "ancestral"},
            {"lemma": "la autonomía", "pos": "noun", "cefr": "B1", "gloss": "autonomy"},
            {"lemma": "bilingüe", "pos": "adjective", "cefr": "B1", "gloss": "bilingual"},
            {"lemma": "el milenio", "pos": "noun", "cefr": "B1", "gloss": "millennium"}
        ],
        "compQuestions": [
            {
                "question": "¿De qué lengua indígena provienen palabras como «cancha», «cóndor» y «pampa»?",
                "options": [
                    "Del quechua.",
                    "Del náhuatl.",
                    "Del maya."
                ],
                "correctIndex": 0,
                "explanation": "Términos como cancha, cóndor, pampa y puma son préstamos directos del idioma quechua andino."
            }
        ]
    },

    # =========================================================================
    # UNIT 03: llegadaeuropeos (The Arrival of the Europeans)
    # =========================================================================
    "b1-llegadaeuropeos-01-viajecolon.json": {
        "id": "story.b1.llegadaeuropeos.01",
        "title": "El viaje de Colón",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The 1492 transatlantic voyage: Isabella's sponsorship after Granada, near-mutiny at sea, Rodrigo de Triana's sighting of land, and Amerigo Vespucci's naming of America.",
        "characters": [],
        "location": "Océano Atlántico y Guanahaní",
        "grammar": ["pretérito indefinido y conectores temporales"],
        "vocabularyTopics": ["El viaje de Colón"],
        "paragraphs": [
            {"type": "narration", "text": "Durante años, el navegante genovés Cristóbal Colón intentó sin éxito convencer a las cortes de Portugal, Inglaterra y Francia de que era posible llegar a las ricas costas de Asia navegando hacia el oeste. Todos los monarcas rechazaron su proyecto por considerarlo descabellado o mal calculado."},
            {"type": "narration", "text": "Sin embargo, en 1492 el panorama político cambió radicalmente. Tras diez años de guerra, los Reyes Católicos completaron la Reconquista con la toma del reino nazarí de Granada. Pocos meses después de esta victoria histórica, la reina Isabel de Castilla aceptó financiar la expedición de Colón, firmando las Capitulaciones de Santa Fe."},
            {"type": "narration", "text": "Cristóbal Colón partió del puerto de Palos de la Frontera el 3 de agosto de 1492 con tres barcos: la Santa María, la Pinta y la Niña. Tras hacer escala en las islas Canarias para reparar averías y cargar provisiones, las carabelas se adentraron en la inmensidad del océano Atlántico."},
            {"type": "narration", "text": "A medida que pasaban las semanas sin ver tierra, la tripulación comenzó a desesperarse. La comida escaseaba, el agua se pudría en los barriles y el temor a no poder regresar desató rumores de motín entre los marineros. Colón tuvo que recurrir a promesas y engaños para mantener el control."},
            {"type": "narration", "text": "Por fin, en la madrugada del 12 de octubre, un marinero de la Pinta llamado Rodrigo de Triana avistó tierra por primera vez. Aunque los reyes habían prometido una generosa recompensa económica vitalicia al primero que viera tierra, Colón reclamó la recompensa para sí mismo, alegando haber visto una luz horas antes."},
            {"type": "narration", "text": "Al amanecer, Colón y sus capitanes decidieron desembarcar en una pequeña isla del archipiélago de las Bahamas, llamada Guanahaní por sus habitantes taínos. Colón tomó posesión de la tierra en nombre de Castilla y procedió a bautizar la isla con el nombre de San Salvador, convencido erróneamente de que había alcanzado las islas de las Indias orientales."},
            {"type": "narration", "text": "Colón murió en 1506 sin admitir jamás que no había llegado a Asia. En 1507, un cartógrafo alemán llamado Martin Waldseemüller publicó un mapa que bautizó el nuevo continente con el nombre de «América», en honor al navegante florentino Américo Vespucio, quien fue el primero en demostrar por escrito que aquellas tierras constituían un continente completamente nuevo."}
        ],
        "keyVocab": [
            {"lemma": "financiar", "pos": "verb", "cefr": "B1", "gloss": "to finance"},
            {"lemma": "rechazar", "pos": "verb", "cefr": "B1", "gloss": "to reject"},
            {"lemma": "la tripulación", "pos": "noun", "cefr": "B1", "gloss": "crew"},
            {"lemma": "el motín", "pos": "noun", "cefr": "B1", "gloss": "mutiny"},
            {"lemma": "avistar", "pos": "verb", "cefr": "B1", "gloss": "to sight, spot"},
            {"lemma": "la recompensa", "pos": "noun", "cefr": "B1", "gloss": "reward"},
            {"lemma": "desembarcar", "pos": "verb", "cefr": "B1", "gloss": "to disembark, land"},
            {"lemma": "bautizar", "pos": "verb", "cefr": "B1", "gloss": "to baptize, name"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué el continente fue llamado «América» y no «Colombia»?",
                "options": [
                    "Porque el cartógrafo Waldseemüller lo nombró en honor a Américo Vespucio.",
                    "Porque los reyes de España eligieron ese nombre en su testamento.",
                    "Porque era el nombre indígena original de las islas del Caribe."
                ],
                "correctIndex": 0,
                "explanation": "Américo Vespucio argumentó que se trataba de un «Mundus Novus», y el cartógrafo Waldseemüller rotuló América en su mapa de 1507."
            }
        ]
    },

    "b1-llegadaeuropeos-02-encuentro.json": {
        "id": "story.b1.llegadaeuropeos.02",
        "title": "El encuentro",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "First contact with the Taíno: the breakdown of hospitality, the gold tribute, the encomienda labor system, and disease devastation.",
        "characters": [],
        "location": "Las Antillas (La Española, Guanahaní)",
        "grammar": ["conectores de contraste y simultaneidad"],
        "vocabularyTopics": ["El encuentro"],
        "paragraphs": [
            {"type": "narration", "text": "Al desembarcar en las playas caribeñas en octubre de 1492, los navegantes europeos entraron en contacto con el pueblo taíno, una sociedad pacífica de agricultores y pescadores que habitaba las islas de las Antillas Mayores."},
            {"type": "narration", "text": "Al principio, el encuentro fue relativamente pacífico. Sin embargo, esa primera impresión cambió con rapidez. Los taínos recibieron a los extranjeros con generosidad y hospitalidad, ofreciéndoles alimentos frescos, loros y ovillos de algodón mediante un amistoso intercambio por cuentas de vidrio y cascabeles de latón."},
            {"type": "narration", "text": "Pero la curiosidad inicial pronto dio paso a la codicia. Mientras los españoles buscaban oro, empezaron a exigir a los taínos que entregaran una cantidad fija de metal precioso cada tres meses. Aquellos que no cumplían con la cuota obligatoria eran castigados con extrema crueldad, incluyendo la mutilación de manos."},
            {"type": "narration", "text": "Al mismo tiempo, se estableció un sistema conocido como encomienda. Oficialmente, la corona española otorgaba a cada colono un grupo de indígenas para brindarles supuesta protección y educación religiosa. En la práctica, la encomienda funcionaba como un sistema despiadado de explotación que exigía mano de obra forzada en minas de oro y plantaciones agrícolas."},
            {"type": "narration", "text": "Después llegó un factor todavía más devastador que la violencia directa: las enfermedades europeas. Virus y bacterias como la viruela, el sarampión y la gripe cruzaron el océano en los cuerpos de los colonizadores. La población indígena no tenía defensas inmunológicas contra estos patógenos desconocidos. En cuestión de pocas décadas, la población taína de La Española llegó a reducirse en más de un noventa por ciento."},
            {"type": "narration", "text": "Tras presenciar estas atrocidades de primera mano como colono en La Española y Cuba, Bartolomé de las Casas tomó una decisión radical. Renunció a sus encomiendas, se ordenó fraile dominico y dedicó el resto de su larga vida a denunciar los abusos de los conquistadores ante la corte real, publicando en 1552 su célebre Brevísima relación de la destrucción de las Indias."}
        ],
        "keyVocab": [
            {"lemma": "el intercambio", "pos": "noun", "cefr": "B1", "gloss": "exchange"},
            {"lemma": "la hospitalidad", "pos": "noun", "cefr": "B1", "gloss": "hospitality"},
            {"lemma": "castigar", "pos": "verb", "cefr": "B1", "gloss": "to punish"},
            {"lemma": "la mano de obra", "pos": "noun", "cefr": "B1", "gloss": "workforce, labor"},
            {"lemma": "la viruela", "pos": "noun", "cefr": "B1", "gloss": "smallpox"},
            {"lemma": "reducirse", "pos": "verb", "cefr": "B1", "gloss": "to shrink, diminish"},
            {"lemma": "presenciar", "pos": "verb", "cefr": "B1", "gloss": "to witness"},
            {"lemma": "denunciar", "pos": "verb", "cefr": "B1", "gloss": "to denounce, report"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué factor causó la caída demográfica más devastadora entre los taínos?",
                "options": [
                    "Las epidemias de enfermedades europeas como la viruela.",
                    "La escasez natural de alimentos en las islas.",
                    "Guerras internas entre diferentes cacicazgos taínos."
                ],
                "correctIndex": 0,
                "explanation": "La falta de inmunidad biológica frente a la viruela y el sarampión provocó un colapso demográfico masivo."
            }
        ]
    },

    "b1-llegadaeuropeos-03-resistencia.json": {
        "id": "story.b1.llegadaeuropeos.03",
        "title": "Conquista y resistencia",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Indigenous resistance in the Caribbean: Hatuey's warning in Cuba, his execution, and Enriquillo's fourteen-year guerrilla revolt in Hispaniola.",
        "characters": [],
        "location": "Cuba y La Española (Bahoruco)",
        "grammar": ["se pasiva en episodios históricos"],
        "vocabularyTopics": ["Conquista y resistencia"],
        "paragraphs": [
            {"type": "narration", "text": "Frente a la brutalidad de la colonización, los pueblos caribeños no se resignaron pasivamente. Desde los primeros momentos, líderes indígenas organizaron rebeliones armadas y tácticas guerrilleras para defender su territorio y su libertad."},
            {"type": "narration", "text": "Uno de los primeros símbolos de esta lucha fue Hatuey, un valiente cacique taíno de La Española. Al ver cómo se maltrataba a su pueblo, Hatuey huyó a Cuba con un grupo de seguidores en varias canoas. Su misión era advertir a los habitantes de la isla vecina sobre la crueldad de los conquistadores y convencerlos de resistir."},
            {"type": "narration", "text": "Allí se organizó una resistencia armada contra los españoles comandados por Diego Velázquez. Utilizando tácticas de emboscada en la espesura de los bosques, los guerreros de Hatuey hostigaron a los colonizadores durante meses. Finalmente, Hatuey fue capturado tras una traición y condenado a morir en la hoguera en 1512."},
            {"type": "narration", "text": "Antes de encender el fuego, un fraile franciscano le ofreció bautizarse para salvar su alma e ir al cielo. Se cuenta que Hatuey preguntó si los españoles también iban a ese cielo; al responderle el fraile que sí, el cacique replicó sin dudar que prefería ir al infierno antes que compartir la eternidad con hombres tan despiadados."},
            {"type": "narration", "text": "Años más tarde, en las escarpadas montañas de Bahoruco en La Española, surgió otra resistencia extraordinaria liderada por el cacique Enriquillo. Educado por frailes franciscanos, Enriquillo decidió rebelarse en 1519 tras sufrir graves abusos por parte de un encomendero."},
            {"type": "narration", "text": "Enriquillo se refugió en la sierra con cientos de guerreros y sus familias. Durante catorce años, el ejército español intentó aplastar su movimiento, pero los rebeldes derrotaron todas las expediciones militares gracias a su conocimiento del terreno."},
            {"type": "narration", "text": "Incapaz de vencerlo por las armas, la corona española tuvo que capitular. En 1533 se firmó un acuerdo de paz que reconocía la libertad de Enriquillo y de su gente, otorgándoles tierras autónomas libres de encomienda y tributo."}
        ],
        "keyVocab": [
            {"lemma": "el cacique", "pos": "noun", "cefr": "B1", "gloss": "indigenous chieftain"},
            {"lemma": "huir", "pos": "verb", "cefr": "B1", "gloss": "to flee"},
            {"lemma": "advertir", "pos": "verb", "cefr": "B1", "gloss": "to warn"},
            {"lemma": "capturar", "pos": "verb", "cefr": "B1", "gloss": "to capture"},
            {"lemma": "la hoguera", "pos": "noun", "cefr": "B1", "gloss": "bonfire, stake"},
            {"lemma": "rebelarse", "pos": "verb", "cefr": "B1", "gloss": "to rebel"},
            {"lemma": "refugiarse", "pos": "verb", "cefr": "B1", "gloss": "to take refuge"},
            {"lemma": "aplastar", "pos": "verb", "cefr": "B1", "gloss": "to crush, suppress"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué logro excepcional consiguió el cacique Enriquillo en La Española?",
                "options": [
                    "Obligó a la corona española a firmar un tratado de paz que reconocía su libertad.",
                    "Expulsó a todos los colonizadores de la isla para siempre.",
                    "Viajó a Madrid para ser nombrado virrey del Caribe."
                ],
                "correctIndex": 0,
                "explanation": "Tras 14 años de resistencia guerrillera en Bahoruco, la corona firmó un tratado de paz con Enriquillo en 1533."
            }
        ]
    },

    "b1-llegadaeuropeos-04-nuevosmundos.json": {
        "id": "story.b1.llegadaeuropeos.04",
        "title": "Nuevos mundos",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Columbian Exchange: ecological and biological transfers, transatlantic slave trade origins, and the global climate impact hypothesis.",
        "characters": [],
        "location": "El Atlántico global",
        "grammar": ["conectores de causa y consecuencia"],
        "vocabularyTopics": ["Nuevos mundos"],
        "paragraphs": [
            {"type": "narration", "text": "El contacto transatlántico desató una gigantesca transferencia biológica, ecológica y cultural que los historiadores denominan el «Intercambio Colombino». Especies vegetales, animales y microorganismos que habían evolucionado aislados durante millones de años cruzaron el océano en ambas direcciones, transformando la faz del planeta."},
            {"type": "narration", "text": "Hacia el este viajaron alimentos americanos fundamentales: el maíz, la papa, el tomate, el cacao, la mandioca, el tabaco y el pimiento. En sentido contrario, los europeos introdujeron en América el trigo, la caña de azúcar, el café, la vid y animales domesticados como el caballo, la vaca, el cerdo y la oveja. El caballo, que se había extinguido en el continente antes de la llegada de los europeos, transformó profundamente la forma de cazar y desplazarse de pueblos indígenas en las llanuras de Norteamérica y las pampas sudamericanas."},
            {"type": "narration", "text": "Sin embargo, este intercambio tuvo consecuencias humanas desastrosas. El cultivo masivo de la caña de azúcar en las islas del Caribe exigía enormes contingentes de mano de obra. Debido a que la población indígena del Caribe ya se había reducido drásticamente por el maltrato y las enfermedades, los colonos recurrieron al tráfico de personas esclavizadas desde África."},
            {"type": "narration", "text": "Por eso, muchos historiadores consideran la caña de azúcar uno de los motores principales detrás del comercio transatlántico de esclavos, un crimen histórico que desplazó forzosamente a más de doce millones de africanos hacia las Américas."},
            {"type": "narration", "text": "El impacto biológico más devastador fue el de los virus euroasiáticos. La población indígena no tenía ninguna inmunidad, ya que estos patógenos habían evolucionado junto a los animales domesticados de Eurasia durante miles de años."},
            {"type": "narration", "text": "Como resultado de esta catástrofe demográfica, millones de hectáreas de tierras de cultivo volvieron a cubrirse de bosque y vegetación salvaje. Investigadores recientes sugieren que esta masiva reforestación absorbió cantidades descomunales de dióxido de carbono de la atmósfera, contribuyendo potencialmente a un enfriamiento del clima global conocido como la Pequeña Edad de Hielo."}
        ],
        "keyVocab": [
            {"lemma": "desatar", "pos": "verb", "cefr": "B1", "gloss": "to unleash"},
            {"lemma": "extinguirse", "pos": "verb", "cefr": "B1", "gloss": "to become extinct"},
            {"lemma": "desplazarse", "pos": "verb", "cefr": "B1", "gloss": "to move, travel"},
            {"lemma": "duradero", "pos": "adjective", "cefr": "B1", "gloss": "lasting, durable"},
            {"lemma": "el patógeno", "pos": "noun", "cefr": "B1", "gloss": "pathogen"},
            {"lemma": "la catástrofe", "pos": "noun", "cefr": "B1", "gloss": "catastrophe"},
            {"lemma": "la hectárea", "pos": "noun", "cefr": "B1", "gloss": "hectare"},
            {"lemma": "absorber", "pos": "verb", "cefr": "B1", "gloss": "to absorb"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué los colonos europeos recurrieron al tráfico de esclavos africanos en el Caribe?",
                "options": [
                    "Porque la población indígena local había sufrido un colapso demográfico drástico.",
                    "Porque las leyes españolas prohibían utilizar mano de obra indígena en la agricultura.",
                    "Porque los esclavos africanos ya conocían las rutas comerciales del Caribe."
                ],
                "correctIndex": 0,
                "explanation": "La caída de la población taína llevó a los colonos a importar mano de obra africana esclavizada para los ingenios azucareros."
            }
        ]
    },

    "b1-llegadaeuropeos-05-transformacion.json": {
        "id": "story.b1.llegadaeuropeos.05",
        "title": "Una transformación histórica",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Contested interpretations of 1492: 'discovery' versus 'invasion', demography debates, and the syncretism of the Virgin of Guadalupe.",
        "characters": [],
        "location": "América Latina",
        "grammar": ["oraciones de relativo explicativas"],
        "vocabularyTopics": ["Una transformación histórica"],
        "paragraphs": [
            {"type": "narration", "text": "Más de cinco siglos después del desembarco de Colón, los acontecimientos de 1492 continúan siendo objeto de intensos debates historiográficos, filosóficos y éticos. La forma en que narramos y nombramos estos hechos revela nuestras propias perspectivas sobre el pasado y el presente."},
            {"type": "narration", "text": "Durante siglos se habló de 'descubrimiento', una palabra que asumía que América no existía realmente hasta que Europa la encontró. Con motivo del quinto centenario en 1992, se propuso la expresión «encuentro de dos mundos», buscando un tono más neutral. Sin embargo, movimientos indígenas y pensadores críticos prefieren términos como «invasión», «conquista» o «inicio del colonialismo», enfatizando el despojo y la violencia que sufrieron los pueblos originarios."},
            {"type": "narration", "text": "Otro debate fundamental reside en la demografía precolombina. Los primeros cálculos fueron publicados por historiadores a quienes hoy se llama 'contadores bajos', quienes estimaban que en 1492 vivían apenas entre ocho y quince millones de personas en todo el continente."},
            {"type": "narration", "text": "Investigaciones posteriores, cuyos autores revisaron fuentes coloniales con más detalle y aplicaron modelos ecológicos, elevaron esa cifra a cien millones de habitantes en toda América. Esta enorme diferencia numérica transforma por completo nuestra comprensión de la magnitud del colapso demográfico posterior."},
            {"type": "narration", "text": "En el plano cultural y espiritual, la transformación dio origen a un complejo sincretismo religioso en el que símbolos cristianos se fusionaron con devociones autóctonas. Un ejemplo célebre es la Virgen de Guadalupe, cuya aparición se sitúa en 1531 en el cerro del Tepeyac, un santuario que antes de la conquista estaba dedicado a Tonantzin, la diosa madre mexica de la fertilidad y la tierra."},
            {"type": "narration", "text": "El 1492 no fue solo una fecha en el calendario: fue el catalizador de una transformación global irreversible que dio nacimiento al mundo moderno, un proceso contradictorio forjado tanto en la tragedia y la resistencia como en el nacimiento de identidades mestizas."}
        ],
        "keyVocab": [
            {"lemma": "el consenso", "pos": "noun", "cefr": "B1", "gloss": "consensus"},
            {"lemma": "el desacuerdo", "pos": "noun", "cefr": "B1", "gloss": "disagreement"},
            {"lemma": "el cálculo", "pos": "noun", "cefr": "B1", "gloss": "calculation, estimate"},
            {"lemma": "elevar", "pos": "verb", "cefr": "B1", "gloss": "to raise, increase"},
            {"lemma": "mestizo", "pos": "adjective", "cefr": "B1", "gloss": "mestizo (mixed heritage)"},
            {"lemma": "la aparición", "pos": "noun", "cefr": "B1", "gloss": "apparition"},
            {"lemma": "sagrado", "pos": "adjective", "cefr": "B1", "gloss": "sacred"},
            {"lemma": "la devoción", "pos": "noun", "cefr": "B1", "gloss": "devotion"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué la Virgen de Guadalupe es considerada un ejemplo de sincretismo religioso?",
                "options": [
                    "Porque su santuario en el Tepeyac se ubicó en un antiguo lugar de culto a la diosa mexica Tonantzin.",
                    "Porque fue pintada por frailes españoles en Roma.",
                    "Porque representa exclusivamente a los reyes de España."
                ],
                "correctIndex": 0,
                "explanation": "El culto guadalupano en el Tepeyac integró tradiciones y espacios sagrados de la devoción prehispánica a Tonantzin."
            }
        ]
    },

    # =========================================================================
    # UNIT 04: conquista (The Conquest)
    # =========================================================================
    "b1-conquista-01-mexico.json": {
        "id": "story.b1.conquista.01",
        "title": "La conquista de México",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The fall of Tenochtitlan: Cortés's scuttling of ships, the Tlaxcala alliance, the Noche Triste, smallpox epidemic, and the two-year siege.",
        "characters": [],
        "location": "Valle de México (Tenochtitlan, Tlaxcala)",
        "grammar": ["voz pasiva en acontecimientos decisivos"],
        "vocabularyTopics": ["La conquista de México"],
        "paragraphs": [
            {"type": "narration", "text": "En febrero de 1519, Hernán Cortés desembarcó en la costa mexicana de Veracruz con once barcos, unos quinientos soldados y dieciséis caballos. Para impedir que sus hombres desertaran o conspiraran para regresar a Cuba, Cortés mandó inutilizar deliberadamente sus naves encallándolas en la arena, un hecho que la leyenda popular transformó erróneamente en «la quema de las naves»."},
            {"type": "narration", "text": "Consciente de que no podía vencer al imperio mexica en solitario, Cortés buscó aliados entre los pueblos sometidos por Tenochtitlan. El pacto más decisivo fue con el señorío de Tlaxcala, un estado guerrero independiente que llevaba décadas resistiendo el cerco mexica. Miles de guerreros tlaxcaltecas se unieron a las fuerzas españolas."},
            {"type": "narration", "text": "El 8 de noviembre de 1519, Cortés fue recibido pacíficamente por el emperador Moctezuma II en las calzadas de Tenochtitlan. A pesar de los regalos y la hospitalidad inicial, Moctezuma poco después fue tomado como rehén dentro de su propio palacio por los españoles."},
            {"type": "narration", "text": "La convivencia se deterioró rápidamente. En mayo de 1520, una masacre de nobles mexicas en el Templo Mayor desató una furiosa insurrección popular. Moctezuma murió en circunstancias confusas, y en la noche del 30 de junio (la Noche Triste), los españoles fueron expulsados violentamente de la ciudad, sufriendo enormes pérdidas."},
            {"type": "narration", "text": "Cortés se refugió en Tlaxcala para reorganizar su ejército y construir trece bergantines armados para sitiar la ciudad por agua. Mientras tanto, un enemigo invisible y letal atacó a los mexicas: una devastadora epidemia de viruela se propagó por Tenochtitlan, matando a miles de defensores y al nuevo tlatoani Cuitláhuac tras solo ochenta días en el trono."},
            {"type": "narration", "text": "Bajo el mando del joven Cuauhtémoc, los mexicas resistieron heroicamente un asedio de noventa y tres días. Los españoles cortaron los acueductos de agua dulce y bloquearon todo suministro de alimentos. Tras combates feroces casa por casa, Tenochtitlan finalmente fue conquistada el 13 de agosto de 1521."}
        ],
        "keyVocab": [
            {"lemma": "inutilizar", "pos": "verb", "cefr": "B1", "gloss": "to disable, scuttle"},
            {"lemma": "el aliado", "pos": "noun", "cefr": "B1", "gloss": "ally"},
            {"lemma": "el rehén", "pos": "noun", "cefr": "B1", "gloss": "hostage"},
            {"lemma": "deteriorarse", "pos": "verb", "cefr": "B1", "gloss": "to deteriorate"},
            {"lemma": "expulsar", "pos": "verb", "cefr": "B1", "gloss": "to expel"},
            {"lemma": "el asedio", "pos": "noun", "cefr": "B1", "gloss": "siege"},
            {"lemma": "el suministro", "pos": "noun", "cefr": "B1", "gloss": "supply"},
            {"lemma": "conspirar", "pos": "verb", "cefr": "B1", "gloss": "to conspire"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué factor biológico debilitó fatalmente a los defensores de Tenochtitlan durante el asedio?",
                "options": [
                    "Una epidemia de viruela que mató al emperador Cuitláhuac y a miles de guerreros.",
                    "La peste negra traída desde Asia.",
                    "Una sequía que secó completamente el lago de Texcoco."
                ],
                "correctIndex": 0,
                "explanation": "La viruela diezmó a la población y a los líderes mexicas en plena defensa de la ciudad."
            }
        ]
    },

    "b1-conquista-02-peru.json": {
        "id": "story.b1.conquista.02",
        "title": "La conquista del Perú",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Pizarro's conquest of the Inca: the civil war, the Cajamarca ambush, Atahualpa's ransom room, his execution, and the Vilcabamba resistance.",
        "characters": [],
        "location": "Los Andes (Cajamarca, Cuzco, Vilcabamba)",
        "grammar": ["se pasiva en episodios históricos"],
        "vocabularyTopics": ["La conquista del Perú"],
        "paragraphs": [
            {"type": "narration", "text": "En 1532, Francisco Pizarro desembarcó en la costa peruana con menos de doscientos soldados. El momento no podía ser más favorable para los invasores: el inmenso imperio del Tawantinsuyu se encontraba dividido y desangrado por una cruenta guerra civil entre dos hermanos herederos, Huáscar y Atahualpa, quienes se disputaban el trono tras la muerte repentina del emperador Huayna Cápac por viruela."},
            {"type": "narration", "text": "Atahualpa acababa de derrotar a su hermano cuando aceptó reunirse con los extranjeros en la ciudad andina de Cajamarca. El 16 de noviembre de 1532, en Cajamarca, se organizó un encuentro entre Atahualpa y los españoles. Confiado en la superioridad numérica de sus miles de guardias desarmados, el Inca entró en la plaza principal."},
            {"type": "narration", "text": "Tras un breve altercado con el fraile Vicente de Valverde sobre un breviario religioso que sirvió de pretexto, los españoles abrieron fuego con cañones y arcabuces ocultos. En cuestión de horas, se masacró a miles de soldados incas y Atahualpa fue capturado con vida."},
            {"type": "narration", "text": "Para obtener su libertad, el Inca ofreció a Pizarro un rescate fabuloso: llenar una gran habitación de oro hasta donde alcanzara su mano y dos veces más de plata. Durante meses se recolectó ese rescate desde templos y palacios de todo el imperio. Sin embargo, tras fundir y repartir el tesoro, Pizarro decidió ejecutar a Atahualpa en julio de 1533 bajo falsos cargos de traición. Para evitar la hoguera, el Inca aceptó bautizarse antes de morir a garrote vil."},
            {"type": "narration", "text": "Los españoles marcharon hacia Cuzco e instalaron a Manco Inca como gobernante títere. No obstante, al comprender las verdaderas intenciones de los colonizadores, Manco Inca escapó en 1536 y lideró una masiva rebelión que llegó a sitiar Cuzco y Lima."},
            {"type": "narration", "text": "Aunque no logró expulsar a los españoles, Manco Inca se retiró a la selva montañosa y fundó el reino rebelde de Vilcabamba. En Vilcabamba se mantuvo una resistencia inca continua durante casi cuarenta años más, hasta que en 1572 el virrey Francisco de Toledo ordenó capturar y ejecutar al último soberano inca, Túpac Amaru I."}
        ],
        "keyVocab": [
            {"lemma": "disputarse", "pos": "verb", "cefr": "B1", "gloss": "to dispute, contest"},
            {"lemma": "el pretexto", "pos": "noun", "cefr": "B1", "gloss": "pretext"},
            {"lemma": "masacrar", "pos": "verb", "cefr": "B1", "gloss": "to massacre"},
            {"lemma": "el rescate", "pos": "noun", "cefr": "B1", "gloss": "ransom"},
            {"lemma": "recolectar", "pos": "verb", "cefr": "B1", "gloss": "to collect"},
            {"lemma": "bautizarse", "pos": "verb", "cefr": "B1", "gloss": "to be baptized"},
            {"lemma": "el títere", "pos": "noun", "cefr": "B1", "gloss": "puppet"},
            {"lemma": "sitiar", "pos": "verb", "cefr": "B1", "gloss": "to besiege"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué ocurrió con la resistencia inca tras la muerte de Atahualpa en 1533?",
                "options": [
                    "Continuó durante casi cuarenta años más desde el reino rebelde de Vilcabamba.",
                    "Terminó por completo de forma inmediata.",
                    "Se trasladó pacíficamente a la costa de Chile."
                ],
                "correctIndex": 0,
                "explanation": "Manco Inca y sus sucesores mantuvieron el estado neoinca de Vilcabamba hasta 1572."
            }
        ]
    },

    "b1-conquista-03-alianzas.json": {
        "id": "story.b1.conquista.03",
        "title": "Alianzas y conflictos",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Indigenous participation in the conquest: the overwhelming numeric dominance of native allies, Malintzin's strategic role, and Tlaxcalan privileges.",
        "characters": [],
        "location": "Mesoamérica y los Andes",
        "grammar": ["gerundio para caracterizar acciones"],
        "vocabularyTopics": ["Alianzas y conflictos"],
        "paragraphs": [
            {"type": "narration", "text": "Uno de los mayores mitos de la historia colonial es que un puñado de soldados españoles conquistó imperios de millones de personas únicamente con su valor y su tecnología militar. En realidad, las conquistas de México y Perú fueron gigantescas guerras civiles indígenas en las que los españoles actuaron como catalizadores de conflictos políticos preexistentes."},
            {"type": "narration", "text": "En el asedio de Tenochtitlan, por cada soldado español combatían entre cincuenta y cien guerreros indígenas aliados de Tlaxcala, Texcoco, Totonacapan y Chalco. Los pueblos aliados superaban ampliamente a los españoles y aportaron alimentos, canoas, cargadores y conocimiento militar indispensable."},
            {"type": "narration", "text": "En este escenario de alianzas complejas destacó la figura de Malintzin (conocida como La Malinche o Doña Marina). Nacida en una familia noble nahua y vendida como esclava a señores mayas en Tabasco, fue entregada a Cortés en 1519. Aprendiendo español con sorprendente rapidez, se convirtió en la intérprete y asesora estratégica de Cortés."},
            {"type": "narration", "text": "Malintzin comprendía a la perfección la diplomacia y las rivalidades mesoamericanas. Durante siglos fue tachada injustamente de traición por el nacionalismo moderno, pero historiadores actuales señalan que, sobreviviendo en circunstancias imposibles, tomó decisiones dentro de un margen de maniobra extremadamente limitado para proteger su vida y mediar entre dos mundos."},
            {"type": "narration", "text": "Tras la caída de Tenochtitlan, los líderes de Tlaxcala hicieron valer su condición de vencedores. Reconociendo su contribución decisiva, la corona española concedió a Tlaxcala un estatus especial que la eximió de la encomienda y le permitió conservar su propio gobierno indígena y sus tierras durante siglos."},
            {"type": "narration", "text": "En los Andes ocurrió un fenómeno similar. Pueblos como los huancas, cañaris y chachapoyas estaban profundamente resentidos por la dominación incaica y las políticas de reubicación forzada. Por ello, apoyaron activamente a los españoles esperando obtener mayor autonomía a cambio, redefiniendo el rumbo de la conquista."}
        ],
        "keyVocab": [
            {"lemma": "superar", "pos": "verb", "cefr": "B1", "gloss": "to exceed, surpass"},
            {"lemma": "el tributo", "pos": "noun", "cefr": "B1", "gloss": "tribute"},
            {"lemma": "la traición", "pos": "noun", "cefr": "B1", "gloss": "treason, betrayal"},
            {"lemma": "el margen de maniobra", "pos": "noun", "cefr": "B1", "gloss": "leeway, room for maneuver"},
            {"lemma": "conceder", "pos": "verb", "cefr": "B1", "gloss": "to grant"},
            {"lemma": "eximir", "pos": "verb", "cefr": "B1", "gloss": "to exempt"},
            {"lemma": "resentido", "pos": "adjective", "cefr": "B1", "gloss": "resentful"},
            {"lemma": "la reubicación", "pos": "noun", "cefr": "B1", "gloss": "relocation"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué recompensa obtuvo Tlaxcala por su alianza con los españoles?",
                "options": [
                    "Un estatus especial con exención de encomiendas y autogobierno indígena.",
                    "El control absoluto de todas las minas de plata de México.",
                    "La independencia total fuera del imperio español."
                ],
                "correctIndex": 0,
                "explanation": "Tlaxcala negoció privilegios legales duraderos que la eximieron del pago de tributos ordinarios y encomiendas."
            }
        ]
    },

    "b1-conquista-04-violenciaypoder.json": {
        "id": "story.b1.conquista.04",
        "title": "Violencia y poder",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Instruments of conquest: calculated terror at Cholula, the legal fiction of the Requerimiento, and tactical adaptation by indigenous armies.",
        "characters": [],
        "location": "Cholula, Cajamarca y campos de batalla",
        "grammar": ["conectores de causa y consecuencia formal"],
        "vocabularyTopics": ["Violencia y poder"],
        "paragraphs": [
            {"type": "narration", "text": "La conquista de América no fue solo un choque militar, sino una combinación deliberada de violencia ejemplarizante, mecanismos jurídicos de dominación y una rápida adaptación táctica por ambas partes."},
            {"type": "narration", "text": "Uno de los episodios más polémicos fue la masacre de Cholula en octubre de 1519. Al llegar a esta ciudad sagrada, Cortés sospechó de una emboscada secreta preparada por los mexicas. Para advertir e intimidar a toda la región, los españoles y tlaxcaltecas cerraron las salidas de la plaza mayor y masacraron a miles de nobles y civiles desarmados en pocas horas."},
            {"type": "narration", "text": "Junto a la fuerza de las armas, la corona española empleó sofisticados instrumentos jurídicos para legitimar la conquista. El más célebre fue el Requerimiento de 1513, un texto legal que se leía a las comunidades indígenas exigiéndoles someterse pacíficamente al papa y a los reyes de Castilla. Puesto que técnicamente se le había 'ofrecido' la oportunidad de someterse, cualquier resistencia posterior se consideraba una rebelión ilegítima que justificaba la guerra justa y la esclavitud de los prisioneros, a pesar de que el documento solía leerse en latín o español sin que nadie pudiera entenderlo."},
            {"type": "narration", "text": "En cuanto a la superioridad militar española, suele exagerarse en los relatos tradicionales. Aunque las armas de fuego, las espadas de acero toledano y los caballos causaron un impacto psicológico inicial inmenso, su eficacia tenía límites severos en selvas densas y montañas escarpadas."},
            {"type": "narration", "text": "Ya que los ejércitos indígenas aprendían rápido, en cuestión de pocas batallas desarrollaron tácticas específicas contra los jinetes: excavaban fosos profundos con estacas afiladas ocultas bajo la hierba para quebrar las patas de los caballos, y usaban lazos de cuerda (boleadoras) y largas picas de madera endurecida al fuego para derribar a los caballeros."},
            {"type": "narration", "text": "Por consiguiente, entender la conquista únicamente como tecnología superior es una simplificación; fue ante todo un proceso político complejo sostenido por la violencia, las divisiones indígenas y el impacto devastador de las epidemias."}
        ],
        "keyVocab": [
            {"lemma": "la emboscada", "pos": "noun", "cefr": "B1", "gloss": "ambush"},
            {"lemma": "advertir", "pos": "verb", "cefr": "B1", "gloss": "to warn"},
            {"lemma": "intimidar", "pos": "verb", "cefr": "B1", "gloss": "to intimidate"},
            {"lemma": "someterse", "pos": "verb", "cefr": "B1", "gloss": "to submit, surrender"},
            {"lemma": "legitimar", "pos": "verb", "cefr": "B1", "gloss": "to legitimize"},
            {"lemma": "el jinete", "pos": "noun", "cefr": "B1", "gloss": "horseman, rider"},
            {"lemma": "el foso", "pos": "noun", "cefr": "B1", "gloss": "pit, trench"},
            {"lemma": "ocultar", "pos": "verb", "cefr": "B1", "gloss": "to conceal, hide"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué función cumplía el documento del «Requerimiento» de 1513?",
                "options": [
                    "Legitimar jurídicamente la guerra contra los indígenas si no aceptaban someterse a la corona.",
                    "Establecer tratados de libre comercio entre España y los pueblos indígenas.",
                    "Distribuir tierras comunales de forma equitativa entre los campesinos."
                ],
                "correctIndex": 0,
                "explanation": "El Requerimiento era una fórmula jurídica que justificaba la violencia si los indígenas no aceptaban de inmediato la soberanía española."
            }
        ]
    },

    "b1-conquista-05-catastrofe.json": {
        "id": "story.b1.conquista.05",
        "title": "¿Conquista o catástrofe?",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Historiography of the conquest: asymmetrical sources, León-Portilla's 'Visión de los vencidos', the Black and White legends, and demographic catastrophe.",
        "characters": [],
        "location": "América colonial y Europa",
        "grammar": ["voz pasiva en balance historiográfico"],
        "vocabularyTopics": ["¿Conquista o catástrofe?"],
        "paragraphs": [
            {"type": "narration", "text": "Al examinar la conquista del continente americano, una de las mayores dificultades radica en la profunda asimetría de las fuentes históricas que han llegado hasta nosotros. Casi todos los relatos escritos sobre la conquista fueron redactados por el bando vencedor: capitanes como Hernán Cortés en sus Cartas de relación o cronistas como Bernal Díaz del Castillo."},
            {"type": "narration", "text": "Los testimonios indígenas directos son escasos debido a la destrucción de códices y bibliotecas. Los pocos testimonios indígenas que sobrevivieron fueron recopilados y traducidos siglos después por Miguel León-Portilla en su célebre obra Visión de los vencidos (1959), permitiendo al mundo conocer poemas conmovedores donde los nahuas lloran la pérdida de Tenochtitlan."},
            {"type": "narration", "text": "Durante siglos, el debate sobre la conquista estuvo polarizado por dos corrientes propagandísticas opuestas. Durante mucho tiempo fue promovida, sobre todo en España, una interpretación conocida como 'leyenda blanca', que presentaba la conquista como una gesta civilizadora y benévola que trajo el cristianismo y la cultura occidental a pueblos supuestamente bárbaros."},
            {"type": "narration", "text": "En el polo opuesto surgió la 'leyenda negra', impulsada por las potencias rivales de España (Inglaterra, Francia y los Países Bajos), que retrataba a los españoles como monstruos guiados únicamente por la codicia y la crueldad sádica. Los historiadores actuales coinciden en que ambas leyendas fueron construidas, en última instancia, con fines políticos más que históricos."},
            {"type": "narration", "text": "Por ello, muchos especialistas prefieren distinguir dos dimensiones del proceso: la 'conquista', entendida como el conflicto bélico y militar relativamente rápido que derribó a los imperios mexica e inca, y la 'catástrofe demográfica', un colapso biológico y social prolongado que causó la muerte de decenas de millones de personas por epidemias, hambrunas y explotación."},
            {"type": "narration", "text": "Reconocer esta complejidad no significa justificar la violencia del pasado, sino entender con rigor cómo se forjó el mundo mestizo y diverso en el que vivimos hoy."}
        ],
        "keyVocab": [
            {"lemma": "redactar", "pos": "verb", "cefr": "B1", "gloss": "to write, draft"},
            {"lemma": "el bando", "pos": "noun", "cefr": "B1", "gloss": "side, faction"},
            {"lemma": "escaso", "pos": "adjective", "cefr": "B1", "gloss": "scarce, limited"},
            {"lemma": "recopilar", "pos": "verb", "cefr": "B1", "gloss": "to compile, collect"},
            {"lemma": "benévolo", "pos": "adjective", "cefr": "B1", "gloss": "benevolent"},
            {"lemma": "resistir", "pos": "verb", "cefr": "B1", "gloss": "to endure, withstand"},
            {"lemma": "de antemano", "pos": "expression", "cefr": "B1", "gloss": "beforehand"},
            {"lemma": "la hambruna", "pos": "noun", "cefr": "B1", "gloss": "famine"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué recopila la célebre obra «Visión de los vencidos» de Miguel León-Portilla?",
                "options": [
                    "Testimonios y cantos nahuas que narran la conquista desde la perspectiva indígena.",
                    "Cartas secretas escritas por Hernán Cortés al rey de España.",
                    "Documentos notariales sobre la venta de tierras coloniales."
                ],
                "correctIndex": 0,
                "explanation": "Publicada en 1959, Visión de los vencidos reunió poemas y relatos en náhuatl sobre la caída de Tenochtitlan."
            }
        ]
    },

    # =========================================================================
    # UNIT 05: sociedadcolonial (Colonial Society)
    # =========================================================================
    "b1-sociedadcolonial-01-imperio.json": {
        "id": "story.b1.sociedadcolonial.01",
        "title": "El imperio español",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Administrative architecture of the Spanish Empire: the viceroyalties of New Spain and Peru, the Casa de Contratación, and 'se obedece pero no se cumple'.",
        "characters": [],
        "location": "Ciudad de México, Lima y Sevilla",
        "grammar": ["voz pasiva en instituciones coloniales"],
        "vocabularyTopics": ["El imperio español"],
        "paragraphs": [
            {"type": "narration", "text": "Tras la caída de los grandes imperios indígenas, la corona española se enfrentó al colosal desafío de gobernar un territorio miles de veces más extenso que la propia península ibérica, separado por miles de kilómetros de océano."},
            {"type": "narration", "text": "Para administrar este vasto continente, la corona creó una sofisticada estructura de virreinatos y audiencias reales. El virreinato de Nueva España fue creado en 1535 con capital en la Ciudad de México; el virreinato del Perú fue establecido en 1542 con capital en Lima. Al frente de cada uno se encontraba un virrey, quien actuaba como representante directo y encarnación de la persona del monarca español."},
            {"type": "narration", "text": "Casi dos siglos y medio después, en el marco de las reformas borbónicas del siglo dieciocho, fueron creados dos virreinatos adicionales, el de Nueva Granada (1717) y el del Río de la Plata (1776), para mejorar la defensa costera y la recaudación fiscal en regiones en rápido crecimiento."},
            {"type": "narration", "text": "En el plano económico, todo el comercio con las colonias estaba controlado por una sola institución, la Casa de Contratación, con sede en Sevilla. Este organismo regulaba rigurosamente la navegación, cobraba impuestos aduaneros y supervisaba el monopolio comercial que prohibía a las colonias comerciar con potencias extranjeras o entre sí."},
            {"type": "narration", "text": "Este sistema fue diseñado para mantener el control sobre un territorio enorme y asegurar que las riquezas de América fluyeran directamente hacia las arcas metropolitanas."},
            {"type": "narration", "text": "No obstante, la enorme distancia y los meses que tardaba en llegar una orden real desde Madrid generaron un célebre mecanismo de pragmatismo legal: la fórmula «se obedece pero no se cumple». Mediante esta práctica jurídica, las autoridades virreinales acataban con respeto la autoridad formal del rey, pero suspendían la aplicación de leyes que consideraban inaplicables o peligrosas para la estabilidad local."}
        ],
        "keyVocab": [
            {"lemma": "el virreinato", "pos": "noun", "cefr": "B1", "gloss": "viceroyalty"},
            {"lemma": "la audiencia", "pos": "noun", "cefr": "B1", "gloss": "royal high court"},
            {"lemma": "la recaudación", "pos": "noun", "cefr": "B1", "gloss": "tax collection"},
            {"lemma": "aduanero", "pos": "adjective", "cefr": "B1", "gloss": "customs, tariff"},
            {"lemma": "el monopolio", "pos": "noun", "cefr": "B1", "gloss": "monopoly"},
            {"lemma": "acatar", "pos": "verb", "cefr": "B1", "gloss": "to comply with, respect"},
            {"lemma": "inaplicable", "pos": "adjective", "cefr": "B1", "gloss": "unworkable, inapplicable"},
            {"lemma": "la estabilidad", "pos": "noun", "cefr": "B1", "gloss": "stability"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué significaba en la práctica la fórmula colonial «se obedece pero no se cumple»?",
                "options": [
                    "Reconocer la autoridad del rey pero suspender la aplicación de una ley considerada dañina o inaplicable.",
                    "Declarar la independencia inmediata de la corona española.",
                    "Negarse a pagar impuestos a la Casa de Contratación."
                ],
                "correctIndex": 0,
                "explanation": "Era un mecanismo legal para adaptar las órdenes reales de Madrid a las complejas realidades locales americanas."
            }
        ]
    },

    "b1-sociedadcolonial-02-jerarquia.json": {
        "id": "story.b1.sociedadcolonial.02",
        "title": "Una sociedad jerárquica",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Social stratification: the two republics, limpieza de sangre certificates, caste systems, and criollo exclusion from high office.",
        "characters": [],
        "location": "América virreinal",
        "grammar": ["se pasiva en estructuras sociales"],
        "vocabularyTopics": ["Una sociedad jerárquica"],
        "paragraphs": [
            {"type": "narration", "text": "La sociedad colonial hispanoamericana se organizó sobre una rígida jerarquía estamental basada en el origen étnico, el nacimiento y el estatus jurídico. Desde los primeros momentos, las leyes de la corona concibieron la existencia de dos esferas separadas: la «república de españoles» y la «república de indios»."},
            {"type": "narration", "text": "En la práctica, se favorecía sistemáticamente a la 'república de españoles' sobre la 'república de indios'. Aunque la nobleza indígena conservó ciertos fueros y cargos locales como caciques gobernadores, la gran masa de población indígena quedó relegada al pago de tributos y al trabajo forzado en minas y haciendas."},
            {"type": "narration", "text": "Para asegurar los privilegios de la élite blanca, se desarrolló una obsesión genealógica con el linaje. Para acceder a la universidad o a un cargo público, se exigía presentar un certificado de 'limpieza de sangre'. Este documento probaba, mediante testigos y registros parroquiales, que la persona no descendía de antepasados judíos, musulmanes, africanos ni indígenas."},
            {"type": "narration", "text": "Con el mestizaje generalizado entre europeos, indígenas y personas de origen africano, la administración colonial y los artistas desarrollaron el sistema de castas: complejas clasificaciones pictóricas que categorizaban combinaciones como mestizo, mulato, zambo o castizo, asignando derechos y restricciones a cada grupo."},
            {"type": "narration", "text": "Incluso dentro de la élite blanca existía una profunda brecha. Se reservaban los cargos más altos casi exclusivamente para los peninsulares, es decir, funcionarios nacidos en España. Los criollos, nacidos en América de ascendencia española, controlaban haciendas, minas y el comercio local, pero sufrían una discriminación sistemática que les impedía acceder a los puestos de virrey, oidor o arzobispo."},
            {"type": "narration", "text": "Con el tiempo, se acumuló tanto resentimiento en torno a esta exclusión que buena parte del liderazgo independentista saldría de esas familias criollas educadas y adineradas que sentían a América como su verdadera patria."}
        ],
        "keyVocab": [
            {"lemma": "la esfera", "pos": "noun", "cefr": "B1", "gloss": "sphere"},
            {"lemma": "el tribunal", "pos": "noun", "cefr": "B1", "gloss": "court, tribunal"},
            {"lemma": "descender", "pos": "verb", "cefr": "B1", "gloss": "to descend from"},
            {"lemma": "el gremio", "pos": "noun", "cefr": "B1", "gloss": "guild"},
            {"lemma": "falsificar", "pos": "verb", "cefr": "B1", "gloss": "to falsify, forge"},
            {"lemma": "el agravio", "pos": "noun", "cefr": "B1", "gloss": "grievance, offense"},
            {"lemma": "el arraigo", "pos": "noun", "cefr": "B1", "gloss": "deep roots, attachment"},
            {"lemma": "acumularse", "pos": "verb", "cefr": "B1", "gloss": "to accumulate"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué la exclusión de los criollos de los altos cargos virreinales generó tanto resentimiento?",
                "options": [
                    "Porque familias criollas ricas y educadas veían que los puestos se entregaban a peninsulares recién llegados.",
                    "Porque a los criollos se les prohibía poseer haciendas o propiedades privadas.",
                    "Porque los criollos pagaban el doble de impuestos que los indígenas."
                ],
                "correctIndex": 0,
                "explanation": "Los criollos consideraban injusto que los mejores cargos estuvieran reservados a los nacidos en la península ibérica."
            }
        ]
    },

    "b1-sociedadcolonial-03-iglesia.json": {
        "id": "story.b1.sociedadcolonial.03",
        "title": "La Iglesia",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Catholic Church as imperial pillar: early universities, hospitals, Jesuit reducciones in Paraguay, and the limits of Inquisitorial jurisdiction.",
        "characters": [],
        "location": "América virreinal",
        "grammar": ["gerundio para acciones simultáneas"],
        "vocabularyTopics": ["La Iglesia"],
        "paragraphs": [
            {"type": "narration", "text": "En el imperio hispanoamericano, la Iglesia católica no fue simplemente una institución religiosa, sino un auténtico pilar del poder civil, la educación, la sanidad y la economía. Bajo el régimen del Patronato Real, los reyes de España tenían la facultad de nombrar obispos y administrar los diezmos eclesiásticos."},
            {"type": "narration", "text": "Vigilando la ortodoxia religiosa mientras construía hospitales, escuelas y universidades, la Iglesia funcionó como una de las instituciones más poderosas del imperio. Apenas pocas décadas después de la conquista, se fundaron la Real y Pontificia Universidad de México (1551) y la Universidad Nacional Mayor de San Marcos en Lima (1551), centros académicos donde se formaron generaciones de letrados y teólogos."},
            {"type": "narration", "text": "Un experimento social y religioso único fueron las reducciones o misiones jesuitas en la región del Río de la Plata y Paraguay. Enseñando la doctrina cristiana mientras aprendían y usaban el idioma guaraní, los jesuitas lograron una relación menos violenta con las comunidades originarias en comparación con el régimen de la encomienda."},
            {"type": "narration", "text": "Estas comunidades, produciendo tejidos y ganado mientras desarrollaban una notable tradición musical y artística barroca, llegaron a ser económicamente prósperas y contaron incluso con milicias indígenas armadas para defenderse de los cazadores de esclavos portugueses."},
            {"type": "narration", "text": "Sin embargo, el inmenso poder e independencia de la Compañía de Jesús despertó recelos en la corte de Madrid. En 1767, el rey Carlos III decretó la expulsión de los jesuitas de todos los dominios de la monarquía hispánica. Las reducciones, dependiendo casi por completo de la administración jesuita, entraron en rápida decadencia tras la expulsión."},
            {"type": "narration", "text": "Aunque el Tribunal del Santo Oficio de la Inquisición perseguía con severidad la herejía y el contrabando de libros prohibidos entre españoles y criollos, oficialmente carecía de jurisdicción sobre la población indígena, que quedaba sujeta a tribunales eclesiásticos ordinarios considerados menos punitivos."}
        ],
        "keyVocab": [
            {"lemma": "la orden religiosa", "pos": "noun", "cefr": "B1", "gloss": "religious order"},
            {"lemma": "semiautónomo", "pos": "adjective", "cefr": "B1", "gloss": "semi-autonomous"},
            {"lemma": "el tejido", "pos": "noun", "cefr": "B1", "gloss": "fabric, textile"},
            {"lemma": "próspero", "pos": "adjective", "cefr": "B1", "gloss": "prosperous"},
            {"lemma": "expulsar", "pos": "verb", "cefr": "B1", "gloss": "to expel"},
            {"lemma": "la herejía", "pos": "noun", "cefr": "B1", "gloss": "heresy"},
            {"lemma": "carecer", "pos": "verb", "cefr": "B1", "gloss": "to lack"},
            {"lemma": "eclesiástico", "pos": "adjective", "cefr": "B1", "gloss": "ecclesiastical, church"}
        ],
        "compQuestions": [
            {
                "question": "¿Tenía el tribunal de la Inquisición jurisdicción sobre los indígenas en las colonias?",
                "options": [
                    "No, oficialmente carecía de jurisdicción sobre la población indígena.",
                    "Sí, todos los procesos inquisitoriales se centraban exclusivamente en los indígenas.",
                    "Solo en los virreinatos de Nueva Granada y Río de la Plata."
                ],
                "correctIndex": 0,
                "explanation": "La corona española consideraba a los indígenas «neófitos» en la fe y los eximió de la jurisdicción del Santo Oficio."
            }
        ]
    },

    "b1-sociedadcolonial-04-vidacotidiana.json": {
        "id": "story.b1.sociedadcolonial.04",
        "title": "La vida cotidiana",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Everyday colonial life: the 1573 urban grid ordinances, central plazas, daily social mixing, and the Chiapas church chocolate scandal.",
        "characters": [],
        "location": "Ciudades coloniales (Oaxaca, Chiapas, Lima)",
        "grammar": ["conectores formales de causa y tiempo"],
        "vocabularyTopics": ["La vida cotidiana"],
        "paragraphs": [
            {"type": "narration", "text": "El paisaje urbano de Hispanoamérica no surgió de forma desordenada o espontánea. A raíz de las Leyes de Indias, promulgadas en 1573 por el rey Felipe II, prácticamente todas las nuevas ciudades siguieron el mismo patrón geométrico: una gran plaza central rodeada por la catedral, el palacio de gobierno y el cabildo, de la cual partían calles rectas en cuadrícula perfecta."},
            {"type": "narration", "text": "A lo largo del día, esa plaza y sus alrededores se llenaban de actividad. Desde las primeras horas de la mañana, vendedores indígenas traían hortalizas en canoas o mulas, aguadores repartían agua fresca desde las fuentes del acueducto y comerciantes ambulantes ofrecían dulces, telas y herramientas."},
            {"type": "narration", "text": "Como consecuencia de esa actividad constante, la plaza funcionaba como el verdadero centro social de la ciudad. Aunque las leyes virreinales insistían en la separación estricta entre españoles e indígenas, en los mercados coloniales esa barrera se difuminaba constantemente, creando un espacio de intercambio lingüístico, musical y gastronómico."},
            {"type": "narration", "text": "Las costumbres sociales daban lugar a intensas disputas cotidianas. En el siglo diecisiete, la alta sociedad colonial tenía una debilidad irresistible por el chocolate caliente espumoso. En San Cristóbal de las Casas (Chiapas), las damas criollas tenían por costumbre hacer que sus sirvientas les sirvieran tazas de chocolate dentro de la catedral durante las largas misas dominicales."},
            {"type": "narration", "text": "El obispo de Chiapas, profundamente escandalizado por la falta de reverencia, prohibió terminantemente beber chocolate en el templo bajo pena de excomunión. La aristocracia local reaccionó con indignación, y poco después el obispo murió repentinamente de violentos dolores estomacales. Aunque nunca se confirmó oficialmente, corrió el rumor generalizado de que había sido envenenado con una taza de chocolate emponzoñado."},
            {"type": "narration", "text": "La vida cotidiana colonial, a raíz de sus propias tensiones de género, de clase y de costumbre, generaba conflictos tan reales como los grandes debates políticos, revelando la vitalidad humana de un mundo en constante transformación."}
        ],
        "keyVocab": [
            {"lemma": "promulgar", "pos": "verb", "cefr": "B1", "gloss": "to enact, promulgate"},
            {"lemma": "la cuadrícula", "pos": "noun", "cefr": "B1", "gloss": "grid"},
            {"lemma": "el acueducto", "pos": "noun", "cefr": "B1", "gloss": "aqueduct"},
            {"lemma": "ambulante", "pos": "adjective", "cefr": "B1", "gloss": "itinerant, street"},
            {"lemma": "difuminarse", "pos": "verb", "cefr": "B1", "gloss": "to blur, fade"},
            {"lemma": "la debilidad", "pos": "noun", "cefr": "B1", "gloss": "weakness, fondness"},
            {"lemma": "escandalizado", "pos": "adjective", "cefr": "B1", "gloss": "scandalized, shocked"},
            {"lemma": "envenenar", "pos": "verb", "cefr": "B1", "gloss": "to poison"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué tantas ciudades coloniales en América Latina tienen el mismo diseño urbano?",
                "options": [
                    "Porque las Leyes de Indias de 1573 ordenaron construir plazas centrales y calles en cuadrícula.",
                    "Porque todas las ciudades fueron diseñadas por el mismo arquitecto sevillano.",
                    "Porque las ciudades prehispánicas ya tenían exactamente ese mismo plano antes de 1492."
                ],
                "correctIndex": 0,
                "explanation": "Las Reales Ordenanzas de Felipe II fijaron la cuadrícula y la plaza mayor como modelo urbanístico obligatorio."
            }
        ]
    },

    "b1-sociedadcolonial-05-vivir.json": {
        "id": "story.b1.sociedadcolonial.05",
        "title": "Vivir en la colonia",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Synthesis of colonial society: a three-century epoch that lasted longer than subsequent independent history, leaving indelible institutional and human layers.",
        "characters": [],
        "location": "América Latina",
        "grammar": ["voz pasiva en síntesis histórica"],
        "vocabularyTopics": ["Vivir en la colonia"],
        "paragraphs": [
            {"type": "narration", "text": "Al reflexionar sobre el periodo colonial, conviene recordar una dimensión fundamental: su extraordinaria duración temporal. Desde la caída de Tenochtitlan en 1521 hasta las guerras de independencia de la década de 1820 transcurrieron tres siglos enteros, una etapa histórica más larga que la vida independiente de la inmensa mayoría de los países latinoamericanos actuales."},
            {"type": "narration", "text": "A lo largo de esas tres centurias, la sociedad colonial descansó sobre tres pilares institucionales. Los territorios fueron administrados mediante virreinatos y audiencias que respondían a una corona lejana. Las oportunidades económicas y políticas fueron distribuidas de forma muy desigual entre peninsulares, criollos, indígenas y africanos. Las estructuras educativas y sanitarias fueron mantenidas, en gran medida, por una Iglesia que actuaba casi como un segundo gobierno."},
            {"type": "narration", "text": "Sin embargo, el mundo colonial no se reducía a decretos oficiales o jerarquías rígidas. Buena parte del trazado urbano actual fue diseñado directamente por una ley real de 1573, pero la vida que floreció en esas calles fue un proceso orgánico y mestizo donde las leyes escritas chocaban a diario con la creatividad popular."},
            {"type": "narration", "text": "La arquitectura barroca, las celebraciones patronales, las recetas gastronómicas, los dialectos regionales y las expresiones artísticas reflejan la fusión de influencias europeas, amerindias y africanas que moldearon el carácter de la región."},
            {"type": "narration", "text": "Entender la sociedad colonial significa comprender dos capas superpuestas: la capa institucional del imperio, con sus leyes y monopolios, y la capa humana de la convivencia diaria en plazas, mercados y hogares. Ambas capas dejaron una huella imborrable que sigue viva en la cultura y la sociedad latinoamericana contemporánea."}
        ],
        "keyVocab": [
            {"lemma": "transcurrir", "pos": "verb", "cefr": "B1", "gloss": "to pass, elapse"},
            {"lemma": "la etapa", "pos": "noun", "cefr": "B1", "gloss": "stage, period"},
            {"lemma": "encajar", "pos": "verb", "cefr": "B1", "gloss": "to fit, match"},
            {"lemma": "el trazado", "pos": "noun", "cefr": "B1", "gloss": "layout, design"},
            {"lemma": "orgánico", "pos": "adjective", "cefr": "B1", "gloss": "organic"},
            {"lemma": "moldear", "pos": "verb", "cefr": "B1", "gloss": "to mold, shape"},
            {"lemma": "el registro", "pos": "noun", "cefr": "B1", "gloss": "record, register"},
            {"lemma": "superpuesto", "pos": "adjective", "cefr": "B1", "gloss": "superimposed, layered"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué es tan relevante la duración del periodo colonial en América Latina?",
                "options": [
                    "Porque duró tres siglos, más tiempo del que muchos países llevan como naciones independientes.",
                    "Porque duró apenas veinte años antes de las primeras independencias.",
                    "Porque fue un periodo sin ningún cambio social ni económico."
                ],
                "correctIndex": 0,
                "explanation": "Los 300 años de dominio colonial dejaron una huella institucional y cultural profunda y duradera."
            }
        ]
    },

    # =========================================================================
    # UNIT 06: economiacolonial (Colonial Economy)
    # =========================================================================
    "b1-economiacolonial-01-plataoro.json": {
        "id": "story.b1.economiacolonial.01",
        "title": "Plata y oro",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Mining economy: the silver boom of Cerro Rico in Potosí, the mita labor draft, the patio amalgamation process, and global silver circulation.",
        "characters": [],
        "location": "Potosí (Alto Perú, Bolivia) y Zacatecas",
        "grammar": ["voz pasiva en procesos económicos"],
        "vocabularyTopics": ["Plata y oro"],
        "paragraphs": [
            {"type": "narration", "text": "El motor financiero del imperio español y el eje de la primera economía global fue la minería de la plata. En 1545 fue descubierto el yacimiento de plata del Cerro Rico de Potosí, en el actual territorio de Bolivia, considerado el depósito de mineral de plata más colosal jamás encontrado en la historia de la humanidad."},
            {"type": "narration", "text": "Casi de la noche a la mañana, a más de cuatro mil metros de altitud, surgió la Villa Imperial de Potosí. Hacia 1600, su auge minero atrajo a más de ciento sesenta mil habitantes, convirtiéndola en una urbe más poblada que Londres, París o Madrid."},
            {"type": "narration", "text": "Enormes cantidades de plata fueron extraídas de esa montaña y enviadas a España. Sin embargo, esta riqueza incalculable tuvo un costo humano aterrador. Para garantizar mano de obra constante, el virrey Francisco de Toledo reactivó y transformó el sistema incaico de la mita, convirtiéndolo en un servicio de trabajo forzado rotativo que obligaba a miles de indígenas andinos a trabajar en condiciones extremas dentro de túneles oscuros y asfixiantes."},
            {"type": "narration", "text": "A partir de 1554, la producción de plata fue transformada por un nuevo método inventado por Bartolomé de Medina: el proceso de patio. Este método utilizaba mercurio líquido traído de las minas de Huancavelica o Almadén para amalgamar la plata y separar el mineral puro de la roca."},
            {"type": "narration", "text": "El mercurio era extremadamente tóxico: miles de trabajadores mineros sufrieron temblores incontrolables, parálisis y graves daños neurológicos irreversibles al inhalar vapores tóxicos o pisar descalzos la mezcla mineral durante meses."},
            {"type": "narration", "text": "Gran parte de esa plata fue acuñada en monedas, los llamados 'reales de a ocho' (pesos de plata españoles). Gracias a las flotas del Atlántico y a la ruta transpacífica del Galeón de Manila, los reales de a ocho de Potosí y Zacatecas se convirtieron en la primera divisa internacional del planeta, llegando a circular ampliamente en mercados de Europa, el Imperio Otomano, la India y la China Ming."}
        ],
        "keyVocab": [
            {"lemma": "el yacimiento", "pos": "noun", "cefr": "B1", "gloss": "deposit, mineral bed"},
            {"lemma": "extraer", "pos": "verb", "cefr": "B1", "gloss": "to extract"},
            {"lemma": "el mineral", "pos": "noun", "cefr": "B1", "gloss": "ore, mineral"},
            {"lemma": "tóxico", "pos": "adjective", "cefr": "B1", "gloss": "toxic"},
            {"lemma": "el temblor", "pos": "noun", "cefr": "B1", "gloss": "tremor, shaking"},
            {"lemma": "el auge", "pos": "noun", "cefr": "B1", "gloss": "boom, height"},
            {"lemma": "acuñar", "pos": "verb", "cefr": "B1", "gloss": "to coin, mint"},
            {"lemma": "circular", "pos": "verb", "cefr": "B1", "gloss": "to circulate"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué consecuencia médica sufrían los trabajadores mineros debido al proceso de patio con mercurio?",
                "options": [
                    "Envenenamiento crónico con temblores y daños neurológicos irreversibles.",
                    "Problemas digestivos pasajeros que se curaban con hierbas locales.",
                    "Fiebre amarilla transmitida por mosquitos en los túneles."
                ],
                "correctIndex": 0,
                "explanation": "La inhalación y el contacto con vapores de mercurio causaban hidrargirismo (envenenamiento por mercurio)."
            }
        ]
    },

    "b1-economiacolonial-02-trabajo.json": {
        "id": "story.b1.economiacolonial.02",
        "title": "Trabajo y explotación",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Labor systems: the encomienda, the 1542 New Laws, the repartimiento, the 1550 Valladolid debate, and enslaved African labor.",
        "characters": [],
        "location": "América virreinal y Valladolid",
        "grammar": ["se pasiva en legislación laboral"],
        "vocabularyTopics": ["Trabajo y explotación"],
        "paragraphs": [
            {"type": "narration", "text": "La economía colonial requería inmensos contingentes de mano de obra para extraer plata, construir ciudades y cultivar tierras agrícolas. Para movilizar y controlar esta fuerza laboral, la corona española implantó una sucesión de sistemas de trabajo coercitivo que fueron evolucionando a lo largo de los siglos."},
            {"type": "narration", "text": "En la encomienda se concedía a un colono español el derecho a la mano de obra de una comunidad indígena a cambio de velar por su bienestar y evangelización. Sin embargo, los abusos brutales de los encomenderos y la rápida caída de la población originaria provocaron intensas protestas morales por parte de religiosos como Antonio de Montesinos y Bartolomé de las Casas."},
            {"type": "narration", "text": "En 1542 se promulgaron las Leyes Nuevas, que intentaron limitar el poder de los encomenderos, prohibiendo la esclavitud indígena y estipulando que las encomiendas no se heredarían a perpetuidad. La ley provocó rebeliones armadas de encomenderos en Perú y México, pero marcó el inicio de la intervención directa de la corona."},
            {"type": "narration", "text": "Con el tiempo, se fue sustituyendo la encomienda por el repartimiento, un sistema de trabajo rotativo más controlado por funcionarios reales, en el que los campesinos indígenas debían prestar servicio remunerado por turnos en obras públicas o haciendas durante algunas semanas al año."},
            {"type": "narration", "text": "Estos debates tuvieron su momento culminante en 1550, cuando en Valladolid se organizó un debate formal sobre si los indígenas tenían plena condición humana y si era legítimo someterlos por la fuerza. Bartolomé de las Casas defendió la plena racionalidad y derechos de los pueblos indígenas, mientras que el erudito Juan Ginés de Sepúlveda defendió la teoría aristotélica de la servidumbre natural. Aunque la controversia no concluyó con un vencedor oficial claro, estimuló la promulgación de leyes protectoras de la corona."},
            {"type": "narration", "text": "Cuando la caída demográfica indígena y las restricciones legales impidieron cubrir la demanda laboral en regiones tropicales y mineras, los hacendados y mineros empezaron a recurrir al tráfico de personas esclavizadas traídas por la fuerza desde el continente africano, instaurando una nueva y terrible dimensión de opresión."}
        ],
        "keyVocab": [
            {"lemma": "conceder", "pos": "verb", "cefr": "B1", "gloss": "to grant"},
            {"lemma": "sustituir", "pos": "verb", "cefr": "B1", "gloss": "to substitute, replace"},
            {"lemma": "rotativo", "pos": "adjective", "cefr": "B1", "gloss": "rotational, by shifts"},
            {"lemma": "convocar", "pos": "verb", "cefr": "B1", "gloss": "to convene, call"},
            {"lemma": "pleno", "pos": "adjective", "cefr": "B1", "gloss": "full, complete"},
            {"lemma": "la subordinación", "pos": "noun", "cefr": "B1", "gloss": "subordination"},
            {"lemma": "el vencedor", "pos": "noun", "cefr": "B1", "gloss": "victor, winner"},
            {"lemma": "recurrir a", "pos": "expression", "cefr": "B1", "gloss": "to resort to"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué pretendían lograr las Leyes Nuevas de 1542 promulgadas por Carlos I?",
                "options": [
                    "Limitar el poder y la herencia de los encomenderos y prohibir la esclavitud indígena.",
                    "Aumentar el número de horas de trabajo forzado en las minas.",
                    "Expulsar a todos los colonos españoles de vuelta a Europa."
                ],
                "correctIndex": 0,
                "explanation": "Las Leyes Nuevas buscaron frenar los abusos feudales de los encomenderos y proteger a la población indígena."
            }
        ]
    },

    "b1-economiacolonial-03-plantaciones.json": {
        "id": "story.b1.economiacolonial.03",
        "title": "Plantaciones",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Plantation agriculture: sugar mills as proto-industrial factories, Brazil's massive slave imports, and Venezuela's 'gran cacao' elite.",
        "characters": [],
        "location": "Caribe, Brasil y costas tropicales",
        "grammar": ["gerundio explicativo"],
        "vocabularyTopics": ["Plantaciones"],
        "paragraphs": [
            {"type": "narration", "text": "Junto a la minería de plata de las tierras altas, el otro gran pilar económico del mundo colonial fue la agricultura de plantación en las llanuras tropicales de las costas atlánticas y las islas del Caribe. Este modelo no se orientaba al autoconsumo local, sino al monocultivo masivo de productos de alta demanda para el mercado europeo."},
            {"type": "narration", "text": "El azúcar fue el producto más importante, aumentando constantemente la demanda europea a medida que el consumo se popularizaba entre todas las clases sociales. Para procesar la caña recién cortada antes de que se fermentara, los hacendados construyeron grandes complejos agroindustriales llamados ingenios."},
            {"type": "narration", "text": "El ingenio azucarero, combinando maquinaria pesada, grandes hornos y mano de obra intensiva, funcionaba casi como una fábrica temprana siglos antes de la Revolución Industrial. La molienda de la caña en ruedas hidráulicas y la cocción del jugo en calderas de cobre exigían turnos de trabajo ininterrumpidos de día y de noche durante los meses de zafra."},
            {"type": "narration", "text": "Las condiciones de trabajo en los ingenios eran extenuantes y peligrosas. Debido a la altísima mortalidad y las bajas tasas de natalidad, las plantaciones dependían de un constante reemplazo de mano de obra. Por esta razón, la colonia portuguesa de Brasil recibió más personas esclavizadas africanas que cualquier otro destino en el continente americano, superando los cuatro millones de seres humanos a lo largo de tres siglos."},
            {"type": "narration", "text": "En otras regiones tropicales prosperaron diferentes cultivos comerciales. En los valles costeros de Venezuela, un pequeño grupo de familias acumuló fortunas cultivando y exportando cacao, convirtiéndose en una de las élites más influyentes, conocidas popularmente como los «grandes cacaos», de donde provenía la acaudalada familia de Simón Bolívar."},
            {"type": "narration", "text": "Asimismo, en las vegas cubanas se cultivaba un tabaco que, produciendo cosechas de gran calidad, se ganaría fama mundial por su aroma inconfundible. Las plantaciones forjaron así un modelo económico agroexportador sumamente rentable para las élites, pero fundado enteramente en la explotación humana."}
        ],
        "keyVocab": [
            {"lemma": "el monocultivo", "pos": "noun", "cefr": "B1", "gloss": "monoculture"},
            {"lemma": "el ingenio", "pos": "noun", "cefr": "B1", "gloss": "sugar mill"},
            {"lemma": "el horno", "pos": "noun", "cefr": "B1", "gloss": "furnace, oven"},
            {"lemma": "el reemplazo", "pos": "noun", "cefr": "B1", "gloss": "replacement"},
            {"lemma": "acumular", "pos": "verb", "cefr": "B1", "gloss": "to accumulate"},
            {"lemma": "la fortuna", "pos": "noun", "cefr": "B1", "gloss": "fortune"},
            {"lemma": "la finca", "pos": "noun", "cefr": "B1", "gloss": "estate, plantation"},
            {"lemma": "la calidad", "pos": "noun", "cefr": "B1", "gloss": "quality"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué se compara el ingenio azucarero colonial con una «fábrica temprana»?",
                "options": [
                    "Porque combinaba maquinaria pesada, hornos de fundición y turnos intensivos de mano de obra.",
                    "Porque funcionaba con máquinas de vapor inventadas en el siglo dieciocho.",
                    "Porque estaba ubicado en el centro de las grandes ciudades europeas."
                ],
                "correctIndex": 0,
                "explanation": "El procesamiento agroindustrial del azúcar requería disciplina fabril, calderas y maquinaria continua."
            }
        ]
    },

    "b1-economiacolonial-04-comercioimperial.json": {
        "id": "story.b1.economiacolonial.04",
        "title": "Comercio imperial",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The trade monopoly: the fleet and galleons convoy system, privateers, widespread contraband trade, and the Manila Galleon transpacific route.",
        "characters": [],
        "location": "Veracruz, Portobelo, La Habana, Acapulco y Manila",
        "grammar": ["conectores formales: a lo largo de, como consecuencia de"],
        "vocabularyTopics": ["Comercio imperial"],
        "paragraphs": [
            {"type": "narration", "text": "Para asegurar el monopolio sobre las riquezas americanas y proteger los cargamentos de plata de los ataques de corsarios y piratas ingleses, franceses y holandeses, la corona española diseñó un estricto sistema mercantilista de navegación."},
            {"type": "narration", "text": "A lo largo de casi todo el periodo colonial, el comercio legal estuvo organizado mediante un sistema de flotas. Dos veces al año, grandes convoyes de galeones armados zarpaban juntos desde Sevilla (y más tarde Cádiz) escoltando a decenas de barcos mercantes. Una flota se dirigía a Veracruz para abastecer al virreinato de Nueva España, y la otra a Portobelo (en el istmo de Panamá) para comerciar con el Perú. Todos los navíos se reunían en el puerto fortificado de La Habana antes de emprender el viaje de regreso a España cargados de plata y mercancías preciosas."},
            {"type": "narration", "text": "Como consecuencia de restricciones tan estrictas, se desarrolló un comercio ilegal, o contrabando. Puesto que las flotas oficiales llegaban solo cada uno o dos años y los precios de las manufacturas peninsulares eran exorbitantes, colonos de todas las clases sociales compraban telas, herramientas y esclavos a comerciantes extranjeros con la complicidad de las propias autoridades locales. En regiones como el Río de la Plata y el Caribe, el contrabando llegó a rivalizar con el comercio legal, o incluso superarlo en volumen."},
            {"type": "narration", "text": "El comercio colonial incluyó también una fascinante dimensión transpacífica. A lo largo de dos siglos y medio, el llamado Galeón de Manila (o Nao de China) navegó anualmente entre Acapulco y Manila, conectando directamente las economías de América y Asia."},
            {"type": "narration", "text": "Como consecuencia directa de esta ruta, ciudades como Acapulco se transformaron en mercados temporales enormes donde la plata mexicana y peruana se intercambiaba por seda, porcelana fina, marfil, especias y lacas chinas. Gran parte de estos productos de lujo asiáticos se consumían en palacios de México y Lima o se reexportaban hacia Europa."},
            {"type": "narration", "text": "El comercio imperial hispánico no fue, por tanto, el sistema cerrado y estático que describían las leyes reales, sino una compleja y dinámica red de rutas globales, convoyes armados y contrabando que conectó a cuatro continentes."}
        ],
        "keyVocab": [
            {"lemma": "la flota", "pos": "noun", "cefr": "B1", "gloss": "fleet"},
            {"lemma": "el pirata", "pos": "noun", "cefr": "B1", "gloss": "pirate"},
            {"lemma": "el contrabando", "pos": "noun", "cefr": "B1", "gloss": "smuggling, contraband"},
            {"lemma": "la complicidad", "pos": "noun", "cefr": "B1", "gloss": "complicity"},
            {"lemma": "rivalizar", "pos": "verb", "cefr": "B1", "gloss": "to rival, compete with"},
            {"lemma": "navegar", "pos": "verb", "cefr": "B1", "gloss": "to sail, navigate"},
            {"lemma": "la seda", "pos": "noun", "cefr": "B1", "gloss": "silk"},
            {"lemma": "la porcelana", "pos": "noun", "cefr": "B1", "gloss": "porcelain"}
        ],
        "compQuestions": [
            {
                "question": "¿Qué intercambiaba el Galeón de Manila entre América y Asia?",
                "options": [
                    "Plata americana a cambio de seda, porcelana y especias asiáticas.",
                    "Trigo europeo a cambio de café africano.",
                    "Madera del Caribe a cambio de armas de fuego de Japón."
                ],
                "correctIndex": 0,
                "explanation": "El Galeón de Manila transportaba plata de México y Perú hacia Filipinas y regresaba con mercancías chinas."
            }
        ]
    },

    "b1-economiacolonial-05-precioimperio.json": {
        "id": "story.b1.economiacolonial.05",
        "title": "El precio del imperio",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The economic paradox of empire: inflation, Spain's imperial debts, domestic industrial stagnation, and the human cost paid by millions.",
        "characters": [],
        "location": "España y América colonial",
        "grammar": ["voz pasiva en síntesis económica"],
        "vocabularyTopics": ["El precio del imperio"],
        "paragraphs": [
            {"type": "narration", "text": "Durante los siglos dieciséis y diecisiete, la corona española parecía la potencia más rica e invencible de la Tierra. Cantidades históricamente inéditas de plata y oro fueron enviadas desde América hacia España, financiando ejércitos, armadas y palacios monumentales como El Escorial."},
            {"type": "narration", "text": "Sin embargo, esta colosal entrada de metal precioso provocó una de las mayores paradojas económicas de la historia moderna. En lugar de generar un desarrollo industrial sostenible en la península, buena parte de la plata fue simplemente utilizada para pagar deudas de guerra contraídas con banqueros genoveses y alemanes, o para comprar manufacturas textiles y herramientas importadas del norte de Europa."},
            {"type": "narration", "text": "Además, la inundación de plata en los mercados europeos desató la llamada «revolución de los precios». Los precios de bienes y servicios fueron empujados al alza durante generaciones, generando una severa inflación que arruinó a los artesanos y campesinos españoles, haciendo que la producción nacional fuera menos competitiva que las importaciones extranjeras."},
            {"type": "narration", "text": "Mientras potencias emergentes como Inglaterra y los Países Bajos desarrollaban una pujante industria manufacturera y sistemas bancarios modernos, España quedó atrapada en una economía rentista y dependiente de la plata americana, sentando las bases de su posterior decadencia económica."},
            {"type": "narration", "text": "En las colonias, los beneficios de esta economía fueron distribuidos de forma extremadamente desigual. Mientras un puñado de hacendados, mineros y grandes comerciantes acapararon inmensas fortunas, las poblaciones indígenas y las personas esclavizadas africanas soportaron el peso del trabajo físico forzado y la marginación."},
            {"type": "narration", "text": "El precio del imperio se pagó así dos veces: primero en las minas y plantaciones de América por millones de vidas humanas, y después en la propia España, cuya economía quedó estructuralmente debilitada por la misma riqueza que parecía hacerla invulnerable."}
        ],
        "keyVocab": [
            {"lemma": "inédito", "pos": "adjective", "cefr": "B1", "gloss": "unprecedented"},
            {"lemma": "la deuda", "pos": "noun", "cefr": "B1", "gloss": "debt"},
            {"lemma": "la manufactura", "pos": "noun", "cefr": "B1", "gloss": "manufacture, manufactured goods"},
            {"lemma": "la inflación", "pos": "noun", "cefr": "B1", "gloss": "inflation"},
            {"lemma": "el ascenso", "pos": "noun", "cefr": "B1", "gloss": "rise, ascent"},
            {"lemma": "acaparar", "pos": "verb", "cefr": "B1", "gloss": "to hoard, monopolize"},
            {"lemma": "el hacendado", "pos": "noun", "cefr": "B1", "gloss": "landowner, estate owner"},
            {"lemma": "soportar", "pos": "verb", "cefr": "B1", "gloss": "to bear, endure"}
        ],
        "compQuestions": [
            {
                "question": "¿Por qué la abundancia de plata americana no impulsó la industria manufacturera en España?",
                "options": [
                    "Porque la plata se usó para pagar deudas bélicas y comprar manufacturas extranjeras, provocando inflación.",
                    "Porque las leyes españolas prohibían vender plata en territorio peninsular.",
                    "Porque toda la plata fue robada por piratas ingleses antes de llegar a los puertos."
                ],
                "correctIndex": 0,
                "explanation": "La plata financió guerras y compras externas en vez de invertirse en la producción manufacturera nacional."
            }
        ]
    }
}

def write_stories(stories_dict):
    for filename, sdata in stories_dict.items():
        paras = sdata["paragraphs"]
        segments = []
        t = 0.0
        for idx, p in enumerate(paras):
            words = len(p["text"].split())
            dur = round(max(5.0, words / 2.3), 1)
            segments.append({
                "paraIndex": idx,
                "startTime": round(t, 1),
                "endTime": round(t + dur, 1),
                "speaker": "Narrator",
                "lang": "es",
                "cues": [{"type": "pause", "durationMs": 250, "reason": "clause-boundary"}] if idx > 0 else [],
                "pronunciations": []
            })
            t += dur

        total_words = sum(len(p["text"].split()) for p in paras)
        est_minutes = max(5, round(total_words / 110))

        doc = {
            "id": sdata["id"],
            "title": sdata["title"],
            "level": sdata["level"],
            "lesson": sdata["lesson"],
            "order": sdata["order"],
            "type": sdata["type"],
            "estimatedMinutes": est_minutes,
            "summary": sdata["summary"],
            "characters": sdata["characters"],
            "location": sdata["location"],
            "grammar": sdata["grammar"],
            "vocabularyTopics": sdata["vocabularyTopics"],
            "paragraphs": paras,
            "narration": {
                "durationSeconds": round(t, 1),
                "pacing": {
                    "speedMultiplier": 1.0,
                    "rate_str": "+0%",
                    "rate_wpm": 145,
                    "style": "natural, expressive"
                },
                "speakers": {
                    "Narrator": {
                        "role": "narrator",
                        "gender": "neutral",
                        "tone": "clear, warm, steady storytelling guide"
                    }
                },
                "segments": segments,
                "pedagogical": {
                    "keyVocabulary": sdata["keyVocab"],
                    "targetGrammar": sdata["grammar"],
                    "comprehensionQuestions": sdata["compQuestions"]
                }
            }
        }

        target_path = DIR / filename
        target_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {filename}: {total_words} words, {len(paras)} paras")

if __name__ == "__main__":
    write_stories(BLOCK1_STORIES)
