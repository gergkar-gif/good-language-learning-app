# Roadmap

Future features and nice-to-haves, captured 2026-08-21 from a user
brain-dump. Not prioritized or sequenced — a parking lot, distinct from
`TROUBLESHOOTING_BACKLOG.md` and `HUNGARIAN_A1_CONTENT_BACKLOG.md`, which
track known bugs in existing content rather than things not yet built.

## Content & curriculum

- [ ] Integrate the same English-Spanish dual-language reading setup with
  originals as exists for Hungarian, up to A1 level.
- [ ] Hungarian: introduce Hungarian cultural material at B1-B2 (for the
  citizenship exam), similar to the LatAm course's dual-track structure.
- [x] Word Bank: same idea as Grammar Guide, but for vocabulary — a
  per-unit collection of the ~15-20 new words the unit introduces.
  **Built 2026-08-27**: `wordBankHtml()` in `engine/curriculum.js` is a
  near-exact clone of `grammarGuideHtml()` — same collect-then-render
  shape, same "fourth screen" slot off a unit's detail view (new
  `openWordBankUnit` state, mutually exclusive with the existing
  `openGrammarGuideUnit`), reached via a new "Word Bank" row placed right
  under "Grammar Guide". `collectUnitVocabTopics()` walks every lesson's
  `vocabulary` sections, grouped by each section's own title (e.g.
  "Greetings"), de-duplicated by lemma across the whole unit so a word
  taught earlier doesn't repeat under a later lesson's group. Renders
  through the same `stepRenderers.vocabulary()` the lesson screen itself
  uses, so it can't drift from how words actually appear in-lesson. New
  `wordBank` tag icon in `engine/art.js`. Verified live: a 6-lesson unit
  correctly shows 46 words across 5 topic groups, and closing/reopening
  navigates cleanly. **Add-to-deck added 2026-08-27**: each word row now
  has a small "+" button (`stepRenderers.vocabulary()`'s new `addToDeck`
  option, only passed by Word Bank's call site — the in-lesson vocabulary
  step is unchanged) that opens the same `Decks.openAddToDeckPicker()`
  overlay the Library's word-tap popup already uses. Wired via
  `data-add-to-deck`/delegated click in `attachCurriculumEvents()`, not an
  inline `onclick`, since a translation can contain a quote character
  ("don't") that would break a naively-interpolated JS string. Verified
  live: 46/46 rows carry a working button, clicking one opens "Add 'hola'
  to a deck".

## Workshop

- [ ] In the various Workshop drillers, show an English translation and an
  explanation of why that's the right response at the bottom of each
  exercise. **Partially fixed 2026-08-27** — audited every driller first:
  Vocabulary, Listening, and Translation drillers already showed both on
  every exercise (they're built at runtime from an inherently bilingual
  corpus — `translation-index.json` — rather than authored per-item), and
  Grammar Driller's 600-item bank already had a "why" explanation on
  100% of items. The real gaps were the 4 Hungarian drillers, where the
  translation/gloss was already available (dictionary/morphology data)
  but not consistently wired into a visible `explanation` field —
  fixed: `hu-suffix.js`'s multiple-choice/fill-blank builders,
  `hu-prefix.js`'s meaning-to-prefix builder (now cites a real
  attested example pair too), `hu-verb.js`'s production builder, and
  `hu-morphology.js`'s construction builder. Also extended
  `GrammarRunner`'s explanation reveal to the `dialogue-complete` and
  `sentence-order` kinds for consistency (no content uses it yet, but
  the display now exists). **Not fixed — this is the bulk of the
  original ask and is content-blocked, not a wiring problem**: Grammar
  Driller's lesson-sourced pool (7,170 entries, pulled from
  `grammar-index.json`) has neither an English translation nor a "why"
  for its two largest exercise types — 3,049 multiple-choice and 2,001
  fill-blank items, 0% coverage on both fields. This mirrors the
  existing lesson fill-blank/dictation translation gap already noted
  above (0/1,560, 0/522) — a real content-authoring project on the
  order of ~5,000 items, not attempted here.
- [x] Verb drill: leaderboard / top score / top accuracy — maybe extended
  to all Workshop activities, not just verbs. **Built 2026-08-27**, for
  Verb Speed only (the "maybe extended to all Workshop activities" part
  wasn't done — every driller's results screen is a near-identical
  copy-pasted block, so extending this would mean threading the same
  history store through 9 files, a bigger refactor than asked for here).
  New `engine/verbs/leaderboard.js`: a personal-best history, not a
  multiplayer ranking (this app has no accounts to compete against) —
  persisted per-course via `Lang.key('verbSpeedScores')`, ranked by
  accuracy then correct count, capped to the top 20 sessions.
  `VerbsSpeed._endSession()` records each completed session (sessions
  with zero answered questions are ignored); `_renderResults()` shows a
  new "Best accuracy" stat alongside the existing grid and a "New
  personal best!" banner when the just-finished session set one.
  Verified live end-to-end: a real 1-minute timed session correctly
  recorded to `localStorage` and rendered both the best-accuracy stat
  and the new-best banner.
- [ ] Translation driller: practice by topic.

## Library / dictionary

- [x] Spanish Library's word-translation popup currently shows the raw
  grammatical parse (e.g. "empezaba: verb · Imperfect, Indicative, 1st
  person singular from empezar, to start, begin, to get started") instead
  of the actual contextual translation (e.g. "started"). Should lead with
  the real translation, and could put the grammar explanation underneath.
  **Fixed 2026-08-27**: reordered `_renderWordReadings()`'s plain fallback
  branch in `engine/reader.js` — the translation now renders first, at the
  same visual weight (`.wp-contextual`) Hungarian's breakdown already gives
  its own contextual line, with "from `<lemma>`" and the pos/gender/tense
  parse (`.wp-analysis`) demoted underneath. The compact subtitle under the
  header (`#popup-analysis`) no longer duplicates the parse for this path
  either. True per-form contextual translation (e.g. "empezaba" →
  "started" rather than the infinitive's own gloss "to start, begin...")
  would need a real conjugation-aware gloss table, which doesn't exist for
  Spanish yet (Hungarian's ladder/chain mechanism is a different,
  language-specific thing) — not attempted here; this only fixes the
  ordering/prominence half of the ask. Verified live: tapping "vive" (from
  "vivir") now shows "to live; to be alive" first, "verb · Present,
  Indicative, 3rd person singular" below it.

## Decks

- [x] Spanish decks: some verb definitions are overly verbose — needs a
  pass to tighten them. **Fixed 2026-08-27**: `short_gloss()` in
  `build-manifest.py` (and its JS twin `Lexicon.shortGloss()` in
  `engine/lexicon.js`) now caps a gloss to its first 3 comma-separated
  synonyms, not just a 56-character cut — e.g. `reunir` went from "to
  gather, to collect, to bring together, to assemble, to get together, to
  round up, to marshal, to compile, to put together, to pull together, to
  draw together, to pool" to "to gather, to collect, to bring together…".
  Only affects the frequency decks (Top 100, 101-250, etc.), which pull
  raw Wiktionary glosses — lesson/topic decks are hand-authored from
  `content/*/vocabulary/` and were already short. Regenerated
  `decks.json` via `build-manifest.py`; since the capping function is
  shared, this also tightened a few dozen overly long Hungarian frequency
  glosses the same way (e.g. "case, instance, event, occurrence" →
  "case, instance, event…") as a side effect of the same fix.
- [x] Decks mechanics should work more like Quizlet. **Built 2026-08-27**.
  Asked which specific mechanic mattered most (a deck screen was, until
  now, just a plain word list — no flashcard/match/learn mode existed at
  all); the user picked all three offered. Each is a self-contained
  module under the new `engine/decks/` directory, same one-file-per-mode
  pattern as Workshop's drillers, reached via new "Flashcards"/"Match"/
  "Learn" buttons on the deck detail screen (`decks.js` gained a small
  `studyMode` state and delegates rendering to whichever module is open,
  closing back to the same deck it was opened from):
  - **Flashcards** (`flashcards.js`): one card at a time, tap to flip
    (CSS 3D transform, no per-frame JS), Prev/Next, shuffle, a completion
    screen with restart.
  - **Match** (`match.js`): timed tap-to-match, 8 pairs per round (a
    full deck would make an unplayably huge grid), wrong pairs flash and
    clear, correct pairs fade. Personal best time persists per deck via
    `localStorage`, same idea as the Verb Speed leaderboard
    (`engine/verbs/leaderboard.js`) — a record to chase, not a
    multiplayer ranking.
  - **Learn** (`learn.js`): adaptive practice — every word starts as
    multiple-choice (recognition) and only "masters" out of the round
    after ALSO surviving a typed question (recall); a wrong answer at
    either stage re-queues the word to reappear in ~3 questions rather
    than immediately or at the very end. Deliberately unscheduled and
    separate from SRS review (`engine/srs.js`) — resets every time it's
    opened and never touches a word's review interval; SRS still owns
    "when should I see this next," Learn is just "drill this deck right
    now." Typed grading is lenient (splits a multi-sense gloss like
    "hello / hi" or "to see, to watch" on `/`/`,` and accepts any
    alternative, stripping a leading "to/a/an/the" from both sides) since
    this grades free-typed English, not the target language.

  Verified live: Flashcards flipped through a real 46-word deck correctly
  end to end; Match won by building a lemma→translation map from the
  deck's own word list and clicking all 8 correct pairs (reached "New
  personal best!"), and the wrong-pair flash confirmed separately; Learn
  fully completed a 5-word deck in 11 rounds (10 is the theoretical
  minimum — 2 passes × 5 words) via the same map-driven approach, with
  both question types and the wrong-answer requeue path exercised.
- [x] Deck word list should default to add order with an explicit sort
  option, and Shuffle shouldn't rearrange the list itself — it should be a
  Flashcards-only presentation toggle, "like the shuffle button on
  Spotify." **Fixed 2026-08-27**: the deck detail screen's old one-shot
  "Shuffle" button (which reordered the persisted list in place) is gone;
  in its place, a small "Added order"/"Sorted A–Z" toggle above the word
  list (`engine/decks.js`'s new `sortOrder` state, default `'natural'` —
  insertion order for a My Deck, decks.json's authored order for a
  Parlour Deck) switches the LIST's own order, never randomizes it.
  Flashcards (`engine/decks/flashcards.js`) instead gained a persistent
  ON/OFF shuffle toggle (icon button in its header, filled when active) —
  off by default, presenting the deck's current list order exactly;
  turning it on reshuffles from that original order, turning it off
  restores that exact order again, and neither ever mutates
  `options.words` itself (a new `_original` array is kept separate from
  the presented `_words`). Match and Learn were left alone — both already
  randomize their own round/queue every time regardless of any list
  order, so a separate shuffle control would have nothing to toggle.
  Verified live: toggling the list's sort control changes only the list
  (confirmed round-trip back to the exact original order); Flashcards'
  toggle starts off (first card "hola", matching the list), turning it on
  changes the first card, turning it off restores "hola" as first again.
- [x] Follow-up to the above, same day: scrap Flashcards (SRS review
  already covers that better), fold Match into the deck screen as one of
  the primary action buttons rather than a separate "Study this deck"
  section, and remove the 20-word daily cap that was blocking bulk-adding
  a deck to review. **Done 2026-08-27**:
  - Deleted `engine/decks/flashcards.js` entirely — its script tag, CSS
    (`.dkf-*`), button, and `studyMode` dispatch branch are all gone.
  - The separate "Study this deck" row (`.dk-study-label`/`.dk-study-btn`)
    is gone too — Match and Learn now sit directly in `.dk-actions`,
    styled identically to "Review this deck"/"Add to review"/"Edit deck"
    (same `.dk-secondary` class), so opening a deck shows one consistent
    row of actions instead of two visually different tiers.
  - `addDeck()` (the "Add N to review" button — bulk SRS-activating an
    entire deck at once) no longer calls `canAddNewWord()`/
    `recordNewWord()` at all. That cap (`engine/xp.js`, `NEW_WORDS_DAILY_CAP
    = 20`) still exists and still works exactly as before for the
    Reader's own "+Add to SRS Deck" popup (`engine/reader.js`/
    `engine/srs.js`'s `addToSRS()`) — it's there specifically to stop
    incidental one-word-at-a-time adds while reading from burying a
    learner, which isn't the same moment as a learner deliberately adding
    a whole deck. Verified live: with the daily counter pre-set to 20/20
    (cap already active), "Add 46 to review" on a 46-word deck added all
    46 with no block and no alert, while the counter itself — and
    `canAddNewWord()` for the Reader's own path — stayed untouched at 20/
    `false`, confirming the two are now fully decoupled rather than one
    fix breaking the other's intended behaviour.

## Grammar reference

- [x] Grammar tips inside Workshop drillers (e.g. Suffix Driller),
  similar to the unit-level Grammar Guide. **Built 2026-08-27**, scoped to
  the Suffix Driller (the user's own example) after they picked "a
  reference panel for the concept" over the lighter alternative (richer
  per-exercise "why" text — already covered by the `explanation` field
  added earlier the same day). New `content/hu/reference/cases.json`: a
  standalone reference — NOT a `grammar.schema.json` file, since that
  schema's id pattern and validate-content.py's glob both assume
  lesson-tied content, and this deliberately isn't tied to any lesson —
  covering all 18 Hungarian cases plus plural and possessive (title,
  suffix form(s), a plain-English explanation of when it's used, one
  example sentence each). `GrammarRunner` gained a generic `_moreInfoHtml()`
  (native `<details>`/`<summary>`, no extra JS) shown alongside the
  existing per-word `explanation`, wired through all 5 exercise kinds so
  any driller can supply `moreInfo` later; only `hu-suffix.js` populates
  it for now via a new `_referenceFor(entry)` lookup keyed the same way
  `_promptFor()`/`_groupFor()` already branch (case code, or plural/
  possessive). Verified live across 80 sampled rounds: 19 of the 20
  concepts observed, zero malformed/`undefined` content, panel expands
  correctly and reads as a real grammar note (e.g. "About the Delative —
  -ról / -ről — Motion off a surface... — Beszélek a munkámról. — I'm
  talking about my job."). **Extended to the other 3 HU drillers,
  2026-08-27**:
  - Morphology Driller reuses `cases.json` directly (it decomposes the
    exact same case/plural/possessive suffixes, just stacked) — `ladder()`
    in `engine/morphology/hungarian.js` now tags every nominal breakdown
    row with a `concept` key (a case code, or `'plural'`/`'possessive'`)
    matching the reference's own keys, purely additive so the Reader's
    tap-word popup (the other consumer of `ladder()`) is unaffected. Wired
    into `_buildRecognition` (the sampled row's own concept) and
    `_buildConstruction` (the last-applied layer, usually the case).
  - Prefix Driller got its own new `content/hu/reference/prefixes.json`,
    one entry per preverb (15: meg-, el-, ki-, be-, le-, fel-, föl-, át-,
    rá-, vissza-, össze-, elő-, után-, ide-, oda-) going beyond the sense
    gloss already shown — e.g. meg-'s aspectual/completive role, fel-/
    föl-'s dialectal-variant relationship (the same pair the earlier
    ambiguous-decoy fix was about).
  - Verb Driller reuses its own existing `TENSE_INFO`/`DEFINITE_INFO`
    strings (previously only shown via a settings-screen "What's this?"
    toggle) as the `moreInfo` for every exercise — one combo per session
    (tense/definiteness is fixed for the whole session, unlike the
    per-word variation in the other three drillers), always including the
    definiteness note and adding the past-tense note only for a
    past-tense session.

  Verified live across all three: Morphology 32/60 rounds showed a panel
  (13 distinct concepts), Prefix 55/60 (title tweaked from "About the
  meg-" to "About the meg- prefix" after the first pass read oddly),
  Verb 8/8 with the combined tense+definiteness note. Zero malformed
  content in any sweep.

## Interface & platform

- [ ] Interface increasingly bilingual as level rises, eventually
  Spanish/Hungarian interface by B2.
- [ ] Dark/light mode.
- [ ] Browser extension: add words to your deck from anywhere on the web.
  - [ ] Same idea, one click: import an article/email/any text straight
    into the Reader.
- [ ] Small AI agent for discussion/writing practice.
- [x] End-of-lesson summary screen ("well done, you finished"). **Built 2026-08-27** — see TROUBLESHOOTING_BACKLOG.md's "Lesson-complete summary card" entry for detail.
- [x] Audio: small sound effects for right answer, wrong answer, finishing
  a lesson, etc. **Built 2026-08-27**, then redesigned same day on
  feedback that the first pass sounded too "gamey": `engine/sound.js`
  (new) synthesises two quiet textures with the Web Audio API rather than
  shipping audio files — a soft paper rustle (filtered noise) for wrong
  answers, and a small singing-bowl-like tone (a few detuned sine
  partials over a slow decay) for correct answers, with both combined
  (rustle then a longer bowl) for lesson complete. No bright synth
  "ding," no Duolingo-style cha-ching — a sound here should register once
  and get out of the way, not perform. Wired into the shared
  `solveStep()`/`failStep()` in `engine/lessons.js`, so every exercise type
  gets sound with one hook each instead of five separate places (unlike the
  accent-sensitivity fix earlier this session, there's only one grading
  path in the main lesson flow to wire — Workshop's drillers weren't
  touched, matching the roadmap item's own "lesson" scope). One global mute
  toggle (new speaker icon in the lesson header, `localStorage`-persisted)
  rather than per-course, since a learner who mutes it won't want it back
  the moment they're somewhere else in the app. Verified live via a
  Playwright node-graph inspection (oscillator/bufferSource/filter counts
  and gain envelopes per sound), since literal listening isn't possible in
  this environment; toggling mute actually suppresses/restores node
  creation, not just the visible icon state.
- [ ] Jump ahead: an end-of-level exam that, passed at 90%+, lets a
  learner skip straight to the next level — the assumption being they
  already know that level's content.
