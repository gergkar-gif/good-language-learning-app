# Report, B2 Unit 62 paprika-tokaj (reader B)

Files: fixes-paprika-tokaj.json (81 fixes), challenges-paprika-tokaj.json (6), facts-paprika-tokaj.md.
Commands run: check-content (7 errors: 6 tell-absolute, 1 length-giveaway; all fixed by rewriting the items), render_lesson, unmet-words (about 190 hits; all put on vocabulary lists, see 1/V), audit-reader-coverage for 5 stories, check_c1_forms (0 hits).

## 1. Found by reading
Stories (segment files):
- 01 p2 "Galeotto Marzio udvari krónikás feljegyzéseiből tudjuk": unverified attribution (Marzio wrote anecdotes of Matthias) -> "A korabeli leírások szerint" (unsure, check).
- 01 p1 "korszakalkotó fordulatot eredményezett": overstated -> "új hatásokat hozott". 01 p4 "híres volt mértéktartó, de ínyenc ... ügyelve arra": unsourced reputation, mind-reading -> "Egyes források szerint ... mértékletesen étkezett" (unsure). 01 p5 "évszázadokon át meghatározta a Kárpát-medence étkezési kultúráját": overstated -> "a történészek szerint a későbbi magyar konyhára is hatott".
- 02 p2 legend told as fact ("az első igazi aszúbort ... Amikor a török csapatok ..."): hedged, "a legenda szerint", with "egyes források szerint az aszú ennél korábban is ismert volt" (check). 02 p3 garbled "aszútésztára ... puttonnyal öntöttek egy gönci hordónyi kiváló mustot": the paste goes into the must -> fixed. 02 p4 verbatim Latin "Vinum Regum, Rex Vinorum" put in Louis XIV's mouth from memory -> anecdote, paraphrase, no quotation. 02 p4 "Az orosz cárok még állandó ... különítményt": undated -> "A 18. században az orosz udvar ..." (check). 02 p5 "a világ legelső zárt és eredetvédett borvidéke" is disputed and "évtizedekkel előzte meg a ... chianti osztályozásokat" is wrong (Chianti 1716, before 1737): rewritten, dispute named in one line, "a magyar törvényhozás" -> royal decree of Charles VI (check). Same "legelső" claim removed from ex08, consolidation ex03 and goal 02/3.
- 03 p5 Thomas Mann and Toscanini at Gundel: unverified -> general wording (check); "békebeli" for the interwar years is wrong (means pre-1914) -> removed; mind-reading ("meggyőződve arról") removed. 03 p3 "amelyeket a kor vezető írói és művészei ihlettek": unsourced, removed; the pancake and palócleves hedged as tradition. 03 p4 cake top "megvédte ... lehetővé téve": hedged tradition.
- 04 p1 "családi borászatokat államosították": small wineries were not nationalised -> "a nagyobb borbirtokokat" (check). 04 p3 Hortobágyi pancake and Somlói galuska "bemutatták" at Expo 58 and "óriási sikert": the pancake is older; hedged "a hagyomány szerint ... vált ismertté" (check). 04 p4 "találóan" judgement removed; "A történészek szerint" added.
- 05 p1 "joggal" judgement removed. 05 p2 "Budapest ... nyerte el ... Michelin-csillagokat": restaurants get stars -> "Budapest éttermei ... a 2010-es évektől" (check). 05 p3 kadarka/kékfrankos as "őshonos": origin disputed -> "őshonos és hagyományos". 05 p3 "felveszik a versenyt a világ elitjével" attributed ("egyes szakírók szerint").
- The unit is titled Paprika, Tokaj & Terroir but no segment mentions paprika (see 4).
Lessons / items:
- Question stems with Hungarian grammar terms (eredményhatározói rag, kötőszó, feltételes mód, segédige, sublativus, redukció): b2-borkultura-01.ex04, 02.ex04, 03.ex04, 04.ex04, 05.ex04, consolidation.ex04 -> plain stems.
- 01.ex08, 02.ex02, 03.ex02, 03.ex08, 04.ex02, 05.ex02: tells (kizárólag, teljesen, semmilyen), absurd wrong options -> plausible ones with one fault.
- 02.ex02 asks for 3-6 puttonyos: not in the segment and out of date (since 2013 only 5-6 puttonyos aszú are sold, check) -> asks what the segment says. 02.ex08 and consolidation ex03 "world's first" -> what the decree did. 04.ex08 "debütált" wrong -> hedged. 05.ex08 (terroir definition) not answerable from the segment, and the length give-away -> asks where kadarka/kékfrankos succeeded. 03.ex03 "friss és szezonális alapanyagok" not in segment. 03.ex08 "romlás" not in segment. 04.ex03 "új desszertjükkel" unsourced. 05.ex03 named varieties as indigenous.
- 02.ex05: kóstolnánk is a second right answer -> answers [ízlelnénk, kóstolnánk].
- 05.ex04, consolidation ex06 and ex08: every wrong option had two faults -> one fault. consolidation.ex06 "Olyan omlósra párolták, hogy ..." is the result clause of Unit 63 (annyira-hogy) -> plain sentence. consolidation ex07/ex12 nonce word "aszúborkülönlegesség" -> "aszú".
- Screens: lesson 05 table "A bort fűszeresre érlelték" is not a natural resultative -> replaced; 01 example "sűrűre sűrűsödjön" and 03 "sűrűre ... nem sűrűsödött" -> "sűrűre forrjon be", "be nem forrt"; English "thicken up thick" fixed; 02 screen "MUST" and "is a grammatical error" overstated (indicative after mintha occurs) -> softened.
- Unmet words: all hits added to the vocabulary list of the first lesson that uses them (01: 18 entries, 02: 14, 03: 6, 04: 11, 05: 27 incl. consolidation-only words, as the consolidation has no vocabulary file). consolidation.ex02 "mikroklíma" -> "éghajlat".

## 2. Metadata
- Items testing the resultative -ra/-re (01.ex04-07, 03.ex04-07, consolidation.ex04, ex05, ex06) were tagged `mintha`; retagged `ra-re` (category grammar). The dialogues (01.ex07, 03.ex07, consolidation.ex06) keep category dialogue; only `teaches` changes.
- distractor_skills added for real forms of other skills: puhán/sűrűn/keményen -> an-en-adverb; puhaként/sűrűként/keményként -> essive-formal-kent; puhává/ropogóssá -> translative-morphology; sűrűvel -> val-vel; keményből -> elative-bol-bel.
- Lesson files carry `"unit": 31` (stale). Stories carry grammar `b2-resultative-similes` (alias of mintha).

## 3. Goals / checklists
- 02 goal 1 and 3, 03 goal 1, 04 goals 1-3, 05 goals 1 and 3, consolidation goals 1-3 rewritten as plain can-do lines in both goal and checklist sections (goal 1 of each is the challenge's canDo).

## 4. Doubtful
- The unit title promises paprika; no segment, lesson or item deals with it. Not fixed (needs a new segment): decide.
- Lessons 02, 04, 05 replay Unit 61's `mintha`: recap lines "You know *mintha* from B2 Unit 61" added to the screens; lesson 01 recaps `ra-re` from A2 Unit 6, lesson 03 recaps lesson 1. No skill of its own exists for the resultative -ra/-re; items now use `ra-re` (A2) - confirm.
- No C1 forms, no Unit 63/65/67 grammar except the removed consolidation ex06 result clause.
- Present-day claims flagged "check" in facts: Michelin stars, 2013 puttonyos rule, Tokaj protected status (not stated in text).
- Story location label "Tokaj, Mád és Sárospatak (1650-1737)" does not match the 1630s legend (metadata only).
- Reading items copy no story questions (the segment files have none).

## 5. Dictionary
mértéktartó | mértéktartó | adjective | moderate, temperate |
aszúkészítés | aszúkészítés | noun | making of aszú wine |
eredetvédett | eredetvédett | adjective | protected by designation of origin |
nemespenész | nemespenész | noun | noble rot (Botrytis) |
túlérett | túlérett | adjective | overripe |
palócleves | palócleves | noun | Palóc soup (lamb soup with beans, dill and sour cream) |
borkészítés | borkészítés | noun | winemaking |
nagyüzemi | nagyüzemi | adjective | large-scale, industrial |
sertéspörkölt | sertéspörkölt | noun | pork stew with paprika |
tömegtermelés | tömegtermelés | noun | mass production |
szaksajtó | szaksajtó | noun | trade press, specialist press |
alapzat | alapzat | noun | foundation, base |
asztalnok | asztalnok | noun | master of the table (court official) |
konyhamester | konyhamester | noun | head cook |
reprezentáció | reprezentáció | noun | representation, official display |
rituálé | rituálé | noun | ritual |
szerémségi | szerémségi | adjective | of Syrmia (Szerémség) |
vadhús | vadhús | noun | game meat |
zöldfűszer | zöldfűszer | noun | fresh herb |
alapbor | alapbor | noun | base wine |
állomásoztat | állomásoztat | verb | to station (troops) |
aszúbor | aszúbor | noun | aszú wine |
aszúsodik | aszúsodik | verb | to turn into aszú (to shrivel with noble rot) |
aszúszem | aszúszem | noun | shrivelled aszú berry |
aszútészta | aszútészta | noun | aszú paste |
botrytis | botrytis | noun | botrytis (noble rot fungus) |
csipeget | csipeget | verb | to pick off bit by bit |
cukortartalom | cukortartalom | noun | sugar content |
fejedelemasszony | fejedelemasszony | noun | princess consort of Transylvania |
gönci | gönci | adjective | of Gönc (Gönc barrel) |
hordónyi | hordónyi | adjective | a barrel's worth of |
méltat | méltat | verb | to praise, to appreciate |
nektár | nektár | noun | nectar |
összetöppen | összetöppen | verb | to shrivel up |
présel | présel | verb | to press |
puttony | puttony | noun | puttony (wooden tub, unit of aszú sweetness) |
puttonyszám | puttonyszám | noun | puttony number |
savszerkezet | savszerkezet | noun | acid structure |
töpörödött | töpörödik | verb | to shrivel |
csokoládés | csokoládés | adjective | chocolate (made with chocolate) |
cukortető | cukortető | noun | sugar topping |
habosra | habos | adjective | frothy |
karamellizál | karamellizál | verb | to caramelise |
mazsolás | mazsolás | adjective | with raisins |
zarándokhely | zarándokhely | noun | place of pilgrimage |
alaplé | alaplé | noun | stock |
csúcsgasztronómia | csúcsgasztronómia | noun | haute cuisine |
élelmiszerár | élelmiszerár | noun | food price |
elzártság | elzártság | noun | isolation |
ízvilág | ízvilág | noun | range of flavours |
lángosozás | lángosozás | noun | eating lángos |
magánétterem | magánétterem | noun | private restaurant |
mesterszakács | mesterszakács | noun | master chef |
pancsolt | pancsol | verb | to water down (wine) |
receptkönyv | receptkönyv | noun | recipe book |
tündököl | tündököl | verb | to shine |
adalékanyag | adalékanyag | noun | additive |
ásványosság | ásványosság | noun | minerality |
beidegződés | beidegződés | noun | ingrained habit |
diadalút | diadalút | noun | triumphant progress |
dűlőszelektált | dűlőszelektált | adjective | single-vineyard selected |
elevenedik | elevenedik | verb | to come to life |
elit | elit | noun | elite |
emelhető | emel | verb | to raise |
gasztroforradalom | gasztroforradalom | noun | gastronomic revolution |
ízharmónia | ízharmónia | noun | harmony of flavours |
kékfrankos | kékfrankos | noun | Kékfrankos (grape variety) |
konyhatechnológia | konyhatechnológia | noun | cooking technology |
mangalicahús | mangalicahús | noun | mangalica pork |
omlós | omlós | adjective | tender, crumbly |
sommelier | sommelier | noun | sommelier |
szezonális | szezonális | adjective | seasonal |
textúra | textúra | noun | texture |
újrafelfedezés | újrafelfedezés | noun | rediscovery |

Fix count: 81 (Unit 62); challenges 6.
