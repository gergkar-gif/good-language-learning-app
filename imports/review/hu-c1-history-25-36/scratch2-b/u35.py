import sys; sys.path.insert(0,'/home/user/parlour-read-b/.scratch')
from gen import *
P='c1-megfigyeles'; V='c1-pegasus-scandal-vocab'
TH='Covert Surveillance and the Pegasus Case, 2021–2026'
S=[f'{P}-0{i}' for i in range(1,6)]
STORY=[
 'stories/world/c1/c1-megfigyeles-01-c1-megfigyeles-01-pegasus-botrany-ujsagirok.json',
 'stories/world/c1/c1-megfigyeles-02-c1-megfigyeles-02-igazsagugyi-pecset-varga-judit.json',
 'stories/world/c1/c1-megfigyeles-03-c1-megfigyeles-03-titkosszolgalati-felelemkeltes.json',
 'stories/world/c1/c1-megfigyeles-04-c1-megfigyeles-04-nemzetbiztonsagi-bizottsag-eltitkolas.json',
 'stories/world/c1/c1-megfigyeles-05-c1-megfigyeles-05-digitalis-jogallam-vedelme.json']
TEXT=[
"2021 júliusában a Pegasus Project nevű nemzetközi újságírói együttműködés, amelyben több szerkesztőség és az Amnesty International biztonsági laboratóriuma is részt vett, azt közölte, hogy az izraeli NSO Group Pegasus nevű kémszoftverét több országban használták telefonok megfigyelésére. Magyarországon a Direkt36 tényfeltáró újságírói központ számolt be arról, hogy a lehetséges célpontok listáján újságírók, ügyvédek és üzletemberek telefonszámai is szerepeltek. Az Amnesty műszaki vizsgálata szerint két magyar újságíró, Panyi Szabolcs és Szabó András telefonján találtak a kémszoftverre utaló nyomokat. Az NSO Group azt közölte, hogy a programot csak állami szerveknek adja el, bűnözés és terrorizmus elleni fellépésre. A magyar kormány azt mondta, hogy a titkosszolgálatok a törvényi keretek között működtek. 2022 elején a parlament Nemzetbiztonsági Bizottságának elnöke, Kósa Lajos azt közölte, hogy egy magyar szolgálat valóban megvásárolta a Pegasust, és a törvények szerint használta.",
"A magyar szabályozás szerint a nemzetbiztonsági szolgálatok titkos információgyűjtését az igazságügyi miniszter engedélyezte, bírói engedély nem kellett hozzá. A szolgálatok kötelesek voltak a miniszterhez fordulni, ha egy magánszemély telefonját vagy levelezését titokban meg akarták figyelni. Az Emberi Jogok Európai Bírósága a Szabó és Vissy kontra Magyarország ügyben 2016. január 12-én hozott ítéletében megállapította, hogy a terrorizmus elleni megfigyelésre vonatkozó magyar szabályozás nem nyújtott elegendő garanciát a visszaélések ellen, ezért sértette a magánélet tiszteletben tartásához való jogot. A kormány szerint a rendszer a törvényekkel összhangban működött, és a szolgálatokat a parlament Nemzetbiztonsági Bizottsága is ellenőrizte. A Társaság a Szabadságjogokért nevű jogvédő szervezet szerint viszont független külső ellenőrzés, vagyis előzetes bírói engedélyezés nélkül nem volt kellően védett a magánszféra. 2019 és 2023 között az igazságügyi miniszter Varga Judit volt. A 2021-es Pegasus-ügy után az engedélyezés módja a vita egyik központi kérdése lett.",
"Az Emberi Jogok Európai Bírósága már 1996-ban, a Goodwin kontra Egyesült Királyság ügyben a sajtószabadság egyik alapfeltételének nevezte az újságírói források védelmét. A forrásvédelem azt jelenti, hogy az újságíró nem köteles elárulni, ki adott neki információt, és a magyar jog is ismeri ezt a szabályt. A Pegasus-ügy 2021-es nyilvánosságra kerülése után a sajtószabadsággal foglalkozó szervezetek és az érintett újságírók azt mondták, hogy a megfigyelés feltehetőleg elriaszthatta a forrásokat attól, hogy újságírókkal beszéljenek. A jogtudomány az ilyen hatást angol szóval chilling effectnek, magyarul hűtő vagy dermesztő hatásnak nevezi. A kormány azt mondta, hogy a megfigyelések törvényesek voltak, és nemzetbiztonsági célt szolgáltak. A bírálók szerint a titkos megfigyelés különösen akkor veszélyes a sajtószabadságra, ha nincs mögötte független ellenőrzés. A két oldal tehát eltérően értékelte, hogy a megfigyelés hogyan hatott az újságírók és a források kapcsolatára.",
"2021 őszén az ellenzéki képviselők a parlament Nemzetbiztonsági Bizottságának összehívását kezdeményezték a Pegasus-ügy kivizsgálására. A kormánypárti képviselők az első ülésen nem jelentek meg, ezért a bizottság nem volt határozatképes. 2022 januárjában a bizottság végül meghallgatta a titkosszolgálatok vezetőit, az ülés anyagát pedig 2070-ig minősítették titkossá. A kormánypárti oldal szerint a minősítés a nemzetbiztonsági érdeket védte, az ellenzék szerint viszont akadályozta az ellenőrzést. Annak ellenére, hogy a kormánypárti oldal és az adatvédelmi hatóság szerint a megfigyelések törvényesek voltak, az Európai Parlament 2022 márciusában vizsgálóbizottságot hozott létre a Pegasus és a hasonló kémszoftverek használatának kivizsgálására. A PEGA nevű bizottság ajánlásait az Európai Parlament 2023 júniusában fogadta el, és a jelentés szerint Magyarországon a kémszoftver használata a sajtószabadságot is veszélyeztette. A magyar kormány azt mondta, hogy a titkosszolgálatok jogszerűen jártak el.",
"A 2026-os választásig tartó években a titkos megfigyelés szabályozásáról két álláspont állt szemben. A jogvédő szervezetek és az ellenzéki oldal szerint a titkos megfigyelést minden esetben független bírói engedélyhez kellene kötni, a kormány szerint viszont a hatályos szabályozás elegendő garanciát tartalmazott. A vita szereplői ugyanarra a kérdésre kerestek választ: a nemzetbiztonsági érdek mellett milyen ellenőrzés szükséges a magánszféra védelméhez. Mindkét oldal a magánszféra védelmére és a nemzet biztonságára hivatkozott. Az Európai Unióban 2024-ben elfogadták az európai médiaszabadsági rendeletet, amely korlátozza, hogy a tagállamok milyen feltételekkel használhatnak kémszoftvert újságírók ellen. 2026. április 12-én a parlamenti választáson a Tisza Párt a 199 mandátumból 141-et szerzett, vagyis kétharmados többséget, Orbán Viktor pedig aznap este elismerte a vereségét. 2026. május 9-én az új Országgyűlés Magyar Pétert választotta miniszterelnökké. Ezzel a vizsgált időszak lezárult.",
]
SUMMARY=[
"2021 nyarán nemzetközi újságírói együttműködés számolt be a Pegasus kémszoftver használatáról; a magyar kormány szerint a titkosszolgálatok a törvényi keretek között működtek.",
"A magyar szabályozás szerint a titkos megfigyelést az igazságügyi miniszter engedélyezte; az Emberi Jogok Európai Bírósága 2016-ban a szabályozás garanciáit hiányosnak találta, a kormány szerint viszont a rendszer összhangban volt a törvényekkel.",
"A Pegasus-ügy után az újságírók és a sajtószabadsággal foglalkozó szervezetek szerint a megfigyelés elriaszthatta a forrásokat; a kormány szerint a megfigyelések törvényesek voltak.",
"2021 és 2023 között a parlament Nemzetbiztonsági Bizottságában és az Európai Parlamentben is vizsgálták az ügyet; a kormány szerint a titkosszolgálatok jogszerűen jártak el.",
"A 2026-os választás előtt a jogvédő szervezetek bírói engedélyezést javasoltak, a kormány szerint a szabályozás elegendő garanciát tartalmazott; 2026 áprilisában a Tisza Párt kétharmados többséget szerzett."]
LESSONS={
1:dict(title="The Pegasus Reports of 2021",grammar="Recap: reporting what someone stated with azt mondta, hogy",gtitle="Recap: Reporting What Someone Stated",
 storytitle="A Pegasus-jelentések, 2021",
 goals=["I can describe how the Pegasus reports of 2021 came out and what the Hungarian government said about them, with dates (*kémszoftver, titkosszolgálat, megfigyelés*).",
  "I can report what each side stated with *azt mondta, hogy* and *azt közölte, hogy* (*az NSO Group azt közölte, hogy …*).",
  "I can keep a company's, an investigator's and a government's claims apart from my own voice."]),
2:dict(title="Authorising Covert Surveillance, 2016–2021",grammar="Recap: obligation in the past with köteles volt and kénytelen volt",gtitle="Recap: Obligation in the Past",
 storytitle="A titkos megfigyelés engedélyezése, 2016–2021",
 goals=["I can describe how covert surveillance was authorised and what the European Court of Human Rights found in 2016, with dates (*engedélyezés, garancia, magánélet*).",
  "I can say what a rule required in the past with *köteles volt* and *kénytelen volt* (*a szolgálatok kötelesek voltak engedélyt kérni*).",
  "I can report how the government and a human rights organisation judged the system."]),
3:dict(title="Journalists and Source Protection, 2021–2023",grammar="Recap: degrees of certainty with feltehetőleg, valószínűleg and aligha",gtitle="Recap: Degrees of Certainty",
 storytitle="Újságírók és forrásvédelem, 2021–2023",
 goals=["I can describe what source protection means and how journalists and the government judged the effect of the surveillance, with dates (*forrásvédelem, sajtószabadság, dermesztő hatás*).",
  "I can mark how certain a claim is with *feltehetőleg*, *valószínűleg* and *aligha* (*feltehetőleg elriasztotta a forrásokat*).",
  "I can report who said what about the effect on sources."]),
4:dict(title="The National Security Committee and the European Parliament, 2021–2023",grammar="Recap: concession with annak ellenére, hogy",gtitle="Recap: Concession",
 storytitle="A Nemzetbiztonsági Bizottság és az Európai Parlament, 2021–2023",
 goals=["I can describe how the Pegasus case was examined in the Hungarian parliament and in the European Parliament, with dates (*Nemzetbiztonsági Bizottság, határozatképes, vizsgálóbizottság*).",
  "I can set a fact against its opposite with *annak ellenére, hogy* (*annak ellenére, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt határozatképes*).",
  "I can report how the governing side and the opposition judged the classification of the hearing."]),
5:dict(title="Surveillance Law and the 2026 Election",grammar="Recap: verbal nouns in -ás/-és",gtitle="Recap: Verbal Nouns in -ás/-és",
 storytitle="A megfigyelés szabályozása és a 2026-os választás",
 goals=["I can sum up the debate about the rules of covert surveillance before the election of 2026 and the change of government, with dates (*szabályozás, visszaélés, rendelet*).",
  "I can name a procedure with a verbal noun in *-ás/-és* (*a megfigyelés bírói engedélyezését*).",
  "I can report, with attribution, what each side proposed or held."]),
}
CONS=dict(title="Unit 35 Consolidation: Covert Surveillance and the Pegasus Case, 2021–2026",
 grammar="Review: reporting, obligation, certainty, concession and verbal nouns",
 goals=["I can summarise the Pegasus case between 2021 and 2026, with years and sources.",
  "I can report, qualify and contrast what the parties stated.",
  "I can give the result of the election of 12 April 2026 and the date of the election of the prime minister."])
INTRO=("Unit 35: "+TH,[
 "In July 2021 an international group of journalists reported that the spyware Pegasus had been used in several countries, among them Hungary. The Hungarian government said its secret services had acted within the law; critics, among them journalists and human rights organisations, questioned how covert surveillance was authorised and supervised. The case was also examined by a committee of the Hungarian parliament and by a committee of the European Parliament.",
 "In five short accounts you follow these events year by year, name who judged them how, and practise the forms a neutral history needs: reporting, obligation in the past, degrees of certainty, concession and verbal nouns. The period ends with the parliamentary election of 12 April 2026."])
GR={
1:("grammar/c1/c1-megfigyeles-01-a-gr.json","Recap: Reporting What Someone Stated",
 "You know *azt mondta, hogy* from B1 Unit 13 (*azt mondta / jelentette ki / közölte, hogy…*): a *hogy* clause gives what someone said. In a history it keeps each party's claim apart from the narrator's voice: *Az NSO Group azt közölte, hogy a programot csak állami szerveknek adja el.* The reporting verb is in the past and the clause keeps its own tense. New in this lesson is the vocabulary of surveillance.",
 "A magyar kormány azt mondta, hogy a titkosszolgálatok a törvényi keretek között működtek.",
 [("Az NSO Group azt közölte, hogy a programot csak állami szerveknek adja el.","The NSO Group stated that it sells the programme only to state bodies."),
  ("A magyar kormány azt mondta, hogy a titkosszolgálatok a törvényi keretek között működtek.","The Hungarian government said that the secret services had operated within the legal framework."),
  ("Az Amnesty azt közölte, hogy két magyar újságíró telefonján a kémszoftverre utaló nyomokat talált.","Amnesty stated that it had found traces pointing to the spyware on the phones of two Hungarian journalists.")]),
2:("grammar/c1/c1-megfigyeles-02-a-gr.json","Recap: Obligation in the Past",
 "You know *köteles* and *kénytelen* from B1 Unit 10: they say that a rule or a circumstance required someone to do something. In a history they describe what a rule required at the time, so the verb *volt* follows them: *a szolgálatok kötelesek voltak engedélyt kérni*. With a plural subject *köteles* takes the plural ending: *a szolgálatok kötelesek voltak*. New in this lesson is the vocabulary of authorising surveillance.",
 "A szolgálatok kötelesek voltak engedélyt kérni az igazságügyi minisztertől.",
 [("A szolgálatok kötelesek voltak engedélyt kérni az igazságügyi minisztertől.","The services had to ask the minister of justice for permission."),
  ("A szolgálat kénytelen volt a miniszterhez fordulni, ha titokban meg akart figyelni egy magánszemélyt.","The service had to turn to the minister if it wanted to watch a private person in secret."),
  ("A kormány szerint a szolgálatok kötelesek voltak betartani a törvényeket.","According to the government, the services had to keep to the laws.")]),
3:("grammar/c1/c1-megfigyeles-03-a-gr.json","Recap: Degrees of Certainty",
 "You know *aligha*, *minden bizonnyal* and *feltehetőleg* from C1 Unit 3: *feltehetőleg* marks a claim as probable, *minden bizonnyal* as very probable, *aligha* as unlikely; *valószínűleg* works like *feltehetőleg*. In a history they keep an assessment apart from the established facts: the dates and the court rulings are stated plainly, while a judgement about effects gets a hedge and a source: *A sajtószabadsággal foglalkozó szervezetek szerint a megfigyelés feltehetőleg elriasztotta a forrásokat.* New in this lesson is the vocabulary of press freedom.",
 "Aligha vitatható, hogy a Bíróság 1996-ban a sajtószabadság alapfeltételének nevezte a forrásvédelmet.",
 [("A sajtószabadsággal foglalkozó szervezetek szerint a megfigyelés feltehetőleg elriasztotta a forrásokat.","According to the organisations dealing with press freedom, the surveillance probably deterred sources."),
  ("Aligha vitatható, hogy a Bíróság 1996-ban a sajtószabadság alapfeltételének nevezte a forrásvédelmet.","It can hardly be disputed that in 1996 the Court called source protection a basic condition of press freedom."),
  ("Az érintett újságírók szerint a megfigyelés valószínűleg csökkentette a források bizalmát.","According to the journalists concerned, the surveillance probably reduced the sources' trust.")]),
4:("grammar/c1/c1-megfigyeles-04-a-gr.json","Recap: Concession",
 "You know *annak ellenére, hogy* from B1 Unit 5 (*annak ellenére, hogy sokat veszekedünk*): the clause names a fact that does not prevent the main clause. In a history it sets what one side held against what happened: *Annak ellenére, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt határozatképes.* The judgement stays with its source. New in this lesson is the vocabulary of parliamentary inquiry.",
 "Annak ellenére, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt határozatképes.",
 [("Annak ellenére, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt határozatképes.","Although the opposition had called the session, the committee did not have a quorum."),
  ("Annak ellenére, hogy a kormánypárti oldal szerint a megfigyelések törvényesek voltak, az Európai Parlament vizsgálóbizottságot hozott létre.","Although according to the governing side the surveillance had been lawful, the European Parliament set up a committee of inquiry."),
  ("Annak ellenére, hogy az ülés anyagát titkosították, a vita a nyilvánosságban folytatódott.","Although the material of the session was classified, the debate continued in public.")]),
5:("grammar/c1/c1-megfigyeles-05-a-gr.json","Recap: Verbal Nouns in -ás/-és",
 "You know *-ás* and *-és* from B1 Unit 16 (*olvas → olvasás*, *pihen → pihenés*): the ending turns a verb into a noun for the action. Reports and histories use these nouns to name a procedure: *engedélyez → engedélyezés*, *alkalmaz → alkalmazás*. The noun takes the endings of the sentence: *a megfigyelés bírói engedélyezését* (object), *a szabályozás* (subject). New in this lesson is the vocabulary of surveillance law.",
 "A jogvédő szervezetek a titkos megfigyelés bírói engedélyezését javasolták.",
 [("A jogvédő szervezetek a titkos megfigyelés bírói engedélyezését javasolták.","The human rights organisations proposed the judicial authorisation of covert surveillance."),
  ("A kormány szerint a szabályozás elegendő garanciát tartalmazott a visszaélések megelőzésére.","According to the government, the regulation contained sufficient guarantees for the prevention of abuse."),
  ("Az európai rendelet korlátozza a kémszoftverek alkalmazását újságírók ellen.","The European regulation restricts the use of spyware against journalists.")]),
}
VOC={
1:("The Pegasus Reports of 2021",[("kémszoftver","spyware","noun"),("titkosszolgálat","secret service","noun"),("megfigyelés","surveillance","noun"),("megfigyel","to put under surveillance, to watch","verb"),("tényfeltáró","investigative","adjective"),("célpont","target","noun"),("nyom","trace","noun"),("szerkesztőség","editorial office, newsroom","noun")]),
2:("Authorising Covert Surveillance, 2016–2021",[("engedélyezés","authorisation","noun"),("igazságügyi miniszter","minister of justice","expression"),("bírói engedély","judicial warrant","expression"),("garancia","guarantee, safeguard","noun"),("magánélet","private life","noun"),("jogvédő szervezet","human rights organisation","expression"),("ellenőrzés","oversight, supervision","noun")]),
3:("Journalists and Source Protection, 2021–2023",[("forrásvédelem","source protection","noun"),("forrás","source","noun"),("sajtószabadság","freedom of the press","noun"),("dermesztő hatás","chilling effect","expression"),("elriaszt","to deter, to scare off","verb"),("alapfeltétel","basic condition","noun"),("nemzetbiztonság","national security","noun"),("bizalom","trust","noun")]),
4:("The National Security Committee and the European Parliament, 2021–2023",[("Nemzetbiztonsági Bizottság","National Security Committee (of the Hungarian parliament)","noun"),("határozatképes","having a quorum","adjective"),("vizsgálóbizottság","committee of inquiry","noun"),("minősít","to classify (as secret)","verb"),("ülés","session, sitting","noun"),("ellenzék","opposition","noun"),("kezdeményez","to initiate, to propose","verb")]),
5:("Surveillance Law and the 2026 Election",[("szabályozás","regulation, set of rules","noun"),("visszaélés","abuse","noun"),("rendelet","regulation, decree","noun"),("korlátoz","to restrict","verb"),("megelőzés","prevention","noun"),("alkalmazás","use, application","noun"),("javasol","to propose","verb"),("elegendő","sufficient","adjective")]),
}
def EXS(n):
    s=S[n-1]; i=lambda st,k:f"{s}-{st}-{k}"
    if n==1: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent a kémszoftver szó?",["Olyan program, amellyel titokban megfigyelnek egy telefont.","Olyan program, amellyel gyorsabban lehet üzenetet küldeni.","Olyan alkalmazás, amellyel fényképet lehet szerkeszteni."],V),
 fb(i('controlled',2),'controlled','grammar',"Az NSO Group azt _____, hogy a programot csak állami szerveknek adja el.","The NSO Group stated that it sells the programme only to state bodies.",'reported-speech-statements',answers=['közölte','mondta'],hint='közöl, past, definite'),
 match(i('controlled',3),'controlled',[["kémszoftver","program a titkos megfigyelésre"],["titkosszolgálat","állami szerv, amely titokban gyűjt információt"],["tényfeltáró","olyan, aki rejtett tényeket derít ki"],["célpont","akit meg akarnak figyelni"],["szerkesztőség","az újságírók közös munkahelye"]],V),
 fb(i('practice',4),'practice','grammar',"A magyar kormány azt mondta, _____ a titkosszolgálatok a törvényi keretek között működtek.","The Hungarian government said that the secret services had operated within the legal framework.",'reported-speech-statements',ans='hogy'),
 sb(i('practice',5),'practice',"Az Amnesty azt közölte, hogy két magyar újságíró telefonján nyomokat talált.","Amnesty stated that it had found traces on the phones of two Hungarian journalists.",'reported-speech-statements'),
 dlg(i('dialogue',6),[("Kérdező","Mit közölt az NSO Group a programról?"),("Válaszadó","Az NSO Group azt közölte, _____ a programot csak állami szerveknek adja el.")],["hogy","amit","aki"],'reported-speech-statements'),
 wr(i('production',7),'production',"Write two sentences: say what the NSO Group stated and what the Hungarian government said in 2021, using reported speech.","Az NSO Group azt közölte, hogy a programot csak állami szerveknek adja el. A magyar kormány azt mondta, hogy a titkosszolgálatok a törvényi keretek között működtek.",'reported-speech-statements'),
 chk(i('check',8),["A kormány azt mondta, hogy a titkosszolgálatok törvényesen működtek.","A kormány azt mondta, hogy a titkosszolgálatok törvényesen működik.","A kormány azt mondta, a titkosszolgálatok hogy törvényesen működtek."],'reported-speech-statements'),
 ]
    if n==2: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent az engedélyezés szó?",["Az, hogy valaki hivatalosan megadja a jogot valamire.","Az, hogy valaki hivatalosan megtiltja egy döntés végrehajtását.","Az, hogy valaki nyilvánosan bírál egy döntést."],V),
 fb(i('controlled',2),'controlled','grammar',"A szolgálatok _____ voltak engedélyt kérni az igazságügyi minisztertől.","The services had to ask the minister of justice for permission.",'formal-obligation',answers=['kötelesek','kénytelenek'],hint='plural subject'),
 match(i('controlled',3),'controlled',[["engedélyezés","a jog hivatalos megadása valamire"],["garancia","biztosíték a visszaélés ellen"],["magánélet","ami nem tartozik a nyilvánosságra"],["ellenőrzés","annak vizsgálata, hogy valaki betartja-e a szabályokat"],["jogvédő szervezet","civil szervezet, amely az emberi jogokat védi"]],V),
 fb(i('practice',4),'practice','grammar',"A szolgálat _____ volt a miniszterhez fordulni, ha titokban meg akart figyelni egy magánszemélyt.","The service had to turn to the minister if it wanted to watch a private person in secret.",'formal-obligation',answers=['kénytelen','köteles']),
 sb(i('practice',5),'practice',"A szolgálatok kötelesek voltak engedélyt kérni az igazságügyi minisztertől.","The services had to ask the minister of justice for permission.",'formal-obligation'),
 dlg(i('dialogue',6),[("Kérdező","Mit írt elő a szabályozás a szolgálatoknak a titkos megfigyelés előtt?"),("Válaszadó","A szolgálatok _____ voltak engedélyt kérni az igazságügyi minisztertől.")],["kötelesek","kötelezően","kötelezés"],'formal-obligation'),
 wr(i('production',7),'production',"Write two sentences: say what the services had to do before a covert surveillance and what the European Court of Human Rights found in 2016.","A szolgálatok kötelesek voltak engedélyt kérni az igazságügyi minisztertől. Az Emberi Jogok Európai Bírósága 2016-ban megállapította, hogy a szabályozás nem nyújtott elegendő garanciát a visszaélések ellen.",'formal-obligation'),
 chk(i('check',8),["A szolgálatok kötelesek voltak engedélyt kérni.","A szolgálatok köteles voltak engedélyt kérni.","A szolgálatok kötelesek voltak engedélyt kérnie."],'formal-obligation',{"2":"inflected-infinitives"}),
 ]
    if n==3: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent a forrásvédelem szó?",["Az újságíró nem köteles elárulni, ki adott neki információt.","Az újságíró köteles minden forrását nyilvánosságra hozni.","A rendőrség őrzi az újságíró lakását."],V),
 fb(i('controlled',2),'controlled','grammar',"A sajtószabadsággal foglalkozó szervezetek szerint a megfigyelés _____ elriasztotta a forrásokat.","According to the organisations dealing with press freedom, the surveillance probably deterred sources.",'epistemic-hedging',answers=['feltehetőleg','valószínűleg'],hint='probably'),
 match(i('controlled',3),'controlled',[["forrás","aki vagy ami információt ad egy újságírónak"],["sajtószabadság","a sajtó joga a szabad tájékoztatásra"],["dermesztő hatás","a félelem, amely visszatart a szólástól"],["nemzetbiztonság","az állam külső és belső védelme"],["bizalom","az, hogy valakire rá merünk bízni valamit"]],V),
 fb(i('practice',4),'practice','grammar',"_____ vitatható, hogy a Bíróság 1996-ban a sajtószabadság alapfeltételének nevezte a forrásvédelmet.","It can hardly be disputed that in 1996 the Court called source protection a basic condition of press freedom.",'epistemic-hedging',ans='Aligha',hint='hardly'),
 sb(i('practice',5),'practice',"Az érintett újságírók szerint a megfigyelés valószínűleg csökkentette a források bizalmát.","According to the journalists concerned, the surveillance probably reduced the sources' trust.",'epistemic-hedging'),
 dlg(i('dialogue',6),[("Kérdező","Hogyan fogalmaztak óvatosan a szervezetek a megfigyelés hatásáról?"),("Válaszadó","A megfigyelés _____ elriasztotta a forrásokat.")],["feltehetőleg","aligha","egyértelműen"],'epistemic-hedging'),
 wr(i('production',7),'production',"Write one sentence with a hedge: say what the organisations dealing with press freedom thought the surveillance probably did to sources.","A sajtószabadsággal foglalkozó szervezetek szerint a megfigyelés feltehetőleg elriasztotta a forrásokat attól, hogy újságírókkal beszéljenek.",'epistemic-hedging'),
 chk(i('check',8),["Az újságírók szerint a megfigyelés feltehetőleg elriasztotta a forrásokat.","Az újságírók szerint a megfigyelés feltehetőleg elriasztott a forrásokat.","Az újságírók szerint a megfigyelés feltehetőleg elriasztották a forrásokat."],'epistemic-hedging'),
 ]
    if n==4: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent a határozatképes szó?",["Egy testület elegendő taggal vesz részt az ülésen.","Egy testület titokban tartja az ülés anyagát.","Egy testület szavazás nélkül hoz döntést."],V),
 fb(i('controlled',2),'controlled','grammar',"Annak _____, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt határozatképes.","Although the opposition had called the session, the committee did not have a quorum.",'concessive-annak-ellenere',ans='ellenére'),
 match(i('controlled',3),'controlled',[["Nemzetbiztonsági Bizottság","a parlament testülete, amely a titkosszolgálatokat ellenőrzi"],["vizsgálóbizottság","testület, amelyet egy ügy kivizsgálására hoznak létre"],["minősít","titkossá nyilvánít"],["ellenzék","a kormányon kívüli pártok"],["ülés","a testület tagjainak találkozója"]],V),
 fb(i('practice',4),'practice','grammar',"Annak ellenére, _____ az ülés anyagát titkosították, a vita a nyilvánosságban folytatódott.","Although the material of the session was classified, the debate continued in public.",'concessive-annak-ellenere',ans='hogy'),
 sb(i('practice',5),'practice',"Annak ellenére, hogy a kormánypárti oldal szerint a megfigyelések törvényesek voltak, az Európai Parlament vizsgálóbizottságot hozott létre.","Although according to the governing side the surveillance had been lawful, the European Parliament set up a committee of inquiry.",'concessive-annak-ellenere'),
 dlg(i('dialogue',6),[("Kérdező","Miért nem tudott ülésezni a bizottság az első alkalommal?"),("Válaszadó","Annak ellenére, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt _____.")],["határozatképes","határozatlan","határozott"],'concessive-annak-ellenere'),
 wr(i('production',7),'production',"Write one sentence with annak ellenére, hogy: say what happened to the committee although the opposition had called the session.","Annak ellenére, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt határozatképes.",'concessive-annak-ellenere'),
 chk(i('check',8),["Annak ellenére, hogy az ellenzék kezdeményezte az ülést, a bizottság nem volt határozatképes.","Annak ellenére, hogy az ellenzék kezdeményezte az ülést, miatt a bizottság nem volt határozatképes.","Annak ellenére, az ellenzék kezdeményezte az ülést hogy, a bizottság nem volt határozatképes."],'concessive-annak-ellenere'),
 ]
    if n==5: return [
 mc(i('introduce',1),'introduce','vocabulary',"Mit jelent a visszaélés szó?",["Egy jog vagy hatalom szabálytalan használata.","Egy jog hivatalos átadása egy polgárnak.","Egy szabály módosítása a parlamentben."],V),
 fb(i('controlled',2),'controlled','grammar',"A jogvédő szervezetek a titkos megfigyelés bírói _____ javasolták.","The human rights organisations proposed the judicial authorisation of covert surveillance.",'nominalization',ans='engedélyezését',hint='engedélyez, verbal noun, object'),
 match(i('controlled',3),'controlled',[["szabályozás","a szabályok összessége"],["visszaélés","egy jog helytelen használata"],["rendelet","kötelező erejű jogi szabály"],["megelőzés","annak elkerülése, hogy valami megtörténjen"],["alkalmazás","az, hogy valamit használnak"]],V),
 fb(i('practice',4),'practice','grammar',"A kormány szerint a szabályozás elegendő garanciát tartalmazott a visszaélések _____.","According to the government, the regulation contained sufficient guarantees for the prevention of abuse.",'nominalization',ans='megelőzésére',hint='megelőz, verbal noun, for'),
 sb(i('practice',5),'practice',"Az európai rendelet korlátozza a kémszoftverek alkalmazását újságírók ellen.","The European regulation restricts the use of spyware against journalists.",'nominalization'),
 dlg(i('dialogue',6),[("Kérdező","Mit javasoltak a jogvédő szervezetek a titkos megfigyeléssel kapcsolatban?"),("Válaszadó","A titkos megfigyelés bírói _____ javasolták.")],["engedélyezését","engedélyezni","engedélyezése"],'nominalization',),
 wr(i('production',7),'production',"Write one sentence with a verbal noun: say what the human rights organisations proposed.","A jogvédő szervezetek a titkos megfigyelés bírói engedélyezését javasolták.",'nominalization'),
 chk(i('check',8),["A jogvédő szervezetek a titkos megfigyelés bírói engedélyezését javasolták.","A jogvédő szervezetek a titkos megfigyelés bírói engedélyezni javasolták.","A jogvédő szervezetek a titkos megfigyelés bírói engedélyezett javasolták."],'nominalization',{"1":"building-the-infinitive-the-suffix-ni","2":"past-tense-indefinite"}),
 ]
def CEX():
    i=lambda k:f"{P}-consolidation-{k}"
    return [
 mc(i(1),'recognize','grammar',"Melyik mondat adja vissza, mit közölt az NSO Group?",["Az NSO Group azt közölte, hogy a programot csak állami szerveknek adja el.","Az NSO Group azt közölte, a programot hogy csak állami szerveknek adja el.","Az NSO Group azt közölte, hogy a programot csak állami szerveknek adjam el."],'reported-speech-statements'),
 mc(i(2),'recognize','grammar',"Which sentence says that the services had to ask for permission?",["A szolgálatok kötelesek voltak engedélyt kérni.","A szolgálatok köteles voltak engedélyt kérni.","A szolgálatok kötelesen voltak engedélyt kérni."],'formal-obligation'),
 match(i(3),'recognize',[["kémszoftver","program a titkos megfigyelésre"],["forrásvédelem","az újságíró nem köteles elárulni a forrását"],["vizsgálóbizottság","testület, amelyet egy ügy kivizsgálására hoznak létre"],["határozatképes","elegendő taggal ülésező"],["bírói engedély","a bíró hivatalos jóváhagyása"]],V),
 fb(i(4),'recall','vocabulary',"Az NSO Group által fejlesztett Pegasus egy _____.","The Pegasus, developed by the NSO Group, is spyware.",V,ans='kémszoftver',hint='spyware'),
 fb(i(5),'recall','vocabulary',"Az ellenzék kezdeményezte a Nemzetbiztonsági Bizottság ülését, de a bizottság nem volt _____.","The opposition called a session of the National Security Committee, but the committee did not have a quorum.",V,ans='határozatképes'),
 fb(i(6),'recall','grammar',"Annak _____, hogy az ellenzék kezdeményezte az ülést, a kormánypárti képviselők nem jelentek meg.","Although the opposition called a session, the pro-government members did not appear.",'concessive-annak-ellenere',ans='ellenére'),
 fb(i(7),'context','grammar',"Az európai rendelet korlátozza a kémszoftverek _____ újságírók ellen.","The European regulation restricts the use of spyware against journalists.",'nominalization',ans='alkalmazását',hint='alkalmaz, verbal noun, object'),
 fb(i(8),'context','grammar',"A szolgálat _____ volt a miniszterhez fordulni a titkos megfigyelés előtt.","The service had to turn to the minister before a covert surveillance.",'formal-obligation',answers=['kénytelen','köteles']),
 mc(i(9),'context','grammar',"Which word marks the claim as probable? 'A megfigyelés _____ elriasztotta a forrásokat.'",["feltehetőleg","aligha","bizonyosan"],'epistemic-hedging'),
 sb(i(10),'produce',"A kormány azt mondta, hogy a rendszer a törvényekkel összhangban működött.","The government said that the system had operated in line with the laws.",'reported-speech-statements'),
 wr(i(11),'production',"Write two sentences about the case of Szabó and Vissy: give the date of the judgment and what the Court found.","2016. január 12-én az Emberi Jogok Európai Bírósága meghozta a Szabó és Vissy kontra Magyarország ügy ítéletét. A Bíróság megállapította, hogy a szabályozás nem nyújtott elegendő garanciát a visszaélések ellen.",V),
 wr(i(12),'production',"Write two sentences about the elections of 2026: give the result of 12 April and the election of the prime minister on 9 May.","2026. április 12-én a Tisza Párt a 199 mandátumból 141-et szerzett. 2026. május 9-én az Országgyűlés Magyar Pétert választotta miniszterelnökké.",V),
 ]
CFG=dict(prefix=P,unit=35,V=V,TH=TH,S=S,STORY=STORY,TEXT=TEXT,SUMMARY=SUMMARY,LESSONS=LESSONS,CONS=CONS,INTRO=INTRO,GR=GR,VOC=VOC,EXS=EXS,CEX=CEX)
if __name__=='__main__':
    if sys.argv[1:]==['run']: run(CFG)
    else: counts(CFG)
