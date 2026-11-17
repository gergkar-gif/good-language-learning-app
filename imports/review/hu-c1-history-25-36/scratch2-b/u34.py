import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from lib import *
U='mta-ceu'; V='c1-mta-ceu-vocab'
TH='Higher Education and Research, 2010–2026'
S=[f'c1-tudomanyosszabadsag-0{i}' for i in range(1,6)]
STORY=[
 'stories/world/c1/c1-tudomanyosszabadsag-01-c1-tudomanyosszabadsag-01-mta-kutatohalozat-elcsatolasa.json',
 'stories/world/c1/c1-tudomanyosszabadsag-02-c1-tudomanyosszabadsag-02-lex-ceu-egyetem-eluldzese.json',
 'stories/world/c1/c1-tudomanyosszabadsag-03-c1-tudomanyosszabadsag-03-alapitvanyi-modellvaltas-kekva.json',
 'stories/world/c1/c1-tudomanyosszabadsag-04-c1-tudomanyosszabadsag-04-erasmus-kizaras-agyelszivas.json',
 'stories/world/c1/c1-tudomanyosszabadsag-05-c1-tudomanyosszabadsag-05-tudomanyos-autonomia-jovo.json']
TEXT=[
"A Magyar Tudományos Akadémiát 1825-ben Széchenyi István felajánlása nyomán alapították, és az évtizedek során kutatóintézetek egész hálózata jött létre körülötte. 2018-ban a kormány új minisztériumot hozott létre Innovációs és Technológiai Minisztérium néven, amelynek vezetője Palkovics László lett. 2019-ben a minisztérium javaslatot tett arra, hogy az Akadémia kutatóintézeteinek irányítása és finanszírozása egy új, kormányzati felügyelet alatt álló hálózathoz kerüljön. A kormány indoklása szerint a változtatás a kutatás és az innováció szorosabb összekapcsolását, valamint a hatékonyabb működést szolgálta. Az Akadémia vezetése, köztük Lovász László elnök, ezzel szemben azt állította, hogy a javaslat sérti az akadémiai autonómiát, és sok kutató aláírásgyűjtéssel tiltakozott. 2019 nyarán az Országgyűlés elfogadta a kapcsolódó törvényt, amelynek nyomán létrejött az Eötvös Loránd Kutatási Hálózat. A kutatóintézetek ettől kezdve ennek a hálózatnak a keretében működtek, az Akadémia pedig tudományos testületként maradt meg. A hálózatot 2023-ban HUN-REN névre keresztelték át.",
"A Közép-európai Egyetemet (CEU) 1991-ben alapították Budapesten, alapítója Soros György volt, és az egyetem amerikai és magyar akkreditációval is működött. 2017 márciusában a kormány módosítani javasolta a felsőoktatási törvényt, és az Országgyűlés 2017. április 4-én el is fogadta a módosítást. A szabályozás szerint az Európai Gazdasági Térségen kívülről érkező egyetem csak akkor működhetett tovább Magyarországon, feltéve, hogy a székhelye szerinti országban is folytatott képzést, és a két ország kormánya egyezményt kötött. A kormány szerint a törvény célja a külföldi egyetemek egységes szabályozása volt. A CEU vezetése és a bírálók szerint a szabályozás főként az egyetemet érintette, ezért Lex CEU néven emlegették. 2017 áprilisában az Európai Bizottság kötelezettségszegési eljárást indított Magyarország ellen. 2018 decemberében a CEU bejelentette, hogy amerikai akkreditációjú képzéseit 2019 őszétől Bécsben folytatja. Az Európai Unió Bírósága 2020. október 6-án kimondta, hogy a magyar szabályozás nem egyeztethető össze az uniós joggal.",
"2019-től a kormány több állami egyetem fenntartását közérdekű vagyonkezelő alapítványokra bízta. Ebben a modellben az állam az egyetem vagyonát és a fenntartói jogokat egy alapítványnak adta át, amelyet kuratórium irányít, és a kuratórium felel az egyetem fenntartásáért és gazdálkodásáért. További egyetemek 2020-ban és 2021-ben váltak alapítványi fenntartásúvá. A kormány szerint az új modell rugalmasabb gazdálkodást, stabilabb forrásokat és nagyobb versenyképességet biztosított az egyetemeknek. A bírálók szerint viszont a kuratóriumokban a kormányhoz közel álló személyek is helyet kaptak, és az egyetemi szenátusok szerepe csökkent. Az oktatók közül többen aggódtak az egyetemi önkormányzat jövője miatt. A legélesebb vita 2020 őszén a Színház- és Filmművészeti Egyetemen (SZFE) zajlott: a szenátus lemondott, az oktatók és a hallgatók pedig tiltakozásul elfoglalták az egyetem épületét. A kormány szerint a fenntartóváltás az egyetem működését szolgálta, a tiltakozók szerint viszont csökkentette az egyetem autonómiáját.",
"2022 szeptemberében az Európai Bizottság a jogállamisági feltételességi mechanizmus alapján pénzügyi intézkedéseket javasolt Magyarországgal szemben, és az indoklásban az összeférhetetlenség kockázatára is hivatkozott. A közérdekű vagyonkezelő alapítványok kuratóriumaiban ugyanis kormánytagok és országgyűlési képviselők is ülhettek, és ezt az uniós intézmények összeférhetetlenségi kockázatnak tekintették. A Tanács 2022 decemberében határozatot hozott, aminek következtében az ilyen alapítványokkal nem lehetett új jogi kötelezettséget vállalni az uniós programok keretében. Ez az Erasmus+ és a Horizont Európa programot is érintette, ezért 2023-tól az alapítványi fenntartású egyetemek nem köthettek új támogatási megállapodásokat. A kormány szerint az intézkedés politikai indíttatású volt, és 2023-ban hazai programot hozott létre a hallgatói mobilitás támogatására, és módosította a kuratóriumi tagságra vonatkozó szabályokat. A bírálók szerint a korlátozás növelhette a hallgatók és a kutatók külföldre távozását, vagyis az agyelszívást.",
"A 2026-os választásig tartó években a felsőoktatásról és a kutatásról szóló vita két fő érvre épült. A kormánypárti oldal szerint az alapítványi modell stabil forrást és hosszú távú tervezést adott az egyetemeknek, az Akadémia kutatóhálózatának átszervezése pedig a kutatás és a gazdaság kapcsolatát erősítette. A bírálók szerint viszont csökkent az egyetemek és az Akadémia autonómiája. A vita fő kérdése az volt, hogy a változtatások a hatékonyságot szolgálták-e, vagy az autonómiát csökkentették. Az uniós korlátozásról a kormány szerint politikai okokból született döntés, ezzel szemben az Európai Bizottság szerint az összeférhetetlenség kockázata indokolta. 2026. április 12-én a parlamenti választáson a Tisza Párt a 199 mandátumból 141-et szerzett, vagyis kétharmados többséget, Orbán Viktor pedig aznap este elismerte a vereségét. 2026. május 9-én az új Országgyűlés Magyar Pétert választotta miniszterelnökké. Ezzel a vizsgált időszak lezárult.",
]
if __name__=='__main__':
    for i,t in enumerate(TEXT): print(i+1,wc(t))

LESSONS={
1:dict(title="The Academy of Sciences and Its Research Institutes, 2018–2023",
 grammar="Recap: attributing a judgement with szerint", gtitle="Recap: Attributing a Judgement",
 storytitle="Az MTA kutatóhálózata, 2018–2023",
 goals=["I can describe how the research institutes of the Hungarian Academy of Sciences were reorganised in 2018–2023, with dates (*kutatóhálózat, autonómia, finanszírozás*).",
  "I can name the source of each view with *szerint* (*a kormány indoklása szerint*).",
  "I can state how the government and the leaders of the Academy judged the change."]),
2:dict(title="Central European University and the Higher Education Act, 2017–2020",
 grammar="Recap: conditions and exceptions with feltéve, hogy and kivéve, ha", gtitle="Recap: Conditions and Exceptions",
 storytitle="A CEU és a felsőoktatási törvény, 2017–2020",
 goals=["I can describe the higher education act of 2017 and the dispute about Central European University, with dates (*akkreditáció, egyezmény, kötelezettségszegési eljárás*).",
  "I can state a condition and an exception with *feltéve, hogy* and *kivéve, ha* (*feltéve, hogy a két ország kormánya egyezményt kötött*).",
  "I can report how the government, the university and the Court of Justice judged the law."]),
3:dict(title="University Foundations, 2019–2021",
 grammar="Recap: proportion with minél … annál", gtitle="Recap: Proportion",
 storytitle="Az alapítványi egyetemek, 2019–2021",
 goals=["I can describe how state universities came under foundations from 2019, with dates (*kuratórium, szenátus, fenntartó*).",
  "I can link two changing quantities with *minél … annál* (*minél stabilabb volt a forrás, annál rugalmasabban gazdálkodhattak az egyetemek*).",
  "I can report how the government and its critics argued about the foundation model."]),
4:dict(title="The EU Funding Dispute and Student Mobility, 2022–2025",
 grammar="Recap: cause and result with emiatt and aminek következtében", gtitle="Recap: Cause and Result",
 storytitle="Az uniós források vitája és a hallgatói mobilitás, 2022–2025",
 goals=["I can describe the dispute about EU funding for the foundation universities in 2022–2025, with dates (*összeférhetetlenség, kötelezettségvállalás, hallgatói mobilitás*).",
  "I can link a cause to its result with *emiatt* and *aminek következtében* (*a Tanács határozatot hozott, és emiatt nem lehetett új kötelezettséget vállalni*).",
  "I can report how the government and the EU institutions explained the restriction."]),
5:dict(title="Higher Education and Research on the Eve of the 2026 Election",
 grammar="Recap: contrast with viszont and ezzel szemben", gtitle="Recap: Setting Views Against Each Other",
 storytitle="Felsőoktatás és kutatás a 2026-os választás előtt",
 goals=["I can sum up the debate on higher education and research before the election of 2026 and the change of government, with dates (*választás, mandátum, miniszterelnök*).",
  "I can set two views against each other with *viszont* and *ezzel szemben* (*a kormány szerint …, a bírálók szerint viszont …*).",
  "I can report, with attribution, how each side judged the period."]),
}
CONS=dict(title="Unit 34 Consolidation: Higher Education and Research, 2010–2026",
 grammar="Review: attribution, conditions, proportion, cause and contrast",
 goals=["I can summarise the changes at the Academy of Sciences, at Central European University and in the universities between 2017 and 2026, with years and sources.",
  "I can attribute, contrast and link causes and results in a history of higher education.",
  "I can report the election of 2026 and the election of the prime minister with dates."])
INTRO=("Unit 34: "+TH,[
 "Between 2017 and 2026 the research institutes of the Hungarian Academy of Sciences and many state universities were reorganised, and Central European University moved its US-accredited programmes to Vienna after a change in the higher education law. Each step was defended by the government and criticised by others, in Hungary and abroad.",
 "In five short accounts you follow these events year by year, name who judged them how, and practise the forms a neutral history needs: attribution, conditions, proportion, cause and result, and contrast. The period ends with the parliamentary election of 12 April 2026."])

GR={
1:("grammar/c1/c1-tudomanyosszabadsag-01-a-gr.json","Recap: Attributing a Judgement",
 "You know *szerint* from B1 Unit 13 (*a hírek szerint*, *úgy tűnik*): it names who says something. A history of a disputed change needs it for every judgement: *a kormány indoklása szerint*, *az Akadémia vezetése szerint*. *szerint* stands after the noun and takes no ending, and the verb stays in the past: *A kormány szerint a változtatás a hatékonyabb működést szolgálta.* New in this lesson is the vocabulary of research funding.",
 "Az Akadémia vezetése szerint a javaslat sértette az autonómiát.",
 [("A kormány indoklása szerint a változtatás a hatékonyabb működést szolgálta.","According to the government's reasoning, the change served more efficient operation."),
  ("Az Akadémia vezetése szerint a javaslat sértette az akadémiai autonómiát.","According to the Academy's leadership, the proposal violated academic autonomy."),
  ("Sok kutató aláírásgyűjtéssel tiltakozott, a kormány szerint viszont a kutatás hatékonyabb lett.","Many researchers protested with a petition, but according to the government research became more efficient.")]),
2:("grammar/c1/c1-tudomanyosszabadsag-02-a-gr.json","Recap: Conditions and Exceptions",
 "You know *feltéve, hogy* ('provided that') and *kivéve, ha* ('except if') from C1 Unit 7: the first sets a condition, the second an exception. In a history of a law they say what the rule required at the time, so the verb stays in the past: *A külföldi egyetem tovább működhetett, feltéve, hogy a két ország kormánya egyezményt kötött.* New in this lesson is the vocabulary of higher education law.",
 "A szabályozás a külföldi egyetemekre vonatkozott, kivéve, ha azok az Európai Gazdasági Térségből érkeztek.",
 [("A külföldi egyetem tovább működhetett, feltéve, hogy a két ország kormánya egyezményt kötött.","The foreign university could go on operating, provided that the governments of the two countries concluded an agreement."),
  ("A szabályozás a külföldi egyetemekre vonatkozott, kivéve, ha azok az Európai Gazdasági Térségből érkeztek.","The regulation applied to foreign universities, except if they came from the European Economic Area."),
  ("A kormány szerint a módosítás egyenlő feltételeket teremtett, feltéve, hogy minden külföldi egyetem teljesíti őket.","According to the government, the amendment created equal conditions, provided that every foreign university meets them.")]),
3:("grammar/c1/c1-tudomanyosszabadsag-03-a-gr.json","Recap: Proportion",
 "You know *minél … annál* from B1 Unit 2 (*minél többet olvasok, annál többet értek*): two comparatives change together. In a history the comparison usually belongs to somebody's argument, so the source comes first and the verbs are in the past: *A kormány szerint minél stabilabb volt a forrás, annál rugalmasabban gazdálkodhattak az egyetemek.* Both parts take the comparative in *-bb*. New in this lesson is the vocabulary of university foundations.",
 "A bírálók szerint minél nagyobb lett a kuratórium szerepe, annál kisebb lett a szenátusé.",
 [("A kormány szerint minél stabilabb volt a forrás, annál rugalmasabban gazdálkodhattak az egyetemek.","According to the government, the more stable the funding was, the more flexibly the universities could manage."),
  ("A bírálók szerint minél nagyobb lett a kuratórium szerepe, annál kisebb lett a szenátusé.","According to the critics, the greater the role of the board became, the smaller that of the senate became."),
  ("A kormány szerint minél több forrást kaptak az egyetemek, annál hosszabb távon tervezhettek.","According to the government, the more funding the universities received, the longer ahead they could plan.")]),
4:("grammar/c1/c1-tudomanyosszabadsag-04-a-gr.json","Recap: Cause and Result",
 "You know *emiatt* from B1 Unit 16 (*Kevés az eső, és emiatt kevés a víz a tóban*) and the formal *aminek következtében*: both link a whole clause to its result. In a history they connect two dated events without a judgement: *A Tanács 2022 decemberében határozatot hozott, és emiatt az alapítványokkal nem lehetett új kötelezettséget vállalni.* *emiatt* begins the second clause; *aminek következtében* follows a comma. New in this lesson is the vocabulary of EU funding.",
 "A Tanács határozatot hozott, aminek következtében az alapítványi egyetemek nem köthettek új megállapodást.",
 [("A Tanács 2022 decemberében határozatot hozott, és emiatt az alapítványokkal nem lehetett új kötelezettséget vállalni.","In December 2022 the Council took a decision, and because of this no new commitment could be made with the foundations."),
  ("A Tanács határozatot hozott, aminek következtében az alapítványi egyetemek nem köthettek új megállapodást.","The Council took a decision, as a result of which the foundation universities could not conclude new agreements."),
  ("A Bizottság összeférhetetlenségi kockázatot jelzett, és emiatt a Tanács intézkedést fogadott el.","The Commission pointed to a risk of conflict of interest, and because of this the Council adopted a measure.")]),
5:("grammar/c1/c1-tudomanyosszabadsag-05-a-gr.json","Recap: Setting Views Against Each Other",
 "You know *viszont* and *ezzel szemben* from B1 Unit 11: they set a second statement against the first. In a history of a dispute they put the two sides next to each other without taking one: *A kormány szerint az uniós korlátozás politikai okokból született, ezzel szemben az Európai Bizottság szerint az összeférhetetlenség kockázata indokolta.* *viszont* usually stands after the first word or phrase of its clause. New in this lesson is the vocabulary of the 2026 election.",
 "A kormány szerint stabil volt a forrás, a bírálók szerint viszont csökkent az autonómia.",
 [("A kormány szerint az uniós korlátozás politikai okokból született, ezzel szemben az Európai Bizottság szerint az összeférhetetlenség kockázata indokolta.","According to the government the EU restriction had political reasons; in contrast, according to the European Commission the risk of conflict of interest justified it."),
  ("A kormánypárti oldal szerint az alapítványi modell stabil forrást adott, a bírálók viszont az autonómia csökkenését emelték ki.","According to the pro-government side the foundation model gave stable funding, but the critics stressed the decline of autonomy."),
  ("Az Akadémia vezetői szerint sérült az autonómia, a kormány szerint viszont erősödött a kutatás és a gazdaság kapcsolata.","According to the Academy's leaders autonomy was damaged, but according to the government the link between research and the economy grew stronger.")]),
}

VOC={
1:("The Academy of Sciences and Its Research Institutes, 2018–2023",[
 ("Magyar Tudományos Akadémia","Hungarian Academy of Sciences","noun"),
 ("kutatóintézet","research institute","noun"),
 ("kutatóhálózat","research network","noun"),
 ("autonómia","autonomy","noun"),
 ("minisztérium","ministry","noun"),
 ("finanszírozás","funding","noun"),
 ("aláírásgyűjtés","petition, collecting signatures","noun"),
 ("indoklás","reasoning, stated grounds","noun"),
 ("átszervezés","reorganisation","noun")]),
2:("Central European University and the Higher Education Act, 2017–2020",[
 ("külföldi egyetem","foreign university","expression"),
 ("felsőoktatási törvény","higher education act","expression"),
 ("akkreditáció","accreditation","noun"),
 ("egyezmény","international agreement, convention","noun"),
 ("székhely","seat, registered headquarters","noun"),
 ("képzés","course of study, programme","noun"),
 ("kötelezettségszegési eljárás","infringement procedure","expression"),
 ("ítélet","judgment, ruling","noun")]),
3:("University Foundations, 2019–2021",[
 ("közérdekű vagyonkezelő alapítvány","public-interest trust foundation","expression"),
 ("kuratórium","board of trustees","noun"),
 ("szenátus","university senate","noun"),
 ("fenntartó","maintainer, body that runs an institution","noun"),
 ("vagyon","property, assets","noun"),
 ("versenyképesség","competitiveness","noun"),
 ("oktató","university teacher, lecturer","noun"),
 ("hallgató","university student","noun"),
 ("gazdálkodik","to manage resources, to run an economy","verb")]),
4:("The EU Funding Dispute and Student Mobility, 2022–2025",[
 ("Erasmus+","Erasmus+ (EU programme for student and staff exchange)","noun"),
 ("Horizont Európa","Horizon Europe (EU research funding programme)","noun"),
 ("jogállamisági feltételességi mechanizmus","rule-of-law conditionality mechanism","expression"),
 ("összeférhetetlenség","conflict of interest","noun"),
 ("kötelezettségvállalás","legal commitment","noun"),
 ("hallgatói mobilitás","student mobility","expression"),
 ("agyelszívás","brain drain","noun"),
 ("határozat","decision, resolution","noun")]),
5:("Higher Education and Research on the Eve of the 2026 Election",[
 ("választás","election","noun"),
 ("Országgyűlés","National Assembly (the Hungarian parliament)","noun"),
 ("mandátum","seat in parliament","noun"),
 ("kétharmados többség","two-thirds majority","expression"),
 ("miniszterelnök","prime minister","noun"),
 ("kormánypárti","pro-government","adjective"),
 ("bíráló","critic","noun")]),
}

def chk(id,opts,teaches,ds=None,q="Melyik mondat helyes?"):
    return mc(id,"check","grammar",q,opts,teaches,ds)
def EXS(n):
    s=S[n-1]; i=lambda stage,k:f"{s}-{stage}-{k}"
    if n==1: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent a kutatóhálózat szó?",["Egymással összekapcsolt kutatóintézetek rendszere.","Egy egyetem hallgatóinak közös szervezete.","Egy minisztérium belső szabályzata."],V),
 fb(i('controlled',2),'controlled','grammar',"A kormány _____ a változtatás a kutatás és az innováció szorosabb összekapcsolását szolgálta.","According to the government, the change served a closer link between research and innovation.",'evidentials',ans='szerint'),
 match(i('controlled',3),'controlled',[["autonómia","egy intézmény joga a saját ügyeit maga intézni"],["finanszírozás","egy működés költségeinek fedezése"],["indoklás","az érvek, amelyekkel valaki egy döntést magyaráz"],["aláírásgyűjtés","tiltakozás vagy kérés aláírásokkal"]],V),
 fb(i('practice',4),'practice','grammar',"Az Akadémia vezetése _____ a javaslat sértette az akadémiai autonómiát.","According to the Academy's leadership, the proposal violated academic autonomy.",'evidentials',ans='szerint'),
 sb(i('practice',5),'practice',"A kormány indoklása szerint a változtatás a hatékonyabb működést szolgálta.","According to the government's reasoning, the change served more efficient operation.",'evidentials'),
 dlg(i('dialogue',6),[("Kérdező","Hogyan indokolta a kormány 2019-ben a Magyar Tudományos Akadémia kutatóintézeteinek átszervezését?"),("Válaszadó","A kormány indoklása _____ a változtatás a kutatás és az innováció kapcsolatát szolgálta.")],["szerint","helyett","óta"],'evidentials'),
 wr(i('production',7),'production',"Write two sentences: say what the government said about the change of 2019 and what the Academy's leaders said, naming the source of each view.","A kormány indoklása szerint a változtatás a hatékonyabb működést szolgálta. Az Akadémia vezetése szerint viszont a javaslat sértette az akadémiai autonómiát.",'evidentials'),
 chk(i('check',8),["A kormány szerint a változtatás a hatékonyabb működést szolgálta.","A kormány szerinte a változtatás a hatékonyabb működést szolgálta.","A szerint kormány a változtatás a hatékonyabb működést szolgálta."],'evidentials',{"1":"inflected-postpositions"}),
 ]
    if n==2: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent az akkreditáció szó?",["Egy képzés hivatalos elismerése egy hatóság részéről.","Egy egyetem hallgatóinak felvételi vizsgája.","Egy tanár külföldi kirándulása."],V),
 fb(i('controlled',2),'controlled','grammar',"A külföldi egyetem tovább működhetett, _____, hogy a két ország kormánya egyezményt kötött.","The foreign university could go on operating, provided that the governments of the two countries concluded an agreement.",'felteve-hogy-kiveve-ha',ans='feltéve'),
 match(i('controlled',3),'controlled',[["akkreditáció","egy képzés hivatalos elismerése"],["egyezmény","két állam írásos megállapodása"],["székhely","az a hely, ahol egy intézmény hivatalosan működik"],["kötelezettségszegési eljárás","az Európai Bizottság eljárása egy tagállam ellen"],["ítélet","egy bíróság döntése egy ügyben"]],V),
 fb(i('practice',4),'practice','grammar',"A szabály a külföldi egyetemekre vonatkozott, _____, ha azok az Európai Gazdasági Térségből érkeztek.","The rule applied to foreign universities, except if they came from the European Economic Area.",'felteve-hogy-kiveve-ha',ans='kivéve'),
 sb(i('practice',5),'practice',"A törvény szerint a külföldi egyetem tovább működhetett, feltéve, hogy egyezmény született.","According to the law, the foreign university could go on operating, provided that an agreement was made.",'felteve-hogy-kiveve-ha'),
 dlg(i('dialogue',6),[("Kérdező","Milyen feltétel mellett működhetett tovább a külföldi egyetem a felsőoktatási törvény 2017-es módosítása szerint?"),("Válaszadó","Tovább működhetett, _____, hogy a két ország kormánya egyezményt kötött.")],["feltéve","kivéve","mintha"],'felteve-hogy-kiveve-ha'),
 wr(i('production',7),'production',"Write two sentences: say what condition the law of 2017 set for the foreign university and what the government said the law was for.","A külföldi egyetem tovább működhetett, feltéve, hogy a két ország kormánya egyezményt kötött. A kormány szerint a törvény célja a külföldi egyetemek egységes szabályozása volt.",'felteve-hogy-kiveve-ha'),
 chk(i('check',8),["A külföldi egyetem tovább működhetett, feltéve, hogy egyezmény született.","A külföldi egyetem tovább működhetett, kivéve, hogy feltéve egyezmény született.","A külföldi egyetem tovább működhetett, hogy feltéve egyezmény született."],'felteve-hogy-kiveve-ha',None,"Melyik mondat helyes?"),
 ]
    if n==3: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent a kuratórium szó?",["Egy alapítvány vagy intézmény vezető testülete.","Egy egyetem hallgatóinak képviselete.","Egy minisztérium jogi osztálya."],V),
 fb(i('controlled',2),'controlled','grammar',"A kormány szerint minél több forrást kapott az egyetem, _____ nagyobb önállósággal működhetett.","According to the government, the more funding the university received, the more independently it could operate.",'correlative-minel-annal',ans='annál'),
 match(i('controlled',3),'controlled',[["kuratórium","egy alapítvány vezető testülete"],["szenátus","az egyetem választott vezető testülete"],["fenntartó","aki egy intézmény működtetéséért felel"],["versenyképesség","az a képesség, hogy valaki helytáll másokkal szemben"],["oktató","aki egy egyetemen tanít"]],V),
 fb(i('practice',4),'practice','grammar',"A kormány szerint _____ stabilabb volt a finanszírozás, annál hosszabb távon tervezhettek az egyetemek.","According to the government, the more stable the funding was, the longer ahead the universities could plan.",'correlative-minel-annal',ans='minél'),
 sb(i('practice',5),'practice',"A bírálók szerint minél nagyobb lett a kuratórium szerepe, annál kisebb lett a szenátusé.","According to the critics, the greater the role of the board became, the smaller that of the senate became.",'correlative-minel-annal'),
 dlg(i('dialogue',6),[("Kérdező","Mit állított a kormány a közérdekű vagyonkezelő alapítványról?"),("Válaszadó","A kormány szerint minél stabilabb volt a forrás, _____ rugalmasabban gazdálkodhattak az egyetemek.")],["annál","mint","hogy"],'correlative-minel-annal'),
 wr(i('production',7),'production',"Write one sentence with minél … annál: give the critics' view of the role of the board and of the senate.","A bírálók szerint minél nagyobb lett a kuratórium szerepe, annál kisebb lett a szenátusé.",'correlative-minel-annal'),
 chk(i('check',8),["A kormány szerint minél stabilabb volt a finanszírozás, annál rugalmasabban gazdálkodhattak az egyetemek.","A kormány szerint minél stabilabb volt a finanszírozás, minél rugalmasabban gazdálkodhattak az egyetemek.","A kormány szerint annál stabilabb volt a finanszírozás, minél rugalmasabban gazdálkodhattak az egyetemek."],'correlative-minel-annal'),
 ]
    if n==4: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent az összeférhetetlenség szó?",["Magánérdek és közfeladat ellentéte.","Két ország közötti határvita.","Egy diák és egy tanár vitája."],V),
 fb(i('controlled',2),'controlled','grammar',"A Tanács 2022 decemberében határozatot hozott, és _____ az alapítványokkal nem lehetett új kötelezettségvállalást tenni.","In December 2022 the Council took a decision, and because of this no new legal commitment could be made with the foundations.",'causal-postpositions',ans='emiatt'),
 match(i('controlled',3),'controlled',[["Erasmus+","az Európai Unió hallgatói és oktatói csereprogramja"],["Horizont Európa","az Európai Unió kutatási támogatási programja"],["hallgatói mobilitás","a hallgatók külföldi tanulmányi útja"],["agyelszívás","a tehetséges szakemberek külföldre távozása"]],V),
 fb(i('practice',4),'practice','grammar',"A Tanács határozatot hozott, aminek _____ az alapítványi egyetemek nem köthettek új támogatási megállapodást.","The Council took a decision, as a result of which the foundation universities could not conclude new grant agreements.",'causal-postpositions',ans='következtében'),
 sb(i('practice',5),'practice',"A Tanács határozatot hozott, és emiatt az alapítványi egyetemek nem köthettek új megállapodást.","The Council took a decision, and because of this the foundation universities could not conclude new agreements.",'causal-postpositions'),
 dlg(i('dialogue',6),[("Kérdező","Miért nem köthettek az alapítványi egyetemek 2023-tól új támogatási megállapodásokat a jogállamisági feltételességi mechanizmus keretében?"),("Válaszadó","A Tanács határozatot hozott, _____ nem lehetett új kötelezettséget vállalni.")],["emiatt","viszont","ugyanis"],'causal-postpositions'),
 wr(i('production',7),'production',"Write one sentence with emiatt: say what followed from the Council's decision of December 2022.","A Tanács 2022 decemberében határozatot hozott, és emiatt az alapítványi egyetemek nem köthettek új támogatási megállapodásokat.",'causal-postpositions'),
 chk(i('check',8),["A Tanács határozatot hozott, aminek következtében az egyetemek nem köthettek új megállapodást.","A Tanács határozatot hozott, aminek következtében miatt az egyetemek nem köthettek új megállapodást.","A Tanács határozatot hozott, aminek következtére az egyetemek nem köthettek új megállapodást."],'causal-postpositions'),
 ]
    if n==5: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent a mandátum szó?",["Egy képviselői hely a parlamentben.","Egy minisztérium hivatalos levele.","Egy egyetem tanulmányi szabályzata."],V),
 fb(i('controlled',2),'controlled','grammar',"A kormánypárti oldal szerint az alapítványi modell stabil forrást adott, a bírálók _____ az autonómia csökkenését emelték ki.","According to the pro-government side the foundation model gave stable funding; the critics, however, stressed the decline of autonomy.",'adversative-contrast',ans='viszont'),
 match(i('controlled',3),'controlled',[["választás","az állampolgárok szavazása képviselőkről"],["mandátum","egy képviselői hely a parlamentben"],["kétharmados többség","a mandátumok kétharmadánál több"],["miniszterelnök","a kormány vezetője"],["Országgyűlés","a magyar parlament"]],V),
 fb(i('practice',4),'practice','grammar',"A kormány szerint az uniós korlátozás politikai okokból született, ezzel _____ az Európai Bizottság szerint az összeférhetetlenség kockázata indokolta.","According to the government the EU restriction had political reasons; in contrast, according to the European Commission the risk of conflict of interest justified it.",'adversative-contrast',ans='szemben'),
 sb(i('practice',5),'practice',"Az Akadémia vezetői szerint sérült az autonómia, a kormány szerint viszont erősödött a kutatás és a gazdaság kapcsolata.","According to the Academy's leaders autonomy was damaged, but according to the government the link between research and the economy grew stronger.",'adversative-contrast'),
 dlg(i('dialogue',6),[("Kérdező","Hogyan vélekedett az Akadémia vezetése és a kormány az új kutatóhálózatról?"),("Válaszadó","Az Akadémia vezetői szerint sérült az autonómia, a kormány szerint _____ erősödött a kutatás és a gazdaság kapcsolata.")],["viszont","ugyanis","tehát"],'adversative-contrast'),
 wr(i('production',7),'production',"Write one sentence that sets the government's view of the foundation model against the critics' view, with viszont.","A kormány szerint az alapítványi modell stabil forrást adott, a bírálók szerint viszont csökkent az egyetemek autonómiája.",'adversative-contrast'),
 chk(i('check',8),["A kormány szerint stabil volt a forrás, a bírálók viszont az autonómia csökkenését említették.","A kormány szerint stabil volt a forrás, a bírálók az viszont autonómia csökkenését említették.","A kormány szerint stabil volt a forrás, a bírálók viszont az autonómia csökkenését említette."],'adversative-contrast'),
 ]

def CEX():
    s='c1-tudomanyosszabadsag-consolidation'; i=lambda k:f"{s}-{k}"
    return [
 mc(i(1),'recognize','grammar',"Melyik mondat nevezi meg a vélemény forrását?",["A kormány szerint a változtatás a hatékonyabb működést szolgálta.","A változtatás a hatékonyabb működést szolgálta, mert a kormány.","A kormány a változtatás a hatékonyabb működést szolgálta szerint."],'evidentials'),
 mc(i(2),'recognize','grammar',"Which sentence says that the university could go on operating provided that an agreement was made?",["A külföldi egyetem tovább működhetett, feltéve, hogy egyezmény született.","A külföldi egyetem tovább működhetett, feltéve, hogy egyezmény születtek.","A külföldi egyetem tovább működhetett, kivéve, hogy egyezmény született."],'felteve-hogy-kiveve-ha'),
 match(i(3),'recognize',[["kuratórium","egy alapítvány vezető testülete"],["akkreditáció","egy képzés hivatalos elismerése"],["kötelezettségszegési eljárás","az Európai Bizottság eljárása egy tagállam ellen"],["Horizont Európa","az Európai Unió kutatási támogatási programja"],["Magyar Tudományos Akadémia","a magyar tudósok testülete 1825-től"]],V),
 fb(i(4),'recall','vocabulary',"2017 áprilisában az Európai Bizottság _____ eljárást indított Magyarország ellen.","In April 2017 the European Commission started infringement proceedings against Hungary.",V,ans='kötelezettségszegési',hint='infringement'),
 fb(i(5),'recall','vocabulary',"Az alapítványi egyetemek vezető testülete a _____.","The governing body of the foundation universities is the board of trustees.",V,ans='kuratórium'),
 fb(i(6),'recall','grammar',"A szabály a külföldi egyetemekre vonatkozott, _____, ha azok az Európai Gazdasági Térségből érkeztek.".replace("a külföldi egyetemekre vonatkozott","minden külföldi egyetemre vonatkozott"),"The rule applied to every foreign university, except if they came from the European Economic Area.",'felteve-hogy-kiveve-ha',ans='kivéve'),
 fb(i(7),'context','grammar',"A bírálók szerint minél nagyobb volt a kuratórium szerepe, annál kisebb volt a _____ szerepe.","According to the critics, the greater the role of the board was, the smaller the role of the senate was.",'correlative-minel-annal',ans='szenátus'),
 fb(i(8),'context','grammar',"A Bizottság összeférhetetlenségi aggályt jelzett, aminek _____ a Tanács határozatot hozott.","The Commission pointed to a conflict-of-interest concern, as a result of which the Council took a decision.",'causal-postpositions',ans='következtében'),
 mc(i(9),'context','grammar',"Which word fills the gap? 'A kormány szerint a modell stabil forrást adott, a bírálók _____ az autonómia csökkenését említették.'",["viszont","ugyanis","tehát"],'adversative-contrast'),
 sb(i(10),'produce',"A kormány szerint a törvény egységes szabályozást hozott, a CEU vezetése szerint viszont főként az egyetemet érintette.","According to the government the law brought uniform regulation, but according to the CEU leadership it mainly concerned the university.",'adversative-contrast'),
 wr(i(11),'production',"Write two sentences about the Lex CEU: give the date of the adoption of the amendment and the judgment of the Court of Justice of 2020.","2017. április 4-én az Országgyűlés elfogadta a felsőoktatási törvény módosítását. Az Európai Unió Bírósága 2020. október 6-án kimondta, hogy a magyar szabályozás nem egyeztethető össze az uniós joggal.",V),
 wr(i(12),'production',"Write two sentences about the elections of 2026: give the result of 12 April and the election of the prime minister on 9 May.","2026. április 12-én a Tisza Párt a 199 mandátumból 141-et szerzett. 2026. május 9-én az Országgyűlés Magyar Pétert választotta miniszterelnökké.",V),
 ]

def run():
    for n in range(1,6):
        stem=S[n-1]; sp=LESSONS[n]
        if n==1: sp=dict(sp,intro=INTRO)
        apply_lesson(sp,stem,n,34)
        g=GR[n]; gram(g[0].replace('grammar/',''),g[1],g[2],g[3],g[4]) if False else None
        gp=g[0]; gram(gp,g[1],g[2],g[3],g[4])
        apply_vocab(stem,VOC[n][0],TH,VOC[n][1])
        apply_ex(stem,EXS(n))
        apply_story(STORY[n-1],sp['storytitle'],V,[TH,sp['title']],SUMMARY[n-1],[TEXT[n-1]])
    apply_lesson(dict(CONS,),'c1-tudomanyosszabadsag-consolidation',6,34)
    apply_ex('c1-tudomanyosszabadsag-consolidation',CEX())
SUMMARY=[
"2018 és 2023 között az Akadémia kutatóintézetei új hálózathoz kerültek; a kormány indoklása és az Akadémia vezetésének álláspontja eltért egymástól.",
"2017-ben az Országgyűlés módosította a felsőoktatási törvényt; a CEU 2019-től amerikai akkreditációjú képzéseit Bécsben folytatta, az Európai Unió Bírósága pedig 2020-ban ítéletet hozott.",
"2019-től több állami egyetem fenntartása közérdekű vagyonkezelő alapítványokhoz került; a kormány és a bírálók eltérően ítélték meg a modellt.",
"2022 végén az uniós Tanács határozata nyomán az alapítványi egyetemek nem köthettek új támogatási megállapodásokat az Erasmus+ és a Horizont Európa programban.",
"A 2026-os választás előtt a kormánypárti oldal és a bírálók eltérően értékelték a felsőoktatás és a kutatás átalakítását; 2026 áprilisában a Tisza Párt kétharmados többséget szerzett."]
if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]=='run':
    run()
