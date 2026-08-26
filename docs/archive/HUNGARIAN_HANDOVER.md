# Hungarian: Handover for Verb Driller + Library (Reader/Lexicon) Work

Written 2026-08-18 to start a fresh session on either of these two tasks
without re-deriving context from scratch. Read this first, then the
task-specific doc it points you to.

## Where things stand right now

- Latest commit: `ba87fa6` ("Audit and close the app's remaining
  Spanish-only assumptions"), pushed to `origin/master`. Everything below
  is current as of that commit.
- **A second agent may be concurrently editing Spanish-only content**
  (`content/es/exercises/`, `content/es/grammar/`, `imports/dictionary/`) as
  part of an unrelated project on the Spanish track. If you see uncommitted
  changes in those paths that you didn't make, they aren't yours to commit —
  leave them alone and stage only what you actually touched (see
  `commit-directly-to-master` in memory for the staging convention this repo
  uses).
- Hungarian A1 Unit 1 is live: 5 lessons (`content/hu/lessons/a1/a1-01.json`
  … `a1-05.json`), selectable via a Course dropdown at the top of My Journey
  (`Lang.available()` in `engine/lang.js` — currently `['es', 'hu']`).
- Three other documents already exist in repo root; don't duplicate their
  content, read them:
  - `HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md` — the actual spec for the
    Library/Lexicon task below. Start there for that task, not here.
  - `MULTI_LANGUAGE_READINESS_AUDIT.md` — everything already confirmed
    language-safe or already fixed elsewhere in the app. Skim it so you
    don't re-discover things already handled.
  - `content/hu/HU_Content_Authoring_Template.md` — how Hungarian lesson
    *content* (not code) gets authored. Not directly relevant to either
    task below, but explains the shape of `content/hu/` if you need it.

## Task 1: Hungarian Verb Driller

**Read `HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md` first anyway** even though
it's titled "Reader" — its lightweight-runtime principle (heavy tooling at
build time, small static data in the browser, no NLP stack shipped to
users) applies here too, and its "do not over-engineer the first version"
framing is exactly the right posture for this task as well.

**Why this is a rewrite, not a config swap** (already flagged in
`multi-language-plan` memory, confirmed concretely by inspecting the data):
Spanish's `imports/verbs/*.json` (654 files, one per verb) shapes each entry
as `mood → tense → person`, where person is Spanish's six slots
(yo/tú/usted/nosotros/vosotros/ustedes). Hungarian conjugation has a
structurally different shape:

- **Definite vs. indefinite conjugation** — a whole second paradigm per
  tense depending on whether the verb's object is definite, with no Spanish
  analogue at all. This doubles the table shape, it doesn't just relabel it.
- Different person set (én/te/ő/mi/ti/ők), no formal/informal split the way
  tú/usted works.
- No grammatical gender anywhere in the system (contrast Spanish, where
  `engine/lexicon.js`'s `article()`/`withArticle()` exist specifically
  because Spanish nouns carry el/la).
- Different tense/mood inventory than Spanish's indicativo/subjuntivo/imperative.

**Where the Spanish implementation lives**, as your model to diverge from —
inspect these before designing anything, the way Phase 1 of the Reader
brief asks you to for the Lexicon:

- `imports/verbs/*.json` — one file per verb, the data shape described above.
- `imports/verbs/verb-list.js` — a plain global script (not `Lang.content()`-scoped;
  see the audit doc's "Confirmed already correct" vs. "Still open" split —
  this one is correctly *not* touched yet, on purpose, until this rewrite happens).
- `engine/verbs.js` — the driller shell (mode switching, settings).
- `engine/verbs/table.js`, `engine/verbs/speed.js`, `engine/verbs/stats.js` —
  the two modes (conjugation table, timed speed drill) and scoring.
- `styles/verbs.css` — already generic/reusable; unlikely to need
  Hungarian-specific changes, but check once real content renders.
- `scripts/import_verbs.py`, `scripts/build_verb_list.py`,
  `scripts/build_verb_index.py` — the Spanish build pipeline that produces
  the files above, useful as a template for an equivalent Hungarian pipeline,
  not something to extend in place.

**Current gate to remove once this is real:** `engine/workshop.js`'s
`DRILLERS` array has `{ id: 'verbs', ..., langs: ['es'] }` — added this
session specifically so a Hungarian learner doesn't see a Verb Driller
silently full of Spanish conjugation. Once Hungarian verb data and a
Hungarian-aware `engine/verbs.js` exist, either drop the `langs` field or
add `'hu'` to it.

**Suggested first step:** inspect a handful of Hungarian verbs' actual
conjugation patterns (regular -ik vs. non-ik verbs, at minimum), sketch the
JSON shape for one verb by hand, and confirm it can drive
`engine/verbs/table.js` with only the changes the different shape actually
requires — before generating data for all of them.

## Task 2: Library function (Reader/Lexicon)

This is `HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md` in full — that document
*is* the spec, don't re-derive it here. Two corrections layered on top of it
during this session, already folded into the brief itself, but worth
repeating since they reverse what might seem like the obvious reading:

1. **Coverage can't be scoped to curriculum vocabulary.** Library's My
   Texts feature lets a learner paste *any* Hungarian text, which runs
   through this same Lexicon. A dictionary sized to the ~150 words across
   Unit 1 (or even all 30 planned A1 lessons) would return "not in the
   dictionary yet" for most of anything a learner actually pastes. The
   dictionary/lemma layer needs coverage close to Spanish's
   (`imports/dictionary/spanish-en.json`, ~110k entries), not a curriculum-sized
   list. Curriculum can only constrain which morphological *labels* get
   surfaced by default early on.
2. **This isn't only the Lexicon.** `engine/drills/grammar.js`,
   `translation.js`, `listening.js`, and `vocabulary.js` all fetch
   `generated/indexes/*.json` from the same kind of hardcoded top-level path
   the Lexicon uses. It's one fix across five files, not five separate
   ones — see the brief's "Wider scope" section for the exact table and the
   recommended `content/<lang>/indexes/...` relocation.

**Suggested first step** (this session got this far, stopped before
installing anything): prototype with HuSpaCy (`pip install huspacy`, a
Hungarian CNN model, not the transformer one — faster to iterate with)
against the brief's own test list (`ház`, `házamban`, `barátaimmal`,
`olvastam`, etc.) and look at the raw morphological output before deciding
the final index shape. Real network access to GitHub/PyPI was confirmed
available in this environment during that investigation.

## One shared piece of infrastructure both tasks touch

Both the generated-index relocation (Task 2) and a Hungarian verb data
pipeline (Task 1) end up needing the same kind of thing: a per-language
subtree under `content/hu/` that a build script writes into and
`Lang.content()` reads back from. If you pick up Task 2 first, the
`content/<lang>/indexes/...` convention it establishes is worth reusing for
Task 1's verb data too, rather than inventing a second convention.
