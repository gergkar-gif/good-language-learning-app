"""
Generates rich, detailed narrative stories for Block 4 (Units 19-24, 30 lessons).
Units:
19: populismo
20: industrializacion
21: revolucioncubana
22: guerrafria
23: eeuu
24: gobiernosmilitares

Embeds every grammar sentence directly from reqs JSON to ensure 100% verbatim accuracy.
"""

import json
import os

reqs = json.load(open('scripts/block4_all_reqs.json', encoding='utf-8'))

def G(lesson_key, idx):
    return reqs[lesson_key]['grammar_sentences'][idx]

STORIES = {}

# =============================================================================
# UNIT 19: populismo
# =============================================================================

# 19.01: populismo-01
k = "populismo-01"
# Grammar (7):
# 0: El populismo surgió en un contexto de crisis económica y transformación social.
# 1: Los líderes populistas apelaron a sectores populares que antes tenían poca representación.
# 2: Las demandas sociales aumentaron mientras las ciudades crecían rápidamente.
# 3: El término "populismo" ha adquirido tantos significados diferentes en el debate político cotidiano que resulta casi imposible utilizarlo sin generar confusión.
# 4: Es precisamente esta ambigüedad lo que hace que definir el populismo clásico resulte un ejercicio analítico tan necesario.
# 5: El populismo clásico latinoamericano se caracterizó por una combinación muy específica de elementos.
# 6: Esta combinación distingue claramente al populismo latinoamericano de otros movimientos políticos del periodo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El concepto de populismo clásico en América Latina",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 4)} En las ciencias sociales y la historia, el término no es un simple insulto ni un elogio, sino una categoría precisa para describir una etapa crucial del siglo veinte."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 2)} El colapso del modelo agroexportador tras el crac de 1929 y la rápida migración del campo a las fábricas urbanas crearon una masa trabajadora excluida del sufragio efectivo y de los beneficios de la riqueza nacional."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 5)} Figuras emblemáticas como Juan Domingo Perón en Argentina, Getúlio Vargas en Brasil y Lázaro Cárdenas en México rompieron las viejas formas de la política oligárquica mediante un estilo de liderazgo directo y carismático."
        },
        {
            "type": "narration",
            "text": f"Estos regímenes combinaron una retórica nacionalista antiimperialista, políticas de industrialización acelerada por sustitución de importaciones y una masiva redistribución de la renta hacia los asalariados a través de sindicatos tutelados por el Estado."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Lejos de ser meras dictaduras militares o democracias liberales convencionales, los populismos clásicos refundaron el pacto social y democratizaron el consumo popular en toda la región."
        }
    ]
}

# 19.02: populismo-02
k = "populismo-02"
# Grammar (7):
# 0: Juan Domingo Perón gobernó Argentina apoyándose en el movimiento obrero organizado.
# 1: Eva Perón desempeñó un papel central en la relación con los trabajadores y los sectores marginados.
# 2: Las políticas sociales ampliaron derechos laborales que beneficiaron a miles de trabajadores.
# 3: El peronismo transformó la política argentina mediante una combinación de reformas y movilización popular.
# 4: Entre 1946 y 1955, el peronismo transformó la vida cotidiana de millones de trabajadores argentinos de una manera que ningún gobierno anterior había conseguido.
# 5: Para las familias trabajadoras, el peronismo significó vacaciones pagadas por primera vez en la vida, aguinaldo y acceso garantizado a la salud pública.
# 6: Esta experiencia explica por qué el peronismo mantuvo una lealtad popular indestructible durante décadas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El peronismo: justicia social y movilización de masas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El 17 de octubre de 1945, una multitudinaria manifestación de obreros procedentes de los suburbios fabriles de Buenos Aires y Berisso ocupó la Plaza de Mayo para exigir la liberación del coronel Juan Domingo Perón. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Elegido presidente en 1946, Perón impulsó los convenios colectivos de trabajo, la indemnización por despido y el estatuto del peón rural. {G(k, 2)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} A través de la Fundación Eva Perón, 'Evita' distribuyó ayuda social directa, construyó policlínicos y hogares escuela, y encabezó la lucha cívica que consagró en 1947 el voto femenino en Argentina."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} El peronismo nacionalizó los ferrocarriles británicos, el gas y los teléfonos, al tiempo que creaba el IAPI para centralizar el comercio exterior de granos y transferir divisas a la industria pesada."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} a pesar del golpe militar que derrocó a Perón en 1955 y de los casi veinte años de proscripción que sufrió su movimiento."
        }
    ]
}

# 19.03: populismo-03
k = "populismo-03"
# Grammar (7):
# 0: Getúlio Vargas transformó el Estado brasileño mediante leyes laborales y reformas institucionales.
# 1: Lázaro Cárdenas impulsó el reparto agrario y la nacionalización del petróleo en México.
# 2: Ambos líderes buscaron incorporar a los trabajadores dentro de un proyecto nacional.
# 3: Las reformas cambiaron la estructura productiva mientras el Estado aumentaba su intervención económica.
# 4: Tanto Vargas como Cárdenas gobernaron en momentos de profunda transformación social, aunque sus proyectos políticos siguieron trayectorias muy diferentes.
# 5: Mientras Cárdenas basó su proyecto principalmente en la movilización campesina, Vargas se apoyó sobre todo en la clase obrera urbana en rápida expansión.
# 6: Ambos líderes compartían, sin embargo, una convicción fundamental: la necesidad de que el Estado nacional asumiera el control de los recursos estratégicos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Getúlio Vargas y Lázaro Cárdenas: las vías brasileña y mexicana",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 4)} En Brasil, Getúlio Vargas llegó al poder tras la Revolución de 1930 y proclamó en 1937 el 'Estado Novo', centralizando la administración e impulsando la industria siderúrgica de Volta Redonda. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"En México, el general Lázaro Cárdenas ejerció la presidencia entre 1934 y 1940, transformando el partido oficial en el PRM corporativo. {G(k, 1)} Cárdenas distribuyó más de veinte millones de hectáreas en ejidos colectivos como La Laguna y decretó la expropiación petrolera el 18 de marzo de 1938."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} Vargas promulgó la Consolidación de las Leyes del Trabajo (CLT) y fundó Petrobras bajo el lema 'El petróleo es nuestro', ganándose el apelativo de 'padre de los pobres'."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 6)} Ambos mandatarios desafiaron las presiones diplomáticas de Washington y Londres para edificar una soberanía energética propia."
        },
        {
            "type": "narration",
            "text": f"La huella de Vargas y Cárdenas consolidó un modelo de capitalismo de Estado y justicia distributiva que definió el desarrollo de las dos mayores economías de la región durante más de medio siglo."
        }
    ]
}

# 19.04: populismo-04
k = "populismo-04"
# Grammar (7):
# 0: Es cuestionable que este "pueblo" invocado constantemente por los líderes populistas corresponda realmente a toda la población de un país.
# 1: Muchos politólogos consideran preocupante esta relación directa entre líder y masas, ya que tiende a debilitar los mecanismos institucionales de control.
# 2: Es también cuestionable que la radio resultara, en sí misma, un factor puramente neutral.
# 3: Sería igualmente cuestionable que redujéramos el populismo latinoamericano a un simple fenómeno de manipulación de masas.
# 4: A raíz de una crisis, un dirigente puede presentar al pueblo como una comunidad unida frente a las élites.
# 5: En el marco de esta retórica, el liderazgo puede parecer una expresión directa de la voluntad popular.
# 6: La retórica puede movilizar grupos diversos, aunque simplifique conflictos que tienen causas diferentes.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Pueblo y líder: el debate sobre el discurso y la democracia",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El rasgo discursivo más distintivo de los líderes populistas fue la división binaria de la sociedad entre el 'pueblo' virtuoso y trabajador, y una 'oligarquía' egoísta vendida a intereses extranjeros. {G(k, 4)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} Con frecuencia, las clases medias urbanas opositoras, los intelectuales disidentes y los partidos de izquierda independiente quedaban estigmatizados como enemigos de la nación. {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"El auge de la radioemisora en las décadas de 1930 y 1940 permitió a los gobernantes comunicarse sin intermediarios con los hogares obreros. {G(k, 2)} El micrófono magnificó el magnetismo oratorio de Perón, Vargas y Gaitán en Colombia."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} El culto a la personalidad, la censura de prensa y la subordinación del poder judicial generaron intensas críticas democráticas por parte de los sectores republicanos tradicionales."
        },
        {
            "type": "narration",
            "text": f"No obstante, {G(k, 3)} Para millones de ciudadanos antes invisibilizados, el populismo constituyó una experiencia emancipadora de reconocimiento social y dignidad humana irrenunciable."
        }
    ]
}

# 19.05: populismo-05
k = "populismo-05"
# Grammar (7):
# 0: Algunos grupos fueron incorporados a la política mientras se ampliaban determinadas políticas sociales.
# 1: Los casos latinoamericanos deben ser comparados porque presentan semejanzas y diferencias importantes.
# 2: La polarización puede ser aumentada por un discurso político que presenta el conflicto como una oposición entre grupos.
# 3: Si bien resulta innegable que estos movimientos produjeron mejoras materiales genuinas, también es cierto que debilitaron las instituciones democráticas de sus países.
# 4: Si bien Perón y Cárdenas representan casos bastante distintos, también es cierto que ambos dejaron una huella política que sus países todavía siguen procesando.
# 5: Si bien el fenómeno suele asociarse principalmente con Argentina y México, también es cierto que surgieron movimientos comparables en Brasil, bajo Getúlio Vargas.
# 6: Si bien resulta tentador reducir el populismo a una simple historia de héroes o villanos, también es cierto que la evidencia histórica exige un juicio más matizado.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El legado populista: conquistas sociales y tensiones institucionales",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El balance histórico del populismo clásico en América Latina continúa siendo objeto de apasionadas controversias entre historiadores y economistas. {G(k, 6)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Movimientos análogos florecieron en Ecuador con José María Velasco Ibarra, en Bolivia con el MNR de Víctor Paz Estenssoro y en Colombia con el fervor popular desatado por Jorge Eliécer Gaitán. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Salarios reales más altos, hospitales públicos y sindicatos robustos coexistieron con tendencias autoritarias, clientelismo estatal y persecución a opositores parlamentarios."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Las élites tradicionales desplazadas conspiraron activamente con sectores militares reaccionarios, desembocando en sangrientos golpes de Estado como el bombardeo de Plaza de Mayo en 1955 y el suicidio de Vargas en 1954."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} El populismo refundó las identidades políticas populares e instaló para siempre la exigencia innegociable de soberanía económica y justicia distributiva en el continente."
        }
    ]
}

# =============================================================================
# UNIT 20: industrializacion
# =============================================================================

# 20.01: industrializacion-01
k = "industrializacion-01"
# Grammar (8):
# 0: La CEPAL fue creada porque se buscaba promover el desarrollo económico de la región.
# 1: Las economías industriales exportaban manufacturas mientras América Latina dependía de materias primas.
# 2: Se propusieron políticas para impulsar la producción interna y reducir la vulnerabilidad externa.
# 3: El economista argentino Raúl Prebisch demostró que las materias primas tendían a perder valor relativo frente a los productos industriales.
# 4: Esta conclusión ponía en cuestión uno de los dogmas centrales de la economía clásica tradicional.
# 5: La teoría del deterioro de los términos de intercambio se convirtió en el fundamento teórico de las políticas de industrialización.
# 6: América Latina necesitaba construir una base industrial propia para romper esta trampa estructural.
# 7: Aunque la estrategia buscaba desarrollar la industria, sus resultados fueron diferentes según el país.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La CEPAL, Raúl Prebisch y el deterioro de los términos de intercambio",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En 1948, las Naciones Unidas establecieron en Santiago de Chile la Comisión Económica para América Latina (CEPAL). {G(k, 0)} Bajo el liderazgo del economista argentino Raúl Prebisch, la CEPAL revolucionó el pensamiento económico del Sur global."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Prebisch argumentó que el comercio mundial estaba estructurado en un 'centro' industrializado y una 'periferia' proveedora de alimentos y minerales. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Con el paso del tiempo, los países latinoamericanos debían entregar cada vez más toneladas de café, cobre o trigo para comprar la misma máquina o tractor importado. {G(k, 4)} La teoría convencional de las 'ventajas comparativas' de David Ricardo quedaba así refutada empíricamente."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} Para salir del subdesarrollo crónico, el Estado debía asumir un rol planificador activo y proteger las manufacturas nacionales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} {G(k, 7)} Las tesis de Prebisch y la CEPAL dotaron a los gobiernos latinoamericanos de una doctrina económica rigurosa para justificar la protección arancelaria y la inversión pública."
        }
    ]
}

# 20.02: industrializacion-02
k = "industrializacion-02"
# Grammar (8):
# 0: Se adoptaron aranceles que protegían a las industrias emergentes de la competencia exterior.
# 1: El Estado financió infraestructuras mientras las empresas privadas invertían en nuevos sectores.
# 2: Los subsidios fueron otorgados para estimular la producción en áreas estratégicas.
# 3: La política de sustitución de importaciones comenzó protegiendo la producción de bienes de consumo no duraderos.
# 4: El objetivo final era mucho más ambicioso: alcanzar la producción de bienes intermedios y de capital.
# 5: Los aranceles proteccionistas crearon un mercado cautivo que garantizaba la rentabilidad de las fábricas locales.
# 6: Esta combinación de medidas permitió que la industria creciera a un ritmo impresionante durante las décadas de 1950 y 1960.
# 7: Gracias en gran medida al impulso sostenido por parte de estos gobiernos, países como Brasil ya contaban con sectores industriales complejos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Aranceles, subsidios y las etapas de la ISI",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Inspirados por el pensamiento cepalino, los gobiernos de América Latina desplegaron un vasto arsenal de herramientas de política pública para fomentar las fábricas nacionales. {G(k, 0)} {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} como calzado, textiles, alimentos elaborados, cerveza, jabones y medicamentos básicos. {G(k, 5)} Los consumidores urbanos compraban productos hechos en el país en lugar de marcas extranjeras."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, la sustitución 'fácil' de bienes de consumo liviano pronto alcanzó su límite técnico. {G(k, 4)} Para sostener el crecimiento, era indispensable fabricar acero, químicos, fertilizantes, motores, camiones y maquinaria pesada en suelo patrio."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Empresas estatales de electricidad y petroquímica suministraron insumos baratos a las industrias manufactureras privadas en São Paulo, Córdoba, Medellín y Monterrey."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} {G(k, 7)} Miles de chimeneas industriales alteraron el horizonte de las grandes urbes, forjando una economía crecientemente diversificada y moderna."
        }
    ]
}

# 20.03: industrializacion-03
k = "industrializacion-03"
# Grammar (8):
# 0: Las empresas estatales fueron creadas para controlar sectores estratégicos.
# 1: El Estado construyó carreteras y centrales eléctricas para apoyar el crecimiento industrial.
# 2: La planificación económica fue utilizada para coordinar las inversiones públicas.
# 3: El Estado asumió el papel de empresario directo en sectores donde la inversión privada resultaba insuficiente.
# 4: La creación de empresas petroleras estatales como Pemex y Petrobras simbolizó esta nueva vocación nacionalista.
# 5: Las empresas siderúrgicas de propiedad pública permitieron abastecer de acero a la industria manufacturera nacional.
# 6: Este modelo convirtió al Estado en el actor económico más poderoso de la sociedad latinoamericana.
# 7: Esta migración masiva no dejaría de transformar el propio rostro demográfico de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Estado empresario y las grandes corporaciones públicas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Dado que la burguesía privada nacional carecía del capital y la tecnología requeridos para acometer megaproyectos de infraestructura, el sector público dio un paso al frente. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Empresas como YPF en Argentina, PEMEX en México, Petrobras en Brasil y ENAP en Chile aseguraron el combustible nacional para las plantas fabriles y el transporte de carga."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} La usina de Volta Redonda en Brasil, Altos Hornos de México (AHMSA) y SOMISA en Argentina transformaron el mineral de hierro en vigas y láminas para la construcción."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Represas hidroeléctricas monumentales como Furnas en Brasil y el complejo Chocón-Cerros Colorados en la Patagonia iluminaron las ciudades. {G(k, 2)} a través de bancos como el BNDES y NAFIN."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Millones de campesinos migraron hacia las fábricas urbanas atraídos por los empleos industriales. {G(k, 7)}"
        }
    ]
}

# 20.04: industrializacion-04
k = "industrializacion-04"
# Grammar (8):
# 0: La industria dependía de maquinaria importada, aunque producía para el mercado interno.
# 1: Se generó empleo urbano, mientras el sector agrario perdía importancia económica.
# 2: La inflación aumentó cuando los gobiernos recurrieron a la emisión monetaria para financiar el gasto público.
# 3: El modelo comenzó a mostrar limitaciones estructurales que resultaron difíciles de superar.
# 4: La dependencia respecto a la importación de bienes de capital se convirtió en una trampa recurrente.
# 5: Los mercados internos relativamente pequeños no permitían alcanzar economías de escala eficientes.
# 6: Las crisis periódicas de balanza de pagos obligaron a frenar el crecimiento económico de manera reiterada.
# 7: Por más que estas transformaciones sociales resultaran genuinamente profundas, no lograron eliminar las viejas desigualdades heredadas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Límites estructurales, cuellos de botella y estrangulamiento externo",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Hacia fines de la década de 1960, el modelo de industrialización sustitutiva comenzó a exhibir graves cuellos de botella. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Para fabricar automóviles, electrodomésticos o fármacos, los países latinoamericanos debían importar costosas patentes, maquinaria de precisión y componentes electrónicos de Estados Unidos, Alemania y Japón."
        },
        {
            "type": "narration",
            "text": f"Como las exportaciones industriales hacia el exterior eran mínimas debido a altos costos locales y baja competitividad, los países sufrían escasez crónica de dólares. {G(k, 6)} Estos ciclos de 'pare y siga' (stop and go) paralizaban periódicamente la producción."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Fuera de gigantes como Brasil y México, las poblaciones de países medianos carecían del poder adquisitivo suficiente para sostener fábricas gigantescas. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 7)} El descuido de la productividad agraria aceleró el éxodo campesino, desbordando los suburbios de las metrópolis y agudizando las contradicciones distributivas."
        }
    ]
}

# 20.05: industrializacion-05
k = "industrializacion-05"
# Grammar (8):
# 0: La industrialización transformó la estructura productiva, aunque persistieron desigualdades regionales.
# 1: Se desarrollaron capacidades técnicas que beneficiaron al país en las décadas siguientes.
# 2: El debate sobre el modelo de desarrollo continuó mientras cambiaban las condiciones internacionales.
# 3: A pesar de sus contradicciones, la ISI transformó a América Latina en una sociedad predominantemente urbana e industrial.
# 4: Las fábricas creadas durante este periodo formaron a generaciones de ingenieros, técnicos y obreros calificados.
# 5: La infraestructura construida sentó las bases materiales del desarrollo contemporáneo de la región.
# 6: El modelo demostró que los países latinoamericanos eran capaces de producir bienes manufacturados complejos.
# 7: Sin embargo, algunos países mantuvieron una fuerte dependencia de las materias primas, mientras otros diversificaron su producción.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El balance histórico de la ISI y la modernización productiva",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Al evaluar el periodo de la industrialización dirigida por el Estado entre 1930 y 1975, el saldo histórico revela una transformación estructural profunda e irreversible. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Argentina produjo aviones a reacción y turbinas hidroeléctricas en Córdoba; Brasil levantó una industria automotriz y aeroespacial de clase mundial como Embraer; y México ensambló maquinaria pesada y productos químicos avanzados."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 1)} Politécnicos e institutos universitarios de tecnología florecieron en todo el continente, generando un invaluable capital humano técnico y científico."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Redes viales pavimentadas, tendidos de alta tensión y sistemas de telecomunicaciones conectaron para siempre las geografías nacionales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} {G(k, 2)} A pesar del posterior viraje neoliberal de los años ochenta y noventa, la base industrial construida durante la era de la ISI continúa siendo el pilar productivo de las principales naciones latinoamericanas."
        }
    ]
}

# =============================================================================
# UNIT 21: revolucioncubana
# =============================================================================

# 21.01: revolucioncubana-01
k = "revolucioncubana-01"
# Grammar (7):
# 0: La dictadura de Batista fue criticada porque limitaba la participación política y reprimía a sus opositores.
# 1: La economía dependía del azúcar, mientras algunos sectores urbanos se beneficiaban del turismo.
# 2: La corrupción aumentó el descontento, aunque la situación económica no afectaba a todos de la misma manera.
# 3: Lejos de ser uno de los países más pobres de la región, Cuba contaba con uno de los ingresos per cápita más altos de América Latina.
# 4: Lejos de reflejar una prosperidad ampliamente compartida, esta riqueza convivía con una desigualdad social profunda.
# 5: Lejos de ser una economía plenamente independiente, la de Cuba dependía casi por completo de una cuota especial de exportación de azúcar hacia Estados Unidos.
# 6: Esta combinación reunía, precisamente, las condiciones que analizamos como precondiciones típicas para una revolución genuina.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Cuba antes de 1959: opulencia habanera y drama campesino",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En la década de 1950, la isla de Cuba presentaba ante el mundo una fachada de cosmopolitismo y modernidad deslumbrante. {G(k, 3)} La Habana ostentaba lujosos hoteles como el Riviera y el Nacional, casinos administrados por la mafia de Meyer Lansky y una vibrante vida cultural nocturna."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, la realidad social era profundamente desgarradora. {G(k, 4)} Mientras las élites disfrutaban del lujo urbano, en los campos del oriente cubano cientos de miles de peones vivían en chozas de guano y pisos de tierra, sufriendo desnutrición infantil y analfabetismo durante el largo 'tiempo muerto' entre cosechas de zafra."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Empresas de Wall Street controlaban los mayores ingenios azucareros, los ferrocarriles, la telefonía y las refinerías petroleras de la isla. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"En el plano político, el golpe de Estado del 10 de marzo de 1952 encabezado por el general Fulgencio Batista clausuró la vida constitucional y desató una ola de corrupción y abusos policíacos. {G(k, 0)} {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La indignación moral de las clases medias, el sufrimiento rural y el cierre de las vías pacíficas convirtieron a Cuba en un polvorín a punto de estallar."
        }
    ]
}

# 21.02: revolucioncubana-02
k = "revolucioncubana-02"
# Grammar (7):
# 0: El ataque fracasó casi por completo, y Castro acabó por pasar casi dos años en prisión.
# 1: Castro organizó un pequeño grupo armado que acabó por desembarcar en Cuba en diciembre de 1956.
# 2: Los pocos sobrevivientes acabaron por refugiarse en las montañas de la Sierra Maestra, iniciando una guerra de guerrillas prolongada.
# 3: Ante el avance imparable de las fuerzas rebeldes, Batista acabó por huir del país hacia República Dominicana.
# 4: Los rebeldes organizaron una guerrilla en la Sierra Maestra mientras intentaban aumentar su apoyo.
# 5: Castro fue encarcelado después del ataque al cuartel Moncada, aunque continuó defendiendo sus objetivos.
# 6: El movimiento revolucionario ganó fuerza porque consiguió combinar acción militar y movilización política.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Fidel Castro, el asalto al Moncada y la Sierra Maestra",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El 26 de julio de 1953, un centenar de jóvenes encabezados por un joven abogado llamado Fidel Castro asaltó el cuartel Moncada en Santiago de Cuba. {G(k, 0)} Durante su juicio, Castro pronunció su célebre alegato 'La historia me absolverá'. {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"Amnistíado en 1955, viajó a México para fundar el Movimiento 26 de Julio (M-26-7) y entrenar a sus combatientes junto a su hermano Raúl y el médico argentino Ernesto 'Che' Guevara. {G(k, 1)} Ochenta y dos expedicionarios navegaron en el sobrecargado yate 'Granma' hasta encallar en los manglares de Las Coloradas."
        },
        {
            "type": "narration",
            "text": f"Sorprendidos por el ejército de Batista en Alegría de Pío, {G(k, 2)} En las cumbres de la Sierra Maestra instalaron Radio Rebelde, repartieron tierras a los campesinos y repelieron la ofensiva militar de verano. {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"A finales de 1958, las columnas rebeldes de Camilo Cienfuegos y el Che Guevara avanzaron hacia el occidente, descarrilando el tren blindado en la batalla de Santa Clara. {G(k, 6)} El 1 de enero de 1959, {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"Fidel Castro y los barbudos entraron triunfantes en La Habana en medio de un delirio popular multitudinario, poniendo fin a la dictadura y abriendo una nueva era revolucionaria en el hemisferio."
        }
    ]
}

# 21.03: revolucioncubana-03
k = "revolucioncubana-03"
# Grammar (7):
# 0: El gobierno se mostraba cada vez menos dispuesto a mantener relaciones normales con las empresas estadounidenses, y cada vez más decidido a impulsar una reforma agraria radical.
# 1: El gobierno de Castro se volvió cada vez menos tolerante con la oposición interna, y cada vez más dispuesto a nacionalizar propiedades estadounidenses.
# 2: Cuba se volvía cada vez menos dependiente del comercio estadounidense y cada vez más cercana a la Unión Soviética.
# 3: El gobierno se volvió cada vez menos parecido a los movimientos populistas, y cada vez más parecido a los regímenes de partido único de tipo soviético.
# 4: Se impulsó una reforma agraria mientras el gobierno intentaba transformar la estructura económica.
# 5: Las empresas fueron nacionalizadas porque el nuevo gobierno quería aumentar el control estatal sobre la economía.
# 6: Cuba se acercó a la Unión Soviética después de que sus relaciones con Estados Unidos se deterioraran.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El giro socialista y la alianza con la Unión Soviética",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En mayo de 1959, el gobierno revolucionario promulgó la Primera Ley de Reforma Agraria, expropiando los grandes latifundios azucareros y ganaderos. {G(k, 4)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"Cuando las refinerías de Esso, Texaco y Shell se negaron a procesar el crudo importado de la URSS, Cuba las intervino de inmediato. Washington respondió cancelando la cuota azucarera cubana. {G(k, 5)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Moscú, bajo el liderazgo de Nikita Jrushchov, acordó comprar toda la cosecha de azúcar de la isla y suministrar petróleo, armas y créditos blandos. {G(k, 6)} {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"En abril de 1961, en vísperas del desembarco en Playa Girón, Fidel Castro proclamó abiertamente el carácter socialista de la revolución. En 1965 se fundó el Partido Comunista de Cuba (PCC). {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"La Campaña de Alfabetización de 1961 erradicó el analfabetismo en un solo año y la salud pública se hizo universal y gratuita, pero el régimen clausuró los periódicos independientes e impuso una estricta disciplina ideológica en la sociedad."
        }
    ]
}

# 21.04: revolucioncubana-04
k = "revolucioncubana-04"
# Grammar (7):
# 0: El mundo entero estuvo a punto de vivir una guerra nuclear directa entre Estados Unidos y la Unión Soviética.
# 1: Ambas superpotencias estuvieron a punto de entrar en un conflicto armado directo.
# 2: Muchos historiadores consideran este el momento más peligroso de toda la Guerra Fría.
# 3: La crisis se resolvió finalmente mediante una negociación secreta.
# 4: La invasión de Bahía de Cochinos fracasó porque las fuerzas revolucionarias lograron derrotar a los invasores.
# 5: La instalación de misiles soviéticos provocó una crisis internacional que duró varios días.
# 6: Estados Unidos estableció un bloqueo naval mientras las dos potencias negociaban una salida a la crisis.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Bahía de Cochinos y la Crisis de los Misiles de 1962",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En abril de 1961, la CIA financió y entrenó a la Brigada 2506 integrada por 1.400 exiliados cubanos para invadir la isla por Bahía de Cochinos (Playa Girón). {G(k, 4)} en menos de setenta y dos horas, consolidando el prestigio militar de Fidel Castro y empujando a Cuba a un pacto militar defensivo secreto con Moscú."
        },
        {
            "type": "narration",
            "text": f"En octubre de 1962, aviones espía estadounidenses U-2 fotografiaron la construcción de bases para misiles balísticos nucleares soviéticos R-12 en territorio cubano, capaces de alcanzar Washington y Nueva York. {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"El presidente John F. Kennedy impuso una 'cuarentena' militar sobre el mar Caribe. {G(k, 6)} Durante trece días angustiosos, {G(k, 0)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Fuerzas estratégicas nucleares de ambos bandos alcanzaron el estado de alerta DEFCON 2, mientras buques soviéticos se aproximaban a la línea de interdicción naval estadounidense."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} entre Kennedy y Jrushchov: la URSS retiró los misiles de Cuba a cambio del compromiso estadounidense de no invadir la isla y el desmantelamiento secreto de los cohetes Jupiter en Turquía, desactivando el holocausto atómico."
        }
    ]
}

# 21.05: revolucioncubana-05
k = "revolucioncubana-05"
# Grammar (7):
# 0: La revolución tuvo influencia en otros países porque algunos grupos la consideraban un ejemplo de transformación política.
# 1: Cuba apoyó movimientos revolucionarios mientras otros gobiernos intentaban contener la insurgencia.
# 2: La solidaridad con Cuba fue importante para algunos movimientos, aunque otros países rechazaron su modelo político.
# 3: No por haber triunfado en un país relativamente pequeño deja de haber sido la Revolución cubana un fenómeno de alcance verdaderamente continental.
# 4: No por haber fracasado la mayoría de estos intentos guerrilleros deja de haber transformado profundamente el mapa político de la región.
# 5: Cuba demostró que un cambio revolucionario genuino era, después de todo, posible.
# 6: Prácticamente ningún gobierno latinoamericano pudo ignorar la sombra de la revolución que había triunfado en la isla en 1959.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La onda expansiva en América Latina y la teoría del foco guerrillero",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El triunfo rebelde en Cuba conmocionó los cimientos políticos de todo el continente americano. {G(k, 3)} {G(k, 5)} frente al poderío hegemónico de los Estados Unidos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} En su ensayo 'La guerra de guerrillas', el Che Guevara teorizó el foquismo: un pequeño grupo armado de vanguardia en el campo podía encender las condiciones para una insurrección continental. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Miles de jóvenes universitarios y sindicalistas formaron organizaciones guerrilleras como las FARC y el ELN en Colombia, el MIR en Chile, los Tupamaros en Uruguay y los Montoneros en Argentina. {G(k, 4)} El asesinato del Che Guevara en La Higuera (Bolivia) en octubre de 1967 consagró su figura como mito universal."
        },
        {
            "type": "narration",
            "text": f"En respuesta diplomática, en 1962 la OEA expulsó a Cuba del sistema interamericano por presión de Washington, rompiendo todos los gobiernos sus lazos con La Habana, con la solitaria y digna excepción de México. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} El desafío cubano obligó a Estados Unidos y a las élites locales a reorganizar completamente sus doctrinas de seguridad nacional y contrainsurgencia."
        }
    ]
}

# =============================================================================
# UNIT 22: guerrafria
# =============================================================================

# 22.01: guerrafria-01
k = "guerrafria-01"
# Grammar (8):
# 0: La Guerra Fría influyó en la política latinoamericana porque dividió a los países en dos bloques.
# 1: Estados Unidos aumentó su presencia mientras la Unión Soviética buscaba aliados en la región.
# 2: Se intensificaron las tensiones ideológicas que afectaron a las instituciones democráticas.
# 3: América Latina se convirtió, a pesar de su distancia geográfica de Europa, en uno de los escenarios más disputados de la Guerra Fría.
# 4: Esta confrontación no fue simplemente un conflicto diplomático abstracto entre dos superpotencias lejanas.
# 5: La rivalidad entre Washington y Moscú redefinió por completo las prioridades de la política interna en prácticamente todos los países de la región.
# 6: Cualquier demanda de reforma social pasó a ser interpretada inmediatamente a través del prisma de la seguridad hemisférica.
# 7: La región se convirtió, casi inevitablemente, en uno de los escenarios más activos de la Guerra Fría.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "América Latina en el tablero de la Guerra Fría",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Tras la Segunda Guerra Mundial, el planeta quedó dividido por una confrontación global entre el capitalismo liderado por Estados Unidos y el socialismo encabezado por la Unión Soviética. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} En Centroamérica y el Cono Sur, las luchas cotidianas por la tierra, los salarios obreros y la educación pública quedaron atrapadas en la lógica bipolar. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 2)} En 1947 se firmó en Río de Janeiro el Tratado Interamericano de Asistencia Recíproca (TIAR), estableciendo un pacto de defensa militar colectiva bajo tutela del Pentágono."
        },
        {
            "type": "narration",
            "text": f"En 1948 se fundó en Bogotá la Organización de los Estados Americanos (OEA), concebida por Washington como un cordón sanitario diplomático contra la penetración comunista."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La intolerancia ideológica se normalizó en las cancillerías, preparando el terreno para la persecución sistemática de las fuerzas de izquierda y el socavamiento de las democracias constitucionales."
        }
    ]
}

# 22.02: guerrafria-02
k = "guerrafria-02"
# Grammar (8):
# 0: Las fuerzas armadas adoptaron la Doctrina de la Seguridad Nacional para combatir lo que consideraban una amenaza interna.
# 1: Los militares definieron al enemigo interno como cualquier grupo sospechoso de simpatizar con el comunismo.
# 2: Se justificó la intervención militar porque se consideraba necesario mantener el orden social.
# 3: La Doctrina de la Seguridad Nacional redefinió por completo la misión histórica de las fuerzas armadas latinoamericanas.
# 4: El enemigo principal ya no era un ejército extranjero que amenazaba las fronteras del país.
# 5: El nuevo enemigo era un adversario ideológico invisible que operaba dentro de la propia sociedad nacional.
# 6: Esta doctrina proporcionó la justificación teórica para convertir a los ejércitos en fuerzas de control político interno.
# 7: Washington estaba dispuesto a tolerar prácticamente cualquier cosa, con tal de que un gobierno se mantuviera firmemente alineado contra el comunismo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Doctrina de la Seguridad Nacional y el enemigo interno",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante la década de 1960, el Estado Mayor Conjunto de Estados Unidos y las academias militares del continente formularon un nuevo marco estratégico. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} Guerrilleros, dirigentes sindicales combativos, sacerdotes de la teología de la liberación, maestros y estudiantes universitarios pasaron a ser catalogados como piezas de una agresión subversiva foránea."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} En escuelas superiores de guerra como la ESG en Brasil y la Escuela de Guerra en Buenos Aires, los oficiales fueron instruidos en técnicas de guerra psicológica, inteligencia y contrainsurgencia urbana."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 6)} La defensa de las instituciones republicanas quedó subordinada a la 'defensa de la civilización occidental y cristiana'. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"Esta doctrina desnaturalizó el rol constitucional de las fuerzas armadas, transformándolas en celosos guardianes de un orden social excluyente y en ejecutores de la más feroz represión estatal del siglo veinte."
        }
    ]
}

# 22.03: guerrafria-03
k = "guerrafria-03"
# Grammar (8):
# 0: La Escuela de las Américas formó a oficiales latinoamericanos en técnicas de contrainsurgencia.
# 1: Miles de militares fueron entrenados en tácticas de combate y guerra psicológica.
# 2: Los cursos reforzaron la idea de que la seguridad interna era la prioridad absoluta.
# 3: Miles de oficiales que más tarde encabezarían golpes de Estado recibieron su formación en la Escuela de las Américas.
# 4: Los manuales de instrucción incluían técnicas avanzadas de interrogatorio y operaciones clandestinas.
# 5: Esta institución se convirtió en uno de los símbolos más controvertidos de la influencia estadounidense en la región.
# 6: Los vínculos personales forjados durante estos cursos facilitaron la coordinación represiva entre distintos ejércitos de la región.
# 7: Los grupos políticos actuaban defendiendo posiciones cada vez más opuestas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Escuela de las Américas y la contrainsurgencia",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En 1946, el Ejército de Estados Unidos fundó en la Zona del Canal de Panamá el 'Centro de Entrenamiento Latinoamericano', rebautizado en 1963 como la Escuela de las Américas (School of the Americas). {G(k, 0)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Por sus aulas pasaron más de 60.000 oficiales latinoamericanos, entre ellos futuros dictadores como Manuel Antonio Noriega de Panamá, Leopoldo Galtieri y Roberto Viola de Argentina, Hugo Banzer de Bolivia y Manuel Contreras de Chile."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 2)} Las cátedras impartían métodos de guerra irregular, infiltración en sindicatos y censura de prensa aprendidos durante los conflictos de Indochina y Argelia. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Oficiales de diferentes naciones compartieron cuarteles y doctrinas comunes, sentando las redes de camaradería que harían posible la coordinación transfronteriza del terrorismo de Estado en los años setenta."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} La Escuela de las Américas simbolizó la militarización absoluta de las relaciones interamericanas a expensas de los derechos humanos y la soberanía popular."
        }
    ]
}

# 22.04: guerrafria-04
k = "guerrafria-04"
# Grammar (8):
# 0: Los gobiernos de izquierda promovieron reformas que fueron vistas con desconfianza por Estados Unidos.
# 1: La polarización política aumentó mientras las organizaciones guerrilleras ganaban presencia.
# 2: Las elecciones fueron cuestionadas cuando los resultados favorecían a sectores reformistas.
# 3: La polarización política alcanzó niveles extremos que destruyeron el espacio para el compromiso democrático.
# 4: Las reformas moderadas comenzaron a ser interpretadas por los sectores conservadores como el primer paso hacia el comunismo.
# 5: Los movimientos revolucionarios veían en cualquier vía electoral una trampa burguesa que solo servía para postergar la lucha armada.
# 6: Esta dinámica de confrontación anuló la posibilidad de consensos y aceleró el derrumbe institucional en varios países.
# 7: Este patrón de intervención, justificada so pretexto de principios elevados, estaba motivado con frecuencia por cálculos mucho más pragmáticos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Polarización ideológica, ruptura democrática y radicalización",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Hacia fines de los años sesenta y principios de los setenta, la convivencia política civil en América Latina se desintegró en una espiral de radicalización irreconciliable. {G(k, 3)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Terratenientes, cámaras patronales y grandes medios de prensa tildaron de 'marxista' cualquier proyecto de reforma agraria o nacionalización de recursos básicos. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"Por el otro extremo, {G(k, 5)} Grupos guerrilleros urbanos ejecutaron secuestros extorsivos y asaltos a cuarteles para acelerar las condiciones de una guerra civil abierta. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} En Chile, Uruguay y Argentina, el centro político moderado fue aplastado por la violencia callejera, las huelgas salvajes y los atentados paramilitares de la ultraderecha armada."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La pérdida de fe compartida en las reglas del juego democrático dejó el escenario despejado para que los mandos castrenses asumieran el control absoluto del poder público."
        }
    ]
}

# 22.05: guerrafria-05
k = "guerrafria-05"
# Grammar (8):
# 0: La Guerra Fría dejó un legado de divisiones políticas que persistieron durante décadas.
# 1: La memoria de este periodo continúa siendo objeto de debate en la sociedad contemporánea.
# 2: Las instituciones democráticas tardaron años en recuperarse tras el fin de los conflictos ideológicos.
# 3: La Guerra Fría en América Latina no fue una guerra incruenta entre superpotencias distantes.
# 4: Las víctimas mortales de este conflicto se contaron por cientos de miles, en su inmensa mayoría ciudadanos latinoamericanos.
# 5: Las consecuencias económicas y sociales de la militarización condicionaron el desarrollo de la región durante décadas.
# 6: Comprender este periodo resulta indispensable para explicar los debates políticos contemporáneos de la región.
# 7: Varios conflictos regionales quedaron vinculados a la rivalidad entre las superpotencias.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El balance humano e institucional de la Guerra Fría",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A diferencia de Europa, donde la Guerra Fría se mantuvo como una 'paz armada' contenida por el equilibrio nuclear, en América Latina el conflicto ardió con ferocidad letal. {G(k, 3)} {G(k, 4)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"Decenas de miles de personas fueron desaparecidas, torturadas y asesinadas en centros clandestinos de detención en el Cono Sur, mientras en Centroamérica guerras civiles arrasaron aldeas indígenas completas en Guatemala y El Salvador."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} La deuda externa se multiplicó para financiar armas y fuga de capitales, destruyendo las conquistas salariales del periodo industrializador. {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Sistemas judiciales desmantelados y policías militarizadas requirieron profundas reformas constitucionales durante las transiciones democráticas de fin de siglo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 6)} Las disputas sobre la verdad, la justicia frente a los crímenes de lesa humanidad y el papel de las superpotencias continúan marcando el corazón de la política latinoamericana."
        }
    ]
}

# =============================================================================
# UNIT 23: eeuu
# =============================================================================

# 23.01: eeuu-01
k = "eeuu-01"
# Grammar (8):
# 0: La Doctrina Monroe estableció que el continente americano no debía ser objeto de colonización europea.
# 1: El Corolario Roosevelt justificó la intervención militar estadounidense en la región.
# 2: Estados Unidos intervino en varios países caribeños para proteger sus intereses económicos y estratégicos.
# 3: La Doctrina Monroe proclamaba en 1823 un principio que parecía, en apariencia, puramente defensivo.
# 4: El Corolario Roosevelt de 1904 transformó esta postura defensiva en una justificación explícita para la intervención armada.
# 5: La política del "gran garrote" convirtió al Caribe en un verdadero mar interior dominado por Washington.
# 6: Esta política generó un profundo resentimiento antiimperialista que perduraría a lo largo de todo el siglo veinte.
# 7: Esta relación profundamente desigual pero mutuamente necesaria definiría buena parte de la historia latinoamericana del siglo veinte.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Doctrina Monroe y la política del Gran Garrote",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} Bajo el lema 'América para los americanos', el presidente James Monroe pretendía frenar los intentos de la Santa Alianza europea de reconquistar las jóvenes repúblicas independizadas."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, al despuntar el siglo veinte, el naciente imperialismo estadounidense redefinió unilateralmente esa doctrina. {G(k, 4)} {G(k, 1)} Theodore Roosevelt afirmó el derecho de EE.UU. a ejercer un 'poder de policía internacional' ante cualquier 'desorden crónico' en el hemisferio."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} Marines estadounidenses desembarcaron y ocuparon militarmente Cuba tras la Enmienda Platt, Puerto Rico en 1898, Nicaragua (1912-1933), Haití (1915-1934) y la República Dominicana (1916-1924), administrando directamente sus aduanas."
        },
        {
            "type": "narration",
            "text": f"En 1903, Roosevelt impulsó la separación forzada de Panamá de Colombia para asegurarse el control soberano sobre la construcción del Canal de Panamá. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Intelectuales como José Martí, José Enrique Rodó y Manuel Ugarte alertaron sobre el coloso del norte, inspirando las primeras grandes resistencias nacionalistas."
        }
    ]
}

# 23.02: eeuu-02
k = "eeuu-02"
# Grammar (8):
# 0: El presidente Franklin D. Roosevelt proclamó la Política del Buen Vecino para mejorar las relaciones con la región.
# 1: Estados Unidos renunció temporalmente a las intervenciones militares directas en América Latina.
# 2: La diplomacia se centró en la cooperación económica y la defensa hemisférica durante la Segunda Guerra Mundial.
# 3: La Política del Buen Vecino representó un giro diplomático significativo respecto a las décadas anteriores.
# 4: Washington retiró a los marines de Centroamérica y el Caribe, prometiendo respetar la soberanía formal de cada país.
# 5: Este cambio de estrategia facilitó la cooperación militar y económica durante la Segunda Guerra Mundial.
# 6: La no intervención formal no impidió que Estados Unidos mantuviera una enorme influencia a través de dictadores aliados.
# 7: Este periodo demostró que la voluntad de intervenir directamente en la región no dependía de la existencia previa de una amenaza comunista.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Política del Buen Vecino y la diplomacia de entreguerras",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En su discurso inaugural de 1933, {G(k, 0)} {G(k, 3)} Agobiado por la Gran Depresión y consciente del repudio unánime hacia el imperialismo armado, Washington adoptó un tono de respeto recíproco."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 4)} Se derogó la humillante Enmienda Platt que limitaba la soberanía cubana y las tropas abandonaron Haití y Nicaragua. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"Esta moderación diplomática se puso a prueba en 1938, cuando el presidente mexicano Lázaro Cárdenas nacionalizó el petróleo. En lugar de enviar buques de guerra, la administración Roosevelt negoció una compensación financiera pacífica."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} Prácticamente todas las repúblicas latinoamericanas se alinearon con los Aliados contra el Eje nazi-fascista, suministrando caucho, petróleo, azúcar y minerales esenciales para la victoria bélica."
        },
        {
            "type": "narration",
            "text": f"No obstante, {G(k, 6)} Dictadores leales como Anastasio Somoza en Nicaragua, Rafael Leónidas Trujillo en República Dominicana y Fulgencio Batista en Cuba consolidaron sus dinastías gracias a la tolerancia de Washington."
        }
    ]
}

# 23.03: eeuu-03
k = "eeuu-03"
# Grammar (8):
# 0: La CIA organizó una operación encubierta para derrocar al gobierno de Jacobo Árbenz en 1954.
# 1: La reforma agraria guatemalteca afectó a las tierras de la United Fruit Company.
# 2: El golpe militar interrumpió un proceso de reformas democráticas que buscaba modernizar el país.
# 3: La intervención encubierta de la CIA en Guatemala en 1954 marcó un precedente decisivo para toda la región.
# 4: La acusación de simpatías comunistas sirvió para justificar el derrocamiento de un gobierno elegido democráticamente.
# 5: La defensa de los intereses económicos de una multinacional estadounidense pesó más que el respeto a la democracia.
# 6: El golpe sumió a Guatemala en cuatro décadas de conflicto armado interno y regímenes militares sangrientos.
# 7: Algunas economías crecían dependiendo de la exportación de materias primas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Guatemala 1954: la CIA, la United Fruit y el fin de la Primavera Democrática",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En 1951, el coronel Jacobo Árbenz Guzmán asumió la presidencia de Guatemala con el mandato de modernizar la economía feudal del país. {G(k, 7)} En 1952 promulgó el Decreto 900 de Reforma Agraria, expropiando tierras ociosas pagando indemnizaciones basadas en el valor fiscal declarado."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} La gigantesca corporación bostoniana, que poseía el monopolio bananero, los ferrocarriles y el puerto de Puerto Barrios, movilizó sus conexiones en Washington a través de los hermanos John Foster Dulles (secretario de Estado) y Allen Dulles (director de la CIA)."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} Bajo el nombre clave 'Operación PBSUCCESS', la CIA utilizó guerra psicológica por radio, bombardeos clandestinos sobre la capital y un ejército mercenario comandado por el coronel Carlos Castillo Armas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} {G(k, 2)} El gobierno constitucional fue derrocado en junio de 1954 y las tierras devueltas a la United Fruit Company."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La tragedia guatemalteca convenció a revolucionarios como el joven Ernesto Guevara de que la transformación social pacífica era inviable frente a la intervención imperialista."
        }
    ]
}

# 23.04: eeuu-04
k = "eeuu-04"
# Grammar (8):
# 0: La Alianza para el Progreso fue lanzada por John F. Kennedy para frenar la influencia de la Revolución cubana.
# 1: Se prometieron miles de millones de dólares para financiar reformas económicas y sociales.
# 2: El programa promovió reformas agrarias y educativas para modernizar las sociedades latinoamericanas.
# 3: La Alianza para el Progreso de 1961 representó el intento más ambicioso de Washington por combinar ayuda económica y reforma social.
# 4: La premisa central era que el desarrollo económico y las reformas moderadas evitarían nuevas revoluciones de tipo cubano.
# 5: Los resultados reales del programa quedaron muy por debajo de las expectativas iniciales.
# 6: Las oligarquías locales bloquearon sistemáticamente las reformas tributarias y agrarias que el plan exigía.
# 7: A raíz de la revolución cubana, Estados Unidos impulsó nuevas políticas regionales.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La Alianza para el Progreso: desarrollo versus contrainsurgencia",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En marzo de 1961, alarmado por el eco continental de la Revolución cubana, el presidente John F. Kennedy convocó en la Casa Blanca a los diplomáticos del hemisferio. {G(k, 7)} {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"En la Conferencia de Punta del Este de agosto de 1961, {G(k, 1)} a lo largo de una década. {G(k, 2)} {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"Kennedy advirtió en una célebre frase: 'Aquellos que hacen imposible una revolución pacífica harán inevitable una revolución violenta'. Sin embargo, {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Los terratenientes y banqueros locales prefirieron financiar golpes militares antes que permitir la redistribución de la tierra y el cobro de impuestos a las grandes fortunas."
        },
        {
            "type": "narration",
            "text": f"Tras el asesinato de Kennedy en 1963, los fondos de ayuda económica fueron desviados hacia la compra de armamento y el fortalecimiento de los aparatos policiales de contrainsurgencia, sepultando las promesas reformistas."
        }
    ]
}

# 23.05: eeuu-05
k = "eeuu-05"
# Grammar (8):
# 0: Las relaciones interamericanas estuvieron marcadas por una tensión constante entre cooperación y conflicto.
# 1: La soberanía nacional fue defendida por diversos movimientos frente a las intervenciones extranjeras.
# 2: El debate sobre el papel de Estados Unidos sigue dividiendo a la opinión pública en el continente.
# 3: El balance de las relaciones interamericanas en el siglo veinte revela una asimetría de poder estructural insoslayable.
# 4: La primacía de los intereses geopolíticos y comerciales estadounidenses chocó reiteradamente con las aspiraciones de soberanía de los pueblos latinoamericanos.
# 5: Esta relación generó una profunda tradición de pensamiento antiimperialista y búsqueda de autonomía regional.
# 6: La influencia estadounidense modeló de manera decisiva la trayectoria política y económica del continente durante todo el siglo.
# 7: A lo largo del siglo, la relación combinó cooperación, presión y resistencia.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La relación asimétrica y el debate sobre la soberanía hemisférica",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A lo largo de todo el siglo veinte, los vínculos diplomáticos y económicos entre Washington y las capitales al sur del río Bravo constituyeron el eje gravitacional de la geopolítica hemisférica. {G(k, 3)} {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Desde las intervenciones navales del Big Stick hasta las operaciones encubiertas de la Guerra Fría y la imposición de recetas de ajuste financiero, la soberanía de los países latinoamericanos fue vulnerada en múltiples ocasiones."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 5)} Pensadores, movimientos estudiantiles y sindicatos forjaron una rica doctrina de autodeterminación, no intervención y solidaridad del Tercer Mundo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} En el ámbito cultural, el consumo de cine, música y tecnología estadounidense convivió con una férrea resistencia defensiva de las identidades nacionales autóctonas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Superar la subordinación neocolonial sin caer en el aislamiento comercial continúa siendo uno de los mayores desafíos diplomáticos para América Latina en el siglo veintiuno."
        }
    ]
}

# =============================================================================
# UNIT 24: gobiernosmilitares
# =============================================================================

# 24.01: gobiernosmilitares-01
k = "gobiernosmilitares-01"
# Grammar (8):
# 0: Los golpes de Estado interrumpieron procesos democráticos en varios países durante las décadas de 1960 y 1970.
# 1: Las fuerzas armadas justificaron su intervención como una medida para frenar el comunismo y restaurar el orden.
# 2: Las instituciones democráticas fueron clausuradas mientras se prohibían los partidos políticos.
# 3: La ola de golpes militares que sacudió a América Latina entre 1964 y 1976 no fue una simple repetición de los antiguos caudillismos del siglo diecinueve.
# 4: Las fuerzas armadas intervinieron como institución corporativa completa, con un proyecto refundacional para toda la sociedad.
# 5: La intervención militar se justificó mediante el discurso del rescate nacional ante un supuesto colapso inminente.
# 6: Esta nueva forma de autoritarismo fue conceptualizada por los sociólogos como el "Estado burocrático-autoritario".
# 7: El poder económico no quedaba en manos de los militares mismos, más bien se entregaba a equipos de tecnócratas civiles.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Estado burocrático-autoritario y la nueva ola militar",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} A diferencia de las asonadas caudillistas decimonónicas, los ejércitos modernos actuaron con un alto grado de disciplina técnica y cohesión doctrinal."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 6)} El politólogo Guillermo O'Donnell acuñó este concepto para describir regímenes encabezados por las cúpulas militares en alianza con tecnócratas civiles y el gran capital transnacional. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 5)} Los comandantes proclamaron que intervenían para extirpar de raíz el 'cáncer marxista', disciplinar al movimiento obrero y reorganizar la economía bajo criterios de libre mercado irrestricto."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Se disolvieron los congresos parlamentarios, se intervinieron las universidades, se suspendieron las garantías constitucionales y se decretó la disolución forzosa de las centrales obreras."
        },
        {
            "type": "narration",
            "text": f"Esta matriz autoritaria se desplegó sucesivamente en Brasil (1964), Argentina (1966 y 1976), Bolivia (1971), Chile (1973) y Uruguay (1973), instaurando los regímenes más represivos y prolongados de la historia sudamericana."
        }
    ]
}

# 24.02: gobiernosmilitares-02
k = "gobiernosmilitares-02"
# Grammar (8):
# 0: El golpe militar de 1964 derrocó al presidente João Goulart en Brasil.
# 1: El régimen combinó represión política con un ambicioso programa de desarrollo económico.
# 2: El "milagro económico" brasileño produjo altas tasas de crecimiento, aunque aumentó la desigualdad social.
# 3: El golpe de 1964 en Brasil inauguró formalmente el ciclo de dictaduras de seguridad nacional en el Cono Sur.
# 4: Los militares brasileños gobernaron mediante una fachada constitucional restrictiva combinada con decretos dictatoriales conocidos como Actos Institucionales.
# 5: El Acta Institucional Número 5 (AI-5) de 1968 clausuró los últimos espacios de libertad de prensa y derechos civiles.
# 6: El modelo económico priorizó las grandes obras públicas faraónicas y la atracción masiva de capital transnacional.
# 7: El proceso de apertura avanzó de tal manera que, tras la ley de amnistía de 1979, el país regresó a un gobierno civil en 1985.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La dictadura brasileña (1964-1985) y el 'milagro económico'",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El 31 de marzo de 1964, una sublevación militar con apoyo del embajador estadounidense Lincoln Gordon derrocó al presidente reformista João Goulart. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Se creó un sistema bipartidista tutelado entre el oficialista ARENA y el opositor consentido MDB. Sin embargo, en diciembre de 1968 el general Costa e Silva endureció al extremo el régimen. {G(k, 5)} Se cerró el Congreso, se impuso la censura previa a periódicos y teatros, y se generalizó la tortura de presos políticos en el DOI-CODI."
        },
        {
            "type": "narration",
            "text": f"Entre 1968 y 1973, bajo la presidencia del general Emílio Garrastazu Médici, {G(k, 1)} El PIB creció a más del diez por ciento anual durante el llamado 'milagro brasileño'. {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"Se construyeron la represa hidroeléctrica de Itaipú, el puente Río-Niterói y la carretera Transamazónica. {G(k, 2)} El ministro de Economía Antônio Delfim Netto declaró que 'había que hacer crecer el pastel antes de repartirlo', pero los salarios reales se derrumbaron."
        },
        {
            "type": "narration",
            "text": f"La crisis del petróleo de 1973 y una deuda externa asfixiante agotaron el milagro. {G(k, 7)} con la asunción de José Sarney tras masivas movilizaciones de 'Diretas Já'."
        }
    ]
}

# 24.03: gobiernosmilitares-03
k = "gobiernosmilitares-03"
# Grammar (8):
# 0: El golpe de Estado del 11 de septiembre de 1973 puso fin al gobierno de Salvador Allende.
# 1: La dictadura encabezada por Augusto Pinochet persiguió a opositores y disolvió las instituciones democráticas.
# 2: Las políticas neoliberales transformaron la economía chilena bajo la influencia de los Chicago Boys.
# 3: El 11 de septiembre de 1973, los aviones de la Fuerza Aérea bombardearon el Palacio de La Moneda en Santiago de Chile.
# 4: La muerte de Salvador Allende en la sede de gobierno simbolizó la destrucción violenta de la vía democrática al socialismo.
# 5: La dictadura de Pinochet implementó un terrorismo de Estado sistemático a través de la policía secreta conocida como DINA.
# 6: Chile se convirtió en el laboratorio pionero del neoliberalismo radical en todo el mundo.
# 7: Tras el fin de la dictadura, los gobiernos democráticos chilenos posteriores mantendrían en gran medida este mismo modelo económico.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El 11 de septiembre en Chile y la refundación pinochetista",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} El presidente Salvador Allende, resistiendo con su fusil AK-47 en su despacho en llamas, transmitió por Radio Magallanes su conmovedor mensaje final al pueblo chileno: 'Mucho más temprano que tarde, de nuevo se abrirán las grandes alamedas por donde pase el hombre libre'."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} La Junta Militar presidida por el general Augusto Pinochet clausuró el Congreso Nacional, prohibió los partidos de izquierda y declaró el estado de sitio permanente. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"El Estadio Nacional y el Estadio Chile se transformaron en campos de concentración masivos donde fue torturado y asesinado el cantautor Víctor Jara. {G(k, 5)} Dirigida por el coronel Manuel Contreras, la DINA cometió secuestros, desapariciones y atentados terroristas internacionales en Buenos Aires, Roma y Washington D.C."
        },
        {
            "type": "narration",
            "text": f"En el plano económico, {G(k, 6)} Un grupo de economistas formados con Milton Friedman en la Universidad de Chicago —los célebres 'Chicago Boys'— aplicó una terapia de shock. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"Se privatizaron cientos de empresas estatales, se desmantelaron los aranceles, se privatizó el sistema de pensiones en AFPs privadas y se municipalizó la educación, consagrando este modelo en la autoritaria Constitución de 1980. {G(k, 7)}"
        }
    ]
}

# 24.04: gobiernosmilitares-04
k = "gobiernosmilitares-04"
# Grammar (8):
# 0: La junta militar argentina asumió el poder en marzo de 1976 mediante un golpe de Estado.
# 1: El régimen militar implementó una represión sistemática que dejó miles de personas desaparecidas.
# 2: Las Madres de Plaza de Mayo comenzaron a reclamar la aparición con vida de sus hijos detenidos.
# 3: La dictadura autodenominada "Proceso de Reorganización Nacional" llevó el terrorismo de Estado a una escala sin precedentes en Argentina.
# 4: Las fuerzas armadas utilizaron cientos de centros clandestinos de detención para torturar y desaparecer a sus víctimas.
# 5: El robo sistemático de bebés nacidos en cautiverio constituyó uno de los crímenes más aberrantes de este periodo.
# 6: El coraje moral de las Madres y Abuelas de Plaza de Mayo rompió el cerco del miedo y conmovió a la comunidad internacional.
# 7: La guerra fue breve; no obstante, sus consecuencias políticas resultarían decisivas para el futuro inmediato del país.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El terrorismo de Estado en Argentina y la resistencia de las Madres",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El 24 de marzo de 1976, {G(k, 0)} encabezada por el general Jorge Rafael Videla, el almirante Emilio Massera y el brigadier Orlando Agosti. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 4)} Lugares como la ESMA en Buenos Aires, El Campito en Campo de Mayo y La Perla en Córdoba se convirtieron en antesalas de la muerte, donde prisioneros eran arrojados vivos al Río de la Plata en los atroces 'vuelos de la muerte'."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Niños recién nacidos eran despojados de sus madres prisioneras y entregados en adopción clandestina con identidades falsificadas a familias militares y allegados al régimen."
        },
        {
            "type": "narration",
            "text": f"El 30 de abril de 1977, un puñado de valientes mujeres con pañuelos blancos en sus cabezas comenzó a marchar en círculos alrededor de la Pirámide de Mayo frente a la Casa Rosada. {G(k, 2)} {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"En 1982, en un intento desesperado por perpetuarse en el poder, el general Leopoldo Galtieri ocupó militarmente las islas Malvinas. {G(k, 7)} La humillante rendición militar aceleró el colapso definitivo del régimen y condujo a las históricas elecciones democráticas de 1983."
        }
    ]
}

# 24.05: gobiernosmilitares-05
k = "gobiernosmilitares-05"
# Grammar (8):
# 0: El Plan Cóndor fue una red de coordinación represiva entre varias dictaduras del Cono Sur.
# 1: Los servicios de seguridad intercambiaron información y colaboraron en la captura de opositores políticos.
# 2: Las víctimas de la coordinación represiva incluyeron a dirigentes políticos, sindicalistas y activistas.
# 3: La 'Operación Cóndor' convirtió al Cono Sur en una zona sin fronteras para el secuestro y asesinato de disidentes políticos.
# 4: Los 'Archivos del Terror' descubiertos en Paraguay en 1992 aportaron pruebas documentales irrefutables sobre esta coordinación criminal.
# 5: La memoria de las víctimas y la lucha por la justicia continúan siendo pilares fundamentales de la democracia en la región.
# 6: Los juicios por crímenes de lesa humanidad sentaron precedentes jurídicos trascendentales en el derecho internacional.
# 7: En definitiva, comparar estos tres países muestra tanto lo que compartían como lo profundamente distintos que fueron sus finales.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Plan Cóndor: coordinación represiva y la lucha por la memoria",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En noviembre de 1975, los jefes de inteligencia militar de Chile, Argentina, Uruguay, Paraguay y Bolivia se reunieron en Santiago convocados por el director de la DINA, Manuel Contreras. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} Comandos clandestinos cruzaban fronteras con total impunidad para secuestrar y ejecutar a refugiados. {G(k, 2)} Entre los atentados más notorios figuraron los asesinatos del general chileno Carlos Prats en Buenos Aires, del excanciller Orlando Letelier en Washington y del expresidente boliviano Juan José Torres."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} El hallazgo de toneladas de documentos oficiales en Asunción demostró la sistematicidad del plan y el respaldo logístico encubierto brindado por la CIA estadounidense."
        },
        {
            "type": "narration",
            "text": f"Con el retorno a la democracia, los países del Cono Sur crearon comisiones de verdad como la CONADEP en Argentina y la Comisión Rettig en Chile. {G(k, 6)} dictadores y torturadores fueron condenados a prisión perpetua en juicios históricos. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} El compromiso indeclinable de 'Nunca Más' ante el terrorismo de Estado se convirtió en la piedra basal moral e institucional de la convivencia democrática latinoamericana."
        }
    ]
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
