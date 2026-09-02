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
- [x] Translation driller: practice by topic. **Built 2026-08-27.** The
  driller's own source data (`translation-index.json`) only ever carried
  `spanish`/`english`/`level`/`source` — no topic — so this was really a
  content-derivation problem before it was a UI one, and the actual
  content turned out messier than expected: the codebase has accumulated
  several different filename conventions over time, not one, and they
  differ between the two courses.
  - `scripts/build_translation_index.py` now derives a `topic` per pair
    from whichever of three shapes its source file's name matches: a
    slug filename (`{level}-{slug}-...`, e.g. `a1-hobbies-03-...` or
    `b1-nacionalismo-03-...`) uses the slug directly as the topic — the 8
    English A1 ones read fine as-is, the 36 Spanish B1 ones (the LatAm
    cultural-history track) get a hand-written label in the new
    `SLUG_TOPIC_LABELS` map; a numeric-unit filename
    (`{level}-{unit:2d}-{lesson:2d}-...`, most of ES) is looked up
    against `curriculum.json`'s `unit.<level>.<NN>` id for that unit's
    title; a numeric lesson-across-level filename (`{level}-{lesson}-
    {variant}-...`, all of HU) is looked up against `lesson.<level>.<NN>`
    instead, since HU's curriculum numbers lessons sequentially across
    the whole level rather than restarting per unit — a real content
    convention difference between the courses, not a bug, discovered
    while building this. B1 additionally needed a fix mid-way: its unit
    ids carry a third "track" segment (`unit.b1.core.NN` /
    `unit.b1.latam.NN`, both numbering 1-36) since it's dual-track, which
    collided until the numeric-unit lookup was scoped to register only
    "core" — B1's numeric filenames are always core; latam's are always
    the slug filenames instead, so this doesn't lose latam topics, they
    just come from the slug path. Coverage after the fix: 3015/3034 (99%)
    ES pairs, 734/734 (100%) HU pairs got a topic; the last 19 ES pairs
    are 5 irregular "b1-03c-*" grammar files that match none of the three
    shapes and simply have no topic (still included in the driller,
    just not topic-filterable).
  - `engine/drills/translation.js`: new Topic `<select>` next to the
    existing Level one, scoped to whichever level is currently selected
    (the full cross-level list is 100+ topics — one level's worth is a
    browsable few dozen), each option showing its sentence count like the
    level options already do. Changing level re-renders the topic list
    and resets the topic selection to "All topics" if the previously
    chosen one doesn't exist at the new level. `_poolFor()` now filters by
    topic as well as level before a session starts. Also added the
    missing "B1" option to the Level select itself while in there — it
    turned out over half of ES's pairs (2,013 of 3,034) were B1 and had
    no way to be selected at all before this, an unrelated pre-existing
    gap noticed and fixed as a one-line addition alongside the topic work.
  - Verified live with Playwright: Level select now reads "B1 (2013
    sentences)"; Topic select at "All levels" lists 111 distinct topics,
    narrows to exactly A1's 19 (matching its 19 curriculum units) when
    Level is switched to A1; starting a session scoped to "At Home"
    produced a thematically correct sentence ("Hay un baño." / "Las
    ventanas están en la habitación."); a B1 latam-track topic ("The
    Cuban Revolution") correctly produced a matching sentence about Cuba,
    confirming both B1 tracks resolve correctly despite their different
    filename shapes; Hungarian's Topic select listed all 30 units. No
    console/page errors in any run.

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
- [x] Equal-weight study row: Review/Match/Learn shouldn't have one
  visually outranking the others. **Done 2026-08-27**: new `.dk-study-row`
  of three identically-sized/styled tabs (`.dk-study-tab`) replaces
  Review's old `.btn-primary` treatment — no single mode reads as "the"
  primary action any more. Review keeps a small due-count badge (real
  scheduling info, not a status claim) and its disabled-when-nothing-due
  state. "Add N to review" and "Edit deck" moved into a smaller, quieter
  `.dk-utility-row` below (plain underlined text buttons, `.dk-link-btn`
  — the same treatment the word list's Sort toggle already used, so it's
  now one consistent "meta action" style rather than a one-off). Verified
  live: all three tabs render at pixel-identical width/height, and
  clicking through to Match still works correctly from its new spot.
- [x] Collapse "Add to review, then Review" into one step; a per-course
  direction toggle and a shuffle for review. Feedback: "the way to review
  and then review, and then you have to add it to review to able to
  review it... too many steps... if you compare it to Quizlet... just go
  and practice what they want to practice... if they want to have the
  English first, good, just flip a switch. If they want to shuffle it,
  good, just flip a switch." **Done 2026-08-27**:
  - `engine/decks.js`: deleted the standalone `addDeck()` function (the
    "Add N to review" button's SRS-card-creation step) and folded its
    logic directly into `reviewDeck()` — any word in the deck with no SRS
    card yet now gets one created on the spot, immediately before
    `startReviewSession()` runs, so clicking "Review" is the only click
    needed regardless of whether any of the deck's words had been
    reviewed before. `newCardSchedule()` always sets a fresh card's
    `nextReview` to right now, so a same-turn creation is included in the
    session it's created for rather than waiting a day. No daily-cap call
    here either (same reasoning as the earlier 20-word-cap fix above:
    this is a deliberate whole-deck action, not the Reader's incidental
    one-word popup). `statusOf()` gained a `ready: due + missing` field —
    what "Review" is actually about to cover — and the deck-detail Review
    tab's badge/disabled state now reads `s.ready` instead of `s.due`, so
    a brand-new deck with zero existing cards shows an enabled Review tab
    with the deck's full word count, not a disabled one reading 0. The
    now-redundant "Add N to review" button and its `[data-add-deck]`
    handler are removed from `.dk-utility-row` (which now only shows
    "Edit deck" for custom decks) and from `detailHtml()`'s status line.
  - The direction toggle (target-language-first vs. English-first) and
    the always-random per-card draw a learner would expect from "shuffle"
    turned out to already exist and already be course-generic — both
    predate this session's Quizlet-mechanics work. `reviewDirection`/
    `toggleReviewDirection()` in `engine/srs.js` already labels its own
    toggle via `Lang.name()` rather than a hardcoded "Spanish", and
    `showNextCard()` already draws the next due card via `shuffled(dueCards)[0]`
    — every card in a review session is already presented in random
    order, with no sequential/linear mode to opt out of, so there's no
    meaningful "off" state a toggle would switch to. No new toggle was
    built for either; both were verified live instead (see below), and
    review's presentation order was deliberately left as-is (always
    random by design, matching SRS practice) rather than adding a
    Flashcards-style on/off switch for a linear order nothing else in the
    app produces.
  - Verified live via Playwright, once per course: opened a Spanish
    lesson deck with zero existing SRS cards for any of its 46 words —
    detail view showed a Review tab already enabled with a "46" badge
    (not disabled/0) and status line "0 mastered · 46 words total" (no
    "in your review deck" framing left); clicking Review launched the
    session immediately (no intermediate step), with due/new/total all
    reading 46 and the direction toggle right there in the session,
    correctly labelled "Spanish". Repeated for a Hungarian lesson deck
    (19 words, all previously un-added): Review tab enabled with badge
    "19", session launched immediately, direction toggle correctly
    labelled "Hungarian" via the same `Lang.name()` call. Clicking the
    direction toggle flipped its `aria-checked` state correctly in both
    runs. No console/page errors in either run.
- [x] Learn mode: gradual, smaller-batch recall instead of one giant pass.
  Feedback arrived in three rounds the same day. First: "you only go
  through one round, and it's not enough... not too many words at one
  go... maybe seven, maximum ten... it needs to be asked at least three
  times with increasing difficulty." Then, once a three-stage version was
  live: "what if we do four stages? And the third is typed English, but
  it is not accent sensitive. And the last one is it has to be perfect."
  Then, once that four-stage version was live: "the learn sequence should
  be from target to English, then multiple choice also from English to
  target, then from English to target typed no accent checking, and the
  fourth one should be from English to target. Perfect. That's the right
  four step sequence." **Done 2026-08-27** — `engine/decks/learn.js`
  rewritten, then revised twice more the same day to land on the final
  sequence below:
  - The deck is shuffled once and chunked into rounds of 7 words
    (`ROUND_SIZE`, the low end of the range asked for, and roughly what
    Quizlet's own Learn mode uses) rather than the whole deck at once —
    only the current round's words are in play; the rest of the deck
    isn't touched until the round clears.
  - Each word needs to pass four `STAGES`, in order, before it's mastered
    and drops out of the round — the final locked-in sequence: (1)
    multiple choice, target-language term shown, pick the English
    meaning; (2) multiple choice, English shown, pick the target-language
    term — the reverse direction, so recognition holds both ways before
    asking for production; (3) typed, English shown, type the
    target-language term, graded leniently — accents not checked
    (`_gradeTargetLenient`) — a first, lower-stakes rep at production; (4)
    typed, English shown, type the target-language term again, same
    direction as stage 3 but graded strictly this time — accents included
    (`_gradeTarget`) — "has to be perfect," so it's last. Passing a stage
    re-queues the word a few questions later rather than immediately
    (`_requeue`, `RETRY_DELAY`), so a word isn't tested four times in a
    row back-to-back — it comes back around, the "gradual recall" the
    original feedback asked for. A wrong answer at any stage doesn't
    demote it, just re-asks the same stage again a few questions later.
  - The two typed stages share one direction (English shown, type the
    target-language term) and differ only in strictness, per the final
    direction above — a deliberate change from the previous version's
    typed-English-meaning stage, which this replaced outright. Both share
    `_normaliseTarget` (lowercase, trims, drops terminal punctuation, NFC
    Unicode representation) as a base; `_gradeTargetLenient` (stage 3)
    additionally strips accent marks from both sides before comparing,
    while `_gradeTarget` (stage 4) leaves them in, matching the standard
    the main lesson flow settled on for the same reason
    (`engine/lessons.js`'s `normalise()`, also 2026-08-27) — an accent is
    often the entire distinction between two target-language words. Both
    stay lenient about the article either way. The now-unused
    `_gradeEnglish`/`_normaliseEnglish` (the old lenient-English grading)
    were deleted along with the stage that used them.
  - Once every word in a round is mastered, the next round starts
    automatically via a "Round N complete — continue" screen (or, on the
    last round, the existing results screen) rather than silently
    dumping straight into new words.
  - A deck too small for a fair multiple-choice round at a given stage
    (fewer than 2 usable decoys, checked against the whole deck's word
    pool, not just the round) skips that stage rather than asking a
    spuriously easy 1-option question — verified live down to a 2-word
    deck, which lands directly on stage 3 (typed, lenient) for both
    words, both MC stages having nothing to build options from.
  - Verified live end-to-end via Playwright across all three revisions,
    each via a temporary in-module debug hook (added, exercised, then
    removed before each commit) to drive real gameplay deterministically.
    Final pass: a 46-word deck's first question showed the target-language
    term as the prompt with English-meaning options (stage 1's "target to
    English" direction, per the final sequence); a 2-word custom deck
    (café/año) skipped both MC stages straight to stage 3, where typing
    the unaccented "cafe"/"ano" was accepted ("✓ Correct!") — confirming
    the lenient grading — then at stage 4 the same unaccented input was
    correctly rejected ("✗ café"/"✗ el año") across several repeated
    requeues, confirming the strict grading holds distinctly from stage
    3's. No console/page errors in any run.
- [x] Decks screen: the top of the tab took up too much space. Feedback:
  "there should be two big numbers. No. Maybe three big numbers. First
  one should be waiting to review... the one in the middle should be
  reviewed today... the last one should be known words... those should be
  the words that the user has mastered... under that, we should have
  review all and all my words... my dictionary should actually go inside
  all my words." **Done 2026-08-27**:
  - The two unevenly-sized "All my words"/"My Dictionary" cards are
    replaced with one compact `.dk-stats-row` of three equal numbers:
    waiting to review (`mineStatus.due`), reviewed today (reused from the
    XP system's existing `xpData.history[today].reviewsDone`, tracked
    since well before this session — no new counter needed), and known
    (`knownWords.length`, the words that have actually graduated out of
    review for good, not the softer in-deck "reviewed 3+ times" signal).
  - The action row under it is down to two buttons: "Review all" and "All
    my words" — "My Dictionary" is gone as a separate destination.
  - My Dictionary is now a state inside "All my words" instead of its own
    screen: `myDeck()` concatenates `srsDeck` (actively reviewing) with
    `knownWords` (graduated), tagging the latter with `known: true`.
    `detailHtml()`'s row rendering shows a `known` state for those rows
    and swaps the usual "×" remove button for "Back to review"
    (`data-move-to-review`, reusing the existing `moveKnownToReview()`)
    since deleting a known word's row shouldn't delete review history it
    doesn't have. The standalone `dictionaryHtml()` screen, `showDictionary`
    state, and its `data-open-dictionary`/`data-close-dictionary` wiring
    are all removed; the "mark a word known by hand" input
    (`addKnownWordByHand()`, unchanged) now sits directly in "All my
    words"'s detail head instead of the old separate screen.
  - Merging the two exposed a latent bug worth fixing alongside it:
    `statusOf()` and `reviewDeck()` both treated any word with no SRS card
    as "never added, create one on Review" — which used to only matter for
    a lesson/topic deck's un-added words, but now that a known word sits
    right next to reviewing ones in the same "All my words" list (and
    "Review" is one click away on that exact screen), the same logic
    would have silently un-graduated every known word the moment someone
    reviewed "All my words". Both functions now skip any word that
    `isKnown()` (or carries `known: true`), so known words stay known
    through a Review click, verified live below.
  - Verified live with Playwright: seeded 3 reviewing words (2 due, 1
    mastered) and 2 known words plus a `reviewsDone: 7` XP history entry
    for today — the stats row read "2 / waiting to review", "7 / reviewed
    today", "2 / known" exactly, the action row showed only "Review all
    (2)" and "All my words", and `[data-open-dictionary]` was absent from
    the DOM. Opening "All my words" showed all 5 words in one list
    ("1 mastered · 5 words total"), the 3 reviewing words with their
    existing states and "×" remove, the 2 known words as `KNOWN` with
    "Back to review" instead. Clicking "Back to review" on one moved it
    from `knownWords` into `srsDeck` correctly; clicking "Review" on "All
    my words" immediately afterward left the *other*, still-known word
    untouched in `knownWords` — confirming the un-graduation bug fix
    actually holds under the exact click sequence a learner would use.
- [x] "No white rectangles" — the Review/Match/Learn study-tab buttons,
  Learn mode's multiple-choice options and typed input, and Match mode's
  tiles all rendered as flat white boxes on the cream page, at odds with
  the app's own documented identity (`styles/base.css`: "the identity is
  open rows on cream separated by hairlines, not a stack of lifted white
  cards"). **Fixed 2026-08-27** — traced to four rules in
  `styles/components.css` (`.dk-study-tab`, `.dkm-tile`, `.dkl-option`,
  `.dkl-input`) filled with `var(--surface)` (pure white `#FFFFFF`)
  instead of `var(--bg)` (the cream `#F5F1E8` every other button/input in
  the app already uses — confirmed against `.dk-secondary` and
  `.dk-editor-input`, both already correctly on `--bg`). Switched all
  four to `--bg`. That in turn flattened two interaction states that had
  been relying on the old white-to-cream contrast to read as "different
  from resting": `.dkm-tile.is-selected`/`.dkl-option.is-correct` now use
  a light navy tint (`rgba(16, 42, 71, 0.05)`, the same tint
  `.lsn-option.selected` already uses elsewhere) instead of the
  now-identical `--bg`, and `.dkm-tile.is-wrong` uses `--accent-bg` to
  pair with its existing `--accent-dark` border/text rather than blending
  into the resting tile. `.dkl-option.is-wrong` was already
  border/text-only with no background of its own, so it needed no change.
  Verified live: screenshotted the deck detail row, Learn mode's MC
  screen at rest and after answering (correct option tinted, wrong option
  bordered red, both legible against the cream resting options), and
  Match mode at rest and with a tile selected (clearly distinguished from
  its neighbours) — no white anywhere, every interaction state still
  reads correctly.
- [x] Match mode: fixed columns instead of one shuffled board. Feedback:
  "shouldn't match have English in one column, Spanish or Hungarian in
  the other, because now it just does randomly... which makes the quick
  matching quite annoying," followed shortly by "English should be in
  the left column." **Fixed 2026-08-27** — `.dkm-grid` is a plain
  2-column CSS grid filled in DOM order, and `_newRound()` in
  `engine/decks/match.js` had been building one combined array of lemma
  and translation tiles and shuffling the whole thing together, so either
  language could land in either column round to round. Changed to shuffle
  the lemma tiles and translation tiles separately, then interleave them
  so English always fills the left column and the target language always
  fills the right (translation first in the interleave, per the
  follow-up direction — an earlier pass had it the other way round and
  was corrected the same day) — each column still independently
  randomised, just no longer swapping sides.
  Verified live with a temporary debug hook (added, exercised, then
  removed before commit): sampled 10 fresh rounds of an 8-word deck and
  confirmed every even tile index was `lemma` and every odd index was
  `translation` in all 10 (before the left/right correction). Re-verified
  the final left-English/right-target order without the hook via a
  6-word deck's actual rendered tile text — "word1..6" consistently in
  the left column, "palabra1..6" consistently in the right, across a
  fresh shuffle. No console/page errors.

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

## Cross-app flow

- [x] The app's sections (Lessons, Library, Workshop, Decks, Journey) read
  as six separate tools rather than one coherent whole — no interjection
  ties them together, so a learner has to already know why Workshop exists
  versus Decks versus Library. First concrete piece, from a brainstorm
  session: after finishing a unit's last lesson, Home should surface a
  Workshop practice round on what that unit just taught, instead of always
  pointing straight at the next lesson. Feedback settled two open
  questions: nudge, not a gate (never blocks progress, always skippable);
  and unit-boundary only, not a raw lesson-count trigger (a count would
  land mid-unit, before a concept is even fully taught — unit-end is the
  moment the content is actually complete). **Built 2026-09-02**:
  - `engine/home.js`'s new `practiceNudge()` detects "just finished a
    unit" from `getProgress()`'s own `completedAt` timestamps (most
    recently completed lesson, checked against whether it's the last
    lesson in its unit's `lessons` array) — no new progress tracking
    needed. Resolves the unit's grammar concept via the exact `teaches`
    tags already authored on every exercise, matched against
    `content/<lang>/indexes/grammar-index.json`'s `bySkill` map (the same
    index Workshop's Grammar Driller already builds its skill list from) —
    `exerciseRefFor()` derives each lesson's own exercise-file ref
    directly from its id, the same level/rest split `loadLesson()` in
    `engine/lessons.js` already uses, so no per-lesson file fetch is
    needed just to find the ref back out. The most-frequent matching skill
    wins; finding none means no nudge for that unit — silently falls back
    to the normal continue card rather than showing a "practice" button
    with nothing behind it.
  - Resolved silently once (practised or skipped) via a small
    `Lang.key('unitPracticeDismissed')`-backed set, so it's a one-time
    beat, never a recurring interruption for the same unit.
  - `GrammarDriller.render()` (`engine/drills/grammar.js`) gained an
    `options.skill` parameter — only honoured from its settings phase, so
    a driller resumed mid-session ignores it — that skips the skill-picker
    screen and launches straight into a session on that exact skill.
    `Workshop.open(id, options)` (`engine/workshop.js`) now threads an
    opaque options object through to whichever driller opens.
  - **Known real gap, not fixed here**: `grammar-index.json` only indexes
    `category:"grammar"` exercises (81 of ~4,700 in Hungarian), while the
    same `teaches` tags are authored far more broadly across
    introduce/controlled/practice/etc. — so today's nudge only fires for
    units whose grammar happens to include a dedicated grammar-category
    exercise, which is a minority of units. Broadening either the index or
    the Grammar Driller's own pool-building to pull from any category
    would widen coverage a lot, but that's a change to what "Grammar
    Driller" draws from across the whole app, not scoped to this pass.
  - Verified live via Playwright for both courses: seeded a Hungarian
    unit's progress (`unit.a1.05`, "Objects & Locations") and confirmed
    the nudge card rendered with the correct title and a real resolved
    skill (`van-and-nincs-there-is-there-isn-t`); clicking "Practise now"
    switched to the Workshop tab and landed directly on "Question 1 of
    10" with zero settings screen; returning to Home afterward showed the
    nudge gone and the normal continue card in its place. Repeated for
    Spanish (`unit.a1.01`, skill `ser-questions`), this time clicking "Not
    now" — nudge disappeared without navigating away, and stayed gone
    after a full page reload. No console/page errors in any run (the one
    404 seen is `drills/grammar/a1-bank.json`, which doesn't exist for
    Hungarian — a pre-existing, harmless fetch failure the driller already
    catches, confirmed present on a baseline Grammar Driller visit with no
    nudge involved at all).
- [x] Lesson-complete should be the connective moment: the just-taught
  words and any milestone crossed currently go unmentioned on the
  "Congratulations!" screen, which was otherwise a dead end straight back
  to whatever tab opened the lesson. **Built 2026-09-02**:
  - `engine/lessons.js`'s `renderLessonSummary()` now also shows the
    lesson's own vocabulary (via the already-existing
    `collectLessonVocabulary()`) as a row of chips, with one "Add N to a
    deck" button wired straight to `Decks.openBulkAddPicker()` — the same
    call the Library's multi-select vocabulary view already uses, so this
    needed no new Decks-side plumbing.
  - Any of Journey's `MILESTONES` newly crossed by finishing this exact
    lesson now shows as a plain line ("Milestone: 100 words met").
    `Journey.MILESTONES` is now exposed alongside the already-public
    `collect()` so the check reuses the same list and test functions
    rather than duplicating them; a small `Lang.key('milestonesSeen')` set
    (same pattern as the post-unit nudge's dismissed-units set) makes sure
    a milestone is only ever announced once, not re-shown on a later visit
    to Journey or a lesson redo.
  - Both the words and milestone sections, along with the new XP/streak
    stat below (see next item), only appear on a genuine first completion
    — `finishLesson()` already knew this from `markLessonComplete()`'s own
    return value, now threaded through to the summary as `firstTime`, so a
    redo doesn't show a stale "+20 XP" or re-announce a milestone that
    isn't newly true. The words themselves aren't gated the same way —
    replaying a lesson to reinforce its vocabulary is a real reason to
    revisit it.
  - Verified live via Playwright (a temporary debug hook driving straight
    to `finishLesson()`, removed after): a fresh Hungarian lesson 1
    completion showed 80% accuracy, "1 min", "+20 XP", "No streak yet",
    "Milestone: First lesson finished", and 5 correctly-labelled word
    chips; clicking "Add 5 to a deck" opened Decks' picker correctly
    titled "Add 5 words to a deck". Redoing the same lesson afterward
    showed 100% accuracy and "1 min" but no XP stat and no milestone line,
    while the same 5 word chips and a streak line were still present, as
    designed. No console/page errors in either run.
- [x] Surface XP/streak feedback inside the lesson itself, not only on
  Home's strip and as a sound effect. **Built 2026-09-02**, folded into
  the same lesson-complete pass above rather than as a separate feature:
  a third stat (`+20 XP`, reading `GRAMMAR_XP` from `engine/xp.js`,
  already a page-level global) joins accuracy and time in the summary's
  existing stat row, and a streak line sits just below it, reusing the
  exact wording Home's own header-streak already uses (`getStreak() > 0
  ? streak + '-day streak' : 'No streak yet'`) rather than inventing a
  second phrasing for the same fact — always shown, even at zero, since a
  blank line there would read as "did I lose my streak?" rather than
  "nothing to report." The existing global `showXPNotification()` toast
  (used for every XP-earning action, reviews included) still fires
  independently and was left alone — this adds a considered restatement
  in the close-of-lesson screen, not a replacement for the real-time one.
- [x] XP is only ever a running total — no tiers, no moment where anything
  happens. Feedback: "where are the levels, when does one level up."
  Deliberately not called a "level" in the build, though — this app
  already has one of those (A1/A2/B1/B2/C1, the CEFR course levels), and
  reusing the word for an XP tier would make two unrelated things both
  say "Level 4." Settled on **Rank** instead, cosmetic only (no unlocks).
  **Built 2026-09-02**:
  - `engine/xp.js`: `rankThreshold(rank)`/`rankForXP(xp)`/`getRank()`.
    Escalating thresholds (100, 300, 600, 1000, 1500, 2100, 2800, 3600,
    4500 for ranks 1-10 — `100 * n * (n+1) / 2`) rather than a flat "every
    100 XP", so early ranks come in a couple of days at this file's own
    "normal day ~30-100 XP" calibration and later ones take real
    sustained effort — the count never turns into daily noise once totals
    climb. Purely numeric ("Rank 4"), no named tiers.
  - Shown in the three places XP already appeared: Home's header
    (`updateXPHeader()`, now "Rank 4 · 1,234 XP" instead of bare XP),
    Journey's XP card (Rank is now the headline reading with a progress
    meter to the next one, reusing the card's own existing `meter()`
    helper; raw XP total moves into the facts list alongside reviews/
    stories rather than being dropped), and a rank-up line in the
    lesson-complete screen, reusing the exact same plain-text treatment
    as the milestone line built alongside it — `finishLesson()` captures
    the rank just before `recordLessonCompleted()` awards this lesson's
    XP, `renderLessonSummary()` compares it against the rank after, and
    only announces "Rank up! You're now Rank N." when they actually
    differ. Gated on `firstTime` the same way the milestone line is, so a
    redo never shows a stale rank-up.
  - Verified live via Playwright: seeded 90 XP (10 short of the Rank 2
    threshold at 100) — Home read "Rank 1 · 90 XP", Journey's XP card
    showed "Rank 1", a meter at 90%, and "90 / 100 XP to Rank 2". Finishing
    a lesson (awards 20 XP, 90 → 110) correctly showed "Rank up! You're
    now Rank 2." in the summary, and Home read "Rank 2 · 110 XP"
    afterward. Redoing an already-completed lesson (no XP re-awarded)
    showed no rank-up line and no XP stat, confirmed against
    `localStorage`'s XP total staying unchanged at 90. No console/page
    errors in any run.
- [x] Decks and Workshop need to integrate into the flow, not just sit next
  to it. Investigated first: found "Add to a deck" (Word Bank, Library,
  and the lesson-complete button built earlier this session) only adds a
  word to a deck's membership list — `addWordToDeck()` never created an
  SRS card, so a just-added word wasn't due, reviewable, or counted
  anywhere (Home's Review door, Journey's stats) until the deck was
  separately opened and reviewed later. Also found Decks' own review
  session had no completion screen at all — `endReviewSession()` just
  closed back to the deck browser with nothing said, unlike Lessons'
  rich summary or even Workshop's plain stat grid. **Built 2026-09-02**:
  - `engine/decks.js`'s `addWordToDeck()` now activates a word for review
    the moment it's added — a fresh, immediately-due SRS card, the same
    thing `reviewDeck()` already does for a whole deck at once, and using
    the same guard against silently un-graduating an already-known word.
    This is the single choke point every "add to deck" caller already
    goes through (Word Bank, Library's bulk-select, the lesson-complete
    button), so all of them are fixed by the one change.
  - `engine/srs.js` gained a real review-session summary
    (`renderReviewSessionSummary()`, shown in a new `#review-summary`
    slot in `index.html`), reusing the exact same building blocks
    `renderLessonSummary()` established for lessons: cards reviewed,
    accuracy (hard/good/easy count as correct, only "again" doesn't —
    the same distinction SM-2 itself makes), time, XP actually earned
    this session (before/after `xpData.total`, not derived from rating
    counts, so it can't drift out of sync with whatever `awardXP()`
    does), a streak line, a rank-up line, and any Journey milestone
    crossed — literally the same functions and wording
    `renderLessonSummary()` uses (`getRank()`, `getStreak()`,
    `newlyReachedMilestones()`), since every one of them turned out to
    already be a plain global, callable from any file. `showNextCard()`
    now branches on whether the just-finished session actually reviewed
    anything (`reviewSessionStats.total > 0`): a real session gets the
    new summary, while opening Review with nothing due to begin with
    keeps the existing "All caught up!" panel, which was already the
    right message for that specific case.
  - Verified live via Playwright: adding a word through the real
    `Decks.openAddToDeckPicker()` flow correctly pushed a new card into
    `srsDeck` with `nextReview` set to now, and Home's Review door
    immediately read "1 word ready to come round again" — confirmed
    same-turn, no separate visit needed. A 4-card review session (2
    good, 1 easy, 1 again) produced "4 cards · 75% correct · 1 min · +7
    XP" with a streak line, and "Done" returned cleanly to the deck
    browser. Seeding 98 XP and rating one card "good" correctly showed
    "Rank up! You're now Rank 2." in the summary. Clearing the deck and
    opening Review again correctly fell back to the plain "All caught
    up!" panel rather than an empty/broken summary. No console/page
    errors in any run.
  - Not attempted here — a bigger, separate design question: cross-linking
    Workshop and Decks results directly (missed review words suggesting a
    grammar drill on their pattern, or a weak drill session suggesting
    adding its words to a deck). Flagged in the original discussion as
    needing its own scoping pass.

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
