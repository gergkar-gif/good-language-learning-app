# Hungarian A1 Content Revision Backlog

Captured 2026-08-21 from a user planning session reviewing Hungarian A1 units
1-5 in depth, plus a set of app-wide decisions. Sequencing per the user:
cross-cutting fixes first, then unit-by-unit content. Format follows
`TROUBLESHOOTING_BACKLOG.md`'s convention — `[ ]` open, `[x]` resolved with an
inline note.

## Decisions made this session

- Audio (real files replacing TTS): deferred — future feature, not in this pass.
- Consolidations: rebuild to ~20 pure exercises each — 5 multiple-choice, then
  15 production, testing the unit's grammar and vocab. **Built 2026-08-26**,
  though the final shape diverged from this line's original 5/15 split per a
  later, more specific instruction ("mostly-reused, ordered easy to hard"):
  28 of 29 consolidation units rebuilt to 20 exercises each, reused directly
  from the unit's own 5 lessons and grouped into four difficulty tiers
  (Recognize/Recall/In Context/Produce) rather than freshly authored. Unit 2
  (`a1-10-consolidation`) is still the original 18-exercise hand-built pilot
  from earlier in that same pass. See memory
  `hu-a1-consolidation-and-recycle-2026-08-26` and
  `hu-a1-consolidation-drilling-preference` for the full account.
- [x] Unit-at-a-glance, renamed "Grammar Guide": LingoDeer-style page
  (numbered index + expanded points below), auto-assembled from each
  lesson's existing `grammar` sections. No vocab section — words already
  live in SRS/Decks by topic. **Built 2026-08-21**: new screen in
  `engine/curriculum.js`, opened via a button at the top of a unit's lesson
  list (`unitDetailHtml`). Walks every lesson in the unit, collects each
  `grammar`-type section's referenced file, and renders a "Grammar Guide"
  header with a one-line dot-separated topic preview, then a "What you'll
  encounter" numbered list — each entry the topic's real title plus its
  text/tip prose (reusing `.lsn-text`/`.lsn-tip`, the same markup the
  lesson's own grammar screen uses). Tables and worked examples are left
  out deliberately to keep it skimmable. Shared engine file — works for
  Spanish too; verified live for both languages.

## Cross-cutting (apply everywhere)

- [x] Word-order exercise: remove the 'Reset' button. **Fixed 2026-08-21**:
  removed the button and the now-dead `lessonResetBuild()` from
  `engine/lessons.js` — tapping a placed tile already removes it individually
  (`lessonRemoveTile`), so Reset had no unique function. Verified live.
- [x] All exercises should recognize 'Enter' as Check, then as Continue, for
  all exercise/lesson types. **Checked 2026-08-21, already true**:
  `_wireLessonEnterToCheck()` in `engine/lessons.js` redirects Enter from any
  focused `.lsn-option`/`.lsn-tile`/text-input to the footer button, whatever
  it currently reads (Check or Continue) — this is keyed off DOM class, not
  exercise type, and every exercise type's interactive buttons (including
  matching's, which use `.lsn-option`) already carry one of those classes.
  This was built for Spanish in an earlier session and applies to Hungarian
  automatically since the engine is shared. No changes made.
- [x] 'Vocabulary' page should come before the two 'introduce' exercises,
  everywhere. **Fixed 2026-08-21**: scanned all 150 A1 lesson files — every
  single one had vocabulary after the Introduce exercise group. Reordered so
  vocabulary sits right after the lesson's grammar section(s), before
  Introduce. Verified live and re-validated JSON across all 150 files.
- [x] Lesson titles are inconsistently full-Hungarian or full-English —
  should always be "English - Hungarian". **Fixed 2026-08-21**: authored a
  bilingual title for every one of the 150 A1 lessons (the existing single-
  language title translated into the other language) and applied via script.
  Consolidation lesson titles ("Unit N Consolidation") were left as-is —
  they're structural labels, not thematic content, so bilingual translation
  doesn't serve a purpose there; flag if that's wrong. Regenerated
  curriculum.json/decks.json afterward. Verified live (title renders
  correctly with accents in the lesson header).
  - Side observation, not fixed: a handful of titles repeat verbatim across
    different lessons/units (e.g. "Hol van?" / "Where Is It?" appears 3
    times, "Összefoglalás" / "Summary" 3 times, "Quantities" twice, "At the
    Café" twice). Not in scope for the bilingual-format fix; flag if these
    should be differentiated.
- [x] *(new mid-session request, not from the original list)* Deck "shuffle"
  button uses an emoji (🔀) icon in every language, not just Hungarian.
  **Fixed 2026-08-21**: added a `shuffle` icon to the app's existing stroked-
  SVG icon set (`engine/art.js`, matching the style of `listening`,
  `workshop`, etc.) and swapped it in for the emoji in `engine/decks.js`.
  This is a shared, app-wide file — fixes Spanish too. Confirmed no other
  pictographic emoji remain anywhere in `engine/*.js` (only the pre-existing,
  intentional ✓/✗ text-glyph convention, which is a different and unrelated
  pattern).

## Curriculum-wide gaps (found 2026-08-21, auditing per user request)

- [x] Vowel harmony has no dedicated treatment anywhere in A1. **Fixed
  2026-08-21**: built a new dedicated grammar page ("Vowel Harmony",
  `a1-22-vh-gr.json`) — the two vowel families, why suffixes come in
  matching versions, and a clean 3-way example table (asztal/szék/sör)
  deliberately avoiding words like *könyv* that are exceptions to their
  own rule. Inserted into Unit 5 Lesson 2 (a1-22, "Objects"), right before
  the existing Plural Nouns page, which is the earliest point a
  vowel-harmonized suffix (the plural -k) is taught — matches the Unit 5
  backlog note below. Trimmed the Plural Nouns page's own vowel-harmony
  aside since it's now properly covered just before it, so it applies
  the concept instead of re-explaining it. Verified live, including that
  it flows correctly through the Grammar Guide.
- [x] Definite/indefinite conjugation is mislabeled, not just under-taught.
  **Investigated and fixed 2026-08-21**: found the fuller picture — the
  actual definite/indefinite *contrast* already gets used in three later
  spots (`a1-114-b` "Hozom", `a1-141-b` "szeretem", and a referenced-but-
  unverified `viselek/viselem` instance), each introduced as an isolated
  aside with no foundational page to point back to. Built one: a new
  "Definite vs Indefinite Conjugation" page in Unit 21 (`a1-102-def-gr.json`,
  inserted into "The Accusative -t") — right after the accusative exists,
  since definite objects are what the definite conjugation is *for*. Uses
  kérek/kérem as the central example, explicitly bridging back to "kérem"
  already having been taught as an interjection in Unit 2. Added two new
  practice exercises (`a1-102-practice-6/7`) testing the egy/a
  indefinite/definite distinction. Updated `a1-114-b` and `a1-141-b` to
  reference this page by name instead of re-deriving the concept solo.
  Separately fixed the immediate mislabeling this gap was named for:
  `a1-61-a-gr.json` (Unit 13) was titled "Present-tense indefinite
  conjugation" while only teaching ordinary present-tense endings, with
  nothing to contrast against this early — renamed to "Present Tense:
  -ok/-ek/-ök" and reworded the false "indefinite present" phrasing, across
  all 5 lessons in Unit 13 that carried the identical wrong title/text.
  - [ ] Found in the process, not yet fixed: Unit 13's five lessons
    (a1-61 through a1-65 — "I Work, I Study", "Everyday Verbs", "Who Does
    What?", "Talking About Activities", "Verb Review") don't just share a
    title — their grammar content is byte-for-byte identical across all
    five, the same duplication-without-customization bug already found and
    fixed in Units 2 and 4. Needs its own pass, same scope as those units'
    fixes: each lesson should teach something distinct that actually
    matches its own title.
- [x] Hungarian sounds: user asked to re-verify directly — a careful
  re-audit against the full alphabet found it was NOT actually complete as
  first claimed. **Fixed 2026-08-21**: two real gaps — `c` (plain, "ts" as
  in "cats", distinct from `cs`) and `j` (sounds like English "y", not
  English "j" — a genuine gotcha) were both missing entirely from the
  Consonant Sounds page. Also the long-vowel table only showed 5 of the 7
  pairs (á and ú had no example row). Added `c`→cukor, `j`→jó (reusing
  already-taught vocabulary), and á→ház, ú→kút to close both gaps.
  `dz`/`dzs` deliberately left out — genuinely rare, appear in a handful of
  loanwords, not standard even in hungarianreference.com-style A1
  coverage. Verified live.

## HUN A1

### Unit 1
- [x] Shouldn't start with a review — nothing to review yet. Instead: a
  welcome page, then 'lesson goals', then the grammar page about 'sounds',
  then the one about 'stress'. **Fixed 2026-08-21**: added a new "intro"
  section type (engine/lessons.js) and a welcome screen using it as the
  first step; removed the opening Review exercise group entirely (and its
  now-orphaned exercises). Order is now Welcome → Lesson Goals → Hungarian
  Vowels → Hungarian Consonant Sounds (stress folded into the latter's tip,
  see below).
  - [x] Stress page: words shouldn't be in ALL CAPS (e.g. SZIA) — confirmed
    live bug in `a1-01-a-gr.json`. **Fixed 2026-08-21**: the ALL-CAPS
    "Notice" examples block was removed as part of the grammar rewrite
    below rather than case-fixed in place — stress is now a short tip
    rather than its own illustrated section.
- [x] S5: not only letters but words should also be listenable.
  - [ ] Get actual sound files, not TTS — build the engine and procure
    CC-licensed files. *(deferred — see Decisions above)*
  - [x] All special sounds should be explained — template:
    hungarianreference.com's Hungarian alphabet phonetic pronunciation page,
    Transliteration Examples section. Maybe split across three grammar
    pages, fold 'stress' in as a tip on one of them. **Fixed 2026-08-21**:
    rewrote the two grammar files as "Hungarian Vowels" (all 7 short/long
    pairs explained, table examples for the ones with no English
    equivalent) and "Hungarian Consonant Sounds" (sz/s/zs/cs/gy/ny/ty/ly all
    explained, with the stress rule folded in as a tip at the end — 2 pages
    rather than 3, judged sufficient). Also fixed the underlying "only
    letters were listenable" bug generally: `table()` in engine/lessons.js
    now supports an explicit `"bothAudible": true` opt-in so a table's
    example-word column gets a listen button too, not just the bare
    letter/digraph column — applied to both new tables.
- [x] S8: take 'kérem' out of this lesson entirely. **Fixed 2026-08-21**:
  removed from the lesson's vocabulary list and from every exercise that
  referenced it (as a taught pair or as a distractor) — it now appears
  nowhere in Unit 1 Lesson 1. It's correctly taught in Unit 2 Lesson 2
  ("Please, Thank You, Sorry").
- [x] S15: the answer could also be 'nem'. **Fixed 2026-08-21**: fill-blank
  `a1-01-practice-3` now accepts either "Igen" or "Nem".
- [x] S19: both replies are good (you can say 'köszönöm' in reply to
  'tea?'). **Fixed 2026-08-21**: this needed a real engine change, not just
  a content edit — dialogue-complete only supported one correct index.
  Extended `shuffledOptions()`/`lessonCheckChoice()` (engine/lessons.js) to
  accept `correct` as an array, applied here (both "Igen." and "Köszönöm."
  now accepted, "Szia." added as a genuine wrong distractor), and exposed
  the same capability for `multiple-choice` since it shares the same
  checking code — schema updated in both content/hu and content/es.

### Unit 1, Lesson 4 (a1-04 / "1.4")
- [x] S5: grammar tip's first sentence is missing a capital letter at the
  start ("Nem"). **Fixed 2026-08-21**: also italicized the inline "nem"
  mentions to match the app's usual convention for target-language words
  embedded in English prose.
- [x] S12: 'nem vagyok' is also correct, not only 'nem tea'. **Fixed
  2026-08-21**: `a1-04-controlled-4` now accepts both "tea" and "vagyok"
  (multi-correct array, see the engine fix under Unit 1 above).
- [x] S15: the answer could be either 'igen' or 'nem' — needs a hint.
  **Fixed 2026-08-21**: `a1-04-practice-1` now accepts both, with a
  "(yes/no)" hint appended to the sentence.
- [x] S22: víz, ház, and nagy appear as new words here without having been
  used in the lesson. **Fixed 2026-08-21**: confirmed by checking every
  word against this lesson's actual grammar/exercise text — víz, ház, nagy,
  and also (unflagged but equally unused) jó, könyv, telefon never appear
  anywhere in Lesson 4. They're all genuinely taught in Lesson 5's reading
  and its own vocabulary list — removed from Lesson 4's vocabulary,
  leaving only igen/nem, which the lesson actually teaches and uses.

### Unit 1, Lesson 5 (a1-05 / "1.5")
- [x] Reading: remove 'kérem' at the end, replace with 'semmiség'. **Fixed
  2026-08-21**: also removed 'kérem' from Lesson 5's own vocabulary
  recap list, which listed it as taught unit vocabulary — now that it's
  taught nowhere in Unit 1 (see the Lesson 1 fix above), leaving it there
  would have been a dangling inconsistency. Confirmed "semmiség" already
  resolves correctly in the Reader's tap-to-translate dictionary
  (imports/dictionary/hungarian-en.json), so the substitution doesn't
  introduce a lookup gap.

### Unit 2
- [x] Root-caused, not just patched. **Investigated 2026-08-21**: this
  wasn't a handful of separate bugs — every lesson in the unit had the
  *vocabulary and title* it was supposed to have, but the *grammar content*
  was uniformly about an unrelated topic (daily-routine verbs, time-of-day,
  frequency, early/late), the same wrong topic cluster in all five lessons.
  Confirmed it isn't a true swap: Units 15 and 17, which really are about
  routines and frequency, still have their own distinct, correct content —
  Unit 2's grammar files were simply never written for what the lesson
  actually teaches. Rewrote all 10 grammar files (2 per lesson) to match
  each lesson's real, already-correct vocabulary and title. Also found and
  fixed a unit-wide duplication artifact along the way: a `practice-2`
  matching exercise with identical greeting pairs, and a `check-2` testing
  "megismételné?" (not taught until Lesson 4), both copy-pasted verbatim
  into every lesson without being customized — fixed wherever the tested
  word wasn't actually taught in that lesson (L1/L2/L3), left alone where
  it legitimately was (L4/L5, where megismételné and jó napot recap are
  real, already-taught content).
  - [x] L1 S9: needs a clue. *(Superseded — S9 in the original numbering
    was inside the removed daily-routine grammar content, which no longer
    exists after the rewrite above.)*
  - [x] L1: the second tip shouldn't go on about 'reggelente' — should
    instead explain 'délelőtt' and 'délután', and how délelőtt differs
    from "morning." *(Superseded — this tip belonged to the wrong grammar
    content entirely, removed in the rewrite. délelőtt/délután belong to
    whichever later unit actually teaches time-of-day vocabulary, not
    Unit 2, which is about greetings.)*
    - [x] S24: the question is about 'megismételné?', which hasn't been
      taught. **Fixed 2026-08-21** — see the check-2 fix above.
  - [x] L2: introduce 'semmi baj' before it's used in S19. **Fixed
    2026-08-21**: added to Lesson 2's vocabulary, along with 'kérem'
    itself, which — despite being half of this lesson's own Hungarian
    title ("Kérem, köszönöm, bocsánat") — was missing from its vocabulary
    entirely. New grammar page written to cover both.
  - [x] L3:
    - [x] Don't introduce 'ön' — spend the time on something else instead.
      **Resolved 2026-08-21**: asked the user for a replacement topic;
      chose "Hogy vagy?" (how are you / basic small talk). Fully retitled,
      re-grammared, re-vocabbed, and every exercise rewritten from
      scratch. Also removed the now-orphaned `uram`/`asszonyom` (sir/
      madam) from Lesson 5, which depended on the dropped formal-address
      theme — replaced with content using only that lesson's own real
      vocabulary (rendben/persze/tessék).
    - [x] This lesson seems confused — it talks about times of day but
      then introduces 'ön'; seems like a mixup. **Explained by the
      root-cause fix above** — neither topic belonged here.
    - [x] S15/S19/S20: "Te Károly?" is nonsense, should be "Te Károly
      vagy?" **Moot after the retheme** — the te/ön exercises that
      contained this sentence no longer exist.
  - [x] L4: lesson title is "I don't understand" but the exercises are
    about 'korán'/'későn' — mixup. **Fixed 2026-08-21**, same root-cause
    rewrite — this lesson's exercises were already correctly about
    understanding/repetition; only its grammar pages were wrong.
  - Also found and fixed while in the unit's consolidation: a
    `sentence-order` exercise (`a1-10-consolidation-7`) with a malformed
    schema (a `words` array instead of `sentences`) that would have
    rendered with no content to reorder — converted to multiple-choice,
    matching how this exercise type was already handled everywhere else
    in A1.

### Unit 3
- [x] Also seems all mixed up — no specifics given, needs a full pass.
  **Investigated 2026-08-21, found to be fine**: checked every lesson's
  grammar content against its title and vocabulary (pronouns → lenni →
  ki/mi → hol laksz → bemutatkozás) — all coherent, no mixup like Unit 2's.
  One unrelated bug found and fixed in passing: `a1-15-consolidation-7`
  had the exact same malformed `sentence-order` schema bug as Unit 2's
  consolidation (see above) — converted to multiple-choice.
  - [x] **Much more serious bug found and fixed later, 2026-08-21**: while
    building unit-grouped decks, found that Unit 3's 5 lessons plus their
    grammar and vocabulary files (20 files total) still carried their OLD
    internal `id` fields from the earlier-session Unit 2/3 renumbering fix —
    only the filenames were updated at the time, not the ids embedded
    inside the JSON. Since the Learn tab starts a lesson by id, not
    filename, every one of Unit 3's lessons was actually loading and
    playing Unit 2's content, and completing either unit would have marked
    the other complete too (both claimed the same ids). This was not
    caught by the "checked to be fine" pass above, which only compared
    content/title/vocab coherence, not id correctness. Confirmed via a
    full-corpus sweep that no other lesson/grammar/vocab file in A1 has
    the same mismatch. All 20 fixed; verified live that Unit 3 lessons now
    load their own real content.

### Unit 4
- [x] Not a wrong-topic mixup like Unit 2 — grammar/vocab/titles all
  cohere (Numbers → Age → Where You Live → Contact Details → combined
  recap). The real, recurring bug was the same unit-wide duplication
  artifact found in Unit 2: several exercises testing age content
  ("Hány éves vagy?"/"Harminc éves vagyok.") had clearly been copy-pasted
  into every lesson without adjusting for what that specific lesson
  actually teaches — including into Lesson 1, before ages exist at all.
- [x] L1 (Numbers 0-10):
  - [x] S16: replace this exercise. **Fixed 2026-08-21**: `practice-5`
    tested "Hány éves vagy?" (age, not taught until Lesson 2) — replaced
    with a numbers-only sequence-completion exercise. `check-2` had the
    same problem and was fixed the same way, though not explicitly named.
  - [x] S21: replace the writing exercise with "list all even numbers."
    **Fixed 2026-08-21** exactly as suggested — `writing-2` previously
    asked for "Harminc éves vagyok." in a lesson that hadn't taught ages.
- [x] L2 (How Old Are You?):
  - [x] S3: 'telefonszám' hasn't been taught yet. **Fixed 2026-08-21**:
    it was in the *Review* section (`review-2`), framing it as prior
    knowledge — telefonszám isn't taught until Lesson 4. Replaced with a
    genuine review of Lesson 1's numbers. Also removed it from
    `controlled-1`'s matching pairs, where it appeared un-introduced.
  - [x] S5: in the tip, explain how 3rd person doesn't need 'van' — hány
    éves vagyok, hány éves vagy, hány éves? **Fixed 2026-08-21**: extended
    the grammar tip to cover the third-person zero-copula form (Hány
    éves? / Harminc éves — no vagyok, no van), tying it back to the
    pattern already taught in Unit 1.
  - [x] S12: 'szám' hasn't been taught before this point. **Resolved as a
    side effect** of the earlier cross-cutting fix moving vocabulary
    ahead of the exercises that use it — szám is now properly pre-taught
    by the time this lesson's exercises reach it.
  - [x] S14: both "harminc éves" and "harminc éves vagyok" are correct.
    **Fixed 2026-08-21**: `practice-2` now accepts both (multi-correct).
  - [x] "Write one short Hungarian sentence using today's personal
    information language" — replace this and similar prompts with more
    direct translation exercises. **Fixed 2026-08-21**: this exact vague
    prompt, always paired with the mismatched answer "Harminc éves
    vagyok." regardless of the lesson's actual topic, turned out to be
    duplicated into every lesson in the unit (L1, L2, L3, L4) — replaced
    each with a direct, on-topic translation prompt.
- [x] L(?) S10: "mi a telefonszámod" exercise — change it. **Fixed
  2026-08-21**: `a1-19-controlled-2` asked the learner to fill in "nulla"
  as if it were an entire phone number, which didn't make sense — rewrote
  to ask for the word "telefonszámom" in context instead.
- [x] L4/L5 (Personal Information recap): "…. éves vagyok" — change it.
  **Fixed 2026-08-21**: `a1-20-controlled-2`'s "____ éves vagyok." had
  only one hardcoded correct number (harminc) when any number word fits —
  extended to accept a curated list.
  - [x] S15: "hány éves …?" — could be vagy/vagyok. **Fixed 2026-08-21**:
    `a1-20-practice-3` now accepts both.
- [x] Reading: start with the bureaucracy/forms framing text. **Fixed
  2026-08-21**, using the exact text supplied.
  - [x] "Tíz? És még egy szám?" doesn't really make sense. **Fixed
    2026-08-21**: root cause was a malformed phone number (13 digit-words
    instead of the standard 11-digit "06 30 123 4567" format used
    everywhere else in the unit) with a reply referencing "tíz", which
    was never actually said. Rewrote the exchange: Meg gives the number in
    the correct format, Károly asks her to repeat it more slowly (reusing
    lassabban/kérem/még egyszer from Unit 2), she does, then she turns the
    question around and asks for his address — all natural, and all
    already-taught vocabulary. Also fixed the same malformed phone number
    in the unit's consolidation model answer for consistency.
  - [x] Meg's birthday is in April and she is 32 years old. **Fixed
    2026-08-21**: updated both facts (was June / 30 — the same age as
    Károly, which the fix also incidentally de-duplicates).

### Unit 5
- [ ] L1:
  - [ ] S4: tip merely restates what was already said above.
  - [ ] S5: explain in the tip that 'micsoda' is made from mi (what) +
    csoda (wonder).
  - [ ] S11: 'micsoda' is translated as "what thing."
  - [ ] S17: replace the "sentences in the right order" exercise with
    another type.
- [ ] L2:
  - [ ] S4: "van egy könyv itt" is very unnatural — "van itt egy könyv" is
    better.
  - [ ] S5: it just drops in vowel harmony with no setup — if we expand
    later, say "for now, this is enough but we'll explain in the next
    lesson."
  - [ ] Lesson goals are weak/terrible ("being able to use asztal and szék")
    — same issue at the start of the lesson.
- [ ] L3: rewrite the lesson goal (at the beginning and end).
  - [ ] Maybe dedicate a full grammar page to vowel harmony in this unit —
    tbc.
- [ ] L4:
  - [ ] S4: what is "zero copula"? (clarify/explain)
  - [ ] S9: "van egy telefon …" — wrong word order, should be "… van egy
    telefon."
  - [ ] S12: "itt nincs lámpa" is more natural.
    - [ ] Maybe explain 'nincs' as the merging of 'nem van'.
  - [ ] S18: "nincs itt szék" means "there is no chair here."
- [ ] L5 (5.5):
  - [ ] S1: revise goals ("I can use tárgy…" doesn't make sense).
  - [ ] S10: "itt van egy lakás" is more natural.
  - [ ] S15: "itt nincs kulcs" and "itt van egy lakás" are more natural.
  - [ ] Story ends very abruptly — should be rounded off.
- [ ] Consolidation:
  - [ ] S2: two options can be correct.
  - [ ] Only 4 steps — audit all consolidations; they should have many more
    steps, filled with productive exercises. *(resolved as a decision above
    — rebuild to ~20 exercises, 5 MC + 15 production — not yet implemented)*
