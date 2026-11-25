from lib import *
U='b2-boliviaoriente'; V='b2-bolivia-lowlands-vocab'
def S(n): return f'{U}-{n}'
# ---------- 01 ser-passive
s=S('01')
vocab(s,[('la misión','mission (a settlement founded by missionaries)','noun'),('el jesuita','Jesuit','noun'),('el templo','church, temple','noun'),('la partitura','musical score','noun'),('expulsar','to expel','verb')],'The Jesuit missions of Chiquitos')
grammar(s,'Ser + Participle: Who Built and Who Was Expelled',[
 {'type':'text','title':'What you already know','content':"You know the passive with *ser* + past participle from B1 Unit 18: *La ley fue aprobada por el Parlamento*. The participle agrees with the subject, and *por* names who did the action. It fits a story about the past, where you want to put the thing that was done first: the churches, the scores, the missionaries."},
 {'type':'table','title':'Passive sentences about the missions','rows':[
  ['Las misiones fueron fundadas por jesuitas.','The missions were founded by Jesuits. (feminine plural: *fundadas*)'],
  ['Los jesuitas fueron expulsados en 1767.','The Jesuits were expelled in 1767. (masculine plural: *expulsados*)'],
  ['La iglesia fue restaurada en el siglo XX.','The church was restored in the twentieth century. (feminine singular: *restaurada*)'],
  ['Seis misiones fueron declaradas Patrimonio de la Humanidad en 1990.','Six missions were declared World Heritage Sites in 1990.']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Los templos fueron construidos con madera de la región.','english':'The churches were built with wood from the region.'},
  {'spanish':'Las partituras fueron encontradas en los archivos de las misiones.','english':'The scores were found in the archives of the missions.'},
  {'spanish':'La música barroca es tocada hoy por orquestas locales.','english':'Baroque music is played today by local orchestras.'}]},
 {'type':'tip','content':"Check the ending of the participle: it matches the subject, not the doer. *Los templos fueron construidos por los indígenas y los misioneros*: *construidos* agrees with *los templos*. Use *por* only when you want to name the doer."}])
lesson(s,'The Chiquitos missions: Jesuit churches that are still in use','Tell the story of the Jesuit missions of Chiquitos, using the ser passive for what was founded, expelled and restored.','the passive with ser + past participle',
 ['I can say what was founded, expelled and restored with *ser* + past participle.','I can say when the Chiquitos missions were declared World Heritage Sites.','I can name the main words for missions, churches and scores in Spanish.'])
ex(s,[
 match(s,1,[['la misión','mission (a settlement founded by missionaries)'],['el jesuita','Jesuit'],['el templo','church, temple'],['la partitura','musical score'],['expulsar','to expel']],V),
 fill(s,2,'Los jesuitas fueron __ de los territorios españoles en 1767.','expulsados','The Jesuits were expelled from the Spanish territories in 1767.','ser-passive',hint='expulsar'),
 mc(s,3,'Which sentence says: "The missions were founded by Jesuits"?',['Las misiones fueron fundadas por jesuitas.','Las misiones fueron fundados por jesuitas.','Las misiones fue fundada por jesuitas.','Las misiones fueron fundando por jesuitas.'],'ser-passive',ds={}),
 build(s,4,'Seis misiones fueron declaradas Patrimonio de la Humanidad en 1990.','Six missions were declared World Heritage Sites in 1990.','ser-passive'),
 dlg(s,5,[('Meg','¿Quién construyó los templos?'),('Carlos','Los templos _____ por jesuitas y por indígenas de la región.')],['fueron construidos','fueron construyendo','fue construido','están construidos'],'ser-passive',ds={1:'progressive',3:'pasiva-estado-estar-participio'}),
 dict_(s,6,'Las partituras fueron encontradas en los archivos de las misiones.','The scores were found in the archives of the missions.','ser-passive')])
story(s,'Las misiones jesuíticas de Chiquitos','Jesuits founded mission towns among the Chiquitano peoples of eastern Bolivia, were expelled in 1767, and six of the mission churches were declared World Heritage Sites in 1990; Baroque music still lives there.',[
 "En el este de Bolivia, en una región llamada Chiquitania, se conservan seis iglesias de antiguas misiones jesuíticas: San Francisco Javier, Concepción, Santa Ana, San Miguel, San Rafael y San José. Los jesuitas llegaron a la zona a fines del siglo XVII y fundaron pueblos, llamados misiones o reducciones, donde vivían familias de los pueblos chiquitanos y de otros pueblos de la región. La primera misión, San Francisco Javier, fue fundada en 1691.",
 "Cada pueblo tenía una plaza, una iglesia, talleres y escuelas. Las iglesias fueron construidas con madera de la región y decoradas con pinturas. En ellas la música tenía un lugar muy importante: los habitantes aprendían a cantar y a tocar instrumentos como el violín.",
 "En 1767, el rey Carlos III ordenó la expulsión de los jesuitas de los territorios españoles, y los misioneros tuvieron que irse. Después de su partida, las comunidades siguieron viviendo en los pueblos y usando las iglesias.",
 "Desde los años setenta del siglo XX, el arquitecto suizo Hans Roth dirigió la restauración de varios templos. Durante esos años aparecieron en los archivos de las misiones muchas partituras de música barroca. Entre ellas hay obras de compositores europeos, como Domenico Zipoli, y también piezas que se compusieron en las misiones.",
 "En 1990, la UNESCO declaró las seis misiones Patrimonio de la Humanidad. Hoy las iglesias siguen siendo lugares de oración, y cada dos años se celebra en la región un festival internacional de música barroca, donde las orquestas locales tocan junto a grupos de otros países."],
 [("When was the mission of San Francisco Javier founded?",["En 1691.","En 1767.","En 1990."],"The first paragraph."),
  ("What happened in 1767?",["El rey ordenó que los jesuitas salieran de los territorios españoles.","La UNESCO declaró las misiones Patrimonio de la Humanidad.","Hans Roth empezó a restaurar los templos."],"The third paragraph."),
  ("What was found in the archives of the missions?",["Partituras de música barroca.","Monedas de plata.","Mapas del Chaco."],"The fourth paragraph.")])
# ---------- 02 contrast
s=S('02')
vocab(s,[('la agroindustria','agribusiness','noun'),('la soya','soya, soybean','noun'),('el ganado','cattle','noun'),('el desmonte','clearing of forest','noun'),('el incendio','fire','noun')],'Santa Cruz and agribusiness')
grammar(s,'However, Nevertheless: Contrast in Santa Cruz',[
 {'type':'text','title':'What you already know','content':"You know *sin embargo* and *aunque* from A2 Unit 28, and *no obstante* from B1 Unit 1. They set one idea against another: good news against a problem, or a fact against a doubt. Santa Cruz is a region full of such contrasts: fast growth and large fields on one side, forest loss and fires on the other. *Sin embargo* and *no obstante* start a new clause and are followed by a comma."},
 {'type':'table','title':'Connectors of contrast','rows':[
  ['Santa Cruz es una ciudad muy grande; sin embargo, hace unas décadas era mucho más pequeña.','Santa Cruz is a very large city; however, a few decades ago it was much smaller.'],
  ['La soya es un producto importante. No obstante, necesita mucha tierra.','Soya is an important product. Nevertheless, it needs a lot of land.'],
  ['Aunque hay mucho ganado, la región también produce soya y caña de azúcar.','Although there is a lot of cattle, the region also produces soya and sugar cane.'],
  ['A pesar de los incendios, la región sigue creciendo.','In spite of the fires, the region keeps growing. (*a pesar de* + noun)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'La agroindustria crea empleo; sin embargo, algunas personas critican el desmonte.','english':'Agribusiness creates jobs; however, some people criticise the clearing of forest.'},
  {'spanish':'El campo produce mucho. No obstante, los incendios preocupan a los ambientalistas.','english':'The countryside produces a lot. Nevertheless, the fires worry environmentalists.'},
  {'spanish':'Aunque Santa Cruz es una ciudad moderna, conserva sus fiestas tradicionales.','english':'Although Santa Cruz is a modern city, it keeps its traditional festivals.'}]},
 {'type':'tip','content':"Do not stop at one connector: choose it by the relation. *Sin embargo* and *no obstante* mark the second idea as a contrast (the formal one is *no obstante*). *Aunque* can start the sentence or sit in the middle: *Aunque hay incendios, la región crece* or *La región crece aunque hay incendios*."}])
lesson(s,'Santa Cruz: a fast-growing city and its farmland','Describe Santa Cruz and its agribusiness, contrasting the benefits and the problems with sin embargo, no obstante and aunque.','contrast and concession connectors like sin embargo and no obstante',
 ['I can contrast two ideas about Santa Cruz with *sin embargo*, *no obstante* and *aunque*.','I can say what Santa Cruz produces and what worries some people.','I can name the main words for farming, forest clearing and fires in Spanish.'])
ex(s,[
 match(s,1,[['la agroindustria','agribusiness'],['la soya','soya, soybean'],['el ganado','cattle'],['el desmonte','clearing of forest'],['el incendio','fire']],V),
 fill(s,2,'La soya es un producto importante. __ embargo, necesita mucha tierra.','Sin','Soya is an important product. However, it needs a lot of land.','contrast-concession-connectors'),
 mc(s,3,'Which sentence says: "Agribusiness creates jobs; however, some people criticise the clearing of forest"?',['La agroindustria crea empleo; sin embargo, algunas personas critican el desmonte.','La agroindustria crea empleo; por eso, algunas personas critican el desmonte.','La agroindustria crea empleo; además, algunas personas critican el desmonte.','La agroindustria crea empleo; entonces, algunas personas critican el desmonte.'],'contrast-concession-connectors',ds={1:'porque-y-por-eso',2:'ordering-markers'}),
 build(s,4,'Aunque Santa Cruz es una ciudad moderna, conserva sus fiestas tradicionales.','Although Santa Cruz is a modern city, it keeps its traditional festivals.','contrast-concession-connectors'),
 dlg(s,5,[('Meg','Dicen que la agroindustria da trabajo a mucha gente.'),('Carlos','Sí; _____ algunas personas critican el desmonte.')],['sin embargo','por lo tanto','por eso'],'contrast-concession-connectors',ds={2:'porque-y-por-eso'}),
 dict_(s,6,'El campo produce mucho; no obstante, los incendios preocupan a los ambientalistas.','The countryside produces a lot; nevertheless, the fires worry environmentalists.','contrast-concession-connectors')])
story(s,'Santa Cruz y la agroindustria','Santa Cruz de la Sierra grew from a small town into Bolivia\'s most populous city on the back of farming; the region also faces forest clearing and fires.',[
 "Santa Cruz de la Sierra es hoy la ciudad más poblada de Bolivia. Fue fundada en 1561 por el español Ñuflo de Chaves, pero en otro lugar: más tarde la ciudad se trasladó al sitio actual. Durante siglos fue una población pequeña y lejana de los centros del país; sin embargo, hoy es la más grande.",
 "En el siglo XX, la región cambió mucho. Llegaron carreteras, inversiones y muchas personas del altiplano y de otras zonas. Hoy el departamento de Santa Cruz produce soya, caña de azúcar, girasol y carne, y la agroindustria tiene un papel muy importante en la economía de Bolivia.",
 "Los habitantes de esta región se llaman a sí mismos cruceños, y muchos usan también la palabra «camba» para hablar de la identidad del oriente. En 2008 Santa Cruz aprobó en un referéndum un estatuto de autonomía; el gobierno central lo consideró ilegal, y el tema siguió en debate.",
 "El crecimiento tiene también un costo. El desmonte para ampliar los cultivos y los pastos reduce el bosque, y en 2019 y en 2024 hubo grandes incendios forestales en el departamento. Algunos productores dicen que necesitan más tierras para producir; no obstante, las organizaciones ambientales piden más control.",
 "Así, Santa Cruz muestra dos caras de una misma realidad: una región que crea empleo y exportaciones, aunque también enfrenta críticas por el impacto ambiental."],
 [("Why is the present-day city of Santa Cruz in a different place from the original one?",["Porque la ciudad se trasladó más tarde.","Porque los incendios destruyeron la ciudad.","Porque la Constitución lo ordenó en 2009."],"The first paragraph."),
  ("What does Santa Cruz produce today, according to the text?",["Soya, caña de azúcar, girasol y carne.","Litio y plata.","Café y bananas solamente."],"The second paragraph."),
  ("What do environmental organisations ask for?",["Más control.","Más incendios.","Menos escuelas."],"The fourth paragraph.")])
# ---------- 03 hedging
s=S('03')
vocab(s,[('el salar','salt flat','noun'),('el litio','lithium','noun'),('la batería','battery','noun'),('la sal','salt','noun'),('el contrato','contract','noun')],'The Salar de Uyuni and lithium')
grammar(s,'Softening a Claim: Uyuni and Lithium',[
 {'type':'text','title':'What you already know','content':"You know *parece que*, *según parece*, *podría decirse que* and *tal vez convendría* from B2 Unit 21. A hedge keeps you from sounding more certain than you are. That matters with lithium, where plans change and many facts are still open."},
 {'type':'table','title':'Four ways to soften','rows':[
  ['Parece que el litio será importante para las baterías del futuro.','It seems that lithium will be important for the batteries of the future.'],
  ['Según parece, los contratos de 2024 todavía necesitan la aprobación del Congreso.','Apparently the contracts of 2024 still need the approval of Congress.'],
  ['Podría decirse que el litio es una oportunidad y también un reto.','One could say that lithium is an opportunity and also a challenge.'],
  ['Tal vez convendría explicar mejor cómo se extrae el litio.','Perhaps it would be a good idea to explain better how lithium is extracted.']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Parece que el Salar de Uyuni es lo que queda de antiguos lagos.','english':'It seems that the Salar de Uyuni is what is left of ancient lakes.'},
  {'spanish':'Según parece, el gobierno quiere una nueva ley del litio.','english':'Apparently the government wants a new lithium law.'},
  {'spanish':'Podría decirse que el salar es un lugar único.','english':'One could say that the salt flat is a unique place.'}]},
 {'type':'tip','content':"Use one hedge at a time. *Parece que* is followed by the indicative; *no parece que* takes the subjunctive: *No parece que sea fácil*. Hedges are for what you do not know; a number or a date from a source needs no hedge, only the source: *según el USGS*."}])
lesson(s,'The Salar de Uyuni and lithium: a salt flat with a future','Describe the Salar de Uyuni and the debate over lithium, using hedges to say what is certain and what is not.','hedging and epistemic distance',
 ['I can soften a claim about lithium with *parece que*, *según parece* and *podría decirse que*.','I can say what the Salar de Uyuni is and how it was formed.','I can say what the government says about lithium contracts, with the date.'])
ex(s,[
 match(s,1,[['el salar','salt flat'],['el litio','lithium'],['la batería','battery'],['la sal','salt'],['el contrato','contract']],V),
 fill(s,2,'__ parece, los contratos de 2024 todavía necesitan la aprobación del Congreso.','Según','Apparently, the contracts of 2024 still need the approval of Congress.','hedging'),
 mc(s,3,'Which sentence says, with a hedge: "It seems that lithium will be important for batteries"?',['Parece que el litio será importante para las baterías.','Es verdad que el litio será importante para las baterías.','Seguro que el litio será importante para las baterías.','Sin duda el litio será importante para las baterías.'],'hedging'),
 build(s,4,'Podría decirse que el salar es un lugar único.','One could say that the salt flat is a unique place.','hedging'),
 dlg(s,5,[('Meg','¿Qué pasa con los contratos del litio?'),('Carlos','_____ todavía necesitan la aprobación del Congreso.')],['Según parece,','Parece de que','Se parece que'],'hedging'),
 dict_(s,6,'Parece que el salar es lo que queda de antiguos lagos.','It seems that the salt flat is what is left of ancient lakes.','hedging')])
story(s,'El Salar de Uyuni y el litio','The Salar de Uyuni, the largest salt flat in the world, lies over lithium-rich brine; the state, foreign firms and the government of Rodrigo Paz have different plans, and in 2026 the 2024 contracts still lacked approval from Congress.',[
 "El Salar de Uyuni está en el suroeste de Bolivia, a unos tres mil seiscientos metros de altura. Con más de diez mil kilómetros cuadrados, es el salar más grande del mundo. Se formó por la desecación de antiguos lagos prehistóricos, y hoy parece una llanura blanca sin fin.",
 "Bajo la costra de sal hay una salmuera, un agua muy salada que contiene litio. Algunas comunidades de la zona recogen sal desde hace generaciones. Además, muchos turistas visitan el salar; en la época de lluvias, una capa fina de agua lo convierte en un enorme espejo.",
 "El litio se usa para fabricar baterías, y por eso muchos países se interesan por él. Según el Servicio Geológico de Estados Unidos, los recursos de litio identificados en Bolivia están entre los mayores del mundo. Sin embargo, la producción de Bolivia es todavía pequeña.",
 "El Estado boliviano quiere controlar este recurso y lo administra mediante una empresa estatal. En 2024 esa empresa firmó contratos con empresas de China y de Rusia. El gobierno del presidente Rodrigo Paz, que asumió en noviembre de 2025, dijo que revisará y publicará esos contratos y que quiere una nueva ley del litio. En 2026 los contratos todavía no tenían la aprobación del Congreso.",
 "Algunas comunidades y organizaciones piden estudios sobre el uso del agua y el impacto ambiental. Parece que el futuro del litio boliviano dependerá de las decisiones políticas de los próximos años."],
 [("What is the Salar de Uyuni?",["El salar más grande del mundo.","Una mina de plata.","Un lago de agua dulce."],"The first paragraph."),
  ("What is lithium used for, according to the text?",["Para fabricar baterías.","Para acuñar monedas.","Para hacer ponchos."],"The third paragraph."),
  ("What happened to the contracts of 2024 by 2026?",["Todavía no tenían la aprobación del Congreso.","El Congreso los aprobó todos.","El gobierno los canceló en 2024."],"The fourth paragraph.")])
# ---------- 04 pluscuamperfecto subj
s=S('04')
vocab(s,[('la trinchera','trench','noun'),('la sed','thirst','noun'),('el armisticio','armistice, truce','noun'),('el veterano','veteran','noun'),('el petróleo','oil, petroleum','noun')],'The Chaco War')
grammar(s,'If It Had Not Happened: The Chaco War',[
 {'type':'text','title':'What you already know','content':"You know *si* + *hubiera* + participle, with *habría* + participle, from B1 Unit 35. It talks about a past that did not happen: *Si hubiera tenido más agua, habría resistido más*. In history it is good for thinking about conditions and consequences without saying what would certainly have happened. Use it for simple, close conditions."},
 {'type':'table','title':'Past conditions that did not happen','rows':[
  ['Si los soldados hubieran tenido más agua, habrían sufrido menos.','If the soldiers had had more water, they would have suffered less.'],
  ['Si la guerra no hubiera terminado en 1935, habría muerto más gente.','If the war had not ended in 1935, more people would have died.'],
  ['Si hubiéramos sabido la historia del Chaco, habríamos entendido el museo.','If we had known the history of the Chaco, we would have understood the museum.'],
  ['Si el clima hubiera sido más fresco, las tropas habrían estado mejor.','If the climate had been cooler, the troops would have been better off.']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'Si hubieran tenido más agua, los soldados habrían sufrido menos en el Chaco.','english':'If they had had more water, the soldiers would have suffered less in the Chaco.'},
  {'spanish':'Si la guerra hubiera continuado, habría habido más muertos.','english':'If the war had continued, there would have been more dead.'},
  {'spanish':'Si no hubiera visto el museo, no habría entendido la historia.','english':'If I had not seen the museum, I would not have understood the history.'}]},
 {'type':'tip','content':"Never put *habría* after *si*: say *si hubiera tenido*, not *si habría tenido*. Both parts use *haber*: *hubiera* in the *si* clause and *habría* in the result. Keep the examples about conditions you can check, not about who would have won."}])
lesson(s,'The Chaco War (1932-1935): a war fought for the Chaco','Tell what the Chaco War was and what followed, using si + pluperfect subjunctive for conditions that did not happen.','counterfactual past conditions with si + pluperfect subjunctive',
 ['I can talk about a past that did not happen with *si* + *hubiera* + participle and *habría* + participle.','I can say who fought the Chaco War, when it ended and what the peace left.','I can name the main words for the war, such as *trinchera*, *sed* and *armisticio*.'])
ex(s,[
 match(s,1,[['la trinchera','trench'],['la sed','thirst'],['el armisticio','armistice, truce'],['el veterano','veteran'],['el petróleo','oil, petroleum']],V),
 fill(s,2,'Si los soldados __ tenido más agua, habrían sufrido menos.','hubieran','If the soldiers had had more water, they would have suffered less.','pluscuamperfecto-subjuntivo-si',answers=['hubieran','hubiesen']),
 mc(s,3,'Which sentence says: "If the war had not ended in 1935, more people would have died"?',['Si la guerra no hubiera terminado en 1935, habría muerto más gente.','Si la guerra no habría terminado en 1935, habría muerto más gente.','Si la guerra no terminara en 1935, habría muerto más gente.','Si la guerra no hubiera terminado en 1935, morirá más gente.'],'pluscuamperfecto-subjuntivo-si',ds={2:'imperfect-subjunctive-forms',3:'futuro-simple'}),
 build(s,4,'Si hubieran tenido más agua, los soldados habrían sufrido menos.','If they had had more water, the soldiers would have suffered less.','pluscuamperfecto-subjuntivo-si'),
 dlg(s,5,[('Meg','¿Por qué sufrieron tanto los soldados?'),('Carlos','Si _____ más agua, habrían sufrido menos.')],['hubieran tenido','habrían tenido','tuvieran'],'pluscuamperfecto-subjuntivo-si',ds={2:'imperfect-subjunctive-forms'}),
 dict_(s,6,'Si la guerra hubiera continuado, habría habido más muertos.','If the war had continued, there would have been more dead.','pluscuamperfecto-subjuntivo-si')])
story(s,'La Guerra del Chaco','Bolivia and Paraguay fought over the Chaco between 1932 and 1935; historians call it the bloodiest war in South America in the twentieth century, and it changed Bolivian politics.',[
 "La Guerra del Chaco enfrentó a Bolivia y Paraguay entre 1932 y 1935. El Chaco es una región seca, calurosa y cubierta de matorrales espinosos, con muy pocos ríos. Los dos países discutían desde hacía años por esa zona, y muchas personas creían que allí había petróleo. Según los historiadores, fue la guerra más sangrienta de Sudamérica en el siglo XX.",
 "Los soldados sufrieron mucho por la sed, el calor y las enfermedades. Si hubieran tenido más agua, habrían sufrido menos: la falta de agua fue uno de los problemas más graves de la guerra. Muchos de los soldados bolivianos venían del altiplano y no conocían un clima como el del Chaco. Las trincheras y las alambradas marcaron la forma de combatir.",
 "El 12 de junio de 1935 se firmó un armisticio. Un tratado de paz de 1938 dejó a Paraguay la mayor parte del territorio en disputa. Bolivia perdió así una gran parte del territorio que reclamaba.",
 "Después de la guerra, los veteranos y muchos jóvenes pidieron cambios políticos y sociales. En 1937 el gobierno boliviano nacionalizó los bienes de la empresa petrolera Standard Oil. Muchos historiadores señalan que la guerra cambió la política del país y ayudó a preparar la revolución de abril de 1952.",
 "Hoy, en Bolivia y en Paraguay, las ciudades tienen monumentos y museos que recuerdan la guerra, y los dos países la recuerdan de maneras distintas."],
 [("Between which countries was the Chaco War fought?",["Bolivia y Paraguay.","Bolivia y Perú.","Paraguay y Argentina."],"The first paragraph."),
  ("What did the soldiers suffer from?",["La sed, el calor y las enfermedades.","El frío y la nieve.","Los terremotos."],"The second paragraph."),
  ("What did the peace treaty of 1938 do?",["Dejó a Paraguay la mayor parte del territorio en disputa.","Dio todo el Chaco a Bolivia.","Creó un país nuevo en el Chaco."],"The third paragraph.")])
# ---------- 05 relative clauses
s=S('05')
vocab(s,[('el carnaval','carnival','noun'),('la diablada','devil dance of Oruro','noun'),('la morenada','dance of Oruro','noun'),('la máscara','mask','noun'),('el bailarín','dancer','noun')],'The Oruro carnival')
grammar(s,'Who and Where: Describing the Oruro Carnival',[
 {'type':'text','title':'What you already know','content':"You know relative clauses with *que* and *quien* from B1 Unit 5, and *donde* for places. A relative clause tells you more about a person, thing or place: *los bailarines que llevan máscaras*, *la ciudad donde se celebra el carnaval*. They let you describe a long procession in one flowing sentence. *Que* is the most common; *quien* is only for people."},
 {'type':'table','title':'Relative clauses at the carnival','rows':[
  ['Oruro es la ciudad donde se celebra el carnaval.','Oruro is the city where the carnival is held. (*donde* for a place)'],
  ['Los bailarines que llevan máscaras representan a los diablos.','The dancers who wear masks represent the devils. (*que* for people)'],
  ['La morenada es una danza que se baila con trajes muy pesados.','The morenada is a dance that is danced in very heavy costumes. (*que* for a thing)'],
  ['La Virgen del Socavón, a quien muchos mineros piden protección, tiene un santuario en Oruro.','The Virgin of the Mineshaft, whom many miners ask for protection, has a shrine in Oruro. (*a quien* after a preposition-like *a*)']]},
 {'type':'examples','title':'In context','items':[
  {'spanish':'La diablada es la danza que más se asocia con el carnaval de Oruro.','english':'The diablada is the dance most associated with the Oruro carnival.'},
  {'spanish':'Los músicos que acompañan a los bailarines tocan en las calles.','english':'The musicians who accompany the dancers play in the streets.'},
  {'spanish':'El santuario donde termina el desfile está en el centro de la ciudad.','english':'The shrine where the parade ends is in the centre of the city.'}]},
 {'type':'tip','content':"Use *donde* when the clause is about a place, and *quien* (with *a* or another preposition) when it is about a person. Everywhere else *que* works. The relative clause stays next to the noun it describes."}])
lesson(s,'The Oruro carnival: a mining city that dances','Describe the Oruro carnival, its dances and its Virgin, using relative clauses with que, quien and donde.','relative clauses with que and quien',
 ['I can describe the dances and the people of the Oruro carnival with *que*, *quien* and *donde*.','I can say when UNESCO recognised the carnival.','I can name the main words for the carnival, the dances and the dancers in Spanish.'])
ex(s,[
 match(s,1,[['el carnaval','carnival'],['la diablada','devil dance of Oruro'],['la morenada','dance of Oruro'],['la máscara','mask'],['el bailarín','dancer']],V),
 fill(s,2,'Oruro es la ciudad __ se celebra el carnaval.','donde','Oruro is the city where the carnival is held.','relative-clauses'),
 mc(s,3,'Which sentence says: "The dancers who wear masks represent the devils"?',['Los bailarines que llevan máscaras representan a los diablos.','Los bailarines quien llevan máscaras representan a los diablos.','Los bailarines llevan máscaras representan a los diablos.','Los bailarines que lleva máscaras representan a los diablos.'],'relative-clauses'),
 build(s,4,'La diablada es la danza que más se asocia con el carnaval de Oruro.','The diablada is the dance most associated with the Oruro carnival.','relative-clauses'),
 dlg(s,5,[('Meg','¿Quiénes son los músicos del desfile?'),('Carlos','Son las personas _____ acompañan a los bailarines.')],['que','donde','cuyo'],'relative-clauses',ds={2:'relativo-posesivo-cuyo'}),
 dict_(s,6,'Los músicos que acompañan a los bailarines tocan en las calles.','The musicians who accompany the dancers play in the streets.','relative-clauses')])
story(s,'El Carnaval de Oruro','The Oruro carnival, recognised by UNESCO in 2001 and 2008, is a long parade of dances such as the diablada and the morenada in honour of the Virgen del Socavón, patron of the miners.',[
 "Oruro es una ciudad minera del altiplano boliviano que cada año celebra uno de los carnavales más conocidos de Sudamérica. La fiesta se celebra antes de la Cuaresma, en febrero o marzo según el año, y dura varios días. La UNESCO lo proclamó Obra Maestra del Patrimonio Oral e Inmaterial de la Humanidad en 2001, y en 2008 lo incluyó en su lista representativa del patrimonio cultural inmaterial.",
 "El carnaval es, ante todo, una fiesta religiosa. Se celebra en honor de la Virgen del Socavón, a quien muchos mineros piden protección. Su santuario está en el centro de la ciudad, y allí termina el desfile principal, en el que los grupos de bailarines entran al templo para saludar a la Virgen.",
 "En el desfile participan miles de bailarines y músicos, organizados en grupos. Cada grupo tiene sus trajes, sus bandas y sus coreografías. Entre las danzas más conocidas están la diablada, la morenada y los caporales. Los bailarines de la diablada llevan máscaras de diablos, trajes bordados y capas de colores.",
 "Según una tradición, la diablada representa la lucha entre los diablos y el arcángel San Miguel, y mezcla ideas del cristianismo con creencias andinas, como la del Tío, el dueño de las minas. Otros pueblos andinos tienen danzas parecidas, y hay debates sobre el origen exacto de algunas de ellas.",
 "Durante el carnaval, Oruro recibe a muchos visitantes. Para las familias de la ciudad, que viven de la minería o del comercio, la fiesta es también una forma de mantener una promesa a la Virgen y de transmitir una tradición de generación en generación."],
 [("When did UNESCO proclaim the Oruro carnival a masterpiece?",["En 2001.","En 1990.","En 1935."],"The first paragraph."),
  ("In honour of whom is the carnival celebrated?",["De la Virgen del Socavón.","De los jesuitas.","Del presidente de Bolivia."],"The second paragraph."),
  ("What does the diablada represent, according to one tradition?",["La lucha entre los diablos y el arcángel San Miguel.","La fundación de Santa Cruz.","La guerra del Chaco."],"The fourth paragraph.")])
# ---------- consolidation
s=S('consolidation')
lesson(s,'Bolivia: the lowlands and the carnival, unit review','Review the Chiquitos missions, Santa Cruz, Uyuni, the Chaco War and the Oruro carnival, with the grammar you used to talk about them.','review: ser passive, contrast connectors, hedging, past hypotheticals, relative clauses',
 ['I can review what I learned about the Chiquitos missions, Santa Cruz, Uyuni, the Chaco War and the Oruro carnival.','I can use the *ser* passive, contrast connectors, hedges, *si* + *hubiera* and relative clauses.','I can say what the 2024 lithium contracts were and where they stood in 2026.'],
 ['I can say what was founded, expelled and restored with *ser* + past participle.','I can contrast two ideas about Santa Cruz with *sin embargo*, *no obstante* and *aunque*.','I can soften a claim about lithium with *parece que*, *según parece* and *podría decirse que*.','I can talk about a past that did not happen with *si* + *hubiera* + participle and *habría* + participle.','I can describe the dances and the people of the Oruro carnival with *que*, *quien* and *donde*.'])
items=[
 match(s,1,[['la misión','mission (a settlement founded by missionaries)'],['el litio','lithium'],['la trinchera','trench'],['la máscara','mask']],V),
 mc(s,2,'Which sentence says: "The church was built with wood from the region"?',['La iglesia fue construida con madera de la región.','La iglesia fue construido con madera de la región.','La iglesia fueron construidas con madera de la región.','La iglesia fue construyendo con madera de la región.'],'ser-passive'),
 fill(s,3,'Santa Cruz es una ciudad muy grande; __ embargo, hace unas décadas era mucho más pequeña.','sin','Santa Cruz is a very large city; however, a few decades ago it was much smaller.','contrast-concession-connectors'),
 mc(s,4,'Which sentence says, with a hedge: "It seems that the Salar de Uyuni is a unique place"?',['Parece que el Salar de Uyuni es un lugar único.','Es verdad que el Salar de Uyuni es un lugar único.','Sin duda el Salar de Uyuni es un lugar único.','Seguro que el Salar de Uyuni es un lugar único.'],'hedging'),
 fill(s,5,'Si el Chaco hubiera tenido más ríos, los soldados __ tenido más agua.','habrían','If the Chaco had had more rivers, the soldiers would have had more water.','pluscuamperfecto-subjuntivo-si'),
 build(s,6,'Oruro es una ciudad minera donde se celebra un gran carnaval.','Oruro is a mining city where a great carnival is held.','relative-clauses'),
 dict_(s,7,'Las iglesias de las misiones fueron decoradas con pinturas.','The churches of the missions were decorated with paintings.','ser-passive'),
 mc(s,8,'According to the texts of this unit, what happened to the contracts of 2024 on lithium?',['En 2026 aún no tenían la aprobación del Congreso.','En 2026 el Congreso los aprobó todos.','En 2026 ya habían producido toda la sal.','En 2024 los canceló el gobierno.'],None,cat='reading')]
for it in items: it['id']=it['id'].replace('consolidation.','con.')
ex(s,items)
