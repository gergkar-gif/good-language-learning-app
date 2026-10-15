# Reader report: units 42 (post-office), 43 (banking), 44 (pharmacy), hu A2

Saved by Claude from reader B's reply (the harness refused the reader's report file, as in units 35–38).

Files written: `fixes-post-office.json` (77 fixes), `fixes-banking.json` (74), `fixes-pharmacy.json` (75); `challenges-post-office.json`, `challenges-banking.json`, `challenges-pharmacy.json` (6 each).

How the fixes were checked: `scripts/check_fixes.py` on a scratchpad copy of each list: 0 rejected in all three. All 34 check-content ERRORs are gone (PO 16, BK 8, PH 10). Unmet-word suspects fall PO 155 to about 49, BK 191 to about 104, PH 179 to about 98; the rest are mostly the lesson-topic words themselves (lakcímkártya, tértivevény, bankkártya …). Exercise fixes replace the whole exercise object.

## 1. Found by reading

### Unit 42, post-office (a2-206 … a2-210-consolidation, story a2-unit-42)

check-content ERRORs (all fixed): a2-207-check-1 (28 vs 17), a2-208-controlled-4 (35 vs 18), a2-208-intro-1 (73 vs 44), a2-209-controlled-4 (30 vs 23), a2-209-intro-1 (50 vs 35), a2-209-intro-2 (44 vs 26), a2-210-controlled-4 (40 vs 27 and tell-absolute "senki"), a2-210-dialogue-1 (12 vs 7), a2-210-check-1 (51 vs 35), a2-210-consolidation-1 (60 vs 32), -2 (59 vs 31), -4 (67 vs 41), -5 (59 vs 35), -13 (64 vs 34), -19 (40 vs 30).

Glued blanks (all fixed to whole-word blanks): a2-208-check-2 "az e havi víz____" + *számlát*; a2-209-controlled-2 "ki____" + *nyílik*; a2-209-check-2 "be____" + *csukta*; a2-210-consolidation-20 "ki____"; a2-210-consolidation-6 "sor____" + *számot*, -9 "értesí____" + *tőt*, -10 "nyitó____" + *kódot*, -15 "nyom____" + *követését*, -18 "csomag____" + *automatába*.

B1 forms drilled or presented, all rewritten with finite verbs:
- present participle -ó: a2-206-practice-1 "bejáratnál **lévő** gépből"; a2-208-practice-4 "csekken **szereplő**"; story "a bejáratnál **lévő** gépből".
- past participle: a2-206-practice-3 and 206-a ex. 3 "**felbélyegzett** boríték"; a2-207-check-1 "**lebélyegzett** feladóvevény"; "**lepecsételt** szelvény" in a2-208-controlled-2, a2-208-dialogue-2, 208-a ex. 3, story, a2-210-consolidation-17; "**kapott**" in a2-209-dialogue-2 and a2-210-consolidation-20; a2-209-check-1 "**megadott**"; a2-210-consolidation-13 "**levágott**", -15 "**feladott**"; a2-210-practice-4 "**található**"; story "megérkezett ajándékot" and question options "SMS-ben **kapott**", "postán **kapott**".
- adverbial -va/-ve: a2-210-consolidation-6 "**belépve**" (and its speaking step), -15 "**beírva**", -20 "**beütve**".
- a2-206-check-2 "**amíg** a sorszáma megjelenik" (unsure which skill); a2-208-practice-4 "**Mielőtt** elindulsz" (`miutan-mielott`).
- hogy + subjunctive: a2-209-practice-2 "hogy **átvedd** a rendelésedet" (B1 `hogy-jon-jen`); rebuilt as "át kell venned".
- Time -ig (*kézbesítésig*, *tizedikéig*): accepted.

Used before taught, fixed: a2-207-controlled-1 *szerződést* (a2-211); a2-209-dialogue-2 *beütöd*, a2-210-consolidation-10/-20 *kód/beütve* (a2-212); a2-210-consolidation-12 *igazolására* (a2-220); a2-206-intro-1 *ügyfélszolgálatot* (a2-215); a2-208-practice-2 *alkalmazással* (a2-218); a2-207-practice-2 *átvételi elismervényt* (a2-210); a2-208-check-2 *postaládába* (a2-210); a2-206-dialogue-1 *hivatalos* (a2-207); a2-210-consolidation-13 *ügyintéző* (a2-211). Not fixed (unsure): speaker label *Ügyintéző* and the story's *Postai ügyintéző* from a2-206, first listed in a2-211.

Unmet words in options/prompts replaced: a2-206-intro-1, a2-207-dialogue-1/-2, a2-206-dialogue-2, a2-208-intro-2, a2-208-check-1, a2-209-intro-1, a2-209-dialogue-1, a2-209-check-1 (now English), a2-210-intro-1, a2-210-check-1, a2-210-dialogue-2.

Wrong or odd Hungarian and English: a2-206-writing-1 "hol **lehet** sorszámot húznom" → "hol **kell** …"; a2-207-check-2 "a **pontos várost**"; a2-208-dialogue-2 "**közösköltséget**" (two words); a2-208-controlled-1 hint "to pay in" → "to pay in (be-)" (unsure); story summary named an áramszámla and a birthday present the text doesn't have (rewritten); "bankkártyával **óhajtok** fizetni" → "szeretnék fizetni"; story "az ajándékot" had no antecedent → "a csomagot".

Wrong-option defects: a2-206-intro-2 (two faults; now one each, with `distractor_skills`); a2-206-dialogue-1 "Muszáj vagyok", "Kellhetek" (non-words); a2-207-intro-2 give-away "(bal felső sarok)"; a2-210-consolidation-19 not real questions; a2-208-check-1 "átfizet" not a verb.

Screens: 206-b presents *szeretnék* + infinitive and 207-b the formal imperative without "You know …" (reworded; 207-b says "earlier in A2", unsure of unit number); 207-b ex. 3 not an imperative (replaced); 206-a, 208-a/b, 209-a/b, 210-a/b are vocabulary/culture notes under grammar titles.

### Unit 43, banking (a2-211 … a2-215-consolidation, story a2-unit-43)

check-content ERRORs (all fixed): a2-212-controlled-4, a2-212-practice-3, a2-214-intro-2, a2-214-practice-3, a2-215-intro-2, a2-215-consolidation-2, -5, -19.

Glued blanks fixed: a2-211-practice-4, a2-211-check-2, a2-212-controlled-2, a2-212-check-2, a2-213-practice-2, a2-213-check-2 ("ter____" + *minálhoz*), a2-214-controlled-1, a2-214-writing-1, a2-215-controlled-1, -practice-2, -practice-4, -writing-1, a2-215-consolidation-6, -7, -8, -9, -15, -18. Left (a whole word adds an unmet word): a2-212-practice-2 "be____", a2-212-dialogue-2 "el____", a2-214-check-2 "be____".

Definite conjugation: a2-215-writing-2 "A bank **minden** jogosulatlan levonást gondosan **kivizsgál**" → *kivizsgálja* (tag changed).

B1 forms: past participles (211-b "dombornyomott", a2-212-practice-3 and a2-215-consolidation-19 "nyomtatott", a2-214-check-1 "kapott", "megadott", a2-214-dialogue-1 "megadott", "vitatott" in a2-215-controlled-2, -practice-2, -consolidation-20 and 215-b, a2-215-controlled-4 "regisztrált", story options "elveszett", "felvett"); present participle (a2-212-writing-1 "fennmaradó", a2-211-check-2 "sorszámhúzó", 215-a "hívható"); story question "kilépve"; a2-215-dialogue-1 "hogy senki se élhessen vissza vele". Vocabulary a2-215 *elveszett*, *ellopott* are participles used as adjectives: not changed.

Used before taught: a2-211-practice-2 "PIN-kódot" (a2-212); a2-211-writing-1 "netbank" (a2-214); a2-212-check-1 *ügyfélszolgálatát* (a2-215); *alkalmazás* (a2-218) in a2-214-practice-1, a2-215-consolidation-10, a2-215-intro-1, a2-215-check-1; a2-214-dialogue-2 rebuilt (wrong options from a2-215, two right answers).

Wrong options and odd items: a2-211-intro-2 (two faults each); a2-211-dialogue-1 and a2-215-consolidation-11 "muszáj vagyok/voltam"; a2-211-dialogue-2 "húzza alá" real phrase; a2-212-controlled-4 "Korlátlanul bármikor." (tell-absolute); a2-214-check-1 punctuation tell; a2-215-check-2 *működhet*/*működik* both right; a2-215-consolidation-15 "számlaszámára" → *számlájára*; several rebuilt as English options or with met words. 214-a ex. 1 "a fele összeget" → fixed; 213-b "Készpénz fizetésnél" → *készpénzes*.

Recaps fixed with "You know …": 211-a (identity and address cards, *Szeretnék* + infinitive, *Kérem, írja alá*), 211-b (sorszámot húzni), a2-211 goal 2. a2-211-practice-1 *mutassa be* → *fel* (unsure).

Story 43: summary fixed (Gábor opens the account, Eszter withdraws); question options fixed.

### Unit 44, pharmacy (a2-216 … a2-220-consolidation, story a2-unit-44)

check-content ERRORs (all fixed): a2-216-intro-1, a2-217-check-1 (tell-absolute "kizárólag"), a2-217-practice-3, a2-219-intro-2, a2-220-intro-2, a2-220-dialogue-1, a2-220-dialogue-2, a2-220-consolidation-2, -4, -19.

Glued blanks fixed: a2-216-controlled-2 (and a2-220-consolidation-6), a2-217-practice-4, a2-218-controlled-1 (and a2-220-consolidation-8), a2-218-controlled-2, -practice-4, -check-2, a2-220-controlled-1, -practice-2, -check-2, a2-220-consolidation-15, -20, a2-216-practice-4 (unsure).

B1 forms: -andó/-endő and -va ("Gyermekektől elzárva tartandó!", "tárolandó") reworded; present participles (story "nyitva tartó", a2-218-controlled-2 "lévő", story option "lévő"); past participles and -va (a2-216-dialogue-1 "leverve", -dialogue-2 "javasolt", "felírt" in a2-217-practice-1/-2, a2-220-consolidation-11/-18 and 217-b, a2-217-dialogue-2 "felírva", 218-a "megengedett", 218-b "feltüntetett", "védett", a2-218-dialogue-2 "kifejezett", "leírtak szerint", a2-219-controlled-4 "elhelyezett", "zárva tartott", a2-220-writing-1 "lepecsételt", 220-b "javasolt", story option "megírt"); -ható/-hető words (only a2-217-check-2 rewritten); 219-b "amíg", 220-a "Mielőtt", a2-220-practice-2 "mielőtt" reworded.

Wrong or odd: a2-219-writing-1 prescription "for the pharmacy" reworded; "recipe" → "prescription" (217-b, a2-220-consolidation-7); 219-a called 1830 the national emergency hotline (reworded, unsure); a2-216-intro-1 wrong options rude/irrelevant; *patikus* → *gyógyszerész*; a2-216-check-1 distractors; many options rebuilt; a2-220-controlled-3 now uses *táppénz*. Story 44: "nyitva tartó patikát" → "Melyik patika van most nyitva?"; summary fixed.

Recaps: no pharmacy screen presents unit 42/43 material as new. 218-a lists *előtt / közben / után* as dosage terms (a1-83 material; unsure).

## 2. Metadata

- a2-206-intro-2: `distractor_skills` added ("1": inflected-infinitives, "2": present-tense-routine-language).
- a2-209-practice-2: `teaches` imperative-definite → inflected-infinitives.
- a2-210-consolidation-19: `distractor_skills` {"1","2": kell-infinitive}.
- a2-211-intro-2: `distractor_skills` {"1": definite-vs-indefinite-conjugation}.
- a2-213-intro-1: `distractor_skills` "1": ban-ben-in removed (*kártyában* ungrammatical).
- a2-215-writing-2: `teaches` how-the-accusative-t-works → definite-vs-indefinite-conjugation (unsure).
- a2-219-writing-1: `teaches` verb-government-nak-nek → ban-ben-in.
- Unsure, not changed: kerek-vs-szeretnek vs nek-conditional tags on similar items; a2-211-practice-2 prefix-word-order; fill-blanks tagged how-the-accusative-t-works without a case in the hint.

## 3. Goals / checklists

Fixed (goal array, goal section, checklist together): a2-210 line 2; a2-210-consolidation both lines; a2-211 line 2; a2-215-consolidation; a2-216 line 2; a2-220-consolidation. Not changed (unsure): a2-209 line 2, a2-212 line 1, a2-216 line 1, a2-219 line 2, a2-208 line 2.

## 4. Doubtful

- Facts (unsure): 208-a/a2-208-intro-2 "díjmentes"; a2-210-check-1/intro-1 "Személyi igazolvány és lakcímkártya" as the accepted ID; 215-b "within 30 days"; 213-b rounding table; a2-211 adókártya required.
- Prefix-glued blanks left: a2-212-practice-2, a2-212-dialogue-2, a2-214-check-2.
- Lexicalised -ó forms not rewritten: *szopogató*, *lázcsillapító*, *fájdalomcsillapító*, *gyulladáscsökkentő*, *torokfertőtlenítő*, *kapható*; also *elveszett*, *ellopott* and -ható/-hető words. Either the lessons go beyond A2, or `present-participle` is placed too high for lexicalised nouns.
- Grammar screens with no grammar: most of 206–220.
- Not fixed: a2-210-practice-2 *meghatalmazott*; a2-210-controlled-2 *fel*/*be*; a2-207-practice-4 and -writing-1 *követni*, *őrizd*.
- Wording doubts: a2-207-writing-1 "utolsó helyzetét"; a2-213-practice-1 "óhajt fizetni"; a2-214-writing-2 "bárhol és bármikor"; a2-212-dialogue-1 "automatához / postához"; a2-218-dialogue-2 weak distractors; a2-218-dialogue-1 "adjon be"; a2-220-consolidation-12.
- Story 44 "az e-recept felhőbe".
- a2-219-intro-1 and a2-220-consolidation-1 offer *104* as a wrong option for the single European emergency number; 104 is the real ambulance number.
- Remaining unmet-word suspects (~250) are mostly topic words missing from the lessons' own vocabulary lists.

## 5. Dictionary

feladóvevény | feladóvevény | noun | certificate of posting, dispatch receipt (stamped at the post office) |
hatjegyű | hatjegyű | adjective | six-digit |
csekkbefizetéshez | csekkbefizetés | noun | paying in a cheque, postal payment of a bill |
csomagautomatához | csomagautomata | noun | parcel locker |
lepecsételt | lepecsétel | verb | to stamp, to put an official stamp on |
lepecsételte | lepecsétel | verb | to stamp, to put an official stamp on |
nyitókóddal | nyitókód | noun | opening code (for a locker) |
nyugtázta | nyugtáz | verb | to acknowledge, to confirm receipt of |
sorszámot | sorszám | noun | queue number, queue ticket |
adókártyámat | adókártya | noun | tax ID card |
bankfiókban | bankfiók | noun | bank branch |
lakcímkártyámat | lakcímkártya | noun | address registration card |
mappámban | mappa | noun | folder, file folder |
mobilbankos | mobilbankos | adjective | of mobile banking (mobile-banking) |
számlanyitás | számlanyitás | noun | account opening |
számlanyitáshoz | számlanyitás | noun | account opening |
torokfájás | torokfájás | noun | sore throat |
torokgyulladás | torokgyulladás | noun | throat inflammation, tonsillitis |
ügyeleti | ügyeleti | adjective | on-call, duty (of the out-of-hours service) |
alhatsz | alszik | verb | to sleep |
hazamehetünk | hazamegy | verb | to go home |
tolóablakot | tolóablak | noun | sliding window, serving hatch |
ügyeletet | ügyelet | noun | duty, on-call service |

## 6. miatt

None in unit 42; no *miattam* … anywhere in 42–44. Plain *X miatt*, all in passing:
- a2-215-controlled-2 "A vitatott tranzakció **miatt** …" (tested word *reklamációt*; teaches how-the-accusative-t-works).
- a2-215-consolidation-18 "Nem kell aggódnod a biztonság **miatt** …" (how-the-accusative-t-works).
- a2-215-consolidation-20 "A vitatott levonás **miatt** …" (copy of -controlled-2).
- a2-220-controlled-1 "… a lázas megbetegedés **miatt**." (how-the-accusative-t-works).
- a2-220-dialogue-2 "ne aggódj a munka **miatt**!" (a2-pharmacy-vocab).
- a2-220-a-gr example 2 "… influenzás tünetek **miatt**." (screen example and speaking step 2).
- Story a2-unit-43 question 1, correct option "… az új munkahelye **miatt** …".
