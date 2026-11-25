from lib import *
U='b2-el-salvador-honduras-vocab'
# ---------- 01 ----------
s='b2-salvadorhonduras-01'
lesson(s,'Copán and the Gulf of Fonseca: a Maya city and a shared gulf',
 'Describe Copán and the Gulf of Fonseca, and say whose monuments and coasts they are, with cuyo.',
 'possessive relative clauses with cuyo (review)',
 ['In this lesson you read about Copán, a Maya city in western Honduras, and about the Gulf of Fonseca, which three countries share. The text is in Spanish; the screens and instructions are in English.',
  'The grammar is the one you know for saying "whose": *cuyo*, *cuya*, *cuyos*, *cuyas*.'],
 ['I can say whose monuments or coasts I am talking about, with *cuyo*, *cuya*, *cuyos* and *cuyas*.',
  'I can describe the stelae and the Hieroglyphic Stairway of Copán.',
  'I can say which three countries share the Gulf of Fonseca.'])
grammar(s,'Whose Stelae? Whose Coasts?',[
 {'type':'text','title':'What you already know','content':'You know *cuyo* from B1 Unit 5. It means "whose" and joins the owner to the thing owned. It agrees with the thing owned, not with the owner, and no article goes before it. It is a good tool for describing places: Copán, *cuyas* stelae are famous, and the gulf, *cuyas* coasts belong to three countries.'},
 {'type':'table','title':'Cuyo agrees with the thing owned','rows':[
  ['un rey cuyo nombre aparece en la escalinata','a king whose name appears on the stairway'],
  ['una ciudad cuya historia está escrita en piedra','a city whose history is written in stone'],
  ['la escalinata, cuyos escalones llevan glifos','the stairway, whose steps carry glyphs'],
  ['el golfo, cuyas costas pertenecen a tres países','the gulf, whose coasts belong to three countries']]},
 {'type':'examples','title':'At work in Honduras','items':[
  {'spanish':'Copán es una ciudad maya cuyas estelas fueron talladas en piedra volcánica.','english':'Copán is a Maya city whose stelae were carved in volcanic stone.'},
  {'spanish':'La escalinata, cuyos escalones llevan más de dos mil glifos, cuenta la historia de la dinastía.','english':'The stairway, whose steps carry more than two thousand glyphs, tells the history of the dynasty.'},
  {'spanish':'El golfo de Fonseca, cuyas aguas son compartidas, tiene manglares en sus orillas.','english':'The Gulf of Fonseca, whose waters are shared, has mangroves on its shores.'},
  {'spanish':'Conocimos a una arqueóloga cuyo trabajo ayuda a leer los glifos.','english':'We met an archaeologist whose work helps to read the glyphs.'}]},
 {'type':'tip','content':'Do not put *que* before the possessive: not *una ciudad que sus estelas…*, but *una ciudad cuyas estelas…*. And no article: not *el cuyo*.'}])
vocab(s,'Maya stone and shared waters','Copán, its stairway and the Gulf of Fonseca',[
 ('la estela','stela, carved stone slab','noun'),('la escalinata','stairway, flight of steps','noun'),('el glifo','glyph','noun'),
 ('tallar','to carve','verb'),('la dinastía','dynasty','noun'),('el golfo','gulf','noun'),('el manglar','mangrove swamp','noun')])
ex(s,[
 match(s+'.ex01',[['la estela','stela, carved stone slab'],['el glifo','glyph'],['la dinastía','dynasty'],['el manglar','mangrove swamp']],U),
 mc(s+'.ex02','Which sentence says "Copán is a city whose stelae are famous"?',
  ['Copán es una ciudad cuyas estelas son famosas.','Copán es una ciudad cuyos estelas son famosas.','Copán es una ciudad que sus estelas son famosas.'],teaches='relativo-posesivo-cuyo'),
 fb(s+'.ex03','La escalinata, __ escalones llevan más de dos mil glifos, cuenta la historia de la dinastía.','cuyos','The stairway, whose steps carry more than two thousand glyphs, tells the history of the dynasty.','relativo-posesivo-cuyo'),
 sb(s+'.ex04',['El','golfo','de','Fonseca,','cuyas','costas','pertenecen','a','tres','países,','tiene','manglares.'],'The Gulf of Fonseca, whose coasts belong to three countries, has mangroves.','relativo-posesivo-cuyo'),
 dlg(s+'.ex05',[('Meg','¿Por qué es famosa Copán?'),('Carlos','_____'),('Meg','Entonces voy a ver las estelas.')],
  ['Por sus estelas, cuyas figuras salen de la piedra casi como estatuas.','Por su golfo, cuyas costas pertenecen a tres países y tienen manglares.','Por sus montañas, cuyos ríos bajan hacia el golfo de Fonseca.'],U),
 dic(s+'.ex06','Copán es una ciudad maya cuyas estelas fueron talladas en piedra volcánica.','Copán is a Maya city whose stelae were carved in volcanic stone.','relativo-posesivo-cuyo')])
story(s,'Copán y el golfo de Fonseca','Copán was a Maya city in western Honduras famous for its carved stelae and its Hieroglyphic Stairway; the Gulf of Fonseca, to the south, is shared by three countries.',
 ['Escultura maya','Escritura jeroglífica','El golfo de Fonseca'],['pronombre relativo cuyo'],[
 'Copán está en el oeste de Honduras, cerca de la frontera con Guatemala. Fue una de las grandes ciudades mayas. Según las inscripciones, el fundador de su dinastía, K\'inich Yax K\'uk\' Mo\', llegó al valle en el año 426, y la dinastía gobernó hasta el siglo IX.',
 'Copán es famosa por su escultura. Los escultores tallaron en piedra volcánica estelas cuyas figuras salen de la piedra casi como estatuas. Muchas de las estelas de la Gran Plaza representan a un gobernante conocido como 18 Conejo, que gobernó a finales del siglo VII y principios del VIII.',
 'La Escalinata Jeroglífica, cuyos escalones llevan más de dos mil glifos, cuenta la historia de la dinastía. Los especialistas la consideran la inscripción jeroglífica más larga que se conoce del mundo maya.',
 'Hacia el siglo IX Copán fue abandonada poco a poco. Muchos arqueólogos piensan que el crecimiento de la población y la pérdida de bosques dañaron los cultivos, pero las causas siguen en discusión. En 1839, el viajero estadounidense John Lloyd Stephens y el dibujante inglés Frederick Catherwood visitaron las ruinas, y sus dibujos las dieron a conocer fuera de Centroamérica. En 1980 la UNESCO declaró el sitio Patrimonio de la Humanidad.',
 'En el sur, en la costa del océano Pacífico, está el golfo de Fonseca, cuyas costas pertenecen a tres países: El Salvador, Honduras y Nicaragua. En sus orillas hay manglares, donde viven peces, camarones y aves. En 1992, la Corte Internacional de Justicia decidió que las aguas del golfo son comunes a los tres países.'],
 [('What does the text say about the Hieroglyphic Stairway of Copán?',['Tiene más de dos mil glifos.','Tiene solo diez glifos.','Está en Guatemala.','Es de la época colonial.'],0,'The text says its steps carry more than two thousand glyphs.'),
  ('According to the text, what is the Gulf of Fonseca?',['Un golfo del Pacífico con costas de tres países.','Un lago de Honduras.','Un río de Guatemala.','Una isla del Caribe.'],0,'The gulf has coasts in El Salvador, Honduras and Nicaragua.'),
  ('What happened to Copán around the ninth century?',['Fue abandonada poco a poco.','Fue fundada por Stephens.','Fue declarada Patrimonio de la Humanidad.','Fue cubierta por el mar.'],0,'The text says it was abandoned little by little.')])
