"""
Generates rich, detailed narrative stories for Block 6 (Units 31-36, 30 lessons).
Units:
31: movimientosindigenas
32: integracionregional
33: finalguerrafria
34: latamnoventa
35: legadosigloveinte
36: americalatinadosmil

Embeds every grammar sentence directly from reqs JSON to ensure 100% verbatim accuracy.
"""

import json
import os

reqs = json.load(open('scripts/block6_all_reqs.json', encoding='utf-8'))

def G(lesson_key, idx):
    return reqs[lesson_key]['grammar_sentences'][idx]

STORIES = {}

# =============================================================================
# UNIT 31: movimientosindigenas
# =============================================================================

# 31.01: movimientosindigenas-01
k = "movimientosindigenas-01"
# Grammar (8):
# 0: A raíz de los cambios históricos, algunas comunidades han defendido territorios que consideran ancestrales.
# 1: A lo largo de los siglos, muchos pueblos han conservado tradiciones que forman parte de su identidad.
# 2: Como consecuencia de distintas políticas, algunas comunidades perdieron parte del territorio que utilizaban.
# 3: Aunque los pueblos indígenas son diversos, muchas comunidades comparten problemas relacionados con la tierra y el reconocimiento.
# 4: Varios cientos de lenguas propias, ninguna de ellas, ni mucho menos, reducible a una sola cultura homogénea.
# 5: La mayoría de los Estados ni siquiera reconocían esta diversidad, y ni mucho menos concedían derechos diferenciados.
# 6: El gobierno no consultó a las comunidades, y ni mucho menos buscó su consentimiento antes de actuar.
# 7: Nadie esperaba una victoria fácil, y ni mucho menos un cambio tan profundo en tan poco tiempo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La emergencia indígena y el despertar de los pueblos originarios",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A finales del siglo veinte, más de cuarenta millones de personas pertenecientes a cientos de nacionalidades originarias habitaban el continente americano. {G(k, 4)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"Durante más de un siglo de vida republicana independiente, las políticas asimilacionistas pretendieron borrar las identidades originarias en nombre de la homogeneidad mestiza. {G(k, 2)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Cuando las empresas madereras, petroleras y mineras penetraron en territorios sagrados en la Amazonía y los Andes, {G(k, 6)} desatando una indignación colectiva acumulada durante generaciones."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} El año 1992, coincidiendo con el V Centenario de la llegada europea, marcó el punto de inflexión con la consigna continental '500 años de resistencia indígena y popular'. {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": "Los pueblos originarios abandonaron la posición de víctimas pasivas para convertirse en protagonistas políticos decisivos de la refundación democrática de América Latina."
        }
    ]
}

# 31.02: movimientosindigenas-02
k = "movimientosindigenas-02"
# Grammar (8):
# 0: El Convenio 169 reconocía, en la medida en que los países lo ratificaran, el derecho a ser consultados previamente.
# 1: Este convenio se convirtió, en la medida en que más países lo fueron ratificando, en la herramienta legal más citada.
# 2: En la medida en que estos derechos territoriales se fueron reconociendo legalmente, también surgieron nuevos conflictos.
# 3: El proyecto solo podía avanzar en la medida en que la comunidad afectada diera su consentimiento previo.
# 4: Algunos territorios fueron reconocidos mediante leyes que protegían derechos comunitarios.
# 5: La propiedad de ciertas tierras fue disputada mientras las comunidades defendían sus reivindicaciones.
# 6: Los derechos territoriales fueron incorporados a normas que buscaban reconocer la diversidad cultural.
# 7: Las demandas fueron presentadas ante instituciones que podían modificar la situación jurídica de las comunidades.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Convenio 169 de la OIT y la batalla por el territorio",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En 1989, la Organización Internacional del Trabajo adoptó el histórico Convenio 169 sobre Pueblos Indígenas y Tribales en Países Independientes. {G(k, 0)} {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 7)} Líderes indígenas recurrieron a las cortes constitucionales y al sistema interamericano de derechos humanos para frenar concesiones extractivas inconsultas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 5)} {G(k, 3)} libre e informado, transformando la relación jurídica entre los Estados nacionales y las nacionalidades indígenas ancestrales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Gobiernos y corporaciones transnacionales alegaron que los recursos del subsuelo pertenecían a la nación entera, chocando frontalmente con la cosmovisión comunitaria del 'Buen Vivir' y la defensa de la Madre Tierra."
        },
        {
            "type": "narration",
            "text": "La lucha por la tierra dejó de ser un simple reclamo agrario de parcelas para convertirse en una demanda integral de autodeterminación territorial y soberanía cultural."
        }
    ]
}

# 31.03: movimientosindigenas-03
k = "movimientosindigenas-03"
# Grammar (8):
# 0: La constitución colombiana definió a Colombia, en calidad de nación, como un país multiétnico y pluricultural.
# 1: Bolivia se redefinió a sí misma, en calidad de Estado, como un "Estado Plurinacional".
# 2: El representante indígena participó en las negociaciones en calidad de observador oficial.
# 3: Este documento fue presentado en calidad de propuesta, no como una decisión ya tomada.
# 4: Se reconoce la diversidad cultural cuando las instituciones permiten que distintas comunidades mantengan sus prácticas.
# 5: Se ha reclamado el uso de lenguas indígenas, aunque todavía existen obstáculos en algunos servicios públicos.
# 6: Se considera que la identidad cambia cuando una comunidad adapta sus prácticas a nuevas circunstancias.
# 7: En algunos países se han creado programas que buscan fortalecer la lengua y la cultura indígenas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Constitucionalismo plurinacional y diversidad cultural",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Durante la década de 1990, una ola de reformas constitucionales barrió el continente para reconocer la composición plural de las repúblicas. {G(k, 0)} {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"En Ecuador (1998 y 2008) y en Bolivia (2009), los movimientos originarios lograron transformaciones aún más radicales. {G(k, 1)} consagrando la justicia comunitaria originaria y la cosmovisión del Sumak Kawsay."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} en asambleas constituyentes y mesas de concertación territorial. {G(k, 3)} para democratizar el acceso a los recursos y la representación legislativa."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} {G(k, 5)} Lenguas como el quechua, el aymara, el guaraní y las lenguas mayas alcanzaron estatus de cooficialidad en sistemas educativos bilingües interculturales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La plurinacionalidad demostró que la unidad nacional no requiere uniformidad autoritaria, sino el respeto recíproco entre pueblos diversos."
        }
    ]
}

# 31.04: movimientosindigenas-04
k = "movimientosindigenas-04"
# Grammar (8):
# 0: La CONAIE organizó el primer gran levantamiento indígena nacional, al grito de "¡Nada solo para los indios, todo para todos!".
# 1: El EZLN se levantó en armas, al grito de "¡Ya basta!", exigiendo tierra, trabajo, vivienda y democracia.
# 2: Miles de manifestantes marcharon al grito de consignas que exigían el reconocimiento inmediato de sus derechos territoriales.
# 3: El movimiento se extendió rápidamente al grito de un lema que resumía, en pocas palabras, sus demandas centrales.
# 4: Las organizaciones crecieron defendiendo sus derechos mientras buscaban mayor representación política.
# 5: Los movimientos avanzaron negociando con gobiernos que no siempre aceptaban sus propuestas.
# 6: Las comunidades participaron en protestas reclamando cambios que pudieran mejorar sus condiciones.
# 7: Los dirigentes fueron adquiriendo influencia mientras construían organizaciones capaces de actuar a escala nacional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Levantamientos indígenas: la CONAIE en Ecuador y el EZLN en Chiapas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En junio de 1990, {G(k, 0)} Millones de campesinos e indígenas de la sierra y la Amazonía ecuatoriana paralizaron carreteras y ocuparon plazas públicas, obligando al gobierno de Rodrigo Borja a negociar títulos de propiedad comunitarios."
        },
        {
            "type": "narration",
            "text": f"El 1 de enero de 1994, coincidiendo con la entrada en vigor del Tratado de Libre Comercio de América del Norte (TLCAN), {G(k, 1)} en las selvas de Chiapas. Liderados por el subcomandante Marcos, los zapatistas exigieron autonomía y justicia para los pueblos originarios."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 7)} En Bolivia, la CSUTCB y las federaciones cocaleras lideradas por Evo Morales bloquearon los caminos del altiplano y el Chapare contra la erradicación forzosa de la hoja de coca milenaria."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 3)} {G(k, 6)} {G(k, 5)} La 'Guerra del Agua' en Cochabamba (2000) y la 'Guerra del Gas' (2003) demostraron la capacidad de veto de los movimientos populares frente a la privatización de los bienes comunes."
        },
        {
            "type": "narration",
            "text": "Estas memorables movilizaciones transformaron para siempre el equilibrio de poder en la región andina y mesoamericana, inaugurando una nueva era de protagonismo político originario."
        }
    ]
}

# 31.05: movimientosindigenas-05
k = "movimientosindigenas-05"
# Grammar (8):
# 0: El número de funcionarios indígenas aumentó, a la vez que crecían también las organizaciones indígenas propias.
# 1: Esta declaración, a la vez que carecía de fuerza legal obligatoria, ofrecía un marco de referencia ampliamente citado.
# 2: Persistían brechas profundas, a la vez que se multiplicaban estos avances políticos y simbólicos.
# 3: Los conflictos se multiplicaron a la vez que crecía la demanda global de materias primas.
# 4: A lo largo de las últimas décadas, la representación ha aumentado, aunque persisten desigualdades importantes.
# 5: La autonomía puede adoptar formas diferentes, por lo que no existe una única solución para todos los pueblos.
# 6: Como consecuencia de la movilización, algunos liderazgos indígenas han adquirido una presencia que antes era limitada.
# 7: Aunque existen avances institucionales, la participación efectiva sigue dependiendo de las condiciones sociales y políticas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Nuevos liderazgos, la victoria de Evo Morales y desafíos del siglo XXI",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En diciembre de 2005, un acontecimiento histórico conmovió al mundo: Evo Morales Ayma, líder sindical aymara, fue elegido presidente de Bolivia con el 54% de los votos, convirtiéndose en el primer mandatario indígena en gobernar el país desde la conquista española."
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 6)} {G(k, 4)} Ministros, diputadas y alcaldes vistieron polleras y ponchos tradicionales en los palacios de gobierno en La Paz, Quito y Bogotá."
        },
        {
            "type": "narration",
            "text": f"En 2007, la Asamblea General de la ONU aprobó la Declaración sobre los Derechos de los Pueblos Indígenas. {G(k, 1)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"Sin embargo, las contradicciones no desaparecieron. {G(k, 3)} {G(k, 2)} El avance de la megaminería, la soja transgénica y las represas hidroeléctricas generó tensiones con gobiernos de todo signo político."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} La defensa de los ecosistemas y la demanda de una verdadera autodeterminación sitúan a los movimientos indígenas en la vanguardia de las luchas ecológicas y sociales del siglo veintiuno."
        }
    ]
}

# =============================================================================
# UNIT 32: integracionregional
# =============================================================================

# 32.01: integracionregional-01
k = "integracionregional-01"
# Grammar (8):
# 0: El sueño de la unidad latinoamericana se remonta a las propuestas de Simón Bolívar en el siglo diecinueve.
# 1: La ALALC y el Pacto Andino buscaron fomentar el comercio intrarregional mediante acuerdos arancelarios.
# 2: Las diferencias económicas y las barreras comerciales dificultaron los primeros intentos de integración.
# 3: En 1826, Simón Bolívar convocó el Congreso Anfictiónico de Panamá con la visión de una confederación de repúblicas hispanoamericanas.
# 4: La Asociación Latinoamericana de Libre Comercio (ALALC) de 1960 representó el primer intento formal de integración comercial moderna.
# 5: El Pacto Andino de 1969 buscó coordinar el desarrollo industrial de Bolivia, Colombia, Chile, Ecuador y Perú.
# 6: Las rivalidades geopolíticas y las dictaduras militares frustraron reiteradamente las metas iniciales de estos bloques.
# 7: Los primeros proyectos de integración regional enfrentaron importantes obstáculos políticos y económicos.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El sueño de Bolívar y los primeros pasos de la integración moderna",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 3)} Bolívar anhelaba una alianza defensiva común que preservara la independencia frente a las ambiciones imperiales europeas y norteamericanas."
        },
        {
            "type": "narration",
            "text": f"Durante el periodo de la industrialización dirigida por el Estado, los países comprendieron que sus mercados nacionales eran demasiado pequeños para sostener industrias de bienes de capital. {G(k, 4)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Se diseñó un estatuto pionero para regular las inversiones extranjeras (Decisión 24) y planificar sectores metalmecánicos y petroquímicos complementarios."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, {G(k, 2)} {G(k, 6)} {G(k, 7)} La salida de Chile bajo la dictadura de Pinochet en 1976 debilitó el proyecto andino."
        },
        {
            "type": "narration",
            "text": "A pesar de estos tropiezos, la convicción de que la integración económica era indispensable para negociar en bloque en el escenario internacional sentó las bases para los tratados de nueva generación de los años noventa."
        }
    ]
}

# 32.02: integracionregional-02
k = "integracionregional-02"
# Grammar (8):
# 0: El Tratado de Asunción de 1991 fundó el Mercosur entre Argentina, Brasil, Paraguay y Uruguay.
# 1: El bloque eliminó aranceles internos y estableció un arancel externo común para el comercio con terceros países.
# 2: El Mercosur promovió un aumento espectacular del comercio entre los países miembros durante sus primeros años.
# 3: El 26 de marzo de 1991, los presidentes de cuatro naciones del Cono Sur firmaron el Tratado de Asunción creando el Mercosur.
# 4: La eliminación progresiva de barreras aduaneras cuadruplicó el comercio intrarregional en menos de una década.
# 5: La integración automotriz y agroindustrial consolidó una profunda interdependencia productiva entre Argentina y Brasil.
# 6: Las asimetrías económicas entre las economías gigantes y los socios menores generaron recurrentes disputas comerciales.
# 7: La creación del Mercosur impulsó el comercio y la cooperación en el Cono Sur.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El nacimiento del Mercosur: el Tratado de Asunción de 1991",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 7)} Tras décadas de rivalidad nuclear y militar entre Buenos Aires y Brasilia, los presidentes Raúl Alfonsín y José Sarney habían iniciado un histórico acercamiento diplomático en 1985."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 4)} El intercambio comercial intrazona saltó de 4.000 millones de dólares en 1990 a más de 20.000 millones a finales de la década."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} Fábricas en Córdoba, Rosario, São Paulo y Curitiba articularon cadenas de montaje complementarias de motores y autopartes."
        },
        {
            "type": "narration",
            "text": f"No obstante, el bloque debió sortear turbulencias monetarias severas tras la devaluación del real brasileño en 1999 y la crisis argentina de 2001. {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": "Con la posterior incorporación del Protocolo de Ushuaia sobre Compromiso Democrático, el Mercosur consolidó una cláusula democrática que frenó intentonas golpistas en Paraguay y afianzó la paz regional."
        }
    ]
}

# 32.03: integracionregional-03
k = "integracionregional-03"
# Grammar (8):
# 0: El Tratado de Libre Comercio de América del Norte (TLCAN) entró en vigor en 1994 entre México, Estados Unidos y Canadá.
# 1: El acuerdo convirtió a México en una de las mayores plataformas de exportación manufacturera del mundo.
# 2: El TLCAN generó profundas transformaciones en la agricultura mexicana, afectando al sector campesino tradicional.
# 3: El 1 de enero de 1994 comenzó a regir el TLCAN, sellando la integración económica formal de México con América del Norte.
# 4: La instalación masiva de plantas maquiladoras en la frontera norte impulsó la exportación de automóviles, televisores y computadoras.
# 5: La importación masiva de maíz subsidiado estadounidense golpeó duramente a millones de pequeños productores campesinos mexicanos.
# 6: El acuerdo profundizó la brecha económica entre el norte industrializado y el sur rural de México.
# 7: El TLCAN transformó la estructura comercial de México y sus relaciones económicas.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El TLCAN y el giro geopolítico de México hacia el norte",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 7)} Negociado por el presidente Carlos Salinas de Gortari, el tratado representó un viraje estratégico decisivo para la economía mexicana."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 4)} Ciudades fronterizas como Tijuana, Ciudad Juárez y Reynosa crecieron a un ritmo vertiginoso al compás de la inversión extranjera directa."
        },
        {
            "type": "narration",
            "text": f"Sin embargo, el impacto social fue sumamente dispar. {G(k, 2)} {G(k, 5)} que no podían competir con la agroindustria tecnificada del 'corn belt' de Iowa e Illinois."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Mientras Querétaro, Monterrey y Aguascalientes se integraban a las cadenas globales de valor aeroespacial y automotriz, estados como Oaxaca, Guerrero y Chiapas permanecían rezagados."
        },
        {
            "type": "narration",
            "text": "El TLCAN consagró el llamado 'regionalismo abierto', atando el destino productivo de México al ciclo económico de los Estados Unidos."
        }
    ]
}

# 32.04: integracionregional-04
k = "integracionregional-04"
# Grammar (8):
# 0: La propuesta del Área de Libre Comercio de las Américas (ALCA) impulsada por Washington fue rechazada en 2005.
# 1: La Cumbre de las Américas de Mar del Plata marcó un giro hacia proyectos de integración con mayor contenido político y social.
# 2: Nuevos organismos como UNASUR y la CELAC promovieron la concertación política sin la participación de Estados Unidos.
# 3: La IV Cumbre de las Américas en Mar del Plata en noviembre de 2005 selló el entierro definitivo del proyecto del ALCA.
# 4: Los presidentes Néstor Kirchner, Luiz Inácio Lula da Silva y Hugo Chávez lideraron el rechazo al tratado de libre comercio hemisférico.
# 5: La Unión de Naciones Suramericanas (UNASUR) se fundó en 2008 para coordinar políticas de defensa, salud e infraestructura física.
# 6: La Comunidad de Estados Latinoamericanos y Caribeños (CELAC) agrupó por primera vez a los treinta y tres países soberanos de la región.
# 7: El rechazo del ALCA abrió una nueva etapa en los proyectos de integración regional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Mar del Plata 2005, el 'No al ALCA' y la nueva arquitectura regional",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En 1994 en Miami, la Casa Blanca había propuesto crear una gigantesca zona de libre comercio desde Alaska hasta Tierra del Fuego. Sin embargo, {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 4)} con el resonante discurso de Chávez en el estadio mundialista proclamando '¡ALCA, ALCA, al carajo!'. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Mediante el Consejo de Defensa Suramericano, UNASUR desactivó graves crisis políticas en Bolivia (2008) y Ecuador (2010) sin intervención de Washington ni de la OEA."
        },
        {
            "type": "narration",
            "text": f"En diciembre de 2011 en Caracas, {G(k, 6)} consolidando un foro diplomático de diálogo autónomo sin la presencia de Estados Unidos ni de Canadá."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} Esta arquitectura multilateral afirmó la vocación latinoamericana de soberanía y multipolaridad en el escenario global."
        }
    ]
}

# 32.05: integracionregional-05
k = "integracionregional-05"
# Grammar (8):
# 0: La integración regional enfrenta tensiones entre modelos económicos diferentes y cambios de orientación política.
# 1: La Alianza del Pacífico y el Mercosur representaron visiones contrastantes sobre la inserción en la economía global.
# 2: La cooperación en infraestructura, energía y ciencia continúa siendo un desafío clave para el desarrollo del continente.
# 3: La Alianza del Pacífico, fundada en 2011 por Chile, Colombia, México y Perú, priorizó la apertura hacia los mercados asiáticos.
# 4: La polarización ideológica debilitó organismos como UNASUR cuando cambiaron los signos políticos de los gobiernos de la región.
# 5: La Iniciativa para la Integración de la Infraestructura Regional Suramericana (IIRSA) buscó conectar corredores bioceánicos.
# 6: La integración latinoamericana requiere superar la retórica diplomática y construir consensos pragmáticos y duraderos.
# 7: El debate sobre el modelo de integración sigue abierto en América Latina.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Modelos en pugna, vaivenes políticos y el futuro de la unidad",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Al iniciarse la segunda década del siglo veintiuno, el mapa de la integración regional exhibía una notable fragmentación. {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 3)} con un enfoque pragmático y desregulado, mientras el Mercosur enfatizaba la protección industrial y la dimensión social y ciudadana."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Los cambios de signo partidario paralizaron temporalmente instituciones multilaterales que dependían en exceso de la afinidad personal entre presidentes de turno."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} Carreteras transoceánicas, gasoductos binacionales e interconexiones eléctricas demostraron ser las venas materiales necesarias para unir a los pueblos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Solo una integración fundamentada en intereses productivos compartidos y respeto a la pluralidad permitirá a América Latina hablar con voz propia y respetada ante las grandes potencias mundiales."
        }
    ]
}

# =============================================================================
# UNIT 33: finalguerrafria
# =============================================================================

# 33.01: finalguerrafria-01
k = "finalguerrafria-01"
# Grammar (8):
# 0: La caída del Muro de Berlín en 1989 y la disolución de la Unión Soviética en 1991 transformaron el escenario internacional.
# 1: El fin del mundo bipolar redujo el apoyo financiero y militar a los movimientos guerrilleros de izquierda.
# 2: Las transiciones a la paz en Centroamérica se aceleraron con el final de la confrontación este-oeste.
# 3: El colapso del bloque soviético privó a los movimientos revolucionarios latinoamericanos de su principal respaldo geopolítico y doctrinario.
# 4: Washington perdió la justificación del "peligro comunista" para respaldar dictaduras militares en el hemisferio.
# 5: La diplomacia de las Naciones Unidas desempeñó un papel protagónico en la verificación de los acuerdos de paz centroamericanos.
# 6: El fin de la Guerra Fría abrió un espacio inédito para la competencia política electoral pacífica en toda la región.
# 7: El final de la Guerra Fría transformó las relaciones políticas en América Latina.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La caída del Muro de Berlín y el nuevo orden geopolítico",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 7)} El terremoto geopolítico que desmanteló el socialismo en Europa del Este repercutió de inmediato en cada rincón de América Latina."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 1)} Sin arsenales ni financiamiento del bloque del Este, las guerrillas centroamericanas y sudamericanas comprendieron la urgencia de buscar salidas políticas negociadas."
        },
        {
            "type": "narration",
            "text": f"Al mismo tiempo, {G(k, 4)} La defensa formal de los derechos humanos y las elecciones libres pasaron a ser la nueva norma diplomática internacional."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} Misiones de cascos azules supervisaron la desmovilización de combatientes y el desarme en Nicaragua, El Salvador y Guatemala."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} La izquierda revolucionaria debió reinventarse, abandonando la lucha armada en el campo para disputar democráticamente el poder en las urnas."
        }
    ]
}

# 33.02: finalguerrafria-02
k = "finalguerrafria-02"
# Grammar (8):
# 0: La invasión estadounidense de Panamá en diciembre de 1989 derrocó al general Manuel Antonio Noriega.
# 1: La operación militar "Causa Justa" causó cientos de víctimas civiles en el barrio de El Chorrillo.
# 2: La intervención demostró que Washington continuaba dispuesto a utilizar la fuerza militar unilateral en la región.
# 3: En la medianoche del 20 de diciembre de 1989, más de veintisiete mil soldados estadounidenses invadieron Panamá.
# 4: Los bombardeos sobre el cuartel central devastaron el populoso barrio de El Chorrillo, provocando un incendio incontrolable.
# 5: El general Noriega, antiguo colaborador de la CIA vinculado al narcotráfico, se refugió en la Nunciatura Apostólica antes de rendirse.
# 6: La invasión de Panamá constituyó la primera gran acción militar estadounidense tras la caída del Muro de Berlín.
# 7: La intervención en Panamá tuvo consecuencias importantes para la política de ese país.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La invasión a Panamá: la 'Operación Causa Justa' de 1989",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 6)} Ordenada por el presidente George H. W. Bush, la operación justificó la acción en la protección del Canal y la captura del dictador."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 1)} Cientos de panameños humildes perecieron en el fuego cruzado, mientras miles de familias quedaron en la indigencia absoluta."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Asediado con altavoces de música rock ensordecedora durante días, Noriega se entregó el 3 de enero de 1990 y fue trasladado a prisiones federales en Miami."
        },
        {
            "type": "narration",
            "text": f"Guillermo Endara juró como presidente en una base militar estadounidense. {G(k, 7)} Las Fuerzas de Defensa panameñas fueron disueltas definitivamente, desmilitarizando el país."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} La invasión desnudó que el fin de la rivalidad soviética no significaba el cese de las acciones de fuerza del Pentágono en su patio trasero."
        }
    ]
}

# 33.03: finalguerrafria-03
k = "finalguerrafria-03"
# Grammar (8):
# 0: Cuba sufrió una crisis económica devastadora tras la desaparición del comercio con la Unión Soviética.
# 1: El gobierno cubano decretó el "Período Especial en Tiempo de Paz" para racionar bienes esenciales.
# 2: La economía cubana se adaptó mediante la apertura al turismo internacional y la despenalización del dólar.
# 3: Entre 1989 y 1993, el producto interno bruto cubano se contrajo en un treinta y cinco por ciento tras el cese de los subsidios soviéticos.
# 4: La población cubana enfrentó apagones diarios de hasta dieciséis horas, escasez crítica de alimentos y falta absoluta de combustible.
# 5: La despenalización de la tenencia de divisas en 1993 y el auge de las inversiones turísticas extranjeras amortiguaron el colapso.
# 6: La "crisis de los balseros" de 1994 vio a más de treinta mil personas lanzarse al mar en precarias embarcaciones rumbo a Florida.
# 7: El Periodo Especial transformó la vida cotidiana y la economía en Cuba.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Cuba en el 'Período Especial': resistencia y reinvención",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} El corte abrupto de los suministros de petróleo, trigo y repuestos provocó un apagón casi total en la isla. {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 4)} Las bicicletas chinas sustituyeron al transporte automotor, mientras las plazas urbanas fueron convertidas en huertos organopónicos para alimentar a la población."
        },
        {
            "type": "narration",
            "text": f"Washington endureció el bloqueo económico mediante las leyes Torricelli (1992) y Helms-Burton (1996). En agosto de 1994, tras las protestas del 'Maleconazo' en La Habana, {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} Se autorizó el trabajo por cuenta propia ('paladares') y se crearon empresas mixtas con cadenas hoteleras europeas y canadienses en Varadero."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} A pesar de un costo social inmenso y una creciente dualidad monetaria, el régimen socialista cubano logró sobrevivir a la marea global anticomunista."
        }
    ]
}

# 33.04: finalguerrafria-04
k = "finalguerrafria-04"
# Grammar (8):
# 0: La política exterior estadounidense en América Latina reorientó sus prioridades hacia el libre comercio y la lucha contra el narcotráfico.
# 1: La "guerra contra las drogas" militarizó la cooperación en seguridad en los países andinos.
# 2: Las cumbres presidenciales hemisféricas promovieron la democracia representativa y la integración de mercados.
# 3: Con la desaparición de la amenaza soviética, la agenda de Washington giró hacia la apertura de mercados y el combate al crimen organizado.
# 4: La erradicación forzosa de cultivos de coca desató intensas protestas de las comunidades campesinas e indígenas en Bolivia y Perú.
# 5: La militarización antidroga generó graves denuncias de violaciones a los derechos humanos en las zonas de producción cocalera.
# 6: La Cumbre de las Américas de Miami en 1994 consagró el compromiso formal con la democracia y el libre comercio como pilares hemisféricos.
# 7: La lucha contra el narcotráfico se convirtió en un eje central de las relaciones entre Estados Unidos y la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La nueva agenda hemisférica: libre comercio, democracia y la guerra contra las drogas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 7)} En la Casa Blanca, la doctrina de seguridad nacional fue reemplazada por la doctrina del 'engagement' comercial."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} {G(k, 2)} Se firmó la Carta Democrática Interamericana para consagrar sanciones diplomáticas contra cualquier alteración del orden constitucional."
        },
        {
            "type": "narration",
            "text": f"En los Andes, la DEA y el Pentágono asumieron la conducción de la represión antinarcóticos. {G(k, 1)} {G(k, 4)} Los cocaleros del Chapare y el Huallaga organizaron sindicatos combativos para defender el arbusto sagrado andino."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} La fumigación aérea con glifosato destruyó cosechas lícitas de subsistencia y contaminó fuentes de agua comunitarias."
        },
        {
            "type": "narration",
            "text": "La guerra antidrogas demostró ser ineficaz para frenar el consumo masivo en el norte, pero dejó una estela de violencia y militarización institucional en las naciones productoras."
        }
    ]
}

# 33.05: finalguerrafria-05
k = "finalguerrafria-05"
# Grammar (8):
# 0: El fin de la Guerra Fría permitió desideologizar parcialmente los debates sobre el desarrollo en América Latina.
# 1: La izquierda latinoamericana debió repensar sus estrategias políticas y sus modelos doctrinarios.
# 2: La consolidación democrática avanzó sin la tutela constante de la confrontación entre superpotencias.
# 3: El Foro de São Paulo, fundado en 1990 por Lula da Silva y Fidel Castro, se convirtió en el espacio de debate clave de la izquierda regional.
# 4: La renuncia a la vía armada permitió a los partidos progresistas ganar elecciones municipales y nacionales en varios países.
# 5: La desaparición del corsé ideológico bipolar habilitó la experimentación con políticas sociales heterodoxas e innovadoras.
# 6: El balance del período confirmó que el destino de América Latina dependía más de sus dinámicas internas que de directivas foráneas.
# 7: El final de la Guerra Fría redefinió los debates políticos y económicos de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La reinvención de la izquierda y el Foro de São Paulo",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 7)} La muerte del dogmatismo estalinista abrió paso a una rica y pluralista reflexión en el pensamiento social del continente."
        },
        {
            "type": "narration",
            "text": f"En julio de 1990, más de cuarenta partidos y organizaciones populares se reunieron en Brasil. {G(k, 3)} {G(k, 1)} Se debatió cómo enfrentar el neoliberalismo sin renunciar a la soberanía popular y la justicia distributiva."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Partidos como el Frente Amplio en Uruguay, el PT en Brasil y el PRD en México conquistaron intendencias, gobernaciones y escaños parlamentarios."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} La participación ciudadana en presupuestos participativos y reformas de salud universal forjó una nueva cultura de gestión pública progresista."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Esta maduración cívica preparó el terreno para la 'marea rosa' de gobiernos progresistas que transformaría el mapa político continental a comienzos del nuevo siglo."
        }
    ]
}

# =============================================================================
# UNIT 34: latamnoventa
# =============================================================================

# 34.01: latamnoventa-01
k = "latamnoventa-01"
# Grammar (8):
# 0: La década de 1990 estuvo marcada por la aplicación generalizada de reformas de mercado en casi toda la región.
# 1: La apertura comercial y financiera transformó la economía de países como Argentina, México, Perú y Brasil.
# 2: Las políticas de estabilización lograron controlar las hiperinflaciones heredadas de la década anterior.
# 3: El Plan de Convertibilidad argentino de 1991 fijó por ley la paridad de un peso por un dólar estadounidense.
# 4: El Plan Real brasileño de 1994, diseñado por Fernando Henrique Cardoso, erradicó una inflación de cuatro dígitos anuales.
# 5: La eliminación de la hiperinflación devolvió la previsibilidad económica cotidiana y expandió masivamente el crédito al consumo.
# 6: La estabilidad de precios se convirtió en el principal activo político de los gobiernos reformistas de la época.
# 7: Las reformas económicas de los años noventa cambiaron la relación entre el Estado y el mercado.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Planes de estabilización: el 'Uno a Uno' y el 'Plan Real'",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 7)} {G(k, 1)} Ministros de hacienda tecnócratas formados en universidades estadounidenses asumieron las riendas del poder económico."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} En Argentina, el ministro Domingo Cavallo impulsó una terapia radical: {G(k, 3)} frenando de golpe la inflación que había devorado los salarios."
        },
        {
            "type": "narration",
            "text": f"En Brasil, {G(k, 4)} mediante la creación transitoria de la Unidad Real de Valor (URV) y una nueva moneda respaldada por reservas internacionales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Las familias pudieron comprar televisores, automóviles y electrodomésticos en cuotas fijas por primera vez en una generación. {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": "Sin embargo, el anclaje monetario sobrevaluado provocó un déficit comercial gigantesco y una peligrosa acumulación de deuda externa para sostener la paridad cambiaria."
        }
    ]
}

# 34.02: latamnoventa-02
k = "latamnoventa-02"
# Grammar (8):
# 0: El "Efecto Tequila" de 1994 en México desató la primera gran crisis financiera de la era de la globalización.
# 1: La devaluación abrupta del peso mexicano provocó la fuga masiva de capitales especulativos extranjeros.
# 2: Un paquete de rescate internacional de cincuenta mil millones de dólares evitó la quiebra financiera del país.
# 3: En diciembre de 1994, el recién asumido gobierno de Ernesto Zedillo devaluó el peso, desatando el 'error de diciembre'.
# 4: La fuga repentina de miles de millones de dólares en 'tesobonos' amenazó con provocar una moratoria financiera total.
# 5: La administración Clinton organizó un rescate financiero sin precedentes con fondos del FMI y del Tesoro estadounidense.
# 6: El colapso del sistema bancario mexicano requirió la creación del multimillonario rescate estatal del Fobaproa.
# 7: La crisis mexicana de 1994 tuvo un impacto inmediato en otros mercados emergentes.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El 'Efecto Tequila' de 1994: el choque de la globalización",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"El año 1994, que comenzó con el optimismo del TLCAN, culminó con una pesadilla financiera en México. {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"El asesinato del candidato oficialista Luis Donaldo Colosio y la insurrección en Chiapas ahuyentaron a los inversores. {G(k, 3)} {G(k, 1)} {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} El crédito impuso condiciones draconianas de tasas de interés al 100% que asfixiaron a las pequeñas empresas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} que absorbió las deudas privadas de los banqueros como deuda pública de todos los contribuyentes durante décadas."
        },
        {
            "type": "narration",
            "text": "El 'Efecto Tequila' demostró la extrema volatilidad de los flujos de capital golondrina en un mundo globalizado y desregulado."
        }
    ]
}

# 34.03: latamnoventa-03
k = "latamnoventa-03"
# Grammar (8):
# 0: El autogolpe de Alberto Fujimori en Perú en 1992 clausuró el Congreso con el respaldo militar.
# 1: El régimen fujimorista combinó políticas neoliberales radicales con prácticas autoritarias y corrupción.
# 2: La captura de Abimael Guzmán en septiembre de 1992 asestó un golpe decisivo a la organización Sendero Luminoso.
# 3: El 5 de abril de 1992, Alberto Fujimori disolvió el Congreso Nacional e intervino el poder judicial en un autogolpe televisado.
# 4: La derrota militar de Sendero Luminoso y la captura de su cúpula otorgaron una enorme popularidad al régimen fujimorista.
# 5: La red clandestina de sobornos y espionaje operada por Vladimiro Montesinos corrompió a jueces, congresistas y medios de prensa.
# 6: La difusión de los "Vladivideos" en el año 2000 provocó la caída del régimen y la fuga de Fujimori a Japón.
# 7: La década de 1990 en Perú estuvo marcada por la violencia, las reformas económicas y el autoritarismo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Perú en los noventa: Fujimori, el autogolpe y la caída de Montesinos",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 7)} Elegido en 1990 tras prometer no aplicar un shock económico, Alberto Fujimori impuso el 'Fujishock', privatizó empresas mineras y energéticas, y recortó subsidios. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"En el frente de seguridad, el GEIN de la Policía Nacional logró una hazaña de inteligencia: {G(k, 2)} en una casa de Lima sin disparar un solo tiro. {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"Bajo la fachada de orden y estabilidad, {G(k, 1)} {G(k, 5)} Desde las oficinas del Servicio de Inteligencia Nacional (SIN), Montesinos grabó cientos de videos pagando fajos de dólares a empresarios y periodistas."
        },
        {
            "type": "narration",
            "text": f"En septiembre del año 2000, {G(k, 6)} desde donde envió su renuncia por fax, antes de ser extraditado y condenado a 25 años de prisión por crímenes de lesa humanidad cometidos por el escuadrón Grupo Colina."
        },
        {
            "type": "narration",
            "text": "La experiencia peruana ilustró cómo la emergencia económica y el terrorismo fueron instrumentalizados para consolidar un régimen autoritario y corrupto."
        }
    ]
}

# 34.04: latamnoventa-04
k = "latamnoventa-04"
# Grammar (8):
# 0: Los movimientos de protesta social se multiplicaron en toda la región contra las consecuencias del modelo neoliberal.
# 1: El movimiento de los "piqueteros" en Argentina utilizó el corte de rutas para reclamar empleo y subsidios sociales.
# 2: Las organizaciones comunitarias y barriales crearon redes de solidaridad para enfrentar la desocupación.
# 3: Las privatizaciones de empresas públicas en localidades del interior argentino desataron los primeros cortes de ruta en Cutral Có y Tartagal.
# 4: El movimiento piquetero se convirtió en un actor político insoslayable con asambleas barriales y comedores comunitarios.
# 5: La Coordinadora del Agua en Cochabamba derrotó el intento de privatizar el agua potable en la histórica "Guerra del Agua" del año 2000.
# 6: Las protestas populares desnudaron el agotamiento social del modelo de libre mercado irrestricto.
# 7: La movilización social creció como respuesta a los problemas de empleo y pobreza.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La resistencia social: piqueteros, 'Guerra del Agua' y nuevas identidades de lucha",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Hacia finales de los años noventa, la aparente apatía social dio paso a una ola de indignación popular en pueblos y periferias urbanas. {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"En Argentina, {G(k, 3)} Petroleros y ferroviarios despedidos encendieron neumáticos en las carreteras. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 4)} El 'piquete y cacerola' unió a los desocupados de los suburbios con las clases medias empobrecidas por la confiscación bancaria del 'corralito'."
        },
        {
            "type": "narration",
            "text": f"En Bolivia, cuando el consorcio transnacional Bechtel elevó las tarifas de agua hasta en un 300%, la población de Cochabamba se sublevó. {G(k, 5)} expulsando a la multinacional y recuperando el control comunal del recurso."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Las calles recuperaron su protagonismo como espacio de soberanía ciudadana y resistencia frente a los dictados de los organismos financieros internacionales."
        }
    ]
}

# 34.05: latamnoventa-05
k = "latamnoventa-05"
# Grammar (8):
# 0: El colapso del modelo de convertibilidad en Argentina en diciembre de 2001 clausuró la era neoliberal de los noventa.
# 1: La consigna "¡Que se vayan todos!" expresó el repudio popular a la clase política tradicional.
# 2: La crisis argentina abrió paso a una nueva etapa política caracterizada por el retorno del Estado interventor.
# 3: Las jornadas del 19 y 20 de diciembre de 2001 culminaron con la renuncia de Fernando de la Rúa y una feroz represión en Plaza de Mayo.
# 4: Argentina declaró la mayor moratoria soberana de la historia financiera mundial por más de cien mil millones de dólares.
# 5: La devaluación del peso puso fin a una década de convertibilidad ficticia, sumiendo al cincuenta por ciento del país en la pobreza.
# 6: El estallido de 2001 en Argentina simbolizó el quiebre definitivo de las recetas del Consenso de Washington en Sudamérica.
# 7: La crisis de 2001 tuvo un impacto decisivo en la política argentina y regional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Diciembre de 2001 en Argentina: '¡Que se vayan todos!' y el fin de una era",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 7)} {G(k, 6)} El país que había sido presentado por el FMI como el alumno ejemplar del libre mercado se desintegró en una crisis total."
        },
        {
            "type": "narration",
            "text": f"El congelamiento de los depósitos bancarios mediante el 'corralito' desató cacerolazos multitudinarios y saqueos a supermercados. {G(k, 3)} con un saldo trágico de treinta y nueve muertos."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} En diez días se sucedieron cinco presidentes en la Casa Rosada. En el Congreso Nacional, {G(k, 4)} ante el aplauso de los legisladores."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Millones de personas acudieron a clubes de trueque para conseguir alimentos y ropa con bonos y cuasimonedas de emergencia."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} El cataclismo argentino sepultó la fe ciega en el libre mercado irrestricto y abrió las puertas a los gobiernos progresistas y populares de la década siguiente."
        }
    ]
}

# =============================================================================
# UNIT 35: legadosigloveinte
# =============================================================================

# 35.01: legadosigloveinte-01
k = "legadosigloveinte-01"
# Grammar (8):
# 0: La revolución boliviana de 1952 y la abolición del ejército en Costa Rica en 1948 mostraron caminos singulares de transformación social.
# 1: La abolición de las fuerzas armadas en Costa Rica permitió redirigir el gasto fiscal hacia la educación y la salud pública.
# 2: La Revolución boliviana nacionalizó las minas de estaño y concedió el voto universal a la mayoría indígena.
# 3: En 1948, el presidente costarricense José Figueres Ferrer derribó simbólicamente con un mazo un muro del Cuartel Bellavista, aboliendo el ejército.
# 4: Costa Rica consolidó una de las democracias más estables y con mayores índices de desarrollo humano de todo el continente.
# 5: La insurrección popular de abril de 1952 en La Paz, liderada por mineros y campesinos armados del MNR, destruyó al ejército oligárquico.
# 6: La reforma agraria boliviana de 1953 distribuyó millones de hectáreas y abolió el pongueaje servil en los campos andinos.
# 7: Las transformaciones de este periodo mostraron diferentes modelos de reforma social.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Caminos singulares: Costa Rica 1948 y la Revolución boliviana de 1952",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 7)} Lejos de ajustarse a un patrón uniforme, algunas naciones ensayaron fórmulas institucionales extraordinariamente originales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 1)} Al destinar los recursos de defensa a las aulas y los hospitales, {G(k, 4)} manteniéndose libre de golpes de Estado y dictaduras militares."
        },
        {
            "type": "narration",
            "text": f"Por su parte, en los Andes bolivianos estalló un cataclismo social. {G(k, 5)} {G(k, 2)} de las familias Patiño, Hochschild y Aramayo."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Los indígenas quechuas y aymaras dejaron de ser sirvientes sin derechos para convertirse en ciudadanos con plenos derechos civiles y políticos."
        },
        {
            "type": "narration",
            "text": "Tanto el pacifismo civil costarricense como el radicalismo agrario boliviano demostraron la audacia transformadora de las sociedades latinoamericanas en el siglo veinte."
        }
    ]
}

# 35.02: legadosigloveinte-02
k = "legadosigloveinte-02"
# Grammar (8):
# 0: Las reformas constitucionales del siglo veinte reflejaron las transformaciones políticas y sociales de cada época.
# 1: Las cartas magnas incorporaron derechos laborales, reforma agraria y soberanía sobre los recursos naturales.
# 2: El constitucionalismo social latinoamericano fue pionero en consagrar garantías colectivas por encima del individualismo liberal.
# 3: La Constitución mexicana de 1917 inauguró formalmente la era del constitucionalismo social en el derecho internacional.
# 4: Las cartas magnas de mitad de siglo consagraron el Estado de bienestar, los derechos sindicales y la función social de la propiedad.
# 5: Las constituciones de la transición democrática de finales de siglo incorporaron tratados internacionales de derechos humanos.
# 6: La constante tensión entre normas constitucionales avanzadas y su aplicación práctica efectiva caracterizó la historia jurídica regional.
# 7: El constitucionalismo reflejó los cambios políticos de la región a lo largo del siglo.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El constitucionalismo social: de Querétaro a las cartas democráticas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 7)} El texto fundamental de las naciones funcionó como el campo de batalla donde se plasmaron las conquistas populares."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 2)} {G(k, 1)} El Artículo 27 y el 123 mexicanos establecieron que el bien común primaba sobre el derecho irrestricto de propiedad privada."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} Cartas como la Constitución peronista de 1949 en Argentina y la guatemalteca de 1945 reconocieron los derechos del trabajador, la niñez y la ancianidad."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} con rango supraconstitucional, facilitando el juzgamiento de crímenes de lesa humanidad y la tutela de minorías."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Reducir la distancia entre la letra viva de la ley y la realidad social cotidiana continúa siendo la gran tarea inacabada de la democracia."
        }
    ]
}

# 35.03: legadosigloveinte-03
k = "legadosigloveinte-03"
# Grammar (8):
# 0: El programa Progresa en México en 1997 inauguró las transferencias monetarias condicionadas en América Latina.
# 1: Las transferencias condicionadas exigían asistencia escolar y controles médicos periódicos para las familias beneficiarias.
# 2: Estos programas redujeron la pobreza extrema pero no alteraron la estructura básica de la desigualdad social.
# 3: El programa Progresa, rebautizado posteriormente como Oportunidades y Prospera, atendió a millones de familias en pobreza extrema.
# 4: Programas similares como "Bolsa Família" en Brasil y "Asignación Universal por Hijo" en Argentina se expandieron por toda la región.
# 5: La entrega directa de subsidios a las madres de familia fortaleció su rol en la toma de decisiones del hogar.
# 6: Estos programas aliviaron la indigencia inmediata sin resolver los problemas de calidad en la educación y salud pública.
# 7: Se reconoció progresivamente que el desarrollo económico no garantizaba por sí solo una reducción de la desigualdad.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Las transferencias condicionadas: Progresa, Bolsa Família y la política social",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"A finales de los años noventa, frente a los límites evidentes del 'derrame' de mercado, {G(k, 7)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 1)} Madres en zonas rurales recibían un ingreso monetario mensual a cambio de asegurar que sus hijos asistieran a la escuela y completaran su cartilla de vacunación."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} En Brasil, 'Bolsa Família' bajo el gobierno de Lula sacó a más de treinta millones de personas de la miseria extrema y erradicó el hambre endémica en el Nordeste."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} {G(k, 6)} Escuelas precarias y hospitales saturados no lograban garantizar una verdadera movilidad social ascendente."
        },
        {
            "type": "narration",
            "text": "Las transferencias condicionadas constituyeron una red de seguridad indispensable ante la emergencia, pero evidenciaron que la justicia distributiva exige empleo formal de calidad e impuestos progresivos a las grandes riquezas."
        }
    ]
}

# 35.04: legadosigloveinte-04
k = "legadosigloveinte-04"
# Grammar (8):
# 0: Las sociedades han cambiado recordando el pasado mientras intentan construir nuevas formas de convivencia.
# 1: Los gobiernos impulsaron políticas de memoria buscando reconocer a las víctimas.
# 2: Las comunidades han debatido sobre el pasado intentando evitar que la violencia vuelva a repetirse.
# 3: Los movimientos sociales continuaron reclamando justicia mientras construían nuevas formas de identidad colectiva.
# 4: Tanto los gobiernos como la sociedad civil de varios países enfrentaron la misma pregunta difícil.
# 5: El libro fue leído tanto por historiadores como por el público general en los años siguientes.
# 6: Tanto el informe argentino como el brasileño llegaron de forma independiente a la misma fórmula.
# 7: Tanto "Nunca Más" como "Brasil: Nunca Mais" dejaron claro que la memoria histórica no dependería de una sola institución.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "Identidad, memoria colectiva y los informes del 'Nunca Más'",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Al clausurar las dictaduras militares, {G(k, 4)} ¿cómo procesar el trauma de la tortura y las desapariciones sin caer en la venganza ni en el olvido cobarde? {G(k, 0)} {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"En Argentina, la comisión presidida por Ernesto Sabato presentó en 1984 el estremecedor informe 'Nunca Más'. En Brasil, un equipo clandestino de abogados y religiosos liderado por Paulo Evaristo Arns y Jaime Wright compiló 'Brasil: Nunca Mais'. {G(k, 6)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 7)} Archivos, testimonios orales y placas conmemorativas en antiguas cárceles secretas se convirtieron en herramientas pedagógicas cívicas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 3)} Agrupaciones como H.I.J.O.S. en Argentina y colectivos de familiares en Chile llevaron a cabo 'escraches' pacíficos para mantener viva la memoria en el espacio público."
        },
        {
            "type": "narration",
            "text": "La construcción activa de la memoria histórica demostró ser el mejor antídoto cívico para asegurar que el terror estatal no vuelva a ensombrecer el destino del continente."
        }
    ]
}

# 35.05: legadosigloveinte-05
k = "legadosigloveinte-05"
# Grammar (8):
# 0: En resumidas cuentas, casos como el de Bolivia en 1952 y el de Costa Rica en 1948 demostraron que no existía una única fórmula para lograr un cambio duradero.
# 1: En resumidas cuentas, la reforma constitucional demostró ser una herramienta de doble filo a lo largo del siglo.
# 2: En resumidas cuentas, ni el crecimiento económico sostenido de algunos países ni programas pioneros como Progresa lograron, por sí solos, cerrar la brecha de desigualdad.
# 3: En resumidas cuentas, la región entró al nuevo milenio habiendo aprendido, a un costo enorme, muchas de las lecciones de su propio siglo XX.
# 4: A lo largo del siglo, la transformación política fue profunda, aunque no eliminó las desigualdades estructurales.
# 5: Como consecuencia de las distintas reformas, algunas instituciones adquirieron mayor estabilidad, pero persistieron problemas sociales.
# 6: El legado del siglo XX puede interpretarse desde perspectivas diferentes, según se prioricen los avances o los costes sociales.
# 7: Aunque la región experimentó cambios importantes, algunas cuestiones del pasado siguen condicionando el presente.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "¿Qué dejó el siglo XX?: balance de un siglo de luces y sombras",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Al hacer el balance del turbulento siglo veinte en América Latina, el panorama que emerge está repleto de contrastes dramáticos y grandezas históricas. {G(k, 6)} {G(k, 4)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 1)} Mientras algunas cartas magnas consagraron derechos de avanzada mundial, otras fueron redactadas por dictaduras para legalizar la exclusión."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} América Latina urbanizó a su población, alfabetizó a sus mayorías y levantó infraestructuras modernas, pero conservó una escandalosa concentración del ingreso en manos del 1% más rico."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} La dependencia de los precios internacionales de los bienes primarios, la debilidad fiscal de los Estados y la vulnerabilidad de las instituciones democráticas persistieron como asignaturas pendientes."
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} Con una ciudadanía más informada, organizada y celosa de sus derechos, América Latina se preparó para asumir con dignidad los desafíos inéditos del siglo veintiuno."
        }
    ]
}

# =============================================================================
# UNIT 36: americalatinadosmil
# =============================================================================

# 36.01: americalatinadosmil-01
k = "americalatinadosmil-01"
# Grammar (8):
# 0: La llegada de gobiernos de izquierda y centroizquierda a principios de los años 2000 fue conocida como la "marea rosa".
# 1: Hugo Chávez, Lula da Silva, Néstor Kirchner y Evo Morales lideraron procesos de cambio político en sus países.
# 2: Estos gobiernos priorizaron el gasto social, la soberanía sobre los recursos y la integración regional.
# 3: La elección de Hugo Chávez en Venezuela en 1998 inició un ciclo político inédito en América Latina.
# 4: La victoria de Lula en Brasil (2002), Kirchner en Argentina (2003) y Evo Morales en Bolivia (2005) consolidó la 'marea rosa'.
# 5: La nacionalización de hidrocarburos y la renegociación de contratos mineros aumentaron los ingresos fiscales del Estado.
# 6: Los programas de reducción de la pobreza lograron sacar a decenas de millones de personas de la indigencia en toda la región.
# 7: La nueva etapa política trajo cambios importantes en las prioridades de gobierno.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La 'Marea Rosa': el giro a la izquierda en América Latina",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 3)} {G(k, 0)} {G(k, 7)} Por primera vez en la historia, mandatarios de extracción obrera, campesina y militar nacionalista llegaron al poder por la vía pacífica de los comicios."
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} A ellos se sumaron Tabaré Vázquez y Pepe Mujica en Uruguay, Rafael Correa en Ecuador, Michelle Bachelet en Chile y Fernando Lugo en Paraguay. {G(k, 1)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} {G(k, 5)} Se recuperaron empresas públicas privatizadas en los noventa y se aumentaron los presupuestos de salud, educación y vivienda popular."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} El índice de Gini experimentó una mejora histórica en casi todos los países de América del Sur, ampliando la clase media y reduciendo el desempleo a mínimos históricos."
        },
        {
            "type": "narration",
            "text": "La 'marea rosa' refundó el orgullo latinoamericano y desafió el Consenso de Washington, inaugurando la década más próspera y soberana del continente contemporáneo."
        }
    ]
}

# 36.02: americalatinadosmil-02
k = "americalatinadosmil-02"
# Grammar (8):
# 0: El extraordinario crecimiento de la economía china impulsó la demanda global de materias primas latinoamericanas.
# 1: El aumento de los precios del petróleo, la soja, el cobre y el gas generó ingresos fiscales récord para los gobiernos de la región.
# 2: El auge exportador financió programas sociales masivos y grandes inversiones en infraestructura pública.
# 3: El vertiginoso ascenso industrial de China convirtió a Beijing en el principal socio comercial de varios países sudamericanos.
# 4: El precio del barril de petróleo superó los cien dólares, mientras la tonelada de soja y el cobre alcanzaban máximos históricos.
# 5: La fabulosa renta extraordinaria de las materias primas permitió acumular reservas internacionales y cancelar deudas con el FMI.
# 6: La bonanza económica alimentó un debate profundo sobre los riesgos de una nueva "reprimarización" extractivista de las economías.
# 7: El auge de los productos básicos transformó las cuentas públicas de varios países.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El 'Superciclo' de las materias primas y la irrupción de China",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"Entre 2003 y 2014, América Latina vivió un periodo de bonanza macroeconómica sin igual. {G(k, 0)} {G(k, 3)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} {G(k, 1)} {G(k, 7)} Brasil, Argentina, Chile, Perú, Venezuela, Bolivia y Ecuador registraron superávits gemelos en sus balanzas comerciales y fiscales."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} Argentina y Brasil cancelaron en un solo pago la totalidad de sus deudas con el FMI, desprendiéndose de las auditorías condicionadas de Washington. {G(k, 2)}"
        },
        {
            "type": "narration",
            "text": f"Sin embargo, ecologistas y economistas encendieron alarmas tempranas. {G(k, 6)} La expansión desmedida de la frontera sojera, la megaminería a cielo abierto y las petroleras amenazaron cuencas hídricas y territorios comunitarios."
        },
        {
            "type": "narration",
            "text": "El superciclo demostró que la bonanza financiera era una bendición para combatir la pobreza inmediata, pero no resolvía por sí sola la necesidad urgente de industrialización y diversificación científica y tecnológica."
        }
    ]
}

# 36.03: americalatinadosmil-03
k = "americalatinadosmil-03"
# Grammar (8):
# 0: Los movimientos feministas han protagonizado multitudinarias movilizaciones por los derechos reproductivos y contra la violencia de género.
# 1: La consigna "Ni Una Menos" nacida en Argentina en 2015 se extendió por todo el continente.
# 2: La "marea verde" logró la legalización del aborto en países como Argentina, México y Colombia.
# 3: El 3 de junio de 2015, cientos de miles de mujeres ocuparon las calles de Buenos Aires bajo la consigna "Ni Una Menos".
# 4: La lucha contra los femicidios y el machismo estructural se convirtió en el movimiento de masas más dinámico de la región.
# 5: La 'marea verde' con pañuelos verdes inundó las plazas de América Latina exigiendo aborto legal, seguro y gratuito.
# 6: La conquista de leyes de paridad de género y matrimonio igualitario transformó la legislación civil en varios países.
# 7: Los movimientos sociales contemporáneos han transformado la agenda política regional.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "La 'Marea Verde' y la revolución feminista latinoamericana",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En la segunda década del siglo veintiuno, una formidable rebelión cultural y social transformó las conciencias en todo el continente. {G(k, 0)} {G(k, 7)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 3)} tras el brutal crimen de la adolescente Chiara Páez. {G(k, 1)} {G(k, 4)} convirtiendo el fin de la impunidad machista en un clamor continental."
        },
        {
            "type": "narration",
            "text": f"{G(k, 5)} {G(k, 2)} En diciembre de 2020 el Congreso argentino aprobó la ley de Interrupción Voluntaria del Embarazo (IVE), seguida de fallos históricos de la Suprema Corte en México (2021) y la Corte Constitucional en Colombia (2022)."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Colectivos de mujeres indígenas y afrodescendientes visibilizaron el feminismo comunitario y la defensa de los territorios frente al extractivismo."
        },
        {
            "type": "narration",
            "text": "El movimiento feminista demostró una capacidad inigualable para interpelar a las nuevas generaciones, situando la igualdad de género, el cuidado y la diversidad en el corazón de la política futura."
        }
    ]
}

# 36.04: americalatinadosmil-04
k = "americalatinadosmil-04"
# Grammar (8):
# 0: El estallido social de octubre de 2019 en Chile evidenció el agotamiento del modelo socioeconómico heredado.
# 1: Las protestas masivas en las calles de Santiago condujeron a la apertura de un proceso constituyente.
# 2: Movilizaciones similares en Colombia y Ecuador expresaron la indignación ciudadana contra la desigualdad y la precariedad.
# 3: El 18 de octubre de 2019, la evasión masiva del metro por estudiantes secundarios desató el 'estallido social' en Chile.
# 4: Más de un millón doscientas mil personas marcharon en Plaza Italia (Plaza Dignidad) bajo la consigna 'No son 30 pesos, son 30 años'.
# 5: El acuerdo por la paz social abrió la convocatoria histórica para redactar una nueva constitución que sustituyera a la de 1980.
# 6: El 'Paro Nacional' de 2021 en Colombia canalizó la protesta juvenil contra reformas tributarias y la violencia policial.
# 7: Las protestas ciudadanas mostraron la persistencia del descontento social en varias democracias de la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "El Estallido Social de 2019 en Chile y las rebeliones ciudadanas",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"En octubre de 2019, una chispa aparentemente menor desató un terremoto político en el país considerado el modelo de estabilidad regional. {G(k, 3)} {G(k, 0)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 4)} La ciudadanía denunció el sistema privatizado de pensiones (AFP), el endeudamiento universitario y la salud segregada. {G(k, 1)} {G(k, 5)}"
        },
        {
            "type": "narration",
            "text": f"{G(k, 2)} En Ecuador, el levantamiento indígena de octubre de 2019 frenó el 'paquetazo' del FMI. En Colombia, {G(k, 6)} abriendo paso a la histórica victoria electoral de Gustavo Petro y Francia Márquez en 2022."
        },
        {
            "type": "narration",
            "text": f"{G(k, 7)} A pesar de la dura represión policial y las heridas oculares causadas por perdigones, la juventud demostró que no estaba dispuesta a aceptar la resignación frente a la precariedad."
        },
        {
            "type": "narration",
            "text": "Estas rebeliones populares confirmaron que la estabilidad democrática requiere no solo el funcionamiento formal de las instituciones, sino una distribución equitativa de la dignidad humana y el bienestar social."
        }
    ]
}

# 36.05: americalatinadosmil-05
k = "americalatinadosmil-05"
# Grammar (8):
# 0: América Latina enfrenta en el siglo veintiuno el desafío de superar la desigualdad, el cambio climático y la polarización política.
# 1: La transición energética justa y la protección de la Amazonía son prioridades globales y regionales ineludibles.
# 2: La integración regional y el fortalecimiento democrático siguen siendo indispensables para el futuro del continente.
# 3: La Amazonía, pulmón planetario compartido por nueve países, enfrenta amenazas críticas de deforestación y minería ilegal.
# 4: La transición hacia energías renovables exige proteger la soberanía sobre minerales estratégicos como el litio y el cobre.
# 5: La polarización política extrema y el uso de noticias falsas en redes sociales amenazan la convivencia democrática.
# 6: América Latina conserva un potencial extraordinario en biodiversidad, creatividad cultural y vocación de paz para el siglo veintiuno.
# 7: Los desafíos del presente exigen nuevas respuestas políticas y sociales en toda la región.
STORIES[reqs[k]['st_file']] = {
    "id": reqs[k]['st_id'],
    "title": "América Latina en el siglo XXI: desafíos ecológicos, democracia y esperanza",
    "paragraphs": [
        {
            "type": "narration",
            "text": f"{G(k, 0)} {G(k, 7)} Tras doscientos años de vida republicana independiente, las naciones latinoamericanas se sitúan ante encrucijadas históricas decisivas."
        },
        {
            "type": "narration",
            "text": f"{G(k, 1)} {G(k, 3)} Gobiernos amazónicos articulan planes conjuntos para frenar el punto de no retorno de la selva tropical y reconocer las reservas indígenas como barrera de conservación ambiental."
        },
        {
            "type": "narration",
            "text": f"En el 'Triángulo del Litio' entre Bolivia, Argentina y Chile, que concentra más de la mitad de las reservas mundiales del mineral blanco, {G(k, 4)} evitando repetir los despojos coloniales del salitre o la plata del pasado."
        },
        {
            "type": "narration",
            "text": f"En el plano político, {G(k, 5)} {G(k, 2)} superando el odio partidario para construir consensos republicanos duraderos y transparentes."
        },
        {
            "type": "narration",
            "text": f"{G(k, 6)} Dueña de una herencia milenaria, una juventud apasionada y una indeclinable sed de justicia, América Latina avanza con esperanza hacia un porvenir soberano, plural y fraterno."
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
