import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
exec(open('/home/user/parlour-read-a/.scratch/u2a.py').read().split("CO='conectores")[0])
CO='conectores-temporales-narrativos'
FR='inversion-enfasis-fronting'; HY='hypothetical-structures'; SC='si-clauses'; RL='relativas-preposicion-el-que'; PR='pasiva-refleja'
# ---------- 02
s='b2-mexiconorte-02'
items=["I can put a quality or a place first, as in Duros eran los días de trabajo, to stress it when I describe vaquero life.",
"I can make the verb agree with a subject that comes after it.",
"I can say where vaquero culture comes from and what the carne asada means in the north.",
"I can use the lesson's words for cattle, ranch work and grazing land."]
lesson2(s,"Vaquero culture and the making of the northerner","Use fronting to stress what was hard, typical or important in the vaquero life of northern Mexico.","fronting for emphasis (recap)",items)
story_update(s,"Vaqueros, ganado y carne asada","Vaquero culture grew up on the cattle lands of northern New Spain; the text describes ranch work, the values historians link to it and the carne asada today.",[
"Mucho antes de que el cine de Hollywood hiciera famoso al cowboy, ya existía una cultura de vaqueros en el norte de Nueva España. Muchas de las técnicas del trabajo con el ganado, como el uso del lazo y de la silla de montar, se desarrollaron en las grandes tierras de pastos de regiones como Sonora, Coahuila y Chihuahua, y muchos de esos trabajadores eran de origen español, indígena o mestizo.",
"Duros eran los días de trabajo. La jornada empezaba antes de salir el sol, y los vaqueros llevaban el ganado de un pasto a otro según las lluvias. Muy lejos de la capital estaba la gente, y tenía que arreglarse sola. Según varios historiadores, eso favoreció una cultura que valoraba el esfuerzo personal, la palabra dada y la ayuda entre compañeros.",
"Hoy esa herencia sigue viva en la carne asada, una comida que se prepara en una parrilla, normalmente al aire libre. Típica del norte es esa reunión de familia y amigos alrededor del fuego, en Sonora, en Nuevo León y en otros estados. Para muchas personas, la carne asada es una forma de estar juntos, de hablar de trabajo y de celebrar la vida en el norte."])
vocab_update(s,"Vaquero culture and the making of the northerner: vocabulary",[
("el vaquero","cowboy, cattle herder","noun"),("el ganado","cattle, livestock","noun"),("el agostadero","grazing land","noun"),("la faena","ranch task, work","noun"),("el temple","mettle, strength of character","noun"),("el lazo","lasso, rope","noun"),("la parrilla","grill","noun")])
grammar_update(s,"Fronting in the Story of the Vaquero",[
T("What you already know","You know *Crucial fue la intervención del mediador* and *En aquella ciudad comenzó la rebelión* from B2 Unit 1: this is fronting. You put the piece you want to stress at the front of the sentence, and the subject usually comes after the verb. Writers use it to give a paragraph a high point. This lesson applies it to the life of the vaqueros and to the carne asada."),
TAB("What can go first",[
["Adjective + ser + subject","Duros eran los días de trabajo. (Hard were the days of work.)"],
["Place or time phrase + verb + subject","En estas tierras nació la cultura vaquera. (In these lands vaquero culture was born.)"],
["Adjective + ser + subject, plural","Típicos del norte son los asados en familia. (Typical of the north are family barbecues.)"]]),
T("Two rules to keep","The verb and the adjective agree with the subject that comes after them: *Duro era el trabajo*, *Duros eran los días*, not *Duros era los días*. The subject stays behind the verb: *Duro el trabajo era* sounds unnatural. Plain order is still the usual order; fronting is for the moment you want to stress."),
EX("In context",[
("Duros eran los días de trabajo en los agostaderos.","Hard were the days of work on the grazing lands."),
("Con el lazo en la mano arreaba el vaquero el ganado.","With the lasso in his hand the vaquero herded the cattle."),
("En estas tierras nació la cultura vaquera.","In these lands vaquero culture was born."),
("Muy larga era la jornada, que empezaba antes de salir el sol.","Very long was the working day, which began before sunrise."),
("Típica del norte es la carne asada con la familia.","Typical of the north is the carne asada with the family.")]),
TIP("Use fronting once in a paragraph, at the point you want to stress. If every sentence starts with its adjective, the text sounds heavy.")])
ex_write(s,[
match2(s+'.ex01',[("el vaquero","cowboy, cattle herder"),("el agostadero","grazing land"),("la faena","ranch task, work"),("el temple","mettle, strength of character")]),
mc(s+'.ex02',"Which sentence puts the hardness of the vaqueros' work with the cattle first, for emphasis?",[
"Duro era el trabajo de los vaqueros con el ganado.",
"Duro el trabajo era de los vaqueros con el ganado.",
"Duros era el trabajo de los vaqueros con el ganado."],FR),
fill(s+'.ex03',"Duros ____ los días de trabajo en el campo.",None,"Hard were the days of work in the field.",FR,answers=["eran","fueron"]),
build(s+'.ex04',["En","estas","tierras","nació","la","cultura","vaquera."],"In these lands vaquero culture was born.",FR),
dial(s+'.ex05',[("Guía","¿Qué comida es muy popular en las reuniones familiares del norte?"),("Tú","_____"),("Guía","Sí, es una tradición muy querida.")],[
"Típica del norte es la carne asada en la parrilla.",
"Típicas del norte es la carne asada en la parrilla.",
"Típica la carne asada es del norte en la parrilla."],FR),
dict_(s+'.ex06',"Con el lazo en la mano, el vaquero arreaba el ganado antes de salir el sol.","With the lasso in his hand, the vaquero herded the cattle before sunrise.",FR)])
# ---------- 03
s='b2-mexiconorte-03'
items=["I can use si + imperfect subjunctive + conditional to say what would happen if something were different in Monterrey.",
"I can use si + present for a realistic condition about the water.",
"I can say how Monterrey became an industrial city and what its water problem is.",
"I can use the lesson's words for steel, drought and shortage."]
lesson2(s,"Monterrey: an industrial city and its water","Use si-clauses to say what happens, or would happen, if conditions change in Monterrey, the industrial capital of the north.","si-clauses and hypotheses (recap)",items)
story_update(s,"Monterrey, ciudad del acero","Monterrey grew into the industrial capital of the north after 1900, with steel, beer, glass and cement; today its biggest problem is water.",[
"Monterrey, capital del estado de Nuevo León, está al pie del Cerro de la Silla. Fue fundada a finales del siglo dieciséis, pero su gran crecimiento llegó a finales del siglo diecinueve, cuando el ferrocarril la unió con el centro del país y con Estados Unidos.",
"En 1900 se fundó la Compañía Fundidora de Fierro y Acero de Monterrey, una de las primeras acerías integradas de América Latina. Alrededor de la industria del acero crecieron empresas de cerveza, vidrio y cemento, y en 1943 se fundó el Tecnológico de Monterrey. La Fundidora cerró en 1986, y en su terreno hay hoy un parque público.",
"La industria sigue siendo muy importante, pero el agua preocupa. En 2022, una sequía grave obligó a restringir el agua en la zona metropolitana. Si llueve menos y la población sigue creciendo, la ciudad tendrá menos agua para cada persona. Si Monterrey pudiera reutilizar más agua, la presión sería menor. Algunos expertos piden más inversión en reutilización y en infraestructura."])
vocab_update(s,"Monterrey: an industrial city and its water: vocabulary",[
("la acería","steelworks","noun"),("la escasez","shortage, scarcity","noun"),("la sequía","drought","noun"),("reutilizar","to reuse","verb")])
grammar_update(s,"Si-clauses in the Story of Monterrey",[
T("What you already know","You know *si* + present from B1 Unit 8 for a realistic condition (*Si perdemos el tren, tomaremos el siguiente*). And you know *Si yo fuera tú* and *si tuviera más tiempo* from B1 Unit 4: *si* + imperfect subjunctive, with the conditional in the result, for an imagined situation. Both are useful for Monterrey, a city whose future depends on water: what happens if it rains less, and what would happen if the city could reuse more."),
TAB("Two kinds of condition",[
["Si + present, future","A real possibility: Si llueve menos, habrá menos agua. (If it rains less, there will be less water.)"],
["Si + imperfect subjunctive, conditional","An imagined situation: Si la ciudad reutilizara más agua, la presión sería menor. (If the city reused more water, the pressure would be less.)"],
["Never *si* + conditional","Not Si la ciudad reutilizaría más agua, but Si reutilizara. The conditional goes in the result."]]),
T("Forms to keep in mind","The imperfect subjunctive comes from the *ellos* form of the *indefinido*: *hubieron* gives *hubiera* (or *hubiese*), *pudieron* gives *pudiera*, *tuvieron* gives *tuviera*. *Hubiera* is the form of *haber* for \"there were\": *Si hubiera más lluvia, el problema sería menor*."),
EX("In context",[
("Si llueve menos, la ciudad tendrá menos agua.","If it rains less, the city will have less water."),
("Si hubiera más lluvia, el problema del agua sería menor.","If there were more rain, the water problem would be smaller."),
("Si Monterrey pudiera reutilizar más agua, la presión sería menor.","If Monterrey could reuse more water, the pressure would be less."),
("Si no hubiera agua suficiente, la industria tendría problemas.","If there were not enough water, industry would have problems."),
("Si la población sigue creciendo, el consumo de agua aumentará.","If the population keeps growing, water use will increase.")]),
TIP("Choose by how you see the situation: if it is a real possibility, *si* + present; if you are imagining something that is not true now, *si* + imperfect subjunctive.")])
ex_write(s,[
match2(s+'.ex01',[("la acería","steelworks"),("la escasez","shortage, scarcity"),("la sequía","drought"),("reutilizar","to reuse")]),
mc(s+'.ex02',"Which sentence says what would happen if Monterrey could reuse more water?",[
"Si Monterrey pudiera reutilizar más agua, la presión sería menor.",
"Si Monterrey podría reutilizar más agua, la presión sería menor.",
"Si Monterrey pudiera reutilizar más agua, la presión fuera menor."],HY),
fill(s+'.ex03',"Si no ____ agua suficiente, la industria tendría problemas.",None,"If there were not enough water, industry would have problems.",HY,hint="haber",answers=["hubiera","hubiese"]),
build(s+'.ex04',["Si","llueve","menos,","la","ciudad","tendrá","menos","agua."],"If it rains less, the city will have less water.",SC),
dial(s+'.ex05',[("Economista","¿Qué podría hacer Monterrey para reducir el problema del agua?"),("Analista","_____"),("Economista","Sería una solución buena, pero cara.")],[
"Si reutilizara más agua, la presión sería menor.",
"Si reutilizaría más agua, la presión sería menor.",
"Si reutiliza más agua, la presión sería menor."],HY),
dict_(s+'.ex06',"Si hubiera más lluvia, el problema del agua sería menor.","If there were more rain, the water problem would be smaller.",HY)])
