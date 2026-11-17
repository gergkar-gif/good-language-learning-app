import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
from u25_text import T25
P='c1-alkotmanyjog'
V='c1-constitutional-breakdown-vocab'
def tbl(rows): return {'type':'table','title':'Patterns in Context','rows':[list(r) for r in rows]}
def txt(t,c): return {'type':'text','title':t,'content':c}

L=[]
# ---------------- Lesson 1
L.append(dict(s='01',title='The Fundamental Law of 2011',grammar_name='Recap: attributing a judgement with szerint',
 goals=["I can describe how the Fundamental Law was adopted in 2011, with the dates and the source of each view (*Alaptörvény, Nemzeti Hitvallás, sarkalatos törvény*).",
        "I can name the source of a judgement about the past with *szerint* (*a Velencei Bizottság 2011-es véleménye szerint*).",
        "I can state how the pro-government side and its critics judged the way the text was prepared."],
 gr=dict(title='Recap: Attributing a Judgement',sections=[
  txt('How it works',"You know *szerint* from B1 Unit 13 (*a hírek szerint*, *úgy tűnik*): it names who says something. A history of a disputed period needs it for every judgement: *a kormány szerint*, *a bírálók szerint*, *a Velencei Bizottság 2011-es véleménye szerint*. *szerint* stands after the noun and takes no ending, and the verb stays in the past: *A kormány szerint az 1989-es szöveg átmeneti volt.* New in this lesson is the vocabulary of constitutional law."),
  txt('Example',"Example: *A bírálók szerint a tervezetet rövid idő alatt vitatták meg.*"),
  tbl([("A kormánypárti oldal szerint az 1989-es szöveg csak átmeneti megoldás volt.","According to the pro-government side, the 1989 text was only a provisional solution."),
       ("A bírálók szerint a tervezetet rövid idő alatt vitatták meg.","According to the critics, the draft was discussed in a short time."),
       ("A Velencei Bizottság 2011-es véleménye szerint a sarkalatos törvények köre aggályos volt.","According to the Venice Commission's opinion of 2011, the range of cardinal laws was a cause for concern.")])]),
 vocab=[('Alaptörvény','Fundamental Law (the constitution in force since 2012)','noun'),
  ('Nemzeti Hitvallás','National Avowal (the preamble of the Fundamental Law)','expression'),
  ('sarkalatos törvény','cardinal law (needs a two-thirds vote)','expression'),
  ('kétharmados többség','two-thirds majority','expression'),
  ('nemzeti konzultáció','national consultation (a government questionnaire)','expression'),
  ('tervezet','draft','noun'),('választó','voter','noun'),
  ('Velencei Bizottság',"Venice Commission (the Council of Europe's advisory body on constitutional law)",'noun')],
 ex=[
  mc(f'{P}-01-introduce-1','introduce','vocabulary',V,'Mit jelent a sarkalatos törvény kifejezés?',
     ['Olyan törvény, amelyet kétharmados többséggel fogadtak el.','Olyan törvény, amelyről a választók népszavazáson döntöttek.','Olyan törvény, amelyet a köztársasági elnök maga hozott.'],0),
  fb(f'{P}-01-controlled-2','controlled','grammar','evidentials','A kormánypárti oldal _____ az 1989-es szöveg csak átmeneti megoldás volt.','According to the pro-government side, the 1989 text was only a provisional solution.',['szerint']),
  mt(f'{P}-01-controlled-3','controlled',V,[('Alaptörvény','Magyarország alkotmánya 2012. január 1-jétől'),('Nemzeti Hitvallás','az Alaptörvény bevezető szövege'),('nemzeti konzultáció','kérdőíves megkérdezés a kormány kezdeményezésére'),('tervezet','a törvényszöveg első változata')]),
  fb(f'{P}-01-practice-4','practice','grammar','evidentials','A Velencei Bizottság 2011-es véleménye _____ a sarkalatos törvények köre aggályos volt.',"According to the Venice Commission's opinion of 2011, the range of cardinal laws was a cause for concern.",['szerint']),
  sb(f'{P}-01-practice-5','practice','evidentials','A bírálók szerint a tervezetet rövid idő alatt vitatták meg.','According to the critics, the draft was discussed in a short time.'),
  dl(f'{P}-01-dialogue-6','evidentials',[('Kérdező','Mit gondolt a Velencei Bizottság 2011-ben az új szövegről?'),('Válaszadó','A Velencei Bizottság véleménye _____ a szöveg több eleme megfelelt az európai normáknak.')],['szerint','helyett','óta'],0),
  sw(f'{P}-01-production-7','production','evidentials','Write two sentences: say how the pro-government side and its critics judged the preparation of the Fundamental Law. Name the source of each view.','A kormánypárti oldal szerint az 1989-es szöveg csak átmeneti megoldás volt, a bírálók szerint viszont a tervezetet rövid idő alatt vitatták meg.'),
  mc(f'{P}-01-check-8','check','grammar','evidentials','Melyik mondat helyes?',
     ['A kormánypárti oldal szerint az 1989-es szöveg átmeneti volt.','A kormánypárti oldal szerinte az 1989-es szöveg átmeneti volt.','A kormánypárti szerint oldal az 1989-es szöveg átmeneti volt.'],0,ds={1:'inflected-postpositions'}),
 ]))
# ---------------- Lesson 2
L.append(dict(s='02',title='The Constitutional Court, 2010–2013',grammar_name='Recap: obligation in the past with köteles volt and kénytelen volt',
 goals=["I can describe the changes to the Constitutional Court's powers between 2010 and 2013, with their dates (*hatáskör, alkotmányjogi panasz, actio popularis*).",
        "I can say what a rule required in the past with *köteles volt* and *kénytelen volt* (*a panaszos köteles volt kimeríteni a jogorvoslatokat*).",
        "I can report how the government and its critics judged these changes."],
 gr=dict(title='Recap: Obligation in the Past',sections=[
  txt('How it works',"You know *köteles* and *kénytelen* from B1 Unit 10: they say that a rule or a circumstance required someone to do something. In a history they describe what a rule required at the time, so the verb *volt* follows them: *a panaszos köteles volt kimeríteni a rendes jogorvoslatokat*. With a plural subject *köteles* takes the plural ending: *a bíróságok kötelesek voltak*. New in this lesson is the vocabulary of constitutional courts."),
  txt('Example',"Example: *2012 után az érintett köteles volt előbb kimeríteni a rendes jogorvoslatokat.*"),
  tbl([("A panaszos köteles volt kimeríteni a rendes jogorvoslatokat.","The complainant had to exhaust the ordinary legal remedies."),
       ("Az érintettek kötelesek voltak előbb kimeríteni a rendes jogorvoslatokat.","Those affected had to exhaust the ordinary legal remedies first."),
       ("A panaszos kénytelen volt előbb más jogorvoslatot igénybe venni.","The complainant had to use another legal remedy first.")])]),
 vocab=[('Alkotmánybíróság','Constitutional Court','noun'),('actio popularis','popular action (anyone could request a review of a law)','expression'),
  ('alkotmányjogi panasz','constitutional complaint','expression'),('jogorvoslat','legal remedy','noun'),('hatáskör','powers, competence','noun'),
  ('államadósság','public debt','noun')],
 ex=[
  mc(f'{P}-02-introduce-1','introduce','vocabulary',V,'Mit jelent az actio popularis?',
     ['Bárki kérhette egy jogszabály vizsgálatát az Alkotmánybíróságtól.','Az alkotmánybírák megválasztása az Országgyűlésben.','A köztársasági elnök joga a törvények aláírására.'],0),
  fb(f'{P}-02-controlled-2','controlled','grammar','formal-obligation','A panaszos köteles _____ kimeríteni a rendes jogorvoslatokat.','The complainant had to exhaust the ordinary legal remedies.',['volt'],hint='lenni, third person, past'),
  mt(f'{P}-02-controlled-3','controlled',V,[('hatáskör','amit egy szerv jogszerűen elvégezhet'),('jogorvoslat','lehetőség a döntés megfellebbezésére'),('államadósság','az állam tartozása'),('alkotmányjogi panasz','az érintett kérelme az Alkotmánybírósághoz')]),
  fb(f'{P}-02-practice-4','practice','grammar','formal-obligation','2012-től az érintett _____ volt előbb minden más jogorvoslatot igénybe venni.','From 2012 the person concerned had to use every other legal remedy first.',['kénytelen','köteles']),
  sb(f'{P}-02-practice-5','practice','formal-obligation','Az érintett kénytelen volt előbb kimeríteni a rendes jogorvoslatokat.','The person concerned had to exhaust the ordinary legal remedies first.'),
  dl(f'{P}-02-dialogue-6','formal-obligation',[('Kérdező','Mit írt elő a szabály 2012 után annak, aki alkotmányjogi panaszt nyújtott be?'),('Válaszadó','A panaszos _____ volt kimeríteni a rendes jogorvoslatokat.')],['köteles','kötelezően','kötelezés'],0),
  sw(f'{P}-02-production-7','production','formal-obligation','Write two sentences about the rules for a constitutional complaint from 2012: say what the complainant had to do first and what happened to the actio popularis.','2012-től az érintett köteles volt előbb kimeríteni a rendes jogorvoslatokat, az actio popularis pedig megszűnt.'),
  mc(f'{P}-02-check-8','check','grammar','formal-obligation','Melyik mondat helyes?',
     ['Az érintettek kötelesek voltak kimeríteni a jogorvoslatokat.','Az érintettek köteles voltak kimeríteni a jogorvoslatokat.','Az érintettek kötelesek voltak kimerítenie a jogorvoslatokat.'],0,ds={2:'inflected-infinitives'}),
 ]))
# ---------------- Lesson 3
L.append(dict(s='03',title='States of Danger and Government Decrees, 2020–2022',grammar_name='Recap: proportion with minél … annál',
 goals=["I can describe the states of danger of 2020 and 2022 and the decrees issued under them, with dates (*veszélyhelyzet, kormányrendelet, felhatalmazás*).",
        "I can link two changing quantities with *minél … annál* (*minél gyorsabban születtek meg a szabályok, annál hatékonyabb lehetett a védekezés*).",
        "I can report how the government and its critics argued about the state of danger."],
 gr=dict(title='Recap: Proportion with minél … annál',sections=[
  txt('How it works',"You know *minél … annál* from B1 Unit 2 (*minél többet olvasok, annál többet értek*): two comparatives change together. In a history the comparison usually belongs to somebody's argument, so the source comes first and the verbs are in the past: *A kormány szerint minél gyorsabban születtek meg a szabályok, annál hatékonyabb lehetett a védekezés.* Both parts take the comparative in *-bb*. New in this lesson is the vocabulary of emergency law."),
  txt('Example',"Example: *Az ellenzék szerint minél tovább tartott az időbeli korlát nélküli felhatalmazás, annál nagyobb volt a jogbizonytalanság kockázata.*"),
  tbl([("A kormány szerint minél gyorsabban születtek meg a szabályok, annál hatékonyabb lehetett a védekezés.","According to the government, the faster the rules were made, the more effective the response could be."),
       ("Az ellenzék szerint minél tovább tartott az időbeli korlát nélküli felhatalmazás, annál nagyobb volt a jogbizonytalanság kockázata.","According to the opposition, the longer the authorisation without a time limit lasted, the greater the risk of legal uncertainty was."),
       ("Az ellenzék szerint minél hosszabb ideig szólt a felhatalmazás, annál nagyobb volt a bizonytalanság.","According to the opposition, the longer the authorisation ran, the greater the uncertainty was.")])]),
 vocab=[('veszélyhelyzet','state of danger (a special legal order)','noun'),('kormányrendelet','government decree','noun'),('felhatalmazás','authorisation','noun'),
  ('hatályon kívül helyez','to repeal','verb'),('meghosszabbít','to extend','verb'),('különleges jogrend','special legal order','expression'),('eltér','to deviate (from)','verb'),('ülésezik','to sit in session','verb'),('jogbizonytalanság','legal uncertainty','noun')],
 ex=[
  mc(f'{P}-03-introduce-1','introduce','vocabulary',V,'Mit jelentett a veszélyhelyzet a magyar jogrendben?',
     ['Különleges jogrendet, amelyben a kormány rendelettel eltérhetett egyes törvényektől.','Olyan időszakot, amelyben az Országgyűlés nem ülésezhetett.','Olyan jogrendet, amelyben az Alkotmánybíróság vezette az államot.'],0),
  fb(f'{P}-03-controlled-2','controlled','grammar','correlative-minel-annal','A kormány szerint minél gyorsabban születtek meg a szabályok, _____ hatékonyabb lehetett a védekezés.','According to the government, the faster the rules were made, the more effective the response could be.',['annál']),
  mt(f'{P}-03-controlled-3','controlled',V,[('veszélyhelyzet','különleges jogrend válsághelyzetben'),('kormányrendelet','a kormány által kiadott jogszabály'),('felhatalmazás','jogosultság, amelyet a törvény ad'),('hatályon kívül helyez','megszüntet egy jogszabályt'),('meghosszabbít','hosszabb időre érvényessé tesz')]),
  fb(f'{P}-03-practice-4','practice','grammar','correlative-minel-annal','Az ellenzék szerint _____ tovább tartott az időbeli korlát nélküli felhatalmazás, annál nagyobb volt a jogbizonytalanság kockázata.','According to the opposition, the longer the authorisation without a time limit lasted, the greater the risk of legal uncertainty was.',['minél']),
  sb(f'{P}-03-practice-5','practice','correlative-minel-annal','A kormány szerint minél gyorsabban születtek meg a szabályok, annál hatékonyabb lehetett a védekezés.','According to the government, the faster the rules were made, the more effective the response could be.'),
  dl(f'{P}-03-dialogue-6','correlative-minel-annal',[('Kérdező','Mivel indokolta a kormány 2020-ban a gyors döntéseket?'),('Válaszadó','Azzal, hogy minél gyorsabban születtek meg a szabályok, _____ hatékonyabb lehetett a védekezés.')],['annál','minél','mint'],0),
  sw(f'{P}-03-production-7','production','correlative-minel-annal','Write one sentence with minél … annál: say what the opposition held about the authorisation without a time limit.','Az ellenzék szerint minél tovább tartott az időbeli korlát nélküli felhatalmazás, annál nagyobb volt a jogbizonytalanság kockázata.'),
  mc(f'{P}-03-check-8','check','grammar','correlative-minel-annal','Which pair of words means \'the longer … the more …\'?',
     ['minél … annál','nem csak … hanem','egyrészt … másrészt'],0,ds={1:'nem-csak-hanem',2:'egyreszt-masreszt'}),
 ]))
# ---------------- Lesson 4
L.append(dict(s='04',title='Courts and Public Offices, 2011–2016',grammar_name='Recap: degrees of certainty with valószínűleg, feltehetőleg and aligha',
 goals=["I can describe the rules on judges and public offices between 2011 and 2016, with their dates (*nyugdíjkorhatár, Országos Bírói Hivatal, Kúria*).",
        "I can mark how certain a claim is with *valószínűleg*, *feltehetőleg* and *aligha* (*aligha vitatható*).",
        "I can report what the European courts and the Venice Commission found, giving the year."],
 gr=dict(title='Recap: Degrees of Certainty',sections=[
  txt('How it works',"You know *aligha*, *minden bizonnyal* and *feltehetőleg* from C1 Unit 3: *feltehetőleg* marks a claim as probable, *minden bizonnyal* as very probable, *aligha* as unlikely; *valószínűleg* works like *feltehetőleg*. In a history they keep an assessment apart from the established facts: the dates and the court rulings are stated plainly, while a judgement about effects gets a hedge and a source: *A bírálók szerint a szabály feltehetőleg gyengítette a bírák függetlenségét.* New in this lesson is the vocabulary of the judiciary."),
  txt('Example',"Example: *Aligha vitatható, hogy a korhatár csökkentése több bíró megbízatását megszüntette.*"),
  tbl([("A bírálók szerint a szabály feltehetőleg gyengítette a bírák függetlenségét.","According to the critics, the rule probably weakened the independence of judges."),
       ("Aligha vitatható, hogy a korhatár csökkentése több bíró megbízatását megszüntette.","It can hardly be disputed that lowering the age limit ended the mandates of several judges."),
       ("A korhatár csökkentése valószínűleg hatással volt a bírói kar összetételére.","The lowering of the age limit probably affected the composition of the judiciary.")])]),
 vocab=[('nyugdíjkorhatár','retirement age','noun'),('Országos Bírói Hivatal','National Judicial Office','noun'),('Kúria','Kúria (the supreme court of Hungary)','noun'),
  ('megbízatás','mandate, term of office','noun'),('tisztség','public office','noun'),('egyenlő bánásmód','equal treatment','expression'),('bírói függetlenség','judicial independence','expression')],
 ex=[
  mc(f'{P}-04-introduce-1','introduce','vocabulary',V,'Mit jelent a megbízatás szó?',
     ['Az az időszak, amelyre valakit tisztségre választottak.','Az a törvény, amely a bírói fizetést szabályozza.','Az a testület, amely az ítéleteket felülvizsgálja.'],0),
  fb(f'{P}-04-controlled-2','controlled','grammar','epistemic-hedging','A bírálók szerint a szabály _____ gyengítette a bírák függetlenségét.','According to the critics, the rule probably weakened the independence of judges.',['feltehetőleg','valószínűleg']),
  mt(f'{P}-04-controlled-3','controlled',V,[('nyugdíjkorhatár','az az életkor, amelyben a munkavállaló nyugdíjba megy'),('Kúria','Magyarország legfőbb bírósága'),('Országos Bírói Hivatal','a bíróságok igazgatását végző szerv'),('egyenlő bánásmód','a megkülönböztetés tilalma'),('bírói függetlenség','a bírák függetlensége más hatalmi ágaktól')]),
  fb(f'{P}-04-practice-4','practice','grammar','epistemic-hedging','A korhatár csökkentése _____ hatással volt a bírói kar összetételére.','The lowering of the age limit probably affected the composition of the judiciary.',['valószínűleg','feltehetőleg']),
  sb(f'{P}-04-practice-5','practice','epistemic-hedging','Aligha vitatható, hogy a korhatár csökkentése több bíró megbízatását megszüntette.','It can hardly be disputed that lowering the age limit ended the mandates of several judges.'),
  dl(f'{P}-04-dialogue-6','epistemic-hedging',[('Kérdező','Mennyire biztos, hogy a szabály gyengítette a bírák függetlenségét?'),('Válaszadó','Ez _____ így volt, de a vélemények megoszlottak.')],['valószínűleg','kétségtelenül','természetesen'],0),
  sw(f'{P}-04-production-7','production','epistemic-hedging','Write two sentences about the retirement age of judges: state the change with its year and then give one hedged assessment of its effect.','2012-ben a bírák kötelező nyugdíjkorhatára hetvenről hatvankét évre csökkent, és ez valószínűleg hatással volt a bírói kar összetételére.'),
  mc(f'{P}-04-check-8','check','grammar','epistemic-hedging','Which sentence presents the effect on the judiciary as probable, but not certain?',
     ['A korhatár csökkentése valószínűleg hatással volt a bírói kar összetételére.','A korhatár csökkentése kétségtelenül hatással volt a bírói kar összetételére.','A korhatár csökkentése aligha volt hatással a bírói kar összetételére.'],0),
 ]))
# ---------------- Lesson 5
L.append(dict(s='05',title='The European Rule-of-Law Procedures and the 2026 Election',grammar_name='Recap: contrast with viszont and ezzel szemben',
 goals=["I can describe the European rule-of-law procedures of 2018–2023 and the change of government in 2026, with dates (*jogállamiság, felfüggesztés, állásfoglalás*).",
        "I can set two views against each other with *viszont* and *ezzel szemben* (*a kormány szerint …, ezzel szemben az Európai Parlament szerint …*).",
        "I can report, with attribution, how each side judged the procedures."],
 gr=dict(title='Recap: Setting Views Against Each Other',sections=[
  txt('How it works',"You know *viszont* and *ezzel szemben* from B1 Unit 11: they set a second statement against the first. In a history of a dispute they put the two sides next to each other without taking one: *A kormány szerint az eljárás politikai indíttatású volt, ezzel szemben az Európai Parlament szerint a jogállamiság helyzete aggályos volt.* *viszont* usually stands after the first word or phrase of its clause. New in this lesson is the vocabulary of European procedures."),
  txt('Example',"Example: *A Tanács 2022-ben felfüggesztésről döntött, a Bizottság 2023-ban viszont felszabadított egy részt.*"),
  tbl([("A kormány szerint az eljárás politikai indíttatású volt, ezzel szemben az Európai Parlament szerint a jogállamiság helyzete aggályos volt.","According to the government the procedure was politically motivated; in contrast, according to the European Parliament the state of the rule of law was a cause for concern."),
       ("Az Európai Parlament 2022-es állásfoglalása szerint Magyarország már nem volt teljes demokrácia, a kormány viszont elutasította ezt az értékelést.","According to the European Parliament's resolution of 2022, Hungary was no longer a full democracy, but the government rejected this assessment."),
       ("A Tanács 2022-ben felfüggesztésről döntött, a Bizottság 2023-ban viszont felszabadított egy részt.","In 2022 the Council decided on a suspension, but in 2023 the Commission released a part.")])]),
 vocab=[('jogállamiság','rule of law','noun'),('jogállamisági eljárás','rule-of-law procedure','expression'),('felfüggesztés','suspension','noun'),('állásfoglalás','resolution, position statement','noun'),
  ('uniós forrás','EU funds','expression'),('felszabadít','to release (funds)','verb'),('miniszterelnök','prime minister','noun'),('választás','election','noun')],
 ex=[
  mc(f'{P}-05-introduce-1','introduce','vocabulary',V,'Mit jelent az állásfoglalás szó?',
     ['Egy testület írásban megfogalmazott álláspontja.','Egy törvény hivatalos kihirdetése.','Egy bíróság végleges ítélete egy ügyben.'],0),
  fb(f'{P}-05-controlled-2','controlled','grammar','adversative-contrast','Az Európai Parlament 2022-es állásfoglalása szerint Magyarország már nem volt teljes demokrácia, a kormány _____ elutasította ezt az értékelést.',"According to the European Parliament's resolution of 2022, Hungary was no longer a full democracy, but the government rejected this assessment.",['viszont']),
  mt(f'{P}-05-controlled-3','controlled',V,[('jogállamiság','az államhatalom jogi korlátozottsága'),('felfüggesztés','ideiglenes leállítás'),('miniszterelnök','a kormány vezetője'),('uniós forrás','az Európai Unió által folyósított pénzügyi támogatás'),('választás','a képviselők megválasztása szavazással')]),
  fb(f'{P}-05-practice-4','practice','grammar','adversative-contrast','A kormány szerint az eljárás politikai indíttatású volt, ezzel _____ az Európai Parlament szerint a jogállamiság helyzete aggályos volt.','According to the government the procedure was politically motivated; in contrast, according to the European Parliament the state of the rule of law was a cause for concern.',['szemben']),
  sb(f'{P}-05-practice-5','practice','adversative-contrast','A Tanács 2022-ben felfüggesztésről döntött, a Bizottság 2023-ban viszont felszabadított egy részt.','In 2022 the Council decided on a suspension, but in 2023 the Commission released a part.'),
  dl(f'{P}-05-dialogue-6','adversative-contrast',[('Kérdező','Hogyan értékelte az eljárást a kormány, és hogyan az Európai Parlament?'),('Válaszadó','A kormány szerint politikai indíttatású volt, az Európai Parlament _____ aggályosnak ítélte a jogállamiság helyzetét.')],['viszont','mert','ezért'],0),
  sw(f'{P}-05-production-7','production','adversative-contrast','Write one sentence setting the position of the government against that of the European Parliament on the procedure begun in 2018.','A kormány szerint az eljárás politikai indíttatású volt, ezzel szemben az Európai Parlament szerint a jogállamiság helyzete aggályos volt.'),
  mc(f'{P}-05-check-8','check','grammar','adversative-contrast','Melyik mondat helyes?',
     ['A Tanács 2022-ben felfüggesztésről döntött, a Bizottság 2023-ban viszont felszabadított egy részt.','A Tanács 2022-ben felfüggesztésről döntött, a Bizottság 2023-ban ezzel felszabadított egy részt.','A Tanács 2022-ben felfüggesztésről döntött, a Bizottság 2023-ban szemben felszabadított egy részt.'],0),
 ]))
# ---------------- Consolidation
CONS=[
  mc(f'{P}-consolidation-1','recognize','grammar','evidentials','Melyik mondat nevezi meg a vélemény forrását?',
     ['A bírálók szerint a tervezetet rövid idő alatt vitatták meg.','A tervezetet rövid idő alatt vitatták meg, mert a bírálók.','A bírálók a tervezetet rövid idő alatt vitatták meg szerint.'],0),
  mc(f'{P}-consolidation-2','recognize','grammar','formal-obligation','Which sentence says that the complainant had to exhaust the legal remedies?',
     ['A panaszos köteles volt kimeríteni a jogorvoslatokat.','A panaszos kimerítette a jogorvoslatokat volt.','A panaszos kötelesen kimeríteni a jogorvoslatokat.'],0),
  mt(f'{P}-consolidation-3','recognize',V,[('Alaptörvény','Magyarország alkotmánya 2012-től'),('veszélyhelyzet','különleges jogrend válsághelyzetben'),('actio popularis','bárki által kérhető vizsgálat az Alkotmánybíróságtól'),('Kúria','Magyarország legfőbb bírósága'),('állásfoglalás','egy testület írásban kifejtett álláspontja')]),
  fb(f'{P}-consolidation-4','recall','vocabulary',V,'2020-ban a kormány a járvány miatt _____ hirdetett.','In 2020 the government declared a state of danger because of the epidemic.',['veszélyhelyzetet']),
  fb(f'{P}-consolidation-5','recall','vocabulary',V,'2012-ben a Legfelsőbb Bíróság helyébe a _____ lépett.','In 2012 the Kúria took the place of the Supreme Court.',['Kúria']),
  fb(f'{P}-consolidation-6','recall','grammar','formal-obligation','Az érintettek előbb _____ voltak kimeríteni a rendes jogorvoslatokat.','Those affected had to exhaust the ordinary remedies first.',['kötelesek','kénytelenek']),
  fb(f'{P}-consolidation-7','context','grammar','correlative-minel-annal','Az ellenzék szerint minél tovább tartott az időbeli korlát nélküli felhatalmazás, annál nagyobb volt a _____ kockázata.','According to the opposition, the longer the authorisation without a time limit lasted, the greater the risk of legal uncertainty was.',['jogbizonytalanság']),
  fb(f'{P}-consolidation-8','context','grammar','adversative-contrast','A kormány szerint az eljárás politikai indíttatású volt, az Európai Parlament _____ aggályosnak ítélte a helyzetet.','According to the government the procedure was politically motivated; the European Parliament, however, judged the situation a cause for concern.',['viszont']),
  mc(f'{P}-consolidation-9','context','grammar','epistemic-hedging','Which word marks the assessment as unlikely? \'_____ vitatható, hogy a korhatár csökkentése hatott a bírói karra.\'',
     ['Aligha','Valószínűleg','Feltehetően'],0),
  sb(f'{P}-consolidation-10','produce','adversative-contrast','A kormány szerint a módosítás összhangban volt az európai normákkal, a bírálók viszont aggályosnak tartották.','According to the government the amendment was in line with European norms, but the critics held it to be a cause for concern.'),
  sw(f'{P}-consolidation-11','production','evidentials','Write two sentences about the Fundamental Law of 2011: give the date of its adoption and the opinion of the Venice Commission, naming the source.','2011. április 18-án az Országgyűlés elfogadta az Alaptörvényt. A Velencei Bizottság 2011-es véleménye szerint a sarkalatos törvények köre aggályos volt.'),
  sw(f'{P}-consolidation-12','production',V,'Write two sentences about the elections of 2026: give the result of 12 April and the election of the prime minister on 9 May.','2026. április 12-én a Tisza Párt a 199 mandátumból 141-et szerzett. 2026. május 9-én az Országgyűlés Magyar Pétert választotta miniszterelnökké.'),
]
# fix ds on cons 9? none
L.append(dict(s='consolidation',title='Unit 25 Consolidation: The Fundamental Law and the Constitutional Court, 2010–2026',grammar_name='Review: attribution, obligation, proportion, certainty and contrast',
 goals=["I can summarise the Fundamental Law, the Constitutional Court's powers and the states of danger between 2010 and 2026, with years and sources.",
        "I can attribute, qualify and contrast views on these events.",
        "I can report the European rule-of-law procedures and the change of government in 2026 with dates."],ex=CONS))
U=dict(stem='c1-alkotmanyjog'.replace('c1-',''),id='constitutional-breakdown',unit_no=25,
 title='The Fundamental Law and the Constitutional Court, 2010–2026',
 intro=["Between 2010 and 2026 Hungary adopted a new constitution, the Fundamental Law (*Alaptörvény*, 2011), changed the powers of the Constitutional Court and declared a state of danger (*veszélyhelyzet*) several times. Each step was welcomed by some and criticised by others, in Hungary and abroad.",
        "In five short accounts you follow these events year by year, name who judged them how, and practise the forms a neutral history needs: attribution, obligation in the past, proportion, degrees of certainty and contrast. The period ends with the parliamentary election of 12 April 2026."],
 stories=[
  dict(file='c1-alkotmanyjog-01-alaptorveny-szuletese',title='Az Alaptörvény elfogadása, 2010–2012',summary='2010 és 2012 között az Országgyűlés új alaptörvényt fogadott el; a kormánypárti oldal és a bírálók eltérően ítélték meg az előkészítést, a Velencei Bizottság pedig 2011-ben véleményt adott a szövegről.',paras=[T25[0]]),
  dict(file='c1-alkotmanyjog-02-alkotmanybirosag-megnyirbalasa',title='Az Alkotmánybíróság hatásköre, 2010–2013',summary='2010 és 2013 között több módosítás változtatta meg az Alkotmánybíróság hatáskörét és eljárásait; a kormány és a bírálók eltérően értékelték ezeket.',paras=[T25[1]]),
  dict(file='c1-alkotmanyjog-03-veszelyhelyzeti-kormanyzas',title='A veszélyhelyzeti jogrend, 2020–2022',summary='2020-ban és 2022-ben a kormány veszélyhelyzetet hirdetett, és rendeletekkel szabályozott; a kormány és a bírálók eltérően ítélték meg ezt a jogrendet.',paras=[T25[2]]),
  dict(file='c1-alkotmanyjog-04-intezmenyi-foglyulejtes',title='A bírósági és közjogi tisztségek szabályai, 2011–2022',summary='2011 és 2022 között új szabályok vonatkoztak a bírákra és a közjogi tisztségek betöltésére; uniós és strasbourgi bíróságok is döntöttek ezekről.',paras=[T25[3]]),
  dict(file='c1-alkotmanyjog-05-jogallamisagi-mechanizmus',title='Az uniós jogállamisági eljárások és a 2026-os választás, 2018–2026',summary='2018 és 2023 között az Európai Unió intézményei több eljárást folytattak Magyarországgal szemben; 2026 áprilisában választást tartottak, májusban új kormány alakult.',paras=[T25[4]]),
 ],lessons=L)
U['stem']='alkotmanyjog'
if __name__=='__main__':
    write_unit(U)
