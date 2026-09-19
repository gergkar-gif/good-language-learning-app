#!/usr/bin/env python3
"""Re-author all 36 Hungarian B1 Citizenship track stories.

Applies 'The Rest is History' narrative storytelling architecture:
- Dramatic hooks, scene setting, and human agency.
- Punchy sentences: average 10-15 words, maximum <= 22 words.
- Focus on the Hungarian naturalization (egyszerűsített honosítás) citizenship interview.
- >= 85% inclusion of newly taught target vocabulary in natural narrative context.
- Eliminates dry academic historiography and archaic feudal pedantry.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "content", "hu", "stories", "world", "b1")

STORIES = {
    # =========================================================================
    # UNIT: b1-orszagma (Hungary Today: Land & Symbols)
    # =========================================================================
    "b1-orszagma-01-elhelyezkedes.json": [
        "Európa térképe állandóan változott az évszázadok során. De hol van Magyarország pontos helye ezen a kontinensen?",
        "Magyarország Közép-Európa szívében helyezkedik el. Ez az elhelyezkedés stratégiai és történelmi szempontból is kiemelkedő.",
        "Az ország a természeti szépségekben gazdag Kárpát-medence területén fekszik. A medencét északról és keletről a Kárpátok hegyei védik.",
        "Az ország területe ma mintegy kilencvenháromezer négyzetkilométer. A jelenlegi lakosság száma megközelítőleg tízmillió fő.",
        "Egy állampolgársági interjún gyakran elhangzik ez a kérdés. Magyarország fekvése ugyanis meghatározza a kultúráját, gazdaságát és az egész nemzeti sorsát."
    ],
    "b1-orszagma-02-megyekesvarosok.json": [
        "Képzeljünk el egy országot, amelyet két fenséges folyó szel ketté. Ez Magyarország földrajzi valósága.",
        "Az ország politikai, kulturális és gazdasági központja a főváros, Budapest. A Duna partján fekvő világváros két történelmi részből, Budából és Pestből egyesült.",
        "A másik fontos folyó a Tisza, amely a keleti síkság tájait öntözi, majd délen a Dunába torkollik.",
        "Nyugaton terül el Közép-Európa legnagyobb édesvizű tava, a Balaton. A magyarok szeretettel hívják ezt a csodás tavat magyar tengernek.",
        "Közigazgatási szempontból az ország tizenkilenc megyére oszlik. A táj rendkívül változatos: a végtelen Alföld síkság mellett festői középhegységek is magasodnak."
    ],
    "b1-orszagma-03-zaszlocimer.json": [
        "Minden független ország legszentebb kincsei a nemzeti jelképek. De mit jelentenek ezek egy leendő állampolgár számára?",
        "A magyar nemzeti zászló három vízszintes színből áll. A piros szín az erőt, a fehér a hűséget, a zöld pedig a reményt szimbolizálja.",
        "Mellette büszkén áll a magyar címer. A címer központi eleme egy függőlegesen osztott pajzs.",
        "A pajzs bal oldalán az Árpád-ház történelmi piros és ezüst sávjai láthatók. A jobb oldalon a zöld hármas halom, rajta arany korona és ezüst kettős kereszt emelkedik.",
        "A pajzs felső élén a keresztény államiság jelképe, a ferde keresztű Szent Korona nyugszik. Ezek a szimbólumok ezer év küzdelmeit őrzik."
    ],
    "b1-orszagma-04-szomszedosorszagok.json": [
        "Vegyünk a kezünkbe egy friss európai térképet. Mi tűnik fel azonnal Magyarország határainál?",
        "Magyarország hét szomszédos országgal határos. Ez a különleges helyzet élénk kulturális és gazdasági kapcsolatokat teremt.",
        "Északon Szlovákia a szomszéd. Északkeleten Ukrajnával, keleten pedig Romániával érintkezik a magyar határ.",
        "Dél felé haladva Szerbia, Horvátország és Szlovénia következik. Nyugaton Ausztria zárja a sort, amely hosszú évszázadokon át közös birodalmat alkotott Magyarországgal.",
        "Egy honosítási beszélgetésen elengedhetetlen a szomszédok ismerete. A határon túli magyar közösségek miatt ezek a kapcsolatok ma is különösen fontosak."
    ],
    "b1-orszagma-05-attekintes.json": [
        "Elérkezett a várva várt nap: a hivatalos állampolgársági interjú pillanata a hivatalban.",
        "Minden leendő állampolgár számára elengedhetetlen a felkészülés: a vizsgán konkrét kérdésekre kell válaszolni.",
        "A jelentkező magabiztosan összefoglalja a tanultakat, és jellemzi Magyarország fekvését és domborzatát.",
        "Beszél a nemzet történelméről, a jellegzetes hagyományokról és a magyar kultúráról szerzett gazdag ismereteiről.",
        "A sikeres honosítás után a jelentkező büszkén teheti le az esküt, és a magyar közösség teljes jogú tagjává válik."
    ],
    "b1-orszagma.json": [
        "Közép-Európa szívében, a festői Kárpát-medence ölelésében terül el Magyarország. Ez a föld ezer éven át harcok, szövetségek és újjászületések színhelye volt.",
        "Az ország szíve Budapest, a Duna partján fekvő lenyűgöző főváros. A táj gazdag kontrasztokban: az Alföld békés síksága, a hegyek és a csillogó Balaton mind hozzátartoznak.",
        "A magyar államiság legfőbb kifejezői a nemzeti jelképek. A piros-fehér-zöld zászló és a Szent Koronával díszített címer a nemzet büszkeségét hirdeti.",
        "Hét szomszédos ország veszi körül Magyarországot. A történelmi határok mentén ma is milliók élnek, akik ápolják a magyar nyelvet és hagyományokat.",
        "Egy állampolgársági vizsgán mindez alapvető tudás. De a legfontosabb mégis a személyes kötődés a kultúrához és a nemzethez."
    ],

    # =========================================================================
    # UNIT: b1-karpatmedence (The Carpathian Basin Before the Magyars)
    # =========================================================================
    "b1-karpatmedence-01-korainepek.json": [
        "Évszázadokkal a magyarok érkezése előtt a Kárpát-medence tájai már élettel teltek meg. Kik laktak itt a történelem hajnalán?",
        "A vaskor és az ókor idején különböző törzsek fedezték fel a termékeny völgyeket. A Duna mentén virágzó falvak épültek.",
        "Az egyik legjelentősebb nép a kelta volt. Ők fejlett kézművességgel, fémmegmunkálással és kereskedelemmel foglalkoztak a vidéken.",
        "A kelták letelepedtek a folyók közelében, és erődített településeket hoztak létre. Ők lettek a térség meghatározó őslakosai.",
        "A Kárpátok természetes fala már ekkor is kiváló védelmet nyújtott. A medence bőséges vizei és termékeny földjei vonzották a hódítókat."
    ],
    "b1-karpatmedence-02-pannonia.json": [
        "A Kr. u. első században a világ akkori ura, a hatalmas Római Birodalom észak felé terjeszkedett. A légiók elérték a Dunát.",
        "A rómaiak meghódították a Duna jobb partját, és megalapították Pannonia tartományt. Ezzel megkezdődött a vidék római korszaka.",
        "Erős kőből épült erődök és virágzó városok nőttek ki a földből. Ilyen volt Aquincum a mai Óbuda helyén, vagy Savaria a mai Szombathelyen.",
        "A légiók katonai utakat építettek, és megindult a pezsgő kereskedelem. Megjelent a szőlőtermesztés, a kőépítészet és az írásbeliség kultúrája.",
        "Négyszáz év után a birodalom meggyengült, és a légiók kivonultak. De a római romok és utak emléke örökre megmaradt Pannónia földjén."
    ],
    "b1-karpatmedence-03-nepvandorlas.json": [
        "A római légiók távozása után hatalmas vihar tört ki Közép-Európában: kezdetét vette a népvándorlás viharos korszaka.",
        "Kelet felől egymás után vándoroltak be a harcias nomád és germán népek. Először a félelmetes hunok érkeztek Attila király vezetésével.",
        "A hunok után gót harcosok és más germán törzsek foglalták el a vidéket. A korábbi városok romba dőltek.",
        "Később a keleti sztyeppékről az avarok vették át az uralmat. Erős lovas birodalmat alapítottak, miközben szláv csoportok telepedtek le a folyók mentén.",
        "Amikor Nagy Károly frank uralkodó seregei betörtek a térségbe, az avar hatalom felbomlott. A Kárpát-medence új urakra várt."
    ],
    "b1-karpatmedence-04-kikeltekitt.json": [
        "A kilencedik század végén egyetlen fejedelem sem uralkodott egyedül a Kárpát-medence egész területén.",
        "Több különböző nép és helyi uralkodó élt itt egymás mellett egyidejűleg a folyók völgyeiben.",
        "A korábbi római és avar uralom nyomai és emlékei még mindig jól látszottak az épületeken és utakon.",
        "A szláv és kései avar falvak lakói békében éltek, és ez a színes korszak megőrizte a különféle kultúrák gazdagságát.",
        "Az itt élő népek később könnyen beolvadtak a magyarságba, gazdagítva a kultúrát saját hatásaikkal és szokásaikkal."
    ],
    "b1-karpatmedence-05-honfoglalaselott.json": [
        "A magyarok korábban nomád lovas népként éltek a keleti síkságokon a hét törzs szövetségében.",
        "A törzsszövetség bölcs vezetői tudták, hogy a Kárpát-medence termékeny földje nem teljesen lakatlan vidék.",
        "A korábbi háborúk miatt azonban több terület elnéptelenedett, így bőséges hely jutott az új otthonnak.",
        "895-ben a magyar hadak átvonultak a magas hegyeken, hogy új hazát és biztonságos hont alapítsanak.",
        "Ezzel megkezdődött a dicsőséges honfoglalás, amelyből egy évszázaddal később megszületett az első magyar keresztény királyság."
    ],
    "b1-karpatmedence.json": [
        "A Kárpát-medence története nem a semmiből indult. Már évezredekkel a magyarok előtt virágzó népek találtak menedéket a Kárpátok ölelésében.",
        "A kelták fémkincsei után a büszke Római Birodalom hódította meg Pannónia földjét. Aquincum kőfalai és a római utak máig hirdetik az ókori civilizáció nagyságát.",
        "A népvándorlás vihara hunokat, gótokat és avarokat hozott a síkságra. Birodalmak születtek és tűntek el egymás után a történelem színpadán.",
        "A kilencedik század végén a tágas medence megosztott volt és új vezetésre várt. A folyók, legelők és hegyek készen álltak az új korszakra.",
        "Ekkor érkeztek meg a magyarok a hágókon át. Ezzel lezárult a vándorlás kora, és megszületett a Kárpát-medence új, ezeréves jövője."
    ],

    # =========================================================================
    # UNIT: b1-honfoglalas (The Honfoglalás 895)
    # =========================================================================
    "b1-honfoglalas-01-nyugatranyomas.json": [
        "A 9. század végén a délorosz sztyeppe végtelen vidéke forrongott. A magyarok akkori hazája, Etelköz veszélybe került.",
        "A keleti sztyeppéken megindult a besenyő és a kazár törzsek terjeszkedése. A katonai nyomás hónapról hónapra növekedett.",
        "A magyar törzsfők felismerték a fenyegetést. A nehéz helyzet arra kényszerítette a népet, hogy új, biztonságos lakóhelyet keressen.",
        "A vezérek bölcs szövetséget kötöttek egymással. Nem akartak szétszéledni, hanem egységes akarattal döntöttek a nyugati vándorlás mellett.",
        "Ez a stratégiai döntés mentette meg a nemzetet. A törzsek elindultak nyugat felé, a hatalmas hegyek irányába."
    ],
    "b1-honfoglalas-02-atkeles.json": [
        "895 tavaszán a magyar törzsek elhagyták korábbi szállásterületüket, Etelközt, és elindultak a hegyek felé.",
        "A cél a Kárpátok meredek vonulata volt. A törzsek a hágók felé vették az irányt családjaikkal és állataikkal.",
        "A fő sereg a festői Vereckei-hágó szikláin keresztül kelt át. Az átkelés fegyelmezetten és gyorsan zajlott.",
        "Minden magyar harcos hűséges fegyvere a híres íj és a tegezben lapuló hegyes nyíl volt.",
        "Amikor átkeltek a magas hegyeken, a bátor nép előtt kitárult az új haza, a Kárpát-medence tágas síksága."
    ],
    "b1-honfoglalas-03-arpadeshettorzs.json": [
        "A honfoglaló magyar nép hét független törzsből állt, amelyek mind saját nemzetségi hagyományokkal rendelkeztek.",
        "Hogy megvédjék magukat a veszélyektől, a törzsek úgy döntöttek, egyetlen erős szövetségben egyesülnek.",
        "A hét vezér még a vándorlás idején ünnepélyes vérszerződést kötött, és közös esküt tett a vérrel teli serleg felett.",
        "Megválasztották Árpádot az egész nép legfőbb fejedelmének, akinek szava minden törzs számára kötelező volt.",
        "Árpád fejedelem és a hét vezér bölcsessége biztosította a nemzeti egységet az új hazában."
    ],
    "b1-honfoglalas-04-birtokbavetel.json": [
        "A Kárpátokon való sikeres átkelés után a magyar törzsek fokozatosan elfoglalták az egész Kárpát-medencét.",
        "A nép gyorsan terjeszkedett a termékeny vidéken: először a tágas Alföld zöld legelőit vették birtokba.",
        "A magyarok hagyományos életformája a pásztorkodás és az állattenyésztés volt, amihez a síkság tökéletes feltételeket nyújtott.",
        "A törzsek alig találkoztak fegyveres ellenállással a helyi lakosság részéről a Dunántúlon és északon.",
        "A helyi szláv és avar népességgel békésen keveredtek, adót szedtek, és közösen kezdték el művelni a földeket."
    ],
    "b1-honfoglalas-05-nemzetiemlekezet.json": [
        "A honfoglalás ezeréves évfordulóján, 1896-ban Magyarország fényes Millenniumi ünnepségeket tartott a nemzet tiszteletére.",
        "Ekkor épült fel a Hősök tere és a hatalmas Millenniumi emlékmű Budapest szívében, amely Árpádot és a hét vezért ábrázolja.",
        "A magyar mondák máig őrzik a szent turulmadár és a csodaszarvas legendás alakját.",
        "Ez a gazdag történelmi örökség és a sok évszázados hagyomány képezi a mai magyar nemzeti identitás legfontosabb alapját.",
        "Egy állampolgársági interjún Árpád emléke büszkeségre ad okot minden leendő magyar polgárnak."
    ],
    "b1-honfoglalas.json": [
        "A 9. század végén a magyar törzsek sorsdöntő válaszút elé kerültek a keleti sztyeppén. A túlélésért új, védett otthont kellett találniuk.",
        "A hét vezér Etelközben vérszerződéssel pecsételte meg a szövetséget, és Árpád fejedelmet választotta meg vezetőnek. Megszületett a nemzeti egység.",
        "895-ben megkezdődött a honfoglalás. A magyarok a Vereckei-hágón és a Kárpátok hágóin átkelve birtokba vették a termékeny Kárpát-medencét.",
        "A törzsek letelepedtek a folyók és a tágas legelők mellett. Békében éltek a helyi népekkel, és erős, biztonságos hazát alapítottak.",
        "Árpád és a honfoglaló ősök emléke máig él a Hősök terén és a nemzet szívében. Ez az ezeréves magyar államiság kezdete."
    ],

    # =========================================================================
    # UNIT: b1-istvankiraly (Saint Stephen & the Founding of the State 1000)
    # =========================================================================
    "b1-istvankiraly-01-gezafejedelem.json": [
        "A tizedik század végén a magyar törzsek feje Géza fejedelem volt. Ő felismerte, hogy a pogány világ ideje lejárt.",
        "A megmaradás érdekében az ország kereszténységre való vezetése mellett döntött. Elhatározta, hogy a nép áttér az új hitre.",
        "Nyugati hittérítő papokat hívott be, hogy terjesszék a keresztény vallást. Az egyház gyorsan építeni kezdte az első templomokat.",
        "Géza megkeresztelkedett, és fiát, Istvánt is megkereszteltette. Erős dinasztikus szövetségeket kötött a szomszédos keresztény államokkal.",
        "Géza fejedelem békét teremtett a határokon, és előkészítette fiának az utat a királyi trón felé."
    ],
    "b1-istvankiraly-02-koronazas.json": [
        "Esztergom, az 1000. év karácsonya. Az egész keresztény Európa lélegzetvisszafojtva figyelt.",
        "A fiatal István apjától, Gézától örökölte a fejedelmi hatalmat, de most királyként akart uralkodni.",
        "II. Szilveszter pápa áldását adta, és díszes királyi koronát küldött Rómából az új államnak.",
        "A főpapok szent olajjal kenték fel az uralkodót. Az ünnepélyes koronázás pillanatában István elfoglalta a magyar trónt.",
        "István tudta, hogy a hatalom óriási felelősség. Erős és független keresztény országot akart hagyni minden későbbi utód számára."
    ],
    "b1-istvankiraly-03-keresztenykiralysag.json": [
        "A korona megszerzése után István király azonnal hozzálátott az ország megszervezéséhez. Hatalmas munka várt rá.",
        "A pogány törzsfők lázadásait fegyverrel verte le, biztosítva a belső békét. Szigorú, de igazságos törvénykönyveket adott ki.",
        "Tíz egyházmegyét alapított, élükre püspököket állított, és megkezdte a gazdag kolostorok építését. Elrendelte, hogy minden tíz falu építsen egy templomot.",
        "Bevezette a tized fizetését az egyház és az állam fenntartására. A keresztény hit a mindennapi élet alapjává vált.",
        "István király kemény kézzel, de tiszta szívvel vezette népét a civilizáció és az európai jövő felé."
    ],
    "b1-istvankiraly-04-szentistvanoroksege.json": [
        "1038-ban elhunyt az első király, de hatalmas öröksége örökre fennmaradt az utókor számára.",
        "István király bölcs intelmeket írt fiának, Imre hercegnek a keresztény hitről és az igazságos kormányzásról.",
        "1083-ban István királyt a katolikus egyház szentté avatta, és ő lett Magyarország fő védőszentje.",
        "Számos szép legenda és monda született csodás tetteiről, tiszteletére pedig az ország minden évben megemlékezik.",
        "Augusztus 20-a, Szent István napja ma Magyarország legfontosabb hivatalos nemzeti ünnepe."
    ],
    "b1-istvankiraly-05-szentkorona.json": [
        "A magyar történelem legszentebb kincse a Szent Korona és az ezeréves koronázási jelvények együttese.",
        "A királyi szimbólumok közé tartozik még a díszes jogar, az arany országalma és a selyemből szőtt koronázási palást.",
        "Ez a felbecsülhetetlen értékű ereklye a független keresztény államiság és a nemzeti folytonosság legfőbb jelképe.",
        "Bár az első királyi dinasztia kihalt, a Szent Korona eszméje évszázadokon át összetartotta a nemzetet.",
        "A koronát ma fegyveres katonák őrzik a Parlament Kupolacsarnokában, ahol mindenki megcsodálhatja."
    ],
    "b1-istvankiraly.json": [
        "Géza fejedelem felismerte, hogy a magyarság csak a keresztény Európához csatlakozva maradhat fenn. Fia, István ezt a történelmi feladatot teljesítette be.",
        "1000 karácsonyán a pápától kapott koronával megkoronázták Istvánt. Megszületett a független Magyar Királyság.",
        "István templomokat épített, törvényeket alkotott és megalapította az egyházmegyéket. Szigorú hite és bölcsessége szilárd alapokra helyezte az államot.",
        "Halála után szentté avatták. Augusztus 20-a, Szent István napja az államalapítás legfényesebb nemzeti ünnepe lett.",
        "A Parlamentben őrzött Szent Korona máig a magyar államiság és a nemzeti büszkeség legfőbb szimbóluma."
    ],

    # =========================================================================
    # UNIT: b1-arpadhaz (The Árpád Dynasty)
    # =========================================================================
    "b1-arpadhaz-01-arpadhazikiralyok.json": [
        "Szent István után a hatalom az Árpád-ház kezében maradt. Ez a dinasztia három évszázadon át formálta az ország sorsát.",
        "Az Árpád-házi királyok mind István rokonai voltak, tőle származtak vagy a dinasztia más ágából leszármazott utódok voltak.",
        "Szent László király szigorú törvénykönyvet adott ki, és a határok védelmében sikeres hadjáratokat vezetett. Később őt is szentté avatták.",
        "Könyves Kálmán király igazi tudós uralkodó volt. Felvilágosult módon eltörölte a boszorkányok büntetését, mondván: boszorkányok nem léteznek.",
        "Az Árpád-ház királyai és szentjei örökre a nemzet büszkeségei maradtak."
    ],
    "b1-arpadhaz-02-aranybulla.json": [
        "1222 tavaszán Székesfehérváron gyűlt össze a felháborodott magyar nemesség. Számos súlyos sérelmet akartak orvosolni.",
        "A király, II. András hatalmas birtokokat osztogatott el, ezért a nemesek írásban követelték régi jogaik védelmét.",
        "A király kénytelen volt kiadni a híres Aranybullát, amely megerősítette a nemesi kiváltságokat és az adómentességet.",
        "A dokumentum korlátozta az uralkodó teljhatalmát, sőt tartalmazta a híres ellenállási jogot is a királyi törvényszegések esetére.",
        "Az Aranybulla évszázadokon át a magyar alkotmányosság és jogállamiság büszke történelmi alapja maradt."
    ],
    "b1-arpadhaz-03-orszagszervezes.json": [
        "Hogyan irányították az Árpád-kori országot? A királyság alapját a vármegyék szilárd rendszere alkotta.",
        "Minden vármegye élén a király megbízott tisztviselője, az ispán állt, aki a rendért és az adókért felelt.",
        "A megye székhelye a királyi vár volt, amelyhez hatalmas földbirtok tartozott a gazdaság fenntartására.",
        "1241-ben a pusztító tatárjárás szinte minden fa- és földvárat elpusztított a síkságokon.",
        "A vész után a király újjáépítette az országot: parancsára erős kővárak épültek a hegycsúcsokon a jövő védelmére."
    ],
    "b1-arpadhaz-04-egyhazesallam.json": [
        "A középkori Magyarországon a keresztény vallás és a királyi hatalom szorosan összefonódott egymással.",
        "Szent István és utódai tíz egyházmegyét hoztak létre, amelyek élén a művelt esztergomi érsek és a püspökök álltak.",
        "A királyi udvar és a nemesek bőkezűen támogatták az új kolostorok építését országszerte.",
        "A jámbor szerzetesek könyveket másoltak, gyógyították a szegényeket és terjesztették a latin nyelvű egyházi kultúrát.",
        "A nép tizedet fizetett a papoknak a termésből, a templom pedig a közösségi élet legfőbb központja lett."
    ],
    "b1-arpadhaz-05-arpadhazvege.json": [
        "1301. január 14-én meghalt III. András király, és ezzel végérvényesen kihalt az Árpád-ház dicső férfiága.",
        "Nem maradt közvetlen törvényes trónörökös a dinasztiából, ami miatt azonnal súlyos örökösödési válság robbant ki.",
        "A királyi dinasztia kihalása után a leggazdagabb főurak könyörtelen hatalmi harcot kezdtek a korona megszerzéséért.",
        "Az ország éveken át küzdött a belső békéért, míg végül új, európai uralkodóházak léptek a trónra.",
        "Bár az Árpád-ház fiúága kihalt, szellemi örökségük ezer éven át a magyar nemzeti önazonosság legfőbb tartópillére maradt."
    ],
    "b1-arpadhaz.json": [
        "Az Árpád-ház uralkodása alatt Magyarország Közép-Európa vezető keresztény királyságává vált. Szent László és Könyves Kálmán neve máig legendás.",
        "1222-ben II. András kiadta az Aranybullát, amely megalapozta a nemesi jogokat és a magyar jogállamiság hagyományait.",
        "Az országot a királyi vármegyék rendszere fogta össze. A tatárjárás vihara után az uralkodók modern kővárakkal erősítették meg a védelmet.",
        "Az egyház és az állam együttműködése virágzó kultúrát és európai műveltséget teremtett a Kárpát-medencében.",
        "Amikor 1301-ben III. András halálával kihalt a dinasztia férfiága, lezárult az első királyi ház korszaka. Örökségük a nemzet szilárd alapja maradt."
    ],

    # =========================================================================
    # UNIT: b1-tatarjaras (The Mongol Invasion 1241–42)
    # =========================================================================
    "b1-tatarjaras-01-tatarokerkezese.json": [
        "1241 telén rettenetes hír érkezett keletről. A mongol és tatár hadsereg gyorsan közeledett a magyar határok felé.",
        "A hírhozók kétségbeesve figyelmeztették a fiatal IV. Béla királyt a hatalmas külső fenyegetésre.",
        "A tatárok elől menekülő kun harcosok már korábban beléptek az országba, menedéket kérve a királytól.",
        "A király véres kardot küldött szét az országban, fegyverbe szólítva a népet, mert a tatárok bármelyik pillanatban betörhetnek.",
        "Végül a tatár sereg áttörte a hágókat, és a pusztító vihar megállíthatatlanul zúdult a védtelen Magyarországra."
    ],
    "b1-tatarjaras-02-muhicsata.json": [
        "1241. április 11-e éjszakáján a Sajó folyó partján állt fel a királyi hadsereg a mongol sereggel szemben.",
        "A magyar katonák védelmi céllal egy szűk szekérvárat hoztak létre, de ez súlyos taktikai hibának bizonyult.",
        "A fürge tatár lovasok éjjel átkeltek a hídon, és teljesen bekerítették a magyar tábort. Nyílzápor zúdult a harcosokra.",
        "A véres ütközet katasztrofális magyar vereséggel végződött. A hadsereg óriási veszteséget szenvedett, a főurak többsége elesett.",
        "IV. Béla király csak a legbátrabb vitézei segítségével tudott elmenekülni a csatatérről. Az ország védtelen maradt."
    ],
    "b1-tatarjaras-03-pusztulas.json": [
        "A muhi csata után soha nem látott pusztulás söpört végig a virágzó Magyar Királyság földjén.",
        "Számtalan falu és gazdag város felégett a támadásban, a gyönyörű templomok és paloták romba dőltek.",
        "A rémült lakosság a sűrű erdőkbe, a Dunakanyar hegyeibe és a védett mocsarakba menekült menedéket keresni.",
        "Amikor a Duna vize télen teljesen befagyott, a mongol lovasok átkeltek a jégen, és a termés is teljesen megsemmisült.",
        "A pusztítás nyomán rettenetes éhínség tizedelte a túlélőket, de a magyar nemzet élni akarása nem tört meg."
    ],
    "b1-tatarjaras-04-belaujjapitese.json": [
        "1242 tavaszán a mongol sereg hirtelen kivonult az országból, és IV. Béla király azonnal visszatért elpusztult hazájába.",
        "A király nem vesztegette az időt, hanem azonnal megkezdte a romokban heverő királyság hatalmas újjáépítését.",
        "Új idegen telepeseket hívott be a szomszédos országokból, és letelepítette őket a kihalt városokba és falvakba.",
        "Bőséges birtokokat adományozott azoknak a nemeseknek, akik kővárat emeltek a határok védelmére.",
        "Hősies és áldozatos munkájáért a magyarok IV. Bélát a második honalapító néven tisztelik máig."
    ],
    "b1-tatarjaras-05-kovarak.json": [
        "A tatárjárás után a király és a nemesség megértette: új katonai védelemre és stratégiára van szükség.",
        "A földből és fából épült régi várak helyett vastag falú, modern kővárak építésébe kezdtek a hegyeken.",
        "IV. Béla király a budai hegyen új fellegvárat és palotát emelt, amely minden ostromnak képes volt ellenállni.",
        "Országszerte több tucat megerősített erődítmény épült, amelyek biztonságos menedéket nyújtottak a lakosságnak.",
        "Amikor a tatárok évtizedekkel később újra támadtak, a sziklaszilárd kővárak sikeresen megvédték a hazát."
    ],
    "b1-tatarjaras.json": [
        "1241-ben a mongol hordák betörtek a virágzó Magyar Királyságba. A tragikus muhi csata után az egész ország a pusztulás szélére sodródott.",
        "Falvak és városok váltak hamuvá, miközben a nép a mocsarakban és hegyekben keresett menedéket a rettegett tatárok elől.",
        "Amikor a tatárok 1242-ben elhagyták a vidéket, IV. Béla király hozzálátott a felperzselt ország újjáépítéséhez.",
        "Kővárak építését rendelte el, behívta a telepeseket és felvirágoztatta a városokat. Ekkor épült fel a Budai Vár és Visegrád fellegvára.",
        "Hatalmas művéért IV. Bélát a magyarok a második honalapítóként tisztelik. A kővárak bástyái máig hirdetik a nemzet túlélését és erejét."
    ]
}

def update_stories():
    updated = 0
    for filename, paragraph_texts in STORIES.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        new_paragraphs = [{"type": "narration", "text": text} for text in paragraph_texts]
        data["paragraphs"] = new_paragraphs

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        updated += 1

    print(f"Total stories successfully re-authored: {updated}/36")

if __name__ == "__main__":
    update_stories()
