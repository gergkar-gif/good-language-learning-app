# Hungarian A1 Content Revision Backlog

Captured 2026-08-21 from a user planning session reviewing Hungarian A1 units
1-5 in depth, plus a set of app-wide decisions. Sequencing per the user:
cross-cutting fixes first, then unit-by-unit content. Format follows
`TROUBLESHOOTING_BACKLOG.md`'s convention — `[ ]` open, `[x]` resolved with an
inline note.

## Decisions made this session

- Audio (real files replacing TTS): deferred — future feature, not in this pass.
- Consolidations: rebuild to ~20 pure exercises each — 5 multiple-choice, then
  15 production, testing the unit's grammar and vocab. *(not started — large
  content-authoring task across 29 consolidation files)*
- Unit-at-a-glance: LingoDeer-style page (numbered index + expanded points
  below), auto-assembled from each lesson's existing `grammar` sections. No
  vocab section — words already live in SRS/Decks by topic. *(not started —
  new feature, needs a renderer + a nav entry per unit)*

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

## HUN A1

### Unit 1
- [ ] Shouldn't start with a review — nothing to review yet. Instead: a
  welcome page, then 'lesson goals', then the grammar page about 'sounds',
  then the one about 'stress'.
  - [ ] Stress page: words shouldn't be in ALL CAPS (e.g. SZIA) — confirmed
    live bug in `a1-01-a-gr.json`.
- [ ] S5: not only letters but words should also be listenable.
  - [ ] Get actual sound files, not TTS — build the engine and procure
    CC-licensed files. *(deferred — see Decisions above)*
  - [ ] All special sounds should be explained — template:
    hungarianreference.com's Hungarian alphabet phonetic pronunciation page,
    Transliteration Examples section. Maybe split across three grammar
    pages, fold 'stress' in as a tip on one of them.
- [ ] S8: take 'kérem' out of this lesson entirely.
- [ ] S15: the answer could also be 'nem'.
- [ ] S19: both replies are good (you can say 'köszönöm' in reply to 'tea?').

### Unit 1, Lesson 4 (a1-04 / "1.4")
- [ ] S5: grammar tip's first sentence is missing a capital letter at the
  start ("Nem").
- [ ] S12: 'nem vagyok' is also correct, not only 'nem tea'.
- [ ] S15: the answer could be either 'igen' or 'nem' — needs a hint.
- [ ] S22: víz, ház, and nagy appear as new words here without having been
  used in the lesson.

### Unit 1, Lesson 5 (a1-05 / "1.5")
- [ ] Reading: remove 'kérem' at the end, replace with 'semmiség'.

### Unit 2
- [ ] L1 S9: needs a clue.
- [ ] L1: the second tip shouldn't go on about 'reggelente' — should instead
  explain 'délelőtt' and 'délután' (before noon / after noon), and how
  délelőtt differs from "morning."
  - [ ] S24: the question is about 'megismételné?', which hasn't been taught.
- [ ] L2: introduce 'semmi baj' before it's used in S19.
- [ ] L3:
  - [ ] Don't introduce 'ön' — it's old-timey, nobody really uses it; spend
    the time on something else instead.
  - [ ] This lesson seems confused — it talks about times of day but then
    introduces 'ön'; seems like a mixup.
  - [ ] S15: "Te Károly?" is nonsense — should be "Te károly vagy?"
  - [ ] S19: same "Te károly" issue — should be "Károly vagy?" or "Te károly
    vagy."
  - [ ] S20: same "Te károly" sentence, fix it.
- [ ] L4: lesson title is "I don't understand" but the exercises are about
  'korán'/'későn' etc. — seems like a mixup.

### Unit 3
- [ ] Also seems all mixed up — no specifics given, needs a full pass.

### Unit 4
- [ ] L1:
  - [ ] S16: replace this exercise.
  - [ ] S21: replace the writing exercise with "list all even numbers."
- [ ] L2:
  - [ ] S3: 'telefonszám' hasn't been taught yet.
  - [ ] S5: in the tip, explain how 3rd person doesn't need 'van' — hány
    éves vagyok, hány éves vagy, hány éves?
  - [ ] S12: 'szám' hasn't been taught before this point.
  - [ ] S14: both "harminc éves" and "harminc éves vagyok" are correct.
  - [ ] "Write one short Hungarian sentence using today's personal
    information language" — replace this and similar prompts with more
    direct translation exercises.
- [ ] L(?) S10: "mi a telefonszámod" exercise — change it.
- [ ] L4: "…. éves vagyok" — change it.
  - [ ] S15: "hány éves …?" — could be vagy/vagyok.
- [ ] Reading: start with: "Moving to a new country comes with a lot of
  bureaucracy — and often, you need to fill in many forms. Károly is
  practising with Meg some of the most important details that one can be
  asked when introducing themselves."
  - [ ] "Tíz? És még egy szám?" doesn't really make sense.
  - [ ] Meg's birthday is in April and she is 32 years old.

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
