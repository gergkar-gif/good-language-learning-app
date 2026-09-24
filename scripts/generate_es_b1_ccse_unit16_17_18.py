#!/usr/bin/env python3
"""Generate Spain Citizenship (CCSE) Units 16, 17, and 18 for es-es B1 track."""

from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict

UNITS_16_17_18 = [
    # =========================================================================
    # UNIT 16: Garantías Constitucionales y el Defensor del Pueblo (unit_num=52, b1-garantias)
    # =========================================================================
    {
        "slug": "garantias",
        "unit_num": 52,
        "title": "Garantías Constitucionales y el Defensor del Pueblo",
        "description": "El Defensor del Pueblo, tutela judicial efectiva y recurso de amparo, estados de alarma, excepción y sitio, teléfono 060 y defensa de los consumidores.",
        "Badge": "Garantías y Defensor",
        "lessons": [
            {
                "num": "01",
                "Title": "El Defensor del Pueblo: Alto Comisionado de las Cortes",
                "title": "El Defensor del Pueblo: Alto Comisionado de las Cortes",
                "grammar_slug": "alto-comisionado-designado-por",
                "story_slug": "defensor",
                "story_title": "Un puente gratuito entre el ciudadano y la Administración: el Defensor del Pueblo",
                "objectives": [
                    "Comprender el artículo 54 CE: el Defensor del Pueblo como alto comisionado de las Cortes Generales.",
                    "Saber que cualquier ciudadano o residente puede acudir gratuitamente al Defensor del Pueblo para presentar una queja frente a la Administración.",
                    "Practicar las construcciones «alto comisionado de las Cortes Generales» y «supervisar la actividad de la Administración»."
                ],
                "vocab": [
                    {"lemma": "el Defensor del Pueblo", "pos": "noun", "translation": "Ombudsman"},
                    {"lemma": "el alto comisionado", "pos": "noun", "translation": "high commissioner"},
                    {"lemma": "supervisar la actividad", "pos": "verb", "translation": "to supervise the activity"},
                    {"lemma": "presentar una queja", "pos": "verb", "translation": "to file a complaint"},
                    {"lemma": "dar cuenta a las Cortes", "pos": "verb", "translation": "to report to the Cortes Generales"},
                    {"lemma": "la actuación administrativa", "pos": "noun", "translation": "administrative action"},
                    {"lemma": "el mandato de cinco años", "pos": "noun", "translation": "five-year term of office"},
                    {"lemma": "el informe anual", "pos": "noun", "translation": "annual report"}
                ],
                "grammar_title": "Definición institucional: «alto comisionado designado por las Cortes Generales»",
                "grammar_text": "El artículo 54 de la Constitución define al **Defensor del Pueblo** con precisión técnica: **«Una ley orgánica regulará la institución del Defensor del Pueblo, como alto comisionado de las Cortes Generales, designado por estas para la defensa de los derechos comprendidos en este Título, a cuyo efecto podrá supervisar la actividad de la Administración, dando cuenta a las Cortes Generales»**.",
                "grammar_examples": [
                    {"es": "El Defensor del Pueblo es el alto comisionado de las Cortes Generales para defender los derechos de los ciudadanos.", "en": "The Ombudsman is the high commissioner of the Cortes Generales to defend citizens' rights."},
                    {"es": "Cualquier persona puede presentar una queja gratuita ante el Defensor del Pueblo sin necesidad de abogado.", "en": "Anyone can file a free complaint with the Ombudsman without needing a lawyer."}
                ],
                "grammar_tip": "Pregunta estrella del CCSE: ¿De quién depende el Defensor del Pueblo y a quién rinde cuentas? A las Cortes Generales (Congreso y Senado), que lo eligen por un mandato de 5 años.",
                "paragraphs": [
                    "¿Qué puede hacer un ciudadano cuando una oficina pública tarda meses sin motivo en resolver su expediente, cuando un hospital o un ayuntamiento vulnera sus derechos o cuando siente que la Administración actúa de manera injusta? Para evitar que la persona se sienta desprotegida frente a la maquinaria del Estado, el artículo 54 de la Constitución Española creó la figura del Defensor del Pueblo.",
                    "La Constitución lo define como el «alto comisionado de las Cortes Generales», designado por el Congreso de los Diputados y el Senado por una mayoría muy amplia (tres quintos de cada Cámara) para un mandato de cinco años. No recibe órdenes del Gobierno ni de ningún ministerio: actúa con total independencia e imparcialidad y da cuenta de su labor directamente a las Cortes Generales mediante un informe anual.",
                    "Su misión principal es la defensa de los derechos y libertades comprendidos en el Título I de la Constitución, para lo cual supervisa la actividad de todas las administraciones públicas (estatal, autonómica y municipal). Además, el Defensor del Pueblo está legitimado para interponer recursos de inconstitucionalidad y recursos de amparo ante el Tribunal Constitucional.",
                    "Una de sus grandes virtudes es su accesibilidad: cualquier persona física o jurídica, sin importar su nacionalidad, su edad (incluso los menores de edad) ni su lugar de residencia, puede dirigirse al Defensor del Pueblo para presentar una queja firmada. Todos sus trámites son completamente gratuitos y no se necesita ni abogado ni procurador.",
                    "Junto al Defensor del Pueblo estatal (con sede en Madrid), muchas comunidades autónomas cuentan con instituciones autonómicas equivalentes que colaboran estrechamente con él, como el Síndic de Greuges en Cataluña y la Comunidad Valenciana, el Ararteko en el País Vasco, el Valedor do Pobo en Galicia, el Justicia de Aragón o el Defensor del Pueblo Andaluz."
                ],
                "questions": [
                    {
                        "question": "Según el artículo 54 de la Constitución Española, ¿qué institución designa al Defensor del Pueblo y ante quién da cuenta de su gestión?",
                        "options": [
                            "Las Cortes Generales (Congreso de los Diputados y Senado)",
                            "El Banco Central Europeo",
                            "El Ministerio de Hacienda",
                            "Las cámaras de comercio provinciales"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Defensor del Pueblo es el alto comisionado de las Cortes Generales, designado por ellas y ante quienes da cuenta."
                    },
                    {
                        "question": "¿Cuál es la función principal del Defensor del Pueblo?",
                        "options": [
                            "Defender los derechos fundamentales de los ciudadanos supervisando la actividad de la Administración",
                            "Recaudar el Impuesto sobre el Valor Añadido (IVA)",
                            "Dirigir la política exterior y militar del Gobierno",
                            "Imponer multas de tráfico en las carreteras"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 54 CE le encomienda la defensa de los derechos del Título I supervisando la actividad de la Administración."
                    },
                    {
                        "question": "¿Cuánto cuesta presentar una queja ante el Defensor del Pueblo en España?",
                        "options": [
                            "Es un trámite totalmente gratuito y no requiere abogado ni procurador",
                            "Cuesta 300 euros de tasa obligatoria",
                            "Exige contratar a tres abogados mercantiles",
                            "Solo pueden presentarla los diputados y senadores"
                        ],
                        "correctIndex": 0,
                        "explanation": "Todas las actuaciones del Defensor del Pueblo son gratuitas para el ciudadano y no requieren abogado."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Por cuántos años es elegido el Defensor del Pueblo por las Cortes Generales?",
                        "options": [
                            "Por 5 años",
                            "Por 2 años",
                            "De forma vitalicia",
                            "Por 10 meses"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Ley Orgánica del Defensor del Pueblo establece un mandato de cinco años."
                    },
                    {
                        "prompt": "¿Puede el Defensor del Pueblo presentar un recurso de inconstitucionalidad o de amparo ante el Tribunal Constitucional?",
                        "options": [
                            "Sí, está expresamente legitimado por la Constitución para interponer ambos recursos",
                            "No, tiene prohibido acudir al Tribunal Constitucional",
                            "Solo puede hacerlo en años bisiestos",
                            "Solo si lo autoriza un alcalde"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 162 CE legitima al Defensor del Pueblo para interponer recursos de inconstitucionalidad y de amparo."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El Defensor del Pueblo es el alto ___ de las Cortes Generales para defender los derechos ciudadanos.",
                        "answer": "comisionado",
                        "options": ["comisionado", "empadronado", "recaudador", "concejal"],
                        "explanation": "El artículo 54 CE lo define como el «alto comisionado de las Cortes Generales».",
                        "english": "The Ombudsman is the high commissioner of the Cortes Generales to defend citizens' rights."
                    },
                    {
                        "sentence": "Para defender los derechos del Título I, el Defensor del Pueblo supervisa la actividad de la ___.",
                        "answer": "Administración",
                        "options": ["Administración", "Meteorología", "Cinematografía", "Gastronomía"],
                        "explanation": "El Defensor del Pueblo supervisa la actividad de la Administración dando cuenta a las Cortes.",
                        "english": "To defend the rights of Title I, the Ombudsman supervises the activity of the Administration."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Defensor del Pueblo es el alto comisionado de las Cortes Generales y supervisa la actividad de la Administración.",
                    "english": "The Ombudsman is the high commissioner of the Cortes Generales and supervises the activity of the Administration."
                },
                "ex_sb": {
                    "words": ["Cualquier", "ciudadano", "puede", "presentar", "una", "queja", "gratuita", "ante", "el", "Defensor", "del", "Pueblo."],
                    "english": "Any citizen can file a free complaint with the Ombudsman."
                }
            },
            {
                "num": "02",
                "Title": "Tutela Judicial Efectiva y Recurso de Amparo",
                "title": "Tutela Judicial Efectiva y Recurso de Amparo",
                "grammar_slug": "sin-que-pueda-producirse-indefension",
                "story_slug": "amparo",
                "story_title": "Presunción de inocencia, justicia gratuita y la última puerta de amparo",
                "objectives": [
                    "Comprender el artículo 24 CE: derecho a la tutela judicial efectiva, prohibición de la indefensión y presunción de inocencia.",
                    "Conocer la asistencia jurídica gratuita (turno de oficio) y el recurso de amparo ante el Tribunal Constitucional (Art. 53.2 CE).",
                    "Practicar las construcciones «sin que, en ningún caso, pueda producirse indefensión» y «recabar la tutela mediante el recurso de amparo»."
                ],
                "vocab": [
                    {"lemma": "la tutela judicial efectiva", "pos": "noun", "translation": "effective judicial protection"},
                    {"lemma": "la indefensión", "pos": "noun", "translation": "defenselessness / lack of legal defense"},
                    {"lemma": "la presunción de inocencia", "pos": "noun", "translation": "presumption of innocence"},
                    {"lemma": "la asistencia jurídica gratuita", "pos": "noun", "translation": "free legal aid"},
                    {"lemma": "el abogado de oficio", "pos": "noun", "translation": "court-appointed public defender"},
                    {"lemma": "el recurso de amparo", "pos": "noun", "translation": "constitutional appeal for protection of fundamental rights"},
                    {"lemma": "agotar la vía judicial", "pos": "verb", "translation": "to exhaust ordinary judicial remedies"},
                    {"lemma": "el proceso público sin dilaciones", "pos": "noun", "translation": "public trial without undue delays"}
                ],
                "grammar_title": "Garantías procesales: «sin que, en ningún caso, pueda producirse indefensión»",
                "grammar_text": "El artículo 24.1 de la Constitución garantiza que todas las personas tienen derecho a obtener la **tutela efectiva de los jueces y tribunales** en el ejercicio de sus derechos e intereses legítimos, **«sin que, en ningún caso, pueda producirse indefensión»**.",
                "grammar_examples": [
                    {"es": "Todas las personas tienen derecho a la tutela efectiva de los jueces, sin que en ningún caso pueda producirse indefensión.", "en": "All persons have the right to effective protection from judges, without defenselessness occurring in any case."},
                    {"es": "La justicia será gratuita cuando así lo disponga la ley y respecto de quienes acrediten insuficiencia de recursos para litigar.", "en": "Justice shall be free when so provided by law and for those who prove insufficient resources to litigate."}
                ],
                "grammar_tip": "Recuerda para el CCSE: si quien acude a los tribunales carece de recursos económicos suficientes, el artículo 119 CE garantiza la asistencia jurídica gratuita (abogado de oficio).",
                "paragraphs": [
                    "De nada serviría que una Constitución enumerase decenas de derechos si un ciudadano no pudiera defenderlos ante un juez independiente cuando alguien los vulnera. Por eso el artículo 24 de la Constitución Española consagra el derecho fundamental más invocado en los tribunales españoles: todas las personas tienen derecho a obtener la tutela efectiva de los jueces y tribunales en el ejercicio de sus derechos e intereses legítimos, sin que, en ningún caso, pueda producirse indefensión.",
                    "El segundo apartado del artículo 24 reúne las garantías del proceso justo: todos tienen derecho al juez ordinario predeterminado por la ley, a la defensa y a la asistencia de letrado, a ser informados de la acusación formulada contra ellos, a un proceso público sin dilaciones indebidas y con todas las garantías, a utilizar los medios de prueba pertinentes, a no declarar contra sí mismos, a no confesarse culpables y a la presunción de inocencia.",
                    "¿Y qué ocurre si una persona necesita defenderse en un juicio pero no tiene dinero para pagar a un abogado? El artículo 119 de la Constitución responde con claridad: la justicia será gratuita cuando así lo disponga la ley y, en todo caso, respecto de quienes acrediten insuficiencia de recursos para litigar. Los Colegios de Abogados organizan en toda España el «turno de oficio» y el servicio de asistencia jurídica gratuita.",
                    "Además, el artículo 53 de la Constitución establece un sistema reforzado de garantías para los derechos más importantes. Si tras acudir a los tribunales ordinarios (agotando la vía judicial previa) un ciudadano considera que un poder público ha vulnerado su derecho a la igualdad (artículo 14), sus derechos fundamentales (artículos 15 a 29) o su objeción de conciencia (artículo 30.2), dispone de un remedio extraordinario.",
                    "Ese remedio es el recurso de amparo constitucional, que se presenta ante el Tribunal Constitucional. A través del recurso de amparo, el máximo intérprete de la Constitución puede anular cualquier acto administrativo o sentencia que haya lesionado un derecho fundamental y restablecer al ciudadano en la integridad de su derecho."
                ],
                "questions": [
                    {
                        "question": "¿Qué garantiza el artículo 119 de la Constitución Española a las personas que acrediten insuficiencia de recursos económicos para litigar en un juicio?",
                        "options": [
                            "La asistencia jurídica gratuita (justicia gratuita y abogado de oficio)",
                            "La exención perpetua de cumplir las leyes de tráfico",
                            "Un puesto vitalicio en el Consejo General del Poder Judicial",
                            "El cierre inmediato del juzgado"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 119 CE garantiza que la justicia será gratuita para quienes acrediten insuficiencia de recursos para litigar."
                    },
                    {
                        "question": "¿Ante qué órgano se presenta el recurso de amparo cuando se vulneran los derechos fundamentales de los artículos 14 a 29 de la Constitución?",
                        "options": [
                            "Ante el Tribunal Constitucional",
                            "Ante el Ayuntamiento del municipio",
                            "Ante el Banco de España",
                            "Ante la Agencia Tributaria"
                        ],
                        "correctIndex": 0,
                        "explanation": "El recurso de amparo se interpone ante el Tribunal Constitucional tras agotar la vía judicial ordinaria."
                    },
                    {
                        "question": "Según el artículo 24 de la Constitución, ¿cómo se considera a toda persona acusada de un delito mientras no se demuestre su culpabilidad en un juicio con todas las garantías?",
                        "options": [
                            "Se le garantiza la presunción de inocencia",
                            "Se la considera culpable desde el primer minuto",
                            "Pierde su nacionalidad de origen",
                            "Tiene obligación de confesarse culpable"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 24.2 CE garantiza el derecho fundamental a la presunción de inocencia."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué prohíbe expresamente el artículo 24.1 de la Constitución al garantizar la tutela judicial efectiva?",
                        "options": [
                            "Que pueda producirse indefensión en ningún caso",
                            "Que los ciudadanos contraten abogados",
                            "Que las sentencias sean motivadas",
                            "Que existan recursos de apelación"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 24.1 CE garantiza la tutela judicial efectiva «sin que, en ningún caso, pueda producirse indefensión»."
                    },
                    {
                        "prompt": "¿Está obligado un ciudadano en España a declarar contra sí mismo o a confesarse culpable en un proceso penal?",
                        "options": [
                            "No, el artículo 24.2 reconoce el derecho a no declarar contra sí mismos y a no confesarse culpables",
                            "Sí, siempre que se lo pida un vecino",
                            "Sí, en todos los juicios civiles",
                            "Solo los martes y jueves"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 24.2 CE garantiza el derecho a no declarar contra sí mismo y a no confesarse culpable."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Todas las personas tienen derecho a la tutela judicial efectiva, sin que pueda producirse ___.",
                        "answer": "indefensión",
                        "options": ["indefensión", "progresividad", "cooficialidad", "abdicación"],
                        "explanation": "«Sin que, en ningún caso, pueda producirse indefensión» (Art. 24.1 CE).",
                        "english": "All persons have the right to effective judicial protection, without defenselessness occurring."
                    },
                    {
                        "sentence": "El recurso de ___ ante el Tribunal Constitucional protege los derechos fundamentales de los artículos 14 a 29.",
                        "answer": "amparo",
                        "options": ["amparo", "tráfico", "catastro", "consumo"],
                        "explanation": "El recurso de amparo (Art. 53.2 CE) protege los derechos fundamentales ante el Tribunal Constitucional.",
                        "english": "The appeal for constitutional protection (amparo) before the Constitutional Court protects the fundamental rights of Articles 14 to 29."
                    }
                ],
                "ex_dict": {
                    "audioText": "La justicia será gratuita respecto de quienes acrediten insuficiencia de recursos para litigar.",
                    "english": "Justice shall be free for those who prove insufficient resources to litigate."
                },
                "ex_sb": {
                    "words": ["Todas", "las", "personas", "tienen", "derecho", "a", "la", "presunción", "de", "inocencia."],
                    "english": "All persons have the right to the presumption of innocence."
                }
            },
            {
                "num": "03",
                "Title": "Estados de Alarma, de Excepción y de Sitio",
                "title": "Estados de Alarma, de Excepción y de Sitio",
                "grammar_slug": "previa-autorizacion-dando-cuenta-al-congreso",
                "story_slug": "estados",
                "story_title": "El artículo 116: cómo responde una democracia ante las emergencias sin perder el control parlamentario",
                "objectives": [
                    "Distinguir con exactitud los tres estados del artículo 116 CE: estado de alarma, estado de excepción y estado de sitio.",
                    "Saber quién declara cada uno y por cuánto tiempo: alarma (Gobierno por decreto hasta 15 días, prórroga autorizada por el Congreso), excepción (Gobierno con previa autorización del Congreso, hasta 30 días) y sitio (mayoría absoluta del Congreso a propuesta del Gobierno).",
                    "Dominar las expresiones «por un plazo máximo de quince días» y «previa autorización del Congreso de los Diputados»."
                ],
                "vocab": [
                    {"lemma": "el estado de alarma", "pos": "noun", "translation": "state of alarm"},
                    {"lemma": "el estado de excepción", "pos": "noun", "translation": "state of emergency / exception"},
                    {"lemma": "el estado de sitio", "pos": "noun", "translation": "state of siege / martial law"},
                    {"lemma": "el decreto acordado en Consejo de Ministros", "pos": "noun", "translation": "decree approved by the Council of Ministers"},
                    {"lemma": "la prórroga", "pos": "noun", "translation": "extension (of a deadline)"},
                    {"lemma": "la previa autorización", "pos": "noun", "translation": "prior authorization"},
                    {"lemma": "la crisis sanitaria", "pos": "noun", "translation": "health crisis"},
                    {"lemma": "la disolución del Congreso", "pos": "noun", "translation": "dissolution of Congress"}
                ],
                "grammar_title": "Control parlamentario de emergencias: «dando cuenta al Congreso» frente a «previa autorización»",
                "grammar_text": "El artículo 116 de la Constitución gradúa la intervención del **Congreso de los Diputados** según la gravedad de la emergencia: el **estado de alarma** lo declara el Gobierno por decreto (máximo 15 días), **dando cuenta al Congreso**, sin cuya autorización no podrá ser prorrogado; el **estado de excepción** lo declara el Gobierno **previa autorización del Congreso**; y el **estado de sitio** lo declara el propio **Congreso por mayoría absoluta**.",
                "grammar_examples": [
                    {"es": "El estado de alarma será declarado por el Gobierno mediante decreto por un plazo máximo de quince días.", "en": "The state of alarm shall be declared by the Government by decree for a maximum period of fifteen days."},
                    {"es": "Mientras estén declarados los estados del artículo 116, no podrá procederse a la disolución del Congreso.", "en": "While the states of Article 116 are declared, the dissolution of Congress may not proceed."}
                ],
                "grammar_tip": "Diferencia clave para el examen CCSE: el estado de alarma lo declara inicialmente el Gobierno (por un máximo de 15 días), pero cualquier prórroga necesita la autorización del Congreso de los Diputados.",
                "paragraphs": [
                    "Toda democracia constitucional puede enfrentarse en algún momento de su historia a catástrofes naturales, epidemias graves, paralizaciones de servicios esenciales o amenazas contra su soberanía. Para que el Estado pueda actuar con eficacia sin caer jamás en la arbitrariedad, el artículo 116 de la Constitución Española regula tres situaciones extraordinarias: los estados de alarma, de excepción y de sitio.",
                    "El primero y más leve es el estado de alarma, previsto para catástrofes o desgracias públicas (como terremotos, inundaciones o crisis sanitarias como la pandemia de 2020) o paralización de servicios públicos esenciales. Lo declara el Gobierno mediante decreto acordado en Consejo de Ministros por un plazo máximo de quince días, dando cuenta inmediatamente al Congreso de los Diputados; sin la autorización expresa del Congreso, ese plazo no puede ser prorrogado.",
                    "El segundo escalón es el estado de excepción, pensado para alteraciones gravísimas del libre ejercicio de los derechos y libertades o del normal funcionamiento de las instituciones democráticas que no puedan resolverse por los medios ordinarios. Aquí el Gobierno no puede declararlo por sí solo: necesita la previa autorización del Congreso de los Diputados, y su duración no podrá exceder de treinta días, prorrogables por otro plazo igual con los mismos requisitos.",
                    "El tercer y más grave nivel es el estado de sitio, reservado para el caso de que se produzca o amenace producirse una insurrección o acto de fuerza contra la soberanía o independencia de España, su integridad territorial o el ordenamiento constitucional. El estado de sitio no lo declara el Gobierno, sino directamente el Congreso de los Diputados por mayoría absoluta, a propuesta exclusiva del Gobierno.",
                    "Para blindar la democracia en los momentos más difíciles, el artículo 116 establece dos garantías fundamentales: mientras esté declarado cualquiera de estos tres estados no podrá procederse a la disolución del Congreso, y el funcionamiento de los poderes constitucionales del Estado no podrá interrumpirse."
                ],
                "questions": [
                    {
                        "question": "¿Quién declara inicialmente el estado de alarma en España y por qué plazo máximo antes de necesitar autorización del Congreso para su prórroga?",
                        "options": [
                            "El Gobierno mediante decreto acordado en Consejo de Ministros, por un plazo máximo de 15 días",
                            "Los alcaldes de las capitales de provincia, por un plazo de dos años",
                            "El Tribunal de Cuentas, por seis meses",
                            "La Real Academia Española, de forma indefinida"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 116.2 CE dispone que el Gobierno declara el estado de alarma por un máximo de 15 días, necesitando autorización del Congreso para prorrogarlo."
                    },
                    {
                        "question": "¿Qué órgano declara el estado de sitio en España según el artículo 116.4 de la Constitución?",
                        "options": [
                            "El Congreso de los Diputados por mayoría absoluta, a propuesta exclusiva del Gobierno",
                            "El Ministerio de Agricultura sin consultar a las Cortes",
                            "Cualquier comisaría de policía",
                            "Las diputaciones provinciales"
                        ],
                        "correctIndex": 0,
                        "explanation": "El estado de sitio es declarado por la mayoría absoluta del Congreso de los Diputados a propuesta exclusiva del Gobierno."
                    },
                    {
                        "question": "¿Se puede disolver el Congreso de los Diputados mientras esté vigente un estado de alarma, de excepción o de sitio?",
                        "options": [
                            "No, el artículo 116.5 prohíbe expresamente disolver el Congreso mientras estén declarados",
                            "Sí, queda disuelto automáticamente el primer día",
                            "Sí, si lo pide un concejal",
                            "Solo en los meses de invierno"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 116.5 CE establece que no podrá procederse a la disolución del Congreso mientras estén declarados los estados de alarma, excepción o sitio."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuáles son los tres estados extraordinarios regulados en el artículo 116 de la Constitución Española?",
                        "options": [
                            "Los estados de alarma, de excepción y de sitio",
                            "Los estados de primavera, verano y otoño",
                            "Los estados municipal, provincial y comarcal",
                            "Los estados civil, mercantil y laboral"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 116 CE regula los estados de alarma, de excepción y de sitio."
                    },
                    {
                        "prompt": "¿Qué requisito previo necesita el Gobierno para poder declarar el estado de excepción?",
                        "options": [
                            "La previa autorización del Congreso de los Diputados",
                            "El permiso de los bancos privados",
                            "Un sorteo público municipal",
                            "Ninguno, puede declararlo por cinco años sin consultar a nadie"
                        ],
                        "correctIndex": 0,
                        "explanation": "Según el artículo 116.3 CE, el estado de excepción requiere la previa autorización del Congreso de los Diputados."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El estado de ___ es declarado por el Gobierno mediante decreto por un plazo máximo de quince días.",
                        "answer": "alarma",
                        "options": ["alarma", "bienestar", "autonomía", "derecho"],
                        "explanation": "El estado de alarma tiene un plazo inicial máximo de 15 días (Art. 116.2 CE).",
                        "english": "The state of alarm is declared by the Government by decree for a maximum period of fifteen days."
                    },
                    {
                        "sentence": "Para prorrogar el estado de alarma más allá de quince días es indispensable la autorización del ___ de los Diputados.",
                        "answer": "Congreso",
                        "options": ["Congreso", "Ayuntamiento", "Consulado", "Museo"],
                        "explanation": "Sin la autorización del Congreso de los Diputados, el estado de alarma no puede ser prorrogado.",
                        "english": "To extend the state of alarm beyond fifteen days, the authorization of the Congress of Deputies is indispensable."
                    }
                ],
                "ex_dict": {
                    "audioText": "El estado de alarma es declarado por el Gobierno por un plazo máximo de quince días.",
                    "english": "The state of alarm is declared by the Government for a maximum period of fifteen days."
                },
                "ex_sb": {
                    "words": ["La", "Constitución", "regula", "los", "estados", "de", "alarma,", "de", "excepción", "y", "de", "sitio."],
                    "english": "The Constitution regulates the states of alarm, exception, and siege."
                }
            },
            {
                "num": "04",
                "Title": "Transparencia, Administración Electrónica y Teléfono 060",
                "title": "Transparencia, Administración Electrónica y Teléfono 060",
                "grammar_slug": "realizar-tramites-a-traves-de",
                "story_slug": "transparencia",
                "story_title": "El teléfono 060, el sistema Cl@ve y el BOE: la Administración a un clic",
                "objectives": [
                    "Recordar el número de teléfono 060 de información de la Administración General del Estado.",
                    "Identificar el Portal de la Transparencia, el Boletín Oficial del Estado (BOE) y los medios de identificación electrónica (DNIe, Certificado Digital y sistema Cl@ve).",
                    "Practicar las expresiones «realizar trámites por vía telemática» y «entrar en vigor tras su publicación en el BOE»."
                ],
                "vocab": [
                    {"lemma": "el teléfono 060", "pos": "noun", "translation": "060 State Administration citizen information phone line"},
                    {"lemma": "el Boletín Oficial del Estado (BOE)", "pos": "noun", "translation": "Official State Gazette"},
                    {"lemma": "el Portal de la Transparencia", "pos": "noun", "translation": "Transparency Portal"},
                    {"lemma": "la administración electrónica", "pos": "noun", "translation": "e-government / electronic administration"},
                    {"lemma": "el sistema Cl@ve", "pos": "noun", "translation": "Cl@ve digital identification system"},
                    {"lemma": "el certificado digital", "pos": "noun", "translation": "digital certificate (FNMT)"},
                    {"lemma": "la Carpeta Ciudadana", "pos": "noun", "translation": "Citizen Folder (online portal)"},
                    {"lemma": "por vía telemática", "pos": "adverb", "translation": "online / electronically"}
                ],
                "grammar_title": "Lenguaje administrativo y digital: «a través del teléfono 060» y «publicarse en el BOE»",
                "grammar_text": "Para describir la relación entre los ciudadanos y las oficinas públicas españolas, se utilizan locuciones instrumentales como **«a través de»**, **«por vía telemática»** y **«mediante el sistema Cl@ve»**: *Los ciudadanos pueden obtener información sobre trámites y empleo público a través del **teléfono 060** o del portal administracion.gob.es*.",
                "grammar_examples": [
                    {"es": "El teléfono 060 ofrece información administrativa general sobre los servicios de la Administración General del Estado.", "en": "The 060 telephone line offers general administrative information about the services of the General State Administration."},
                    {"es": "Las leyes aprobadas por las Cortes Generales se publican en el Boletín Oficial del Estado (BOE).", "en": "Laws passed by the Cortes Generales are published in the Official State Gazette (BOE)."}
                ],
                "grammar_tip": "No confundas en el examen CCSE los números de tres cifras: 112 (emergencias), 016 (violencia de género), 091 (Policía Nacional), 062 (Guardia Civil) y 060 (información de la Administración General del Estado).",
                "paragraphs": [
                    "En el examen CCSE es muy importante distinguir los números telefónicos públicos de tres cifras que existen en España. Si una persona no sufre una urgencia médica ni policial, sino que necesita información administrativa sobre cómo renovar el pasaporte, solicitar una beca, pedir cita previa en un organismo público o consultar convocatorias de empleo público estatal, debe marcar el número 060.",
                    "El teléfono 060 es el servicio oficial de atención e información al ciudadano de la Administración General del Estado, complementado en internet por el Punto de Acceso General (administracion.gob.es). A través de él, cualquier residente puede orientarse dentro de los ministerios y organismos públicos sin tener que desplazarse físicamente de ventanilla en ventanilla.",
                    "Además, España cuenta con una de las administraciones electrónicas más avanzadas de Europa. Gracias al DNI electrónico (DNIe), al Certificado Digital de la Fábrica Nacional de Moneda y Timbre (FNMT) y al sistema Cl@ve (Cl@ve PIN y Cl@ve Permanente), los ciudadanos pueden realizar trámites por vía telemática las 24 horas del día: desde descargar un certificado de empadronamiento o la vida laboral hasta presentar la declaración de la Renta.",
                    "La aplicación y web «Mi Carpeta Ciudadana» reúne en un solo lugar las notificaciones pendientes, los títulos educativos, los puntos del carné de conducir de la DGT, los bienes inmuebles y las citas previas del ciudadano.",
                    "Por último, dos herramientas garantizan la publicidad de las normas y el control ciudadano: el Boletín Oficial del Estado (BOE), diario oficial de consulta pública y gratuita donde deben publicarse todas las leyes, reales decretos y convocatorias oficiales para que entren en vigor, y el Portal de la Transparencia, donde se publican los contratos públicos, las subvenciones y las retribuciones de los altos cargos."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es el número de teléfono de información administrativa general para el ciudadano sobre los servicios y trámites de la Administración General del Estado?",
                        "options": ["060", "112", "016", "062"],
                        "correctIndex": 0,
                        "explanation": "El 060 es el teléfono oficial de información administrativa de la Administración General del Estado."
                    },
                    {
                        "question": "¿En qué diario oficial del Estado deben publicarse las leyes y los reales decretos en España para que entren en vigor y sean conocidos por todos?",
                        "options": [
                            "En el Boletín Oficial del Estado (BOE)",
                            "En el Diario Deportivo Nacional",
                            "En el Catálogo de Museos",
                            "En la Guía Telefónica Provincial"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Boletín Oficial del Estado (BOE) es el diario oficial en el que se publican las leyes, disposiciones y actos de inserción obligatoria."
                    },
                    {
                        "question": "¿Cómo se llama el sistema público de identificación electrónica que permite a los ciudadanos realizar trámites por internet ante la Administración española mediante código PIN o contraseña?",
                        "options": [
                            "El sistema Cl@ve (junto al Certificado Digital y el DNIe)",
                            "El sistema Schengen",
                            "El sistema D'Hondt",
                            "El sistema CERA"
                        ],
                        "correctIndex": 0,
                        "explanation": "Cl@ve es el sistema de identificación electrónica de las administraciones públicas españolas."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué portal público permite a cualquier ciudadano consultar los presupuestos, contratos públicos y sueldos de los altos cargos del Estado?",
                        "options": [
                            "El Portal de la Transparencia",
                            "El Registro de la Propiedad Intelectual",
                            "La taquilla del Teatro Real",
                            "El censo de vehículos históricos"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Portal de la Transparencia garantiza el derecho de acceso a la información pública."
                    },
                    {
                        "prompt": "¿Qué significan las siglas BOE en la vida jurídica y administrativa española?",
                        "options": [
                            "Boletín Oficial del Estado",
                            "Banco de Operaciones Exteriores",
                            "Brigada de Orden Especial",
                            "Biblioteca de Obras Españolas"
                        ],
                        "correctIndex": 0,
                        "explanation": "BOE significa Boletín Oficial del Estado."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El teléfono ___ ofrece información al ciudadano sobre los trámites de la Administración General del Estado.",
                        "answer": "060",
                        "options": ["060", "016", "112", "091"],
                        "explanation": "El 060 es el número de información de la Administración General del Estado.",
                        "english": "The 060 phone line offers information to citizens about the procedures of the General State Administration."
                    },
                    {
                        "sentence": "Todas las leyes aprobadas por las Cortes Generales se publican en el Boletín Oficial del ___ (BOE).",
                        "answer": "Estado",
                        "options": ["Estado", "Deporte", "Turismo", "Comercio"],
                        "explanation": "BOE son las siglas del Boletín Oficial del Estado.",
                        "english": "All laws approved by the Cortes Generales are published in the Official State Gazette (BOE)."
                    }
                ],
                "ex_dict": {
                    "audioText": "El teléfono cero sesenta ofrece información sobre los trámites de la Administración General del Estado.",
                    "english": "The zero-sixty telephone line offers information about the procedures of the General State Administration."
                },
                "ex_sb": {
                    "words": ["Las", "leyes", "entran", "en", "vigor", "tras", "su", "publicación", "en", "el", "Boletín", "Oficial", "del", "Estado."],
                    "english": "Laws enter into force after their publication in the Official State Gazette."
                }
            },
            {
                "num": "05",
                "Title": "Defensa de los Consumidores y Usuarios",
                "title": "Defensa de los Consumidores y Usuarios",
                "grammar_slug": "hoja-de-reclamaciones-garantia-legal",
                "story_slug": "consumo",
                "story_title": "La hoja de reclamaciones, el ticket de compra y los tres años de garantía",
                "objectives": [
                    "Comprender el artículo 51 CE sobre la defensa de los consumidores y usuarios.",
                    "Conocer la obligatoriedad de las hojas de reclamaciones en los establecimientos, el plazo de garantía legal de 3 años para productos nuevos y el derecho de desistimiento de 14 días en compras por internet.",
                    "Practicar las expresiones «solicitar la hoja de reclamaciones» y «contar con una garantía legal de tres años»."
                ],
                "vocab": [
                    {"lemma": "el consumidor y usuario", "pos": "noun", "translation": "consumer and user"},
                    {"lemma": "la hoja de reclamaciones", "pos": "noun", "translation": "official complaint form"},
                    {"lemma": "la garantía legal", "pos": "noun", "translation": "legal warranty"},
                    {"lemma": "el derecho de desistimiento", "pos": "noun", "translation": "right of withdrawal (cooling-off period)"},
                    {"lemma": "la OMIC (Oficina Municipal de Información al Consumidor)", "pos": "noun", "translation": "Municipal Consumer Information Office"},
                    {"lemma": "el Sistema Arbitral de Consumo", "pos": "noun", "translation": "Consumer Arbitration System"},
                    {"lemma": "el etiquetado claro", "pos": "noun", "translation": "clear product labeling"},
                    {"lemma": "el comprobante o factura de compra", "pos": "noun", "translation": "receipt or purchase invoice"}
                ],
                "grammar_title": "Derechos de compra y consumo: «solicitar la hoja de reclamaciones»",
                "grammar_text": "El artículo 51 de la Constitución ordena a los poderes públicos garantizar la **defensa de los consumidores y usuarios**, protegiendo mediante procedimientos eficaces su seguridad, su salud y sus legítimos intereses económicos. En la práctica diaria, todo establecimiento comercial está obligado a tener a disposición del cliente **«hojas de reclamaciones»** oficiales.",
                "grammar_examples": [
                    {"es": "Todos los establecimientos comerciales están obligados a facilitar al cliente la hoja de reclamaciones cuando la solicite.", "en": "All commercial establishments are obliged to provide the customer with the official complaint form when requested."},
                    {"es": "En España los bienes de consumo nuevos cuentan con una garantía legal de tres años desde su entrega.", "en": "In Spain new consumer goods have a legal warranty of three years from their delivery."}
                ],
                "grammar_tip": "Recuerda para el CCSE: todos los comercios y restaurantes en España tienen obligación de disponer de hojas de reclamaciones oficiales para los consumidores.",
                "paragraphs": [
                    "Comprar un electrodoméstico, contratar una tarifa de internet, comer en un restaurante o reservar un billete de tren son actos cotidianos protegidos por la Constitución Española. El artículo 51 establece que los poderes públicos garantizarán la defensa de los consumidores y usuarios, protegiendo, mediante procedimientos eficaces, la seguridad, la salud y los legítimos intereses económicos de los mismos.",
                    "Además, ese mismo artículo encomienda a los poderes públicos promover la información y la educación de los consumidores y usuarios, fomentar sus organizaciones (como las asociaciones de consumidores presentes en toda España) y oírlas en las cuestiones que puedan afectarles.",
                    "¿Qué herramientas concretas tiene un ciudadano en España cuando surge un problema con una compra o un servicio? La primera es conservar siempre el tique, recibo o factura de compra, indispensable para ejercer la garantía. Desde 2022, la legislación española amplió el plazo de garantía legal de todos los productos nuevos de consumo duradero (como teléfonos, ordenadores, lavadoras o automóviles) a tres años desde la fecha de entrega.",
                    "Si la compra se ha realizado a distancia —por ejemplo, por internet o por teléfono—, el consumidor disfruta del derecho de desistimiento: dispone de un plazo mínimo de 14 días naturales para devolver el producto sin necesidad de justificar su decisión y sin penalización.",
                    "Cuando un cliente considera que un comercio, hotel o restaurante ha vulnerado sus derechos, puede solicitar en el propio local la hoja de reclamaciones oficial (cuya tenencia y entrega son obligatorias en todos los establecimientos). Una copia queda en el comercio y otra se entrega en la Oficina Municipal de Información al Consumidor (OMIC) o en la Dirección General de Consumo de la comunidad autónoma, pudiendo resolverse el conflicto de manera rápida y gratuita a través del Sistema Arbitral de Consumo."
                ],
                "questions": [
                    {
                        "question": "¿Qué documento oficial están obligados a tener todos los comercios y establecimientos abiertos al público en España para que el cliente pueda formular una queja?",
                        "options": [
                            "La hoja de reclamaciones",
                            "El padrón electoral",
                            "El libro de sesiones del Senado",
                            "La carta náutica"
                        ],
                        "correctIndex": 0,
                        "explanation": "Todos los establecimientos comerciales en España tienen la obligación legal de disponer de hojas de reclamaciones y entregarlas al consumidor que las solicite."
                    },
                    {
                        "question": "¿Cuál es actualmente el plazo general de la garantía legal para los productos nuevos de consumo en España?",
                        "options": [
                            "3 años desde la entrega del producto",
                            "15 días desde la compra",
                            "3 meses únicamente",
                            "No existe garantía obligatoria por ley"
                        ],
                        "correctIndex": 0,
                        "explanation": "La normativa española de defensa de los consumidores establece una garantía legal de 3 años para los bienes nuevos."
                    },
                    {
                        "question": "¿Qué oficina de los ayuntamientos asesora gratuitamente a los vecinos sobre sus derechos como compradores y tramita sus reclamaciones de consumo?",
                        "options": [
                            "La OMIC (Oficina Municipal de Información al Consumidor)",
                            "La Jefatura Provincial de Tráfico",
                            "La Capitanía Marítima",
                            "La Confederación Hidrográfica"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las OMIC (Oficinas Municipales de Información al Consumidor) informan y ayudan gratuitamente a los ciudadanos en materia de consumo."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿De cuántos días naturales dispone como mínimo un consumidor en España para ejercer su derecho de desistimiento en una compra por internet?",
                        "options": [
                            "De 14 días naturales",
                            "De 1 solo día",
                            "De 2 horas",
                            "Están prohibidas las devoluciones en internet"
                        ],
                        "correctIndex": 0,
                        "explanation": "El derecho legal de desistimiento en compras a distancia o por internet es de un mínimo de 14 días naturales."
                    },
                    {
                        "prompt": "¿Qué artículo de la Constitución Española encomienda a los poderes públicos la defensa de los consumidores y usuarios?",
                        "options": [
                            "El artículo 51",
                            "El artículo 3",
                            "El artículo 66",
                            "El artículo 159"
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 51 CE garantiza la defensa de los consumidores y usuarios."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Si un cliente no recibe una atención correcta en un comercio, puede solicitar la ___ de reclamaciones.",
                        "answer": "hoja",
                        "options": ["hoja", "urna", "beca", "tasa"],
                        "explanation": "La hoja de reclamaciones es obligatoria en todos los establecimientos comerciales.",
                        "english": "If a customer does not receive proper service in a shop, they can request the official complaint form."
                    },
                    {
                        "sentence": "En España, los productos nuevos de consumo cuentan con una ___ legal de tres años.",
                        "answer": "garantía",
                        "options": ["garantía", "censura", "legislatura", "regencia"],
                        "explanation": "La garantía legal de los productos nuevos en España es de 3 años.",
                        "english": "In Spain, new consumer products come with a three-year legal warranty."
                    }
                ],
                "ex_dict": {
                    "audioText": "Todos los establecimientos comerciales están obligados a disponer de hojas de reclamaciones para los consumidores.",
                    "english": "All commercial establishments are obliged to have official complaint forms available for consumers."
                },
                "ex_sb": {
                    "words": ["Los", "poderes", "públicos", "garantizan", "la", "defensa", "de", "los", "consumidores", "y", "usuarios."],
                    "english": "Public authorities guarantee the defense of consumers and users."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 17: Geografía Física: Relieve, Costas, Ríos y Clima (unit_num=53, b1-geografia)
    # =========================================================================
    {
        "slug": "geografia",
        "unit_num": 53,
        "title": "Geografía Física: Relieve, Costas, Ríos y Clima",
        "description": "Fronteras y mares de España, el Teide y el Mulhacén, los ríos Tajo y Ebro, los cuatro climas españoles y los 16 Parques Nacionales.",
        "Badge": "Geografía Física",
        "lessons": [
            {
                "num": "01",
                "Title": "La Península Ibérica, los Archipiélagos y las Fronteras",
                "title": "La Península Ibérica, los Archipiélagos y las Fronteras",
                "grammar_slug": "limitar-al-norte-con-banado-por",
                "story_slug": "situacion",
                "story_title": "Entre dos mares y un océano: la encrucijada geográfica de España",
                "objectives": [
                    "Situar geográficamente a España (unos 506.000 km², cuarto país más extenso de Europa) y sus fronteras terrestres.",
                    "Identificar los mares que bañan sus costas (Mar Cantábrico, Océano Atlántico y Mar Mediterráneo) y sus dos archipiélagos (Baleares y Canarias).",
                    "Practicar las construcciones geográficas «limitar al norte/oeste con» y «estar bañado por»."
                ],
                "vocab": [
                    {"lemma": "la península ibérica", "pos": "noun", "translation": "Iberian Peninsula"},
                    {"lemma": "el archipiélago", "pos": "noun", "translation": "archipelago"},
                    {"lemma": "limitar con", "pos": "verb", "translation": "to border on"},
                    {"lemma": "estar bañado/a por", "pos": "verb", "translation": "to be washed / bordered by (a sea or ocean)"},
                    {"lemma": "el mar Cantábrico", "pos": "noun", "translation": "Cantabrian Sea (Bay of Biscay)"},
                    {"lemma": "el mar Mediterráneo", "pos": "noun", "translation": "Mediterranean Sea"},
                    {"lemma": "el océano Atlántico", "pos": "noun", "translation": "Atlantic Ocean"},
                    {"lemma": "el estrecho de Gibraltar", "pos": "noun", "translation": "Strait of Gibraltar"}
                ],
                "grammar_title": "Descripción geográfica: «limitar al noreste con» y «estar bañado por»",
                "grammar_text": "En español geográfico, las fronteras terrestres se expresan con el verbo **«limitar»** seguido de punto cardinal y la preposición **«con»** (*España limita al oeste con Portugal y al noreste con Francia y Andorra*), mientras que las costas se describen con la pasiva **«estar bañado/a por»** (*la península está bañada por el mar Cantábrico, el océano Atlántico y el mar Mediterráneo*).",
                "grammar_examples": [
                    {"es": "En la península ibérica, España limita al oeste con Portugal y al noreste con Francia y Andorra.", "en": "On the Iberian Peninsula, Spain borders Portugal to the west and France and Andorra to the northeast."},
                    {"es": "Las Islas Baleares están situadas en el mar Mediterráneo y las Islas Canarias en el océano Atlántico.", "en": "The Balearic Islands are located in the Mediterranean Sea and the Canary Islands in the Atlantic Ocean."}
                ],
                "grammar_tip": "Recuerda para la Tarea 3 del CCSE los 5 países con los que España tiene frontera terrestre: Francia, Andorra, Portugal, Marruecos (en Ceuta y Melilla) y Reino Unido (en Gibraltar).",
                "paragraphs": [
                    "Situada en el extremo suroccidental de Europa, a solo catorce kilómetros del continente africano a través del estrecho de Gibraltar, España cuenta con una superficie aproximada de 506.000 kilómetros cuadrados. Es el cuarto país más extenso del continente europeo (después de Rusia, Ucrania y Francia) y el segundo de la Unión Europea por superficie.",
                    "El territorio español se compone de cuatro grandes ámbitos geográficos: la mayor parte de la península ibérica (alrededor del 85 % de su superficie), el archipiélago de las Islas Baleares en el mar Mediterráneo, el archipiélago de las Islas Canarias en el océano Atlántico frente a la costa noroccidental de África, y las ciudades autónomas de Ceuta y Melilla en el norte del continente africano.",
                    "¿Con qué países tiene España frontera terrestre? Al noreste, a lo largo de la cordillera de los Pirineos, España limita con Francia y con el pequeño Principado de Andorra. Al oeste, a lo largo de la frontera más larga y antigua de Europa (conocida tradicionalmente como «La Raya»), limita con Portugal. En el sur peninsular existe la verja con el territorio británico de Gibraltar, y en el norte de África Ceuta y Melilla tienen frontera terrestre con Marruecos.",
                    "Las costas españolas, de casi 8.000 kilómetros de longitud, están bañadas por tres grandes masas de agua: al norte, el mar Cantábrico baña las costas de Galicia, Asturias, Cantabria y el País Vasco; al oeste y suroeste (así como en las Islas Canarias), el océano Atlántico baña las costas gallegas y las de Huelva y Cádiz; y al este y sureste (incluidas las Islas Baleares y Ceuta y Melilla), el mar Mediterráneo se extiende desde el estrecho de Gibraltar hasta el cabo de Creus en Girona.",
                    "Esta posición estratégica entre el Atlántico y el Mediterráneo y entre Europa y África explica por qué la geografía de España presenta una diversidad climática, paisajística y ecológica única en el continente."
                ],
                "questions": [
                    {
                        "question": "¿En qué mar u océano se encuentran situados los dos archipiélagos españoles, las Islas Baleares y las Islas Canarias?",
                        "options": [
                            "Las Islas Baleares en el mar Mediterráneo y las Islas Canarias en el océano Atlántico",
                            "Ambos archipiélagos están en el mar Cantábrico",
                            "Las Islas Baleares en el Atlántico y las Canarias en el Mediterráneo",
                            "En el mar del Norte"
                        ],
                        "correctIndex": 0,
                        "explanation": "Baleares se sitúa en el mar Mediterráneo oriental y Canarias en el océano Atlántico."
                    },
                    {
                        "question": "¿Con qué dos Estados limita España al noreste a lo largo de la cordillera de los Pirineos?",
                        "options": [
                            "Con Francia y Andorra",
                            "Con Italia y Suiza",
                            "Con Portugal y Bélgica",
                            "Con Alemania y Austria"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Pirineos forman la frontera natural del noreste peninsular con Francia y el Principado de Andorra."
                    },
                    {
                        "question": "¿Qué mar baña toda la costa norte de España, desde Galicia hasta el País Vasco?",
                        "options": [
                            "El mar Cantábrico",
                            "El mar Adriático",
                            "El mar Egeo",
                            "El mar Báltico"
                        ],
                        "correctIndex": 0,
                        "explanation": "El mar Cantábrico baña las costas del norte de España (cornisa cantábrica)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Con qué país tiene España su frontera terrestre más larga, situada al oeste de la península ibérica?",
                        "options": [
                            "Con Portugal",
                            "Con Francia",
                            "Con Andorra",
                            "Con Marruecos"
                        ],
                        "correctIndex": 0,
                        "explanation": "La frontera hispano-portuguesa («La Raya»), al oeste peninsular, es la más larga de España."
                    },
                    {
                        "prompt": "¿Qué estrecho separa el sur de la península ibérica del norte de África y une el océano Atlántico con el mar Mediterráneo?",
                        "options": [
                            "El estrecho de Gibraltar",
                            "El canal de la Mancha",
                            "El estrecho de Mesina",
                            "El estrecho de Magallanes"
                        ],
                        "correctIndex": 0,
                        "explanation": "El estrecho de Gibraltar une el Atlántico y el Mediterráneo y separa España de Marruecos."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Las Islas Baleares están bañadas por el mar ___ y las Islas Canarias por el océano Atlántico.",
                        "answer": "Mediterráneo",
                        "options": ["Mediterráneo", "Cantábrico", "Báltico", "Caribe"],
                        "explanation": "El archipiélago balear se encuentra en el mar Mediterráneo.",
                        "english": "The Balearic Islands are washed by the Mediterranean Sea and the Canary Islands by the Atlantic Ocean."
                    },
                    {
                        "sentence": "Al noreste, a lo largo de los Pirineos, España limita con Francia y con el Principado de ___.",
                        "answer": "Andorra",
                        "options": ["Andorra", "Mónaco", "Luxemburgo", "Malta"],
                        "explanation": "Francia y Andorra son los dos países fronterizos en los Pirineos.",
                        "english": "To the northeast, along the Pyrenees, Spain borders France and the Principality of Andorra."
                    }
                ],
                "ex_dict": {
                    "audioText": "España limita al oeste con Portugal y al noreste con Francia y Andorra a través de los Pirineos.",
                    "english": "Spain borders Portugal to the west and France and Andorra to the northeast across the Pyrenees."
                },
                "ex_sb": {
                    "words": ["Las", "costas", "de", "España", "están", "bañadas", "por", "el", "Cantábrico,", "el", "Atlántico", "y", "el", "Mediterráneo."],
                    "english": "The coasts of Spain are washed by the Cantabrian, the Atlantic, and the Mediterranean."
                }
            },
            {
                "num": "02",
                "Title": "La Meseta Central y las Grandes Cordilleras",
                "title": "La Meseta Central y las Grandes Cordilleras",
                "grammar_slug": "el-pico-mas-alto-de-espana-y-de-la-peninsula",
                "story_slug": "relieve",
                "story_title": "Del Teide al Mulhacén: un país de mesetas y montañas",
                "objectives": [
                    "Distinguir sin confusión el pico más alto de toda España (el Teide, 3.718 m, en Tenerife) del pico más alto de la península ibérica (el Mulhacén, 3.479 m, en Sierra Nevada, Granada) y del más alto de los Pirineos (el Aneto, 3.404 m, en Huesca).",
                    "Identificar la Meseta Central y las principales cordilleras: Sistema Central, Cordillera Cantábrica, Sistema Ibérico, Sierra Morena, Pirineos y Sistemas Béticos.",
                    "Practicar las construcciones superlativas relativas («el pico más alto de...»)."
                ],
                "vocab": [
                    {"lemma": "la Meseta Central", "pos": "noun", "translation": "Central Plateau (Meseta)"},
                    {"lemma": "la cordillera / el sistema montañoso", "pos": "noun", "translation": "mountain range"},
                    {"lemma": "el Teide", "pos": "noun", "translation": "Mount Teide (highest peak in Spain, 3,718 m, Tenerife)"},
                    {"lemma": "el Mulhacén", "pos": "noun", "translation": "Mulhacén (highest peak of the Iberian Peninsula, 3,479 m)"},
                    {"lemma": "el Aneto", "pos": "noun", "translation": "Aneto (highest peak of the Pyrenees, 3,404 m)"},
                    {"lemma": "Sierra Nevada", "pos": "noun", "translation": "Sierra Nevada (mountain range in Granada)"},
                    {"lemma": "el Sistema Central", "pos": "noun", "translation": "Central System mountain range"},
                    {"lemma": "los Pirineos", "pos": "noun", "translation": "Pyrenees"}
                ],
                "grammar_title": "Superlativos geográficos: «el pico más alto de España» frente a «el más alto de la península»",
                "grammar_text": "En el examen CCSE es fundamental prestar atención al complemento del superlativo **«el pico más alto de...»**: si la pregunta dice **«de España»**, la respuesta es **el Teide** (3.718 m, volcán en la isla de Tenerife, Canarias); si dice **«de la península ibérica»**, la respuesta es **el Mulhacén** (3.479 m, en Sierra Nevada, Granada).",
                "grammar_examples": [
                    {"es": "El Teide, situado en la isla de Tenerife, es el pico más alto de España con más de 3.700 metros.", "en": "Mount Teide, located on the island of Tenerife, is the highest peak in Spain at over 3,700 meters."},
                    {"es": "El Mulhacén, en Sierra Nevada (Granada), es la cumbre más alta de la península ibérica.", "en": "Mulhacén, in Sierra Nevada (Granada), is the highest summit on the Iberian Peninsula."}
                ],
                "grammar_tip": "¡No caigas en la trampa clásica del examen CCSE! Pico más alto de ESPAÑA = El Teide (Tenerife). Pico más alto de la PENÍNSULA = El Mulhacén (Sierra Nevada, Granada). Pico más alto de los PIRINEOS = El Aneto (Huesca).",
                "paragraphs": [
                    "España es uno de los países con mayor altitud media de Europa (unos 660 metros sobre el nivel del mar), solo superado por países alpinos o caucásicos como Suiza y Austria. El corazón del relieve peninsular lo ocupa una gran llanura elevada llamada la Meseta Central, que abarca buena parte de Castilla y León, Castilla-La Mancha, Madrid y Extremadura.",
                    "La Meseta Central está dividida en dos mitades (la Submeseta Norte, recorrida por el río Duero, y la Submeseta Sur, surcada por el Tajo y el Guadiana) por una cordillera interior que cruza el centro de la península: el Sistema Central, al que pertenecen las sierras de Guadarrama (entre Madrid y Segovia), Gredos y Somosierra. Más al sur, dentro de la Submeseta Sur, se alzan los Montes de Toledo.",
                    "Alrededor de la Meseta se disponen como un cinturón varios sistemas montañosos que la rodean: al norte, la Cordillera Cantábrica (con los escarpados Picos de Europa); al noreste y este, el Sistema Ibérico (que separa la Meseta del valle del Ebro); y al sur, Sierra Morena, frontera natural entre la Mancha y el valle del Guadalquivir en Andalucía.",
                    "Más allá de ese anillo interior se levantan las grandes cordilleras exteriores de la península: al noreste, los Pirineos forman una muralla de más de 400 kilómetros entre España, Andorra y Francia, cuya cumbre más elevada es el pico Aneto (3.404 metros, en la provincia de Huesca, Aragón); y al sureste se extienden los Sistemas Béticos, donde brilla Sierra Nevada (en Granada, Andalucía).",
                    "En Sierra Nevada se alza el Mulhacén (3.479 metros), que es el pico más alto de toda la península ibérica. Sin embargo, si buscamos la montaña más alta de toda España, debemos viajar al océano Atlántico: en la isla canaria de Tenerife se levanta el volcán del Teide, que con sus 3.718 metros de altitud ostenta el título de techo de España."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es el pico más alto de toda España y en qué isla se encuentra?",
                        "options": [
                            "El Teide (3.718 m), en la isla de Tenerife (Islas Canarias)",
                            "El Mulhacén, en la isla de Mallorca",
                            "El Aneto, en la isla de Gran Canaria",
                            "El Moncayo, en la isla de Ibiza"
                        ],
                        "correctIndex": 0,
                        "explanation": "El volcán del Teide, en Tenerife (Canarias), es el pico más alto de España con 3.718 metros."
                    },
                    {
                        "question": "¿Cuál es la montaña más alta de la península ibérica y en qué cordillera está situada?",
                        "options": [
                            "El Mulhacén (3.479 m), en Sierra Nevada (Sistemas Béticos, Granada)",
                            "El Teide, en el Sistema Central",
                            "El Aneto, en Sierra Morena",
                            "Peña Vieja, en los Montes de Toledo"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Mulhacén (3.479 m), en Sierra Nevada (Granada), es la cumbre más alta de la península ibérica."
                    },
                    {
                        "question": "¿Qué cordillera divide la Meseta Central en dos partes (Submeseta Norte y Submeseta Sur) e incluye las sierras de Guadarrama y Gredos?",
                        "options": [
                            "El Sistema Central",
                            "Los Pirineos",
                            "La Cordillera Costero-Catalana",
                            "Sierra Morena"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Sistema Central atraviesa la Meseta dividiéndola en Submeseta Norte y Submeseta Sur."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál es el pico más alto de la cordillera de los Pirineos, situado en la provincia de Huesca (Aragón)?",
                        "options": [
                            "El Aneto (3.404 m)",
                            "El Teide",
                            "El Mulhacén",
                            "El Almanzor"
                        ],
                        "correctIndex": 0,
                        "explanation": "El pico Aneto (3.404 m) es la cumbre más alta de los Pirineos."
                    },
                    {
                        "prompt": "¿Qué cordillera separa el sur de la Meseta Central del valle del río Guadalquivir en Andalucía?",
                        "options": [
                            "Sierra Morena",
                            "Los Pirineos",
                            "El Macizo Galaico",
                            "La Cordillera Cantábrica"
                        ],
                        "correctIndex": 0,
                        "explanation": "Sierra Morena es el escalón montañoso que separa la Meseta del valle del Guadalquivir."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El ___, situado en la isla de Tenerife, es el pico más alto de toda España.",
                        "answer": "Teide",
                        "options": ["Teide", "Mulhacén", "Aneto", "Naranco"],
                        "explanation": "El Teide (3.718 m) es el techo de España.",
                        "english": "Mount Teide, located on the island of Tenerife, is the highest peak in all of Spain."
                    },
                    {
                        "sentence": "El ___, en Sierra Nevada (Granada), es la cumbre más alta de la península ibérica.",
                        "answer": "Mulhacén",
                        "options": ["Mulhacén", "Teide", "Aneto", "Guadarrama"],
                        "explanation": "El Mulhacén (3.479 m) es el pico más alto de la península ibérica.",
                        "english": "Mulhacén, in Sierra Nevada (Granada), is the highest peak on the Iberian Peninsula."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Teide es el pico más alto de España y el Mulhacén es el más alto de la península ibérica.",
                    "english": "Mount Teide is the highest peak in Spain and Mulhacén is the highest on the Iberian Peninsula."
                },
                "ex_sb": {
                    "words": ["El", "Sistema", "Central", "divide", "la", "Meseta", "en", "Submeseta", "Norte", "y", "Submeseta", "Sur."],
                    "english": "The Central System divides the Meseta into the Northern Sub-plateau and the Southern Sub-plateau."
                }
            },
            {
                "num": "03",
                "Title": "Las Tres Vertientes Hidrográficas y los Grandes Ríos",
                "title": "Las Tres Vertientes Hidrográficas y los Grandes Ríos",
                "grammar_slug": "desembocar-en-el-rio-mas-largo",
                "story_slug": "rios",
                "story_title": "El Tajo hacia el Atlántico y el Ebro hacia el Mediterráneo: las arterias de agua",
                "objectives": [
                    "Distinguir el río más largo de la península ibérica (el Tajo, que desemboca en Lisboa en el Atlántico) del río más largo y caudaloso que discurre íntegramente por España (el Ebro, que desemboca en el Mediterráneo).",
                    "Clasificar los grandes ríos españoles en las tres vertientes: cantábrica, atlántica (Miño, Duero, Tajo, Guadiana, Guadalquivir) y mediterránea (Ebro, Júcar, Turia, Segura).",
                    "Practicar los verbos hidrográficos «nacer en», «pasar por» y «desembocar en»."
                ],
                "vocab": [
                    {"lemma": "la vertiente hidrográfica", "pos": "noun", "translation": "watershed / drainage basin"},
                    {"lemma": "desembocar en", "pos": "verb", "translation": "to flow into / empty into (a sea or ocean)"},
                    {"lemma": "el río Tajo", "pos": "noun", "translation": "Tagus River (longest of the Iberian Peninsula)"},
                    {"lemma": "el río Ebro", "pos": "noun", "translation": "Ebro River (most voluminous river in Spain)"},
                    {"lemma": "el río Duero", "pos": "noun", "translation": "Douro River"},
                    {"lemma": "el río Guadalquivir", "pos": "noun", "translation": "Guadalquivir River (navigable up to Seville)"},
                    {"lemma": "el río Miño / el río Guadiana", "pos": "noun", "translation": "Miño River / Guadiana River"},
                    {"lemma": "el caudal / caudaloso", "pos": "noun", "translation": "water flow / voluminous"}
                ],
                "grammar_title": "Verbos de geografía fluvial: «nacer en», «pasar por» y «desembocar en»",
                "grammar_text": "Para describir el recorrido de un río se utilizan tres verbos con sus preposiciones fijas: **«nacer en»** (lugar de origen), **«pasar por»** o **«atravesar»** (ciudades o regiones que recorre) y **«desembocar en»** (mar u océano donde vierte sus aguas): *El río Tajo **nace en** la sierra de Albarracín, **pasa por** Aranjuez y Toledo y **desemboca en** el océano Atlántico en Lisboa*.",
                "grammar_examples": [
                    {"es": "El Tajo es el río más largo de la península ibérica y desemboca en el océano Atlántico.", "en": "The Tagus is the longest river on the Iberian Peninsula and empties into the Atlantic Ocean."},
                    {"es": "El Ebro pasa por Zaragoza y desemboca en el mar Mediterráneo formando el Delta del Ebro en Tarragona.", "en": "The Ebro flows through Zaragoza and empties into the Mediterranean Sea forming the Ebro Delta in Tarragona."}
                ],
                "grammar_tip": "Regla de oro para el CCSE: Miño, Duero, Tajo, Guadiana y Guadalquivir desembocan en el OCÉANO ATLÁNTICO; el Ebro, el Turia, el Júcar y el Segura desembocan en el MAR MEDITERRÁNEO.",
                "paragraphs": [
                    "Como la Meseta Central está ligeramente inclinada hacia el oeste, la mayoría de los grandes ríos de la península ibérica viajan de este a oeste para verter sus aguas en el océano Atlántico. La hidrografía española se divide en tres grandes vertientes según el mar u océano en el que desembocan sus ríos: la vertiente cantábrica, la vertiente atlántica y la vertiente mediterránea.",
                    "Los ríos de la vertiente cantábrica (como el Bidasoa, el Nervión en Bilbao, el Besaya, el Sella o el Nalón en Asturias) nacen en la Cordillera Cantábrica muy cerca de la costa: por eso son ríos cortos, de fuerte pendiente y muy caudalosos y regulares gracias a las lluvias constantes del norte.",
                    "En la vertiente atlántica brillan cinco grandes ríos que todo candidato al examen CCSE debe conocer de norte a sur. En el noroeste, el río Miño (con su principal afluente, el Sil) recorre Galicia. En la Submeseta Norte, el río Duero atraviesa Castilla y León (pasando por Soria, Aranda, Tordesillas y Zamora) antes de entrar en Portugal y desembocar en Oporto. En el centro, el río Tajo —que nace en los Montes Universales (Teruel) y pasa por Aranjuez, Toledo, Talavera de la Reina y Alcántara antes de llegar a Lisboa— es, con más de 1.000 kilómetros, el río más largo de la península ibérica.",
                    "Más al sur, también hacia el Atlántico, discurren el río Guadiana (que pasa por Mérida y Badajoz y desemboca en Ayamonte) y el río Guadalquivir, eje histórico de Andalucía: nace en la sierra de Cazorla (Jaén), pasa por Córdoba y Sevilla y desemboca en Sanlúcar de Barrameda (Cádiz), frente al Parque Nacional de Doñana. El Guadalquivir tiene una singularidad única: es el único río navegable de España para barcos de gran calado, desde su desembocadura hasta el puerto de Sevilla.",
                    "Por último, en la vertiente mediterránea los ríos suelen ser más cortos e irregulares por la escasez de lluvias estivales —como el Ter y el Llobregat en Cataluña, el Turia y el Júcar en la Comunidad Valenciana o el Segura en Murcia y Alicante—, con una gigantesca excepción: el río Ebro. El Ebro nace en Fontibre (Cantabria), atraviesa La Rioja, Navarra y Aragón (pasando por Logroño y Zaragoza) y desemboca en el Mediterráneo en el Delta del Ebro (Tarragona): con unos 930 kilómetros, es el río más caudaloso y el más largo de los que discurren íntegramente por territorio español."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es el río más largo de la península ibérica, que pasa por Toledo y desemboca en el océano Atlántico en Lisboa?",
                        "options": ["El río Tajo", "El río Segura", "El río Miño", "El río Nervión"],
                        "correctIndex": 0,
                        "explanation": "El Tajo (con más de 1.000 km entre España y Portugal) es el río más largo de la península ibérica."
                    },
                    {
                        "question": "¿Cuál es el río más caudaloso de España y el más largo de los que desembocan en el mar Mediterráneo, pasando por Zaragoza?",
                        "options": ["El río Ebro", "El río Duero", "El río Guadalquivir", "El río Guadiana"],
                        "correctIndex": 0,
                        "explanation": "El río Ebro es el más caudaloso de España, pasa por Logroño y Zaragoza, y desemboca en el mar Mediterráneo (Tarragona)."
                    },
                    {
                        "question": "¿Cuál es el único río de España navegable desde el mar hasta una gran ciudad interior (Sevilla), pasando antes por Córdoba?",
                        "options": [
                            "El río Guadalquivir",
                            "El río Manzanares",
                            "El río Turia",
                            "El río Bidasoa"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Guadalquivir recorre Andalucía pasando por Córdoba y Sevilla y es el único río navegable de España hasta Sevilla."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué océano o mar desembocan los ríos Miño, Duero, Tajo, Guadiana y Guadalquivir?",
                        "options": [
                            "En el océano Atlántico",
                            "En el mar Mediterráneo",
                            "En el mar Cantábrico",
                            "En el mar Negro"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los cinco grandes ríos (Miño, Duero, Tajo, Guadiana y Guadalquivir) pertenecen a la vertiente atlántica."
                    },
                    {
                        "prompt": "¿Qué río baña la ciudad de Valencia y desemboca en el mar Mediterráneo?",
                        "options": [
                            "El río Turia",
                            "El río Duero",
                            "El río Miño",
                            "El río Nalón"
                        ],
                        "correctIndex": 0,
                        "explanation": "El río Turia atraviesa la ciudad de Valencia y desemboca en el mar Mediterráneo."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El río ___ es el más largo de la península ibérica y pasa por ciudades como Aranjuez y Toledo.",
                        "answer": "Tajo",
                        "options": ["Tajo", "Segura", "Turia", "Sella"],
                        "explanation": "El Tajo es el río más largo de la península ibérica.",
                        "english": "The Tagus River is the longest on the Iberian Peninsula and passes through cities such as Aranjuez and Toledo."
                    },
                    {
                        "sentence": "El río ___ pasa por Zaragoza y desemboca en el mar Mediterráneo en la provincia de Tarragona.",
                        "answer": "Ebro",
                        "options": ["Ebro", "Duero", "Miño", "Guadiana"],
                        "explanation": "El Ebro desemboca en el mar Mediterráneo formando el Delta del Ebro en Tarragona.",
                        "english": "The Ebro River passes through Zaragoza and flows into the Mediterranean Sea in the province of Tarragona."
                    }
                ],
                "ex_dict": {
                    "audioText": "El río Tajo desemboca en el océano Atlántico y el río Ebro desemboca en el mar Mediterráneo.",
                    "english": "The Tagus River empties into the Atlantic Ocean and the Ebro River empties into the Mediterranean Sea."
                },
                "ex_sb": {
                    "words": ["El", "Guadalquivir", "pasa", "por", "Córdoba", "y", "Sevilla", "y", "desemboca", "en", "el", "Atlántico."],
                    "english": "The Guadalquivir passes through Córdoba and Seville and empties into the Atlantic."
                }
            },
            {
                "num": "04",
                "Title": "Los Cuatro Grandes Climas de España y sus Paisajes",
                "title": "Los Cuatro Grandes Climas de España y sus Paisajes",
                "grammar_slug": "caracterizarse-por-temperaturas-suaves",
                "story_slug": "climas",
                "story_title": "De la lluvia verde del norte a la eterna primavera de Canarias",
                "objectives": [
                    "Identificar los cuatro grandes climas de España: oceánico (o atlántico), mediterráneo (costero, de interior y seco), de montaña y subtropical (Canarias).",
                    "Relacionar cada clima con sus temperaturas, precipitaciones y regiones características.",
                    "Practicar las construcciones «caracterizarse por + sustantivo» y «temperaturas suaves durante todo el año»."
                ],
                "vocab": [
                    {"lemma": "el clima oceánico (o atlántico)", "pos": "noun", "translation": "oceanic / Atlantic climate"},
                    {"lemma": "el clima mediterráneo", "pos": "noun", "translation": "Mediterranean climate"},
                    {"lemma": "el clima subtropical", "pos": "noun", "translation": "subtropical climate (Canary Islands)"},
                    {"lemma": "el clima de montaña", "pos": "noun", "translation": "mountain / alpine climate"},
                    {"lemma": "las precipitaciones abundantes", "pos": "noun", "translation": "abundant rainfall"},
                    {"lemma": "la amplitud térmica", "pos": "noun", "translation": "temperature range (difference between winter and summer)"},
                    {"lemma": "la sequía estival", "pos": "noun", "translation": "summer drought"},
                    {"lemma": "caracterizarse por", "pos": "verb", "translation": "to be characterized by"}
                ],
                "grammar_title": "Descripción climática: «caracterizarse por» y «temperaturas suaves»",
                "grammar_text": "Para describir los climas de una región se utiliza el verbo pronominal **«caracterizarse por»** seguido de grupos nominales con adjetivos especificativos: *El clima subtropical de las Islas Canarias **se caracteriza por** temperaturas suaves y cálidas durante todo el año y escasas precipitaciones*.",
                "grammar_examples": [
                    {"es": "El clima oceánico del norte de España se caracteriza por precipitaciones abundantes y temperaturas suaves.", "en": "The oceanic climate of northern Spain is characterized by abundant rainfall and mild temperatures."},
                    {"es": "Las Islas Canarias disfrutan de un clima subtropical debido a su cercanía al trópico de Cáncer y a los vientos alisios.", "en": "The Canary Islands enjoy a subtropical climate due to their proximity to the Tropic of Cancer and the trade winds."}
                ],
                "grammar_tip": "Pregunta habitual del CCSE: ¿Qué clima tienen las Islas Canarias? Clima subtropical (temperaturas suaves y primaverales todo el año). ¿Y Galicia y la cornisa cantábrica? Clima oceánico o atlántico.",
                "paragraphs": [
                    "Pocos países del mundo ofrecen en su territorio contrastes climáticos tan marcados como España. En un mismo día de invierno es posible esquiar en las cumbres nevadas del Pirineo o de Sierra Nevada, pasear bajo una lluvia fina por un bosque verde de Galicia y bañarse en el mar a veintidós grados en una playa del sur de Tenerife o Gran Canaria.",
                    "El primer gran dominio es el clima oceánico (también llamado atlántico), propio del norte y noroeste peninsular: Galicia, el Principado de Asturias, Cantabria, el País Vasco y el norte de Navarra. Se caracteriza por temperaturas suaves tanto en invierno como en verano y por precipitaciones abundantes y regulares repartidas durante todo el año, lo que da origen a los prados y bosques caducifolios de «la España verde».",
                    "El segundo y más extenso es el clima mediterráneo, que presenta tres variedades bien diferenciadas. En la costa del mar Mediterráneo, las Islas Baleares y el suroeste andaluz predomina el mediterráneo típico o costero, con inviernos templados, veranos cálidos y lluvias concentradas en otoño y primavera. En el interior de la Meseta y la depresión del Ebro (Madrid, Castilla y León, Castilla-La Mancha, Extremadura, Aragón) se da el clima mediterráneo de interior o continentalizado, con una gran amplitud térmica: inviernos fríos y veranos muy calurosos y secos. Por último, en el sureste peninsular (Almería, Murcia y parte de Alicante) aparece el clima mediterráneo seco o subdesértico, el más árido de Europa.",
                    "El tercer tipo es el clima de montaña, presente en las grandes cordilleras situadas por encima de los 1.200 o 1.500 metros de altitud (Pirineos, Sistema Central, Cordillera Cantábrica, Sistema Ibérico y Sierra Nevada), caracterizado por inviernos largos y muy fríos con frecuentes precipitaciones en forma de nieve y veranos frescos y cortos.",
                    "Finalmente, el archipiélago de las Islas Canarias posee un clima único en España: el clima subtropical. Gracias a su latitud próxima al trópico de Cáncer, a la corriente marina fría de Canarias y a los vientos alisios, las islas disfrutan de temperaturas suaves y primaverales durante los doce meses del año (con medias cercanas a los 20-22 °C) y precipitaciones escasas, más abundantes en las caras norte de las islas montañosas que en las islas orientales como Lanzarote y Fuerteventura."
                ],
                "questions": [
                    {
                        "question": "¿Qué tipo de clima es característico de las Islas Canarias, con temperaturas suaves y primaverales durante todo el año?",
                        "options": [
                            "El clima subtropical",
                            "El clima polar ártico",
                            "El clima alpino de alta montaña en todas sus playas",
                            "El clima continental extremo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Islas Canarias tienen un clima subtropical caracterizado por temperaturas suaves todo el año."
                    },
                    {
                        "question": "¿Qué clima predomina en el norte de España (Galicia, Asturias, Cantabria y País Vasco), caracterizado por lluvias abundantes todo el año y paisajes verdes?",
                        "options": [
                            "El clima oceánico o atlántico",
                            "El clima desértico",
                            "El clima tropical monzónico",
                            "El clima ecuatorial"
                        ],
                        "correctIndex": 0,
                        "explanation": "La cornisa cantábrica y Galicia disfrutan de un clima oceánico o atlántico."
                    },
                    {
                        "question": "¿Cómo son los inviernos y los veranos en el clima mediterráneo de interior (o continentalizado) propio de la Meseta Central?",
                        "options": [
                            "Los inviernos son fríos y los veranos son muy calurosos y secos",
                            "No existe diferencia de temperatura entre enero y agosto",
                            "Llueve torrencialmente todos los días de julio y agosto",
                            "La temperatura nunca baja de 25 grados en invierno"
                        ],
                        "correctIndex": 0,
                        "explanation": "El clima mediterráneo de interior de la Meseta tiene una elevada amplitud térmica: inviernos fríos y veranos muy calurosos."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué zona del sureste de España se registra el clima mediterráneo más seco y árido de Europa?",
                        "options": [
                            "En Almería, Murcia y parte de Alicante",
                            "En A Coruña y Lugo",
                            "En Oviedo y Santander",
                            "En San Sebastián y Bilbao"
                        ],
                        "correctIndex": 0,
                        "explanation": "El sureste peninsular (Almería y Murcia) presenta el clima mediterráneo seco o subdesértico."
                    },
                    {
                        "prompt": "¿Dónde se localiza en España el clima de montaña con abundantes nevadas invernales?",
                        "options": [
                            "En las grandes cordilleras como los Pirineos, Sierra Nevada o el Sistema Central",
                            "En las playas de Fuerteventura",
                            "En el Delta del Ebro al nivel del mar",
                            "En la bahía de Cádiz"
                        ],
                        "correctIndex": 0,
                        "explanation": "El clima de montaña es propio de las cumbres de los Pirineos, Sierra Nevada, Cordillera Cantábrica y Sistema Central."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "Las Islas Canarias disfrutan de un clima ___ con temperaturas suaves durante todo el año.",
                        "answer": "subtropical",
                        "options": ["subtropical", "polar", "cantábrico", "continental"],
                        "explanation": "El clima subtropical es exclusivo del archipiélago canario.",
                        "english": "The Canary Islands enjoy a subtropical climate with mild temperatures throughout the year."
                    },
                    {
                        "sentence": "El clima ___ del norte de España se caracteriza por precipitaciones abundantes y regulares.",
                        "answer": "oceánico",
                        "options": ["oceánico", "desértico", "tropical", "ecuatorial"],
                        "explanation": "El clima oceánico (o atlántico) caracteriza a Galicia y la cornisa cantábrica.",
                        "english": "The oceanic climate of northern Spain is characterized by abundant and regular rainfall."
                    }
                ],
                "ex_dict": {
                    "audioText": "Las Islas Canarias tienen un clima subtropical con temperaturas suaves durante todo el año.",
                    "english": "The Canary Islands have a subtropical climate with mild temperatures throughout the year."
                },
                "ex_sb": {
                    "words": ["El", "norte", "de", "España", "se", "caracteriza", "por", "su", "clima", "oceánico", "y", "sus", "paisajes", "verdes."],
                    "english": "Northern Spain is characterized by its oceanic climate and its green landscapes."
                }
            },
            {
                "num": "05",
                "Title": "La Red de Parques Nacionales y la Biodiversidad",
                "title": "La Red de Parques Nacionales y la Biodiversidad",
                "grammar_slug": "declarado-parque-nacional-en-peligro",
                "story_slug": "parques",
                "story_title": "De los Picos de Europa a Doñana y Timanfaya: los dieciséis tesoros naturales",
                "objectives": [
                    "Conocer la Red de Parques Nacionales de España (16 parques nacionales) y ubicar los más preguntados en el CCSE: Picos de Europa (el más antiguo, 1918), Ordesa y Monte Perdido, Doñana, Teide, Timanfaya, Garajonay, Monfragüe, Tablas de Daimiel y Sierra de Guadarrama.",
                    "Identificar especies emblemáticas protegidas como el lince ibérico y el águila imperial ibérica.",
                    "Practicar las construcciones «ser declarado Parque Nacional» y «contar con el mayor número de Reservas de la Biosfera»."
                ],
                "vocab": [
                    {"lemma": "el Parque Nacional", "pos": "noun", "translation": "National Park"},
                    {"lemma": "la Reserva de la Biosfera", "pos": "noun", "translation": "UNESCO Biosphere Reserve"},
                    {"lemma": "los Picos de Europa", "pos": "noun", "translation": "Picos de Europa (first National Park in Spain, 1918)"},
                    {"lemma": "el Parque Nacional de Doñana", "pos": "noun", "translation": "Doñana National Park (Andalusia)"},
                    {"lemma": "el Parque Nacional de Timanfaya", "pos": "noun", "translation": "Timanfaya National Park (Lanzarote)"},
                    {"lemma": "el Parque Nacional de Ordesa y Monte Perdido", "pos": "noun", "translation": "Ordesa y Monte Perdido National Park (Pyrenees, Huesca)"},
                    {"lemma": "el lince ibérico", "pos": "noun", "translation": "Iberian lynx"},
                    {"lemma": "la biodiversidad", "pos": "noun", "translation": "biodiversity"}
                ],
                "grammar_title": "Patrimonio natural: «ser declarado Parque Nacional» y ubicación regional",
                "grammar_text": "En la Tarea 3 del CCSE es muy frecuente preguntar en qué comunidad autónoma o isla se encuentra un **Parque Nacional**. Se emplean participios pasivos como **«situado en»**, **«compartido entre»** y **«declarado Parque Nacional en»**: *El Parque Nacional de los Picos de Europa, **declarado** en 1918, está **compartido entre** Asturias, Cantabria y Castilla y León*.",
                "grammar_examples": [
                    {"es": "El Parque Nacional de Doñana, situado en Andalucía, es uno de los humedales más importantes de Europa.", "en": "Doñana National Park, located in Andalusia, is one of the most important wetlands in Europe."},
                    {"es": "El Parque Nacional de Timanfaya se encuentra en la isla canaria de Lanzarote.", "en": "Timanfaya National Park is located on the Canary Island of Lanzarote."}
                ],
                "grammar_tip": "Memoriza las ubicaciones clave para el CCSE: Picos de Europa (Asturias, Cantabria y León), Ordesa y Monte Perdido (Huesca, Aragón), Doñana y Sierra Nevada (Andalucía), Monfragüe (Extremadura), Tablas de Daimiel y Cabañeros (Castilla-La Mancha), Teide (Tenerife) y Timanfaya (Lanzarote).",
                "paragraphs": [
                    "España es el país con mayor biodiversidad de la Unión Europea y lidera a nivel mundial la lista de Reservas de la Biosfera reconocidas por la UNESCO, con más de cincuenta espacios protegidos. La joya de la corona de la conservación ambiental en nuestro país es la Red de Parques Nacionales, integrada actualmente por dieciséis parques repartidos entre la península y los dos archipiélagos.",
                    "España fue pionera en Europa en la protección de la naturaleza: en el verano de 1918 se declararon los dos primeros parques nacionales españoles. El primero fue la Montaña de Covadonga —hoy ampliado como Parque Nacional de los Picos de Europa, compartido entre el Principado de Asturias, Cantabria y la provincia de León (Castilla y León)—; y pocas semanas después nació el Parque Nacional de Ordesa y Monte Perdido, en el Pirineo de Huesca (Aragón). También en los Pirineos, pero en Cataluña (Lleida), se alza el Parque Nacional de Aigüestortes i Estany de Sant Maurici.",
                    "En el interior peninsular destacan cuatro parques imprescindibles para el examen CCSE: el Parque Nacional de la Sierra de Guadarrama (compartido entre la Comunidad de Madrid y Segovia), el Parque Nacional de Monfragüe (en Cáceres, Extremadura, santuario de aves rapaces y dehesas), y dos parques situados en Castilla-La Mancha: las Tablas de Daimiel (humedal único en Ciudad Real) y Cabañeros (entre Ciudad Real y Toledo).",
                    "En el sur, Andalucía cuenta con tres parques nacionales: el célebre Parque Nacional de Doñana (entre Huelva, Sevilla y Cádiz, refugio de millones de aves migratorias y del lince ibérico), el Parque Nacional de Sierra Nevada (en Granada y Almería) y el más reciente de toda la red, el Parque Nacional de la Sierra de las Nieves (en Málaga, declarado en 2021). En las costas atlántica y mediterránea se sitúan además el Parque Nacional Marítimo-Terrestre de las Islas Atlánticas de Galicia y el del Archipiélago de Cabrera (en las Islas Baleares).",
                    "Finalmente, las Islas Canarias albergan nada menos que cuatro parques nacionales volcánicos y subtropicales de fama mundial: el Parque Nacional del Teide (en Tenerife, el más visitado de España), el Parque Nacional de Timanfaya (con sus impresionantes paisajes volcánicos en Lanzarote), el Parque Nacional de Garajonay (con sus bosques húmedos de laurisilva en La Gomera) y el Parque Nacional de la Caldera de Taburiente (en La Palma)."
                ],
                "questions": [
                    {
                        "question": "¿En qué comunidad autónoma se encuentra el Parque Nacional de Doñana, famoso por sus marismas, aves migratorias y la protección del lince ibérico?",
                        "options": [
                            "En Andalucía (entre Huelva, Sevilla y Cádiz)",
                            "En el País Vasco",
                            "En La Rioja",
                            "En la Región de Murcia"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Parque Nacional de Doñana se sitúa en el suroeste de Andalucía (Huelva, Sevilla y Cádiz)."
                    },
                    {
                        "question": "¿Qué tres comunidades autónomas comparten el Parque Nacional de los Picos de Europa, el más antiguo de España (1918)?",
                        "options": [
                            "El Principado de Asturias, Cantabria y Castilla y León (León)",
                            "Cataluña, Aragón y la Comunidad Valenciana",
                            "Extremadura, Madrid y Andalucía",
                            "Galicia, Navarra y Murcia"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Picos de Europa se extienden por Asturias, Cantabria y el norte de la provincia de León (Castilla y León)."
                    },
                    {
                        "question": "¿En qué isla de las Canarias se encuentra el Parque Nacional volcánico de Timanfaya?",
                        "options": [
                            "En Lanzarote",
                            "En Mallorca",
                            "En Ibiza",
                            "En Menorca"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Parque Nacional de Timanfaya está situado en la isla canaria de Lanzarote."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿En qué comunidad autónoma está situado el Parque Nacional de Monfragüe?",
                        "options": [
                            "En Extremadura (provincia de Cáceres)",
                            "En Cantabria",
                            "En las Islas Baleares",
                            "En Navarra"
                        ],
                        "correctIndex": 0,
                        "explanation": "Monfragüe se encuentra en la provincia de Cáceres, en Extremadura."
                    },
                    {
                        "prompt": "¿En qué provincia aragonesa del Pirineo se encuentra el Parque Nacional de Ordesa y Monte Perdido?",
                        "options": [
                            "En Huesca (Aragón)",
                            "En Almería",
                            "En Pontevedra",
                            "En Badajoz"
                        ],
                        "correctIndex": 0,
                        "explanation": "Ordesa y Monte Perdido está en el Pirineo oscense (Huesca, Aragón)."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "El Parque Nacional de ___ está situado en Andalucía y es uno de los grandes refugios del lince ibérico.",
                        "answer": "Doñana",
                        "options": ["Doñana", "Timanfaya", "Cabrera", "Ordesa"],
                        "explanation": "Doñana es el emblemático parque nacional de Andalucía.",
                        "english": "Doñana National Park is located in Andalusia and is one of the great sanctuaries of the Iberian lynx."
                    },
                    {
                        "sentence": "El Parque Nacional de los ___ de Europa fue el primer espacio declarado Parque Nacional en España en 1918.",
                        "answer": "Picos",
                        "options": ["Picos", "Ríos", "Montes", "Valles"],
                        "explanation": "El Parque Nacional de los Picos de Europa (creado en 1918 como Montaña de Covadonga) es el más antiguo de España.",
                        "english": "Picos de Europa National Park was the first area declared a National Park in Spain in 1918."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Parque Nacional de Doñana se encuentra en Andalucía y el de Timanfaya está en Lanzarote.",
                    "english": "Doñana National Park is located in Andalusia and Timanfaya is in Lanzarote."
                },
                "ex_sb": {
                    "words": ["Los", "Picos", "de", "Europa", "fueron", "el", "primer", "Parque", "Nacional", "declarado", "en", "España."],
                    "english": "The Picos de Europa were the first National Park declared in Spain."
                }
            }
        ]
    },

    # =========================================================================
    # UNIT 18: La España Verde: Galicia, Asturias, Cantabria y País Vasco (unit_num=54, b1-norte)
    # =========================================================================
    {
        "slug": "norte",
        "unit_num": 54,
        "title": "La España Verde: Galicia, Asturias, Cantabria y País Vasco",
        "description": "Provincias, capitales, patrimonio y cultura de Galicia, Asturias, Cantabria, País Vasco, Navarra y La Rioja.",
        "Badge": "Norte de España",
        "lessons": [
            {
                "num": "01",
                "Title": "Galicia: Las Cuatro Provincias, Santiago y las Rías",
                "title": "Galicia: Las Cuatro Provincias, Santiago y las Rías",
                "grammar_slug": "estar-integrada-por-cuatro-provincias",
                "story_slug": "galicia",
                "story_title": "El faro más antiguo del mundo, las rías y la meta del Camino en Santiago",
                "objectives": [
                    "Memorizar las cuatro provincias de Galicia (A Coruña, Lugo, Ourense y Pontevedra) y su capital autonómica (Santiago de Compostela).",
                    "Identificar la Torre de Hércules (A Coruña), la Muralla romana de Lugo, la Catedral de Santiago y las Rías Altas y Baixas.",
                    "Practicar las construcciones «estar integrada por cuatro provincias» y «ostentar la capitalidad autonómica»."
                ],
                "vocab": [
                    {"lemma": "Santiago de Compostela", "pos": "noun", "translation": "Santiago de Compostela (capital of Galicia)"},
                    {"lemma": "A Coruña, Lugo, Ourense y Pontevedra", "pos": "noun", "translation": "the four provinces of Galicia"},
                    {"lemma": "la ría", "pos": "noun", "translation": "ria / coastal inlet"},
                    {"lemma": "el Camino de Santiago", "pos": "noun", "translation": "Way of St. James (pilgrimage route)"},
                    {"lemma": "la Torre de Hércules", "pos": "noun", "translation": "Tower of Hercules (Roman lighthouse in A Coruña)"},
                    {"lemma": "la Muralla romana de Lugo", "pos": "noun", "translation": "Roman Walls of Lugo (UNESCO)"},
                    {"lemma": "la Xunta de Galicia", "pos": "noun", "translation": "Regional Government of Galicia"},
                    {"lemma": "el gaitero / la muñeira", "pos": "noun", "translation": "bagpiper / traditional Galician dance"}
                ],
                "grammar_title": "Geografía política autonómica: «estar integrada por» y «tener su capital en»",
                "grammar_text": "En la Tarea 3 del CCSE es imprescindible saber cuántas y cuáles son las provincias de cada comunidad autónoma, y distinguir cuando la capital autonómica no es capital de provincia: *La comunidad autónoma de Galicia **está integrada por cuatro provincias** (**A Coruña, Lugo, Ourense y Pontevedra**) y **tiene su capital en** Santiago de Compostela (situada en la provincia de A Coruña)*.",
                "grammar_examples": [
                    {"es": "Galicia está integrada por cuatro provincias: A Coruña, Lugo, Ourense y Pontevedra.", "en": "Galicia is made up of four provinces: A Coruña, Lugo, Ourense, and Pontevedra."},
                    {"es": "La Catedral de Santiago de Compostela es la meta histórica de los peregrinos del Camino de Santiago.", "en": "The Cathedral of Santiago de Compostela is the historic destination of pilgrims on the Way of St. James."}
                ],
                "grammar_tip": "¡Pregunta fija del CCSE! Las 4 provincias de Galicia son A Coruña, Lugo, Ourense (la única sin mar) y Pontevedra. Su capital autonómica es Santiago de Compostela.",
                "paragraphs": [
                    "En el extremo noroccidental de la península ibérica, asomada al océano Atlántico y al mar Cantábrico, se extiende Galicia, una comunidad histórica donde conviven en armonía dos lenguas oficiales: el castellano y el gallego. Su institución de autogobierno recibe el nombre de Xunta de Galicia y su fiesta oficial, el Día Nacional de Galicia, se celebra cada 25 de julio, festividad del Apóstol Santiago.",
                    "Para el examen CCSE es indispensable recordar que Galicia está dividida en cuatro provincias: tres de ellas son costeras —A Coruña, Lugo y Pontevedra— y una es interior —Ourense, atravesada por el río Miño y los impresionantes cañones del río Sil en la Ribeira Sacra—. La capital de la comunidad autónoma no es ninguna de las cuatro capitales provinciales, sino la ciudad de Santiago de Compostela, situada dentro de la provincia de A Coruña.",
                    "La costa gallega es famosa en todo el mundo por sus rías —antiguos valles fluviales inundados por el mar—, divididas en las Rías Altas (al norte) y las Rías Baixas (al suroeste, en Pontevedra, donde se encuentra el Parque Nacional de las Islas Atlánticas, con las islas Cíes, Ons, Sálvora y Cortegada, y grandes ciudades portuarias como Vigo).",
                    "El patrimonio histórico gallego cuenta con tres bienes declarados Patrimonio de la Humanidad por la UNESCO que suelen aparecer en el examen: en primer lugar, el centro histórico y la Catedral de Santiago de Compostela, punto final desde la Edad Media del Camino de Santiago, primer Itinerario Cultural Europeo.",
                    "En segundo lugar, en la ciudad de A Coruña se alza la Torre de Hércules, el faro romano en funcionamiento más antiguo del mundo (del siglo I d. C.). Y en tercer lugar, la ciudad de Lugo conserva íntegra su Muralla romana de más de dos kilómetros de perímetro. En su gastronomía brillan el pulpo «á feira», la empanada gallega, el caldo gallego, la tarta de Santiago y los mariscos de sus rías."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las cuatro provincias que integran la comunidad autónoma de Galicia?",
                        "options": [
                            "A Coruña, Lugo, Ourense y Pontevedra",
                            "Oviedo, Santander, Bilbao y Vitoria",
                            "León, Zamora, Salamanca y Palencia",
                            "Huesca, Zaragoza, Teruel y Soria"
                        ],
                        "correctIndex": 0,
                        "explanation": "Galicia está formada por las cuatro provincias de A Coruña, Lugo, Ourense y Pontevedra."
                    },
                    {
                        "question": "¿Cuál es la capital de la comunidad autónoma de Galicia, meta del célebre camino de peregrinación europeo?",
                        "options": [
                            "Santiago de Compostela",
                            "Vigo",
                            "Ourense",
                            "Ferrol"
                        ],
                        "correctIndex": 0,
                        "explanation": "Santiago de Compostela (en la provincia de A Coruña) es la capital autonómica de Galicia."
                    },
                    {
                        "question": "¿En qué ciudad gallega se encuentra la Torre de Hércules, el faro romano en activo más antiguo del mundo?",
                        "options": [
                            "En A Coruña",
                            "En Ourense",
                            "En Pontevedra",
                            "En Lugo"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Torre de Hércules se alza en la costa de la ciudad de A Coruña."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Cuál de las cuatro provincias de Galicia es la única que no tiene costa marítima?",
                        "options": [
                            "Ourense",
                            "Pontevedra",
                            "A Coruña",
                            "Lugo"
                        ],
                        "correctIndex": 0,
                        "explanation": "Ourense es la única provincia interior de Galicia."
                    },
                    {
                        "prompt": "¿Qué ciudad gallega es famosa por conservar completo todo el perímetro de su Muralla romana, declarada Patrimonio de la Humanidad?",
                        "options": [
                            "Lugo",
                            "Vigo",
                            "Santiago de Compostela",
                            "Pontevedra"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Muralla romana de Lugo rodea íntegramente el casco histórico de la ciudad."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La comunidad autónoma de Galicia tiene su capital en ___ de Compostela.",
                        "answer": "Santiago",
                        "options": ["Santiago", "Oviedo", "Santander", "Logroño"],
                        "explanation": "Santiago de Compostela es la capital de Galicia.",
                        "english": "The autonomous community of Galicia has its capital in Santiago de Compostela."
                    },
                    {
                        "sentence": "Las cuatro provincias de Galicia son A Coruña, Lugo, ___ y Pontevedra.",
                        "answer": "Ourense",
                        "options": ["Ourense", "Álava", "Cáceres", "Zamora"],
                        "explanation": "A Coruña, Lugo, Ourense y Pontevedra son las cuatro provincias gallegas.",
                        "english": "The four provinces of Galicia are A Coruña, Lugo, Ourense, and Pontevedra."
                    }
                ],
                "ex_dict": {
                    "audioText": "Galicia tiene su capital en Santiago de Compostela y está formada por A Coruña, Lugo, Ourense y Pontevedra.",
                    "english": "Galicia has its capital in Santiago de Compostela and is formed by A Coruña, Lugo, Ourense, and Pontevedra."
                },
                "ex_sb": {
                    "words": ["La", "Torre", "de", "Hércules", "es", "un", "faro", "romano", "situado", "en", "A", "Coruña."],
                    "english": "The Tower of Hercules is a Roman lighthouse located in A Coruña."
                }
            },
            {
                "num": "02",
                "Title": "El Principado de Asturias: Oviedo y Picos de Europa",
                "title": "El Principado de Asturias: Oviedo y Picos de Europa",
                "grammar_slug": "comunidad-uniprovincial-capital-en-oviedo",
                "story_slug": "asturias",
                "story_title": "Paraíso natural entre los Picos de Europa, el arte prerrománico y el Teatro Campoamor",
                "objectives": [
                    "Identificar el Principado de Asturias como comunidad autónoma uniprovincial con capital en Oviedo y grandes ciudades como Gijón y Avilés.",
                    "Conocer su patrimonio: el arte prerrománico asturiano (Santa María del Naranco), Covadonga y los Picos de Europa, los Premios Princesa de Asturias y la cultura de la sidra y la fabada.",
                    "Practicar las expresiones «comunidad autónoma uniprovincial» y «entregar los Premios Princesa de Asturias en Oviedo»."
                ],
                "vocab": [
                    {"lemma": "el Principado de Asturias", "pos": "noun", "translation": "Principality of Asturias"},
                    {"lemma": "Oviedo", "pos": "noun", "translation": "Oviedo (capital of Asturias)"},
                    {"lemma": "Gijón", "pos": "noun", "translation": "Gijón (largest coastal city in Asturias)"},
                    {"lemma": "la comunidad uniprovincial", "pos": "noun", "translation": "single-province autonomous community"},
                    {"lemma": "los Premios Princesa de Asturias", "pos": "noun", "translation": "Princess of Asturias Awards"},
                    {"lemma": "el arte prerrománico asturiano", "pos": "noun", "translation": "Asturian Pre-Romanesque art"},
                    {"lemma": "la fabada asturiana", "pos": "noun", "translation": "Asturian bean stew (fabada)"},
                    {"lemma": "la sidra / el queso Cabrales", "pos": "noun", "translation": "Asturian cider / Cabrales blue cheese"}
                ],
                "grammar_title": "Organización territorial: las siete «comunidades autónomas uniprovinciales»",
                "grammar_text": "En España existen **siete comunidades autónomas uniprovinciales** (formadas por una sola provincia): **Asturias, Cantabria, La Rioja, Navarra, Comunidad de Madrid, Región de Murcia e Islas Baleares**. En el caso del **Principado de Asturias**, el nombre de la comunidad y provincia es Asturias y su capital es **Oviedo**.",
                "grammar_examples": [
                    {"es": "El Principado de Asturias es una comunidad autónoma uniprovincial cuya capital es la ciudad de Oviedo.", "en": "The Principality of Asturias is a single-province autonomous community whose capital is the city of Oviedo."},
                    {"es": "Cada otoño se entregan en el Teatro Campoamor de Oviedo los Premios Princesa de Asturias.", "en": "Every autumn the Princess of Asturias Awards are presented at the Campoamor Theater in Oviedo."}
                ],
                "grammar_tip": "No confundas en el CCSE la capital del Principado de Asturias (**Oviedo**, donde se entregan los Premios Princesa de Asturias) con su ciudad costera más poblada (**Gijón**).",
                "paragraphs": [
                    "Al este de Galicia, encajado entre la imponente Cordillera Cantábrica y las aguas del mar Cantábrico, se encuentra el Principado de Asturias, famoso por su lema turístico «Asturias, Paraíso Natural». Recibe el título histórico de Principado desde el siglo XIV porque el heredero o heredera de la Corona de España ostenta la dignidad tradicional de Príncipe o Princesa de Asturias.",
                    "Desde el punto de vista territorial, el Principado de Asturias es una de las siete comunidades autónomas uniprovinciales de España: cuenta con una sola provincia (Asturias) y su capital es la ciudad interior de Oviedo. Junto a Oviedo, su ciudad más poblada es el gran puerto marítimo e industrial de Gijón, al que se suma la ciudad portuaria y cultural de Avilés (sede del Centro Niemeyer).",
                    "En el corazón de Oviedo se levantan joyas únicas declaradas Patrimonio de la Humanidad por la UNESCO: los monumentos del arte prerrománico asturiano de los siglos IX y X, como Santa María del Naranco, San Miguel de Lillo y San Julián de los Prados, además de la Cámara Santa de su Catedral. Cada mes de octubre, el Teatro Campoamor de Oviedo se viste de gala para la entrega de los prestigiosos Premios Princesa de Asturias.",
                    "En el oriente asturiano se alzan los lagos de Covadonga (Enol y Ercina) y las cumbres calizas del Parque Nacional de los Picos de Europa, presididas por el mítico Naranjo de Bulnes (Picu Urriellu). Sus ríos cristalinos, como el Sella —famoso por la fiesta estival del Descenso Internacional del Sella en piragua entre Arriondas y Ribadesella— y el Narcea, son santuarios del salmón.",
                    "La cultura gastronómica asturiana es una de las más queridas de España: su plato más emblemático es la fabada asturiana (elaborada con alubias blancas llamadas «fabes», chorizo, morcilla y lacón), acompañada de sus decenas de variedades de quesos artesanales —encabezados por el queso azul de Cabrales, madurado en cuevas de los Picos de Europa— y de la sidra natural, cuya cultura de escanciado ha sido reconocida como Patrimonio Cultural Inmaterial de la Humanidad."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la capital de la comunidad autónoma uniprovincial del Principado de Asturias, sede de la entrega de los Premios Princesa de Asturias?",
                        "options": [
                            "Oviedo",
                            "Santander",
                            "Pamplona",
                            "Santiago de Compostela"
                        ],
                        "correctIndex": 0,
                        "explanation": "Oviedo es la capital del Principado de Asturias y alberga el Teatro Campoamor donde se entregan los Premios Princesa de Asturias."
                    },
                    {
                        "question": "¿Cuál es el plato tradicional más famoso de la gastronomía de Asturias, preparado con alubias blancas («fabes») y embutidos?",
                        "options": [
                            "La fabada asturiana",
                            "El gazpacho andaluz",
                            "La paella valenciana",
                            "El cocido madrileño"
                        ],
                        "correctIndex": 0,
                        "explanation": "La fabada asturiana y la sidra natural son los símbolos más conocidos de la gastronomía de Asturias."
                    },
                    {
                        "question": "¿Qué monumentos de los siglos IX y X situados en el monte Naranco de Oviedo son Patrimonio de la Humanidad por la UNESCO?",
                        "options": [
                            "Las iglesias del arte prerrománico asturiano, como Santa María del Naranco y San Miguel de Lillo",
                            "El Acueducto romano de Segovia",
                            "La Alhambra nazarí",
                            "La Sagrada Familia"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los monumentos de Oviedo y del Reino de Asturias (arte prerrománico asturiano) son Patrimonio de la Humanidad."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Por cuántas provincias está formado el Principado de Asturias?",
                        "options": [
                            "Por una sola provincia (es una comunidad autónoma uniprovincial)",
                            "Por cuatro provincias",
                            "Por ocho provincias",
                            "Por tres provincias"
                        ],
                        "correctIndex": 0,
                        "explanation": "Asturias es una de las siete comunidades autónomas uniprovinciales de España."
                    },
                    {
                        "prompt": "¿Cuál es la bebida tradicional de Asturias elaborada con manzana y servida mediante el arte del escanciado?",
                        "options": [
                            "La sidra",
                            "La horchata de chufa",
                            "El vino de Jerez",
                            "El cava catalán"
                        ],
                        "correctIndex": 0,
                        "explanation": "La sidra natural asturiana es la bebida tradicional del Principado."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La capital del Principado de Asturias es la ciudad de ___.",
                        "answer": "Oviedo",
                        "options": ["Oviedo", "Santander", "Bilbao", "Lugo"],
                        "explanation": "Oviedo es la capital del Principado de Asturias.",
                        "english": "The capital of the Principality of Asturias is the city of Oviedo."
                    },
                    {
                        "sentence": "La ___ asturiana y el queso de Cabrales son dos productos emblemáticos de la gastronomía de Asturias.",
                        "answer": "fabada",
                        "options": ["fabada", "paella", "ensaimada", "escalivada"],
                        "explanation": "La fabada asturiana es el plato tradicional más representativo de Asturias.",
                        "english": "Asturian fabada and Cabrales cheese are two emblematic products of the gastronomy of Asturias."
                    }
                ],
                "ex_dict": {
                    "audioText": "El Principado de Asturias es una comunidad uniprovincial cuya capital es la ciudad de Oviedo.",
                    "english": "The Principality of Asturias is a single-province community whose capital is the city of Oviedo."
                },
                "ex_sb": {
                    "words": ["Los", "Premios", "Princesa", "de", "Asturias", "se", "entregan", "en", "el", "Teatro", "Campoamor", "de", "Oviedo."],
                    "english": "The Princess of Asturias Awards are presented at the Campoamor Theater in Oviedo."
                }
            },
            {
                "num": "03",
                "Title": "Cantabria: Santander, Altamira y Valles Pasiegos",
                "title": "Cantabria: Santander, Altamira y Valles Pasiegos",
                "grammar_slug": "conocida-como-la-capilla-sixtina",
                "story_slug": "cantabria",
                "story_title": "Los bisontes de Altamira y la bahía de Santander",
                "objectives": [
                    "Identificar Cantabria como comunidad autónoma uniprovincial con capital en Santander.",
                    "Conocer la Cueva de Altamira (en Santillana del Mar, Patrimonio de la Humanidad), el Palacio de la Magdalena (sede de verano de la UIMP) y el valle de Liébana en los Picos de Europa.",
                    "Practicar las construcciones apositivas «conocido/a como» y «situado/a en el municipio de»."
                ],
                "vocab": [
                    {"lemma": "Cantabria", "pos": "noun", "translation": "Cantabria"},
                    {"lemma": "Santander", "pos": "noun", "translation": "Santander (capital of Cantabria)"},
                    {"lemma": "la Cueva de Altamira", "pos": "noun", "translation": "Cave of Altamira (Paleolithic cave art, UNESCO)"},
                    {"lemma": "el arte rupestre paleolítico", "pos": "noun", "translation": "Paleolithic rock/cave art"},
                    {"lemma": "Santillana del Mar", "pos": "noun", "translation": "Santillana del Mar (historic town in Cantabria)"},
                    {"lemma": "el Palacio de la Magdalena", "pos": "noun", "translation": "Magdalena Palace (Santander)"},
                    {"lemma": "el sobao pasiego / la quesada", "pos": "noun", "translation": "sobao pasiego sponge cake / quesada pasiega"},
                    {"lemma": "las anchoas de Santoña", "pos": "noun", "translation": "anchovies from Santoña"}
                ],
                "grammar_title": "Aposiciones culturales: «conocida como la Capilla Sixtina del arte rupestre»",
                "grammar_text": "En textos sobre patrimonio cultural se utiliza el participio **«conocido/a como»** para introducir el sobrenombre universal de un monumento: *La Cueva de Altamira, situada en Santillana del Mar (Cantabria), es **conocida como** «la Capilla Sixtina del arte rupestre paleolítico» por la perfección de sus bisontes policromados*.",
                "grammar_examples": [
                    {"es": "Cantabria es una comunidad autónoma uniprovincial del norte de España cuya capital es Santander.", "en": "Cantabria is a single-province autonomous community in northern Spain whose capital is Santander."},
                    {"es": "La Cueva de Altamira, descubierta en el siglo XIX en Cantabria, es Patrimonio de la Humanidad por la UNESCO.", "en": "The Cave of Altamira, discovered in the 19th century in Cantabria, is a UNESCO World Heritage Site."}
                ],
                "grammar_tip": "Pregunta clásica del CCSE: ¿En qué comunidad autónoma se encuentra la Cueva de Altamira, famosa por sus pinturas prehistóricas de bisontes? En Cantabria (cerca de Santillana del Mar).",
                "paragraphs": [
                    "Entre el Principado de Asturias al oeste, el País Vasco al este y Castilla y León al sur se extiende Cantabria, otra de las comunidades autónomas uniprovinciales de la España verde. En sus montañas de Fontibre nace el río Ebro, y en su costa se abre una de las bahías más hermosas del mundo: la bahía de Santander, capital de la comunidad autónoma.",
                    "Santander combina su tradición marinera con una intensa vida cultural y universitaria. En la península de la Magdalena se levanta el Palacio de la Magdalena, antigua residencia real de verano que desde hace décadas acoge los célebres cursos internacionales de verano de la Universidad Internacional Menéndez Pelayo (UIMP), mientras que junto al muelle brilla el vanguardista Centro Botín, diseñado por el arquitecto Renzo Piano.",
                    "A pocos kilómetros de Santander, en el municipio de Santillana del Mar, se encuentra uno de los mayores tesoros de la historia de la humanidad: la Cueva de Altamira. Descubierta en 1879 por Marcelino Sanz de Sautuola y su pequeña hija María («¡Mira, papá, bueyes pintados!»), sus pinturas de bisontes, caballos y ciervos de hace más de 14.000 años fueron bautizadas como «la Capilla Sixtina del arte rupestre paleolítico» y son Patrimonio de la Humanidad por la UNESCO.",
                    "El interior de Cantabria ofrece paisajes deslumbrantes, desde el Parque de la Naturaleza de Cabárceno hasta la comarca de Liébana, al pie del teleférico de Fuente Dé en el Parque Nacional de los Picos de Europa, donde se venera el Monasterio de Santo Toribio de Liébana. En la villa costera de Comillas sorprende además «El Capricho», una de las pocas obras construidas por el genial arquitecto modernista Antoni Gaudí fuera de Cataluña.",
                    "En la mesa cántabra destacan las célebres anchoas en aceite del puerto de Santoña, el cocido montañés y el cocido lebaniego, y la repostería tradicional de los Valles Pasiegos: los sobaos pasiegos y la quesada pasiega, elaborados con la excelente mantequilla y leche de sus praderas."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la capital de la comunidad autónoma uniprovincial de Cantabria?",
                        "options": [
                            "Santander",
                            "Oviedo",
                            "Vitoria-Gasteiz",
                            "Bilbao"
                        ],
                        "correctIndex": 0,
                        "explanation": "Santander es la capital de la comunidad autónoma de Cantabria."
                    },
                    {
                        "question": "¿En qué comunidad autónoma se encuentra la famosa Cueva de Altamira, declarada Patrimonio de la Humanidad por sus pinturas rupestres paleolíticas de bisontes?",
                        "options": [
                            "En Cantabria (en el municipio de Santillana del Mar)",
                            "En la Región de Murcia",
                            "En las Islas Baleares",
                            "En Extremadura"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Cueva de Altamira está situada en Santillana del Mar, en la comunidad autónoma de Cantabria."
                    },
                    {
                        "question": "¿Qué gran río español nace en Fontibre, en las montañas de Cantabria, antes de cruzar el noreste peninsular hasta el Mediterráneo?",
                        "options": [
                            "El río Ebro",
                            "El río Guadalquivir",
                            "El río Guadiana",
                            "El río Segura"
                        ],
                        "correctIndex": 0,
                        "explanation": "El río Ebro nace en Fontibre (Cantabria)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué palacio de Santander acoge cada verano los cursos internacionales de la Universidad Internacional Menéndez Pelayo (UIMP)?",
                        "options": [
                            "El Palacio de la Magdalena",
                            "El Palacio de la Aljafería",
                            "El Palacio de San Telmo",
                            "El Palacio de Fuensalida"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Palacio de la Magdalena en Santander es la sede histórica de los cursos de verano de la UIMP."
                    },
                    {
                        "prompt": "¿Cuáles son los dulces típicos más conocidos de los Valles Pasiegos en Cantabria?",
                        "options": [
                            "Los sobaos pasiegos y la quesada pasiega",
                            "Los piononos de Santa Fe",
                            "El turrón de Jijona",
                            "Los fartons valencianos"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los sobaos pasiegos y la quesada son los postres emblemáticos de Cantabria."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La capital de la comunidad autónoma de Cantabria es la ciudad costera de ___.",
                        "answer": "Santander",
                        "options": ["Santander", "Oviedo", "Pamplona", "Logroño"],
                        "explanation": "Santander es la capital de Cantabria.",
                        "english": "The capital of the autonomous community of Cantabria is the coastal city of Santander."
                    },
                    {
                        "sentence": "La Cueva de ___, en Cantabria, es mundialmente famosa por sus pinturas prehistóricas de bisontes.",
                        "answer": "Altamira",
                        "options": ["Altamira", "Doñana", "Covadonga", "Cabrera"],
                        "explanation": "La Cueva de Altamira (Santillana del Mar, Cantabria) alberga las célebres pinturas paleolíticas.",
                        "english": "The Cave of Altamira, in Cantabria, is world-famous for its prehistoric paintings of bison."
                    }
                ],
                "ex_dict": {
                    "audioText": "La Cueva de Altamira se encuentra en Cantabria y la capital de la comunidad es Santander.",
                    "english": "The Cave of Altamira is located in Cantabria and the capital of the community is Santander."
                },
                "ex_sb": {
                    "words": ["La", "Cueva", "de", "Altamira", "es", "famosa", "por", "sus", "pinturas", "rupestres", "en", "Cantabria."],
                    "english": "The Cave of Altamira is famous for its cave paintings in Cantabria."
                }
            },
            {
                "num": "04",
                "Title": "El País Vasco: Tres Provincias, Vitoria-Gasteiz y el Guggenheim",
                "title": "El País Vasco: Tres Provincias, Vitoria-Gasteiz y el Guggenheim",
                "grammar_slug": "compuesta-por-tres-territorios-historicos",
                "story_slug": "paisvasco",
                "story_title": "De Vitoria-Gasteiz al titanio de Bilbao y la Concha de San Sebastián",
                "objectives": [
                    "Memorizar las tres provincias (territorios históricos) del País Vasco (Euskadi): Álava (capital Vitoria-Gasteiz), Bizkaia (capital Bilbao) y Gipuzkoa (capital Donostia-San Sebastián).",
                    "Recordar que la sede de las instituciones comunes (capital autonómica) es Vitoria-Gasteiz, que el Museo Guggenheim está en Bilbao y que el Festival Internacional de Cine se celebra en San Sebastián.",
                    "Practicar las construcciones «compuesta por tres provincias» y «acoger el Museo Guggenheim / el Festival de Cine»."
                ],
                "vocab": [
                    {"lemma": "el País Vasco (Euskadi)", "pos": "noun", "translation": "Basque Country"},
                    {"lemma": "Álava, Bizkaia (Vizcaya) y Gipuzkoa (Guipúzcoa)", "pos": "noun", "translation": "the three provinces of the Basque Country"},
                    {"lemma": "Vitoria-Gasteiz", "pos": "noun", "translation": "Vitoria-Gasteiz (capital of Álava and institutional capital of the Basque Country)"},
                    {"lemma": "Bilbao", "pos": "noun", "translation": "Bilbao (capital of Bizkaia, home to the Guggenheim Museum)"},
                    {"lemma": "Donostia-San Sebastián", "pos": "noun", "translation": "San Sebastián (capital of Gipuzkoa, film festival host)"},
                    {"lemma": "el Museo Guggenheim Bilbao", "pos": "noun", "translation": "Guggenheim Museum Bilbao"},
                    {"lemma": "el Lehendakari / el Gobierno Vasco", "pos": "noun", "translation": "President of the Basque Government / Basque Government"},
                    {"lemma": "el Concierto Económico", "pos": "noun", "translation": "Basque Economic Agreement (foral tax system)"}
                ],
                "grammar_title": "Capitalidad frente a ciudad más poblada: el caso de Vitoria-Gasteiz y Bilbao",
                "grammar_text": "En el examen CCSE se pregunta a menudo por la capital del **País Vasco (Euskadi)** porque muchos candidatos la confunden con Bilbao (su ciudad más poblada). La respuesta correcta es **Vitoria-Gasteiz** (capital de la provincia de **Álava**), donde tienen su sede el Parlamento Vasco y el Gobierno Vasco presidido por el **Lehendakari**.",
                "grammar_examples": [
                    {"es": "El País Vasco está formado por tres provincias: Álava, Bizkaia y Gipuzkoa, y su capital es Vitoria-Gasteiz.", "en": "The Basque Country is formed by three provinces: Álava, Bizkaia, and Gipuzkoa, and its capital is Vitoria-Gasteiz."},
                    {"es": "El Museo Guggenheim se encuentra en la ciudad de Bilbao, mientras que San Sebastián acoge un famoso festival de cine.", "en": "The Guggenheim Museum is located in the city of Bilbao, while San Sebastián hosts a famous film festival."}
                ],
                "grammar_tip": "¡Tres datos de oro para el CCSE sobre el País Vasco! 1) Tres provincias: Álava, Bizkaia y Gipuzkoa. 2) Capital autonómica: Vitoria-Gasteiz. 3) Museo Guggenheim: en Bilbao.",
                "paragraphs": [
                    "En el extremo oriental de la cornisa cantábrica, donde los montes verdes se encuentran con el comienzo de los Pirineos y la frontera francesa, se sitúa el País Vasco o Euskadi. Es una comunidad autónoma bilingüe en la que el castellano comparte oficialidad con el euskera (o vasco), la lengua viva más antigua de Europa occidental.",
                    "El País Vasco está integrado por tres provincias, denominadas también en su Estatuto de Autonomía «territorios históricos»: Álava (Araba), en el interior; Bizkaia (Vizcaya), en la costa occidental; y Gipuzkoa (Guipúzcoa), en la costa oriental fronteriza con Francia. Cada territorio histórico cuenta con sus propias Juntas Generales y Diputación Foral, y disfruta del régimen fiscal propio del Concierto Económico.",
                    "¿Cuál es la capital del País Vasco? Aunque Bilbao es su área metropolitana más poblada, la sede de las instituciones comunes —el Parlamento Vasco y la residencia oficial del Lehendakari (presidente del Gobierno Vasco)— se encuentra en Vitoria-Gasteiz, capital de la provincia de Álava, famosa por su anillo verde ecológico y su casco medieval.",
                    "Por su parte, Bilbao (capital de Bizkaia), atravesada por la ría del Nervión y conectada en su desembocadura por el Puente Colgante de Bizkaia (Patrimonio de la Humanidad), protagonizó desde 1997 una transformación urbana admirada en todo el planeta gracias a la inauguración del Museo Guggenheim Bilbao, una escultura de titanio diseñada por el arquitecto canadiense-estadounidense Frank Gehry.",
                    "Finalmente, Donostia-San Sebastián (capital de Gipuzkoa), enmarcada por la célebre bahía de La Concha y el Peine del Viento del escultor Eduardo Chillida, acoge cada mes de septiembre el Festival Internacional de Cine de San Sebastián (donde se entrega la Concha de Oro) y es mundialmente famosa por su alta cocina y su cultura de los «pintxos»."
                ],
                "questions": [
                    {
                        "question": "¿Cuáles son las tres provincias (o territorios históricos) que componen la comunidad autónoma del País Vasco?",
                        "options": [
                            "Álava, Bizkaia (Vizcaya) y Gipuzkoa (Guipúzcoa)",
                            "A Coruña, Lugo y Ourense",
                            "Huesca, Zaragoza y Teruel",
                            "León, Palencia y Burgos"
                        ],
                        "correctIndex": 0,
                        "explanation": "El País Vasco está formado por las tres provincias de Álava, Bizkaia y Gipuzkoa."
                    },
                    {
                        "question": "¿Cuál es la capital institucional de la comunidad autónoma del País Vasco, sede del Parlamento Vasco y del Gobierno Vasco?",
                        "options": [
                            "Vitoria-Gasteiz",
                            "Bilbao",
                            "Donostia-San Sebastián",
                            "Pamplona"
                        ],
                        "correctIndex": 0,
                        "explanation": "Vitoria-Gasteiz (capital de Álava) es la sede de las instituciones comunes y capital del País Vasco."
                    },
                    {
                        "question": "¿En qué ciudad del País Vasco se encuentra el famoso Museo Guggenheim de arte contemporáneo, diseñado por Frank Gehry?",
                        "options": [
                            "En Bilbao",
                            "En Vitoria-Gasteiz",
                            "En San Sebastián",
                            "En Santander"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Museo Guggenheim está situado junto a la ría del Nervión en la ciudad de Bilbao (Bizkaia)."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Qué ciudad vasca celebra cada mes de septiembre un prestigioso Festival Internacional de Cine en el que se entrega la «Concha de Oro»?",
                        "options": [
                            "Donostia-San Sebastián",
                            "Vitoria-Gasteiz",
                            "Barakaldo",
                            "Eibar"
                        ],
                        "correctIndex": 0,
                        "explanation": "El Festival Internacional de Cine de San Sebastián entrega como máximo galardón la Concha de Oro."
                    },
                    {
                        "prompt": "¿Qué nombre recibe el presidente del Gobierno Vasco?",
                        "options": [
                            "Lehendakari",
                            "Síndic",
                            "Justicia Mayor",
                            "Regidor"
                        ],
                        "correctIndex": 0,
                        "explanation": "El presidente del Gobierno Vasco recibe la denominación oficial de Lehendakari."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La sede del Parlamento Vasco y capital del País Vasco es la ciudad de ___-Gasteiz.",
                        "answer": "Vitoria",
                        "options": ["Vitoria", "Bilbao", "Donostia", "Pamplona"],
                        "explanation": "Vitoria-Gasteiz es la capital institucional del País Vasco.",
                        "english": "The seat of the Basque Parliament and capital of the Basque Country is the city of Vitoria-Gasteiz."
                    },
                    {
                        "sentence": "El famoso Museo Guggenheim de arquitectura de titanio se encuentra en la ciudad de ___.",
                        "answer": "Bilbao",
                        "options": ["Bilbao", "Santander", "Oviedo", "Logroño"],
                        "explanation": "El Museo Guggenheim Bilbao fue inaugurado en 1997 en la capital vizcaína.",
                        "english": "The famous Guggenheim Museum of titanium architecture is located in the city of Bilbao."
                    }
                ],
                "ex_dict": {
                    "audioText": "El País Vasco está formado por Álava, Bizkaia y Gipuzkoa y su capital es Vitoria-Gasteiz.",
                    "english": "The Basque Country is formed by Álava, Bizkaia, and Gipuzkoa and its capital is Vitoria-Gasteiz."
                },
                "ex_sb": {
                    "words": ["El", "Museo", "Guggenheim", "se", "encuentra", "en", "la", "ciudad", "vasca", "de", "Bilbao."],
                    "english": "The Guggenheim Museum is located in the Basque city of Bilbao."
                }
            },
            {
                "num": "05",
                "Title": "Navarra y La Rioja: Del Pirineo a las Tierras del Vino",
                "title": "Navarra y La Rioja: Del Pirineo a las Tierras del Vino",
                "grammar_slug": "cuna-de-la-lengua-comunidad-foral",
                "story_slug": "navarrayrioja",
                "story_title": "San Fermín en Pamplona y los primeros versos en castellano en San Millán de la Cogolla",
                "objectives": [
                    "Identificar la Comunidad Foral de Navarra (uniprovincial, capital Pamplona, fiestas de San Fermín el 7 de julio) y La Rioja (uniprovincial, capital Logroño).",
                    "Conocer los Monasterios de San Millán de la Cogolla (Suso y Yuso) en La Rioja como cuna de las primeras palabras escritas en romance castellano y en euskera, así como la Denominación de Origen Calificada Rioja.",
                    "Practicar las expresiones «Comunidad Foral de Navarra» y «cuna de las primeras palabras escritas en castellano»."
                ],
                "vocab": [
                    {"lemma": "la Comunidad Foral de Navarra", "pos": "noun", "translation": "Chartered Community of Navarre"},
                    {"lemma": "Pamplona (Iruña)", "pos": "noun", "translation": "Pamplona (capital of Navarre)"},
                    {"lemma": "las fiestas de San Fermín", "pos": "noun", "translation": "San Fermín festival (July 6–14, Pamplona)"},
                    {"lemma": "La Rioja", "pos": "noun", "translation": "La Rioja"},
                    {"lemma": "Logroño", "pos": "noun", "translation": "Logroño (capital of La Rioja)"},
                    {"lemma": "los Monasterios de San Millán de la Cogolla", "pos": "noun", "translation": "Monasteries of San Millán de la Cogolla (Suso and Yuso, UNESCO)"},
                    {"lemma": "las Glosas Emilianenses", "pos": "noun", "translation": "Emilianense Glosses (first written notes in Spanish and Basque)"},
                    {"lemma": "la Denominación de Origen Calificada Rioja", "pos": "noun", "translation": "Rioja Qualified Designation of Origin (wine)"}
                ],
                "grammar_title": "Denominaciones históricas y culturales: «Comunidad Foral» y «cuna del castellano»",
                "grammar_text": "En la geografía política de España, Navarra recibe el nombre oficial de **Comunidad Foral de Navarra** porque conserva su régimen foral histórico y su propio Convenio Económico. Por su parte, **La Rioja** alberga los **Monasterios de San Millán de la Cogolla (Suso y Yuso)**, considerados la **«cuna del castellano escrito»**.",
                "grammar_examples": [
                    {"es": "Pamplona es la capital de la Comunidad Foral de Navarra y celebra en julio las fiestas de San Fermín.", "en": "Pamplona is the capital of the Chartered Community of Navarre and celebrates the festival of San Fermín in July."},
                    {"es": "Logroño es la capital de La Rioja, comunidad famosa en todo el mundo por sus vinos y por los monasterios de San Millán.", "en": "Logroño is the capital of La Rioja, a community famous worldwide for its wines and the monasteries of San Millán."}
                ],
                "grammar_tip": "Recuerda para el CCSE: Navarra (capital Pamplona) y La Rioja (capital Logroño) son dos comunidades autónomas uniprovinciales bañadas por el río Ebro.",
                "paragraphs": [
                    "Al sur del País Vasco y de la cordillera de los Pirineos, siguiendo el curso alto del río Ebro, se encuentran dos comunidades autónomas uniprovinciales de extraordinaria personalidad histórica y cultural: la Comunidad Foral de Navarra y La Rioja. Por ambas entra en España y avanza hacia el oeste el Camino de Santiago Francés, cruzando desde Roncesvalles hasta Pamplona, Puente la Reina, Estella, Logroño, Nájera y Santo Domingo de la Calzada.",
                    "La Comunidad Foral de Navarra —que conserva su histórico régimen foral y su propio Convenio Económico fiscal— tiene su capital en la ciudad de Pamplona (Iruña en euskera, lengua que es cooficial junto al castellano en la zona vascófona del norte navarro). Su geografía ofrece en pocos kilómetros un contraste asombroso: desde los bosques húmedos del Pirineo (como la Selva de Irati, uno de los mayores hayedos de Europa) hasta el paisaje semidesértico de las Bardenas Reales en el sur.",
                    "Cada año, del 6 al 14 de julio, Pamplona se convierte en el centro de todas las miradas internacionales con las fiestas de San Fermín, inmortalizadas por el escritor estadounidense Ernest Hemingway en su novela «Fiesta» (*The Sun Also Rises*), que comienzan con el lanzamiento del «chupinazo» el 6 de julio al mediodía y continúan con los encierros cada mañana del 7 al 14 de julio.",
                    "Justo al suroeste de Navarra, en la margen derecha del río Ebro, se extiende La Rioja, la comunidad autónoma de menor población de la España peninsular, cuya capital es la acogedora ciudad de Logroño. El nombre de La Rioja es sinónimo universal de cultura vitivinícola: sus bodegas centenarias y vanguardistas producen los vinos de la Denominación de Origen Calificada (DOCa) Rioja, la más antigua de España.",
                    "Pero La Rioja guarda además un tesoro espiritual y lingüístico único en el mundo hispanohablante: en un valle al pie de la sierra de la Demanda se alzan los Monasterios de San Millán de la Cogolla (los monasterios de Suso, arriba, y de Yuso, abajo), declarados Patrimonio de la Humanidad por la UNESCO. Allí, hace más de mil años, un monje anotó en los márgenes de un códice latino las Glosas Emilianenses: las primeras frases escritas en romance hispánico y también las primeras palabras en euskera."
                ],
                "questions": [
                    {
                        "question": "¿Cuál es la capital de la Comunidad Foral de Navarra, mundialmente famosa por celebrar en julio las fiestas de San Fermín?",
                        "options": [
                            "Pamplona",
                            "Logroño",
                            "Vitoria-Gasteiz",
                            "Zaragoza"
                        ],
                        "correctIndex": 0,
                        "explanation": "Pamplona es la capital de la Comunidad Foral de Navarra y celebra las fiestas de San Fermín del 6 al 14 de julio."
                    },
                    {
                        "question": "¿Cuál es la capital de la comunidad autónoma uniprovincial de La Rioja?",
                        "options": [
                            "Logroño",
                            "Pamplona",
                            "Soria",
                            "Burgos"
                        ],
                        "correctIndex": 0,
                        "explanation": "Logroño, a orillas del río Ebro, es la capital de La Rioja."
                    },
                    {
                        "question": "¿Qué monasterios situados en La Rioja son Patrimonio de la Humanidad por ser considerados la cuna de las primeras palabras escritas en romance castellano y en euskera?",
                        "options": [
                            "Los Monasterios de San Millán de la Cogolla (Suso y Yuso)",
                            "El Monasterio de El Escorial",
                            "El Monasterio de Poblet",
                            "El Monasterio de Guadalupe"
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Monasterios de San Millán de la Cogolla (Suso y Yuso), en La Rioja, son la cuna de las Glosas Emilianenses."
                    }
                ],
                "ex_mc": [
                    {
                        "prompt": "¿Por qué producto agroalimentario con Denominación de Origen Calificada es mundialmente conocida la comunidad autónoma de La Rioja?",
                        "options": [
                            "Por sus vinos (vino de Rioja)",
                            "Por los plátanos subtropicales",
                            "Por el arroz de marisma",
                            "Por los dátiles"
                        ],
                        "correctIndex": 0,
                        "explanation": "La Denominación de Origen Calificada Rioja es una de las regiones vinícolas más prestigiosas del mundo."
                    },
                    {
                        "prompt": "¿En qué fecha se celebra el día grande de las fiestas de San Fermín en Pamplona?",
                        "options": [
                            "El 7 de julio (las fiestas duran del 6 al 14 de julio)",
                            "El 19 de marzo",
                            "El 15 de mayo",
                            "El 31 de diciembre"
                        ],
                        "correctIndex": 0,
                        "explanation": "El 7 de julio es el día de San Fermín en Pamplona, dentro de las fiestas que se celebran del 6 al 14 de julio."
                    }
                ],
                "ex_fb": [
                    {
                        "sentence": "La capital de la Comunidad Foral de Navarra es la ciudad de ___.",
                        "answer": "Pamplona",
                        "options": ["Pamplona", "Logroño", "Santander", "Oviedo"],
                        "explanation": "Pamplona es la capital de Navarra.",
                        "english": "The capital of the Chartered Community of Navarre is the city of Pamplona."
                    },
                    {
                        "sentence": "La capital de la comunidad autónoma de La Rioja es la ciudad de ___.",
                        "answer": "Logroño",
                        "options": ["Logroño", "Pamplona", "Vitoria", "Huesca"],
                        "explanation": "Logroño es la capital de La Rioja.",
                        "english": "The capital of the autonomous community of La Rioja is the city of Logroño."
                    }
                ],
                "ex_dict": {
                    "audioText": "Pamplona es la capital de la Comunidad Foral de Navarra y Logroño es la capital de La Rioja.",
                    "english": "Pamplona is the capital of the Chartered Community of Navarre and Logroño is the capital of La Rioja."
                },
                "ex_sb": {
                    "words": ["Los", "Monasterios", "de", "San", "Millán", "de", "la", "Cogolla", "se", "encuentran", "en", "La", "Rioja."],
                    "english": "The Monasteries of San Millán de la Cogolla are located in La Rioja."
                }
            }
        ]
    }
]


def main():
    for u in UNITS_16_17_18:
        emit_unit_from_dict(u)


if __name__ == "__main__":
    main()
