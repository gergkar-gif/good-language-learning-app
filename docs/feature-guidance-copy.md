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

**Look (chosen 2026-09-24, framed the same day):** Source Serif italic,
primary ink, a thin accent-coloured line on the left, small muted ×, on a
lightly framed eggshell panel (#FDFBF6, a shade over white) with a hairline border and a small pointer
up to what it describes, so it reads as floating above the page. No shadow
(design principles). Floats just below its anchor rather than pushing content
down.

**Form:** small floating notes anchored next to the thing they describe.
They close when tapped away or when the feature is used. Never shown over a
question in progress. At most one new note per day, apart from the handful
inside the first lesson.

---

## 1. First open

Replaces the current Home welcome card (language picker + philosophy
paragraph + three buttons). No tour, no room list.

**1a. Opening screen**
- Text: A place to learn a language properly, at your own pace.
- Then: What would you like to learn? — Spanish · Hungarian

**1a-ii. Which Spanish** (only if Spanish was picked)
- Text: Which Spanish?
- Buttons: Latin America · Spain

**1b. Starting point**
- Two buttons, no question or caption above them:
  Start from the beginning · Find my level
- "Find my level" goes straight to the short placement test.

## 2. The first lesson

Only notes in this section may appear several in one day.

**2a. Listen**
- Trigger: first speaker button
- Text: Tap to hear it read aloud.

**2b. Tap a word**
- Trigger: first reading passage
- Text: Tap any word to see what it means.

**2c. Missed answers**
- Trigger: first question answered after a wrong try, once it's done (a
  step revealed after three tries isn't queued again, so it gets no note)
- Text: Anything you miss comes back at the end.

## 3. End of the first lesson

**3a. Invitation (end-of-lesson screen)**
- Text: {n} new words are in your deck, ready for a short review.
  (Changed from "Tomorrow they'll come back…": new cards are due at once.)
- Buttons: See your deck · Next lesson

**3b. Arriving in Decks**
- Text: Words from your lessons collect here. There's no need to make cards yourself.

## 4. Day 2

**4a. First review card**
- Text: Words come back less often as you get them right.

## 5. First speaking or writing task

- Text: There's no single right answer here. You'll get notes on what worked and what to adjust.

*(Note: The old per-lesson end-of-lesson invitations — `invite-decks`, `invite-library`, `invite-verb-driller`, `invite-listening-driller`, `invite-workshop` — were superseded by Home's recommendation engine and removed from `engine/guide.js`.)*

## 6. Later, when useful

These appear only when there's a reason, at most one per day.

**6a. My Texts**
- Trigger: reaching A2, or five Library stories read
- Where: Library, next to the My Texts tab
- Text: Import an EPUB, Word doc, or text file — or paste anything in — and look up words the same way.

**6b. Known words (graduated from review)**
- Trigger: a word graduates out of review on its own (it was answered right often enough)
- Where: the review session summary
- Text: Words you know well graduate out of review as known. Find them anytime in All my words.

**6c. Grammar Guide**
- Trigger: first time a learner reopens a finished lesson
- Where: unit page, next to the Grammar Guide link
- Text: Every unit's grammar is collected here, in case you want to look something up.

**6d. Import flashcards**
- Trigger: third visit to Decks
- Where: next to Import
- Text: If you have flashcards elsewhere, you can import them from Quizlet, Anki, Memrise or a spreadsheet.

**6e. Streak import**
- Trigger: first visit to Journey
- Where: next to the streak
- Text: If you're coming from another app, you can bring your streak with you.

## 7. For reference

"About Parlour" (`Guide.openOverviewModal()` in `engine/guide.js`) stays reachable from Home's footer and the sidebar footer.

The drillers' "About this drill" info (`engine/drillInfo.js`) stays in the plain, second-person voice ("what this trains, why it might feel strange at first, what getting better looks like").
