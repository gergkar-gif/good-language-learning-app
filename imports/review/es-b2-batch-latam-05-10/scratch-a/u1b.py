from lib import *
U='b2-el-salvador-honduras-vocab'
# ---------- 02 ----------
s='b2-salvadorhonduras-02'; T='estilo-indirecto-informacion'
lesson(s,'Northern Honduras: banana companies, the Garífuna and Berta Cáceres',
 'Report what people said and cite sources about the banana strike, the Garífuna and Berta Cáceres, with dijo que and según.',
 'reported statements and sources: dijo que, según (review)',
 ['In this lesson you read about the north of Honduras: the banana companies, the Garífuna people and the Lenca leader Berta Cáceres. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for reporting what someone said and for naming a source: *dijo que* and *según*.'],
 ['I can report what people said, with *dijo que* and the right past tense.','I can name my source with *según*.','I can tell the story of the 1954 banana strike and of Berta Cáceres in a few sentences.'])
grammar(s,'Who Said It?',[
 {'type':'text','title':'What you already know','content':'You know *decir que* and *según* + the source from B1 Unit 13. After a past verb such as *dijo*, the verb inside moves back: *queremos* becomes *querían*, *hemos perdido* becomes *habían perdido*. On a topic where people disagree, naming the source is the honest way to speak.'},
 {'type':'table','title':'Reporting a statement','rows':[
  ['«Queremos mejores salarios.»','Dijeron que querían mejores salarios.'],
  ['«Hemos perdido nuestras tierras.»','Dijeron que habían perdido sus tierras.'],
  ['(source) la UNESCO','Según la UNESCO, la música garífuna es parte del patrimonio de la humanidad.'],
  ['(source) los historiadores','Según los historiadores, la huelga cambió las relaciones de trabajo.']]},
 {'type':'examples','title':'In northern Honduras','items':[
  {'spanish':'Los trabajadores dijeron que querían mejores salarios.','english':'The workers said that they wanted better wages.'},
  {'spanish':'Según el COPINH, el río Gualcarque es sagrado para el pueblo lenca.','english':'According to COPINH, the Gualcarque river is sacred to the Lenca people.'},
  {'spanish':'La familia de Berta Cáceres dijo que todavía faltaban responsables por juzgar.','english':'Berta Cáceres\'s family said that other people responsible were still to be tried.'},
  {'spanish':'Según los historiadores, la huelga de 1954 duró más de dos meses.','english':'According to historians, the 1954 strike lasted more than two months.'}]},
 {'type':'tip','content':'After *decir* there is no *de*: *dijeron que querían*, not *dijeron de que querían*. And do not drop *que*: not *dijeron querían*. With *según* you do not need *que*: *según los historiadores, …*.'}])
vocab(s,'Bananas, culture and land','Companies, a strike, the Garífuna and a river',[
 ('la huelga','strike','noun'),('la plantación','plantation','noun'),('la represa','dam','noun'),('sagrado','sacred','adjective'),
 ('lenca','Lenca (an Indigenous people of Honduras)','adjective'),('el bananero','banana worker; banana grower','noun')])
ex(s,[
 match(s+'.ex01',[['la huelga','strike'],['la plantación','plantation'],['la represa','dam'],['sagrado','sacred']],U),
 mc(s+'.ex02','In 1954 the workers said: "Queremos mejores salarios." Which sentence reports this correctly?',
  ['Los trabajadores dijeron que querían mejores salarios.','Los trabajadores dijeron querían mejores salarios.','Los trabajadores dijeron de que querían mejores salarios.'],teaches=T),
 fb(s+'.ex03','__ la UNESCO, la música garífuna forma parte del patrimonio cultural de la humanidad.','Según','According to UNESCO, Garífuna music is part of humanity\'s cultural heritage.',T),
 sb(s+'.ex04',['Según','el','COPINH,','el','río','Gualcarque','es','sagrado','para','el','pueblo','lenca.'],'According to COPINH, the Gualcarque river is sacred to the Lenca people.',T),
 dlg(s+'.ex05',[('Meg','¿Qué dijeron los trabajadores bananeros en 1954?'),('Carlos','_____'),('Meg','Entonces la huelga fue por el trabajo.')],
  ['Dijeron que querían mejores salarios y mejores condiciones de trabajo.','Dijeron que el río Gualcarque era sagrado para su pueblo.','Dijeron que la UNESCO había declarado su música patrimonio en 2001.'],U),
 dic(s+'.ex06','Según los historiadores, la huelga de 1954 duró más de dos meses.','According to historians, the 1954 strike lasted more than two months.',T)])
story(s,'La costa norte de Honduras: bananos, garífunas y Berta Cáceres','On the north coast of Honduras, banana companies, the 1954 strike, the Garífuna people and the killing of the Lenca leader Berta Cáceres are told with their sources.',
 ['Compañías bananeras','Cultura garífuna','Berta Cáceres'],['estilo indirecto','según + fuente'],[
 'A comienzos del siglo XX, compañías estadounidenses como la United Fruit Company y la Standard Fruit plantaron bananos en la costa norte de Honduras. Construyeron ferrocarriles y puertos para sacar la fruta. Según muchos historiadores, las compañías tuvieron una gran influencia en la política del país. De esa época viene la expresión «república bananera», que el escritor O. Henry usó en 1904 en un libro sobre un país imaginario inspirado en Honduras.',
 'En 1954, miles de trabajadores de las plantaciones hicieron una huelga que duró más de dos meses. Dijeron que querían mejores salarios y mejores condiciones de trabajo. Según muchos historiadores, la huelga cambió las relaciones laborales del país, y en 1959 se aprobó un Código del Trabajo.',
 'En la misma costa viven los garífunas. Su historia empezó en la isla de San Vicente, en el Caribe, donde personas de origen africano e indígena formaron una comunidad. En 1797, los británicos los llevaron a la isla hondureña de Roatán, y desde allí se extendieron por la costa de Centroamérica. En 2001, la UNESCO proclamó su lengua, su música y su danza obra maestra del patrimonio oral e intangible de la humanidad.',
 'Varias comunidades garífunas dicen que han perdido tierras de la costa. En 2015, la Corte Interamericana de Derechos Humanos dijo que Honduras había violado los derechos de dos comunidades garífunas sobre sus tierras.',
 'Berta Cáceres, una mujer lenca, fue una de las fundadoras del COPINH, una organización indígena, en 1993. Según el COPINH, el río Gualcarque es sagrado para su pueblo, y Cáceres se opuso a la represa de Agua Zarca. En 2015 recibió el Premio Medioambiental Goldman. El 3 de marzo de 2016 fue asesinada en su casa, en La Esperanza. En 2018, un tribunal hondureño condenó a siete hombres por el crimen, y en 2021 otro tribunal condenó a un exdirectivo de la empresa de la represa. Su familia dice que todavía faltan otros responsables.'],
 [('What did the banana workers say in 1954?',['Dijeron que querían mejores salarios.','Dijeron que querían una nueva moneda.','Dijeron que querían cerrar los puertos.','Dijeron que querían más plantaciones.'],0,'The text says they said they wanted better wages and conditions.'),
  ('Where did the British take the Garífuna in 1797?',['A la isla de Roatán.','A la isla de Cuba.','A la ciudad de Copán.','A La Esperanza.'],0,'The text says they were taken to Roatán.'),
  ('What does the text say about the family of Berta Cáceres?',['Dice que faltan otros responsables.','Dice que el caso está cerrado.','Vive en Estados Unidos.','Trabaja en la represa.'],0,'The text says her family says other people responsible are still missing.')])

# ---------- 03 ----------
s='b2-salvadorhonduras-03'; T='contrast-concession-connectors'
lesson(s,'Óscar Romero and the war in El Salvador: from 1977 to the peace of 1992',
 'Tell the story of Archbishop Romero, the civil war and the 1992 peace accords, with sin embargo and no obstante.',
 'contrast with sin embargo and no obstante (review)',
 ['In this lesson you read about Archbishop Óscar Romero, the civil war in El Salvador and the peace accords of 1992. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for saying "however": *sin embargo* and *no obstante*.'],
 ['I can show a contrast between two facts, with *sin embargo* and *no obstante*.','I can tell what happened to Archbishop Romero in 1977 and 1980.','I can say how the civil war ended.'])
grammar(s,'However, Nevertheless',[
 {'type':'text','title':'What you already know','content':'You know *sin embargo* from A2 Unit 28 and *no obstante* from B1 Unit 1. Both join two facts that pull in different directions: something expected, and what happened instead. *No obstante* is a little more formal. Put a semicolon or a full stop before them and a comma after them. This is useful when you tell a hard story, because the connector shows the turn without any opinion from you.'},
 {'type':'table','title':'Two facts, one contrast','rows':[
  ['Muchos esperaban un obispo tranquilo; sin embargo, Romero habló por las víctimas.','Many expected a quiet bishop; however, Romero spoke for the victims.'],
  ['La guerra fue dura; no obstante, las dos partes llegaron a un acuerdo.','The war was hard; nevertheless, the two sides reached an agreement.'],
  ['Hubo muchas amenazas. Sin embargo, Romero siguió hablando por la radio.','There were many threats. However, Romero kept speaking on the radio.'],
  ['Había miedo; no obstante, mucha gente escuchaba la misa en casa.','There was fear; nevertheless, many people listened to Mass at home.']]},
 {'type':'examples','title':'In the story of El Salvador','items':[
  {'spanish':'La guerra duró doce años. Sin embargo, en 1992 se firmó la paz.','english':'The war lasted twelve years. However, peace was signed in 1992.'},
  {'spanish':'La guerra fue muy violenta; no obstante, las dos partes negociaron con la ayuda de la ONU.','english':'The war was very violent; nevertheless, the two sides negotiated with the help of the UN.'},
  {'spanish':'Romero fue nombrado arzobispo en 1977; sin embargo, pocas semanas después empezó a hablar con más fuerza.','english':'Romero was named archbishop in 1977; however, a few weeks later he began to speak out more strongly.'},
  {'spanish':'Hubo amenazas; no obstante, la misa se oía por la radio cada domingo.','english':'There were threats; nevertheless, the Mass was heard on the radio every Sunday.'}]},
 {'type':'tip','content':'*Sin embargo* and *no obstante* do not mean *por eso* ("that is why"): after them the second fact goes against the first one. Do not put *que* after them.'}])
vocab(s,'A bishop, a war and a peace','Romero, the civil war and the accords',[
 ('el arzobispo','archbishop','noun'),('la guerrilla','guerrilla group','noun'),('el campesino','farmer, peasant','noun'),
 ('el acuerdo','agreement','noun'),('la paz','peace','noun'),('la masacre','massacre','noun')])
ex(s,[
 match(s+'.ex01',[['el arzobispo','archbishop'],['el campesino','farmer, peasant'],['la guerrilla','guerrilla group'],['la masacre','massacre']],U),
 mc(s+'.ex02','Which sentence says "Many expected a quiet bishop; however, Romero spoke for the victims"?',
  ['Muchos esperaban un obispo tranquilo; sin embargo, Romero habló por las víctimas.','Muchos esperaban un obispo tranquilo; por eso, Romero habló por las víctimas.','Muchos esperaban un obispo tranquilo; además, Romero habló por las víctimas.'],teaches=T,ds={1:'porque-y-por-eso',2:'ordering-markers'}),
 fb(s+'.ex03','La guerra duró doce años. Sin __, en 1992 las dos partes firmaron la paz.','embargo','The war lasted twelve years. However, in 1992 the two sides signed peace.',T),
 sb(s+'.ex04',['La','guerra','fue','muy','violenta;','no','obstante,','las','dos','partes','llegaron','a','un','acuerdo.'],'The war was very violent; nevertheless, the two sides reached an agreement.',T),
 dlg(s+'.ex05',[('Meg','¿Cómo terminó la guerra en El Salvador?'),('Carlos','_____'),('Meg','Entonces el acuerdo fue muy importante.')],
  ['Fue una guerra larga; sin embargo, en 1992 se firmó la paz en Ciudad de México.','Terminó en 1980, el día en que murió el arzobispo Romero.','Todavía no terminó: la guerra continúa entre el FMLN y el gobierno.'],U),
 dic(s+'.ex06','Mucha gente lo escuchaba por la radio; sin embargo, otros lo criticaban.','Many people listened to him on the radio; however, others criticised him.',T)])
story(s,'Óscar Romero y la guerra civil de El Salvador','Archbishop Romero spoke out for the victims of violence and was killed in 1980; the civil war that followed ended with the Chapultepec peace accords in 1992.',
 ['Óscar Romero','La guerra civil salvadoreña','Los Acuerdos de Chapultepec'],['sin embargo','no obstante'],[
 'En febrero de 1977, Óscar Romero fue nombrado arzobispo de San Salvador. Muchas personas pensaban que sería un obispo tranquilo y prudente. Sin embargo, pocas semanas después, el 12 de marzo de 1977, fue asesinado el sacerdote jesuita Rutilio Grande, amigo de Romero, que trabajaba con campesinos.',
 'Cada domingo hablaba en la catedral, y muchas personas escuchaban su misa por la radio. Criticaba la violencia del gobierno y del ejército. Para muchos salvadoreños era la voz de los pobres; no obstante, otros lo criticaban por meterse en la política.',
 'El 23 de marzo de 1980, Romero pidió a los soldados que no obedecieran órdenes de matar y que cesara la represión. Al día siguiente, el 24 de marzo, fue asesinado mientras celebraba misa en la capilla de un hospital. Según la Comisión de la Verdad de la ONU, el exmayor Roberto d\'Aubuisson dio la orden.',
 'Ese mismo año empezó la guerra civil entre el gobierno y el FMLN, un grupo guerrillero. Duró doce años y murieron decenas de miles de personas, muchas de ellas civiles. Según la Comisión de la Verdad, la gran mayoría de los casos que investigó fueron cometidos por agentes del Estado y por grupos armados que actuaban con ellos. En diciembre de 1981 soldados mataron a cientos de civiles en El Mozote; en 2012, la Corte Interamericana de Derechos Humanos dijo que el Estado era responsable.',
 'No obstante la violencia, las dos partes negociaron con la ayuda de la ONU. El 16 de enero de 1992 firmaron los Acuerdos de Paz en el castillo de Chapultepec, en Ciudad de México. Los acuerdos redujeron el ejército, crearon una nueva policía civil y permitieron que el FMLN fuera un partido político. Romero fue beatificado en 2015, y el papa Francisco lo declaró santo en octubre de 2018.'],
 [('What did Romero do on 23 March 1980?',['Pidió a los soldados que no obedecieran órdenes de matar.','Firmó los Acuerdos de Paz.','Viajó a Ciudad de México.','Fundó el FMLN.'],0,'The text says he asked the soldiers not to obey orders to kill.'),
  ('How long did the civil war last, according to the text?',['Doce años.','Dos años.','Cincuenta años.','Un mes.'],0,'The text says it lasted twelve years.'),
  ('Where were the peace accords signed?',['En el castillo de Chapultepec, en Ciudad de México.','En la catedral de San Salvador.','En Roma.','En El Mozote.'],0,'The accords were signed on 16 January 1992 in Mexico City.')])
