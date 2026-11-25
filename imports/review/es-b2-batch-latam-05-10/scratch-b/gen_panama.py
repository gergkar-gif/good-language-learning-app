import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-panama-vocab'
U='Panama'
INTRO_TAIL='The screens and instructions are in English; the readings are in Spanish.'

# ---------------- 01
s='b2-panama-01'
lesson(s,'The Isthmus of Panama and the Darién: a jungle without a road',
 'Describe the isthmus and the Darién jungle with relative clauses (que, quien).',
 'relative clauses with que and quien',
 ['In this lesson you read about the narrow strip of land between two seas and about the Darién, the jungle where the Pan-American Highway stops. You will also read what the Panamanian authorities said about migrants who cross it.',
  'The grammar is one you know: relative clauses with *que* and *quien*. '+INTRO_TAIL],
 ['I can describe the isthmus and the Darién with relative clauses (*que*, *quien*).',
  'I can say what the Darién is and why it matters.',
  'I can use the new words for the isthmus, swamps and eagles.'])
write_gr(s,'grammar.b2.panama.01.geografia-darien','The Isthmus and the Jungle: Relative Clauses',[
 T('You know relative clauses with *que* and *quien* from B1 Unit 5. They let you add information about a person, a thing or a place inside one sentence. Panama\'s geography is a good place to use them: an isthmus is a strip of land *que* joins two continents, and the Darién is a jungle *que* has no road.','What you already know'),
 TB('Que and quien at work',[
  ('El istmo es una franja de tierra que une dos continentes.','*que* for a thing: the isthmus is a strip of land that joins two continents'),
  ('La selva que está en el este del país no tiene carretera.','*que* for a place: the jungle that lies in the east of the country has no road'),
  ('Los migrantes que cruzan la selva se enfrentan a muchos peligros.','*que* for people: the migrants who cross the jungle face many dangers'),
  ('Los guías con quienes hablamos conocen bien el río.','*quien* after a preposition: the guides we talked to know the river well')]),
 EX([('La Carretera Panamericana, que recorre casi todo el continente, se interrumpe en el Darién.','The Pan-American Highway, which runs along almost the whole continent, stops in the Darién.'),
     ('Los emberá, que viven junto a los ríos, conocen bien la selva.','The Emberá, who live beside the rivers, know the jungle well.'),
     ('El águila harpía, que es el ave nacional de Panamá, vive en el Darién.','The harpy eagle, which is Panama\'s national bird, lives in the Darién.'),
     ('Las personas con quienes habló el periodista caminaron varios días.','The people the journalist spoke to walked for several days.')]),
 TIP('*Que* is the usual choice for people, things and places. *Quien* (plural *quienes*) is for people only, and you mostly need it after a preposition: *con quienes*, *de quienes*. A comma before *que* gives extra information (*El Darién, que está en el este, es una selva*); without commas the clause says which one you mean.')])
write_voc(s,'vocab.b2.panama.01','The isthmus and the jungle','Land, swamps and wildlife',[
 ('el istmo','isthmus','noun'),('la franja','strip, band (of land)','noun'),('el pantano','swamp','noun'),('el águila','eagle','noun'),('el ave','bird','noun')])
write_ex(s,[
 match(s+'.ex01',[('el istmo','isthmus'),('la franja','strip, band (of land)'),('el pantano','swamp'),('el águila','eagle')],V),
 mc(s+'.ex02','Which sentence says "The jungle that lies in the east of the country has no road"?',
  ['La selva que está en el este del país no tiene carretera.','La selva quien está en el este del país no tiene carretera.','La selva que ella está en el este del país no tiene carretera.'],teaches='relative-clauses'),
 fill(s+'.ex03','Los guías con __ hablamos conocen bien la selva.','quienes','The guides we talked to know the jungle well.','relative-clauses'),
 build(s+'.ex04','El águila harpía, que es el ave nacional de Panamá, vive en el Darién.','The harpy eagle, which is Panama\'s national bird, lives in the Darién.','relative-clauses'),
 dlg(s+'.ex05','¿Qué es el Darién?','','Ahora lo entiendo.',
  ['Es una selva del este de Panamá donde no hay carretera.','Es una isla del Caribe con muchas playas y hoteles.','Es un lago que se formó para el canal.'],V),
 dict_(s+'.ex06','La Carretera Panamericana, que recorre casi todo el continente, se interrumpe en el Darién.','The Pan-American Highway, which runs along almost the whole continent, stops in the Darién.','relative-clauses')])
n=story(s,'El istmo y la selva del Darién','Panama is a narrow strip of land between two seas, and the Darién jungle in the east has no road; the text also reports what the authorities said about migrants crossing it in 2023 and 2025.',[
 'Panamá es un istmo: una franja estrecha de tierra que une América del Norte con América del Sur y que separa el mar Caribe del océano Pacífico. En su parte más angosta mide unos cincuenta kilómetros de ancho. Durante mucho tiempo se dijo que el istmo se cerró hace unos tres millones de años; hoy los científicos discuten la fecha exacta. Lo que sí se sabe es que por esta franja pasaron animales y plantas de un continente a otro.',
 'En el este del país está el Darién, una selva de montañas, ríos y pantanos donde viven pueblos indígenas como los emberá y los wounaan. La Carretera Panamericana, que recorre casi todo el continente, se interrumpe allí: entre Panamá y Colombia no hay carretera. En el Parque Nacional del Darién, que la UNESCO declaró Patrimonio de la Humanidad en 1981, viven el jaguar y el águila harpía, que es el ave nacional de Panamá.',
 'En los últimos años el Darién se hizo conocido por otra razón. Según las autoridades panameñas, más de medio millón de personas cruzaron la selva a pie en 2023, y muchas de ellas eran venezolanas. Los migrantes que cruzan la selva se enfrentan a ríos peligrosos, a la lluvia y a los robos, como han denunciado organizaciones humanitarias. Algunas comunidades de la zona, que viven junto a los ríos, reciben a los migrantes al final de la caminata.',
 'En 2025, según esas mismas autoridades, el número de cruces bajó mucho. La selva sigue siendo, mientras tanto, el hogar de los pueblos que viven allí desde hace siglos.'],
 [('What does the text say about the Pan-American Highway?',['Se interrumpe en el Darién, entre Panamá y Colombia.','Pasa por el Darién y llega hasta el mar Caribe.','Termina en el canal, en el centro de Panamá.'],'The second paragraph says the highway stops in the Darién.'),
  ('According to the Panamanian authorities, what happened in 2023?',['Más de medio millón de personas cruzaron el Darién a pie.','Se terminó la carretera entre Panamá y Colombia.','Los migrantes dejaron de usar la selva.'],'The third paragraph gives the authorities\' figure for 2023.'),
  ('Who lives in the Darién, according to the text?',['Pueblos indígenas como los emberá y los wounaan.','Solo científicos y guardas del parque.','Los guna, en un archipiélago del Caribe.'],'The second paragraph names the Emberá and the Wounaan.')])
print(s,n)

# ---------------- 02
s='b2-panama-02'
lesson(s,'The Panama Canal: from a French failure to Panamanian control',
 'Tell the history of the canal, from 1881 to 1999, with antes de que and después de que.',
 'clauses with antes de que and despues de que',
 ['In this lesson you follow the canal from the French attempt of 1881 to the day in 1999 when Panama took it over. You will also read about the canal in the news in 2023-2025.',
  'The grammar is one you know: clauses with *antes de que* and *después de que*. '+INTRO_TAIL],
 ['I can say what happened before or after an event in the history of the canal, with *antes de que* and *después de que*.',
  'I can say what happened on 31 December 1999.',
  'I can use the new words for treaties, locks and sovereignty.'])
write_gr(s,'grammar.b2.panama.02.canal-soberania','The Canal in Time: Before and After',[
 T('You know *antes de que* and *después de que* from B2 Unit 7. The history of the canal is a chain of events, so it is the natural place to use them. After *antes de que* the verb is always in the subjunctive; after *después de que* it is in the indicative when the event has happened, and in the subjunctive when it is still to come.','What you already know'),
 TB('Before and after, applied to the canal',[
  ('Antes de que existiera el canal, los barcos rodeaban América del Sur.','*antes de que* + imperfect subjunctive: before the canal existed, ships sailed round South America'),
  ('Antes de que la obra se terminara, la empresa francesa quebró.','*antes de que* + imperfect subjunctive: before the work was finished, the company went bankrupt'),
  ('Después de que Panamá se separó de Colombia, firmó un tratado con Estados Unidos.','*después de que* + indicative: something that happened'),
  ('Después de que lleguen los barcos, se cerrarán las esclusas.','*después de que* + subjunctive: something still to come')]),
 EX([('Antes de que Panamá recibiera el canal, la Zona del Canal estaba bajo control estadounidense.','Before Panama received the canal, the Canal Zone was under American control.'),
     ('Después de que se firmó el tratado de 1903, Estados Unidos empezó a construir el canal.','After the treaty of 1903 was signed, the United States began to build the canal.'),
     ('Los barcos esperan en el mar antes de que se abran las esclusas.','The ships wait at sea before the locks open.'),
     ('Después de que pase el barco, las esclusas se vuelven a llenar.','After the ship passes, the locks fill again.')]),
 TIP('Ask the two questions you know. Who does the second action: the same person (*antes de salir*) or someone else (*antes de que salga*)? And for *después de que*: has it happened (indicative) or not yet (subjunctive)? *Antes de que* never takes the indicative.')])
write_voc(s,'vocab.b2.panama.02','The canal and sovereignty','Treaties, locks and control',[
 ('la soberanía','sovereignty','noun'),('la esclusa','lock (on a canal)','noun'),('el tratado','treaty','noun'),('rodear','to go round, to surround','verb'),('quebrar','to go bankrupt','verb')])
write_ex(s,[
 match(s+'.ex01',[('la soberanía','sovereignty'),('la esclusa','lock (on a canal)'),('el tratado','treaty'),('rodear','to go round, to surround')],V),
 mc(s+'.ex02','Which sentence says "Before the canal opened, ships sailed round South America"?',
  ['Antes de que se abriera el canal, los barcos rodeaban América del Sur.','Antes de que se abrió el canal, los barcos rodeaban América del Sur.','Antes de que el canal se abra, los barcos rodeaban América del Sur.'],teaches='antes-despues-de-que'),
 fill(s+'.ex03','Antes de que el canal __ a manos de Panamá, Estados Unidos controló la Zona del Canal durante décadas.','pasara','Before the canal passed into the hands of Panama, the United States controlled the Canal Zone for decades.','antes-despues-de-que',answers=['pasara','pasase']),
 build(s+'.ex04','Antes de que se terminara la obra, la empresa francesa quebró.','Before the work was finished, the French company went bankrupt.','antes-despues-de-que'),
 dlg(s+'.ex05','¿Qué pasó el 31 de diciembre de 1999?','','Gracias, ahora lo sé.',
  ['Panamá asumió el control total del canal, que antes administraba Estados Unidos.','Estados Unidos abrió el canal por primera vez, después de más de diez años de obras.','Panamá se separó de Colombia con la ayuda de barcos estadounidenses.'],V),
 dict_(s+'.ex06','Después de que se firmó el tratado de 1903, Estados Unidos empezó a construir el canal.','After the treaty of 1903 was signed, the United States began to build the canal.','antes-despues-de-que')])
n=story(s,'El canal de Panamá: de la quiebra francesa a la soberanía','The text tells how a French company failed in the 1880s, how the United States built the canal and ran a zone around it, how Panama took the canal over in 1999, and what happened in 2023-2025.',[
 'Durante siglos, los barcos que querían ir de un océano a otro tenían que rodear América del Sur. Antes de que existiera el canal, el viaje por el cabo de Hornos era largo y peligroso. La idea de cortar el istmo ya se discutía en el siglo XVI.',
 'En 1881 una empresa francesa, dirigida por Ferdinand de Lesseps, que había construido el canal de Suez, empezó a excavar en Panamá. Los derrumbes y enfermedades como la fiebre amarilla mataron a miles de trabajadores; según las estimaciones más citadas, a más de veinte mil. La empresa quebró en 1889, antes de que la obra se terminara.',
 'En 1903, después de que Panamá se separó de Colombia con el apoyo de barcos de guerra estadounidenses, se firmó el tratado Hay–Bunau-Varilla. Ningún panameño lo firmó: lo hizo en nombre de Panamá un ingeniero francés, Philippe Bunau-Varilla. El tratado daba a Estados Unidos el control, sin límite de tiempo, de una franja de tierra a los dos lados del canal: la Zona del Canal. El canal se abrió en agosto de 1914.',
 'El 9 de enero de 1964, después de que un grupo de estudiantes panameños entró en la Zona para izar su bandera, hubo enfrentamientos y murieron varias personas, la mayoría panameñas. Panamá rompió relaciones con Estados Unidos; hoy esa fecha es el Día de los Mártires.',
 'En 1977 el presidente estadounidense Jimmy Carter y el general panameño Omar Torrijos firmaron dos tratados. Panamá recibiría el canal a fines de 1999. Antes de que llegara ese día, en 1979, la Zona del Canal dejó de existir. Desde el 31 de diciembre de 1999 el canal está en manos de Panamá.',
 'En 2023 y 2024 la sequía bajó el nivel del lago Gatún, y se limitó el paso de barcos. En 2025 el presidente de Estados Unidos, Donald Trump, dijo que quería que el canal volviera a su control; el presidente de Panamá, José Raúl Mulino, respondió que la soberanía del canal no se negocia.'],
 [('Who signed the treaty of 1903 on behalf of Panama?',['Un ingeniero francés, Philippe Bunau-Varilla.','El presidente de Colombia.','Un grupo de estudiantes panameños.'],'The third paragraph says no Panamanian signed it.'),
  ('What happened on 31 December 1999, according to the text?',['El canal pasó a estar en manos de Panamá.','Se abrió el canal por primera vez.','Terminó la obra de los franceses.'],'The fifth paragraph says the canal has been in Panama\'s hands since that date.'),
  ('Why did the French company fail?',['Las enfermedades y los derrumbes mataron a miles de trabajadores, y la empresa quebró en 1889.','Estados Unidos compró la empresa en 1881.','Los estudiantes panameños cerraron la obra en 1964.'],'The second paragraph links the deaths, the landslides and the bankruptcy of 1889.')])
print(s,n)

# ---------------- 03
s='b2-panama-03'
lesson(s,'Afro-Antillean Panama: the workers who built the canal',
 'Talk about the Afro-Antillean workers and their legacy in Panama, granting a point with si bien.',
 'formal concessive clauses with si bien and the indicative',
 ['In this lesson you read about the workers from the Caribbean islands who came to build the railway and the canal, how they were treated, and what they left in Panamanian life.',
  'The grammar is one you know: *si bien* for granting a point formally. '+INTRO_TAIL],
 ['I can grant a point in a formal sentence with *si bien* and the indicative.',
  'I can say who the Afro-Antillean workers were and how the gold and silver lists treated them.',
  'I can use the new words for wages, workers and nationality.'])
write_gr(s,'grammar.b2.panama.03.herencia-afroantillana','Granting a Point: Si Bien',[
 T('You know *si bien* "although it is true that" from B2 Unit 8. It is formal, it takes the indicative, and it grants a fact before you say what matters more. The story of the Afro-Antillean workers is full of this contrast: their work was essential, *si bien* they were paid less.','What you already know'),
 TB('Si bien at work',[
  ('Si bien su trabajo era esencial, cobraban menos.','Although their work was essential, they were paid less.'),
  ('Si bien muchos hablaban inglés, se quedaron en Panamá.','Although many spoke English, they stayed in Panama.'),
  ('Los trabajadores, si bien eran necesarios, vivían separados.','The workers, although they were necessary, lived separately. (*si bien* can sit between commas.)'),
  ('Su trabajo era esencial; no obstante, cobraban menos.','Their work was essential; nevertheless they were paid less. (*no obstante*, B1 Unit 1.)')]),
 EX([('Si bien llegaron para trabajar, muchos antillanos se quedaron en Panamá.','Although they came to work, many West Indians stayed in Panama.'),
     ('Si bien la obra terminó en 1914, las comunidades antillanas siguieron creciendo.','Although the work ended in 1914, the Antillean communities kept growing.'),
     ('Esa música, si bien nació en Panamá, tiene raíces antillanas.','That music, although it was born in Panama, has Antillean roots.'),
     ('Si bien la Constitución de 1941 cambió la regla, la de 1946 la corrigió.','Although the Constitution of 1941 changed the rule, the one of 1946 corrected it.')]),
 TIP('After *si bien* use the indicative, because you are confirming a fact; do not add *que* and do not add *pero* in the main clause. It is two words with no accent: *sí* with an accent means "yes". For "even if" (a possibility) you still need *aunque* with the subjunctive.')])
write_voc(s,'vocab.b2.panama.03','Workers and legacy','Wages, lists and nationality',[
 ('cobrar','to be paid, to charge','verb'),('la nacionalidad','nationality, citizenship','noun'),('contratar','to hire','verb'),('la lista','list, roll','noun'),('la plata','silver','noun')])
write_ex(s,[
 match(s+'.ex01',[('cobrar','to be paid, to charge'),('la nacionalidad','nationality, citizenship'),('contratar','to hire'),('la lista','list, roll'),('la plata','silver')],V),
 mc(s+'.ex02','Which sentence says "Although their work was essential, the Antillean workers were paid less"?',
  ['Si bien su trabajo era esencial, los trabajadores antillanos cobraban menos.','Si bien que su trabajo era esencial, los trabajadores antillanos cobraban menos.','Si bien su trabajo era esencial, pero los trabajadores antillanos cobraban menos.'],teaches='concesivas-si-bien'),
 fill(s+'.ex03','__ bien muchos hablaban inglés, las comunidades antillanas se quedaron en Panamá.','Si','Although many spoke English, the Antillean communities stayed in Panama.','concesivas-si-bien'),
 build(s+'.ex04','Si bien llegaron para trabajar, muchos antillanos se quedaron en Panamá.','Although they came to work, many West Indians stayed in Panama.','concesivas-si-bien'),
 dlg(s+'.ex05','¿Qué era la lista de plata en la Zona del Canal?','','Ahora lo entiendo.',
  ['Era la lista de los trabajadores que cobraban menos, casi todos antillanos.','Era el nombre de un barco que cruzaba el canal cada semana.','Era un documento que recibían los ingenieros al terminar la obra.'],V),
 dict_(s+'.ex06','Si bien su trabajo era esencial, los trabajadores de la lista de plata cobraban menos.','Although their work was essential, the workers on the silver list were paid less.','concesivas-si-bien')])
n=story(s,'Los trabajadores afroantillanos y su herencia','The text describes the workers from the Caribbean islands who built the canal, the gold and silver lists, their communities, the citizenship rules of 1941 and 1946, and their legacy in food and music.',[
 'Para construir el canal hacían falta muchos trabajadores, y en Panamá no había suficientes. Por eso llegaron decenas de miles de personas de las islas del Caribe, sobre todo de Jamaica y de Barbados. Los franceses ya los habían contratado en el siglo XIX, y Estados Unidos siguió haciéndolo después.',
 'Si bien su trabajo era esencial, los trabajadores antillanos no tenían las mismas condiciones que los demás. En la Zona del Canal, Estados Unidos usaba dos listas de pago: la de oro y la de plata. En la práctica, la lista de oro era sobre todo para trabajadores estadounidenses blancos, y la de plata, para trabajadores antillanos negros. Los de la lista de plata cobraban menos y vivían y comían en lugares separados. Muchos murieron en accidentes y por enfermedades.',
 'Terminada la obra, muchos se quedaron. Si bien hablaban inglés y pertenecían a iglesias protestantes, se instalaron en barrios de la ciudad de Panamá y de Colón, donde fundaron sociedades de ayuda mutua, iglesias y periódicos.',
 'Su situación legal siguió siendo difícil. La Constitución de 1941 negó la nacionalidad panameña a los hijos de ciertos inmigrantes, entre ellos muchos antillanos. La Constitución de 1946 les devolvió ese derecho.',
 'Hoy la herencia antillana forma parte de la vida panameña. Se ve en la comida, como el arroz con coco, y en la música: según algunos historiadores, el reggae en español nació en Panamá en los años ochenta, con raíces en la música de los inmigrantes antillanos. En la capital, el Museo Afroantillano conserva la memoria de aquellos trabajadores.'],
 [('What were the gold list and the silver list?',['Dos listas de pago de la Zona del Canal, con salarios y condiciones distintos.','Dos monedas que se usaban en todo Panamá.','Dos barcos que cruzaban el canal.'],'The second paragraph explains the two pay lists.'),
  ('What did the Constitution of 1941 do, according to the text?',['Negó la nacionalidad panameña a los hijos de ciertos inmigrantes, entre ellos muchos antillanos.','Dio la nacionalidad a todos los trabajadores del canal.','Cerró las iglesias protestantes del país.'],'The fourth paragraph says the 1941 rule was changed in 1946.'),
  ('Where did many Antillean workers settle after the work ended?',['En barrios de la ciudad de Panamá y de Colón.','En las islas de Guna Yala.','En la selva del Darién.'],'The third paragraph names Panama City and Colón.')])
print(s,n)

# ---------------- 04
s='b2-panama-04'
lesson(s,'Panama as a hub: ships, flights, banks and unequal wealth',
 'Describe how Panama earns its living and who benefits, using the se passive.',
 'the passive se construction',
 ['In this lesson you read how Panama became a place where goods, flights and money meet: the Colón Free Zone, the airport, the dollar and the banks. You also read about the Panama Papers, the gap between regions and the copper mine.',
  'The grammar is one you know: the *se* passive, for saying what is done without saying who does it. '+INTRO_TAIL],
 ['I can say what is sold, used or published in Panama with the *se* passive.',
  'I can say why the Colón Free Zone and the airport matter to the economy.',
  'I can use the new words for trade, tariffs and money.'])
write_gr(s,'grammar.b2.panama.04.economia-hub-financiero','What Is Sold, Used and Published: the Se Passive',[
 T('You know the *se* passive from B1 Unit 6: *se busca una persona*, *se buscan personas*. When the doer does not matter, *se* + the verb says what is done, and the verb agrees with the thing. Trade and finance are described this way all the time: what is sold, what is used, what is published.','What you already know'),
 TB('The se passive in Panama\'s economy',[
  ('En la zona franca se venden mercancías de muchos países.','plural thing, plural verb: goods from many countries are sold'),
  ('En Panamá se usa el dólar estadounidense desde 1904.','singular thing, singular verb: the US dollar has been used since 1904'),
  ('Se publicaron los Papeles de Panamá en 2016.','past tense: the Panama Papers were published in 2016'),
  ('Las mercancías se reexportan a otros países.','the subject can come first: the goods are re-exported to other countries')]),
 EX([('En la Zona Libre de Colón se venden mercancías que luego se reexportan.','In the Colón Free Zone goods are sold which are later re-exported.'),
     ('En Panamá se usa el dólar, y el balboa solo existe en monedas.','In Panama the dollar is used, and the balboa exists only as coins.'),
     ('Después del escándalo se cambiaron algunas leyes.','After the scandal some laws were changed.'),
     ('En el aeropuerto de Tocumen se conectan vuelos de todo el continente.','At Tocumen airport flights from all over the continent connect.')]),
 TIP('Look at the thing, not at *se*: *se vende una casa*, *se venden casas*. If you want to name who did it (*fue publicado por periodistas*), the passive with *ser* + participle is the tool (you know *ser* + participle from B1 Unit 18); with *se* you leave the doer out.')])
write_voc(s,'vocab.b2.panama.04','Trade and money','Tariffs, goods and banks',[
 ('el arancel','tariff, customs duty','noun'),('la mercancía','goods, merchandise','noun'),('reexportar','to re-export','verb'),('la mina','mine','noun'),('inconstitucional','unconstitutional','adjective')])
write_ex(s,[
 match(s+'.ex01',[('el arancel','tariff, customs duty'),('la mercancía','goods, merchandise'),('la mina','mine'),('inconstitucional','unconstitutional')],V),
 mc(s+'.ex02','Which sentence says "Goods from many countries are sold in the Colón Free Zone"?',
  ['En la Zona Libre de Colón se venden mercancías de muchos países.','En la Zona Libre de Colón se vende mercancías de muchos países.','En la Zona Libre de Colón venden se mercancías de muchos países.'],teaches='pasiva-refleja'),
 fill(s+'.ex03','Los Papeles de Panamá se __ en 2016.','publicaron','The Panama Papers were published in 2016.','pasiva-refleja',hint='publicar'),
 build(s+'.ex04','En Panamá se usa el dólar estadounidense desde 1904.','In Panama the US dollar has been used since 1904.','pasiva-refleja'),
 dlg(s+'.ex05','¿Qué se vende en la Zona Libre de Colón?','','Qué interesante.',
  ['Se venden mercancías de muchos países, sin pagar aranceles.','Se venden solo frutas del interior del país, para el mercado local.','Se vende solo agua del lago Gatún a los barcos.'],V),
 dict_(s+'.ex06','En la Zona Libre de Colón se venden mercancías que luego se reexportan a otros países.','In the Colón Free Zone goods are sold which are later re-exported to other countries.','pasiva-refleja')])
n=story(s,'Panamá, centro de comercio y de finanzas','The text explains how Panama lives from services, trade and money, the Panama Papers, the gap between the capital and the indigenous regions, and the copper mine dispute of 2023.',[
 'Desde la bahía de la ciudad de Panamá se ve una línea de rascacielos que podría estar en cualquier ciudad rica del mundo. Esa imagen resume el modelo económico del país: Panamá vive sobre todo de los servicios, y su mejor recurso es su posición geográfica, entre dos océanos y entre dos continentes.',
 'El canal es la base de ese modelo. En la Zona Libre de Colón, creada en 1948 y presentada como una de las zonas francas más grandes de América, se venden mercancías sin aranceles de importación, y luego se reexportan a otros países de América Latina. En el aeropuerto de Tocumen, la aerolínea panameña Copa conecta la capital con muchas ciudades del continente. Además, en Panamá se usa el dólar estadounidense desde 1904; el balboa, la moneda propia del país, existe solo en monedas.',
 'Los bancos también son importantes. En 2016 se publicaron los Papeles de Panamá: más de once millones de documentos de un bufete panameño, Mossack Fonseca, que llegaron a periodistas de todo el mundo. Los documentos mostraron cómo personas de muchos países usaban empresas panameñas para guardar dinero en el extranjero. Después, Panamá cambió algunas leyes. En 2019 el GAFI, un organismo internacional contra el lavado de dinero, puso al país en su lista gris, la de los países bajo vigilancia; lo retiró de esa lista en 2023.',
 'La riqueza, sin embargo, no llega a todos por igual. La pobreza es mucho mayor en las comarcas indígenas y en el interior del país que en la capital. En 2023 hubo grandes protestas por el contrato de una mina de cobre en Donoso, y la Corte Suprema declaró inconstitucional ese contrato; la mina dejó de producir. En 2025 el gobierno del presidente José Raúl Mulino seguía estudiando qué hacer con ella.'],
 [('What is sold in the Colón Free Zone, according to the text?',['Mercancías sin aranceles de importación, que luego se reexportan.','Solo productos agrícolas del interior del país.','Dólares y balboas para los turistas.'],'The second paragraph describes the free zone.'),
  ('What does the text say about money in Panama?',['Se usa el dólar estadounidense desde 1904, y el balboa existe solo en monedas.','Se usa el balboa en papel moneda desde 1948.','Se usa el euro en la Zona Libre de Colón.'],'The second paragraph explains the dollar and the balboa.'),
  ('What happened to the copper mine contract in 2023?',['La Corte Suprema lo declaró inconstitucional, y la mina dejó de producir.','El gobierno lo amplió por veinte años.','Una empresa de Hong Kong compró la mina.'],'The fourth paragraph reports the Supreme Court decision.')])
print(s,n)

# ---------------- 05
s='b2-panama-05'
lesson(s,'Guna Yala and the rising sea: an island community moves to the mainland',
 'Talk about Guna autonomy and the climate move of 2024, using por más que.',
 'concessive clauses with por mas que and subjunctive',
 ['In this lesson you read about the Guna people and their comarca on the Caribbean coast, and about Gardi Sugdub, an island community that moved to the mainland in 2024 because of the rising sea.',
  'The grammar is one you know: *por más que* for "however much". '+INTRO_TAIL],
 ['I can say that nothing changes however much something happens, with *por más que* and *por mucho que*.',
  'I can say who governs Guna Yala and when the Guna rose up.',
  'I can use the new words for comarcas, islands and the sea.'])
write_gr(s,'grammar.b2.panama.05.pueblos-indigenas-comarcas','However Much: Por Más Que',[
 T('You know *por más que* "however much, no matter how much" from B2 Unit 8. It takes the subjunctive when the effort or amount is open and does not change the result. The climate story of the Guna islands fits it well: however much people do, the sea keeps rising.','What you already know'),
 TB('Por más que and por mucho que',[
  ('Por más que se construyan muros, el mar seguirá subiendo.','However many walls are built, the sea will keep rising. (Open, general: subjunctive.)'),
  ('Por mucho que cueste, algunas familias quieren irse.','However much it costs, some families want to leave.'),
  ('Por muy seguras que sean las casas nuevas, dejar la isla es difícil.','However safe the new houses are, leaving the island is hard. (*por muy* + adjective + *que* + subjunctive.)'),
  ('Por más que ampliaron la isla, el agua entraba en las casas.','However much they enlarged the island, the water came into the houses. (It really happened: indicative.)')]),
 EX([('Por más que bajen las emisiones, el nivel del mar seguirá subiendo durante décadas.','However much emissions fall, the sea level will keep rising for decades.'),
     ('Por más que las casas nuevas sean seguras, para muchos es difícil dejar la isla.','However safe the new houses are, for many it is hard to leave the island.'),
     ('Por mucho que cambie el clima, los guna quieren conservar su cultura.','However much the climate changes, the Guna want to keep their culture.'),
     ('Por más que lo intentaron, no pudieron detener el agua.','However hard they tried, they could not stop the water.')]),
 TIP('Use the subjunctive when you look ahead or speak in general (*por más que se construyan*), and the indicative when you tell what really happened (*por más que ampliaron*). The main clause often says that nothing changes: *no*, *seguirá*, *igual*.')])
write_voc(s,'vocab.b2.panama.05','Comarcas and the sea','Autonomy, islands and tides',[
 ('la comarca','indigenous region with its own authorities','noun'),('guna','Guna (an indigenous people of Panama); of the Guna','noun'),('la mola','mola (Guna textile panel)','noun'),('la marea','tide','noun'),('ampliar','to enlarge, to extend','verb'),('el nivel del mar','sea level','noun')])
write_ex(s,[
 match(s+'.ex01',[('la comarca','indigenous region with its own authorities'),('la mola','mola (Guna textile panel)'),('la marea','tide'),('ampliar','to enlarge, to extend')],V),
 mc(s+'.ex02','Which sentence says "However much emissions fall, the sea level will keep rising"?',
  ['Por más que bajen las emisiones, el nivel del mar seguirá subiendo.','Por más que bajan las emisiones, el nivel del mar seguirá subiendo.','Por más bajen las emisiones, el nivel del mar seguirá subiendo.'],teaches='concesivas-por-mas-que'),
 fill(s+'.ex03','Por más que las casas nuevas __ seguras, para muchos es difícil dejar la isla.','sean','However safe the new houses are, for many it is hard to leave the island.','concesivas-por-mas-que'),
 build(s+'.ex04','Por más que ampliaron la isla, el agua entraba en las casas.','However much they enlarged the island, the water came into the houses.','concesivas-por-mas-que'),
 dlg(s+'.ex05','¿Quién tiene la autoridad en la comarca de Guna Yala?','','Gracias, ahora lo entiendo.',
  ['El pueblo guna, con sus propias autoridades.','Una empresa que opera el canal desde 1999.','Un grupo de visitantes que llegó en 2024.'],V),
 dict_(s+'.ex06','Por más que bajen las emisiones, el nivel del mar seguirá subiendo durante décadas.','However much emissions fall, the sea level will keep rising for decades.','concesivas-por-mas-que')])
n=story(s,'Guna Yala y el mar que sube','The text presents the Guna comarca and its autonomy, the uprising of 1925, and the move of the Gardi Sugdub islanders to the mainland in 2024 because of the rising sea.',[
 'En la costa caribeña de Panamá está la comarca de Guna Yala, un archipiélago con cientos de islas, muchas de ellas muy pequeñas y sin habitantes. Allí vive el pueblo guna, que gobierna su territorio con sus propias autoridades: el Congreso General Guna y los congresos de cada comunidad. En Panamá hay varias comarcas indígenas; además de Guna Yala, existen, por ejemplo, la Emberá-Wounaan y la Ngäbe-Buglé.',
 'La autonomía de los guna tiene una historia. En febrero de 1925, después de que la policía panameña intentó cambiar sus costumbres, los guna se rebelaron en la llamada Revolución Dule. Poco después se firmó un acuerdo con el Estado, y en 1938 una ley reconoció el territorio de los guna como comarca. Los guna son conocidos también por sus molas, telas de colores hechas con capas de tela cosidas.',
 'Hoy el pueblo guna enfrenta un problema nuevo: el mar. Muchas comunidades viven en islas bajas, apenas un poco por encima del nivel del mar. Por más que los habitantes de Gardi Sugdub ampliaron la isla con piedras, el agua entraba en las casas cuando subía la marea. Según los científicos, por mucho que bajen las emisiones, el nivel del mar seguirá subiendo durante décadas.',
 'En 2024, más de mil personas de Gardi Sugdub se trasladaron a Isber Yala, un barrio nuevo construido por el Estado en tierra firme. Las autoridades y la prensa lo presentaron como una de las primeras reubicaciones planificadas por el cambio climático en América Latina. Para muchos fue una decisión difícil: por más que las casas nuevas sean seguras, no es fácil dejar la isla donde nacieron.'],
 [('Who governs the comarca of Guna Yala, according to the text?',['El pueblo guna, con sus propias autoridades.','La Autoridad del Canal de Panamá.','Un consorcio de empresas turísticas.'],'The first paragraph names the Guna General Congress.'),
  ('What happened in February 1925?',['Los guna se rebelaron en la Revolución Dule.','Los guna se trasladaron a Isber Yala.','Se abrió la Zona Libre de Colón.'],'The second paragraph describes the uprising.'),
  ('Where did the people of Gardi Sugdub move in 2024?',['A Isber Yala, un barrio nuevo en tierra firme.','A la ciudad de Colón, junto al canal.','A otra isla más grande del archipiélago.'],'The fourth paragraph names Isber Yala.')])
print(s,n)

# ---------------- consolidation
s='b2-panama-consolidation'
lesson(s,'Panama: Unit Review','Review the isthmus, the canal, the Afro-Antillean workers, the economy and the Guna comarca, with the grammar you used to talk about them.',
 'review: relative clauses, antes de que and después de que, si bien, the se passive, por más que',
 [],
 ['I can review what I learned about Panama, from the Darién to Guna Yala.',
  'I can use relative clauses, *antes de que* and *después de que*, *si bien*, the *se* passive and *por más que*.',
  'I can put the main events of the canal in order.',
  'I can say what is disputed or changing today, and who says so.'],
 ['I can describe a place or a person with *que* and *quien*.',
  'I can say what happened before or after an event with *antes de que* and *después de que*.',
  'I can grant a point formally with *si bien*.',
  'I can say what is sold, used or published with the *se* passive.',
  'I can say that nothing changes however much something happens, with *por más que*.'])
p=R+'lessons/b2/b2-panama-consolidation.json'; d=rj(p)
for sec in d['sections']:
    if sec['type']=='goal': sec['items']=['I can review what I learned about Panama, from the Darién to Guna Yala.','I can use relative clauses, *antes de que* and *después de que*, *si bien*, the *se* passive and *por más que*.','I can put the main events of the canal in order.','I can say what is disputed or changing today, and who says so.']
wj(p,d)
write_ex(s,[
 match(s+'.ex01',[('el istmo','isthmus'),('la soberanía','sovereignty'),('el arancel','tariff, customs duty'),('la comarca','indigenous region with its own authorities')],V),
 mc(s+'.ex02','Which sentence is correct?',['Antes de que Panamá recibiera el canal, la Zona del Canal existía.','Antes de que Panamá recibió el canal, la Zona del Canal existía.','Antes de que Panamá reciba el canal, la Zona del Canal existía.'],teaches='antes-despues-de-que'),
 fill(s+'.ex03','Los guna, __ viven en las islas de Guna Yala, tienen sus propias autoridades.',None,'The Guna, who live on the islands of Guna Yala, have their own authorities.','relative-clauses',answers=['que','quienes']),
 fill(s+'.ex04','Las mercancías de la Zona Libre de Colón se __ a otros países de América Latina.','reexportan','The goods of the Colón Free Zone are re-exported to other Latin American countries.','pasiva-refleja',hint='reexportar'),
 build(s+'.ex05','Por mucho que cambie el clima, los guna quieren conservar su cultura.','However much the climate changes, the Guna want to keep their culture.','concesivas-por-mas-que'),
 mc(s+'.ex06','Which sentence is correct?',['Si bien el canal se abrió en 1914, Panamá no lo administró hasta 1999.','Si bien el canal se abriera en 1914, Panamá no lo administró hasta 1999.','Si bien que el canal se abrió en 1914, Panamá no lo administró hasta 1999.'],teaches='concesivas-si-bien'),
 mc(s+'.ex07','According to the texts, what did the Supreme Court decide in 2023 about the copper mine?',['Declaró inconstitucional el contrato de la mina.','Dijo que la mina podía seguir abierta.','Vendió la mina a una empresa de Hong Kong.'],cat='reading'),
 dict_(s+'.ex08','Se publicaron los Papeles de Panamá en 2016, y después Panamá cambió algunas leyes.','The Panama Papers were published in 2016, and afterwards Panama changed some laws.','pasiva-refleja')])
