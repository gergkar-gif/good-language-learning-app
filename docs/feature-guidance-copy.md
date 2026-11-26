# New-learner introduction — flow and copy

How Parlour introduces itself to someone opening it for the first time.
Agreed and built 2026-09-24 (ACHIEVED.md item 87). The live text is in the
code (`engine/guide.js`, `engine/home.js` and the call sites); if you edit
a line here, ask for it to be carried over.

**Principle:** on day one they learn the language, not the app. Parlour shows
itself over the first week, one area at a time, each right after something
that makes that area useful.

**Voice:** understated. Say what it does, in one or two plain sentences.
No exclamation marks, no jokes, one feature per note.

**Look:** Source Serif italic, primary ink, a thin primary top rule (`2px` desktop / `1.5px` mobile), generous muted × close target, on a soft wash panel (`var(--wash)`) with no shadow (design principles). Floats just below its anchor (or automatically flips above when near the bottom of the viewport / mobile bottom nav) rather than pushing content down.

**Form:** small floating notes anchored next to the thing they describe.
They close on any tap (including on the note itself), on `Escape`, or when the feature is used (using a feature also marks its note seen so it never appears later). Never shown over a question in progress. At most one new note per day, apart from the handful inside the first lesson.

---

## 1. First open

Replaces the old Home welcome card. No tour, no room list. A quiet *"Already have an account? Sign in"* link stays at the bottom so returning learners on a new device can sign in directly (`Sync.openSignInModal()`).

**1a. Opening screen**
- Text: A place to learn a language properly, at your own pace.
- Then: What would you like to learn? — Spanish · Hungarian

**1a-ii. Which Spanish** (only if Spanish was picked)
- Text: Which Spanish?
- Buttons: Latin America · Spain

**1b. Starting point**
- Two buttons, no question or caption above them:
  Start from the beginning · Find my level
- "Start from the beginning" goes straight into Lesson 1.
- "Find my level" goes straight to the short placement test.

## 2. The first lesson

Only notes in this section (`inLesson: true`) may appear several in one day.

**2a. Listen** (`lesson-listen`)
- Trigger: first speaker button on a non-question step
- Text: Tap to hear it read aloud.

**2b. Tap a word** (`lesson-tap-word`)
- Trigger: first reading passage
- Text: Tap any word to see what it means.
- Marked seen on use when tapping a word in a lesson.

**2c. Missed answers** (`lesson-missed`)
- Trigger: first question answered after a wrong try, once it's done (a
  step revealed after three tries isn't queued again, so it gets no note)
- Text: Anything you miss comes back at the end.

## 3. First Home landing & Decks

**3a. Study desk** (`home-desk`)
- Trigger: first real Home visit after first-open setup
- Where: Home hero card (`.hm-continue`)
- Text: Your study desk. Come back here anytime for what to do next, or pick a quick session below.

**3b. Arriving in Decks** (`decks-arrival`)
- Trigger: first visit to Decks with at least one word in the deck
- Where: Decks explainer header (`.dk-explainer`, above the action buttons)
- Text: Words from your lessons collect here. There's no need to make cards yourself.
- Marked seen on use when starting a deck review.

## 4. First review & reading

**4a. First review card** (`review-first`)
- Trigger: first flipped card in SRS review
- Where: flipped above `#review-ratings` (`preferAbove: true`)
- Text: Words come back less often as you get them right.
- Marked seen and cleared on card rating (click or keyboard `1–4`).

**4b. First story or text in Library** (`library-arrival`)
- Trigger: first opened story in Parlour Library ([engine/reader.js](file:///home/antigravity/gergkar-gif/good-language-learning-app/engine/reader.js)) or My Texts / Saved ([engine/library.js](file:///home/antigravity/gergkar-gif/good-language-learning-app/engine/library.js))
- Where: story title / header (`.story-title`)
- Text: Tap any word to see what it means. Words you look up can go into your deck.
- Marked seen on use when tapping a word in the Reader.

## 5. First open-ended speaking or writing task (`production`)

- Trigger: first time opening an open-ended tab in Speaking Studio (Verbal Production / Conversation Scenarios) or Writing Studio (Written Production / Written Exchanges) — not Sentence Drills or Sentence Translation
- Text: There's no single right answer here. You'll get notes on what worked and what to adjust.

*(Note: The old per-lesson end-of-lesson invitations — `invite-decks`, `invite-library`, `invite-verb-driller`, `invite-listening-driller`, `invite-workshop` — were superseded by Home's recommendation engine and removed from `engine/guide.js`.)*

## 6. Later, when useful

These appear only when there's a reason, at most one per day, and are skipped if the learner already used the feature.

**6a. My Texts** (`library-mytexts`)
- Trigger: reaching A2, or five Library stories read (and not already on the My Texts tab)
- Where: Library, next to the My Texts tab
- Text: Import an EPUB, Word doc, or text file — or paste anything in — and look up words the same way.
- Marked seen on use when clicking the My Texts tab.

**6b. Known words (graduated from review)** (`my-dictionary`)
- Trigger: a word graduates out of review on its own (it was answered right often enough)
- Where: the review session summary
- Text: Words you know well graduate out of review as known. Find them anytime in All my words.
- Marked seen on use when opening All my words.

**6c. Grammar Guide** (`grammar-guide`)
- Trigger: unit page after reopening a finished lesson
- Where: unit page, next to the Grammar Guide link
- Text: Every unit's grammar is collected here, in case you want to look something up.
- Marked seen on use when opening Grammar Guide.

**6d. Import flashcards** (`decks-import`)
- Trigger: third visit to Decks (`My Decks` tab)
- Where: next to Import deck
- Text: If you have flashcards elsewhere, you can import them from Quizlet, Anki, Memrise or a spreadsheet.
- Marked seen on use when clicking Import deck.

**6e. Streak import** (`journey-streak`)
- Trigger: first visit to Journey (only when no streak has been imported and current streak is under 7 days)
- Where: next to Import a streak
- Text: If you're coming from another app, you can bring your streak with you.
- Marked seen on use when clicking Import a streak.

## 7. For reference

"About Parlour" (`Guide.openOverviewModal()` in `engine/guide.js`) stays reachable from Home's footer and the sidebar footer.

The drillers' "About this drill" info (`engine/drillInfo.js`) stays in the plain, second-person voice ("what this trains, why it might feel strange at first, what getting better looks like").
