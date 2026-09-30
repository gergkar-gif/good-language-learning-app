"""
unit33_exercises_data.py
Exercise sets for Latin American Spanish B2 Unit 33 (Core & Regional),
strictly matching the 4-exercise pattern per lesson.
"""

EXERCISES_DATA = {
    # Core 33
    "b2-33-01": [
        {
            "id": "b2-33-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["condicionales-a-condicion-con-tal"],
            "question": "¿Qué modo verbal exige de forma invariable la locución 'a condición de que' en la subordinada?",
            "options": [
                "Modo indicativo exclusivamente",
                "Modo subjuntivo",
                "Infinitivo simple únicamente",
                "Modo imperativo"
            ],
            "correct": 1
        },
        {
            "id": "b2-33-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["condicionales-a-condicion-con-tal"],
            "sentence": "Suscribiremos el tratado comercial a condición de que se __ las cláusulas arancelarias acordadas.",
            "answer": "respeten",
            "english": "We will sign the trade treaty on condition that the agreed tariff clauses are respected."
        },
        {
            "id": "b2-33-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-33-01-vocab"],
            "pairs": [
                ["a condición de que", "on condition that"],
                ["con tal de que", "provided that"],
                ["estipulación", "stipulation"],
                ["vinculante", "binding"]
            ]
        },
        {
            "id": "b2-33-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "En 'Rayuela' de Julio Cortázar, ¿qué actitud muestra Horacio Oliveira frente a las certezas burguesas?",
            "options": [
                "Aceptación sumisa de las normas sociales parisinas.",
                "Escepticismo radical e hiperlucidez racional que le impiden entregarse a la vida espontánea.",
                "Entusiasmo comercial por enriquecerse en la banca.",
                "Devoción religiosa a los dogmas escolásticos tradicionales."
            ],
            "correct": 1
        }
    ],
    "b2-33-02": [
        {
            "id": "b2-33-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["condicionales-salvedad-exclusion"],
            "question": "¿Cuál de las siguientes locuciones de salvedad condicional nunca admite el modo indicativo?",
            "options": [
                "Salvo que",
                "A menos que",
                "Excepto que",
                "Siempre que"
            ],
            "correct": 1
        },
        {
            "id": "b2-33-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["condicionales-salvedad-exclusion"],
            "sentence": "Las tarifas preferenciales no se aplicarán, a menos que la empresa __ el origen regional de sus insumos.",
            "answer": "demuestre",
            "english": "Preferential tariffs will not apply, unless the enterprise proves the regional origin of its inputs."
        },
        {
            "id": "b2-33-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-33-02-vocab"],
            "pairs": [
                ["a menos que", "unless"],
                ["salvo que", "except that"],
                ["salvedad", "qualification"],
                ["eximente", "exemption"]
            ]
        },
        {
            "id": "b2-33-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué representa la figura de Lucía, 'La Maga', en contraste con Oliveira en 'Rayuela'?",
            "options": [
                "Una sabiduría intuitiva, poética y directa que desafía los pedantes silogismos de Horacio.",
                "Una profesora de lógica aristotélica en la Sorbona.",
                "Una agente de aduanas que vigila a los inmigrantes sudamericanos.",
                "Una médica cirujana en un hospital público de París."
            ],
            "correct": 0
        }
    ],
    "b2-33-03": [
        {
            "id": "b2-33-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["condicionales-gerundio-de-infinitivo"],
            "question": "¿A qué estructura oracional equivale exactamente la fórmula 'De haber mediado arbitraje'?",
            "options": [
                "Si hubiera mediado arbitraje",
                "Cuando mediare arbitraje",
                "Aunque medió arbitraje",
                "Puesto que medió arbitraje"
            ],
            "correct": 0
        },
        {
            "id": "b2-33-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["condicionales-gerundio-de-infinitivo"],
            "sentence": "De no __ advertido las discrepancias a tiempo, los ministros habrían firmado un acuerdo lesivo.",
            "answer": "haber",
            "english": "Had they not noticed the discrepancies in time, the ministers would have signed a harmful agreement."
        },
        {
            "id": "b2-33-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-33-03-vocab"],
            "pairs": [
                ["de haber mediado", "had there been mediation"],
                ["actuando así", "by acting thus"],
                ["corolario", "corollary"],
                ["conjeturar", "to conjecture"]
            ]
        },
        {
            "id": "b2-33-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué acontecimiento trágico desencadena la ruptura entre Oliveira y La Maga en París?",
            "options": [
                "El robo de un manuscrito en el Barrio Latino.",
                "La muerte silenciosa del pequeño Rocamadour en la buhardilla durante una reunión del Club.",
                "La quiebra de una galería de arte moderno.",
                "Un duelo a espada en las orillas del Sena."
            ],
            "correct": 1
        }
    ],
    "b2-33-04": [
        {
            "id": "b2-33-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["condicionales-como-no-advertencia"],
            "question": "¿Qué valor discursivo añade la construcción 'como no + subjuntivo' en comparación con 'si no'?",
            "options": [
                "Un matiz de cortesía deferente",
                "Un matiz enfático de advertencia, admonición o amenaza de consecuencias perjudiciales",
                "Una duda retórica sin consecuencias",
                "Un agradecimiento formal protocolar"
            ],
            "correct": 1
        },
        {
            "id": "b2-33-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["condicionales-como-no-advertencia"],
            "sentence": "Como no __ pronto en la disputa fronteriza, el litigio llegará a tribunales internacionales.",
            "answer": "intervengan",
            "english": "Unless they intervene soon in the border dispute, the litigation will reach international courts."
        },
        {
            "id": "b2-33-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-33-04-vocab"],
            "pairs": [
                ["como no intervengas", "unless you intervene"],
                ["admonición", "admonition"],
                ["apercibimiento", "formal warning"],
                ["inminente", "imminent"]
            ]
        },
        {
            "id": "b2-33-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿En qué consiste el episodio del tablón entre ventanas en la sección bonaerense de 'Rayuela'?",
            "options": [
                "En una fuga de presidiarios a través de los techos.",
                "En una escena absurda donde Oliveira, Traveler y Talita tienden una madera para pasarse yerba mate y clavos.",
                "En un recital de poesía vanguardista sobre la avenida Corrientes.",
                "En la construcción de un escenario para un circo ecuestre."
            ],
            "correct": 1
        }
    ],
    "b2-33-05": [
        {
            "id": "b2-33-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["desiderativas-contrafacticas-ponderativas"],
            "question": "¿Qué tiempo verbal exige 'ojalá' para manifestar una lamentación contrafáctica sobre el pasado?",
            "options": [
                "Presente de indicativo",
                "Pluscuamperfecto de subjuntivo",
                "Futuro simple",
                "Condicional simple"
            ],
            "correct": 1
        },
        {
            "id": "b2-33-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["desiderativas-contrafacticas-ponderativas"],
            "sentence": "¡Quién __ desandar el tiempo y evitar aquel desacuerdo fundacional entre las dos repúblicas!",
            "answer": "pudiera",
            "english": "Would that one could retrace time and avert that foundational disagreement between the two republics!"
        },
        {
            "id": "b2-33-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-33-05-vocab"],
            "pairs": [
                ["quién pudiera", "would that one could"],
                ["ojalá hubiera", "if only there had been"],
                ["añoranza", "yearning"],
                ["quimera", "chimera"]
            ]
        },
        {
            "id": "b2-33-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es el postulado central de la 'contranovela' teorizada por Morelli en 'Rayuela'?",
            "options": [
                "Imitar fielmente la estructura del melodrama decimonónico.",
                "Demoler las fórmulas burguesas gastadas del lenguaje para activar al lector como cocreador cómplice.",
                "Escribir exclusivamente manuales técnicos de gramática normativa.",
                "Prohibir la traducción de novelas extranjeras a América Latina."
            ],
            "correct": 1
        }
    ],
    "b2-33-consolidation": [
        {
            "id": "b2-33-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["condicionales-a-condicion-con-tal"],
            "question": "Selecciona la oración redactada con pulcritud normativa formal:",
            "options": [
                "Firmarán el pacto a condición de que se respeten los aranceles vigentes.",
                "Firmarán el pacto a condición que se respeten los aranceles vigentes.",
                "Firmarán el pacto a condición de que se respetan los aranceles vigentes.",
                "Firmarán el pacto con tal que respetan los aranceles vigentes."
            ],
            "correct": 0
        },
        {
            "id": "b2-33-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["condicionales-salvedad-exclusion"],
            "question": "¿Qué enunciado expresa correctamente una salvedad condicional con modo subjuntivo?",
            "options": [
                "El acuerdo entrará en vigor el mes próximo, a menos que un socio lo vete.",
                "El acuerdo entrará en vigor el mes próximo, a menos que un socio lo veta.",
                "El acuerdo entrará en vigor el mes próximo, a menos de que un socio lo veta.",
                "El acuerdo entrará en vigor el mes próximo, a menos que un socio lo vetará."
            ],
            "correct": 0
        },
        {
            "id": "b2-33-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["condicionales-gerundio-de-infinitivo"],
            "sentence": "De haber __ las advertencias de los diplomáticos, no se habría desatado el litigio arancelario.",
            "answer": "escuchado",
            "english": "Had they listened to the diplomats' warnings, the tariff dispute would not have broken out."
        },
        {
            "id": "b2-33-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Por qué califica Julio Cortázar de 'contranovela' a su obra cumbre 'Rayuela'?",
            "options": [
                "Porque narra la vida secreta de los contrabandistas de alcohol en el Caribe.",
                "Porque subvierte la lectura pasiva lineal y rompe las convenciones sintácticas de la novela realista tradicional.",
                "Porque está escrita enteramente en dialecto lunfardo porteño sin signos de puntuación.",
                "Porque fue prohibida por todos los tribunales de justicia de América del Sur."
            ],
            "correct": 1
        }
    ],
    # Regional 33 (Integración)
    "b2-integracion-01": [
        {
            "id": "b2-integracion-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["integracion-formulas-restrictivas-alcance"],
            "question": "¿Qué modo verbal rige 'en la medida en que' cuando formula una condición hipotética o sujeta a negociación?",
            "options": [
                "Modo subjuntivo",
                "Modo indicativo exclusivamente",
                "Infinitivo compuesto obligatorio",
                "Modo imperativo"
            ],
            "correct": 0
        },
        {
            "id": "b2-integracion-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["integracion-formulas-restrictivas-alcance"],
            "sentence": "El comercio intrazona se expandirá en la medida en que los socios __ sus tributos aduaneros.",
            "answer": "armonicen",
            "english": "Intra-zone commerce will expand to the extent that partners harmonize their customs taxes."
        },
        {
            "id": "b2-integracion-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["integracion-01-vocab"],
            "pairs": [
                ["arancel común", "common external tariff"],
                ["asimetría", "asymmetry"],
                ["convergencia", "convergence"],
                ["desgravación", "tariff reduction"]
            ]
        },
        {
            "id": "b2-integracion-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué tratado fundacional de 1991 dio origen formal al Mercado Común del Sur (Mercosur)?",
            "options": [
                "El Tratado de Montevideo de 1980.",
                "El Tratado de Asunción, firmado por Argentina, Brasil, Paraguay y Uruguay.",
                "El Protocolo de Ushuaia de 1998.",
                "El Acuerdo de Cartagena de 1969."
            ],
            "correct": 1
        }
    ],
    "b2-integracion-02": [
        {
            "id": "b2-integracion-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["integracion-condicionales-inversion-enfasis"],
            "question": "¿Qué valor sintáctico imprime la construcción 'así + subjuntivo' en 'así cueste el doble'?",
            "options": [
                "Finalidad premeditada",
                "Concesión enfática o determinación irrenunciable equivalente a 'por más que cueste'",
                "Causa real pasada",
                "Consecuencia indeseada"
            ],
            "correct": 1
        },
        {
            "id": "b2-integracion-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["integracion-condicionales-inversion-enfasis"],
            "sentence": "Completaremos la interconexión de las bolsas de valores, así __ años de reformas normativas.",
            "answer": "requiera",
            "english": "We will complete the interconnection of stock exchanges, even if it requires years of regulatory reforms."
        },
        {
            "id": "b2-integracion-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["integracion-02-vocab"],
            "pairs": [
                ["cadena de valor", "value chain"],
                ["homologación", "standardization"],
                ["pragmático", "pragmatic"],
                ["bursátil", "securities-related"]
            ]
        },
        {
            "id": "b2-integracion-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué plataforma financiera transfronteriza crearon las bolsas de Chile, Colombia, México y Perú?",
            "options": [
                "El Banco Central del Sur.",
                "El Mercado Integrado Latinoamericano (MILA).",
                "La Corporación Andina de Fomento.",
                "El Fondo Monetario del Pacífico."
            ],
            "correct": 1
        }
    ],
    "b2-integracion-03": [
        {
            "id": "b2-integracion-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["integracion-consecutivas-intensivas"],
            "question": "¿Qué modo verbal sigue a 'de tal suerte que' cuando introduce una consecuencia real consumada?",
            "options": [
                "Modo subjuntivo exclusivamente",
                "Modo indicativo",
                "Infinitivo obligatorio",
                "Modo imperativo"
            ],
            "correct": 1
        },
        {
            "id": "b2-integracion-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["integracion-consecutivas-intensivas"],
            "sentence": "Dragaron la dársena de Chancay, de tal suerte que los portacontenedores de gran calado __ sin dificultad.",
            "answer": "atracan",
            "english": "They dredged the Chancay basin, such that large draft container ships dock without difficulty."
        },
        {
            "id": "b2-integracion-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["integracion-03-vocab"],
            "pairs": [
                ["paso cordillerano", "mountain pass"],
                ["bioceánico", "bioceanic"],
                ["calado", "draft"],
                ["megapuerto", "mega-port"]
            ]
        },
        {
            "id": "b2-integracion-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué ventaja logística decisiva ofrece el megapuerto de Chancay para las exportaciones suramericanas?",
            "options": [
                "Exclusividad para embarcaciones pesqueras artesanales de madera.",
                "Conexión directa transpacífica hacia Asia con aguas profundas, reduciendo la travesía a veinticinco días.",
                "Clausura de todas las conexiones ferroviarias con el interior.",
                "Cobro de peaje obligatorio en lingotes de oro a los buques extranjeros."
            ],
            "correct": 1
        }
    ],
    "b2-integracion-04": [
        {
            "id": "b2-integracion-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["integracion-modales-correspondencia"],
            "question": "¿Qué relación sintáctica expresa la locución modal 'a medida que' entre dos magnitudes dinámicas?",
            "options": [
                "Causa única determinante",
                "Progresión o correspondencia simultánea y proporcional",
                "Exclusión condicional categórica",
                "Finalidad contractual estricta"
            ],
            "correct": 1
        },
        {
            "id": "b2-integracion-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["integracion-modales-correspondencia"],
            "sentence": "A medida que __ la demanda en São Paulo, la central de Itaipú eleva el despacho de sus turbinas.",
            "answer": "crece",
            "english": "As demand in São Paulo grows, the Itaipú plant elevates the dispatch of its turbines."
        },
        {
            "id": "b2-integracion-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["integracion-04-vocab"],
            "pairs": [
                ["represa binacional", "binational dam"],
                ["hidroelectricidad", "hydroelectricity"],
                ["excedente", "surplus"],
                ["gasoducto", "gas pipeline"]
            ]
        },
        {
            "id": "b2-integracion-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuáles son las dos colosales centrales hidroeléctricas binacionales situadas sobre el río Paraná?",
            "options": [
                "Guri y Caruachi.",
                "Itaipú (Brasil-Paraguay) y Yacyretá (Argentina-Paraguay).",
                "Salto Grande y El Chocón.",
                "Tres Gargantas y Asuán."
            ],
            "correct": 1
        }
    ],
    "b2-integracion-05": [
        {
            "id": "b2-integracion-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["integracion-desiderativas-institucionales"],
            "question": "¿Qué modo verbal rige obligatoriamente la fórmula institucional 'es menester que'?",
            "options": [
                "Modo subjuntivo",
                "Modo indicativo",
                "Gerundio simple",
                "Condicional compuesto"
            ],
            "correct": 0
        },
        {
            "id": "b2-integracion-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["integracion-desiderativas-institucionales"],
            "sentence": "Es menester que los Estados miembros __ plenamente los derechos laborales de los trabajadores migrantes.",
            "answer": "garanticen",
            "english": "It is necessary that member States fully guarantee the labor rights of migrant workers."
        },
        {
            "id": "b2-integracion-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["integracion-05-vocab"],
            "pairs": [
                ["libre tránsito", "free transit"],
                ["convalidación", "validation of degrees"],
                ["acuerdo migratorio", "migration accord"],
                ["supranacional", "supranational"]
            ]
        },
        {
            "id": "b2-integracion-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué beneficio esencial otorga el Acuerdo sobre Residencia del Mercosur a los ciudadanos suramericanos?",
            "options": [
                "Exención vitalicia del pago de servicios públicos en su país natal.",
                "Derecho a radicarse temporal y permanentemente con plenas garantías laborales, educativas y de salud en los países partes.",
                "Obligación de incorporarse al servicio diplomático extranjero.",
                "Prohibición de enviar remesas económicas a sus familiares."
            ],
            "correct": 1
        }
    ],
    "b2-integracion-consolidation": [
        {
            "id": "b2-integracion-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["integracion-formulas-restrictivas-alcance"],
            "question": "Identifica la opción gramaticalmente correcta en registro culto formal:",
            "options": [
                "La unión aduanera avanzará en la medida en que los socios armonicen sus políticas fiscales.",
                "La unión aduanera avanzará en la medida que los socios armonizan sus políticas fiscales.",
                "La unión aduanera avanzará a la medida en que los socios armonicen sus políticas fiscales.",
                "La unión aduanera avanzará de la medida que los socios armonicen sus políticas fiscales."
            ],
            "correct": 0
        },
        {
            "id": "b2-integracion-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["integracion-condicionales-inversion-enfasis"],
            "question": "¿Qué oración formula una determinación enfática inquebrantable mediante 'así + subjuntivo'?",
            "options": [
                "Completaremos el corredor bioceánico, así cueste el doble del presupuesto inicial.",
                "Completaremos el corredor bioceánico, así cuesta el doble del presupuesto inicial.",
                "Completaremos el corredor bioceánico, así costará el doble del presupuesto inicial.",
                "Completaremos el corredor bioceánico, así costó el doble del presupuesto inicial."
            ],
            "correct": 0
        },
        {
            "id": "b2-integracion-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["integracion-consecutivas-intensivas"],
            "sentence": "Diseñaron las redes eléctricas de tal suerte que __ las caídas de tensión durante el invierno.",
            "answer": "evitaron",
            "english": "They designed the electrical grids in such a way that they averted voltage drops during the winter."
        },
        {
            "id": "b2-integracion-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es la síntesis de complementariedad que define la integración suramericana contemporánea?",
            "options": [
                "La clausura total de las rutas fluviales a favor de ferrocarriles privados.",
                "La convergencia entre la capacidad productiva del Mercosur y la apertura bioceánica transpacífica de la Alianza del Pacífico.",
                "La prohibición absoluta de intercambiar estudiantes y profesionales entre repúblicas hermanas.",
                "La venta de todas las represas hidroeléctricas a monopolios del hemisferio norte."
            ],
            "correct": 1
        }
    ]
}
