import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-cuba-vocab'
TAIL='The screens and instructions are in English; the readings are in Spanish.'

# ---------- 01
s='b2-cuba-01'
lesson(s,'Havana and Viñales: a fortified port city and a tobacco valley',
 'Describe Havana and the Viñales valley, adding your own stance with adverbs like lamentablemente and en rigor.',
 'focus and stance adverbs like precisamente and francamente',
 ['In this lesson you read about Havana, a port that Spain defended with fortresses, and about the Viñales valley, where tobacco grows between limestone hills. You will also read what is happening to many of the old buildings today.',
  'The grammar is one you know: stance and focus adverbs such as *lamentablemente*, *en rigor* and *precisamente*. '+TAIL],
 ['I can show my attitude to a fact with stance adverbs such as *lamentablemente*, *francamente* and *en rigor*.',
  'I can describe Old Havana and the Viñales valley.',
  'I can use the new words for fortresses, limestone hills and tobacco fields.'])
write_gr(s,None,'Havana and Viñales: Showing Your Attitude',[
 T('You know stance and focus adverbs such as *francamente* and *en rigor* from B2 Unit 1, and also *lamentablemente*, *precisamente* and *apenas*. A stance adverb steps outside the action and comments on the whole sentence. Describing a city is a good place to use them, because you often want to say how you feel about what you see: that something is a pity, or that, strictly speaking, a date is not what people think.','What you already know'),
 TB('Stance and focus adverbs at work',[
  ('Lamentablemente, algunos edificios están en mal estado.','*lamentablemente*: your feeling about a fact (a pity that...)'),
  ('En rigor, el pueblo de La Habana existía desde 1514.','*en rigor*: strictly speaking, you give the exact truth'),
  ('Precisamente en esas tierras rojas se cultiva el tabaco.','*precisamente*: exactly there, pointing at what follows'),
  ('La fortaleza apenas sufrió daños.','*apenas*: barely; no commas, it sits right before the verb')]),
 EX([('Lamentablemente, algunos edificios de La Habana Vieja están en mal estado.','Unfortunately, some buildings in Old Havana are in poor condition.'),
     ('En rigor, el pueblo de La Habana existía desde 1514 en otro lugar de la costa.','Strictly speaking, the town of Havana had existed since 1514 in another place on the coast.'),
     ('Precisamente en esas tierras rojas se cultiva un tabaco muy apreciado.','It is exactly in those red lands that a much-appreciated tobacco is grown.'),
     ('Francamente, la visita a la fortaleza no me convenció.','Frankly, the visit to the fortress did not convince me.')]),
 TIP('Try the comma test you know. If you can put commas round the adverb, it comments on the whole sentence: *Lamentablemente, ...*. Right after the verb with no commas, the same kind of word usually describes how something was done: *Habló francamente*. *Precisamente* and *apenas* take no commas.')])
write_voc(s,None,'Havana and Viñales','Fortresses, hills and tobacco',[
 ('la fortaleza','fortress','noun'),('el mogote','limestone hill (Viñales)','noun'),('la vega','tobacco field','noun'),('el derrumbe','collapse','noun'),('la colina','hill','noun'),('la roca','rock','noun')])
write_ex(s,[
 match(s+'.ex01',[('la fortaleza','fortress'),('el mogote','limestone hill (Viñales)'),('la vega','tobacco field'),('el derrumbe','collapse')],V),
 mc(s+'.ex02','Which sentence says "Frankly, the visit to the fortress did not convince me"?',
  ['Francamente, la visita a la fortaleza no me convenció.','La visita a la fortaleza no me convenció francamente.','Franco, la visita a la fortaleza no me convenció.'],teaches='stance-adverbs'),
 fill(s+'.ex03','En __, el pueblo de La Habana existía desde 1514 en otro lugar de la costa.','rigor','Strictly speaking, the town of Havana had existed since 1514 in another place on the coast.','stance-adverbs'),
 build(s+'.ex04','Lamentablemente, algunos edificios de La Habana Vieja están en mal estado.','Unfortunately, some buildings in Old Havana are in poor condition.','stance-adverbs'),
 dlg(s+'.ex05','¿Qué es un mogote?','','Ahora lo entiendo.',
  ['Es una colina de roca, típica del valle de Viñales.','Es una fortaleza de piedra que defiende la bahía de La Habana.','Es una plaza con una catedral en el centro de la ciudad.'],V),
 dict_(s+'.ex06','Precisamente en las tierras rojas de Viñales se cultiva un tabaco muy apreciado.','It is exactly in the red lands of Viñales that a much-appreciated tobacco is grown.','stance-adverbs')])
n=story(s,'La Habana y el valle de Viñales','Havana was a fortified port where Spanish fleets gathered, and its old centre is a World Heritage Site with buildings in need of repair; Viñales is a tobacco valley between limestone hills.',[
 'La Habana está en una bahía profunda y bien protegida, y por eso fue durante siglos un punto de reunión de las flotas españolas que volvían a Europa con plata y otras riquezas de América. La ciudad se fundó en su sitio actual en 1519; en rigor, el pueblo existía desde 1514 en otro lugar de la costa. Para defender La Habana de los piratas y de otras potencias se construyeron fortalezas de piedra, como el castillo del Morro y la fortaleza de San Carlos de la Cabaña, que se levantó después de 1762, cuando los británicos ocuparon la ciudad durante unos meses.',
 'La Habana Vieja, declarada Patrimonio de la Humanidad por la UNESCO en 1982, conserva plazas como la Plaza de Armas, la Plaza Vieja y la Plaza de la Catedral, y casas con portales, balcones y vitrales de colores. La Oficina del Historiador de la Ciudad ha restaurado muchos de esos edificios. Lamentablemente, otros están en mal estado, y en los últimos años se han producido derrumbes en la ciudad.',
 'A unas pocas horas en carretera hacia el oeste está el valle de Viñales, en la provincia de Pinar del Río. El valle es famoso por sus mogotes, colinas de roca caliza con paredes casi verticales y cima redonda, que se elevan sobre los campos de cultivo. Allí los campesinos, llamados vegueros, cultivan tabaco en las vegas de tierra roja, y muchos todavía trabajan con bueyes. Precisamente en esa región se cultiva un tabaco muy apreciado. La UNESCO declaró el valle paisaje cultural de la humanidad en 1999.'],
 [('Why was Havana a meeting point for Spanish fleets, according to the text?',['Porque está en una bahía profunda y bien protegida.','Porque tiene las minas de plata más grandes de América.','Porque está en el centro de la isla, lejos del mar.'],'The first paragraph links the bay to the fleets.'),
  ('What does the text say about some buildings in Old Havana?',['Están en mal estado, y ha habido derrumbes en los últimos años.','Fueron construidos por los británicos en 1762.','Se convirtieron en fortalezas en 1982.'],'The second paragraph reports poor condition and collapses.'),
  ('What are the mogotes of Viñales?',['Colinas de roca caliza que se elevan sobre los campos de cultivo.','Plazas con casas de colores en La Habana Vieja.','Fortalezas de piedra junto a la bahía.'],'The third paragraph describes the mogotes.')])
print(s,n)

# ---------- 02
s='b2-cuba-02'
lesson(s,'José Martí: the writer who prepared Cuba\'s war of independence',
 'Report what José Martí wrote and did, using reported speech and the right tense shifts.',
 'reported speech and tense shifting',
 ['In this lesson you read about José Martí, the Cuban poet, journalist and organiser who died in 1895 in the war for independence. You will report what he wrote, always in your own words: this lesson contains no quotations from his works.',
  'The grammar is one you know: reported speech with *dijo que*, *escribió que* and *explicó que*, and the tense shifts. '+TAIL],
 ['I can report what someone said or wrote, shifting the tenses (*quería*, *había escrito*, *haría*).',
  'I can tell the main events of Martí\'s life in order.',
  'I can use the new words for exile, essays and letters.'])
write_gr(s,None,'What Martí Wrote: Reporting in the Past',[
 T('You know reported speech with *dijo que* and *afirmó que* from B1 Unit 13: *decir*, *afirmar* or *explicar* + *que*, and when the reporting verb is in the past the verb inside moves back. The present becomes the imperfect, the preterite becomes the pluperfect, and the future becomes the conditional. History is told this way: you say that someone wrote, or said, or explained something. In this lesson every report is a paraphrase in your own words, never a quotation.','What you already know'),
 TB('Tense shifts in reports',[
  ('Martí escribió: quiero la independencia. -> Martí escribió que quería la independencia.','present -> imperfect: he wrote that he wanted independence'),
  ('Carlos: Martí publicó el ensayo en 1891. -> Carlos dijo que Martí había publicado el ensayo en 1891.','preterite -> pluperfect: Carlos said that Martí had published the essay in 1891'),
  ('Meg: visitaré Viñales. -> Meg dijo que visitaría Viñales.','future -> conditional: Meg said that she would visit Viñales'),
  ('La guía: los mogotes son colinas. -> La guía dijo que los mogotes eran colinas.','present -> imperfect: the guide said that the mogotes were hills')]),
 EX([('Martí escribió que quería la independencia de Cuba.','Martí wrote that he wanted the independence of Cuba.'),
     ('Carlos dijo que Martí había muerto en 1895.','Carlos said that Martí had died in 1895.'),
     ('Martí explicó que su deber era impedir que Estados Unidos se extendiera por las Antillas.','Martí explained that his duty was to stop the United States from spreading across the Antilles.'),
     ('La guía dijo que los mogotes eran colinas de roca caliza.','The guide said that the mogotes were limestone hills.')]),
 TIP('The shift happens only when the reporting verb is in the past. *Martí dice que quiere* (present) keeps the present, but *Martí dijo que quería* moves back. Pronouns and time words move too: *aquí* becomes *allí*, *mañana* becomes *al día siguiente*. And never put words in an author\'s mouth: when you do not have the exact words, report the idea with *explicó que*.')])
write_voc(s,None,'José Martí','Exile, essays and letters',[
 ('el destierro','exile','noun'),('el ensayo','essay','noun'),('la carta','letter','noun'),('impedir','to prevent, to stop','verb')])
write_ex(s,[
 match(s+'.ex01',[('el destierro','exile'),('el ensayo','essay'),('la carta','letter'),('impedir','to prevent, to stop')],V),
 mc(s+'.ex02','Carlos told Meg that José Martí had died in 1895. Which sentence says this?',
  ['Carlos dijo que Martí había muerto en 1895.','Carlos dijo que Martí ha muerto en 1895.','Carlos dijo que Martí moriría en 1895.'],teaches='estilo-indirecto'),
 fill(s+'.ex03','Carlos dijo que Martí __ publicado «Nuestra América» en 1891.','había','Carlos said that Martí had published «Nuestra América» in 1891.','estilo-indirecto'),
 build(s+'.ex04','Martí escribió que quería la independencia de Cuba.','Martí wrote that he wanted the independence of Cuba.','estilo-indirecto'),
 dlg(s+'.ex05','¿Qué hizo Martí en Nueva York?','','Qué interesante.',
  ['Trabajó como periodista y escribió poemas, ensayos y cartas.','Dirigió la construcción de una fortaleza en La Habana.','Fundó el Instituto de Cine de Cuba.'],V),
 dict_(s+'.ex06','Martí explicó que su deber era impedir que Estados Unidos se extendiera por las Antillas.','Martí explained that his duty was to stop the United States from spreading across the Antilles.','estilo-indirecto')])
n=story(s,'José Martí, poeta y organizador de la independencia','The text tells the life of José Martí, from his arrest as a teenager and exile to the war of 1895 and his death at Dos Ríos, and explains why people with different views still cite him today.',[
 'José Martí nació en La Habana en 1853, hijo de padres españoles. A los dieciséis años fue condenado a seis años de trabajos forzados por oponerse a las autoridades coloniales. Después lo enviaron a España, donde estudió Derecho y Filosofía y Letras. Más tarde vivió en México, Guatemala, Venezuela y, durante casi quince años, en Nueva York, donde trabajó como periodista y escribió poemas, ensayos y cartas.',
 'En enero de 1891 publicó el ensayo «Nuestra América». En él explicó que los países de América Latina debían conocer su propia realidad y no copiar modelos de otros lugares. Ese mismo año apareció su libro de poemas «Versos sencillos».',
 'Martí quería la independencia de Cuba, que seguía siendo una colonia española. En 1892 fundó el Partido Revolucionario Cubano, con el apoyo de muchos emigrados cubanos, entre ellos trabajadores del tabaco de Florida. En enero de 1895, las autoridades de Estados Unidos incautaron en Fernandina, Florida, barcos y armas de la expedición. Aun así, la guerra empezó en febrero, y en abril Martí llegó a Cuba.',
 'Murió el 19 de mayo de 1895 en Dos Ríos, en un combate contra tropas españolas, a los cuarenta y dos años. En una carta a su amigo Manuel Mercado, escrita el día anterior, Martí explicó que su deber era impedir, con la independencia de Cuba, que Estados Unidos se extendiera por las Antillas.',
 'Hoy Martí es una figura central en Cuba: su cumpleaños se celebra cada 28 de enero, y su imagen está en plazas y escuelas. Tanto el gobierno cubano como sus críticos, dentro y fuera de la isla, citan sus ideas para defender posiciones distintas.'],
 [('What was Martí sentenced to at the age of sixteen?',['A seis años de trabajos forzados.','A vivir en Nueva York.','A dirigir un periódico.'],'The first paragraph reports the sentence.'),
  ('What did Martí explain in his letter to Manuel Mercado?',['Que su deber era impedir que Estados Unidos se extendiera por las Antillas.','Que quería vivir en España.','Que ya había ganado la guerra de independencia.'],'The fourth paragraph paraphrases the letter.'),
  ('Who cites Martí\'s ideas today, according to the text?',['Tanto el gobierno cubano como sus críticos.','Solo el gobierno de Estados Unidos.','Solo los historiadores españoles.'],'The last paragraph says both sides cite him.')])
print(s,n)

# ---------- 03
s='b2-cuba-03'
lesson(s,'Cuba from 1959: the revolution, the literacy campaign and the Cold War',
 'Tell what happened after 1959, using conditions without si (de + infinitive and the gerund).',
 'conditions without si using de + infinitive or the gerund',
 ['In this lesson you read what happened in Cuba after 1 January 1959: the agrarian reform, the literacy campaign of 1961, the Bay of Pigs and the missile crisis. The revolution and its results are disputed, so the text gives dated facts and says who judges what.',
  'The grammar is one you know: conditions without *si*, with *de* + infinitive or with the gerund. '+TAIL],
 ['I can state a condition without *si*, with *de* + infinitive or the gerund.',
  'I can say what the literacy campaign of 1961 was and who took part in it.',
  'I can use the new words for literacy, peasants and the embargo.'])
write_gr(s,None,'If Not, If Necessary: Conditions Without Si',[
 T('You know conditions without *si* from B2 Unit 10: *de* + infinitive (*De ser necesario*, *De no haber existido*) and the gerund (*Estudiando más, aprobarías*). They are shorter and sound more written. The literacy campaign and the Cold War are full of "if" thinking: what would have happened without the campaign, what is done if necessary.','What you already know'),
 TB('Conditions without si',[
  ('De no haber existido la campaña, muchas personas no habrían aprendido a leer.','*de* + *haber* + participle = *si no hubiera existido*: had the campaign not existed'),
  ('De ser necesario, los brigadistas se quedaban a dormir en la casa.','*de* + infinitive = *si era necesario*: if necessary'),
  ('De haber sabido leer, los campesinos habrían podido escribir cartas.','*de haber sabido* = *si hubieran sabido*: had they known how to read'),
  ('Estudiando cada noche, aprenderías a leer en pocos meses.','gerund = *si estudiaras*: if you studied every night')]),
 EX([('De no haber existido la campaña, muchas personas no habrían aprendido a leer.','Had the campaign not existed, many people would not have learned to read.'),
     ('De ser necesario, los brigadistas se quedaban a dormir en la casa de la familia.','If necessary, the volunteer teachers stayed to sleep in the family\'s house.'),
     ('De haber sabido leer, muchos campesinos habrían podido escribir cartas.','Had they known how to read, many peasants could have written letters.'),
     ('Estudiando cada noche, aprenderías a leer en pocos meses.','If you studied every night, you would learn to read in a few months.')]),
 TIP('After *de* the verb is always an infinitive: *De haberlo sabido*, never *De hubiera sabido*. The main clause shows the time: conditional perfect (*habrían aprendido*) for the past, present or imperfect for a real condition. A gerund condition shares its subject with the main clause.')])
write_voc(s,None,'1959, literacy and the Cold War','Literacy, peasants and embargo',[
 ('la alfabetización','literacy campaign, teaching to read','noun'),('el campesino','peasant, farmer','noun'),('el embargo','embargo','noun'),('el misil','missile','noun')])
write_ex(s,[
 match(s+'.ex01',[('la alfabetización','literacy campaign, teaching to read'),('el campesino','peasant, farmer'),('el embargo','embargo'),('el misil','missile')],V),
 mc(s+'.ex02','Which sentence means "If you studied every night, you would learn to read in a few months"?',
  ['Estudiando cada noche, aprenderías a leer en pocos meses.','Estudiar cada noche, aprenderías a leer en pocos meses.','Estudiado cada noche, aprenderías a leer en pocos meses.'],teaches='implicit-conditionals'),
 fill(s+'.ex03','De __ necesario, los brigadistas se quedaban a dormir en la casa de la familia.','ser','If necessary, the volunteer teachers stayed to sleep in the family\'s house.','implicit-conditionals'),
 build(s+'.ex04','De no haber existido la campaña, muchas personas no habrían aprendido a leer.','Had the campaign not existed, many people would not have learned to read.','implicit-conditionals'),
 dlg(s+'.ex05','¿Qué hicieron los brigadistas en 1961?','','Ahora lo entiendo.',
  ['Fueron al campo a enseñar a leer a los campesinos.','Construyeron los misiles que llegaron a la isla.','Dirigieron la reforma agraria desde La Habana.'],V),
 dict_(s+'.ex06','De haber sabido leer, muchos campesinos habrían podido escribir cartas.','Had they known how to read, many peasants could have written letters.','implicit-conditionals')])
n=story(s,'1959: revolución, alfabetización y Guerra Fría','After 1 January 1959 Cuba carried out an agrarian reform and a literacy campaign, faced the Bay of Pigs and the missile crisis, and today the government and its critics judge those years differently.',[
 'El 1 de enero de 1959, el presidente Fulgencio Batista salió de Cuba, y los rebeldes dirigidos por Fidel Castro llegaron a La Habana el 8 de enero. Muchos cubanos celebraron el cambio; otros se opusieron al nuevo gobierno o salieron del país.',
 'En mayo de 1959 se aprobó la primera ley de reforma agraria, que limitó en general a unas cuatrocientas hectáreas la tierra que podía tener una persona o una empresa, y repartió tierra entre campesinos. Empresas estadounidenses, que tenían mucha tierra en la isla, perdieron parte de ella. Estados Unidos respondió con medidas económicas, y en 1962 impuso un embargo comercial, que el gobierno cubano llama «bloqueo». Cuba se acercó a la Unión Soviética.',
 'En 1961 el gobierno organizó una campaña de alfabetización. Según las cifras oficiales, unos cien mil jóvenes, muchos de ellos adolescentes, viajaron al campo para enseñar a leer y a escribir a los campesinos, y vivieron con las familias. De ser necesario, se quedaban a dormir en la casa de la familia. La campaña terminó el 22 de diciembre de 1961, y según el gobierno cubano unas setecientas mil personas aprendieron a leer y a escribir.',
 'En abril de 1961, un grupo de exiliados cubanos entrenados por Estados Unidos desembarcó en Bahía de Cochinos (Playa Girón) y fue derrotado por las fuerzas cubanas en pocos días. En octubre de 1962, la «crisis de los misiles» llevó al mundo al borde de una guerra nuclear: Estados Unidos descubrió misiles soviéticos en Cuba, y la Unión Soviética aceptó retirarlos después de un acuerdo con Estados Unidos, que se comprometió a no invadir Cuba.',
 'Hoy los cubanos y los historiadores valoran esos años de forma distinta. El gobierno cubano destaca la educación, la salud pública y la soberanía; sus críticos señalan que el país tiene un solo partido legal y que se limitaron libertades como la de prensa y la de asociación.'],
 [('What did the first agrarian reform law of May 1959 do?',['Limitó la tierra que podía tener una persona o una empresa y repartió tierra entre campesinos.','Prohibió el cultivo de tabaco en toda la isla.','Entregó las tierras a empresas estadounidenses.'],'The second paragraph describes the law.'),
  ('According to the official figures, who travelled to the countryside in 1961?',['Unos cien mil jóvenes, que enseñaron a leer y a escribir a los campesinos.','Soldados soviéticos, que instalaron misiles.','Exiliados cubanos, que desembarcaron en Bahía de Cochinos.'],'The third paragraph gives the official figures.'),
  ('What happened in October 1962?',['Estados Unidos descubrió misiles soviéticos en Cuba, y la Unión Soviética aceptó retirarlos.','Batista salió de Cuba.','Terminó la campaña de alfabetización.'],'The fourth paragraph describes the missile crisis.')])
print(s,n)

# ---------- 04
s='b2-cuba-04'
lesson(s,'Son, trova and cinema: Cuban culture in song and film',
 'Talk about Cuban music and film with the verbs that change meaning in the past: conocer, saber, querer, poder.',
 'verbs with aspectual meaning shifts in past tenses',
 ['In this lesson you read about the son, the Nueva Trova, the film institute ICAIC and the album Buena Vista Social Club. You will practise telling the past with verbs that mean something different in the preterite and in the imperfect.',
  'The grammar is one you know: *conocer*, *saber*, *querer* and *poder* in the preterite and the imperfect. '+TAIL],
 ['I can tell the difference between *conocí* and *conocía*, *supe* and *sabía*, *quise* and *quería*, *pude* and *podía*.',
  'I can say what the son and the Nueva Trova are.',
  'I can use the new words for troubadours, rhythm and lyrics.'])
write_gr(s,None,'Met, Found Out, Refused: Verbs That Change Meaning',[
 T('You know *conocer*, *saber*, *querer* and *poder* from B2 Unit 2. In the imperfect they name a state (I knew, I wanted, I was able); in the preterite they name an event with a start or an end, and the meaning shifts: I met, I found out, I tried or refused, I managed. Stories of songs and films are full of such moments.','What you already know'),
 TB('Same verb, two tenses',[
  ('Conocía el son. / Conocí a un trovador.','I knew the son. / I met a troubadour (for the first time).'),
  ('Sabía la letra. / Supe la noticia ayer.','I knew the lyrics. / I found out the news yesterday.'),
  ('Quería irse. / No quiso irse.','He wanted to leave. / He refused to leave.'),
  ('Podía cantar. / Pudo cantar.','He was able to sing. / He managed to sing.')]),
 EX([('Sergio no quiso irse de Cuba con su familia.','Sergio refused to leave Cuba with his family.'),
     ('El gobierno quiso crear un cine propio y fundó el ICAIC en 1959.','The government set out to create its own cinema and founded the ICAIC in 1959.'),
     ('Ayer conocí a un trovador cubano en un concierto.','Yesterday I met a Cuban troubadour at a concert.'),
     ('Cuando conocí el son, no sabía que había nacido en el este de la isla.','When I got to know the son, I did not know it had been born in the east of the island.')]),
 TIP('Do not translate by tense alone: ask whether something happened (an event) or how things were (a state). In the negative, *no quiso* is a refusal, *no pudo* means you tried and did not manage, and *no quería* and *no podía* only say how things stood.')])
write_voc(s,None,'Son, trova and cinema','Troubadours, rhythm and lyrics',[
 ('el trovador','troubadour, singer-songwriter','noun'),('la clave','claves (two sticks); rhythm pattern','noun'),('la letra','lyrics','noun'),('el cantautor','singer-songwriter','noun'),('el ritmo','rhythm','noun'),('el palo','stick','noun')])
write_ex(s,[
 match(s+'.ex01',[('el trovador','troubadour, singer-songwriter'),('la clave','claves (two sticks); rhythm pattern'),('la letra','lyrics'),('el cantautor','singer-songwriter'),('el ritmo','rhythm'),('el palo','stick')],V),
 mc(s+'.ex02','Which sentence says "Sergio refused to leave Cuba with his family"?',
  ['Sergio no quiso irse de Cuba con su familia.','Sergio no quería irse de Cuba con su familia.','Sergio no pudo irse de Cuba con su familia.'],teaches='verbos-cambio-significado-pasado'),
 fill(s+'.ex03','Ayer __ a un trovador cubano en un concierto.','conocí','Yesterday I met a Cuban troubadour at a concert.','verbos-cambio-significado-pasado'),
 build(s+'.ex04','El gobierno quiso crear un cine propio y fundó el ICAIC en 1959.','The government set out to create its own cinema and founded the ICAIC in 1959.','verbos-cambio-significado-pasado'),
 dlg(s+'.ex05','¿Qué es la clave?','','Gracias, ahora lo entiendo.',
  ['Son dos palos de madera que dan el ritmo del son.','Es un baile lento de las fiestas de La Habana.','Es una película del director Gutiérrez Alea.'],V),
 dict_(s+'.ex06','Cuando conocí el son, no sabía que había nacido en el este de la isla.','When I got to know the son, I did not know it had been born in the east of the island.','verbos-cambio-significado-pasado')])
n=story(s,'El son, la trova y el cine cubano','Cuban music mixes African and Spanish traditions; the text covers the son, the Nueva Trova, the film institute ICAIC and the film Memorias del subdesarrollo, and the album Buena Vista Social Club.',[
 'La música es una de las grandes aportaciones de Cuba. En ella se mezclaron ritmos africanos, traídos por personas esclavizadas, y melodías y poesía de origen español, de campesinos de Andalucía y de las islas Canarias. De esa mezcla nacieron géneros como el danzón, el mambo, el bolero y el son.',
 'El son nació a fines del siglo XIX en el este de la isla, en la región de Santiago de Cuba. En él suenan la guitarra, el tres, los bongós, las maracas y la clave, dos palos de madera que marcan el ritmo. En los años veinte el son llegó a las salas de baile de La Habana, y desde allí se hizo famoso en otros países.',
 'Después de 1959 surgió la Nueva Trova, con cantautores como Silvio Rodríguez, Pablo Milanés y Noel Nicola. Cantaban con la guitarra y escribían letras muy poéticas, sobre el amor, la historia y la vida del país, y muchas de sus canciones se hicieron famosas en toda América Latina.',
 'En marzo de 1959 el gobierno creó el Instituto Cubano del Arte e Industria Cinematográficos, el ICAIC, que produjo películas, documentales y noticieros. En 1968, el director Tomás Gutiérrez Alea estrenó «Memorias del subdesarrollo», basada en una novela de Edmundo Desnoes. Su protagonista, Sergio, no quiso irse de Cuba con su familia y observa cómo cambia la ciudad.',
 'En los años noventa, durante la crisis económica, la música cubana tuvo un nuevo éxito internacional con el disco «Buena Vista Social Club». El guitarrista estadounidense Ry Cooder y el productor británico Nick Gold lo grabaron en La Habana con músicos cubanos mayores, como Compay Segundo, Rubén González, Ibrahim Ferrer y Omara Portuondo. El disco salió en 1997, y en 1999 el director alemán Wim Wenders hizo un documental con el mismo nombre.'],
 [('Where was the son born, according to the text?',['En el este de la isla, en la región de Santiago de Cuba.','En La Habana, en los años veinte.','En las islas Canarias, en el siglo XIX.'],'The second paragraph says the son was born in the east.'),
  ('What did Sergio do in «Memorias del subdesarrollo»?',['No quiso irse de Cuba con su familia.','Fundó el ICAIC en 1959.','Grabó un disco con Ry Cooder.'],'The fourth paragraph describes the protagonist.'),
  ('Who recorded the album «Buena Vista Social Club», according to the text?',['Ry Cooder y Nick Gold, con músicos cubanos mayores.','Wim Wenders, con músicos alemanes.','Silvio Rodríguez y Pablo Milanés.'],'The last paragraph names the album\'s makers.')])
print(s,n)

# ---------- 05
s='b2-cuba-05'
lesson(s,'From the Special Period to today: crisis, reforms and emigration',
 'Tell the economic history of Cuba since 1991 with por más que, and say who gives which explanation.',
 'concessive clauses with por mas que and subjunctive',
 ['In this lesson you read about Cuba since 1991: the loss of Soviet support, the Special Period, the rafters of 1994, the thaw of 2014, the unified currency of 2021 and the situation in 2026. Cuban politics is disputed, so the text gives dated facts and says who explains what.',
  'The grammar is one you know: *por más que* for "however much". '+TAIL],
 ['I can say that nothing changes however much something happens, with *por más que* and *por mucho que*.',
  'I can say what the Special Period was and when the Soviet Union ended.',
  'I can use the new words for blackouts, shortages and rafts.'])
write_gr(s,None,'However Much: Por Más Que',[
 T('You know *por más que* "however much, no matter how much" from B2 Unit 8. It takes the subjunctive when the effort or amount is open and does not change the result (*Por más que insistas, no voy a cambiar de idea*). When you tell what really happened, you may read the indicative (*Por más que insistió, no consiguió nada*). Cuba\'s recent history is a series of efforts and results, so it is easy to apply.','What you already know'),
 TB('Por más que, open or real',[
  ('Por más que cambien las leyes, la vida diaria no mejorará de un día para otro.','open and general: subjunctive'),
  ('Por más que crezca el turismo, el país seguirá necesitando combustible.','open, looking ahead: subjunctive'),
  ('Por más que se abrió al turismo, el país siguió pasando años difíciles.','it really happened: indicative'),
  ('Por más que el viaje era peligroso, miles de personas salieron en balsas en 1994.','a real fact: indicative')]),
 EX([('Por más que cambien las leyes, la vida diaria no mejorará de un día para otro.','However much the laws change, daily life will not get better overnight.'),
     ('Por más que crezca el turismo, el país seguirá necesitando combustible.','However much tourism grows, the country will still need fuel.'),
     ('Por más que se abrió al turismo, el país siguió pasando años difíciles.','However much it opened to tourism, the country went on through difficult years.'),
     ('Por más que el viaje era peligroso, unas treinta y cinco mil personas salieron en balsas en 1994.','Although the journey was dangerous, about thirty-five thousand people left on rafts in 1994.')]),
 TIP('Use the subjunctive when you look ahead or speak in general, and the indicative when you say what really happened. The main clause often says that nothing changes: *no*, *seguirá*, *siguió*. *Por mucho que* works in the same way.')])
write_voc(s,None,'Crisis and emigration','Blackouts, shortages, rafts',[
 ('el apagón','blackout, power cut','noun'),('la escasez','shortage','noun'),('la balsa','raft','noun'),('la divisa','foreign currency','noun')])
write_ex(s,[
 match(s+'.ex01',[('el apagón','blackout, power cut'),('la escasez','shortage'),('la balsa','raft'),('la divisa','foreign currency')],V),
 mc(s+'.ex02','Which sentence says "However much the laws change, daily life will not get better overnight"?',
  ['Por más que cambien las leyes, la vida diaria no mejorará de un día para otro.','Por más que cambiarán las leyes, la vida diaria no mejorará de un día para otro.','Por más que cambiaran las leyes, la vida diaria no mejorará de un día para otro.'],teaches='concesivas-por-mas-que'),
 fill(s+'.ex03','Por más que __ el turismo, el país seguirá necesitando combustible.','crezca','However much tourism grows, the country will still need fuel.','concesivas-por-mas-que',hint='crecer'),
 build(s+'.ex04','Por más que se abrió al turismo, el país siguió pasando años difíciles.','However much it opened to tourism, the country went on through difficult years.','concesivas-por-mas-que'),
 dlg(s+'.ex05','¿Qué fue el período especial?','','Ahora lo entiendo.',
  ['Fue la crisis económica de los años noventa en Cuba.','Fue la campaña de alfabetización de 1961, con cien mil jóvenes.','Fue la guerra de independencia que empezó en 1895.'],V),
 dict_(s+'.ex06','Por más que el viaje era peligroso, unas treinta y cinco mil personas salieron en balsas en 1994.','Although the journey was dangerous, about thirty-five thousand people left on rafts in 1994.','concesivas-por-mas-que')])
n=story(s,'Del período especial a la crisis actual','Since the Soviet Union ended in 1991 Cuba has gone through the Special Period, the rafters of 1994, the thaw and its end, the monetary reform and protests of 2021, and a new energy crisis in 2026, with different explanations given by the government and its critics.',[
 'En 1991 la Unión Soviética se disolvió, y Cuba perdió a su principal socio comercial. La economía cayó con fuerza: según las estimaciones más citadas, el producto interior bruto bajó un treinta y cinco por ciento entre 1989 y 1993. El gobierno llamó a esa etapa el «período especial». Faltaban combustible, alimentos y electricidad, había apagones largos y mucha gente empezó a moverse en bicicleta por La Habana.',
 'En 1993 se permitió tener dólares, y el país se abrió más al turismo y a la inversión extranjera. Por más que se abrió al turismo, los años noventa siguieron siendo muy difíciles para muchas familias. En agosto de 1994, después de unas protestas en el Malecón de La Habana, unas treinta y cinco mil personas salieron de la isla en balsas hacia Estados Unidos. Después, los dos países firmaron acuerdos migratorios.',
 'En diciembre de 2014 los presidentes Barack Obama y Raúl Castro anunciaron un acercamiento entre los dos países, y Obama visitó La Habana en 2016. Con el gobierno estadounidense siguiente, Estados Unidos aplicó más de doscientas cuarenta nuevas medidas contra Cuba, y la pandemia de 2020 redujo el turismo.',
 'En 2021 se unificó la moneda cubana, y subió la inflación. El 11 de julio de 2021 hubo manifestaciones en muchas ciudades, que según muchos observadores fueron las más extensas en décadas. El gobierno acusó a Estados Unidos de promover las protestas; organizaciones de derechos humanos criticaron las detenciones y los juicios posteriores. Desde 2021, según distintas estimaciones, cientos de miles de cubanos han emigrado.',
 'En enero de 2026, según la prensa internacional, se detuvieron los envíos de petróleo desde Venezuela, y desde entonces ha habido varios apagones en todo el país. El gobierno cubano atribuye la crisis principalmente al embargo estadounidense; otros analistas señalan también problemas de la economía cubana. Por más que discrepen sobre las causas, los dos reconocen que faltan combustible y electricidad.'],
 [('What happened to Cuba\'s economy between 1989 and 1993, according to the most-cited estimates?',['El producto interior bruto bajó un treinta y cinco por ciento.','El turismo creció con fuerza.','La economía se recuperó con ayuda soviética.'],'The first paragraph gives the estimate.'),
  ('What happened in August 1994?',['Unas treinta y cinco mil personas salieron de la isla en balsas.','Obama visitó La Habana.','Se unificó la moneda cubana.'],'The second paragraph describes the rafters.'),
  ('How does the Cuban government explain the crisis of 2026, according to the text?',['Lo atribuye principalmente al embargo estadounidense.','Lo atribuye a la pandemia de 2020.','Lo atribuye a la disolución de la Unión Soviética.'],'The last paragraph reports the government\'s explanation.')])
print(s,n)

# ---------- consolidation
s='b2-cuba-consolidation'
lesson(s,'Cuba: Unit Review','Review Havana and Viñales, José Martí, the revolution and the literacy campaign, Cuban music and film, and Cuba since 1991, with the grammar you used to talk about them.',
 'review: stance adverbs, reported speech, conditions without si, verbs that change meaning, por más que',
 [],[],
 ['I can show my attitude to a fact with stance adverbs such as *lamentablemente* and *en rigor*.',
  'I can report what someone said or wrote, shifting the tenses.',
  'I can state a condition without *si*, with *de* + infinitive or the gerund.',
  'I can use *conocí*, *supe*, *quise* and *pude* for events and *conocía*, *sabía*, *quería* and *podía* for states.',
  'I can talk about Cuba\'s crises with *por más que*, saying who explains what.'])
p=R+'lessons/b2/b2-cuba-consolidation.json'; d=rj(p)
for sec in d['sections']:
    if sec['type']=='goal': sec['items']=['I can review what I learned about Cuba, from Havana to today.','I can use stance adverbs, reported speech, conditions without *si*, the verbs that change meaning and *por más que*.','I can put events from 1895 to 1994 in order.','I can say who gives which explanation when a matter is disputed.']
wj(p,d)
ords=['La Habana colonial resguarda fortalezas de piedra y plazas históricas. [Colonial Havana keeps stone fortresses and historic squares.]',
 'En 1895 murió José Martí en Dos Ríos. [In 1895 José Martí died at Dos Ríos.]',
 'En 1961 terminó la campaña de alfabetización. [In 1961 the literacy campaign ended.]',
 'En 1994 miles de personas salieron de Cuba en balsas. [In 1994 thousands of people left Cuba on rafts.]']
ex_order={'id':s+'.ex05','type':'sentence-order','category':'grammar','sentences':ords,'solution':[0,1,2,3],'teaches':['preterito-indefinido']}
ex_wr={'id':s+'.ex08','type':'structured-writing','category':'writing','template':[
 {'prompt':'Say that the guide said that the mogotes were limestone hills. Start with "La guía dijo que".','answer':'La guía dijo que los mogotes eran colinas de roca caliza.'},
 {'prompt':'Say that Martí wrote that he wanted the independence of Cuba. Start with "Martí escribió que".','answer':'Martí escribió que quería la independencia de Cuba.'}],'teaches':['estilo-indirecto']}
write_ex(s,[
 match(s+'.ex01',[('la fortaleza','fortress'),('el campesino','peasant, farmer'),('el trovador','troubadour, singer-songwriter'),('el apagón','blackout, power cut')],V),
 mc(s+'.ex02','Which sentence says "Strictly speaking, Martí was born in Havana"?',['En rigor, Martí nació en La Habana.','Con rigor, Martí nació en La Habana.','Por rigor, Martí nació en La Habana.'],teaches='stance-adverbs'),
 fill(s+'.ex03','Carlos dijo que Martí __ nacido en La Habana en 1853.','había','Carlos said that Martí had been born in Havana in 1853.','estilo-indirecto'),
 fill(s+'.ex04','De __ necesario, los jóvenes se quedaban a vivir con las familias del campo.','ser','If necessary, the young people stayed to live with the country families.','implicit-conditionals'),
 ex_order,
 mc(s+'.ex06','Which sentence says "The director found out the news yesterday"?',['El director supo la noticia ayer.','El director sabía la noticia ayer.','El director sabe la noticia ayer.'],teaches='verbos-cambio-significado-pasado'),
 mc(s+'.ex07','According to the texts, what happened on 22 December 1961?',['Terminó la campaña de alfabetización.','Empezó la campaña de alfabetización.','Murió José Martí en Dos Ríos.'],cat='reading'),
 ex_wr])
