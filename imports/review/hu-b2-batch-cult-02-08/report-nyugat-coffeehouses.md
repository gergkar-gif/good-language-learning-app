# Reader A report: hu b2 nyugat-coffeehouses (B2 Unit 2, culture track)

Files: fixes-nyugat-coffeehouses.json (88 fixes), challenges-nyugat-coffeehouses.json (6), facts-nyugat-coffeehouses.md.
Commands run: check-content (7 errors, all fixed below), render_lesson (no `!!`), unmet-words (about 110 hits, vocabulary fixes below), audit-reader-coverage for the five stems.
The story files carry no `questions`; reading questions are the lessons' `reading` items (ex06 of each lesson), checked against the segments.

## 1. Found by reading
Stories (segments, fixed on the segment files; every line also in the facts file):
- seg 01 p1: "Míg más európai nagyvárosokban az írók többnyire zárt szalonokban vagy egyetemi klubokban találkoztak" is false (Vienna, Prague, Paris had literary cafés); "joggal nevezték a kávéházak fővárosának" is a judgement (Vienna usually holds the title); "több mint ötszáz" is an estimate. Fixed: "Budapestet is ... tartották", other cities had cafés and salons, "a becslések szerint". (unsure on wording)
- seg 01 p3: the key legend names Molnár Ferenc (16 in 1894). Fixed to "egyes változatok szerint Molnár Ferenc és barátai". (unsure)
- seg 01 p4: "karzat / mélyvíz" division and the "kutyanyelv" writer's kit are memoir lore: hedged "A visszaemlékezések szerint". "kutyanyelv" = narrow paper strip: check the meaning.
- seg 01 p5: "lebontotta a társadalmi korlátokat" and "egyetlen jól sikerült kézirat ... másnap az egész körút az ő nevét emlegesse" stated as fact: softened and attributed to anecdotes.
- seg 02 p3: "Kelemen kőműves lantot pengető alakját" (name is Kőműves Kelemen; the lute detail is unverified); "pontosan sűrítette magába a szerkesztők hitvallását" is an interpretation. Fixed. (unsure)
- seg 02 p4: "képes volt alapjaiban megváltoztatni a magyar közgondolkodást" stated as fact: "sokak szerint ... befolyásolta".
- seg 02 p5: "kizárólag az esztétikai színvonal alapján" and "valódi fordulópontjává" overstated: hedged ("A hagyomány szerint", "Sok irodalomtörténész ezért tekinti").
- seg 03 p1: "alig néhány oldalnyi saját aforizmát" unverifiable; "akart hátrahagyni" is mind-reading. Fixed.
- seg 03 p2: "felismerte benne" (mind-reading) and "Móricz egyetlen éjszaka alatt ... legismertebb prózaírójává vált" (anecdote as fact): hedged, "közlésre érdemesnek ítélte".
- seg 03 p3: anecdote of hours of argument over one adjective: hedged.
- seg 03 p4: "szinte sohasem írt hivatalos levelet" is unsourced and odd; the generosity claim is memoir lore. Fixed.
- seg 03 p5: "mindannyian tudták a választ: Osvát Ernő szigora emelte a Nyugatot európai magaslatra" is mind-reading and glorifying. Fixed to "sokan ... említették".
- seg 04 p1: "majd a Nyugat élére állt" is false (Ady was its leading poet, not an editor). Fixed.
- seg 04 p2: modernists "kimutatták" settles a critical dispute: "azt állították".
- seg 04 p3: "a Kelet népe valamint a Magyar Figyelő hasábjain" (Kelet népe is Ignotus's essay title, not a Tisza paper; Magyar Figyelő unverified): both names removed. "minden eddiginél szélesebb olvasóközönség" hedged "sokak szerint". (unsure)
- seg 04 p4: conservative critics arguing at the Centrál in the evening: memoir lore, hedged.
- seg 04 p5: "megtanította a magyar értelmiséget" editorial moral: given to the modernists.
- seg 05 p1: Kosztolányi and Déry as Hadik regulars unverified: "Karinthy Frigyes és íróbarátainak asztaltársasága". (unsure)
- seg 05 p2: "mert a háborús cenzúra nem engedte meg a lap fennmaradását az eredeti nevén" unsupported (Nyugat ended with Babits's death); removed from the story and from L05 ex06's right option.
- seg 05 p3: "a Hungária vagy a Lukács": Hungária was the 1950s name of the New York café itself, so it cannot be a separate survivor next to it; Lukács is a pastry shop. Fixed to "presszó és cukrászda, például a Lukács". (unsure)
- seg 05 p4: the Centrál, New York and Hadik reopened after 1989 only in later years; "ma újra ... rendeznek" is a present-day claim: check (no fix, in the facts file).
- seg 05 p5: "a magyar kultúra legjava mindig ... született meg" sweeping: replaced.
Lessons:
- L01 gr example 3: "az épület éjjel-nappal nyitva állt" states the key legend as fact: replaced. Table "A szalonok zártak voltak" awkward: "zárt társaságok voltak" (unsure).
- L01 intro: "places to drink espresso" anachronistic: "coffee".
- L01 ex04: wrong option 2 ("..., viszont a kávéházak ...") is natural Hungarian (two right answers); replaced by "a viszont kávéházak"; stem "kötőszó" removed.
- L01 ex02: participial phrase "nyomdából érkezett" (Unit 2 may not use expanded participial phrases): removed. L03 ex03 "hibátlanul megírt", L03 gr example "a tökéletesre csiszolt kéziratot" (also the second speaking step) and consolidation ex04 "ugyanannál az asztalnál ülő írók" (also the first speaking step): rewritten without the participle.
- L01 ex05 ("a főpincér mindenkit név szerint ismert"), ex07 ("masterpieces were born at the marble table"), ex08 answers ("csak a kiváltságosokat", "minden tehetséges író előtt"): not in the segment or overstated; replaced.
- L02 ex04: wrong option "ennek ellenére hogy" is not a real string and "ennek ellenére" would also fit; replaced. L02 ex08 "bebizonyította" presents Ignotus's argument as proven.
- L02 gr text 2: "amellett érvelt, hogy" is a cataphoric anchor (`b2-cataphoric-clauses`, Unit 17): replaced by "azt írta, hogy".
- L03 ex02: "Móricz ... a novella kézirata révén vált híressé" is wrong (the story was published): rewritten (now tests the possessed accusative, `acc-poss`). ex04 stem "határozószón ... kizárólagos fókusz": grammar terms, and "kávéházban" is not a határozószó. ex07 "sohasem engedett": an absolute the segment doesn't state.
- L04 ex04 option 3 was a garbled non-phrase. L04 ex08 "az egész ország figyelmét" overclaims. L04 gr text 2 says Ady drew on Protestant biblical Hungarian and Parisian symbolism, the story says kuruc songs and the Károli Bible: consistent enough, left.
- L05 ex04: options 2 and 3 had two faults or were garbled (*Míg az ötvenes éveket illeti, korántsem ...*): now one fault each. ex06 absurd wrong options. ex08 "bezáratta" is a causative in -tat (Unit 19) and "1989 után ... újjászülettek" compresses the story.
- Consolidation ex09 right answer "Éppen a kávéházakban született meg a modern magyar újságírás" is an overclaim and the stem used grammar terms: new item on the karzat/kefelenyomat. ex12 "a legnagyobb tehetségeit" overclaim.
- Errors from check-content, all fixed: length-giveaway L01.ex01, L02.ex01, L02.ex06, L04.ex06, L05.ex01, L05.ex06; tell-absolute L03.ex01 (*Sohasem*).
- Vocabulary (unmet-words): fixes add the hits to the first lesson that uses them (01: 9 words; 02: 12; 03: 11; 04: 9; 05: 10). Six words used first in the consolidation (konzervatív, népies, forma, alkotói, próza, réved) are put on lesson 05 because the consolidation has no vocabulary file. Vocab-unused suspects (ami azt illeti, hitvallás, irányzat, önzetlenség, felfedez, vitairat, továbbvisz) occur in segments and screens; accepted.

## 2. Metadata
- Lessons 02 to 05 and the consolidation tag every grammar item `b2-contrastive-topic`, although they test other skills (retagged by fix):
  - míg … addig → `mig-egyidejuseg` (B1 Unit 4): L02 ex03, ex05; consolidation ex05, ex11.
  - ezzel szemben → `adversative-contrast` (B1 Unit 21): L02 ex04 (with `distractor_skills` {"1": "causal-postpositions"} on *ennek következtében*).
  - preverb inversion after csak / éppen → `b2-focus-inversion` (B2 Unit 1): L03 ex03, ex04, ex05, ex08; L05 ex03, ex05; consolidation ex06, ex09, ex12.
  - egyrészt … másrészt → `egyreszt-masreszt` (B1 Unit 7): L04 ex04.
  - korántsem (word and builder) → unit vocabulary: L04 ex03, ex05, consolidation ex07 (category vocabulary).
  - open writing with several forms → unit vocabulary: L02 ex08, L04 ex08, L05 ex08.
  - L03 ex02 → `acc-poss` (possessed accusative).
- The reviewer should run lock_tags after applying.

## 3. Goals / checklists
- L01 goal 3 "distinguish everyday hospitality vocabulary and literary café terminology": no item practises it (unsure).
- L03 goal 1 promised "why he published almost nothing of his own": rewritten ("describe Ernő Osvát's editorial standard and say whom he discovered"), also the challenge canDo.
- L04 goal 1 template "analyze the polemical debates": rewritten as a plain can-do. L04 goal 3 "at B2 level" is filler (left).
- Consolidation goal 1 "with B2 lexical precision": rewritten. Consolidation goals 2 and 3 say "fluently" (left).
- L05 goal 3 "public spheres": not practised (left).
- Recap screens: L01 (Ami … illeti from B2 Unit 1, viszont from B1 Unit 21), L02 (míg B1 Unit 4, ezzel szemben B1 Unit 21), L03 (preverb inversion B2 Unit 1), L04 (egyrészt … másrészt B1 Unit 7), L05 (B2 Unit 1, B1 Units 4 and 21) all presented known material as new; each gets a "You know ..." sentence. L01 intro promised to "master" patterns taught before: "revisiting".

## 4. Doubtful
- Unit 2 recap names use the knowledge sheet: Ami … illeti (B2 Unit 1, b2-01-03), viszont and ezzel szemben (B1 Unit 21), míg (B1 Unit 4), egyrészt … másrészt (B1 Unit 7), focus inversion (B2 Unit 1, b2-01-02). The b1 Unit 4 grammar file also shows "míg X, addig Y".
- korántsem … hanem: no earlier unit teaches it (it first appears in b2-13 / Unit 25 lessons); the lesson 04 screen presents it as its own material; kept, tagged vocabulary.
- The unit's own grammar screens contain no later-B2 forms except the one cataphoric phrase fixed above. Segments use *amellett érvelt, hogy* and *arra, hogy* (stories are exempt; the second is gone with the fix).
- L02 ex03 hint "by contrast / correlative": "nem" fits the L04 ex03 blank too, but the hint "by no means" pins *korántsem* (left).
- The facts file lists every claim; the ones marked check to verify first: the Hungária/Lukács line, Magyar Csillag years, the reopening dates of the three cafés, the Kelet népe / Ignotus first-issue claim, the Nyugat emblem, Hét krajcár date, and the 500-coffeehouse figure.
- Reading items (ex06): L01 answerable (the fix removed paper and ink from the price claim); L02 answerable from p5; L03 ex06 answerable; L04 ex06 answerable after the "azt állították" fix; L05 ex06 answerable after the fix.

## 5. Dictionary
kékesfekete | kékesfekete | adjective | bluish-black |
tárcaírói | tárcaíró | noun | feuilleton writer |
vendéglátóhely | vendéglátóhely | noun | catering establishment, hospitality venue |
csillárfényt | csillárfény | noun | chandelier light |
életszemléletét | életszemlélet | noun | outlook on life, worldview |
kutyanyelvet | kutyanyelv | noun | narrow paper strip used by writers in cafés |
mélyvíznek | mélyvíz | noun | deep water, the deep end |
ugyanannál | ugyanaz | pronoun | the same |
zárhasson | zár | verb | to close, to lock |
emlékérme | emlékérme | noun | commemorative medal |
programadó | programadó | adjective | programmatic, setting out a programme |
tömegsajtó | tömegsajtó | noun | mass press |
könyvkereskedések | könyvkereskedés | noun | bookshop |
közgondolkodást | közgondolkodás | noun | public opinion, public way of thinking |
olvasóállványain | olvasóállvány | noun | reading rack, newspaper stand |
pengető | penget | verb | to pluck (a string) |
stílusirányzatot | stílusirányzat | noun | stylistic trend |
szimbolizmusa | szimbolizmus | noun | symbolism |
társadalomrajza | társadalomrajz | noun | portrayal of society |
virtuozitása | virtuozitás | noun | virtuosity |
félkész | félkész | adjective | half-finished |
bontakoztatta | bontakoztat | verb | to develop, to bring to unfold |
nyomorgó | nyomorog | verb | to live in poverty |
oldalnyi | oldalnyi | adjective | a page's worth |
őseredeti | őseredeti | adjective | primeval, utterly original |
prózaírójává | prózaíró | noun | prose writer |
vitakultúra | vitakultúra | noun | culture of debate |
asztalnyira | asztalnyi | adjective | the width of a table |
modernisták | modernista | noun | modernist |
sajtópárbajokba | sajtópárbaj | noun | press duel, newspaper polemic |
verstani | verstani | adjective | of versification, prosodic |
családiasabb | családias | adjective | homely, family-like |
ellenőrizhetetlen | ellenőrizhetetlen | adjective | impossible to check or control |
gyorsbüfévé | gyorsbüfé | noun | snack bar |
könyvbemutatókat | könyvbemutató | noun | book launch |
presszó | presszó | noun | espresso bar, small café |

Fix count: 88 (exercises 40, story segments 22, grammar screens 11, lesson files 10, vocabulary 5); challenges 6.
