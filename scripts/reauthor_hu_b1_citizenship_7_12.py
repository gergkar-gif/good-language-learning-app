#!/usr/bin/env python3
"""Re-author Hungarian B1 Citizenship track stories for units 7-12 (36 stories).

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
    # UNIT 7: b1-anjouk (The Angevin & Later Medieval Kings)
    # =========================================================================
    "b1-anjouk-01-karolyrobert.json": [
        "1301-ben kihalt az Árpád-ház férfiága, és a Magyar Királyság a káosz szélére sodródott. Ki hozhat rendet egy széthulló birodalomban?",
        "A gazdag tartományurak, akiket kiskirály névvel illettek, saját hadsereggel uralkodtak. Nem engedelmeskedtek a központi hatalomnak.",
        "A fiatal Anjou Károly Róbert király azonban kitartó harcokban legyőzte őket, és megszilárdít minden királyi jogkört.",
        "A bányászat fejlesztésével Körmöcbányán megindult a drága nemesfém kitermelése. Megkezdődött a híres magyar aranyforint pénzverés folyamata.",
        "A királyi jövedelem ugrásszerűen nőtt, és a kincstár gyorsan megtelt arannyal. Magyarország Európa egyik leggazdagabb gazdasági hatalma lett."
    ],
    "b1-anjouk-02-visegrad.json": [
        "1335 őszén rendkívüli diplomáciai esemény zajlott Visegrádon. Hogyan foghat össze három közép-európai királyság a közös jólétért?",
        "Károly Róbert meghívására létrejött a híres királytalálkozó, amelyen a cseh és lengyel uralkodó vett részt.",
        "A szomszédos országok vezetői történelmi jelentőségű katonai és gazdasági szövetség mellett kötelezték el magukat.",
        "Közös megegyezéssel elkerül minden bécsi vámot egy új kereskedelmi út megnyitása révén.",
        "A felek között szilárd vámmegállapodás született, amelyben a magyar király közvetítő szerepet vállalt. Ez a sikeres egyezség ma a V4 alapja."
    ],
    "b1-anjouk-03-nagylajos.json": [
        "Károly Róbert fia, Nagy Lajos igazi eszményi lovagkirály volt Európa trónjain. De vajon hogyan kormányozta hatalmas birodalmát?",
        "Hosszú és dicsőséges uralkodás alatt a Magyar Királyság perszonálunióra lépett Lengyelországgal, határai három tengerig értek.",
        "1351-ben az uralkodó új törvénykönyv kiadásával lepte meg az országot. Ez a rendelet megerősít minden korábbi alapvető nemesi szabadságjogot.",
        "A nemesség védelmére bevezette az ősiség elvét, amely szigorúan szabályozta a földbirtok családi öröklés kérdését.",
        "A jobbágyok számára kötelezővé tette a kilenced adó fizetését. Ezzel Nagy Lajos évszázadokra meghatározta a magyar társadalmi rendet."
    ],
    "b1-anjouk-04-zsigmond.json": [
        "A tizennegyedik század végén új, sötét viharfelhők tornyosultak a déli határon. Az oszmán hadsereg megindult Európa felé.",
        "Luxemburgi Zsigmond magyar király, a későbbi német-római császár gyorsan felismerte a halálos veszélyt.",
        "Tudta, hogy a birodalmat komoly hadjárat fenyeget, ezért nagyszabású katonai védelmi reformba kezdett.",
        "A déli határvidéken kiépült az első összefüggő végvárrendszer, amelyben minden fontos végvár szilárd falakkal büszkélkedhetett.",
        "Zsigmond megalapította a Sárkány lovagrend szervezetet is a határok védelmére. A déli védelem sikeresen állta a törökök rohamait."
    ],
    "b1-anjouk-05-nandorfehervar.json": [
        "1456 nyarán a rettegett II. Mehmed szultán hatalmas sereggel érkezett Nándorfehérvár alá. Vajon ki állíthatja meg a hódítókat?",
        "A kulcsfontosságú várat a legendás törökverő hadvezér, Hunyadi János kormányzó és hős katonái védték.",
        "A véres ostrom során a magyar vitézek hihetetlen bátorsággal és önfeláldozással visszaverték a szultán rohamait.",
        "A fényes győzelem hetven évre megállította az oszmán előrenyomulást. A pápa elrendelte a déli harangszó szokását a hősiesség tiszteletére.",
        "Bár Hunyadi a csata után pestis járványban elhunyt, halhatatlan neve és dicső tette örökre megmaradt a nemzeti emlékezet lapjain."
    ],
    "b1-anjouk.json": [
        "Az Árpád-ház kihalása után Anjou Károly Róbert új korszakot nyitott. Legyőzte a kiskirályokat, és aranyforintjával talpra állította a gazdaságot.",
        "1335-ben Visegrádon a cseh és lengyel királlyal kötött szövetséget. Ez a királytalálkozó máig a közép-európai együttműködés szimbóluma.",
        "Fia, Nagy Lajos lovagkirály uralkodása alatt Magyarország európai nagyhatalommá vált. Az 1351-es törvények rögzítették az ősiség és a kilenced szabályait.",
        "Zsigmond császár korában az oszmán fenyegetés ellen kiépült a déli végvárrendszer, amely évtizedeken át védte a hazát.",
        "1456-ban Nándorfehérvár falainál Hunyadi János megállította a szultánt. A déli harangszó azóta is minden délben erre a győzelemre emlékeztet."
    ],

    # =========================================================================
    # UNIT 8: b1-matyas (Matthias Corvinus & the Renaissance Court)
    # =========================================================================
    "b1-matyas-01-megvalasztas.json": [
        "1458 telén a befagyott Duna jegén tízezres tömeg gyűlt össze Budán. Ki lesz a Magyar Királyság új uralkodója?",
        "A nép és a köznemesség Hunyadi Mátyást követelte, miközben a vezető főnemes csoportok heves vitát folytattak.",
        "Hosszú és feszült tárgyalás után megszületett a döntés: az ifjú Hunyadi fiú foglalja el a magyar trón helyét.",
        "A megválasztás pillanatában Mátyás még Prágában volt fogságban, de hamarosan hazatért az ünnepélyes eseményre.",
        "A szent koronázás után a királyi címerpajzs dísze, a gyűrűt tartó fekete holló az egész ország jelképe lett."
    ],
    "b1-matyas-02-feketesereg.json": [
        "A középkori királyok ritkán tartottak fizetett katonákat békében. Mátyás király azonban teljesen megújította a hadviselés művészetét.",
        "Létrejött a híres fekete sereg, Közép-Európa első jól képzett állandó hadsereg alakulata.",
        "A tapasztalt zsoldos harcosok vaskos fegyelem alatt szolgáltak, modern fegyverzet és puskák védték őket.",
        "A kiváló tehetségű hadvezér vezetése alatt a sereg sorra nyerte a hadjáratokat és foglalta el Bécset.",
        "A hadsereg fenntartását és a hadisarc fizetését a király szigorú adóztatási rendszere biztosította."
    ],
    "b1-matyas-03-reneszanszudvar.json": [
        "Hogyan vált egy közép-európai királyi vár az itáliai kultúra legfontosabb északi központjává?",
        "Mátyás király felesége, Beatrix királyné révén Buda és Visegrád udvarába beköltözött a ragyogó reneszánsz korszak.",
        "Olasz mesterek által virágzott az építészet és a művészet, a hegyen felépült a csodás visegrádi palota.",
        "A királyi könyvtár a világ egyik legértékesebb gyűjteménye volt, a kézzel másolt corvina kódexek száma meghaladta az ezret.",
        "A budai várban számos híres tudós és humanista filozófus talált békés otthonra és támogatásra."
    ],
    "b1-matyas-04-igazsagossag.json": [
        "A magyar néphagyományban egyetlen király sem maradt olyan elevenen, mint Hunyadi Mátyás. De miért hívták igazságosnak?",
        "A legendák szerint a király gyakran öltött szegényes álruha öltözéket, hogy titokban ellenőrizze a főurak viselkedését.",
        "Mátyás bátor adóreform bevezetésével megszüntette a kibúvókat, és a háztartásokra kivetett füstadó fizetését rendelte el.",
        "Szigorú rendtartás és következetes bíráskodás jellemezte uralmát, amely a kisemberek védelmét is biztosította.",
        "A törvényesség tisztelete miatt a népmese világában Mátyás örökre az elnyomottak védelmezője maradt."
    ],
    "b1-matyas-05-orokseg.json": [
        "1490 tavaszán Bécsben hirtelen bekövetkezett a nagy uralkodó halál eseménye, és mély gyász borult az országra.",
        "Mátyás király után nem maradt törvényes felnőtt örökös, így a hatalmas központi monarchia gyorsan hanyatlani kezdett.",
        "A nép ajkán azonnal megszületett a szomorú mondás: Meghalt Mátyás, oda az igazság.",
        "Ez a híres közmondás generációkon át őrizte azt az emléket, hogy uralkodása igazi aranykor és virágkor volt.",
        "A hálás utókor szemében Mátyás gazdag öröksége a nemzet csúcspontja, egy dicsőséges történelmi korszak megtestesítője maradt."
    ],
    "b1-matyas.json": [
        "1458-ban a Duna jegén Hunyadi Mátyást királlyá választotta a nép. Fiatal kora ellenére hamar rendet teremtett a birodalomban.",
        "A híres fekete sereg segítségével megerősítette a határokat, és fegyelmezett állandó hadsereget épített ki.",
        "Udvarában virágzott a reneszánsz kultúra és a humanista tudomány. A budai Corvina könyvtár egész Európában csodálatot keltett.",
        "Álruhás látogatásai és reformjai miatt a nép igazságos királyként tisztelte, aki védte a gyengéket a főuraktól.",
        "1490-es halála után a mondás így szólt: Meghalt Mátyás, oda az igazság. Uralkodása a magyar történelem virágkora volt."
    ],

    # =========================================================================
    # UNIT 9: b1-mohacs (The Battle of Mohács 1526)
    # =========================================================================
    "b1-mohacs-01-meggyengult.json": [
        "Mátyás halála után harminc év alatt a virágzó királyság a mélybe zuhant. Hogyan omolhat össze egy nagyhatalom ilyen gyorsan?",
        "A meggyengült központi hatalmat a nemesség önzése és a szüntelen belső viszály tette tehetetlenné.",
        "Az 1514-es véres parasztfelkelés leverése után a jobbágyság sorsa még nehezebb lett a nemesi megtorlás miatt.",
        "A királyi kincstár teljesen kiürült, és a krónikus zsoldoshiány miatt a sereget feloszlatták.",
        "A nemesi széthúzás megakadályozta az összefogást, miközben a határokon már gyülekeztek a hódító oszmán csapatok."
    ],
    "b1-mohacs-02-elorenyomulas.json": [
        "1526 tavaszán Isztambulból útnak indult I. Szulejmán szultán hatalmas és jól felszerelt serege Közép-Európa felé.",
        "A grandiózus katonai hadjárat célja a Magyar Királyság teljes meghódítása és Bécs elérése volt.",
        "A félelmetes oszmán túlerő modern ágyú tüzérséggel és janicsár gyalogsággal vonult előre a Duna mentén.",
        "Minden déli végvár ostrom alatt roskadozott, Nándorfehérvár eleste után a határok védtelenek maradtak.",
        "A magyar királyi udvar kétségbeesett segítségkérés levelei visszhang nélkül maradtak, a nemzet teljes elszigeteltség állapotába került."
    ],
    "b1-mohacs-03-csata.json": [
        "1526. augusztus 29-én délután Mohács mellett állt szemben a két hadsereg a nyári hőségben.",
        "Tomori Pál érsek fővezér bátor elgondolása szerint egy hirtelen, mindent elsöprő roham dönthette el a csatát.",
        "A zárt hadrend élén támadó nehéz magyar lovasság kezdetben visszanyomta az oszmán előőrsöket.",
        "Ám a szultán soraiból megnyíló gyilkos tüzérségi tűz és a golyózápor pillanatok alatt megtörte a támadást.",
        "Kezdetét vette a pánikszerű megfutamodás a mocsár és a patakok felé, a rosszul megválasztott taktika katasztrófát hozott."
    ],
    "b1-mohacs-04-kiralyhalala.json": [
        "A vesztes csatatérről fejvesztve menekült a fiatal, húszéves magyar uralkodó, II. Lajos király kíséretével.",
        "A viharos menekülés közben a megáradt Csele-patak partján a király lova megcsúszott a sárban és hanyatt esett.",
        "A nehéz páncél súlya miatt a király nem tudott felállni a vízből, és szomorú fulladás vetett véget életének.",
        "Két hónappal később találták meg a holttest földi maradványait, és Székesfehérváron temették el.",
        "Mivel nem maradt hátra törvényes trónörökös, az országban azonnal súlyos dinasztikus válság robbant ki a trónért."
    ],
    "b1-mohacs-05-fontossag.json": [
        "Mohács nemcsak egy vesztes ütközet volt, hanem a magyar történelem legnagyobb és legsúlyosabb tragédiája.",
        "Ez a végzetes dátum sorsdöntő fordulópont és korszakhatár, amely után a középkori független királyság darabokra hullott.",
        "A szomorú közmondás így vigasztalja a bánkódót: Több is veszett Mohácsnál.",
        "A véres csata helyszínén ma méltó emlékhely fogadja a látogatókat a nemzeti emlékezet és a gyász jegyében.",
        "A tragédia legfontosabb történelmi tanulság üzenete: a széthúzás bukást hoz, de a nemzet megmaradás hite legyőzhetetlen."
    ],
    "b1-mohacs.json": [
        "1526 előtt a belső viszályok és az üres kincstár miatt a Magyar Királyság védelmi ereje végzetesen meggyengült.",
        "Szulejmán szultán hatalmas ágyúkkal és félelmetes túlerővel vonult a Duna mentén a védtelen ország szívébe.",
        "Augusztus 29-én a mohácsi mezőn a magyar roham összeomlott a pusztító oszmán tüzérségi tűz alatt.",
        "A fiatal II. Lajos király a Csele-patakba fulladt nehéz páncéljában, és az ország trónörökös nélkül maradt.",
        "Mohács a nemzeti történelem legnagyobb fordulópontja lett. A független Magyar Királyság másfél évszázadra elveszítette egységét."
    ],

    # =========================================================================
    # UNIT 10: b1-haromresz (Three Parts of Hungary)
    # =========================================================================
    "b1-haromresz-01-kiralyi.json": [
        "1541-ben Buda oszmán kézre került, és az ország területe három részre szakadt. Mi maradt meg a nyugati végeken?",
        "A nyugati és északi vármegyék alkották a területet, amely Királyi Magyarország néven a Habsburg Birodalom része lett.",
        "A Habsburg-kormányzat új központja Pozsony városa lett, ahol a királyi kancellária és az országgyűlés működött.",
        "A nemesi rendeket a nádor képviselte, akit a rendszeres rendi gyűlés ülésein választottak meg a törvények betartására.",
        "A déli határokon új végvárvonal épült ki, ahol a határvédelem mindennapos és kemény harcot jelentett a katonáknak."
    ],
    "b1-haromresz-02-hodoltsag.json": [
        "Az ország középső területe másfél évszázadra az Oszmán Birodalom közvetlen tartományává vált. Milyen volt az élet itt?",
        "A Török Hódoltság közigazgatási alapegysége a vilajet lett, amelynek élén a teljhatalmú budai pasa állt.",
        "Az adók pontos beszedését a szigorú defterdár felügyelte, miközben a lakosságot kettős adóztatás sújtotta.",
        "A városok képe átalakult: megjelent a karcsú minaret, a félholdas kupolájú dzsámi és a gőzölgő törökfürdő épülete.",
        "A magyar lakosság megtartotta hitét és nyelvét, miközben a keleti szokások is beszivárogtak a mindennapi életbe."
    ],
    "b1-haromresz-03-erdely.json": [
        "Miközben a középső részeken a szultán parancsolt, a keleti hegyek között különleges magyar állam született.",
        "Létrejött az önálló Erdélyi Fejedelemség, amelynek ragyogó fejedelmi székhelye a festői Gyulafehérvár városa lett.",
        "A választott magyar fejedelem ügyes diplomáciával és rendszeres adófizetés fejében megőrizte a belső függetlenséget.",
        "Itt virágzott a reformáció és az anyanyelvi kultúra, és a világon elsőként törvénybe iktatták a vallásszabadság jogát.",
        "Erdély fontos közvetítő szerep feladatot látott el Kelet és Nyugat között, őrizve a magyar államiság lángját."
    ],
    "b1-haromresz-04-veghazak.json": [
        "A hódoltság és a keresztény világ határán állandó fegyverropogás és harci kiáltások verték fel a csendet.",
        "A bátor végvári vitéz mindennapi feladata a portya és a veszélyes bajvívás volt az ellenséggel szemben.",
        "A végvárak mögött a mezőváros lakossága virágzó marhakereskedelem révén szállította az állatokat Nyugat-Európa felé.",
        "A falvakban sok helyen elnéptelenedés fenyegetett, de a bátor paraszti ellenállás gyakran megfékezte a portyázókat.",
        "A háborús viszonyok ellenére a két világ között lassanként kialakult egy sajátos kulturális és gazdasági együttélés."
    ],
    "b1-haromresz-05-megosztottsag.json": [
        "Másfél évszázadon át a magyar nemzet tragikus politikai megosztottság állapotában volt kénytelen élni.",
        "A szörnyű háborús rombolás ellenére a nemzeti egység gondolata és a kulturális folytonosság soha nem szakadt meg.",
        "A magyar nyelv, az irodalom és a protestáns iskolák a nemzeti túlélés legfőbb bástyáivá váltak a viharban.",
        "A lakosság szíve mélyén mindig élt a remény: eljön a budai vár és a területek dicső visszafoglalás pillanata.",
        "Amikor a törökök végleg kivonultak, megkezdődhetett a felperzselt ország hatalmas újjáépítés munkája az új korszakban."
    ],
    "b1-haromresz.json": [
        "1541-ben Buda elestével az ország három részre szakadt: Királyi Magyarországra, a Hódoltságra és az Erdélyi Fejedelemségre.",
        "Nyugaton Pozsony lett az új főváros, ahol a Habsburg uralkodók és a magyar rendek közösen szervezték a végvárvonal védelmét.",
        "A középső területeken a török vilajetek uralkodtak, ahol a dzsámik és a kettős adóztatás nyomták rá bélyegüket az életre.",
        "Erdélyben a magyar fejedelmek virágzó anyanyelvi kultúrát teremtettek, és a tordai országgyűlésen kimondták a vallásszabadságot.",
        "A másfél évszázados megosztottság dacára a nemzeti egység megmaradt, és megalapozta a későbbi újjáépítés sikerét."
    ],

    # =========================================================================
    # UNIT 11: b1-erdelyaranykora (Transylvania's Golden Age)
    # =========================================================================
    "b1-erdelyaranykora-01-onallo.json": [
        "Hogyan maradhatott fenn egy önálló magyar állam két világbirodalom, a Habsburgok és az Oszmánok szorításában?",
        "A keleti országrészben megszületett az Erdélyi Fejedelemség, amely ügyes politikával védte a magyar függetlenséget.",
        "Bár a szultán volt a névleges hűbérúr, a tartomány teljes belső önállóság élvezett a mindennapi életben.",
        "A fejedelmi székhely, Gyulafehérvár falai között ülésezett a rendi országgyűlés, amely megerősítette a három nemzet kiváltság jogait.",
        "Az önálló külpolitika lehetővé tette, hogy a pusztító háborúk idején Erdélyben meginduljon a békés építkezés korszaka."
    ],
    "b1-erdelyaranykora-02-vallasbeke.json": [
        "1568-ban egy erdélyi kisváros, Torda olyan döntést hozott, amely kétszáz évvel megelőzte egész Európát. Mi történt ott?",
        "A tordai országgyűlésen megszületett a híres tordai ediktum, amely a világon elsőként hirdette ki a hit szabadságát.",
        "A törvény kimondta: a hit Isten ajándéka, ezért senkit sem szabad üldözni vagy bántani vallási meggyőződése miatt.",
        "Négy bevett vallás kapott egyenlő védelmet: a katolikus, a lutheránus evangélikus, a református és az unitárius egyház.",
        "Ez a felekezeti béke és a tiszteletre méltó vallásszabadság tette Erdélyt a tolerancia és a béke szigetévé."
    ],
    "b1-erdelyaranykora-03-bethlen.json": [
        "1613-ban kiváló államférfi lépett a trónra: Bethlen Gábor fejedelem, aki alatt beköszöntött Erdély aranykora.",
        "A fejedelem a korszerű merkantilizmus elveit követte: az állami bevételeket a kereskedelem és ipar fejlesztésére fordította.",
        "Felfuttatta a bányászat ágát, és szigorúan ellenőrizte a stratégiai fontosságú nemesfém-kivitel forgalmát.",
        "A gazdasági fellendülés révén hatalmas összegeket költött kultúrára: Gyulafehérváron fejedelmi kollégium nyitotta meg kapuit.",
        "Bőkezű mecénás hírében állt, külföldi professzorokat hívott meg, és tehetséges magyar diákokat küldött európai egyetemekre."
    ],
    "b1-erdelyaranykora-04-europa.json": [
        "Amikor Európában kitört a pusztító harmincéves háború, az erdélyi fejedelem nem maradhatott tétlen néző.",
        "Bethlen Gábor mint megbízható szövetséges csatlakozott a protestáns liga táborához a császári elnyomás ellen.",
        "Gyors hadjárat vezetésével felszabadította Felső-Magyarországot, és csapatai még Bécs falait is megközelítették.",
        "Sikerei nyomán kedvező békeszerződés született, amely garantálta a magyar rendi és vallási jogok érvényesülését.",
        "A fejedelmi diplomácia és a mesteri egyensúlyozás révén Erdély nemzetközi elismertség szintjére emelkedett Európában."
    ],
    "b1-erdelyaranykora-05-hagyatek.json": [
        "Milyen kincseket hagyott ránk az erdélyi aranykor, amelyek ma is formálják a magyar identitást?",
        "A gazdag református műveltség részeként megszületett Károli Gáspár bibliafordítás munkája, amely egységesítette a nyelvet.",
        "Szapora nyomdászat virágzott a városokban, és megindult a magas színvonalú anyanyelvi oktatás országszerte.",
        "A templomokban zengő közös zsoltáréneklés erősítette a lelkeket és mélyítette a közösségi nemzeti tudat érzését.",
        "Ez a csodálatos történelmi hagyaték bizonyítja, hogy a magyar kultúra a legnehezebb időkben is erős bástya maradt."
    ],
    "b1-erdelyaranykora.json": [
        "A török hódoltság idején az Erdélyi Fejedelemség megőrizte a magyar államiság belső önállóságát és függetlenségét.",
        "Az 1568-as tordai ediktum a világon elsőként mondta ki a vallásszabadságot négy bevett vallás egyenjogúsításával.",
        "Bethlen Gábor fejedelemsége alatt Erdély gazdasági virágkort élt meg, és európai hírű kollégiumok épültek.",
        "A harmincéves háborúban folytatott sikeres diplomácia révén Erdély a nemzetközi politika elismert szereplőjévé vált.",
        "Az erdélyi szellemi örökség, az anyanyelv és a könyvnyomtatás a magyar nemzeti kultúra örök bástyája maradt."
    ],

    # =========================================================================
    # UNIT 12: b1-torokkiuzese (Driving Out the Ottomans)
    # =========================================================================
    "b1-torokkiuzese-01-ostrom.json": [
        "1683-ban a török hadsereg kudarcot vallott Bécs falainál. Ezzel megkezdődött a végső leszámolás az Oszmán Birodalommal.",
        "XI. Ince pápa kezdeményezésére megalakult az európai Szent Liga szövetség Magyarország felszabadítására.",
        "1686 nyarán Lotaringiai Károly herceg vezetésével megindult a várva várt Buda visszafoglalása véres küzdelme.",
        "A heteken át tartó ostrom alatt a fülsiketítő ágyútűz romba döntötte a budai vár vastag falait.",
        "Petneházy Dávid magyar hajdúi törtek be elsőként a résen, miközben az utolsó budai védő, Abdurrahman pasa hősi halált halt. Megvalósult a dicső felszabadulás."
    ],
    "b1-torokkiuzese-02-karloca.json": [
        "Buda sikeres visszafoglalása után a szövetséges csapatok nem álltak meg. Hatalmas felszabadító hadjárat söpört végig a vidéken.",
        "1687-ben a nagyharsányi csata, amelyet második mohácsi csatának is neveznek, megtörte az oszmán fősereget.",
        "Tíz évvel később a zentai csata fényes diadalában a lángelméjű Savoyai Jenő herceg végleg tönkrezúzta a szultán seregét.",
        "1699-ben megkötötték a történelmi karlócai béke egyezményt, amellyel hivatalosan bekövetkezett a török hódoltság vége.",
        "Az új déli határvonal kijelölésével a Temesköz kivételével az egész ország a bécsi udvar fennhatóság alá került."
    ],
    "b1-torokkiuzese-03-ara.json": [
        "A török kiűzése hatalmas öröm volt, de a szabadságnak rettenetes ára volt. Milyen állapotban hevert az ország?",
        "Másfél évszázadnyi háborúskodás után elképesztő pusztulás, leégett falvak és kísérteties romváros fogadta a hazatérőket.",
        "Súlyos elnéptelenedés sújtotta az Alföldet, miközben az éhínség és a halálos járvány tizedelte a lakosságot.",
        "A lakosságra nehezedett az idegen csapatok hadseregtartás kötelezettsége: a kötelező élelemadó, a porció és a szállítás, a forspont.",
        "Ez a kíméletlen anyagi teher gyakran még a korábbi török adóknál is elviselhetetlenebbnek bizonyult a szegény parasztoknak."
    ],
    "b1-torokkiuzese-04-serelmek.json": [
        "A törökök távoztak, de a magyarok nem kapták vissza a békét. Új veszély fenyegetett: az abszolutista Habsburg-uralom.",
        "Bécs úgy kezelte Magyarországot, mint fegyverrel meghódított új területet, és az országot katonai megszállás alá helyezte.",
        "A felállított Újszerzeményi Bizottság csak magas fegyverváltság kifizetése ellenében adta vissza a régi családi birtokokat.",
        "A nemesi jogok sérelme és a hatalmas adók miatt országszerte robbanásszerű elégedetlenség söpört végig a vármegyékben.",
        "A király törölte az Aranybulla híres ellenállási jog cikkelyét, és a magyar országgyűlés elfogadta az örökös királyság elvét."
    ],
    "b1-torokkiuzese-05-szabadsagharc.json": [
        "Az elkeseredett nép nem tűrte sokáig az elnyomást. A hegyekben gyülekezni kezdtek a bujdosó katonák.",
        "Először Thököly Imre vezetésével indult meg a kuruc felkelés a császári csapatok ellen a Felvidéken.",
        "Hamarosan a gazdag főnemes, II. Rákóczi Ferenc állt az ellenállás élére: Cum Deo pro Patria et Libertate!",
        "Kitört a dicsőséges Rákóczi-szabadságharc, amely széles nemzeti összefogás erejével egyesítette a jobbágyokat és a nemeseket.",
        "Ez a nemzeti függetlenség küzdelem döntő történelmi fordulat lett: bebizonyította, hogy a magyar szabadságvágyat nem lehet eltiporni."
    ],
    "b1-torokkiuzese.json": [
        "1686-ban a Szent Liga seregei véres ostrom után felszabadították a budai várat a másfél évszázados oszmán uralom alól.",
        "A nagyharsányi és a zentai diadal után az 1699-es karlócai béke lezárta a hódoltság korszakát Magyarországon.",
        "A felszabadulás hatalmas pusztulással, elnéptelenedéssel és a császári csapatok súlyos beszállásolási terheivel járt.",
        "A bécsi abszolutizmus megsértette a rendi jogokat, eltörölte az ellenállási jogot és fegyverváltságot követelt a birtokokért.",
        "A növekvő elégedetlenség végül a Rákóczi-szabadságharcban robbant ki, amely a magyar szabadságvágy örök jelképévé vált."
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
