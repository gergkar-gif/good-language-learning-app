from lib import *
U='b2-costa-rica-vocab'
# ---------- 04 ----------
s='b2-costarica-04'; T='antes-despues-de-que'
lesson(s,'Pura Vida: forests, ecotourism and clean energy',
 'Tell how Costa Rica protected its forests and what came before and after, with antes de que and después de que.',
 'antes de que and después de que (review)',
 ['In this lesson you read about how Costa Rica stopped cutting its forests, about ecotourism, about electricity and about the phrase *pura vida*. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for saying what came before or after someone else\'s action: *antes de que* and *después de que*.'],
 ['I can say what happened before or after someone else\'s action, with *antes de que* and *después de que*.','I can tell how Costa Rica protected its forests.','I can say where most of its electricity comes from.'])
grammar(s,'Before It Changed, After It Changed',[
 {'type':'text','title':'What you already know','content':'You know *antes de que* and *después de que* from B2 Unit 7. With the same person you use an infinitive (*antes de salir*). With a new subject you need *que*. *Antes de que* always takes the subjunctive. *Después de que* takes the indicative for something that happened and the subjunctive for something still to come.'},
 {'type':'table','title':'The three patterns','rows':[
  ['antes de que + subjunctive (always)','Antes de que lleguen los turistas, los guías revisan los senderos.'],
  ['después de que + indicative (it happened)','Después de que se creó el programa de pagos, más propietarios protegieron su bosque.'],
  ['después de que + subjunctive (still to come)','Después de que termine la temporada, los hoteles cierran unas semanas.'],
  ['antes de / después de + infinitive (same person)','Antes de abrir, los guías revisan los senderos.']]},
 {'type':'examples','title':'Forests and tourism','items':[
  {'spanish':'Antes de que el turismo creciera, el país había perdido gran parte de sus bosques.','english':'Before tourism grew, the country had lost a large part of its forests.'},
  {'spanish':'Después de que el país aprobó una ley forestal en 1996, empezaron los pagos por servicios ambientales.','english':'After the country passed a forestry law in 1996, payments for environmental services began.'},
  {'spanish':'Los guías revisan los senderos antes de que lleguen los visitantes.','english':'The guides check the trails before the visitors arrive.'},
  {'spanish':'Después de que termine la sequía, las represas volverán a producir más electricidad.','english':'After the drought ends, the dams will produce more electricity again.'}]},
 {'type':'tip','content':'After *antes de que* never use the indicative: not *antes de que llegan*. After *después de que* ask yourself whether it has happened: yes, indicative; not yet, subjunctive.'}])
vocab(s,'Forests, tourism and energy','Forest laws, ecotourism and electricity',[
 ('el bosque','forest','noun'),('la ley forestal','forestry law','noun'),('el turismo','tourism','noun'),('la electricidad','electricity','noun'),
 ('renovable','renewable','adjective'),('el sendero','path, trail','noun'),('proteger','to protect','verb')])
ex(s,[
 match(s+'.ex01',[['la ley forestal','forestry law'],['la electricidad','electricity'],['renovable','renewable'],['el sendero','path, trail']],U),
 mc(s+'.ex02','Which sentence says "The guides check the trails before the visitors arrive"?',
  ['Los guías revisan los senderos antes de que lleguen los visitantes.','Los guías revisan los senderos antes de que llegan los visitantes.','Los guías revisan los senderos antes de llegan los visitantes.'],teaches=T,ds={1:'present-tense'}),
 fb(s+'.ex03','Después de que el país __ una ley forestal en 1996, empezaron los pagos por servicios ambientales.','aprobó','After the country passed a forestry law in 1996, payments for environmental services began.',T,hint='aprobar'),
 sb(s+'.ex04',['Los','guías','revisan','los','senderos','antes','de','que','lleguen','los','visitantes.'],'The guides check the trails before the visitors arrive.',T),
 dlg(s+'.ex05',[('Meg','¿Cuándo empezó Costa Rica a pagar por proteger los bosques?'),('Carlos','_____'),('Meg','Gracias, ahora tengo la fecha.')],
  ['Después de que el país aprobó una ley forestal en 1996.','Antes de que terminara la guerra civil de 1948.','Después de que el volcán Arenal empezó a dormir.'],U),
 dic(s+'.ex06','Antes de que el turismo creciera, el país había perdido gran parte de sus bosques.','Before tourism grew, the country had lost a large part of its forests.',T)])
story(s,'Pura vida: bosques, ecoturismo y energía','Costa Rica lost much of its forest in the twentieth century, then passed laws and paid owners to protect it; today ecotourism is important and most electricity comes from renewable sources.',
 ['Deforestación y recuperación','Ecoturismo','Electricidad'],['antes de que','después de que'],[
 'Durante el siglo XX, Costa Rica perdió gran parte de sus bosques: muchos terrenos se convirtieron en pastos para el ganado y en campos de café y de banano. Antes de que el país cambiara de política, la selva retrocedía cada año.',
 'En 1996, el país aprobó una ley forestal. Después de que se aprobó esa ley, empezó el programa de pago por servicios ambientales: el Estado paga a los dueños de terrenos que protegen o plantan bosque. Una parte del dinero viene de un impuesto sobre los combustibles. Hoy los bosques cubren más de la mitad del territorio, y a Costa Rica se la suele citar como la primera nación tropical que revirtió la deforestación.',
 'Sobre esa base creció el ecoturismo. Los visitantes recorren puentes colgantes, parques nacionales y reservas con guías, que revisan los senderos antes de que lleguen los grupos. El turismo es hoy una de las fuentes de ingresos más importantes del país.',
 'La electricidad también es un tema de orgullo. En la mayoría de los años recientes, más del noventa y cinco por ciento de la electricidad vino de fuentes renovables, sobre todo de represas, de plantas geotérmicas y de parques de viento. En 2023 y 2024, sin embargo, las sequías redujeron el agua de las represas, y el país necesitó usar más plantas térmicas. El gobierno tiene un plan para reducir las emisiones de dióxido de carbono hasta el año 2050.',
 'Muchos costarricenses usan la expresión «pura vida» para saludar, para despedirse, para dar las gracias o para decir que todo va bien. Para muchas personas, la frase resume una forma tranquila de vivir y un cariño por la naturaleza del país.'],
 [('What happened to Costa Rica\'s forests in the twentieth century?',['El país perdió gran parte de sus bosques.','El país plantó bosques en todo su territorio.','El país prohibió el turismo.','El país cerró las represas.'],0,'The text says the country lost much of its forest.'),
  ('What does the programme of payments for environmental services do?',['Paga a los dueños que protegen o plantan bosque.','Paga a los turistas.','Construye represas.','Cobra impuestos al café.'],0,'The text says the State pays owners who protect or plant forest.'),
  ('What happened to electricity in 2023 and 2024?',['Las sequías obligaron a usar más plantas térmicas.','Todo el país se quedó sin electricidad.','Se cerraron las plantas geotérmicas.','Se abrió un canal.'],0,'The text says droughts made the country use more thermal plants.')])

# ---------- 05 ----------
s='b2-costarica-05'; T='infinitive-vs-que-subjunctive'
lesson(s,'Pineapples, migrants and the regions: the other side of Costa Rica',
 'Describe the work, the migration and the regional gaps in Costa Rica, choosing between the infinitive and que + subjunctive.',
 'one person or two: infinitive vs que + subjunctive (review)',
 ['In this lesson you read about pineapple and banana farms, Nicaraguan workers and the differences between regions in Costa Rica. The text is in Spanish; the screens and instructions are in English. The facts are dated and attributed.',
  'The grammar is the one you know for choosing between an infinitive and *que* + subjunctive: *quieren trabajar* or *quieren que las empresas paguen*.'],
 ['I can choose between an infinitive and *que* + subjunctive, depending on who does the second action.','I can say what workers and organisations want.','I can tell which regions have the biggest gaps.'])
grammar(s,'One Person or Two?',[
 {'type':'text','title':'What you already know','content':'You know *quiero salir* and *quiero que salgas* from B2 Unit 4: the choice depends on who does the second action. If the person who wants is also the person who acts, use an infinitive: *Los trabajadores quieren tener contrato*. If someone else acts, use *que* + subjunctive: *Los sindicatos quieren que las empresas paguen el salario mínimo*. Reports about work and migration are full of both.'},
 {'type':'table','title':'Same person or new person?','rows':[
  ['Los migrantes quieren trabajar con contrato.','same person: the migrants want to work with a contract'],
  ['Los sindicatos quieren que las empresas paguen el salario mínimo.','new person: the unions want the companies to pay the minimum wage'],
  ['Las familias esperan encontrar trabajo.','same person: the families hope to find work'],
  ['Las organizaciones piden que el gobierno proteja los ríos.','new person: the organisations ask the government to protect the rivers']]},
 {'type':'examples','title':'About farms and regions','items':[
  {'spanish':'Muchos trabajadores migrantes quieren trabajar con un contrato legal.','english':'Many migrant workers want to work with a legal contract.'},
  {'spanish':'Los sindicatos quieren que las empresas paguen el salario mínimo.','english':'The unions want the companies to pay the minimum wage.'},
  {'spanish':'Las organizaciones ambientales piden que el gobierno proteja los ríos.','english':'Environmental organisations ask the government to protect the rivers.'},
  {'spanish':'Los jóvenes de la costa esperan encontrar empleo cerca de su casa.','english':'Young people on the coast hope to find a job near home.'}]},
 {'type':'tip','content':'English hides the second person (*they want the companies to pay*), so ask yourself who does the second action. Same person: infinitive. New person: *que* + subjunctive. Not *quieren que tener*, and not *quieren las empresas pagar*.'}])
vocab(s,'Farms, work and regions','Agribusiness, migration and regional gaps',[
 ('la piña','pineapple','noun'),('el trabajador','worker','noun'),('el contrato','contract','noun'),('el sindicato','trade union','noun'),
 ('el salario mínimo','minimum wage','noun'),('el empleo','job, employment','noun')])
ex(s,[
 match(s+'.ex01',[['la piña','pineapple'],['el contrato','contract'],['el sindicato','trade union'],['el empleo','job, employment']],U),
 mc(s+'.ex02','Which sentence says "The unions want the companies to pay the minimum wage"?',
  ['Los sindicatos quieren que las empresas paguen el salario mínimo.','Los sindicatos quieren que las empresas pagan el salario mínimo.','Los sindicatos quieren las empresas pagar el salario mínimo.'],teaches=T,ds={1:'present-tense'}),
 fb(s+'.ex03','Muchos trabajadores migrantes quieren __ con un contrato legal.','trabajar','Many migrant workers want to work with a legal contract.',T),
 sb(s+'.ex04',['Las','organizaciones','piden','que','el','gobierno','proteja','los','ríos.'],'The organisations ask the government to protect the rivers.',T),
 dlg(s+'.ex05',[('Meg','¿Qué quieren los trabajadores de las plantaciones de piña?'),('Carlos','_____'),('Meg','Es un tema muy importante.')],
  ['Quieren trabajar con contrato, y quieren que las empresas paguen el salario mínimo.','Quieren visitar el parque nacional Corcovado y ver las tortugas verdes.','Quieren que el ejército vuelva a Costa Rica.'],U),
 dic(s+'.ex06','Las organizaciones piden que el gobierno proteja los ríos y que las empresas cuiden el agua.','The organisations ask the government to protect the rivers and the companies to take care of the water.',T)])
story(s,'Piñas, migrantes y regiones: el otro lado de Costa Rica','Costa Rica is a major pineapple exporter and relies on Nicaraguan workers; reports mention pay, pesticide and regional gaps, and in 2026 Laura Fernández became president.',
 ['Agroindustria','Migración','Desigualdades regionales'],['infinitivo o que + subjuntivo'],[
 'Costa Rica es uno de los mayores exportadores de piña fresca del mundo, y también exporta mucho banano. Estas plantaciones dan empleo y traen dinero al país, pero organizaciones ambientales dicen que los pesticidas pueden contaminar ríos y aguas subterráneas. Piden que el gobierno controle mejor el uso de esos productos y que las empresas cuiden el agua.',
 'Gran parte del trabajo agrícola lo hacen migrantes, sobre todo nicaragüenses. Cientos de miles de nicaragüenses viven en Costa Rica, algunos desde hace décadas, y otros llegaron después de la crisis política de 2018. Según informes de organizaciones sociales, algunos trabajadores migrantes reciben menos del salario mínimo o no tienen contrato. Los sindicatos quieren que las empresas cumplan la ley, y muchos trabajadores quieren trabajar con un contrato legal.',
 'También hay diferencias entre regiones. Los informes anuales del programa Estado de la Nación muestran que en el Valle Central hay más empleo y más ingresos que en las zonas de la costa y de la frontera, como Limón, Puntarenas o los cantones del norte. Muchos jóvenes de esas zonas esperan encontrar trabajo cerca de su casa.',
 'En las elecciones de 2026 ganó Laura Fernández, que asumió la presidencia el 8 de mayo de 2026. Es la segunda mujer presidenta de la historia del país. Entre los temas del debate político están la seguridad y el crimen organizado, y también la manera de reducir las diferencias entre regiones.'],
 [('What do the environmental organisations say about the farms?',['Dicen que los pesticidas pueden contaminar el agua.','Dicen que las plantaciones no dan empleo.','Dicen que no hay piñas.','Dicen que el ejército las vigila.'],0,'The text says the organisations say pesticides can pollute water.'),
  ('Who does much of the farm work, according to the text?',['Migrantes, sobre todo nicaragüenses.','Soldados.','Turistas.','Estudiantes de Monteverde.'],0,'The text says much of the farm work is done by migrants, especially Nicaraguans.'),
  ('Who became president on 8 May 2026?',['Laura Fernández.','Óscar Arias.','Luis Alberto Monge.','José Figueres.'],0,'The text says Laura Fernández took office on 8 May 2026.')])

# ---------- consolidation ----------
s='b2-costarica-consolidation'
lesson(s,'Unit 7 Consolidation: Costa Rica',
 'Review the nature, the abolition of the army, the welfare state, forests and energy, and the farms and regions of Costa Rica, with the grammar you used to talk about them.',
 'review: cleft sentences, no es que… sino que…, el hecho de que, antes de que and después de que, infinitive and que + subjunctive',
 [],
 ['I can review what I learned about Costa Rica, from its volcanoes to its regions.',
  'I can use cleft sentences, *no es que… sino que…*, *el hecho de que*, *antes de que* and *después de que*.',
  'I can choose between an infinitive and *que* + subjunctive.',
  'I can put events from 1941 to 2026 in order.'],
 ['I can put a place, a time or an idea in the spotlight with *Fue… donde* and *Lo que… es…*.','I can correct a reason with *No es que… sino que…*.','I can comment on a known fact with *el hecho de que* + subjunctive.','I can say what came before or after someone else\'s action, with *antes de que* and *después de que*, and choose between an infinitive and *que* + subjunctive.'])
ex(s,[
 match(s+'.ex01',[['el bosque nuboso','cloud forest'],['el ejército','army'],['la lista de espera','waiting list'],['el sindicato','trade union']],U),
 {'id':s+'.ex02','type':'multiple-choice','category':'reading','question':'According to the texts, in which year was the CCSS created?','options':['En 1941.','En 1948.','En 1983.','En 1996.'],'correct':0},
 mc(s+'.ex03','Which sentence says "The fact that the EBAIS reach the neighbourhoods helps patients"?',
  ['El hecho de que los EBAIS lleguen a los barrios ayuda a los pacientes.','El hecho que los EBAIS lleguen a los barrios ayuda a los pacientes.','El hecho de que los EBAIS llegar a los barrios ayuda a los pacientes.'],teaches='el-hecho-de-que-subjuntivo'),
 fb(s+'.ex04','No es que la guerra civil de 1948 fuera larga, __ que fue muy violenta.','sino','It is not that the 1948 civil war was long, but that it was very violent.','refutacion-no-es-que-sino'),
 {'id':s+'.ex05','type':'sentence-order','category':'grammar','sentences':[
  'En 1941 se creó la CCSS. [In 1941 the CCSS was created.]',
  'En 1948 hubo una guerra civil. [In 1948 there was a civil war.]',
  'En 1996 se aprobó una ley forestal. [In 1996 a forestry law was passed.]',
  'En 2026 Laura Fernández asumió la presidencia. [In 2026 Laura Fernández took office as president.]'],'solution':[0,1,2,3],'teaches':['preterito-indefinido']},
 dlg(s+'.ex06',[('Meg','¿Dónde desovan las tortugas verdes?'),('Carlos','_____'),('Meg','Qué bonito.')],
  ['Es en Tortuguero, en la costa del Caribe, donde desovan.','Es en el Cuartel Bellavista, en San José, donde desovan.','Es en una escuela de Nicoya donde desovan.'],U),
 dic(s+'.ex07','Los guías revisan los senderos antes de que lleguen los visitantes.','The guides check the trails before the visitors arrive.','antes-despues-de-que'),
 {'id':s+'.ex08','type':'structured-writing','category':'writing','template':[
  {'prompt':'Say that what surprises you most in Costa Rica is the variety of species. Start with "Lo que".','answer':'Lo que más me sorprende en Costa Rica es la variedad de especies.'},
  {'prompt':'Say that the unions want the companies to pay the minimum wage. Start with "Los sindicatos quieren".','answer':'Los sindicatos quieren que las empresas paguen el salario mínimo.'},
  {'prompt':'Say that the guides check the trails before the visitors arrive. Use "antes de que".','answer':'Los guías revisan los senderos antes de que lleguen los visitantes.'}],'teaches':[U]}])
