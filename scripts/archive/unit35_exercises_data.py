"""
unit35_exercises_data.py
Exercise sets for Latin American Spanish B2 Unit 35 (Core & Regional),
strictly matching the 4-exercise pattern per lesson.
"""

EXERCISES_DATA = {
    # Core 35
    "b2-35-01": [
        {
            "id": "b2-35-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["registro-nominalizacion-estilo-ensayistico"],
            "question": "¿Qué efecto estilístico produce la nominalización en un ensayo académico formal?",
            "options": [
                "Disminuye la coherencia lógica de las oraciones.",
                "Sintetiza la información, eleva la densidad conceptual y compacta los argumentos.",
                "Obliga al autor a escribir exclusivamente en tiempo pretérito imperfecto.",
                "Elimina la necesidad de usar sustantivos abstractos."
            ],
            "correct": 1
        },
        {
            "id": "b2-35-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["registro-nominalizacion-estilo-ensayistico"],
            "sentence": "La __ paulatina de la soberanía alimentaria demanda políticas agrarias justas y solidarias.",
            "answer": "recuperación",
            "english": "The gradual recovery of food sovereignty demands fair and solidary agrarian policies."
        },
        {
            "id": "b2-35-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-35-01-vocab"],
            "pairs": [
                ["nominalización", "transforming a verb or clause into a noun"],
                ["desarticulación", "dismantling / disruption"],
                ["legitimación", "legitimization"],
                ["abstracción", "abstraction"]
            ]
        },
        {
            "id": "b2-35-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "En 'Los ríos profundos' de José María Arguedas, ¿cómo percibe Ernesto la arquitectura incaica del Cusco?",
            "options": [
                "Como ruinas muertas sin ningún significado espiritual.",
                "Como una fuerza telúrica viva que late y resiste la opresión histórica.",
                "Como un estorbo para el desarrollo urbanístico contemporáneo.",
                "Como una copia imperfecta de los palacios barrocos españoles."
            ],
            "correct": 1
        }
    ],
    "b2-35-02": [
        {
            "id": "b2-35-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["registro-impersonalidad-distanciamiento-discursivo"],
            "question": "¿Cuál de las siguientes construcciones ejemplifica el distanciamiento e impersonalidad en la crónica de opinión?",
            "options": [
                "A mí me parece que los ministros son todos unos incompetentes.",
                "Cabe colegir de los antecedentes recabados que la resolución ministerial carecía de aval técnico.",
                "Yo creo firmemente que se equivocaron.",
                "Nosotros los periodistas no entendemos nada de economía."
            ],
            "correct": 1
        },
        {
            "id": "b2-35-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["registro-impersonalidad-distanciamiento-discursivo"],
            "sentence": "Conviene __ que ninguna autoridad gubernamental desmintió los testimonios documentados.",
            "answer": "puntualizar",
            "english": "It is worth pointing out that no governmental authority denied the documented testimonies."
        },
        {
            "id": "b2-35-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-35-02-vocab"],
            "pairs": [
                ["cabe colegir", "it can be gathered / deduced"],
                ["deontológico", "ethical / related to professional duties"],
                ["fehaciente", "reliable / irrefutable"],
                ["distanciamiento", "distancing / objectivity"]
            ]
        },
        {
            "id": "b2-35-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué rol cumple el trompo mágico ('zumbayllu') en el patio del colegio de Abancay?",
            "options": [
                "Genera apuestas clandestinas entre los profesores.",
                "Suspende las reyertas violentas entre los internos y conecta a Ernesto con la música cósmica andina.",
                "Sirve de proyectil para romper las ventanas del internado.",
                "Es un regalo traído directamente de una feria en París."
            ],
            "correct": 1
        }
    ],
    "b2-35-03": [
        {
            "id": "b2-35-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["registro-marcadores-contraargumentacion-formal"],
            "question": "¿Qué función cumple el conector 'antes bien' en un debate dialéctico riguroso?",
            "options": [
                "Introduce una duda irrelevante.",
                "Introduce una rectificación correctiva que intensifica la afirmación contraria previa.",
                "Marca el cierre definitivo de la sesión sin posibilidad de réplica.",
                "Indica que la acción ocurrió cronológicamente antes del mediodía."
            ],
            "correct": 1
        },
        {
            "id": "b2-35-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["registro-marcadores-contraargumentacion-formal"],
            "sentence": "La gran minería genera ingresos fiscales; en __, compromete de forma irreversible las fuentes hídricas.",
            "answer": "contrapartida",
            "english": "Large-scale mining generates fiscal revenues; on the other hand, it irreversibly compromises water sources."
        },
        {
            "id": "b2-35-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-35-03-vocab"],
            "pairs": [
                ["antes bien", "rather / on the contrary"],
                ["en contrapartida", "in contrast / on the other hand"],
                ["refutación", "rebuttal / refutation"],
                ["antítesis", "antithesis / opposing idea"]
            ]
        },
        {
            "id": "b2-35-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Por qué se sublevan las chicheras lideradas por doña Felipa en 'Los ríos profundos'?",
            "options": [
                "Para exigir la bajada de aranceles al aguardiente importado.",
                "Para recuperar la sal acaparada por comerciantes y repartirla entre los campesinos hambrientos.",
                "Para proclamar la independencia de la ciudad de Abancay.",
                "Para impedir la construcción de una nueva iglesia diocesana."
            ],
            "correct": 1
        }
    ],
    "b2-35-04": [
        {
            "id": "b2-35-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["registro-formulas-protocolarias-correspondencia"],
            "question": "¿Qué fórmula epistolar es habitual en la apertura solemne de un oficio oficial en América Latina?",
            "options": [
                "¡Hola qué tal amigo!",
                "Tengo el honor de dirigirme a Vuestra Excelencia para elevar a su conocimiento el informe adjunto.",
                "Te escribo esta carta rapidito para que sepas qué pasó.",
                "Por la presente te cuento lo siguiente sin vueltas."
            ],
            "correct": 1
        },
        {
            "id": "b2-35-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["registro-formulas-protocolarias-correspondencia"],
            "sentence": "En atención a lo requerido por la comisión, __ remitir los antecedentes procesales legalizados.",
            "answer": "cúmpleme",
            "english": "In attention to what was requested by the commission, it is my duty to forward the legalized procedural background."
        },
        {
            "id": "b2-35-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-35-04-vocab"],
            "pairs": [
                ["cúmpleme", "it is my duty / duty-bound to"],
                ["antecedente", "background / prior record"],
                ["despacho", "official office / dispatch"],
                ["certificar", "to certify / attest officially"]
            ]
        },
        {
            "id": "b2-35-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué representa el río Pachachaca en la vivencia espiritual de Ernesto?",
            "options": [
                "Una frontera infranqueable que divide a la sociedad en dos bandos en guerra eterna.",
                "Una corriente viva de aguas profundas y purificadoras que simboliza la resistencia invencible andina.",
                "Un curso de agua contaminado por desechos industriales sin valor mítico.",
                "Una ruta fluvial para el transporte de mercancías extranjeras."
            ],
            "correct": 1
        }
    ],
    "b2-35-05": [
        {
            "id": "b2-35-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["registro-densidad-lexica-sintesis"],
            "question": "¿Qué estructura sintáctica otorga máxima concisión y ritmo ágil a la síntesis narrativa formal?",
            "options": [
                "El participio absoluto al inicio del período sintáctico ('Concluido el debate...')",
                "El encadenamiento de ocho oraciones coordinadas copulativas con 'y'",
                "La eliminación de todos los verbos de la oración",
                "El uso exclusivo de frases exclamativas breves"
            ],
            "correct": 0
        },
        {
            "id": "b2-35-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["registro-densidad-lexica-sintesis"],
            "sentence": "__ las instancias de mediación previa, las partes recurrieron al arbitraje vinculante.",
            "answer": "Agotadas",
            "english": "Having exhausted prior mediation instances, the parties turned to binding arbitration."
        },
        {
            "id": "b2-35-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-35-05-vocab"],
            "pairs": [
                ["participio absoluto", "absolute participle construction"],
                ["concisión", "conciseness / brevity"],
                ["diáfano", "crystal clear / lucid"],
                ["vínculo jurídico", "legal bond / nexus"]
            ]
        },
        {
            "id": "b2-35-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es la aportación literaria capital de José María Arguedas en 'Los ríos profundos'?",
            "options": [
                "Haber creado una lengua novelesca mestiza capaz de expresar en castellano la poesía y la sintaxis espiritual del quechua.",
                "Haber defendido la abolición total de las lenguas indígenas en el Perú.",
                "Haber escrito la primera novela policial de detectives en Lima.",
                "Haber redactado un manual de agricultura para hacendados feudales."
            ],
            "correct": 0
        }
    ],
    "b2-35-consolidation": [
        {
            "id": "b2-35-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["registro-nominalizacion-estilo-ensayistico"],
            "question": "Selecciona la oración redactada con óptima nominalización y densidad académica:",
            "options": [
                "La desarticulación de las estructuras feudales propició el despertar cívico y la autodeterminación comunitaria.",
                "Porque desarticularon las cosas de los feudales la gente se despertó y se organizó sola.",
                "Cuando ya no hubo feudales todos se pusieron a hacer asambleas comunitarias libres.",
                "El hecho de que cayeran los feudales hizo que la gente tuviera más derechos."
            ],
            "correct": 0
        },
        {
            "id": "b2-35-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["registro-marcadores-contraargumentacion-formal"],
            "question": "¿Qué enunciado emplea correctamente un conector contraargumentativo formal?",
            "options": [
                "El fallo no perjudicó a los campesinos; antes bien, ratificó sus linderos ancestrales.",
                "El fallo no perjudicó a los campesinos; en tanto que ratificó sus linderos.",
                "El fallo no perjudicó a los campesinos; o sea que ratificó sus linderos.",
                "El fallo no perjudicó a los campesinos; por ende que ratificó sus linderos."
            ],
            "correct": 0
        },
        {
            "id": "b2-35-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["registro-formulas-protocolarias-correspondencia"],
            "sentence": "Me permito reiterar a Vuestra Excelencia las seguridades de mi más __ consideración.",
            "answer": "distinguida",
            "english": "I take the liberty of reiterating to Your Excellency the assurances of my most distinguished consideration."
        },
        {
            "id": "b2-35-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "En el desenlace de 'Los ríos profundos', ¿qué catástrofe quiebra el orden señorial en Abancay?",
            "options": [
                "Un terremoto que derriba todas las iglesias barrocas.",
                "Una epidemia devastadora de tifus que hace huir a los hacendados mientras los humildes bajan a orar.",
                "Una inundación marina provocada por un maremoto en el Pacífico.",
                "Una erupción volcánica que cubre de ceniza los valles."
            ],
            "correct": 1
        }
    ],

    # Regional 35 (Pluralismo)
    "b2-pluralismo-01": [
        {
            "id": "b2-pluralismo-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["pluralismo-concesivas-oposicion-reivindicativa"],
            "question": "¿Qué matiz semántico aporta la locución concesiva 'a despecho de' frente al neutro 'a pesar de'?",
            "options": [
                "Denota sumisión resignada ante el poder establecido.",
                "Enfatiza un desafío firme, perseverancia moral y triunfo de la acción sobre un entorno hostil.",
                "Indica que el sujeto ignoraba la existencia de leyes.",
                "Expresa arrepentimiento por haber iniciado una protesta."
            ],
            "correct": 1
        },
        {
            "id": "b2-pluralismo-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["pluralismo-concesivas-oposicion-reivindicativa"],
            "sentence": "A __ de las presiones de las corporaciones mineras, la comunidad mantuvo la defensa del río.",
            "answer": "despecho",
            "english": "In spite of the pressures from mining corporations, the community maintained the defense of the river."
        },
        {
            "id": "b2-pluralismo-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["pluralismo-01-vocab"],
            "pairs": [
                ["a despecho de", "in spite of / in defiance of"],
                ["autodeterminación", "self-determination"],
                ["aculturación", "acculturation / forced cultural assimilation"],
                ["inalienable", "inalienable / non-transferable"]
            ]
        },
        {
            "id": "b2-pluralismo-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué estipula el Convenio 169 de la OIT sobre los proyectos que afectan tierras indígenas?",
            "options": [
                "La venta forzosa de los territorios colectivos a la banca privada.",
                "La obligación imperativa de realizar una consulta libre, previa e informada con las comunidades.",
                "La disolución de los concejos comunales de ancianos.",
                "La prohibición de enseñar idiomas originarios en las escuelas."
            ],
            "correct": 1
        }
    ],
    "b2-pluralismo-02": [
        {
            "id": "b2-pluralismo-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["pluralismo-relativas-preposicionales-institucionales"],
            "question": "¿Cuál es la formulación correcta con relativa preposicional en el ámbito normativo?",
            "options": [
                "Se consagró un régimen autonómico, con arreglo al cual las comunidades eligen a sus autoridades.",
                "Se consagró un régimen autonómico, con arreglo al que las comunidades eligen sus autoridades.",
                "Se consagró un régimen autonómico, con arreglo en el que las comunidades eligen autoridades.",
                "Se consagró un régimen autonómico, según que las comunidades eligen sus autoridades."
            ],
            "correct": 0
        },
        {
            "id": "b2-pluralismo-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["pluralismo-relativas-preposicionales-institucionales"],
            "sentence": "El Convenio 169 de la OIT, al __ del cual se realiza la consulta previa, posee jerarquía constitucional.",
            "answer": "amparo",
            "english": "ILO Convention 169, under the protection of which prior consultation is held, possesses constitutional hierarchy."
        },
        {
            "id": "b2-pluralismo-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["pluralismo-02-vocab"],
            "pairs": [
                ["al amparo de", "under the protection of"],
                ["con arreglo a", "in accordance with / pursuant to"],
                ["deslinde", "demarcation / jurisdictional boundary"],
                ["consuetudinario", "customary / based on unwritten tradition"]
            ]
        },
        {
            "id": "b2-pluralismo-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué principio medular guía las resoluciones de la justicia comunitaria andina?",
            "options": [
                "El encarcelamiento solitario de máxima seguridad.",
                "La reparación del daño tangible, la sanación colectiva y el restablecimiento del equilibrio comunitario.",
                "El cobro de honorarios en lingotes de oro a los campesinos.",
                "La imposición de penas de destierro definitivo al extranjero."
            ],
            "correct": 1
        }
    ],
    "b2-pluralismo-03": [
        {
            "id": "b2-pluralismo-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["pluralismo-formulas-reconocimiento-constitucional"],
            "question": "¿Qué modo verbal rigen las matrices declarativas constitucionales de principio ('la Constitución consagra que...')?",
            "options": [
                "Modo subjuntivo preceptivo",
                "Modo indicativo exclusivamente",
                "Participio pasivo",
                "Gerundio de posterioridad"
            ],
            "correct": 0
        },
        {
            "id": "b2-pluralismo-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["pluralismo-formulas-reconocimiento-constitucional"],
            "sentence": "La Constitución consagra que todos los pueblos originarios __ de autonomía territorial y gobierno propio.",
            "answer": "gocen",
            "english": "The Constitution establishes that all indigenous peoples shall enjoy territorial autonomy and self-government."
        },
        {
            "id": "b2-pluralismo-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["pluralismo-03-vocab"],
            "pairs": [
                ["biocéntrico", "biocentric / life-centered"],
                ["sujeto de derechos", "subject of legal rights"],
                ["cuenca hidrográfica", "hydrographic river basin"],
                ["remediación", "environmental remediation / cleanup"]
            ]
        },
        {
            "id": "b2-pluralismo-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué organismo colegiado tutela los derechos del río Atrato tras la Sentencia T-622 en Colombia?",
            "options": [
                "Una empresa multinacional de ingeniería portuaria.",
                "El cuerpo colegiado de guardianes del río Atrato, integrado por delegados del Estado y líderes comunitarios.",
                "Un tribunal militar de alta montaña.",
                "La Cámara de Comercio de Bogotá exclusivamente."
            ],
            "correct": 1
        }
    ],
    "b2-pluralismo-04": [
        {
            "id": "b2-pluralismo-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["pluralismo-causales-explicativas-jurisprudencia"],
            "question": "¿Cuál de los siguientes nexos causales se utiliza habitualmente en la fundamentación judicial formal?",
            "options": [
                "Porque sí nomás",
                "Habida cuenta de que / toda vez que",
                "O sea que",
                "Como que"
            ],
            "correct": 1
        },
        {
            "id": "b2-pluralismo-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["pluralismo-causales-explicativas-jurisprudencia"],
            "sentence": "Se suspendieron las faenas mineras, __ vez que no se había convocado la consulta previa vinculante.",
            "answer": "toda",
            "english": "Mining works were suspended, inasmuch as the binding prior consultation had not been convened."
        },
        {
            "id": "b2-pluralismo-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["pluralismo-04-vocab"],
            "pairs": [
                ["habida cuenta de que", "taking into account that"],
                ["toda vez que", "inasmuch as / since"],
                ["bilingüismo aditivo", "additive bilingualism"],
                ["revitalización", "linguistic revitalization"]
            ]
        },
        {
            "id": "b2-pluralismo-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué innovación pedagógica define a la Educación Intercultural Bilingüe moderna?",
            "options": [
                "La castellanización forzosa mediante castigos corporales.",
                "El aprendizaje cognitivo en la lengua materna originaria complementado con el castellano y saberes ancestrales.",
                "La eliminación de todas las clases de matemáticas y ciencias.",
                "La sustitución de los profesores rurales por software extranjero no adaptado."
            ],
            "correct": 1
        }
    ],
    "b2-pluralismo-05": [
        {
            "id": "b2-pluralismo-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["pluralismo-perifrasis-obligacion-estatutaria"],
            "question": "¿Qué valor confiere la perífrasis 'haber de + infinitivo' en los tratados internacionales de derechos humanos?",
            "options": [
                "Una sugerencia opcional sin consecuencias vinculantes.",
                "Un mandato estatutario formal o deber convencional de inexcusable cumplimiento.",
                "Una acción que se completó en el pasado remoto.",
                "Una duda sobre la soberanía territorial de los Estados."
            ],
            "correct": 1
        },
        {
            "id": "b2-pluralismo-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["pluralismo-perifrasis-obligacion-estatutaria"],
            "sentence": "Los Estados parte __ de implementar mecanismos eficaces de protección para las lideresas ambientales.",
            "answer": "han",
            "english": "States parties are to implement effective protection mechanisms for women environmental leaders."
        },
        {
            "id": "b2-pluralismo-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["pluralismo-05-vocab"],
            "pairs": [
                ["haber de", "to have to / bound to by statute"],
                ["ecofeminismo", "ecofeminism / community environmental feminism"],
                ["lideresa", "female leader / grassroots woman leader"],
                ["cautelar", "preventive / protective measure"]
            ]
        },
        {
            "id": "b2-pluralismo-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es la aportación cardinal del Acuerdo de Escazú ratificado en 2021?",
            "options": [
                "La privatización de todos los bosques tropicales de la cuenca amazónica.",
                "La consagración de medidas vinculantes y garantías judiciales para la protección de personas defensoras del medio ambiente.",
                "La eliminación de las licencias ambientales en el sector minero.",
                "El cierre de los juzgados agrarios en zonas indígenas."
            ],
            "correct": 1
        }
    ],
    "b2-pluralismo-consolidation": [
        {
            "id": "b2-pluralismo-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["pluralismo-concesivas-oposicion-reivindicativa"],
            "question": "Identifica la oración redactada con la locución concesiva de registro solemne correcta:",
            "options": [
                "A despecho de las presiones corporativas, la comunidad sostuvo la defensa irrenunciable del río.",
                "A despecho que las presiones corporativas existieran, la comunidad sostuvo la defensa del río.",
                "A despecho por las presiones corporativas, la comunidad sostuvo la defensa del río.",
                "En despecho de las presiones corporativas, la comunidad sostuvo la defensa del río."
            ],
            "correct": 0
        },
        {
            "id": "b2-pluralismo-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["pluralismo-formulas-reconocimiento-constitucional"],
            "question": "¿Qué enunciado expresa un mandato de rango constitucional con el modo verbal apropiado?",
            "options": [
                "Es postulado innegociable que la Naturaleza sea reconocida formalmente como sujeto de derechos.",
                "Es postulado innegociable que la Naturaleza es reconocida formalmente como sujeto de derechos.",
                "Es postulado innegociable de que la Naturaleza sea reconocida como sujeto de derechos.",
                "Es postulado innegociable que la Naturaleza será reconocida como sujeto de derechos."
            ],
            "correct": 0
        },
        {
            "id": "b2-pluralismo-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["pluralismo-relativas-preposicionales-institucionales"],
            "sentence": "Se acordó un protocolo interjurisdiccional, en __ del cual jueces ordinarios y autoridades comunales cooperan.",
            "answer": "virtud",
            "english": "An interjurisdictional protocol was agreed upon, in virtue of which ordinary judges and communal authorities cooperate."
        },
        {
            "id": "b2-pluralismo-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué síntesis fundamental proyecta la experiencia del pluralismo jurídico hacia el siglo XXI?",
            "options": [
                "Que la coexistencia armónica de la justicia estatal y los saberes ancestrales fortalece la dignidad democrática y el cuidado planetario.",
                "Que todas las leyes nacionales deben ser sustituidas por códigos militares.",
                "Que la protección ambiental impide el crecimiento económico de las ciudades.",
                "Que los tratados de derechos humanos son incompatibles con el derecho consuetudinario."
            ],
            "correct": 0
        }
    ]
}
