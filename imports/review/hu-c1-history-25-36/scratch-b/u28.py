import sys; sys.path.insert(0,"/home/user/parlour-read-b/.scratch")
from lib import *
V="c1-railway-decay-vocab"; P="c1-kozlekedespolitika"
UT="Railways, Motorways and Public Transport Policy, 2010–2026"
def t(s): return {"type":"text","title":s[0],"content":s[1]}
def tab(rows): return {"type":"table","title":"Patterns in Context","rows":rows}
L={}
# ---------------- 01
L["01"]=dict(
 title="MÁV, Rolling Stock and Delays, 2010–2024",
 intro_title="Unit 28: "+UT,
 intro=["This unit follows Hungarian transport policy from 2010 to the spring of 2026 as a finished period. Five accounts cover the state railway company MÁV, the branch lines, the motorway concession, the Budapest–Belgrade railway and the fare passes.",
        "Each judgement in the texts has a source: the critics, the government's reasoning, an expert. Where a matter was disputed, the other side is named too."],
 grammar_title="Naming the Source of a Judgement",
 goal=["I can say who made a judgement about the railway and name the other side.",
       "I can describe the condition of the tracks and vehicles of the state railway in the past tense, with years.",
       "I can use the words of railway operation and delays (*lassújel*, *járműpark*, *késés*)."],
 grammar=[
  t(("Source and Contrast","You know *szerint* and *állítólag* from B1 Unit 13, and *viszont* and *azonban* from B1 Unit 11. In a text about a disputed period every judgement gets its source, and the other side stands beside it: `a bírálók szerint …, a kormány indoklása szerint viszont …`. A source can be a group (`a bírálók`, `a szakértők`), an institution (`a kormány indoklása`) or a document.")),
  t(("Past Narration with Years","The narrator states only what happened and when: `2023-ban a minisztérium több mellékvonalon felfüggesztette a személyforgalmat.` The view on it belongs to someone: `A bírálók szerint a pályák karbantartására kevés pénz jutott.`")),
  tab([["A bírálók szerint a pályák karbantartására kevés pénz jutott.","According to the critics, little money went to track maintenance."],
       ["A kormány indoklása szerint az állam több fővonalat is felújított.","According to the government's reasoning, the state also renovated several main lines."],
       ["A szakértők szerint a lassújelek miatt megszaporodtak a késések.","According to the experts, delays became more frequent because of the speed restrictions."]])],
 vocab=[("lassújel","temporary speed restriction on a section of track","noun"),("járműpark","fleet of vehicles (rolling stock)","noun"),("menetrendszerűség","punctuality, running to the timetable","noun"),("pályaromlás","deterioration of the track","noun"),("karbantartás","maintenance","noun"),("késés","delay","noun"),("fővonal","main line","noun"),("felújítás","renovation","noun"),("ideiglenes","temporary","adjective")],
 story=dict(file="c1-kozlekedespolitika-01-mav-valsag-lassujelek",title="A MÁV és a vasúti járműpark, 2010–2024",skill="evidentials",
  summary="A MÁV-csoport a 2010 és 2024 közötti években: a pályák és a járművek állapotáról, a késésekről és a lassújelekről szóló vita, a bírálók és a kormány álláspontja szerint.",
  text=["2010 és 2024 között a magyar vasúti személyszállítás nagy részét az állami tulajdonú MÁV-csoport végezte, amelynek személyforgalmi társasága a MÁV-START volt. A vasúti pályák és járművek állapotáról ebben az időszakban folyamatos vita zajlott.",
        "A bírálók szerint a pályák karbantartására és a járművek cseréjére kevés pénz jutott. A szakértők azt mondták, hogy emiatt sok szakaszon lassújelet kellett bevezetni: ilyenkor a pálya állapota miatt a vonatoknak lassabban kellett haladniuk, és a késések megszaporodtak.",
        "A kormány indoklása szerint viszont az állam uniós támogatással több fővonalat is felújított, és a fejlesztések folytatódtak. A nyári hőségben az utasok gyakran panaszkodtak azokra a kocsikra, amelyekben nem működött a légkondicionáló.",
        "A vita fő kérdése az volt, hogy a vasút nehézségeit a pénzhiány vagy a szervezet működése okozta-e. Erről a két oldal eltérően vélekedett, és a kérdés megítélése vitatott volt."]),
 challenge=dict(title="Communicative Challenge: Who Said It",scenario="You have read about the state railway company MÁV in the years 2010–2024. A friend asks what the critics said about the tracks.",prompt="Tell your friend what the critics said about track maintenance and what the government's reasoning added.",cues=["Name the critics as the source and say what they said about maintenance","Name the government's reasoning as the other source and say what it added"],target="A bírálók szerint a pályák karbantartására kevés pénz jutott. A kormány indoklása szerint viszont az állam több fővonalat is felújított.",english="According to the critics, little money went to track maintenance. According to the government's reasoning, however, the state also renovated several main lines."),
 items=[
  mc(P+"-01-introduce-1","vocabulary","introduce","Mit jelent a *lassújel* a vasúti közlekedésben?",["A pálya állapota miatt elrendelt ideiglenes sebességkorlátozást.","A vonat érkezését jelző hangszórós bemondást az állomáson.","A mozdonyvezető pihenőidejét szabályozó menetrendi előírást."],V,1),
  fb(P+"-01-controlled-2","controlled","A bírálók _____ a pályák karbantartására kevés pénz jutott.","szerint","According to the critics, little money went to track maintenance.","evidentials"),
  match(P+"-01-controlled-3","controlled",[("lassújel","ideiglenes sebességkorlátozás a pálya állapota miatt"),("járműpark","egy vállalat összes vasúti járműve"),("menetrendszerűség","az, hogy a vonatok a menetrend szerint közlekednek"),("pályaromlás","a vágány műszaki állapotának romlása")],V),
  fb(P+"-01-practice-4","practice","A bírálók szerint megszaporodtak a késések; a kormány indoklása szerint _____ a fővonalak felújítása folytatódott.",["viszont","azonban"],"According to the critics delays became more frequent; according to the government's reasoning, however, the renovation of the main lines continued.","adversative-contrast","but, on the other hand"),
  sb(P+"-01-practice-5","practice","A szakértők szerint a lassújelek miatt megszaporodtak a késések.","According to the experts, delays became more frequent because of the speed restrictions.","evidentials"),
  dlg(P+"-01-dialogue-6",[("Tanár","Mit mondtak a bírálók a pályák állapotáról?"),("Diák","A bírálók _____ a karbantartásra kevés pénz jutott."),("Tanár","És a kormány indoklása?")],["szerint","szerinte","szerintem"],"evidentials",2),
  wr(P+"-01-production-7","production","Write one or two sentences in Hungarian about what the experts said about delays, naming the source.","A szakértők szerint a lassújelek miatt megszaporodtak a késések, és a menetrendszerűség romlott.",V),
  mc(P+"-01-check-8","grammar","check","Melyik mondat tulajdonítja a véleményt valakinek?",["A bírálók szerint a pályákra kevés pénz jutott.","A pályákra kevés pénz jutott, ez a helyzet magától értetődő volt.","A pályákra egyértelműen kevés pénz jutott a MÁV-nak."],"evidentials",0),
 ])
# ---------------- 02
L["02"]=dict(
 title="Branch Line Suspensions and Rail-Replacement Buses",
 intro_title="Unit 28: "+UT,
 intro=["This lesson covers the branch lines, where passenger service was suspended and buses ran instead.","The government's reasoning and the critics' objections are given side by side."],
 grammar_title="Obligation and Compulsion in the Past",
 goal=["I can say what a company or an authority was obliged to do or forced to do, in the past tense.",
       "I can describe the suspension of branch line service and the objections to it, with the source of each view.",
       "I can use the words of local public transport (*mellékvonal*, *pótlóbusz*, *elszigetelődés*)."],
 grammar=[
  t(("Obliged and Forced","You know *köteles* and *kénytelen* from B1 Unit 10. In a past account they take *volt*: `a társaság köteles volt üzemeltetni a megrendelt vonatokat`, `a minisztérium kénytelen volt felfüggeszteni a forgalmat`. *Köteles* names a duty laid down by a rule or contract; *kénytelen* names a lack of choice.")),
  t(("Whose Reasoning","A *kénytelen volt* sentence gives the reasoning of one side, so it needs its source: `a kormány indoklása szerint … kénytelen volt …`. With a plural subject the adjective agrees: `a lakosok kénytelenek voltak`.")),
  tab([["A társaság köteles volt üzemeltetni a megrendelt vonatokat.","The company was obliged to operate the trains that had been ordered."],
       ["A kormány indoklása szerint a minisztérium kénytelen volt felfüggeszteni a forgalmat.","According to the government's reasoning, the ministry was forced to suspend the service."],
       ["Az önkormányzatok szerint a lakosok kénytelenek voltak buszra szállni.","According to the local governments, the residents were forced to take a bus."]])],
 vocab=[("mellékvonal","branch line (a railway line of secondary importance)","noun"),("forgalomszüneteltetés","suspension of service","noun"),("pótlóbusz","rail-replacement bus","noun"),("közszolgáltatási szerződés","public service contract","expression"),("elszigetelődés","isolation","noun"),("önkormányzat","local government","noun"),("felfüggesztés","suspension","noun")],
 story=dict(file="c1-kozlekedespolitika-02-mellekvonalak-felszamolasa",title="A mellékvonalak és a pótlóbuszok",skill="formal-obligation",
  summary="A vasúti mellékvonalak vitatott helyzete és a személyforgalom felfüggesztése 2023-ban, a kormány indoklása és a bírálók kifogásai szerint.",
  text=["A vasúti mellékvonalak jövője már 2010 előtt is vitatéma volt, mert ezeken a vonalakon kevés utas utazott, a fenntartásuk viszont pénzbe került. Az 1990-es évektől több vonalon megszüntették vagy szüneteltették a személyforgalmat, és a kérdés 2010 után is visszatérő vita maradt.",
        "2023-ban az illetékes minisztérium több mellékvonalon felfüggesztette a személyforgalmat, és a vonatok helyett buszokat indított. A hivatalos kifejezés forgalomszüneteltetés volt, vagyis ideiglenes megoldás. A kormány indoklása szerint a pályák állapota és a járművek hiánya miatt a társaság kénytelen volt felfüggeszteni a forgalmat.",
        "A bírálók, köztük helyi önkormányzatok és civil szervezetek, azt mondták, hogy a vidéki települések lakói így nehezebben jutnak el az iskolába és a munkahelyre. Az eljutási alapjog kifejezést ők használták. Attól is tartottak, hogy a szüneteltetett vonalak később végleg megszűnnek.",
        "A két oldal eltérően ítélte meg a helyzetet, és a kérdés vitatott maradt."]),
 challenge=dict(title="Communicative Challenge: A Suspended Line",scenario="You have read about the suspension of service on the branch lines in 2023. A friend asks why the service was suspended.",prompt="Tell your friend what the government's reasoning said and what the local governments said.",cues=["Give the government's reasoning: the ministry had no choice","Give the local governments' view: what the residents had to do"],target="A kormány indoklása szerint a minisztérium kénytelen volt felfüggeszteni a forgalmat. Az önkormányzatok szerint a lakosok kénytelenek voltak buszra szállni.",english="According to the government's reasoning, the ministry was forced to suspend the service. According to the local governments, the residents were forced to take a bus."),
 items=[
  mc(P+"-02-introduce-1","vocabulary","introduce","Mit jelentett a *forgalomszüneteltetés* a hivatalos nyelvhasználatban?",["Azt, hogy egy vonalon ideiglenesen nem közlekednek vonatok.","Azt, hogy egy vonalon a vonatok csak teherszállításra használhatók.","Azt, hogy egy vonalon a jegyek egy hónapig ingyenesek lesznek."],V,2),
  fb(P+"-02-controlled-2","controlled","A társaság köteles _____ üzemeltetni a megrendelt vonatokat.","volt","The company was obliged to operate the trains that had been ordered.","formal-obligation"),
  match(P+"-02-controlled-3","controlled",[("mellékvonal","kisebb forgalmú vasútvonal a fővonalak mellett"),("pótlóbusz","vonat helyett közlekedő autóbusz"),("elszigetelődés","a település kapcsolatának gyengülése a külvilággal"),("önkormányzat","a település helyi választott vezetése")],V),
  fb(P+"-02-practice-4","practice","A kormány indoklása szerint a pályák állapota miatt a minisztérium _____ volt felfüggeszteni a forgalmat.","kénytelen","According to the government's reasoning, the ministry was forced to suspend the service because of the condition of the tracks.","formal-obligation","forced (adjective)"),
  sb(P+"-02-practice-5","practice","Az önkormányzatok szerint a lakosok kénytelenek voltak buszra szállni.","According to the local governments, the residents were forced to take a bus.","formal-obligation"),
  dlg(P+"-02-dialogue-6",[("Tanár","Mit írt elő a közszolgáltatási szerződés a társaságnak?"),("Diák","A társaság _____ üzemeltetni a megrendelt vonatokat."),("Tanár","És mit mondott a kormány indoklása a felfüggesztésről?")],["köteles volt","kötelesek voltak","kötelesség volt"],"formal-obligation",1),
  wr(P+"-02-production-7","production","Write one or two sentences in Hungarian about what the local governments said about the residents of the villages, naming the source.","Az önkormányzatok szerint a vidéki lakosok kénytelenek voltak buszra szállni, és nehezebben jutottak el az iskolába.",V),
  mc(P+"-02-check-8","grammar","check","Melyik kifejezés jelenti, hogy valakinek nem volt más választása?",["kénytelen volt","hajlandó volt","szabad volt"],"formal-obligation",2),
 ])
# ---------------- 03
L["03"]=dict(
 title="The Motorway Concession, 2022",
 intro_title="Unit 28: "+UT,
 intro=["This lesson covers the decision of 2022 to hand the operation of part of the motorway network to a concession company for 35 years.","The reasons of the government and the objections of the critics are given with their sources."],
 grammar_title="The More, the More: Minél … annál …",
 goal=["I can link the length of a contract to the freedom to change it with *minél … annál …*.",
       "I can describe the motorway concession of 2022 and the objections to it, with the source of each view.",
       "I can use the words of public contracts (*koncesszió*, *rendelkezésre állási díj*, *átláthatóság*)."],
 grammar=[
  t(("Two Quantities Together","You know *minél … annál …* from B1 Unit 2. The first clause has *minél* and a comparative, the second *annál* and a comparative: `Minél hosszabb a szerződés, annál hosszabb ideig köti az államot.` A history text uses it for how things are connected, and gives the source of a disputed link: `A bírálók szerint minél hosszabb a szerződés, annál nehezebb módosítani.`")),
  t(("Word Order","The comparative stands next to *minél* and *annál*: `minél több pénzt köt le …, annál kisebb mozgástere marad …`. The two clauses are separated by a comma.")),
  tab([["Minél hosszabb a szerződés, annál hosszabb ideig köti az államot.","The longer the contract, the longer it binds the state."],
       ["Minél több pénzt köt le egy szerződés, annál kisebb a költségvetés mozgástere.","The more money a contract ties up, the smaller the budget's room for manoeuvre."],
       ["A bírálók szerint minél hosszabb a koncesszió, annál nehezebb módosítani a feltételeket.","According to the critics, the longer the concession, the harder it is to change the conditions."]])],
 vocab=[("koncesszió","concession (a long contract handing a public task to a company)","noun"),("rendelkezésre állási díj","availability fee (paid by the state for roads kept usable)","expression"),("üzemeltetés","operation (of a facility)","noun"),("átláthatóság","transparency","noun"),("költségvetés","budget","noun"),("mozgástér","room for manoeuvre","noun"),("szerződés","contract","noun"),("közfeladat","public task","noun")],
 story=dict(file="c1-kozlekedespolitika-03-autopalya-koncesszio-35ev",title="Az autópálya-koncesszió, 2022",skill="correlative-minel-annal",
  summary="A 2022-es döntés az autópálya-hálózat egy részének 35 éves koncessziójáról, a kormány indoklása és a bírálók kifogásai szerint.",
  text=["A magyar autópálya-hálózat a 2010-es években jelentősen bővült. 2022-ben a kormány úgy döntött, hogy az autópályák egy részének üzemeltetését és fejlesztését 35 évre koncesszióba adja.",
        "A koncesszió azt jelenti, hogy az állam hosszú időre átad egy közfeladatot egy magáncégnek, és ezért díjat fizet neki. Ez a rendelkezésre állási díj: az állam azért fizet, hogy az utak használhatók legyenek.",
        "A kormány indoklása szerint a megoldás biztosítja az utak fenntartását és fejlesztését. A bírálók szerint viszont minél hosszabb a szerződés, annál nehezebb módosítani a feltételeit, és minél több pénzt köt le a díj, annál kisebb a költségvetés mozgástere, például a vasút számára.",
        "A bírálók a szerződés átláthatóságát is vitatták. A koncesszió megítélése vitatott volt."]),
 challenge=dict(title="Communicative Challenge: A Long Contract",scenario="You have read about the motorway concession of 2022. A friend asks why the critics objected to such a long contract.",prompt="Tell your friend what the critics said about the length of the contract.",cues=["Say whose view it is","Say how the length of the contract and the changing of the conditions go together"],target="A bírálók szerint minél hosszabb a koncesszió, annál nehezebb módosítani a feltételeket.",english="According to the critics, the longer the concession, the harder it is to change the conditions."),
 items=[
  mc(P+"-03-introduce-1","vocabulary","introduce","Mit jelent a *koncesszió* közigazgatási szövegben?",["Hosszú időre szóló szerződést, amellyel az állam közfeladatot bíz egy magáncégre.","Rövid határidejű szerződést, amellyel egy cég irodát bérel egy állami hivatalban.","Olyan adót, amelyet minden autós évente egyszer fizet be az államnak."],V,0),
  fb(P+"-03-controlled-2","controlled","Minél hosszabb a szerződés, _____ hosszabb ideig köti az államot.","annál","The longer the contract, the longer it binds the state.","correlative-minel-annal"),
  match(P+"-03-controlled-3","controlled",[("koncesszió","közfeladat hosszú távú átadása egy cégnek"),("rendelkezésre állási díj","az állam fizetése a használható utakért"),("üzemeltetés","egy létesítmény működtetése és karbantartása"),("átláthatóság","az, hogy a szerződés adatai nyilvánosak és ellenőrizhetők")],V),
  fb(P+"-03-practice-4","practice","Minél több pénzt köt le egy szerződés, annál _____ a költségvetés mozgástere.",["kisebb","szűkebb"],"The more money a contract ties up, the smaller the budget's room for manoeuvre.","correlative-minel-annal","small, comparative"),
  sb(P+"-03-practice-5","practice","Minél hosszabb a koncessziós időszak, annál nehezebb módosítani a feltételeket.","The longer the concession period, the harder it is to change the conditions.","correlative-minel-annal"),
  dlg(P+"-03-dialogue-6",[("Tanár","Miért vitatták a bírálók a hosszú szerződést?"),("Diák","Szerintük minél hosszabb a szerződés, _____ nehezebb módosítani."),("Tanár","És mit mondott a kormány indoklása?")],["annál","olyan","akkor"],"correlative-minel-annal",1),
  wr(P+"-03-production-7","production","Write a sentence in Hungarian with minél … annál … about a long contract and the budget.","Minél hosszabb a szerződés, annál tovább köti az államot, és annál kisebb a költségvetés mozgástere.",V),
  mc(P+"-03-check-8","grammar","check","Melyik mondat helyes?",["Minél hosszabb a szerződés, annál hosszabb ideig köt.","Minél hosszabb a szerződés, minél hosszabb ideig köt.","Annál hosszabb a szerződés, minél hosszabb ideig köt."],"correlative-minel-annal",2),
 ])
# ---------------- 04
L["04"]=dict(
 title="The Budapest–Belgrade Railway, 2013–2026",
 intro_title="Unit 28: "+UT,
 intro=["This lesson covers the modernisation of the Budapest–Belgrade railway, financed largely by a Chinese loan.","The government's reasoning and the critics' objections are given with their sources."],
 grammar_title="Despite It: Annak ellenére, hogy …",
 goal=["I can say that something happened although there was an objection, with *annak ellenére, hogy …*.",
       "I can describe the Budapest–Belgrade railway project and the objections to it, with the source of each view.",
       "I can use the words of large investments (*hitel*, *titkosítás*, *megtérülés*)."],
 grammar=[
  t(("Although …","You know *annak ellenére, hogy* from B1 Unit 5. In a history text it shows that a fact held while an objection stood: `Annak ellenére, hogy a megtérülés vitatott volt, az építés megkezdődött.` The fact is stated by the narrator; the objection is attributed.")),
  t(("Two Sides of One Project","The same project can be described from two sources: `a kormány indoklása szerint …, a bírálók szerint viszont …`. You know *viszont* from B1 Unit 11. The contrast is in the sources, not in the narrator's voice.")),
  tab([["Annak ellenére, hogy a megtérülés vitatott volt, az építés megkezdődött.","Although the return on the investment was disputed, construction began."],
       ["A kormány indoklása szerint a vonal része a teherfolyosónak.","According to the government's reasoning, the line is part of the freight corridor."],
       ["A bírálók szerint viszont a megtérülés bizonytalan.","According to the critics, however, the return is uncertain."]])],
 vocab=[("hitel","loan, credit","noun"),("titkosítás","classification (making data secret)","noun"),("megtérülés","return on an investment","noun"),("teherfolyosó","freight corridor","noun"),("elővárosi","suburban","adjective"),("beruházás","investment (a large project)","noun")],
 story=dict(file="c1-kozlekedespolitika-04-budapest-belgrad-visszassagok",title="A Budapest–Belgrád vasútvonal, 2013–2026",skill="concessive-annak-ellenere",
  summary="A Budapest–Belgrád vasútvonal korszerűsítésének története 2013-tól: a kínai hitel, a titkosítás és a megtérülésről szóló vita, a kormány és a bírálók szerint.",
  text=["A Budapest–Belgrád vasútvonal korszerűsítéséről 2013-ban Magyarország, Szerbia és Kína képviselői egyeztettek, a részletes megállapodások 2014-ben és később születtek. Az építés költségének nagy részét kínai hitelből fedezték, és az Országgyűlés 2020-ban törvénnyel hirdette ki a vonatkozó megállapodást.",
        "A szerződések egy részét a kormány titkosította, ezért a költségekről és a megtérülésről kevés adat volt nyilvános. Annak ellenére, hogy a megtérülés vitatott volt, az építés 2022-ben megkezdődött.",
        "A kormány indoklása szerint a vonal része annak a teherfolyosónak, amely Közép-Európát a görög kikötőkkel köti össze, és javítja a kereskedelmi kapcsolatokat. A bírálók, köztük több közlekedési szakértő, azt mondták, hogy a megtérülés bizonytalan. Szerintük az összeget az elővárosi vasútfejlesztésekre is lehetett volna fordítani.",
        "A szerb szakasz 2022-ben megnyílt. A projekt megítélése megosztott volt."]),
 challenge=dict(title="Communicative Challenge: A Disputed Investment",scenario="You have read about the Budapest–Belgrade railway. A friend asks how the project went on although its return was disputed.",prompt="Tell your friend that the construction began although the return was disputed, and what the critics said.",cues=["Say that the construction began although the return was disputed","Say what the critics said about the return"],target="Annak ellenére, hogy a megtérülés vitatott volt, az építés megkezdődött. A bírálók szerint a megtérülés bizonytalan.",english="Although the return was disputed, construction began. According to the critics, the return is uncertain."),
 items=[
  mc(P+"-04-introduce-1","vocabulary","introduce","Mit jelent a *megtérülés* egy beruházásnál?",["Azt, hogy a befektetett összeg idővel visszatér a bevételekből.","Azt, hogy a beruházást egy másik városba helyezik át.","Azt, hogy az építkezés befejezése után a pályát lebontják."],V,0),
  fb(P+"-04-controlled-2","controlled","Annak _____, hogy a megtérülés vitatott volt, az építés megkezdődött.","ellenére","Although the return was disputed, construction began.","concessive-annak-ellenere","despite (postposition)"),
  match(P+"-04-controlled-3","controlled",[("hitel","kölcsön, amelyet vissza kell fizetni"),("titkosítás","adatok kizárása a nyilvánosságból"),("teherfolyosó","az áruszállítás fő útvonala több országon át"),("elővárosi","a nagyváros körüli településeket érintő")],V),
  fb(P+"-04-practice-4","practice","Annak ellenére, _____ a költségekről kevés adat volt nyilvános, a két oldal vitatkozott a megtérülésről.","hogy","Although little data on the costs was public, the two sides argued about the return.","concessive-annak-ellenere"),
  sb(P+"-04-practice-5","practice","Annak ellenére, hogy a megtérülés vitatott volt, az építés megkezdődött.","Although the return was disputed, construction began.","concessive-annak-ellenere"),
  dlg(P+"-04-dialogue-6",[("Tanár","Megkezdődött az építés, pedig vitatott volt a megtérülés?"),("Diák","Igen, annak _____, hogy vitatott volt, megkezdődött."),("Tanár","Mit mondtak a bírálók?")],["ellenére","miatt","óta"],"concessive-annak-ellenere",0),
  wr(P+"-04-production-7","production","Write two sentences in Hungarian about the Budapest–Belgrade line: what the government's reasoning said and what the critics said.","A kormány indoklása szerint a vonal része a teherfolyosónak. A bírálók szerint viszont a megtérülés bizonytalan.",V),
  mc(P+"-04-check-8","grammar","check","Melyik mondat helyes?",["Annak ellenére, hogy vitatott volt, megkezdődött.","Annak ellenére, vitatott volt, megkezdődött.","Annak ellenére, hogy vitatott volt, hogy megkezdődött."],"concessive-annak-ellenere",1),
 ])
# ---------------- 05
L["05"]=dict(
 title="Fare Passes and the Debate Before the 2026 Election",
 intro_title="Unit 28: "+UT,
 intro=["This lesson covers the cheap passes of 2023 and the arguments about public transport before the election of 2026.","It closes the period with the dated facts of the spring of 2026."],
 grammar_title="Reporting What Was Said",
 goal=["I can report what the pro-government side and the experts said about the passes with *azt mondta, hogy …*.",
       "I can describe the fare passes of 2023 and the arguments about them, with the source of each view.",
       "I can use the words of fares and elections (*bérlet*, *jegybevétel*, *választási kampány*)."],
 grammar=[
  t(("Reported Statements","You know *azt mondta, hogy …* from B1 Unit 13. The verb takes *azt* and the clause follows with *hogy*: `A szakértők azt mondták, hogy a felújításra is szükség van.` The tense of the original statement stays as it was said.")),
  t(("Naming Each Side","Reported statements keep the two sides apart: `a kormánypárti oldal azt mondta, hogy …`, `a szakértők közül többen azt közölték, hogy …`. The narrator reports; the sides judge.")),
  tab([["A kormánypárti oldal azt mondta, hogy az olcsó bérlet segített az ingázóknak.","The pro-government side said that the cheap pass helped commuters."],
       ["A szakértők azt mondták, hogy a felújításra is szükség van.","The experts said that renovation was also needed."],
       ["Az ellenzék azt közölte, hogy a közlekedés fontos választási téma.","The opposition said that transport was an important election issue."]])],
 vocab=[("bérlet","pass (a ticket valid for a period)","noun"),("jegybevétel","ticket revenue","noun"),("választási kampány","election campaign","expression"),("ingázó","commuter","noun"),("kormánypárti","pro-government","adjective"),("ellenzék","opposition","noun"),("megye","county","noun")],
 story=dict(file="c1-kozlekedespolitika-05-orszageberlet-valsag-jovo",title="Az országbérlet és a vita 2026 előtt",skill="reported-speech-statements",
  summary="A 2023-ban bevezetett olcsó bérletek, az azokról szóló viták és a közlekedés a 2026-os választás előtt, majd az időszak lezárása a választás eredményével.",
  text=["2023-ban a kormány bevezette az országbérletet és a vármegyebérletet: a havi bérlettel olcsón lehetett utazni a MÁV és a Volánbusz járatain. A vármegye név 2023-tól volt a megye hivatalos neve.",
        "A kormánypárti oldal azt mondta, hogy az olcsó bérlet segített az ingázóknak, és többen választották a közösségi közlekedést. A szakértők közül többen azt közölték, hogy a jegyek mellett a járművek és a pályák felújítására is szükség van, és a kiesett jegybevétel kérdéséről is vita volt.",
        "A 2026-os választás előtt a közlekedés a kampány egyik témája volt, és a pártok eltérő programokat mutattak be. Az ellenzék azt mondta, hogy a vasút állapota fontos kérdés, a kormánypárti oldal pedig a bérletek és a fejlesztések eredményeire hivatkozott.",
        "2026. április 12-én a Tisza Párt a 199 mandátumból 141-et szerzett, ami kétharmados többség volt, és Orbán Viktor még aznap este elismerte a vereséget. 2026. május 9-én az új Országgyűlés Magyar Pétert választotta miniszterelnökké. 2026. október 1-jétől a megyét ismét megyének hívják."]),
 challenge=dict(title="Communicative Challenge: Two Sides on the Passes",scenario="You have read about the cheap passes of 2023. A friend asks what the pro-government side and the experts said.",prompt="Tell your friend what each side said about the passes.",cues=["Say what the pro-government side said about the commuters","Say what the experts said about renovation"],target="A kormánypárti oldal azt mondta, hogy az olcsó bérlet segített az ingázóknak. A szakértők azt mondták, hogy a felújításra is szükség van.",english="The pro-government side said that the cheap pass helped commuters. The experts said that renovation was also needed."),
 items=[
  mc(P+"-05-introduce-1","vocabulary","introduce","Mit jelent a *bérlet*?",["Meghatározott időre szóló jegyet, amellyel többször lehet utazni.","Egyszeri jegyet, amely csak egy útra érvényes a vonaton.","Azt a díjat, amelyet a vasúttársaság a pálya használatáért fizet."],V,2),
  fb(P+"-05-controlled-2","controlled","A kormánypárti oldal azt mondta, _____ az olcsó bérlet segített az ingázóknak.","hogy","The pro-government side said that the cheap pass helped commuters.","reported-speech-statements"),
  match(P+"-05-controlled-3","controlled",[("ingázó","aki rendszeresen másik településre utazik dolgozni vagy tanulni"),("jegybevétel","a jegyek eladásából származó pénz"),("választási kampány","a választás előtti időszak, amikor a pártok programot mutatnak be"),("ellenzék","a kormányon kívüli pártok összessége")],V),
  fb(P+"-05-practice-4","practice","A szakértők azt _____, hogy a felújításra is szükség van.","mondták","The experts said that renovation was also needed.","reported-speech-statements","say, past, 3pl definite"),
  sb(P+"-05-practice-5","practice","A szakértők azt mondták, hogy a járművek felújítására is szükség van.","The experts said that the renovation of the vehicles was also needed.","reported-speech-statements"),
  dlg(P+"-05-dialogue-6",[("Tanár","Mit mondott a kormánypárti oldal a bérletről?"),("Diák","Azt _____, hogy a bérlet segített az ingázóknak."),("Tanár","És a szakértők?")],["mondta","mondtam","mondani"],"reported-speech-statements",1),
  wr(P+"-05-production-7","production","Write two sentences in Hungarian reporting what the pro-government side and the experts said about the passes, with azt mondta/mondták, hogy.","A kormánypárti oldal azt mondta, hogy az olcsó bérlet segített az ingázóknak. A szakértők azt mondták, hogy a felújításra is szükség van.",V),
  mc(P+"-05-check-8","grammar","check","Melyik kifejezés tulajdonít állítást másnak?",["azt mondták, hogy","nyilvánvaló, hogy","kétségtelen, hogy"],"reported-speech-statements",0),
 ])
# ---------------- consolidation
L["consolidation"]=dict(
 title="Unit 28 Consolidation: "+UT,
 intro_title="Consolidation Goals",intro=[""],
 goal=["I can sum up the disputes about transport policy between 2010 and 2026, with the source of each view.",
       "I can report the disputes about the branch lines, the motorway concession and the Budapest–Belgrade line, with the source of each view.",
       "I can close an account of transport policy with the dated facts of the spring of 2026."],
 items=[
  mc(P+"-consolidation-1","grammar","recognize","Melyik mondat nevezi meg, hogy ki mondta a véleményt?",["A szakértők szerint a lassújelek miatt nőttek a késések.","A lassújelek miatt természetesen nőttek a késések.","A késések nőttek, és ez egyértelmű volt."],"evidentials",1),
  mc(P+"-consolidation-2","grammar","recognize","Melyik kifejezés jelent kényszert?",["kénytelen volt","hajlandó volt","képes volt"],"formal-obligation",0),
  match(P+"-consolidation-3","recognize",[("lassújel","a pálya állapota miatti ideiglenes lassítás"),("mellékvonal","kis forgalmú, másodlagos vasútvonal"),("koncesszió","közfeladat átadása hosszú időre"),("megtérülés","a befektetés visszatérése a bevételekből"),("bérlet","többször használható, időre szóló jegy")],V),
  fb(P+"-consolidation-4","recall","A vonat helyett közlekedő autóbusz neve _____.","pótlóbusz","The bus that runs instead of the train is called a rail-replacement bus.",V,"replacement bus",cat="vocabulary"),
  fb(P+"-consolidation-5","recall","Az állam a rendelkezésre állási díjat azért fizette, hogy az utak használhatók _____.","legyenek","The state paid the availability fee so that the roads would be usable.","hogy-jon-jen","be (subjunctive, plural)"),
  fb(P+"-consolidation-6","recall","A kormány indoklása _____ a pályák állapota miatt szüneteltették a forgalmat.","szerint","According to the government's reasoning, service was suspended because of the condition of the tracks.","evidentials"),
  fb(P+"-consolidation-7","context","Minél több a megálló, _____ lassabb az utazás.","annál","The more stops there are, the slower the journey.","correlative-minel-annal"),
  fb(P+"-consolidation-8","context","Annak _____, hogy sok vita volt, az építés megkezdődött.","ellenére","Although there was much dispute, construction began.","concessive-annak-ellenere","despite (postposition)"),
  mc(P+"-consolidation-9","grammar","context","Mi a *szerint* szerepe egy történeti szövegben?",["Megnevezi, ki állította az adott véleményt.","Jelzi, hogy az állítás biztosan igaz.","Jelzi, hogy az állítás későbbi időre vonatkozik."],"evidentials",2),
  sb(P+"-consolidation-10","produce","A szakértők azt mondták, hogy a pályák felújítására is szükség van.","The experts said that the renovation of the tracks was also needed.","reported-speech-statements"),
  wr(P+"-consolidation-11","production","Write two sentences in Hungarian about the motorway concession: what the critics said and what the government's reasoning said, naming each source.","A bírálók szerint minél hosszabb a szerződés, annál nehezebb módosítani. A kormány indoklása szerint a megoldás biztosítja az utak fenntartását.",V),
  wr(P+"-consolidation-12","production","Write one or two sentences in Hungarian about the election of 12 April 2026.","2026. április 12-én a Tisza Párt a 199 mandátumból 141-et szerzett, és Orbán Viktor még aznap este elismerte a vereséget.",V),
 ],
 challenge=dict(title="Communicative Challenge: Summing Up the Unit",scenario="At the end of a talk about transport policy from 2010 to 2026, a friend asks what you remember.",prompt="Tell your friend what the critics said about the motorway concession and how the period ended.",cues=["Say what the critics said about the concession","Say what happened on 12 April 2026"],target="A bírálók szerint minél hosszabb a koncesszió, annál nehezebb módosítani a feltételeket. 2026. április 12-én a Tisza Párt a 199 mandátumból 141-et szerzett.",english="According to the critics, the longer the concession, the harder it is to change the conditions. On 12 April 2026 the Tisza party won 141 of the 199 seats."),
)
for n,l in L.items():
    if n=="consolidation": l["grammar_title"]="Review and Capstone Integration"
    l.setdefault("grammar_title","")
S=dict(stem=P,unit_title=UT,unit_id="railway-decay",lessons=L,chfile="/home/user/parlour-read-b/challenges-railway-decay.json")
if __name__=="__main__":
    # word counts
    for n,l in L.items():
        if "story" in l: print(n,words(" ".join(l["story"]["text"])))
