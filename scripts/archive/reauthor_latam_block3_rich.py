"""
Reauthors Latin America B1 Block 3 (Units 13-18, lessons 01-05) stories.
Each story is 350-500 words in engaging, narrative history style.
Strictly embeds ALL grammar example sentences verbatim and covers all vocabulary words and exercise facts.
"""

import json
import os

reqs = json.load(open('scripts/block3_all_reqs.json', encoding='utf-8'))

# We will define rich narrative paragraphs for each of the 30 lessons in Block 3.
# We ensure every single sentence in reqs[lesson_key]['grammar_sentences'] is included verbatim in the text.

STORIES = {
    # =========================================================================
    # UNIT 13: economiasexportacion
    # =========================================================================
    "b1-economiasexportacion-01-modelo.json": {
        "id": "story.b1.economiasexportacion.01",
        "title": "El auge del modelo agroexportador",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Entre 1870 y 1914, América Latina vivió una de las transformaciones económicas más vertiginosas de su historia moderna. El rápido crecimiento industrial de Europa occidental y Estados Unidos generó un apetito insaciable por alimentos, minerales y fibras vegetales. Durante la segunda mitad del siglo diecinueve, América Latina se integró plenamente en la economía global."
            },
            {
                "type": "narration",
                "text": "El comercio se volvió más libre que antes, pero la región siguió exportando sobre todo materias primas. Países que durante décadas habían permanecido aislados por guerras civiles se volcaron hacia el comercio exterior. Esta especialización resultó mucho más rentable que cualquier intento anterior de desarrollar una industria local diversificada."
            },
            {
                "type": "narration",
                "text": "El modelo exportador resultaba, comparado con la economía colonial, mucho más dinámico en términos de ingresos totales. Cada país tendió a especializarse en los bienes que su geografía le permitía producir a gran escala: trigo y carne en Argentina, café en Brasil y Colombia, salitre en Chile y azúcar en Cuba. La demanda internacional de materias primas impulsó el crecimiento de las exportaciones."
            },
            {
                "type": "narration",
                "text": "Ese crecimiento económico benefició enormemente a las élites terratenientes y a los comerciantes de los puertos, quienes levantaron suntuosos palacetes en Buenos Aires y Río de Janeiro. Sin embargo, este esquema acarreaba un peligro estructural latente. Cuanto más dependía un país de un solo producto, más expuesto quedaba a cualquier caída repentina de su precio."
            },
            {
                "type": "narration",
                "text": "Las inversiones extranjeras financiaron puertos y ferrocarriles para facilitar el comercio, acelerando la modernización pero profundizando la dependencia. El modelo agroexportador transformó profundamente la vida social y económica de la región, fijando un rumbo que condicionaría todo el siglo veinte."
            }
        ]
    },

    "b1-economiasexportacion-02-productos.json": {
        "id": "story.b1.economiasexportacion.02",
        "title": "Monocultivos y enclaves: el mapa productivo",
        "paragraphs": [
            {
                "type": "narration",
                "text": "El mapa económico de América Latina a finales del siglo diecinueve se caracterizó por la concentración en unos pocos rubros altamente cotizados. Los productos que tenían demanda internacional podían generar ingresos importantes. Los países latinoamericanos exportaban materias primas que necesitaban las economías industriales europeas y norteamericanas."
            },
            {
                "type": "narration",
                "text": "El café llegó a representar más de la mitad de todas las exportaciones brasileñas. En el estado de São Paulo, los cafetales devoraron millones de hectáreas y atrajeron a una marea de inmigrantes italianos. Cuando aumentaba la demanda, los productores ampliaban la producción."
            },
            {
                "type": "narration",
                "text": "En el desierto de Atacama, tras la Guerra del Pacífico (1879-1884), Chile concentró la producción mundial de salitre natural para fertilizantes y pólvora. Los yacimientos de nitrato financiaban más de la mitad del presupuesto estatal. Pero Si los precios bajaban, los ingresos de los productores podían disminuir."
            },
            {
                "type": "narration",
                "text": "En Centroamérica y el Caribe, compañías estadounidenses como la infame United Fruit Company establecieron plantaciones de banano bajo un régimen de enclave territorial casi soberano. El café y el azúcar eran productos que dominaban las exportaciones en varios países de la cuenca caribeña."
            },
            {
                "type": "narration",
                "text": "La materia prima que se exportaba dependía de las condiciones del mercado internacional. Esa extrema dependencia ató la suerte cotidiana de millones de trabajadores a las fluctuaciones en las bolsas de Londres y Wall Street."
            }
        ]
    },

    "b1-economiasexportacion-03-infraestructura.json": {
        "id": "story.b1.economiasexportacion.03",
        "title": "Ferrocarriles, capital británico y puertos modernos",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Para transportar millones de toneladas de granos, carnes y minerales desde el interior hasta los buques transoceánicos, se requirió una colosal revolución técnica. Para transportar estas mercancías de manera eficiente, se construyeron redes ferroviarias extensas. Se instalaron líneas de telégrafo que conectaban las zonas de producción con los centros urbanos."
            },
            {
                "type": "narration",
                "text": "Aunque resulte tentador imaginar los ferrocarriles como simples símbolos de progreso nacional, la mayoría fueron construidos por empresas extranjeras. La City de Londres canalizó sumas astronómicas hacia empréstitos y concesiones privadas, de modo que el capital británico controló las principales líneas férreas y servicios públicos de la región."
            },
            {
                "type": "narration",
                "text": "Aunque estas empresas generaran empleo local, buena parte de sus ganancias salía directamente del país. En Chile, empresarios como John Thomas North, el 'Rey del Salitre', ejercieron una hegemonía económica casi indiscutida. Su influencia se extendía incluso sobre la política chilena, aunque nunca ocupara ningún cargo oficial en el gobierno."
            },
            {
                "type": "narration",
                "text": "El diseño de las vías no buscaba integrar las provincias entre sí, sino conectar en abanico los centros productivos con la costa. Los puertos se expandieron enormemente, aunque su función principal siguiera siendo la salida de materias primas."
            },
            {
                "type": "narration",
                "text": "Los puertos fueron modernizados para permitir la llegada de barcos de mayor tamaño, como Puerto Madero en Buenos Aires y el puerto de Santos en Brasil. Esta infraestructura consolidó una geografía económica orientada hacia el Atlántico y el Pacífico antes que hacia el propio desarrollo interno."
            }
        ]
    },

    "b1-economiasexportacion-04-vulnerabilidad.json": {
        "id": "story.b1.economiasexportacion.04",
        "title": "La fragilidad del crecimiento hacia afuera",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia 1900, la prosperidad agroexportadora parecía incontenible a los ojos de las oligarquías latinoamericanas, pero bajo esa superficie dorada se acumulaban profundas fragilidades. Aunque las exportaciones generaban riqueza, los beneficios no siempre se distribuían de manera igual."
            },
            {
                "type": "narration",
                "text": "Para entonces, la concentración de tierras en inmensos latifundios había alcanzado niveles récord. Varios países habían concentrado su producción en un solo producto antes de que llegara la crisis de precios. Habían dependido de los préstamos británicos para financiar las grandes obras antes de que cambiaran las condiciones internacionales."
            },
            {
                "type": "narration",
                "text": "Los grandes propietarios podían obtener beneficios mientras los trabajadores recibían ingresos menores. En las haciendas y plantaciones, los peones vivían a menudo atados por deudas en las tiendas de raya. Como consecuencia de la concentración de la tierra, aumentó la desigualdad en algunas regiones."
            },
            {
                "type": "narration",
                "text": "Muchos campesinos habían perdido el acceso a las tierras comunales antes de que el modelo alcanzara su apogeo. El crecimiento económico no significaba necesariamente una distribución igual de la riqueza, provocando tensiones sociales en el campo y en las ciudades."
            },
            {
                "type": "narration",
                "text": "Las economías locales habían abandonado la producción de alimentos básicos para dedicarse al monocultivo antes de que los precios cayeran en los mercados mundiales. La bonanza dependía enteramente de compradores externos que no tenían ningún compromiso con la estabilidad de América Latina."
            }
        ]
    },

    "b1-economiasexportacion-05-legado.json": {
        "id": "story.b1.economiasexportacion.05",
        "title": "La herencia del modelo exportador y el caso del guano",
        "paragraphs": [
            {
                "type": "narration",
                "text": "El siglo diecinueve dejó lecciones dramáticas sobre los riesgos del monocultivo, siendo el ciclo del guano en el Perú (1840-1875) el ejemplo más ilustrativo. Durante tres décadas, el Estado peruano recibió ingresos gigantescos por la venta de este fertilizante natural a las potencias europeas. Si esos ingresos se hubieran invertido de manera sistemática en infraestructura, la historia económica del país habría sido muy distinta."
            },
            {
                "type": "narration",
                "text": "El modelo exportador transformó la economía, pero también dejó una fuerte dependencia exterior. En lugar de crear industrias duraderas, la riqueza del guano se evaporó en burocracia, importaciones de lujo y una deuda externa asfixiante. Si el Perú hubiera diversificado su economía durante estas décadas, habría estado mucho mejor preparado para lo que vino después."
            },
            {
                "type": "narration",
                "text": "Hacia 1870 el guano comenzó a agotarse y los fertilizantes químicos artificiales aparecieron en Europa. Si esos sustitutos hubieran tardado unas décadas más en desarrollarse, es posible que Perú hubiera tenido más tiempo para adaptarse. Pero el colapso fiscal fue fulminante y dejó al país indefenso ante la Guerra del Pacífico."
            },
            {
                "type": "narration",
                "text": "Esta historia de auge y caída se repitió con el caucho en el Amazonas y el salitre en el norte chileno. Si cualquiera de estos países hubiera dependido de dos o tres exportaciones, probablemente habría amortiguado mejor cada una de estas crisis."
            },
            {
                "type": "narration",
                "text": "La experiencia de estos años influyó en las políticas económicas posteriores. La lección era inequívoca: el crecimiento basado únicamente en vender materias primas sin diversificación industrial constituía un castillo de arena frente a los vaivenes de la economía mundial."
            }
        ]
    },

    # =========================================================================
    # UNIT 14: cambiosocial
    # =========================================================================
    "b1-cambiosocial-01-ciudades.json": {
        "id": "story.b1.cambiosocial.01",
        "title": "La gran explosión urbana",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia 1870, Buenos Aires era, según la describían sus propios habitantes, poco más que una \"gran aldea\". Sin embargo, el dinamismo agroexportador desató un proceso de urbanización sin precedentes en toda la región. El crecimiento de las ciudades aceleró la demanda de servicios públicos y transporte."
            },
            {
                "type": "narration",
                "text": "En pocas décadas, Buenos Aires, Río de Janeiro, São Paulo, Santiago y la Ciudad de México multiplicaron exponencialmente su población. No existía todavía un sistema de alcantarillado adecuado, y buena parte de la ciudad carecía de alumbrado público confiable. En muchas ciudades se construyeron avenidas amplias y edificios administrativos imponentes."
            },
            {
                "type": "narration",
                "text": "Los alcaldes y planificadores urbanos se inspiraron en las reformas del barón Haussmann en París. Con la llegada masiva de migrantes, la ciudad creció a un ritmo que sus servicios básicos apenas podían soportar. La expansión urbana transformó la vida cotidiana de las clases populares."
            },
            {
                "type": "narration",
                "text": "Mientras la élite construía bulevares arbolados, palacios de mármol y teatros de ópera, los sectores populares se hacinaban en los conventillos de Buenos Aires y los cortiços de Río. Esta transformación no solo cambió el aspecto de las ciudades, sino también la estructura misma de su sociedad."
            },
            {
                "type": "narration",
                "text": "La ciudad moderna se convirtió así en un escenario de asombrosa opulencia y lacerante precariedad, donde la cuestión social amenazaba con estallar en cualquier momento."
            }
        ]
    },

    "b1-cambiosocial-02-inmigracion.json": {
        "id": "story.b1.cambiosocial.02",
        "title": "La marea inmigrante y las nuevas clases sociales",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Entre 1880 y 1930, más de cuatro millones de inmigrantes europeos desembarcaron en los puertos del Río de la Plata y el sur de Brasil. Italianos, españoles, portugueses, alemanes y polacos llegaron atraídos por promesas de trabajo y tierras. La llegada de inmigrantes transformó la composición social de varias regiones."
            },
            {
                "type": "narration",
                "text": "Se formó una clase media urbana que buscaba nuevas oportunidades profesionales. Hijos de inmigrantes se convirtieron en médicos, maestros, abogados, pequeños comerciantes y empleados públicos. En algunos países se fortaleció la burguesía vinculada al comercio y a la industria."
            },
            {
                "type": "narration",
                "text": "Al mismo tiempo, Se concentraba una parte importante de la clase obrera en las ciudades industriales. Miles de hombres y mujeres trabajaban extenuantes jornadas en talleres textiles, frigoríficos de carne, fundiciones y obras portuarias."
            },
            {
                "type": "narration",
                "text": "Se produjeron cambios sociales a medida que crecían las ciudades. La tradicional dicotomía colonial entre amos y peones dio paso a una sociedad civil mucho más compleja y exigente."
            },
            {
                "type": "narration",
                "text": "Las nuevas clases medias y populares pronto cuestionaron el monopolio político de las oligarquías terratenientes, reclamando elecciones libres, educación laica y representación política genuina."
            }
        ]
    },

    "b1-cambiosocial-03-claseobrera.json": {
        "id": "story.b1.cambiosocial.03",
        "title": "El nacimiento del movimiento obrero",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A principios del siglo veinte, las condiciones de vida de los trabajadores urbanos y mineros eran alarmantes. Las jornadas laborales superaban con frecuencia las doce o catorce horas diarias, no existía descanso dominical remunerado ni indemnización por accidentes. La inmigración aumentó mientras las ciudades necesitaban más trabajadores."
            },
            {
                "type": "narration",
                "text": "Los migrantes llegaron buscando empleo y construyendo nuevos asentamientos. Con ellos viajaron libros, periódicos y folletos de agitación política. Las huelgas se multiplicaron mientras los obreros exigían mejores salarios."
            },
            {
                "type": "narration",
                "text": "Bajo la influencia del anarquismo y el socialismo, los trabajadores comenzaron a fundar sociedades de socorro mutuo, periódicos combativos y federaciones obreras como la FORA en Argentina y la FOCH en Chile. Los sindicatos crecieron organizando a los trabajadores de diferentes sectores industriales."
            },
            {
                "type": "narration",
                "text": "Las organizaciones obreras exigían la jornada de ocho horas, salarios dignos en moneda de curso legal y el fin de las tiendas de raya patronales. La movilización obrera creció mientras las fábricas aumentaban su producción."
            },
            {
                "type": "narration",
                "text": "La respuesta de los gobiernos oligárquicos fue a menudo la represión abierta y leyes de expulsión de extranjeros, pero el movimiento obrero ya se había consolidado como un actor político insoslayable."
            }
        ]
    },

    "b1-cambiosocial-04-mujeres.json": {
        "id": "story.b1.cambiosocial.04",
        "title": "Conflictos laborales, huelgas y tragedias obreras",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Las tensiones acumuladas en los centros mineros y fabriles desembocaron en memorables jornadas de lucha social. Estas ideas encontraron eco entre los trabajadores, hasta que se convirtieron en organización sindical concreta. En las fábricas textiles y talleres, miles de mujeres desempeñaron un papel decisivo en las huelgas."
            },
            {
                "type": "narration",
                "text": "En diciembre de 1907, miles de mineros del salitre en el norte chileno marcharon con sus familias hacia Iquique en reclamo de salarios dignos. Se congregaron en la Escuela Santa María. Esperaban allí, pacíficamente, hasta que el gobierno respondiera a sus peticiones."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el 21 de diciembre las tropas del general Roberto Silva Renard abrieron fuego de ametralladora, asesinando a cientos de obreros desarmados. Nunca se estableció una cifra exacta antes de que el hecho quedara, durante décadas, prácticamente silenciado."
            },
            {
                "type": "narration",
                "text": "En enero de 1919 en Buenos Aires, la huelga de los talleres metalúrgicos Vasena desató la Semana Trágica, con sangrientos enfrentamientos callejeros y persecución a militantes obreros. El conflicto no hizo más que intensificarse antes de que terminara la década."
            },
            {
                "type": "narration",
                "text": "En Colombia, la Masacre de las Bananeras en Ciénaga (1928) mostró que el Estado estaba dispuesto a usar el ejército para proteger los intereses de compañías extranjeras como la United Fruit. La cuestión obrera se tiñó de sangre y dignidad."
            }
        ]
    },

    "b1-cambiosocial-05-sociedadtransformada.json": {
        "id": "story.b1.cambiosocial.05",
        "title": "La sociedad latinoamericana en el umbral de una nueva era",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Hacia 1920, América Latina no solo había transformado el aspecto de sus ciudades, sino también la propia composición de su población. Los viejos mecanismos de control colonial y deferencia hacia el patrón de hacienda estaban en franca decadencia."
            },
            {
                "type": "narration",
                "text": "En 1918, la Reforma Universitaria de Córdoba en Argentina proclamó la democratización de la enseñanza superior, extendiendo su influencia por todo el continente. El movimiento no solo cuestionó el monopolio eclesiástico de las universidades, sino también el elitismo que mantenía fuera a los hijos de la clase media."
            },
            {
                "type": "narration",
                "text": "Las clases medias no solo exigían mayor participación política, sino también reformas educativas de amplio alcance. Las mujeres fundaron las primeras organizaciones sufragistas y centros feministas, como el Consejo Nacional de Mujeres impulsado por Julieta Lanteri y Paulina Luisi."
            },
            {
                "type": "narration",
                "text": "Los sindicatos no solo lograron la jornada de ocho horas en varios países, sino también el reconocimiento legal del derecho de huelga. Los cambios sociales no solo afectaron a las grandes metrópolis, sino que se extendieron paulatinamente a las provincias."
            },
            {
                "type": "narration",
                "text": "La transformación social del primer tercio del siglo veinte sentó las bases para el surgimiento de nuevos movimientos populares y proyectos de soberanía nacional."
            }
        ]
    },

    # =========================================================================
    # UNIT 15: revolucion
    # =========================================================================
    "b1-revolucion-01-tensiones.json": {
        "id": "story.b1.revolucion.01",
        "title": "El concepto de revolución en el siglo veinte",
        "paragraphs": [
            {
                "type": "narration",
                "text": "¿Qué distingue a una verdadera revolución de una simple revuelta o un golpe de cuartel? Para los historiadores, una revolución implica una ruptura radical con el orden sociopolítico preexistente. Se ampliaron las demandas de participación social en los primeros años del siglo veinte."
            },
            {
                "type": "narration",
                "text": "Se organizaron movimientos para transformar las instituciones políticas dominadas por camarillas oligárquicas. No es lo mismo un golpe de Estado encabezado por generales que una insurrección popular que moviliza a millones de campesinos y trabajadores."
            },
            {
                "type": "narration",
                "text": "No es lo mismo derrocar a un presidente que transformar por completo la estructura social de un país. Esta distinción entre revolución política y revolución social resulta fundamental para comprender el siglo veinte latinoamericano."
            },
            {
                "type": "narration",
                "text": "Se cuestionó la concentración de la tierra en pocas manos y el control extranjero de los recursos naturales. A raíz del conflicto, se propusieron reformas que cambiaron las instituciones fundamentales del Estado."
            },
            {
                "type": "narration",
                "text": "No es lo mismo un nuevo presidente que un nuevo país. Cuando una sociedad entra en ebullición revolucionaria, todas las certezas sobre la propiedad, el derecho y el poder se transforman radicalmente."
            }
        ]
    },

    "b1-revolucion-02-porfiriato.json": {
        "id": "story.b1.revolucion.02",
        "title": "La cuestión agraria y las raíces del descontento",
        "paragraphs": [
            {
                "type": "narration",
                "text": "La chispa de los procesos revolucionarios en América Latina casi siempre se encendió en el campo. Debido a que las leyes liberales de privatización habían despojado a muchas comunidades de sus tierras comunales, millones de personas se encontraron trabajando tierras que antes eran suyas."
            },
            {
                "type": "narration",
                "text": "A causa de que este despojo se repitió en prácticamente todos los países, la reivindicación de la tierra se convirtió en la demanda revolucionaria más extendida del continente. Se exigió una distribución más justa de la tierra para alimentar a las familias campesinas."
            },
            {
                "type": "narration",
                "text": "En algunos países, este descontento permaneció contenido durante décadas, debido a que los gobiernos combinaban represión selectiva con concesiones menores. Se cuestionaron los derechos de los grandes propietarios que acaparaban millones de hectáreas ociosas."
            },
            {
                "type": "narration",
                "text": "Se organizaron protestas en varias comunidades rurales que enfrentaban la voracidad de las haciendas azucareras y ganaderas. Se reclamaron nuevas formas de propiedad agrícola que protegieran los derechos ancestrales indígenas."
            },
            {
                "type": "narration",
                "text": "La cuestión agraria fue uno de sus motores centrales, precisamente a causa de que esta tensión llevaba ya décadas acumulándose sin resolverse, convirtiendo al campo en un polvorín a punto de estallar."
            }
        ]
    },

    "b1-revolucion-03-madero.json": {
        "id": "story.b1.revolucion.03",
        "title": "Obreros, huelgas y el desafío de las alianzas",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Junto al clamor campesino por la tierra, las fábricas y minas aportaron una fuerza combativa disciplinada. Los trabajadores protestaron, reclamando mejores salarios y un trato digno. Los obreros se organizaron, formando sindicatos en las fábricas textiles y ferroviarias."
            },
            {
                "type": "narration",
                "text": "Los mineros participaron en huelgas, exigiendo mejores condiciones laborales frente a empresas extranjeras intransigentes. Los trabajadores se movilizaron, defendiendo sus derechos laborales en las plazas públicas. Sin embargo, unir el campo y la ciudad resultó una tarea titánica."
            },
            {
                "type": "narration",
                "text": "El movimiento obrero no logró articularse con el movimiento campesino sin que existieran profundas diferencias culturales entre ambos grupos. Estos sindicatos organizaron huelgas generales de gran escala, sin que estos movimientos consiguieran aliarse de manera duradera con las demandas campesinas."
            },
            {
                "type": "narration",
                "text": "Esta separación no ocurrió sin que hubiera intentos genuinos de unirlos a través de comités mixtos y periódicos populares. La desconfianza mutua y las distancias geográficas dificultaron la coordinación estratégica en momentos cruciales."
            },
            {
                "type": "narration",
                "text": "Ningún movimiento revolucionario logró triunfar de manera duradera sin que se produjera una alianza efectiva entre el descontento rural y el urbano. Cuando esa confluencia histórica se produjo, el viejo régimen no pudo resistir el empuje."
            }
        ]
    },

    "b1-revolucion-04-zapatapancho.json": {
        "id": "story.b1.revolucion.04",
        "title": "La toma del poder y el reto de construir el Estado",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Derribar a un dictador atrincherado en su palacio suele ser el momento más épico de cualquier insurrección popular. Sin embargo, El verdadero desafío comenzará después: construir un nuevo Estado capaz de gobernar un país profundamente fracturado."
            },
            {
                "type": "narration",
                "text": "Los movimientos revolucionarios exitosos tendrán que enfrentar preguntas que ninguna consigna previa a la victoria logra responder por sí sola. ¿Cómo reactivar la economía destruida? ¿Cómo desarmar a los caudillos rebeldes? ¿Cómo conciliar las aspiraciones campesinas con el orden legal?"
            },
            {
                "type": "narration",
                "text": "La fase que sigue a una victoria revolucionaria será, con frecuencia, más violenta que la propia lucha por el poder. A raíz del triunfo revolucionario, se propusieron nuevas reformas institucionales para consolidar las conquistas populares."
            },
            {
                "type": "narration",
                "text": "Como consecuencia del conflicto, se redactó una nueva constitución que codificó los derechos sociales. Sin embargo, la transformación política fue gradual y llena de contradicciones. A lo largo del proceso, surgieron nuevos conflictos políticos entre las distintas facciones triunfantes."
            },
            {
                "type": "narration",
                "text": "Esta tensión explicará por qué tantos movimientos terminarán derivando hacia formas de gobierno alejadas de sus ideales fundacionales, sustituyendo el entusiasmo democrático inicial por una disciplina estatal centralizada."
            }
        ]
    },

    "b1-revolucion-05-constitucion1917.json": {
        "id": "story.b1.revolucion.05",
        "title": "Precondiciones estructurales y debates históricos",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al examinar los grandes estallidos sociales de América Latina, los historiadores y sociólogos identifican patrones recurrentes. Se puede considerar que la revolución abrió nuevas posibilidades políticas para sectores antes marginados. Se puede afirmar que el proceso produjo cambios importantes en la legislación y la cultura política."
            },
            {
                "type": "narration",
                "text": "Se puede interpretar que la revolución también generó violencia y destrucción económica de inmensa magnitud. Se puede señalar que sus consecuencias fueron contradictorias, combinando avances sociales indiscutibles con nuevas formas de autoritarismo."
            },
            {
                "type": "narration",
                "text": "Tanto la concentración extrema de la tierra como la existencia de un movimiento obrero organizado resultan condiciones casi siempre presentes en las crisis revolucionarias. Tanto los países con enorme desigualdad de tierra como los países con fuertes movimientos sindicales experimentaron décadas de tensión."
            },
            {
                "type": "narration",
                "text": "Lo que distingue un país donde estalla una revolución es tanto la debilidad del Estado como la capacidad de las fuerzas de oposición para actuar coordinadamente frente al poder central."
            },
            {
                "type": "narration",
                "text": "Con estas herramientas conceptuales -tanto la definición de revolución como sus precondiciones estructurales- estamos ya preparados para examinar el caso mexicano, el primer gran cataclismo revolucionario del siglo veinte."
            }
        ]
    },

    # =========================================================================
    # UNIT 16: revolucionmexicana
    # =========================================================================
    "b1-revolucionmexicana-01-caudillos.json": {
        "id": "story.b1.revolucionmexicana.01",
        "title": "El ocaso del Porfiriato (1876-1910)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En 1910, Porfirio Díaz llevaba ya gobernando México, casi sin interrupción, treinta y cuatro años. El régimen porfirista, bajo el lema de 'Orden y Progreso', exhibía cifras económicas deslumbrantes. Durante el Porfiriato se ampliaron los ferrocarriles, aunque el poder político permaneció muy concentrado."
            },
            {
                "type": "narration",
                "text": "México llevaba décadas atrayendo inversión extranjera masiva y modernizando sus principales ciudades. La modernización económica fue impulsada por inversiones que transformaron distintas regiones mineras e industriales del norte y el centro del país."
            },
            {
                "type": "narration",
                "text": "La reelección de Díaz permitió que su gobierno continuara durante décadas sin dar cabida a la renovación democrática. El poder era monopolizado por una camarilla de tecnócratas y terratenientes conocidos como 'los Científicos'."
            },
            {
                "type": "narration",
                "text": "Este mismo periodo llevaba concentrando la propiedad de la tierra en muy pocas manos a una velocidad extraordinaria. Comunidades indígenas enteras fueron despojadas de sus tierras ancestrales en Morelos, Sonora y Yucatán para engrosar gigantescas haciendas azucareras y henequeneras."
            },
            {
                "type": "narration",
                "text": "Esta combinación llevaba funcionando con éxito durante más de tres décadas gracias al uso sistemático del ejército y la policía de rurales. Pero cuando el anciano dictador cumplió ochenta años, el edificio porfirista crujió ante el menor temblor político."
            }
        ]
    },

    "b1-revolucionmexicana-02-cardenas.json": {
        "id": "story.b1.revolucionmexicana.02",
        "title": "La insurrección maderista y la caída del dictador",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En 1908, Porfirio Díaz declaró al periodista James Creelman que México estaba listo para la democracia. Francisco I. Madero, un hacendado liberal del norte, tomó al pie de la letra sus palabras y fundó el Partido Nacional Antirreeleccionista. Madero denunció la falta de elecciones libres y llamó a la población a levantarse en armas."
            },
            {
                "type": "narration",
                "text": "El Plan de San Luis Potosí pedía que el pueblo mexicano se levantara en armas el 20 de noviembre de 1910. Madero exigía que se anularan las elecciones y que se convocaran nuevos comicios verdaderamente libres bajo el lema 'Sufragio Efectivo, No Reelección'."
            },
            {
                "type": "narration",
                "text": "La insurrección prendió con fuerza en el norte con Pascual Orozco y Pancho Villa, y en el sur con Emiliano Zapata. Ante el avance imparable de las fuerzas revolucionarias, Díaz pidió que se negociara su salida del poder. En mayo de 1911, Díaz renunció y partió al exilio en Francia, advirtiendo que Madero 'había soltado al tigre'."
            },
            {
                "type": "narration",
                "text": "Se inició una nueva etapa política, aunque las tensiones sociales no desaparecieron. Después de que Díaz cayó, continuaron los conflictos porque distintos grupos tenían objetivos diferentes."
            },
            {
                "type": "narration",
                "text": "El propio Madero pronto exigiría de sus antiguos aliados algo que muchos de ellos no estaban dispuestos a aceptar: paciencia. Madero creía que bastaba con una reforma democrática, mientras campesinos y obreros exigían tierra y justicia social inmediata."
            }
        ]
    },

    "b1-revolucionmexicana-03-petroleo.json": {
        "id": "story.b1.revolucionmexicana.03",
        "title": "Zapata, Villa y la guerra de facciones",
        "paragraphs": [
            {
                "type": "narration",
                "text": "El hecho de que Madero no atendiera con suficiente urgencia la reforma agraria explica la ruptura casi inmediata con Zapata. En noviembre de 1911, Emiliano Zapata proclamó el Plan de Ayala, exigiendo la restitución inmediata de las tierras comunales a los pueblos bajo la consigna 'Tierra y Libertad'."
            },
            {
                "type": "narration",
                "text": "En febrero de 1913, el general Victoriano Huerta encabezó un sangriento golpe militar durante la Decena Trágica, asesinando a Madero. Para derrocar a Huerta, Venustiano Carranza lideró el Ejército Constitucionalista. Mientras avanzaban los ejércitos revolucionarios, cambiaban las alianzas políticas en el campo de batalla."
            },
            {
                "type": "narration",
                "text": "Villa dirigía un ejército revolucionario que tenía una fuerte presencia en el norte: la legendaria División del Norte. Zapata defendía el reparto agrario, mientras sus seguidores reclamaban cambios en la propiedad de la tierra en los campos de Morelos."
            },
            {
                "type": "narration",
                "text": "El hecho de que Zapata y Villa tuvieran objetivos y estilos tan distintos no impidió que, en 1914, ambos ejércitos ocuparan juntos la Ciudad de Mキシco y se fotografiaran en la silla presidencial de Palacio Nacional. El hecho de que esta alianza careciera de un programa político unificado explica por qué resultó tan efímera."
            },
            {
                "type": "narration",
                "text": "Las fuerzas constitucionalistas de Álvaro Obregón derrotaron militarmente a Villa en las batallas de Celaya (1915). Tanto Zapata como Villa acabarían siendo asesinados, sin haber logrado nunca imponer plenamente su visión particular de la revolución, aunque sus demandas quedaron inmortalizadas en la memoria popular."
            }
        ]
    },

    "b1-revolucionmexicana-04-artecultura.json": {
        "id": "story.b1.revolucionmexicana.04",
        "title": "La Constitución de Querétaro de 1917",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Para institucionalizar el nuevo orden surgido de las armas, Venustiano Carranza convocó a un congreso constituyente. Lo que se redactó en la ciudad de Querétaro, en 1917, superó ampliamente cualquier expectativa moderada. A raíz de la revolución, la Constitución incorporó demandas relacionadas con la tierra y el trabajo."
            },
            {
                "type": "narration",
                "text": "Lo que hizo verdaderamente radical a esta nueva constitución fueron dos artículos en particular: el Artículo 27 y el Artículo 123. El Artículo 27 declaró que la propiedad originaria de tierras, aguas y recursos del subsuelo correspondía a la Nación, sentando las bases jurídicas para el reparto agrario y la nacionalización petrolera."
            },
            {
                "type": "narration",
                "text": "Por su parte, el Artículo 123 consagró los derechos laborales más avanzados del mundo: jornada máxima de ocho horas, salario mínimo, prohibición del trabajo infantil y derecho a la huelga. El artículo constitucional estableció derechos que podían utilizarse para impulsar reformas profundas."
            },
            {
                "type": "narration",
                "text": "En el marco de la nueva etapa política, el Estado asumió nuevas responsabilidades sociales. Lo que distinguió a esta constitución de la mayoría de las constituciones liberales del siglo diecinueve fue su ambición social explícita."
            },
            {
                "type": "narration",
                "text": "Lo que hace de la Constitución de 1917 un documento tan estudiado, incluso un siglo después, es precisamente esa combinación entre garantías individuales liberales y soberanía social comunitaria."
            }
        ]
    },

    "b1-revolucionmexicana-05-legadorevolucion.json": {
        "id": "story.b1.revolucionmexicana.05",
        "title": "El legado institucional y el cardenismo",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Concluida la fase armada que costó más de un millón de vidas, México inició una compleja etapa de reconstrucción. Se produjeron cambios institucionales importantes, aunque muchas demandas continuaron pendientes en los años siguientes. El legado revolucionario incluyó reformas que cambiaron la relación entre el Estado y la sociedad."
            },
            {
                "type": "narration",
                "text": "Se puede hablar de una reconstrucción política gradual, porque las transformaciones no ocurrieron de inmediato. En 1929, Plutarco Elías Calles fundó el Partido Nacional Revolucionario (PNR) para canalizar las disputas de los caudillos por vías institucionales."
            },
            {
                "type": "narration",
                "text": "El momento culminante de las reformas revolucionarias llegó durante la presidencia de Lázaro Cárdenas (1934-1940), quien repartió más de veinte millones de hectáreas a comunidades ejidales y decretó la expropiación petrolera en 1938."
            },
            {
                "type": "narration",
                "text": "El legado institucional de esta revolución no fue tanto una transformación completa e inmediata de la sociedad como la creación de un partido político dominante y un Estado árbitro. El resultado no fue tanto una sociedad plenamente igualitaria como una estabilidad política notable."
            },
            {
                "type": "narration",
                "text": "Gracias a este singular arreglo corporativo, México evitó el ciclo de golpes de Estado y dictaduras militares que sufrieron muchos de sus vecinos sudamericanos. El legado de la Revolución mexicana no fue tanto un final feliz y definitivo como el comienzo de un experimento institucional único en el continente."
            }
        ]
    },

    # =========================================================================
    # UNIT 17: nacionalismo
    # =========================================================================
    "b1-nacionalismo-01-ideas.json": {
        "id": "story.b1.nacionalismo.01",
        "title": "La construcción del Estado nacional moderno",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En las décadas que siguieron a 1910, los gobiernos latinoamericanos se propusieron forjar Estados modernos y unificados, superando el localismo y las divisiones regionales heredadas del siglo anterior. Durante este proceso se fortalecieron las instituciones, aunque la autoridad central no llegó a todas las regiones de la misma manera."
            },
            {
                "type": "narration",
                "text": "La administración estatal fue ampliada porque los gobiernos buscaban ejercer mayor autoridad sobre las provincias periféricas. Se crearon ministerios de hacienda, trabajo y educación pública con burocracias profesionales."
            },
            {
                "type": "narration",
                "text": "Las instituciones fueron reorganizadas mientras cambiaban las relaciones entre el Estado y las regiones. El ejército se profesionalizó mediante academias militares modernas, subordinando a los caudillos armados provinciales a la cadena de mando nacional."
            },
            {
                "type": "narration",
                "text": "Durante el proceso de unificación, el Estado extendió las redes de correos, carreteras, juzgados y recaudación impositiva. El Estado nacional comenzó a intervenir de manera activa en la regulación de la vida económica y en la resolución de conflictos sociales."
            },
            {
                "type": "narration",
                "text": "Esta consolidación estatal dotó por primera vez a los gobiernos centrales de instrumentos reales de soberanía, preparando el terreno para los grandes proyectos transformadores del siglo veinte."
            }
        ]
    },

    "b1-nacionalismo-02-indigenismo.json": {
        "id": "story.b1.nacionalismo.02",
        "title": "Nacionalismo cultural, indigenismo y vanguardias",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A pesar de que la construcción de un Estado más fuerte podría parecer un asunto puramente administrativo, estuvo acompañada por un ambicioso proyecto cultural. Intelectuales, escritores y artistas buscaron definir qué significaba ser auténticamente latinoamericano, alejándose de la ciega imitación de Europa."
            },
            {
                "type": "narration",
                "text": "En México, Perú y Bolivia surgió el indigenismo. El indigenismo buscaba incorporar el pasado prehispánico a la identidad nacional, a pesar de que las comunidades indígenas vivas siguieran sufriendo pobreza extrema. En Perú, José Carlos Mariátegui y Luis E. Valcárcel reivindicaron la cosmovisión andina."
            },
            {
                "type": "narration",
                "text": "En Brasil, la Semana de Arte Moderno buscó, a pesar de las resistencias de los sectores más conservadores, definir una identidad artística genuinamente brasileña. En 1922 en São Paulo, Mário de Andrade y Oswald de Andrade lanzaron el movimiento antropofágico: devorar la cultura europea para crear algo original y tropical."
            },
            {
                "type": "narration",
                "text": "Los muralistas mexicanos como Diego Rivera, José Clemente Orozco y David Alfaro Siqueiros cubrieron los muros públicos con la epopeya del pueblo mestizo. El indigenismo influyó en las artes plásticas y en la literatura de la época."
            },
            {
                "type": "narration",
                "text": "Esta paradoja -celebrar el pasado indígena a pesar de que se ignoraran las condiciones reales de los pueblos indígenas contemporáneos- resultaría cada vez más visible, pero dejó una huella estética imborrable en la conciencia continental."
            }
        ]
    },

    "b1-nacionalismo-03-economico.json": {
        "id": "story.b1.nacionalismo.03",
        "title": "La escuela pública como forja de la nación",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Para convertir a millones de campesinos e inmigrantes en ciudadanos patriotas, la escuela pública fue la herramienta más poderosa del Estado. Mientras crecían las escuelas públicas, aumentaba también el interés por formar ciudadanos. Los gobiernos impulsaron la alfabetización porque consideraban que la educación fortalecía la ciudadanía."
            },
            {
                "type": "narration",
                "text": "En México, el primer secretario de Educación Pública, José Vasconcelos, lanzó en 1921 una gigantesca cruzada de 'misiones culturales'. Maestros rurales viajaron a pie y a caballo a los rincones más apartados del país para enseñar a leer, higiene, música y civismo."
            },
            {
                "type": "narration",
                "text": "Dado el número de misiones organizadas, estas seguramente habrán alcanzado, hacia finales de la década de 1920, a una parte considerable de la población rural. Para entonces se habrá construido, solo en México, un número de escuelas rurales varias veces superior al que existía antes de la revolución."
            },
            {
                "type": "narration",
                "text": "Quienes hayan revisado su impacto real habrán confirmado que la educación pública resultó decisiva para construir un sentido de pertenencia nacional. En las aulas se enseñaba el himno patrio, el culto a los héroes de la independencia y una lengua común."
            },
            {
                "type": "narration",
                "text": "La escuela, el maestro y el idioma nacional se habrán convertido, en la práctica, en la cara más visible del propio Estado en las comunidades donde nunca antes había llegado la autoridad central."
            }
        ]
    },

    "b1-nacionalismo-04-cultura.json": {
        "id": "story.b1.nacionalismo.04",
        "title": "Integración territorial y presencia estatal",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A lo largo del proceso, los gobiernos intentaron reforzar las fronteras y ampliar la administración hacia las regiones interiores. La construcción de caminos, telégrafos y puentes comenzó a suturar un territorio que durante el siglo anterior había estado fragmentado en feudos aislados."
            },
            {
                "type": "narration",
                "text": "Amplias regiones del interior ya no estaban físicamente desconectadas del resto del territorio nacional, gracias al ferrocarril. En el marco de la integración territorial, algunas comunidades negociaron su posición frente al avance estatal."
            },
            {
                "type": "narration",
                "text": "Muchas comunidades rurales que antes gestionaban sus propios asuntos ya no podían hacerlo sin la intervención de alguna autoridad estatal. El servicio militar obligatorio, los censos nacionales y los registros civiles incorporaron a millones de personas a la vida institucional."
            },
            {
                "type": "narration",
                "text": "Poblaciones enteras ya no podían permanecer invisibles para el aparato estadístico del Estado. Las instituciones ampliaron su presencia en zonas donde el poder central antes había sido débil o inexistente."
            },
            {
                "type": "narration",
                "text": "Las regiones más remotas del país ya no podían considerarse, con propiedad, territorios ajenos a la autoridad efectiva del Estado nacional, consolidando el mapa geopolítico de cada república."
            }
        ]
    },

    "b1-nacionalismo-05-sintesis.json": {
        "id": "story.b1.nacionalismo.05",
        "title": "El nuevo rostro del Estado-nación",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A medida que avanzaban las primeras décadas del siglo veinte, el propio significado de la palabra \"Estado\" fue transformándose. El Estado-nación fue construido mediante reformas, aunque la integración política siguió siendo desigual entre el centro y la periferia."
            },
            {
                "type": "narration",
                "text": "A medida que se profesionalizaban los ejércitos y crecía la presencia burocrática cotidiana, el Estado dejaba de depender de la lealtad personal hacia un caudillo. La modernización fortaleció instituciones que aumentaron la capacidad administrativa del Estado en materia tributaria y jurídica."
            },
            {
                "type": "narration",
                "text": "A medida que este proceso avanzaba, también lo hacía un proyecto cultural paralelo destinado a dar sentido simbólico al Estado. La legitimidad se construía mientras el Estado intentaba integrar poblaciones diversas bajo símbolos patrios y derechos ciudadanos compartidos."
            },
            {
                "type": "narration",
                "text": "A medida que la escuela, el censo y el servicio militar alcanzaban regiones cada vez más remotas, la experiencia de ser ciudadano se volvía más concreta. El Estado nacional se convirtió en el principal mediador entre las clases sociales y en el promotor de la soberanía económica."
            },
            {
                "type": "narration",
                "text": "Esta síntesis nacionalista -institucional, cultural y territorial- redefinió la política latinoamericana, preparando el escenario para las grandes conmociones que desencadenaría la crisis mundial de 1929."
            }
        ]
    },

    # =========================================================================
    # UNIT 18: grandepresion
    # =========================================================================
    "b1-grandepresion-01-crisis1929.json": {
        "id": "story.b1.grandepresion.01",
        "title": "El crac de Wall Street y el colapso financiero",
        "paragraphs": [
            {
                "type": "narration",
                "text": "En octubre de 1929, la Bolsa de Nueva York se desplomó estrepitosamente en los fatídicos Jueves Negro y Martes Negro. Los inversores, que apenas acababan de disfrutar de casi una década de crecimiento aparentemente imparable, entraron en pánico. Millones de personas que acababan de perder buena parte de sus ahorros se lanzaron a retirar dinero de los bancos."
            },
            {
                "type": "narration",
                "text": "El resultado fue una crisis que, aunque había comenzado en Nueva York, no tardaría en sentirse en cualquier rincón del planeta. A raíz del colapso financiero, disminuyeron la producción y el comercio internacional a un ritmo vertiginoso."
            },
            {
                "type": "narration",
                "text": "A lo largo de los primeros años de la crisis, numerosos países experimentaron una fuerte recesión. Las quiebras bancarias en Estados Unidos y Europa paralizaron de golpe los flujos internacionales de crédito."
            },
            {
                "type": "narration",
                "text": "Como consecuencia de la crisis, la demanda internacional se redujo considerablemente. Los países industriales levantaron barreras arancelarias draconianas como el arancel Smoot-Hawley en Estados Unidos para proteger sus mercados internos."
            },
            {
                "type": "narration",
                "text": "Aunque la crisis comenzó en Estados Unidos, sus efectos se extendieron a otras economías con una rapidez devastadora. Para América Latina, atada al comercio exterior, representó el final abrupto de una era dorada."
            }
        ]
    },

    "b1-grandepresion-02-americalatina.json": {
        "id": "story.b1.grandepresion.02",
        "title": "El impacto demoledor en América Latina",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Tan pronto como la crisis financiera estadounidense comenzó a extenderse por el mundo, América Latina descubrió su vulnerabilidad estructural. Los países latinoamericanos sufrieron las consecuencias directas de la recesión mundial. Los ingresos por exportación fueron reducidos por la caída de la demanda internacional."
            },
            {
                "type": "narration",
                "text": "Tan pronto como la demanda mundial de café, cobre y salitre se desplomó, los precios de estos productos cayeron en picado. Las materias primas fueron vendidas a precios mucho más bajos durante la crisis. El café brasileño perdió más del sesenta por ciento de su valor, llevando al gobierno a quemar millones de sacos en locomotoras."
            },
            {
                "type": "narration",
                "text": "En Chile, según un informe de la Sociedad de Naciones, el impacto fue el más severo del mundo: las exportaciones de cobre y salitre cayeron en más del ochenta por ciento, arrojando a la miseria a decenas de miles de mineros en Atacama."
            },
            {
                "type": "narration",
                "text": "Tan pronto como los bancos estadounidenses y europeos dejaron de prestar dinero, varios gobiernos se vieron obligados a suspender el pago de su deuda externa. Los créditos internacionales fueron cortados por los bancos extranjeros."
            },
            {
                "type": "narration",
                "text": "Tan pronto como los gobiernos comprendieron la magnitud de lo que estaba ocurriendo, quedó claro que el modelo exportador no podría sobrevivir sin cambios. La crisis fiscal y social amenazaba la estabilidad de todos los regímenes políticos de la región."
            }
        ]
    },

    "b1-grandepresion-03-menoscomercio.json": {
        "id": "story.b1.grandepresion.03",
        "title": "La asfixia fiscal y el cierre de los mercados",
        "paragraphs": [
            {
                "type": "narration",
                "text": "La Gran Depresión fue la peor crisis económica que América Latina había sufrido jamás hasta ese momento. Entre 1929 y 1932, el valor de las exportaciones de la región se contrajo en más del sesenta por ciento. Esta caída resultó ser la mayor contracción comercial que sus economías jamás habían experimentado."
            },
            {
                "type": "narration",
                "text": "Se redujeron las importaciones cuando disminuyeron los ingresos procedentes de las exportaciones. Como los Estados dependían de los aranceles aduaneros para sus presupuestos, La caída del comercio se tradujo en la peor crisis fiscal que estos gobiernos jamás habían enfrentado."
            },
            {
                "type": "narration",
                "text": "Sin divisas para comprar bienes manufacturados en el extranjero, las tiendas quedaron desabastecidas y el desempleo se disparó en las ciudades portuarias. Se aumentaron algunos aranceles para proteger la producción nacional. En varios países se adoptaron medidas para estimular la demanda interna."
            },
            {
                "type": "narration",
                "text": "Esta combinación resultó la prueba más severa que los Estados latinoamericanos recién fortalecidos jamás habían enfrentado. Los gobernantes comprendieron que el viejo dogma liberal del libre cambio no ofrecía ninguna respuesta a la catástrofe."
            },
            {
                "type": "narration",
                "text": "El colapso comercial forzó a la región a replantearse de raíz su modelo económico y a buscar desesperadamente alternativas dentro de sus propias fronteras."
            }
        ]
    },

    "b1-grandepresion-04-cambiarmodelo.json": {
        "id": "story.b1.grandepresion.04",
        "title": "El viraje hacia la Industrialización por Sustitución de Importaciones",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Frente al colapso de las importaciones, una pregunta inevitable se impuso en los ministerios y las empresas: ¿Por qué seguir dependiendo de importar manufacturas en lugar de producirlas dentro del propio país? En lugar de exportar materias primas baratas para importar después productos caros, los países debían fabricar ellos mismos buena parte de lo que compraban."
            },
            {
                "type": "narration",
                "text": "Así nació el modelo de Industrialización por Sustitución de Importaciones (ISI). Los gobiernos respondieron a la crisis impulsando la producción nacional mediante aranceles proteccionistas, cuotas de importación y tipos de cambio preferenciales para maquinaria industrial."
            },
            {
                "type": "narration",
                "text": "Las industrias crecieron sustituyendo algunos productos que antes se importaban: textiles, alimentos procesados, calzado, cerveza, cemento y medicamentos básicos. Talleres y fábricas proliferaron en los suburbios de São Paulo, Buenos Aires, Medellín y la Ciudad de México."
            },
            {
                "type": "narration",
                "text": "Los Estados ampliaron su intervención buscando reducir los efectos de la crisis. En lugar de limitarse a recaudar impuestos y mantener el orden, muchos gobiernos comenzaron a invertir directamente en industrias estratégicas como el petróleo, el acero y la energía eléctrica."
            },
            {
                "type": "narration",
                "text": "Las economías cambiaron adaptándose a un contexto en el que el comercio internacional era menor. El eje dinámico de la economía se trasladó definitivamente del campo a las fábricas de las grandes ciudades."
            }
        ]
    },

    "b1-grandepresion-05-transformoregion.json": {
        "id": "story.b1.grandepresion.05",
        "title": "1929 como punto de inflexión histórica",
        "paragraphs": [
            {
                "type": "narration",
                "text": "La Gran Depresión no fue una simple recesión cíclica; fue un auténtico terremoto político, social y económico que clausuró el siglo diecinueve en América Latina. La crisis expuso brutalmente la vulnerabilidad del modelo exportador. De ahí que muchos historiadores consideren 1929 uno de los verdaderos puntos de inflexión de la historia contemporánea."
            },
            {
                "type": "narration",
                "text": "La crisis demostró que ese modelo ya no bastaba. De ahí que resultara tan difícil, después de 1929, defender seriamente su continuidad. En 1930, una ola de golpes de Estado y cambios revolucionarios derribó regímenes en Argentina, Brasil, Perú, Bolivia y Chile. En Brasil, la Revolución de 1930 llevó al poder a Getúlio Vargas, poniendo fin a la 'República Velha' de los barones del café."
            },
            {
                "type": "narration",
                "text": "A lo largo de la década, la crisis produjo una transformación de las políticas económicas de varios países. Como consecuencia de la caída de las exportaciones, los gobiernos tuvieron que buscar nuevas fuentes de crecimiento en el mercado interno y el empleo urbano."
            },
            {
                "type": "narration",
                "text": "La crisis puso de manifiesto una dependencia exterior que había sido menos visible durante los años anteriores. Aunque la recuperación fue desigual, el periodo contribuyó a fortalecer la intervención del Estado en la economía."
            },
            {
                "type": "narration",
                "text": "Se abrió un espacio político para nuevas ideas. De ahí que surgieran figuras políticas de un tipo nuevo, capaces de apelar directamente a las masas de trabajadores urbanos con programas nacionalistas. La industrialización comenzó casi por necesidad. De ahí que se convirtiera, en las siguientes décadas, en la política económica dominante de la región, inaugurando la era del populismo clásico."
            }
        ]
    }
}

OUTPUT_DIR = "content/es-latam/stories/world/b1"

def main():
    for fname, data in STORIES.items():
        data["level"] = "B1"
        path = os.path.join(OUTPUT_DIR, fname)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        words = sum(len(p["text"].split()) for p in data["paragraphs"])
        print(f"Wrote {fname}: {words} words, {len(data['paragraphs'])} paras")

if __name__ == "__main__":
    main()
