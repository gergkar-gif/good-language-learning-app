import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
V='b2-regional-integration-corridors-vocab'
T=lambda t,c:{"type":t,"content":c}
def ex(items): return {"type":"examples","title":"In context","items":[{"spanish":a,"english":b} for a,b in items]}
def wc(stem,paras): print(stem,words(paras))

# ---------- 01
s='b2-integracion-01'
lesson(s,"Mercosur: from the Treaty of Asunción to a customs union","I can state a condition with *siempre que*, *con tal de que* or *a menos que*.")
grammar(s,"Provided That, Unless: Conditions in Trade Talks",[
 {"type":"text","title":"What you already know","content":"You know *siempre que*, *con tal de que* and *a menos que* from B1 Unit 21. They add a condition to a statement and take the present subjunctive when the condition looks to the future. *Siempre que* and *con tal de que* mean \"as long as\" or \"provided that\"; *a menos que* means \"unless\". Trade talks are full of such conditions: what a bloc will do, and only if its members agree."},
 ex([("El bloque avanzará siempre que los socios armonicen sus normas.","The bloc will move forward as long as the partners harmonise their rules."),
     ("Un socio pequeño aceptará la unión aduanera con tal de que reciba fondos para sus obras.","A small partner will accept the customs union provided that it receives funds for its projects."),
     ("El arancel común no cambia a menos que todos los socios estén de acuerdo.","The common tariff does not change unless all the partners agree."),
     ("Un país ratificará el tratado siempre que su parlamento lo apruebe.","A country will ratify the treaty as long as its parliament approves it.")]),
 T("tip","Use the present subjunctive after all three, even when English says \"will\": *armonicen*, not *armonizarán*. *A menos que* reverses the meaning of the other two: *a menos que todos estén de acuerdo* means \"unless all agree\".")])
exercises(s,[
 mc(1,s,"grammar","conditional-conjunctions","Which sentence means \"The bloc can move forward as long as the partners harmonise their rules\"?",
  ["El bloque puede avanzar siempre que los socios armonicen sus normas.","El bloque puede avanzar siempre que los socios armonizan sus normas.","El bloque puede avanzar a menos que los socios armonicen sus normas."],0,{1:"present-tense"}),
 fb(2,s,"conditional-conjunctions","El arancel común no cambia a menos que todos los socios __ de acuerdo.","estén","The common tariff does not change unless all the partners agree."),
 mt(3,s,V,[("arancel común","common external tariff"),("unión aduanera","customs union"),("socio","partner"),("armonizar","to harmonise")]),
 mc(4,s,"reading","","When did the presidents sign the Treaty of Asunción, according to the text?",
  ["El 26 de marzo de 1991, en Asunción.","El 26 de marzo de 1991, en Montevideo.","El 26 de marzo de 1995, en Asunción."],0)])
vocab(s,"Mercosur and the customs union",[("arancel común","common external tariff","expression"),("unión aduanera","customs union","expression"),("socio","partner","noun"),("armonizar","to harmonise","verb")])
P=["El 26 de marzo de 1991, en Asunción, los presidentes de Argentina, Brasil, Paraguay y Uruguay firmaron el tratado que creó el Mercado Común del Sur, el Mercosur. Los cuatro países acababan de volver a la democracia después de dictaduras militares. El tratado fijó como meta la libre circulación de bienes, servicios y factores productivos, un arancel común frente al resto del mundo y la coordinación de las políticas económicas.",
"El comercio entre los socios creció mucho en los años noventa. Desde 1995 el bloque funciona como una unión aduanera, pero una unión imperfecta: hay excepciones al arancel común, y sectores como el automotor y el azúcar tienen reglas especiales.",
"Brasil y Argentina tienen las economías más grandes del bloque; Paraguay y Uruguay, las más pequeñas. Paraguay y Uruguay han señalado muchas veces que el bloque los favorece menos que a los grandes. Por eso, en 2004 se creó el FOCEM, un fondo al que los socios más grandes aportan la mayor parte del dinero y que financia, sobre todo en Paraguay y Uruguay, obras de carreteras, electricidad y saneamiento.",
"Los socios también discuten cómo negociar con terceros países. Algunos gobiernos han pedido más libertad para firmar acuerdos por separado; otros defienden que el bloque negocie unido. Las decisiones se toman por consenso: el arancel común no cambia a menos que todos los socios estén de acuerdo. Para resolver los conflictos entre socios, el Protocolo de Olivos, de 2002, creó un Tribunal Permanente de Revisión con sede en Asunción.",
"En enero de 2026 la Unión Europea y el Mercosur firmaron un acuerdo comercial, y su parte comercial se aplica de forma provisional desde mayo de 2026, según informó la prensa. El bloque seguirá avanzando siempre que los socios logren ponerse de acuerdo sobre su política comercial."]
# fix last sentence: no forecast
P[4]="En enero de 2026 la Unión Europea y el Mercosur firmaron un acuerdo comercial, y según informó la prensa su parte comercial se aplica de forma provisional desde mayo de 2026."
wc(s,P)
story(s,"Del Tratado de Asunción al Mercosur","The Treaty of Asunción created Mercosur in 1991; the text explains the customs union, the gap between big and small members, the FOCEM fund and the 2026 agreement with the EU.",P,[
 ("What did the treaty of 26 March 1991 create?",["El Mercado Común del Sur, el Mercosur.","La Comunidad Andina.","La Alianza del Pacífico."],0,"The first paragraph says the treaty created Mercosur."),
 ("What is the FOCEM for, according to the text?",["Financia obras de carreteras, electricidad y saneamiento, sobre todo en Paraguay y Uruguay.","Paga el sueldo de los presidentes de los cuatro países.","Cobra un arancel a los productos de Europa."],0,"The third paragraph describes the fund."),
 ("When does the common tariff change, according to the text?",["Solo cuando todos los socios están de acuerdo.","Cuando lo decide solo Brasil.","Cada año, de forma automática."],0,"Decisions are taken by consensus.")])

# ---------- 02
s='b2-integracion-02'
lesson(s,"The Pacific Alliance: Chile, Colombia, Mexico and Peru look to Asia","I can say what would have happened in a past situation, with *hubiera* + past participle and no *si*.")
grammar(s,"Had It Been So: Past Conditions Without Si",[
 {"type":"text","title":"What you already know","content":"You know *si hubiera* + past participle from B1 Unit 35, and from B2 Unit 10 you know that *hubiera* + participle can open a sentence in place of *si* (*Hubiera salido antes, habría llegado*), and that *aunque* or *aun cuando* + *hubiera* + participle means \"even if … had …\". The history of the Pacific Alliance gives you days and events to imagine differently."},
 ex([("Hubiera estado en Lima el 28 de abril de 2011, habría visto la firma de la Declaración de Lima.","Had I been in Lima on 28 April 2011, I would have seen the signing of the Lima Declaration."),
     ("Hubiéramos viajado a Lima en abril de 2011, habríamos visto a los presidentes de los cuatro países.","Had we travelled to Lima in April 2011, we would have seen the presidents of the four countries."),
     ("Aun cuando México no se hubiera unido al MILA en 2014, el mercado habría seguido con tres bolsas.","Even if Mexico had not joined MILA in 2014, the market would have gone on with three stock exchanges.")]),
 T("tip","Only *hubiera* (or *hubiese*) + participle can open the sentence in place of *si*, and the result clause uses *habría* + participle. Do not put *habré* or a past tense in its place.")])
exercises(s,[
 mc(1,s,"grammar","inversiones-condicionales-de-haber","Which sentence means \"Had I been in Lima on 28 April 2011, I would have seen the signing\"?",
  ["Hubiera estado en Lima el 28 de abril de 2011, habría visto la firma.","Hubiera estado en Lima el 28 de abril de 2011, habré visto la firma.","Estuve en Lima el 28 de abril de 2011, habría visto la firma."],0,{1:"futuro-perfecto",2:"preterito-indefinido"}),
 fb(2,s,"inversiones-condicionales-de-haber","Hubiéramos viajado a Lima en abril de 2011, __ visto a los presidentes de los cuatro países.","habríamos","Had we travelled to Lima in April 2011, we would have seen the presidents of the four countries."),
 mt(3,s,V,[("bolsa de valores","stock exchange"),("materias primas","raw materials"),("cobre","copper"),("firma","signing")]),
 mc(4,s,"reading","","Which four countries founded the Pacific Alliance in 2011, according to the text?",
  ["Chile, Colombia, México y Perú.","Argentina, Brasil, Paraguay y Uruguay.","Bolivia, Colombia, Ecuador y Perú."],0)])
vocab(s,"The Pacific Alliance",[("bolsa de valores","stock exchange","expression"),("materias primas","raw materials","expression"),("cobre","copper","noun"),("firma","signing / signature","noun")])
P=["En 1969 Bolivia, Chile, Colombia, Ecuador y Perú firmaron el Acuerdo de Cartagena, que creó el Pacto Andino, hoy Comunidad Andina. Chile salió en 1976, y la Comunidad Andina sigue existiendo con cuatro miembros: Bolivia, Colombia, Ecuador y Perú.",
"El 28 de abril de 2011, en Lima, los presidentes de Chile, Colombia, México y Perú firmaron la Declaración de Lima y fundaron la Alianza del Pacífico. El acuerdo marco se firmó en 2012. Los cuatro países querían la libre circulación de bienes, servicios, capitales y personas, y una presencia mayor en la región de Asia-Pacífico. A diferencia del Mercosur, la Alianza no creó un arancel común.",
"Desde 2012 funciona una plataforma de movilidad estudiantil y académica que ofrece becas para estudiar en los países socios. En 2013 Chile y Colombia abrieron una embajada compartida en Ghana, un ejemplo de cooperación en el exterior.",
"El Mercado Integrado Latinoamericano, el MILA, une desde 2011 las bolsas de valores de Santiago, Bogotá y Lima, y en 2014 se unió la de México. Con este sistema se pueden comprar y vender acciones de empresas de los cuatro países. Aun cuando México no se hubiera unido, el MILA habría seguido funcionando con tres bolsas.",
"Los países de la Alianza venden a China, Japón y Corea del Sur, sobre todo, materias primas como el cobre, el petróleo y la harina de pescado. Según varios analistas, la Alianza necesita exportar productos con más valor agregado. En los últimos años, además, algunos gobiernos miembros han tenido desacuerdos políticos."]
wc(s,P)
story(s,"La Alianza del Pacífico","The Pacific Alliance was founded in Lima in 2011 by Chile, Colombia, Mexico and Peru; the text covers its aims, student grants, the MILA stock-market link and its raw-material exports to Asia, after the Andean Community of 1969.",P,[
 ("Which country left the Andean Pact in 1976, according to the text?",["Chile.","Perú.","Colombia."],0,"The first paragraph says Chile left in 1976."),
 ("What does the MILA do, according to the text?",["Une las bolsas de valores de Santiago, Bogotá, Lima y México.","Une los bancos centrales de Europa y Asia.","Une los puertos del Atlántico y del Pacífico."],0,"The fourth paragraph describes the MILA."),
 ("What do the Alliance countries sell mostly to China, Japan and South Korea, according to the text?",["Materias primas, como el cobre y el petróleo.","Aviones y computadoras.","Café y azúcar solamente."],0,"The last paragraph names raw materials.")])

# ---------- 03
s='b2-integracion-03'
lesson(s,"Bioceanic corridors: roads, passes and the port of Chancay","I can say how much of something led to a result, with *tan … que*, *tanto … que* and *de tal manera que*.")
grammar(s,"So Deep That: Results in Roads and Ports",[
 {"type":"text","title":"What you already know","content":"You know *tan … que*, *tanto … que* and *de tal manera que* from B2 Unit 31. They say how much of something led to a real result, so the verb after *que* is in the indicative. Roads, passes and ports give plenty of cases: how deep, how snowy, how high."},
 ex([("El puerto de Chancay es tan profundo que recibe barcos muy grandes.","The port of Chancay is so deep that it receives very large ships."),
     ("Nieva tanto en la cordillera que, a veces, el paso de Los Libertadores se cierra.","It snows so much in the mountains that sometimes the Los Libertadores pass closes."),
     ("Los Andes son tan altos que durante siglos separaron la costa del Pacífico del interior.","The Andes are so high that for centuries they separated the Pacific coast from the interior."),
     ("La carretera Interoceánica une Brasil y Perú de tal manera que los camiones cruzan los Andes.","The Interoceanic Highway joins Brazil and Peru in such a way that lorries cross the Andes.")]),
 T("tip","*Tan* goes before an adjective or an adverb and never changes. After a verb, or before a noun, use *tanto* (*tantos camiones*). The result is real, so the verb after *que* is in the indicative.")])
exercises(s,[
 mc(1,s,"grammar","consecutivas-de-tal-manera","Which sentence means \"The port of Chancay is so deep that it receives very large ships\"?",
  ["El puerto de Chancay es tan profundo que recibe barcos muy grandes.","El puerto de Chancay es tan profundo como recibe barcos muy grandes.","El puerto de Chancay es tanto profundo que recibe barcos muy grandes."],0),
 fb(2,s,"consecutivas-de-tal-manera","Nieva tanto en la cordillera que, a veces, las autoridades __ el paso de Los Libertadores.","cierran","It snows so much in the mountains that sometimes the authorities close the Los Libertadores pass."),
 mt(3,s,V,[("ferrocarril","railway"),("cordillera","mountain range"),("calado","draught (depth of water)"),("carretera","main road")]),
 mc(4,s,"reading","","What does the text say about the port of Chancay?",
  ["Está al norte de Lima y se abrió en noviembre de 2024.","Está al sur de Lima y se abrió en noviembre de 2024.","Está al norte de Lima y se abrió en noviembre de 1994."],0)])
vocab(s,"Roads, passes and ports",[("ferrocarril","railway","noun"),("cordillera","mountain range","noun"),("calado","draught (depth of water)","noun"),("carretera","main road","noun")])
P=["Los Andes han separado durante siglos la costa del Pacífico de las regiones del interior y del Atlántico. Hoy varios proyectos quieren unir los dos océanos por tierra, para que las mercancías de Brasil, Paraguay o Bolivia lleguen más rápido a los puertos del Pacífico y de ahí a Asia.",
"La Carretera Interoceánica Sur, terminada a comienzos de la década de 2010, une el estado brasileño de Acre con puertos del sur del Perú como Ilo, Matarani y San Juan de Marcona. Cruza la selva de Madre de Dios y los Andes. Los Andes son tan altos que esta carretera necesitó muchas obras de ingeniería.",
"Otro proyecto es el corredor vial bioceánico, que une Porto Murtinho, en Brasil, con los puertos del norte de Chile, pasando por Paraguay y el norte de Argentina. En julio de 2026, según informó la prensa paraguaya, se unieron las dos partes del puente sobre el río Paraguay entre Carmelo Peralta y Porto Murtinho; los accesos deben terminarse en 2027.",
"En el sur, el paso de Los Libertadores, entre Argentina y Chile, lo cruzan muchos camiones. Nieva tanto en la cordillera que, a veces, el paso se cierra en invierno. Por eso Argentina y Chile han estudiado un túnel de baja altura en Agua Negra, entre la provincia de San Juan y la región de Coquimbo. Es un proyecto binacional.",
"En noviembre de 2024 se inauguró el puerto de Chancay, a unos ochenta kilómetros al norte de Lima. Es un puerto de aguas profundas, tan profundo que puede recibir barcos muy grandes, y la empresa china COSCO Shipping tiene la mayoría de la inversión. Según sus promotores, el puerto acorta el viaje por mar entre Sudamérica y Asia."]
wc(s,P)
story(s,"Corredores entre dos océanos","Several road, rail and port projects try to link South America's Atlantic and Pacific sides: the Interoceanic Highway, the bioceanic road corridor, the Andean passes and the port of Chancay.",P,[
 ("What does the Interoceanic Highway join, according to the text?",["El estado brasileño de Acre con puertos del sur del Perú.","Buenos Aires con Montevideo.","Bogotá con Caracas."],0,"The second paragraph describes the route."),
 ("What happened in July 2026, according to Paraguayan press?",["Se unieron las dos partes del puente entre Carmelo Peralta y Porto Murtinho.","Se abrió el túnel de Agua Negra.","Se cerró el paso de Los Libertadores."],0,"The third paragraph reports the bridge."),
 ("What does the text say about the Agua Negra tunnel?",["Es un proyecto binacional de Argentina y Chile.","Ya lo usan todos los camiones.","Está en Perú."],0,"The fourth paragraph calls it a binational project.")])

# ---------- 04
s='b2-integracion-04'
lesson(s,"Shared energy: Itaipú, Yacyretá and the gas pipeline from Bolivia","I can describe two changes that grow together, with *a medida que* and *cuanto más … más …*.")
grammar(s,"As and The More: Changes That Go Together",[
 {"type":"text","title":"What you already know","content":"You know *a medida que* and *cuanto más …, más …* from B1 Unit 2. *A medida que* + indicative describes a change in progress (\"as\"), and *cuanto más …, más …* says that the second change grows with the first (\"the more …, the more …\"); *cuanto menos* gives the opposite direction. An electric grid is a good case: demand, rain and power all move together."},
 ex([("A medida que crece el consumo de Paraguay, queda menos energía para vender a Brasil.","As Paraguay's consumption grows, less energy is left to sell to Brazil."),
     ("A medida que aumenta la demanda, las centrales producen más.","As demand increases, the power stations produce more."),
     ("Cuanto más se conectan las redes eléctricas, más fácil es compartir electricidad.","The more the electricity grids are connected, the easier it is to share electricity."),
     ("Cuanto menos llueve en la cuenca del Paraná, menos electricidad producen las centrales.","The less it rains in the Paraná basin, the less electricity the power stations produce.")]),
 T("tip","After *a medida que* use the indicative for a change that is really happening. *Cuanto* does not change when a verb follows it, and the second half starts with *más* or *menos*: *cuanto más estudio, más entiendo*.")])
exercises(s,[
 mc(1,s,"grammar","cuanto-mas-tanto-mas","Which sentence means \"The more electricity a country uses, the more it needs to produce\"?",
  ["Cuanto más electricidad usa un país, más necesita producir.","Cuanto más electricidad usa un país, menos necesita producir.","Cuanto más electricidad usa un país, mejor necesita producir."],0),
 fb(2,s,"cuanto-mas-tanto-mas","A medida que __ la demanda de electricidad, las centrales producen más.","aumenta","As the demand for electricity increases, the power stations produce more."),
 mt(3,s,V,[("represa","dam"),("central eléctrica","power station"),("excedente","surplus"),("gasoducto","gas pipeline")]),
 mc(4,s,"reading","","How is the energy of Itaipú shared, according to the text?",
  ["Brasil y Paraguay tienen derecho a la mitad cada uno.","Brasil tiene derecho a toda la energía de la central.","Paraguay tiene derecho a más de la mitad de la energía."],0)])
vocab(s,"Dams, power and gas",[("represa","dam","noun"),("central eléctrica","power station","expression"),("excedente","surplus","noun"),("gasoducto","gas pipeline","noun")])
P=["El río Paraná marca parte de la frontera entre Brasil y Paraguay y, más al sur, entre Argentina y Paraguay. En ese río hay dos grandes centrales hidroeléctricas binacionales: Itaipú, de Brasil y Paraguay, y Yacyretá, de Argentina y Paraguay. Los tratados de las dos centrales se firmaron en 1973.",
"Itaipú empezó a producir electricidad en 1984 y tiene una capacidad de catorce mil megavatios. Según el tratado, cada país tiene derecho a la mitad de la energía. Paraguay usa solo una parte de su mitad y, según el tratado, vende el excedente a Brasil. Itaipú cubre la mayor parte de la electricidad que consume Paraguay. A medida que crece el consumo de Paraguay, queda menos excedente para vender.",
"El Anexo C del tratado fija las bases financieras de la central. El tratado preveía revisarlo a los cincuenta años, en 2023, y desde entonces Brasil y Paraguay negocian esa revisión. Paraguay ha pedido poder vender su energía sobrante a otros compradores.",
"El gasoducto Bolivia-Brasil, de más de tres mil kilómetros, lleva gas boliviano a Brasil desde 1999, hasta São Paulo y el sur del país. Además, hay líneas eléctricas que conectan a Argentina, Brasil, Paraguay y Uruguay y permiten intercambiar electricidad. Cuanto más se conectan las redes, más fácil es compartir la energía entre países."]
wc(s,P)
story(s,"Energía compartida en el Cono Sur","Itaipú and Yacyretá, two dams on the Paraná built under 1973 treaties, the sharing of Itaipú's power between Brazil and Paraguay, the review of its Annex C and the gas pipeline from Bolivia.",P,[
 ("Which two countries own the Itaipú power station, according to the text?",["Brasil y Paraguay.","Argentina y Uruguay.","Bolivia y Chile."],0,"The first paragraph names them."),
 ("What does Paraguay do with the energy it does not use, according to the text?",["Vende el excedente a Brasil.","Lo vende a Europa.","Lo pierde."],0,"The second paragraph says it sells the surplus to Brazil."),
 ("Since when does the gas pipeline carry Bolivian gas to Brazil, according to the text?",["Desde 1999.","Desde 1973.","Desde 2023."],0,"The last paragraph gives the year.")])

# ---------- 05
s='b2-integracion-05'
lesson(s,"Towards South American citizenship: residence, identity cards and degrees","I can say what should happen, with *es importante que* and other value judgments + subjunctive.")
grammar(s,"It Is Important That: Judgments About Agreements",[
 {"type":"text","title":"What you already know","content":"You know *es importante que*, *es necesario que* and *es mejor que* from A2 Unit 27: after a value judgment about what other people should do, the verb after *que* is in the present subjunctive. Agreements about residence, identity cards and degrees are written in just this way: what governments should recognise and allow."},
 ex([("Es importante que los países reconozcan los documentos de identidad de los demás.","It is important that countries recognise each other's identity documents."),
     ("Es necesario que los trabajadores migrantes tengan los mismos derechos que los ciudadanos del país.","It is necessary that migrant workers have the same rights as the country's citizens."),
     ("Es mejor que los trámites sean rápidos.","It is better that the paperwork is quick."),
     ("Es una lástima que algunos títulos no se reconozcan en otros países.","It is a pity that some degrees are not recognised in other countries.")]),
 T("tip","For a general idea use the infinitive (*Es importante reconocer los títulos*); when a new subject follows, use *que* and the subjunctive (*Es importante que los países reconozcan los títulos*).")])
exercises(s,[
 mc(1,s,"grammar","subjunctive-value-judgments","Which sentence means \"It is important that countries recognise each other's identity documents\"?",
  ["Es importante que los países reconozcan los documentos de los demás.","Es importante que los países reconocen los documentos de los demás.","Es importante que los países reconozca los documentos de los demás."],0,{1:"present-tense"}),
 fb(2,s,"subjunctive-value-judgments","Es importante que los trabajadores migrantes __ los mismos derechos que los ciudadanos del país.","tengan","It is important that migrant workers have the same rights as the country's citizens."),
 mt(3,s,V,[("residencia","residence permit"),("ciudadanía","citizenship"),("título","degree certificate"),("migrante","migrant")]),
 mc(4,s,"reading","","What does the Residence Agreement allow, according to the text?",
  ["Vivir y trabajar en otro país del acuerdo.","Votar en las elecciones nacionales de cualquier país.","Trabajar solo en el país donde se nació."],0)])
vocab(s,"Residence and citizenship",[("residencia","residence permit","noun"),("ciudadanía","citizenship","noun"),("título","degree certificate","noun"),("migrante","migrant","noun")])
P=["Además del comercio, los acuerdos de integración tratan también de las personas: de quienes cruzan las fronteras para trabajar, estudiar o reunirse con su familia.",
"En 2002 los países del Mercosur y sus asociados Bolivia y Chile firmaron el Acuerdo de Residencia, que se aplica desde 2009. Según el acuerdo, un ciudadano de un país firmante puede pedir una residencia temporal de dos años en otro país firmante, si presenta su nacionalidad y no tiene antecedentes penales graves. Después puede pedir la residencia permanente. Los residentes tienen derecho a trabajar y a recibir el mismo trato que los ciudadanos en áreas como la educación y la salud. Más tarde, otros países, como Colombia, Ecuador y Perú, se sumaron al acuerdo.",
"La UNASUR se creó en 2008. Desde 2018 varios miembros se retiraron o suspendieron su participación, y Brasil volvió en 2023. En varios países sudamericanos los turistas pueden entrar con el documento nacional de identidad en vez del pasaporte.",
"El sistema ARCU-SUR, del Mercosur, acredita la calidad de algunas carreras universitarias, como medicina, ingeniería o agronomía. Esa acreditación facilita el reconocimiento de los títulos entre países, pero no lo garantiza. Algunas organizaciones de migrantes han pedido que los trámites sean más rápidos y que los países apliquen estos acuerdos con menos obstáculos."]
wc(s,P)
story(s,"Hacia una ciudadanía sudamericana","The text covers the 2002 Residence Agreement, the identity-card travel rules, the history of UNASUR and the ARCU-SUR degree accreditation, as steps towards free movement of people in South America.",P,[
 ("How long is the temporary residence under the Residence Agreement, according to the text?",["Dos años.","Diez años.","Un mes."],0,"The second paragraph says two years."),
 ("What can many tourists use instead of a passport in South America, according to the text?",["El documento nacional de identidad.","Una carta de su presidente.","Un boleto de avión."],0,"The third paragraph says so."),
 ("What does ARCU-SUR do, according to the text?",["Acredita la calidad de algunas carreras universitarias.","Cierra las universidades privadas.","Da becas a todos los estudiantes."],0,"The last paragraph describes it.")])

# ---------- consolidation
s='b2-integracion-consolidation'
lesson(s,"Review: bridges, treaties and shared resources in South America","I can use conditions, past conditions, results and value judgments to talk about South American integration.")
exercises(s,[
 mc(1,s,"grammar","conditional-conjunctions","Which sentence means \"The agreement will work as long as everyone follows the rules\"?",
  ["El acuerdo funcionará siempre que todos sigan las reglas.","El acuerdo funcionará siempre que todos siguen las reglas.","El acuerdo funcionará a menos que todos sigan las reglas."],0,{1:"present-tense"}),
 mc(2,s,"grammar","inversiones-condicionales-de-haber","Which sentence means \"Had we been in Chancay in November 2024, we would have seen the new port\"?",
  ["Hubiéramos estado en Chancay en noviembre de 2024, habríamos visto el puerto nuevo.","Hubiéramos estado en Chancay en noviembre de 2024, habremos visto el puerto nuevo.","Habíamos estado en Chancay en noviembre de 2024, habríamos visto el puerto nuevo."],0,{1:"futuro-perfecto",2:"pluscuamperfecto"}),
 fb(3,s,"consecutivas-de-tal-manera","Itaipú produce tanta energía que Paraguay no __ toda su parte.","usa","Itaipú produces so much energy that Paraguay does not use all its share."),
 mc(4,s,"reading","","Which treaty created Mercosur, according to the lesson texts?",
  ["El Tratado de Asunción, de 1991.","El Acuerdo de Cartagena, de 1969.","La Declaración de Lima, de 2011."],0)])
