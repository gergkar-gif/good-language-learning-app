# Reader B, hu b2 Unit 72 speaking-hungarian-today (culture track)

Fix file: fixes-speaking-hungarian-today.json (92 fixes). Challenges: challenges-speaking-hungarian-today.json (6). Facts: facts-speaking-hungarian-today.md. Nothing was tested (per the brief).

## 1. Found by reading
- **"Belső Pista" (story 04, lesson 04 title, intro of lesson 01, vocabulary title, ex08):** I could not identify any Hungarian idiom "Belső Pista" meaning the inner cultural compass; it looks invented. Removed from the story text (replaced by "belső kulturális iránytű"), the segment title, the lesson title and screen title, the vocabulary title, the lesson 01 intro and ex08 (unsure: "sure": false). The combined unit reading, `stories/manifest.json`, `curriculum.json` and `indexes/competencies-index.json` still carry the old title; the reviewer must rebuild/rename them.
- s04 p2: a film line put in quotation marks from memory ("a nemzetközi helyzet egyre fokozódik", A tanú): paraphrased; "nem enged a negyvennyolcból" kept as a saying without quotation marks (check).
- s02 p2: Petőfi's Nemzeti dal "lit the flame of the revolution from the Pilvax table": a legend stated as fact; hedged ("a hagyomány szerint", check). s02 p1: "a költő ... lépett fel a sorskérdések eldöntésekor" overstated, attributed to the traditional view. s02 p3 "a fasiszta barbárság poklában": loaded phrase replaced. s02 p4 ranking and "bizonyították": attributed and softened.
- s01 p2 etymology of kéz/szem/víz/vér/él given as proof: attributed to linguists; p3 "minden idegen elemet magyarrá formáltak" overclaim; p4 "birodalmi elnyomás" loaded label, and a generalisation about the nation's feelings: attributed; p5 speaker number marked as an estimate.
- s03 p1 "a világ kevés himnuszának egyike", "közmondásos ... alapmotívum": hedged and the origin of "sírva vigad a magyar" flagged (check); p3 "utolsó, elvehetetlen védőbástya" and p4 stereotype stated as a rule: attributed.
- s05 p1 "tizennyolc eset" depends on the counting (check); p3 "C1 mesterszint" mislabels C1 (mastery is C2): fixed.
- Grammar 01 example "nyelvtani rendszere teljesen egyedi maradt" (overclaim, reused in the read-aloud step), 02 example "mindig" (also read aloud), 04 examples "legfőbb kulcsa" and "rendkívül mélyek", 05 example "legfontosabb ismérve": softened, English follows.
- Screens 01, 02, 03, 05 presented known forms as new (see group 4).
- Items: 02.ex04 option 2 (*aggódván ... vetett*) is correct literary Hungarian (the -ván/-vén form, B2 Unit 11): a second right answer, replaced; 04.ex05 takes *mindamellett* and *mindazonáltal* (equal), consolidation ex05 takes *Jóllehet* and *Noha*.
- Reading items not answerable from the story: 02.ex08 (how the Bori notebook survived: the story never says; replaced by what its lines show), 04.ex08 (the "Belső Pista" concept), 03.ex08 (compares the anthem with "most European anthems": the story only says it is unusual; the new question asks what the text says), 01.ex07 question premise "szláv és germán többségű kontinens" (Europe also has Romance languages).
- Absurd wrong options replaced by plausible wrong claims or one-fault forms: 01.ex08, 02.ex02, 02.ex08, 03.ex02, 03.ex08, 04.ex02, 04.ex08, 05.ex02, 05.ex08, consolidation ex02; two-fault or non-form options fixed: 04.ex07 (option 3), 05.ex07 (option 3: *várnám, elmélyülésben, felfedezésére*), consolidation ex06, ex07, ex09.
- check-content ERRORs (12): length give-aways 01.ex08, 02.ex08, 03.ex08, 04.ex02, 04.ex04, 05.ex04, 05.ex08, consolidation ex02, and tells (*kizárólag*) 02.ex02, 03.ex08, 05.ex02, 05.ex08: all rewritten.
- Stems with Hungarian grammar terms (*emelkedett megengedő kötőszó*, *határozói igeneves*, *retorikai ellentétpár*, *mondatszerkesztés*, *legválasztékosabban*): replaced with plain questions. Wrong options that were C1 or not yet taught: *Feltéve* (01.ex04, 04.ex04, consolidation ex04), *Hacsak*, *amennyiben* as wrong options (03.ex04, consolidation ex08): replaced.
- 05.ex04 compared "B2/C1 szintű" sentences, a C1 claim; now a register item (what suits an official talk).

## 2. Metadata
- No retags were needed beyond what the fixes set: all grammar-tagged items keep skills that match (`contrastive-discourse-markers` 01.ex05 and consolidation ex08, `participle-actions` 02.ex04, `past-participle-adjective` 02.ex05, `egyreszt-masreszt` 03.ex04 and ex06); 01.ex07, 04.ex07 and 05.ex07 carry the verb-government tags and `distractor_skills` for the case options (04.ex07 now `verb-government-ban-ben` and `verb-government-rol-rel`; 05.ex07 `verb-government-ban-ben` and `verb-government-ra-re`).
- Not fixed, unsure: 02.ex05 is tagged `past-participle-adjective` while the sentence is now a plain sentence with *vetett*; still right.

## 3. Goals / checklists
- Each goal line exists three times in a lesson file; each rewrite is a set of three fixes. Rewritten first lines (they become the challenge `canDo`): 02 ("sacred civic role ... moral leaders" stated as fact: now "why Hungarian tradition sees poets ... as the conscience of the nation"), 03 ("unique ... razor-sharp"), 04 ("decipher ... legendary literary allusions, and idiomatic mental frames"). Others rewritten: 01 [1], 04 [1] (promised *mintegy*, which the screen never teaches), 05 [2] ("enjoy ... without hesitation"), consolidation [1] ("fluently integrate ... register shifts"). 01 [0], 05 [0] and consolidation [0] are plain already.

## 4. Doubtful
- **Culture unit replays earlier grammar (one line):** lessons 01, 02, 03 and 05 present *jóllehet*, *noha*, *mindazonáltal*, the participles and *egyfelől ... másfelől* as new; recap lines added (jóllehet/noha: "from earlier units"; *mindazonáltal*: B2 Unit 31; participles: B1 Units 57, 11, 3 and B2 Unit 3; *egyrészt ... másrészt*: B1 Unit 7). Unit 71's capstone content is "later" per the sheet but nothing from it is used.
- *egyszersmind*, *mindamellett* and *nem annyira ..., mint inkább* are on no earlier screen: left as this unit's new items (lesson 03 and 04), not C1 per the sheet's C1 list (unsure).
- C1 form: only `feltéve, ha` in the 05 table (the check_c1_forms hit): replaced by *abban az esetben, ha*; also *Feltéve* / *Hacsak* as wrong options in 01.ex04, 04.ex04, consolidation ex04 and ex08.
- Present-day or political: the cultural generalisations (poets' status, national melancholy and humour, language and identity) are all attributed ("sokak szerint", "a hagyományos felfogás szerint"); no present-day politician or party appears; the Soviet-era political jokes are not quoted. The reviewer should confirm Petőfi/Pilvax, the "sírva vigad a magyar" phrase and the Katona József Színház are still as described.
- 01.ex04: the sentence frame "nyelvtani alapjai évezredek óta változatlanok" remains a hard-to-defend claim about the grammar; I kept it because only the conjunction is tested (unsure).
- Challenges: the stories have no characters; scenarios use a learner in Budapest (café, literature class, pub, course end, farewell dinner).

## 5. Dictionary (literal compound guess / not in the dictionary), from the five audits
szigetnyelv | szigetnyelv | noun | island language |
tizenhárommillió | tizenhárommillió | number | thirteen million |
alapszókincse | alapszókincs | noun | core vocabulary |
állattartást | állattartás | noun | animal husbandry |
jövevényszavak | jövevényszó | noun | loanword |
kereszteződésében | kereszteződés | noun | crossroads, intersection |
kölcsönszavak | kölcsönszó | noun | loanword (borrowed word) |
nyelvtanulót | nyelvtanuló | noun | language learner |
rokontalanság | rokontalanság | noun | lack of kin, kinlessness |
halálmenet | halálmenet | noun | death march |
hivatástudat | hivatástudat | noun | sense of vocation |
ceruzacsonkkal | ceruzacsonk | noun | pencil stub |
eldöntésekor | eldöntés | noun | decision, deciding |
megbénultak | megbénul | verb | to become paralysed |
ostorozó | ostorozó | adjective | scourging, castigating |
szavalóversenyek | szavalóverseny | noun | recitation contest |
elvehetetlen | elvehetetlen | adjective | that cannot be taken away |
érzésvilág | érzésvilág | noun | emotional world |
alapmotívuma | alapmotívum | noun | basic motif |
bűnbánó | bűnbánó | adjective | penitent, repentant |
ikertestvére | ikertestvér | noun | twin sibling |
közmondásos | közmondásos | adjective | proverbial |
önironikus | önironikus | adjective | self-ironic |
önleleplező | önleleplező | adjective | self-revealing |
pártbürokráciával | pártbürokrácia | noun | party bureaucracy |
szívkamrájába | szívkamra | noun | heart chamber, innermost place |
abszurdizmusa | abszurdizmus | noun | absurdism |
allúziók | allúzió | noun | allusion |
átszövik | átsző | verb | to interweave |
kultikus | kultikus | adjective | cult (of a film or book) |
leleményességéé | leleményesség | noun | ingenuity |
reflexió | reflexió | noun | reflection |
mesterszint | mesterszint | noun | master level |

Fix count Unit 72: 92.
