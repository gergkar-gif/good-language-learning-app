# Reader B, hu b2 Unit 70 knowledge-economy (culture track)

Fix file: fixes-knowledge-economy.json (127 fixes). Challenges: challenges-knowledge-economy.json (6). Facts: facts-knowledge-economy.md. Nothing was tested (per the brief); the fixes were written against the files as they stand.

## 1. Found by reading
- s01 p1 "2023 őszén a világ tudományos közvéleménye ... figyelt": overstated, announcement was in October; BME renamed to its full present name (BME also in s03). Fixed (unsure on degrees: facts).
- s01 p3 "mindig szoros kapcsolatot ápolt a hazai tudományos élettel. Meggyőződése szerint ...": unsourced mind-reading; replaced by a plain statement; "a bécsi egyetemen és a müncheni ... Intézetben": institute is in Garching, Vienna was the technical university (check).
- s01 p4/p5: "lehetővé teheti ... még azelőtt, hogy a klinikai tünetek megjelennének", "hatalmas lendületet adott", "bizonyítja": hedged as the researchers' hope / softened.
- s02 p1-2: ranking claims ("legmodernebb", "a kontinens legjelentősebb beruházásai közé"), "Prága és Bukarest mellett" (the other pillars are near them), and lasers that recreate conditions inside stars (unsupported for ELI-ALPS); fixed.
- s02 p3-5: "mérnöki csoda", earthquakes and tenth-of-a-degree figure, "nyílt hozzáférésű nemzetközi konzorcium", "felbecsülhetetlen", Science Park as an existing ecosystem (a plan; check): softened.
- s03 p1: NYTK/BME present names (check HUN-REN). s03 p3: "Ha a mondat elején áll a fókusz ... teljesen megváltoztatja ... jelentését": focus is the word before the verb and changes emphasis; fixed. s03 p4: "garantálják a nemzeti digitális szuverenitást" (present-day policy claim) and ungrammatical "kizárólagos függősége helyett": rewritten and attributed to the developers. s03 p5: "bizonyítják", flat counterfactual: hedged.
- s04 p1: "ázsiai és európai autóipari óriások" (the plants belong mainly to battery makers), "alapjaiban alakítva át"; p2 promises attributed to supporters; p3 water and energy demand attributed to the concerns; p4 "elérte az országos csúcsfogyasztás szintjét" given with no year or source: dated to the 2020s and hedged (check).
- s05 p3: "A ... Akadémia határozottan küzd e folyamat ellen", "szolgalelkű idegennyelv-használat": present-day language-policy judgement removed, the loanword debate named in one line (check the Academy's role). p4: "demokratikus társadalom alapfeltétele" attributed to linguists; C1 "Feltéve, ha" replaced by *Amennyiben*. p5 "évezredeken át": fixed. p1 speaker figure marked as an estimate.
- Lesson 01 intro body[0]/[2] ("stratégiai csomóponttá válhat", the promise of feltéve, ha and hacsak nem, "megvalósulhatott volna"); lesson 03 goal "*ha lett volna..., akkor...*" shows a wrong pattern; fixed.
- Grammar 01 table/tip (C1 form), 02 (hacsak nem and a tip about double negatives), 04 tip invented an indicative/subjunctive distinction between *azzal a feltétellel / azzal a kikötéssel* (replaced, unsure), 05 tip "marks the transition to C1 mastery": rewritten.
- Reading items: 01.ex08 asked for a claim the story does not make ("összes kémiai kötés"), 05.ex08 for "the Academy considers it a national priority" (not in the story): replaced by questions the stories answer. 01.ex02, 02.ex02, 02.ex08, 03.ex02, 03.ex08, 04.ex02, 04.ex08, 05.ex02 had absurd wrong options (Mars, steam engines, deep-sea reefs, submarines, polar frost, rain stopped by solar panels, forbidden vowels): replaced by plausible wrong claims that the stories contradict.
- Items with two faults or acceptable replies: 03.ex04 option 4 (*nem volna lett képes*), 03.ex07, 04.ex07 option 2 (natural reply), 05.ex07 option 2, 01.ex07, 02.ex07, consolidation ex06, ex07, ex09 (wrong options were non-forms): rewritten with one fault each; 02.ex03 accepts both *tiszta terekben* and *tiszta terekbe* (elhelyez takes both).
- check-content ERRORs: 01.ex02 and 02.ex08 length give-aways, tell-absolute in 02.ex08, 05.ex02, 05.ex08: all rewritten. Suspect answer-in-prompt 03.ex05 (*volna*): blank moved to *befejezték* with a hint. Suspect recap-unmarked 05-a-gr: the screen is now a marked recap.
- Stems with Hungarian grammar terms (*kötőszó*, *ellenfaktuális*, *összetett feltételes kifejezés*) in 01/02/04/05/consolidation: replaced by *Melyik szó illik a mondatba?* and plain questions.
- Present-day or policy statements in items: 03.ex03 ("elengedhetetlen"), 03.ex07 / consolidation ex09 ("kiszolgáltatottá válnánk", "garantálja"): attributed or softened.
- Consolidation ex02 asked for "legmagasabb szintű" research infrastructure (ranking) and had absurd options: rewritten with real institutions.
- Lesson files carry `"unit": 35` while the course lists this as Unit 70 (not fixed; flag for the reviewer).

## 2. Metadata
- 01.ex04, 02.ex04, 05.ex04, consolidation ex04 and ex08: conjunction choice, retagged `category: vocabulary`, `teaches: b2-knowledge-economy-vocab` (the wrong answers show a meaning, not a grammar form; wrong tag past-conditional-volna).
- 01.ex05 (*azzal*), 04.ex04 (*azzal/annak/ebben/arról*), 04.ex05 (*Abban*): `case-inflected-pronouns`, grammar.
- Builders and fills on *amennyiben* / *azzal a kikötéssel* (01.ex06, 02.ex05, 04.ex06, 05.ex05, 05.ex06, consolidation ex05, ex10) and dialogues 01.ex07, 02.ex07, 04.ex07, consolidation ex06, ex07, ex09: vocabulary (the item no longer tests the past conditional). 04.ex07 and 01.ex07 and consolidation ex07 carry `distractor_skills` index 1 `participle-actions` (the *-va/-ve* form is a real form of that skill).
- 03.ex07 and 05.ex07: `hypothetical-ha-conditional` (the wrong options break the *ha*-conditional pairing).
- consolidation ex12 open writing: unit vocabulary. Items that keep `past-conditional-volna`: 03.ex04, 03.ex05, 03.ex06, consolidation ex11 (the form tested).
- Lock after applying: `python scripts/lock_tags.py hu b2/knowledge-economy --update` (reviewer).

## 3. Goals / checklists
- Every goal line exists three times per lesson file (top `goal`, goal section, checklist): each rewritten line is a set of three fixes. Rewritten: 01 [1], 02 [1], 03 [1], 05 [1] and [2], consolidation [1]. 01 [1] and 02 [1] promised C1 or unknown forms (*feltéve, ha*, *hacsak nem*); 03 [1] showed *ha lett volna*; 05 [2] asked the learner to advocate a policy position; consolidation [1] "effortlessly deploy multi-layered".
- The first lines of all six lessons are plain can-do lines already; the challenges copy them as `canDo`.
- Lesson `grammar` lines of 01 and 02 and the screen titles in the lesson files were rewritten to match the grammar files.

## 4. Doubtful
- **C1 forms (group 4 per brief):** lessons 01 and 05 taught *feltéve, ha* (C1, `felteve-hogy-kiveve-ha`) in screens, items, goals, speaking and the story (05 p4); rewritten with *amennyiben* / *azzal a feltétellel, hogy*. 26 hits from check_c1_forms.py (01: ex04, ex07, screens, goals, intro; 05: ex04, screen, example; consolidation: ex04, ex06 prompt text, ex12) are all covered.
- ***hacsak nem*** (lessons 02 and 05): on no earlier core screen (only on C1 screens); rewritten to *amennyiben ... nem*, tip replaced. The reviewer may want to confirm with the user whether lesson 02 should keep it.
- **This culture unit replays Unit 69's grammar** (amennyiben, abban az esetben, ha, azzal a feltétellel, hogy, counterfactual stacking): recap lines added in 01, 02, 03, 04, 05 (B2 Unit 13, B1 Unit 67, B1 Unit 39, B2 Unit 69 from the sheet); *azzal a kikötéssel, hogy* is not on the sheet and stays as lesson 04's one new phrase (unsure).
- Present-day facts all marked "check" in facts-knowledge-economy.md: ELI-ALPS set-up and Science Park, HUN-REN NYTK name, PULI, battery plant operators and zone, solar capacity figure, Academy role, speaker count.
- Not fixed: the skill tag `b2-speculative-conditionals` in the stories is an alias of `past-conditional-volna`, which does not fit lessons 01, 02, 04, 05 (they now teach no new skill; the unit vocabulary tag was used on items).
- Challenges: the stories have no characters, so each scenario uses a role in the unit's setting (student in Mór, researcher in Szeged, linguist in Budapest, engineer in Debrecen).
- Unsure fixes carry `"sure": false`.

## 5. Dictionary (literal compound guess / not in the dictionary), from the five audits
csúcsteljesítményű | csúcsteljesítményű | adjective | high-performance |
lézerközpont | lézerközpont | noun | laser centre |
tizedfokos | tizedfokos | adjective | of a tenth of a degree |
szabályalapú | szabályalapú | adjective | rule-based |
akkumulátoripar | akkumulátoripar | noun | battery industry |
csúcsfogyasztás | csúcsfogyasztás | noun | peak consumption |
napelem | napelem | noun | solar panel |
napenergia | napenergia | noun | solar energy |
talajvíz | talajvíz | noun | groundwater |
géntechnológia | géntechnológia | noun | genetic engineering |
idegennyelv-használat | idegennyelv-használat | noun | use of foreign languages |
klímaváltozás | klímaváltozás | noun | climate change |
nyelvstratégia | nyelvstratégia | noun | language strategy |
tizennégymillió | tizennégymillió | number | fourteen million |
elektronmozgások | elektronmozgás | noun | electron movement |
kimerevítették | kimerevít | verb | to freeze (a moving image) |
lézerimpulzusok | lézerimpulzus | noun | laser pulse |
meghódíthatók | meghódít | verb | to conquer |
móri | móri | adjective | from Mór |
szárnycsapását | szárnycsapás | noun | wingbeat |
anyagtudósokat | anyagtudós | noun | materials scientist |
fénysűrűséget | fénysűrűség | noun | light intensity |
hozzáférésű | hozzáférésű | adjective | having (a kind of) access |
létrejövő | létrejövő | adjective | emerging, coming into being |
lézeres | lézeres | adjective | laser-based |
precíziós | precíziós | adjective | precision |
rezgésmentes | rezgésmentes | adjective | vibration-free |
startupok | startup | noun | start-up company |
tudástranszfert | tudástranszfer | noun | knowledge transfer |
ultrarövid | ultrarövid | adjective | ultrashort |
vendégkutatókat | vendégkutató | noun | visiting researcher |
annotált | annotált | adjective | annotated |
értő | értő | adjective | understanding, skilled |
fókuszszabályok | fókuszszabály | noun | focus rule |
igetőből | igető | noun | verb stem |
neuronális | neuronális | adjective | neural |
pragmatikai | pragmatikai | adjective | pragmatic |
szövegkorpuszok | szövegkorpusz | noun | text corpus |
szuperszámítógépeken | szuperszámítógép | noun | supercomputer |
támaszkodhasson | támaszkodik | verb | to rely on |
techóriások | techóriás | noun | tech giant |
tokenizálókra | tokenizáló | noun | tokenizer |
akkumulátoros | akkumulátoros | adjective | battery-based |
cellagyártáson | cellagyártás | noun | cell manufacturing |
energiatárolókat | energiatároló | noun | energy storage unit |
koncentrálódik | koncentrálódik | verb | to be concentrated |
kulcseleme | kulcselem | noun | key element |
robbanásszerű | robbanásszerű | adjective | explosive, very rapid |
tőkeberuházásokkal | tőkeberuházás | noun | capital investment |
alapfeltétele | alapfeltétel | noun | basic precondition |
folklórhasználatra | folklórhasználat | noun | use as folklore only |
jövőkutatók | jövőkutató | noun | futurologist |
kultúrnyelv | kultúrnyelv | noun | cultured (standard literary) language |

Fix count Unit 70: 127.
