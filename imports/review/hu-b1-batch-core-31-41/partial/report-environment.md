# Reader A report: hu b1, batch core 31-41 (Units 31, 33, 35)

Each unit's fixes and challenges are written to its own files in `/home/user/parlour-read-a` before the next unit was started. `old` texts were checked for uniqueness only while building the lists (no `check_fixes.py`, no apply script).

---
## UNIT 31 environment (b1-16-01 .. 05, consolidation; story b1-16-gardonyi)

Unit 31 teaches three skills: `causal-postpositions` (b1-16-02-a), `noun-compounds` (b1-16-02-b) and `nominalization` (b1-16-04-b). Everything else in it is known: lessons 1, 3, 5 and the first screen of 4 are recaps. Files: `fixes-environment.json` (89 fixes), `challenges-environment.json` (6).

### 1. Found by reading
- b1-16-01-a-gr (*ezért and így*), b1-16-01-b-gr (*kell* + inflected infinitive, "subjunctive clauses"), b1-16-03-a-gr (*ha*), b1-16-03-b-gr (-ódik verbs), b1-16-04-a-gr (*azért, hogy*), b1-16-05-a-gr (*szokott*), b1-16-05-b-gr (*véleményem szerint*) present A1/A2/B1 forms as new (A1 Unit 24, A2 Units 41, 13, 28, 31, 12, 29; A1 Unit 17; B1 Unit 5). Fix: each rewritten as "You know … from Unit N" with the new context.
- b1-16-03-a-gr uses the past conditional with *volna* (*Ha korábban elkezdtük volna*; B1 Unit 39, later) and unmet *erodálódni*. Fix: recap of *ha* with present and *ha* + conditional (*lenne*).
- b1-16-01-b-gr example 1 and b1-16-01.ex07 use the verbal noun *megőrzéséért* (taught b1-16-04-b); b1-16-02-a-gr example 2 uses *elégetése* (same). Fix: new example *Sokat kell tennünk a környezetvédelemért.* and a new builder; example 2 of 02-a replaced.
- b1-16-02-b-gr called *ökológiai lábnyom* (adjective + noun) a compound noun, gave no hyphen rule and nothing on the possessive half of `noun-compounds`. Fix: rule for one-word compounds, hyphens for three or more parts, adjective stays separate, possessive *-a/-e* example.
- b1-16-04-b-gr named *energiatakarékosság* (takarékos + -ság) as an -ás/-és verbal noun and gave no -ás/-és rule. Fix: vowel-harmony rule with *tanulás, olvasás, pihenés, újrahasznosítás, étkezés*; example 1 replaced.
- b1-16-05-a-gr example 2 (*Igyekszem … vásárolni*) has no *szokott* + infinitive, the pattern the screen states. Fix: *Hetente többször szoktam helyi termelőktől vásárolni zöldséget.*
- Glued blanks: b1-16-02.ex11 (*üvegház____*), ex12 (*ökológiai ____ot*), b1-16-04.ex09 (*újrahasznosít____* + *ás*). Fix: whole-word blanks.
- Reading-category items with no text, absurd wrong options and a tell or length give-away, replaced by grammar or vocabulary items: b1-16-01.ex08, 02.ex08, 03.ex08, 04.ex08, 05.ex08, consolidation.ex08.
- check-content ERRORs, all fixed: length-giveaway b1-16-01.ex05, 01.ex08, 05.ex08, consolidation.ex02; tell-absolute b1-16-05.ex05 (*Soha*).
- Wrong options that are garbled non-phrases with two faults: b1-16-01.ex02, 03.ex02, 04.ex02, 05.ex02, consolidation.ex02. Fix: one fault each (*ezért* for *mert*, *hanem*, *miatt* alone, *emiatt* for *miatt*).
- b1-16-02.ex02: wrong option 3 fails by an accusative (*a Földet*), a second skill, and the item is tagged `mert-because` but tests *emiatt* vs *miatt*. Fix: connector-only faults, retag.
- English glosses used as `english` on builders: b1-16-02.ex07, consolidation.ex05 said "Build the sentence in the correct order." Fix: translation.
- Hungarian metalanguage and "(Lesson N)" in stems (*Melyik mondat fejezi ki helyesen…*): b1-16-01.ex02, 02.ex02, 03.ex02, 04.ex02, 05.ex02, consolidation.ex02. Fix: English stems.
- b1-16-01 vocab *szelektív hulladékgyűjtés = selective waste collection, recycling*: "recycling" is *újrahasznosítás* (lesson 4, and the consolidation matching). Fix: "separate waste collection (sorting waste)" in the list and in ex01.
- Unmet words: every id in the `unmet-words.js` list has a fix: b1-16-01 ex02 ex03 ex04 ex05 ex08; 02 ex03 ex04 ex05 ex06 ex08 ex11; 03 ex02 ex05 ex07 ex08; 04 ex03 ex04 ex05 ex06 ex07 ex08 ex09; 05 ex02 ex03 ex05 ex06 ex08; consolidation ex02–ex08. Words with no list at all (*kőolaj, hulladékkezelés, termelünk, szemetet, műanyag, kezelik, elégetik, ültetni, takarítunk, fosszilis, tüzelőanyagot, égve, hagyunk, szennyezettsége, megszűnjön, gazdálkodó, áruházláncokból, villany*) are all rewritten out, not added to lists.
- STORY b1-16-gardonyi: question 1 asks for the "central idea" (generic). Fix: *Mit mond a tanító az erdőről az öreg erdésznek?* with options about the forest. Questions 2 and 3 are fine.

### 2. Metadata
- b1-16-02.ex02 `mert-because` → `causal-postpositions` (tests emiatt).
- b1-16-02.ex08, 03.ex08: category reading → vocabulary, `b1-environment-vocab` (new items are meaning items).
- b1-16-02.ex12: `noun-compounds` → `b1-environment-vocab` (a fill-blank supplying a noun).
- b1-16-01.ex08: reading → grammar, `inflected-infinitives`; b1-16-03.ex02 and consolidation.ex08 → `ha-clause`; b1-16-04.ex08 and consolidation.ex04 → `azert-hogy-purpose`; b1-16-05.ex08 → `szokott-infinitive-habitual-actions`.
- b1-16-04.ex03: vocabulary → `nominalization` (lesson 4 had one item for its new skill). b1-16-04.ex09 stays `nominalization`.
- No `distractor_skills` on any new option (every wrong option is a connector fault or a non-form). Run `lock_tags.py … --update` after applying.

### 3. Goals / checklists
- All five lessons shared lines 2–4 ("form causal and result clauses using ezért and emiatt", "discuss environmental issues, conservation, and sustainable habits", "master four new target vocabulary items in authentic context") and line 1 was a garbled "vocabulary for one has to….". Lessons 1, 3, 4, 5 never teach *emiatt*. Fix: four lesson-specific lines each, in both places in the lesson JSON (`goal` and the Lesson Goals section).
- The lesson `grammar` line was identical in all five lessons ("Causal and Consequence Connectors (ezért, emiatt, aminek következtében)"). Fix: one per lesson. Consolidation has no checklist; its challenge `canDo` is a unit line.

### 4. Doubtful
- *aminek következtében* uses a case-inflected relative (`vonatkozoi-nevmas-esetei`, B1 Unit 21, later). It is the taught chunk of b1-16-02-a, so left (unsure); *ennek következtében* would avoid it.
- b1-16-04-a-gr example 2 (*Azért vezették be az újrahasznosítást …*) uses a verbal noun one screen before the verbal-noun screen of the same lesson (unsure, left).
- Story: János bácsi's *Nem fél egyedül az erdőben …?* is a negative question (unsure; natural Hungarian for "aren't you afraid").
- Story question 3 option 4 (*kizárólag*-type wording) is fine; story comprehension questions are in Hungarian without `questionEnglish` (B1, left).
- The core-unit rule left several screen examples with words in no list (*átlaghőmérséklet, tüzelőanyag, szezonális, igyekszem*): they are the screens' own examples, so they count as met in their own lesson (unsure whether the reviewer wants them rewritten too).

### 5. Dictionary
derengő | derengő | adj | dim, faintly glowing |
megtisztul | megtisztul | verb | to be cleansed, to become pure |
mohos | mohos | adj | mossy |
posztókabátos | posztókabátos | adj | wearing a cloth coat |
vadcsapásokat | vadcsapás | noun | game trail, animal track |
zsivaja | zsivaj | noun | din, hubbub (of voices) |
jólesik | jólesik | verb | to feel good, to be pleasant |
viharlámpás | viharlámpás | noun | storm lantern, hurricane lamp |

Fix count, Unit 31: 89 fixes, 6 challenges.

---
## UNIT 33 society-inequality (b1-17-01 .. 05, consolidation; story b1-17-moricz)

Unit 33 teaches one new skill, `kent-vs-mint` (b1-17-01-b). The essive-formal *-ként* (A2 Unit 36) and the distributive *-nként* (A2 Unit 14) that fill most of the unit are known. Files: `fixes-society-inequality.json` (83 fixes), `challenges-society-inequality.json` (6).

### 1. Found by reading
- b1-17-01-a-gr presents *-ként* as new (A2 Unit 36, a2-176-a); b1-17-02-a-gr presents *-nként* as new (A2 Unit 14, a2-68-b); b1-17-02-b-gr (*míg*, *ezzel szemben*), b1-17-03-a-gr (*hogy* + -jon/-jen), b1-17-03-b-gr (*részesül* + -ban/-ben), b1-17-04-a-gr (*aki/amely*), b1-17-04-b-gr (-ó/-ő participles), b1-17-05-a-gr (opinion) all present forms of earlier units as new (B1 Units 4, 21, 5, 21, 10/A2 4, 11; A2 Units 12, 29). Fix: each rewritten as "You know … from Unit N".
- b1-17-05-b-gr title "Subjunctive of Hope" but every example is indicative (*kapnak*, *meghozzák*, *lesz*). Fix: recap of *bízik benne* + *hogy* + indicative (A2 Units 33, 11).
- b1-17-02-a-gr example 2 (*Évente többször szerveznek képzéseket*) is a *-nta/-nte* time word, not a *-nként* example. Fix: *csoportonként* example.
- b1-17-01-b-gr says *-ként* "strictly" designates a role and *mint* goes with nouns; it gives no pair showing the difference and ignores that *mint vezető* ("as a leader") is also natural. Fix: *Anna tanárként dolgozik* vs *úgy dolgozik, mint egy tanár* contrast. (unsure about the *mint vezető* point, see 4)
- b1-17-03-b-gr title lists *juttat vmit*, never explained; b1-17-02-b-gr title lists *ezzel ellentétben*, never explained; b1-17-05-a-gr title lists *Meggyőződésem szerint*, never explained. Fix: titles trimmed.
- Glued blanks (the learner types only the suffix): b1-17-01.ex04 (*Példa____*), ex06 (*Önkéntes____*), ex12 (*Vezető____*); 02.ex04 (*Munkanélküli____*), ex06 (*hónap____*); 03.ex04, ex06; 04.ex04, ex06; 05.ex04, ex06; consolidation.ex04 (*fejen____*). Fix: whole-word blanks (*Gyerekként*, *Hónaponként*, *Családonként*, …), hint names the word and its role.
- Hungarian metalanguage and "(Lesson N)" in the stems of ex02 in lessons 1–5 (*Melyik mondat használja helyesen a -ként vagy -nként ragot?*), with garbled wrong options (*Állampolgármint*, *… ként a gyermek*, *Önkéntesmint*): two faults each. Fix: English stems; wrong options are real forms (*Állampolgárnak*, *Állampolgárrá*, `distractor_skills` on the translative).
- b1-17-01.ex10: wrong option *Királyként él, mint úgy egy* (scrambled, two faults) and *Úgy él egy királyként*; note *Királyként él* is itself natural for "lives like a king". Fix: options with one fault (*mint egy királyként*, *egy király*).
- Reading-category items with no text, absurd wrong options: b1-17-02.ex08, 03.ex08, 04.ex08, 05.ex08 (quoting a line, *mindenki* tell in 05), consolidation.ex08. Fix: grammar items (*ezzel szemben*, *hogy* + -jon/-jen, *amelyek*, *bízom abban, hogy*) and a story question.
- check-content ERRORs, all fixed: tell-absolute b1-17-01.ex08 (*mindenki*), b1-17-05.ex08 (*mindenki*), consolidation.ex08 (*teljesen*); length-giveaway b1-17-03.ex05 (90 vs 55), consolidation.ex02 (79 vs 48), ex06 (114 vs 80), ex08 (97 vs 65).
- b1-17-02.ex07 (lesson 2) is built from lesson 5 vocabulary (*emberi méltóság*, *együttélés*) and unmet *alapköve*. Fix: lesson 2 sentence.
- `english` "Build the sentence in the correct order." on b1-17-01.ex07, consolidation.ex05. Fix: translation.
- Unmet words: every id in the `unmet-words.js` list has a fix (b1-17-01 ex02–ex08; 02 ex02–ex08; 03 ex03 ex05–ex08; 04 ex03 ex05 ex06 ex08; 05 ex02 ex03 ex05 ex06 ex08; consolidation ex02–ex08). Hungarian options and stems for meaning items became English items.
- STORY b1-17-moricz: question 1 asks for the author's "main message" (generic) and its right option was three times the length of the others. Fix: *Mit mond az édesanya a végén arról, ki a leggazdagabb ember?* with options in the mother's words. Questions 2 and 3 are fine. Story has *indulni készültek volna* (B1 Unit 39, one incidental use; stories keep their forms, unsure).

### 2. Metadata
- b1-17-02.ex02 `essive-formal-kent` → `distributive-nkent` (tests -nként).
- b1-17-02.ex08 reading → grammar `adversative-contrast`; b1-17-03.ex08 → `hogy-jon-jen`; b1-17-04.ex08 → `relative-clauses-aki-ami-amely`; b1-17-05.ex08 → `hogy-clauses`. consolidation.ex08 stays reading.
- `distractor_skills`: `{"2":"translative-morphology"}` on the *-vá/-vé* options (*Állampolgárrá*, *Rászorulóvá*, *önkéntessé*), `{"1":"essive-formal-kent"}` on b1-17-02.ex02 (*családként*). Run `lock_tags.py … --update` after applying.

### 3. Goals / checklists
- All five lessons shared "I can use the essive-formal suffix -ként and distributive -nként in Hungarian.", "I can discuss social issues, equality of opportunity, and solidarity.", "I can master four new target vocabulary items in authentic context.", and line 1 was a garbled "vocabulary for talked about as….". Lessons 3–5 never practise the new line 2. Fix: four lesson-specific lines each, in both places in the lesson JSON.
- The lesson `grammar` line was identical in five lessons ("Essive-Formal -ként & Distributive -nként in Social Discourse"). Fix: one per lesson. Consolidation has no checklist; its challenge `canDo` is a unit line.

### 4. Doubtful
- `mint` + a noun also marks a capacity (*mint vezető*, *mint szülő*), so the "-ként = role, mint = comparison" split of the unit's one new skill is simpler than real usage; the new text only contrasts the two clear cases (unsure whether the reviewer wants a hedge).
- *Királyként él* is natural for "lives like a king", so a -ként item whose English says "(a comparison)" can't offer it as the right answer; b1-17-01.ex09 keeps *Vezetőmint* as a non-word option, fine.
- The screens' own example words in no list (*rászoruló*, *felzárkóztató*, *munkahelyteremtés*, *kistelepüléseken*) are left, as they are the screens' own examples (unsure).
- b1-17-04-b-gr example 1 *támogató kezet nyújt a nehéz sorsú embertársainknak* is literary; left.

### 5. Dictionary
ablakréseken | ablakrés | noun | gap around a window frame, draughty crack |
feküdt | fekszik | verb | to lie, to be lying down |
jóakaratú | jóakaratú | adj | well-meaning, kind-hearted |
kenyereskosár | kenyereskosár | noun | bread basket |
kenyérhéjat | kenyérhéj | noun | bread crust |
kisboltba | kisbolt | noun | small shop, corner shop |
konyhaasztalon | konyhaasztal | noun | kitchen table |
kopogtatott | kopogtat | verb | to knock |
lavórban | lavór | noun | washbasin, wash bowl |
lógasd | lógat | verb | to let something hang, to dangle (ne lógasd az orrod = don't sulk) |
mellécsúsztatva | mellécsúsztat | verb | to slip in beside, to slide alongside |
mennyezetű | mennyezetű | adj | with a ceiling (alacsony mennyezetű = low-ceilinged) |
négykézláb | négykézláb | adv | on all fours |
rézfillérnél | rézfillér | noun | copper penny, small copper coin |
sublót | sublót | noun | old-style chest of drawers, dresser |
sublótfiókokat | sublótfiók | noun | drawer of a dresser |
szalmás | szalmás | adj | thatched, made of straw |
szatócsboltba | szatócsbolt | noun | village grocery store, general store |
tükröződött | tükröződik | verb | to be reflected, to show in the eyes or face |
útravalóul | útravaló | noun | provisions for a journey (útravalóul = as provisions) |
bőrtárca | bőrtárca | noun | leather wallet |
döngölt | döngöl | verb | to tamp or ram down (döngölt padló = beaten-earth floor) |
varródoboz | varródoboz | noun | sewing box |

Fix count, Unit 33: 83 fixes, 6 challenges.
