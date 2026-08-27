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
- [ ] Decks mechanics should work more like Quizlet. **Captured
  2026-08-27, explicitly deferred by the user** ("to be discussed
  later") — no design or scope decided yet.

## Grammar reference

- [ ] Grammar tips inside Workshop drillers (e.g. Suffix Driller),
  similar to the unit-level Grammar Guide. **Captured 2026-08-27** — user
  proposed this ("maybe we should"); needs a design decision before
  building, since "similar to the Grammar Guide" could mean two fairly
  different things: (a) a reference panel/link to the general grammar
  concept being drilled (e.g. "About the Instrumental Case"), which
  doesn't map cleanly since a driller pulls from the whole
  dictionary/word-index rather than one unit's lessons, so there's no
  single Grammar Guide entry to link to — this would mean authoring new
  concept-level reference content; or (b) richer per-exercise "why" text
  than the terse one-liners `explanation` already shows (added
  2026-08-27, see "Workshop" section above) — a smaller, more
  self-contained change. Asked the user to clarify before starting.

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
