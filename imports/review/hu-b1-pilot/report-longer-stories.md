# hu B1 Unit 1 `longer-stories` (b1-01-01 to b1-01-05, b1-01-consolidation, story b1-01-janosvitez)

The harness refused to let me write `/home/user/parlour-read-a/report-longer-stories.md` ("subagents should return findings as text"). This reply is the only copy of the report.

**Files written:**
- `/home/user/parlour-read-a/fixes-longer-stories.json`: 48 fixes. A dry run in memory (no files touched) showed every `old` occurs exactly once, every id exists, and the JSON stays valid. I did not run `check_fixes.py`, because it writes and restores files.
- `/home/user/parlour-read-a/challenges-longer-stories.json`: 6 challenges, one per lesson plus consolidation, with the same fields as `challenges.json`. Each `canDo` is the lesson's first checklist line, unchanged.

**Commands run** (from `/home/user/parlour-read-a`):
- `check-content.py hu b1 longer-stories` found 0 errors and 5 suspects. Those are consolidation-4 to -8, replays of lesson items. I left them alone, except consolidation-8, which gets the same fix as its source b1-01-05-practice-1.
- `render_lesson.js` ran for all six stems.
- `audit-reader-coverage.js --story b1-01-janosvitez --top 0` ran.
- `unmet-words.js` also ran for the six stems. I did not run `validate-content.py`.

## 1. Found by reading

**b1-01-01**
- b1-01-01-intro-2: wrong option *azóta* is first taught in b1-02-04 (unmet). Fix: *mindig*.
- b1-01-01-practice-4: "Which sentence correctly sets a scene, not an event?" offers *Mostanában ...* and *Jelenleg ...*. Both words are in no vocabulary list, and present-tense statements are not "events" anyway. Fix: "Which sentence opens a story about the past?" with *Most egy kis faluban lakunk.* and *Holnap egy kis faluban fogunk lakni.* (one fault each). Retagged, see 2.
- b1-01-01-dialogue-2: wrong option *Korábban egészen más lesz itt az élet.* is absurd after "Milyen volt itt korábban?". Fix: *Korábban egészen más voltak itt az élet.* (one agreement fault).
- b1-01-01-writing-1: the prompt says "you lived" but the stored answer is *laktunk*. Fix: "we lived".
- b1-01-01-check-2: english "life here was earlier completely different" is not English. Fix: "used to be completely different".
- b1-01-01-a-gr screen 1 says "the slot you already use for *tegnap* or *a következő nap*". *a következő* is taught in b1-01-02. Fix: *ma reggel*.
- b1-01-01-a-gr tip: "the way Spanish does" compares with a language other than English. Fix: removed.

**b1-01-02**
- b1-01-02-intro-1: wrong option *mielőtt* is taught in b1-01-03. Fix: *előtt*.
- b1-01-02-intro-2: wrong option *azután* is unmet (first taught in b1-karpatmedence-02). Fix: *aztán* (A2).
- b1-01-02-dialogue-1: wrong option *Mielőtt megérkezem, elmegyek sétálni.* uses *mielőtt* before its lesson and also changes the tense, so it has two faults. Fix: *Miután megérkezem, elmegyek sétálni.*
- b1-01-02-dialogue-2: Károly asks "Ki terítette meg az asztalt?" and Meg answers "Károly megterítette" to Károly himself. The wrong option *A következő héten Károly megteríti az asztalt.* is absurd. Fix: Petra asks, and the wrong option becomes *Én főztem, eközben Károly megterítettem az asztalt.* (one person-ending fault).
- b1-01-02-writing-2: nothing in the prompt cues *is*, but the stored answer is *Három e-mail is jött egymás után.* Fix: answer *Három e-mail jött egymás után.*
- b1-01-02-check-2: `answers` accepts *jövő*, but *a jövő héten* means "next week" from now and does not fit the past *felkeltünk*. Fix: only *következő*.

**b1-01-03**
- b1-01-03-intro-2: wrong option *kudarc* is taught in b1-01-04. Fix: *hangulat*.
- b1-01-03-practice-4: "A hős rájött, hogy...": *hős* is in no vocabulary list. Fix: "Anna rájött, hogy..." with "Anna realized/forgot/hoped that...".
- b1-01-03-dialogue-2: wrong option *Csak most jössz rá, ...* changes both person and tense and drops *elég*. Fix: *Csak most jövök rá, és ez elég meglepő volt.*

**b1-01-04**
- b1-01-04-a-gr: "*lezár* ... a transitive verb, so it needs a definite or indefinite object just like any other" is meaningless. Fix: "a transitive verb with the prefix *le-*, so it takes an object (*lezártuk a napot*)."
- b1-01-04-intro-2: wrong option *kinyit* is in no list. Fix: *elindul*. I avoided *becsuk*, because it would also mean "close".
- b1-01-04-controlled-4: wrong option *fordulópont* is a natural right answer ("nem kudarc volt, csak egy fordulópont"). Fix: *hangulat*.
- b1-01-04-dialogue-1: wrong option *Az eredmény az lesz, hogy senki nem volt elégedett.* is absurd, with two faults. Fix: *Az eredmény az lesz, hogy mindenki elégedett volt.* Also the prompt *Hogyan végződött a projekt?*: *végződött* is in no list (unsure). Fix: *Mi lett a projekttel?*
- b1-01-04-dialogue-2: wrong option *Igen, nem volt kudarc, nagyon sikeres volt.* uses *sikeres* (B2, unmet) and contradicts itself. Fix: *Igen, nem volt kudarc, inkább egy jó tanulság.* (unsure: a native might read "Igen, nem volt" as agreement).

**b1-01-05**
- b1-01-05-controlled-2: *Azóta is ____ emlékszem a hangjára.* has unmet *azóta*. *emlékszem* is in no list, and *emlékszik valamire* is B1 verb government -ra/-re. Fix: *Ez a részlet ____ megmaradt bennem.* / "This detail stayed vividly in my memory."
- b1-01-05-practice-1 (and its replay b1-01-consolidation-8): the order is illogical. "Miután elköltöztünk, minden megváltozott" comes before "Mielőtt véglegesen elmentünk, még egyszer visszanéztünk", so we move away before we leave. It also uses unmet words (*elköltözik, megváltozik, véglegesen, visszanéz, letelepedik*). Fix, identical on both items: *Akkoriban egy kis faluban laktunk. / Miután megérkezett a levél, elindultunk a városba. / Mielőtt hazamentünk, még sétáltunk a parkban. / Végül hazaértünk.*
- b1-01-05-practice-4: the wrong option "No connectors — just short, disconnected sentences" is absurd. The right option ("one or two at most") also disagrees with the lesson 4 tip ("two or three"). Fix: right "Only the connectors the job needs, a few at most"; wrong "Both miután and mielőtt in every single sentence".
- b1-01-05-dialogue-1: wrong option *Nem tudok most mesélni, mert nagyon sietek ...* is a natural reply to *Mesélj el egy hosszabb történetet!*. *hosszabb* and *apró* are unmet. Fix: Petra asks *Mi a lényeg a történetben?* / right *A lényeg az, hogy mindenki hazaért.* / wrong *A részlet az, hogy mindenki hazaért.*
- b1-01-05-dialogue-2: wrong option *Nem, a szerző itt lezárta a történetet, nincs folytatása.* is a natural answer to the yes/no question, and *visszamegyünk* is unmet. Fix: *Igen, a szerző már ír róla, szóval biztosan lesz folytatása.* / wrong *... biztosan nincs folytatása.*
- b1-01-05-writing-1: the stored answer says *nagyon élénken*, but the screen, builder and speaking item all use *különösen élénken*, and the prompt pins neither. Fix: prompt "particularly vividly", answer *Egy részlet különösen élénken megmaradt bennem.*
- b1-01-05-check-2: *szolgálja* is B2 and in no list. Fix: *Egy jó történetben minden ____ fontos.* / "In a good story, every detail is important."
- b1-01-05-reading-1: option 3 *Mert Jancsi katona akart lenni a faluban.* is not a plausible cause. Fix: *Mert Jancsi nem akart több libát őrizni.* (unsure).
- b1-01-05-reading-2: option *Az, hogy találkozott egy varázslóval.* is not in the story, and *varázsló* is unmet. Fix: *Az, hogy találkozott a huszárokkal.*
- Story, paras 3 and 5: *Mielőtt elindult volna ...* and *Mielőtt végleg útnak indult volna ...* use the past conditional (`past-conditional-volna`, B1 Unit 39). That contradicts lesson 3's "both verbs stay in plain past". Fix: *elindult*, *indult*.
- Story, para 3: *hogy elbúcsúzzon* is hogy + subjunctive (B1 Unit 5). Fix: *és elbúcsúzott*.
- Story, para 4: *kérte, hogy ne menjen messzire, ne hagyja el őt* is a reported command (B1 Unit 53). Fix: *kérte: „Ne menj messzire, ne hagyj egyedül a faluban!”* (unsure).
- Story comprehension question 1, *Mi a történet legfontosabb központi témája?*, is generic. Fix: *Mit csinált Jancsi napról napra a faluban?* with four new options and a new explanation drawn from para 1.

**b1-01-consolidation**
- b1-01-consolidation-9: *elsötétült, meglepődött, elsötétül, meglepődtünk* are in no list, and the wrong option mixes tenses. Fix: *Hirtelen jött a vihar, és ez nagyon meglepő volt.* / wrong *Hirtelen jön a vihar, és ez nagyon meglepő volt.*
- b1-01-consolidation-10, step 1: the prompt says "you lived" but the answer is *laktunk*. Fix: "we lived".
- b1-01-consolidation-11: *emlékszem* is unmet and drills -ra/-re government. Fix: "the end of the story stayed vividly in your memory" / *A történet vége élénken megmaradt bennem.*
- b1-01-consolidation-7 (*beugrott*, found only in lesson 3's own screen) is a copy of b1-01-03-practice-2. Left alone.

## 2. Metadata
- b1-01-01-practice-4: now `category` grammar, `teaches` past-tense-indefinite, `distractor_skills` {1: present-tense-routine-language, 2: fog-infinitive}. The wrong answers show the tense, not vocabulary.
- b1-01-01-dialogue-2: `teaches` b1-longer-stories-vocab becomes van-past, because the wrong option is now a form error.
- b1-01-02-dialogue-2: `teaches` b1-longer-stories-vocab becomes definite-past.
- b1-01-02-intro-1 and b1-01-03-intro-1 ("Which word means ..."): grammar/miutan-mielott becomes vocabulary/b1-longer-stories-vocab (rulebook § 3). Unsure, because the skill's words are what is asked.
- b1-01-consolidation-9: `teaches` past-tense-indefinite becomes irregular-past (*jött*), with `distractor_skills` {1: megy-jon}. Unsure.
- After applying the fixes, run `python scripts/lock_tags.py hu b1/longer-stories --update --reason "..."`.

## 3. Goals / checklists
- No sure defect. Lesson 1's fourth line, "four new scene-setting words", also covers *hangulat* and *leír*, which are not scene-setting words (unsure, no fix).

## 4. Doubtful
- Lessons 4 and 5 teach *Az eredmény az volt, hogy ...* and *A lényeg az, hogy ...* (az + hogy-clause). That is the B2 family `b2-cataphoric-clauses`, and the miután/mielőtt screens overlap `b2-temporal-framing`. Either the screens go beyond B1 or the B2 skills' level is wrong (unsure).
- The story has other later-B1 forms that I left, since they are not drilled:
  - *ahol* twice (B1 Unit 10) and *amíg* (B1 Unit 4).
  - *azonban* (B1 Unit 21).
  - Present participles *jóravaló, felemelő, megrázó* (B1 Unit 11).
  - Past participles *tiltott, elveszett, otthon maradt, vívott* (B1 Unit 3).
- Para 8's "egy könnyes búcsú a kapuban" does not match para 3, where they meet by the stream.
- The adaptation ends with Jancsi in Fairyland and never fulfils the promise "visszatér érte" that reading-3 asks about (unsure).
- Reading questions still use unmet story words (*liba, katona, tiltott, visszatér, elviszi, magával, elhatározta*). That is unavoidable when asking about the story.
- b1-01-02-controlled-4 puts an English parenthetical inside the Hungarian question: "(I showed it — the letter is definite)".
- b1-01-03-writing-1: *bezártam* and *becsuktam* are both natural, but only *bezártam* is stored. The fill-blank accepts both.
- Lesson 1, screen 2 example 3 and check-2 pair *amikor* with *korábban* ("Amikor a nagyapám fiatal volt, korábban ..."). Redundant, not wrong.
- b1-01-02-practice-4: wrong option *Először főztem, eközben megterítettem az asztalt.* might pass for some natives (unsure).
- b1-01-05-practice-3: the options' `inflected` forms lack the article the base sentence has (*eredmény* for *Az eredmény*).
- b1-01-04-practice-3: the second option also changes the sentence to *legközelebb korábban indulunk*, adding unmet words.

## 5. Dictionary
éktelen | éktelen | adj | awful, dreadful, monstrous |
elálmosodott | elálmosodik | verb | to become sleepy, to doze off |
észrevette | észrevesz | verb | to notice |
jóravaló | jóravaló | adj | decent, well-behaved, good-natured |
nagyvilágba | nagyvilág | noun | the wide world |
nagyvilágban | nagyvilág | noun | the wide world |
réges | réges | adj | ancient, very old (réges-régen: ages ago) |
gyöngyszemét | gyöngyszem | noun | pearl; gem, jewel |

**Fix count: longer-stories 48 (6 marked `"sure": false`).**