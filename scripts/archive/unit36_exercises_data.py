"""
unit36_exercises_data.py
Exercise sets for Latin American Spanish B2 Unit 36 (Capstone Core & Regional),
strictly matching the 4-exercise pattern per lesson.
"""

EXERCISES_DATA = {
    # Core 36
    "b2-36-01": [
        {
            "id": "b2-36-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["voz-cadencia-ritmo-sintactico"],
            "question": "¿Qué recurso estilístico confiere cadencia solemne y equilibrio sintáctico a una tesis de clausura?",
            "options": [
                "El uso exclusivo de frases coloquiales incompletas.",
                "El bimembrismo rítmico y el paralelismo contrastivo ('No es A, sino B').",
                "La eliminación de toda puntuación en el texto.",
                "La repetición monótona de la conjunción copulativa 'y'."
            ],
            "correct": 1
        },
        {
            "id": "b2-36-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["voz-cadencia-ritmo-sintactico"],
            "sentence": "Examinar el pasado con __ permite proyectar el porvenir con audacia soberana y compromiso cívico.",
            "answer": "lucidez",
            "english": "Examining the past with lucidity makes it possible to project the future with sovereign audacity and civic commitment."
        },
        {
            "id": "b2-36-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-36-01-vocab"],
            "pairs": [
                ["cadencia", "rhythmic flow / cadence"],
                ["bimembrismo", "two-part parallel structure"],
                ["lucidez", "lucidity / intellectual clarity"],
                ["aforístico", "aphoristic / concise and memorable"]
            ]
        },
        {
            "id": "b2-36-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "En 'El Aleph' de Jorge Luis Borges, ¿qué acontecimiento luctuoso abre la narración?",
            "options": [
                "El derrumbe de la Biblioteca Nacional de Buenos Aires.",
                "La muerte de la amada Beatriz Viterbo en una ardiente mañana de febrero.",
                "El naufragio de un vapor en el Río de la Plata.",
                "El incendio de la casona de la calle Garay."
            ],
            "correct": 1
        }
    ],
    "b2-36-02": [
        {
            "id": "b2-36-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["voz-modalizacion-epistemica-compleja"],
            "question": "¿Cuál de las siguientes oraciones muestra una modalización epistémica reflexiva de registro superior?",
            "options": [
                "Todos tienen que estar de acuerdo conmigo obligatoriamente.",
                "Cabría postular legítimamente que la integración no es un lujo, sino un imperativo de supervivencia.",
                "Es obvio que nadie sabe nada de geopolítica.",
                "Yo digo que esto es así porque yo lo digo."
            ],
            "correct": 1
        },
        {
            "id": "b2-36-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["voz-modalizacion-epistemica-compleja"],
            "sentence": "Resulta __ que el acervo cultural compartido constituye nuestra mayor carta de presentación global.",
            "answer": "indudable",
            "english": "It is undeniable that shared cultural heritage constitutes our greatest global calling card."
        },
        {
            "id": "b2-36-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-36-02-vocab"],
            "pairs": [
                ["postular", "to posit / put forward as hypothesis"],
                ["aventurado", "risky / rash / overly bold"],
                ["indudable", "undeniable / beyond doubt"],
                ["epistémico", "epistemic / related to degree of certainty"]
            ]
        },
        {
            "id": "b2-36-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué pretende lograr el mediocre poeta Carlos Argentino Daneri en su obra 'La Tierra'?",
            "options": [
                "Componer canciones populares para el carnaval de Montevideo.",
                "Versificar prolijamente cada rincón del planeta, describiendo paisajes y tarifas sin ningún criterio poético selectivo.",
                "Escribir un tratado de botánica tropical en verso latino.",
                "Traducir los clásicos griegos al dialecto lunfardo."
            ],
            "correct": 1
        }
    ],
    "b2-36-03": [
        {
            "id": "b2-36-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["voz-organizadores-macroestructurales-ensayo"],
            "question": "¿Qué conector metadiscursivo es idóneo para introducir un nuevo eje temático en la arquitectura del ensayo?",
            "options": [
                "Cambiando de tema de golpe",
                "Por lo que atañe a / en lo tocante a",
                "Pues resulta que",
                "Y dale con que"
            ],
            "correct": 1
        },
        {
            "id": "b2-36-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["voz-organizadores-macroestructurales-ensayo"],
            "sentence": "A la __ de estas consideraciones, la cooperación científica interregional adquiere rango prioritario.",
            "answer": "luz",
            "english": "In light of these considerations, interregional scientific cooperation acquires priority status."
        },
        {
            "id": "b2-36-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-36-03-vocab"],
            "pairs": [
                ["a la luz de", "in light of"],
                ["por lo que atañe a", "as far as ... is concerned"],
                ["en consonancia con", "in consonance with / in accordance with"],
                ["macroestructura", "macrostructure / overall textual architecture"]
            ]
        },
        {
            "id": "b2-36-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué visión sobrecogedora experimenta Borges al recostarse en la oscuridad del sótano de la calle Garay?",
            "options": [
                "La aparición de un fantasma colonial que le exige dinero.",
                "La visión del Aleph: un punto resplandeciente donde coexisten todos los lugares del universo simultáneamente sin confundirse.",
                "Un túnel secreto que conduce al puerto de Buenos Aires.",
                "Un espejo roto que refleja únicamente su propio rostro envejecido."
            ],
            "correct": 1
        }
    ],
    "b2-36-04": [
        {
            "id": "b2-36-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["voz-metaforas-conceptuales-retorica"],
            "question": "¿Cómo opera una metáfora conceptual fecunda en la ensayística de nivel superior?",
            "options": [
                "Como un juego de palabras cómico sin relación con el tema.",
                "Como una estructura cognitiva que proyecta significado coherente y fuerza persuasiva a lo largo de la argumentación.",
                "Como un error sintáctico que debe corregirse de inmediato.",
                "Como una traducción literal de refranes anglosajones."
            ],
            "correct": 1
        },
        {
            "id": "b2-36-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["voz-metaforas-conceptuales-retorica"],
            "sentence": "Nuestra América es un archipiélago de memorias que confluyen en un mismo __ emancipador y fraterno.",
            "answer": "cauce",
            "english": "Our America is an archipelago of memories that flow into the same emancipatory and fraternal riverbed."
        },
        {
            "id": "b2-36-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-36-04-vocab"],
            "pairs": [
                ["cauce", "riverbed / channel / course"],
                ["archipiélago", "archipelago / cluster of diversity"],
                ["metáfora conceptual", "conceptual metaphor"],
                ["persuasión", "persuasion / rhetorical force"]
            ]
        },
        {
            "id": "b2-36-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué drama estético plantea Borges ante la experiencia inefable de la totalidad cósmica?",
            "options": [
                "Que el lenguaje humano es sucesivo en el tiempo y no puede reproducir con fidelidad una revelación infinita y simultánea.",
                "Que los editores le exigieron acortar el cuento por falta de papel.",
                "Que olvidó llevar lápiz y papel al sótano para anotar lo que veía.",
                "Que Daneri le cobró una suma exorbitante por permitirle entrar."
            ],
            "correct": 0
        }
    ],
    "b2-36-05": [
        {
            "id": "b2-36-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["voz-integracion-registro-estilo"],
            "question": "¿Qué cualidad define a la 'voz propia' del hablante competente en el nivel B2 culminante?",
            "options": [
                "La imitación pasiva de frases hechas y lugares comunes.",
                "La integración armónica de precisión conceptual, autoridad argumentativa y calidez expresiva con estilo personal.",
                "El rechazo de las normas gramaticales del idioma español.",
                "La utilización exclusiva de tecnicismos incomprensibles."
            ],
            "correct": 1
        },
        {
            "id": "b2-36-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["voz-integracion-registro-estilo"],
            "sentence": "Nos negamos a aceptar la fatalidad del desencanto; apostamos con __ por la justicia distributiva y la fraternidad.",
            "answer": "firmeza",
            "english": "We refuse to accept the fatality of disenchantment; we firmly wager on distributive justice and brotherhood."
        },
        {
            "id": "b2-36-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-36-05-vocab"],
            "pairs": [
                ["voz propia", "authentic authorial voice"],
                ["desencanto", "disenchantment / disillusionment"],
                ["firmeza", "firmness / steadfast resolve"],
                ["modulación", "register modulation / stylistic nuance"]
            ]
        },
        {
            "id": "b2-36-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué melancólica meditación clausura 'El Aleph' en la posdata del autor?",
            "options": [
                "La certeza de que la casona fue convertida en museo municipal.",
                "La dolorosa conciencia de la fragilidad del recuerdo humano y el olvido inevitable que borra incluso los rostros más amados.",
                "La victoria judicial de Daneri contra los propietarios de la confitería.",
                "La decisión del narrador de abandonar la literatura para siempre."
            ],
            "correct": 1
        }
    ],
    "b2-36-consolidation": [
        {
            "id": "b2-36-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["voz-cadencia-ritmo-sintactico"],
            "question": "Selecciona el período sintáctico que manifiesta mayor elegancia clásica y cadencia rítmica:",
            "options": [
                "Ni el desaliento venció la esperanza, ni la adversidad quebró la fraternidad inquebrantable de los pueblos.",
                "No perdimos la esperanza y tampoco se rompió la amistad entre todos los pueblos.",
                "La esperanza no se perdió para nada y la fraternidad siguió más o menos igual.",
                "Porque los pueblos son amigos entonces no se perdió la esperanza en ningún momento."
            ],
            "correct": 0
        },
        {
            "id": "b2-36-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["voz-modalizacion-epistemica-compleja"],
            "question": "¿Qué enunciado recurre a la atenuación epistémica para defender una propuesta con máxima cortesía intelectual?",
            "options": [
                "Quien no apoye esta medida es un enemigo del progreso.",
                "Habría cabido esperar un compromiso más audaz de las partes; no obstante, los avances alcanzados son estimables.",
                "El acuerdo firmado es una vergüenza absoluta para el continente.",
                "Ustedes no entienden la trascendencia de este tratado internacional."
            ],
            "correct": 1
        },
        {
            "id": "b2-36-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["voz-organizadores-macroestructurales-ensayo"],
            "sentence": "En __ con lo expuesto a lo largo del dictamen, el pleno ratificó los convenios multilaterales.",
            "answer": "consonancia",
            "english": "In consonance with what was set forth throughout the ruling, the plenary ratified the multilateral conventions."
        },
        {
            "id": "b2-36-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "En el universo literario borgeano, ¿qué valor universal encarna el Aleph?",
            "options": [
                "El secreto militar mejor guardado de la República Argentina.",
                "El símbolo supremo del infinito y la metáfora de la literatura como espejo donde el universo entero se contempla a sí mismo.",
                "Un truco de magia óptica para engañar a los incautos.",
                "Un talismán para ganar juegos de azar en los salones porteños."
            ],
            "correct": 1
        }
    ],

    # Regional 36 (Futuro)
    "b2-futuro-01": [
        {
            "id": "b2-futuro-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["futuro-prospectiva-hipotesis-complejas"],
            "question": "¿Qué estructura sintáctica otorga máxima concisión y rigor prospectivo a un escenario geopolítico futuro?",
            "options": [
                "La locución 'de + infinitivo' ('De articularse una política común, la región negociaría con ventaja...')",
                "El uso del pretérito imperfecto de indicativo sin conjunción",
                "El empleo de frases exclamativas informales",
                "La supresión del verbo principal de la apódosis"
            ],
            "correct": 0
        },
        {
            "id": "b2-futuro-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["futuro-prospectiva-hipotesis-complejas"],
            "sentence": "De coordinar las inversiones en litio y cobre, Suramérica __ con ventaja ante las superpotencias.",
            "answer": "negociaría",
            "english": "Were it to coordinate investments in lithium and copper, South America would negotiate favorably with superpowers."
        },
        {
            "id": "b2-futuro-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["futuro-01-vocab"],
            "pairs": [
                ["prospectiva", "prospective analysis / future forecasting"],
                ["asimetría", "geopolitical asymmetry"],
                ["interdependencia", "interdependence"],
                ["de mediar", "if there were / should there be"]
            ]
        },
        {
            "id": "b2-futuro-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué factor decisivo explica la eclosión global del cine latinoamericano en el siglo XXI?",
            "options": [
                "La copia indiscriminada de las fórmulas comerciales de Hollywood.",
                "La conjunción entre leyes de fomento audiovisual, formación técnica rigurosa y un compromiso insobornable con la memoria histórica y la descolonización de la mirada.",
                "La prohibición de emitir películas extranjeras en los cines nacionales.",
                "El doblaje obligatorio de todas las películas al inglés."
            ],
            "correct": 1
        }
    ],
    "b2-futuro-02": [
        {
            "id": "b2-futuro-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["futuro-concesivas-ponderacion-riesgos"],
            "question": "¿Qué matiz pragmático aporta la locución 'aun a riesgo de' en una toma de decisiones soberana?",
            "options": [
                "Denota cobardía y vacilación ante las amenazas externas.",
                "Expresa la determinación ética y firmeza soberana de actuar asumiendo peligros o costes calculados.",
                "Indica desconocimiento total de los riesgos involucrados.",
                "Equivale a una renuncia incondicional a los objetivos previstos."
            ],
            "correct": 1
        },
        {
            "id": "b2-futuro-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["futuro-concesivas-ponderacion-riesgos"],
            "sentence": "Aun a __ de afrontar litigios arbitrales, los Estados han de salvaguardar las cuencas de agua dulce.",
            "answer": "riesgo",
            "english": "Even at the risk of facing arbitral disputes, States must safeguard fresh water basins."
        },
        {
            "id": "b2-futuro-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["futuro-02-vocab"],
            "pairs": [
                ["si bien", "while / although"],
                ["aun a riesgo de", "even at the risk of"],
                ["salvaguardia", "safeguard"],
                ["soberanía energética", "energy sovereignty"]
            ]
        },
        {
            "id": "b2-futuro-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cómo abordan escritoras contemporáneas como Mariana Enríquez o Samanta Schweblin las problemáticas de la región?",
            "options": [
                "Escribiendo manuales de autoayuda individualista.",
                "Utilizando el terror gótico y el thriller psicológico para explorar los horrores reales de las dictaduras, la desigualdad y la degradación ambiental.",
                "Celebrando el consumismo suntuario de las élites.",
                "Ignorando por completo la realidad sociopolítica de sus países."
            ],
            "correct": 1
        }
    ],
    "b2-futuro-03": [
        {
            "id": "b2-futuro-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["futuro-diplomacia-compromiso-vinculante"],
            "question": "¿Qué modo verbal exige la cláusula subordinada en una resolución diplomática vinculante ('los Estados acuerdan que...')?",
            "options": [
                "Modo subjuntivo preceptivo",
                "Modo indicativo exclusivamente",
                "Infinitivo compuesto únicamente",
                "Modo imperativo directo"
            ],
            "correct": 0
        },
        {
            "id": "b2-futuro-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["futuro-diplomacia-compromiso-vinculante"],
            "sentence": "Los mandatarios acuerdan que se __ una ventanilla única para dinamizar el comercio transfronterizo.",
            "answer": "implemente",
            "english": "The leaders agree that a one-stop window be implemented to energize cross-border trade."
        },
        {
            "id": "b2-futuro-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["futuro-03-vocab"],
            "pairs": [
                ["multilateralismo", "multilateralism"],
                ["vinculante", "binding"],
                ["concertación", "concertation / coordination"],
                ["fondo de contingencia", "contingency fund"]
            ]
        },
        {
            "id": "b2-futuro-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es el desafío cardinal que enfrenta América Latina ante la explotación del litio y los minerales críticos?",
            "options": [
                "Exportar la mayor cantidad de salmuera bruta sin cobrar impuestos.",
                "Superar el modelo extractivista primario mediante cadenas de valor industrial, innovación científica y protección estricta de las cuencas andinas.",
                "Cerrar todas las universidades de ingeniería de la región.",
                "Prohibir el uso de automóviles eléctricos en el continente."
            ],
            "correct": 1
        }
    ],
    "b2-futuro-04": [
        {
            "id": "b2-futuro-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["futuro-relativos-complejos-tratados"],
            "question": "En la frase 'Se creó un tribunal ambiental regional, cuyas sentencias serán vinculantes', ¿con qué concuerda 'cuyas'?",
            "options": [
                "Con el antecedente masculino singular 'tribunal'.",
                "Con el sustantivo femenino plural que le sigue inmediatamente ('sentencias').",
                "Con el verbo 'serán'.",
                "No concuerda con ningún elemento de la oración."
            ],
            "correct": 1
        },
        {
            "id": "b2-futuro-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["futuro-relativos-complejos-tratados"],
            "sentence": "Se aprobó el estatuto de integración, en __ del cual se garantiza la libre circulación de talentos.",
            "answer": "virtud",
            "english": "The integration statute was approved, under which the free circulation of talents is guaranteed."
        },
        {
            "id": "b2-futuro-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["futuro-04-vocab"],
            "pairs": [
                ["en virtud del cual", "under which / by virtue of which"],
                ["cuyo", "whose"],
                ["al amparo del cual", "under the auspices of which"],
                ["unívoco", "unambiguous / unequivocal"]
            ]
        },
        {
            "id": "b2-futuro-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cómo han transformado las juventudes latinoamericanas contemporáneas la práctica de la protesta ciudadana?",
            "options": [
                "Mediante el aislamiento y la desmovilización pasiva en las redes.",
                "Articulando movilizaciones horizontales que combinan arte callejero, música contestataria, demandas feministas y activismo digital en defensa de los bienes comunes.",
                "Exigiendo el retorno a gobiernos dictatoriales del siglo XX.",
                "Clausurando las bibliotecas universitarias públicas."
            ],
            "correct": 1
        }
    ],
    "b2-futuro-05": [
        {
            "id": "b2-futuro-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["futuro-sintesis-estrategica-proyeccion"],
            "question": "¿Qué conector de recapitulación confiere máxima autoridad a la conclusión de un documento estratégico multilateral?",
            "options": [
                "Bueno pues al final",
                "En síntesis / en definitiva / a modo de corolario",
                "Y así quedó la cosa",
                "Como quien dice"
            ],
            "correct": 1
        },
        {
            "id": "b2-futuro-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["futuro-sintesis-estrategica-proyeccion"],
            "sentence": "A modo de __, cabe reafirmar que la unidad en la diversidad es nuestra mayor fortaleza civilizatoria.",
            "answer": "corolario",
            "english": "By way of corollary, it is worth reaffirming that unity in diversity is our greatest civilizatory strength."
        },
        {
            "id": "b2-futuro-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["futuro-05-vocab"],
            "pairs": [
                ["Patria Grande", "concept of a united and integrated Latin America"],
                ["corolario", "corollary / natural deduction or outcome"],
                ["en síntesis", "in synthesis / in summary"],
                ["porvenir", "future horizon"]
            ]
        },
        {
            "id": "b2-futuro-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué horizonte ético y político proyecta América Latina hacia el escenario mundial del siglo XXI?",
            "options": [
                "El sometimiento sumiso a las directrices de una sola potencia militar extranjera.",
                "La construcción de una comunidad solidaria e integrada (la Patria Grande), que aporta al mundo biodiversidad, justicia social, hospitalidad y vocación pacífica.",
                "La parcelación del continente en microestados en disputa permanente.",
                "La renuncia definitiva a los convenios internacionales sobre derechos humanos."
            ],
            "correct": 1
        }
    ],
    "b2-futuro-consolidation": [
        {
            "id": "b2-futuro-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["futuro-prospectiva-hipotesis-complejas"],
            "question": "Identifica la formulación condicional prospectiva con pulcritud gramatical irreprochable:",
            "options": [
                "De consolidarse la libre movilidad ciudadana, la integración regional daría un salto civilizatorio irreversible.",
                "De consolidarse la libre movilidad ciudadana, la integración regional dio un salto ayer.",
                "Si se consolidara la libre movilidad ciudadana, la integración regional daría saltos si acaso.",
                "De consolidando la libre movilidad ciudadana, la integración regional dará un salto."
            ],
            "correct": 0
        },
        {
            "id": "b2-futuro-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["futuro-diplomacia-compromiso-vinculante"],
            "question": "¿Qué enunciado expresa un mandato multilateral vinculante con el régimen verbal preceptivo correcto?",
            "options": [
                "Los cancilleres estipulan que ningún diferendo limítrofe se resuelva mediante el uso de la fuerza.",
                "Los cancilleres estipulan de que ningún diferendo limítrofe se resuelve por la fuerza.",
                "Los cancilleres estipulan que ningún diferendo limítrofe se resolverá obligatoriamente por la fuerza.",
                "Los cancilleres estipulan que ningún diferendo limítrofe se resolvió ayer."
            ],
            "correct": 0
        },
        {
            "id": "b2-futuro-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["futuro-relativos-complejos-tratados"],
            "sentence": "Se creó una corte internacional ambiental, __ sentencias tendrán carácter vinculante e inapelable.",
            "answer": "cuyas",
            "english": "An international environmental court was created, whose rulings will have binding and unappealable status."
        },
        {
            "id": "b2-futuro-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "Al concluir las 72 unidades duales del nivel B2 de español latinoamericano, ¿cuál es el mayor logro formativo del estudiante?",
            "options": [
                "Haber memorizado conjugaciones verbales aisladas sin aplicación práctica.",
                "Haber conquistado una voz propia con fluidez superior, comprensión de la rica diversidad regional y capacidad para dialogar con el alma contemporánea de América Latina.",
                "La capacidad de traducir únicamente textos comerciales básicos con ayuda de un diccionario.",
                "La sustitución de su acento nativo por un dialecto artificial."
            ],
            "correct": 1
        }
    ]
}
