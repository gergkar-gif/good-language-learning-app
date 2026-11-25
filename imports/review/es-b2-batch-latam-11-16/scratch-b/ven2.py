import sys, json; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-venezuela-llanos-diaspora-vocab'
P='b2-venezuelasabana'
L={}

L['01']=dict(
 title='The Llanos and the joropo: cattle, rivers and music',
 goal="Describe the Llanos, the llanero and the joropo with relative clauses (que, quien, donde, cuyo).",
 grammar_label='relative clauses with que, quien, donde and cuyo',
 goal_items=["I can describe a person, a thing or a place with *que*, *quien* and *donde*.",
  "I can say what the Llanos are and what instruments the joropo uses.",
  "I can use the new words for plain, cowboy, harp and cattle."],
 screen=screen('x','Who, Which, Where: Describing the Llanos',
  "You know *que*, *quien* and *donde* from B1 Unit 5: relative clauses, with *que* and *quien* for people and things, *donde* for places, and *cuyo* for \"whose\". They let you add information about a noun without starting a new sentence. The llanero, the joropo and the plains are easy to describe this way.",
  'Relative clauses on this topic',
  [("El llanero es el hombre que cuida el ganado a caballo.","*que*: the man who looks after the cattle"),
   ("El joropo es la música que se baila en los Llanos.","*que* for a thing"),
   ("Los Llanos son la región donde viven los llaneros.","*donde* for a place"),
   ("El joropo, cuyos instrumentos son el arpa, el cuatro y las maracas, es música de baile.","*cuyos* agrees with *instrumentos*, the thing owned")],
  [("El llanero es el hombre que cuida el ganado a caballo.","The llanero is the man who looks after the cattle on horseback."),
   ("El joropo es la música que se baila en los Llanos.","The joropo is the music that is danced in the Llanos."),
   ("Los Llanos son la región donde viven los llaneros.","The Llanos are the region where the llaneros live."),
   ("Pedro Elías Gutiérrez, quien compuso «Alma llanera», es conocido en todo el país.","Pedro Elías Gutiérrez, who composed \"Alma llanera\", is known throughout the country.")],
  "*Que* is the all-round relative pronoun for people and things; *quien* needs a person and often follows a comma or a preposition (*con quien*); *donde* needs a place. Choose by the role of the pronoun in its own clause: *los Llanos, donde viven los llaneros*, never *los Llanos, que viven los llaneros*."),
 vocab_title='The Llanos: plain, cowboy and harp',
 vocab_theme='Cattle, joropo and the plains of the Orinoco',
 vocab=[('llano','plain, flat grassland','noun'),('llanero','cowboy of the Llanos','noun'),('joropo','joropo (music and dance of the Llanos)','noun'),('arpa','harp','noun'),('ganado','cattle','noun'),('cuatro','cuatro (small four-string guitar)','noun')],
 exercises=[
  match('E.ex01',[('el llano','flat grassland'),('el llanero','cowboy of the plains'),('el joropo','music and dance of the Llanos'),('el arpa','harp')],V),
  fb('E.ex02','El llanero es el hombre __ cuida el ganado a caballo.','que','The llanero is the man who looks after the cattle on horseback.','relative-clauses'),
  mc('E.ex03','Which sentence means "The Llanos are the region where the llaneros live"?',['Los Llanos son la región donde viven los llaneros.','Los Llanos son la región que viven los llaneros.','Los Llanos son la región quien viven los llaneros.'],'relative-clauses'),
  sb('E.ex04','El joropo es la música que se baila en los Llanos.','The joropo is the music that is danced in the Llanos.','relative-clauses'),
  dlg('E.ex05',[('Meg','¿Qué es un llanero?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es una persona que trabaja con el ganado en los Llanos.','Es un instrumento que suena en las fiestas.','Es un río grande que cruza los Llanos.'],V),
  dic('E.ex06','El arpa es el instrumento que se oye en el joropo.','The harp is the instrument that you hear in the joropo.','relative-clauses'),
  reading('E.ex07','Which instruments does the joropo use, according to the text?',['El arpa, el cuatro y las maracas.','El piano, el violín y la guitarra eléctrica.','La marimba, la flauta y el tambor.']),
 ],
 story=dict(title='Los Llanos y el joropo',
  summary="The Llanos are the great plains of the Orinoco basin, where cattle ranching, the llanero and the joropo, played with harp, cuatro and maracas, are the best-known traditions.",
  paras=[
  "Los Llanos son las grandes llanuras del río Orinoco, en varios estados de Venezuela, como Apure, Barinas y Guárico, y también en Colombia. Es una región casi plana, con pocos árboles. El año tiene dos épocas: en la estación de lluvias, de mayo a noviembre, muchos ríos se desbordan y grandes zonas quedan bajo el agua; en la estación seca, de diciembre a abril, la tierra se seca.",
  "La actividad más tradicional de los Llanos es la ganadería. El llanero es el hombre que cuida el ganado a caballo, y su vida ha dado muchas canciones y muchas historias. Los llaneros también lucharon en las guerras de independencia, bajo el mando de José Antonio Páez.",
  "El joropo es la música más conocida de los Llanos. Se toca con el arpa, con el cuatro, que es una guitarra pequeña de cuatro cuerdas, y con las maracas. Se baila en pareja, con un zapateado muy rápido.",
  "«Alma llanera», compuesta por Pedro Elías Gutiérrez en 1914, es una de las canciones más populares del país, y muchos venezolanos la consideran un segundo himno.",
  "En 2017 la UNESCO incluyó los cantos de trabajo de los Llanos de Colombia y de Venezuela en su lista del patrimonio cultural inmaterial. Son canciones que acompañan el trabajo con el ganado, y que los llaneros cantan mientras trabajan."],
  qs=[("When does the rainy season last in the Llanos, according to the text?",["De mayo a noviembre.","De diciembre a abril.","Todo el año."],"The first paragraph gives the months."),
      ("Who is the llanero?",["Es el hombre que cuida el ganado a caballo.","Es el músico que toca el arpa en la ciudad.","Es el gobernador del estado Apure."],"The second paragraph defines him."),
      ("What happened in 2017, according to the text?",["La UNESCO incluyó los cantos de trabajo de los Llanos en su lista del patrimonio inmaterial.","Pedro Elías Gutiérrez compuso «Alma llanera».","José Antonio Páez fue presidente."],"The last paragraph gives the date.")]))

L['02']=dict(
 title='The Gran Sabana and Canaima: the kingdom of the tepuis',
 goal="Spotlight one idea about Canaima and Angel Falls with cleft sentences.",
 grammar_label='cleft sentences',
 goal_items=["I can spotlight a person, a place or a time with *Fue ... quien / donde / cuando* and *Lo que ... es*.",
  "I can say what a tepui is and who gave Angel Falls its current name.",
  "I can use the new words for tepui, waterfall and height."],
 screen=screen('x','In the Spotlight: Canaima',
  "You know *lo que* and cleft sentences from B2 Unit 1: they split one idea into two halves joined by *ser*, so that the piece you want to stress lands in the spotlight. You know *lo que* from B1 Unit 20. Canaima, with its tepuis and its famous waterfall, gives you something to stress in every sentence.",
  'Cleft sentences on this topic',
  [("Lo que más impresiona es la altura de la cascada.","*lo que* + verb + *ser*: spotlights a thing"),
   ("Fue el piloto Jimmie Angel quien sobrevoló la cascada en 1933.","*fue ... quien*: spotlights who did it"),
   ("Es en Canaima donde está el Salto Ángel.","*es ... donde*: spotlights the place"),
   ("Fue en 1994 cuando la UNESCO declaró Canaima Patrimonio de la Humanidad.","*fue ... cuando*: spotlights the time")],
  [("Lo que más impresiona de Canaima son los tepuyes.","What impresses most about Canaima is the tepuis."),
   ("Fue el piloto Jimmie Angel quien sobrevoló la cascada en 1933.","It was the pilot Jimmie Angel who flew over the waterfall in 1933."),
   ("Es en Canaima donde está el Salto Ángel.","It is in Canaima that Angel Falls is."),
   ("Fue en 1994 cuando la UNESCO declaró Canaima Patrimonio de la Humanidad.","It was in 1994 that UNESCO declared Canaima a World Heritage site.")],
  "The tense of *ser* follows the time of the other verb: *Fue ... quien sobrevoló* (past), *Es ... donde está* (present). With a plural spotlight, careful writing makes *ser* agree: *Lo que impresiona son los tepuyes*. Use a cleft sentence for the one idea you want to be remembered, not in every sentence."),
 vocab_title='Canaima: tepui, waterfall and height',
 vocab_theme='The Gran Sabana, tepuis and Angel Falls',
 vocab=[('tepuy','tepui, flat-topped mountain with steep walls','noun'),('cascada','waterfall','noun'),('sabana','savanna, open grassland','noun'),('altura','height','noun'),('piloto','pilot','noun'),('pemón','Pemón (an indigenous people of the Gran Sabana)','noun')],
 exercises=[
  match('E.ex01',[('el tepuy','flat-topped mountain'),('la cascada','waterfall'),('la sabana','open grassland'),('la altura','height')],V),
  fb('E.ex02','Lo que más impresiona __ la altura de la cascada.','es','What impresses most is the height of the waterfall.','oraciones-hendidas-enfasis'),
  mc('E.ex03','Which sentence means "It was the pilot Jimmie Angel who flew over the waterfall in 1933"?',['Fue el piloto Jimmie Angel quien sobrevoló la cascada en 1933.','Es el piloto Jimmie Angel quien sobrevoló la cascada en 1933.','Fue el piloto Jimmie Angel donde sobrevoló la cascada en 1933.'],'oraciones-hendidas-enfasis',ds={1:'present-tense'}),
  sb('E.ex04','Fue en 1994 cuando la UNESCO declaró Canaima Patrimonio de la Humanidad.','It was in 1994 that UNESCO declared Canaima a World Heritage site.','oraciones-hendidas-enfasis'),
  dlg('E.ex05',[('Meg','¿Qué es un tepuy?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es una montaña con la cima plana y paredes muy altas.','Es una cascada muy alta que cae desde una nube.','Es un río grande que cruza la sabana.'],V),
  dic('E.ex06','Lo que más impresiona de Canaima son los tepuyes.','What impresses most about Canaima is the tepuis.','oraciones-hendidas-enfasis'),
  reading('E.ex07','What is the Pemón name of Angel Falls, according to the text?',['Kerepakupai Merú.','Cascada del Orinoco.','Salto de Roraima.']),
 ],
 story=dict(title='La Gran Sabana y Canaima',
  summary="The Gran Sabana and Canaima National Park, a UNESCO site since 1994, are known for their tepuis and for Angel Falls, called Kerepakupai Merú by the Pemón.",
  paras=[
  "La Gran Sabana, en el sureste de Venezuela, es una región de sabanas abiertas y de montañas con la cima plana, los tepuyes. El Parque Nacional Canaima, en el estado Bolívar, protege una gran parte de esa región. Es muy grande: ocupa unos treinta mil kilómetros cuadrados. La UNESCO lo declaró Patrimonio de la Humanidad en 1994.",
  "Los tepuyes son formaciones de roca muy antiguas, de más de mil millones de años. Tienen paredes casi verticales, y algunos superan los dos mil metros de altura. Como están tan aislados, en sus cimas viven plantas y animales que casi no existen en otros lugares. El monte Roraima, de más de dos mil ochocientos metros, está en la frontera entre Venezuela, Brasil y Guyana.",
  "En el Auyán-tepuy está el Salto Ángel, la cascada más alta del mundo, con 979 metros de altura. Su nombre indígena es Kerepakupai Merú. El nombre actual viene de Jimmie Angel, un piloto estadounidense que sobrevoló la cascada en 1933 y aterrizó en la cima del Auyán-tepuy en 1937. Los indígenas de la región ya la conocían mucho antes.",
  "Los pemones son el pueblo indígena que vive desde hace mucho tiempo en la Gran Sabana. Los tepuyes forman parte de sus historias y de su tradición. Hoy muchos pemones trabajan como guías para los visitantes que llegan a Canaima."],
  qs=[("In which year did UNESCO declare Canaima a World Heritage site?",["En 1994.","En 1933.","En 1937."],"The first paragraph gives the year."),
      ("What is Angel Falls, according to the text?",["Es la cascada más alta del mundo.","Es el tepuy más alto de Venezuela.","Es un río de los Llanos."],"The third paragraph describes it."),
      ("Where does the current name of Angel Falls come from?",["De Jimmie Angel, un piloto estadounidense.","De un presidente venezolano.","De un explorador alemán."],"The third paragraph explains the name.")]))

L['03']=dict(
 title='Hyperinflation and the economic crisis: causes and disputes',
 goal="Explain the causes of Venezuela's crisis with debido a and a raíz de, and say whose explanation it is.",
 grammar_label='formal cause connectors: debido a and a raíz de',
 goal_items=["I can give a cause with *debido a* or *a raíz de* followed by a noun.",
  "I can say what the government and its critics each give as the causes of the crisis.",
  "I can use the new words for inflation, wage and shortage."],
 screen=screen('x','Because Of: The Causes of a Crisis',
  "You know *debido a* and *a raíz de* from B1 Unit 6: formal ways to say \"because of\" and \"as a result of\", always followed by a noun. They are useful for the Venezuelan crisis, but only if you say whose explanation you give: the government and its critics do not agree on the causes.",
  'Cause and consequence',
  [("Debido a la caída del precio del petróleo, los ingresos del país bajaron.","*debido a* + noun; the consequence follows"),
   ("A raíz de las sanciones, según el gobierno, bajó la producción.","*a raíz de* + noun, with the source named"),
   ("Debido a la inflación, los salarios compraban cada vez menos.","*debido a* + noun"),
   ("Los salarios compraban menos porque los precios subían.","with a verb (*subían*) use *porque*")],
  [("Debido a la caída del precio del petróleo en 2014, los ingresos del país bajaron.","Because of the fall in the oil price in 2014, the country's income fell."),
   ("A raíz de las sanciones, según el gobierno, bajó la producción de petróleo.","As a result of the sanctions, according to the government, oil production fell."),
   ("Según los críticos, debido al control de precios, faltaron productos.","According to the critics, because of price controls, goods were missing."),
   ("Debido a la inflación, los salarios compraban cada vez menos.","Because of inflation, wages bought less and less.")],
  "*Debido a* and *a raíz de* take a noun: *debido a la inflación*. If you want a verb, use *porque*. On a disputed topic, put the source next to the cause: *según el gobierno*, *según los críticos*."),
 vocab_title='The crisis: inflation, wages and shortage',
 vocab_theme='Hyperinflation and the economic crisis in Venezuela',
 vocab=[('inflación','inflation','noun'),('salario','wage, pay','noun'),('escasez','shortage','noun'),('sanción','sanction, penalty imposed by one country on another','noun'),('bolívar','bolívar (Venezuelan currency)','noun'),('caída','fall, drop','noun')],
 exercises=[
  match('E.ex01',[('la inflación','rise in prices'),('el salario','money a worker is paid'),('la escasez','shortage'),('la sanción','penalty imposed by one country on another')],V),
  fb('E.ex02','__ a la caída del precio del petróleo en 2014, los ingresos del país bajaron.','Debido','Because of the fall in the oil price in 2014, the country\'s income fell.','formal-cause-connectors',hint='because of'),
  mc('E.ex03','Which sentence means "Because of the shortage, prices rose"?',['Debido a la escasez, los precios subieron.','Debido a hubo escasez, los precios subieron.','Porque la escasez, los precios subieron.'],'formal-cause-connectors'),
  sb('E.ex04','A raíz de las sanciones, según el gobierno, bajó la producción de petróleo.','As a result of the sanctions, according to the government, oil production fell.','formal-cause-connectors'),
  dlg('E.ex05',[('Meg','¿Qué es la escasez?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es cuando hay muy pocos productos y mucha gente los quiere.','Es cuando los precios bajan mucho en todas las tiendas.','Es cuando el gobierno sube el salario a todos.'],V),
  dic('E.ex06','Debido a la inflación, el bolívar perdía valor cada día.','Because of inflation, the bolívar lost value every day.','formal-cause-connectors'),
  reading('E.ex07','What does the government say about the causes of the crisis, according to the text?',['Dice que la causa principal son las sanciones.','Dice que la causa principal es la corrupción.','Dice que no hubo una crisis económica.']),
 ],
 story=dict(title='La crisis económica y la hiperinflación',
  summary="After the fall of the oil price in 2014 Venezuela went through a deep crisis with hyperinflation; the government blames sanctions, its critics blame economic policy and corruption, and in 2026 the political situation changed.",
  paras=[
  "Según los datos de la OPEP, Venezuela tiene las mayores reservas de petróleo del mundo. Pero en 2014 bajó el precio internacional del petróleo, y los ingresos del país cayeron. A raíz de esa caída, la economía entró en una crisis muy fuerte: bajó la producción, faltaron alimentos y medicinas, y los precios subieron muy rápido.",
  "La inflación fue tan alta que se habló de hiperinflación: en 2018 superó el cien mil por ciento, según el Banco Central. En agosto de 2018 el gobierno quitó cinco ceros al bolívar. A partir de 2019, mucha gente empezó a usar dólares en los comercios, y la economía se dolarizó en parte.",
  "Las causas son discutidas. El gobierno de Nicolás Maduro dice que la crisis se debe sobre todo a las sanciones económicas de Estados Unidos, que afectaron al sistema financiero desde 2017 y a la petrolera PDVSA desde 2019. Sus críticos, entre ellos muchos economistas y la oposición, dicen que la crisis empezó antes de las sanciones y que se debe al control de precios y de cambio, a la corrupción y a la mala gestión de PDVSA.",
  "Debido a la crisis, según organizaciones humanitarias, el salario de muchas personas perdió casi todo su valor, y muchas familias dependieron de ayudas, de dinero enviado desde el extranjero y de pequeños trabajos.",
  "En 2026 la situación política cambió: el 3 de enero fuerzas de Estados Unidos capturaron a Nicolás Maduro, y desde entonces Delcy Rodríguez gobierna como presidenta encargada. Ella ha prometido elecciones, pero todavía sin fecha."],
  qs=[("What fell in 2014, according to the text?",["El precio internacional del petróleo.","La producción de café.","El número de turistas."],"The first paragraph says so."),
      ("What does the government say about the causes of the crisis?",["Que se debe sobre todo a las sanciones de Estados Unidos.","Que se debe a la corrupción del gobierno.","Que no hubo ninguna crisis."],"The third paragraph gives its view."),
      ("What do the critics say?",["Que la crisis empezó antes de las sanciones y se debe a la política económica y a la corrupción.","Que las sanciones fueron la única causa.","Que el petróleo no tiene importancia."],"The third paragraph gives their view.")]))

L['04']=dict(
 title='The exodus: millions of Venezuelans abroad',
 goal="Report figures and statements with their source, using según and verbs such as informar de que and explicar que.",
 grammar_label='reporting information and citing sources',
 goal_items=["I can give the source of a statement with *según* and report it with *informó de que* or *explica que*.",
  "I can say how many Venezuelans live abroad, according to UNHCR, and in which year.",
  "I can use the new words for exodus, migrant, refugee and border."],
 screen=screen('x','Citing the Source: The Exodus',
  "You know *según* and how to report information from B1 Unit 13: *según* + the source, *informar de que* and *explicar que*. They separate what a source says from your own opinion. Figures about migration change from year to year and depend on who counts, so every figure needs its source and its date.",
  'Naming the source',
  [("Según ACNUR, unos 7,9 millones de venezolanos vivían fuera del país a finales de 2025.","*según* + source, with the date"),
   ("ACNUR informó de que muchas personas salieron del país.","*informar de que* + statement"),
   ("ACNUR explica que muchas personas salieron por la crisis.","*explicar que* + statement"),
   ("Según los testigos, el viaje fue largo.","*según* also works with people as the source")],
  [("Según ACNUR, unos 7,9 millones de venezolanos vivían fuera del país a finales de 2025.","According to UNHCR, about 7.9 million Venezuelans lived outside the country at the end of 2025."),
   ("ACNUR informó de que muchas personas salieron del país.","UNHCR reported that many people left the country."),
   ("Según ACNUR, Colombia es el país que más personas venezolanas ha recibido.","According to UNHCR, Colombia is the country that has received the most Venezuelans."),
   ("ACNUR explica que muchas personas salieron por la crisis económica.","UNHCR explains that many people left because of the economic crisis.")],
  "Keep the source and your own view apart. *Según ACNUR* tells the reader that the figure is ACNUR's; add the date, because the number changes. After *informó de que* and *explica que* the statement is a full clause; do not drop the *que* (*informó de que muchas personas salieron*)."),
 vocab_title='The exodus: migrants, refugees and borders',
 vocab_theme='Venezuelan migration abroad',
 vocab=[('éxodo','exodus, mass departure','noun'),('migrante','migrant','noun'),('refugiado','refugee','noun'),('frontera','border','noun'),('cifra','figure, number','noun'),('acoger','to take in, to host','verb')],
 exercises=[
  match('E.ex01',[('el éxodo','mass departure of people'),('el migrante','person who moves to another country'),('el refugiado','person who flees from danger'),('la frontera','border')],V),
  fb('E.ex02','__ ACNUR, unos 7,9 millones de venezolanos vivían fuera del país a finales de 2025.','Según','According to UNHCR, about 7.9 million Venezuelans lived outside the country at the end of 2025.','estilo-indirecto-informacion',hint='according to'),
  mc('E.ex03','Which sentence means "UNHCR reported that many people left the country"?',['ACNUR informó de que muchas personas salieron del país.','ACNUR informó de muchas personas salieron del país.','ACNUR informó a que muchas personas salieron del país.'],'estilo-indirecto-informacion'),
  sb('E.ex04','ACNUR explica que los países que acogen a muchas personas necesitan apoyo.','UNHCR explains that the countries that host many people need support.','estilo-indirecto-informacion'),
  dlg('E.ex05',[('Meg','¿Qué es un refugiado?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es una persona que sale de su país para buscar protección.','Es una persona que viaja a otro país solo de vacaciones.','Es una persona que trabaja en la frontera de su país.'],V),
  dic('E.ex06','Según ACNUR, la cifra de personas venezolanas fuera del país es muy alta.','According to UNHCR, the number of Venezuelans outside the country is very high.','estilo-indirecto-informacion'),
  reading('E.ex07','Which country created a temporary protection status for Venezuelans in 2021, according to the text?',['Colombia, en febrero de 2021.','Perú, en febrero de 1990.','Chile, en marzo de 1980.']),
 ],
 story=dict(title='El éxodo venezolano',
  summary="According to UNHCR about 7.9 million Venezuelans were living abroad at the end of 2025, most of them in Latin American countries such as Colombia, which created a temporary protection status in 2021.",
  paras=[
  "Desde 2014, millones de venezolanos han salido de su país. Según ACNUR, la agencia de la ONU para los refugiados, a finales de 2025 había unos 7,9 millones de venezolanos fuera de Venezuela. Según la misma agencia, Colombia es el país que más personas venezolanas ha recibido, seguido de Perú. Brasil, Chile y Ecuador también han recibido a muchas personas.",
  "ACNUR y otras organizaciones explican que muchas personas salieron por la crisis económica, la falta de alimentos y de medicinas, y la inseguridad. Otras salieron por razones políticas. Sobre las causas de la crisis hay desacuerdo: el gobierno venezolano culpa a las sanciones, y sus críticos culpan a la política económica.",
  "Muchas personas viajaron en autobús, pero otras caminaron durante días por las carreteras de Colombia, incluso por zonas frías de montaña, porque no tenían dinero para el pasaje.",
  "En febrero de 2021 Colombia creó el Estatuto Temporal de Protección para Migrantes Venezolanos, que permite a muchas personas vivir y trabajar legalmente en el país durante diez años.",
  "ACNUR informó de que los países que acogen a tantas personas necesitan más apoyo internacional. Al mismo tiempo, esas comunidades de migrantes han cambiado las ciudades donde viven, con nuevos comercios, restaurantes y trabajos."],
  qs=[("According to UNHCR, how many Venezuelans were living abroad at the end of 2025?",["Unos 7,9 millones.","Unos 79 mil.","Unos 790 millones."],"The first paragraph gives the figure."),
      ("Which country has received the most Venezuelans, according to the same agency?",["Colombia.","España.","Cuba."],"The first paragraph names it."),
      ("What did Colombia create in February 2021?",["El Estatuto Temporal de Protección para Migrantes Venezolanos.","Una frontera nueva con Venezuela.","Un museo de la migración."],"The fourth paragraph says so.")]))

L['05']=dict(
 title='The diaspora: Venezuelan culture around the world',
 goal="Express wishes about the past with ojalá and the pluperfect subjunctive, using the Venezuelan diaspora as the topic.",
 grammar_label='past wishes with ojalá + pluperfect subjunctive',
 goal_items=["I can express a wish about the past with *ojalá* + *hubiera* and a participle.",
  "I can say how arepas and the orchestras of El Sistema travelled with Venezuelans.",
  "I can use the new words for arepa, flour and orchestra."],
 screen=screen('x','If Only: Wishes About the Past',
  "You know *ojalá* with the pluperfect subjunctive from B2 Unit 16: *Ojalá hubiera estudiado más*, \"I wish I had studied more\". It is a wish about something that did not happen, so it can no longer come true. People who live far from home use it often, and so does anyone who thinks back on a decision.",
  'Ojalá + pluperfect subjunctive',
  [("Ojalá hubiera podido quedarme con mi familia.","I wish I had been able to stay with my family."),
   ("Ojalá hubiéramos llevado más harina.","I wish we had taken more flour."),
   ("Ojalá no hubieras tenido que irte.","I wish you had not had to leave."),
   ("¡Quién hubiera podido volver antes!","If only I had been able to come back earlier!")],
  [("Ojalá hubiera podido quedarme con mi familia.","I wish I had been able to stay with my family."),
   ("Ojalá hubiéramos llevado más harina.","I wish we had taken more flour."),
   ("Ojalá hubiera salido antes.","I wish I had left earlier."),
   ("¡Quién hubiera podido volver antes!","If only I had been able to come back earlier!")],
  "Use *hubiera* (or *hubiese*), never *habría*, after *ojalá*: *Ojalá hubiera venido*, not *Ojalá habría venido*. A wish about the past is always a regret. These sentences express a feeling: they do not say what really happened."),
 vocab_title='The diaspora: arepa, flour and orchestra',
 vocab_theme='Venezuelan food and music abroad',
 vocab=[('arepa','arepa (round maize bread)','noun'),('harina','flour','noun'),('extrañar','to miss (someone or something)','verb'),('orquesta','orchestra','noun'),('director','conductor, director','noun'),('maíz','maize, corn','noun')],
 exercises=[
  match('E.ex01',[('la arepa','round maize bread'),('la harina','flour'),('extrañar','to miss someone or something'),('la orquesta','orchestra')],V),
  fb('E.ex02','Ojalá __ podido quedarme con mi familia.',None,'I wish I had been able to stay with my family.','counterfactual-wishes',hint='haber',answers=['hubiera','hubiese']),
  mc('E.ex03','Which sentence means "I wish I had brought more flour"?',['Ojalá hubiera traído más harina.','Ojalá habría traído más harina.','Ojalá traiga más harina.'],'counterfactual-wishes',ds={2:'subjuntivo-deseos'}),
  sb('E.ex04','Ojalá hubiéramos llevado más harina.','I wish we had taken more flour.','counterfactual-wishes'),
  dlg('E.ex05',[('Meg','¿Quién es Gustavo Dudamel?'),('Carlos','_____'),('Meg','Ahora lo entiendo.')],['Es un director de orquesta nacido en Barquisimeto.','Es el ingeniero que inventó la harina de maíz.','Es la persona que empezó el programa El Sistema.'],V),
  dic('E.ex06','Ojalá hubiera podido ver a mi familia antes.','I wish I had been able to see my family earlier.','counterfactual-wishes'),
  reading('E.ex07','What did Luis Caballero Mejías invent, according to the text?',['Una harina de maíz para hacer arepas.','Un instrumento para tocar joropo.','Un programa de orquestas para jóvenes.']),
 ],
 story=dict(title='La diáspora venezolana y su cultura',
  summary="Venezuelans abroad have taken their arepas and their music with them, from precooked maize flour to the orchestras of El Sistema, while many feel the distance from their families.",
  paras=[
  "La migración ha cambiado también la cultura de los países adonde llegaron los venezolanos. En ciudades como Bogotá, Lima, Santiago, Madrid o Miami hay hoy restaurantes venezolanos, y la arepa se conoce en muchos países.",
  "La arepa es un pan redondo de maíz. Hacerla en casa se volvió mucho más fácil con la harina de maíz precocida, que el ingeniero Luis Caballero Mejías inventó en los años cincuenta. Hoy esa harina se vende en tiendas de muchos países.",
  "La música venezolana también viaja. El Sistema, un programa de orquestas y coros juveniles fundado por José Antonio Abreu en 1975, formó a miles de jóvenes músicos. Entre ellos está Gustavo Dudamel, nacido en Barquisimeto, que ha dirigido orquestas en muchos países.",
  "Para muchas personas, vivir lejos significa extrañar a la familia. Algunos migrantes dicen que ojalá hubieran podido quedarse en su país, y otros dicen que ojalá hubieran salido antes. Las opiniones son muy distintas, porque las historias de cada persona también lo son.",
  "Hoy, muchas familias tienen miembros en dos o más países, y se mantienen en contacto por teléfono y por internet. Algunas personas han regresado a Venezuela en los últimos años, y otras han decidido quedarse en los países que las acogieron."],
  qs=[("What is an arepa?",["Es un pan redondo de maíz.","Es una sopa de verduras.","Es un instrumento musical."],"The second paragraph defines it."),
      ("Who founded El Sistema, and when?",["José Antonio Abreu, en 1975.","Gustavo Dudamel, en 2017.","Luis Caballero Mejías, en 1950."],"The third paragraph gives both."),
      ("What do some migrants say, according to the text?",["Que ojalá hubieran podido quedarse en su país.","Que todos deberían volver a Venezuela.","Que nunca extrañan a su familia."],"The fourth paragraph reports it.")]))

L['consolidation']=dict(
 title='Review: the Llanos, Canaima, the crisis and the diaspora',
 goal="Review relative clauses, cleft sentences, cause connectors, reporting with según and past wishes on the themes of this unit.",
 goal_items=["I can use relative clauses, cleft sentences, cause connectors, *según* and *ojalá hubiera* about Venezuela.",
  "I can tell the Llanos, Canaima, the crisis, the exodus and the diaspora apart.",
  "I can read short Spanish texts about these topics and answer questions."],
 checklist_items=["I can describe a person, a thing or a place with *que*, *quien* and *donde*.",
  "I can spotlight one idea with a cleft sentence.",
  "I can give a cause with *debido a* and a source with *según*.",
  "I can express a wish about the past with *ojalá* and *hubiera*."],
 exercises=[
  match('E.ex01',[('el llanero','cowboy of the plains'),('el tepuy','flat-topped mountain'),('la escasez','shortage'),('el refugiado','person who flees from danger')],V),
  mc('E.ex02','Which sentence means "The joropo is the music that is played with the harp"?',['El joropo es la música que se toca con el arpa.','El joropo es la música donde se toca con el arpa.','El joropo es la música quien se toca con el arpa.'],'relative-clauses'),
  fb('E.ex03','Es en Canaima __ está el Salto Ángel.','donde','It is in Canaima that Angel Falls is.','oraciones-hendidas-enfasis'),
  fb('E.ex04','A __ de la crisis, millones de personas salieron del país.','raíz','As a result of the crisis, millions of people left the country.','formal-cause-connectors'),
  mc('E.ex05','Which sentence means "UNHCR explains that many people left"?',['ACNUR explica que muchas personas salieron.','ACNUR explica de muchas personas salieron.','ACNUR explica a que muchas personas salieron.'],'estilo-indirecto-informacion'),
  mc('E.ex06','Which sentence means "I wish we had left earlier"?',['Ojalá hubiéramos salido antes.','Ojalá habríamos salido antes.','Ojalá saliéramos antes.'],'counterfactual-wishes',ds={2:'imperfect-subjunctive-forms'}),
  reading('E.ex07','According to the texts, in which year did UNESCO declare Canaima a World Heritage site?',['Fue en 1994.','Fue en 2017.','Fue en 1975.']),
  sw('E.ex08',[('Say that you wish you had left earlier. Start with "Ojalá".','Ojalá hubiera salido antes.'),('Say that you wish you had been able to see your family. Start with "Ojalá".','Ojalá hubiera podido ver a mi familia.')],'counterfactual-wishes'),
 ])

spec=dict(pre=P,uid='venezuela-llanos-diaspora',lessons={})
for n,l in L.items():
    stem=f'{P}-{n}'
    for e in l['exercises']: e['id']=e['id'].replace('E',stem,1)
    spec['lessons'][n]=l
build_unit(spec)
print('built')

M=lambda t,sc,pr,cu,tg,en,cd: dict(tier='tier1',level='B2',title='Communicative Challenge: '+t,scenario=sc,prompt=pr,cues=cu,target=tg,english=en,canDo=cd)
c={}
g=lambda n: L[n]['goal_items'][0]
c[P+'-01']=M('Who Is a Llanero','You are Meg. You and Carlos are watching a documentary about the Llanos of Venezuela, and he asks what a llanero is.','Tell Carlos what a llanero is.',['Say that he is a man','Say what he does with the cattle'],'El llanero es el hombre que cuida el ganado a caballo.','The llanero is the man who looks after the cattle on horseback.',g('01'))
c[P+'-02']=M('Who Saw the Waterfall First','You are Carlos. You have read an article about Angel Falls, and Meg asks where its current name comes from.','Tell Meg who flew over the waterfall in 1933, stressing the person.',['Stress who did it','Say what he did and when'],'Fue el piloto Jimmie Angel quien sobrevoló la cascada en 1933.','It was the pilot Jimmie Angel who flew over the waterfall in 1933.',g('02'))
c[P+'-03']=M('Why Income Fell','You are Meg. You are telling Carlos what you read about the Venezuelan economy.','Tell Carlos why the income of the country fell, using a formal connector.',['Give the cause with a formal connector','Say what fell'],'Debido a la caída del precio del petróleo en 2014, los ingresos del país bajaron.',"Because of the fall in the oil price in 2014, the country's income fell.",g('03'))
c[P+'-04']=M('How Many Are Abroad','You are Carlos. You are reading a report about Venezuelan migration, and Meg asks how many Venezuelans live abroad.','Tell Meg the figure, with its source and its date.',['Name the source','Say the figure and the date'],'Según ACNUR, a finales de 2025 había unos 7,9 millones de venezolanos fuera del país.','According to UNHCR, at the end of 2025 there were about 7.9 million Venezuelans outside the country.',g('04'))
c[P+'-05']=M('What Some Migrants Wish','You are Meg. You are telling Carlos what you read about the feelings of some Venezuelan migrants.','Tell Carlos what some migrants say about staying in their country.',['Say who says it','Use a wish about the past'],'Algunos migrantes dicen que ojalá hubieran podido quedarse en su país.','Some migrants say that they wish they had been able to stay in their country.',g('05'))
c[P+'-consolidation']=M('A Short Summary','You are Meg. You are telling Carlos what you remember about the music of the Llanos.','Tell Carlos what the joropo is.',['Say what the joropo is','Say where it is danced'],'El joropo es la música que se baila en los Llanos.','The joropo is the music that is danced in the Llanos.',L['consolidation']['checklist_items'][0])
json.dump(c,open('/home/user/parlour-read-b/challenges-venezuela-llanos-diaspora.json','w'),indent=2,ensure_ascii=False)
