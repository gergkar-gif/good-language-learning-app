#!/usr/bin/env python3
import json
import os

DIR = 'content/es/stories/world/b1'

STORIES = {
    # =========================================================================
    # UNIT 31: movimientosindigenas
    # =========================================================================
    'b1-movimientosindigenas-01-pueblosindigenas.json': [
        'América Latina llegó a albergar a más de cuarenta millones de personas indígenas.',
        'Estos pueblos no formaban un grupo homogéneo, sino un mosaico de rica diversidad cultural.',
        'El grupo más numeroso habitaba la vasta región del altiplano andino.',
        'Cada comunidad sentía pertenecer a una tierra ancestral con derechos históricos sagrados.',
        'El estado colonial tardó siglos en conceder un estatus diferenciado a sus habitantes originarios.'
    ],
    'b1-movimientosindigenas-02-tierraderechos.json': [
        'En 1989, la OIT decidió redactar el histórico Convenio 169 sobre pueblos indígenas.',
        'Los estados comenzaron a ratificar este pacto como una herramienta legal de defensa.',
        'La ley exigía una consulta previa antes de tocar cualquier territorio ancestral.',
        'Las comunidades del resguardo indígena protegieron sus bosques del codiciado avance maderero.',
        'La demanda de autogobierno territorial transformó para siempre la relación con el poder central.'
    ],
    'b1-movimientosindigenas-03-identidadyreconocimiento.json': [
        'Las nuevas constituciones comenzaron a definir a la nación como un espacio multiétnico.',
        'Se reconoció el carácter pluricultural de la sociedad frente a siglos de discriminación.',
        'Los activistas supieron coincidir en que el respeto cultural era un principio rector.',
        'Este reclamo estaba sustentado en la resistencia histórica y el orgullo cotidiano del pueblo.',
        'Reconocer la diversidad obligó a redefinir la identidad nacional en todo el continente.'
    ],
    'b1-movimientosindigenas-04-movilizacionpolitica.json': [
        'En Ecuador, un masivo levantamiento indígena logró paralizar carreteras y ciudades en 1990.',
        'La protesta popular ayudó a contribuir a la posterior caída de presidentes autoritarios.',
        'En Bolivia, el dirigente cocalero Evo Morales organizó a los sindicatos del campo.',
        'Una población antes marginal decidió unirse para exigir representación política real en las urnas.',
        'En 2005, el movimiento indígena conquistó la mayoría absoluta y alcanzó la presidencia boliviana.'
    ],
    'b1-movimientosindigenas-05-nuevasvoces.json': [
        'Líderes campesinos ganaron elecciones locales y llegaron a gobernar como alcalde provincial.',
        'Los movimientos desarrollaron un sofisticado discurso político para defender su territorio ancestral.',
        'Muchas comunidades solían carecer de servicios básicos en medio de una amplia brecha social.',
        'Los pueblos rechazaron cada megaproyecto hidroeléctrico que amenazaba sus ríos y selvas sagradas.',
        'En este nuevo marco, los derechos indígenas establecieron una agenda para un cambio duradero.'
    ],
    'b1-movimientosindigenas.json': [
        'A finales del siglo veinte, los pueblos indígenas emergieron como poderosos actores políticos.',
        'En los Andes y la Amazonía, las comunidades campesinas desafiaron siglos de silencio y racismo.',
        'Los levantamientos populares paralizaron países enteros y tumbaron gobiernos desconectados del pueblo.',
        'Nuevas cartas magnas reconocieron el carácter plurinacional y los derechos colectivos territoriales.',
        'La llegada de Evo Morales al poder coronó décadas de resistencia y dignidad originaria.'
    ],

    # =========================================================================
    # UNIT 32: integracionregional
    # =========================================================================
    'b1-integracionregional-01-porqueintegrarse.json': [
        'Simón Bolívar solía soñar con una confederación de repúblicas hispanoamericanas unidas.',
        'Aquel gran anhelo de unidad no logró concretarse debido a rivalidades locales tempranas.',
        'Durante décadas, el proteccionismo aduanero y la lentitud comercial dividieron a las naciones vecinas.',
        'Con la crisis de la deuda volvió a surgir la necesidad de integración.',
        'La apertura económica dio un nuevo impulso a la creación de un mercado común.'
    ],
    'b1-integracionregional-02-mercosur.json': [
        'En marzo de 1991, cuatro presidentes decidieron firmar el Tratado de Asunción.',
        'El bloque acordó eliminar aranceles aduaneros y coordinar políticas comerciales conjuntas.',
        'Argentina y Brasil aportaron el mayor peso económico a la membresía del nuevo Mercosur.',
        'Nuevos países vecinos comenzaron a incorporarse como asociados para repartir beneficios comerciales.',
        'Sin embargo, el incumplimiento recurrente de pactos bilaterales generó constantes fricciones internas.'
    ],
    'b1-integracionregional-03-comunidadandina.json': [
        'El Pacto Andino fue un antiguo acuerdo subregional fundado en 1969 en Cartagena.',
        'El proyecto estaba inspirado en el modelo de integración de la Comunidad Europea.',
        'La alianza decidió reorganizarse en los años noventa para buscar un rumbo más dinámico.',
        'El bloque andino logró dotarse de instituciones políticas como un parlamento y tribunal propio.',
        'Algunos socios solían alegar tensiones internas, pero el núcleo comercial logró sobrevivir.'
    ],
    'b1-integracionregional-04-comercioycooperacion.json': [
        'El auge del comercio exterior obligó a profundizar la cooperación entre las economías vecinas.',
        'El intercambio de manufactura industrial creció rápidamente entre las principales fábricas del continente.',
        'Sin embargo, el pequeño agricultor no podía competir contra el grano subsidiado norteamericano.',
        'El acuerdo trilateral norteamericano demostró la dificultad de lograr un esquema coherente para todos.',
        'La proliferación de tratados generó un mapa superpuesto de regulaciones aduaneras confusas.'
    ],
    'b1-integracionregional-05-unaregionunida.json': [
        'Construir una región unida requería contar con una voluntad política sólida y compartida.',
        'Era necesario vincular carreteras, puertos y vías de energía bajo un mecanismo moderno de cooperación.',
        'No convenía subestimar las profundas asimetrías económicas entre las pequeñas y grandes naciones.',
        'Las instituciones lograron sobrevivir a crisis recurrentes gracias a un denso tejido diplomático.',
        'Los gobiernos crearon un paraguas institucional más amplio para resolver conflictos en paz.'
    ],
    'b1-integracionregional.json': [
        'La integración regional renació en América Latina tras el final de la Guerra Fría.',
        'La creación del Mercosur en 1991 unió los mercados de Argentina, Brasil, Uruguay y Paraguay.',
        'La Comunidad Andina modernizó sus instituciones para facilitar el libre tránsito de mercancías y personas.',
        'Pese al avance comercial, las crisis financieras y disputas bilaterales frenaron la unión monetaria.',
        'La integración demostró ser indispensable para negociar en bloque ante los gigantes económicos mundiales.'
    ],

    # =========================================================================
    # UNIT 33: finalguerrafria
    # =========================================================================
    'b1-finalguerrafria-01-1989.json': [
        'En 1989, los berlineses salieron con picos a derribar el Muro de Berlín.',
        'En una célebre cumbre diplomática, Washington y Moscú anunciaron conjuntamente el fin de las tensiones.',
        'El orden bipolar que parecía inamovible colapsó ante el asombro del mundo entero.',
        'América Latina dejó de ser el escenario de sangrienta confrontación entre potencias nucleares.',
        'La caída soviética obligó a cada potencia militar a replantear sus doctrinas de seguridad.'
    ],
    'b1-finalguerrafria-02-unnuevomundo.json': [
        'Gorbachov tuvo que renunciar a su cargo como líder de la Unión Soviética en 1991.',
        'El colapso del mundo bipolar consagró el triunfo de la democracia liberal occidental.',
        'El modelo comunista dejó de verse como una alternativa viable para el continente americano.',
        'Las dictaduras militares tuvieron que ceder el mando ante una presión internacional sumamente intensa.',
        'La región inició un nuevo ensayo democrático buscando estabilidad institucional y apertura económica.'
    ],
    'b1-finalguerrafria-03-nuevasprioridades.json': [
        'La Casa Blanca ya no necesitaba contener la expansión del comunismo en la región.',
        'La lucha contra el narcotráfico se convirtió en el eje de la agenda de seguridad.',
        'Washington decidió lanzar una agresiva iniciativa antidrogas de escala hemisférica.',
        'La política exterior dio un giro profundo hacia la cooperación policial transnacional.',
        'Los cuarteles militares comenzaron a coordinarse con agentes antidrogas foráneos en las fronteras.'
    ],
    'b1-finalguerrafria-04-americalatinadespuesdelaguerrafria.json': [
        'En Cuba, el Producto Interno Bruto comenzó a contraerse más de un tercio tras 1991.',
        'La pérdida de subsidios soviéticos desató una severa escasez de combustible y alimentos básicos.',
        'La población sufría un constante apagón en medio del rápido deterioro del nivel de vida.',
        'La desesperación popular llegó a desembocar en la célebre crisis de los balseros en 1994.',
        'Miles de cubanos decidieron abandonar la isla en un bote improvisado o precaria embarcación.'
    ],
    'b1-finalguerrafria-05-haciaanosnoventa.json': [
        'La disolución de la Unión Soviética cambió radicalmente el panorama geopolítico regional.',
        'Sin el patrocinio extranjero, muchos antiguos aliados tuvieron que pactar el fin del conflicto.',
        'La región vivió un doloroso proceso de desarme militar en función de acuerdos negociados.',
        'Este cambio silencioso y profundo permitió consolidar instituciones civiles en casi todos los países.',
        'América Latina cerró el ciclo de la Guerra Fría para entrar en una nueva era.'
    ],
    'b1-finalguerrafria.json': [
        'La caída del Muro de Berlín en 1989 puso un punto final a la Guerra Fría.',
        'América Latina dejó de ser el campo de batalla de intereses geopolíticos entre superpotencias extranjeras.',
        'En Centroamérica, guerrillas y ejércitos firmaron la paz tras décadas de masacres y destrucción mutua.',
        'Cuba perdió los subsidios soviéticos y enfrentó la durísima crisis del Período Especial.',
        'El fin del conflicto bipolar abrió el camino hacia la integración regional y la economía global.'
    ],

    # =========================================================================
    # UNIT 34: latamnoventa
    # =========================================================================
    'b1-latamnoventa-01-losanosdemenem.json': [
        'Carlos Menem llegó a la presidencia de Argentina prometiendo una revolución productiva para el pueblo.',
        'El gobierno selló un pacto con los grandes grupos económicos para acelerar la venta de empresas estatales.',
        'La prensa comenzó a bautizar el modelo económico con el nombre de plan de convertibilidad.',
        'Para cada seguidor frenó la inflación, pero cada detractor denunciaba una excesiva concentración de riqueza.',
        'Escándalos por presunto lavado de dinero y tráfico de armas marcaron los últimos años del gobierno.'
    ],
    'b1-latamnoventa-02-fujimoriyperu.json': [
        'En 1990, un desconocido ingeniero agrónomo llamado Alberto Fujimori decidió postularse a la presidencia peruana.',
        'Contra todo pronóstico, Fujimori logró derrotar en las urnas al célebre escritor Mario Vargas Llosa.',
        'Tras investir su mandato, el grupo terrorista Sendero Luminoso intentó sembrar el pánico en Lima.',
        'En abril de 1992, con el respaldo militar, Fujimori decidió disolver el congreso nacional.',
        'El mandatario actuó como comandante autoritario e impuso un régimen de mano dura sin contrapesos.'
    ],
    'b1-latamnoventa-03-mexicoyeltlcan.json': [
        'El 1 de enero de 1994, el tratado del TLCAN logró entrar en vigor comercial.',
        'Ese mismo día, el subcomandante Marcos salió a encabezar el levantamiento armado en Chiapas.',
        'El asesinato del candidato Colosio en plena carrera electoral llegó a conmocionar al país entero.',
        'A finales de año, las reservas comenzaron a agotarse y el gobierno tuvo que devaluar el peso.',
        'Una masiva fuga de capitales obligó a Washington a coordinar un rescate financiero de emergencia.'
    ],
    'b1-latamnoventa-04-democraciaymercado.json': [
        'Millones de electores acudían a la urna para elegir presidentes con amplias facultades de mando.',
        'Los nuevos mandatarios promovieron una acelerada apertura económica sin consultar a las instituciones civiles.',
        'En Brasil, un escándalo que involucró al tesorero de campaña terminó con Fernando Collor de Mello.',
        'El congreso decidió iniciar un juicio político para destituir al mandatario por corrupción comprobada.',
        'Los analistas salieron a señalar la urgencia de fortalecer cada contrapeso democrático institucional.'
    ],
    'b1-latamnoventa-05-unadecadadecontrastes.json': [
        'Durante los noventa, la región tuvo que atravesar profundas transformaciones sociales y políticas.',
        'Las reformas promovidas por cada organismo financiero internacional prometían generar un crecimiento sostenido.',
        'La privatización logró beneficiar a sectores empresariales, pero el ingreso de los trabajadores disminuyó fuertemente.',
        'La brecha de desigualdad y exclusión social comenzó a sacudir la estabilidad de las ciudades.',
        'La década terminó mostrando que la promesa del mercado libre no alcanzó a las mayorías.'
    ],
    'b1-latamnoventa.json': [
        'La década de 1990 transformó a América Latina bajo el influjo del libre mercado.',
        'Líderes como Menem en Argentina y Fujimori en Perú aplicaron privatizaciones masivas y reformas de choque.',
        'México selló el tratado del TLCAN mientras el zapatismo se levantaba en armas desde Chiapas.',
        'La estabilidad monetaria frenó la hiperinflación pero generó un fuerte aumento de desempleo e informalidad.',
        'Hacia el año 2000, las crisis financieras y el descontento social anunciaban nuevos vientos políticos.'
    ],

    # =========================================================================
    # UNIT 35: legadosigloveinte
    # =========================================================================
    'b1-legadosigloveinte-01-revolucionyreforma.json': [
        'En 1910, la Revolución Mexicana logró derrocar la larga dictadura del general Porfirio Díaz.',
        'El nuevo orden decidió decretar una profunda reforma agraria para devolver tierras a campesinos.',
        'En Costa Rica, se acordó la abolición del ejército tras un disputado conflicto armado en 1948.',
        'La conquista del sufragio universal femenino transformó la participación ciudadana en las urnas.',
        'Estas reformas permitieron anular viejos privilegios y construir un progreso cívico duradero.'
    ],
    'b1-legadosigloveinte-02-dictaduraydemocracia.json': [
        'El siglo veinte presenció un inédito enfrentamiento entre la bota militar y las urnas.',
        'Tras décadas de tiranía, la sociedad civil logró recuperar cada derecho y libertad civil arrebatada.',
        'Los congresos volvieron a promulgar leyes constitucionales para defender al individuo y su colectivo social.',
        'Se reconoció el carácter pluricultural del estado y se otorgó título de propiedad comunal indígena.',
        'La democracia diseñó cada mecanismo concreto para evitar el retorno de la violencia castrense.'
    ],
    'b1-legadosigloveinte-03-desigualdadydesarrollo.json': [
        'A finales de siglo, los gobiernos crearon programas de transferencia monetaria para familias pobres.',
        'La ayuda solía condicionar la entrega del dinero a que los hijos asistan a la escuela.',
        'Los hogares de escasos recursos debían cumplir con un riguroso control médico periódico.',
        'El objetivo central consistía en invertir en capital humano para romper el ciclo del atraso.',
        'Los primeros resultados mostraron un alentador descenso de la desnutrición infantil en las comunidades.'
    ],
    'b1-legadosigloveinte-04-identidadymemoria.json': [
        'Durante los años oscuros, las iglesias tuvieron que enfrentar la feroz persecución dictatorial militar.',
        'En Chile, el cardenal Raúl Silva Henríquez fundó la célebre Vicaría de la Solidaridad.',
        'El titular eclesiástico decidió encargar a un equipo legal la defensa de presos políticos perseguidos.',
        'Los abogados lograron armar un detallado expediente de cada centro clandestino de tortura militar.',
        'Aquel archivo permitió transmitir la verdad y castigar a los culpables de crímenes atroces.'
    ],
    'b1-legadosigloveinte-05-quedejoelsigloxx.json': [
        'América Latina debió cargar con una compleja herencia política al despedir el siglo veinte.',
        'La modernización resultó ser un arma de doble filo que transformó ciudades pero aumentó contrastes.',
        'La región no logró arrancar de raíz la desigualdad que solía perpetuarse de padres a hijos.',
        'Una alarmante brecha social continuó dividiendo a ricos y desposeídos en todo el continente.',
        'El continente entraba al siglo veintiuno debiendo arrastrar una enorme agenda social pendiente.'
    ],
    'b1-legadosigloveinte.json': [
        'El siglo veinte fue una era de profundas revoluciones, dictaduras y renacer democrático.',
        'Las movilizaciones campesinas y obreras conquistaron derechos laborales y el voto universal definitivo.',
        'El terrorismo de estado dejó heridas abiertas que la memoria y la justicia intentaron sanar.',
        'La urbanización acelerada transformó las capitales pero dejó sin resolver la desigualdad histórica.',
        'Al cruzar el milenio, América Latina reivindicaba su identidad soberana con esperanza renovada.'
    ],

    # =========================================================================
    # UNIT 36: americalatinadosmil
    # =========================================================================
    'b1-americalatinadosmil-01-unaregiontransformada.json': [
        'En Caracas, un excoronel que lideró un fallido golpe militar en 1992 ganó las elecciones.',
        'Hugo Chávez capitalizó el rechazo generalizado hacia un sistema político bipartidista totalmente desgastado.',
        'El nuevo mandatario impulsó la convocatoria a una constituyente para cambiar las bases del estado.',
        'A través de un referéndum popular, la ciudadanía aprobó una nueva carta magna bolivariana.',
        'Aquel triunfo electoral marcó un giro histórico y cambió el rumbo político del continente sudamericano.'
    ],
    'b1-americalatinadosmil-02-politica.json': [
        'En 2001, la quiebra financiera de Argentina logró desatar una conmoción social y política inédita.',
        'Miles de manifestantes rodearon el congreso forzando la sustitución de cinco presidentes en diez días.',
        'En Ecuador y Bolivia, protestas populares obligaron a asumir el mando al vicepresidente de turno.',
        'Incluso oficiales de rango medio comenzaron a simpatizar con las demandas de los movimientos sociales.',
        'A pesar del caos, la democracia logró estabilizarse y consolidarse a través del voto ciudadano.'
    ],
    'b1-americalatinadosmil-03-economiayglobalizacion.json': [
        'La salida masiva de cada emigrante hacia el extranjero transformó la economía de familias enteras.',
        'El envío regular de cada remesa familiar comenzó a multiplicarse a un ritmo sin precedentes.',
        'Para millones de hogares, ese dinero fue un verdadero salvavidas frente a la pobreza cotidiana.',
        'Las remesas llegaron a superar a la exportación tradicional como principal fuente de divisas nacionales.',
        'Los pueblos de Centroamérica y el Caribe pudieron evitar quedarse atrás en la economía globalizada.'
    ],
    'b1-americalatinadosmil-04-sociedadeidentidad.json': [
        'Al comenzar el siglo veintiuno, la población urbana llegó a rondar el ochenta por ciento continental.',
        'El éxodo agrario del campo despobló comunidades y aceleró el crecimiento urbano descontrolado.',
        'En cada periferia capitalina creció un poblado marginal o un precario asentamiento sin agua potable.',
        'La falta de vivienda digna se convirtió en un problema social extendido por casi toda la región.',
        'Casi ninguna ciudad representaba una excepción ante la creciente demanda de mejores servicios urbanos.'
    ],
    'b1-americalatinadosmil-05-americalatinaalentrarenelnuevosiglo.json': [
        'El 31 de diciembre de 1999, Washington debió transferir el Canal de Panamá a soberanía panameña.',
        'Aquel histórico traspaso de control territorial se completó en pleno festejo y sin ningún contratiempo.',
        'Atrás quedaba el siglo veinte estrechamente ligado a intervenciones militares y dictaduras castrenses.',
        'Los presidentes acordaron pactar un orden de cooperación y respeto al derecho internacional soberano.',
        'Un renovado optimismo democrático comenzó a recorrer cada rincón de América Latina hacia el nuevo milenio.'
    ],
    'b1-americalatinadosmil.json': [
        'El cambio de milenio inauguró un ciclo de intensas transformaciones sociales en toda América Latina.',
        'El traspaso pacífico del Canal a Panamá simbolizó el fin de la era imperial en el continente.',
        'La llegada de líderes de izquierda al poder canalizó el descontento contra las políticas neoliberales.',
        'Las remesas de migrantes y el auge del precio de materias primas impulsaron la economía.',
        'Con voz propia, la región encaraba el siglo veintiuno con confianza en su propio destino democrático.'
    ]
}

def update_stories():
    updated = 0
    for filename, paragraph_texts in STORIES.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f'File not found: {filepath}')
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        new_paragraphs = [{'type': 'narration', 'text': text} for text in paragraph_texts]
        data['paragraphs'] = new_paragraphs

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        updated += 1
        print(f'Updated: {filename} ({len(new_paragraphs)} paragraphs)')

    print(f"\nTotal Block 6 stories successfully re-authored: {updated}/36")

if __name__ == '__main__':
    update_stories()
