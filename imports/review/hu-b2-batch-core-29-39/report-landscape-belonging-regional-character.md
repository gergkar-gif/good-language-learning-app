# Unit 37 landscape-belonging-regional-character (b2-19)

Checks run: check-content (12 errors, 0 suspects), render_lesson (no `!!`), audit-reader-coverage, unmet-words (about 190 hits). Fixes: fixes-landscape-belonging-regional-character.json (86 fixes), challenges: 6. Replacement sentences reuse words that unmet-words did not flag; not re-run (told not to test).

## 1. Found by reading
- b2-19-03 grammar tip and items: fine factually (*felmegy/lemegy*). Dialogue-2 said *felköltözik a városokba* (*fel* is for the capital only) with wrong options *leköltözik a fővárosba / költöznek le*; rewritten with *fővárosba* and one-fault options.
- Dialogues 19-01 to 19-05, consolidation-8: wrong options had two to three faults (e.g. *Elmegyek vidékben*, *a folyónak innen* with *mentében*, *Nyírségen ... alkot ... alkotnának ... arculattal*, word-salad options in 05 controlled-2/-3 and consolidation-1); each wrong option now changes one thing (case on the noun, or position of the postposition).
- b2-19-04 vocabulary *cíviselem* ("Civis burgher") is not a Hungarian word I can confirm; the word for the Debrecen burghers is *cívis*. Replaced in the vocabulary file (unsure), in 19-04-intro-1, and options in 19-01-check-2 and 19-03-check-2. Also in b2-20-05-ex.json (Unit 39 file) and generated files content/hu/decks/decks.json and content/hu/indexes/word-lesson-index.json (rebuild).
- b2-19-04 grammar screen presented -ban/-ben and -on/-en/-ön as new: now "You know ... from A1". Also the jargon "cognitive spatial models" removed.
- b2-19-02 grammar contrasts *keresztül*: added "you know *keresztül* from B1 Unit 15" (unsure, the sheet names Unit 15 for *felé/felől*; the B1 screen title lists *keresztül, át*).
- b2-19-05: goal line "critically interpret Illyés Gyula's literary portrait ... in Puszták népe" (appears in the lesson file's goal, goal section and checklist) presents the story as the book: reworded "as the story shows it" in all three places. Dialogue-2 and the three reading questions said "Illyés leírása szerint", "Puszták népe": now "a történetben / a történet szerint". Story comprehension question 1 and its explanation (story file) said "Illyés Gyula szociográfiájának ... Illyés műve": reworded to "a történet".
- 19-05 writing-2 prompt "evaluating Illyés Gyula's portrait" and answer "Illyés Gyula könyvében" replaced by a sentence about the servants in the story.
- Unmet words: all hits rewritten (01 controlled-4, practice-2/3/4, dialogues, writing, check-1; 02 controlled-4, practice-2/3/4, dialogues, writing, check-1; 03 practice-1/2/3, dialogues, writing, check-1/-2; 04 controlled-3/4, practice-1/2/3, dialogues, writing, check-1; 05 controlled-2, practice-1/3, dialogues, writing, check-1, reading 1-3; consolidation-1/3/4/5/7/8/12).
- check-content errors fixed: length-giveaway 03 intro-1, 04 intro-1, 05 intro-1, 05 reading-1/-2/-3, consolidation 3/7/9; tell-absolute *Kizárólag*, *teljesen* (reading options rewritten).
- 19-05-check-2 (13 vs 9) and 19-05-practice-4: not changed, see 4.
- 19-02-check-2 and 19-01-check-2 wrong options *cselédség*, *cíviselem* were words from later lessons: replaced.
- Hints: no arrow hints; hints now name base word and role.

## 2. Metadata
- All grammar items carry `b2-spatial-postpositions`, which 19-01 teaches. But 19-03 tests fel/le/ki/be (directional-preverbs, known; getting-on-and-off-fel-and-le exists too) and 19-04 tests -on/-ban on region names (`on-en-on`, `ban-ben-in`, A1). Retagged 19-03 controlled-2/3/4, practice-1/2, check-1, dialogue-1/2 and consolidation-6 to `directional-preverbs`; 19-04 controlled-2/3/4, practice-1, check-1, dialogue-1/2 to `on-en-on` / `ban-ben-in` (all sure:false; category is already grammar/dialogue; lock_tags update needed).
- 19-01-check-2 etc: no change.

## 3. Goals / checklists
- 19-05 goal line fixed (see 1). 19-03 goal "conventional Hungarian directional preverbs (fel/le, ki/be)" is a known-skill goal; fine. Checklist/goal jargon ("argument structure"-style) in 19-05 line 1 "integrate advanced spatial postpositions and descriptive adjectives into ethnographic essays" is more than the lesson practises (unsure).
- Challenges: 6 written (the lesson challenge screens are generic placeholders). Characters used: Gyula (young writer) and the old farmhand of the story.

## 4. Doubtful
- Lesson b2-19-03 is built on directional preverbs (the figurative *fel/le* for capital and provinces is close to `b2-figurative-preverbs`, taught in Unit 55); retagged to the known `directional-preverbs`, content kept (about 9 items, unsure).
- Lesson b2-19-04 is a region-case lesson tagged with the postposition skill; retagged (see 2).
- Story narration last paragraph "tette Illyés Gyula remekművét ... szociográfiájává" presents the scene as the book itself; the story `source` is relabelled by the reviewer, the narration line is story text and left (unsure).
- 19-05-check-2 (13 vs 9): *összetartozás* vs *látóhatár*, *székhely*: word lengths; left.
- 19-04 "Veszprém ... székhely" (practice-4) and the unflagged *Békésben* removed; *megye* wording fine.
- 19-03 grammar example 4 ("connect into the central bloodstream") is an odd metaphor; left.
- 19-04 tip "names ending in -föld ... *always* take -on" fine.
- Present-day check: *Tolna megyei* now removed from items; counties are *megye*.

## 5. Dictionary
cselédkönyv | cselédkönyv | noun | servant's record book (the booklet that bound a farmhand to the estate) |
kenyérkereset | kenyérkereset | noun | earning one's daily bread |
látóhatár | látóhatár | noun | horizon |
mezőföld | Mezőföld | noun | Mezőföld, a plain region in Transdanubia |
nagybirtok | nagybirtok | noun | large estate |
adomák | adoma | noun | anecdote, funny tale |
árokpartot | árokpart | noun | ditch bank |
cselédházak | cselédház | noun | farmhands' house |
cselédsorsot | cselédsors | noun | the fate of a farmhand |
dűlőút | dűlőút | noun | field track |
jegenyefasorokon | jegenyefasor | noun | row of poplars |
körforgásból | körforgás | noun | cycle, circulation |
kukoricaszárakat | kukoricaszár | noun | corn stalk |
kútágasok | kútágas | noun | well sweep (pole of a draw-well) |
lankáin | lanka | noun | gentle slope |
lépteink | lépte | noun | footstep (usually lépés) |
mázsáit | mázsa | noun | quintal, 100 kg weight |
ökrös | ökrös | adjective | drawn by oxen |
padlójú | padlójú | adjective | with a floor of a given kind |
rácegrespusztai | Rácegrespuszta | noun | Rácegrespuszta, an estate in Tolna |
simontornyai | Simontornya | noun | Simontornya, a town in Tolna |
szekérutak | szekérút | noun | cart road |
szociográfiájává | szociográfia | noun | sociography |
talpalatnyi | talpalatnyi | adjective | a foot's breadth, tiny (of land) |
tanúságtétellé | tanúságtétel | noun | testimony |
uraság | uraság | noun | the gentry, the lord of the manor |
urasági | urasági | adjective | of the manor lord |

Fix count: 86 fixes (plus 6 challenges).
