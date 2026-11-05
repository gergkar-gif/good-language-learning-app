# Reader A report: hu b2 elite-education (B2 Unit 20, culture track)

Files: fixes-elite-education.json (74 fixes: exercises 21, stories 23, grammar 9, goals/lessons 16, vocabulary 5), challenges-elite-education.json (6), facts-elite-education.md. Commands run: check-content (10 errors, all addressed), render_lesson (no `!!`), unmet-words (about 110 hits; vocabulary fixes), audit-reader-coverage for the five stems. The stories have no `questions`; the lessons' ex08 items are the reading questions (none copies a story question).

## 1. Found by reading
- seg 01: Neumann "a few years after" Wigner is wrong (near contemporaries) and "founder of modern computer science" overclaims; "érettségizik" in a past narrative -> subjunctive; Wigner's portrait in Princeton and "úgy érezte" are unverified anecdote / mind-reading -> hedged; L01 ex07's question rests on the portrait -> rewritten. (unsure for the dates and Szegő)
- seg 02: "felismerték" (mind-reading); "Trefort ezért Lipcsébe küldte" (who sent Kármán, and when, is not certain) -> neutral wording; anecdote of the six-year-old Tódor hedged; "mindketten kiemelték" (Teller, Polányi) unverified; "egyenrangúként", "a tanárképzés bölcsője" overclaim. (unsure)
- seg 03: "legendásan szigorú", "Európa egyik leggazdagabb szakkönyvtára", "kizárólag a tudománynak" overclaim; the Ménesi út building came after 1895 -> "később"; Kosztolányi was not a Collegium member (Kodály, Babits, Szekfű were) and "kortársai" made no sense; "within a decade the level of Hungarian secondary education rose" is unsupported -> removed; Bartoniek, the translation seminars and the language requirement: check. (unsure)
- seg 04: typo "a ezeréves"; the thousand years belong to the abbey; the orders were dissolved in 1950, not 1948; Pannonhalma and Győr are Benedictine, not "Piarist or Franciscan"; AKG founder name unverified -> removed; "poroszoktól örökölt" unsupported; church restitution and the present mix of schools: hedged / check.
- seg 05: "készíttetik fel" for teachers who prepare pupils themselves is wrong -> "készítik"; "négyszeres-ötszörös" figure unsupported (also L05 ex03 "ötszörös"); "igazi titka soha nem" -> softened; "mentoráltat" is an odd causative (unsure, kept, a real use of the lesson's pattern). Present-day entrance rules and programmes: check.
- Grammar screens: L01's causative rule list was wrong (*megold → megoldat* listed under -tat/-tet; "consonant + t" monosyllables like *fest* take -et) -> rewritten (unsure, check); L02's example *fárasztotta* is not a causative -> replaced; L03 screen title "Agentless ..." names a later unit's topic -> renamed; L05 tip derived *tehetséggondozás* from a causative -> replaced.
- check-content errors fixed: length-giveaway L01.ex02, L02.ex02, L02.ex04, L03.ex08, L04.ex02, L04.ex04, L05.ex02, consolidation.ex02; tell-absolute (Kizárólag) L01.ex02, L02.ex02. Suspects: option-language L02.ex04 and consolidation.ex02 (English stems with English options: the options are rewritten to plausible misconceptions); consolidation-copy ex05 (a replay, accepted).
- Absurd wrong options replaced with plausible one-fault ones: L01 ex08, L02 ex02, ex04, ex08 (Bolyai/Kőrösi Csoma/Kempelen/Jedlik), L03 ex02, ex04 (scrambled non-sentence), ex08, L04 ex02, ex04, ex08, L05 ex02, consolidation ex02, ex08.
- Two right answers: L03 ex07 (*helyezte* is natural next to *helyeztette*) and L05 ex04 (*készítették* with *magántanárral*) -> the wrong options now carry one clear fault (indefinite conjugation; number / tense).
- L02 ex06: "Az édesapja ..." had no antecedent -> Kármán Mór and his son.
- L01 goal 1 and the intro: "Rátz és Mikola" (Hungarian *és* in an English line); the intro says "you will master causative verb derivation" (Unit 19 material) -> "revisit".
- Vocabulary: unmet hits added to the first lesson that uses them (01: 6; 02: 11; 03: 17; 04: 3; 05: 14). Not added: inflected forms the tool flags although the lemma is listed (*gyakorlóiskolában*, *vehettek* of *részt vesz*). I did not run unmet-words on my own replacement texts; the reviewer should (new words: *diktált*, *másoltatta*, *tankönyv*, *haladjanak*, *vegyék ki*).

## 2. Metadata
- L01 ex03 (fill-blank, answer *vezettette*): tested form is the causative -> `causative-verbal-derivations`, category `grammar` (was unit vocabulary).
- L04 ex06 (builder *hagyták, hogy ... szerkesszenek*): tests *hogy* + subjunctive -> `hogy-jon-jen` (B1 Unit 5); category stays `grammar`.
- All other grammar items carry `causative-verbal-derivations` (B2 Unit 19, known); no `distractor_skills`. Run lock_tags after applying.

## 3. Goals / checklists
- Goal line 1 of L01-L05 was a template ("nurtured scientific talent", "trace the historical shifts ... through 1948 nationalization to 1989", "analyze contemporary ... debates"): rewritten as plain can-do lines (also the challenge canDo). L03 line 2 listed *alapíttat, pályáztat*, which the lesson never uses -> *építtet, helyeztet, fordíttat*. L05 line 2 drops "fluently".
- Recap screens: all five grammar screens present B2 Unit 19 (causatives) as new; L04 also *hagy / enged, hogy* + subjunctive (B1 Unit 5). Each now opens with "You know ... from B2 Unit 19". The L01 intro likewise.

## 4. Doubtful
- Causative rule in L01 (-at/-et vs -tat/-tet) and the claim that *-val/-vel* marks the causee of a transitive base always: unsure, ask a native.
- Facts marked check in facts-elite-education.md: Kármán's Leipzig trip, Bartoniek, the Ménesi út building date, 1950 dissolution, AKG, present-day entrance procedure, scholarship programmes.
- L02 ex08: Szilárd Leó and Gábor Dénes as non-Minta pupils: check.
- L05 ex02: the right option now states the risk as the segment does ("kedvezhet"); the question asks for a "veszély".
- No later-core skill is taught as its own; no C1 forms found.

## 5. Dictionary
fizikatanár | fizikatanár | noun | physics teacher |
tanárképzés | tanárképzés | noun | teacher training |
emeltetett | emeltet | verb | to have (a building) erected |
tehetséggondozás | tehetséggondozás | noun | nurturing of talent |
világszínvonalú | világszínvonalú | adjective | world-class |
oktatáspolitika | oktatáspolitika | noun | education policy |
oktatástörténet | oktatástörténet | noun | history of education |
készíttetik | készíttet | verb | to have (something) made or prepared |
nyolcosztályos | nyolcosztályos | adjective | eight-form, eight-year |
túljelentkezés | túljelentkezés | noun | oversubscription |
érettségizik | érettségizik | verb | to sit the school-leaving exam |
felekezetű | felekezetű | adjective | of a given denomination |
különóra | különóra | noun | extra lesson |
szakmunka | szakmunka | noun | specialist work, professional literature |
elemeztet | elemeztet | verb | to have (something) analysed |
fejszámolási | fejszámolás | noun | mental arithmetic |
főgimnázium | főgimnázium | noun | upper-secondary grammar school |
gyakorlóiskola | gyakorlóiskola | noun | practice school for trainee teachers |
kísérleteztet | kísérleteztet | verb | to make (someone) experiment |
tanárjelölt | tanárjelölt | noun | trainee teacher |
vezetőtanár | vezetőtanár | noun | mentor teacher |
vitatkoztat | vitatkoztat | verb | to make (someone) debate |
bentlakásos | bentlakásos | adjective | residential, boarding |
elitkollégium | elitkollégium | noun | elite residential college |
érdemelvű | érdemelvű | adjective | merit-based |
helyeztet | helyeztet | verb | to have (someone) placed or posted |
kollégista | kollégista | noun | college resident |
műhelymunka | műhelymunka | noun | workshop work |
szakkönyvtár | szakkönyvtár | noun | specialist library |
szentel | szentel | verb | to devote |
államosíttat | államosíttat | verb | to have (something) nationalised |
piarista | piarista | adjective | Piarist |
sárospataki | sárospataki | adjective | of Sárospatak |
gondolkodású | gondolkodású | adjective | -minded |
elitgimnázium | elitgimnázium | noun | elite gimnázium |
felvételiztet | felvételiztet | verb | to examine (applicants) at entrance |
felzárkóztatás | felzárkóztatás | noun | remedial support |
motivált | motivált | adjective | motivated |
mentoráltat | mentoráltat | verb | to have (someone) mentored |
oktatásszociológus | oktatásszociológus | noun | sociologist of education |
szakkollégium | szakkollégium | noun | specialist college |
tehetségműhely | tehetségműhely | noun | talent workshop |

Fix count: 74 (exercises 21, stories 23, grammar 9, goals/lessons 16, vocabulary 5).
